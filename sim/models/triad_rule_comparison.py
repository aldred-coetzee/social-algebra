"""Which directed triad rule best predicts the sign of a closing or converting tie?  Formation-ordered, held out.

Prior work: docs/prior-work/106 section 1.2 (Leskovec, Huttenlocher & Kleinberg 2010, "LHK": balance, weak balance,
status, the 16 directed triad types; ledger L4799-L4817, L4850), 104 (Newcomb and Doreian & Krackhardt, "D&K": the
eight ordered-triple types and the first-tie asymmetry, L4481-L4515), 117 sections 3.3-3.4 (the two data sets,
L4561-L4580), 112 section 6.5 (the sign-law tests; test 2, "person terms dominate", is this module's N1), and the
Newcomb run this continues (sim/results/newcomb_n3.md, models/newcomb.py).  Ledger ids are the `id` fields of
docs/ledger.jsonl entries (not always the line number: L0898 is line 1279) and are given as [L....].

THE TEST.  models/00-v0.md section 4.2 (v0.2.1) carries (4.2b) strict balance as a structure theorem, (4.2d) a DIRECTED
LAW (a two-factor product rule on the two ties into the third person, independent of the first tie: D&K's first-tie
partition, the closing tie takes the sign of the second tie, [L4508, L4511, L4490-L4498]) and (4.2e) weak balance as a
depletion; its section 7 says the partition must reproduce against a row-wise sign-shuffle null in a longitudinal explicit-sign
panel and that, if DLL is depleted like LLD, (4.2d) is refuted and the symmetric rule returns.  Five rules compete to predict
the sign of a tie that CLOSES a triad (or, in wiki-RfA, re-signs a tie), with models fitted on the past and scored on the
future: strict balance (the product rule), weak (Davis) balance, the first-tie asymmetric rule (on forward chains: (4.2d)),
LHK's status rule, and a person-propensity baseline.  The static comparison (D&K's eight types against shuffled-sign nulls)
and paired contrasts with a cluster bootstrap are run alongside.

DATA (local use only, never committed; sim/data/README.md has sources, terms and checksums).  Bitcoin OTC and Alpha
(SNAP soc-sign-bitcoin*.csv.gz; Kumar et al. 2016): directed ratings -10..+10 with a Unix time, no pair rated
twice [L4567-L4571].  wiki-RfA (SNAP wiki-RfA.txt.gz; West et al. 2014): votes on adminship requests [L4561-L4564].
The wiki comments (Wikipedia text, CC BY-SA) are skipped line by line and never stored; names become integers on
load and are never written out.  Bitcoin Alpha's timestamps are whole days (one stamp per day, 04:00 or 05:00 UTC;
1,647 distinct values for 24,186 ratings), so "earlier" means an earlier day there; OTC's are unique and sub-second.

OBJECTS.
 * Tie: a signed directed rating u -> v (+1 / -1; zero ratings and, by default, neutral votes are not ties).
   A closing tie is the first tie between u and v in EITHER direction (the unordered pair's first; 117's
   convention [L4572-L4573]) with at least one common neighbour w visible before it.  A converting tie
   (wiki-RfA) is a re-vote on a candidate the voter had voted on at an earlier candidacy; the target is the new sign.
 * Visible: a tie is context for a target only if its visibility time is STRICTLY earlier than the target's cut.
   Bitcoin: the rating time.  wiki-RfA, primary: cut = start of the target's election, visibility = end of the
   election that holds the context vote, so the crowd's concurrent votes are never context.  The election result
   (RES) is never a feature.  Hence a target's features are a function of the ties visible before it, not of its own
   sign, of any later tie or of any later label (tests/test_triad_rule_comparison.py checks this by deletion and
   by flipping signs).
 * Context triad: a common neighbour w with the ties u~w and w~v; 16 directed types [F|B][F|B][p|m][p|m] (F: u -> w,
   B: w -> u; F: w -> v, B: v -> w; signs) [L4814], one instance per existing directed tie pair, and a direction-free
   pair-level sign per side (+ if a positive tie one way and a positive or no tie the other, - analogously, else 0)
   [L4812], one undirected vote per common neighbour.  Each instance also records which of the two ties was formed
   first (u~w, w~v or simultaneous).

RULES (a table over context types; label +, -, or silent).  Strict balance: the product of the two pair-level signs
[L4800].  Weak (Davis) balance: the same, silent on (-,-) [L4815].  Status: orient the path u -> w -> v, flip a sign
whose edge is reversed, predict sign(s1 + s2), silent when they cancel (8 of 16 types) [L4801, L4196].  First-tie
asymmetric: balance, except that in a forward chain u -> w -> v (D&K's ordered triple (i->j)(j->k)(i->k)) a negative
FIRST tie u -> w reverses the balance prediction [L4508].  NOTE (derived here, tests/): reversing the product when
s1 < 0 gives s2, so on a forward chain this rule predicts the sign of the SECOND tie w -> v in all four cells; that is
why 'copy incoming', 'first-tie on all forms' and 'first-tie by formation order' (copy the later-formed tie) are run
beside it.  Conjunction: positive only if both ties are positive (LHK's learned forward-chain pattern [L4811], sa).
Person propensity: LHK's four signed degrees, the sender's earlier out-votes (+, -) and the receiver's earlier
in-votes (+, -) [L4813], log(1 + count).

MODELS AND METRICS.  Every model is a ridge-1 logistic regression on its feature blocks, fitted on the training
ties only; a rule enters as log(1 + votes for +) and log(1 + votes for -), so a rule is judged by how well its
labelling sorts the closing signs.  The rule's OWN hard prediction (majority of its votes, ties and silence to +,
the convention of 106's recount of LHK [L4817]) is scored beside it.  Held-out log-loss, accuracy, balanced accuracy (threshold at the
training positive share) and AUC, on the natural class mix.  Intervals: cluster bootstrap (raters or ratees;
voters or elections), the scheme with the larger standard error; paired differences of log-loss for contrasts.

NULLS.  N0: the training positive share, and an adaptive 'recent rate' (smoothed positive share of the last 500
visible ties).  N1: the person-propensity model (a triad rule is only a triad effect if it beats or adds to it).
N2: for 'do the triad terms add to the person terms', the rows of the added features are permuted among ties of
equal embeddedness, in the training and the test set, and the model is refitted (anti-conservative where the refit
overfits: a feature that duplicates the person terms overfits less than a shuffled one, so the size of an addition is
judged by the paired bootstrap of held-out log-loss, not by this p).  N3: for the static eight-type pattern, the closing
signs are shuffled within sender (the formation-ordered analogue of the Newcomb run's row-wise null [L4485]: D&K's null
redraws every tie of a row, here only the closing sign moves and the context ties stay as they were), within sender and
calendar year, and within receiver (the control the Newcomb run lacked: reception held fixed); the pool is the closing
ties that have a forward-chain context, each counted once (split over its forward-chain cells) or once per triad.

FIXED IN THE DESIGN BEFORE THE FIRST RUN OF THE PRIMARY SPLIT (2026-11-01; the rules, models, split and contrasts were
not changed in response to its results except as listed in the next paragraph).  Primary protocol: chronological 70/30 split of all
target ties by cut time; closing ties with >= 1 common neighbour; Bitcoin signs = sign of the rating, wiki-RfA
neutral votes dropped, election-start horizon; ridge 1; the five rules and the person baseline; held-out
log-loss as the headline; bootstrap B = 2000.  The contrasts of interest: each rule against the base rate and
against the person baseline; the first-tie rule against strict balance, weak balance and status; the 16 types
added to the person terms.  The replication criterion for the first-tie asymmetry: D&K's eight directions (LLL,
LDD, DLL, DDD above the sender-shuffle null; LLD, LDL, DLD, DDL below) reproduced, in particular DLL above and DLD
below, and the first-tie rule out-predicting balance in time; section 7 of v0.2.1 puts the refutation the other way
round: DLL depleted like LLD refutes (4.2d) (this criterion was written down after an exploratory look at the
sixteen-cell tables, so it is a stated criterion, not a blind prediction).  Variations (all run, none dropped): embeddedness
thresholds, sign recodes, target sets, split fraction, frozen snapshot, ridge, wiki-RfA horizon, alternative rule
forms.  Seeds are fixed (SEED); the report is deterministic.

ADDED AFTER THE FIRST LOOK AT RESULTS (post hoc, reported anyway).  (1) The Bitcoin test periods have a different
share of negative ratings from their training periods (OTC 27.6% against 13.5%), so the 'recent rate' baseline and a
rolling-origin evaluation (every block predicted by models fitted on everything earlier) were added; the single split
stays the headline.  (2) The static comparison was seen to depend on sender propensity, so the receiver-shuffle null
and the person-adjusted coefficients (ff_coefficients) were added.  (3) The Newcomb reception re-read
(newcomb_reception_check): the D&K pattern is the partition 'closing sign = second-tie sign' from the second wave on,
and shrinks to chance under a column-wise (reception-holding) null.  (4) The wiki-RfA windows that the file
carries twice (complete copies under the opposite result label) were merged after the data README flagged them.
(5) The shuffle pool of the static comparison was first every closing tie; it was corrected to the closing ties that
have a forward-chain context (a sender's other ties do not carry the same sign mix, and including them made every
cell look depleted on wiki-RfA), and the event-normalised weighting was added beside the instance weighting after
seeing that instance weights tie embeddedness to sign.  The first version's wiki-RfA reading ("4/8") was wrong and
is not reported.  (6) The 'where the rules disagree' subset (closing ties with a negative-first-tie forward chain) and
the A^2 forward-chain rule (v0.1 (4.2a)) were added as sharper tests of the same contrast.

CHANGED IN REVIEW (2026-11-01; the results file's '## Review' section has the detail).  No rule, model, split, null or
seed changed.  The variation win counts (render_winners, the verdict) count the pre-specified configuration once: it
recurs as the reference row of the recode, split, ridge and horizon tables (PRIMARY_REPEAT_LABELS).  The verdict lists
every variation configuration in which the first-tie rule beats strict balance by its interval (ft_ahead_rows), where
it had named one.  Status and the A^2 sign are 'behind balance', not 'refuted': each beats the base rate on some site.
(4.2e) is scoped by the all-negative cell, which goes strict balance's way on OTC.  The person-adjusted coefficients use
B_COEF = 400 cluster-bootstrap refits (100 before), and their B is printed.  Wording and ledger citations corrected.
`report` now keeps a '## Review' section appended to the results file instead of overwriting it (keep_reviews).

CAVEATS that bound every reading: signs are ratings and public votes, not liking; Bitcoin Alpha's order is
daily; closing ties with a common neighbour are a minority of the ties; a rank recode (Newcomb) and a rating or a
vote are different instruments with no bridge (v0.2 section 0.6, rule 7).
"""
from __future__ import annotations

import calendar
import gzip
import hashlib
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from scipy.special import expit
from scipy.stats import rankdata

# ------------------------------------------------------------------ data locations and checksums

SIM_DIR = Path(__file__).resolve().parents[1]
BITCOIN_DIR = SIM_DIR / "data" / "bitcoin"
BITCOIN_FILES = {"otc": "soc-sign-bitcoinotc.csv.gz", "alpha": "soc-sign-bitcoinalpha.csv.gz"}
BITCOIN_SHA256 = {
    "otc": "6424ac981dad3a019f697fc1b9fcd85c19d8d9f039797758e9ffb6fea100c373",
    "alpha": "3a178611b9c2f39c9a0dc75936f28557317f1733319b49da4838232b3757cd76",
}
WIKI_FILE = SIM_DIR / "data" / "wiki-rfa" / "wiki-RfA.txt.gz"
WIKI_SHA256 = "88d53196fb2564a2e20286dbba818832f718cc352bb181a2101d23d2556f0862"
RESULTS_FILE = SIM_DIR / "results" / "triad_rule_comparison.md"


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def _need(path: Path, sha: str, what: str) -> None:
    if not path.exists():
        raise FileNotFoundError(
            f"{path} is missing: {what} is local-use-only and is not in the repo "
            "(sim/data/README.md has the source and terms); it is not fetched automatically."
        )
    if sha256_of(path) != sha:
        raise ValueError(f"{path} does not match the recorded sha256 {sha}")


# ------------------------------------------------------------------ the sixteen directed triad types [L4814]
# For a target tie u -> v and a common neighbour w:
#   d1 = F (u -> w) or B (w -> u);  d2 = F (w -> v) or B (v -> w);  s1, s2 the two signs.
# Type index = ((d1 * 2 + d2) * 2 + [s1 < 0]) * 2 + [s2 < 0]; names are [F|B][F|B][p|m][p|m] as in LHK.

TYPE_D1 = np.array([(t >> 3) & 1 for t in range(16)])
TYPE_D2 = np.array([(t >> 2) & 1 for t in range(16)])
TYPE_S1 = np.array([1 if ((t >> 1) & 1) == 0 else -1 for t in range(16)])
TYPE_S2 = np.array([1 if (t & 1) == 0 else -1 for t in range(16)])
TYPE_NAMES = tuple(
    "FB"[TYPE_D1[t]] + "FB"[TYPE_D2[t]] + "pm"[(t >> 1) & 1] + "pm"[t & 1] for t in range(16)
)
UND_NAMES = ("pp", "pm", "mp", "mm")  # undirected (direction-free) triad types [L4816]
ORDER_NAMES = ("uw_first", "wv_first", "simultaneous")  # which context tie was formed first


def type_index(d1: int, d2: int, s1: int, s2: int) -> int:
    return ((d1 * 2 + d2) * 2 + (0 if s1 > 0 else 1)) * 2 + (0 if s2 > 0 else 1)


# ------------------------------------------------------------------ the rules as label tables
# A rule maps every context type to +1 (predicts a positive closing tie), -1 (negative) or 0 (silent).
# Directed rules are tables of shape (16, 3) over (type, formation-order); undirected ones are (4,).


def _directed_table(fn) -> np.ndarray:
    L = np.zeros((16, 3), dtype=np.int8)
    for t in range(16):
        for o in range(3):
            L[t, o] = fn(int(TYPE_D1[t]), int(TYPE_D2[t]), int(TYPE_S1[t]), int(TYPE_S2[t]), o)
    return L


def _status(d1, d2, s1, s2, o):
    # orient the path u -> w -> v, flipping a sign when its edge is reversed [L4801, L4196, L5422]
    a = s1 if d1 == 0 else -s1
    b = s2 if d2 == 0 else -s2
    return a if a == b else 0


def _first_tie_ff(d1, d2, s1, s2, o):
    # D&K's types are the transitive triples (i->j)(j->k)(i->k): FF here.  Balance, except that when
    # the FIRST tie (u -> w) is negative the balance prediction is reversed [L4508, L4511].
    bal = s1 * s2
    if d1 == 0 and d2 == 0:
        return bal if s1 > 0 else -bal
    return bal


def _first_tie_ff_only(d1, d2, s1, s2, o):
    return _first_tie_ff(d1, d2, s1, s2, o) if (d1 == 0 and d2 == 0) else 0


def _first_tie_all(d1, d2, s1, s2, o):
    bal = s1 * s2
    return bal if s1 > 0 else -bal


def _first_tie_time(d1, d2, s1, s2, o):
    # the FIRST-FORMED context tie, not the first in chain order
    bal = s1 * s2
    if o == 0:
        return bal if s1 > 0 else -bal
    if o == 1:
        return bal if s2 > 0 else -bal
    return 0


def _conjunction(d1, d2, s1, s2, o):
    # the pattern LHK's logistic fit learned on forward chains: positive only if both links are [L4811, sa]
    return 1 if (s1 > 0 and s2 > 0) else -1


def _copy_incoming(d1, d2, s1, s2, o):
    return s2 if d2 == 0 else 0


def _balance_directed(d1, d2, s1, s2, o):
    return s1 * s2


def _weak_directed(d1, d2, s1, s2, o):
    return 0 if (s1 < 0 and s2 < 0) else s1 * s2


def _a_squared(d1, d2, s1, s2, o):
    # v0.1 (4.2a) dA/dt = A^2 [L0898]: the sign of a new tie u -> v is the sign of (A^2)_uv = sum_w a_uw a_wv, i.e. the
    # net vote of the forward chains u -> w -> v alone, each voting the product of its two signs
    return s1 * s2 if (d1 == 0 and d2 == 0) else 0


DIRECTED_RULES: dict[str, np.ndarray] = {
    "status": _directed_table(_status),
    "first_tie": _directed_table(_first_tie_ff),  # primary reading of the Newcomb first-tie rule
    "first_tie_ffonly": _directed_table(_first_tie_ff_only),
    "first_tie_all": _directed_table(_first_tie_all),
    "first_tie_time": _directed_table(_first_tie_time),
    "conjunction": _directed_table(_conjunction),
    "copy_incoming": _directed_table(_copy_incoming),
    "strict_inst": _directed_table(_balance_directed),
    "weak_inst": _directed_table(_weak_directed),
    "a_squared": _directed_table(_a_squared),
}
UNDIRECTED_RULES: dict[str, np.ndarray] = {
    "strict": np.array([1, -1, -1, 1], dtype=np.int8),  # product rule [L4800]
    "weak": np.array([1, -1, -1, 0], dtype=np.int8),  # Davis: silent on (-,-) [L4815]
}
RULE_LABELS = {
    "strict": "strict balance (product)",
    "weak": "weak (Davis) balance",
    "first_tie": "first-tie asymmetric",
    "status": "status (LHK)",
    "conjunction": "conjunction (LHK learned)",
    "copy_incoming": "copy the incoming tie",
    "first_tie_ffonly": "first-tie, FF only",
    "first_tie_all": "first-tie, all forms",
    "first_tie_time": "first-tie, time-first",
    "strict_inst": "strict, per directed instance",
    "weak_inst": "weak, per directed instance",
    "a_squared": "A^2 sign (forward chains only)",
}
PRIMARY_RULES = ("strict", "weak", "first_tie", "status")


# ------------------------------------------------------------------ tie tables


@dataclass
class TieTable:
    """Signed directed ties, one row each.  A row is a context record (visible to targets whose cut is
    after t_vis) and, if is_target, a target tie predicted from the state at its own cut t_cut.
    t_form orders the two context ties of an instance (first-formed rule)."""

    name: str
    u: np.ndarray
    v: np.ndarray
    s: np.ndarray  # int8, +1 / -1
    t_form: np.ndarray
    t_vis: np.ndarray
    t_cut: np.ndarray
    is_target: np.ndarray
    g: np.ndarray  # cluster id of the group (election / timestamp) for the bootstrap
    n_nodes: int
    info: dict = field(default_factory=dict)

    @property
    def n(self) -> int:
        return len(self.u)


def _dense(*arrays: np.ndarray) -> tuple[list[np.ndarray], int]:
    """Relabel node ids to 0..N-1 over the union of the arrays."""
    allv = np.concatenate(arrays)
    uniq, inv = np.unique(allv, return_inverse=True)
    out, k = [], 0
    for a in arrays:
        out.append(inv[k : k + len(a)].astype(np.int64))
        k += len(a)
    return out, len(uniq)


def load_bitcoin_raw(site: str, verify: bool = True):
    """(source, target, rating, time) arrays in file order.  Counts: L4568 (OTC), L4570 (Alpha)."""
    path = BITCOIN_DIR / BITCOIN_FILES[site]
    if verify:
        _need(path, BITCOIN_SHA256[site], f"the Bitcoin {site.upper()} rating file")
    elif not path.exists():
        raise FileNotFoundError(path)
    src, tgt, rat, tim = [], [], [], []
    with gzip.open(path, "rt", encoding="ascii") as f:
        for line in f:
            a = line.strip().split(",")
            if len(a) != 4:
                continue
            src.append(int(a[0]))
            tgt.append(int(a[1]))
            rat.append(int(a[2]))
            tim.append(float(a[3]))
    return np.array(src), np.array(tgt), np.array(rat), np.array(tim)


BITCOIN_RECODES = {
    # name: (smallest rating counted +, largest rating counted -).  Ratings in between are dropped
    # from the graph altogether (neither target nor context).  A modelling choice (module docstring).
    "all": (1, -1),
    "drop+1": (2, -1),
    "drop-1..-4": (1, -5),
    "drop+1,-1..-4": (2, -5),
}


def bitcoin_ties(site: str, recode: str = "all", verify: bool = True) -> TieTable:
    src, tgt, rat, tim = load_bitcoin_raw(site, verify)
    keep = src != tgt
    src, tgt, rat, tim = src[keep], tgt[keep], rat[keep], tim[keep]
    order = np.argsort(tim, kind="stable")  # Alpha's file is not time-sorted
    src, tgt, rat, tim = src[order], tgt[order], rat[order], tim[order]
    pos_min, neg_max = BITCOIN_RECODES[recode]
    s = np.where(rat >= pos_min, 1, np.where(rat <= neg_max, -1, 0)).astype(np.int8)
    keep = s != 0
    src, tgt, s, tim = src[keep], tgt[keep], s[keep], tim[keep]
    (u, v), n_nodes = _dense(src, tgt)
    _, g = np.unique(tim, return_inverse=True)
    return TieTable(
        name=f"bitcoin-{site}", u=u, v=v, s=s, t_form=tim, t_vis=tim, t_cut=tim.copy(),
        is_target=np.ones(len(u), dtype=bool), g=g.astype(np.int64), n_nodes=n_nodes,
        info={"recode": recode, "distinct_times": int(len(np.unique(tim)))},
    )


# ------------------------------------------------------------------ wiki-RfA

_MONTHS = {m: i + 1 for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}
_DATE_RE = re.compile(r"^\s*(\d{1,2}):(\d{2}),\s*(\d{1,2})\s+([A-Za-z]+)\s+(\d{4})\s*$")


