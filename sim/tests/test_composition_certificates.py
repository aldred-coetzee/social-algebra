"""Composition laws for the small-gain no-escalation certificate: models/01 §2.1 (a fragment of a
certified group is certified), §3.1 (merge, row-sum form), §3.2 (merge, loop-gain form, an iff),
§3.3 (uniform cliques, an exact iff) and §3.4 (one member joins, an exact iff), from
models/01-composition-and-levers.md as revised 2026-10-31 after next-pattern's audit.

These are the project's own derived results, not published ones, so there is no prior-work file or
ledger id for the claims; the objects they act on are v0.1's (models/00-v0.md §5; ledger L3996
small-gain, L4467 the (n-1)g clique row sums).  The standing facts F1-F3 of §1 are sanity-checked
first, because every proof leans on them.

Conventions.  Gamma[i, j] is the gain from j to i, so a row sum is a member's total incoming gain.
Every random test is seeded and states its draw count.  A failure here is a finding about a
theorem, so no tolerance is relaxed to make a test pass: tolerances are set by floating-point noise
(observed at most 3e-12 in the sweeps run while writing these tests) and the iff tests put the
offending matrices in the assertion message.  BAND: a draw whose spectral radius lies within 1e-9
of 1 on either side of an iff is excluded and counted (there the two sides can only be told apart
by noise); the tests require the exclusions to stay under 1% of draws.

Findings recorded by these tests (the asserts below reproduce every number except the 100,000
extra draws, a one-off sweep not re-run here):
  * Theorem 3.2's iff held in every draw (2,000 here; 100,000 more across five other seeds when
    the tests were written), with half the draws on each side of the threshold and some within 1e-6
    (relative, in the cross-gain scale) of it.
  * §3.3 is an exact iff and the 2x2 quotient reproduces rho(Gamma_m) to 2e-15 relative, on every
    one of 1,764 grid pairs; the row-sum bound of §3.1 is sufficient there and conservative by
    the factor sqrt(b_1 b_2)/min(b_1, b_2) (see test_corollary_33_conservativeness_ratio).
"""
import itertools

import numpy as np
import pytest
from models import certificates as cert

BAND = 1e-9      # |rho - 1| below this: too close to call by floating point, draw excluded and counted
RTOL = 1e-12     # slack for comparisons that are equalities or inequalities in exact arithmetic

N_SPLIT = 500    # Theorem 2.1 draws
N_ROWSUM = 500   # Theorem 3.1 draws
N_IFF = 2000     # Theorem 3.2 iff draws
N_ONEWAY = 1000  # Theorem 3.2 one-way draws (each tested in both directions)
N_PROOF = 400    # Theorem 3.2 proof-step draws
N_JOIN = 2000    # Corollary 3.4 iff draws
N_JOIN_ROWSUM = 500


# --------------------------------------------------------------------------- helpers

def _fmt(M) -> str:
    return np.array2string(np.asarray(M), precision=17, separator=", ", max_line_width=200)


def _report(draw: int, seed: int, **named) -> str:
    """Assertion text holding everything needed to rebuild an offending instance exactly."""
    out = [f"draw {draw} of seed {seed}"]
    for k, v in named.items():
        out.append(f"{k} =\n{_fmt(v)}" if isinstance(v, np.ndarray) else f"{k} = {v!r}")
    return "\n".join(out)


def _scaled_instance(rng):
    """(G1, C12, C21, G2) with both groups certified and the cross blocks scaled together by t, so
    the loop gain rho(P) = m^2 for a multiplier m (P is bilinear in C12, C21).  30% of draws put m
    within 1e-2..1e-6 (relative) of the threshold m = 1, on either side; the rest are log-uniform
    in [0.2, 5], so both outcomes occur with a spread of margins.  A draw with no loop (P
    nilpotent, rho(P) = 0) has nothing to scale towards: it gets a scale in [0.5, 20] and must
    be certified whatever the scale."""
    G1, C12, C21, G2 = cert.random_two_groups(rng)
    unit = cert.loop_gain(G1, C12, G2, C21)
    if unit > 1e-9:
        if rng.random() < 0.3:
            m = 1 + rng.choice([-1.0, 1.0]) * 10 ** -rng.uniform(2, 6)
        else:
            m = float(np.exp(rng.uniform(np.log(0.2), np.log(5.0))))
        t = m / np.sqrt(unit)
    else:
        t = rng.uniform(0.5, 20.0)
    return G1, t * C12, t * C21, G2


def _clique_grid():
    """(n, g) pairs with rho = (n-1) g <= 0.95; n = 1 has no internal tie, so one g stands for all."""
    grid_n = (1, 2, 3, 4, 6, 9, 14, 21, 32)
    grid_g = (0.005, 0.01, 0.02, 0.05, 0.1, 0.2, 0.4, 0.8)
    return [(n, g) for n in grid_n for g in (grid_g if n > 1 else (0.1,)) if (n - 1) * g <= 0.95]


def _merge_grid():
    cl = _clique_grid()
    return [(n1, g1, n2, g2) for (n1, g1), (n2, g2) in itertools.product(cl, cl)]


# --------------------------------------------------------------------------- standing facts (models/01 §1)

