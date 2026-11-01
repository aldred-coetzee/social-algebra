"""The crowd gate on wiki-RfA, read as a 2003-2013 online setting: does a later vote complement or substitute
for the running crowd, and does participation follow a monotone cascade, ignite, or close at a decisive margin?

Prior work: models/00-v0.md section 4.4 (the crowd law r(t+1) = F[r(t)]; the two-sided gate
F = F_theta - F~_thetabar; the sign operand sigma on F), section 2.1/2.3, section 6 Theorem 6.3
(monotone cascade) and section 7 ("Crowd" test); models/02-our-claims.md Claim 1 (the group state is the
threshold distribution; the excess function E_F(r) = F(r) - r); docs/prior-work/112 section 6.5 (the sign-law
registry's five tests); docs/prior-work/117 section 3.3 (the wiki-RfA file).  Ledger ids (grep docs/ledger.jsonl):
Granovetter's map and its fixed point L1831 [read], monotone convergence L1201 [derived], cascade operator
L1235, non-identifiability by moments L1225; thresholds as the net result of costs and benefits L3959;
Kuran's utility and threshold function L3965, L3967, thresholds falling as the share rises T(S) L4395,
the external and internal payoffs L4392-L4394; Cantoni et al.'s complements-vs-substitutes evidence
L4353-L4355 and its scope L4363, the two mechanisms that supply an upper gate L4347 (own turnout "no longer
needed") and L4348 (crackdown probability rising with size); the wiki-RfA file L4561-L4564.  L1130 (a
randomised prior-rating experiment: positive prior ratings raised later positive ratings, negative ones
were corrected) is `sa`, abstract only: it is named in the results as a comparator and feeds nothing.

WHAT IS TESTED.  Each adminship election is a crowd event: signed public votes with minute-resolution
timestamps, 2003-2013, a medium (a wiki page that shows the running tally) in which every voter sees what
the crowd has done so far.  v0.1 (and v0.2.1, models/00-v0.md section 4.4) carries the sign of "more of the crowd
acting makes me more likely to act" as a setting operand sigma (Hong Kong march: substitutes, sigma = -1 at that margin, L4355; Granovetter
and Kuran: complements, sigma = +1); this module estimates sigma here.

 (1) SIGN-FOLLOWING.  For every non-neutral vote: the running support share s and the running turnout n of the
     votes strictly before it, then P(support | s, n, ...) controlling for the voter's own propensity (support rate
     in the voter's votes at OTHER (candidate, result, year) groups, shrunk), the candidate's outcome (the election's leave-one-out support
     share and its result), and the clock (hours since the first vote, position).  sigma > 0 (complements) if the
     coefficient on s exceeds its null, sigma < 0 (substitutes) if it falls below: a sign of CO-MOVEMENT, since the
     null cannot tell influence from a shared shock (below).  The null is the WITHIN-ELECTION
     SHUFFLE: the same votes (signs, voters, composition) reassigned at random to the election's own timestamps.
     The shuffle reproduces every mechanical artefact of the estimator (sampling without replacement, the
     leave-one-out bias, the controls) so that only order-dependence remains.  The same machinery is run on the
     SHARE OF THE LAST L VOTES (L = 5, 10, 20), on a time-reversal placebo (the next L votes), on agreement with the
     recent and the cumulative majority, by prior turnout, and on the minutes between consecutive votes.  Reported
     by year and by election size.  The time-reversal placebo turned out NOT to discriminate influence from a shared
     shock (a reversible process looks the same run backwards; tested on planted data), and is reported as
     time-symmetry only.
 (2) PARTICIPATION.  Cumulative curves per election; their shape against a clock-only null (votes redrawn from the
     pooled hour profile); the stall (no vote after hour t) by final support; late acceleration (ignition) by the
     running state; a discrete-time Poisson hazard of new votes with the running support share as state, tested with
     the same kind of shuffle (signs reassigned among the vote slots, times fixed: the null in which timing does not
     care about the sign HISTORY, composition kept).
 (3) VARIATIONS.  The sign dependence in eleven forms (cumulative share linear = Kuran's falling threshold, with
     curvature = convex bandwagon or concave gate, spline, windowed shares, vote margin, log-odds, majority step,
     share x turnout) and the participation hazard in six (clock only; turnout; turnout + recent rate; + share
     monotone; + share with curvature; + share bands), compared out of sample (election-level folds), the
     mechanical gain of each form (the same form fitted to shuffled elections) subtracted, because in-sample
     likelihood rewards flexibility and a flexible form also fits the nonlinear way composition enters.

TERMS AND DATA.  SNAP wiki-RfA (West, Paskov, Leskovec & Potts 2014, TACL 2: 297-310): no terms stated by
SNAP (117 section 3.3, L4561); the comments are Wikipedia text (CC BY-SA) and are NEVER parsed, stored or used
here (the parser discards every TXT line as it streams past), user names are replaced by integers on load and never
written out.
The data file is local-use-only and git-ignored (sim/data/README.md); computed statistics only go to
sim/results/.

WHAT THE DATA CAN AND CANNOT SAY (the report repeats it).  Observational order-dependence cannot separate
influence from a shared shock that arrives at one moment; the shuffle null tests exchangeability of order,
not causation.  A vote is a public, consequential, one-shot act on a wiki, not a riot; the candidate's
quality, the nominator's text and the page's own prompts are not observed; an election that stops early
(the file does not say why; closure of a decisive failure is the presumed reason) is an institutional gate on
top of the voluntary one.
"""
from __future__ import annotations

import os

for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):   # one BLAS thread per worker
    os.environ.setdefault(_v, "1")

import dataclasses
import datetime
import gzip
import hashlib
import multiprocessing as mp
import re
import urllib.request
from pathlib import Path
from typing import Callable, Iterable

import numpy as np

SIM_DIR = Path(__file__).resolve().parents[1]
DATA_FILE = SIM_DIR / "data" / "wiki-rfa" / "wiki-RfA.txt.gz"
SOURCE_URL = "https://snap.stanford.edu/data/wiki-RfA.txt.gz"
SIZE_BYTES = 14_936_383
SHA256 = "88d53196fb2564a2e20286dbba818832f718cc352bb181a2101d23d2556f0862"
FETCH_HINT = (f"fetch {SOURCE_URL} into sim/data/wiki-rfa/ (local use only, git-ignored; "
              f"{SIZE_BYTES:,} bytes, sha256 {SHA256}; sim/data/README.md)")

SEED = 20261101
GAP_DAYS = 10.0          # a new candidacy starts after a silence this long within one (candidate, result, year)
STRAY_MAX = 3            # a cluster of at most this many votes beside a big sibling is a stray timestamp
STRAY_SIBLING_MIN = 10
N_MIN = 20               # least non-neutral votes for an election to enter the sign analysis
M_MIN = 5                # least earlier non-neutral votes before a vote is a target of the sign analysis
KAPPA = 4.0              # prior strength (pseudo-votes) of the voter-propensity shrinkage
HOUR_EDGES = np.array([0.0, 1, 2, 4, 8, 16, 32, 64, 128, 1e9])   # clock controls: hours since the first vote
SIZE_EDGES = (20, 40, 80, 160, 10**9)                              # election size classes (non-neutral votes)
SIZE_LABELS = ("20-39", "40-79", "80-159", "160+")

_MONTH_NUM = {m[:3].lower(): i + 1 for i, m in enumerate(
    "January February March April May June July August September October November December".split())}
_MONTH_NUM["mya"] = 5            # a typo that occurs once
_DAT = re.compile(r"^(\d{1,2}):(\d{2}), (\d{1,2}) ([A-Za-z]+) (\d{4})$")
_EPOCH_ORD = datetime.date(2000, 1, 1).toordinal()


# =================================================================== data layer

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def fetch(dest: Path | str = DATA_FILE, url: str = SOURCE_URL, timeout: float = 300.0) -> Path:
    """Download the SNAP file for local use only.  Refuses (writes nothing) if the sha256 differs from the
    recorded one.  The sessions that wrote this module reused the copy already under sim/data/wiki-rfa/."""
    with urllib.request.urlopen(url, timeout=timeout) as resp:
        data = resp.read()
    if hashlib.sha256(data).hexdigest() != SHA256:
        raise ValueError(f"{url}: sha256 differs from the recorded {SHA256}; nothing written")
    dest = Path(dest)
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_name(dest.name + ".part")
    tmp.write_bytes(data)
    tmp.replace(dest)
    return dest


def parse_minute(s: str) -> float:
    """'19:53, 25 January 2013' -> minutes since 2000-01-01 00:00 (the printed wall clock; Wikipedia
    signatures are UTC).  NaN when the field is empty or not a date (9,367 empty; one hour of 31).  A month
    is matched on its first three letters, so 'Jun', 'Sept' and the slips 'Julu' and 'Janry' parse and 'Mya'
    is read as May."""
    m = _DAT.match(s.strip())
    if m is None:
        return float("nan")
    hh, mi, dd, mon, yy = m.groups()
    mm = _MONTH_NUM.get(mon[:3].lower())
    if mm is None or int(hh) > 23 or int(mi) > 59:
        return float("nan")
    try:
        day = datetime.date(int(yy), mm, int(dd)).toordinal() - _EPOCH_ORD
    except ValueError:
        return float("nan")
    return day * 1440.0 + int(hh) * 60 + int(mi)


@dataclasses.dataclass(frozen=True)
class Votes:
    """The raw file, one row per record, in file order.  Names are integers (-1 for the empty voter field)."""
    voter: np.ndarray    # int32
    cand: np.ndarray     # int32
    vote: np.ndarray     # int8: +1 support, -1 oppose, 0 neutral
    res: np.ndarray      # int8: +1 promoted, -1 not
    year: np.ndarray     # int16
    minute: np.ndarray   # float64, NaN if undated
    n_names: int         # voters and candidates share one numbering, so voter == cand is a self-vote

    @property
    def n(self) -> int:
        return len(self.vote)


def parse_lines(lines: Iterable[str]) -> Votes:
    """Parse the SNAP record format (SRC/TGT/VOT/RES/YEA/DAT/TXT, blank line between records).  The TXT field
    is skipped, never stored."""
    names: dict[str, int] = {}
    voter, cand, vote, res, year, minute = [], [], [], [], [], []
    cur: dict[str, str] = {}

    def flush() -> None:
        if not cur:
            return
        v = cur.get("SRC", "")
        voter.append(names.setdefault(v, len(names)) if v else -1)
        cand.append(names.setdefault(cur["TGT"], len(names)))
        vote.append(int(cur["VOT"]))
        res.append(int(cur["RES"]))
        year.append(int(cur["YEA"]))
        minute.append(parse_minute(cur.get("DAT", "")))
        cur.clear()

    for line in lines:
        line = line.rstrip("\n")
        if not line:
            flush()
            continue
        if line.startswith("TXT:"):
            continue
        k, _, v = line.partition(":")
        cur[k] = v
    flush()
    return Votes(np.array(voter, np.int32), np.array(cand, np.int32), np.array(vote, np.int8),
                 np.array(res, np.int8), np.array(year, np.int16), np.array(minute, np.float64),
                 len(names))


_CACHE: dict = {}


def load_votes(path: Path | str = DATA_FILE, verify: bool = True) -> Votes:
    """The wiki-RfA file as integer arrays.  `verify` checks the recorded size and sha256 of the local copy."""
    path = Path(path)
    key = (str(path), verify)
    if key in _CACHE:
        return _CACHE[key]
    if not path.exists():
        raise FileNotFoundError(f"{path} is missing: {FETCH_HINT}")
    if verify and path == DATA_FILE:
        if path.stat().st_size != SIZE_BYTES or sha256_of(path) != SHA256:
            raise ValueError(f"{path} does not match the recorded size/sha256 ({FETCH_HINT})")
    with gzip.open(path, "rt", encoding="utf-8", errors="replace") as fh:
        votes = parse_lines(fh)
    _CACHE[key] = votes
    return votes


@dataclasses.dataclass(frozen=True)
class Elections:
    """Dated, deduplicated, non-self votes sorted by (election, minute, file order), election-contiguous.

    An ELECTION is a cluster of one (candidate, result, year) group split at silences longer than
    `gap_days`; a cluster of at most STRAY_MAX votes next to a cluster of at least STRAY_SIBLING_MIN is a
    stray timestamp and is dropped.  A voter appearing twice in one election keeps the LAST vote (the final
    position, as the file records it).  Undated votes (9,367) and the empty voter field (1,661) are dropped.
    """
    cl: np.ndarray        # int32 election index per vote
    voter: np.ndarray     # int32
    vote: np.ndarray      # int8
    minute: np.ndarray    # float64
    fidx: np.ndarray      # int64 original file row
    start: np.ndarray     # int64 first row of each election
    size: np.ndarray      # int64 votes per election (incl. neutral)
    cand: np.ndarray      # int32 per election
    res: np.ndarray       # int8 per election
    year: np.ndarray      # int16 per election
    dropped: dict         # counts of what was dropped and why

    @property
    def n_elections(self) -> int:
        return len(self.size)

    def hours(self) -> np.ndarray:
        """Hours since the first vote of the vote's election."""
        return (self.minute - self.minute[self.start][self.cl]) / 60.0


def build_elections(v: Votes, gap_days: float = GAP_DAYS, stray_max: int = STRAY_MAX,
                    stray_sibling_min: int = STRAY_SIBLING_MIN) -> Elections:
    dropped = {"undated": int(np.isnan(v.minute).sum()), "empty_voter": int((v.voter < 0).sum()),
               "self_vote": 0, "stray": 0, "duplicate": 0}
    keep = ~np.isnan(v.minute) & (v.voter >= 0)
    selfv = keep & (v.voter == v.cand)
    dropped["self_vote"] = int(selfv.sum())
    keep &= ~selfv
    fidx = np.nonzero(keep)[0]
    key = (v.cand[fidx].astype(np.int64) * 3 + (v.res[fidx] + 1)) * 4096 + (v.year[fidx] - 2000)
    _, gid = np.unique(key, return_inverse=True)
    order = np.lexsort((fidx, v.minute[fidx], gid))
    fidx, gid = fidx[order], gid[order]
    minute = v.minute[fidx]
    new = np.ones(len(fidx), bool)
    new[1:] = (gid[1:] != gid[:-1]) | (np.diff(minute) > gap_days * 1440.0)
    cl = np.cumsum(new) - 1
    size = np.bincount(cl)
    # strays: a tiny cluster whose group also has a big one
    grp_of_cl = gid[np.nonzero(new)[0]]
    big_in_group = np.zeros(gid.max() + 1, bool)
    np.logical_or.at(big_in_group, grp_of_cl, size >= stray_sibling_min)
    stray_cl = (size <= stray_max) & big_in_group[grp_of_cl]
    ok = ~stray_cl[cl]
    dropped["stray"] = int((~ok).sum())
    fidx, gid, minute, cl = fidx[ok], gid[ok], minute[ok], cl[ok]
    # dedupe (election, voter): keep the last
    vkey = cl.astype(np.int64) * (v.n_names + 1) + v.voter[fidx]
    _, last_rev = np.unique(vkey[::-1], return_index=True)
    keep_idx = np.sort(len(vkey) - 1 - last_rev)
    dropped["duplicate"] = int(len(vkey) - len(keep_idx))
    fidx, gid, minute, cl = fidx[keep_idx], gid[keep_idx], minute[keep_idx], cl[keep_idx]
    _, cl = np.unique(cl, return_inverse=True)           # dense again
    size = np.bincount(cl)
    start = np.concatenate([[0], np.cumsum(size)[:-1]])
    return Elections(cl.astype(np.int32), v.voter[fidx], v.vote[fidx], minute, fidx, start, size,
                     v.cand[fidx][start], v.res[fidx][start], v.year[fidx][start], dropped)


# =================================================================== part 1: sign sequences

def _group_key(v: Votes, rows: np.ndarray) -> np.ndarray:
    """The (voter, candidate, result, year) group of each file row, as one int64."""
    return ((v.voter[rows].astype(np.int64) * v.n_names + v.cand[rows]) * 3 + (v.res[rows] + 1)) * 4096 + (v.year[rows] - 2000)


def _counted_votes(v: Votes) -> np.ndarray:
    """File rows that the voter history counts: the non-neutral, named, non-self votes, one per (voter,
    candidate, result, year) group (the last in FILE order), over the whole file (dated or not)."""
    m = (v.vote != 0) & (v.voter >= 0) & (v.voter != v.cand)
    idx = np.nonzero(m)[0]
    _, last_rev = np.unique(_group_key(v, idx)[::-1], return_index=True)
    return idx[np.sort(len(idx) - 1 - last_rev)]


def voter_history(v: Votes) -> tuple[np.ndarray, np.ndarray]:
    """Per voter: (V_i, S_i) = the number of that voter's non-neutral votes and how many were support, each
    (voter, candidate, result, year) group counted once (the last vote in file order), over the WHOLE file
    (dated or not).  Used leave-the-group-out: a vote's own propensity is (S_i - y_g + kappa*pi)/(V_i - 1 + kappa),
    y_g the support indicator of the vote the history COUNTED for the vote's group (build_sign_data)."""
    sel = _counted_votes(v)
    nv = np.bincount(v.voter[sel], minlength=v.n_names)
    ns = np.bincount(v.voter[sel], weights=(v.vote[sel] == 1).astype(float), minlength=v.n_names)
    return nv, ns


def counted_group_vote(v: Votes, rows: np.ndarray) -> np.ndarray:
    """For file rows of non-neutral votes: 1.0 if the vote the history counted for the row's (voter, candidate,
    result, year) group is a support, else 0.0.  It differs from the row's own sign when a voter changed his vote
    and the file lists the votes out of time order (the election keeps the last in TIME, the history the last in
    file order), or votes with different signs in two candidacies of one group: 182 of the 162,733 votes of the
    sign sample.  Subtracting the row's own sign there (the first version) left the counted vote in and took a
    vote out that was never counted (the voter's other support count could reach -1)."""
    sel = _counted_votes(v)
    gk = _group_key(v, sel)
    order = np.argsort(gk)
    gk, gy = gk[order], (v.vote[sel][order] == 1).astype(float)
    k = _group_key(v, rows)
    pos = np.searchsorted(gk, k)
    if np.any(pos >= len(gk)) or np.any(gk[np.minimum(pos, len(gk) - 1)] != k):
        raise ValueError("a row's (voter, candidate, result, year) group is not in the voter history")
    return gy[pos]


