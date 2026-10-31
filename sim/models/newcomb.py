"""Newcomb fraternity: the n = 3 refutation test of models/00-v0.md section 7, run on data.

Prior work: docs/prior-work/104-newcomb-doreian-krackhardt-at-source.md (direction D596);
triangle types and weak vs strict balance: docs/prior-work/084 sections 4-6.  Ledger ids are
given as [L....] and are the lines of docs/ledger.jsonl with source "104 §..." (L4471-L4546).

THE TEST (v0.1 section 7, n = 3; "v0's hypothesis, not a source's"): in longitudinal signed
triads the one-negative triangle must be (a) under-represented against a sign-shuffled null and
(b) convert to a balanced triangle faster than the all-negative one; "if conversion runs at the
null rate, (4.2b)/(5.1) is refuted".  Half (a) is D&K's static count, half (b) is the NEW
computation: neither paper prints a type-to-type transition table [L4527].

DATA (local use only, never committed; sim/data/README.md has the terms).  Fifteen 17 x 17
sociomatrices NEWC0-NEWC15 without NEWC9, each row a forced rank 1-16 of the other 16 men
[L4471, L4538].  "Waves" 1..15 below are observation indices (D&K's "weeks"); wave 9 is NEWC8 and
wave 10 is NEWC10, so transition 9 -> 10 spans two calendar weeks, which the authors ignored
[L4472, L4545 (the week mapping is 104's inference)].  The UCI mirror's 14 networks [L4543] is
not what is used.  Absence of a stated licence is not a grant [L4539, L4544].

THE SIGN RECODE IS A MODELLING CHOICE, NOT DATA.  The files hold ranks only.  Following Doreian
& Krackhardt (2001) ranks 1-4 become + ("L", like), ranks 14-16 become - ("D", dislike) and
ranks 5-13 become 0, so every man sends exactly 4 positive, 3 negative and 9 null ties in every
wave [L4476; 68 + and 51 - ties per wave, L4480].  D&K call this "a major data problem": a man
ranking 16 others cannot be told from his ranks to dislike all of them or merely like none
[L4479].  The sign never records a sign the men reported, the cut is the analysts' [L4477,
L4478], and a "conversion" can be a rank crossing the cut-off.  The sensitivity recodes (top-3
/ bottom-3, top-5 / bottom-4, and D&K's own top-3 / bottom-2) change the cut, nothing else.
Null ties are a third state here; absence is NOT coded negative (unlike file 102, L4429).

OBJECTS.
 * Directed triple (i, j, k), ordered, ties i->j, j->k and the completion i->k, all signed;
   eight types named by the signs in that order, L = +, D = - [L4481].  (The brief of 2026-10-31
   said "the 16 D&K types"; D&K have eight.  Sixteen is Leskovec et al.'s count of directed triad
   types with edge direction, 084 section 4.)  Heider-balanced = even number of D, i.e. LLL, LDD,
   DLD, DDL [L4482]; Davis weak balance also allows DDD [L4483].  One-negative = LLD, LDL, DLL;
   all-negative = DDD.  Counted over ALL ordered triples, not conditioned to be independent.
 * Undirected triangle: a vertex triple {i, j, k} whose three pairs all carry a nonzero
   symmetrised sign.  Two symmetrisation rules, both modelling choices (104 section 8(b) says
   one must be recorded): "agree" = the common sign if both directions agree, else 0 (so only
   mutual ties survive; this is the rule of the brief and the one faithful to v0's symmetric
   a_ij); "sum" = sign(S_ij + S_ji), so one signed direction is enough and a + / - conflict is
   0.  Types by number of negative edges: 0 (+++), 1 (++-), 2 (+--), 3 (---).  Strict (Heider /
   Cartwright-Harary, v0 (4.2b)) balanced = 0 or 2 negatives; weak (Davis) balanced additionally
   allows 3, forbidding only the one-negative triangle [084 section 10; v0 section 4.2].
   A triple with a zero pair is "incomplete", which v0 section 4.2 calls vacuously balanced.

NULLS.
 * Static: D&K's row-wise shuffle [L4485]: each man's 16 ranks are re-assigned to the other 16 at
   random and recoded, so every man keeps his 4 L and 3 D out-ties and received ties are free.
   10,000 draws.  The shuffle's distribution does not depend on the observed wave (every row of
   every wave is a permutation of 1..16), so one sample of draws serves all 15 waves; D&K's
   "per wave" [L4485 note] is the same in distribution.  D&K's statistic p(obs > random) is the
   share of draws whose simulated count the observation strictly exceeds; > 0.95 is "significantly
   more", < 0.05 "significantly fewer" [L4486].  That lower-tail rule counts a tie as "fewer", so
   it is only used for the directed counts (tens to hundreds); the sparse triangle counts use
   the tie-inclusive exact Monte-Carlo p-values instead.
 * Dynamics, two nulls for the same conversion rates:
   "indep"  - both waves of a transition re-shuffled independently (the literal "shuffled
              waves").  Persistence is destroyed, so the null conversion rate is just the
              marginal share of balanced triples and observed rates fall far below it for every
              type; it does not isolate balance pressure and is reported only to show that.
   "cond"   - the start wave is kept and the next wave's ties are re-assigned at random WITHIN
              each stratum of start sign, keeping every man's start -> end transition table
              (directed triples: per sender row), or the whole dyad transition table of the
              symmetrised graph (triangles).  Persistence, turnover, 4/3/9 counts and the sign
              flow are held; only WHICH ties change is randomised.  An excess of conversion over
              this null is the signature of changes aimed at tension; it cannot tell balance from
              reciprocity, popularity or rivalry, which are D&K's other mechanisms [L4511,
              L4512, L4515].
 Conversion rate of start class A into target set G over a window of transitions = (triples of
 class A at wave w that are of a type in G at w + 1) / (triples of class A at wave w), pooled.
 Targets: strict balanced complete types, weak balanced complete types, and (separately)
 incomplete (a tie fell to 0); "relief" = strict balanced OR incomplete, which reads v0 section 4.2's
 "one tie absent -> vacuously balanced" literally.  Permutation p-values use (1 + #{null >= obs}) /
 (B + 1).

FIXED BEFORE ANY RESULT WAS COMPUTED (so the verdict cannot be shopped).  Primary recode 4/3;
10,000 draws; headline cells (H1) the eight directed D&K types over all 14 transitions pooled and
(H2) undirected triangles under "agree" over all 14 transitions pooled; the secondary cells are
the "sum" rule, the windows (first 5 transitions, last 9, all but the two-week gap), and the
three sensitivity recodes.  ADDED AFTER the first transition matrices were seen (so post hoc, though
motivated by v0's own convention): the "relief" target, because nearly every exit from a tense
triple goes through a tie dropping to 0 rather than through a sign change, and the reading of the
z-score matrices as to where tension goes.  Nothing was dropped for disagreeing.

Per-wave tests of D&K's reported pattern are regression assertions in
tests/test_newcomb_triads.py; a non-reproduction is a finding and is recorded, not tuned away.
"""
from __future__ import annotations

