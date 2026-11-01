"""Wiki-RfA tie conversion and Bitcoin formation: the checks that the machinery behind
sim/results/wikirfa_conversion.md is right.

Prior work: docs/prior-work/117-modern-signed-and-split-datasets.md (D610) sections 3.3 and 3.4; the 16 directed triad
types of Leskovec, Huttenlocher & Kleinberg (2010) as in docs/prior-work/106 section 1.2; the Newcomb run this
continues (tests/test_newcomb_triads.py).  Ledger ids are the lines with source "117 ..." (L4547-L4668, L4854, L4855):
wiki-RfA file and counts L4561-L4563, repeat candidacies re-sign ties L4564 (dup L4855); Bitcoin files, counts, the
undirected projection, the closure table and the product rule L4567-L4579; Bitcoin cannot test conversion L4571, L4580.

Two groups.  (1) Machinery, no data needed: the date parser on the file's slips, the record parser, the candidacy rule
(gaps, duplicated elections, strays, undated votes), the vote table, triad types and the balance logic against brute
force, the contexts and the cell statistics against a brute-force enumerator on a random synthetic network, the
shufflers' invariants, the planted-effect behaviour of the interaction contrast, the Bitcoin triangle counter.
(2) Data tests, skipped with a reason when the git-ignored SNAP files are absent (fetch them with
`cd sim && ~/.local/bin/uv run python -m models.wikirfa_report fetch`; the data are not redistributable,
sim/data/README.md): file integrity; the counts 117 published, reproduced (a non-reproduction is a finding, recorded,
not tuned away); the network facts the report relies on; the observed statistics; and seeded small-draw checks that
the nulls behave as designed.  Null draws are Monte Carlo, so seeded assertions about them are qualitative or have wide
margins; the observed counts are deterministic and are pinned.
"""
from __future__ import annotations

import collections
import dataclasses
import gzip
import io
import itertools

import numpy as np
import pytest

from models import wikirfa as wr

needs_wiki = pytest.mark.skipif(
    not wr.WIKIRFA.path.exists(),
    reason="sim/data/wiki-rfa/wiki-RfA.txt.gz is absent (local-use-only, git-ignored): "
    "cd sim && ~/.local/bin/uv run python -m models.wikirfa_report fetch",
)
needs_bitcoin = pytest.mark.skipif(
    not (wr.OTC.path.exists() and wr.ALPHA.path.exists()),
    reason="sim/data/bitcoin/*.csv.gz is absent (local-use-only, git-ignored): "
    "cd sim && ~/.local/bin/uv run python -m models.wikirfa_report fetch",
)


# ------------------------------------------------------------------ (1) machinery: parsing

@pytest.mark.parametrize("text,status", [
    ("19:53, 25 January 2013", "ok"), ("00:02, 1 June 2013", "ok"), ("23:59, 31 Dec 2006", "ok"),
    ("17:44, 26 Mya 2007", "repaired"), ("10:00, 3 Julu 2008", "repaired"), ("10:00, 3 Janry 2008", "repaired"),
    ("31:29, 24 May 2008", "invalid"), ("12:61, 24 May 2008", "invalid"), ("12:00, 31 February 2008", "invalid"),
    ("", "empty"), ("not a date", "invalid"),
])
def test_parse_dat_reads_the_files_slips_and_flags_the_rest(text, status):
    """The DAT field: abbreviated months occur (Jun, Apr, ...), three months carry a slip (Mya, Julu, Janry; 1 each in the
    file), one record has an hour of 31, 9,367 are empty [L4561].  Slips are repaired, impossible dates become NaN."""
    value, st = wr.parse_dat(text)
    assert st == status
    assert (not np.isnan(value)) == (status in ("ok", "repaired"))


def test_parse_dat_orders_by_time_and_resolves_minutes():
    a, _ = wr.parse_dat("23:59, 31 December 2006")
    b, _ = wr.parse_dat("00:00, 1 January 2007")
    c, _ = wr.parse_dat("00:01, 1 January 2007")
    assert a < b < c
    assert abs((c - b) - 1 / 1440) < 1e-9


def test_parse_wikirfa_toy_file_skips_comments_and_interns_names():
    lines = [
        "SRC:Alice", "TGT:Bob", "VOT:1", "RES:1", "YEA:2010", "DAT:12:00, 1 May 2010", "TXT:'''Support''' SRC:fake", "",
        "SRC:Carol", "TGT:Bob", "VOT:-1", "RES:1", "YEA:2010", "DAT:13:30, 2 May 2010", "TXT:", "",
        "SRC:", "TGT:Bob", "VOT:0", "RES:1", "YEA:2010", "DAT:", "TXT:x", "",
        "SRC:Alice", "TGT:Dave", "VOT:1", "RES:-1", "YEA:2011", "DAT:09:00, 3 Mya 2011", "TXT:y",
    ]
    raw = wr.parse_wikirfa(lines)                              # the last record has no trailing blank line
    assert raw.notes["n_records"] == 4 and raw.notes["n_users"] == 4
    assert raw.voter.tolist() == [0, 2, -1, 0] and raw.cand.tolist() == [1, 1, 1, 3]
    assert raw.vote.tolist() == [1, -1, 0, 1] and raw.res.tolist() == [1, 1, 1, -1]
    assert raw.notes["n_empty_voter"] == 1 and raw.notes["dat_empty"] == 1 and raw.notes["dat_repaired"] == 1
    assert np.isnan(raw.t[2]) and not np.isnan(raw.t[3])


def test_parse_wikirfa_is_loud_about_a_record_without_a_target():
    with pytest.raises(ValueError):
        wr.parse_wikirfa(["SRC:A", "VOT:1", "RES:1", "YEA:2010", ""])


# ------------------------------------------------------------------ (1) machinery: candidacies and the vote table

def _raw(rows, n_users=20):
    """rows: (voter, cand, vote, res, yea, t); voter -1 = empty; t None = undated."""
    a = list(zip(*rows))
    return wr.RawVotes(np.array(a[0], dtype=np.int32), np.array(a[1], dtype=np.int32), np.array(a[2], dtype=np.int8),
                       np.array(a[3], dtype=np.int8), np.array(a[4], dtype=np.int16),
                       np.array([np.nan if x is None else x for x in a[5]], dtype=np.float64), n_users, {})


