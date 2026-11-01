# The crowd gate on wiki-RfA, 2003-2013: complements or substitutes, cascade, ignition, two-sided gate

_Generated 2026-11-01 by `cd sim && ~/.local/bin/uv run python -m models.crowd_gate_wikirfa report` (seed 20261101; 400 within-election shuffles for the main null, 100 for each robustness variant, 12 for the form comparison, 150 for the hazard terms). Code: `sim/models/crowd_gate_wikirfa.py`; checks: `sim/tests/test_crowd_gate_wikirfa.py`. Ledger ids (grep `docs/ledger.jsonl`): the crowd law L1831, L1201, L1235, L1225; thresholds L3959, L3965, L3967, L4395; the Hong Kong march L4353-L4355, scope L4363, upper-gate mechanisms L4347, L4348; the data L4561-L4564. Results are computed statistics only; the data file is local-use-only and is not redistributed (`sim/data/README.md`)._

**What was tested.** `models/00-v0.md` §4.4 writes the crowd law as r(t+1) = F[r(t)] with a two-sided gate (a person joins iff theta_i <= r <= thetabar_i) and carries the sign of "more of the crowd acting makes me more likely to act" as a setting operand sigma (the Hong Kong march found substitutes at its margin, L4355, and its authors say the sign may flip with turnout, L4363). Each adminship election on Wikipedia is a crowd event: signed public votes with minute timestamps, in a medium that shows the running tally. This file estimates sigma there, tests the participation curves for the monotone-cascade shape (Theorem 6.3), for ignition and for an upper gate, and compares the forms of the law out of sample.

## Verdict

**In short.**

