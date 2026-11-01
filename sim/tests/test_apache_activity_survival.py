"""Apache Incubator: team-scale activity and survival, and the checks that the machinery behind it is right.

Prior work: docs/prior-work/117-modern-signed-and-split-datasets.md section 4.3 (the dataset and its counts,
L4623-L4633, L4666); models/02-our-claims.md Claim 1 (a group's state is a distribution, not a mean; the
reason for asking whether the shape of the activity distribution carries what the mean does not: L1225
Granovetter's two crowds with one mean and opposite outcomes, L1831 the threshold map); models/00-v0.md
section 7 "Team" (the coupling term goes if it adds no gain over individual dynamics for who leaves; L5742
state-dependent inertia, L4367 the partner term near zero beside it); size: L5779 and L5740; early warning:
L0512 and L0527 (rising lag-1 autocorrelation and variance before a transition), L0547 and L3057 (their low
specificity).  Results and verdict: sim/results/apache_activity_survival.md, written by
models/apache_activity_survival.py from the same functions.

Two groups.  (1) Machinery, no data needed: the shape measures against hand values, the cross-validation and
the permutation test against known signals and known nulls, the early-warning statistics against processes
whose answer is known (including the finding that they have no power on short series), the robot and list
rules, the pseudonymisation, and the table builders on synthetic panels.  (2) Data tests, skipped with a reason
when the git-ignored files are absent (cd sim && ~/.local/bin/uv run python -m models.apache_activity_survival
fetch, then build; sim/data/README.md): the build reproduces 117's counts, nothing personal is in what the build
leaves, the labels agree with the papers' counts, and the recorded findings of the results file are reproduced
by the same code.  A failure of a data test is a finding, not something to tune away.
"""
from __future__ import annotations

import itertools
import json
import re

import numpy as np
import pytest
from scipy.optimize import minimize
from scipy.stats import kendalltau

from models import apache_activity_survival as A

needs_data = pytest.mark.skipif(
    not ((A.DERIVED / "meta.json").exists() and (A.DATA_DIR / A.PODLINGS_FILE).exists()),
    reason="sim/data/apache-incubator/derived is absent (local-use-only, git-ignored): cd sim && "
    "~/.local/bin/uv run python -m models.apache_activity_survival fetch && "
    "~/.local/bin/uv run python -m models.apache_activity_survival build",
)


# ------------------------------------------------------------------ (1) machinery: shape measures

def test_gini_known_values():
    """Hand values: [1..5] has Gini 4/15; equal shares 0; one member holding everything (n-1)/n, 1 once rescaled."""
    assert A.gini([1, 2, 3, 4, 5]) == pytest.approx(4 / 15)
    assert A.gini([3, 3, 3, 3]) == pytest.approx(0.0)
    assert A.gini([0, 0, 0, 10]) == pytest.approx(0.75)
    assert A.gini_corrected([0, 0, 0, 10]) == pytest.approx(1.0)
    assert np.isnan(A.gini_corrected([5]))


def test_shape_measures_ignore_scale_and_order():
    """Claim 1's point is about shape: the measures must not move with the unit or the labelling of members."""
    rng = np.random.default_rng(3)
    a = rng.pareto(1.5, 30) + 1
    f0 = A.shape_features(a)
    for b in (a * 7.5, rng.permutation(a)):
        f1 = A.shape_features(b)
        for k in ("gini", "top1", "top3", "entropy", "effn", "theil", "cv"):
            assert f1[k] == pytest.approx(f0[k]), k


def test_top_share_entropy_and_effective_number():
    assert A.top_share([1, 2, 3, 4, 10], 1) == pytest.approx(0.5)
    assert A.top_share([1, 2, 3, 4, 10], 3) == pytest.approx(0.85)
    assert A.norm_entropy([5, 5, 5, 5]) == pytest.approx(1.0)
    assert A.eff_number([5, 5, 5, 5]) == pytest.approx(4.0)
    assert A.eff_number([1000, 1, 1, 1]) < 1.1
    assert A.norm_entropy([1000, 1, 1, 1]) < 0.1


def test_exchangeable_members_are_far_less_concentrated_than_a_heavy_tail():
    """The 'interchangeable members' null: chance alone spreads events almost evenly once there are enough of them."""
    rng = np.random.default_rng(1)
    g_many, _ = A.exchangeable_gini(10, 1000, rng)
    g_few, _ = A.exchangeable_gini(10, 20, rng)
    assert g_many < 0.1 < g_few
    heavy = np.array([200, 100, 50, 25, 12, 6, 3, 2, 1, 1.0])
    assert A.gini_corrected(heavy) > 5 * g_many


# ------------------------------------------------------------------ (1) machinery: scoring and tests

