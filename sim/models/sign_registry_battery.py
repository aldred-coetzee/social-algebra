"""The sign-law registry's five tests (112 section 6.5), run on wiki-RfA, Bitcoin OTC, Bitcoin Alpha and BlueTempNet.

Prior work: docs/prior-work/112-sign-generators-cross-check-and-candidate-sign-law.md section 6.2 (the R-E
module: z_ij = a_i + b_j + sum_tau c_tau n_tau(i,j), forward-chain pattern pp +, pm -, mp -, mm -; ledger L5421,
L4811, L4833) and section 6.5 (the five tests that could refute it; hand-off to D614); docs/prior-work/106
(Leskovec, Huttenlocher & Kleinberg 2010, "LHK": the 16 directed triad types, the degree features, the balanced
accuracies; L4799-L4801, L4814-L4816, L4826-L4833, L4850-L4852); docs/prior-work/117 (the data: wiki-RfA
L4561-L4564, Bitcoin OTC and Alpha L4567-L4580, BlueTempNet L4593-L4598, L4663).  Question the battery answers
(next-pattern's, for the first-outcome decision of models/00-v0.md section 0.5): DO SIGNS HAVE A MECHANISM INSIDE
THE REGISTRY BEYOND PERSON PROPENSITIES?

THE FIVE TESTS (112 section 6.5, as run here).
 T1 Form transfer.  Fit the 16 directed triad types per site; check the forward-chain pattern (FFpp +, FFpm -,
    FFmp -, FFmm -) and FFmm < 0; "refuted if mm > 0 with adequate support".  Two designs: STATIC (LHK's: all other
    edges of the snapshot are the evidence) and CAUSAL (only edges with a strictly earlier time are the evidence),
    each with and without the person features.
 T2 Person terms against triad terms.  Held-out sign accuracy (AUC, balanced accuracy, log-loss) from the sender and
    receiver propensities alone, the triad terms alone, and both; forward-chained time-split, features computed
    only from strictly earlier edges (no leakage).  "Prediction: person terms carry more; refuted if the triad
    terms add more than the person terms."
 T3 Drift by year.  Refit per year (a separate snapshot per year); "the sign pattern is stable while intercepts move;
    refuted if the sign pattern flips with year."
 T4 Symmetry.  The share of reciprocated pairs with opposite signs ("rare" in LHK's 2003-09 data [L4812]; "if it is
    not rare in a modern medium, R-A must not be used there without a symmetrisation rule").
 T5 Visibility.  Whether the target's received majority outperforms the voter's own history at low embeddedness
    (LHK's Wikipedia 0.706 against 0.576 [L4852]); whether the gap moves with the date.  As L4852 says, the data cannot
    split a received-majority advantage into candidate quality, shared information and visibility of earlier votes; a
    before/after comparison of vote windows and a position gradient were both tried in design and dropped, because in a
    stationary process the two directions of time are statistically indistinguishable and a gradient has other causes
    (early voters are nominators).  T5 therefore reports the gap, by embeddedness and by date, and does not claim to
    identify visibility.

DECISION RULES, FIXED BEFORE ANY RESULT WAS COMPUTED (so the verdict cannot be shopped; they are the constants named
RULE_* below and are asserted in the tests).
 R1 (T1).  Forward-chain type tau has predicted sign sigma = (+, -, -, -).  With the cluster-robust z = beta / SE:
    SUPPORTED if sigma z > 1.96, CONTRADICTED if sigma z < -1.96, else UNDECIDED.  ADEQUATE SUPPORT for a type means
    at least RULE_MIN_SUPPORT = 100 edges carry at least one triad of it; below that the type is UNDECIDED whatever z
    is.  The form transfers at a site if FFmm is SUPPORTED and no forward-chain type is CONTRADICTED; the registry is
    REFUTED at a site if FFmm is CONTRADICTED with adequate support.
 R2 (T2).  Primary metric: pooled held-out AUC over four forward-chained test blocks, 95% interval from a cluster
    bootstrap (clusters = elections for wiki-RfA, receivers elsewhere) that resamples the same clusters for every
    model.  D = AUC(person) - AUC(triad); G = AUC(person + triad) - AUC(person).  "Person terms carry more" if the
    interval of D lies above 0.  Triad terms add a MECHANISM beyond person propensities at a site if G >= RULE_G_MATERIAL
    = 0.02 AUC (the lower end of LHK's quoted 2-6 point gain over the degree features [L4829]) with the interval of G
    above 0; "small" if the interval is above 0 but G < 0.02; "none" otherwise.  Across sites: YES if material at
    three or more of the four, NO if at most one, else MIXED.  The same is reported inside the high-embeddedness
    stratum (C >= 5), where triad evidence exists.
 R3 (T3).  Per year-bin static fits.  A forward-chain type is FLIPPED in a bin if it is CONTRADICTED there with adequate
    support.  The registry is REFUTED at a site by drift if some type is FLIPPED in at least RULE_FLIP_BINS = 2 bins.
    "Intercepts move" if Cochran's Q over the per-bin intercepts has p < 0.001 and their range is at least 0.5 logit.
 R4 (T4).  "Rare" if the opposite-sign share of reciprocated pairs is at most RULE_RARE = 0.10.  Reported against two
    nulls: independent signs at the observed marginals, and the person-propensity model.
 R5 (T5).  Visibility SUPPORTED at a site if the lower bound of the 95% interval of BA(InSign) - BA(OutSign) at
    embeddedness 0 exceeds RULE_GAP = 0.02; ABSENT if the upper bound is below 0.02; else UNDECIDED.

AMENDMENTS MADE AFTER A FIRST LOOK AT THE DATA (2026-11-01; none changes a threshold above, all are reported, nothing was
dropped).
 (a) R1 and R3 did not say whether the person terms are in the fit.  R-E as the registry writes it has them (a_i + b_j +
     sum c_tau n_tau); LHK's coefficient table has the 16 types alone.  A first look at T1 showed the two diverge, so both are
     reported and every verdict says which fit it is for.
 (b) The standard errors of R1/R3 and the intervals of R2/R5 resample receivers (elections) only, as written, but senders are
     strongly clustered too (ICC of the sign across senders up to 0.7), so a two-way version (Cameron-Gelbach-Miller
     sandwich; pigeonhole bootstrap resampling senders and receivers independently) is computed beside each and both are
     shown.
 (c) R2's G is not zero under a person-only world (triad counts carry extra information about users' propensities), so G
     and the coefficients are also compared with replicates of a person-only generative null whose ridge is tuned to match
     the real person-only AUC, and with planted mechanisms of known size.  An earlier, heavily shrunken generator gave a
     world with far less person signal than the data and was replaced.
 (d) A before/after window comparison and a position gradient, designed to split visibility from candidate quality, were
     dropped as non-identifying (the first was run once on wiki-RfA during development; see the results file).
 (e) Review 2026-11-01 (no threshold changed): the verdict calls a site ABSENT under R5 only when the receiver-cluster and the
     two-way intervals agree, as it already did for SUPPORTED (r5_both); its wording was brought into line with the numbers
     (see the review section of the results file).

DATA (local use only, never committed; sim/data/README.md has source, terms and checksum of each).  wiki-RfA
(SNAP wiki-RfA.txt.gz; West, Paskov, Leskovec & Potts 2014), Bitcoin OTC and Alpha (SNAP; Kumar, Spezzano,
Subrahmanian & Faloutsos 2016; Kumar et al. 2018), BlueTempNet (Jeong, Jiang, Tan, Bernard & Liu 2024; the authors'
public GitHub repository serves the files through Git LFS [L4594]).  The wiki-RfA comments are Wikipedia text
(CC BY-SA): lines starting "TXT:" are skipped before decoding and no text is kept; user names are replaced by integers
on load and never written out.

CONVENTIONS.
 * Edge: ordered pair (u, v) with sign s in {+1, -1}, time t (seconds).  wiki-RfA: voter u -> candidate v; neutral
   votes (VOT 0), empty-voter records, self-votes and undated votes are dropped; the first dated vote of an ordered
   pair is the edge (repeat candidacies are the other agent's conversion test).  Bitcoin: rater u -> ratee v, sign =
   sign of the rating (no zeros).  BlueTempNet: the feed-creator graph (graph_dimension1), follow = +, block = -, one
   record per ordered pair as released (where a pair had both, the release keeps the block [L4595]); the larger
   feed-member graph (1.15 GB) is not used.
 * Time order and leakage.  Edges are sorted by time.  A CAUSAL feature of an edge uses only edges with a strictly
   earlier time (edges sharing a timestamp are simultaneous and invisible to one another; Bitcoin Alpha's times are
   coarse, 22,539 of 24,186 repeat an earlier value, so it loses same-day evidence by this rule).  A STATIC feature
   uses every other edge, as LHK did.
 * Triad types [F|B][F|B][p|m][p|m] [L4814]: for an edge u -> v and a common neighbour w, first letter F if the
   u-w edge points u -> w (B if w -> u), second letter F if the w-v edge points w -> v (B if v -> w), then the signs
   of the u-w and w-v edges.  A neighbour joined by edges in both directions contributes one triad per combination.
   Embeddedness C(u,v) is the number of common neighbours, direction ignored [L4825].
 * Person terms: the sender's earlier outgoing signs and the receiver's earlier incoming signs (their counts, and
   shrunken log-odds of them).  This is the empirical a_i and b_j of the registry; a second reading (a_i, b_j as
   ridge-fitted effects frozen at the end of the training window) is a variation.
 * Balance features [L4800, L4815]: strict = sum over triads of s(u,w) s(w,v) (direction ignored); weak = the same
   with the mm triads set to 0.  Status feature [L4801]: after orienting the path u -> w -> v (an edge's sign flips
   when its direction is reversed) the feature of a triad is sign(s1 + s2), which is 0 for half of the 16 types; the
   node status score is sigma(x) = d+_in + d-_out - d-_in - d+_out [L4802].

THE NULL.  T1/T3: coefficients are tested against 0 with cluster-robust standard errors (receiver clusters and two-way) and
are also compared with what a PERSON-ONLY WORLD gives: the real network skeleton (who rates whom, when) with the signs redrawn
from a period intercept plus one ridge-fitted effect per sender and receiver, the ridge tuned so that the online person model
reaches the real held-out AUC (calibrate_generator), 20 replicates run through the whole pipeline (null_battery_parallel).
T2: the same world gives the distribution of G = AUC(person + triad) - AUC(person) when nothing but person propensities
generated the signs (it is not 0: triad counts carry extra information about the users), and worlds with a PLANTED
forward-chain mechanism of 0.1 or 0.3 log-odds per triad (signs drawn in time order from the counts of the signs already
drawn) show what a mechanism of known size looks like: the coefficients recovered and the G produced, so that a zero result
is known to be one the test could have avoided.  T4: independent signs at the observed marginals, and the person model's
expected opposite share.  T5: no null beyond the bootstrap; the gap is judged against RULE_GAP.
"""
from __future__ import annotations

import gzip
import hashlib
import math
import re
import sys
import time
import zipfile
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
from scipy import optimize, sparse, special, stats

# --------------------------------------------------------------------------------------------------- constants

HERE = Path(__file__).resolve()
SIM = HERE.parents[1]
DATA = SIM / "data"

RULE_MIN_SUPPORT = 100       # R1: edges carrying >= 1 triad of a type before its z may count
RULE_G_MATERIAL = 0.02       # R2: AUC gain of triad terms over person terms that counts as a mechanism
RULE_FLIP_BINS = 2           # R3: year-bins in which a type must be CONTRADICTED to call the pattern flipped
RULE_INTERCEPT_RANGE = 0.5   # R3: logit range of year intercepts that counts as "moving" (with Q p < 0.001)
RULE_RARE = 0.10             # R4: opposite-sign share of reciprocated pairs that still counts as rare
RULE_GAP = 0.02              # R5: balanced-accuracy gap (InSign - OutSign) that counts as visibility
Z95 = 1.959963984540054

# forward-chain order and predicted signs (112 section 6.2: pp +, pm -, mp -, mm -)
FORWARD = ("FFpp", "FFpm", "FFmp", "FFmm")
FORWARD_SIGN = {"FFpp": +1, "FFpm": -1, "FFmp": -1, "FFmm": -1}

# the 16 types in the order [FF FB BF BB] x [pp pm mp mm]; index = 4 * direction_class + 2 * [s1<0] + [s2<0]
TYPES = tuple(d + s for d in ("FF", "FB", "BF", "BB") for s in ("pp", "pm", "mp", "mm"))
TYPE_INDEX = {name: i for i, name in enumerate(TYPES)}


def _type_sign_pair(name: str) -> tuple[int, int]:
    return (+1 if name[2] == "p" else -1, +1 if name[3] == "p" else -1)


def _type_dirs(name: str) -> tuple[bool, bool]:
    return (name[0] == "B", name[1] == "B")   # (u-w edge reversed?, w-v edge reversed?)


# balance (strict, weak) and status predictions of each type, from the definitions in the header
BAL_STRICT = np.array([_type_sign_pair(n)[0] * _type_sign_pair(n)[1] for n in TYPES], dtype=float)
BAL_WEAK = np.array([0.0 if n.endswith("mm") else BAL_STRICT[i] for i, n in enumerate(TYPES)], dtype=float)


def _status_value(name: str) -> int:
    s1, s2 = _type_sign_pair(name)
    r1, r2 = _type_dirs(name)
    a = -s1 if r1 else s1          # oriented along u -> w
    b = -s2 if r2 else s2          # oriented along w -> v
    return int(np.sign(a + b))


STATUS = np.array([_status_value(n) for n in TYPES], dtype=float)


# --------------------------------------------------------------------------------------------------- sources

@dataclass(frozen=True)
class Source:
    key: str
    rel: str                      # path under sim/data/
    url: str
    nbytes: int
    sha256: str
    cite: str
    terms: str

    @property
    def path(self) -> Path:
        return DATA / self.rel


SOURCES = {
    "wiki": Source(
        "wiki", "wiki-rfa/wiki-RfA.txt.gz", "https://snap.stanford.edu/data/wiki-RfA.txt.gz", 14_936_383,
        "88d53196fb2564a2e20286dbba818832f718cc352bb181a2101d23d2556f0862",
        "West, Paskov, Leskovec & Potts 2014, TACL 2: 297-310, doi:10.1162/tacl_a_00184",
        "SNAP states none; comments are Wikipedia text (CC BY-SA), never kept; local use only"),
    "otc": Source(
        "otc", "bitcoin/soc-sign-bitcoinotc.csv.gz", "https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz",
        397_258, "6424ac981dad3a019f697fc1b9fcd85c19d8d9f039797758e9ffb6fea100c373",
        "Kumar, Spezzano, Subrahmanian & Faloutsos 2016, ICDM, doi:10.1109/ICDM.2016.0033; Kumar et al. 2018, WSDM, "
        "doi:10.1145/3159652.3159729", "SNAP states none; local use only"),
    "alpha": Source(
        "alpha", "bitcoin/soc-sign-bitcoinalpha.csv.gz", "https://snap.stanford.edu/data/soc-sign-bitcoinalpha.csv.gz",
        149_480, "3a178611b9c2f39c9a0dc75936f28557317f1733319b49da4838232b3757cd76",
        "Kumar, Spezzano, Subrahmanian & Faloutsos 2016, ICDM, doi:10.1109/ICDM.2016.0033; Kumar et al. 2018, WSDM, "
        "doi:10.1145/3159652.3159729", "SNAP states none; local use only"),
    "bsky": Source(
        "bsky", "bluesky/networks_to_share.zip",
        "https://media.githubusercontent.com/media/ujeong1/BlueTempNet-IEEE-DATA-2024/main/data/networks_to_share.zip",
        221_305_868, "360839bfc6f7e4e8642ec207917c1401f2f665aa63478d3c3ff5fee5b6a9cf23",
        "Jeong, Jiang, Tan, Bernard & Liu 2024, IEEE Data Descriptions 1: 71-79, doi:10.1109/IEEEDATA.2024.3474640",
        "DataCite lists CC BY 4.0 for the DataPort record (doi:10.21227/yrsy-ee91); the GitHub copy has no licence file; "
        "the authors ask for citation; local use only"),
}
SITE_ORDER = ("wiki", "otc", "alpha", "bsky")
SITE_LABEL = {"wiki": "wiki-RfA", "otc": "Bitcoin OTC", "alpha": "Bitcoin Alpha", "bsky": "BlueTempNet"}


def sha256_of(path: Path, chunk: int = 1 << 20) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


def available(key: str) -> bool:
    return SOURCES[key].path.exists()


def fetch(key: str, timeout: float = 600.0) -> Path:
    """Download one source with the standard library, refusing a file whose sha256 differs from the recorded one.
    Sends no identity beyond urllib's default agent.  Does nothing if the file is already present."""
    import urllib.request
    src = SOURCES[key]
    if src.path.exists():
        return src.path
    src.path.parent.mkdir(parents=True, exist_ok=True)
    tmp = src.path.with_suffix(src.path.suffix + ".part")
    with urllib.request.urlopen(src.url, timeout=timeout) as r, open(tmp, "wb") as f:
        while True:
            b = r.read(1 << 20)
            if not b:
                break
            f.write(b)
    if sha256_of(tmp) != src.sha256:
        tmp.unlink()
        raise RuntimeError(f"{src.url}: sha256 differs from the recorded {src.sha256}; file refused")
    tmp.rename(src.path)
    return src.path


# --------------------------------------------------------------------------------------------------- edge sets

@dataclass
class EdgeSet:
    """Signed directed ties sorted by time (stable).  u, v are dense node ids 0..n_nodes-1."""
    name: str
    u: np.ndarray
    v: np.ndarray
    s: np.ndarray            # int8, +1 / -1
    t: np.ndarray            # float64 seconds since the epoch
    cluster: np.ndarray      # int32; election id (wiki-RfA) or receiver id
    n_nodes: int
    info: dict = field(default_factory=dict)

    @property
    def m(self) -> int:
        return len(self.u)

    @property
    def y(self) -> np.ndarray:
        return (self.s > 0).astype(np.float64)

    @property
    def year(self) -> np.ndarray:
        return years_of(self.t)

    def take(self, idx) -> "EdgeSet":
        idx = np.asarray(idx)
        return EdgeSet(self.name, self.u[idx], self.v[idx], self.s[idx], self.t[idx], self.cluster[idx],
                       self.n_nodes, dict(self.info))


def years_of(t: np.ndarray) -> np.ndarray:
    return (np.asarray(t, dtype="float64").astype("int64").astype("datetime64[s]").astype("datetime64[Y]")
            .astype("int64") + 1970).astype(np.int16)


def _sorted_edgeset(name, u, v, s, t, cluster, n_nodes, info) -> EdgeSet:
    order = np.argsort(t, kind="stable")
    return EdgeSet(name, u[order].astype(np.int32), v[order].astype(np.int32), s[order].astype(np.int8),
                   t[order].astype(np.float64), cluster[order].astype(np.int32), int(n_nodes), info)


def _compress(*arrays):
    """Dense ids over the union of the arrays' values."""
    allv = np.concatenate(arrays)
    uniq, inv = np.unique(allv, return_inverse=True)
    out, pos = [], 0
    for a in arrays:
        out.append(inv[pos:pos + len(a)].astype(np.int32))
        pos += len(a)
    return out, len(uniq)


_MONTH = {m: i + 1 for i, m in enumerate(("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov",
                                          "dec"))}
_TYPO = {"mya": "may"}        # the file's one transposed month (the others, 'Julu' and 'Janry', read from their first three letters)
_DAT = re.compile(r"^(\d{1,2}):(\d{2}), (\d{1,2}) ([A-Za-z]+) (\d{4})$")


def parse_dat(s: str) -> float:
    """wiki-RfA 'HH:MM, D Month YYYY' -> seconds since the epoch (UTC), NaN if absent or impossible.  The file uses full
    and three-letter month names and has a few typos ('Julu', 'Mya', 'Janry'), so the month is read from its first
    three letters ('Mya' is mapped by hand); one record has hour 31 and is treated as undated."""
    m = _DAT.match(s.strip())
    if not m:
        return float("nan")
    hh, mm, dd, mon, yy = m.groups()
    mon = _MONTH.get(_TYPO.get(mon.lower(), mon[:3].lower()))
    if mon is None:
        return float("nan")
    try:
        d = np.datetime64(f"{int(yy):04d}-{mon:02d}-{int(dd):02d}T{int(hh):02d}:{int(mm):02d}", "s")
    except ValueError:
        return float("nan")
    return float(d.astype("int64"))


def parse_wikirfa_lines(lines) -> dict:
    """Records of the SNAP wiki-RfA text format as arrays.  `lines` is an iterable of bytes lines.  Lines starting
    'TXT:' (the voter's comment, Wikipedia text) are skipped before they are decoded."""
    names: dict[str, int] = {}
    src, tgt, vot, res, yea, tim = [], [], [], [], [], []
    cur: dict[str, str] = {}

    def flush():
        if "TGT" in cur and "VOT" in cur:
            sname = cur.get("SRC", "").strip()
            src.append(names.setdefault(sname, len(names)) if sname else -1)
            tgt.append(names.setdefault(cur["TGT"].strip(), len(names)))
            vot.append(int(cur["VOT"]))
            res.append(int(cur.get("RES", "0") or 0))
            yea.append(int(cur.get("YEA", "0") or 0))
            tim.append(parse_dat(cur.get("DAT", "")))
        cur.clear()

    for raw in lines:
        if raw.startswith(b"TXT:"):
            continue
        line = raw.decode("utf-8", "replace").rstrip("\r\n")
        if not line.strip():
            flush()
            continue
        k, _, val = line.partition(":")
        if k in ("SRC", "TGT", "VOT", "RES", "YEA", "DAT"):
            cur[k] = val
    flush()
    return dict(src=np.array(src, np.int64), tgt=np.array(tgt, np.int64), vot=np.array(vot, np.int8),
                res=np.array(res, np.int8), yea=np.array(yea, np.int16), t=np.array(tim, np.float64),
                n_names=len(names))


def assign_elections(tgt, res, t, gap_days: float = 14.0) -> np.ndarray:
    """Election id of each dated vote: votes of one (candidate, result) are split wherever consecutive dated votes are
    more than `gap_days` apart (an RfA runs about a week; a candidate can fail twice in a year)."""
    n = len(tgt)
    order = np.lexsort((t, res, tgt))
    ids = np.empty(n, np.int64)
    cur = -1
    prev_key = None
    prev_t = None
    for k in order:
        key = (tgt[k], res[k])
        if key != prev_key or t[k] - prev_t > gap_days * 86400.0:
            cur += 1
        ids[k] = cur
        prev_key, prev_t = key, t[k]
    return ids


