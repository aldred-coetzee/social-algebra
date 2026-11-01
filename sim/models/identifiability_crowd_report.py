"""Run the crowd-law identifiability study end to end and write sim/results/identifiability_crowd.md.

    cd sim
    ~/.local/bin/uv run python -m models.identifiability_crowd_report report [--workers N] [--cache DIR]

Everything computed lives in models/identifiability_crowd.py (tasks, engines, estimators; ledger ids are in its
LEDGER); this module only organises the tables and the text, as models/newcomb_report.py does for the Newcomb test.
Seeded and independent of scheduling: the numbers in the results file are reproduced exactly by the same command
(25 to 40 minutes on six shared cores, dominated by the n = 100 lattice cells; --cache keeps finished tasks so that a run can be
resumed or extended).  No data are read or
written: every crowd is simulated.
"""
from __future__ import annotations

import argparse
import datetime
from pathlib import Path

import numpy as np

from models.identifiability_crowd import FITTED, RESULTS, SEED, run_all

def _md(headers, rows):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return "\n".join(out)


def _f(x, d=2):
    return "-" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{d}f}"


def _p(x):
    return "-" if x is None or (isinstance(x, float) and np.isnan(x)) else ("<0.001" if x < 0.001 else f"{x:.3f}")


def _sel(results, kind, mfit=False, **cond):
    """Results of one kind matching `cond`.  The review's SBC cells of the misspecification setups (spec setup="mfit") are
    returned only with mfit=True, so that every table and count written before the review is unchanged by them."""
    out = []
    for k, r in results:
        if k != kind:
            continue
        sp_ = r["spec"]
        if (sp_.get("setup") == "mfit") != mfit:
            continue
        if all(sp_.get(a) == b for a, b in cond.items()):
            out.append(r)
    return out


def _one(results, kind, **cond):
    r = _sel(results, kind, **cond)
    assert len(r) == 1, (kind, cond, len(r))
    return r[0]


def _calibrated(s):
    """Flag used in the tables: no scored quantity or joint-likelihood rank is detectably non-uniform at 0.001 and no
    central-90% coverage is more than 3.5 binomial standard errors from 0.90."""
    M = s["M"]
    band = 3.5 * np.sqrt(0.09 / M)
    ok = (s["min_ks"] >= 1e-3 and s["ll_ks"] >= 1e-3 and s["c90_min"] >= 0.9 - band and s["c90_max"] <= 0.9 + band
          and abs(s["ll_c90"] - 0.9) <= band)
    return "yes" if ok else "NO"


def tbl_visited(results):
    rows = []
    for gen in ("beta", "clipnorm", "bimodal", "logitnorm"):
        for n in (100, 1000):
            r = _sel(results, "visited", gen=gen, n=n)
            if r:
                r = r[0]
                rows.append([gen, n, _f(r["med"], 0), f"{r['q25']:.0f}-{r['q75']:.0f}", _f(100 * r["le3"], 0) + "%",
                             _f(100 * r["le5"], 0) + "%", _f(100 * r["ge8"], 0) + "%", _f(100 * r["full"], 0) + "%"])
    return _md(["generator", "n", "median points of F read", "IQR", "<= 3 points", "<= 5 points", ">= 8 points",
                "cascade to everyone"], rows)


def tbl_engine_validation(results):
    rows = []
    for r in _sel(results, "sbc", engine="lattice"):
        sp_, s, s2 = r["spec"], r["summary"], r["sl_summary"]
        d = r.get("pm_diff", {})
        rows.append([sp_["fam"], sp_["n"], sp_["sigma"], s["M"], _calibrated(s), _p(s["min_ks"]), _f(s["ll_c90"]),
                     _calibrated(s2), _p(s2["min_ks"]), _f(s2["ll_c90"]), _f(d.get("tau")), _f(d.get("F(0.55)"))])
    rows.sort(key=lambda r: (r[0], r[1], r[2]))
    return _md(["family", "n", "sigma", "M", "lattice calibrated", "lattice min KS p", "lattice joint-ll c90",
                "synthetic calibrated", "synthetic min KS p", "synthetic joint-ll c90",
                "mean abs diff of posterior mean, tau (prior sd)", "same, F(0.55)"], rows)


def tbl_sbc(results):
    """Calibration of every SBC cell of the natural-run design."""
    rows = []
    for r in _sel(results, "sbc"):
        sp_ = r["spec"]
        if sp_.get("runs"):
            continue
        s = r["summary"]
        rows.append([sp_["fam"], sp_["engine"], sp_["n"], sp_["sigma"], s["M"], r["G"], _calibrated(s), _p(s["min_ks"]),
                     f"{s['c90_min']:.2f}-{s['c90_max']:.2f}", _f(s["ll_c90"]), _p(s["ll_ks"])])
    order = {"exact": 0, "lattice": 1, "sl": 2}
    rows.sort(key=lambda r: (r[0], r[2], r[3], order[r[1]]))
    return _md(["family", "engine", "n", "sigma", "M", "grid", "calibrated", "min KS p", "central-90% coverage range",
                "joint-ll coverage", "joint-ll KS p"], rows)


def _best_engine(results, fam, n, sigma):
    """The cell whose engine is exact where possible: exact at sigma = 0, lattice where it was run, else synthetic."""
    for eng in ("exact", "lattice", "sl"):
        for r in _sel(results, "sbc", fam=fam, n=n, sigma=sigma, engine=eng):
            if not r["spec"].get("runs"):
                return r
    return None


def tbl_information(results, fam):
    rows = []
    for n in (30, 100, 300, 1000, 3000):
        for sigma in (0.0, 0.01, 0.03, 0.1):
            r = _best_engine(results, fam, n, sigma)
            if r is None:
                continue
            s = r["summary"]
            tot = s["n_F_in"] + s["n_F_out"]
            tag = r["spec"]["engine"] + ("" if _calibrated(s) == "yes" else "*")
            rows.append([n, sigma, tag, s["M"], _f(s["sd_params"]), _f(s["sd_tau"], 3), _f(s["sd_F0"]), _f(s["sd_F_in"]),
                         _f(s["sd_F_out"]), _f(s["rmse_tau"]), _f(s["rmse_F_in"]), _f(s["rmse_F_out"]), _f(s["c90_F_in"]),
                         _f(s["c90_F_out"]), f"{100 * s['n_F_out'] / max(tot, 1):.0f}%"])
    return _md(["n", "sigma", "engine", "M", "params", "tau", "F(0)", "F inside", "F outside", "RMSE tau", "RMSE F inside",
                "RMSE F outside", "c90 F inside", "c90 F outside", "readings outside"], rows)


FAIL_CRITERIA = (("tau", "sd_tau", 0.05), ("parameters", "sd_params", 0.25), ("F inside", "sd_F_in", 0.25),
                 ("F outside", "sd_F_out", 0.25))
FAIL_NS = (30, 100, 300, 1000, 3000)


def _first_n(results, fam, sigma, key, thr):
    """(smallest n from which the median relative posterior sd `key` stays below `thr` for every larger n tested,
    whether every cell from there on is calibrated); (None, True) if it does not at the largest n."""
    cells = [(n, _best_engine(results, fam, n, sigma)) for n in FAIL_NS]
    ok = [(n, r["summary"][key] < thr, _calibrated(r["summary"]) == "yes") for n, r in cells
          if r is not None and not np.isnan(r["summary"][key])]
    for i in range(len(ok)):
        if all(o[1] for o in ok[i:]):
            return ok[i][0], all(o[2] for o in ok[i:])
    return None, True


def _fmt_n(first):
    n, cal = first
    return "never" if n is None else f"{n:,}" + ("" if cal else "*")


def tbl_failure(results):
    """Smallest n (of 30, 100, 300, 1000, 3000) from which the median relative posterior sd stays below the criterion,
    per family and noise level; 'never' if it does not at n = 3000.  A star marks a verdict resting on a cell where the
    engine was not calibrated."""
    rows = []
    for fam in ("beta", "clipnorm"):
        for sigma in (0.0, 0.01, 0.03, 0.1):
            row = [fam, sigma]
            for label, key, thr in FAIL_CRITERIA:
                f = _first_n(results, fam, sigma, key, thr)
                row.append("never" if f[0] is None else f">= {f[0]}" + ("" if f[1] else "*"))
            rows.append(row)
    return _md(["family", "sigma"] + [f"{lab} (< {thr:g} of prior sd)" for lab, _k, thr in FAIL_CRITERIA], rows)


def tbl_dirichlet(results):
    rows = []
    for r in sorted(_sel(results, "dirichlet"), key=lambda r: r["spec"]["n"]):
        rows.append([r["spec"]["n"], r["spec"]["M"], _p(min(r["ks"])), _f(r["c90"]), _f(r["sd_in"]), _f(r["sd_out"]),
                     r["n_in"], r["n_out"]])
    return _md(["n", "M", "min KS p of F at the 6 probes", "central-90% coverage", "posterior sd / prior sd, F inside",
                "same, F outside (above the stall)", "readings inside", "readings outside"], rows)


def tbl_misspec_detail(results, n, sigma):
    r = _one(results, "misspec", n=n, sigma=sigma)
    rows = []
    for gen, c in r["cells"].items():
        for f in FITTED:
            sm = c["summ"][f]
            rows.append([gen, f, "matched" if gen == f else "-", _f(sm["tau"]["cov"]), _f(sm["F0"]["cov"]), _f(sm["inside"]["cov"]),
                         _f(sm["outside"]["cov"]), _f(sm["inside"]["rmse"]), _f(sm["outside"]["rmse"]),
                         _f(sm["outside"]["sd"]), _f(c["confusion"][f])])
    return _md(["generator", "fitted", "", "tau cov90", "F(0) cov90", "F inside cov90", "F outside cov90",
                "F inside RMSE", "F outside RMSE", "F outside post sd", "share where it has the largest marginal likelihood"], rows)


def tbl_misspec_pooled(results):
    rows = []
    for r in sorted(_sel(results, "misspec"), key=lambda r: (r["spec"]["sigma"], r["spec"]["n"])):
        n, sigma = r["spec"]["n"], r["spec"]["sigma"]
        acc = {"m": [], "x": []}
        for gen, c in r["cells"].items():
            for f in FITTED:
                sm = c["summ"][f]
                acc["m" if gen == f else "x"].append((sm["tau"]["cov"], sm["inside"]["cov"], sm["outside"]["cov"],
                                                      sm["inside"]["rmse"], sm["outside"]["rmse"]))
        row = [n, sigma]
        for key in ("m", "x"):
            a = np.nanmean(np.array(acc[key]), axis=0)
            row += [_f(a[0]), _f(a[1]), _f(a[2]), _f(a[3]), _f(a[4])]
        diag = np.mean([r["cells"][g]["confusion"][g] for g in ("beta", "clipnorm", "logitnorm")])
        row.append(_f(diag))
        rows.append(row)
    hdr = ["n", "sigma"] + [f"{k}: {h}" for k in ("matched", "mismatched") for h in
                            ("tau cov", "F in cov", "F out cov", "F in RMSE", "F out RMSE")] + ["matched family wins (mean)"]
    return _md(hdr, rows)