import hashlib
import itertools
import re
import urllib.request
from dataclasses import dataclass
from pathlib import Path

import numpy as np

# ------------------------------------------------------------------ constants

N = 17  # actors [L4471]
N_WAVES = 15  # observation indices 1..15 [L4471, L4472]
N_TRANSITIONS = N_WAVES - 1  # 14 [L4472]
GAP_TRANSITION = 9  # 1-based: wave 9 (NEWC8) -> wave 10 (NEWC10) spans two calendar weeks [L4472, L4545]
WAVE_LABELS = tuple(f"NEWC{k}" for k in (0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 13, 14, 15))

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "newcomb"
DATA_FILE = DATA_DIR / "newfrat.dat"
SHA256 = "884537cbb60cf6c9c8e3cea3fa2d9f4a54fef8981b28151e65d65c5d89d43b46"
# Original host (vlado.fmf.uni-lj.si) timed out from the box on 2026-10-31 [L4538]; the Wayback
# snapshots of the same path are public and byte-identical (checked 2021-04-21 vs 2024-10-04).
SOURCE_URLS = (
    "https://web.archive.org/web/20241004180913id_/http://vlado.fmf.uni-lj.si/pub/networks/data/UciNet/newfrat.dat",
    "https://web.archive.org/web/20210421135101id_/http://vlado.fmf.uni-lj.si/pub/networks/data/UciNet/newfrat.dat",
    "http://vlado.fmf.uni-lj.si/pub/networks/data/UciNet/newfrat.dat",
)

TRIPLE_TYPES = ("LLL", "LLD", "LDL", "LDD", "DLL", "DLD", "DDL", "DDD")  # (i->j)(j->k)(i->k) [L4481]
TRIPLE_BALANCED = ("LLL", "LDD", "DLD", "DDL")  # even number of D [L4482]
TRIPLE_ONE_NEG = ("LLD", "LDL", "DLL")
TRIPLE_ALL_NEG = ("DDD",)
TRIANGLE_TYPES = ("+++", "++-", "+--", "---")  # by number of negative edges: 0, 1, 2, 3
SYM_RULES = ("agree", "sum")
RECODES = {"4/3": (4, 3), "3/3": (3, 3), "5/4": (5, 4), "3/2": (3, 2)}  # (n_pos, n_neg) [L4476, L4478]
PRIMARY_RECODE = "4/3"


@dataclass(frozen=True)
class Level:
    """Type codes of one counting level and the class sets used by the conversion statistics."""

    name: str
    labels: tuple[str, ...]  # code -> label, the last one is "inc" (a zero pair: incomplete)
    one_neg: tuple[int, ...]
    all_neg: tuple[int, ...]
    strict_bal: tuple[int, ...]  # Heider: even number of negatives [L4482]
    weak_bal: tuple[int, ...]  # Davis: strict + all-negative [L4483]

    @property
    def inc(self) -> int:
        return len(self.labels) - 1

    @property
    def k(self) -> int:
        return len(self.labels)


