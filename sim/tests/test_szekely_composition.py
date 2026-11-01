"""Szekely 2021 composition test: the rule, the split by round, no test-round leakage, the criteria and their edges.

Prior work: results/synthetic_population_identifiability.md "Decision" (why composition is under test),
docs/prior-work/118-measured-drive-datasets.md (the dataset).  Results: sim/results/szekely_composition.md.

Two groups.  (1) Machinery on synthetic arrays, no data needed: the split by round, the cut choice, the rates, the freeze,
the report's refusal without the rule, the criterion edges.  (2) Data tests, skipped with a reason when the git-ignored
file is absent: the facts in the results file are recomputed from the file, and the file's decisions follow the criteria
applied to its own numbers.  A failure of a data test is a finding, not something to tune away.
"""
from __future__ import annotations

import re

import numpy as np
import pytest

from models import szekely_composition as S

needs_data = pytest.mark.skipif(
    not S.DATA.exists(),
    reason="sim/data/szekely2021/full.csv is absent (local-use-only, git-ignored): download https://osf.io/download/ra9ex/ "
    "(sha256 in sim/data/README.md)",
)


# ------------------------------------------------------------------ (1) machinery

def test_split_is_by_round_within_each_phase():
    r = np.arange(1, 29)
    tr, te = S.split_rounds(r)
    assert not (tr & te).any() and (tr | te).all()
    assert list(r[tr]) == list(range(1, 11)) + list(range(15, 25))
    assert list(r[te]) == [11, 12, 13, 14, 25, 26, 27, 28]
    assert list(S.phase_of(r)[:15]) == [1] * 14 + [2]
    t0, t1 = S.split_rounds(np.array([0, 29, -3]))
    assert not t0.any() and not t1.any()


def test_rule_text_carries_the_preregistered_numbers():
    r = S.RULE_TEXT
    for needle in ("total contribution >= 300", "penalty 1", "{15°, 20°, 22.45°, 25°, 30°, 35°}", "at most two cuts", "2,000 draws",
                   "seed 20261101", "more than 0.02", "exceeds 0.55", "No re-tuning after scoring.", "rounds 1-10 and 15-24", "rounds 11-14 and 25-28"):
        assert needle in r, needle
    assert "[" not in r.replace("[...]", "")  # the bracketed parameter was filled
    assert (S.CUT_GRID, S.BOOT, S.SEED, S.AUC_MARGIN, S.K1_AUC_FLOOR, S.SWITCH, S.TRAIN_LEN) == (
        (15.0, 20.0, 22.45, 25.0, 30.0, 35.0), 2000, 20261101, 0.02, 0.55, 15, 10)


def test_criterion_edges_are_strict():
    # K2 / K3 form: both conditions, AUC strictly more than 0.02
    assert S.beats(0.70, 0.67, 0.50, 0.52)
    assert not S.beats(0.70, 0.68, 0.50, 0.52)          # exactly the margin is not more
    assert not S.beats(0.70, 0.60, 0.52, 0.52)          # equal log-loss is not lower
    assert not S.beats(0.70, 0.60, 0.53, 0.52)
    assert not S.beats(0.619, 0.60, 0.50, 0.52)         # 0.019
    assert S.beats(0.6201, 0.60, 0.50, 0.52)
    # float noise at the margin cannot count as more
    assert not S.beats(0.60 + 0.02, 0.60, 0.4, 0.5)
    # K1: AUC strictly above 0.55 and log-loss below the baseline's
    assert S.k1_met(0.56, 0.60, 0.65)
    assert not S.k1_met(0.55, 0.60, 0.65)
    assert not S.k1_met(0.56, 0.65, 0.65)
    assert not S.k1_met(0.70, 0.66, 0.65)


def test_cut_choice_uses_training_rows_only_and_finds_a_planted_cut():
    """Outcome depends on the number of members above 25: the choice lands on 25 and does not move when test data change."""
    rng = np.random.default_rng(3)
    V = rng.uniform(0, 45, size=(400, 6))
    n_above = (V > 25).sum(1)
    y = (rng.random(400) < 1 / (1 + np.exp(-(1.5 * (n_above - 2.2))))).astype(float)
    cuts, l1, lf = S.choose_cuts(V, y, S.CUT_GRID)
    assert 25.0 in cuts and lf <= l1 + 1e-12
    # same call, shuffled order of the grid: same answer; and a copy of the arrays: same answer
    assert S.choose_cuts(V.copy(), y.copy(), S.CUT_GRID[::-1])[0] == cuts
    # at most two cuts
    assert len(cuts) <= 2
    # a second cut is only kept if the in-training log-loss is lower
    if len(cuts) == 1:
        assert lf == l1
    else:
        assert lf < l1


