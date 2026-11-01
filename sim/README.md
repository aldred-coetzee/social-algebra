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
what terms. Fetch the Newcomb ranks with `~/.local/bin/uv run python -m models.newcomb_report fetch`, the SNAP
wiki-RfA and Bitcoin files with `~/.local/bin/uv run python -m models.wikirfa_report fetch`.

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

## Wiki-RfA conversion and Bitcoin formation (2026-11-01): 61 tests (44 need no data, 17 skip without it)

`models/wikirfa.py` and `tests/test_wikirfa_conversion.py` run the tie-CONVERSION half of the n = 3 test of
`models/00-v0.md` section 7 on SNAP wiki-RfA, where a voter rates the same candidate at two candidacies
(`docs/prior-work/117` section 3.3, L4564), and the formation half on Bitcoin OTC and Alpha (117 section 3.4);
`models/wikirfa_report.py` writes `results/wikirfa_conversion.md` (all numbers, tables and the verdict; about 7 minutes
on an idle 8-core box, seeded). Data are local-use-only (`data/README.md`: source, terms, sha256). Like the Newcomb run this
is **new computation**, not a published equation; the anchors are 117's own counts.

| Counted by 117 | Ledger ids | Test | Status |
|---|---|---|---|
| wiki-RfA: 198,275 votes (144,451 / 41,176 / 12,648), per-year totals, 11,380 named voters | L4562, L4563 | `test_wikirfa_reproduces_117s_vote_counts` | PASS |
| re-signing: 3,761 pairs vote in more than one year, 7,793 pairs carry more than one vote (16,330 votes), 519 + 158 = 677 changes | L4564, L4855 | `test_wikirfa_resign_counts_reproduce_117_for_the_changes` | PASS (the two non-changing cells give 1,971 and 632 against 117's 1,946 and 647) |
| Bitcoin OTC: 21,492 pairs, 33,493 triangles, 29,900 balanced (89.3%) against a shuffled 69.3%, the closing table, 3,354 one-negative | L4572-L4575 | `test_bitcoin_reproduces_117s_counts_and_the_product_rule` | PASS |
| Bitcoin Alpha: 14,124 pairs, 22,153 triangles (20,016 strictly ordered), 17,567 balanced (87.8%) | L4572, L4576, L4577 | same | PASS |

Findings (full tables in `results/wikirfa_conversion.md`):

1. **Counts.** 198,275 records give 4,047 candidacies, 5,990 re-votes and 1,201 conversions (951 oppose-to-support, 250
   support-to-oppose; 117's 677 is a lower bound and is reproduced exactly), in 229,424 (re-vote, third party,
   orientation) triple instances. The file holds 18 elections under both outcome labels (15 as complete copies), which
   grouping by result turns into 618 spurious zero-day re-votes.
2. **Against the brief's null (signs shuffled within voter, 10,000 draws) conversion moves triples toward weak balance:**
   56.7% of the weak-balance changes are repairs against 50.0% (p < 1e-4), but 4.3 to 6.4 of the 6.7 points are the 79%
   oppose-to-support direction mix (a candidate who failed and ran again is judged better).
3. **Holding the network and permuting who converts (Newcomb's conditional design) leaves +3.1 points** (same new candidacy and
   old sign, z +6.8), **+1.4** (same voter, z +2.9) and +1.2 (also voter generosity, z +3.2); a re-vote in a one-negative triple
   flips at 31.4% against 27.9 / 30.0 / 29.6%. The part only balance could produce (a double-difference contrast that cancels
   the voter's generosity and the candidate's reception) sits in triples where u and v rated the same third party; the
   chain u -> w -> v shows none.
4. **v0 section 7's contrast (one-negative faster than all-negative)** holds against its null only without a voter control
   (+4.7 points, z +5.0; within voter +0.1).
5. **First-tie asymmetry:** a positive tie turns negative above null only when the lone negative tie touches the voter
   (DLL-FF, DLL-BF, LLD-FB: 11.4% against 7.6%), not when it is the third party's tie to the candidate (7.0% against 6.9%); with
   the voter held fixed the contrast is zero, so it is the voter's negativity, not the triple.
6. **Bitcoin:** 117's closure figure reproduces exactly and shrinks under a within-rater (72.7%) and within-ratee (80.1%) shuffle
   in OTC and vanishes in Alpha (strictly ordered, ratee null 87.6% against 87.8%); the all-negative triangle is enriched under
   the global shuffle but, in OTC, depleted under the rater and ratee shuffles, so 117's "strict balance fails" depends on the baseline.
7. **Not decided:** the v0 section 7 criterion "conversion at the null rate" has no unique null, and the answer depends on which is
   taken; votes are not friendships, a vote is a one-shot evaluation, the clock is the candidacy, and re-voters are 3% of pairs.

## Reciprocity gate on the Bitcoin OTC and Alpha networks (2026-11-01): 57 tests (41 need no data, 16 skip without it)

`models/gate_reciprocity_bitcoin.py` (loader, response pairs and covariates, responder-fixed-effects least squares by Gram
matrices, the one-sided / two-sided / dead-zone forms with grid-searched thresholds, cross-validation that re-chooses the
thresholds inside every training fold, cluster bootstrap, Wald and trend tests), `models/gate_reciprocity_bitcoin_report.py`
(every analysis, the verdict guards, and the commands `fetch`, `check`, `report`, `render`) and
`tests/test_gate_reciprocity_bitcoin.py` run v0's O-jive prediction (zero influence inside a band of small partner levels,
L0857) on the SNAP Bitcoin OTC and Alpha ratings (117 section 3.4, L4567-L4580): the rating a trader gives back against the
rating received from the same counterparty, time-ordered. New computation, not a published equation; tables and the verdict
are in `results/gate_reciprocity_bitcoin.md` (about three minutes, seeded; `report --pickle f` then `render f` re-renders the
text without recomputing). The slow end-to-end test needs `GATE_RECIPROCITY_E2E=1`.