TRIPLE_LEVEL = Level(
    "triple",
    TRIPLE_TYPES + ("inc",),
    one_neg=tuple(TRIPLE_TYPES.index(t) for t in TRIPLE_ONE_NEG),
    all_neg=(TRIPLE_TYPES.index("DDD"),),
    strict_bal=tuple(TRIPLE_TYPES.index(t) for t in TRIPLE_BALANCED),
    weak_bal=tuple(TRIPLE_TYPES.index(t) for t in TRIPLE_BALANCED + ("DDD",)),
)
TRIANGLE_LEVEL = Level(
    "triangle",
    TRIANGLE_TYPES + ("inc",),
    one_neg=(1,),
    all_neg=(3,),
    strict_bal=(0, 2),
    weak_bal=(0, 2, 3),
)

# index tables ---------------------------------------------------------------

_ORD = np.array([t for t in itertools.product(range(N), repeat=3) if len(set(t)) == 3], dtype=np.intp)
TRI_I, TRI_J, TRI_K = _ORD[:, 0], _ORD[:, 1], _ORD[:, 2]  # 17 * 16 * 15 = 4080 ordered triples
_VT = np.array(list(itertools.combinations(range(N), 3)), dtype=np.intp)
VT_I, VT_J, VT_K = _VT[:, 0], _VT[:, 1], _VT[:, 2]  # C(17, 3) = 680 vertex triples
_DY = np.array(list(itertools.combinations(range(N), 2)), dtype=np.intp)
DY_I, DY_J = _DY[:, 0], _DY[:, 1]  # 136 dyads
_DIDX = np.full((N, N), -1, dtype=np.intp)
_DIDX[DY_I, DY_J] = np.arange(len(_DY))
_DIDX[DY_J, DY_I] = np.arange(len(_DY))
D_IJ, D_IK, D_JK = _DIDX[VT_I, VT_J], _DIDX[VT_I, VT_K], _DIDX[VT_J, VT_K]
OFF_COLS = np.array([[j for j in range(N) if j != i] for i in range(N)], dtype=np.intp)  # (17, 16)
ROWS = np.arange(N)[:, None]


# ------------------------------------------------------------------ data

def sha256_of(path: Path) -> str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def parse_dl(text: str) -> tuple[tuple[str, ...], np.ndarray]:
    """Parse a UCINET DL full-matrix file with level labels: returns (labels, array (nm, n, n))."""
    lines = [ln.strip() for ln in text.replace("\r", "").split("\n")]
    lines = [ln for ln in lines if ln]
    if not lines or lines[0].upper() != "DL":
        raise ValueError("not a DL file")
    head = lines[1].upper()
    n = int(re.search(r"\bN\s*=\s*(\d+)", head).group(1))
    nm = int(re.search(r"\bNM\s*=\s*(\d+)", head).group(1))
    fmt = lines[2].upper()
    if "FULLMATRIX" not in fmt or "DIAGONAL PRESENT" not in fmt:
        raise ValueError(f"unsupported DL format line: {lines[2]!r}")
    if lines[3].upper() != "LEVEL LABELS:":
        raise ValueError("expected LEVEL LABELS:")
    k = 4
    labels = []
    while lines[k].upper() != "DATA:":
        labels.append(lines[k])
        k += 1
    if len(labels) != nm:
        raise ValueError(f"{len(labels)} labels but NM={nm}")
    nums = np.array([int(tok) for ln in lines[k + 1:] for tok in ln.split()], dtype=np.int64)
    if nums.size != nm * n * n:
        raise ValueError(f"{nums.size} numbers, expected {nm * n * n}")
    return tuple(labels), nums.reshape(nm, n, n)


def load_ranks(path: Path | str = DATA_FILE, verify: bool = True) -> np.ndarray:
    """The 15 rank matrices, shape (15, 17, 17), int8, diagonal 0, off-diagonal ranks 1-16.
    Every row is checked to be a permutation of 1..16 and the label list to be NEWC0-NEWC15 without
    NEWC9, which is the count D&K and the 1996 paper use [L4471, L4472, L4543, L4545]."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(
            f"{path} is missing: the Newcomb rank file is local-use-only and is not in the repo. "
            "Fetch it with: cd sim && ~/.local/bin/uv run python -m models.newcomb_report fetch"
        )
    if verify and sha256_of(path) != SHA256:
        raise ValueError(f"{path} does not match the recorded sha256 {SHA256}")
    labels, arr = parse_dl(path.read_text(encoding="ascii"))
    if labels != WAVE_LABELS:
        raise ValueError(f"unexpected wave labels {labels}")
    if arr.shape != (N_WAVES, N, N):
        raise ValueError(f"unexpected shape {arr.shape}")
    if np.any(arr[:, np.arange(N), np.arange(N)] != 0):
        raise ValueError("nonzero diagonal")
    off = arr[:, ROWS, OFF_COLS]  # (15, 17, 16)
    if not np.array_equal(np.sort(off, axis=-1), np.broadcast_to(np.arange(1, N), off.shape)):
        raise ValueError("a row is not a permutation of ranks 1..16")
    return arr.astype(np.int8)


def fetch(dest: Path | str = DATA_FILE, urls: tuple[str, ...] = SOURCE_URLS, timeout: float = 60.0) -> Path:
    """Download newfrat.dat for LOCAL USE ONLY into the git-ignored sim/data/newcomb/.  Checks the
    recorded sha256 before writing anything; sends no identity beyond urllib's default agent."""
    dest = Path(dest)
    last: Exception | None = None
    for url in urls:
        try:
            with urllib.request.urlopen(url, timeout=timeout) as resp:
                data = resp.read()
        except OSError as exc:
            last = exc
            continue
        if hashlib.sha256(data).hexdigest() != SHA256:
            last = ValueError(f"{url}: sha256 mismatch")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        tmp = dest.with_name(dest.name + ".part")
        tmp.write_bytes(data)
        tmp.replace(dest)
        return dest
    raise RuntimeError(f"could not fetch the Newcomb rank file from any source: {last}")