def test_standing_facts_F1_F2_F3():
    """Sanity of the helpers and of the facts every proof leans on (models/01 §1), 300 draws each.
    (F1) 0 <= B <= A entrywise => rho(B) <= rho(A).  (F2) rho(A) <= max_i sum_j |a_ij|, any real
    matrix.  (F3) A >= 0 with rho(A) < 1 => (I - A)^-1 = sum_k A^k >= 0 (the sum is formed as
    prod_j (I + A^(2^j)) = sum_{k<1024} A^k, enough for rho <= 0.9)."""
    rng = np.random.default_rng(1101)
    for _ in range(300):
        n = int(rng.integers(2, 12))
        A = cert.random_gain_matrix(n, rng, density=rng.uniform(0.2, 1.0))
        B = A * rng.random((n, n))                                # 0 <= B <= A entrywise
        assert cert.spectral_radius(B) <= cert.spectral_radius(A) + RTOL                  # F1
        R = rng.normal(size=(n, n))                                                       # F2, signed
        assert cert.spectral_radius(R) <= np.abs(R).sum(axis=1).max() + RTOL
        assert cert.spectral_radius(A) <= cert.max_row_sum(A) + RTOL
        C = cert.random_certified(n, rng, density=rng.uniform(0.2, 1.0), rho_hi=0.9)      # F3
        inv = np.linalg.inv(np.eye(n) - C)
        assert inv.min() >= -RTOL
        neumann = np.eye(n)
        for j in range(10):
            neumann = neumann @ (np.eye(n) + np.linalg.matrix_power(C, 2 ** j))
        assert np.allclose(inv, neumann, rtol=1e-10, atol=1e-12)


# --------------------------------------------------------------------------- Theorem 2.1 (split)

def test_theorem_21_fragments_of_a_certified_group_are_certified():
    """Claim (models/01 §2.1, [derived]): if rho(Gamma) < 1 and the group splits into blocks that keep
    only their internal gains, every block has rho(Gamma_B) <= rho(Gamma) < 1.  500 random
    non-negative Gamma (3-20 members, zero diagonal, random density 0.15-1 so many are reducible,
    scaled to rho in (0.05, 0.99)), each cut into a random 2-4 block partition (blocks are
    arbitrary index sets, not contiguous).  Also checks the proof's own step: the zero-padded
    Gamma'_B satisfies 0 <= Gamma'_B <= Gamma entrywise and has the same radius."""
    seed = 2101
    rng = np.random.default_rng(seed)
    positive_blocks = 0
    for draw in range(N_SPLIT):
        n = int(rng.integers(3, 21))
        G = cert.random_certified(n, rng, density=rng.uniform(0.15, 1.0), allow_nilpotent=False)
        rho = cert.spectral_radius(G)
        assert 0 < rho < 1
        k = int(rng.integers(2, min(4, n) + 1))
        blocks = cert.random_partition(n, k, rng)
        assert sorted(np.concatenate(blocks)) == list(range(n)) and all(len(b) for b in blocks)
        for B in blocks:
            GB = cert.restrict(G, B)
            padded = cert.pad(G, B)
            assert np.all(padded >= 0) and np.all(padded <= G)                       # 0 <= G'_B <= G
            rho_B = cert.spectral_radius(GB)
            assert rho_B == pytest.approx(cert.spectral_radius(padded), abs=RTOL)    # padding keeps rho
            msg = _report(draw, seed, G=G, block=B, rho=rho, rho_B=rho_B)
            assert rho_B <= rho + RTOL, msg
            assert rho_B < 1, msg
            positive_blocks += rho_B > 0
    assert positive_blocks > N_SPLIT  # the sample is not degenerate: plenty of blocks with real loops


def test_theorem_21_bound_is_attained_for_block_diagonal_gain():
    """Claim (models/01 §2.1, tightness): rho(Gamma_B) <= rho(Gamma) cannot be improved to a
    margin.  For a block-diagonal Gamma (no cross ties) the dominant block has exactly the radius of
    the whole, and the splitting along the blocks loses nothing.  Constructed, 100 draws."""
    rng = np.random.default_rng(2102)
    for _ in range(100):
        nA, nB = (int(x) for x in rng.integers(2, 9, 2))
        A = cert.random_certified(nA, rng, allow_nilpotent=False)
        B = cert.random_certified(nB, rng, allow_nilpotent=False)
        G = np.block([[A, np.zeros((nA, nB))], [np.zeros((nB, nA)), B]])
        blocks = [np.arange(nA), np.arange(nA, nA + nB)]
        radii = [cert.spectral_radius(cert.restrict(G, b)) for b in blocks]
        assert max(radii) == pytest.approx(cert.spectral_radius(G), abs=RTOL)
        assert max(radii) < 1


# --------------------------------------------------------------------------- Theorem 3.1 (merge, row sums)

def test_theorem_31_row_sums_below_one_imply_certified():
    """Claim (models/01 §3.1, [derived]): if every member's total incoming gain in the merged group,
    old plus cross, is below one, then rho(Gamma_m) < 1 (rho <= ||.||_inf, F2).  500 random block
    matrices Gamma_m = [Gamma_1 C_12; C_21 Gamma_2] (1-10 members per group, random density, rows
    rescaled to random sums in (0.05, 1 - 1e-6), and in 30% of draws to sums in (0.95, 1 - 1e-6)
    so the bound is probed close to its edge).  The hypotheses of §3 hold and are checked: both
    groups are certified, because their rows sum to less than one."""
    seed = 3101
    rng = np.random.default_rng(seed)
    for draw in range(N_ROWSUM):
        n1, n2 = (int(x) for x in rng.integers(1, 11, 2))
        M = cert.merged(
            cert.random_gain_matrix(n1, rng, density=rng.uniform(0.3, 1.0)),
            cert.random_cross(n1, n2, rng, density=rng.uniform(0.3, 1.0)),
            cert.random_cross(n2, n1, rng, density=rng.uniform(0.3, 1.0)),
            cert.random_gain_matrix(n2, rng, density=rng.uniform(0.3, 1.0)))
        lo = 0.95 if rng.random() < 0.3 else 0.05
        M = cert.scale_rows_to_sums(M, rng.uniform(lo, 1 - 1e-6, n1 + n2))
        G1, G2 = M[:n1, :n1], M[n1:, n1:]
        msg = _report(draw, seed, Gamma_m=M)
        assert cert.max_row_sum(M) < 1, msg                       # the hypothesis of 3.1
        assert cert.spectral_radius(G1) < 1 and cert.spectral_radius(G2) < 1, msg
        rho = cert.spectral_radius(M)
        assert rho <= cert.max_row_sum(M) + RTOL, msg             # the proof's inequality (F2)
        assert rho < 1, msg
        # 3.2 agrees (the loop gain is below one as well)
        assert cert.loop_gain(G1, M[:n1, n1:], G2, M[n1:, :n1]) < 1, msg