def parse_wiki_date(text: str) -> float | None:
    """'23:13, 19 April 2013' -> UTC seconds, or None for a missing or unreadable date.  Month names
    are read by their first three letters (the file also has 'Jun', 'Oct'); typos such as 'Mya' fail."""
    m = _DATE_RE.match(text or "")
    if not m:
        return None
    hh, mi, dd, mon, yy = m.groups()
    mon = _MONTHS.get(mon[:3].lower())
    if mon is None:
        return None
    hh, mi, dd, yy = int(hh), int(mi), int(dd), int(yy)
    if not (0 <= hh <= 23 and 0 <= mi <= 59 and 1 <= dd <= 31 and 1990 <= yy <= 2030):
        return None
    try:
        return float(calendar.timegm((yy, mon, dd, hh, mi, 0)))
    except (ValueError, OverflowError):
        return None


def load_wiki_raw(verify: bool = True) -> dict:
    """Parse wiki-RfA.txt.gz into arrays.  The TXT field (Wikipedia text, CC BY-SA) is skipped line by
    line and never stored.  Voter and candidate names are interned to integers and not returned.
    Returns dict of arrays in file order; the votes of one election are contiguous in the file."""
    if verify:
        _need(WIKI_FILE, WIKI_SHA256, "the wiki-RfA vote file")
    intern: dict[str, int] = {}
    src, tgt, vot, res, tim = [], [], [], [], []
    block, blk_key, blk_id = [], None, -1
    cur: dict[str, str] = {}

    def flush():
        nonlocal blk_key, blk_id
        if "SRC" not in cur or "TGT" not in cur or "VOT" not in cur:
            return
        s_name = cur["SRC"]
        t_name = cur["TGT"]
        key = (t_name, cur.get("RES"), cur.get("YEA"))
        if key != blk_key:
            blk_key = key
            blk_id += 1
        src.append(-1 if s_name == "" else intern.setdefault(s_name, len(intern)))
        tgt.append(intern.setdefault(t_name, len(intern)))
        vot.append(int(cur["VOT"]))
        res.append(int(cur.get("RES", "0")))
        d = parse_wiki_date(cur.get("DAT", ""))
        tim.append(np.nan if d is None else d)
        block.append(blk_id)

    with gzip.open(WIKI_FILE, "rt", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line:
                if cur:
                    flush()
                    cur = {}
                continue
            k, _, val = line.partition(":")
            if k == "TXT":
                continue
            if k in ("SRC", "TGT", "VOT", "RES", "YEA", "DAT"):
                cur[k] = val
        if cur:
            flush()
    return {
        "src": np.array(src), "tgt": np.array(tgt), "vot": np.array(vot, dtype=np.int8),
        "res": np.array(res, dtype=np.int8), "time": np.array(tim), "block": np.array(block),
        "n_names": len(intern),
    }


GAP_DAYS = 14.0  # votes of one block further apart than this belong to different candidacies
MIN_ELECTION_VOTES = 10  # a further cluster smaller than this is a stray, dropped
MIN_MAIN_VOTES = 3  # a block whose largest dated cluster is smaller than this is dropped
DAY = 86400.0


def wiki_elections(raw: dict) -> dict:
    """Assign each vote to an election window.  Votes of one candidacy are contiguous in the file
    (a 'block' of equal candidate, result, year).  Within a block the dated votes are split wherever
    consecutive sorted times are more than GAP_DAYS apart.  The largest cluster is an election
    (if it has at least MIN_MAIN_VOTES dated votes); any further cluster of at least MIN_ELECTION_VOTES
    is a second candidacy of the same candidate and result in one year and is another election;
    smaller further clusters are strays (mis-dated or late signatures) and are dropped entirely.  A
    vote with no readable date joins the election when the block has exactly one, and is dropped when
    it has two or none.  Window = [min, max] of the cluster's dated votes.
    Returns arrays election (int, -1 = dropped), e_start, e_end (per election)."""
    block, tim = raw["block"], raw["time"]
    n = len(block)
    election = np.full(n, -1, dtype=np.int64)
    starts, ends = [], []
    cut = np.flatnonzero(np.diff(block)) + 1
    bounds = np.concatenate([[0], cut, [n]])
    n_multi = 0
    for a, b in zip(bounds[:-1], bounds[1:]):
        idx = np.arange(a, b)
        ok = ~np.isnan(tim[idx])
        if not ok.any():
            continue
        di = idx[ok]
        di = di[np.argsort(tim[di], kind="stable")]
        ts = tim[di]
        brk = np.flatnonzero(np.diff(ts) > GAP_DAYS * DAY) + 1
        clusters = np.split(np.arange(len(di)), brk)
        main = max(range(len(clusters)), key=lambda i: len(clusters[i]))
        if len(clusters[main]) < MIN_MAIN_VOTES:
            continue
        chosen = [c for i, c in enumerate(clusters) if i == main or len(c) >= MIN_ELECTION_VOTES]
        first = len(starts)
        for c in chosen:
            eid = len(starts)
            starts.append(float(ts[c[0]]))
            ends.append(float(ts[c[-1]]))
            election[di[c]] = eid
        if len(chosen) == 1:
            election[idx[~ok]] = first
        else:
            n_multi += 1
    starts, ends = np.array(starts), np.array(ends)
    # The file carries some elections twice, under the opposite result label (a complete copy): merge
    # elections of the same candidate with the same window so the copies are one election.
    tgt = raw["tgt"] if "tgt" in raw else np.zeros(n, dtype=np.int64)
    first_row = np.full(len(starts), -1, dtype=np.int64)
    rows = np.flatnonzero(election >= 0)
    first_row[election[rows][::-1]] = rows[::-1]
    canon: dict = {}
    remap = np.arange(len(starts))
    for e in range(len(starts)):
        key = (int(tgt[first_row[e]]) if first_row[e] >= 0 else -1, float(starts[e]), float(ends[e]))
        if key in canon:
            remap[e] = canon[key]
        else:
            canon[key] = e
    n_merged = int((remap != np.arange(len(starts))).sum())
    election = np.where(election >= 0, remap[np.maximum(election, 0)], -1)
    return {"election": election, "e_start": starts, "e_end": ends, "n_multi_blocks": n_multi, "n_merged": n_merged}


def _group_median(groups: np.ndarray, values: np.ndarray, default: np.ndarray) -> np.ndarray:
    """Median of the non-NaN values per group id (0..G-1); groups with none get default[group]."""
    G = len(default)
    out = default.astype(float).copy()
    ok = ~np.isnan(values)
    g, x = groups[ok], values[ok]
    order = np.lexsort((x, g))
    g, x = g[order], x[order]
    if len(g) == 0:
        return out
    starts = np.flatnonzero(np.concatenate([[True], g[1:] != g[:-1]]))
    ends = np.concatenate([starts[1:], [len(g)]])
    for a, b in zip(starts, ends):
        k = b - a
        out[g[a]] = x[a + k // 2] if k % 2 else 0.5 * (x[a + k // 2 - 1] + x[a + k // 2])
    return out


WIKI_NEUTRAL = ("drop", "oppose", "support")


def wiki_ties(neutral: str = "drop", horizon: str = "election", verify: bool = True) -> TieTable:
    """wiki-RfA as a signed directed tie table: voter -> candidate, support +1, oppose -1; neutral
    votes dropped (primary), or coded -1 or +1 (recodes).  horizon='election' (primary): a vote is
    predicted from the ties of elections that ended before its election STARTED, so the network is the
    one the voter walked into and the crowd's concurrent votes are excluded.  horizon='vote': a dated
    vote is predicted from every dated vote strictly earlier (minute resolution), within the election
    too (the herding setting); undated votes are not targets and become visible at their election's end.
    Self votes and votes with no named voter are dropped; a voter's several votes in one election are
    collapsed to the last one."""
    if neutral not in WIKI_NEUTRAL or horizon not in ("election", "vote"):
        raise ValueError("bad option")
    raw = load_wiki_raw(verify)
    el = wiki_elections(raw)
    election = el["election"]
    keep = (election >= 0) & (raw["src"] >= 0) & (raw["src"] != raw["tgt"])
    vot = raw["vot"].astype(np.int64)
    if neutral == "oppose":
        vot = np.where(vot == 0, -1, vot)
    elif neutral == "support":
        vot = np.where(vot == 0, 1, vot)
    keep &= vot != 0
    idx = np.flatnonzero(keep)
    src, tgt, s, tim, ele = raw["src"][idx], raw["tgt"][idx], vot[idx].astype(np.int8), raw["time"][idx], election[idx]
    # collapse a voter's repeated votes within one election to the last (dated: latest time, else file order)
    key = ele.astype(np.int64) * (raw["n_names"] + 1) + src
    tsort = np.where(np.isnan(tim), -np.inf, tim)
    order = np.lexsort((np.arange(len(key)), tsort, key))  # by key, then time, then file order
    key_s = key[order]
    last = np.ones(len(order), dtype=bool)
    last[:-1] = key_s[1:] != key_s[:-1]
    sel = order[last]
    sel.sort()
    src, tgt, s, tim, ele = src[sel], tgt[sel], s[sel], tim[sel], ele[sel]
    e_start, e_end = el["e_start"][ele], el["e_end"][ele]
    # a vote with no time is placed at the median dated time of its election
    med = _group_median(ele, tim, el["e_start"])
    t_form = np.where(np.isnan(tim), med[ele], tim)
    dated = ~np.isnan(tim)
    if horizon == "election":
        t_vis, t_cut, is_t = e_end, e_start, np.ones(len(src), dtype=bool)
    else:
        t_vis = np.where(dated, tim, e_end)
        t_cut = np.where(dated, tim, e_end)
        is_t = dated.copy()
    order = np.argsort(t_vis, kind="stable")
    (u, v), n_nodes = _dense(src, tgt)
    tt = TieTable(
        name="wiki-rfa", u=u[order], v=v[order], s=s[order], t_form=t_form[order], t_vis=t_vis[order],
        t_cut=t_cut[order], is_target=is_t[order], g=ele[order].astype(np.int64), n_nodes=n_nodes,
        info={
            "neutral": neutral, "horizon": horizon, "n_elections": int(len(np.unique(ele))),
            "n_multi_blocks": el["n_multi_blocks"], "n_merged": el["n_merged"], "n_date_dropped": int((election < 0).sum()), "votes_kept": int(len(src)),
            "votes_in_file": int(len(raw["src"])),
        },
    )
    return tt


# ------------------------------------------------------------------ the event engine


@dataclass
class Events:
    """One row per target tie, in order of its cut time.  Everything about a row is computed from ties
    visible STRICTLY before the row's cut (t_vis < t_cut), never from the row's own sign or any later tie.
      C   (m, 48)  directed triad-instance counts [type * 3 + formation order] (type order TYPE_NAMES)
      U   (m, 4)   undirected pair-level triad counts (UND_NAMES), one vote per common neighbour [L4812]
      deg (m, 4)   visible out-votes (+, -) of u and in-votes (+, -) of v
      emb          number of common neighbours (distinct third parties tied to both u and v)
      prev, recip  sign of a visible u->v / v->u tie (0 = none)
      recent       smoothed positive share of the last RECENT_K visible ties: an adaptive base rate
    """

    name: str
    idx: np.ndarray
    u: np.ndarray
    v: np.ndarray
    y: np.ndarray  # 1 = positive, 0 = negative
    t: np.ndarray  # the true cut time (used for the chronological split)
    g: np.ndarray
    C: np.ndarray
    U: np.ndarray
    deg: np.ndarray
    emb: np.ndarray
    prev: np.ndarray
    recip: np.ndarray
    recent: np.ndarray
    n_nodes: int
    info: dict = field(default_factory=dict)

    @property
    def m(self) -> int:
        return len(self.y)

    @property
    def C16(self) -> np.ndarray:
        return self.C.reshape(self.m, 16, 3).sum(axis=2)

    @property
    def pair_first(self) -> np.ndarray:
        """No tie in either direction between u and v was visible: the unordered pair's first tie."""
        return (self.prev == 0) & (self.recip == 0)

    def subset(self, mask: np.ndarray) -> "Events":
        mask = np.asarray(mask)
        return Events(
            self.name, self.idx[mask], self.u[mask], self.v[mask], self.y[mask], self.t[mask], self.g[mask],
            self.C[mask], self.U[mask], self.deg[mask], self.emb[mask], self.prev[mask], self.recip[mask],
            self.recent[mask], self.n_nodes, dict(self.info),
        )


RECENT_K = 500  # window of the adaptive base rate (fixed before any result)


def build_events(tt: TieTable, freeze_at: float | None = None) -> Events:
    """Sweep the ties in time order and, for every target, read the triad context off the state of the
    graph as it was at the target's cut.  Records with t_vis < cut are in the state; ties of the same
    group or the same instant are never (strict inequality), so the construction cannot use a tie
    that is concurrent with, or later than, the target.  freeze_at: targets are given the snapshot of
    min(cut, freeze_at), i.e. the graph frozen at that time (no test-period ties as context)."""
    n = tt.n
    rec_order = np.argsort(tt.t_vis, kind="stable")
    tvis_sorted = tt.t_vis[rec_order]
    tgt = np.flatnonzero(tt.is_target)
    cut_eff = tt.t_cut[tgt] if freeze_at is None else np.minimum(tt.t_cut[tgt], freeze_at)
    o = np.argsort(cut_eff, kind="stable")
    tgt, cut_eff = tgt[o], cut_eff[o]
    m = len(tgt)

    u_l, v_l, s_l, tf_l = tt.u.tolist(), tt.v.tolist(), tt.s.tolist(), tt.t_form.tolist()
    nbr: list[dict] = [dict() for _ in range(tt.n_nodes)]
    outp = [0] * tt.n_nodes
    outn = [0] * tt.n_nodes
    inp = [0] * tt.n_nodes
    inn = [0] * tt.n_nodes

    C = np.zeros((m, 48), dtype=np.int16)
    U = np.zeros((m, 4), dtype=np.int16)
    deg = np.zeros((m, 4), dtype=np.int32)
    emb = np.zeros(m, dtype=np.int32)
    prev = np.zeros(m, dtype=np.int8)
    recip = np.zeros(m, dtype=np.int8)
    recent = np.full(m, 0.5)
    cumpos = np.concatenate([[0], np.cumsum(tt.s[rec_order] > 0)])

    def add(r: int) -> None:
        a, b, sg, tf = u_l[r], v_l[r], s_l[r], tf_l[r]
        na, nb = nbr[a], nbr[b]
        ea = na.get(b)
        if ea is None:
            ea = na[b] = [0, 0.0, 0, 0.0]
            nb[a] = [0, 0.0, 0, 0.0]
        eb = nb[a]
        ea[0], ea[1] = sg, tf  # from a's side: out (a -> b)
        eb[2], eb[3] = sg, tf  # from b's side: in  (a -> b)
        if sg > 0:
            outp[a] += 1
            inp[b] += 1
        else:
            outn[a] += 1
            inn[b] += 1

    p = 0
    i = 0
    tgt_l = tgt.tolist()
    cut_l = cut_eff.tolist()
    while i < m:
        c = cut_l[i]
        j = i
        while j < m and cut_l[j] == c:
            j += 1
        while p < n and tvis_sorted[p] < c:
            add(int(rec_order[p]))
            p += 1
        lo = max(0, p - RECENT_K)
        recent[i:j] = (cumpos[p] - cumpos[lo] + 1.0) / ((p - lo) + 2.0)
        for k in range(i, j):
            r = tgt_l[k]
            u, v = u_l[r], v_l[r]
            Nu, Nv = nbr[u], nbr[v]
            deg[k, 0], deg[k, 1], deg[k, 2], deg[k, 3] = outp[u], outn[u], inp[v], inn[v]
            e_uv = Nu.get(v)
            if e_uv is not None:
                prev[k] = e_uv[0]
                recip[k] = e_uv[2]
            if not Nu or not Nv:
                continue
            common = Nu.keys() & Nv.keys()
            emb[k] = len(common)
            cnt = [0] * 48
            und = [0, 0, 0, 0]
            for w in common:
                eu, ev = Nu[w], Nv[w]
                # pair-level direction-free signs [L4812]
                a0, a2 = eu[0], eu[2]
                su = a0 if a2 == 0 else (a2 if a0 == 0 else (a0 if a0 == a2 else 0))
                b0, b2 = ev[0], ev[2]
                sv = b0 if b2 == 0 else (b2 if b0 == 0 else (b0 if b0 == b2 else 0))
                if su and sv:
                    und[(0 if su > 0 else 1) * 2 + (0 if sv > 0 else 1)] += 1
                # directed instances: first tie F (u -> w) / B (w -> u); second tie F (w -> v) / B (v -> w)
                for d1 in (0, 1):
                    if d1 == 0:
                        s1, t1 = eu[0], eu[1]
                    else:
                        s1, t1 = eu[2], eu[3]
                    if s1 == 0:
                        continue
                    for d2 in (0, 1):
                        if d2 == 0:
                            s2, t2 = ev[2], ev[3]
                        else:
                            s2, t2 = ev[0], ev[1]
                        if s2 == 0:
                            continue
                        typ = ((d1 * 2 + d2) * 2 + (0 if s1 > 0 else 1)) * 2 + (0 if s2 > 0 else 1)
                        o3 = 0 if t1 < t2 else (1 if t1 > t2 else 2)
                        cnt[typ * 3 + o3] += 1
            C[k] = cnt
            U[k] = und
        i = j
    return Events(
        name=tt.name, idx=tgt, u=tt.u[tgt], v=tt.v[tgt], y=(tt.s[tgt] > 0).astype(np.int8), t=tt.t_cut[tgt],
        g=tt.g[tgt], C=C, U=U, deg=deg, emb=emb, prev=prev, recip=recip, recent=recent, n_nodes=tt.n_nodes,
        info={**tt.info, "freeze_at": freeze_at},
    )


def brute_force_context(tt: TieTable, k: int) -> tuple[int, np.ndarray, np.ndarray]:
    """Slow reference for ONE target (row k of the TieTable): recount the context from scratch by
    scanning every record, with the same strict-visibility rule.  Used by the tests to check the sweep.
    Returns (embeddedness, C (48,), U (4,)); for repeated ties the latest visible one (by t_vis, then
    file order) stands, which is what the sweep does."""
    cut = tt.t_cut[k]
    vis = np.flatnonzero(tt.t_vis < cut)
    vis = vis[np.argsort(tt.t_vis[vis], kind="stable")]
    state: dict[tuple[int, int], tuple[int, float]] = {}
    for r in vis:
        state[(int(tt.u[r]), int(tt.v[r]))] = (int(tt.s[r]), float(tt.t_form[r]))
    u, v = int(tt.u[k]), int(tt.v[k])
    nodes = {a for (a, b) in state} | {b for (a, b) in state}
    C = np.zeros(48, dtype=np.int64)
    Uc = np.zeros(4, dtype=np.int64)
    e = 0
    for w in nodes:
        if w == u or w == v:
            continue
        uw, wu = state.get((u, w)), state.get((w, u))
        vw, wv = state.get((v, w)), state.get((w, v))
        if not (uw or wu) or not (vw or wv):
            continue
        e += 1

        def sb(x, y):
            a = x[0] if x else 0
            b = y[0] if y else 0
            return a if b == 0 else (b if a == 0 else (a if a == b else 0))

        su, sv = sb(uw, wu), sb(wv, vw)
        if su and sv:
            Uc[(0 if su > 0 else 1) * 2 + (0 if sv > 0 else 1)] += 1
        for d1, first in ((0, uw), (1, wu)):
            if not first:
                continue
            for d2, second in ((0, wv), (1, vw)):
                if not second:
                    continue
                typ = type_index(d1, d2, first[0], second[0])
                t1, t2 = first[1], second[1]
                C[typ * 3 + (0 if t1 < t2 else (1 if t1 > t2 else 2))] += 1
    return e, C, Uc


# ------------------------------------------------------------------ rule counts and own predictions


def rule_counts(ev: Events, rule: str) -> tuple[np.ndarray, np.ndarray]:
    """Number of context triads in which the rule predicts + and -, per event.  Balance rules count one
    vote per common neighbour on the undirected pair-level signs (U); the others count directed
    instances (C), as LHK do for their 16 types [L4814]."""
    if rule in UNDIRECTED_RULES:
        L = UNDIRECTED_RULES[rule]
        return ev.U @ (L == 1).astype(np.int64), ev.U @ (L == -1).astype(np.int64)
    L = DIRECTED_RULES[rule].reshape(48)
    return ev.C @ (L == 1).astype(np.int64), ev.C @ (L == -1).astype(np.int64)


def rule_prediction(ev: Events, rule: str) -> tuple[np.ndarray, np.ndarray]:
    """The rule's own hard prediction (1 = positive) and whether it voted at all.  Majority of its
    votes; a tie, including no vote, goes to + (LHK's convention, L4817, and the majority class)."""
    npl, nmi = rule_counts(ev, rule)
    return (nmi <= npl).astype(np.int8), (npl + nmi) > 0


# ------------------------------------------------------------------ models: logistic regression on feature blocks


def fit_logit(X: np.ndarray, y: np.ndarray, l2: float = 1.0, max_iter: int = 60) -> np.ndarray:
    """Ridge-penalised logistic regression by damped Newton; returns [intercept, coefficients].  The
    intercept is not penalised.  X may have zero columns (then the base rate)."""
    n = len(y)
    A = np.hstack([np.ones((n, 1)), X.astype(np.float64)]) if X.size else np.ones((n, 1))
    q = A.shape[1]
    pen = np.full(q, float(l2))
    pen[0] = 0.0
    mean = float(np.clip(y.mean(), 1e-6, 1 - 1e-6))
    beta = np.zeros(q)
    beta[0] = np.log(mean / (1 - mean))

    def nll(b):
        z = A @ b
        return float(np.sum(np.logaddexp(0, z) - y * z) + 0.5 * np.sum(pen * b * b))

    cur = nll(beta)
    for _ in range(max_iter):
        mu = expit(A @ beta)
        W = mu * (1 - mu)
        grad = A.T @ (mu - y) + pen * beta
        H = (A * W[:, None]).T @ A + np.diag(pen) + 1e-9 * np.eye(q)
        step = np.linalg.solve(H, grad)
        t = 1.0
        while t > 1e-6:
            new = beta - t * step
            val = nll(new)
            if val <= cur + 1e-12:
                break
            t *= 0.5
        else:
            break
        done = abs(cur - val) < 1e-10 * max(1.0, abs(cur))
        beta, cur = new, val
        if done:
            break
    return beta


def predict_logit(beta: np.ndarray, X: np.ndarray) -> np.ndarray:
    z = np.full(X.shape[0], beta[0], dtype=np.float64)
    if X.shape[1]:
        z = z + X @ beta[1:]
    return expit(z)


def feature_block(ev: Events, block: str) -> np.ndarray:
    """Feature columns of one named block.  Counts enter as log(1 + count)."""
    if block == "person":  # LHK's four signed degrees: u's out-votes, v's in-votes
        return np.log1p(ev.deg.astype(np.float64))
    if block == "person_rate":  # the same as two smoothed log-odds (sender, receiver), a_u + b_v form
        out = (ev.deg[:, 0] + 1.0) / (ev.deg[:, 0] + ev.deg[:, 1] + 2.0)
        inn = (ev.deg[:, 2] + 1.0) / (ev.deg[:, 2] + ev.deg[:, 3] + 2.0)
        return np.column_stack([np.log(out / (1 - out)), np.log(inn / (1 - inn))])
    if block == "recip":
        return np.column_stack([(ev.recip > 0).astype(float), (ev.recip < 0).astype(float)])
    if block == "prev":
        return np.column_stack([(ev.prev > 0).astype(float), (ev.prev < 0).astype(float)])
    if block == "sat16":
        return np.log1p(ev.C16.astype(np.float64))
    if block == "und4":
        return np.log1p(ev.U.astype(np.float64))
    if block == "emb":
        return np.log1p(ev.emb.astype(np.float64))[:, None]
    if block == "recent":  # logit of the adaptive recent positive share
        r = np.clip(ev.recent, 1e-3, 1 - 1e-3)
        return np.log(r / (1 - r))[:, None]
    if block.startswith("rule:"):
        npl, nmi = rule_counts(ev, block[5:])
        return np.column_stack([np.log1p(npl), np.log1p(nmi)]).astype(np.float64)
    raise ValueError(f"unknown block {block!r}")


def design(ev: Events, blocks: tuple[str, ...]) -> np.ndarray:
    if not blocks:
        return np.zeros((ev.m, 0))
    return np.hstack([feature_block(ev, b) for b in blocks])


# ------------------------------------------------------------------ metrics and the cluster bootstrap

EPS = 1e-6


def logloss_vec(y: np.ndarray, p: np.ndarray) -> np.ndarray:
    p = np.clip(p, EPS, 1 - EPS)
    return -(y * np.log(p) + (1 - y) * np.log1p(-p))


def auc(y: np.ndarray, score: np.ndarray) -> float:
    n1 = int(y.sum())
    n0 = len(y) - n1
    if n1 == 0 or n0 == 0:
        return float("nan")
    r = rankdata(score)
    return float((r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def balanced_accuracy(y: np.ndarray, yhat: np.ndarray) -> float:
    pos, neg = y == 1, y == 0
    if not pos.any() or not neg.any():
        return float("nan")
    return float(0.5 * ((yhat[pos] == 1).mean() + (yhat[neg] == 0).mean()))


def _relabel(c: np.ndarray) -> tuple[np.ndarray, int]:
    _, inv = np.unique(c, return_inverse=True)
    return inv.astype(np.int64), int(inv.max()) + 1


def cluster_boot_sums(cols: np.ndarray, clusters: np.ndarray, B: int, rng: np.random.Generator) -> np.ndarray:
    """Cluster-bootstrap totals of additive per-row statistics.  cols (n, q); returns (B, q): each row is
    the column sums over a resample of the clusters (with replacement, same number of clusters)."""
    cl, K = _relabel(clusters)
    S = np.zeros((K, cols.shape[1]))
    for j in range(cols.shape[1]):
        S[:, j] = np.bincount(cl, weights=cols[:, j], minlength=K)
    out = np.empty((B, cols.shape[1]))
    for b in range(B):
        out[b] = S[rng.integers(0, K, K)].sum(axis=0)
    return out


def boot_ci(point: float, draws: np.ndarray) -> tuple[float, float, float]:
    """(lo, hi, se) percentile interval and standard error of bootstrap draws."""
    lo, hi = np.percentile(draws, [2.5, 97.5])
    return float(lo), float(hi), float(np.std(draws, ddof=1))


# ------------------------------------------------------------------ the chronological evaluation

L2 = 1.0
TRAIN_FRAC = 0.70


def split_time(ev_all: Events, frac: float = TRAIN_FRAC) -> float:
    """The cut that sends the first `frac` of ALL target events (before any masking) to training.
    Events with t < T train, events with t >= T test, so tied times never straddle the cut."""
    return float(np.quantile(ev_all.t, frac, method="lower"))


# name -> feature blocks.  Every model is a logistic regression on its blocks (intercept included), fitted
# on the training events only.  A rule enters as two features: log(1 + votes for +) and log(1 + votes for -).
MODEL_BLOCKS: dict[str, tuple[str, ...]] = {
    "base rate": (),
    "recent rate": (),  # no fitted parameter: the smoothed positive share of the last RECENT_K visible ties
    "strict balance": ("rule:strict",),
    "weak balance": ("rule:weak",),
    "first-tie asymmetric": ("rule:first_tie",),
    "status": ("rule:status",),
    "conjunction": ("rule:conjunction",),
    "copy incoming": ("rule:copy_incoming",),
    "strict (per instance)": ("rule:strict_inst",),
    "weak (per instance)": ("rule:weak_inst",),
    "A^2 sign (FF only)": ("rule:a_squared",),
    "first-tie, FF only": ("rule:first_tie_ffonly",),
    "first-tie, all forms": ("rule:first_tie_all",),
    "first-tie, time-first": ("rule:first_tie_time",),
    "saturated 16 types": ("sat16",),
    "person propensity": ("person",),
    "person (rate form)": ("person_rate",),
    "person + recent": ("person", "recent"),
    "person + strict": ("person", "rule:strict"),
    "person + weak": ("person", "rule:weak"),
    "person + first-tie": ("person", "rule:first_tie"),
    "person + status": ("person", "rule:status"),
    "person + conjunction": ("person", "rule:conjunction"),
    "person + 16 types": ("person", "sat16"),
    "person + reciprocity": ("person", "recip"),
    "person + reciprocity + 16 types": ("person", "recip", "sat16"),
}
OWN_RULES = {
    "strict balance": "strict", "weak balance": "weak", "first-tie asymmetric": "first_tie",
    "status": "status", "conjunction": "conjunction", "copy incoming": "copy_incoming",
    "strict (per instance)": "strict_inst", "weak (per instance)": "weak_inst", "A^2 sign (FF only)": "a_squared",
    "first-tie, FF only": "first_tie_ffonly", "first-tie, all forms": "first_tie_all",
    "first-tie, time-first": "first_tie_time",
}
PRIMARY_MODELS = (
    "base rate", "recent rate", "strict balance", "weak balance", "first-tie asymmetric", "status",
    "person propensity", "conjunction", "saturated 16 types", "person + strict", "person + weak",
    "person + first-tie", "person + status", "person + 16 types",
)
CORE_RULES = ("strict balance", "weak balance", "first-tie asymmetric", "status")


@dataclass
class Evaluation:
    """Held-out predictions of a set of models on one chronological split (or several pooled), with
    cluster-bootstrap machinery for the additive statistics."""

    name: str
    T: float
    n_train: int
    n_test: int
    y: np.ndarray
    cal: dict  # model -> predicted P(+) on the test events
    own: dict  # rule model -> (hard prediction, voted)
    coef: dict  # model -> fitted coefficients (last fold if pooled)
    clusters: dict  # scheme -> cluster ids of the test events
    thr: np.ndarray  # per test event: training positive share (balanced-accuracy threshold)
    train_rate: float
    test_rate: float
    cols: np.ndarray | None = None
    colnames: list = field(default_factory=list)
    _boot: dict = field(default_factory=dict)

    def _build_cols(self) -> None:
        y = self.y.astype(float)
        cols, names = [np.ones_like(y), y, 1 - y], ["N", "Npos", "Nneg"]
        for m, p in self.cal.items():
            cols.append(logloss_vec(self.y, p))
            names.append(f"L:{m}")
            hat05 = (p >= 0.5).astype(int)
            hatpr = (p >= self.thr).astype(int)
            cols += [(hat05 == self.y).astype(float), ((hatpr == 1) & (self.y == 1)).astype(float),
                     ((hatpr == 0) & (self.y == 0)).astype(float)]
            names += [f"A:{m}", f"Ap:{m}", f"An:{m}"]
        for m, (hat, _) in self.own.items():
            cols += [(hat == self.y).astype(float), ((hat == 1) & (self.y == 1)).astype(float),
                     ((hat == 0) & (self.y == 0)).astype(float)]
            names += [f"oA:{m}", f"oAp:{m}", f"oAn:{m}"]
        self.cols = np.column_stack(cols)
        self.colnames = names

    def _col(self, name: str) -> int:
        return self.colnames.index(name)

    def bootstrap(self, B: int, seed: int) -> None:
        rng = np.random.default_rng(seed)
        for scheme, cl in self.clusters.items():
            self._boot[scheme] = cluster_boot_sums(self.cols, cl, B, rng)

    def _stat(self, sums: np.ndarray, spec) -> np.ndarray:
        """spec: ('ll', m) | ('dll', a, b) | ('acc', m, own) | ('bacc', m, own); sums (..., q)."""
        c = self._col
        kind = spec[0]
        N = sums[..., c("N")]
        if kind == "ll":
            return sums[..., c(f"L:{spec[1]}")] / N
        if kind == "dll":
            return (sums[..., c(f"L:{spec[1]}")] - sums[..., c(f"L:{spec[2]}")]) / N
        pre = "o" if spec[2] else ""
        if kind == "acc":
            return sums[..., c(f"{pre}A:{spec[1]}")] / N
        if kind == "bacc":
            return 0.5 * (sums[..., c(f"{pre}Ap:{spec[1]}")] / sums[..., c("Npos")]
                          + sums[..., c(f"{pre}An:{spec[1]}")] / sums[..., c("Nneg")])
        raise ValueError(spec)

    def point(self, spec) -> float:
        return float(self._stat(self.cols.sum(axis=0), spec))

    def ci(self, spec) -> tuple[float, float, float]:
        """(lo, hi, se) of the 95% percentile interval under the cluster scheme with the largest standard
        error (the conservative one)."""
        best = None
        for scheme, draws in self._boot.items():
            d = self._stat(draws, spec)
            se = float(np.std(d, ddof=1))
            if best is None or se > best[2]:
                lo, hi = np.percentile(d, [2.5, 97.5])
                best = (float(lo), float(hi), se)
        return best

    def pvalue_diff(self, a: str, b: str) -> float:
        """Two-sided bootstrap p of 'log-loss of a equals log-loss of b' (share of paired-difference draws
        on the wrong side of zero, doubled; conservative scheme; floored at 1/(B+1))."""
        best = None
        for scheme, draws in self._boot.items():
            d = self._stat(draws, ("dll", a, b))
            se = float(np.std(d, ddof=1))
            if best is None or se > best[0]:
                best = (se, max(2 * min((d <= 0).mean(), (d >= 0).mean()), 1.0 / (len(d) + 1)))
        return best[1]

    def coverage(self, rule_model: str) -> float:
        return float(self.own[rule_model][1].mean())

    def auc(self, m: str) -> float:
        return auc(self.y, self.cal[m])

    def diff(self, a: str, b: str) -> tuple[float, float, float, float]:
        """(point, lo, hi, p) of logloss(a) - logloss(b); negative = a better."""
        lo, hi, _ = self.ci(("dll", a, b))
        return self.point(("dll", a, b)), lo, hi, self.pvalue_diff(a, b)


def _fit_predict(ev_tr: Events, ev_te: Events, models, extra, l2):
    cal, own, coef = {}, {}, {}
    for m in models:
        if m == "recent rate":
            cal[m] = ev_te.recent.copy()
            coef[m] = np.array([])
        else:
            blocks = tuple(extra) + MODEL_BLOCKS[m]
            Xtr, Xte = design(ev_tr, blocks), design(ev_te, blocks)
            beta = fit_logit(Xtr, ev_tr.y.astype(float), l2=l2)
            cal[m] = predict_logit(beta, Xte)
            coef[m] = beta
        if m in OWN_RULES:
            own[m] = rule_prediction(ev_te, OWN_RULES[m])
    return cal, own, coef


def evaluate(
    ev_all: Events,
    mask: np.ndarray,
    T: float,
    models: tuple[str, ...] = PRIMARY_MODELS,
    extra: tuple[str, ...] = (),
    schemes: tuple[str, ...] = ("u", "v"),
    B: int = 0,
    seed: int = 20261101,
    l2: float = L2,
    name: str = "",
    T_hi: float = np.inf,
) -> Evaluation:
    """Fit every model on the training events (mask & t < T) and score it on the test events
    (mask & T <= t < T_hi).  `extra` blocks are added to every fitted model (e.g. 'prev' for re-votes, so
    the base model is persistence).  Nothing about a test event, its label or any later event enters a
    fit: a fit sees training rows only, and a row's features were fixed by build_events from ties visible
    before its cut.  With extra, 'recent rate' is the unfitted adaptive baseline and ignores it."""
    tr = mask & (ev_all.t < T)
    te = mask & (ev_all.t >= T) & (ev_all.t < T_hi)
    ev_tr, ev_te = ev_all.subset(tr), ev_all.subset(te)
    cal, own, coef = _fit_predict(ev_tr, ev_te, models, extra, l2)
    cl = {s: {"u": ev_te.u, "v": ev_te.v, "g": ev_te.g}[s] for s in schemes}
    rate = float(ev_tr.y.mean()) if ev_tr.m else 0.5
    out = Evaluation(
        name=name or ev_all.name, T=T, n_train=int(tr.sum()), n_test=int(te.sum()), y=ev_te.y.astype(int),
        cal=cal, own=own, coef=coef, clusters=cl, thr=np.full(ev_te.m, rate), train_rate=rate,
        test_rate=float(ev_te.y.mean()),
    )
    out._build_cols()
    if B:
        out.bootstrap(B, seed)
    return out


def rolling_origin(
    ev_all: Events, mask: np.ndarray, n_folds: int = 5, start_frac: float = 0.5,
    models: tuple[str, ...] = PRIMARY_MODELS, extra: tuple[str, ...] = (), schemes=("u", "v"),
    B: int = 0, seed: int = 20261101, l2: float = L2,
) -> tuple[Evaluation, list[Evaluation]]:
    """Expanding-window evaluation: the events after the first `start_frac` are cut into n_folds equal
    blocks of events; block k is predicted by models fitted on everything before it.  Returns the pooled
    Evaluation (all blocks' held-out predictions together) and the per-block ones.  Less exposed to a
    level shift between one training period and one test period than a single split."""
    qs = [np.quantile(ev_all.t, f, method="lower") for f in np.linspace(start_frac, 1.0, n_folds + 1)[:-1]]
    edges = qs + [np.inf]
    folds = [evaluate(ev_all, mask, edges[k], models, extra, schemes, 0, seed, l2, name=f"fold{k+1}", T_hi=edges[k + 1])
             for k in range(n_folds)]
    ok = [f for f in folds if f.n_test > 0]
    pooled = Evaluation(
        name=ok[0].name + " (rolling)", T=ok[0].T, n_train=ok[0].n_train, n_test=sum(f.n_test for f in ok),
        y=np.concatenate([f.y for f in ok]),
        cal={m: np.concatenate([f.cal[m] for f in ok]) for m in ok[0].cal},
        own={m: (np.concatenate([f.own[m][0] for f in ok]), np.concatenate([f.own[m][1] for f in ok])) for m in ok[0].own},
        coef=ok[-1].coef,
        clusters={s: np.concatenate([f.clusters[s] for f in ok]) for s in ok[0].clusters},
        thr=np.concatenate([f.thr for f in ok]), train_rate=float(np.mean([f.train_rate for f in ok])),
        test_rate=float(np.concatenate([f.y for f in ok]).mean()),
    )
    pooled._build_cols()
    if B:
        pooled.bootstrap(B, seed)
    return pooled, folds


# ------------------------------------------------------------------ the static pattern: D&K's eight types, sender and receiver nulls

DK_TYPES = ("LLL", "LLD", "LDL", "LDD", "DLL", "DLD", "DDL", "DDD")  # (u->w)(w->v)(u->v), L = +, D = - [L4481]
# The Newcomb pattern, from wave 6 on [L4490-L4498; sim/results/newcomb_n3.md 2.1]: +1 above the null, -1 below.
DK_NEWCOMB_DIRECTION = {"LLL": 1, "LLD": -1, "LDL": -1, "LDD": 1, "DLL": 1, "DLD": -1, "DDL": -1, "DDD": 1}
DK_COPY_SECOND = {t: (1 if t[1] == t[2] else -1) for t in DK_TYPES}  # closing sign equals the second tie's sign
DK_BALANCE = {t: (1 if (t.count("D") % 2 == 0) else -1) for t in DK_TYPES}  # even number of D: Heider-balanced
_FF = {"LL": 0, "LD": 1, "DL": 2, "DD": 3}  # FFpp, FFpm, FFmp, FFmm in the 16-type order
T_FFMP, T_FFMM = 2, 3


def dk_counts(C16: np.ndarray, y: np.ndarray, weights: str = "instance") -> np.ndarray:
    """Counts of the eight D&K types over FF contexts: for each FF cell (s1, s2) and closing sign.
    C16 (m, 16) per-event type counts, y (m,) closing sign.  weights='instance': one count per triad (u, w, v), as
    D&K count ordered triples; a closing tie with many common neighbours then counts many times.
    weights='event': each closing tie counts once, split over its FF cells in proportion to its instances, so
    the unit is the closing tie and embeddedness cannot masquerade as a link between cell and sign."""
    ff = C16[:, :4].astype(np.float64)
    if weights == "event":
        tot_e = ff.sum(axis=1, keepdims=True)
        ff = np.divide(ff, tot_e, out=np.zeros_like(ff), where=tot_e > 0)
    elif weights != "instance":
        raise ValueError(weights)
    pos = ff.T @ y.astype(np.float64)
    tot = ff.sum(axis=0)
    out = np.zeros(8)
    for i, t in enumerate(DK_TYPES):
        cell = _FF[t[:2]]
        out[i] = pos[cell] if t[2] == "L" else tot[cell] - pos[cell]
    return out


def _group_permute(y: np.ndarray, groups: np.ndarray, rng: np.random.Generator, order1: np.ndarray) -> np.ndarray:
    """A permutation of y within each group (groups contiguous after `order1`)."""
    r = rng.random(len(y))
    order2 = np.lexsort((r, groups))
    out = np.empty_like(y)
    out[order1] = y[order2]
    return out


def dk_static(ev: Events, mask: np.ndarray, null: str = "u", B: int = 2000, seed: int = 20261101, weights: str = "event") -> dict:
    """D&K's static comparison on formation-ordered ties.  The events are the target ties in `mask` that have at
    least one forward-chain (FF) context; each carries the contexts (u->w, w->v) that existed before it.  Null:
    the closing signs are shuffled within sender (null='u', the formation-ordered analogue of the Newcomb run's
    row-wise shuffle [L4485], which redrew every tie of a row: here every sender keeps the mix of + and - of his
    closing ties, the context ties do not move, and reception is free), within sender and calendar year (null='uy': the same, with
    the drift of the site's positive share held), within receiver (null='v': every receiver keeps the mix of
    signs he was given; the sender's tendency is free), or over all events (null='all').  weights: see dk_counts.
    NOTE the eight counts are four coupled pairs (a cell's two closings sum to the cell total), so a z score
    and its side come in +/- pairs and 'agreement x/8' counts cells twice.  Returns obs, null mean/sd, z, D&K's
    p(obs > random) (mid-p), the side, and agreement with three readings of the pattern."""
    keep = mask & (ev.C16[:, :4].sum(axis=1) > 0)
    e = ev.subset(keep)
    C16, y = e.C16, e.y
    obs = dk_counts(C16, y, weights)
    rng = np.random.default_rng(seed)
    year = np.floor(e.t / (365.25 * 86400.0)).astype(np.int64)
    groups = {"u": e.u, "v": e.v, "uy": e.u * 64 + (year - year.min()) if e.m else e.u,
              "all": np.zeros(e.m, dtype=np.int64)}[null]
    order1 = np.argsort(groups, kind="stable")
    draws = np.empty((B, 8))
    for b in range(B):
        draws[b] = dk_counts(C16, _group_permute(y, groups, rng, order1), weights)
    mean, sd = draws.mean(0), draws.std(0, ddof=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        z = np.where(sd > 0, (obs - mean) / np.where(sd > 0, sd, 1), np.nan)
    p_gt = (obs[None, :] > draws).mean(0) + 0.5 * (obs[None, :] == draws).mean(0)  # mid-p version of D&K's statistic
    side = np.where(obs > mean, 1, np.where(obs < mean, -1, 0))
    out = {"obs": obs, "mean": mean, "sd": sd, "z": z, "p_gt": p_gt, "side": side, "n_events": e.m, "null": null, "B": B, "weights": weights}
    for key, ref in (("newcomb", DK_NEWCOMB_DIRECTION), ("copy_second", DK_COPY_SECOND), ("balance", DK_BALANCE)):
        out[f"agree_{key}"] = int(sum(1 for i, t in enumerate(DK_TYPES) if side[i] == ref[t]))
    return out


def ff_cell_table(ev: Events, mask: np.ndarray, B: int = 1000, seed: int = 20261101, scheme: str = "v") -> list[dict]:
    """P(closing +) in each of the four FF cells with a cluster-bootstrap interval, weighting every triad
    (instance) or every closing tie (event: split over its cells), and the contrasts that separate the readings
    of the pattern.  Cells in (first tie, second tie) order.  Events without an FF context are left out."""
    keep = mask & (ev.C16[:, :4].sum(axis=1) > 0)
    e = ev.subset(keep)
    ff = e.C16[:, :4].astype(float)
    ffe = ff / ff.sum(axis=1, keepdims=True)
    y = e.y.astype(float)
    cols = np.column_stack([ff, ff * y[:, None], ffe, ffe * y[:, None]])  # instance tot/pos, event tot/pos
    cl = {"u": e.u, "v": e.v, "g": e.g}[scheme]
    draws = cluster_boot_sums(cols, cl, B, np.random.default_rng(seed))
    tot = cols.sum(axis=0)
    names = ("pp", "pm", "mp", "mm")

    def rates(sums, off):
        return sums[..., off + 4: off + 8] / np.maximum(sums[..., off: off + 4], 1e-12)

    rows = []
    for w, off in (("instance", 0), ("event", 8)):
        r0, rb = rates(tot, off), rates(draws, off)
        for i, nm in enumerate(names):
            lo, hi = np.percentile(rb[:, i], [2.5, 97.5])
            rows.append({"weights": w, "cell": "FF" + nm, "instances": int(round(tot[off + i])) if w == "instance" else float(tot[off + i]),
                         "events": int((ff[:, i] > 0).sum()), "p_pos": float(r0[i]), "lo": float(lo), "hi": float(hi)})
        contrasts = {
            "mp - pm": (r0[2] - r0[1], rb[:, 2] - rb[:, 1]),  # the two one-negative starts: 0 under balance, >0 under copy-second
            "pp - mm": (r0[0] - r0[3], rb[:, 0] - rb[:, 3]),  # >0 when (-,-) does NOT close positive
            "mm - mp": (r0[3] - r0[2], rb[:, 3] - rb[:, 2]),  # balance: +, copy-second: -
        }
        for k, (pt, d) in contrasts.items():
            lo, hi = np.percentile(d, [2.5, 97.5])
            rows.append({"weights": w, "cell": k, "instances": 0, "events": 0, "p_pos": float(pt), "lo": float(lo), "hi": float(hi)})
    return rows


def cell_table16(ev: Events, mask: np.ndarray) -> list[dict]:
    """All sixteen types: instances, events, P(closing +) (instance-weighted) and each rule's label."""
    e = ev.subset(mask)
    C16 = e.C16.astype(float)
    y = e.y.astype(float)
    rows = []
    for t in range(16):
        n = C16[:, t].sum()
        rows.append({
            "type": TYPE_NAMES[t], "instances": int(n), "events": int((C16[:, t] > 0).sum()),
            "p_pos": float((C16[:, t] * y).sum() / n) if n else float("nan"),
            "balance": int(TYPE_S1[t] * TYPE_S2[t]),
            "status": int(DIRECTED_RULES["status"][t, 0]), "first_tie": int(DIRECTED_RULES["first_tie"][t, 0]),
            "conjunction": int(DIRECTED_RULES["conjunction"][t, 0]),
        })
    return rows


# ------------------------------------------------------------------ do the triad terms add to the person terms? a permutation null


def _emb_bins(emb: np.ndarray) -> np.ndarray:
    return np.digitize(emb, [2, 3, 5, 10])  # bins: 1, 2, 3-4, 5-9, 10+


def _perm_within(groups: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    """Index permutation that shuffles rows within groups."""
    r = rng.random(len(groups))
    order = np.lexsort((r, groups))  # sorted by group, random within
    base = np.argsort(groups, kind="stable")
    perm = np.empty(len(groups), dtype=np.int64)
    perm[base] = order
    return perm


def added_value(
    ev_all: Events, mask: np.ndarray, T: float, base: tuple[str, ...], add: tuple[str, ...],
    extra: tuple[str, ...] = (), n_perm: int = 200, seed: int = 20261101, l2: float = L2,
) -> dict:
    """Held-out log-loss gain from adding the feature blocks `add` to a model with blocks `base`, and the
    permutation null for that gain: the rows of the added features are shuffled among events with the same
    embeddedness bin, separately in the training and the test events (so the added features keep their
    marginal distribution and their link to embeddedness but lose their link to the sign and to the other
    features), the model is refitted on the shuffled training rows and scored on the shuffled test rows.
    p = (1 + #{null gain >= observed gain}) / (n_perm + 1)."""
    tr = mask & (ev_all.t < T)
    te = mask & (ev_all.t >= T)
    a, b = ev_all.subset(tr), ev_all.subset(te)
    Xb_tr, Xb_te = design(a, tuple(extra) + base), design(b, tuple(extra) + base)
    Xa_tr, Xa_te = design(a, add), design(b, add)
    ytr, yte = a.y.astype(float), b.y.astype(float)
    beta0 = fit_logit(Xb_tr, ytr, l2)
    ll0 = float(logloss_vec(yte, predict_logit(beta0, Xb_te)).mean())
    beta1 = fit_logit(np.hstack([Xb_tr, Xa_tr]), ytr, l2)
    ll1 = float(logloss_vec(yte, predict_logit(beta1, np.hstack([Xb_te, Xa_te]))).mean())
    gain = ll0 - ll1
    rng = np.random.default_rng(seed)
    bins_tr, bins_te = _emb_bins(a.emb), _emb_bins(b.emb)
    null = np.empty(n_perm)
    for k in range(n_perm):
        ptr, pte = _perm_within(bins_tr, rng), _perm_within(bins_te, rng)
        bk = fit_logit(np.hstack([Xb_tr, Xa_tr[ptr]]), ytr, l2)
        llk = float(logloss_vec(yte, predict_logit(bk, np.hstack([Xb_te, Xa_te[pte]]))).mean())
        null[k] = ll0 - llk
    return {
        "ll_base": ll0, "ll_full": ll1, "gain": gain, "null_mean": float(null.mean()), "null_sd": float(null.std(ddof=1)),
        "null_max": float(null.max()), "p": float((1 + (null >= gain).sum()) / (n_perm + 1)), "n_test": b.m, "n_perm": n_perm,
    }


# ------------------------------------------------------------------ 117's undirected closure table, reproduced


def undirected_closure(site: str) -> dict:
    """117's static formation-order count [L4572-L4577]: the undirected projection keeps the first rating
    between two users in either direction; a triangle is three mutually rated pairs; its edges are ordered
    by the time of those first ratings; the closing edge is the latest.  Returns counts of pairs, triangles,
    the (+,+) / (+,-) / (-,-) starts with the share closing positive, the product-rule agreement, and the
    same restricted to the triangles whose three first-rating times are all distinct (the only ones whose
    formation order does not depend on a tie-break; 117's 'strictly ordered' 20,016 of 22,153 in Alpha)."""
    src, tgt, rat, tim = load_bitcoin_raw(site)
    order = np.argsort(tim, kind="stable")
    src, tgt, rat, tim = src[order], tgt[order], rat[order], tim[order]
    first: dict[tuple[int, int], tuple[int, float, int]] = {}
    for k in range(len(src)):
        a, b = int(src[k]), int(tgt[k])
        key = (a, b) if a < b else (b, a)
        if key not in first:
            first[key] = (1 if rat[k] > 0 else -1, float(tim[k]), k)
    adj: dict[int, set] = defaultdict(set)
    for a, b in first:
        adj[a].add(b)
        adj[b].add(a)
    n_tri = 0
    start = {"pp": [0, 0], "pm": [0, 0], "mm": [0, 0]}  # [triangles, closing positive]
    prod_ok = 0
    strict_n = strict_ok = 0
    for (a, b) in first:
        for c in adj[a] & adj[b]:
            if c < b:  # count each triangle once, by its two smallest ids a < b < c
                continue
            if c <= a:
                continue
            es = sorted(((first[(a, b)]), first[(a, c) if a < c else (c, a)], first[(b, c) if b < c else (c, b)]), key=lambda x: (x[1], x[2]))
            s1, s2, s3 = es[0][0], es[1][0], es[2][0]
            n_tri += 1
            key = "pp" if (s1 > 0 and s2 > 0) else ("mm" if (s1 < 0 and s2 < 0) else "pm")
            start[key][0] += 1
            start[key][1] += int(s3 > 0)
            ok = s3 == s1 * s2
            prod_ok += int(ok)
            if es[0][1] < es[1][1] < es[2][1]:  # all three times distinct: the order is not a tie-break
                strict_n += 1
                strict_ok += int(ok)
    return {
        "pairs": len(first), "triangles": n_tri, "starts": start, "product_ok": prod_ok,
        "strict_triangles": strict_n, "strict_product_ok": strict_ok,
    }


# ------------------------------------------------------------------ Newcomb re-read: what the first-tie pattern is there


def newcomb_reception_check(n_draws: int = 2000, seed: int = 20261101) -> dict:
    """The Newcomb run's own eight-type pattern, read against the 'closing sign equals second-tie sign'
    partition, under (a) D&K's row-wise null (each man's out-signs fixed; reception free) and (b) a
    column-wise null (each man's received signs fixed and permuted across senders; popularity held, the
    senders' quotas free).  POST HOC: neither is in the pre-specification of this test.  Needs the
    git-ignored Newcomb ranks (models.newcomb)."""
    from models import newcomb as nc

    S = nc.recode(nc.load_ranks())  # (15, 17, 17), D&K's top-4 / bottom-3
    obs = nc.triple_counts(S)  # (15, 8), nc.TRIPLE_TYPES == DK_TYPES order
    assert nc.TRIPLE_TYPES == DK_TYPES
    rng = np.random.default_rng(seed)
    row_null = nc.static_null(rng, n_draws)["triple"]
    row = nc.compare_to_null(obs, row_null)
    side_row = np.sign(obs - nc.expected_triple_counts()).astype(int)  # exact null means, (15, 8)

    def col_shuffle(Sw: np.ndarray, B: int) -> np.ndarray:
        n = Sw.shape[0]
        out = np.zeros((B, n, n), dtype=np.int8)
        for j in range(n):
            rows = [i for i in range(n) if i != j]
            col = Sw[rows, j]
            out[:, rows, j] = rng.permuted(np.broadcast_to(col, (B, n - 1)).copy(), axis=1)
        return out

    side_col = np.zeros((15, 8), dtype=int)
    z_col = np.zeros((15, 8))
    for w in range(15):
        nulls = nc.triple_counts(col_shuffle(S[w], n_draws))
        mean, sd = nulls.mean(0), nulls.std(0, ddof=1)
        z_col[w] = (obs[w] - mean) / sd
        side_col[w] = np.sign(obs[w] - mean).astype(int)
    ref_copy = np.array([DK_COPY_SECOND[t] for t in DK_TYPES])
    ref_new = np.array([DK_NEWCOMB_DIRECTION[t] for t in DK_TYPES])
    return {
        "side_row": side_row, "z_row": row["z"], "side_col": side_col, "z_col": z_col,
        "agree_copy_row": (side_row == ref_copy).sum(axis=1), "agree_copy_col": (side_col == ref_copy).sum(axis=1),
        "agree_newcomb_row": (side_row == ref_new).sum(axis=1),
        "max_abs_z_col": np.abs(z_col).max(axis=1), "n_draws": n_draws,
    }


# ------------------------------------------------------------------ the experiment: sites, masks, primary runs and variations

SITE_NAMES = ("bitcoin-otc", "bitcoin-alpha", "wiki-rfa")
SITE_SCHEMES = {"bitcoin-otc": ("u", "v"), "bitcoin-alpha": ("u", "v"), "wiki-rfa": ("u", "g")}
SITE_TITLES = {"bitcoin-otc": "Bitcoin OTC", "bitcoin-alpha": "Bitcoin Alpha", "wiki-rfa": "wiki-RfA"}
KS = (1, 2, 3, 5, 10, 25)  # embeddedness thresholds
SEED = 20261101
B_PRIMARY = 2000  # cluster-bootstrap draws, primary tables
B_VAR = 400  # draws in the variation tables
N_PERM = 200  # permutations in the added-value null
N_SHUF = 2000  # shuffles in the static D&K pattern
B_CELL = 1000  # cluster-bootstrap draws for the forward-chain cell rates (section 4.6)
B_COEF = 400  # cluster-bootstrap refits for the person-adjusted FF coefficients (section 4.6); 100 before the review

_cache: dict = {}


def site_events(site: str, recode: str = "all", horizon: str = "election", freeze_at: float | None = None) -> Events:
    """Events for a site, cached.  recode: Bitcoin rating recode name, or wiki neutral handling."""
    key = (site, recode, horizon, freeze_at)
    if key not in _cache:
        if site.startswith("bitcoin-"):
            tt = bitcoin_ties(site.split("-")[1], recode)
        else:
            tt = wiki_ties(recode, horizon)
        _cache[key] = build_events(tt, freeze_at)
    return _cache[key]


def default_recode(site: str) -> str:
    return "all" if site.startswith("bitcoin-") else "drop"


def mask_closing(ev: Events, k: int = 1) -> np.ndarray:
    """The primary target set: the first tie of an unordered pair (no tie in either direction visible),
    with at least k common neighbours.  117's 'closing' convention [L4572-L4573]."""
    return (ev.emb >= k) & ev.pair_first


def mask_all_new(ev: Events, k: int = 1) -> np.ndarray:
    """Every tie with no earlier tie in the SAME direction (so the reciprocating ones are included)."""
    return (ev.emb >= k) & (ev.prev == 0)


def mask_reciprocating(ev: Events, k: int = 1) -> np.ndarray:
    return (ev.emb >= k) & (ev.prev == 0) & (ev.recip != 0)


def mask_disagree(ev: Events, k: int = 1) -> np.ndarray:
    """Closing ties with a forward chain whose FIRST tie is negative (FFmp or FFmm): the only contexts in which
    the first-tie rule and strict balance say different things."""
    c = ev.C16
    return mask_closing(ev, k) & ((c[:, T_FFMP] + c[:, T_FFMM]) > 0)


def mask_converting(ev: Events, k: int = 1) -> np.ndarray:
    """A re-vote: the same ordered pair already had a visible tie (wiki-RfA only)."""
    return (ev.emb >= k) & (ev.prev != 0)


VAR_MODELS = (
    "base rate", "recent rate", "strict balance", "weak balance", "first-tie asymmetric", "status",
    "person propensity", "saturated 16 types", "person + strict", "person + first-tie", "person + 16 types",
)
FORM_MODELS = (
    "base rate", "strict balance", "strict (per instance)", "weak balance", "weak (per instance)",
    "first-tie asymmetric", "first-tie, FF only", "first-tie, all forms", "first-tie, time-first",
    "A^2 sign (FF only)", "status", "conjunction", "copy incoming", "saturated 16 types", "person propensity", "person (rate form)",
)


def run_primary(site: str, B: int = B_PRIMARY, converting: bool = False) -> dict:
    """The pre-specified primary run for one site: 70/30 chronological split, closing ties with >= 1
    common neighbour, every model; plus the rolling-origin check."""
    ev = site_events(site, default_recode(site))
    T = split_time(ev)
    mask = mask_converting(ev) if converting else mask_closing(ev)
    extra = ("prev",) if converting else ()
    sch = SITE_SCHEMES[site]
    models = tuple(m for m in PRIMARY_MODELS if not (converting and m == "recent rate"))
    res = evaluate(ev, mask, T, models, extra, sch, B, SEED, name=site)
    pooled, folds = rolling_origin(ev, mask, 5, 0.5, models, extra, sch, B, SEED)
    out = {"site": site, "ev": ev, "T": T, "mask": mask, "res": res, "pooled": pooled, "folds": folds, "converting": converting}
    if not converting:
        md = mask_disagree(ev)
        out["res_dis"] = evaluate(ev, md, T, models, extra, sch, B, SEED, name=site + " (rules disagree)")
        out["mask_dis"] = md
    return out


def run_forms(site: str, B: int = B_VAR) -> dict:
    ev = site_events(site, default_recode(site))
    T = split_time(ev)
    mask = mask_closing(ev)
    res = evaluate(ev, mask, T, FORM_MODELS, (), SITE_SCHEMES[site], B, SEED, name=site)
    pooled, _ = rolling_origin(ev, mask, 5, 0.5, FORM_MODELS, (), SITE_SCHEMES[site], B, SEED)
    return {"res": res, "pooled": pooled}


def _vrow(label: str, res: Evaluation, extra_info: dict | None = None) -> dict:
    """One variation row: sizes, held-out log-loss of the headline models, and two headline contrasts."""
    row = {"label": label, "n_train": res.n_train, "n_test": res.n_test, "test_rate": res.test_rate, "train_rate": res.train_rate}
    for m in VAR_MODELS:
        if m in res.cal:
            row[m] = res.point(("ll", m))
    if res._boot:
        row["d_ft_strict"] = res.diff("first-tie asymmetric", "strict balance")[:3]
        row["d_p16_person"] = res.diff("person + 16 types", "person propensity")[:3]
        row["d_strict_person"] = res.diff("strict balance", "person propensity")[:3]
    if extra_info:
        row.update(extra_info)
    return row


def run_variations(site: str, B: int = B_VAR) -> dict:
    """All variations for one site.  Each returns a list of rows (see _vrow)."""
    out: dict = {}
    sch = SITE_SCHEMES[site]
    base_recode = default_recode(site)
    ev0 = site_events(site, base_recode)
    T0 = split_time(ev0)

    # 1. embeddedness thresholds
    rows = []
    for k in KS:
        m = mask_closing(ev0, k)
        n_te = int((m & (ev0.t >= T0)).sum())
        if n_te < 40 or int((m & (ev0.t < T0)).sum()) < 40:
            rows.append({"label": f"k >= {k}", "n_train": int((m & (ev0.t < T0)).sum()), "n_test": n_te, "skipped": True})
            continue
        rows.append(_vrow(f"k >= {k}", evaluate(ev0, m, T0, VAR_MODELS, (), sch, B, SEED)))
    out["embeddedness"] = rows

    # 2. sign recodes
    rows = []
    recodes = list(BITCOIN_RECODES) if site.startswith("bitcoin-") else list(WIKI_NEUTRAL)
    for rc in recodes:
        ev = site_events(site, rc)
        T = split_time(ev)
        rows.append(_vrow(rc if site.startswith("bitcoin-") else f"neutral: {rc}", evaluate(ev, mask_closing(ev), T, VAR_MODELS, (), sch, B, SEED)))
    out["recodes"] = rows

    # 3. target sets: first tie of a pair / every new directed tie / reciprocating only
    rows = []
    tgt_models = ("base rate", "recent rate", "strict balance", "first-tie asymmetric", "person propensity",
                  "person + reciprocity", "person + 16 types", "person + reciprocity + 16 types")
    for label, mfun in (("first tie of the pair (primary)", mask_closing), ("every new directed tie", mask_all_new), ("reciprocating ties only", mask_reciprocating)):
        res = evaluate(ev0, mfun(ev0), T0, tgt_models, (), sch, B, SEED)
        r = {"label": label, "n_train": res.n_train, "n_test": res.n_test, "test_rate": res.test_rate}
        for m in tgt_models:
            r[m] = res.point(("ll", m))
        r["d_recip16_recip"] = res.diff("person + reciprocity + 16 types", "person + reciprocity")[:3]
        rows.append(r)
    out["targets"] = rows

    # 4. time: split fraction, frozen snapshot, rolling origin
    rows = []
    for frac in (0.5, 0.6, 0.7, 0.8):
        T = split_time(ev0, frac)
        rows.append(_vrow(f"split {int(frac * 100)}/{100 - int(frac * 100)}", evaluate(ev0, mask_closing(ev0), T, VAR_MODELS, (), sch, B, SEED)))
    evf = site_events(site, base_recode, "election", T0)
    true_first = np.zeros(int(max(ev0.idx.max(), evf.idx.max())) + 1, dtype=bool)
    true_first[ev0.idx[ev0.pair_first]] = True  # the target set is defined by the true history,
    maskf = (evf.emb >= 1) & true_first[evf.idx]  # the features by the frozen snapshot
    rows.append(_vrow("snapshot frozen at the 70% cut", evaluate(evf, maskf, T0, VAR_MODELS, (), sch, B, SEED)))
    pooled, _ = rolling_origin(ev0, mask_closing(ev0), 5, 0.5, VAR_MODELS, (), sch, B, SEED)
    rows.append(_vrow("rolling origin, 5 blocks from 50%", pooled))
    pooled3, _ = rolling_origin(ev0, mask_closing(ev0), 10, 0.3, VAR_MODELS, (), sch, B, SEED)
    rows.append(_vrow("rolling origin, 10 blocks from 30%", pooled3))
    out["time"] = rows

    # 5. regularisation and aggregation of the person terms
    rows = []
    for l2 in (0.01, 1.0, 100.0):
        rows.append(_vrow(f"ridge {l2:g}", evaluate(ev0, mask_closing(ev0), T0, VAR_MODELS, (), sch, B, SEED, l2=l2)))
    out["ridge"] = rows

    # 6. wiki: horizon
    if site == "wiki-rfa":
        rows = []
        evv = site_events(site, "drop", "vote")
        Tv = split_time(evv)
        rows.append(_vrow("election start (primary)", evaluate(ev0, mask_closing(ev0), T0, VAR_MODELS, (), sch, B, SEED)))
        rows.append(_vrow("every earlier dated vote", evaluate(evv, mask_closing(evv), Tv, VAR_MODELS, (), sch, B, SEED)))
        out["horizon"] = rows
    return out


def ff_coefficients(
    ev: Events, mask: np.ndarray, blocks: tuple[str, ...] = ("person", "sat16"), B: int = 100,
    seed: int = SEED, scheme: str = "v", l2: float = L2,
) -> dict:
    """Does the first tie matter once the person terms are in?  Fit person + the 16 type counts on all
    events in the mask and return the four FF coefficients (log1p count scale) with cluster-bootstrap
    intervals (refits on resampled clusters), plus the contrast FFmp - FFpm: zero if the first tie of a
    one-negative start is irrelevant given the person terms, positive under 'copy the second tie'."""
    e = ev.subset(mask)
    X = design(e, blocks)
    y = e.y.astype(float)
    off = 0  # first design column of the sat16 block
    for b in blocks:
        if b == "sat16":
            break
        off += feature_block(e.subset(np.arange(min(e.m, 2))), b).shape[1]
    else:
        raise ValueError("blocks must contain 'sat16'")
    col_ff = {nm: off + TYPE_NAMES.index(nm) for nm in ("FFpp", "FFpm", "FFmp", "FFmm")}
    beta = fit_logit(X, y, l2)
    cl = {"u": e.u, "v": e.v, "g": e.g}[scheme]
    _, inv = np.unique(cl, return_inverse=True)
    K = int(inv.max()) + 1
    order = np.argsort(inv, kind="stable")
    bounds = np.concatenate([[0], np.cumsum(np.bincount(inv, minlength=K))])
    rows_by = [order[bounds[k]: bounds[k + 1]] for k in range(K)]
    rng = np.random.default_rng(seed)
    draws = np.empty((B, 4))
    for b in range(B):
        pick = rng.integers(0, K, K)
        idx = np.concatenate([rows_by[k] for k in pick])
        bb = fit_logit(X[idx], y[idx], l2)
        draws[b] = [bb[1 + col_ff[nm]] for nm in ("FFpp", "FFpm", "FFmp", "FFmm")]
    pt = np.array([beta[1 + col_ff[nm]] for nm in ("FFpp", "FFpm", "FFmp", "FFmm")])
    out = {"cells": {}, "n": e.m, "B": B, "scheme": scheme}
    for i, nm in enumerate(("FFpp", "FFpm", "FFmp", "FFmm")):
        lo, hi = np.percentile(draws[:, i], [2.5, 97.5])
        out["cells"][nm] = (float(pt[i]), float(lo), float(hi))
    d = draws[:, 2] - draws[:, 1]
    lo, hi = np.percentile(d, [2.5, 97.5])
    out["mp_minus_pm"] = (float(pt[2] - pt[1]), float(lo), float(hi))
    # the product structure of balance: (pp + mm) - (pm + mp) > 0 when like signs close positive and unlike signs negative
    d2 = draws[:, 0] + draws[:, 3] - draws[:, 1] - draws[:, 2]
    lo2, hi2 = np.percentile(d2, [2.5, 97.5])
    out["balance_interaction"] = (float(pt[0] + pt[3] - pt[1] - pt[2]), float(lo2), float(hi2))
    return out


# ------------------------------------------------------------------ everything the report needs

def run_static(site: str, B_shuffle: int = N_SHUF, n_perm: int = N_PERM, B_coef: int = B_COEF) -> dict:
    """The replication half: D&K's eight types under the sender and receiver nulls (whole period, and the
    test period alone), the FF and sixteen-cell tables, the FF coefficients given the person terms, and the
    permutation tests of what the triad terms add to the person terms."""
    ev = site_events(site, default_recode(site))
    T = split_time(ev)
    mask = mask_closing(ev)
    out: dict = {"site": site, "T": T}
    out["dk"] = {
        (null, part, w): dk_static(ev, mask & ((ev.t >= T) if part == "test" else True), null, B_shuffle, SEED, w)
        for null in ("u", "v") for part, w in (("all", "event"), ("all", "instance"), ("test", "event"))
    }
    out["dk"][("uy", "all", "event")] = dk_static(ev, mask, "uy", B_shuffle, SEED, "event")
    out["ff"] = ff_cell_table(ev, mask, B_CELL, SEED, SITE_SCHEMES[site][1])
    out["cells16"] = cell_table16(ev, mask)
    out["coef"] = ff_coefficients(ev, mask, ("person", "sat16"), B_coef, SEED, SITE_SCHEMES[site][1])
    out["added"] = {
        name: added_value(ev, mask, T, ("person",), blocks, (), n_perm, SEED)
        for name, blocks in (
            ("16 types", ("sat16",)), ("strict balance", ("rule:strict",)), ("weak balance", ("rule:weak",)),
            ("first-tie asymmetric", ("rule:first_tie",)), ("status", ("rule:status",)),
        )
    }
    return out


def run_all(quick: bool = False) -> dict:
    """Compute everything.  quick=True shrinks every Monte-Carlo size (for the smoke test only)."""
    Bp, Bv, nperm, nshuf, Bc = (200, 60, 20, 100, 10) if quick else (B_PRIMARY, B_VAR, N_PERM, N_SHUF, B_COEF)
    R: dict = {"quick": quick, "sites": {}}
    for site in SITE_NAMES:
        entry: dict = {}
        entry["primary"] = run_primary(site, Bp)
        if site == "wiki-rfa":
            entry["converting"] = run_primary(site, Bp, converting=True)
        entry["static"] = run_static(site, nshuf, nperm, Bc)
        entry["forms"] = run_forms(site, Bv)
        entry["variations"] = run_variations(site, Bv)
        R["sites"][site] = entry
    R["closure117"] = {s: undirected_closure(s) for s in ("otc", "alpha")}
    try:
        R["newcomb"] = newcomb_reception_check(200 if quick else 2000, SEED)
    except FileNotFoundError:
        R["newcomb"] = None
    return R


# ------------------------------------------------------------------ rendering

def _t(x: float, d: int = 3) -> str:
    return "n/a" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{d}f}"


def _ci(pt: float, lo: float, hi: float, d: int = 3) -> str:
    return f"{pt:.{d}f} [{lo:.{d}f}, {hi:.{d}f}]"


def _sci(pt: float, lo: float, hi: float, d: int = 3) -> str:
    return f"{pt:+.{d}f} [{lo:+.{d}f}, {hi:+.{d}f}]"


def _p(p: float) -> str:
    return "<0.001" if p < 0.001 else f"{p:.3f}"


def md_table(headers: list[str], rows: list[list[str]], align: str | None = None) -> list[str]:
    a = align or ("l" + "r" * (len(headers) - 1))
    sep = ["---:" if c == "r" else ":---" for c in a]
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(sep) + " |"]
    out += ["| " + " | ".join(r) + " |" for r in rows]
    return out


def render_eval(res: Evaluation, title: str, models: tuple[str, ...] = PRIMARY_MODELS, rolling: bool = False, base_label: str = "base rate") -> list[str]:
    L = [f"**{title}** (train {res.n_train:,} events, test {res.n_test:,}; positive share train {res.train_rate:.3f}, test {res.test_rate:.3f})", ""]
    rows = []
    for m in models:
        if m not in res.cal:
            continue
        lo, hi, _ = res.ci(("ll", m))
        a_cal = res.point(("acc", m, False))
        b_cal = res.point(("bacc", m, False))
        row = [("base rate" if m == "base rate" and base_label == "base rate" else (base_label if m == "base rate" else m)),
               _ci(res.point(("ll", m)), lo, hi), "-" if (rolling or m in ("base rate", "recent rate")) else _t(res.auc(m)),
               _t(a_cal), _t(b_cal)]
        if m in res.own:
            alo, ahi, _ = res.ci(("acc", m, True))
            blo, bhi, _ = res.ci(("bacc", m, True))
            row += [f"{res.coverage(m):.2f}", _ci(res.point(("acc", m, True)), alo, ahi), _ci(res.point(("bacc", m, True)), blo, bhi)]
        else:
            row += ["-", "-", "-"]
        rows.append(row)
    L += md_table(["model", "held-out log-loss [95% CI]", "AUC", "acc @0.5", "bal. acc @prior",
                   "own: coverage", "own: accuracy [CI]", "own: bal. accuracy [CI]"], rows)
    return L


def render_contrasts(res: Evaluation, pairs: list[tuple[str, str]]) -> list[str]:
    rows = []
    B = min((len(d) for d in res._boot.values()), default=0)
    floor = 1.0 / (B + 1) if B else 0.0
    for a, b in pairs:
        if a in res.cal and b in res.cal:
            pt, lo, hi, p = res.diff(a, b)
            # at the floor 1/(B+1) the bootstrap p is a bound, not a value (B = 400 gives 0.0025)
            ptxt = f"<= {floor:.4f}" if (floor >= 0.001 and p <= floor + 1e-12) else _p(p)
            rows.append([f"{a} - {b}", _sci(pt, lo, hi), ptxt])
    return md_table(["paired contrast (log-loss; negative = first is better)", "difference [95% CI]", "bootstrap p"], rows)


CONTRASTS_PRIMARY = [
    ("strict balance", "base rate"), ("weak balance", "base rate"), ("first-tie asymmetric", "base rate"),
    ("status", "base rate"), ("person propensity", "base rate"), ("person propensity", "recent rate"),
    ("strict balance", "person propensity"), ("weak balance", "person propensity"),
    ("first-tie asymmetric", "person propensity"), ("status", "person propensity"),
    ("first-tie asymmetric", "strict balance"), ("first-tie asymmetric", "weak balance"), ("first-tie asymmetric", "status"),
    ("weak balance", "strict balance"), ("status", "strict balance"),
    ("person + 16 types", "person propensity"), ("person + strict", "person propensity"), ("person + weak", "person propensity"),
    ("person + first-tie", "person propensity"), ("person + status", "person propensity"),
    ("person + first-tie", "person + strict"), ("person + first-tie", "person + weak"), ("person + 16 types", "person + strict"),
    ("person + strict", "strict balance"), ("person + weak", "weak balance"), ("saturated 16 types", "weak balance"),
    ("conjunction", "weak balance"),
]


def render_dk(st: dict, site: str) -> list[str]:
    L = []
    for null, nulltxt in (("u", "sender null (closing signs shuffled within sender: the formation-ordered analogue of the Newcomb run's row-wise null)"),
                          ("v", "receiver null (closing signs shuffled within receiver: reception held)")):
        r = st["dk"][(null, "all", "event")]
        L.append(f"*{SITE_TITLES[site]}, {nulltxt}; whole period, each closing tie counted once (split over its forward-chain cells), {r['n_events']:,} closing ties with a forward-chain context.* "
                 f"Agreement of the eight directions with: Newcomb {r['agree_newcomb']}/8, 'closing = second tie' {r['agree_copy_second']}/8, strict balance {r['agree_balance']}/8.")
        L.append("")
        rows = []
        for i, t in enumerate(DK_TYPES):
            sd = {1: "over", -1: "under", 0: "-"}[int(r["side"][i])]
            rows.append([t, f"{r['obs'][i]:,.1f}", f"{r['mean'][i]:,.1f}", _t(r["z"][i], 1), _t(r["p_gt"][i]), sd,
                         {1: "over", -1: "under"}[DK_NEWCOMB_DIRECTION[t]], {1: "over", -1: "under"}[DK_BALANCE[t]]])
        L += md_table(["type", "observed", "null mean", "z", "p(obs > null)", "here", "Newcomb", "strict balance"], rows, "lrrrrlll")
        L.append("")
    return L


def render_rule_table() -> list[str]:
    """The sixteen types and what each rule says about the closing tie (the first formation-order state
    for the time-first rule is omitted: it is a table over 3 states)."""
    rows = []
    sg = {1: "+", -1: "-", 0: "."}
    for t in range(16):
        rows.append([TYPE_NAMES[t], sg[int(TYPE_S1[t] * TYPE_S2[t])], sg[int(DIRECTED_RULES["status"][t, 0])],
                     sg[int(DIRECTED_RULES["first_tie"][t, 0])], sg[int(DIRECTED_RULES["conjunction"][t, 0])],
                     sg[int(DIRECTED_RULES["copy_incoming"][t, 0])]])
    return md_table(["type (u->w, w->v, signs)", "strict balance", "status", "first-tie", "conjunction", "copy incoming"], rows, "lrrrrr")


VAR_HEAD = ["variant", "n test", "test +", "base", "recent", "strict", "weak", "first-tie", "status", "person", "16 types", "person+16",
            "first-tie - strict [CI]", "person+16 - person [CI]"]


def _star_best(vals: dict[str, float], names: tuple[str, ...]) -> str | None:
    cand = {n: vals[n] for n in names if n in vals and vals[n] == vals[n]}
    return min(cand, key=cand.get) if cand else None


def render_variation(rows: list[dict]) -> list[str]:
    body = []
    for r in rows:
        if r.get("skipped"):
            body.append([r["label"], f"{r['n_test']}", "-"] + ["too few"] + [""] * 10)
            continue
        best = _star_best(r, ("strict balance", "weak balance", "first-tie asymmetric", "status"))

        def cell(m, key=None):
            v = r.get(m)
            s = _t(v) if v is not None else "-"
            return f"**{s}**" if best == m else s

        d1 = _sci(*r["d_ft_strict"]) if "d_ft_strict" in r else "-"
        d2 = _sci(*r["d_p16_person"]) if "d_p16_person" in r else "-"
        body.append([r["label"], f"{r['n_test']:,}", _t(r["test_rate"], 2), cell("base rate"), cell("recent rate"), cell("strict balance"),
                     cell("weak balance"), cell("first-tie asymmetric"), cell("status"), cell("person propensity"),
                     cell("saturated 16 types"), cell("person + 16 types"), d1, d2])
    return md_table(VAR_HEAD, body)


def render_targets(rows: list[dict]) -> list[str]:
    models = ("base rate", "recent rate", "strict balance", "first-tie asymmetric", "person propensity", "person + reciprocity", "person + 16 types", "person + reciprocity + 16 types")
    body = []
    for r in rows:
        body.append([r["label"], f"{r['n_test']:,}", _t(r["test_rate"], 2)] + [_t(r[m]) for m in models] + [_sci(*r["d_recip16_recip"])])
    return md_table(["target set", "n test", "test +"] + ["base", "recent", "strict", "first-tie", "person", "person+recip", "person+16", "person+recip+16"] + ["(person+recip+16) - (person+recip) [CI]"], body)


FORM_CONTRASTS = [
    ("first-tie asymmetric", "strict (per instance)"), ("strict (per instance)", "strict balance"),
    ("weak (per instance)", "weak balance"), ("first-tie, FF only", "first-tie asymmetric"),
    ("first-tie, all forms", "first-tie asymmetric"), ("first-tie, time-first", "first-tie asymmetric"),
    ("copy incoming", "first-tie asymmetric"), ("conjunction", "weak balance"), ("person (rate form)", "person propensity"),
    ("A^2 sign (FF only)", "strict (per instance)"), ("A^2 sign (FF only)", "strict balance"),
]


def render_dk_summary(R: dict) -> list[str]:
    rows = []
    sd = {1: "over", -1: "under", 0: "-"}
    i_dll, i_dld, i_ddd = DK_TYPES.index("DLL"), DK_TYPES.index("DLD"), DK_TYPES.index("DDD")
    for site in SITE_NAMES:
        S = R["sites"][site]["static"]
        for null, nl in (("u", "sender"), ("uy", "sender x year"), ("v", "receiver")):
            for part, w in (("all", "event"), ("test", "event"), ("all", "instance")):
                if (null, part, w) not in S["dk"]:
                    continue
                r = S["dk"][(null, part, w)]
                rows.append([SITE_TITLES[site], nl, f"{'whole' if part == 'all' else 'test'}, {w}", f"{r['n_events']:,}",
                             f"{r['agree_newcomb']}/8", f"{r['agree_copy_second']}/8", f"{r['agree_balance']}/8",
                             f"{sd[int(r['side'][i_dll])]} (z {r['z'][i_dll]:+.1f})", f"{sd[int(r['side'][i_dld])]} (z {r['z'][i_dld]:+.1f})",
                             f"{sd[int(r['side'][i_ddd])]} (z {r['z'][i_ddd]:+.1f})"])
    return md_table(["site", "null", "period, weighting", "closing ties", "matches Newcomb", "matches 'closing = second tie'", "matches strict balance",
                     "DLL (Newcomb: over)", "DLD (Newcomb: under)", "DDD (Newcomb: over)"], rows, "lllrrrrlll")


#  Rows of the recode, split, ridge and horizon tables that ARE the pre-specified configuration (default recode, 70/30
#  split, ridge 1, election-start horizon): each table shows it as its reference row, and the embeddedness table already
#  has it as 'k >= 1'.  The win counts keep it once, so a site has 16 (Bitcoin) or 17 (wiki-RfA) distinct configurations.
PRIMARY_REPEAT_LABELS = (
    "all", "neutral: drop", f"split {int(TRAIN_FRAC * 100)}/{100 - int(TRAIN_FRAC * 100)}", f"ridge {L2:g}",
    "election start (primary)",
)


def variation_rows(R: dict, site: str) -> list[dict]:
    """The distinct variation configurations of a site (target-set rows excluded: a different model list), the
    pre-specified one once."""
    V = R["sites"][site]["variations"]
    return [r for k, v in V.items() if k != "targets" for r in v
            if not r.get("skipped") and not (k != "embeddedness" and r["label"] in PRIMARY_REPEAT_LABELS)]


def ft_ahead_rows(R: dict) -> list[tuple]:
    """Every distinct variation configuration in which the first-tie rule beats strict balance by its paired interval:
    (site, label, (point, lo, hi), first-tie log-loss, weak-balance log-loss)."""
    out = []
    for site in SITE_NAMES:
        for r in variation_rows(R, site):
            d = r.get("d_ft_strict")
            if d is not None and d[2] < 0:
                out.append((site, r["label"], tuple(d), r["first-tie asymmetric"], r["weak balance"]))
    return out


def render_winners(R: dict) -> list[str]:
    """Across every variation row of a site (embeddedness, recode, time design, ridge, horizon): which of the four
    canonical single rules has the lowest held-out log-loss, which model overall, and how often the paired intervals
    put the first-tie rule below or above strict balance, and the 16 types above or below the person terms alone."""
    from collections import Counter

    rows = []
    overall = ("person propensity", "saturated 16 types", "person + strict", "person + first-tie", "person + 16 types")
    for site in SITE_NAMES:
        rr = variation_rows(R, site)
        n = len(rr)
        br = Counter(min(CORE_RULES, key=lambda m: r[m]) for r in rr)
        bo = Counter(min(overall + CORE_RULES, key=lambda m: r[m]) for r in rr)
        ftb = sum(1 for r in rr if "d_ft_strict" in r and r["d_ft_strict"][2] < 0)
        ftw = sum(1 for r in rr if "d_ft_strict" in r and r["d_ft_strict"][1] > 0)
        p16b = sum(1 for r in rr if "d_p16_person" in r and r["d_p16_person"][2] < 0)
        p16w = sum(1 for r in rr if "d_p16_person" in r and r["d_p16_person"][1] > 0)
        spb = sum(1 for r in rr if "d_strict_person" in r and r["d_strict_person"][2] < 0)
        spw = sum(1 for r in rr if "d_strict_person" in r and r["d_strict_person"][1] > 0)
        rows.append([SITE_TITLES[site], str(n), ", ".join(f"{k.split()[0]} {v}" for k, v in br.most_common()),
                     ", ".join(f"{k} {v}" for k, v in bo.most_common()), f"{ftb} / {n - ftb - ftw} / {ftw}", f"{spb} / {n - spb - spw} / {spw}", f"{p16b} / {n - p16b - p16w} / {p16w}"])
    return md_table(["site", "distinct configurations", "best single rule (count)", "best model overall (count)",
                     "first-tie vs strict: better / tied / worse", "strict vs person: better / tied / worse", "person+16 vs person: better / tied / worse"], rows, "lrllrrr")


def render_forms(site: str, fr: dict) -> list[str]:
    res, pooled = fr["res"], fr["pooled"]
    best_single = min(res.point(("ll", m)) for m in FORM_MODELS if m in OWN_RULES)
    rows = []
    for m in sorted(FORM_MODELS, key=lambda m: res.point(("ll", m))):
        lo, hi, _ = res.ci(("ll", m))
        d_best = None
        rows.append([m, _ci(res.point(("ll", m)), lo, hi), _t(res.auc(m)) if m != "base rate" else "-",
                     _t(pooled.point(("ll", m))), _t(res.point(("acc", m, True))) if m in res.own else "-"])
    out = md_table(["model form (sorted by 70/30 log-loss)", "70/30 held-out log-loss [CI]", "AUC", "rolling-origin log-loss", "own accuracy"], rows)
    out.append("")
    rules = sorted([m for m in FORM_MODELS if m in OWN_RULES], key=lambda m: res.point(("ll", m)))
    anyf = sorted([m for m in FORM_MODELS if m != "base rate"], key=lambda m: res.point(("ll", m)))
    pt, lo, hi, _ = res.diff(rules[1], rules[0])
    pr = sorted([m for m in FORM_MODELS if m in OWN_RULES], key=lambda m: pooled.point(("ll", m)))
    out.append(f"**Best-fitting rule form: {rules[0]}** ({res.point(('ll', rules[0])):.3f}); the runner-up, {rules[1]} ({res.point(('ll', rules[1])):.3f}), is behind by {pt:+.3f} [{lo:+.3f}, {hi:+.3f}]. "
               f"Under the rolling origin the best rule form is {pr[0]} ({pooled.point(('ll', pr[0])):.3f}). Best of all forms listed, the person terms included: **{anyf[0]}** ({res.point(('ll', anyf[0])):.3f}). "
               f"The first-tie rule's own forms, best to worst: " + ", ".join(f"{m} {res.point(('ll', m)):.3f}" for m in sorted([m for m in FORM_MODELS if m.startswith("first-tie")], key=lambda m: res.point(("ll", m)))) + ".")
    out.append("")
    out += render_contrasts(res, FORM_CONTRASTS)
    return out


def _winner_counts(R: dict) -> dict:
    from collections import Counter

    out = {}
    for site in SITE_NAMES:
        rr = variation_rows(R, site)
        out[site] = (len(rr), Counter(min(CORE_RULES, key=lambda m: r[m]) for r in rr))
    return out


def verdict_text(R: dict) -> list[str]:
    S = R["sites"]
    A, B_, W = SITE_NAMES  # otc, alpha, wiki
    P = {s: S[s]["primary"] for s in SITE_NAMES}
    res = {s: P[s]["res"] for s in SITE_NAMES}
    pool = {s: P[s]["pooled"] for s in SITE_NAMES}

    def ll(s, m, r=None):
        return (r or res[s]).point(("ll", m))

    def trio(m, f="{:.3f}"):
        return " / ".join(f.format(ll(s, m)) for s in SITE_NAMES)

    def dif(s, a, b, r=None):
        pt, lo, hi, _ = (r or res[s]).diff(a, b)
        return f"{pt:+.3f} [{lo:+.3f}, {hi:+.3f}]"

    def cell(s, w, name):
        row = [r for r in S[s]["static"]["ff"] if r["weights"] == w and r["cell"] == name][0]
        return row

    def ffc(s, name="mp - pm", w="event"):
        r = cell(s, w, name)
        return f"{r['p_pos']:+.2f} [{r['lo']:+.2f}, {r['hi']:+.2f}]"

    def dk(s, null, part="all", w="event"):
        return S[s]["static"]["dk"][(null, part, w)]

    def dll(s, null, part="all", w="event"):
        r = dk(s, null, part, w)
        i = DK_TYPES.index("DLL")
        return f"{'above' if r['side'][i] > 0 else 'below'} its null (z {r['z'][i]:+.1f})"

    nw = _winner_counts(R)
    tot = sum(n for n, _ in nw.values())
    weak_wins = sum(c["weak balance"] for _, c in nw.values())
    ft_wins = sum(c["first-tie asymmetric"] for _, c in nw.values())
    st_wins = sum(c["strict balance"] for _, c in nw.values())
    status_wins = sum(c["status"] for _, c in nw.values())

    short = {"bitcoin-otc": "OTC", "bitcoin-alpha": "Alpha", "wiki-rfa": "wiki-RfA"}
    ahead = ft_ahead_rows(R)
    ahead_txt = ", ".join(f"{short[s_]} {lab}" for s_, lab, *_ in ahead) or "none"
    weak_lowest = all(min(CORE_RULES, key=lambda m: ll(s_, m)) == "weak balance" for s_ in SITE_NAMES)
    i_dll = DK_TYPES.index("DLL")

    L: list[str] = []
    A_ = L.append
    A_("**Bottom line.** By the criterion that `models/00-v0.md` section 7 states for the directed law (4.2d) (*if DLL is depleted like LLD, (4.2d) is refuted and the symmetric rule returns*), (4.2d) is refuted on "
       f"Bitcoin OTC and Alpha, where DLL is depleted and balance returns (on Alpha by the whole-period null; the test period alone gives z {dk(B_, 'u', 'test')['z'][i_dll]:+.1f}), "
       f"and reproduced, weakly, on wiki-RfA (DLL z {dk(W, 'u')['z'][i_dll]:+.1f}), where it is a reception pattern: it reverses when reception is held, "
       "it is indistinguishable from zero once the person terms are in, and the rule built from it predicts no better than balance at the pre-specified split "
       f"(it beats strict balance by its interval in {len(ahead)} of {tot} variation configurations: {ahead_txt}). "
       + ("Weak balance has the lowest held-out log-loss of the four canonical single triad rules on every site at the pre-specified split, level with strict balance (and on Alpha with the first-tie rule); "
          if weak_lowest else "Weak balance is level with or ahead of the other canonical single triad rules at the pre-specified split; ")
       + "the person terms predict more than any triad rule except on Bitcoin OTC.")
    A_("")
    A_("**In short.**")
    A_("")
    A_("- *Best of the four canonical single rules: weak balance; strict balance is level with it; the first-tie rule is never ahead of weak balance at the pre-specified split (level with strict balance on Alpha and wiki-RfA); status is last.* "
       "Held-out log-loss at the pre-specified split "
       f"(OTC / Alpha / wiki-RfA; lower is better): weak {trio('weak balance')}, strict {trio('strict balance')}, first-tie {trio('first-tie asymmetric')}, "
       f"status {trio('status')}, person propensity {trio('person propensity')}, training base rate {trio('base rate')}, recent rate {trio('recent rate')}. "
       f"Weak balance has the lowest log-loss of the four canonical single rules in {weak_wins} of {tot} distinct variation configurations "
       f"(OTC {nw[A][1]['weak balance']} of {nw[A][0]}, Alpha {nw[B_][1]['weak balance']} of {nw[B_][0]}, wiki-RfA {nw[W][1]['weak balance']} of {nw[W][0]}; the pre-specified configuration, which several tables repeat, counted once), "
       f"the first-tie rule in {ft_wins} (OTC {nw[A][1]['first-tie asymmetric']}, Alpha {nw[B_][1]['first-tie asymmetric']}, wiki-RfA {nw[W][1]['first-tie asymmetric']}), strict balance in {st_wins}, status in {status_wins}; "
       f"the first-tie rule beats strict balance by its paired interval in {len(ahead)} ({ahead_txt}) (section 5.5). "
       f"Weak against strict: OTC {dif(A, 'weak balance', 'strict balance')}, Alpha {dif(B_, 'weak balance', 'strict balance')}, wiki-RfA {dif(W, 'weak balance', 'strict balance')}. "
       f"Status is not distinguishable from the training base rate on Alpha ({dif(B_, 'status', 'base rate')}). LHK's learned conjunction pattern, a fifth rule we added, is ahead of weak balance on wiki-RfA "
       f"({dif(W, 'conjunction', 'weak balance')}) and behind it on OTC ({dif(A, 'conjunction', 'weak balance')}) and level on Alpha ({dif(B_, 'conjunction', 'weak balance')}).")
    A_("")
    L += _verdict_table(R)
    A_("")
    A_("- *Person terms against triad terms.* On **Alpha** and **wiki-RfA** the person-propensity baseline beats every single triad rule "
       f"(strict - person: Alpha {dif(B_, 'strict balance', 'person propensity')}, wiki-RfA {dif(W, 'strict balance', 'person propensity')}) and the triad terms add little to it "
       f"(16 types - person: Alpha {dif(B_, 'person + 16 types', 'person propensity')} at the split and {dif(B_, 'person + 16 types', 'person propensity', pool[B_])} rolling; "
       f"wiki-RfA {dif(W, 'person + 16 types', 'person propensity')}). On **OTC** it does not: strict balance alone beats the person terms alone at the pre-specified split "
       f"({dif(A, 'strict balance', 'person propensity')}; AUC {res[A].auc('strict balance'):.3f} against {res[A].auc('person propensity'):.3f}), the triad terms add a great deal to them "
       f"({dif(A, 'person + 16 types', 'person propensity')}), and the best model is person + strict balance ({ll(A, 'person + strict'):.3f}). Under the rolling origin the OTC gap shrinks to "
       f"{dif(A, 'strict balance', 'person propensity', pool[A])}. So 112 section 6.5 test 2 ('person terms dominate') is supported on two sites; on OTC it fails at the pre-specified split and the two are level under the rolling origin.")
    A_("")
    A_("- *Does the first-tie asymmetry replicate outside the fraternity? As a static pattern, on one site of three, weakly; as a predictor, not ahead of balance at the pre-specified split, and ahead of strict balance "
       f"by its interval in {len(ahead)} of {tot} variation configurations; given the person terms, nowhere.*")
    A_(f"  - *Static, under the formation-ordered analogue of the Newcomb run's row-wise null (closing signs shuffled within sender, the context ties held; each closing tie counted once):* the eight directions of the fraternity are reproduced on **wiki-RfA** "
       f"({dk(W, 'u')['agree_newcomb']}/8; DLL {dll(W, 'u')}, whole period; {dk(W, 'u', 'test')['agree_newcomb']}/8 in the test period alone), not on **Alpha** "
       f"({dk(B_, 'u')['agree_newcomb']}/8; DLL {dll(B_, 'u')}) and not on **OTC** ({dk(A, 'u')['agree_newcomb']}/8; DLL {dll(A, 'u')}, and the eight directions are those of strict balance, {dk(A, 'u')['agree_balance']}/8). "
       f"With reception held (closing signs shuffled within receiver) the two directions that carry the asymmetry, DLL above and DLD below, are reversed on all three: DLL is below its null (OTC z {dk(A, 'v')['z'][4]:+.1f}, "
       f"Alpha {dk(B_, 'v')['z'][4]:+.1f}, wiki-RfA {dk(W, 'v')['z'][4]:+.1f}). "
       + (f"The agreement counts under the sender null, and the side of DLL under both nulls, do not depend on the weighting (each tie once or every triad), "
          f"on the period (whole or test only) or on holding the sender and the year together (section 4.2); the sizes do (Alpha's DLL under the sender null, test period alone: z {dk(B_, 'u', 'test')['z'][i_dll]:+.1f})."
          if _dk_stable(S) else "The agreement counts or the side of DLL change with the weighting, the period or the sender-by-year null on at least one site (section 4.2)."))
    A_(f"  - *Cell contrast* P(closing +) after (first -, second +) minus after (first +, second -), which strict balance puts at zero and the asymmetry makes positive: OTC {ffc(A)}, "
       f"**Alpha {ffc(B_)}**, wiki-RfA {ffc(W)} (reversed). Alpha has the asymmetry between the two one-negative starts, in the raw cells.")
    A_(f"  - *Predictive.* The first-tie rule minus strict balance in held-out log-loss: OTC {dif(A, 'first-tie asymmetric', 'strict balance')} (rolling {dif(A, 'first-tie asymmetric', 'strict balance', pool[A])}), "
       f"Alpha {dif(B_, 'first-tie asymmetric', 'strict balance')}, wiki-RfA {dif(W, 'first-tie asymmetric', 'strict balance')}; on the closing ties where the two rules can differ "
       f"(a forward chain with a negative first tie) OTC {dif(A, 'first-tie asymmetric', 'strict balance', P[A]['res_dis'])}, Alpha {dif(B_, 'first-tie asymmetric', 'strict balance', P[B_]['res_dis'])}, "
       f"wiki-RfA {dif(W, 'first-tie asymmetric', 'strict balance', P[W]['res_dis'])}. Against weak balance on wiki-RfA it is worse ({dif(W, 'first-tie asymmetric', 'weak balance')}). "
       f"Beside the person terms the first-tie rule adds less than balance on OTC (person + first-tie - person + strict {dif(A, 'person + first-tie', 'person + strict')}) and the same on wiki-RfA "
       f"({dif(W, 'person + first-tie', 'person + strict')}); on Alpha it is nominally the best addition ({dif(B_, 'person + first-tie', 'person + strict')}; rolling {dif(B_, 'person + first-tie', 'person + strict', pool[B_])}; "
       f"disagreement subset {dif(B_, 'person + first-tie', 'person + strict', P[B_]['res_dis'])}), a hint that clears no interval. "
       + _ahead_txt(R, ahead))
    A_(f"  - *Given the person terms* the coefficient contrast FFmp - FFpm that the asymmetry makes positive is {_ci_txt(S[A]['static']['coef']['mp_minus_pm'])} (OTC), "
       f"{_ci_txt(S[B_]['static']['coef']['mp_minus_pm'])} (Alpha), {_ci_txt(S[W]['static']['coef']['mp_minus_pm'])} (wiki-RfA; {S[A]['static']['coef'].get('B', 100):,} cluster-bootstrap refits): "
       "zero within the interval, the Bitcoin point estimates on the wrong side for an asymmetry. "
       + _balance_txt(R))
    A_("")
    A_("- *What the fraternity's pattern was.* Re-read post hoc, D&K's eight-type pattern in the Newcomb ranks is, from the second wave on, exactly the partition 'the closing tie has the sign of the second tie' "
       f"(8 of 8 cells in {int((R['newcomb']['agree_copy_row'][1:] == 8).sum())} of 14 waves under the row-wise null), so the first tie takes no part in it; under a column-wise null that holds each man's popularity it shrinks to about chance "
       f"(agreement {int(R['newcomb']['agree_copy_col'].min())}-{int(R['newcomb']['agree_copy_col'].max())} of 8, |z| <= {R['newcomb']['max_abs_z_col'].max():.1f}). What the Newcomb run called a first-tie asymmetry is "
       "a consensus about the third man, in the sense that it disappears when each man's popularity is held. Reception is what the sender null leaves free and the receiver null removes, which is why wiki-RfA reproduces the pattern under the first and loses it under the second."
       if R.get("newcomb") is not None else "- (Newcomb ranks absent: re-read skipped.)")
    A_("")
    C = S[W]["converting"]["res"]
    A_(f"- *Converting ties (wiki-RfA re-votes).* Persistence alone gives {C.point(('ll', 'base rate')):.3f}; adding the context of weak balance {C.point(('ll', 'weak balance')):.3f} ({dif(W, 'weak balance', 'base rate', C)}), "
       f"strict {C.point(('ll', 'strict balance')):.3f}, first-tie {C.point(('ll', 'first-tie asymmetric')):.3f} ({dif(W, 'first-tie asymmetric', 'strict balance', C)} against strict), status "
       f"{C.point(('ll', 'status')):.3f} ({dif(W, 'status', 'base rate', C)}); the person terms {C.point(('ll', 'person propensity')):.3f}. Rules help a little, balance most, and the 16 types add nothing to the person terms "
       f"({dif(W, 'person + 16 types', 'person propensity', C)}). Conversion is not decided by any rule.")
    A_("")
    A_("**Status of `models/00-v0.md` section 4.2 as now written (v0.2.1): (4.2b) strict balance as a structure theorem, (4.2d) the directed law, (4.2e) weak balance as a depletion.**")
    A_("")
    cells_ok = {s_: dk(s_, "u")["agree_copy_second"] // 2 for s_ in SITE_NAMES}
    A_(f"- *(4.2d), the directed law (a two-factor product rule on the ties into the third person): refuted by section 7's own criterion on two of three sites, reproduced, weakly, on the third, and where it reproduces it is reception.* "
       f"Against the row-wise (sender) null, in its formation-ordered form, DLL is depleted like LLD on OTC (z {dk(A, 'u')['z'][DK_TYPES.index('DLL')]:+.1f}) and on Alpha (z {dk(B_, 'u')['z'][DK_TYPES.index('DLL')]:+.1f}), and the symmetric rule returns: all eight directions on OTC "
       f"are those of strict balance ({dk(A, 'u')['agree_balance']}/8), on Alpha {dk(B_, 'u')['agree_balance']}/8 with the two misses in the (-,-) cells where weak balance is silent. "
       f"On Alpha the refutation rests on the whole period: the test period alone gives z {dk(B_, 'u', 'test')['z'][i_dll]:+.1f}, and the raw cells do show the asymmetry (mp - pm {ffc(B_)}), "
       "which holding each sender's own mix removes. On wiki-RfA DLL is enriched "
       f"(z {dk(W, 'u')['z'][DK_TYPES.index('DLL')]:+.1f}) and the partition reproduces. Cells of the four that follow the two-factor partition: wiki-RfA {cells_ok[W]}, Alpha {cells_ok[B_]}, OTC {cells_ok[A]} (OTC fails in both "
       "first-tie-negative cells, where it follows the three-factor product). What reproduces involves only the two ties into the third person, which is a statement about that person's reception and not a triadic law; "
       f"it reverses when reception is held (DLL below its receiver null on all three, z {dk(A, 'v')['z'][DK_TYPES.index('DLL')]:+.1f} / {dk(B_, 'v')['z'][DK_TYPES.index('DLL')]:+.1f} / {dk(W, 'v')['z'][DK_TYPES.index('DLL')]:+.1f}), the contrast "
       "it predicts is indistinguishable from zero once the person terms are in, and the forward-chain rule built from it predicts no better than the three-factor product at the pre-specified split (above). The post hoc Newcomb re-read says the same of the fraternity. "
       "The reading of the third person as a contested Object, DLL as R-C's rivalry (section 4.2, 'ours and untested'), was read from the DLL-over pattern; that pattern shrinks to within "
       + (f"{R['newcomb']['max_abs_z_col'].max():.1f} SD" if R.get("newcomb") is not None else "a few SD")
       + " of its null once each man's popularity is held (section 4.1), so it is not evidence for rivalry.")
    def zz(s_, t):
        return dk(s_, "u")["z"][DK_TYPES.index(t)]

    i_ddd = DK_TYPES.index("DDD")
    otc_ddd_under = all(int(r["side"][i_ddd]) == -1 for r in S[A]["static"]["dk"].values())
    cA, cB, cW = (S[s_]["static"]["coef"]["cells"]["FFmm"] for s_ in SITE_NAMES)

    def excl(c):
        return c[1] > 0 or c[2] < 0

    A_("- *(4.2e), weak balance as a depletion: the depletion of LLD and LDL is supported on all three sites; the Davis half, an all-negative closing that is not depleted, on Alpha and wiki-RfA but not on OTC; "
       "as a predictor weak balance is not worse than strict balance at the pre-specified split on any site.* "
       f"Two of the three one-negative closings, LLD and LDL, are below the sender null on all three sites but present (OTC z {zz(A, 'LLD'):+.1f} / {zz(A, 'LDL'):+.1f}, Alpha {zz(B_, 'LLD'):+.1f} / {zz(B_, 'LDL'):+.1f}, "
       f"wiki-RfA {zz(W, 'LLD'):+.1f} / {zz(W, 'LDL'):+.1f}); the third, DLL, is the (4.2d) cell above. The all-negative closing DDD, the cell that separates Davis from Heider, is above the sender null on Alpha "
       f"(z {zz(B_, 'DDD'):+.1f}) and wiki-RfA ({zz(W, 'DDD'):+.1f}) and below it on OTC ({zz(A, 'DDD'):+.1f}{'; below its null in every variant of section 4.2' if otc_ddd_under else ''}), strict balance's direction. "
       f"On Bitcoin the (-,-) start closes positive (FFmm {cell(A, 'event', 'FFmm')['p_pos']:.0%} on OTC, {cell(B_, 'event', 'FFmm')['p_pos']:.0%} on Alpha, each tie once, against {cell(A, 'event', 'FFpm')['p_pos']:.0%} "
       f"and {cell(A, 'event', 'FFmp')['p_pos']:.0%} for the mixed starts on OTC), and weak balance, silent there, loses nothing in log-loss (the start is rare: {cell(A, 'event', 'FFmm')['events']:,} and "
       f"{cell(B_, 'event', 'FFmm')['events']:,} closing ties); on wiki-RfA weak balance is ahead of strict ({dif(W, 'weak balance', 'strict balance')}), and the (-,-) vote carries nothing once the person terms are in. "
       "The product structure of balance survives the person terms on Bitcoin and is faint on wiki-RfA "
       "(section 4.6). The learned FFmm coefficient of L4833 (-0.73 / -0.59 / -0.77, balance says +1) **does not transfer** to 2010-16 Bitcoin, where the person-adjusted coefficient is "
       f"{_ci_txt(cA)} (OTC) and {_ci_txt(cB)} (Alpha), on {cell(A, 'event', 'FFmm')['events']:,} and {cell(B_, 'event', 'FFmm')['events']:,} closing ties "
       + ("(modest support, intervals excluding zero)" if excl(cA) and excl(cB) else "(an interval that includes zero on at least one of the two)")
       + (", and is zero within its interval on wiki-RfA (112 section 6.5 test 1)." if not excl(cW) else f", and is {_ci_txt(cW)} on wiki-RfA (112 section 6.5 test 1)."))
    status_last = (all(max(CORE_RULES, key=lambda m: ll(s_, m)) == "status" for s_ in SITE_NAMES)
                   and all(max(CORE_RULES, key=lambda m: r[m]) == "status" for s_ in SITE_NAMES for r in variation_rows(R, s_)))
    status_trivial = all(res[s_].point(("acc", "status", True)) < res[s_].test_rate for s_ in SITE_NAMES)
    fW = S[W]["forms"]["res"]
    a2_w_base = fW.diff("A^2 sign (FF only)", "base rate")
    A_("- *(4.2b), strict balance as a structure theorem:* a theorem, untouched by data. As an empirical rule it is level in size with weak balance on Bitcoin "
       f"(weak - strict: OTC {dif(A, 'weak balance', 'strict balance')}, Alpha {dif(B_, 'weak balance', 'strict balance')}) and behind it on wiki-RfA. "
       "*Behind balance on these data (each carries signal on some site, so 'refuted' would overstate it):* status as a triad rule ("
       + ("last of the four canonical rules at the pre-specified split and in every variation configuration" if status_last else "behind balance at the pre-specified split")
       + ("; its own hard predictions are below the always-positive accuracy on all three sites" if status_trivial else "")
       + f"; as features, against the base rate: OTC {dif(A, 'status', 'base rate')}, Alpha {dif(B_, 'status', 'base rate')}, wiki-RfA {dif(W, 'status', 'base rate')}); "
       "and the kinetic law (4.2a), dA/dt = A^2, read as a sign predictor for a new tie (the net product vote of the forward chains alone), which is worse than direction-free balance on OTC "
       f"({dif(A, 'A^2 sign (FF only)', 'strict balance', S[A]['forms']['res'])}) and wiki-RfA ({dif(W, 'A^2 sign (FF only)', 'strict balance', fW)}"
       + (f"; there it is no better than the base rate, {a2_w_base[0]:+.3f} [{a2_w_base[1]:+.3f}, {a2_w_base[2]:+.3f}]" if a2_w_base[1] < 0 < a2_w_base[2] else "")
       + f") and level on Alpha ({dif(B_, 'A^2 sign (FF only)', 'strict balance', S[B_]['forms']['res'])}); using direction does not help.")
    A_("- *Supported otherwise:* the person-propensity terms as the larger part of the predictable sign on Alpha and wiki-RfA, with the triad terms adding a small, real amount (wiki-RfA) or a large one (OTC); "
       "and, post hoc, the reading of the Newcomb first-tie pattern as reception.")
    A_("- *Not decided:* whether a rivalry mechanism of D&K's kind exists beyond reception in a small closed group, where reception can be held and the first tie is a rival's (the sender and receiver nulls each hold one person effect, "
       "the person-adjusted contrast holds both approximately and finds nothing distinguishable from zero, but none of the three media is a rivalry setting); "
       f"whether the wiki-RfA static agreement (DLL {dll(W, 'u')}) is anything but reception; whether the directed distinctions matter at all (the 16-type model against weak balance: "
       f"OTC {dif(A, 'saturated 16 types', 'weak balance')}, Alpha {dif(B_, 'saturated 16 types', 'weak balance')}, wiki-RfA {dif(W, 'saturated 16 types', 'weak balance')}); and the dynamical half of section 7 "
       "(conversion of a standing tie: no Bitcoin tie is re-signed, and the wiki-RfA re-votes are re-ratings of a re-run candidate; the dedicated conversion test is `results/wikirfa_conversion.md`).")
    A_("- *For section 4.2 (a proposal, Aldred's call):* demote (4.2d) from a directed law to a **reception term**: in the Newcomb data and on wiki-RfA the sign of a tie into k agrees with the other ties into k beyond the sender's own mix; "
       "write the triad law as a **table of conditional sign probabilities over the 16 directed types, per site and period, estimated beside the person terms**, with weak balance as the structure it is closest to on Bitcoin and no first-tie term; "
       "withdraw the rivalry reading of DLL until a setting that can hold reception supplies it. A decisive test of the asymmetry as rivalry needs a signed panel of a small group with an independent measure of each member's popularity, "
       "which this ledger does not have.")
    return L


def _ci_txt(t, d: int = 2) -> str:
    return f"{t[0]:+.{d}f} [{t[1]:+.{d}f}, {t[2]:+.{d}f}]"


def _dk_stable(S: dict) -> bool:
    """True when, on every site, the sender-null agreement counts are the same in every variant of section 4.2 (weighting,
    period, sender by year) and the side of DLL is the same within the sender variants and within the receiver variants."""
    i = DK_TYPES.index("DLL")
    for site in SITE_NAMES:
        dk = S[site]["static"]["dk"]
        su = [r for k, r in dk.items() if k[0] in ("u", "uy")]
        sv = [r for k, r in dk.items() if k[0] == "v"]
        if len({(r["agree_newcomb"], r["agree_copy_second"], r["agree_balance"]) for r in su}) != 1:
            return False
        if len({int(r["side"][i]) for r in su}) != 1 or len({int(r["side"][i]) for r in sv}) != 1:
            return False
    return True


def _ahead_txt(R: dict, ahead: list[tuple]) -> str:
    """The verdict's sentence on the variation configurations in which the first-tie rule beats strict balance by its
    interval (ft_ahead_rows), each with what it is."""
    short = {"bitcoin-otc": "OTC", "bitcoin-alpha": "Alpha", "wiki-rfa": "wiki-RfA"}
    if not ahead:
        return "In no variation configuration is the first-tie rule ahead of strict balance by its interval (section 5.5)."
    items = []
    for site, label, (pt, lo, hi), ft, wk in ahead:
        ci = f"{pt:+.3f} [{lo:+.3f}, {hi:+.3f}]"
        if label == "every earlier dated vote":
            items.append(f"{short[site]}'s vote-level horizon, where a voter sees the same election's earlier votes ({ci}); it is still behind weak balance there ({ft:.3f} against {wk:.3f}), "
                         "and a rule that copies the earlier votes on the candidate is the herding setting, which is reception again")
        elif label.startswith("ridge "):
            rows = {r["label"]: r for r in R["sites"][site]["variations"]["ridge"]}
            p0, rr = rows.get(f"ridge {L2:g}"), rows[label]
            extra = (f", a penalty under which strict balance worsens from {p0['strict balance']:.3f} (ridge {L2:g}) to {rr['strict balance']:.3f} and the first-tie rule only from "
                     f"{p0['first-tie asymmetric']:.3f} to {ft:.3f}" if p0 else "")
            items.append(f"{short[site]} at {label} ({ci}; first-tie {ft:.3f} against weak balance {wk:.3f}){extra}")
        else:
            items.append(f"{short[site]}, {label} ({ci}; first-tie {ft:.3f}, weak balance {wk:.3f})")
    n = len(items)
    return (f"The {'one variation configuration' if n == 1 else f'{n} variation configurations'} in which the first-tie rule is ahead of strict balance by its interval (section 5.5): "
            + "; ".join(items) + ".")


def _n2_caveat(R: dict) -> str:
    """Section 4.7: where the permutation null (N2) and the paired bootstrap of section 3 disagree about an addition to the
    person terms (N2 p <= 0.05 while the paired interval of the held-out log-loss difference includes zero)."""
    names = {"16 types": "person + 16 types", "strict balance": "person + strict", "weak balance": "person + weak",
             "first-tie asymmetric": "person + first-tie", "status": "person + status"}
    parts = []
    for site in SITE_NAMES:
        res = R["sites"][site]["primary"]["res"]
        bad = []
        for nm, r in R["sites"][site]["static"]["added"].items():
            m = names.get(nm)
            if m is None or m not in res.cal:
                continue
            pt, lo, hi, _ = res.diff(m, "person propensity")
            if r["p"] <= 0.05 and hi >= 0:
                floor = 1.0 / (r["n_perm"] + 1)
                ptxt = f"<= {floor:.3f}" if r["p"] <= floor + 1e-12 else f"{r['p']:.3f}"
                bad.append(f"{m} - person {pt:+.3f} [{lo:+.3f}, {hi:+.3f}] against N2 p {ptxt}")
        if bad:
            parts.append(f"{SITE_TITLES[site]}: " + "; ".join(bad))
    head = ("The null is anti-conservative where the refit overfits: a feature that duplicates the person terms overfits less than a shuffled one, so an addition with no held-out gain "
            "can still beat a null whose mean gain is negative. ")
    if not parts:
        return head + "Here every addition that N2 calls beyond noise also has a paired bootstrap interval (section 3) wholly below zero."
    return (head + "Where N2 and the paired bootstrap of section 3 disagree (N2 p <= 0.05 while the paired interval of the held-out log-loss difference includes zero), "
            "the interval is the reading: " + " | ".join(parts) + ".")


PRESPECIFIED_CONTRASTS = (
    [(m, "base rate") for m in CORE_RULES + ("person propensity",)]
    + [(m, "person propensity") for m in CORE_RULES]
    + [("first-tie asymmetric", b) for b in ("strict balance", "weak balance", "status")]
    + [("person + 16 types", "person propensity")]
)  # the contrasts of interest fixed in the design (module docstring), per site


def _mc_caveat(R: dict) -> str:
    """The multiple-comparisons caveat, with the pre-specified contrasts that a Bonferroni correction would not pass."""
    from scipy.stats import norm

    n = len(PRESPECIFIED_CONTRASTS) * len(SITE_NAMES)
    thr = 0.05 / n
    mid = []
    for s in SITE_NAMES:
        P = R["sites"][s]["primary"]
        for a, b in PRESPECIFIED_CONTRASTS:
            pt, lo, hi, p = P["res"].diff(a, b)
            if thr <= p < 0.05:
                rp = P["pooled"].diff(a, b)
                mid.append(f"{SITE_TITLES[s]} {a} - {b} {pt:+.3f} [{lo:+.3f}, {hi:+.3f}], p {p:.3f} (rolling origin {rp[0]:+.3f} [{rp[1]:+.3f}, {rp[2]:+.3f}], p {_p(rp[3])})")
    zw = R["sites"]["wiki-rfa"]["static"]["dk"][("u", "all", "event")]["z"][DK_TYPES.index("DLL")]
    pw = float(2 * norm.sf(abs(zw)))
    txt = (f"No correction is made for the many comparisons: section 3 alone has {len(CONTRASTS_PRIMARY)} paired contrasts per site, and sections 4 and 5 add more; all but the pre-specified ones are descriptive. "
           f"Of the {n} pre-specified contrasts ({len(PRESPECIFIED_CONTRASTS)} per site: each rule and the person terms against the base rate, each rule against the person terms, the first-tie rule against "
           "strict, weak and status, the 16 types added to the person terms), ")
    txt += (f"those with p between the Bonferroni threshold {thr:.4f} and 0.05 are: " + "; ".join(mid) + ". " if mid
            else f"none has p between the Bonferroni threshold {thr:.4f} and 0.05. ")
    txt += (f"The static criterion is one pre-specified cell (DLL) on three sites: wiki-RfA's z {zw:+.1f} (two-sided p {pw:.3f}) "
            + ("passes" if pw < 0.05 / 3 else "does not pass") + " a correction for three sites (0.017) and "
            + ("passes" if pw < 0.05 / 12 else "does not pass") + " one over the four coupled cells of three sites (0.004).")
    return txt


def _balance_txt(R: dict) -> str:
    S = R["sites"]
    parts = []
    for s in SITE_NAMES:
        b = S[s]["static"]["coef"].get("balance_interaction")
        if b is not None:
            parts.append(f"{_ci_txt(b)} ({ {'bitcoin-otc': 'OTC', 'bitcoin-alpha': 'Alpha', 'wiki-rfa': 'wiki-RfA'}[s] })")
    if not parts:
        return ""
    return ("The product structure of balance, (FFpp + FFmm) - (FFpm + FFmp) in the same model, is " + ", ".join(parts) + ".")


def _verdict_table(R: dict) -> list[str]:
    S = R["sites"]
    rows = []
    res = {s: S[s]["primary"]["res"] for s in SITE_NAMES}
    rows.append(["always positive (accuracy = test positive share)"] + sum([[_t(res[s].test_rate), "-"] for s in SITE_NAMES], []))
    spec = [("training base rate", "base rate", False), ("recent rate", "recent rate", False), ("strict balance", "strict balance", True), ("weak balance", "weak balance", True),
            ("first-tie asymmetric", "first-tie asymmetric", True), ("status", "status", True), ("person propensity", "person propensity", False),
            ("person + weak balance", "person + weak", False), ("person + 16 types", "person + 16 types", False)]
    for label, m, own in spec:
        row = [label]
        for s in SITE_NAMES:
            r = res[s]
            lo, hi, _ = r.ci(("ll", m))
            row += [_t(r.point(("acc", m, own))), _ci(r.point(("ll", m)), lo, hi)]
        rows.append(row)
    L = ["Accuracy and held-out log-loss per rule per site (pre-specified 70/30 split; accuracy is the rule's own majority-vote prediction with silence to +, or the model's at 0.5; log-loss is the calibrated one with its 95% cluster-bootstrap interval; "
         "balanced accuracy, AUC and the rolling-origin results are in section 3):", ""]
    L += md_table(["model", "OTC accuracy", "OTC log-loss", "Alpha accuracy", "Alpha log-loss", "wiki-RfA accuracy", "wiki-RfA log-loss"], rows)
    names = {"bitcoin-otc": "OTC", "bitcoin-alpha": "Alpha", "wiki-rfa": "wiki-RfA"}
    parts = []
    for s in SITE_NAMES:
        best = max(res[s].point(("acc", m, True)) for m in CORE_RULES)
        parts.append(f"{names[s]} {best:.3f} against {res[s].test_rate:.3f}")
    pa = [res["wiki-rfa"].point(("acc", m, False)) for m in ("person propensity", "person + weak", "person + 16 types")]
    rw = res["wiki-rfa"]
    shares, precs = [], []
    for m in ("strict balance", "weak balance", "first-tie asymmetric"):
        hat = rw.own[m][0]
        neg = hat == 0
        shares.append(float(neg.mean()))
        precs.append(float((rw.y[neg] == 0).mean()) if neg.any() else float("nan"))
    L += ["", "Read accuracy against the first row. The best accuracy of any of the four rules' own predictions against always-positive: " + "; ".join(parts) +
          f". On wiki-RfA none of the rules' own predictions reaches the trivial accuracy: strict, weak and first-tie vote negative on {min(shares):.0%}-{max(shares):.0%} of the test votes and are right "
          f"{min(precs):.0%}-{max(precs):.0%} of the time when they do (the positive class is {rw.test_rate:.0%} of the test votes). Log-loss and AUC are the fairer scores there, and only the person-based models clear the "
          f"trivial accuracy ({min(pa):.3f}-{max(pa):.3f})."]
    return L


def render_report(R: dict) -> str:
    import datetime as _dt

    q = R["quick"]
    L: list[str] = []
    A = L.append
    A("# Which directed triad rule best predicts the sign of a closing or converting tie?")
    A("")
    A(f"_Generated {_dt.date.today().isoformat()} by `uv run python -m models.triad_rule_comparison report` (seed {SEED}"
      f"{'; QUICK MODE, Monte-Carlo sizes cut, do not cite' if q else ''}). Code: `sim/models/triad_rule_comparison.py`; checks: "
      "`sim/tests/test_triad_rule_comparison.py`. Ledger ids are the `id` fields of `docs/ledger.jsonl` entries (not always line numbers), named in the module docstring. "
      "Results are computed statistics only; the data files are local-use-only, git-ignored and not redistributed (`sim/data/README.md`)._")
    A("")
    A("**What was tested.** `models/00-v0.md` section 4.2 (v0.2.1) carries three statements about triads: (4.2b) strict balance as a structure theorem; (4.2d) a **directed law**, a two-factor product rule on the two ties into "
      "the third person, sgn(a_ik)·sgn(a_jk) = +, independent of the first tie i -> j, which is D&K's first-tie partition of the eight ordered-triple types {LLL, LDD, DLL, DDD} enriched and {LLD, LDL, DLD, DDL} depleted "
      "[hypothesis; one group of 17 men]; and (4.2e) weak balance as a depletion, not a prohibition. Its section 7 states the test: reproduce the partition against a row-wise sign-shuffle null in a longitudinal "
      "explicit-sign panel; *if DLL is depleted like LLD, (4.2d) is refuted and the symmetric rule returns*; and it asks for a side-by-side of directed triad rules. Here five rules compete to predict the sign of a tie "
      "that **closes** a triad (or, in wiki-RfA, **re-signs** a tie), on three formation-ordered, explicit-sign data sets, with models fitted on the past and scored on the future: strict balance (the product rule), "
      "weak (Davis) balance, the first-tie asymmetric rule (on a forward chain it is (4.2d): the closing tie takes the sign of the second tie), Leskovec et al.'s status rule, and a person-propensity baseline "
      "(sender and receiver sign tendencies from earlier ties). The static test of section 7 is run too, on the same data.")
    A("")
    A("## Verdict")
    A("")
    L += verdict_text(R)
    A("")
    # ---------------------------------------------------------------- 1
    A("## 1. Data, terms, target sets")
    A("")
    A("- **Bitcoin OTC and Bitcoin Alpha** (SNAP `soc-sign-bitcoinotc.csv.gz`, 397,258 bytes; `soc-sign-bitcoinalpha.csv.gz`, 149,480 bytes). "
      "Pseudonymous traders rate one another from -10 to +10 after a trade; Kumar, Spezzano, Subrahmanian & Faloutsos (2016), Edge weight prediction in weighted signed networks, ICDM, "
      "doi:10.1109/ICDM.2016.0033, and Kumar, Hooi, Makhija, Kumar, Faloutsos & Subrahmanian (2018), REV2: fraudulent user prediction in rating platforms, WSDM, doi:10.1145/3159652.3159729 "
      "(the two papers the SNAP pages ask users to cite). "
      "**Terms:** none stated by SNAP [L4567]; fetched for local use into git-ignored `sim/data/bitcoin/`, never committed, sha256 recorded in `sim/data/README.md`. "
      "OTC: 35,592 ratings, 5,881 nodes, 90.0% positive [L4568], unique sub-second timestamps; Alpha: 24,186 ratings, 3,783 nodes, 93.6% positive [L4570], "
      "**timestamps are whole days (one stamp per day, at 04:00 or 05:00 UTC: 1,647 distinct values; 24,062 ratings share a timestamp with another)** (this module's counts, checked by its tests). "
      "No ordered pair is rated twice [L4571].")
    A("- **wiki-RfA** (SNAP `wiki-RfA.txt.gz`, 14,936,383 bytes). West, Paskov, Leskovec & Potts (2014), TACL 2, doi:10.1162/tacl_a_00184. Votes on Wikipedia adminship "
      "requests: voter, candidate, support/oppose/neutral, election result, date. **Terms:** none stated by SNAP (page read 2026-11-01, `sim/data/README.md`); the vote comments are Wikipedia text "
      "(CC BY-SA and GFDL [L4561]) and "
      "**are skipped line by line and never held in memory**; user names are replaced by integers on load and never written out. 198,275 votes: 144,451 support, 41,176 oppose, "
      "12,648 neutral [L4562].")
    A("- **Newcomb fraternity ranks**, used only in the post hoc re-read of section 4.1 (UCINET `newfrat.dat`, 13,702 bytes, the Internet Archive's copy of Batagelj & Mrvar's Pajek datasets). "
      "**Terms:** none stated, so treated as not licensed for redistribution: local use only, git-ignored, sha256 in `sim/data/README.md`; only computed statistics appear here. "
      "Credit: Newcomb (1961), *The Acquaintance Process*; Nordlie (1958); UCINET (Borgatti, Everett & Freeman 1992), distributed via Batagelj & Mrvar (2006), Pajek datasets.")
    A("- **What is a tie, a closing tie, a converting tie.** A tie is a signed directed rating u -> v. A **closing** tie is the first tie between u and v in either "
      "direction (117's closing convention, [L4572-L4573]) that has at least one *common neighbour* w (a third party tied to both, in any direction) visible before it. "
      "A **converting** tie (wiki-RfA only) is a re-vote: u had already voted on v at an earlier candidacy; the target is the new sign. "
      "Bitcoin has no converting ties [L4571].")
    wi = R["sites"]["wiki-rfa"]["primary"]["ev"].info
    A("- **What 'before' means (no leakage).** A tie is visible as context only if its visibility time is *strictly* earlier than the target's cut. Bitcoin: the "
      "rating time (so, in Alpha, same-day ratings are never context for each other: the order inside a day is unknown). wiki-RfA, primary: the cut is the "
      "*start* of the target's election and a vote becomes visible at the *end* of its election, so a vote sees only the network its voter walked into, never "
      "the concurrent crowd. An election is a block of consecutive records of one candidate, result and year, split wherever the dated votes are more than "
      "14 days apart; stray clusters of fewer than 10 votes and votes without a readable date in an ambiguous block are dropped (" + f"{wi['n_date_dropped']:,}" + " of the 198,275 votes), elections that the file "
      "carries twice with identical windows are merged (" + f"{wi['n_merged']}" + "), the election result (RES) is never used as a feature.")
    sizes = []
    for site in SITE_NAMES:
        ev = R["sites"][site]["primary"]["ev"]
        m = R["sites"][site]["primary"]["mask"]
        res = R["sites"][site]["primary"]["res"]
        sizes.append([SITE_TITLES[site], f"{ev.m:,}", f"{int((ev.emb >= 1).sum()):,}", f"{int(m.sum()):,}", f"{ev.y[m].mean():.3f}", f"{res.n_train:,}", f"{res.n_test:,}",
                      f"{int(np.median(ev.emb[m]))}", f"{int((ev.emb[m] >= 25).sum()):,}"])
    A("")
    L += md_table(["site", "target ties", "with >= 1 common neighbour", "closing ties used", "positive share (used)", "train", "test", "median embeddedness", "embeddedness >= 25"], sizes)
    A("")
    # ---------------------------------------------------------------- 2
    A("## 2. Method")
    A("")
    A("**Rules.** Each rule labels every context triad (a common neighbour w, with the two ties u~w and w~v) as predicting a positive closing tie, a negative one, or "
      "nothing. Balance (strict and weak) is applied the way Leskovec, Huttenlocher & Kleinberg (2010) define it [L4800, L4812, L4815]: on the direction-free pair sign, "
      "one vote per common neighbour. The others use the 16 directed types [F|B][F|B][p|m][p|m] [L4814], one vote per directed instance. "
      "'First-tie asymmetric' is the Newcomb run's rule written as a predictor: balance, except that in a forward chain u -> w -> v (D&K's ordered triple "
      "(i->j)(j->k)(i->k), [L4481]) **a negative first tie u -> w reverses the balance prediction** [L4508, L4511]. Since reversing the product when s1 = - gives s2, "
      "this rule predicts *the sign of the second tie w -> v* in every forward chain; that identity is why a 'copy incoming' diagnostic and a time-first variant are run beside it.")
    A("")
    L += render_rule_table()
    A("")
    A("Weak balance is the strict-balance column with the (-,-) pair-level vote silent. The conjunction column is LHK's learned forward-chain pattern [L4811] extended to all forms by 'positive only if both ties are "
      "positive' (our extension). Further forms are run in section 5.4: balance per directed instance, the A^2 sign (the net product vote of forward chains only, v0.1 (4.2a)), the first-tie rule on forward chains "
      "only, on all forms, and by formation order (copy the later-formed tie).")
    A("")
    A("**Models.** Every model is a logistic regression (ridge 1) fitted on the training period only. A rule enters as two features, log(1 + votes for +) and log(1 + votes for -), "
      "so a rule is judged by how well its *labelling* of the contexts sorts the closing signs; the same rule's **own** hard prediction (majority of its votes, ties and silence to +, "
      "the convention of 106's recount of LHK [L4817]) is reported beside it. *Person propensity* is LHK's four signed degrees [L4813]: u's earlier out-votes (+, -) and v's earlier in-votes (+, -), "
      "all counted from visible ties only (log(1 + count)). *Saturated 16 types* is a logistic model on the 16 triad-type counts alone, the triad half of LHK's 23-feature model [L4799]. The 'person + X' models add X to "
      "the person terms. *Base rate* is the training positive share; *recent rate* has no fitted parameter and is the smoothed positive share of the last "
      f"{RECENT_K} visible ties (an adaptive base rate, added because the Bitcoin test periods have a different share of negatives from their training periods).")
    A("")
    A("**Protocol (fixed in the design before the first run of the primary split; the replication criterion was written down after an exploratory look at the sixteen-cell tables).** Chronological 70/30 split of all target ties by cut time (ties never straddle the cut); parameters from the "
      "training ties; each test tie's features from the ties visible before its own cut (the context grows through the test period, as it would in use; a 'frozen snapshot' variation "
      "removes that); closing ties with at least one common neighbour; accuracy, balanced accuracy, AUC and log-loss on the natural class mix. "
      f"Intervals: cluster bootstrap (B = {B_PRIMARY if not q else 200} in section 3, {B_VAR if not q else 60} in section 5; in section 4.6, {B_CELL} draws for the cell rates and "
      f"{B_COEF if not q else 10} refits for the coefficients), clusters = raters or ratees for Bitcoin and voters or elections for wiki-RfA, the scheme with the larger standard error "
      "(section 4.6 uses ratees or elections). "
      "**Nulls.** (N0) a constant at the training positive share, and the adaptive recent rate; (N1) the person-propensity model: a triad rule must beat it to be more than a person effect; "
      f"(N2) for the question 'do the triad terms add to the person terms', the rows of the added features are permuted among ties of equal embeddedness in the training and in the test set and the "
      f"model is refitted ({N_PERM if not q else 20} permutations; anti-conservative where the refit overfits, section 4.7); (N3) for the static eight-type pattern, the closing signs are shuffled within sender "
      "(the formation-ordered analogue of the Newcomb run's row-wise null [L4485], which redrew every tie of a row: here only the closing sign moves and the context ties stay as they were), within sender and calendar year, and, as a control that "
      "the Newcomb run did not have, within receiver; the pool is the closing ties that have a forward-chain context.")
    A("")
    ro = R["sites"]["bitcoin-otc"]["primary"]["res"]
    A("**Added after the first look at results (post hoc, reported anyway).** (1) The Bitcoin test periods have a different share of negative ratings from their training periods "
      f"(OTC {1 - ro.test_rate:.1%} against {1 - ro.train_rate:.1%}), so the *recent rate* baseline and the rolling-origin evaluation (every block predicted by models fitted on everything earlier) were added; "
      "the single 70/30 split stays the headline, as pre-specified, and where the two designs rank models differently the text says so. (2) The receiver-shuffle null, the sender-by-year null and the person-adjusted "
      "coefficients, after seeing that the static comparison depends on which person effect is held. (3) The Newcomb reception re-read (section 4.1). (4) The merging of the elections the file carries twice, after the data "
      "README flagged them. (5) The shuffle pool of the static comparison was first every closing tie; it was corrected to the closing ties that have a forward-chain context (the first version made every positive-closing "
      "cell look depleted on wiki-RfA and gave a wrong '4/8' there, not reported), and the each-tie-once weighting was added beside the every-triad weighting. (6) The 'where the rules disagree' subset and the A^2 rule "
      "(v0.1 (4.2a)), as sharper tests of the same contrast.")
    A("")
    # ---------------------------------------------------------------- 3
    A("## 3. Primary results")
    A("")
    for site in SITE_NAMES:
        P = R["sites"][site]["primary"]
        A(f"### 3.{SITE_NAMES.index(site) + 1} {SITE_TITLES[site]}: closing ties")
        A("")
        L += render_eval(P["res"], f"{SITE_TITLES[site]}, 70/30 chronological split")
        A("")
        L += render_contrasts(P["res"], CONTRASTS_PRIMARY)
        A("")
        L += render_eval(P["pooled"], f"{SITE_TITLES[site]}, rolling origin (5 expanding blocks over the last half)", rolling=True)
        A("")
        pairs = [("strict balance", "person propensity"), ("first-tie asymmetric", "strict balance"), ("person + 16 types", "person propensity"), ("person + first-tie", "person + strict")]
        L += render_contrasts(P["pooled"], pairs)
        A("")
        A(f"*Where the rules disagree.* The first-tie rule and strict balance say different things only when a closing tie has a forward chain whose first tie is negative ({int(P['mask_dis'].sum()):,} of "
          f"{int(P['mask'].sum()):,} closing ties). On those ties alone (models refitted on the training ties of that kind):")
        A("")
        L += render_eval(P["res_dis"], f"{SITE_TITLES[site]}, closing ties with a negative-first-tie forward chain", models=("base rate", "strict balance", "weak balance", "first-tie asymmetric", "status", "person propensity", "person + strict", "person + first-tie", "person + 16 types"))
        A("")
        L += render_contrasts(P["res_dis"], [("first-tie asymmetric", "strict balance"), ("first-tie asymmetric", "weak balance"), ("first-tie asymmetric", "person propensity"),
                                              ("strict balance", "person propensity"), ("person + first-tie", "person + strict")])
        A("")
    C = R["sites"]["wiki-rfa"]["converting"]
    A("### 3.4 wiki-RfA: converting ties (re-votes)")
    A("")
    A("The target is the new sign of a voter's vote on a candidate the voter had voted on before. Every model includes the voter's previous sign, so the 'base rate' row is **persistence** "
      "(predict the old sign, calibrated). The question is what each rule's context adds to persistence. The 'own' columns are the rule's hard prediction alone and ignore the previous sign, "
      "so they are not comparable with persistence's accuracy; read the log-loss, which has the previous sign in every row.")
    A("")
    L += render_eval(C["res"], "wiki-RfA re-votes, 70/30 chronological split", base_label="persistence (previous sign)")
    A("")
    L += render_contrasts(C["res"], [("strict balance", "base rate"), ("weak balance", "base rate"), ("first-tie asymmetric", "base rate"), ("status", "base rate"),
                                    ("person propensity", "base rate"), ("person + 16 types", "person propensity"), ("first-tie asymmetric", "strict balance")])
    A("")
    L += render_eval(C["pooled"], "wiki-RfA re-votes, rolling origin", rolling=True, base_label="persistence (previous sign)")
    A("")
    # ---------------------------------------------------------------- 4
    A("## 4. Does the first-tie asymmetry replicate outside the fraternity?")
    A("")
    nc_ = R.get("newcomb")
    A("### 4.1 What the Newcomb pattern is (post hoc re-read of the Newcomb run)")
    A("")
    if nc_ is not None:
        ag = nc_["agree_copy_row"]
        A("D&K's eight-type pattern in the Newcomb ranks, from the second wave on, is exactly the partition **'the closing tie has the sign of the second tie'**: "
          "LLL, LDD, DLL, DDD above the row-wise null, LLD, LDL, DLD, DDL below it. Counting the eight directions that match that partition under the row-wise null: "
          + ", ".join(f"w{w + 1} {int(a)}/8" for w, a in enumerate(ag)) + ". Under a **column-wise null** (each man's received signs held and permuted across senders, so popularity is "
          "held and the senders' quotas are free) the same pattern shrinks to "
          f"|z| <= {nc_['max_abs_z_col'].max():.1f} in every cell of every wave (median over waves of the largest |z|: {np.median(nc_['max_abs_z_col']):.1f}); agreement with the partition "
          f"{int(nc_['agree_copy_col'].min())}-{int(nc_['agree_copy_col'].max())}/8, about what chance gives (4/8). "
          f"({nc_['n_draws']:,} draws per null; D&K's own 10,000-draw numbers are in `newcomb_n3.md`.) "
          "The first tie plays no part in this partition: DLL over and DLD under are 'copy the second tie' as much as LLL over and LLD under. "
          "So the pattern the Newcomb run called a first-tie asymmetry is also what a consensus about the third man (differential popularity, D&K's 'recognition of attributes', [L4512]) produces; "
          "the Newcomb data cannot separate the two, and a replication has to.")
    else:
        A("(Newcomb ranks not present locally: re-read skipped.)")
    A("")
    A("### 4.2 Summary of the eight-type comparison on the three sites")
    A("")
    A("Direction of each of D&K's eight types against a shuffled-sign null, on formation-ordered closing ties, compared with three readings: the Newcomb pattern, "
      "'the closing tie has the sign of the second tie' (which the Newcomb pattern equals from the second wave on), and strict balance. 'over' means more than the null. "
      "**Weighting.** 'event' counts each closing tie once, split over its forward-chain cells (the unit is the tie, and embeddedness cannot pose as a link between cell and sign); "
      "'instance' counts every triad, as D&K count ordered triples, so a tie with many common neighbours counts many times and the test also asks whether embeddedness goes with sign. "
      "**Four coupled pairs.** A cell's two closings sum to the cell total, so each z score has a mirror image and 'x/8' counts every cell twice: 4/8 means two of the four cells agree. "
      "The two cells that separate the Newcomb pattern from balance are the two whose first tie is negative (mp: DLL against DLD; mm: DDL against DDD).")
    A("")
    L += render_dk_summary(R)
    A("")
    for site in SITE_NAMES:
        S = R["sites"][site]["static"]
        A(f"### 4.{3 + SITE_NAMES.index(site)} {SITE_TITLES[site]}: the eight D&K types on formation-ordered closing ties")
        A("")
        L += render_dk(S, site)
    A("### 4.6 The four forward-chain cells, and what the first tie adds once the person terms are in")
    A("")
    A("Share of closing ties that are positive, by the signs (first tie u -> w, second tie w -> v), counting every triad ('instance') or every closing tie once ('event': split over its cells), "
      f"cluster-bootstrap 95% interval ({B_CELL:,} draws; clusters are ratees on Bitcoin and elections on wiki-RfA). Strict balance says: pp high, pm low, mp low, mm high. The first-tie rule (= copy the second tie): pp high, pm low, **mp high**, mm low.")
    A("")
    for site in SITE_NAMES:
        S = R["sites"][site]["static"]
        rows = []
        for r in S["ff"]:
            is_cell = r["instances"] != 0 or r["cell"].startswith("FF")
            rows.append([r["cell"], r["weights"], (f"{r['instances']:,.0f}" if r["weights"] == "instance" else f"{r['instances']:,.1f}") if is_cell else "",
                         f"{r['events']:,}" if is_cell else "",
                         (_ci(r["p_pos"], r["lo"], r["hi"]) if is_cell else _sci(r["p_pos"], r["lo"], r["hi"]))])
        A(f"*{SITE_TITLES[site]}*")
        A("")
        L += md_table(["cell or contrast", "weighting", "triads (instance) or closing-tie weight (event)", "closing ties", "P(closing +) or difference [95% CI]"], rows, "llrrr")
        A("")
        c = S["coef"]
        rows = [[k, _sci(*v, 2)] for k, v in c["cells"].items()] + [["FFmp - FFpm (first-tie asymmetry given the person terms)", _sci(*c["mp_minus_pm"], 2)]]
        if "balance_interaction" in c:
            rows.append(["(FFpp + FFmm) - (FFpm + FFmp) (the product structure of balance given the person terms)", _sci(*c["balance_interaction"], 2)])
        A(f"Coefficients of the four forward-chain counts in the model *person + 16 types* fitted on all {c['n']:,} closing ties, training and test together, as a description, not a forecast "
          f"(log-odds per unit of log(1 + count); cluster-bootstrap 95% interval, {c.get('B', 100):,} refits on resampled {'elections' if c.get('scheme', 'v') == 'g' else 'ratees'}):")
        A("")
        L += md_table(["term", "coefficient [95% CI]"], rows)
        A("")
    A("### 4.7 Do the triad terms add anything to the person terms? (permutation null)")
    A("")
    rows = []
    for site in SITE_NAMES:
        for name, r in R["sites"][site]["static"]["added"].items():
            floor = 1.0 / (r["n_perm"] + 1)
            rows.append([SITE_TITLES[site], f"person + {name}", _t(r["ll_base"], 4), _t(r["ll_full"], 4), f"{r['gain']:+.4f}", f"{r['null_mean']:+.4f} (sd {r['null_sd']:.4f}, max {r['null_max']:+.4f})",
                         (f"<= {floor:.3f}" if r["p"] <= floor + 1e-12 else f"{r['p']:.3f}")])
    L += md_table(["site", "added to the person terms", "log-loss person only", "log-loss with the addition", "gain", "gain under the permutation null", "p"], rows, "llrrrrr")
    A("")
    A("The permutation null's mean gain is negative when the added features are noise (the refitted model overfits them); the p value says the observed gain is beyond what shuffled features give, "
      "not that it is large. The size of the gain is the column before.")
    A("")
    A(_n2_caveat(R))
    A("")
    # ---------------------------------------------------------------- 5
    A("## 5. Variations")
    A("")
    A("Every table is the pre-specified protocol with one thing changed; entries are held-out log-loss (lower is better; the best of the four canonical single rules is in bold). "
      "'first-tie - strict' and 'person+16 - person' are paired log-loss differences with cluster-bootstrap intervals "
      f"(B = {B_VAR if not q else 60}); negative means the first named model is better. Intervals on the individual entries are in section 3 and are of the same order as in the primary tables.")
    A("")
    for site in SITE_NAMES:
        V = R["sites"][site]["variations"]
        A(f"### 5.{SITE_NAMES.index(site) + 1} {SITE_TITLES[site]}")
        A("")
        for key, ttl in (("embeddedness", "Embeddedness threshold (closing ties with at least k common neighbours; the model is refitted on the training ties that pass the same threshold)"),
                         ("recodes", "Sign recode" + (" (ratings in between are dropped from the graph, as targets and as context)" if site.startswith("bitcoin") else " (neutral votes)")),
                         ("time", "Time design"), ("ridge", "Ridge penalty")):
            A(f"**{ttl}**")
            A("")
            L += render_variation(V[key])
            A("")
        A("**Target set** (the rules see triads only; 'person+recip' adds the sign of a visible v -> u tie)")
        A("")
        L += render_targets(V["targets"])
        A("")
        if "horizon" in V:
            A("**Context horizon** (wiki-RfA): election start (the network the voter walked into) against every earlier dated vote, including the same election's earlier votes (the herding setting; undated votes are not targets)")
            A("")
            L += render_variation(V["horizon"])
            A("")
    A("### 5.4 Which form of each rule fits best")
    A("")
    A("Alternative forms of the same rules on the primary split (balance counted per pair or per directed instance; the first-tie rule on forward chains only, on forward chains with balance elsewhere "
      "[primary], on all forms, or by formation order; the person terms as counts or as two smoothed rates), sorted by held-out log-loss.")
    A("")
    for site in SITE_NAMES:
        A(f"*{SITE_TITLES[site]}*")
        A("")
        L += render_forms(site, R["sites"][site]["forms"])
        A("")
    A("### 5.5 Which variant wins, in counts")
    A("")
    A("Over the distinct configurations of the variation tables of section 5.1-5.3 (embeddedness, sign recode, time design, ridge, wiki-RfA horizon; the target-set rows have a different model list and are left out), "
      "how often each canonical single rule has the lowest held-out log-loss, which model is best overall, and how often the paired 95% interval puts one model below the other ('better' = the first named model has the lower log-loss with the interval wholly below zero). "
      "The pre-specified configuration is the reference row of the recode, split, ridge and (wiki-RfA) horizon tables as well as 'k >= 1'; it is counted once, so a site has "
      + ", ".join(f"{len(variation_rows(R, s))} ({SITE_TITLES[s]})" for s in SITE_NAMES) + " distinct configurations.")
    A("")
    L += render_winners(R)
    A("")
    # ---------------------------------------------------------------- 6
    A("## 6. Reproduction of file 117's undirected closure counts")
    A("")
    a, b = R["closure117"]["otc"], R["closure117"]["alpha"]
    A(f"The formation-order counts of 117 section 3.4 [L4572-L4577] are reproduced from the same files by an independent code path (first rating per unordered pair, triangles of mutually rated pairs, "
      f"edges ordered by time). OTC: {a['pairs']:,} pairs, {a['triangles']:,} triangles, starts (+,+) {a['starts']['pp'][0]:,} / (+,-) {a['starts']['pm'][0]:,} / (-,-) {a['starts']['mm'][0]:,}, closing positive "
      f"{a['starts']['pp'][1]:,} / {a['starts']['pm'][1]:,} / {a['starts']['mm'][1]:,}, product rule {a['product_ok']:,} ({a['product_ok'] / a['triangles']:.1%}); all identical to 117. "
      f"Alpha: {b['pairs']:,} pairs, {b['triangles']:,} triangles, {b['strict_triangles']:,} with three distinct times of which {b['strict_product_ok']:,} follow the product rule "
      f"({b['strict_product_ok'] / b['strict_triangles']:.1%}), identical to 117; the three start classes ({b['starts']['pp'][0]:,}, {b['starts']['pm'][0]:,}, {b['starts']['mm'][0]:,}) differ from 117's "
      "(19,814, 1,855, 484) by one or two triangles because ties between equal timestamps are broken arbitrarily (by file order here), as 117 says of its own run.")
    A("")
    A("## 7. Caveats")
    A("")
    for c in caveats(R):
        A(f"- {c}")
    A("")
    A("## Reproduce")
    A("")
    A("    cd sim")
    A("    ~/.local/bin/uv run python -m models.triad_rule_comparison report      # a few minutes on a quiet machine, seeded")
    A("    ~/.local/bin/uv run pytest tests/test_triad_rule_comparison.py")
    A("")
    A("`report --save-pickle PATH` keeps the computed numbers and `report --from-pickle PATH` re-renders the prose from them without recomputing (the numbers are seeded and identical on a rerun). "
      "A `## Review` section appended below is kept when the file is re-rendered.")
    A("")
    return "\n".join(L) + "\n"


def caveats(R: dict) -> list[str]:
    def share(site: str) -> tuple[int, int]:
        P = R["sites"][site]["primary"]
        return int(P["mask"].sum()), P["ev"].m

    (a, na), (b, nb), (c, nc_) = share("bitcoin-otc"), share("bitcoin-alpha"), share("wiki-rfa")
    return [
        "Three data sets, two kinds of medium (trading-forum ratings and public votes), 2003-2016: this is a test of whether a rule found on one fraternity's 1956 rankings transfers to online rating and voting sites, "
        "not a test of the rules in a group of about 17 people.",
        "The signs are ratings (Bitcoin, after a trade) and public votes (wiki-RfA, strategic and consequential), not liking. A negative Bitcoin rating is often a fraud report. "
        "Nothing here bridges these to Newcomb's rank recode (v0.2 section 0.6, rule 7).",
        "Alpha's timestamps are whole days, so 'earlier' means an earlier day; within-day order, and every same-day context, is lost. OTC's are unique and sub-second.",
        f"Only embedded closing ties are scored: {a / na:.0%} of OTC's ratings, {b / nb:.0%} of Alpha's and {c / nc_:.0%} of wiki-RfA's non-neutral votes. The results are about ties that close a triad.",
        "Person propensity is estimated from the same site's earlier ties; for a wiki-RfA candidate on a first candidacy there is no earlier in-vote, so the receiver half of the baseline is empty there "
        "(election-start horizon). The vote-level horizon variation shows what the same election's earlier votes add.",
        _mc_caveat(R),
        f"wiki-RfA elections are reconstructed from the file's block order and its dates ({R['sites']['wiki-rfa']['primary']['ev'].info['n_elections']:,} elections against 117's 3,926 "
        f"(candidate, year, result) groups); {R['sites']['wiki-rfa']['primary']['ev'].info['n_date_dropped']:,} votes are dropped for ambiguous or stray dates.",
        "The rolling-origin pooled AUC is not shown: it would mix predictions calibrated on different training periods.",
        "Rankings of variants (sections 5.4 and 5.5) are read off the same held-out period that scores them, so the best of many variants is optimistic by selection; differences smaller than the paired intervals are ties, "
        "not rankings, and no variant was chosen to produce a number elsewhere in this file.",
        "The person baseline is LHK's four signed degrees as log counts, a linear model; a stronger person model (latent sender and receiver effects, REV2-style) could absorb more of what the triad terms add. "
        "Its counts also grow through the test period (the context is online), which the frozen-snapshot variation removes.",
        "A null that fixes the sender's and the receiver's sign mix at once (a two-margin swap shuffle on the sender-by-receiver grid) was not implemented; the sender and receiver nulls each hold one margin "
        "and the person-adjusted coefficient approximates both.",
        "The static D&K comparison is shown with each closing tie counted once and with every triad counted; triads that share a closing tie are not independent, and the shuffles permute whole closing ties, "
        "so the z scores are relative to that structure and are large because there are thousands of ties, not because the effects are large.",
    ]


def keep_reviews(new_text: str, old_text: str) -> str:
    """Reviews appended by hand to the results file ('## Review (date)' to the end) are history, not output: a re-render
    keeps them after the freshly generated text instead of deleting them."""
    k = old_text.find("\n## Review (")
    return new_text if k < 0 else new_text.rstrip("\n") + "\n" + old_text[k:]


def main(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0] if __doc__ else "")
    ap.add_argument("cmd", choices=["report"], help="report: run everything and write sim/results/triad_rule_comparison.md")
    ap.add_argument("--quick", action="store_true", help="shrink Monte-Carlo sizes (smoke test; the output is marked)")
    ap.add_argument("--out", default=str(RESULTS_FILE))
    ap.add_argument("--save-pickle", default=None, help="also pickle the computed results here (to re-render prose without recomputing)")
    ap.add_argument("--from-pickle", default=None, help="skip the computation and render from a pickle written by --save-pickle")
    args = ap.parse_args(argv)
    import pickle

    if args.from_pickle:
        with open(args.from_pickle, "rb") as f:
            R = pickle.load(f)
    else:
        R = run_all(quick=args.quick)
        if args.save_pickle:
            with open(args.save_pickle, "wb") as f:
                pickle.dump(R, f)
    text = render_report(R)
    out = Path(args.out)
    if out.exists():
        text = keep_reviews(text, out.read_text(encoding="utf-8"))
    out.write_text(text, encoding="utf-8")
    print(f"wrote {args.out} ({len(text):,} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
