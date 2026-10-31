"""Altafini 2013; survey 23 section 10 (theorem tagged [standard]).

Parked test (predates the ledger).  Ledger: L2270, L3643, L3644 (`sa`, from 23 s10), now
backed by the full read in docs/prior-work/095: L4304, L4307, L4308.  The fuller
reproduction is tests/test_altafini_095.py; this file is kept because it passes."""
import numpy as np
import pytest
from models import altafini as al

pytestmark = pytest.mark.unverified_source


@pytest.mark.parametrize("seed", range(10))
def test_balanced_gives_bipartite_consensus(seed):
    """Claim (23 s10): connected structurally balanced signed graph =>
    |x_i| converge to a common value, signs opposite across the two camps;
    limit = sigma_i (1/n) sum_j sigma_j x_j(0)."""
    rng = np.random.default_rng(seed)
    n = 8
    A, camp = al.random_signed_graph(n, 0.5, rng, balanced=True)
    assert al.is_balanced(A)
    x0 = rng.normal(size=n) * 3
    x = al.simulate(A, x0)
    expected = camp * (camp @ x0) / n
    assert x == pytest.approx(expected, abs=1e-6)
    assert np.allclose(np.abs(x), np.abs(x[0]), atol=1e-6)


@pytest.mark.parametrize("seed", range(10))
def test_unbalanced_goes_to_zero(seed):
    """Claim (23 s10): connected, not balanced => signed Laplacian is stable
    and all states go to zero."""
    rng = np.random.default_rng(100 + seed)
    n = 8
    while True:
        A, _ = al.random_signed_graph(n, 0.5, rng, balanced=False)
        if not al.is_balanced(A):
            break
    x = al.simulate(A, rng.normal(size=n) * 3, T=500)
    assert np.abs(x).max() < 1e-6