def test_theorem_31_constant_row_sums_make_the_bound_tight():
    """Claim (models/01 §3.1, tightness): rho(Gamma_m) <= max row sum is attained.  When every row
    sums to the same s < 1 the all-ones vector is a positive eigenvector, so rho = s exactly: the
    certificate can sit arbitrarily close to its limit while the row-sum hypothesis still holds.
    Constructed for s in {0.5, 0.9, 0.999999}, 50 random merged matrices each."""
    rng = np.random.default_rng(3102)
    done = 0
    for s in (0.5, 0.9, 0.999999):
        for _ in range(50):
            n1, n2 = (int(x) for x in rng.integers(1, 9, 2))
            M = cert.merged(cert.random_gain_matrix(n1, rng, density=0.7),
                            cert.random_cross(n1, n2, rng), cert.random_cross(n2, n1, rng),
                            cert.random_gain_matrix(n2, rng, density=0.7))
            M = cert.scale_rows_to_sums(M, np.full(n1 + n2, s))
            if not np.all(M.sum(axis=1) > 0):
                continue                                     # a zero row cannot be rescaled to s
            assert cert.max_row_sum(M) == pytest.approx(s, abs=1e-14)
            assert cert.spectral_radius(M) == pytest.approx(s, abs=1e-12)
            done += 1
    assert done >= 100   # (all 150 are effective with this seed)


def test_theorem_31_merge_counterexample_two_pairs():
    """Claim (models/01 §3, §3.1 failure case): two certified groups can merge into an uncertified one.
    Two 2-member groups with weak internal gain a = 0.1 (rho = 0.1 each) and strong reciprocal cross
    gain c = 0.8 on every cross pair: every row of Gamma_m sums to a + 2c = 1.7, so rho(Gamma_m) =
    1.7 >= 1.  §3.2 predicts it: rho(P) = 4 c^2/(1-a)^2 = 3.16 >= 1, and both sides cross 1 at the same
    place, c = (1-a)/2 = 0.45 (checked a hair either side)."""
    a, c = 0.1, 0.8
    G1, C12, C21, G2 = cert.two_pair_counterexample(a, c)
    M = cert.merged(G1, C12, C21, G2)
    assert cert.spectral_radius(G1) == pytest.approx(a) and cert.spectral_radius(G2) == pytest.approx(a)
    assert cert.spectral_radius(G1) < 1 and cert.spectral_radius(G2) < 1           # both certified
    assert cert.spectral_radius(M) == pytest.approx(a + 2 * c)                      # = 1.7
    assert cert.spectral_radius(M) >= 1                                              # merged: NOT certified
    assert cert.loop_gain(G1, C12, G2, C21) == pytest.approx(4 * c ** 2 / (1 - a) ** 2)
    assert cert.loop_gain(G1, C12, G2, C21) >= 1
    assert M.sum(axis=1).min() >= 1                                                  # 3.1's premise fails everywhere
    for c_edge, certified in ((0.45 - 1e-3, True), (0.45 + 1e-3, False)):
        G1, C12, C21, G2 = cert.two_pair_counterexample(a, c_edge)
        assert (cert.spectral_radius(cert.merged(G1, C12, C21, G2)) < 1) is certified
        assert (cert.loop_gain(G1, C12, G2, C21) < 1) is certified


def test_theorem_31_smallest_counterexample_two_singletons():
    """Claim (models/01 §2.1 Reading, smallest merge counterexample): two singletons, Gamma_1 = Gamma_2 =
    [0] (certified, rho = 0), joined by c_12 = c_21 = 1 give Gamma_m = [0 1; 1 0] with rho = 1, which is
    not certified (the certificate needs rho < 1).  The loop gain is 1 as well, and every row sums to
    exactly 1, so 3.1's strict hypothesis fails at equality.  For singletons rho(Gamma_m) =
    sqrt(c_12 c_21) and rho(P) = c_12 c_21: only the product matters (c_12 = 4, c_21 = 1/4 also gives
    rho = 1), and the threshold is the product reaching 1."""
    zero = np.zeros((1, 1))
    M = cert.merged(zero, np.array([[1.0]]), np.array([[1.0]]), zero)
    assert np.array_equal(M, np.array([[0.0, 1.0], [1.0, 0.0]]))
    assert cert.spectral_radius(zero) == 0
    assert cert.spectral_radius(zero) < 1
    assert cert.spectral_radius(M) == pytest.approx(1.0, abs=1e-15)
    assert not cert.spectral_radius(M) < 1
    assert cert.loop_gain(zero, np.array([[1.0]]), zero, np.array([[1.0]])) == pytest.approx(1.0)
    assert np.all(M.sum(axis=1) == 1.0)
    for c12, c21 in ((4.0, 0.25), (0.5, 2.0), (1.0, 1.0)):
        M = cert.merged(zero, np.array([[c12]]), np.array([[c21]]), zero)
        assert cert.spectral_radius(M) == pytest.approx(np.sqrt(c12 * c21), abs=1e-14)
        assert cert.loop_gain(zero, np.array([[c12]]), zero, np.array([[c21]])) == pytest.approx(c12 * c21)
        assert not cert.spectral_radius(M) < 1
    for c in (0.9, 0.999):                                   # just below: certified
        assert cert.spectral_radius(cert.merged(zero, [[c]], [[c]], zero)) == pytest.approx(c)
        assert cert.spectral_radius(cert.merged(zero, [[c]], [[c]], zero)) < 1


