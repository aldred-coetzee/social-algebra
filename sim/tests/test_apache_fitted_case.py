"""Apache Incubator fitted case: the rule, the split, the freeze, the criterion and the bootstrap.

Prior work: models/00-v0.md section 1.1 (team activity, prospective first-year growth g) and section 8 "Team" (the rule
written first); results/apache_activity_survival.md (the in-sample work and its Review; ledger L4623-L4633).  Results:
sim/results/apache_fitted_case.md, written by models/apache_fitted_case.py.

Two groups.  (1) Machinery, no data needed: the split by start year, the frozen model (fitted on training rows only, so a
change in the test rows or labels cannot move it), the decision criterion (including that equality with the margin is NOT
a pass), the bootstrap against known answers, and that the features of a podling come from its first W months only.
(2) Data tests, skipped with a reason when the git-ignored files are absent: the sets are disjoint and cover the labels,
the rule is verbatim at the top of the results file, the file's decision agrees with the criterion applied to its own
numbers, and nothing personal is in it.  A failure of a data test is a finding, not something to tune away.
"""
from __future__ import annotations

import re

import numpy as np
import pytest

from models import apache_activity_survival as A
from models import apache_fitted_case as F

needs_data = pytest.mark.skipif(
    not ((A.DERIVED / "meta.json").exists() and (A.DATA_DIR / A.PODLINGS_FILE).exists()),
    reason="sim/data/apache-incubator/derived is absent (local-use-only, git-ignored): cd sim && "
    "~/.local/bin/uv run python -m models.apache_activity_survival fetch && "
    "~/.local/bin/uv run python -m models.apache_activity_survival build",
)


# ------------------------------------------------------------------ (1) machinery

def test_split_is_disjoint_and_by_calendar_year_of_start():
    years = np.arange(2000, 2025)
    tr, te = F.split_masks(years)
    assert not (tr & te).any()
    assert years[tr].min() == 2003 and years[tr].max() == 2012
    assert years[te].min() == 2013 and years[te].max() == 2021
    assert not (tr | te)[years < 2003].any() and not (tr | te)[years > 2021].any()


def test_rule_text_carries_the_preregistered_numbers():
    """The rule is the brief's: train 2003-2012, test 2013-2021, margin 0.02, 2,000 draws, W = 12 and 6."""
    r = F.RULE_TEXT
    for needle in ("2003-01-01 to 2012-12-31", "2013-01-01 to 2021-12-31", "more than 0.02", "2,000 draws", "6-month feature window",
                   "Fit all on training only; freeze.", "B's log-loss is lower than A's"):
        assert needle in r, needle
    assert (F.TRAIN_YEARS, F.TEST_YEARS, F.AUC_MARGIN, F.BOOT) == ((2003, 2012), (2013, 2021), 0.02, 2000)


def test_frozen_model_depends_on_training_rows_only():
    """Fitting uses the training rows; the stored constants then give the same test predictions whatever the test labels are."""
    rng = np.random.default_rng(0)
    Xtr = rng.normal(size=(120, 2))
    ytr = (Xtr[:, 0] + 0.3 * rng.normal(size=120) > 0).astype(float)
    fz = F.Frozen.fit(Xtr, ytr, ("a", "b"))
    Xte = rng.normal(size=(40, 2))
    p1 = fz.predict(Xte)
    # a second fit on the identical training rows is identical, and nothing about the test rows enters
    fz2 = F.Frozen.fit(Xtr.copy(), ytr.copy(), ("a", "b"))
    assert np.allclose(fz.beta, fz2.beta) and np.allclose(p1, fz2.predict(Xte))
    # the raw-scale form is the same model
    b0, sl = fz.raw()
    z = b0 + Xte @ sl
    assert np.allclose(1 / (1 + np.exp(-z)), p1)


