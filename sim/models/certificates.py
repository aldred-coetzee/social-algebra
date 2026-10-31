"""Composition laws for the small-gain no-escalation certificate
(models/01-composition-and-levers.md, as revised 2026-10-31 after the audit: models/01 §2.1
split, §3.1 and §3.2 merge, §3.3 uniform cliques (exact), §3.4 one member joins (exact)).

Objects (models/00-v0.md §5; ledger L3996 [read] for small-gain, L4467 [derived] for the
(n-1)g clique row sums).  A group has a gain matrix Gamma = (gamma_ij) >= 0, gamma_ij the gain
from j to i, zero diagonal; the certificate is rho(Gamma) < 1.  Merging G_1 and G_2 gives

    Gamma_m = [[Gamma_1, C_12], [C_21, Gamma_2]]

where C_12 holds the gains members of G_1 receive from members of G_2 and C_21 the reverse.
Rows are receivers, so a row sum is a member's total incoming gain, the quantity models/01 §3.1
bounds.  This module only builds those objects and the quantities the theorems talk about
(spectral radius, the loop matrix P of §3.2, the clique bound of §3.3); the claims themselves
are asserted in tests/test_composition_certificates.py.

Plain numpy.  Spectral radii come from eigenvalues (eigvalsh when the matrix is exactly
symmetric, eigvals otherwise); scipy is used only for brentq in `exact_threshold`.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import brentq


# --------------------------------------------------------------------------- basic objects

def spectral_radius(A: np.ndarray) -> float:
    """rho(A) = max |eigenvalue| (models/01 §1 uses it on non-negative A)."""
    A = np.asarray(A, dtype=float)
    if A.size == 0:
        return 0.0
    if np.array_equal(A, A.T):
        return float(np.abs(np.linalg.eigvalsh(A)).max())
    return float(np.abs(np.linalg.eigvals(A)).max())


def max_row_sum(A: np.ndarray) -> float:
    """||A||_inf for A >= 0: the largest total incoming gain (the F2 bound of models/01 §1)."""
    return float(np.asarray(A, dtype=float).sum(axis=1).max())


def is_nilpotent(G: np.ndarray) -> bool:
    """True iff the support digraph of non-negative G has no cycle, i.e. rho(G) = 0.

    Decided on the 0/1 support (S^n = 0), which is exact: sums of positive terms cannot cancel,
    so no floating-point eigenvalue noise is involved."""
    S = (np.asarray(G) > 0).astype(float)
    return not np.any(np.linalg.matrix_power(S, len(S)))


# --------------------------------------------------------------------------- random generators

def random_gain_matrix(n: int, rng: np.random.Generator, density: float = 1.0,
                       lo: float = 0.1, hi: float = 1.0) -> np.ndarray:
    """Non-negative n x n, zero diagonal; each off-diagonal entry present with probability
    `density`, weight U(lo, hi).  Any cycle has geometric-mean weight >= lo, so a matrix that is
    not nilpotent has rho >= lo (no tiny, noise-dominated radii)."""
    G = rng.uniform(lo, hi, (n, n)) * (rng.random((n, n)) < density)
    np.fill_diagonal(G, 0.0)
    return G


def random_certified(n: int, rng: np.random.Generator, density: float = 1.0,
                     rho_lo: float = 0.05, rho_hi: float = 0.99,
                     allow_nilpotent: bool = True) -> np.ndarray:
    """Random zero-diagonal G >= 0 scaled so rho(G) = U(rho_lo, rho_hi) < 1.

    A support with no cycle has rho = 0 and nothing to scale: it is returned as drawn (it is
    certified, rho = 0 < 1) when `allow_nilpotent`, otherwise redrawn."""
    if n < 2 and not allow_nilpotent:
        raise ValueError("a 1-member group is always nilpotent")
    while True:
        G = random_gain_matrix(n, rng, density)
        if is_nilpotent(G):
            if allow_nilpotent:
                return G
            continue
        return G * (rng.uniform(rho_lo, rho_hi) / spectral_radius(G))


def random_cross(n_rows: int, n_cols: int, rng: np.random.Generator, density: float = 1.0,
                 lo: float = 0.1, hi: float = 1.0) -> np.ndarray:
    """Random non-negative cross-gain block with at least one positive entry."""
    while True:
        C = rng.uniform(lo, hi, (n_rows, n_cols)) * (rng.random((n_rows, n_cols)) < density)
        if C.any():
            return C


def random_two_groups(rng: np.random.Generator, max_size: int = 8):
    """(G1, C12, C21, G2) at unit scale: two certified groups of 1..max_size members (random
    density; rho in (0.05, 0.99), or no cycle at all) and non-empty random cross blocks of random
    density.  Both groups satisfy the hypotheses of models/01 §3.2 by construction."""
    n1, n2 = (int(x) for x in rng.integers(1, max_size + 1, 2))
    G1 = random_certified(n1, rng, density=rng.uniform(0.3, 1.0))
    G2 = random_certified(n2, rng, density=rng.uniform(0.3, 1.0))
    C12 = random_cross(n1, n2, rng, density=rng.uniform(0.3, 1.0))
    C21 = random_cross(n2, n1, rng, density=rng.uniform(0.3, 1.0))
    return G1, C12, C21, G2


def random_partition(n: int, k: int, rng: np.random.Generator) -> list[np.ndarray]:
    """Random partition of range(n) into k non-empty index blocks (not contiguous)."""
    perm = rng.permutation(n)
    labels = np.empty(n, dtype=int)
    labels[perm[:k]] = np.arange(k)
    labels[perm[k:]] = rng.integers(0, k, n - k)
    return [np.flatnonzero(labels == b) for b in range(k)]


def scale_rows_to_sums(M: np.ndarray, sums: np.ndarray) -> np.ndarray:
    """Rescale each row of a non-negative matrix so row i sums to sums[i] (zero rows stay zero)."""
    s = M.sum(axis=1)
    f = np.divide(sums, s, out=np.zeros_like(s), where=s > 0)
    return M * f[:, None]


# --------------------------------------------------------------------------- split (models/01 §2.1)

def restrict(G: np.ndarray, idx: np.ndarray) -> np.ndarray:
    """Gamma_B: Gamma restricted to B x B (a fragment keeps only its internal gains)."""
    return G[np.ix_(idx, idx)]


def pad(G: np.ndarray, idx: np.ndarray) -> np.ndarray:
    """Gamma'_B of the proof of Theorem 2.1: Gamma_B padded with zeros to the size of Gamma."""
    out = np.zeros_like(G)
    out[np.ix_(idx, idx)] = G[np.ix_(idx, idx)]
    return out