def test_candidacies_split_at_gaps_not_at_result_or_year():
    """A candidate who fails twice in one year has two candidacies; one gap of 14 days or less does not split."""
    rows = [(v, 0, 1, -1, 2006, 100.0 + 0.2 * v) for v in range(1, 13)]           # first run, days 100-102
    rows += [(v, 0, -1, -1, 2006, 160.0 + 0.2 * v) for v in range(1, 13)]          # second run, same year, same result
    rows += [(v, 1, 1, 1, 2006, 100.0 + v) for v in range(2, 14)]                  # days 102-113: gaps of 1 day, one run
    cs = wr.assign_candidacies(_raw(rows))
    assert cs.notes["n_candidacies"] == 3
    assert len(set(cs.cy[:12])) == 1 and len(set(cs.cy[12:24])) == 1 and cs.cy[0] != cs.cy[12]
    assert len(set(cs.cy[24:])) == 1


def test_an_election_recorded_twice_with_opposite_labels_is_one_candidacy_with_unknown_result():
    """117's (candidate, year, result) elections count 3,926; in 18 clusters the same election appears under both results
    (92 votes each, say).  Grouping by result would make the copy a second candidacy and its votes 618 zero-gap 're-votes'."""
    rows = [(v, 0, 1, 1, 2007, 200.0 + 0.1 * v) for v in range(1, 15)]
    rows += [(v, 0, 1, -1, 2007, 200.0 + 0.1 * v) for v in range(1, 15)]
    cs = wr.assign_candidacies(_raw(rows))
    assert cs.notes["n_candidacies"] == 1 and cs.notes["n_clusters_with_both_labels"] == 1 and cs.notes["n_clusters_label_tie"] == 1
    assert cs.res.tolist() == [0]
    vt = wr.build_vote_table(_raw(rows), cs)
    assert len(vt.voter) == 14 and vt.notes["n_collapsed_within_candidacy"] == 14      # one copy of each vote survives
    assert len(wr.build_transitions(vt).cur) == 0


def _day(y, m, d, h=0.0):
    return __import__("datetime").date(y, m, d).toordinal() + h / 24.0


def test_a_late_stray_signature_joins_the_big_candidacy_and_an_unplaceable_undated_vote_is_dropped():
    rows = [(v, 0, 1, 1, 2008, _day(2008, 5, 1, v / 2)) for v in range(1, 14)]    # a 13-vote candidacy, May 2008
    rows += [(15, 0, -1, 1, 2008, _day(2010, 1, 1))]                               # one vote dated 600 days later: a stray
    rows += [(16, 0, 1, 1, 2008, None)]                                            # undated, one candidacy: placed
    rows += [(v, 1, 1, 1, 2008, _day(2008, 5, 1, v / 2)) for v in range(2, 14)]   # candidate 1, first run
    rows += [(v, 1, 1, 1, 2010, _day(2010, 1, 1, v / 2)) for v in range(2, 14)]   # candidate 1, second run
    rows += [(17, 1, 1, 1, 2009, None)]                                            # undated, 2009 sits between the runs: dropped
    cs = wr.assign_candidacies(_raw(rows))
    assert cs.notes["n_stray_clusters"] == 1 and cs.notes["n_stray_votes"] == 1 and cs.notes["n_unplaced_undated"] == 1
    assert cs.cy[13] == cs.cy[0] and cs.cy[14] == cs.cy[0]                          # stray and undated joined candidacy 0
    assert cs.t_eff[13] == pytest.approx(cs.median[cs.cy[0]])                       # at the candidacy's median time
    assert cs.cy[-1] == -1 and cs.notes["n_candidacies"] == 3


def test_an_undated_vote_goes_to_the_candidacy_of_its_year():
    rows = [(v, 1, 1, 1, 2008, _day(2008, 5, 1, v / 2)) for v in range(2, 14)]
    rows += [(v, 1, 1, 1, 2010, _day(2010, 1, 1, v / 2)) for v in range(2, 14)]
    rows += [(17, 1, 1, 1, 2010, None)]
    cs = wr.assign_candidacies(_raw(rows))
    assert cs.cy[-1] == cs.cy[12] and cs.cy[-1] != cs.cy[0]


def test_a_candidate_with_only_undated_votes_gets_a_pseudo_candidacy_at_midsummer():
    rows = [(v, 3, 1, 1, 2004, None) for v in range(1, 6)]
    cs = wr.assign_candidacies(_raw(rows))
    assert cs.notes["n_candidacies"] == 1 and cs.notes["n_undated_only_candidates"] == 1
    assert cs.start[0] == pytest.approx(__import__("datetime").date(2004, 7, 1).toordinal())


def test_vote_table_drops_neutral_empty_and_self_votes_collapses_within_candidacy_and_builds_transitions():
    rows = [(v, 0, 1, 1, 2006, 100.0 + 0.1 * v) for v in range(1, 13)]
    rows += [(1, 0, -1, 1, 2006, 100.5)]                                           # voter 1 changes his mind in the same RfA
    rows += [(-1, 0, 1, 1, 2006, 100.2), (0, 0, 1, 1, 2006, 100.3), (5, 0, 0, 1, 2006, 100.4)]   # empty voter, self, neutral
    rows += [(v, 0, 1, 1, 2007, 400.0 + 0.1 * v) for v in range(1, 13)]           # second candidacy
    raw = _raw(rows)
    cs = wr.assign_candidacies(raw)
    vt = wr.build_vote_table(raw, cs)
    assert vt.notes["n_empty_voter"] == 1 and vt.notes["n_neutral"] == 1 and vt.notes["n_self"] == 1
    assert vt.notes["n_collapsed_within_candidacy"] == 1
    tr = wr.build_transitions(vt)
    assert len(tr.cur) == 12                                                        # voters 1..12, one transition each
    old, new = vt.sign[tr.prev], vt.sign[tr.cur]
    assert int((old != new).sum()) == 1                                             # voter 1: the LAST vote of candidacy 1 was -1
    assert np.all(vt.cy[tr.prev] != vt.cy[tr.cur]) and np.all(tr.cutoff == vt.cy_start[vt.cy[tr.cur]])


# ------------------------------------------------------------------ (1) machinery: triad logic

def test_triad_types_follow_lhks_naming_and_example():
    """106 section 1.2: 'The type FBmp is u negative to w and v positive to w.'"""
    assert wr.triad_type(1, -1, +1) == "FBmp"
    assert wr.triad_type(0, 1, 1) == "FFpp" and wr.triad_type(2, -1, -1) == "BFmm" and wr.triad_type(3, 1, -1) == "BBpm"
    assert len({wr.triad_type(o, a, b) for o in range(4) for a in (1, -1) for b in (1, -1)}) == 16