def test_theorem_31_row_sum_condition_is_sufficient_not_necessary():
    """Claim (models/01 §3.2 Reading, "sharper"): 3.1's hypothesis is not needed.  Two singletons with
    c_12 = 4, c_21 = 0.2 have a row sum of 4 >= 1, yet rho(Gamma_m) = sqrt(0.8) = 0.894 < 1, and the
    loop gain 0.8 < 1 says so (a diagonal rescaling of the two members makes the ties equal)."""
    zero = np.zeros((1, 1))
    M = cert.merged(zero, [[4.0]], [[0.2]], zero)
    assert cert.max_row_sum(M) == pytest.approx(4.0)
    assert not cert.max_row_sum(M) < 1                                   # 3.1 does not apply
    assert cert.spectral_radius(M) == pytest.approx(np.sqrt(0.8), abs=1e-14)
    assert cert.spectral_radius(M) < 1                                   # but it is certified
    assert cert.loop_gain(zero, [[4.0]], zero, [[0.2]]) == pytest.approx(0.8)


# --------------------------------------------------------------------------- Theorem 3.2 (merge, loop gain)

def test_theorem_32_iff_on_random_blocks():
    """Claim (models/01 §3.2, [derived], the audited proof): with rho(Gamma_1), rho(Gamma_2) < 1,
    rho(Gamma_m) < 1 if and only if rho(P) < 1, P = (I-Gamma_1)^-1 C_12 (I-Gamma_2)^-1 C_21.
    2,000 random draws: groups of 1-8 members (random density, rho in (0.05, 0.99) or cycle-free),
    random non-negative sparse-or-dense cross blocks, scaled together across the threshold (half the
    draws on each side, 30% within 1e-2..1e-6 of it, some with no loop at all).  rho(Gamma_m) is
    computed from the full merged matrix, rho(P) from the block formula; the two sides are compared
    in EVERY draw outside the 1e-9 band.  If it ever fails the assertion prints the offending
    matrices: that would mean the proof is wrong, so nothing here is to be loosened.  (100,000 further
    draws over five other seeds, run once when this test was written, also had no failure.)"""
    seed = 3201
    rng = np.random.default_rng(seed)
    failures, excluded, n_cert, n_unc, n_noloop, n_near = [], 0, 0, 0, 0, 0
    for draw in range(N_IFF):
        G1, C12, C21, G2 = _scaled_instance(rng)
        assert cert.spectral_radius(G1) < 1 and cert.spectral_radius(G2) < 1      # hypotheses
        rho_m = cert.spectral_radius(cert.merged(G1, C12, C21, G2))
        rho_P = cert.loop_gain(G1, C12, G2, C21)
        if abs(rho_m - 1) < BAND or abs(rho_P - 1) < BAND:
            excluded += 1
            continue
        if (rho_m < 1) != (rho_P < 1):
            failures.append(_report(draw, seed, rho_Gamma_m=rho_m, rho_P=rho_P,
                                    Gamma_1=G1, C_12=C12, C_21=C21, Gamma_2=G2))
        n_cert += rho_m < 1
        n_unc += rho_m >= 1
        n_noloop += rho_P < 1e-9
        n_near += abs(rho_P - 1) < 1e-3
    print(f"\n3.2 iff: {N_IFF} draws, {len(failures)} disagreements, {excluded} excluded (band {BAND:g}); "
          f"certified {n_cert}, uncertified {n_unc}, no-loop {n_noloop}, within 1e-3 of threshold {n_near}")
    assert not failures, ("Theorem 3.2's iff FAILED; first counterexample:\n" + failures[0]
                          + f"\n({len(failures)} disagreements in all)")
    assert excluded <= N_IFF // 100
    assert 0.3 * N_IFF < n_cert < 0.7 * N_IFF   # the scaling really straddles the threshold
    assert n_near >= 200                        # and many draws sit very close to it
    assert n_noloop > 0                         # draws with no loop at all were included


def test_theorem_32_both_sides_cross_one_at_the_same_point():
    """Claim (models/01 §3.2, corollary of the iff and continuity): scale C_12 and C_21 together by t;
    rho(P) = t^2 rho(P_1), so the loop gain reaches 1 at t* = 1/sqrt(rho(P_1)).  The iff then forces
    rho(Gamma_m(t*)) = 1 exactly (it is >= 1 by the iff, <= 1 by continuity from below).  300 draws
    with a loop; checked to 1e-9 (observed 7e-15)."""
    rng = np.random.default_rng(3202)
    done = 0
    while done < 300:
        G1, C12, C21, G2 = cert.random_two_groups(rng)
        unit = cert.loop_gain(G1, C12, G2, C21)
        if unit <= 1e-9:
            continue
        t = 1 / np.sqrt(unit)
        assert cert.loop_gain(G1, t * C12, G2, t * C21) == pytest.approx(1.0, abs=1e-12)
        assert cert.spectral_radius(cert.merged(G1, t * C12, t * C21, G2)) == pytest.approx(1.0, abs=1e-9)
        done += 1