def test_auc_matches_brute_force_with_ties():
    rng = np.random.default_rng(2)
    y = rng.integers(0, 2, 40)
    s = rng.integers(0, 6, 40).astype(float)  # many ties
    pos, neg = s[y == 1], s[y == 0]
    brute = np.mean([(p > q) + 0.5 * (p == q) for p, q in itertools.product(pos, neg)])
    assert A.auc_score(y, s) == pytest.approx(brute)


def test_logit_fit_matches_a_generic_optimiser():
    rng = np.random.default_rng(4)
    X = rng.normal(size=(300, 3))
    y = (rng.random(300) < 1 / (1 + np.exp(-(0.5 + X @ np.array([1.0, -0.7, 0.0]))))).astype(float)
    b = A.logit_fit(X, y, l2=0.0)

    def nll(beta):
        eta = beta[0] + X @ beta[1:]
        return np.sum(np.log1p(np.exp(eta)) - y * eta)

    ref = minimize(nll, np.zeros(4), method="BFGS").x
    assert b == pytest.approx(ref, abs=1e-3)
    assert np.linalg.norm(A.logit_fit(X, y, l2=50.0)[1:]) < np.linalg.norm(b[1:])  # ridge shrinks


def test_cv_auc_sees_signal_and_not_noise():
    rng = np.random.default_rng(5)
    n = 240
    x = rng.normal(size=n)
    y = (rng.random(n) < 1 / (1 + np.exp(-1.5 * x))).astype(float)
    noise = rng.normal(size=(n, 4))
    assert A.cv_auc(x, y, repeats=5, seed=1) > 0.7
    assert 0.35 < A.cv_auc(noise, y, repeats=5, seed=1) < 0.62


def test_permutation_gain_test_is_calibrated():
    """When the extra columns are noise the permutation p is spread out (rarely tiny); when they carry signal it is small."""
    rng = np.random.default_rng(6)
    n = 160
    ps_null, ps_sig = [], []
    for k in range(10):
        base = rng.normal(size=(n, 1))
        extra = rng.normal(size=(n, 3))
        y = (rng.random(n) < 1 / (1 + np.exp(-base[:, 0]))).astype(float)
        ps_null.append(A.perm_gain(base, extra, y, perms=40, seed=k, repeats=3)[1])
        y2 = (rng.random(n) < 1 / (1 + np.exp(-(base[:, 0] + 1.5 * extra[:, 0])))).astype(float)
        ps_sig.append(A.perm_gain(base, extra, y2, perms=40, seed=k, repeats=3)[1])
    assert np.mean(np.array(ps_null) < 0.1) <= 0.3
    assert np.median(ps_sig) < 0.1


def test_size_strata_are_quantile_bins_and_the_permutation_stays_inside_them():
    """The conditional null (review 2026-11-01): rows are permuted only within bins of team size, so the shape-size
    correlation survives the permutation; with shape built to carry only size, the free null sits lower than the binned one."""
    rng = np.random.default_rng(16)
    n = rng.integers(3, 80, 200).astype(float)
    st = A.size_strata(n)
    assert set(np.unique(st)) == set(range(5)) and max(np.bincount(st)) - min(np.bincount(st)) < 25
    for s in range(5):  # every bin is a contiguous range of n
        assert n[st == s].max() <= n[st > s].min() if (st > s).any() else True
    ln_n = np.log(n)
    y = (rng.random(200) < 1 / (1 + np.exp(-(1.2 * (ln_n - ln_n.mean()))))).astype(float)
    base = np.c_[ln_n, rng.normal(size=200)]
    shape = np.c_[-ln_n + 0.3 * rng.normal(size=200)]  # a top-k share: falls with n, nothing beyond it
    _, p_free, null_free = A.perm_gain(base, shape, y, perms=40, seed=1, repeats=3)
    _, p_strat, null_strat = A.perm_gain(base, shape, y, perms=40, seed=1, repeats=3, strata=st)
    assert null_free.mean() < null_strat.mean() + 0.002 and p_strat > 0.05


def test_grid_family_counts_a_repeated_test_once_and_drops_a_constant():
    rows = [{"perm_p": 0.2}, {"perm_p": 0.2, "same_as_primary": True}, {"perm_p": 0.01}, {"perm_p": 1.0, "degenerate": True}, {"N": 3}]
    assert A.grid_family(rows) == [0, 2]


def test_results_file_has_no_unformatted_fields():
    """A string that missed its f prefix prints the expression instead of the number (found in review 2026-11-01)."""
    if not A.RESULTS.exists():
        pytest.skip("results/apache_activity_survival.md has not been generated: models.apache_activity_survival report")
    text = A.RESULTS.read_text()
    assert not re.search(r"\{[^{}\n]*(\[['\"]|\bfor\b|:\.\d|:\+)[^{}\n]*\}", text)


