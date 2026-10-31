"""Allesina & Tang 2012; survey 30 section A3.  Parked test (predates the ledger): no ledger id
(see models/allesina_tang.py); not an adopted equation."""
import numpy as np
import pytest
from models import allesina_tang as at

S, C, SIGMA = 600, 0.2, 0.5


@pytest.mark.parametrize("kind", ["random", "predator_prey", "mixed"])
def test_ellipse_semi_axes(kind):
    """Claim (30 A3): bulk eigenvalues fill an ellipse with horizontal
    semi-axis sigma sqrt(SC)(1+tau) and vertical sigma sqrt(SC)(1-tau);
    tau = 0, -2/pi, +2/pi for random, predator-prey, mixed."""
    rng = np.random.default_rng(1)
    h, v = at.bulk_extent(at.community(S, C, SIGMA, kind, rng))
    ph, pv = at.predicted_radii(S, C, SIGMA, kind)
    assert h == pytest.approx(ph, rel=0.08)
    assert v == pytest.approx(pv, rel=0.08)


def test_predator_prey_is_more_stable_than_random():
    """Claim (30 A3): predator-prey needs sigma sqrt(SC)(1-2/pi) < d, so a
    system of the same sigma*sqrt(SC) that is unstable when random can be
    stable when predator-prey (K up to pi/(pi-2) ~ 2.75 d), while mixed
    (K < pi/(pi+2) ~ 0.61 d) is less stable."""
    rng = np.random.default_rng(2)
    d = 1.0
    K = 1.5 * d  # sigma sqrt(SC) = 1.5
    sig = K / np.sqrt(S * C)
    stable = {}
    for kind in ["random", "predator_prey", "mixed"]:
        B = at.community(S, C, sig, kind, rng)
        stable[kind] = (np.linalg.eigvals(B).real.max() - d) < 0
    assert stable == {"random": False, "predator_prey": True, "mixed": False}
    # mixed unstable already at K=0.8 d, random/pp stable there
    sig = 0.8 / np.sqrt(S * C)
    assert np.linalg.eigvals(at.community(S, C, sig, "mixed", rng)).real.max() > 0.8 * 0 + 1.0 * 0.8 * (1 + 2 / np.pi) * 0.9
    assert np.linalg.eigvals(at.community(S, C, sig, "random", rng)).real.max() < 1.0


def test_thresholds_constants():
    """Claim (30 A3): K < pi/(pi-2) ~ 2.75 and K < pi/(pi+2) ~ 0.61."""
    assert np.pi / (np.pi - 2) == pytest.approx(2.752, abs=1e-3)
    assert np.pi / (np.pi + 2) == pytest.approx(0.611, abs=1e-3)
    # sharp transition at the predicted K for predator-prey
    rng = np.random.default_rng(3)
    for K, expect_stable in [(2.5, True), (3.0, False)]:
        sig = K / np.sqrt(S * C)
        B = at.community(S, C, sig, "predator_prey", rng)
        assert (np.linalg.eigvals(B).real.max() < 1.0) == expect_stable
