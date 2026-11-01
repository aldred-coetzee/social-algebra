"""The sign-law registry's five tests (112 section 6.5), and the checks that the machinery behind them is right.

Prior work: docs/prior-work/112 section 6.2 (R-E: z = a_i + b_j + sum c_tau n_tau; pp +, pm -, mp -, mm -; ledger L5421,
L4811, L4833), section 6.5 (the five tests); 106 (Leskovec, Huttenlocher & Kleinberg 2010, "LHK": 16 directed triad types
L4814, status and balance rules L4800-L4801, weak balance L4815, accuracies L4826-L4829, visibility L4852, symmetry L4812);
117 (data: wiki-RfA L4561-L4564, Bitcoin L4567-L4580, BlueTempNet L4593-L4598).  Module: models/sign_registry_battery.py;
results and verdict: sim/results/sign_registry_battery.md (produced by `report` from the same functions).

Four groups.
 (1) MACHINERY, no data: the triad counter against a brute-force definition (causal and static), the no-leakage properties
     (changing the future changes no causal feature and no earlier forward-chained prediction), the logistic fit against
     scipy, AUC against its definition, the bootstrap, the parsers, the decision rules as pre-registered, the symmetry,
     visibility tests on constructed networks whose answer is known, and a PLANTED-MECHANISM check (a synthetic
     network with and without a forward-chain mechanism pushed through the same pipeline) so that a null result is known to be
     one the test could have avoided.
 (2) DATA INTEGRITY, skipped with the fetch command when a git-ignored file is absent: checksums and the counts 117 printed.
 (3) THE REGISTRY'S PREDICTIONS on the four sites.  These assert what 112 section 6.5 predicts; where the data refuted a
     prediction the test is `xfail(strict=True)` with the measured value in the reason (a finding, not a tuned test), and a
     second test asserts the measured fact.  The thresholds are the pre-registered constants; none was moved to pass.
 (4) THE REPORT is regenerated from the cached statistics (skipped when they are absent).
"""
from __future__ import annotations

import math

import numpy as np
import pytest
from scipy import optimize, special, stats

from models import sign_registry_battery as sr


def needs(key):
    return pytest.mark.skipif(
        not sr.available(key),
        reason=f"sim/data/{sr.SOURCES[key].rel} is absent (local-use-only, git-ignored): "
               f"cd sim && ~/.local/bin/uv run python -m models.sign_registry_battery fetch {key}")


SITES = [pytest.param(k, marks=needs(k), id=k) for k in sr.SITE_ORDER]


# ------------------------------------------------------------------------------------------------- constructed networks

def toy_edges(seed=1, n=25, m=160, tmax=90):
    """A random signed digraph with many tied timestamps."""
    rng = np.random.default_rng(seed)
    pairs = set()
    while len(pairs) < m:
        a, b = rng.integers(0, n, 2)
        if a != b:
            pairs.add((int(a), int(b)))
    pairs = sorted(pairs)
    u = np.array([p[0] for p in pairs])
    v = np.array([p[1] for p in pairs])
    s = np.where(rng.random(m) < 0.65, 1, -1)
    t = rng.integers(0, tmax, m).astype(float)
    return sr._sorted_edgeset("toy", u, v, s, t, v.copy(), n, {})


def skeleton(n=900, m=16000, seed=3, closure=0.6):
    """A time-ordered who-rates-whom skeleton with heavy-tailed activity and triadic closure (so that triads exist)."""
    rng = np.random.default_rng(seed)
    act = rng.lognormal(0, 1.0, n)
    act /= act.sum()
    pop = rng.lognormal(0, 1.0, n)
    pop /= pop.sum()
    nbrs = [[] for _ in range(n)]
    seen = set()
    u_l, v_l = [], []
    senders = rng.choice(n, size=m * 3, p=act)
    k = 0
    while len(u_l) < m and k < len(senders):
        u = int(senders[k])
        k += 1
        if rng.random() < closure and nbrs[u]:
            w = nbrs[u][rng.integers(len(nbrs[u]))]
            if nbrs[w]:
                v = nbrs[w][rng.integers(len(nbrs[w]))]
            else:
                v = int(rng.choice(n, p=pop))
        else:
            v = int(rng.choice(n, p=pop))
        if v == u or (u, v) in seen:
            continue
        seen.add((u, v))
        nbrs[u].append(v)
        nbrs[v].append(u)
        u_l.append(u)
        v_l.append(v)
    m = len(u_l)
    t = np.arange(m, dtype=float)
    u, v = np.array(u_l), np.array(v_l)
    return sr.EdgeSet("skeleton", u.astype(np.int32), v.astype(np.int32), np.ones(m, np.int8), t, v.astype(np.int32), n, {})


def person_eta(E, seed=5, sd_send=0.9, sd_recv=0.9, base=1.2):
    rng = np.random.default_rng(seed)
    a = rng.normal(0, sd_send, E.n_nodes)
    b = rng.normal(0, sd_recv, E.n_nodes)
    return base + a[E.u] + b[E.v]


# ------------------------------------------------------------------------------------------------- (1) machinery: tables

def test_type_order_and_names():
    """16 types [F|B][F|B][p|m][p|m] in the order FF FB BF BB x pp pm mp mm [L4814]."""
    assert len(sr.TYPES) == 16 and sr.TYPES[0] == "FFpp" and sr.TYPES[3] == "FFmm" and sr.TYPES[15] == "BBmm"
    assert sr.TYPES[sr.TYPE_INDEX["FBmp"]] == "FBmp"
    assert sr.FORWARD == ("FFpp", "FFpm", "FFmp", "FFmm")
    assert [sr.FORWARD_SIGN[n] for n in sr.FORWARD] == [1, -1, -1, -1]       # 112 section 6.2 [L5421]


def test_status_rule_predicts_eight_types_as_lhk():
    """Status predicts 8 of the 16 types (sign of the oriented sum, 0 when the two cancel) [L4801, L4836]; the eight are
    FFpp +, FFmm -, FBpm +, FBmp -, BFpm -, BFmp +, BBpp -, BBmm + (so 'status disagrees at Epinions on FBpm, BFmp and BBmm'
    is a statement about learned signs against exactly these)."""
    pred = {n: int(v) for n, v in zip(sr.TYPES, sr.STATUS) if v}
    assert pred == {"FFpp": 1, "FFmm": -1, "FBpm": 1, "FBmp": -1, "BFpm": -1, "BFmp": 1, "BBpp": -1, "BBmm": 1}


def test_balance_rules():
    """Strict balance: the product of the two signs, direction ignored, on all 16 types [L4800]; weak balance agrees on
    pp, pm, mp and makes no prediction on mm [L4815]."""
    for i, n in enumerate(sr.TYPES):
        s1 = 1 if n[2] == "p" else -1
        s2 = 1 if n[3] == "p" else -1
        assert sr.BAL_STRICT[i] == s1 * s2
        assert sr.BAL_WEAK[i] == (0 if n.endswith("mm") else s1 * s2)