- *sigma, the sign of a vote's co-movement with the crowd just before it, is positive and nowhere robustly negative.* The share of the previous 10 votes enters P(support) with logit coefficient 1.44 against a shuffle null of -0.01 (z +16.1), with z >= 2 in 9 of the 9 years from 2005 on (2004 has 67 elections and no power) and in 4 of the 4 size classes; the same holds for the previous 5 and 20, in an election-fixed-effect model, and in the agreement of a vote with the majority of the last 5 to 10 votes (2.2). A net negative association (substitutes as co-movement) is refuted at this scale. This is an association: whether a negative causal response sits under a stronger shared shock is not decided by these data (the third point).
- *The cumulative running share, the state variable the law names, carries little of it.* Out of sample, on votes with at least 20 earlier votes (where the cumulative share and a short window differ), the cumulative share adds +0.03 log-likelihood per 1000 votes in its linear (Kuran) form and +1.25 as a spline (z +5.4) beyond the controls once the mechanical gain (the same form fitted to shuffled elections) is subtracted; the last-10-vote share adds +3.27. The sign of the cumulative coefficient depends on the sample and the estimator: +0.85 at five or more earlier votes (z +7.9 against the shuffle), +1.69 and +1.54 below 20 earlier votes (where the cumulative share is itself a short window), -1.26 and -5.47 above 40 in the same logit, but above its shuffle null at every turnout once an election-specific trend is removed (the detrended coefficients and their nulls are both negative; the excess is positive). Read literally, a later vote has the sign of the majority of the *last 5* votes +1.1 points more often than random order gives (z +18.0; last 10: +0.6, z +17.7; +3.1 points when the previous vote came within 20 minutes) and the sign of the *cumulative majority* -0.4 points (z -22.3). The cumulative sign is therefore **not identified here** (non-stationary elections), and the law's state variable, if it is a crowd share, is a short-memory one.
- *Whether the local dependence is influence or a shared shock is not decided, and the usual placebo cannot decide it.* The dependence on the next 10 votes (1.63) is about as strong as on the previous 10 (1.44; the fixed-effect model puts them the other way round, 0.154 against 0.165); on planted data a forward-influence world looks the same (tested), so time-symmetry is reported as time-symmetry. The gap profile shows the excess agreement of consecutive votes peaks at 2-5 minutes (+6.1 points) and is gone after about four hours; votes saved in the same minute agree *less* than chance (-8.0 points, z -6.2), which neither planted model produces and which is left unexplained.
- *Participation (Theorem 6.3's object): a monotone, decelerating curve, no ignition tied to the state, and a one-sided gate.* Pooled, 47% of an election's votes arrive in the first 24 hours; the dominant shape (decelerating, with or without an end bump, 87% of elections) is one a common clock produces 98% of the time, so the shape does not discriminate; the spread of the first-day share across elections is 5.1 times the clock's, and 13% of elections have shapes the clock rarely makes (2.0%). The late rise in the contested band is no larger than composition predicts (contested minus decisive +0.22 against +0.30 under the shuffle, z -2.7); one band departs the other way: elections with a running share of .85-.95 at hour 120 rise more in the last 12 hours than the shuffle gives (ratio 1.24 against 1.13, z +5.8), so the late rise is not purely clock and composition, but it is not the law's ignition (a surge in contested states). Participation falls when the running tally is against the candidate, already in the first 24 hours, before almost any early closure (bands below 50% and 50-70%: -0.21 and -0.09 log-points against the path-free null), and more over the week (-0.31 and -0.18, which includes elections the rule had closed); it is flat once support passes about 70%, and the bands above 85% do not fall. **No upper gate at decisive success shows in the path of the running share; failure closes the process** (no vote after 72 h: 70% of elections ending below 40% support, 32% at 40-60%, 0.2% at 90% or more; 397 of the 402 elections silent after 72 h failed).
- *Best-fitting forms, out of sample, mechanical gain removed.* Sign: the share of the last 10 votes (+3.27 per 1000 votes, SE 0.37); the cumulative forms gain much less (linear +0.03, curvature +0.46, spline +1.25, step at 50% +0.62, margin -0.01), and the log-odds form less than its own mechanical gain (-0.97). Participation: a saturating share term (concave, negative curvature) ranks first in 2 of 3 windows, by margins inside the standard errors; the convex (Kuran) curvature is never supported.

**Status of the claims about the crowd law's sign in this medium and era.**

- *Refuted:* a net negative association (substitutes as co-movement) for the vote's sign at the local scale; an upper gate on participation at decisive success in the form this design can see, a fall of arrivals with the running share's path over and above the election's final composition: the bands above 85% sit at or above their null (over 1-168 h within 0.01 log-points; over 24-168 h +0.06 and +0.10, z +4.0 and +5.7). A gate that acts through the final composition is absorbed by the composition control and is not tested.
- *Supported:* positive local co-movement of signs (sigma > 0 as an association), short-memory, strongest within an hour, in every year from 2005 and every size class; a one-sided, saturating dependence of participation on the running support share (a fall below 70%, present in the first day; flat above); a stall (closure) that attaches to failure and rises as final support falls (397 of the 402 elections silent after 72 h failed).
- *Not found:* state-triggered late acceleration (ignition): the contested band's late rise is no larger than composition alone predicts (the .85-.95 band's is larger, z +5.8: not where ignition would show); 3.5% of elections do have a mid-phase surge the clock cannot make, and whether the state triggers those is untested. A convex (Kuran: accelerating) curvature of participation in the running share: the raw curvature is negative in every window, and so is its excess over the shuffle null (1-24 h -0.09 (z -1.2), 24-168 h -0.04 (z -0.2), 1-168 h -0.25 (z -3.0)), beyond the null only over 1-168 h.
- *Undecided:* influence against shared shock as the source of the co-movement; the sign of the dependence on the cumulative share at 40 or more earlier votes; whether the monotone cascade orbit is the process behind the participation curve (the curve's shape is what attention decay also produces).

## 1. Data, terms, cleaning

- **Source and terms.** SNAP `wiki-RfA.txt.gz` (West, Paskov, Leskovec & Potts 2014, TACL 2: 297-310, doi:10.1162/tacl_a_00184), the local copy under `sim/data/wiki-rfa/`: 14,936,383 bytes, sha256 `88d53196fb2564a2e20286dbba818832f718cc352bb181a2101d23d2556f0862`. SNAP states no terms; the comments are Wikipedia text (CC BY-SA) and are never parsed, stored or used here (the parser discards every TXT line); user names become integers on load and are never written out. Nothing from the file is committed.
- **Counts reproduce 117.** 198,275 votes: 144,451 support, 41,176 oppose, 12,648 neutral (L4562); per-year totals are tested in the suite (L4563).
- **Cleaning.** 188,907 votes carry a timestamp. Dropped: 9,368 undated (9,367 empty fields and one impossible hour), 1,661 with no voter, 88 self-votes, 30 stray timestamps (a cluster of at most 3 votes beside a cluster of at least 10), 396 repeat votes by one voter in one election (the last stands). An *election* is one (candidate, result, year) group split at silences over 10 days (3,926 groups became 4,062 elections: a candidate can fail twice in a year). 188,393 votes remain.
- **Sign sample.** Non-neutral votes of the 2,493 elections with at least 20 of them: 162,733 votes (81.4% support); targets are votes with at least 5 earlier non-neutral votes (150,218). **Participation sample.** All votes (neutral too) of the 2,595 elections with at least 20 dated votes: 174,705 votes.

Elections and votes in the sign sample, by year and by size class (non-neutral votes per election):

| year | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 |
|---|---|---|---|---|---|---|---|---|---|---|
| elections | 67 | 321 | 599 | 597 | 355 | 225 | 142 | 89 | 68 | 30 |
| votes | 1,820 | 12,817 | 37,916 | 36,092 | 26,374 | 18,960 | 12,126 | 7,589 | 5,756 | 3,283 |

| size class | 20-39 | 40-79 | 80-159 | 160+ |
|---|---|---|---|---|
| elections | 693 | 1086 | 647 | 67 |
| votes | 20,058 | 62,571 | 67,204 | 12,900 |

## 2. Part 1: does a later vote follow the running crowd?

**The estimator.** For every target vote: the running support share s and the running turnout n of the votes strictly before it (votes in the same minute do not see each other). Logit of P(support) on s with the voter's propensity (his support rate at his OTHER (candidate, result, year) groups, shrunk with 4 pseudo-votes at the pooled rate, plus a first-timer flag and log experience), the election's leave-one-out support share and its result (the candidate's final outcome), log turnout and the clock (hour bins, position in the election). Standard errors are clustered by election.

**The null.** The same votes (signs, voters, composition) reassigned at random to the election's own timestamps, 400 times, the whole pipeline re-run each time. It reproduces every mechanical artefact of the estimator (sampling without replacement, the leave-one-out bias, the controls) so only order-dependence is left. The controls ladder shows why this matters: the raw coefficient is 6.0 and the shuffle alone gives 5.8.

**Controls ladder** (coefficient on the running share, all targets; null from 100 shuffles):

| controls | coefficient | null mean (sd) | z |
|---|---|---|---|
| clock and turnout only | 6.01 | 5.83 (0.03) | +6.5 |
| + voter propensity | 6.27 | 6.09 (0.03) | +5.5 |
| + candidate outcome (no propensity) | 0.86 | 0.01 (0.09) | +9.4 |
| + both (the primary specification) | 0.85 | 0.01 (0.11) | +7.5 |

The candidate's outcome is the confounder (a good candidate has a high running share and later supporters); the voter's propensity moves nothing. What the outcome control costs: under herding the final composition is itself an outcome of the early votes, and conditioning on it makes the test conservative for complements (tested on planted data).

### 2.1 Primary result, by year and by election size

| cell | elections | votes | P(sup) | logit coef (se) | AME +10 pts (pp) | shuffle null (sd) | z | p (>= obs) | FE-LPM coef (se) | FE null | FE z |
|---|---|---|---|---|---|---|---|---|---|---|---|
| all | 2493 | 150,218 | 0.81 | 0.85 (0.10) | +0.76 (0.09) | -0.00 (0.11) | +7.9 | <= 0.0025 | 0.28 (0.03) | -0.70 | +32.0 |
| 2004 | 67 | 1,484 | 0.88 | 0.61 (0.86) | +0.45 (0.64) | +0.11 (1.18) | +0.4 | 0.304 | -0.80 (0.31) | -1.19 | +1.2 |
| 2005 | 321 | 11,210 | 0.89 | 1.02 (0.51) | +0.61 (0.31) | -0.03 (0.50) | +2.1 | 0.007 | -0.04 (0.15) | -0.89 | +7.4 |
| 2006 | 599 | 34,909 | 0.81 | 0.84 (0.21) | +0.72 (0.18) | -0.01 (0.20) | +4.2 | <= 0.0025 | 0.24 (0.06) | -0.74 | +14.7 |
| 2007 | 597 | 33,096 | 0.83 | 0.82 (0.19) | +0.67 (0.16) | +0.01 (0.25) | +3.3 | <= 0.0025 | 0.36 (0.06) | -0.73 | +16.0 |
| 2008 | 355 | 24,588 | 0.79 | 0.99 (0.21) | +0.99 (0.21) | -0.00 (0.25) | +3.9 | <= 0.0025 | 0.31 (0.07) | -0.67 | +13.3 |
| 2009 | 225 | 17,824 | 0.77 | 0.97 (0.23) | +1.04 (0.25) | -0.04 (0.27) | +3.7 | <= 0.0025 | 0.23 (0.08) | -0.64 | +9.7 |
| 2010 | 142 | 11,415 | 0.79 | 0.12 (0.31) | +0.12 (0.29) | -0.03 (0.41) | +0.4 | 0.362 | 0.16 (0.08) | -0.68 | +7.4 |
| 2011 | 89 | 7,143 | 0.83 | 1.33 (0.40) | +1.14 (0.34) | -0.04 (0.53) | +2.6 | <= 0.0025 | 0.30 (0.16) | -0.71 | +6.6 |
| 2012 | 68 | 5,416 | 0.75 | 1.11 (0.45) | +1.17 (0.47) | -0.03 (0.49) | +2.3 | <= 0.0025 | 0.44 (0.15) | -0.67 | +7.3 |
| 2013 | 30 | 3,133 | 0.81 | 2.13 (1.07) | +2.09 (1.06) | -0.22 (0.93) | +2.5 | <= 0.0025 | 0.48 (0.30) | -0.68 | +4.9 |
| size 20-39 | 693 | 16,587 | 0.63 | 0.28 (0.15) | +0.30 (0.16) | +0.03 (0.20) | +1.3 | 0.105 | -0.29 (0.06) | -1.01 | +10.1 |
| size 40-79 | 1086 | 57,124 | 0.82 | 0.85 (0.13) | +0.73 (0.11) | -0.01 (0.16) | +5.3 | <= 0.0025 | 0.23 (0.04) | -0.72 | +19.7 |
| size 80-159 | 647 | 63,949 | 0.85 | 1.43 (0.23) | +1.20 (0.19) | -0.02 (0.23) | +6.2 | <= 0.0025 | 0.53 (0.05) | -0.55 | +21.7 |
| size 160+ | 67 | 12,558 | 0.81 | 0.77 (0.62) | +0.87 (0.70) | -0.11 (0.58) | +1.5 | 0.062 | 0.66 (0.12) | -0.47 | +8.5 |

Reading: the coefficient is positive in every year and every size class; 8 years reach p <= 0.01 (one-sided, in the direction of complements), and 7 pass a Bonferroni bar for the 15 cells (p <= 0.0033; the smallest attainable p is 0.0025). The fixed-effect model's null is far below zero (an election fixed effect contains the vote's own sign), so only the z against it is read. Overall AME: +0.76 points of P(support) per +10 points of running share.

### 2.2 Other estimators of the same quantity (all targets)

| estimator | observed | shuffle null (sd) | z | p (>= obs) |
|---|---|---|---|---|
| logit, primary | 0.848 | -0.005 (0.108) | +7.9 | <= 0.0025 |
| logit, elections weighted equally | 0.675 | 0.003 (0.107) | +6.3 | <= 0.0025 |
| linear, election fixed effects | 0.280 | -0.700 (0.031) | +32.0 | <= 0.0025 |
| linear, election-specific quadratic trend removed | -2.293 | -2.628 (0.056) | +6.0 | <= 0.0025 |
| linear, voter fixed effects + composition controls | 0.348 | 0.000 (0.013) | +26.7 | <= 0.0025 |
| agreement with the cumulative majority (>= 5 earlier votes) | 0.838 | 0.842 (0.000) | -20.1 | 1.000 |

The first five agree on the sign of the excess over their own nulls (the detrended coefficient is negative, but less so than its null). The last is the literal reading of "follows the running majority" with the *cumulative* majority: agreement is slightly *below* what random order gives. That statistic has no power against complements in a cumulative world (planted data) and picks up non-stationarity: real elections open with a run of supports and drift, so the early majority is a poorer guide to later votes than a random sample would be.

**Agreement with the majority before the vote** (targets with at least 5 earlier votes; a strict majority needed; excess in percentage points over random order). *Fast* = the previous vote was at most 20 minutes earlier, *slow* = longer:

| majority of | agreement | random order (sd) | excess (points) | z | fast: excess (z) | slow: excess (z) |
|---|---|---|---|---|---|---|
| all earlier votes | 0.8383 | 0.8419 (0.0002) | -0.37 | -22.3 | +1.12 (+8.7) | -1.00 (-18.4) |
| last 20 votes | 0.8469 | 0.8438 (0.0003) | +0.31 | +11.0 | +1.86 (+14.2) | -0.36 (-5.7) |
| last 10 votes | 0.8532 | 0.8467 (0.0004) | +0.65 | +17.7 | +2.29 (+17.0) | -0.06 (-1.0) |
| last 5 votes | 0.8316 | 0.8210 (0.0006) | +1.06 | +18.0 | +3.11 (+19.8) | +0.18 (+2.2) |

The answer to the literal question is two-sided. Votes follow the majority of the last 5 to 10 votes more often than random order gives, almost entirely when votes are arriving within minutes of each other; they do not follow the cumulative majority (below random order in every year, points: 2005 -0.5, 2006 -0.5, 2007 -0.4, 2008 -0.3, 2009 -0.4, 2010 -0.3, 2011 -0.3, 2012 -0.4, 2013 -0.2). The recent-majority excess is positive in every size class (20-39 +0.7, 40-79 +0.6, 80-159 +0.7, 160+ +0.7 points for the last 10) and in every year from 2006 (2006 +0.5, 2007 +0.8, 2008 +0.8, 2009 +0.9, 2010 +0.5, 2011 +0.6, 2012 +1.3, 2013 +0.7).

### 2.3 By running turnout (the sign can flip with turnout, L4363)

| earlier votes | logit coef | null (sd) | z | detrended FE coef | null (sd) | z |
|---|---|---|---|---|---|---|
| 5-9 | +1.69 | -0.01 (0.18) | +9.5 | -1.64 | -1.83 (0.07) | +2.8 |
| 10-19 | +1.54 | -0.02 (0.23) | +6.7 | -2.58 | -2.84 (0.07) | +3.6 |
| 20-39 | +0.34 | -0.01 (0.29) | +1.2 | -2.63 | -3.17 (0.10) | +5.5 |
| 40-79 | -1.26 | -0.00 (0.49) | -2.6 | -2.90 | -3.59 (0.14) | +5.0 |
| 80+ | -5.47 | +0.17 (1.20) | -4.7 | -2.10 | -3.15 (0.25) | +4.1 |

Read against their own nulls, the two estimators agree below 20 earlier votes (both above the null) and disagree above 40: the logit falls below its null, the detrended model stays above its null (its coefficients are negative, its null more so). Both are calibrated against their own shuffle null, and the disagreement is a statement about what each assumes of the election's trend, so the sign of the cumulative dependence at high turnout is **undecided**. A stricter minimum number of earlier votes moves the primary coefficient the same way (2.5).

### 2.4 The local dependence, and the time-reversal placebo that does not discriminate

| window L | logit: previous L votes (z) | logit: next L votes (z) | FE: previous L (z) | FE: next L (z) |
|---|---|---|---|---|
| 5 | 1.09 (+20.1) | 1.12 (+20.6) | +0.139 (+26.5) | +0.128 (+25.2) |
| 10 | 1.44 (+16.1) | 1.63 (+17.5) | +0.165 (+22.6) | +0.154 (+21.4) |
| 20 | 1.77 (+10.1) | 2.27 (+12.9) | +0.175 (+16.4) | +0.150 (+15.4) |

Entered together, the share of the previous L and the next L votes both carry the dependence, at every L, in the logit and in the fixed-effect model. If earlier votes caused later ones, the previous window should dominate; it does not. **That is a weaker conclusion than it looks**: on planted data (suite) a stationary chain in which each vote follows its five predecessors also gives equal coefficients on both windows -- a reversible process looks the same run backwards -- exactly as a shared shock does. The placebo shows the dependence is about equally strong in both directions (the logit puts the next window a little ahead, the fixed-effect model the previous one); it neither supports nor refutes influence.

**The local dependence by year and by size** (previous 10 and next 10 votes entered together; logit coefficients with the primary controls, 200 shuffles, so the z of the first row differs a little from the table above, which uses 400):

| cell | targets | previous 10 (se) | null | z | next 10 (se) | z |
|---|---|---|---|---|---|---|
| all | 112,850 | 1.44 (0.07) | -0.00 | +15.3 | 1.63 (0.07) | +17.8 |
| 2004 | 480 | -0.01 (1.77) | -0.99 | +0.5 | 1.10 (1.17) | +1.0 |
| 2005 | 6,394 | 1.76 (0.37) | -0.22 | +3.2 | 1.73 (0.39) | +3.2 |
| 2006 | 25,932 | 1.47 (0.13) | -0.01 | +6.9 | 1.85 (0.14) | +8.6 |
| 2007 | 24,149 | 1.40 (0.14) | -0.03 | +7.2 | 1.62 (0.14) | +7.9 |
| 2008 | 19,267 | 1.33 (0.16) | -0.04 | +6.8 | 1.40 (0.18) | +7.5 |
| 2009 | 14,455 | 1.30 (0.22) | -0.03 | +6.1 | 1.43 (0.22) | +6.5 |
| 2010 | 9,285 | 1.28 (0.22) | -0.09 | +3.9 | 1.58 (0.22) | +4.8 |
| 2011 | 5,809 | 2.02 (0.27) | -0.15 | +4.8 | 1.49 (0.29) | +3.8 |
| 2012 | 4,396 | 1.64 (0.21) | -0.16 | +4.0 | 1.44 (0.28) | +3.4 |
| 2013 | 2,683 | 1.20 (0.51) | -0.32 | +2.2 | 1.57 (0.37) | +2.6 |
| size 20-39 | 6,191 | 1.21 (0.31) | -0.06 | +3.4 | 1.43 (0.33) | +3.9 |
| size 40-79 | 40,844 | 1.51 (0.11) | -0.02 | +9.4 | 1.62 (0.12) | +10.8 |
| size 80-159 | 54,258 | 1.56 (0.10) | -0.01 | +12.3 | 1.72 (0.09) | +13.0 |
| size 160+ | 11,557 | 1.05 (0.21) | -0.05 | +4.9 | 1.18 (0.23) | +5.4 |

Positive in both directions in 13 of the 13 cells from 2005 (years and size classes). (2004: 67 elections, nothing to read.) With 13 cells a one-sided Bonferroni bar at 0.05 is z >= 2.67; 12 of the 13 pass it for the previous 10. This is the registry's drift test (112 section 6.5, test 3: a stable sign pattern while magnitudes move), which 112 states for the 16-type tie-sign model and which is applied here by analogy to the crowd coefficient: the coefficient runs from 1.2 to 2.0 across 2005-2013 with no sign change.

**Is it the opening wave?** The first votes of an election are plausibly the nominator's circle (an informal look at the file's first records suggested it; not coded, the module never reads the comments). Excluding the opening hours as *targets* (their votes stay in the windows as context), previous-10 / next-10 coefficients (100 shuffles each):

