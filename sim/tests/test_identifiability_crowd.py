"""Identifiability of the crowd law from aggregate curves, on independent synthetic crowds.

Module: models/identifiability_crowd.py.  Results and verdict: sim/results/identifiability_crowd.md (produced
by models/identifiability_crowd_report.py from the same functions).  Prior work: docs/prior-work/094 (SBC, recovery, misspecification),
089 (what the event datasets record), models/00-v0.md 4.4 and 6.3 (the crowd law), models/02-our-claims.md
Claim 1 (the group state is the threshold distribution; ignition).  Ledger ids cited below are in
`identifiability_crowd.LEDGER` and are checked against docs/ledger.jsonl by the last test.

No data are used and none are needed (sim/data/README.md is not touched): every crowd is simulated.

Four groups.  (A) The law and the engines that read it: the exact path law sums to one and matches the
simulator; the lattice and synthetic engines agree with it where they should.  (B) Structure, as exact
constructions: what a noise-free curve fixes and what it cannot (the claims behind the verdict).  (C) The
statistics: the monotone-order test, the non-parametric posterior, simulation-based calibration (SBC) of the
engines, including a check that SBC itself detects a wrong posterior and that the synthetic engine is NOT valid
where the results file says so.  (D) Small versions of the headline findings.  Seeds are fixed; Monte Carlo
assertions have wide margins, and a failure is a finding.
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pytest
from scipy import stats

from models import identifiability_crowd as ic
from models import identifiability_crowd_report as rep

ROOT = Path(__file__).resolve().parents[2]
CLIP = ic.FAMILIES["clipnorm"]
BETA = ic.FAMILIES["beta"]


# ------------------------------------------------------------------ (A) the law and its engines

@pytest.mark.parametrize("fam,p", [("clipnorm", [0.3, 0.2]), ("beta", [0.1, 1.5, 3.0])])
def test_exact_path_law_sums_to_one(fam, p):
    """Claim (derived in the module docstring; v0.1 6.3, L1201, L1831): the sequential-binomial law of the integer
    path k_0..k_T is a probability distribution.  Enumerate every path for n = 4 and T = 5."""
    n = 4
    Ftab = ic.FAMILIES[fam].table(np.array([p]), np.arange(n + 1) / n)[0]
    paths = ic.enumerate_paths(n, Ftab, 5)
    assert sum(paths.values()) == pytest.approx(1.0, abs=1e-12)


def test_exact_path_law_matches_the_simulator():
    """The same law against 60,000 simulated crowds (n = 5): chi-square over the paths with expected count >= 20,
    and no simulated path outside the enumeration.  Tests the simulator and the law against each other."""
    n, T = 5, 5
    p = np.array([0.3, 0.2])
    paths = ic.enumerate_paths(n, CLIP.table(p[None], np.arange(n + 1) / n)[0], T)
    rng = np.random.default_rng(1)
    N = 60_000
    counts = {}
    for _ in range(N):
        k = tuple(ic.orbit_counts(CLIP.sample(p, n, rng), T))
        counts[k] = counts.get(k, 0) + 1
    assert set(counts) <= set(paths)
    chi = sum((counts.get(k, 0) - N * q) ** 2 / (N * q) for k, q in paths.items() if N * q >= 20)
    df = sum(1 for q in paths.values() if N * q >= 20) - 1
    assert stats.chi2.sf(chi, df) > 1e-3


def test_orbit_is_the_least_fixed_point():
    """v0.1 Theorem 6.3(i) (L1201, L1235, L3961): from r(0) = F_n(0) the orbit is non-decreasing and ends at the
    least k with #{theta <= k/n} <= k, which `lfp_count` computes without iterating."""
    rng = np.random.default_rng(2)
    for _ in range(300):
        fam = ic.FAMILIES[("beta", "clipnorm", "bimodal", "logitnorm")[int(rng.integers(4))]]
        n = int(rng.integers(5, 80))
        th = fam.sample(fam.draw(rng), n, rng)
        k = ic.orbit_counts(th, n + 2)
        assert (np.diff(k) >= 0).all()
        assert k[-1] == ic.lfp_count(th)


def test_population_stall_reproduces_granovetters_fold():
    """L3962 / L1833: normal thresholds with mean 25 on the 0-100 scale jump from a small equilibrium to nearly
    everyone at sigma_c about 12.2.  The population stall tau of the clipped normal does the same between
    sigma = 0.122 and 0.123 (mean 0.25)."""
    t = ic.tau_of(CLIP.table(np.array([[0.25, 0.122], [0.25, 0.123]]), ic.RGRID))
    assert t[0] < 0.1 and t[1] == 1.0


