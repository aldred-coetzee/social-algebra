"""Identifiability of the crowd law from aggregate curves, on independent synthetic crowds.

What this tests.  The crowd law of models/00-v0.md section 4.4 is Granovetter's map r(t+1) = F[r(t)]
(ledger L1831, L3960, L3961) with the two-sided gate F = F_theta - F~_thetabar (L3959, L4355) and, from
models/02-our-claims.md Claim 1, a group state that is the whole threshold distribution (merge = mixture,
ignition criterion 1.4).  The event datasets of docs/prior-work/089 give aggregate counts over time and never a
threshold (L3980, L4469).  Under the no-circularity rule of notes/2026-10-29-modelled-population-testbed.md
the crowds below come from generators that are NOT the fitted family (beta, bimodal, logit-normal and
clipped-normal thresholds; one- and two-sided gates), and the only thing the fitting code sees is the noisy
aggregate curve r(0), ..., r(T).  Method of the checks: docs/prior-work/094 (SBC, parameter recovery,
deliberate misspecification, model recovery).

Three questions: (1) can F be recovered from the curve, and at what n and noise; (2) can a two-sided gate be
told from a one-sided one; (3) can Claim 1.4's ignition criterion be predicted from the parts' curves.
Results: sim/results/identifiability_crowd.md, written by `models/identifiability_crowd_report.py` from these functions.

The finite crowd is exact.  n members have thresholds theta_i; k_0 = #{theta_i <= 0} (instigators) and
k_{t+1} = #{theta_i <= k_t / n}, so the whole curve is a sequence of integers (the map F_n of v0.1 6.3 with
r(0) = F_n(0)).  Three likelihood engines read that curve:

  exact      (noise-free): the sequential-binomial law of the integer path, derived below and checked by
             enumeration of every path for tiny n (the probabilities sum to one) and against the simulator.
  lattice    (noise sigma > 0): the exact forward algorithm on the pairs (k_{t-1}, k_t), the state of a
             second-order Markov chain.  Exact, but its cost grows as n^3: used at n = 30 and 100.
  synthetic  (noise sigma > 0, any n): Wood's synthetic likelihood.  The mean and covariance of the curve at
             every grid point are estimated by simulating the frozen-crowd law S times with common random
             numbers; the observation is taken to be Gaussian with that mean and covariance.  An
             approximation: it is calibrated when n sigma is large (n = 1000) and not when counts and noise are on
             the same lattice scale (n = 100, sigma = 0.01); the results file shows where.

Derivation of the exact law [derived, shown].  Let e_{-1} = 0 and e_t = k_t / n.  The count k_{t+1} is the number
of thresholds <= e_t.  Given the past, the n - k_t members not yet counted have thresholds above e_{t-1} (their
number is n - k_t because k_t = #{theta <= e_{t-1}}), so the number of new members k_{t+1} - k_t, whose thresholds
lie in (e_{t-1}, e_t], is Binomial(n - k_t, q_t) with q_t = (F(e_t) - F(e_{t-1})) / (1 - F(e_{t-1})), and
k_0 ~ Binomial(n, F(0)).  The product of these terms is the probability of the path; a stalled step
(e_t = e_{t-1}) has q_t = 0 and contributes 1.  This holds for one-sided gates only (it needs e_t >= e_{t-1}).

What a curve fixes [derived, shown; tests in tests/test_identifiability_crowd.py, group B].
  Proposition B.  The orbit reads #{theta <= e} only at the visited shares e_t <= r* (r* = the stall).  So it fixes
  the counts of thresholds in the cells between visited shares and nothing about thresholds above r*, and nothing
  about where, within a cell, they sit.  Claim 1.4's decisive quantity F_1(M) is read at the host's stall M, which in
  every igniting pair lies strictly above the intruder's own stall (Claim 1.2): outside what the intruder's curve
  can ever show.
  Proposition A.  A non-decreasing orbit is a function k_{t+1} = h(k_t) of the state alone, and a one-sided crowd
  with k_0 members at 0, k_{t+1} - k_t at k_t / n and the rest at 1 reproduces it exactly.  So a monotone curve
  never separates a two-sided from a one-sided gate; only a decline can.  A one-sided stall is absorbing, so the
  only other trace is a curve that is flat and then grows again.  The cumulative (ever-joined) count never declines,
  so a test for declines has no power on it; it can show a plateau followed by growth (after an overshoot), which
  is measured in the results file.
  Proposition B runs the other way from L1225: there no finite moment of F fixes the outcome; here the outcome
  curve does not fix F above its stall.
  Counts are not shares: with thresholds as absolute numbers of others (Granovetter allows either, L3983) the
  count curve does not depend on the pool N, so r* = c*/N is not identified from counts.
"""
from __future__ import annotations

from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy import special as sp
from scipy import stats

SIM = Path(__file__).resolve().parents[1]
RESULTS = SIM / "results" / "identifiability_crowd.md"
SEED = 20261101

# Ledger lines this module and its tests rest on (docs/ledger.jsonl; checked to exist by the tests).
LEDGER = {
    "L1225": "the outcome is not a function of any finite moment of F (Granovetter)",
    "L1201": "monotone F: the orbit rises to the least fixed point [derived]",
    "L1235": "cascade operator, least fixed point by Knaster-Tarski",
    "L1831": "the map r(t+1) = F[r(t)]; equilibrium at the first crossing of the diagonal",
    "L3959": "thresholds are net costs and benefits; the origin of preferences is excluded",
    "L3960": "r(t+1) = F[r(t)] (089)",
    "L3961": "equilibrium F(r_e) = r_e at the first crossing from above (089)",
    "L1833": "normal thresholds, mean 25: the fold at sigma about 12.2 (computed 12.222)",
    "L3962": "normal thresholds: the fold at sigma_c about 12.2 on the 0-100 scale",
    "L3964": "thresholds 0..99 give 100; one threshold moved from 1 to 2 gives 1",
    "L3980": "CCC sizes are order-of-magnitude bins; half are unknown",
    "L3988": "CCC size coding rule: 'hundreds' = 200, 'thousands' = 2,000",
    "L4347": "threshold public good: own turnout no longer needed above the production point",
    "L4348": "crackdown probability rises with size (the individual cost falls; the net cost may go either way)",
    "L4353": "Cantoni et al.: truthful information moved believed attendance (first stage)",
    "L4354": "Cantoni et al.: own attendance fell below the 17% prior and rose above it (reduced form)",
    "L4355": "2SLS: own attendance falls with believed attendance at the Hong Kong margin",
    "L4363": "scope of the substitutes finding is open",
    "L4469": "NAVCO camp_size is ordinal bins; annual resolution",
    "L3983": "a Granovetter threshold is the number or proportion of others who must act first",
    "L4136": "SBC rank statistic",
    "L4137": "SBC theorem: ranks are uniform for exact posterior draws",
    "L4138": "SBC catches designed failures (cited inside the range L4136-L4140)",
    "L4139": "centred eight schools under HMC is biased in tau (cited inside the range L4136-L4140)",
    "L4140": "SBC validates computation only, not the model",
    "L4149": "model recovery: the confusion matrix depends on the noise regime",
    "L4153": "data-dependent test quantities make SBC sensitive",
    "L4156": "joint likelihood as a test quantity",
    "L4157": "deliberate misspecification: measure the damage",
    "L4158": "fake-data recovery is an upper bound on what can be learned",
    "L4160": "confusion and inversion matrices",
}

# --------------------------------------------------------------------------------------------------
# threshold families (population CDFs, densities, samplers, discrete prior grids, continuous priors)
# --------------------------------------------------------------------------------------------------

Z_MIN = 0.02  # every family has at least this instigator share: crowds with none never move (v0.1 6.3)


def _col(P, j, x):
    """Column j of the parameter matrix P (G, p), shaped to broadcast against x of shape (G,) or (1, R)."""
    return P[:, j].reshape((-1,) + (1,) * (np.ndim(x) - 1))


def _logit(x):
    x = np.clip(x, 1e-300, 1 - 1e-16)
    return np.log(x) - np.log1p(-x)


class Family:
    """A threshold distribution on [0, 1] with an atom at 0 (instigators).  Methods are vectorised over a
    parameter matrix P of shape (G, p).  `cdf(P, x)` with x of shape (G,) is pairwise; with x of shape
    (1, R) it returns the (G, R) table.  F(1) = 1 always; thresholds at exactly 1 (the clipped-normal atom)
    never join before everyone has, so F(1-) < 1 there."""

    name = ""
    pnames: tuple = ()

    def cdf(self, P, x):
        raise NotImplementedError

    def sample(self, p, n, rng):
        raise NotImplementedError

    def draw(self, rng):
        raise NotImplementedError

    def grid(self, size="std"):
        raise NotImplementedError

    def table(self, P, r):
        return self.cdf(P, np.asarray(r, float)[None, :])


class BetaAtom(Family):
    """theta = 0 with probability z, else Beta(a, b).  Parameters (z, a, b)."""

    name = "beta"
    pnames = ("z", "a", "b")

    def cdf(self, P, x):
        z, a, b = _col(P, 0, x), _col(P, 1, x), _col(P, 2, x)
        x = np.clip(x, 0.0, 1.0)
        return z + (1 - z) * sp.betainc(a, b, x)

    def sample(self, p, n, rng):
        z, a, b = p
        th = rng.beta(a, b, n)
        th[rng.random(n) < z] = 0.0
        return th

    def draw(self, rng):
        return np.array([np.exp(rng.uniform(np.log(Z_MIN), np.log(0.25))),
                         np.exp(rng.uniform(np.log(0.6), np.log(8.0))),
                         np.exp(rng.uniform(np.log(0.6), np.log(8.0)))])

    def grid(self, size="std"):
        zs, m = (np.array([0.02, 0.04, 0.07, 0.12, 0.20]), 9) if size == "std" else \
            (np.array([0.02, 0.03, 0.05, 0.08, 0.13, 0.22]), 12)
        ab = np.geomspace(0.6, 8.0, m)
        return np.array([[z, a, b] for z in zs for a in ab for b in ab])


class ClipNorm(Family):
    """Granovetter's normal thresholds clipped to [0, 1].  Parameters (mu, s).  The instigator share is
    Phi(-mu / s); we require it to be at least Z_MIN."""

    name = "clipnorm"
    pnames = ("mu", "s")

    def cdf(self, P, x):
        mu, s = _col(P, 0, x), _col(P, 1, x)
        return np.where(x >= 1.0, 1.0, sp.ndtr((np.maximum(x, 0.0) - mu) / s))

    def sample(self, p, n, rng):
        mu, s = p
        return np.clip(rng.normal(mu, s, n), 0.0, 1.0)

    def draw(self, rng):
        while True:
            mu = rng.uniform(0.04, 0.6)
            s = np.exp(rng.uniform(np.log(0.03), np.log(0.4)))
            if sp.ndtr(-mu / s) >= Z_MIN:
                return np.array([mu, s])

    def grid(self, size="std"):
        nm, ns = (18, 14) if size == "std" else (36, 28)
        out = [[mu, s] for mu in np.linspace(0.04, 0.6, nm) for s in np.geomspace(0.03, 0.4, ns)
               if sp.ndtr(-mu / s) >= Z_MIN]
        return np.array(out)