| targets | n | previous 10 (z) | next 10 (z) |
|---|---|---|---|
| none excluded | 112,850 | 1.44 (+14.8) | 1.63 (+17.0) |
| first 1 h excluded | 112,199 | 1.44 (+14.7) | 1.63 (+16.8) |
| first 6 h excluded | 100,319 | 1.44 (+13.2) | 1.63 (+15.5) |
| first 24 h excluded | 63,998 | 1.41 (+12.5) | 1.71 (+14.6) |

The coefficients move by at most 0.09 when up to the first 24 hours' targets are dropped, and every z stays above 12: it is not the opening wave.

**Asymmetric herding?** A randomised experiment on prior ratings (L1130, `sa`, abstract only: a comparator, not evidence here) found positive prior ratings raised later positive ones while negative ones were corrected. Slopes of the logit in the share of the previous 10 votes below and above one half, each against its shuffle null (the null is not flat: composition enters nonlinearly): below 50%: -0.38 against -1.97 (excess +1.59, z +12.2); above 50%: +2.77 against +0.72 (excess +2.05, z +25.7). The difference of the two slopes, above minus below, is +0.46 over its null (z +3.5): the excess is larger above one half (following a supportive run) than below it, but both are positive: an asymmetry of degree, not the correction of opposing runs the comparator reports.

