# Apache Incubator: the fitted case. Does first-year growth add out-of-time information about graduation beyond team size?

_Generated 2026-11-01 by `uv run python -m models.apache_fitted_case report` (seed 20261101; 2000 bootstrap draws). Code: `sim/models/apache_fitted_case.py`; checks: `sim/tests/test_apache_fitted_case.py`. Built on `sim/models/apache_activity_survival.py` (loaders, member rule, landmark table, logistic fit, AUC and log-loss are imported, not changed). Data: the Apache Incubator sustainability dataset (CC BY 4.0, doi:10.5281/zenodo.5637530) and the ASF's `podlings.xml`; local-use-only, not in the repo; this file holds counts and statistics only, no name, address or message text._

**What we are trying to achieve (one line).** An algebra of drives, of persons and of groups, composed into an equation set usable to predict or steer outcomes at the membership, group and crowd scales, sensitive to group size, composition and definition (`CLAUDE.md`, 2026-10-29); first outcome activity (2026-11-01). This is the single fitted case on which the team-scale half of that programme continues or stops: `models/00-v0.md` section 8 "Team".

## The rule, written before any fit

Copied verbatim from the brief of 2026-11-01; written into this file before the first number was computed (`report` refuses to run unless this block is already here).

1. Unit: a podling with a recorded outcome (graduated vs retired). Training set: podlings whose incubation STARTED 2003-01-01 to 2012-12-31. Test set: podlings started 2013-01-01 to 2021-12-31. No podling appears in both. Nothing from the test set is looked at until the models are frozen.
2. Features, all computable from the first 12 months of a podling's record only: n = number of regular members (as the existing module defines it, computed on months 0–11); g = prospective first-year growth as in §1.1; start year as a control. Models: (A) size only: logistic on n; (B) size + growth: logistic on n and g; (C) size + growth + start year. Baseline (0): predict the training-set base rate. Fit all on training only; freeze.
3. Score on the test set once: held-out AUC and log-loss for (0), (A), (B), (C); the pre-registered decision criterion is: B beats A on held-out AUC by more than 0.02 AND B's log-loss is lower than A's. Report bootstrap intervals (resample test podlings, 2,000 draws) for the AUC difference B − A; do not re-tune.
4. Secondary (reported, not decisive, clearly labelled): the conversation-concentration lead (development-list messages, automated senders removed, W = 12 months; Gini and top-3 share added to A) scored on the same held-out set with the same frozen protocol; and the same four models with a 6-month feature window.
5. Everything else is exploratory and must be labelled so.

## Decisions the rule left open (taken before any fit)

