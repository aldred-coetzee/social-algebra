"""Newcomb fraternity: the n = 3 refutation test of models/00-v0.md section 7, run on data, and the
checks that the machinery behind it is right.

Prior work: docs/prior-work/104-newcomb-doreian-krackhardt-at-source.md (D596); 084 sections 4-6.
Ledger ids are the lines with source "104 §..." (L4471-L4546).  Results and verdict:
sim/results/newcomb_n3.md, produced by models/newcomb_report.py from the same functions.

Two groups.  (1) Machinery, no data needed: counting vs brute force, null samplers vs closed forms,
the conditional shuffles' invariants, the conversion arithmetic on a hand example.  (2) Data tests,
skipped with a reason when the git-ignored rank file is absent (fetch it with
`cd sim && ~/.local/bin/uv run python -m models.newcomb_report fetch`; the data are not
redistributable, sim/data/README.md): the file's integrity, agreement with numbers the 1996 paper
published for the same ranks, D&K's reported Figure 1 pattern (a non-reproduction is a finding,
recorded, not tuned away), and the new transition counts.  Seeds are fixed; the null draws are
Monte Carlo, so seeded assertions are qualitative or have wide margins.
"""
from __future__ import annotations

import itertools
import re

import numpy as np
import pytest

from models import newcomb as nc

needs_data = pytest.mark.skipif(
    not nc.DATA_FILE.exists(),
    reason="sim/data/newcomb/newfrat.dat is absent (local-use-only, git-ignored): "
    "cd sim && ~/.local/bin/uv run python -m models.newcomb_report fetch",
)
OFF = nc.OFF_COLS


# ------------------------------------------------------------------ (1) machinery

def _brute_triples(S):
    out = np.zeros(8, dtype=int)
    for i, j, k in itertools.permutations(range(S.shape[0]), 3):
        a, b, c = int(S[i, j]), int(S[j, k]), int(S[i, k])
        if a and b and c:
            out[4 * (a < 0) + 2 * (b < 0) + (c < 0)] += 1
    return out


def _brute_triangles(s):
    out = np.zeros(4, dtype=int)
    for i, j, k in itertools.combinations(range(s.shape[0]), 3):
        a, b, c = int(s[i, j]), int(s[i, k]), int(s[j, k])
        if a and b and c:
            out[(a < 0) + (b < 0) + (c < 0)] += 1
    return out


def test_parse_dl_reads_labels_and_matrices():
    """The UCINET DL full-matrix reader (the format of newfrat.dat [L4538]) on a toy file."""
    text = "DL\r\nN=2 NM=2\r\nFORMAT = FULLMATRIX DIAGONAL PRESENT\r\nLEVEL LABELS:\r\nA\r\nB\r\nDATA:\r\n 0 1\r\n 1 0\r\n 0 2\r\n 1 0\r\n"
    labels, arr = nc.parse_dl(text)
    assert labels == ("A", "B")
    assert arr.tolist() == [[[0, 1], [1, 0]], [[0, 2], [1, 0]]]
    with pytest.raises(ValueError):
        nc.parse_dl(text.replace(" 1 0\r\n", "", 1))


def test_recode_row_composition_for_every_cut():
    """Top-n_pos -> +, bottom-n_neg -> -, rest 0, diagonal 0 [L4476, L4478]: every row of any rank matrix gets exactly
    n_pos '+', n_neg '-' and 16 - n_pos - n_neg zeros, so 68 + and 51 - ties per wave at 4/3 [L4480]."""
    rng = np.random.default_rng(0)
    ranks = np.zeros((nc.N, nc.N), dtype=np.int8)
    for i in range(nc.N):
        ranks[i, OFF[i]] = rng.permutation(np.arange(1, nc.N))
    for (npos, nneg) in nc.RECODES.values():
        S = nc.recode(ranks, npos, nneg)
        rows = S[nc.ROWS, OFF]
        assert ((rows == 1).sum(1) == npos).all() and ((rows == -1).sum(1) == nneg).all()
        assert (S[np.arange(nc.N), np.arange(nc.N)] == 0).all()
    S = nc.recode(ranks)
    assert (S == 1).sum() == 68 and (S == -1).sum() == 51
    assert S[ranks == 4].min() == 1 and S[ranks == 5].max() == 0 and S[ranks == 13].max() == 0 and S[ranks == 14].max() == -1


