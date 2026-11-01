"""Runs the reciprocity-gate analyses of models/gate_reciprocity_bitcoin.py on the SNAP Bitcoin OTC and Alpha files and
writes sim/results/gate_reciprocity_bitcoin.md.

    cd sim
    ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report fetch    # once; checks sha256, git-ignored
    ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report report   # about three minutes, seeded; --pickle f saves the numbers
    ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report render f # re-render the text from a pickle, nothing recomputed
    ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report check    # data integrity only

Every number in the results file is computed here, from the files, with fixed seeds.  The prose that states what the
numbers mean is written by hand around them; before the file is written, `guards()` asserts the facts that prose relies
on (a sign, an ordering, a p-value bound), so a re-run that changes the picture refuses to write a stale verdict.
"""
from __future__ import annotations

import argparse
import datetime
import sys
import time
from pathlib import Path

import numpy as np

from models import gate_reciprocity_bitcoin as gb

RESULTS = gb.SIM_DIR / "results" / "gate_reciprocity_bitcoin.md"
SEED = 20261101
B_BOOT = 1000
CV_REPEATS = 5
MIN_STRATUM = 100


# ------------------------------------------------------------------ small formatting helpers

def f2(x, d=2, plus=False):
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "n/a"
    return f"{x:+.{d}f}" if plus else f"{x:.{d}f}"


def pm(est, se, d=2, plus=True):
    if est is None or se is None:
        return "n/a"
    return f"{f2(est, d, plus)} ({f2(se, d, False)})"


def pstr(p):
    """A p-value with its operator: '< 1e-10', '= 3e-05', '= 0.074'."""
    if p is None:
        return "n/a"
    if p < 1e-10:
        return "< 1e-10"
    if p < 1e-3:
        return f"= {p:.0e}"
    return f"= {p:.3f}"


def ci(lo, hi, d=2, plus=False):
    return f"[{f2(lo, d, plus)}, {f2(hi, d, plus)}]"


def pct(x, d=1):
    return "n/a" if x is None else f"{100 * x:.{d}f}%"


def bin_label(b):
    return f"{b[0]}" if b[0] == b[1] else f"{b[0]}..{b[1]}"


def form_name(key):
    fam, shape = key
    return gb.form_label(fam, shape)


def q(arr, lo=2.5, hi=97.5):
    a = np.asarray(arr, dtype=float)
    return float(np.percentile(a, lo)), float(np.percentile(a, hi))


# ------------------------------------------------------------------ the computation

def platform_block(S: gb.Sample, B: int, seed: int, cv_repeats: int) -> dict:
    D = gb.sample_fe(S)
    out: dict = dict(n_pairs=S.n, n_fe=D.n, n_responders=int(len(np.unique(D.resp))), gap=gb.gap_summary(S))
    out["curve"] = gb.curve_table(S, fe=True)
    out["curve_raw"] = gb.curve_table(S, fe=False)
    out["flat"] = gb.flatness_tests(S)
    out["increments"] = gb.increment_test(S)
    out["copy"] = gb.copy_excess(S, seed=seed)
    out["habit"] = gb.habit_offset_table(S)
    out["sign"] = gb.sign_margin(S)
    out["wald_any"] = gb.wald_any_response(S)
    out["profile"] = gb.profile_summary(D)
    out["habit_mean"] = (float(np.nanmean(S.habit_resp_all)), float(np.nanmedian(S.habit_resp_all)))
    out["alt_se"] = gb.profile_alt_se(D)
    # forms: in-sample and cross-validated, responder fixed effects
    eng = gb.Engine(D.x, D.y, [gb.contiguous(D.resp)])
    fits = eng.fit_all(gb.PRESPEC_FORMS + gb.EXPLORATORY_FORMS)
    out["fits"] = fits
    out["null_rss"] = fits[("null", None)].rss
    cv = gb.cv_losses(D.x, D.y, D.resp, K=10, repeats=cv_repeats, seed=seed)
    out["cv"] = {k: float(np.nanmean(v)) for k, v in cv.items() if isinstance(k, tuple)}
    out["cv_n"] = cv["n_scored"]
    pre = [k for k in out["cv"] if k[0] not in gb.EXPLORATORY_NAMES and k[0] != "saturated"]
    best = min(pre, key=lambda k: out["cv"][k])
    out["cv_best_prespec"] = best
    out["cv_diff"] = {k: gb.paired_diff(cv[k], cv[best], D.resp) for k in out["cv"]}

    def pdiff(a, b):
        d, se = gb.paired_diff(cv[a], cv[b], D.resp)
        return d, se

    out["cv_pairs"] = {
        "D-step vs T-graded": pdiff(("D", "step"), ("T", "graded")),
        "D-step vs D-graded": pdiff(("D", "step"), ("D", "graded")),
        "T-graded vs D-graded": pdiff(("T", "graded"), ("D", "graded")),
        "linear vs T-graded": pdiff(("linear", None), ("T", "graded")),
        "T-step vs T-graded": pdiff(("T", "step"), ("T", "graded")),
        "T-hinge (flat over {-1, +1}) vs T-graded": pdiff(("T", "hinge"), ("T", "graded")),
        "O+ graded vs T-graded": pdiff(("O+", "graded"), ("T", "graded")),
        "O- graded vs T-graded": pdiff(("O-", "graded"), ("T", "graded")),
        "D-graded vs clipped mirror + jump": pdiff(("D", "graded"), ("jump+clip", None)),
        "T-graded vs clipped mirror + jump": pdiff(("T", "graded"), ("jump+clip", None)),
        "clipped mirror + jump vs saturated": pdiff(("jump+clip", None), ("saturated", None)),
        "D-graded vs no-band two slopes": pdiff(("D", "graded"), ("knee2", None)),
        "T-graded vs no-band two slopes": pdiff(("T", "graded"), ("knee2", None)),
        "no-band two slopes vs saturated": pdiff(("knee2", None), ("saturated", None)),
    }
    out["dprofile"] = {sh: gb.profile_rss_by_kp(D, sh) for sh in ("step", "graded")}
    out["knee2_k2_rss"] = eng.fit_cols("knee2_at_2", None, ["Ph1", "Ph2", "Ns1", "Nh1"]).rss
    out["knee2_profile"] = {K: eng.fit_cols("knee2", None, ["Ph1", f"Ph{K}", "Ns1", "Nh1"], None, (K,), 1) for K in range(2, 10)}
    out["boot"] = gb.bootstrap_forms(D, B=B, seed=seed)
    # drift
    out["years"] = gb.year_table(S, min_n=MIN_STRATUM)
    ok_years = [r["year"] for r in out["years"] if "est" in r]
    yy = S.subset(np.isin(S.year, ok_years))
    Dy = gb.sample_fe(yy)
    out["trend"] = gb.trend_test(Dy, Dy.year.astype(float))
    out["trend_years"] = ok_years
    out["year_trend"] = {nm: gb.year_trend(out["years"], nm) for nm in gb.PROFILE_NAMES}
    # strata
    out["emb_prior"] = _strata(S, _emb_labels(S.emb_prior), EMB_ORDER)
    out["emb_static"] = _strata(S, _emb_labels(S.emb_static), EMB_ORDER)
    out["gap_strata"] = _strata(S, _gap_labels(S.gap), None)
    # control specifications
    out["specs"] = {sp: gb.spec_summary(S, sp) for sp in ("raw", "fe", "fe2", "cov_all", "cov_prior", "fe_inertia")}
    out["signal"] = gb.signal_coding_cv(S, repeats=cv_repeats, seed=seed)
    # reversal placebo
    Rv = S.reversed()
    Dr = gb.sample_fe(Rv)
    out["rev_profile"] = gb.profile_summary(Dr)
    out["rev_curve"] = gb.curve_table(Rv)
    engr = gb.Engine(Dr.x, Dr.y, [gb.contiguous(Dr.resp)])
    fr = engr.fit_all(gb.PRESPEC_FORMS + gb.EXPLORATORY_FORMS)
    out["rev_r2"] = {k: 1 - v.rss / fr[("null", None)].rss for k, v in fr.items()}
    out["rev_n"] = Dr.n
    # capped responders
    C = gb.sample_fe(gb.cap_per_responder(S, 3, seed))
    out["capped"] = (C.n, gb.profile_summary(C))
    return out


EMB_ORDER = ["0", "1-2", "3-9", "10+"]


def exact_copy_shares(S: gb.Sample) -> dict:
    """Share of responses that repeat the received rating exactly: all, within ten minutes, a day or more later, and the same
    three for received ratings above +1 (where chance, given a habit of +1, cannot produce it)."""
    same = S.y == S.x
    g = S.gap
    out = {}
    for lab, m in (("all", np.ones(S.n, bool)), ("within10", g < 600), ("after1d", g >= 86400)):
        out[lab] = (int(m.sum()), float(same[m].mean()) if m.any() else None)
        m2 = m & (S.x > 1)
        out[lab + "_above1"] = (int(m2.sum()), float(same[m2].mean()) if m2.any() else None)
    return out


def _emb_labels(e):
    return np.array(["0" if v == 0 else "1-2" if v <= 2 else "3-9" if v <= 9 else "10+" for v in e])


def _gap_labels(gap):
    return np.array(["a: < 10 min" if v < 600 else "b: 10 min - 1 d" if v < 86400 else "c: 1 d - 30 d" if v < 30 * 86400 else "d: > 30 d"
                     for v in gap])


def _strata(S: gb.Sample, labels: np.ndarray, order) -> dict:
    D = gb.sample_fe(S)
    lab = labels[gb.fe_mask(S.resp)]
    res = gb.stratified_profile(D, lab, min_n=MIN_STRATUM, order=order)
    tests = {nm: gb.strata_equal(res, nm) for nm in gb.PROFILE_NAMES}
    params = {l: {nm: gb.strata_param(res, l, nm) for nm in gb.PROFILE_NAMES} for l in res["labels"]}
    return dict(labels=res["labels"], n_by=res["n_by"], too_small=res["too_small"], params=params, tests=tests)


def analyse(B: int = B_BOOT, seed: int = SEED, cv_repeats: int = CV_REPEATS, log=print) -> dict:
    t0 = time.time()
    R = {k: gb.load_ratings(k) for k in ("otc", "alpha")}
    PS = {k: gb.pair_structure(R[k]) for k in R}
    S, info = {}, {}
    for k in R:
        S[k], info[k] = gb.build_sample(R[k], PS[k])
    T = gb.tied_sample(R["alpha"], PS["alpha"], seed=seed)
    res: dict = dict(info=info, seed=seed, B=B, cv_repeats=cv_repeats)
    res["share_plus1"] = {k: float((R[k].rating == 1).mean()) for k in R}
    res["exact_copy"] = {k: exact_copy_shares(S[k]) for k in S}
    res["opposite_sign"] = {}
    for k in R:
        # reciprocated pairs carrying opposite signs (112 section 6.5 test 4): count over all reciprocated pairs
        rev = PS[k].rev
        i = np.flatnonzero((rev >= 0) & (np.arange(R[k].n) < rev))
        res["opposite_sign"][k] = (int((R[k].rating[i] * R[k].rating[rev[i]] < 0).sum()), int(len(i)))
    for k in S:
        log(f"[{time.time() - t0:6.1f}s] platform block {k}")
        res[k] = platform_block(S[k], B, seed, cv_repeats)
    # like-for-like platform comparisons and the unordered Alpha pairs
    log(f"[{time.time() - t0:6.1f}s] platform comparisons")
    comps = {}
    O = S["otc"]
    for label, smp in (("OTC, gap >= 1 day", O.subset(O.gap >= 86400)), ("OTC, gap < 1 day", O.subset(O.gap < 86400)),
                       ("Alpha, ordered (gap >= 1 day)", S["alpha"]), ("Alpha, same-day pairs (random orientation)", T)):
        D = gb.sample_fe(smp)
        comps[label] = gb.profile_summary(D) | dict(curve=gb.curve_table(smp))
    res["platform"] = comps
    res["tied_n"] = T.n
    # copy excess by gap (OTC)
    res["copy_by_gap"] = {}
    for label, lo, hi in (("< 1 min", 0, 60), ("1-10 min", 60, 600), ("10 min - 1 h", 600, 3600), ("1 h - 1 d", 3600, 86400),
                          ("1 d - 30 d", 86400, 30 * 86400), ("> 30 d", 30 * 86400, 1e12)):
        m = (O.gap >= lo) & (O.gap < hi)
        res["copy_by_gap"][label] = (int(m.sum()), gb.copy_excess(O.subset(m), xs=(1, 2, 3), B=200, seed=seed))
    # extensive margin
    log(f"[{time.time() - t0:6.1f}s] extensive margin")
    res["ext"] = {w: gb.response_rates(R["otc"], PS["otc"], w) for w in (1.0, 30.0)}
    res["elapsed"] = time.time() - t0
    return res