def load_wikirfa(path: Path | str | None = None) -> EdgeSet:
    path = Path(path) if path else SOURCES["wiki"].path
    with gzip.open(path, "rb") as f:
        d = parse_wikirfa_lines(f)
    n_all = len(d["src"])
    keep = (d["src"] >= 0) & (d["vot"] != 0) & (d["src"] != d["tgt"])
    n_named = int(keep.sum())
    keep &= ~np.isnan(d["t"])
    sel = np.flatnonzero(keep)
    src, tgt, vot, res, t = d["src"][sel], d["tgt"][sel], d["vot"][sel], d["res"][sel], d["t"][sel]
    elec = assign_elections(tgt, res, t)
    # first dated vote of each ordered pair
    order = np.argsort(t, kind="stable")
    key = src[order] * (d["n_names"] + 1) + tgt[order]
    _, first = np.unique(key, return_index=True)
    first = np.sort(order[first])
    (ui, vi), n_nodes = _compress(src[first], tgt[first])
    info = dict(n_records=n_all, n_named_nonneutral=n_named, n_dated=int(keep.sum()), n_pairs=len(first),
                n_elections=int(len(np.unique(elec[first]))), n_nodes_raw=d["n_names"])
    return _sorted_edgeset("wiki-RfA", ui, vi, vot[first], t[first], elec[first], n_nodes, info)


def load_bitcoin(key: str, path: Path | str | None = None) -> EdgeSet:
    assert key in ("otc", "alpha")
    path = Path(path) if path else SOURCES[key].path
    with gzip.open(path, "rt") as f:
        raw = np.loadtxt(f, delimiter=",")
    src, tgt, rating, t = raw[:, 0].astype(np.int64), raw[:, 1].astype(np.int64), raw[:, 2], raw[:, 3]
    keep = (src != tgt) & (rating != 0)
    (ui, vi), n_nodes = _compress(src[keep], tgt[keep])
    s = np.where(rating[keep] > 0, 1, -1)
    info = dict(n_rows=len(raw), n_kept=int(keep.sum()))
    return _sorted_edgeset("Bitcoin " + key.upper(), ui, vi, s, t[keep], vi.copy(), n_nodes, info)


def parse_gexf_edges(fileobj):
    """Stream the edges of a NetworkX-written GEXF file: yields (source, target, sign, time-string).  The parser is the
    standard library's expat, which has no external entities; the file is read incrementally."""
    import xml.etree.ElementTree as ET
    for _, el in ET.iterparse(fileobj, events=("end",)):
        if el.tag.rsplit("}", 1)[-1] != "edge":
            continue
        sign = tstr = None
        for av in el.iter():
            if av.tag.rsplit("}", 1)[-1] == "attvalue":
                if av.get("for") == "0":
                    sign = int(av.get("value"))
                elif av.get("for") == "1":
                    tstr = av.get("value")
        yield int(el.get("source")), int(el.get("target")), sign, tstr
        el.clear()


def _iso_seconds(x: str) -> float:
    """'2023-09-11T02:37:47.141Z' -> seconds since the epoch."""
    sec = np.datetime64(x[:19], "s").astype("int64")
    frac = float("0." + x[20:23]) if len(x) > 20 and x[19] == "." else 0.0
    return float(sec) + frac


def load_bluesky(path: Path | str | None = None, member: str = "graph_dimension1_to_share.gexf") -> EdgeSet:
    path = Path(path) if path else SOURCES["bsky"].path
    src, tgt, sg, tm = [], [], [], []
    with zipfile.ZipFile(path) as z, z.open(member) as f:
        for a, b, s, ts in parse_gexf_edges(f):
            src.append(a), tgt.append(b), sg.append(s), tm.append(_iso_seconds(ts))
    src, tgt, sg, tm = np.array(src), np.array(tgt), np.array(sg), np.array(tm)
    keep = (src != tgt) & ((sg == 1) | (sg == -1))
    (ui, vi), n_nodes = _compress(src[keep], tgt[keep])
    info = dict(n_rows=len(src), n_kept=int(keep.sum()), member=member)
    return _sorted_edgeset("BlueTempNet creators", ui, vi, sg[keep], tm[keep], vi.copy(), n_nodes, info)


def load_site(key: str) -> EdgeSet:
    if key == "wiki":
        return load_wikirfa()
    if key in ("otc", "alpha"):
        return load_bitcoin(key)
    if key == "bsky":
        return load_bluesky()
    raise KeyError(key)


# --------------------------------------------------------------------------------------------------- triad engine

@dataclass
class Features:
    """Per-edge evidence, computed under one rule (causal or static); every array has one row per edge of the set."""
    mode: str
    tri: np.ndarray          # (m, 16) int32 triad counts, TYPES order
    emb: np.ndarray          # (m,) int32 common neighbours (direction ignored)
    op: np.ndarray           # sender's positive out-ties
    on: np.ndarray           # sender's negative out-ties
    ip: np.ndarray           # receiver's positive in-ties
    inn: np.ndarray          # receiver's negative in-ties
    uip: np.ndarray          # sender's positive in-ties
    uin: np.ndarray          # sender's negative in-ties
    vop: np.ndarray          # receiver's positive out-ties
    von: np.ndarray          # receiver's negative out-ties
    rev: np.ndarray          # int8: sign of the reverse tie v -> u if it is in the evidence, else 0
    grate: np.ndarray        # global positive share in the evidence (Laplace-smoothed)
    queried: np.ndarray      # bool: rows that were computed (all, unless a sample was asked for)


def compute_features(E: EdgeSet, mode: str = "causal", query: np.ndarray | None = None) -> Features:
    """Triad counts, embeddedness, signed degrees and the reverse tie of every edge, from the evidence its mode allows.

    mode 'causal': the evidence of edge k is the edges with a strictly earlier time (edges are inserted after all
    edges sharing a timestamp have been queried).  mode 'static': the evidence is every other edge of the set (the
    edge's own sign is removed from the degree counts; a triad never contains the edge itself).
    `query` is an optional boolean mask of the rows to compute (the others stay zero), the graph being built from all
    edges either way; used to bound the cost on the larger sets."""
    if mode not in ("causal", "static"):
        raise ValueError(mode)
    m, n = E.m, E.n_nodes
    U, V, S, T = E.u.tolist(), E.v.tolist(), E.s.tolist(), E.t
    want = np.ones(m, bool) if query is None else np.asarray(query, bool)
    out = [dict() for _ in range(n)]       # out[u][w] = sign of u -> w
    inn = [dict() for _ in range(n)]       # inn[v][w] = sign of w -> v
    nb = [set() for _ in range(n)]
    cop = [0] * n
    con = [0] * n
    cip = [0] * n
    cin = [0] * n
    tri = np.zeros((m, 16), np.int32)
    emb = np.zeros(m, np.int32)
    cols = {k: np.zeros(m, np.int32) for k in ("op", "on", "ip", "inn", "uip", "uin", "vop", "von")}
    rev = np.zeros(m, np.int8)
    grate = np.zeros(m, np.float64)
    state = {"pos": 0, "tot": 0}

    def add(k):
        u, v, s = U[k], V[k], S[k]
        out[u][v] = s
        inn[v][u] = s
        nb[u].add(v)
        nb[v].add(u)
        if s > 0:
            cop[u] += 1
            cip[v] += 1
            state["pos"] += 1
        else:
            con[u] += 1
            cin[v] += 1
        state["tot"] += 1

    def query_row(k, own):
        u, v = U[k], V[k]
        ou, iu, ov, iv = out[u], inn[u], out[v], inn[v]
        cn = nb[u] & nb[v]
        emb[k] = len(cn)
        cnt = [0] * 16
        for w in cn:
            a = ou.get(w)      # u -> w
            b = iu.get(w)      # w -> u
            c = iv.get(w)      # w -> v
            d = ov.get(w)      # v -> w
            if a is not None:
                if c is not None:
                    cnt[(a < 0) * 2 + (c < 0)] += 1
                if d is not None:
                    cnt[4 + (a < 0) * 2 + (d < 0)] += 1
            if b is not None:
                if c is not None:
                    cnt[8 + (b < 0) * 2 + (c < 0)] += 1
                if d is not None:
                    cnt[12 + (b < 0) * 2 + (d < 0)] += 1
        tri[k] = cnt
        p_own = 1 if own > 0 else 0
        n_own = 1 - p_own if own != 0 else 0
        cols["op"][k] = cop[u] - p_own
        cols["on"][k] = con[u] - n_own
        cols["ip"][k] = cip[v] - p_own
        cols["inn"][k] = cin[v] - n_own
        cols["uip"][k] = cip[u]
        cols["uin"][k] = cin[u]
        cols["vop"][k] = cop[v]
        cols["von"][k] = con[v]
        rev[k] = ov.get(u, 0)
        grate[k] = (state["pos"] - p_own + 1.0) / (state["tot"] - (1 if own != 0 else 0) + 2.0)

    if mode == "static":
        for k in range(m):
            add(k)
        for k in np.flatnonzero(want):
            query_row(int(k), S[int(k)])
    else:
        k = 0
        while k < m:
            j = k + 1
            while j < m and T[j] == T[k]:
                j += 1
            for q in range(k, j):
                if want[q]:
                    query_row(q, 0)
            for q in range(k, j):
                add(q)
            k = j
    return Features(mode, tri, emb, cols["op"], cols["on"], cols["ip"], cols["inn"], cols["uip"], cols["uin"],
                    cols["vop"], cols["von"], rev, grate, want)


def brute_force_triads(E: EdgeSet, k: int, mode: str) -> tuple[np.ndarray, int]:
    """Reference implementation for the tests: the 16 triad counts and the embeddedness of edge k, straight from the
    definition, scanning every other edge."""
    u, v = int(E.u[k]), int(E.v[k])
    if mode == "causal":
        ev = [(int(a), int(b), int(c)) for a, b, c, t in zip(E.u, E.v, E.s, E.t) if t < E.t[k]]
    else:
        ev = [(int(a), int(b), int(c)) for i, (a, b, c) in enumerate(zip(E.u, E.v, E.s)) if i != k]
    sign = {(a, b): c for a, b, c in ev}
    nodes = {a for a, _, _ in ev} | {b for _, b, _ in ev}
    cnt = np.zeros(16, int)
    emb = 0
    for w in nodes:
        if w in (u, v):
            continue
        adj_u = (u, w) in sign or (w, u) in sign
        adj_v = (v, w) in sign or (w, v) in sign
        if not (adj_u and adj_v):
            continue
        emb += 1
        for d1, e1 in (("F", (u, w)), ("B", (w, u))):
            for d2, e2 in (("F", (w, v)), ("B", (v, w))):
                if e1 in sign and e2 in sign:
                    name = d1 + d2 + ("p" if sign[e1] > 0 else "m") + ("p" if sign[e2] > 0 else "m")
                    cnt[TYPE_INDEX[name]] += 1
    return cnt, emb


# --------------------------------------------------------------------------------------------------- design matrices

def slog(x):
    """Signed log: sign(x) log(1 + |x|)."""
    x = np.asarray(x, float)
    return np.sign(x) * np.log1p(np.abs(x))


def _logit_shrunk(pos, neg, prior, strength):
    r = (pos + strength * prior) / (pos + neg + strength)
    return special.logit(np.clip(r, 1e-4, 1 - 1e-4))


def person_block(F: Features) -> tuple[np.ndarray, list[str]]:
    """The person terms: what the sender has said before (outgoing signs) and what the receiver has been told before
    (incoming signs), as shrunken log-odds at two prior strengths and as log counts.  This is the empirical a_i and b_j of
    the registry (R-E) and is deliberately generous (eight columns), so that the gain a triad term shows over it is not
    the gain over a weak baseline."""
    cols = [_logit_shrunk(F.op, F.on, F.grate, 1.0), _logit_shrunk(F.ip, F.inn, F.grate, 1.0),
            _logit_shrunk(F.op, F.on, F.grate, 10.0), _logit_shrunk(F.ip, F.inn, F.grate, 10.0),
            np.log1p(F.op), np.log1p(F.on), np.log1p(F.ip), np.log1p(F.inn)]
    names = ["send_logit1", "recv_logit1", "send_logit10", "recv_logit10", "log_send_pos", "log_send_neg",
             "log_recv_pos", "log_recv_neg"]
    return np.column_stack(cols), names


def node_status(F: Features) -> tuple[np.ndarray, np.ndarray]:
    """sigma(u), sigma(v) with sigma(x) = d+_in + d-_out - d-_in - d+_out [L4802], from the evidence counts."""
    su = F.uip + F.on - F.uin - F.op
    sv = F.ip + F.von - F.inn - F.vop
    return su.astype(float), sv.astype(float)


def triad_scalars(F: Features) -> dict[str, np.ndarray]:
    t = F.tri.astype(float)
    return {"bal_strict": t @ BAL_STRICT, "bal_weak": t @ BAL_WEAK, "status_tri": t @ STATUS}


def tri4(F: Features) -> np.ndarray:
    """Undirected triad types: pp, pm, mp, mm summed over the four direction classes [L4816]."""
    t = F.tri.astype(float)
    return np.column_stack([t[:, [0, 4, 8, 12]].sum(1), t[:, [1, 5, 9, 13]].sum(1), t[:, [2, 6, 10, 14]].sum(1),
                            t[:, [3, 7, 11, 15]].sum(1)])


TRI4_NAMES = ["pp", "pm", "mp", "mm"]


def block(F: Features, name: str, transform: str = "raw") -> tuple[np.ndarray, list[str]]:
    """A named block of columns.  transform: 'raw', 'log' (log1p / signed log) or 'share' (counts over total triads)."""
    if name == "person":
        return person_block(F)
    if name in ("tri16", "tri4"):
        X = F.tri.astype(float) if name == "tri16" else tri4(F)
        names = list(TYPES) if name == "tri16" else TRI4_NAMES
        if transform == "log":
            X = np.log1p(X)
        elif transform == "share":
            X = X / np.maximum(X.sum(1, keepdims=True), 1.0)
        return X, names
    if name in ("bal_strict", "bal_weak", "status_tri"):
        x = triad_scalars(F)[name]
        if transform == "log":
            x = slog(x)
        elif transform == "share":
            x = x / np.maximum(F.tri.sum(1), 1.0)
        return x[:, None], [name]
    if name == "status_node":
        su, sv = node_status(F)
        d = sv - su        # positive favours '+': the receiver stands higher than the sender [L4802]
        return (slog(d) if transform == "log" else d)[:, None], [name]
    if name == "recip":
        return np.column_stack([(F.rev > 0).astype(float), (F.rev < 0).astype(float)]), ["rev_pos", "rev_neg"]
    if name == "person_flex":
        P, nm = person_block(F)
        a, b = P[:, 2], P[:, 3]                         # sender and receiver log-odds at prior strength 10
        extra = np.column_stack([a * a, b * b, a * b, P[:, 4] * P[:, 6], P[:, 5] * P[:, 7]])
        return np.column_stack([P, extra]), nm + ["send2", "recv2", "send_x_recv", "pos_x_pos", "neg_x_neg"]
    if name == "tri16_x_person":
        P, _ = person_block(F)
        T = np.log1p(F.tri.astype(float))
        cols = [T * P[:, [2]], T * P[:, [3]]]
        return np.column_stack(cols), [f"{n}*send" for n in TYPES] + [f"{n}*recv" for n in TYPES]
    if name == "person_lite":
        return (np.column_stack([_logit_shrunk(F.op, F.on, F.grate, 1.0), _logit_shrunk(F.ip, F.inn, F.grate, 1.0)]),
                ["send_logit1", "recv_logit1"])
    if name == "degree7":
        # LHK's seven degree features [L4813]: d+_in(v), d-_in(v), d+_out(u), d-_out(u), C(u,v), out(u), in(v)
        X = np.column_stack([F.ip, F.inn, F.op, F.on, F.emb, F.op + F.on, F.ip + F.inn]).astype(float)
        if transform == "log":
            X = np.log1p(X)
        return X, ["d+in(v)", "d-in(v)", "d+out(u)", "d-out(u)", "C", "out(u)", "in(v)"]
    raise KeyError(name)


# variants for T2 and the Variations: name -> (blocks, transform family)
#   'count' transforms (raw / log) apply to tri16, tri4, bal_*, status_tri, status_node; person and recip are fixed.
VARIANTS = {
    "person": ("person",),
    "person+bal_strict": ("person", "bal_strict"),
    "person+bal_weak": ("person", "bal_weak"),
    "person+status": ("person", "status_tri", "status_node"),
    "person+bal_strict+status": ("person", "bal_strict", "status_tri", "status_node"),
    "person+bal_weak+status": ("person", "bal_weak", "status_tri", "status_node"),
    "person+tri4": ("person", "tri4"),
    "person+tri16": ("person", "tri16"),
    "person+tri16+status": ("person", "tri16", "status_node"),
    "person+recip": ("person", "recip"),
    "person+tri16+recip": ("person", "tri16", "recip"),
    "person_flex": ("person_flex",),
    "person_flex+tri16+interactions": ("person_flex", "tri16", "tri16_x_person"),
    "person_flex+tri16+interactions+recip": ("person_flex", "tri16", "tri16_x_person", "recip", "status_node"),
    "tri16": ("tri16",),
    "tri4": ("tri4",),
    "bal_strict": ("bal_strict",),
    "bal_weak": ("bal_weak",),
    "status": ("status_tri", "status_node"),
    "tri16+status": ("tri16", "status_node"),
}


def design(F: Features, blocks: tuple[str, ...], transform: str = "raw") -> tuple[np.ndarray, list[str]]:
    Xs, names = [], []
    for b in blocks:
        tr = transform if b not in ("person", "person_lite", "person_flex", "tri16_x_person", "recip") else "raw"
        X, nm = block(F, b, tr)
        Xs.append(X)
        names += nm
    return np.column_stack(Xs), names


# --------------------------------------------------------------------------------------------------- logistic model

@dataclass
class LogitFit:
    coef: np.ndarray         # original units, without intercept
    intercept: float
    cov: np.ndarray | None   # (k+1, k+1) in original units, intercept first; cluster-robust if clusters were given
    cov2: np.ndarray | None  # the same with two-way clustering (clusters and cluster2), if both were given
    mu: np.ndarray
    sd: np.ndarray
    ridge: float
    n_iter: int
    converged: bool
    loglik: float            # unpenalised log-likelihood at the solution
    n: int

    def decision(self, X) -> np.ndarray:
        return np.asarray(X, float) @ self.coef + self.intercept

    def predict_proba(self, X) -> np.ndarray:
        return special.expit(self.decision(X))

    @property
    def se(self) -> np.ndarray:
        """Standard errors of (intercept, coef...) or NaN if no covariance was requested."""
        if self.cov is None:
            return np.full(len(self.coef) + 1, np.nan)
        return np.sqrt(np.maximum(np.diag(self.cov), 0.0))

    @property
    def se2(self) -> np.ndarray:
        """Standard errors with two-way clustering (Cameron-Gelbach-Miller), NaN if not requested."""
        if self.cov2 is None:
            return np.full(len(self.coef) + 1, np.nan)
        return np.sqrt(np.maximum(np.diag(self.cov2), 0.0))

    @property
    def n_params(self) -> int:
        return len(self.coef) + 1


def fit_logit(X, y, ridge: float = 1.0, cluster=None, max_iter: int = 80, tol: float = 1e-10,
              se: bool = False, cluster2=None) -> LogitFit:
    """Ridge-penalised logistic regression by Newton steps with step halving.  Columns are standardised for the fit and
    reported in their own units; the intercept is not penalised.  `ridge` is on the scale of the summed log-likelihood
    for standardised columns, so it is negligible at the sample sizes used here unless it is large.  With se=True the
    covariance is the cluster-robust sandwich (clusters given, else observations) with the G/(G-1) correction.  With
    `cluster2` as well, `cov2` is the two-way version (sum of the two one-way meats minus the meat of their intersection,
    which is the single observation when no (cluster, cluster2) pair repeats), clipped to be positive semi-definite."""
    X = np.asarray(X, float)
    y = np.asarray(y, float)
    n, k = X.shape
    mu = X.mean(0)
    sd = X.std(0)
    sd = np.where(sd < 1e-12, 1.0, sd)
    Z = np.column_stack([np.ones(n), (X - mu) / sd])
    pen = np.full(k + 1, float(ridge))
    pen[0] = 0.0
    p0 = float(np.clip(y.mean(), 1e-6, 1 - 1e-6))
    beta = np.zeros(k + 1)
    beta[0] = math.log(p0 / (1 - p0))

    def obj(b):
        eta = Z @ b
        return float(np.sum(np.logaddexp(0.0, eta) - y * eta) + 0.5 * np.sum(pen * b * b))

    f = obj(beta)
    converged = False
    it = 0
    for it in range(1, max_iter + 1):
        p = special.expit(Z @ beta)
        g = Z.T @ (p - y) + pen * beta
        W = p * (1 - p)
        H = (Z * W[:, None]).T @ Z + np.diag(pen) + 1e-9 * np.eye(k + 1)
        step = np.linalg.solve(H, g)
        t = 1.0
        while True:
            bn = beta - t * step
            fn = obj(bn)
            if fn <= f + 1e-10 * (1 + abs(f)) or t < 1e-10:
                break
            t *= 0.5
        d = np.max(np.abs(bn - beta))
        beta, fprev, f = bn, f, fn
        if d < 1e-8 or abs(fprev - f) < tol * (1 + abs(f)):
            converged = True
            break
    p = special.expit(Z @ beta)
    eta = Z @ beta
    ll = float(-np.sum(np.logaddexp(0.0, eta) - y * eta))
    # back to original units
    coef = beta[1:] / sd
    intercept = float(beta[0] - np.sum(beta[1:] * mu / sd))
    cov = None
    cov2 = None
    if se:
        W = p * (1 - p)
        H = (Z * W[:, None]).T @ Z + np.diag(pen) + 1e-9 * np.eye(k + 1)
        Hinv = np.linalg.inv(H)
        R = Z * (y - p)[:, None]

        def meat_of(cl_):
            if cl_ is None:
                S = R
            else:
                _, inv = np.unique(np.asarray(cl_), return_inverse=True)
                G = inv.max() + 1
                S = np.column_stack([np.bincount(inv, weights=R[:, j], minlength=G) for j in range(k + 1)])
            Gn = S.shape[0]
            return S.T @ S * (Gn / max(Gn - 1, 1))

        m1 = meat_of(cluster)
        A = np.zeros((k + 1, k + 1))
        A[0, 0] = 1.0
        A[0, 1:] = -mu / sd
        A[1:, 1:] = np.diag(1.0 / sd)
        cov = A @ (Hinv @ m1 @ Hinv) @ A.T
        if cluster2 is not None:
            m2 = meat_of(cluster2)
            V2 = Hinv @ (m1 + m2 - R.T @ R) @ Hinv
            ev, Q = np.linalg.eigh((V2 + V2.T) / 2)
            V2 = (Q * np.clip(ev, 0.0, None)) @ Q.T
            cov2 = A @ V2 @ A.T
    return LogitFit(coef, intercept, cov, cov2, mu, sd, float(ridge), it, converged, ll, n)


# --------------------------------------------------------------------------------------------------- metrics

def auc_score(y, s) -> float:
    y = np.asarray(y).astype(bool)
    n1 = int(y.sum())
    n0 = len(y) - n1
    if n1 == 0 or n0 == 0:
        return float("nan")
    r = stats.rankdata(s)
    return float((r[y].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0))


def logloss(y, p) -> float:
    p = np.clip(np.asarray(p, float), 1e-9, 1 - 1e-9)
    y = np.asarray(y, float)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def balanced_accuracy(y, p, thr: float) -> float:
    y = np.asarray(y).astype(bool)
    pred = np.asarray(p) >= thr
    if y.sum() == 0 or (~y).sum() == 0:
        return float("nan")
    return float(0.5 * (pred[y].mean() + (~pred[~y]).mean()))