def test_balance_predicts_all_16_types_and_status_exactly_eight():
    """106 section 1.2: 'It makes no prediction when the two signs cancel, so it predicts on 8 of the 16 types and balance
    on all 16.'  Weak balance (Davis) agrees with balance on pp, pm, mp and makes no prediction on mm."""
    types = [(o, a, b) for o in range(4) for a in (1, -1) for b in (1, -1)]
    assert all(wr.balance_prediction(a, b) in (1, -1) for _, a, b in types)
    assert sum(1 for o, a, b in types if wr.status_prediction(o, a, b) != 0) == 8
    assert wr.status_prediction(0, 1, 1) == 1 and wr.status_prediction(0, -1, -1) == -1 and wr.status_prediction(0, 1, -1) == 0
    assert wr.status_prediction(2, 1, -1) == -1              # BFpm: u->w flipped to a negative, w->v negative


def test_flipping_any_tie_of_a_one_negative_triple_makes_it_weakly_balanced():
    """Why FIX is exactly 'the triple was one-negative', whichever tie converts (module docstring)."""
    for signs in itertools.product((1, -1), repeat=3):
        if wr.n_negative(*signs) != 1:
            continue
        assert wr.weakly_unbalanced(1)
        for i in range(3):
            flipped = list(signs)
            flipped[i] = -flipped[i]
            assert not wr.weakly_unbalanced(wr.n_negative(*flipped))
            assert not wr.strictly_unbalanced(wr.n_negative(*flipped))


def test_fix_and_break_masks_match_the_definition_cell_by_cell():
    for c in range(64):
        s1, s2, old, new = (int(x[c]) for x in (wr.CELL_S1, wr.CELL_S2, wr.CELL_OLD, wr.CELL_NEW))
        before, after = wr.n_negative(s1, s2, old), wr.n_negative(s1, s2, new)
        changed = old != new
        assert bool(wr.FIXW[c]) == (changed and wr.weakly_unbalanced(before) and not wr.weakly_unbalanced(after))
        assert bool(wr.BRKW[c]) == (changed and not wr.weakly_unbalanced(before) and wr.weakly_unbalanced(after))
        assert bool(wr.FIXS[c]) == (changed and wr.strictly_unbalanced(before) and not wr.strictly_unbalanced(after))
        assert bool(wr.BRKS[c]) == (changed and not wr.strictly_unbalanced(before) and wr.strictly_unbalanced(after))
        assert int(wr.cell_codes(np.array([wr.CELL_O[c]]), np.array([s1]), np.array([s2]), np.array([old]), np.array([new]))[0]) == c


def test_dk_types_put_the_converting_tie_in_the_position_the_orientation_implies():
    """FF: (u->w, w->v, u->v) so the converting tie is third; FB: (u->v, v->w, u->w) first; BF: (w->u, u->v, w->v) second;
    BB is a directed cycle with no D&K type.  Vary the converting tie's sign and the string changes only there."""
    for o in (0, 1, 2):
        pos = wr.FOCAL_POSITION[o] - 1
        for a, b in itertools.product((1, -1), repeat=2):
            plus, minus = wr.dk_type(o, a, b, 1), wr.dk_type(o, a, b, -1)
            assert [i for i in range(3) if plus[i] != minus[i]] == [pos]
    assert wr.dk_type(3, 1, 1, 1) is None
    assert wr.dk_type(0, -1, 1, 1) == "DLL"                  # u dislikes w, w likes v, u likes v: first tie negative
    assert wr.dk_type(1, 1, 1, -1) == "DLL"                  # the converting tie itself is the lone negative, in first place
    assert wr.dk_type(2, 1, 1, -1) == "LDL"


# ------------------------------------------------------------------ (1) machinery: a random network against brute force

def synthetic_raw(seed: int = 0, n_users: int = 26, n_cands: int = 12) -> wr.RawVotes:
    rng = np.random.default_rng(seed)
    rows = []
    for c in range(n_cands):
        starts = np.sort(rng.choice(np.arange(0, 2400, 80), size=int(rng.integers(1, 4)), replace=False)) + 730000.0
        for s in starts:
            res = int(rng.choice([-1, 1]))
            for u in rng.choice([x for x in range(n_users) if x != c], size=int(rng.integers(11, 20)), replace=False):
                rows.append((int(u), c, int(rng.choice([-1, 1, 1, 1, 0], p=[0.25, 0.3, 0.25, 0.1, 0.1])), res, 2005,
                             float(s + 6.0 * rng.random())))
    return _raw(rows, n_users)


@pytest.fixture(scope="module")
def synth() -> wr.Network:
    net = wr.build_network(synthetic_raw())
    assert len(net.trans.cur) > 30 and len(net.ctx.tr) > 300 and int((net.vt.sign[net.trans.prev] != net.vt.sign[net.trans.cur]).sum()) > 5
    return net


def _brute_instances(net: wr.Network):
    vt, tr = net.vt, net.trans
    out = []
    for t in range(len(tr.cur)):
        u, v, cut = int(vt.voter[tr.cur[t]]), int(vt.cand[tr.cur[t]]), float(tr.cutoff[t])

        def latest(a, b):
            rows = [i for i in range(len(vt.voter)) if vt.voter[i] == a and vt.cand[i] == b and vt.t[i] < cut]
            return max(rows, key=lambda i: (vt.t[i], i)) if rows else None

        for w in sorted(set(vt.voter.tolist()) | set(vt.cand.tolist())):
            if w in (u, v):
                continue
            first = [(0, latest(u, w)), (1, latest(w, u))]
            second = [(0, latest(w, v)), (1, latest(v, w))]
            for a, r1 in first:
                for b, r2 in second:
                    if r1 is not None and r2 is not None:
                        out.append((t, 2 * a + b, r1, r2))
    return sorted(out)


def test_contexts_match_a_brute_force_enumeration(synth):
    got = sorted(zip(synth.ctx.tr.tolist(), synth.ctx.o.tolist(), synth.ctx.e1.tolist(), synth.ctx.e2.tolist()))
    assert got == _brute_instances(synth)
    c = synth.ctx
    assert np.all(synth.vt.t[c.e1] < synth.trans.cutoff[c.tr]) and np.all(synth.vt.t[c.e2] < synth.trans.cutoff[c.tr])
    assert len(set(got)) == len(got)


