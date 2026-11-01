"""Wiki-RfA and Bitcoin OTC/Alpha: the tie-CONVERSION half of v0.1's n = 3 test on explicit-sign data.

Prior work: docs/prior-work/117-modern-signed-and-split-datasets.md (D610), sections 3.3 (wiki-RfA) and
3.4 (Bitcoin); the 16 directed triad types and the balance / status predictions of docs/prior-work/106
section 1.2 (Leskovec, Huttenlocher & Kleinberg 2010); the Newcomb run this continues,
sim/results/newcomb_n3.md and models/newcomb.py.  Ledger ids are the lines of docs/ledger.jsonl with
source "117 ..." (L4547-L4668, L4854, L4855): wiki-RfA file, counts and year totals L4561-L4563;
repeat candidacies re-sign ties L4564 (dup L4855); Bitcoin files, counts, projection, closure table and
product rule L4567-L4579; Bitcoin cannot test conversion L4571, L4580.  Terms: none stated by SNAP for
either dataset (117 section 3.3; L4567); the wiki-RfA comments are Wikipedia text (CC BY-SA): the parser streams
past them and stores none; user names are replaced by integers on load and never written out.

WHAT IS TESTED (v0.1 section 7, n = 3, "v0's hypothesis, not a source's"): in longitudinal signed
triads the one-negative triangle must convert to a balanced triangle faster than the all-negative
one, and if conversion runs at the null rate (4.2b)/(5.1) is refuted.  Newcomb (ranks recoded to
signs, one group, 17 men) left this undecided; wiki-RfA is the first explicit-sign file with the same
ordered pair re-signed: a voter (u) rates a candidate (v) at a candidacy, and again at a later
candidacy of the same candidate, sometimes with the opposite sign [L4564].

OBJECTS.
 * Vote: (voter, candidate, sign, time).  Neutral votes (VOT 0) carry no sign and are dropped, as in
   the SNAP network statistics and in 117's recount.  Votes with an empty voter field (1,661) and a
   voter voting on himself (103) are dropped.
 * Candidacy: one election.  The file's year and result do not identify it (a candidate can fail twice in a year,
   and 18 elections carry BOTH outcome labels, in 15 cases as a complete copy (equal numbers of votes under each label),
   which grouping by result would turn into a second candidacy and 618 zero-day "re-votes"), so a candidate's dated votes are split wherever there is a gap of
   more than 14 days (GAP_DAYS; an RfA runs about 7 days, the median span of the clusters is 6.3 days).  A cluster's
   result is the majority label of its votes, 0 (unknown) on a tie.  A cluster of at most 3 votes next to one of at
   least 10 is a stray (a mis-dated or late signature) and is merged into the nearest big cluster, at that cluster's
   median time.  An undated vote (9,367; the file has no DAT) goes to its candidacy, or to the one whose year
   matches YEA, and is placed at the candidacy's median time; one it cannot place is dropped (467).  A voter's
   several votes in one candidacy (1,186, mostly the duplicated elections) are collapsed to the last.
 * Transition: two consecutive non-neutral votes by one voter on one candidate at different
   candidacies.  A CONVERSION is a transition whose sign differs (-> + or + ->-).  117's "677" is the
   first-versus-last comparison of each pair's first vote per YEAR [L4564]; every sign change between
   consecutive candidacies is counted here, which is more (resign_counts_117 reproduces 117's 519 and 158).
 * Context of a transition u -> v: every w tied to both u and v before the candidacy began (the
   votes dated before the first vote of the new candidacy, so that the network is the one the
   voter walked into and not the crowd's concurrent reactions), with the latest earlier sign of
   each directed tie.  One INSTANCE per (transition, w, direction of the u-w tie, direction of the
   w-v tie): the 16 types of LHK are [F|B][F|B][p|m][p|m], F = u to w (first letter) / w to v (second
   letter), B = the reverse, p / m = the signs of the u-w and w-v ties [106 section 1.2].  The third
   tie, u -> v, is the one that converts, so every triple is judged before (old sign) and after (new
   sign).  A reciprocated tie contributes an instance per direction.
 * Balance of a triple: strict (Heider, Cartwright-Harary) = an even number of negative ties;
   weak (Davis; the primary reading here, v0 section 4.2 and 084) = no triple with exactly one
   negative tie.  FIX = a converting instance that goes from weakly unbalanced to balanced, BREAK = from
   weakly balanced to unbalanced, the rest (all-negative <-> two-negative) are neutral under weak
   balance.  Flipping any tie of a one-negative triple makes it balanced, so FIX is exactly "the
   triple was one-negative", whichever tie converts.
 * Directed D&K types (Newcomb, 104): for the three orientations in which the ties form an ordered
   triple i->j, j->k, i->k the type is named by the signs in that order (L = +, D = -).  With
   u -> v as the converting tie: FF is (u->w, w->v, u->v) so the converting tie is the third
   ("completion") tie; FB is (u->v, v->w, u->w) so it is the FIRST tie; BF is (w->u, u->v, w->v)
   so it is the SECOND.  BB is a directed cycle and has no D&K type.  "First tie negative" is DLL.

STATISTICS (pooled over instances; triples share ties, so the permutation nulls, not a binomial, carry the inference,
as in the Newcomb run).
 * H1 share_w = FIX / (FIX + BREAK) over the converting instances: of the weak-balance changes, the fraction that
   repair a one-negative triple.  share_s is the same for strict balance (the triple was odd-negative).  The event-level
   mean (each conversion weighs 1) is the check against heavy re-voters.
 * H2 hazard by class: the conversion rate of re-votes whose triple was 0, 1, 2 or 3 negative before (r0..r3), and the
   contrasts r1 - r3 (v0 section 7: one-negative faster than all-negative) and r1 - r(weakly balanced classes).
 * H3 the D&K first-tie table: conversion count and rate per (type before, orientation) for LLD, LDL and DLL, the repair
   (the converting tie is the lone negative one) and join (a positive tie turns negative) rates, contrasts of DLL against
   LDL, and the split of joins by whether the lone negative tie touches the converting voter.
 * I the interaction contrast: the double difference of conversion rates over the four context cells, in which the voter's
   generosity (the u-w sign) and the candidate's reception by the third party (the w-v sign) cancel, so that what is left
   is the product of signs that only balance (or homophily of judgement) predicts.

NULLS (10,000 draws; p = (1 + #{null >= obs}) / (B + 1), and the lower tail alongside).  Three families.
 * "voter_uncond" (the brief's null): signs shuffled within voter, over all of a voter's non-neutral votes, timestamps and
   targets kept; the conversions are RE-DETERMINED from the shuffled signs.  Its mix of + ->- and - -> + is about even;
   the observed conversions are 79% - -> + (a candidate who failed and ran again was usually judged better the second
   time), and in a mostly positive context that direction mix alone moves share_w.
 * "ctx_*" (conversions held): the observed old and new sign of every re-vote are kept and only the signs of the context
   ties are shuffled, within voter, within voter and candidacy outcome, or within candidacy.  They compare the
   converters' triples with random triples, so they are blind to the static depletion of one-negative triples (the
   (a) half of the test).
 * "ev_*" (network held; Newcomb's conditional design): contexts and old signs stay as observed and the conversion
   indicator is permuted among the re-votes of a stratum (same new candidacy and old sign; same old and new candidacy;
   same voter and old sign; the first with terciles of the number of triples, or of the voter's share of positive
   votes), so every pre-state class size is fixed and only WHO CONVERTS is random.  This is the dynamic test; an excess
   over it is conversion aimed at tension within comparable re-votes, and it cannot separate balance from following
   the crowd, reciprocity, status or rivalry [L4511, L4512].

FIXED BEFORE ANY NULL WAS COMPUTED.  The candidacy rule (14 days, strays), the context cut-off (first vote of the new
candidacy), weak balance as the primary reading, H1 under the brief's unconditional "voter" null as the headline test, and
10,000 draws.  Seen before any null: the direction mix (952 -> + and 249 + ->-, counted while characterising the 677; 951
and 250 after the duplicated elections were merged) and the observed pooled shares.  POST HOC, in this order: the
conditional context shuffles (on the direction mix); the event-permutation family (when the context shuffles disagreed with
each other and with the brief's, and because the hazard statistic needs the pre-state class sizes held fixed, as Newcomb's
conditional null held the start wave); the interaction contrast and the orientation split (on seeing that the FF cell rates
carry no product structure); the voter-generosity and number-of-triples terciles; the incidence split of the join cells.
Sensitivities (cut-off at the vote, no co-voters, contexts at most two years old, by orientation, by era, undated dropped)
are secondary; none replaces the headline.  Nothing was dropped for disagreeing.

CAVEATS BUILT INTO THE DESIGN (the report repeats them): a vote is a one-shot public evaluation of a candidacy, not a
friendship; the triple's other two ties are votes too, cast at other candidacies; times are minutes at best and a
candidacy is a week, so "before" is by candidacy; the voters who re-vote are 3% of pairs (selection), and candidates re-run
after failing (selection of the ties that can convert at all); only the voter's tie to the candidate is re-observed, so
tension resolved through the other two ties is invisible.

BITCOIN (formation only: no ordered pair is rated twice [L4571, L4580]).  The undirected projection signs and times each
pair by its earliest rating; a triangle is "balanced" when the third edge has the product of the first two, i.e. an even
number of negative ties.  Nulls: all pair signs permuted (117's), ratings shuffled within rater, within ratee.
"""
from __future__ import annotations