def test_lattice_engine_equals_the_exact_law_at_tiny_noise():
    """The exact forward algorithm on (k_{t-1}, k_t) reduces to the path law when the noise is far below the
    lattice spacing 1/n: log-lik(y = k/n) = log P(path) + (T+1) log(1/(sigma sqrt(2 pi)))."""
    n, T, sig = 5, 5, 1e-3
    P = np.array([[0.3, 0.2], [0.25, 0.12]])
    Ftab = CLIP.table(P, np.arange(n + 1) / n)
    k = ic.orbit_counts(CLIP.sample(P[0], n, np.random.default_rng(2)), T)
    lhs = ic.ll_lattice(k / n, n, Ftab, sig)
    rhs = ic.path_logprob_exact(k, n, Ftab) + (T + 1) * np.log(1 / (sig * np.sqrt(2 * np.pi)))
    assert lhs == pytest.approx(rhs, abs=1e-6)


def test_lattice_engine_matches_monte_carlo_marginal_likelihood():
    """The exact filter against the average Gaussian density over 40,000 simulated crowds (n = 5, sigma = 0.15), within
    four Monte Carlo standard errors, for two parameter points."""
    n, T, sig = 5, 5, 0.15
    P = np.array([[0.3, 0.2], [0.25, 0.12]])
    y = np.array([0.0, 0.2, 0.4, 0.4, 0.6, 0.4])
    ll = ic.ll_lattice(y, n, CLIP.table(P, np.arange(n + 1) / n), sig)
    rng = np.random.default_rng(3)
    for gi in range(2):
        vals = np.empty(40_000)
        for i in range(len(vals)):
            kk = ic.orbit_counts(CLIP.sample(P[gi], n, rng), T)
            vals[i] = np.exp(-0.5 * ((y - kk / n) / sig) ** 2).prod() / (sig * np.sqrt(2 * np.pi)) ** (T + 1)
        m, se = vals.mean(), vals.std() / np.sqrt(len(vals))
        assert abs(np.exp(ll[gi]) - m) < 4 * se


def test_synthetic_moments_match_the_simulator():
    """The synthetic engine's mean and covariance of the curve are those of the simulator (n = 300, two parameter
    points, 4,000 simulated crowds against 1,500 common-random-number paths): means within 0.01, sds within 20%
    where the sd exceeds 0.02."""
    n, T = 300, 8
    for fam, p in ((CLIP, [0.2, 0.15]), (BETA, [0.08, 1.5, 3.0])):
        P = np.array([p])
        rng = np.random.default_rng(5)
        sim = np.array([ic.orbit_counts(fam.sample(P[0], n, rng), T) / n for _ in range(4000)])
        mu, cov = ic.sl_moments(fam, P, n, [ic.Run(None, T)], 1500, np.random.default_rng(6))
        assert np.abs(mu[0] - sim.mean(0)).max() < 0.01
        sd_sim, sd_sl = sim.std(0), np.sqrt(np.diag(cov[0]))
        big = sd_sim > 0.02
        assert np.all(np.abs(sd_sl[big] / sd_sim[big] - 1) < 0.2)


# ------------------------------------------------------------------ (B) structure: what a curve fixes

def test_curve_fixes_F_only_at_visited_points():
    """Proposition B (module): the noise-free orbit uses #{theta <= e_t} at the visited shares e_t <= r* only, so every
    threshold above the stall r* can be redrawn without changing the curve, for any T.  This is the converse of L1225
    (there no finite moment of F fixes the outcome): the outcome curve cannot fix F above its own stall."""
    rng = np.random.default_rng(4)
    changed = 0
    for _ in range(200):
        fam = ic.FAMILIES[("beta", "clipnorm", "bimodal")[int(rng.integers(3))]]
        th = fam.sample(fam.draw(rng), 60, rng)
        th2 = ic.redraw_above_stall(th, rng)
        assert (ic.orbit_counts(th, 15) == ic.orbit_counts(th2, 15)).all()
        changed += int(not np.array_equal(np.sort(th), np.sort(th2)))
    assert changed > 50  # the redraw really changed the crowds, not just the curve's equality