@pytest.mark.parametrize("seed", range(4))
def test_counting_matches_brute_force(seed):
    """triple_counts (8 ordered types, L4481) and triangle_counts (0-3 negative edges) against loops over every
    triple, on D&K-shaped and on dense random sign matrices, for both symmetrisation rules."""
    rng = np.random.default_rng(seed)
    mats = [nc.null_signs(rng, 1)[0], rng.integers(-1, 2, size=(nc.N, nc.N)).astype(np.int8)]
    for S in mats:
        S = S.copy()
        S[np.arange(nc.N), np.arange(nc.N)] = 0
        assert np.array_equal(nc.triple_counts(S), _brute_triples(S))
        for rule in nc.SYM_RULES:
            s = nc.symmetrise(S, rule)
            assert np.array_equal(s, s.T) and not np.diag(s).any()
            assert np.array_equal(nc.triangle_counts(s), _brute_triangles(s))
        # codes are the same classification as the counts
        assert np.array_equal(np.bincount(nc.triple_codes(S), minlength=9)[:8], nc.triple_counts(S))
        s = nc.symmetrise(S, "sum")
        assert np.array_equal(np.bincount(nc.triangle_codes(s), minlength=5)[:4], nc.triangle_counts(s))
        d = s[nc.DY_I, nc.DY_J]
        assert np.array_equal(nc.triangle_codes_from_dyads(d), nc.triangle_codes(s))


def test_symmetrisation_rules_on_the_four_cases():
    """'agree': the common sign if both directions carry the same value; 'sum': sign of the sum.  Both modelling choices."""
    S = np.zeros((3, 3), dtype=np.int8)
    S[0, 1], S[1, 0] = 1, 1  # mutual +
    S[0, 2], S[2, 0] = 1, 0  # one-way +
    S[1, 2], S[2, 1] = 1, -1  # conflict
    assert nc.symmetrise(S, "agree")[[0, 0, 1], [1, 2, 2]].tolist() == [1, 0, 0]
    assert nc.symmetrise(S, "sum")[[0, 0, 1], [1, 2, 2]].tolist() == [1, 1, 0]
    with pytest.raises(ValueError):
        nc.symmetrise(S, "max")


def test_type_vocabulary_matches_the_ledger():
    """Eight types named (i->j)(j->k)(i->k) [L4481]; balanced = even number of D [L4482]; Davis also allows DDD [L4483].
    (The brief's '16 D&K types' is Leskovec's 16 directed triad types, 084 section 4; D&K have eight.)"""
    assert len(nc.TRIPLE_TYPES) == 8 and len(set(nc.TRIPLE_TYPES)) == 8
    even = tuple(t for t in nc.TRIPLE_TYPES if t.count("D") % 2 == 0)
    assert set(even) == set(nc.TRIPLE_BALANCED) == {"LLL", "LDD", "DLD", "DDL"}
    assert set(nc.TRIPLE_ONE_NEG) == {t for t in nc.TRIPLE_TYPES if t.count("D") == 1}
    lv = nc.TRIPLE_LEVEL
    assert {nc.TRIPLE_TYPES[c] for c in lv.weak_bal} == set(nc.TRIPLE_BALANCED) | {"DDD"}
    assert nc.TRIANGLE_LEVEL.strict_bal == (0, 2) and nc.TRIANGLE_LEVEL.weak_bal == (0, 2, 3)


def test_row_shuffle_null_has_the_closed_form_means():
    """D&K's null [L4485]: each man's 4 L / 3 D / 9 0 re-arranged at random.  Means of the eight type counts and of the
    four 'agree' triangle counts equal the closed forms (rows independent; ties i->j and i->k share row i), and the
    reciprocated-positive count has mean 17, the 1996 paper's null level [L4521]."""
    null = nc.static_null(np.random.default_rng(1), 20000)
    se = null["triple"].std(0, ddof=1) / np.sqrt(20000)
    assert np.all(np.abs(null["triple"].mean(0) - nc.expected_triple_counts()) < 5 * se)
    se = null["agree"].std(0, ddof=1) / np.sqrt(20000)
    assert np.all(np.abs(null["agree"].mean(0) - nc.expected_agree_triangle_counts()) < 5 * se)
    assert abs(null["recip"].mean() - 17.0) < 5 * null["recip"].std(ddof=1) / np.sqrt(20000)
    assert nc.expected_triple_counts().sum() == pytest.approx(4080 * (7 / 16) * (6 / 15) * (7 / 16))
    assert nc.expected_agree_triangle_counts()[0] == pytest.approx(680 * (4 / 16 * 3 / 15) ** 3)


def test_row_shuffle_null_keeps_row_composition():
    S = nc.null_signs(np.random.default_rng(2), 200, 5, 4)
    rows = S[:, nc.ROWS, OFF]
    assert ((rows == 1).sum(-1) == 5).all() and ((rows == -1).sum(-1) == 4).all()
    assert (S[:, np.arange(nc.N), np.arange(nc.N)] == 0).all()


