# Synthetic population: can known drives be recovered from observables, and do they predict group outcomes?

_Generated 2026-11-01 by `uv run python -m models.synthetic_population report` (seeds 20261101 training, 20261102 held-out, 20261100 calibration of one world constant). Code: `sim/models/synthetic_population.py`; checks: `sim/tests/test_synthetic_population.py`. Built on `sim/models/apache_activity_survival.py` (`logit_fit`, `auc_score`, `logloss` imported, not changed). Everything here is synthetic: no third-party data, no licence question._

**What we are trying to achieve (one line).** An algebra of drives, of persons and of groups, composed into an equation set usable to predict or steer outcomes at the membership, group and crowd scales, sensitive to group size (`CLAUDE.md`, 2026-10-29); first outcome activity (2026-11-01). This experiment asks the identifiability question the real-data tests could not: where drives are KNOWN to generate behaviour, can they be recovered from the observables, and do they predict held-out group outcomes beyond person-level rates?

## The rule, written before any run

Copied verbatim from the brief of 2026-11-01; written into this file before the first number was computed (`report` refuses to run unless this block is already here).

1. World. Persons have a drive vector θ_i = (s_i, a_i, f_i): activity set point s_i ~ N(0,1), affiliation a_i ~ N(0,1), aversion f_i ~ N(0,1), independent, fixed. Groups of size n ∈ {3, 8, 25}. 60 groups per size for training, 30 per size held out, drawn fresh. T = 120 steps per group.
2. Generator (NOT v0's linear coupled form). At each step each person i chooses one action from {act, idle, approach j, avoid j for each j ≠ i} by softmax with temperature 1 over utilities: U(act) = s_i + 0.5·m_{-i}(t−1) where m_{-i} is the others' mean activity last step (1 if they acted else 0); U(idle) = 0; U(approach j) = a_i + 0.8·sim(i,j) − 0.3·r_ij(t−1), U(avoid j) = f_i − 0.8·sim(i,j) + 0.3·r_ij(t−1), where sim(i,j) = −|a_i − a_j| and r_ij(t) is a relationship state updated r_ij ← 0.8·r_ij + 1 on approach, −1 on avoid, decays otherwise. A person leaves the group permanently when their realised utility (the utility of the chosen action, plus Gumbel noise) has been below −1 for 10 consecutive steps. Noise seeds fixed: 20261101 for training worlds, 20261102 for held-out.
3. Observables (all the inference may see): per person per step, whether they acted (0/1); the signed tie events (who approached/avoided whom, when); exit step if any. Drives are never seen by any inference.
4. Inference methods, each fitted on training groups only, frozen, applied to held-out groups: (P) person-effects: per-person activity rate and net approach rate estimated from the first 60 steps; (D) drive recovery: a maximum-likelihood fit of the generator's three per-person parameters from the first 60 steps' observables, with the generator's structure known but the parameters unknown (treat 0.5, 0.8, 0.3 as known constants; estimate θ_i by maximising the softmax likelihood of the observed choices, scipy.optimize per person); (O) oracle: the true θ_i.
5. Outcomes to predict on held-out groups from steps 61–120: (i) group total activity in steps 61–120 (RMSE, relative to predicting the training mean); (ii) whether any member exits in steps 61–120 (AUC and log-loss); (iii) per-person activity in steps 61–120 (RMSE). The predictor for each method is a ridge regression (reuse `logit_fit` for the binary outcome, write a small ridge for continuous) from the method's per-person features aggregated to the group by mean and min, fitted on training groups only, penalty 1, standardised on training.
6. Identifiability measure: Pearson correlation between recovered θ̂_i and true θ_i, per drive, per group size, on held-out persons; also at 30 and 120 steps of observation (secondary).
7. Criteria, decided before the run: (C1) drives are "recoverable at size n" if all three correlations exceed 0.5 at 60 steps; (C2) the drive-based predictor D "beats" P at size n if D's RMSE on (i) is lower by more than 5% of P's AND D's AUC on (ii) exceeds P's by more than 0.02; (C3) D is "near oracle" if D's RMSE on (i) is within 10% of O's. Report all three per size. A failure of C2 where C1 holds means recovered drives carry no extra information about outcomes beyond person rates; a failure of C1 means the drives cannot be recovered from these observables with this much data.
8. Secondary, labelled so: C1 with tie-sign events withheld (activity only), to show which channel carries the drives.

Nothing else is run. No tuning.

## Deviation from the rule

**A defect in the rule, found by working it through before any run, and the one deviation made.** Item 2's exit condition cannot fire. The realised utility of a person is the maximum over their actions of (utility + Gumbel noise). Because idle has utility 0 and is always available, that maximum is below a threshold c with probability exp(-e^(-c) x S) <= exp(-e^(-c)), where S = sum_k e^(U_k) >= 1. At the rule's c = -1 that is at most 0.066 per step, and ten steps in a row is at most 1.6e-12: nobody ever leaves, outcome (ii) has no events at any size, and its AUC is undefined. The calibration table below confirms it (first row). The minimal repair that keeps the rule's form (a streak of 10 steps, the same realised utility, a threshold) is to make the threshold c a property of the world, chosen once, before the training and held-out worlds are drawn, on a third seed (20261100) that no later number uses: 40 groups per size, each c in a fixed grid, and the c that maximises the minimum over the three sizes of min(p, 1 - p), p = the share of groups with at least one exit in steps 60..119 (ties to the smaller c). The training and held-out worlds then run with that c. Nothing else in the rule is altered, and no inference method sees c being chosen. Because S grows with n (more approach and avoid options), a single c cannot make exits equally likely at all sizes; where a size ends with no or all-groups exits, outcome (ii) is reported as undefined there and C2 is then 'not met (AUC undefined)'.

### Calibration of the exit threshold c (seed 20261100, 40 groups per size; share of groups with an exit in steps 60..119 / mean share of persons gone before step 60)

| c | n = 3 | n = 8 | n = 25 | score = min over sizes of min(p, 1 - p) |
|---|---|---|---|---|
| -1.0 (the rule's value) | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 / 0.00 | 0.000 |
| +1.0 | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 / 0.00 | 0.000 |
| +1.5 | 0.00 / 0.00 | 0.00 / 0.00 | 0.00 / 0.00 | 0.000 |
| +2.0 | 0.10 / 0.02 | 0.00 / 0.00 | 0.00 / 0.00 | 0.000 |
| +2.5 | 0.25 / 0.18 | 0.03 / 0.00 | 0.00 / 0.00 | 0.000 |
| +3.0 | 0.47 / 0.44 | 0.17 / 0.02 | 0.00 / 0.00 | 0.000 |
| +3.5 | 0.20 / 0.79 | 0.57 / 0.15 | 0.10 / 0.00 | 0.100 |
| +4.0 | 0.00 / 1.00 | 0.82 / 0.47 | 0.50 / 0.02 | 0.000 |

Chosen: **c = +3.5**. Used for every training and held-out world below.

## Decisions the rule left open (taken before the run)

- **Reading of item 7, C2.** The brief says "lower by more than 5% of P's" without naming the quantity; it is read as 5% of P's RMSE on (i). D beats P when (RMSE_P - RMSE_D) > 0.05 x RMSE_P on outcome (i) AND AUC_D - AUC_P > 0.02 on outcome (ii). Both strict: a difference exactly at a margin is not a pass. C1 is strict (> 0.5). C3 is RMSE_D <= 1.10 x RMSE_O ("within 10%", inclusive).
- **Joint fit per group, not per person in isolation.** A person's utilities for approach/avoid depend on the other members' a_j, which are also unknown. D therefore maximises the softmax likelihood of ALL the group's observed choices over all 3n parameters at once (L-BFGS-B, analytic gradient, one group at a time), which is the per-person likelihood summed over persons with the others' a_j free. Start at 0; box bounds +-6. A weak Gaussian stabiliser N(0, 3^2) on each parameter is added (a ridge, 1/18 per unit squared), because an unpenalised likelihood diverges for a person who never chose some action; the true population is N(0, 1), so the stabiliser is far weaker than the truth and is not tuned.
- **State is computed from the observables.** The relationship state r_ij(t-1) and the others' mean activity m(t-1) are deterministic functions of the observed choices, so D conditions on them exactly (reconstructed in `reconstruct_state`; a test checks it equals the generator's internal state). The exit event itself is not used in the likelihood (the person simply stops contributing after their last step).
- **Choice, noise, presence.** A person chooses by Gumbel-max (identical to softmax at temperature 1); the realised utility is max_k (U_k + G_k), which is the chosen action's utility plus its noise. A person who has left chooses nothing, is not a target of approach/avoid, and is not counted in m. Exit takes effect at the end of the step in which the streak reaches 10; `exit_step` is that step (0-indexed). r_ij is directional (i's state towards j) and changes only by i's own approach/avoid of j.
- **Features.** P: per person, acts / steps present, and (approaches - avoids) / steps present, over steps 0..59 while present. D: (s-hat, a-hat, f-hat). O: the true (s, a, f). Group features: mean and min across all the group's members (including those who left before step 60, whose features come from the steps they were present). One model per group size.
- **Outcomes.** (i) total acts by all members in steps 60..119 (0-indexed; "61-120"); (ii) any exit with exit_step in 60..119; (iii) per person present at step 60: acts / steps present in steps 60..119. For (iii) the regressors are the person's OWN features plus the group mean and min (group aggregates alone cannot separate members of a group); persons absent at step 60 have no outcome. RMSE is relative to predicting the training-set mean (baseline); a binary outcome with a single class in training predicts the training base rate and the AUC is reported where defined.
- **Ridge.** Continuous: centre y, standardise X on training, minimise |y - Xb|^2 + 1 x |b|^2 (intercept free). Binary: `apache_activity_survival.logit_fit`, penalty 1, on the same standardisation. Frozen: mean, sd and coefficients stored from training, applied unchanged to held-out.
- **Secondary, activity only.** Ties withheld means the observable is only whether each person acted (act vs not-act), plus the others' activity m. The tie state r is then unobservable and is taken as 0 in the likelihood (a misspecification: the generator has r != 0), and the likelihood is of act versus not-act, where the not-act probability sums idle, approach and avoid. Run at 60 steps on the held-out groups. Also at 30 and 120 steps with ties (item 6).
- **Correlations** are pooled over all held-out persons of a size (30 groups x n persons), recovered against true, at each window; persons who left early are included with the steps they were present.
- **Compute.** The group-level fits are independent and run in a process pool (up to 8 workers). Seeds: each group has its own stream, default_rng([seed, n, group index]); the world's drives and noise both come from that stream, so a training and a held-out group can never share a person.

