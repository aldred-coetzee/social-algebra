"""Marvel, Kleinberg, Kleinberg & Strogatz 2011, PNAS 108(5), 1771-1776,
DOI 10.1073/pnas.1013213108: dX/dt = X^2 on symmetric X.

Prior-work files: docs/prior-work/060 section 5 and 083 section 2.3.
Ledger: L0898 (the equation), L3154 (blow-up time and sign pattern under three
conditions), L3826 (Zachary fit; a fit, not reproduced here).  v0.1 (4.2a).
"""
import numpy as np
import pytest
from models import marvel as mv

N = 8


def _x0(seed: int, mean: float = 0.3) -> np.ndarray:
    return mv.random_symmetric(N, np.random.default_rng(seed), mean)


@pytest.mark.parametrize("seed", range(6))
def test_closed_form_solves_the_ode(seed):
    """Claim (L0898, 083 eq 4): X(t) = X0 (I - t X0)^-1 solves dX/dt = X^2.
    Numerical integration to 90% of t* matches it."""
    X0 = _x0(seed)
    lam1, _, _ = mv.leading(X0)
    assert lam1 > 0
    t = 0.9 / lam1
    assert mv.integrate(X0, t) == pytest.approx(mv.closed_form(X0, t), rel=1e-6, abs=1e-8)


@pytest.mark.parametrize("seed", range(6))
def test_blowup_time_is_inverse_leading_eigenvalue(seed):
    """Claim (L3154): for lambda_1 > 0 the solution blows up at t* = 1/lambda_1.
    ||X(t)||_F ~ lambda_1 / (1 - t lambda_1): finite just before t*, scaling as the
    pole predicts as t -> t*, and the matrix I - tX0 is singular exactly at t*."""
    X0 = _x0(seed)
    lam1, _, _ = mv.leading(X0)
    tstar = 1 / lam1
    assert np.linalg.eigvalsh(np.eye(N) - tstar * X0).min() == pytest.approx(0.0, abs=1e-10)
    n1, n2 = (np.linalg.norm(mv.closed_form(X0, tstar * (1 - e)), "fro") for e in (1e-4, 1e-5))
    assert n2 / n1 == pytest.approx(10.0, rel=1e-2)  # pole of order one at t*
    assert np.linalg.norm(mv.closed_form(X0, 0.999 * tstar), "fro") > 100  # diverging
    assert np.isfinite(mv.integrate(X0, tstar * 0.999)).all()


@pytest.mark.parametrize("seed", range(6))
def test_rank_one_limit_and_sign_pattern_is_two_factions(seed):
    """Claim (L3154, Marvel Eq. 5): if lambda_1 > 0, lambda_1 != lambda_2 and every
    component of omega_1 is nonzero, X/||X|| -> omega_1 omega_1^T and sgn x_kl = sgn(w_k w_l):
    factions S = {w_k > 0}, T = {w_k < 0}, friendly inside and unfriendly across."""
    X0 = _x0(seed)
    lam1, lam2, w1 = mv.leading(X0)
    assert lam1 > lam2 and np.all(np.abs(w1) > 1e-9)
    X = mv.integrate(X0, (1 - 1e-4) / lam1)
    Xn = X / np.linalg.norm(X, "fro")
    assert Xn == pytest.approx(np.outer(w1, w1), abs=2e-3)  # rank-one approach
    assert np.linalg.matrix_rank(Xn, tol=1e-2) == 1
    assert np.array_equal(np.sign(X), np.sign(np.outer(w1, w1)))
    # balance: every triangle has an odd number of positive edges (product of signs > 0)
    s = np.sign(X)
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                assert s[i, j] * s[j, k] * s[i, k] > 0


def test_no_blowup_when_leading_eigenvalue_not_positive():
    """Claim (L3154 first condition): lambda_1 <= 0 gives no finite-time blow-up; with X0
    negative definite, X(t) = X0 (I - tX0)^-1 stays bounded for all t > 0 and tends to 0."""
    X0 = -(lambda G: G @ G.T + np.eye(N))(np.random.default_rng(0).normal(size=(N, N)) * 0.3)
    assert mv.leading(X0)[0] < 0
    norms = [np.linalg.norm(mv.closed_form(X0, t)) for t in (1, 10, 1e3, 1e6)]
    assert max(norms) <= np.linalg.norm(X0) + 1e-12 and norms[-1] < 1e-2


def test_zero_component_leaves_pattern_unsigned():
    """Claim (L3154 third condition): if omega_1 has a zero component the pattern is not
    determined.  X0 = block [[1, .5],[.5, 1]] + [0.2]: omega_1 = (1,1,0)/sqrt2, and the
    third member's ties to the others stay exactly 0 through the blow-up."""
    X0 = np.zeros((3, 3)); X0[:2, :2] = [[1, .5], [.5, 1]]; X0[2, 2] = 0.2
    lam1, _, w1 = mv.leading(X0)
    assert abs(w1[2]) < 1e-12
    X = mv.closed_form(X0, 0.999 / lam1)
    assert X[0, 2] == 0 and X[1, 2] == 0
