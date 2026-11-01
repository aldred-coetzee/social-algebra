"""A reciprocity gate on the Bitcoin OTC and Alpha trust networks (models/gate_reciprocity_bitcoin.py).

THE TEST UNDER TEST.  models/00-v0.md (v0.2; the law is v0.1's) writes the dyad influence as an O-jive: zero for the partner's
level inside a band [K-, K+], bounded constants beyond [section 3 'D2' and 4.1; ledger L0857 (the form), L0853 (the model it
sits in), L0834 (the one coupling parameter with a direction, quarantined), L4367 (the linear partner term is about 0)].  The
prediction: in the Bitcoin OTC and Alpha rating data [117 section 3.4, ledger L4567-L4580; every ordered pair rated once,
L4571; opposite-sign reciprocated pairs L4572] the rating a trader GIVES back has a dead zone in the rating RECEIVED from
that counterparty.  Embeddedness is the number of common neighbours [L4825].

Three groups.
 (1) MACHINERY, synthetic data, no files needed: the loader's validation, the pairing of ratings into response pairs and
     every covariate on a hand-checked toy file, the fixed-effects absorption and the Gram-matrix fits against brute-force
     dummy-variable regression, the threshold search and cross-validation against PLANTED truths (an O-jive, a sign jump with
     two slopes, a sign-only step, a one-sided rule: the right form must win and the planted thresholds be recovered), the
     held-out prediction against an explicit refit, the cluster sandwich, Wald-test calibration, the copy-excess estimator under
     independence and under planted copying, the bootstrap, the trend test.
 (2) DATA, skipped with the fetch command when the git-ignored SNAP files are absent: the counts of 117 [L4567-L4572],
     time resolution (OTC sub-second, Alpha whole days), and the response function's headline numbers.
 (3) FINDINGS.  The v0 prediction is encoded as two tests that FAIL on the data and are recorded as strict xfails (the
     convention of Leonard's Table 1 in test_leonard_thetac.py): a failure is a finding, not something to tune away.  The
     refutations are asserted as ordinary passing tests beside them.

Seeds are fixed.  The slow end-to-end run (analyse + render + guards) runs only with GATE_RECIPROCITY_E2E=1.
"""
from __future__ import annotations

import gzip
import json
import os
import re
from pathlib import Path

import numpy as np
import pytest

from models import gate_reciprocity_bitcoin as gb

needs_data = pytest.mark.skipif(
    not gb.data_available(),
    reason="sim/data/bitcoin/*.csv.gz are absent (local-use-only, git-ignored): "
    "cd sim && ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report fetch",
)


# ================================================================== (1) machinery

TOY = np.array([   # SOURCE, TARGET, RATING, TIME : hand-checked below
    [1, 2, 1, 100], [2, 1, 5, 160], [3, 4, -10, 200], [4, 3, -10, 500], [5, 6, 2, 300], [6, 1, 3, 120],
    [1, 3, 4, 600], [4, 5, 1, 700], [5, 4, 1, 700], [2, 6, 7, 50], [4, 6, -3, 900],
], dtype=float)


def toy_ratings(platform="toy"):
    return gb.ratings_from_array(platform, TOY)


@pytest.mark.parametrize("mutate,msg", [
    (lambda a: a.__setitem__((0, 2), 0), "without 0"),
    (lambda a: a.__setitem__((0, 2), 11), "without 0"),
    (lambda a: a.__setitem__((0, 2), 2.5), "without 0"),
    (lambda a: a.__setitem__((0, 1), a[0, 0]), "self-rating"),
    (lambda a: a.__setitem__((1, slice(0, 2)), a[0, :2]), "more than once"),
    (lambda a: a.__setitem__((0, 3), np.nan), "non-finite"),
])
def test_loader_validation_rejects_malformed_files(mutate, msg):
    """The properties 117 counted and every later step relies on: integer ratings -10..10 with no zero [L4568, L4570], no
    self-rating, no ordered pair rated twice [L4571], finite times."""
    a = TOY.copy()
    mutate(a)
    with pytest.raises(ValueError, match=msg):
        gb.ratings_from_array("toy", a)
    gb.ratings_from_array("toy", TOY)    # the good file loads
    with pytest.raises(ValueError):
        gb.ratings_from_array("toy", TOY[:, :3])


def test_load_ratings_reads_a_gzip_file_and_checks_sha(tmp_path, monkeypatch):
    """The reader, the checksum guard and the missing-file message, on a toy file in a temporary data directory."""
    monkeypatch.setattr(gb, "DATA_DIR", tmp_path)
    p = tmp_path / gb.SOURCES["otc"].filename
    with gzip.open(p, "wt") as fh:
        fh.write("\n".join(",".join(f"{v:g}" if i < 3 else f"{v:.5f}" for i, v in enumerate(r)) for r in TOY) + "\n")
    R = gb.load_ratings("otc", verify=False)
    assert R.n == len(TOY) and R.platform == "otc"
    with pytest.raises(ValueError, match="sha256"):
        gb.load_ratings("otc", verify=True)
    p.unlink()
    with pytest.raises(FileNotFoundError, match="gate_reciprocity_bitcoin_report fetch"):
        gb.load_ratings("otc")


def test_fetch_refuses_a_download_with_the_wrong_checksum(tmp_path, monkeypatch):
    """fetch() verifies the recorded sha256 BEFORE writing anything; a wrong payload leaves no file behind."""
    monkeypatch.setattr(gb, "DATA_DIR", tmp_path / "bitcoin")

    class Resp:
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

        def read(self):
            return b"not the dataset"

    monkeypatch.setattr(gb.urllib.request, "urlopen", lambda url, timeout=0: Resp())
    with pytest.raises(ValueError, match="sha256 mismatch"):
        gb.fetch(("otc",))
    assert not (tmp_path / "bitcoin").exists() or not any((tmp_path / "bitcoin").iterdir())


def test_pair_structure_on_the_toy_file():
    """Hand-checked: pairs {1,2} and {3,4} are reciprocated with different times (first ratings 1->2 and 3->4), {4,5} is a TIED
    pair (same timestamp: no order, neither rating is 'initiating'), everything else is unreciprocated and initiating."""
    R = toy_ratings()
    ps = gb.pair_structure(R)
    assert ps.n_pairs_reciprocal == 3 and ps.n_pairs_tied == 1
    first = {(int(R.src[k]), int(R.dst[k])) for k in np.flatnonzero(ps.first)}
    assert first == {(1, 2), (3, 4)}
    tied = {(int(R.src[k]), int(R.dst[k])) for k in np.flatnonzero(ps.tied)}
    assert tied == {(4, 5), (5, 4)}
    init = {(int(R.src[k]), int(R.dst[k])) for k in np.flatnonzero(ps.initiating)}
    assert init == {(1, 2), (3, 4), (5, 6), (6, 1), (1, 3), (2, 6), (4, 6)}
    # every reverse index points at the swapped pair
    for k in np.flatnonzero(ps.rev >= 0):
        assert (R.src[ps.rev[k]], R.dst[ps.rev[k]]) == (R.dst[k], R.src[k])