def test_boot_auc_interval_brackets_the_estimate():
    rng = np.random.default_rng(7)
    y = rng.integers(0, 2, 120)
    s = y + rng.normal(size=120)
    lo, hi = A.boot_auc(y, s, rng, B=300)
    assert lo < A.auc_score(y, s) < hi
    d_lo, d_hi, share = A.boot_auc_diff(y, s, s, rng, B=100)
    assert d_lo == d_hi == 0.0 and share == 0.0


def test_hanley_mcneil_standard_error_is_sane():
    se = A.hanley_se(0.75, 150, 50)
    assert 0.03 < se < 0.05
    assert A.hanley_se(0.75, 1500, 500) < se


# ------------------------------------------------------------------ (1) machinery: early-warning statistics

def test_kendall_time_matches_scipy_including_ties_and_nan():
    rng = np.random.default_rng(8)
    for _ in range(5):
        y = rng.normal(size=14) + np.linspace(0, 1, 14)
        y[3] = y[4]
        assert A.kendall_time(y) == pytest.approx(kendalltau(np.arange(14), y).statistic)
    y = np.array([1.0, np.nan, 2.0, 3.0, 5.0, 4.0])
    ok = ~np.isnan(y)
    assert A.kendall_time(y) == pytest.approx(kendalltau(np.arange(ok.sum()), y[ok]).statistic)
    assert np.isnan(A.kendall_time([1.0, 2.0, 3.0]))


def _ar1(phi, rng):
    e = rng.normal(size=len(phi))
    x = np.zeros(len(phi))
    for t in range(1, len(phi)):
        x[t] = phi[t] * x[t - 1] + e[t]
    return x


def test_rolling_indicators_recover_a_known_ar1_process():
    """L0512: AR1 and variance of the detrended series in a moving window.  For phi = 0.7 the sd is 1/sqrt(1-phi^2)."""
    rng = np.random.default_rng(9)
    x = _ar1(np.full(3000, 0.7), rng)
    ar1, sd = A.rolling_indicators(x, 300)
    assert np.nanmean(ar1) == pytest.approx(0.7, abs=0.08)
    assert np.nanmean(sd) == pytest.approx(1 / np.sqrt(1 - 0.49), rel=0.06)


def test_detrending_keeps_a_drifting_mean_from_looking_like_memory():
    """A straight line plus white noise has high lag-1 autocorrelation unless the line is removed in the window."""
    rng = np.random.default_rng(10)
    x = np.linspace(0, 80, 400) + rng.normal(size=400)
    lin, _ = A.rolling_indicators(x, 40, "linear")
    mean_only, _ = A.rolling_indicators(x, 40, "mean")
    assert abs(np.nanmean(lin)) < 0.25
    assert np.nanmean(mean_only) > 0.6


def test_ews_taus_see_a_long_rising_memory_and_nothing_in_a_constant_one():
    rng = np.random.default_rng(11)
    up = np.array([A.ews_taus(_ar1(np.linspace(0.1, 0.97, 400), rng), 395, 100, 150) for _ in range(20)])
    flat = np.array([A.ews_taus(_ar1(np.full(400, 0.5), rng), 395, 100, 150) for _ in range(20)])
    assert np.nanmean(up[:, 0]) > 0.4 and np.nanmean(up[:, 1]) > 0.3
    assert abs(np.nanmean(flat[:, 0])) < 0.15


def test_early_warning_has_no_power_on_monthly_series_and_some_on_weekly_ones():
    """The finding behind the results file's early-warning verdict: at the series lengths a podling's life
    allows in months, a true slowing down is not told from none; with weekly counts it is, partly."""
    monthly = A.ews_power(6, 12, rng=np.random.default_rng(12), sims=150)
    weekly = A.ews_power(26, 52, rng=np.random.default_rng(12), sims=150)
    assert monthly["auc_ar1"] < 0.65
    assert weekly["auc_ar1"] > 0.65
    assert weekly["alarm_tp_ar1"] > 2 * weekly["alarm_fp_ar1"]


def test_too_short_a_series_returns_nan():
    assert all(np.isnan(v) for v in A.ews_taus(np.arange(10.0), 10, 6, 12))


# ------------------------------------------------------------------ (1) machinery: rules and pseudonyms