def _panel_stub(n_p=40, seed=0):
    """A small stand-in with the Panel's attributes, so that fit_phase can run without the file."""
    rng = np.random.default_rng(seed)
    P = S.Panel.__new__(S.Panel)
    P.n_persons = n_p
    P.svo_angle = rng.uniform(0, 45, n_p)
    P.risk = rng.integers(0, 11, n_p).astype(float)
    P.agreeableness = rng.integers(10, 50, n_p).astype(float)
    P.contrib = rng.integers(0, 101, size=(n_p, 28)).astype(float)
    P.prev = np.full((n_p, 28), np.nan)
    P.prev[:, 1:] = P.contrib[:, :-1]
    rnd, mem, y = [], [], []
    for r in range(1, 29):
        for g in range(6):
            m = rng.choice(n_p, 6, replace=False)
            rnd.append(r)
            mem.append(m)
            y.append(P.contrib[m, r - 1].sum() + 40 * (P.svo_angle[m] > 25).sum())
    P.rnd, P.mem, P.y_cont = np.array(rnd), np.array(mem), np.array(y)
    P.y_bin = (P.y_cont >= S.THRESHOLD).astype(float)
    P.high_first = np.arange(len(rnd)) % 2 == 0
    return P


def test_rates_use_training_rounds_of_the_phase_only():
    P = _panel_stub()
    st = S.person_training_stats(P, 1)
    expect = np.nanmean(P.contrib[:, 0:10], axis=1)
    assert np.allclose(st["rate"], expect)
    # change every test-round contribution (rounds 11-14 and 25-28): phase 1 and phase 2 rates do not move
    P2 = _panel_stub()
    P2.contrib[:, 10:14] += 999.0
    P2.contrib[:, 24:28] -= 999.0
    for ph in (1, 2):
        assert np.allclose(S.person_training_stats(P, ph)["rate"], S.person_training_stats(P2, ph)["rate"])
    # phase 2 uses rounds 15-24
    assert np.allclose(S.person_training_stats(P, 2)["rate"], np.nanmean(P.contrib[:, 14:24], axis=1))


def test_member_without_training_rounds_gets_the_grand_mean():
    P = _panel_stub()
    P.contrib[3, 0:10] = np.nan
    st = S.person_training_stats(P, 1)
    assert st["rate"][3] == pytest.approx(np.nanmean(P.contrib[:, 0:10]))
    assert st["persons_without_rate"] == 1


def test_no_test_round_leakage_into_fit_or_cuts():
    """Scramble every test group-round's outcome and contribution: coefficients, cuts and training numbers are unchanged;
    only the test-side numbers move."""
    P = _panel_stub(seed=5)
    a = S.fit_phase(P, 1, "svo_angle")
    _, te = S.split_rounds(P.rnd)
    Q = _panel_stub(seed=5)
    rng = np.random.default_rng(9)
    Q.y_cont = np.where(te, rng.permutation(Q.y_cont), Q.y_cont)
    Q.y_bin = (Q.y_cont >= S.THRESHOLD).astype(float)
    Q.contrib[:, 10:14] = rng.integers(0, 101, size=(Q.n_persons, 4)).astype(float)
    Q.contrib[:, 24:28] = rng.integers(0, 101, size=(Q.n_persons, 4)).astype(float)
    b = S.fit_phase(Q, 1, "svo_angle")
    assert a["cuts"] == b["cuts"] and a["ll_final_cuts"] == b["ll_final_cuts"]
    for k in a["models"]:
        assert np.allclose(a["models"][k]["beta_std"], b["models"][k]["beta_std"]), k
    assert a["base_rate_train"] == b["base_rate_train"]
    assert not np.array_equal(a["y_te_bin"], b["y_te_bin"]) or not np.array_equal(a["y_te_cont"], b["y_te_cont"])
    # drive-only models do not depend on the contributions at all, so their test predictions are identical
    for k in ("M", "Mo", "T"):
        assert np.allclose(a["scores"][k], b["scores"][k])


def test_phase_one_fit_ignores_phase_two_rows():
    P = _panel_stub(seed=7)
    a = S.fit_phase(P, 1, "svo_angle")
    Q = _panel_stub(seed=7)
    ph2 = S.phase_of(Q.rnd) == 2
    Q.y_cont = np.where(ph2, 0.0, Q.y_cont)
    Q.y_bin = (Q.y_cont >= S.THRESHOLD).astype(float)
    Q.contrib[:, 14:] = 0.0
    b = S.fit_phase(Q, 1, "svo_angle")
    for k in a["models"]:
        assert np.allclose(a["models"][k]["beta_std"], b["models"][k]["beta_std"]), k
    assert np.allclose(a["scores"]["R+T"], b["scores"]["R+T"])