def tbl_confusion(results, cells=None):
    """Every misspecification cell by default (corrected at review: five of the twelve were shown, while the verdict's
    ranges are taken over all of them)."""
    if cells is None:
        cells = sorted({(r["spec"]["n"], r["spec"]["sigma"]) for r in _sel(results, "misspec")}, key=lambda c: (c[1], c[0]))
    rows = []
    for n, sigma in cells:
        r = _sel(results, "misspec", n=n, sigma=sigma)
        if not r:
            continue
        for gen, c in r[0]["cells"].items():
            rows.append([n, sigma, gen, c["cells_M"] if "cells_M" in c else c["M"]] + [_f(c["confusion"][f]) for f in FITTED])
    return _md(["n", "sigma", "generated by", "M"] + [f"fitted best: {f}" for f in FITTED], rows)


def tbl_sbc_mfit(results):
    """SBC of the misspecification setups (added at review): the synthetic engine on the fine grids with S = 1,000."""
    rows = []
    for r in sorted(_sel(results, "sbc", mfit=True), key=lambda r: (r["spec"]["fam"], r["spec"]["sigma"], r["spec"]["n"])):
        sp_, s = r["spec"], r["summary"]
        rows.append([sp_["fam"], sp_["n"], sp_["sigma"], s["M"], r["G"], _calibrated(s), _p(s["min_ks"]),
                     f"{s['c90_min']:.2f}-{s['c90_max']:.2f}", _f(s["ll_c90"]), _p(s["ll_ks"]), _f(s["c90_F_in"]), _f(s["c90_F_out"])])
    return _md(["family", "n", "sigma", "M", "grid", "calibrated", "min KS p", "central-90% coverage range", "joint-ll coverage",
                "joint-ll KS p", "c90 F inside", "c90 F outside"], rows)


def reading_sbc_mfit(results):
    cells = _sel(results, "sbc", mfit=True)
    if not cells:
        return ""
    bad = sorted((r["spec"]["fam"], r["spec"]["n"], r["spec"]["sigma"]) for r in cells if _calibrated(r["summary"]) != "yes")
    good = [r["summary"] for r in cells if _calibrated(r["summary"]) == "yes"]
    names = {"beta": "beta+atom", "clipnorm": "clipped normal", "logitnorm": "logit-normal"}
    det = _one(results, "misspec", n=1000, sigma=0.03)["cells"]
    f0 = {f_: det[f_]["summ"][f_]["F0"]["cov"] for f_ in FITTED}
    f0_grid = {r["spec"]["fam"]: r["summary"].get("c90_by", {}).get("F0", float("nan")) for r in cells
               if r["spec"]["n"] == 1000 and r["spec"]["sigma"] == 0.03}
    by = {}
    for f_, n_, s_ in bad:
        by.setdefault(f_, []).append(f"({n_}, {s_:g})")
    return f"""
*The engine behind these rows* (added at review). The cells above with sigma > 0 fit with the synthetic engine on the fine grids with S = 1,000,
which no SBC cell of 3.2 checked. Here is SBC of exactly those setups (same setup seeds), the truth drawn on the fine grid:

""" + tbl_sbc_mfit(results) + f"""

It passes in {len(cells) - len(bad)} of {len(cells)}; the cells where it does not are {'; '.join(names[f_] + ' ' + ', '.join(v) for f_, v in by.items())} (family (n, sigma)), worst
central-90% coverage {min(r['summary']['c90_min'] for r in cells):.2f} and worst joint-likelihood coverage {min(r['summary']['ll_c90'] for r in cells):.2f}. So part of the matched rows' under-coverage at those
cells is the engine's; elsewhere, where every quantity (F(0) included) is covered {min(s['c90_min'] for s in good):.2f} to {max(s['c90_max'] for s in good):.2f} with the truth on the grid,
what the matched rows lose is the continuous truth falling between grid values. The low matched F(0) coverage of the detail table has the same cause
({_f(f0['beta'])} for beta+atom and {_f(f0['logitnorm'])} for logit-normal, whose F(0) is z itself on a grid of six values, against {_f(f0['clipnorm'])} for the clipped normal): in the
same setups with the truth on the grid, F(0) is covered {_f(f0_grid.get('beta'))} and {_f(f0_grid.get('logitnorm'))} (n = 1,000, sigma = 0.03), and an interval made of grid values covers a
continuous truth only when the posterior straddles it. The mismatched-against-matched comparison is made within the same cells and engine.
"""


def tbl_twosided(results):
    rows = []
    for r in sorted(_sel(results, "twosided"), key=lambda r: (-r["spec"]["nu"], r["spec"]["wbar"], r["spec"]["n"], r["spec"]["sigma"])):
        sp_, ra = r["spec"], r["rates"]
        rows.append([sp_["nu"], sp_["wbar"], sp_["n"], sp_["sigma"], r["M"], _f(ra["ceiling"]), _f(ra["big_decline"]),
                     _f(ra["lrt"]), _f(ra["drop"]), _f(ra["lrt_one"]), _f(ra["drop_one"]), _f(ra["lrt_cum"]),
                     _f(ra.get("plateau_growth"))])
    return _md(["share with upper gate", "gate width", "n", "sigma", "M", "current share declines (noise-free)",
                "a step decline >= 3 sigma sqrt2", "power: order test", "power: any-drop rule", "false positive: order test",
                "false positive: any-drop rule", "ever-joined curve: order-test rejection",
                "ever-joined curve: plateau then growth (noise-free)"], rows)


def tbl_ignition(results, designs=False):
    rows = []
    for r in _sel(results, "ignition"):
        sp_ = r["spec"]
        if bool(sp_.get("designs")) != designs:
            continue
        a, ci = r["auc"], r["ci"]

        def cell(name):
            return "-" if name not in a else f"{a[name]:.2f} [{ci[name][0]:.2f}, {ci[name][1]:.2f}]"

        def skill(name):
            b = r["brier"]
            return "-" if name not in b else f"{1 - b[name] / b['base']:+.2f}"

        gens = "matched (beta, clipped normal)" if sp_["gens"] == ("beta", "clipnorm") else "other (bimodal, logit-normal)"
        row = [gens, sp_["n"], sp_["sigma"], r["N"], f"{r['npos']} ({100 * r['prev']:.0f}%)", cell("oracle"), cell("summary"),
               cell("bma_nat"), skill("bma_nat"), cell("probe")]
        if designs:
            row += [cell("bma_p1"), cell("bma_p2"), cell("bma_p4"), skill("bma_p4")]
        rows.append(row)
    rows.sort(key=lambda r: (r[0], r[2], r[1]))
    hdr = ["generators", "n", "sigma", "pairs", "igniting", "AUC known-F margin", "AUC curve summaries",
           "AUC fitted model, natural runs", "Brier skill of it", "AUC adaptive probe"]
    if designs:
        hdr += ["AUC fitted model + 1 seeded run", "+ 2 seeded runs", "+ 4 seeded runs", "Brier skill, + 4 seeded runs"]
    return _md(hdr, rows)


def tbl_ignition_material(results):
    rows = []
    for r in _sel(results, "ignition"):
        sp_ = r["spec"]
        a, ci = r["auc_mat"], r["ci_mat"]

        def cell(name):
            return "-" if name not in a else f"{a[name]:.2f} [{ci[name][0]:.2f}, {ci[name][1]:.2f}]"

        gens = "matched" if sp_["gens"] == ("beta", "clipnorm") else "other"
        rows.append([gens, sp_["n"], sp_["sigma"], "p4" if sp_.get("designs") else "nat",
                     f"{r['npos_mat']} ({100 * r['prev_mat']:.0f}%)", cell("oracle"), cell("summary"), cell("bma_nat"),
                     cell("probe"), cell("bma_p4")])
    rows.sort(key=lambda r: (r[0], r[2], r[1], r[3]))
    return _md(["generators", "n", "sigma", "run", "material ignitions (>= 2% of the crowd)", "AUC known-F margin",
                "AUC curve summaries", "AUC fitted model, natural runs", "AUC adaptive probe", "AUC fitted model + 4 seeded runs"], rows)


def tbl_designs_F(results):
    rows = []
    for r in _sel(results, "sbc"):
        sp_ = r["spec"]
        if not sp_.get("runs"):
            continue
        s = r["summary"]
        rows.append([sp_["fam"], sp_["sigma"], sp_["design"], _calibrated(s), _f(s["sd_params"]), _f(s["sd_F_in"]), _f(s["sd_F_out"]),
                     _f(s["rmse_F_out"]), _f(s["c90_F_out"])])
    order = {"nat": 0, "p1": 1, "p2": 2, "p4": 3}
    rows.sort(key=lambda r: (r[0], r[1], order[r[2]]))
    return _md(["family", "sigma", "design", "calibrated", "params", "F inside", "F outside", "RMSE F outside", "c90 F outside"], rows)


def tbl_dynamic(results):
    rows = []
    for r in sorted(_sel(results, "dynamic"), key=lambda r: (r["spec"]["fam"], r["spec"]["sigma"], r["spec"]["alpha_true"])):
        sp_, d = r["spec"], r["res"]
        rows.append([sp_["fam"], sp_["sigma"], sp_["alpha_true"]] + [_f(v) for v in d["share"]]
                    + [_f(d["rmse_F"][a]) for a in d["alphas"]])
    al = ("0.25", "0.5", "0.75", "1.0")
    return _md(["family", "sigma", "true alpha"] + [f"best: alpha={a}" for a in al] + [f"RMSE F, fitted alpha={a}" for a in al], rows)


def tbl_subsample(results):
    rows = []
    for r in sorted(_sel(results, "subsample"), key=lambda r: (r["spec"]["fam"], r["spec"]["m_true"])):
        sp_, d = r["spec"], r["res"]
        for key, lab in (("known", "m known"), ("assume1", "m wrongly taken as 1"), ("unknown", "m unknown (marginalised)")):
            rows.append([sp_["fam"], sp_["m_true"], lab, _f(d[key]["sd_tau"], 3), _f(d[key]["sd_F"]), _f(d[key]["rmse_tau"]),
                         _f(d[key]["rmse_F"])])
    return _md(["family", "true turns per observation", "fit", "tau post sd (prior sd)", "F post sd (prior sd)",
                "tau RMSE (prior sd)", "F RMSE (prior sd)"], rows)


def tbl_obsmodel(results):
    rows = []
    for r in sorted(_sel(results, "obsmodel"), key=lambda r: (r["spec"]["fam"], r["spec"]["s_rel"])):
        sp_, d = r["spec"], r["res"]
        for key in ("additive", "relative"):
            rows.append([sp_["fam"], sp_["s_rel"], key, _f(d[key]["cov_tau"]), _f(d[key]["cov_F"]), _f(d[key]["sd_tau"], 3)])
    return _md(["family", "relative counting error", "noise model fitted", "tau cov90", "F inside cov90", "tau post sd"], rows)


def _pct(a, b):
    return f"{a} ({100 * a / max(b, 1):.0f}%)"