def test_theorem_32_one_way_cross_ties_are_always_certified():
    """Claim (models/01 §3.2 Reading): two certified groups with cross ties in one direction only
    (C_21 = 0 or C_12 = 0) are always certified, whatever the strength of the ties.  Gamma_m is block
    triangular, so rho(Gamma_m) = max(rho(Gamma_1), rho(Gamma_2)) < 1 and the loop matrix is the zero
    matrix.  1,000 draws, each in both directions, tie scale log-uniform in [0.01, 100] (far beyond
    anything certifiable by row sums); equality checked to 1e-9 (observed at most 3e-12)."""
    seed = 3203
    rng = np.random.default_rng(seed)
    for draw in range(N_ONEWAY):
        G1, C12, C21, G2 = cert.random_two_groups(rng)
        t = float(np.exp(rng.uniform(np.log(0.01), np.log(100.0))))
        expect = max(cert.spectral_radius(G1), cert.spectral_radius(G2))
        for label, A12, A21 in (("C_21 = 0", t * C12, 0 * C21), ("C_12 = 0", 0 * C12, t * C21)):
            rho_m = cert.spectral_radius(cert.merged(G1, A12, A21, G2))
            msg = _report(draw, seed, direction=label, scale=t, rho_Gamma_m=rho_m, expected=expect,
                          Gamma_1=G1, C_12=A12, C_21=A21, Gamma_2=G2)
            assert abs(rho_m - expect) < 1e-9, msg
            assert rho_m < 1, msg
            assert cert.loop_gain(G1, A12, G2, A21) == 0.0, msg


def test_theorem_32_proof_steps_hold_numerically():
    """Claim (models/01 §3.2, the audited proof, line by line): with A = I - Gamma_1, B = I - Gamma_2 and
    P' = B^-1 C_21 A^-1 C_12, rho(P') = rho(P).  (=>) if rho(Gamma_m) < 1: x = (I - Gamma_m)^-1 1 >= 1,
    x_1 >= A^-1 C_12 x_2, x_2 >= B^-1 1 + P' x_2, B^-1 1 >= 1, hence P' x_2 < x_2 componentwise and the
    Collatz-Wielandt bound gives rho(P') < 1.  (<=) if rho(P') < 1: S = B - C_21 A^-1 C_12 = B (I - P'),
    S^-1 = (I - P')^-1 B^-1 >= 0, the block-inverse formula reproduces (I - Gamma_m)^-1 with four
    non-negative blocks, y = (I - Gamma_m)^-1 1 > 0 has Gamma_m y < y, so rho(Gamma_m) < 1.  400
    draws (groups of 1-6, loop gain m^2 with m log-uniform in [0.3, 3]); draws within 1e-6 of the
    threshold are skipped here because the inverses blow up there (the iff test covers them)."""
    rng = np.random.default_rng(3204)
    n_fwd = n_bwd = 0
    for draw in range(N_PROOF):
        G1, C12, C21, G2 = cert.random_two_groups(rng, max_size=6)
        unit = cert.loop_gain(G1, C12, G2, C21)
        t = (float(np.exp(rng.uniform(np.log(0.3), np.log(3.0)))) / np.sqrt(unit)) if unit > 1e-9 \
            else rng.uniform(0.5, 20.0)
        C12, C21 = t * C12, t * C21
        n1, n2 = len(G1), len(G2)
        one1, one2 = np.ones(n1), np.ones(n2)
        A, B = np.eye(n1) - G1, np.eye(n2) - G2
        Ainv, Binv = np.linalg.inv(A), np.linalg.inv(B)
        Pp = Binv @ C21 @ Ainv @ C12
        M = cert.merged(G1, C12, C21, G2)
        rho_m, rho_Pp = cert.spectral_radius(M), cert.spectral_radius(Pp)
        assert rho_Pp == pytest.approx(cert.loop_gain(G1, C12, G2, C21), abs=1e-9 * max(1, rho_Pp))  # rho(XY) = rho(YX)
        assert np.all(Binv >= np.eye(n2) - 1e-12)                                                    # (I-G2)^-1 >= I
        if rho_m < 1 - 1e-6:                                                                         # (=>)
            n_fwd += 1
            x = np.linalg.solve(np.eye(n1 + n2) - M, np.ones(n1 + n2))
            x1, x2 = x[:n1], x[n1:]
            tol = 1e-9 * max(1.0, x.max())
            assert x.min() >= 1 - tol
            assert np.allclose(x1, Ainv @ (one1 + C12 @ x2), rtol=1e-8, atol=tol)                   # row block 1
            assert np.all(x1 >= Ainv @ C12 @ x2 - tol)
            assert np.allclose(x2, Binv @ (one2 + C21 @ x1), rtol=1e-8, atol=tol)                   # row block 2
            assert np.all(x2 >= Binv @ one2 + Pp @ x2 - tol)
            assert np.all(Binv @ one2 >= 1 - tol)
            assert np.all(Pp @ x2 < x2)                                                              # strict
            assert rho_Pp <= np.max((Pp @ x2) / x2) + 1e-9 and np.max((Pp @ x2) / x2) < 1            # Collatz-Wielandt
        if rho_Pp < 1 - 1e-6:                                                                        # (<=)
            n_bwd += 1
            S = cert.schur_complement(G1, C12, G2, C21)
            assert np.allclose(S, B @ (np.eye(n2) - Pp), rtol=1e-8, atol=1e-9)
            Sinv = np.linalg.inv(S)
            tol = 1e-9 * max(1.0, np.abs(Sinv).max())
            assert Sinv.min() >= -tol
            assert np.allclose(Sinv, np.linalg.inv(np.eye(n2) - Pp) @ Binv, rtol=1e-7, atol=tol)
            Minv = np.linalg.inv(np.eye(n1 + n2) - M)
            blocks = [Ainv + Ainv @ C12 @ Sinv @ C21 @ Ainv, Ainv @ C12 @ Sinv,
                      Sinv @ C21 @ Ainv, Sinv]
            got = [Minv[:n1, :n1], Minv[:n1, n1:], Minv[n1:, :n1], Minv[n1:, n1:]]
            for formula, direct in zip(blocks, got):
                assert np.allclose(formula, direct, rtol=1e-6, atol=1e-8 * max(1.0, np.abs(Minv).max()))
                assert formula.min() >= -1e-8 * max(1.0, np.abs(Minv).max())
            y = Minv @ np.ones(n1 + n2)
            assert np.all(y > 0) and np.all(M @ y < y)
            assert np.max((M @ y) / y) < 1 and rho_m <= np.max((M @ y) / y) + 1e-9
    assert n_fwd > 100 and n_bwd > 100   # both directions of the proof were exercised often