def test_robot_patterns_flag_relays_and_spare_surnames():
    flagged = [("jira@apache.org", "Jane Doe (JIRA)"), ("asfgit@git.apache.org", "asfgit"), ("gitbox@apache.org", "GitBox"),
               ("noreply@github.com", "GitHub"), ("hudson@builds.apache.org", "Apache Jenkins Server"), ("commits@x.apache.org", ""),
               ("jclouds-bot@x.org", ""), ("dev-help@x.apache.org", "x")]
    spared = [("bob.jenkins@example.com", "Bob Jenkins"), ("x@example.org", "Paul Hudson"), ("alice@apache.org", "Alice Smith"),
              ("12345+someone@users.noreply.github.com", "Some One"), ("ci-user@foo.com", "Dev")]
    assert all(A.is_bot(a, n) for a, n in flagged)
    assert not any(A.is_bot(a, n) for a, n in spared)


def test_list_classes():
    for name, cls in (("dev", 1), ("dev-de", 1), ("distributedlog-dev", 1), ("user", 2), ("users", 2), ("users-fr", 2), ("announce", 2),
                      ("commits", 0), ("issues", 0), ("notifications", 0), ("reviews", 0), ("distributedlog-commits", 0), ("codereview", 0)):
        assert A.list_class(name) == cls, name
    assert A.is_human_list("marketing") and not A.is_human_list("issues")


def test_month_and_day_helpers():
    days = (np.array(["2009-01-12", "2021-07-31", "2003-04-01"], dtype="datetime64[D]") - np.datetime64("1970-01-01")).astype(int)
    assert A.ym_of_day(days).tolist() == [2009 * 12, 2021 * 12 + 6, 2003 * 12 + 3]
    assert A._day("2009-01-12 17:11:30") == int(days[0])
    assert A._day("1999-01-01 00:00:00") == -1  # before the first valid date
    assert A._day("2105-08-31 00:00:00") == -1  # clocks wrong by a century
    assert A._day("not a date") == -1


def test_address_normalisation():
    assert A._norm_email(" <Alice+list@Example.ORG> ") == "alice@example.org"
    assert A._norm_email("") == ""


def test_pseudonymiser_is_salted_and_stable():
    a, b = A._Pseudonymiser(b"salt-one-16bytes"), A._Pseudonymiser(b"salt-two-16bytes")
    assert a("x@y.org") == a("x@y.org") != b("x@y.org")
    assert a("x@y.org") != a("z@y.org")


def test_relabelling_is_project_local_dense_and_joins_the_two_files():
    """The same hash in the commit file and in the mail file becomes one integer; ids start at 0 in each project,
    numbered by first activity; the bot flag is the OR over both files.  No hash value survives."""
    C = {"proj": np.array([0, 0, 1], np.int16), "person": np.array([111, 222, 111], np.uint64), "day": np.array([50, 10, 5], np.int32),
         "bot": np.array([False, False, False])}
    E = {"proj": np.array([0, 0, 1, 1], np.int16), "person": np.array([222, 333, 444, 111], np.uint64), "day": np.array([20, 5, 7, 9], np.int32),
         "bot": np.array([True, False, False, False])}
    (cp, ep), p_proj, p_local, p_bot = A._relabel_two(C, E)
    # project 0: first days 333 (5), 222 (10), 111 (50) -> 0, 1, 2
    assert cp[:2].tolist() == [2, 1]
    assert ep[:2].tolist() == [1, 0]  # 222 shared with the commit file, 333 only in mail
    # project 1: 111 (5), 444 (7) -> 0, 1; 111 in mail (day 9) is the same person as in commits
    assert cp[2] == 0 and ep[2:].tolist() == [1, 0]
    assert p_proj.tolist() == [0, 0, 0, 1, 1] and p_local.tolist() == [0, 1, 2, 0, 1]
    assert p_bot.tolist() == [False, True, False, False, False]  # person 222 of project 0 was a robot in the mail file
    assert max(cp.max(), ep.max()) < 3


# ------------------------------------------------------------------ (1) machinery: tables on synthetic panels

def _synthetic_panel(seed=0, projects=6, months=30):
    """Hand-made matrices: even projects 'graduate' with growing activity and an even-ish team, odd ones 'retire' with decay."""
    rng = np.random.default_rng(seed)
    mats = {k: [] for k in ("commits", "files", "loc", "msg_human", "msg_dev", "msg_all", "reply_human")}
    labels, exit_m = [], []
    for p in range(projects):
        grad = p % 2 == 0
        n = 9 if grad else 5
        rate = np.linspace(1.0, 4.0, months) if grad else np.linspace(3.0, 0.1, months)
        C = rng.poisson(rate[None, :] * np.linspace(2.0, 0.5, n)[:, None]).astype(float)
        for k in mats:
            mats[k].append(C.copy() if k in ("commits", "files") else np.zeros_like(C))
        labels.append(1 if grad else 0)
        exit_m.append(months - 1 if grad else months - 3)
    return A.Panel.synthetic(mats, labels, exit_m)