def tbl_claim14(results):
    """Corrected at review (2026-11-01): the igniting-pair check is Claim 1.2's equal case, not its strictness (now
    checked in the sandwich pairs), and the flips are split by the redrawn part's role."""
    r = _one(results, "claim14")
    t1 = _md(["random finite pairs (n = 40 each)", "igniting", "igniting with equal stalls (Claim 1.2's equal case violated)",
              "Claim 1.4 necessary condition violated"],
             [[f"{r['pairs']:,}", f"{r['igniting']:,}", r["equal_bad"], r["nec_bad"]]])
    host = r["flip_trials"] - r["flip_trials_intr"]
    t2 = _md(["one part (clipped normal, n = 40) redrawn above its own stall, same live curve: pairs", "merge outcome flipped",
              "pairs in which the redrawn part is the intruder", "flipped there",
              "pairs in which it is the host or the stalls are equal", "flipped there"],
             [[f"{r['flip_trials']:,}", _pct(r["flips"], r["flip_trials"]), r["flip_trials_intr"],
               _pct(r["flips_intr"], r["flip_trials_intr"]), host, _pct(r["flips"] - r["flips_intr"], host)]])
    t3 = _md(["live, unsaturated pairs (n = 200 each)", "lower <= merged stall <= upper end violated",
              "pairs with unequal stalls", "merge not strictly above the lower stall (Claim 1.2 strictness violated)",
              "upper end of the sandwich changes when both crowds are redrawn above their stalls (same curves)",
              "... by more than 0.05"],
             [[r["up_trials"], r["sand_bad"], r["strict_trials"], r["strict_bad"], _pct(r["up_chg"], r["up_trials"]),
               _pct(r["up_big"], r["up_trials"])]])
    return t1 + "\n\n" + t2 + "\n\n" + t3


def _facts(results):
    """The few numbers the verdict quotes, pulled from the tables so that text and tables cannot disagree."""
    V = {}
    for fam in ("beta", "clipnorm"):
        for n in (30, 100, 300, 1000, 3000):
            for sg in (0.0, 0.01, 0.03, 0.1):
                r = _best_engine(results, fam, n, sg)
                if r is not None:
                    V[(fam, n, sg)] = dict(r["summary"], engine=r["spec"]["engine"], cal=_calibrated(r["summary"]))
    return V


def _range(vals, d=2):
    vals = [v for v in vals if v is not None and not (isinstance(v, float) and np.isnan(v))]
    if not vals:
        return "-"
    lo, hi = f"{min(vals):.{d}f}", f"{max(vals):.{d}f}"
    # compared as printed (corrected at review: 0.853 and 0.857 printed as one value, '0.85', beside a table showing 0.86)
    return lo if lo == hi else f"{lo}-{hi}"


TESTED = """## What was tested

Granovetter's map r(t+1) = F[r(t)] (`models/00-v0.md` 4.4; L1831, L3960, L3961) with the two-sided gate (L3959, L4355), and
Claim 1 of `models/02-our-claims.md` (the state of a crowd is its whole threshold distribution F; a merge is the mixture; ignition,
Claim 1.4), are the crowd law. The event datasets of `docs/prior-work/089` record aggregate counts over time and never a threshold
(L3980, L3988, L4469). Under the no-circularity rule of `notes/2026-10-29-modelled-population-testbed.md` this file builds crowds
from generators that are **not** the fitted family and shows the fitting code only the noisy aggregate curve r(0), ..., r(10). Three
questions: **(1)** can F be recovered from the curve, and at what crowd size n and observation noise sigma; **(2)** can a two-sided
gate be told from a one-sided one; **(3)** can Claim 1.4's ignition criterion be predicted from the two parts' curves. The nulls are
named where each test is introduced: rank uniformity for calibration, a monotone latent curve for the gate, no skill beyond the base
rate for ignition.
"""

DATA_AND_TERMS = """## 1. Data and terms

**None.** Every crowd is simulated; nothing is downloaded, no credential or licence is involved, and `sim/data/` is untouched.
The relation to the event datasets of 089 matters for the reading of everything below. CCC sizes are order-of-magnitude bins and half
the events have none (L3980, L3988); NAVCO's `camp_size` is six ordinal bins at annual resolution (L4469); no dataset defines the
group whose share r(t) would be formed (089 section 3, equation-to-data map). This test therefore gives the crowd law **more**
than the event datasets give it: a known denominator n, a share on a continuous scale, ten equally spaced turns, a known noise level.
What cannot be fitted under these favourable conditions cannot be fitted on the real data.
"""

METHOD = """## 2. Method

**The crowd and the curve.** A crowd of n members has thresholds theta_i, shares of the crowd. The state is the share r. The first
share is the instigators', r(0) = F_n(0), and then r(t+1) = F_n(r(t)) with F_n the empirical CDF (v0.1 4.4a; L1831, L3960,
L3961), so the curve is a sequence of integers k_t / n and is exact. The two-sided gate is theta_i <= r <= thetabar_i (L3959,
L4355; v0.1 2.3). Observed: y_t = r(t) + N(0, sigma^2), t = 0, ..., 10 (eleven points), unclipped, with sigma in {0, 0.01, 0.03, 0.1}
(sigma = 0 is exact counts). A crowd enters a dataset only if its curve reaches max(3 sigma, 1/n): event datasets contain events.
This selection depends on the observed data only, which leaves SBC valid (conditionally on y the ranks are still uniform).

**Generators.** Every one puts at least 2% of members at threshold 0 (a crowd with no instigator never moves, v0.1 6.3; the prior is
therefore a prior over crowds that can start):

| generator | parameters and continuous prior | role |
|---|---|---|
| beta+atom | z log-uniform [0.02, 0.25]; Beta(a, b), a, b log-uniform [0.6, 8] | generator and fitted family |
| clipped normal | mu uniform [0.04, 0.6], s log-uniform [0.03, 0.4], Phi(-mu/s) >= 0.02 (Granovetter's own family, L3962) | generator and fitted family |
| bimodal | z log-uniform [0.02, 0.2]; early mode m1 in [0.03, 0.35], late mode m2 in [0.45, 0.95], weight w in [0.2, 0.8], concentration log-uniform [8, 40] (as `explore/mixture_equilibria.py`) | generator only |
| logit-normal | z log-uniform [0.02, 0.25]; logit(theta) ~ N(mu, s), mu in [-3, 1], s log-uniform [0.3, 2.5] | generator and fitted family |

The fitted families are beta+atom, clipped normal and logit-normal, each on a discrete grid that is also the prior (uniform over
the grid; beta+atom 405 points, clipped normal 111, logit-normal 315; 'fine' grids of 864, 441 and 840 are used for the
misspecification and ignition work). A discrete prior makes the grid posterior **exact** and SBC exact; its cost is that a
continuous truth falls between grid points, which matters only where the posterior is narrower than the grid (stated where it does).

**Which parts are independent of the fit.** The well-specified SBC of 3.2 has the generator equal to the fitted family *by construction*: it is a computation and identifiability check
(094 section 5, items 1 and 2), a best case, and cannot fail because the model is wrong about crowds. The no-circularity rule bites in 3.3 (bimodal and logit-normal crowds fitted by the other
families), in the ignition work with the "other" generators, in the two-sided generator (which no fitted model contains) and in the inertial and subsampled curves of section 4.

**Engines.** `exact`: the sequential-binomial law of the integer path (derivation in the module docstring; the probabilities of all
paths sum to one for tiny n and match the simulator, tests group A), used at sigma = 0. `lattice`: the exact forward algorithm on
(k_(t-1), k_t) for sigma > 0, cost growing as n^3, used at n = 30 (M = 200) and n = 100 (M = 40). `synthetic`: Wood's synthetic
likelihood with common random numbers (S = 800 to 2,000 simulated crowds per grid point), an approximation used at n = 100 to 3,000
for sigma > 0. Its calibration is **measured**, not assumed (section 3.2): it is approximately calibrated at n >= 1,000 and not where counts
and noise live on the same scale (n sigma of order 1 to 10). SBC measured it on the standard grids with S = 2,000; the misspecification
(3.3) and ignition (3.5) cells with sigma > 0 use it at every n on the fine grids with S = 1,000 and 800. The misspecification setups
were given their own SBC at review (end of 3.3); the ignition setups (S = 800, two families pooled) were not.

**Uncertainty.** Each coverage or share is a proportion of M independent curves, so its binomial standard error is sqrt(p (1 - p) / M): at p = 0.9 it is 0.009 for M = 1,000, 0.015 for M = 400,
0.017 for M = 300, 0.013 for M = 500, 0.021 for M = 200 and 0.047 for M = 40; pooled readings of F (several probes per curve) are correlated within a curve and are less certain than their count suggests. AUCs carry
bootstrap intervals. Posterior-sd medians have no interval; their cell-to-cell scatter is visible across neighbouring rows.

**SBC (the computation check, 094 L4136, L4137, L4140).** Draw theta on the grid, simulate a live crowd and curve, compute the grid
posterior, and take the randomised rank of the truth under it for each of: every parameter, the population stall tau = min(r : F(r) <= r)
(models/02 Fact 0), F(0), F at r = 0.1, 0.25, 0.4, 0.55, 0.7, 0.85, and the joint log-likelihood of the data (L4156, L4153). **The
null is rank uniformity** (an exact posterior). Reported: KS p-value, and the coverage of the central 90% interval (nominal 0.90). A cell is
called calibrated if no KS p is below 0.001 and every coverage is within 3.5 binomial standard errors of 0.90. *Information* is the
median posterior sd divided by the prior sd, and RMSE of the posterior mean over the prior sd; F(r) is read **inside** the visited
range (r <= the level the curve reached) or **outside** it. A pass certifies the arithmetic, not the theory (094 L4140); information is
a best case (L4158).

**Misspecification and model recovery (094 L4157, L4149, L4160).** Curves from the independent generators with continuous parameters,
each fitted by every fitted family; scored by coverage of the 5-95% interval of tau, F(0) and F inside/outside, RMSE, and which family
has the largest marginal likelihood (a confusion matrix with a uniform prior over the three fitted families).

**One- versus two-sided gate.** The two-sided generator gives a fraction nu of members an upper gate theta + (1 - theta) V, V ~
Beta(w kappa, (1 - w) kappa), kappa = 6; the rest stay for ever. Detectors, with sigma known: the **order test** (likelihood ratio of a
non-decreasing latent curve against an unrestricted one, isotonic fit, critical value simulated under the flat curve, which is the
least favourable null so the test has size <= 0.05 for every non-decreasing curve) and an **any-drop rule** (largest drop y_s - y_t
over s < t, same calibration). Power is measured on two-sided crowds and false positives on one-sided crowds with the same lower
thresholds.

**Ignition (models/02 Claim 1.4).** Two independent crowds of n members each (merge weight 1/2); the label is realised ignition of the
merged finite crowd (stall strictly above both parts' stalls, in members; "material" ignition: at least 2% of the crowd higher).
Eligible: both curves live and neither ends above 0.97. Predictors, each scored by AUC against the label (95% bootstrap interval): the
population ignition margin computed from the TRUE generators (a reference that knows F exactly; not a ceiling, because the curves
also carry the realised crowds' own thresholds); the posterior-predictive probability of population ignition from fitting beta+atom
and clipped normal (averaged over the two families) to each curve; a logistic regression on summaries of the two curves (levels,
initial shares); an adaptive probe (start each crowd at the higher final level and read r(1) - r(0), an intervention on r); and the
fitted model given one, two or four fixed seeded runs.
"""


def dir_min_p(results):
    """The sentence fragment on the smallest KS p of the non-parametric posterior's SBC."""
    dr = _sel(results, "dirichlet")
    return f"the smallest of its {sum(len(r['ks']) for r in dr)} KS p-values is {min(min(r['ks']) for r in dr):.3f}"