## Counts

| size | training groups / persons | held-out groups / persons | groups with an exit in steps 60..119, training / held-out | persons present at step 60 (outcome iii), training / held-out | mean total acts in steps 60..119, held-out |
|---|---|---|---|---|---|
| 3 | 60 / 180 | 30 / 90 | 15 of 60 / 7 of 30 | 45 / 26 | 10.2 |
| 8 | 60 / 480 | 30 / 240 | 26 of 60 / 15 of 30 | 416 / 206 | 26.4 |
| 25 | 60 / 1500 | 30 / 750 | 4 of 60 / 3 of 30 | 1496 / 748 | 36.7 |

## C1. Recovery of the drives (correlation of recovered with true, held-out persons, 60 steps)

| size | corr(s-hat, s) | corr(a-hat, a) | corr(f-hat, f) | C1 (all three > 0.5) |
|---|---|---|---|---|
| 3 | 0.828 | 0.750 | 0.766 | MET |
| 8 | 0.656 | 0.804 | 0.879 | MET |
| 25 | 0.608 | 0.931 | 0.856 | MET |

### Secondary: observation length (ties observed) and the channel (activity only, 60 steps)

| size | window | corr s | corr a | corr f | C1 |
|---|---|---|---|---|---|
| 3 | 30 steps, ties | 0.800 | 0.723 | 0.718 | MET |
| 3 | 60 steps, ties | 0.828 | 0.750 | 0.766 | MET |
| 3 | 120 steps, ties | 0.831 | 0.753 | 0.764 | MET |
| 3 | 60 steps, activity only (ties withheld) | 0.741 | 0.087 | 0.271 | NOT MET |
| 8 | 30 steps, ties | 0.612 | 0.781 | 0.839 | MET |
| 8 | 60 steps, ties | 0.656 | 0.804 | 0.879 | MET |
| 8 | 120 steps, ties | 0.743 | 0.889 | 0.919 | MET |
| 8 | 60 steps, activity only (ties withheld) | 0.544 | 0.167 | 0.500 | NOT MET |
| 25 | 30 steps, ties | 0.516 | 0.885 | 0.796 | MET |
| 25 | 60 steps, ties | 0.608 | 0.931 | 0.856 | MET |
| 25 | 120 steps, ties | 0.715 | 0.950 | 0.910 | MET |
| 25 | 60 steps, activity only (ties withheld) | 0.559 | 0.033 | 0.431 | NOT MET |