| Fact | Ledger ids | Test | Status |
|---|---|---|---|
| OTC 35,592 and Alpha 24,186 ratings, 5,881 and 3,783 nodes, 32,029 / 3,563 and 22,650 / 1,536 positive / negative, 358 and 248 reciprocated pairs with opposite signs, 21,492 and 14,124 pairs | L4568, L4570-L4572 | `test_files_match_the_recorded_checksums_and_117_counts` | PASS |
| OTC 14,100 reciprocated pairs, none tied; Alpha 10,062, of which 7,323 share a timestamp (its times are whole days, 04:00 or 05:00 UTC), 2,739 ordered, every gap at least a day (found here, not in 117) | L4571 | `test_pairing_counts_and_time_resolution` | PASS |
| v0 prediction: the response is flat over a band of small received ratings | L0857 | `test_v0_prediction_a_flat_band_of_small_received_ratings` | XFAIL (strict): +2 is 0.85 above +1, chi2(1) = 221 |
| v0 prediction: the step O-jive with free thresholds is at least as good out of sample as a graded form with no band | L0857 | `test_v0_prediction_the_step_odjive_beats_a_graded_form_without_a_band` | XFAIL (strict): worse by 6.5 SE |
| Planted truths (an O-jive, a sign jump with two slopes, a sign-only step, a one-sided rule, a synthetic network with a planted response): the search and the cross-validation recover them | none (constructed) | `test_search_recovers_...`, `test_cross_validation_...`, `test_pipeline_recovers_...` | PASS |

Findings (full tables in the results file):

1. **Dead zone in the response: refuted on OTC, and on Alpha for every band reaching +2** (Alpha's band {-1, +1} is not
   rejected: 17 responses to a -1, p = 0.07). The response at +2 is 0.85 points (SE 0.06) above the response at +1 on OTC and
   1.06 (0.24) on Alpha; flatness over +1..+4 is rejected at p < 1e-10 on both; the response climbs 0.83 per rating point
   from +1 (95% CI 0.77-0.89; Alpha 0.64-1.02), with responder fixed effects, and the same under none, two-way effects,
   habit covariates and earlier-events-only covariates. As a claim about influence it needs one more step (a shared view of
   the deal adds slope inside any band): no O-jive step sits on top of a linear slope over +1..+4 (equal increments, p = 0.90
   on OTC, 0.54 on Alpha).
2. **The O-jive as written fits worse than a graded response with no band**: out of sample the step form with free thresholds
   loses to a two-sided graded form with the band closed by 0.46 squared rating points (6.5 SE) on OTC and 0.59 (3.1 SE) on
   Alpha; one-sided forms lose by 1.2 to 1.7. Its thresholds (K+ = 3 or 4, K- = -1 or -2) are a step standing in for a ramp.
3. **The best dead-zone fit is a band of the single rating +1** (K+ = 2, K- = -1 in 100% of 1,000 OTC bootstrap draws), and that is
   concavity, not a zone: a step at +2 plus the slope after it span exactly the functions of a no-band curve with two slopes
   and a knee at +2 (equal residual sums of squares, `test_dead_zone_graded_with_the_one_rating_band_is_a_two_slope_curve...`);
   moving the knee to +8 fits better with one threshold instead of two (OTC BIC -120, Alpha -35; out of sample no worse). Against
   the responder's own habit the response to +1 is +0.05 (SE 0.05): +1 is the zero-crossing, the modal rating.
