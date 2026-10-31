"""v0.1 generic update (3.0): x_i(t+1) = x_i + D1 + D2 + D3 (models/00-v0.md section 3).

D1 set point with two-regime inertia (3.1; L0853, L2096, L4368)
D2 gated affiliation, O-jive form: zero inside [K-, K+], bounded constants beyond (L0857)
D3 linear goal attraction omega_i (g_i - x_i) (3.3; L3864, linear case)
"""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Params:
    p: np.ndarray       # set points
    r_minus: np.ndarray  # inertia below the set point
    r_plus: np.ndarray   # inertia above the set point
    K_minus: np.ndarray  # lower gate edge (< 0)
    K_plus: np.ndarray   # upper gate edge (> 0)
    c_plus: float        # bounded response above K+
    c_minus: float       # bounded response below K- (negative)
    omega: np.ndarray    # goal strengths (0 = D3 absent)
    g: np.ndarray        # goals


def random_params(n: int, rng: np.random.Generator, gate: float = 5.0, with_d3: bool = False) -> Params:
    return Params(
        p=rng.uniform(-1, 1, n),
        r_minus=rng.uniform(0.5, 0.7, n), r_plus=rng.uniform(0.2, 0.4, n),
        K_minus=np.full(n, -gate), K_plus=np.full(n, gate),
        c_plus=0.3, c_minus=-0.3,
        omega=rng.uniform(0.05, 0.2, n) if with_d3 else np.zeros(n),
        g=rng.uniform(-1, 1, n))


def step(x: np.ndarray, P: Params) -> np.ndarray:
    n = len(x)
    r = np.where(x < P.p, P.r_minus, P.r_plus)
    d1 = -(1 - r) * (x - P.p)
    d2 = np.zeros(n)
    for i in range(n):
        xj = np.delete(x, i)
        d2[i] = P.c_plus * (xj > P.K_plus[i]).sum() + P.c_minus * (xj < P.K_minus[i]).sum()
    d3 = P.omega * (P.g - x)
    return x + d1 + d2 + d3


def run(x0: np.ndarray, P: Params, T: int) -> np.ndarray:
    traj = [x0.copy()]
    for _ in range(T):
        traj.append(step(traj[-1], P))
    return np.array(traj)