def test_forward_chain_status_is_balance_except_mm():
    """On forward chains balance gives (+, -, -, +), weak balance (+, -, -, 0) and status (+, 0, 0, -) [L4811]: FFmm is the
    type that separates balance (+) from status (-), which is why the registry's headline is FFmm < 0."""
    idx = [sr.TYPE_INDEX[n] for n in sr.FORWARD]
    assert list(sr.BAL_STRICT[idx]) == [1, -1, -1, 1]
    assert list(sr.BAL_WEAK[idx]) == [1, -1, -1, 0]
    assert list(sr.STATUS[idx]) == [1, 0, 0, -1]


def test_pre_registered_rules_are_the_ones_in_the_module_docstring():
    """The decision rules were fixed before any result was computed; this test pins the numbers."""
    assert sr.RULE_MIN_SUPPORT == 100 and sr.RULE_G_MATERIAL == 0.02 and sr.RULE_FLIP_BINS == 2
    assert sr.RULE_INTERCEPT_RANGE == 0.5 and sr.RULE_RARE == 0.10 and sr.RULE_GAP == 0.02
    doc = sr.__doc__
    for token in ("RULE_MIN_SUPPORT = 100", "RULE_G_MATERIAL", "0.02 AUC", "RULE_FLIP_BINS = 2", "RULE_RARE = 0.10"):
        assert token in doc


def test_classify_z_rule_r1():
    assert sr.classify_z(-1, -3.0, 500) == "SUPPORTED"
    assert sr.classify_z(-1, +3.0, 500) == "CONTRADICTED"
    assert sr.classify_z(-1, -1.9, 500) == "UNDECIDED"
    assert sr.classify_z(+1, +2.5, 500) == "SUPPORTED"
    assert sr.classify_z(-1, +9.0, 99) == "UNDECIDED"                    # below adequate support nothing counts
    assert sr.classify_z(-1, float("nan"), 500) == "UNDECIDED"


def test_r5_verdict_needs_both_cluster_rules():
    """Review 2026-11-01: SUPPORTED and ABSENT both need the receiver-cluster and the two-way interval to agree."""
    assert sr.r5_both("SUPPORTED", "SUPPORTED") == "SUPPORTED" and sr.r5_both("ABSENT", "ABSENT") == "ABSENT"
    assert sr.r5_both("ABSENT", "UNDECIDED") == "UNDECIDED" and sr.r5_both("SUPPORTED", "UNDECIDED") == "UNDECIDED"
    assert sr.r5_both("UNDECIDED", "UNDECIDED") == "UNDECIDED"


def test_r2_tiers_and_overall():
    mk = lambda d, lo, hi: dict(diff=d, ci=(lo, hi))
    assert sr.r2_tier(mk(0.03, 0.02, 0.04)) == "material"
    assert sr.r2_tier(mk(0.015, 0.01, 0.02)) == "small"
    assert sr.r2_tier(mk(0.03, -0.01, 0.05)) == "none"
    assert sr.r2_tier(mk(-0.006, -0.013, 0.0005)) == "none"
    assert sr.r2_overall(["material"] * 3 + ["none"]) == "YES"
    assert sr.r2_overall(["material", "small", "none", "none"]) == "NO"
    assert sr.r2_overall(["material", "material", "none", "none"]) == "MIXED"


# ------------------------------------------------------------------------------------------------- (1) machinery: triads

@pytest.mark.parametrize("mode", ["causal", "static"])
def test_triad_counts_match_brute_force_definition(mode):
    """Every row (16 types and embeddedness) against a definition-level scan of the other edges, on a graph with many tied
    timestamps (ties are simultaneous and invisible in the causal mode)."""
    E = toy_edges()
    F = sr.compute_features(E, mode)
    for k in range(E.m):
        cnt, emb = sr.brute_force_triads(E, k, mode)
        assert np.array_equal(cnt, F.tri[k]) and emb == F.emb[k], (mode, k)
    assert F.tri.sum() > 0


def test_causal_features_equal_those_of_the_prefix_run():
    """The no-leakage property, stated as an identity: the causal features of an edge are what a run on only the edges with
    time <= its own gives (so nothing later can have entered)."""
    E = toy_edges(seed=4)
    F = sr.compute_features(E, "causal")
    rng = np.random.default_rng(0)
    for k in rng.choice(E.m, 25, replace=False):
        pre = np.flatnonzero(E.t <= E.t[k])
        Fp = sr.compute_features(E.take(pre), "causal")
        row = int(np.flatnonzero(pre == k)[0])
        for name in ("tri", "emb", "op", "on", "ip", "inn", "uip", "uin", "vop", "von", "rev", "grate"):
            assert np.allclose(getattr(F, name)[k], getattr(Fp, name)[row]), (k, name)


def test_changing_the_future_changes_no_causal_feature_but_changes_static_ones():
    """Flip every sign after time T: causal features of edges at or before T are unchanged; the static ones are not (the
    control that shows the test could fail)."""
    E = toy_edges(seed=2)
    T = 45.0
    E2 = sr.EdgeSet(E.name, E.u, E.v, np.where(E.t > T, -E.s, E.s).astype(np.int8), E.t, E.cluster, E.n_nodes, {})
    early = E.t <= T
    Fc, Fc2 = sr.compute_features(E, "causal"), sr.compute_features(E2, "causal")
    for name in ("tri", "emb", "op", "on", "ip", "inn", "uip", "uin", "vop", "von", "rev", "grate"):
        assert np.allclose(getattr(Fc, name)[early], getattr(Fc2, name)[early]), name
    Fs, Fs2 = sr.compute_features(E, "static"), sr.compute_features(E2, "static")
    assert not np.array_equal(Fs.tri[early], Fs2.tri[early])


def test_edges_with_the_same_timestamp_do_not_see_each_other():
    """u->w and w->v at one instant: neither is evidence for u->v at that instant; an instant later both are."""
    u = np.array([0, 1, 0, 0])
    v = np.array([1, 2, 2, 2])
    s = np.array([1, 1, 1, 1])
    t = np.array([5.0, 5.0, 6.0, 7.0])
    E = sr._sorted_edgeset("tie", u, v, s, t, v.copy(), 3, {})
    F = sr.compute_features(E, "causal")
    # edge index 2 is 0->2 at t=6 (path 0->1, 1->2 at t=5 is visible); edge 3 would be a duplicate pair, ignored by the test
    assert F.tri[2, sr.TYPE_INDEX["FFpp"]] == 1 and F.emb[2] == 1
    # the two t=5 edges (0->1 and 1->2) are each other's neighbours only through each other: no triad for either
    assert F.tri[0].sum() == 0 and F.tri[1].sum() == 0