def test_build_sample_covariates_on_the_toy_file():
    """x, y, ids, gap, the responder's habit (mean of the ratings he gave when he rated FIRST, before and over the whole
    file), the first rater's leave-one-out habit, reputation before the response and over the whole file excluding the
    response, the responder's previous rating, the copy baseline, and embeddedness, all hand-computed."""
    R = toy_ratings()
    S, info = gb.build_sample(R)
    assert info["n_response_pairs"] == 2 and info["n_pairs_tied"] == 1
    order = np.argsort(S.first)
    S = S.subset(order)                        # row 0: pair 1->2 ; row 1: pair 3->4
    assert S.first.tolist() == [1, 3] and S.resp.tolist() == [2, 4]
    assert S.x.tolist() == [1.0, -10.0] and S.y.tolist() == [5.0, -10.0]
    assert S.gap.tolist() == [60.0, 300.0]
    # responder 2 gave +7 (to 6, at t=50) as an initiating rating before t2=160; responder 4's only initiating rating is at t=900
    assert S.habit_resp[0] == 7.0 and np.isnan(S.habit_resp[1])
    assert S.habit_resp_all.tolist()[0] == 7.0 and S.habit_resp_all[1] == -3.0
    # first rater 1 also rated 3 first (+4): leave-one-out mean excluding x = 4; first rater 3 has no other initiating rating
    assert S.habit_first_loo[0] == 4.0 and np.isnan(S.habit_first_loo[1])
    # ... and from events BEFORE the response only (review 2026-11-01): 1's other initiating rating (+4, t=600) comes after
    # t2=160, so there is none; the earlier-events control set must not see it
    assert np.isnan(S.habit_first_prior[0]) and np.isnan(S.habit_first_prior[1])
    # reputation of 1: received +3 (from 6, t=120 < 160) before the response; whole file excluding y=5: (3+5-5)/1 = 3
    assert S.recv_first_prior[0] == 3.0 and S.recv_first_all[0] == 3.0
    # reputation of 3: nothing before t2=500; whole file excluding y=-10: only +4 (from 1)
    assert np.isnan(S.recv_first_prior[1]) and S.recv_first_all[1] == 4.0
    # the responder's previous rating given before the response
    assert S.prev_resp[0] == 7.0 and np.isnan(S.prev_resp[1])
    # share of the responder's initiating ratings equal to x
    assert S.copy_base.tolist() == [0.0, 0.0]
    # embeddedness: 1 and 2 share neighbour 6 (static 1); both edges to 6 were rated before t2=160 (6->1 at 120, 2->6 at 50)
    assert S.emb_static.tolist() == [1, 0] and S.emb_prior.tolist() == [1, 0]


def test_tied_sample_gives_both_orientations_and_keeps_only_tied_pairs():
    """Alpha-style ties: same timestamp, no order.  tied_sample orients each pair by a seeded coin."""
    rng = np.random.default_rng(3)
    rows = []
    for i in range(400):
        a, b = 1000 + 2 * i, 1001 + 2 * i
        rows += [[a, b, 1 + i % 5, 86400.0 * i], [b, a, 1 + (i * 3) % 5, 86400.0 * i]]
    R = gb.ratings_from_array("alpha", np.array(rows, dtype=float))
    ps = gb.pair_structure(R)
    assert ps.n_pairs_tied == 400 and ps.first.sum() == 0
    T = gb.tied_sample(R, ps, seed=1)
    assert T.n == 400
    frac = float(np.mean(T.first < T.resp))
    assert 0.4 < frac < 0.6                         # both orientations occur, fairly
    assert gb.tied_sample(R, ps, seed=1).first.tolist() == T.first.tolist()      # seeded
    assert gb.tied_sample(R, ps, seed=2).first.tolist() != T.first.tolist()


def test_history_counts_strictly_before():
    h = gb.History(np.array([7, 7, 7, 9]), np.array([3.0, 1.0, 2.0, 5.0]), np.array([30, 10, 20, 50]))
    assert h.before(7, 2.0) == (1, 10.0)            # strictly before 2.0: the event at 1.0 only
    assert h.before(7, 2.5) == (2, 30.0)
    assert h.before(7, 0.5) == (0, 0.0) and h.before(8, 9.0) == (0, 0.0)
    assert h.total(7) == (3, 60.0)
    assert h.last_before(7, 2.5) == 20.0 and np.isnan(h.last_before(7, 1.0))


def test_embeddedness_matches_brute_force_on_random_graph():
    rng = np.random.default_rng(5)
    n_nodes, m = 40, 260
    pairs = set()
    rows = []
    t = 0.0
    while len(rows) < m:
        a, b = rng.integers(0, n_nodes, 2)
        if a == b or (a, b) in pairs:
            continue
        pairs.add((a, b))
        t += rng.random() + 0.01
        rows.append([a + 1, b + 1, int(rng.choice([-3, 1, 2, 5])), t])
    R = gb.ratings_from_array("rand", np.array(rows, dtype=float))
    ps = gb.pair_structure(R)
    S, _ = gb.build_sample(R, ps)
    assert S.n > 10
    earliest = {}
    for a, b, _, tt in rows:
        for u, v in ((a, b), (b, a)):
            earliest[(u, v)] = min(earliest.get((u, v), np.inf), tt)
    nodes = {u for u, _ in earliest}
    for r in range(S.n):
        i, j, t2 = int(S.first[r]), int(S.resp[r]), S.t2[r]
        common = [k for k in nodes if (i, k) in earliest and (j, k) in earliest and k not in (i, j)]
        assert S.emb_static[r] == len(common)
        assert S.emb_prior[r] == sum(1 for k in common if earliest[(i, k)] < t2 and earliest[(j, k)] < t2)
    assert np.all(S.emb_prior <= S.emb_static)
    # review 2026-11-01: the first rater's habit from events before the response only, by brute force (x itself excluded)
    ini = np.flatnonzero(ps.initiating)
    finite = 0
    for r in range(S.n):
        i, j, t2 = int(S.first[r]), int(S.resp[r]), S.t2[r]
        vals = [R.rating[k] for k in ini if R.src[k] == i and R.dst[k] != j and R.time[k] < t2]
        allv = [R.rating[k] for k in ini if R.src[k] == i and R.dst[k] != j]
        if vals:
            finite += 1
            assert S.habit_first_prior[r] == pytest.approx(np.mean(vals))
        else:
            assert np.isnan(S.habit_first_prior[r])
        assert (np.isnan(S.habit_first_loo[r]) and not allv) or S.habit_first_loo[r] == pytest.approx(np.mean(allv))
    assert 0 < finite < S.n


def test_absorb_matches_dummy_regression_one_and_two_way():
    """Group-mean removal equals regressing on group dummies (Frisch-Waugh), one-way exactly, two-way to tolerance."""
    rng = np.random.default_rng(0)
    n = 700
    g1, g2 = rng.integers(0, 60, n), rng.integers(0, 35, n)
    V = rng.normal(size=(n, 4)) + g1[:, None] * 0.1
    A = gb.absorb(V, [g1])
    for k in range(4):
        for u in np.unique(g1):
            assert abs(A[g1 == u, k].mean()) < 1e-12
    D = np.column_stack([(g1 == u).astype(float) for u in np.unique(g1)] + [(g2 == u).astype(float) for u in np.unique(g2)[1:]])
    y = V[:, 0]
    resid = y - D @ np.linalg.lstsq(D, y, rcond=None)[0]
    assert np.abs(gb.absorb(V[:, [0]], [g1, g2])[:, 0] - resid).max() < 1e-8
    assert np.array_equal(gb.absorb(V, []), V)


def synth(truth="odjive", n_resp=400, per=7, seed=0, noise=1.0, resp_sd=1.5):
    """Responder-effect data with a PLANTED response function f(x); returns (x, y, resp)."""
    rng = np.random.default_rng(seed)
    resp = np.repeat(np.arange(n_resp), per)
    alpha = rng.normal(0, resp_sd, n_resp)[resp]
    vals = np.array([-10, -5, -2, -1, 1, 2, 3, 4, 5, 6, 8, 10])
    p = np.array([.04, .02, .02, .02, .30, .14, .10, .08, .08, .06, .06, .08])
    x = rng.choice(vals, size=len(resp), p=p / p.sum()).astype(float)
    f = {
        "odjive": np.where(x <= -2, -6.0, 0.0) + np.where(x >= 3, 3.0, 0.0),                       # K- = -2, K+ = 3, bounded steps
        "graded": np.where(x < 0, -6.0 + 0.8 * (x + 1), 0.8 * (x - 1)),                          # sign jump, slope 0.8 each side, no band
        "signonly": np.where(x < 0, -6.0, 0.0),
        "posonly": np.maximum(x - 3, 0.0) * 1.0,
        "null": np.zeros_like(x),
    }[truth]
    y = alpha + f + noise * rng.normal(size=len(x))
    return x, y, resp