- **Population.** The module's own landmark table: a resolved podling (graduated or retired by the data end, from the ASF's `podlings.xml`) still in the Incubator at month W (exit month >= W), so that no feature can contain the exit; at least 3 regular members (the module's `min_n`), so that ln n and the shape measures are defined. The podlings dropped by these two conditions are counted below, by set.
- **Features.** n = regular members, active (commits plus human-list messages from non-automated senders) in at least ceil(W/4) of the window's months, at least 2 (3 of 12 at W = 12; 2 of 6 at W = 6); the model takes ln n (the module's size feature). g = ln((events in the window's second half + 1)/(events in its first half + 1)), the halves being months 0-5 and 6-11 at W = 12 and months 0-2 and 3-5 at W = 6; g enters as a number, not as the growth/steady/collapse classes. Start year = the calendar year of the podling's `startdate`.
- **Fit.** The module's ridge logistic regression (`logit_fit`, penalty 1 on inputs standardised on the training set, intercept free), the module's default, not tuned. Frozen means: training mean, standard deviation and coefficients are stored and applied unchanged to the test set. Model C extrapolates the start year beyond the training range (2013-2021 against 2003-2012); that is what the rule asks for.
- **Scoring.** Held-out AUC (`auc_score`, Mann-Whitney, ties one half) and log-loss (`logloss`, probabilities clipped to [1e-6, 1-1e-6]) of the graduation probability, once, on the test set. The baseline's AUC is 0.5 by construction (a constant).
- **Bootstrap.** Resample the test podlings with replacement, 2,000 draws, seed 20261101, models frozen (predictions fixed); a draw with one class only is skipped and counted. 95% percentile intervals. Reported for B - A in AUC and in log-loss and for each model's AUC.
- **Conversation lead (secondary).** Development-list messages (module measure `dev_messages`: every message on a development list that is not commit mail, from a non-automated sender), W = 12; a regular member of THAT measure is active on a development list in at least 3 of the 12 months; Gini (rescaled by n/(n-1)) and top-3 share of the members' totals are added to A's ln n (A's n is the events-based n of the primary). They need at least 3 such members, so the secondary is scored on the podlings that have them, and A is re-fitted and re-scored on that same subset for the comparison; the podlings lost are counted.

**What had been seen before the rule was written (disclosure).** The in-sample work (`results/apache_activity_survival.md`) used all 207 podlings at risk at month 12, including the ones that are now the test set: size AUC 0.758, size + growth 0.768 (a paired edge of +0.010, 95% -0.012 to +0.033), the split by era with the shape results of each, and the conversation lead's era dependence (absent before 2013, present after). The rule, the criterion and the margin of 0.02 were fixed after seeing that, not before it. So the test set is out-of-time but not unseen: its in-sample aggregates were. No model is fitted on the 2013-2021 podlings here. The features of all podlings are built in one table (the module's landmark table), and the split is applied before any fit; no statistic that involves a test podling's outcome (AUC, log-loss, bootstrap) is computed until all models are frozen. The counts of the test set (labels and start dates only) are read first.

## Counts

| set | resolved (graduated / retired) | still incubating at month 12 (graduated / retired) |
|---|---|---|
| training: started 2003-2012 | 153 (116 / 37) | 116 (85 / 31) |
| test: started 2013-2021 | 116 (89 / 27) | 91 (70 / 21) |

(Podlings started outside both ranges, resolved: 0; none is in either set. No podling is in both sets: the sets are disjoint by calendar year of the start.)

Used by the primary analysis (W = 12), after the module's condition of at least 3 regular members in months 0-11:

| set | podlings | graduated / retired | base rate of graduation | dropped for n < 3 |
|---|---|---|---|---|
| training | 110 | 84 / 26 | 0.764 | 6 |
| test | 91 | 70 / 21 | 0.769 | 0 |

## Frozen coefficients (fitted on the training set only)

Inputs are standardised on the training set (mean and standard deviation in the last-but-one column); the coefficients act on the standardised inputs; the raw columns are the same model on the original scale (ln n, g in log-ratio units, calendar year). Logistic, ridge penalty 1 (the module's default, not tuned). Sign: positive goes with graduation.

| model | intercept (standardised) | coefficients on standardised inputs | raw intercept | raw slopes | training mean / sd of inputs | in-training 5-fold CV AUC |
|---|---|---|---|---|---|---|
| A | +1.434 | ln n +1.052 | -2.357 | ln n +1.2280 | ln n 3.088 / 0.857 | 0.755 |
| B | +1.469 | ln n +1.057, g +0.321 | -2.455 | ln n +1.2334, g +0.4365 | ln n 3.088 / 0.857, g 0.265 / 0.734 | 0.755 |
| C | +1.467 | ln n +1.075, g +0.345, start year +0.148 | -126.826 | ln n +1.2546, g +0.4699, start year +0.0619 | ln n 3.088 / 0.857, g 0.265 / 0.734, start year 2008.491 / 2.385 | 0.747 |

## Held-out result (test set, scored once)

Test set: 91 podlings, 70 graduated and 21 retired. Intervals: bootstrap of the test podlings, 2000 draws (0 skipped for one class), models frozen.

| model | held-out AUC [95% bootstrap] | held-out log-loss [95% bootstrap] | mean predicted | in-training AUC |
|---|---|---|---|---|
| baseline: the training-set base rate | 0.500 [0.500, 0.500] | 0.540 [0.437, 0.643] | 0.764 | - |
| A: size only, logistic on ln n | 0.764 [0.650, 0.869] | 0.454 [0.356, 0.555] | 0.774 | 0.767 |
| B: size + growth, logistic on ln n and g | 0.778 [0.677, 0.875] | 0.451 [0.355, 0.553] | 0.755 | 0.779 |
| C: size + growth + start year | 0.775 [0.674, 0.871] | 0.457 [0.336, 0.582] | 0.809 | 0.786 |

**B minus A (the decisive contrast).**

| quantity | point | 95% bootstrap interval | share of draws |
|---|---|---|---|
| AUC, B - A | +0.014 | [-0.033, +0.063] | above 0: 0.741; above 0.02: 0.409 |
| log-loss, B - A | -0.002 | [-0.030, +0.027] | below 0: 0.563 |

## Decision, exactly per the criterion

Criterion (rule item 3): B beats A on held-out AUC by more than 0.02 AND B's log-loss is lower than A's.

**Decision: the criterion is NOT MET.** B's held-out AUC 0.778 against A's 0.764: difference +0.014 (not more than 0.02). B's held-out log-loss 0.451 against A's 0.454: difference -0.002 (lower). The criterion needs both; here only the log-loss condition holds.

For reference only (not part of the criterion): C against A, AUC +0.011, log-loss +0.004; C against B, AUC -0.003, log-loss +0.006.

## Secondary (reported, not decisive)

### S1. The conversation-concentration lead, same frozen protocol

Development-list messages, automated senders removed, W = 12; Gini and top-3 share of the development-list members' totals added to A's ln n. Needs at least 3 regular development-list members, so scored on a subset of the same held-out set: training 109 podlings (84 / 25), test 90 (70 / 20); lost to the extra condition (beyond n >= 3 in events): 7 training and 1 test. A is re-fitted and re-scored on this subset.

| model | intercept (standardised) | coefficients on standardised inputs | raw intercept | raw slopes | training mean / sd of inputs | in-training 5-fold CV AUC |
|---|---|---|---|---|---|---|
| A | +1.456 | ln n +1.000 | -2.196 | ln n +1.1774 | ln n 3.101 / 0.849 | 0.746 |
| A+conv | +1.486 | ln n +1.418, Gini (dev lists) +0.096, top-3 share (dev lists) +0.590 | -6.194 | ln n +1.6699, Gini (dev lists) +0.7136, top-3 share (dev lists) +3.5408 | ln n 3.101 / 0.849, Gini (dev lists) 0.563 / 0.134, top-3 share (dev lists) 0.593 / 0.167 | 0.753 |

| model | held-out AUC [95% bootstrap] | held-out log-loss [95% bootstrap] | mean predicted | in-training AUC |
|---|---|---|---|---|
| baseline: the training-set base rate | 0.500 [0.500, 0.500] | 0.530 [0.436, 0.638] | 0.771 | - |
| A on this subset | 0.752 [0.632, 0.862] | 0.456 [0.358, 0.556] | 0.782 | 0.759 |
| A + Gini + top-3 (development lists) | 0.835 [0.749, 0.911] | 0.434 [0.344, 0.525] | 0.781 | 0.788 |

A+conv minus A: AUC +0.083 [+0.018, +0.152]; log-loss -0.022 [-0.052, +0.008]. Read against the lead's own rule (gain above 0.02 AUC): above 0.02. This is the lead of `results/apache_activity_survival.md` 7.4 on podlings that were part of its in-sample data (the test era 2013-2021 is the era where the lead was present in-sample); it was found in a search of 42 variants and is NOT the confirmation on podlings after July 2021 that that file asks for. The lead's own rule also needs a one-sided permutation p, which is not computed here.

### S2. The same four models with a 6-month feature window

W = 6: features from months 0-5 (n: active in at least 2 of the 6 months; g: months 3-5 against months 0-2). Population: still incubating at month 6 with at least 3 regular members. Training 138 (108 / 30), test 115 (88 / 27); dropped for n < 3: 9 training, 0 test. Resolved podlings still incubating at month 6: training 147, test 115.

| model | intercept (standardised) | coefficients on standardised inputs | raw intercept | raw slopes | training mean / sd of inputs | in-training 5-fold CV AUC |
|---|---|---|---|---|---|---|
| A | +1.684 | ln n +1.328 | -2.629 | ln n +1.4506 | ln n 2.973 / 0.915 | 0.802 |
| B | +1.684 | ln n +1.325, g +0.037 | -2.632 | ln n +1.4473, g +0.0304 | ln n 2.973 / 0.915, g 0.433 / 1.207 | 0.798 |
| C | +1.676 | ln n +1.322, g +0.056, start year +0.112 | -87.304 | ln n +1.4441, g +0.0467, start year +0.0422 | ln n 2.973 / 0.915, g 0.433 / 1.207, start year 2008.326 / 2.660 | 0.790 |

| model | held-out AUC [95% bootstrap] | held-out log-loss [95% bootstrap] | mean predicted | in-training AUC |
|---|---|---|---|---|
| baseline: the training-set base rate | 0.500 [0.500, 0.500] | 0.546 [0.446, 0.646] | 0.783 | - |
| A: size only, logistic on ln n | 0.767 [0.667, 0.856] | 0.473 [0.369, 0.587] | 0.808 | 0.812 |
| B: size + growth, logistic on ln n and g | 0.769 [0.668, 0.858] | 0.472 [0.368, 0.586] | 0.807 | 0.814 |
| C: size + growth + start year | 0.765 [0.664, 0.855] | 0.487 [0.369, 0.618] | 0.843 | 0.813 |

B minus A: AUC +0.002 [-0.005, +0.010]; log-loss -0.001 [-0.004, +0.002].

**The criterion applied to the 6-month window (secondary, not decisive): the criterion is NOT MET.** B's held-out AUC 0.769 against A's 0.767: difference +0.002 (not more than 0.02). B's held-out log-loss 0.472 against A's 0.473: difference -0.001 (lower). The criterion needs both; here only the log-loss condition holds.

## Exploratory (nothing here was pre-specified)

- **Population sensitivity.** The primary drops podlings with fewer than 3 regular members (five of the six in-sample were retired). Re-running A, B, C with those podlings included and ln(1 + n) in place of ln n (the same frozen protocol):

  training 116 (85 / 31), test 91 (70 / 21); held-out AUC A 0.764, B 0.780, C 0.778; log-loss A 0.458, B 0.453, C 0.453; B - A in AUC +0.016 [-0.039, +0.069]. (The criterion read on this population: not met.)
- **Calibration across the eras.** Training base rate of graduation 0.764, test 0.769 (the base rate itself barely moved); mean predicted probability on the test set: A 0.774, B 0.755, C 0.809. C's higher mean comes from extrapolating the start-year slope into 2013-2021.
- **Fit against transfer.** In-training AUC against held-out AUC: A 0.767 against 0.764, B 0.779 against 0.778, C 0.786 against 0.775 (in-training 5-fold CV AUC in the coefficient table). The size signal travelled to 2013-2021 about intact.

## Caveats

- **Size is close to a tautology.** The number of people active in the first year is part of what 'a project that thrives' means; a podling that has not drawn three regular members by month 12 is already, in most senses, failing. Size predicting graduation is the expected result and is no support for any mechanism of the algebra. What the criterion tests is narrower: whether the direction of the first-year trend adds anything out of time.
- **The outcome labels are an institution's.** Graduated is a vote of the Incubator; retired is mostly an administrative closing after a project has gone quiet (L4632: dissolution against success, not a split). Activity is both a symptom and a cause of the label, the exit month's mail is partly about the exit, and the dataset holds only podlings resolved by mid-2021, so the 2013-2021 test set is a closed cohort in which the slowest outcomes are missing.
- **Era drift.** The Incubator's practice, tooling and the places where work is recorded changed between the two periods (more of the discussion in trackers and pull requests); the base rate of graduation is nearly the same in the two periods (see above) but what produces it need not be, the commit file starts in 2005 (nine early podlings have no first-year commits, all in the training period), and model C extrapolates the start year beyond the range on which it was fitted.
- **The test set is small.** 91 podlings, 21 of them retired. A difference of 0.02 in AUC is well inside the sampling noise of one AUC from a sample this size (the interval of B - A above shows how much); the decision is therefore made on a rule that cannot separate small true effects from nothing, and the interval, not the verdict word, is the information. The bootstrap resamples podlings with the models fixed, so it leaves out the variation from re-fitting on another training set.
- **The test era was not unseen** (disclosure above), and the margin 0.02 and the criterion were written knowing the in-sample edge was +0.010.
- **One pseudonym per address, activity not effort, 'regular member' a window choice**: as in `results/apache_activity_survival.md` section 8, unchanged here.
- **A refutation here is of the proxy only.** The dataset records no anchoring, no enemy weight and no tie signs; nothing in this file touches the certificate of `models/00-v0.md` 7.5. What the criterion decides is whether first-year growth, as the measurable of 1.1, carries out-of-time information about exit beyond size on this population.

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.apache_fitted_case rule      # once: writes the rule into this file, no number
    ~/.local/bin/uv run python -m models.apache_fitted_case report    # fits, freezes, scores once; about a minute
    ~/.local/bin/uv run pytest -q

## Review (2026-11-01; reconstructed into this file at the close-out)

_An adversarial review of this file and its code was run on 2026-11-01 at 09:55 UTC by a separate agent (Opus, general-purpose, briefed to "find anything that would make the reported decision wrong", not to rerun the analysis). Its report lived only in the session transcript until the close-out of the same day, when `docs/post-mortem.md` noted the gap and it was copied here from the transcript. The text below is the review's own, lightly re-set; nothing in it was changed. It was not a full rerun: it recomputed the AUC, log-loss and bootstrap from the frozen predictions and read the code against the rule._

**Verdict: the decision stands.** The criterion is NOT MET. Nothing material was found that would flip it or make the reported numbers untrustworthy.

1. **Confirmed: the headline numbers recompute exactly from the frozen predictions**, with an independent pairwise-comparison AUC (ties count one half) and a log-loss written by hand. AUC: A 0.76395, B 0.77823, B−A = +0.0142857, exactly 21/1470 (21 concordant pairs out of 70×21). Log-loss: A 0.45360, B 0.45145. Bootstrap: percentiles of the 2,000 paired draws give [−0.0335, +0.0626], 0 draws skipped; the shares (0.741 above 0, 0.409 above 0.02) agree with the interval. `criterion()` returns False. The rounding fix (`apache_fitted_case.py:115`) only touches a gap of 1e-12, so the direction cannot change.
2. **Confirmed: no leakage.** `Frozen.fit` (`:98-102`) takes mean, sd and coefficients from training rows only; mu and sd re-derived from the training rows agree, and the ridge gradient at the stored beta is about 1e-15. `landmark_table` computes everything per podling, with no threshold pooled across podlings. The only rule that uses more than the window is the relay-bot rule (`apache_activity_survival.py:897-903`): whole-record totals, no labels, flagging 1 pseudonym in total. The population filters (exit ≥ W, n ≥ 3) are the same for both sets and were fixed earlier.
3. **Confirmed: rule before fit, from the transcript, not the repo.** The implementing agent ran `rule` at 09:38:54Z and the first `report` at 09:38:58Z; before that it wrote the module but fitted nothing. `report` was then run twice more (09:39:16, 09:42:05); those edits changed only wording (calibration paragraph, extra honesty caveats) and the rounding fix, not models or features. The repo itself holds no evidence of this order, because `write_report` overwrites the stub; the order rests on the transcript timestamps.
4. **Confirmed: the code applies the stated parameters.** W=12, halves 0-5 / 6-11, MIN_N=3, L2=1.0, SEED=20261101, BOOT=2000. Only W=12 and the 2,000 draws are in the rule itself; the rest are under "decisions the rule left open". The rule says "logistic on n"; the code uses ln n, disclosed.
5. **Plausible wording mismatch with `models/00-v0.md` section 8.** That section's pre-registration says the claim is "refuted… if size + g does not beat size alone", with no margin, and "with the pre-fixed cuts". The code uses continuous g (disclosed). On point estimates B does beat A, so under that looser wording the verdict is ambiguous. Downstream text should cite the 2026-11-01 brief's criterion (gain above 0.02 AUC and lower log-loss) and the interval, not section 8's phrasing.
6. **Confirmed: secondary S1 is labelled correctly.** The +0.083 is marked not decisive and not the post-July-2021 confirmation, and the missing permutation p is noted.
7. **Confirmed: the tests are partly smoke.** Real: the split, the no-test-label test, criterion edge cases, and recomputation of the file's numbers; all 15 pass. Not tested: that `report` refuses without the rule. Self-referential: the "rule verbatim" test, because the report writes the rule block from the same constant.
8. **Confirmed: the results file neither overclaims nor underclaims.** It states the test's low power and the disclosure that the test era's in-sample aggregates had been seen. The test start years actually run 2013-2019, which the closed-cohort caveat covers.

_Comparison with the body above: every number agrees after rounding. The review's lower bound −0.0335 displays here as −0.033. Items 5 and 7 were not in this file before this section._