def test_same_standalone_curve_different_merge_outcome():
    """models/02 Claim 1.4 (and the converse of L1225): two intruders with IDENTICAL, live standalone curves (differing only
    above their own stall) merge with the same host to opposite outcomes, so the parts' curves do not determine ignition."""
    rng = np.random.default_rng(3)
    found = None
    for _ in range(4000):
        a = CLIP.sample(CLIP.draw(rng), 40, rng)
        ka = ic.orbit_counts(a, 12)
        if ka[0] == 0 or ka[-1] > 30:
            continue
        a2 = ic.redraw_above_stall(a, rng)
        h = BETA.sample(BETA.draw(rng), 40, rng)
        if ic.ignites(a, h) != ic.ignites(a2, h):
            found = (a, a2, h)
            break
    assert found is not None
    a, a2, h = found
    assert (ic.orbit_counts(a, 12) == ic.orbit_counts(a2, 12)).all() and ic.orbit_counts(a, 12)[0] > 0
    assert ic.lfp_count(a) == ic.lfp_count(a2)


def test_ignition_is_decided_beyond_the_intruders_stall():
    """models/02 Claim 1.2 (its equal case: equal stalls never ignite) and 1.4 (necessary condition), replicated on 20,000
    random finite pairs from our four generators: in every igniting pair the host stalls strictly above the intruder, and the intruder has
    F_1(M) > M and F_1(M-) >= M at the host's stall M.  Hence the decisive quantity F_1(M) is always evaluated
    above the intruder's own stall, where its standalone curve carries no information (previous test)."""
    rng = np.random.default_rng(3)
    found = 0
    fams = [ic.FAMILIES[f] for f in ("beta", "clipnorm", "bimodal", "logitnorm")]
    for _ in range(20_000):
        t = []
        for _i in range(2):
            fam = fams[int(rng.integers(4))]
            t.append(fam.sample(fam.draw(rng), 40, rng))
        if not ic.ignites(t[0], t[1]):
            continue
        found += 1
        s = [ic.lfp_count(x) / 40 for x in t]
        if s[0] > s[1]:
            t, s = t[::-1], s[::-1]
        M = s[1]
        assert s[0] < M
        assert (t[0] <= M).mean() > M and (t[0] < M).mean() >= M
    assert found > 500


def test_sandwich_upper_end_is_not_fixed_by_the_parts_curves():
    """models/02 Claim 1.2 and 1.11: the merge lies between the smaller stall and the least common pre-fixed point of
    the two parts (checked on every pair), but that upper end reads both F beyond the stalls: redrawing the thresholds
    above each crowd's own stall leaves both curves identical and moves the upper end in a large share of pairs.  The
    refutation test of Claim 1.11 (a merger above the upper end) cannot be set from the parts' curves."""
    rng = np.random.default_rng(12)
    fams = [ic.FAMILIES[f] for f in ("beta", "clipnorm", "bimodal", "logitnorm")]
    n, tot, moved = 150, 0, 0
    for _ in range(1500):
        t = []
        for _i in range(2):
            fam = fams[int(rng.integers(4))]
            t.append(fam.sample(fam.draw(rng), n, rng))
        if any(ic.orbit_counts(x, 12)[0] == 0 or ic.lfp_count(x) >= 0.97 * n for x in t):
            continue
        up = ic.common_prefixed_point(*t)
        km, nm = ic.merged_stall(*t)
        assert min(ic.lfp_count(x) / n for x in t) - 1e-12 <= km / nm <= up + 1e-12
        t2 = [ic.redraw_above_stall(x, rng) for x in t]
        assert all((ic.orbit_counts(a, 12) == ic.orbit_counts(b, 12)).all() for a, b in zip(t, t2))
        tot += 1
        moved += int(ic.common_prefixed_point(*t2) != up)
    assert tot > 200 and moved / tot > 0.3