**Gap profile.** Do consecutive votes agree, by the minutes between them (excess over the shuffle null):

| gap (minutes) | pairs | agree | null | excess | z |
|---|---|---|---|---|---|
| 1 | 3,842 | 0.834 | 0.786 | +0.048 | +8.5 |
| 2-5 | 14,856 | 0.838 | 0.777 | +0.061 | +20.0 |
| 6-20 | 31,774 | 0.814 | 0.773 | +0.042 | +20.1 |
| 21-60 | 38,539 | 0.798 | 0.778 | +0.020 | +11.5 |
| 61-240 | 45,960 | 0.795 | 0.788 | +0.007 | +4.1 |
| 241-1000 | 21,652 | 0.802 | 0.807 | -0.005 | -2.0 |
| >1000 | 2,700 | 0.810 | 0.811 | -0.000 | -0.1 |
| same minute (order-free) | 927 | 0.660 | 0.740 | -0.080 | -6.2 |

The dependence is a few percentage points, peaks at 2-5 minutes, is a third of its peak by an hour and is gone after about four hours. Votes saved in the same minute agree **less** than chance (pairs are compared without using their order, because within a minute the file lists supports before opposes). On planted data both a visible-influence world and a continuous shock give a same-minute *surplus*, so the deficit is produced by neither; a technical cause (for example simultaneous saves of one section being refused by the wiki) is a guess that was not checked. The pattern fits "the recent past matters" and is why the recency window fits best (4.1).

### 2.5 Robustness to the cleaning

| variant | targets | logit coef (z) | FE coef (z) | previous-10 share (z) | next-10 share (z) |
|---|---|---|---|---|---|
| primary (gap 10 d, n >= 20, m >= 5, kappa 4) | 150,218 | +0.85 (+8.0) | +0.28 (+29.2) | 1.44 (+16.7) | 1.63 (+17.6) |
| silence of 14 days splits a candidacy | 150,231 | +0.85 (+7.3) | +0.28 (+31.8) | 1.45 (+15.0) | 1.62 (+16.0) |
| elections of at least 40 votes | 133,631 | +1.03 (+7.1) | +0.40 (+31.3) | 1.45 (+16.6) | 1.62 (+18.0) |
| targets with at least 10 votes before | 137,782 | +0.42 (+3.4) | +0.27 (+27.7) | 1.44 (+16.7) | 1.63 (+17.6) |
| targets with at least 20 votes before | 112,859 | -0.55 (-2.2) | +0.23 (+28.8) | 1.44 (+16.7) | 1.63 (+17.6) |
| targets cast at least 1 h after the first vote | 147,504 | +0.78 (+7.2) | +0.26 (+29.4) | 1.44 (+16.7) | 1.63 (+17.6) |
| propensity prior strength 1 | 150,218 | +0.88 (+8.3) | +0.28 (+29.0) | 1.45 (+16.9) | 1.63 (+17.8) |
| propensity prior strength 16 | 150,218 | +0.81 (+7.8) | +0.28 (+29.5) | 1.43 (+16.7) | 1.61 (+17.5) |