def test_conditional_row_shuffle_keeps_start_and_every_mans_transition_table():
    """The 'cond' null for directed triples: S_w untouched, each man's (start, end) multiset preserved, only WHICH ties change moves."""
    rng = np.random.default_rng(3)
    S0, S1 = nc.null_signs(rng, 1)[0], nc.null_signs(rng, 1)[0]
    out = nc.null_next_within_rows(rng, S0, S1, 40)
    assert out.shape == (40, nc.N, nc.N) and (out[:, np.arange(nc.N), np.arange(nc.N)] == 0).all()
    for d in range(40):
        for i in range(nc.N):
            assert sorted(zip(S0[i, OFF[i]], out[d, i, OFF[i]])) == sorted(zip(S0[i, OFF[i]], S1[i, OFF[i]]))
    assert (out != S1).any()
    # uniformity: in a stratum of m targets holding the multiset of end states, each target gets a given state with the right frequency
    big = nc.null_next_within_rows(rng, S0, S1, 6000)
    i = 5
    plus = [j for j in OFF[i] if S0[i, j] == 1]
    ends = [S1[i, j] for j in plus]
    for state in set(ends):
        freq = (big[:, i, plus] == state).mean(0)
        assert np.allclose(freq, ends.count(state) / len(plus), atol=0.04)


def test_conditional_dyad_shuffle_keeps_start_and_the_dyad_transition_table():
    rng = np.random.default_rng(4)
    s0 = nc.symmetrise(nc.null_signs(rng, 1)[0], "sum")
    s1 = nc.symmetrise(nc.null_signs(rng, 1)[0], "sum")
    out = nc.null_next_within_dyads(rng, s0, s1, 30)
    a, b = s0[nc.DY_I, nc.DY_J], s1[nc.DY_I, nc.DY_J]
    assert out.shape == (30, 136)
    for d in range(30):
        assert sorted(zip(a, out[d])) == sorted(zip(a, b))
    assert (out != b).any()


def test_null_transitions_wiring_matches_a_manual_pipeline():
    """null_transitions composes shuffle -> type codes -> transition counts; written out by hand with the same seed the three pipelines
    ('cond' directed, 'cond' triangle under 'sum', 'indep') give the same counts, so the wiring (waves, strata, levels) is right."""
    S = nc.null_signs(np.random.default_rng(9), 15)  # fifteen synthetic waves
    out = nc.null_transitions(S, nc.TRIPLE_LEVEL, None, "cond", 6, np.random.default_rng(1))
    assert out.shape == (14, 6, 9, 9)
    Sn = nc.null_next_within_rows(np.random.default_rng(1), S[0], S[1], 6)
    assert np.array_equal(out[0], nc.transition_counts(nc.triple_codes(S[0]), nc.triple_codes(Sn), 9))

    out = nc.null_transitions(S, nc.TRIANGLE_LEVEL, "sum", "cond", 6, np.random.default_rng(2))
    s = nc.symmetrise(S, "sum")
    d = nc.null_next_within_dyads(np.random.default_rng(2), s[0], s[1], 6)
    s_next = np.zeros((6, nc.N, nc.N), dtype=np.int8)
    s_next[:, nc.DY_I, nc.DY_J] = d
    s_next[:, nc.DY_J, nc.DY_I] = d
    assert np.array_equal(out[0], nc.transition_counts(nc.triangle_codes(s[0]), nc.triangle_codes(s_next), 5))

    out = nc.null_transitions(S, nc.TRIANGLE_LEVEL, "agree", "indep", 6, np.random.default_rng(3), (4, 3))
    r = np.random.default_rng(3)
    S0, S1 = nc.null_signs(r, 6, 4, 3), nc.null_signs(r, 6, 4, 3)
    ref = nc.transition_counts(nc.triangle_codes(nc.symmetrise(S0, "agree")), nc.triangle_codes(nc.symmetrise(S1, "agree")), 5)
    assert np.array_equal(out[0], ref)
    with pytest.raises(ValueError):
        nc.null_transitions(S, nc.TRIPLE_LEVEL, None, "bogus", 2, np.random.default_rng(0))
    # observed transitions: one table per consecutive pair of waves, each accounting for every triple once
    T = nc.observed_transitions(S, nc.TRIANGLE_LEVEL, "sum")
    assert T.shape == (14, 5, 5) and (T.sum((1, 2)) == 680).all()


def test_transition_counts_match_a_loop():
    rng = np.random.default_rng(5)
    start = rng.integers(0, 5, size=50)
    end = rng.integers(0, 5, size=(7, 50))
    got = nc.transition_counts(start, end, 5)
    assert got.shape == (7, 5, 5) and (got.sum((1, 2)) == 50).all()
    for b in range(7):
        ref = np.zeros((5, 5), dtype=int)
        for x, y in zip(start, end[b]):
            ref[x, y] += 1
        assert np.array_equal(got[b], ref)
    assert np.array_equal(nc.transition_counts(start, end[0], 5), got[0])