def section_structure(results):
    c14 = _sel(results, "claim14")
    out = ["""## 3. Results

### 3.1 What a noise-free curve can fix: exact results

This section is arithmetic, not simulation: each statement is a construction with a test (`tests/test_identifiability_crowd.py`,
group B), true for any n and any F.

**Proposition B: a curve reads F at a handful of points, and none above its own stall.** The orbit reads the count of thresholds at 0
and at each distinct level the curve reaches, the last of which is the stall r*. It fixes how many thresholds lie in each cell between
those points and nothing about where inside a cell they sit or about any threshold above r*. `redraw_above_stall` redraws every
threshold above r* and leaves the whole curve identical. It runs the other way from L1225, where no finite moment of F fixes the
outcome: here the outcome curve, and so any summary of it, does not fix F above its stall. How many points does a curve read?

""" + tbl_visited(results) + """

*(F is read at 0 and at every distinct level, the stall included. "Cascade to everyone" means the curve ends at 1, where nothing is
left above the stall to be unknown.)*
"""]
    if c14:
        r = c14[0]
        out.append("""**Consequence for Claim 1.2 and 1.4.** Checked on random finite pairs from the four generators (beta, bimodal and
clipped-normal families were also among those of `models/02`'s own check, 1.8; logit-normal is new), with code independent of
that check:

""" + tbl_claim14(results) + f"""

Claim 1.2's equal case (equal stalls merge to that stall, so never ignite) and Claim 1.4's necessary condition hold in every
igniting pair (no violation in {r['igniting']:,} ignitions); the sandwich (smaller stall <= merged stall <= upper end) holds in every
pair tried, and its strictness (unequal stalls merge strictly above the smaller) in all {r['strict_trials']} pairs with unequal stalls:
that is support for both claims on finite crowds. But in an igniting pair the intruder's stall is strictly below the host's stall M,
and the decisive quantity F_1(M) is read at M, **above the intruder's own stall, where its curve is silent** (Proposition B). An
intruder redrawn above its own stall (the same live curve, a different crowd) merges with the same host to the opposite outcome in
{100 * r['flips_intr'] / max(r['flip_trials_intr'], 1):.0f}% of the pairs tried; a redrawn host cannot change the outcome (the merge
reaches the host's stall M only through thresholds at or below M, which the redraw keeps) and none did, so over all pairs the rate is
{100 * r['flips'] / max(r['flip_trials'], 1):.0f}%. The upper end of the sandwich, the quantity the refutation test of Claim 1.11
needs, moves in {100 * r['up_chg'] / max(r['up_trials'], 1):.0f}% of pairs when only the thresholds above the stalls are redrawn
({100 * r['up_big'] / max(r['up_trials'], 1):.0f}% by more than 0.05). **Neither the ignition criterion nor the refutation test of
the merge law can be evaluated from the two parts' curves alone.**
""")
    out.append("""**Proposition A: a monotone curve cannot show the gate.** If a crowd's current-share curve never declines it is a function
k_(t+1) = h(k_t) of the state alone, and a one-sided crowd built from the curve reproduces it exactly (`orbit_equivalent_one_sided`).
So a two-sided gate whose curve happens to be monotone is indistinguishable from a one-sided one at any n and with no noise, while a
one-sided curve never declines (v0.1 6.3(i), L1201). The decline is the only trace in the current-share curve. The ever-joined
(cumulative) count never declines at all; its only trace of the gate is a plateau followed by growth, which a one-sided stall
(absorbing) never shows.

**Counts are not shares.** With thresholds as absolute numbers of others (Granovetter allows either, L3983) the COUNT curve does not
depend on the pool N, so the stall share c*/N is not identified from counts (`count_orbit`; test). CCC, Mass Mobilization and NAVCO
record counts or count bins with no defined pool (L3980, L3988, L4469).

**The non-parametric posterior, noise-free (exact, conjugate).** A histogram-Dirichlet prior on F (40 cells and an instigator atom)
has an exact posterior given the integer curve: the cell masses are Dirichlet(prior + counts) and, within a cell, F keeps its prior
law. SBC passes (it is exact; """ + dir_min_p(results) + """); the information is the point:

""" + tbl_dirichlet(results))
    return "\n".join(out)


def section_recovery(results):
    out = ["""### 3.2 Question 1: recovering F from the curve when the family is right

**Calibration of the engines (SBC, 094 L4136-L4140, L4153, L4156).** Generator = fitted family, theta drawn on the grid. "Calibrated"
is defined in section 2; the stars in later tables mark a cell that is not.

""" + tbl_sbc(results) + """

**The synthetic engine against the exact one on identical datasets** (same seeds; n = 30 and 100, where the exact lattice engine can
run). This is what the synthetic engine's flags above rest on:

""" + tbl_engine_validation(results)]
    out.append("""

**Information: what the posterior leaves open** (beta+atom, then clipped normal; cells use the exact engine at sigma = 0, the lattice
engine at n = 30 and at n = 100 where it was run, the synthetic engine elsewhere; * = engine not calibrated in that cell). Columns are
the median posterior sd divided by the prior sd (0 = known, 1 = the prior), RMSE of the posterior mean over the prior sd, and the
central-90% coverage of F read inside / outside the visited range. The discrete prior caps the resolution: values near 0.00 mean "to
within a grid cell".

*beta+atom*

""" + tbl_information(results, "beta") + """

*clipped normal*

""" + tbl_information(results, "clipnorm") + """

**Where recovery fails** (smallest n from which the median relative posterior sd stays below the criterion; "never" = not at n = 3,000;
star = rests on an uncalibrated cell):

""" + tbl_failure(results))
    out.append(reading_recovery(results))
    return "\n".join(out)


def section_misspec(results):
    return """### 3.3 Question 1 under independent generators: the wrong family, and which family the curve prefers

Curves from beta+atom, clipped-normal, logit-normal and **bimodal** crowds (continuous parameters), each fitted by all three fitted
families. Detail at n = 1,000, sigma = 0.03, then pooled over cells ("matched" = generator and fitted family the same). **At sigma = 0 and
large n the matched rows lose coverage because the continuous truth falls between grid points (the posterior is narrower than the
grid), not because the fit is wrong; read the mismatched rows against the matched ones in the same row of the pooled table.**

""" + tbl_misspec_detail(results, 1000, 0.03) + """

Pooled over the generator-by-family pairs (matched: beta+atom, clipped normal and logit-normal fitted to themselves; mismatched: all
other pairs, which include everything fitted to the bimodal generator):

""" + tbl_misspec_pooled(results) + """

Model recovery: the share of curves for which each fitted family has the largest marginal likelihood (a perfect instrument would put
1.00 on the generating family; the bimodal generator has no matching family):

""" + tbl_confusion(results) + "\n" + reading_misspec(results) + reading_sbc_mfit(results)


def section_twosided(results):
    return """### 3.4 Question 2: a two-sided gate from aggregate curves

The null is a non-decreasing latent curve (a one-sided gate). The ceiling for any detector working on a single current-share curve is the
share of two-sided crowds whose noise-free curve declines at all (Proposition A); the order test and the any-drop rule are the two
detectors; the one-sided control crowds give their false-positive rates; the last two columns are the ever-joined curve.

""" + tbl_twosided(results) + "\n" + reading_twosided(results)


def section_ignition(results):
    return """### 3.5 Question 3: predicting ignition from the parts' curves

Prevalence is of strict realised ignition among eligible pairs; AUC with a 95% bootstrap interval (200 resamples); 0.5 = no skill.
"Brier skill" is 1 minus the Brier score over the base-rate score (0 = no better than the base rate).

""" + tbl_ignition(results) + """

*Material ignition (the merge stalls at least 2% of the crowd higher), same predictors:*

""" + tbl_ignition_material(results) + """

*Interventions on r: the fitted model given one, two or four fixed seeded runs (a run started at r(0) = 0.5; 0.35 and 0.7; 0.2, 0.4,
0.6 and 0.8, each observed for three steps), n = 1,000:*

""" + tbl_ignition(results, designs=True) + "\n" + reading_ignition(results)


def section_variations(results):
    return """## 4. Variations

Each variation changes one part of the model form or the design and reports which variant fits best.

**4.1 Fitted threshold family.** Section 3.3: the family with the largest marginal likelihood, by generator (the confusion table).

**4.2 Dynamic form: the turn map against an inertial variant.** Curves from r(t+1) = r(t) + alpha (F_n(r(t)) - r(t)) with alpha = 0.25 to
1 (alpha = 1 is v0.1's turn map; alpha < 1: each member re-decides with probability alpha per turn, in expectation), observed for 16
turns at n = 1,000; each curve fitted by the same family at every alpha. "Best" = largest marginal likelihood; RMSE = posterior mean
of tau and F(r) at the probes, over the prior sd.

""" + tbl_dynamic(results) + """

**4.3 The time axis: observing every m-th turn.** Curves from the turn map observed at turns 0, m, 2m, ..., 5m (n = 1,000, sigma = 0.03).
Fits: m known, m wrongly taken to be 1, and m unknown (marginalised over 1, 2, 3).

""" + tbl_subsample(results) + """

**4.4 The observation model: multiplicative counting error.** Curves observed as r exp(N(-s^2/2, s^2)), the way crowd counts are wrong,
fitted with additive Gaussian noise of matched overall size or with noise proportional to the level (n = 1,000).

""" + tbl_obsmodel(results) + """

**4.5 Design: interventions on r.** SBC with the natural run plus seeded runs (n = 1,000; the same cells feed section 3.5):

""" + tbl_designs_F(results) + """

**4.6 Detectors of the gate.** Section 3.4: the order test against the any-drop rule, and the ever-joined curve.
""" + reading_variations(results)