def multiple_comparisons(res: dict) -> dict:
    """The load-bearing tests against a Bonferroni correction (added at review, 2026-11-01): the flatness rejections the
    verdict uses, across every flatness test run (both platforms), and the D-step against T-graded comparison across the
    paired comparisons of one platform."""
    from scipy import stats
    O, A = res["otc"], res["alpha"]
    lab = [t[0] for t in gb.FLAT_TESTS]
    used = [(O, lab[0]), (O, lab[2]), (O, lab[4]), (A, lab[0]), (A, lab[2])]       # {+1,+2}, {+1..+4} both; OTC {-1,+1}
    flat_p_max = max({r["label"]: r for r in blk["flat"]}[l]["p"] for blk, l in used)
    n_flat = sum(1 for blk in (O, A) for r in blk["flat"] if r["p"] is not None)
    dst = {k: res[k]["cv_pairs"]["D-step vs T-graded"] for k in ("otc", "alpha")}
    dst_p = {k: float(2 * stats.norm.sf(abs(d / se))) for k, (d, se) in dst.items()}
    return dict(flat_p_max=float(flat_p_max), n_flat=n_flat, dst_p=dst_p, n_pairs=len(O["cv_pairs"]))


# ------------------------------------------------------------------ guards: facts the written verdict relies on

def guards(res: dict) -> list[str]:
    """Assertions on the computed numbers.  Each returns a short description when it holds; a failure raises
    AssertionError naming the sentence of the verdict that is no longer true."""
    ok: list[str] = []
    O, A = res["otc"], res["alpha"]

    def need(cond, msg):
        assert cond, "VERDICT GUARD FAILED: " + msg
        ok.append(msg)

    fl = {r["label"]: r for r in O["flat"]}
    fa = {r["label"]: r for r in A["flat"]}
    k12 = gb.FLAT_TESTS[0][0]
    k14 = gb.FLAT_TESTS[2][0]
    ks = gb.FLAT_TESTS[4][0]
    need(fl[k12]["p"] < 1e-10 and fl[k12]["est"][0] > 0.5, "OTC: flatness over {+1, +2} rejected (p < 1e-10), +2 above +1")
    need(fa[k12]["p"] < 1e-3 and fa[k12]["est"][0] > 0.5, "Alpha: flatness over {+1, +2} rejected (p < 1e-3), +2 above +1")
    need(fl[k14]["p"] < 1e-10 and fa[k14]["p"] < 1e-10, "both platforms: flatness over {+1, ..., +4} rejected (p < 1e-10)")
    need(fl[ks]["p"] < 1e-3 and fl[ks]["est"][0] < -1, "OTC: the mildest negative rating (-1) is far below +1 (the negative side has no dead zone)")
    # review 2026-11-01: the verdict now says Alpha's band {-1, +1} is NOT rejected, and that no excess step sits on a line
    need(fa[ks]["p"] > 0.05, "Alpha: the symmetric band {-1, +1} is not rejected (a thin cell; the verdict says so)")
    for lab, blk in (("OTC", O), ("Alpha", A)):
        it = blk["increments"]
        need(it["p"] is not None and it["p"] > 0.05, f"{lab}: no excess step on top of a line over +1..+4 (equal increments not rejected)")
        need(it["inc45"] is not None and it["inc45"] < min(it["inc"]), f"{lab}: the increment from +4 to +5 is smaller than every increment over +1..+4 (no step at +5)")
    d, se = O["cv_pairs"]["T-hinge (flat over {-1, +1}) vs T-graded"]
    need(d / se > 3, "OTC: the hinge's narrowest band (flat over {-1, +1}) loses to the same form with a sign jump by more than 3 SE")
    d, se = O["cv_pairs"]["D-step vs T-graded"]
    need(d / se > 3, "OTC: the literal O-jive (D, step) is worse out of sample than the no-band graded form by more than 3 SE")
    d, se = A["cv_pairs"]["D-step vs T-graded"]
    need(d / se > 2, "Alpha: the literal O-jive (D, step) is worse out of sample than the no-band graded form by more than 2 SE")
    d, se = O["cv_pairs"]["linear vs T-graded"]
    need(d > 0, "OTC: a sign jump plus separate slopes beats a single line out of sample")
    d, se = O["cv_pairs"]["D-graded vs clipped mirror + jump"]
    need(abs(d / se) < 2, "OTC: the dead-zone graded form is not distinguishable from the no-band clipped mirror (|z| < 2)")
    d, se = A["cv_pairs"]["D-graded vs clipped mirror + jump"]
    need(abs(d / se) < 2, "Alpha: the dead-zone graded form is not distinguishable from the no-band clipped mirror (|z| < 2)")
    d, se = A["cv_pairs"]["T-graded vs D-graded"]
    need(abs(d / se) < 2, "Alpha: freeing the band does not improve on closing it (|z| < 2)")
    for lab, blk in (("OTC", O), ("Alpha", A)):
        d, se = blk["cv_pairs"]["D-graded vs no-band two slopes"]
        need(d / se > -2, f"{lab}: a no-band two-slope curve is not worse out of sample than the dead-zone graded fit (difference > -2 SE)")
        kk, dd = blk["fits"][("knee2", None)], blk["fits"][("D", "graded")]
        need(kk.rss < dd.rss and kk.ic("bic") < dd.ic("bic"), f"{lab}: the no-band two-slope curve beats the dead-zone graded fit in residual sum of squares and in BIC, with one threshold instead of two")
    for lab, blk in (("OTC", O), ("Alpha", A)):
        for nm in ("no-band two slopes vs saturated", "clipped mirror + jump vs saturated"):
            d, se = blk["cv_pairs"][nm]
            need(abs(d / se) < 1.0, f"{lab}: {nm} is within one SE out of sample")
    need(O["fits"][("D", "graded")].cand.kp == 2 and abs(O["knee2_k2_rss"] - O["fits"][("D", "graded")].rss) < 1e-6 * O["fits"][("D", "graded")].rss,
         "OTC: the dead-zone graded fit with the one-rating band is the same function class as a no-band two-slope curve with its knee at +2 (equal RSS)")
    for nm in ("O+ graded vs T-graded", "O- graded vs T-graded"):
        for lab, blk in (("OTC", O), ("Alpha", A)):
            d, se = blk["cv_pairs"][nm]
            need(d / se > 3, f"{lab}: {nm} (one-sided) loses to the two-sided form by more than 3 SE")
    tb = O["boot"]
    dg = gb.threshold_distribution(tb["thr"][("D", "graded")])
    need(dg["kp"].get(2, 0) >= 0.9 and dg["kn"].get(1, 0) >= 0.9, "OTC: the dead-zone graded fit puts the band at the single rating +1 (K+ = 2, K- = 1) in >= 90% of draws")
    dh = gb.threshold_distribution(tb["thr"][("D", "hinge")], "hinge")
    need(dh["narrowest"] >= 0.9, "OTC: the continuous (hinge) dead-zone form takes its narrowest band, knots +1 and -1 (flat over {-1, +1}), in >= 90% of draws")
    ds = gb.threshold_distribution(tb["thr"][("D", "step")], "step")
    need(ds["empty"] == 0 and sum(v for k, v in ds["kp"].items() if k >= 3) >= 0.9, "OTC: the literal O-jive places K+ at 3 or higher in >= 90% of draws (a step standing in for a ramp)")
    pr, pa = O["profile"], A["profile"]
    need(pr["est"]["slope14"] > 0.6 and pr["est"]["neg"] < -5, "OTC: slope over ratings 1-4 above 0.6 per point; negative received rating shifts the response by more than 5 points")
    need(pa["est"]["slope14"] > 0.4 and pa["est"]["neg"] < -4, "Alpha: the same signs and orders of magnitude")
    hb = {r["x"]: r for r in O["habit"]}
    need(abs(hb[1]["mean"]) < 0.2 and hb[2]["mean"] > 0.5, "OTC: against the responder's own habit, +1 is the zero-influence point and +2 is already above it")
    for key in ("resp", "first", "two_way"):
        need(O["alt_se"][key]["slope14"] < 1.3 * O["alt_se"]["resp"]["slope14"], f"OTC: slope SE clustered by {key} is within 30% of the responder-clustered SE")
    # drift
    # review 2026-11-01: the pooled SE ignores year-to-year scatter; only claims that survive it are made
    yo = O["year_trend"]
    need(O["trend"]["slope14"][0] / O["trend"]["slope14"][1] > 2 and yo["slope14"]["slope"] / yo["slope14"]["se_infl"] > 2 and yo["slope14"]["p_lof"] > 0.05,
         "OTC: the 1-4 slope rises over 2011-2015 (pooled trend t > 2; on the yearly estimates z > 2 with no lack of fit)")
    for nm in ("neg", "hi910"):
        need(yo[nm]["p_lof"] < 0.05 and abs(yo[nm]["slope"] / yo[nm]["se_infl"]) < 2,
             f"OTC: {nm} is not linear in year and has no trend that survives the year-to-year scatter (|z| < 2)")
    need(all(r["shift2"] / r["se2"] > 3 for r in O["years"] if "shift2" in r), "OTC: in every estimable year +2 is above +1 by more than 3 SE")
    need(all(r["shift2"] > 0 for r in A["years"] if "shift2" in r), "Alpha: in every estimable year +2 is above +1")
    need(all(r["d_graded"] == (2, 1) for r in O["years"] if "d_graded" in r), "OTC: the graded dead-zone fit is the one-rating band in every estimable year")
    # variations
    sg = O["signal"]
    need(sg["mse"]["u bins (saturated in u)"] > sg["mse"]["x bins (saturated in x)"] + 3 * sg["diff"]["u bins (saturated in u)"][1], "OTC: the level of the received rating predicts better than its deviation from the sender's habit")
    need(O["rev_profile"]["est"]["neg"] > pr["est"]["neg"] + 2, "OTC: the negative jump is much smaller in the time-reversed regression (asymmetry)")
    need(O["sign"]["p_neg_after_neg"] > 0.8 > 0.6 > O["sign"]["p_neg_before_neg"], "OTC: a negative first rating is answered negatively > 80% of the time, but < 60% of negative responses followed a negative rating")
    ptf = res["platform"]
    a1, a2 = ptf["OTC, gap >= 1 day"], ptf["Alpha, ordered (gap >= 1 day)"]
    need(abs(a1["est"]["slope14"] - a2["est"]["slope14"]) < 2 * np.hypot(a1["se"]["slope14"], a2["se"]["slope14"]),
         "like-for-like (gap >= 1 day) the two platforms have the same 1-4 slope within 2 SE")
    for lab, blk in (("OTC", O), ("Alpha", A)):
        t = blk["gap_strata"]["tests"]["slope14"]
        need(t is not None and t[2] > 0.05, f"{lab}: the 1-4 slope does not differ across gap strata (p > 0.05)")
    cg = {k: v[1] for k, v in res["copy_by_gap"].items()}
    need(cg["< 1 min"][0]["pi"] > 0.6 and cg["> 30 d"][0]["pi"] < 0, "OTC: copying at +1 is high within a minute (> 0.6) and negative after 30 days")
    ex = {r["bin"]: r for r in res["ext"][30.0]}
    ex1 = {r["bin"]: r for r in res["ext"][1.0]}
    need(ex[(-10, -10)]["rate"] < 0.15 and ex[(1, 1)]["rate"] > 0.6, "OTC: a negative received rating is answered by a rating in <15% of cases, a +1 in >60% (30 days)")
    need(abs(ex1[(1, 1)]["rate"] - ex1[(2, 2)]["rate"]) < 0.03 and ex1[(10, 10)]["rate"] < ex1[(2, 2)]["rate"] - 0.2, "OTC: the answering rate is flat over +1 and +2 and falls by more than 20 points by +10 (1 day)")
    for lab, blk in (("OTC", O), ("Alpha", A)):
        need(abs(blk["specs"]["raw"]["est"]["slope14"] - blk["specs"]["fe"]["est"]["slope14"]) < 0.1, f"{lab}: pooled and fixed-effects 1-4 slopes agree within 0.1")
    mn = min(blk[k]["params"][l]["slope14"][0] for blk in (O, A) for k in ("emb_prior", "emb_static") for l in blk[k]["labels"] if blk[k]["params"][l]["slope14"])
    need(mn > 0.2, "no embeddedness bin has a 1-4 slope below 0.2")
    xo = res["opposite_sign"]
    need(all(a / b < 0.04 for a, b in xo.values()), "opposite-sign reciprocated pairs are below 4% on both platforms")
    mc = multiple_comparisons(res)
    need(mc["flat_p_max"] * mc["n_flat"] < 0.05, "the verdict's flatness rejections survive a Bonferroni correction over every flatness test")
    need(mc["dst_p"]["otc"] * mc["n_pairs"] < 0.05, "OTC: D-step against T-graded survives a Bonferroni correction over the platform's paired comparisons")
    return ok