class Bimodal(Family):
    """Instigators z; the rest a two-Beta mixture, weight w on the early mode m1, 1 - w on the late mode m2,
    both with concentration kappa (as explore/mixture_equilibria.py).  Parameters (z, w, m1, m2, kappa).
    A generator only: it is never a fitted family."""

    name = "bimodal"
    pnames = ("z", "w", "m1", "m2", "kappa")

    def cdf(self, P, x):
        z, w, m1, m2, k = (_col(P, j, x) for j in range(5))
        x = np.clip(x, 0.0, 1.0)
        return z + (1 - z) * (w * sp.betainc(m1 * k, (1 - m1) * k, x) + (1 - w) * sp.betainc(m2 * k, (1 - m2) * k, x))

    def sample(self, p, n, rng):
        z, w, m1, m2, k = p
        early = rng.random(n) < w
        th = np.where(early, rng.beta(m1 * k, (1 - m1) * k, n), rng.beta(m2 * k, (1 - m2) * k, n))
        th[rng.random(n) < z] = 0.0
        return th

    def draw(self, rng):
        return np.array([np.exp(rng.uniform(np.log(Z_MIN), np.log(0.2))), rng.uniform(0.2, 0.8),
                         rng.uniform(0.03, 0.35), rng.uniform(0.45, 0.95),
                         np.exp(rng.uniform(np.log(8.0), np.log(40.0)))])

    def grid(self, size="std"):
        raise NotImplementedError("bimodal is a generator only")


class LogitNorm(Family):
    """Instigators z; the rest logit-normal: logit(theta) ~ N(mu, s).  Parameters (z, mu, s)."""

    name = "logitnorm"
    pnames = ("z", "mu", "s")

    def cdf(self, P, x):
        z, mu, s = _col(P, 0, x), _col(P, 1, x), _col(P, 2, x)
        body = sp.ndtr((_logit(np.clip(x, 0.0, 1.0)) - mu) / s)
        return np.where(x >= 1.0, 1.0, np.where(x <= 0.0, z, z + (1 - z) * body))

    def sample(self, p, n, rng):
        z, mu, s = p
        th = sp.expit(rng.normal(mu, s, n))
        th[rng.random(n) < z] = 0.0
        return th

    def draw(self, rng):
        return np.array([np.exp(rng.uniform(np.log(Z_MIN), np.log(0.25))), rng.uniform(-3.0, 1.0),
                         np.exp(rng.uniform(np.log(0.3), np.log(2.5)))])

    def grid(self, size="std"):
        zs, nm, ns = (np.array([0.02, 0.04, 0.07, 0.12, 0.20]), 9, 7) if size == "std" else \
            (np.array([0.02, 0.03, 0.05, 0.08, 0.13, 0.22]), 14, 10)
        return np.array([[z, mu, s] for z in zs for mu in np.linspace(-3.0, 1.0, nm)
                         for s in np.geomspace(0.3, 2.5, ns)])


FAMILIES = {f.name: f for f in (BetaAtom(), ClipNorm(), Bimodal(), LogitNorm())}
FITTED = ("beta", "clipnorm", "logitnorm")  # the families that are ever fitted

# --------------------------------------------------------------------------------------------------
# the finite crowd: exact integer orbits (one- and two-sided gates), stall, merge
# --------------------------------------------------------------------------------------------------


def orbit_counts(theta, T, start=None):
    """Counts k_0, ..., k_T of the one-sided crowd law.  k_0 = #{theta <= 0} unless `start` (an exogenous
    seed count) is given; k_{t+1} = #{theta <= k_t / n}.  Exact: only comparisons of floats with k/n."""
    n = len(theta)
    ts = np.sort(theta)
    k = np.empty(T + 1, dtype=np.int64)
    k[0] = np.searchsorted(ts, 0.0, side="right") if start is None else start
    for t in range(T):
        k[t + 1] = np.searchsorted(ts, k[t] / n, side="right")
    return k


def orbit_two_sided(theta, theta_bar, T, start=None):
    """Counts of the two-sided gate: i is joined iff theta_i <= r <= theta_bar_i (v0.1 2.3, 4.4).  Requires
    theta <= theta_bar member by member, so #{theta_bar < r} is contained in #{theta <= r}.  The orbit is
    r(0) = F(0) and r(t+1) = F(r(t)) with F = F_theta - F~_thetabar; it need not be monotone or converge."""
    n = len(theta)
    ts, tb = np.sort(theta), np.sort(theta_bar)
    k = np.empty(T + 1, dtype=np.int64)

    def count(r):
        return np.searchsorted(ts, r, side="right") - np.searchsorted(tb, r, side="left")

    k[0] = count(0.0) if start is None else start
    for t in range(T):
        k[t + 1] = count(k[t] / n)
    return k


def plateau_then_growth(seq):
    """True if the sequence is flat for one step and moves afterwards.  A one-sided orbit is absorbed at its stall, and
    any orbit of a map on the state alone repeats once it repeats, so this never happens to a current-share
    orbit; it can happen to the ever-joined count of a two-sided crowd."""
    seq = np.asarray(seq)
    return bool(np.any((seq[1:-1] == seq[:-2]) & (seq[2:] != seq[1:-1])))


def orbit_two_sided_ever(theta, theta_bar, T):
    """Two-sided orbit and the CUMULATIVE count of members who have ever been joined by each step.  The ever-joined
    curve is non-decreasing by construction, so it can never show a decline; it can show a plateau followed by growth
    (see `plateau_then_growth`), which a one-sided orbit never does."""
    n = len(theta)
    k = orbit_two_sided(theta, theta_bar, T)
    ever = np.zeros(n, bool)
    out = np.empty(T + 1, dtype=np.int64)
    r = 0.0
    for t in range(T + 1):
        joined = (theta <= r) & (r <= theta_bar) if t > 0 else (theta <= 0.0) & (0.0 <= theta_bar)
        ever |= joined
        out[t] = ever.sum()
        r = k[t] / n
    return k, out


def lfp_count(theta):
    """Least k with #{theta <= k/n} <= k: the stall of the one-sided crowd (Fact 0 of models/02 Claim 1)."""
    n = len(theta)
    ts = np.sort(theta)
    k = np.arange(n + 1)
    cnt = np.searchsorted(ts, k / n, side="right")
    return int(np.argmax(cnt <= k))


def common_prefixed_point(theta1, theta2):
    """Upper end of the merge sandwich (models/02 Claim 1.2): the least r at which BOTH crowds have F(r) <= r, i.e.
    the least share at which both parts would stop on their own.  Candidates are the lattice points j / n_i."""
    s1, s2 = np.sort(theta1), np.sort(theta2)
    n1, n2 = len(s1), len(s2)
    cand = np.unique(np.concatenate([np.arange(n1 + 1) / n1, np.arange(n2 + 1) / n2]))
    ok = (np.searchsorted(s1, cand, side="right") / n1 <= cand) & (np.searchsorted(s2, cand, side="right") / n2 <= cand)
    return float(cand[np.argmax(ok)])


def merged_stall(theta1, theta2):
    """Stall count of the merged crowd (thresholds are shares of the crowd, models/02 1.1) and its size."""
    both = np.concatenate([theta1, theta2])
    return lfp_count(both), len(both)


def ignites(theta1, theta2):
    """Realised ignition (models/02 Claim 1.4): the merge stalls strictly above both parts' own stalls."""
    n1, n2 = len(theta1), len(theta2)
    k1, k2 = lfp_count(theta1), lfp_count(theta2)
    km, nm = merged_stall(theta1, theta2)
    # km/nm > k1/n1 and km/nm > k2/n2, by cross-multiplication (exact integers)
    return bool(km * n1 > nm * k1 and km * n2 > nm * k2)


def ignition_margin(theta1, theta2):
    """Realised ignition margin: the merge's stall share minus the larger of the parts' stall shares."""
    n1, n2 = len(theta1), len(theta2)
    km, nm = merged_stall(theta1, theta2)
    return km / nm - max(lfp_count(theta1) / n1, lfp_count(theta2) / n2)


def observe(k, n, sigma, rng, kind="gauss"):
    """Observed share curve.  gauss: r + N(0, sigma^2), unclipped.  lognorm: r * exp(N(-s^2/2, s^2)) with
    s = sigma (a relative error; zeros stay zero), the way a crowd count is typically wrong."""
    r = np.asarray(k, float) / n
    if sigma == 0:
        return r
    if kind == "gauss":
        return r + rng.normal(0.0, sigma, r.shape)
    if kind == "lognorm":
        return r * np.exp(rng.normal(-0.5 * sigma ** 2, sigma, r.shape))
    raise ValueError(kind)


# --------------------------------------------------------------------------------------------------
# exact law of the noise-free integer path
# --------------------------------------------------------------------------------------------------


def _binom_logpmf(d, m, q):
    """log Binomial(m, q) pmf at d, vectorised over q, with exact handling of q = 0 and q = 1."""
    return (sp.gammaln(m + 1.0) - sp.gammaln(d + 1.0) - sp.gammaln(m - d + 1.0)
            + sp.xlogy(d, q) + sp.xlog1py(m - d, -q))


def path_logprob_exact(k, n, Ftab):
    """log P(k_0, ..., k_T | theta) for each grid point.  Ftab[g, j] = F_g(j / n), j = 0..n.  One-sided
    gates only; the path must be non-decreasing.  See the module docstring for the derivation."""
    k = np.asarray(k)
    G = Ftab.shape[0]
    ll = _binom_logpmf(float(k[0]), float(n), Ftab[:, 0])
    kprev = 0
    for t in range(len(k) - 1):
        d, m = float(k[t + 1] - k[t]), float(n - k[t])
        Fa, Fb = Ftab[:, kprev], Ftab[:, k[t]]
        den = 1.0 - Fa
        q = np.where(den > 0, np.clip((Fb - Fa) / np.where(den > 0, den, 1.0), 0.0, 1.0), 0.0)
        term = _binom_logpmf(d, m, q)
        if m > 0:
            term = np.where(den > 0, term, -np.inf)  # all mass already counted yet members remain
        ll = ll + term
        kprev = int(k[t])
    return ll


def path_logprob_exact_one(k, n, Fvec):
    """Single-parameter version of `path_logprob_exact` (Fvec[j] = F(j / n))."""
    return float(path_logprob_exact(k, n, np.asarray(Fvec)[None, :])[0])


def enumerate_paths(n, Fvec, T):
    """Every path (k_0, ..., k_T) of the one-sided law with its probability, by recursion; for tiny n.
    Used to check that the law sums to one and to compare with simulation."""
    out = {}

    def rec(path):
        if len(path) == T + 1:
            out[tuple(path)] = np.exp(path_logprob_exact_one(path, n, Fvec))
            return
        for c in range(path[-1], n + 1):
            rec(path + [c])

    for k0 in range(n + 1):
        rec([k0])
    return out


# --------------------------------------------------------------------------------------------------
# lattice engine: exact forward algorithm on (k_{t-1}, k_t), noise N(0, sigma^2) on the share
# --------------------------------------------------------------------------------------------------


def _lattice_consts(n):
    ar = np.arange(n + 1)
    b_, c_ = np.meshgrid(ar, ar, indexing="ij")  # b = k_t, c = k_{t+1}
    valid = c_ >= b_
    dmat = np.where(valid, c_ - b_, 0).astype(float)
    mmat = (n - b_).astype(float)
    logC = np.where(valid, sp.gammaln(mmat + 1) - sp.gammaln(dmat + 1) - sp.gammaln(mmat - dmat + 1), -np.inf)
    emat = np.where(valid, n - c_, 0).astype(float)
    return ar, dmat, logC, emat


def lattice_transitions(n, F):
    """Transition tensor P[g, a, b, c] = P(k_{t+1} = c | k_{t-1} = a, k_t = b) for grid rows F (g, n+1)."""
    ar, dmat, logC, emat = _lattice_consts(n)
    Fa, Fb = F[:, :, None], F[:, None, :]
    den = 1.0 - Fa
    q = np.where(den > 0, np.clip((Fb - Fa) / np.where(den > 0, den, 1.0), 0.0, 1.0), 0.0)  # (g, a, b)
    logP = (logC[None, None] + sp.xlogy(dmat[None, None], q[..., None])
            + sp.xlog1py(emat[None, None], -q[..., None]))
    return np.exp(logP)