import collections
import dataclasses
import datetime
import gzip
import hashlib
import multiprocessing as mp
import os
import re
import urllib.request
import zlib
from pathlib import Path
from typing import Iterable

import numpy as np

SIM_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = SIM_DIR / "data"
SEED = 20261101
N_DRAWS = 10_000
GAP_DAYS = 14.0
STRAY_MAX = 3
STRAY_MAIN_MIN = 10
FETCH_CMD = "cd sim && ~/.local/bin/uv run python -m models.wikirfa_report fetch"


# ------------------------------------------------------------------ data sources

@dataclasses.dataclass(frozen=True)
class Source:
    key: str
    url: str
    path: Path
    sha256: str
    size: int


WIKIRFA = Source(
    "wikirfa", "https://snap.stanford.edu/data/wiki-RfA.txt.gz", DATA_DIR / "wiki-rfa" / "wiki-RfA.txt.gz",
    "88d53196fb2564a2e20286dbba818832f718cc352bb181a2101d23d2556f0862", 14_936_383)
OTC = Source(
    "otc", "https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz", DATA_DIR / "bitcoin" / "soc-sign-bitcoinotc.csv.gz",
    "6424ac981dad3a019f697fc1b9fcd85c19d8d9f039797758e9ffb6fea100c373", 397_258)
ALPHA = Source(
    "alpha", "https://snap.stanford.edu/data/soc-sign-bitcoinalpha.csv.gz", DATA_DIR / "bitcoin" / "soc-sign-bitcoinalpha.csv.gz",
    "3a178611b9c2f39c9a0dc75936f28557317f1733319b49da4838232b3757cd76", 149_480)
SOURCES = {s.key: s for s in (WIKIRFA, OTC, ALPHA)}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def fetch(src: Source, timeout: float = 300.0) -> Path:
    """Download one SNAP file for LOCAL USE ONLY into the git-ignored sim/data/.  The recorded sha256 is
    checked before anything is written; sends no identity beyond urllib's default agent."""
    with urllib.request.urlopen(src.url, timeout=timeout) as resp:
        data = resp.read()
    if hashlib.sha256(data).hexdigest() != src.sha256:
        raise ValueError(f"{src.url}: sha256 differs from the recorded {src.sha256}; nothing written")
    src.path.parent.mkdir(parents=True, exist_ok=True)
    tmp = src.path.with_name(src.path.name + ".part")
    tmp.write_bytes(data)
    tmp.replace(src.path)
    return src.path


def require(src: Source, verify: bool = True) -> Path:
    if not src.path.exists():
        raise FileNotFoundError(
            f"{src.path} is missing: the file is local-use-only and is not in the repo. Fetch it with: {FETCH_CMD}")
    if verify and sha256_of(src.path) != src.sha256:
        raise ValueError(f"{src.path} does not match the recorded sha256 {src.sha256}")
    return src.path


# ------------------------------------------------------------------ parsing the wiki-RfA file

_MONTHS = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
           "november", "december")
_MONTH_NUM = {m[:3]: i + 1 for i, m in enumerate(_MONTHS)}
_DAT = re.compile(r"^(\d\d):(\d\d), (\d{1,2}) ([A-Za-z]+) (\d{4})$")


def parse_dat(s: str) -> tuple[float, str]:
    """'19:53, 25 January 2013' -> (proleptic ordinal day + fraction of the day, 'ok').  A month typed
    with a slip ('Mya', 'Julu', 'Janry' occur once each) is matched on its first three letters, with
    'Mya' read as May, and reported as 'repaired'.  An empty field is 'empty'; a date that does not exist
    (an hour of 31 occurs once) is 'invalid'; both give NaN."""
    if not s:
        return float("nan"), "empty"
    m = _DAT.match(s)
    if m is None:
        return float("nan"), "invalid"
    hh, mm, dd, mon, yy = m.groups()
    mon = mon.lower()
    status = "ok" if (mon in _MONTHS or mon in _MONTH_NUM) else "repaired"
    key = "may" if mon == "mya" else mon[:3]
    if key not in _MONTH_NUM or int(hh) > 23 or int(mm) > 59:
        return float("nan"), "invalid"
    try:
        day = datetime.date(int(yy), _MONTH_NUM[key], int(dd)).toordinal()
    except ValueError:
        return float("nan"), "invalid"
    return day + (int(hh) * 60 + int(mm)) / 1440.0, status


@dataclasses.dataclass
class RawVotes:
    """One row per record of the file, in file order.  voter is -1 where the field is empty."""
    voter: np.ndarray
    cand: np.ndarray
    vote: np.ndarray       # -1 oppose, 0 neutral, +1 support
    res: np.ndarray        # -1 candidate rejected, +1 accepted
    yea: np.ndarray        # year in which the election started (the file's YEA)
    t: np.ndarray          # day number, NaN where undated
    n_users: int
    notes: dict


def parse_wikirfa(lines: Iterable[str]) -> RawVotes:
    """Parse the SNAP record format (blank-line separated SRC/TGT/VOT/RES/YEA/DAT/TXT lines).  The TXT
    comment is Wikipedia text and is skipped without being stored; names become integers."""
    names: dict[str, int] = {}

    def uid(s: str) -> int:
        return names.setdefault(s, len(names))

    voter, cand, vote, res, yea, tm = [], [], [], [], [], []
    status = collections.Counter()
    rec: dict[str, str] = {}

    def flush():
        if not rec:
            return
        for k in ("TGT", "VOT", "RES", "YEA"):
            if k not in rec or rec[k] == "":
                raise ValueError(f"record without {k}: {rec}")
        v = int(rec["VOT"])
        if v not in (-1, 0, 1):
            raise ValueError(f"unexpected vote {v}")
        voter.append(uid(rec["SRC"]) if rec.get("SRC") else -1)
        cand.append(uid(rec["TGT"]))
        vote.append(v)
        res.append(int(rec["RES"]))
        yea.append(int(rec["YEA"]))
        t, st = parse_dat(rec.get("DAT", ""))
        tm.append(t)
        status[st] += 1
        rec.clear()

    for line in lines:
        line = line.rstrip("\r\n")
        if not line:
            flush()
            continue
        key, _, val = line.partition(":")
        if key in ("SRC", "TGT", "VOT", "RES", "YEA", "DAT"):
            rec[key] = val
    flush()
    voter_a = np.array(voter, dtype=np.int32)
    notes = {
        "n_records": len(voter_a), "n_users": len(names), "n_empty_voter": int((voter_a < 0).sum()),
        "dat_ok": status["ok"], "dat_repaired": status["repaired"], "dat_empty": status["empty"],
        "dat_invalid": status["invalid"],
    }
    return RawVotes(voter_a, np.array(cand, dtype=np.int32), np.array(vote, dtype=np.int8),
                    np.array(res, dtype=np.int8), np.array(yea, dtype=np.int16), np.array(tm, dtype=np.float64),
                    len(names), notes)


