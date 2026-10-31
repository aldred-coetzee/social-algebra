"""Allesina & Tang 2012 stability criteria for random community matrices.

Parked file (predates the ledger).  Ledger ids: none cover the ellipse law itself;
the only ledger lines on May's criterion are L1399 and L1417 (both `sa`, in file 070's
cross-check), so this module has no adopted-equation id and v0.1 does not use it.
Source: docs/prior-work/30-ecological-stability-resilience.md, section A3
(Nature 483, 205-208, DOI 10.1038/nature10832), tagged [read: arXiv
1105.2071v1 full text] in the validation log; A2 (May 1972) is tagged
[from standard account] but is checked in A2's own "Check of the statement".

M = -d I + B. Each pair (B_ij, B_ji) is nonzero with prob C; magnitudes
half-normal |N(0, sigma^2)|. tau = E[B_ij B_ji]/sigma^2. Bulk eigenvalues
fill an ellipse centred at -d with horizontal semi-axis
sigma sqrt(SC) (1 + tau) and vertical sigma sqrt(SC) (1 - tau).
random: tau=0; predator-prey: tau=-2/pi; competition/mutualism mix: +2/pi.
"""
import numpy as np


def community(S, C, sigma, kind, rng):
    """Pairs (i<j) are linked with prob C; each direction gets an independent
    half-normal magnitude (so E|X| = sigma sqrt(2/pi)); signs set by `kind`."""
    link = np.triu(rng.random((S, S)) < C, 1)
    m_ij = np.abs(rng.normal(0, sigma, (S, S)))
    m_ji = np.abs(rng.normal(0, sigma, (S, S)))
    s = rng.choice([-1, 1], (S, S))
    t = rng.choice([-1, 1], (S, S))
    if kind == "random":  # independent signs, E[B_ij B_ji] = 0
        a, b = s, t
    elif kind == "predator_prey":  # opposite signs, which is + chosen at random
        a, b = s, -s
    elif kind == "mixed":  # same sign, sign random
        a, b = s, s
    else:
        raise ValueError(kind)
    return np.where(link, m_ij * a, 0.0) + np.where(link, m_ji * b, 0.0).T


def tau(kind):
    return {"random": 0.0, "predator_prey": -2 / np.pi, "mixed": 2 / np.pi}[kind]


def predicted_radii(S, C, sigma, kind):
    R = sigma * np.sqrt(S * C)
    return R * (1 + tau(kind)), R * (1 - tau(kind))


def bulk_extent(B):
    ev = np.linalg.eigvals(B)
    return ev.real.max(), ev.imag.max()
