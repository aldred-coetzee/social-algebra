"""Granovetter 1978, AJS 83(6), 1420-1443, DOI 10.1086/226707: threshold model
r(t+1) = F[r(t)]; and v0.1 Theorem 6.3 (monotone cascade) with the two-sided gate.

Prior-work file: docs/prior-work/066 section 1 (p. 1425 two crowds, pp. 1427 map).
Ledger: L1225 (outcome not a function of the mean), L1831 / L3960 / L3961 (the map and
its first-crossing equilibrium), L1201 (monotone convergence, [derived]), L1235
(cascade operator, [derived]), L3959 (thresholds as net costs and benefits), and v0.1's
two-sided F = F_theta - F~_thetabar (models/00-v0.md 2.3, 4.4, 6.3).
Thresholds are counts out of n, so shares are k/n and all comparisons are exact.
"""
import numpy as np
import pytest
from models import granovetter as gv


def test_two_crowds_equilibria_100_and_1():
    """Claim (L1225, 066 p. 1425): thresholds 0,1,...,99 -> equilibrium 100 (everyone);
    replace the person at 1 by a second person at 2 -> equilibrium 1.  Start r(0) =
    share of zero-threshold members.  Means and spreads are nearly identical."""
    a = np.arange(100)
    b = a.copy(); b[1] = 2
    oa, ob = gv.iterate(a), gv.iterate(b)
    assert oa[0] == 1 and oa[-1] == 100
    assert ob[0] == 1 and ob[-1] == 1
    assert a.mean() == pytest.approx(49.5) and b.mean() == pytest.approx(49.51)
    assert a.std() == pytest.approx(b.std(), rel=1e-3)
    assert gv.F_count(100, a) == 100 and gv.F_count(1, b) == 1  # both are fixed points of F


@pytest.mark.parametrize("seed", range(20))
def test_theorem_63_i_least_fixed_point_within_n_steps(seed):
    """Claim (v0.1 6.3(i), [derived], L1201, L1235): for non-decreasing F with values in
    {0,1/n,...,1} and r(0)=0, r(t+1)=F[r(t)] is non-decreasing, reaches a fixed point in
    at most n steps, and that point is the LEAST fixed point.  F here is the CDF of
    random integer thresholds (Granovetter's own case)."""
    rng = np.random.default_rng(seed)
    n = int(rng.integers(5, 60))
    theta = rng.integers(0, n + 1, n)
    orbit = gv.iterate(theta, start=0)
    assert all(b >= a for a, b in zip(orbit, orbit[1:]))      # monotone
    assert len(orbit) - 1 <= n + 1                             # last step is the repeat
    assert orbit[-1] == gv.least_fixed_point(theta)
    assert gv.F_count(orbit[-1], theta) == orbit[-1]
    # the instigator start r(0)=F(0) is the same orbit shifted by one step
    assert gv.iterate(theta)[-1] == orbit[-1]


@pytest.mark.parametrize("seed", range(10))
def test_two_sided_F_is_difference_of_cdfs(seed):
    """Claim (v0.1 2.3, [derived]): with theta_i <= theta_bar_i, the count of
    {theta_i <= r <= theta_bar_i} equals #{theta_i <= r} - #{theta_bar_i < r}."""
    rng = np.random.default_rng(seed)
    n = 40
    th = rng.integers(0, n + 1, n)
    thb = th + rng.integers(0, n + 1, n)
    for c in range(n + 1):
        assert gv.F_count(c, th, thb) == (th <= c).sum() - (thb < c).sum()


def test_nonmonotone_two_sided_gate_cycles():
    """Claim (v0.1 6.3 corollary): monotone F is a HYPOTHESIS of 6.3.  Constructed (not a
    published example): n=2, person A joined iff r = 0 (theta=0, theta_bar=0), person B
    joined iff r = 1 (theta=theta_bar=2).  F(0)=1, F(1)=0, F(2)=1: no fixed point, orbit
    0 -> 1 -> 0 -> ... cycles, and F is not monotone.  The same people with the upper
    gates removed (theta_bar = infinity) converge as 6.3 says."""
    th, thb = np.array([0, 2]), np.array([0, 2])
    F = [gv.F_count(c, th, thb) for c in range(3)]
    assert F == [1, 0, 1]
    assert not any(F[c] == c for c in range(3))
    orbit = gv.iterate(th, thb, start=0, max_steps=10)
    assert orbit == [0, 1, 0]  # revisits 0: a 2-cycle
    assert gv.F_count(orbit[-1], th, thb) != orbit[-1]  # never settles
    one_sided = gv.iterate(th, start=0)
    assert one_sided[-1] == gv.least_fixed_point(th)
    assert len(one_sided) - 1 <= 2 + 1