# --------------------------------------------------------------------------- merge (models/01 §3.1, §3.2)

def merged(G1: np.ndarray, C12: np.ndarray, C21: np.ndarray, G2: np.ndarray) -> np.ndarray:
    """Gamma_m = [[G1, C12], [C21, G2]] (inputs are coerced to arrays: np.block reads nested lists
    as layout, so a bare [[c]] would be taken for a block grid)."""
    G1, C12, C21, G2 = (np.asarray(X, dtype=float) for X in (G1, C12, C21, G2))
    return np.block([[G1, C12], [C21, G2]])


def loop_matrix(G1: np.ndarray, C12: np.ndarray, G2: np.ndarray, C21: np.ndarray) -> np.ndarray:
    """P = (I - G1)^-1 C12 (I - G2)^-1 C21 of models/01 §3.2 (n1 x n1).

    Built as X @ Y with X = (I - G1)^-1 C12 and Y = (I - G2)^-1 C21 by linear solves."""
    X = np.linalg.solve(np.eye(len(G1)) - G1, C12)
    Y = np.linalg.solve(np.eye(len(G2)) - G2, C21)
    return X @ Y


def loop_gain(G1: np.ndarray, C12: np.ndarray, G2: np.ndarray, C21: np.ndarray) -> float:
    """rho(P): the gain of the loop G1 -> G2 -> G1 (models/01 §3.2)."""
    return spectral_radius(loop_matrix(G1, C12, G2, C21))


def schur_complement(G1: np.ndarray, C12: np.ndarray, G2: np.ndarray, C21: np.ndarray) -> np.ndarray:
    """S = (I - G2) - C21 (I - G1)^-1 C12, the Schur complement of I - Gamma_m w.r.t. I - G1."""
    return (np.eye(len(G2)) - G2) - C21 @ np.linalg.solve(np.eye(len(G1)) - G1, C12)


def two_pair_counterexample(a: float = 0.1, c: float = 0.8):
    """Two 2-member groups with weak internal gain a and strong reciprocal cross gain c on every
    cross pair (models/01 §3.1 failure case).  Returns (G1, C12, C21, G2).

    Every row of Gamma_m sums to a + 2c, so the all-ones vector is its Perron vector and
    rho(Gamma_m) = a + 2c.  Since (I - G) J = J/(1 - a) for J = ones(2, 2), P = (c/(1-a))^2 J J
    = 2 (c/(1-a))^2 J, so rho(P) = 4 c^2 / (1-a)^2; both cross 1 together at c = (1-a)/2."""
    G = np.array([[0.0, a], [a, 0.0]])
    C = np.full((2, 2), c)
    return G, C, C.copy(), G.copy()