def make_sample(x, y, resp, first=None, year=None, t1=None, t2=None):
    n = len(x)
    nan = np.full(n, np.nan)
    first = np.arange(n) + 10 ** 6 if first is None else first
    t1 = np.zeros(n) if t1 is None else t1
    t2 = np.ones(n) if t2 is None else t2
    year = np.full(n, 2012) if year is None else year
    z = np.zeros(n, dtype=np.int64)
    return gb.Sample("synthetic", np.asarray(x, float), np.asarray(y, float), np.asarray(resp, np.int64), np.asarray(first, np.int64),
                     t1, t2, year, z, z.copy(), nan, nan, nan, nan, nan, nan, nan, nan)


def test_engine_fits_equal_dummy_variable_least_squares():
    """Gram-matrix fits on FE-absorbed data equal explicit regression on responder dummies: coefficients and RSS."""
    x, y, resp = synth("graded", n_resp=60, per=6, seed=1)
    eng = gb.Engine(x, y, [gb.contiguous(resp)])
    D = np.column_stack([(resp == u).astype(float) for u in np.unique(resp)])
    names, Z = gb.column_bank(x)
    for cols in (["lin"], ["Ph1", "Ns1", "Nh1"], ["Ps3", "Ns2"], ["Cl6", "Ns1"], ["p_slope14", "p_hi58", "p_hi910", "p_neg"]):
        X = np.column_stack([D] + [Z[:, names.index(c)] for c in cols])
        b = np.linalg.lstsq(X, y, rcond=None)[0]
        rss = float(np.sum((y - X @ b) ** 2))
        fit = eng.fit_cols("test", None, cols)
        assert fit.rss == pytest.approx(rss, rel=1e-9)
        assert np.allclose(fit.coef, b[-len(cols):], atol=1e-8)
        assert fit.k == len(cols)
    assert eng.fit_cols("null", None, []).rss == pytest.approx(float(np.sum(gb.absorb(y, [resp]) ** 2)), rel=1e-12)


def test_dead_zone_graded_with_the_one_rating_band_is_a_two_slope_curve_with_a_knee_at_two():
    """A step at +2 plus the slope after it (Ps2, Ph2) spans the same functions as a line through +1 plus a change of slope at
    +2 (Ph1, Ph2), because (x - 1)+ = 1[x >= 2] + (x - 2)+ for x >= 1.  So the dead-zone fit with K+ = 2, K- = 1 is NOT a
    different kind of curve from a no-band two-slope curve: equal residual sums of squares, to rounding, on any data; and on a
    pure ramp with no band at all the graded search still lands on (2, 1), by nesting, while the continuous form takes its
    narrowest band, knots +1 and -1 (a hinge cannot have an empty band: see the next test)."""
    for seed in (1, 2, 3):
        x, y, resp = synth("graded", n_resp=200, per=6, seed=seed)
        eng = gb.Engine(x, y, [gb.contiguous(resp)])
        a = eng.fit_cols("a", None, ["Ps2", "Ph2", "Ns1", "Nh1"])
        b = eng.fit_cols("b", None, ["Ph1", "Ph2", "Ns1", "Nh1"])
        assert a.rss == pytest.approx(b.rss, rel=1e-9)
        assert eng.fit_form("D", "graded").rss <= eng.fit_form("T", "graded").rss + 1e-9
    x, y, resp = synth("graded", n_resp=500, per=8, seed=20)
    eng = gb.Engine(x, y, [gb.contiguous(resp)])
    g = eng.search("D", "graded")[0].cand
    h = eng.search("D", "hinge")[0].cand
    s_ = eng.search("D", "step")[0].cand
    assert (g.kp, g.kn) == (2, 1) and (h.kp, h.kn) == (1, 1) and s_.kp >= 4          # a step stands in for a ramp at an interior K+
    assert eng.fit_form("knee2", None).thr[0] >= 2


def test_a_hinge_is_zero_at_its_knot_so_its_narrowest_band_holds_minus_one_and_plus_one():
    """Found at review (2026-11-01).  A hinge max(x - K, 0) is zero AT its knot, so the two-sided hinge at the origin (knots +1
    and -1) gives the ratings -1 and +1 the same response: it is flat over {-1, +1}, a band of two observed ratings, not 'no
    dead zone' as it was labelled.  Step and graded sides are active at their threshold, so their (1, 1) band is empty."""
    x = np.array([-2, -1, 1, 2], dtype=float)
    names, Z = gb.column_bank(x)
    th = gb.candidates("T", "hinge")[0]
    cols = Z[:, [names.index(c) for c in th.cols]]
    assert np.array_equal(cols[1], cols[2])                              # x = -1 and x = +1: identical design rows
    assert th.band_values == 2
    for sh in ("step", "graded"):
        assert gb.candidates("T", sh)[0].band_values == 0
    dh = gb.candidates("D", "hinge")
    assert min(c.band_values for c in dh) == 2 and (dh[0].kp, dh[0].kn) == (1, 1)
    thr = np.array([[1, 1]] * 9 + [[2, 1]])
    h, g = gb.threshold_distribution(thr, "hinge"), gb.threshold_distribution(thr, "graded")
    assert h["empty"] == 0.0 and h["narrowest"] == 0.9 and g["empty"] == 0.9 == g["narrowest"]
    assert "flat over {-1, +1}" in gb.form_label("T", "hinge") and "no dead zone" in gb.form_label("T", "graded")


def test_increment_test_sees_a_step_on_top_of_a_line_and_not_a_line_alone():
    """Found at review: flatness tests the association, and a shared view of the deal adds slope inside any band.  An O-jive
    step on top of a LINEAR association still shows as an excess increment.  On a planted line (0.8 per point) the
    equal-increments test over +1..+4 keeps about its nominal size; with a step of +1.5 at +3 on top of the line it rejects."""
    rej = 0
    for s in range(40):
        x, y, resp = synth("graded", n_resp=150, per=6, seed=500 + s)
        rej += gb.increment_test(make_sample(x, y, resp))["p"] < 0.05
    assert rej / 40 <= 0.15
    x, y, resp = synth("graded", n_resp=400, per=8, seed=900)
    r = gb.increment_test(make_sample(x, y + 1.5 * (x >= 3), resp))
    assert r["p"] < 1e-4 and r["inc"][1] > r["inc"][0] + 1.0
    assert r["inc45"] == pytest.approx(0.8, abs=0.3)                       # the line continues from +4 to +5


def test_year_trend_weighs_the_year_to_year_scatter():
    """Found at review: a pooled trend SE allows no year-to-year scatter about the line.  On yearly estimates that lie on a line
    the WLS slope is recovered with no lack of fit and no inflation; one off-line year (as the OTC 9-10 level in 2015) shows as
    lack of fit and inflates the SE; rows without estimates are skipped and fewer than three years give None."""
    years = [2011, 2012, 2013, 2014, 2015]
    rows = [dict(year=y, est={"a": 1.0 + 0.1 * (y - 2013)}, se={"a": 0.05}) for y in years]
    t = gb.year_trend(rows, "a")
    assert t["slope"] == pytest.approx(0.1) and t["lof"] == pytest.approx(0.0, abs=1e-9) and t["se_infl"] == pytest.approx(t["se"])
    rows[-1]["est"]["a"] = 3.0
    t2 = gb.year_trend(rows, "a")
    assert t2["p_lof"] < 0.01 and t2["se_infl"] > 3 * t2["se"]
    assert gb.year_trend(rows[:2], "a") is None
    assert gb.year_trend([dict(year=2010, pairs=3)] + rows, "a")["years"] == years


