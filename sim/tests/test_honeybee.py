"""Seeley 2012 / Pais 2013 cross-inhibition model; survey 29 section B1.
Parked test (predates the ledger).  Ledger: L2327, L2328, L2329, L1356, L2331, L3653."""
import numpy as np
import pytest
from models import honeybee as hb


@pytest.mark.parametrize("v", [1.5, 2.0, 3.0, 5.0])
def test_deadlock_threshold_matches_formula(v):
    """Claim (29 B1, Pais Eq. 4): for equal values the symmetric point loses
    stability at sigma* = 4v^3/(v^2-1)^2. Numerically locate the eigenvalue
    crossing and compare."""
    assert hb.numeric_sigma_star(v) == pytest.approx(hb.sigma_star(v), rel=1e-5)


def test_pitchfork_by_simulation():
    """Claim (29 B1 validator): at v=2 (sigma*=3.56) the system stays symmetric
    at 0.9 sigma* and breaks symmetry at 1.1 sigma* (survey: (0.41,0.41) vs
    (0.26,0.49))."""
    v = 2.0
    s = hb.sigma_star(v)
    lo = hb.final_state(v, 0.9 * s)
    hi = hb.final_state(v, 1.1 * s)
    assert abs(lo[0] - lo[1]) < 1e-3
    assert abs(hi[0] - hi[1]) > 0.1
    # NOTE: survey 29 quotes the symmetric split as 0.41; the converged
    # equilibrium is 0.381 (root of the equilibrium condition, and the
    # long-time ODE limit). 0.41 looks like an unconverged Euler transient.
    assert lo[0] == pytest.approx(hb.symmetric_x(v, 0.9 * s), abs=1e-6)
    assert lo[0] == pytest.approx(0.381, abs=0.001)
    assert sorted(hi) == pytest.approx([0.26, 0.49], abs=0.01)


@pytest.mark.parametrize("v", [0.5, 0.8, 1.0])
def test_no_threshold_for_v_leq_1(v):
    """Claim (29 validation log): sigma* exists only for v > 1; for v <= 1
    equal options deadlock however large the stop signal."""
    for sigma in (1, 10, 100, 1000):
        assert hb.antisym_eigenvalue(v, sigma) < 0
    x = hb.final_state(v, 100.0)
    assert abs(x[0] - x[1]) < 1e-3