def _brute_summary(net: wr.Network):
    sg = net.sign
    old_t, new_t = net.old_new()
    fix_w = brk_w = fix_s = brk_s = 0
    n = collections.Counter()
    k = collections.Counter()
    for t, o, e1, e2 in zip(net.ctx.tr, net.ctx.o, net.ctx.e1, net.ctx.e2):
        s1, s2, old, new = int(sg[e1]), int(sg[e2]), int(old_t[t]), int(new_t[t])
        before, after = wr.n_negative(s1, s2, old), wr.n_negative(s1, s2, new)
        n[before] += 1
        if old != new:
            k[before] += 1
            fix_w += wr.weakly_unbalanced(before) and not wr.weakly_unbalanced(after)
            brk_w += (not wr.weakly_unbalanced(before)) and wr.weakly_unbalanced(after)
            fix_s += wr.strictly_unbalanced(before)
            brk_s += not wr.strictly_unbalanced(before)
    return fix_w, brk_w, fix_s, brk_s, n, k


def test_cell_statistics_match_a_brute_force_classification(synth):
    obs = wr.observed(synth)
    fix_w, brk_w, fix_s, brk_s, n, k = _brute_summary(synth)
    assert (obs["d_fix_w"], obs["d_brk_w"], obs["d_fix_s"], obs["d_brk_s"]) == (fix_w, brk_w, fix_s, brk_s)
    assert obs["d_share_w"] == pytest.approx(fix_w / (fix_w + brk_w))
    for c in range(4):
        assert (obs[f"d_n{c}"], obs[f"d_k{c}"]) == (n[c], k[c])
    assert obs["d_n_inst"] == len(synth.ctx.tr) == sum(n.values())
    assert obs["d_fix_w"] == obs["d_k1"]                                           # FIX is exactly the conversions of one-negative triples


def test_event_level_share_is_the_mean_of_each_conversions_own_share(synth):
    sg = synth.sign
    old_t, new_t = synth.old_new()
    ctx = synth.ctx
    per = collections.defaultdict(lambda: [0, 0])
    for t, e1, e2 in zip(ctx.tr, ctx.e1, ctx.e2):
        s1, s2, old, new = int(sg[e1]), int(sg[e2]), int(old_t[t]), int(new_t[t])
        if old == new:
            continue
        before, after = wr.n_negative(s1, s2, old), wr.n_negative(s1, s2, new)
        per[t][0] += wr.weakly_unbalanced(before)
        per[t][1] += (not wr.weakly_unbalanced(before)) and wr.weakly_unbalanced(after)
    shares = [f / (f + b) for f, b in per.values() if f + b]
    es, n_ev = wr.event_share(ctx, len(synth.trans.cur), sg[ctx.e1], sg[ctx.e2], old_t, new_t)
    assert n_ev == len(shares) and es == pytest.approx(np.mean(shares))


# ------------------------------------------------------------------ (1) machinery: the nulls

def test_shuffler_preserves_every_strata_multiset_and_is_uniform_within_a_stratum():
    rng = np.random.default_rng(1)
    group = np.repeat(np.arange(6), [1, 2, 3, 3, 5, 8])
    values = np.arange(len(group)).astype(np.int8)
    sh = wr.Shuffler(group)
    for _ in range(50):
        out = sh(values, rng)
        for g in range(6):
            assert sorted(out[group == g].tolist()) == sorted(values[group == g].tolist())
    sh3 = wr.Shuffler(np.zeros(3, dtype=np.int64))
    seen = collections.Counter(tuple(sh3(np.array([1, 2, 3], dtype=np.int8), rng).tolist()) for _ in range(6000))
    assert len(seen) == 6 and min(seen.values()) > 800                              # all six orders, each about 1/6


def test_context_nulls_hold_the_observed_conversions_and_the_unconditional_one_does_not(synth):
    old, new = synth.old_new()
    n_conv = int((old != new).sum())
    for name in ("ctx_voter", "ctx_voter_res", "ctx_candidacy"):
        r = wr.run_null(synth, name, 30, 5, workers=1, chunk=10)
        assert np.all(r["conv"][:, 0] == n_conv)
        assert np.all(r["cells"].sum(1) == len(synth.ctx.tr))
    r = wr.run_null(synth, "voter_uncond", 60, 5, workers=1, chunk=20)
    assert r["conv"][:, 0].std() > 0 and np.all(r["cells"].sum(1) == len(synth.ctx.tr))


def test_event_permutation_keeps_stratum_conversion_counts_directions_and_the_pre_state(synth):
    """The Newcomb-style null: contexts and old signs are held, so every pre-state class size is fixed; the number of
    conversions, and of each direction, is preserved within strata, hence overall."""
    obs = wr.observed(synth)
    old, new = synth.old_new()
    for name in ("ev_cur_old", "ev_pair_old", "ev_voter_old", "ev_cur_old_deg", "ev_cur_old_pos"):
        r = wr.run_null(synth, name, 40, 5, workers=1, chunk=10)
        D = wr.derived(r["cells"])
        assert np.all(r["conv"][:, 0] == int((old != new).sum()))
        assert np.all(r["conv"][:, 1] == int(((old < 0) & (new > 0)).sum()))
        for c in range(4):
            assert np.all(D[f"n{c}"] == obs[f"d_n{c}"])                             # denominators fixed
        assert np.all(D["n_inst"] == obs["d_n_inst"])


def test_event_permutation_strata_are_what_they_say(synth):
    vt, tr = synth.vt, synth.trans
    old = vt.sign[tr.prev]
    has = np.zeros(len(tr.cur), dtype=bool)
    has[np.unique(synth.ctx.tr)] = True
    g = wr.strata_of(synth, "cur_old")
    for a, b in itertools.combinations(range(len(g)), 2):
        if has[a] and has[b]:
            assert (g[a] == g[b]) == (vt.cy[tr.cur[a]] == vt.cy[tr.cur[b]] and (old[a] > 0) == (old[b] > 0))
    assert len(np.unique(g[~has])) == int((~has).sum())                             # transitions without a triple stay fixed
    gv = wr.strata_of(synth, "voter_old")
    assert np.all((gv[has][:, None] == gv[has][None, :]) == ((vt.voter[tr.cur][has][:, None] == vt.voter[tr.cur][has][None, :]) &
                                                              ((old[has][:, None] > 0) == (old[has][None, :] > 0))))


def test_null_draws_do_not_depend_on_the_number_of_workers(synth):
    import multiprocessing as mp
    if "fork" not in mp.get_all_start_methods():
        pytest.skip("no fork start method on this platform")
    for name in ("voter_uncond", "ev_cur_old"):
        a = wr.run_null(synth, name, 40, 9, workers=1, chunk=10)
        b = wr.run_null(synth, name, 40, 9, workers=3, chunk=10)
        assert np.array_equal(a["cells"], b["cells"]) and np.array_equal(a["conv"], b["conv"])
        assert np.allclose(a["event_share"], b["event_share"], equal_nan=True)
    c = wr.run_null(synth, "ev_cur_old", 40, 10, workers=1, chunk=10)
    assert not np.array_equal(a["cells"], c["cells"])                               # a different seed gives different draws