def test_compare_to_null_statistics():
    """p_gt is D&K's p(obs > random) [L4486]; p_up / p_dn are the tie-inclusive add-one exact Monte-Carlo p-values."""
    c = nc.compare_to_null(np.array([[3]]), np.array([[0], [1], [2], [3], [3], [4], [5]]))
    assert c["p_gt"][0, 0] == pytest.approx(3 / 7) and c["p_lt"][0, 0] == pytest.approx(2 / 7)
    assert c["p_up"][0, 0] == pytest.approx((1 + 4) / 8) and c["p_dn"][0, 0] == pytest.approx((1 + 5) / 8)
    assert c["mean"][0, 0] == pytest.approx(18 / 7)
    z = nc.compare_to_null(np.array([[2]]), np.zeros((10, 1), dtype=int))["z"]
    assert np.isnan(z).all()  # a null that never varies gives no z
    assert nc.dk_flag(0.99) == "more" and nc.dk_flag(0.01) == "fewer" and nc.dk_flag(0.5) == "n.s."
    # a zero observed against a null that is mostly zero is NOT 'under' (the tie-inclusive rule), unlike D&K's strict rule
    zero = nc.compare_to_null(np.array([0]), np.array([[0]] * 80 + [[1]] * 20))
    assert zero["p_gt"][0] == 0.0 and zero["p_dn"][0] > 0.5
    assert nc.side(np.array([0]), zero["mean"], zero["p_up"], zero["p_dn"]).tolist() == ["-"]


def test_dk_pattern_checks_each_claim():
    ok = np.zeros((15, 8))
    ok[:, 0] = 1.0  # LLL
    ok[:, 3] = 1.0  # LDD
    ok[:, 4] = np.r_[0.5, np.full(4, 0.5), np.full(10, 0.99)]  # DLL
    ok[:, 7] = np.r_[np.full(4, 0.8), np.full(11, 1.0)]  # DDD
    ok[:, 5] = np.r_[np.full(4, 0.3), np.full(11, 0.0)]  # DLD
    ok[:, 6] = np.r_[0.01, np.full(3, 0.2), np.full(11, 0.0)]  # DDL
    assert all(nc.dk_pattern(ok).values())
    bad = ok.copy()
    bad[10, 4] = 0.9  # DLL dips below significance at wave 11
    res = nc.dk_pattern(bad)
    assert not res["DLL above the null in every wave from 6 on [L4494]"] and res["LDD above the null from wave 2 [L4491]"]
    bad = ok.copy()
    bad[:, 2] = 0.5  # LDL no longer below the null
    assert not nc.dk_pattern(bad)["LDL below the null in all 15 waves [L4492]"]


def test_conversion_arithmetic_on_a_hand_example():
    """conversion_stats on a toy 'cond'-style null whose answer is known by hand (K = 5 triangle level)."""
    lv = nc.TRIANGLE_LEVEL
    B = 100
    Tobs = np.zeros((14, 5, 5), dtype=int)
    Tobs[0, 1] = [1, 2, 1, 0, 4]  # 8 one-negative: 1->+++, 2 stay, 1->+--, 4 lose a tie  => strict 2, relief 6
    Tobs[0, 3] = [0, 0, 0, 6, 2]  # 8 all-negative: 6 stay, 2 lose a tie
    Tnull = np.zeros((14, B, 5, 5), dtype=np.int32)
    Tnull[0, :, 1] = [1, 3, 0, 0, 4]  # strict 1, relief 5
    Tnull[0, :, 3] = [0, 0, 0, 6, 2]
    r = nc.conversion_stats(Tobs, Tnull, lv, nc.window_transitions("all"))
    one, allneg = r["classes"]["one_neg"], r["classes"]["all_neg"]
    assert one["start_obs"] == 8 and one["strict"]["num_obs"] == 2 and one["strict"]["rate_obs"] == pytest.approx(0.25)
    assert one["strict"]["rate_null_mean"] == pytest.approx(1 / 8) and one["strict"]["p_up"] == pytest.approx(1 / (B + 1))
    assert one["relief"]["rate_obs"] == pytest.approx(6 / 8) and one["relief"]["rate_null_mean"] == pytest.approx(5 / 8)
    assert one["inc"]["rate_obs"] == pytest.approx(0.5)
    assert allneg["weak"]["rate_obs"] == pytest.approx(6 / 8) and allneg["weak"]["p_up"] == pytest.approx(1.0)
    assert r["diff"]["strict"]["obs"] == pytest.approx(0.25) and r["diff"]["strict"]["null_mean"] == pytest.approx(0.125)
    assert r["diff"]["strict"]["p_up"] == pytest.approx(1 / (B + 1))
    # a class with nobody at risk gives nan, not a spurious p-value
    r0 = nc.conversion_stats(Tobs[:, :, :] * 0, Tnull * 0, lv, [0])
    assert np.isnan(r0["classes"]["one_neg"]["strict"]["rate_obs"]) and np.isnan(r0["diff"]["strict"]["p_up"])