class WeightedScorer:
    """Metrics of one score vector under non-negative observation weights (bootstrap multiplicities).  Sorting is done
    once, each replicate is a few passes."""

    def __init__(self, y, p):
        self.y = np.asarray(y, float)
        self.p = np.asarray(p, float)
        self.uniq, self.inv = np.unique(self.p, return_inverse=True)
        self._lp = np.log(np.clip(self.p, 1e-9, 1 - 1e-9))
        self._lq = np.log(np.clip(1 - self.p, 1e-9, 1 - 1e-9))

    def auc(self, w=None) -> float:
        w = np.ones(len(self.y)) if w is None else w
        npos = np.bincount(self.inv, weights=w * self.y, minlength=len(self.uniq))
        nneg = np.bincount(self.inv, weights=w * (1 - self.y), minlength=len(self.uniq))
        below = np.cumsum(nneg) - nneg
        Wp, Wn = npos.sum(), nneg.sum()
        if Wp == 0 or Wn == 0:
            return float("nan")
        return float(np.sum(npos * (below + 0.5 * nneg)) / (Wp * Wn))

    def ba(self, thr: float, w=None) -> float:
        w = np.ones(len(self.y)) if w is None else w
        pred = self.p >= thr
        wp, wn = w * self.y, w * (1 - self.y)
        if wp.sum() == 0 or wn.sum() == 0:
            return float("nan")
        return float(0.5 * (np.sum(wp * pred) / wp.sum() + np.sum(wn * ~pred) / wn.sum()))

    def logloss(self, w=None) -> float:
        w = np.ones(len(self.y)) if w is None else w
        return float(-np.sum(w * (self.y * self._lp + (1 - self.y) * self._lq)) / w.sum())


class ClusterBoot:
    """Cluster bootstrap multiplicities, generated lazily: replicate b gives every observation the number of times its
    cluster was drawn (clusters resampled with replacement).  With a second clustering the two are resampled
    independently and an observation's weight is the product of its two multiplicities (the pigeonhole bootstrap of Owen
    and Eckles, which respects dependence along both senders and receivers and is slightly conservative).  One instance is
    shared by every model being compared, so differences are paired."""

    def __init__(self, cluster, B: int, seed: int, cluster2=None):
        rng = np.random.default_rng(seed)
        _, self.cl = np.unique(np.asarray(cluster), return_inverse=True)
        G = int(self.cl.max()) + 1
        self.counts = rng.multinomial(G, np.full(G, 1.0 / G), size=B).astype(np.int32)
        self.cl2 = None
        if cluster2 is not None:
            _, self.cl2 = np.unique(np.asarray(cluster2), return_inverse=True)
            G2 = int(self.cl2.max()) + 1
            self.counts2 = rng.multinomial(G2, np.full(G2, 1.0 / G2), size=B).astype(np.int32)
        self.B = B

    def w(self, b: int) -> np.ndarray:
        w = self.counts[b][self.cl].astype(np.float64)
        if self.cl2 is not None:
            w = w * self.counts2[b][self.cl2]
        return w


def percentile_ci(x, level: float = 0.95) -> tuple[float, float]:
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    if len(x) == 0:
        return float("nan"), float("nan")
    a = (1 - level) / 2
    return float(np.quantile(x, a)), float(np.quantile(x, 1 - a))


# --------------------------------------------------------------------------------------------------- T2: forward chain

FOLD_FRACS = (0.40, 0.55, 0.70, 0.85, 1.00)     # forward-chained: train [0, b_j), test [b_j, b_j+1)
INNER_FRAC = 0.30                                # transform selection: train [0, 0.30), validate [0.30, 0.40)
COUNT_BLOCKS = ("tri16", "tri4", "bal_strict", "bal_weak", "status_tri", "status_node", "degree7")
EMB_STRATA = ((0, 0, "C = 0"), (1, 4, "C 1-4"), (5, 24, "C 5-24"), (25, 10 ** 9, "C >= 25"))


def aligned_index(t: np.ndarray, frac: float) -> int:
    """Index at or after frac * m that does not split a group of equal timestamps."""
    m = len(t)
    i = int(round(frac * m))
    if i >= m:
        return m
    while 0 < i < m and t[i] == t[i - 1]:
        i += 1
    return i


def fold_bounds(t: np.ndarray, fracs=FOLD_FRACS) -> list[int]:
    return [aligned_index(t, f) for f in fracs]


@dataclass
class SpecResult:
    name: str
    blocks: tuple
    transform: str
    n_params: int
    pred: np.ndarray            # NaN outside the pooled test window
    thr: np.ndarray             # per-edge BA threshold (training prevalence of the fold)
    fold_of: np.ndarray         # fold index of each edge (-1 outside the test window)
    ridge: float


def run_spec(E: EdgeSet, F: Features, name: str, blocks: tuple, bounds: list[int] | None = None,
             ridge: float = 1.0, transforms=("raw", "log")) -> SpecResult:
    """Forward-chained held-out predictions of one variant.  The transform (raw or log counts) is chosen on an inner
    validation block of the first training window and then held fixed; each fold is refit on every edge before its test
    block.  The features of every edge come only from strictly earlier edges (F is a causal Features)."""
    if F.mode != "causal":
        raise ValueError("held-out prediction needs causal features")
    m = E.m
    y = E.y
    bounds = fold_bounds(E.t) if bounds is None else bounds
    i_in = aligned_index(E.t, INNER_FRAC)
    tr_choice = "raw"
    if any(b in COUNT_BLOCKS for b in blocks) and len(transforms) > 1:
        best = None
        for tr in transforms:
            X, _ = design(F, blocks, tr)
            fit = fit_logit(X[:i_in], y[:i_in], ridge)
            ll = logloss(y[i_in:bounds[0]], fit.predict_proba(X[i_in:bounds[0]]))
            if best is None or ll < best[0]:
                best = (ll, tr)
        tr_choice = best[1]
    X, names = design(F, blocks, tr_choice)
    pred = np.full(m, np.nan)
    thr = np.full(m, np.nan)
    fold_of = np.full(m, -1, np.int16)
    for j in range(len(bounds) - 1):
        a, lo, hi = bounds[j], bounds[j], bounds[j + 1]
        fit = fit_logit(X[:a], y[:a], ridge)
        pred[lo:hi] = fit.predict_proba(X[lo:hi])
        thr[lo:hi] = y[:a].mean()
        fold_of[lo:hi] = j
    return SpecResult(name, tuple(blocks), tr_choice, X.shape[1] + 1, pred, thr, fold_of, ridge)


def run_specs(E: EdgeSet, F: Features, names=None, ridge: float = 1.0, bounds=None, verbose: bool = False) -> dict:
    names = list(VARIANTS) if names is None else list(names)
    out = {}
    for nm in names:
        t0 = time.time()
        out[nm] = run_spec(E, F, nm, VARIANTS[nm], bounds=bounds, ridge=ridge)
        if verbose:
            print(f"    {nm:28s} {out[nm].transform:4s} k={out[nm].n_params:3d}  {time.time() - t0:5.1f}s", flush=True)
    return out


def test_window(res: SpecResult) -> np.ndarray:
    return ~np.isnan(res.pred)


def summarise_specs(E: EdgeSet, F: Features, results: dict, B: int = 300, seed: int = 20261101,
                    mask: np.ndarray | None = None, ref: str = "person", twoway: bool = False) -> dict:
    """Pooled held-out metrics of each variant with cluster-bootstrap intervals, and paired differences from `ref`
    (AUC, log-loss).  `mask` restricts the evaluation to a stratum of edges (e.g. embeddedness >= 5)."""
    first = next(iter(results.values()))
    win = test_window(first)
    if mask is not None:
        win = win & mask
    idx = np.flatnonzero(win)
    y = E.y[idx]
    boot = ClusterBoot(E.cluster[idx], B, seed, E.u[idx] if twoway else None)
    ws = [boot.w(b) for b in range(B)] if len(idx) * B < 6e7 else None
    wget = (lambda b: ws[b]) if ws is not None else boot.w
    sc = {nm: WeightedScorer(y, r.pred[idx]) for nm, r in results.items()}
    out = {"n": int(len(idx)), "pos_share": float(y.mean()), "models": {}, "diff": {}}
    base = {}
    for nm, r in results.items():
        s = sc[nm]
        thr = r.thr[idx]
        a = np.array([s.auc(wget(b)) for b in range(B)])
        l = np.array([s.logloss(wget(b)) for b in range(B)])
        ba_point = _ba_array_thr(y, r.pred[idx], thr)
        out["models"][nm] = dict(auc=s.auc(), auc_ci=percentile_ci(a), logloss=s.logloss(), logloss_ci=percentile_ci(l),
                                 ba=ba_point, n_params=r.n_params, transform=r.transform)
        base[nm] = (a, l)
    if ref in results:
        a0, l0 = base[ref]
        for nm in results:
            if nm == ref:
                continue
            a, l = base[nm]
            out["diff"][nm] = dict(
                d_auc=out["models"][nm]["auc"] - out["models"][ref]["auc"], d_auc_ci=percentile_ci(a - a0),
                d_logloss=out["models"][nm]["logloss"] - out["models"][ref]["logloss"],
                d_logloss_ci=percentile_ci(l - l0))
    return out


def _ba_array_thr(y, p, thr) -> float:
    y = np.asarray(y).astype(bool)
    pred = np.asarray(p) >= np.asarray(thr)
    if y.sum() == 0 or (~y).sum() == 0:
        return float("nan")
    return float(0.5 * (pred[y].mean() + (~pred[~y]).mean()))


def paired_diff(E: EdgeSet, results: dict, a: str, b: str, mask: np.ndarray | None = None, B: int = 300,
                seed: int = 20261101, metric: str = "auc", twoway: bool = False) -> dict:
    """Difference metric(a) - metric(b) on the pooled test window (optionally a stratum), cluster bootstrap."""
    win = test_window(results[a]) & test_window(results[b])
    if mask is not None:
        win = win & mask
    idx = np.flatnonzero(win)
    if len(idx) < 50 or E.y[idx].min() == E.y[idx].max():
        return dict(n=len(idx), diff=float("nan"), ci=(float("nan"), float("nan")))
    y = E.y[idx]
    cb = ClusterBoot(E.cluster[idx], B, seed, E.u[idx] if twoway else None)
    sa, sb = WeightedScorer(y, results[a].pred[idx]), WeightedScorer(y, results[b].pred[idx])
    f = (lambda s, w: s.auc(w)) if metric == "auc" else (lambda s, w: s.logloss(w))
    boot = np.array([f(sa, cb.w(i)) - f(sb, cb.w(i)) for i in range(B)])
    return dict(n=int(len(idx)), diff=f(sa, None) - f(sb, None), ci=percentile_ci(boot))


# --------------------------------------------------------------------------------------------------- T1 / T3: coefficients

def classify_z(sign: int, z: float, support: int) -> str:
    """R1: SUPPORTED / CONTRADICTED / UNDECIDED for a coefficient with predicted sign `sign`."""
    if support < RULE_MIN_SUPPORT or not np.isfinite(z):
        return "UNDECIDED"
    if sign * z > Z95:
        return "SUPPORTED"
    if sign * z < -Z95:
        return "CONTRADICTED"
    return "UNDECIDED"


def theory_signs() -> dict[str, dict[str, int]]:
    return {"balance": {n: int(BAL_STRICT[i]) for i, n in enumerate(TYPES)},
            "weak": {n: int(BAL_WEAK[i]) for i, n in enumerate(TYPES)},
            "status": {n: int(STATUS[i]) for i, n in enumerate(TYPES)}}


def coefficient_table(E: EdgeSet, F: Features, blocks=("tri16",), subset: np.ndarray | None = None,
                      ridge: float = 1e-4) -> dict:
    """16-type logistic fit on a set of edges (raw counts, as LHK) with cluster-robust standard errors, the R1 status of
    each forward-chain type, and the agreement of the learned signs with balance, weak balance and status."""
    sel = np.ones(E.m, bool) if subset is None else np.asarray(subset, bool)
    X, names = design(F, blocks, "raw")
    fit = fit_logit(X[sel], E.y[sel], ridge=ridge, cluster=E.cluster[sel], se=True, cluster2=E.u[sel])
    se = fit.se[1:]
    se2 = fit.se2[1:]
    rows = {}
    for j, nm in enumerate(names):
        if nm in TYPE_INDEX:
            support = int((F.tri[sel, TYPE_INDEX[nm]] > 0).sum())
        else:
            support = int(sel.sum())
        z = fit.coef[j] / se[j] if se[j] > 0 else float("nan")
        z2 = fit.coef[j] / se2[j] if se2[j] > 0 else float("nan")
        rows[nm] = dict(coef=float(fit.coef[j]), se=float(se[j]), z=float(z), se2=float(se2[j]), z2=float(z2),
                        support=support)
    for nm in FORWARD:
        r = rows[nm]
        r["status"] = classify_z(FORWARD_SIGN[nm], r["z"], r["support"])
        r["status2"] = classify_z(FORWARD_SIGN[nm], r["z2"], r["support"])
    ts = theory_signs()
    agree = {}
    for th, tab in ts.items():
        pred = [n for n in TYPES if tab[n] != 0]
        sig = [n for n in pred if rows[n]["support"] >= RULE_MIN_SUPPORT and abs(rows[n]["z"]) > Z95]
        agree[th] = dict(n_predicted=len(pred), n_significant=len(sig),
                         n_agree=sum(1 for n in sig if np.sign(rows[n]["coef"]) == tab[n]))
    st = [rows[n]["status"] for n in FORWARD]
    st2 = [rows[n]["status2"] for n in FORWARD]
    verdict = dict(
        form_transfers=(rows["FFmm"]["status"] == "SUPPORTED") and ("CONTRADICTED" not in st),
        refuted=(rows["FFmm"]["status"] == "CONTRADICTED"),
        form_transfers2=(rows["FFmm"]["status2"] == "SUPPORTED") and ("CONTRADICTED" not in st2),
        refuted2=(rows["FFmm"]["status2"] == "CONTRADICTED"),
        mm_adequate=bool(rows["FFmm"]["support"] >= RULE_MIN_SUPPORT))
    return dict(n=int(sel.sum()), pos_share=float(E.y[sel].mean()), intercept=float(fit.intercept),
                intercept_se=float(fit.se[0]), intercept_se2=float(fit.se2[0]), rows=rows, agree=agree,
                verdict=verdict, converged=fit.converged, loglik=fit.loglik, n_params=fit.n_params)


def make_bins(E: EdgeSet, unit: str, min_n: int) -> np.ndarray:
    """Bin label (0..B-1) of each edge: calendar years or quarters, small bins merged into a neighbour so that each has
    at least `min_n` edges."""
    yr = E.year.astype(int)
    month = (E.t.astype("int64").astype("datetime64[s]").astype("datetime64[M]").astype("int64") % 12)
    if unit == "quarter":
        lab = yr * 4 + month // 3
    elif unit == "month":
        lab = yr * 12 + month
    else:
        lab = yr
    uniq = np.unique(lab)
    counts = {int(k): int((lab == k).sum()) for k in uniq}
    groups = [[int(k)] for k in uniq]
    changed = True
    while changed and len(groups) > 1:
        changed = False
        sizes = [sum(counts[k] for k in g) for g in groups]
        i = int(np.argmin(sizes))
        if sizes[i] < min_n:
            j = i + 1 if i + 1 < len(groups) else i - 1
            if i + 1 < len(groups) and i - 1 >= 0 and sizes[i - 1] < sizes[i + 1]:
                j = i - 1
            a, b = sorted((i, j))
            groups[a] = groups[a] + groups[b]
            del groups[b]
            changed = True
    mapping = {k: gi for gi, g in enumerate(groups) for k in g}
    return np.array([mapping[int(k)] for k in lab], dtype=np.int16)


def bin_names(E: EdgeSet, bins: np.ndarray, unit: str) -> list[str]:
    yr = E.year.astype(int)
    out = []
    for b in range(int(bins.max()) + 1):
        sel = bins == b
        if unit in ("quarter", "month"):
            month = (E.t[sel].astype("int64").astype("datetime64[s]").astype("datetime64[M]").astype("int64") % 12)
            if unit == "quarter":
                lab = yr[sel] * 4 + month // 3
                f = lambda x: f"{x // 4}Q{x % 4 + 1}"
            else:
                lab = yr[sel] * 12 + month
                f = lambda x: f"{x // 12}-{x % 12 + 1:02d}"
            lo, hi = lab.min(), lab.max()
            out.append(f(lo) if lo == hi else f"{f(lo)}..{f(hi)}")
        else:
            lo, hi = yr[sel].min(), yr[sel].max()
            out.append(str(lo) if lo == hi else f"{lo}-{str(hi)[2:]}")
    return out


def dersimonian_laird(est, se) -> dict:
    """Heterogeneity of independent estimates: Cochran's Q, its chi-square p, I^2, the random-effects tau and mean."""
    est, se = np.asarray(est, float), np.asarray(se, float)
    ok = np.isfinite(est) & np.isfinite(se) & (se > 0)
    est, se = est[ok], se[ok]
    k = len(est)
    if k < 2:
        return dict(k=k, Q=float("nan"), p=float("nan"), I2=float("nan"), tau=float("nan"), mean=float("nan"))
    w = 1 / se ** 2
    mean = np.sum(w * est) / np.sum(w)
    Q = float(np.sum(w * (est - mean) ** 2))
    p = float(stats.chi2.sf(Q, k - 1))
    I2 = max(0.0, (Q - (k - 1)) / Q) if Q > 0 else 0.0
    c = np.sum(w) - np.sum(w ** 2) / np.sum(w)
    tau2 = max(0.0, (Q - (k - 1)) / c)
    return dict(k=k, Q=Q, p=p, I2=float(I2), tau=float(math.sqrt(tau2)), mean=float(mean))


def anova_icc(group, y) -> float:
    """One-way ANOVA intracluster correlation of a binary outcome across unbalanced groups (nodes)."""
    group = np.asarray(group)
    y = np.asarray(y, float)
    _, g = np.unique(group, return_inverse=True)
    G = g.max() + 1
    n_i = np.bincount(g, minlength=G).astype(float)
    sum_i = np.bincount(g, weights=y, minlength=G)
    N = n_i.sum()
    if G < 2 or N <= G:
        return float("nan")
    grand = y.sum() / N
    ssb = np.sum(sum_i ** 2 / n_i) - N * grand ** 2
    ssw = np.sum(y ** 2) - np.sum(sum_i ** 2 / n_i)
    msb = ssb / (G - 1)
    msw = ssw / (N - G)
    n0 = (N - np.sum(n_i ** 2) / N) / (G - 1)
    den = msb + (n0 - 1) * msw
    return float((msb - msw) / den) if den > 0 else float("nan")


def drift_by_bin(E: EdgeSet, unit: str, min_n: int, design_kind: str = "snapshot", F_causal: Features | None = None,
                 person: bool = False) -> dict:
    """Refit the 16-type model in each bin.  'snapshot': the bin's edges alone form the graph (static features inside
    the bin).  'history': features are the causal ones of the full history, fitted on the bin's edges only."""
    bins = make_bins(E, unit, min_n)
    names = bin_names(E, bins, unit)
    per = []
    for b in range(len(names)):
        idx = np.flatnonzero(bins == b)
        if design_kind == "snapshot":
            Eb = E.take(idx)
            Fb = compute_features(Eb, "static")
        else:
            assert F_causal is not None
            Eb = E.take(idx)
            Fb = Features(**{**F_causal.__dict__,
                             **{k: getattr(F_causal, k)[idx] for k in
                                ("tri", "emb", "op", "on", "ip", "inn", "uip", "uin", "vop", "von", "rev", "grate",
                                 "queried")}})
        tab = coefficient_table(Eb, Fb, blocks=(("person", "tri16") if person else ("tri16",)))
        tab["name"] = names[b]
        tab["edges"] = int(len(idx))
        tab["t_lo"], tab["t_hi"] = float(Eb.t.min()), float(Eb.t.max())
        tab["icc_send"] = anova_icc(Eb.u, Eb.y)
        tab["icc_recv"] = anova_icc(Eb.v, Eb.y)
        tab["base_logit"] = float(special.logit(np.clip(Eb.y.mean(), 1e-6, 1 - 1e-6)))
        per.append(tab)
    het = {}
    for nm in FORWARD:
        het[nm] = dersimonian_laird([p["rows"][nm]["coef"] for p in per], [p["rows"][nm]["se"] for p in per])
    het["intercept"] = dersimonian_laird([p["intercept"] for p in per], [p["intercept_se"] for p in per])
    ints = np.array([p["intercept"] for p in per])
    flips = {nm: sum(1 for p in per if p["rows"][nm]["status"] == "CONTRADICTED") for nm in FORWARD}
    flips2 = {nm: sum(1 for p in per if p["rows"][nm]["status2"] == "CONTRADICTED") for nm in FORWARD}
    supported = {nm: sum(1 for p in per if p["rows"][nm]["status"] == "SUPPORTED") for nm in FORWARD}
    supported2 = {nm: sum(1 for p in per if p["rows"][nm]["status2"] == "SUPPORTED") for nm in FORWARD}
    adequate = {nm: sum(1 for p in per if p["rows"][nm]["support"] >= RULE_MIN_SUPPORT) for nm in FORWARD}
    verdict = dict(
        flipped_types=[nm for nm in FORWARD if flips[nm] >= RULE_FLIP_BINS],
        refuted=any(flips[nm] >= RULE_FLIP_BINS for nm in FORWARD),
        intercepts_move=bool(het["intercept"]["p"] < 1e-3 and (ints.max() - ints.min()) >= RULE_INTERCEPT_RANGE),
        intercept_range=float(ints.max() - ints.min()), flips=flips, supported=supported, adequate=adequate,
        flips2=flips2, supported2=supported2, refuted2=any(flips2[nm] >= RULE_FLIP_BINS for nm in FORWARD),
        flipped_types2=[nm for nm in FORWARD if flips2[nm] >= RULE_FLIP_BINS])
    return dict(unit=unit, kind=design_kind, bins=per, het=het, verdict=verdict, person=person)


# --------------------------------------------------------------------------------------------------- T4: symmetry

def wilson(k: int, n: int, z: float = Z95) -> tuple[float, float]:
    if n == 0:
        return float("nan"), float("nan")
    p = k / n
    den = 1 + z * z / n
    c = (p + z * z / (2 * n)) / den
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / den
    return c - h, c + h


def reciprocated_pairs(E: EdgeSet) -> dict:
    """Each unordered pair with a tie in both directions once: indices of the earlier and the later tie."""
    n = E.n_nodes
    key = E.u.astype(np.int64) * n + E.v
    order = np.argsort(key)
    sk = key[order]
    rkey = E.v.astype(np.int64) * n + E.u
    pos = np.searchsorted(sk, rkey)
    pos = np.minimum(pos, len(sk) - 1)
    has = sk[pos] == rkey
    i = np.flatnonzero(has & (E.u < E.v))
    j = order[pos[i]]
    first = np.where(E.t[i] <= E.t[j], i, j)
    second = np.where(E.t[i] <= E.t[j], j, i)
    return dict(i=i, j=j, first=first, second=second)