def test_compare_uses_the_tie_inclusive_monte_carlo_p():
    null = np.array([0.1, 0.2, 0.2, 0.3, np.nan])
    c = wr.compare(0.2, null)
    assert c["B"] == 4 and c["p_ge"] == pytest.approx((1 + 3) / 5) and c["p_le"] == pytest.approx((1 + 3) / 5)
    c = wr.compare(0.5, null)
    assert c["p_ge"] == pytest.approx(1 / 5) and c["p_le"] == pytest.approx(1.0)
    assert np.isnan(wr.compare(float("nan"), null)["p_ge"])


# ------------------------------------------------------------------ (1) machinery: statistics on planted effects

def _planted_cells(rate) -> np.ndarray:
    """A 64-cell count vector with 1000 instances in every (o, s1, s2, old) combination, of which rate(o, s1, s2, old) convert."""
    cells = np.zeros(64, dtype=np.int64)
    for c in range(64):
        if bool(wr.CELL_CHG[c]):
            cells[c] = round(1000 * rate(int(wr.CELL_O[c]), int(wr.CELL_S1[c]), int(wr.CELL_S2[c]), int(wr.CELL_OLD[c])))
        else:
            cells[c] = round(1000 * (1 - rate(int(wr.CELL_O[c]), int(wr.CELL_S1[c]), int(wr.CELL_S2[c]), int(wr.CELL_OLD[c]))))
    return cells


def test_interaction_contrast_ignores_additive_effects_and_picks_up_the_product_rule():
    base = lambda o, a, b, old: 0.2 + 0.1 * (a > 0) + 0.05 * (b > 0)                  # a generous voter, a liked candidate  # noqa: E731
    assert abs(wr.interaction_stats(_planted_cells(base))["I"]) < 1e-9
    balance = lambda o, a, b, old: 0.2 + 0.2 * (a * b * (-old) > 0)                   # convert exactly where the triple is odd-negative  # noqa: E731
    d = wr.interaction_stats(_planted_cells(balance))
    assert d["I"] == pytest.approx(0.4) and all(d["I_" + nm] == pytest.approx(0.4) for nm in wr.ORIENT)
    anti = lambda o, a, b, old: 0.2 + 0.2 * (a * b * (-old) < 0)                      # noqa: E731
    assert wr.interaction_stats(_planted_cells(anti))["I"] == pytest.approx(-0.4)


def test_first_tie_table_from_a_planted_cells_vector():
    rate = lambda o, a, b, old: 0.5 if (o == 1 and a == 1 and b == 1 and old < 0) else 0.1    # FB, old -, both legs +: DLL with the converting tie negative  # noqa: E731
    f = wr.first_tie_stats(_planted_cells(rate))
    assert f["repair_DLL"] == pytest.approx(0.5) and f["repair_LDL"] == pytest.approx(0.1) and f["repair_LLD"] == pytest.approx(0.1)
    assert f["repair_DLL_minus_LDL"] == pytest.approx(0.4) and f["join_DLL"] == pytest.approx(0.1)
    assert sum(f[f"comp_{t}"] for t in wr.DK_UNBALANCED) == pytest.approx(1.0)


def test_join_incidence_split_from_a_planted_cells_vector():
    """The six join cells split by whether the lone negative tie touches the converting voter (DLL-FF, DLL-BF, LLD-FB) or is
    the third party's tie to the candidate (LDL-FF, LDL-FB, LLD-BF); the cell sets are checked against the D&K typing."""
    inc = {(0, -1, 1, 1), (2, -1, 1, 1), (1, -1, 1, 1)}                                  # (orientation, s1, s2, old)
    typ = lambda o, a, b, old: wr.dk_type(o, a, b, old)                                  # noqa: E731
    assert {typ(*c) for c in inc if c[0] == 0} == {"DLL"} and {typ(*c) for c in inc if c[0] == 2} == {"DLL"} and {typ(*c) for c in inc if c[0] == 1} == {"LLD"}
    rate = lambda o, a, b, old: 0.3 if (o, a, b, old) in inc else 0.05                    # noqa: E731
    f = wr.first_tie_stats(_planted_cells(rate))
    assert f["join_inc"] == pytest.approx(0.3) and f["join_notinc"] == pytest.approx(0.05) and f["join_inc_minus_notinc"] == pytest.approx(0.25)


def test_characterise_reports_pairs_concentration_and_gaps(synth):
    ch = wr.characterise(synth)
    keys = synth.vt.voter.astype(np.int64) * synth.vt.n_users + synth.vt.cand
    assert ch["n_pairs_total"] == len(np.unique(keys)) and ch["n_voters_conv"] <= ch["n_voters_revote"]
    assert ch["max_conv_per_voter"] >= 1 and 0 <= ch["top10_voter_share_conv"] <= 1
    assert set(ch["gap_days"]) == {"all", "conv", "nonconv", "up", "down"} and ch["n_conv"] == ch["n_up"] + ch["n_down"]
    assert sum(c for c, _ in ch["by_year"].values()) == ch["n_conv"] and sum(n for _, n in ch["by_year"].values()) == ch["n_trans"]


def test_missing_or_altered_files_fail_loudly_with_the_fetch_command(tmp_path):
    gone = dataclasses.replace(wr.WIKIRFA, path=tmp_path / "nope" / "wiki-RfA.txt.gz")
    with pytest.raises(FileNotFoundError, match="wikirfa_report fetch"):
        wr.require(gone)
    bad = tmp_path / "wiki-RfA.txt.gz"
    bad.write_bytes(b"not the file")
    with pytest.raises(ValueError, match="sha256"):
        wr.require(dataclasses.replace(wr.WIKIRFA, path=bad))