def lattice_prepare(n, Ftab, budget=3e8):
    """Cache the transition tensors when they fit in `budget` bytes (n up to about 40 on a 800-point grid);
    otherwise None and `ll_lattice` rebuilds them chunk by chunk on every call."""
    if Ftab.shape[0] * (n + 1) ** 3 * 8 > budget:
        return None
    return lattice_transitions(n, Ftab)


def ll_lattice(y, n, Ftab, sigma, prep=None, chunk=None):
    """Exact log-likelihood of the observed curve y_0..y_T (y_t ~ N(k_t / n, sigma^2)) at every grid point.
    The state (k_{t-1}, k_t) is a second-order Markov chain with the binomial transitions above; the
    forward recursion alpha_{t+1}[b, c] = w_{t+1}[c] sum_a alpha_t[a, b] P[a, b, c] is exact."""
    y = np.asarray(y, float)
    G = Ftab.shape[0]
    ar = np.arange(n + 1)
    w = np.exp(-0.5 * ((y[:, None] - ar[None, :] / n) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi))  # (T+1, n+1)
    if chunk is None:
        chunk = G if prep is not None else max(1, int(4e6 // (n + 1) ** 3))
    out = np.empty(G)
    for s0 in range(0, G, chunk):
        F = Ftab[s0:s0 + chunk]
        g = F.shape[0]
        Pm = prep[s0:s0 + chunk] if prep is not None else lattice_transitions(n, F)
        alpha = np.zeros((g, n + 1, n + 1))  # a = k_{-1} = 0 initially
        k0 = np.exp(_binom_logpmf(ar[None, :].astype(float), float(n), F[:, :1]))
        alpha[:, 0, :] = k0 * w[0][None, :]
        logscale = np.zeros(g)
        sc = alpha.sum(axis=(1, 2))
        dead = sc <= 0
        logscale += np.log(np.where(sc > 0, sc, 1.0))
        alpha /= np.where(sc > 0, sc, 1.0)[:, None, None]
        for t in range(1, len(y)):
            alpha = np.einsum("gab,gabc->gbc", alpha, Pm) * w[t][None, None, :]
            sc = alpha.sum(axis=(1, 2))
            dead |= sc <= 0
            logscale += np.log(np.where(sc > 0, sc, 1.0))
            alpha /= np.where(sc > 0, sc, 1.0)[:, None, None]
        out[s0:s0 + chunk] = np.where(dead, -np.inf, logscale)
    return out


# --------------------------------------------------------------------------------------------------
# synthetic-likelihood engine: exact simulator, common random numbers, Gaussian law of the curve
# --------------------------------------------------------------------------------------------------


@dataclass
class Run:
    """One observed run of the crowd (all runs of a design come from the same frozen crowd).  seed=None:
    the natural run from the instigators, r(0) = alpha F_n(0).  seed=s: an exogenous start r(0) = s (an
    intervention on r), observed from step 1.  T = number of steps; `obs` = the steps that are observed."""

    seed: float | None = None
    T: int = 10
    obs: tuple | None = None


def sl_moments(fam, P, n, runs, S, rng, alpha=1.0):
    """Mean (G, M) and covariance (G, M, M) of the observed curve under each grid point, by simulating the
    frozen-crowd law S times with COMMON random numbers (Wood 2010's synthetic likelihood, with the grid
    shared by all draws so the estimates are smooth in the parameters).

    A crowd with threshold CDF F is the sorted uniforms U_(1) <= ... <= U_(n) pushed through F^-1, so
    #{theta <= r} = #{U <= F(r)}: the orbit needs F and the uniforms only, never the thresholds.  One set
    of S uniform samples is used for every grid point.  alpha = 1 is the turn map k_{t+1} = F_n(k_t / n);
    alpha < 1 the inertial variant r_{t+1} = r_t + alpha (F_n(r_t) - r_t).  `runs` as in `Run`; a seeded run
    starts at r(0) = seed.  The result excludes observation noise (add sigma^2 I)."""
    G = P.shape[0]
    U = np.sort(rng.random((S, n)), axis=1)
    flat = (U + np.arange(S)[:, None]).ravel()  # sorted globally: sample s occupies [s, s + 1)

    def count(Fq):  # Fq (S, G) in [0, 1] -> counts #{U_s <= Fq}
        q = np.clip(Fq, 0.0, 1.0) + np.arange(S)[:, None]
        return (np.searchsorted(flat, q.ravel(), side="right").reshape(S, G) - np.arange(S)[:, None] * n)

    means = []
    for run in runs:
        curve = np.empty((S, G, run.T + 1))
        if run.seed is None:
            r = alpha * count(np.broadcast_to(fam.cdf(P, np.zeros(G)), (S, G))) / n
        else:
            r = np.full((S, G), float(run.seed))
        curve[:, :, 0] = r
        for t in range(run.T):
            Fq = _cdf_rows(fam, P, r)
            r = r + alpha * (count(Fq) / n - r)
            curve[:, :, t + 1] = r
        obs = run.obs if run.obs is not None else tuple(range(0 if run.seed is None else 1, run.T + 1))
        means.append(curve[:, :, list(obs)])
    X = np.concatenate(means, axis=2)  # (S, G, M)
    mu = X.mean(axis=0)
    D = X - mu[None]
    cov = np.einsum("sgi,sgj->gij", D, D) / (S - 1)
    return mu, cov


def _cdf_rows(fam, P, r):
    """F_g(r[s, g]) for every sample row s: (S, G) -> (S, G), pairwise in g."""
    S, G = r.shape
    Prep = np.tile(P, (S, 1))
    return fam.cdf(Prep, r.reshape(-1)).reshape(S, G)


def sl_finish(mu, cov, sigma, rel_sigma=0.0):
    """Precision and log-determinant of cov + observation noise, for `ll_gauss`."""
    M = mu.shape[1]
    diag = sigma ** 2 + (rel_sigma * mu) ** 2
    S = cov + diag[:, :, None] * np.eye(M)[None] + 1e-12 * np.eye(M)[None]
    prec = np.linalg.inv(S)
    _, logdet = np.linalg.slogdet(S)
    return mu, prec, logdet


# --------------------------------------------------------------------------------------------------
# Gaussian likelihood of the stacked observed vector
# --------------------------------------------------------------------------------------------------


def ll_gauss(y, mom):
    """Gaussian log-likelihood of the stacked observed vector y at each grid point (synthetic moments)."""
    mean, prec, logdet = mom
    d = np.asarray(y, float)[None, :] - mean
    quad = np.einsum("gi,gij,gj->g", d, prec, d)
    return -0.5 * (quad + logdet + mean.shape[1] * np.log(2 * np.pi))


# --------------------------------------------------------------------------------------------------
# quantities of interest, posteriors on a discrete prior grid, simulation-based calibration
# --------------------------------------------------------------------------------------------------

PROBES = (0.1, 0.25, 0.4, 0.55, 0.7, 0.85)  # shares r at which F(r) is read
RGRID = np.linspace(0.0, 1.0, 2001)


def tau_of(Ftab_r):
    """Population stall tau(F) = min{r : F(r) <= r} on RGRID, for a (G, 2001) table (models/02 Fact 0)."""
    ok = Ftab_r <= RGRID[None, :] + 1e-12
    return RGRID[np.argmax(ok, axis=1)]


def quantities(fam, P):
    """(G, nq) matrix of the quantities whose recovery is scored, and their names: the parameters, the
    population stall tau, the instigator share F(0), and F at the probe shares.  Rounded so that ties
    between grid points are exact ties."""
    Ft = fam.table(P, RGRID)
    cols = [P[:, j] for j in range(P.shape[1])]
    names = list(fam.pnames)
    cols.append(tau_of(Ft)); names.append("tau")
    cols.append(fam.cdf(P, np.zeros(len(P)))); names.append("F0")
    for r in PROBES:
        cols.append(fam.cdf(P, np.full(len(P), r))); names.append(f"F({r:g})")
    return np.round(np.stack(cols, axis=1), 9), names


def posterior_weights(ll):
    """Normalised posterior on the uniform grid prior from log-likelihoods (nan if no grid point can
    produce the data)."""
    m = np.max(ll)
    if not np.isfinite(m):
        return None
    w = np.exp(ll - m)
    return w / w.sum()


def randomized_pit(w, Q, g, rng):
    """For each column of Q the randomised probability integral transform of the truth Q[g] under the
    discrete posterior w: P(q < q_true) + U P(q = q_true).  Uniform on (0, 1) if the posterior is exact."""
    qt = Q[g][None, :]
    lower = (w[:, None] * (Q < qt)).sum(axis=0)
    tie = (w[:, None] * (Q == qt)).sum(axis=0)
    return lower + rng.random(Q.shape[1]) * tie


@dataclass
class Setup:
    """Everything about a fitted grid that does not depend on the data: the grid (the discrete prior), the scored
    quantities on it, and the engine's tables (exact/lattice: F at the lattice j / n; synthetic: moments)."""

    fam: Family
    P: np.ndarray
    n: int
    T: int
    sigma: float
    engine: str
    Q: np.ndarray
    qnames: list
    Ftab: np.ndarray | None = None
    mom: tuple | None = None
    runs: tuple = ()
    alpha: float = 1.0
    prep: np.ndarray | None = None
    Ft: np.ndarray | None = None  # (G, 2001) population CDF on RGRID
    temper: float = 1.0  # multiplies the log-likelihood; != 1 builds a deliberately wrong posterior (SBC power check)


def make_setup(fam_name, n, sigma, T=10, engine=None, S=1000, seed=0, runs=None, alpha=1.0, P=None,
               size="std", rel_sigma=0.0):
    """Precompute everything about the grid that does not depend on the data."""
    fam = FAMILIES[fam_name]
    P = fam.grid(size) if P is None else P
    Q, qn = quantities(fam, P)
    Ft = fam.table(P, RGRID)
    if engine is None:
        engine = "exact" if sigma == 0 else "sl"
    st = Setup(fam, P, n, T, sigma, engine, Q, qn, runs=tuple(runs) if runs else (Run(None, T),), alpha=alpha, Ft=Ft)
    if engine in ("exact", "lattice"):
        st.Ftab = fam.table(P, np.arange(n + 1) / n)
    if engine == "lattice":
        st.prep = lattice_prepare(n, st.Ftab)
    if engine == "sl":
        mu, cov = sl_moments(fam, P, n, list(st.runs), S, np.random.default_rng(seed), alpha=alpha)
        st.mom = sl_finish(mu, cov, sigma, rel_sigma)
    return st


def loglik(st, y, k=None):
    """Log-likelihood of one observed curve (and, for the exact engine, its integer path) at every grid point."""
    if st.engine == "exact":
        ll = path_logprob_exact(k, st.n, st.Ftab)
    elif st.engine == "lattice":
        ll = ll_lattice(y, st.n, st.Ftab, st.sigma, prep=st.prep)
    else:
        ll = ll_gauss(y, st.mom)
    return ll * st.temper if st.temper != 1.0 else ll


def is_live(y, n, sigma):
    """An event dataset only contains crowds that moved: the curve reaches 3 sigma (or one member)."""
    return bool(np.max(y) >= max(3 * sigma, 1.0 / n))


def level_hat(y):
    """Estimate of where the curve ended (mean of the last three points), used only to label F(r) as read
    inside or outside the support the curve visited."""
    return float(np.clip(np.mean(y[-3:]), 0.0, 1.0))


def observe_runs(th, st, rng):
    """Noisy observed vector for the design of `st` from the frozen crowd `th`: the natural run (steps in
    run.obs) and any seeded runs (an exogenous start r(0) = seed, observed from step 1).  Returns the stacked
    vector, the natural run's part (used only to decide whether the crowd is live) and, for the turn map
    alpha = 1, the natural run's integer path (read by the exact engine)."""
    n = len(th)
    parts, y_nat, k_nat = [], None, None
    for run in st.runs:
        if run.seed is None:
            if st.alpha == 1.0:
                k_nat = orbit_counts(th, run.T)
                r = k_nat / n
            else:
                r = orbit_inertial(th, run.T, st.alpha)
            obs = run.obs if run.obs is not None else tuple(range(run.T + 1))
            r = r[list(obs)]
        else:
            r = orbit_inertial(th, run.T, st.alpha, seed=run.seed)
            obs = run.obs if run.obs is not None else tuple(range(1, run.T + 1))
            r = r[[o - 1 for o in obs]]
        r = r + (rng.normal(0.0, st.sigma, r.shape) if st.sigma > 0 else 0.0)
        if run.seed is None and y_nat is None:
            y_nat = r
        parts.append(r)
    return np.concatenate(parts), y_nat, k_nat


def sbc_cell(st, M, rng, max_tries=None):
    """M live datasets drawn from the prior predictive of `st` (generator = fitted family, theta on the grid)
    and their posteriors.  Returns arrays: u (M, nq) randomised ranks, pm / ps posterior mean and sd, truth,
    u_ll the rank of the joint log-likelihood (Modrak et al.), level (M,), plus the number of draws tried."""
    G, nq = st.Q.shape
    prior_sd = st.Q.std(axis=0)
    U, PM, PS, TR, LV, UL = [], [], [], [], [], []
    tries = 0
    max_tries = max_tries or 200 * M
    while len(U) < M and tries < max_tries:
        tries += 1
        g = int(rng.integers(G))
        th = st.fam.sample(st.P[g], st.n, rng)
        y, y_nat, k = observe_runs(th, st, rng)
        if not is_live(y_nat, st.n, st.sigma):
            continue
        ll = loglik(st, y, k)
        w = posterior_weights(ll)
        if w is None:
            continue
        U.append(randomized_pit(w, st.Q, g, rng))
        pm = w @ st.Q
        PM.append(pm)
        PS.append(np.sqrt(np.maximum(w @ st.Q ** 2 - pm ** 2, 0.0)))
        TR.append(st.Q[g])
        LV.append(level_hat(y_nat))
        lo = float(w[ll < ll[g]].sum())
        ti = float(w[ll == ll[g]].sum())
        UL.append(lo + rng.random() * ti)
    return dict(u=np.array(U), pm=np.array(PM), ps=np.array(PS), truth=np.array(TR), level=np.array(LV),
                u_ll=np.array(UL), prior_sd=prior_sd, names=st.qnames, tries=tries, M=len(U))


def summarize_u(u):
    """Rank-uniformity summaries for a vector of randomised ranks: KS p-value, central 50 / 90% coverage."""
    u = np.asarray(u)
    ks = stats.kstest(u, "uniform").pvalue
    c50 = float(np.mean((u >= 0.25) & (u <= 0.75)))
    c90 = float(np.mean((u >= 0.05) & (u <= 0.95)))
    return dict(ks=float(ks), c50=c50, c90=c90, n=len(u))


# --------------------------------------------------------------------------------------------------
# structure: what a curve can and cannot fix (constructions behind the tests)
# --------------------------------------------------------------------------------------------------


def orbit_equivalent_one_sided(k, n):
    """Thresholds of a one-sided crowd whose orbit is the given non-decreasing path k_0, ..., k_T.

    Proposition A [derived, shown].  Let k be the orbit of ANY crowd, one- or two-sided, whose orbit is
    non-decreasing.  Then k_{t+1} is a function of k_t alone (the next count is read off the current share), so a
    stalled step stays stalled.  Put k_0 members at threshold 0, d_s = k_{s+1} - k_s members at threshold k_s / n
    for each s, and the rest at 1.  The members at thresholds <= k_t / n are those at 0 and those placed for steps
    s <= t (a step s > t has k_s >= k_t and adds members only if k_s > k_t, by persistence), so their number is
    k_0 + sum_{s <= t} d_s = k_{t+1}: the orbit is reproduced exactly.  A monotone curve therefore cannot tell a
    two-sided gate from a one-sided one, whatever n and however small the noise."""
    th = np.ones(n)
    k = np.asarray(k)
    th[: k[0]] = 0.0
    pos = int(k[0])
    for t in range(len(k) - 1):
        d = int(k[t + 1] - k[t])
        if d > 0:
            th[pos:pos + d] = k[t] / n
            pos += d
    return th


def redraw_above_stall(theta, rng):
    """A crowd with the same orbit as `theta` and different thresholds.  The orbit uses #{theta <= e_t} only
    at the visited shares e_t <= r* = k*/n, so every threshold above r* can be replaced by any other value
    above r* (Proposition B: the curve fixes F on [0, r*] at the visited points and nothing above r*)."""
    n = len(theta)
    rstar = lfp_count(theta) / n
    out = theta.copy()
    above = out > rstar
    out[above] = rng.uniform(np.nextafter(rstar, 1.0), 1.0, int(above.sum()))
    return out


def count_orbit(theta_abs, T):
    """Orbit in COUNTS when thresholds are absolute numbers of others (Granovetter allows either; L3983):
    c_{t+1} = #{theta_abs <= c_t}.  The pool size N never enters, so counts cannot fix the denominator."""
    ts = np.sort(theta_abs)
    c = np.empty(T + 1, dtype=np.int64)
    c[0] = np.searchsorted(ts, 0, side="right")
    for t in range(T):
        c[t + 1] = np.searchsorted(ts, c[t], side="right")
    return c


def orbit_inertial(theta, T, alpha, seed=None):
    """Inertial variant: r_{t+1} = r_t + alpha (F_n(r_t) - r_t), r_{-1} = 0 (alpha = 1 is the turn map).
    Natural start: the shares r_0 .. r_T (r_0 = alpha F_n(0)); from an exogenous start `seed` (a share):
    r_1 .. r_T.  Each member re-decides with probability alpha per turn, in expectation (v0.1's turns have
    no clock; this is the simplest way to give them one)."""
    n = len(theta)
    ts = np.sort(theta)
    out = []
    if seed is None:
        r = alpha * np.searchsorted(ts, 0.0, side="right") / n
        out.append(r)
    else:
        r = float(seed)
    for _ in range(T):
        r = r + alpha * (np.searchsorted(ts, r, side="right") / n - r)
        out.append(r)
    return np.array(out)


# ---- the non-parametric, noise-free posterior (histogram-Dirichlet prior): exact and conjugate ----


class DirichletHistogram:
    """Thresholds on the grid {0, 1/B, ..., 1}; probabilities p ~ Dirichlet(alpha) with an atom of prior mass
    g0 at 0 (instigators).  A crowd is n draws from p.

    Exact posterior from the noise-free orbit [derived, shown].  The path k_0..k_T is the event that the counts of
    thresholds in the cells {0}, (c_{-1}, c_0], (c_0, c_1], ..., and the remainder are (k_0, k_1 - k_0, ...),
    where the cut indices c_t = floor(k_t B / n) are fixed by the path.  The likelihood is a function of the
    cell masses alone, so by the aggregation property of the Dirichlet the cell masses are Dirichlet(alpha_cell +
    counts) and, within a cell, the normalised probabilities keep their PRIOR law, independent of the data.
    Above the stall the posterior is therefore the prior conditional on the remaining mass, whatever n."""

    def __init__(self, B=40, c=20.0, g0=0.05):
        self.B = B
        base = np.full(B + 1, (1 - g0) / B)
        base[0] = g0
        self.alpha = c * base

    def sample_prior(self, rng):
        return rng.dirichlet(self.alpha)

    def crowd_path(self, p, n, T, rng):
        N = rng.multinomial(n, p)
        cum = np.cumsum(N)
        k = np.empty(T + 1, dtype=np.int64)
        k[0] = N[0]
        for t in range(T):
            j = int(np.floor(k[t] * self.B / n + 1e-12))
            k[t + 1] = cum[min(j, self.B)]
        return k

    def cells(self, k, n):
        """Cut indices and counts: list of (lo, hi, count) with atoms lo < j <= hi (lo = -1 for the atom at 0)."""
        B = self.B
        out = [(-1, 0, int(k[0]))]
        prev = 0
        for t in range(len(k) - 1):
            c = min(int(np.floor(k[t] * B / n + 1e-12)), B)
            cnt = int(k[t + 1] - k[t])
            if c > prev:
                out.append((prev, c, cnt))
                prev = c
            else:
                assert cnt == 0
        if prev < B:
            out.append((prev, B, int(n - k[-1])))
        return out

    def posterior_samples(self, k, n, L, rng):
        cells = self.cells(k, n)
        P = np.zeros((L, self.B + 1))
        a_cell = np.array([self.alpha[lo + 1:hi + 1].sum() for lo, hi, _ in cells])
        cnt = np.array([c for _, _, c in cells], float)
        masses = rng.dirichlet(a_cell + cnt, size=L) if len(cells) > 1 else np.ones((L, 1))
        for i, (lo, hi, _) in enumerate(cells):
            a = self.alpha[lo + 1:hi + 1]
            inner = rng.dirichlet(a, size=L) if len(a) > 1 else np.ones((L, 1))
            P[:, lo + 1:hi + 1] = masses[:, i:i + 1] * inner
        return P

    def prior_samples(self, L, rng):
        return rng.dirichlet(self.alpha, size=L)


# ---- one- versus two-sided gate: a monotone-order test on the observed curve ----


def draw_two_sided(fam, p, n, nu, wbar, rng, kappa=6.0):
    """Lower thresholds from `fam`; a fraction nu of members also has an upper gate theta + (1 - theta) V,
    V ~ Beta(wbar kappa, (1 - wbar) kappa), above which they drop out (backlash, substitutes: L4347, L4348).
    The others stay for ever.  Satisfies theta <= theta_bar member by member."""
    th = fam.sample(p, n, rng)
    finite = rng.random(n) < nu
    V = rng.beta(wbar * kappa, (1 - wbar) * kappa, n)
    return th, np.where(finite, th + (1 - th) * V, 1.0)


def isotonic_nondecreasing(Y):
    """Least-squares non-decreasing fit of each row of Y (N, m), by the min-max formula
    fit_i = max_{j <= i} min_{k >= i} mean(Y[j..k])."""
    Y = np.atleast_2d(Y)
    N, m = Y.shape
    cs = np.concatenate([np.zeros((N, 1)), np.cumsum(Y, axis=1)], axis=1)
    J, K = np.meshgrid(np.arange(m), np.arange(m), indexing="ij")
    cnt = np.where(K >= J, K - J + 1, 1)
    Av = (cs[:, K + 1] - cs[:, J]) / cnt
    fit = np.empty_like(Y, dtype=float)
    for i in range(m):
        fit[:, i] = Av[:, : i + 1, i:].min(axis=2).max(axis=1)
    return fit


def lrt_stat(Y, sigma):
    """Likelihood-ratio statistic of 'the latent curve is non-decreasing' against 'unrestricted' for
    Gaussian noise of known sd sigma: sum (y - isotonic fit)^2 / sigma^2.  Large = a decline."""
    return ((Y - isotonic_nondecreasing(Y)) ** 2).sum(axis=1) / sigma ** 2


def max_drop_stat(Y, sigma):
    """Largest drop y_s - y_t over s < t, in units of sigma sqrt(2): the 'any decline' rule."""
    m = Y.shape[1]
    drops = [Y[:, s] - Y[:, t] for s in range(m) for t in range(s + 1, m)]
    return np.max(drops, axis=0) / (sigma * np.sqrt(2))


_CRIT_CACHE: dict = {}


def flat_null_critical(stat, m, alpha, N=200_000, seed=12345):
    """Critical value of `stat` under the least-favourable null (the latent curve constant), by simulation.
    For testing a monotone cone against its complement the flat curve is the least favourable null, so a test
    of this size has size <= alpha for every non-decreasing latent curve (Robertson, Wright & Dykstra 1988)."""
    key = (stat.__name__, m, alpha, N, seed)
    if key not in _CRIT_CACHE:
        Z = np.random.default_rng(seed).normal(size=(N, m))
        _CRIT_CACHE[key] = float(np.quantile(stat(Z, 1.0), 1 - alpha))
    return _CRIT_CACHE[key]


# --------------------------------------------------------------------------------------------------
# independent generators fitted by the wrong family: the damage, and which family the curve prefers
# --------------------------------------------------------------------------------------------------


def wquantile(vals, w, qs):
    """Weighted quantiles of a discrete distribution."""
    o = np.argsort(vals, kind="stable")
    v, c = vals[o], np.cumsum(w[o])
    return np.array([v[min(int(np.searchsorted(c, q)), len(v) - 1)] for q in qs])


def truth_functionals(gen, p):
    """tau, F(0) and F at the probe shares for a generator with continuous parameters p (same order as the
    functional columns of `quantities`)."""
    P = np.asarray(p, float)[None, :]
    Ft = gen.table(P, RGRID)
    out = [tau_of(Ft)[0], float(gen.cdf(P, np.zeros(1))[0])]
    out += [float(gen.cdf(P, np.full(1, r))[0]) for r in PROBES]
    return np.array(out)


def misspec_cell(gen_name, fits, n, sigma, M, rng, T=10, max_tries=None):
    """M live curves from the independent generator `gen_name` (continuous parameters), each fitted by every
    family in `fits` (dict name -> Setup).  Per fit: posterior mean / sd and 5-95% limits of the functional
    columns (tau, F0, F at the probes), the truth, and the log marginal likelihood (uniform grid prior)."""
    gen = FAMILIES[gen_name]
    names = list(fits)
    nf = 2 + len(PROBES)
    rec = {f: dict(pm=[], ps=[], lo=[], hi=[]) for f in names}
    truth, level, ml, tries = [], [], [], 0
    max_tries = max_tries or 200 * M
    while len(truth) < M and tries < max_tries:
        tries += 1
        p = gen.draw(rng)
        th = gen.sample(p, n, rng)
        k = orbit_counts(th, T)
        y = observe(k, n, sigma, rng)
        if not is_live(y, n, sigma):
            continue
        per = {}
        for f, st in fits.items():
            ll = loglik(st, y, k)
            w = posterior_weights(ll)
            if w is None:
                per = None
                break
            Qf = st.Q[:, len(st.fam.pnames):]
            pm = w @ Qf
            ps = np.sqrt(np.maximum(w @ Qf ** 2 - pm ** 2, 0.0))
            lohi = np.array([wquantile(Qf[:, j], w, (0.05, 0.95)) for j in range(nf)])
            m = np.max(ll)
            per[f] = (pm, ps, lohi[:, 0], lohi[:, 1], m + np.log(np.mean(np.exp(ll - m))))
        if per is None:
            continue
        for f in names:
            for key, v in zip(("pm", "ps", "lo", "hi"), per[f][:4]):
                rec[f][key].append(v)
        ml.append([per[f][4] for f in names])
        truth.append(truth_functionals(gen, p))
        level.append(level_hat(y))
    out = dict(gen=gen_name, n=n, sigma=sigma, names=names, truth=np.array(truth), level=np.array(level),
               ml=np.array(ml), tries=tries, M=len(truth))
    for f in names:
        out[f] = {k: np.array(v) for k, v in rec[f].items()}
        out[f]["prior_sd"] = fits[f].Q[:, len(fits[f].fam.pnames):].std(axis=0)
    return out


def misspec_summary(res, fit):
    """Coverage of the 90% interval, normalised RMSE and mean posterior sd for tau, F0 and the F probes read
    INSIDE (r <= the level the curve reached) and OUTSIDE it, for one fitted family."""
    d = res[fit]
    tr, lv = res["truth"], res["level"]
    sdp = d["prior_sd"]
    cov = (d["lo"] <= tr + 1e-9) & (tr <= d["hi"] + 1e-9)
    err = (d["pm"] - tr) / sdp
    sd = d["ps"] / sdp
    out = {}
    for name, j in (("tau", 0), ("F0", 1)):
        out[name] = dict(cov=float(cov[:, j].mean()), rmse=float(np.sqrt(np.mean(err[:, j] ** 2))),
                         sd=float(np.median(sd[:, j])), n=len(tr))
    inside = np.array([[r <= l for r in PROBES] for l in lv])
    pj = np.arange(2, 2 + len(PROBES))
    for lab, mask in (("inside", inside), ("outside", ~inside)):
        c = cov[:, pj][mask]
        e = err[:, pj][mask]
        s_ = sd[:, pj][mask]
        out[lab] = dict(cov=float(c.mean()) if c.size else np.nan,
                        rmse=float(np.sqrt(np.mean(e ** 2))) if c.size else np.nan,
                        sd=float(np.median(s_)) if c.size else np.nan, n=int(c.size))
    return out


def confusion(res):
    """For one generator: the share of its curves for which each fitted family has the largest marginal likelihood
    (one row of the confusion matrix of 094 L4149, L4160, with a uniform prior over the fitted families)."""
    ml = res["ml"]
    best = np.argmax(ml, axis=1)
    share = np.bincount(best, minlength=ml.shape[1]) / len(ml)
    return dict(zip(res["names"], share))


# --------------------------------------------------------------------------------------------------
# ignition (models/02 Claim 1.4) predicted from the parts' aggregate curves
# --------------------------------------------------------------------------------------------------

IGN_MARGIN = 0.005  # population-level ignition: merged stall exceeds both parts' by more than this share
MATERIAL_MARGIN = 0.02  # "material" realised ignition: the merge stalls at least this share of the crowd higher


def pop_margin(Ft1, Ft2):
    """Population-level ignition margin for rows of CDF tables on RGRID, (S, 2001) each: the merge of two equal-sized
    crowds is the mixture (F1 + F2) / 2 (models/02 1.1), its stall the least r with F_m(r) <= r (Fact 0); the
    margin is that stall minus the larger of the parts' stalls."""
    r = RGRID[None, :]
    Em = 0.5 * (Ft1 + Ft2) - r
    tm = RGRID[np.argmax(Em <= 1e-12, axis=1)]
    return tm - np.maximum(tau_of(Ft1), tau_of(Ft2))


def pop_ignites(Ft1, Ft2, margin=IGN_MARGIN):
    """Population-level ignition (models/02 Claim 1.4): the margin exceeds `margin`.  Boolean (S,)."""
    return pop_margin(Ft1, Ft2) > margin


def auc_score(score, label):
    """Area under the ROC curve (Mann-Whitney), ties counted half; nan if one class is empty."""
    score, label = np.asarray(score, float), np.asarray(label, bool)
    pos, neg = score[label], score[~label]
    if len(pos) == 0 or len(neg) == 0:
        return float("nan")
    ranks = stats.rankdata(np.concatenate([pos, neg]))
    return float((ranks[: len(pos)].sum() - len(pos) * (len(pos) + 1) / 2) / (len(pos) * len(neg)))


def auc_ci(score, label, rng, B=300):
    """Bootstrap 95% interval of the AUC (pairs resampled)."""
    score, label = np.asarray(score, float), np.asarray(label, bool)
    vals = []
    for _ in range(B):
        i = rng.integers(len(score), size=len(score))
        a = auc_score(score[i], label[i])
        if not np.isnan(a):
            vals.append(a)
    return (float(np.quantile(vals, 0.025)), float(np.quantile(vals, 0.975))) if vals else (np.nan, np.nan)


def brier(prob, label):
    return float(np.mean((np.asarray(prob, float) - np.asarray(label, float)) ** 2))


def draw_pair(gen_names, n, sigma, rng, seeds=(), T=10, T_seed=3):
    """Two independent crowds from random generators in `gen_names`: their thresholds, integer orbits, noisy
    natural curves, noisy seeded curves for the fixed `seeds`, and the generator CDF tables."""
    crowds = []
    for _ in range(2):
        gen = FAMILIES[gen_names[int(rng.integers(len(gen_names)))]]
        p = gen.draw(rng)
        th = gen.sample(p, n, rng)
        k = orbit_counts(th, T)
        y = observe(k, n, sigma, rng)
        ys = [orbit_inertial(th, T_seed, 1.0, seed=s_) + (rng.normal(0, sigma, T_seed) if sigma > 0 else 0.0)
              for s_ in seeds]
        crowds.append(dict(gen=gen, p=p, th=th, k=k, y=y, ys=ys, Ft=gen.table(np.asarray(p)[None, :], RGRID)[0]))
    return crowds


def probe_excess(th, share, sigma, rng):
    """One adaptive probe: start the crowd at r(0) = share and observe r(1) = F_n(share) + noise; return r(1) - share.
    This is an intervention on r (the design of Cantoni et al.'s belief experiment, L4353-L4355)."""
    n = len(th)
    r1 = np.searchsorted(np.sort(th), share, side="right") / n
    return float(r1 + (rng.normal(0, sigma) if sigma > 0 else 0.0) - share)


class Fitted:
    """A fitted model for a crowd: one Setup, or an average over several families with a uniform prior over
    the families and, within each, over its grid.  `weights(y, k)` is the posterior over all grid points."""

    def __init__(self, setups):
        self.setups = list(setups)
        self.Ft = np.vstack([s.Ft for s in self.setups])
        self.logprior = np.concatenate([np.full(len(s.P), -np.log(len(s.P)) - np.log(len(self.setups)))
                                        for s in self.setups])

    def weights(self, y, k=None):
        ll = np.concatenate([loglik(s, y, k) for s in self.setups])
        return posterior_weights(ll + self.logprior)


def ignition_cell(gen_names, n, sigma, Npairs, rng, models=None, designs=None, T=10, S_post=300, max_level=0.97):
    """Predict realised ignition of the merge of two independent crowds from their noisy standalone curves.

    Eligible pairs: both live and neither curve ends above `max_level` (a saturated crowd cannot be ignited
    further).  Predictors, scored by AUC against the realised label (strict, in members):
      oracle   the population-level ignition margin of the TRUE generators (a reference that knows F exactly; it
               is not a ceiling, because the curves also carry the realised crowds' own thresholds);
      model    posterior-predictive probability of population ignition from a Fitted model, per design (natural
               run only, or plus fixed-seed runs): `models` maps name -> (Fitted, design name);
      summary  features of the two curves for a logistic regression (done by `ignition_summary_auc`);
      probe    the largest excess of an adaptive one-step probe of each crowd started at the higher final level."""
    models = models or {}
    designs = designs or {"nat": ()}
    all_seeds = sorted({s_ for d in designs.values() for s_ in d})
    rows, tries = [], 0
    while len(rows) < Npairs and tries < 400 * Npairs:
        tries += 1
        pair = draw_pair(gen_names, n, sigma, rng, seeds=all_seeds, T=T)
        if not all(is_live(c["y"], n, sigma) for c in pair):
            continue
        L = [level_hat(c["y"]) for c in pair]
        if max(L) >= max_level:
            continue
        row = dict(label=ignites(pair[0]["th"], pair[1]["th"]),
                   label_mat=bool(ignition_margin(pair[0]["th"], pair[1]["th"]) >= MATERIAL_MARGIN),
                   L=L, y0=[float(c["y"][0]) for c in pair],
                   oracle=float(pop_margin(pair[0]["Ft"][None], pair[1]["Ft"][None])[0]),
                   probe=max(probe_excess(c["th"], max(L), sigma, rng) for c in pair))
        for name, (fitted, d) in models.items():
            ws = []
            for c in pair:
                yy = np.concatenate([c["y"]] + [c["ys"][all_seeds.index(s_)] for s_ in designs[d]])
                ws.append(fitted.weights(yy, c["k"]))
            if any(w is None for w in ws):
                row[name] = np.nan
                continue
            g1 = rng.choice(len(ws[0]), size=S_post, p=ws[0])
            g2 = rng.choice(len(ws[1]), size=S_post, p=ws[1])
            row[name] = float(pop_ignites(fitted.Ft[g1], fitted.Ft[g2]).mean())
        rows.append(row)
    return rows


def summary_features(row):
    lo, hi = sorted(row["L"])
    y0 = sorted(row["y0"])
    return np.array([lo, hi, hi - lo, y0[0], y0[1], (hi - lo) ** 2, lo * hi])


def fit_logistic(X, y, ridge=1e-2):
    """L2-regularised logistic regression (standardised features), returns a scoring function."""
    from scipy.optimize import minimize

    mu, sd = X.mean(0), X.std(0) + 1e-9
    Z = np.hstack([(X - mu) / sd, np.ones((len(X), 1))])

    def nll(w):
        a = Z @ w
        return np.sum(np.logaddexp(0, a) - y * a) + ridge * np.sum(w[:-1] ** 2)

    def grad(w):
        a = Z @ w
        return Z.T @ (sp.expit(a) - y) + 2 * ridge * np.r_[w[:-1], 0.0]

    w = minimize(nll, np.zeros(Z.shape[1]), jac=grad, method="L-BFGS-B").x
    return lambda Xn: np.hstack([(Xn - mu) / sd, np.ones((len(Xn), 1))]) @ w


# --------------------------------------------------------------------------------------------------
# variations of the model form
# --------------------------------------------------------------------------------------------------


def logmeanexp(ll):
    m = np.max(ll)
    return m + np.log(np.mean(np.exp(ll - m)))


def dynamic_form_cell(fam_name, n, sigma, M, rng, alpha_true, alphas=(0.25, 0.5, 0.75, 1.0), T=16, S=800):
    """Which dynamic form fits?  Curves come from the inertial crowd with alpha_true (alpha = 1 the turn map of
    v0.1; alpha < 1 members re-decide with probability alpha per turn), thresholds from `fam_name` with
    continuous parameters.  Each curve is fitted by the same threshold family with alpha fixed at every value
    of `alphas`.  Returns the share of curves for which each alpha has the largest marginal likelihood, and, for
    every fitted alpha, the RMSE (over the prior sd) of the posterior mean of tau and of F at ALL the probes."""
    fam = FAMILIES[fam_name]
    sts = {a: make_setup(fam_name, n, sigma, T=T, engine="sl", S=S, seed=11, alpha=a) for a in alphas}
    wins = np.zeros(len(alphas))
    lbf = []
    errs = {a: [] for a in alphas}
    got = 0
    while got < M:
        p = fam.draw(rng)
        th = fam.sample(p, n, rng)
        y = orbit_inertial(th, T, alpha_true)
        y = y + (rng.normal(0, sigma, y.shape) if sigma > 0 else 0.0)
        if not is_live(y, n, sigma):
            continue
        mls = []
        for a in alphas:
            ll = loglik(sts[a], y)
            mls.append(logmeanexp(ll))
            w = posterior_weights(ll)
            Qf = sts[a].Q[:, len(fam.pnames):]
            tr = truth_functionals(fam, p)
            errs[a].append(((w @ Qf) - tr) / Qf.std(axis=0))
        mls = np.array(mls)
        wins[int(np.argmax(mls))] += 1
        lbf.append(mls - mls.max())
        got += 1
    err = {a: np.array(v) for a, v in errs.items()}
    return dict(alpha_true=alpha_true, alphas=alphas, share=wins / M, mean_logml=np.mean(lbf, axis=0),
                rmse_tau={a: float(np.sqrt(np.mean(err[a][:, 0] ** 2))) for a in alphas},
                rmse_F={a: float(np.sqrt(np.mean(err[a][:, 2:] ** 2))) for a in alphas})


def subsample_cell(fam_name, n, sigma, M, rng, m_true, ms=(1, 2, 3), J=5, S=800):
    """Observation every m-th turn.  Curves from the turn map observed at times 0, m, 2m, ..., J m.  Three fits:
    the true m known, m wrongly taken to be 1, and m unknown (marginalised over `ms`, uniform prior).  Returns the
    median relative posterior sd of tau and of F at ALL the probes (median over probes, then over curves), and the
    RMSE of the posterior mean over the prior sd (over curves; for F over curves and probes together).
    Corrected at review (2026-11-01): `rmse_F` was the median over curves of each curve's RMS error, not an RMSE."""
    fam = FAMILIES[fam_name]
    Tfull = J * max(ms)
    sts = {m: make_setup(fam_name, n, sigma, T=Tfull, engine="sl", S=S, seed=13,
                         runs=[Run(None, Tfull, tuple(m * j for j in range(J + 1)))]) for m in ms}
    res = {k: dict(sd_tau=[], sd_F=[], e_tau=[], e_F=[]) for k in ("known", "assume1", "unknown")}
    pm_correct = []
    got = 0
    while got < M:
        p = fam.draw(rng)
        th = fam.sample(p, n, rng)
        kfull = orbit_counts(th, Tfull)
        yfull = observe(kfull, n, sigma, rng)
        y = yfull[[m_true * j for j in range(J + 1)]]
        if not is_live(y, n, sigma):
            continue
        tr = truth_functionals(fam, p)
        lls = {m: loglik(sts[m], y) for m in ms}
        Qf = sts[ms[0]].Q[:, len(fam.pnames):]
        psd = Qf.std(axis=0)
        L_ = np.concatenate([lls[m] for m in ms]) - np.log(len(ms))
        wall = posterior_weights(L_)
        pm_correct.append(float(np.exp(logmeanexp(lls[m_true])) / sum(np.exp(logmeanexp(lls[m])) for m in ms)))
        for key, w, Q_ in (("known", posterior_weights(lls[m_true]), Qf), ("assume1", posterior_weights(lls[1]), Qf),
                           ("unknown", wall, np.vstack([Qf] * len(ms)))):
            pm = w @ Q_
            ps = np.sqrt(np.maximum(w @ Q_ ** 2 - pm ** 2, 0.0))
            res[key]["sd_tau"].append(ps[0] / psd[0])
            res[key]["sd_F"].append(np.median(ps[2:] / psd[2:]))
            res[key]["e_tau"].append((pm[0] - tr[0]) / psd[0])
            res[key]["e_F"].append(np.sqrt(np.mean(((pm[2:] - tr[2:]) / psd[2:]) ** 2)))
        got += 1
    out = {k: dict(sd_tau=float(np.median(v["sd_tau"])), sd_F=float(np.median(v["sd_F"])),
                   rmse_tau=float(np.sqrt(np.mean(np.square(v["e_tau"])))), rmse_F=float(np.sqrt(np.mean(np.square(v["e_F"])))))
           for k, v in res.items()}
    out["p_true_m"] = float(np.mean(pm_correct))
    return out


def observation_model_cell(fam_name, n, s_rel, M, rng, S=800):
    """Multiplicative (log-normal) counting error s_rel, the way crowd counts are wrong, fitted by (a) additive
    Gaussian noise of matched overall size and (b) Gaussian noise proportional to the level.  Returns the
    coverage of the 90% interval for tau and the inside F probes, and the mean posterior sd."""
    fam = FAMILIES[fam_name]
    additive = make_setup(fam_name, n, 0.3 * s_rel, engine="sl", S=S, seed=17)
    relative = make_setup(fam_name, n, 0.003, engine="sl", S=S, seed=17, rel_sigma=s_rel)
    out = {}
    for name, st in (("additive", additive), ("relative", relative)):
        cov_t, cov_F, sd_t = [], [], []
        got = 0
        r2 = np.random.default_rng(int(rng.integers(2 ** 31)))
        while got < M:
            p = fam.draw(r2)
            th = fam.sample(p, n, r2)
            k = orbit_counts(th, 10)
            y = observe(k, n, s_rel, r2, kind="lognorm")
            if y.max() < 3 * 0.3 * s_rel or y.max() * n < 1:
                continue
            w = posterior_weights(loglik(st, y))
            if w is None:
                continue
            Qf = st.Q[:, len(fam.pnames):]
            tr = truth_functionals(fam, p)
            lv = level_hat(y)
            lohi = [wquantile(Qf[:, j], w, (0.05, 0.95)) for j in range(Qf.shape[1])]
            cov_t.append(lohi[0][0] - 1e-9 <= tr[0] <= lohi[0][1] + 1e-9)
            for j, r in enumerate(PROBES):
                if r <= lv:
                    cov_F.append(lohi[2 + j][0] - 1e-9 <= tr[2 + j] <= lohi[2 + j][1] + 1e-9)
            pm = w @ Qf
            sd_t.append(np.sqrt(max(w @ Qf[:, 0] ** 2 - pm[0] ** 2, 0.0)) / Qf[:, 0].std())
            got += 1
        out[name] = dict(cov_tau=float(np.mean(cov_t)), cov_F=float(np.mean(cov_F)), sd_tau=float(np.median(sd_t)),
                         nF=len(cov_F))
    return out


# --------------------------------------------------------------------------------------------------
# summaries and the tasks the report runs (top-level so that a process pool can pickle them)
# --------------------------------------------------------------------------------------------------


def _seed(*key):
    import zlib

    return (SEED + zlib.crc32(repr(key).encode())) % (2 ** 32)


def sbc_summary(res):
    """Plain-number summary of an `sbc_cell` result: calibration of every scored quantity (KS p, central 90%
    coverage and its z-score), of the joint log-likelihood rank, and the information in the posterior (median
    posterior sd / prior sd, RMSE / prior sd) for the parameters, tau, F(0) and F read INSIDE and OUTSIDE the
    support the curve visited."""
    names, u, M = res["names"], res["u"], res["M"]
    nq = len(names)
    ks = np.array([stats.kstest(u[:, j], "uniform").pvalue for j in range(nq)])
    c90 = np.array([np.mean((u[:, j] >= 0.05) & (u[:, j] <= 0.95)) for j in range(nq)])
    z90 = (c90 - 0.9) / np.sqrt(0.09 / M)
    ix = {nm: i for i, nm in enumerate(names)}
    pidx = [i for i, nm in enumerate(names) if nm not in ("tau", "F0") and not nm.startswith("F(")]
    fidx = [i for i, nm in enumerate(names) if nm.startswith("F(")]
    plev = np.array([float(names[i][2:-1]) for i in fidx])
    sdrel = res["ps"] / res["prior_sd"][None, :]
    err = (res["pm"] - res["truth"]) / res["prior_sd"][None, :]
    inside = res["level"][:, None] >= plev[None, :]
    out = dict(M=M, tries=res["tries"], min_ks=float(ks.min()), c90_min=float(c90.min()), c90_max=float(c90.max()),
               z90_max=float(np.max(np.abs(z90))), n_ks_001=int((ks < 0.001).sum()), nq=nq,
               c90_by={nm: float(c) for nm, c in zip(names, c90)})  # per quantity (added at review)
    ull = res["u_ll"]
    out["ll_ks"] = float(stats.kstest(ull, "uniform").pvalue)
    out["ll_c90"] = float(np.mean((ull >= 0.05) & (ull <= 0.95)))
    out["sd_params"] = float(np.mean([np.median(sdrel[:, i]) for i in pidx]))
    out["sd_tau"] = float(np.median(sdrel[:, ix["tau"]]))
    out["sd_F0"] = float(np.median(sdrel[:, ix["F0"]]))
    out["rmse_tau"] = float(np.sqrt(np.mean(err[:, ix["tau"]] ** 2)))
    uf = u[:, fidx]
    for lab, mask in (("in", inside), ("out", ~inside)):
        if mask.sum():
            out[f"sd_F_{lab}"] = float(np.median(sdrel[:, fidx][mask]))
            out[f"rmse_F_{lab}"] = float(np.sqrt(np.mean(err[:, fidx][mask] ** 2)))
            out[f"c90_F_{lab}"] = float(np.mean((uf[mask] >= 0.05) & (uf[mask] <= 0.95)))
        else:
            out[f"sd_F_{lab}"] = out[f"rmse_F_{lab}"] = out[f"c90_F_{lab}"] = float("nan")
        out[f"n_F_{lab}"] = int(mask.sum())
    return out


def task_sbc(spec):
    """One SBC cell.  spec: fam, n, sigma, engine, M, S, size, T, runs (optional), seed key.  setup="mfit" builds the
    synthetic engine with the setup seed of the misspecification cells, so that the cell checks exactly the setup they fit
    with (added at review, 2026-11-01)."""
    fam, n, sigma, engine = spec["fam"], spec["n"], spec["sigma"], spec["engine"]
    setup_seed = _seed("mfit", fam, n) if spec.get("setup") == "mfit" else _seed("setup", fam, n)
    st = make_setup(fam, n, sigma, T=spec.get("T", 10), engine=engine, S=spec.get("S", 2000),
                    seed=setup_seed, size=spec.get("size", "std"), runs=spec.get("runs"))
    rng = np.random.default_rng(_seed("sbc", fam, n, sigma, engine, spec.get("tag", "")))
    res = sbc_cell(st, spec["M"], rng)
    out = dict(spec=spec, G=len(st.P), summary=sbc_summary(res))
    if spec.get("compare_sl"):
        # the synthetic engine on the SAME datasets (same seed, same draws): how far it is from the exact posterior
        st2 = make_setup(fam, n, sigma, T=spec.get("T", 10), engine="sl", S=2000, seed=_seed("setup", fam, n),
                         size=spec.get("size", "std"))
        res2 = sbc_cell(st2, spec["M"], np.random.default_rng(_seed("sbc", fam, n, sigma, engine, spec.get("tag", ""))))
        out["sl_summary"] = sbc_summary(res2)
        ix = {nm: i for i, nm in enumerate(res["names"])}
        same = np.allclose(res["truth"], res2["truth"])
        out["same_data"] = bool(same)
        if same:
            sd = res["prior_sd"]
            out["pm_diff"] = {nm: float(np.mean(np.abs(res["pm"][:, i] - res2["pm"][:, i])) / sd[i]) for nm, i in ix.items()
                              if nm in ("tau", "F0", "F(0.25)", "F(0.55)")}
    return out


def task_misspec(spec):
    n, sigma = spec["n"], spec["sigma"]
    engine = "exact" if sigma == 0 else "sl"
    fits = {f: make_setup(f, n, sigma, engine=engine, S=spec.get("S", 1000), seed=_seed("mfit", f, n), size="fine")
            for f in FITTED}
    out = dict(spec=spec, cells={})
    for gen in spec["gens"]:
        res = misspec_cell(gen, fits, n, sigma, spec["M"], np.random.default_rng(_seed("mis", gen, n, sigma)))
        out["cells"][gen] = dict(M=res["M"], confusion=confusion(res),
                                 mean_ml={f: float(res["ml"][:, i].mean() - res["ml"].max(axis=1).mean())
                                          for i, f in enumerate(res["names"])},
                                 summ={f: misspec_summary(res, f) for f in FITTED})
    return out


def task_twosided(spec):
    fam_names, n, sigma, nu, wbar, M = spec["fams"], spec["n"], spec["sigma"], spec["nu"], spec["wbar"], spec["M"]
    T = 10
    rng = np.random.default_rng(_seed("two", fam_names, n, sigma, nu, wbar))
    m = T + 1
    cvs = {st.__name__: flat_null_critical(st, m, 0.05) for st in (lrt_stat, max_drop_stat)}
    rec = dict(ceiling=[], lrt=[], drop=[], lrt_cum=[], big_decline=[], lrt_one=[], drop_one=[], plateau_growth=[])
    got = 0
    while got < M:
        fam = FAMILIES[fam_names[int(rng.integers(len(fam_names)))]]
        p = fam.draw(rng)
        th, tb = draw_two_sided(fam, p, n, nu, wbar, rng)
        k, ever = orbit_two_sided_ever(th, tb, T)
        if k.max() == 0:
            continue
        got += 1
        y = observe(k, n, sigma, rng)[None, :]
        rec["ceiling"].append(bool((np.diff(k) < 0).any()))
        rec["big_decline"].append(bool(((k[:-1] - k[1:]).max() / n) >= 3 * sigma * np.sqrt(2)))
        rec["lrt"].append(bool(lrt_stat(y, sigma)[0] > cvs["lrt_stat"]))
        rec["drop"].append(bool(max_drop_stat(y, sigma)[0] > cvs["max_drop_stat"]))
        yc = observe(ever, n, sigma, rng)[None, :]
        rec["lrt_cum"].append(bool(lrt_stat(yc, sigma)[0] > cvs["lrt_stat"]))
        rec["plateau_growth"].append(plateau_then_growth(ever))
        # the one-sided control: the same lower thresholds, no upper gates
        k1 = orbit_counts(th, T)
        y1 = observe(k1, n, sigma, rng)[None, :]
        rec["lrt_one"].append(bool(lrt_stat(y1, sigma)[0] > cvs["lrt_stat"]))
        rec["drop_one"].append(bool(max_drop_stat(y1, sigma)[0] > cvs["max_drop_stat"]))
    return dict(spec=spec, rates={k: float(np.mean(v)) for k, v in rec.items() if v}, M=got)


def task_ignition(spec):
    """One ignition cell.  spec: gens, n, sigma, Npairs, designs (dict name -> seeds), fits (family names)."""
    gens, n, sigma = spec["gens"], spec["n"], spec["sigma"]
    designs = spec.get("designs") or {"nat": ()}
    engine = "exact" if sigma == 0 else "sl"
    models = {}
    for dn, seeds in designs.items():
        runs = [Run(None, 10)] + [Run(seed=s_, T=3) for s_ in seeds]
        sts = [make_setup(f, n, sigma, engine=engine, S=spec.get("S", 800), seed=_seed("ig", f, n, dn), size="fine",
                          runs=runs) for f in spec["fits"]]
        models["bma_" + dn] = (Fitted(sts), dn)
    rows = ignition_cell(gens, n, sigma, spec["Npairs"], np.random.default_rng(_seed("igc", gens, n, sigma)),
                         models=models, designs=designs)
    tr = ignition_cell(gens, n, sigma, spec.get("Ntrain", 1500), np.random.default_rng(_seed("igt", gens, n, sigma)))
    lab = np.array([r["label"] for r in rows])
    lab_m = np.array([r["label_mat"] for r in rows])
    rng = np.random.default_rng(_seed("igb", gens, n, sigma))
    out = dict(spec=spec, prev=float(lab.mean()), npos=int(lab.sum()), N=len(rows), prev_mat=float(lab_m.mean()),
               npos_mat=int(lab_m.sum()), auc={}, ci={}, brier={}, auc_mat={}, ci_mat={})
    scores = {"oracle": np.array([r["oracle"] for r in rows]), "probe": np.array([r["probe"] for r in rows])}
    f = fit_logistic(np.array([summary_features(r) for r in tr]), np.array([r["label"] for r in tr], float))
    scores["summary"] = f(np.array([summary_features(r) for r in rows]))
    for name in models:
        scores[name] = np.array([r[name] for r in rows])
    for name, sc in scores.items():
        ok = ~np.isnan(sc)
        out["auc"][name] = auc_score(sc[ok], lab[ok])
        out["ci"][name] = auc_ci(sc[ok], lab[ok], rng, B=200)
        out["auc_mat"][name] = auc_score(sc[ok], lab_m[ok])
        out["ci_mat"][name] = auc_ci(sc[ok], lab_m[ok], rng, B=200)
    for name in models:
        sc = scores[name]
        ok = ~np.isnan(sc)
        out["brier"][name] = brier(sc[ok], lab[ok])
    out["brier"]["base"] = brier(np.full(len(lab), lab.mean()), lab)
    return out


def task_dynamic(spec):
    return dict(spec=spec, res=dynamic_form_cell(spec["fam"], spec["n"], spec["sigma"], spec["M"],
                                                 np.random.default_rng(_seed("dyn", spec["fam"], spec["n"], spec["alpha_true"])),
                                                 spec["alpha_true"]))


def task_subsample(spec):
    return dict(spec=spec, res=subsample_cell(spec["fam"], spec["n"], spec["sigma"], spec["M"],
                                              np.random.default_rng(_seed("sub", spec["fam"], spec["n"], spec["m_true"])),
                                              spec["m_true"]))


def task_obsmodel(spec):
    return dict(spec=spec, res=observation_model_cell(spec["fam"], spec["n"], spec["s_rel"], spec["M"],
                                                      np.random.default_rng(_seed("obs", spec["fam"], spec["n"], spec["s_rel"]))))


def task_dirichlet(spec):
    """Noise-free non-parametric posterior: calibration of F at the probe cells and posterior sd / prior sd of F
    read inside and outside the visited support, for each n."""
    n, M, L = spec["n"], spec["M"], spec.get("L", 300)
    rng = np.random.default_rng(_seed("dir", n))
    dh = DirichletHistogram()
    idx = [int(round(r * dh.B)) for r in PROBES]
    prior_sd = np.cumsum(dh.prior_samples(5000, rng), axis=1)[:, idx].std(axis=0)
    us, rin, rout, got = [], [], [], 0
    while got < M:
        p = dh.sample_prior(rng)
        k = dh.crowd_path(p, n, 12, rng)
        if k.max() == 0:
            continue
        got += 1
        cp = np.cumsum(dh.posterior_samples(k, n, L, rng), axis=1)[:, idx]
        tr = np.cumsum(p)[idx]
        u = (cp < tr).mean(axis=0) + rng.random(len(idx)) * (cp == tr).mean(axis=0)
        us.append(u)
        lvl = k[-1] / n
        for j, r in enumerate(PROBES):
            (rin if r <= lvl else rout).append(cp[:, j].std() / prior_sd[j])
    us = np.array(us)
    return dict(spec=spec, ks=[float(stats.kstest(us[:, j], "uniform").pvalue) for j in range(len(idx))],
                c90=float(np.mean((us >= 0.05) & (us <= 0.95))), sd_in=float(np.median(rin)) if rin else float("nan"),
                sd_out=float(np.median(rout)) if rout else float("nan"), n_in=len(rin), n_out=len(rout))


# --------------------------------------------------------------------------------------------------
# the full run
# --------------------------------------------------------------------------------------------------

def task_visited(spec):
    """How many points of F does a noise-free curve read?  F is read at 0 and at every distinct level of the
    curve (the last of which is the stall), so a curve with d distinct levels reads F at d + 1 points."""
    gen, n, M = FAMILIES[spec["gen"]], spec["n"], spec["M"]
    rng = np.random.default_rng(_seed("vis", spec["gen"], n))
    pts, stall_share, got = [], [], 0
    while got < M:
        th = gen.sample(gen.draw(rng), n, rng)
        k = orbit_counts(th, 60)
        if k[0] == 0:
            continue
        got += 1
        pts.append(len(np.unique(k)) + 1)
        stall_share.append(k[-1] / n)
    pts = np.array(pts)
    return dict(spec=spec, med=float(np.median(pts)), q25=float(np.quantile(pts, 0.25)), q75=float(np.quantile(pts, 0.75)),
                le3=float(np.mean(pts <= 3)), le5=float(np.mean(pts <= 5)), ge8=float(np.mean(pts >= 8)),
                full=float(np.mean(np.array(stall_share) >= 0.999)))


def task_claim14(spec):
    """Replicate models/02 Claim 1.2 (the sandwich, its equal case and its strictness) and 1.4 (necessary condition) on
    random FINITE pairs from our four generators, and count how often two crowds with the same live standalone curve
    merge to opposite outcomes.

    Corrected at review (2026-11-01): the check made in the igniting pairs, that their stalls differ, is Claim 1.2's
    EQUAL case (equal stalls merge to that stall, so never ignite; `equal_bad`), not its strictness, and was reported
    as strictness.  Strictness (unequal stalls merge strictly above the lower one; `strict_bad`) is now checked in the
    sandwich pairs.  The redrawn crowd of the flip experiment is either part, not always the intruder, so the flips are
    also counted for the pairs in which it is the intruder (`flips_intr` of `flip_trials_intr`).  No random number is
    drawn by the added checks, so every earlier count is unchanged."""
    rng = np.random.default_rng(_seed("c14", spec["M"]))
    fams = [FAMILIES[f] for f in ("beta", "clipnorm", "bimodal", "logitnorm")]
    n = spec.get("n", 40)
    ign = equal_bad = nec_bad = 0
    for _ in range(spec["M"]):
        t = []
        for _i in range(2):
            fam = fams[int(rng.integers(4))]
            t.append(fam.sample(fam.draw(rng), n, rng))
        if not ignites(t[0], t[1]):
            continue
        ign += 1
        s_ = [lfp_count(x) / n for x in t]
        if s_[0] > s_[1]:
            t, s_ = t[::-1], s_[::-1]
        M_ = s_[1]
        equal_bad += int(not s_[0] < M_)
        nec_bad += int(not ((t[0] <= M_).mean() > M_ and (t[0] < M_).mean() >= M_))
    flips = trials = flips_intr = trials_intr = 0
    for _ in range(spec["M"] // 4):
        a = fams[1].sample(fams[1].draw(rng), n, rng)
        ka = orbit_counts(a, 12)
        if ka[0] == 0 or ka[-1] > 0.75 * n:
            continue
        h_f = fams[int(rng.integers(4))]
        h = h_f.sample(h_f.draw(rng), n, rng)
        a2 = redraw_above_stall(a, rng)
        assert (orbit_counts(a2, 12) == ka).all()
        trials += 1
        flip = int(ignites(a, h) != ignites(a2, h))
        flips += flip
        if lfp_count(a) < lfp_count(h):  # equal sizes: the redrawn crowd is the intruder
            trials_intr += 1
            flips_intr += flip
    # the sandwich of Claim 1.2: lower <= merged stall <= upper, and is its upper end fixed by the parts' curves?
    sand_bad = up_trials = up_chg = up_big = strict_trials = strict_bad = 0
    n2 = spec.get("n_sandwich", 200)
    for _ in range(spec["M"] // 10):
        t = []
        for _i in range(2):
            fam = fams[int(rng.integers(4))]
            t.append(fam.sample(fam.draw(rng), n2, rng))
        if any(orbit_counts(x, 12)[0] == 0 or lfp_count(x) >= 0.97 * n2 for x in t):
            continue
        u1 = common_prefixed_point(*t)
        km, nm = merged_stall(*t)
        lo = min(lfp_count(t[0]) / n2, lfp_count(t[1]) / n2)
        sand_bad += int(not (lo - 1e-12 <= km / nm <= u1 + 1e-12))
        k_lo, k_hi = sorted((lfp_count(t[0]), lfp_count(t[1])))
        if k_lo != k_hi:  # strictness: the merge stalls strictly above the lower stall (exact integers)
            strict_trials += 1
            strict_bad += int(not km * n2 > nm * k_lo)
        t2 = [redraw_above_stall(x, rng) for x in t]
        u2 = common_prefixed_point(*t2)
        up_trials += 1
        up_chg += int(u1 != u2)
        up_big += int(abs(u1 - u2) > 0.05)
    return dict(spec=spec, pairs=spec["M"], igniting=ign, equal_bad=equal_bad, nec_bad=nec_bad, flip_trials=trials,
                flips=flips, flip_trials_intr=trials_intr, flips_intr=flips_intr, sand_bad=sand_bad,
                strict_trials=strict_trials, strict_bad=strict_bad, up_trials=up_trials, up_chg=up_chg, up_big=up_big)


DESIGNS = {"nat": (), "p1": (0.5,), "p2": (0.35, 0.7), "p4": (0.2, 0.4, 0.6, 0.8)}


def build_specs(quick=False):
    """Every task of the report as (kind, spec).  quick=True shrinks the sample sizes for a smoke run."""
    Mb = 1000 if not quick else 120
    Ml = 200 if not quick else 24
    Ml100 = 40 if not quick else 6
    tasks = []
    for fam in ("beta", "clipnorm"):
        for n in (30, 100, 300, 1000, 3000):
            tasks.append(("sbc", dict(fam=fam, n=n, sigma=0.0, engine="exact", M=Mb)))
        for sigma in (0.01, 0.03, 0.1):
            tasks.append(("sbc", dict(fam=fam, n=30, sigma=sigma, engine="lattice", M=Ml, compare_sl=True)))
        for sigma in (0.03, 0.1):
            tasks.append(("sbc", dict(fam=fam, n=100, sigma=sigma, engine="lattice", M=Ml100, compare_sl=True)))
        for n in (100, 300, 1000, 3000):
            for sigma in (0.01, 0.03, 0.1):
                tasks.append(("sbc", dict(fam=fam, n=n, sigma=sigma, engine="sl", M=Mb)))
        for dn, seeds in DESIGNS.items():
            runs = [Run(None, 10)] + [Run(seed=s_, T=3) for s_ in seeds]
            for sigma in (0.03, 0.1):
                tasks.append(("sbc", dict(fam=fam, n=1000, sigma=sigma, engine="sl", M=Mb, runs=runs, tag="design-" + dn,
                                          design=dn)))
    Mm = 400 if not quick else 40
    for n, sigma in [(100, 0.0), (1000, 0.0), (3000, 0.0)] + [(n, sg) for n in (300, 1000, 3000) for sg in (0.01, 0.03, 0.1)]:
        tasks.append(("misspec", dict(n=n, sigma=sigma, M=Mm, gens=("beta", "clipnorm", "bimodal", "logitnorm"))))
    # added at review (2026-11-01): SBC of exactly the setups the misspecification cells fit with when sigma > 0 (fine grids,
    # S = 1,000, their setup seeds), the truth drawn on the fine grid.  No SBC cell had checked them.
    for fam in FITTED:
        for n in (300, 1000, 3000):
            for sigma in (0.01, 0.03, 0.1):
                tasks.append(("sbc", dict(fam=fam, n=n, sigma=sigma, engine="sl", M=Mm, S=1000, size="fine", setup="mfit",
                                          tag="mfit")))
    Mt = 500 if not quick else 60
    for nu, wbar in [(0.1, 0.5), (0.3, 0.5), (0.6, 0.5), (0.3, 0.15)]:
        for n in (100, 1000):
            for sigma in (0.01, 0.03, 0.1):
                tasks.append(("twosided", dict(fams=("beta", "clipnorm"), n=n, sigma=sigma, nu=nu, wbar=wbar, M=Mt)))
    Np = 2000 if not quick else 150
    for gens in (("beta", "clipnorm"), ("bimodal", "logitnorm")):
        for n in (100, 300, 1000, 3000):
            for sigma in (0.0, 0.03):
                tasks.append(("ignition", dict(gens=gens, fits=("beta", "clipnorm"), n=n, sigma=sigma, Npairs=Np,
                                               Ntrain=Np)))
        for sigma in (0.03, 0.1):
            tasks.append(("ignition", dict(gens=gens, fits=("beta", "clipnorm"), n=1000, sigma=sigma, Npairs=Np,
                                           Ntrain=Np, designs=DESIGNS)))
    Md = 300 if not quick else 40
    for fam in ("clipnorm", "beta"):
        for sigma in (0.03, 0.1):
            for at in (0.25, 0.5, 0.75, 1.0):
                tasks.append(("dynamic", dict(fam=fam, n=1000, sigma=sigma, M=Md, alpha_true=at)))
        for m_true in (1, 2, 3):
            tasks.append(("subsample", dict(fam=fam, n=1000, sigma=0.03, M=Md, m_true=m_true)))
        for s_rel in (0.1, 0.3):
            tasks.append(("obsmodel", dict(fam=fam, n=1000, s_rel=s_rel, M=Md)))
    for n in (30, 100, 300, 1000, 3000, 10000):
        tasks.append(("dirichlet", dict(n=n, M=400 if not quick else 40)))
    for gen in ("beta", "clipnorm", "bimodal", "logitnorm"):
        for n in (100, 1000):
            tasks.append(("visited", dict(gen=gen, n=n, M=1000 if not quick else 100)))
    tasks.append(("claim14", dict(M=20000 if not quick else 2000)))
    return tasks


_TASK_FN = {"claim14": task_claim14, "visited": task_visited, "sbc": task_sbc, "misspec": task_misspec, "twosided": task_twosided, "ignition": task_ignition,
            "dynamic": task_dynamic, "subsample": task_subsample, "obsmodel": task_obsmodel, "dirichlet": task_dirichlet}


def _run_task(kt):
    kind, spec = kt
    return kind, _TASK_FN[kind](spec)


def _task_key(kt):
    import hashlib

    kind, spec = kt
    return kind + "-" + hashlib.sha1(repr((kind, sorted(spec.items(), key=lambda kv: kv[0]))).encode()).hexdigest()[:16]


def run_all(quick=False, workers=6, log=print, cache=None, only=None, select=None):
    """Run every task (in a process pool, seeded per task so the output does not depend on scheduling).  `cache`
    is an optional directory: finished tasks are pickled there and reused, which lets a long run be resumed or
    extended without recomputing (the numbers are identical because every task seeds itself)."""
    import multiprocessing as mp
    import pickle
    from concurrent.futures import as_completed

    tasks = build_specs(quick)
    if only:
        tasks = [t for t in tasks if t[0] in only]
    if select:
        tasks = [t for t in tasks if select(*t)]
    cost = {"sbc": lambda sp: 600 if sp["engine"] == "lattice" and sp["n"] >= 100 else 60 if sp["engine"] == "lattice" else 5,
            "misspec": lambda sp: 20, "twosided": lambda sp: 3, "ignition": lambda sp: 60 if sp.get("designs") else 40,
            "dynamic": lambda sp: 5, "subsample": lambda sp: 5, "obsmodel": lambda sp: 5, "dirichlet": lambda sp: 5,
            "visited": lambda sp: 3, "claim14": lambda sp: 30}
    results = [None] * len(tasks)
    todo = []
    for i, t in enumerate(tasks):
        f = Path(cache) / (_task_key(t) + ".pkl") if cache else None
        if f is not None and f.exists():
            results[i] = pickle.load(open(f, "rb"))
        else:
            todo.append(i)
    log(f"  {len(tasks) - len(todo)} cached, {len(todo)} to run")
    order = sorted(todo, key=lambda i: -cost[tasks[i][0]](tasks[i][1]))
    if order:
        with ProcessPoolExecutor(max_workers=workers, mp_context=mp.get_context("fork")) as ex:
            futs = {ex.submit(_run_task, tasks[i]): i for i in order}
            done = 0
            for f in as_completed(futs):
                i = futs[f]
                results[i] = f.result()
                if cache:
                    Path(cache).mkdir(parents=True, exist_ok=True)
                    pickle.dump(results[i], open(Path(cache) / (_task_key(tasks[i]) + ".pkl"), "wb"))
                done += 1
                if done % 10 == 0 or done == len(order):
                    log(f"  {done}/{len(order)} tasks done")
    return results