(100 shuffles each. The two window columns need ten votes on each side, so they ignore the minimum-history and one-hour rules and change only with the silence, the election size and the propensity prior.) The local dependence and the fixed-effect result do not move with the cleaning. The cumulative logit coefficient does: positive for five earlier votes, weaker at ten, negative at twenty -- the same turnout dependence as 2.3, not a cleaning effect.

## 3. Part 2: participation

### 3.1 Cumulative curves

| group | elections | votes | 1 h | 6 h | 24 h | 72 h | 120 h | 168 h |
|---|---|---|---|---|---|---|---|---|
| all | 2595 | 174,705 | 0.07 | 0.21 | 0.47 | 0.73 | 0.87 | 0.98 |
| final support <.40 | 332 | 12,575 | 0.13 | 0.38 | 0.74 | 0.92 | 0.97 | 0.99 |
| final support .40-.60 | 319 | 18,462 | 0.08 | 0.23 | 0.54 | 0.82 | 0.92 | 0.99 |
| final support .60-.75 | 363 | 31,037 | 0.05 | 0.17 | 0.42 | 0.69 | 0.84 | 0.97 |
| final support .75-.90 | 346 | 27,862 | 0.05 | 0.17 | 0.40 | 0.67 | 0.83 | 0.98 |
| final support >=.90 | 1235 | 84,769 | 0.07 | 0.20 | 0.45 | 0.72 | 0.86 | 0.99 |
| 20-39 votes | 686 | 19,916 | 0.12 | 0.31 | 0.62 | 0.83 | 0.92 | 0.99 |
| 40-79 votes | 1131 | 65,920 | 0.07 | 0.20 | 0.47 | 0.74 | 0.87 | 0.98 |
| 80-159 votes | 698 | 73,308 | 0.06 | 0.18 | 0.43 | 0.71 | 0.86 | 0.99 |
| 160+ votes | 80 | 15,561 | 0.06 | 0.17 | 0.40 | 0.68 | 0.84 | 0.97 |

Share of an election's votes cast by each hour after its first vote (pooled over votes). Every curve is monotone (a count), front-loaded and concave. Elections that end below 40% support are over soonest; elections of 80 or more votes are the slowest to fill.

### 3.2 Shape against a clock-only null

Stage rates over hours 1-24, 24-96, 96-156, 156-168 (1285 elections of 60 or more votes). The null redraws each election's votes independently from the pooled hour profile of elections of its size: participation as one common clock and nothing else (300 redraws; interval = 2.5-97.5%).

| shape | observed | clock-only null |
|---|---|---|
| decelerating | 46.1% | 46.3% [43.6%, 48.6%] |
| decelerating + end bump | 40.6% | 51.7% [49.4%, 54.6%] |
| mid-phase faster than day 1 | 3.5% | 0.1% [0.0%, 0.2%] |
| other | 9.7% | 2.0% [1.3%, 2.7%] |

Variance across elections of the first-day share of votes: observed 0.0184, clock-only null 0.0036 (97.5% point 0.0040): **5.1 times** the clock's. The plainest shape (rates non-increasing, no late bump) matches the clock to the percentage point, and the clock makes the end-bump variant more often than the data show, so the curve's shape does not discriminate between a cascade orbit and attention decay. What a clock cannot make is the spread: elections differ in speed, and (3.3-3.5) the difference is tied to how the tally goes.

### 3.3 Stall: the process stops early for failure, and more often the lower the final support

| final support | elections | no vote after 72 h | after 120 h | after 144 h |
|---|---|---|---|---|
| <.40 | 332 | 70.2% [65.1%, 74.8%] | 76.8% [72.0%, 81.0%] | 81.3% [76.8%, 85.2%] |
| .40-.60 | 319 | 32.3% [27.4%, 37.6%] | 43.6% [38.2%, 49.1%] | 51.4% [45.9%, 56.8%] |
| .60-.75 | 363 | 14.3% [11.1%, 18.3%] | 20.7% [16.8%, 25.1%] | 25.6% [21.4%, 30.3%] |
| .75-.90 | 346 | 3.2% [1.8%, 5.6%] | 6.1% [4.0%, 9.1%] | 9.0% [6.4%, 12.4%] |
| >=.90 | 1235 | 0.2% [0.1%, 0.7%] | 1.1% [0.6%, 1.8%] | 6.0% [4.8%, 7.5%] |

Wilson intervals. Theorem 6.3's orbit stalls at the least fixed point; here the candidacies that stall before the deadline are failing ones (397 of the 402 elections with no vote after 72 h were not promoted), and the stall rate rises steadily as the final support falls, not only at decisive failure (the file does not say why; early closing or withdrawal would be the presumed reasons -- an institutional gate on top of the voluntary one). Successful candidacies run on at a low rate to the clock. The closing gate is one-sided.

### 3.4 Ignition: is there a late acceleration, and does the state trigger it?

| running share at hour 120 | elections | votes/h, 120-156 h | votes/h, 156-168 h | ratio last 12 h / before [95% CI] | null (sd) | z |
|---|---|---|---|---|---|---|
| <.50 | 163 | 0.104 | 0.074 | 0.71 [0.58, 0.86] | 0.76 (0.02) | -2.4 |
| .50-.70 | 262 | 0.166 | 0.169 | 1.01 [0.89, 1.15] | 1.08 (0.03) | -2.1 |
| .70-.85 | 280 | 0.289 | 0.387 | 1.34 [1.21, 1.47] | 1.40 (0.03) | -2.0 |
| .85-.95 | 323 | 0.226 | 0.281 | 1.24 [1.14, 1.37] | 1.13 (0.02) | +5.8 |
| >=.95 | 930 | 0.189 | 0.211 | 1.12 [1.06, 1.18] | 1.13 (0.01) | -1.7 |

Elections still alive (a vote between hours 72 and 120) with 30 or more votes; the ratio exceeds one in the passing bands (a deadline bump), is about one at 50-70% and is below one only where the tally is losing. The contested-passing band (70-85%) minus the pooled decisive bands is +0.22; the shuffle that keeps each election's composition but randomises the path gives +0.30 (0.03), so the contrast is **smaller** than composition alone predicts (z -2.7). Ignition in the law's sense (a rise triggered by a contested state) is not seen. The band-by-band z column is not flat, though: <.50 -2.4, .50-.70 -2.1, .70-.85 -2.0, .85-.95 +5.8, >=.95 -1.7; the late rise is therefore not purely a clock-and-composition effect, but where it departs from the shuffle (above the null at .85-.95; below it at <.50, .50-.70, .70-.85) is not a surge in the contested band, which is where ignition would show.