CAVEATS = """## 5. Caveats

- **Synthetic.** Nothing here says real crowds obey the law. It says what an aggregate curve could tell us about the law **if** they did,
  under favourable conditions (known denominator, continuous shares, equal turns, known noise). The structural results (3.1) do not
  depend on any prior; every number in 3.2 to 3.5 does.
- **The prior.** Crowds with at least 2% instigators, parameters in the ranges of section 2, smooth threshold families. Smooth families
  flatter extrapolation: real threshold distributions can have atoms and gaps, and Granovetter's own pair (thresholds 0 to 99, one moved
  from 1 to 2: equilibrium 100 against 1, L3964) is the limiting case in which one threshold decides the outcome and no smooth family
  would find it. The numbers are for these generators, not for crowds.
- **Information is relative to a discrete grid prior** and saturates at the grid scale (values near 0.00 mean "to within a cell"); coverage under
  a continuous truth is grid-limited where the posterior is narrower than the grid (the matched rows at sigma = 0 and large n in 3.3).
- **Engines.** The exact and lattice engines are exact; the lattice engine runs only to n = 100 and, at n = 100, with M = 40 datasets per cell
  (a coverage standard error of 0.05), so its "calibrated" there has little power. The synthetic engine is an approximation:
  slightly over-confident where it works (at n = 1,000 the central-90% coverage of the scored quantities ranges from 0.86 to 0.92) and invalid where n sigma is small. Cells marked * rest on it.
  The misspecification and ignition cells with sigma > 0 rest on it too, on the fine grids with S = 1,000 and 800; the misspecification setups have
  their own SBC at the end of 3.3, and the ignition setups were not checked (added at review).
- **The fitted grids.** The beta+atom and logit-normal grids stop at an instigator share z of 0.20 (standard) and 0.22 (fine), while those generators
  draw z up to 0.25, so about 5% of the "matched" curves of 3.3 and 3.5 have a z outside the fitted grid (added at review).
- **Multiple comparisons.** About a dozen quantities per cell and about sixty cells: a few isolated KS p-values below 0.01 are expected
  from an exact engine and are not flagged; the calibration flag uses 0.001 and 3.5 standard errors. Under exact posteriors it fires by chance in at
  most about 2% of cells (11 or 12 KS tests and as many coverages per cell), about one of the sixty (two of the 87 with the review's cells); none of
  the 20 exact and lattice cells fired, and the synthetic engine's flags are far more than chance. The AUC and coverage comparisons are descriptive,
  with marginal intervals and no paired tests; the wrong-family model's deficit against the summaries at (100, 0.03) and (300, 0.03) clears both
  intervals (added at review).
- **Observation model (4.4).** The additive fit uses sigma = 0.3 times the relative error (the error at a level of 0.3), and the two noise models
  are scored on different simulated datasets, not the same ones (added at review).
- **Selection and eligibility** (live crowds; unsaturated pairs) are my definitions and depend only on the observed curves. Quantities
  read "outside the visited range" are defined from the observed level of the curve, not from the truth.
- **The time axis.** Ten equal turns, no clock. Sections 4.2 and 4.3 show that a clock matters; the law as written has none.
- **Ignition.** The label is the realised ignition of two finite crowds; the model-based score is a population-level quantity, so its Brier
  skill is a statement about a mismatched target and the AUC is the fair comparison. The adaptive probe and the seeded runs assume that a
  crowd can be started at an exogenous share and observed again; whether any real event offers that is open (Cantoni et al. moved
  believed attendance, not attendance, L4353, and the scope of their finding is open, L4363).
- **The gate.** One parametrisation of the upper gate (a fraction nu with a Beta window); the order test takes sigma as known (an unknown
  sigma lowers its power); no test was built for the plateau-then-growth trace in the ever-joined curve, so its detectability under noise
  is not measured, only its noise-free frequency.
- **Not tested:** per-member data, heterogeneous response times, network structure (Granovetter's friend weights), more than two parts in
  a merge, and anything about whether a real crowd's F is stable between events.
"""

REPRODUCE = """## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.identifiability_crowd_report report --workers 6 --cache /tmp/idcrowd-cache   # rewrites this file; 25 to 40 minutes on six shared cores
    ~/.local/bin/uv run pytest tests/test_identifiability_crowd.py                                                    # about 30 s

Every task seeds itself from the task description, so the numbers do not depend on scheduling or on `--workers`. `--quick` cuts every
sample size (smoke run only).
"""


def _flagged_sl(results):
    """The synthetic-engine cells that are not calibrated, as 'family (n, sigma)' strings."""
    out = []
    for r in _sel(results, "sbc", engine="sl"):
        sp_ = r["spec"]
        if not sp_.get("runs") and _calibrated(r["summary"]) != "yes":
            out.append((sp_["fam"], sp_["n"], sp_["sigma"], r["summary"]["c90_min"], r["summary"]["ll_c90"]))
    return sorted(out)


def _fmt_cells(cells):
    names = {"beta": "beta+atom", "clipnorm": "clipped normal"}
    by = {}
    for fam, n, sg, *_ in cells:
        by.setdefault(fam, []).append(f"({n}, {sg:g})")
    return "; ".join(f"{names[f]} " + ", ".join(v) for f, v in by.items())


def reading_recovery(results):
    V = _facts(results)
    cc = _calib_counts(results)
    bad = _flagged_sl(results)
    lo_c90 = min(b[3] for b in bad) if bad else float("nan")
    ev = _sel(results, "sbc", engine="lattice")
    ev_diff_tau = [r["pm_diff"]["tau"] for r in ev if "pm_diff" in r]
    ev_diff_F = [r["pm_diff"]["F(0.55)"] for r in ev if "pm_diff" in r]
    sl30 = [r for r in ev if r["spec"]["n"] == 30]
    sl30_bad = sum(_calibrated(r["sl_summary"]) != "yes" for r in sl30)
    g = lambda fam, n, sg, key: V[(fam, n, sg)][key]
    return f"""
**Reading.**

- *Calibration.* The exact engine passes in {cc['exact'][0]} of {cc['exact'][1]} cells and the lattice engine in {cc['lattice'][0]} of {cc['lattice'][1]} (the n = 100 cells have 40 datasets each, so
  little power there). The synthetic engine passes in {cc['sl'][0]} of {cc['sl'][1]}; the cells where it does not are {_fmt_cells(bad)} (family (n, sigma)); the worst central-90% coverage among
  them is {lo_c90:.2f}. Against the exact lattice engine on identical datasets it fails in {sl30_bad} of {len(sl30)} cells at n = 30 and its posterior means differ from the exact ones by
  {_range(ev_diff_tau)} (tau) and {_range(ev_diff_F)} (F(0.55)) prior sds on average. So the synthetic engine is used as an approximation, flagged with a star where it is not calibrated;
  everything in this section at n <= 100 with noise rests on the lattice engine, except n = 100 with sigma = 0.01, which has only a flagged synthetic cell
  (sections 3.3 and 3.5 use the synthetic engine at every n with sigma > 0, without stars; section 2, Engines).
- *Exact counts.* The stall is read to within a twentieth of its prior sd from n = 1,000 for beta+atom (median posterior sd of tau {_f(g('beta', 300, 0.0, 'sd_tau'), 3)} at n = 300, {_f(g('beta', 1000, 0.0, 'sd_tau'), 3)} at n = 1,000) and at every n for the clipped normal
  ({_f(g('clipnorm', 30, 0.0, 'sd_tau'), 3)} at n = 30); F inside the visited range to within a quarter of its prior sd from n = 30 for beta+atom ({_f(g('beta', 30, 0.0, 'sd_F_in'))}; {_f(g('beta', 100, 0.0, 'sd_F_in'))} at n = 100) and from n = 100 for the clipped normal ({_f(g('clipnorm', 100, 0.0, 'sd_F_in'))}). The two parameters of the clipped normal are recovered from n = 100 ({_f(g('clipnorm', 100, 0.0, 'sd_params'))}) to n = 1,000 ({_f(g('clipnorm', 1000, 0.0, 'sd_params'))}); the
  three of beta+atom are still at {_f(g('beta', 1000, 0.0, 'sd_params'))} and {_f(g('beta', 3000, 0.0, 'sd_params'))} of the prior sd at n = 1,000 and 3,000: many (z, a, b) give nearly the same few points.
  F outside the visited range is the part that stays open: {_f(g('beta', 3000, 0.0, 'sd_F_out'))} (beta+atom) and {_f(g('clipnorm', 3000, 0.0, 'sd_F_out'))} (clipped normal) at n = 3,000, with an RMSE of the posterior mean of
  {_f(g('beta', 3000, 0.0, 'rmse_F_out'))} and {_f(g('clipnorm', 3000, 0.0, 'rmse_F_out'))} prior sds.
- *At sigma >= 0.03 noise sets a floor that n barely lifts.* At sigma = 0.03 the parameters stay at {_f(g('beta', 300, 0.03, 'sd_params'))}, {_f(g('beta', 1000, 0.03, 'sd_params'))}, {_f(g('beta', 3000, 0.03, 'sd_params'))} (beta+atom, n = 300, 1,000, 3,000) and at sigma = 0.1 at
  {_f(g('beta', 300, 0.1, 'sd_params'))}, {_f(g('beta', 1000, 0.1, 'sd_params'))}, {_f(g('beta', 3000, 0.1, 'sd_params'))}; for the clipped normal {_f(g('clipnorm', 300, 0.1, 'sd_params'))}, {_f(g('clipnorm', 1000, 0.1, 'sd_params'))}, {_f(g('clipnorm', 3000, 0.1, 'sd_params'))} at sigma = 0.1. The first-share F(0) is
  limited by sigma itself ({_f(g('beta', 3000, 0.1, 'sd_F0'))} at sigma = 0.1). There, beyond a few hundred members a larger crowd helps little and less noisy counts help more; at sigma = 0.01
  n still helps (clipped normal {_f(g('clipnorm', 300, 0.01, 'sd_params'))}{'' if V[('clipnorm', 300, 0.01)]['cal'] == 'yes' else '*'}, {_f(g('clipnorm', 1000, 0.01, 'sd_params'))}, {_f(g('clipnorm', 3000, 0.01, 'sd_params'))} at n = 300, 1,000, 3,000; corrected at review: this bullet said a larger crowd does not help at all).
- *Small crowds.* At n = 30 even exact counts leave the stall of a beta+atom crowd open ({_f(g('beta', 30, 0.0, 'sd_tau'))} of the prior sd; {_f(g('beta', 100, 0.0, 'sd_tau'))} at n = 100): the finite crowd's own luck, not the observer's noise, decides where it stops.
- *The intervals are honest.* In the calibrated cells with n >= 300 the central-90% coverage of F is {_range([g(f_, n_, s_, 'c90_F_in') for f_ in ('beta', 'clipnorm') for n_ in (300, 1000, 3000) for s_ in (0.0, 0.01, 0.03, 0.1) if (f_, n_, s_) in V and V[(f_, n_, s_)]['cal'] == 'yes'])} inside and
  {_range([g(f_, n_, s_, 'c90_F_out') for f_ in ('beta', 'clipnorm') for n_ in (300, 1000, 3000) for s_ in (0.0, 0.01, 0.03, 0.1) if (f_, n_, s_) in V and V[(f_, n_, s_)]['cal'] == 'yes'])} outside the visited range: the width outside is information, not a calculation error.
  A correct parametric family does not make F identifiable outside the visited range, it makes it an assumption with a calibrated width.
"""