def test_dynamic_state_fills_missing_lag_with_the_training_mean():
    P = _panel_stub(seed=2)
    P.prev[:, :] = np.nan                      # every lag missing
    out = S.fit_phase(P, 1, "svo_angle")
    # all D inputs equal the fill value, so D carries no information: constant prediction, AUC exactly 0.5
    assert np.ptp(out["scores"]["D"]) < 1e-9


def test_linear_ridge_matches_closed_form_and_freezes():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(80, 3))
    y = X @ np.array([1.0, -2.0, 0.5]) + 3 + rng.normal(0, 0.1, 80)
    lf = S.LinFrozen.fit(X, y)
    Z = (X - X.mean(0)) / X.std(0)
    b = np.linalg.solve(Z.T @ Z + np.eye(3), Z.T @ (y - y.mean()))
    assert np.allclose(lf.beta, b) and lf.ybar == pytest.approx(y.mean())
    X2 = rng.normal(size=(10, 3))
    assert np.allclose(lf.predict(X2), y.mean() + ((X2 - X.mean(0)) / X.std(0)) @ b)


def test_report_refuses_without_the_rule(tmp_path, monkeypatch):
    monkeypatch.setattr(S, "RESULTS", tmp_path / "szekely_composition.md")
    with pytest.raises(SystemExit) as e:
        S.main(["report"])
    assert "rule" in str(e.value)
    (tmp_path / "szekely_composition.md").write_text("# something else\n")
    with pytest.raises(SystemExit):
        S.main(["report"])


def test_rule_stub_writes_facts_and_rule_and_no_number_of_a_fit(tmp_path, monkeypatch):
    p = tmp_path / "r.md"
    S.write_rule_stub(p)
    t = p.read_text()
    assert S.RULE_TEXT in t and S.FACTS_TEXT in t
    assert t.index("Facts about the data") < t.index("The rule, written before any fit")
    assert "auc" not in t.split("## The rule")[0].lower()


def test_bootstrap_uses_the_same_draws_for_every_model():
    rng = np.random.default_rng(0)
    y = (rng.random(120) < 0.5).astype(float)
    s = rng.random(120)
    R = S.score_stratum(y, y * 10, {"0": np.full(120, 0.5), "M": s, "R": s.copy()}, {"0": np.full(120, 5.0), "M": y * 10, "R": y * 10}, draws=200)
    c = S.contrast(R, "M", "R")
    assert c["auc_ci"] == (0.0, 0.0) and c["ll_ci"] == (0.0, 0.0)
    assert R["test"]["M"]["rmse_ratio"] == pytest.approx(0.0)


def test_result_text_has_no_participant_row():
    t = S.facts_block() + S.rule_block() + " ".join(S.IMPLEMENTATION)
    assert not re.search(r"\b\d{5}\b,\s*\d{1,2}\b", t)        # no 'group_id, round' pair
    assert "@" not in t


# ------------------------------------------------------------------ (2) data

@pytest.fixture(scope="module")
def panel():
    return S.Panel()


@needs_data
def test_file_checksum_and_shape():
    assert S.sha256_of() == S.DATA_SHA256
    n_raw, rows = S.read_game_rows()
    assert n_raw == 14872 and len(rows) == 8008
    assert len({(r["id"], r["round"]) for r in rows}) == 8008 and len({r["id"] for r in rows}) == 286


