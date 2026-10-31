"""Granovetter 1978 threshold model r(t+1) = F[r(t)] and v0.1's two-sided gate
(docs/prior-work/066 section 1; ledger L1225, L1831, L3959-L3961, L1201, L1235).

Integer thresholds are in people (out of n), so every comparison is exact:
person i joins iff theta_i <= count <= theta_bar_i.
"""
from __future__ import annotations

import numpy as np


def F_count(count: int, theta: np.ndarray, theta_bar: np.ndarray | None = None) -> int:
    """Number joined when `count` have joined (two-sided gate if theta_bar given)."""
    on = theta <= count
    if theta_bar is not None:
        on &= count <= theta_bar
    return int(on.sum())


def iterate(theta: np.ndarray, theta_bar: np.ndarray | None = None, start: int | None = None,
            max_steps: int = 10_000) -> list[int]:
    """Orbit of count -> F(count) until a fixed point or a repeat; start defaults to
    the number of zero-threshold members (Granovetter's instigators)."""
    c = int((theta == 0).sum()) if start is None else start
    orbit = [c]
    seen = {c}
    for _ in range(max_steps):
        c = F_count(c, theta, theta_bar)
        orbit.append(c)
        if orbit[-1] == orbit[-2] or c in seen:
            break
        seen.add(c)
    return orbit


def least_fixed_point(theta: np.ndarray) -> int:
    """Smallest count c with F(c) = c, by brute force over 0..n."""
    for c in range(len(theta) + 1):
        if F_count(c, theta) == c:
            return c
    raise AssertionError("monotone F on {0..n} must have a fixed point")