# --------------------------------------------------------------------------- Corollary 3.3 (uniform cliques)

def test_corollary_33_exact_iff_on_grid():
    """Claim (models/01 §3.3, [derived], exact): for uniform cliques (n_1, g_1), (n_2, g_2) with every
    cross tie of gain c, the merge is certified iff c^2 < (1 - rho_1)(1 - rho_2)/(n_1 n_2), rho_i =
    (n_i - 1) g_i.  Grid: 42 cliques (n in {1,2,3,4,6,9,14,21,32}, g in {0.005..0.8}, rho <= 0.95)
    squared = 1,764 merges, each tested at ten values of c from 0.1 to 5 times the claimed
    threshold, including 1 -/+ 1e-6 of it.  rho(Gamma_m) is computed directly from the full merged
    matrix, and rho_i from the clique matrices themselves (which must equal (n_i - 1) g_i, L4467)."""
    fractions = (0.1, 0.5, 0.9, 0.99, 1 - 1e-6, 1 + 1e-6, 1.01, 1.1, 2.0, 5.0)
    failures, excluded, tested = [], 0, 0
    for n1, g1, n2, g2 in _merge_grid():
        rho1 = cert.spectral_radius(cert.clique(n1, g1))
        rho2 = cert.spectral_radius(cert.clique(n2, g2))
        assert rho1 == pytest.approx(cert.clique_radius(n1, g1), abs=RTOL)
        assert rho2 == pytest.approx(cert.clique_radius(n2, g2), abs=RTOL)
        limit = (1 - rho1) * (1 - rho2) / (n1 * n2)
        for f in fractions:
            c = f * np.sqrt(limit)
            rho_m = cert.spectral_radius(cert.uniform_merge(n1, g1, n2, g2, c))
            if abs(rho_m - 1) < BAND:
                excluded += 1
                continue
            tested += 1
            if (rho_m < 1) != (c * c < limit):
                failures.append((n1, g1, n2, g2, c, rho_m, limit))
    print(f"\n3.3 iff on grid: {tested} (merge, c) cases, {len(failures)} disagreements, {excluded} excluded")
    assert not failures, f"Corollary 3.3's iff FAILED at (n1, g1, n2, g2, c, rho_m, limit) = {failures[0]}"
    assert excluded == 0 and tested == len(_merge_grid()) * len(fractions)


def test_corollary_33_quotient_spectral_radius():
    """Claim (models/01 §3.3, equitable partition): rho(Gamma_m) is the spectral radius of the 2x2
    quotient [[rho_1, n_2 c], [n_1 c, rho_2]].  Checked on all 1,764 grid merges at c = 0 and 0.1 to 5
    times the threshold (so rho(Gamma_m) from below 1 to well above it) to a relative 1e-12
    (observed 2e-15)."""
    worst = 0.0
    for n1, g1, n2, g2 in _merge_grid():
        c_star = cert.exact_threshold_closed_form(n1, g1, n2, g2)
        for f in (0.0, 0.1, 0.5, 1.0, 2.0, 5.0):
            c = f * c_star
            rho_m = cert.spectral_radius(cert.uniform_merge(n1, g1, n2, g2, c))
            rho_q = cert.spectral_radius(cert.quotient(n1, g1, n2, g2, c))
            worst = max(worst, abs(rho_m - rho_q) / max(1.0, rho_m))
    assert worst <= 1e-12, f"quotient and full matrix differ by a relative {worst:.3e}"


def test_corollary_33_row_sum_bound_is_sufficient():
    """Claim (models/01 §3.3 Remark, from §3.1): c < min(b_1, b_2), b_1 = (1 - rho_1)/n_2,
    b_2 = (1 - rho_2)/n_1, makes every row of Gamma_m sum to less than one, hence rho(Gamma_m) < 1.
    On all 1,764 grid merges at c = 0.25, 0.5, 0.9, 0.999999 times the bound the row sums (computed
    from the matrix) are below 1 and so is rho; at c = the bound the largest row sum is exactly 1, so
    the bound is where §3.1's hypothesis first fails."""
    for n1, g1, n2, g2 in _merge_grid():
        bound = cert.row_sum_bound(n1, g1, n2, g2)
        for f in (0.25, 0.5, 0.9, 0.999999):
            M = cert.uniform_merge(n1, g1, n2, g2, f * bound)
            assert cert.max_row_sum(M) < 1
            assert cert.spectral_radius(M) <= cert.max_row_sum(M) + RTOL
            assert cert.spectral_radius(M) < 1
        assert cert.max_row_sum(cert.uniform_merge(n1, g1, n2, g2, bound)) == pytest.approx(1.0, abs=1e-12)