def symmetry_test(E: EdgeSet, F_static: Features, B: int = 300, seed: int = 20261101) -> dict:
    """T4.  Share of reciprocated pairs whose two ties have opposite signs, with a Wilson interval; the null of
    independent signs at the observed marginals; the null of the person model (the sender-and-receiver model fitted on
    every edge, the expected opposite share given each tie's own predicted probability); the correlation of the two
    ties' residuals from that model; the reply sign given the first sign; and the share by the year of the later tie."""
    rp = reciprocated_pairs(E)
    i, j = rp["i"], rp["j"]
    n = len(i)
    if n == 0:
        return dict(n_pairs=0)
    si, sj = E.s[i], E.s[j]
    opp = (si != sj)
    k = int(opp.sum())
    pos_share = float(np.mean(np.concatenate([E.s[i] > 0, E.s[j] > 0])))
    X, _ = design(F_static, ("person",), "raw")
    fit = fit_logit(X, E.y, ridge=1.0)
    p = fit.predict_proba(X)
    pi, pj = p[i], p[j]
    exp_opp = float(np.mean(pi * (1 - pj) + (1 - pi) * pj))
    ri, rj = E.y[i] - pi, E.y[j] - pj
    rng = np.random.default_rng(seed)
    bs = np.empty(B)
    bc = np.empty(B)
    with np.errstate(invalid="ignore", divide="ignore"):         # a degenerate resample (constant residuals) gives NaN
        rcorr = float(np.corrcoef(ri, rj)[0, 1]) if n > 2 else float("nan")
        for b in range(B):
            r = rng.integers(0, n, n)
            bs[b] = opp[r].mean()
            bc[b] = np.corrcoef(ri[r], rj[r])[0, 1]
    first, second = rp["first"], rp["second"]
    s1, s2 = E.s[first], E.s[second]
    reply = {}
    for lab, mask in (("after +", s1 > 0), ("after -", s1 < 0)):
        nn = int(mask.sum())
        kk = int((s2[mask] > 0).sum())
        reply[lab] = dict(n=nn, p_pos=kk / nn if nn else float("nan"), ci=wilson(kk, nn))
    yrs = E.year[second]
    by_year = {}
    for yv in np.unique(yrs):
        mk = yrs == yv
        by_year[int(yv)] = dict(n=int(mk.sum()), share=float(opp[mk].mean()),
                                ci=wilson(int(opp[mk].sum()), int(mk.sum())))
    tied = int((E.t[first] == E.t[second]).sum())
    return dict(n_pairs=n, n_edges=E.m, share_pairs=2 * n / E.m, opposite=k, share=k / n, ci=wilson(k, n),
                pos_share_in_pairs=pos_share, null_independent=2 * pos_share * (1 - pos_share),
                null_person=exp_opp, resid_corr=rcorr, resid_corr_ci=percentile_ci(bc),
                share_boot_ci=percentile_ci(bs), reply=reply, by_year=by_year, simultaneous_pairs=tied,
                rare=bool(k / n <= RULE_RARE))


# --------------------------------------------------------------------------------------------------- T5: visibility

def _ba_binary(y, pred_pos, w=None) -> float:
    y = np.asarray(y, float)
    w = np.ones(len(y)) if w is None else w
    wp, wn = w * y, w * (1 - y)
    if wp.sum() == 0 or wn.sum() == 0:
        return float("nan")
    return float(0.5 * (np.sum(wp * pred_pos) / wp.sum() + np.sum(wn * ~pred_pos) / wn.sum()))


def visibility_test(E: EdgeSet, F: Features, B: int = 300, seed: int = 20261101, bins: np.ndarray | None = None,
                    bin_labels: list[str] | None = None, twoway: bool = False) -> dict:
    """T5.  Balanced accuracy of InSign (predict '+' iff the target's other incoming ties are at least as often '+' as
    '-') and OutSign (the same for the sender's other outgoing ties) [L4802], by embeddedness stratum and, if `bins` is
    given, by date bin; the gap InSign - OutSign with cluster-bootstrap intervals; the verdict of R5 at C = 0."""
    y = E.y
    in_pred = F.ip >= F.inn
    out_pred = F.op >= F.on
    boot = ClusterBoot(E.cluster, B, seed, E.u if twoway else None)
    Ws = [boot.w(b) for b in range(B)] if E.m * B < 6e7 else None

    def gap_stats(mask):
        idx = np.flatnonzero(mask)
        if len(idx) < 30 or y[idx].min() == y[idx].max():
            return None
        yi = y[idx]
        a_ = _ba_binary(yi, in_pred[idx])
        b_ = _ba_binary(yi, out_pred[idx])
        wb = (lambda r: Ws[r][idx]) if Ws is not None else (lambda r: boot.w(r)[idx])
        ba_in = np.array([_ba_binary(yi, in_pred[idx], wb(r)) for r in range(B)])
        ba_out = np.array([_ba_binary(yi, out_pred[idx], wb(r)) for r in range(B)])
        return dict(n=int(len(idx)), pos_share=float(yi.mean()), ba_in=a_, ba_out=b_, gap=a_ - b_,
                    ba_in_ci=percentile_ci(ba_in), ba_out_ci=percentile_ci(ba_out),
                    gap_ci=percentile_ci(ba_in - ba_out))

    out = {"mode": F.mode, "all": gap_stats(np.ones(E.m, bool)), "strata": {}, "bins": {}}
    for lo, hi, lab in EMB_STRATA:
        out["strata"][lab] = gap_stats((F.emb >= lo) & (F.emb <= hi))
    if bins is not None:
        for b in range(int(bins.max()) + 1):
            out["bins"][bin_labels[b] if bin_labels else str(b)] = gap_stats((bins == b) & (F.emb == 0))
    g = out["strata"]["C = 0"]
    if g is None:
        out["verdict"] = "UNDECIDED"
    elif g["gap_ci"][0] > RULE_GAP:
        out["verdict"] = "SUPPORTED"
    elif g["gap_ci"][1] < RULE_GAP:
        out["verdict"] = "ABSENT"
    else:
        out["verdict"] = "UNDECIDED"
    return out


# --------------------------------------------------------------------------------------------------- Variations

def static_cv(E: EdgeSet, F: Features, names: list[str], K: int = 5, seed: int = 20261101, ridge: float = 1.0,
              transform: str = "log") -> dict:
    """LHK's protocol: the evidence is the whole snapshot (every other edge), edges are split at random into K folds,
    each fold is predicted by a model fitted on the others (10-fold in LHK; K = 5 here).  Returned: out-of-fold scores of
    each variant, for comparison with the time-split numbers and with L4826-L4829."""
    if F.mode != "static":
        raise ValueError("static_cv needs static features")
    m = E.m
    y = E.y
    rng = np.random.default_rng(seed)
    fold = rng.integers(0, K, m)
    out = {}
    for nm in names:
        blocks = {**VARIANTS, "degree7": ("degree7",), "degree7+tri16": ("degree7", "tri16"),
                  "person_lite": ("person_lite",), "person_lite+tri16": ("person_lite", "tri16")}[nm]
        X, _ = design(F, blocks, transform)
        pred = np.empty(m)
        for f in range(K):
            tr, te = fold != f, fold == f
            fit = fit_logit(X[tr], y[tr], ridge)
            pred[te] = fit.predict_proba(X[te])
        out[nm] = SpecResult(nm, blocks, transform, X.shape[1] + 1, pred, np.full(m, y.mean()), fold.astype(np.int16),
                             ridge)
    return out


def summarise_static(E: EdgeSet, results: dict, ref: str, masks: dict[str, np.ndarray], B: int = 200,
                     seed: int = 20261101) -> dict:
    out = {}
    for lab, mask in masks.items():
        idx = np.flatnonzero(mask)
        if len(idx) < 100 or E.y[idx].min() == E.y[idx].max():
            continue
        y = E.y[idx]
        cb = ClusterBoot(E.cluster[idx], B, seed)
        sc = {nm: WeightedScorer(y, r.pred[idx]) for nm, r in results.items()}
        base = np.array([sc[ref].auc(cb.w(b)) for b in range(B)])
        rows = {}
        for nm, r in results.items():
            a = np.array([sc[nm].auc(cb.w(b)) for b in range(B)])
            rows[nm] = dict(auc=sc[nm].auc(), ci=percentile_ci(a), ba=_ba_array_thr(y, r.pred[idx], r.thr[idx]),
                            d_auc=sc[nm].auc() - sc[ref].auc(), d_ci=percentile_ci(a - base))
        out[lab] = dict(n=int(len(idx)), pos_share=float(y.mean()), rows=rows)
    return out


def run_frozen_effects(E: EdgeSet, F: Features, with_triad: bool, bounds=None, lam_grid=(0.5, 2.0, 8.0),
                       triad_blocks=("tri16",)) -> SpecResult:
    """The other reading of 'person terms alone': a_i (sender) and b_j (receiver) as ridge-fitted effects, one per node,
    frozen at the end of each training window; a node unseen in training has effect 0.  With triad terms (the causal
    16-type counts, log1p) added if with_triad.  Ridge strength chosen on the inner validation block of the first window."""
    m = E.m
    y = E.y
    bounds = fold_bounds(E.t) if bounds is None else bounds
    n = E.n_nodes
    Xd = design(F, triad_blocks, "log")[0] if with_triad else np.zeros((m, 0))
    mu, sd = Xd[:bounds[0]].mean(0), Xd[:bounds[0]].std(0)
    sd = np.where(sd < 1e-12, 1.0, sd)
    Xd = (Xd - mu) / sd
    kd = Xd.shape[1]
    ar = np.arange(m)

    def build(rows):
        r = np.asarray(rows)
        S = sparse.csr_matrix((np.ones(len(r)), (np.arange(len(r)), E.u[r])), shape=(len(r), n))
        R = sparse.csr_matrix((np.ones(len(r)), (np.arange(len(r)), E.v[r])), shape=(len(r), n))
        return sparse.hstack([sparse.csr_matrix(np.ones((len(r), 1))), S, R, sparse.csr_matrix(Xd[r])], format="csr")

    def fit(rows, lam):
        X = build(rows)
        yy = y[rows]
        p0 = float(np.clip(yy.mean(), 1e-6, 1 - 1e-6))
        pen = np.zeros(X.shape[1])
        pen[1:1 + 2 * n] = lam
        pen[1 + 2 * n:] = 1e-2
        th0 = np.zeros(X.shape[1])
        th0[0] = math.log(p0 / (1 - p0))

        def fg(th):
            eta = X @ th
            f = np.sum(np.logaddexp(0.0, eta) - yy * eta) + 0.5 * np.sum(pen * th * th)
            g = X.T @ (special.expit(eta) - yy) + pen * th
            return f, g

        res = optimize.minimize(fg, th0, jac=True, method="L-BFGS-B", options={"maxiter": 400, "maxcor": 20})
        return res.x

    i_in = aligned_index(E.t, INNER_FRAC)
    best = None
    for lam in lam_grid:
        th = fit(ar[:i_in], lam)
        ll = logloss(y[i_in:bounds[0]], special.expit(build(ar[i_in:bounds[0]]) @ th))
        if best is None or ll < best[0]:
            best = (ll, lam)
    lam = best[1]
    pred = np.full(m, np.nan)
    thr = np.full(m, np.nan)
    fold_of = np.full(m, -1, np.int16)
    for j in range(len(bounds) - 1):
        a, lo, hi = bounds[j], bounds[j], bounds[j + 1]
        th = fit(ar[:a], lam)
        seen_u = np.zeros(n, bool)
        seen_v = np.zeros(n, bool)
        seen_u[E.u[:a]] = True
        seen_v[E.v[:a]] = True
        th = th.copy()
        th[1:1 + n][~seen_u] = 0.0         # unseen node: prior mean (0 is already the ridge solution; kept explicit)
        th[1 + n:1 + 2 * n][~seen_v] = 0.0
        pred[lo:hi] = special.expit(build(ar[lo:hi]) @ th)
        thr[lo:hi] = y[:a].mean()
        fold_of[lo:hi] = j
    nm = "frozen_effects" + ("+tri16" if with_triad else "")
    return SpecResult(nm, ("frozen",) + tuple(triad_blocks if with_triad else ()), f"ridge {lam:g}", 1 + 2 * n + kd,
                      pred, thr, fold_of, lam)


# --------------------------------------------------------------------------------------------------- the person-only null

def person_generator(E: EdgeSet, lam: float = 2.0, bin_unit: str = "quarter", min_n: int = 500) -> np.ndarray:
    """Linear predictor eta (per edge) of the person-only model fitted to every edge: a period intercept, one ridge-fitted
    effect per sender and one per receiver (the registry's a_i and b_j with nothing else).  Used as the data-generating
    process of the null 'signs come from person propensities alone' on the real network skeleton (who rates whom, when)."""
    n, m = E.n_nodes, E.m
    bins = make_bins(E, bin_unit, min_n)
    nb = int(bins.max()) + 1
    ar = np.arange(m)
    X = sparse.hstack([sparse.csr_matrix((np.ones(m), (ar, bins)), shape=(m, nb)),
                       sparse.csr_matrix((np.ones(m), (ar, E.u)), shape=(m, n)),
                       sparse.csr_matrix((np.ones(m), (ar, E.v)), shape=(m, n))], format="csr")
    pen = np.r_[np.full(nb, 1e-3), np.full(2 * n, lam)]
    y = E.y
    th0 = np.zeros(X.shape[1])
    th0[:nb] = math.log(np.clip(y.mean(), 1e-6, 1 - 1e-6) / (1 - np.clip(y.mean(), 1e-6, 1 - 1e-6)))

    def fg(th):
        eta = X @ th
        f = np.sum(np.logaddexp(0.0, eta) - y * eta) + 0.5 * np.sum(pen * th * th)
        return f, X.T @ (special.expit(eta) - y) + pen * th

    res = optimize.minimize(fg, th0, jac=True, method="L-BFGS-B", options={"maxiter": 500, "maxcor": 20})
    return X @ res.x


def calibrate_generator(E: EdgeSet, target_auc: float, grid=(0.03, 0.1, 0.3), seed: int = 11, log=None) -> dict:
    """Choose the ridge of the person generator so that the person-only model, run through the forward-chained pipeline on
    signs simulated from it, reaches the held-out AUC the real data gave it (`target_auc`).  A heavily shrunken generator
    makes a world with less person signal than the real one, in which the triad terms have more to add; matching the person
    AUC makes the null a fair one.  Linear interpolation of the simulated AUC in log(lambda) between the grid points."""
    pts = []
    for lam in grid:
        eta = person_generator(E, lam=lam)
        Es = simulate_signs(E, eta, None, seed=seed)
        Fc = compute_features(Es, "causal")
        r = run_spec(Es, Fc, "person", ("person",))
        idx = np.flatnonzero(test_window(r))
        auc = WeightedScorer(Es.y[idx], r.pred[idx]).auc()
        pts.append((math.log(lam), auc, eta, lam))
        if log:
            log(f"    generator lambda {lam:g}: simulated person AUC {auc:.4f} (target {target_auc:.4f})")
    xs = np.array([p[0] for p in pts])
    ys = np.array([p[1] for p in pts])
    if target_auc >= ys.max():
        k = int(np.argmax(ys))
        return dict(lam=pts[k][3], eta=pts[k][2], sim_auc=float(ys[k]), grid=[(p[3], p[1]) for p in pts])
    if target_auc <= ys.min():
        k = int(np.argmin(ys))
        return dict(lam=pts[k][3], eta=pts[k][2], sim_auc=float(ys[k]), grid=[(p[3], p[1]) for p in pts])
    order = np.argsort(ys)
    lx = float(np.interp(target_auc, ys[order], xs[order]))
    lam = math.exp(lx)
    eta = person_generator(E, lam=lam)
    return dict(lam=lam, eta=eta, sim_auc=float("nan"), grid=[(p[3], p[1]) for p in pts])


def simulate_signs(E: EdgeSet, eta: np.ndarray, coef: np.ndarray | None = None, seed: int = 0) -> EdgeSet:
    """Same skeleton (u, v, t, clusters), new signs.  coef = None or all zero: independent draws from sigmoid(eta) (the
    person-only null).  Otherwise the signs are drawn in time order from sigmoid(eta + coef . triad counts), the counts
    being those of the signs already drawn (strictly earlier edges), i.e. a planted triad mechanism of known size on top of
    the person terms."""
    rng = np.random.default_rng(seed)
    m = E.m
    if coef is None or not np.any(coef):
        s = np.where(rng.random(m) < special.expit(eta), 1, -1).astype(np.int8)
        return EdgeSet(E.name, E.u, E.v, s, E.t, E.cluster, E.n_nodes, dict(E.info))
    n = E.n_nodes
    U, V, T = E.u.tolist(), E.v.tolist(), E.t
    out = [dict() for _ in range(n)]
    inn = [dict() for _ in range(n)]
    nb = [set() for _ in range(n)]
    c = np.asarray(coef, float).tolist()
    draws = rng.random(m).tolist()
    eta_l = eta.tolist()
    s = np.zeros(m, np.int8)
    k = 0
    while k < m:
        j = k + 1
        while j < m and T[j] == T[k]:
            j += 1
        for q in range(k, j):
            u, v = U[q], V[q]
            ou, iu, ov, iv = out[u], inn[u], out[v], inn[v]
            z = eta_l[q]
            for w in nb[u] & nb[v]:
                a, b, cc, d = ou.get(w), iu.get(w), iv.get(w), ov.get(w)
                if a is not None:
                    if cc is not None:
                        z += c[(a < 0) * 2 + (cc < 0)]
                    if d is not None:
                        z += c[4 + (a < 0) * 2 + (d < 0)]
                if b is not None:
                    if cc is not None:
                        z += c[8 + (b < 0) * 2 + (cc < 0)]
                    if d is not None:
                        z += c[12 + (b < 0) * 2 + (d < 0)]
            s[q] = 1 if draws[q] < 1.0 / (1.0 + math.exp(-z)) else -1
        for q in range(k, j):
            u, v = U[q], V[q]
            out[u][v] = int(s[q])
            inn[v][u] = int(s[q])
            nb[u].add(v)
            nb[v].add(u)
        k = j
    return EdgeSet(E.name, E.u, E.v, s, E.t, E.cluster, E.n_nodes, dict(E.info))


def planted_coef(scale: float) -> np.ndarray:
    """A forward-chain mechanism of per-triad size `scale`: FFpp +, FFpm -, FFmp -, FFmm -, nothing on the other types."""
    c = np.zeros(16)
    c[TYPE_INDEX["FFpp"]] = +scale
    c[TYPE_INDEX["FFpm"]] = -scale
    c[TYPE_INDEX["FFmp"]] = -scale
    c[TYPE_INDEX["FFmm"]] = -scale
    return c


def replicate_statistics(E: EdgeSet, with_static: bool = True) -> dict:
    """What one replicate of the null battery records: the pooled held-out AUC of person / triad / both (D and G), and the
    four forward-chain coefficients of the triad-only and person-adjusted fits in the causal and static designs."""
    Fc = compute_features(E, "causal")
    res = run_specs(E, Fc, ["person", "tri16", "person+tri16"])
    idx = np.flatnonzero(test_window(res["person"]))
    y = E.y[idx]
    auc = {nm: WeightedScorer(y, r.pred[idx]).auc() for nm, r in res.items()}
    out = dict(auc=auc, D=auc["person"] - auc["tri16"], G=auc["person+tri16"] - auc["person"], coef={})
    hi = (Fc.emb >= 5)[idx]
    ys, a0 = y[hi], res["person"].pred[idx][hi]
    if ys.min() != ys.max():
        out["G_C5"] = WeightedScorer(ys, res["person+tri16"].pred[idx][hi]).auc() - WeightedScorer(ys, a0).auc()
    designs = [("causal", Fc)] + ([("static", compute_features(E, "static"))] if with_static else [])
    for label, F in designs:
        for blocks in (("tri16",), ("person", "tri16")):
            tab = coefficient_table(E, F, blocks=blocks)
            out["coef"][f"{label}:{'+'.join(blocks)}"] = {nm: tab["rows"][nm]["coef"] for nm in FORWARD}
    return out


# --------------------------------------------------------------------------------------------------- verdict rules

def r2_tier(G: dict) -> str:
    """R2 at one site from the paired difference G = AUC(person + triad) - AUC(person)."""
    if not np.isfinite(G["diff"]) or not np.isfinite(G["ci"][0]):
        return "none"
    if G["ci"][0] > 0 and G["diff"] >= RULE_G_MATERIAL:
        return "material"
    if G["ci"][0] > 0:
        return "small"
    return "none"


def r2_overall(tiers: list[str]) -> str:
    k = sum(1 for t in tiers if t == "material")
    if k >= 3:
        return "YES"
    if k <= 1:
        return "NO"
    return "MIXED"


def r5_both(one_way: str, two_way: str) -> str:
    """R5 as the verdict reads it: SUPPORTED or ABSENT only where the receiver-cluster and the two-way intervals agree, else
    UNDECIDED.  Review 2026-11-01: the verdict had required both rules for SUPPORTED but read ABSENT from the receiver-cluster
    rule alone, which called Bitcoin OTC absent although its two-way interval is [-0.14, +0.11]."""
    return one_way if one_way == two_way else "UNDECIDED"


# --------------------------------------------------------------------------------------------------- one site, everything

CACHE = DATA / "sign_registry_battery_cache"
BIN_CFG = {"wiki": ("year", 3000), "otc": ("year", 1000), "alpha": ("year", 1000), "bsky": ("month", 9000)}
T1_BLOCKS = [("tri16",), ("person_lite", "tri16"), ("degree7", "tri16"), ("person", "tri16"), ("person_flex", "tri16")]


def jsonable(x):
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    if isinstance(x, (list, tuple)):
        return [jsonable(v) for v in x]
    if isinstance(x, (np.floating, float)):
        return None if not np.isfinite(x) else float(x)
    if isinstance(x, (np.integer,)):
        return int(x)
    if isinstance(x, (np.bool_,)):
        return bool(x)
    if isinstance(x, np.ndarray):
        return jsonable(x.tolist())
    return x


def _null_worker(args):
    Er, with_static = args
    return replicate_statistics(Er, with_static)


def null_battery_parallel(E, eta, scale, R, seed, with_static=True, workers=1):
    coef = planted_coef(scale) if scale else None
    sims = [(simulate_signs(E, eta, coef, seed=seed * 1000 + r), with_static) for r in range(R)]
    if workers <= 1:
        reps = [_null_worker(a) for a in sims]
    else:
        from concurrent.futures import ProcessPoolExecutor
        with ProcessPoolExecutor(max_workers=workers) as ex:
            reps = list(ex.map(_null_worker, sims))
    return dict(scale=scale, R=R, reps=reps)


VARIANT_PAIRS = [
    ("person+bal_weak", "person+bal_strict"), ("bal_weak", "bal_strict"),
    ("person+bal_strict+status", "person+bal_strict"), ("person+bal_weak+status", "person+bal_weak"),
    ("person+status", "person"), ("person+tri16+status", "person+tri16"), ("person+tri16", "person+bal_weak"),
    ("person+tri16", "person+tri4"), ("person+tri4", "person+bal_weak"), ("person+recip", "person"),
    ("person+tri16+recip", "person+tri16"), ("person_flex", "person"),
    ("person_flex+tri16+interactions", "person_flex"), ("frozen_effects", "person"), ("tri16+status", "tri16"),
    ("tri16", "status"), ("person+bal_strict", "person"), ("person+bal_weak", "person"), ("person+tri16", "person"),
]