def test_static_features_do_not_use_the_edge_itself():
    """Flipping an edge's own sign leaves its own static features (triads, degrees, global rate) unchanged."""
    E = toy_edges(seed=7)
    F = sr.compute_features(E, "static")
    for k in (0, 17, 90, 150):
        s2 = E.s.copy()
        s2[k] = -s2[k]
        F2 = sr.compute_features(sr.EdgeSet(E.name, E.u, E.v, s2, E.t, E.cluster, E.n_nodes, {}), "static")
        for name in ("tri", "emb", "op", "on", "ip", "inn", "uip", "uin", "vop", "von", "rev"):
            assert np.allclose(getattr(F, name)[k], getattr(F2, name)[k]), (k, name)
        assert math.isclose(F.grate[k], F2.grate[k])


def test_sampled_queries_equal_full_queries_on_the_rows_asked_for():
    E = toy_edges(seed=3)
    full = sr.compute_features(E, "causal")
    mask = np.zeros(E.m, bool)
    mask[::7] = True
    part = sr.compute_features(E, "causal", query=mask)
    assert np.array_equal(full.tri[mask], part.tri[mask]) and part.tri[~mask].sum() == 0


# ------------------------------------------------------------------------------------------------- (1) machinery: models

def test_logit_matches_a_generic_optimiser_and_standardisation_is_transparent():
    rng = np.random.default_rng(0)
    n, k = 4000, 5
    X = rng.normal(size=(n, k)) * np.array([1, 3, 0.5, 10, 1])
    beta = rng.normal(size=k)
    y = (rng.random(n) < special.expit(X @ beta + 0.4)).astype(float)
    fit = sr.fit_logit(X, y, ridge=0.0)
    nll = lambda b: np.sum(np.logaddexp(0, X @ b[1:] + b[0]) - y * (X @ b[1:] + b[0]))
    ref = optimize.minimize(nll, np.zeros(k + 1), method="BFGS", options={"gtol": 1e-9})
    assert fit.converged and np.allclose(fit.coef, ref.x[1:], atol=1e-5) and abs(fit.intercept - ref.x[0]) < 1e-5
    fit2 = sr.fit_logit(X * np.array([1, 1, 1, 1000, 1]), y, ridge=0.0)       # a column in other units
    assert np.isclose(fit2.coef[3] * 1000, fit.coef[3], atol=1e-5)
    assert abs(fit.loglik + nll(ref.x)) < 1e-3


def test_ridge_shrinks_and_leaves_the_intercept_alone():
    rng = np.random.default_rng(1)
    X = rng.normal(size=(500, 3))
    y = (rng.random(500) < special.expit(2 * X[:, 0] + 1.0)).astype(float)
    free, shrunk = sr.fit_logit(X, y, ridge=0.0), sr.fit_logit(X, y, ridge=500.0)
    assert np.all(np.abs(shrunk.coef) < np.abs(free.coef))
    assert abs(shrunk.decision(X).mean() - special.logit(y.mean())) < 0.2         # base rate is kept by the free intercept


def test_cluster_robust_covariance_matches_a_direct_sandwich():
    rng = np.random.default_rng(2)
    n = 600
    cl = rng.integers(0, 40, n)
    X = rng.normal(size=(n, 2))
    y = (rng.random(n) < special.expit(X[:, 0] - 0.5 + 0.5 * (cl % 3 - 1))).astype(float)
    fit = sr.fit_logit(X, y, ridge=0.0, cluster=cl, se=True)
    Z = np.column_stack([np.ones(n), X])
    p = special.expit(Z @ np.r_[fit.intercept, fit.coef])
    H = (Z * (p * (1 - p))[:, None]).T @ Z
    S = np.array([((y - p)[cl == g][:, None] * Z[cl == g]).sum(0) for g in np.unique(cl)])
    G = len(S)
    V = np.linalg.inv(H) @ (S.T @ S * G / (G - 1)) @ np.linalg.inv(H)
    assert np.allclose(fit.cov, V, rtol=1e-3, atol=1e-6)


def test_two_way_covariance_matches_a_direct_cameron_gelbach_miller_sandwich():
    """Two-way clustering (receiver x sender): meat = receiver meat + sender meat - observation meat (the intersection of the two
    clusterings is one observation when no pair repeats), each one-way meat with its G/(G-1)."""
    rng = np.random.default_rng(4)
    n = 800
    pairs = set()
    while len(pairs) < n:
        pairs.add((int(rng.integers(0, 30)), int(rng.integers(0, 40))))
    pairs = sorted(pairs)
    r = np.array([p[0] for p in pairs])
    snd = np.array([p[1] for p in pairs])
    a, b = rng.normal(size=30), rng.normal(size=40)
    X = rng.normal(size=(n, 2))
    y = (rng.random(n) < special.expit(0.8 * X[:, 0] + a[r] + b[snd])).astype(float)
    fit = sr.fit_logit(X, y, ridge=0.0, cluster=r, cluster2=snd, se=True)
    Z = np.column_stack([np.ones(n), X])
    p = special.expit(Z @ np.r_[fit.intercept, fit.coef])
    H = (Z * (p * (1 - p))[:, None]).T @ Z
    Hi = np.linalg.inv(H)
    R = Z * (y - p)[:, None]

    def meat(cl):
        S = np.array([R[cl == g].sum(0) for g in np.unique(cl)])
        return S.T @ S * (len(S) / (len(S) - 1))

    V = Hi @ (meat(r) + meat(snd) - R.T @ R) @ Hi
    assert np.allclose(fit.cov2, V, rtol=1e-3, atol=1e-6)
    assert np.allclose(fit.cov, Hi @ meat(r) @ Hi, rtol=1e-3, atol=1e-6)
    assert (fit.se2 > 0).all()


def test_pigeonhole_bootstrap_weights_are_the_product_of_the_two_multiplicities():
    r = np.array([0, 0, 1, 1, 2, 2, 2])
    s = np.array([0, 1, 0, 1, 0, 1, 2])
    cb = sr.ClusterBoot(r, 20, seed=2, cluster2=s)
    for b in range(20):
        w = cb.w(b)
        assert np.allclose(w, cb.counts[b][r] * cb.counts2[b][s])
        assert cb.counts[b].sum() == 3 and cb.counts2[b].sum() == 3


def test_auc_equals_its_definition_with_ties_and_weights_are_multiplicities():
    rng = np.random.default_rng(3)
    s = np.round(rng.random(300), 1)                       # many ties
    y = (rng.random(300) < s).astype(float)
    pos, neg = s[y == 1], s[y == 0]
    brute = np.mean(pos[:, None] > neg[None, :]) + 0.5 * np.mean(pos[:, None] == neg[None, :])
    assert math.isclose(sr.auc_score(y, s), brute, rel_tol=1e-12)
    sc = sr.WeightedScorer(y, s)
    assert math.isclose(sc.auc(), brute, rel_tol=1e-12)
    w = rng.integers(0, 4, 300).astype(float)
    rep = np.repeat(np.arange(300), w.astype(int))
    assert math.isclose(sc.auc(w), sr.auc_score(y[rep], s[rep]), rel_tol=1e-12)
    assert math.isclose(sc.logloss(w), sr.logloss(y[rep], s[rep]), rel_tol=1e-9)