4. **The sign gate is large**: a negative received rating shifts the response by -8.4 (0.34) points against +1 (Alpha -6.6);
   even -1 moves it by -4.1. The level of the received rating predicts better than its deviation from the sender's habit.
   Knee of the positive response about 7 (6-8).
5. **Drift**: the form holds in 2011-2015 (OTC) and 2011-2014 (Alpha); the OTC 1-4 slope rises 0.72 to 0.87 (trend +0.07 per
   year, SE 0.03; +0.06 (0.03) from the yearly estimates); the negative jump and the 9-10 level show no trend once the
   year-to-year scatter is allowed for; 2010 and 2016 have 51 and 21 OTC pairs, too few. Shape does not change with embeddedness; OTC and Alpha
   agree like for like (gap of a day or more).
6. **Caution on meaning**: 58% of OTC responses come within ten minutes and 83% of those repeat the received rating exactly
   (72% of all OTC responses), so this is an association net of the persons' levels (time order is necessary, not sufficient); the negative side is
   asymmetric in time (a negative first rating is answered negatively 95% of the time, but only 47% of negative responses
   followed a negative first rating).
7. **A bug the tests caught**: `ratings_from_array` cast ratings to integers before validating them, so 2.5 became 2
   silently; integrality is now checked first (`test_loader_validation_rejects_malformed_files`).
8. **Review (2026-11-01)**, appended to the results file. Fixed: the two-sided hinge was labelled "no dead zone" but is
   flat over {-1, +1} (a hinge is zero at its knot), so the D-hinge "empty band" was wrong; the earlier-events control set
   used the first rater's whole-file habit; the drift claims for the negative jump and the 9-10 level ignored the
   year-to-year scatter; the verdict claimed Alpha's {-1, +1} refuted. Tests: `test_a_hinge_is_zero_at_its_knot...`,
   `test_increment_test_...`, `test_year_trend_...`, and brute-force checks of the new earlier-events covariate.

## Sign-registry battery (2026-11-01): 102 tests (42 need no data, 60 skip without it); 91 passed, 11 xfailed (strict)

