#!/usr/bin/env python
"""D609 exploratory numerics: merge (mixture) and split (conditioning) of Granovetter threshold crowds.

Direction D609 (docs/research-map.md, cluster Y).  Definitions (models/00-v0.md 2.3, 4.4, Thm 6.3;
docs/prior-work/066 sections 1-3):

  * a crowd of n members has thresholds theta_i in [0,1]; F(r) = #{i : theta_i <= r} / n;
  * dynamics r(t+1) = F[r(t)] from r(0) = F(0); equilibrium r* = lfp(F), written tau(F);
  * MERGE of (n1,F1), (n2,F2): the mixture F_m = lam F1 + (1-lam) F2, lam = n1/(n1+n2)
    (the union of the two threshold lists, thresholds kept as FRACTIONS of the crowd);
  * SPLIT by a rule on members: the conditional CDFs of the two parts (same thresholds,
    new denominators).  A split is a merge read backwards: F is the mixture of its parts.

Everything is EXACT: thresholds are integers over a fixed grid, theta = a / D, so every
comparison "theta <= k/N" is the integer comparison a*N <= k*D, and equilibria are Fractions.
Nothing here is a proof; section "Statements" of the report separates what has a short proof
(given in the report), what a counterexample refutes, and what is only observed.

Run (from sim/):   ~/.local/bin/uv run --frozen python explore/mixture_equilibria.py [--quick]
Writes:            sim/results/mixture_equilibria.md   (deterministic for a given --seed)
Touches nothing else.  numpy only (plus models/certificates.py, read-only, for section H).
"""
from __future__ import annotations

import argparse
import multiprocessing as mp
import sys
import time
from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations_with_replacement
from pathlib import Path

import numpy as np

SIM = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SIM))

D = 10**7  # threshold grid: theta = a / D, integer a in [0, D]; a = 0 instigator, a = D "never"


# =========================================================================================
# exact core
# =========================================================================================