def test_windows():
    assert nc.window_transitions("all") == list(range(14))
    assert nc.window_transitions("early") == [0, 1, 2, 3, 4] and nc.window_transitions("late") == list(range(5, 14))
    assert 8 not in nc.window_transitions("nogap") and len(nc.window_transitions("nogap")) == 13  # transition 9 -> 10 [L4472]


def test_fetch_refuses_a_file_whose_checksum_differs(tmp_path):
    """fetch() verifies the recorded sha256 before writing anything (local-use data, sim/data/README.md)."""
    junk = tmp_path / "junk.dat"
    junk.write_bytes(b"not the Newcomb file")
    dest = tmp_path / "out" / "newfrat.dat"
    with pytest.raises(RuntimeError):
        nc.fetch(dest=dest, urls=(junk.as_uri(),))
    assert not dest.exists()


# ------------------------------------------------------------------ (2) data

@pytest.fixture(scope="module")
def ranks():
    return nc.load_ranks()


@pytest.fixture(scope="module")
def signs(ranks):
    return nc.recode(ranks)


@pytest.fixture(scope="module")
def static(signs):
    """Observed counts and the 10,000-draw D&K null at the primary recode, plus their comparison."""
    obs = nc.observed_counts(signs)
    null = nc.static_null(np.random.default_rng(20261031), 10_000)
    return obs, null, {k: nc.compare_to_null(obs[k], null[k]) for k in ("triple", "agree", "sum")}


@needs_data
def test_data_integrity(ranks):
    """15 waves of 17 x 17 ranks, labels NEWC0-NEWC15 without NEWC9, rows are permutations of 1..16, checksum as recorded
    [L4471, L4538, L4543, L4545]; the UCI mirror's 14 networks is not what is used."""
    assert ranks.shape == (15, 17, 17)
    assert nc.sha256_of(nc.DATA_FILE) == nc.SHA256
    assert nc.WAVE_LABELS == tuple(f"NEWC{k}" for k in [*range(9), *range(10, 16)])
    assert (np.sort(ranks[:, nc.ROWS, OFF], axis=-1) == np.arange(1, 17)).all()
    assert nc.N_TRANSITIONS == 14 and nc.GAP_TRANSITION == 9


@needs_data
def test_fixed_counts_per_wave(signs):
    """Every man sends 4 +, 3 - and 9 null ties in every wave, so 68 + and 51 - per wave [L4476, L4480]."""
    rows = signs[:, nc.ROWS, OFF]
    assert ((rows == 1).sum(-1) == 4).all() and ((rows == -1).sum(-1) == 3).all() and ((rows == 0).sum(-1) == 9).all()
    assert ((signs == 1).sum((1, 2)) == 68).all() and ((signs == -1).sum((1, 2)) == 51).all()


@needs_data
def test_recode_reproduces_the_1996_papers_reciprocity_and_turnover(signs):
    """The 1996 paper measured, on these ranks with this recode, 30-35 reciprocated ties of 68 per wave (text) with 36 in
    weeks 3-5 and 10 (plot) [L4520] and 'slightly above 30%' of dyadic ties changing at the first transition [L4527].
    Agreement is evidence that the file, the wave order and the recode are the authors'."""
    rec = nc.reciprocated_positive(signs)
    assert rec.min() == 30 and rec.max() == 36
    assert [w + 1 for w in np.flatnonzero(rec == 36)] == [3, 4, 5, 10]
    off = ~np.eye(17, dtype=bool)
    first = (signs[0] != signs[1])[off].mean()
    assert 0.30 < first < 0.33
    assert all((signs[t] != signs[t + 1])[off].mean() < first for t in range(1, 14))  # turnover falls after the first transition


@needs_data
def test_dk_figure1_pattern_is_reproduced(static):
    """D&K 2001 Figure 1 as stated in words [L4490-L4498], per wave, against the 10,000-draw row shuffle [L4485, L4486].
    The brief's two: LLD and LDL under-represented from the start (every wave), DLL over-represented from week 6."""
    _, _, cmp_ = static
    p = cmp_["triple"]["p_gt"]
    i = nc.TRIPLE_TYPES.index
    assert (p[:, i("LLD")] < 0.05).all() and (p[:, i("LDL")] < 0.05).all()
    assert (p[5:, i("DLL")] > 0.95).all() and (p[:5, i("DLL")] < 0.95).all()  # significant from week 6, not before
    results = nc.dk_pattern(p)
    assert all(results.values()), [k for k, v in results.items() if not v]