def test_corollary_33_conservativeness_ratio():
    """Claim (models/01 §3.3 Remark): the row-sum bound c < min(b_1, b_2) is sufficient but the exact
    threshold is the geometric mean sqrt(b_1 b_2), so the exact threshold exceeds the bound by the
    factor sqrt(b_1 b_2)/min(b_1, b_2) = sqrt(max/min) >= 1, equal to 1 exactly when b_1 = b_2.
    The threshold is found NUMERICALLY (root-finding on rho of the full merged matrix, no formula)
    for all 1,764 grid merges and compared with the closed form; it is also symmetric under
    swapping the two cliques.  Also reproduces the worked example n = (10, 2), rho = (0.45, 0.10):
    bound c < 0.090, truth c < 0.157.

    MEASURED (grid above, 2026-11-01): ratio exact/bound
        min 1.000 (b_1 = b_2, so the bound IS the truth: 52 of 1,764 merges, 2.9% -- the 42
        identical-clique pairs and 10 coincidences; the next-most balanced pair is 0.16% off),
        quartiles 1.23 / 2.21, median 1.581, mean 1.875,
        max 8.222 at (n_1, g_1, n_2, g_2) = (2, 0.8, 32, 0.005): a 2-clique already at rho = 0.8
        merging with a loose 32-clique (rho = 0.155), where b_1 = 0.00625 but b_2 = 0.42;
        worked example 1.748.  Equivalently the row-sum certificate guarantees only 1/ratio of the
        true tolerance: a median 63%, as little as 12%.  The conservativeness is largest when the
        two groups differ in size or in slack, and zero when they match.
    (The asserts below pin these figures, so this paragraph cannot rot.)"""
    ratios, tight = [], 0
    worst = (0.0, None)
    for n1, g1, n2, g2 in _merge_grid():
        b1, b2 = cert.row_sum_limits(n1, g1, n2, g2)
        bound = min(b1, b2)
        exact = cert.exact_threshold(n1, g1, n2, g2)
        assert exact == pytest.approx(np.sqrt(b1 * b2), rel=1e-9)                         # the closed form
        assert cert.exact_threshold_closed_form(n1, g1, n2, g2) == pytest.approx(exact, rel=1e-9)
        assert exact == pytest.approx(cert.exact_threshold(n2, g2, n1, g1), rel=1e-9)     # symmetric in the two groups
        ratio = exact / bound
        assert ratio == pytest.approx(np.sqrt(b1 * b2) / min(b1, b2), rel=1e-9)
        assert ratio >= 1 - 1e-9                                                           # sufficiency
        balanced = abs(b1 - b2) <= 1e-12 * min(b1, b2)                                     # b_1 = b_2 ...
        if balanced:
            assert ratio == pytest.approx(1.0, abs=1e-9)                                   # ... the bound is the truth
        if abs(b1 - b2) > 1e-6 * min(b1, b2):                                              # clearly unbalanced ...
            assert ratio > 1 + 1e-7                                                        # ... strictly conservative
        tight += balanced
        ratios.append(ratio)
        if ratio > worst[0]:
            worst = (ratio, (n1, g1, n2, g2))
    r = np.array(ratios)
    summary = (f"3.3 conservativeness, {len(r)} grid merges: ratio exact/bound min {r.min():.3f}, "
               f"median {np.median(r):.3f}, mean {r.mean():.3f}, max {r.max():.3f} at (n1,g1,n2,g2) = {worst[1]}; "
               f"ratio == 1 for {tight / len(r):.1%}; quartiles {np.percentile(r, 25):.2f}/{np.percentile(r, 75):.2f}; "
               f"row-sum certificate guarantees {1 / np.median(r):.0%} of the true tolerance (median), "
               f"{1 / r.max():.0%} (worst)")
    print("\n" + summary)
    assert len(r) == 1764
    assert r.min() == pytest.approx(1.0, abs=1e-9)
    assert np.percentile(r, 25) == pytest.approx(1.23, abs=5e-3)
    assert np.median(r) == pytest.approx(1.581, abs=5e-4)
    assert np.percentile(r, 75) == pytest.approx(2.21, abs=5e-3)
    assert r.mean() == pytest.approx(1.875, abs=5e-4)
    assert r.max() == pytest.approx(8.222, abs=5e-4)
    assert tight == 52
    assert worst[1] == (2, 0.8, 32, 0.005)
    # the worked example of §3.3: n = (10, 2), rho = (0.45, 0.10), i.e. g_1 = 0.45/9 and g_2 = 0.10/1
    n1, g1, n2, g2 = 10, 0.45 / 9, 2, 0.10
    assert cert.clique_radius(n1, g1) == pytest.approx(0.45) and cert.clique_radius(n2, g2) == pytest.approx(0.10)
    assert cert.row_sum_bound(n1, g1, n2, g2) == pytest.approx(0.090, abs=5e-4)
    exact = cert.exact_threshold(n1, g1, n2, g2)
    assert exact == pytest.approx(0.157, abs=5e-4)
    assert exact / cert.row_sum_bound(n1, g1, n2, g2) == pytest.approx(1.748, abs=5e-4)


# --------------------------------------------------------------------------- Corollary 3.4 (one member joins)

def _join_instance(rng):
    """A certified group of 1-12 members plus a newcomer's incoming row c_in (what p receives) and
    outgoing column c_out (what the members receive from p), random support.  c_out is scaled so
    the scalar c_in (I-G)^-1 c_out (linear in c_out) is m: 30% of draws within 1e-2..1e-6 (relative)
    of the threshold m = 1, the rest log-uniform in [0.2, 5].  If the supports are such that there is
    no loop through p (scalar 0), c_out gets a scale in [0.5, 20] and the join must be certified."""
    n = int(rng.integers(1, 13))
    G = cert.random_certified(n, rng, density=rng.uniform(0.3, 1.0))
    c_in = cert.random_cross(1, n, rng, density=rng.uniform(0.3, 1.0))[0]
    c_out = cert.random_cross(n, 1, rng, density=rng.uniform(0.3, 1.0))[:, 0]
    unit = cert.join_loop_gain(G, c_in, c_out)
    if unit > 1e-9:
        if rng.random() < 0.3:
            m = 1 + rng.choice([-1.0, 1.0]) * 10 ** -rng.uniform(2, 6)
        else:
            m = float(np.exp(rng.uniform(np.log(0.2), np.log(5.0))))
        c_out = c_out * (m / unit)
    else:
        c_out = c_out * rng.uniform(0.5, 20.0)
    return G, c_in, c_out