def test_search_recovers_planted_odjive_thresholds_and_form_ranking():
    """A planted step O-jive (dead zone between -1 and +2, bounded constants -6 below -2 and +3 from 3): the D-step search
    recovers (K+, K-) = (3, 2) exactly; it beats the sign-only step, the one-sided steps and the linear form in-sample; and
    the null of no response is far behind."""
    x, y, resp = synth("odjive", n_resp=500, per=8, seed=2)
    eng = gb.Engine(x, y, [gb.contiguous(resp)])
    fit, rss, cands = eng.search("D", "step")
    assert (fit.cand.kp, fit.cand.kn) == (3, 2)
    fits = eng.fit_all(gb.PRESPEC_FORMS)
    d = fits[("D", "step")]
    for key in (("T", "step"), ("O+", "step"), ("O-", "step"), ("linear", None), ("null", None)):
        assert d.rss < fits[key].rss * 0.9, key
    assert d.ic("bic") < min(fits[k].ic("bic") for k in fits if k[0] in ("T", "O+", "O-", "linear", "null"))
    # tie-breaking prefers the narrowest band: candidates list is sorted by band width first
    assert [c.band_values for c in cands] == sorted(c.band_values for c in cands)


@pytest.mark.parametrize("truth,expect", [("graded", ("T", "graded")), ("signonly", ("T", "step")), ("posonly", ("O+", "hinge"))])
def test_cross_validation_prefers_the_planted_form(truth, expect):
    """Out-of-sample, with the thresholds re-chosen in every training fold, the planted form (or one nesting it with
    nothing to gain) is within one SE of the best pre-specified form and clearly beats the null."""
    x, y, resp = synth(truth, n_resp=300, per=8, seed=4)
    cv = gb.cv_losses(x, y, resp, forms=gb.PRESPEC_FORMS, K=10, repeats=2, seed=7)
    keys = [k for k in cv if isinstance(k, tuple) and k[0] != "saturated"]
    best = min(keys, key=lambda k: np.nanmean(cv[k]))
    d, se = gb.paired_diff(cv[expect], cv[best], resp)
    assert d <= max(2 * se, 0.02), (truth, expect, best, d, se)
    assert np.nanmean(cv[expect]) < np.nanmean(cv[("null", None)]) * 0.8 or truth == "null"


def test_cross_validation_odjive_truth_makes_dstep_beat_tstep_and_linear():
    x, y, resp = synth("odjive", n_resp=400, per=8, seed=6)
    cv = gb.cv_losses(x, y, resp, forms=gb.PRESPEC_FORMS, K=10, repeats=2, seed=1)
    for other in (("T", "step"), ("linear", None), ("O+", "step"), ("O-", "step")):
        d, se = gb.paired_diff(cv[other], cv[("D", "step")], resp)
        assert d > 3 * se, (other, d, se)


def test_cv_scores_identical_rows_for_every_form_and_is_seeded():
    x, y, resp = synth("graded", n_resp=80, per=3, seed=8)
    a = gb.cv_losses(x, y, resp, forms=gb.PRESPEC_FORMS, K=10, repeats=2, seed=3)
    b = gb.cv_losses(x, y, resp, forms=gb.PRESPEC_FORMS, K=10, repeats=2, seed=3)
    rows = a["rows_scored"]
    for k in a:
        if isinstance(k, tuple):
            assert np.array_equal(np.isfinite(a[k]), rows)                 # paired: same rows for every form
            assert np.allclose(a[k][rows], b[k][rows])                      # seeded
    assert a["n_scored"] == rows.sum() and rows.sum() <= len(x)


def test_predict_fold_equals_an_explicit_dummy_refit():
    """Held-out prediction yhat = ybar_g + (w - wbar_g).b equals fitting the dummy-variable regression on the training rows
    and predicting the held-out rows of the same responders; rows of responders with no training row are NaN."""
    x, y, resp = synth("graded", n_resp=40, per=5, seed=9)
    n = len(x)
    rng = np.random.default_rng(2)
    te = rng.random(n) < 0.25
    te |= resp == 0                                   # responder 0 entirely held out
    tr = ~te
    gtr = gb.contiguous(resp[tr])
    bank = gb.column_bank(x)
    eng = gb.Engine(x[tr], y[tr], [gtr], bank=(bank[0], bank[1][tr]))
    fit = eng.fit_cols("test", None, ["Ph1", "Ns1", "Nh1"])
    lut = {u: i for i, u in enumerate(np.unique(resp[tr]))}
    tg = [np.array([lut.get(u, -1) for u in resp[te]])]
    W_te = np.column_stack([bank[1][te]])
    pred = gb.predict_fold(eng, W_te, tg, fit)
    cols = [bank[0].index(c) for c in ["Ph1", "Ns1", "Nh1"]]
    users = np.unique(resp[tr])
    Dtr = np.column_stack([(resp[tr] == u).astype(float) for u in users])
    X = np.column_stack([Dtr, bank[1][tr][:, cols]])
    b = np.linalg.lstsq(X, y[tr], rcond=None)[0]
    for r, (u, row) in enumerate(zip(resp[te], bank[1][te][:, cols])):
        if u in lut:
            want = b[list(users).index(u)] + row @ b[len(users):]
            assert pred[r] == pytest.approx(want, abs=1e-7)
        else:
            assert np.isnan(pred[r])


def test_cluster_cov_matches_a_manual_sandwich():
    x, y, resp = synth("graded", n_resp=50, per=6, seed=10)
    eng = gb.Engine(x, y, [gb.contiguous(resp)])
    fit = eng.fit_cols("p", None, ["Ph1", "Ns1", "Nh1"])
    cov = eng.cluster_cov(fit, resp)
    names, Z = gb.column_bank(x)
    Xt = gb.absorb(Z[:, [names.index(c) for c in ["Ph1", "Ns1", "Nh1"]]], [resp])
    yt = gb.absorb(y, [resp])
    b = np.linalg.solve(Xt.T @ Xt, Xt.T @ yt)
    e = yt - Xt @ b
    meat = np.zeros((3, 3))
    for u in np.unique(resp):
        s = Xt[resp == u].T @ e[resp == u]
        meat += np.outer(s, s)
    G, N, K = len(np.unique(resp)), len(y), 3
    want = G / (G - 1) * (N - 1) / (N - K) * np.linalg.inv(Xt.T @ Xt) @ meat @ np.linalg.inv(Xt.T @ Xt)
    assert np.allclose(cov, want, rtol=1e-8, atol=1e-12)
    assert np.allclose(fit.coef, b, atol=1e-9)


def test_wald_flatness_test_has_power_and_roughly_correct_size():
    """Flatness over {1, 2}: with a PLANTED flat band the Wald test rejects at about its nominal 5% rate; with a planted
    slope it rejects almost always."""
    rej_null, rej_alt = 0, 0
    reps = 80
    for s in range(reps):
        x, y, resp = synth("null", n_resp=120, per=6, seed=100 + s)
        flat = gb.flatness_tests(make_sample(x, y, resp))[0]
        rej_null += flat["p"] < 0.05
        x, y, resp = synth("graded", n_resp=120, per=6, seed=300 + s)
        rej_alt += gb.flatness_tests(make_sample(x, y, resp))[0]["p"] < 0.05
    assert 0.0 <= rej_null / reps <= 0.14
    assert rej_alt / reps > 0.95


