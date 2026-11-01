# Szekely 2021: does the composition of measured drives predict a group's threshold outcome, and do drives add to person rates?

**Caveats (added 2026-11-01).** The K1 margin (the 0.55 cut) was fixed after the outcome frequencies had been seen (line "The rule's margin was fixed after seeing outcome frequencies" below), though before any relation of a drive to an outcome was computed; read K1 with that in mind. One group size, one measured drive.

_Generated 2026-11-01 by `uv run python -m models.szekely_composition report` (seed 20261101; 2000 bootstrap draws). Code: `sim/models/szekely_composition.py`; checks: `sim/tests/test_szekely_composition.py`. Built on `sim/models/apache_activity_survival.py` and `sim/models/apache_fitted_case.py` (`logit_fit`, `auc_score`, `logloss`, `Frozen`, `criterion`, `bootstrap` imported, not changed). Data: Szekely, Lipari, Antonioni, Paolucci, Sanchez, Tummolini & Andrighetto (2021), Nature Communications 12, 5452, doi:10.1038/s41467-021-25734-w (article CC BY 4.0); data OSF project https://osf.io/wvgk9, file `full.csv` (OSF project licence field empty; reuse is 'data available' with attribution); local-use-only and git-ignored; this file holds counts and statistics only, never a participant row._

**What we are trying to achieve (one line).** An algebra of drives, of persons and of groups, composed into an equation set usable to predict or steer outcomes at the membership, group and crowd scales, sensitive to group size, composition and definition (`CLAUDE.md`, 2026-10-29); first outcome activity (2026-11-01). This is the composition test on a real experiment with a measured drive: the synthetic population (`results/synthetic_population_identifiability.md`, Decision) found drives recoverable but their LINEAR composition no better than person rates, so how the drives are combined is what is under test here.

## Facts about the data, established before the rule's parameters were fixed

Read from `full.csv` (sha256 `b0f366fe...bbeeb2`, 4.5 MB) before the rule's parameters were fixed. Only the structure of the file, its group-level outcome frequencies and its person-level distributions were looked at; no relation between any drive and any outcome was computed.

- **Size and the "two rows per person-round".** 14,872 rows, 286 persons, 28 rounds. The file is long in the experiment's belief-manipulation design: in 8 of the 28 rounds (1, 5, 10, 14, 15, 19, 24, 28) each person has FOUR rows, one per hypothetical-expectation condition (`manipulation`: High or Low empirical expectation crossed with High or Low normative expectation, used for the conditional-contribution elicitation), and in the other 20 rounds one row (`manipulation` blank). So 20 x 286 + 8 x 286 x 4 = 14,872. The flag `odr` is 1 on exactly one row per person-round (8,008 rows = 286 x 28; the "High EE and High NE" row in a conditional round, the blank row elsewhere) and 0 on the other 6,864 (286 x 8 x 3); the 6,864 carry no `contribution` and no `total_contribution`. The meaning of `odr` is inferred from this (the file's codebook was not read); what is established is that `odr` = 1 selects one row per person-round that carries the actual game record, and every analysis here uses those 8,008 rows only.
- **Treatment and the switch.** Two orders: High (0.9) to Low (0.6), 148 persons; Low (0.6) to High (0.9), 138. `disaster_probability` is constant within each phase of a person and changes at **round 15**: rounds 1-14 are phase 1, rounds 15-28 phase 2. It is the same for all members of a group-round (a group never mixes orders).
- **Group id and size.** `group_id` identifies a group-round (1,392 distinct values, each in exactly one round): groups are reshuffled every round. 1,261 group-rounds have six rows in the file; 131 have 1-5 (rounds 1-3 hold 48-49 groups, the rest 50). Players absent from the file still contributed to `total_contribution`.
- **Threshold.** In 800 of 1,392 group-rounds `total_contribution` is at least 300 and in all 800 `disaster_outcome` is 0; below 300 a disaster occurs with the round's probability (199 of 218 at 0.9, 220 of 374 at 0.6). The threshold is therefore 300 (of a 600 maximum with six players). The recorded total ranges 0 to 485; 57.5% of group-rounds reach 300. `total_contribution` equals the sum of the members' recorded contributions in the 1,063 six-row groups with no missing contribution; where a member has no recorded contribution the total usually exceeds the sum (of the 151 six-row, no-exclusion cases with exactly one member missing: by exactly 50 in 72, by 0 in 4, by other amounts from 20 to 90 in the rest).
- **`inactive` and `excluded`.** `inactive` is a running count of the person's rounds with a timeout on the contribution decision (non-decreasing; 0 for 10,873 of 14,872 rows). In the 8,008 game rows the contribution is missing in exactly 567, exactly the rows where `timeout_contribute` says a timeout occurred. `excluded` = "Excluded" on 371 game rows (23 persons, absorbing: once excluded, excluded for every later round; the first exclusion falls at inactive = 4); an excluded person has no contribution and leaves the group. Timeout players who are not excluded stay in the group and the total includes a default for them.
- **Persons.** `svo_angle`, `risk` and `agreeableness` are constant per person and have no missing value (286 each). `risk` is an ordinal scale exported with value labels on its ends only: persons have 1 (57), 2 (85), 3 (41), 4 (40), or the labels "Risk averse" (44) and "Risk seeking" (19), whose numeric codes the file does not give; the six levels read as a 0-5 scale with the labelled ends at 0 and 5 (an inference, recorded as a decision below). `agreeableness` is numeric, 17 to 45. `svo_angle` runs from -11.7 to 61.2 degrees, median 30.2; share of persons above 15 / 20 / 22.45 / 25 / 30 / 35 degrees: 0.797 / 0.734 / 0.699 / 0.650 / 0.507 / 0.364. `svo_type`: Prosocial 199, Individualistic 86, Altruistic 1.
- **Lag.** `contribution_1` is the previous round's recorded contribution (7,179 of 7,179 comparable pairs match exactly); missing in round 1 and after a timeout.
- **What was seen of the outcome before the rule.** The overall frequency of threshold-reached group-rounds (57.5%) and its frequency by round (0.82 in round 1, falling to 0.44 in round 28), over all rounds including the ones that are now test rounds. This is an aggregate of the outcome, not a relation with any drive. The rule, the split and the margin were fixed after seeing it.