### 3.5 The hazard of new votes and the gate

Poisson regression of the number of votes per bin (16 bins over hours 1-168) on a common time profile, year, the first hour's votes (election scale), the final-support class (composition), log turnout since the first hour, the previous bin's rate (persistence) and the running support share (three or more earlier non-neutral votes; bands below). Coefficients relative to the 70-85% band. The shuffle reassigns the signs among the vote slots of each election, so timing, turnout and composition are untouched and only the share's *path* is randomised; a coefficient beyond its null is dependence of timing on the tally's history, over and above the election's composition.

| window | turnout | rate | < 50% | 50-70% | 85-95% | >= 95% | share (linear) | share curvature |
|---|---|---|---|---|---|---|---|---|
| 1-24 h | 0.16 | 0.34 | -0.30 / -0.09 (-7.5) | -0.10 / -0.00 (-3.8) | -0.02 / +0.00 (-0.9) | -0.00 / +0.01 (-0.6) | +0.32 / +0.09 (+6.7) | -0.46 / -0.37 (-1.2) |
| 24-168 h | 0.33 | 0.47 | -0.59 / -0.20 (-10.9) | -0.36 / -0.12 (-12.7) | -0.02 / -0.08 (+4.0) | +0.02 / -0.08 (+5.7) | +1.17 / +0.29 (+12.3) | -2.10 / -2.06 (-0.2) |
| 1-168 h | 0.19 | 0.45 | -0.51 / -0.20 (-14.3) | -0.27 / -0.09 (-12.8) | -0.06 / -0.06 (+0.0) | -0.04 / -0.05 (+0.5) | +0.59 / +0.19 (+13.2) | -0.86 / -0.61 (-3.0) |

Each share cell: observed / shuffle null (z). Participation is lower than the composition-and-clock null when the tally runs against the candidate, and is flat at and above 85%; in the late window the high bands sit *above* the null. The low bands of the late window include elections the closing rule had already stopped (3.3), so there the gate is partly institutional; the first-day window, before almost any early closure, shows the same direction at a smaller size. The raw curvature is negative, but so is its null (most of it is the mechanical shape the shuffle also gives); the excess is 1-24 h -0.09 (z -1.2), 24-168 h -0.04 (z -0.2), 1-168 h -0.25 (z -3.0): a plateau, not a fall, and never convex. The turnout coefficient (0.59 to 0.67 alone, 0.12 to 0.33 once the previous rate is controlled) is an association with no null: turnout and unobserved popularity are not separable here, so it is not read as complements in participation.

## 4. Part 3: variations, compared out of sample

### 4.1 The sign's dependence on the crowd: the forms compared

Same controls, same votes (at least 20 earlier), election-level 5-fold cross-validation. "CV gain" is the held-out log-likelihood per 1000 votes over the controls-only model; "null gain" is the same number from 12 within-election shuffles, **where any gain is mechanical** (flexible forms fit the nonlinear way the candidate's composition enters); "excess" is the difference.

| form | params | AIC | CV gain (se) | null gain (sd) | excess | z |
|---|---|---|---|---|---|---|
| controls only (no running state) | 17 | 68916 | +0.00 (0.00) | +0.00 (0.00) | +0.00 | n/a |
| cumulative share, linear (Kuran: threshold falls with the share) | 18 | 68904 | +0.03 (0.05) | -0.00 (0.00) | +0.03 | +6.2 |
| cumulative share + curvature (convex = bandwagon, concave = gate) | 19 | 67847 | +4.77 (0.32) | +4.31 (0.17) | +0.46 | +2.6 |
| cumulative share, spline (knots .50 .75 .90) | 21 | 66829 | +9.31 (0.46) | +8.07 (0.23) | +1.25 | +5.4 |
| share of the last 5 votes | 18 | 68338 | +2.59 (0.32) | -0.01 (0.01) | +2.60 | +400.4 |
| share of the last 10 votes | 18 | 68187 | +3.27 (0.37) | -0.00 (0.01) | +3.27 | +300.6 |
| share of the last 20 votes | 18 | 68342 | +2.55 (0.34) | -0.01 (0.01) | +2.56 | +377.2 |
| vote margin S - O (tens) | 18 | 68909 | +0.01 (0.05) | +0.01 (0.02) | -0.01 | -0.3 |
| log-odds of the tally | 18 | 67717 | +5.35 (0.34) | +6.32 (0.18) | -0.97 | -5.3 |
| majority indicator (step at 50%) | 18 | 68445 | +2.10 (0.23) | +1.48 (0.11) | +0.62 | +5.8 |
| cumulative share x log turnout | 19 | 68906 | -0.00 (0.05) | +0.08 (0.05) | -0.08 | -1.6 |
| cumulative share + last 5 votes | 19 | 68274 | +2.86 (0.32) | -0.01 (0.01) | +2.87 | +431.0 |

z is the excess over the sd of the 12 null draws: a test against random order, rough with so few draws, and not a precision (the se column is the sampling error of the gain itself). In-sample AIC prefers the log-odds and spline forms; most of their out-of-sample gain is what shuffled data give too (the spline +8.07 of +9.31; the log-odds form more than all of it, excess -0.97, z -5.3). **The best fit is the share of the last 10 votes** (excess +3.27), then the last 5 and last 20; adding the cumulative share to the last 5 adds +0.27. Kuran's linear threshold-falls-with-the-share form (cumulative share, linear) has excess +0.03 (beyond a null that barely moves, z +6.2, but 1% of the window's); the spline keeps +1.25 (z +5.4) and the step at 50% +0.62 (z +5.8), order-dependence the linear form misses, which may be the recent votes seen through the cumulative share; the two-sided (concave) curvature +0.46 (z +2.6); the vote margin -0.01. Slopes of the spline form by segment (logit scale, observed; they contain the mechanical shape and are not read): 0-.50 +0.1, .50-.75 -1.4, .75-.90 +1.2, .90-1 +15.1.

### 4.2 The participation hazard: the forms compared

Held-out Poisson log-likelihood of each form over the "turnout + recent rate" form, with the share of the same form fitted to shuffled signs as the null gain (20 shuffles). Standard errors are across elections.

| window | form | params | gain over turnout+rate (se) | null gain | excess |
|---|---|---|---|---|---|
| 1-24 h | + share, monotone | 26 | +108 (23) | +16 | +92 |
| 1-24 h | + share + curvature (convex = Kuran, concave = two-sided) | 27 | +122 (25) | +22 | +100 |
| 1-24 h | + share bands (free shape) | 29 | +98 (22) | -0 | +98 |
| 24-168 h | + share, monotone | 26 | +1549 (244) | +1200 | +348 |
| 24-168 h | + share + curvature (convex = Kuran, concave = two-sided) | 27 | +1669 (247) | +1287 | +382 |
| 24-168 h | + share bands (free shape) | 29 | +1521 (239) | +1205 | +315 |
| 1-168 h | + share, monotone | 34 | +588 (66) | +210 | +378 |
| 1-168 h | + share + curvature (convex = Kuran, concave = two-sided) | 35 | +660 (71) | +239 | +421 |
| 1-168 h | + share bands (free shape) | 37 | +697 (77) | +216 | +481 |