def test_balanced_accuracy():
    y = np.array([1, 1, 1, 1, 0, 0])
    p = np.array([.9, .8, .4, .6, .3, .7])
    assert math.isclose(sr.balanced_accuracy(y, p, 0.5), 0.5 * (3 / 4 + 1 / 2))


def test_cluster_bootstrap_resamples_whole_clusters_and_is_seeded():
    cl = np.repeat(np.arange(10), [3, 5, 1, 2, 4, 6, 1, 1, 2, 5])
    b1, b2 = sr.ClusterBoot(cl, 50, seed=1), sr.ClusterBoot(cl, 50, seed=1)
    assert np.array_equal(b1.counts, b2.counts) and (b1.counts.sum(1) == 10).all()
    w = b1.w(3)
    assert len(w) == len(cl) and all(len(set(w[cl == g])) == 1 for g in range(10))


def test_aligned_index_never_splits_a_timestamp_and_folds_are_chronological():
    t = np.repeat(np.arange(20.0), 5)
    for f in (0.3, 0.41, 0.55, 0.7, 0.85):
        i = sr.aligned_index(t, f)
        assert i == len(t) or t[i] != t[i - 1]
    assert sr.aligned_index(t, 1.0) == len(t)
    b = sr.fold_bounds(t)
    assert b == sorted(b) and b[-1] == len(t)


def test_forward_chained_predictions_never_use_later_labels():
    """Poison every label from the start of the third test block on (and recompute the causal features): predictions in the
    first two test blocks are identical, because their features come from earlier edges and their fits from earlier labels."""
    E = sr.EdgeSet(*[getattr(skeleton(n=500, m=8000, seed=11), a) for a in ("name", "u", "v", "s", "t", "cluster", "n_nodes",
                                                                            "info")])
    eta = person_eta(E)
    E = sr.simulate_signs(E, eta, sr.planted_coef(0.3), seed=1)
    bounds = sr.fold_bounds(E.t)
    cut = bounds[2]
    s2 = E.s.copy()
    rng = np.random.default_rng(0)
    s2[cut:] = np.where(rng.random(E.m - cut) < 0.5, 1, -1)
    E2 = sr.EdgeSet(E.name, E.u, E.v, s2, E.t, E.cluster, E.n_nodes, {})
    r1 = sr.run_spec(E, sr.compute_features(E, "causal"), "x", ("person", "tri16"))
    r2 = sr.run_spec(E2, sr.compute_features(E2, "causal"), "x", ("person", "tri16"))
    early = (r1.fold_of >= 0) & (r1.fold_of <= 1)
    assert early.sum() > 1000 and np.allclose(r1.pred[early], r2.pred[early])
    assert not np.allclose(r1.pred[r1.fold_of == 3], r2.pred[r2.fold_of == 3])       # the poisoned block does differ


def test_run_spec_refuses_static_features():
    E = toy_edges()
    with pytest.raises(ValueError):
        sr.run_spec(E, sr.compute_features(E, "static"), "x", ("person",))


def test_dersimonian_laird():
    h = sr.dersimonian_laird([0.0, 1.0], [1.0, 1.0])
    assert math.isclose(h["Q"], 0.5) and math.isclose(h["p"], stats.chi2.sf(0.5, 1)) and h["I2"] == 0.0
    h = sr.dersimonian_laird([0.0, 5.0, 10.0], [0.1, 0.1, 0.1])
    assert h["I2"] > 0.99 and h["p"] < 1e-10 and h["tau"] > 4


def test_anova_icc():
    g = np.repeat(np.arange(50), 6)
    same = (np.arange(50) % 2)[g].astype(float)
    assert sr.anova_icc(g, same) > 0.99
    rng = np.random.default_rng(0)
    assert abs(sr.anova_icc(g, (rng.random(300) < 0.5).astype(float))) < 0.08


def test_make_bins_merges_small_years_into_neighbours():
    years = np.repeat([2003, 2004, 2005, 2006], [150, 4000, 5000, 3200])
    t = np.array([np.datetime64(f"{y}-06-15", "s").astype("int64") for y in years], float)
    E = sr.EdgeSet("x", np.zeros(len(t), np.int32), np.zeros(len(t), np.int32), np.ones(len(t), np.int8), t,
                   np.zeros(len(t), np.int32), 1, {})
    b = sr.make_bins(E, "year", 3000)
    assert list(np.unique(b)) == [0, 1, 2] and (b[:4150] == 0).all()               # 2003 joined 2004
    names = sr.bin_names(E, b, "year")
    assert names == ["2003-04", "2005", "2006"]


# ------------------------------------------------------------------------------------------------- (1) machinery: parsers

def test_wikirfa_parser_skips_comments_and_reads_odd_dates():
    text = (b"SRC:Alice\nTGT:Bob\nVOT:1\nRES:1\nYEA:2013\nDAT:23:13, 19 April 2013\nTXT:'''Support''' as co-nom.\n\n"
            b"SRC:Carol\nTGT:Bob\nVOT:-1\nRES:1\nYEA:2013\nDAT:01:04, 20 Jun 2013\nTXT:Oppose\n\n"
            b"SRC:\nTGT:Bob\nVOT:0\nRES:1\nYEA:2013\nDAT:\nTXT:nobody\n\n"
            b"SRC:Dan\nTGT:Bob\nVOT:1\nRES:1\nYEA:2013\nDAT:12:00, 3 Julu 2013\nTXT:x\n")
    d = sr.parse_wikirfa_lines(text.splitlines(keepends=True))
    assert list(d["vot"]) == [1, -1, 0, 1] and d["n_names"] == 4                      # Alice, Bob, Carol, Dan
    assert d["src"][2] == -1                                                          # empty voter field
    assert d["t"][0] == float(np.datetime64("2013-04-19T23:13", "s").astype("int64"))
    assert d["t"][1] == float(np.datetime64("2013-06-20T01:04", "s").astype("int64"))
    assert np.isnan(d["t"][2])
    assert d["t"][3] == float(np.datetime64("2013-07-03T12:00", "s").astype("int64"))     # 'Julu' read as July


def test_parse_dat_rejects_impossible_times():
    assert np.isnan(sr.parse_dat("31:29, 24 May 2008"))      # the one record in the file with hour 31
    assert np.isnan(sr.parse_dat("")) and np.isnan(sr.parse_dat("garbage"))
    assert sr.parse_dat("00:00, 1 January 1970") == 0.0
    assert sr.parse_dat("00:01, 1 Janry 1970") == 60.0
    assert sr.parse_dat("00:00, 1 Mya 1970") == float(np.datetime64("1970-05-01", "s").astype("int64"))