def lfp_count(a: np.ndarray, d: int = D) -> int:
    """Smallest k in 0..n with #{i : a_i * n <= k * d} <= k.

    For a monotone F on the grid {0, 1/n, ..., 1} the least pre-fixed point is the least fixed
    point (v0.1 Thm 6.3), so k/n = tau(F).  Vectorised over k; `a` is a sorted int64 array."""
    n = a.size
    k = np.arange(n + 1, dtype=np.int64)
    cnt = np.searchsorted(a, (k * d) // n, side="right")  # a_i <= floor(k d / n)  <=>  a_i n <= k d
    return int(np.argmax(cnt <= k))


def lfp_orbit_count(a: np.ndarray, d: int = D) -> int:
    """The DEFINITION: r(0) = F(0), r(t+1) = F[r(t)] in count space, run to the repeat."""
    n = a.size
    k = int(np.searchsorted(a, 0, side="right"))
    while True:
        k2 = int(np.searchsorted(a, (k * d) // n, side="right"))
        if k2 == k:
            return k
        k = k2


def F_count(a: np.ndarray, p: int, q: int, d: int = D) -> int:
    """Number of members with theta <= p/q (exact)."""
    return int(np.searchsorted(a, (p * d) // q, side="right"))


def tau(a: np.ndarray) -> Fraction:
    return Fraction(lfp_count(a), a.size)


def tau_max_pair(a1: np.ndarray, a2: np.ndarray) -> Fraction:
    """lfp(max(F1,F2)) = the least COMMON pre-fixed point min(P1 & P2), P_i = {r : F_i(r) <= r}.

    A fixed point of max(F1,F2) is a value of F1 or F2, so it lies on the grid (1/n1)Z or
    (1/n2)Z; test both grids exactly."""
    n1, n2 = a1.size, a2.size
    k = np.arange(n1 + 1, dtype=np.int64)
    q = (k * D) // n1
    c11 = np.searchsorted(a1, q, side="right")
    c21 = np.searchsorted(a2, q, side="right")
    ok = (c11 <= k) & (c21 * n1 <= k * n2)
    best = Fraction(int(np.argmax(ok)), n1)
    k = np.arange(n2 + 1, dtype=np.int64)
    q = (k * D) // n2
    c12 = np.searchsorted(a1, q, side="right")
    c22 = np.searchsorted(a2, q, side="right")
    ok = (c22 <= k) & (c12 * n2 <= k * n1)
    cand = Fraction(int(np.argmax(ok)), n2)
    return min(best, cand)


def orbit_general(a1: np.ndarray, a2: np.ndarray, step) -> Fraction:
    """Independent check: exact orbit of r -> step(F1(r), F2(r)) from 0 (Fractions)."""
    r = Fraction(0)
    while True:
        f1 = Fraction(F_count(a1, r.numerator, r.denominator), a1.size)
        f2 = Fraction(F_count(a2, r.numerator, r.denominator), a2.size)
        r2 = step(f1, f2)
        if r2 == r:
            return r
        r = r2


def mix_orbit(a1: np.ndarray, a2: np.ndarray, lam: Fraction) -> Fraction:
    """Exact orbit of the mixture lam*F1 + (1-lam)*F2 for ANY rational lam (no replication)."""
    return orbit_general(a1, a2, lambda f1, f2: lam * f1 + (1 - lam) * f2)


def category(k: int, n: int, z: int) -> str:
    """D dormant (no instigators, tau = 0); F full (tau = 1); I inert (tau = F(0) > 0: the
    instigators recruit nobody); P partial cascade (F(0) < tau < 1)."""
    if z == 0:
        return "D"
    if k == n:
        return "F"
    if k == z:
        return "I"
    return "P"


# =========================================================================================
# A. exhaustive small cases (pure python, no sampling)
# =========================================================================================

def lfp_small(ts, K):
    n = len(ts)
    k = sum(1 for t in ts if t == 0)
    while True:
        k2 = sum(1 for t in ts if t * n <= k * K)
        if k2 == k:
            return Fraction(k, n)
        k = k2


def F_small(ts, K, r: Fraction) -> Fraction:
    return Fraction(sum(1 for t in ts if t * r.denominator <= r.numerator * K), len(ts))


def tau_max_small(c1, c2, K) -> Fraction:
    n1, n2 = len(c1), len(c2)
    cands = sorted({Fraction(k, n1) for k in range(n1 + 1)} | {Fraction(k, n2) for k in range(n2 + 1)})
    for r in cands:
        if F_small(c1, K, r) <= r and F_small(c2, K, r) <= r:
            return r
    raise AssertionError


def analyse_small(c1, c2, K) -> dict:
    """Pure-python re-derivation of the fields of analyse_pair (no numpy, thresholds as ints over K)."""
    n1, n2 = len(c1), len(c2)
    N = n1 + n2
    cm = tuple(sorted(c1 + c2))
    t1, t2, tm = lfp_small(c1, K), lfp_small(c2, K), lfp_small(cm, K)
    z1, z2 = c1.count(0), c2.count(0)
    z = z1 + z2
    if t1 < t2:
        latent = F_small(c1, K, t2) > t2
    elif t2 < t1:
        latent = F_small(c2, K, t1) > t1
    else:
        latent = False
    pos = min((x for x in cm if x > 0), default=None)
    return dict(t1=t1, t2=t2, tm=tm, tmx=tau_max_small(c1, c2, K), latent=latent,
                pred=pos is not None and pos * N <= z * K, act=tm > Fraction(z, N),
                c1=category(int(t1 * n1), n1, z1), c2=category(int(t2 * n2), n2, z2), z1=z1, z2=z2, N=N)


def selfcheck(seed: int, trials: int) -> tuple[int, int]:
    """Compare the numpy/Fraction path (analyse_pair) with the pure-python path on random small crowds
    whose thresholds lie on a grid of 1/K, K = 100 (which divides D).  Returns (trials, disagreements)."""
    rng = np.random.default_rng(seed)
    K = 100
    unit = D // K
    bad = 0
    for _ in range(trials):
        cs = []
        for _ in range(2):
            n = int(rng.integers(1, 26))
            al, be = np.exp(rng.uniform(np.log(0.3), np.log(4), 2))
            t = np.rint(K * rng.beta(al, be, n)).astype(int)
            t[rng.random(n) < rng.choice([0.0, 0.05, 0.2])] = 0
            t[rng.random(n) < rng.choice([0.0, 0.1, 0.3])] = K
            cs.append(tuple(sorted(int(x) for x in t)))
        a1, a2 = (np.array(c, dtype=np.int64) * unit for c in cs)
        r, q = analyse_pair(a1, a2), analyse_small(cs[0], cs[1], K)
        if any(r[k] != q[k] for k in ("t1", "t2", "tm", "tmx", "latent", "pred", "act", "c1", "c2", "z1", "z2", "N")):
            bad += 1
    return trials, bad


def below_eq(c1, c2, K) -> bool:
    """F_{c1} <= F_{c2} pointwise (check at every breakpoint; both are step functions)."""
    n1, n2 = len(c1), len(c2)
    for x in set(c1) | set(c2) | {0}:
        a = sum(1 for t in c1 if t <= x)
        b = sum(1 for t in c2 if t <= x)
        if a * n2 > b * n1:
            return False
    return True


def exhaustive(K: int, nmax: int):
    """All unordered pairs of crowds with 1..nmax members and thresholds in {0, 1/K, ..., 1}."""
    crowds = []
    for n in range(1, nmax + 1):
        crowds += list(combinations_with_replacement(range(K + 1), n))
    info = {}
    for c in crowds:
        z = c.count(0)
        pos = min((t for t in c if t > 0), default=None)
        info[c] = (len(c), z, pos, lfp_small(c, K))
    cnt = Counter()
    first: dict[str, tuple] = {}  # statement -> minimal example (by merged size, then tuples)

    def note(key, N, c1, c2, extra):
        cur = first.get(key)
        cand = (N, len(c1), c1, c2)
        if cur is None or cand < cur[0]:
            first[key] = (cand, extra)

    for i, c1 in enumerate(crowds):
        n1, z1, p1, t1 = info[c1]
        for c2 in crowds[i:]:
            n2, z2, p2, t2 = info[c2]
            cm = tuple(sorted(c1 + c2))
            N = n1 + n2
            tm = lfp_small(cm, K)
            lam = Fraction(n1, N)
            avg = lam * t1 + (1 - lam) * t2
            lo, hi = min(t1, t2), max(t1, t2)
            tmx = tau_max_small(c1, c2, K)
            cnt["pairs"] += 1
            ex = (t1, t2, tm)
            if tm < lo:
                cnt["below_min"] += 1; note("below_min", N, c1, c2, ex)
            if tm > hi:
                cnt["ign"] += 1; note("ign", N, c1, c2, ex)
            if tm < avg:
                cnt["lt_avg"] += 1; note("lt_avg", N, c1, c2, ex)
            if tm > avg:
                cnt["gt_avg"] += 1; note("gt_avg", N, c1, c2, ex)
            if tm > tmx:
                cnt["above_tmax"] += 1
            if tm == tmx:
                cnt["eq_tmax"] += 1
            # latent pressure: F_low(tau_high) > tau_high
            if t1 < t2:
                latent = F_small(c1, K, t2) > t2
            elif t2 < t1:
                latent = F_small(c2, K, t1) > t1
            else:
                latent = False
            if latent:
                cnt["latent"] += 1
            if tm > hi and not latent:
                cnt["ign_no_latent"] += 1
            if latent and tm > hi:
                cnt["latent_and_ign"] += 1
            # first step
            z = z1 + z2
            pos = min([p for p in (p1, p2) if p is not None], default=None)
            pred = pos is not None and pos * N <= z * K
            act = tm > Fraction(z, N)
            if pred != act:
                cnt["firststep_mismatch"] += 1
            for (n_, z_, p_, t_) in ((n1, z1, p1, t1), (n2, z2, p2, t2)):
                if (p_ is not None and p_ * n_ <= z_ * K) != (t_ > Fraction(z_, n_)):
                    cnt["firststep_mismatch_part"] += 1
            norec1 = t1 == Fraction(z1, n1)
            norec2 = t2 == Fraction(z2, n2)
            if norec1 and norec2:
                cnt["norec_pairs"] += 1
                if tm < avg:
                    cnt["norec_below_avg_viol"] += 1
            if norec1 and norec2 and act:
                cnt["created"] += 1; note("created", N, c1, c2, ex)
            live = z1 > 0 and z2 > 0
            if live and tm < avg:
                cnt["lt_avg_live"] += 1; note("lt_avg_live", N, c1, c2, ex)
            if live and tm > avg:
                cnt["gt_avg_live"] += 1; note("gt_avg_live", N, c1, c2, ex)
            if live and tm > hi:
                cnt["ign_live"] += 1; note("ign_live", N, c1, c2, ex)
            if tm == 1 and t1 < 1 and t2 < 1:
                cnt["kill_full"] += 1; note("kill_full", N, c1, c2, ex)
                if live:
                    cnt["kill_full_live"] += 1; note("kill_full_live", N, c1, c2, ex)
            if norec1 and norec2 and act and live and t1 < 1 and t2 < 1:
                cnt["created_strict"] += 1; note("created_strict", N, c1, c2, ex)
            if t1 == 1 and t2 == 1:
                cnt["both_full"] += 1
                if tm != 1:
                    cnt["both_full_viol"] += 1
            if z1 == 0 and z2 == 0:
                cnt["both_dormant"] += 1
                if tm > 0:
                    cnt["both_dormant_viol"] += 1
            if (z1 == 0) != (z2 == 0):
                cnt["dormant_plus_live"] += 1
                if tm == 0:
                    cnt["dormant_plus_live_dead"] += 1
            # monotonicity, both orders
            for (u, v, tu, tv) in ((c1, c2, t1, t2), (c2, c1, t2, t1)):
                if below_eq(u, v, K):
                    cnt["ordered"] += 1
                    if tu > tv:
                        cnt["ordered_viol"] += 1
                    # and the merge of an ordered pair is between them
                    if not (tu <= tm <= tv):
                        cnt["ordered_between_viol"] += 1
    return cnt, first


# =========================================================================================
# B. random crowds: families (thresholds as integers over the grid D)
# =========================================================================================

GRAN_N = [10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000, 2000, 5000, 10000]  # all divide D
assert all(D % g == 0 for g in GRAN_N)
BASE_FAMS = ["uniform", "beta", "bimodal", "normal", "atoms", "gran", "full"]
SIZED_FAMS = [f for f in BASE_FAMS if f != "gran"]   # families that honour the requested n


def rand_n(rng) -> int:
    return int(round(np.exp(rng.uniform(np.log(10), np.log(10_000)))))


def _zw(rng):
    """Instigator share z (0 with prob .25) and never-join share w (0 with prob .5)."""
    z = 0.0 if rng.random() < 0.25 else float(np.exp(rng.uniform(np.log(0.003), np.log(0.3))))
    w = 0.0 if rng.random() < 0.5 else float(rng.uniform(0.0, 0.4))
    return z, w


def _finish(x, z, w, rng, n):
    """Continuous draws x in (0,1) -> grid thresholds; strictly positive unless an instigator."""
    a = np.clip(np.floor(x * D), 1, D).astype(np.int64)
    u = rng.random(n)
    a[u < z] = 0
    a[(u >= z) & (u < z + w)] = D
    return np.sort(a)


def make_dist(fam: str, rng):
    """-> (draw(n, rng) -> sorted int64 thresholds, label).  Parameters fixed at creation."""
    if fam == "uniform":
        lo = rng.uniform(0, 0.7); hi = rng.uniform(lo + 0.05, 1.0); z, w = _zw(rng)
        return (lambda n, r: _finish(r.uniform(lo, hi, n), z, w, r, n),
                f"uniform[{lo:.2f},{hi:.2f}] z={z:.3f} w={w:.2f}")
    if fam == "beta":
        al, be = np.exp(rng.uniform(np.log(0.3), np.log(8), 2)); z, w = _zw(rng)
        return (lambda n, r: _finish(r.beta(al, be, n), z, w, r, n),
                f"beta({al:.2f},{be:.2f}) z={z:.3f} w={w:.2f}")
    if fam == "bimodal":
        p = rng.uniform(0.2, 0.8); k1, k2 = np.exp(rng.uniform(np.log(5), np.log(60), 2))
        m1 = rng.uniform(0.03, 0.35); m2 = rng.uniform(0.45, 0.95); z, w = _zw(rng)

        def draw(n, r):
            pick = r.random(n) < p
            x = np.where(pick, r.beta(m1 * k1, (1 - m1) * k1, n), r.beta(m2 * k2, (1 - m2) * k2, n))
            return _finish(x, z, w, r, n)
        return draw, f"bimodal(p={p:.2f}; m={m1:.2f},{m2:.2f}; k={k1:.0f},{k2:.0f}) z={z:.3f} w={w:.2f}"
    if fam == "normal":
        mu = rng.uniform(0.1, 0.5); sg = float(np.exp(rng.uniform(np.log(0.02), np.log(0.4))))

        def draw(n, r):
            x = r.normal(mu, sg, n)
            a = np.clip(np.floor(x * D), 1, D - 1).astype(np.int64)
            a[x <= 0] = 0
            a[x >= 1] = D
            return np.sort(a)
        return draw, f"normal(mu={mu:.2f}, sd={sg:.3f}) clipped"
    if fam == "atoms":
        k = int(rng.integers(1, 5)); loc = np.sort(rng.uniform(0.001, 1.0, k))
        wt = rng.dirichlet(np.ones(k)); z, w = _zw(rng)

        def draw(n, r):
            x = loc[r.choice(k, n, p=wt)]
            return _finish(x, z, w, r, n)
        return draw, "atoms(" + ",".join(f"{l:.3f}:{q:.2f}" for l, q in zip(loc, wt)) + f") z={z:.3f} w={w:.2f}"
    if fam == "gran":
        nG = int(rng.choice(GRAN_N)); unit = D // nG; u = rng.random()
        moves = []
        if u < 0.25:
            kind = "G0"
        elif u < 0.5 and nG >= 3:
            kind = "G1"
        else:
            kind = "Gpert"
            moves = [(int(rng.integers(0, nG)), int(rng.choice([-2, -1, 1, 2]))) for _ in range(int(rng.integers(1, 4)))]

        def draw(n, r):
            j = np.arange(nG)
            if kind == "G1":
                j[1] = 2
            for i, s in moves:
                j[i] = min(max(j[i] + s, 0), nG)
            return np.sort(j * unit)
        return draw, f"{kind}(n={nG})" + (f" moves={moves}" if moves else "")
    if fam == "full":
        s = float(np.exp(rng.uniform(np.log(1e-3), np.log(1.0))))

        def draw(n, r):
            k = np.arange(n, dtype=np.int64)
            x = np.floor((k / n) * (1 - s * r.random(n)) * D).astype(np.int64)
            return np.sort(np.minimum(x, (k * D) // n))  # theta_k <= k/n exactly  =>  tau = 1
        return draw, f"full(slack={s:.3f})"
    raise ValueError(fam)


def draw_pair(scen: str, rng):
    """-> (a1, label1, a2, label2) for a scenario name."""
    if scen == "mixed":
        f1, f2 = rng.choice(BASE_FAMS), rng.choice(BASE_FAMS)
    elif scen == "sameG":
        f1 = f2 = rng.choice(["uniform", "beta", "bimodal", "normal"])
    else:
        f1 = f2 = scen
    d1, l1 = make_dist(f1, rng)
    if scen == "sameG":
        d2, l2 = d1, l1
    else:
        d2, l2 = make_dist(f2, rng)
    n1, n2 = rand_n(rng), rand_n(rng)
    return d1(n1, rng), l1, d2(n2, rng), l2


# -----------------------------------------------------------------------------------------

def analyse_pair(a1: np.ndarray, a2: np.ndarray) -> dict:
    """Everything the report tabulates about merging crowds a1 and a2 (sorted int arrays)."""
    n1, n2 = a1.size, a2.size
    N = n1 + n2
    am = np.sort(np.concatenate((a1, a2)))
    k1, k2, km = lfp_count(a1), lfp_count(a2), lfp_count(am)
    t1, t2, tm = Fraction(k1, n1), Fraction(k2, n2), Fraction(km, N)
    z1 = int(np.searchsorted(a1, 0, side="right")); z2 = int(np.searchsorted(a2, 0, side="right"))
    z = z1 + z2
    lam = Fraction(n1, N)
    avg = lam * t1 + (1 - lam) * t2
    lo, hi = min(t1, t2), max(t1, t2)
    tmx = tau_max_pair(a1, a2)
    if t1 < t2:
        latent = F_count(a1, k2, n2) * n2 > k2 * n1
    elif t2 < t1:
        latent = F_count(a2, k1, n1) * n1 > k1 * n2
    else:
        latent = False
    apos = int(am[z]) if z < N else None
    pred = apos is not None and apos * N <= z * D
    return dict(n1=n1, n2=n2, N=N, t1=t1, t2=t2, tm=tm, lam=lam, avg=avg, lo=lo, hi=hi, tmx=tmx,
                z1=z1, z2=z2, latent=latent, pred=pred, act=km > z,
                c1=category(k1, n1, z1), c2=category(k2, n2, z2),
                norec1=(k1 == z1), norec2=(k2 == z2), km=km, z=z)


class Tally:
    """Counts for one scenario.  Keys named viol_* are statements with a proof: expected 0."""

    def __init__(self):
        self.c = Counter()
        self.cat = defaultdict(Counter)   # sorted category pair -> counts
        self.nb = defaultdict(Counter)    # size bucket of N -> counts
        self.over = []                    # tm - hi for ignition draws
        self.dav = []                     # float(tm - avg)
        self.ex = {}                      # key -> (score, description)

    def add(self, r: dict, label):
        c = self.c
        c["pairs"] += 1
        tm, lo, hi, avg = r["tm"], r["lo"], r["hi"], r["avg"]
        ign = tm > hi
        cp = "".join(sorted((r["c1"], r["c2"])))
        b = self.nb["N<100" if r["N"] < 100 else "100-999" if r["N"] < 1000 else "1000-9999" if r["N"] < 10000 else ">=10000"]
        b["pairs"] += 1
        if cp not in ("DD", "FF"):
            b["elig"] += 1
        if cp in ("DI", "DP", "II", "IP", "PP"):
            b["elig_ign"] += 1
        cc = self.cat[cp]
        cc["pairs"] += 1
        if tm < lo:
            c["viol_below_min"] += 1
        if ign:
            c["ign"] += 1; cc["ign"] += 1; b["ign"] += 1
            self.over.append(float(tm - hi))
            self._best("ign", float(tm - hi), r, label)
        elif tm == hi:
            c["at_max"] += 1
        else:
            c["between"] += 1
        if tm > r["tmx"]:
            c["viol_above_tmax"] += 1
        if tm == r["tmx"]:
            c["eq_tmax"] += 1
        if r["tmx"] > hi:
            c["tmax_above_max"] += 1
        if tm < avg:
            c["lt_avg"] += 1; cc["lt_avg"] += 1; b["lt_avg"] += 1
            self._best("lt_avg", float(avg - tm), r, label)
        elif tm > avg:
            c["gt_avg"] += 1; cc["gt_avg"] += 1; b["gt_avg"] += 1
            self._best("gt_avg", float(tm - avg), r, label)
        else:
            c["eq_avg"] += 1
        self.dav.append(float(tm - avg))
        if r["latent"]:
            c["latent"] += 1
            if ign:
                c["latent_and_ign"] += 1
        if ign and not r["latent"]:
            c["viol_ign_without_latent"] += 1
        if r["pred"] != r["act"]:
            c["viol_firststep"] += 1
        if r["norec1"] and r["norec2"]:
            c["norec_pairs"] += 1
            if tm < avg:
                c["viol_norec_below_avg"] += 1       # M10: parts that recruit nobody merge to >= the average
        if r["norec1"] and r["norec2"] and r["act"]:
            c["created"] += 1
            if r["z1"] > 0 and r["z2"] > 0 and r["t1"] < 1 and r["t2"] < 1:
                c["created_live"] += 1
            self._best("created", float(tm - Fraction(r["z"], r["N"])), r, label)
        if r["t1"] == 1 and r["t2"] == 1:
            c["both_full"] += 1
            if tm != 1:
                c["viol_both_full"] += 1
        if r["z1"] == 0 and r["z2"] == 0:
            c["both_dormant"] += 1
            if tm > 0:
                c["viol_both_dormant"] += 1
        if (r["z1"] == 0) != (r["z2"] == 0):
            c["dormant_plus_live"] += 1
            if tm == 0:
                c["dormant_plus_live_dead"] += 1

    def _best(self, key, score, r, label):
        cur = self.ex.get(key)
        if cur is None or score > cur[0]:
            self.ex[key] = (score, dict(n1=r["n1"], n2=r["n2"], t1=r["t1"], t2=r["t2"], tm=r["tm"],
                                        lam=r["lam"], avg=r["avg"], label=label))


def verify_sample(a1, a2) -> int:
    """Independent re-computation by exact orbits; returns the number of disagreements (0 expected)."""
    n1, n2 = a1.size, a2.size
    am = np.sort(np.concatenate((a1, a2)))
    bad = 0
    km = lfp_count(am)
    if lfp_orbit_count(am) != km or lfp_orbit_count(a1) != lfp_count(a1) or lfp_orbit_count(a2) != lfp_count(a2):
        bad += 1
    lam = Fraction(n1, n1 + n2)
    if mix_orbit(a1, a2, lam) != Fraction(km, n1 + n2):
        bad += 1
    if orbit_general(a1, a2, max) != tau_max_pair(a1, a2):
        bad += 1
    if orbit_general(a1, a2, min) != min(tau(a1), tau(a2)):
        bad += 1
    return bad


def run_scenario(args):
    scen, seed, pairs, nverify = args
    rng = np.random.default_rng(seed)
    t = Tally()
    bad = 0
    nv = 0
    for _ in range(pairs):
        a1, l1, a2, l2 = draw_pair(scen, rng)
        t.add(analyse_pair(a1, a2), (l1, l2))
        if nv < nverify and a1.size + a2.size <= 600:
            bad += verify_sample(a1, a2); nv += 1
    t.c["verified"] = nv
    t.c["verify_bad"] = bad
    return scen, t


# =========================================================================================
# C. ordered pairs: F1 <= F2 pointwise  =>  tau1 <= tau_m <= tau2   (monotonicity, and betweenness)
# =========================================================================================

def run_monotone(seed: int, trials: int) -> Counter:
    rng = np.random.default_rng(seed)
    c = Counter()
    for _ in range(trials):
        fam = str(rng.choice(BASE_FAMS))
        d, _ = make_dist(fam, rng)
        a = d(rand_n(rng), rng)
        q = int(rng.choice([1, 1, 1, 2, 3]))
        ar = np.repeat(a, q)                                  # same F, q times the members (sorted)
        p_move = float(rng.choice([0.05, 0.3, 1.0]))
        amt = (rng.random(ar.size) ** float(rng.choice([1, 4]))) * float(rng.choice([0.01, 0.1, 0.5])) * D
        low = np.where(rng.random(ar.size) < p_move, amt.astype(np.int64), 0)
        b = np.sort(np.maximum(ar - low, 0))                  # every threshold weakly lower => F_b >= F_a
        ta, tb = tau(a), tau(b)
        tm = tau(np.sort(np.concatenate((a, b))))
        c["trials"] += 1
        if ta > tb:
            c["viol_monotone"] += 1
        if ta < tb:
            c["strict"] += 1
        if not (ta <= tm <= tb):
            c["viol_between"] += 1
        if ta < tm < tb:
            c["strictly_between"] += 1
    return c


# =========================================================================================
# G. mixing-weight sweeps: lam |-> tau(F_lam) is quasi-concave (unimodal)
# =========================================================================================

def run_sweep(seed: int, trials: int, J: int = 20):
    rng = np.random.default_rng(seed)
    c = Counter()
    for _ in range(trials):
        f1, f2 = (str(rng.choice(SIZED_FAMS)) for _ in range(2))
        d1, _ = make_dist(f1, rng); d2, _ = make_dist(f2, rng)
        n = int(rng.integers(10, 201))
        a1, a2 = d1(n, rng), d2(n, rng)
        ts = [tau(a2)] + [tau(np.sort(np.concatenate((np.tile(a1, j), np.tile(a2, J - j))))) for j in range(1, J)] + [tau(a1)]
        c["trials"] += 1
        # quasi-concavity:  t_j >= min(max_{i<j} t_i, max_{k>j} t_k)  for all interior j
        pm = [ts[0]]
        for t in ts[1:]:
            pm.append(max(pm[-1], t))
        sm = [ts[-1]]
        for t in reversed(ts[:-1]):
            sm.append(max(sm[-1], t))
        sm.reverse()
        if any(ts[j] < min(pm[j - 1], sm[j + 1]) for j in range(1, J)):
            c["viol_quasiconcave"] += 1
        hi = max(ts[0], ts[J])
        win = [j for j in range(1, J) if ts[j] > hi]
        if ts[0] == ts[J] and win:
            c["viol_equal_tau_ignition"] += 1
        if win:
            c["ign_somewhere"] += 1
            if win != list(range(win[0], win[-1] + 1)):
                c["viol_window_not_contiguous"] += 1
            c["window_width_total"] += len(win)
            # weight on the LOW crowd: j if crowd 1 is low, else J - j.  Claim: ign set = {1, ..., w_max}
            w = sorted(j if ts[J] < ts[0] else J - j for j in win)
            if w != list(range(1, w[-1] + 1)):
                c["viol_downward_closure"] += 1
            if w[-1] >= 2:
                c["window_wider_than_one_step"] += 1
        lo = min(ts[0], ts[J])
        if any(ts[j] < lo for j in range(1, J)):
            c["viol_below_min_sweep"] += 1
        if len(set(ts)) > 2:
            c["nonconstant"] += 1
        if any(ts[j + 1] < ts[j] for j in range(J)) and any(ts[j + 1] > ts[j] for j in range(J)):
            c["nonmonotone"] += 1
    return c


# =========================================================================================
# E2. is latent pressure also SUFFICIENT for ignition at some mixing weight?  (generic: yes, ties: no)
# =========================================================================================

def run_smalllam(seed: int, want: int = 300, maxtries: int = 30000) -> Counter:
    rng = np.random.default_rng(seed)
    c = Counter()
    lams = [Fraction(1, 2**j) for j in range(1, 31)]
    tries = 0
    while c["latent"] < want and tries < maxtries:
        tries += 1
        fam = str(rng.choice(["uniform", "beta", "bimodal"]))       # continuous thresholds: no ties
        d1, _ = make_dist(fam, rng); d2, _ = make_dist(fam, rng)
        a1, a2 = d1(int(rng.integers(10, 301)), rng), d2(int(rng.integers(10, 301)), rng)
        t1, t2 = tau(a1), tau(a2)
        if t1 == t2:
            continue
        alo, ahi, thi = (a1, a2, t2) if t1 < t2 else (a2, a1, t1)
        latent = F_count(alo, thi.numerator, thi.denominator) * thi.denominator > thi.numerator * alo.size
        c["pairs"] += 1
        if latent:
            c["latent"] += 1
            res = [mix_orbit(alo, ahi, lam) > thi for lam in lams]
            if any(res):
                c["latent_ign_some_lam"] += 1
                c["first_j_" + str(res.index(True) + 1)] += 1
            else:
                c["latent_no_ign_any_lam"] += 1
        else:
            if any(mix_orbit(alo, ahi, lam) > thi for lam in lams[:10]):
                c["viol_nonlatent_ign"] += 1
            c["nonlatent"] += 1
    return c


def mix_orbit_small(c1, c2, K, lam: Fraction) -> Fraction:
    r = Fraction(0)
    while True:
        r2 = lam * F_small(c1, K, r) + (1 - lam) * F_small(c2, K, r)
        if r2 == r:
            return r
        r = r2


def smalllam_exhaustive(K: int, nmax: int):
    """Tie-heavy small crowds: latent pairs with NO ignition at any lam = 2^-j, j <= 12."""
    crowds = []
    for n in range(1, nmax + 1):
        crowds += list(combinations_with_replacement(range(K + 1), n))
    tau_ = {c: lfp_small(c, K) for c in crowds}
    lams = [Fraction(1, 2**j) for j in range(1, 13)]
    cnt = Counter()
    best = None
    for c1 in crowds:
        for c2 in crowds:
            t1, t2 = tau_[c1], tau_[c2]
            if not t1 < t2:
                continue
            if not F_small(c1, K, t2) > t2:
                continue
            cnt["latent_ordered"] += 1
            grid = [mix_orbit_small(c1, c2, K, Fraction(j, 20)) > t2 for j in range(1, 20)]   # weight j/20 on crowd 1
            if any(grid):
                top = max(j for j, g in enumerate(grid) if g)
                if not all(grid[: top + 1]):
                    cnt["viol_downward_closure"] += 1
                cnt["grid_ign"] += 1
            if any(mix_orbit_small(c1, c2, K, lam) > t2 for lam in lams):
                cnt["ign_some"] += 1
            else:
                cnt["never"] += 1
                cand = (len(c1) + len(c2), len(c1), c1, c2)
                if best is None or cand < best:
                    best = cand
    return cnt, best


# =========================================================================================
# F. splits
# =========================================================================================

def split_masks(a: np.ndarray, rng):
    """(rule, mask of part A) for a sorted threshold array a (rank = threshold order)."""
    n = a.size
    p = float(rng.uniform(0.1, 0.9))
    out = []
    out.append(("coin(1/2)", rng.random(n) < 0.5))
    out.append(("coin(p)", rng.random(n) < p))
    m = np.zeros(n, bool); m[: max(1, int(p * n))] = True
    out.append(("by threshold (low / high)", m))
    sc = np.arange(n) + rng.normal(0, 0.2 * n, n)
    m = np.zeros(n, bool); m[np.argsort(sc)[: n // 2]] = True
    out.append(("noisy threshold rank", m))
    z = int(np.searchsorted(a, 0, side="right"))
    m = np.zeros(n, bool); m[:z] = True
    rest = np.flatnonzero(~m); m[rest[rng.random(rest.size) < 0.5]] = True
    out.append(("instigators to A", m))
    return out


def run_splits(seed: int, wholes: int):
    rng = np.random.default_rng(seed)
    c = defaultdict(Counter)            # rule -> counts
    zb = defaultdict(Counter)           # instigator-count bucket (coin 1/2) -> counts
    for _ in range(wholes):
        fam = str(rng.choice(BASE_FAMS))
        d, _ = make_dist(fam, rng)
        a = d(max(20, rand_n(rng)), rng)
        n = a.size
        k = lfp_count(a); z = int(np.searchsorted(a, 0, side="right"))
        t = Fraction(k, n)
        for rule, m in split_masks(a, rng):
            na = int(m.sum())
            if na < 2 or n - na < 2:
                continue
            A, B = a[m], a[~m]
            kA, kB = lfp_count(A), lfp_count(B)
            zA, zB = int(np.searchsorted(A, 0, side="right")), int(np.searchsorted(B, 0, side="right"))
            tA, tB = Fraction(kA, A.size), Fraction(kB, B.size)
            cas = k > z                                        # the whole cascades beyond its instigators
            cc = c[rule]
            cc["splits"] += 1
            if cas:
                cc["cascading_wholes"] += 1
                if tA < t and tB < t:
                    cc["kill_both_below"] += 1
                if kA == zA and kB == zB:
                    cc["kill_both_inert"] += 1
                if tA == 0 or tB == 0:
                    cc["some_part_dormant"] += 1
                if tA > t or tB > t:
                    cc["some_part_above"] += 1
                if t == 1:
                    cc["whole_full"] += 1
                    if tA < 1 and tB < 1:
                        cc["full_both_lt1"] += 1
                    if tA == 0 and tB == 0:
                        cc["viol_literal_e"] += 1
                if rule.startswith("coin(1/2)"):
                    key = "1" if z == 1 else "2-3" if z <= 3 else "4-9" if z <= 9 else "10-49" if z <= 49 else ">=50"
                    zb[key]["cascading"] += 1
                    zb[key]["exp_dormant"] += 2.0 ** (1 - z)      # P(a fair coin leaves a part with no instigator)
                    if tA < t and tB < t:
                        zb[key]["kill"] += 1
                    if tA == 0 or tB == 0:
                        zb[key]["dormant_part"] += 1
            if tA > t and tB > t:
                cc["viol_both_above"] += 1
            if tA == 0 and tB == 0 and t > 0:
                cc["viol_dormant_parts_live_whole"] += 1
            if rule.startswith("by threshold") and not (tB <= t <= tA):
                cc["viol_threshold_sandwich"] += 1
            if t < min(tA, tB):
                cc["viol_below_both_parts"] += 1
    return c, zb


def run_split_exhaustive(seed: int, wholes: int, K: int = 12):
    """All bipartitions of small crowds: does SOME split kill a cascade?  Does some make both parts more active?"""
    rng = np.random.default_rng(seed)
    c = Counter()
    for _ in range(wholes):
        n = int(rng.integers(4, 10))
        shape = float(rng.choice([0.5, 1.0, 2.0]))
        ts = tuple(sorted(int(min(K, max(0, round(K * rng.beta(shape, 1.5 * shape))))) for _ in range(n)))
        if rng.random() < 0.5:
            ts = tuple(sorted(ts[:-1] + (0,)))                 # make sure there is an instigator
        t = lfp_small(ts, K); z = ts.count(0)
        if not t > Fraction(z, n):
            continue                                           # keep only wholes that cascade
        c["cascading_wholes"] += 1
        kill = above = False
        for mask in range(1, 2 ** (n - 1)):                    # member n-1 always in B: all bipartitions once
            A = tuple(ts[i] for i in range(n) if mask >> i & 1)
            B = tuple(ts[i] for i in range(n) if not mask >> i & 1)
            tA, tB = lfp_small(A, K), lfp_small(B, K)
            if tA < t and tB < t:
                kill = True
            if tA > t and tB > t:
                above = True
        c["some_split_kills"] += kill
        c["some_split_lifts_both"] += above
        if t == 1:
            c["full_wholes"] += 1
            c["full_some_split_kills"] += kill
    return c


# =========================================================================================
# E3. crowds drawn from ONE population (exchangeable): does ignition die out with n?
# =========================================================================================

def make_pops(seed: int, npops: int):
    """Beta(al,be) thresholds with instigator share z; smooth equilibrium tau_G and slope F_G'(tau_G)."""
    from scipy.stats import beta as sbeta
    rng = np.random.default_rng(seed)
    grid = np.linspace(0, 1, 200001)
    pops = []
    for _ in range(npops):
        al, be = (float(x) for x in np.exp(rng.uniform(np.log(0.5), np.log(8), 2)))
        z = float(rng.choice([0.02, 0.1]))
        FG = z + (1 - z) * sbeta.cdf(grid, al, be)
        i = int(np.argmax(FG <= grid))                       # first crossing from above
        pops.append((al, be, z, float(grid[i]), float((1 - z) * sbeta.pdf(grid[i], al, be))))
    return pops


def run_samepop(seed: int, n: int, pops, trials: int) -> Counter:
    rng = np.random.default_rng(seed)
    c = Counter()
    for (al, be, z, tg, sl) in pops:
        cls = "crit" if sl >= 0.7 else "trans"
        for _ in range(trials):
            a1 = _finish(rng.beta(al, be, n), z, 0.0, rng, n)
            a2 = _finish(rng.beta(al, be, n), z, 0.0, rng, n)
            r = analyse_pair(a1, a2)
            c[cls + "_pairs"] += 1
            if r["tm"] > r["hi"]:
                c[cls + "_ign"] += 1
            if r["tm"] < r["lo"]:
                c["viol_below_min"] += 1
    return c


# =========================================================================================
# H. the certificate side (models/01 Thm 2.1) -- contrast
# =========================================================================================

def run_certificate(seed: int, trials: int) -> Counter:
    from models import certificates as cert
    rng = np.random.default_rng(seed)
    c = Counter()
    for _ in range(trials):
        n = int(rng.integers(2, 31))
        G = cert.random_certified(n, rng, density=float(rng.choice([0.3, 0.6, 1.0])))
        rho = cert.spectral_radius(G)
        k = int(rng.integers(2, min(n, 6) + 1))
        for idx in cert.random_partition(n, k, rng):
            c["blocks"] += 1
            r = cert.spectral_radius(cert.restrict(G, idx))
            if r > rho + 1e-12:
                c["viol_split_monotone"] += 1
            if r < rho - 1e-12:
                c["block_strictly_lower"] += 1
        # merge of two certified groups with random cross gains: rho(Gamma_m) >= max(rho_1, rho_2)
        n1, n2 = int(rng.integers(1, 12)), int(rng.integers(1, 12))
        G1 = cert.random_certified(n1, rng); G2 = cert.random_certified(n2, rng)
        h12, h21 = float(rng.choice([0.05, 0.3, 1.0])), float(rng.choice([0.05, 0.3, 1.0]))
        C12 = cert.random_cross(n1, n2, rng, density=float(rng.choice([0.2, 1.0])), lo=0.1 * h12, hi=h12)
        C21 = cert.random_cross(n2, n1, rng, density=float(rng.choice([0.2, 1.0])), lo=0.1 * h21, hi=h21)
        rm = cert.spectral_radius(cert.merged(G1, C12, C21, G2))
        c["merges"] += 1
        if rm < max(cert.spectral_radius(G1), cert.spectral_radius(G2)) - 1e-12:
            c["viol_merge_ge_max"] += 1
        if rm >= 1:
            c["merge_uncertified"] += 1
    return c


# =========================================================================================
# I. Granovetter's two crowds, merged;  J. the two-atom family in closed form
# =========================================================================================

def gran_crowd(n: int, kind: str) -> np.ndarray:
    unit = D // n
    j = np.arange(n)
    if kind == "G1":
        j[1] = 2
    return np.sort(j * unit)


def gran_table():
    rows = []
    for (n1, n2) in [(10, 10), (100, 100), (1000, 1000), (100, 1000), (10, 1000)]:
        for k1, k2 in [("G0", "G0"), ("G0", "G1"), ("G1", "G1")]:
            a1, a2 = gran_crowd(n1, k1), gran_crowd(n2, k2)
            r = analyse_pair(a1, a2)
            rows.append((n1, k1, n2, k2, r["t1"], r["t2"], r["tm"], r["avg"]))
    return rows


def atoms_formula(z1, n1, s1, z2, n2, s2):
    """Closed form for two-atom crowds (z_i instigators, rest at threshold s_i = a_i/D), s1 <= s2."""
    N = n1 + n2
    m = Fraction(z1 + z2, N)                 # lam m1 + (1-lam) m2
    u = Fraction(n1 + z2, N)                 # lam + (1-lam) m2 : crowd 1 fully in, crowd 2's instigators
    S1, S2 = Fraction(s1, D), Fraction(s2, D)
    if m < S1:
        return m
    return Fraction(1) if u >= S2 else u


def run_atoms(seed: int, trials: int):
    rng = np.random.default_rng(seed)
    c = Counter()
    for _ in range(trials):
        n1, n2 = int(rng.integers(2, 60)), int(rng.integers(2, 60))
        z1, z2 = int(rng.integers(0, n1)), int(rng.integers(0, n2))
        s1, s2 = sorted(int(x) for x in rng.integers(1, D // 2, 2))
        if rng.random() < 0.5:
            (n1, z1, s1), (n2, z2, s2) = (n1, z1, s1), (n2, z2, s2)
        a1 = np.sort(np.array([0] * z1 + [s1] * (n1 - z1), dtype=np.int64))
        a2 = np.sort(np.array([0] * z2 + [s2] * (n2 - z2), dtype=np.int64))
        got = tau(np.sort(np.concatenate((a1, a2))))
        c["trials"] += 1
        if got != atoms_formula(z1, n1, s1, z2, n2, s2):
            c["viol_formula"] += 1
        r = analyse_pair(a1, a2)
        if r["tm"] > r["hi"]:
            c["ign"] += 1
    return c


def sweep_example(J: int = 20):
    """tau_lam for F1 = all at 0.05 (dormant, latent) and F2 = 10% instigators, 90% at 0.5 (n = 100 each)."""
    a1 = np.full(100, int(0.05 * D), dtype=np.int64)
    a2 = np.sort(np.array([0] * 10 + [D // 2] * 90, dtype=np.int64))
    rows = []
    for j in range(J + 1):
        if j == 0:
            t = tau(a2)
        elif j == J:
            t = tau(a1)
        else:
            t = tau(np.sort(np.concatenate((np.tile(a1, j), np.tile(a2, J - j)))))
        rows.append((Fraction(j, J), t))
    return rows


# =========================================================================================
# driver
# =========================================================================================

SCENARIOS = ["uniform", "beta", "bimodal", "normal", "atoms", "gran", "full", "mixed", "sameG"]


def merge_tally(ts):
    out = Tally()
    for t in ts:
        out.c.update(t.c)
        for k, v in t.cat.items():
            out.cat[k].update(v)
        for k, v in t.nb.items():
            out.nb[k].update(v)
        out.over += t.over
        out.dav += t.dav
        for k, v in t.ex.items():
            if k not in out.ex or v[0] > out.ex[k][0]:
                out.ex[k] = v
    return out


def compute_all(args) -> dict:
    q = args.quick
    P = 1500 if q else args.pairs
    chunks = 1 if q else 4
    ss = np.random.SeedSequence(args.seed)
    seeds = [int(s.generate_state(1)[0]) for s in ss.spawn(200)]
    sd = iter(seeds)
    exh_cfg = [(6, 3)] if q else [(12, 3), (6, 5)]
    ctx = mp.get_context("fork")
    R: dict = {"P": P, "args": vars(args)}
    t0 = time.time()
    with ctx.Pool(args.jobs) as pool:
        h_scen = {s: [pool.apply_async(run_scenario, ((s, next(sd), P // chunks, 150 if q else 400),)) for _ in range(chunks)]
                  for s in SCENARIOS}
        h_exh = {cfg: pool.apply_async(exhaustive, cfg) for cfg in exh_cfg}
        h_mono = pool.apply_async(run_monotone, (next(sd), 500 if q else 20000))
        h_sweep = pool.apply_async(run_sweep, (next(sd), 150 if q else 6000))
        h_small = pool.apply_async(run_smalllam, (next(sd), 30 if q else 400))
        h_smex = pool.apply_async(smalllam_exhaustive, (6, 3 if q else 4))
        h_split = pool.apply_async(run_splits, (next(sd), 150 if q else 6000))
        h_splex = pool.apply_async(run_split_exhaustive, (next(sd), 60 if q else 3000))
        pops = make_pops(next(sd), 12 if q else 60)
        SP_N = [30, 100, 300] if q else [30, 100, 300, 1000, 3000, 10000]
        h_sp = {n: pool.apply_async(run_samepop, (next(sd), n, pops, 10 if q else 100)) for n in SP_N}
        h_cert = pool.apply_async(run_certificate, (next(sd), 300 if q else 20000))
        h_atoms = pool.apply_async(run_atoms, (next(sd), 300 if q else 20000))
        R["scen"] = {s: merge_tally([h.get()[1] for h in hs]) for s, hs in h_scen.items()}
        R["exh"] = {cfg: h.get() for cfg, h in h_exh.items()}
        R["mono"] = h_mono.get()
        R["sweep"] = h_sweep.get()
        R["small"] = h_small.get()
        R["smex"] = h_smex.get()
        R["split"] = h_split.get()
        R["splex"] = h_splex.get()
        R["samepop"] = {n: h.get() for n, h in h_sp.items()}
        R["pops"] = pops
        R["cert"] = h_cert.get()
        R["atoms"] = h_atoms.get()
    R["selfcheck"] = selfcheck(next(sd), 2000 if q else 40000)
    R["gran"] = gran_table()
    R["sweep_ex"] = sweep_example()
    R["seconds"] = time.time() - t0
    return R


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seed", type=int, default=20261031)
    ap.add_argument("--pairs", type=int, default=40000, help="merge pairs per scenario (9 scenarios)")
    ap.add_argument("--jobs", type=int, default=min(8, mp.cpu_count()))
    ap.add_argument("--quick", action="store_true", help="small run for smoke testing")
    ap.add_argument("--out", type=Path, default=SIM / "results" / "mixture_equilibria.md")
    ap.add_argument("--cache", type=Path, default=None, help="dev convenience: pickle of results")
    ap.add_argument("--raw", action="store_true", help="print raw counters instead of writing the report")
    args = ap.parse_args()
    import pickle
    if args.cache and args.cache.exists():
        R = pickle.loads(args.cache.read_bytes())
    else:
        R = compute_all(args)
        if args.cache:
            args.cache.write_bytes(pickle.dumps(R))
    if args.raw:
        dump_raw(R)
        return
    text = render(R)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(text)
    print(f"wrote {args.out} ({len(text.splitlines())} lines) in {R['seconds']:.0f}s")


def dump_raw(R):
    print("seconds", R["seconds"])
    for s, t in R["scen"].items():
        print(f"\n== {s}: {dict(t.c)}")
        print("   cat:", {k: dict(v) for k, v in sorted(t.cat.items())})
        print("   nb :", {k: dict(v) for k, v in t.nb.items()})
        if t.over:
            o = np.array(t.over)
            print(f"   overshoot n={o.size} median={np.median(o):.4f} p90={np.quantile(o, .9):.4f} max={o.max():.4f}")
        for k, v in t.ex.items():
            print("   ex", k, v[0], v[1])
    for cfg, (cnt, first) in R["exh"].items():
        print("\nEXH", cfg, dict(cnt))
        for k, (key, extra) in first.items():
            print("  first", k, key, extra)
    for k in ("mono", "sweep", "small", "smex", "splex", "cert", "atoms"):
        print("\n", k, R[k])
    print(" samepop", {n: dict(c) for n, c in R["samepop"].items()})
    print(" pops with slope>=0.7:", sum(1 for p in R["pops"] if p[4] >= 0.7), "of", len(R["pops"]))
    for rule, cc in R["split"][0].items():
        print(" split", rule, dict(cc))
    print(" split by z", {k: dict(v) for k, v in R["split"][1].items()})


# =========================================================================================
# report
# =========================================================================================

def _n(x) -> str:
    return f"{int(x):,}"


def _pc(a, b, d=1) -> str:
    return "n/a" if not b else f"{100.0 * a / b:.{d}f}%"


def _fx(x: Fraction, big: int = 40) -> str:
    return str(x) if x.denominator <= big else f"{float(x):.4f}"


def _crowd(c, K) -> str:
    return "{" + ", ".join(str(Fraction(t, K)) for t in c) + "}"


def _example(first_by_cfg: dict, key: str):
    """Smallest example for `key` over the exhaustive configurations -> (K, (N, n1, c1, c2), (t1, t2, tm))."""
    best = None
    for (K, nmax), (cnt, first) in first_by_cfg.items():
        if key in first:
            cand = (first[key][0], K, first[key][1])
            if best is None or cand[0] < best[0]:
                best = cand
    if best is None:
        return None
    (N, n1, c1, c2), K, ex = best
    return K, (N, n1, c1, c2), ex


def _ex_line(first_by_cfg, key, note="") -> str:
    r = _example(first_by_cfg, key)
    if r is None:
        return f"- `{key}`: none found."
    K, (N, n1, c1, c2), (t1, t2, tm) = r
    lam = Fraction(n1, N)
    avg = lam * t1 + (1 - lam) * t2
    return (f"- crowd 1 = {_crowd(c1, K)}, crowd 2 = {_crowd(c2, K)}: "
            f"tau_1 = {t1}, tau_2 = {t2}, merged {_crowd(sorted(c1 + c2), K)}: **tau_m = {tm}**; "
            f"lambda-average {_fx(avg)}.{note}")


def _m6_line(first_by_cfg) -> str:
    r = _example(first_by_cfg, "created_strict")
    if r is None:
        return "- none found."
    K, (N, n1, c1, c2), (t1, t2, tm) = r
    n2 = len(c2)
    m1, m2 = Fraction(c1.count(0), n1), Fraction(c2.count(0), n2)
    p1 = Fraction(min(x for x in c1 if x > 0), K)
    p2 = Fraction(min(x for x in c2 if x > 0), K)
    mm = Fraction(c1.count(0) + c2.count(0), N)
    return (f"- crowd 1 = {_crowd(c1, K)} (m_1 = {m1}, least positive threshold {p1} > m_1: recruits nobody), crowd 2 = {_crowd(c2, K)} "
            f"(m_2 = {m2}, least positive threshold {p2} > m_2: recruits nobody). Merged instigator share {mm} >= {min(p1, p2)}, "
            f"so the merge recruits, and the cascade runs to **tau_m = {tm}**.")


def _split_line(first_by_cfg, key) -> str:
    r = _example(first_by_cfg, key)
    if r is None:
        return "- none found."
    K, (N, n1, c1, c2), (t1, t2, tm) = r
    return (f"- whole {_crowd(sorted(c1 + c2), K)} (tau = {tm}) splits into {_crowd(c1, K)} (tau = {t1}) and {_crowd(c2, K)} (tau = {t2}).")


def render(R) -> str:
    A, S = R["args"], R["scen"]
    TOT = merge_tally(list(S.values()))
    c = TOT.c
    exh = R["exh"]
    ec = lambda k: sum(cnt.get(k, 0) for cnt, _ in exh.values())
    EXH = ec("pairs")
    cats = lambda t, k: t.cat[k]["pairs"]
    out: list[str] = []
    w = out.append

    def tbl(head, rows, left=(0,)):
        w("| " + " | ".join(head) + " |")
        w("|" + "|".join("---" if i in left else "---:" for i in range(len(head))) + "|")
        for r in rows:
            w("| " + " | ".join(str(x) for x in r) + " |")
        w("")

    # ---------------------------------------------------------------- derived facts
    elig_avg = c["pairs"] - cats(TOT, "DD") - cats(TOT, "FF")
    ign_cats = ("DI", "DP", "II", "IP", "PP")
    elig_ign = sum(cats(TOT, k) for k in ign_cats)
    ign = c["ign"]
    viol_keys = sorted(k for k in c if k.startswith("viol"))
    total_viol = sum(c[k] for k in viol_keys)
    sweep, mono, small, smex = R["sweep"], R["mono"], R["small"], R["smex"][0]
    splits, zb = R["split"]
    splex, cert = R["splex"], R["cert"]
    samepop = R["samepop"]
    ov = np.array(TOT.over)
    exh_viol = sum(ec(k) for k in ("below_min", "above_tmax", "ign_no_latent", "firststep_mismatch", "firststep_mismatch_part",
                                   "both_full_viol", "both_dormant_viol", "dormant_plus_live_dead", "ordered_viol",
                                   "ordered_between_viol"))
    split_viol = sum(cc[k] for cc in splits.values() for k in cc if k.startswith("viol"))
    all_viol = (total_viol + exh_viol + sum(v for k, v in mono.items() if k.startswith("viol"))
                + sum(v for k, v in sweep.items() if k.startswith("viol")) + sum(v for k, v in small.items() if k.startswith("viol"))
                + sum(v for k, v in smex.items() if k.startswith("viol")) + split_viol + splex["some_split_lifts_both"]
                + sum(v for k, v in cert.items() if k.startswith("viol")) + R["atoms"]["viol_formula"]
                + sum(sp["viol_below_min"] for sp in samepop.values()) + c["verify_bad"] + R["selfcheck"][1])

    # ---------------------------------------------------------------- header
    w("# D609 exploratory numerics: merge and split of Granovetter threshold crowds")
    w("")
    w(f"_Generated by `sim/explore/mixture_equilibria.py` (seed {A['seed']}, {_n(R['P'])} random pairs per scenario, "
      f"{R['seconds']:.0f} s on {A['jobs']} cores). Re-run: `cd sim && ~/.local/bin/uv run --frozen python explore/mixture_equilibria.py`; "
      f"counts are deterministic for the seed. This file is generated: edit the script, not the file._")
    w("")
    w("**Status: exploratory.** Direction D609 (`docs/research-map.md`, cluster Y), toward `models/02-our-claims.md`. "
      "Tags as elsewhere in the repo: **[derived, shown]** a short proof given on this page, mine and not yet audited; "
      "**[computed]** observed in draws, which is evidence and never proof; **FALSE** refuted by a counterexample listed in section 5. "
      "Nothing here touches `models/` or any test.")
    w("")
    if all_viol:
        w(f"> **WARNING: {all_viol} violation(s) of statements marked proved were recorded in this run. Treat the proofs below as suspect until this is explained.**")
        w("")

    # ---------------------------------------------------------------- 0 answers
    w("## 0. Answers in brief")
    w("")
    w(f"1. **Is lfp(F_m) always between the parts' lfps? No: the lower half is a theorem, the upper half is false.** "
      f"tau(F_m) >= min(tau_1, tau_2) held in all {_n(c['pairs'] + EXH)} pairs and has a one-line proof (M1). "
      f"tau(F_m) > max(tau_1, tau_2) (\"ignition\") occurred in {_n(ign)} of {_n(elig_ign)} random pairs where it is possible "
      f"({_pc(ign, elig_ign)}; pairs with a full crowd or two dormant crowds cannot ignite) and in {_n(ec('ign'))} of {_n(EXH)} exhaustive small pairs. "
      "The smallest case has three members: {1/6} merged with {0, 2/3} (section 5). **A live crowd is never dampened below the min** (M1), "
      "though it can be dampened far below its own value and below the lambda-average.")
    w(f"2. **Who ignites.** Dormancy is not required. Ignition occurs in every category pair where the max is below 1 and the pair is not two dormant crowds "
      f"(table B), including two crowds that each have instigators and recruit nobody (I x I: {_n(sum(S[s].cat['II']['ign'] for s in S))}). "
      "The exact condition: ignition above max requires **latent pressure**, F_low(tau_high) > tau_high (M7; "
      f"{_n(c['viol_ign_without_latent'] + ec('ign_no_latent'))} exceptions in {_n(c['pairs'] + EXH)} pairs), "
      "and the set of intruder weights that ignite is an interval (0, lambda*) (M7).")
    w(f"3. **Averages (Q2): neither bound holds.** In the {_n(elig_avg)} random pairs where the two can differ, tau_m < lambda-average in {_pc(c['lt_avg'], elig_avg)} "
      f"(so \"tau_m >= average\" is violated that often) and tau_m > lambda-average in {_pc(c['gt_avg'], elig_avg)} (so \"tau_m <= average\" is violated that often). "
      "Dilution and discrete gaps push below (Granovetter-type crowds almost always: table A) but never when neither part recruits, where pooled instigators give tau_m >= average (M10); ignition and instigator pooling push above.")
    w("4. **Statements that hold in every draw (Q3), all with short proofs (section 3):** (a) both tau = 1 gives tau_m = 1, as the special case c = 1 of "
      "\"{F : tau(F) >= c} is convex\" (M4); (b) F_1 <= F_2 pointwise gives tau_1 <= tau_2, and then tau_1 <= tau_m <= tau_2 (M3); "
      "(c) the sandwich is exact, tau(min(F_1,F_2)) = min(tau_1,tau_2) <= tau_m <= tau(max(F_1,F_2)) = the least common pre-fixed point (M2); "
      "(d) as stated, \"two crowds with lfp = 0 merge to lfp > 0\" is **impossible** (lfp = 0 means F(0) = 0, and F_m(0) is the average of the F_i(0)); "
      "the true version is exact and short: two crowds that recruit nobody merge into one that does iff the merged instigator share reaches the smallest positive threshold (M6); "
      "(e) as stated, \"lfp = 1 whole, two conditional parts with lfp = 0\" is **impossible** for the same reason; "
      f"the true version (whole cascades, both parts strictly below it) occurs in {_pc(splits['coin(1/2)']['kill_both_below'], splits['coin(1/2)']['cascading_wholes'])} of fair-coin splits of cascading wholes, "
      "mostly when the whole has one instigator, never when the parts are cut by threshold (M8).")
    w(f"5. **Certificate contrast (Q4).** rho(Gamma_B) <= rho(Gamma) for every block in {_n(cert['blocks'])} random splits (violations: {cert['viol_split_monotone']}), "
      "so the certificate is hereditary under split. The equilibrium is not: it only satisfies tau(whole) >= min(tau_parts), "
      f"and in {_pc(splits['coin(1/2)']['some_part_above'], splits['coin(1/2)']['cascading_wholes'])} of fair-coin splits of cascading wholes some part is strictly more active than the whole.")
    w("6. **Structure.** The merge is *linear* in the excess function E_F(r) = F(r) - r, and the equilibrium is its first non-positive point. "
      "So no function of the parts' equilibria and sizes can give the merged equilibrium (proposition N: two pairs with identical (tau_1, tau_2, n_1, n_2) have merged equilibria 1 and 1/3). "
      "A group-level drive state must carry the excess function, not a summary of it.")
    w("7. **Open (best conjecture):** for crowds drawn from one population whose first crossing is transversal, "
      "P(ignition) -> 0 as the sizes grow, at about the n^(-1/2) rate a linearisation suggests (section 4.8). Not proved.")
    w("")

    # ---------------------------------------------------------------- 1 setup
    w("## 1. Setup")
    w("")
    w("A crowd of n members has thresholds theta_i in [0,1]; F(r) = #{i : theta_i <= r}/n; dynamics r(0) = F(0), r(t+1) = F(r(t)); equilibrium "
      "tau(F) = lfp(F) (v0.1 Thm 6.3). A threshold of 0 is an **instigator**; a threshold of 1 is a member who joins only when everyone else has (a \"never\"). "
      "Write P(F) = {r in [0,1] : F(r) <= r} (the **pre-fixed set**; 1 is always in it) and E_F(r) = F(r) - r (the **excess**).")
    w("")
    w("- **Merge** of (n_1, F_1) and (n_2, F_2): F_m = lam F_1 + (1 - lam) F_2 with lam = n_1/(n_1 + n_2), i.e. the union of the two threshold lists with thresholds kept as *fractions of the crowd* "
      "(so a merge dilutes: a member who needed 10% of 100 people now needs 10% of 200). **Split** by a rule on members: the two conditional CDFs, same thresholds, new denominators. "
      "F is the mixture of its parts, so *a split is a merge read backwards*.")
    w("- **Exactness.** Thresholds are integers over a grid of D = 10^7 (theta = a/D), so \"theta <= k/N\" is the integer test a*N <= k*D, equilibria are `Fraction`s, "
      "and no floating-point comparison decides anything reported here. The equilibrium is computed as the smallest pre-fixed point (vectorised) and cross-checked "
      f"against the literal orbit r(t+1) = F(r(t)) and against exact orbits of the min, max and mixture maps in {_n(c['verified'])} sampled draws with N <= 600: **{c['verify_bad']} disagreements**. "
      f"Separately, an independent pure-python reimplementation (no numpy, integer arithmetic over a grid of 1/100) agrees with the main path on every field of the pair analysis "
      f"(equilibria, upper bound, latent pressure, first-step test, categories) in {_n(R['selfcheck'][0])} random small pairs: **{R['selfcheck'][1]} disagreements**.")
    w("- **Draws.** Each random pair has two independent crowds with n_i log-uniform in [10, 10,000] (so N = n_1 + n_2 runs from 20 to 20,000); the Granovetter family uses n in {10, ..., 10,000} on the integer grid. "
      "Families: `uniform` (U[a,b], a in [0,.7]); `beta` (shapes log-uniform in [.3,8]); `bimodal` (two betas, modes in [.03,.35] and [.45,.95]); `normal` (Granovetter's clipped normal, mean .1 to .5, sd .02 to .4); "
      "`atoms` (1 to 4 point masses); `gran` (Granovetter's uniform crowd {0,1,...,n-1}/n, his perturbed crowd with the member at 1 moved to 2, and 1 to 3 random one- or two-step moves of that crowd); "
      "`full` (built so that tau = 1: the k-th member's threshold is at most k/n); `mixed` (families chosen at random per crowd); `sameG` (both crowds from the same distribution). "
      "Except `normal`, `gran` and `full`, each member is an instigator with probability z (0 with probability .25, else log-uniform in [.003,.3]) and a \"never\" with probability w (0 or U[0,.4]). "
      "**These rates describe my sampling design, not the world** (a quarter of crowds are dormant by construction); the tables show what exists and how it is structured, not how common it is.")
    w("- **Categories** of a crowd: D dormant (no instigators, tau = 0); I inert (instigators exist, tau = F(0): they recruit nobody); P partial cascade (F(0) < tau < 1); F full (tau = 1).")
    w("")

    # ---------------------------------------------------------------- 2 statements
    w("## 2. Statements and their status")
    w("")
    w("Throughout, tau_i = tau(F_i), tau_m = tau(F_lam), lam in [0,1] the weight of F_1, and P_i = P(F_i). \"Checked\" counts pairs (or sweeps, splits, blocks) in which the statement was evaluated; "
      "\"violations\" counts failures. A proof with zero violations is evidence that the proof and the code agree; it is not what makes the statement true.")
    w("")
    Pm = c["pairs"]
    rows = [
        ("M1", "tau_m >= min(tau_1, tau_2): the merge is never below both parts; P(F_lam) is contained in P_1 union P_2", "PROVED [derived, shown]",
         _n(Pm + EXH + sweep["trials"] * 19), c["viol_below_min"] + ec("below_min") + sweep["viol_below_min_sweep"] + sum(sp["viol_below_min"] for sp in samepop.values())),
        ("M2", "tau_m <= tau_cap := least common pre-fixed point min(P_1 intersect P_2) = tau(max(F_1,F_2)); and tau(min(F_1,F_2)) = min(tau_1,tau_2)", "PROVED [derived, shown]",
         _n(Pm + EXH), c["viol_above_tmax"] + ec("above_tmax")),
        ("M3", "F_1 <= F_2 pointwise gives tau_1 <= tau_2, and then tau_1 <= tau_m <= tau_2", "PROVED [derived, shown]",
         _n(ec("ordered") + mono["trials"]), ec("ordered_viol") + ec("ordered_between_viol") + mono["viol_monotone"] + mono["viol_between"]),
        ("M4", "{F : tau(F) >= c} is convex: both tau = 1 gives tau_m = 1; lam -> tau(F_lam) is unimodal", "PROVED [derived, shown]",
         f"{_n(c['both_full'] + ec('both_full'))} full-full; {_n(sweep['trials'])} sweeps", c["viol_both_full"] + ec("both_full_viol") + sweep["viol_quasiconcave"]),
        ("M5", "tau(F) = 0 iff F(0) = 0: two dormant crowds merge dormant; dormant + live is always live; literal (d) is impossible", "PROVED [derived, shown]",
         f"{_n(c['both_dormant'] + ec('both_dormant'))} dormant-dormant; {_n(c['dormant_plus_live'] + ec('dormant_plus_live'))} dormant-live",
         c["viol_both_dormant"] + ec("both_dormant_viol") + c["dormant_plus_live_dead"] + ec("dormant_plus_live_dead")),
        ("M6", "first step: the merge recruits beyond its instigators iff (smallest positive threshold) <= lam m_1 + (1-lam) m_2, m_i = F_i(0)", "PROVED [derived, shown]",
         _n(Pm + EXH), c["viol_firststep"] + ec("firststep_mismatch") + ec("firststep_mismatch_part")),
        ("M7", "ignition above max needs F_low(tau_high) > tau_high; the weights that ignite form an interval (0, lam*); with a margin, latent pressure is also sufficient", "PROVED [derived, shown]",
         f"{_n(Pm + EXH)} pairs; {_n(sweep['ign_somewhere'] + smex.get('grid_ign', 0))} windows", c["viol_ign_without_latent"] + ec("ign_no_latent") + small.get("viol_nonlatent_ign", 0)
         + sweep.get("viol_downward_closure", 0) + smex.get("viol_downward_closure", 0) + sweep.get("viol_window_not_contiguous", 0)),
        ("M8", "split corollaries: min(tau_A, tau_B) <= tau(whole); no split makes both parts strictly more active; cut by threshold, tau_B <= tau <= tau_A", "PROVED [derived, shown]",
         f"{_n(sum(cc['splits'] for cc in splits.values()))} splits; {_n(splex['cascading_wholes'])} wholes x all bipartitions", split_viol + splex["some_split_lifts_both"]),
        ("M9", "certificate: rho(Gamma_B) <= rho(Gamma) (models/01 Thm 2.1) and rho(Gamma_m) >= max rho_i", "PROVED (models/01; Perron-Frobenius)",
         f"{_n(cert['blocks'])} blocks; {_n(cert['merges'])} merges", cert["viol_split_monotone"] + cert["viol_merge_ge_max"]),
        ("M10", "if neither part recruits (tau_i = F_i(0)) then tau_m >= lam tau_1 + (1-lam) tau_2; so violating \"tau_m >= average\" needs a recruiting part", "PROVED [derived, shown]",
         _n(c["norec_pairs"] + ec("norec_pairs")), c["viol_norec_below_avg"] + ec("norec_below_avg_viol")),
        ("N", "tau_m is not a function of (tau_1, tau_2, n_1, n_2)", "PROVED by example (section 5)", "2 pairs", 0),
        ("F1", "tau_m <= max(tau_1, tau_2) for all pairs", "FALSE", _n(Pm + EXH), f"{_n(ign + ec('ign'))} violate"),
        ("F2", "tau_m >= lam tau_1 + (1-lam) tau_2", "FALSE", _n(Pm + EXH), f"{_n(c['lt_avg'] + ec('lt_avg'))} violate"),
        ("F3", "tau_m <= lam tau_1 + (1-lam) tau_2", "FALSE", _n(Pm + EXH), f"{_n(c['gt_avg'] + ec('gt_avg'))} violate"),
        ("F4", "latent pressure is sufficient for ignition at some weight (no margin assumed)", "FALSE (ties)", _n(smex['latent_ordered']),
         f"{_n(smex['never'])} violate"),
        ("C1", "iid crowds from one transversal population: P(ignition) -> 0 as n -> infinity", "OPEN (section 4.8)", "see 4.8", "n/a"),
    ]
    tbl(["id", "statement", "status", "checked", "violations"], rows, left=(0, 1, 2))

    # ---------------------------------------------------------------- 3 proofs
    w("## 3. Proofs (short; the first one carries the rest)")
    w("")
    w("**Fact 0.** tau(F) = min P(F). *Proof.* Run the orbit one step earlier, from 0: rho_0 = 0, rho_1 = F(0) (the problem's r(0)), rho_{t+1} = F(rho_t). Its limit r* satisfies F(r*) = r* (v0.1 Thm 6.3(i)), so r* is in P(F). If r is in P(F), then rho_0 = 0 <= r, and rho_t <= r implies rho_{t+1} = F(rho_t) <= F(r) <= r, so r* <= r. (This is the Knaster-Tarski reading of Thm 6.3.) "
      "Because F_lam is affine in lam, **E_{F_lam} = lam E_1 + (1 - lam) E_2**, and r is in P(F_lam) iff that combination is <= 0.")
    w("")
    w("**M1 and M2.** If lam E_1(r) + (1-lam) E_2(r) <= 0 then E_1(r) <= 0 or E_2(r) <= 0, so P(F_lam) is contained in P_1 union P_2; if both are <= 0 so is the combination, so P_1 intersect P_2 is contained in P(F_lam). "
      "Take minima: min(tau_1, tau_2) <= tau_m <= min(P_1 intersect P_2). Since P(min(F_1,F_2)) = P_1 union P_2 and P(max(F_1,F_2)) = P_1 intersect P_2, the two bounds are exactly tau(min(F_1,F_2)) and tau(max(F_1,F_2)): "
      "**the sandwich in (c) is an identity, and neither end can be improved from the parts' equilibria alone** (the lower end can be approached, to within about one grid step, when F_2 hugs the diagonal from above up to tau_2 and F_1 drops far below it after tau_1). "
      "In terms of (tau_1, tau_2) alone nothing better than min <= tau_m <= 1 is valid: for (tau_1, tau_2) = (0, 1/2) the merged value can be anything from 1/3 to 1 (proposition N and section 5).")
    w("")
    w("**M3.** F <= G pointwise gives P(G) contained in P(F), hence tau(F) <= tau(G). If F_1 <= F_2 then F_1 <= F_lam <= F_2.")
    w("")
    w("**M4.** tau(F) >= c iff F(r) > r for every r < c: a family of strict *linear* inequalities, so {F : tau(F) >= c} is convex. "
      "Hence for any mixture of any number of crowds tau >= the least of the parts; c = 1 gives (a); and {lam : tau(F_lam) >= c} is an interval for every c, i.e. lam -> tau(F_lam) is unimodal.")
    w("")
    w("**M5.** tau(F) = 0 iff r(0) = F(0) = 0. F_lam(0) = lam F_1(0) + (1-lam) F_2(0) is zero iff both are (for 0 < lam < 1). So (d) as literally stated cannot happen, and a dormant crowd merged with any live crowd is live.")
    w("")
    w("**M6.** Let m = F(0) and theta+ the smallest positive threshold. The orbit starts at m, so tau = m iff F(m) = m iff no member has theta in (0, m] iff theta+ > m. For the merge, m = lam m_1 + (1-lam) m_2 and theta+ = min(theta+_1, theta+_2). "
      "*Reading:* two crowds that each recruit nobody (theta+_i > m_i) merge into one that does exactly when the smaller least threshold, say theta+_1, satisfies theta+_1 <= lam m_1 + (1-lam) m_2; "
      "this needs m_2 > theta+_1 > m_1, i.e. the other crowd's instigators, diluted by the weights, reach the first rung of the ladder. Whether the cascade then runs on is not decided by the first step.")
    w("")
    w("**M7.** Let tau_1 < tau_2 and let lam be the weight of F_1. (i) If F_1(tau_2) <= tau_2 then tau_2 is in P_1 intersect P_2, so tau_m <= tau_2 for **every** lam (M2): ignition needs F_low(tau_high) > tau_high. "
      "(ii) tau_m > tau_2 iff E_lam > 0 on [0, tau_2]. For 0 < lam' < lam, E_lam' = (lam'/lam) E_lam + (1 - lam'/lam) E_2 with E_2 >= 0 on [0, tau_2], so E_lam' > 0 too: **the ignition set is downward closed in the intruder's weight**, "
      "an interval (0, lam*). (iii) If moreover eps := inf over r < tau_2 of E_2(r) is > 0 (a margin; generic for continuous thresholds) and E_1(tau_2) > 0, then E_lam >= -lam + (1-lam) eps > 0 below tau_2 and E_lam(tau_2) = lam E_1(tau_2) > 0 at tau_2, "
      "so every lam < eps/(1+eps) ignites: a small enough group with latent pressure at a stalled crowd's stall point restarts it. "
      "Without a margin (iii) fails, e.g. F_2 = 1/2 on [0, 2/3) touches the diagonal from above at its own equilibrium 1/2: F4 and section 5.")
    w("")
    w("**M8 (split).** F = lam_A F_A + lam_B F_B, so M1 to M7 apply with the parts in the roles of crowds. (i) min(tau_A, tau_B) <= tau(F): **no split makes both parts strictly more active than the whole.** "
      "(ii) Both parts strictly *less* active is exactly ignition read backwards, so a split can kill a cascade. (iii) tau(F) = 0 iff both parts are dormant, so the literal (e) is impossible. "
      "(iv) If A = {theta <= c} and B = {theta > c} then F_B <= F <= F_A, so tau_B <= tau <= tau_A (M3): cutting by threshold can never kill. (v) With a fair coin and z instigators, "
      "P(some part has none) = 2^(1-z), and a part with none is dormant: this is the dominant way random splits kill (table E).")
    w("")
    w("**M10.** tau_m >= F_m(0) = lam F_1(0) + (1-lam) F_2(0). If tau_i = F_i(0) for both parts (neither recruits beyond its instigators) the right side is lam tau_1 + (1-lam) tau_2. "
      "So pooling instigators is at least additive; \"tau_m >= average\" can fail only when some part is a partial or full cascade (table B: the D x D, D x I and I x I rows have no pair below the average).")
    w("")
    w("**N (non-compositionality).** Pair 1: {1/6} with {0, 2/3}. Pair 2: {1} with {0, 2/3}. Both have (n_1, n_2) = (1, 2), tau_1 = 0, tau_2 = 1/2; the merged equilibria are given in section 5 (1 and 1/3). "
      "In general tau_m depends on E_1, E_2 only through their values on [0, tau_m], which is why a *distribution* is needed as the group state.")
    w("")

    # ---------------------------------------------------------------- 4 tables
    w("## 4. Results")
    w("")
    w("### 4.1 Table A: Q1 and Q2 on random pairs, by scenario")
    w("")
    w("`elig(avg)` = pairs that are neither two dormant nor two full crowds (otherwise tau_m = average trivially). `elig(ign)` = pairs with no full crowd and not two dormant (the only pairs that can ignite). "
      "Percentages of tau_m < avg and tau_m > avg are of elig(avg); ignition is of elig(ign).")
    w("")
    rows = []
    for s in SCENARIOS + ["ALL"]:
        t = TOT if s == "ALL" else S[s]
        cc = t.c
        ea = cc["pairs"] - cats(t, "DD") - cats(t, "FF")
        ei = sum(cats(t, k) for k in ign_cats)
        rows.append((s, _n(cc["pairs"]), _n(ea), _n(cc["viol_below_min"]), _n(cc["ign"]), _pc(cc["ign"], ei), _n(cc["lt_avg"]), _pc(cc["lt_avg"], ea),
                     _n(cc["gt_avg"]), _pc(cc["gt_avg"], ea)))
    tbl(["scenario", "pairs", "elig(avg)", "tau_m < min", "tau_m > max (ignition)", "of elig(ign)", "tau_m < avg", "of elig(avg)", "tau_m > avg", "of elig(avg)"], rows)
    w("Read: the `tau_m < min` column is the theorem M1 (zero everywhere). `gran` merges fall below the average in the large majority of non-trivial pairs: Granovetter-type crowds are marginal "
      "(F(r) = r + 1/n), so a merge, which re-expresses every threshold as a fraction of a different size, nearly always opens a gap early.")
    w("")
    w("### 4.2 Table B: who ignites (category pairs, all scenarios pooled)")
    w("")
    rows = []
    for k in ("DD", "DI", "DP", "DF", "II", "IP", "FI", "PP", "FP", "FF"):
        pr = sum(S[s].cat[k]["pairs"] for s in S)
        ig = sum(S[s].cat[k]["ign"] for s in S)
        lt = sum(S[s].cat[k]["lt_avg"] for s in S)
        gt = sum(S[s].cat[k]["gt_avg"] for s in S)
        rows.append(({"FI": "I x F", "FP": "P x F"}.get(k, f"{k[0]} x {k[1]}"), _n(pr), _n(ig), _pc(ig, pr), _n(lt), _n(gt), "can ignite" if k in ign_cats else "cannot (max = 1, or both dormant)"))
    tbl(["pair", "pairs", "ignition", "rate", "tau_m < avg", "tau_m > avg", ""], rows)
    w("(F x F includes the 40,000 `full` pairs.)")
    w("")
    w("Ignition is not a dormant-crowd phenomenon: pairs of inert crowds (I x I) and of partial cascades (P x P) ignite. What they share is latent pressure: "
      f"in {_n(c['latent'])} pairs the lower crowd's map lies above the diagonal at the higher crowd's equilibrium, and {_n(c['latent_and_ign'])} of those ignited at their natural weight "
      f"(the rest are blocked, either by dilution, the natural lam being above lam*, or by a tie, F4). The first-step version (M6): "
      f"{_n(c['created_live'])} random pairs and {_n(ec('created_strict'))} exhaustive pairs are two crowds that both have instigators, are not saturated, and recruit nobody, "
      f"merging into one that does (counting dormant members of the pair as recruiting nobody: {_n(c['created'])} and {_n(ec('created'))}).")
    w("")
    w("### 4.3 Table C: size of the effect")
    w("")
    indep = ("uniform", "beta", "bimodal", "normal", "atoms", "mixed")
    w("Left block: independent populations (the six scenarios other than `gran`, `full`, `sameG`, which would distort the size mix). Right block: `sameG`. "
      "`ignition` is of the pairs that can ignite; the averages are of the pairs where they can differ.")
    w("")
    rows = []
    for k in ("N<100", "100-999", "1000-9999", ">=10000"):
        ei = sum(S[s_].nb[k]["elig_ign"] for s_ in indep)
        ea = sum(S[s_].nb[k]["elig"] for s_ in indep)
        ig = sum(S[s_].nb[k]["ign"] for s_ in indep)
        lt = sum(S[s_].nb[k]["lt_avg"] for s_ in indep)
        gt = sum(S[s_].nb[k]["gt_avg"] for s_ in indep)
        sp = S["sameG"].nb[k]
        rows.append((k, _n(ei), _pc(ig, ei), _pc(lt, ea), _pc(gt, ea), _n(sp["elig_ign"]), _pc(sp["ign"], sp["elig_ign"])))
    tbl(["N = n_1 + n_2", "can-ignite pairs", "ignition", "tau_m < avg", "tau_m > avg", "can-ignite sameG", "ignition sameG"], rows)
    b1 = np.mean(ov < 0.01); b2 = np.mean((ov >= 0.01) & (ov < 0.1)); b3 = np.mean((ov >= 0.1) & (ov < 0.5)); b4 = np.mean(ov >= 0.5)
    w(f"Overshoot tau_m - max among the {_n(len(ov))} random ignitions: median {np.median(ov):.4f}, maximum {ov.max():.4f}; "
      f"{100 * b1:.0f}% are under 0.01, {100 * b2:.0f}% are 0.01 to 0.1, {100 * b3:.0f}% are 0.1 to 0.5 and {100 * b4:.0f}% are above 0.5 "
      "(small overshoots are one more member or a few joining; large ones are the merge running a whole ladder of rungs). "
      "Ignition barely changes with size for independent populations (it stays within a few points of its overall rate); it falls steadily for crowds drawn from one population (right block, and table G).")
    w("")
    w("### 4.4 Ordered pairs, monotonicity, sweeps in the mixing weight")
    w("")
    w(f"- **M3** [computed]: {_n(mono['trials'])} coupled pairs (crowd 2 = crowd 1, possibly replicated 1 to 3 times, with random members' thresholds lowered; sizes up to 30,000): "
      f"tau_1 <= tau_2 in all ({_n(mono['strict'])} strictly), tau_1 <= tau_m <= tau_2 in all ({_n(mono['strictly_between'])} strictly inside). Plus {_n(ec('ordered'))} ordered pairs in the exhaustive enumeration, 0 violations.")
    w(f"- **M4/M7** [computed]: {_n(sweep['trials'])} sweeps over lam = j/20 (equal sizes up to 200, 6 families): lam -> tau(F_lam) was non-monotone in {_n(sweep['nonmonotone'])} of them, "
      f"the same number as there are ignition windows (as it must be: a unimodal profile that is not monotone has to rise above its starting end); quasi-concavity violations: {sweep['viol_quasiconcave']}; ignition windows that were not of the form (0, lam*] on the grid: {sweep['viol_downward_closure']} "
      f"(and {smex.get('viol_downward_closure', 0)} in the tie-heavy exhaustive set); ignitions with tau_1 = tau_2: {sweep['viol_equal_tau_ignition']}.")
    w(f"- **M7 sufficiency** [computed]: among {_n(small['latent'])} generic (continuous-threshold) pairs with latent pressure, {_n(small['latent_ign_some_lam'])} ignite at some lam = 2^-j, j <= 30 "
      f"({_n(small['first_j_1'])} already at lam = 1/2, {_n(small['first_j_2'])} first at 1/4); none of {_n(small['nonlatent'])} pairs without it ignites. With ties allowed (thresholds on a coarse grid, exhaustive, n <= 4, K = 6): "
      f"{_n(smex['never'])} of {_n(smex['latent_ordered'])} latent ordered pairs never ignite at any lam = 2^-j, which is F4.")
    w(f"- **Two-atom closed form** [computed]: for crowds with z_i instigators and the rest at one threshold s_i (s_1 <= s_2), N = n_1 + n_2, tau_m = (z_1+z_2)/N if (z_1+z_2)/N < s_1; "
      f"else 1 if (n_1+z_2)/N >= s_2; else (n_1+z_2)/N. Checked against the exact merge in {_n(R['atoms']['trials'])} random draws, {R['atoms']['viol_formula']} mismatches "
      f"({_n(R['atoms']['ign'])} of them ignitions). Example below.")
    w("")
    w("Example sweep: crowd 1 = 100 members all at 0.05 (dormant); crowd 2 = 100 members, 10 at 0 and 90 at 0.5 (tau_2 = 0.1). lam = weight of crowd 1.")
    w("")
    rows = [(str(l), str(t), f"{float(t):.3f}") for l, t in R["sweep_ex"]]
    half = (len(rows) + 1) // 2
    tbl(["lam", "tau_lam", "decimal", "lam ", "tau_lam ", "decimal "], [rows[i] + (rows[i + half] if i + half < len(rows) else ("", "", "")) for i in range(half)])
    w("tau_lam rises above both parts for lam in (0, 1/2] (latent pressure: crowd 1 is entirely at 0.05 <= 0.1), reaches 1 for lam in [4/9, 1/2] (the merged share clears crowd 2's rung at 0.5), "
      "and collapses to below 0.05 once the intruders dilute the instigators below crowd 1's threshold (lam > 1/2).")
    w("")
    w("### 4.5 Table D: splits")
    w("")
    w("Wholes are random crowds (7 families, 20 to 10,000 members) that **cascade** (tau > F(0)). Rules: fair coin; coin with random p; cut by threshold rank (lowest p to part A); threshold rank plus noise (sd 0.2 n); "
      "all instigators to A plus a random half of the rest. `kill` = both parts strictly below the whole; `kill (first step)` = both parts recruit nobody.")
    w("")
    rows = []
    for rule, cc in splits.items():
        cw = cc["cascading_wholes"]
        rows.append((rule, _n(cc["splits"]), _n(cw), _n(cc["kill_both_below"]), _pc(cc["kill_both_below"], cw), _pc(cc["kill_both_inert"], cw),
                     _pc(cc["some_part_dormant"], cw), _pc(cc["some_part_above"], cw), _pc(cc["full_both_lt1"], cc["whole_full"])))
    tbl(["rule", "splits", "cascading wholes", "kill", "of cascading", "kill (first step)", "a part dormant", "a part above whole", "tau = 1 whole, both parts < 1"], rows)
    w(f"Never observed: both parts strictly above the whole (M8(i)); whole with tau > 0 and both parts dormant (M5); cut-by-threshold violating tau_B <= tau <= tau_A "
      f"({sum(cc['viol_threshold_sandwich'] for cc in splits.values())} violations). Exhaustive: of {_n(splex['cascading_wholes'])} cascading wholes with 4 to 9 members and thresholds on a grid of 1/12, "
      f"{_n(splex['some_split_kills'])} ({_pc(splex['some_split_kills'], splex['cascading_wholes'])}) have **some** bipartition that kills the cascade, "
      f"including {_n(splex['full_some_split_kills'])} of {_n(splex['full_wholes'])} full-cascade wholes; {splex['some_split_lifts_both']} have a bipartition with both parts strictly above.")
    w("")
    w("### 4.6 Table E: why fair-coin splits kill, by number of instigators in the whole")
    w("")
    rows = []
    for k in ("1", "2-3", "4-9", "10-49", ">=50"):
        z = zb[k]
        rows.append((k, _n(z["cascading"]), f"{z['exp_dormant']:.1f}", _n(z["dormant_part"]), _n(z["kill"]), _pc(z["kill"], z["cascading"])))
    tbl(["instigators z", "cascading wholes", "expected with a dormant part (2^(1-z))", "observed", "kill", "kill rate"], rows)
    w("The expected and observed counts of splits that leave a part without any instigator agree; with one instigator one part is always dormant. "
      "Kills with many instigators exist but are rare (near-critical wholes). This is Granovetter's own sampling point (his p. 1431: a random crowd of 100 has no instigator with probability .37), seen from the split side.")
    w("")
    w("### 4.7 Table F (Q4): the certificate, by contrast")
    w("")
    tbl(["", "certificate rho(Gamma)", "equilibrium tau(F)"],
        [("whole vs parts under split", f"rho(Gamma_B) <= rho(Gamma): {cert['blocks'] - cert['viol_split_monotone']:,} of {cert['blocks']:,} blocks (0 violations)",
          f"parts both above whole: never; some part above: {_pc(splits['coin(1/2)']['some_part_above'], splits['coin(1/2)']['cascading_wholes'])}; both below (kill): {_pc(splits['coin(1/2)']['kill_both_below'], splits['coin(1/2)']['cascading_wholes'])}"),
         ("whole vs parts under merge", f"rho(Gamma_m) >= max(rho_1, rho_2): 0 violations in {cert['merges']:,}; {_pc(cert['merge_uncertified'], cert['merges'])} of merged pairs are uncertified (random cross gains up to 1; says nothing about real groups)",
          f"tau_m >= min only; above max in {_pc(ign, elig_ign)} of possible pairs; below the average in {_pc(c['lt_avg'], elig_avg)}"),
         ("inheritance", "hereditary: certified whole implies certified parts", "not hereditary: a cascading whole can have only dormant or inert parts")])
    w("One line: the certificate is a *worst-case over interactions* quantity, so the whole dominates every part; the equilibrium is a *mixture* quantity, so the whole dominates only the least active part. "
      "That is the asymmetry between the two kinds of group state: the set \"certified\" (rho < 1) is closed under split and not under merge; the set \"full cascade\" (tau = 1, or tau >= c) is closed under merge (M4) and not under split.")
    w("")
    w("### 4.8 Table G: same-population crowds (the open item C1)")
    w("")
    w(f"{len(R['pops'])} random Beta populations with instigator share z in {{.02, .1}}; for each, pairs of independent samples of equal size n; ignition rate (tau_m > max). "
      "`transversal` = the population's own first crossing has slope F_G'(tau_G) < 0.7; `near-critical` = slope >= 0.7.")
    w("")
    rows = []
    for n, cc in samepop.items():
        rows.append((_n(n), _n(cc["trans_pairs"]), _n(cc["trans_ign"]), _pc(cc["trans_ign"], cc["trans_pairs"], 2), _n(cc["crit_pairs"]), _n(cc["crit_ign"]), _pc(cc["crit_ign"], cc["crit_pairs"])))
    tbl(["n per crowd", "transversal pairs", "ignitions", "rate", "near-critical pairs", "ignitions", "rate"], rows)
    ns = sorted(samepop)
    r0 = samepop[ns[0]]["trans_ign"] / samepop[ns[0]]["trans_pairs"]
    r1 = max(samepop[ns[-1]]["trans_ign"], 1) / samepop[ns[-1]]["trans_pairs"]
    slope = np.log(r1 / r0) / np.log(ns[-1] / ns[0])
    tot_ev = sum(samepop[n_]["trans_ign"] for n_ in ns)
    ncrit = sum(1 for p_ in R["pops"] if p_[4] >= 0.7)
    last = samepop[ns[-1]]
    w(f"Over n = {ns[0]} to {ns[-1]:,} the transversal rate falls from {100 * r0:.2f}% to {last['trans_ign']} event{'s' if last['trans_ign'] != 1 else ''} in {last['trans_pairs']:,} pairs "
      f"(a two-point log-log slope of about {slope:.2f}, counting at least one event); the {ncrit} near-critical populations fall far more slowly. "
      "*Heuristic for C1:* for a transversal crossing, tau_i - tau_G is to first order a linear functional of the empirical process at tau_G, divided by 1 - G'(tau_G); the pooled sample gives the same functional of the pooled process, "
      "which is the lam-weighted average of the two. So to first order tau_m lies **between** tau_1 and tau_2, and ignition needs second-order or discreteness effects, of relative size n^(-1/2). "
      f"Not proved: the slope rests on {tot_ev} transversal events in all.")
    w("")

    # ---------------------------------------------------------------- 5 examples
    w("## 5. Counterexamples and examples with their thresholds")
    w("")
    w("Smallest cases found by exhaustive enumeration (all unordered pairs of crowds with 1 to 3 members and thresholds in {0, 1/12, ..., 1}, and with 1 to 5 members and thresholds in {0, 1/6, ..., 1}; the two sets overlap, so \"exhaustive pairs\" counts evaluations); \"smallest\" is by merged size.")
    w("")
    ex = R["exh"]
    w("**F1: tau_m > max (ignition), N = 3.**")
    w(_ex_line(ex, "ign", " Latent pressure: F_1(1/2) = 1 > 1/2."))
    w("")
    w("**F1 with both crowds live (each has an instigator), smallest:**")
    w(_ex_line(ex, "ign_live"))
    w("")
    w("**F2: tau_m < lambda-average (dilution), N = 3, and with both crowds live:**")
    w(_ex_line(ex, "lt_avg"))
    w(_ex_line(ex, "lt_avg_live"))
    w("")
    w("**F3: tau_m > lambda-average (instigators pooled), both crowds live:**")
    w(_ex_line(ex, "gt_avg_live"))
    w("")
    w("**(d) done right (M6): two crowds that each have instigators, are not saturated and recruit nobody, merging into one that cascades. Smallest:**")
    w(_m6_line(ex))
    w("")
    w("**(e) done right: a whole with tau = 1 whose two conditional parts are both strictly below 1 (a merge read backwards); smallest, then smallest with an instigator in each part:**")
    w(_split_line(ex, "kill_full"))
    w(_split_line(ex, "kill_full_live"))
    w("")
    w("**N: the same (tau_1, tau_2, n_1, n_2) = (0, 1/2, 1, 2), different merged equilibria** (computed here):")
    tA, tB = lfp_small((1, 0, 4), 6), lfp_small((6, 0, 4), 6)
    w(f"- {{1/6}} with {{0, 2/3}}: merged {{0, 1/6, 2/3}}, tau_m = {tA}.")
    w(f"- {{1}} with {{0, 2/3}}: merged {{0, 2/3, 1}}, tau_m = {tB}.")
    w("")
    n_ = 1000
    unit_ = D // n_
    a1_ = np.sort(np.array([0] * 200 + [D] * 800, dtype=np.int64))
    a2_ = np.sort(np.concatenate((np.arange(800, dtype=np.int64) * unit_, np.full(200, D, dtype=np.int64))))
    rs = analyse_pair(a1_, a2_)
    w("**Sharpness of the lower bound (M1/M2), computed here.** Crowd 1: 200 instigators and 800 members who never join (tau_1 = " + str(rs["t1"]) + "). "
      "Crowd 2: the Granovetter staircase 0, 1/1000, ..., 799/1000 plus 200 members who never join, so its map hugs the diagonal from above up to tau_2 = " + str(rs["t2"]) + ". "
      "Equal sizes, merged: **tau_m = " + str(rs["tm"]) + " = " + f"{float(rs['tm']):.4f}" + "**, only " + f"{float(rs['tm'] - rs['lo']):.4f}" + " above min(tau_1, tau_2) = " + _fx(rs["lo"]) + " (within one grid step), and far below the average " + _fx(rs["avg"]) + ".")
    w("")
    (cntK, best) = R["smex"]
    nv = _crowd(best[2], 6), _crowd(best[3], 6)
    tK = lfp_small(tuple(sorted(best[2] + best[3])), 6)
    w(f"**F4: latent pressure without ignition at any weight (a tie).** Crowd 1 = {nv[0]}, crowd 2 = {nv[1]}: tau_1 = 0, tau_2 = 1/2, and F_1(1/2) = 1 > 1/2, yet crowd 2's map equals 1/2 on [0, 2/3), "
      "so the merged instigator share (1-lam)/2 is below crowd 1's threshold 1/2 for every lam > 0: no first step, whatever the weight (at the natural weight lam = 1/3 the merge has tau_m = " + str(tK) + "). Crowd 2 has no margin, which is what M7(iii) needs.")
    w("")
    w("**Granovetter's two crowds, merged** (G0 = {0, 1/n, ..., (n-1)/n}, tau = 1; G1 = G0 with the member at 1/n moved to 2/n, tau = 1/n). Merged size n_1 + n_2.")
    w("")
    rows = [(f"{a} (n={n1})", f"{b} (n={n2})", _fx(t1), _fx(t2), _fx(tm, 400), _fx(av, 400)) for (n1, a, n2, b, t1, t2, tm, av) in R["gran"]]
    tbl(["crowd 1", "crowd 2", "tau_1", "tau_2", "tau_m", "lam-average"], rows)
    w("G0 with G0 is full (M4). G0 with G1 at equal n collapses to 1.5/n: far below the average, because the merged share starts at 1/n, clears the first rung (G0's member at 1/n), reaches 1.5/n, and stops below the next rung at 2/n. "
      "The two crowds that Granovetter called \"essentially identical\" merge to an outcome that is neither of theirs.")
    w("")

    # ---------------------------------------------------------------- 6 conjectures
    w("## 6. What I would carry into `models/02`, and what I would not")
    w("")
    w("**Carry (proved here, short, to be audited):**")
    w("")
    w("1. *Merge sandwich.* P_1 intersect P_2 is contained in P(F_lam), which is contained in P_1 union P_2; so min(tau_1,tau_2) <= tau(F_lam) <= tau(max(F_1,F_2)) for every lam, "
      "and both ends are identities for the maps min(F_1,F_2) and max(F_1,F_2). Consequences: {tau >= c} is convex (tau is quasi-concave on CDFs, unimodal in lam); both-full merges are full; a merge is never below both parts; no split makes both parts strictly more active than the whole.")
    w("2. *Ignition.* Above the higher part needs F_low(tau_high) > tau_high; the weights that ignite form an interval (0, lam*); with a margin, latent pressure suffices for small weights; "
      "the first step is exact (merged instigator share >= least positive threshold).")
    w("3. *Non-compositionality, and what composes.* tau does not compose (N); the excess E_F does, linearly under mixture, and tau is its first non-positive point. "
      "That is the precise sense in which a group's drive state is a distribution and not a mean or an equilibrium.")
    w("4. *Mean-type statements are false* (F1 to F3). Do not write \"the merged equilibrium is between / above / below the average\" anywhere.")
    w("5. *Asymmetry with the certificate.* Certificate: hereditary under split (models/01 Thm 2.1), merge >= max of parts. Equilibrium: merge >= min of parts, split not hereditary. "
      "This is the formal content of \"a group is more than its members\" for the cascade side.")
    w("")
    w("**Conjecture (open, section 4.8).** C1: for crowds that are iid samples of a population G with a transversal first crossing (G(r) > r below tau_G, G'(tau_G) < 1, G(0) > 0), "
      "P(tau_m > max(tau_1, tau_2)) -> 0 as n_1, n_2 -> infinity with n_1/n_2 fixed, at rate about n^(-1/2).")
    w("")
    w("**Not done, and where the next numerics should go.** (1) The two-sided gate of v0.1 (F = F_theta - F~, non-monotone): there is no least fixed point in general and none of this applies. "
      "(2) Partial mixing: the merge here has every member respond to the pooled share; a homophily weight h (respond to (1-h) own crowd + h pooled) interpolates between two separate crowds and the full merge, "
      "and is the natural Granovetter-style social-structure extension. (3) Merges of more than two crowds: M1 to M4 hold verbatim (convexity), M6 and M7 need restating. "
      "(4) Thresholds as counts rather than fractions (a merge that does not dilute) would change every result about dilution; v0.1 uses fractions, so this page does.")
    w("")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    main()