def test_ols_with_fixed_effects_equals_dummies_and_wald_statistic():
    x, y, resp = synth("graded", n_resp=70, per=5, seed=12)
    X = gb.category_columns(x)
    ols = gb.OLS(X, y, [gb.contiguous(resp)], resp, list(gb.CAT_NAMES))
    D = np.column_stack([(resp == u).astype(float) for u in np.unique(resp)])
    keep = X.std(axis=0) > 0
    b = np.linalg.lstsq(np.column_stack([D, X[:, keep]]), y, rcond=None)[0][-int(keep.sum()):]
    assert np.allclose(ols.coef, b, atol=1e-8)
    R = np.eye(len(ols.coef))[:2]
    chi2, df, p = ols.wald(R)
    assert df == 2 and chi2 == pytest.approx(float(ols.coef[:2] @ np.linalg.solve(ols.cov[:2, :2], ols.coef[:2])))
    assert 0 <= p <= 1


def test_profile_columns_definition():
    x = np.array([-10, -1, 1, 2, 4, 5, 8, 9, 10], dtype=float)
    P = gb.profile_columns(x)
    assert P[:, 0].tolist() == [0, 0, 0, 1, 3, 0, 0, 0, 0]          # slope over 1..4, zero at the base +1
    assert P[:, 1].tolist() == [0, 0, 0, 0, 0, 1, 1, 0, 0]          # 5..8
    assert P[:, 2].tolist() == [0, 0, 0, 0, 0, 0, 0, 1, 1]          # 9..10
    assert P[:, 3].tolist() == [1, 1, 0, 0, 0, 0, 0, 0, 0]          # negative
    names, Z = gb.column_bank(x)
    assert np.array_equal(Z[:, names.index("p_slope14")], P[:, 0])


def test_column_bank_forms_have_the_stated_shapes():
    x = np.array([-10, -2, -1, 1, 2, 3, 7, 10], dtype=float)
    names, Z = gb.column_bank(x)
    col = lambda n: Z[:, names.index(n)]  # noqa: E731
    assert col("Ps3").tolist() == [0, 0, 0, 0, 0, 1, 1, 1]            # active from +3
    assert col("Ph3").tolist() == [0, 0, 0, 0, 0, 0, 4, 7]            # (x - 3)+
    assert col("Ns2").tolist() == [1, 1, 0, 0, 0, 0, 0, 0]            # active from -2 downward
    assert col("Nh1").tolist() == [9, 1, 0, 0, 0, 0, 0, 0]            # (-1 - x)+
    assert col("Cl7").tolist() == [-7, -2, -1, 1, 2, 3, 7, 7]
    assert col("Cp7").tolist() == [0, 0, 0, 1, 2, 3, 7, 7]
    assert "Ps1" not in names                                          # K+ = 1 has no step column (it is the sign step)
    assert [c.cols for c in gb.candidates("T", "step")] == [("Ns1",)]
    assert [c.cols for c in gb.candidates("T", "graded")] == [("Ph1", "Ns1", "Nh1")]
    d = gb.candidates("D", "graded")
    assert any(c.kp == 2 and c.kn == 1 and c.cols == ("Ps2", "Ph2", "Ns1", "Nh1") for c in d)
    assert all(c.family == "D" for c in d) and len(d) == 100


def test_bootstrap_draw_resamples_whole_clusters():
    cluster = np.repeat(np.arange(30), np.arange(1, 31) % 4 + 1)
    rows_of = gb.cluster_rows(cluster)
    assert sum(len(r) for r in rows_of) == len(cluster)
    idx, new = gb.bootstrap_draw(rows_of, np.random.default_rng(0))
    assert len(new) == len(idx) and new.max() == len(rows_of) - 1
    for g in np.unique(new):
        members = idx[new == g]
        assert len(np.unique(cluster[members])) == 1                  # each new cluster is one old cluster
        assert len(members) == (cluster == cluster[members[0]]).sum()  # complete


def test_trend_test_recovers_a_planted_trend_in_the_slope():
    rng = np.random.default_rng(1)
    n_resp, per = 300, 8
    resp = np.repeat(np.arange(n_resp), per)
    year = rng.integers(2011, 2016, len(resp)).astype(float)
    x = rng.choice([1, 2, 3, 4, 5, 8], size=len(resp)).astype(float)
    slope = 0.7 + 0.1 * (year - 2013)
    y = rng.normal(0, 1.5, n_resp)[resp] + slope * np.where(x <= 4, x - 1, 3) + rng.normal(size=len(resp))
    S = make_sample(x, y, resp, year=year.astype(int))
    t = gb.trend_test(S, S.year.astype(float))
    est, se = t["slope14"]
    assert abs(est - 0.1) < 3 * se + 0.02 and est / se > 3


def test_copy_excess_is_zero_under_independence_and_recovers_planted_copying():
    """If a responder draws his rating from his own habit whatever he received, the copy excess is about 0; if half of the
    responses are copies of x it is about 0.5 (the estimator (obs - base) / (1 - base))."""
    rng = np.random.default_rng(4)
    n, n_resp = 6000, 800
    resp = rng.integers(0, n_resp, n)
    x = rng.choice([1, 2, 3], size=n, p=[.5, .3, .2]).astype(float)
    # the responder's initiating ratings: 12 draws from his own habit distribution
    prof = {u: rng.choice([1, 2, 3], size=12, p=[.7, .2, .1]) for u in range(n_resp)}
    y_ind = np.array([rng.choice(prof[u]) for u in resp], dtype=float)
    S = make_sample(x, y_ind, resp)
    S.copy_base = np.array([np.mean(prof[u] == xx) for u, xx in zip(resp, x)])
    rows = {r["x"]: r for r in gb.copy_excess(S, xs=(1, 2, 3), B=60, seed=1)}
    for v in (1, 2, 3):
        assert abs(rows[v]["pi"]) < 0.08 and rows[v]["lo"] < 0.02 < rows[v]["hi"] + 0.05
    S.y = np.where(rng.random(n) < 0.5, x, y_ind)
    rows = {r["x"]: r for r in gb.copy_excess(S, xs=(1, 2, 3), B=60, seed=1)}
    for v in (1, 2, 3):
        assert abs(rows[v]["pi"] - 0.5) < 0.08


def test_reversed_sample_swaps_roles():
    x, y, resp = synth("graded", n_resp=20, per=3, seed=3)
    first = np.arange(len(x)) // 2
    S = make_sample(x, y, resp, first=first)
    R = S.reversed()
    assert np.array_equal(R.x, S.y) and np.array_equal(R.y, S.x) and np.array_equal(R.resp, S.first) and np.array_equal(R.first, S.resp)
    assert np.all(np.isnan(R.habit_resp)) and np.all(np.isnan(R.copy_base))


def test_fe_mask_and_cap_per_responder():
    g = np.array([1, 1, 2, 3, 3, 3, 4])
    assert gb.fe_mask(g).tolist() == [True, True, False, True, True, True, False]
    assert gb.fe_mask(g, np.array([1, 1, 1, 1, 0, 0, 1], dtype=bool)).tolist() == [True, True, False, False, False, False, False]
    x, y, resp = synth("null", n_resp=30, per=7, seed=1)
    S = make_sample(x, y, resp)
    C = gb.cap_per_responder(S, 3, seed=1)
    assert C.n == 30 * 3 and np.bincount(C.resp).max() == 3
    assert gb.cap_per_responder(S, 3, seed=1).y.tolist() == C.y.tolist()


def test_threshold_distribution_and_paired_diff():
    thr = np.array([[2, 1]] * 7 + [[3, 1]] * 2 + [[1, 1]])
    d = gb.threshold_distribution(thr)
    assert d["kp"] == {1: 0.1, 2: 0.7, 3: 0.2} and d["kn"] == {1: 1.0} and d["empty"] == 0.1 and d["modal"][0] == ((2, 1), 0.7)
    la, lb = np.array([2.0, 3.0, np.nan, 4.0]), np.array([1.0, 1.0, 5.0, 4.0])
    m, se = gb.paired_diff(la, lb, np.array([0, 0, 1, 2]))
    assert m == pytest.approx(1.0) and se >= 0                       # NaN rows dropped: mean of (1, 2, 0)