def test_fetch_refuses_a_download_whose_checksum_differs_and_writes_nothing(tmp_path, monkeypatch):
    src = dataclasses.replace(wr.OTC, path=tmp_path / "bitcoin" / "x.csv.gz")

    class Resp(io.BytesIO):
        def __enter__(self):
            return self

        def __exit__(self, *a):
            return False

    monkeypatch.setattr(wr.urllib.request, "urlopen", lambda url, timeout=0: Resp(b"something else"))
    with pytest.raises(ValueError, match="nothing written"):
        wr.fetch(src)
    assert not src.path.exists() and not src.path.parent.exists()
    payload = gzip.compress(b"1,2,3,4.0\n")
    ok = dataclasses.replace(src, sha256=__import__("hashlib").sha256(payload).hexdigest())
    monkeypatch.setattr(wr.urllib.request, "urlopen", lambda url, timeout=0: Resp(payload))
    assert wr.fetch(ok) == src.path and src.path.read_bytes() == payload


def test_report_formatting_helpers():
    from models import wikirfa_report as rep
    assert rep.pc(0.5673) == "56.7%" and rep.pp(0.0312) == "+3.1" and rep.pp(-0.0007, 2) == "-0.07"
    assert rep.fp(1 / 10_001, 10_000) == "<1e-4" and rep.fp(0.0521, 10_000) == "0.052" and rep.fp(0.0004, 10_000) == "4.0e-4"
    t = rep.table(["a", "b"], [["x", "1"]])
    assert t[1] == "| :--- | ---: |" and t[2] == "| x | 1 |"


# ------------------------------------------------------------------ (1) machinery: Bitcoin

def _toy_bitcoin():
    """Pairs: 0-1 rated + by 0 at t=1 and - by 1 at t=0.5 (the earlier one fixes the pair: -), 1-2 (+, t=2), 0-2 (-, t=3),
    2-3 (-, t=4), 1-3 (-, t=5).  Triangles {0,1,2} (-, +, -) and {1,2,3} (+, -, -) have two negatives each; had the later
    rating of 0-1 been used, {0,1,2} would be the one-negative (+, +, -)."""
    rows = [(0, 1, 5, 1.0), (1, 2, 3, 2.0), (0, 2, -2, 3.0), (2, 3, -1, 4.0), (1, 3, -4, 5.0), (1, 0, -3, 0.5)]
    a = np.array(rows)
    return {"src": a[:, 0].astype(np.int64), "dst": a[:, 1].astype(np.int64), "rating": a[:, 2].astype(np.int64), "time": a[:, 3]}


def test_bitcoin_projection_signs_pairs_by_their_earliest_rating_and_counts_triangles_once():
    p = wr.bitcoin_projection(_toy_bitcoin())
    assert len(p.sign) == 5 and p.n_both_signs == 1 and len(p.tri) == 2             # triangles {0,1,2} and {1,2,3}
    pairs = {(int(a), int(b)): int(s) for a, b, s in zip(p.pair_a, p.pair_b, p.sign)}
    assert pairs[(0, 1)] == -1                                                       # the earlier rating 1 -> 0 (-3) decides, not 0 -> 1 (+5)
    st = wr.bitcoin_stats(p.sign, p.tri)
    assert st["n"] == 2 and st["neg_counts"] == [0, 0, 2, 0]                         # {0,1,2}: -, +, - ; {1,2,3}: +, -, -
    assert st["balanced"] == 2


def test_bitcoin_closure_table_orders_edges_by_time():
    d = {"src": np.array([0, 1, 0]), "dst": np.array([1, 2, 2]), "rating": np.array([5, 5, -5]), "time": np.array([1.0, 2.0, 3.0])}
    p = wr.bitcoin_projection(d)
    st = wr.bitcoin_stats(p.sign, p.tri)
    assert st["first_pp"] == 1 and st["close_pos_pp"] == 0 and st["neg_counts"] == [0, 1, 0, 0]       # (+,+) then a negative closer
    assert not p.tied[0]
    d["time"] = np.array([1.0, 1.0, 3.0])
    assert wr.bitcoin_projection(d).tied[0]


def test_bitcoin_nulls_keep_the_pair_count_and_shuffle_signs():
    d = _toy_bitcoin()
    p = wr.bitcoin_projection(d)
    for within in (False, True):
        nl = wr.bitcoin_null(p, d, 30, 3, within_rater=within)
        assert np.all(nl["n"] == 2) and np.all(nl["neg_counts"].sum(1) == 2)
    g = wr.bitcoin_null(p, d, 200, 3)
    assert set(g["balanced"].tolist()) == {1, 2}      # one + among five pairs: on the shared pair both triangles balance, elsewhere one does


# ------------------------------------------------------------------ (2) data: wiki-RfA

@pytest.fixture(scope="module")
def raw() -> wr.RawVotes:
    return wr.load_wikirfa()


@pytest.fixture(scope="module")
def cands(raw) -> wr.Candidacies:
    return wr.assign_candidacies(raw)


@pytest.fixture(scope="module")
def net(raw, cands) -> wr.Network:
    return wr.build_network(raw, cands)


@needs_wiki
def test_wikirfa_file_matches_the_recorded_checksum_and_size():
    assert wr.WIKIRFA.path.stat().st_size == wr.WIKIRFA.size == 14_936_383                   # 117: 14,936,383 bytes [L4561]
    assert wr.sha256_of(wr.WIKIRFA.path) == wr.WIKIRFA.sha256


@needs_wiki
def test_wikirfa_reproduces_117s_vote_counts(raw):
    """L4562: 198,275 votes: 144,451 support, 41,176 oppose, 12,648 neutral; 11,380 named voters; the page's 11,381 users
    include the empty voter field, here 1,661 records.  L4563: votes per year."""
    assert len(raw.voter) == 198_275
    assert collections.Counter(raw.vote.tolist()) == {1: 144_451, -1: 41_176, 0: 12_648}
    assert raw.n_users == 11_380 and raw.notes["n_empty_voter"] == 1_661
    assert len(set(raw.voter[raw.voter >= 0].tolist()) | set(raw.cand.tolist())) == 11_380
    per_year = collections.Counter(raw.yea.tolist())
    assert [per_year[y] for y in range(2003, 2014)] == [203, 6_541, 20_239, 45_325, 41_541, 30_479, 21_375, 13_970, 8_556, 6_474, 3_572]
    assert sum(per_year.values()) == 198_275


@needs_wiki
def test_wikirfa_dates_the_file_has_slips_empties_and_one_impossible_time(raw):
    n = raw.notes
    assert (n["dat_empty"], n["dat_repaired"], n["dat_invalid"]) == (9_367, 3, 1)
    assert n["dat_ok"] + n["dat_repaired"] + n["dat_empty"] + n["dat_invalid"] == 198_275
    ok = ~np.isnan(raw.t)
    lo, hi = raw.t[ok].min(), raw.t[ok].max()
    import datetime
    assert datetime.date.fromordinal(int(lo)).year == 2003 and datetime.date.fromordinal(int(hi)).year == 2013