def test_strictness_and_only_the_intruders_thresholds_above_its_stall_matter():
    """Added at review (2026-11-01).  (i) models/02 Claim 1.2's strictness on finite pairs: unequal stalls merge strictly
    above the smaller.  (ii) Redrawing the HOST (the higher stall, or either part when the stalls are equal) above its own
    stall never changes whether the merge ignites: the merge passes the host's stall M only through thresholds at or
    below M, which the redraw keeps.  So the flips of section 3.1 can only come from a redrawn intruder.  (iii)
    `task_claim14` reports no violation and no flip from a redrawn host."""
    rng = np.random.default_rng(13)
    fams = [ic.FAMILIES[f] for f in ("beta", "clipnorm", "bimodal", "logitnorm")]
    unequal = host_trials = 0
    for _ in range(1500):
        a, b = (fams[int(rng.integers(4))] for _i in range(2))
        t = [a.sample(a.draw(rng), 60, rng), b.sample(b.draw(rng), 60, rng)]
        k = sorted(ic.lfp_count(x) for x in t)
        km, nm = ic.merged_stall(*t)
        if k[0] != k[1]:
            unequal += 1
            assert km * 60 > nm * k[0]
        host = int(ic.lfp_count(t[1]) >= ic.lfp_count(t[0]))
        t2 = list(t)
        t2[host] = ic.redraw_above_stall(t[host], rng)
        host_trials += 1
        assert ic.ignites(*t) == ic.ignites(*t2)
    assert unequal > 1000 and host_trials == 1500
    r = ic.task_claim14(dict(M=2000))
    assert r["equal_bad"] == r["nec_bad"] == r["sand_bad"] == r["strict_bad"] == 0 and r["strict_trials"] > 0
    assert r["flips"] == r["flips_intr"] and r["flip_trials_intr"] < r["flip_trials"]


def test_monotone_curve_cannot_tell_two_sided_from_one_sided():
    """Proposition A (module), v0.1 2.3 and 4.4 (L3959, L4355): whenever a two-sided crowd's curve is non-decreasing, a one-sided crowd built
    from the curve alone reproduces it exactly.  Checked on random two-sided crowds."""
    rng = np.random.default_rng(5)
    checked = 0
    for _ in range(600):
        fam = ic.FAMILIES[("beta", "clipnorm")[int(rng.integers(2))]]
        n = int(rng.integers(20, 200))
        th, tb = ic.draw_two_sided(fam, fam.draw(rng), n, nu=0.2, wbar=0.4, rng=rng)
        k = ic.orbit_two_sided(th, tb, 12)
        if (np.diff(k) < 0).any():
            continue
        checked += 1
        eq = ic.orbit_equivalent_one_sided(k, n)
        assert (ic.orbit_counts(eq, 12) == k).all()
    assert checked > 100


def test_one_sided_curves_never_decline_but_two_sided_ones_can():
    """v0.1 Theorem 6.3(i) (L1201): a one-sided orbit never declines.  A two-sided gate can (L4347, L4348: own turnout no longer
    needed; crackdown probability rising with size).  The decline is therefore the only trace a single curve can carry."""
    rng = np.random.default_rng(6)
    declines_two = declines_one = 0
    for _ in range(300):
        fam = ic.FAMILIES[("beta", "clipnorm")[int(rng.integers(2))]]
        n = 100
        th, tb = ic.draw_two_sided(fam, fam.draw(rng), n, nu=0.4, wbar=0.4, rng=rng)
        declines_two += int((np.diff(ic.orbit_two_sided(th, tb, 10)) < 0).any())
        declines_one += int((np.diff(ic.orbit_counts(th, 10)) < 0).any())
    assert declines_one == 0 and declines_two > 30


def test_ever_joined_curve_never_declines_but_can_plateau_and_grow():
    """The cumulative (ever-joined) count of a two-sided crowd is non-decreasing by construction, so a test for declines
    has no power on it.  Its only trace of the gate is a plateau followed by growth, which a one-sided orbit (absorbed
    at its stall) and the current-share orbit of ANY crowd (a map on the state) never show.  Here with a large
    share of upper-gated members, 100 crowds of 400."""
    rng = np.random.default_rng(7)
    ever_pg = cur_pg = 0
    for _ in range(100):
        fam = ic.FAMILIES[("beta", "clipnorm")[int(rng.integers(2))]]
        th, tb = ic.draw_two_sided(fam, fam.draw(rng), 400, nu=0.6, wbar=0.5, rng=rng)
        k, ever = ic.orbit_two_sided_ever(th, tb, 10)
        assert (np.diff(ever) >= 0).all() and (ever >= k).all()
        ever_pg += ic.plateau_then_growth(ever)
        cur_pg += ic.plateau_then_growth(k)
        assert not ic.plateau_then_growth(ic.orbit_counts(th, 10))
    assert cur_pg == 0 and ever_pg >= 3