## Outcomes on the held-out groups (steps 60..119), ridge predictors fitted on the training groups

RMSE is in the outcome's own units; 'rel' is RMSE divided by the RMSE of predicting the training mean (below 1 is better than the mean). AUC and log-loss are for 'any member exits'; the baseline log-loss predicts the training base rate.

| size | method | (i) group total activity: RMSE [rel] | (ii) any exit: AUC | (ii) log-loss | (iii) per-person activity: RMSE [rel] |
|---|---|---|---|---|---|
| 3 | baseline (training mean / base rate) | 15.250 [1.000] | 0.500 | 0.544 | 0.2890 [1.000] |
| 3 | P person effects | 16.126 [1.057] | 0.596 | 0.537 | 0.1776 [0.614] |
| 3 | D drive recovery | 14.729 [0.966] | 0.571 | 0.549 | 0.1657 [0.573] |
| 3 | O oracle | 15.178 [0.995] | 0.497 | 0.678 | 0.1267 [0.438] |
| 8 | baseline (training mean / base rate) | 11.472 [1.000] | 0.500 | 0.702 | 0.0854 [1.000] |
| 8 | P person effects | 9.636 [0.840] | 0.653 | 0.679 | 0.0536 [0.628] |
| 8 | D drive recovery | 9.110 [0.794] | 0.644 | 0.849 | 0.0659 [0.772] |
| 8 | O oracle | 8.501 [0.741] | 0.751 | 0.601 | 0.0578 [0.676] |
| 25 | baseline (training mean / base rate) | 18.747 [1.000] | 0.500 | 0.333 | 0.0466 [1.000] |
| 25 | P person effects | 7.301 [0.389] | 0.457 | 0.514 | 0.0249 [0.534] |
| 25 | D drive recovery | 14.973 [0.799] | 0.617 | 0.350 | 0.0384 [0.825] |
| 25 | O oracle | 12.513 [0.667] | 0.728 | 0.302 | 0.0347 [0.744] |