def test_landmark_table_on_a_synthetic_panel():
    P = _synthetic_panel()
    t = A.landmark_table(P, 12, min_months=3)
    assert len(t["y"]) == 6 and t["y"].tolist() == [1, 0, 1, 0, 1, 0]
    first = P.window_totals(0, "events", 0, 12, min_months=3)
    assert t["n"][0] == len(first) and t["T"][0] == first.sum()
    assert t["gini"][0] == pytest.approx(A.gini_corrected(first))
    # a podling that exits before the landmark is not at risk at it
    P.exit_m[1] = 5
    assert len(A.landmark_table(P, 12, min_months=3)["y"]) == 5


def test_hazard_table_labels_competing_exits_correctly():
    P = _synthetic_panel()
    h = A.hazard_table(P, w=6, h=6, step=3, t_min=6)
    for p in range(6):
        rows = h["p"] == p
        em, lab = int(P.exit_m[p]), int(P.label[p])
        t = h["t"][rows]
        assert t.max() <= em  # still incubating at every origin
        want_ret = (t + 6 > em) & (lab == 0)
        assert (h["y_ret"][rows] == want_ret).all()
        assert (h["y_grad"][rows] == ((t + 6 > em) & (lab == 1))).all()


def test_trajectory_classes_separate_growth_to_the_end_from_collapse():
    months = 36
    up = np.tile(np.linspace(1, 20, months), (6, 1)).round()
    down = np.tile(np.r_[np.linspace(1, 20, 12), np.linspace(20, 0, 6), np.zeros(18)], (6, 1)).round()
    mats = {k: [up if k == "commits" else np.zeros_like(up), down if k == "commits" else np.zeros_like(down)] for k in
            ("commits", "files", "loc", "msg_human", "msg_dev", "msg_all", "reply_human")}
    P = A.Panel.synthetic(mats, [1, 0], [months - 1, months - 1])
    tc = A.trajectory_classes(P)["classes"]
    assert tc["ended at peak"]["grad"] == 1 and tc["collapsed"]["ret"] == 1


def test_step_against_smooth_picks_the_right_form():
    rng = np.random.default_rng(13)
    x = rng.normal(size=300)
    y_step = (rng.random(300) < np.where(x > 0.3, 0.9, 0.15)).astype(float)
    y_smooth = (rng.random(300) < 1 / (1 + np.exp(-0.9 * x))).astype(float)
    a, b = A.step_vs_smooth(x, y_step, repeats=5), A.step_vs_smooth(x, y_smooth, repeats=5)
    assert a["step_logloss"] < a["smooth_logloss"]
    assert b["smooth_logloss"] < b["step_logloss"]


def _member_world(coupled: bool, seed=0, projects=24, members=10, months=60):
    """Members are active with a probability that depends on their own last month (D1); if `coupled`, also on
    the share of the others active last month (D2).  The comparison must find D2 only when it is there."""
    rng = np.random.default_rng(seed)
    mats = {k: [] for k in ("commits", "files", "loc", "msg_human", "msg_dev", "msg_all", "reply_human")}
    for _ in range(projects):
        act = np.zeros((members, months))
        act[:, 0] = rng.random(members) < 0.5
        for t in range(1, months):
            share = act[:, t - 1].mean()
            lin = -1.5 + 1.6 * act[:, t - 1] + (3.5 * (share - 0.5) if coupled else 0.0)
            act[:, t] = rng.random(members) < 1 / (1 + np.exp(-lin))
        for k in mats:
            mats[k].append(act.copy() if k == "commits" else np.zeros_like(act))
    return A.Panel.synthetic(mats, [1] * projects, [months - 1] * projects)


def test_the_coupling_test_finds_coupling_when_present_and_not_when_absent():
    """The D1-against-D2 comparison of section 5.5 must have power: a world with real coupling shows a gain, one without shows none."""
    gains = {}
    for coupled in (False, True):
        mp = A.member_panel(_member_world(coupled), min_members=5)
        gains[coupled] = A.d1_d2_analysis(mp, repeats=1, boot=60)["D2 gain"]["diff"]
    assert gains[False] < 0.005
    assert gains[True] > 0.01


def test_conditional_shape_coefficient_recovers_a_known_direction():
    """The direction table of the conversation lead: with the outcome built to depend on the Gini at a given size and
    mean, the standardised coefficient is positive with an interval above zero; with it built not to, the interval covers zero."""
    rng = np.random.default_rng(14)
    n = 220
    ln_n, ln_mean, gini = rng.normal(size=n), rng.normal(size=n), rng.normal(size=n)
    base = {"n": np.full(n, 10.0), "gini": gini, "ln_mean": ln_mean, "ln_n": ln_n}
    for beta, expect_pos in ((1.2, True), (0.0, False)):
        y = (rng.random(n) < 1 / (1 + np.exp(-(0.8 * ln_n + beta * gini)))).astype(float)
        c = A.cond_shape_coefs(base | {"y": y}, features=("gini",), boot=200)["gini"]
        assert (c[1] > 0) is expect_pos or (not expect_pos and c[1] < 0 < c[2])


