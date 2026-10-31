# sim/ -- regression tests of the adopted equations

**Purpose.** Reproduce, as `pytest` tests, the published results of the equations that
`models/00-v0.md` (v0.1) adopted, so that a misread equation in a survey or in v0.1 shows up as a
failing test. This is validation of the equation set. It is **not** the modelled population of
`notes/2026-10-29-modelled-population-testbed.md`: nothing here simulates people, fits data, or runs
v0.1 as a population model. Each test states the published claim, paper and ledger id(s) in its
docstring; each module docstring names the prior-work file and section. Tests assert the published
result and were not tuned to pass; a failure is a finding.

## Run

    cd sim
    ~/.local/bin/uv sync          # creates .venv from pyproject.toml / uv.lock; never system packages
    ~/.local/bin/uv run pytest

(The old `.venv` from 2026-10-29 was reused by `uv sync` without trouble, so `UV_PROJECT_ENVIRONMENT`
was not needed.) `uv.lock` is committed. Python >= 3.12; numpy, scipy, pytest only.

Tests on third-party data skip (with the command in the reason) when the data file is absent: the
files in `data/` are local-use-only and git-ignored, `data/README.md` records where each came from and on
what terms. Fetch the Newcomb ranks with `~/.local/bin/uv run python -m models.newcomb_report fetch`.

## Results (2026-10-31): 156 passed, 3 xfailed (strict), 0 failed

| Model | Ledger ids | Published result | Test | Status |
|---|---|---|---|---|
| Wankhede et al. 2025, v0.1 Thm 6.1 / (4.3c) | L3993, L4004 | A4: w_i > 2E_i => unique globally exponentially stable equilibrium; mu_inf(J) = max_i[-w_i + 2E_i - 3z_i^2/r_i] | `test_wankhede_theorem61.py` | PASS |
| v0.1 6.1, Euler turns (derived) | L4004 | ‖I+hJ‖_inf = 1 - h min(w_i - 2E_i); contraction; Euler limit = ODE equilibrium | same | PASS |
| Wankhede converse (constructed) | L4004 | w < 2c hostile pair has two stable attractors; w > 2c one | same | PASS |
| Marvel et al. 2011, dX/dt = X^2 | L0898, L3154 | closed form; blow-up at t* = 1/lambda_1; X/‖X‖ -> omega_1 omega_1^T; sign pattern = two factions (all triangles balanced); no blow-up if lambda_1 <= 0; zero component leaves pattern unsigned | `test_marvel_blowup.py` | PASS |
| Granovetter 1978 two crowds | L1225, L1831, L3960, L3961 | thresholds 0..99 -> 100; second threshold-2 replacing threshold-1 -> 1 | `test_granovetter_crowds.py` | PASS |
| v0.1 Thm 6.3(i) | L1201, L1235 | monotone F: non-decreasing orbit, fixed point within n steps, = least fixed point | same | PASS |
| v0.1 two-sided gate (2.3, 4.4) | L3959, L4355 | F = F_theta - F~_thetabar; constructed non-monotone F (n=2) cycles 0->1->0, one-sided version converges | same | PASS |
| Leonard et al. 2012, Eq. 7 | L3873, L3874 | theta_c = 2 arccos r: 51.7, 106.3, 90.0 degrees | `test_leonard_thetac.py` | PASS |
| Leonard decisions M010, M001 | L3873, L3874 | stable iff theta2 > theta_c (checked at theta_c +/- 0.5 and 3 degrees, r = 0.9, 0.6, 0.707, by solving Eq. 6 numerically) | same | PASS |
| Leonard compromise M111 | L3874 | stable for theta2 < theta_c | same | PASS |
| Leonard full dynamics | L3871-L3873 | keeps 12 uncoupled above theta_c, couples it below (+/- 8 degrees) | same | PASS |
| Leonard Table 1 (N3 > 2N1: M111 unstable exactly when decisions stable) | 086 Table 1 | not reproduced by the transverse test | same | XFAIL (strict), see Findings |
| Altafini 2013 Thm 1 | L4304, L4307 | balanced connected undirected: limit (1/n) 1^T D x0 D1; unbalanced: 0 | `test_altafini_095.py` | PASS |
| Altafini 2013 Thm 2 | L4308 | strongly connected, digon sign-symmetric digraph: nu^T D x0 D1 (balanced), 1/n if weight balanced, 0 if unbalanced | same | PASS |
| Proskurnikov et al. 2016 Example 1 | L4310, L4311 | a12 = a21 = -1, a31,a32 > 0: x -> (xi, -xi, rho xi), not 0, not polarised | same | PASS |
| v0.1 (3.0) smoke, n = 3 and 10 | L0853, L0857, L2096, L4368 | closed gates => x_i -> p_i, error x r_i^(+/-) each turn, monotone (Thm 6.2) | `test_v01_generic_update.py` | PASS |

### Parked tests (predate the ledger; kept, all pass)