def test_counts_do_not_fix_the_denominator():
    """L3980, L3988 (CCC and its kin record counts or order-of-magnitude bins): thresholds as absolute numbers of others
    give the same COUNT curve whatever the pool N, but different SHARES, so the stall share r* = c*/N is
    not identified from counts (the share-of-pool reading of F needs N).  Here N = 100 and N = 400, same thresholds."""
    theta_abs = np.arange(40)  # 40 members with thresholds 0..39 (a full cascade among themselves)
    c = ic.count_orbit(theta_abs, 60)
    assert c[-1] == 40
    for N in (100, 400):
        assert c[-1] / N in (0.4, 0.1)
    assert 40 / 100 != 40 / 400


def test_inertial_variant_is_the_turn_map_at_alpha_one():
    """The inertial variant r_{t+1} = r_t + alpha (F_n(r_t) - r_t) of the Variations section is the turn map at alpha = 1,
    and slower (same stall, more steps) for alpha < 1."""
    rng = np.random.default_rng(8)
    th = CLIP.sample(np.array([0.2, 0.15]), 500, rng)
    k = ic.orbit_counts(th, 10) / 500
    assert np.allclose(ic.orbit_inertial(th, 10, 1.0), k)
    slow = ic.orbit_inertial(th, 60, 0.5)
    assert slow[3] < k[3] and slow[-1] == pytest.approx(k[-1], abs=1e-6)


# ------------------------------------------------------------------ (C) statistics

def _pava(y):
    vals, wts, cnts = [], [], []
    for yi in y:
        vals.append(float(yi)); wts.append(1.0); cnts.append(1)
        while len(vals) > 1 and vals[-2] > vals[-1]:
            w = wts[-2] + wts[-1]
            v = (vals[-2] * wts[-2] + vals[-1] * wts[-1]) / w
            c = cnts[-2] + cnts[-1]
            vals[-2:], wts[-2:], cnts[-2:] = [v], [w], [c]
    return np.repeat(vals, cnts)


def test_isotonic_fit_matches_pava():
    """The min-max isotonic fit used by the likelihood-ratio test equals the pool-adjacent-violators solution."""
    rng = np.random.default_rng(9)
    Y = rng.normal(size=(200, 11)).cumsum(axis=1) * 0.3 + rng.normal(size=(200, 11))
    assert np.abs(ic.isotonic_nondecreasing(Y) - np.array([_pava(y) for y in Y])).max() < 1e-10


def test_monotone_order_test_has_size_below_alpha_and_power_on_a_decline():
    """The flat latent curve is the least favourable null (Robertson, Wright & Dykstra), so a test of size 0.05 under it has size
    <= 0.05 for every non-decreasing curve; and it rejects a decline of eight noise standard deviations (a curve that
    rises to 0.8 and falls to 0 with sigma = 0.1)."""
    rng = np.random.default_rng(10)
    m, sig = 11, 0.1
    cv = ic.flat_null_critical(ic.lrt_stat, m, 0.05)
    for mu in (np.zeros(m), np.linspace(0, 1, m), np.r_[np.zeros(5), 0.5 * np.ones(6)]):
        Z = mu + rng.normal(0, sig, size=(6000, m))
        assert np.mean(ic.lrt_stat(Z, sig) > cv) < 0.065
    mu = np.r_[np.linspace(0, 0.8, 6), np.linspace(0.6, 0.0, 5)]
    Z = mu + rng.normal(0, sig, size=(2000, m))
    assert np.mean(ic.lrt_stat(Z, sig) > cv) > 0.95
    mild = np.r_[np.linspace(0, 0.6, 6), 0.6 - np.linspace(0.05, 0.25, 5)]  # a total decline of 2.5 sigma
    assert np.mean(ic.lrt_stat(mild + rng.normal(0, sig, size=(2000, m)), sig) > cv) < 0.5