def test_response_rates_drop_unanswerable_first_ratings():
    """Extensive margin: first ratings of the last `window` days are dropped; answered = a reverse rating inside the window."""
    day = 86400.0
    rows = [[1, 2, 1, 0.0], [2, 1, 1, 0.5 * day],                    # answered in half a day
            [3, 4, 1, 0.0], [4, 3, 1, 5 * day],                      # answered after 5 days: not inside a 1-day window
            [5, 6, -10, 0.0],                                        # never answered
            [7, 8, 1, 10 * day]]                                     # inside the last window: dropped
    R = gb.ratings_from_array("t", np.array(rows, dtype=float))
    ps = gb.pair_structure(R)
    r1 = {r["bin"]: r for r in gb.response_rates(R, ps, 1.0)}
    assert r1[(1, 1)]["n"] == 2 and r1[(1, 1)]["answered"] == 1      # (1->2) answered, (3->4) not; (7->8) dropped
    assert r1[(-10, -10)]["n"] == 1 and r1[(-10, -10)]["answered"] == 0
    r30 = {r["bin"]: r for r in gb.response_rates(R, ps, 6.0)}
    assert r30[(1, 1)]["answered"] == 2


def test_stratified_profile_drops_small_strata_and_keeps_order():
    x, y, resp = synth("graded", n_resp=120, per=6, seed=11)
    S = make_sample(x, y, resp)
    idx = np.arange(S.n)
    strata = np.where(idx % 50 == 0, "tiny", np.where(idx % 2 == 0, "b", "a"))
    res = gb.stratified_profile(S, strata, min_n=100, order=["b", "a", "tiny"])
    assert res["labels"] == ["b", "a"] and list(res["too_small"]) == ["tiny"] and res["too_small"]["tiny"] == int((strata == "tiny").sum())
    assert gb.strata_param(res, "tiny", "slope14") is None
    for lab in ("a", "b"):
        est, se = gb.strata_param(res, lab, "slope14")
        assert abs(est - 0.8) < 4 * se + 0.05                          # the planted slope (0.8 per point) in each stratum
    w = gb.strata_equal(res, "slope14")
    assert w is not None and w[1] == 1 and w[2] > 0.001                # same planted slope in both strata


def synth_network(seed=0, n_nodes=700, n_init=9000):
    """A synthetic rating network with a PLANTED response: a fraction of first ratings are answered after an exponential delay
    with y = alpha_v + 0.8 (min(x, 4) - 1) for positive x, + a sign jump of -6 for negative x, plus noise, where alpha_v is a trait
    of the responder v that also sets his habit of rating when he rates first."""
    rng = np.random.default_rng(seed)
    alpha = rng.choice([1.0, 1.0, 1.0, 2.0, 3.0], size=n_nodes + 1)
    vals = np.array([-10, -3, 1, 2, 3, 4, 5, 8])
    probs = np.array([.03, .02, .45, .17, .11, .08, .08, .06])
    seen, rows, t = set(), [], 0.0
    while len(seen) < n_init:
        u, v = rng.integers(1, n_nodes + 1, 2)
        if u == v or (u, v) in seen or (v, u) in seen:
            continue
        seen.add((u, v))
        t += rng.exponential(2000.0)
        x = int(rng.choice(vals, p=probs)) if rng.random() < 0.5 else int(np.clip(round(alpha[u]), 1, 10))   # the initiator's habit half the time
        rows.append([u, v, x, t])
        if rng.random() < 0.6:
            f = -6.0 if x < 0 else 0.8 * (min(x, 4) - 1)
            y = int(np.clip(round(alpha[v] + f + rng.normal(0, 0.7)), -10, 10))
            y = y if y != 0 else (1 if x > 0 else -1)
            rows.append([v, u, y, t + rng.exponential(5000.0) + 1.0])
    return np.array(rows, dtype=float)


def test_pipeline_recovers_a_planted_response_from_raw_ratings():
    """Raw ratings -> pairs -> covariates -> control sets -> profile: the planted slope (0.8 per point over 1-4) and the sign
    jump (about -6 against +1) come back under responder effects, under two sets of effects, and under habit covariates; the
    dead-zone fit does not invent a band wider than the planted one-rating reference; the flat-band test rejects."""
    R = gb.ratings_from_array("synthetic", synth_network(1))
    ps = gb.pair_structure(R)
    S, info = gb.build_sample(R, ps)
    assert info["n_response_pairs"] > 2000 and info["n_pairs_tied"] == 0
    for spec in ("fe", "fe2", "cov_all", "cov_prior", "fe_inertia"):
        r = gb.spec_summary(S, spec)
        assert r is not None, spec
        assert abs(r["est"]["slope14"] - 0.8) < 0.15, (spec, r["est"])
        assert -8.0 < r["est"]["neg"] < -4.0, (spec, r["est"])
    D = gb.sample_fe(S)
    assert gb.flatness_tests(S)[0]["p"] < 1e-6
    off = {r["x"]: r for r in gb.habit_offset_table(S, xs=(1, 2, 3), min_n=30)}
    assert abs(off[1]["mean"]) < 0.25 and 0.4 < off[2]["mean"] < 1.2          # +1 is the zero-influence point against the habit
    eng = gb.Engine(D.x, D.y, [gb.contiguous(D.resp)])
    assert gb.PROFILE_NAMES == ("slope14", "hi58", "hi910", "neg")
    cur = {r["bin"]: r for r in gb.curve_table(S)}
    assert cur[(1, 1)]["shift"] == 0.0 and cur[(2, 2)]["shift"] == pytest.approx(0.8, abs=0.25)
    yt = {r["year"]: r for r in gb.year_table(S, min_n=50)}
    assert all(r["fe_rows"] >= 0 for r in yt.values())
    alt = gb.profile_alt_se(D)
    assert set(alt) == {"resp", "first", "two_way"} and all(alt[k]["slope14"] > 0 for k in alt)
    sm = gb.sign_margin(S)
    assert sm["p_neg_after_neg"] > 0.9 and sm["p_neg_after_pos"] < 0.05
    chi2, df, p = gb.wald_any_response(S)
    assert 5 <= df <= 12                                                     # categories absent from the synthetic file are dropped
    assert p < 1e-6 and gb.gap_summary(S)["share_le_1d"] > 0.9
    sc = gb.signal_coding_cv(S, repeats=1)
    assert sc is not None and sc["mse"]["x bins (saturated in x)"] < sc["null_mse"]
    assert eng.fit_form("D", "graded").rss <= eng.fit_form("T", "graded").rss + 1e-9      # D nests T


def test_cited_ledger_ids_exist():
    """Every ledger id cited in this test file, in the module and in the report exists in docs/ledger.jsonl [the repo rule:
    nothing is cited from memory]."""
    ledger = Path(__file__).resolve().parents[2] / "docs" / "ledger.jsonl"
    if not ledger.exists():
        pytest.skip("docs/ledger.jsonl not present")
    ids = {json.loads(line)["id"] for line in ledger.read_text().splitlines() if line.strip()}
    here = Path(__file__).resolve().parents[1]
    cited = set()
    for p in (Path(__file__), here / "models" / "gate_reciprocity_bitcoin.py", here / "models" / "gate_reciprocity_bitcoin_report.py"):
        text = p.read_text()
        for m in re.finditer(r"\bL(\d{4})(?:-L(\d{4}))?", text):
            lo = int(m.group(1))
            hi = int(m.group(2)) if m.group(2) else lo
            cited.update(f"L{k:04d}" for k in range(lo, hi + 1))
    assert cited and cited <= ids, sorted(cited - ids)