# ------------------------------------------------------------------ recode and symmetrisation

def recode(ranks: np.ndarray, n_pos: int = 4, n_neg: int = 3) -> np.ndarray:
    """Rank -> sign: ranks 1..n_pos -> +1, ranks 17-n_neg..16 -> -1, the rest (and the diagonal) 0.
    The default is D&K's top-4 / bottom-3 [L4476]; it is a modelling choice [L4479]."""
    if n_pos < 0 or n_neg < 0 or n_pos + n_neg > N - 1:
        raise ValueError("bad cut")
    r = np.asarray(ranks)
    S = np.zeros(r.shape, dtype=np.int8)
    S[(r >= 1) & (r <= n_pos)] = 1
    S[r >= N - n_neg] = -1
    return S


def symmetrise(S: np.ndarray, rule: str = "agree") -> np.ndarray:
    """Undirected sign of each pair from the two directed signs.  "agree": the common sign if both
    directions carry the same value, else 0.  "sum": sign(S_ij + S_ji) (one signed direction is
    enough; a +/- conflict gives 0).  Both are modelling choices (module docstring)."""
    St = np.swapaxes(S, -1, -2)
    if rule == "agree":
        return np.where(S == St, S, 0).astype(np.int8)
    if rule == "sum":
        return np.sign(S.astype(np.int16) + St).astype(np.int8)
    raise ValueError(f"unknown symmetrisation rule {rule!r}")


def reciprocated_positive(S: np.ndarray) -> np.ndarray:
    """Ordered positive ties i->j with j->i also positive (1996 paper, p. 123: 30-35 of 68 per
    wave, null median about 17) [L4520, L4521]."""
    P = (S == 1)
    return (P & np.swapaxes(P, -1, -2)).sum(axis=(-2, -1))


# ------------------------------------------------------------------ counting