@dataclasses.dataclass(frozen=True)
class SignData:
    """Non-neutral votes of elections with at least `n_min` of them, election-contiguous and time-sorted.

    SLOT-attached arrays belong to a position in the election's timeline and stay put under a shuffle;
    VOTE-attached arrays (y, p, first, exp, voter) are what a shuffle moves between slots."""
    # slot-attached
    cl: np.ndarray          # dense election index per slot
    c0: np.ndarray          # global index of the election's first slot, per slot
    esz: np.ndarray         # election size (non-neutral votes), per slot
    minute: np.ndarray
    hours: np.ndarray       # since the election's first vote (any kind)
    tie_first: np.ndarray   # global index of the first slot with the same minute (strictly-earlier votes end here)
    tie_end: np.ndarray     # one past the last slot with the same minute (strictly-later votes start here)
    hbin: np.ndarray        # clock bin index
    year: np.ndarray        # per slot (election year)
    res: np.ndarray         # per slot, +1/-1
    # vote-attached
    y: np.ndarray           # 1.0 support, 0.0 oppose
    p: np.ndarray           # leave-this-group-out propensity (voter, candidate, result, year), shrunk
    first: np.ndarray       # 1.0 if the voter has no other vote in the file
    exp: np.ndarray         # log1p(number of the voter's other votes)
    voter: np.ndarray
    # election-level
    estart: np.ndarray
    esize: np.ndarray
    ekey: np.ndarray        # index into Elections for each election here
    eyear: np.ndarray
    eres: np.ndarray
    ek: np.ndarray          # supports per election

    @property
    def n(self) -> int:
        return len(self.y)

    @property
    def n_elections(self) -> int:
        return len(self.esize)


def build_sign_data(v: Votes, E: Elections, n_min: int = N_MIN, kappa: float = KAPPA) -> SignData:
    nv, ns = voter_history(v)
    pi = float(ns.sum() / nv.sum())
    nn = E.vote != 0
    cl_all = E.cl.astype(np.int64)
    n_nn = np.bincount(cl_all[nn], minlength=E.n_elections)
    elect = np.nonzero(n_nn >= n_min)[0]
    mask = nn & np.isin(cl_all, elect)
    idx = np.nonzero(mask)[0]                                     # still time-sorted and election-contiguous
    _, cl = np.unique(cl_all[idx], return_inverse=True)
    esize = np.bincount(cl)
    estart = np.concatenate([[0], np.cumsum(esize)[:-1]])
    c0 = estart[cl]
    esz = esize[cl]
    minute = E.minute[idx]
    hours_all = E.hours()                                         # since the election's first vote of any kind
    hours = hours_all[idx]
    n = len(idx)
    same_prev = np.zeros(n, bool)
    same_prev[1:] = (cl[1:] == cl[:-1]) & (minute[1:] == minute[:-1])
    run_start = np.maximum.accumulate(np.where(~same_prev, np.arange(n), 0))
    same_next = np.zeros(n, bool)
    same_next[:-1] = same_prev[1:]
    last_of_run = ~same_next
    run_end_pos = np.where(last_of_run, np.arange(n) + 1, n + 1)
    run_end = np.minimum.accumulate(run_end_pos[::-1])[::-1]
    y = (E.vote[idx] == 1).astype(float)
    vid = E.voter[idx]
    other_n = nv[vid] - 1.0
    other_s = ns[vid] - counted_group_vote(v, E.fidx[idx])        # leave out the vote the history counted
    p = (other_s + kappa * pi) / (other_n + kappa)
    ek = np.bincount(cl, weights=y).astype(float)
    ekey = elect
    return SignData(cl=cl, c0=c0, esz=esz, minute=minute, hours=hours, tie_first=run_start, tie_end=run_end,
                    hbin=np.digitize(hours, HOUR_EDGES) - 1, year=E.year[elect][cl], res=E.res[elect][cl],
                    y=y, p=p, first=(other_n <= 0).astype(float), exp=np.log1p(np.maximum(other_n, 0)), voter=vid,
                    estart=estart, esize=esize, ekey=ekey, eyear=E.year[elect], eres=E.res[elect], ek=ek)


def size_class(esize: np.ndarray) -> np.ndarray:
    return np.digitize(esize, SIZE_EDGES[1:-1])


def within_shuffle(rng: np.random.Generator, SD: SignData) -> np.ndarray:
    """A random assignment of each election's votes to that election's own slots (election blocks stay in
    place).  Returns `src`: slot j holds the vote that sits at index src[j] in the observed arrangement."""
    return np.lexsort((rng.random(SD.n), SD.cl))


@dataclasses.dataclass
class Arrangement:
    """Everything that depends on which vote sits in which slot."""
    y: np.ndarray
    p: np.ndarray
    first: np.ndarray
    exp: np.ndarray
    voter: np.ndarray
    n_prior: np.ndarray
    S_prior: np.ndarray
    n_post: np.ndarray
    S_post: np.ndarray
    cs: np.ndarray        # exclusive prefix sum of y over slots (length n+1)
    f_loo: np.ndarray


def arrange(SD: SignData, src: np.ndarray | None = None) -> Arrangement:
    if src is None:
        y, p, first, exp, voter = SD.y, SD.p, SD.first, SD.exp, SD.voter
    else:
        y, p, first, exp, voter = SD.y[src], SD.p[src], SD.first[src], SD.exp[src], SD.voter[src]
    cs = np.concatenate([[0.0], np.cumsum(y)])
    end = SD.c0 + SD.esz
    n_prior = (SD.tie_first - SD.c0).astype(float)
    S_prior = cs[SD.tie_first] - cs[SD.c0]
    n_post = (end - SD.tie_end).astype(float)
    S_post = cs[end] - cs[SD.tie_end]
    K = cs[end] - cs[SD.c0]
    f_loo = (K - y) / (SD.esz - 1.0)
    return Arrangement(y, p, first, exp, voter, n_prior, S_prior, n_post, S_post, cs, f_loo)


def windowed(SD: SignData, A: Arrangement, L: int) -> tuple[np.ndarray, np.ndarray]:
    """Support count and size of the last L votes strictly before the vote's minute."""
    lo = np.maximum(SD.tie_first - L, SD.c0)
    return A.cs[SD.tie_first] - A.cs[lo], (SD.tie_first - lo).astype(float)