def test_dirichlet_posterior_is_calibrated_and_returns_the_prior_above_the_stall():
    """The exact non-parametric (histogram-Dirichlet) posterior from the noise-free orbit: SBC ranks of F at the probe
    shares are uniform, and above the stall the posterior sd stays at (nearly) the prior sd whatever n, while below
    it shrinks with n (module docstring).  Run at n = 30 and n = 2000."""
    rng = np.random.default_rng(11)
    dh = ic.DirichletHistogram()
    idx = [int(round(r * dh.B)) for r in ic.PROBES]
    prior_sd = np.cumsum(dh.prior_samples(4000, rng), axis=1)[:, idx].std(axis=0)
    out = {}
    for n in (30, 2000):
        us, rin, rout, got = [], [], [], 0
        while got < 250:
            p = dh.sample_prior(rng)
            k = dh.crowd_path(p, n, 12, rng)
            if k.max() == 0:
                continue
            got += 1
            cp = np.cumsum(dh.posterior_samples(k, n, 200, rng), axis=1)[:, idx]
            tr = np.cumsum(p)[idx]
            us.append((cp < tr).mean(axis=0) + rng.random(len(idx)) * (cp == tr).mean(axis=0))
            for j, r in enumerate(ic.PROBES):
                (rin if r <= k[-1] / n else rout).append(cp[:, j].std() / prior_sd[j])
        us = np.array(us)
        assert all(stats.kstest(us[:, j], "uniform").pvalue > 1e-3 for j in range(len(idx)))
        out[n] = (np.median(rin), np.median(rout))
    assert out[30][1] > 0.85 and out[2000][1] > 0.85  # above the stall: the prior, at any n
    assert out[2000][0] < 0.5 * out[30][0]  # below it: shrinks with n


def test_sbc_passes_for_the_exact_engine():
    """SBC computation check (094 L4136, L4137, L4140): with the generator equal to the fitted family and the exact
    sequential-binomial likelihood the randomised ranks are uniform for every scored quantity, and so is the joint
    log-likelihood rank (L4156).  n = 30 and 300, clipped normal."""
    for n in (30, 300):
        st = ic.make_setup("clipnorm", n, 0.0, engine="exact")
        s = ic.sbc_summary(ic.sbc_cell(st, 500, np.random.default_rng(21 + n)))
        assert s["min_ks"] > 1e-3 and s["ll_ks"] > 1e-3
        assert 0.84 < s["c90_min"] and s["c90_max"] < 0.96


def test_sbc_detects_a_deliberately_wrong_posterior():
    """The check of the check (094 L4140; Talts et al.): a posterior sharpened by tempering (log-likelihood x 3) is
    over-confident and one flattened (x 0.3) is over-dispersed; SBC must reject both."""
    for temper, worst in ((3.0, "c90_min"), (0.3, "c90_max")):
        st = ic.make_setup("clipnorm", 100, 0.0, engine="exact")
        st.temper = temper
        s = ic.sbc_summary(ic.sbc_cell(st, 500, np.random.default_rng(31)))
        assert s["z90_max"] > 4 and s["min_ks"] < 1e-3
        assert (s[worst] < 0.8) if worst == "c90_min" else (s[worst] > 0.96)


def test_lattice_engine_is_calibrated_at_small_n():
    """SBC of the exact lattice engine with noise (n = 30, sigma = 0.05): uniform ranks.  Small M, so the margins are wide."""
    st = ic.make_setup("clipnorm", 30, 0.05, engine="lattice")
    s = ic.sbc_summary(ic.sbc_cell(st, 120, np.random.default_rng(41)))
    assert s["min_ks"] > 1e-3 and s["ll_ks"] > 1e-3 and s["c90_min"] > 0.75


def test_synthetic_engine_is_usable_at_large_n_and_not_at_small_n_low_noise():
    """The synthetic (Gaussian) engine: usable where the results use it (n = 1000, sigma = 0.03: the central 90% interval
    of every scored quantity covers 0.82-0.97 of the truths; at M = 3000 the coverage is 0.88-0.91, a mild
    over-confidence of one or two points), and NOT valid at n = 100, sigma = 0.01, where counts and noise live on
    the same lattice scale and its joint-likelihood ranks are strongly over-confident (coverage about 0.7).  The results
    file reports the second as a limit of the engine, not as a finding about crowds."""
    ok = ic.sbc_summary(ic.sbc_cell(ic.make_setup("clipnorm", 1000, 0.03, engine="sl", S=2000, seed=1), 1000,
                                    np.random.default_rng(51)))
    bad = ic.sbc_summary(ic.sbc_cell(ic.make_setup("clipnorm", 100, 0.01, engine="sl", S=2000, seed=1), 800,
                                     np.random.default_rng(52)))
    assert 0.82 < ok["c90_min"] and ok["c90_max"] < 0.97 and ok["ll_c90"] > 0.82
    assert bad["ll_c90"] < 0.78 and bad["ll_ks"] < 1e-3
    assert ok["ll_c90"] - bad["ll_c90"] > 0.08