`models/sign_registry_battery.py` and `tests/test_sign_registry_battery.py` run the five tests of `docs/prior-work/112`
section 6.5 on the registry's sign law R-E (person terms a_i + b_j plus the 16 directed triad types, forward chains pp +, pm -,
mp -, mm -; ledger L5421, L4811, L4833) on wiki-RfA, Bitcoin OTC, Bitcoin Alpha and BlueTempNet's feed-creator graph (fetched
from the authors' public GitHub LFS endpoint, checksum-verified; `data/README.md`). `python -m models.sign_registry_battery
compute SITE` caches the statistics (minutes to tens of minutes, seeded); `report` writes `results/sign_registry_battery.md`
(tables, the person-only null, planted mechanisms, variations). The decision rules are constants pinned by a test and were fixed
before any result; amendments made after a first look are listed in the module docstring and in the results file.

| Registry prediction (112 section 6.5) | Ledger ids | Test | Status |
|---|---|---|---|
| 1: FFmm < 0 in the 16-type fit alone (LHK's reading) | L4833, L5421 | `test_t1_ffmm_is_negative_in_the_16_type_fit_alone` | PASS wiki-RfA, Alpha, BlueTempNet; XFAIL OTC (z -1.8) |
| 1: the whole forward chain pp +, pm -, mp -, mm - | L4811 | `test_t1_the_whole_forward_chain_pattern_...` | PASS wiki-RfA, BlueTempNet; XFAIL OTC, Alpha (FFpp undecided) |
| 1: FFmm < 0 survives person terms (R-E as written) | L5421 | `test_t1_ffmm_survives_person_terms_in_the_fit` | XFAIL all four (+0.01, +0.02, -0.06 undecided; +0.11 at BlueTempNet) |
| 2: person terms carry more than triad terms | L5444, L4850 | `test_t2_person_terms_carry_more_than_triad_terms` | PASS all four (D +0.056 to +0.152 AUC) |
| 2: the triad terms add a material mechanism (R2 0.02) | L4829 | `test_t2_triad_terms_add_no_material_...` | not material anywhere (G -0.006 to +0.010); R2 NO |
| 3: sign pattern stable by date, intercepts move | L4857, L4859 | `test_t3_...` | PASS all four |
| 4: opposite-sign reciprocation rare (10% or less) | L4812 | `test_t4_opposite_sign_reciprocation_is_rare` | PASS OTC, Alpha, BlueTempNet; XFAIL wiki-RfA (14.6%) |
| 5: received majority beats own history at C = 0 | L4852, L5444 | `test_t5_target_majority_beats_own_history_...` | PASS wiki-RfA (+0.177); XFAIL OTC, Alpha, BlueTempNet |

Findings (full tables in `results/sign_registry_battery.md`):

1. **Do signs have a mechanism beyond person propensities? No, not a material one.** Held out in time, person terms alone beat triad
   terms alone at every site, and the 16 triad types add G = -0.006 (Alpha), +0.005 (wiki-RfA), +0.009 (BlueTempNet), +0.010 (OTC) AUC
   to person terms: R2 (material = 0.02) is NO at four of four, with receiver-cluster and with sender-and-receiver intervals. At C >= 5
   (dense triad evidence) OTC reaches +0.031.
2. **FFmm < 0 is a person effect.** Fitted alone, as LHK did, it is supported at wiki-RfA, Alpha and BlueTempNet (OTC undecided), but
   signs redrawn from person propensities on the same networks give -0.58 to -0.80, and with person terms in the fit FFmm is
   +0.01, +0.02, -0.06 (undecided) and +0.11 at BlueTempNet (positive). Power is firm at wiki-RfA (a planted -0.3 returns -0.33),
   weak at the Bitcoin sites (-0.04, -0.18).
3. **A small residue is real** (above a person-only world at wiki-RfA, OTC, BlueTempNet; not at Alpha), in mixed-sign chains (FFpm,
   FFmp: a third to two thirds of their size without person terms) and in agreement through a shared third party (FBpp, FBmm, BFpp,
   BFmm positive; FBmp, BFpm negative); and in reciprocity, which R-E lacks (+0.001 to +0.019 AUC).
4. **Drift**: no forward-chain type is contradicted in two date bins at any site while intercepts move (0.9 to 2.7 logit) and the
   between-user variance of the sign moves (BlueTempNet sender ICC 0.37 to 0.70). Opposite-sign reciprocation rises with the date at every site.
5. **Visibility**: the received-majority advantage at low embeddedness (+0.177) is wiki-RfA's and vanishes by C >= 25 as in LHK; it is
   absent at OTC and BlueTempNet. It cannot be read as visibility (quality and shared information are not separated).
6. **Variations**: strict and weak balance are indistinguishable once person terms are in the model (weak beats strict alone, +0.024 at
   wiki-RfA); status adds at most +0.001 AUC; the best of the registry's own forms is person plus 16 types plus status (person plus
   strict balance plus status at Alpha); the best variant overall adds the reverse-tie sign and interactions.
7. **What the test could and could not see**: a planted forward-chain effect of 0.3 per triad adds only +0.004 to +0.009 AUC on
   these skeletons (most edges have little triad evidence), and the static design returns about a quarter to a third of a planted effect
   at wiki-RfA where the causal design returns all of it.

## Test battery index (2026-11-01): the six empirical tests and the wiki-RfA conversion test

One row per test, in the columns of the first table. All are **new computation** on third-party data or on synthetic crowds,
not published equations; the claim column gives the published or pre-registered claim each was set against, and the
results file holds every number and the verdict (each ends with a hand-written `## Review (date)` section; the report
writers keep that section when they regenerate the file). Data-dependent tests skip when `data/` is empty. Fuller
accounts of the Bitcoin reciprocity, sign-registry and wiki-RfA conversion runs are in the sections above.