# ================================================================== (2) the data

@pytest.fixture(scope="module")
def bt():
    """Ratings, pair structure and response-pair samples of both platforms, loaded once (checksum verified)."""
    out = {}
    for k in ("otc", "alpha"):
        R = gb.load_ratings(k)
        ps = gb.pair_structure(R)
        S, info = gb.build_sample(R, ps)
        out[k] = dict(R=R, ps=ps, S=S, info=info)
    return out


@needs_data
def test_files_match_the_recorded_checksums_and_117_counts(bt):
    """117 section 3.4 [counted; L4568, L4570-L4572]: OTC 35,592 ratings, 5,881 nodes, 32,029 positive and 3,563 negative; Alpha
    24,186, 3,783, 22,650 and 1,536; no zero rating; no ordered pair rated twice; 358 and 248 reciprocated pairs carry both
    signs; 21,492 and 14,124 undirected pairs."""
    for k, (n, nodes, pos, neg, opp, pairs) in {"otc": (35592, 5881, 32029, 3563, 358, 21492), "alpha": (24186, 3783, 22650, 1536, 248, 14124)}.items():
        R = bt[k]["R"]
        assert gb.sha256_of(gb.SOURCES[k].path) == gb.SOURCES[k].sha256
        assert R.n == n and bt[k]["info"]["n_nodes"] == nodes
        assert int((R.rating > 0).sum()) == pos and int((R.rating < 0).sum()) == neg
        ps = bt[k]["ps"]
        i = np.flatnonzero((ps.rev >= 0) & (np.arange(R.n) < ps.rev))
        assert int((R.rating[i] * R.rating[ps.rev[i]] < 0).sum()) == opp
        assert R.n - ps.n_pairs_reciprocal == pairs


@needs_data
def test_pairing_counts_and_time_resolution(bt):
    """OTC: 14,100 reciprocated pairs, none tied (sub-second times).  Alpha: 10,062 reciprocated, 7,323 on the same day
    (times are local midnights, 04:00 or 05:00 UTC), 2,739 orderable, every ordered gap at least one day.  Every pair gives
    one initiating rating, tied pairs none."""
    o, a = bt["otc"], bt["alpha"]
    assert (o["ps"].n_pairs_reciprocal, o["ps"].n_pairs_tied, o["info"]["n_response_pairs"]) == (14100, 0, 14100)
    assert (a["ps"].n_pairs_reciprocal, a["ps"].n_pairs_tied, a["info"]["n_response_pairs"]) == (10062, 7323, 2739)
    assert np.mean(o["R"].time != np.floor(o["R"].time)) > 0.99
    assert set(np.unique(a["R"].time % 86400).astype(int)) == {14400, 18000}
    assert a["S"].gap.min() >= 86400
    assert o["ps"].initiating.sum() == 21492 and a["ps"].initiating.sum() == 14124 - 7323
    g = bt["otc"]["S"].gap
    assert np.median(g) < 600 and np.mean(g <= 600) > 0.5            # most OTC responses come within ten minutes


@needs_data
def test_embeddedness_is_consistent_on_the_real_graph(bt):
    S = bt["otc"]["S"]
    assert np.all(S.emb_prior <= S.emb_static)
    assert 0.25 < np.mean(S.emb_static == 0) < 0.35 and 0.5 < np.mean(S.emb_prior == 0) < 0.65


@needs_data
def test_response_function_headline_numbers_otc(bt):
    """OTC, responder fixed effects: the shift of the response at each received rating against +1 [the first look at the
    means and the numbers of the results file]: +2 about +0.85, +3 +1.64, +4 +2.5, a negative rating about -8.4, and the
    four-number profile."""
    S = bt["otc"]["S"]
    D = gb.sample_fe(S)
    assert (D.n, len(np.unique(D.resp))) == (11795, 2020)
    cur = {r["bin"]: r for r in gb.curve_table(S)}
    assert cur[(1, 1)]["n"] == 7241
    assert cur[(2, 2)]["shift"] == pytest.approx(0.85, abs=0.03) and cur[(3, 3)]["shift"] == pytest.approx(1.64, abs=0.04)
    assert cur[(4, 4)]["shift"] == pytest.approx(2.52, abs=0.06)
    assert cur[(-1, -1)]["shift"] < -3 and cur[(-10, -10)]["shift"] < -9.5
    p = gb.profile_summary(D)
    assert p["est"]["slope14"] == pytest.approx(0.83, abs=0.03) and p["se"]["slope14"] < 0.04
    assert p["est"]["neg"] == pytest.approx(-8.36, abs=0.25) and 3.2 < p["est"]["hi58"] < 3.7


@needs_data
def test_flat_band_is_rejected_on_both_platforms_and_every_estimable_year(bt):
    """The refutation of the dead zone as a FLAT band [section 3.2 of the results]: the response at +2 differs from the response
    at +1 and flatness over +1..+4 is rejected, on OTC (p < 1e-10) and Alpha (p < 1e-8), and for each OTC year with enough rows."""
    for k, bound in (("otc", 1e-10), ("alpha", 1e-8)):
        t = gb.flatness_tests(bt[k]["S"])
        assert t[0]["p"] < (1e-10 if k == "otc" else 1e-3) and t[0]["est"][0] > 0.5
        assert t[2]["p"] < bound
    for r in gb.year_table(bt["otc"]["S"]):
        if "shift2" in r:
            assert r["shift2"] / r["se2"] > 3, r["year"]
    off = {r["x"]: r for r in gb.habit_offset_table(bt["otc"]["S"])}
    assert abs(off[1]["mean"]) < 0.2 and off[2]["mean"] > 0.5          # +1 is the zero-influence point against the responder's own habit


@needs_data
def test_negative_side_and_sign_margin(bt):
    sm = gb.sign_margin(bt["otc"]["S"])
    assert (sm["n_neg"], sm["n_pos"]) == (321, 13779)
    assert sm["p_neg_after_neg"] > 0.9 and sm["p_neg_after_pos"] < 0.03
    assert sm["p_neg_before_neg"] < 0.6                                # most negative responses did not follow a negative rating
    f = gb.flatness_tests(bt["otc"]["S"])[4]
    assert f["est"][0] < -2 and f["p"] < 1e-3                          # the mildest negative rating already moves the response


@needs_data
def test_forms_in_sample_otc(bt):
    """In-sample, responder FE: the best dead-zone fit is the one-rating band (K+ = 2, K- = 1), the literal step O-jive puts K+
    at 3, the continuous (hinge) dead-zone form takes its narrowest band, knots +1 and -1 (flat over {-1, +1}), and the
    ranking by BIC puts the graded forms first."""
    D = gb.sample_fe(bt["otc"]["S"])
    eng = gb.Engine(D.x, D.y, [gb.contiguous(D.resp)])
    fits = eng.fit_all()
    g = fits[("D", "graded")].cand
    assert (g.kp, g.kn) == (2, 1)
    s = fits[("D", "step")].cand
    assert s.kp == 3 and s.kn in (1, 2)
    h = fits[("D", "hinge")].cand
    assert (h.kp, h.kn) == (1, 1)
    bic = {k: f.ic("bic") for k, f in fits.items()}
    pre = {k: v for k, v in bic.items() if k[0] not in gb.EXPLORATORY_NAMES and k[0] != "saturated"}
    assert min(pre, key=pre.get) == ("D", "graded")
    assert bic[("T", "graded")] < bic[("linear", None)] < bic[("D", "step")] < bic[("O-", "graded")] < bic[("O+", "graded")] < bic[("null", None)]
    assert bic[("jump+clip", None)] < bic[("T", "graded")]
    # the one-rating band IS a two-slope curve with its knee at +2; with the knee where the data put it the no-band curve wins
    k2 = fits[("knee2", None)]
    assert k2.rss < fits[("D", "graded")].rss and k2.ic("bic") < fits[("D", "graded")].ic("bic") - 50 and k2.thr[0] >= 5


