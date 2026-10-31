"""Altafini 2013 consensus on signed networks.

Parked file (predates the ledger), now cited to ledger ids: written from
docs/prior-work/23 section 10 (ledger L2256, L2270, L3643, L3644, all `sa`),
and since superseded by the full read in docs/prior-work/095 (ledger L4304,
L4307, L4308 `read`).  Altafini 2013, IEEE TAC 58(4), DOI
10.1109/TAC.2012.2224251.  The digraph / Proskurnikov functions added below
serve tests/test_altafini_095.py.

    dx_i/dt = sum_j |a_ij| (sgn(a_ij) x_j - x_i),  i.e. dx/dt = -L_s x,
    L_s = diag(sum_j |a_ij|) - A.
Connected undirected graph: bipartite consensus iff structurally balanced
(camps friendly within, hostile between), otherwise x -> 0.
"""
import numpy as np
from scipy.linalg import expm


def signed_laplacian(A):
    return np.diag(np.abs(A).sum(1)) - A


def simulate(A, x0, T=200.0):
    return expm(-signed_laplacian(A) * T) @ x0


def is_balanced(A):
    """2-colour by BFS using edge signs; balanced iff no contradiction."""
    n = len(A)
    col = np.zeros(n, dtype=int)
    col[0] = 1
    stack = [0]
    while stack:
        i = stack.pop()
        for j in range(n):
            if A[i, j] != 0:
                want = col[i] * int(np.sign(A[i, j]))
                if col[j] == 0:
                    col[j] = want
                    stack.append(j)
                elif col[j] != want:
                    return False
    return True


def random_signed_graph(n, p, rng, balanced):
    """Connected undirected random graph with weights in [0.5, 1.5]."""
    while True:
        U = np.triu(rng.random((n, n)) < p, 1)
        G = U | U.T
        # connectivity check
        seen = {0}; st = [0]
        while st:
            i = st.pop()
            for j in np.flatnonzero(G[i]):
                if j not in seen:
                    seen.add(j); st.append(j)
        if len(seen) == n:
            break
    W = np.triu(rng.uniform(0.5, 1.5, (n, n)), 1)
    W = (W + W.T) * G
    if balanced:
        camp = rng.choice([-1, 1], n)
        if abs(camp.sum()) == n:
            camp[0] = -camp[0]
        S = np.outer(camp, camp)
        return W * S, camp
    S = np.where(rng.random((n, n)) < 0.5, 1, -1)
    S = np.triu(S, 1); S = S + S.T
    return W * S, None


# ---- additions for the 095 reproduction (ledger L4304, L4307, L4308, L4310, L4311) ----

def signed_laplacian_rows(A: np.ndarray) -> np.ndarray:
    """Directed form L = C - A, C = diag(sum_j |a_ij|) (095 sec 2, eq (4))."""
    return signed_laplacian(A)


def gauge(A: np.ndarray, camp: np.ndarray) -> np.ndarray:
    """D A D with D = diag(camp)."""
    return A * np.outer(camp, camp)


def left_null(L: np.ndarray) -> np.ndarray:
    """Normalised (nu^T 1 = 1) left null vector of L (assumed one-dimensional)."""
    w, V = np.linalg.eig(L.T)
    k = int(np.argmin(np.abs(w)))
    v = np.real(V[:, k])
    return v / v.sum()


def underlying_balanced(A: np.ndarray) -> bool:
    """Structural balance of a digraph with digon-sign-symmetric signs: balance of the
    underlying undirected signed graph (sign taken from whichever arc exists)."""
    S = np.where(A != 0, np.sign(A), np.sign(A.T))
    return is_balanced(S)


def strongly_connected(A: np.ndarray) -> bool:
    n = len(A)
    R = (A != 0) | np.eye(n, dtype=bool)
    for _ in range(n):
        R = R | ((R.astype(int) @ R.astype(int)) > 0)
    return bool(R.all())


def random_strong_digraph(n: int, rng: np.random.Generator, balanced: bool, extra: float = 0.3) -> tuple[np.ndarray, np.ndarray]:
    """Strongly connected, digon-sign-symmetric signed digraph (ring i->i+1 plus random
    arcs).  Signs come from a symmetric matrix S, so a digon never has opposite signs.
    balanced: S = camp camp^T.  Unbalanced: random symmetric S, resampled until the
    underlying graph is unbalanced.  Returns (A, camp or empty)."""
    while True:
        arcs = rng.random((n, n)) < extra
        np.fill_diagonal(arcs, False)
        for i in range(n):
            arcs[i, (i + 1) % n] = True
        W = rng.uniform(0.5, 1.5, (n, n)) * arcs
        if balanced:
            camp = rng.choice([-1, 1], n)
            if abs(camp.sum()) == n:
                camp[0] = -camp[0]
            return W * np.outer(camp, camp), camp
        S = np.triu(np.where(rng.random((n, n)) < 0.5, 1, -1), 1)
        S = S + S.T
        A = W * S
        if not underlying_balanced(A):
            return A, np.array([])


def proskurnikov_example1(a31: float, a32: float) -> np.ndarray:
    """095 sec 4 Example 1: a12 = a21 = -1, agents 1 and 2 ignore agent 3."""
    return np.array([[0, -1, 0], [-1, 0, 0], [a31, a32, 0.0]])
