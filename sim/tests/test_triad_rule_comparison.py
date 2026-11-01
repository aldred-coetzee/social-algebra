"""Which directed triad rule best predicts the sign of a closing or converting tie: the checks.

Module: models/triad_rule_comparison.py; results: results/triad_rule_comparison.md.  Prior work:
docs/prior-work/106 section 1.2 (Leskovec, Huttenlocher & Kleinberg 2010: balance, weak balance, status,
the 16 directed triad types, ledger L4799-L4817), 104 (Newcomb and Doreian & Krackhardt: first-tie
asymmetry, L4481-L4515), 117 sections 3.3-3.4 (the data, L4561-L4580), 112 section 6.5 (the sign-law tests,
whose test 2 is 'person terms dominate').

Three groups.  (1) Machinery, no data: the rule tables against the ledger's definitions and against an
independent re-derivation, the event sweep against a brute-force recount, the NO-LEAKAGE properties (a
target's features are unchanged by deleting everything not yet visible, by flipping any label that is not
yet visible, and a fit is unchanged by the test labels), the metrics, the bootstrap, the permutation null,
the wiki-RfA election builder on synthetic files.  (2) Data tests, skipped with a reason when the
git-ignored files are absent (sim/data/README.md has the sources and terms; the files are not fetched
automatically): the files against the ledger's counts, and the reproduction of 117's undirected closure
counts (L4572-L4577) by a code path independent of the sweep.  (3) Findings regression tests, also
data-dependent: the numbers of results/triad_rule_comparison.md that carry its verdict, with wide
margins.  They assert what was found, not what was hoped; a failure there is a finding, to be recorded and
not tuned away.
"""
from __future__ import annotations

import gzip
import itertools

import numpy as np
import pytest
from scipy.optimize import minimize

from models import newcomb as _nc
from models import triad_rule_comparison as T

needs_bitcoin = pytest.mark.skipif(
    not all((T.BITCOIN_DIR / f).exists() for f in T.BITCOIN_FILES.values()),
    reason="sim/data/bitcoin/*.csv.gz are absent (local-use-only, git-ignored; SNAP soc-sign-bitcoinotc / soc-sign-bitcoinalpha, sim/data/README.md)",
)
needs_wiki = pytest.mark.skipif(
    not T.WIKI_FILE.exists(),
    reason="sim/data/wiki-rfa/wiki-RfA.txt.gz is absent (local-use-only, git-ignored; SNAP wiki-RfA, sim/data/README.md)",
)


# ------------------------------------------------------------------ helpers

def synth_table(rng, n_nodes=9, n_ties=140, n_times=30, elections=False, name="synthetic") -> T.TieTable:
    """A random temporal signed digraph with repeated pairs and many tied times.  elections=True gives
    concurrent, overlapping 'elections': the ties of one election share the cut (its start) and become
    visible together at its end, as in the wiki-RfA primary horizon."""
    u = rng.integers(0, n_nodes, n_ties)
    v = rng.integers(0, n_nodes, n_ties)
    keep = u != v
    u, v = u[keep], v[keep]
    n = len(u)
    s = np.where(rng.random(n) < 0.7, 1, -1).astype(np.int8)
    if elections:
        e = rng.integers(0, 10, n)
        start = 6.0 * np.arange(10) + rng.integers(0, 3, 10)
        end = start + 8.0  # overlaps the next election
        t_cut, t_vis = start[e], end[e]
        t_form = start[e] + rng.integers(0, 8, n)
        g = e.astype(np.int64)
    else:
        t_form = rng.integers(0, n_times, n).astype(float)
        t_cut, t_vis = t_form.copy(), t_form.copy()
        g = t_form.astype(np.int64)
    return T.TieTable(name, u.astype(np.int64), v.astype(np.int64), s, t_form.astype(float), t_vis.astype(float),
                      t_cut.astype(float), np.ones(n, dtype=bool), g, n_nodes)


def assert_event_equal(ev, k, ref, kr):
    assert ev.emb[k] == ref.emb[kr]
    np.testing.assert_array_equal(ev.C[k], ref.C[kr])
    np.testing.assert_array_equal(ev.U[k], ref.U[kr])
    np.testing.assert_array_equal(ev.deg[k], ref.deg[kr])
    assert ev.prev[k] == ref.prev[kr] and ev.recip[k] == ref.recip[kr]
    assert ev.recent[k] == pytest.approx(ref.recent[kr])


