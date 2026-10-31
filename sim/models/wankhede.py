"""Wankhede et al. opinion dynamics with stubbornness, signed influence and a
cubic resource penalty (docs/prior-work/090 section 4a; ledger L3993, L4004).

    dz_i/dt = -w_i (z_i - p_i) + sum_k a_ik (z_k - z_i) - z_i^3 / r_i

a_ik > 0 friend, a_ik < 0 enemy.  Linear law (no cubic term) is used for the
Euler-turn version of v0.1 Theorem 6.1.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def split_weights(A: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return (F, E): friends' total weight and enemies' total |weight| per row."""
    off = A - np.diag(np.diag(A))
    return np.where(off > 0, off, 0.0).sum(1), np.where(off < 0, -off, 0.0).sum(1)


def rhs(z: np.ndarray, A: np.ndarray, w: np.ndarray, p: np.ndarray, r: np.ndarray | None) -> np.ndarray:
    """Right-hand side; r=None drops the cubic term (the linear law)."""
    off = A - np.diag(np.diag(A))
    coupling = off @ z - off.sum(1) * z
    out = -w * (z - p) + coupling
    if r is not None:
        out = out - z**3 / r
    return out


def jacobian(z: np.ndarray, A: np.ndarray, w: np.ndarray, r: np.ndarray | None) -> np.ndarray:
    """J_ii = -w_i - sum_k a_ik - 3 z_i^2 / r_i; J_ik = a_ik."""
    off = A - np.diag(np.diag(A))
    J = off.copy()
    cub = 0.0 if r is None else 3 * z**2 / r
    J[np.diag_indices_from(J)] = -w - off.sum(1) - cub
    return J


def log_norm_inf(J: np.ndarray) -> float:
    """mu_inf(J) = max_i [J_ii + sum_{k != i} |J_ik|]."""
    off = np.abs(J - np.diag(np.diag(J))).sum(1)
    return float((np.diag(J) + off).max())


def integrate(z0: np.ndarray, A, w, p, r, T: float = 200.0) -> np.ndarray:
    sol = solve_ivp(lambda t, z: rhs(z, A, w, p, r), (0, T), z0, rtol=1e-10, atol=1e-12, method="LSODA")
    return sol.y[:, -1]


def euler_matrix(A: np.ndarray, w: np.ndarray, h: float) -> np.ndarray:
    """Linear part M = I + hJ of the Euler map x -> x + h f(x) for the linear law."""
    return np.eye(len(w)) + h * jacobian(np.zeros(len(w)), A, w, None)


def random_signed(n: int, rng: np.random.Generator, p_enemy: float = 0.4) -> np.ndarray:
    """Dense directed signed weight matrix, zero diagonal; weights in [0.2, 1.2]."""
    mag = rng.uniform(0.2, 1.2, (n, n))
    sign = np.where(rng.random((n, n)) < p_enemy, -1.0, 1.0)
    A = mag * sign
    np.fill_diagonal(A, 0.0)
    return A