@needs_data
def test_dk_exact_values_where_the_text_gives_them(static):
    """LLL 'never departs' from 1.0 [L4490]; DDD 'reaches 1.0 at week 5' [L4495]; LDD '1.0 from week 2' [L4491]."""
    p = static[2]["triple"]["p_gt"]
    i = nc.TRIPLE_TYPES.index
    assert p[:, i("LLL")].min() > 0.999 and p[4:, i("DDD")].min() > 0.999 and p[1:, i("LDD")].min() > 0.999
    assert p[0, i("DDL")] < 0.05 and p[1, i("DDL")] > p[0, i("DDL")]  # 'already significant at the start', then 'departs from 0 in week 2'


@needs_data
def test_pooled_one_negative_directed_forms_are_under_represented_every_wave(static):
    """v0 section 7 half (a), directed: the pool LLD+LDL+DLL is below the sign-shuffled null in all 15 waves although DLL alone is above it."""
    obs, null, _ = static
    one = nc.TRIPLE_LEVEL.one_neg
    c = nc.compare_to_null(nc.pool(obs["triple"], one)[:, None], nc.pool(null["triple"], one)[:, None])
    assert (c["p_dn"][:, 0] <= 0.05).all() and (c["z"][:, 0] < -2).all()
    share = nc.pool(obs["triple"], one) / obs["triple"].sum(-1)
    assert share.max() < 0.40 and share.min() > 0.15  # depleted, not forbidden


@needs_data
def test_dll_is_the_exception_to_the_symmetric_triangle_rule(static):
    """A rule symmetric in the three ties (v0 (4.2b)/(5.1)) cannot distinguish DLL from LLD and LDL; the data do (104 section 9):
    the first tie negative => over-represented from wave 6 [L4494, L4508, L4511]."""
    c = static[2]["triple"]
    i = nc.TRIPLE_TYPES.index
    assert (c["z"][5:, i("DLL")] > 2).all() and (c["z"][:, i("LLD")] < -2).all() and (c["z"][:, i("LDL")] < -2).all()


@needs_data
def test_strict_balance_fails_and_weak_survives_statically(static):
    """The all-negative triple DDD, forbidden by strict (Heider) balance, is enriched from wave 5 on [L4495]; the one-negative is depleted
    (weak balance, L4483).  The all-negative triangle is also enriched under 'sum' in most waves."""
    _, _, cmp_ = static
    i = nc.TRIPLE_TYPES.index
    assert (cmp_["triple"]["z"][4:, i("DDD")] > 4).all()
    over = (cmp_["sum"]["p_up"][:, 3] <= 0.05) & (static[0]["sum"][:, 3] > cmp_["sum"]["mean"][:, 3])
    assert over.sum() >= 10


@needs_data
def test_agree_rule_cannot_test_the_one_negative_triangle(static):
    """Under 'agree' (only mutual same-sign ties) there is ONE one-negative triangle in 15 waves; the null expects 0.25 a wave and is
    zero 78% of the time, so 'under-represented' is untestable at this size.  Fixed by the brief, reported as the headline cell."""
    obs, null, cmp_ = static
    assert obs["agree"][:, 1].sum() == 1
    assert 0.2 < cmp_["agree"]["mean"][0, 1] < 0.3 and 0.7 < (null["agree"][:, 1] == 0).mean() < 0.85
    assert (cmp_["agree"]["p_dn"][:, 1] > 0.5).all()  # never 'under'


@needs_data
def test_sum_rule_one_negative_triangle_is_under_represented_in_about_half_the_waves(static):
    obs, _, cmp_ = static
    c = cmp_["sum"]
    flags = nc.side(obs["sum"][:, 1], c["mean"][:, 1], c["p_up"][:, 1], c["p_dn"][:, 1])
    assert (flags == "under").sum() >= 6 and (flags == "over").sum() == 0
    assert (obs["sum"][:, 1] < c["mean"][:, 1]).all()  # below the null mean in every wave, significantly in about half