def synth_events(rng, n=4000, signal="person", name="synthetic") -> T.Events:
    """Events built directly (no sweep): features with a known data-generating process.
    signal 'person': the sign depends on the four person counts only.  'triad': it depends on the
    FFmp count beyond the person terms.  'none': the sign is independent of everything."""
    deg = rng.poisson(3.0, (n, 4)).astype(np.int32)
    C = np.zeros((n, 48), dtype=np.int16)
    C16 = rng.poisson(0.5, (n, 16)).astype(np.int16)
    C[:, ::3] = C16  # all counts in formation-order state 0
    U = np.column_stack([C16[:, 0] + C16[:, 4], C16[:, 1] + C16[:, 5], C16[:, 2] + C16[:, 6], C16[:, 3] + C16[:, 7]]).astype(np.int16)
    emb = np.maximum(1, C16.sum(axis=1) // 2).astype(np.int32)
    z = 1.2 * (np.log1p(deg[:, 0]) - np.log1p(deg[:, 1])) + 1.5 * (np.log1p(deg[:, 2]) - np.log1p(deg[:, 3])) + 1.0
    if signal == "triad":
        z = z + 1.2 * C16[:, T.TYPE_NAMES.index("FFmp")] - 1.0 * C16[:, T.TYPE_NAMES.index("FFpm")]
    if signal == "none":
        z = np.zeros(n) + 1.0
    y = (rng.random(n) < 1 / (1 + np.exp(-z))).astype(np.int8)
    return T.Events(
        name=name, idx=np.arange(n), u=rng.integers(0, 300, n), v=rng.integers(0, 300, n), y=y, t=np.arange(n, dtype=float),
        g=rng.integers(0, 60, n), C=C, U=U, deg=deg, emb=emb, prev=np.zeros(n, np.int8), recip=np.zeros(n, np.int8),
        recent=np.full(n, 0.5), n_nodes=300,
    )


# ------------------------------------------------------------------ (1a) the rules against the ledger

def test_type_tables_decode_and_name_consistently():
    """The 16 directed types [F|B][F|B][p|m][p|m] (LHK, L4814): index <-> (d1, d2, s1, s2) <-> name."""
    assert len(set(T.TYPE_NAMES)) == 16
    for t in range(16):
        d1, d2, s1, s2 = int(T.TYPE_D1[t]), int(T.TYPE_D2[t]), int(T.TYPE_S1[t]), int(T.TYPE_S2[t])
        assert T.type_index(d1, d2, s1, s2) == t
        assert T.TYPE_NAMES[t] == "FB"[d1] + "FB"[d2] + ("p" if s1 > 0 else "m") + ("p" if s2 > 0 else "m")
    assert T.TYPE_NAMES[0] == "FFpp" and T.TYPE_NAMES[3] == "FFmm" and T.TYPE_NAMES[14] == "BBmp"


def _label(rule: str, t: int, o: int = 0) -> int:
    return int(T.DIRECTED_RULES[rule][t, o])


def test_status_is_the_orient_and_add_rule_and_predicts_8_of_16():
    """L4801, L4196, L5422: orient u -> w -> v, flip a sign when its edge is reversed, predict
    sign(s(u,w) + s(w,v)), silent when they cancel; 8 of the 16 types.  Re-derived here edge by edge."""
    silent = 0
    for t in range(16):
        d1, d2, s1, s2 = int(T.TYPE_D1[t]), int(T.TYPE_D2[t]), int(T.TYPE_S1[t]), int(T.TYPE_S2[t])
        a = s1 * (1 if d1 == 0 else -1)  # u -> w direction kept: sign kept; w -> u reversed: sign flipped
        b = s2 * (1 if d2 == 0 else -1)  # w -> v kept; v -> w reversed
        assert _label("status", t) == int(np.sign(a + b))
        silent += _label("status", t) == 0
    assert silent == 8
    ff = [_label("status", T.TYPE_NAMES.index(n)) for n in ("FFpp", "FFpm", "FFmp", "FFmm")]
    assert ff == [1, 0, 0, -1]  # "status's sum gives (+, 0, 0, -)" [L4811]


def test_balance_weak_and_conjunction_tables():
    """L4800 balance: (+,-,-,+); L4815 weak balance: the same on pp, pm, mp and silent on mm;
    L4811 the learned forward-chain pattern (+,-,-,-), a conjunction."""
    np.testing.assert_array_equal(T.UNDIRECTED_RULES["strict"], [1, -1, -1, 1])
    np.testing.assert_array_equal(T.UNDIRECTED_RULES["weak"], [1, -1, -1, 0])
    ff = [T.TYPE_NAMES.index(n) for n in ("FFpp", "FFpm", "FFmp", "FFmm")]
    assert [_label("conjunction", t) for t in ff] == [1, -1, -1, -1]
    for t in range(16):
        s1, s2 = int(T.TYPE_S1[t]), int(T.TYPE_S2[t])
        assert _label("strict_inst", t) == s1 * s2
        assert _label("weak_inst", t) == (0 if (s1 < 0 and s2 < 0) else s1 * s2)


def test_first_tie_rule_is_balance_with_the_prediction_reversed_when_the_first_tie_is_negative():
    """The Newcomb run's rule (L4508: balance supported when the first tie is positive, contradicted when
    it is negative) as a table.  On a forward chain it equals the sign of the SECOND tie in all four
    cells; elsewhere it is balance (primary), silent (FF only) or the same reversal (all forms)."""
    for t in range(16):
        d1, d2, s1, s2 = int(T.TYPE_D1[t]), int(T.TYPE_D2[t]), int(T.TYPE_S1[t]), int(T.TYPE_S2[t])
        bal = s1 * s2
        if d1 == 0 and d2 == 0:
            assert _label("first_tie", t) == (bal if s1 > 0 else -bal) == s2  # copies the second tie
            assert _label("first_tie_ffonly", t) == s2
        else:
            assert _label("first_tie", t) == bal
            assert _label("first_tie_ffonly", t) == 0
        assert _label("first_tie_all", t) == (bal if s1 > 0 else -bal) == s2
        # copy-incoming: the sign of w -> v when the second tie points at v, silent when v rated w
        assert _label("copy_incoming", t) == (s2 if d2 == 0 else 0)


def test_time_first_rule_copies_the_later_formed_context_tie():
    """Reading 'first' as first-FORMED: reversing balance when the earlier tie is negative equals the sign
    of the later tie; simultaneous ties have no first and the rule is silent."""
    for t in range(16):
        s1, s2 = int(T.TYPE_S1[t]), int(T.TYPE_S2[t])
        assert _label("first_tie_time", t, 0) == s2  # u~w formed first, so w~v is later
        assert _label("first_tie_time", t, 1) == s1  # w~v first, so u~w is later
        assert _label("first_tie_time", t, 2) == 0


def test_a_squared_rule_is_the_net_vote_of_the_matrix_square():
    """v0.1 (4.2a) dA/dt = A^2 [L0898]: the sign predicted for a new tie u -> v is the sign of (A^2)_uv = sum_w a_uw a_wv.
    The 'A^2 sign' rule counts the forward chains u -> w -> v voting s1 * s2, so n_plus - n_minus must equal (A^2)_uv for
    every absent pair of a random signed digraph whose ties are all visible before the target."""
    rng = np.random.default_rng(17)
    n = 9
    A = np.where(rng.random((n, n)) < 0.35, rng.choice([-1, 1], (n, n)), 0)
    np.fill_diagonal(A, 0)
    ii, jj = np.nonzero(A)
    absent = [(u, v) for u in range(n) for v in range(n) if u != v and A[u, v] == 0][:12]
    u = np.concatenate([ii, [a for a, b in absent]])
    v = np.concatenate([jj, [b for a, b in absent]])
    s = np.concatenate([A[ii, jj], np.ones(len(absent), dtype=int)]).astype(np.int8)
    t = np.concatenate([np.arange(len(ii), dtype=float), np.full(len(absent), 1000.0)])
    tt = T.TieTable("a2", u, v, s, t, t.copy(), t.copy(), np.concatenate([np.zeros(len(ii), bool), np.ones(len(absent), bool)]),
                    np.arange(len(u)), n)
    ev = T.build_events(tt)
    A2 = A @ A
    npl, nmi = T.rule_counts(ev, "a_squared")
    for k in range(ev.m):
        uu, vv = int(tt.u[ev.idx[k]]), int(tt.v[ev.idx[k]])
        assert npl[k] - nmi[k] == A2[uu, vv]
    assert ev.m == len(absent)


def test_newcomb_pattern_constants_are_the_copy_second_partition():
    """The eight directions of D&K's Newcomb pattern (L4490-L4498) coincide with 'the closing tie has the
    sign of the second tie' (a property of the constants; the data version is in the Newcomb test below)."""
    assert T.DK_NEWCOMB_DIRECTION == T.DK_COPY_SECOND
    # and strict balance differs from it exactly on the four types with a negative first tie
    differ = [t for t in T.DK_TYPES if T.DK_BALANCE[t] != T.DK_COPY_SECOND[t]]
    assert sorted(differ) == ["DDD", "DDL", "DLD", "DLL"]


# ------------------------------------------------------------------ (1b) the sweep against brute force, and no leakage

HAND_TABLE = dict(
    u=[0, 2, 0], v=[2, 3, 3], s=[1, -1, 1], t=[1.0, 2.0, 3.0],
)


def _hand(u, v, s, t, n=5):
    t = np.array(t, dtype=float)
    return T.TieTable("hand", np.array(u), np.array(v), np.array(s, dtype=np.int8), t, t.copy(), t.copy(),
                      np.ones(len(u), dtype=bool), np.arange(len(u)), n)


def test_hand_example_forward_chain_pm():
    """0 -> 2 (+, t=1), 2 -> 3 (-, t=2), then the target 0 -> 3 (t=3): one common neighbour w = 2, forward
    chain with first tie positive and second negative = FFpm (index 1), the u~w tie formed first (state 0);
    pair-level (p, m) = 'pm'; person counts: u has 1 earlier out-vote (+), v 1 earlier in-vote (-)."""
    ev = T.build_events(_hand(**HAND_TABLE))
    k = int(np.flatnonzero(ev.idx == 2)[0])
    assert ev.emb[k] == 1
    expect = np.zeros(48, dtype=int)
    expect[T.TYPE_NAMES.index("FFpm") * 3 + 0] = 1
    np.testing.assert_array_equal(ev.C[k], expect)
    np.testing.assert_array_equal(ev.U[k], [0, 1, 0, 0])
    np.testing.assert_array_equal(ev.deg[k], [1, 0, 0, 1])
    assert ev.prev[k] == 0 and ev.recip[k] == 0 and ev.pair_first[k]
    # the first two ties have no common neighbour and no context
    assert ev.emb[int(np.flatnonzero(ev.idx == 0)[0])] == 0


def test_hand_example_reverse_chain_and_both_directions():
    """2 -> 0 (-, t=1) and 3 -> 2 (+, t=2): both ties point the 'wrong' way (B, B), signs (m, p): BBmp
    (index 14).  Adding 0 -> 2 (+, t=0.5) makes the u~w pair reciprocated: instances FB.. and BB.. both
    appear, the pair-level sign is 0 (opposite signs in the two directions, L4812) and so casts no undirected vote."""
    ev = T.build_events(_hand(u=[2, 3, 0], v=[0, 2, 3], s=[-1, 1, 1], t=[1.0, 2.0, 3.0]))
    k = int(np.flatnonzero(ev.idx == 2)[0])
    expect = np.zeros(48, dtype=int)
    expect[T.TYPE_NAMES.index("BBmp") * 3 + 0] = 1
    np.testing.assert_array_equal(ev.C[k], expect)
    ev2 = T.build_events(_hand(u=[0, 2, 3, 0], v=[2, 0, 2, 3], s=[1, -1, 1, 1], t=[0.5, 1.0, 2.0, 3.0]))
    k2 = int(np.flatnonzero(ev2.idx == 3)[0])
    c16 = ev2.C16[k2]
    assert c16[T.TYPE_NAMES.index("BBmp")] == 1 and c16[T.TYPE_NAMES.index("FBpp")] == 1 and c16.sum() == 2
    np.testing.assert_array_equal(ev2.U[k2], [0, 0, 0, 0])  # +/- in the two directions: no undirected sign
    assert ev2.emb[k2] == 1


def test_simultaneous_ties_are_never_context_for_each_other():
    """Strict visibility (t_vis < cut): two ties at the same instant, as in Bitcoin Alpha's daily stamps."""
    ev = T.build_events(_hand(u=[0, 2, 0], v=[2, 3, 3], s=[1, 1, 1], t=[1.0, 2.0, 2.0]))
    assert ev.emb.max() == 0  # the target (t=2) does not see the other t=2 tie
    ev = T.build_events(_hand(u=[0, 2, 0], v=[2, 3, 3], s=[1, 1, 1], t=[1.0, 2.0, 2.5]))
    assert ev.emb[int(np.flatnonzero(ev.idx == 2)[0])] == 1


def test_election_ties_are_context_only_after_the_election_ends():
    """wiki-RfA primary horizon: ties of one election share the cut (start) and become visible at its end.
    Election A: 0 -> 2, 2 -> 3 (cut 0, visible 5).  Election B (cut 4, overlapping A): target 0 -> 3 sees nothing.
    Election C (cut 6): target 0 -> 3 sees the A ties as a forward chain."""
    n = 7
    u = np.array([0, 2, 0, 0]); v = np.array([2, 3, 3, 3]); s = np.array([1, 1, 1, 1], dtype=np.int8)
    t_form = np.array([1.0, 2.0, 4.5, 6.5]); t_cut = np.array([0.0, 0.0, 4.0, 6.0]); t_vis = np.array([5.0, 5.0, 9.0, 11.0])
    tt = T.TieTable("el", u, v, s, t_form, t_vis, t_cut, np.ones(4, dtype=bool), np.array([0, 0, 1, 2]), n)
    ev = T.build_events(tt)
    by = {int(i): k for k, i in enumerate(ev.idx)}
    assert ev.emb[by[2]] == 0  # election B starts at 4 < 5: A is still running
    assert ev.emb[by[3]] == 1 and ev.C16[by[3]][T.TYPE_NAMES.index("FFpp")] == 1
    # person counts: u = 0 has one visible out-vote (0 -> 2, election A); election B's 0 -> 3 ends at 9 > 6 and is not visible
    assert ev.deg[by[3]].tolist() == [1, 0, 1, 0]
    assert ev.prev[by[3]] == 0 and ev.pair_first[by[3]]


@pytest.mark.parametrize("elections", [False, True])
def test_sweep_equals_brute_force_on_random_graphs(elections):
    """The sweep (build_events) against a from-scratch recount for EVERY target of several random temporal
    graphs with repeated pairs, tied times and (elections=True) overlapping elections."""
    for seed in range(4):
        rng = np.random.default_rng(100 + seed)
        tt = synth_table(rng, elections=elections)
        ev = T.build_events(tt)
        assert ev.m == tt.n
        for k in range(ev.m):
            e, C, U = T.brute_force_context(tt, int(ev.idx[k]))
            assert e == ev.emb[k]
            np.testing.assert_array_equal(ev.C[k], C)
            np.testing.assert_array_equal(ev.U[k], U)


@pytest.mark.parametrize("elections", [False, True])
def test_no_leakage_prefix_invariance(elections):
    """A target's features depend only on ties visible before its cut: delete every record that is not yet
    visible (keep the target itself) and the features are identical."""
    rng = np.random.default_rng(7)
    tt = synth_table(rng, elections=elections)
    ev = T.build_events(tt)
    for r in rng.choice(tt.n, 25, replace=False):
        keep = (tt.t_vis < tt.t_cut[r]) | (np.arange(tt.n) == r)
        sub = T.TieTable("sub", tt.u[keep], tt.v[keep], tt.s[keep], tt.t_form[keep], tt.t_vis[keep], tt.t_cut[keep],
                         tt.is_target[keep], tt.g[keep], tt.n_nodes)
        evs = T.build_events(sub)
        new_row = int(np.flatnonzero(np.flatnonzero(keep) == r)[0])
        assert_event_equal(ev, int(np.flatnonzero(ev.idx == r)[0]), evs, int(np.flatnonzero(evs.idx == new_row)[0]))


@pytest.mark.parametrize("elections", [False, True])
def test_no_leakage_labels_that_are_not_yet_visible_do_not_matter(elections):
    """Flip the sign of the target and of every record that is not yet visible at its cut: its features do not move."""
    rng = np.random.default_rng(11)
    tt = synth_table(rng, elections=elections)
    ev = T.build_events(tt)
    for r in rng.choice(tt.n, 25, replace=False):
        flip = (tt.t_vis >= tt.t_cut[r]) | (np.arange(tt.n) == r)
        s2 = np.where(flip, -tt.s, tt.s).astype(np.int8)
        tt2 = T.TieTable("flip", tt.u, tt.v, s2, tt.t_form, tt.t_vis, tt.t_cut, tt.is_target, tt.g, tt.n_nodes)
        ev2 = T.build_events(tt2)
        k, k2 = int(np.flatnonzero(ev.idx == r)[0]), int(np.flatnonzero(ev2.idx == r)[0])
        np.testing.assert_array_equal(ev.C[k], ev2.C[k2])
        np.testing.assert_array_equal(ev.U[k], ev2.U[k2])
        np.testing.assert_array_equal(ev.deg[k], ev2.deg[k2])
        assert ev.prev[k] == ev2.prev[k2] and ev.recip[k] == ev2.recip[k2]


def test_frozen_snapshot_hides_ties_formed_after_the_freeze():
    """freeze_at=T: a target at or after T sees only ties visible before T, even if many ties came between."""
    rng = np.random.default_rng(3)
    tt = synth_table(rng, n_ties=200)
    Tf = 15.0
    evf = T.build_events(tt, freeze_at=Tf)
    for k in range(evf.m):
        r = int(evf.idx[k])
        if tt.t_cut[r] >= Tf:
            # the same target, with every record at or after Tf deleted (except itself), gives the same features
            keep = (tt.t_vis < Tf) | (np.arange(tt.n) == r)
            sub = T.TieTable("s", tt.u[keep], tt.v[keep], tt.s[keep], tt.t_form[keep], tt.t_vis[keep], tt.t_cut[keep],
                             tt.is_target[keep], tt.g[keep], tt.n_nodes)
            evs = T.build_events(sub, freeze_at=Tf)
            nr = int(np.flatnonzero(np.flatnonzero(keep) == r)[0])
            kk = int(np.flatnonzero(evs.idx == nr)[0])
            np.testing.assert_array_equal(evf.C[k], evs.C[kk])
            np.testing.assert_array_equal(evf.deg[k], evs.deg[kk])
            break


# ------------------------------------------------------------------ (1c) models, metrics, bootstrap, nulls

def test_logit_intercept_only_is_the_log_odds_of_the_mean():
    y = np.array([1.0] * 30 + [0.0] * 10)
    beta = T.fit_logit(np.zeros((40, 0)), y)
    assert beta[0] == pytest.approx(np.log(0.75 / 0.25), abs=1e-6)
    np.testing.assert_allclose(T.predict_logit(beta, np.zeros((5, 0))), 0.75, atol=1e-8)


def test_logit_minimises_the_ridge_objective():
    """fit_logit against scipy's optimiser on the same penalised negative log-likelihood."""
    rng = np.random.default_rng(0)
    X = rng.normal(size=(300, 3))
    y = (rng.random(300) < 1 / (1 + np.exp(-(X @ [1.0, -0.5, 0.0] + 0.3)))).astype(float)
    beta = T.fit_logit(X, y, l2=2.0)

    def obj(b):
        z = b[0] + X @ b[1:]
        return np.sum(np.logaddexp(0, z) - y * z) + 0.5 * 2.0 * np.sum(b[1:] ** 2)

    ref = minimize(obj, np.zeros(4), method="BFGS", options={"gtol": 1e-10}).x
    np.testing.assert_allclose(beta, ref, atol=1e-4)


def test_metrics_against_hand_values():
    y = np.array([1, 1, 0, 0, 1])
    p = np.array([0.9, 0.6, 0.4, 0.7, 0.2])
    expect = -np.mean([np.log(0.9), np.log(0.6), np.log(0.6), np.log(0.3), np.log(0.2)])
    assert T.logloss_vec(y, p).mean() == pytest.approx(expect)
    # AUC by brute-force pair counting
    pos, neg = p[y == 1], p[y == 0]
    brute = np.mean([(a > b) + 0.5 * (a == b) for a, b in itertools.product(pos, neg)])
    assert T.auc(y, p) == pytest.approx(brute)
    assert T.balanced_accuracy(y, np.array([1, 1, 0, 1, 0])) == pytest.approx(0.5 * (2 / 3 + 1 / 2))


def test_cluster_bootstrap_is_wider_than_iid_when_clusters_are_correlated():
    """Rows in 40 clusters share a large cluster effect: the cluster bootstrap standard error of the mean
    must be several times the naive one, and its mean must be the observed mean."""
    rng = np.random.default_rng(5)
    K, m = 40, 50
    eff = rng.normal(0, 1.0, K)
    x = (eff[:, None] + rng.normal(0, 0.3, (K, m))).ravel()
    cl = np.repeat(np.arange(K), m)
    cols = np.column_stack([x, np.ones_like(x)])
    draws = T.cluster_boot_sums(cols, cl, 1500, np.random.default_rng(1))
    means = draws[:, 0] / draws[:, 1]
    naive = x.std(ddof=1) / np.sqrt(len(x))
    assert means.std(ddof=1) > 4 * naive
    assert means.mean() == pytest.approx(x.mean(), abs=0.05)


def test_permutation_within_groups_preserves_group_composition():
    rng = np.random.default_rng(2)
    groups = rng.integers(0, 6, 200)
    perm = T._perm_within(groups, rng)
    assert sorted(perm.tolist()) == list(range(200))
    np.testing.assert_array_equal(groups[perm], groups)  # each row is replaced by a row of its own group
    y = rng.integers(0, 2, 200)
    order1 = np.argsort(groups, kind="stable")
    y2 = T._group_permute(y, groups, rng, order1)
    for g in range(6):
        assert y[groups == g].sum() == y2[groups == g].sum()


def test_dk_counts_hand_example_and_null_means():
    """Two closing ties: one with an FFpp context (closing +), one with FFmp and FFmm contexts (closing -):
    LLL = 1, DLD = 1, DDD = 1.  Shuffling over all events moves the counts but conserves their totals."""
    C16 = np.zeros((2, 16), dtype=int)
    C16[0, 0] = 1  # FFpp
    C16[1, 2] = 1  # FFmp
    C16[1, 3] = 1  # FFmm
    y = np.array([1, 0])
    obs = T.dk_counts(C16, y)
    d = dict(zip(T.DK_TYPES, obs))
    assert d["LLL"] == 1 and d["DLD"] == 1 and d["DDD"] == 1 and sum(obs) == 3
    sw = T.dk_counts(C16, np.array([0, 1]))
    d2 = dict(zip(T.DK_TYPES, sw))
    assert d2["LLD"] == 1 and d2["DLL"] == 1 and d2["DDL"] == 1 and sum(sw) == 3


def test_dk_event_weights_split_each_closing_tie_once():
    """weights='event': a closing tie with FFpp x3 and FFmp x1 contributes 3/4 and 1/4, however many instances it has;
    a tie without a forward chain contributes nothing.  Totals of the eight counts = number of ties with an FF context."""
    C16 = np.zeros((3, 16), dtype=int)
    C16[0, 0], C16[0, 2] = 3, 1
    C16[1, 3] = 5
    y = np.array([1, 0, 1])
    d = dict(zip(T.DK_TYPES, T.dk_counts(C16, y, "event")))
    assert d["LLL"] == pytest.approx(0.75) and d["DLL"] == pytest.approx(0.25) and d["DDD"] == pytest.approx(1.0)
    assert sum(d.values()) == pytest.approx(2.0)
    di = dict(zip(T.DK_TYPES, T.dk_counts(C16, y, "instance")))
    assert di["LLL"] == 3 and di["DLL"] == 1 and di["DDD"] == 5
    with pytest.raises(ValueError):
        T.dk_counts(C16, y, "nonsense")


def test_dk_static_restricts_to_events_with_a_forward_chain_and_shuffles_within_group():
    """The shuffle pool is the events that have an FF context (a sender's other events are not part of the pool); the
    null mean of every cell's positive count equals sum_e w_e,cell * (sender's positive rate over the pool)."""
    rng = np.random.default_rng(13)
    ev = synth_events(rng, 1500, "person")
    ev.u = rng.integers(0, 40, ev.m)
    ev.C[:300] = 0  # 300 events without any context at all
    mask = np.ones(ev.m, bool)
    r = T.dk_static(ev, mask, "u", B=600, seed=3, weights="event")
    keep = ev.C16[:, :4].sum(1) > 0
    assert r["n_events"] == int(keep.sum())
    e = ev.subset(keep)
    w = e.C16[:, :4] / e.C16[:, :4].sum(1, keepdims=True)
    rate = np.array([e.y[e.u == g].mean() for g in e.u])
    exp_pos = (w * rate[:, None]).sum(0)  # expected positive weight in each cell
    got = [r["mean"][T.DK_TYPES.index(t)] for t in ("LLL", "LDL", "DLL", "DDL")]
    np.testing.assert_allclose(got, exp_pos, rtol=0.05, atol=0.5)


def test_dk_static_sender_by_year_null_keeps_each_sender_year_rate():
    """null='uy' shuffles within (sender, calendar year): the null mean of each cell's positive weight equals
    sum_e w_e,cell * (positive rate of e's sender-year group), which differs from the plain sender null when the
    positive rate drifts between years."""
    rng = np.random.default_rng(23)
    ev = synth_events(rng, 2500, "person")
    ev.u = rng.integers(0, 25, ev.m)
    year_len = 365.25 * 86400.0
    ev.t = np.sort(rng.random(ev.m) * 3 * year_len)
    yr = np.floor(ev.t / year_len).astype(int)
    drift = np.array([0.9, 0.6, 0.3])[yr]  # the positive rate falls year by year
    ev.y = (rng.random(ev.m) < drift).astype(np.int8)
    ev.C[:] = 0
    ev.C[:, 0] = rng.integers(0, 3, ev.m)
    ev.C[:, 6] = rng.integers(0, 3, ev.m)  # FFmp (type 2) lives at column 2 * 3
    keep = ev.C16[:, :4].sum(1) > 0
    e = ev.subset(keep)
    year = np.floor(e.t / year_len).astype(int)
    w = e.C16[:, :4] / e.C16[:, :4].sum(1, keepdims=True)
    grp = e.u * 64 + (year - year.min())
    rate = np.array([e.y[grp == g].mean() for g in grp])
    exp_pos = (w * rate[:, None]).sum(0)
    r = T.dk_static(ev, np.ones(ev.m, bool), "uy", B=500, seed=2, weights="event")
    got = [r["mean"][T.DK_TYPES.index(t)] for t in ("LLL", "LDL", "DLL", "DDL")]
    np.testing.assert_allclose(got, exp_pos, rtol=0.05, atol=0.5)
    r_plain = T.dk_static(ev, np.ones(ev.m, bool), "u", B=500, seed=2, weights="event")
    assert abs(r["mean"][0] - r_plain["mean"][0]) > 0 and r["null"] == "uy"


def test_ff_cell_table_rates_by_hand():
    """Four closing ties: e0 FFpp x2 (+); e1 FFpp x1 + FFmp x1 (-); e2 FFmp x2 (+); e3 FFmm x1 (-).  Per triad:
    pp 2 of 3 positive, mp 2 of 3, mm 0 of 1.  Per closing tie (split over its cells): pp 1.0 of 1.5, mp 1.0 of 1.5, mm 0 of 1."""
    rng = np.random.default_rng(0)
    ev = synth_events(rng, 4)
    ev.C[:] = 0
    ev.C[0, 0 * 3] = 2
    ev.C[1, 0 * 3], ev.C[1, 2 * 3] = 1, 1
    ev.C[2, 2 * 3] = 2
    ev.C[3, 3 * 3] = 1
    ev.y[:] = [1, 0, 1, 0]
    ev.v = np.arange(4)
    rows = T.ff_cell_table(ev, np.ones(4, bool), B=20, seed=1, scheme="v")
    by = {(r["weights"], r["cell"]): r for r in rows}
    assert by[("instance", "FFpp")]["p_pos"] == pytest.approx(2 / 3) and by[("instance", "FFmp")]["p_pos"] == pytest.approx(2 / 3)
    assert by[("instance", "FFmm")]["p_pos"] == 0 and by[("instance", "FFmp")]["instances"] == 3
    assert by[("event", "FFpp")]["p_pos"] == pytest.approx(1.0 / 1.5) and by[("event", "FFmp")]["p_pos"] == pytest.approx(1.0 / 1.5)
    assert by[("event", "FFpp")]["instances"] == pytest.approx(1.5)
    assert by[("instance", "mp - pm")]["p_pos"] == pytest.approx(2 / 3 - 0.0)  # FFpm has no triad: rate 0
    cells = T.cell_table16(ev, np.ones(4, bool))
    assert [c["instances"] for c in cells[:4]] == [3, 0, 3, 1] and cells[0]["type"] == "FFpp" and cells[2]["balance"] == -1


def test_permutation_null_finds_a_planted_triad_effect_and_not_a_null_one():
    """added_value: with the sign driven by the FFmp / FFpm counts beyond the person terms the 16-type block
    adds held-out log-loss and its permutation p is small; with a sign independent of the triads it adds
    nothing and p is large."""
    rng = np.random.default_rng(21)
    ev = synth_events(rng, 5000, "triad")
    r = T.added_value(ev, np.ones(ev.m, bool), 3500.0, ("person",), ("sat16",), (), n_perm=60, seed=1)
    assert r["gain"] > 0.02 and r["p"] < 0.05
    ev0 = synth_events(rng, 5000, "none")
    r0 = T.added_value(ev0, np.ones(ev0.m, bool), 3500.0, ("person",), ("sat16",), (), n_perm=60, seed=1)
    assert r0["gain"] < 0.01 and r0["p"] > 0.1


def test_evaluate_fit_uses_only_training_rows():
    """Changing the labels of the test events (and nothing else) leaves every fitted coefficient unchanged,
    and the first test events' predictions unchanged; flipping a TRAINING label changes the fit."""
    rng = np.random.default_rng(9)
    ev = synth_events(rng, 3000, "person")
    mask = np.ones(ev.m, bool)
    base = T.evaluate(ev, mask, 2000.0, T.VAR_MODELS)
    ev2 = synth_events(np.random.default_rng(9), 3000, "person")
    ev2.y[2000:] = 1 - ev2.y[2000:]
    alt = T.evaluate(ev2, mask, 2000.0, T.VAR_MODELS)
    for m in T.VAR_MODELS:
        np.testing.assert_allclose(base.coef[m], alt.coef[m])
        np.testing.assert_allclose(base.cal[m], alt.cal[m])  # the features are fixed; only the scoring labels moved
    ev3 = synth_events(np.random.default_rng(9), 3000, "person")
    ev3.y[:1000] = 1 - ev3.y[:1000]
    alt3 = T.evaluate(ev3, mask, 2000.0, T.VAR_MODELS)
    assert not np.allclose(base.coef["person propensity"], alt3.coef["person propensity"])


def test_evaluate_ranks_person_signal_above_triad_rules_on_person_data():
    rng = np.random.default_rng(31)
    ev = synth_events(rng, 6000, "person")
    res = T.evaluate(ev, np.ones(ev.m, bool), 4200.0, T.PRIMARY_MODELS)
    ll = {m: res.point(("ll", m)) for m in T.PRIMARY_MODELS}
    assert ll["person propensity"] < ll["strict balance"] - 0.05
    assert ll["person propensity"] < ll["base rate"] - 0.05
    assert ll["person + 16 types"] == pytest.approx(ll["person propensity"], abs=0.01)


def test_variation_counts_keep_the_primary_configuration_once_and_list_every_first_tie_win():
    """The win counts of section 5.5 and the verdict: the recode, split, ridge and horizon tables each repeat the pre-specified
    configuration as their reference row; it is counted once (as 'k >= 1').  ft_ahead_rows lists every distinct configuration
    whose first-tie - strict interval lies wholly below zero, on every site (the review found the verdict naming one of two)."""
    def row(label, d_ft=(0.0, -0.01, 0.01), **ll):
        r = {m: 0.5 for m in T.VAR_MODELS}
        r.update(ll)
        r.update(label=label, d_ft_strict=d_ft, d_p16_person=(0.0, -0.01, 0.01), d_strict_person=(0.0, -0.01, 0.01))
        return r

    win = (-0.02, -0.03, -0.01)
    common = {
        "embeddedness": [row("k >= 1"), row("k >= 2"), {"label": "k >= 25", "n_train": 9, "n_test": 3, "skipped": True}],
        "targets": [row("first tie of the pair (primary)", win)],  # a different model list: never counted
        "time": [row("split 50/50"), row(f"split {int(T.TRAIN_FRAC * 100)}/{100 - int(T.TRAIN_FRAC * 100)}", win), row("rolling origin, 5 blocks from 50%")],
        "ridge": [row("ridge 0.01"), row(f"ridge {T.L2:g}"), row("ridge 100", win, **{"first-tie asymmetric": 0.4})],
    }
    btc = dict(common, recodes=[row("all"), row("drop+1")])
    wiki = dict(common, recodes=[row("neutral: drop"), row("neutral: oppose")],
                horizon=[row("election start (primary)"), row("every earlier dated vote", win)])
    R = {"sites": {"bitcoin-otc": {"variations": btc}, "bitcoin-alpha": {"variations": btc}, "wiki-rfa": {"variations": wiki}}}
    assert [r["label"] for r in T.variation_rows(R, "bitcoin-otc")] == [
        "k >= 1", "k >= 2", "split 50/50", "rolling origin, 5 blocks from 50%", "ridge 0.01", "ridge 100", "drop+1"]
    assert [r["label"] for r in T.variation_rows(R, "wiki-rfa")] == [
        "k >= 1", "k >= 2", "split 50/50", "rolling origin, 5 blocks from 50%", "ridge 0.01", "ridge 100", "neutral: oppose",
        "every earlier dated vote"]
    ahead = T.ft_ahead_rows(R)
    assert [(s, lab) for s, lab, *_ in ahead] == [
        ("bitcoin-otc", "ridge 100"), ("bitcoin-alpha", "ridge 100"), ("wiki-rfa", "ridge 100"), ("wiki-rfa", "every earlier dated vote")]
    assert ahead[0][3] == 0.4 and ahead[0][2] == win
    txt = T._ahead_txt(R, ahead)
    assert txt.startswith("The 4 variation configurations") and "herding" in txt and "worsens from 0.500" in txt


def test_a_rerender_keeps_the_reviews_appended_to_the_results_file():
    """report rewrites the results file; a '## Review (date)' section appended by hand is carried over, not deleted."""
    old = "# Old\n\nold numbers\n\n## Review (2026-11-01)\n\nwhat was checked\n"
    assert T.keep_reviews("# New\n\nnew numbers\n", old) == "# New\n\nnew numbers\n\n## Review (2026-11-01)\n\nwhat was checked\n"
    assert T.keep_reviews("# New\n", "# Old, never reviewed\n") == "# New\n"


def test_rolling_origin_blocks_are_disjoint_and_each_trained_on_the_past():
    rng = np.random.default_rng(41)
    ev = synth_events(rng, 4000, "person")
    mask = rng.random(ev.m) < 0.6
    pooled, folds = T.rolling_origin(ev, mask, 5, 0.5, ("base rate", "person propensity"))
    assert sum(f.n_test for f in folds) == pooled.n_test == int((mask & (ev.t >= np.quantile(ev.t, 0.5, method="lower"))).sum())
    Ts = [f.T for f in folds]
    assert Ts == sorted(Ts) and len(set(Ts)) == 5
    for f in folds:
        assert f.n_train == int((mask & (ev.t < f.T)).sum())


# ------------------------------------------------------------------ (1d) wiki-RfA parsing and elections on synthetic files

def test_wiki_date_parser():
    assert T.parse_wiki_date("23:13, 19 April 2013") == 1366413180.0  # 2013-04-19 23:13 UTC
    assert T.parse_wiki_date("02:41, 29 Oct 2009") == T.parse_wiki_date("02:41, 29 October 2009")
    assert T.parse_wiki_date("14:47, 1 Julu 2012") == T.parse_wiki_date("14:47, 1 July 2012")  # first three letters
    assert T.parse_wiki_date("17:44, 26 Mya 2007") is None
    assert T.parse_wiki_date("31:29, 24 May 2008") is None
    assert T.parse_wiki_date("") is None and T.parse_wiki_date("no date") is None


def test_group_median():
    g = np.array([0, 0, 0, 1, 1, 2])
    x = np.array([5.0, 1.0, 3.0, 2.0, np.nan, np.nan])
    out = T._group_median(g, x, np.array([-1.0, -2.0, -3.0]))
    np.testing.assert_allclose(out, [3.0, 2.0, -3.0])
    out = T._group_median(np.array([0, 0]), np.array([1.0, 4.0]), np.array([0.0]))
    assert out[0] == pytest.approx(2.5)


def test_wiki_elections_split_strays_and_undated_votes():
    """One block with two candidacies 100 days apart (both large) plus a mis-dated stray: two elections,
    stray dropped, the undated vote of an ambiguous block dropped; another block with one candidacy and an
    undated vote keeps it."""
    day = 86400.0
    t0 = 1.2e9
    times = list(t0 + day * np.linspace(0, 5, 14)) + list(t0 + day * (100 + np.linspace(0, 5, 12))) + [t0 + day * 400, np.nan]
    blk = [0] * len(times)
    times2 = list(t0 + day * 900 + day * np.linspace(0, 6, 15)) + [np.nan]
    raw = {"block": np.array(blk + [1] * len(times2)), "time": np.array(times + times2)}
    el = T.wiki_elections(raw)
    e = el["election"]
    assert len(el["e_start"]) == 3 and el["n_multi_blocks"] == 1
    assert (e[:14] == 0).all() and (e[14:26] == 1).all()
    assert e[26] == -1 and e[27] == -1  # the stray, and the undated vote of the two-election block
    assert (e[28:43] == 2).all() and e[43] == 2  # the undated vote of a one-election block joins it
    assert el["e_end"][0] - el["e_start"][0] == pytest.approx(5 * day)


def test_wiki_ties_on_a_synthetic_file(tmp_path, monkeypatch):
    """Neutral votes dropped (or recoded), a self vote and an empty voter dropped, a voter's repeat vote in one
    election collapsed to the last, cut = election start, visibility = election end, comments never read."""
    recs = []

    def rec(src, tgt, vot, res, yea, dat, txt="comment text"):
        recs.append(f"SRC:{src}\nTGT:{tgt}\nVOT:{vot}\nRES:{res}\nYEA:{yea}\nDAT:{dat}\nTXT:{txt}\n")

    for i in range(6):  # election 1, candidate 'C1', dated over 5 days
        rec(f"v{i}", "C1", 1 if i % 2 else -1, 1, 2008, f"1{i}:00, {10 + i} March 2008")
    rec("v0", "C1", 1, 1, 2008, "12:00, 16 March 2008")  # v0 votes again, last one stands (+)
    rec("C1", "C1", 1, 1, 2008, "12:00, 12 March 2008")  # self vote
    rec("", "C1", 1, 1, 2008, "12:00, 12 March 2008")  # empty voter
    rec("v9", "C1", 0, 1, 2008, "12:00, 13 March 2008")  # neutral
    for i in range(5):  # election 2, a different candidate, later
        rec(f"v{i}", "C2", 1, -1, 2008, f"0{i}:30, {1 + i} June 2008")
    path = tmp_path / "w.gz"
    with gzip.open(path, "wt", encoding="utf-8") as f:
        f.write("\n".join(recs))
    monkeypatch.setattr(T, "WIKI_FILE", path)
    tt = T.wiki_ties("drop", "election", verify=False)
    assert tt.n == 6 + 5  # 6 voters in election 1 after collapsing and dropping, 5 in election 2
    c1 = tt.t_cut == tt.t_cut.min()
    assert c1.sum() == 6 and (tt.t_vis[c1] > tt.t_cut[c1]).all() and tt.t_vis[c1].min() == tt.t_vis[c1].max()
    assert tt.t_vis[c1].max() < tt.t_cut[~c1].min()
    # neutral handling
    tt_op = T.wiki_ties("oppose", "election", verify=False)
    assert tt_op.n == tt.n + 1 and (tt_op.s == -1).sum() == (tt.s == -1).sum() + 1
    tt_su = T.wiki_ties("support", "election", verify=False)
    assert (tt_su.s == 1).sum() == (tt.s == 1).sum() + 1
    # vote-level horizon: every dated vote is a target with its own time
    tt_v = T.wiki_ties("drop", "vote", verify=False)
    assert tt_v.is_target.all() and (tt_v.t_cut == tt_v.t_vis).all()
    ev = T.build_events(tt)
    # election 2's candidate (C2) has no earlier tie, so nobody is tied to both a voter and C2: no context anywhere
    assert ev.emb.max() == 0


def test_bitcoin_ties_on_a_synthetic_file(tmp_path, monkeypatch):
    """Sorting of an unsorted file by time (stable for equal stamps), the rating recodes, self ratings dropped."""
    rows = ["5,6,3,200", "5,6,-1,100", "1,2,1,100", "2,2,5,150", "3,4,-5,100", "4,3,2,300"]
    d = tmp_path
    with gzip.open(d / "soc-sign-bitcoinotc.csv.gz", "wt") as f:
        f.write("\n".join(rows) + "\n")
    monkeypatch.setattr(T, "BITCOIN_DIR", d)
    tt = T.bitcoin_ties("otc", "all", verify=False)
    assert tt.n == 5 and (np.diff(tt.t_form) >= 0).all() and tt.t_form[0] == 100
    assert tt.info["distinct_times"] == 3
    tt2 = T.bitcoin_ties("otc", "drop+1", verify=False)  # rating +1 dropped, others kept
    assert tt2.n == 4
    tt3 = T.bitcoin_ties("otc", "drop-1..-4", verify=False)  # -1 dropped, -5 kept
    assert tt3.n == 4 and (tt3.s == -1).sum() == 1


# ------------------------------------------------------------------ (2) the data files against the ledger

@needs_bitcoin
def test_bitcoin_files_match_the_ledger_counts():
    """L4568 (OTC: 35,592 ratings, 5,881 nodes, 32,029 positive, 3,563 negative, no zero, 2010-11-08 18:45 UTC to
    2016-01-25 01:12), L4570 (Alpha: 24,186; 3,783; 22,650; 1,536), L4571 (no ordered pair rated twice).  The
    loader refuses a file whose sha256 differs from the one recorded in sim/data/README.md.  Alpha's
    timestamps being whole days (one stamp per day, at 04:00 or 05:00 UTC; 1,647 distinct) and OTC's being unique
    and sub-second are this module's own counts, not the ledger's."""
    import datetime as dt

    for site, (n, nodes, pos, neg) in {"otc": (35592, 5881, 32029, 3563), "alpha": (24186, 3783, 22650, 1536)}.items():
        src, tgt, rat, tim = T.load_bitcoin_raw(site)
        assert len(src) == n and len(set(src.tolist()) | set(tgt.tolist())) == nodes
        assert (rat > 0).sum() == pos and (rat < 0).sum() == neg and (rat == 0).sum() == 0
        assert len(set(zip(src.tolist(), tgt.tolist()))) == n
        assert rat.min() == -10 and rat.max() == 10
    src, tgt, rat, tim = T.load_bitcoin_raw("otc")
    assert dt.datetime.fromtimestamp(tim.min(), dt.UTC).strftime("%Y-%m-%d %H:%M") == "2010-11-08 18:45"
    assert dt.datetime.fromtimestamp(tim.max(), dt.UTC).strftime("%Y-%m-%d %H:%M") == "2016-01-25 01:12"
    assert len(np.unique(tim)) == len(tim)  # OTC: unique stamps
    assert (tim % 1 != 0).all()  # and sub-second
    src, tgt, rat, tim = T.load_bitcoin_raw("alpha")
    assert len(np.unique(tim)) == 1647 and (tim % 3600 == 0).all()
    assert set(np.unique((tim % 86400) // 3600).astype(int).tolist()) <= {4, 5}  # one stamp per day, 04:00 or 05:00 UTC
    assert len(np.unique(np.floor((tim - 4 * 3600) / 86400))) == 1647  # and never two stamps on one day
    _, counts = np.unique(tim, return_counts=True)
    assert int(counts[counts > 1].sum()) == 24062  # ratings that share their timestamp with another (the report's section 1)


@needs_bitcoin
def test_bitcoin_loader_refuses_a_changed_file(tmp_path, monkeypatch):
    with gzip.open(tmp_path / "soc-sign-bitcoinotc.csv.gz", "wt") as f:
        f.write("1,2,3,100\n")
    monkeypatch.setattr(T, "BITCOIN_DIR", tmp_path)
    with pytest.raises(ValueError):
        T.load_bitcoin_raw("otc")


@needs_wiki
def test_wiki_file_matches_the_ledger_counts():
    """L4562: 198,275 votes, 144,451 support, 41,176 oppose, 12,648 neutral; 11,380 distinct names (L4562 calls them
    'named voters', but 11,380 is voters and candidates together: 10,416 names vote, and 964 candidates never do); the data
    README adds 1,661 empty voter fields and 9,367 votes without a time plus one impossible hour (9,369
    unreadable here, because the three month-name slips 'Mya', 'Julu', 'Janry' are read by their first
    three letters and only 'Mya' fails)."""
    raw = T.load_wiki_raw()
    assert len(raw["src"]) == 198275
    assert (raw["vot"] == 1).sum() == 144451 and (raw["vot"] == -1).sum() == 41176 and (raw["vot"] == 0).sum() == 12648
    assert raw["n_names"] == 11380
    assert len(np.unique(raw["src"][raw["src"] >= 0])) == 10416  # the named voters proper
    assert (raw["src"] < 0).sum() == 1661
    assert np.isnan(raw["time"]).sum() == 9369


@needs_wiki
def test_wiki_elections_and_ties_construction():
    """The election builder keeps nearly every vote, finds elections of about a week (median span 6-7 days), merges
    the elections the file carries twice, and the tie table has strictly positive visibility lag within an election."""
    raw = T.load_wiki_raw()
    el = T.wiki_elections(raw)
    assert (el["election"] >= 0).sum() > 0.99 * len(raw["src"])
    spans = (el["e_end"] - el["e_start"]) / 86400
    assert 5.5 < np.median(spans) < 7.5 and spans.max() <= 40
    assert el["n_merged"] >= 15  # the data README: 15 elections appear twice as complete copies
    tt = T.wiki_ties("drop", "election")
    assert (tt.t_vis >= tt.t_cut).all() and (tt.t_vis > tt.t_cut).mean() > 0.999
    assert tt.n == tt.info["votes_kept"] and abs(tt.n - 182419) < 500  # regression of the construction
    assert 3800 < tt.info["n_elections"] < 3900


# ------------------------------------------------------------------ (2b) 117's closure counts, reproduced independently

@needs_bitcoin
def test_117_undirected_closure_is_reproduced():
    """117 section 3.4: OTC 21,492 pairs and 33,493 triangles [L4572]; starts (+,+) 26,964, (+,-) 5,500, (-,-) 1,029
    with 24,875 / 23.0% / 76.8% closing positive [L4573]; product rule 29,900 of 33,493 [L4574].  Alpha: 14,124 pairs
    and 22,153 triangles [L4572]; 17,567 of the 20,016 triangles with three distinct times follow the product rule
    [L4577]; start classes 19,814 / 1,855 / 484 [L4576] up to the tie-break 117 says it made arbitrarily (<= 3 off)."""
    a = T.undirected_closure("otc")
    assert (a["pairs"], a["triangles"]) == (21492, 33493)
    assert a["starts"] == {"pp": [26964, 24875], "pm": [5500, 1265], "mm": [1029, 790]}
    assert a["product_ok"] == 29900 and a["strict_triangles"] == 33493
    assert round(100 * 1265 / 5500, 1) == 23.0 and round(100 * 790 / 1029, 1) == 76.8
    b = T.undirected_closure("alpha")
    assert (b["pairs"], b["triangles"]) == (14124, 22153)
    assert (b["strict_triangles"], b["strict_product_ok"]) == (20016, 17567)
    for key, n117 in (("pp", 19814), ("pm", 1855), ("mm", 484)):
        assert abs(b["starts"][key][0] - n117) <= 3


@needs_bitcoin
@pytest.mark.parametrize("site", ["otc", "alpha"])
def test_sweep_on_real_bitcoin_matches_brute_force(site):
    """The event sweep against a from-scratch recount on 40 random real events of each site, and the target-set sizes
    that the results file reports (a regression of the construction)."""
    tt = T.bitcoin_ties(site)
    ev = T.build_events(tt)
    rng = np.random.default_rng(5)
    for k in rng.choice(ev.m, 40, replace=False):
        e, C, U = T.brute_force_context(tt, int(ev.idx[k]))
        assert e == ev.emb[k]
        np.testing.assert_array_equal(ev.C[k], C)
        np.testing.assert_array_equal(ev.U[k], U)
    expect = {"otc": (14934, 8972), "alpha": (9497, 7875)}[site]
    assert (int((ev.emb >= 1).sum()), int(T.mask_closing(ev).sum())) == expect


@needs_wiki
def test_sweep_on_real_wiki_matches_brute_force_and_never_uses_the_same_election():
    tt = T.wiki_ties("drop", "election")
    ev = T.build_events(tt)
    rng = np.random.default_rng(6)
    for k in rng.choice(ev.m, 25, replace=False):
        e, C, U = T.brute_force_context(tt, int(ev.idx[k]))
        assert e == ev.emb[k]
        np.testing.assert_array_equal(ev.C[k], C)
    # every context tie of an event comes from an election that ended before the event's election started
    r = int(ev.idx[int(rng.integers(0, ev.m))])
    vis = tt.t_vis < tt.t_cut[r]
    same = tt.g == tt.g[r]
    assert not (vis & same).any()


# ------------------------------------------------------------------ (2c) the Newcomb re-read (post hoc)

needs_newcomb = pytest.mark.skipif(
    not _nc.DATA_FILE.exists(),
    reason="sim/data/newcomb/newfrat.dat is absent (local-use-only, git-ignored): cd sim && ~/.local/bin/uv run python -m models.newcomb_report fetch",
)


@needs_newcomb
def test_newcomb_pattern_is_the_copy_second_partition_and_shrinks_when_reception_is_held():
    """POST HOC (not in the pre-specification).  Under D&K's row-wise null (L4485) the sides of the eight types
    (L4490-L4498; exact null means from models.newcomb.expected_triple_counts) match the partition 'closing sign =
    second-tie sign' in all eight cells from the second wave on (7 of 8 at wave 1).  Under a column-wise null (each
    man's received signs held, permuted across senders) the same eight cells agree with the partition at chance
    level (4-6 of 8 in every wave) and no cell of any wave is further than 4 SD from its null, against up to 15 SD
    under the row-wise null.  The first tie is not part of the partition, so the Newcomb 'first-tie asymmetry' and
    a consensus about the third man (D&K's 'recognition of attributes', L4512) are the same pattern in these data."""
    r = T.newcomb_reception_check(n_draws=300, seed=1)
    assert (r["agree_copy_row"][1:] == 8).all() and r["agree_copy_row"][0] >= 7
    assert (r["agree_newcomb_row"] == r["agree_copy_row"]).all()  # the Newcomb pattern IS the partition
    assert r["agree_copy_col"].max() <= 6 and r["agree_copy_col"].mean() < 6
    assert r["max_abs_z_col"].max() < 4.0
    assert np.abs(r["z_row"]).max() > 10


# ------------------------------------------------------------------ (2d) end-to-end smoke of the report (quick mode)

@needs_bitcoin
@needs_wiki
def test_report_renders_end_to_end_in_quick_mode(tmp_path):
    """run_all(quick=True) and render_report on the real files: no crash, every section present, the numbers that
    are stated in prose agree with the tables they come from, and the CLI re-renders the same text from a pickle."""
    import pickle

    R = T.run_all(quick=True)
    text = T.render_report(R)
    pkl, out = tmp_path / "R.pkl", tmp_path / "out.md"
    pkl.write_bytes(pickle.dumps(R))
    assert T.main(["report", "--from-pickle", str(pkl), "--out", str(out)]) == 0
    assert out.read_text(encoding="utf-8") == text
    for head in ("## Verdict", "## 1. Data, terms, target sets", "## 2. Method", "## 3. Primary results",
                 "## 4. Does the first-tie asymmetry replicate outside the fraternity?", "## 5. Variations",
                 "### 5.4 Which form of each rule fits best", "## 6. Reproduction of file 117's undirected closure counts", "## 7. Caveats"):
        assert head in text
    assert "QUICK MODE" in text
    assert text.count("| strict balance |") >= 3
    P = R["sites"]["bitcoin-otc"]["primary"]
    assert P["res"].n_train + P["res"].n_test == int(P["mask"].sum())
    assert f"{P['res'].n_test:,}" in text


# ------------------------------------------------------------------ (3) the findings that carry the verdict (regression)
# These assert what results/triad_rule_comparison.md reports, with margins wide enough for the smaller bootstrap
# used here (B = 300) and the seeded Monte Carlo.  They are findings, not hypotheses: if one fails after a code
# change, the result changed, and the verdict in the results file and the module's prose have to be revisited.

@pytest.fixture(scope="module")
def findings():
    out = {}
    for site in T.SITE_NAMES:
        ev = T.site_events(site, T.default_recode(site))
        Tsp = T.split_time(ev)
        mask = T.mask_closing(ev)
        res = T.evaluate(ev, mask, Tsp, T.PRIMARY_MODELS, (), T.SITE_SCHEMES[site], 300, T.SEED, name=site)
        out[site] = {
            "ev": ev, "T": Tsp, "mask": mask, "res": res,
            "dk_u": T.dk_static(ev, mask, "u", 300, T.SEED, "event"),
            "dk_v": T.dk_static(ev, mask, "v", 300, T.SEED, "event"),
            "ff": {(r["weights"], r["cell"]): r for r in T.ff_cell_table(ev, mask, 200, T.SEED, T.SITE_SCHEMES[site][1])},
            "coef": T.ff_coefficients(ev, mask, ("person", "sat16"), 40, T.SEED, T.SITE_SCHEMES[site][1]),
        }
    return out


OTC, ALPHA, WIKI = T.SITE_NAMES
DLL = T.DK_TYPES.index("DLL")


def _ll(f, site, m):
    return f[site]["res"].point(("ll", m))


def _diff(f, site, a, b):
    pt, lo, hi, _ = f[site]["res"].diff(a, b)
    return pt, lo, hi


@needs_bitcoin
@needs_wiki
def test_finding_balance_is_the_best_single_rule_and_status_the_worst(findings):
    """Held-out log-loss: weak balance is within 0.003 of strict balance everywhere and the lowest of the four canonical rules
    on OTC and wiki-RfA (and level with them on Alpha); status is last on all three; on wiki-RfA weak beats strict by 0.004+."""
    f = findings
    for s in T.SITE_NAMES:
        assert _ll(f, s, "weak balance") <= _ll(f, s, "strict balance") + 0.003
        assert _ll(f, s, "status") > max(_ll(f, s, m) for m in ("strict balance", "weak balance", "first-tie asymmetric"))
    assert 0.22 < _ll(f, OTC, "weak balance") < 0.31 and _ll(f, OTC, "weak balance") < _ll(f, OTC, "first-tie asymmetric") - 0.08
    assert _diff(f, WIKI, "weak balance", "strict balance")[2] < -0.003
    assert abs(_ll(f, ALPHA, "weak balance") - _ll(f, ALPHA, "first-tie asymmetric")) < 0.01
    pt, lo, hi = _diff(f, ALPHA, "status", "base rate")
    assert lo < 0 < hi  # status is not distinguishable from the base rate on Alpha


@needs_bitcoin
@needs_wiki
def test_finding_first_tie_rule_is_not_better_than_balance_at_the_primary_split(findings):
    """first-tie minus strict balance at the pre-specified split: OTC clearly worse (CI wholly above 0, +0.14 in the report);
    Alpha and wiki-RfA within 0.02 and 0.004, with no interval wholly below zero.  Not 'never': two variation configurations
    (Alpha at ridge 100, wiki-RfA's vote-level horizon) have it ahead of strict balance by its interval, and the report
    lists them (ft_ahead_rows)."""
    f = findings
    pt, lo, hi = _diff(f, OTC, "first-tie asymmetric", "strict balance")
    assert lo > 0.04 and pt > 0.08
    for s, bound in ((ALPHA, 0.02), (WIKI, 0.004)):
        pt, lo, hi = _diff(f, s, "first-tie asymmetric", "strict balance")
        assert abs(pt) < bound and hi > -0.003 and not (hi < 0)


@needs_bitcoin
@needs_wiki
def test_finding_person_terms_dominate_on_alpha_and_wiki_not_on_otc(findings):
    """112 section 6.5 test 2: person propensity beats the best single triad rule on Alpha and wiki-RfA; on OTC strict balance
    alone beats the person terms alone at the pre-specified split, and the triad terms add a great deal to the person terms."""
    f = findings
    assert _ll(f, ALPHA, "person propensity") < _ll(f, ALPHA, "weak balance") - 0.03
    assert _ll(f, WIKI, "person propensity") < _ll(f, WIKI, "weak balance") - 0.02
    assert _diff(f, OTC, "strict balance", "person propensity")[2] < 0
    assert _diff(f, OTC, "person + 16 types", "person propensity")[2] < -0.03
    assert _diff(f, WIKI, "person + 16 types", "person propensity")[2] < 0  # small but real


@needs_bitcoin
@needs_wiki
def test_finding_dll_is_not_over_represented_on_bitcoin_but_is_on_wiki_under_the_sender_null(findings):
    """The static replication (event weights): under the formation-ordered analogue of the Newcomb run's row-wise null (closing
    signs shuffled within sender, the context ties held) DLL is
    BELOW its null on OTC (z -19 in the report) and Alpha (-5.6) and ABOVE it on wiki-RfA (+2.5, 8 of 8 directions as in the
    fraternity); with reception held (shuffle within receiver) DLL is below its null on all three."""
    f = findings
    for s, zmax in ((OTC, -8.0), (ALPHA, -2.0)):
        assert f[s]["dk_u"]["side"][DLL] == -1 and f[s]["dk_u"]["z"][DLL] < zmax
        assert f[s]["dk_u"]["agree_newcomb"] <= 6
    assert f[OTC]["dk_u"]["agree_balance"] == 8
    assert f[WIKI]["dk_u"]["side"][DLL] == 1 and f[WIKI]["dk_u"]["z"][DLL] > 1.0 and f[WIKI]["dk_u"]["agree_newcomb"] == 8
    for s in T.SITE_NAMES:
        assert f[s]["dk_v"]["side"][DLL] == -1 and f[s]["dk_v"]["z"][DLL] < -5.0


@needs_bitcoin
@needs_wiki
def test_finding_raw_cell_contrast_only_on_alpha_and_none_given_person_terms(findings):
    """P(closing +) after (first -, second +) minus after (first +, second -), event-weighted: about zero on OTC, clearly positive
    on Alpha (+0.44 in the report), reversed on wiki-RfA (-0.15).  Given the person terms the coefficient contrast FFmp - FFpm is
    zero within its interval on all three; the product structure of balance is strongly positive on Bitcoin."""
    f = findings
    assert abs(f[OTC]["ff"][("event", "mp - pm")]["p_pos"]) < 0.1
    assert f[ALPHA]["ff"][("event", "mp - pm")]["lo"] > 0.2
    assert f[WIKI]["ff"][("event", "mp - pm")]["hi"] < -0.08
    for s in T.SITE_NAMES:
        pt, lo, hi = f[s]["coef"]["mp_minus_pm"]
        assert lo < 0 < hi
    assert f[OTC]["coef"]["balance_interaction"][1] > 1.0 and f[ALPHA]["coef"]["balance_interaction"][1] > 0.3
    assert f[OTC]["coef"]["cells"]["FFmm"][1] > 0 and f[ALPHA]["coef"]["cells"]["FFmm"][1] > 0  # LHK's 'FFmm negative' does not transfer
    assert f[WIKI]["coef"]["cells"]["FFmm"][1] < 0 < f[WIKI]["coef"]["cells"]["FFmm"][2]


@needs_wiki
def test_finding_converting_ties_persistence_plus_balance():
    """wiki-RfA re-votes: every model includes the previous sign; weak balance improves on persistence alone by 0.01+ (CI wholly
    below zero) and the 16 types add nothing to the person terms."""
    ev = T.site_events("wiki-rfa", "drop")
    Tsp = T.split_time(ev)
    res = T.evaluate(ev, T.mask_converting(ev), Tsp, T.PRIMARY_MODELS, ("prev",), ("u", "g"), 300, T.SEED)
    pt, lo, hi, _ = res.diff("weak balance", "base rate")
    assert hi < 0 and pt < -0.01
    pt, lo, hi, _ = res.diff("person + 16 types", "person propensity")
    assert lo < 0 < hi


@needs_newcomb
def test_finding_newcomb_pattern_row_null_is_the_partition_even_with_exact_means():
    """Same as the Newcomb test above with the production sample size (2,000 draws): the exact-null-mean sides match the
    partition in 14 of 15 waves in all eight cells."""
    r = T.newcomb_reception_check(n_draws=2000, seed=T.SEED)
    assert int((r["agree_copy_row"] == 8).sum()) == 14 and r["agree_copy_row"][0] == 7


def test_results_file_is_a_full_run_with_a_verdict():
    """sim/results/triad_rule_comparison.md must be the full seeded run (not --quick) and carry a verdict."""
    if not T.RESULTS_FILE.exists():
        pytest.skip("sim/results/triad_rule_comparison.md has not been generated: cd sim && ~/.local/bin/uv run python -m models.triad_rule_comparison report")
    text = T.RESULTS_FILE.read_text(encoding="utf-8")
    assert "QUICK MODE" not in text and "(verdict pending)" not in text
    for head in ("## Verdict", "**Bottom line.**", "## 4. Does the first-tie asymmetry replicate outside the fraternity?", "## 5. Variations", "## 7. Caveats"):
        assert head in text