def load_wikirfa(path: Path | str | None = None, verify: bool = True) -> RawVotes:
    p = require(WIKIRFA, verify) if path is None else Path(path)
    with gzip.open(p, "rt", encoding="utf-8", newline="") as fh:
        return parse_wikirfa(fh)


def resign_counts_117(raw: RawVotes) -> dict:
    """117's convention [L4564]: ordered pairs with a named voter, file order, the FIRST vote of the pair
    in each YEA, then the first and last NON-NEUTRAL of those year-first votes.  Returns the counts of
    (first sign, last sign) over the pairs that vote in more than one year, the number of such pairs, the
    number of pairs with more than one vote and the votes in them, and the number of sign changes."""
    seen = collections.defaultdict(list)
    for i in range(len(raw.voter)):
        if raw.voter[i] >= 0:
            seen[(int(raw.voter[i]), int(raw.cand[i]))].append(i)
    out = collections.Counter()
    multi_year = n_pairs = n_votes = 0
    for idx in seen.values():
        if len(idx) < 2:
            continue
        n_pairs += 1
        n_votes += len(idx)
        by_year: dict[int, int] = {}
        for i in idx:
            by_year.setdefault(int(raw.yea[i]), int(raw.vote[i]))
        if len(by_year) < 2:
            continue
        multi_year += 1
        seq = [by_year[y] for y in sorted(by_year) if by_year[y] != 0]
        if len(seq) >= 2:
            out[(seq[0], seq[-1])] += 1
    return {"cells": dict(out), "multi_year_pairs": multi_year, "pairs_gt1_vote": n_pairs, "votes_in_those": n_votes,
            "changes": out[(-1, 1)] + out[(1, -1)]}


# ------------------------------------------------------------------ candidacies

@dataclasses.dataclass
class Candidacies:
    cy: np.ndarray        # per raw vote, -1 where unplaced
    t_eff: np.ndarray     # per raw vote: own time if dated and in its cluster, else the candidacy median
    start: np.ndarray     # per candidacy: first dated vote (July 1 of YEA where no vote is dated)
    median: np.ndarray
    cand: np.ndarray
    res: np.ndarray
    notes: dict


def assign_candidacies(raw: RawVotes, gap_days: float = GAP_DAYS) -> Candidacies:
    """Group a candidate's dated votes into candidacies at gaps of more than gap_days.  The grouping is by
    CANDIDATE, not by (candidate, result): in 18 clusters the file holds the whole election twice, once
    labelled accepted and once rejected (92 votes each, say), and grouping by result would turn the copy into a
    second candidacy and its votes into 618 'repeat votes' with a zero-day gap.  A cluster's result is the
    majority label of its votes, 0 where the labels tie.  See the module docstring for strays and undated votes."""
    n = len(raw.cand)
    cy = np.full(n, -1, dtype=np.int32)
    t_eff = raw.t.copy()
    start: list[float] = []
    median: list[float] = []
    cand_of: list[int] = []
    res_of: list[int] = []
    by_cand: dict[int, list[int]] = {}
    for i in range(n):
        by_cand.setdefault(int(raw.cand[i]), []).append(i)
    notes = collections.Counter()
    notes["n_candidates"] = len(by_cand)

    def new_cy(c, r, s_, m):
        start.append(s_)
        median.append(m)
        cand_of.append(c)
        res_of.append(r)
        return len(start) - 1

    def majority(votes_res: np.ndarray) -> int:
        d = int((votes_res > 0).sum()) - int((votes_res < 0).sum())
        return 1 if d > 0 else (-1 if d < 0 else 0)

    for c, idx_l in by_cand.items():
        idx = np.array(idx_l)
        dated = idx[~np.isnan(raw.t[idx])]
        undated = idx[np.isnan(raw.t[idx])]
        ids: list[int] = []
        if len(dated):
            dated = dated[np.argsort(raw.t[dated], kind="stable")]
            parts = np.split(dated, np.nonzero(np.diff(raw.t[dated]) > gap_days)[0] + 1)
            if len(parts) > 1:
                notes["n_candidates_with_several_candidacies"] += 1
            sizes = [len(p) for p in parts]
            main = [k for k, sz in enumerate(sizes) if sz >= STRAY_MAIN_MIN]
            stray = [k for k, sz in enumerate(sizes) if sz <= STRAY_MAX] if main else []
            med = [float(np.median(raw.t[p])) for p in parts]
            cid: dict[int, int] = {}
            for k in range(len(parts)):
                if k in stray:
                    continue
                r = majority(raw.res[parts[k]])
                if (raw.res[parts[k]] > 0).any() and (raw.res[parts[k]] < 0).any():
                    notes["n_clusters_with_both_labels"] += 1
                    notes["n_clusters_label_tie"] += int(r == 0)
                cid[k] = new_cy(c, r, float(raw.t[parts[k]].min()), med[k])
                cy[parts[k]] = cid[k]
                ids.append(cid[k])
            for k in stray:
                nearest = min(main, key=lambda m: abs(med[m] - med[k]))
                cy[parts[k]] = cid[nearest]
                t_eff[parts[k]] = median[cid[nearest]]
                notes["n_stray_votes"] += len(parts[k])
                notes["n_stray_clusters"] += 1
        if len(undated):
            if not ids:
                notes["n_undated_only_candidates"] += 1
                for y in sorted(set(int(v) for v in raw.yea[undated])):
                    for r in (-1, 1):
                        sel = undated[(raw.yea[undated] == y) & (raw.res[undated] == r)]
                        if len(sel):
                            x = float(datetime.date(y, 7, 1).toordinal())
                            k = new_cy(c, r, x, x)
                            cy[sel] = k
                            t_eff[sel] = x
            elif len(ids) == 1:
                cy[undated] = ids[0]
                t_eff[undated] = median[ids[0]]
            else:
                years = {k: datetime.date.fromordinal(int(start[k])).year for k in ids}
                for i in undated:
                    y, r = int(raw.yea[i]), int(raw.res[i])
                    hit = [k for k in ids if years[k] == y] or [k for k in ids if abs(years[k] - y) == 1 and res_of[k] == r]
                    if len(hit) > 1:
                        hit = [k for k in hit if res_of[k] == r]
                    if len(hit) == 1:
                        cy[i] = hit[0]
                        t_eff[i] = median[hit[0]]
                    else:
                        notes["n_unplaced_undated"] += 1
    notes["n_candidacies"] = len(start)
    return Candidacies(cy, t_eff, np.array(start), np.array(median), np.array(cand_of, dtype=np.int32),
                       np.array(res_of, dtype=np.int8), dict(notes))


# ------------------------------------------------------------------ the vote table, transitions, contexts

@dataclasses.dataclass
class VoteTable:
    """Non-neutral votes, one row per (voter, candidate, candidacy), sorted by (pair, time, file order)."""
    voter: np.ndarray
    cand: np.ndarray
    sign: np.ndarray       # int8 +1 / -1
    t: np.ndarray
    cy: np.ndarray
    res: np.ndarray        # outcome of the vote's candidacy
    cy_start: np.ndarray
    cy_res: np.ndarray
    cy_cand: np.ndarray
    n_users: int
    notes: dict