@needs_data
@pytest.mark.parametrize("level,rule", [(nc.TRIPLE_LEVEL, None), (nc.TRIANGLE_LEVEL, "sum"), (nc.TRIANGLE_LEVEL, "agree")])
def test_transition_tables_are_consistent_with_the_static_counts(signs, level, rule):
    """Each transition table accounts for every triple once; its row sums are the type counts at wave w and its column sums those at w + 1."""
    T = nc.observed_transitions(signs, level, rule)
    codes = nc.level_codes(signs, level, rule)
    assert T.shape == (14, level.k, level.k)
    for t in range(14):
        assert T[t].sum() == codes.shape[1]
        assert np.array_equal(T[t].sum(1), np.bincount(codes[t], minlength=level.k))
        assert np.array_equal(T[t].sum(0), np.bincount(codes[t + 1], minlength=level.k))
    counts = nc.triple_counts(signs) if level is nc.TRIPLE_LEVEL else nc.triangle_counts(nc.symmetrise(signs, rule))
    assert np.array_equal(T.sum(1)[:, : level.inc], counts[1:])  # complete types at waves 2..15
    assert np.array_equal(T.sum(2)[:, : level.inc], counts[:-1])  # complete types at waves 1..14


@needs_data
def test_observed_pooled_transition_counts(signs):
    """Deterministic facts about the data and the recode (no null involved), all 14 transitions pooled: who is at risk and where they go.
    The headline numbers of sim/results/newcomb_n3.md."""
    def pooled(level, rule):
        return nc.observed_transitions(signs, level, rule).sum(0)

    def cls(O, level, name):
        rows = list(getattr(level, name))
        return int(O[rows].sum()), int(O[np.ix_(rows, level.strict_bal)].sum()), int(O[rows, level.inc].sum()), int(O[np.ix_(rows, level.weak_bal)].sum())

    O = pooled(nc.TRIPLE_LEVEL, None)
    assert cls(O, nc.TRIPLE_LEVEL, "one_neg") == (1375, 15, 728, 15)
    assert cls(O, nc.TRIPLE_LEVEL, "all_neg") == (652, 2, 253, 399)
    O = pooled(nc.TRIANGLE_LEVEL, "sum")
    assert cls(O, nc.TRIANGLE_LEVEL, "one_neg") == (601, 33, 311, 33)
    assert cls(O, nc.TRIANGLE_LEVEL, "all_neg") == (251, 7, 90, 161)
    O = pooled(nc.TRIANGLE_LEVEL, "agree")
    assert cls(O, nc.TRIANGLE_LEVEL, "one_neg")[:2] == (1, 0) and cls(O, nc.TRIANGLE_LEVEL, "all_neg")[:2] == (7, 0)


@pytest.fixture(scope="module")
def conversion(signs):
    """Seeded conditional-null conversion statistics, 3,000 draws (the report uses 10,000), all transitions pooled."""
    rng = np.random.default_rng(7)
    out = {}
    for cell, (level, rule) in {"triple": (nc.TRIPLE_LEVEL, None), "sum": (nc.TRIANGLE_LEVEL, "sum")}.items():
        Tobs = nc.observed_transitions(signs, level, rule)
        Tc = nc.null_transitions(signs, level, rule, "cond", 3000, rng)
        Ti = nc.null_transitions(signs, level, rule, "indep", 1000, rng)
        w = nc.window_transitions("all")
        out[cell] = (nc.conversion_stats(Tobs, Tc, level, w), nc.conversion_stats(Tobs, Ti, level, w))
    return out


@needs_data
@pytest.mark.parametrize("cell", ["triple", "sum"])
def test_v07_conversion_one_negative_is_not_shown_faster_than_all_negative(conversion, cell):
    """v0 section 7 half (b), literal reading: the one-negative class converts into a complete balanced type no more than modestly above
    its null rate, and its excess over the all-negative class is within what the conditional null already produces (the null favours
    the one-negative class).  Qualitative: ratio above 1 but small, difference not significant at 5%."""
    stats = conversion[cell][0]
    one, allneg = stats["classes"]["one_neg"], stats["classes"]["all_neg"]
    assert 1.0 < one["strict"]["rate_obs"] / one["strict"]["rate_null_mean"] < 2.0
    assert stats["diff"]["strict"]["p_up"] > 0.03
    assert allneg["strict"]["rate_obs"] < 0.05  # all-negative triples essentially never convert (2 of 652; 7 of 251)


@needs_data
@pytest.mark.parametrize("cell", ["triple", "sum"])
def test_all_negative_triples_persist_more_than_chance(conversion, cell):
    """Weak balance (nothing to repair) vs strict (repair): the all-negative class stays a complete weakly-balanced triple far more often than
    random tie change would, and resists 'relief' [L4483, L4495]."""
    c = conversion[cell][0]["classes"]["all_neg"]
    assert c["weak"]["rate_obs"] - c["weak"]["rate_null_mean"] > 0.08 and c["weak"]["p_up"] < 0.01
    assert c["relief"]["rate_obs"] < c["relief"]["rate_null_mean"] and c["relief"]["p_dn"] < 0.01


