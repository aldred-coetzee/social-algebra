"""A reciprocity gate on the Bitcoin OTC and Alpha trust networks: does the rating a trader GIVES a
counterparty depend on the rating RECEIVED from that counterparty, and is the dependence gated?

THE TEST.  models/00-v0.md (v0.2; the same law as v0.1) writes the dyad update x_i(t+1) = a_i + r_i x_i(t) +
I_ij(x_j(t)) with I the O-jive (Gottman, Swanson & Murray 1999, doi:10.1037/0893-3200.13.1.3): ZERO for K- <= x_j <= K+ (a dead zone), a bounded constant beyond each
threshold, a function of the partner's LEVEL not of the difference [section 4.1, section 3 "D2"; ledger L0853,
L0857 (the form), L0834 (the one coupling parameter with a direction), L4367 (the linear partner term is about
0)].  Prior work 112 section 6.2 puts the rule "s_ij = +1 if zbar > theta+, -1 if zbar < -theta-, else 0" (dead-zone
widths theta+, theta-) into the sign module, and 117 section 5.1 ranks Bitcoin OTC and Alpha second for the sign law,
with "reputation at rating time and reciprocity as covariates for the rating sign" among its first runs; the data
facts are 117 section 3.4 [L4567-L4580; the tie is rated once and never re-signed, L4571].  The prediction under
test: the response of a rating to the rating received from the same counterparty has a dead zone (no response for
small received ratings).

THE DATA (local use only; sim/data/README.md has the terms).  SNAP soc-sign-bitcoinotc.csv.gz and
soc-sign-bitcoinalpha.csv.gz [L4567-L4570]: rows SOURCE,TARGET,RATING,TIME, RATING an integer in -10..10 with no
zero, TIME Unix seconds.  OTC has sub-second times (sorted); ALPHA's times are DAY-resolution (04:00 or 05:00
UTC, i.e. local midnight), so two ratings of the same day cannot be ordered.  That decides the design below.

DEFINITIONS.
 * Response pair.  An unordered pair {i, j} with BOTH directions rated and different timestamps.  i is the FIRST
   rater (rated j at t1), j the RESPONDER (rated i at t2 > t1).  x = rating j RECEIVED from i, y = rating j GAVE
   (the response).  Each ordered pair is rated at most once [L4571] so a pair gives at most one (x, y).
   OTC: 14,100 response pairs, none tied.  Alpha: 2,739 ordered pairs and 7,323 TIED pairs (same day) that carry no
   order and are kept apart (they are analysed unordered in the report, with a random orientation).
 * Time order is necessary, not sufficient, for "response": the two ratings follow one trade, and OTC's median
   gap is minutes (the report quantifies it), so the response function is an ASSOCIATION net of the persons'
   levels that mixes true reciprocation with a shared view of one trade.  Caveats are in the report.
 * Person levels.  The responder's "habit" is the mean of the ratings j gave when j rated FIRST (initiating
   ratings: no earlier rating from the counterparty), so it is not contaminated by the response mechanism.  The
   first rater's habit is the leave-one-out mean of i's other initiating ratings (whole file; for the earlier-events
   variation, only those given before the response).  Reception of i is the mean of the ratings i received from
   others.  The primary control is a RESPONDER FIXED EFFECT (absorbs every time-
   invariant trait of j: habit, reception, general reciprocity); the others are variations.
 * Embeddedness (Leskovec, Huttenlocher & Kleinberg 2010: the number of common neighbours of the endpoints
   [L4825]): common neighbours in the undirected graph of rated pairs, static (whole file) and time-respecting
   (both edges to the neighbour rated before the response).

THE FORMS (section "forms" below).  Thresholds are on the integer received rating.  P(K): the positive side
active from rating K upward; N(K): the negative side active from rating -K downward; shapes: 'step' (bounded
constants beyond the threshold: v0's literal O-jive), 'hinge' (continuous, graded beyond), 'graded' (jump plus
slope, nesting both).  A step or graded side is active AT its threshold; a hinge max(x - K, 0) is zero AT its knot K,
so a hinge's band includes its knots (Candidate.band_values).  Families: O+ (positive side only), O- (negative side
only), T (two-sided, thresholds at the origin: no dead zone for the step and graded shapes; the T hinge, knots at
+1 and -1, gives those two ratings the same response, so it is flat over {-1, +1}), D (two-sided, free band
(K-, K+): the O-jive / dead zone).  References: null, linear,
saturated (one mean per rating bin).  Exploratory, data-suggested and flagged as such: a clipped mirror and a sign
jump with a clipped mirror.  Fits are least squares on FE-absorbed data, thresholds by grid search, compared by
BIC and by cross-validation in which the thresholds are re-chosen inside every training fold.

Everything is numpy; no data are written anywhere but the git-ignored data directory (fetch).
"""
from __future__ import annotations

import gzip
import hashlib
import urllib.request
from dataclasses import dataclass, field, replace
from pathlib import Path

import numpy as np

SIM_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = SIM_DIR / "data" / "bitcoin"


@dataclass(frozen=True)
class Source:
    key: str
    filename: str
    url: str
    sha256: str
    size: int

    @property
    def path(self) -> Path:
        return DATA_DIR / self.filename


SOURCES = {
    "otc": Source("otc", "soc-sign-bitcoinotc.csv.gz", "https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz",
                  "6424ac981dad3a019f697fc1b9fcd85c19d8d9f039797758e9ffb6fea100c373", 397258),
    "alpha": Source("alpha", "soc-sign-bitcoinalpha.csv.gz", "https://snap.stanford.edu/data/soc-sign-bitcoinalpha.csv.gz",
                    "3a178611b9c2f39c9a0dc75936f28557317f1733319b49da4838232b3757cd76", 149480),
}


# ------------------------------------------------------------------ data

def sha256_of(path: Path | str) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def data_available(*keys: str) -> bool:
    return all(SOURCES[k].path.exists() for k in (keys or tuple(SOURCES)))


def fetch(keys: tuple[str, ...] = ("otc", "alpha"), timeout: float = 60.0) -> list[Path]:
    """Download the SNAP files for LOCAL USE ONLY into the git-ignored sim/data/bitcoin/.  Each download is checked
    against the recorded sha256 before anything is written; no identity is sent beyond urllib's default agent."""
    out = []
    for k in keys:
        src = SOURCES[k]
        with urllib.request.urlopen(src.url, timeout=timeout) as resp:
            data = resp.read()
        if hashlib.sha256(data).hexdigest() != src.sha256:
            raise ValueError(f"{src.url}: sha256 mismatch, nothing written")
        src.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = src.path.with_name(src.path.name + ".part")
        tmp.write_bytes(data)
        tmp.replace(src.path)
        out.append(src.path)
    return out


@dataclass(frozen=True)
class Ratings:
    platform: str
    src: np.ndarray      # rater id
    dst: np.ndarray      # ratee id
    rating: np.ndarray   # int, -10..10 without 0
    time: np.ndarray     # float seconds

    @property
    def n(self) -> int:
        return len(self.rating)


def validate_ratings(R: Ratings) -> None:
    """The properties 117 counted and that every later step relies on [L4568, L4570, L4571]."""
    if not (len(R.src) == len(R.dst) == len(R.rating) == len(R.time)):
        raise ValueError("column length mismatch")
    if not np.all(np.isfinite(R.time)):
        raise ValueError("non-finite time")
    if np.any(R.rating == 0) or np.any(np.abs(R.rating) > 10) or np.any(R.rating != np.round(R.rating)):
        raise ValueError("ratings must be integers in -10..10 without 0")
    if np.any(R.src == R.dst):
        raise ValueError("self-rating present")
    key = R.src.astype(np.int64) * (int(max(R.src.max(), R.dst.max())) + 1) + R.dst.astype(np.int64)
    if len(np.unique(key)) != len(key):
        raise ValueError("an ordered pair is rated more than once")


def ratings_from_array(platform: str, arr: np.ndarray) -> Ratings:
    arr = np.asarray(arr, dtype=np.float64)
    if arr.ndim != 2 or arr.shape[1] != 4:
        raise ValueError("expected four columns SOURCE,TARGET,RATING,TIME")
    # integrality is checked BEFORE the integer cast, which would silently truncate a rating of 2.5 to 2
    if not np.all(np.isfinite(arr[:, :3])) or np.any(arr[:, :3] != np.round(arr[:, :3])):
        raise ValueError("ids and ratings must be integers in -10..10 without 0 (finite, whole numbers)")
    R = Ratings(platform, arr[:, 0].astype(np.int64), arr[:, 1].astype(np.int64), arr[:, 2].astype(np.int64), arr[:, 3])
    validate_ratings(R)
    return R


def load_ratings(platform: str, verify: bool = True) -> Ratings:
    src = SOURCES[platform]
    if not src.path.exists():
        raise FileNotFoundError(
            f"{src.path} is missing: the SNAP Bitcoin file is local-use-only and not in the repo. Fetch it with: "
            "cd sim && ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report fetch")
    if verify and sha256_of(src.path) != src.sha256:
        raise ValueError(f"{src.path} does not match the recorded sha256 {src.sha256}")
    with gzip.open(src.path, "rt", encoding="ascii") as fh:
        arr = np.loadtxt(fh, delimiter=",", dtype=np.float64, ndmin=2)
    return ratings_from_array(platform, arr)


# ------------------------------------------------------------------ response pairs

