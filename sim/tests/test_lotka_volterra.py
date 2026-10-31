"""Lotka-Volterra, survey 28 section A1.  Parked test (predates the ledger): no ledger id
(see models/lotka_volterra.py); not an adopted equation."""
import numpy as np
import pytest
from models import lotka_volterra as lv

P = (1.0, 0.5, 0.2, 0.6)  # a, b, d, g


def test_V_conserved_along_orbits():
    """Claim (28 A1): LV gives neutral cycles with a conserved quantity
    V = d x - g ln x + b y - a ln y."""
    for z0 in [(2.0, 1.0), (1.0, 3.0), (5.0, 0.5)]:
        t, (x, y) = lv.trajectory(z0, P, T=200)
        v = lv.V(x, y, *P)
        assert np.max(np.abs(v - v[0])) < 1e-7


def test_orbits_are_closed_cycles():
    """Claim (28 A1): neutral (closed) cycles, not damped. Prey peaks recur
    at constant amplitude."""
    t, (x, y) = lv.trajectory((2.0, 1.0), P, T=300, n=30000)
    peaks = [i for i in range(1, len(x) - 1) if x[i] > x[i - 1] and x[i] > x[i + 1]]
    assert len(peaks) >= 5
    assert x[peaks].max() - x[peaks].min() < 1e-4


def test_conservation_broken_by_saturation():
    """Claim (28 A1, empirical standing): any realistic modification (density
    dependence) breaks the conserved quantity. Add prey self-limitation."""
    from scipy.integrate import solve_ivp
    a, b, d, g = P
    f = lambda t, z: [a * z[0] * (1 - z[0] / 10) - b * z[0] * z[1], d * z[0] * z[1] - g * z[1]]
    s = solve_ivp(f, (0, 200), [2, 1], t_eval=np.linspace(0, 200, 2000), rtol=1e-10, atol=1e-12)
    v = lv.V(s.y[0], s.y[1], *P)
    assert abs(v[-1] - v[0]) > 1e-2
