"""Honeybee nest-site selection with cross-inhibition.

Parked file (predates the ledger).  Ledger ids: L2327 (Pais Eq. 1), L2328 (Pais
parameterisation gamma = rho = v, alpha = 1/v), L2329 and L1356 (sigma* = 4 v^3 /
(v^2-1)^2), L2331 (antisymmetric eigenvalue, [derived]), L3653 (sigma* exists only for
v > 1, [derived]); all `read`/`derived`.  Not used by v0.1 (cross-inhibition is not a
v0.1 term).
Source: docs/prior-work/29-animal-collective-behaviour.md, section B1
(Seeley et al. 2012; Pais et al. 2013). Tagged [read: full text] and
[derived] in the file's validation log; equations are NOT from abstract only.

    dxA/dt = gA*U - aA*xA + rA*xA*U - sB*xA*xB
    dxB/dt = gB*U - aB*xB + rB*xB*U - sA*xA*xB,   U = 1 - xA - xB
    gamma_i = rho_i = v_i, alpha_i = 1/v_i, sigma value-independent.
Equal values: pitchfork at sigma* = 4 v^3 / (v^2 - 1)^2, only for v > 1.
"""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def rhs(t, x, vA, vB, sigma):
    xA, xB = x
    U = 1.0 - xA - xB
    return [
        vA * U - xA / vA + vA * xA * U - sigma * xA * xB,
        vB * U - xB / vB + vB * xB * U - sigma * xA * xB,
    ]


def sigma_star(v):
    return 4 * v**3 / (v**2 - 1) ** 2


def symmetric_x(v, sigma):
    """Symmetric equilibrium x_A = x_B = x: solve v*U - x/v + v*x*U - sigma*x^2 = 0."""
    f = lambda x: v * (1 - 2 * x) - x / v + v * x * (1 - 2 * x) - sigma * x**2
    return brentq(f, 0.0, 0.5)


def jacobian(x, v, sigma, h=1e-6):
    J = np.zeros((2, 2))
    for j in range(2):
        d = np.zeros(2)
        d[j] = h
        J[:, j] = (np.array(rhs(0, x + d, v, v, sigma)) - np.array(rhs(0, x - d, v, v, sigma))) / (2 * h)
    return J


def antisym_eigenvalue(v, sigma):
    """Eigenvalue of the Jacobian at the symmetric point for (1,-1) perturbations."""
    x = symmetric_x(v, sigma)
    J = jacobian(np.array([x, x]), v, sigma)
    return (J @ np.array([1.0, -1.0]))[0]


def numeric_sigma_star(v, lo=1e-3, hi=1e3):
    """Locate where the symmetric point loses stability (eigenvalue crosses 0)."""
    return brentq(lambda s: antisym_eigenvalue(v, s), lo, hi, xtol=1e-10)


def final_state(v, sigma, x0=(0.3, 0.1), T=3000.0):
    sol = solve_ivp(rhs, (0, T), x0, args=(v, v, sigma), rtol=1e-10, atol=1e-12, method="LSODA")
    return sol.y[:, -1]
