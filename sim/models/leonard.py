"""Leonard et al. 2012 (PNAS 109, 227-232) compromise-or-choose model
(docs/prior-work/086 section 1; ledger L3871-L3874).

Mean headings Psi_k of informed subgroups 1, 2 and uninformed 3 on a coupling
manifold A = (A12, A13, A23) in {0,1}^3 (slow dynamics, Eq. 6); coupling weights
a_jl = 1/(1+exp(-eta)), d eta/dt = K2 (rho - r), rho = |cos((Psi_j - Psi_l)/2)|.
A manifold's pair (j,l) with A_jl = 0 stays uncoupled iff rho_jl < r there; with
A_jl = 1 stays coupled iff rho_jl > r.  That is the transverse stability test.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp

PAIRS = ((0, 1), (0, 2), (1, 2))  # 12, 13, 23


def theta_c(r: float) -> float:
    return 2 * np.arccos(r)


def slow_rhs(psi: np.ndarray, A: dict[tuple[int, int], float], th: tuple[float, float], N: tuple[int, int, int],
             K1: float) -> np.ndarray:
    n = sum(N)
    pref = (th[0], th[1], None)
    out = np.zeros(3)
    for k in range(3):
        d = np.sin(pref[k] - psi[k]) if pref[k] is not None else 0.0
        s = 0.0
        for j in range(3):
            if j != k:
                a = A[(min(j, k), max(j, k))]
                s += a * N[j] * np.sin(psi[j] - psi[k])
        out[k] = d + (K1 / n) * s
    return out


def slow_equilibrium(manifold: tuple[int, int, int], th2: float, N=(5, 5, 11), K1: float = 2.0,
                     psi0: np.ndarray | None = None, T: float = 400.0) -> np.ndarray:
    """Equilibrium of Eq. 6 on the given manifold (A12, A13, A23), th1 = 0, th2 = th2."""
    A = dict(zip(PAIRS, map(float, manifold)))
    th = (0.0, th2)
    y0 = np.array([0.1, th2 - 0.1, th2 / 2]) if psi0 is None else psi0
    sol = solve_ivp(lambda t, y: slow_rhs(y, A, th, N, K1), (0, T), y0, rtol=1e-11, atol=1e-13, method="LSODA")
    return sol.y[:, -1]


def rho(psi: np.ndarray) -> dict[tuple[int, int], float]:
    return {(j, l): abs(np.cos((psi[j] - psi[l]) / 2)) for j, l in PAIRS}


def eta_rates(manifold: tuple[int, int, int], th2: float, r: float, K2: float = 1.0, **kw) -> dict[tuple[int, int], float]:
    """d eta/dt = K2 (rho - r) at the manifold's slow equilibrium; for a decision/compromise
    to be stable, uncoupled pairs need a negative rate and coupled pairs a positive one."""
    psi = slow_equilibrium(manifold, th2, **kw)
    return {pr: K2 * (v - r) for pr, v in rho(psi).items()}


def manifold_is_stable(manifold: tuple[int, int, int], th2: float, r: float, **kw) -> bool:
    rates = eta_rates(manifold, th2, r, **kw)
    return all((rates[pr] > 0) if m else (rates[pr] < 0) for pr, m in zip(PAIRS, manifold))


def full_rhs(y: np.ndarray, th2: float, r: float, N, K1: float, K2: float) -> np.ndarray:
    psi, eta = y[:3], y[3:]
    a = 1 / (1 + np.exp(-eta))
    A = dict(zip(PAIRS, a))
    d_eta = np.array([K2 * (abs(np.cos((psi[j] - psi[l]) / 2)) - r) for j, l in PAIRS])
    return np.concatenate([slow_rhs(psi, A, (0.0, th2), N, K1), d_eta])


def simulate_full(th2: float, r: float, y0: np.ndarray, N=(5, 5, 11), K1=2.0, K2=2.0, T=300.0) -> np.ndarray:
    sol = solve_ivp(lambda t, y: full_rhs(y, th2, r, N, K1, K2), (0, T), y0, rtol=1e-9, atol=1e-11, method="LSODA")
    return sol.y[:, -1]