def test_election_ids_split_on_long_gaps():
    day = 86400.0
    tgt = np.array([1, 1, 1, 1, 2, 2])
    res = np.array([-1, -1, -1, -1, 1, 1])
    t = np.array([0, 2, 4, 40, 1, 3]) * day
    ids = sr.assign_elections(tgt, res, t)
    assert ids[0] == ids[1] == ids[2] != ids[3] and ids[4] == ids[5] and len(set(ids)) == 3


def test_gexf_edge_stream_and_iso_times():
    xml = (b'<?xml version="1.0"?><gexf xmlns="http://www.gexf.net/1.2draft"><graph><nodes/><edges>'
           b'<edge source="1" target="2" id="0"><attvalues><attvalue for="0" value="-1" />'
           b'<attvalue for="1" value="2023-09-11T02:37:47.141Z" /></attvalues></edge>'
           b'<edge source="2" target="3" id="1"><attvalues><attvalue for="0" value="1" />'
           b'<attvalue for="1" value="2023-07-24T15:06:06.183Z" /></attvalues></edge></edges></graph></gexf>')
    import io
    rows = list(sr.parse_gexf_edges(io.BytesIO(xml)))
    assert rows == [(1, 2, -1, "2023-09-11T02:37:47.141Z"), (2, 3, 1, "2023-07-24T15:06:06.183Z")]
    assert math.isclose(sr._iso_seconds("1970-01-01T00:00:01.500Z"), 1.5)


# ------------------------------------------------------------------------------------------------- (1) machinery: T4, T5

def _edgeset(rows, n=None):
    u = np.array([r[0] for r in rows])
    v = np.array([r[1] for r in rows])
    s = np.array([r[2] for r in rows])
    t = np.array([r[3] for r in rows], float)
    n = n or int(max(u.max(), v.max()) + 1)
    return sr._sorted_edgeset("c", u, v, s, t, v.copy(), n, {})