def compute_site(key: str, B: int = 300, R_null: int = 20, R_planted: int = 8, planted_scales=(0.1, 0.3),
                 seed: int = 20261101, workers: int = 1, log=print) -> dict:
    """Everything the report needs for one site; pure computation, no printing except progress through `log`."""
    t_start = time.time()

    def say(msg):
        log(f"[{key} {time.time() - t_start:6.0f}s] {msg}")

    E = load_site(key)
    src = SOURCES[key]
    unit, min_n = BIN_CFG[key]
    bins = make_bins(E, unit, min_n)
    labels = bin_names(E, bins, unit)
    data = dict(label=SITE_LABEL[key], edges=E.m, nodes=E.n_nodes, pos_share=float(E.y.mean()), info=E.info,
                t_lo=float(E.t.min()), t_hi=float(E.t.max()), n_clusters=int(len(np.unique(E.cluster))),
                distinct_times=int(len(np.unique(E.t))), source=dict(url=src.url, nbytes=src.nbytes, sha256=src.sha256,
                                                                      cite=src.cite, terms=src.terms),
                years={int(a): int(b) for a, b in zip(*np.unique(E.year, return_counts=True))},
                bins=[dict(name=labels[b], edges=int((bins == b).sum())) for b in range(len(labels))],
                bin_unit=unit)
    Fc = compute_features(E, "causal")
    Fs = compute_features(E, "static")
    data["emb_share"] = {lab: float(((Fc.emb >= lo) & (Fc.emb <= hi)).mean()) for lo, hi, lab in EMB_STRATA}
    data["emb_share_static"] = {lab: float(((Fs.emb >= lo) & (Fs.emb <= hi)).mean()) for lo, hi, lab in EMB_STRATA}
    say("features done")

    t1 = {}
    for mode, F in (("static", Fs), ("causal", Fc)):
        for blocks in T1_BLOCKS:
            t1[f"{mode}:{'+'.join(blocks)}"] = coefficient_table(E, F, blocks)
        for blocks in (("tri16",), ("person", "tri16")):
            t1[f"{mode}:C5:{'+'.join(blocks)}"] = coefficient_table(E, F, blocks, subset=F.emb >= 5)
    say("T1 done")

    names = list(VARIANTS)
    res = run_specs(E, Fc, names)
    say("T2 specs fitted")
    fz = {"frozen_effects": run_frozen_effects(E, Fc, False), "frozen_effects+tri16": run_frozen_effects(E, Fc, True)}
    say("T2 frozen effects fitted")
    all_res = {**res, **fz}
    summ = summarise_specs(E, Fc, all_res, B=B, seed=seed)
    summ_c5 = summarise_specs(E, Fc, all_res, B=B, seed=seed, mask=Fc.emb >= 5)
    D = paired_diff(E, res, "person", "tri16", B=B, seed=seed)
    G = paired_diff(E, res, "person+tri16", "person", B=B, seed=seed)
    Gc5 = paired_diff(E, res, "person+tri16", "person", mask=Fc.emb >= 5, B=B, seed=seed)
    Dc5 = paired_diff(E, res, "person", "tri16", mask=Fc.emb >= 5, B=B, seed=seed)
    D2 = paired_diff(E, res, "person", "tri16", B=B, seed=seed, twoway=True)
    G2 = paired_diff(E, res, "person+tri16", "person", B=B, seed=seed, twoway=True)
    Gc5_2 = paired_diff(E, res, "person+tri16", "person", mask=Fc.emb >= 5, B=B, seed=seed, twoway=True)
    Dc5_2 = paired_diff(E, res, "person", "tri16", mask=Fc.emb >= 5, B=B, seed=seed, twoway=True)
    strata = {}
    for lo, hi, lab in EMB_STRATA:
        mk = (Fc.emb >= lo) & (Fc.emb <= hi)
        strata[lab] = dict(D=paired_diff(E, res, "person", "tri16", mask=mk, B=B, seed=seed),
                           G=paired_diff(E, res, "person+tri16", "person", mask=mk, B=B, seed=seed))
    folds = []
    first = res["person"]
    for j in range(len(FOLD_FRACS) - 1):
        idx = np.flatnonzero(first.fold_of == j)
        yj = E.y[idx]
        row = dict(fold=j, n=int(len(idx)), t_lo=float(E.t[idx].min()), t_hi=float(E.t[idx].max()),
                   pos_share=float(yj.mean()))
        for nm in ("person", "tri16", "person+tri16"):
            row[nm] = auc_score(yj, res[nm].pred[idx])
        folds.append(row)
    t2 = dict(n_test=summ["n"], summary=summ, summary_c5=summ_c5, D=D, G=G, D_c5=Dc5, G_c5=Gc5, strata=strata,
              folds=folds, tier=r2_tier(G), tier_c5=r2_tier(Gc5), bounds=fold_bounds(E.t),
              frozen_lambda=fz["frozen_effects"].ridge, D2=D2, G2=G2, D_c5_2=Dc5_2, G_c5_2=Gc5_2,
              tier2=r2_tier(G2), tier_c5_2=r2_tier(Gc5_2))
    t2["pairs"] = {}
    for a_, b_ in VARIANT_PAIRS:
        if a_ in all_res and b_ in all_res:
            t2["pairs"][f"{a_} | {b_}"] = dict(
                auc=paired_diff(E, all_res, a_, b_, B=B, seed=seed),
                logloss=paired_diff(E, all_res, a_, b_, B=B, seed=seed, metric="logloss"),
                auc_c5=paired_diff(E, all_res, a_, b_, mask=Fc.emb >= 5, B=B, seed=seed))
    best = min(summ["models"], key=lambda k: summ["models"][k]["logloss"])
    t2["best_logloss"] = best
    t2["best_auc"] = max(summ["models"], key=lambda k: summ["models"][k]["auc"])
    say("T2 summarised")

    cv_names = ["degree7", "person", "tri16", "degree7+tri16", "person+tri16"]
    cv = static_cv(E, Fs, cv_names)
    masks = {"all": np.ones(E.m, bool), "C >= 5": Fs.emb >= 5, "C >= 25": Fs.emb >= 25}
    t2["static_cv"] = summarise_static(E, cv, "degree7", masks, B=min(B, 200), seed=seed)
    say("static CV done")

    t3 = {}
    for kind in ("snapshot", "history"):
        for person in (False, True):
            t3[f"{kind}:{'person' if person else 'triad-only'}"] = drift_by_bin(E, unit, min_n, kind, Fc, person)
    say("T3 done")

    t4 = symmetry_test(E, Fs, B=300, seed=seed)
    say("T4 done")

    t5 = dict(static=visibility_test(E, Fs, B=min(B, 300), seed=seed, bins=bins, bin_labels=labels),
              causal=visibility_test(E, Fc, B=min(B, 300), seed=seed, bins=bins, bin_labels=labels),
              static2=visibility_test(E, Fs, B=min(B, 300), seed=seed, bins=bins, bin_labels=labels, twoway=True),
              causal2=visibility_test(E, Fc, B=min(B, 300), seed=seed, bins=bins, bin_labels=labels, twoway=True))
    say("T5 done")

    null = {}
    if R_null:
        target = summ["models"]["person"]["auc"]
        cal = calibrate_generator(E, target, log=say)
        eta, lam = cal["eta"], cal["lam"]
        say(f"person generator calibrated (lambda {lam:.3g}, real person AUC {target:.4f})")
        null["generator_auc"] = auc_score(E.y, eta)
        null["lambda"] = lam
        null["target_person_auc"] = target
        null["calibration_grid"] = cal["grid"]
        null["person-only"] = null_battery_parallel(E, eta, 0.0, R_null, 1, workers=workers)
        say("null: person-only done")
        for sc in planted_scales:
            null[f"planted {sc}"] = null_battery_parallel(E, eta, sc, R_planted, 2, workers=workers)
            say(f"null: planted {sc} done")
    return jsonable(dict(key=key, data=data, t1=t1, t2=t2, t3=t3, t4=t4, t5=t5, null=null,
                         seconds=time.time() - t_start))


def cache_path(key: str) -> Path:
    return CACHE / f"{key}.json"


def run_and_cache(key: str, **kw) -> dict:
    import json
    CACHE.mkdir(parents=True, exist_ok=True)
    out = compute_site(key, **kw)
    cache_path(key).write_text(json.dumps(out))
    return out


def load_cached(key: str) -> dict | None:
    import json
    p = cache_path(key)
    return json.loads(p.read_text()) if p.exists() else None


def transfer_matrix(Es: dict, Fs: dict, blocks=("tri16",), min_emb: int = 5, ridge: float = 1e-3) -> dict:
    """Cross-site transfer of the fitted form (LHK's Table 6, L4830): the model fitted on every edge of site A (static
    features), scored on the edges of site B with embeddedness >= min_emb.  AUC and the accuracy-at-the-training-prevalence
    balanced accuracy of B's own fit are the diagonal."""
    keys = list(Es)
    X = {k: design(Fs[k], blocks, "raw")[0] for k in keys}
    out = {}
    fits = {k: fit_logit(X[k], Es[k].y, ridge) for k in keys}
    for a in keys:
        for b in keys:
            sel = Fs[b].emb >= min_emb
            p = fits[a].predict_proba(X[b][sel])
            y = Es[b].y[sel]
            out[(a, b)] = dict(auc=auc_score(y, p), n=int(sel.sum()),
                               ba=_ba_array_thr(y, p, np.full(len(y), Es[a].y.mean())))
    return out


# --------------------------------------------------------------------------------------------------- the report

def _f(x, d=3, plus=False):
    if x is None or (isinstance(x, float) and not np.isfinite(x)):
        return "n/a"
    return f"{x:+.{d}f}" if plus else f"{x:.{d}f}"


def _ci(ci, d=3, plus=True):
    if not ci or ci[0] is None or ci[1] is None:
        return "n/a"
    return f"[{_f(ci[0], d, plus)}, {_f(ci[1], d, plus)}]"


def _md(header, rows, align=None):
    align = align or ["---"] + ["---:"] * (len(header) - 1)
    out = ["| " + " | ".join(header) + " |", "| " + " | ".join(align) + " |"]
    out += ["| " + " | ".join(str(c) for c in r) + " |" for r in rows]
    return out


def _fin(x) -> bool:
    return x is not None and bool(np.isfinite(x))


def _pct(x, d=1):
    return "n/a" if x is None else f"{100 * x:.{d}f}%"


def _date(t):
    return str(np.datetime64(int(t), "s"))[:10]


def null_arrays(R: dict, scen: str) -> dict:
    reps = R["null"][scen]["reps"]
    out = dict(G=np.array([r["G"] for r in reps]), D=np.array([r["D"] for r in reps]),
               G5=np.array([r.get("G_C5", np.nan) for r in reps]),
               auc_person=np.array([r["auc"]["person"] for r in reps]),
               auc_tri=np.array([r["auc"]["tri16"] for r in reps]), coef={})
    for k in reps[0]["coef"]:
        out["coef"][k] = np.array([[r["coef"][k][nm] for nm in FORWARD] for r in reps])
    return out


def null_z(obs: float, arr: np.ndarray) -> tuple[float, float, float, float]:
    """(null mean, null sd, z, one-sided p that the null is at least as large as the observation)."""
    arr = arr[np.isfinite(arr)]
    mu, sd = float(arr.mean()), float(arr.std(ddof=1)) if len(arr) > 1 else float("nan")
    z = (obs - mu) / sd if sd and np.isfinite(sd) and sd > 0 else float("nan")
    p = (1 + int(np.sum(arr >= obs))) / (len(arr) + 1)
    return mu, sd, z, p


def write_report(path: Path, sites=SITE_ORDER) -> None:
    """Assemble sim/results/sign_registry_battery.md from the cached per-site statistics (and, for the transfer matrix,
    the data themselves).  The verdict text is written by `verdict_text`, whose sentences are guarded by assertions on the
    numbers they quote, so a rerun on changed data fails rather than misstates."""
    Rs = {k: load_cached(k) for k in sites}
    missing = [k for k, v in Rs.items() if v is None]
    if missing:
        raise SystemExit(f"cached statistics missing for {missing}: run `compute SITE` first")
    L = []
    L += _report_head(Rs)
    L += verdict_text(Rs)
    L += _sec_data(Rs)
    L += _sec_method(Rs)
    L += _sec_t1(Rs)
    L += _sec_t2(Rs)
    L += _sec_t3(Rs)
    L += _sec_t4(Rs)
    L += _sec_t5(Rs)
    L += _sec_variations(Rs)
    L += _sec_null(Rs)
    L += _sec_caveats(Rs)
    L += _sec_reproduce(Rs)
    tail = ""
    if Path(path).exists():               # a review appended by hand ("## Review (date)") survives a regeneration
        old = Path(path).read_text()
        i = old.find("\n## Review (")
        tail = old[i:] if i >= 0 else ""
    Path(path).write_text("\n".join(L) + "\n" + tail)


def _report_head(Rs):
    return [
        "# Sign-law registry battery: the five tests of 112 section 6.5 on wiki-RfA, Bitcoin OTC and Alpha, and BlueTempNet",
        "",
        f"_Generated {time.strftime('%Y-%m-%d')} by `cd sim && ~/.local/bin/uv run python -m models.sign_registry_battery "
        "report` from statistics cached by `compute SITE` (seeded, 20261101). Code: `sim/models/sign_registry_battery.py`; "
        "checks: `sim/tests/test_sign_registry_battery.py`. Ledger ids: L5421 (the R-E form), L4811 and L4833 (forward "
        "chains), L4826-L4830 and L4850-L4852 (LHK's accuracies, person terms, visibility), L4812 (symmetry), L4857-L4859 "
        "(unrefreshed magnitudes, validity record), L4561-L4564 (wiki-RfA), L4567-L4580 (Bitcoin), L4593-L4598 "
        "(BlueTempNet). Results are computed statistics only; the data are local-use-only and are not redistributed "
        "(`sim/data/README.md`)._",
        "",
    ]


def _sec_data(Rs):
    L = ["## 1. Data and terms", ""]
    rows = []
    for k, R in Rs.items():
        d, src = R["data"], R["data"]["source"]
        rows.append([SITE_LABEL[k], f"{src['nbytes']:,}", f"`{src['sha256'][:12]}`", f"{d['edges']:,}", f"{d['nodes']:,}",
                     _pct(d["pos_share"]), f"{_date(d['t_lo'])} to {_date(d['t_hi'])}", f"{d['distinct_times']:,}",
                     f"{d['n_clusters']:,}"])
    L += _md(["site", "file bytes", "sha256", "edges used", "nodes", "positive", "period", "distinct times", "clusters"], rows)
    L += ["", "Clusters are the units resampled by the bootstrap and used by the robust standard errors: elections for "
          "wiki-RfA, receivers elsewhere.", ""]
    for k, R in Rs.items():
        src = R["data"]["source"]
        L.append(f"- **{SITE_LABEL[k]}.** {src['cite']}. Fetched from `{src['url']}`. Terms: {src['terms']}.")
    w = Rs.get("wiki")
    if w:
        i = w["data"]["info"]
        L += ["", f"wiki-RfA filters: {i['n_records']:,} records; {i['n_named_nonneutral']:,} with a named voter, a non-neutral vote "
              f"and not a self-vote; {i['n_dated']:,} of those dated; the first dated vote of each ordered pair is the edge "
              f"({i['n_pairs']:,} edges in {i['n_elections']:,} elections). Neutral votes, empty-voter records, self-votes "
              "and undated votes are dropped; repeat votes by a pair are the other agent's conversion test, not used here."]
    b = Rs.get("bsky")
    if b:
        L += ["", f"BlueTempNet: the feed-creator graph (`graph_dimension1`), {b['data']['info']['n_rows']:,} signed records, of "
              f"which {b['data']['info']['n_rows'] - b['data']['edges']} self-loops are dropped. The feed-member graph "
              "(1.15 GB, 4.9 million follows) was not used. A follow is interest and a block is partly a safety tool (117 section 3.6); "
              "where a pair had both, the release keeps the block [L4595]."]
    L += ["", "Embeddedness C(u,v) (common neighbours, direction ignored) of the edges, as the share of all edges, under the causal "
          "rule (earlier edges only) and the static rule (every other edge):", ""]
    rows = []
    for k, R in Rs.items():
        d = R["data"]
        rows.append([SITE_LABEL[k]] + [f"{_pct(d['emb_share'][lab], 0)} / {_pct(d['emb_share_static'][lab], 0)}"
                                       for _, _, lab in EMB_STRATA])
    L += _md(["site"] + [lab for _, _, lab in EMB_STRATA], rows)
    L.append("")
    return L


def two_way_changes(Rs) -> str:
    """Every threshold verdict (R1 letters of the forward chains, R2 tiers, R3 flips, R5) that differs between the receiver-cluster
    rule and the two-way rule, as a sentence."""
    ch = []
    for k, R in Rs.items():
        for fit in ("static:tri16", "static:person+tri16", "causal:tri16", "causal:person+tri16"):
            for nm in FORWARD:
                r = R["t1"][fit]["rows"][nm]
                if r["status"] != r["status2"]:
                    ch.append(f"{SITE_LABEL[k]} {fit.replace(':', ' ')} {nm} {r['status']} to {r['status2']}")
        t = R["t2"]
        for a, b, what in (("tier", "tier2", "R2 tier"), ("tier_c5", "tier_c5_2", "R2 tier at C >= 5")):
            if t[a] != t[b]:
                ch.append(f"{SITE_LABEL[k]} {what} {t[a]} to {t[b]}")
        if R["t5"]["static"]["verdict"] != R["t5"]["static2"]["verdict"]:
            ch.append(f"{SITE_LABEL[k]} R5 (static) {R['t5']['static']['verdict']} to {R['t5']['static2']['verdict']}")
        for key, v in R["t3"].items():
            if v["verdict"]["refuted"] != v["verdict"]["refuted2"]:
                ch.append(f"{SITE_LABEL[k]} R3 {key} {v['verdict']['refuted']} to {v['verdict']['refuted2']}")
    return "; ".join(ch) + "." if ch else "none."


def _sec_method(Rs):
    return [
        "## 2. Method",
        "",
        "**Objects.** An edge is an ordered pair (u, v) with a sign, a time and a cluster. The 16 triad types are LHK's "
        "[F|B][F|B][p|m][p|m] [L4814]: for a common neighbour w of u and v, F if the u-w edge points u to w (B if w to u), F if "
        "the w-v edge points w to v (B if v to w), then the two signs. FFpp, FFpm, FFmp, FFmm are the forward chains. "
        "**Person terms** are the sender's earlier outgoing signs and the receiver's earlier incoming signs, as counts and "
        "shrunken log-odds (eight columns, deliberately generous; the empirical a_i and b_j of R-E). A second reading, a_i and "
        "b_j as ridge-fitted effects frozen at the end of each training window, is a variation.",
        "",
        "**Two evidence rules.** *Static* (LHK's): every other edge of the snapshot is the evidence for an edge. *Causal*: only "
        "edges with a strictly earlier time are (edges at the same instant are invisible to one another). T2 uses only the "
        "causal rule; T1 and T3 report both.",
        "",
        "**T2 protocol.** Edges are sorted by time; four forward-chained folds: train on the first 40% of edges and test on "
        "the next 15%, then train on 55% and test on the next 15%, and so on to 100% (60% of the edges are tested once). "
        "Logistic regression, ridge 1 on standardised columns, refit on every edge before each test block; the choice of raw "
        "or log counts is made once on an inner validation block (30% to 40%) and then held fixed. Metrics are pooled over "
        "the test blocks: AUC (primary), balanced accuracy at the training prevalence, log-loss. Intervals are 95% "
        "percentile intervals of a cluster bootstrap that resamples the same clusters for every model, so differences are "
        "paired; the clusters are elections (wiki-RfA) or receivers, as pre-registered, and a second, two-way interval "
        "resamples receivers and senders independently (the pigeonhole bootstrap), because the sign is strongly clustered "
        f"by sender as well (ICC of the sign across senders up to "
        f"{max(b['icc_send'] for R in Rs.values() for b in R['t3']['snapshot:triad-only']['bins']):.2f}, section 5). The z-values of the "
        "coefficients likewise come in a receiver-cluster and a two-way (Cameron-Gelbach-Miller) version.",
        "",
        "**Pre-registered decision rules** (constants in the module, pinned by a test, fixed before any result): "
        f"R1 a forward-chain coefficient is SUPPORTED if sigma z > 1.96, CONTRADICTED if sigma z < -1.96, with at least "
        f"{RULE_MIN_SUPPORT} edges carrying a triad of the type; the registry is refuted at a site if FFmm is CONTRADICTED. "
        f"R2 triad terms add a mechanism beyond person terms at a site if G = AUC(person + triad) - AUC(person) is at least "
        f"{RULE_G_MATERIAL} with its interval above 0 ('small' if only the interval is above 0); YES overall if material at "
        f"three or more of four sites, NO at one or none. R3 the pattern flips with date if a type is CONTRADICTED in at least "
        f"{RULE_FLIP_BINS} date bins; intercepts 'move' if Q has p < 0.001 and the range is at least {RULE_INTERCEPT_RANGE} "
        f"logit. R4 opposite signs are 'rare' at {RULE_RARE:.0%} or less of reciprocated pairs. R5 visibility is SUPPORTED if "
        f"the lower bound of BA(InSign) - BA(OutSign) at C = 0 exceeds {RULE_GAP}.",
        "",
        "**What was and was not fixed in advance, stated plainly.** The numerical rules above were written before any result "
        "existed. R1 and R3 did not say whether the person terms are in the fit; a first look at T1 showed that the two readings "
        "diverge sharply, so both are reported side by side and every verdict says which it is for (nothing was dropped). "
        "The one-way clustering of the rules ignored the sender effect, so the two-way version was added beside it; where it "
        "changes a verdict that depends on a threshold the change is: " + two_way_changes(Rs) + " "
        "The person-only generative null (section 9) was added after the first T2 pass showed G small, to interpret G; its "
        "first version (heavily shrunken person effects) produced a world with far less person signal than the real data "
        "and was replaced by one whose ridge is tuned so that the person-only model reaches the real data's held-out AUC. A "
        "before/after comparison of vote windows was run once on wiki-RfA during development (the k votes after a vote predicted "
        "it slightly better than the k before, by 0.2 to 1.9 balanced-accuracy points, k = 1 to 10) and a position gradient was "
        "never run; both were meant to separate visibility from candidate quality and were dropped because neither identifies "
        "it (in a stationary process the two directions of time are statistically indistinguishable, and a gradient has other "
        "causes, such as nominators voting first).",
        "",
    ]


_STAT_LETTER = {"SUPPORTED": "S", "CONTRADICTED": "C", "UNDECIDED": "u"}


def _cell(row):
    """coefficient (z with receiver clusters / z with receiver-and-sender clusters) and the two R1 letters"""
    zs = lambda v: "n/a" if v is None else f"{v:+.1f}"
    c = "n/a" if row.get("coef") is None else f"{row['coef']:+.3f}"
    if "status2" in row:
        return f"{c} ({zs(row.get('z'))}/{zs(row.get('z2'))}) {_STAT_LETTER[row['status']]}/{_STAT_LETTER[row['status2']]}"
    return f"{c} ({zs(row.get('z'))}) {_STAT_LETTER[row['status']]}"