The state terms earn their keep against the common-clock-plus-persistence model in every window, and the ordering among the share forms is small beside the standard errors. The raw curvature is negative in every window and its excess over the shuffle null is negative in every window (1-24 h -0.09 (z -1.2), 24-168 h -0.04 (z -0.2), 1-168 h -0.25 (z -3.0); 3.5), beyond the null only over 1-168 h: saturating, and never convex (Kuran's accelerating bandwagon).

### 4.3 Mapping to the law's forms

| law's form | implemented as | result |
|---|---|---|
| one-sided monotone F (Granovetter) | linear in the share | sign: excess +0.03; participation: gain over turnout+rate in every window |
| Kuran: threshold falls with the share | linear (sign) / positive curvature (participation) | sign: a negligible gain (+0.03); participation: curvature, and its excess over the null, negative in every window |
| two-sided gate (hump) | negative curvature / free bands | sign: curvature excess +0.46; participation: the fall is on the *low* side only |
| recency, not the cumulative share | share of the last L votes | sign: the largest gain (excess +3.27; the cumulative share's best form, the spline, +1.25) |

## 5. The sign operand sigma in this medium and era

| scale of the law | measure | sign of the dependence | status |
|---|---|---|---|
| vote's sign, local (last 5-20 votes) | controlled logit, election FE, agreement with the recent majority; every year from 2005, all sizes | + (co-movement) | supported; influence vs shock undecided |
| vote's sign, cumulative share | controlled logit; out-of-sample gain | + below 20 earlier votes; spec-dependent above 40; a small out-of-sample gain (spline +1.25, linear +0.03, against the window's +3.27) | not identified |
| vote's sign, cumulative majority | agreement vs random order | below random order (-0.4 points) | read as non-stationarity (2.2), not as substitutes |
| participation, running support share | Poisson hazard, shuffle null | + and saturating; flat above 85%; present in the first day | one-sided gate supported (the late-window part partly the closing rule) |
| participation, decisive success | bands >= 85%, against the path-shuffle null | no fall (at or above the null) | upper gate refuted in its path-dependent form; a gate through the final composition is not tested |
| participation, decisive failure | bands < 70%; stall table | falls; process stalls (72 h: 70% vs 0.2%) | closure, partly institutional |
| participation, late acceleration | end-window ratio by state | deadline bump in every band but the losing ones; contrast below composition; the .85-.95 band above it (z +5.8) | state-triggered ignition not seen |

So sigma is **+1 as co-movement at the scale of the last few votes, with a short memory, and not -1 anywhere that survives a second estimator**. `models/00-v0.md` §4.4 carries sigma as a setting operand (since v0.1); for this setting the reading is: sigma = +1 as an association (the causal sign is not identified: influence and a shared shock are not separated), the state is a recency window rather than the cumulative share r(t), and the law's two-sided gate reduces to a lower gate on participation when the tally runs against. The Hong Kong substitutes (L4355) are not repeated here; the claim that the sign flips with turnout (L4363) is reproduced by the logit on the cumulative share and contradicted by the detrended model, so it stays open.

## 6. Caveats

- **Observational.** The shuffle null tests exchangeability of order given composition. It does not separate influence from a shared shock; the one placebo that might (time reversal) is shown on planted data not to. Slow drift within an election would also break exchangeability; the gap profile (no excess agreement of consecutive votes more than four hours apart) argues against drift as the source of the local co-movement, and the detrended estimator (2.2) removes a quadratic trend from the cumulative one.
- **A vote is not a riot.** It is a public, consequential, one-shot act on a wiki, cast by editors who can see the page and the tally; voters often give a reason that cites the nominator or an earlier voter (an informal look at the file suggested so; not coded, and the module never reads the comments). The opening votes are plausibly the nominator's circle (the same informal look; tested only indirectly, by dropping the opening hours, 2.4).
- **Timestamps** are signature times to the minute, in the file's wall clock; a changed vote carries the time of its last signature; 5% of votes are undated and were dropped (missing at random is assumed). File order within a minute is page order and is not used.
- **Election definition.** A candidacy is a (candidate, result, year) group split at 10-day silences; 14 days gives the same results (2.5). An election that stops early is part of the data and is shown as such, not removed.
- **Controlling the final outcome** conditions on a post-treatment variable when influence exists: the primary logit understates complements (planted data) and the election-fixed-effect model has a strongly negative mechanical null. Each is read only against its own shuffle.
- **Non-stationarity.** Elections open with a run of supports and drift; the cumulative running share partly measures that drift. This is why its sign is spec-dependent and why recency windows fit.
- **Turnout and rate coefficients in the hazard have no null** (the shuffle does not move them) and confound popularity with persistence; they are described, not tested.
- **Participation counts all votes** (support, oppose and neutral). The law's two-sided gate is stated for the share who have taken one action; side-specific hazards (supporters' arrival against the support share, opposers' against the oppose share) were not fitted, because a sign-specific response cannot be tested against a sign-shuffle null. The lower gate found here is on total participation.
- **One site, 2003-2013, English Wikipedia.** The law is not tested beyond it. Years 2003-2004 have too few elections to read (2004: 67).
- **Multiplicity.** 15 cells in 2.1 (7 years pass a Bonferroni bar), 13 in the local table (12 pass), five turnout bins times two estimators in 2.3, 18 hazard share terms, 12 sign forms, and many specifications elsewhere. The verdict rests on statistics with |z| of 4 or more, on signs that agree across cells and estimators, and on point estimates, not on the marginal cells; a single cell with |z| near 2 (the logit at 40-79 earlier votes, a year like 2013) is not evidence on its own. p-values are the one-sided shuffle p with the +1 correction (smallest possible 1/(B+1)).

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.crowd_gate_wikirfa report      # 20 to 30 minutes on eight cores; writes results/crowd_gate_wikirfa.md
    ~/.local/bin/uv run pytest tests/test_crowd_gate_wikirfa.py

The local copy of the data is reused from `sim/data/wiki-rfa/` (fetch only if absent: `python -m models.crowd_gate_wikirfa fetch`, which refuses a file whose sha256 differs). Every random draw is seeded by (seed, tag, draw), so the numbers do not depend on the number of cores. Regenerating keeps any hand-written `## Review (date)` section at the end of this file.

## Review (2026-11-01)

_A second session reviewed this test the same day, after the file above was first generated. The numbers above are now from the corrected code, re-run at the published settings (seed 20261101, 400 shuffles for the main null). Nothing was committed._

**Re-run and re-derivation.**
- Suite before the review: 44 passed. After it: 47 passed (three new tests: the propensity toy, the asymmetry, keeping this section).
- Re-run at the published settings, the original code regenerated the first version of this file **byte for byte**, so its numbers were current.
- An independent rebuild of the primary estimate gives **0.8478** on the same 150,218 targets, AME +0.76 points. It used per-election loops for the strictly-earlier share and turnout, rebuilt the controls from the parsed votes, and fitted with scipy L-BFGS rather than the module's IRLS.

**One code error, fixed.** The voter propensity is meant to leave out the vote's own (voter, candidate, result, year) group. The code subtracted the kept vote's sign, but the history had counted the group's last vote in *file* order. For **182 of 162,733 votes** the two differ: a changed vote listed out of time order, or a voter in two candidacies of one group with different signs. For those votes the counted vote stayed in, and a vote that was never counted was taken out (the voter's other-support count could reach -1).
- The code now subtracts the counted vote (`counted_group_vote`).
- A toy test fails on the old code (0.571 against 0.771).
- Effect: the primary coefficient goes from 0.8483 to 0.8478, with z unchanged. The controls fit better (log-likelihood +3.8), so every AIC in 4.1 is 7 to 8 lower. No other printed number moved by more than one unit in its last digit (2010: 0.13 to 0.12; next-20 window: 2.26 to 2.27).