def test_symmetry_counts_on_a_constructed_network():
    """Five reciprocated pairs: (++), (++), (--), (+-), (-+) -> 2 of 5 opposite; the reply after a '+' is '+' in 3 of 4."""
    rows = []
    sign_pairs = [(1, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for k, (a, b) in enumerate(sign_pairs):
        rows += [(2 * k, 2 * k + 1, a, 100 * k + 1), (2 * k + 1, 2 * k, b, 100 * k + 2)]
    rows += [(0, 3, 1, 1000), (4, 7, -1, 1001)]                                 # unreciprocated ties
    E = _edgeset(rows)
    F = sr.compute_features(E, "static")
    res = sr.symmetry_test(E, F, B=20)
    assert res["n_pairs"] == 5 and res["opposite"] == 2 and math.isclose(res["share"], 0.4)
    assert res["reply"]["after +"]["n"] == 3 and math.isclose(res["reply"]["after +"]["p_pos"], 2 / 3)
    assert res["reply"]["after -"]["n"] == 2 and math.isclose(res["reply"]["after -"]["p_pos"], 0.5)
    lo, hi = sr.wilson(2, 5)
    assert lo < 0.4 < hi


def test_wilson_interval_known_value():
    lo, hi = sr.wilson(50, 100)
    assert math.isclose(lo, 0.4038, abs_tol=2e-4) and math.isclose(hi, 0.5962, abs_tol=2e-4)


def test_visibility_baselines_are_the_majorities_of_the_other_ties():
    """OutSign predicts '+' iff the sender's other outgoing ties are at least as often '+'; InSign likewise for the target's
    incoming ties [L4802].  Static mode excludes the edge itself."""
    rows = [(0, 10, 1, 1), (0, 11, 1, 2), (0, 12, -1, 3),          # sender 0: + + -
            (1, 10, 1, 4), (2, 10, 1, 5), (3, 10, -1, 6)]          # target 10: + + + -
    E = _edgeset(rows)
    F = sr.compute_features(E, "static")
    k = int(np.flatnonzero((E.u == 0) & (E.v == 12))[0])             # the '-' tie of sender 0: others are ++ -> predict '+'
    assert F.op[k] == 2 and F.on[k] == 0 and (F.op >= F.on)[k]
    k = int(np.flatnonzero((E.u == 3) & (E.v == 10))[0])             # the '-' tie into 10: others are +++ -> predict '+'
    assert F.ip[k] == 3 and F.inn[k] == 0


# ------------------------------------------------------------------------------------------------- (1) machinery: simulation

def test_planted_simulation_draws_use_exactly_the_causal_counts():
    """The sign of each simulated edge is Bernoulli(sigmoid(eta + c . causal triad counts of the simulated past)): rebuild
    the probability from compute_features on the simulated set and the same uniform draws."""
    E = skeleton(n=200, m=2500, seed=1)
    eta = person_eta(E, seed=2)
    c = sr.planted_coef(0.4)
    c[sr.TYPE_INDEX["BFpp"]] = 0.2
    Es = sr.simulate_signs(E, eta, c, seed=9)
    F = sr.compute_features(Es, "causal")
    z = eta + F.tri.astype(float) @ c
    draws = np.random.default_rng(9).random(E.m)
    assert np.array_equal(Es.s, np.where(draws < special.expit(z), 1, -1))


def test_null_simulation_is_independent_draws_from_eta():
    E = skeleton(n=300, m=4000, seed=2)
    eta = person_eta(E, seed=3)
    Es = sr.simulate_signs(E, eta, None, seed=4)
    draws = np.random.default_rng(4).random(E.m)
    assert np.array_equal(Es.s, np.where(draws < special.expit(eta), 1, -1))
    assert np.array_equal(Es.u, E.u) and np.array_equal(Es.t, E.t)


@pytest.fixture(scope="module")
def synthetic_worlds():
    """A network skeleton with triads, and three sign worlds on it: person terms only, a planted weak mechanism, a planted
    strong one (forward-chain, per-triad log-odds 0.15 and 0.5)."""
    E = skeleton(n=1200, m=26000, seed=3)
    eta = person_eta(E, seed=5, sd_send=1.0, sd_recv=1.0, base=1.5)
    worlds = {}
    for name, scale in (("null", 0.0), ("weak", 0.15), ("strong", 0.5)):
        Es = sr.simulate_signs(E, eta, sr.planted_coef(scale) if scale else None, seed=21)
        Fc = sr.compute_features(Es, "causal")
        Fs = sr.compute_features(Es, "static")
        worlds[name] = (Es, Fc, Fs)
    return worlds


def test_person_effects_alone_produce_the_forward_chain_pattern_in_the_triad_only_fit(synthetic_worlds):
    """The central confound.  Signs generated from sender and receiver propensities ONLY still give FFpm, FFmp and FFmm
    negative (and FFpp positive) when the 16 types are fitted without person terms, because a triad counts a sender's
    negativity and a receiver's unpopularity; with person terms in the fit the pattern is gone.  (LHK's Table 2 fit has no
    person terms [L4811, L4833].)"""
    Es, Fc, Fs = synthetic_worlds["null"]
    bare = sr.coefficient_table(Es, Fs, ("tri16",))["rows"]
    ctrl = sr.coefficient_table(Es, Fs, ("person", "tri16"))["rows"]
    for nm, sign in sr.FORWARD_SIGN.items():
        assert sign * bare[nm]["z"] > 1.96, (nm, bare[nm])                    # looks like a mechanism
    assert abs(ctrl["FFmm"]["coef"]) < 0.1 and abs(ctrl["FFpm"]["coef"]) < 0.1 and abs(ctrl["FFpp"]["coef"]) < 0.1


def test_a_planted_mechanism_is_recovered_with_person_terms_in_the_fit(synthetic_worlds):
    """Power check of T1: a forward-chain mechanism of 0.5 per triad is recovered (right signs, right size to within a third)
    by the person-adjusted fit in the causal design."""
    Es, Fc, Fs = synthetic_worlds["strong"]
    rows = sr.coefficient_table(Es, Fc, ("person", "tri16"))["rows"]
    for nm, sign in sr.FORWARD_SIGN.items():
        assert rows[nm]["status"] == "SUPPORTED", (nm, rows[nm])
        assert abs(rows[nm]["coef"] - sign * 0.5) < 0.17, (nm, rows[nm]["coef"])


def test_planted_mechanism_raises_the_held_out_gain_of_triad_terms(synthetic_worlds):
    """Power check of T2: G (AUC of person + triad minus person) is about zero or below in the person-only world and clearly
    positive, with its interval above 0, when a mechanism is planted; D (person minus triad) stays positive."""
    g = {}
    for name, (Es, Fc, Fs) in synthetic_worlds.items():
        res = sr.run_specs(Es, Fc, ["person", "tri16", "person+tri16"])
        g[name] = sr.paired_diff(Es, res, "person+tri16", "person", B=100)
        assert sr.paired_diff(Es, res, "person", "tri16", B=100)["ci"][0] > 0
    assert g["null"]["diff"] < 0.004 and g["null"]["ci"][0] < 0.004
    assert g["strong"]["ci"][0] > 0 and g["strong"]["diff"] > g["weak"]["diff"] > g["null"]["diff"] - 0.002
    assert g["strong"]["diff"] > 0.01


def test_replicate_statistics_has_the_pieces_the_report_reads():
    E = skeleton(n=300, m=5000, seed=4)
    eta = person_eta(E, seed=1)
    rep = sr.replicate_statistics(sr.simulate_signs(E, eta, None, seed=1))
    assert set(rep["auc"]) == {"person", "tri16", "person+tri16"} and "G" in rep and "D" in rep
    assert set(rep["coef"]) == {"causal:tri16", "causal:person+tri16", "static:tri16", "static:person+tri16"}
    assert set(rep["coef"]["static:tri16"]) == set(sr.FORWARD)


def test_calibration_picks_a_ridge_that_matches_the_target_auc():
    E = skeleton(n=300, m=5000, seed=5)
    eta0 = person_eta(E, seed=2, sd_send=1.0, sd_recv=1.0)
    real = sr.simulate_signs(E, eta0, None, seed=3)
    res = sr.run_spec(real, sr.compute_features(real, "causal"), "p", ("person",))
    idx = np.flatnonzero(sr.test_window(res))
    target = sr.WeightedScorer(real.y[idx], res.pred[idx]).auc()
    cal = sr.calibrate_generator(real, target, grid=(0.03, 0.3, 3.0))
    assert 0.01 <= cal["lam"] <= 5.0 and cal["eta"].shape == (real.m,)
    assert len(cal["grid"]) == 3


# ------------------------------------------------------------------------------------------------- (2) data integrity

@pytest.mark.parametrize("key", SITES)
def test_source_file_matches_the_recorded_size_and_checksum(key):
    src = sr.SOURCES[key]
    assert src.path.stat().st_size == src.nbytes
    assert sr.sha256_of(src.path) == src.sha256


@needs("otc")
@needs("alpha")
@pytest.mark.parametrize("key,rows,pos,pairs,tri,both", [("otc", 35592, 32029, 21492, 33493, 358),
                                                         ("alpha", 24186, 22650, 14124, 22153, 248)])
def test_bitcoin_counts_reproduce_file_117(key, rows, pos, pairs, tri, both):
    """117 section 3.4 [L4568, L4570, L4571, L4572]: ratings, positives, no ordered pair rated twice, undirected pairs,
    triangles, and pairs whose two directions carry opposite signs."""
    from scipy import sparse
    E = sr.load_site(key)
    assert E.m == rows and int((E.s > 0).sum()) == pos
    assert len(set(zip(E.u.tolist(), E.v.tolist()))) == E.m                  # no re-rating
    n = E.n_nodes
    A = sparse.coo_matrix((np.ones(E.m), (E.u, E.v)), shape=(n, n)).tocsr()
    U = ((A + A.T) > 0).astype(float)
    U.setdiag(0)
    U.eliminate_zeros()
    assert U.nnz // 2 == pairs
    assert int(round((U @ U).multiply(U).sum() / 6)) == tri
    rp = sr.reciprocated_pairs(E)
    assert int((E.s[rp["i"]] != E.s[rp["j"]]).sum()) == both


@needs("wiki")
def test_wikirfa_counts_reproduce_file_117():
    """117 section 3.3 [L4562]: 198,275 votes, 144,451 support, 41,176 oppose, 12,648 neutral; 1,661 empty voters; the file
    has 9,367 undated votes (counted here) and one impossible time (hour 31)."""
    import gzip
    with gzip.open(sr.SOURCES["wiki"].path, "rb") as f:
        d = sr.parse_wikirfa_lines(f)
    assert len(d["vot"]) == 198275
    assert int((d["vot"] == 1).sum()) == 144451 and int((d["vot"] == -1).sum()) == 41176 and int((d["vot"] == 0).sum()) == 12648
    assert int((d["src"] < 0).sum()) == 1661
    assert int(np.isnan(d["t"]).sum()) == 9367 + 1             # 9,367 empty DAT fields + the one record with hour 31
    E = sr.load_wikirfa()
    assert len(np.unique(E.cluster)) == E.info["n_elections"] and E.info["n_dated"] == 177181
    assert len(set(zip(E.u.tolist(), E.v.tolist()))) == E.m                  # first dated vote of each ordered pair


@needs("bsky")
def test_bluesky_creator_graph_reproduces_file_117():
    """117 section 3.6 [L4595]: 273,696 follow and 24,362 block edges (8.2% negative); self-loops are dropped (24)."""
    E = sr.load_bluesky()
    assert E.info["n_rows"] == 298058 and E.m + 24 == 298058
    assert 24338 <= int((E.s < 0).sum()) <= 24362 and 0.081 < (E.s < 0).mean() < 0.083
    assert len(set(zip(E.u.tolist(), E.v.tolist()))) == E.m
    assert E.t.min() >= float(np.datetime64("2023-05-11T00:00", "s").astype("int64"))
    assert E.t.max() <= float(np.datetime64("2024-05-12T00:00", "s").astype("int64"))


@needs("alpha")
def test_real_causal_features_ignore_the_future():
    """The no-leakage identity on real data: the causal features of sampled Alpha edges are those of a run on the edges
    that are not later than them."""
    E = sr.load_site("alpha")
    F = sr.compute_features(E, "causal")
    rng = np.random.default_rng(0)
    for k in rng.choice(E.m, 12, replace=False):
        pre = np.flatnonzero(E.t <= E.t[k])
        Fp = sr.compute_features(E.take(pre), "causal", query=(pre == k))
        row = int(np.flatnonzero(pre == k)[0])
        assert np.array_equal(F.tri[k], Fp.tri[row]) and F.op[k] == Fp.op[row] and F.inn[k] == Fp.inn[row]


# ------------------------------------------------------------------------------------------------- (3) the registry's predictions

_STATE: dict = {}


def state(key):
    if key not in _STATE:
        E = sr.load_site(key)
        _STATE[key] = dict(E=E, Fs=sr.compute_features(E, "static"), Fc=sr.compute_features(E, "causal"))
    return _STATE[key]


def memo(key, name, fn):
    st = state(key)
    if name not in st:
        st[name] = fn(st)
    return st[name]


def t1(key, mode, blocks):
    return memo(key, f"t1:{mode}:{'+'.join(blocks)}",
                lambda st: sr.coefficient_table(st["E"], st["Fs" if mode == "static" else "Fc"], blocks))


def t2(key):
    def f(st):
        res = sr.run_specs(st["E"], st["Fc"], ["person", "tri16", "person+tri16"])
        return dict(res=res, D=sr.paired_diff(st["E"], res, "person", "tri16", B=100),
                    G=sr.paired_diff(st["E"], res, "person+tri16", "person", B=100),
                    G5=sr.paired_diff(st["E"], res, "person+tri16", "person", mask=st["Fc"].emb >= 5, B=100))
    return memo(key, "t2", f)


def t3(key, person=False):
    cfg = sr.BIN_CFG[key]
    return memo(key, f"t3:{person}", lambda st: sr.drift_by_bin(st["E"], cfg[0], cfg[1], "snapshot", st["Fc"], person))


def t4(key):
    return memo(key, "t4", lambda st: sr.symmetry_test(st["E"], st["Fs"], B=50))


def t5(key):
    return memo(key, "t5", lambda st: sr.visibility_test(st["E"], st["Fs"], B=100))


def refuted(table: dict):
    """Parametrisation of the four sites in which the sites named in `table` are known findings (strict xfail with the
    measured reason), so that a change of data or code that flips one is noticed."""
    out = []
    for k in sr.SITE_ORDER:
        marks = [needs(k)]
        if k in table:
            marks.append(pytest.mark.xfail(strict=True, reason=table[k]))
        out.append(pytest.param(k, marks=marks, id=k))
    return out


# ---- T1: form transfer (112 section 6.5 item 1) ----------------------------------------------------------------------

# Findings, 2026-11-01 (measured values in the reasons; strict xfail, so a change that flips one is noticed).
FFMM_ALONE = {
    "otc": "FFmm = -0.185, z = -1.8 (-1.7 two-way): UNDECIDED in the 16-type fit alone at Bitcoin OTC",
}
FOUR_CHAINS_ALONE = {
    "otc": "FFpp = +0.044 (z 0.5) and FFmm = -0.185 (z -1.8) are UNDECIDED at Bitcoin OTC",
    "alpha": "FFpp = +0.044 (z +0.5) is UNDECIDED at Bitcoin Alpha (94% of ratings are positive; a positive chain says little)",
}
FFMM_WITH_PERSON = {
    "wiki": "FFmm = +0.013 (z +0.8) with person terms in the fit: UNDECIDED at wiki-RfA",
    "otc": "FFmm = +0.023 (z +0.3) with person terms in the fit: UNDECIDED at Bitcoin OTC",
    "alpha": "FFmm = -0.059 (z -0.3) with person terms in the fit: UNDECIDED at Bitcoin Alpha",
    "bsky": "FFmm = +0.109 (z +3.4, +2.7 two-way) with person terms in the fit: CONTRADICTED (positive) at BlueTempNet",
}


@pytest.mark.parametrize("key", refuted(FFMM_ALONE))
def test_t1_ffmm_is_negative_in_the_16_type_fit_alone(key):
    """112 section 6.5 item 1 and L4833: FFmm (u negative to w, w negative to v) has a negative coefficient; R1 SUPPORTED means
    z < -1.96 with at least 100 supporting edges (static evidence, LHK's design, clusters = receivers)."""
    r = t1(key, "static", ("tri16",))["rows"]["FFmm"]
    assert r["status"] == "SUPPORTED", r


@pytest.mark.parametrize("key", SITES)
def test_t1_no_forward_chain_is_contradicted_in_the_16_type_fit_alone(key):
    """'refuted if mm > 0 with adequate support': in the 16-type fit alone no forward chain has the wrong sign with z beyond
    1.96, in either evidence design."""
    for mode in ("static", "causal"):
        rows = t1(key, mode, ("tri16",))["rows"]
        assert all(rows[n]["status"] != "CONTRADICTED" for n in sr.FORWARD), (mode, {n: rows[n]["coef"] for n in sr.FORWARD})


@pytest.mark.parametrize("key", refuted(FOUR_CHAINS_ALONE))
def test_t1_the_whole_forward_chain_pattern_is_supported_in_the_16_type_fit_alone(key):
    rows = t1(key, "static", ("tri16",))["rows"]
    assert all(rows[n]["status"] == "SUPPORTED" for n in sr.FORWARD), {n: (rows[n]["coef"], rows[n]["z"]) for n in sr.FORWARD}


@pytest.mark.parametrize("key", refuted(FFMM_WITH_PERSON))
def test_t1_ffmm_survives_person_terms_in_the_fit(key):
    """R-E as the registry writes it has a_i + b_j in z: with person terms in the fit FFmm < 0 should still be SUPPORTED."""
    r = t1(key, "static", ("person", "tri16"))["rows"]["FFmm"]
    assert r["status"] == "SUPPORTED", r


@pytest.mark.parametrize("key", SITES)
def test_t1_ffmm_is_never_supported_once_person_terms_are_in_the_fit(key):
    """The measured fact behind the xfails above: in the static and the causal design, with the eight person columns, FFmm is
    not SUPPORTED at any site (it is within a few hundredths of zero or positive)."""
    for mode in ("static", "causal"):
        r = t1(key, mode, ("person", "tri16"))["rows"]["FFmm"]
        assert r["status"] != "SUPPORTED", (mode, r)


# ---- T2: person terms against triad terms (item 2) -------------------------------------------------------------------

@pytest.mark.parametrize("key", SITES)
def test_t2_person_terms_carry_more_than_triad_terms(key):
    """Prediction: held-out AUC from person terms alone exceeds that from the 16 triad counts alone, with the interval of the
    difference above 0 (time-split, causal features)."""
    D = t2(key)["D"]
    assert D["diff"] > 0.04 and D["ci"][0] > 0, D


@pytest.mark.parametrize("key", SITES)
def test_t2_triad_terms_add_no_material_mechanism_beyond_person_terms(key):
    """R2: G = AUC(person + triad) - AUC(person) is below the pre-registered 0.02 at every site (it is within ~0.01 either
    way), so the registry's triad terms are not a 'material' mechanism beyond person propensities on this protocol."""
    G = t2(key)["G"]
    assert G["diff"] < sr.RULE_G_MATERIAL and sr.r2_tier(G) != "material", G


def test_t2_r2_verdict_across_the_four_sites_is_no():
    tiers = [sr.r2_tier(t2(k)["G"]) for k in sr.SITE_ORDER if sr.available(k)]
    if len(tiers) < 4:
        pytest.skip("needs all four sources")
    assert sr.r2_overall(tiers) == "NO", tiers


# ---- T3: drift by date (item 3) ------------------------------------------------------------------------------------------

@pytest.mark.parametrize("key", SITES)
def test_t3_forward_chain_signs_do_not_flip_with_date_in_the_16_type_fit_alone(key):
    """R3: no forward-chain type is CONTRADICTED (adequate support, z beyond 1.96 on the wrong side) in two or more date bins."""
    v = t3(key)["verdict"]
    assert not v["refuted"], v


@pytest.mark.parametrize("key", SITES)
def test_t3_intercepts_move_with_date(key):
    """The moderator reading predicts that intercepts move while the pattern holds: Q p < 0.001 and a range of at least
    0.5 logit across date bins."""
    v = t3(key)["verdict"]
    assert v["intercepts_move"], v


# ---- T4: symmetry (item 4) ---------------------------------------------------------------------------------------------

RARE = {"wiki": "14.6% [13.7%, 15.5%] of reciprocated wiki-RfA pairs have opposite signs (R4 'rare' is 10% or less); the pairs are "
                "two votes in two elections, not replies"}


@pytest.mark.parametrize("key", refuted(RARE))
def test_t4_opposite_sign_reciprocation_is_rare(key):
    """LHK call reciprocated opposite signs rare; R4 makes that 10% or less of reciprocated pairs."""
    t = t4(key)
    assert t["share"] <= sr.RULE_RARE, (t["share"], t["ci"])


@pytest.mark.parametrize("key", SITES)
def test_t4_reciprocated_ties_are_concordant_beyond_person_terms(key):
    """The two ties of a reciprocated pair have positively correlated residuals from the sender-and-receiver model, with the
    interval above 0: signs are more alike within a pair than person propensities make them."""
    t = t4(key)
    assert t["resid_corr_ci"][0] > 0, t["resid_corr_ci"]


# ---- T5: visibility (item 5) --------------------------------------------------------------------------------------------

GAP = {
    "otc": "gap at C = 0 is -0.020 [-0.046, +0.004] at Bitcoin OTC: ABSENT on the receiver-cluster rule, UNDECIDED two-way "
           "[-0.14, +0.11], so UNDECIDED in the verdict (R5)",
    "alpha": "gap at C = 0 is -0.001 [-0.030, +0.048] at Bitcoin Alpha: UNDECIDED (R5)",
    "bsky": "gap at C = 0 is -0.060 [-0.094, -0.030] at BlueTempNet: OutSign beats InSign, ABSENT (R5)",
}


@pytest.mark.parametrize("key", refuted(GAP))
def test_t5_target_majority_beats_own_history_at_low_embeddedness(key):
    """R5 SUPPORTED: lower bound of BA(InSign) - BA(OutSign) at C = 0 above 0.02 (static evidence, as LHK)."""
    t = t5(key)
    assert t["verdict"] == "SUPPORTED", (t["verdict"], t["strata"]["C = 0"]["gap"], t["strata"]["C = 0"]["gap_ci"])


@needs("wiki")
def test_t5_gap_vanishes_with_embeddedness_on_wiki_rfa_as_in_lhk():
    """LHK (L4851): InSign beats OutSign at C >= 0 (0.706 against 0.576) and the two are level at C >= 25 (0.578 against
    0.572).  On wiki-RfA the gap at C = 0 is large and at C >= 25 within a few hundredths."""
    t = t5("wiki")
    assert t["strata"]["C = 0"]["gap"] > 0.10 and abs(t["strata"]["C >= 25"]["gap"]) < 0.03


@needs("otc")
def test_t5_bitcoin_otc_is_absent_on_one_rule_only():
    """Review 2026-11-01, the measured fact behind the verdict's 'undecided' at Bitcoin OTC: R5 is ABSENT with receiver clusters
    and UNDECIDED with receiver-and-sender clusters, and the verdict needs both to agree."""
    one = t5("otc")
    two = memo("otc", "t5_2", lambda st: sr.visibility_test(st["E"], st["Fs"], B=100, twoway=True))
    assert one["verdict"] == "ABSENT" and two["verdict"] == "UNDECIDED"
    assert sr.r5_both(one["verdict"], two["verdict"]) == "UNDECIDED"


# ---- the report -------------------------------------------------------------------------------------------------------------

@pytest.mark.skipif(not all(sr.cache_path(k).exists() for k in sr.SITE_ORDER),
                    reason="statistics not cached: cd sim && for s in wiki otc alpha bsky; do ~/.local/bin/uv run python "
                           "-m models.sign_registry_battery compute $s; done")
def test_report_is_regenerated_from_the_cached_statistics(tmp_path):
    out = tmp_path / "r.md"
    sr.write_report(out)
    text = out.read_text()
    for head in ("## Verdict", "## 1. Data and terms", "## 3. T1", "## 4. T2", "## 5. T3", "## 6. T4", "## 7. T5",
                 "## 8. Variations", "## 9. The null", "## 10. Caveats", "## 11. Reproduce"):
        assert head in text, head
    assert "nan" not in text.lower().replace("financ", "")        # no unformatted missing value leaked into a table
