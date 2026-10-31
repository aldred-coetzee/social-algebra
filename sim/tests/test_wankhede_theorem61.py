"""v0.1 Theorem 6.1 / (4.3c): the Wankhede no-split certificate.

Prior-work file: docs/prior-work/090 section 4a (Wankhede, Mandal, Martinez &
Tallapragada, IEEE TCNS 12(1), 5-17, 2025, DOI 10.1109/TCNS.2024.3510590,
arXiv:2404.04912).  Ledger: L3993 (dynamics), L4004 (log-norm, A4, Thm 4.3);
the Euler-turn version is v0.1's own derivation (models/00-v0.md 6.1, [derived]).
"""
import numpy as np
import pytest
from models import wankhede as wk

SEEDS = range(8)


def _system(seed: int, n: int = 6, margin: float = 0.3):
    rng = np.random.default_rng(seed)
    A = wk.random_signed(n, rng)
    F, E = wk.split_weights(A)
    w = 2 * E + margin + rng.uniform(0, 0.5, n)  # A4: w_i > 2 E_i
    p = rng.uniform(-2, 2, n)
    r = rng.uniform(0.5, 2.0, n)
    return rng, A, F, E, w, p, r


@pytest.mark.parametrize("seed", SEEDS)
def test_unique_equilibrium_from_random_starts(seed):
    """Claim (Wankhede Thm 4.3, L4004): under A4, w_i > 2 sum_{enemies} |a_ik| for
    every i, the system has a unique globally exponentially stable equilibrium.
    Every random start must reach the same point, which is a zero of the field."""
    rng, A, F, E, w, p, r = _system(seed)
    ends = np.array([wk.integrate(rng.uniform(-6, 6, len(w)), A, w, p, r) for _ in range(12)])
    assert np.abs(ends - ends[0]).max() < 1e-6
    assert np.abs(wk.rhs(ends[0], A, w, p, r)).max() < 1e-7


@pytest.mark.parametrize("seed", SEEDS)
def test_log_norm_formula(seed):
    """Claim (L4004): mu_inf(J(z)) = max_i[-w_i + 2 sum_{enemies}|a_ik| - 3 z_i^2/r_i]
    (friends' terms cancel) and is negative under A4 at every z."""
    rng, A, F, E, w, p, r = _system(seed)
    for _ in range(5):
        z = rng.uniform(-4, 4, len(w))
        mu = wk.log_norm_inf(wk.jacobian(z, A, w, r))
        assert mu == pytest.approx(np.max(-w + 2 * E - 3 * z**2 / r), abs=1e-10)
        assert mu < 0


@pytest.mark.parametrize("seed", SEEDS)
def test_euler_inf_norm_formula_and_contraction(seed):
    """Claim (v0.1 6.1, [derived]): with h max_i(w_i+F_i+E_i) < 1 the Euler map of the
    linear law has ||I + hJ||_inf = 1 - h min_i(w_i - 2E_i) < 1, and
    mu_inf(J) = -min_i(w_i - 2E_i).  Checked numerically, plus the contraction itself."""
    rng, A, F, E, w, p, r = _system(seed)
    h = 0.9 / np.max(w + F + E)
    M = wk.euler_matrix(A, w, h)
    assert np.all(np.diag(M) > 0)  # the proof's M_ii > 0 step
    assert np.abs(M).sum(1).max() == pytest.approx(1 - h * np.min(w - 2 * E), abs=1e-12)
    assert np.linalg.norm(M, np.inf) < 1
    assert wk.log_norm_inf(wk.jacobian(np.zeros(len(w)), A, w, None)) == pytest.approx(-np.min(w - 2 * E), abs=1e-12)
    # the Euler map itself contracts in the inf-norm and converges to the continuous equilibrium
    f = lambda x: x + h * wk.rhs(x, A, w, p, None)
    x, y = rng.uniform(-5, 5, len(w)), rng.uniform(-5, 5, len(w))
    assert np.abs(f(x) - f(y)).max() <= np.linalg.norm(M, np.inf) * np.abs(x - y).max() + 1e-12
    for _ in range(3000):
        x = f(x)
    assert np.abs(x - wk.integrate(y, A, w, p, None)).max() < 1e-6


def test_counterexample_hostile_pair_weak_anchors_two_attractors():
    """Claim (L4004, converse): the certificate is sufficient only.  Two mutual enemies
    a12 = a21 = -c with anchors w < 2c violate A4; with p = 0 the antisymmetric mode
    u' = (2c - w)u - u^3/r has a pitchfork, giving two stable equilibria (u, -u) and
    (-u, u), u = sqrt(r (2c - w)).  Constructed here (not a published example); with
    w > 2c the equilibrium is unique."""
    c, r = 1.0, 1.0
    A = np.array([[0, -c], [-c, 0.0]])
    rv, p = np.array([r, r]), np.zeros(2)
    for w0, two in ((0.5, True), (2.5, False)):
        w = np.array([w0, w0])
        a = wk.integrate(np.array([1.0, -1.0]), A, w, p, rv)
        b = wk.integrate(np.array([-1.0, 1.0]), A, w, p, rv)
        if two:
            u = np.sqrt(r * (2 * c - w0))
            assert a == pytest.approx([u, -u], abs=1e-6)
            assert b == pytest.approx([-u, u], abs=1e-6)
            for eq in (a, b):  # each is a stable equilibrium (Jacobian eigenvalues negative)
                assert np.linalg.eigvals(wk.jacobian(eq, A, w, rv)).real.max() < 0
            assert w0 < 2 * c  # certificate violated
        else:
            assert a == pytest.approx(b, abs=1e-6)
            assert w0 > 2 * c