## Decision, exactly per the criteria

| size | C1 recoverable | C2 D beats P | C3 D near oracle | reading |
|---|---|---|---|---|
| 3 | MET | NOT MET | MET | C1 holds, C2 fails (D's AUC on (ii) does not exceed P's by more than 0.02): by the rule's own reading, recovered drives carry no extra information about these outcomes beyond person rates, subject to the caveats on the aggregation and on the small counts. RMSE gap (P - D)/P = +0.087 (needs > 0.05); AUC gap D - P = -0.025 (needs > 0.02). D/O RMSE on (i) = 0.970 (needs <= 1.10). |
| 8 | MET | NOT MET | MET | C1 holds, C2 fails (D's AUC on (ii) does not exceed P's by more than 0.02): by the rule's own reading, recovered drives carry no extra information about these outcomes beyond person rates, subject to the caveats on the aggregation and on the small counts. RMSE gap (P - D)/P = +0.055 (needs > 0.05); AUC gap D - P = -0.009 (needs > 0.02). D/O RMSE on (i) = 1.072 (needs <= 1.10). |
| 25 | MET | NOT MET | NOT MET | C1 holds, C2 fails (D's RMSE on (i) is not lower than P's by more than 5% (it is higher)): by the rule's own reading, recovered drives carry no extra information about these outcomes beyond person rates, subject to the caveats on the aggregation and on the small counts. RMSE gap (P - D)/P = -1.051 (needs > 0.05); AUC gap D - P = 0.160 (needs > 0.02). D/O RMSE on (i) = 1.197 (needs <= 1.10). |