# ------------------------------------------------------------------ rendering

def _keep_review(text, path):
    """`text` with a hand-written '## Review (' section at the end of the existing file at `path` kept, so
    regenerating the numbers does not delete a review of them."""
    p = Path(path)
    if p.exists():
        old = p.read_text(encoding="utf-8")
        i = old.find("\n## Review (")
        if i >= 0:
            return text.rstrip("\n") + "\n" + old[i:]
    return text


def render(res: dict) -> str:
    O, A = res["otc"], res["alpha"]
    info = res["info"]
    L: list[str] = []
    add = L.append

    def table(header, rows, align=None):
        add("| " + " | ".join(header) + " |")
        al = align or ["---"] * len(header)
        add("| " + " | ".join(al) + " |")
        for r in rows:
            add("| " + " | ".join(str(c) for c in r) + " |")
        add("")

    fo = {r["label"]: r for r in O["flat"]}
    fa = {r["label"]: r for r in A["flat"]}
    k12 = gb.FLAT_TESTS[0][0]
    k14 = gb.FLAT_TESTS[2][0]
    ks = gb.FLAT_TESTS[4][0]
    po, pa = O["profile"], A["profile"]
    bo, ba = O["boot"], A["boot"]
    prof_ci = {nm: q(bo["profile"][:, i]) for i, nm in enumerate(gb.PROFILE_NAMES)}
    prof_ci_a = {nm: q(ba["profile"][:, i]) for i, nm in enumerate(gb.PROFILE_NAMES)}
    hb = {r["x"]: r for r in O["habit"]}
    sm, sa_ = O["sign"], A["sign"]
    cp = {r["x"]: r for r in O["copy"]}
    cpa = {r["x"]: r for r in A["copy"]}
    ku, kua = bo["knee"], ba["knee"]
    knee_med, knee_ci = int(np.median(ku)), (int(np.percentile(ku, 2.5)), int(np.percentile(ku, 97.5)))
    kud = {int(k): float((ku == k).mean()) for k in np.unique(ku)}
    dgo = gb.threshold_distribution(bo["thr"][("D", "graded")], "graded")
    dso = gb.threshold_distribution(bo["thr"][("D", "step")], "step")
    dho = gb.threshold_distribution(bo["thr"][("D", "hinge")], "hinge")
    dga = gb.threshold_distribution(ba["thr"][("D", "graded")], "graded")
    dsa = gb.threshold_distribution(ba["thr"][("D", "step")], "step")
    dha = gb.threshold_distribution(ba["thr"][("D", "hinge")], "hinge")
    cvp, cva = O["cv_pairs"], A["cv_pairs"]
    xo = res["opposite_sign"]
    ext1 = {r["bin"]: r for r in res["ext"][1.0]}
    ext30 = {r["bin"]: r for r in res["ext"][30.0]}
    tr = O["trend"]
    gp = O["gap"]
    o_info, a_info = info["otc"], info["alpha"]
    yrs = {r["year"]: r for r in O["years"]}
    yrs_a = {r["year"]: r for r in A["years"]}
    est_years = [y for y, r in yrs.items() if "est" in r]
    est_years_a = [y for y, r in yrs_a.items() if "est" in r]
    hi910_peak = max(est_years, key=lambda y: yrs[y]["est"]["hi910"])
    pair_share_o = o_info["n_pairs_reciprocal"] / (o_info["n_ratings"] - o_info["n_pairs_reciprocal"])
    pair_share_a = a_info["n_pairs_reciprocal"] / (a_info["n_ratings"] - a_info["n_pairs_reciprocal"])
    zdiff = lambda c: c[0] / c[1]  # noqa: E731
    d_st = cvp["D-step vs T-graded"]
    d_stA = cva["D-step vs T-graded"]
    clipd = cvp["D-graded vs clipped mirror + jump"]
    ex_hi = ext1[(10, 10)]["rate"], ext30[(10, 10)]["rate"]
    n_m10_o = sm["n_m10"]
    k2o, k2a = O["fits"][("knee2", None)], A["fits"][("knee2", None)]
    dgo_fit, dga_fit = O["fits"][("D", "graded")], A["fits"][("D", "graded")]
    k2_dist = {pl: (int(np.median(blk["boot"]["knee2"])), int(np.percentile(blk["boot"]["knee2"], 2.5)), int(np.percentile(blk["boot"]["knee2"], 97.5)))
               for pl, blk in (("otc", O), ("alpha", A))}
    k2c = {pl: blk["cv_pairs"]["D-graded vs no-band two slopes"] for pl, blk in (("otc", O), ("alpha", A))}
    k2_slopes = O["knee2_profile"][2].coef[:2]
    sample_o_dropped = 1 - O["n_fe"] / O["n_pairs"]
    pname = {"slope14": "the 1-4 slope", "neg": "the negative jump", "hi910": "the 9-10 level"}
    yo, ya = O["year_trend"], A["year_trend"]
    zt = lambda d: d["slope"] / d["se_infl"]  # noqa: E731
    sig_a_tr = [nm for nm in ("slope14", "neg", "hi910") if ya[nm] and abs(zt(ya[nm])) > 1.96]
    alpha_trend_sentence = (f"On Alpha ({len(ya['slope14']['years'])} estimable years) the yearly estimates show a trend beyond 2 SE only for "
                            + ("; ".join(f"{pname[n]} ({pm(ya[n]['slope'], ya[n]['se_infl'])} per year)" for n in sig_a_tr) if sig_a_tr else "none of the three")
                            + ".")
    sig_a = [str(r["year"]) for r in A["years"] if "shift2" in r and r["shift2"] / r["se2"] > 1.96]
    inc_o, inc_a = O["increments"], A["increments"]
    se_sym_a = abs(fa[ks]["est"][0]) / np.sqrt(fa[ks]["chi2"])
    th_o, th_a = O["cv_pairs"]["T-hinge (flat over {-1, +1}) vs T-graded"], A["cv_pairs"]["T-hinge (flat over {-1, +1}) vs T-graded"]
    z2o = [r for r in O["curve"] if r["bin"] == (2, 2)][0]
    z2a = [r for r in A["curve"] if r["bin"] == (2, 2)][0]
    emb_cells = [(n_, k, l, blk[k]["params"][l]["slope14"], blk[k]["n_by"][l]) for n_, blk in (("OTC", O), ("Alpha", A)) for k in ("emb_prior", "emb_static")
                 for l in blk[k]["labels"] if blk[k]["params"][l]["slope14"]]
    emb_weak = [c for c in emb_cells if c[3][0] / c[3][1] < 3]
    emb_weak_txt = "; ".join(f"{c[0]}, {'static' if c[1] == 'emb_static' else 'time-respecting'} count, {c[2]} common neighbours, {c[4]} rows: {f2(c[3][0], 2)} (SE {f2(c[3][1], 2)})" for c in emb_weak)

    add("# A reciprocity gate on the Bitcoin OTC and Alpha trust networks: is there a dead zone?")
    add("")
    add(f"_Generated {datetime.date.today().isoformat()} by `uv run python -m models.gate_reciprocity_bitcoin_report report` (seed {res['seed']}, "
        f"{res['B']} cluster-bootstrap draws, {res['cv_repeats']} x 10-fold CV repeats, {res['elapsed']:.0f} s). Code: "
        "`sim/models/gate_reciprocity_bitcoin.py`, `sim/models/gate_reciprocity_bitcoin_report.py`; checks: "
        "`sim/tests/test_gate_reciprocity_bitcoin.py`. Ledger ids are lines of `docs/ledger.jsonl` (O-jive L0857, L0853, L0834, L4367; "
        "Bitcoin L4567-L4580; embeddedness L4825). Results are computed statistics only; the "
        "rating files are local-use-only and are not redistributed (`sim/data/README.md`)._")
    add("")
    add("**What was tested.** `models/00-v0.md` (v0.2; the law is v0.1's) writes the dyad influence as an O-jive (the influence function of Gottman, Swanson & Murray 1999, "
        "*J. Family Psychology* 13:3-19, doi:10.1037/0893-3200.13.1.3, as read in L0857): zero while the "
        "partner's level lies in a band [K-, K+], a bounded constant beyond each threshold, a function of the partner's LEVEL "
        "(sections 3 'D2' and 4.1). 112 section 6.2 carries dead-zone widths into the sign module. The prediction: where one trader "
        "rates another, the rating a trader GIVES back has a dead zone in the rating RECEIVED from that counterparty. The data are Bitcoin OTC "
        "and Alpha (117 section 3.4, L4567-L4580), 2010-2016: every ordered pair is rated once, "
        f"{pct(pair_share_o, 0)} of OTC pairs and {pct(pair_share_a, 0)} of Alpha pairs are rated in both directions.")
    add("")

    # ------------------------------------------------------------ verdict
    add("## Verdict")
    add("")
    add("**In short.**")
    add("")
    add(f"- **Dead zone in the response: refuted on OTC, and on Alpha for every band that reaches +2.** A dead zone is a flat response over a band of small received "
        f"ratings. On OTC the response is flat over no band that holds two observed ratings; on Alpha every band that reaches +2 is rejected, but the band {{-1, +1}} is not "
        f"({fa[ks]['n_min']} responses to a -1: {pm(fa[ks]['est'][0], se_sym_a, 1)} against +1, p {pstr(fa[ks]['p'])}). After a received +2 the response is "
        f"{f2(fo[k12]['est'][0], 2, True)} points above its level after a received +1 on OTC (chi2(1) = {fo[k12]['chi2']:.0f}, p {pstr(fo[k12]['p'])}) and "
        f"{f2(fa[k12]['est'][0], 2, True)} on Alpha (p {pstr(fa[k12]['p'])}); flatness over +1..+4 is rejected at p {pstr(fo[k14]['p'])} on OTC and p {pstr(fa[k14]['p'])} on Alpha. "
        f"The response climbs {f2(po['est']['slope14'], 2)} rating points per received point from the first point (OTC, 95% CI {ci(*prof_ci['slope14'])}; "
        f"Alpha {f2(pa['est']['slope14'], 2)} {ci(*prof_ci_a['slope14'])}). This refutes the dead zone as a property of the observed response. As a property of the INFLUENCE it needs one more "
        f"step, because a shared view of the deal (undecided, below) would add slope inside any band; but the O-jive's bounded step would then still show as an excess jump on top of a "
        f"linear slope, and none is seen between +1 and +4 (increments {', '.join(f2(v, 2, True) for v in inc_o['inc'])} on OTC, equal: chi2(2) = {inc_o['chi2']:.1f}, p {pstr(inc_o['p'])}; "
        f"Alpha {', '.join(f2(v, 2, True) for v in inc_a['inc'])}, p {pstr(inc_a['p'])}; the step from +4 to +5 is smaller, {f2(inc_o['inc45'], 2, True)} on OTC).")
    add(f"- **The O-jive as written fits worse than a graded response with no band.** With bounded constants beyond free thresholds (D, step) it loses out of "
        f"sample to the graded two-sided form with the band closed (T, graded) by {f2(d_st[0], 2)} squared rating points ({zdiff(d_st):.1f} SE) on OTC and "
        f"{f2(d_stA[0], 2)} ({zdiff(d_stA):.1f} SE) on Alpha. One-sided forms (positive-only, negative-only) lose by {f2(min(cvp['O- graded vs T-graded'][0], cva['O- graded vs T-graded'][0]), 1)} "
        f"to {f2(max(cvp['O+ graded vs T-graded'][0], cva['O+ graded vs T-graded'][0]), 1)}.")
    add(f"- **The best dead-zone fit finds a band of one rating, +1, and that band is concavity, not a zone.** With a graded response beyond the thresholds the fit puts "
        f"K- at -1 and K+ at +2 in {pct(dgo['kn'].get(1, 0), 0)} and {pct(dgo['kp'].get(2, 0), 0)} of OTC bootstrap draws (Alpha {pct(dga['kn'].get(1, 0), 0)} and "
        f"{pct(dga['kp'].get(2, 0), 0)}). That fit spans exactly the functions of a no-band curve with two slopes whose knee sits at +2 (a step at +2 plus the slope after it equal one line through +1 "
        f"plus a change of slope at +2; the residual sums of squares agree to {abs(O['knee2_k2_rss'] - dgo_fit.rss) / dgo_fit.rss:.0e}); the slopes are {f2(k2_slopes[0], 2)} from +1 to +2 and {f2(k2_slopes[0] + k2_slopes[1], 2)} beyond. "
        f"Moving the knee to +{k2o.thr[0]} (bootstrap median {k2_dist['otc'][0]}, 95% range {k2_dist['otc'][1]}-{k2_dist['otc'][2]}) fits better in sample with ONE threshold instead of two: residual sum of squares {k2o.rss - dgo_fit.rss:+.0f} and BIC "
        f"{k2o.ic('bic') - dgo_fit.ic('bic'):+.0f} on OTC ({k2a.rss - dga_fit.rss:+.0f} and {k2a.ic('bic') - dga_fit.ic('bic'):+.0f} on Alpha), and out of sample it is no worse (dead-zone fit minus it: {f2(k2c['otc'][0], 3, True)}, {k2c['otc'][0] / k2c['otc'][1]:+.1f} SE on OTC; "
        f"{f2(k2c['alpha'][0], 3, True)}, {k2c['alpha'][0] / k2c['alpha'][1]:+.1f} SE on Alpha; exploratory form). Freeing the band gains {f2(cvp['T-graded vs D-graded'][0], 3)} squared points over closing it on OTC "
        f"(z = {zdiff(cvp['T-graded vs D-graded']):.1f}) and nothing detectable on Alpha. The one rating +1 is where the response crosses zero: against the responder's own mean initiating rating the response to +1 is "
        f"{pm(hb[1]['mean'], hb[1]['se'])} and to +2 {pm(hb[2]['mean'], hb[2]['se'])}; +1 is the modal rating ({pct(res['share_plus1']['otc'], 0)} of all OTC ratings) and, on average, the responders' own habit "
        f"(mean initiating rating {f2(O['habit_mean'][0], 2)}).")
    add(f"- **The sign gate is real and large.** A negative received rating moves the response by {pm(po['est']['neg'], po['se']['neg'])} points against a +1 "
        f"(Alpha {pm(pa['est']['neg'], pa['se']['neg'])}); {pct(sm['p_neg_after_neg'], 0)} of OTC responses to a negative rating are negative, against {pct(sm['p_neg_after_pos'], 1)} after a positive one. "
        f"The mildest negative rating, -1, already moves the response by {f2(fo[ks]['est'][0], 1, True)} points against +1 on OTC (p {pstr(fo[ks]['p'])}), "
        f"so on OTC there is no dead zone on the negative side either; on Alpha the -1 cell ({fa[ks]['n_min']} responses) is too thin to say.")
    add(f"- **'Bounded constants beyond the threshold' holds only as saturation.** The positive response rises {f2(po['est']['slope14'], 1)} per point to +4, more slowly to about +{knee_med} (clipped-mirror knee "
        f"{knee_med}, {ci(knee_ci[0], knee_ci[1], 0)}) and not further: the levels at 5-8 and at 9-10 are {pm(po['est']['hi58'], po['se']['hi58'], 1)} and {pm(po['est']['hi910'], po['se']['hi910'], 1)} above +1. "
        f"The 9-10 ratings are unstable (only {pct(ex_hi[0], 0)} of +10 first ratings are answered within a day, {pct(ex_hi[1], 0)} within 30 days) and the negative side is near its floor at -10. "
        "Between the thresholds nothing is flat.")
    add(f"- **Drift 2010-2016.** The form does not change: in every year with enough pairs ({min(est_years)}-{max(est_years)} on OTC, {min(est_years_a)}-{max(est_years_a)} on Alpha) the response at +2 exceeds the response at +1 "
        f"(on Alpha as a point estimate, individually significant only in {', '.join(sig_a) if sig_a else 'no year'}), "
        f"and on OTC the best dead-zone fit is the one-rating band every year. On OTC the 1-4 slope rises modestly: {f2(yrs[2011]['est']['slope14'], 2)} (2011), {f2(yrs[2012]['est']['slope14'], 2)}, "
        f"{f2(yrs[2013]['est']['slope14'], 2)}, {f2(yrs[2014]['est']['slope14'], 2)}, {f2(yrs[2015]['est']['slope14'], 2)} (2015), a pooled trend of {pm(tr['slope14'][0], tr['slope14'][1], 3)} per year and "
        f"{pm(yo['slope14']['slope'], yo['slope14']['se_infl'], 3)} from the yearly estimates (lack of fit p {pstr(yo['slope14']['p_lof'])}). The negative jump and the 9-10 level have pooled trends "
        f"({pm(tr['neg'][0], tr['neg'][1])} and {pm(tr['hi910'][0], tr['hi910'][1])} per year) that the years do not follow: neither is linear in year (lack of fit p {pstr(yo['neg']['p_lof'])} and "
        f"p {pstr(yo['hi910']['p_lof'])}; the 9-10 level is highest in {hi910_peak}), and against the year-to-year scatter their trends are z = {zt(yo['neg']):+.1f} and {zt(yo['hi910']):+.1f}: "
        f"no drift is shown for either. {alpha_trend_sentence} 2010 and 2016 hold too few pairs to estimate "
        f"({yrs[2010]['pairs']} and {yrs[2016]['pairs']} on OTC; {yrs_a[2010]['pairs']} and {yrs_a[2016]['pairs']} on Alpha).")
    add("")
    add(f"**Thresholds.** K- = -1: any negative rating transmits ({pct(dgo['kn'].get(1, 0), 0)} of OTC draws in the graded fit; the step form spreads over "
        f"{', '.join(f'-{k}: {pct(v, 0)}' for k, v in sorted(dso['kn'].items()) if v >= 0.05)}). K+ = +2 in the graded fit, i.e. a dead zone of the single rating +1 (OTC draws {pct(dgo['kp'].get(2, 0), 0)}, Alpha {pct(dga['kp'].get(2, 0), 0)}); "
        f"the literal step form gives K+ = {', '.join(f'{k}: {pct(v, 0)}' for k, v in sorted(dso['kp'].items()) if v >= 0.05)} on OTC because a single step is the best one-step stand-in for a ramp, and its implied band is rejected by the flatness tests. "
        f"Upper knee of the positive response: {knee_med} ({ci(knee_ci[0], knee_ci[1], 0)}).")
    add("")
    add("**Status of the prediction.**")
    add("")
    add(f"- *Refuted:* a flat band of small received ratings in the response: over any two or more observed ratings on OTC (the band {{+1, +2}} in every estimable OTC year), and over any band reaching +2 on Alpha; "
        f"the 1-4 slope is more than 3 SE above zero in {len(emb_cells) - len(emb_weak)} of {len(emb_cells)} embeddedness bins "
        f"(the exceptions, all thin: {emb_weak_txt if emb_weak else 'none'}); and a response that is a bounded constant just beyond the thresholds.")
    add("- *Supported:* a response that depends on the sign of the received rating (a large jump at zero, K- = -1), grows with the LEVEL of the received rating up to a knee near 7, depends on the level and not on its deviation from the sender's habit, and keeps this form over 2011-2015 and across both platforms.")
    add(f"- *Undecided:* whether the association is reciprocation or two traders' shared view of one trade (the ratings follow one deal; {pct(gp['share_le_10min'], 0)} of OTC responses come within 10 minutes and {pct(res['exact_copy']['otc']['within10'][1], 0)} of those repeat the received rating exactly: time order is necessary, not sufficient); "
        "a dead zone in the influence hidden under a shared view that is not linear in the received rating; "
        f"Alpha's band {{-1, +1}} ({fa[ks]['n_min']} responses to a -1); "
        f"whether a band narrower than the scale's one-point resolution exists; the negative side below -1 ({sm['n_neg']} OTC and {sa_['n_neg']} Alpha negative received ratings, {pct(sm['share_m10'], 0)} and {pct(sa_['share_m10'], 0)} of them -10); the 9-10 ratings.")
    add("")
    add("*For v0.2 (proposals, not adopted):* in a rating medium the dyad response is better written as a graded function of the partner's level with a sign jump and a knee than as an O-jive "
        "(and so is the influence, unless a shared view that is not linear in the received rating hides a zone); "
        "the dead-zone widths theta+ and theta- of 112 section 6.2 should start at 0 here (112 section 6.3 and v0.2 section 4.5 already say so: 'start at 0, wide slack'; "
        "those widths act on the accumulated evaluation zbar, which this test reaches only through the received rating); and the response is to the LEVEL of the partner's rating, "
        "which is what the O-jive's own form says (v0.2 section 3 'D2').")
    add("")

    # ------------------------------------------------------------ 1. data
    add("## 1. Data, terms, definitions")
    add("")
    add("- **Source.** SNAP `soc-sign-bitcoinotc.csv.gz` and `soc-sign-bitcoinalpha.csv.gz` (Kumar, Spezzano, Subrahmanian & Faloutsos 2016, "
        "ICDM, doi:10.1109/ICDM.2016.0033; Kumar, Hooi, Makhija, Kumar, Faloutsos & Subrahmanian 2018, WSDM, doi:10.1145/3159652.3159729), public downloads from "
        "`https://snap.stanford.edu/data/` kept in the git-ignored `sim/data/bitcoin/`; sha256 "
        f"`{gb.SOURCES['otc'].sha256}` (OTC, {gb.SOURCES['otc'].size:,} bytes) and `{gb.SOURCES['alpha'].sha256}` (Alpha, {gb.SOURCES['alpha'].size:,} bytes), "
        "byte-identical to a fresh download on 2026-11-01. Terms: none stated by SNAP; treated as not licensed for redistribution and never committed (`sim/data/README.md`; Licensing in `CLAUDE.md`). "
        "Checked on every load, matching 117: integer ratings -10..10 with no zero, no ordered pair rated twice, no self-rating.")
    add("")
    table(["platform", "ratings", "nodes", "pairs rated both ways", "ordered response pairs", "same-timestamp pairs", "rows with responder FE", "responders"],
          [["OTC", f"{o_info['n_ratings']:,}", f"{o_info['n_nodes']:,}", f"{o_info['n_pairs_reciprocal']:,}", f"{o_info['n_response_pairs']:,}", f"{o_info['n_pairs_tied']:,}", f"{O['n_fe']:,}", f"{O['n_responders']:,}"],
           ["Alpha", f"{a_info['n_ratings']:,}", f"{a_info['n_nodes']:,}", f"{a_info['n_pairs_reciprocal']:,}", f"{a_info['n_response_pairs']:,}", f"{a_info['n_pairs_tied']:,}", f"{A['n_fe']:,}", f"{A['n_responders']:,}"]])
    add("- **Time resolution decides the design.** OTC times are sub-second, so every reciprocated pair has a first and a second rating. "
        "Alpha's are whole days (all at 04:00 or 05:00 UTC, local midnight): "
        f"{a_info['n_pairs_tied']:,} of its {a_info['n_pairs_reciprocal']:,} reciprocated pairs carry one timestamp and cannot be ordered. "
        f"They are kept out of the time-ordered analysis and analysed separately as unordered pairs with a random orientation ({res['tied_n']:,} pairs; section 5.4). "
        "Alpha's ordered pairs are therefore all pairs with a gap of a day or more, a sample biased towards slow responses; "
        "the like-for-like comparison is OTC with a gap of a day or more (section 5.4).")
    add(f"- **Response pair.** First rater i rated j at t1; responder j rated i at t2 > t1. x = the rating j received from i; y = the rating j gave. "
        f"One (x, y) per pair. **The gap is short**: on OTC the median is {gp['quantiles_seconds'][2] / 60:.1f} minutes, "
        f"{pct(gp['share_le_1min'], 0)} of responses come within a minute, {pct(gp['share_le_10min'], 0)} within 10 minutes, {pct(gp['share_le_1d'], 0)} within a day, "
        f"{pct(gp['share_le_30d'], 0)} within 30 days. A rating follows one deal (117), so for most pairs the two ratings are two views of one event, one entered "
        "seconds or minutes after the other, and the response function below is an association net of the persons' levels, not an isolated causal effect.")
    add(f"- **Controls (primary).** A fixed effect for the RESPONDER, absorbing every time-invariant trait of j (his habit of rating, how he is rated, his "
        "general reciprocity); inference clustered by responder (other clusterings in section 3.3). Rows of responders with one response pair cannot inform a fixed effect and are dropped "
        f"from those fits ({pct(sample_o_dropped, 0)} of OTC pairs). Variations (section 5.1): none; responder and first-rater effects; the responder's habit "
        "(the mean of the ratings he gave when he rated first, so uncontaminated by the response mechanism), the first rater's habit and reputation as "
        "covariates, from the whole file or from earlier events only; the responder's previous rating (inertia, D1's r_i).")
    add("- **Embeddedness** (Leskovec, Huttenlocher & Kleinberg 2010, WWW, doi:10.1145/1772690.1772756; L4825): common neighbours of the pair in the undirected graph of rated pairs, counted "
        "either over the whole file (static) or only for neighbours both of whose edges were first rated before the response (time-respecting; primary).")
    add("- **Years** are the calendar year (UTC) of the RESPONSE. Cells with fewer than 100 rows are listed, not fitted.")
    add("")

    # ------------------------------------------------------------ 2. method
    add("## 2. Method and the nulls")
    add("")
    add("**Forms** (thresholds on the integer received rating; K+ = the first positive rating on which the positive side is active; K- the first negative one, as the rating -K-). "
        "All include a free level (the responder effect). 'step' = a bounded constant beyond the threshold (v0's literal O-jive), 'hinge' = continuous and graded beyond it, "
        "'graded' = a jump AND a slope (nests both). A step or graded side is active AT its threshold; a hinge is zero AT its knot and active from the next rating, so for the hinge "
        "K is the knot and the band includes it: the two-sided hinge at the origin has its knots at +1 and -1, the ratings nearest zero, and is flat over both "
        "(corrected at review: this form was labelled 'no dead zone').")
    add("")
    table(["family", "meaning", "free thresholds", "what the prediction says"],
          [["null", "no dependence on x", "0", "no coupling"],
           ["linear", "one slope on x, both signs", "0", "the linear partner term (L4367: about 0 for couples)"],
           ["O+ / O-", "one-sided: only high (or only low) received ratings matter", "1", "a gate open on one side"],
           ["T", "two-sided, thresholds at the origin (K+ = 1, K- = 1): no dead zone for step and graded; the hinge, zero at its knots +1 and -1, is flat over {-1, +1}", "0", "sign matters, size may (graded)"],
           ["D", "two-sided with a free band (K-, K+): the O-jive / dead zone (for the hinge the band includes its knots)", "2", "v0.2 section 4.1: zero inside, bounded beyond (step)"],
           ["saturated", "one mean per rating bin (14 bins)", "13 mean parameters", "reference: no functional form"],
           ["clipped mirror; jump + clipped mirror", "linear up to a knee U then flat, without / with a sign jump", "1", "exploratory: suggested by the first look at the means; NOT part of the pre-specified comparison"],
           ["no band, two slopes", "T graded plus a change of slope at the rating K on the positive side", "1", "exploratory: the no-band rival with the same function class as the dead-zone fit when K = 2"]],
          ["---", "---", "---", "---"])
    add("**Comparison.** In-sample least squares with thresholds on a grid, BIC counting each threshold as a parameter; and out-of-sample squared error from 10-fold cross-validation "
        f"repeated {res['cv_repeats']} times, in which the thresholds are CHOSEN AGAIN inside each training fold and the held-out row's responder effect is re-estimated from its training rows "
        "(held-out rows whose responder has no training row are not scored, for every form, so the comparison is paired). Differences carry a cluster-robust standard error (responder).")
    add("")
    add("**Nulls.** (1) *No response*: y independent of x given the responder effect; the cluster-robust Wald test of all twelve received-rating contrasts. (2) *No dead zone*: the response is "
        "flat over the band; tested head-on by Wald tests of equality of the mean response over the observed ratings inside a candidate band (section 3.2), and by whether freeing the band "
        "(D) beats the same shape with the band closed (T) out of sample (section 4). (3) *Copying beyond habit*: if a responder drew his rating from his own habit regardless of x, the share of "
        "responses equal to x would equal the share of his initiating ratings equal to x; the excess over that is the copy excess (section 3.1). (4) *Exchangeability*: if the two ratings were exchangeable "
        "(the same process whichever was entered first), swapping their roles would give the same curve; section 5.6. Two views of one deal give that only if the two views carry equal noise and spread, "
        "so a difference is weak evidence of a response, and similarity does not show a shared view (corrected at review: this null was stated as 'only two views of one deal').")
    add("")
    add("**What was and was not fixed in advance.** The family names come from the task (one-sided, two-sided, dead zone). The raw mean response by received rating, and a few responder-fixed-effect contrasts, were looked at "
        "BEFORE the model forms were coded; the shapes (step / hinge / graded), the threshold grids (1-10 on each side) and the criteria (BIC; cross-validation with the thresholds re-chosen in each fold) were then fixed in the "
        "module and the pre-specified forms were not changed after any comparison was run. The four-number 'profile' summary and the two clipped-mirror forms were chosen from that first look; the no-band two-slope form was added LATER, "
        "after the dead-zone fit had returned its one-rating band, to ask what that band is. All of them are labelled exploratory wherever they appear. "
        "The test is therefore not blind. What protects the verdict is that it rests on the FAILURE of a prediction the model made before the data (a flat band), on a head-on flatness test that no tuning of a form can rescue, "
        "and on out-of-sample comparisons with the thresholds re-chosen inside every training fold.")
    add("")

    # ------------------------------------------------------------ 3. results
    add("## 3. The response function")
    add("")
    add("### 3.1 Response by received rating")
    add("")
    add(f"Responder fixed effects. 'Shift' = the mean response against the response to +1 (cluster-robust SE); 'y - habit' = the response minus the responder's own mean initiating rating "
        f"(single ratings only); 'copy excess' = share of responses that are exact copies beyond what the responder's habit gives (95% cluster-bootstrap CI); responders who never rated first are left out of those two columns. Overall test of no response: "
        f"chi2({O['wald_any'][1]}) = {O['wald_any'][0]:.0f}, p {pstr(O['wald_any'][2])} (OTC); chi2({A['wald_any'][1]}) = {A['wald_any'][0]:.0f}, p {pstr(A['wald_any'][2])} (Alpha).")
    add("")
    for name, blk, cpd in (("OTC", O, cp), ("Alpha (ordered pairs, gap >= 1 day)", A, cpa)):
        hbd = {r["x"]: r for r in blk["habit"]}
        add(f"**{name}** ({blk['n_fe']:,} rows)")
        add("")
        rows = []
        for r in blk["curve"]:
            b = r["bin"]
            v = b[0] if b[0] == b[1] else None
            h = hbd.get(v) if v is not None else None
            c_ = cpd.get(v) if v is not None else None
            rows.append([bin_label(b), r["n"], f2(r.get("mean_y")), pm(r["shift"], r["se"]) if r["shift"] is not None and r["se"] is not None else ("0 (ref.)" if b == gb.BASE_BIN else "n/a"),
                         pm(h["mean"], h["se"]) if h and h["mean"] is not None else "", pct(r.get("p_neg"), 1),
                         pct(r.get("p_copy"), 0) if r.get("p_copy") is not None else "",
                         (f"{f2(c_['pi'], 2)} {ci(c_['lo'], c_['hi'])}" if c_ and c_["pi"] is not None else "")])
        table(["received x", "n", "mean y", "shift vs +1 (SE)", "y - habit (SE)", "P(y < 0)", "P(y = x)", "copy excess"], rows,
              ["---", "---:", "---:", "---:", "---:", "---:", "---:", "---:"])
    pis = [cp[v]["pi"] for v in range(2, 11) if cp[v]["pi"] is not None]
    ec, eca = res["exact_copy"]["otc"], res["exact_copy"]["alpha"]
    add(f"The response rises by a near-constant step from +1 to +4 (about {f2(po['est']['slope14'], 1)} per point) with no flat stretch, saturates between 5 and 8, and is erratic at 9-10 (few rows, a minority of such ratings is answered, section 3.3). "
        "A negative rating turns the response negative in almost every case. Beyond what the responder's habit gives, a third to a half of the responses repeat a positive received rating exactly, at every size from +2 to +10 "
        f"(OTC copy excess {f2(min(pis), 2)} to {f2(max(pis), 2)}): the copy share does not grow with size (if anything it falls), the opposite of a gate that opens for large ratings. "
        "On Alpha the copy excess at +1 is nil (its ordered pairs are the slow ones; section 5.5 shows that copying decays with the gap). "
        f"Exact copying is the norm on OTC: {pct(ec['all'][1], 0)} of all responses repeat the received rating exactly ({pct(ec['within10'][1], 0)} of the responses within ten minutes, {pct(ec['after1d'][1], 0)} of those a day or more later; "
        f"{pct(ec['all_above1'][1], 0)} when the received rating is above +1); on Alpha's ordered pairs {pct(eca['all'][1], 0)} ({pct(eca['all_above1'][1], 0)} above +1).")
    add("")
    add("### 3.2 Is the response flat over a band? (the defining property of a dead zone)")
    add("")
    rows = []
    for lab, _ in gb.FLAT_TESTS:
        a_, b_ = fo[lab], fa[lab]
        rows.append([lab, a_["df"], f"{a_['chi2']:.1f}" if a_["chi2"] is not None else "n/a", pstr(a_["p"]), "[" + ", ".join(f2(v, 2, True) for v in a_["est"]) + "]" if a_["est"] else "",
                     f"{b_['chi2']:.1f}" if b_["chi2"] is not None else "n/a", pstr(b_["p"]), "[" + ", ".join(f2(v, 2, True) for v in b_["est"]) + "]" if b_["est"] else ""])
    table(["band (observed ratings inside it)", "df", "OTC chi2", "p", "OTC contrasts vs +1", "Alpha chi2", "p", "Alpha contrasts vs +1"], rows,
          ["---", "---:", "---:", "---:", "---", "---:", "---:", "---"])
    se_sym = abs(fo[ks]["est"][0]) / np.sqrt(fo[ks]["chi2"])
    add(f"Every band that holds two or more observed ratings is rejected on both platforms except the symmetric band {{-1, +1}} on Alpha, where only {fa[ks]['n_min']} responses follow a -1 "
        f"(the OTC estimate for the same band is {f2(fo[ks]['est'][0], 1, True)}, SE {f2(se_sym, 1)}). A dead zone consisting of the single rating +1 cannot be tested by flatness; it is the zero-crossing discussed in the verdict. "
        f"The +2 contrast is {z2o['shift'] / z2o['se']:.0f} SE from zero on OTC and {z2a['shift'] / z2a['se']:.1f} SE on Alpha.")
    add("")
    add("*A dead zone hidden under a linear association* (added at review). These tests are of the association. If part of it is a shared view of the deal, that part adds slope inside any band, "
        "and a dead zone in the influence would be masked; but if the added part is linear over +1..+4, the O-jive's bounded step still shows as an excess increment at K+. "
        f"The increments of the response from +1 to +2, +2 to +3 and +3 to +4 are {', '.join(f2(v, 2, True) for v in inc_o['inc'])} on OTC (equal: chi2(2) = {inc_o['chi2']:.2f}, p {pstr(inc_o['p'])}) "
        f"and {', '.join(f2(v, 2, True) for v in inc_a['inc'])} on Alpha (chi2(2) = {inc_a['chi2']:.2f}, p {pstr(inc_a['p'])}); from +4 to +5 it is {f2(inc_o['inc45'], 2, True)} on OTC "
        f"and {f2(inc_a['inc45'], 2, True)} on Alpha, smaller, the opposite of a step. No step at +2, +3, +4 or +5 sits on the line. A shared view that is not linear in x could still mask one.")
    add("")
    add("### 3.3 Sign and magnitude")
    add("")
    add("The four-number profile of the response function (exploratory summary; responder fixed effects; cluster-robust SE in parentheses; 95% cluster-bootstrap CI in brackets):")
    add("")
    rows = []
    for nm, lab in (("slope14", "slope over received ratings 1-4 (points per point)"), ("hi58", "level shift for 5-8 against +1"),
                    ("hi910", "level shift for 9-10 against +1"), ("neg", "level shift for a negative received rating")):
        rows.append([lab, f"{pm(po['est'][nm], po['se'][nm])} {ci(*prof_ci[nm])}", f"{pm(pa['est'][nm], pa['se'][nm])} {ci(*prof_ci_a[nm])}"])
    rows.append(["within-responder R2: profile / linear / saturated", f"{po['r2']:.3f} / {O['specs']['fe']['r2_linear']:.3f} / {po['r2_saturated']:.3f}",
                 f"{pa['r2']:.3f} / {A['specs']['fe']['r2_linear']:.3f} / {pa['r2_saturated']:.3f}"])
    table(["parameter", "OTC", "Alpha"], rows, ["---", "---:", "---:"])
    ase = O["alt_se"]
    add(f"Clustering by first rater or two-way (responder and first rater) leaves the OTC standard errors where they are (slope 1-4: {f2(ase['resp']['slope14'], 3)} by responder, {f2(ase['first']['slope14'], 3)} by first rater, "
        f"{f2(ase['two_way']['slope14'], 3)} two-way; negative jump {f2(ase['resp']['neg'], 2)}, {f2(ase['first']['neg'], 2)}, {f2(ase['two_way']['neg'], 2)}).")
    add("")
    add(f"*Sign margin.* After a negative received rating the response is negative in {pct(sm['p_neg_after_neg'], 1)} of {sm['n_neg']} cases (OTC) and {pct(sa_['p_neg_after_neg'], 1)} of "
        f"{sa_['n_neg']} (Alpha); after a positive one in {pct(sm['p_neg_after_pos'], 1)} of {sm['n_pos']:,} and {pct(sa_['p_neg_after_pos'], 1)} of {sa_['n_pos']:,}. "
        f"With responder effects the difference is {pm(sm['fe_diff'], sm['fe_se'], 3)} (OTC) and {pm(sa_['fe_diff'], sa_['fe_se'], 3)} (Alpha).")
    add("")
    add(f"*Extensive margin* (does he answer at all? OTC; first ratings of the last 30 days dropped): the share of first ratings answered by a rating within a day is "
        f"{pct(ext1[(1, 1)]['rate'], 0)} for +1, {pct(ext1[(2, 2)]['rate'], 0)} for +2, {pct(ext1[(3, 3)]['rate'], 0)} for +3, {pct(ext1[(5, 5)]['rate'], 0)} for +5, "
        f"{pct(ext1[(10, 10)]['rate'], 0)} for +10 and {pct(ext1[(-10, -10)]['rate'], 0)} for -10 (within 30 days: {pct(ext30[(1, 1)]['rate'], 0)}, {pct(ext30[(2, 2)]['rate'], 0)}, "
        f"{pct(ext30[(3, 3)]['rate'], 0)}, {pct(ext30[(5, 5)]['rate'], 0)}, {pct(ext30[(10, 10)]['rate'], 0)}, {pct(ext30[(-10, -10)]['rate'], 0)}). The probability of answering is flat over +1 and +2, "
        "falls steadily with larger ratings and collapses after a negative one. The intensive-margin curve above is therefore estimated on a selected set of responders, selected more tightly at high x; "
        "the high bins should be read with that in mind.")
    add("")
    add("### 3.4 Drift by year (response year)")
    add("")
    for name, blk in (("OTC", O), ("Alpha", A)):
        rows = []
        for r in blk["years"]:
            if "est" not in r:
                rows.append([r["year"], f"{r['pairs']:,}", f"{r['fe_rows']:,}", "too few", "", "", "", "", ""])
                continue
            rows.append([r["year"], f"{r['pairs']:,}", f"{r['fe_rows']:,}", pm(r["shift2"], r["se2"]), pm(r["est"]["slope14"], r["se"]["slope14"]), pm(r["est"]["hi58"], r["se"]["hi58"]),
                         pm(r["est"]["hi910"], r["se"]["hi910"]), pm(r["est"]["neg"], r["se"]["neg"]),
                         f"K+={r['d_graded'][0]}, K-={r['d_graded'][1]} / {r['d_step'][0]}, {r['d_step'][1]}"])
        add(f"**{name}**")
        add("")
        table(["year", "pairs", "FE rows", "+2 vs +1", "slope 1-4", "5-8", "9-10", "negative", "dead-zone fit: graded / step"], rows,
              ["---", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---"])
        t = blk["trend"]
        add(f"Linear trend per year over {min(blk['trend_years'])}-{max(blk['trend_years'])} (pooled, responder FE; its SE allows no year-to-year scatter about the line): slope 1-4 {pm(t['slope14'][0], t['slope14'][1], 3)}, negative jump {pm(t['neg'][0], t['neg'][1], 2)}, "
            f"9-10 level {pm(t['hi910'][0], t['hi910'][1], 2)}, 5-8 level {pm(t['hi58'][0], t['hi58'][1], 2)}.")
        add("")
        yt_ = blk["year_trend"]
        add("From the yearly estimates of the table (weighted by 1/SE^2; the SE inflated when the years scatter about the line more than their SEs allow; added at review): "
            + ", ".join(f"{lab_} {pm(yt_[nm]['slope'], yt_[nm]['se_infl'], 3 if nm == 'slope14' else 2)} (lack of fit chi2({yt_[nm]['df']}) = {yt_[nm]['lof']:.1f}, p {pstr(yt_[nm]['p_lof'])})"
                        for nm, lab_ in (("slope14", "slope 1-4"), ("neg", "negative jump"), ("hi910", "9-10 level"), ("hi58", "5-8 level")) if yt_[nm]) + ".")
        add("")
    zmin = min(r["shift2"] / r["se2"] for r in O["years"] if "shift2" in r)
    odd_a = [str(r["year"]) for r in A["years"] if "d_graded" in r and r["d_graded"] != (2, 1)]
    add(f"On OTC the response at +2 exceeds the response at +1 in every estimable year (z from {zmin:.1f} up), and the graded dead-zone fit is the one-rating band every year. On Alpha it is positive in all {len(est_years_a)} estimable years "
        f"but individually significant only in {', '.join(sig_a) if sig_a else 'none'} (SE 0.5-0.7 per year; the pooled test of section 3.2 is the sharper one); the band differs from the one-rating band in {', '.join(odd_a) if odd_a else 'no year'}. "
        f"On OTC the 1-4 slope strengthens modestly; the sign jump and the 9-10 level move from year to year without a trend that survives the scatter (z = {zt(yo['neg']):+.1f} and {zt(yo['hi910']):+.1f}; "
        f"the 9-10 level is highest in {hi910_peak}). Corrected at review: this paragraph said the sign jump weakens and the 9-10 level falls, from the pooled trends alone.")
    add("")

    # ------------------------------------------------------------ 4. forms
    add("## 4. One-sided, two-sided and dead-zone forms compared")
    add("")
    add("In-sample (BIC, within-responder R2) and out-of-sample (10-fold CV mean squared error of the response, in squared rating points). "
        "'params' = mean parameters plus searched thresholds. 'vs best' = difference from the best PRE-SPECIFIED form, with a cluster-robust SE. Exploratory forms are starred.")
    add("")
    for name, blk in (("OTC", O), ("Alpha", A)):
        add(f"**{name}** ({blk['n_fe']:,} rows, {blk['cv_n']:,} scored in CV)")
        add("")
        fits, cv, cd = blk["fits"], blk["cv"], blk["cv_diff"]
        best_ic = min(f.ic("bic") for k, f in fits.items() if k[0] not in gb.EXPLORATORY_NAMES and k[0] != "saturated")
        rows = []
        for fam, shape, _ in gb.PRESPEC_FORMS + gb.EXPLORATORY_FORMS:
            k = (fam, shape)
            f = fits[k]
            thr = ""
            if f.cand is not None and shape == "hinge":     # a hinge is zero at its knot: show the knots, not 'K+ = 1'
                thr = ", ".join(([f"knot +{f.cand.kp}"] if f.cand.kp is not None else []) + ([f"knot -{f.cand.kn}"] if f.cand.kn is not None else []))
            elif f.cand is not None:
                thr = ", ".join(([f"K+={f.cand.kp}"] if f.cand.kp is not None else []) + ([f"K-=-{f.cand.kn}"] if f.cand.kn is not None else []))
            elif fam in gb.EXPLORATORY_NAMES:
                thr = f"knee {'K' if fam == 'knee2' else 'U'}={f.thr[0]}"
            exploratory = fam in gb.EXPLORATORY_NAMES
            d_, se_ = cd[k]
            rows.append([gb.form_label(fam, shape) + (" *" if exploratory else ""), thr, f.k + f.n_thr, f"{1 - f.rss / blk['null_rss']:.3f}", f"{f.ic('bic') - best_ic:+.0f}",
                         f"{cv[k]:.3f}", "best" if k == blk["cv_best_prespec"] else (f"{d_:+.3f} ({se_:.3f})" if se_ > 0 else "identical")])
        table(["form", "thresholds", "params", "R2 (within)", "BIC - best pre-spec.", "CV MSE", "CV vs best pre-spec. (SE)"], rows, ["---", "---", "---:", "---:", "---:", "---:", "---:"])
    add("\\* exploratory, chosen after seeing the means.")
    add("")
    add("**Paired comparisons that carry the verdict** (CV squared error, first minus second, positive = the second is better; cluster-robust SE):")
    add("")
    rows = []
    for nm in O["cv_pairs"]:
        d1, s1 = cvp[nm]
        d2, s2 = cva[nm]
        rows.append([nm, f"{d1:+.3f} ({s1:.3f}); z = {d1 / s1:+.1f}" if s1 > 0 else "identical", f"{d2:+.3f} ({s2:.3f}); z = {d2 / s2:+.1f}" if s2 > 0 else "identical"])
    table(["comparison", "OTC", "Alpha"], rows, ["---", "---:", "---:"])
    add("Reading: (i) the literal O-jive (D, step) loses clearly to the graded two-sided forms; (ii) closing the band (T, graded) costs "
        f"{f2(cvp['T-graded vs D-graded'][0], 3)} on OTC (z = {zdiff(cvp['T-graded vs D-graded']):.1f}), but the dead-zone graded fit with the one-rating band is the same function class as a no-band two-slope curve with its knee at +2, "
        f"and the no-band two-slope curve with the knee where the data put it (+{k2o.thr[0]} on OTC, +{k2a.thr[0]} on Alpha) is as good out of sample and better by BIC with one threshold instead of two, so what the band buys is a decrease of slope, not a zone; "
        "(iii) one-sided forms lose by a wide margin, so both sides respond; (iv) the linear form loses to the two-line form because of the sign jump.")
    add("")
    add("### 4.1 Thresholds: how stable are they? (cluster bootstrap over responders)")
    add("")
    rows = []
    for name, dd in (("OTC", {"graded": dgo, "step": dso, "hinge": dho}), ("Alpha", {"graded": dga, "step": dsa, "hinge": dha})):
        for sh in ("step", "graded", "hinge"):
            d_ = dd[sh]
            rows.append([name, f"D, {sh}" + (" (K = knot)" if sh == "hinge" else ""), ", ".join(f"{k}: {pct(v, 0)}" for k, v in sorted(d_["kp"].items()) if v >= 0.005), ", ".join(f"-{k}: {pct(v, 0)}" for k, v in sorted(d_["kn"].items()) if v >= 0.02),
                         pct(d_["empty"], 0), pct(d_["narrowest"], 0), ", ".join(f"({p[0]},{p[1]}): {pct(w, 0)}" for p, w in d_["modal"] if w >= 0.005)])
    table(["platform", "form", "K+ (share of draws)", "K- (share of draws, >= 2%)", "band empty", "narrowest band (K+ = K- = 1)", "most frequent (K+, K-)"], rows,
          ["---", "---", "---", "---", "---:", "---:", "---"])
    add(f"For step and graded the narrowest band is empty. For the hinge it is not: a hinge is zero at its knot, so knots at +1 and -1 give those two ratings the same response, and a hinge band is never empty "
        f"(corrected at review: this table reported the hinge's band as empty in {pct(dho['narrowest'], 0)} of OTC draws). The continuous dead-zone form takes that narrowest band, flat over {{-1, +1}}, in "
        f"{pct(dho['narrowest'], 0)} of OTC and {pct(dha['narrowest'], 0)} of Alpha draws, and it loses out of sample to the same form with a sign jump (T, graded) by {f2(th_o[0], 3)} ({zdiff(th_o):.1f} SE) on OTC "
        f"and {f2(th_a[0], 3)} ({zdiff(th_a):.1f} SE) on Alpha: the smallest dead zone a continuous O-jive can have is rejected where the -1 cell has rows (OTC), as the flatness test of {{-1, +1}} says.")
    add("")
    add(f"Clipped-mirror knee (exploratory): OTC {knee_med} ({ci(knee_ci[0], knee_ci[1], 0)}; draws {', '.join(f'{k}: {pct(v, 0)}' for k, v in sorted(kud.items()))}); "
        f"Alpha {int(np.median(kua))} ({ci(int(np.percentile(kua, 2.5)), int(np.percentile(kua, 97.5)), 0)}). "
        f"Knee of the no-band two-slope curve (exploratory): OTC {k2_dist['otc'][0]} ({ci(k2_dist['otc'][1], k2_dist['otc'][2], 0)}), Alpha {k2_dist['alpha'][0]} ({ci(k2_dist['alpha'][1], k2_dist['alpha'][2], 0)}).")
    add("")
    add("The step form's K+ of 3-4 is not a dead zone: a single bounded step is the best one-step approximation to a ramp, so the search puts it where the ramp is steepest "
        "(the profile of RSS against K+ below is lowest at 3 for the step and at 2 for the graded form), and the flatness tests reject the band it implies.")
    add("")
    add("Residual sum of squares by positive threshold K+ (best K- for each), OTC; lower is better:")
    add("")
    rows = []
    stp, grd = {k: (kn, r) for k, kn, r in O["dprofile"]["step"]}, {k: (kn, r) for k, kn, r in O["dprofile"]["graded"]}
    best_s, best_g = min(r for _, r in stp.values()), min(r for _, r in grd.values())
    for k in sorted(set(stp) | set(grd)):
        rows.append([k, f"{stp[k][1] - best_s:+.0f} (K-=-{stp[k][0]})" if k in stp else "", f"{grd[k][1] - best_g:+.0f} (K-=-{grd[k][0]})" if k in grd else ""])
    table(["K+", "step: RSS - best", "graded: RSS - best"], rows, ["---:", "---:", "---:"])

    # ------------------------------------------------------------ 5. variations
    add("## 5. Variations")
    add("")
    best_pre_o, best_pre_a = form_name(O["cv_best_prespec"]), form_name(A["cv_best_prespec"])
    add(f"**Which model variant fits best.** Among the pre-specified forms the best out-of-sample on OTC is *{best_pre_o}* and on Alpha *{best_pre_a}*. On Alpha it is not separable from the "
        f"no-band two-line form (T, graded; {f2(cva['T-graded vs D-graded'][0], 3)}, z = {zdiff(cva['T-graded vs D-graded']):.1f}); on OTC the margin is "
        f"{f2(cvp['T-graded vs D-graded'][0], 3)} squared points (z = {zdiff(cvp['T-graded vs D-graded']):.1f}) and is the one-rating band, which section 4 shows to be a knee at +2. "
        f"Overall the best description, pre-specified or not, is a no-band curve: the exploratory two-slope form (BIC {O['fits'][('knee2', None)].ic('bic') - O['fits'][('D', 'graded')].ic('bic'):+.0f} against the dead-zone graded fit on OTC, "
        f"{A['fits'][('knee2', None)].ic('bic') - A['fits'][('D', 'graded')].ic('bic'):+.0f} on Alpha) and the sign-jump-plus-clipped-mirror form "
        f"({O['fits'][('jump+clip', None)].k + O['fits'][('jump+clip', None)].n_thr} parameters including the knee) are each within one SE of the saturated reference on both platforms. "
        "The variants below change what is held fixed; none restores a dead zone.")
    add("")
    add("### 5.1 Controls")
    add("")
    rows = []
    names = {"raw": "none (pooled)", "fe": "responder FE (primary)", "fe2": "responder + first-rater FE", "cov_all": "habit, first rater's habit, reputation (whole file)",
             "cov_prior": "same, earlier events only", "fe_inertia": "responder FE + previous rating"}
    for sp in ("raw", "fe", "fe2", "cov_all", "cov_prior", "fe_inertia"):
        for pl, blk in (("OTC", O), ("Alpha", A)):
            r = blk["specs"][sp]
            if r is None:
                continue
            rows.append([names[sp], pl, f"{r['n']:,}", pm(r["est"]["slope14"], r["se"]["slope14"]), pm(r["est"]["hi58"], r["se"]["hi58"]), pm(r["est"]["neg"], r["se"]["neg"]),
                         f"K+={r['d_graded'][0]}, K-={r['d_graded'][1]}", form_name(r["best_bic"]), f"{r['bic_gap_d_vs_t']:+.0f}"])
    table(["control set", "platform", "n", "slope 1-4", "5-8", "negative", "dead-zone fit (graded)", "best form by BIC", "BIC: D graded - T graded"], rows,
          ["---", "---", "---:", "---:", "---:", "---:", "---", "---", "---:"])
    sl = lambda blk: [blk["specs"][sp]["est"]["slope14"] for sp in blk["specs"] if blk["specs"][sp]]  # noqa: E731
    ng = lambda blk: [blk["specs"][sp]["est"]["neg"] for sp in blk["specs"] if blk["specs"][sp]]  # noqa: E731
    add(f"The 1-4 slope stays between {f2(min(sl(O)), 2)} and {f2(max(sl(O)), 2)} on OTC and between {f2(min(sl(A)), 2)} and {f2(max(sl(A)), 2)} on Alpha whatever is controlled, and the dead-zone fit is the one-rating band in "
        "nearly every row: the response is not produced by stable differences between raters (stingy raters pairing with stingy ones, popular traders with generous ones). The negative jump moves most "
        f"({f2(min(ng(O)), 1)} to {f2(max(ng(O)), 1)} on OTC), and that is where the cells are thinnest. Pair-specific confounds (a shared deal, a standing partnership) are not removed by any of these.")
    add("")
    add("### 5.2 The level of the received rating, or its deviation from the sender's habit?")
    add("")
    for name, blk in (("OTC", O), ("Alpha", A)):
        sg = blk["signal"]
        add(f"**{name}** (rows with a first-rater habit: {sg['n']:,}; null MSE {sg['null_mse']:.2f})")
        add("")
        rows = [[k, f"{v:.3f}", f"{sg['diff'][k][0]:+.3f} ({sg['diff'][k][1]:.3f})" if sg["diff"][k][1] > 0 else "best"] for k, v in sorted(sg["mse"].items(), key=lambda kv: kv[1])]
        table(["design (responder FE)", "CV MSE", "vs best (SE)"], rows, ["---", "---:", "---:"])
    add("The deviation u = x - (first rater's habit) predicts much worse than the level x, and adds nothing once the level is in: the response is to what was said, not to how unusual it was for him to say it. "
        "That matches the form of the O-jive (a function of the partner's level, v0.2 section 3 'D2') and argues against a 'surprise' gate.")
    add("")
    add("### 5.3 By embeddedness")
    add("")
    for name, blk in (("OTC", O), ("Alpha", A)):
        for key, lab in (("emb_prior", "time-respecting (primary)"), ("emb_static", "static")):
            st = blk[key]
            rows = []
            for l in st["labels"]:
                p = st["params"][l]
                rows.append([l, f"{st['n_by'][l]:,}"] + [pm(*p[nm]) if p[nm] else "n/a" for nm in gb.PROFILE_NAMES])
            add(f"**{name}, common neighbours {lab}**")
            add("")
            table(["common neighbours", "FE rows", "slope 1-4", "5-8", "9-10", "negative"], rows, ["---", "---:", "---:", "---:", "---:", "---:"])
            tt = st["tests"]
            add("Equality across bins (Wald): " + "; ".join(f"{nm}: chi2({t[1]}) = {t[0]:.1f}, p {pstr(t[2])}" for nm, t in tt.items() if t) + ".")
            add("")
    allsl = sorted((blk[k]["params"][l]["slope14"][0], blk[k]["params"][l]["slope14"][1], n_, k, l, blk[k]["n_by"][l]) for n_, blk in (("OTC", O), ("Alpha", A)) for k in ("emb_prior", "emb_static")
                   for l in blk[k]["labels"] if blk[k]["params"][l]["slope14"])
    lo1, lo2 = allsl[0], allsl[1]
    emb_p = [(n_, key, nm, blk[key]["tests"][nm][2]) for n_, blk in (("OTC", O), ("Alpha", A)) for key in ("emb_prior", "emb_static") for nm in gb.PROFILE_NAMES if blk[key]["tests"][nm]]
    prior_p = [c for c in emb_p if c[1] == "emb_prior"]
    static_sig = [c for c in emb_p if c[1] == "emb_static" and c[3] < 0.05]
    lo_p = min(prior_p, key=lambda c: c[3])
    pn = {"slope14": "1-4 slope", "hi58": "5-8 level", "hi910": "9-10 level", "neg": "negative jump"}
    add(f"The shape does not depend on embeddedness in any consistent way. In the time-respecting count (primary) no parameter differs across bins at the 5% level on either platform "
        f"(smallest p {pstr(lo_p[3])}: {lo_p[0]}, {pn[lo_p[2]]}). In the static count "
        + (("; ".join(f"{c[0]} {pn[c[2]]} differs (p {pstr(c[3])})" for c in static_sig)) if static_sig else "none differs") +
        f"; the static count credits a pair with neighbours it only acquired after the response, so it is the weaker measure. The 1-4 slope is positive in all {len(allsl)} bins: the smallest is "
        f"{f2(lo1[0], 2)} (SE {f2(lo1[1], 2)}; {lo1[2]}, {'static' if lo1[3] == 'emb_static' else 'time-respecting'} count, {lo1[4]} common neighbours, {lo1[5]} rows) and the next {f2(lo2[0], 2)} (SE {f2(lo2[1], 2)}). "
        "Leskovec et al.'s embeddedness effect concerns triads, not this dyadic response; 112 section 6.5 test 5 (visibility at low embeddedness) is a different question and is not answered here.")
    add("")
    add("### 5.4 By platform")
    add("")
    rows = []
    for lab, r in res["platform"].items():
        rows.append([lab, f"{r['n']:,}", pm(r["est"]["slope14"], r["se"]["slope14"]), pm(r["est"]["hi58"], r["se"]["hi58"]), pm(r["est"]["hi910"], r["se"]["hi910"]), pm(r["est"]["neg"], r["se"]["neg"])])
    table(["sample", "FE rows", "slope 1-4", "5-8", "9-10", "negative"], rows, ["---", "---:", "---:", "---:", "---:", "---:"])
    a1, a2 = res["platform"]["OTC, gap >= 1 day"], res["platform"]["Alpha, ordered (gap >= 1 day)"]
    b1, b2 = res["platform"]["OTC, gap < 1 day"], res["platform"]["Alpha, same-day pairs (random orientation)"]
    zs = {nm: (a1["est"][nm] - a2["est"][nm]) / np.hypot(a1["se"][nm], a2["se"][nm]) for nm in gb.PROFILE_NAMES}
    zt_ = {nm: (b1["est"][nm] - b2["est"][nm]) / np.hypot(b1["se"][nm], b2["se"][nm]) for nm in gb.PROFILE_NAMES}
    big = [f"{nm} (z = {zz[nm]:+.1f}, {lab_})" for zz, lab_ in ((zs, "slow pairs"), (zt_, "fast and same-day pairs")) for nm in gb.PROFILE_NAMES if abs(zz[nm]) > 1.96]
    add("Like for like the platforms agree: OTC with a gap of a day or more against Alpha's ordered pairs differ by z = " + ", ".join(f"{nm} {zs[nm]:+.1f}" for nm in gb.PROFILE_NAMES) +
        "; OTC under a day against Alpha's same-day pairs (an arbitrary orientation, so an association rather than a time-ordered response) by z = " + ", ".join(f"{nm} {zt_[nm]:+.1f}" for nm in gb.PROFILE_NAMES) +
        ("; beyond 2 SE: " + "; ".join(big) if big else "; no difference reaches 2 SE") +
        ". The full-OTC and full-Alpha columns of section 3 differ mainly because Alpha's ordered pairs are all slow. "
        f"Reciprocated pairs carrying opposite signs (112 section 6.5 test 4): OTC {xo['otc'][0]} of {xo['otc'][1]:,} ({pct(xo['otc'][0] / xo['otc'][1], 1)}), Alpha {xo['alpha'][0]} of {xo['alpha'][1]:,} ({pct(xo['alpha'][0] / xo['alpha'][1], 1)}): rare.")
    add("")
    add("### 5.5 By the gap between the two ratings")
    add("")
    for name, blk in (("OTC", O), ("Alpha", A)):
        st = blk["gap_strata"]
        rows = []
        for l in st["labels"]:
            p = st["params"][l]
            rows.append([l, f"{st['n_by'][l]:,}"] + [pm(*p[nm]) if p[nm] else "n/a" for nm in gb.PROFILE_NAMES])
        add(f"**{name}**")
        add("")
        table(["gap", "FE rows", "slope 1-4", "5-8", "9-10", "negative"], rows, ["---", "---:", "---:", "---:", "---:", "---:"])
        tt = st["tests"]
        add("Equality across gaps (Wald): " + "; ".join(f"{nm}: chi2({t[1]}) = {t[0]:.1f}, p {pstr(t[2])}" for nm, t in tt.items() if t) + ".")
        add("")
    rows = []
    for lab, (n, ce) in res["copy_by_gap"].items():
        d_ = {r["x"]: r for r in ce}
        rows.append([lab, f"{n:,}"] + [f"{f2(d_[v]['pi'], 2)} {ci(d_[v]['lo'], d_[v]['hi'])}" if d_[v]["pi"] is not None else "n/a" for v in (1, 2, 3)])
    add("Copy excess by gap (OTC; 95% cluster-bootstrap CI):")
    add("")
    table(["gap", "pairs", "copy excess at +1", "at +2", "at +3"], rows, ["---", "---:", "---:", "---:", "---:"])
    gto, gta = O["gap_strata"]["tests"], A["gap_strata"]["tests"]
    add("The slope over 1-4 is the same for responses a minute later and responses a month later; what changes with the gap is how often the response is an exact copy at +1 (high within minutes, 'rate for rate'; "
        f"below the responder's habit after a day), the 9-10 level (p {pstr(gto['hi910'][2])} on OTC, p {pstr(gta['hi910'][2])} on Alpha) and, on OTC, the size of the negative jump (p {pstr(gto['neg'][2])}). "
        "The graded response survives the delay; the exact mirroring does not.")
    add("")
    add("### 5.6 Time-reversed placebo")
    add("")
    rr, ra = O["rev_profile"], A["rev_profile"]
    add(f"Swap the roles: regress the EARLIER rating on the LATER one (fixed effect for the first rater). If the two ratings were exchangeable it would be symmetric; two views of one deal give that only with equal noise and spread in the two views (section 2, null 4). "
        f"OTC reversed: slope 1-4 {pm(rr['est']['slope14'], rr['se']['slope14'])}, 5-8 {pm(rr['est']['hi58'], rr['se']['hi58'])}, 9-10 {pm(rr['est']['hi910'], rr['se']['hi910'])}, "
        f"negative {pm(rr['est']['neg'], rr['se']['neg'])} (forward: {f2(po['est']['slope14'], 2, True)}, {f2(po['est']['hi58'], 2, True)}, {f2(po['est']['hi910'], 2, True)}, {f2(po['est']['neg'], 2, True)}). "
        f"Alpha reversed: slope {pm(ra['est']['slope14'], ra['se']['slope14'])}, negative {pm(ra['est']['neg'], ra['se']['neg'])} (forward {f2(pa['est']['slope14'], 2, True)}, {f2(pa['est']['neg'], 2, True)}). "
        f"The graded positive slope is smaller in reverse but of the same order ({pm(rr['est']['slope14'], rr['se']['slope14'])} against {pm(po['est']['slope14'], po['se']['slope14'])}), as compatible with a shared view of one deal as with a response. The negative jump is not: "
        f"a negative first rating is answered by a negative one {pct(sm['p_neg_after_neg'], 0)} of the time (OTC; Alpha {pct(sa_['p_neg_after_neg'], 0)}), but only {pct(sm['p_neg_before_neg'], 0)} of the {sm['n_neg_resp']} negative responses followed a negative first rating (Alpha {pct(sa_['p_neg_before_neg'], 0)}). "
        "The rest are negative ratings given after a positive one. That asymmetry is what retaliation predicts; it is also what a scam sequence produces (a seller rates the buyer well at the deal, the cheated buyer rates him badly later), and no field of the file separates the two. "
        "Neither direction has a dead zone.")
    add("")
    add("### 5.7 Capped responders")
    add("")
    cn, cs = O["capped"]
    cna, csa = A["capped"]
    add(f"At most three response pairs per responder, chosen at random (so that busy responders cannot carry the curve): OTC {cn:,} rows, slope 1-4 {pm(cs['est']['slope14'], cs['se']['slope14'])}, negative {pm(cs['est']['neg'], cs['se']['neg'])}; "
        f"Alpha {cna:,} rows, slope {pm(csa['est']['slope14'], csa['se']['slope14'])}, negative {pm(csa['est']['neg'], csa['se']['neg'])}.")
    add("")

    # ------------------------------------------------------------ 6. caveats
    add("## 6. Caveats")
    add("")
    add("1. **Association, not isolated causation.** The two ratings follow one deal and arrive minutes apart; time order does not remove a shared view of the deal or an agreement to rate each other. "
        "The time-reversed check (5.6) finds the negative side asymmetric and the positive slope nearly symmetric. A causal reading of the positive slope needs variation in what a responder knew when he rated, which the file lacks.")
    add("2. **The response function is estimated on responders.** Whether a trader answers at all depends strongly on the received rating (3.3), so the shape at high x describes a selected set. "
        "The REV2 paper (Kumar et al. 2018) is about fraudulent ratings in these two networks; this file does not say which ratings are fraudulent, and the 9-10 bins are the least stable across years and gaps.")
    add("3. **Resolution.** Ratings are integers and none is zero. A flat band narrower than one rating point cannot be seen; the data say only that no band of two or more observed ratings is flat. "
        "The 'band' of the best dead-zone fit is one rating, +1, and carries no evidence of a zone.")
    add(f"4. **Thin negative side.** {sm['n_neg']} OTC and {sa_['n_neg']} Alpha received ratings are negative ({sm['n_m10']} and {sa_['n_m10']} of them -10). The -1..-5 cells hold 50 or fewer rows each; claims about thresholds below -1 are not supported either way.")
    add(f"5. **Alpha timestamps are days.** {pct(a_info['n_pairs_tied'] / a_info['n_pairs_reciprocal'], 0)} of its reciprocated pairs are unorderable and kept out of the ordered analysis; the ordered ones are slow. The platform comparison is made like for like for that reason.")
    mc = multiple_comparisons(res)
    bonf = {k: min(1.0, p * mc["n_pairs"]) for k, p in mc["dst_p"].items()}
    alpha_bonf = ("survives it narrowly" if bonf["alpha"] < 0.05 else "does not survive it") + f" on Alpha (corrected p {pstr(bonf['alpha'])}; it sits near the line and moves with the number of CV repeats)"
    add("6. **Researcher degrees of freedom and multiple comparisons.** See section 2: the first look preceded the forms. Thresholds are chosen on grids; the CV re-chooses them inside folds, the BIC counts them. "
        "No multiple-comparison correction is applied to the many tables of section 5; the conclusions do not rest on any single cell. Checked at review against a Bonferroni correction: "
        f"the flatness rejections the verdict uses survive it across all {mc['n_flat']} flatness tests (largest p {pstr(mc['flat_p_max'])}, corrected p {pstr(min(1.0, mc['flat_p_max'] * mc['n_flat']))}); "
        f"D-step against T-graded, across the {mc['n_pairs']} paired comparisons of a platform, survives it on OTC (corrected p {pstr(bonf['otc'])}) and {alpha_bonf}. The drift claims did not survive the "
        "year-to-year scatter and were cut at review (section 3.4); the one kept, the 1-4 slope's, is modest and is one of four parameters tried. The head-on flatness tests are Wald tests, not calibrated against a threshold-search null; "
        "the claim that freeing the band helps is the modest one (z about 2 on OTC) and is not leaned on.")
    add("7. **One population.** Pseudonymous Bitcoin traders 2010-2016 on two IRC-era web-of-trust sites; the sign means 'trust after a deal'. Not couples (the O-jive's origin), not teams, not Wikipedia.")
    add("8. **Ratings are treated as numbers.** The fits are least squares on the rating; no ordinal model was fitted. The two discrete outcomes of sections 3.1 and 3.3 (a negative response; an exact copy) are the checks on the coding, and agree with the numeric picture.")
    add("")

    # ------------------------------------------------------------ 7. consequences
    add("## 7. What this does to the model (proposals, not adopted)")
    add("")
    add("- `models/00-v0.md` section 4.1 and 3 'D2': the O-jive's dead zone is not found in this dyadic rating medium. Where the coupling is measured by a rating of the partner, write I(x) as a graded function with a sign jump and a saturation knee; "
        "keep the dead-zone widths as soft settings that start at 0 (112 section 6.3 already says so). The couples evidence for a husband's K- (L0834) is one of ten tests in one cohort and stays quarantined; this result is neither support nor refutation of it, because the medium differs.")
    add("- The linear partner term of L4367 (about 0 at 6 s in couples) does not carry over: the linear term here is large (about 0.8 per point) and the sign jump larger still. Bitcoin ratings are a communicated, public, post-deal evaluation, not a moment-by-moment affect; the two media should not share one coupling constant.")
    add(f"- 112 section 6.5 test 4 (symmetry): opposite-sign reciprocated pairs are {pct(xo['otc'][0] / xo['otc'][1], 1)} (OTC) and {pct(xo['alpha'][0] / xo['alpha'][1], 1)} (Alpha), so the condition that section sets for using R-A's symmetric layer without a symmetrisation rule holds in this medium; "
        "the asymmetry that remains is the time-ordered negative response of 5.6.")
    add("- For the sign law (R-X, exchange as sentiment): ratings given after a deal copy the rating received at a rate that does not grow with its size and decays with the delay. That is an exchange-norm term with a delay parameter, not a drive coupling.")
    add("")

    # ------------------------------------------------------------ reproduction
    add("## Reproduction")
    add("")
    add("    cd sim")
    add("    ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report fetch    # once; sha256-checked, git-ignored")
    add("    ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report report   # writes this file (a few minutes; seeded)")
    add("    ~/.local/bin/uv run pytest tests/test_gate_reciprocity_bitcoin.py")
    add("")
    add(f"The verdict above is guarded: `report` refuses to write the file if any of {len(guards(res))} stated facts (signs, orderings, p-value bounds) stops holding.")
    add("")
    return "\n".join(L)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch", help="download the SNAP files for local use (git-ignored); verifies sha256")
    sub.add_parser("check", help="verify the local files and print the basic counts")
    rp = sub.add_parser("report", help="run every analysis and write sim/results/gate_reciprocity_bitcoin.md")
    rp.add_argument("--boot", type=int, default=B_BOOT)
    rp.add_argument("--out", default=str(RESULTS))
    rp.add_argument("--pickle", default=None, help="also save the computed results here (for re-rendering the text without recomputing)")
    rr = sub.add_parser("render", help="re-render the results file from a pickle saved by `report --pickle`")
    rr.add_argument("pickle")
    rr.add_argument("--out", default=str(RESULTS))
    args = ap.parse_args(argv)
    if args.cmd == "fetch":
        for p in gb.fetch():
            print(f"wrote {p}")
        return 0
    if args.cmd == "check":
        for k in ("otc", "alpha"):
            R = gb.load_ratings(k)
            ps = gb.pair_structure(R)
            print(k, R.n, "ratings;", ps.n_pairs_reciprocal, "reciprocated pairs;", ps.n_pairs_tied, "tied;", int(ps.first.sum()), "ordered response pairs")
        return 0
    if args.cmd == "render":
        import pickle
        with open(args.pickle, "rb") as fh:
            res = pickle.load(fh)
        ok = guards(res)
        Path(args.out).write_text(_keep_review(render(res), args.out), encoding="utf-8")
        print(f"wrote {args.out}; {len(ok)} guards held (re-rendered, nothing recomputed)")
        return 0
    res = analyse(B=args.boot)
    if args.pickle:
        import pickle
        with open(args.pickle, "wb") as fh:
            pickle.dump(res, fh)
    ok = guards(res)
    text = _keep_review(render(res), args.out)
    Path(args.out).write_text(text, encoding="utf-8")
    print(f"wrote {args.out}; {len(ok)} guards held; {res['elapsed']:.0f} s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