# ------------------------------------------------------------------ (D) small versions of the findings

def test_posterior_is_narrow_where_the_curve_went_and_wide_where_it_did_not():
    """Question 1, well specified (exact engine, n = 1000, clipped normal, M = 400): F is recovered where the curve
    visited and is not above it.  Median posterior sd / prior sd of F(r): small inside, large outside; the
    interval remains calibrated in both (SBC), so the width is information, not error."""
    st = ic.make_setup("clipnorm", 1000, 0.0, engine="exact")
    s = ic.sbc_summary(ic.sbc_cell(st, 400, np.random.default_rng(61)))
    assert s["sd_F_in"] < 0.1 and s["sd_F_out"] > 0.15 and s["sd_F_out"] > 4 * s["sd_F_in"]
    assert 0.8 < s["c90_F_in"] < 0.97 and 0.8 < s["c90_F_out"] < 0.99


def test_a_wrong_family_is_fitted_confidently_and_wrongly():
    """Deliberate misspecification (094 L4157, L4158): bimodal crowds fitted by a clipped normal (n = 1000, sigma = 0.03)
    lose the coverage of F inside the visited range (the matched fit keeps it) and their error outside it is more than
    twice the matched fit's."""
    n, sig = 1000, 0.03
    fits = {f: ic.make_setup(f, n, sig, engine="sl", S=800, seed=3, size="fine") for f in ("clipnorm", "beta")}
    wrong = ic.misspec_cell("bimodal", fits, n, sig, 200, np.random.default_rng(71))
    right = ic.misspec_cell("clipnorm", fits, n, sig, 200, np.random.default_rng(72))
    sw, sr = ic.misspec_summary(wrong, "clipnorm"), ic.misspec_summary(right, "clipnorm")
    assert sr["inside"]["cov"] > 0.8 and sw["inside"]["cov"] < 0.5
    assert sw["outside"]["rmse"] > 2 * sr["outside"]["rmse"]


def test_two_sided_gate_is_detectable_only_through_declines():
    """Question 2 in miniature (n = 1000, sigma = 0.03): the monotone-order test rejects only when the curve declines
    by more than noise, no more often than its ceiling (the share of curves that decline at all), at about its size under the one-sided control,
    and at about its size on the cumulative (ever-joined) curve, which cannot decline."""
    r = ic.task_twosided(dict(fams=("beta", "clipnorm"), n=1000, sigma=0.03, nu=0.3, wbar=0.5, M=250))["rates"]
    assert r["lrt"] > 3 * r["lrt_one"] + 0.05
    assert r["lrt"] <= r["ceiling"] and r["lrt_one"] < 0.1 and r["lrt_cum"] < 0.1  # the cumulative curve cannot decline


def test_ignition_cell_plumbing_and_the_probe_reads_the_necessary_condition():
    """Question 3 in miniature (exact engine, n = 200, 120 eligible pairs): the cell returns a label, the known-F margin, a
    fitted-model probability and the adaptive probe for every pair; the posterior is a proper distribution; and the
    probe -- an intervention at the host's stall, where Claim 1.4's necessary condition F_1(M) > M is read -- ranks
    the igniting pairs above the others (AUC well above 1/2)."""
    n = 200
    st = [ic.make_setup(f, n, 0.0, engine="exact", size="std") for f in ("beta", "clipnorm")]
    fitted = ic.Fitted(st)
    rows = ic.ignition_cell(("beta", "clipnorm"), n, 0.0, 120, np.random.default_rng(81),
                            models={"bma_nat": (fitted, "nat")})
    assert len(rows) == 120
    lab = np.array([r["label"] for r in rows])
    assert 0 < lab.sum() < len(lab)
    for key in ("oracle", "probe", "bma_nat"):
        assert np.isfinite([r[key] for r in rows]).all()
    k = ic.orbit_counts(CLIP.sample(np.array([0.2, 0.15]), n, np.random.default_rng(1)), 10)
    w = fitted.weights(k / n, k)
    assert w.sum() == pytest.approx(1.0) and (w >= 0).all()
    assert ic.auc_score([r["probe"] for r in rows], lab) > 0.65