def reading_misspec(results):
    pm_ = _pooled_mis(results, True)
    m, x = pm_["m"], pm_["x"]
    tabs = {r["spec"]["sigma"]: r for r in _sel(results, "misspec")}
    diag = {}
    for r in _sel(results, "misspec"):
        for gen in ("beta", "clipnorm", "logitnorm"):
            diag.setdefault((gen, r["spec"]["sigma"] > 0), []).append(r["cells"][gen]["confusion"][gen])
    bim_best = {}
    for r in _sel(results, "misspec"):
        c = r["cells"]["bimodal"]["confusion"]
        for f_, v in c.items():
            bim_best.setdefault(f_, []).append(v)
    pos = {s_: [r for r in _sel(results, "misspec") if r["spec"]["sigma"] == s_] for s_ in (0.01, 0.03, 0.1)}
    floor = {}
    for r in _sel(results, "misspec", sigma=0.0):
        mm, xx = [], []
        for gen, c in r["cells"].items():
            for f_ in FITTED:
                (mm if gen == f_ else xx).append(c["summ"][f_]["inside"]["cov"])
        floor[r["spec"]["n"]] = (float(np.nanmean(mm)), float(np.nanmean(xx)))

    def pooled_cov(sg, which):
        acc = []
        for r in pos[sg]:
            for gen, c in r["cells"].items():
                for f_ in FITTED:
                    if (gen == f_) == (which == "m"):
                        sm = c["summ"][f_]
                        acc.append((sm["inside"]["cov"], sm["outside"]["cov"]))
        return np.nanmean(np.array(acc), axis=0)

    return f"""
**Reading** (pooled over the cells with sigma > 0):

- *A wrong family is fitted confidently and wrongly.* The 90% interval of F covers the truth for {_f(x[1])} of readings inside the visited range and {_f(x[2])} outside when the family is wrong, against
  {_f(m[1])} and {_f(m[2])} when it matches; the RMSE of the posterior mean outside is {_f(x[4])} prior sds against {_f(m[4])}. Coverage inside falls as the data get cleaner, for both
  (sigma = 0.01, 0.03, 0.1: mismatched {_f(pooled_cov(0.01, 'x')[0])}, {_f(pooled_cov(0.03, 'x')[0])}, {_f(pooled_cov(0.1, 'x')[0])}; matched {_f(pooled_cov(0.01, 'm')[0])}, {_f(pooled_cov(0.03, 'm')[0])}, {_f(pooled_cov(0.1, 'm')[0])}), because the posterior narrows toward the grid spacing
  and, at sigma = 0.01 with n <= 1,000, because the synthetic engine is itself over-confident there (3.2); it falls much further when the family is wrong.
  The error is in the visited range too, not only above it: a family is a constraint on the whole of F.
- *The curve cannot say which family it is.* By marginal likelihood the generating family comes out first for {_range(diag[('clipnorm', True)])} of clipped-normal curves, {_range(diag[('beta', True)])} of beta+atom curves and {_range(diag[('logitnorm', True)])} of
  logit-normal curves (chance 0.33). With exact counts the clipped normal and beta+atom are recognised {_range(diag[('clipnorm', False)])} and {_range(diag[('beta', False)])} of the time, the logit-normal {_range(diag[('logitnorm', False)])}. Noise degrades it
  further: at n = 1,000, sigma = 0.1 beta+atom curves are attributed to the clipped normal more often than to beta+atom. Bimodal crowds, which have no matching family, are attributed to logit-normal
  ({_range(bim_best['logitnorm'])}) or beta+atom ({_range(bim_best['beta'])}) and least often to the clipped normal ({_range(bim_best['clipnorm'])}); the preferred family is not a diagnosis of the crowd.
- *At sigma = 0 and large n the matched coverage is a grid artefact* (matched F-inside coverage {_f(floor[100][0])} at n = 100, {_f(floor[1000][0])} at n = 1,000, {_f(floor[3000][0])} at n = 3,000; mismatched {_f(floor[100][1])}, {_f(floor[1000][1])}, {_f(floor[3000][1])}): the
  truth falls between grid points. The RMSE columns carry the comparison there.
"""


def reading_twosided(results):
    tw = _sel(results, "twosided")
    strong = [r for r in tw if r["spec"]["nu"] == 0.6]
    weak = [r for r in tw if r["spec"]["nu"] <= 0.3 and r["spec"]["wbar"] == 0.15 or r["spec"]["nu"] == 0.1]
    diff = [abs(r["rates"]["lrt"] - r["rates"]["drop"]) for r in tw]
    lrt_better = sum(r["rates"]["lrt"] > r["rates"]["drop"] + 0.02 for r in tw)
    drop_better = sum(r["rates"]["drop"] > r["rates"]["lrt"] + 0.02 for r in tw)
    return f"""
**Reading.**

- *The ceiling is high and the detectors reach little of it.* {_f(100 * min(r['rates']['ceiling'] for r in tw), 0)}% to {_f(100 * max(r['rates']['ceiling'] for r in tw), 0)}% of two-sided crowds decline somewhere in the noise-free curve, but a decline that
  stands out of the noise (a single step of 3 sigma sqrt 2) occurs in {_f(100 * min(r['rates']['big_decline'] for r in tw), 0)}% to {_f(100 * max(r['rates']['big_decline'] for r in tw), 0)}% and the order test detects {_f(100 * min(r['rates']['lrt'] for r in tw), 0)}% to {_f(100 * max(r['rates']['lrt'] for r in tw), 0)}%: power follows the share of material
  declines, not the share of declines. It is best with many wide-windowed members (nu = 0.6: {_f(100 * min(r['rates']['lrt'] for r in strong), 0)}% to {_f(100 * max(r['rates']['lrt'] for r in strong), 0)}%) and exact-ish counts (sigma = 0.01), and
  falls to {_f(100 * max(r['rates']['lrt'] for r in tw if r['spec']['sigma'] == 0.1 and r['spec']['nu'] < 0.6), 0)}% or less at sigma = 0.1 unless 60% of the members are gated.
- *No false alarms.* One-sided control crowds are rejected at {_f(100 * min(r['rates']['lrt_one'] for r in tw), 0)}% to {_f(100 * max(r['rates']['lrt_one'] for r in tw), 0)}% (order test) and {_f(100 * min(r['rates']['drop_one'] for r in tw), 0)}% to {_f(100 * max(r['rates']['drop_one'] for r in tw), 0)}% (any-drop rule) against a nominal 5%;
  both are conservative because the critical value is for the flat curve, the least favourable null.
- *Which detector.* The two agree within {_f(100 * max(diff), 0)} points everywhere; the order test is the more powerful in {lrt_better} cells and the any-drop rule in {drop_better} of {len(tw)} (by more than 2 points). Neither wins.
- *The cumulative curve.* The order test rejects the ever-joined curve at its size ({_f(100 * min(r['rates']['lrt_cum'] for r in tw), 0)}% to {_f(100 * max(r['rates']['lrt_cum'] for r in tw), 0)}%): it cannot decline. Its plateau-then-growth trace exists in {_f(100 * min(r['rates']['plateau_growth'] for r in tw), 0)}% to
  {_f(100 * max(r['rates']['plateau_growth'] for r in tw), 0)}% of crowds (most with nu = 0.6, wide windows, n = 1,000); no detector for it under noise was built.
- *What this means.* Nothing in a monotone curve, or in the stall level, separates the gates. A two-sided gate is **testable** only where it makes the crowd visibly shrink and the count error is a few percent.
"""


def reading_ignition(results):
    ig = _sel(results, "ignition")
    nat = [r for r in ig if not r["spec"].get("designs")]
    des = [r for r in ig if r["spec"].get("designs")]
    mt = lambda r: r["spec"]["gens"] == ("beta", "clipnorm")
    A_ = lambda rs, k: [r["auc"][k] for r in rs if k in r["auc"]]
    fit_m, fit_o = A_([r for r in nat if mt(r)], "bma_nat"), A_([r for r in nat if not mt(r)], "bma_nat")
    sm_m, sm_o = A_([r for r in nat if mt(r)], "summary"), A_([r for r in nat if not mt(r)], "summary")
    ref_m, ref_o = A_([r for r in nat if mt(r)], "oracle"), A_([r for r in nat if not mt(r)], "oracle")
    pr0 = A_([r for r in nat if r["spec"]["sigma"] == 0.0], "probe")
    pr3 = A_([r for r in nat if r["spec"]["sigma"] == 0.03], "probe")
    pr1 = A_([r for r in des if r["spec"]["sigma"] == 0.1], "probe")
    pr1_txt = "; ".join(f"{r['auc']['probe']:.2f} [{r['ci']['probe'][0]:.2f}, {r['ci']['probe'][1]:.2f}] "
                        f"({'matched' if mt(r) else 'other'})" for r in des if r["spec"]["sigma"] == 0.1)
    k1 = [r for r in ig if r["spec"]["n"] == 1000]
    k1_fit_m, k1_fit_o = A_([r for r in k1 if mt(r)], "bma_nat"), A_([r for r in k1 if not mt(r)], "bma_nat")
    k1_ref_m, k1_ref_o = A_([r for r in k1 if mt(r)], "oracle"), A_([r for r in k1 if not mt(r)], "oracle")
    k1_sum = A_(k1, "summary")
    worse = [(r["spec"]["n"], r["spec"]["sigma"]) for r in nat if not mt(r) and r["auc"]["bma_nat"] + 0.02 < r["auc"]["summary"]]
    better = [(r["spec"]["n"], r["spec"]["sigma"]) for r in nat if mt(r) and r["auc"]["bma_nat"] > r["auc"]["summary"] + 0.02]
    return f"""
**Reading.**

- *Ignition is predictable above chance, but not by the criterion.* From natural curves the fitted model reaches AUC {_range(fit_m)} with a matching family and {_range(fit_o)} with a wrong one; a logistic regression on curve
  summaries (final levels and initial shares, no model of F) reaches {_range(sm_m)} and {_range(sm_o)}. The fitted model beats the summaries by more than 0.02 in {len(better)} of {sum(mt(r) for r in nat)} matched cells and
  is worse by more than 0.02 in {len(worse)} of {sum(not mt(r) for r in nat)} cells with the wrong family, (n, sigma) = {', '.join(f'({n}, {s:g})' for n, s in worse)}.
  Like for like at n = 1,000 (the {len(k1)} cells of both tables): the fitted model {_range(k1_fit_m)} with the matching family, against {_range(k1_ref_m)} for the reference that knows F,
  and {_range(k1_fit_o)} with a wrong one, against {_range(k1_ref_o)}; summaries {_range(k1_sum)}. With the right family the curve comes close to the reference, because the family supplies F above the stall (added at review).
- *Even knowing F exactly, small crowds are only partly predictable.* The reference that uses the true generators' CDFs reaches {_range(ref_m)} (matched) and {_range(ref_o)} (other families), rising with n (at n = 100
  {_range([r['auc']['oracle'] for r in nat if r['spec']['n'] == 100])}, at n = 3,000 {_range([r['auc']['oracle'] for r in nat if r['spec']['n'] == 3000])}): a realised crowd of 100 differs from its F by more than the margin that decides ignition. The curve-based scores can exceed the
  reference because the curves also carry the realised crowds' own thresholds.
- *An intervention reads the necessary condition directly.* The adaptive probe (start each crowd at the higher final level, read r(1) - r(0)) reaches AUC {_range(pr0)} with exact counts, {_range(pr3)} at sigma = 0.03 and
  {_range(pr1)} at sigma = 0.1: it measures F_1(M) - M, the quantity the curves cannot supply. It reads a necessary condition, not a sufficient one, so it stops short of 1 even without noise,
  and noise of 0.1 takes it to {pr1_txt} (corrected at review: "chance-like values", which only the first is).
- *Seeded runs.* Adding one run started at r(0) = 0.5 lifts the fitted model at n = 1,000 from {_range([r['auc']['bma_nat'] for r in des if mt(r)])} to {_range([r['auc']['bma_p1'] for r in des if mt(r)])} (matching) and from
  {_range([r['auc']['bma_nat'] for r in des if not mt(r)])} to {_range([r['auc']['bma_p1'] for r in des if not mt(r)])} (wrong family); more runs add little in AUC, much in Brier skill ({_range([1 - r['brier']['bma_p4'] / r['brier']['base'] for r in des], 2)} against
  {_range([1 - r['brier']['bma_nat'] / r['brier']['base'] for r in des], 2)}). The material-ignition AUCs (second table) are similar or higher.
  The 95% intervals of one seeded run and of the natural run are disjoint in {sum(r['ci']['bma_nat'][1] < r['ci']['bma_p1'][0] for r in des)} of {len(des)} cells
  ({', '.join(f"{'matched' if mt(r) else 'other'} sigma = {r['spec']['sigma']:g}" for r in des if r['ci']['bma_nat'][1] < r['ci']['bma_p1'][0])}); in the others they overlap, and no paired test of the difference was run (added at review).
"""