def build_vote_table(raw: RawVotes, cands: Candidacies) -> VoteTable:
    ok = (raw.voter >= 0) & (cands.cy >= 0) & (raw.vote != 0) & (raw.voter != raw.cand)
    notes = {
        "n_records": len(raw.voter),
        "n_empty_voter": int((raw.voter < 0).sum()),
        "n_neutral": int((raw.vote == 0).sum()),
        "n_self": int(((raw.voter == raw.cand) & (raw.voter >= 0)).sum()),
        "n_unplaced": int((cands.cy < 0).sum()),
    }
    idx = np.nonzero(ok)[0]
    notes["n_usable"] = len(idx)
    n_users = raw.n_users
    pair = raw.voter[idx].astype(np.int64) * n_users + raw.cand[idx]
    cy = cands.cy[idx]
    o = np.lexsort((idx, cands.t_eff[idx], cy, pair))        # pair, candidacy, time, file order
    idx, pair, cy = idx[o], pair[o], cy[o]
    keep = np.ones(len(idx), dtype=bool)
    keep[:-1] = ~((pair[:-1] == pair[1:]) & (cy[:-1] == cy[1:]))     # the last vote of the voter in the candidacy
    notes["n_collapsed_within_candidacy"] = int((~keep).sum())
    idx, pair = idx[keep], pair[keep]
    t = cands.t_eff[idx]
    o = np.lexsort((idx, t, pair))
    idx, pair, t = idx[o], pair[o], t[o]
    cy = cands.cy[idx]
    vt = VoteTable(
        voter=raw.voter[idx].astype(np.int32), cand=raw.cand[idx].astype(np.int32), sign=raw.vote[idx].astype(np.int8),
        t=t, cy=cy.astype(np.int32), res=cands.res[cy], cy_start=cands.start, cy_res=cands.res, cy_cand=cands.cand,
        n_users=n_users, notes=notes)
    vt.notes["n_rows"] = len(idx)
    return vt


@dataclasses.dataclass
class Transitions:
    prev: np.ndarray      # row of the earlier vote
    cur: np.ndarray       # row of the later vote (the converting one, when the signs differ)
    cutoff: np.ndarray    # context time: only votes dated strictly before it are context


def build_transitions(vt: VoteTable, cutoff: str = "start") -> Transitions:
    key = vt.voter.astype(np.int64) * vt.n_users + vt.cand
    prev = np.nonzero(key[:-1] == key[1:])[0].astype(np.int32)
    cur = prev + 1
    if cutoff == "start":
        c = vt.cy_start[vt.cy[cur]]
    elif cutoff == "vote":
        c = vt.t[cur]
    else:
        raise ValueError(cutoff)
    return Transitions(prev, cur.astype(np.int32), c)


ORIENT = ("FF", "FB", "BF", "BB")


@dataclasses.dataclass
class Contexts:
    tr: np.ndarray        # transition index
    o: np.ndarray         # orientation 0 FF, 1 FB, 2 BF, 3 BB  (2 * [first letter B] + [second letter B])
    e1: np.ndarray        # row of the latest earlier vote on the u-w tie
    e2: np.ndarray        # row of the latest earlier vote on the w-v tie
    w: np.ndarray         # the third node


def _group_edges(a: np.ndarray, b: np.ndarray, first_t: np.ndarray):
    """For each node a: its partners b sorted by the time of the first vote on the tie."""
    o = np.lexsort((first_t, a))
    a_s, b_s, f_s = a[o], b[o], first_t[o]
    nodes, first = np.unique(a_s, return_index=True)
    ends = np.concatenate([first[1:], [len(a_s)]])
    return {int(x): (b_s[s:e], f_s[s:e]) for x, s, e in zip(nodes, first, ends)}


def build_contexts(vt: VoteTable, trans: Transitions) -> Contexts:
    n = len(vt.voter)
    N = vt.n_users
    key = vt.voter.astype(np.int64) * N + vt.cand
    starts = np.concatenate([[0], np.nonzero(key[:-1] != key[1:])[0] + 1])
    ends = np.concatenate([starts[1:], [n]])
    edge = {int(key[s]): (int(s), int(e)) for s, e in zip(starts, ends)}
    first_t = vt.t[starts]
    out_nb = _group_edges(vt.voter[starts], vt.cand[starts], first_t)    # u -> partners (u voted on them)
    in_nb = _group_edges(vt.cand[starts], vt.voter[starts], first_t)     # v <- partners (voted on v)
    empty = (np.empty(0, dtype=np.int32), np.empty(0))

    def latest(a: int, b: int, cut: float) -> int:
        s, e = edge[a * N + b]
        k = int(np.searchsorted(vt.t[s:e], cut, side="left"))
        return s + k - 1

    def nbrs(table, x: int, cut: float) -> set:
        a, f = table.get(x, empty)
        return set(a[: int(np.searchsorted(f, cut, side="left"))].tolist())

    tr_l, o_l, e1_l, e2_l, w_l = [], [], [], [], []
    for t in range(len(trans.cur)):
        u, v, cut = int(vt.voter[trans.cur[t]]), int(vt.cand[trans.cur[t]]), float(trans.cutoff[t])
        ou, iu = nbrs(out_nb, u, cut), nbrs(in_nb, u, cut)        # u voted on w | w voted on u
        ov, iv = nbrs(out_nb, v, cut), nbrs(in_nb, v, cut)        # v voted on w | w voted on v
        common = (ou | iu) & (ov | iv)
        common.discard(u)
        common.discard(v)
        for w in common:
            first = []
            if w in ou:
                first.append((0, latest(u, w, cut)))
            if w in iu:
                first.append((1, latest(w, u, cut)))
            second = []
            if w in iv:
                second.append((0, latest(w, v, cut)))
            if w in ov:
                second.append((1, latest(v, w, cut)))
            for a, r1 in first:
                for b, r2 in second:
                    tr_l.append(t)
                    o_l.append(2 * a + b)
                    e1_l.append(r1)
                    e2_l.append(r2)
                    w_l.append(w)
    ctx = Contexts(np.array(tr_l, dtype=np.int32), np.array(o_l, dtype=np.int8), np.array(e1_l, dtype=np.int32),
                   np.array(e2_l, dtype=np.int32), np.array(w_l, dtype=np.int32))
    return ctx


@dataclasses.dataclass
class Network:
    vt: VoteTable
    trans: Transitions
    ctx: Contexts

    @property
    def sign(self) -> np.ndarray:
        return self.vt.sign

    def old_new(self) -> tuple[np.ndarray, np.ndarray]:
        return self.vt.sign[self.trans.prev], self.vt.sign[self.trans.cur]

    def restrict(self, mask: np.ndarray) -> "Network":
        """The same votes and transitions with only the instances where mask is true."""
        c = self.ctx
        return Network(self.vt, self.trans, Contexts(c.tr[mask], c.o[mask], c.e1[mask], c.e2[mask], c.w[mask]))


def build_network(raw: RawVotes, cands: Candidacies | None = None, cutoff: str = "start") -> Network:
    cands = assign_candidacies(raw) if cands is None else cands
    vt = build_vote_table(raw, cands)
    vt.notes.update({"cands_" + k: v for k, v in cands.notes.items()})
    trans = build_transitions(vt, cutoff)
    return Network(vt, trans, build_contexts(vt, trans))


# ------------------------------------------------------------------ balance logic (pure, no data)

def n_negative(*signs) -> int:
    return sum(1 for s in signs if s < 0)


def weakly_unbalanced(neg: int) -> bool:
    """Davis: only the triple with exactly one negative tie is forbidden (084; v0 section 4.2)."""
    return neg == 1


def strictly_unbalanced(neg: int) -> bool:
    """Heider / Cartwright-Harary: an odd number of negative ties (v0 (4.2b))."""
    return neg % 2 == 1


def balance_prediction(s1: int, s2: int) -> int:
    """LHK's f_balance: the sign of u -> v that gives the triangle an even number of negative ties."""
    return s1 * s2


def status_prediction(o: int, s1: int, s2: int) -> int:
    """LHK's f_status [106 section 1.2]: flip the ties to run u -> w and w -> v (a reversed tie changes sign),
    predict sign(s(u,w) + s(w,v)); 0 where they cancel (8 of the 16 types)."""
    a = s1 if o in (0, 1) else -s1       # first letter F: u -> w kept; B: w -> u reversed
    b = s2 if o in (0, 2) else -s2       # second letter F: w -> v kept; B: v -> w reversed
    return int(np.sign(a + b))


def triad_type(o: int, s1: int, s2: int) -> str:
    """One of LHK's 16 types, e.g. 'FBmp': u negative to w and v positive to w."""
    return ORIENT[o] + ("p" if s1 > 0 else "m") + ("p" if s2 > 0 else "m")


FOCAL_POSITION = {0: 3, 1: 1, 2: 2}      # position of u -> v in D&K's ordered triple (i->j, j->k, i->k)