def _sec_t1(Rs):
    L = ["## 3. T1: form transfer, the 16-type model per site", "",
         "Forward-chain coefficients of the logistic fit of the sign on the 16 raw triad counts (as LHK), by evidence rule and "
         "with or without the person terms in the fit. Cell: coefficient per triad, then z with clusters = receivers "
         "(elections for wiki-RfA), the pre-registered rule, and z with receiver-and-sender clusters (two-way), then the R1 "
         "letter under each (S supported, C contradicted, u undecided; at least 100 supporting edges). Predicted: FFpp +, "
         "FFpm -, FFmp -, FFmm -. 'Transfers' = FFmm supported and no forward chain contradicted; 'refuted' = FFmm "
         "contradicted. Senders are strongly clustered (section 5, ICC), so the two-way z is the more careful one; where "
         "the two disagree both are shown.", ""]
    rows = []
    for k, R in Rs.items():
        for mode in ("static", "causal"):
            for blocks, lab in (("tri16", "16 types alone"), ("person+tri16", "16 types + person terms")):
                t = R["t1"][f"{mode}:{blocks}"]
                v = t["verdict"]
                rows.append([SITE_LABEL[k], mode, lab] + [_cell(t["rows"][n]) for n in FORWARD] +
                            [("yes" if v["form_transfers"] else "no") + " / " + ("yes" if v["form_transfers2"] else "no"),
                             ("YES" if v["refuted"] else "no") + " / " + ("YES" if v["refuted2"] else "no")])
    L += _md(["site", "evidence", "fit"] + list(FORWARD) + ["transfers (1-way / 2-way)", "refuted (1-way / 2-way)"], rows,
             ["---", "---", "---", "---:", "---:", "---:", "---:", "---", "---"])
    L += ["", "Support (edges carrying at least one triad of the type), static design:", ""]
    rows = []
    for k, R in Rs.items():
        t = R["t1"]["static:tri16"]
        rows.append([SITE_LABEL[k], f"{t['n']:,}"] + [f"{t['rows'][n]['support']:,}" for n in FORWARD])
    L += _md(["site", "edges"] + list(FORWARD), rows)

    L += ["", "### 3.1 All 16 types, static design, with the sign each theory predicts", "",
          "Learned coefficient (z) of the 16-type fit alone, then with person terms. Theory signs: B strict balance, W weak "
          "balance (0 = no prediction), S status [L4800, L4801, L4815]. In LHK's Table 2 (L4836) balance agreed with the learned "
          "signs on 13, 12 and 9 of 16 types at Epinions, Slashdot and Wikipedia and status on 5, 6 and 6 of its 8.", ""]
    ts = theory_signs()
    for fit, lab in (("static:tri16", "16 types alone"), ("static:person+tri16", "16 types + person terms")):
        rows = []
        for n in TYPES:
            plus = sum(1 for R in Rs.values() if R["t1"][fit]["rows"][n]["support"] >= RULE_MIN_SUPPORT
                       and R["t1"][fit]["rows"][n]["z2"] > Z95)
            minus = sum(1 for R in Rs.values() if R["t1"][fit]["rows"][n]["support"] >= RULE_MIN_SUPPORT
                        and R["t1"][fit]["rows"][n]["z2"] < -Z95)
            rows.append([n, f"{ts['balance'][n]:+d} / {ts['weak'][n]:+d} / {ts['status'][n]:+d}"] +
                        [f"{R['t1'][fit]['rows'][n]['coef']:+.3f} ({R['t1'][fit]['rows'][n]['z']:+.1f})" for R in Rs.values()] +
                        [f"{plus}+ {minus}-"])
        L += [f"*{lab}* (z with receiver clusters; the last column counts sites where the two-way z is beyond 1.96 with "
              "support >= 100)", ""]
        L += _md(["type", "B / W / S"] + [SITE_LABEL[k] for k in Rs] + ["sites sig."], rows,
                 ["---", "---:"] + ["---:"] * (len(Rs) + 1))
        ag = []
        for k, R in Rs.items():
            a = R["t1"][fit]["agree"]
            ag.append(f"{SITE_LABEL[k]}: balance {a['balance']['n_agree']}/{a['balance']['n_significant']}, weak "
                      f"{a['weak']['n_agree']}/{a['weak']['n_significant']}, status {a['status']['n_agree']}/"
                      f"{a['status']['n_significant']}")
        L += ["", "Agreement of significant coefficients (|z| > 1.96, support >= 100) with each theory: " + "; ".join(ag) + ".", ""]

    L += ["### 3.2 How the forward chain depends on what is controlled (static design)", "",
          "The same four coefficients as the person controls get stronger: none; two columns (shrunken sender and receiver "
          "log-odds); LHK's seven degree features [L4813]; the eight-column person block; the same with squares and products "
          "(14 columns).", ""]
    rows = []
    for k, R in Rs.items():
        for blocks, lab in (("tri16", "none"), ("person_lite+tri16", "2 columns"), ("degree7+tri16", "LHK degree7"),
                            ("person+tri16", "person (8)"), ("person_flex+tri16", "person (14)")):
            t = R["t1"][f"static:{blocks}"]
            rows.append([SITE_LABEL[k], lab] + [_cell(t["rows"][n]) for n in FORWARD])
    L += _md(["site", "controls"] + list(FORWARD), rows, ["---", "---", "---:", "---:", "---:", "---:"])

    L += ["", "### 3.3 Where triad evidence exists: edges with C >= 5 (static design)", ""]
    rows = []
    for k, R in Rs.items():
        for blocks, lab in (("tri16", "16 types alone"), ("person+tri16", "16 types + person terms")):
            t = R["t1"][f"static:C5:{blocks}"]
            rows.append([SITE_LABEL[k], f"{t['n']:,}", lab] + [_cell(t["rows"][n]) for n in FORWARD])
    L += _md(["site", "edges", "fit"] + list(FORWARD), rows, ["---", "---:", "---", "---:", "---:", "---:", "---:"])

    L += ["", "### 3.4 Cross-site transfer of the fitted form", ""]
    try:
        Es = {k: load_site(k) for k in Rs}
        Fs = {k: compute_features(Es[k], "static") for k in Rs}
        L += ["AUC at C >= 5 of the model fitted on every edge of the row site (static evidence) and scored on the column "
              "site's edges (LHK's Table 6 analogue, L4830: 0.925 to 0.935 on Epinions and Slashdot and 0.772 to 0.802 on "
              "Wikipedia at C >= 25, whichever site trained it). The diagonal is a fit scored in-sample.", ""]
        for blocks, lab in ((("tri16",), "16 types alone"), (("person", "tri16"), "16 types + person terms")):
            tm = transfer_matrix(Es, Fs, blocks, 5)
            rows = [[SITE_LABEL[a]] + [f"{tm[(a, b)]['auc']:.3f}" for b in Rs] for a in Rs]
            L += [f"*{lab}*", ""]
            L += _md(["trained on"] + [f"scored on {SITE_LABEL[b]}" for b in Rs], rows)
            L.append("")
    except Exception as e:      # data absent: say so rather than fail the report
        L += [f"(not computed: {type(e).__name__}: {e})", ""]
    return L


def _sec_t2(Rs):
    L = ["## 4. T2: person terms against triad terms, held out in time", "",
         "Forward-chained, causal features, pooled over the four test blocks (60% of the edges, the latest in time). "
         "'person' = the eight person columns; 'triad' = the 16 triad counts alone; 'both' = person + triad. "
         "D = AUC(person) - AUC(triad) (the registry predicts D > 0); G = AUC(both) - AUC(person) (what the triad terms add "
         "beyond person terms; R2 calls it material at 0.02). 95% cluster-bootstrap intervals in brackets.", ""]
    rows = []
    for k, R in Rs.items():
        m = R["t2"]["summary"]["models"]
        for nm in ("person", "tri16", "person+tri16"):
            d = m[nm]
            rows.append([SITE_LABEL[k], {"person": "person", "tri16": "triad", "person+tri16": "both"}[nm],
                         f"{d['auc']:.4f} {_ci(d['auc_ci'], 4, False)}", f"{d['ba']:.4f}", f"{d['logloss']:.4f}",
                         d["n_params"], d["transform"]])
    L += _md(["site", "model", "AUC", "balanced acc.", "log-loss", "params", "counts"], rows,
             ["---", "---", "---:", "---:", "---:", "---:", "---"])
    L += ["", "Differences (paired). Intervals: first with clusters = receivers (elections for wiki-RfA), the pre-registered "
          "choice; second two-way (receivers and senders resampled independently, the pigeonhole bootstrap), which respects "
          "the strong sender effect.", ""]
    rows = []
    for k, R in Rs.items():
        t = R["t2"]
        g, d, g5 = t["G"], t["D"], t["G_c5"]
        rows.append([SITE_LABEL[k], f"{t['n_test']:,}", f"{d['diff']:+.4f} {_ci(d['ci'], 4)} / {_ci(t['D2']['ci'], 4)}",
                     f"{g['diff']:+.4f} {_ci(g['ci'], 4)} / {_ci(t['G2']['ci'], 4)}", f"{t['tier']} / {t['tier2']}",
                     f"{g5['n']:,}", f"{g5['diff']:+.4f} {_ci(g5['ci'], 4)} / {_ci(t['G_c5_2']['ci'], 4)}",
                     f"{t['tier_c5']} / {t['tier_c5_2']}"])
    L += _md(["site", "test edges", "D person - triad", "G both - person", "R2 tier (1-way / 2-way)", "edges C >= 5",
              "G, C >= 5", "tier, C >= 5"], rows)
    tiers = [R["t2"]["tier"] for R in Rs.values()]
    tiers2 = [R["t2"]["tier2"] for R in Rs.values()]
    L += ["", f"R2 across the sites run ({len(tiers)}): material at {sum(t == 'material' for t in tiers)}, small at "
          f"{sum(t == 'small' for t in tiers)}, none at {sum(t == 'none' for t in tiers)} -> **{r2_overall(tiers)}** (YES needs "
          f"three of four); with two-way intervals: material at {sum(t == 'material' for t in tiers2)}, small at "
          f"{sum(t == 'small' for t in tiers2)}, none at {sum(t == 'none' for t in tiers2)} -> **{r2_overall(tiers2)}**.", ""]

    L += ["### 4.1 By embeddedness of the edge", "",
          "Triad terms can only help where there is triad evidence; D and G inside strata of C (causal).", ""]
    rows = []
    for k, R in Rs.items():
        for lab in [x[2] for x in EMB_STRATA]:
            s = R["t2"]["strata"][lab]
            rows.append([SITE_LABEL[k], lab, f"{s['G']['n']:,}", f"{s['D']['diff']:+.4f}" if _fin(s["D"]["diff"]) else "n/a",
                         f"{s['G']['diff']:+.4f} {_ci(s['G']['ci'], 4)}" if _fin(s["G"]["diff"]) else "n/a"])
    L += _md(["site", "stratum", "edges", "D", "G"], rows)

    L += ["", "### 4.2 By test block", "",
          "AUC in each forward-chained block (person / triad / both), the period of the block and its positive share.", ""]
    rows = []
    for k, R in Rs.items():
        for f in R["t2"]["folds"]:
            rows.append([SITE_LABEL[k], f["fold"] + 1, f"{_date(f['t_lo'])} to {_date(f['t_hi'])}", f"{f['n']:,}", _pct(f["pos_share"]),
                         f"{f['person']:.3f}", f"{f['tri16']:.3f}", f"{f['person+tri16']:.3f}", f"{f['person+tri16'] - f['person']:+.3f}"])
    L += _md(["site", "block", "period", "edges", "positive", "person", "triad", "both", "G"], rows,
             ["---", "---:", "---", "---:", "---:", "---:", "---:", "---:", "---:"])

    L += ["", "### 4.3 Against LHK's own protocol (static evidence, random folds)", "",
          "Five random folds, every other edge of the snapshot as evidence, as in LHK (10 folds there). 'degree7' is LHK's seven "
          "degree features; they found the triad types added 2 to 6 points of accuracy over them [L4829] and the degree "
          "features alone about 0.886 at C >= 25 on Epinions [L4828].", ""]
    rows = []
    for k, R in Rs.items():
        cv = R["t2"]["static_cv"]
        for lab in ("all", "C >= 5", "C >= 25"):
            if lab not in cv:
                continue
            r = cv[lab]["rows"]
            rows.append([SITE_LABEL[k], lab, f"{cv[lab]['n']:,}", f"{r['degree7']['auc']:.3f}", f"{r['person']['auc']:.3f}",
                         f"{r['tri16']['auc']:.3f}", f"{r['degree7+tri16']['auc']:.3f}",
                         f"{r['degree7+tri16']['d_auc']:+.3f} {_ci(r['degree7+tri16']['d_ci'], 3)}",
                         f"{r['person+tri16']['auc'] - r['person']['auc']:+.3f}"])
    L += _md(["site", "edges", "n", "degree7", "person", "triad", "degree7 + triad", "gain over degree7", "gain over person"], rows,
             ["---", "---", "---:", "---:", "---:", "---:", "---:", "---:", "---:"])
    big = [f"{SITE_LABEL[k]} at {lab_}" for k, R in Rs.items() for lab_, v in R["t2"]["static_cv"].items()
           if v["rows"]["degree7+tri16"]["d_auc"] >= 0.02]
    more = []
    for k, R in Rs.items():
        a_ = R["t2"]["static_cv"]["all"]["rows"]
        sg = a_["person+tri16"]["auc"] - a_["person"]["auc"]
        if sg - R["t2"]["G"]["diff"] > 0.002:
            more.append(f"{SITE_LABEL[k]} ({sg:+.3f} against {R['t2']['G']['diff']:+.3f})")
    big0 = [f"{SITE_LABEL[k]} at {lab_}" for k, R in Rs.items() for lab_, v in R["t2"]["static_cv"].items()
            if v["rows"]["degree7+tri16"]["d_auc"] >= 0.02 and v["rows"]["degree7+tri16"]["d_ci"][0] <= 0]
    L += ["", "LHK's 2 to 6 points over the degree features (points of balanced accuracy on balanced sets, read from a figure "
          "[L4829]; the gains here are AUC, so the comparison is loose) are reached here (point estimates"
          + (f"; the interval includes 0 at {', '.join(big0)}" if big0 else "") + ") at " + (", ".join(big) if big else "no site")
          + "; elsewhere the triad types add less. On all edges the static protocol gives the triad terms more than the time-split "
          "protocol does at " + (", ".join(more) if more else "no site") + " (gain over person terms against G), as expected if "
          "static evidence includes edges that came after the one being predicted.", ""]
    return L