def test_gini_against_mean_finds_the_better_predictor():
    rng = np.random.default_rng(15)
    n = 240
    ln_n, ln_mean, gini = rng.normal(size=n), rng.normal(size=n), rng.normal(size=n)
    y = (rng.random(n) < 1 / (1 + np.exp(-(0.6 * ln_n + 1.5 * gini)))).astype(float)
    r = A.gini_vs_mean({"n": np.full(n, 10.0), "gini": gini, "ln_mean": ln_mean, "ln_n": ln_n, "y": y}, repeats=3, boot=200)
    assert r["diff"] > 0.1 and r["lo"] > 0


# ------------------------------------------------------------------ (1) machinery: guards

def test_primary_specification_is_the_one_written_down():
    """The decision rules were fixed before the outcome relations were computed; changing PRIMARY silently would void them."""
    assert A.PRIMARY["W"] == 12 and A.PRIMARY["min_n"] == 3 and A.PRIMARY["shape"] == ("gini", "top1", "top3", "entropy")
    assert A.PRIMARY["base"] == ("ln_n", "ln_mean") and A.PRIMARY["folds"] == 5 and A.PRIMARY["l2"] == 1.0
    assert (A.PRIMARY["ews_w"], A.PRIMARY["ews_L"]) == (6, 12)
    assert A.regular_months(12) == 3 and A.regular_months(3) == 2 and A.regular_months(24) == 6


def test_results_file_names_no_person():
    """No name, no address in the results (CC BY data are aggregated; the files carry personal data, L4623)."""
    if not A.RESULTS.exists():
        pytest.skip("results/apache_activity_survival.md has not been generated: models.apache_activity_survival report")
    text = A.RESULTS.read_text()
    assert "@" not in text
    assert not re.search(r"\b[\w.+-]+@[\w-]+\.[\w.]+\b", text)


def test_results_file_has_the_parts_the_brief_asks_for():
    """Data and terms, method, the null, numbers with uncertainty, the verdict, caveats, a Variations section."""
    if not A.RESULTS.exists():
        pytest.skip("results/apache_activity_survival.md has not been generated: models.apache_activity_survival report")
    text = A.RESULTS.read_text()
    for h in ("## Verdict", "## 1. Data and terms", "## 2. Method", "## 3. Does the distribution beat the mean?", "## 4. What changes with n",
              "## 5. Cascade and escalation analogues", "## 6. The survival form", "## 7. Variations", "## 8. What this test cannot say", "## Reproduce"):
        assert h in text, h
    assert "CC BY 4.0" in text and "952ec9c66f1c2a96ddf3deab2e78f9e9" in text and "doi:10.5281/zenodo.5637530" in text
    assert "The nulls" in text and "Pre-specified" in text and "What an activity-first outcome could be fitted to" in text


# ------------------------------------------------------------------ (2) data tests

@pytest.fixture(scope="module")
def panel():
    return A.Panel()


@pytest.fixture(scope="module")
def tab(panel):
    return A.landmark_table(panel, A.PRIMARY["W"])


@needs_data
def test_build_reproduces_the_counts_of_117():
    """L4624, L4625: 12,608,575 commit rows from 265 projects; 2,161,558 messages from 274 projects.  The csv parser
    meets 562 and 7 short records beyond these; set aside they leave exactly 117's counts."""
    m = json.loads((A.DERIVED / "meta.json").read_text())
    assert m["limit"] is None, "derived/ was built with --limit (a smoke test); rebuild"
    assert m["commit_rows"] - m["commit_malformed"] == A.COUNTS_117["commit_rows"]
    assert m["email_rows"] - m["email_malformed"] == A.COUNTS_117["email_rows"]
    assert m["commit_projects"] == A.COUNTS_117["commit_projects"] and m["email_projects"] == A.COUNTS_117["email_projects"]
    assert 340_000 < m["commit_commits"] < 370_000  # file rows grouped by revision


@needs_data
def test_nothing_personal_is_left_by_the_build():
    m = json.loads((A.DERIVED / "meta.json").read_text())
    for name in m["projects"] + m["lists"]:
        assert "@" not in name and " " not in name
    assert "@" not in json.dumps(m)
    for f in ("commits.npz", "emails.npz", "persons.npz"):
        z = np.load(A.DERIVED / f, allow_pickle=False)
        for k in z.files:
            assert z[k].dtype.kind in "iub", (f, k, z[k].dtype)  # integers and booleans only: no strings
    # no 64-bit hash survived: person ids are small project-local integers
    assert np.load(A.DERIVED / "commits.npz")["person"].max() < 5_000
    assert np.load(A.DERIVED / "emails.npz")["person"].max() < 5_000