**Checks that found nothing wrong.**
- *Null model.* The within-election shuffle is implemented as described:
  - Vote-attached arrays move together: sign, propensity, first-timer flag, experience and voter.
  - Slot-attached arrays stay put: minutes, tie runs, clock bins, election size and result. So the strictly-earlier bookkeeping is redone on every draw.
  - The participation null permutes non-neutral signs among non-neutral slots and keeps the times. The shape null redraws hours from the pooled profile of the election's size class.
  - It is the right null for exchangeability of order given composition. It cannot separate influence from a shared shock, or from slow drift (the gap profile argues against drift, see the caveats). It cannot see a gate that acts through the final composition. The verdict now says each of these where it matters.
- *Within-minute order.* Within a minute the file lists supports before opposes, which could leak into windows and consecutive pairs at tie boundaries. Dropping every pair that touches a same-minute run leaves the gap profile unchanged (2-5 min: +0.061, z +21.6).
- *Leakage.* Running states use strictly earlier minutes only, which a test checks against a brute-force loop. Cross-validation folds are whole elections. The composition controls (leave-one-out share, result, final class) use the whole election by design and are read only against their own shuffle.
- *Multiple comparisons.* The file now prints Bonferroni counts: 7 of 10 years in 2.1 pass p <= 0.0033, and 12 of 13 local cells pass z >= 2.67. The sign forms now carry z against their null draws. The caveat names the marginal cells, and no verdict rests on one.
- *Terms and data.* Use matches `sim/data/README.md`:
  - The file is read in place and is git-ignored (`git check-ignore`).
  - The comments are discarded at parse time.
  - Names become integers on load and are never written.
  - The results and tests hold statistics only; the tests use synthetic toy names.
  - Wording fixed: "never read into memory" became "never parsed, stored or used", because the parser does read each TXT line before discarding it. The remarks on what the comments say are now labelled as an informal look.
  - Not changed here: `sim/data/README.md` and L4562 say "11,380 named voters". That figure is voters and candidates together; the voters alone number 10,416, as 117 §3.3 and this suite count them.
- *Ledger ids.* Every cited id exists and says what the code assumes:
  - L1831 is a split root (L3511, L3512), cited the way v0.2.1 cites it.
  - L1201's left-continuity condition holds for the maps the orbit test uses.
  - L1130 is `sa` and feeds nothing.
  - 112 §6.5 test 3 is not a ledger id. 112 states it for the 16-type tie-sign model, so its use here is now called an analogy.

**Verdict wording that went beyond the numbers, corrected.**
1. *"Substitutes refuted."* Now: a net negative *association* is refuted. The causal sign is not identified.
2. *"The cumulative forms are at the null."* Against the null's spread they are not:
   - spline +1.25 (z +5.4)
   - step at 50% +0.62 (z +5.8)
   - curvature +0.46 (z +2.6)
   - linear +0.03 (z +6.2, but 1% of the window's +3.27)
   - log-odds -0.97 (z -5.3, below its mechanical gain)

   Now "carries little of it". The verdict also says the comparison uses only votes with at least 20 earlier votes.
3. *"Positive at every turnout once detrended."* The detrended coefficients are negative. What is positive at every turnout is their excess over the null. Fixed here and in 2.2-2.3.
4. *Upper gate.* The status list and section 5 said "refuted" while the summary said "not found". Now: refuted only in the path-dependent form this design can see. A gate acting through the final composition is untested.
5. *Kuran's convex participation curve "refuted, the curvature is negative".* That was the raw coefficient, and the shuffle gives most of it (null -0.37, -2.06, -0.61). The excess is negative in every window but beyond its null only over 1-168 h (z -3.0). Moved to "not found". The test now checks the excess.
6. *"Late acceleration is a clock-and-composition effect."* The 85-95% band rises more than the shuffle gives (1.24 against 1.13, z +5.8). That is said now and recorded in a test. A surge in contested states, which is what ignition would be, is still not seen.
7. *"Stall attaches to decisive failure only."* 32% of elections ending at 40-60% stall too. Now: the stall attaches to failure (397 of the 402 elections silent after 72 h failed) and rises as final support falls. Test renamed.
8. *Lower gate.* The first-day window is now quoted (-0.21 and -0.09 log-points), because the week-long figures include elections closed by the rule.
9. *"No asymmetry between following a supportive and an opposing run."* This was never tested. The new test of the difference gives +0.46 over its null (z +3.5): the excess is larger after supportive runs, though both excesses are positive. Now a data test.
10. *Smaller fixes:*
    - "Small beside the local effect" removed: the local AME is +1.24 points against +0.76.
    - "The same to two decimals" replaced: the coefficients move by up to 0.09.
    - "Time-symmetric" became "about equal": the logit and the fixed-effect model order the two windows differently.
    - "One-sided, against complements" became "in the direction of complements".
    - The dominant shape no longer says "rates non-increasing", because it includes the end-bump class.
    - Hard-coded counts are now taken from the run. One of them had printed "all N years" without checking.
11. `write_report` now keeps any `## Review (date)` section when the file is regenerated (tested), so this section survives the next run.

**Verdict after review.**
- *Supported:* sigma = +1 **as co-movement** with the last 5 to 20 votes. The evidence: z +16, every year from 2005, every size class, logit and fixed-effect models. It is short-memory, and influence against shared shock is undecided.
- *Weak:* the cumulative share carries little of the dependence (spline +1.25 against the window's +3.27). Its sign above 40 earlier votes is undecided.
- *Participation:* a one-sided lower gate, present in the first day and partly the closing rule later. No path-dependent upper gate. No ignition, though one passing band has a state-dependent late rise. The participation curve's shape does not discriminate between a cascade orbit and attention decay.
- *What changed:* the first version overstated five things: substitutes "refuted" as if causal, the cumulative forms "at the null", Kuran's convexity "refuted" on a mostly mechanical coefficient, the stall as "decisive failure only", and "no asymmetry" without a test. The numbers stand.