@needs_data
@pytest.mark.parametrize("cell", ["triple", "sum"])
def test_relief_asymmetry_between_one_negative_and_all_negative(conversion, cell):
    """Post-hoc reading (v0 section 4.2: a lost tie is vacuously balanced): one-negative relieves faster than all-negative, more than the null difference."""
    stats = conversion[cell][0]
    assert stats["diff"]["relief"]["obs"] > 0.10 and stats["diff"]["relief"]["p_up"] < 0.01
    # ...but in the directed data the one-negative class by itself is not above its own null
    if cell == "triple":
        assert stats["classes"]["one_neg"]["relief"]["p_up"] > 0.02


@needs_data
@pytest.mark.parametrize("cell", ["triple", "sum"])
def test_independent_shuffles_are_not_the_test(conversion, cell):
    """The literal 'shuffled waves' null re-draws both waves, so persistence is destroyed: observed conversion and tie-loss rates sit far below it
    for BOTH classes, which is why it cannot isolate balance pressure."""
    ind = conversion[cell][1]["classes"]
    for cname in ("one_neg", "all_neg"):
        assert ind[cname]["strict"]["rate_obs"] < ind[cname]["strict"]["rate_null_mean"]
        assert ind[cname]["strict"]["p_dn"] < 0.01
        assert ind[cname]["inc"]["rate_obs"] < 0.7 * ind[cname]["inc"]["rate_null_mean"]


@needs_data
def test_tension_leaves_through_lost_ties_not_sign_flips(signs):
    """Where tension goes (post hoc): among one-negative triples at risk, a lost tie is far commoner than a conversion, and the
    first-tie-positive forms lose ties more than the conditional null, DLL less (the first-tie rule in the dynamics, L4508)."""
    rng = np.random.default_rng(11)
    Tobs = nc.observed_transitions(signs, nc.TRIPLE_LEVEL)
    Tc = nc.null_transitions(signs, nc.TRIPLE_LEVEL, None, "cond", 3000, rng).sum(0).astype(float)
    O = Tobs.sum(0)
    inc = nc.TRIPLE_LEVEL.inc
    z = (O[:, inc] - Tc.mean(0)[:, inc]) / Tc.std(0, ddof=1)[:, inc]
    t = nc.TRIPLE_TYPES.index
    assert z[t("LLD")] > 2 and z[t("LDL")] > 2 and z[t("DLL")] < -2
    one = list(nc.TRIPLE_LEVEL.one_neg)
    assert O[one, inc].sum() > 20 * O[np.ix_(one, nc.TRIPLE_LEVEL.strict_bal)].sum()


@needs_data
def test_recode_sensitivity_static_contrasts(ranks):
    """[L4478]: D&K say the qualitative results also hold for top-3/bottom-3 and top-3/bottom-2 (unverified in 104).  Operationalised as the
    sign of each contrast in most waves, for all four cuts: LLD under, LDL under, DLL over (waves 6-15), DDD over (waves 5-15), pooled
    one-negative under.  And D&K's ten wave-by-wave claims hold exactly at 4/3 but NOT at the other cuts (a finding: the details are not stable)."""
    i = nc.TRIPLE_TYPES.index
    held = {}
    for k, (name, (npos, nneg)) in enumerate(nc.RECODES.items()):
        S = nc.recode(ranks, npos, nneg)
        obs = nc.observed_counts(S)
        null = nc.static_null(np.random.default_rng([20261031, k]), 10_000, npos, nneg)
        c = nc.compare_to_null(obs["triple"], null["triple"])
        assert (c["p_gt"][:, i("LLD")] < 0.05).sum() >= 13 and (c["p_gt"][:, i("LDL")] < 0.05).sum() >= 13
        assert (c["p_gt"][5:, i("DLL")] > 0.95).sum() >= 8 and (c["p_gt"][4:, i("DDD")] > 0.95).sum() >= 9
        pool = nc.compare_to_null(nc.pool(obs["triple"], nc.TRIPLE_LEVEL.one_neg)[:, None], nc.pool(null["triple"], nc.TRIPLE_LEVEL.one_neg)[:, None])
        assert (pool["p_dn"][:, 0] <= 0.05).sum() >= 10
        held[name] = sum(nc.dk_pattern(c["p_gt"]).values())
    assert held[nc.PRIMARY_RECODE] == 10
    assert all(v < 10 for r, v in held.items() if r != nc.PRIMARY_RECODE)


@needs_data
def test_report_builds_end_to_end():
    """The report generator runs and its verdict guards hold at a small draw count (so the prose and the numbers cannot drift apart silently)."""
    from models import newcomb_report as rep

    out = rep.run(n_draws=1500)
    text = rep.build_report(out)
    assert text.startswith("# Newcomb fraternity") and "## Verdict" in text and "## Reproduce" in text
    assert "(pending)" not in text and not re.search(r"\bnan\b", text, flags=re.I)
