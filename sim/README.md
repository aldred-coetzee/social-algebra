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