def dk_type(o: int, s1: int, s2: int, f: int) -> str | None:
    """D&K's type (L = +, D = -) of the ordered triple, with f the sign of the converting tie u -> v;
    None for the cyclic orientation BB."""
    ch = lambda s: "L" if s > 0 else "D"      # noqa: E731
    if o == 0:
        return ch(s1) + ch(s2) + ch(f)
    if o == 1:
        return ch(f) + ch(s2) + ch(s1)
    if o == 2:
        return ch(s1) + ch(f) + ch(s2)
    return None


DK_TYPES = ("LLL", "LLD", "LDL", "LDD", "DLL", "DLD", "DDL", "DDD")
DK_UNBALANCED = ("LLD", "LDL", "DLL")


# ------------------------------------------------------------------ cells: every statistic is a function of these

_c = np.arange(64)
CELL_O = (_c // 16).astype(np.int8)
CELL_S1 = np.where((_c >> 3) & 1, 1, -1).astype(np.int8)
CELL_S2 = np.where((_c >> 2) & 1, 1, -1).astype(np.int8)
CELL_OLD = np.where((_c >> 1) & 1, 1, -1).astype(np.int8)
CELL_NEW = np.where(_c & 1, 1, -1).astype(np.int8)
CELL_CHG = CELL_OLD != CELL_NEW
CELL_NB = ((CELL_S1 < 0).astype(int) + (CELL_S2 < 0) + (CELL_OLD < 0))
CELL_NA = ((CELL_S1 < 0).astype(int) + (CELL_S2 < 0) + (CELL_NEW < 0))
CELL_DK_BEFORE = [dk_type(int(o), int(a), int(b), int(f)) for o, a, b, f in zip(CELL_O, CELL_S1, CELL_S2, CELL_OLD)]
CELL_DK_AFTER = [dk_type(int(o), int(a), int(b), int(f)) for o, a, b, f in zip(CELL_O, CELL_S1, CELL_S2, CELL_NEW)]
CELL_TYPE = [triad_type(int(o), int(a), int(b)) for o, a, b in zip(CELL_O, CELL_S1, CELL_S2)]
FIXW = CELL_CHG & (CELL_NB == 1)
BRKW = CELL_CHG & (CELL_NB != 1) & (CELL_NA == 1)
FIXS = CELL_CHG & (CELL_NB % 2 == 1)
BRKS = CELL_CHG & (CELL_NB % 2 == 0)
UP = CELL_CHG & (CELL_OLD < 0)           # a negative vote became positive
DOWN = CELL_CHG & (CELL_OLD > 0)         # a positive vote became negative


def cell_codes(o, s1, s2, old, new) -> np.ndarray:
    return (o.astype(np.int16) * 16 + (s1 > 0) * 8 + (s2 > 0) * 4 + (old > 0) * 2 + (new > 0)).astype(np.int16)


def cell_counts(ctx: Contexts, s1, s2, old_t, new_t) -> np.ndarray:
    code = cell_codes(ctx.o, s1, s2, old_t[ctx.tr], new_t[ctx.tr])
    return np.bincount(code, minlength=64)


def _msum(cells, mask):
    return cells @ mask.astype(np.int64)


def _ratio(a, b):
    a = np.asarray(a, dtype=np.float64)
    b = np.asarray(b, dtype=np.float64)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where(b > 0, a / b, np.nan)


def derived(cells: np.ndarray) -> dict:
    """All instance-pooled statistics from the 64 cell counts; accepts (64,) or (B, 64)."""
    d = {}
    d["n_inst"] = cells.sum(-1)
    d["n_chg"] = _msum(cells, CELL_CHG)
    d["fix_w"], d["brk_w"] = _msum(cells, FIXW), _msum(cells, BRKW)
    d["share_w"] = _ratio(d["fix_w"], d["fix_w"] + d["brk_w"])
    d["fix_s"], d["brk_s"] = _msum(cells, FIXS), _msum(cells, BRKS)
    d["share_s"] = _ratio(d["fix_s"], d["fix_s"] + d["brk_s"])
    for name, m in (("up", UP), ("down", DOWN)):
        f, b = _msum(cells, FIXW & m), _msum(cells, BRKW & m)
        d[f"fix_w_{name}"], d[f"brk_w_{name}"] = f, b
        d[f"share_w_{name}"] = _ratio(f, f + b)
        fs, bs = _msum(cells, FIXS & m), _msum(cells, BRKS & m)
        d[f"share_s_{name}"] = _ratio(fs, fs + bs)
        d[f"n_chg_{name}"] = _msum(cells, m)
    for k in range(4):
        n = _msum(cells, CELL_NB == k)
        c = _msum(cells, (CELL_NB == k) & CELL_CHG)
        d[f"n{k}"], d[f"k{k}"], d[f"r{k}"] = n, c, _ratio(c, n)
    d["r1_minus_r3"] = d["r1"] - d["r3"]
    bal_n, bal_k = d["n0"] + d["n2"] + d["n3"], d["k0"] + d["k2"] + d["k3"]
    d["r_bal"] = _ratio(bal_k, bal_n)
    d["r1_minus_rbal"] = d["r1"] - d["r_bal"]
    return d


def dk_table(cells: np.ndarray) -> dict:
    """(type before, orientation) -> (instances, conversions); orientations FF FB BF only."""
    out = {}
    for typ in DK_TYPES:
        for o in (0, 1, 2):
            m = (CELL_O == o) & np.array([t == typ for t in CELL_DK_BEFORE])
            out[(typ, o)] = (_msum(cells, m), _msum(cells, m & CELL_CHG))
    return out


def first_tie_stats(cells: np.ndarray) -> dict:
    """The D&K first-tie table, from the 64 cells (works for (64,) and (B, 64)).  For each of the three one-negative
    types (LLD, LDL, DLL) and each transitive orientation: instances n, conversions k, rate.  REPAIR = the converting
    tie is the lone negative one (a -> + conversion; FF-LLD, BF-LDL, FB-DLL); JOIN = it is a positive tie and
    turns negative (+ ->-; the other six cells).  Per type the repair rate and the pooled join rate, the share of
    the three types among converting one-negative instances, and the contrasts of the DLL (first tie negative)
    type against LDL and against LLD and LDL together."""
    out = {}
    nk = dk_table(cells)
    repair_cell = {"LLD": 0, "LDL": 2, "DLL": 1}              # orientation in which the converting tie is the negative one
    for typ in DK_UNBALANCED:
        for o in (0, 1, 2):
            n, k = nk[(typ, o)]
            out[f"n_{typ}_{ORIENT[o]}"], out[f"k_{typ}_{ORIENT[o]}"], out[f"rate_{typ}_{ORIENT[o]}"] = n, k, _ratio(k, n)
        n_rep, k_rep = nk[(typ, repair_cell[typ])]
        n_join = sum(nk[(typ, o)][0] for o in (0, 1, 2) if o != repair_cell[typ])
        k_join = sum(nk[(typ, o)][1] for o in (0, 1, 2) if o != repair_cell[typ])
        out[f"repair_{typ}"], out[f"join_{typ}"] = _ratio(k_rep, n_rep), _ratio(k_join, n_join)
        out[f"k_repair_{typ}"], out[f"k_join_{typ}"] = k_rep, k_join
        out[f"n_repair_{typ}"], out[f"n_join_{typ}"] = n_rep, n_join
    k_tot = sum(out[f"k_repair_{t}"] + out[f"k_join_{t}"] for t in DK_UNBALANCED)
    for typ in DK_UNBALANCED:
        out[f"comp_{typ}"] = _ratio(out[f"k_repair_{typ}"] + out[f"k_join_{typ}"], k_tot)
    inc = (("DLL", 0), ("DLL", 2), ("LLD", 1))       # the lone negative tie touches the converting voter u (u->w, w->u)
    notinc = (("LDL", 0), ("LDL", 1), ("LLD", 2))    # it is the third party's tie to the candidate (w->v, v->w)
    for nm, cellset in (("inc", inc), ("notinc", notinc)):
        n_ = sum(nk[c][0] for c in cellset)
        k_ = sum(nk[c][1] for c in cellset)
        out[f"join_{nm}"] = _ratio(k_, n_)
    out["join_inc_minus_notinc"] = out["join_inc"] - out["join_notinc"]
    for kind in ("repair", "join"):
        n_other = sum(out[f"n_{kind}_{t}"] for t in ("LLD", "LDL"))
        k_other = sum(out[f"k_{kind}_{t}"] for t in ("LLD", "LDL"))
        out[f"{kind}_LLDLDL"] = _ratio(k_other, n_other)
        out[f"{kind}_DLL_minus_LDL"] = out[f"{kind}_DLL"] - out[f"{kind}_LDL"]
        out[f"{kind}_DLL_minus_others"] = out[f"{kind}_DLL"] - out[f"{kind}_LLDLDL"]
    return out


def interaction_stats(cells: np.ndarray) -> dict:
    """The part of the pooled FIX excess that only BALANCE can produce.  Within each orientation and old sign the
    conversion rate of the four context cells (u-w sign, w-v sign) = pp, pm, mp, mm; additive effects of either sign
    (a generous voter converts more, a candidate liked by w draws conversions) cancel in the double difference
        D = sgn(old) * (r_pp + r_mm - r_pm - r_mp),     sgn = +1 for old -, -1 for old +,
    which is positive when conversion is higher exactly where the product of the three signs is negative (strict
    balance would convert there).  I is the precision-weighted mean of the eight block contrasts (weight = harmonic
    sum of the four cell sizes), I_<orientation> the mean of the two blocks of one orientation."""
    out = {}
    num = den = 0.0
    per_o = {o: [0.0, 0.0] for o in range(4)}
    for o in range(4):
        for old in (-1, 1):
            n = {}
            k = {}
            for a, b, nm in ((1, 1, "pp"), (1, -1, "pm"), (-1, 1, "mp"), (-1, -1, "mm")):
                m = (CELL_O == o) & (CELL_S1 == a) & (CELL_S2 == b) & (CELL_OLD == old)
                n[nm], k[nm] = _msum(cells, m), _msum(cells, m & CELL_CHG)
            r = {nm: _ratio(k[nm], n[nm]) for nm in n}
            d = (r["pp"] + r["mm"] - r["pm"] - r["mp"]) * (1 if old < 0 else -1)
            with np.errstate(divide="ignore", invalid="ignore"):
                w = 1.0 / sum(1.0 / np.maximum(np.asarray(n[nm], dtype=np.float64), 1e-9) for nm in n)
            w = np.where(np.all([np.asarray(n[nm]) > 0 for nm in n], axis=0), w, 0.0)
            d = np.where(w > 0, d, 0.0)
            tag = f"{ORIENT[o]}_{'neg' if old < 0 else 'pos'}"
            out["D_" + tag], out["W_" + tag] = d, w
            num = num + w * d
            den = den + w
            per_o[o][0] = per_o[o][0] + w * d
            per_o[o][1] = per_o[o][1] + w
    out["I"] = _ratio(num, den)
    for o in range(4):
        out["I_" + ORIENT[o]] = _ratio(per_o[o][0], per_o[o][1])
    return out


def event_share(ctx: Contexts, n_trans: int, s1, s2, old_t, new_t) -> tuple[float, int]:
    """Mean over converting transitions of their own FIX / (FIX + BREAK) (weak balance); each conversion
    weighs one whatever the number of third parties.  Returns (mean, number of conversions that count)."""
    old, new = old_t[ctx.tr], new_t[ctx.tr]
    chg = old != new
    nb = (s1 < 0).astype(np.int8) + (s2 < 0) + (old < 0)
    na = (s1 < 0).astype(np.int8) + (s2 < 0) + (new < 0)
    fix = (chg & (nb == 1)).astype(np.float64)
    brk = (chg & (nb != 1) & (na == 1)).astype(np.float64)
    f = np.bincount(ctx.tr, weights=fix, minlength=n_trans)
    b = np.bincount(ctx.tr, weights=brk, minlength=n_trans)
    tot = f + b
    ok = tot > 0
    return (float((f[ok] / tot[ok]).mean()) if ok.any() else float("nan")), int(ok.sum())


def observed(net: Network) -> dict:
    sg = net.sign
    old_t, new_t = net.old_new()
    cells = cell_counts(net.ctx, sg[net.ctx.e1], sg[net.ctx.e2], old_t, new_t)
    es, ne = event_share(net.ctx, len(net.trans.cur), sg[net.ctx.e1], sg[net.ctx.e2], old_t, new_t)
    return {"cells": cells, "event_share": es, "n_events": ne, **{"d_" + k: v for k, v in derived(cells).items()}}


# ------------------------------------------------------------------ nulls

@dataclasses.dataclass(frozen=True)
class NullSpec:
    """kind 'signs': shuffle all signs within strata (votes), the conversions are re-determined from the shuffled
    signs (the brief's null, UNCONDITIONAL).  kind 'context': the observed old and new sign of every transition
    are held and only the signs of the context ties are shuffled within strata (votes).  kind 'events': the
    contexts are held as observed and the conversion indicator is permuted among the transitions of a stratum
    (transitions), which keeps every pre-state class size fixed, as Newcomb's conditional null does."""
    name: str
    kind: str
    strata: str


NULL_SPECS = {s.name: s for s in (
    NullSpec("voter_uncond", "signs", "voter"),               # the brief's null
    NullSpec("ctx_voter", "context", "voter"),
    NullSpec("ctx_voter_res", "context", "voter_res"),
    NullSpec("ctx_candidacy", "context", "candidacy"),
    NullSpec("ev_cur_old", "events", "cur_old"),              # same new candidacy, same old sign
    NullSpec("ev_pair_old", "events", "pair_old"),            # same old and new candidacy, same old sign
    NullSpec("ev_voter_old", "events", "voter_old"),          # same voter, same old sign
    NullSpec("ev_cur_old_deg", "events", "cur_old_deg"),      # ... and the same number of triples (terciles)
    NullSpec("ev_cur_old_pos", "events", "cur_old_pos"),      # ... and the same voter generosity (terciles)
)}


def strata_of(net: Network, strata: str) -> np.ndarray:
    """Group ids: one per vote row for the vote-level strata, one per transition for the event-level strata
    (transitions with no triple at all are given a stratum of their own, so that they stay fixed)."""
    vt, tr = net.vt, net.trans
    if strata == "voter":
        return vt.voter.astype(np.int64)
    if strata == "voter_res":
        return vt.voter.astype(np.int64) * 3 + (vt.res + 1)
    if strata == "candidacy":
        return vt.cy.astype(np.int64)
    old = vt.sign[tr.prev]
    sgn = (old > 0).astype(np.int64)
    if strata == "cur_old":
        g = vt.cy[tr.cur].astype(np.int64) * 2 + sgn
    elif strata == "pair_old":
        g = (vt.cy[tr.prev].astype(np.int64) * (int(vt.cy.max()) + 1) + vt.cy[tr.cur]) * 2 + sgn
    elif strata == "voter_old":
        g = vt.voter[tr.cur].astype(np.int64) * 2 + sgn
    elif strata in ("cur_old_deg", "cur_old_pos"):
        if strata == "cur_old_deg":
            x = np.bincount(net.ctx.tr, minlength=len(tr.cur)).astype(np.float64)
        else:                                  # the voter's share of positive votes over all his non-neutral votes
            pos = np.bincount(vt.voter, weights=(vt.sign > 0), minlength=vt.n_users)
            tot = np.bincount(vt.voter, minlength=vt.n_users)
            x = (pos / np.maximum(tot, 1))[vt.voter[tr.cur]]
        cuts = np.quantile(x[x == x], [1 / 3, 2 / 3])
        tercile = np.searchsorted(cuts, x, side="right")
        g = (vt.cy[tr.cur].astype(np.int64) * 2 + sgn) * 3 + tercile
    else:
        raise ValueError(strata)
    has = np.zeros(len(tr.cur), dtype=bool)
    has[np.unique(net.ctx.tr)] = True
    g = np.where(has, g, g.max() + 1 + np.arange(len(g)))
    return g


class Shuffler:
    """Uniform random permutation of the values within each stratum: random keys added to the stratum
    number, one argsort per draw."""

    def __init__(self, group: np.ndarray):
        self.P = np.argsort(group, kind="stable")
        self.g = group[self.P].astype(np.float64)
        self.n = len(group)

    def __call__(self, values: np.ndarray, rng: np.random.Generator) -> np.ndarray:
        o = np.argsort(self.g + rng.random(self.n))
        out = np.empty_like(values)
        out[self.P] = values[self.P][o]
        return out


_STATE: dict = {}


def _conv_triplet(old_t, new_t):
    chg = old_t != new_t
    return int(chg.sum()), int(((old_t < 0) & (new_t > 0)).sum()), int(((old_t > 0) & (new_t < 0)).sum())


def _chunk(args):
    key, spec, n, seq = args
    net: Network = _STATE[key]
    ctx = net.ctx
    T = len(net.trans.cur)
    shuf = Shuffler(strata_of(net, spec.strata))
    rng = np.random.default_rng(seq)
    old_obs, new_obs = net.old_new()
    sg0 = net.sign
    cells = np.empty((n, 64), dtype=np.int32)
    es = np.empty(n)
    conv = np.empty((n, 3), dtype=np.int32)
    if spec.kind == "events":
        s1, s2 = sg0[ctx.e1], sg0[ctx.e2]
        base = cell_codes(ctx.o, s1, s2, old_obs[ctx.tr], np.ones(len(ctx.tr), dtype=np.int8)) - 1   # new bit cleared
        c_obs = (old_obs != new_obs).astype(np.int8)
        for i in range(n):
            c = shuf(c_obs, rng).astype(bool)
            new_t = np.where(c, -old_obs, old_obs).astype(np.int8)
            cells[i] = np.bincount(base + (new_t[ctx.tr] > 0), minlength=64)
            es[i], _ = event_share(ctx, T, s1, s2, old_obs, new_t)
            conv[i] = _conv_triplet(old_obs, new_t)
        return cells, es, conv
    for i in range(n):
        sg = shuf(sg0, rng)
        if spec.kind == "context":
            old_t, new_t = old_obs, new_obs
        else:
            old_t, new_t = sg[net.trans.prev], sg[net.trans.cur]
        s1, s2 = sg[ctx.e1], sg[ctx.e2]
        cells[i] = cell_counts(ctx, s1, s2, old_t, new_t)
        es[i], _ = event_share(ctx, T, s1, s2, old_t, new_t)
        conv[i] = _conv_triplet(old_t, new_t)
    return cells, es, conv


def run_null(net: Network, spec: NullSpec | str, n_draws: int = N_DRAWS, seed: int = SEED,
             workers: int | None = None, chunk: int = 250) -> dict:
    """n_draws of the null.  The result does not depend on the number of workers: draws are made in fixed
    chunks, each with its own seeded stream.  Returns {'cells': (B, 64), 'event_share': (B,), 'conv': (B, 3)}."""
    spec = NULL_SPECS[spec] if isinstance(spec, str) else spec
    sizes = [chunk] * (n_draws // chunk) + ([n_draws % chunk] if n_draws % chunk else [])
    base = zlib.crc32(spec.name.encode())
    seqs = [np.random.SeedSequence([seed, base, i]) for i in range(len(sizes))]
    key = f"net{id(net)}"
    _STATE[key] = net
    try:
        jobs = [(key, spec, n, s) for n, s in zip(sizes, seqs)]
        workers = (os.cpu_count() or 1) if workers is None else workers
        if workers > 1 and len(jobs) > 1 and "fork" in mp.get_all_start_methods():
            with mp.get_context("fork").Pool(min(workers, len(jobs))) as pool:
                parts = pool.map(_chunk, jobs)
        else:
            parts = [_chunk(j) for j in jobs]
    finally:
        _STATE.pop(key, None)
    return {"cells": np.concatenate([p[0] for p in parts]), "event_share": np.concatenate([p[1] for p in parts]),
            "conv": np.concatenate([p[2] for p in parts])}


def compare(obs: float, null: np.ndarray) -> dict:
    """Observed value against null draws: mean, sd, z, and the one-sided tie-inclusive Monte-Carlo p-values
    (1 + #{null >= obs}) / (B + 1) and (1 + #{null <= obs}) / (B + 1); NaN draws (an undefined ratio) are dropped."""
    x = np.asarray(null, dtype=np.float64)
    x = x[~np.isnan(x)]
    if not len(x) or np.isnan(obs):
        return {"obs": obs, "mean": float("nan"), "sd": float("nan"), "z": float("nan"), "p_ge": float("nan"),
                "p_le": float("nan"), "B": len(x)}
    tol = 1e-12
    sd = float(x.std(ddof=1)) if len(x) > 1 else float("nan")
    return {"obs": float(obs), "mean": float(x.mean()), "sd": sd, "z": (obs - x.mean()) / sd if sd > 0 else float("nan"),
            "p_ge": (1 + int((x >= obs - tol).sum())) / (len(x) + 1), "p_le": (1 + int((x <= obs + tol).sum())) / (len(x) + 1),
            "B": len(x)}


# ------------------------------------------------------------------ characterising the conversions

def characterise(net: Network) -> dict:
    """Counts, directions, timing and selection of the transitions (descriptive; nothing here is a test)."""
    vt, tr = net.vt, net.trans
    old, new = net.old_new()
    chg = old != new
    gap = vt.t[tr.cur] - vt.t[tr.prev]
    out = {
        "n_trans": len(tr.cur), "n_conv": int(chg.sum()), "n_up": int(((old < 0) & (new > 0)).sum()),
        "n_down": int(((old > 0) & (new < 0)).sum()),
        "n_pairs_with_trans": len(np.unique(vt.voter[tr.cur].astype(np.int64) * vt.n_users + vt.cand[tr.cur])),
        "n_pairs_with_conv": len(np.unique(vt.voter[tr.cur[chg]].astype(np.int64) * vt.n_users + vt.cand[tr.cur[chg]])),
        "trans_old_neg": int((old < 0).sum()), "trans_old_pos": int((old > 0).sum()),
    }
    out["rate_conv_old_neg"] = out["n_up"] / max(out["trans_old_neg"], 1)
    out["rate_conv_old_pos"] = out["n_down"] / max(out["trans_old_pos"], 1)
    q = [10, 25, 50, 75, 90]
    out["gap_days"] = {nm: np.percentile(gap[m], q).tolist() if m.any() else None for nm, m in
                       (("all", np.ones_like(chg)), ("conv", chg), ("nonconv", ~chg), ("up", (old < 0) & chg), ("down", (old > 0) & chg))}
    # outcomes of the two candidacies: (old res, new res)
    ores, nres = vt.res[tr.prev], vt.res[tr.cur]
    out["res_cross"] = {nm: {(int(a), int(b)): int(((ores == a) & (nres == b) & m).sum()) for a in (-1, 1) for b in (-1, 1)}
                        for nm, m in (("all", np.ones_like(chg)), ("up", (old < 0) & chg), ("down", (old > 0) & chg))}
    # k-th candidacy of the candidate (by start time) that the converting vote belongs to
    order = np.lexsort((vt.cy_start, vt.cy_cand))
    rank = np.empty(len(order), dtype=np.int32)
    seen = collections.Counter()
    for c in order:
        rank[c] = seen[int(vt.cy_cand[c])]
        seen[int(vt.cy_cand[c])] += 1
    nth = rank[vt.cy[tr.cur]] + 1
    out["nth_candidacy"] = {int(k): int(((nth == k) & chg).sum()) for k in range(2, 6)}
    out["nth_candidacy_trans"] = {int(k): int((nth == k).sum()) for k in range(2, 6)}
    out["share_within_a_year"] = float((gap < 365.25)[chg].mean())
    year = np.array([datetime.date.fromordinal(int(x)).year for x in vt.t[tr.cur]])
    out["by_year"] = {int(y): (int(((year == y) & chg).sum()), int((year == y).sum())) for y in np.unique(year)}   # year -> (conversions, re-votes)
    # coverage of the conversions by at least one triple
    has = np.zeros(len(tr.cur), dtype=bool)
    has[np.unique(net.ctx.tr)] = True
    out["n_trans_with_ctx"], out["n_conv_with_ctx"] = int(has.sum()), int((has & chg).sum())
    out["ctx_per_trans"] = np.percentile(np.bincount(net.ctx.tr, minlength=len(tr.cur))[has], [50, 90, 99, 100]).tolist()
    out["n_pairs_total"] = int(len(np.unique(vt.voter.astype(np.int64) * vt.n_users + vt.cand)))
    out["n_inst"] = len(net.ctx.tr)
    out["inst_by_orientation"] = np.bincount(net.ctx.o, minlength=4).tolist()
    out["n_w_distinct"] = int(len(np.unique(net.ctx.w)))
    voter, cand = vt.voter[tr.cur], vt.cand[tr.cur]
    per_voter = np.bincount(voter[chg], minlength=vt.n_users)
    out["n_voters_revote"] = int(len(np.unique(voter)))
    out["n_voters_conv"] = int((per_voter > 0).sum())
    out["n_cands_conv"] = int(len(np.unique(cand[chg])))
    out["max_conv_per_voter"] = int(per_voter.max())
    out["top10_voter_share_conv"] = float(np.sort(per_voter)[-10:].sum() / max(chg.sum(), 1))
    return out


def type_table(net: Network) -> list[dict]:
    """The 16 LHK types over CONVERTING instances: counts by (type, direction of conversion), and what balance
    and status predicted for the converting tie."""
    sg = net.sign
    old_t, new_t = net.old_new()
    ctx = net.ctx
    s1, s2 = sg[ctx.e1], sg[ctx.e2]
    old, new = old_t[ctx.tr], new_t[ctx.tr]
    chg = old != new
    rows = []
    for o in range(4):
        for a in (1, -1):
            for b in (1, -1):
                m = (ctx.o == o) & (s1 == a) & (s2 == b)
                up = int((m & chg & (old < 0)).sum())
                dn = int((m & chg & (old > 0)).sum())
                n_old_neg, n_old_pos = int((m & (old < 0)).sum()), int((m & (old > 0)).sum())
                bal = balance_prediction(a, b)
                st = status_prediction(o, a, b)
                rows.append({"type": triad_type(o, a, b), "n": int(m.sum()), "up": up, "down": dn,
                             "n_old_neg": n_old_neg, "n_old_pos": n_old_pos, "balance": bal, "status": st})
    return rows


# ------------------------------------------------------------------ Bitcoin OTC and Alpha (formation only)

def load_bitcoin(src: Source, verify: bool = True) -> dict:
    """SOURCE, TARGET, RATING (-10..+10) as int arrays and TIME (Unix seconds, with a fractional part in
    these files) as floats, in file order."""
    p = require(src, verify)
    with gzip.open(p, "rt", encoding="ascii") as fh:
        a = np.loadtxt(fh, delimiter=",", dtype=np.float64)
    return {"src": a[:, 0].astype(np.int64), "dst": a[:, 1].astype(np.int64), "rating": a[:, 2].astype(np.int64),
            "time": a[:, 3]}


@dataclasses.dataclass
class Projection:
    """Undirected projection: one tie per unordered pair, signed and timed by the EARLIEST rating of the pair
    (file order breaks ties), the rule that reproduces 117's pair and triangle counts [L4572]."""
    pair_a: np.ndarray
    pair_b: np.ndarray
    sign: np.ndarray            # per pair
    time: np.ndarray
    rating_row: np.ndarray      # per pair: the row of the directed rating that fixed it
    tri: np.ndarray             # (T, 3) pair indices, ordered by (time, pair index): first, second, closing
    tied: np.ndarray            # per triangle: the closing time equals the second's, or the second equals the first
    n_both_signs: int
    n_nodes: int


def bitcoin_projection(d: dict) -> Projection:
    src, dst, rat, tm = d["src"], d["dst"], d["rating"], d["time"]
    keep = (src != dst) & (rat != 0)
    rows = np.nonzero(keep)[0]
    a, b = np.minimum(src[rows], dst[rows]), np.maximum(src[rows], dst[rows])
    M = int(max(src.max(), dst.max())) + 1
    key = a * M + b
    o = np.lexsort((rows, tm[rows], key))
    rows, a, b, key = rows[o], a[o], b[o], key[o]
    first = np.concatenate([[True], key[1:] != key[:-1]])
    pa, pb, prow = a[first], b[first], rows[first]
    sign = np.sign(rat[prow]).astype(np.int8)
    time = tm[prow]
    # pairs whose two directions carry opposite signs
    sgn_all = np.sign(rat[rows])
    grp = np.cumsum(first) - 1
    mn = np.full(len(pa), 2)
    mx = np.full(len(pa), -2)
    np.minimum.at(mn, grp, sgn_all)
    np.maximum.at(mx, grp, sgn_all)
    n_both = int(((mn == -1) & (mx == 1)).sum())
    idx = {(int(x), int(y)): i for i, (x, y) in enumerate(zip(pa, pb))}
    adj = collections.defaultdict(set)
    for x, y in zip(pa.tolist(), pb.tolist()):
        adj[x].add(y)
        adj[y].add(x)
    tri = []
    for x, y in zip(pa.tolist(), pb.tolist()):
        for c in adj[x] & adj[y]:
            if c > y:                                   # x < y < c: each triangle once
                tri.append((idx[(x, y)], idx[(x, c)], idx[(y, c)]))
    tri = np.array(tri, dtype=np.int64).reshape(-1, 3)
    tt = time[tri]
    ordr = np.argsort(tt * (len(pa) + 1) + tri, axis=1)             # by time, then pair index
    tri_s = np.take_along_axis(tri, ordr, axis=1)
    ts = np.take_along_axis(tt, ordr, axis=1)
    tied = (ts[:, 1] == ts[:, 0]) | (ts[:, 2] == ts[:, 1])
    return Projection(pa, pb, sign, time, prow, tri_s, tied, n_both, len(set(pa.tolist()) | set(pb.tolist())))


def bitcoin_stats(sign: np.ndarray, tri: np.ndarray, subset: np.ndarray | None = None) -> dict:
    """Balanced share (product of the three signs positive = the closing edge has the product of the first
    two), counts by number of negative ties, and the closing-edge table by the first two edges."""
    s = sign[tri] if subset is None else sign[tri[subset]]
    neg = (s < 0).sum(1)
    first_neg = (s[:, 0] < 0).astype(int) + (s[:, 1] < 0)
    close_pos = s[:, 2] > 0
    out = {"n": len(s), "balanced": int((neg % 2 == 0).sum()), "neg_counts": np.bincount(neg, minlength=4).tolist()}
    for k, nm in enumerate(("pp", "pm", "mm")):
        m = first_neg == k
        out[f"first_{nm}"] = int(m.sum())
        out[f"close_pos_{nm}"] = int((m & close_pos).sum())
    return out


def bitcoin_null(proj: Projection, d: dict, n_draws: int, seed: int, within_rater: bool = False,
                 subset: np.ndarray | None = None, within: str | None = None) -> dict:
    """Sign-shuffled null for bitcoin_stats.  within=None: the signs permuted over all pairs (the null of 117);
    'rater': the directed ratings' signs permuted within rater (a negative-prone rater stays negative-prone);
    'ratee': within ratee (a widely distrusted trader stays distrusted).  In both grouped nulls the pairs are re-signed
    by the same earliest rating.  within_rater=True is the old spelling of within='rater'."""
    within = "rater" if within_rater and within is None else within
    rng = np.random.default_rng([seed, {None: 0, "rater": 1, "ratee": 2}[within]])
    shuf = None if within is None else Shuffler((d["src"] if within == "rater" else d["dst"]).astype(np.int64))
    rsign = np.sign(d["rating"]).astype(np.int8)
    acc = collections.defaultdict(list)
    for _ in range(n_draws):
        if shuf is not None:
            sg = shuf(rsign, rng)[proj.rating_row].astype(np.int8)
        else:
            sg = rng.permutation(proj.sign)
        st = bitcoin_stats(sg, proj.tri, subset)
        for k, v in st.items():
            acc[k].append(v)
    return {k: np.array(v) for k, v in acc.items()}