def reading_variations(results):
    dyn = _sel(results, "dynamic")
    sub = _sel(results, "subsample")
    obs = _sel(results, "obsmodel")
    diag = {a: [r["res"]["share"][list(r["res"]["alphas"]).index(a)] for r in dyn if r["spec"]["alpha_true"] == a] for a in (0.25, 0.5, 0.75, 1.0)}
    wrong = []
    for r in dyn:
        d = r["res"]
        at = d["alpha_true"]
        wrong.append((d["rmse_F"][1.0] if at != 1.0 else None, d["rmse_F"][at]))
    w1 = [a for a, b in wrong if a is not None]
    wb = [b for a, b in wrong if a is not None]
    sub_unknown = [r["res"]["unknown"]["sd_F"] for r in sub]
    sub_known = [r["res"]["known"]["sd_F"] for r in sub if r["spec"]["m_true"] > 1]
    sub_assume = [r["res"]["assume1"]["sd_F"] for r in sub if r["spec"]["m_true"] > 1]
    rm_known = [r["res"]["known"]["rmse_F"] for r in sub if r["spec"]["m_true"] > 1]
    rm_assume = [r["res"]["assume1"]["rmse_F"] for r in sub if r["spec"]["m_true"] > 1]
    dcells = [r for r in _sel(results, "sbc") if r["spec"].get("runs")]
    ndes, ndes_bad = len(dcells), sum(_calibrated(r["summary"]) != "yes" for r in dcells)
    add_F = [r["res"]["additive"]["cov_F"] for r in obs]
    rel_F = [r["res"]["relative"]["cov_F"] for r in obs]
    return f"""
**Which variant fits best.**

- *Threshold family (4.1):* the generating family comes first in {_range([r['cells']['clipnorm']['confusion']['clipnorm'] for r in _sel(results, 'misspec')])} of clipped-normal curves, {_range([r['cells']['beta']['confusion']['beta'] for r in _sel(results, 'misspec')])} of beta+atom curves and
  {_range([r['cells']['logitnorm']['confusion']['logitnorm'] for r in _sel(results, 'misspec')])} of logit-normal curves across the cells; for bimodal crowds the family that comes first is wrong by construction (3.3).
- *Dynamic form (4.2):* the true alpha has the largest marginal likelihood in {_range(diag[0.25])} of curves at alpha = 0.25, {_range(diag[0.5])} at 0.5, {_range(diag[0.75])} at 0.75 and {_range(diag[1.0])} at 1.0 (the turn map). alpha = 0.75
  and 1.0 are the hardest to separate. The clock matters for F: fitting the turn map to inertial curves (alpha < 1) gives an RMSE of F of {_range(w1)} prior sds, against {_range(wb)} with the right alpha.
- *Time axis (4.3):* if the number of turns per observation is unknown the posterior sd of F is {_range(sub_unknown)} of the prior sd, against {_range(sub_known)} when it is known; assuming it is 1 when it is 2 or 3 gives a posterior
  sd of {_range(sub_assume)} (over-confident) and an RMSE of {_range(rm_assume)} against {_range(rm_known)}.
- *Observation model (4.4):* noise proportional to the level covers F inside the visited range in {_range(rel_F)} against {_range(add_F)} for additive noise (nominal 0.90) when the counting error is multiplicative.
- *Design (4.5):* the posterior sd of F outside the visited range is {_range([r['summary']['sd_F_out'] for r in _sel(results, 'sbc') if r['spec'].get('design') == 'nat'])} of the prior sd from the natural run alone and falls to
  {_range([r['summary']['sd_F_out'] for r in _sel(results, 'sbc') if r['spec'].get('design') == 'p1'])} with one seeded run, {_range([r['summary']['sd_F_out'] for r in _sel(results, 'sbc') if r['spec'].get('design') == 'p2'])} with two and {_range([r['summary']['sd_F_out'] for r in _sel(results, 'sbc') if r['spec'].get('design') == 'p4'])} with four ({ndes_bad} of the {ndes} design cells {'is' if ndes_bad == 1 else 'are'} not calibrated).
- *Gate detectors (4.6):* the order test and the any-drop rule tie (3.4).
"""



def _calib_counts(results):
    """(calibrated, total) natural-run SBC cells per engine."""
    out = {}
    for r in _sel(results, "sbc"):
        sp_ = r["spec"]
        if sp_.get("runs"):
            continue
        c, t = out.get(sp_["engine"], (0, 0))
        out[sp_["engine"]] = (c + (_calibrated(r["summary"]) == "yes"), t + 1)
    return out


def _pooled_mis(results, sigma_pos=True):
    """Matched / mismatched coverage and RMSE pooled over the misspecification cells (sigma > 0 or sigma = 0)."""
    acc = {"m": [], "x": []}
    for r in _sel(results, "misspec"):
        if (r["spec"]["sigma"] > 0) != sigma_pos:
            continue
        for gen, c in r["cells"].items():
            for f in FITTED:
                sm = c["summ"][f]
                acc["m" if gen == f else "x"].append((sm["tau"]["cov"], sm["inside"]["cov"], sm["outside"]["cov"],
                                                      sm["inside"]["rmse"], sm["outside"]["rmse"]))
    return {k: np.nanmean(np.array(v), axis=0) for k, v in acc.items()}