## The rule, written before any fit

Copied from the brief of 2026-11-01; the one bracketed parameter of item 2 ("[about 70%]") is filled from the data facts above (10 of the phase's 14 rounds) and the rounds are written out; nothing else is changed. Written into this file before the first model was fitted (`report` refuses to run unless this block is already here).

1. Unit: a group-round (one group of 6 in one round, one treatment order), with outcome y_bin = threshold reached (total contribution >= 300) and y_cont = total contribution. Persons' drive inputs: svo_angle (primary); secondary: risk, agreeableness.
2. Split, out of time within each treatment phase: phase 1 = rounds before the switch (rounds 1-14), phase 2 = rounds from the switch (rounds 15-28); within each phase the first 10 rounds (rounds 1-10 and 15-24; 71%, about 70%) train and the last 4 rounds (rounds 11-14 and 25-28; 29%, about 30%) test. Person-level training statistics (rates) are computed on training rounds only. Nothing from test rounds enters any fit. Models are fitted once per phase and frozen.
3. Models of the group outcome, all ridge (penalty 1, standardised on training), logistic for y_bin, linear for y_cont:
   (0) training base rate / mean;
   (M) mean composition: group mean of svo_angle (the field's standard aggregation);
   (Mo) moments: mean, min, max, sd of svo_angle;
   (T) threshold composition (ours, Claim 1 in models/02-our-claims.md: the group state is the count above a cut): the number of members with svo_angle above a cut c, with c chosen on the training rounds from the grid {15°, 20°, 22.45°, 25°, 30°, 35°} by training log-loss, then frozen; plus the number above a second cut if that improves training log-loss (at most two cuts);
   (R) person rates: each member's mean contribution over the training rounds of that phase (a person-effects rival; members with no training rounds get the training grand mean), aggregated as mean and min;
   (R+T) rates plus the threshold count;
   (R+M) rates plus the SVO mean.
4. Score on the test rounds once: held-out AUC and log-loss for y_bin, RMSE for y_cont (relative to predicting the training mean). Bootstrap over test group-rounds, 2,000 draws, seed 20261101, for the decisive differences.
5. Criteria, fixed now: (K1) measured drives carry information: M beats 0 on held-out log-loss and its AUC exceeds 0.55. (K2) composition matters: T beats M by more than 0.02 held-out AUC AND lower log-loss. (K3) drives add to rates: R+T beats R by more than 0.02 AUC AND lower log-loss (also report R+M vs R). Each per phase and pooled.
6. Secondary, labelled: the same with risk and agreeableness in place of svo_angle; and a dynamic person state, the member's previous-round contribution (contribution_1) aggregated as mean, as a further rival (D), vs R.
7. Everything else exploratory and labelled so. No re-tuning after scoring.

## Decisions the rule left open (taken before any fit)

- **Population.** A group-round is in the analysis if all six of its members have a row in the file and none of them is excluded (1,228 of 1,392; the others are counted below by reason). A group of fewer than six rows has members the file does not describe, so its composition is unknown; an excluded member is not playing and the group is not a group of six. Members who timed out (no recorded contribution) stay in: they are in the group and their drive values are known. The outcome is the recorded `total_contribution` (which includes the default for a timeout), y_bin = total >= 300, y_cont = total.
- **Treatment order.** Both orders are pooled within a phase. No model has an order or disaster-probability term (the rule's feature lists have none), so the 0.9 and 0.6 conditions are a source of unexplained outcome variation and a possible confound for any feature that differs between orders; the number of each order in each set is reported.
- **Phases and the pooled row.** Models are fitted once per phase (rule item 2). The pooled row concatenates the two phases' frozen test predictions and scores them together; nothing is refitted on pooled data. The pooled baseline (0) is each phase's own training base rate, so its pooled AUC is not 0.5.
- **Rates (R).** A person's rate in a phase is the mean of the person's recorded contributions (timeout rounds are skipped) over that phase's 10 training rounds, taken from every one of the person's game rows in those rounds (including rows in group-rounds that are not in the analysis). A person with none gets the grand mean of all recorded contributions in that phase's training rounds. In the TRAINING group-rounds a member's rate includes that member's own contribution in the very round being predicted, so R is flattered inside training and its coefficients are fitted on a feature that is partly the outcome; in the test rounds it is a pure forecast. The rule fixes this construction; the consequence is a caveat.
- **Cut choice (T).** Candidate counts use a strict inequality (angle > c). Each candidate cut is scored by the in-training log-loss of the ridge logistic model on that one count; the lowest wins, ties to the lower cut. A second cut is the best remaining grid value given the first (lowest in-training log-loss of the two-count model) and is KEPT if that two-count log-loss is lower than the one-cut log-loss at all (read literally: 'if that improves training log-loss'); no tolerance. Cuts are chosen per phase from that phase's training rounds only. For risk and agreeableness, whose scales differ, the grid is the 20th, 35th, 50th, 65th and 80th percentiles of the distinct persons who appear in that phase's training group-rounds.
- **Fit.** Logistic: `apache_activity_survival.logit_fit` through `apache_fitted_case.Frozen` (ridge penalty 1 on inputs standardised on the training rows, intercept free). Linear: centre y on the training mean, standardise the inputs on training, minimise squared error + 1 x |b|^2. Means, standard deviations and coefficients are stored from training and applied unchanged to the test rows.
- **Mo and sd.** sd is the population standard deviation (ddof 0) of the six members' angles.
- **Scoring.** Held-out AUC (`auc_score`, ties one half) and log-loss (`logloss`, clipped to [1e-6, 1-1e-6]) of y_bin; RMSE of y_cont, also given as a ratio to the RMSE of predicting the phase's training mean (below 1 beats the baseline).
- **Criteria edges.** Every margin is strict: K1 needs M's AUC > 0.55 and M's log-loss < the baseline's; K2 and K3 need an AUC difference > 0.02 (compared after rounding to 12 places, so that float noise cannot turn exactly 0.02 into 'more') and a lower log-loss. Where the criterion fails because of an AUC difference between 0 and 0.02, or because only one condition holds, the file says which.
- **Bootstrap.** Resample the test group-rounds with replacement, 2,000 draws, seed 20261101, within a phase for the phase rows and over the concatenated test rows for the pooled row; predictions frozen; the same draws for every model; a draw with one class only is skipped and counted. 95% percentile intervals, reported for every difference named in the criteria and for each model's AUC and log-loss. The bootstrap resamples group-rounds as independent although the same persons recur across rounds (a caveat).
- **Dynamic state (D).** The mean over the six members of `contribution_1`, the previous round's recorded contribution. A missing value (round 1, or after a timeout) is replaced by the phase's training mean of `contribution_1`. D is a one-step-ahead forecast: in a test round it uses the members' contributions in the previous round, which may itself be a test round; this is an input observed before the round, not a fit to test data. D is scored against R only.
- **Risk coding.** `risk` mixes the numerals 1-4 with two text labels. The labels are mapped to the ends of the scale the numerals sit inside: "Risk averse" = 0 and "Risk seeking" = 5, so the scale reads 0-5 in the order averse, 1, 2, 3, 4, seeking. This is an inference from the labelling, not from a codebook; risk's cut grid is percentile-based, so only the ordering matters for T, but the spacing matters for the mean in M, Mo and R+M. The direction (higher = more risk-seeking) does not matter to any model.
- **Secondary drives.** Risk and agreeableness get the same models M, Mo, T, R+T, R+M (cuts from the percentile grid) and the same K1-K3; R and D do not depend on the drive and are the same models as in the primary.

## Counts

File: 14,872 rows; 286 persons; game rows (`odr` = 1): 8,008. Group-rounds in the file: 1,392. Dropped from the analysis: fewer than 6 rows: 131; 6 rows, a member excluded: 33; no recorded total: 0. Analysed: 1,228 group-rounds of six.

| phase | set | rounds | group-rounds | reached / not | reached share | mean total | High-first order group-rounds |
|---|---|---|---|---|---|---|---|
| 1 | train | 1-10 | 451 | 304 / 147 | 0.674 | 308.1 | 240 |
| 1 | test | 11-14 | 174 | 111 / 63 | 0.638 | 297.1 | 96 |
| 2 | train | 15-24 | 432 | 253 / 179 | 0.586 | 298.2 | 238 |
| 2 | test | 25-28 | 171 | 88 / 83 | 0.515 | 289.5 | 95 |

Persons without any recorded contribution in a phase's training rounds (given the grand mean): phase 1 1, phase 2 15.

## Frozen choices and coefficients (primary drive, svo_angle; fitted on training rounds only)

- **Phase 1.** Grid [15.0, 20.0, 22.45, 25.0, 30.0, 35.0]. Cut(s) chosen for T: **22.45, 25** degrees; in-training log-loss with one cut 0.6274, with the final cut set 0.6170.
- **Phase 2.** Grid [15.0, 20.0, 22.45, 25.0, 30.0, 35.0]. Cut(s) chosen for T: **15, 35** degrees; in-training log-loss with one cut 0.6642, with the final cut set 0.6614.

Coefficients act on inputs standardised on the training rows; positive goes with reaching the threshold. Logistic ridge, penalty 1.

| phase | model | features | coefficients on standardised inputs (intercept first) | in-training AUC |
|---|---|---|---|---|
| 1 | M | mean | +0.729, +0.113 | 0.532 |
| 1 | Mo | mean, min, max, sd | +0.729, +0.120, -0.035, -0.010, -0.043 | 0.535 |
| 1 | T | n above 22.45, n above 25 | +0.750, +0.808, -0.690 | 0.590 |
| 1 | R | rate mean, rate min | +0.883, +1.187, +0.340 | 0.818 |
| 1 | R+T | rate mean, rate min, n above 22.45, n above 25 | +0.910, +1.199, +0.312, +0.673, -0.643 | 0.821 |
| 1 | R+M | rate mean, rate min, mean | +0.888, +1.169, +0.358, +0.086 | 0.817 |
| 1 | D | previous-round contribution, mean | +0.887, +1.314 | 0.797 |
| 2 | M | mean | +0.351, +0.259 | 0.573 |
| 2 | Mo | mean, min, max, sd | +0.352, +0.276, +0.128, -0.106, +0.121 | 0.583 |
| 2 | T | n above 15, n above 35 | +0.356, +0.278, +0.170 | 0.611 |
| 2 | R | rate mean, rate min | +0.296, +2.038, +0.321 | 0.873 |
| 2 | R+T | rate mean, rate min, n above 15, n above 35 | +0.294, +1.993, +0.362, +0.086, +0.210 | 0.876 |
| 2 | R+M | rate mean, rate min, mean | +0.299, +2.008, +0.339, +0.109 | 0.873 |
| 2 | D | previous-round contribution, mean | +0.370, +1.348 | 0.802 |

## Held-out result, primary drive (svo_angle), scored once

### Phase 1: 174 test group-rounds (111 reached, 63 not; 0 of 2000 draws skipped for one class)

| model | held-out AUC [95% bootstrap] | held-out log-loss [95% bootstrap] | RMSE of total / baseline RMSE |
|---|---|---|---|
| 0: training base rate / mean | 0.500 [0.500, 0.500] | 0.658 [0.607, 0.708] | 1.000 |
| M: mean of the drive | 0.581 [0.498, 0.666] | 0.652 [0.602, 0.703] | 0.998 |
| Mo: mean, min, max, sd of the drive | 0.578 [0.490, 0.662] | 0.651 [0.601, 0.703] | 1.002 |
| T: count above a cut (cuts chosen on training) | 0.556 [0.466, 0.642] | 0.660 [0.604, 0.719] | 0.999 |
| R: person rates (mean, min) | 0.811 [0.740, 0.875] | 0.485 [0.400, 0.567] | 0.746 |
| R+T: rates + count above cut | 0.793 [0.717, 0.861] | 0.497 [0.407, 0.589] | 0.752 |
| R+M: rates + mean of the drive | 0.810 [0.740, 0.874] | 0.485 [0.401, 0.569] | 0.752 |
| D: previous-round contribution (mean) | 0.810 [0.738, 0.875] | 0.508 [0.445, 0.578] | 0.660 |

### Phase 2: 171 test group-rounds (88 reached, 83 not; 0 of 2000 draws skipped for one class)

| model | held-out AUC [95% bootstrap] | held-out log-loss [95% bootstrap] | RMSE of total / baseline RMSE |
|---|---|---|---|
| 0: training base rate / mean | 0.500 [0.500, 0.500] | 0.703 [0.679, 0.729] | 1.000 |
| M: mean of the drive | 0.543 [0.455, 0.626] | 0.698 [0.667, 0.731] | 0.995 |
| Mo: mean, min, max, sd of the drive | 0.548 [0.463, 0.632] | 0.699 [0.666, 0.733] | 0.999 |
| T: count above a cut (cuts chosen on training) | 0.548 [0.463, 0.632] | 0.697 [0.660, 0.735] | 1.001 |
| R: person rates (mean, min) | 0.853 [0.789, 0.908] | 0.503 [0.412, 0.606] | 0.756 |
| R+T: rates + count above cut | 0.848 [0.786, 0.904] | 0.509 [0.418, 0.612] | 0.763 |
| R+M: rates + mean of the drive | 0.852 [0.789, 0.907] | 0.506 [0.415, 0.610] | 0.758 |
| D: previous-round contribution (mean) | 0.861 [0.805, 0.911] | 0.487 [0.427, 0.551] | 0.666 |

### Pooled: 345 test group-rounds (199 reached, 146 not; 0 of 2000 draws skipped for one class)

| model | held-out AUC [95% bootstrap] | held-out log-loss [95% bootstrap] | RMSE of total / baseline RMSE |
|---|---|---|---|
| 0: training base rate / mean | 0.563 [0.510, 0.621] | 0.680 [0.650, 0.708] | 1.000 |
| M: mean of the drive | 0.610 [0.552, 0.671] | 0.675 [0.643, 0.704] | 0.997 |
| Mo: mean, min, max, sd of the drive | 0.606 [0.546, 0.669] | 0.675 [0.643, 0.704] | 1.000 |
| T: count above a cut (cuts chosen on training) | 0.581 [0.523, 0.645] | 0.678 [0.642, 0.713] | 1.000 |
| R: person rates (mean, min) | 0.838 [0.796, 0.881] | 0.494 [0.428, 0.560] | 0.751 |
| R+T: rates + count above cut | 0.829 [0.785, 0.873] | 0.503 [0.436, 0.572] | 0.758 |
| R+M: rates + mean of the drive | 0.837 [0.793, 0.880] | 0.495 [0.429, 0.563] | 0.756 |
| D: previous-round contribution (mean) | 0.839 [0.795, 0.883] | 0.498 [0.451, 0.544] | 0.663 |

## Decision, exactly per the criteria (primary drive)

**K1** (measured drives carry information: M beats 0 on held-out log-loss AND its AUC exceeds 0.55).

| stratum | M held-out AUC [95%] | M log-loss | baseline log-loss | log-loss M - 0 [95%] | criterion |
|---|---|---|---|---|---|
| phase 1 | 0.581 [0.498, 0.666] | 0.652 | 0.658 | -0.006 [-0.014, +0.003] | MET |
| phase 2 | 0.543 [0.455, 0.626] | 0.698 | 0.703 | -0.005 [-0.023, +0.014] | NOT MET |
| pooled | 0.610 [0.552, 0.671] | 0.675 | 0.680 | -0.005 [-0.016, +0.005] | MET |

**K2** (composition matters: T beats M by more than 0.02 held-out AUC AND lower log-loss). Differences are T minus M.

| stratum | test group-rounds | AUC difference [95%] | log-loss difference [95%] | share of draws AUC > +0.02 | criterion |
|---|---|---|---|---|---|
| phase 1 | 174 | -0.025 [-0.121, +0.070] | +0.008 [-0.016, +0.040] | 0.171 | NOT MET |
| phase 2 | 171 | +0.005 [-0.034, +0.043] | -0.001 [-0.015, +0.012] | 0.222 | NOT MET |
| pooled | 345 | -0.029 [-0.073, +0.017] | +0.004 [-0.012, +0.020] | 0.019 | NOT MET |

**K3** (drives add to rates: R+T beats R by more than 0.02 AUC AND lower log-loss). Differences are (R+T) minus R.

| stratum | test group-rounds | AUC difference [95%] | log-loss difference [95%] | share of draws AUC > +0.02 | criterion |
|---|---|---|---|---|---|
| phase 1 | 174 | -0.018 [-0.046, +0.004] | +0.013 [-0.008, +0.039] | 0.000 | NOT MET |
| phase 2 | 171 | -0.004 [-0.017, +0.008] | +0.007 [-0.007, +0.020] | 0.001 | NOT MET |
| pooled | 345 | -0.009 [-0.022, +0.002] | +0.010 [-0.003, +0.024] | 0.000 | NOT MET |

K3, companion report (rule item 5): (R+M) minus R.

| stratum | test group-rounds | AUC difference [95%] | log-loss difference [95%] | share of draws AUC > +0.02 | criterion |
|---|---|---|---|---|---|
| phase 1 | 174 | -0.001 [-0.010, +0.007] | +0.000 [-0.005, +0.006] | 0.000 | NOT MET |
| phase 2 | 171 | -0.001 [-0.006, +0.005] | +0.003 [-0.002, +0.009] | 0.000 | NOT MET |
| pooled | 345 | -0.001 [-0.006, +0.002] | +0.002 [-0.002, +0.006] | 0.000 | NOT MET |

| | phase 1 | phase 2 | pooled |
|---|---|---|---|
| primary: svo_angle | K1 MET / K2 NOT MET / K3 NOT MET | K1 NOT MET / K2 NOT MET / K3 NOT MET | K1 MET / K2 NOT MET / K3 NOT MET |

**Reading (nothing new is tested here).**

- **K1** holds on the point estimates in phase 1, pooled and fails in phase 2; it is a weak pass where it holds: M's log-loss gain over the baseline is -0.006 / -0.005 / -0.005 (phase 1 / phase 2 / pooled), every one of those intervals contains 0, and the lower end of M's AUC interval is 0.498 / 0.455 / 0.552, below the 0.55 floor in the phases. The pooled AUC is flattered by the phase mix: the baseline alone, which uses no drive, has pooled AUC 0.563 because the two phases have different base rates, so the pooled K1 floor is partly met by phase membership.
- **K2** fails everywhere on the point estimates: T minus M is -0.025 / +0.005 / -0.029 in AUC. No interval excludes 0 in either direction, so the data do not show composition-as-count to be better, and they do not show it to be worse either; the share of bootstrap draws in which T beats M by more than 0.02 is 0.17 / 0.22 / 0.02.
- **K3** fails everywhere: adding the count to rates changes held-out AUC by -0.018 / -0.004 / -0.009 and log-loss by +0.013 / +0.007 / +0.010; adding the mean changes AUC by -0.001 / -0.001 / -0.001. Person rates alone carry the held-out information (AUC 0.811 / 0.853 / 0.838), and the measured drive adds none that this test can see.

## Secondary (reported, not decisive)

### S1. Risk and agreeableness in place of svo_angle

Same models, same frozen protocol, cuts from the percentile grid. Decision rows as for the primary.

**risk (secondary).** Cuts chosen: phase 1 1, 4; phase 2 1, 2.

| stratum | K1: M AUC [95%] / log-loss M - 0 | K1 | K2: T - M AUC [95%] / log-loss | K2 | K3: (R+T) - R AUC [95%] / log-loss | K3 | (R+M) - R AUC / log-loss |
|---|---|---|---|---|---|---|---|
| phase 1 | 0.627 [0.533, 0.710] / -0.025 | MET | -0.017 [-0.077, +0.041] / +0.001 | NOT MET | +0.002 [-0.002, +0.007] / -0.001 | NOT MET | -0.001 / +0.001 |
| phase 2 | 0.538 [0.452, 0.622] / -0.002 | NOT MET | +0.001 [-0.112, +0.114] / +0.001 | NOT MET | +0.001 [-0.004, +0.007] / -0.002 | NOT MET | -0.000 / -0.000 |
| pooled | 0.627 [0.567, 0.687] / -0.014 | MET | -0.010 [-0.055, +0.036] / +0.001 | NOT MET | +0.001 [-0.002, +0.004] / -0.002 | NOT MET | +0.000 / +0.000 |

| risk (secondary) | K1 MET / K2 NOT MET / K3 NOT MET | K1 NOT MET / K2 NOT MET / K3 NOT MET | K1 MET / K2 NOT MET / K3 NOT MET |

**agreeableness (secondary).** Cuts chosen: phase 1 30, 33; phase 2 34, 39.

| stratum | K1: M AUC [95%] / log-loss M - 0 | K1 | K2: T - M AUC [95%] / log-loss | K2 | K3: (R+T) - R AUC [95%] / log-loss | K3 | (R+M) - R AUC / log-loss |
|---|---|---|---|---|---|---|---|
| phase 1 | 0.533 [0.445, 0.625] / -0.000 | NOT MET | -0.044 [-0.133, +0.044] / +0.006 | NOT MET | -0.004 [-0.009, -0.000] / +0.002 | NOT MET | -0.000 / -0.000 |
| phase 2 | 0.485 [0.396, 0.571] / +0.006 | NOT MET | -0.012 [-0.063, +0.037] / +0.004 | NOT MET | -0.010 [-0.022, +0.002] / +0.004 | NOT MET | -0.007 / +0.001 |
| pooled | 0.567 [0.506, 0.630] / +0.003 | NOT MET | -0.022 [-0.054, +0.011] / +0.005 | NOT MET | -0.005 [-0.012, +0.001] / +0.003 | NOT MET | -0.002 / +0.001 |

| agreeableness (secondary) | K1 NOT MET / K2 NOT MET / K3 NOT MET | K1 NOT MET / K2 NOT MET / K3 NOT MET | K1 NOT MET / K2 NOT MET / K3 NOT MET |

### S2. A dynamic person state (D) against person rates (R)

D = mean over members of the previous-round contribution; the contrast is D minus R, with the same strict AUC margin and log-loss condition (the rule gives D no margin of its own; this is the K3 form, an assumption).

| stratum | test group-rounds | AUC difference [95%] | log-loss difference [95%] | share of draws AUC > +0.02 | criterion |
|---|---|---|---|---|---|
| phase 1 | 174 | -0.001 [-0.074, +0.070] | +0.024 [-0.043, +0.091] | 0.286 | NOT MET |
| phase 2 | 171 | +0.008 [-0.052, +0.071] | -0.015 [-0.109, +0.069] | 0.363 | NOT MET |
| pooled | 345 | +0.001 [-0.044, +0.045] | +0.004 [-0.051, +0.060] | 0.197 | NOT MET |

## Exploratory (nothing here was pre-specified)

- **Does the drive relate to the person's own behaviour?** Correlation, across the persons in the phase's training group-rounds, of svo_angle with the person's training-round mean contribution: phase 1 +0.215, phase 2 +0.174; risk -0.115 / -0.137; agreeableness +0.073 / -0.032.
- **Fit against transfer.** In-training AUC of each model is in the coefficient table; the held-out AUCs are in the stratum tables above. R is flattered in training (its rate contains the outcome being predicted, see the decisions above), so a large gap between its two numbers is expected and is not overfitting of the usual kind.
- **D and the total.** D's RMSE ratio is 0.660 / 0.666 / 0.663 against R's 0.746 / 0.756 / 0.751 (phase 1 / phase 2 / pooled), so the previous round's contributions forecast the continuous total better than the person rates do while the two tie on the binary outcome. Not a criterion; the RMSE difference has no interval here.
- **Two nearby cuts.** Where the rule's literal second-cut step kept two cuts, the two counts together are a count in a band if the cuts are close (phase 1 cuts: 22.45, 25; phase 2: 15, 35), and opposite-signed coefficients in the coefficient table show it; the literal rule keeps a second cut on any in-training log-loss gain, however small (phase 2's gain is 0.0028).
- **Total-contribution outcome.** The RMSE column of each table is y_cont relative to the training mean. The criteria are on the binary outcome only.

## Caveats

- **One group size.** Every group is six. Nothing here tests sensitivity to group size, which is half of what the programme claims; it tests composition at n = 6 only.
- **Reshuffled groups.** Groups are re-formed every round, so a member's rate is estimated across many different compositions, and a group-round is a one-off assembly. This helps the person-effects reading (the rate is a clean person trait) and hurts any model of a stable group state; it also means the same persons recur across group-rounds, so the bootstrap, which treats group-rounds as independent, understates the uncertainty.
- **Norms change across rounds** (the paper's own finding: empirical and normative expectations and contributions move with the disaster probability and with time). A model fitted on rounds 1-10 meets rounds 11-14 under the same probability but a later norm state; the frozen models cannot track that. The outcome frequency falls from 0.82 in round 1 to 0.44 in round 28, so the base rate differs between training and test inside a phase. Order and disaster probability are not in any model.
- **The threshold game favours a count-above-cut form.** A group reaches the threshold when the total passes 300, a threshold on a sum; a count of members above a cut is a natural coarse summary of that sum. T therefore has a structural advantage in this game that it may not have in games without a threshold. A pass on K2 here is weak support for the algebra's claim; a failure is stronger evidence against it than a pass is for it.
- **SVO is one drive among the paper's many measures.** The slider measures preference over own-and-other payoffs; it is not curiosity, fear or desire, and the experiment's main driver (beliefs about what others will do, the empirical and normative expectations) is not used here as a drive. A refutation is of this proxy for this outcome only.
- **R is built to be strong.** The person-effects rival uses the training outcomes themselves; inside training it contains the target. In the test rounds it is a real forecast, and the rule compares only held-out numbers.
- **The rule's margin was fixed after seeing outcome frequencies** (facts above) but before any relation of a drive to an outcome.
- **Measurement.** `svo_angle` is a single administration on day 1; an angle is a continuous summary of a slider task and its cuts (15 to 35 degrees) are the grid of the rule, not natural thresholds (22.45 degrees is the conventional boundary between individualistic and prosocial).
- **Licence and credit.** The article is CC BY 4.0; the OSF project sets no licence, so the data are used as 'available' with attribution and not redistributed. Credit: Szekely et al. 2021 for the experiment and the data; Murphy, Ackermann & Handgraaf (2011) for the SVO slider measure (as named by the paper; not read here). Nothing from the file is reproduced beyond aggregate statistics.

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.szekely_composition rule      # once: writes the data facts and the rule into this file, no model number
    ~/.local/bin/uv run python -m models.szekely_composition report    # fits, freezes, scores once; about a minute
    ~/.local/bin/uv run pytest -q tests/test_szekely_composition.py
