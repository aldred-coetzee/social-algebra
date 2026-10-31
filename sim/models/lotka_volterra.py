"""Lotka-Volterra predator-prey with its conserved quantity.

Parked file (predates the ledger).  Ledger ids: none; the survey's A1 lines were never
extracted as equations (the only LV lines are L1773, a data fit, and L2581, a note).
Not used by v0.1.
Source: docs/prior-work/28-predator-prey-ecology-of-fear.md, section A1
(Lotka 1925; Volterra 1926, DOI 10.1038/118558a0). The equations are the
standard form quoted in A1:  dx/dt = a x - b x y,  dy/dt = d x y - g y.
The conserved quantity V = d x - g ln x + b y - a ln y is the textbook
first integral (A1 states a conserved quantity exists; the survey file does
not print V, so V is derived here by dV/dt = 0, which the test checks).
"""
import numpy as np
from scipy.integrate import solve_ivp


def rhs(t, z, a, b, d, g):
    x, y = z
    return [a * x - b * x * y, d * x * y - g * y]


def V(x, y, a, b, d, g):
    return d * x - g * np.log(x) + b * y - a * np.log(y)


def trajectory(z0, params, T=100.0, n=2000):
    t = np.linspace(0, T, n)
    sol = solve_ivp(rhs, (0, T), z0, args=params, t_eval=t, rtol=1e-11, atol=1e-13, method="DOP853")
    return sol.t, sol.y