@needs_data
def test_person_ids_are_dense_within_each_project(panel):
    pz = np.load(A.DERIVED / "persons.npz")
    for p in range(len(panel.names)):
        loc = np.sort(pz["local"][pz["proj"] == p])
        assert loc.tolist() == list(range(len(loc)))


@needs_data
def test_labels_agree_with_the_papers_counts(panel):
    """L4628, L4629, L4630: 269 projects in the MSR paper, 273 (211 graduated + 62 retired) in the APEX paper; the ASF's own
    status file labels all but a few of the 275 names, and every matched project is resolved by the data end."""
    res = panel.resolved()
    assert panel.matched.sum() >= 262 and len(res) == panel.matched.sum()
    g, r = int((panel.label[res] == 1).sum()), int((panel.label[res] == 0).sum())
    assert 195 <= g <= 215 and 58 <= r <= 70
    assert abs(g + r - 269) <= 2  # the MSR paper's 269 labelled projects (L4628)


@needs_data
def test_podlings_older_than_the_commit_file_are_few_and_change_nothing(panel):
    """L4624, L4625: commits start 2005-01-30, mail 2003-04-01.  The podlings whose first year predates the commit file
    have too small an n; there are few, and the size effect and the null shape gain stand without them (review 2026-11-01)."""
    c = A.coverage_check(panel, repeats=4, perms=0)
    assert 3 <= c["short"] <= 15 and c["committers_short"] < c["committers_rest"]
    assert c["primary_rest"]["auc_size"] > 0.7 and abs(c["primary_rest"]["gain"]) < 0.02


@needs_data
def test_activity_stops_at_the_exit_month(panel):
    """The files cover the incubation only: almost nothing falls after the exit month; the exit month itself is active."""
    D = A.descriptives(panel)
    assert D["share_events_after_exit_month"] < 0.03
    k, n = D["last_active_is_exit_month"]["graduated"]
    assert k / n > 0.9


@needs_data
def test_robots_carry_much_of_the_mail_and_little_of_the_code(panel):
    D = A.descriptives(panel)
    assert 0.3 < D["activity_robot_share"]["msg_human"] < 0.6
    assert D["activity_robot_share"]["commits"] < 0.1


@needs_data
def test_primary_landmark_table(tab):
    y = tab["y"]
    assert abs(len(y) - 207) <= 3 and abs(int(y.sum()) - 155) <= 3 and abs(int((1 - y).sum()) - 52) <= 3
    assert 15 <= np.median(tab["n"]) <= 25  # a team, not a crowd (the any-event rule gives a median of 56)
    assert (tab["exit_m"] >= 12).all()  # nothing at risk exited inside the window


@needs_data
def test_shape_adds_nothing_to_size_and_mean_for_graduation(tab):
    """The recorded finding of question 1 (not a tuned pass): size predicts, the mean does not, the shape adds no
    held-out gain, in the primary specification."""
    r = A.h1_analysis(tab, perms=80, boot=300, repeats=6)
    assert 0.70 < r["single"]["size ln n"]["auc"] < 0.84
    assert r["single"]["mean ln(T/n)"]["auc"] < 0.66
    assert abs(r["gain"]["diff"]) < 0.03 and r["gain"]["perm_p"] > 0.05
    assert r["gain"]["perm_p_strat"] > 0.05  # the conditional null (within size quintiles) agrees
    assert r["gain"]["lo"] < 0 < r["gain"]["hi"] or abs(r["gain"]["diff"]) < 0.02
    assert r["gini_obs_median"] > 3 * r["gini_null_median"]  # far more concentrated than interchangeable members


@needs_data
def test_graduation_rises_with_size_and_the_shape_effect_depends_on_it(tab):
    """L5779 (the sign of a group-size effect depends on a moderator, there the return) and L5740 (the turnover effect
    flips with community size): an effect that changes with a setting, here concentration's with n.  Pre-specified
    interaction test (2 df), and the review's split of it: the Gini x ln n term carries it, the mean x ln n term does not."""
    s = A.size_analysis(tab, boot=200, repeats=4, perm_halves=20)
    rates = [b["rate"] for b in s["bins"] if b["N"] >= 15]
    assert rates == sorted(rates) or rates[-1] > rates[0] + 0.25
    assert s["bins"][-1]["rate"] > 0.85 and s["bins"][-1]["label"] == "26+"
    assert s["interaction_lr"]["p"] < 0.01
    assert s["interaction_gini_lr"]["p"] < 0.01 and s["interaction_mean_lr"]["p"] > 0.05