def _reverse_index(R: Ratings) -> np.ndarray:
    """For each rating k (u -> v) the index of the rating v -> u, or -1."""
    ids, inv = np.unique(np.concatenate([R.src, R.dst]), return_inverse=True)
    m = len(ids)
    s, d = inv[: R.n].astype(np.int64), inv[R.n:].astype(np.int64)
    key, rkey = s * m + d, d * m + s
    order = np.argsort(key, kind="stable")
    sk = key[order]
    pos = np.minimum(np.searchsorted(sk, rkey), R.n - 1)
    found = sk[pos] == rkey
    return np.where(found, order[pos], -1)


@dataclass(frozen=True)
class PairStructure:
    """All index bookkeeping of one platform: which rating answers which."""
    rev: np.ndarray        # index of the reverse rating or -1
    first: np.ndarray      # k is the earlier rating of a reciprocated pair (strictly earlier)
    tied: np.ndarray       # k has a reverse rating with the same timestamp
    initiating: np.ndarray  # k opens a pair: unreciprocated, or the earlier of a reciprocated pair

    @property
    def n_pairs_reciprocal(self) -> int:
        return int(((self.rev >= 0) & (np.arange(len(self.rev)) < self.rev)).sum())

    @property
    def n_pairs_tied(self) -> int:
        return int(self.tied.sum() // 2)


def pair_structure(R: Ratings) -> PairStructure:
    rev = _reverse_index(R)
    has = rev >= 0
    t_rev = np.where(has, R.time[np.where(has, rev, 0)], np.nan)
    first = has & (R.time < t_rev)
    tied = has & (R.time == t_rev)
    initiating = ~has | first
    return PairStructure(rev, first, tied, initiating)


# ------------------------------------------------------------------ per-person histories (strictly-before queries)

class History:
    """Per-node time-sorted event lists with prefix sums: count and sum of values strictly before a time."""

    def __init__(self, nodes: np.ndarray, times: np.ndarray, values: np.ndarray):
        order = np.lexsort((times, nodes))
        nodes, times, values = nodes[order], times[order], values[order].astype(np.float64)
        self._t: dict[int, np.ndarray] = {}
        self._cs: dict[int, np.ndarray] = {}
        self._v: dict[int, np.ndarray] = {}
        if len(nodes):
            cut = np.flatnonzero(np.diff(nodes)) + 1
            for a, b in zip(np.r_[0, cut], np.r_[cut, len(nodes)]):
                u = int(nodes[a])
                self._t[u] = times[a:b]
                self._v[u] = values[a:b]
                self._cs[u] = np.r_[0.0, np.cumsum(values[a:b])]

    def before(self, node: int, t: float) -> tuple[int, float]:
        """(count, sum) of the node's events with time < t."""
        ts = self._t.get(int(node))
        if ts is None:
            return 0, 0.0
        c = int(np.searchsorted(ts, t, side="left"))
        return c, float(self._cs[int(node)][c])

    def total(self, node: int) -> tuple[int, float]:
        ts = self._t.get(int(node))
        if ts is None:
            return 0, 0.0
        return len(ts), float(self._cs[int(node)][-1])

    def last_before(self, node: int, t: float) -> float:
        ts = self._t.get(int(node))
        if ts is None:
            return float("nan")
        c = int(np.searchsorted(ts, t, side="left"))
        return float(self._v[int(node)][c - 1]) if c > 0 else float("nan")


def _mean(c: int, s: float) -> float:
    return s / c if c > 0 else float("nan")


@dataclass
class Sample:
    """One row per response pair.  x: rating the responder received; y: rating the responder gave."""
    platform: str
    x: np.ndarray
    y: np.ndarray
    resp: np.ndarray       # responder id (gives y)
    first: np.ndarray      # first rater id (gives x)
    t1: np.ndarray
    t2: np.ndarray
    year: np.ndarray       # calendar year (UTC) of the response
    emb_static: np.ndarray
    emb_prior: np.ndarray
    habit_resp: np.ndarray        # responder: mean of initiating ratings given before the response (NaN if none)
    habit_resp_all: np.ndarray    # responder: mean of all initiating ratings given (NaN if none)
    n_habit_resp: np.ndarray
    habit_first_loo: np.ndarray   # first rater: mean of other initiating ratings, whole file (NaN if none)
    recv_first_prior: np.ndarray  # first rater as ratee: mean rating received from others before the response
    recv_first_all: np.ndarray    # same, whole file, excluding the response itself
    prev_resp: np.ndarray         # responder's most recent rating given (to anyone) before the response
    copy_base: np.ndarray         # share of the responder's initiating ratings equal to x (NaN if none)
    # first rater: mean of his other initiating ratings given BEFORE the response (NaN if none); None when not built
    # (synthetic samples).  Review 2026-11-01: the earlier-events control set used habit_first_loo, a whole-file mean.
    habit_first_prior: np.ndarray | None = None
    extra: dict = field(default_factory=dict)

    _ARRAYS = ("x", "y", "resp", "first", "t1", "t2", "year", "emb_static", "emb_prior", "habit_resp",
               "habit_resp_all", "n_habit_resp", "habit_first_loo", "recv_first_prior", "recv_first_all",
               "prev_resp", "copy_base", "habit_first_prior")

    @property
    def n(self) -> int:
        return len(self.x)

    @property
    def gap(self) -> np.ndarray:
        return self.t2 - self.t1

    def subset(self, mask: np.ndarray) -> "Sample":
        mask = np.asarray(mask)
        kw = {a: (None if getattr(self, a) is None else getattr(self, a)[mask]) for a in self._ARRAYS}
        return Sample(platform=self.platform, extra={}, **kw)

    def reversed(self) -> "Sample":
        """Swap the roles of the two ratings: the EARLIER rating becomes the outcome and the later one the signal.
        Used by the time-reversal placebo; covariates tied to the old roles are dropped."""
        nan = np.full(self.n, np.nan)
        return replace(self, x=self.y.copy(), y=self.x.copy(), resp=self.first.copy(), first=self.resp.copy(),
                       habit_resp=nan, habit_resp_all=nan, n_habit_resp=nan, habit_first_loo=nan,
                       recv_first_prior=nan, recv_first_all=nan, prev_resp=nan, copy_base=nan,
                       habit_first_prior=nan, extra={})


def _embeddedness(R: Ratings, first: np.ndarray, resp: np.ndarray, t2: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Common neighbours of the pair in the undirected graph of rated pairs: whole file, and counting only the
    neighbours k for which BOTH the i-k and the j-k edges were first rated before t2."""
    earliest: dict[int, dict[int, float]] = {}
    for a, b, t in zip(R.src.tolist(), R.dst.tolist(), R.time.tolist()):
        for u, v in ((a, b), (b, a)):
            d = earliest.setdefault(u, {})
            if v not in d or t < d[v]:
                d[v] = t
    st = np.zeros(len(first), dtype=np.int64)
    pr = np.zeros(len(first), dtype=np.int64)
    for r, (i, j, tt) in enumerate(zip(first.tolist(), resp.tolist(), t2.tolist())):
        di, dj = earliest[i], earliest[j]
        if len(di) > len(dj):
            di, dj = dj, di
        common = [k for k in di if k in dj]
        st[r] = len(common)
        pr[r] = sum(1 for k in common if di[k] < tt and dj[k] < tt)
    return st, pr


def build_sample(R: Ratings, ps: PairStructure | None = None) -> tuple[Sample, dict]:
    """The response pairs of one platform with all covariates, and the bookkeeping counts."""
    ps = ps or pair_structure(R)
    k1 = np.flatnonzero(ps.first)
    k2 = ps.rev[k1]
    first, resp = R.src[k1], R.dst[k1]
    x, y = R.rating[k1].astype(np.float64), R.rating[k2].astype(np.float64)
    t1, t2 = R.time[k1], R.time[k2]
    year = 1970 + t2.astype("datetime64[s]").astype("datetime64[Y]").astype(np.int64)
    emb_static, emb_prior = _embeddedness(R, first, resp, t2)

    ini = np.flatnonzero(ps.initiating)
    init_hist = History(R.src[ini], R.time[ini], R.rating[ini])
    recv_hist = History(R.dst, R.time, R.rating)
    given_hist = History(R.src, R.time, R.rating)
    # share of the responder's initiating ratings equal to each value, for the copy-excess baseline
    init_vals: dict[int, np.ndarray] = {}
    for u in np.unique(R.src[ini]):
        init_vals[int(u)] = R.rating[ini][R.src[ini] == u]

    n = len(k1)
    habit_resp, habit_resp_all = np.full(n, np.nan), np.full(n, np.nan)
    n_habit = np.zeros(n)
    habit_first, recv_prior, recv_all, prev = (np.full(n, np.nan) for _ in range(4))
    copy_base = np.full(n, np.nan)
    habit_first_prior = np.full(n, np.nan)
    for r in range(n):
        i, j, a, b = int(first[r]), int(resp[r]), t1[r], t2[r]
        c, s = init_hist.before(j, b)
        habit_resp[r] = _mean(c, s)
        n_habit[r] = c
        c, s = init_hist.total(j)
        habit_resp_all[r] = _mean(c, s)
        if int(j) in init_vals:
            copy_base[r] = float(np.mean(init_vals[int(j)] == x[r]))
        c, s = init_hist.total(i)
        habit_first[r] = _mean(c - 1, s - x[r])          # x itself is one of i's initiating ratings
        c, s = init_hist.before(i, b)
        habit_first_prior[r] = _mean(c - 1, s - x[r])    # x (at t1 < t2) is among those given before the response
        c, s = recv_hist.before(i, b)
        recv_prior[r] = _mean(c, s)
        c, s = recv_hist.total(i)
        recv_all[r] = _mean(c - 1, s - y[r])              # y is a rating i received (from j)
        prev[r] = given_hist.last_before(j, b)
    S = Sample(R.platform, x, y, resp, first, t1, t2, year, emb_static, emb_prior, habit_resp, habit_resp_all,
               n_habit, habit_first, recv_prior, recv_all, prev, copy_base, habit_first_prior)
    info = dict(n_ratings=R.n, n_nodes=len(np.unique(np.r_[R.src, R.dst])), n_pairs_reciprocal=ps.n_pairs_reciprocal,
                n_pairs_tied=ps.n_pairs_tied, n_response_pairs=n, n_initiating=int(ps.initiating.sum()))
    return S, info


def tied_sample(R: Ratings, ps: PairStructure, seed: int = 0) -> Sample:
    """The TIED pairs (identical timestamps: on Alpha, the same day), which carry no order, given a RANDOM orientation
    (a fair coin per pair, seeded): the 'responder' is whichever rater the coin names.  Only x, y, ids, times and
    year are defined; covariates are left undefined."""
    rng = np.random.default_rng(seed)
    k1 = np.flatnonzero(ps.tied & (np.arange(R.n) < ps.rev))
    k2 = ps.rev[k1]
    flip = rng.random(len(k1)) < 0.5
    ka, kb = np.where(flip, k2, k1), np.where(flip, k1, k2)    # ka: the 'first' rating; kb: the 'response'
    n = len(k1)
    nan = np.full(n, np.nan)
    t = R.time[ka]
    year = 1970 + t.astype("datetime64[s]").astype("datetime64[Y]").astype(np.int64)
    return Sample(R.platform + "-tied", R.rating[ka].astype(np.float64), R.rating[kb].astype(np.float64),
                  R.dst[ka], R.src[ka], t, R.time[kb], year, np.zeros(n, dtype=np.int64), np.zeros(n, dtype=np.int64),
                  nan, nan, nan, nan, nan, nan, nan, nan, habit_first_prior=nan)


def fe_mask(group: np.ndarray, extra_mask: np.ndarray | None = None) -> np.ndarray:
    """Rows whose group has at least two rows (after the optional extra mask): the rows a fixed-effects fit can use."""
    m = np.ones(len(group), dtype=bool) if extra_mask is None else np.asarray(extra_mask).copy()
    ids = np.unique(group[m], return_inverse=True)[1]
    cnt = np.bincount(ids)
    keep = np.zeros(len(group), dtype=bool)
    keep[np.flatnonzero(m)[cnt[ids] >= 2]] = True
    return keep


# ------------------------------------------------------------------ fixed-effect absorption

def contiguous(g: np.ndarray) -> np.ndarray:
    return np.unique(g, return_inverse=True)[1].astype(np.int64)


def _demean_once(A: np.ndarray, g: np.ndarray) -> None:
    """Subtract the group mean from every column of A, in place (groups sorted once, one reduceat for all columns)."""
    order = np.argsort(g, kind="stable")
    gs = g[order]
    starts = np.r_[0, np.flatnonzero(np.diff(gs)) + 1]
    cnt = np.diff(np.r_[starts, len(gs)]).astype(np.float64)
    sums = np.add.reduceat(A[order], starts, axis=0)
    means = np.empty_like(A)
    means[order] = np.repeat(sums / cnt[:, None], cnt.astype(np.int64), axis=0)
    A -= means


def absorb(V: np.ndarray, groups: list[np.ndarray], iters: int = 500, tol: float = 1e-10) -> np.ndarray:
    """Remove group means (one-way: exact; several groupings: alternating projections to tolerance).
    V is (n,) or (n, k); groups are integer arrays (any labels).  Returns a float copy."""
    A = np.array(V, dtype=np.float64, copy=True)
    one = A.ndim == 1
    if one:
        A = A[:, None]
    if not groups:
        return A[:, 0] if one else A
    if len(groups) == 1:
        _demean_once(A, groups[0])
    else:
        for _ in range(iters):
            prev = A.copy()
            for g in groups:
                _demean_once(A, g)
            if np.abs(A - prev).max() < tol:
                break
    return A[:, 0] if one else A


# ------------------------------------------------------------------ the candidate columns (integer ratings)

PROFILE_NAMES = ("slope14", "hi58", "hi910", "neg")


def profile_columns(x: np.ndarray) -> np.ndarray:
    """Four numbers that summarise the shape of the response function, all measured against the rating +1:
    slope14: response per rating point over ratings 1..4;  hi58, hi910: level shift for ratings 5..8 and 9..10;
    neg: level shift for a negative received rating."""
    s14 = np.where((x >= 1) & (x <= 4), x - 1.0, 0.0)
    # keep slope14 a pure within-1..4 slope: ratings above 4 carry only their own level shift
    return np.column_stack([s14, ((x >= 5) & (x <= 8)).astype(float), (x >= 9).astype(float), (x < 0).astype(float)])




BINS = ((-10, -10), (-9, -6), (-5, -4), (-3, -2), (-1, -1), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
        (7, 8), (9, 9), (10, 10))
BASE_BIN = (1, 1)


def bin_name(b: tuple[int, int]) -> str:
    return f"B{b[0]}_{b[1]}"


def column_bank(x: np.ndarray) -> tuple[list[str], np.ndarray]:
    """Every candidate design column as a function of the received rating x (floats holding integers)."""
    cols: dict[str, np.ndarray] = {"lin": x.astype(np.float64)}
    for K in range(2, 11):
        cols[f"Ps{K}"] = (x >= K).astype(np.float64)
    for K in range(1, 10):
        cols[f"Ph{K}"] = np.maximum(x - K, 0.0)
    for K in range(1, 11):
        cols[f"Ns{K}"] = (x <= -K).astype(np.float64)
    for K in range(1, 10):
        cols[f"Nh{K}"] = np.maximum(-K - x, 0.0)
    for U in range(1, 11):
        cols[f"Cl{U}"] = np.clip(x, -U, U)
        cols[f"Cp{U}"] = np.minimum(np.maximum(x, 0.0), U)
    for b in BINS:
        if b != BASE_BIN:
            cols[bin_name(b)] = ((x >= b[0]) & (x <= b[1])).astype(np.float64)
    for nm, col in zip(PROFILE_NAMES, profile_columns(x).T):
        cols["p_" + nm] = col
    names = list(cols)
    return names, np.column_stack([cols[k] for k in names])


# ------------------------------------------------------------------ forms

SHAPES = ("step", "hinge", "graded")


def p_cols(K: int, shape: str) -> list[str]:
    """Positive side active from rating K.  K = 1 has no step column (it would duplicate the sign step N(1))."""
    step = [f"Ps{K}"] if K >= 2 else []
    hinge = [f"Ph{K}"] if K <= 9 else []
    return {"step": step, "hinge": hinge, "graded": step + hinge}[shape]


def n_cols(K: int, shape: str) -> list[str]:
    """Negative side active from rating -K downward."""
    step = [f"Ns{K}"]
    hinge = [f"Nh{K}"] if K <= 9 else []
    return {"step": step, "hinge": hinge, "graded": step + hinge}[shape]


@dataclass(frozen=True)
class Candidate:
    family: str
    shape: str
    kp: int | None     # positive threshold K+ (None: no positive term)
    kn: int | None     # negative threshold K- as a positive number (rating -kn), None: no negative term
    cols: tuple[str, ...]

    @property
    def band_values(self) -> int:
        """Number of observed rating values inside the dead band.  A step or graded side is active AT its threshold, so
        its band holds 1..K+-1 and -1..-(K- - 1).  A hinge max(x - K, 0) is zero AT its knot and active from the next
        rating, so its band also holds K+ and -K-: the narrowest two-sided hinge (knots +1 and -1) is flat over {-1, +1}
        and a hinge band is never empty.  (Corrected at review, 2026-11-01: the hinge band was counted as if active at
        the knot; the ordering of candidates within a family is unchanged, every hinge count moving by the same amount.)"""
        extra = 1 if self.shape == "hinge" else 0
        return (0 if self.kp is None else self.kp - 1 + extra) + (0 if self.kn is None else self.kn - 1 + extra)

    @property
    def n_thr(self) -> int:
        return {"O+": 1, "O-": 1, "T": 0, "D": 2}[self.family]


def candidates(family: str, shape: str) -> list[Candidate]:
    if family == "O+":
        out = [Candidate(family, shape, K, None, tuple(p_cols(K, shape))) for K in range(1, 11)]
    elif family == "O-":
        out = [Candidate(family, shape, None, K, tuple(n_cols(K, shape))) for K in range(1, 11)]
    elif family == "T":
        out = [Candidate(family, shape, 1, 1, tuple(p_cols(1, shape) + n_cols(1, shape)))]
    elif family == "D":
        out = [Candidate(family, shape, kp, kn, tuple(p_cols(kp, shape) + n_cols(kn, shape)))
               for kp in range(1, 11) for kn in range(1, 11)]
    else:
        raise ValueError(family)
    out = [c for c in out if c.cols]
    out.sort(key=lambda c: (c.band_values, c.kp or 0, c.kn or 0))   # narrowest band first: ties go to it
    return out


PRESPEC_FORMS = (
    ("null", None, None), ("linear", None, None),
    ("O+", "step", None), ("O+", "hinge", None), ("O+", "graded", None),
    ("O-", "step", None), ("O-", "hinge", None), ("O-", "graded", None),
    ("T", "step", None), ("T", "hinge", None), ("T", "graded", None),
    ("D", "step", None), ("D", "hinge", None), ("D", "graded", None),
    ("saturated", None, None),
)
EXPLORATORY_FORMS = (("clip", None, None), ("jump+clip+", None, None), ("jump+clip", None, None), ("knee2", None, None))
EXPLORATORY_NAMES = frozenset(f for f, _, _ in EXPLORATORY_FORMS)


def form_label(family: str, shape: str | None) -> str:
    if family == "T" and shape == "hinge":
        # continuous at the origin needs knots at the ratings nearest zero, +1 and -1, which then get the same response
        return "two-sided at the origin, hinge (knots +1 and -1: flat over {-1, +1}, no jump)"
    base = {"null": "null (no response)", "linear": "linear (two-sided, no gate)", "saturated": "saturated (one mean per rating bin)",
            "O+": "one-sided, positive only", "O-": "one-sided, negative only",
            "T": "two-sided, no dead zone", "D": "dead zone (O-jive)",
            "clip": "clipped mirror (exploratory)", "jump+clip+": "sign jump + clipped positive mirror (exploratory)",
            "jump+clip": "sign jump + clipped mirror (exploratory)",
            "knee2": "no band, two slopes on the positive side (exploratory)"}[family]
    return base + (f", {shape}" if shape else "")


@dataclass(frozen=True)
class Fit:
    family: str
    shape: str | None
    cand: Candidate | None       # the chosen threshold candidate (None for references)
    thr: tuple                   # chosen thresholds, readable (kp, kn) / (U,) / ()
    cols: tuple[str, ...]        # design columns used (candidate columns; controls are added by the engine)
    coef: np.ndarray             # coefficients for cols + controls
    rss: float
    k: int                       # rank of the mean design (columns + controls)
    n_thr: int                   # free thresholds searched
    n: int

    def ic(self, kind: str = "bic") -> float:
        pen = np.log(self.n) if kind == "bic" else 2.0
        return self.n * np.log(self.rss / self.n) + (self.k + self.n_thr) * pen


class Engine:
    """Fixed-effects-absorbed least squares over the column bank, by Gram matrices.

    groups: contiguous integer arrays absorbed from y and every column (empty: a constant is added instead).
    controls: (n, c) numeric covariates forced into every model."""

    def __init__(self, x: np.ndarray, y: np.ndarray, groups: list[np.ndarray] | None = None,
                 controls: np.ndarray | None = None, bank: tuple[list[str], np.ndarray] | None = None):
        self.groups = list(groups or [])
        names, Z = bank if bank is not None else column_bank(x)
        C = np.zeros((len(y), 0)) if controls is None else np.asarray(controls, dtype=np.float64)
        if C.ndim == 1:
            C = C[:, None]
        cnames = [f"ctl{i}" for i in range(C.shape[1])]
        if not self.groups:
            C = np.column_stack([np.ones(len(y)), C])
            cnames = ["const"] + cnames
        self.names = list(names) + cnames
        self.idx = {n: i for i, n in enumerate(self.names)}
        self.ctl_idx = [self.idx[c] for c in cnames]
        self.W = np.column_stack([Z, C])                 # raw design bank
        self.y = np.asarray(y, dtype=np.float64)
        self.n = len(self.y)
        self.Wt = absorb(self.W, self.groups) if self.groups else self.W
        self.yt = absorb(self.y, self.groups) if self.groups else self.y
        self.G = self.Wt.T @ self.Wt
        self.zy = self.Wt.T @ self.yt
        self.yy = float(self.yt @ self.yt)

    # --- generic solver
    def _solve(self, idx: list[int]) -> tuple[np.ndarray, float, int]:
        G, c = self.G[np.ix_(idx, idx)], self.zy[idx]
        if len(idx) == 0:
            return np.zeros(0), self.yy, 0
        w, V = np.linalg.eigh(G)
        tol = 1e-9 * max(float(w.max()), 1e-300)
        keep = w > tol
        b = V[:, keep] @ ((V[:, keep].T @ c) / w[keep])
        return b, float(self.yy - b @ c), int(keep.sum())

    def fit_cols(self, family: str, shape: str | None, cols: list[str], cand: Candidate | None = None,
                 thr: tuple = (), n_thr: int = 0) -> Fit:
        idx = [self.idx[c] for c in cols] + self.ctl_idx
        b, rss, rk = self._solve(idx)
        return Fit(family, shape, cand, thr, tuple(cols), b, max(rss, 1e-12), rk, n_thr, self.n)

    def _batched_rss(self, cand_idx: np.ndarray) -> np.ndarray:
        """RSS for many same-width column sets at once.  cand_idx: (m, w) column indices (controls appended)."""
        G = self.G[cand_idx[:, :, None], cand_idx[:, None, :]]
        c = self.zy[cand_idx]
        scale = np.maximum(np.einsum("mii->mi", G).max(axis=1), 1e-300)
        eps = (1e-10 * scale)[:, None, None] * np.eye(G.shape[1])[None]
        b = np.linalg.solve(G + eps, c[:, :, None])[:, :, 0]
        return self.yy - np.einsum("mi,mi->m", b, c)

    def search(self, family: str, shape: str) -> tuple[Fit, np.ndarray, list[Candidate]]:
        """Best candidate of a family/shape by RSS (narrowest band wins ties); also the RSS of every candidate."""
        cands = candidates(family, shape)
        ctl = self.ctl_idx
        by_w: dict[int, list[int]] = {}
        for i, c in enumerate(cands):
            by_w.setdefault(len(c.cols), []).append(i)
        rss = np.full(len(cands), np.inf)
        for w, ids in by_w.items():
            arr = np.array([[self.idx[n] for n in cands[i].cols] + ctl for i in ids], dtype=np.int64)
            rss[ids] = self._batched_rss(arr)
        best = int(np.argmax(rss <= rss.min() * (1 + 1e-9) + 1e-12))     # first (narrowest) within tolerance of the min
        c = cands[best]
        fit = self.fit_cols(family, shape, list(c.cols), c, (c.kp, c.kn), c.n_thr)
        return fit, rss, cands

    # --- all forms
    def fit_form(self, family: str, shape: str | None) -> Fit:
        if family == "null":
            return self.fit_cols("null", None, [])
        if family == "linear":
            return self.fit_cols("linear", None, ["lin"])
        if family == "saturated":
            return self.fit_cols("saturated", None, [bin_name(b) for b in BINS if b != BASE_BIN])
        if family in ("O+", "O-", "T", "D"):
            return self.search(family, shape)[0]
        if family == "knee2":
            # T graded (sign jump, a line on each side through +1 and -1) plus a change of slope at the rating K: NO band.
            # K = 2 spans the same functions as the dead-zone graded fit with K+ = 2, K- = 1 (Ph1 = Ps2 + Ph2 on positive x).
            best = None
            for K in range(2, 10):
                f = self.fit_cols("knee2", None, ["Ph1", f"Ph{K}", "Ns1", "Nh1"], None, (K,), 1)
                if best is None or f.rss < best.rss * (1 - 1e-9):
                    best = f
            return best
        if family in ("clip", "jump+clip+", "jump+clip"):
            best = None
            for U in range(1, 11):
                cols = {"clip": [f"Cl{U}"], "jump+clip+": ["Ns1", f"Cp{U}"], "jump+clip": ["Ns1", f"Cl{U}"]}[family]
                f = self.fit_cols(family, None, cols, None, (U,), 1)
                if best is None or f.rss < best.rss * (1 - 1e-9):
                    best = f
            return best
        raise ValueError(family)

    def fit_all(self, forms=PRESPEC_FORMS + EXPLORATORY_FORMS) -> dict[tuple[str, str | None], Fit]:
        return {(f, s): self.fit_form(f, s) for f, s, _ in forms}

    # --- cluster-robust covariance of a fitted column set
    def cluster_cov(self, fit: Fit, cluster: np.ndarray) -> np.ndarray:
        idx = [self.idx[c] for c in fit.cols] + self.ctl_idx
        X = self.Wt[:, idx]
        e = self.yt - X @ fit.coef
        bread = np.linalg.pinv(X.T @ X)
        cl = contiguous(cluster)
        S = np.zeros((cl.max() + 1, X.shape[1]))
        np.add.at(S, cl, X * e[:, None])
        meat = S.T @ S
        G, N, K = S.shape[0], self.n, fit.k
        c = G / max(G - 1, 1) * (N - 1) / max(N - K, 1)
        return c * bread @ meat @ bread


def predict_fold(train: "Engine", test_W: np.ndarray, test_group: list[np.ndarray] | None, fit: Fit) -> np.ndarray:
    """Predictions for held-out rows from a model fitted on the training rows of `train`.
    With fixed effects the held-out row's own group mean (from the training rows) supplies the intercept:
        yhat = ybar_g + (w - wbar_g) . b.   test_group: the held-out rows' group ids in the TRAIN engine's numbering,
    -1 where the group has no training row (those rows are not predicted)."""
    idx = [train.idx[c] for c in fit.cols] + train.ctl_idx
    b = fit.coef
    if not train.groups:
        return test_W[:, idx] @ b
    g = test_group[0]
    gtr = train.groups[0]
    ng = int(gtr.max()) + 1
    cnt = np.bincount(gtr, minlength=ng).astype(np.float64)
    ybar = np.bincount(gtr, weights=train.y, minlength=ng) / np.maximum(cnt, 1)
    out = np.full(len(g), np.nan)
    ok = (g >= 0) & (cnt[np.maximum(g, 0)] > 0)
    gg = g[ok]
    if not idx:
        out[ok] = ybar[gg]
        return out
    wbar = np.column_stack([np.bincount(gtr, weights=train.W[:, j], minlength=ng) for j in idx]) / np.maximum(cnt, 1)[:, None]
    out[ok] = ybar[gg] + ((test_W[ok][:, idx] - wbar[gg]) @ b)
    return out


# ------------------------------------------------------------------ cross-validation (thresholds re-chosen in every training fold)

def make_folds(n: int, K: int, rng: np.random.Generator, cluster: np.ndarray | None = None) -> np.ndarray:
    """Fold ids 0..K-1.  With a cluster array, whole clusters go to one fold (grouped CV)."""
    if cluster is None:
        f = np.arange(n) % K
        rng.shuffle(f)
        return f
    cl = contiguous(cluster)
    fc = np.arange(cl.max() + 1) % K
    rng.shuffle(fc)
    return fc[cl]


def cv_losses(x: np.ndarray, y: np.ndarray, fe: np.ndarray | None, controls: np.ndarray | None = None,
              forms=PRESPEC_FORMS + EXPLORATORY_FORMS, K: int = 10, repeats: int = 3, seed: int = 20261101,
              grouped_by: np.ndarray | None = None) -> dict:
    """Out-of-sample squared error per row and form.  With a fixed-effect group `fe`, rows are split at random and
    the group's intercept is re-estimated from the training rows (held-out rows whose group has no training row
    are not scored, for EVERY form, so comparisons are paired).  Without fe, folds are whole clusters of
    `grouped_by` (default: none) and a constant is fitted.  Returns {form: per-row mean loss over repeats},
    plus 'rows_scored' (bool) and 'n_scored'."""
    n = len(y)
    rng = np.random.default_rng(seed)
    groups_all = [contiguous(fe)] if fe is not None else []
    bank = column_bank(x)
    loss = {(f, s): np.zeros(n) for f, s, _ in forms}
    cnt = np.zeros(n)
    for _ in range(repeats):
        folds = make_folds(n, K, rng, None if fe is not None else grouped_by)
        for k in range(K):
            te, tr = folds == k, folds != k
            if te.sum() == 0:
                continue
            g_tr = [contiguous(groups_all[0][tr])] if groups_all else []
            C_tr = None if controls is None else controls[tr]
            eng = Engine(x[tr], y[tr], g_tr, C_tr, bank=(bank[0], bank[1][tr]))
            # held-out design (same column order as eng.W)
            C_te = np.zeros((te.sum(), 0)) if controls is None else np.asarray(controls[te], dtype=np.float64).reshape(te.sum(), -1)
            if not groups_all:
                C_te = np.column_stack([np.ones(te.sum()), C_te])
            W_te = np.column_stack([bank[1][te], C_te])
            tg = None
            if groups_all:
                lut = {g: i for i, g in enumerate(np.unique(groups_all[0][tr]))}
                tg = [np.array([lut.get(g, -1) for g in groups_all[0][te]], dtype=np.int64)]
                # contiguous(groups_all[0][tr]) numbers groups by sorted unique value: same as lut above
            fits = eng.fit_all(forms)
            ids = np.flatnonzero(te)
            ok = np.ones(len(ids), dtype=bool)
            preds = {}
            for key, fit in fits.items():
                p = predict_fold(eng, W_te, tg, fit)
                ok &= np.isfinite(p)
                preds[key] = p
            for key, p in preds.items():
                loss[key][ids[ok]] += (y[ids[ok]] - p[ok]) ** 2
            cnt[ids[ok]] += 1
    rows = cnt > 0
    out = {key: np.where(rows, loss[key] / np.maximum(cnt, 1), np.nan) for key in loss}
    out["rows_scored"] = rows
    out["n_scored"] = int(rows.sum())
    return out


def paired_diff(la: np.ndarray, lb: np.ndarray, cluster: np.ndarray) -> tuple[float, float]:
    """Mean of la - lb over rows scored in both, and its cluster-robust standard error."""
    ok = np.isfinite(la) & np.isfinite(lb)
    d = (la - lb)[ok]
    cl = contiguous(cluster[ok])
    Gn = cl.max() + 1
    s = np.bincount(cl, weights=d, minlength=Gn)
    n = ok.sum()
    mean = d.mean()
    se = np.sqrt(Gn / max(Gn - 1, 1) * np.sum((s - mean * np.bincount(cl, minlength=Gn)) ** 2)) / n
    return float(mean), float(se)


# ------------------------------------------------------------------ cluster bootstrap

def cluster_rows(cluster: np.ndarray) -> list[np.ndarray]:
    cl = contiguous(cluster)
    order = np.argsort(cl, kind="stable")
    cut = np.flatnonzero(np.diff(cl[order])) + 1
    return np.split(order, cut)


def bootstrap_draw(rows_of: list[np.ndarray], rng: np.random.Generator) -> tuple[np.ndarray, np.ndarray]:
    """Resample whole clusters with replacement: returns row indices and NEW contiguous cluster ids (a cluster drawn
    twice counts as two clusters, which is what a fixed effect for it should do)."""
    pick = rng.integers(0, len(rows_of), len(rows_of))
    idx = np.concatenate([rows_of[p] for p in pick])
    new = np.repeat(np.arange(len(pick)), [len(rows_of[p]) for p in pick])
    return idx, new


# ------------------------------------------------------------------ the summary (profile) model and category model

CAT_NAMES = ("-10..-3", "-2", "-1", "2", "3", "4", "5", "6", "7", "8", "9", "10")


def cat_mask(x: np.ndarray, name: str) -> np.ndarray:
    return x <= -3 if name == "-10..-3" else x == int(name)


def category_columns(x: np.ndarray) -> np.ndarray:
    """Dummies for every received rating but +1 (negatives -10..-3 pooled), the base category."""
    cols = [(x <= -3), (x == -2), (x == -1)] + [(x == v) for v in range(2, 11)]
    return np.column_stack(cols).astype(np.float64)


class OLS:
    """Fixed-effects least squares with cluster-robust covariance (CR1) for a given design."""

    def __init__(self, X: np.ndarray, y: np.ndarray, groups: list[np.ndarray], cluster: np.ndarray, names=None):
        self.names = list(names) if names is not None else [f"b{i}" for i in range(X.shape[1])]
        Xt = absorb(X, groups) if groups else X.astype(np.float64)
        yt = absorb(y, groups) if groups else np.asarray(y, dtype=np.float64)
        keep = Xt.std(axis=0) > 1e-9
        Xt = Xt[:, keep]
        self.names = [n for n, k in zip(self.names, keep) if k]
        if not groups:
            Xt = np.column_stack([np.ones(len(yt)), Xt])
            self.names = ["const"] + self.names
        self.keep = keep
        self.Xt, self.yt = Xt, yt
        XtX = self.Xt.T @ self.Xt
        self.bread = np.linalg.inv(XtX)
        self.coef = self.bread @ (self.Xt.T @ self.yt)
        self.resid = self.yt - self.Xt @ self.coef
        cl = contiguous(cluster)
        S = np.zeros((cl.max() + 1, self.Xt.shape[1]))
        np.add.at(S, cl, self.Xt * self.resid[:, None])
        N, K, G = len(y), self.Xt.shape[1], S.shape[0]
        c = G / max(G - 1, 1) * (N - 1) / max(N - K, 1)
        self.cov = c * self.bread @ (S.T @ S) @ self.bread
        self.n, self.n_clusters = N, G

    def se(self) -> np.ndarray:
        return np.sqrt(np.diag(self.cov))

    def wald(self, R: np.ndarray, r: np.ndarray | None = None) -> tuple[float, int, float]:
        """Wald test of R b = r (cluster-robust).  Returns (chi2, df, p) with p from the chi-square law."""
        from scipy import stats
        R = np.atleast_2d(R)
        r = np.zeros(R.shape[0]) if r is None else np.asarray(r, dtype=float)
        d = R @ self.coef - r
        V = R @ self.cov @ R.T
        chi2 = float(d @ np.linalg.solve(V, d))
        return chi2, R.shape[0], float(stats.chi2.sf(chi2, R.shape[0]))

    def contrast(self, c: np.ndarray) -> tuple[float, float]:
        c = np.asarray(c, dtype=float)
        return float(c @ self.coef), float(np.sqrt(c @ self.cov @ c))


# ------------------------------------------------------------------ analyses (pure computation; the report formats them)

def sample_fe(S: Sample, extra_mask: np.ndarray | None = None) -> Sample:
    """The rows a responder-fixed-effects fit can use: responders with at least two response pairs."""
    return S.subset(fe_mask(S.resp, extra_mask))


def bin_columns(x: np.ndarray) -> tuple[list[str], np.ndarray]:
    names = [bin_name(b) for b in BINS if b != BASE_BIN]
    cols = [((x >= b[0]) & (x <= b[1])).astype(np.float64) for b in BINS if b != BASE_BIN]
    return names, np.column_stack(cols)


def gap_summary(S: Sample) -> dict:
    gap = S.gap
    qs = np.quantile(gap, [0.1, 0.25, 0.5, 0.75, 0.9])
    return dict(n=S.n, quantiles_seconds=qs.tolist(),
                share_le_1min=float((gap <= 60).mean()), share_le_10min=float((gap <= 600).mean()),
                share_le_1h=float((gap <= 3600).mean()), share_le_1d=float((gap <= 86400).mean()),
                share_le_30d=float((gap <= 30 * 86400).mean()))


def copy_excess(S: Sample, xs=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -10), B: int = 400, seed: int = 7) -> list[dict]:
    """Model-free copying.  obs = share of responses that EQUAL the received rating; base = the share of the responder's
    own initiating ratings equal to that value (what chance, given the person's habit, would give); the excess
    pi = (obs - base) / (1 - base) is the share of responses that must be copies if every other response is a draw from
    the habit.  Cluster (responder) bootstrap CI.  Rows without an initiating rating of the responder are dropped."""
    ok = np.isfinite(S.copy_base)
    x, y, base, cl = S.x[ok], S.y[ok], S.copy_base[ok], contiguous(S.resp[ok])
    rows = []
    rng = np.random.default_rng(seed)
    G = cl.max() + 1
    for v in xs:
        m = x == v
        n = int(m.sum())
        if n < 30:
            rows.append(dict(x=v, n=n, obs=None, base=None, pi=None, lo=None, hi=None))
            continue
        a = np.bincount(cl[m], weights=(y[m] == v).astype(float), minlength=G)
        b_ = np.bincount(cl[m], weights=base[m], minlength=G)
        c = np.bincount(cl[m], minlength=G).astype(float)
        obs, bs = a.sum() / c.sum(), b_.sum() / c.sum()
        pi = (obs - bs) / (1 - bs)
        draws = []
        for _ in range(B):
            pk = rng.integers(0, G, G)
            cc = c[pk].sum()
            if cc == 0:
                continue
            o, b2 = a[pk].sum() / cc, b_[pk].sum() / cc
            draws.append((o - b2) / (1 - b2))
        lo, hi = np.quantile(draws, [0.025, 0.975])
        rows.append(dict(x=v, n=n, obs=float(obs), base=float(bs), pi=float(pi), lo=float(lo), hi=float(hi)))
    return rows


def curve_table(S: Sample, fe: bool = True) -> list[dict]:
    """The response function by received-rating bin: raw mean, responder-FE shift against the rating +1 with a
    cluster-robust SE, share of negative responses, share of exact copies."""
    D = sample_fe(S) if fe else S
    names, X = bin_columns(D.x)
    ols = OLS(X, D.y, [contiguous(D.resp)] if fe else [], D.resp, names)
    rows = []
    for b in BINS:
        m = (D.x >= b[0]) & (D.x <= b[1])
        n = int(m.sum())
        row = dict(bin=b, n=n)
        if n:
            row.update(mean_y=float(D.y[m].mean()), p_neg=float((D.y[m] < 0).mean()),
                       p_copy=float((D.y[m] == D.x[m]).mean()) if b[0] == b[1] else None)
        nm = bin_name(b)
        if b == BASE_BIN:
            row.update(shift=0.0, se=None)
        elif nm in ols.names:
            c, s = ols.contrast(np.eye(len(ols.names))[ols.names.index(nm)])
            row.update(shift=c, se=s)
        else:
            row.update(shift=None, se=None)
        rows.append(row)
    return rows


FLAT_TESTS = (
    ("positive band {1, 2}: response at +2 equals response at +1", ("2",)),
    ("positive band {1, 2, 3}: flat over 1-3", ("2", "3")),
    ("positive band {1, ..., 4}: flat over 1-4", ("2", "3", "4")),
    ("positive band {1, ..., 5}: flat over 1-5", ("2", "3", "4", "5")),
    ("symmetric band of absolute rating 1: response at -1 equals response at +1", ("-1",)),
    ("symmetric band of absolute rating up to 2: flat over -2, -1, +1, +2", ("-2", "-1", "2")),
)


def flatness_tests(S: Sample, fe: bool = True) -> list[dict]:
    """The defining property of a dead zone is a FLAT response over the band.  For each candidate band (a set of observed
    received ratings around the origin) a cluster-robust Wald test that the response is the same at every rating in it
    (the rating +1 is the reference).  A dead zone containing a single observed rating cannot be tested this way."""
    D = sample_fe(S) if fe else S
    ols = OLS(category_columns(D.x), D.y, [contiguous(D.resp)] if fe else [], D.resp, list(CAT_NAMES))
    out = []
    for label, nms in FLAT_TESTS:
        if any(n not in ols.names for n in nms):
            out.append(dict(label=label, df=len(nms), chi2=None, p=None, est=None, n_min=None))
            continue
        R = np.zeros((len(nms), len(ols.names)))
        for r, n in enumerate(nms):
            R[r, ols.names.index(n)] = 1
        chi2, df, p = ols.wald(R)
        est = [float(ols.coef[ols.names.index(n)]) for n in nms]
        n_min = int(min(cat_mask(D.x, n).sum() for n in nms))
        out.append(dict(label=label, df=df, chi2=chi2, p=p, est=est, n_min=n_min))
    return out


def increment_test(S: Sample, fe: bool = True) -> dict:
    """Flatness tests the ASSOCIATION.  A dead zone in the influence could hide under a shared view of the deal, which
    adds slope inside any band; if that added part is linear over +1..+4, the O-jive's bounded step still shows as an
    EXCESS increment at K+ on top of the line.  Cluster-robust Wald test that the increments of the response over
    +1..+4 are equal (no excess step at +2, +3 or +4), responder FE; also the increment from +4 to +5.  (Added at
    review, 2026-11-01.)"""
    D = sample_fe(S) if fe else S
    ols = OLS(category_columns(D.x), D.y, [contiguous(D.resp)] if fe else [], D.resp, list(CAT_NAMES))
    if any(n not in ols.names for n in ("2", "3", "4")):
        return dict(chi2=None, df=2, p=None, inc=None, inc45=None)
    i2, i3, i4 = (ols.names.index(n) for n in ("2", "3", "4"))
    R = np.zeros((2, len(ols.names)))
    R[0, i2], R[0, i3] = 2.0, -1.0                    # (f2 - f1) - (f3 - f2), f1 = 0 (the base)
    R[1, i2], R[1, i3], R[1, i4] = -1.0, 2.0, -1.0    # (f3 - f2) - (f4 - f3)
    chi2, df, p = ols.wald(R)
    b = ols.coef
    inc45 = float(b[ols.names.index("5")] - b[i4]) if "5" in ols.names else None
    return dict(chi2=chi2, df=df, p=p, inc=[float(b[i2]), float(b[i3] - b[i2]), float(b[i4] - b[i3])], inc45=inc45)


def profile_summary(S: Sample, groups: list[np.ndarray] | None = None, controls: np.ndarray | None = None,
                    cluster: np.ndarray | None = None) -> dict:  # noqa: C901
    """The four-number profile of the response function (slope on ratings 1-4, level shifts for 5-8 and 9-10, the
    jump for a negative received rating) with cluster-robust SEs, from the fixed-effects (or pooled) fit."""
    eng = Engine(S.x, S.y, groups if groups is not None else [contiguous(S.resp)], controls)
    fit = eng.fit_cols("profile", None, ["p_" + n for n in PROFILE_NAMES])
    cov = eng.cluster_cov(fit, S.resp if cluster is None else cluster)
    nm = len(PROFILE_NAMES)
    est = {n: float(fit.coef[i]) for i, n in enumerate(PROFILE_NAMES)}
    se = {n: float(np.sqrt(max(cov[i, i], 0.0))) for i, n in enumerate(PROFILE_NAMES)}
    null = eng.fit_cols("null", None, [])
    sat = eng.fit_form("saturated", None)
    return dict(est=est, se=se, n=S.n, rss=fit.rss, r2=1 - fit.rss / null.rss, r2_saturated=1 - sat.rss / null.rss,
                n_clusters=int(len(np.unique(S.resp))), cov=cov[:nm, :nm])


def profile_alt_se(D: Sample) -> dict:
    """Standard errors of the four-number profile under other clusterings: by first rater, and two-way (responder and
    first rater: V_resp + V_first - V_row, Cameron-Gelbach-Miller), for comparison with the responder clustering."""
    base = profile_summary(D)
    first = profile_summary(D, cluster=D.first)
    row = profile_summary(D, cluster=np.arange(D.n))
    V2 = base["cov"] + first["cov"] - row["cov"]
    return dict(resp=base["se"], first=first["se"],
                two_way={n: float(np.sqrt(max(V2[i, i], 0.0))) for i, n in enumerate(PROFILE_NAMES)})


def stratified_profile(S: Sample, strata: np.ndarray, groups: list[np.ndarray] | None = None, min_n: int = 100,
                       order: list | None = None) -> dict:
    """One profile per stratum (ratings 1-4 slope, 5-8, 9-10, negative jump) in ONE responder-fixed-effects model, with
    a free level per stratum, so the strata share the fixed effects and the covariance across strata is kept.
    Strata with fewer than `min_n` rows are left out of the model (they are listed in 'too_small') because a profile
    cannot be estimated from them.  Columns with no variation inside a stratum are dropped (their names are absent)."""
    strata = np.asarray(strata)
    present = sorted(set(strata.tolist()))
    counts = {l: int((strata == l).sum()) for l in ([l for l in order if l in present] if order else present)}
    labs = [l for l, n in counts.items() if n >= min_n]
    small = [l for l, n in counts.items() if n < min_n]
    use = np.isin(strata, labs)
    D = S.subset(use)
    st = strata[use]
    P = profile_columns(D.x)
    cols, names = [], []
    for l in labs[1:]:
        cols.append((st == l).astype(float))
        names.append(f"{l}|level")
    for l in labs:
        m = (st == l).astype(float)
        for j, nm in enumerate(PROFILE_NAMES):
            cols.append(P[:, j] * m)
            names.append(f"{l}|{nm}")
    ols = OLS(np.column_stack(cols), D.y, [contiguous(D.resp)] if groups is None else groups, D.resp, names)
    return dict(ols=ols, labels=labs, n_by={l: counts[l] for l in labs}, too_small={l: counts[l] for l in small})


def strata_param(res: dict, label, name: str) -> tuple[float, float] | None:
    ols: OLS = res["ols"]
    key = f"{label}|{name}"
    if key not in ols.names:
        return None
    i = ols.names.index(key)
    return float(ols.coef[i]), float(np.sqrt(ols.cov[i, i]))


def strata_equal(res: dict, name: str, labels: list | None = None) -> tuple[float, int, float] | None:
    """Wald test that parameter `name` is the same in all the (estimable) strata."""
    ols: OLS = res["ols"]
    labs = [l for l in (labels or res["labels"]) if f"{l}|{name}" in ols.names]
    if len(labs) < 2:
        return None
    R = np.zeros((len(labs) - 1, len(ols.names)))
    for r in range(len(labs) - 1):
        R[r, ols.names.index(f"{labs[r]}|{name}")] = 1
        R[r, ols.names.index(f"{labs[r + 1]}|{name}")] = -1
    return ols.wald(R)


def trend_test(S: Sample, score: np.ndarray, groups: list[np.ndarray] | None = None) -> dict:
    """Linear trend of each profile parameter in a numeric score (e.g. the year): the profile is interacted with the
    centred score, a level shift with the score is included, and each trend coefficient has a cluster-robust SE.
    Returns {name: (trend per unit score, se), name + '_mean': (value at the mean score, se)}."""
    sc = np.asarray(score, dtype=float)
    sc = sc - sc.mean()
    P = profile_columns(S.x)
    X = np.column_stack([P, P * sc[:, None], sc])
    names = list(PROFILE_NAMES) + [n + "*score" for n in PROFILE_NAMES] + ["score"]
    ols = OLS(X, S.y, groups if groups is not None else [contiguous(S.resp)], S.resp, names)
    out = {}
    for nm in PROFILE_NAMES:
        if nm + "*score" not in ols.names:
            continue
        i, j = ols.names.index(nm + "*score"), ols.names.index(nm)
        out[nm] = (float(ols.coef[i]), float(np.sqrt(ols.cov[i, i])))
        out[nm + "_mean"] = (float(ols.coef[j]), float(np.sqrt(ols.cov[j, j])))
    return out


def year_trend(rows: list[dict], name: str) -> dict | None:
    """The trend of one profile parameter judged against the year-to-year scatter.  trend_test's pooled SE treats the
    years as if they left the line only by sampling error; here the yearly estimates of year_table (disjoint rows) are
    regressed on the year by weighted least squares (weights 1/SE^2), with the lack-of-fit chi2 (df = years - 2) and
    the slope's SE inflated by sqrt(chi2/df) when the years scatter about the line more than their SEs allow.  (Added at
    review, 2026-11-01.)"""
    from scipy import stats
    rr = [r for r in rows if "est" in r]
    if len(rr) < 3:
        return None
    t = np.array([r["year"] for r in rr], dtype=float)
    est = np.array([r["est"][name] for r in rr], dtype=float)
    w = 1.0 / np.array([r["se"][name] for r in rr], dtype=float) ** 2
    tc = t - np.average(t, weights=w)
    b = float(np.sum(w * tc * est) / np.sum(w * tc * tc))
    a = float(np.average(est, weights=w))
    se = float(np.sqrt(1.0 / np.sum(w * tc * tc)))
    lof = float(np.sum(w * (est - a - b * tc) ** 2))
    df = len(rr) - 2
    return dict(slope=b, se=se, lof=lof, df=df, p_lof=float(stats.chi2.sf(lof, df)),
                se_infl=se * float(np.sqrt(max(1.0, lof / df))), years=t.astype(int).tolist())


def year_table(S: Sample, min_n: int = 100) -> list[dict]:
    """By response year: pairs, FE rows, the response at +2 against +1 (the first step out of the candidate dead zone),
    the profile, and the chosen dead-zone thresholds.  Years with fewer than `min_n` FE rows are listed, not fitted."""
    rows = []
    for yr in sorted(set(S.year.tolist())):
        Y = S.subset(S.year == yr)
        D = sample_fe(Y)
        row = dict(year=int(yr), pairs=Y.n, fe_rows=D.n)
        if D.n < min_n:
            rows.append(row)
            continue
        ols = OLS(category_columns(D.x), D.y, [contiguous(D.resp)], D.resp, list(CAT_NAMES))
        if "2" in ols.names:
            c, se = ols.contrast(np.eye(len(ols.names))[ols.names.index("2")])
            row.update(shift2=c, se2=se)
        ps = profile_summary(D)
        row.update(est=ps["est"], se=ps["se"])
        eng = Engine(D.x, D.y, [contiguous(D.resp)])
        row.update(d_graded=eng.fit_form("D", "graded").thr, d_step=eng.fit_form("D", "step").thr)
        rows.append(row)
    return rows


def habit_offset_table(S: Sample, xs=(1, 2, 3, 4, 5, 8, 10, -1, -10), min_n: int = 15) -> list[dict]:
    """The response measured against the responder's OWN habit (mean of the ratings j gave when j rated first, whole
    file): d = y - habit, by received rating, with a cluster-robust SE of the mean.  A zero-influence point shows as d = 0."""
    ok = np.isfinite(S.habit_resp_all)
    d = (S.y - S.habit_resp_all)[ok]
    x, cl = S.x[ok], contiguous(S.resp[ok])
    G = cl.max() + 1
    rows = []
    for v in xs:
        m = x == v
        n = int(m.sum())
        if n < min_n:
            rows.append(dict(x=v, n=n, mean=None, se=None))
            continue
        mean = d[m].mean()
        s_g = np.bincount(cl[m], weights=d[m] - mean, minlength=G)
        k = len(np.unique(cl[m]))
        se = np.sqrt(k / max(k - 1, 1) * np.sum(s_g ** 2)) / n
        rows.append(dict(x=v, n=n, mean=float(mean), se=float(se)))
    return rows


def sign_margin(S: Sample) -> dict:
    """The sign gate in probability: share of negative responses after a negative against a positive received rating, and
    the responder-FE difference with a cluster-robust SE."""
    D = sample_fe(S)
    neg = (D.x < 0).astype(float)[:, None]
    yb = (D.y < 0).astype(float)
    ols = OLS(neg, yb, [contiguous(D.resp)], D.resp, ["neg"])
    c, se = ols.contrast(np.array([1.0]))
    return dict(n_neg=int((S.x < 0).sum()), n_pos=int((S.x > 0).sum()),
                p_neg_after_neg=float((S.y[S.x < 0] < 0).mean()), p_neg_after_pos=float((S.y[S.x > 0] < 0).mean()),
                n_neg_resp=int((S.y < 0).sum()), p_neg_before_neg=float((S.x[S.y < 0] < 0).mean()),
                share_m10=float((S.x[S.x < 0] == -10).mean()), n_m10=int((S.x == -10).sum()),
                fe_diff=c, fe_se=se)


def wald_any_response(S: Sample) -> tuple[float, int, float]:
    D = sample_fe(S)
    ols = OLS(category_columns(D.x), D.y, [contiguous(D.resp)], D.resp, list(CAT_NAMES))
    return ols.wald(np.eye(len(ols.names)))


def cap_per_responder(S: Sample, cap: int = 3, seed: int = 5) -> Sample:
    """At most `cap` response pairs per responder, chosen at random (seeded): the check that a few busy responders do not
    carry the curve."""
    rng = np.random.default_rng(seed)
    keep = np.zeros(S.n, dtype=bool)
    for rows in cluster_rows(S.resp):
        pick = rows if len(rows) <= cap else rng.choice(rows, cap, replace=False)
        keep[pick] = True
    return S.subset(keep)


def bootstrap_forms(D: Sample, B: int = 500, seed: int = 11, keep_forms=None) -> dict:
    """Cluster (responder) bootstrap of the fixed-effects fits: the thresholds the dead-zone family selects, the
    four-number profile, how much freeing the band improves on the no-band form, and the clipped-mirror knee."""
    rng = np.random.default_rng(seed)
    rows_of = cluster_rows(D.resp)
    names, Zall = column_bank(D.x)
    forms = keep_forms or (("D", "step"), ("D", "graded"), ("D", "hinge"), ("T", "graded"), ("T", "step"), ("T", "hinge"),
                           ("linear", None), ("jump+clip", None), ("knee2", None), ("saturated", None), ("null", None))
    rec = {f: [] for f in forms}
    thr = {("D", "step"): [], ("D", "graded"): [], ("D", "hinge"): []}
    prof, knee, knee2 = [], [], []
    for _ in range(B):
        idx, new = bootstrap_draw(rows_of, rng)
        eng = Engine(D.x[idx], D.y[idx], [new], bank=(names, Zall[idx]))
        for f in forms:
            fit = eng.fit_form(*f)
            rec[f].append(fit.rss)
            if f in thr:
                thr[f].append((fit.cand.kp, fit.cand.kn))
            if f == ("jump+clip", None):
                knee.append(fit.thr[0])
            if f == ("knee2", None):
                knee2.append(fit.thr[0])
        prof.append(eng.fit_cols("profile", None, ["p_" + n for n in PROFILE_NAMES]).coef)
    out = dict(rss={f: np.array(v) for f, v in rec.items()}, thr={f: np.array(v) for f, v in thr.items()},
               profile=np.array(prof), knee=np.array(knee), knee2=np.array(knee2), n=D.n, B=B)
    return out


def threshold_distribution(thr: np.ndarray, shape: str = "graded") -> dict:
    """Selection frequencies of (K+, K-) over bootstrap draws: marginals, the empty band, the narrowest band the shape
    can express (K+ = K- = 1), the modal pair.  For step and graded the narrowest band is empty; for the hinge it holds
    -1 and +1 (Candidate.band_values), so a hinge band is never empty."""
    kp, kn = thr[:, 0].astype(int), thr[:, 1].astype(int)
    pairs, cnt = np.unique(thr, axis=0, return_counts=True)
    top = np.argsort(-cnt)[:3]
    narrow = (kp == 1) & (kn == 1)
    empty = np.zeros(len(kp), dtype=bool) if shape == "hinge" else narrow
    return dict(kp={int(k): float((kp == k).mean()) for k in np.unique(kp)},
                kn={int(k): float((kn == k).mean()) for k in np.unique(kn)},
                empty=float(empty.mean()), narrowest=float(narrow.mean()),
                modal=[(tuple(int(v) for v in pairs[i]), float(cnt[i] / len(thr))) for i in top])


def profile_rss_by_kp(D: Sample, shape: str) -> list[tuple[int, int, float]]:
    """For the dead-zone family: for every positive threshold K+ the best RSS over K-, and the K- that gives it."""
    eng = Engine(D.x, D.y, [contiguous(D.resp)])
    fit, rss, cands = eng.search("D", shape)
    best: dict[int, tuple[float, int]] = {}
    for r, c in zip(rss, cands):
        if c.kp not in best or r < best[c.kp][0]:
            best[c.kp] = (float(r), c.kn)
    return [(kp, best[kp][1], best[kp][0]) for kp in sorted(best)]


# ---- fixed-design cross-validation (no threshold search): for coding variations

def cv_design(designs: dict[str, np.ndarray], y: np.ndarray, fe: np.ndarray, K: int = 10, repeats: int = 3,
              seed: int = 20261101) -> dict:
    """Out-of-sample squared error for fixed designs under responder fixed effects: random row folds, group means from
    the training rows, rows whose group has no training row not scored (same rows for every design)."""
    n = len(y)
    g = contiguous(fe)
    rng = np.random.default_rng(seed)
    loss = {k: np.zeros(n) for k in designs}
    cnt = np.zeros(n)
    for _ in range(repeats):
        folds = make_folds(n, K, rng)
        for k in range(K):
            te, tr = folds == k, folds != k
            gt = g[tr]
            ng = int(g.max()) + 1
            c = np.bincount(gt, minlength=ng).astype(float)
            ybar = np.bincount(gt, weights=y[tr], minlength=ng) / np.maximum(c, 1)
            ok = c[g[te]] > 0
            ids = np.flatnonzero(te)[ok]
            for name, X in designs.items():
                Xtr = X[tr]
                xbar = np.column_stack([np.bincount(gt, weights=Xtr[:, j], minlength=ng) for j in range(X.shape[1])]) / np.maximum(c, 1)[:, None] if X.shape[1] else np.zeros((ng, 0))
                Xd = Xtr - xbar[gt]
                yd = y[tr] - ybar[gt]
                b = np.linalg.lstsq(Xd, yd, rcond=None)[0] if X.shape[1] else np.zeros(0)
                gg = g[ids]
                pred = ybar[gg] + ((X[ids] - xbar[gg]) @ b if X.shape[1] else 0.0)
                loss[name][ids] += (y[ids] - pred) ** 2
            cnt[ids] += 1
    rows = cnt > 0
    out = {k: np.where(rows, v / np.maximum(cnt, 1), np.nan) for k, v in loss.items()}
    out["rows_scored"] = rows
    return out


# ---- the specification variations

def spec_summary(S: Sample, spec: str) -> dict | None:
    """One control specification: the profile, the dead-zone thresholds, the best pre-specified form by BIC.
    Specs: raw | fe | fe2 (responder and first-rater FE) | cov_all (the responder's habit, the first rater's habit and
    reputation, whole file) | cov_prior (the same three from events before the response only) | fe_inertia."""
    X = S
    groups: list[np.ndarray] = []
    controls = None
    if spec == "raw":
        pass
    elif spec == "fe":
        X = sample_fe(S)
        groups = [contiguous(X.resp)]
    elif spec == "fe2":
        keep = np.ones(S.n, bool)
        while True:
            ci, cj = {}, {}
            for a, b_ in zip(S.first[keep], S.resp[keep]):
                ci[a] = ci.get(a, 0) + 1
                cj[b_] = cj.get(b_, 0) + 1
            k2 = keep & np.array([ci.get(a, 0) >= 2 and cj.get(b_, 0) >= 2 for a, b_ in zip(S.first, S.resp)])
            if k2.sum() == keep.sum():
                break
            keep = k2
        X = S.subset(keep)
        groups = [contiguous(X.resp), contiguous(X.first)]
    elif spec in ("cov_all", "cov_prior"):
        if spec == "cov_prior" and S.habit_first_prior is None:
            raise ValueError("cov_prior needs habit_first_prior (built by build_sample)")
        # review 2026-11-01: cov_prior used the whole-file habit_first_loo; it now uses events before the response only
        cols = [S.habit_resp_all, S.habit_first_loo, S.recv_first_all] if spec == "cov_all" else \
               [S.habit_resp, S.habit_first_prior, S.recv_first_prior]
        C = np.column_stack(cols)
        ok = np.all(np.isfinite(C), axis=1)
        X, controls = S.subset(ok), C[ok]
    elif spec == "fe_inertia":
        ok = np.isfinite(S.prev_resp)
        X = sample_fe(S, ok)
        groups = [contiguous(X.resp)]
        controls = X.prev_resp
    else:
        raise ValueError(spec)
    if X.n < 200:
        return None
    eng = Engine(X.x, X.y, groups, controls)
    prof_fit = eng.fit_cols("profile", None, ["p_" + n for n in PROFILE_NAMES])
    cov = eng.cluster_cov(prof_fit, X.resp)
    est = {n: float(prof_fit.coef[i]) for i, n in enumerate(PROFILE_NAMES)}
    se = {n: float(np.sqrt(max(cov[i, i], 0.0))) for i, n in enumerate(PROFILE_NAMES)}
    fits = eng.fit_all(PRESPEC_FORMS)
    null = fits[("null", None)]
    best = min((k for k in fits if k[0] not in ("null", "saturated")), key=lambda k: fits[k].ic("bic"))
    dg, dsl = fits[("D", "graded")], fits[("D", "step")]
    return dict(spec=spec, n=X.n, est=est, se=se, r2_profile=1 - prof_fit.rss / null.rss,
                r2_linear=1 - fits[("linear", None)].rss / null.rss, r2_saturated=1 - fits[("saturated", None)].rss / null.rss,
                d_graded=dg.thr, d_step=dsl.thr, best_bic=best, bic_gap_d_vs_t=fits[("D", "graded")].ic("bic") - fits[("T", "graded")].ic("bic"),
                ctl_coef=[float(c) for c in prof_fit.coef[len(PROFILE_NAMES):]])


def signal_coding_cv(S: Sample, K: int = 10, repeats: int = 3, seed: int = 20261101) -> dict | None:
    """Absolute received rating x against the rating RELATIVE to the first rater's own habit u = x - habit (the signal's
    'surprise'): fixed designs, responder-FE CV.  Rows without a first-rater habit are dropped."""
    ok = np.isfinite(S.habit_first_loo)
    D = sample_fe(S, ok)
    if D.n < 500:
        return None
    u = D.x - D.habit_first_loo
    ub = np.column_stack([(u > lo) & (u <= hi) for lo, hi in
                          ((-np.inf, -4), (-4, -2), (-2, -1), (-1, 0), (1, 2), (2, 4), (4, np.inf))]).astype(float)   # (0, 1] is the base
    _, xb = bin_columns(D.x)
    sign = (D.x < 0).astype(float)[:, None]
    designs = {
        "linear in x": D.x[:, None],
        "linear in u": u[:, None],
        "linear in x and u": np.column_stack([D.x, u]),
        "x bins (saturated in x)": xb,
        "u bins (saturated in u)": ub,
        "sign(x) + u bins": np.column_stack([sign, ub]),
        "x bins + u bins": np.column_stack([xb, ub]),
        "x bins + linear u": np.column_stack([xb, u]),
    }
    cv = cv_design(designs, D.y, D.resp, K, repeats, seed)
    mse = {k: float(np.nanmean(cv[k])) for k in designs}
    best = min(mse, key=mse.get)
    diff = {k: paired_diff(cv[k], cv[best], D.resp) for k in designs}
    base = float(np.nanmean(cv_design({"null": np.zeros((D.n, 0))}, D.y, D.resp, K, repeats, seed)["null"]))
    return dict(n=D.n, mse=mse, best=best, diff=diff, null_mse=base)


def response_rates(R: Ratings, ps: PairStructure, window_days: float = 30.0) -> list[dict]:
    """Extensive margin: for every FIRST rating (one that opens its pair), the share answered by a rating of the other
    direction within `window_days`, by the rating given.  First ratings in the last `window_days` of the file are
    dropped (they cannot have been answered yet).  Only for a platform with exact timestamps."""
    t_end = R.time.max()
    first = ps.initiating & (R.time <= t_end - window_days * 86400)
    ans = np.zeros(R.n, dtype=bool)
    has = ps.rev >= 0
    tr = np.where(has, R.time[np.where(has, ps.rev, 0)], np.nan)
    ans[has] = (tr[has] > R.time[has]) & (tr[has] - R.time[has] <= window_days * 86400)
    rows = []
    for b in BINS:
        m = first & (R.rating >= b[0]) & (R.rating <= b[1])
        n = int(m.sum())
        if n == 0:
            rows.append(dict(bin=b, n=0))
            continue
        k = int(ans[m].sum())
        p = k / n
        z = 1.96
        den = 1 + z * z / n
        centre = (p + z * z / (2 * n)) / den
        half = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
        rows.append(dict(bin=b, n=n, answered=k, rate=p, lo=float(centre - half), hi=float(centre + half)))
    return rows