def test_corollary_34_exact_iff_on_random_instances():
    """Claim (models/01 §3.4, [derived], exact): a person p joining a certified group G is certified
    iff c_{p.} (I - Gamma)^-1 c_{.p} < 1 (c_{p.}: what p receives from the members; c_{.p}: what the
    members receive from p).  2,000 random instances (1-12 members, random supports, cycle-free
    groups included), the newcomer's outgoing gains scaled across the threshold as in the 3.2 test.
    rho(Gamma_m) is computed from the enlarged matrix; the scalar is also checked to be rho(P) of §3.2
    for G_2 = {p} (rank one), to a relative 1e-9."""
    seed = 3401
    rng = np.random.default_rng(seed)
    failures, excluded, n_cert, n_near, worst = [], 0, 0, 0, 0.0
    for draw in range(N_JOIN):
        G, c_in, c_out = _join_instance(rng)
        assert cert.spectral_radius(G) < 1                                          # hypothesis: G certified
        s = cert.join_loop_gain(G, c_in, c_out)
        P = cert.loop_gain(G, c_out[:, None], np.zeros((1, 1)), c_in[None, :])      # 3.2 with G_2 = {p}
        worst = max(worst, abs(s - P) / max(1.0, s))
        rho_m = cert.spectral_radius(cert.join_one(G, c_in, c_out))
        if abs(rho_m - 1) < BAND or abs(s - 1) < BAND:
            excluded += 1
            continue
        if (rho_m < 1) != (s < 1):
            failures.append(_report(draw, seed, rho_enlarged=rho_m, scalar=s, Gamma=G, c_in=c_in, c_out=c_out))
        n_cert += rho_m < 1
        n_near += abs(s - 1) < 1e-3
    print(f"\n3.4 iff: {N_JOIN} instances, {len(failures)} disagreements, {excluded} excluded, "
          f"certified {n_cert}, within 1e-3 of threshold {n_near}")
    assert not failures, "Corollary 3.4's iff FAILED; first counterexample:\n" + failures[0]
    assert worst < 1e-9                              # the scalar is rho(P)
    assert excluded <= N_JOIN // 100
    assert 0.3 * N_JOIN < n_cert < 0.7 * N_JOIN      # straddles the threshold
    assert n_near >= 200


def test_corollary_34_row_sum_version_is_sufficient_but_not_needed():
    """Claim (models/01 §3.4 Reading): the row-sum version (the newcomer's incoming sum below 1 and
    every member's total, old plus the newcomer's influence, below 1) is sufficient but not needed.
    (i) 500 random instances satisfying both clauses (checked, not assumed) are certified and have the
    exact scalar below 1.  (ii) Constructed: G = [[0, .1], [.1, 0]], c_in = c_out = (.6, .6): the
    newcomer's incoming sum is 1.2 >= 1 so the row-sum version does not apply, yet rho(Gamma_m) = 0.9 and
    the scalar is 0.8 < 1: certified.  (iii) With (.8, .8) the scalar is 1.42 and rho(Gamma_m) = 1.18:
    a newcomer who is overwhelmed AND strongly reciprocal does break the certificate."""
    seed = 3402
    rng = np.random.default_rng(seed)
    for draw in range(N_JOIN_ROWSUM):
        n = int(rng.integers(1, 13))
        G = cert.random_gain_matrix(n, rng, density=rng.uniform(0.3, 1.0))
        G = cert.scale_rows_to_sums(G, rng.uniform(0.05, 1 - 1e-6, n))             # members' rows sum < 1
        c_in = rng.uniform(0.1, 1.0, n) * (rng.random(n) < 0.8)
        if not c_in.any():
            c_in[0] = 0.5
        c_in = c_in * (rng.uniform(0.0, 1 - 1e-6) / c_in.sum())                      # newcomer's incoming sum < 1
        c_out = (1 - G.sum(axis=1)) * rng.uniform(0.0, 1 - 1e-6, n)                  # member j: row sum + c_jp < 1
        msg = _report(draw, seed, Gamma=G, c_in=c_in, c_out=c_out)
        assert c_in.sum() < 1 and np.all(G.sum(axis=1) + c_out < 1), msg            # both clauses hold
        assert cert.spectral_radius(cert.join_one(G, c_in, c_out)) < 1, msg
        assert cert.join_loop_gain(G, c_in, c_out) < 1, msg
    G = np.array([[0.0, 0.1], [0.1, 0.0]])
    for w, certified in ((0.6, True), (0.8, False)):
        v = np.array([w, w])
        assert v.sum() >= 1                                                           # (ii)/(iii): clause 1 fails
        # (I - G) 1 = 0.9 * 1, so the scalar is 2 w^2 / 0.9; the Perron vector of Gamma_m is
        # (x, x, y), so lambda (lambda - 0.1) = 2 w^2 and rho = (0.1 + sqrt(0.01 + 8 w^2)) / 2
        assert cert.join_loop_gain(G, v, v) == pytest.approx(2 * w * w / 0.9, abs=1e-12)
        assert cert.spectral_radius(cert.join_one(G, v, v)) == pytest.approx(
            (0.1 + np.sqrt(0.01 + 8 * w * w)) / 2, abs=1e-12)
        assert (cert.join_loop_gain(G, v, v) < 1) is certified
        assert (cert.spectral_radius(cert.join_one(G, v, v)) < 1) is certified