def test_run_case_ignores_test_labels_when_fitting():
    """Changing every test label changes the scores' AUC but not a single coefficient or prediction."""
    rng = np.random.default_rng(1)
    n = 200
    year = np.r_[np.full(100, 2008.0), np.full(100, 2016.0)]
    ln_n = rng.normal(3, 0.8, n)
    y = (rng.random(n) < 1 / (1 + np.exp(-(1.2 * (ln_n - 3) + 1)))).astype(float)
    tab = {"n": np.exp(ln_n) + 5, "ln_n": ln_n, "growth": rng.normal(0, 1, n), "cal_year": year, "y": y}
    R1 = F.run_case(tab, F.MODELS, draws=50)
    tab2 = dict(tab)
    y2 = y.copy()
    y2[100:] = 1 - y2[100:]
    tab2["y"] = y2
    R2 = F.run_case(tab2, F.MODELS, draws=50)
    for k in ("A", "B", "C"):
        assert np.allclose(R1["models"][k]["beta_std"], R2["models"][k]["beta_std"])
        assert np.allclose(R1["scores"][k], R2["scores"][k])
    assert R1["test"]["A"]["auc"] != R2["test"]["A"]["auc"]
    assert R1["n_train"] == R2["n_train"] == 100 and R1["n_test"] == 100


def test_baseline_is_the_training_base_rate_and_auc_half():
    rng = np.random.default_rng(2)
    n = 160
    year = np.r_[np.full(80, 2005.0), np.full(80, 2015.0)]
    ln_n = rng.normal(3, 0.8, n)
    y = (rng.random(n) < 0.7).astype(float)
    tab = {"n": np.full(n, 10.0), "ln_n": ln_n, "growth": rng.normal(size=n), "cal_year": year, "y": y}
    R = F.run_case(tab, F.MODELS, draws=20)
    assert np.allclose(R["scores"]["0"], y[:80].mean())
    assert R["test"]["0"]["auc"] == 0.5
    p = y[:80].mean()
    yt = y[80:]
    expect = -(yt * np.log(p) + (1 - yt) * np.log(1 - p)).mean()
    assert R["test"]["0"]["ll"] == pytest.approx(expect)


def test_criterion_needs_both_conditions_and_strictly_more_than_the_margin():
    assert F.criterion(0.70, 0.73, 0.50, 0.49)
    assert not F.criterion(0.70, 0.73, 0.50, 0.50)  # log-loss equal is not lower
    assert not F.criterion(0.70, 0.73, 0.50, 0.51)
    assert not F.criterion(0.70, 0.72, 0.50, 0.40)  # exactly the margin is not more than the margin
    assert not F.criterion(0.70, 0.715, 0.50, 0.40)


def test_bootstrap_identical_scores_give_zero_difference_and_known_auc():
    rng = np.random.default_rng(3)
    y = (rng.random(80) < 0.5).astype(int)
    s = rng.random(80)
    B = F.bootstrap(y, {"A": s, "B": s}, draws=200, seed=5)
    assert np.allclose(B["auc"]["A"], B["auc"]["B"]) and np.allclose(B["ll"]["A"], B["ll"]["B"])
    perfect = F.bootstrap(y, {"P": y * 0.9 + 0.05}, draws=100, seed=5)
    assert np.allclose(perfect["auc"]["P"], 1.0)
    assert len(B["auc"]["A"]) + B["skipped"] == 200


def test_bootstrap_interval_contains_zero_for_a_useless_extra_score():
    """A noise score added to nothing: B - A is centred near 0 and its interval holds 0."""
    rng = np.random.default_rng(4)
    y = (rng.random(150) < 0.7).astype(int)
    a = 0.3 + 0.4 * y + 0.3 * rng.normal(size=150)
    b = a + 0.01 * rng.normal(size=150)
    B = F.bootstrap(y, {"A": a, "B": b}, draws=500, seed=7)
    lo, hi = F.interval(B["auc"]["B"] - B["auc"]["A"])
    assert lo <= 0 <= hi


def _synthetic_panel(spike_after: float):
    """Two podlings, 30 months, 6 persons; a burst of activity from month 12 on that is varied between calls."""
    months = 30
    mats = {k: [] for k in ("commits", "files", "loc", "msg_human", "msg_dev", "msg_all", "reply_human")}
    rng = np.random.default_rng(11)
    for _ in range(2):
        base = (rng.random((6, months)) < 0.5).astype(float)
        late = base.copy()
        late[:, 12:] = late[:, 12:] * 0 + spike_after
        for k in mats:
            mats[k].append(late.copy() if k in ("commits", "files", "loc") else np.zeros((6, months)))
    return A.Panel.synthetic(mats, labels=[1, 0], exit_m=[20, 25])