def verdict(results):
    V = _facts(results)
    cc = _calib_counts(results)
    vis = _sel(results, "visited")
    dr = _sel(results, "dirichlet")
    tw = _sel(results, "twosided")
    ig = _sel(results, "ignition")
    c14 = _one(results, "claim14")
    g = lambda fam, n, sg, key: V[(fam, n, sg)][key]
    pooled = _pooled_mis(results)
    pm, px = pooled["m"], pooled["x"]
    diag = {}
    for r in _sel(results, "misspec"):
        if r["spec"]["sigma"] > 0:
            for gen in ("beta", "clipnorm", "logitnorm"):
                diag.setdefault(gen, []).append(r["cells"][gen]["confusion"][gen])
    bad = _flagged_sl(results)
    ev = [r for r in _sel(results, "sbc", engine="lattice") if r["spec"]["n"] == 30]
    ev_bad = sum(_calibrated(r["sl_summary"]) != "yes" for r in ev)
    tw_ceiling = [r["rates"]["ceiling"] for r in tw]
    tw_power = [r["rates"]["lrt"] for r in tw]
    tw_pow_s = {s_: [r["rates"]["lrt"] for r in tw if r["spec"]["sigma"] == s_] for s_ in (0.01, 0.03, 0.1)}
    tw_fp = [max(r["rates"]["lrt_one"], r["rates"]["drop_one"]) for r in tw]
    tw_cum = [r["rates"]["lrt_cum"] for r in tw]
    tw_pg = [r["rates"]["plateau_growth"] for r in tw]

    def auc(kind_pred, sel):
        return [r["auc"][kind_pred] for r in ig if sel(r["spec"]) and kind_pred in r["auc"]]

    nat = lambda sp_: not sp_.get("designs")
    des = lambda sp_: bool(sp_.get("designs"))
    matched = lambda sp_: sp_["gens"] == ("beta", "clipnorm")
    a_fit_m = auc("bma_nat", lambda sp_: nat(sp_) and matched(sp_))
    a_fit_o = auc("bma_nat", lambda sp_: nat(sp_) and not matched(sp_))
    a_sum = auc("summary", lambda sp_: nat(sp_))
    a_ref_1k = auc("oracle", lambda sp_: sp_["n"] == 1000)
    a_seed_m = [r["auc"][k] for r in ig if des(r["spec"]) and matched(r["spec"]) for k in ("bma_p1", "bma_p2", "bma_p4")]
    a_seed_o = [r["auc"][k] for r in ig if des(r["spec"]) and not matched(r["spec"]) for k in ("bma_p1", "bma_p2", "bma_p4")]
    a_nat_des_m = [r["auc"]["bma_nat"] for r in ig if des(r["spec"]) and matched(r["spec"])]
    a_nat_des_o = [r["auc"]["bma_nat"] for r in ig if des(r["spec"]) and not matched(r["spec"])]
    a_probe0 = auc("probe", lambda sp_: sp_["sigma"] == 0.0)
    ds = {(r["spec"]["fam"], r["spec"]["sigma"], r["spec"]["design"]): r["summary"] for r in _sel(results, "sbc")
          if r["spec"].get("runs")}
    rm_tau = [g(f_, n_, s_, "rmse_tau") for f_ in ("beta", "clipnorm") for n_ in (1000, 3000) for s_ in (0.0, 0.01, 0.03, 0.1)]
    ff = {(f_, s_): [_first_n(results, f_, s_, key, thr) for _l, key, thr in FAIL_CRITERIA] for f_ in ("beta", "clipnorm")
          for s_ in (0.0, 0.01, 0.03, 0.1)}
    out = []
    A = out.append
    A("## Verdict\n")
    A(f"""**In short.** From the aggregate curve of a crowd the crowd law can be fitted to *where the crowd stopped*, to *the instigator share* and to *F at the few points the
curve visited* (a median of {_range([r['med'] for r in vis], 0)} points; {_range([100 * r['le3'] for r in vis], 0)}% of curves read three or fewer). It cannot be fitted, without assuming the family, to F above the curve's own stall; nor to the threshold family, to the gate's sign (except through a decline),
or to the quantity that decides ignition. The event datasets of 089 (counts or count bins, no pool) give less than this test gave the model,
so they cannot fit F, evaluate Claim 1.4's criterion or set Claim 1.11's refutation test; what would is data that move r (interventions) or per-member thresholds.
""")
    A("**Supported** (exact, or measured with the calibration shown in 3.2):\n")
    star = lambda fam, n_, s_: "" if V[(fam, n_, s_)]["cal"] == "yes" else "*"
    mf = _sel(results, "sbc", mfit=True)
    A(f"""1. *The exact engines are right; the synthetic one is right only where n sigma is large.* SBC passes in {cc['exact'][0]} of {cc['exact'][1]} exact-engine cells (n = 30 to 3,000, exact counts) and in {cc['lattice'][0]} of {cc['lattice'][1]} lattice-engine
   cells (noise, n = 30 and 100; the n = 100 cells have 40 datasets each). The synthetic (Gaussian) engine passes in only {cc['sl'][0]} of {cc['sl'][1]} cells, mostly failing at n <= 300 with sigma <= 0.03 (worst central-90% coverage
   {min(b[3] for b in bad):.2f}), and fails in {ev_bad} of {len(ev)} comparisons with the exact engine at n = 30. Its cells carry a star in 3.2; the misspecification and ignition cells with sigma > 0 (3.3, 3.5)
   also rest on it, at every n, without stars, and the misspecification setups' own SBC fails in {sum(_calibrated(r['summary']) != 'yes' for r in mf)} of {len(mf)} cells (end of 3.3; corrected at review: this item said
   the engines are right wherever they are used).""")
    A(f"""2. *Claims 1.2 and 1.4 hold on finite crowds.* No violation of Claim 1.2's equal case or Claim 1.4's necessary condition in {c14['igniting']:,} igniting pairs, nor of the sandwich in
   {c14['up_trials']} pairs or of its strictness in the {c14['strict_trials']} of them with unequal stalls, from four generators (three of them, beta, bimodal and clipped normal, also used by `models/02`'s own check, 1.8;
   corrected at review: the igniting-pair check was reported as strictness, and the generators as ones the claims were not built on).""")
    A(f"""3. *The stall is read, and F is read where the curve went.* In a correctly specified family at n = 1,000 and sigma = 0.03 the median posterior sd of the stall tau is {_f(g('clipnorm', 1000, 0.03, 'sd_tau'), 3)}{star('clipnorm', 1000, 0.03)} (clipped normal)
   and {_f(g('beta', 1000, 0.03, 'sd_tau'), 3)}{star('beta', 1000, 0.03)} (beta+atom) of its prior sd, and of F inside the visited range {_f(g('clipnorm', 1000, 0.03, 'sd_F_in'))}{star('clipnorm', 1000, 0.03)} and {_f(g('beta', 1000, 0.03, 'sd_F_in'))}{star('beta', 1000, 0.03)} (* = synthetic engine not calibrated in that cell); with exact counts at n = 3,000 all four are below 0.01. The median hides
   the near-critical crowds, where the stall is a coin toss: the RMSE of tau's posterior mean is {_range(rm_tau)} of the prior sd over the cells with n >= 1,000 (column "RMSE tau" in 3.2).""")
    A("""
**Refuted** (as claims about what an aggregate curve can do):
""")
    A(f"""4. *F above the stall is not recoverable without assuming the family.* Exactly: redrawing every threshold above the stall leaves the curve unchanged. With a non-parametric prior the posterior sd of F above the stall stays
   at {_range([r['sd_out'] for r in dr])} of the prior's from n = {min(r['spec']['n'] for r in dr)} to {max(r['spec']['n'] for r in dr):,}. In a parametric family the family's own shape fills the gap, with a width that is calibrated where the engine is (3.2): with exact counts at n = 3,000 the posterior sd of F
   outside the visited range is {_f(g('clipnorm', 3000, 0.0, 'sd_F_out'))} (clipped normal) and {_f(g('beta', 3000, 0.0, 'sd_F_out'))} (beta+atom) of the prior sd, against {_f(g('clipnorm', 3000, 0.0, 'sd_F_in'))} inside, and with noise (sigma >= 0.03, n = 300 to 3,000) it is
   {_range([g(f_, n_, s_, 'sd_F_out') for f_ in ('beta', 'clipnorm') for n_ in (300, 1000, 3000) for s_ in (0.03, 0.1)])} for both families.""")
    A(f"""5. *Recovery fails at these sample sizes* (median posterior sd above a quarter of the prior sd; the table "Where recovery fails" in 3.2). The parameters: for beta+atom at every n tested once
   sigma >= 0.01, and with exact counts below n = {_fmt_n(ff[('beta', 0.0)][1])}; for the clipped normal below n = {_fmt_n(ff[('clipnorm', 0.0)][1])} with exact counts, and at sigma = 0.1 at every n ({_range([g('clipnorm', n_, 0.1, 'sd_params') for n_ in (300, 1000, 3000)])} of the prior sd at n = 300 to 3,000).
   F above the stall: for beta+atom at every n and noise tested; for the clipped normal below n = {_fmt_n(ff[('clipnorm', 0.0)][3])} (exact counts; sigma = 0.01 as well), and at every n for sigma >= 0.03. The stall itself is open at n <= 100
   for beta+atom ({_f(g('beta', 30, 0.0, 'sd_tau'))} and {_f(g('beta', 100, 0.0, 'sd_tau'))} of the prior sd with exact counts). Noise sets the floor, not n: beta+atom's parameters sit at {_range([g('beta', n_, 0.03, 'sd_params') for n_ in (300, 1000, 3000)])} (sigma = 0.03) and
   {_range([g('beta', n_, 0.1, 'sd_params') for n_ in (300, 1000, 3000)])} (sigma = 0.1) from n = 300 to 3,000.""")
    A(f"""6. *The family cannot be learned from the curve, and a wrong one is fitted confidently.* Fitted to a different family (pooled over cells with sigma > 0), the 90% interval of F covers the truth for {_f(px[1])} of
   readings inside the visited range and {_f(px[2])} outside, against {_f(pm[1])} and {_f(pm[2])} for the matching family, and the error outside is {_f(px[4])} prior sds against {_f(pm[4])}. By marginal likelihood the generating
   family comes first for {_range(diag['clipnorm'])} of clipped-normal curves, {_range(diag['beta'])} of beta+atom curves and {_range(diag['logitnorm'])} of logit-normal curves (chance 0.33); bimodal crowds are attributed to logit-normal or
   beta+atom (no bimodal family was fitted, which is the point).""")
    k1 = [r for r in ig if r["spec"]["n"] == 1000]
    k1m = [r for r in k1 if matched(r["spec"])]
    k1o = [r for r in k1 if not matched(r["spec"])]
    A(f"""7. *Claim 1.4's criterion and Claim 1.11's test cannot be evaluated from the parts' curves.* The decisive quantity is F_1(M) at the host's stall M, above the intruder's own stall (Claim 1.2's equal case), where its curve is silent. An intruder
   redrawn above its own stall, with the same live curve, merges with the same host to the opposite outcome in {_f(100 * c14['flips_intr'] / c14['flip_trials_intr'], 0)}% of pairs (a redrawn host cannot flip it), and the sandwich's upper end moves in {_f(100 * c14['up_chg'] / c14['up_trials'], 0)}%. From natural curves ignition is predicted with AUC {_range(a_fit_m, 2)} (matching family) and
   {_range(a_fit_o, 2)} (wrong family) over n = 100 to 3,000, against {_range(a_sum, 2)} for a logistic regression on curve summaries. Like for like at n = 1,000: {_range([r['auc']['bma_nat'] for r in k1m], 2)} (matching family) against {_range([r['auc']['oracle'] for r in k1m], 2)} for a reference that knows F exactly,
   and {_range([r['auc']['bma_nat'] for r in k1o], 2)} (wrong family) against {_range([r['auc']['oracle'] for r in k1o], 2)}. So a right family predicts nearly as well as knowing F, because it supplies F above the stall by assumption, and a wrong one can do worse than the summaries
   (corrected at review: the reference was quoted at n = 1,000 against the fitted model's range over all n, and the flip rate over pairs in which no flip is possible).""")
    A(f"""8. *A two-sided gate is visible only as a decline.* Between {_f(100 * min(tw_ceiling), 0)}% and {_f(100 * max(tw_ceiling), 0)}% of two-sided crowds have any decline in the noise-free current-share curve (the ceiling, Proposition A); the order test
   detects {_f(100 * min(tw_power), 0)}% to {_f(100 * max(tw_power), 0)}% (up to {_f(100 * max(tw_pow_s[0.01]), 0)}% at sigma = 0.01, {_f(100 * max(tw_pow_s[0.03]), 0)}% at 0.03, {_f(100 * max(tw_pow_s[0.1]), 0)}% at 0.1), with false positives of at most {_f(100 * max(tw_fp), 0)}% (nominal 5%). On the cumulative (ever-joined)
   curve it rejects at its size ({_f(100 * min(tw_cum), 0)}% to {_f(100 * max(tw_cum), 0)}%); that curve's only trace is a plateau followed by growth, in {_f(100 * min(tw_pg), 0)}% to {_f(100 * max(tw_pg), 0)}% of crowds (noise-free).""")
    A(f"""
**What fixes it: interventions on r.** One run started at an exogenous share (r(0) = 0.5) takes the posterior sd of F outside the visited range from {_f(ds[('beta', 0.03, 'nat')]['sd_F_out'])} to {_f(ds[('beta', 0.03, 'p1')]['sd_F_out'])} (beta+atom, sigma = 0.03) and
from {_f(ds[('clipnorm', 0.03, 'nat')]['sd_F_out'])} to {_f(ds[('clipnorm', 0.03, 'p1')]['sd_F_out'])} (clipped normal); four runs to {_f(ds[('beta', 0.03, 'p4')]['sd_F_out'])} and {_f(ds[('clipnorm', 0.03, 'p4')]['sd_F_out'])}. The ignition AUC at n = 1,000 goes from {_range(a_nat_des_m, 2)} to {_range(a_seed_m, 2)} with matching families and from
{_range(a_nat_des_o, 2)} to {_range(a_seed_o, 2)} with wrong ones; an adaptive probe at the host's stall reaches {_range(a_probe0, 2)} with exact counts. This is the design of Cantoni et al.'s belief experiment (L4353-L4355), which moved the believed share rather than the share
itself: move the input of F and read the response. The curve alone cannot do it. The F-recovery numbers are within the right parametric family (4.5); without a family a seeded run reads F only at the points its own orbit visits.

**Not decided.** Whether real crowds follow the law at all (nothing here touches data); how the numbers change with threshold distributions that have atoms and gaps (Granovetter's own pair, L3964, is the
extreme; these generators are smooth); heterogeneous response times beyond the two variations in section 4; whether any real event offers an intervention on r (L4363 leaves the scope of the one experiment open).

**Status, by claim.**

- *Refuted:* that an aggregate curve identifies F above its own stall (exact; the non-parametric posterior is the prior at every n), the threshold family, or Claim 1.4's ignition criterion (at any n and noise level tested);
  that a fitted parametric family substitutes for that identification (above the stall it fixes F only through its own shape, to {_f(g('clipnorm', 3000, 0.0, 'sd_F_out'))} to {_f(g('beta', 3000, 0.0, 'sd_F_out'))} of the prior sd at n = 3,000 even when right, and a wrong
  one is fitted with 90% intervals that cover {_f(px[1])} to {_f(px[2])} of the truths); and that a monotone curve can show a two-sided gate.
- *Supported:* the crowd law and Claims 1.2 and 1.4 as internally consistent on finite crowds; that the stall and the visited part of F are recoverable from a clean enough curve in a correct family (exact counts,
  n >= 300 to 1,000); that interventions on r recover what passive curves cannot (F shown within the right parametric family, 4.5; with a wrong family they raise the ignition
  AUC, 3.5).
- *Not decided:* the crowd law as a description of any real crowd.
""")
    return "\n".join(out)


def write_report(results, path=RESULTS, quick=False):
    """Assemble the markdown file from the task results."""
    today = datetime.date.today().isoformat()
    head = (f"# Identifiability of the crowd law from aggregate curves, on independent synthetic crowds\n\n"
            f"_Generated {today} by `uv run python -m models.identifiability_crowd_report report` (seed {SEED}"
            f"{'; QUICK RUN, sample sizes cut, not the reported numbers' if quick else ''}). Code: "
            "`sim/models/identifiability_crowd.py` (tasks, engines), `sim/models/identifiability_crowd_report.py` (this file); checks: "
            "`sim/tests/test_identifiability_crowd.py`. No data are used: every crowd is simulated. Ledger ids are those of "
            "`identifiability_crowd.LEDGER`._\n")
    parts = [head, TESTED, verdict(results), DATA_AND_TERMS, METHOD, section_structure(results), section_recovery(results),
             section_misspec(results), section_twosided(results), section_ignition(results), section_variations(results),
             CAVEATS, REPRODUCE]
    text = "\n\n".join(p.strip("\n") for p in parts) + "\n"
    Path(path).write_text(text)
    return text


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", choices=["report"])
    ap.add_argument("--quick", action="store_true", help="cut every sample size (smoke run; not the reported numbers)")
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--cache", default=None, help="directory in which finished tasks are kept, so a run can be resumed")
    ap.add_argument("--out", default=None, help="write the markdown here instead of sim/results/identifiability_crowd.md")
    args = ap.parse_args(argv)
    print("running tasks ...", flush=True)
    results = run_all(quick=args.quick, workers=args.workers, cache=args.cache)
    write_report(results, path=args.out or RESULTS, quick=args.quick)
    print("wrote", args.out or RESULTS)


if __name__ == "__main__":
    main()