@needs_wiki
def test_wikirfa_resign_counts_reproduce_117_for_the_changes(raw):
    """L4564 / L4855: 3,761 pairs vote in more than one election year; 677 change sign between first and last non-neutral
    vote (519 oppose to support, 158 support to oppose); 7,793 pairs carry more than one vote (16,330 votes).  117's
    two non-changing cells (1,946 and 647) are NOT reproduced exactly by the stated convention: 1,971 and 632 here."""
    r = wr.resign_counts_117(raw)
    assert r["multi_year_pairs"] == 3_761 and r["pairs_gt1_vote"] == 7_793 and r["votes_in_those"] == 16_330
    assert r["cells"][(-1, 1)] == 519 and r["cells"][(1, -1)] == 158 and r["changes"] == 677
    assert abs(r["cells"][(1, 1)] - 1_946) <= 30 and abs(r["cells"][(-1, -1)] - 647) <= 30


@needs_wiki
def test_wikirfa_election_recorded_twice_finding(cands):
    """18 clusters of one candidate's dated votes carry both outcome labels (the whole election twice); 15 are exact ties."""
    assert cands.notes["n_clusters_with_both_labels"] == 18 and cands.notes["n_clusters_label_tie"] == 15
    assert int((cands.res == 0).sum()) == 15
    assert cands.notes["n_stray_clusters"] == 23 and cands.notes["n_candidacies"] == 4_047


@needs_wiki
def test_wikirfa_network_facts_the_report_relies_on(net):
    vt, tr = net.vt, net.trans
    old, new = net.old_new()
    assert vt.notes["n_usable"] == 184_182 and vt.notes["n_rows"] == 182_996 and vt.notes["n_self"] == 103
    assert len(tr.cur) == 5_990 and int((old != new).sum()) == 1_201
    assert int(((old < 0) & (new > 0)).sum()) == 951 and int(((old > 0) & (new < 0)).sum()) == 250
    assert len(net.ctx.tr) == 229_424
    assert np.all(vt.t[net.ctx.e1] < tr.cutoff[net.ctx.tr]) and np.all(vt.t[net.ctx.e2] < tr.cutoff[net.ctx.tr])
    assert np.all(vt.cy[tr.prev] != vt.cy[tr.cur]) and np.all(vt.t[tr.cur] > vt.t[tr.prev])        # no zero-gap re-votes survive


@needs_wiki
def test_wikirfa_characterisation(net):
    ch = wr.characterise(net)
    assert (ch["n_trans"], ch["n_conv"], ch["n_up"], ch["n_down"]) == (5_990, 1_201, 951, 250)
    assert ch["n_pairs_with_conv"] == 1_176 and ch["n_conv_with_ctx"] == 1_192
    assert ch["rate_conv_old_neg"] == pytest.approx(951 / 1_957) and ch["rate_conv_old_pos"] == pytest.approx(250 / 4_033)
    assert ch["res_cross"]["up"][(-1, 1)] == 665 and ch["share_within_a_year"] > 0.8


@needs_wiki
def test_wikirfa_observed_statistics_are_pinned(net):
    o = wr.observed(net)
    assert (o["d_fix_w"], o["d_brk_w"], o["d_fix_s"], o["d_brk_s"]) == (24_061, 18_353, 26_512, 19_202)
    assert o["d_share_w"] == pytest.approx(0.56729, abs=1e-5) and o["d_share_s"] == pytest.approx(0.57995, abs=1e-5)
    assert o["d_share_w_up"] == pytest.approx(0.65726, abs=1e-5) and o["d_share_w_down"] == pytest.approx(0.30978, abs=1e-5)
    assert [int(o[f"d_n{k}"]) for k in range(4)] == [116_371, 76_525, 31_453, 5_075]
    assert o["d_fix_w"] == o["d_k1"] and o["n_events"] == 1_189


@needs_wiki
def test_wikirfa_types_are_16_and_status_predicts_8(net):
    rows = wr.type_table(net)
    assert len(rows) == 16 and sum(r["n"] for r in rows) == 229_424
    assert sum(1 for r in rows if r["status"] != 0) == 8
    assert sum(r["up"] for r in rows) == int(wr.observed(net)["d_n_chg_up"]) and sum(r["down"] for r in rows) == int(wr.observed(net)["d_n_chg_down"])


@needs_wiki
def test_brief_null_has_even_directions_so_the_headline_is_mostly_the_direction_mix(net):
    """Seeded, 300 draws.  The within-voter shuffle re-determines the conversions and gives about as many + -> - as - -> +
    (observed: 79% - -> +), and its FIX share sits at one half; the observed 0.567 is above it and the context-shuffle
    nulls that hold the observed directions already sit at 0.54-0.56."""
    o = wr.observed(net)
    r = wr.run_null(net, "voter_uncond", 300, 11, workers=1)
    D = wr.derived(r["cells"])
    assert abs(D["share_w"].mean() - 0.5) < 0.01 and abs(r["conv"][:, 1].mean() / r["conv"][:, 0].mean() - 0.5) < 0.02
    assert o["d_share_w"] > D["share_w"].max()
    c = wr.run_null(net, "ctx_voter_res", 300, 11, workers=1)
    assert 0.53 < wr.derived(c["cells"])["share_w"].mean() < 0.56 and np.all(c["conv"][:, 0] == 1_201)


@needs_wiki
def test_event_permutation_null_has_a_lower_fix_share_than_the_data_and_fixed_denominators(net):
    """Seeded, 300 draws of the Newcomb-style null: contexts held, conversions permuted within the same new candidacy and
    old sign.  Its mean FIX share is about 0.536; the data's 0.567 exceeds every draw; the class sizes never move."""
    o = wr.observed(net)
    r = wr.run_null(net, "ev_cur_old", 300, 12, workers=1)
    D = wr.derived(r["cells"])
    assert 0.52 < D["share_w"].mean() < 0.55 and o["d_share_w"] > D["share_w"].max()
    assert np.all(D["n1"] == o["d_n1"]) and np.all(r["conv"][:, 0] == 1_201)


@needs_wiki
def test_the_chain_orientation_shows_no_balance_interaction_and_the_shared_third_party_one_does(net):
    """Seeded, 300 draws.  FF (u -> w -> v, 'a friend of my friend') has an interaction contrast at its null; FB (u and v both
    rated w) is well above it."""
    o = wr.interaction_stats(wr.observed(net)["cells"])
    r = wr.run_null(net, "ev_cur_old", 300, 13, workers=1)
    nul = wr.interaction_stats(r["cells"])
    assert wr.compare(o["I_FF"], nul["I_FF"])["z"] < 2 and wr.compare(o["I_FB"], nul["I_FB"])["z"] > 3
    assert wr.compare(o["I"], nul["I"])["z"] > 3


