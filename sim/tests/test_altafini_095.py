"""Altafini 2013, IEEE TAC 58(4), 935-946, DOI 10.1109/TAC.2012.2224251 (read as the
author's Sept-2012 manuscript) and Proskurnikov, Matveev & Cao 2016, IEEE TAC 61(6),
1524-1536, DOI 10.1109/TAC.2015.2471655 (arXiv:1508.05034).

Prior-work file: docs/prior-work/095 sections 2-4.  Ledger: L4304 (the flow, eq (4)),
L4307 (Theorem 1), L4308 (Theorem 2), L4310 (Proskurnikov Thm 1), L4311 (their Example 1).
v0.1 (4.2) state layer.  Supersedes the `sa` ledger lines L2270, L3643, L3644 used by the
parked tests/test_altafini.py.
"""
import numpy as np
import pytest
from scipy.integrate import solve_ivp
from models import altafini as al

N = 7


def _flow(A, x0, T):
    """Integrate dx_i/dt = -sum_j |a_ij|(x_i - sgn(a_ij) x_j) (L4304) with an ODE solver."""
    f = lambda t, x: np.array([-sum(abs(A[i, j]) * (x[i] - np.sign(A[i, j]) * x[j]) for j in range(len(x)))
                               for i in range(len(x))])
    return solve_ivp(f, (0, T), x0, rtol=1e-10, atol=1e-12).y[:, -1]


@pytest.mark.parametrize("seed", range(6))
def test_theorem1_balanced_undirected(seed):
    """Claim (L4307, Altafini Thm 1): connected undirected balanced graph => bipartite
    consensus with lim x = (1/n) 1^T D x(0) D 1 (D = diag of the camp signs)."""
    rng = np.random.default_rng(seed)
    A, camp = al.random_signed_graph(N, 0.5, rng, balanced=True)
    assert np.allclose(A, A.T) and al.is_balanced(A)
    x0 = rng.normal(size=N) * 3
    expected = (camp @ x0) / N * camp
    assert _flow(A, x0, 80.0) == pytest.approx(expected, abs=1e-6)
    assert al.simulate(A, x0) == pytest.approx(expected, abs=1e-8)  # matrix-exponential route agrees


@pytest.mark.parametrize("seed", range(6))
def test_theorem1_unbalanced_undirected_goes_to_zero(seed):
    """Claim (L4307): connected undirected UNBALANCED graph => lim x(t) = 0 for all x(0)."""
    rng = np.random.default_rng(50 + seed)
    while True:
        A, _ = al.random_signed_graph(N, 0.6, rng, balanced=False)
        if not al.is_balanced(A):
            break
    assert _flow(A, rng.normal(size=N) * 3, 200.0) == pytest.approx(np.zeros(N), abs=1e-6)


@pytest.mark.parametrize("seed", range(5))
def test_theorem2_strongly_connected_digon_symmetric_digraph(seed):
    """Claim (L4308, Altafini Thm 2): strongly connected, digon sign-symmetric digraph =>
    balanced: lim x = nu^T D x(0) D 1, nu the normalised left null vector of D L D;
    unbalanced: lim x = 0."""
    rng = np.random.default_rng(200 + seed)
    for balanced in (True, False):
        A, camp = al.random_strong_digraph(N, rng, balanced)
        assert al.strongly_connected(A) and not np.any((A * A.T) < 0)  # hypotheses hold
        x0 = rng.normal(size=N) * 3
        x = al.simulate(A, x0, T=400.0)
        if balanced:
            nu = al.left_null(al.signed_laplacian(al.gauge(A, camp)))
            assert x == pytest.approx((nu @ (camp * x0)) * camp, abs=1e-6)
        else:
            assert x == pytest.approx(np.zeros(N), abs=1e-6)


def test_theorem2_weight_balanced_limit_is_the_mean():
    """Claim (L4308): if also weight balanced, nu = 1/n and lim x = (1/n) 1^T D x(0) D 1.
    Weight-balanced = a sum of weighted directed cycles (in-weight = out-weight)."""
    rng = np.random.default_rng(7)
    n = 6
    base = np.zeros((n, n))
    for c in range(3):  # three weighted cycles through all nodes in random order
        perm, wc = rng.permutation(n), rng.uniform(0.5, 1.5)  # one weight per cycle
        for a, b in zip(perm, np.roll(perm, -1)):
            base[a, b] += wc
    camp = np.array([1, 1, -1, 1, -1, -1])
    A = base * np.outer(camp, camp)
    assert np.allclose(np.abs(A).sum(1), np.abs(A).sum(0))  # weight balanced
    x0 = rng.normal(size=n)
    assert al.simulate(A, x0, T=600.0) == pytest.approx((camp @ x0) / n * camp, abs=1e-6)


@pytest.mark.parametrize("a31,a32", [(1.0, 1.0), (2.0, 0.5), (0.3, 1.7)])
def test_proskurnikov_example1_converges_to_the_equilibrium_line(a31, a32):
    """Claim (L4311, Proskurnikov-Matveev-Cao Example 1; L4310): a12 = a21 = -1, a31, a32 > 0,
    agents 1 and 2 ignoring 3: quasi-strongly connected, unbalanced, NOT strongly connected,
    yet x -> (xi, -xi, rho xi), xi = (x1(0) - x2(0))/2, rho = (a31 - a32)/(|a31| + |a32|):
    neither polarisation (|x_i| equal, signs by camps) nor zero.  Theorem 2's strong
    connectivity hypothesis is what fails."""
    A = al.proskurnikov_example1(a31, a32)
    assert not al.strongly_connected(A) and not al.underlying_balanced(A)
    x0 = np.array([2.0, -0.5, 1.3])
    xi, rho = (x0[0] - x0[1]) / 2, (a31 - a32) / (abs(a31) + abs(a32))
    x = al.simulate(A, x0, T=200.0)
    assert x == pytest.approx([xi, -xi, rho * xi], abs=1e-8)
    assert np.abs(x).max() > 0.5            # not zero
    assert abs(rho) < 1  # stated range of rho