def _logit(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return np.log(p / (1 - p))


SPLINE_KNOTS = (0.5, 0.75, 0.9)


def feature(SD: SignData, A: Arrangement, name: str) -> np.ndarray:
    """One named column, over all slots.  Running-state features use the votes strictly before the vote."""
    npr = np.maximum(A.n_prior, 1.0)
    if name == "s":
        return A.S_prior / npr
    if name == "s_post":
        return A.S_post / np.maximum(A.n_post, 1.0)
    if name == "s2":                                   # curvature of the share, centred on the usual pass line
        return (A.S_prior / npr - 0.75) ** 2
    if name.startswith("win"):
        S, m = windowed(SD, A, int(name[3:]))
        return S / np.maximum(m, 1.0)
    if name == "margin":                               # visible tally difference S - O, in tens of votes
        return (2 * A.S_prior - A.n_prior) / 10.0
    if name == "logodds":
        return np.log((A.S_prior + 0.5) / (A.n_prior - A.S_prior + 0.5))
    if name == "major":
        return np.sign(2 * A.S_prior - A.n_prior)
    if name.startswith("hinge"):                       # (s - knot)_+ with knot = 0.5 / 0.75 / 0.9
        k = float(name[5:])
        return np.maximum(A.S_prior / npr - k, 0.0)
    if name == "s_x_logn":
        return (A.S_prior / npr) * np.log1p(A.n_prior)
    if name == "f_loo":
        return A.f_loo
    if name == "res":
        return SD.res.astype(float)
    if name == "logit_p":
        return _logit(A.p)
    if name == "first":
        return A.first
    if name == "exp":
        return A.exp
    if name == "logn":
        return np.log1p(A.n_prior)
    if name == "logh":
        return np.log1p(SD.hours)
    if name == "pos":
        return A.n_prior / SD.esz
    if name == "pos2":
        return (A.n_prior / SD.esz) ** 2
    if name.startswith("hb"):
        return (SD.hbin == int(name[2:])).astype(float)
    if name.startswith("yr"):
        return (SD.year == int(name[2:])).astype(float)
    raise KeyError(name)


CLOCK = tuple(f"hb{i}" for i in range(1, len(HOUR_EDGES) - 1)) + ("pos", "pos2")
CONTROLS_X = ("f_loo", "res", "logit_p", "first", "exp", "logn") + CLOCK       # across-election logit
CONTROLS_FE = ("logit_p", "first", "exp", "logn") + CLOCK                     # within-election (election FE)


def columns(SD: SignData, A: Arrangement, names: Iterable[str], rows: np.ndarray) -> np.ndarray:
    return np.column_stack([feature(SD, A, nm)[rows] for nm in names])


def target_rows(SD: SignData, A: Arrangement, m_min: int = M_MIN, need_post: int = 0,
                election_mask: np.ndarray | None = None, min_hours: float = 0.0) -> np.ndarray:
    """Slots that are targets: at least m_min votes strictly before (and, for the placebo, need_post after),
    cast at least `min_hours` after the election's first vote."""
    ok = A.n_prior >= m_min
    if min_hours > 0:
        ok &= SD.hours >= min_hours
    if need_post:
        ok &= A.n_post >= need_post
    if election_mask is not None:
        ok &= election_mask[SD.cl]
    return np.nonzero(ok)[0]


# ------------------------------------------------------------------ estimators

@dataclasses.dataclass
class Fit:
    names: tuple
    beta: np.ndarray
    se: np.ndarray | None
    ll: float
    n: int
    mu: np.ndarray | None = None


def logit_irls(X: np.ndarray, y: np.ndarray, groups: np.ndarray | None = None, weights: np.ndarray | None = None,
               names: tuple = (), robust: bool = True, max_iter: int = 30, ridge: float = 1e-9) -> Fit:
    """Logistic regression by IRLS (Newton), optional case weights; cluster-robust (sandwich, G/(G-1)) standard
    errors by `groups`.  Not penalised beyond a 1e-9 ridge that only guards a singular design."""
    n, k = X.shape
    w0 = np.ones(n) if weights is None else weights
    beta = np.zeros(k)
    beta[0] = 0.0
    eta = np.zeros(n)
    ll_old = -np.inf
    for _ in range(max_iter):
        mu = 1.0 / (1.0 + np.exp(-np.clip(eta, -30, 30)))
        W = np.maximum(mu * (1 - mu), 1e-10) * w0
        z = eta + (y - mu) / np.maximum(mu * (1 - mu), 1e-10)
        XtW = X.T * W
        H = XtW @ X + ridge * np.eye(k)
        beta_new = np.linalg.solve(H, XtW @ z)
        eta = X @ beta_new
        step = np.max(np.abs(beta_new - beta))
        beta = beta_new
        if step < 1e-8:
            break
    mu = 1.0 / (1.0 + np.exp(-np.clip(eta, -30, 30)))
    ll = float(np.sum(w0 * (y * np.log(np.clip(mu, 1e-12, 1)) + (1 - y) * np.log(np.clip(1 - mu, 1e-12, 1)))))
    se = None
    if robust and groups is not None:
        W = np.maximum(mu * (1 - mu), 1e-10) * w0
        bread = np.linalg.inv((X.T * W) @ X + ridge * np.eye(k))
        score = X * ((y - mu) * w0)[:, None]
        G = int(groups.max()) + 1
        sg = np.zeros((G, k))
        np.add.at(sg, groups, score)
        meat = sg.T @ sg
        ng = len(np.unique(groups))
        se = np.sqrt(np.maximum(np.diag(bread @ meat @ bread) * ng / max(ng - 1, 1), 0.0))
    return Fit(tuple(names), beta, se, ll, n, mu)


def _demean(M: np.ndarray, g: np.ndarray, G: int) -> np.ndarray:
    cnt = np.bincount(g, minlength=G).astype(float)
    cnt[cnt == 0] = 1.0
    if M.ndim == 1:
        return M - (np.bincount(g, weights=M, minlength=G) / cnt)[g]
    out = np.empty_like(M)
    for j in range(M.shape[1]):
        out[:, j] = M[:, j] - (np.bincount(g, weights=M[:, j], minlength=G) / cnt)[g]
    return out


def lpm_fe(X: np.ndarray, y: np.ndarray, groups: np.ndarray, names: tuple = (), robust: bool = True,
           ridge: float = 1e-9) -> Fit:
    """Linear probability model with election fixed effects (within transformation, no constant in X).
    The coefficient is a probability change per unit of the column.  Cluster-robust by election."""
    G = int(groups.max()) + 1
    Xd = _demean(X, groups, G)
    yd = _demean(y.astype(float), groups, G)
    k = X.shape[1]
    XtX = Xd.T @ Xd + ridge * np.eye(k)
    beta = np.linalg.solve(XtX, Xd.T @ yd)
    res = yd - Xd @ beta
    se = None
    if robust:
        bread = np.linalg.inv(XtX)
        sg = np.zeros((G, k))
        np.add.at(sg, groups, Xd * res[:, None])
        ng = len(np.unique(groups))
        se = np.sqrt(np.maximum(np.diag(bread @ (sg.T @ sg) @ bread) * ng / max(ng - 1, 1), 0.0))
    return Fit(tuple(names), beta, se, float(-0.5 * np.sum(res ** 2)), len(y))


def ame(fit: Fit, col: int, X: np.ndarray, delta: float = 0.1) -> float:
    """Average marginal effect of `delta` on column `col` of a logit fit: mean of mu(1-mu) * beta * delta."""
    return float(np.mean(fit.mu * (1 - fit.mu)) * fit.beta[col] * delta)


# ------------------------------------------------------------------ the statistics and the shuffle null

PLACEBO_WINDOWS = (5, 10, 20)
TURNOUT_BINS = ((5, 10), (10, 20), (20, 40), (40, 80), (80, 10**9))


def cells_of(SD: SignData) -> dict[str, np.ndarray]:
    """Election masks: all, each year with data, each size class."""
    sc = size_class(SD.esize)
    cells = {"all": np.ones(SD.n_elections, bool)}
    for y in sorted(int(x) for x in np.unique(SD.eyear)):
        if y >= 2004:
            cells[f"y{y}"] = SD.eyear == y
    for k, lab in enumerate(SIZE_LABELS):
        cells[f"n{lab}"] = sc == k
    return cells


def _window_pair(SD: SignData, A: Arrangement, L: int) -> tuple[np.ndarray, np.ndarray]:
    """Share of the previous L votes and of the next L votes (strictly before / after the vote's minute)."""
    lo = np.maximum(SD.tie_first - L, SD.c0)
    prior = (A.cs[SD.tie_first] - A.cs[lo]) / np.maximum(SD.tie_first - lo, 1)
    hi = np.minimum(SD.tie_end + L, SD.c0 + SD.esz)
    post = (A.cs[hi] - A.cs[SD.tie_end]) / np.maximum(hi - SD.tie_end, 1)
    return prior, post


def _detrend(M: np.ndarray, g: np.ndarray, pos: np.ndarray, G: int, deg: int = 2) -> np.ndarray:
    """Residuals of each column of M after regressing, WITHIN each election, on 1, pos, ..., pos^deg."""
    one = M.ndim == 1
    M = M[:, None] if one else M
    P = np.column_stack([pos ** d for d in range(deg + 1)])
    k = P.shape[1]
    PP = np.zeros((G, k, k))
    for a in range(k):
        for b in range(a, k):
            w = np.bincount(g, weights=P[:, a] * P[:, b], minlength=G)
            PP[:, a, b] = w
            PP[:, b, a] = w
    PP += 1e-9 * np.eye(k)
    out = np.empty_like(M, dtype=float)
    for j in range(M.shape[1]):
        rhs = np.stack([np.bincount(g, weights=P[:, a] * M[:, j], minlength=G) for a in range(k)], axis=1)
        coef = np.linalg.solve(PP, rhs[:, :, None])[:, :, 0]
        out[:, j] = M[:, j] - np.einsum("ik,ik->i", P, coef[g])
    return out[:, 0] if one else out


def sign_stats(SD: SignData, src: np.ndarray | None, cells: dict[str, np.ndarray],
               windows: tuple = PLACEBO_WINDOWS, extras: bool = True, m_min: int = M_MIN,
               min_hours: float = 0.0) -> dict[str, float]:
    """Every statistic of the sign analysis for ONE arrangement of votes in slots (src=None: the observed one).

    logit_s / logit_ame10: coefficient on the running support share in a logit with the voter's propensity, the
        election's leave-one-out support share and result, turnout and the clock (hour bins, position); and the
        average marginal effect of +10 points of running share on P(support).
    fe_s: the same share in a linear probability model with election fixed effects (no f_loo / result: the
        fixed effect is the candidate's whole outcome).
    agree: P(the vote has the sign of the running majority), over votes with a strict majority before them.
    Placebo (cell 'all'): the previous-L-votes share against the next-L-votes share, same construction.
    Extras (cell 'all'): fe_q (fe_s after removing an election-specific quadratic trend in position), fev_s (voter
        fixed effects in place of the propensity, composition controls kept), logit_s_w (election-equal weights),
        and the coefficients by prior-turnout bin."""
    A = arrange(SD, src)
    out: dict[str, float] = {}
    fl = ("s",) + CONTROLS_X
    ff = ("s",) + CONTROLS_FE
    for name, mask in cells.items():
        rows = target_rows(SD, A, m_min=m_min, election_mask=mask, min_hours=min_hours)
        if len(rows) < 400:
            for k in ("logit_s", "logit_ame10", "fe_s", "agree"):
                out[f"{name}:{k}"] = np.nan
            continue
        X = np.column_stack([np.ones(len(rows)), columns(SD, A, fl, rows)])
        f = logit_irls(X, A.y[rows], robust=False)
        out[f"{name}:logit_s"] = float(f.beta[1])
        out[f"{name}:logit_ame10"] = ame(f, 1, X)
        Xf = columns(SD, A, ff, rows)
        out[f"{name}:fe_s"] = float(lpm_fe(Xf, A.y[rows], SD.cl[rows], robust=False).beta[0])
        n, S = A.n_prior[rows], A.S_prior[rows]
        dec = 2 * S != n
        out[f"{name}:agree"] = float(np.mean((A.y[rows][dec] == 1) == (2 * S[dec] > n[dec])))
    for L in windows:
        rows = target_rows(SD, A, m_min=L, need_post=L)
        wp, wq = _window_pair(SD, A, L)
        base = columns(SD, A, ("f_loo", "res", "logit_p", "first", "exp", "logn") + CLOCK, rows)
        f = logit_irls(np.column_stack([np.ones(len(rows)), wp[rows], wq[rows], base]), A.y[rows], robust=False)
        out[f"placebo:L{L}:logit_prior"], out[f"placebo:L{L}:logit_post"] = float(f.beta[1]), float(f.beta[2])
        ctrl = columns(SD, A, CONTROLS_FE, rows)
        g = lpm_fe(np.column_stack([wp[rows], wq[rows], ctrl]), A.y[rows], SD.cl[rows], robust=False)
        out[f"placebo:L{L}:fe_prior"], out[f"placebo:L{L}:fe_post"] = float(g.beta[0]), float(g.beta[1])
    if extras:
        rows = target_rows(SD, A, m_min=m_min, min_hours=min_hours)
        pos = A.n_prior[rows] / SD.esz[rows]
        yq = _detrend(A.y[rows], SD.cl[rows], pos, SD.n_elections)
        Xq = _detrend(columns(SD, A, ("s",) + CONTROLS_FE[:4], rows), SD.cl[rows], pos, SD.n_elections)
        out["all:fe_q"] = float(np.linalg.lstsq(Xq, yq, rcond=None)[0][0])
        X = np.column_stack([np.ones(len(rows)), columns(SD, A, fl, rows)])
        w = 1.0 / SD.esz[rows]
        out["all:logit_s_w"] = float(logit_irls(X, A.y[rows], weights=w * len(rows) / w.sum(), robust=False).beta[1])
        v_dense = np.unique(A.voter[rows], return_inverse=True)[1]
        keepv = ("s", "f_loo", "res", "logn") + CLOCK          # voter fixed effects in place of the propensity
        out["all:fev_s"] = float(lpm_fe(columns(SD, A, keepv, rows), A.y[rows], v_dense, robust=False).beta[0])
        nprior = A.n_prior[rows]
        for lo, hi in TURNOUT_BINS:
            m = (nprior >= lo) & (nprior < hi)
            r2 = rows[m]
            X2 = np.column_stack([np.ones(len(r2)), columns(SD, A, fl, r2)])
            out[f"turnout{lo}-{hi}:logit_s"] = float(logit_irls(X2, A.y[r2], robust=False).beta[1])
            out[f"turnout{lo}-{hi}:fe_q"] = float(np.linalg.lstsq(Xq[m], yq[m], rcond=None)[0][0])
    return out


_WORK: dict = {}


def _null_chunk(args):
    seed, b0, b1 = args
    SD, cells, kw = _WORK["SD"], _WORK["cells"], _WORK["kw"]
    rows = []
    for b in range(b0, b1):
        rng = np.random.default_rng(np.random.SeedSequence([seed, b]))
        rows.append(sign_stats(SD, within_shuffle(rng, SD), cells, **kw))
    return rows


def sign_null(SD: SignData, cells: dict[str, np.ndarray], B: int = 1000, seed: int = SEED, n_jobs: int = 8,
              **kw) -> tuple[list[str], np.ndarray]:
    """B within-election shuffles, each reproducing the full statistic vector.  Draw b is seeded by
    (seed, b) alone, so the result does not depend on n_jobs."""
    _WORK.update(SD=SD, cells=cells, kw=kw)
    chunks = [(seed, b0, min(b0 + 8, B)) for b0 in range(0, B, 8)]
    if n_jobs > 1:
        with mp.get_context("fork").Pool(n_jobs) as pool:
            parts = pool.map(_null_chunk, chunks)
    else:
        parts = [_null_chunk(c) for c in chunks]
    recs = [r for part in parts for r in part]
    keys = list(recs[0].keys())
    return keys, np.array([[r[k] for k in keys] for r in recs])


def compare_to_null(obs: float, null: np.ndarray) -> dict:
    """Observed against its null draws: centred two-sided p, and the one-sided p in each direction
    (+1 correction), plus z against the null's sd."""
    null = null[~np.isnan(null)]
    if len(null) < 2 or np.isnan(obs):
        nan = float("nan")
        return {"obs": float(obs), "null_mean": nan, "null_sd": nan, "z": nan, "p_two": nan, "p_up": nan,
                "p_down": nan, "B": len(null)}
    m, sd = float(null.mean()), float(null.std(ddof=1))
    B = len(null)
    return {"obs": float(obs), "null_mean": m, "null_sd": sd, "z": (obs - m) / sd if sd > 0 else float("nan"),
            "p_two": (1 + int(np.sum(np.abs(null - m) >= abs(obs - m)))) / (B + 1),
            "p_up": (1 + int(np.sum(null >= obs))) / (B + 1), "p_down": (1 + int(np.sum(null <= obs))) / (B + 1), "B": B}


def sign_fit_table(SD: SignData, cells: dict[str, np.ndarray]) -> dict[str, dict]:
    """Observed fits with cluster-robust standard errors, per cell: the logit (coefficient, SE, AME of +10
    points) and the election-FE linear model (coefficient, SE), with counts."""
    A = arrange(SD)
    out = {}
    fl = ("s",) + CONTROLS_X
    ff = ("s",) + CONTROLS_FE
    for name, mask in cells.items():
        rows = target_rows(SD, A, election_mask=mask)
        if len(rows) < 400:
            continue
        g = SD.cl[rows]
        X = np.column_stack([np.ones(len(rows)), columns(SD, A, fl, rows)])
        f = logit_irls(X, A.y[rows], groups=g, names=("const",) + fl)
        Xf = columns(SD, A, ff, rows)
        h = lpm_fe(Xf, A.y[rows], g, names=ff)
        m_ame = float(np.mean(f.mu * (1 - f.mu)))
        out[name] = {"n_votes": int(len(rows)), "n_elections": int(len(np.unique(g))),
                     "support_rate": float(A.y[rows].mean()),
                     "logit_s": float(f.beta[1]), "logit_se": float(f.se[1]),
                     "ame10": m_ame * f.beta[1] * 0.1, "ame10_se": m_ame * f.se[1] * 0.1,
                     "fe_s": float(h.beta[0]), "fe_se": float(h.se[0])}
    return out


def ladder_stats(SD: SignData, src: np.ndarray | None) -> dict[str, float]:
    """The coefficient on the running share as controls are added: clock only; + voter propensity; + the
    candidate's outcome (leave-one-out share and result); both (the primary specification)."""
    A = arrange(SD, src)
    rows = target_rows(SD, A)
    out = {}
    sets = {"clock": CLOCK + ("logn",), "propensity": ("logit_p", "first", "exp", "logn") + CLOCK,
            "outcome": ("f_loo", "res", "logn") + CLOCK, "both": CONTROLS_X}
    for name, ctrl in sets.items():
        X = np.column_stack([np.ones(len(rows)), columns(SD, A, ("s",) + tuple(ctrl), rows)])
        out[name] = float(logit_irls(X, A.y[rows], robust=False).beta[1])
    return out


LOCAL_L = 10


def local_stats(SD: SignData, src: np.ndarray | None, cells: dict[str, np.ndarray], L: int = LOCAL_L,
                robust: bool = False, min_hours: float = 0.0) -> dict[str, float]:
    """The LOCAL dependence by cell: logit coefficients on the share of the previous L votes and of the next L
    votes, entered together, with the primary controls (composition, propensity, turnout, clock)."""
    A = arrange(SD, src)
    wp, wq = _window_pair(SD, A, L)
    out = {}
    for name, mask in cells.items():
        rows = target_rows(SD, A, m_min=L, need_post=L, election_mask=mask, min_hours=min_hours)
        if len(rows) < 400:
            out.update({f"{name}:prior": float("nan"), f"{name}:post": float("nan")})
            continue
        base = columns(SD, A, ("f_loo", "res", "logit_p", "first", "exp", "logn") + CLOCK, rows)
        X = np.column_stack([np.ones(len(rows)), wp[rows], wq[rows], base])
        f = logit_irls(X, A.y[rows], groups=SD.cl[rows] if robust else None, robust=robust)
        out[f"{name}:prior"], out[f"{name}:post"] = float(f.beta[1]), float(f.beta[2])
        if robust:
            out[f"{name}:prior_se"], out[f"{name}:post_se"] = float(f.se[1]), float(f.se[2])
            out[f"{name}:n"] = float(len(rows))
    return out


LATE_HOURS = (0.0, 1.0, 6.0, 24.0)


def compute_local_after(SD: SignData, B: int = 100, seed: int = SEED, n_jobs: int = 8) -> dict:
    """The local dependence when the opening hours are not targets (they stay in the windows as context): is it
    the nominators' opening wave?"""
    allc = {"all": np.ones(SD.n_elections, bool)}
    out = {}
    for h in LATE_HOURS:
        obs = local_stats(SD, None, allc, min_hours=h)
        null = pmap([(lambda b=b: local_stats(SD, within_shuffle(np.random.default_rng(np.random.SeedSequence([seed, 29, b])), SD), allc, min_hours=h))
                     for b in range(B)], n_jobs)
        out[h] = {k: compare_to_null(obs[k], np.array([d[k] for d in null])) for k in obs}
        out[h]["n"] = int(len(target_rows(SD, arrange(SD), m_min=LOCAL_L, need_post=LOCAL_L, min_hours=h)))
    return out


def compute_local(SD: SignData, cells: dict[str, np.ndarray], B: int = 200, seed: int = SEED, n_jobs: int = 8) -> dict:
    obs = local_stats(SD, None, cells, robust=True)
    null = pmap([(lambda b=b: local_stats(SD, within_shuffle(np.random.default_rng(np.random.SeedSequence([seed, 19, b])), SD), cells))
                 for b in range(B)], n_jobs)
    cmp = {k: compare_to_null(obs[k], np.array([d[k] for d in null])) for k in obs if not (k.endswith("_se") or k.endswith(":n"))}
    return {"obs": obs, "cmp": cmp, "B": B}


def asym_stats(SD: SignData, src: np.ndarray | None, L: int = LOCAL_L) -> dict[str, float]:
    """Slopes of the logit in the share of the previous L votes below and above one half (a hinge at 0.5), the
    comparator for an asymmetric-herding pattern (positive prior ratings raised later positive ones, negative
    ones were 'corrected': L1130, `sa`, abstract only, a comparator and nothing more)."""
    A = arrange(SD, src)
    wp, _ = _window_pair(SD, A, L)
    rows = target_rows(SD, A, m_min=L)
    base = columns(SD, A, ("f_loo", "res", "logit_p", "first", "exp", "logn") + CLOCK, rows)
    w = wp[rows]
    X = np.column_stack([np.ones(len(rows)), w, np.maximum(w - 0.5, 0.0), base])
    b = logit_irls(X, A.y[rows], robust=False).beta
    # 'diff' = above - below (the hinge coefficient): the asymmetry itself, tested against its own null
    return {"below": float(b[1]), "above": float(b[1] + b[2]), "diff": float(b[2])}


def compute_asym(SD: SignData, B: int = 200, seed: int = SEED, n_jobs: int = 8) -> dict:
    obs = asym_stats(SD, None)
    null = pmap([(lambda b=b: asym_stats(SD, within_shuffle(np.random.default_rng(np.random.SeedSequence([seed, 23, b])), SD)))
                 for b in range(B)], n_jobs)
    return {k: compare_to_null(obs[k], np.array([d[k] for d in null])) for k in obs}


MAJORITY_WINDOWS = (5, 10, 20)


FAST_MINUTES = 20.0


def _gap_prev(SD: SignData) -> np.ndarray:
    """Minutes since the previous vote of the same election (1e9 for an election's first vote)."""
    g = np.full(SD.n, 1e9)
    same = SD.cl[1:] == SD.cl[:-1]
    g[1:][same] = SD.minute[1:][same] - SD.minute[:-1][same]
    return g


def majority_stats(SD: SignData, src: np.ndarray | None, cells: dict[str, np.ndarray]) -> dict[str, float]:
    """Does a vote have the sign of the majority before it?  Share of votes (with a strict majority) whose sign
    matches the majority of ALL earlier votes, and of the LAST 5, 10 and 20 earlier votes; on the targets of the
    primary analysis (at least M_MIN earlier votes).  For cell 'all' also split by pace: the previous vote at most
    FAST_MINUTES before ('_fast') or longer ago ('_slow')."""
    A = arrange(SD, src)
    gp = _gap_prev(SD)
    out = {}
    for name, mask in cells.items():
        rows_all = target_rows(SD, A, m_min=M_MIN, election_mask=mask)
        sets = {"": rows_all}
        if name == "all":
            sets["_fast"] = rows_all[gp[rows_all] <= FAST_MINUTES]
            sets["_slow"] = rows_all[gp[rows_all] > FAST_MINUTES]
        for suffix, rows in sets.items():
            y = A.y[rows] == 1
            n, S = A.n_prior[rows], A.S_prior[rows]
            dec = 2 * S != n
            out[f"{name}:cum{suffix}"] = float(np.mean(y[dec] == (2 * S[dec] > n[dec]))) if dec.any() else float("nan")
            for L in MAJORITY_WINDOWS:
                Sw, m = windowed(SD, A, L)
                Sw, m = Sw[rows], m[rows]
                dec = 2 * Sw != m
                out[f"{name}:w{L}{suffix}"] = float(np.mean(y[dec] == (2 * Sw[dec] > m[dec]))) if dec.any() else float("nan")
    return out


def compute_majority(SD: SignData, cells: dict[str, np.ndarray], B: int = 400, seed: int = SEED, n_jobs: int = 8) -> dict:
    obs = majority_stats(SD, None, cells)
    null = pmap([(lambda b=b: majority_stats(SD, within_shuffle(np.random.default_rng(np.random.SeedSequence([seed, 17, b])), SD), cells))
                 for b in range(B)], n_jobs)
    return {k: compare_to_null(obs[k], np.array([d[k] for d in null])) for k in obs}


GAP_EDGES = np.array([1.0, 2.0, 6.0, 21.0, 61.0, 241.0, 1001.0, 1e12])
GAP_LABELS = ("1", "2-5", "6-20", "21-60", "61-240", "241-1000", ">1000")


def gap_profile(SD: SignData, src: np.ndarray | None = None) -> dict[str, float]:
    """Do votes agree with the vote just before them, as a function of the minutes between them?

    For consecutive votes of one election (slot j, j+1) at least one minute apart: the share with the same sign,
    by gap.  For votes cast in the SAME minute the order in the file is the page's section order (supports are
    listed before opposes), not the order of casting, so that bin is computed without using order: the share of
    agreeing pairs among all pairs of votes in one minute.  Votes in one minute cannot have read each other
    through the saved page; a pull toward the earlier vote needs a gap, a shared shock does not."""
    A = arrange(SD, src)
    y = A.y
    same = SD.cl[1:] == SD.cl[:-1]
    gap = SD.minute[1:] - SD.minute[:-1]
    agree = (y[1:] == y[:-1]).astype(float)
    b = np.digitize(gap, GAP_EDGES) - 1
    out = {}
    for i, lab in enumerate(GAP_LABELS):
        m = same & (gap >= 1) & (b == i)
        out[f"gap{lab}"] = float(agree[m].mean()) if m.any() else float("nan")
    first = np.nonzero(np.arange(SD.n) == SD.tie_first)[0]
    last = SD.tie_end[first]
    multi = (last - first) >= 2
    a = A.cs[last[multi]] - A.cs[first[multi]]
    n = (last - first)[multi].astype(float)
    pairs = n * (n - 1) / 2
    out["same_minute"] = float((a * (a - 1) / 2 + (n - a) * (n - a - 1) / 2).sum() / pairs.sum())
    return out


def gap_counts(SD: SignData) -> dict[str, int]:
    same = SD.cl[1:] == SD.cl[:-1]
    gap = SD.minute[1:] - SD.minute[:-1]
    b = np.digitize(gap, GAP_EDGES) - 1
    out = {f"gap{lab}": int(np.sum(same & (gap >= 1) & (b == i))) for i, lab in enumerate(GAP_LABELS)}
    first = np.nonzero(np.arange(SD.n) == SD.tie_first)[0]
    n = (SD.tie_end[first] - first)
    out["same_minute"] = int((n * (n - 1) // 2).sum())
    return out


def compute_gap(SD: SignData, B: int = 400, seed: int = SEED, n_jobs: int = 8) -> dict:
    obs = gap_profile(SD)
    null = pmap([(lambda b=b: gap_profile(SD, within_shuffle(np.random.default_rng(np.random.SeedSequence([seed, 13, b])), SD)))
                 for b in range(B)], n_jobs)
    return {"counts": gap_counts(SD), "cmp": {k: compare_to_null(obs[k], np.array([d[k] for d in null])) for k in obs}}


_TASKS: list = []


def _run_task(i):
    return _TASKS[i]()


def pmap(thunks: list, n_jobs: int = 8) -> list:
    """Run zero-argument callables, in order, on a fork pool (state is shared copy-on-write, nothing is pickled
    but the results)."""
    global _TASKS
    _TASKS = list(thunks)
    if n_jobs <= 1 or len(_TASKS) == 1:
        return [t() for t in _TASKS]
    with mp.get_context("fork").Pool(min(n_jobs, len(_TASKS))) as pool:
        return pool.map(_run_task, range(len(_TASKS)), chunksize=1)


# =================================================================== part 2: participation

CHECK_HOURS = (1, 3, 6, 12, 24, 48, 72, 96, 120, 144, 156, 168)
BIN_EDGES = np.array([1, 2, 3, 4, 6, 9, 12, 18, 24, 36, 48, 72, 96, 120, 144, 156, 168], float)
EARLY_HI = 24.0                           # the 'voluntary' window: before almost any early closure
FINAL_EDGES = (0.4, 0.6, 0.75, 0.9)       # final-share classes: <.4, .4-.6, .6-.75, .75-.9, >=.9
FINAL_LABELS = ("<.40", ".40-.60", ".60-.75", ".75-.90", ">=.90")
STAGES = (("A", 1.0, 24.0), ("B", 24.0, 96.0), ("C", 96.0, 156.0), ("D", 156.0, 168.0))
N_MIN_PART = 20                           # least dated votes (any kind) for an election in the participation analysis


def final_class(share: np.ndarray) -> np.ndarray:
    return np.digitize(share, FINAL_EDGES)


@dataclasses.dataclass(frozen=True)
class HazardData:
    """Votes of every kind, election-contiguous and time-sorted, with the hourly bins of the first week.

    Bin b of election e covers hours [BIN_EDGES[b], BIN_EDGES[b+1]) since the election's first vote; the
    hour [0, 1) is the SEED (the nominators and the first voters) and is not modelled, only used as the
    election's scale n1.  `before[e, b]` is the global index of the first vote at or after the bin's start,
    so the votes strictly before it are the slots [estart[e], before[e, b])."""
    sign: np.ndarray            # per vote: +1 support, -1 oppose, 0 neutral
    hours: np.ndarray
    estart: np.ndarray
    esize: np.ndarray
    eyear: np.ndarray
    eres: np.ndarray
    before: np.ndarray          # (n_el, n_bins + 1)
    count: np.ndarray           # (n_el, n_bins) votes in the bin
    n1: np.ndarray              # votes in [0, 1) hour
    fshare: np.ndarray          # final support share of the non-neutral votes
    fclass: np.ndarray
    last_hour: np.ndarray
    nn_idx: np.ndarray          # global indices of the non-neutral votes
    nn_cl: np.ndarray           # their election index

    @property
    def n_elections(self) -> int:
        return len(self.esize)


def build_hazard_data(E: Elections, n_min: int = N_MIN_PART) -> HazardData:
    elect = np.nonzero(E.size >= n_min)[0]
    keep = np.isin(E.cl, elect)
    idx = np.nonzero(keep)[0]
    _, cl = np.unique(E.cl[idx], return_inverse=True)
    esize = np.bincount(cl)
    estart = np.concatenate([[0], np.cumsum(esize)[:-1]])
    hours = E.hours()[idx]
    sign = E.vote[idx].astype(np.int8)
    key = cl * 100000.0 + hours
    n_el = len(esize)
    edges = np.concatenate([[0.0], BIN_EDGES])
    q = (np.arange(n_el)[:, None] * 100000.0 + edges[None, :]).ravel()
    pos = np.searchsorted(key, q, side="left").reshape(n_el, len(edges))   # vote index at/after each edge
    n1 = pos[:, 1] - pos[:, 0]
    before = pos[:, 1:]                                                     # starts at hour 1
    count = np.diff(before, axis=1)
    S = np.bincount(cl, weights=(sign == 1).astype(float), minlength=n_el)
    O = np.bincount(cl, weights=(sign == -1).astype(float), minlength=n_el)
    fshare = S / np.maximum(S + O, 1)
    last_hour = hours[estart + esize - 1]
    nn = np.nonzero(sign != 0)[0]
    return HazardData(sign, hours, estart, esize, E.year[elect], E.res[elect], before, count, n1, fshare,
                      final_class(fshare), last_hour, nn, cl[nn])


def shuffle_signs(rng: np.random.Generator, HD: HazardData) -> np.ndarray:
    """Reassign the non-neutral signs among the non-neutral slots of each election (neutral slots stay)."""
    order = np.lexsort((rng.random(len(HD.nn_idx)), HD.nn_cl))
    out = HD.sign.copy()
    out[HD.nn_idx] = HD.sign[HD.nn_idx[order]]
    return out


def hazard_states(HD: HazardData, sign: np.ndarray) -> dict[str, np.ndarray]:
    """Per (election, bin): turnout so far n, support S and oppose O so far, strictly before the bin starts."""
    cs = np.concatenate([[0.0], np.cumsum(sign == 1)])
    co = np.concatenate([[0.0], np.cumsum(sign == -1)])
    st = HD.estart[:, None]
    S = cs[HD.before[:, :-1]] - cs[st]
    O = co[HD.before[:, :-1]] - co[st]
    n = (HD.before[:, :-1] - st).astype(float)
    return {"n": n, "S": S, "O": O}


SHARE_BANDS = (0.5, 0.7, 0.85, 0.95)       # running-share bands: <.5, .5-.7, .7-.85, .85-.95, >=.95
SHARE_LABELS = ("<.50", ".50-.70", ".70-.85", ".85-.95", ">=.95")
BAND_BASE = 2                              # contested-passing band is the reference


def _hazard_columns(HD: HazardData, sign: np.ndarray, spec: str, b_lo: int, b_hi: int) -> tuple:
    """Design for bins b_lo..b_hi-1.  Returns X, y, offset, group, names.  `spec` is a '+'-joined list of
    state terms: turn, s, s2, bands, (empty string: clock only)."""
    n_el = HD.n_elections
    nb = b_hi - b_lo
    st = hazard_states(HD, sign)
    n, S, O = st["n"][:, b_lo:b_hi], st["S"][:, b_lo:b_hi], st["O"][:, b_lo:b_hi]
    nn = S + O
    few = nn < 5
    s = np.where(few, 0.75, S / np.maximum(nn, 1))
    cols, names = [], []
    onehot = np.zeros((n_el, nb, nb))
    onehot[:, np.arange(nb), np.arange(nb)] = 1.0
    for j in range(nb):
        cols.append(onehot[:, :, j])
        names.append(f"bin{b_lo + j}")
    for yv in range(2005, 2014):
        cols.append(np.repeat((HD.eyear == yv).astype(float)[:, None], nb, axis=1))
        names.append(f"yr{yv}")
    cols.append(np.repeat(np.log1p(HD.n1)[:, None], nb, axis=1))
    names.append("log_n1")
    for c in range(1, 5):
        cols.append(np.repeat((HD.fclass == c).astype(float)[:, None], nb, axis=1))
        names.append(f"final{c}")
    terms = [t for t in spec.split("+") if t]
    if any(t in ("s", "s2", "bands") for t in terms):
        cols.append(few.astype(float))
        names.append("few")
    for t in terms:
        if t == "turn":
            cols.append(np.log1p(n) - np.log1p(HD.n1)[:, None])
            names.append("turn")
        elif t == "rate":                                # persistence: the previous bin's arrival rate
            prev = np.concatenate([HD.n1[:, None].astype(float), HD.count[:, :-1].astype(float)], axis=1)
            width = np.concatenate([[1.0], np.diff(BIN_EDGES)[:-1]])
            cols.append(np.log((prev[:, b_lo:b_hi] + 0.5) / width[b_lo:b_hi][None, :]))
            names.append("rate")
        elif t == "s":
            cols.append(s - 0.75)
            names.append("s")
        elif t == "s2":
            cols.append((s - 0.75) ** 2)
            names.append("s2")
        elif t == "bands":
            band = np.digitize(s, SHARE_BANDS)
            for k in range(len(SHARE_LABELS)):
                if k != BAND_BASE:
                    cols.append(((band == k) & ~few).astype(float))
                    names.append(f"band{k}")
        else:
            raise KeyError(t)
    X = np.stack([c.reshape(-1) for c in cols], axis=1)
    y = HD.count[:, b_lo:b_hi].reshape(-1).astype(float)
    off = np.log(np.tile(np.diff(BIN_EDGES)[b_lo:b_hi], n_el))
    grp = np.repeat(np.arange(n_el), nb)
    return X, y, off, grp, tuple(names)


@dataclasses.dataclass
class PoissonFit:
    names: tuple
    beta: np.ndarray
    se: np.ndarray | None
    ll: float                    # log-likelihood without the log(y!) constant
    mu: np.ndarray


def poisson_irls(X, y, off, groups=None, names=(), robust=True, max_iter=60, ridge=1e-6) -> PoissonFit:
    k = X.shape[1]
    beta = np.zeros(k)
    beta[0] = np.log(max(y.sum() / np.exp(off).sum(), 1e-6)) if np.all(X[:, 0] >= 0) else 0.0
    eta = X @ beta + off
    for _ in range(max_iter):
        mu = np.exp(np.clip(eta, -30, 30))
        z = eta - off + (y - mu) / mu
        XtW = X.T * mu
        beta_new = np.linalg.solve(XtW @ X + ridge * np.eye(k), XtW @ z)
        eta = X @ beta_new + off
        step = np.max(np.abs(beta_new - beta))
        beta = beta_new
        if step < 1e-8:
            break
    mu = np.exp(np.clip(eta, -30, 30))
    ll = float(np.sum(y * eta - mu))
    se = None
    if robust and groups is not None:
        bread = np.linalg.inv((X.T * mu) @ X + ridge * np.eye(k))
        sg = np.zeros((int(groups.max()) + 1, k))
        np.add.at(sg, groups, X * (y - mu)[:, None])
        ng = len(np.unique(groups))
        se = np.sqrt(np.maximum(np.diag(bread @ (sg.T @ sg) @ bread) * ng / max(ng - 1, 1), 0.0))
    return PoissonFit(tuple(names), beta, se, ll, mu)


# ------------------------------------------------------------------ curves, shapes, stalls, late acceleration

def _stage_counts(hours: np.ndarray, cl: np.ndarray, n_el: int) -> np.ndarray:
    out = np.zeros((n_el, len(STAGES)))
    for j, (_, lo, hi) in enumerate(STAGES):
        m = (hours >= lo) & (hours < hi if hi < 168.0 else hours <= hi)
        out[:, j] = np.bincount(cl[m], minlength=n_el)
    return out


def curve_table(HD: HazardData, groups: dict[str, np.ndarray], checks=CHECK_HOURS) -> dict[str, dict]:
    """Cumulative participation: for each group of elections the vote-weighted share of all votes cast by each
    checkpoint hour (since the first vote) and the median over elections of the election's own share."""
    cl = np.repeat(np.arange(HD.n_elections), HD.esize)
    out = {}
    for name, mask in groups.items():
        sel = mask[cl]
        h = HD.hours[sel]
        pooled = [float(np.mean(h <= c)) for c in checks]
        per = np.array([[np.mean(HD.hours[HD.estart[e]:HD.estart[e] + HD.esize[e]] <= c) for c in checks]
                        for e in np.nonzero(mask)[0]])
        out[name] = {"n_elections": int(mask.sum()), "n_votes": int(sel.sum()), "pooled": pooled,
                     "median": [float(x) for x in np.median(per, axis=0)]}
    return out


def shape_class(counts: np.ndarray) -> np.ndarray:
    """Stage counts (A: 1-24 h, B: 24-96 h, C: 96-156 h, D: 156-168 h) -> a class per election:
    0 decelerating (rates non-increasing A >= B >= C >= D), 1 decelerating then an end bump (A >= B >= C, D > C),
    2 mid-phase faster than the first day (B > A: an ignition or S shape), 3 other."""
    w = np.array([hi - lo for _, lo, hi in STAGES])
    r = counts / w
    A_, B_, C_, D_ = r.T
    cls = np.full(len(r), 3)
    dec = (A_ >= B_) & (B_ >= C_)
    cls[dec & (C_ >= D_)] = 0
    cls[dec & (D_ > C_)] = 1
    cls[B_ > A_] = 2
    return cls


SHAPE_LABELS = ("decelerating", "decelerating + end bump", "mid-phase faster than day 1", "other")


def shape_table(HD: HazardData, n_min: int = 60, B: int = 300, seed: int = SEED) -> dict:
    """Observed shape classes against the clock-only null: each election's N votes redrawn independently from
    the pooled hour profile of elections of its size class (the null in which participation is a common clock
    and nothing else).  Also the spread across elections of the first-day share, observed against the null."""
    cl_v = np.repeat(np.arange(HD.n_elections), HD.esize)
    sel_el = np.nonzero(HD.esize >= n_min)[0]
    cls_edges = (60, 100, 160, 10**9)
    sc = np.digitize(HD.esize[sel_el], cls_edges[1:-1])
    obs_counts = _stage_counts(HD.hours, cl_v, HD.n_elections)[sel_el]
    in168 = (HD.hours <= 168.0)
    obs_cls = shape_class(obs_counts)
    obs_f24 = obs_counts[:, 0] / np.maximum(obs_counts.sum(axis=1), 1)
    rng = np.random.default_rng(seed)
    prof = {}
    for k in range(3):
        els = sel_el[sc == k]
        h = np.concatenate([HD.hours[HD.estart[e]:HD.estart[e] + HD.esize[e]] for e in els])
        prof[k] = h[(h >= 1.0) & (h <= 168.0)]
    null_freq = np.zeros((B, 4))
    null_var = np.zeros(B)
    stage_edges = np.array([1.0, 24.0, 96.0, 156.0, 168.0])
    for b in range(B):
        cnts = np.zeros((len(sel_el), 4))
        for k in range(3):
            idx = np.nonzero(sc == k)[0]
            if not len(idx):
                continue
            n_in = np.round(obs_counts[idx].sum(axis=1)).astype(int)
            draw = rng.choice(prof[k], size=int(n_in.sum()), replace=True)
            owner = np.repeat(idx, n_in)
            bins = np.clip(np.digitize(draw, stage_edges[1:-1]), 0, 3)
            np.add.at(cnts, (owner, bins), 1)
        c = shape_class(cnts)
        null_freq[b] = np.bincount(c, minlength=4) / len(c)
        null_var[b] = np.var(cnts[:, 0] / np.maximum(cnts.sum(axis=1), 1), ddof=1)
    obs_freq = np.bincount(obs_cls, minlength=4) / len(obs_cls)
    return {"n_elections": int(len(sel_el)), "obs_freq": obs_freq, "null_mean": null_freq.mean(0),
            "null_lo": np.percentile(null_freq, 2.5, axis=0), "null_hi": np.percentile(null_freq, 97.5, axis=0),
            "var_f24_obs": float(np.var(obs_f24, ddof=1)), "var_f24_null": float(null_var.mean()),
            "var_f24_null_hi": float(np.percentile(null_var, 97.5))}


def stall_table(HD: HazardData, windows=((72, 168), (120, 168), (144, 168))) -> dict:
    """P(no vote after hour t) -- the process has stalled (an institutional close or a lull to the deadline) --
    by the election's FINAL support class.  Descriptive; Wilson intervals.  Each row: (stalled, elections, share,
    Wilson low, Wilson high, stalled elections that were nevertheless promoted)."""
    out = {}
    for t, _ in windows:
        row = []
        for c in range(5):
            m = HD.fclass == c
            st = m & (HD.last_hour < t)
            k = int(st.sum())
            n = int(m.sum())
            row.append((k, n, *wilson(k, n), int(np.sum(st & (HD.eres == 1)))))
        out[t] = row
    return out


def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float, float]:
    if n == 0:
        return float("nan"), float("nan"), float("nan")
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return p, c - h, c + h


def late_acceleration(HD: HazardData, sign: np.ndarray, n_min: int = 30, t_state: float = 120.0,
                      alive_window=(72.0, 120.0)) -> dict:
    """Rate of votes in the last 12 hours (156-168 h) over the rate in the 36 hours before (120-156 h), by the
    running support share at hour `t_state`, among elections still alive (a vote in `alive_window`).  Ratio of
    sums per band; bands as SHARE_BANDS."""
    cl_v = np.repeat(np.arange(HD.n_elections), HD.esize)
    pre = HD.hours < t_state
    S = np.bincount(cl_v[pre & (sign == 1)], minlength=HD.n_elections).astype(float)
    O = np.bincount(cl_v[pre & (sign == -1)], minlength=HD.n_elections).astype(float)
    nn = S + O
    s = np.where(nn >= 5, S / np.maximum(nn, 1), np.nan)
    alive = np.bincount(cl_v[(HD.hours >= alive_window[0]) & (HD.hours < alive_window[1])], minlength=HD.n_elections) > 0
    cC = np.bincount(cl_v[(HD.hours >= t_state) & (HD.hours < 156.0)], minlength=HD.n_elections).astype(float)
    cD = np.bincount(cl_v[(HD.hours >= 156.0) & (HD.hours <= 168.0)], minlength=HD.n_elections).astype(float)
    ok = alive & (HD.esize >= n_min) & ~np.isnan(s)
    band = np.digitize(np.where(np.isnan(s), 0, s), SHARE_BANDS)
    out = {}
    wC, wD = 156.0 - t_state, 12.0
    for k, lab in enumerate(SHARE_LABELS):
        m = ok & (band == k)
        if m.sum() == 0:
            continue
        rC, rD = cC[m].sum() / wC, cD[m].sum() / wD
        out[lab] = {"n": int(m.sum()), "rate_C": float(rC / m.sum()), "rate_D": float(rD / m.sum()),
                    "ratio": float(rD / rC) if rC > 0 else float("nan")}
    out["_ok"] = ok
    out["_band"] = band
    out["_cC"], out["_cD"] = cC, cD
    return out


def late_accel_stat(HD: HazardData, sign: np.ndarray, **kw) -> dict[str, float]:
    """Ratio D/C by band, and the contrast (contested-passing band .70-.85 minus the pooled decisive bands
    >= .85 and < .50)."""
    t = late_acceleration(HD, sign, **kw)
    wC = 156.0 - kw.get("t_state", 120.0)
    ok, band, cC, cD = t["_ok"], t["_band"], t["_cC"], t["_cD"]
    r = {}
    for k, lab in enumerate(SHARE_LABELS):
        m = ok & (band == k)
        r[lab] = (cD[m].sum() / 12.0) / max(cC[m].sum() / wC, 1e-9) if m.sum() else float("nan")
    dec = ok & np.isin(band, (0, 3, 4))
    mid = ok & (band == 2)
    r["contrast"] = ((cD[mid].sum() / 12.0) / max(cC[mid].sum() / wC, 1e-9)) - ((cD[dec].sum() / 12.0) / max(cC[dec].sum() / wC, 1e-9))
    return r


# =================================================================== part 3: variations, compared out of sample

M_MIN_FORMS = 20       # every form is compared on the same votes: at least 20 before (so a 20-vote window exists)
SIGN_FORMS = {
    "controls only (no running state)": (),
    "cumulative share, linear (Kuran: threshold falls with the share)": ("s",),
    "cumulative share + curvature (convex = bandwagon, concave = gate)": ("s", "s2"),
    "cumulative share, spline (knots .50 .75 .90)": ("s", "hinge0.5", "hinge0.75", "hinge0.9"),
    "share of the last 5 votes": ("win5",),
    "share of the last 10 votes": ("win10",),
    "share of the last 20 votes": ("win20",),
    "vote margin S - O (tens)": ("margin",),
    "log-odds of the tally": ("logodds",),
    "majority indicator (step at 50%)": ("major",),
    "cumulative share x log turnout": ("s", "s_x_logn"),
    "cumulative share + last 5 votes": ("s", "win5"),
}


def _folds(n_groups: int, k: int, seed: int) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return rng.permutation(np.arange(n_groups) % k)


def compare_sign_forms(SD: SignData, k: int = 5, seed: int = SEED, forms: dict | None = None,
                       src: np.ndarray | None = None) -> list[dict]:
    """Each form of the running-state dependence, with the same controls, on the same votes; fit and scored
    out of sample with election-level folds.  Reports the in-sample log-likelihood, AIC, the held-out
    log-likelihood per 1000 votes relative to the controls-only model, and the standard error of that
    difference across elections."""
    forms = SIGN_FORMS if forms is None else forms
    A = arrange(SD, src)
    rows = target_rows(SD, A, m_min=M_MIN_FORMS)
    g = SD.cl[rows]
    y = A.y[rows]
    fold_of_el = _folds(SD.n_elections, k, seed)
    fold = fold_of_el[g]
    base = columns(SD, A, CONTROLS_X, rows)
    held = {}
    out = []
    for name, feats in forms.items():
        st = columns(SD, A, feats, rows) if feats else np.zeros((len(rows), 0))
        X = np.column_stack([np.ones(len(rows)), st, base])
        full = logit_irls(X, y, groups=g, names=("const",) + tuple(feats) + CONTROLS_X)
        ll_el = np.zeros(SD.n_elections)
        for f in range(k):
            tr, te = fold != f, fold == f
            fit = logit_irls(X[tr], y[tr], robust=False)
            mu = 1 / (1 + np.exp(-np.clip(X[te] @ fit.beta, -30, 30)))
            ll = y[te] * np.log(np.clip(mu, 1e-12, 1)) + (1 - y[te]) * np.log(np.clip(1 - mu, 1e-12, 1))
            ll_el += np.bincount(g[te], weights=ll, minlength=SD.n_elections)
        held[name] = ll_el
        i0 = 1
        out.append({"form": name, "k": X.shape[1], "ll": full.ll, "aic": 2 * X.shape[1] - 2 * full.ll,
                    "state_coef": {nm: (float(full.beta[i0 + j]), float(full.se[i0 + j])) for j, nm in enumerate(feats)},
                    "cv_ll": float(ll_el.sum()), "n": len(rows)})
    ref = held[next(iter(forms))]
    present = np.bincount(g, minlength=SD.n_elections) > 0
    for r in out:
        d = held[r["form"]] - ref
        r["cv_gain_per_1000"] = float(d.sum() / r["n"] * 1000)
        r["cv_gain_se"] = float(d[present].std(ddof=1) * np.sqrt(present.sum()) / r["n"] * 1000)
    return out


def spline_shape(SD: SignData) -> dict:
    """Slopes of P(support) in the running share, by segment, from the spline form (logit scale), with
    cluster-robust standard errors: slope on [0, .5), [.5, .75), [.75, .9), [.9, 1]."""
    A = arrange(SD)
    rows = target_rows(SD, A, m_min=M_MIN)
    feats = ("s", "hinge0.5", "hinge0.75", "hinge0.9")
    X = np.column_stack([np.ones(len(rows)), columns(SD, A, feats + CONTROLS_X, rows)])
    f = logit_irls(X, A.y[rows], groups=SD.cl[rows])
    b = f.beta[1:5]
    # cumulative slopes
    T = np.tril(np.ones((4, 4)))
    slopes = T @ b
    # delta-method SE via the robust covariance of the four state coefficients
    k = X.shape[1]
    bread = np.linalg.inv((X.T * (f.mu * (1 - f.mu))) @ X + 1e-9 * np.eye(k))
    score = X * (A.y[rows] - f.mu)[:, None]
    G = SD.n_elections
    sg = np.zeros((G, k))
    np.add.at(sg, SD.cl[rows], score)
    V = bread @ (sg.T @ sg) @ bread
    V4 = V[1:5, 1:5]
    se = np.sqrt(np.diag(T @ V4 @ T.T))
    return {"segments": ("0-.50", ".50-.75", ".75-.90", ".90-1"), "slope": slopes, "se": se, "n": len(rows)}


HAZARD_FORMS = {
    "clock + composition + scale": "",
    "+ turnout (one-sided complement in participation)": "turn",
    "+ turnout + recent rate": "turn+rate",
    "+ share, monotone": "turn+rate+s",
    "+ share + curvature (convex = Kuran, concave = two-sided)": "turn+rate+s+s2",
    "+ share bands (free shape)": "turn+rate+bands",
}
HAZARD_WINDOWS = {"1-24 h": (0, 8), "24-168 h": (8, 16), "1-168 h": (0, 16)}
RATE_FORM = "+ turnout + recent rate"


def compare_hazard_forms(HD: HazardData, window: tuple[int, int], k: int = 5, seed: int = SEED,
                         forms: dict | None = None, sign: np.ndarray | None = None) -> list[dict]:
    forms = HAZARD_FORMS if forms is None else forms
    sign = HD.sign if sign is None else sign
    n_el = HD.n_elections
    fold_of_el = _folds(n_el, k, seed)
    lo, hi = window
    held, out = {}, []
    for name, spec in forms.items():
        X, y, off, grp, names = _hazard_columns(HD, sign, spec, lo, hi)
        full = poisson_irls(X, y, off, grp, names)
        fold = fold_of_el[grp]
        ll_el = np.zeros(n_el)
        for f in range(k):
            tr, te = fold != f, fold == f
            fit = poisson_irls(X[tr], y[tr], off[tr], robust=False)
            eta = np.clip(X[te] @ fit.beta + off[te], -30, 30)
            ll_el += np.bincount(grp[te], weights=y[te] * eta - np.exp(eta), minlength=n_el)
        held[name] = ll_el
        coef = {nm: (float(b), float(s)) for nm, b, s in zip(names, full.beta, full.se)
                if nm in ("turn", "rate", "s", "s2") or nm.startswith("band")}
        out.append({"form": name, "spec": spec, "k": X.shape[1], "ll": full.ll, "aic": 2 * X.shape[1] - 2 * full.ll,
                    "coef": coef, "cv_ll": float(ll_el.sum()), "n_rows": len(y)})
    ref = held[next(iter(forms))]
    ref2 = held.get(RATE_FORM)
    for r in out:
        d = held[r["form"]] - ref
        r["cv_gain"] = float(d.sum())
        r["cv_gain_se"] = float(d.std(ddof=1) * np.sqrt(n_el))
        if ref2 is not None:
            d2 = held[r["form"]] - ref2
            r["cv_vs_rate"] = float(d2.sum())
            r["cv_vs_rate_se"] = float(d2.std(ddof=1) * np.sqrt(n_el))
    return out


def hazard_null(HD: HazardData, spec: str, window: tuple[int, int], B: int = 200, seed: int = SEED,
                keys: tuple = ("s", "s2", "band0", "band1", "band3", "band4")) -> dict:
    """Observed and sign-shuffled coefficients of the share terms of a hazard form.  The shuffle reassigns the
    non-neutral signs among the non-neutral slots of each election, so timing, turnout, composition and the
    first-hour scale are untouched and only the running share's PATH is randomised."""
    def one(sign):
        X, y, off, grp, names = _hazard_columns(HD, sign, spec, *window)
        f = poisson_irls(X, y, off, grp, names, robust=False)
        return {nm: float(b) for nm, b in zip(names, f.beta) if nm in keys}
    obs = one(HD.sign)
    nulls = [one(shuffle_signs(np.random.default_rng(np.random.SeedSequence([seed, b])), HD)) for b in range(B)]
    return {k: compare_to_null(obs[k], np.array([d[k] for d in nulls])) for k in obs}


# =================================================================== the run that feeds the results file

def _shuffled_sign_data(SD: SignData, seed: int, b: int) -> SignData:
    src = within_shuffle(np.random.default_rng(np.random.SeedSequence([seed, 7, b])), SD)
    return dataclasses.replace(SD, y=SD.y[src], p=SD.p[src], first=SD.first[src], exp=SD.exp[src], voter=SD.voter[src])


def bootstrap_ratio(ok: np.ndarray, band: np.ndarray, cC: np.ndarray, cD: np.ndarray, wC: float, B: int, seed: int) -> dict:
    """Bootstrap over elections of the ratio (rate in the last 12 h)/(rate before it) in each running-share band."""
    rng = np.random.default_rng(seed)
    out = {}
    idx = np.nonzero(ok)[0]
    n = len(idx)
    W = rng.multinomial(n, np.full(n, 1.0 / n), size=B).astype(float)          # B x n resampling counts
    for k, lab in enumerate(SHARE_LABELS):
        m = band[idx] == k
        if m.sum() < 5:
            continue
        num = W[:, m] @ cD[idx][m] / 12.0
        den = W[:, m] @ cC[idx][m] / wC
        r = num / np.maximum(den, 1e-9)
        out[lab] = (float(np.percentile(r, 2.5)), float(np.percentile(r, 97.5)))
    return out


ROBUST_VARIANTS = {
    "primary (gap 10 d, n >= 20, m >= 5, kappa 4)": {},
    "silence of 14 days splits a candidacy": {"gap_days": 14.0},
    "elections of at least 40 votes": {"n_min": 40},
    "targets with at least 10 votes before": {"m_min": 10},
    "targets with at least 20 votes before": {"m_min": 20},
    "targets cast at least 1 h after the first vote": {"min_hours": 1.0},
    "propensity prior strength 1": {"kappa": 1.0},
    "propensity prior strength 16": {"kappa": 16.0},
}


def compute_all(B: int = 400, B_rob: int = 100, B_forms: int = 12, B_haz: int = 150, B_hforms: int = 20,
                seed: int = SEED, n_jobs: int = 8, log: Callable[[str], None] = lambda s: None,
                B_ladder: int = 100, B_shape: int = 300, B_late: int = 300, B_boot: int = 1000, k_folds: int = 5,
                variants: dict | None = None) -> dict:
    """Everything the results file reports, with fixed seeds.  Takes 15 to 30 minutes on eight cores.  The
    defaults are the published settings; the keyword counts exist so that a test can run the whole pipeline small."""
    R: dict = {"seed": seed, "B": B, "B_rob": B_rob, "B_forms": B_forms, "B_haz": B_haz, "B_hforms": B_hforms,
               "B_ladder": B_ladder, "B_shape": B_shape, "B_late": B_late, "B_boot": B_boot, "k_folds": k_folds}
    v = load_votes()
    E = build_elections(v)
    SD = build_sign_data(v, E)
    HD = build_hazard_data(E)
    R["data"] = {
        "records": int(v.n), "support": int((v.vote == 1).sum()), "oppose": int((v.vote == -1).sum()),
        "neutral": int((v.vote == 0).sum()), "dated": int((~np.isnan(v.minute)).sum()),
        "dropped": E.dropped, "n_elections": int(E.n_elections), "n_votes_kept": int(len(E.vote)),
        "sign_elections": int(SD.n_elections), "sign_votes": int(SD.n),
        "hazard_elections": int(HD.n_elections), "hazard_votes": int(HD.sign.size),
        "size_bytes": SIZE_BYTES, "sha256": SHA256,
        "by_year": {int(y): (int((SD.eyear == y).sum()), int(SD.esize[SD.eyear == y].sum())) for y in np.unique(SD.eyear)},
        "by_size": {lab: (int((size_class(SD.esize) == k).sum()), int(SD.esize[size_class(SD.esize) == k].sum()))
                    for k, lab in enumerate(SIZE_LABELS)},
        "support_rate_sign": float(SD.y.mean()),
    }
    cells = cells_of(SD)
    log("part 1: observed fits")
    R["sign_fit"] = sign_fit_table(SD, cells)
    R["sign_obs"] = sign_stats(SD, None, cells)
    log(f"part 1: main shuffle null, B={B}")
    keys, null = sign_null(SD, cells, B=B, seed=seed, n_jobs=n_jobs)
    R["sign_keys"], R["sign_null"] = keys, null
    R["sign_cmp"] = {k: compare_to_null(R["sign_obs"][k], null[:, i]) for i, k in enumerate(keys)
                     if not np.isnan(R["sign_obs"][k])}
    log("part 1: ladder")
    lad_obs = ladder_stats(SD, None)
    lad_null = pmap([(lambda b=b: ladder_stats(SD, within_shuffle(np.random.default_rng(np.random.SeedSequence([seed, 5, b])), SD)))
                     for b in range(B_ladder)], n_jobs)
    R["ladder"] = {k: compare_to_null(lad_obs[k], np.array([d[k] for d in lad_null])) for k in lad_obs}
    log("part 1: robustness variants")
    variants = ROBUST_VARIANTS if variants is None else variants
    rob = {}
    for name, kw in variants.items():
        bkw = {k: kw[k] for k in ("gap_days",) if k in kw}
        skw = {k: kw[k] for k in ("n_min", "kappa") if k in kw}
        tkw = {k: kw[k] for k in ("m_min", "min_hours") if k in kw}
        E2 = build_elections(v, **bkw) if bkw else E
        SD2 = build_sign_data(v, E2, **skw) if (bkw or skw) else SD
        c2 = {"all": np.ones(SD2.n_elections, bool)}
        o2 = sign_stats(SD2, None, c2, windows=(10,), extras=False, **tkw)
        k2, n2 = sign_null(SD2, c2, B=B_rob, seed=seed + 1, n_jobs=n_jobs, windows=(10,), extras=False, **tkw)
        row = {}
        for key in ("all:logit_s", "all:fe_s", "placebo:L10:logit_prior", "placebo:L10:logit_post"):
            row[key] = compare_to_null(o2[key], n2[:, k2.index(key)])
        row["n_votes"] = int(len(target_rows(SD2, arrange(SD2), m_min=tkw.get("m_min", M_MIN), min_hours=tkw.get("min_hours", 0.0))))
        row["n_elections"] = int(SD2.n_elections)
        rob[name] = row
    R["robust"] = rob
    log("part 3: sign forms, observed and shuffled")
    R["sign_forms_obs"] = compare_sign_forms(SD, k=k_folds)
    shuf = pmap([(lambda b=b: compare_sign_forms(_shuffled_sign_data(SD, seed, b), k=k_folds)) for b in range(B_forms)], n_jobs)
    R["sign_forms_null"] = {r["form"]: np.array([s[i]["cv_gain_per_1000"] for s in shuf])
                            for i, r in enumerate(R["sign_forms_obs"])}
    R["spline"] = spline_shape(SD)
    log("part 1: time-gap profile and majority agreement")
    R["gap"] = compute_gap(SD, B=B, seed=seed, n_jobs=n_jobs)
    R["majority"] = compute_majority(SD, cells, B=B, seed=seed, n_jobs=n_jobs)
    log("part 1: asymmetry of the local dependence")
    R["asym"] = compute_asym(SD, B=max(B // 2, 20), seed=seed, n_jobs=n_jobs)
    log("part 1: local dependence without the opening hours")
    R["local_after"] = compute_local_after(SD, B=B_rob, seed=seed, n_jobs=n_jobs)
    log("part 1: local dependence by cell")
    R["local"] = compute_local(SD, cells, B=max(B // 2, 20), seed=seed, n_jobs=n_jobs)
    log("part 2: curves, shapes, stalls, late acceleration")
    cl_groups = {"all": np.ones(HD.n_elections, bool)}
    for c in range(5):
        cl_groups[f"final support {FINAL_LABELS[c]}"] = HD.fclass == c
    sc_h = np.digitize(HD.esize, (40, 80, 160))
    for k, lab in enumerate(("20-39", "40-79", "80-159", "160+")):
        cl_groups[f"{lab} votes"] = sc_h == k
    R["curves"] = curve_table(HD, cl_groups)
    R["shape"] = shape_table(HD, B=B_shape, seed=seed)
    R["stall"] = stall_table(HD)
    la = late_acceleration(HD, HD.sign)
    R["late_obs"] = {k: la[k] for k in SHARE_LABELS if k in la}
    ls_obs = late_accel_stat(HD, HD.sign)
    ls_null = [late_accel_stat(HD, shuffle_signs(np.random.default_rng(np.random.SeedSequence([seed, 9, b])), HD))
               for b in range(B_late)]
    R["late_cmp"] = {k: compare_to_null(ls_obs[k], np.array([d[k] for d in ls_null])) for k in ls_obs}
    R["late_boot"] = bootstrap_ratio(la["_ok"], la["_band"], la["_cC"], la["_cD"], 36.0, B_boot, seed)
    log("part 2: hazard shuffle tests")
    specs = {"turn+rate+s+s2": ("s", "s2"), "turn+rate+bands": ("band0", "band1", "band3", "band4")}
    jobs, tags = [], []
    for w, win in HAZARD_WINDOWS.items():
        for spec, keys_ in specs.items():
            jobs.append(lambda spec=spec, win=win, keys_=keys_: hazard_null(HD, spec, win, B=B_haz, seed=seed, keys=keys_))
            tags.append((w, spec))
    res = pmap(jobs, n_jobs)
    R["hazard_null"] = {t: r for t, r in zip(tags, res)}
    log("part 3: hazard forms")
    R["hazard_forms_obs"] = {w: compare_hazard_forms(HD, win, k=k_folds) for w, win in HAZARD_WINDOWS.items()}
    hj, ht = [], []
    for w, win in HAZARD_WINDOWS.items():
        for b in range(B_hforms):
            hj.append(lambda win=win, b=b: compare_hazard_forms(HD, win, k=k_folds, sign=shuffle_signs(
                np.random.default_rng(np.random.SeedSequence([seed, 11, b])), HD)))
            ht.append(w)
    hr = pmap(hj, n_jobs)
    R["hazard_forms_null"] = {w: {r["form"]: np.array([h[i]["cv_gain"] for h, t in zip(hr, ht) if t == w])
                                  for i, r in enumerate(R["hazard_forms_obs"][w])} for w in HAZARD_WINDOWS}
    R["turnout_bins"] = [(lo, hi) for lo, hi in TURNOUT_BINS]
    return R


# =================================================================== the results file

RESULTS = SIM_DIR / "results" / "crowd_gate_wikirfa.md"


def _t(headers: list[str], rows: list[list]) -> list[str]:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out + [""]


def _pm(x: float, se: float, d: int = 2) -> str:
    return f"{x:.{d}f} ({se:.{d}f})"


def _z(c: dict) -> str:
    return f"{c['z']:+.1f}" if not np.isnan(c["z"]) else "n/a"


def _p(p: float, B: int) -> str:
    return f"<= {1 / (B + 1):.4f}" if p <= 1 / (B + 1) + 1e-12 else f"{p:.3f}"


def cells_in_order(fit: dict) -> list[str]:
    return [c for c in fit]


def _cell_label(c: str) -> str:
    return {"all": "all"}.get(c, c[1:] if c.startswith("y") else "size " + c[1:])


def format_report(R: dict) -> str:
    cmp = R["sign_cmp"]
    B = R["B"]
    d = R["data"]
    fit = R["sign_fit"]
    L: list[str] = []
    add = L.append
    allc, all_fe = cmp["all:logit_s"], cmp["all:fe_s"]
    f_all = fit["all"]
    yrs = [c for c in fit if c.startswith("y")]
    pos_years = [c for c in yrs if fit[c]["logit_s"] > 0]
    sig_years = [c for c in yrs if cmp[f"{c}:logit_s"]["p_up"] <= 0.01]
    sz = [c for c in fit if c.startswith("n")]
    lead = lambda k: cmp[k]
    w10p, w10q = cmp["placebo:L10:logit_prior"], cmp["placebo:L10:logit_post"]
    gp = R["gap"]["cmp"]
    bins = {f"{lo}-{hi}": (cmp[f"turnout{lo}-{hi}:logit_s"], cmp[f"turnout{lo}-{hi}:fe_q"]) for lo, hi in TURNOUT_BINS}
    forms = {r["form"]: r for r in R["sign_forms_obs"]}
    nullm = {k: float(np.mean(v)) for k, v in R["sign_forms_null"].items()}
    ex = {k: forms[k]["cv_gain_per_1000"] - nullm[k] for k in forms}
    nulls = {k: float(np.std(v, ddof=1)) if len(v) > 1 else float("nan") for k, v in R["sign_forms_null"].items()}
    exz = {k: ex[k] / nulls[k] if nulls[k] > 0 else float("nan") for k in forms}
    zf = lambda k: f"{exz[k]:+.1f}" if np.isfinite(exz[k]) else "n/a"
    k_step = "majority indicator (step at 50%)"
    k_c5 = "cumulative share + last 5 votes"
    k_ctrl = "controls only (no running state)"
    k_cum = "cumulative share, linear (Kuran: threshold falls with the share)"
    k_w10 = "share of the last 10 votes"
    k_w5 = "share of the last 5 votes"
    k_spl = "cumulative share, spline (knots .50 .75 .90)"
    k_cur = "cumulative share + curvature (convex = bandwagon, concave = gate)"
    k_lo = "log-odds of the tally"
    k_mar = "vote margin S - O (tens)"
    hz = R["hazard_null"]
    hf = R["hazard_forms_obs"]
    hfn = R["hazard_forms_null"]
    sh = R["shape"]
    stall = R["stall"]
    late = R["late_obs"]
    lc = R["late_cmp"]
    cur = R["curves"]
    maj = R["majority"]

    add("# The crowd gate on wiki-RfA, 2003-2013: complements or substitutes, cascade, ignition, two-sided gate")
    add("")
    add(f"_Generated 2026-11-01 by `cd sim && ~/.local/bin/uv run python -m models.crowd_gate_wikirfa report` "
        f"(seed {R['seed']}; {R['B']} within-election shuffles for the main null, {R['B_rob']} for each robustness "
        f"variant, {R['B_forms']} for the form comparison, {R['B_haz']} for the hazard terms). Code: "
        "`sim/models/crowd_gate_wikirfa.py`; checks: `sim/tests/test_crowd_gate_wikirfa.py`. Ledger ids (grep "
        "`docs/ledger.jsonl`): the crowd law L1831, L1201, L1235, L1225; thresholds L3959, L3965, L3967, L4395; the "
        "Hong Kong march L4353-L4355, scope L4363, upper-gate mechanisms L4347, L4348; the data L4561-L4564. Results are "
        "computed statistics only; the data file is local-use-only and is not redistributed (`sim/data/README.md`)._")
    add("")
    add("**What was tested.** `models/00-v0.md` §4.4 writes the crowd law as r(t+1) = F[r(t)] with a two-sided gate "
        "(a person joins iff theta_i <= r <= thetabar_i) and carries the sign of \"more of the crowd acting makes me more "
        "likely to act\" as a setting operand sigma (the Hong Kong march found substitutes at its margin, L4355, and its "
        "authors say the sign may flip with turnout, L4363). Each adminship election on Wikipedia is a crowd event: signed "
        "public votes with minute timestamps, in a medium that shows the running tally. This file estimates sigma there, "
        "tests the participation curves for the monotone-cascade shape (Theorem 6.3), for ignition and for an upper gate, "
        "and compares the forms of the law out of sample.")
    add("")
    add("## Verdict")
    add("")
    add("**In short.**")
    add("")
    loc = R["local"]["cmp"]
    yrs05 = [c for c in yrs if c != "y2004"]
    loc_years = [c for c in yrs05 if f"{c}:prior" in loc and loc[f"{c}:prior"]["z"] >= 2.0]
    loc_sizes = [c for c in sz if loc[f"{c}:prior"]["z"] >= 2.0]
    n04 = d["by_year"].get(2004, (0, 0))[0]
    add(f"- *sigma, the sign of a vote's co-movement with the crowd just before it, is positive and nowhere robustly negative.* "
        f"The share of the previous 10 votes enters P(support) with logit coefficient {w10p['obs']:.2f} against a shuffle null of "
        f"{w10p['null_mean']:+.2f} (z {_z(w10p)}), with z >= 2 in {len(loc_years)} of the {len(yrs05)} years from 2005 on "
        f"(2004 has {n04} elections and no power) and in {len(loc_sizes)} of the {len(sz)} size classes; the same holds for the previous 5 and 20, in an "
        "election-fixed-effect model, and in the agreement of a vote with the majority of the last 5 to 10 votes (2.2). "
        f"A net negative association (substitutes as co-movement) is refuted at this scale. The z of {_z(w10p)} belongs to this "
        "previous-10 SHARE estimator alone (other windows and estimators differ). This is co-movement with the crowd just before a "
        "vote, not shown to be influence: influence against a shared shock is undecided by these data, and so is whether a "
        "negative causal response sits under a stronger shared shock (the third point).")
    add(f"- *The cumulative running share, the state variable the law names, carries little of it.* Out of sample, on votes with at "
        f"least {M_MIN_FORMS} earlier votes (where the cumulative share and a short window differ), the cumulative "
        f"share adds {ex[k_cum]:+.2f} log-likelihood per 1000 votes in its linear (Kuran) form and {ex[k_spl]:+.2f} as a spline "
        f"(z {zf(k_spl)}) beyond the controls once the mechanical gain (the same form fitted to shuffled elections) is "
        f"subtracted; the last-10-vote share adds {ex[k_w10]:+.2f}. The sign of the "
        f"cumulative coefficient depends on the sample and the estimator: {fit['all']['logit_s']:+.2f} at five or more earlier votes "
        f"(z {_z(allc)} against the shuffle), {bins['5-10'][0]['obs']:+.2f} and {bins['10-20'][0]['obs']:+.2f} below 20 earlier votes "
        f"(where the cumulative share is itself a short window), "
        f"{bins['40-80'][0]['obs']:+.2f} and {bins['80-1000000000'][0]['obs']:+.2f} above 40 in the same logit, but above its shuffle "
        f"null at every turnout once an election-specific trend is removed (the detrended coefficients and their nulls are both "
        f"negative; the excess is positive). Read literally, a later vote has the sign of the majority of the *last 5* votes "
        f"{(maj['all:w5']['obs'] - maj['all:w5']['null_mean']) * 100:+.1f} points more often than random order gives (z {_z(maj['all:w5'])}; "
        f"last 10: {(maj['all:w10']['obs'] - maj['all:w10']['null_mean']) * 100:+.1f}, z {_z(maj['all:w10'])}; "
        f"{(maj['all:w5_fast']['obs'] - maj['all:w5_fast']['null_mean']) * 100:+.1f} points when the previous vote came within 20 minutes) and the sign of the "
        f"*cumulative majority* {(maj['all:cum']['obs'] - maj['all:cum']['null_mean']) * 100:+.1f} points (z {_z(maj['all:cum'])}). "
        "The cumulative sign is therefore **not identified here** (non-stationary elections), and the law's state variable, "
        "if it is a crowd share, is a short-memory one.")
    fe10p, fe10q = cmp["placebo:L10:fe_prior"], cmp["placebo:L10:fe_post"]
    add(f"- *Whether the local dependence is influence or a shared shock is not decided, and the usual placebo cannot decide it.* "
        f"The dependence on the next 10 votes ({w10q['obs']:.2f}) is about as strong as on the previous 10 ({w10p['obs']:.2f}; the "
        f"fixed-effect model {'puts them the other way round' if (w10q['obs'] > w10p['obs']) != (fe10q['obs'] > fe10p['obs']) else 'orders them the same way'}, "
        f"{fe10q['obs']:.3f} against {fe10p['obs']:.3f}); on planted data a "
        "forward-influence world looks the same (tested), so time-symmetry is reported as time-symmetry. The gap profile "
        f"shows the excess agreement of consecutive votes peaks at 2-5 minutes ({(gp['gap2-5']['obs'] - gp['gap2-5']['null_mean']) * 100:+.1f} points) and is gone after about "
        f"four hours; votes saved in the same minute agree *less* than chance "
        f"({(gp['same_minute']['obs'] - gp['same_minute']['null_mean']) * 100:+.1f} points, z {_z(gp['same_minute'])}), which neither planted model "
        "produces and which is left unexplained.")
    hx = lambda w, k: hz[(w, "turn+rate+bands")][k]["obs"] - hz[(w, "turn+rate+bands")][k]["null_mean"]
    late_bands = [lab for lab in SHARE_LABELS if lab in lc]
    late_top = max(late_bands, key=lambda lab: lc[lab]["z"])
    late_dev = (f"one band departs the other way: elections with a running share of {late_top} at hour 120 rise more in the last 12 hours than "
                f"the shuffle gives (ratio {late[late_top]['ratio']:.2f} against {lc[late_top]['null_mean']:.2f}, z {_z(lc[late_top])}), "
                "so the late rise is not purely clock and composition, but it is not the law's ignition (a surge in contested states)"
                if lc[late_top]["z"] >= 3.0 else "no band's late rise departs from the shuffle by three standard deviations")
    def _hex(w):
        rate = [x for x in hf[w] if x["spec"] == "turn+rate"][0]["cv_gain"]
        return {r["spec"]: r["cv_vs_rate"] - (float(np.mean(hfn[w][r["form"]])) - rate) for r in hf[w]
                if r["spec"] in ("turn+rate+s", "turn+rate+s+s2", "turn+rate+bands")}
    first_curv = [w for w in HAZARD_WINDOWS if max(_hex(w), key=_hex(w).get) == "turn+rate+s+s2"]
    st72 = stall[72]
    n_st72, n_st72_prom = sum(r[0] for r in st72), sum(r[5] for r in st72)
    add(f"- *Participation (Theorem 6.3's object): a monotone, decelerating curve, no ignition tied to the state, and a one-sided "
        f"gate.* Pooled, {cur['all']['pooled'][4]:.0%} of an election's votes arrive in the first 24 hours; the dominant shape "
        f"(decelerating, with or without an end bump, {sh['obs_freq'][0] + sh['obs_freq'][1]:.0%} of elections) is one a common clock produces "
        f"{sh['null_mean'][0] + sh['null_mean'][1]:.0%} of the time, so the shape does not discriminate; the spread of the first-day share across elections is "
        f"{sh['var_f24_obs'] / sh['var_f24_null']:.1f} times the clock's, and {sh['obs_freq'][2] + sh['obs_freq'][3]:.0%} of elections "
        f"have shapes the clock rarely makes ({sh['null_mean'][2] + sh['null_mean'][3]:.1%}). The late rise in the contested band is "
        f"no larger than composition predicts (contested minus decisive {lc['contrast']['obs']:+.2f} against "
        f"{lc['contrast']['null_mean']:+.2f} under the shuffle, z {_z(lc['contrast'])}); {late_dev}. "
        "Participation falls when the running tally is against the candidate, already in the first 24 hours, before almost any "
        f"early closure (bands below 50% and 50-70%: {hx('1-24 h', 'band0'):+.2f} and {hx('1-24 h', 'band1'):+.2f} log-points against "
        f"the path-free null), and more over the week ({hx('1-168 h', 'band0'):+.2f} and {hx('1-168 h', 'band1'):+.2f}, which includes "
        "elections the rule had closed); it is flat once support passes 70% (a band edge, SHARE_BANDS, not an estimated breakpoint), and the bands above 85% do not fall. "
        "**No upper gate at decisive success shows in the path of the running share; failure closes the process** "
        f"(no vote after 72 h: {st72[0][2]:.0%} of elections ending below 40% support, {st72[1][2]:.0%} at 40-60%, "
        f"{st72[4][2]:.1%} at 90% or more; {n_st72 - n_st72_prom} of the {n_st72} elections silent after 72 h failed).")
    add("- *Best-fitting forms, out of sample, mechanical gain removed.* Sign: the share of the last 10 votes "
        f"({ex[k_w10]:+.2f} per 1000 votes, SE {forms[k_w10]['cv_gain_se']:.2f}); the cumulative forms gain much less (linear "
        f"{ex[k_cum]:+.2f}, curvature {ex[k_cur]:+.2f}, spline {ex[k_spl]:+.2f}, step at 50% {ex[k_step]:+.2f}, margin {ex[k_mar]:+.2f}), "
        f"and the log-odds form less than its own mechanical gain ({ex[k_lo]:+.2f}). "
        f"Participation: a saturating share term (concave, negative curvature) ranks first in {len(first_curv)} of "
        f"{len(HAZARD_WINDOWS)} windows, by margins inside the standard errors; the convex (Kuran) curvature is never supported.")
    add("")
    add("**Status of the claims about the crowd law's sign in this medium and era.**")
    add("")
    hi_all = max(abs(hx("1-168 h", "band3")), abs(hx("1-168 h", "band4")))
    hb_late = hz[("24-168 h", "turn+rate+bands")]
    s2z = {w: hz[(w, "turn+rate+s+s2")]["s2"]["z"] for w in HAZARD_WINDOWS}
    s2x = {w: hz[(w, "turn+rate+s+s2")]["s2"]["obs"] - hz[(w, "turn+rate+s+s2")]["s2"]["null_mean"] for w in HAZARD_WINDOWS}
    s2_beyond = [w for w in HAZARD_WINDOWS if s2z[w] <= -2.0]
    s2_txt = ", ".join(f"{w} {s2x[w]:+.2f} (z {s2z[w]:+.1f})" for w in HAZARD_WINDOWS)
    s2_neg_raw = all(hz[(w, "turn+rate+s+s2")]["s2"]["obs"] < 0 for w in HAZARD_WINDOWS)
    s2_neg_ex = all(x < 0 for x in s2x.values())
    s2_where = f"only over {', '.join(s2_beyond)}" if s2_beyond else "in no window"
    add("- *Refuted:* a net negative association (substitutes as co-movement) for the vote's sign at the local scale; an upper "
        "gate on participation at decisive success in the form this design can see, a fall of arrivals with the running share's "
        "path over and above the election's final composition: the bands above 85% sit at or above their null (over 1-168 h within "
        f"{hi_all:.2f} log-points; over 24-168 h {hx('24-168 h', 'band3'):+.2f} and {hx('24-168 h', 'band4'):+.2f}, z {_z(hb_late['band3'])} "
        f"and {_z(hb_late['band4'])}). A gate that acts through the final composition is absorbed by the composition control and "
        "is not tested.")
    every = lambda xs, n, one, many: f"every {one}" if len(xs) == n else f"{len(xs)} of the {n} {many}"
    add("- *Supported:* positive local co-movement of signs (sigma > 0 as an association), short-memory, strongest within an hour, "
        f"in {every(loc_years, len(yrs05), 'year', 'years')} from 2005 and {every(loc_sizes, len(sz), 'size class', 'size classes')}; "
        "a one-sided, saturating dependence of participation on the running support share "
        "(a fall below 70%, a band edge and not an estimated breakpoint, present in the first day; flat above); a stall (closure) that attaches to failure and rises as "
        f"final support falls ({n_st72 - n_st72_prom} of the {n_st72} elections silent after 72 h failed).")
    add("- *Not found:* state-triggered late acceleration (ignition): the contested band's late rise is no larger than "
        f"composition alone predicts (the {late_top} band's is larger, z {_z(lc[late_top])}: not where ignition would show); "
        f"{sh['obs_freq'][2]:.1%} of elections do have a mid-phase surge the clock cannot make, and whether the state triggers "
        "those is untested. A convex (Kuran: accelerating) curvature of participation in the running share: the raw curvature is "
        + ("negative in every window" if s2_neg_raw else "not of one sign")
        + (", and so is its excess over the shuffle null" if s2_neg_ex else "; its excess over the shuffle null is")
        + f" ({s2_txt}), beyond the null {s2_where}.")
    add("- *Undecided:* influence against shared shock as the source of the co-movement; the sign of the dependence on the "
        "cumulative share at 40 or more earlier votes; whether the monotone cascade orbit is the process behind "
        "the participation curve (the curve's shape is what attention decay also produces).")
    add("")

    # ------------------------------------------------------------------ 1. data
    add("## 1. Data, terms, cleaning")
    add("")
    add(f"- **Source and terms.** SNAP `wiki-RfA.txt.gz` (West, Paskov, Leskovec & Potts 2014, TACL 2: 297-310, "
        f"doi:10.1162/tacl_a_00184), the local copy under `sim/data/wiki-rfa/`: {d['size_bytes']:,} bytes, sha256 `{d['sha256']}`. "
        "SNAP states no terms; the comments are Wikipedia text (CC BY-SA) and are never parsed, stored or used here (the parser "
        "discards every TXT line); user names become integers on load and are never written out. Nothing from the file is committed.")
    add(f"- **Counts reproduce 117.** {d['records']:,} votes: {d['support']:,} support, {d['oppose']:,} oppose, {d['neutral']:,} neutral "
        "(L4562); per-year totals are tested in the suite (L4563).")
    dr = d["dropped"]
    add(f"- **Cleaning.** {d['dated']:,} votes carry a timestamp. Dropped: {dr['undated']:,} undated (9,367 empty fields and one "
        f"impossible hour), {dr['empty_voter']:,} with no voter, {dr['self_vote']} self-votes, {dr['stray']} stray timestamps "
        f"(a cluster of at most {STRAY_MAX} votes beside a cluster of at least {STRAY_SIBLING_MIN}), {dr['duplicate']} repeat votes "
        "by one voter in one election (the last stands). An *election* is one (candidate, result, year) group split at silences "
        f"over {GAP_DAYS:g} days (3,926 groups became {d['n_elections']:,} elections: a candidate can fail twice in a year). "
        f"{d['n_votes_kept']:,} votes remain.")
    add(f"- **Sign sample.** Non-neutral votes of the {d['sign_elections']:,} elections with at least {N_MIN} of them: "
        f"{d['sign_votes']:,} votes ({d['support_rate_sign']:.1%} support); targets are votes with at least {M_MIN} earlier "
        f"non-neutral votes ({f_all['n_votes']:,}). **Participation sample.** All votes (neutral too) of the "
        f"{d['hazard_elections']:,} elections with at least {N_MIN_PART} dated votes: {d['hazard_votes']:,} votes.")
    add("")
    add("Elections and votes in the sign sample, by year and by size class (non-neutral votes per election):")
    add("")
    rows = [[y, e, v] for y, (e, v) in d["by_year"].items()] 
    add("| year | " + " | ".join(str(y) for y in d["by_year"]) + " |")
    add("|---|" + "|".join("---" for _ in d["by_year"]) + "|")
    add("| elections | " + " | ".join(str(e) for e, _ in d["by_year"].values()) + " |")
    add("| votes | " + " | ".join(f"{v:,}" for _, v in d["by_year"].values()) + " |")
    add("")
    add("| size class | " + " | ".join(d["by_size"]) + " |")
    add("|---|" + "|".join("---" for _ in d["by_size"]) + "|")
    add("| elections | " + " | ".join(str(e) for e, _ in d["by_size"].values()) + " |")
    add("| votes | " + " | ".join(f"{v:,}" for _, v in d["by_size"].values()) + " |")
    add("")

    # ------------------------------------------------------------------ 2. sign
    add("## 2. Part 1: does a later vote follow the running crowd?")
    add("")
    add("**The estimator.** For every target vote: the running support share s and the running turnout n of the votes strictly "
        "before it (votes in the same minute do not see each other). Logit of P(support) on s with the voter's propensity (his "
        f"support rate at his OTHER (candidate, result, year) groups, shrunk with {KAPPA:g} pseudo-votes at the pooled rate, plus a first-timer flag and log "
        "experience), the election's leave-one-out support share and its result (the candidate's final outcome), log turnout "
        "and the clock (hour bins, position in the election). Standard errors are clustered by election.")
    add("")
    add("**The null.** The same votes (signs, voters, composition) reassigned at random to the election's own timestamps, "
        f"{R['B']} times, the whole pipeline re-run each time. It reproduces every mechanical artefact of the estimator "
        "(sampling without replacement, the leave-one-out bias, the controls) so only order-dependence is left. The "
        f"controls ladder shows why this matters: the raw coefficient is {R['ladder']['clock']['obs']:.1f} and the shuffle alone gives {R['ladder']['clock']['null_mean']:.1f}.")
    add("")
    lad = R["ladder"]
    add(f"**Controls ladder** (coefficient on the running share, all targets; null from {R.get('B_ladder', 100)} shuffles):")
    add("")
    L.extend(_t(["controls", "coefficient", "null mean (sd)", "z"],
            [["clock and turnout only", f"{lad['clock']['obs']:.2f}", f"{lad['clock']['null_mean']:.2f} ({lad['clock']['null_sd']:.2f})", _z(lad['clock'])],
             ["+ voter propensity", f"{lad['propensity']['obs']:.2f}", f"{lad['propensity']['null_mean']:.2f} ({lad['propensity']['null_sd']:.2f})", _z(lad['propensity'])],
             ["+ candidate outcome (no propensity)", f"{lad['outcome']['obs']:.2f}", f"{lad['outcome']['null_mean']:.2f} ({lad['outcome']['null_sd']:.2f})", _z(lad['outcome'])],
             ["+ both (the primary specification)", f"{lad['both']['obs']:.2f}", f"{lad['both']['null_mean']:.2f} ({lad['both']['null_sd']:.2f})", _z(lad['both'])]]))
    add("The candidate's outcome is the confounder (a good candidate has a high running share and later supporters); the "
        "voter's propensity moves nothing. What the outcome control costs: under herding the final composition is itself an "
        "outcome of the early votes, and conditioning on it makes the test conservative for complements (tested on planted data).")
    add("")
    add("### 2.1 Primary result, by year and by election size")
    add("")
    rows = []
    for c in fit:
        f = fit[c]
        a, b = cmp[f"{c}:logit_s"], cmp[f"{c}:fe_s"]
        rows.append([_cell_label(c), f["n_elections"], f"{f['n_votes']:,}", f"{f['support_rate']:.2f}", _pm(f["logit_s"], f["logit_se"]),
                     f"{f['ame10'] * 100:+.2f} ({f['ame10_se'] * 100:.2f})", f"{a['null_mean']:+.2f} ({a['null_sd']:.2f})", _z(a), _p(a["p_up"], B),
                     _pm(f["fe_s"], f["fe_se"]), f"{b['null_mean']:+.2f}", _z(b)])
    L.extend(_t(["cell", "elections", "votes", "P(sup)", "logit coef (se)", "AME +10 pts (pp)", "shuffle null (sd)", "z", "p (>= obs)",
             "FE-LPM coef (se)", "FE null", "FE z"], rows))
    pos_sizes = [c for c in sz if fit[c]["logit_s"] > 0]
    n_cells = len(fit)
    bonf = 0.05 / n_cells
    bonf_years = [c for c in yrs if cmp[f"{c}:logit_s"]["p_up"] <= bonf + 1e-12]
    add(f"Reading: the coefficient is positive in {every(pos_years, len(yrs), 'year', 'years')} and "
        f"{every(pos_sizes, len(sz), 'size class', 'size classes')}; "
        f"{len(sig_years)} years reach p <= 0.01 (one-sided, in the direction of complements), and {len(bonf_years)} pass a "
        f"Bonferroni bar for the {n_cells} cells (p <= {bonf:.4f}; the smallest attainable p is {1 / (B + 1):.4f}). The fixed-effect "
        "model's null is far below zero (an election fixed effect contains the vote's own sign), so only the z against it is read. "
        f"Overall AME: {f_all['ame10'] * 100:+.2f} points of P(support) per +10 points of running share.")
    add("")
    add("### 2.2 Other estimators of the same quantity (all targets)")
    add("")
    def row(lbl, key, scale=1.0):
        c = cmp[key]
        return [lbl, f"{c['obs']:.3f}", f"{c['null_mean']:.3f} ({c['null_sd']:.3f})", _z(c), _p(c["p_up"], B)]
    L.extend(_t(["estimator", "observed", "shuffle null (sd)", "z", "p (>= obs)"],
            [row("logit, primary", "all:logit_s"), row("logit, elections weighted equally", "all:logit_s_w"),
             row("linear, election fixed effects", "all:fe_s"), row("linear, election-specific quadratic trend removed", "all:fe_q"),
             row("linear, voter fixed effects + composition controls", "all:fev_s"),
             row("agreement with the cumulative majority (>= 5 earlier votes)", "all:agree")]))
    add("The first five agree on the sign of the excess over their own nulls (the detrended coefficient is negative, but less so "
        "than its null). The last is the literal reading of \"follows the running "
        "majority\" with the *cumulative* majority: agreement is slightly *below* what random order gives. That statistic has "
        "no power against complements in a cumulative world (planted data) and picks up non-stationarity: real elections open "
        "with a run of supports and drift, so the early majority is a poorer guide to later votes than a random sample would be.")
    add("")
    add("**Agreement with the majority before the vote** (targets with at least 5 earlier votes; a strict majority needed; excess "
        "in percentage points over random order). *Fast* = the previous vote was at most 20 minutes earlier, *slow* = longer:")
    add("")
    rows = []
    for lbl, k in (("all earlier votes", "cum"), ("last 20 votes", "w20"), ("last 10 votes", "w10"), ("last 5 votes", "w5")):
        a, f_, s_ = maj[f"all:{k}"], maj[f"all:{k}_fast"], maj[f"all:{k}_slow"]
        rows.append([lbl, f"{a['obs']:.4f}", f"{a['null_mean']:.4f} ({a['null_sd']:.4f})", f"{(a['obs'] - a['null_mean']) * 100:+.2f}", _z(a),
                     f"{(f_['obs'] - f_['null_mean']) * 100:+.2f} ({_z(f_)})", f"{(s_['obs'] - s_['null_mean']) * 100:+.2f} ({_z(s_)})"])
    L.extend(_t(["majority of", "agreement", "random order (sd)", "excess (points)", "z", "fast: excess (z)", "slow: excess (z)"], rows))
    ys = [c for c in fit if c.startswith("y")]
    add("The answer to the literal question is two-sided. Votes follow the majority of the last 5 to 10 votes more often than "
        "random order gives, almost entirely when votes are arriving within minutes of each other; they do not follow the "
        "cumulative majority (below random order in every year, points: "
        + ", ".join(f"{c[1:]} {(maj[c + ':cum']['obs'] - maj[c + ':cum']['null_mean']) * 100:+.1f}" for c in ys[1:]) + "). The recent-majority excess is positive in every size class ("
        + ", ".join(f"{c[1:]} {(maj[c + ':w10']['obs'] - maj[c + ':w10']['null_mean']) * 100:+.1f}" for c in fit if c.startswith("n")) + " points for the last 10) and in every year from 2006 ("
        + ", ".join(f"{c[1:]} {(maj[c + ':w10']['obs'] - maj[c + ':w10']['null_mean']) * 100:+.1f}" for c in ys[2:]) + ").")
    add("")
    add("### 2.3 By running turnout (the sign can flip with turnout, L4363)")
    add("")
    rows = []
    for lo, hi in TURNOUT_BINS:
        a, b = bins[f"{lo}-{hi}"]
        lab = f"{lo}-{hi - 1}" if hi < 10**8 else f"{lo}+"
        rows.append([lab, f"{a['obs']:+.2f}", f"{a['null_mean']:+.2f} ({a['null_sd']:.2f})", _z(a), f"{b['obs']:.2f}", f"{b['null_mean']:.2f} ({b['null_sd']:.2f})", _z(b)])
    L.extend(_t(["earlier votes", "logit coef", "null (sd)", "z", "detrended FE coef", "null (sd)", "z"], rows))
    add("Read against their own nulls, the two estimators agree below 20 earlier votes (both above the null) and disagree "
        "above 40: the logit falls below its null, the detrended model stays above its null (its coefficients are negative, its "
        "null more so). Both are calibrated against their own shuffle null, and the disagreement "
        "is a statement about what each assumes of the election's trend, so the sign of the cumulative dependence at high "
        "turnout is **undecided**. A stricter minimum number of earlier votes moves the primary coefficient the same way "
        "(2.5).")
    add("")
    add("### 2.4 The local dependence, and the time-reversal placebo that does not discriminate")
    add("")
    rows = []
    for Lw in PLACEBO_WINDOWS:
        a, b = cmp[f"placebo:L{Lw}:logit_prior"], cmp[f"placebo:L{Lw}:logit_post"]
        c, e = cmp[f"placebo:L{Lw}:fe_prior"], cmp[f"placebo:L{Lw}:fe_post"]
        rows.append([Lw, f"{a['obs']:.2f} ({_z(a)})", f"{b['obs']:.2f} ({_z(b)})", f"{c['obs']:+.3f} ({_z(c)})", f"{e['obs']:+.3f} ({_z(e)})"])
    L.extend(_t(["window L", "logit: previous L votes (z)", "logit: next L votes (z)", "FE: previous L (z)", "FE: next L (z)"], rows))
    add("Entered together, the share of the previous L and the next L votes both carry the dependence, at every L, in the "
        "logit and in the fixed-effect model. If earlier votes caused later ones, the previous window should dominate; it does "
        "not. **That is a weaker conclusion than it looks**: on planted data (suite) a stationary chain in which each vote "
        "follows its five predecessors also gives equal coefficients on both windows -- a reversible process looks the same "
        "run backwards -- exactly as a shared shock does. The placebo shows the dependence is about equally strong in both "
        "directions (the logit puts the next window a little ahead, the fixed-effect model the previous one); it neither "
        "supports nor refutes influence.")
    add("")
    add("**The local dependence by year and by size** (previous 10 and next 10 votes entered together; logit coefficients with the primary controls, "
        f"{R['local']['B']} shuffles, so the z of the first row differs a little from the table above, which uses {R['B']}):")
    add("")
    rows = []
    for c in cells_in_order(fit):
        a, b = loc[f"{c}:prior"], loc[f"{c}:post"]
        ob = R["local"]["obs"]
        rows.append([_cell_label(c), f"{int(ob[c + ':n']):,}", f"{_pm(a['obs'], ob[c + ':prior_se'])}", f"{a['null_mean']:+.2f}", _z(a), f"{_pm(b['obs'], ob[c + ':post_se'])}", _z(b)])
    L.extend(_t(["cell", "targets", "previous 10 (se)", "null", "z", "next 10 (se)", "z"], rows))
    yr_prior = [R["local"]["obs"][f"{c}:prior"] for c in yrs05]
    cells_pos = [c for c in yrs05 + sz if R["local"]["obs"][f"{c}:prior"] > 0 and R["local"]["obs"][f"{c}:post"] > 0]
    from scipy.stats import norm
    m_loc = len(yrs05) + len(sz)
    z_bar = float(norm.isf(0.05 / m_loc))
    add(f"Positive in both directions in {len(cells_pos)} of the {m_loc} cells from 2005 (years and size classes). "
        f"(2004: {n04} elections, nothing to read.) With {m_loc} cells a one-sided Bonferroni bar at 0.05 is z >= {z_bar:.2f}; "
        f"{sum(1 for c in yrs05 + sz if loc[c + ':prior']['z'] >= z_bar)} of the {m_loc} pass it for the previous 10. "
        "This is the registry's drift test (112 section 6.5, test 3: a stable sign pattern while magnitudes move), which 112 "
        "states for the 16-type tie-sign model and which is applied here by analogy to the crowd coefficient: "
        f"the coefficient runs from {min(yr_prior):.1f} to {max(yr_prior):.1f} across 2005-2013 with no sign change.")
    add("")
    la_ = R["local_after"]
    add("**Is it the opening wave?** The first votes of an election are plausibly the nominator's circle (an informal look at "
        "the file's first records suggested it; not coded, the module never reads the comments). Excluding the opening hours as "
        "*targets* (their votes stay in the "
        f"windows as context), previous-10 / next-10 coefficients ({R['B_rob']} shuffles each):")
    add("")
    rows = [[f"first {h:g} h excluded" if h else "none excluded", f"{la_[h]['n']:,}", f"{la_[h]['all:prior']['obs']:.2f} ({_z(la_[h]['all:prior'])})",
             f"{la_[h]['all:post']['obs']:.2f} ({_z(la_[h]['all:post'])})"] for h in LATE_HOURS]
    L.extend(_t(["targets", "n", "previous 10 (z)", "next 10 (z)"], rows))
    h0 = LATE_HOURS[0]
    mv = max(abs(la_[h][k]["obs"] - la_[h0][k]["obs"]) for h in LATE_HOURS for k in ("all:prior", "all:post"))
    add(f"The coefficients move by at most {mv:.2f} when up to the first {max(LATE_HOURS):g} hours' targets are dropped, and every z "
        "stays above 12: it is not the opening wave." if min(la_[h][k]["z"] for h in LATE_HOURS for k in ("all:prior", "all:post")) > 12
        else f"The coefficients move by at most {mv:.2f} when up to the first {max(LATE_HOURS):g} hours' targets are dropped.")
    add("")
    ay = R["asym"]
    add("**Asymmetric herding?** A randomised experiment on prior ratings (L1130, `sa`, abstract only: a comparator, not evidence here) found "
        "positive prior ratings raised later positive ones while negative ones were corrected. Slopes of the logit in the share of the "
        f"previous 10 votes below and above one half, each against its shuffle null (the null is not flat: composition enters nonlinearly): "
        f"below 50%: {ay['below']['obs']:+.2f} against {ay['below']['null_mean']:+.2f} (excess {ay['below']['obs'] - ay['below']['null_mean']:+.2f}, z {_z(ay['below'])}); "
        f"above 50%: {ay['above']['obs']:+.2f} against {ay['above']['null_mean']:+.2f} (excess {ay['above']['obs'] - ay['above']['null_mean']:+.2f}, z {_z(ay['above'])}). "
        + (f"The difference of the two slopes, above minus below, is {ay['diff']['obs'] - ay['diff']['null_mean']:+.2f} over its null "
           f"(z {_z(ay['diff'])}): " if "diff" in ay else "")
        + ("no asymmetry between following a supportive and an opposing run is detected at this power."
           if "diff" in ay and abs(ay["diff"]["z"]) < 2.0 else
           (("the excess is larger above one half (following a supportive run) than below it" if ay["diff"]["obs"] > ay["diff"]["null_mean"]
             else "the excess is larger below one half (following an opposing run) than above it")
            + (", but both are positive: an asymmetry of degree, not the correction of opposing runs the comparator reports."
               if min(ay["below"]["obs"] - ay["below"]["null_mean"], ay["above"]["obs"] - ay["above"]["null_mean"]) > 0 else ".")) if "diff" in ay
           else "The difference was not tested."))
    add("")
    add("**Gap profile.** Do consecutive votes agree, by the minutes between them (excess over the shuffle null):")
    add("")
    gc = R["gap"]["counts"]
    rows = [[lab, f"{gc['gap' + lab]:,}", f"{gp['gap' + lab]['obs']:.3f}", f"{gp['gap' + lab]['null_mean']:.3f}", f"{gp['gap' + lab]['obs'] - gp['gap' + lab]['null_mean']:+.3f}", _z(gp['gap' + lab])]
            for lab in GAP_LABELS]
    rows.append(["same minute (order-free)", f"{gc['same_minute']:,}", f"{gp['same_minute']['obs']:.3f}", f"{gp['same_minute']['null_mean']:.3f}",
                 f"{gp['same_minute']['obs'] - gp['same_minute']['null_mean']:+.3f}", _z(gp['same_minute'])])
    L.extend(_t(["gap (minutes)", "pairs", "agree", "null", "excess", "z"], rows))
    add("The dependence is a few percentage points, peaks at 2-5 minutes, is a third of its peak by an hour and is gone after about four hours. "
        "Votes saved in the same minute agree **less** than chance (pairs are compared without using their order, because "
        "within a minute the file lists supports before opposes). On planted data both a visible-influence world and a "
        "continuous shock give a same-minute *surplus*, so the deficit is produced by neither; a technical cause (for example "
        "simultaneous saves of one section being refused by the wiki) is a guess that was not checked. The pattern fits "
        "\"the recent past matters\" and is why the recency window fits best (4.1).")
    add("")
    add("### 2.5 Robustness to the cleaning")
    add("")
    rows = []
    for name, r in R["robust"].items():
        a, b, c, e = r["all:logit_s"], r["all:fe_s"], r["placebo:L10:logit_prior"], r["placebo:L10:logit_post"]
        rows.append([name, f"{r['n_votes']:,}", f"{a['obs']:+.2f} ({_z(a)})", f"{b['obs']:+.2f} ({_z(b)})", f"{c['obs']:.2f} ({_z(c)})", f"{e['obs']:.2f} ({_z(e)})"])
    L.extend(_t(["variant", "targets", "logit coef (z)", "FE coef (z)", "previous-10 share (z)", "next-10 share (z)"], rows))
    add(f"({R['B_rob']} shuffles each. The two window columns need ten votes on each side, so they ignore the minimum-history and "
        "one-hour rules and change only with the silence, the election size and the propensity prior.) The local dependence and "
        "the fixed-effect result do not move with the cleaning. The "
        "cumulative logit coefficient does: positive for five earlier votes, weaker at ten, negative at twenty -- the same "
        "turnout dependence as 2.3, not a cleaning effect.")
    add("")

    # ------------------------------------------------------------------ 3. participation
    add("## 3. Part 2: participation")
    add("")
    add("### 3.1 Cumulative curves")
    add("")
    hdr = ["group", "elections", "votes"] + [f"{h} h" for h in (1, 6, 24, 72, 120, 168)]
    idx = [CHECK_HOURS.index(h) for h in (1, 6, 24, 72, 120, 168)]
    rows = [[k, v["n_elections"], f"{v['n_votes']:,}"] + [f"{v['pooled'][i]:.2f}" for i in idx] for k, v in cur.items()]
    L.extend(_t(hdr, rows))
    add("Share of an election's votes cast by each hour after its first vote (pooled over votes). Every curve is monotone (a count), front-loaded and concave. Elections that end below 40% support are "
        "over soonest; elections of 80 or more votes are the slowest to fill.")
    add("")
    add("### 3.2 Shape against a clock-only null")
    add("")
    add(f"Stage rates over hours 1-24, 24-96, 96-156, 156-168 ({sh['n_elections']} elections of 60 or more votes). The null redraws "
        "each election's votes independently from the pooled hour profile of elections of its size: participation as one "
        f"common clock and nothing else ({R.get('B_shape', 300)} redraws; interval = 2.5-97.5%).")
    add("")
    rows = [[SHAPE_LABELS[i], f"{sh['obs_freq'][i]:.1%}", f"{sh['null_mean'][i]:.1%} [{sh['null_lo'][i]:.1%}, {sh['null_hi'][i]:.1%}]"] for i in range(4)]
    L.extend(_t(["shape", "observed", "clock-only null"], rows))
    add(f"Variance across elections of the first-day share of votes: observed {sh['var_f24_obs']:.4f}, clock-only null "
        f"{sh['var_f24_null']:.4f} (97.5% point {sh['var_f24_null_hi']:.4f}): **{sh['var_f24_obs'] / sh['var_f24_null']:.1f} times** the clock's. "
        "The plainest shape (rates non-increasing, no late bump) matches the clock to the percentage point, and the clock makes the "
        "end-bump variant more often than the data show, so the curve's shape does not discriminate between a cascade "
        "orbit and attention decay. What a clock cannot make is the spread: elections differ in speed, and (3.3-3.5) the difference is tied to how the tally goes.")
    add("")
    add("### 3.3 Stall: the process stops early for failure, and more often the lower the final support")
    add("")
    rows = []
    for c in range(5):
        r72, r120, r144 = stall[72][c], stall[120][c], stall[144][c]
        rows.append([FINAL_LABELS[c], r72[1], f"{r72[2]:.1%} [{r72[3]:.1%}, {r72[4]:.1%}]", f"{r120[2]:.1%} [{r120[3]:.1%}, {r120[4]:.1%}]", f"{r144[2]:.1%} [{r144[3]:.1%}, {r144[4]:.1%}]"])
    L.extend(_t(["final support", "elections", "no vote after 72 h", "after 120 h", "after 144 h"], rows))
    add(f"Wilson intervals. Theorem 6.3's orbit stalls at the least fixed point; here the candidacies that stall before the "
        f"deadline are failing ones ({n_st72 - n_st72_prom} of the {n_st72} elections with no vote after 72 h were not promoted), "
        "and the stall rate rises steadily as the final support falls, not only at decisive failure (the file does not say why; "
        "early closing or withdrawal would be the presumed reasons -- an institutional gate on top of the voluntary one). "
        "Successful candidacies run on at a low rate to the clock. The closing gate is one-sided.")
    add("")
    add("### 3.4 Ignition: is there a late acceleration, and does the state trigger it?")
    add("")
    rows = []
    for lab in SHARE_LABELS:
        if lab not in late:
            continue
        o = late[lab]
        cm = lc[lab]
        bt = R["late_boot"].get(lab, (float("nan"), float("nan")))
        rows.append([lab, o["n"], f"{o['rate_C']:.3f}", f"{o['rate_D']:.3f}", f"{o['ratio']:.2f} [{bt[0]:.2f}, {bt[1]:.2f}]", f"{cm['null_mean']:.2f} ({cm['null_sd']:.2f})", _z(cm)])
    L.extend(_t(["running share at hour 120", "elections", "votes/h, 120-156 h", "votes/h, 156-168 h", "ratio last 12 h / before [95% CI]", "null (sd)", "z"], rows))
    add(f"Elections still alive (a vote between hours 72 and 120) with 30 or more votes; the ratio exceeds one in the passing "
        f"bands (a deadline bump), is about one at 50-70% and is below one only where the tally is losing. The contested-passing band (70-85%) "
        f"minus the pooled decisive bands is {lc['contrast']['obs']:+.2f}; the shuffle that keeps each election's composition "
        f"but randomises the path gives {lc['contrast']['null_mean']:+.2f} ({lc['contrast']['null_sd']:.2f}), so the contrast is "
        f"**smaller** than composition alone predicts (z {_z(lc['contrast'])}). Ignition in the law's sense (a rise triggered by "
        "a contested state) is not seen. The band-by-band z column is not flat, though: "
        + ", ".join(f"{lab} {_z(lc[lab])}" for lab in SHARE_LABELS if lab in lc)
        + "; the late rise is therefore not purely a clock-and-composition effect, but where it departs from the shuffle (above "
        "the null at " + (", ".join(lab for lab in SHARE_LABELS if lab in lc and lc[lab]["z"] >= 2.0) or "no band")
        + "; below it at " + (", ".join(lab for lab in SHARE_LABELS if lab in lc and lc[lab]["z"] <= -2.0) or "no band")
        + ") is not a surge in the contested band, which is where ignition would show.")
    add("")
    add("### 3.5 The hazard of new votes and the gate")
    add("")
    add("Poisson regression of the number of votes per bin (16 bins over hours 1-168) on a common time profile, year, the "
        "first hour's votes (election scale), the final-support class (composition), log turnout since the first hour, the "
        "previous bin's rate (persistence) and the running support share (three or more earlier non-neutral votes; "
        "bands below). Coefficients relative to the 70-85% band. The shuffle reassigns the signs among the vote slots of "
        "each election, so timing, turnout and composition are untouched and only the share's *path* is randomised; a "
        "coefficient beyond its null is dependence of timing on the tally's history, over and above the election's "
        "composition.")
    add("")
    rows = []
    for w in HAZARD_WINDOWS:
        b = hz[(w, "turn+rate+bands")]
        s = hz[(w, "turn+rate+s+s2")]
        f_bands = [r for r in hf[w] if r["spec"] == "turn+rate+bands"][0]["coef"]
        rows.append([w, f"{f_bands['turn'][0]:.2f}", f"{f_bands['rate'][0]:.2f}"] +
                    [f"{b[k]['obs']:+.2f} / {b[k]['null_mean']:+.2f} ({_z(b[k])})" for k in ("band0", "band1", "band3", "band4")] +
                    [f"{s['s']['obs']:+.2f} / {s['s']['null_mean']:+.2f} ({_z(s['s'])})", f"{s['s2']['obs']:+.2f} / {s['s2']['null_mean']:+.2f} ({_z(s['s2'])})"])
    L.extend(_t(["window", "turnout", "rate", "< 50%", "50-70%", "85-95%", ">= 95%", "share (linear)", "share curvature"], rows))
    t_alone = [r["coef"]["turn"][0] for w in HAZARD_WINDOWS for r in hf[w] if r["spec"] == "turn"]
    t_rate = [r["coef"]["turn"][0] for w in HAZARD_WINDOWS for r in hf[w] if r["spec"].startswith("turn+rate")]
    add("Each share cell: observed / shuffle null (z). Participation is lower than the composition-and-clock null when the "
        "tally runs against the candidate, and is flat at and above 85%; in the late window the high bands sit *above* the "
        "null. The low bands of the late window include elections the closing rule had already stopped (3.3), so there the "
        "gate is partly institutional; the first-day window, before almost any early closure, shows the same direction at a "
        "smaller size. The raw curvature is negative, but so is its null (most of it is the mechanical shape the shuffle also "
        f"gives); the excess is {s2_txt}: "
        + ("a plateau, not a fall, and never convex. " if s2_neg_ex else "not of one sign. ")
        + f"The turnout coefficient ({min(t_alone):.2f} to {max(t_alone):.2f} alone, {min(t_rate):.2f} to {max(t_rate):.2f} once the "
        "previous rate is controlled) is an association "
        "with no null: turnout and unobserved popularity are not separable here, so it is not read as complements in "
        "participation.")
    add("")

    # ------------------------------------------------------------------ 4. variations
    add("## 4. Part 3: variations, compared out of sample")
    add("")
    add("### 4.1 The sign's dependence on the crowd: the forms compared")
    add("")
    add(f"Same controls, same votes (at least {M_MIN_FORMS} earlier), election-level 5-fold cross-validation. \"CV gain\" is the "
        "held-out log-likelihood per 1000 votes over the controls-only model; \"null gain\" is the same number from "
        f"{R['B_forms']} within-election shuffles, **where any gain is mechanical** (flexible forms fit the nonlinear way the "
        "candidate's composition enters); \"excess\" is the difference.")
    add("")
    rows = []
    for r in R["sign_forms_obs"]:
        k = r["form"]
        nv = R["sign_forms_null"][k]
        rows.append([k, r["k"], f"{r['aic']:.0f}", f"{r['cv_gain_per_1000']:+.2f} ({r['cv_gain_se']:.2f})",
                     f"{nv.mean():+.2f} ({nulls[k]:.2f})", f"{r['cv_gain_per_1000'] - nv.mean():+.2f}", zf(k)])
    L.extend(_t(["form", "params", "AIC", "CV gain (se)", "null gain (sd)", "excess", "z"], rows))
    add(f"z is the excess over the sd of the {R['B_forms']} null draws: a test against random order, rough with so few draws, "
        "and not a precision (the se column is the sampling error of the gain itself). In-sample AIC prefers the log-odds and "
        "spline forms; most of their out-of-sample gain is what shuffled data give too (the spline "
        f"{nullm[k_spl]:+.2f} of {forms[k_spl]['cv_gain_per_1000']:+.2f}; the log-odds form more than all of it, excess {ex[k_lo]:+.2f}, "
        f"z {zf(k_lo)}). **The best fit is the share of the last 10 votes** (excess {ex[k_w10]:+.2f}), then the last 5 and last 20; "
        f"adding the cumulative share to the last 5 adds {ex[k_c5] - ex[k_w5]:+.2f}. Kuran's linear threshold-falls-with-the-share "
        f"form (cumulative share, linear) has excess {ex[k_cum]:+.2f} (beyond a null that barely moves, z {zf(k_cum)}, but "
        f"{ex[k_cum] / ex[k_w10]:.0%} of the window's); the spline keeps {ex[k_spl]:+.2f} (z {zf(k_spl)}) and the step at 50% "
        f"{ex[k_step]:+.2f} (z {zf(k_step)}), order-dependence the linear form misses, which may be the recent votes seen through "
        f"the cumulative share; the two-sided (concave) curvature {ex[k_cur]:+.2f} (z {zf(k_cur)}); the vote margin {ex[k_mar]:+.2f}. "
        "Slopes of the spline form by segment (logit scale, observed; they contain the mechanical shape and "
        "are not read): "
        + ", ".join(f"{R['spline']['segments'][i]} {R['spline']['slope'][i]:+.1f}" for i in range(4)) + ".")
    add("")
    add("### 4.2 The participation hazard: the forms compared")
    add("")
    add("Held-out Poisson log-likelihood of each form over the \"turnout + recent rate\" form, with the share of the same form "
        f"fitted to shuffled signs as the null gain ({R.get('B_hforms', 20)} shuffles). Standard errors are across elections.")
    add("")
    rows = []
    for w in HAZARD_WINDOWS:
        for r in hf[w]:
            if r["spec"] in ("turn+rate+s", "turn+rate+s+s2", "turn+rate+bands"):
                nv = hfn[w][r["form"]]
                g_null = float(np.mean(nv)) - [x for x in hf[w] if x["spec"] == "turn+rate"][0]["cv_gain"]
                rows.append([w, r["form"], r["k"], f"{r['cv_vs_rate']:+.0f} ({r['cv_vs_rate_se']:.0f})", f"{g_null:+.0f}", f"{r['cv_vs_rate'] - g_null:+.0f}"])
    L.extend(_t(["window", "form", "params", "gain over turnout+rate (se)", "null gain", "excess"], rows))
    add("The state terms earn their keep against the common-clock-plus-persistence model in every window, and the "
        "ordering among the share forms is small beside the standard errors. The raw curvature is "
        + ("negative in every window" if s2_neg_raw else "not of one sign") + " and its excess over the shuffle null is "
        + ("negative in every window" if s2_neg_ex else "not of one sign") + f" ({s2_txt}; 3.5), beyond the null {s2_where}: "
        + ("saturating, and never convex (Kuran's accelerating bandwagon)." if s2_neg_ex else "no consistent shape."))
    add("")
    add("### 4.3 Mapping to the law's forms")
    add("")
    L.extend(_t(["law's form", "implemented as", "result"],
            [["one-sided monotone F (Granovetter)", "linear in the share", f"sign: excess {ex[k_cum]:+.2f}; participation: gain over turnout+rate in every window"],
             ["Kuran: threshold falls with the share", "linear (sign) / positive curvature (participation)", f"sign: a negligible gain ({ex[k_cum]:+.2f}); participation: " + ("curvature, and its excess over the null, negative in every window" if s2_neg_ex else "curvature excess not of one sign")],
             ["two-sided gate (hump)", "negative curvature / free bands", "sign: curvature excess " + f"{ex[k_cur]:+.2f}" + "; participation: the fall is on the *low* side only"],
             ["recency, not the cumulative share", "share of the last L votes", f"sign: the largest gain (excess {ex[k_w10]:+.2f}; the cumulative share's best form, the spline, {ex[k_spl]:+.2f})"]]))

    # ------------------------------------------------------------------ 5. sigma
    add("## 5. The sign operand sigma in this medium and era")
    add("")
    L.extend(_t(["scale of the law", "measure", "sign of the dependence", "status"],
            [["vote's sign, local (last 5-20 votes)", "controlled logit, election FE, agreement with the recent majority; every year from 2005, all sizes", "+ (co-movement)", "supported; influence vs shock undecided"],
             ["vote's sign, cumulative share", "controlled logit; out-of-sample gain", f"+ below 20 earlier votes; spec-dependent above 40; a small out-of-sample gain (spline {ex[k_spl]:+.2f}, linear {ex[k_cum]:+.2f}, against the window's {ex[k_w10]:+.2f})", "not identified"],
             ["vote's sign, cumulative majority", "agreement vs random order", f"below random order ({(maj['all:cum']['obs'] - maj['all:cum']['null_mean']) * 100:+.1f} points)", "read as non-stationarity (2.2), not as substitutes"],
             ["participation, running support share", "Poisson hazard, shuffle null", "+ and saturating; flat above 85%; present in the first day", "one-sided gate supported (the late-window part partly the closing rule)"],
             ["participation, decisive success", "bands >= 85%, against the path-shuffle null", "no fall (at or above the null)", "upper gate refuted in its path-dependent form; a gate through the final composition is not tested"],
             ["participation, decisive failure", "bands < 70%; stall table", f"falls; process stalls (72 h: {stall[72][0][2]:.0%} vs {stall[72][4][2]:.1%})", "closure, partly institutional"],
             ["participation, late acceleration", "end-window ratio by state", f"deadline bump in every band but the losing ones; contrast below composition; the {late_top} band above it (z {_z(lc[late_top])})", "state-triggered ignition not seen"]]))
    add("So sigma is **+1 as co-movement at the scale of the last few votes, with a short memory, and not -1 anywhere that "
        "survives a second estimator**. `models/00-v0.md` §4.4 carries sigma as a setting operand (since v0.1); for this "
        "setting the reading is: sigma = +1 as an association (the causal sign is not identified: influence and a shared shock "
        "are not separated), the state is a recency window rather than the cumulative share r(t), and the law's two-sided gate "
        "reduces to a lower gate on participation when the tally runs against. The Hong Kong substitutes (L4355) "
        "are not repeated here; the claim that the sign flips with turnout (L4363) is reproduced by the logit on the "
        "cumulative share and contradicted by the detrended model, so it stays open.")
    add("")
    add("## 6. Caveats")
    add("")
    for c in [
        "**Observational.** The shuffle null tests exchangeability of order given composition. It does not separate influence from a shared shock; the one placebo that might (time reversal) is shown on planted data not to. Slow drift within an election would also break exchangeability; the gap profile (no excess agreement of consecutive votes more than four hours apart) argues against drift as the source of the local co-movement, and the detrended estimator (2.2) removes a quadratic trend from the cumulative one.",
        "**A vote is not a riot.** It is a public, consequential, one-shot act on a wiki, cast by editors who can see the page and the tally; voters often give a reason that cites the nominator or an earlier voter (an informal look at the file suggested so; not coded, and the module never reads the comments). The opening votes are plausibly the nominator's circle (the same informal look; tested only indirectly, by dropping the opening hours, 2.4).",
        "**Timestamps** are signature times to the minute, in the file's wall clock; a changed vote carries the time of its last signature; 5% of votes are undated and were dropped (missing at random is assumed). File order within a minute is page order and is not used.",
        "**Election definition.** A candidacy is a (candidate, result, year) group split at 10-day silences; 14 days gives the same results (2.5). An election that stops early is part of the data and is shown as such, not removed.",
        "**Controlling the final outcome** conditions on a post-treatment variable when influence exists: the primary logit understates complements (planted data) and the election-fixed-effect model has a strongly negative mechanical null. Each is read only against its own shuffle.",
        "**Non-stationarity.** Elections open with a run of supports and drift; the cumulative running share partly measures that drift. This is why its sign is spec-dependent and why recency windows fit.",
        "**Turnout and rate coefficients in the hazard have no null** (the shuffle does not move them) and confound popularity with persistence; they are described, not tested.",
        "**Participation counts all votes** (support, oppose and neutral). The law's two-sided gate is stated for the share who have taken one action; side-specific hazards (supporters' arrival against the support share, opposers' against the oppose share) were not fitted, because a sign-specific response cannot be tested against a sign-shuffle null. The lower gate found here is on total participation.",
        "**One site, 2003-2013, English Wikipedia.** The law is not tested beyond it. Years 2003-2004 have too few elections to read (2004: 67).",
        f"**Multiplicity.** {n_cells} cells in 2.1 ({len(bonf_years)} years pass a Bonferroni bar), {m_loc} in the local table ({sum(1 for c in yrs05 + sz if loc[c + ':prior']['z'] >= z_bar)} pass), five turnout bins times two estimators in 2.3, {len(HAZARD_WINDOWS) * 6} hazard share terms, {len(R['sign_forms_obs'])} sign forms, and many specifications elsewhere. The verdict rests on statistics with |z| of 4 or more, on signs that agree across cells and estimators, and on point estimates, not on the marginal cells; a single cell with |z| near 2 (the logit at 40-79 earlier votes, a year like 2013) is not evidence on its own. p-values are the one-sided shuffle p with the +1 correction (smallest possible 1/(B+1)).",
    ]:
        add(f"- {c}")
    add("")
    add("## Reproduce")
    add("")
    add("    cd sim")
    add("    ~/.local/bin/uv run python -m models.crowd_gate_wikirfa report      # 20 to 30 minutes on eight cores; writes results/crowd_gate_wikirfa.md")
    add("    ~/.local/bin/uv run pytest tests/test_crowd_gate_wikirfa.py")
    add("")
    add("The local copy of the data is reused from `sim/data/wiki-rfa/` (fetch only if absent: `python -m models.crowd_gate_wikirfa fetch`, "
        "which refuses a file whose sha256 differs). Every random draw is seeded by (seed, tag, draw), so the numbers do not depend on the number of cores. "
        "Regenerating keeps any hand-written `## Review (date)` section at the end of this file.")
    add("")
    return "\n".join(L)


REVIEW_HEAD = "\n## Review ("


def keep_reviews(text: str, old: str | None) -> str:
    """`text` with the hand-written review sections of `old` (everything from its first '## Review (' heading on)
    appended, so regenerating the numbers does not delete a review of them."""
    i = old.find(REVIEW_HEAD) if old else -1
    return text if i < 0 else text.rstrip("\n") + "\n" + old[i:]


def write_report(R: dict, path: Path | str = RESULTS) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    old = path.read_text(encoding="utf-8") if path.exists() else None
    path.write_text(keep_reviews(format_report(R), old), encoding="utf-8")
    return path


def main(argv: list[str] | None = None) -> None:
    import argparse
    import pickle
    import sys
    import time

    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", choices=["fetch", "report", "format"])
    ap.add_argument("--pickle", help="report: save the raw results here; format: read them from here")
    ap.add_argument("--jobs", type=int, default=8)
    ap.add_argument("--quick", action="store_true", help="small numbers of shuffles (a smoke run, not the published numbers)")
    a = ap.parse_args(argv)
    if a.cmd == "fetch":
        print(fetch())
        return
    if a.cmd == "format":
        R = pickle.load(open(a.pickle, "rb"))
        print(write_report(R))
        return
    t0 = time.time()
    log = lambda s: print(f"[{time.time() - t0:7.1f}s] {s}", file=sys.stderr, flush=True)
    kw = dict(B=40, B_rob=20, B_forms=3, B_haz=20, B_hforms=3) if a.quick else {}
    R = compute_all(n_jobs=a.jobs, log=log, **kw)
    if a.pickle:
        pickle.dump(R, open(a.pickle, "wb"))
    print(write_report(R))


if __name__ == "__main__":
    main()