# --------------------------------------------------------------------------- uniform cliques (models/01 §3.3)

def clique(n: int, g: float) -> np.ndarray:
    """Complete graph on n members, uniform internal gain g, zero diagonal."""
    return g * (np.ones((n, n)) - np.eye(n))


def clique_radius(n: int, g: float) -> float:
    """rho_i = (n_i - 1) g_i (ledger L4467): Gamma_i 1 = rho_i 1."""
    return (n - 1) * g


def uniform_merge(n1: int, g1: float, n2: int, g2: float, c: float) -> np.ndarray:
    """Gamma_m for two uniform cliques with every cross tie of gain c."""
    return merged(clique(n1, g1), np.full((n1, n2), c), np.full((n2, n1), c), clique(n2, g2))


def quotient(n1: int, g1: float, n2: int, g2: float, c: float) -> np.ndarray:
    """The 2 x 2 quotient [[rho_1, n_2 c], [n_1 c, rho_2]] of the equitable two-cell partition
    (models/01 §3.3): its spectral radius is rho(Gamma_m)."""
    return np.array([[clique_radius(n1, g1), n2 * c], [n1 * c, clique_radius(n2, g2)]])


def row_sum_limits(n1: int, g1: float, n2: int, g2: float) -> tuple[float, float]:
    """(b_1, b_2) = ((1 - rho_1)/n_2, (1 - rho_2)/n_1): the two terms of the row-sum bound
    c < min(b_1, b_2) that Theorem 3.1 gives for uniform cliques (models/01 §3.3 Remark)."""
    return (1 - clique_radius(n1, g1)) / n2, (1 - clique_radius(n2, g2)) / n1


def row_sum_bound(n1: int, g1: float, n2: int, g2: float) -> float:
    """min(b_1, b_2): every c below it makes all rows of Gamma_m sum to less than one."""
    return min(row_sum_limits(n1, g1, n2, g2))


def exact_threshold_closed_form(n1: int, g1: float, n2: int, g2: float) -> float:
    """c* = sqrt((1 - rho_1)(1 - rho_2)/(n_1 n_2)) = sqrt(b_1 b_2), the geometric mean of the
    two row-sum limits: Corollary 3.3 certifies the merge iff c < c* (models/01 §3.3)."""
    b1, b2 = row_sum_limits(n1, g1, n2, g2)
    return float(np.sqrt(b1 * b2))


def exact_threshold(n1: int, g1: float, n2: int, g2: float) -> float:
    """Largest c with rho(Gamma_m(c)) < 1, by root-finding on the FULL merged matrix.

    rho(Gamma_m(c)) is non-decreasing in c (F1), so its first crossing of 1 is the supremum of
    certified c.  No formula for the answer is used: the bracket starts at the row-sum bound
    (where rho <= 1) and is doubled until it is crossed."""
    def f(c: float) -> float:
        return spectral_radius(uniform_merge(n1, g1, n2, g2, c)) - 1.0

    hi = row_sum_bound(n1, g1, n2, g2)
    while f(hi) < 0:
        hi *= 2
    return float(brentq(f, 0.0, hi, xtol=1e-14, rtol=1e-12))


# --------------------------------------------------------------------------- one member joins (models/01 §3.4)

def join_one(G: np.ndarray, c_in: np.ndarray, c_out: np.ndarray) -> np.ndarray:
    """Gamma_m when one person p (the last index) joins G.  c_in[j] is the gain from member j to p
    (p's incoming, row p); c_out[j] is the gain from p to member j (column p).  gamma_pp = 0."""
    n = len(G)
    M = np.zeros((n + 1, n + 1))
    M[:n, :n] = G
    M[n, :n] = c_in
    M[:n, n] = c_out
    return M


def join_loop_gain(G: np.ndarray, c_in: np.ndarray, c_out: np.ndarray) -> float:
    """c_{p.} (I - G)^-1 c_{.p}, the scalar of Corollary 3.4: the enlarged group is certified iff
    it is below one.  It is rho(P) of §3.2 for G_2 = {p}, where P = (I - G)^-1 c_out c_in^T is
    rank one: the walk-sum p -> members -> through G -> back to p."""
    return float(c_in @ np.linalg.solve(np.eye(len(G)) - G, c_out))