@needs_data
def test_facts_in_the_results_file_are_recomputed_from_the_data(panel):
    n_raw, rows = S.read_game_rows()
    import collections
    # conditional rounds
    import csv
    with open(S.DATA, encoding="utf-8", errors="replace", newline="") as f:
        raw = list(csv.DictReader(f))
    cond = sorted({int(r["round"]) for r in raw if r["manipulation"] == "High EE and Low NE"})
    assert cond == [1, 5, 10, 14, 15, 19, 24, 28]
    assert sum(r["odr"] == "0" for r in raw) == 6864
    # switch at round 15 in both orders; constant within a person-phase
    dp = collections.defaultdict(set)
    for r in rows:
        dp[(r["treatment"], int(r["round"]) >= S.SWITCH)].add(r["disaster_probability"])
    assert all(len(v) == 1 for v in dp.values()) and len(dp) == 4
    # group ids: one round each, 1,392 group-rounds, 1,261 with six rows
    g = collections.defaultdict(list)
    for r in rows:
        g[r["group_id"]].append(r)
    assert len(g) == 1392 and len({r["round"] for v in g.values() for r in v[:1]}) >= 1
    assert all(len({r["round"] for r in v}) == 1 for v in g.values())
    assert sum(len(v) == 6 for v in g.values()) == 1261
    # threshold: totals at or above 300 never meet a disaster; 800 such group-rounds; 57.5%
    tot = {k: (float(v[0]["total_contribution"]), v[0]["disaster_outcome"], v[0]["disaster_probability"]) for k, v in g.items()}
    hi = [t for t in tot.values() if t[0] >= 300]
    assert len(hi) == 800 and all(t[1] == "0" for t in hi)
    assert round(len(hi) / 1392, 3) == 0.575
    # timeouts: contribution missing exactly where a timeout occurred; excluded persons absorbing, first at inactive 4
    assert sum(r["contribution"] == "" for r in rows) == 567 == sum(r["timeout_contribute"] == "Timeout occurred" for r in rows)
    ex = [r for r in rows if r["excluded"] == "Excluded"]
    assert len(ex) == 371 and len({r["id"] for r in ex}) == 23 and min(int(r["inactive"]) for r in ex) == 4
    # persons: constants, no missing
    for col in ("svo_angle", "risk", "agreeableness"):  # raw strings: constant per person, none blank
        d = collections.defaultdict(set)
        for r in rows:
            d[r["id"]].add(r[col])
        assert len(d) == 286 and all(len(v) == 1 and "" not in v for v in d.values())
    assert collections.Counter(r["risk"] for r in {r["id"]: r for r in rows}.values()) == collections.Counter({"2": 85, "1": 57, "Risk averse": 44, "3": 41, "4": 40, "Risk seeking": 19})
    assert set(np.unique(panel.risk)) == {0.0, 1.0, 2.0, 3.0, 4.0, 5.0} and not np.isnan(panel.agreeableness).any()
    a = panel.svo_angle
    assert a.min() == pytest.approx(-11.7, abs=0.03) and a.max() == pytest.approx(61.2, abs=0.03) and np.median(a) == pytest.approx(30.2, abs=0.05)
    for c, share in zip(S.CUT_GRID, (0.797, 0.734, 0.699, 0.650, 0.507, 0.364)):
        assert round(float((a > c).mean()), 3) == share, c
    # lag matches
    ok = tot2 = 0
    for p in range(panel.n_persons):
        for rd in range(1, 28):
            x, y = panel.prev[p, rd], panel.contrib[p, rd - 1]
            if not np.isnan(x) and not np.isnan(y):
                tot2 += 1
                ok += abs(x - y) < 1e-6
    assert (ok, tot2) == (7179, 7179)


@needs_data
def test_panel_population_and_sets(panel):
    assert len(panel.rnd) == 1228 and panel.dropped == {"fewer than 6 rows": 131, "6 rows, a member excluded": 33, "no recorded total": 0}
    assert panel.mem.shape == (1228, 6)
    assert all(len(set(m)) == 6 for m in panel.mem)
    tr, te = S.split_rounds(panel.rnd)
    ph = S.phase_of(panel.rnd)
    for p in (1, 2):
        assert (tr & (ph == p)).sum() > 0 and (te & (ph == p)).sum() > 0
    # y_bin follows the 300 threshold of the recorded total
    assert np.array_equal(panel.y_bin, (panel.y_cont >= 300).astype(float))
    # no group-round is both train and test; every analysed group-round is in exactly one
    assert ((tr ^ te) | ~(tr | te)).all() and (tr | te).all()


@needs_data
def test_results_file_opens_with_facts_then_rule_and_its_decisions_follow_the_criteria():
    if not S.RESULTS.exists():
        pytest.skip("results file not yet generated")
    t = S.RESULTS.read_text()
    assert S.RULE_TEXT in t and S.FACTS_TEXT in t
    assert t.index("Facts about the data") < t.index("The rule, written before any fit")
    if "## Decision, exactly per the criteria" not in t:
        pytest.skip("stub only")
    assert "NOT MET" in t or "MET" in t


@needs_data
def test_decision_row_in_the_results_file_follows_from_recomputation(panel):
    """Recompute the primary run (few bootstrap draws: the verdicts do not depend on them) and find its decision row in the file."""
    if not S.RESULTS.exists() or "## Decision, exactly per the criteria" not in S.RESULTS.read_text():
        pytest.skip("results file not yet generated")
    res = S.run_drive(panel, "svo_angle", draws=20, with_D=True)
    assert S._decision_line("primary: svo_angle", res) in S.RESULTS.read_text()
    # and each verdict is the criterion applied to the same stratum's own numbers
    for s in S.STRATA:
        t = res["strata"][s]["test"]
        v = res["strata"][s]["verdict"]
        assert v["K2"] == (round(t["T"]["auc"] - t["M"]["auc"], 12) > 0.02 and t["T"]["ll"] < t["M"]["ll"])
        assert v["K3"] == (round(t["R+T"]["auc"] - t["R"]["auc"], 12) > 0.02 and t["R+T"]["ll"] < t["R"]["ll"])
        assert v["K1"] == (t["M"]["ll"] < t["0"]["ll"] and t["M"]["auc"] > 0.55)