def test_features_use_the_first_W_months_only():
    """Changing everything after month W leaves n, g and the shape features of the landmark table unchanged."""
    t1 = A.landmark_table(_synthetic_panel(0.0), W=12)
    t2 = A.landmark_table(_synthetic_panel(9.0), W=12)
    for k in ("n", "growth", "gini", "top3", "T"):
        assert np.allclose(t1[k], t2[k], equal_nan=True), k


def test_growth_matches_the_definition_in_1_1():
    """g = ln((events in months 6-11 + 1)/(events in months 0-5 + 1))."""
    months = 20
    c = np.zeros((4, months))
    c[:, :6] = 1.0   # 24 events in months 0-5
    c[:, 6:12] = 2.0  # 48 events in months 6-11
    mats = {k: [c.copy() if k == "commits" else np.zeros((4, months))] for k in ("commits", "files", "loc", "msg_human", "msg_dev", "msg_all", "reply_human")}
    pan = A.Panel.synthetic(mats, labels=[1], exit_m=[15])
    t = A.landmark_table(pan, W=12)
    assert t["growth"][0] == pytest.approx(np.log(49 / 25))


def test_result_text_has_no_address():
    if F.RESULTS.exists():
        assert "@" not in F.RESULTS.read_text()


# ------------------------------------------------------------------ (2) data tests

@pytest.fixture(scope="module")
def panel():
    return A.Panel()


@pytest.fixture(scope="module")
def table(panel):
    return F.make_table(panel, 12, conversation=True)


@needs_data
def test_sets_are_disjoint_and_every_row_is_in_one_by_start_year(panel, table):
    tr, te = F.split_masks(table["cal_year"])
    assert not (tr & te).any()
    assert (tr | te).all()  # no resolved podling started outside 2003-2021
    # calendar years come from the ASF start dates
    assert table["cal_year"].min() >= 2003 and table["cal_year"].max() <= 2021
    assert len(set(table["p"][tr].astype(int)) & set(table["p"][te].astype(int))) == 0


@needs_data
def test_counts_reproduce_the_in_sample_totals(panel, table):
    """The 207 podlings at risk at month 12 (155 / 52) are the union of the two sets before the n >= 3 condition."""
    c = F.counts_for(panel, 12)
    g = c["train"]["incubating_at_W"][0] + c["test"]["incubating_at_W"][0]
    r = c["train"]["incubating_at_W"][1] + c["test"]["incubating_at_W"][1]
    assert (g, r) == (155, 52)
    assert c["outside"] == 0
    assert len(table["p"]) == 207


@needs_data
def test_results_file_opens_with_the_rule_verbatim_and_its_decision_follows_the_criterion():
    txt = F.RESULTS.read_text()
    assert F.RULE_TEXT in txt
    assert txt.index(F.RULE_TEXT) < txt.index("## Counts") < txt.index("## Held-out result")
    m = re.search(r"\*\*Decision: the criterion is (MET|NOT MET)\.\*\* B's held-out AUC ([0-9.]+) against A's ([0-9.]+).*?log-loss ([0-9.]+) against A's ([0-9.]+)", txt)
    assert m
    met = F.criterion(float(m[3]), float(m[2]), float(m[5]), float(m[4]), margin=F.AUC_MARGIN - 1e-9)
    # printed to three decimals, so allow the knife-edge to be re-read from the file's own difference
    d = re.search(r"AUC, B - A \| ([+-][0-9.]+)", txt)
    assert (m[1] == "MET") == (met and float(d[1]) > F.AUC_MARGIN)


@needs_data
def test_recomputing_the_primary_reproduces_the_file(panel, table):
    """The numbers in the file are the numbers the code gives, with the frozen protocol and fixed seed."""
    R = F.run_case(table, F.MODELS)
    txt = F.RESULTS.read_text()
    for k in ("A", "B", "C"):
        assert f"{R['test'][k]['auc']:.3f}" in txt
    assert f"{R['diff']['auc']:+.3f}" in txt
    assert R["diff"]["met"] == (R["diff"]["auc"] > F.AUC_MARGIN and R["test"]["B"]["ll"] < R["test"]["A"]["ll"])