## Caveats

- **This is a synthetic world of our own design.** The generator is a softmax choice model with a relationship state, written for this test; nothing says people, or any real group, behave like it. A result here is about identifiability in a world where the answer is known, not about people.
- **The generator's structure is given to method D.** D knows the utility form, the three constants (0.5, 0.8, 0.3), the choice set and the exit-free likelihood; only the drive values are unknown. This is a best case for D: a real analyst does not know the structure, and a misspecified drive model would recover less. A failure of C1 here is therefore strong; a success is the most that could be hoped for, not evidence for real data.
- **The drives are the generator's primitives by construction.** That drives exist in this world is not a finding; what is tested is whether they can be recovered from the observables at 60 steps, at three group sizes, and whether recovering them adds anything about held-out outcomes beyond per-person rates, which are themselves almost sufficient statistics for a person whose behaviour is a function of three fixed numbers.
- **The exit condition needed a repair** (see Deviation): the threshold was chosen on a third seed to make exits possible; at some sizes exits remain rare or universal, and outcome (ii) is then weak or undefined there. Exit depends on the number of options (larger groups have more of them), which is a property of this generator, not of groups.
- **The aggregation is a poor match to this generator.** Group features are the mean and min of per-person values and the regression is linear in them, but the group's total activity is a sum of softmax probabilities e^s/Z_i, nonlinear in the drives, with Z_i growing with the number of options. Per-person act rates measure that directly, so P has a built-in advantage on (i) that the drives must overcome through a linear map; the oracle O, which has the true drives, does not beat the baseline by much at n = 3 and is far from perfect at n = 25 for the same reason. A C2 failure here is therefore partly a failure of the rule's prescribed predictor form, not only of the drives' information. This was not tuned.
- **The chosen exit threshold gives a degenerate small world.** The calibration score at the chosen c was only 0.10 (no c in the grid made exits moderately likely at every size). At n = 3 most members have gone before step 60 (see the calibration row), so the held-out n = 3 outcomes rest on few remaining persons and low activity; at n = 25 only a handful of groups have an exit in the outcome window, so AUC (ii) there rests on a handful of events.
- **Small held-out sets.** 30 groups per size: 30 group-level outcomes for (i) and (ii) at each size. AUC on a handful of exit events is very noisy; no intervals are computed (the rule asked for none), so a gap near a margin is not distinguishable from nothing.
- **Group aggregates by mean and min** lose which member is which; the (iii) regression adds the person's own features to the aggregates, a decision of this file (see Decisions). Different aggregates could change C2.
- **Activity-only secondary is misspecified on purpose of the withholding:** r cannot be observed without ties and is set to 0 in that likelihood; part of any shortfall there is that misspecification, not only the missing channel.
- **One run, no tuning.** The tests exercise machinery on small worlds; the numbers above are the single run.

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.synthetic_population rule      # once: writes the rule into this file, no number
    ~/.local/bin/uv run python -m models.synthetic_population report    # the single run; writes this file
    ~/.local/bin/uv run pytest -q tests/test_synthetic_population.py