def _sec_t3(Rs):
    L = ["## 5. T3: drift by date", "",
         "Each date bin is refitted separately: the bin's own edges form the snapshot (static evidence inside the bin), "
         "16 types alone. Bins are calendar years (months for BlueTempNet) merged until each has enough edges (3,000 for wiki-RfA, "
         "1,000 for Bitcoin, 9,000 for BlueTempNet). Cell: coefficient "
         "(z) and R1 letter. 'Q p' is Cochran's test that the per-bin estimates are equal; I^2 the share of their variance that "
         "is heterogeneity. ICC is the between-user share of the variance of the sign, for senders and for receivers.", ""]
    for k, R in Rs.items():
        d = R["t3"]["snapshot:triad-only"]
        rows = []
        for b in d["bins"]:
            rows.append([b["name"], f"{b['edges']:,}", _pct(b["pos_share"]), f"{b['intercept']:+.2f}"] +
                        [_cell(b["rows"][n]) for n in FORWARD] + [f"{b['icc_send']:.2f}", f"{b['icc_recv']:.2f}"])
        L += [f"**{SITE_LABEL[k]}**", ""]
        L += _md(["bin", "edges", "positive", "intercept"] + list(FORWARD) + ["ICC send", "ICC recv"], rows,
                 ["---", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---:"])
        het = d["het"]
        L += ["", "Heterogeneity across bins (Q p / I^2): " + "; ".join(
            f"{n} {het[n]['p']:.2g} / {het[n]['I2']:.2f}" for n in list(FORWARD) + ["intercept"]) + ".", ""]
    L += ["### 5.1 R3 verdicts", "",
          "Bins in which a forward-chain type is CONTRADICTED (R1 rule, per bin), for the four readings: snapshot or cumulative "
          "history evidence, 16 types alone or with person terms. R3 calls the pattern flipped when a type is contradicted in "
          f"at least {RULE_FLIP_BINS} bins.", ""]
    rows = []
    for k, R in Rs.items():
        for key in ("snapshot:triad-only", "history:triad-only", "snapshot:person", "history:person"):
            v = R["t3"][key]["verdict"]
            rows.append([SITE_LABEL[k], key.replace(":person", ":+person"), len(R["t3"][key]["bins"]),
                         ", ".join(f"{n[2:]} {v['flips'][n]}/{v['flips2'][n]}" for n in FORWARD),
                         ", ".join(f"{n[2:]} {v['supported'][n]}/{v['supported2'][n]} of {v['adequate'][n]}" for n in FORWARD),
                         ("FLIPPED " + "/".join(v["flipped_types"]) if v["refuted"] else "stable") + " ; " +
                         ("FLIPPED " + "/".join(v["flipped_types2"]) if v["refuted2"] else "stable"),
                         f"{'yes' if v['intercepts_move'] else 'no'} (range {v['intercept_range']:.2f})"])
    L += _md(["site", "reading", "bins", "contradicted bins, 1-way/2-way (pp pm mp mm)", "supported bins, 1-way/2-way of adequate",
              "R3, 1-way ; 2-way", "intercepts move"], rows,
             ["---", "---", "---:", "---", "---", "---", "---"])
    L.append("")
    return L


def _sec_t4(Rs):
    L = ["## 6. T4: symmetry", "",
         "A reciprocated pair has a tie in each direction. Opposite-sign share with a Wilson interval; the null of independent "
         "signs at the observed marginals (2p(1-p), p the positive share inside reciprocated pairs); the person-propensity null "
         "(the expected opposite share if each tie were drawn from the sender-and-receiver model fitted on all ties); the "
         "correlation of the two ties' residuals from that model (positive = concordant beyond person terms). 'Reply' is the "
         "probability that the later tie of a pair is positive given the sign of the earlier one. R4 'rare' = at most 10%.", ""]
    rows = []
    for k, R in Rs.items():
        t = R["t4"]
        rp = t["reply"]
        rows.append([SITE_LABEL[k], f"{t['n_pairs']:,} ({_pct(t['share_pairs'], 0)} of ties)", f"{_pct(t['share'])} {_ci([100 * t['ci'][0], 100 * t['ci'][1]], 1, False)}%",
                     _pct(t["null_independent"]), _pct(t["null_person"]), f"{t['resid_corr']:+.2f} {_ci(t['resid_corr_ci'], 2)}",
                     f"{_pct(rp['after +']['p_pos'])} (n {rp['after +']['n']:,})", f"{_pct(rp['after -']['p_pos'])} (n {rp['after -']['n']:,})",
                     "rare" if t["rare"] else "NOT rare"])
    L += _md(["site", "reciprocated pairs", "opposite signs", "null: independent", "null: person", "residual corr.", "reply + after +",
              "reply + after -", "R4"], rows, ["---", "---", "---:", "---:", "---:", "---:", "---:", "---:", "---"])
    L += ["", "Opposite-sign share by the year of the pair's later tie:", ""]
    years = sorted({int(y) for R in Rs.values() for y in R["t4"]["by_year"]})
    rows = []
    for k, R in Rs.items():
        by = R["t4"]["by_year"]
        rows.append([SITE_LABEL[k]] + [(f"{_pct(by[str(y)]['share'])} (n {by[str(y)]['n']})" if str(y) in by else "") for y in years])
    L += _md(["site"] + [str(y) for y in years], rows)
    L.append("")
    return L


def _sec_t5(Rs):
    L = ["## 7. T5: visibility", "",
         "Balanced accuracy of InSign (predict + iff the target's other incoming ties are at least as often + as -) and OutSign "
         "(the same for the sender's other outgoing ties) [L4802], and their gap, by embeddedness; 95% cluster-bootstrap "
         "intervals. LHK's Wikipedia figures at C >= 0: InSign 0.706, OutSign 0.576; at C >= 25: 0.578 and 0.572 [L4851, L4852]. "
         "R5: SUPPORTED if the lower bound of the gap at C = 0 exceeds 0.02. The data cannot say whether a received-majority "
         "advantage is candidate quality, shared information or visibility of earlier votes [L4852].", ""]
    rows = []
    for k, R in Rs.items():
        for mode in ("static", "causal"):
            t = R["t5"][mode]
            t2w = R["t5"][mode + "2"]
            for lab in ["all"] + [x[2] for x in EMB_STRATA]:
                g = t["all"] if lab == "all" else t["strata"][lab]
                g2 = t2w["all"] if lab == "all" else t2w["strata"][lab]
                if g is None:
                    continue
                rows.append([SITE_LABEL[k], mode, lab, f"{g['n']:,}", f"{g['ba_in']:.3f}", f"{g['ba_out']:.3f}",
                             f"{g['gap']:+.3f} {_ci(g['gap_ci'], 3)} / {_ci(g2['gap_ci'], 3) if g2 else 'n/a'}",
                             f"{t['verdict']} / {t2w['verdict']}" if lab == "C = 0" else ""])
    L += _md(["site", "evidence", "stratum", "edges", "InSign", "OutSign", "gap (interval 1-way / 2-way)", "R5 at C = 0 (1-way / 2-way)"],
             rows, ["---", "---", "---", "---:", "---:", "---:", "---:", "---"])
    L += ["", "Does the gap move with the date? Gap at C = 0 by date bin (static evidence):", ""]
    labs = []
    for R in Rs.values():
        labs.append([b["name"] for b in R["data"]["bins"]])
    for k, R in Rs.items():
        bins = R["t5"]["static"]["bins"]
        rows = [[name, (f"{g['n']:,}" if g else "-"), (f"{g['gap']:+.3f} {_ci(g['gap_ci'], 3)}" if g else "-")]
                for name, g in bins.items()]
        L += [f"**{SITE_LABEL[k]}**", ""] + _md(["bin", "edges at C = 0", "gap"], rows) + [""]
    return L


REGISTRY_FORMS = ("person", "person+bal_strict", "person+bal_weak", "person+status", "person+bal_strict+status",
                  "person+bal_weak+status", "person+tri4", "person+tri16", "person+tri16+status")


def _sec_variations(Rs):
    L = ["## 8. Variations: model forms, and which fits best", "",
         "Every variant is run through the same forward-chained protocol as T2 (person terms are the eight online columns "
         "unless the name says otherwise). **Balance features**: `bal_strict` is the one-column sum over triads of s(u,w) s(w,v) "
         "(Heider, all 16 types), `bal_weak` the same with the mm types set to 0 (Davis); `tri4` the four undirected types; "
         "`tri16` the 16 free types. **Status features**: `status` = the one-column sum of the oriented status rule over "
         "triads plus the node status difference sigma(v) - sigma(u) [L4801, L4802]. `recip` = the sign of the reverse tie "
         "when it is already in the evidence. `person_flex` adds squares and products of the person columns; "
         "`+interactions` adds the 16 log counts times the sender and receiver log-odds. `frozen_effects` is the other reading "
         "of a_i and b_j: one ridge-fitted effect per user, frozen at the end of each training window. Counts are raw or log, "
         "chosen once on the inner validation block. Sorted by pooled held-out log-loss; the best row of each site is in bold; "
         "the best of the registry's own forms (person plus balance, status or triad terms) is marked.", ""]
    for k, R in Rs.items():
        m = R["t2"]["summary"]["models"]
        df = R["t2"]["summary"]["diff"]
        order = sorted(m, key=lambda n: m[n]["logloss"])
        best_reg = min([n for n in order if n in REGISTRY_FORMS], key=lambda n: m[n]["logloss"])
        rows = []
        for n in order:
            d = m[n]
            dd = df.get(n)
            nm = f"**{n}**" if n == order[0] else (f"{n} (best registry form)" if n == best_reg else n)
            rows.append([nm, d["n_params"], d["transform"], f"{d['auc']:.4f}",
                         (f"{dd['d_auc']:+.4f} {_ci(dd['d_auc_ci'], 4)}" if dd else "(reference)"), f"{d['logloss']:.4f}", f"{d['ba']:.4f}"])
        L += [f"**{SITE_LABEL[k]}** (best by log-loss: {order[0]}; by AUC: {R['t2']['best_auc']})", ""]
        L += _md(["variant", "params", "counts", "AUC", "AUC minus person", "log-loss", "balanced acc."], rows,
                 ["---", "---:", "---", "---:", "---:", "---:", "---:"])
        L.append("")
    L += ["### 8.1 Paired comparisons that answer the named questions", "",
          "First minus second; AUC and log-loss differences with 95% intervals; and the AUC difference restricted to edges with "
          "C >= 5. A negative log-loss difference favours the first model.", ""]
    names = {"person+bal_weak | person+bal_strict": "weak minus strict balance (with person terms)",
             "bal_weak | bal_strict": "weak minus strict balance (alone)",
             "person+bal_strict+status | person+bal_strict": "status added to strict balance",
             "person+bal_weak+status | person+bal_weak": "status added to weak balance",
             "person+status | person": "status added to person terms",
             "person+tri16+status | person+tri16": "status added to the 16 types",
             "tri16+status | tri16": "status added to the 16 types (no person terms)",
             "tri16 | status": "16 types minus status (no person terms)",
             "person+tri16 | person+bal_weak": "16 free types minus weak balance",
             "person+tri16 | person+tri4": "16 directed types minus 4 undirected types",
             "person+tri4 | person+bal_weak": "4 undirected types minus weak balance",
             "person+bal_strict | person": "strict balance added to person terms",
             "person+bal_weak | person": "weak balance added to person terms",
             "person+tri16 | person": "16 types added to person terms (G)",
             "person+recip | person": "reverse-tie sign added to person terms",
             "person+tri16+recip | person+tri16": "reverse-tie sign added to the 16 types",
             "person_flex | person": "flexible person terms minus person terms",
             "person_flex+tri16+interactions | person_flex": "16 types + interactions added to flexible person terms",
             "frozen_effects | person": "frozen user effects minus online person terms"}
    for k, R in Rs.items():
        rows = []
        for key, lab in names.items():
            p = R["t2"]["pairs"].get(key)
            if not p:
                continue
            rows.append([lab, f"{p['auc']['diff']:+.4f} {_ci(p['auc']['ci'], 4)}", f"{p['logloss']['diff']:+.4f} {_ci(p['logloss']['ci'], 4)}",
                         f"{p['auc_c5']['diff']:+.4f} {_ci(p['auc_c5']['ci'], 4)}" if _fin(p["auc_c5"]["diff"]) else "n/a"])
        L += [f"**{SITE_LABEL[k]}**", ""] + _md(["comparison", "AUC", "log-loss", "AUC at C >= 5"], rows) + [""]
    L += ["### 8.2 Restricting to edges with C >= 5", "",
          "The same ranking on the edges that have triad evidence (best of all variants and best registry form by log-loss, and "
          "G):", ""]
    rows = []
    for k, R in Rs.items():
        m = R["t2"]["summary_c5"]["models"]
        order = sorted(m, key=lambda n: m[n]["logloss"])
        best_reg = min([n for n in order if n in REGISTRY_FORMS], key=lambda n: m[n]["logloss"])
        g = R["t2"]["summary_c5"]["diff"].get("person+tri16")
        rows.append([SITE_LABEL[k], f"{R['t2']['summary_c5']['n']:,}", order[0], best_reg,
                     f"{m['person']['auc']:.3f}", f"{m['person+tri16']['auc']:.3f}",
                     f"{g['d_auc']:+.4f} {_ci(g['d_auc_ci'], 4)}" if g else "n/a"])
    L += _md(["site", "edges", "best by log-loss", "best registry form", "AUC person", "AUC both", "G"], rows,
             ["---", "---:", "---", "---", "---:", "---:", "---:"])
    L.append("")
    return L


def _sec_null(Rs):
    L = ["## 9. The null, and what the test could have found", "",
         "**Why a null is needed.** Triad counts are built from the same ties as the person terms, so G is not zero when "
         "nothing but person propensities generated the signs: the counts carry extra (noisy) information about users' "
         "propensities, such as how a user is treated as a receiver when the question concerns their behaviour as a sender. "
         "The right comparison for G, and for the forward-chain coefficients, is therefore not zero but what a world with "
         "person propensities only would give.", "",
         "**The person-only world.** The real network skeleton (who rates whom, and when) is kept; the signs are redrawn from "
         "a period intercept plus one ridge-fitted effect per sender and per receiver, with the ridge tuned so that the "
         "online person model reaches the same held-out AUC it reached on the real signs; each redrawn world goes through the "
         "whole pipeline. Two further worlds add a planted forward-chain mechanism of known size on top of the same person "
         "terms (FFpp +, FFpm -, FFmp -, FFmm - by 0.1 or 0.3 log-odds per triad; the signs are drawn in time order from the "
         "counts of the signs already drawn).", ""]
    rows = []
    for k, R in Rs.items():
        n = R["null"]
        po, p1, p3 = null_arrays(R, "person-only"), null_arrays(R, "planted 0.1"), null_arrays(R, "planted 0.3")
        gobs, dobs = R["t2"]["G"]["diff"], R["t2"]["D"]["diff"]
        mu, sd, z, p = null_z(gobs, po["G"])
        g5 = R["t2"]["G_c5"]["diff"]
        mu5, sd5, z5, p5 = null_z(g5, po["G5"]) if np.isfinite(po["G5"]).sum() > 2 else (np.nan,) * 4
        rows.append([SITE_LABEL[k], f"{n['lambda']:.3g}", f"{n['target_person_auc']:.4f} / {po['auc_person'].mean():.4f}",
                     f"{gobs:+.4f}", f"{mu:+.4f} ({sd:.4f})", f"{z:+.1f}", f"{p:.3f}",
                     f"{p1['G'].mean():+.4f}", f"{p3['G'].mean():+.4f}",
                     f"{g5:+.4f}", f"{mu5:+.4f}", f"{z5:+.1f}"])
    L += _md(["site", "ridge", "person AUC: real / null world", "G observed", "G, person-only world (sd)", "z", "p",
              "G, planted 0.1", "G, planted 0.3", "G at C >= 5", "null at C >= 5", "z"], rows,
             ["---", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---:", "---:"])
    widen, clear = [], []
    for k, R in Rs.items():
        po = null_arrays(R, "person-only")["G"]
        lo, hi = R["t2"]["G2"]["ci"]
        widen.append(((hi - lo) / (2 * Z95)) / po.std(ddof=1))
        if lo > po.mean():
            clear.append(k)
    L += ["", f"Replicates: {len(Rs[next(iter(Rs))]['null']['person-only']['reps'])} person-only, "
          f"{len(Rs[next(iter(Rs))]['null']['planted 0.1']['reps'])} per planted size. z = (observed - null mean) / null sd; p = "
          "share of null replicates at or above the observation (with +1). The null sd is the spread of G over redrawn signs with "
          f"the generator's person effects held fixed, {min(widen):.0f} to {max(widen):.0f} times narrower than the two-way bootstrap "
          "spread of the observed G (section 4), so z measures distance from this generator rather than the precision of G; the "
          f"observed G's two-way interval lies above the null mean at {_names(clear)}. The generator's effects are fitted on every "
          "edge with a light ridge (in-sample AUC on the real signs "
          + ", ".join(f"{R['null']['generator_auc']:.2f} at {SITE_LABEL[k]}" for k, R in Rs.items())
          + "), so the person-only world inherits much of the real sign pattern; it is static, and has no reciprocity beyond "
          "person effects (added at review).", "",
          "### 9.1 The forward-chain pattern in the person-only world", "",
          "Mean forward-chain coefficients over the person-only replicates (sd in brackets), against the observed ones. If "
          "the pattern of the 16 types alone (static) appears here it needs no mechanism.", ""]
    rows = []
    for k, R in Rs.items():
        po = null_arrays(R, "person-only")
        for fit, lab in (("static:tri16", "static, 16 types alone"), ("static:person+tri16", "static, + person terms"),
                         ("causal:tri16", "causal, 16 types alone"), ("causal:person+tri16", "causal, + person terms")):
            arr = po["coef"][fit]
            obs = R["t1"][fit]["rows"]
            cells = []
            for j, nm in enumerate(FORWARD):
                mu, sd, z, p = null_z(obs[nm]["coef"], arr[:, j])
                cells.append(f"{obs[nm]['coef']:+.2f} vs {mu:+.2f} ({sd:.2f}), z {z:+.1f}")
            rows.append([SITE_LABEL[k], lab] + cells)
    L += _md(["site", "fit"] + [f"{n}: observed vs null" for n in FORWARD], rows, ["---", "---", "---:", "---:", "---:", "---:"])
    L += ["", "### 9.2 Planted mechanisms: recovered?", "",
          "Mean person-adjusted coefficients over the replicates with a planted mechanism (the planted values "
          "are +0.1/-0.1/-0.1/-0.1 and +0.3/-0.3/-0.3/-0.3), and the held-out gain G they produced. Two things follow. "
          "A mechanism of 0.3 per triad, the size of the triad-only coefficients, adds very little AUC on these skeletons, "
          "which is the sensitivity of the test. And the static design attenuates a mechanism that acts from earlier ties on "
          "later ones, because the later edges it counts are noise to an earlier tie: it returns a fraction of the planted "
          "size where the causal design returns all of it, so coefficient sizes are comparable with planted sizes only in "
          "the causal rows. FFmm is also poorly supported on the small Bitcoin skeletons, where even a planted -0.3 does not "
          "come back.", ""]
    rows = []
    for k, R in Rs.items():
        for scen in ("planted 0.1", "planted 0.3"):
            a = null_arrays(R, scen)
            for fit, lab in (("causal:person+tri16", "causal, + person"), ("static:person+tri16", "static, + person")):
                rows.append([SITE_LABEL[k], scen, lab] + [f"{a['coef'][fit][:, j].mean():+.2f}" for j in range(4)] +
                            [f"{a['G'].mean():+.4f} ({a['G'].std(ddof=1):.4f})", f"{a['G5'][np.isfinite(a['G5'])].mean():+.4f}"])
    L += _md(["site", "world", "fit"] + list(FORWARD) + ["G (sd)", "G at C >= 5"], rows,
             ["---", "---", "---", "---:", "---:", "---:", "---:", "---:", "---:"])
    L.append("")
    return L


def _sec_caveats(Rs):
    return [
        "## 10. Caveats",
        "",
        "- **Four sites, three media, two eras.** Bitcoin OTC and Alpha are two views of one market (2010-16); wiki-RfA is public "
        "voting on one wiki (2003-13); BlueTempNet is Bluesky follows and blocks (2023-24) in the creator graph only. The registry's "
        "R-E was checked on 1999-2009 sites; nothing here is a re-estimate on those. Magnitudes are per site and per period "
        "[L4857, L4859].",
        "- **The signs mean different things.** A Bitcoin rating follows a trade; an RfA vote is public, consequential and "
        "strategic; a block is partly a safety tool and a follow is not affect [L4567, L4823; 117 section 3.6]. No site records a "
        "drive.",
        "- **Person terms are measured, not known.** The online person columns are noisy estimates of a_i and b_j from earlier "
        "ties; the triad counts add some information about the same users. That is why the person-only world is needed, and it "
        "assumes static person effects: if users' propensities drift, a triad-only gain over a static world could be a "
        "recent-behaviour gain, not a mechanism.",
        "- **Controlling for person terms is not innocent.** If a triad mechanism shaped the earlier ties, it also shaped the "
        "person histories, so person-adjusted triad coefficients are lower bounds on a mechanism that acts through both; the "
        "claim made is predictive (what triad counts add to held-out accuracy given person histories), not causal.",
        "- **Static against causal coefficients.** A mechanism that acts from earlier ties on later ones is attenuated in a static "
        "fit, because the later edges it counts are noise to an earlier tie: a planted 0.3 per triad comes back as 0.07 to 0.09 in "
        "the static fit and 0.28 to 0.33 in the causal fit at wiki-RfA (section 9.2). LHK's design is static, so its coefficients "
        "(and the R1 rows labelled static) understate such a mechanism by a factor of three or four; the causal rows do not, and "
        "they agree with the static ones on every sign that matters here (FFmm is not negative once person terms are in).",
        "- **Insensitivity of the AUC increment.** A forward-chain mechanism of 0.3 log-odds per triad, planted on the real "
        "skeletons, adds only a few thousandths of AUC, because most edges have little or no triad evidence (section 1). "
        "G < 0.02 does not exclude a per-triad effect of that size; the coefficients and the strata at C >= 5 are the better "
        "guides, and R2 as pre-registered is the less sensitive instrument.",
        "- **Additive logistic forms only.** The registry's R-E is additive in the logit; nonlinear learners (trees, "
        "embeddings; Chiang et al. found low-rank global methods beat local triad methods [L4864]) were not tried, and "
        "global structure beyond common neighbours is outside the registry's form.",
        "- **Time resolution.** Bitcoin Alpha's times are coarse (about 1,650 distinct values for 24,186 ratings), so the causal "
        "rule discards same-day evidence there; wiki-RfA times are to the minute but voters in one election are partly "
        "simultaneous.",
        "- **wiki-RfA reciprocal pairs are not replies.** A voter and a candidate who each voted on the other did so in two "
        "different elections, years apart; the T4 share there is a different thing from a trader's reply.",
        "- **Interval method.** Percentile intervals from 300 bootstrap replicates; null replicates number 20 (person-only) and 8 "
        "per planted size, so null means carry visible Monte Carlo error, shown as the sd, and the smallest possible p is 1/21.",
        _multiplicity_caveat(Rs),
        "",
    ]


def _multiplicity_caveat(Rs) -> str:
    """Added at review (2026-11-01): what the per-test rules would lose under a family-wise correction, and how far R2's NO
    rests on its threshold.  Computed from the cached statistics, so it cannot drift from the numbers."""
    zb = float(stats.norm.isf(0.025 / 16))         # Bonferroni over the 16 forward-chain cells of one fit (4 sites x 4 types)
    marg = []
    for k, R in Rs.items():
        r = R["t1"]["static:tri16"]["rows"]["FFmm"]
        if r["status"] == "SUPPORTED" and min(abs(r["z"]), abs(r["z2"])) < zb:
            marg.append(f"FFmm in the 16-type fit alone at {SITE_LABEL[k]} (z {r['z']:+.1f} / {r['z2']:+.1f})")
        r = R["t1"]["static:person+tri16"]["rows"]["FFmm"]
        if r["status2"] == "CONTRADICTED" and abs(r["z2"]) < zb:
            marg.append(f"FFmm positive with person terms at {SITE_LABEL[k]} on the two-way rule (z {r['z2']:+.1f})")
    elig = sorted((R["t2"]["G"]["diff"] for R in Rs.values()
                   if R["t2"]["tier"] != "none" and R["t2"]["tier2"] != "none"), reverse=True)
    sens = ""
    if len(elig) >= 2:
        sens = (f" With the same intervals R2 would read MIXED at a threshold of {elig[1]:.4f} or below"
                + (f" and YES at {elig[2]:.4f} or below" if len(elig) >= 3 else "") + ".")
    return ("- **Multiplicity and thresholds** (added at review). R1 to R5 are per-test rules (|z| beyond 1.96, 95% intervals) "
            "applied without a family-wise correction across four sites, four forward chains, two evidence rules, two fits, two "
            "clusterings and the per-bin calls of T3. Claims that rest on one marginal z would not survive a Bonferroni correction "
            f"over the sixteen forward-chain cells of one fit (|z| above {zb:.2f}): " + ("; ".join(marg) if marg else "none") + ". "
            "R2's NO is the conservative direction, but its 0.02 threshold is a gain in balanced-accuracy points that LHK's "
            "figure shows by eye (about +-0.02) over a different baseline [L4829], used here as an AUC gain." + sens +
            " The variant rankings of section 8 are chosen on the same test window they are scored on, so the order of close "
            "variants is optimistic.")


def _sec_reproduce(Rs):
    return [
        "## 11. Reproduce",
        "",
        "    cd sim",
        "    ~/.local/bin/uv run python -m models.sign_registry_battery fetch            # missing sources, sha256-checked",
        "    for s in wiki otc alpha bsky; do ~/.local/bin/uv run python -m models.sign_registry_battery compute $s --workers 3; done",
        "    ~/.local/bin/uv run python -m models.sign_registry_battery report",
        "    ~/.local/bin/uv run pytest tests/test_sign_registry_battery.py",
        "",
        "`compute` is seeded and takes minutes to tens of minutes per site (BlueTempNet longest; most of it is the null "
        "replicates). Statistics are cached under `sim/data/sign_registry_battery_cache/` (git-ignored, with the data); "
        "`report` rewrites this file from them. The Bluesky sources are fetched from the authors' public GitHub LFS "
        "endpoint (`fetch bsky`, 221 MB, checksum-verified).",
        "",
    ]



def _scoreboard(Rs):
    """One table: each test, as the data answered it, by site."""
    ks = list(Rs)
    rows = []

    def row(label, fn):
        rows.append([label] + [fn(k, Rs[k]) for k in ks])

    def ff(R, fit, nm="FFmm"):
        r = R["t1"][fit]["rows"][nm]
        return f"{r['coef']:+.2f} ({r['z']:+.1f}/{r['z2']:+.1f}) {_STAT_LETTER[r['status']]}/{_STAT_LETTER[r['status2']]}"

    row("T1  FFmm, 16 types alone, static: coef (z 1-way/2-way) R1", lambda k, R: ff(R, "static:tri16"))
    row("T1  FFmm, 16 types alone, in a person-only world", lambda k, R: (
        lambda arr: f"{arr[:, 3].mean():+.2f} ({arr[:, 3].std(ddof=1):.2f})")(null_arrays(R, "person-only")["coef"]["static:tri16"]))
    row("T1  FFmm, with person terms (R-E as written), static", lambda k, R: ff(R, "static:person+tri16"))
    row("T1  forward chains supported with person terms, static (of 4; 1-way/2-way)", lambda k, R: (
        f"{sum(R['t1']['static:person+tri16']['rows'][n]['status'] == 'SUPPORTED' for n in FORWARD)}/"
        f"{sum(R['t1']['static:person+tri16']['rows'][n]['status2'] == 'SUPPORTED' for n in FORWARD)}"))
    row("T2  D = AUC(person) - AUC(triad), 2-way interval", lambda k, R: f"{R['t2']['D']['diff']:+.3f} {_ci(R['t2']['D2']['ci'], 3)}")
    row("T2  G = AUC(both) - AUC(person), 2-way interval", lambda k, R: f"{R['t2']['G']['diff']:+.4f} {_ci(R['t2']['G2']['ci'], 4)}")
    row("T2  R2 tier (1-way / 2-way)", lambda k, R: f"{R['t2']['tier']} / {R['t2']['tier2']}")
    row("T2  G at C >= 5, 2-way interval", lambda k, R: f"{R['t2']['G_c5']['diff']:+.4f} {_ci(R['t2']['G_c5_2']['ci'], 4)}")
    row("T2  G minus person-only-world mean (z)", lambda k, R: (
        lambda po: f"{R['t2']['G']['diff'] - po['G'].mean():+.4f} (z {null_z(R['t2']['G']['diff'], po['G'])[2]:+.1f})")(null_arrays(R, "person-only")))
    row("T3  forward chains CONTRADICTED in >= 2 date bins (16 types alone)", lambda k, R: (
        "FLIPPED " + "/".join(R["t3"]["snapshot:triad-only"]["verdict"]["flipped_types"])
        if R["t3"]["snapshot:triad-only"]["verdict"]["refuted"] else "none"))
    row("T3  intercepts move (range, logit)", lambda k, R: (
        f"{'yes' if R['t3']['snapshot:triad-only']['verdict']['intercepts_move'] else 'no'} "
        f"({R['t3']['snapshot:triad-only']['verdict']['intercept_range']:.2f})"))
    row("T4  opposite-sign share of reciprocated pairs", lambda k, R: (
        f"{_pct(R['t4']['share'])} ({'rare' if R['t4']['rare'] else 'NOT rare'})"))
    row("T5  InSign - OutSign at C = 0 (static), R5 1-way / 2-way (the verdict needs both)", lambda k, R: (
        f"{R['t5']['static']['strata']['C = 0']['gap']:+.3f} {R['t5']['static']['verdict']} / {R['t5']['static2']['verdict']}"))
    return _md(["test (rule)"] + [SITE_LABEL[k] for k in ks], rows, ["---"] + ["---:"] * len(ks))


def _rng(vals, fmt="{:+.3f}"):
    vals = [v for v in vals if v is not None and np.isfinite(v)]
    if not vals:
        return "n/a"
    lo, hi = fmt.format(min(vals)), fmt.format(max(vals))
    return lo if lo == hi else f"{lo} to {hi}"


def _names(keys):
    keys = list(keys)
    if not keys:
        return "no site"
    labs = [SITE_LABEL[k] for k in keys]
    return labs[0] if len(labs) == 1 else ", ".join(labs[:-1]) + " and " + labs[-1]
def verdict_text(Rs):
    """The verdict, written from the numbers.  Every claim is guarded by an assertion on the values it rests on, so that a
    rerun on different data fails here instead of printing a sentence that is no longer true."""
    ks = list(Rs)
    n = len(ks)
    lab = SITE_LABEL
    t2 = {k: Rs[k]["t2"] for k in ks}
    t1s = {k: Rs[k]["t1"]["static:tri16"]["rows"] for k in ks}
    t1p = {k: Rs[k]["t1"]["static:person+tri16"]["rows"] for k in ks}
    po = {k: null_arrays(Rs[k], "person-only") for k in ks}
    pairs = {k: t2[k]["pairs"] for k in ks}

    # ------------------------------------------------------------------ T2
    Dd = [t2[k]["D"]["diff"] for k in ks]
    Gd = [t2[k]["G"]["diff"] for k in ks]
    assert all(t2[k]["D2"]["ci"][0] > 0 for k in ks), "person terms no longer carry more at every site"
    assert max(Gd) < RULE_G_MATERIAL, "a site reaches the material tier: rewrite the verdict"
    tiers = [t2[k]["tier"] for k in ks]
    tiers2 = [t2[k]["tier2"] for k in ks]
    assert r2_overall(tiers) == "NO" and r2_overall(tiers2) == "NO"
    zG = {k: null_z(t2[k]["G"]["diff"], po[k]["G"]) for k in ks}
    above = [k for k in ks if zG[k][2] > 3]
    c5_material = [k for k in ks if t2[k]["tier_c5"] == "material"]
    G_null = [po[k]["G"].mean() for k in ks]

    # ------------------------------------------------------------------ T1
    alone = {k: t1s[k]["FFmm"] for k in ks}
    pers = {k: t1p[k]["FFmm"] for k in ks}
    alone_ok = [k for k in ks if alone[k]["status"] == "SUPPORTED" and alone[k]["status2"] == "SUPPORTED"]
    alone_und = [k for k in ks if alone[k]["status"] == "UNDECIDED" and alone[k]["status2"] == "UNDECIDED"]
    assert set(alone_ok) | set(alone_und) == set(ks), "FFmm alone is contradicted or split between the two rules somewhere"
    all4 = [k for k in ks if all(t1s[k][m]["status2"] == "SUPPORTED" for m in FORWARD)]
    assert not [k for k in ks if pers[k]["status2"] == "SUPPORTED"], "FFmm survives person terms somewhere (two-way)"
    pers_pos2 = [k for k in ks if pers[k]["status2"] == "CONTRADICTED"]
    pers_pos1 = [k for k in ks if pers[k]["status"] == "CONTRADICTED" and k not in pers_pos2]
    nullmm = {k: null_z(alone[k]["coef"], po[k]["coef"]["static:tri16"][:, 3]) for k in ks}
    assert all(nullmm[k][0] < -0.2 for k in ks), "a person-only world no longer gives FFmm < 0"
    assert all(nullmm[k][2] > 0 for k in ks), "observed FFmm is more negative than a person-only world's somewhere"
    keep = [k for k in ks if t1p[k]["FFpm"]["status2"] == "SUPPORTED" and t1p[k]["FFmp"]["status2"] == "SUPPORTED"]
    ratio = [t1p[k][m]["coef"] / t1s[k][m]["coef"] for k in keep for m in ("FFpm", "FFmp")]
    assert len(keep) >= 3 and 0.2 < min(ratio) and max(ratio) < 0.8, "mixed-sign chains no longer keep a third to two thirds"
    cmm = {k: Rs[k]["t1"]["causal:person+tri16"]["rows"]["FFmm"] for k in ks}
    planted_mm = {k: float(null_arrays(Rs[k], "planted 0.3")["coef"]["causal:person+tri16"][:, 3].mean()) for k in ks}
    excl = [k for k in ks if cmm[k]["coef"] - Z95 * cmm[k]["se2"] > planted_mm[k]]
    assert excl, "the planted FFmm is excluded nowhere"
    surv = {}
    for t_ in TYPES:
        sg = [np.sign(t1p[k][t_]["coef"]) for k in ks if t1p[k][t_]["support"] >= RULE_MIN_SUPPORT and abs(t1p[k][t_]["z2"]) > Z95]
        if len(sg) >= 3 and len(set(sg)) == 1:
            surv[t_] = int(sg[0])
    assert "FFmm" not in surv and "FFpm" in surv and "FFmp" in surv

    # ------------------------------------------------------------------ T3, T4, T5
    flips = {k: Rs[k]["t3"]["snapshot:triad-only"]["verdict"] for k in ks}
    assert not any(v["refuted"] or v["refuted2"] for v in flips.values()), "the pattern flips with date somewhere"
    moves = [k for k in ks if flips[k]["intercepts_move"]]
    p2 = [k for k in ks if Rs[k]["t3"]["snapshot:person"]["verdict"]["refuted2"]]
    p1 = [k for k in ks if Rs[k]["t3"]["snapshot:person"]["verdict"]["refuted"] and k not in p2]
    early = [k for k in ("otc", "alpha") if k in ks and flips[k]["flips"]["FFpp"] == 1]
    t4 = {k: Rs[k]["t4"] for k in ks}
    rare = [k for k in ks if t4[k]["rare"]]
    notrare = [k for k in ks if not t4[k]["rare"]]
    def yrs(k):
        return sorted((int(y), v["share"]) for y, v in t4[k]["by_year"].items() if v["n"] >= 100)
    y0 = {k: yrs(k)[0] for k in ks}
    y1 = {k: yrs(k)[-1] for k in ks}
    assert all(y1[k][1] > y0[k][1] for k in ks), "the opposite-sign share no longer rises with the date everywhere"
    t5 = {k: Rs[k]["t5"] for k in ks}
    r5 = {k: r5_both(t5[k]["static"]["verdict"], t5[k]["static2"]["verdict"]) for k in ks}
    vis = [k for k in ks if r5[k] == "SUPPORTED"]
    vis_abs = [k for k in ks if r5[k] == "ABSENT"]
    vis_und = [k for k in ks if r5[k] == "UNDECIDED"]
    vis_abs1 = [k for k in vis_und if t5[k]["static"]["verdict"] == "ABSENT"]      # absent on the receiver-cluster rule only

    # ------------------------------------------------------------------ variations
    rc = {k: pairs[k]["person+recip | person"]["auc"] for k in ks}
    rc_more = [k for k in ks if rc[k]["ci"][0] > 0 and rc[k]["diff"] > t2[k]["G"]["diff"]]
    assert len(rc_more) >= 2, "reciprocity is no longer larger than the triads at two sites"
    ws = {k: pairs[k]["person+bal_weak | person+bal_strict"]["auc"] for k in ks}
    assert all(abs(ws[k]["diff"]) < 0.002 for k in ks), "strict and weak balance are no longer indistinguishable"
    stt = {k: pairs[k]["person+status | person"]["auc"] for k in ks}
    stt_t = {k: pairs[k]["person+tri16+status | person+tri16"]["auc"] for k in ks}
    assert max(abs(stt[k]["diff"]) for k in ks) < 0.005 and max(abs(stt_t[k]["diff"]) for k in ks) < 0.005
    best = {k: t2[k]["best_logloss"] for k in ks}
    mm = {k: t2[k]["summary"]["models"] for k in ks}
    best_reg = {k: min([m_ for m_ in mm[k] if m_ in REGISTRY_FORMS], key=lambda m_: mm[k][m_]["logloss"]) for k in ks}
    frozen = [pairs[k]["frozen_effects | person"]["auc"]["diff"] for k in ks]
    assert max(frozen) < -0.05

    # ------------------------------------------------------------------ added at review (2026-11-01)
    # how big the residue is against the planted calibration, and whether the bootstrap agrees with the replicate z
    p3 = {k: null_arrays(Rs[k], "planted 0.3") for k in ks}
    exc = {k: t2[k]["G"]["diff"] - po[k]["G"].mean() for k in ks}
    exc3 = {k: p3[k]["G"].mean() - po[k]["G"].mean() for k in ks}
    assert all(exc3[k] > 0 for k in ks), "a planted 0.3 mechanism no longer raises G above the person-only world"
    big = [k for k in above if exc[k] > exc3[k]]
    assert [k for k in above if t2[k]["G2"]["ci"][0] > po[k]["G"].mean()] == above, \
        "the two-way bootstrap interval of G no longer clears the null mean where the replicate z does"
    gabove = [t2[k]["G"]["diff"] for k in above]
    full = [k for k in ks if planted_mm[k] <= -0.27]
    ws_lead = [k for k in ks if ws[k]["ci"][1] < 0]                                  # strict ahead with person terms
    assert all(ws[k]["ci"][0] < 0 for k in ks), "weak balance now beats strict with person terms somewhere"
    pp_low = [k for k in ks if t1p[k]["FFpp"]["status2"] != "SUPPORTED"]
    assert all(list(np.sign(po[k]["coef"]["static:tri16"].mean(0))) == [1, -1, -1, -1] for k in ks), \
        "a person-only world no longer gives the whole forward-chain pattern in the 16-type fit alone"
    mm_null_p = {k: float(po[k]["coef"]["static:person+tri16"][:, 3].mean()) for k in ks}

    L = ["## Verdict", ""]
    L += ["**In short.** *Do signs have a mechanism inside the registry beyond person propensities?* **No by the pre-registered "
          "rule (R2), and not in the form the registry writes; but not nothing.** The registry's headline, FFmm < 0, is a person "
          "effect, and the triad terms add less than the pre-registered 0.02 AUC to person terms at every site. What remains beyond "
          f"static person propensities is a residue at {_names(above)} ({100 * min(gabove):.1f} to {100 * max(gabove):.1f} points of AUC "
          f"overall, {100 * max(t2[k]['G_c5']['diff'] for k in ks):.1f} at the best site where triad evidence is dense) that is only "
          "partly what the registry names. Small in AUC is not small per triad: on these networks a planted forward-chain mechanism "
          f"of 0.3 log-odds per triad adds only {_rng([100 * exc3[k] for k in ks], '{:.1f}')} points above the person-only world"
          + (f", and the residue exceeds that at {_names(big)}" if big else "") + ".", ""]
    L += [f"- **Person terms carry the prediction.** Held out in time (causal features, four forward-chained blocks), a user's own earlier "
          "signs and the signs others gave the target predict a sign better than the 16 triad types do: AUC "
          f"{_rng(Dd)} higher at the {n} sites, every interval above 0 (the registry's prediction, 112 section 6.5 item 2, holds). "
          f"Adding the triad types to the person terms adds {_rng(Gd)} AUC against the pre-registered 0.02 for a material "
          f"mechanism: R2 is **{r2_overall(tiers)}** (material at none of {n}; the same with sender-and-receiver intervals)."]
    L += [f"- **A residue beyond static person propensities is real, and small in AUC.** Against the null (signs redrawn from person "
          f"propensities on the same network, G {_rng(G_null)}) the observed G is clearly above it at {_names(above)} (z "
          f"{', '.join(f'{zG[k][2]:+.1f}' for k in above)} in units of the null's replicate spread, which holds the person effects fixed; "
          "the two-way bootstrap interval of the observed G, which is wider, also lies above the null mean at each); where triad "
          f"evidence is dense (C >= 5) G is {_rng([t2[k]['G_c5']['diff'] for k in ks])}, material at {_names(c5_material)}. With person terms in "
          "the fit the types that keep a sign and a z beyond 1.96 (against 0; the null was recorded for the forward chains only) at "
          "three or more sites are "
          + ", ".join(f"{t_} ({'+' if sgn > 0 else '-'})" for t_, sgn in surv.items())
          + ": two of the registry's forward chains (the mixed-sign ones, at "
          f"{_rng(ratio, '{:.2f}')} of their size without person terms) and agreement through a shared third party, not FFmm and not FFpp."]
    L += [f"- **FFmm < 0 is a person effect.** Fitted alone, as LHK did, it is supported at {_names(alone_ok)} (undecided at "
          f"{_names(alone_und)}; contradicted nowhere), and the whole forward chain pp +, pm -, mp -, mm - is supported at "
          f"{_names(all4)}. But signs drawn from person propensities alone give FFmm {_rng([nullmm[k][0] for k in ks], '{:+.2f}')} on the same networks, "
          f"as negative as or more negative than observed ({_rng([alone[k]['coef'] for k in ks], '{:+.2f}')}); and with person terms in the fit, which "
          f"is how R-E is written, FFmm is {_rng([pers[k]['coef'] for k in ks], '{:+.2f}')}: no better than 0 at "
          f"{_names([k for k in ks if k not in pers_pos2])}"
          + (f" and positive at {_names(pers_pos2)} (z beyond 1.96 on both rules)" if pers_pos2 else "")
          + (f" (positive on the receiver-cluster rule only at {_names(pers_pos1)})" if pers_pos1 else "") + ". "
          "Power: with person terms in the causal fit a planted FFmm of -0.3 comes back as "
          + ", ".join(f"{planted_mm[k]:+.2f} at {lab[k]}" for k in ks)
          + (" (full size nowhere" if not full else f" (full size at {_names(full)}")
          + (", attenuated elsewhere)" if len(full) < len(ks) else ")") + "; the observed values are "
          + ", ".join(f"{cmm[k]['coef']:+.2f} [{cmm[k]['coef'] - Z95 * cmm[k]['se2']:+.2f}, {cmm[k]['coef'] + Z95 * cmm[k]['se2']:+.2f}] at {lab[k]}" for k in ks)
          + f", so a mechanism of that size is excluded at {_names(excl)} and cannot be excluded at {_names([k for k in ks if k not in excl])}."]
    L += [f"- **Reciprocity is a pair-level effect of the same order as the triads.** The reverse tie's sign adds "
          f"{_rng([rc[k]['diff'] for k in ks])} AUC to person terms (interval above 0 at {_names([k for k in ks if rc[k]['ci'][0] > 0])}; more than "
          f"the 16 triad types add at {_names(rc_more)}, less at {_names([k for k in ks if k not in rc_more])}); R-E has no such term."]
    L += ["", *_scoreboard(Rs), ""]
    L += ["**Registry claims, one by one.**", ""]
    L += [f"- *T1, form transfer (R1).* **Supported** in the reading LHK fitted (16 types alone) at {_names(alone_ok)}; **undecided** at "
          f"{_names(alone_und)} (FFmm z {', '.join(f'{alone[k]['z']:+.1f}' for k in alone_und)}); **not supported** in the reading R-E writes "
          "(person terms in the fit): FFmm is not significantly negative at any site"
          + (f" (R1's refutation, FFmm contradicted with adequate support, is met at {_names(pers_pos2)} on both rules, though a "
             "person-only world gives " + ", ".join(f"{mm_null_p[k]:+.2f}" for k in pers_pos2) + " there too)" if pers_pos2 else "")
          + f", and FFpp is not significantly positive at {_names(pp_low)}. FFpm and FFmp survive at {_names(keep)}."]
    L += [f"- *T2, person terms against triad terms.* Person terms carry more: **supported** (D {_rng(Dd)}). The triad terms add more than person terms: "
          f"**refuted**. R2 as pre-registered: **{r2_overall(tiers)}**. The result depends on what a person term is: with ridge-fitted effects frozen at the "
          "end of training (the other reading of a_i and b_j) person terms alone fall far below even the triad terms, because most "
          f"test-period users are new (frozen minus online AUC {_rng(frozen)})."]
    L += [f"- *T3, drift by date.* **Supported**: no forward-chain type is contradicted in two date bins at any site in the 16-type fit alone "
          f"(R3), while intercepts move at {_names(moves)} (range {_rng([flips[k]['intercept_range'] for k in ks], '{:.2f}')} logit). The "
          "between-user variance of the sign (ICC, section 5) moves too, across date bins: "
          + "; ".join(f"{lab[k]} senders {_rng([b['icc_send'] for b in Rs[k]['t3']['snapshot:triad-only']['bins']], '{:.2f}')}, receivers "
                       f"{_rng([b['icc_recv'] for b in Rs[k]['t3']['snapshot:triad-only']['bins']], '{:.2f}')}" for k in ks)
          + ". With person terms in the fit R3 is "
          + (f"met by FFmm (positive in two or more bins) at {_names(p2)}" if p2 else "met nowhere")
          + (f" and, on the receiver-cluster rule only, at {_names(p1)}" if p1 else "")
          + ". Magnitudes are not stable (I^2 is high for most coefficients)"
          + (f"; the 2010-11 bin (98% positive) has FFpp negative at {_names(early)}, one bin" if early else "") + "."]
    L += [f"- *T4, symmetry.* Opposite signs are **rare** (R4, at most 10%) at {_names(rare)} ({_rng([t4[k]['share'] for k in rare], '{:.3f}')}) and "
          f"**not rare** at {_names(notrare)} ({_rng([t4[k]['share'] for k in notrare], '{:.3f}')}), where a reciprocated pair is two votes in two "
          "elections years apart, not a reply. The two ties of a pair are concordant beyond person terms at every site (residual "
          f"correlation {_rng([t4[k]['resid_corr'] for k in ks], '{:.2f}')}): R-A's symmetric p_ij is defensible where replies are quick, but it is "
          "the reverse tie, not a symmetric factor, that carries the information. The opposite-sign share rises with the date at every site "
          "(first to last year with at least 100 pairs): " + "; ".join(f"{lab[k]} {y0[k][1]:.1%} in {y0[k][0]} to {y1[k][1]:.1%} in {y1[k][0]}"
                                                                         for k in ks) + "."]
    def drift_of_gap(k):
        b = [(nm, g["gap"]) for nm, g in t5[k]["static"]["bins"].items() if g]
        pk = max(b, key=lambda x: x[1])
        parts = [f"{b[0][1]:+.2f} in {b[0][0]}"]
        if pk[0] not in (b[0][0], b[-1][0]):
            parts.append(f"{pk[1]:+.2f} in {pk[0]}")
        parts.append(f"{b[-1][1]:+.2f} in {b[-1][0]}")
        return f"{lab[k]} " + ", ".join(parts)
    L += [f"- *T5, visibility.* **Supported** at {_names(vis)} (gap at C = 0 {_rng([t5[k]['static']['strata']['C = 0']['gap'] for k in vis])}, vanishing by C >= 25 "
          f"as in LHK); **absent** at {_names(vis_abs)}; undecided at {_names(vis_und)}"
          + (f" (absent on the receiver-cluster rule only at {_names(vis_abs1)}, whose two-way interval is wide)" if vis_abs1 else "")
          + ". Both rules must agree for either call. The gap moves with the date (at C = 0, static evidence): "
          + "; ".join(drift_of_gap(k) for k in ks) + ". It cannot be read as visibility: a received-majority advantage is also "
          "candidate quality and shared information, and a before/after test of earlier against later votes does not identify "
          "visibility (section 2)."]
    L += ["", "**Refuted, supported, undecided.**", ""]
    L += [f"- *Refuted:* FFmm < 0 as something beyond person propensities (R-E as written: not significantly negative with person terms "
          "at any site" + (f", positive at {_names(pers_pos2)}" if pers_pos2 else "") + "); that triad terms carry more than person terms "
          "(D > 0 at every site); a material triad gain beyond person terms (R2 NO: material at no site); "
          + (f"opposite-sign reciprocation as rare at {_names(notrare)}; " if notrare else "")
          + (f"a received-majority advantage at {_names(vis_abs)} (R5 absent on both rules)." if vis_abs else "")]
    L += [f"- *Supported:* that person terms carry more than triad terms; the forward-chain pattern in the 16-type fit alone at {_names(all4)} "
          f"(FFmm < 0 at {_names(alone_ok)}), as R1 reads it, though a person-only world gives the same pattern; stability of the pattern "
          f"across date bins with moving intercepts; rare opposite signs at {_names(rare)}; "
          f"a received-majority advantage at low embeddedness at {_names(vis)}; mixed-sign chains (FFpm, FFmp) as a small negative term beyond person terms at {_names(keep)}."]
    L += [f"- *Undecided:* FFmm < 0 in the 16-type fit alone at {_names(alone_und)}; FFpp > 0 at "
          f"{_names([k for k in ks if t1s[k]['FFpp']['status2'] == 'UNDECIDED'])}; visibility at {_names(vis_und)}; and whether the residue is a "
          "mechanism or a drifting person propensity (the null's person effects are static). The FFmm test has little power on the two small "
          "Bitcoin skeletons (a planted -0.3 does not come back there), so its null is firm at the larger sites only."]
    wsa = {k: pairs[k]["bal_weak | bal_strict"]["auc"] for k in ks}
    L += ["", "**Variations.** With person terms in the model strict and weak balance are practically indistinguishable (weak minus "
          f"strict AUC {_rng([ws[k]['diff'] for k in ks], '{:+.4f}')}"
          + (f"; strict is ahead by that much, with the interval excluding 0, at {_names(ws_lead)}" if ws_lead else "")
          + "); alone, dropping the mm term helps where triads are many (weak minus strict AUC "
          f"{'; '.join(f'{lab[k]} {wsa[k]['diff']:+.3f} {_ci(wsa[k]['ci'], 3)}' for k in ks)}), which is LHK's weak-balance reading. Status adds {_rng([stt[k]['diff'] for k in ks], '{:+.4f}')} AUC to person terms and "
          f"{_rng([stt_t[k]['diff'] for k in ks], '{:+.4f}')} to the 16 types (a small log-loss gain at some sites, no material AUC gain). By held-out "
          f"log-loss the best of the registry's own forms is {'; '.join(f'{lab[k]}: {best_reg[k]}' for k in ks)}; the best variant overall is "
          f"{'; '.join(f'{lab[k]}: {best[k]}' for k in ks)}.", ""]
    L += ["**What this does not settle.** It tests the registry's additive-logistic triad terms against online person histories on four "
          "sites; nonlinear learners, global structure, a measured drive, or exogenous variation in the triads could find more. "
          "Person-adjusted triad coefficients understate a mechanism that also shaped the person histories, and the null's person "
          "effects are static, so a user whose propensity drifts would also make recent triad counts informative (section 10). "
          "The AUC increment is insensitive on sparse skeletons: a planted forward-chain effect of 0.3 log-odds per triad adds only a "
          "few thousandths of AUC (section 9.2), so the coefficients and the C >= 5 strata carry the weight.", ""]
    L += ["**For the first-outcome decision (Aldred's, not made here).** On this evidence the sign that a 'holds together or splits' "
          "model needs is a person-level propensity (a sender's habit, a receiver's standing) plus a local residue worth about one "
          f"point of AUC overall ({100 * max(t2[k]['G_c5']['diff'] for k in ks):.0f} where triads are dense at the best site), not an "
          "output of the registry's triad terms as written; v0.2 section 2.2 already treats the sign as an input, and the residue is "
          "too small in AUC, and too unlike the registry's form, to derive the sign from structure or composition instead. It does "
          "not say whether those propensities are drives (no site measures one) or whether the residue is a mechanism or drifting "
          "propensities, and it says nothing about conformity or effort outcomes.", ""]
    return L


# --------------------------------------------------------------------------------------------------- command line

def main(argv=None) -> int:
    import argparse
    ap = argparse.ArgumentParser(prog="python -m models.sign_registry_battery", description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    f = sub.add_parser("fetch", help="download the sources that are missing (sha256-checked)")
    f.add_argument("sites", nargs="*", default=list(SITE_ORDER))
    c = sub.add_parser("compute", help="run everything for one site and cache the statistics (git-ignored)")
    c.add_argument("site", choices=SITE_ORDER)
    c.add_argument("--workers", type=int, default=1)
    c.add_argument("--R-null", type=int, default=20)
    c.add_argument("--R-planted", type=int, default=8)
    c.add_argument("--B", type=int, default=300)
    r = sub.add_parser("report", help="write sim/results/sign_registry_battery.md from the cached statistics")
    r.add_argument("--out", default=str(SIM / "results" / "sign_registry_battery.md"))
    a = ap.parse_args(argv)
    if a.cmd == "fetch":
        for k in a.sites:
            print(k, fetch(k))
        return 0
    if a.cmd == "compute":
        out = run_and_cache(a.site, B=a.B, R_null=a.R_null, R_planted=a.R_planted, workers=a.workers,
                            log=lambda m: print(m, flush=True))
        print(f"{a.site}: {out['seconds']:.0f}s, cached at {cache_path(a.site)}")
        return 0
    if a.cmd == "report":
        write_report(Path(a.out))
        print("wrote", a.out)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())