@needs_data
def test_growth_separates_the_outcomes(tab):
    g = A.growth_analysis(tab)
    c = g["classes"]
    assert c["growth"]["rate"] > c["steady"]["rate"] > c["decline"]["rate"]
    assert g["fisher_growth_vs_decline"] < 0.01


@needs_data
def test_early_warning_does_not_discriminate_retirement(panel):
    """Monthly series: no separation (and, by the power test above, no power).  Weekly series: no separation either,
    where the simulated signal would be caught.  The level trend does separate."""
    rng = np.random.default_rng(1)
    m = A.ews_table(panel, w=6, L=12, lag=1)
    ar1 = A.ews_compare(m, "tau_ar1", rng, boot=100)
    lev = A.ews_compare(m, "tau_level", rng, boot=100)
    assert 0.40 < ar1["auc"] < 0.62
    assert lev["auc"] < 0.40
    w = A.ews_table_weekly(panel, w=26, L=52, lag=0)
    assert A.ews_compare(w, "tau_ar1", rng, boot=100)["auc"] < 0.55


@needs_data
def test_weekly_series_agree_with_monthly_ones(panel):
    """The weekly series (7-day bins from the first of the start month) must carry the same events as the monthly matrices."""
    for p in panel.resolved()[::27]:
        wk, mo = panel.weekly_total(p).sum(), panel.monthly_total(p, "events").sum()
        assert abs(wk - mo) <= 0.01 * max(mo, 1), (panel.names[p], wk, mo)


@needs_data
def test_weekly_within_project_comparison_runs_and_is_a_percentile(panel):
    t = A.ews_time_matched_weekly(panel, w=26, L=52, lag=0)
    assert len(t["y"]) >= 20
    u = t["u_ar1"][np.isfinite(t["u_ar1"])]
    assert ((u >= 0) & (u <= 1)).all()


@needs_data
def test_conversation_concentration_lead_is_recorded(panel):
    """The recorded lead of section 7.4 (a finding of a search, not a confirmed result): for development-list messages
    the shape adds held-out AUC to size and mean at 12 and 18 months, in the later podlings, and not with robots kept;
    for commits plus messages it does not at 12 months."""
    kw = dict(repeats=4, perms=100, seed=A.SEED)
    r12 = A.quick_eval(A.landmark_table(panel, 12, measure="dev_messages"), perms_strat=100, **kw)
    r18 = A.quick_eval(A.landmark_table(panel, 18, measure="dev_messages"), perms_strat=100, **kw)
    assert r12["gain"] > 0.015 and r12["perm_p"] < 0.05 and r12["perm_p_strat"] < 0.05
    assert r18["gain"] > 0.04 and r18["perm_p"] < 0.05 and r18["perm_p_strat"] < 0.05
    late = [p for p in panel.resolved() if panel.start_ym[p] // 12 >= 2013]
    assert A.quick_eval(A.landmark_table(panel, 12, measure="dev_messages", projects=late), **kw)["gain"] > 0.03
    assert A.quick_eval(A.landmark_table(panel, 12, measure="dev_messages", bots="keep"), **kw)["gain"] < 0.02
    assert A.quick_eval(A.landmark_table(panel, 12), **kw)["gain"] < 0.02  # commits plus messages: the primary, no gain
    g = A.gini_vs_mean(A.landmark_table(panel, 12, measure="dev_messages"), repeats=4, boot=300)
    assert g["lo"] > 0  # the Gini beats the mean for conversation


@needs_data
def test_smooth_beats_step_in_early_size(tab):
    ok = np.isfinite(tab["ln_n"]) & (tab["n"] >= 3)
    r = A.step_vs_smooth(tab["ln_n"][ok], tab["y"][ok], repeats=5)
    assert r["smooth_logloss"] < r["step_logloss"] < r["base_logloss"]


@needs_data
def test_survival_form_agrees_with_the_landmark_form(panel):
    h = A.hazard_table(panel)
    r = A.hazard_analysis(h, target="y_ret", repeats=2, boot=100)
    assert r["tenure+size+mean"]["auc"] > 0.7
    assert r["shape gain"]["lo"] < 0 < r["shape gain"]["hi"] or abs(r["shape gain"]["diff"]) < 0.02
    assert r["events"] == int(h["y_ret"].sum()) and r["event_projects"] <= 70


@needs_data
def test_individual_dynamics_carry_the_member_level_signal(panel):
    """v0 section 7 'Team': D2 adds no practical gain over D1 for who stays active (the test of the machinery
    on synthetic worlds above shows it would have found one)."""
    mp = A.member_panel(panel)
    r = A.d1_d2_analysis(mp, repeats=1, boot=100)
    assert r["D1"]["auc"] > 0.85
    assert r["D2 gain"]["diff"] < 0.01