def _pm(S: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    return (S == 1).astype(np.float64), (S == -1).astype(np.float64)


def triple_counts(S: np.ndarray) -> np.ndarray:
    """Counts of the eight ordered-triple types, shape (..., 8) in TRIPLE_TYPES order [L4481].
    count_abc = sum_{i,j,k} A_ij B_jk C_ik = sum((A @ B) * C); zero diagonals force i, j, k distinct."""
    P, M = _pm(S)
    mats = {"L": P, "D": M}
    out = np.empty(S.shape[:-2] + (8,), dtype=np.int64)
    ab: dict[str, np.ndarray] = {}
    for t, name in enumerate(TRIPLE_TYPES):
        if name[:2] not in ab:
            ab[name[:2]] = mats[name[0]] @ mats[name[1]]
        out[..., t] = np.rint((ab[name[:2]] * mats[name[2]]).sum(axis=(-2, -1))).astype(np.int64)
    return out


def triangle_counts(s: np.ndarray) -> np.ndarray:
    """Counts of complete undirected triangles with 0, 1, 2, 3 negative edges, shape (..., 4), from
    a symmetric sign matrix.  tr-style identities: +++ = sum(P*PP)/6, ++- = sum(M*PP)/2,
    +-- = sum(P*MM)/2, --- = sum(M*MM)/6."""
    if not np.array_equal(s, np.swapaxes(s, -1, -2)):
        raise ValueError("triangle_counts needs a symmetric sign matrix")
    P, M = _pm(s)
    PP, MM = P @ P, M @ M
    ax = (-2, -1)
    c = np.stack(
        [(P * PP).sum(ax) / 6, (M * PP).sum(ax) / 2, (P * MM).sum(ax) / 2, (M * MM).sum(ax) / 6], axis=-1
    )
    return np.rint(c).astype(np.int64)


def triple_codes(S: np.ndarray) -> np.ndarray:
    """Per ordered triple (4080): 0..7 = TRIPLE_TYPES index, 8 = incomplete (some tie is 0)."""
    a, b, c = S[..., TRI_I, TRI_J], S[..., TRI_J, TRI_K], S[..., TRI_I, TRI_K]
    complete = (a != 0) & (b != 0) & (c != 0)
    code = 4 * (a < 0).astype(np.int8) + 2 * (b < 0).astype(np.int8) + (c < 0).astype(np.int8)
    return np.where(complete, code, TRIPLE_LEVEL.inc).astype(np.int8)


def _tri_codes_from(a: np.ndarray, b: np.ndarray, c: np.ndarray) -> np.ndarray:
    complete = (a != 0) & (b != 0) & (c != 0)
    neg = (a < 0).astype(np.int8) + (b < 0).astype(np.int8) + (c < 0).astype(np.int8)
    return np.where(complete, neg, TRIANGLE_LEVEL.inc).astype(np.int8)


def triangle_codes(s: np.ndarray) -> np.ndarray:
    """Per vertex triple (680): number of negative edges 0..3, 4 = incomplete."""
    return _tri_codes_from(s[..., VT_I, VT_J], s[..., VT_I, VT_K], s[..., VT_J, VT_K])


def triangle_codes_from_dyads(d: np.ndarray) -> np.ndarray:
    """Same, from a dyad vector (..., 136) in combinations(range(17), 2) order."""
    return _tri_codes_from(d[..., D_IJ], d[..., D_IK], d[..., D_JK])


def transition_counts(start: np.ndarray, end: np.ndarray, k: int) -> np.ndarray:
    """Counts [a, b] of items with start code a and end code b.  `end` is (..., M); `start` is
    (M,) or broadcastable to it; result (..., k, k)."""
    end = np.asarray(end)
    start = np.broadcast_to(np.asarray(start), end.shape).astype(np.int64)
    lead = end.shape[:-1]
    batch = int(np.prod(lead)) if lead else 1
    idx = (start * k + end).reshape(batch, -1) + (np.arange(batch) * k * k)[:, None]
    counts = np.bincount(idx.ravel(), minlength=batch * k * k)
    return counts.reshape(lead + (k, k))


def pool(counts: np.ndarray, idx: tuple[int, ...] | list[int]) -> np.ndarray:
    """Sum the last axis over the given type columns (e.g. the three one-negative triple types)."""
    return counts[..., list(idx)].sum(axis=-1)


# ------------------------------------------------------------------ nulls

def null_signs(rng: np.random.Generator, n_draws: int, n_pos: int = 4, n_neg: int = 3) -> np.ndarray:
    """D&K's null [L4485]: every man's 16 ranks assigned to the other 16 at random, recoded.
    Equivalent to a uniform random arrangement of the row's n_pos '+', n_neg '-' and the rest '0'
    over his 16 off-diagonal cells.  Shape (n_draws, 17, 17), int8."""
    base = np.zeros(N - 1, dtype=np.int8)
    base[:n_pos] = 1
    base[N - 1 - n_neg:] = -1
    rows = rng.permuted(np.broadcast_to(base, (n_draws, N, N - 1)).copy(), axis=-1)
    S = np.zeros((n_draws, N, N), dtype=np.int8)
    S[:, ROWS, OFF_COLS] = rows
    return S


def _shuffle_within_strata(rng: np.random.Generator, start: np.ndarray, end: np.ndarray, n_draws: int) -> np.ndarray:
    """Randomly permute `end` among the positions that share the same `start` value, independently
    for each draw and for each leading index.  start, end: (..., m); result (n_draws, ..., m)."""
    start, end = np.asarray(start), np.asarray(end)
    order = np.argsort(start, axis=-1, kind="stable")
    end_sorted = np.take_along_axis(end, order, axis=-1)
    keys = (start - start.min()).astype(np.float64) * 2.0 + rng.random((n_draws,) + start.shape)
    perm = np.argsort(keys, axis=-1)
    out = np.empty((n_draws,) + end.shape, dtype=end.dtype)
    np.put_along_axis(out, perm, np.broadcast_to(end_sorted, out.shape), axis=-1)
    return out


def null_next_within_rows(rng: np.random.Generator, S_w: np.ndarray, S_w1: np.ndarray, n_draws: int) -> np.ndarray:
    """'cond' null for directed triples: keep S_w; in every sender row re-assign the next wave's
    signs at random among the targets that shared the same start sign.  Each man's start -> end
    transition table (persistence, turnover, the 4/3/9 counts) is preserved exactly; only which
    ties change moves.  Shape (n_draws, 17, 17)."""
    s0 = S_w[ROWS, OFF_COLS]
    s1 = S_w1[ROWS, OFF_COLS]
    new = _shuffle_within_strata(rng, s0, s1, n_draws)
    out = np.zeros((n_draws, N, N), dtype=np.int8)
    out[:, ROWS, OFF_COLS] = new
    return out


def null_next_within_dyads(rng: np.random.Generator, s_w: np.ndarray, s_w1: np.ndarray, n_draws: int) -> np.ndarray:
    """'cond' null for undirected triangles: keep the symmetrised s_w; re-assign the next wave's
    dyad signs at random among the dyads that shared the same start sign (the dyad transition
    table is preserved).  Shape (n_draws, 136)."""
    return _shuffle_within_strata(rng, s_w[DY_I, DY_J], s_w1[DY_I, DY_J], n_draws)


def static_null(rng: np.random.Generator, n_draws: int = 10_000, n_pos: int = 4, n_neg: int = 3, chunk: int = 2000) -> dict[str, np.ndarray]:
    """Counts under D&K's row-wise sign shuffle: 'triple' (B, 8), 'agree' and 'sum' triangle counts
    (B, 4) and the reciprocated-positive count 'recip' (B,)."""
    out: dict[str, list[np.ndarray]] = {"triple": [], "agree": [], "sum": [], "recip": []}
    done = 0
    while done < n_draws:
        b = min(chunk, n_draws - done)
        S = null_signs(rng, b, n_pos, n_neg)
        out["triple"].append(triple_counts(S))
        out["agree"].append(triangle_counts(symmetrise(S, "agree")))
        out["sum"].append(triangle_counts(symmetrise(S, "sum")))
        out["recip"].append(reciprocated_positive(S))
        done += b
    return {k: np.concatenate(v) for k, v in out.items()}


def observed_counts(S: np.ndarray) -> dict[str, np.ndarray]:
    """The same four quantities for the observed waves S (15, 17, 17)."""
    return {
        "triple": triple_counts(S),
        "agree": triangle_counts(symmetrise(S, "agree")),
        "sum": triangle_counts(symmetrise(S, "sum")),
        "recip": reciprocated_positive(S),
    }


def compare_to_null(obs: np.ndarray, null: np.ndarray) -> dict[str, np.ndarray]:
    """obs (..., K) counts vs null draws (B, K).  Returns arrays shaped like obs:
    mean, sd, z (nan where sd = 0), p_gt = share of draws strictly below the observation (D&K's
    p(obs > random) [L4486]), p_lt = share strictly above, and the tie-inclusive exact Monte-Carlo
    p-values p_up = (1 + #{null >= obs}) / (B + 1), p_dn = (1 + #{null <= obs}) / (B + 1)."""
    obs = np.asarray(obs)
    null = np.asarray(null)
    B = null.shape[0]
    o = obs[..., None, :]  # (..., 1, K)
    mean, sd = null.mean(0), null.std(0, ddof=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        z = np.where(sd > 0, (obs - mean) / np.where(sd > 0, sd, 1), np.nan)
    return {
        "mean": np.broadcast_to(mean, obs.shape).copy(),
        "sd": np.broadcast_to(sd, obs.shape).copy(),
        "z": z,
        "p_gt": (o > null).mean(axis=-2),
        "p_lt": (o < null).mean(axis=-2),
        "p_up": (1 + (null >= o).sum(axis=-2)) / (B + 1),
        "p_dn": (1 + (null <= o).sum(axis=-2)) / (B + 1),
    }


def dk_flag(p_gt: float, alpha: float = 0.05) -> str:
    """D&K's reading of p(obs > random) [L4486]: 'more' above 1 - alpha, 'fewer' below alpha."""
    return "more" if p_gt > 1 - alpha else "fewer" if p_gt < alpha else "n.s."


def side(obs, mean, p_up, p_dn, alpha: float = 0.05):
    """'over' / 'under' / '-' per element, from the tie-inclusive exact Monte-Carlo p-values (used for
    the sparse triangle counts, where D&K's strict-inequality rule would call a tied zero 'fewer')."""
    obs, mean, p_up, p_dn = (np.asarray(x) for x in (obs, mean, p_up, p_dn))
    return np.where((p_up <= alpha) & (obs > mean), "over", np.where((p_dn <= alpha) & (obs < mean), "under", "-"))


def dk_pattern(p_gt: np.ndarray, hi: float = 0.95, lo: float = 0.05) -> dict[str, bool]:
    """D&K's text-stated Figure 1 claims about p(obs > random) by wave [L4490-L4498], checked on an
    array (15, 8) in TRIPLE_TYPES order.  Only claims the authors state in words are included; values
    read off the plotted figure are not [L4506, L4526, L4528, L4530 are the [fig] lines]."""
    T = {t: np.asarray(p_gt)[:, i] for i, t in enumerate(TRIPLE_TYPES)}
    six_on = np.asarray(p_gt)[5:]
    return {
        "LLL above the null in all 15 waves [L4490]": bool((T["LLL"] > hi).all()),
        "LDD above the null from wave 2 [L4491]": bool((T["LDD"][1:] > hi).all()),
        "LDL below the null in all 15 waves [L4492]": bool((T["LDL"] < lo).all()),
        "LLD below the null in all 15 waves, significant at the outset [L4493]": bool((T["LLD"] < lo).all()),
        "DLL not significant at wave 1 [L4494]": bool(lo <= T["DLL"][0] <= hi),
        "DLL above the null in every wave from 6 on [L4494]": bool((T["DLL"][5:] > hi).all()),
        "DDD above the null from wave 5 on [L4495]": bool((T["DDD"][4:] > hi).all()),
        "DLD below the null from wave 5 on [L4496]": bool((T["DLD"][4:] < lo).all()),
        "DDL below the null at wave 1 and from wave 5 on [L4497]": bool(T["DDL"][0] < lo and (T["DDL"][4:] < lo).all()),
        "from wave 6 every type is on one side of its null [L4498]": bool(((six_on > hi) | (six_on < lo)).all()),
    }


# ------------------------------------------------------------------ transitions

def level_codes(S: np.ndarray, level: Level, rule: str | None = None) -> np.ndarray:
    """Per-wave type codes of every triple of `level`: (15, 4080) or (15, 680)."""
    if level is TRIPLE_LEVEL:
        return triple_codes(S)
    return triangle_codes(symmetrise(S, rule or "agree"))


def observed_transitions(S: np.ndarray, level: Level, rule: str | None = None) -> np.ndarray:
    """(14, K, K) counts of triples going from type a at wave w to type b at wave w + 1."""
    codes = level_codes(S, level, rule)
    return np.stack([transition_counts(codes[t], codes[t + 1], level.k) for t in range(codes.shape[0] - 1)])


def null_transitions(
    S: np.ndarray,
    level: Level,
    rule: str | None,
    kind: str,
    n_draws: int,
    rng: np.random.Generator,
    recode_cut: tuple[int, int] = (4, 3),
    chunk: int = 1000,
) -> np.ndarray:
    """(14, B, K, K) null transition counts.  kind = 'cond' (start kept, next wave's changes
    re-placed within strata of start sign) or 'indep' (both waves re-shuffled independently, with
    the recode's row composition).  Draws are independent across transitions."""
    T = S.shape[0] - 1
    k = level.k
    out = np.empty((T, n_draws, k, k), dtype=np.int32)
    if level is TRIANGLE_LEVEL:
        s_all = symmetrise(S, rule or "agree")
    for t in range(T):
        done = 0
        while done < n_draws:
            b = min(chunk, n_draws - done)
            if kind == "cond":
                if level is TRIPLE_LEVEL:
                    start = triple_codes(S[t])
                    end = triple_codes(null_next_within_rows(rng, S[t], S[t + 1], b))
                else:
                    start = triangle_codes(s_all[t])
                    end = triangle_codes_from_dyads(null_next_within_dyads(rng, s_all[t], s_all[t + 1], b))
                out[t, done:done + b] = transition_counts(start, end, k)
            elif kind == "indep":
                S0 = null_signs(rng, b, *recode_cut)
                S1 = null_signs(rng, b, *recode_cut)
                if level is TRIPLE_LEVEL:
                    c0, c1 = triple_codes(S0), triple_codes(S1)
                else:
                    c0 = triangle_codes(symmetrise(S0, rule or "agree"))
                    c1 = triangle_codes(symmetrise(S1, rule or "agree"))
                out[t, done:done + b] = transition_counts(c0, c1, k)
            else:
                raise ValueError(f"unknown null kind {kind!r}")
            done += b
    return out


def window_transitions(spec: str) -> list[int]:
    """0-based transition indices (transition t is wave t+1 -> t+2): 'all', 'early' (first 5),
    'late' (the other 9), 'nogap' (all but the two-week gap 9 -> 10)."""
    allt = list(range(N_TRANSITIONS))
    if spec == "all":
        return allt
    if spec == "early":
        return allt[:5]
    if spec == "late":
        return allt[5:]
    if spec == "nogap":
        return [t for t in allt if t != GAP_TRANSITION - 1]
    raise ValueError(spec)


def _tail_p(null_vals: np.ndarray, obs: float) -> tuple[float, float]:
    """Add-one exact Monte-Carlo tail p-values (P(null >= obs), P(null <= obs)); nan if undefined."""
    ok = null_vals[~np.isnan(null_vals)]
    if not ok.size or np.isnan(obs):
        return float("nan"), float("nan")
    return float((1 + (ok >= obs - 1e-12).sum()) / (ok.size + 1)), float((1 + (ok <= obs + 1e-12).sum()) / (ok.size + 1))


def conversion_stats(Tobs: np.ndarray, Tnull: np.ndarray, level: Level, window: list[int]) -> dict:
    """Pooled conversion statistics over the window's transitions.

    For each start class (one_neg, all_neg) and each target set the observed count and rate, the
    null mean rate, and one-sided permutation p-values p_up = P(null >= obs), p_dn = P(null <= obs)
    (add-one correction) and the two-sided p_two = min(1, 2 min(p_up, p_dn)).  Target sets:
      strict  - complete strict-balanced types (Heider: even number of negatives)        [L4482]
      weak    - complete weak-balanced types (strict + all-negative; Davis)              [L4483]
      inc     - incomplete: a tie fell to 0 (v0 section 4.2 calls this vacuously balanced)
      relief  - strict + inc: balanced either by a sign change or by losing a tie
                (ADDED AFTER the first transition matrices were seen; it is v0's own convention)
    `diff[t]` is r(one_neg) - r(all_neg) for t in (strict, relief): the v0 section 7 claim is that
    the one-negative class converts FASTER; it is compared with the same difference computed on each
    null draw (the null difference is not zero because the classes have different routes).  When the
    null keeps the start wave ('cond') the denominators are fixed; for 'indep' they vary by draw and
    the rates are per-draw ratios over the draws with a nonzero denominator."""
    O = Tobs[window].sum(axis=0)  # (K, K)
    Nn = Tnull[window].sum(axis=0).astype(np.int64)  # (B, K, K)
    res: dict = {"obs_matrix": O, "null_mean_matrix": Nn.mean(0), "B": Nn.shape[0], "classes": {}}
    classes = {"one_neg": level.one_neg, "all_neg": level.all_neg}
    targets = {
        "strict": level.strict_bal,
        "weak": level.weak_bal,
        "inc": (level.inc,),
        "relief": tuple(level.strict_bal) + (level.inc,),
    }
    rates_null: dict[tuple[str, str], np.ndarray] = {}
    for cname, crows in classes.items():
        rows = list(crows)
        d_obs = int(O[rows].sum())
        d_null = Nn[:, rows].sum(axis=(1, 2))
        valid = d_null > 0
        entry: dict = {"start_obs": d_obs, "start_null_mean": float(d_null.mean())}
        for tname, tcols in targets.items():
            cols = list(tcols)
            num_obs = int(O[np.ix_(rows, cols)].sum())
            num_null = Nn[:, rows][:, :, cols].sum(axis=(1, 2))
            with np.errstate(invalid="ignore", divide="ignore"):
                rate_null = np.where(valid, num_null / np.where(valid, d_null, 1), np.nan)
            rates_null[(cname, tname)] = rate_null
            rate_obs = num_obs / d_obs if d_obs else float("nan")
            p_up, p_dn = _tail_p(rate_null, rate_obs)
            entry[tname] = {
                "num_obs": num_obs,
                "rate_obs": rate_obs,
                "num_null_mean": float(num_null.mean()),
                "rate_null_mean": float(np.nanmean(rate_null)) if valid.any() else float("nan"),
                "p_up": p_up,
                "p_dn": p_dn,
                "p_two": min(1.0, 2 * min(p_up, p_dn)) if not np.isnan(p_up) else float("nan"),
            }
        res["classes"][cname] = entry
    res["diff"] = {}
    for tname in ("strict", "relief"):
        d_obs = res["classes"]["one_neg"][tname]["rate_obs"] - res["classes"]["all_neg"][tname]["rate_obs"]
        d_null = rates_null[("one_neg", tname)] - rates_null[("all_neg", tname)]
        p_up, p_dn = _tail_p(d_null, d_obs)
        res["diff"][tname] = {
            "obs": d_obs,
            "null_mean": float(np.nanmean(d_null)) if np.any(~np.isnan(d_null)) else float("nan"),
            "p_up": p_up,
            "p_dn": p_dn,
        }
    return res


# ------------------------------------------------------------------ closed forms (used by the tests)

def expected_triple_counts(n_pos: int = 4, n_neg: int = 3) -> np.ndarray:
    """E[count of each ordered-triple type] under the row-wise shuffle, in closed form:
    n(n-1)(n-2) * [N_a/(n-1)] * [(N_c - [a=c])/(n-2)] * [N_b/(n-1)] for type (a, b, c): the first and
    third ties come from the same row i, the second from row j, and rows are independent."""
    Nl = {"L": n_pos, "D": n_neg}
    out = []
    for a, b, c in TRIPLE_TYPES:
        pi = Nl[a] / (N - 1) * (Nl[c] - (a == c)) / (N - 2)
        out.append(N * (N - 1) * (N - 2) * pi * Nl[b] / (N - 1))
    return np.array(out)


def expected_agree_triangle_counts(n_pos: int = 4, n_neg: int = 3) -> np.ndarray:
    """E[count of complete 'agree' triangles with 0..3 negative edges] under the row-wise shuffle:
    a triangle needs both directions of each pair to carry the edge sign, so row r supplies the two
    entries toward the other two vertices, with probability N_x/(n-1) * (N_y - [x=y])/(n-2)."""
    Nl = {1: n_pos, -1: n_neg}
    out = np.zeros(4)
    for e_ij, e_ik, e_jk in itertools.product((1, -1), repeat=3):
        p = 1.0
        for x, y in ((e_ij, e_ik), (e_ij, e_jk), (e_ik, e_jk)):  # rows i, j, k
            p *= Nl[x] / (N - 1) * (Nl[y] - (x == y)) / (N - 2)
        out[sum(e < 0 for e in (e_ij, e_ik, e_jk))] += p
    return out * len(VT_I)