@needs_wiki
def test_first_tie_table_has_the_dll_join_asymmetry(net):
    o = wr.first_tie_stats(wr.observed(net)["cells"])
    r = wr.run_null(net, "ev_cur_old", 300, 14, workers=1)
    nul = wr.first_tie_stats(r["cells"])
    assert o["join_DLL"] > o["join_LLD"] > o["join_LDL"]
    assert wr.compare(o["join_DLL_minus_LDL"], nul["join_DLL_minus_LDL"])["z"] > 3
    assert abs(wr.compare(o["join_LDL"], nul["join_LDL"])["z"]) < 2.5                        # the second-tie-negative form is at its null


@needs_wiki
@needs_bitcoin
def test_report_orchestration_runs_end_to_end_with_a_few_draws():
    """The report's run() on 8 draws per null: every key the text uses is there and the observed numbers are the pinned ones.
    (build_report itself asserts that the verdict's claims hold, which needs the full 10,000 draws.)"""
    from models import wikirfa_report as rep
    out = rep.run(n_draws=8, seed=1, workers=1, progress=lambda m: None)
    assert set(rep.MAIN_NULLS) == set(out["main"]) and len(out["variants"]) == 10
    assert out["char"]["n_conv"] == 1_201 and out["resign117"]["changes"] == 677 and out["obs"]["d_fix_w"] == 24_061
    for st in out["main"].values():
        assert {"share_w", "event_share", "r1", "I", "I_FB", "ft_join_inc_minus_notinc", "n1"} <= set(st)
    assert out["bitcoin"]["otc"]["all"]["balanced"] == 29_900 and out["bitcoin"]["alpha"]["ordered"]["balanced"] == 17_567
    assert set(out["bitcoin"]["otc"]) >= {"null_global", "null_rater", "null_ratee"}
    assert out["ft_counts"][("DLL", 1)][1] == 9_720


# ------------------------------------------------------------------ (2) data: Bitcoin

@needs_bitcoin
def test_bitcoin_files_match_the_recorded_checksums():
    for src in (wr.OTC, wr.ALPHA):
        assert src.path.stat().st_size == src.size and wr.sha256_of(src.path) == src.sha256   # 397,258 and 149,480 bytes [L4567]


@needs_bitcoin
def test_bitcoin_reproduces_117s_counts_and_the_product_rule():
    """L4568-L4577.  OTC: 35,592 ratings (32,029 positive), 5,881 nodes, 21,492 pairs (358 with both signs), 33,493 triangles,
    the third edge equals the product of the first two in 29,900 (89.3%), null 69.3% (67.9-70.7).  Alpha: 24,186 (22,650),
    3,783 nodes, 14,124 pairs (248), 22,153 triangles of which 20,016 strictly ordered, product rule 17,567 of those (87.8%)."""
    d = wr.load_bitcoin(wr.OTC)
    assert len(d["src"]) == 35_592 and int((d["rating"] > 0).sum()) == 32_029 and int((d["rating"] < 0).sum()) == 3_563 and not (d["rating"] == 0).any()
    assert len(np.unique(d["src"] * 1_000_000 + d["dst"])) == len(d["src"])                  # no ordered pair rated twice [L4571]
    p = wr.bitcoin_projection(d)
    assert (p.n_nodes, len(p.sign), p.n_both_signs, len(p.tri), int(p.tied.sum())) == (5_881, 21_492, 358, 33_493, 0)
    st = wr.bitcoin_stats(p.sign, p.tri)
    assert st["balanced"] == 29_900 and st["neg_counts"] == [24_875, 3_354, 5_025, 239]
    assert (st["first_pp"], st["close_pos_pp"]) == (26_964, 24_875)
    assert (st["first_pm"], st["first_mm"]) == (5_500, 1_029) and round(st["close_pos_pm"] / st["first_pm"], 3) == 0.230
    assert round(st["close_pos_mm"] / st["first_mm"], 3) == 0.768
    nl = wr.bitcoin_null(p, d, 200, 3)
    share = nl["balanced"] / nl["n"]
    assert 0.683 < share.mean() < 0.703 and share.max() < 0.72 and st["balanced"] / st["n"] > share.max() + 0.15
    assert abs(nl["neg_counts"][:, 1].mean() - 10_187) < 150                                  # L4575: about 10,187
    a = wr.load_bitcoin(wr.ALPHA)
    assert len(a["src"]) == 24_186 and int((a["rating"] > 0).sum()) == 22_650
    pa = wr.bitcoin_projection(a)
    assert (pa.n_nodes, len(pa.sign), pa.n_both_signs, len(pa.tri), int(pa.tied.sum())) == (3_783, 14_124, 248, 22_153, 2_137)
    so = wr.bitcoin_stats(pa.sign, pa.tri, ~pa.tied)
    assert so["n"] == 20_016 and so["balanced"] == 17_567
    sa = wr.bitcoin_stats(pa.sign, pa.tri)
    assert (sa["first_pp"], sa["first_pm"], sa["first_mm"]) == (19_814, 1_855, 484) and sa["neg_counts"][1] == 2_518 and sa["neg_counts"][3] == 96


@needs_bitcoin
def test_bitcoin_within_rater_null_is_a_stricter_baseline_than_the_global_shuffle():
    """The global shuffle ignores that some raters are negative far more often than others; keeping each rater's signs, the
    balanced share of the null rises (OTC about 0.73 against 0.69) and, unlike under the global shuffle, the all-negative
    triangle is rarer than the null (239 observed against about 1,000)."""
    d = wr.load_bitcoin(wr.OTC)
    p = wr.bitcoin_projection(d)
    g = wr.bitcoin_null(p, d, 100, 4)
    w = wr.bitcoin_null(p, d, 100, 4, within_rater=True)
    assert (w["balanced"] / w["n"]).mean() > (g["balanced"] / g["n"]).mean() + 0.02
    obs = wr.bitcoin_stats(p.sign, p.tri)
    assert obs["neg_counts"][3] > g["neg_counts"][:, 3].max() and obs["neg_counts"][3] < w["neg_counts"][:, 3].min()
    assert obs["neg_counts"][1] < g["neg_counts"][:, 1].min() and obs["neg_counts"][1] < w["neg_counts"][:, 1].min()
