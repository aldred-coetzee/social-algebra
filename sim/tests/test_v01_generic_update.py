"""Smoke test of v0.1's generic update (3.0) with D1 + D2 + D3 at n = 3 and n = 10,
and Theorem 6.2 (decoupling under closed gates).

Prior-work files: 059 / 20 section 1 for D1 and the O-jive (Gottman-Murray 1999).
Ledger: L0853, L2096 (uninfluenced steady state a/(1-r), stable iff |r|<1), L0857 (O-jive:
zero inside a band, bounded constants beyond), L4367/L4368 (two-regime inertia),
L3864 (goal term), and v0.1 3.0-3.3, 6.2 (models/00-v0.md).  Deterministic; no data.
"""
import numpy as np
import pytest
from models import v01

SIZES = (3, 10)


def _setup(n, with_d3=False, seed=0):
    rng = np.random.default_rng(seed + n)
    P = v01.random_params(n, rng, gate=5.0, with_d3=with_d3)
    return P, rng.uniform(-2, 2, n)  # |x| < gate: all gates closed from the start


@pytest.mark.parametrize("n", SIZES)
def test_theorem_62_closed_gates_decouple_to_set_point(n):
    """Claim (v0.1 6.2, L0853, L0857, L2096): with every incoming signal inside the gate,
    D2 = 0 and each x_i is an independent recursion that approaches p_i monotonically, the
    error shrinking by exactly r_i^- (below p_i) or r_i^+ (above) each turn, i.e. at rate
    1 - r_i.  D3 absent."""
    P, x0 = _setup(n)
    traj = v01.run(x0, P, 60)
    assert np.abs(traj).max() < 5.0  # the gates really stay closed throughout
    e = traj - P.p
    r = np.where(traj[:-1] < P.p, P.r_minus, P.r_plus)
    assert (e[1:] == pytest.approx(r * e[:-1], abs=1e-12))     # geometric, regime-wise
    assert np.all(e[1:] * e[:-1] >= 0)                          # never crosses p_i: monotone
    assert traj[-1] == pytest.approx(P.p, abs=1e-4)


@pytest.mark.parametrize("n", SIZES)
def test_open_gate_breaks_decoupling(n):
    """Control for 6.2: pushing one member past K+ makes the others respond (D2 != 0),
    so the closed-gate result is a statement about the gate, not a vacuous one."""
    P, x0 = _setup(n)
    x0 = x0.copy(); x0[0] = 9.0
    x1 = v01.step(x0, P)
    pure_d1 = x0 - (1 - np.where(x0 < P.p, P.r_minus, P.r_plus)) * (x0 - P.p)
    assert np.abs(x1[1:] - pure_d1[1:]).max() > 0.1


@pytest.mark.parametrize("n", SIZES)
def test_d3_changes_the_limit_so_62_needs_d3_absent(n):
    """Finding on the wording of 6.2 ('D1 (+ D3) alone ... x_i -> p_i at rate 1 - r_i').
    With D3 present and g_i != p_i, the closed-gate fixed point is
    x* = ((1-r) p + omega g)/((1-r) + omega), not p_i, and the rate is 1 - r + omega.
    The theorem as worded is true only for D3 absent (or omega = 0); asserted here as such."""
    P, x0 = _setup(n, with_d3=True)
    traj = v01.run(x0, P, 400)
    r = np.where(traj[-2] < P.p, P.r_minus, P.r_plus)
    xstar = ((1 - r) * P.p + P.omega * P.g) / ((1 - r) + P.omega)
    assert traj[-1] == pytest.approx(xstar, abs=1e-6)
    assert np.abs(traj[-1] - P.p).max() > 1e-3  # not p_i


@pytest.mark.parametrize("n", SIZES)
def test_update_is_deterministic_and_finite(n):
    """Smoke: (3.0) with all three drives and some gates open runs, is finite and repeatable."""
    P, x0 = _setup(n, with_d3=True)
    x0 = x0.copy(); x0[0] = 7.0
    a, b = v01.run(x0, P, 200), v01.run(x0, P, 200)
    assert np.array_equal(a, b) and np.isfinite(a).all()