def test_task_list_is_complete_and_keys_are_unique():
    """The report's task list (models/identifiability_crowd.build_specs): every kind is present, every task has a distinct
    cache key (so a resumed run cannot mix up two cells), and the SBC grid covers both families, all five crowd sizes
    at sigma = 0 and the three engines."""
    tasks = ic.build_specs()
    keys = [ic._task_key(t_) for t_ in tasks]
    assert len(set(keys)) == len(keys)
    kinds = {k for k, _ in tasks}
    assert kinds == {"sbc", "misspec", "twosided", "ignition", "dynamic", "subsample", "obsmodel", "dirichlet", "visited", "claim14"}
    sbc = [s_ for k, s_ in tasks if k == "sbc"]
    assert {s_["engine"] for s_ in sbc} == {"exact", "lattice", "sl"}
    assert {(s_["fam"], s_["n"]) for s_ in sbc if s_["engine"] == "exact"} == {(f, n) for f in ("beta", "clipnorm") for n in (30, 100, 300, 1000, 3000)}
    # review 2026-11-01: SBC of every setup the misspecification cells fit with when sigma > 0 (fine grid, S = 1,000)
    mis = {(f, s_["n"], s_["sigma"]) for k, s_ in tasks if k == "misspec" and s_["sigma"] > 0 for f in ic.FITTED}
    assert {(s_["fam"], s_["n"], s_["sigma"]) for s_ in sbc if s_.get("setup") == "mfit"} == mis
    assert all(s_["size"] == "fine" and s_["S"] == 1000 for s_ in sbc if s_.get("setup") == "mfit")


def _fake_cell(fam, n, sigma, engine, **summary):
    base = dict(M=1000, tries=1000, min_ks=0.3, c90_min=0.89, c90_max=0.91, z90_max=1.0, ll_ks=0.3, ll_c90=0.9, sd_params=0.5,
                sd_tau=0.5, sd_F0=0.5, sd_F_in=0.5, sd_F_out=0.5, rmse_tau=0.5, rmse_F_in=0.5, rmse_F_out=0.5, c90_F_in=0.9,
                c90_F_out=0.9, n_F_in=100, n_F_out=100, nq=12)
    base.update(summary)
    return ("sbc", dict(spec=dict(fam=fam, n=n, sigma=sigma, engine=engine, M=1000), G=100, summary=base))


def test_report_helpers_flag_calibration_and_find_the_failure_sizes():
    """models/identifiability_crowd_report.py on hand-made cells: the calibration flag (no KS p below 0.001, every coverage within 3.5
    binomial standard errors of 0.90), the smallest n from which a criterion holds for every larger n, and the number formatting."""
    ok = _fake_cell("beta", 100, 0.0, "exact")[1]["summary"]
    assert rep._calibrated(ok) == "yes"
    assert rep._calibrated(dict(ok, min_ks=1e-4)) == "NO"
    assert rep._calibrated(dict(ok, c90_min=0.80)) == "NO"
    assert rep._calibrated(dict(ok, ll_c90=0.80)) == "NO"
    sds = {30: 0.9, 100: 0.4, 300: 0.2, 1000: 0.1, 3000: 0.05}
    cells = [_fake_cell("beta", n, 0.0, "exact", sd_params=v) for n, v in sds.items()]
    assert rep._first_n(cells, "beta", 0.0, "sd_params", 0.25) == (300, True)
    assert rep._first_n(cells, "beta", 0.0, "sd_params", 0.01) == (None, True)
    cells[2] = _fake_cell("beta", 300, 0.0, "exact", sd_params=0.2, c90_min=0.7)  # uncalibrated cell on the way: star
    assert rep._first_n(cells, "beta", 0.0, "sd_params", 0.25) == (300, False)
    assert rep._fmt_n((300, False)) == "300*" and rep._fmt_n((None, True)) == "never"
    assert rep._range([0.501, 0.504]) == "0.50" and rep._range([0.5, 0.62]) == "0.50-0.62" and rep._f(float("nan")) == "-"
    assert rep._range([0.853, 0.857]) == "0.85-0.86"  # compared as printed (review 2026-11-01)
    assert rep._p(0.0004) == "<0.001" and rep._md(["a", "b"], [[1, 2]]).count("\n") == 2


def test_cited_ledger_ids_exist():
    """Every ledger id the module cites (identifiability_crowd.LEDGER) is a line of docs/ledger.jsonl."""
    ids = {json.loads(line)["id"] for line in open(ROOT / "docs" / "ledger.jsonl")}
    assert set(ic.LEDGER) <= ids