| Model | Ledger ids / results file | Published or pre-registered claim | Test | Status |
|---|---|---|---|---|
| `models/identifiability_crowd.py`, `identifiability_crowd_report.py` (synthetic crowds from generators outside the fitted family) | `LEDGER` in the module (L1225, L1831, L3959-L3961, L3980, L3988, L4355, L4469); `results/identifiability_crowd.md` | Claim 1 of `models/02-our-claims.md` (a crowd's state is its whole threshold distribution F; ignition, 1.4) and v0 4.4's two-sided gate: can F, the gate sign and the ignition quantity be recovered from an aggregate curve r(0..10)? | `test_identifiability_crowd.py` (31 test functions) | PASS as a finding: F is fitted where the curve visited, the stall point and the instigator share; not F above the stall, the family, the gate sign (except through a decline) or the ignition quantity; 089's count data cannot fit F |
| `models/crowd_gate_wikirfa.py` | L1130, L1201, L1225, L1235, L1831, L3959, L3965, L3967, L4347-L4363, L4392-L4395, L4561-L4564; `results/crowd_gate_wikirfa.md` | v0 4.4: the sign sigma of "more of the crowd acting makes me more likely to act", the shape of participation curves, a one-sided or two-sided gate (Theorem 6.3's object) | `test_crowd_gate_wikirfa.py` (47 test functions) | sigma > 0 as an association (previous-10 share estimator, logit 1.44, z +16.1; influence versus shared shock undecided); no upper gate at decisive success, failure closes the process; the 70% in the participation result is a band edge (SHARE_BANDS), not an estimated breakpoint |
| `models/gate_reciprocity_bitcoin.py`, `gate_reciprocity_bitcoin_report.py` | L4567-L4580, L0857; `results/gate_reciprocity_bitcoin.md` | v0 prediction (the O-jive): zero influence inside a band of small partner levels (L0857) | `test_gate_reciprocity_bitcoin.py` (57 tests, 41 need no data) | Both prediction tests XFAIL (strict): no dead zone, the graded form fits better out of sample (see the section above) |
| `models/sign_registry_battery.py` | L4811, L4812, L4826-L4833, L4850-L4859, L5421, L5444, plus data ids L4561-L4564, L4567-L4580, L4593-L4598; `results/sign_registry_battery.md` | `docs/prior-work/112` section 6.5: five pre-registered tests of the registry's sign law R-E (decision rules R1-R5 fixed before any result) | `test_sign_registry_battery.py` (102 tests, 42 need no data) | R2 NO at four of four sites (triad terms add under 0.02 AUC to person terms); FFmm < 0 is a person effect; a residue of 0.5-1.0 AUC points remains, larger than a planted 0.3 log-odds-per-triad mechanism at OTC and BlueTempNet and of a different form (see the section above); 11 XFAIL (strict) |
| `models/triad_rule_comparison.py` | L0898, L4196, L4481-L4515, L4561-L4580, L4799-L4817, L4833, L4850, L5422; `results/triad_rule_comparison.md` | v0 section 7's criterion: if DLL is depleted like LLD, (4.2d) is refuted and the symmetric rule returns; weak, strict, first-tie and status rules compared on held-out log-loss | `test_triad_rule_comparison.py` (53 test functions) | (4.2d) refuted on Bitcoin OTC and Alpha, weakly reproduced on wiki-RfA (a reception pattern); weak balance has the lowest held-out log-loss of the four single rules in 41 of 49 configurations |
| `models/apache_activity_survival.py` | L4623-L4633, L4666, L1225, L1831, L5779, L5740, L0512, L0527, L0547, L3057, L1404-L1406, L5742, L4367, L5764; `results/apache_activity_survival.md` | Claim 1: the shape of the activity distribution (not its mean) predicts graduation; size and early-warning signals (v0 section 7, team scale) | `test_apache_activity_survival.py` (53 test functions) | (1) shape beyond size and mean: not supported (AUC change +0.000); (2) size is the predictor and the shape-by-size interaction is supported; (3) growth versus collapse predictive, critical-mass step and early-warning signals not found (the monthly series could not have shown them) |
| `models/wikirfa.py`, `wikirfa_report.py` (conversion half; Bitcoin formation half) | L4562-L4564, L4572-L4577, L4855; `results/wikirfa_conversion.md` | `models/00-v0.md` section 7: conversion of a one-negative triple into a balanced one is faster than of an all-negative triple, at the null rate (the n = 3 test, conversion half) | `test_wikirfa_conversion.py` (61 tests, 44 need no data) | Counts reproduce 117's; conversion moves toward weak balance by +6.7 points over the within-voter null, mostly direction mix; +1.2 to +3.1 under network-held nulls; not decided (see the section above) |
| `models/synthetic_population.py` | none (synthetic generator of our own; `notes/2026-10-29-modelled-population-testbed.md`); `results/synthetic_population_identifiability.md` | Pre-registered: with known drives generating behaviour (softmax choice model, not v0's linear form), can drives be recovered from activity and tie events (C1), and does a drive-based predictor beat person rates on held-out group outcomes (C2, C3), at n = 3, 8, 25? | `test_synthetic_population.py` (15 tests) | see the results file |
| `models/szekely_composition.py` | none (measured SVO angles in a real threshold game; `results/synthetic_population_identifiability.md` Decision is why composition is under test); `results/szekely_composition.md` | Claim 1 of `models/02-our-claims.md` (the group state is a count above a cut, not a mean) and whether a measured drive adds to person rates: pre-registered K1-K3 (rule written before any fit) per phase and pooled, Szekely et al. 2021 | `test_szekely_composition.py` (19 tests, 5 need data) | K1 weak (point passes, intervals contain 0), K2 NOT MET, K3 NOT MET in every stratum; person rates carry the held-out information |
