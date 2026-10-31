"""Marvel, Kleinberg, Kleinberg & Strogatz structural-balance dynamics
dX/dt = X^2 (docs/prior-work/060 section 5 and 083 section 2.3; ledger L0898,
L3154, L3826).  X symmetric.  Closed form X(t) = X0 (I - t X0)^-1.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


def random_symmetric(n: int, rng: np.random.Generator, mean: float = 0.0) -> np.ndarray:
    G = rng.normal(mean, 1.0, (n, n))
    return (G + G.T) / 2


def closed_form(X0: np.ndarray, t: float) -> np.ndarray:
    n = len(X0)
    return X0 @ np.linalg.inv(np.eye(n) - t * X0)


def integrate(X0: np.ndarray, t_end: float) -> np.ndarray:
    n = len(X0)
    sol = solve_ivp(lambda t, y: (y.reshape(n, n) @ y.reshape(n, n)).ravel(), (0, t_end), X0.ravel(),
                    rtol=1e-12, atol=1e-14, method="DOP853")
    return sol.y[:, -1].reshape(n, n)


def leading(X0: np.ndarray) -> tuple[float, float, np.ndarray]:
    """(lambda_1, lambda_2, omega_1) with ascending eigh reordered."""
    lam, Q = np.linalg.eigh(X0)
    return float(lam[-1]), float(lam[-2]), Q[:, -1]