| Module | Ledger ids now cited | Notes |
|---|---|---|
| `allesina_tang.py` / test | none exist (only `sa` L1399, L1417 on May's criterion) | not an adopted equation; v0.1 does not use it |
| `altafini.py` / test | L2270, L3643, L3644 (`sa`), superseded by `read` L4304, L4307, L4308 | module extended with digraph helpers for the 095 tests |
| `honeybee.py` / test | L2327, L2328, L2329, L1356, L2331, L3653 | test also records that survey 29's 0.41 symmetric split is really 0.381 |
| `lotka_volterra.py` / test | none (A1 never extracted as equations) | not used by v0.1 |

## Findings

1. **Theorem 6.2 wording (v0.1).** It says closed gates leave "D1 (+ D3) alone ... x_i -> p_i at
   rate 1 - r_i". With D3 present and g_i != p_i that is false: the fixed point is
   ((1-r)p + omega g)/((1-r) + omega) and the rate is 1 - r + omega. True only with D3 absent (or
   g_i = p_i with the rate corrected). Same caveat for 6.1's "D3 absent or with a common goal"
   as far as a single equilibrium p_i is concerned. Asserted in `test_d3_changes_the_limit_so_62_needs_d3_absent`.
2. **Leonard Table 1** (xfail above). The decision-manifold threshold (Eq. 7) reproduces
   exactly; the claim that the compromise M111 is unstable above theta_c for N3 > 2N1 does not
   follow from the transverse sign test, which is only a necessary condition. Unresolved: it needs
   the slow-flow Jacobian on M111 and Eq. 8, or the paper's SI.
3. Test constructions that are v0.1's or ours, not published: Wankhede hostile-pair counterexample,
   the n = 2 cycling F, the Euler-turn norm identity (v0.1 6.1 [derived]), Leonard's use of the
   eta-sign as the stability criterion (derived from L3872).

## Newcomb n = 3 test (2026-11-01): 44 tests (19 need no data, 25 skip without it)

`models/newcomb.py` and `tests/test_newcomb_triads.py` run the n = 3 refutation test of `models/00-v0.md`
section 7 on the Newcomb fraternity ranks (`docs/prior-work/104`, ledger L4471-L4546);
`models/newcomb_report.py` writes `results/newcomb_n3.md` (all numbers, tables and the verdict; about a
minute, seeded). Unlike the rows above this is **new computation**, not a published equation: the static half
reproduces Doreian & Krackhardt (2001); the conversion half (type-to-type transitions, against a null that
keeps each man's own persistence) is printed in neither D&K paper.

| Published result | Ledger ids | Test | Status |
|---|---|---|---|
| D&K 2001 Figure 1, ten claims stated in words, under their 10,000-draw row-wise sign shuffle: LLD and LDL under-represented from week 1, DLL over-represented from week 6, DDD over from week 5, LLL and LDD over, DLD and DDL under | L4485-L4498 | `test_dk_figure1_pattern_is_reproduced`, `..._exact_values_...` | PASS (10 of 10 at top-4/bottom-3; 7, 7 and 4 of 10 at 3/3, 5/4, 3/2) |
| 1996 paper on the same ranks: 30-35 reciprocated ties of 68 a wave (36 in weeks 3-5 and 10), null about 17, first-transition turnover "slightly above 30%" | L4520, L4521, L4527 | `test_recode_reproduces_the_1996_papers_...` | PASS (30-36, 36 exactly in waves 3, 4, 5, 10; 31.2%) |
| 68 + and 51 - ties every wave, 4/3/9 per man | L4476, L4480 | `test_fixed_counts_per_wave` | PASS |

Findings (full tables in `results/newcomb_n3.md`):

1. **The pre-specified undirected cell cannot be run.** With only mutual same-sign ties ("agree" symmetrisation) the
   data hold one one-negative triangle in 15 waves against 0.25 expected per wave; conversion has 1 and 7 triangles
   at risk. The "sum" rule (either direction signs a pair) and D&K's directed triples carry the analysis.
2. **Static half: supported in aggregate, refuted for DLL.** The one-negative pool is below the sign-shuffled null in all
   15 waves, LLD and LDL in all 15, but DLL (also one-negative, first tie negative) is above it from wave 6; DDD is
   enriched. Symmetric (4.2b)/(5.1) cannot tell the three apart; strict balance fails, weak survives as a depletion.
3. **Dynamic half: not decided.** Conversion of a one-negative triple into a complete balanced one is rare (15
   directed, 33 "sum" events), about 1.5 times its null rate (p 0.10 and 0.02), and not shown faster than the
   all-negative class (p 0.33 and 0.08). Counting a lost tie as balanced (v0 section 4.2, post hoc), one-negative
   resolves faster than all-negative, but because all-negative triples are unusually stable.
4. **The brief's "16 D&K types" are eight** (LLL ... DDD); sixteen is Leskovec et al.'s directed triad count.
5. **D&K's footnote that the qualitative results hold at top-3/bottom-3 and top-3/bottom-2 (L4478) is true of the
   contrasts and false of the wave-by-wave details** (7 and 4 of their 10 claims hold). The recode decides the power,
   not the static verdicts.