@needs_data
def test_the_one_rating_band_equals_a_knee_at_two_on_the_real_data(bt):
    for k in ("otc", "alpha"):
        D = gb.sample_fe(bt[k]["S"])
        eng = gb.Engine(D.x, D.y, [gb.contiguous(D.resp)])
        d = eng.fit_form("D", "graded")
        assert (d.cand.kp, d.cand.kn) == (2, 1)
        two = eng.fit_cols("two", None, ["Ph1", "Ph2", "Ns1", "Nh1"])
        assert two.rss == pytest.approx(d.rss, rel=1e-9)


@needs_data
def test_out_of_sample_the_odjive_loses_to_a_graded_form_without_band(bt):
    """Cross-validation, thresholds re-chosen in each training fold: D-step (the literal O-jive) is worse than T-graded by more
    than 4 SE on OTC; one-sided graded forms are worse than T-graded by more than 5 SE; a no-band clipped mirror is within 2 SE
    of the best dead-zone fit."""
    D = gb.sample_fe(bt["otc"]["S"])
    cv = gb.cv_losses(D.x, D.y, D.resp, K=10, repeats=2, seed=gb.SOURCES["otc"].size)
    def z(a, b):
        d, se = gb.paired_diff(cv[a], cv[b], D.resp)
        return d / se
    assert z(("D", "step"), ("T", "graded")) > 4
    assert z(("O+", "graded"), ("T", "graded")) > 5 and z(("O-", "graded"), ("T", "graded")) > 5
    assert abs(z(("D", "graded"), ("jump+clip", None))) < 2
    assert np.nanmean(cv[("jump+clip", None)]) < np.nanmean(cv[("linear", None)])


@needs_data
def test_drift_and_platform_and_reversal(bt):
    """Drift: the 1-4 slope rises over 2011-2015 on OTC (trend t > 2); platforms agree like for like (OTC gap >= 1 day against
    Alpha's ordered pairs, 1-4 slope within 2 SE); the negative jump is much smaller in the time-reversed regression."""
    O, A = bt["otc"]["S"], bt["alpha"]["S"]
    ok = (O.year >= 2011) & (O.year <= 2015)
    D = gb.sample_fe(O.subset(ok))
    est, se = gb.trend_test(D, D.year.astype(float))["slope14"]
    assert est > 0 and est / se > 2
    a = gb.profile_summary(gb.sample_fe(O.subset(O.gap >= 86400)))
    b = gb.profile_summary(gb.sample_fe(A))
    assert abs(a["est"]["slope14"] - b["est"]["slope14"]) < 2 * np.hypot(a["se"]["slope14"], b["se"]["slope14"])
    fwd = gb.profile_summary(gb.sample_fe(O))
    rev = gb.profile_summary(gb.sample_fe(O.reversed()))
    assert rev["est"]["neg"] > fwd["est"]["neg"] + 2


@needs_data
def test_signal_coding_level_beats_deviation_from_habit(bt):
    r = gb.signal_coding_cv(bt["otc"]["S"], repeats=1)
    assert r["mse"]["x bins (saturated in x)"] + 3 * r["diff"]["u bins (saturated in u)"][1] < r["mse"]["u bins (saturated in u)"]
    assert abs(r["diff"]["x bins + u bins"][0]) < 3 * max(r["diff"]["x bins + u bins"][1], 1e-3)    # the deviation adds nothing to the level


@needs_data
def test_extensive_margin_is_flat_over_one_and_two_and_collapses_after_a_negative(bt):
    rows = {r["bin"]: r for r in gb.response_rates(bt["otc"]["R"], bt["otc"]["ps"], 1.0)}
    assert abs(rows[(1, 1)]["rate"] - rows[(2, 2)]["rate"]) < 0.03 and rows[(10, 10)]["rate"] < rows[(2, 2)]["rate"] - 0.2
    assert rows[(-10, -10)]["rate"] < 0.1


@needs_data
def test_copy_excess_otc_is_large_and_does_not_depend_on_size(bt):
    rows = {r["x"]: r for r in gb.copy_excess(bt["otc"]["S"], xs=(1, 2, 3, 5), B=100, seed=5)}
    for v in (1, 2, 3, 5):
        assert 0.3 < rows[v]["pi"] < 0.6
    by_gap = {}
    S = bt["otc"]["S"]
    for lab, lo, hi in (("fast", 0, 60), ("slow", 30 * 86400, 1e12)):
        m = (S.gap >= lo) & (S.gap < hi)
        by_gap[lab] = gb.copy_excess(S.subset(m), xs=(1,), B=100, seed=5)[0]["pi"]
    assert by_gap["fast"] > 0.6 and by_gap["slow"] < 0                # copying at +1 decays with the delay


# ================================================================== (3) findings: the v0 prediction as strict xfails

@needs_data
@pytest.mark.xfail(strict=True, reason="FINDING (results/gate_reciprocity_bitcoin.md section 3.2): v0's dead zone predicts a flat response "
                   "over a band of small received ratings; the response at +2 is 0.85 points above the response at +1 (chi2 = 221).")
def test_v0_prediction_a_flat_band_of_small_received_ratings(bt):
    """v0.2 section 4.1 / L0857: zero influence for K- <= x <= K+.  Predicted: flatness over {+1, +2} is NOT rejected (p > 0.05).
    Observed: rejected at p < 1e-10 on OTC.  Recorded as a strict xfail: the failure is the finding."""
    assert gb.flatness_tests(bt["otc"]["S"])[0]["p"] > 0.05


@needs_data
@pytest.mark.xfail(strict=True, reason="FINDING (results/gate_reciprocity_bitcoin.md section 4): bounded constants beyond free thresholds "
                   "(the O-jive as written) lose out of sample to a graded two-sided form with no band by 6.5 SE on OTC.")
def test_v0_prediction_the_step_odjive_beats_a_graded_form_without_a_band(bt):
    """L0857: the O-jive is zero inside a band and a bounded constant beyond each threshold.  Predicted: the step form with free
    thresholds is at least as good out of sample as the graded two-sided form with the band closed (difference within 1 SE or
    in its favour).  Observed: it is worse by about 6 SE.  Strict xfail."""
    D = gb.sample_fe(bt["otc"]["S"])
    cv = gb.cv_losses(D.x, D.y, D.resp, K=10, repeats=2, seed=11)
    d, se = gb.paired_diff(cv[("D", "step")], cv[("T", "graded")], D.resp)
    assert d <= se


# ================================================================== end to end (slow, opt-in)

@needs_data
@pytest.mark.skipif(os.environ.get("GATE_RECIPROCITY_E2E") != "1", reason="slow end-to-end run: set GATE_RECIPROCITY_E2E=1")
def test_report_end_to_end_small_bootstrap(tmp_path):
    """analyse -> guards -> render with a small bootstrap: the guards hold and the rendered file carries the verdict."""
    from models import gate_reciprocity_bitcoin_report as rp
    res = rp.analyse(B=30, cv_repeats=1, log=lambda *_: None)
    ok = rp.guards(res)
    assert len(ok) > 30
    text = rp.render(res)
    for needle in ("## Verdict", "Dead zone in the response: refuted", "## 5. Variations", "## Reproduction", "Thresholds."):
        assert needle in text
    # a flipped fact must stop the report
    res["otc"]["cv_pairs"]["D-step vs T-graded"] = (-1.0, 0.1)
    with pytest.raises(AssertionError, match="VERDICT GUARD FAILED"):
        rp.guards(res)
