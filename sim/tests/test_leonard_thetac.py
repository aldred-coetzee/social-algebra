"""Leonard, Shen, Nabet, Scardovi, Couzin & Levin 2012, PNAS 109(1), 227-232,
DOI 10.1073/pnas.1118318108: compromise or choose.

Prior-work file: docs/prior-work/086 section 1 (Eqs. 6, 7; the 52, 106 and 90 degree
examples).  Ledger: L3871-L3873 (heading, coupling and slow dynamics), L3874 (Eq. 7,
and the identity theta_c = 2 arccos r, [derived]).  v0.1 (4.3a), (4.3b).

Stability test used: on a coupling manifold (A12, A13, A23) the slow dynamics (Eq. 6) are
solved to equilibrium; the coupling weights then keep their 0/1 values iff, for every pair,
rho_jl - r has the sign that pushes eta the right way (negative for an uncoupled pair, positive
for a coupled one; d eta/dt = K2 (rho - r), L3872).  Eq. 6 is solved numerically, so the
theta_c formula is NOT assumed in the stability test.
"""
import numpy as np
import pytest
from models import leonard as ln

DECISIONS = ((0, 1, 0), (0, 0, 1))  # M010, M001
COMPROMISE = (1, 1, 1)              # M111


@pytest.mark.parametrize("r,deg", [(0.9, 51.7), (0.6, 106.3), (0.707, 90.0)])
def test_theta_c_values(r, deg):
    """Claim (086; L3874, Eq. 7): theta_c = 2 arccos r = arccos(2r^2 - 1); r = 0.9, 0.6,
    0.707 give 51.7, 106.3, 90.0 degrees."""
    assert np.degrees(ln.theta_c(r)) == pytest.approx(deg, abs=0.06)
    assert ln.theta_c(r) == pytest.approx(np.arccos(2 * r**2 - 1))


@pytest.mark.parametrize("r", [0.9, 0.6, 0.707])
@pytest.mark.parametrize("delta", [3.0, 0.5])
def test_decision_manifolds_stable_above_theta_c_only(r, delta):
    """Claim (L3874, Eq. 7): M010 and M001 are both stable iff theta2 > theta_c.  Slightly
    above theta_c (by `delta` degrees): both stable.  Slightly below: neither is.
    N = (5, 5, 11), K1 = 2 (the paper's Fig. 5 parameters)."""
    tc = np.degrees(ln.theta_c(r))
    for m in DECISIONS:
        assert ln.manifold_is_stable(m, np.radians(tc + delta), r)
        assert not ln.manifold_is_stable(m, np.radians(tc - delta), r)


@pytest.mark.parametrize("r", [0.9, 0.6, 0.707])
def test_compromise_stable_below_theta_c(r):
    """Claim (L3874, Eq. 7): M111 is stable for theta2 < theta_c ('stable if')."""
    tc = np.degrees(ln.theta_c(r))
    assert ln.manifold_is_stable(COMPROMISE, np.radians(tc - 3.0), r)


@pytest.mark.xfail(strict=True, reason=(
    "FINDING, not a fit: 086 Table 1 says that with N3 > 2 N1 the compromise M111 is unstable "
    "precisely when M010 and M001 are stable.  With the Fig. 5 parameters (N = 5, 5, 11; K1 = 2) the "
    "transverse test applied to the numerically solved M111 equilibrium finds every pair still coupled "
    "(rho > r) even 20 degrees above theta_c, because K1 N3 / N pulls the two informed headings together. "
    "Either the test used here is only a necessary condition for M111 (its slow-flow stability and "
    "Eq. 8 are not tested), or Table 1 needs conditions this reduction omits.  Unresolved; the "
    "decision-manifold result (Eq. 7) is unaffected."))
@pytest.mark.parametrize("r", [0.9, 0.6, 0.707])
def test_compromise_loses_stability_above_theta_c_table1(r):
    """Claim (086 Table 1, L3874 context): N3 > 2 N1 => M111 unstable exactly when M010/M001 stable."""
    tc = np.degrees(ln.theta_c(r))
    assert not ln.manifold_is_stable(COMPROMISE, np.radians(tc + 3.0), r)


@pytest.mark.parametrize("r", [0.9, 0.6])
def test_full_dynamics_choose_above_compromise_below(r):
    """Claim (086 T1, simulation of Eqs. 3-6 with the coupling dynamics on): started near the
    decision manifold M010 (1 and 3 coupled, 2 uncoupled), the system keeps pair 12 uncoupled
    when theta2 > theta_c and couples it (compromise) when theta2 < theta_c.  Eq. 7 is an
    'iff' for manifold stability; whether a trajectory is attracted is a separate matter
    (086 T1), so only these two clear-margin cases are asserted."""
    tc = np.degrees(ln.theta_c(r))
    y0 = np.array([0.0, 0.0, 0.0, -4.0, 4.0, -4.0])  # eta12, eta13, eta23
    for sign in (+1, -1):
        th2 = np.radians(tc + sign * 8.0)
        y0[1] = th2
        end = ln.simulate_full(th2, r, y0)
        eta12 = end[3]
        if sign > 0:
            assert eta12 < 0
        else:
            assert eta12 > 0
