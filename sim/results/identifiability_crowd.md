# Identifiability of the crowd law from aggregate curves, on independent synthetic crowds

_Generated 2026-11-01 by `uv run python -m models.identifiability_crowd_report report` (seed 20261101). Code: `sim/models/identifiability_crowd.py` (tasks, engines), `sim/models/identifiability_crowd_report.py` (this file); checks: `sim/tests/test_identifiability_crowd.py`. No data are used: every crowd is simulated. Ledger ids are those of `identifiability_crowd.LEDGER`._

## What was tested

Granovetter's map r(t+1) = F[r(t)] (`models/00-v0.md` 4.4; L1831, L3960, L3961) with the two-sided gate (L3959, L4355), and
Claim 1 of `models/02-our-claims.md` (the state of a crowd is its whole threshold distribution F; a merge is the mixture; ignition,
Claim 1.4), are the crowd law. The event datasets of `docs/prior-work/089` record aggregate counts over time and never a threshold
(L3980, L3988, L4469). Under the no-circularity rule of `notes/2026-10-29-modelled-population-testbed.md` this file builds crowds
from generators that are **not** the fitted family and shows the fitting code only the noisy aggregate curve r(0), ..., r(10). Three
questions: **(1)** can F be recovered from the curve, and at what crowd size n and observation noise sigma; **(2)** can a two-sided
gate be told from a one-sided one; **(3)** can Claim 1.4's ignition criterion be predicted from the two parts' curves. The nulls are
named where each test is introduced: rank uniformity for calibration, a monotone latent curve for the gate, no skill beyond the base
rate for ignition.

## Verdict

**In short.** From the aggregate curve of a crowd the crowd law can be fitted to *where the crowd stopped*, to *the instigator share* and to *F at the few points the
curve visited* (a median of 3-6 points; 2-50% of curves read three or fewer). It cannot be fitted, without assuming the family, to F above the curve's own stall; nor to the threshold family, to the gate's sign (except through a decline),
or to the quantity that decides ignition. The event datasets of 089 (counts or count bins, no pool) give less than this test gave the model,
so they cannot fit F, evaluate Claim 1.4's criterion or set Claim 1.11's refutation test; what would is data that move r (interventions) or per-member thresholds.

**Supported** (exact, or measured with the calibration shown in 3.2):

1. *The exact engines are right; the synthetic one is right only where n sigma is large.* SBC passes in 10 of 10 exact-engine cells (n = 30 to 3,000, exact counts) and in 10 of 10 lattice-engine
   cells (noise, n = 30 and 100; the n = 100 cells have 40 datasets each). The synthetic (Gaussian) engine passes in only 14 of 24 cells, mostly failing at n <= 300 with sigma <= 0.03 (worst central-90% coverage
   0.72), and fails in 6 of 6 comparisons with the exact engine at n = 30. Its cells carry a star in 3.2; the misspecification and ignition cells with sigma > 0 (3.3, 3.5)
   also rest on it, at every n, without stars, and the misspecification setups' own SBC fails in 9 of 27 cells (end of 3.3; corrected at review: this item said
   the engines are right wherever they are used).
2. *Claims 1.2 and 1.4 hold on finite crowds.* No violation of Claim 1.2's equal case or Claim 1.4's necessary condition in 1,882 igniting pairs, nor of the sandwich in
   495 pairs or of its strictness in the 484 of them with unequal stalls, from four generators (three of them, beta, bimodal and clipped normal, also used by `models/02`'s own check, 1.8;
   corrected at review: the igniting-pair check was reported as strictness, and the generators as ones the claims were not built on).
3. *The stall is read, and F is read where the curve went.* In a correctly specified family at n = 1,000 and sigma = 0.03 the median posterior sd of the stall tau is 0.004* (clipped normal)
   and 0.027 (beta+atom) of its prior sd, and of F inside the visited range 0.08* and 0.06 (* = synthetic engine not calibrated in that cell); with exact counts at n = 3,000 all four are below 0.01. The median hides
   the near-critical crowds, where the stall is a coin toss: the RMSE of tau's posterior mean is 0.09-0.38 of the prior sd over the cells with n >= 1,000 (column "RMSE tau" in 3.2).

**Refuted** (as claims about what an aggregate curve can do):

4. *F above the stall is not recoverable without assuming the family.* Exactly: redrawing every threshold above the stall leaves the curve unchanged. With a non-parametric prior the posterior sd of F above the stall stays
   at 0.96-0.98 of the prior's from n = 30 to 10,000. In a parametric family the family's own shape fills the gap, with a width that is calibrated where the engine is (3.2): with exact counts at n = 3,000 the posterior sd of F
   outside the visited range is 0.12 (clipped normal) and 0.42 (beta+atom) of the prior sd, against 0.00 inside, and with noise (sigma >= 0.03, n = 300 to 3,000) it is
   0.35-0.62 for both families.
5. *Recovery fails at these sample sizes* (median posterior sd above a quarter of the prior sd; the table "Where recovery fails" in 3.2). The parameters: for beta+atom at every n tested once
   sigma >= 0.01, and with exact counts below n = 1,000; for the clipped normal below n = 100 with exact counts, and at sigma = 0.1 at every n (0.40-0.42 of the prior sd at n = 300 to 3,000).
   F above the stall: for beta+atom at every n and noise tested; for the clipped normal below n = 3,000 (exact counts; sigma = 0.01 as well), and at every n for sigma >= 0.03. The stall itself is open at n <= 100
   for beta+atom (0.49 and 0.26 of the prior sd with exact counts). Noise sets the floor, not n: beta+atom's parameters sit at 0.35-0.43 (sigma = 0.03) and
   0.54-0.59 (sigma = 0.1) from n = 300 to 3,000.
6. *The family cannot be learned from the curve, and a wrong one is fitted confidently.* Fitted to a different family (pooled over cells with sigma > 0), the 90% interval of F covers the truth for 0.52 of
   readings inside the visited range and 0.57 outside, against 0.83 and 0.86 for the matching family, and the error outside is 1.31 prior sds against 0.72. By marginal likelihood the generating
   family comes first for 0.74-0.87 of clipped-normal curves, 0.34-0.78 of beta+atom curves and 0.23-0.35 of logit-normal curves (chance 0.33); bimodal crowds are attributed to logit-normal or
   beta+atom (no bimodal family was fitted, which is the point).
7. *Claim 1.4's criterion and Claim 1.11's test cannot be evaluated from the parts' curves.* The decisive quantity is F_1(M) at the host's stall M, above the intruder's own stall (Claim 1.2's equal case), where its curve is silent. An intruder
   redrawn above its own stall, with the same live curve, merges with the same host to the opposite outcome in 17% of pairs (a redrawn host cannot flip it), and the sandwich's upper end moves in 50%. From natural curves ignition is predicted with AUC 0.71-0.85 (matching family) and
   0.62-0.79 (wrong family) over n = 100 to 3,000, against 0.63-0.78 for a logistic regression on curve summaries. Like for like at n = 1,000: 0.80-0.85 (matching family) against 0.86-0.88 for a reference that knows F exactly,
   and 0.73-0.82 (wrong family) against 0.85-0.91. So a right family predicts nearly as well as knowing F, because it supplies F above the stall by assumption, and a wrong one can do worse than the summaries
   (corrected at review: the reference was quoted at n = 1,000 against the fitted model's range over all n, and the flip rate over pairs in which no flip is possible).
8. *A two-sided gate is visible only as a decline.* Between 35% and 64% of two-sided crowds have any decline in the noise-free current-share curve (the ceiling, Proposition A); the order test
   detects 2% to 52% (up to 52% at sigma = 0.01, 39% at 0.03, 30% at 0.1), with false positives of at most 5% (nominal 5%). On the cumulative (ever-joined)
   curve it rejects at its size (1% to 4%); that curve's only trace is a plateau followed by growth, in 0% to 22% of crowds (noise-free).

**What fixes it: interventions on r.** One run started at an exogenous share (r(0) = 0.5) takes the posterior sd of F outside the visited range from 0.49 to 0.08 (beta+atom, sigma = 0.03) and
from 0.33 to 0.06 (clipped normal); four runs to 0.03 and 0.04. The ignition AUC at n = 1,000 goes from 0.81-0.84 to 0.89-0.94 with matching families and from
0.76-0.82 to 0.82-0.90 with wrong ones; an adaptive probe at the host's stall reaches 0.82-0.92 with exact counts. This is the design of Cantoni et al.'s belief experiment (L4353-L4355), which moved the believed share rather than the share
itself: move the input of F and read the response. The curve alone cannot do it. The F-recovery numbers are within the right parametric family (4.5); without a family a seeded run reads F only at the points its own orbit visits.

**Not decided.** Whether real crowds follow the law at all (nothing here touches data); how the numbers change with threshold distributions that have atoms and gaps (Granovetter's own pair, L3964, is the
extreme; these generators are smooth); heterogeneous response times beyond the two variations in section 4; whether any real event offers an intervention on r (L4363 leaves the scope of the one experiment open).

**Status, by claim.**

- *Refuted:* that an aggregate curve identifies F above its own stall (exact; the non-parametric posterior is the prior at every n), the threshold family, or Claim 1.4's ignition criterion (at any n and noise level tested);
  that a fitted parametric family substitutes for that identification (above the stall it fixes F only through its own shape, to 0.12 to 0.42 of the prior sd at n = 3,000 even when right, and a wrong
  one is fitted with 90% intervals that cover 0.52 to 0.57 of the truths); and that a monotone curve can show a two-sided gate.
- *Supported:* the crowd law and Claims 1.2 and 1.4 as internally consistent on finite crowds; that the stall and the visited part of F are recoverable from a clean enough curve in a correct family (exact counts,
  n >= 300 to 1,000); that interventions on r recover what passive curves cannot (F shown within the right parametric family, 4.5; with a wrong family they raise the ignition
  AUC, 3.5).
- *Not decided:* the crowd law as a description of any real crowd.

## 1. Data and terms

**None.** Every crowd is simulated; nothing is downloaded, no credential or licence is involved, and `sim/data/` is untouched.
The relation to the event datasets of 089 matters for the reading of everything below. CCC sizes are order-of-magnitude bins and half
the events have none (L3980, L3988); NAVCO's `camp_size` is six ordinal bins at annual resolution (L4469); no dataset defines the
group whose share r(t) would be formed (089 section 3, equation-to-data map). This test therefore gives the crowd law **more**
than the event datasets give it: a known denominator n, a share on a continuous scale, ten equally spaced turns, a known noise level.
What cannot be fitted under these favourable conditions cannot be fitted on the real data.

## 2. Method

**The crowd and the curve.** A crowd of n members has thresholds theta_i, shares of the crowd. The state is the share r. The first
share is the instigators', r(0) = F_n(0), and then r(t+1) = F_n(r(t)) with F_n the empirical CDF (v0.1 4.4a; L1831, L3960,
L3961), so the curve is a sequence of integers k_t / n and is exact. The two-sided gate is theta_i <= r <= thetabar_i (L3959,
L4355; v0.1 2.3). Observed: y_t = r(t) + N(0, sigma^2), t = 0, ..., 10 (eleven points), unclipped, with sigma in {0, 0.01, 0.03, 0.1}
(sigma = 0 is exact counts). A crowd enters a dataset only if its curve reaches max(3 sigma, 1/n): event datasets contain events.
This selection depends on the observed data only, which leaves SBC valid (conditionally on y the ranks are still uniform).

**Generators.** Every one puts at least 2% of members at threshold 0 (a crowd with no instigator never moves, v0.1 6.3; the prior is
therefore a prior over crowds that can start):

| generator | parameters and continuous prior | role |
|---|---|---|
| beta+atom | z log-uniform [0.02, 0.25]; Beta(a, b), a, b log-uniform [0.6, 8] | generator and fitted family |
| clipped normal | mu uniform [0.04, 0.6], s log-uniform [0.03, 0.4], Phi(-mu/s) >= 0.02 (Granovetter's own family, L3962) | generator and fitted family |
| bimodal | z log-uniform [0.02, 0.2]; early mode m1 in [0.03, 0.35], late mode m2 in [0.45, 0.95], weight w in [0.2, 0.8], concentration log-uniform [8, 40] (as `explore/mixture_equilibria.py`) | generator only |
| logit-normal | z log-uniform [0.02, 0.25]; logit(theta) ~ N(mu, s), mu in [-3, 1], s log-uniform [0.3, 2.5] | generator and fitted family |

The fitted families are beta+atom, clipped normal and logit-normal, each on a discrete grid that is also the prior (uniform over
the grid; beta+atom 405 points, clipped normal 111, logit-normal 315; 'fine' grids of 864, 441 and 840 are used for the
misspecification and ignition work). A discrete prior makes the grid posterior **exact** and SBC exact; its cost is that a
continuous truth falls between grid points, which matters only where the posterior is narrower than the grid (stated where it does).

**Which parts are independent of the fit.** The well-specified SBC of 3.2 has the generator equal to the fitted family *by construction*: it is a computation and identifiability check
(094 section 5, items 1 and 2), a best case, and cannot fail because the model is wrong about crowds. The no-circularity rule bites in 3.3 (bimodal and logit-normal crowds fitted by the other
families), in the ignition work with the "other" generators, in the two-sided generator (which no fitted model contains) and in the inertial and subsampled curves of section 4.

**Engines.** `exact`: the sequential-binomial law of the integer path (derivation in the module docstring; the probabilities of all
paths sum to one for tiny n and match the simulator, tests group A), used at sigma = 0. `lattice`: the exact forward algorithm on
(k_(t-1), k_t) for sigma > 0, cost growing as n^3, used at n = 30 (M = 200) and n = 100 (M = 40). `synthetic`: Wood's synthetic
likelihood with common random numbers (S = 800 to 2,000 simulated crowds per grid point), an approximation used at n = 100 to 3,000
for sigma > 0. Its calibration is **measured**, not assumed (section 3.2): it is approximately calibrated at n >= 1,000 and not where counts
and noise live on the same scale (n sigma of order 1 to 10). SBC measured it on the standard grids with S = 2,000; the misspecification
(3.3) and ignition (3.5) cells with sigma > 0 use it at every n on the fine grids with S = 1,000 and 800. The misspecification setups
were given their own SBC at review (end of 3.3); the ignition setups (S = 800, two families pooled) were not.

**Uncertainty.** Each coverage or share is a proportion of M independent curves, so its binomial standard error is sqrt(p (1 - p) / M): at p = 0.9 it is 0.009 for M = 1,000, 0.015 for M = 400,
0.017 for M = 300, 0.013 for M = 500, 0.021 for M = 200 and 0.047 for M = 40; pooled readings of F (several probes per curve) are correlated within a curve and are less certain than their count suggests. AUCs carry
bootstrap intervals. Posterior-sd medians have no interval; their cell-to-cell scatter is visible across neighbouring rows.

**SBC (the computation check, 094 L4136, L4137, L4140).** Draw theta on the grid, simulate a live crowd and curve, compute the grid
posterior, and take the randomised rank of the truth under it for each of: every parameter, the population stall tau = min(r : F(r) <= r)
(models/02 Fact 0), F(0), F at r = 0.1, 0.25, 0.4, 0.55, 0.7, 0.85, and the joint log-likelihood of the data (L4156, L4153). **The
null is rank uniformity** (an exact posterior). Reported: KS p-value, and the coverage of the central 90% interval (nominal 0.90). A cell is
called calibrated if no KS p is below 0.001 and every coverage is within 3.5 binomial standard errors of 0.90. *Information* is the
median posterior sd divided by the prior sd, and RMSE of the posterior mean over the prior sd; F(r) is read **inside** the visited
range (r <= the level the curve reached) or **outside** it. A pass certifies the arithmetic, not the theory (094 L4140); information is
a best case (L4158).

**Misspecification and model recovery (094 L4157, L4149, L4160).** Curves from the independent generators with continuous parameters,
each fitted by every fitted family; scored by coverage of the 5-95% interval of tau, F(0) and F inside/outside, RMSE, and which family
has the largest marginal likelihood (a confusion matrix with a uniform prior over the three fitted families).

**One- versus two-sided gate.** The two-sided generator gives a fraction nu of members an upper gate theta + (1 - theta) V, V ~
Beta(w kappa, (1 - w) kappa), kappa = 6; the rest stay for ever. Detectors, with sigma known: the **order test** (likelihood ratio of a
non-decreasing latent curve against an unrestricted one, isotonic fit, critical value simulated under the flat curve, which is the
least favourable null so the test has size <= 0.05 for every non-decreasing curve) and an **any-drop rule** (largest drop y_s - y_t
over s < t, same calibration). Power is measured on two-sided crowds and false positives on one-sided crowds with the same lower
thresholds.

**Ignition (models/02 Claim 1.4).** Two independent crowds of n members each (merge weight 1/2); the label is realised ignition of the
merged finite crowd (stall strictly above both parts' stalls, in members; "material" ignition: at least 2% of the crowd higher).
Eligible: both curves live and neither ends above 0.97. Predictors, each scored by AUC against the label (95% bootstrap interval): the
population ignition margin computed from the TRUE generators (a reference that knows F exactly; not a ceiling, because the curves
also carry the realised crowds' own thresholds); the posterior-predictive probability of population ignition from fitting beta+atom
and clipped normal (averaged over the two families) to each curve; a logistic regression on summaries of the two curves (levels,
initial shares); an adaptive probe (start each crowd at the higher final level and read r(1) - r(0), an intervention on r); and the
fitted model given one, two or four fixed seeded runs.

## 3. Results

### 3.1 What a noise-free curve can fix: exact results

This section is arithmetic, not simulation: each statement is a construction with a test (`tests/test_identifiability_crowd.py`,
group B), true for any n and any F.

**Proposition B: a curve reads F at a handful of points, and none above its own stall.** The orbit reads the count of thresholds at 0
and at each distinct level the curve reaches, the last of which is the stall r*. It fixes how many thresholds lie in each cell between
those points and nothing about where inside a cell they sit or about any threshold above r*. `redraw_above_stall` redraws every
threshold above r* and leaves the whole curve identical. It runs the other way from L1225, where no finite moment of F fixes the
outcome: here the outcome curve, and so any summary of it, does not fix F above its stall. How many points does a curve read?

| generator | n | median points of F read | IQR | <= 3 points | <= 5 points | >= 8 points | cascade to everyone |
|---|---|---|---|---|---|---|---|
| beta | 100 | 3 | 2-6 | 50% | 70% | 16% | 37% |
| beta | 1000 | 5 | 2-7 | 42% | 62% | 23% | 40% |
| clipnorm | 100 | 5 | 4-6 | 13% | 62% | 17% | 63% |
| clipnorm | 1000 | 6 | 4-8 | 2% | 46% | 28% | 58% |
| bimodal | 100 | 4 | 2-7 | 41% | 63% | 19% | 26% |
| bimodal | 1000 | 6 | 3-9 | 26% | 44% | 33% | 34% |
| logitnorm | 100 | 4 | 2-6 | 38% | 68% | 15% | 51% |
| logitnorm | 1000 | 5 | 3-7 | 30% | 58% | 24% | 54% |

*(F is read at 0 and at every distinct level, the stall included. "Cascade to everyone" means the curve ends at 1, where nothing is
left above the stall to be unknown.)*

**Consequence for Claim 1.2 and 1.4.** Checked on random finite pairs from the four generators (beta, bimodal and
clipped-normal families were also among those of `models/02`'s own check, 1.8; logit-normal is new), with code independent of
that check:

| random finite pairs (n = 40 each) | igniting | igniting with equal stalls (Claim 1.2's equal case violated) | Claim 1.4 necessary condition violated |
|---|---|---|---|
| 20,000 | 1,882 | 0 | 0 |

| one part (clipped normal, n = 40) redrawn above its own stall, same live curve: pairs | merge outcome flipped | pairs in which the redrawn part is the intruder | flipped there | pairs in which it is the host or the stalls are equal | flipped there |
|---|---|---|---|---|---|
| 1,018 | 112 (11%) | 663 | 112 (17%) | 355 | 0 (0%) |

| live, unsaturated pairs (n = 200 each) | lower <= merged stall <= upper end violated | pairs with unequal stalls | merge not strictly above the lower stall (Claim 1.2 strictness violated) | upper end of the sandwich changes when both crowds are redrawn above their stalls (same curves) | ... by more than 0.05 |
|---|---|---|---|---|---|
| 495 | 0 | 484 | 0 | 246 (50%) | 178 (36%) |

Claim 1.2's equal case (equal stalls merge to that stall, so never ignite) and Claim 1.4's necessary condition hold in every
igniting pair (no violation in 1,882 ignitions); the sandwich (smaller stall <= merged stall <= upper end) holds in every
pair tried, and its strictness (unequal stalls merge strictly above the smaller) in all 484 pairs with unequal stalls:
that is support for both claims on finite crowds. But in an igniting pair the intruder's stall is strictly below the host's stall M,
and the decisive quantity F_1(M) is read at M, **above the intruder's own stall, where its curve is silent** (Proposition B). An
intruder redrawn above its own stall (the same live curve, a different crowd) merges with the same host to the opposite outcome in
17% of the pairs tried; a redrawn host cannot change the outcome (the merge
reaches the host's stall M only through thresholds at or below M, which the redraw keeps) and none did, so over all pairs the rate is
11%. The upper end of the sandwich, the quantity the refutation test of Claim 1.11
needs, moves in 50% of pairs when only the thresholds above the stalls are redrawn
(36% by more than 0.05). **Neither the ignition criterion nor the refutation test of
the merge law can be evaluated from the two parts' curves alone.**

**Proposition A: a monotone curve cannot show the gate.** If a crowd's current-share curve never declines it is a function
k_(t+1) = h(k_t) of the state alone, and a one-sided crowd built from the curve reproduces it exactly (`orbit_equivalent_one_sided`).
So a two-sided gate whose curve happens to be monotone is indistinguishable from a one-sided one at any n and with no noise, while a
one-sided curve never declines (v0.1 6.3(i), L1201). The decline is the only trace in the current-share curve. The ever-joined
(cumulative) count never declines at all; its only trace of the gate is a plateau followed by growth, which a one-sided stall
(absorbing) never shows.

**Counts are not shares.** With thresholds as absolute numbers of others (Granovetter allows either, L3983) the COUNT curve does not
depend on the pool N, so the stall share c*/N is not identified from counts (`count_orbit`; test). CCC, Mass Mobilization and NAVCO
record counts or count bins with no defined pool (L3980, L3988, L4469).

**The non-parametric posterior, noise-free (exact, conjugate).** A histogram-Dirichlet prior on F (40 cells and an instigator atom)
has an exact posterior given the integer curve: the cell masses are Dirichlet(prior + counts) and, within a cell, F keeps its prior
law. SBC passes (it is exact; the smallest of its 36 KS p-values is 0.005); the information is the point:

| n | M | min KS p of F at the 6 probes | central-90% coverage | posterior sd / prior sd, F inside | same, F outside (above the stall) | readings inside | readings outside |
|---|---|---|---|---|---|---|---|
| 30 | 400 | 0.046 | 0.90 | 0.66 | 0.96 | 736 | 1664 |
| 100 | 400 | 0.478 | 0.91 | 0.45 | 0.97 | 498 | 1902 |
| 300 | 400 | 0.159 | 0.90 | 0.28 | 0.96 | 488 | 1912 |
| 1000 | 400 | 0.381 | 0.91 | 0.21 | 0.98 | 386 | 2014 |
| 3000 | 400 | 0.015 | 0.90 | 0.17 | 0.97 | 418 | 1982 |
| 10000 | 400 | 0.005 | 0.90 | 0.15 | 0.97 | 465 | 1935 |

### 3.2 Question 1: recovering F from the curve when the family is right

**Calibration of the engines (SBC, 094 L4136-L4140, L4153, L4156).** Generator = fitted family, theta drawn on the grid. "Calibrated"
is defined in section 2; the stars in later tables mark a cell that is not.

| family | engine | n | sigma | M | grid | calibrated | min KS p | central-90% coverage range | joint-ll coverage | joint-ll KS p |
|---|---|---|---|---|---|---|---|---|---|---|
| beta | exact | 30 | 0.0 | 1000 | 405 | yes | 0.037 | 0.87-0.91 | 0.90 | 0.285 |
| beta | lattice | 30 | 0.01 | 200 | 405 | yes | 0.141 | 0.85-0.92 | 0.90 | 0.044 |
| beta | lattice | 30 | 0.03 | 200 | 405 | yes | 0.075 | 0.86-0.93 | 0.91 | 0.286 |
| beta | lattice | 30 | 0.1 | 200 | 405 | yes | 0.196 | 0.88-0.93 | 0.90 | 0.683 |
| beta | exact | 100 | 0.0 | 1000 | 405 | yes | 0.207 | 0.87-0.91 | 0.88 | 0.188 |
| beta | sl | 100 | 0.01 | 1000 | 405 | NO | <0.001 | 0.76-0.87 | 0.72 | <0.001 |
| beta | lattice | 100 | 0.03 | 40 | 405 | yes | 0.258 | 0.85-0.95 | 0.93 | 0.471 |
| beta | sl | 100 | 0.03 | 1000 | 405 | NO | <0.001 | 0.82-0.89 | 0.82 | <0.001 |
| beta | lattice | 100 | 0.1 | 40 | 405 | yes | 0.023 | 0.82-0.97 | 0.78 | 0.168 |
| beta | sl | 100 | 0.1 | 1000 | 405 | NO | 0.006 | 0.86-0.91 | 0.85 | <0.001 |
| beta | exact | 300 | 0.0 | 1000 | 405 | yes | 0.032 | 0.89-0.91 | 0.90 | 0.422 |
| beta | sl | 300 | 0.01 | 1000 | 405 | NO | <0.001 | 0.83-0.90 | 0.84 | <0.001 |
| beta | sl | 300 | 0.03 | 1000 | 405 | yes | 0.029 | 0.88-0.91 | 0.88 | 0.002 |
| beta | sl | 300 | 0.1 | 1000 | 405 | yes | 0.101 | 0.89-0.90 | 0.88 | 0.010 |
| beta | exact | 1000 | 0.0 | 1000 | 405 | yes | 0.022 | 0.89-0.91 | 0.90 | 0.194 |
| beta | sl | 1000 | 0.01 | 1000 | 405 | NO | <0.001 | 0.86-0.92 | 0.86 | 0.024 |
| beta | sl | 1000 | 0.03 | 1000 | 405 | yes | 0.069 | 0.88-0.90 | 0.88 | 0.113 |
| beta | sl | 1000 | 0.1 | 1000 | 405 | yes | 0.002 | 0.88-0.90 | 0.88 | 0.066 |
| beta | exact | 3000 | 0.0 | 1000 | 405 | yes | 0.009 | 0.88-0.91 | 0.89 | 0.687 |
| beta | sl | 3000 | 0.01 | 1000 | 405 | yes | 0.143 | 0.87-0.91 | 0.90 | 0.500 |
| beta | sl | 3000 | 0.03 | 1000 | 405 | yes | 0.001 | 0.89-0.91 | 0.90 | 0.129 |
| beta | sl | 3000 | 0.1 | 1000 | 405 | yes | 0.259 | 0.89-0.91 | 0.90 | 0.679 |
| clipnorm | exact | 30 | 0.0 | 1000 | 111 | yes | 0.191 | 0.87-0.90 | 0.90 | 0.005 |
| clipnorm | lattice | 30 | 0.01 | 200 | 111 | yes | 0.023 | 0.88-0.93 | 0.92 | 0.909 |
| clipnorm | lattice | 30 | 0.03 | 200 | 111 | yes | 0.053 | 0.90-0.94 | 0.92 | 0.363 |
| clipnorm | lattice | 30 | 0.1 | 200 | 111 | yes | 0.296 | 0.88-0.93 | 0.90 | 0.911 |
| clipnorm | exact | 100 | 0.0 | 1000 | 111 | yes | 0.081 | 0.88-0.91 | 0.89 | 0.655 |
| clipnorm | sl | 100 | 0.01 | 1000 | 111 | NO | <0.001 | 0.72-0.85 | 0.71 | <0.001 |
| clipnorm | lattice | 100 | 0.03 | 40 | 111 | yes | 0.026 | 0.85-0.95 | 0.80 | 0.722 |
| clipnorm | sl | 100 | 0.03 | 1000 | 111 | NO | <0.001 | 0.79-0.89 | 0.78 | <0.001 |
| clipnorm | lattice | 100 | 0.1 | 40 | 111 | yes | 0.114 | 0.88-1.00 | 0.95 | 0.547 |
| clipnorm | sl | 100 | 0.1 | 1000 | 111 | yes | 0.002 | 0.87-0.91 | 0.88 | 0.003 |
| clipnorm | exact | 300 | 0.0 | 1000 | 111 | yes | 0.397 | 0.88-0.91 | 0.88 | 0.635 |
| clipnorm | sl | 300 | 0.01 | 1000 | 111 | NO | <0.001 | 0.81-0.88 | 0.83 | <0.001 |
| clipnorm | sl | 300 | 0.03 | 1000 | 111 | NO | 0.002 | 0.88-0.91 | 0.86 | 0.029 |
| clipnorm | sl | 300 | 0.1 | 1000 | 111 | yes | 0.083 | 0.88-0.92 | 0.89 | 0.648 |
| clipnorm | exact | 1000 | 0.0 | 1000 | 111 | yes | 0.024 | 0.88-0.92 | 0.88 | 0.472 |
| clipnorm | sl | 1000 | 0.01 | 1000 | 111 | yes | 0.002 | 0.88-0.90 | 0.89 | 0.416 |
| clipnorm | sl | 1000 | 0.03 | 1000 | 111 | NO | 0.109 | 0.86-0.89 | 0.88 | 0.032 |
| clipnorm | sl | 1000 | 0.1 | 1000 | 111 | yes | 0.029 | 0.89-0.91 | 0.89 | 0.258 |
| clipnorm | exact | 3000 | 0.0 | 1000 | 111 | yes | 0.186 | 0.89-0.91 | 0.91 | 0.802 |
| clipnorm | sl | 3000 | 0.01 | 1000 | 111 | yes | 0.020 | 0.88-0.90 | 0.90 | 0.173 |
| clipnorm | sl | 3000 | 0.03 | 1000 | 111 | yes | 0.117 | 0.89-0.91 | 0.90 | 0.902 |
| clipnorm | sl | 3000 | 0.1 | 1000 | 111 | yes | 0.362 | 0.87-0.91 | 0.90 | 0.826 |

**The synthetic engine against the exact one on identical datasets** (same seeds; n = 30 and 100, where the exact lattice engine can
run). This is what the synthetic engine's flags above rest on:

| family | n | sigma | M | lattice calibrated | lattice min KS p | lattice joint-ll c90 | synthetic calibrated | synthetic min KS p | synthetic joint-ll c90 | mean abs diff of posterior mean, tau (prior sd) | same, F(0.55) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| beta | 30 | 0.01 | 200 | yes | 0.141 | 0.90 | NO | <0.001 | 0.60 | 0.17 | 0.31 |
| beta | 30 | 0.03 | 200 | yes | 0.075 | 0.91 | NO | 0.011 | 0.77 | 0.13 | 0.23 |
| beta | 30 | 0.1 | 200 | yes | 0.196 | 0.90 | NO | 0.053 | 0.85 | 0.07 | 0.12 |
| beta | 100 | 0.03 | 40 | yes | 0.258 | 0.93 | yes | 0.112 | 0.78 | 0.10 | 0.16 |
| beta | 100 | 0.1 | 40 | yes | 0.023 | 0.78 | yes | 0.153 | 0.82 | 0.07 | 0.11 |
| clipnorm | 30 | 0.01 | 200 | yes | 0.023 | 0.92 | NO | <0.001 | 0.54 | 0.24 | 0.32 |
| clipnorm | 30 | 0.03 | 200 | yes | 0.053 | 0.92 | NO | <0.001 | 0.76 | 0.19 | 0.26 |
| clipnorm | 30 | 0.1 | 200 | yes | 0.296 | 0.90 | NO | 0.025 | 0.86 | 0.06 | 0.14 |
| clipnorm | 100 | 0.03 | 40 | yes | 0.026 | 0.80 | NO | 0.186 | 0.68 | 0.09 | 0.12 |
| clipnorm | 100 | 0.1 | 40 | yes | 0.114 | 0.95 | yes | 0.346 | 0.88 | 0.04 | 0.06 |


**Information: what the posterior leaves open** (beta+atom, then clipped normal; cells use the exact engine at sigma = 0, the lattice
engine at n = 30 and at n = 100 where it was run, the synthetic engine elsewhere; * = engine not calibrated in that cell). Columns are
the median posterior sd divided by the prior sd (0 = known, 1 = the prior), RMSE of the posterior mean over the prior sd, and the
central-90% coverage of F read inside / outside the visited range. The discrete prior caps the resolution: values near 0.00 mean "to
within a grid cell".

*beta+atom*

| n | sigma | engine | M | params | tau | F(0) | F inside | F outside | RMSE tau | RMSE F inside | RMSE F outside | c90 F inside | c90 F outside | readings outside |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 | 0.0 | exact | 1000 | 0.72 | 0.494 | 0.66 | 0.20 | 0.64 | 0.52 | 0.23 | 0.75 | 0.90 | 0.89 | 54% |
| 30 | 0.01 | lattice | 200 | 0.77 | 0.494 | 0.66 | 0.20 | 0.63 | 0.55 | 0.23 | 0.79 | 0.90 | 0.87 | 57% |
| 30 | 0.03 | lattice | 200 | 0.82 | 0.512 | 0.71 | 0.22 | 0.68 | 0.50 | 0.25 | 0.77 | 0.91 | 0.87 | 57% |
| 30 | 0.1 | lattice | 200 | 0.66 | 0.374 | 0.84 | 0.26 | 0.58 | 0.42 | 0.35 | 0.63 | 0.90 | 0.91 | 26% |
| 100 | 0.0 | exact | 1000 | 0.64 | 0.259 | 0.33 | 0.09 | 0.62 | 0.38 | 0.13 | 0.74 | 0.89 | 0.90 | 60% |
| 100 | 0.01 | sl* | 1000 | 0.58 | 0.050 | 0.37 | 0.12 | 0.44 | 0.42 | 0.18 | 0.75 | 0.83 | 0.78 | 54% |
| 100 | 0.03 | lattice | 40 | 0.72 | 0.381 | 0.45 | 0.14 | 0.66 | 0.47 | 0.17 | 0.63 | 0.94 | 0.88 | 57% |
| 100 | 0.1 | lattice | 40 | 0.60 | 0.190 | 0.69 | 0.20 | 0.56 | 0.13 | 0.24 | 0.59 | 0.90 | 0.98 | 23% |
| 300 | 0.0 | exact | 1000 | 0.36 | 0.072 | 0.15 | 0.02 | 0.55 | 0.27 | 0.05 | 0.69 | 0.91 | 0.88 | 55% |
| 300 | 0.01 | sl* | 1000 | 0.51 | 0.028 | 0.18 | 0.06 | 0.49 | 0.33 | 0.11 | 0.73 | 0.86 | 0.84 | 54% |
| 300 | 0.03 | sl | 1000 | 0.43 | 0.059 | 0.29 | 0.10 | 0.46 | 0.24 | 0.15 | 0.67 | 0.90 | 0.88 | 46% |
| 300 | 0.1 | sl | 1000 | 0.59 | 0.007 | 0.67 | 0.19 | 0.46 | 0.30 | 0.28 | 0.60 | 0.90 | 0.90 | 25% |
| 1000 | 0.0 | exact | 1000 | 0.23 | 0.001 | 0.01 | 0.00 | 0.48 | 0.13 | 0.02 | 0.65 | 0.90 | 0.89 | 54% |
| 1000 | 0.01 | sl* | 1000 | 0.50 | 0.012 | 0.04 | 0.02 | 0.54 | 0.19 | 0.07 | 0.72 | 0.87 | 0.85 | 56% |
| 1000 | 0.03 | sl | 1000 | 0.39 | 0.027 | 0.20 | 0.06 | 0.50 | 0.23 | 0.13 | 0.66 | 0.89 | 0.89 | 46% |
| 1000 | 0.1 | sl | 1000 | 0.57 | 0.003 | 0.61 | 0.16 | 0.47 | 0.21 | 0.26 | 0.64 | 0.89 | 0.87 | 27% |
| 3000 | 0.0 | exact | 1000 | 0.22 | 0.000 | 0.00 | 0.00 | 0.42 | 0.09 | 0.01 | 0.63 | 0.90 | 0.89 | 57% |
| 3000 | 0.01 | sl | 1000 | 0.38 | 0.007 | 0.00 | 0.00 | 0.52 | 0.17 | 0.04 | 0.69 | 0.88 | 0.89 | 56% |
| 3000 | 0.03 | sl | 1000 | 0.35 | 0.006 | 0.15 | 0.04 | 0.51 | 0.23 | 0.12 | 0.67 | 0.91 | 0.90 | 44% |
| 3000 | 0.1 | sl | 1000 | 0.54 | 0.002 | 0.60 | 0.15 | 0.47 | 0.20 | 0.26 | 0.58 | 0.89 | 0.91 | 25% |

*clipped normal*

| n | sigma | engine | M | params | tau | F(0) | F inside | F outside | RMSE tau | RMSE F inside | RMSE F outside | c90 F inside | c90 F outside | readings outside |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 30 | 0.0 | exact | 1000 | 0.34 | 0.032 | 0.45 | 0.26 | 0.89 | 0.66 | 0.28 | 0.99 | 0.88 | 0.88 | 18% |
| 30 | 0.01 | lattice | 200 | 0.34 | 0.027 | 0.47 | 0.26 | 0.98 | 0.62 | 0.28 | 0.91 | 0.89 | 0.91 | 16% |
| 30 | 0.03 | lattice | 200 | 0.36 | 0.032 | 0.47 | 0.28 | 0.81 | 0.56 | 0.29 | 0.89 | 0.92 | 0.92 | 15% |
| 30 | 0.1 | lattice | 200 | 0.51 | 0.030 | 0.60 | 0.36 | 0.81 | 0.45 | 0.42 | 0.70 | 0.90 | 0.98 | 7% |
| 100 | 0.0 | exact | 1000 | 0.19 | 0.012 | 0.23 | 0.14 | 0.73 | 0.57 | 0.15 | 0.88 | 0.89 | 0.88 | 19% |
| 100 | 0.01 | sl* | 1000 | 0.21 | 0.005 | 0.22 | 0.13 | 0.36 | 0.56 | 0.21 | 1.08 | 0.83 | 0.62 | 15% |
| 100 | 0.03 | lattice | 40 | 0.22 | 0.010 | 0.26 | 0.17 | 0.88 | 0.60 | 0.20 | 1.01 | 0.88 | 1.00 | 10% |
| 100 | 0.1 | lattice | 40 | 0.42 | 0.024 | 0.43 | 0.31 | 0.49 | 0.29 | 0.34 | 0.25 | 0.91 | 1.00 | 6% |
| 300 | 0.0 | exact | 1000 | 0.08 | 0.001 | 0.11 | 0.06 | 0.48 | 0.41 | 0.08 | 0.73 | 0.89 | 0.88 | 18% |
| 300 | 0.01 | sl* | 1000 | 0.13 | 0.003 | 0.15 | 0.08 | 0.39 | 0.53 | 0.13 | 0.80 | 0.87 | 0.75 | 18% |
| 300 | 0.03 | sl* | 1000 | 0.21 | 0.006 | 0.20 | 0.13 | 0.42 | 0.44 | 0.17 | 0.77 | 0.91 | 0.84 | 14% |
| 300 | 0.1 | sl | 1000 | 0.42 | 0.017 | 0.40 | 0.29 | 0.62 | 0.27 | 0.34 | 0.75 | 0.90 | 0.91 | 6% |
| 1000 | 0.0 | exact | 1000 | 0.01 | 0.000 | 0.03 | 0.00 | 0.27 | 0.29 | 0.03 | 0.50 | 0.90 | 0.91 | 18% |
| 1000 | 0.01 | sl | 1000 | 0.05 | 0.001 | 0.06 | 0.03 | 0.28 | 0.34 | 0.07 | 0.66 | 0.90 | 0.86 | 16% |
| 1000 | 0.03 | sl* | 1000 | 0.16 | 0.004 | 0.13 | 0.08 | 0.35 | 0.38 | 0.15 | 0.75 | 0.89 | 0.82 | 13% |
| 1000 | 0.1 | sl | 1000 | 0.40 | 0.015 | 0.39 | 0.27 | 0.49 | 0.23 | 0.32 | 0.71 | 0.90 | 0.92 | 6% |
| 3000 | 0.0 | exact | 1000 | 0.00 | 0.000 | 0.00 | 0.00 | 0.12 | 0.14 | 0.01 | 0.38 | 0.90 | 0.90 | 16% |
| 3000 | 0.01 | sl | 1000 | 0.01 | 0.000 | 0.02 | 0.00 | 0.19 | 0.22 | 0.04 | 0.59 | 0.90 | 0.88 | 16% |
| 3000 | 0.03 | sl | 1000 | 0.14 | 0.002 | 0.10 | 0.06 | 0.40 | 0.28 | 0.14 | 0.70 | 0.90 | 0.89 | 15% |
| 3000 | 0.1 | sl | 1000 | 0.40 | 0.016 | 0.39 | 0.26 | 0.47 | 0.28 | 0.32 | 0.76 | 0.89 | 0.86 | 7% |

**Where recovery fails** (smallest n from which the median relative posterior sd stays below the criterion; "never" = not at n = 3,000;
star = rests on an uncalibrated cell):

| family | sigma | tau (< 0.05 of prior sd) | parameters (< 0.25 of prior sd) | F inside (< 0.25 of prior sd) | F outside (< 0.25 of prior sd) |
|---|---|---|---|---|---|
| beta | 0.0 | >= 1000 | >= 1000 | >= 30 | never |
| beta | 0.01 | >= 100* | never | >= 30* | never |
| beta | 0.03 | >= 1000 | never | >= 30 | never |
| beta | 0.1 | >= 300 | never | >= 100 | never |
| clipnorm | 0.0 | >= 30 | >= 100 | >= 100 | >= 3000 |
| clipnorm | 0.01 | >= 30* | >= 100* | >= 100* | >= 3000 |
| clipnorm | 0.03 | >= 30* | >= 100* | >= 100* | never |
| clipnorm | 0.1 | >= 30 | never | never | never |

**Reading.**

- *Calibration.* The exact engine passes in 10 of 10 cells and the lattice engine in 10 of 10 (the n = 100 cells have 40 datasets each, so
  little power there). The synthetic engine passes in 14 of 24; the cells where it does not are beta+atom (100, 0.01), (100, 0.03), (100, 0.1), (300, 0.01), (1000, 0.01); clipped normal (100, 0.01), (100, 0.03), (300, 0.01), (300, 0.03), (1000, 0.03) (family (n, sigma)); the worst central-90% coverage among
  them is 0.72. Against the exact lattice engine on identical datasets it fails in 6 of 6 cells at n = 30 and its posterior means differ from the exact ones by
  0.04-0.24 (tau) and 0.06-0.32 (F(0.55)) prior sds on average. So the synthetic engine is used as an approximation, flagged with a star where it is not calibrated;
  everything in this section at n <= 100 with noise rests on the lattice engine, except n = 100 with sigma = 0.01, which has only a flagged synthetic cell
  (sections 3.3 and 3.5 use the synthetic engine at every n with sigma > 0, without stars; section 2, Engines).
- *Exact counts.* The stall is read to within a twentieth of its prior sd from n = 1,000 for beta+atom (median posterior sd of tau 0.072 at n = 300, 0.001 at n = 1,000) and at every n for the clipped normal
  (0.032 at n = 30); F inside the visited range to within a quarter of its prior sd from n = 30 for beta+atom (0.20; 0.09 at n = 100) and from n = 100 for the clipped normal (0.14). The two parameters of the clipped normal are recovered from n = 100 (0.19) to n = 1,000 (0.01); the
  three of beta+atom are still at 0.23 and 0.22 of the prior sd at n = 1,000 and 3,000: many (z, a, b) give nearly the same few points.
  F outside the visited range is the part that stays open: 0.42 (beta+atom) and 0.12 (clipped normal) at n = 3,000, with an RMSE of the posterior mean of
  0.63 and 0.38 prior sds.
- *At sigma >= 0.03 noise sets a floor that n barely lifts.* At sigma = 0.03 the parameters stay at 0.43, 0.39, 0.35 (beta+atom, n = 300, 1,000, 3,000) and at sigma = 0.1 at
  0.59, 0.57, 0.54; for the clipped normal 0.42, 0.40, 0.40 at sigma = 0.1. The first-share F(0) is
  limited by sigma itself (0.60 at sigma = 0.1). There, beyond a few hundred members a larger crowd helps little and less noisy counts help more; at sigma = 0.01
  n still helps (clipped normal 0.13*, 0.05, 0.01 at n = 300, 1,000, 3,000; corrected at review: this bullet said a larger crowd does not help at all).
- *Small crowds.* At n = 30 even exact counts leave the stall of a beta+atom crowd open (0.49 of the prior sd; 0.26 at n = 100): the finite crowd's own luck, not the observer's noise, decides where it stops.
- *The intervals are honest.* In the calibrated cells with n >= 300 the central-90% coverage of F is 0.88-0.91 inside and
  0.86-0.92 outside the visited range: the width outside is information, not a calculation error.
  A correct parametric family does not make F identifiable outside the visited range, it makes it an assumption with a calibrated width.

### 3.3 Question 1 under independent generators: the wrong family, and which family the curve prefers

Curves from beta+atom, clipped-normal, logit-normal and **bimodal** crowds (continuous parameters), each fitted by all three fitted
families. Detail at n = 1,000, sigma = 0.03, then pooled over cells ("matched" = generator and fitted family the same). **At sigma = 0 and
large n the matched rows lose coverage because the continuous truth falls between grid points (the posterior is narrower than the
grid), not because the fit is wrong; read the mismatched rows against the matched ones in the same row of the pooled table.**

| generator | fitted |  | tau cov90 | F(0) cov90 | F inside cov90 | F outside cov90 | F inside RMSE | F outside RMSE | F outside post sd | share where it has the largest marginal likelihood |
|---|---|---|---|---|---|---|---|---|---|---|
| beta | beta | matched | 0.86 | 0.64 | 0.86 | 0.83 | 0.13 | 0.68 | 0.50 | 0.61 |
| beta | clipnorm | - | 0.77 | 0.37 | 0.49 | 0.28 | 0.31 | 2.23 | 0.36 | 0.26 |
| beta | logitnorm | - | 0.86 | 0.64 | 0.81 | 0.77 | 0.14 | 1.61 | 0.87 | 0.13 |
| clipnorm | beta | - | 0.65 | 0.45 | 0.49 | 0.74 | 0.24 | 0.65 | 0.35 | 0.10 |
| clipnorm | clipnorm | matched | 0.94 | 0.89 | 0.91 | 0.84 | 0.17 | 0.83 | 0.39 | 0.81 |
| clipnorm | logitnorm | - | 0.65 | 0.50 | 0.78 | 0.81 | 0.19 | 0.77 | 0.68 | 0.09 |
| bimodal | beta | - | 0.72 | 0.53 | 0.37 | 0.52 | 0.39 | 0.80 | 0.28 | 0.41 |
| bimodal | clipnorm | - | 0.48 | 0.27 | 0.28 | 0.36 | 0.67 | 2.09 | 0.25 | 0.14 |
| bimodal | logitnorm | - | 0.81 | 0.63 | 0.48 | 0.62 | 0.48 | 1.41 | 0.63 | 0.45 |
| logitnorm | beta | - | 0.92 | 0.54 | 0.48 | 0.65 | 0.34 | 0.93 | 0.45 | 0.39 |
| logitnorm | clipnorm | - | 0.80 | 0.45 | 0.48 | 0.27 | 0.37 | 1.63 | 0.30 | 0.32 |
| logitnorm | logitnorm | matched | 0.93 | 0.66 | 0.84 | 0.87 | 0.20 | 0.82 | 0.82 | 0.29 |

Pooled over the generator-by-family pairs (matched: beta+atom, clipped normal and logit-normal fitted to themselves; mismatched: all
other pairs, which include everything fitted to the bimodal generator):

| n | sigma | matched: tau cov | matched: F in cov | matched: F out cov | matched: F in RMSE | matched: F out RMSE | mismatched: tau cov | mismatched: F in cov | mismatched: F out cov | mismatched: F in RMSE | mismatched: F out RMSE | matched family wins (mean) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 100 | 0.0 | 0.95 | 0.86 | 0.92 | 0.13 | 0.82 | 0.81 | 0.55 | 0.67 | 0.29 | 1.35 | 0.66 |
| 1000 | 0.0 | 0.80 | 0.48 | 0.87 | 0.08 | 0.63 | 0.59 | 0.19 | 0.44 | 0.25 | 1.36 | 0.73 |
| 3000 | 0.0 | 0.65 | 0.28 | 0.77 | 0.08 | 0.59 | 0.48 | 0.09 | 0.32 | 0.27 | 1.39 | 0.74 |
| 300 | 0.01 | 0.88 | 0.83 | 0.83 | 0.14 | 0.80 | 0.71 | 0.43 | 0.55 | 0.43 | 1.46 | 0.63 |
| 1000 | 0.01 | 0.85 | 0.71 | 0.83 | 0.11 | 0.72 | 0.66 | 0.34 | 0.55 | 0.38 | 1.35 | 0.64 |
| 3000 | 0.01 | 0.79 | 0.58 | 0.80 | 0.10 | 0.71 | 0.63 | 0.23 | 0.50 | 0.34 | 1.36 | 0.64 |
| 300 | 0.03 | 0.92 | 0.88 | 0.85 | 0.18 | 0.76 | 0.76 | 0.60 | 0.59 | 0.39 | 1.37 | 0.59 |
| 1000 | 0.03 | 0.91 | 0.87 | 0.85 | 0.17 | 0.78 | 0.74 | 0.52 | 0.56 | 0.35 | 1.35 | 0.57 |
| 3000 | 0.03 | 0.88 | 0.80 | 0.86 | 0.15 | 0.72 | 0.70 | 0.45 | 0.54 | 0.32 | 1.29 | 0.60 |
| 300 | 0.1 | 0.97 | 0.93 | 0.90 | 0.30 | 0.66 | 0.84 | 0.75 | 0.64 | 0.40 | 1.23 | 0.46 |
| 1000 | 0.1 | 0.96 | 0.93 | 0.94 | 0.29 | 0.71 | 0.80 | 0.71 | 0.59 | 0.40 | 1.21 | 0.49 |
| 3000 | 0.1 | 0.96 | 0.92 | 0.90 | 0.29 | 0.65 | 0.79 | 0.69 | 0.60 | 0.39 | 1.18 | 0.48 |

Model recovery: the share of curves for which each fitted family has the largest marginal likelihood (a perfect instrument would put
1.00 on the generating family; the bimodal generator has no matching family):

| n | sigma | generated by | M | fitted best: beta | fitted best: clipnorm | fitted best: logitnorm |
|---|---|---|---|---|---|---|
| 100 | 0.0 | beta | 400 | 0.76 | 0.16 | 0.08 |
| 100 | 0.0 | clipnorm | 400 | 0.06 | 0.87 | 0.07 |
| 100 | 0.0 | bimodal | 400 | 0.43 | 0.08 | 0.49 |
| 100 | 0.0 | logitnorm | 400 | 0.47 | 0.18 | 0.35 |
| 1000 | 0.0 | beta | 400 | 0.86 | 0.06 | 0.08 |
| 1000 | 0.0 | clipnorm | 400 | 0.02 | 0.93 | 0.05 |
| 1000 | 0.0 | bimodal | 400 | 0.43 | 0.03 | 0.54 |
| 1000 | 0.0 | logitnorm | 400 | 0.53 | 0.07 | 0.39 |
| 3000 | 0.0 | beta | 400 | 0.84 | 0.07 | 0.10 |
| 3000 | 0.0 | clipnorm | 400 | 0.01 | 0.94 | 0.05 |
| 3000 | 0.0 | bimodal | 400 | 0.47 | 0.01 | 0.52 |
| 3000 | 0.0 | logitnorm | 400 | 0.47 | 0.08 | 0.44 |
| 300 | 0.01 | beta | 400 | 0.78 | 0.17 | 0.06 |
| 300 | 0.01 | clipnorm | 400 | 0.08 | 0.87 | 0.04 |
| 300 | 0.01 | bimodal | 400 | 0.57 | 0.10 | 0.33 |
| 300 | 0.01 | logitnorm | 400 | 0.54 | 0.23 | 0.23 |
| 1000 | 0.01 | beta | 400 | 0.77 | 0.15 | 0.09 |
| 1000 | 0.01 | clipnorm | 400 | 0.07 | 0.84 | 0.08 |
| 1000 | 0.01 | bimodal | 400 | 0.49 | 0.08 | 0.43 |
| 1000 | 0.01 | logitnorm | 400 | 0.51 | 0.18 | 0.31 |
| 3000 | 0.01 | beta | 400 | 0.74 | 0.14 | 0.11 |
| 3000 | 0.01 | clipnorm | 400 | 0.08 | 0.86 | 0.06 |
| 3000 | 0.01 | bimodal | 400 | 0.48 | 0.08 | 0.44 |
| 3000 | 0.01 | logitnorm | 400 | 0.51 | 0.17 | 0.32 |
| 300 | 0.03 | beta | 400 | 0.67 | 0.25 | 0.08 |
| 300 | 0.03 | clipnorm | 400 | 0.12 | 0.80 | 0.08 |
| 300 | 0.03 | bimodal | 400 | 0.40 | 0.19 | 0.41 |
| 300 | 0.03 | logitnorm | 400 | 0.42 | 0.28 | 0.29 |
| 1000 | 0.03 | beta | 400 | 0.61 | 0.26 | 0.13 |
| 1000 | 0.03 | clipnorm | 400 | 0.10 | 0.81 | 0.09 |
| 1000 | 0.03 | bimodal | 400 | 0.41 | 0.14 | 0.45 |
| 1000 | 0.03 | logitnorm | 400 | 0.39 | 0.32 | 0.29 |
| 3000 | 0.03 | beta | 400 | 0.66 | 0.19 | 0.15 |
| 3000 | 0.03 | clipnorm | 400 | 0.09 | 0.81 | 0.11 |
| 3000 | 0.03 | bimodal | 400 | 0.41 | 0.12 | 0.47 |
| 3000 | 0.03 | logitnorm | 400 | 0.46 | 0.21 | 0.33 |
| 300 | 0.1 | beta | 400 | 0.36 | 0.42 | 0.22 |
| 300 | 0.1 | clipnorm | 400 | 0.08 | 0.74 | 0.17 |
| 300 | 0.1 | bimodal | 400 | 0.18 | 0.33 | 0.49 |
| 300 | 0.1 | logitnorm | 400 | 0.25 | 0.47 | 0.28 |
| 1000 | 0.1 | beta | 400 | 0.35 | 0.40 | 0.25 |
| 1000 | 0.1 | clipnorm | 400 | 0.06 | 0.78 | 0.17 |
| 1000 | 0.1 | bimodal | 400 | 0.17 | 0.33 | 0.49 |
| 1000 | 0.1 | logitnorm | 400 | 0.20 | 0.46 | 0.34 |
| 3000 | 0.1 | beta | 400 | 0.34 | 0.40 | 0.26 |
| 3000 | 0.1 | clipnorm | 400 | 0.10 | 0.76 | 0.14 |
| 3000 | 0.1 | bimodal | 400 | 0.25 | 0.27 | 0.48 |
| 3000 | 0.1 | logitnorm | 400 | 0.24 | 0.41 | 0.35 |

**Reading** (pooled over the cells with sigma > 0):

- *A wrong family is fitted confidently and wrongly.* The 90% interval of F covers the truth for 0.52 of readings inside the visited range and 0.57 outside when the family is wrong, against
  0.83 and 0.86 when it matches; the RMSE of the posterior mean outside is 1.31 prior sds against 0.72. Coverage inside falls as the data get cleaner, for both
  (sigma = 0.01, 0.03, 0.1: mismatched 0.33, 0.52, 0.72; matched 0.71, 0.85, 0.92), because the posterior narrows toward the grid spacing
  and, at sigma = 0.01 with n <= 1,000, because the synthetic engine is itself over-confident there (3.2); it falls much further when the family is wrong.
  The error is in the visited range too, not only above it: a family is a constraint on the whole of F.
- *The curve cannot say which family it is.* By marginal likelihood the generating family comes out first for 0.74-0.87 of clipped-normal curves, 0.34-0.78 of beta+atom curves and 0.23-0.35 of
  logit-normal curves (chance 0.33). With exact counts the clipped normal and beta+atom are recognised 0.87-0.94 and 0.76-0.86 of the time, the logit-normal 0.35-0.44. Noise degrades it
  further: at n = 1,000, sigma = 0.1 beta+atom curves are attributed to the clipped normal more often than to beta+atom. Bimodal crowds, which have no matching family, are attributed to logit-normal
  (0.33-0.54) or beta+atom (0.17-0.57) and least often to the clipped normal (0.01-0.33); the preferred family is not a diagnosis of the crowd.
- *At sigma = 0 and large n the matched coverage is a grid artefact* (matched F-inside coverage 0.86 at n = 100, 0.48 at n = 1,000, 0.28 at n = 3,000; mismatched 0.55, 0.19, 0.09): the
  truth falls between grid points. The RMSE columns carry the comparison there.

*The engine behind these rows* (added at review). The cells above with sigma > 0 fit with the synthetic engine on the fine grids with S = 1,000,
which no SBC cell of 3.2 checked. Here is SBC of exactly those setups (same setup seeds), the truth drawn on the fine grid:

| family | n | sigma | M | grid | calibrated | min KS p | central-90% coverage range | joint-ll coverage | joint-ll KS p | c90 F inside | c90 F outside |
|---|---|---|---|---|---|---|---|---|---|---|---|
| beta | 300 | 0.01 | 400 | 864 | NO | 0.001 | 0.82-0.90 | 0.81 | <0.001 | 0.86 | 0.84 |
| beta | 1000 | 0.01 | 400 | 864 | yes | 0.190 | 0.86-0.92 | 0.88 | 0.206 | 0.90 | 0.87 |
| beta | 3000 | 0.01 | 400 | 864 | NO | <0.001 | 0.87-0.90 | 0.91 | 0.239 | 0.89 | 0.88 |
| beta | 300 | 0.03 | 400 | 864 | yes | 0.220 | 0.85-0.93 | 0.86 | 0.012 | 0.90 | 0.86 |
| beta | 1000 | 0.03 | 400 | 864 | yes | 0.011 | 0.88-0.92 | 0.89 | 0.229 | 0.89 | 0.91 |
| beta | 3000 | 0.03 | 400 | 864 | yes | 0.024 | 0.88-0.91 | 0.88 | 0.444 | 0.89 | 0.90 |
| beta | 300 | 0.1 | 400 | 864 | yes | 0.315 | 0.88-0.92 | 0.89 | 0.457 | 0.90 | 0.89 |
| beta | 1000 | 0.1 | 400 | 864 | yes | 0.014 | 0.89-0.93 | 0.88 | 0.935 | 0.92 | 0.89 |
| beta | 3000 | 0.1 | 400 | 864 | yes | 0.177 | 0.88-0.92 | 0.90 | 0.120 | 0.90 | 0.87 |
| clipnorm | 300 | 0.01 | 400 | 441 | NO | 0.002 | 0.78-0.86 | 0.79 | <0.001 | 0.85 | 0.71 |
| clipnorm | 1000 | 0.01 | 400 | 441 | yes | 0.022 | 0.85-0.91 | 0.86 | 0.058 | 0.87 | 0.90 |
| clipnorm | 3000 | 0.01 | 400 | 441 | NO | <0.001 | 0.88-0.93 | 0.87 | 0.304 | 0.92 | 0.90 |
| clipnorm | 300 | 0.03 | 400 | 441 | NO | <0.001 | 0.83-0.89 | 0.83 | <0.001 | 0.87 | 0.78 |
| clipnorm | 1000 | 0.03 | 400 | 441 | yes | 0.087 | 0.89-0.92 | 0.88 | 0.680 | 0.91 | 0.87 |
| clipnorm | 3000 | 0.03 | 400 | 441 | yes | 0.278 | 0.89-0.91 | 0.89 | 0.218 | 0.90 | 0.87 |
| clipnorm | 300 | 0.1 | 400 | 441 | yes | 0.338 | 0.88-0.93 | 0.88 | 0.698 | 0.91 | 0.93 |
| clipnorm | 1000 | 0.1 | 400 | 441 | yes | 0.384 | 0.90-0.93 | 0.90 | 0.887 | 0.91 | 0.90 |
| clipnorm | 3000 | 0.1 | 400 | 441 | yes | 0.252 | 0.89-0.94 | 0.90 | 0.333 | 0.92 | 0.89 |
| logitnorm | 300 | 0.01 | 400 | 840 | NO | 0.001 | 0.80-0.89 | 0.77 | <0.001 | 0.86 | 0.81 |
| logitnorm | 1000 | 0.01 | 400 | 840 | NO | <0.001 | 0.82-0.90 | 0.80 | <0.001 | 0.85 | 0.86 |
| logitnorm | 3000 | 0.01 | 400 | 840 | yes | 0.126 | 0.86-0.93 | 0.89 | 0.168 | 0.90 | 0.88 |
| logitnorm | 300 | 0.03 | 400 | 840 | NO | 0.017 | 0.86-0.90 | 0.83 | <0.001 | 0.88 | 0.85 |
| logitnorm | 1000 | 0.03 | 400 | 840 | NO | 0.026 | 0.86-0.93 | 0.84 | 0.138 | 0.88 | 0.90 |
| logitnorm | 3000 | 0.03 | 400 | 840 | yes | 0.018 | 0.89-0.92 | 0.86 | 0.380 | 0.90 | 0.91 |
| logitnorm | 300 | 0.1 | 400 | 840 | yes | 0.321 | 0.87-0.93 | 0.87 | 0.603 | 0.90 | 0.90 |
| logitnorm | 1000 | 0.1 | 400 | 840 | yes | 0.061 | 0.88-0.92 | 0.86 | 0.192 | 0.89 | 0.89 |
| logitnorm | 3000 | 0.1 | 400 | 840 | yes | 0.024 | 0.87-0.92 | 0.86 | 0.179 | 0.89 | 0.85 |

It passes in 18 of 27; the cells where it does not are beta+atom (300, 0.01), (3000, 0.01); clipped normal (300, 0.01), (300, 0.03), (3000, 0.01); logit-normal (300, 0.01), (300, 0.03), (1000, 0.01), (1000, 0.03) (family (n, sigma)), worst
central-90% coverage 0.78 and worst joint-likelihood coverage 0.77. So part of the matched rows' under-coverage at those
cells is the engine's; elsewhere, where every quantity (F(0) included) is covered 0.85 to 0.94 with the truth on the grid,
what the matched rows lose is the continuous truth falling between grid values. The low matched F(0) coverage of the detail table has the same cause
(0.64 for beta+atom and 0.66 for logit-normal, whose F(0) is z itself on a grid of six values, against 0.89 for the clipped normal): in the
same setups with the truth on the grid, F(0) is covered 0.89 and 0.93 (n = 1,000, sigma = 0.03), and an interval made of grid values covers a
continuous truth only when the posterior straddles it. The mismatched-against-matched comparison is made within the same cells and engine.

### 3.4 Question 2: a two-sided gate from aggregate curves

The null is a non-decreasing latent curve (a one-sided gate). The ceiling for any detector working on a single current-share curve is the
share of two-sided crowds whose noise-free curve declines at all (Proposition A); the order test and the any-drop rule are the two
detectors; the one-sided control crowds give their false-positive rates; the last two columns are the ever-joined curve.

| share with upper gate | gate width | n | sigma | M | current share declines (noise-free) | a step decline >= 3 sigma sqrt2 | power: order test | power: any-drop rule | false positive: order test | false positive: any-drop rule | ever-joined curve: order-test rejection | ever-joined curve: plateau then growth (noise-free) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0.6 | 0.5 | 100 | 0.01 | 500 | 0.57 | 0.45 | 0.52 | 0.53 | 0.03 | 0.04 | 0.03 | 0.12 |
| 0.6 | 0.5 | 100 | 0.03 | 500 | 0.55 | 0.31 | 0.38 | 0.38 | 0.03 | 0.04 | 0.03 | 0.09 |
| 0.6 | 0.5 | 100 | 0.1 | 500 | 0.56 | 0.12 | 0.30 | 0.28 | 0.02 | 0.04 | 0.02 | 0.14 |
| 0.6 | 0.5 | 1000 | 0.01 | 500 | 0.64 | 0.43 | 0.47 | 0.47 | 0.02 | 0.02 | 0.01 | 0.22 |
| 0.6 | 0.5 | 1000 | 0.03 | 500 | 0.58 | 0.34 | 0.39 | 0.37 | 0.03 | 0.03 | 0.02 | 0.20 |
| 0.6 | 0.5 | 1000 | 0.1 | 500 | 0.58 | 0.10 | 0.26 | 0.25 | 0.02 | 0.04 | 0.03 | 0.19 |
| 0.3 | 0.15 | 100 | 0.01 | 500 | 0.41 | 0.06 | 0.14 | 0.15 | 0.02 | 0.03 | 0.03 | 0.01 |
| 0.3 | 0.15 | 100 | 0.03 | 500 | 0.43 | 0.01 | 0.07 | 0.09 | 0.02 | 0.03 | 0.02 | 0.01 |
| 0.3 | 0.15 | 100 | 0.1 | 500 | 0.40 | 0.00 | 0.03 | 0.04 | 0.01 | 0.02 | 0.02 | 0.01 |
| 0.3 | 0.15 | 1000 | 0.01 | 500 | 0.60 | 0.06 | 0.14 | 0.16 | 0.02 | 0.02 | 0.03 | 0.00 |
| 0.3 | 0.15 | 1000 | 0.03 | 500 | 0.56 | 0.00 | 0.06 | 0.08 | 0.02 | 0.03 | 0.02 | 0.00 |
| 0.3 | 0.15 | 1000 | 0.1 | 500 | 0.58 | 0.00 | 0.03 | 0.03 | 0.03 | 0.03 | 0.02 | 0.00 |
| 0.3 | 0.5 | 100 | 0.01 | 500 | 0.50 | 0.31 | 0.38 | 0.39 | 0.03 | 0.03 | 0.02 | 0.01 |
| 0.3 | 0.5 | 100 | 0.03 | 500 | 0.51 | 0.21 | 0.27 | 0.28 | 0.01 | 0.03 | 0.02 | 0.02 |
| 0.3 | 0.5 | 100 | 0.1 | 500 | 0.51 | 0.00 | 0.07 | 0.07 | 0.02 | 0.02 | 0.04 | 0.01 |
| 0.3 | 0.5 | 1000 | 0.01 | 500 | 0.57 | 0.33 | 0.37 | 0.39 | 0.03 | 0.04 | 0.01 | 0.00 |
| 0.3 | 0.5 | 1000 | 0.03 | 500 | 0.56 | 0.16 | 0.18 | 0.21 | 0.02 | 0.03 | 0.02 | 0.00 |
| 0.3 | 0.5 | 1000 | 0.1 | 500 | 0.59 | 0.00 | 0.04 | 0.06 | 0.03 | 0.04 | 0.02 | 0.01 |
| 0.1 | 0.5 | 100 | 0.01 | 500 | 0.36 | 0.11 | 0.15 | 0.20 | 0.02 | 0.03 | 0.03 | 0.00 |
| 0.1 | 0.5 | 100 | 0.03 | 500 | 0.35 | 0.01 | 0.08 | 0.10 | 0.02 | 0.03 | 0.03 | 0.00 |
| 0.1 | 0.5 | 100 | 0.1 | 500 | 0.37 | 0.00 | 0.03 | 0.04 | 0.03 | 0.04 | 0.01 | 0.00 |
| 0.1 | 0.5 | 1000 | 0.01 | 500 | 0.48 | 0.12 | 0.18 | 0.19 | 0.02 | 0.03 | 0.02 | 0.00 |
| 0.1 | 0.5 | 1000 | 0.03 | 500 | 0.45 | 0.00 | 0.03 | 0.06 | 0.03 | 0.05 | 0.02 | 0.00 |
| 0.1 | 0.5 | 1000 | 0.1 | 500 | 0.42 | 0.00 | 0.02 | 0.03 | 0.02 | 0.05 | 0.02 | 0.00 |

**Reading.**

- *The ceiling is high and the detectors reach little of it.* 35% to 64% of two-sided crowds decline somewhere in the noise-free curve, but a decline that
  stands out of the noise (a single step of 3 sigma sqrt 2) occurs in 0% to 45% and the order test detects 2% to 52%: power follows the share of material
  declines, not the share of declines. It is best with many wide-windowed members (nu = 0.6: 26% to 52%) and exact-ish counts (sigma = 0.01), and
  falls to 7% or less at sigma = 0.1 unless 60% of the members are gated.
- *No false alarms.* One-sided control crowds are rejected at 1% to 3% (order test) and 2% to 5% (any-drop rule) against a nominal 5%;
  both are conservative because the critical value is for the flat curve, the least favourable null.
- *Which detector.* The two agree within 4 points everywhere; the order test is the more powerful in 0 cells and the any-drop rule in 4 of 24 (by more than 2 points). Neither wins.
- *The cumulative curve.* The order test rejects the ever-joined curve at its size (1% to 4%): it cannot decline. Its plateau-then-growth trace exists in 0% to
  22% of crowds (most with nu = 0.6, wide windows, n = 1,000); no detector for it under noise was built.
- *What this means.* Nothing in a monotone curve, or in the stall level, separates the gates. A two-sided gate is **testable** only where it makes the crowd visibly shrink and the count error is a few percent.

### 3.5 Question 3: predicting ignition from the parts' curves

Prevalence is of strict realised ignition among eligible pairs; AUC with a 95% bootstrap interval (200 resamples); 0.5 = no skill.
"Brier skill" is 1 minus the Brier score over the base-rate score (0 = no better than the base rate).

| generators | n | sigma | pairs | igniting | AUC known-F margin | AUC curve summaries | AUC fitted model, natural runs | Brier skill of it | AUC adaptive probe |
|---|---|---|---|---|---|---|---|---|---|
| matched (beta, clipped normal) | 100 | 0.0 | 2000 | 237 (12%) | 0.72 [0.69, 0.77] | 0.69 [0.66, 0.72] | 0.76 [0.72, 0.78] | +0.05 | 0.90 [0.89, 0.91] |
| matched (beta, clipped normal) | 300 | 0.0 | 2000 | 169 (8%) | 0.76 [0.72, 0.81] | 0.72 [0.68, 0.77] | 0.82 [0.79, 0.85] | +0.16 | 0.84 [0.82, 0.86] |
| matched (beta, clipped normal) | 1000 | 0.0 | 2000 | 158 (8%) | 0.88 [0.84, 0.91] | 0.77 [0.74, 0.80] | 0.85 [0.82, 0.89] | +0.24 | 0.83 [0.81, 0.85] |
| matched (beta, clipped normal) | 3000 | 0.0 | 2000 | 131 (7%) | 0.92 [0.89, 0.96] | 0.78 [0.74, 0.82] | 0.85 [0.81, 0.89] | +0.31 | 0.82 [0.79, 0.84] |
| matched (beta, clipped normal) | 100 | 0.03 | 2000 | 216 (11%) | 0.71 [0.67, 0.75] | 0.63 [0.58, 0.67] | 0.71 [0.67, 0.75] | +0.01 | 0.72 [0.68, 0.75] |
| matched (beta, clipped normal) | 300 | 0.03 | 2000 | 194 (10%) | 0.80 [0.76, 0.84] | 0.71 [0.68, 0.74] | 0.77 [0.74, 0.81] | +0.06 | 0.72 [0.68, 0.75] |
| matched (beta, clipped normal) | 1000 | 0.03 | 2000 | 202 (10%) | 0.86 [0.83, 0.89] | 0.73 [0.70, 0.76] | 0.80 [0.78, 0.83] | +0.09 | 0.72 [0.69, 0.75] |
| matched (beta, clipped normal) | 3000 | 0.03 | 2000 | 175 (9%) | 0.92 [0.89, 0.95] | 0.77 [0.74, 0.81] | 0.79 [0.75, 0.82] | +0.12 | 0.70 [0.66, 0.73] |
| other (bimodal, logit-normal) | 100 | 0.0 | 2000 | 490 (24%) | 0.80 [0.77, 0.82] | 0.74 [0.71, 0.76] | 0.76 [0.74, 0.78] | -0.06 | 0.92 [0.91, 0.93] |
| other (bimodal, logit-normal) | 300 | 0.0 | 2000 | 443 (22%) | 0.86 [0.83, 0.88] | 0.75 [0.72, 0.77] | 0.77 [0.74, 0.79] | -0.02 | 0.91 [0.90, 0.92] |
| other (bimodal, logit-normal) | 1000 | 0.0 | 2000 | 431 (22%) | 0.91 [0.89, 0.93] | 0.76 [0.74, 0.78] | 0.78 [0.76, 0.80] | -0.00 | 0.90 [0.88, 0.91] |
| other (bimodal, logit-normal) | 3000 | 0.0 | 2000 | 380 (19%) | 0.95 [0.94, 0.97] | 0.76 [0.74, 0.78] | 0.77 [0.74, 0.79] | -0.03 | 0.90 [0.88, 0.91] |
| other (bimodal, logit-normal) | 100 | 0.03 | 2000 | 466 (23%) | 0.82 [0.79, 0.84] | 0.73 [0.71, 0.76] | 0.62 [0.59, 0.65] | -0.19 | 0.86 [0.84, 0.88] |
| other (bimodal, logit-normal) | 300 | 0.03 | 2000 | 393 (20%) | 0.83 [0.80, 0.86] | 0.74 [0.72, 0.76] | 0.64 [0.61, 0.67] | -0.09 | 0.84 [0.82, 0.86] |
| other (bimodal, logit-normal) | 1000 | 0.03 | 2000 | 405 (20%) | 0.89 [0.87, 0.92] | 0.75 [0.72, 0.77] | 0.73 [0.70, 0.75] | +0.00 | 0.83 [0.81, 0.85] |
| other (bimodal, logit-normal) | 3000 | 0.03 | 2000 | 324 (16%) | 0.95 [0.93, 0.96] | 0.77 [0.74, 0.79] | 0.79 [0.77, 0.82] | +0.08 | 0.83 [0.81, 0.85] |

*Material ignition (the merge stalls at least 2% of the crowd higher), same predictors:*

| generators | n | sigma | run | material ignitions (>= 2% of the crowd) | AUC known-F margin | AUC curve summaries | AUC fitted model, natural runs | AUC adaptive probe | AUC fitted model + 4 seeded runs |
|---|---|---|---|---|---|---|---|---|---|
| matched | 100 | 0.0 | nat | 202 (10%) | 0.73 [0.69, 0.78] | 0.73 [0.69, 0.75] | 0.79 [0.77, 0.83] | 0.92 [0.90, 0.93] | - |
| matched | 300 | 0.0 | nat | 118 (6%) | 0.77 [0.72, 0.83] | 0.76 [0.72, 0.80] | 0.88 [0.84, 0.90] | 0.87 [0.85, 0.88] | - |
| matched | 1000 | 0.0 | nat | 101 (5%) | 0.88 [0.83, 0.92] | 0.78 [0.74, 0.81] | 0.91 [0.88, 0.93] | 0.85 [0.83, 0.87] | - |
| matched | 3000 | 0.0 | nat | 80 (4%) | 0.95 [0.91, 0.98] | 0.79 [0.74, 0.83] | 0.92 [0.88, 0.95] | 0.84 [0.82, 0.87] | - |
| matched | 100 | 0.03 | nat | 141 (7%) | 0.70 [0.65, 0.74] | 0.65 [0.60, 0.70] | 0.73 [0.69, 0.77] | 0.78 [0.74, 0.82] | - |
| matched | 300 | 0.03 | nat | 116 (6%) | 0.80 [0.75, 0.85] | 0.73 [0.69, 0.77] | 0.79 [0.76, 0.83] | 0.78 [0.74, 0.81] | - |
| matched | 1000 | 0.03 | nat | 103 (5%) | 0.85 [0.81, 0.90] | 0.73 [0.68, 0.76] | 0.83 [0.81, 0.85] | 0.77 [0.72, 0.82] | - |
| matched | 1000 | 0.03 | p4 | 92 (5%) | 0.85 [0.80, 0.90] | 0.73 [0.69, 0.77] | 0.84 [0.80, 0.86] | 0.78 [0.74, 0.82] | 0.96 [0.95, 0.98] |
| matched | 3000 | 0.03 | nat | 80 (4%) | 0.92 [0.87, 0.96] | 0.73 [0.68, 0.77] | 0.86 [0.82, 0.89] | 0.75 [0.70, 0.81] | - |
| matched | 1000 | 0.1 | p4 | 30 (2%) | 0.84 [0.74, 0.93] | 0.77 [0.71, 0.83] | 0.90 [0.86, 0.93] | 0.59 [0.50, 0.68] | 0.98 [0.98, 0.99] |
| other | 100 | 0.0 | nat | 466 (23%) | 0.80 [0.78, 0.83] | 0.75 [0.72, 0.77] | 0.76 [0.74, 0.79] | 0.93 [0.92, 0.94] | - |
| other | 300 | 0.0 | nat | 423 (21%) | 0.86 [0.84, 0.89] | 0.76 [0.74, 0.78] | 0.77 [0.75, 0.80] | 0.92 [0.90, 0.92] | - |
| other | 1000 | 0.0 | nat | 410 (20%) | 0.92 [0.90, 0.94] | 0.77 [0.75, 0.80] | 0.78 [0.76, 0.80] | 0.91 [0.90, 0.92] | - |
| other | 3000 | 0.0 | nat | 363 (18%) | 0.95 [0.94, 0.97] | 0.77 [0.75, 0.80] | 0.77 [0.75, 0.80] | 0.90 [0.89, 0.92] | - |
| other | 100 | 0.03 | nat | 424 (21%) | 0.82 [0.80, 0.85] | 0.76 [0.74, 0.79] | 0.63 [0.60, 0.66] | 0.89 [0.87, 0.90] | - |
| other | 300 | 0.03 | nat | 361 (18%) | 0.84 [0.82, 0.87] | 0.76 [0.74, 0.78] | 0.65 [0.62, 0.68] | 0.87 [0.85, 0.89] | - |
| other | 1000 | 0.03 | nat | 379 (19%) | 0.91 [0.88, 0.92] | 0.76 [0.73, 0.78] | 0.74 [0.71, 0.76] | 0.86 [0.84, 0.88] | - |
| other | 1000 | 0.03 | p4 | 334 (17%) | 0.92 [0.90, 0.94] | 0.78 [0.75, 0.81] | 0.76 [0.72, 0.78] | 0.86 [0.84, 0.88] | 0.83 [0.81, 0.86] |
| other | 3000 | 0.03 | nat | 305 (15%) | 0.96 [0.94, 0.97] | 0.77 [0.74, 0.79] | 0.79 [0.77, 0.82] | 0.85 [0.83, 0.87] | - |
| other | 1000 | 0.1 | p4 | 141 (7%) | 0.87 [0.82, 0.91] | 0.85 [0.82, 0.88] | 0.83 [0.80, 0.87] | 0.70 [0.66, 0.75] | 0.92 [0.89, 0.95] |

*Interventions on r: the fitted model given one, two or four fixed seeded runs (a run started at r(0) = 0.5; 0.35 and 0.7; 0.2, 0.4,
0.6 and 0.8, each observed for three steps), n = 1,000:*

| generators | n | sigma | pairs | igniting | AUC known-F margin | AUC curve summaries | AUC fitted model, natural runs | Brier skill of it | AUC adaptive probe | AUC fitted model + 1 seeded run | + 2 seeded runs | + 4 seeded runs | Brier skill, + 4 seeded runs |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| matched (beta, clipped normal) | 1000 | 0.03 | 2000 | 179 (9%) | 0.86 [0.82, 0.89] | 0.76 [0.73, 0.79] | 0.81 [0.79, 0.85] | +0.12 | 0.72 [0.69, 0.75] | 0.93 [0.91, 0.95] | 0.94 [0.91, 0.96] | 0.92 [0.90, 0.95] | +0.54 |
| matched (beta, clipped normal) | 1000 | 0.1 | 2000 | 94 (5%) | 0.88 [0.83, 0.93] | 0.77 [0.73, 0.81] | 0.84 [0.80, 0.87] | +0.07 | 0.55 [0.49, 0.61] | 0.89 [0.86, 0.92] | 0.90 [0.87, 0.94] | 0.91 [0.87, 0.94] | +0.32 |
| other (bimodal, logit-normal) | 1000 | 0.03 | 2000 | 355 (18%) | 0.91 [0.89, 0.93] | 0.78 [0.76, 0.80] | 0.76 [0.73, 0.79] | +0.06 | 0.83 [0.81, 0.86] | 0.85 [0.83, 0.88] | 0.85 [0.83, 0.88] | 0.82 [0.79, 0.84] | +0.17 |
| other (bimodal, logit-normal) | 1000 | 0.1 | 2000 | 158 (8%) | 0.85 [0.81, 0.89] | 0.84 [0.80, 0.87] | 0.82 [0.79, 0.86] | +0.10 | 0.67 [0.62, 0.72] | 0.86 [0.82, 0.90] | 0.90 [0.87, 0.92] | 0.90 [0.87, 0.92] | +0.36 |

**Reading.**

- *Ignition is predictable above chance, but not by the criterion.* From natural curves the fitted model reaches AUC 0.71-0.85 with a matching family and 0.62-0.79 with a wrong one; a logistic regression on curve
  summaries (final levels and initial shares, no model of F) reaches 0.63-0.78 and 0.73-0.77. The fitted model beats the summaries by more than 0.02 in 7 of 8 matched cells and
  is worse by more than 0.02 in 2 of 8 cells with the wrong family, (n, sigma) = (100, 0.03), (300, 0.03).
  Like for like at n = 1,000 (the 8 cells of both tables): the fitted model 0.80-0.85 with the matching family, against 0.86-0.88 for the reference that knows F,
  and 0.73-0.82 with a wrong one, against 0.85-0.91; summaries 0.73-0.84. With the right family the curve comes close to the reference, because the family supplies F above the stall (added at review).
- *Even knowing F exactly, small crowds are only partly predictable.* The reference that uses the true generators' CDFs reaches 0.71-0.92 (matched) and 0.80-0.95 (other families), rising with n (at n = 100
  0.71-0.82, at n = 3,000 0.92-0.95): a realised crowd of 100 differs from its F by more than the margin that decides ignition. The curve-based scores can exceed the
  reference because the curves also carry the realised crowds' own thresholds.
- *An intervention reads the necessary condition directly.* The adaptive probe (start each crowd at the higher final level, read r(1) - r(0)) reaches AUC 0.82-0.92 with exact counts, 0.70-0.86 at sigma = 0.03 and
  0.55-0.67 at sigma = 0.1: it measures F_1(M) - M, the quantity the curves cannot supply. It reads a necessary condition, not a sufficient one, so it stops short of 1 even without noise,
  and noise of 0.1 takes it to 0.55 [0.49, 0.61] (matched); 0.67 [0.62, 0.72] (other) (corrected at review: "chance-like values", which only the first is).
- *Seeded runs.* Adding one run started at r(0) = 0.5 lifts the fitted model at n = 1,000 from 0.81-0.84 to 0.89-0.93 (matching) and from
  0.76-0.82 to 0.85-0.86 (wrong family); more runs add little in AUC, much in Brier skill (0.17-0.54 against
  0.06-0.12). The material-ignition AUCs (second table) are similar or higher.
  The 95% intervals of one seeded run and of the natural run are disjoint in 2 of 4 cells
  (matched sigma = 0.03, other sigma = 0.03); in the others they overlap, and no paired test of the difference was run (added at review).

## 4. Variations

Each variation changes one part of the model form or the design and reports which variant fits best.

**4.1 Fitted threshold family.** Section 3.3: the family with the largest marginal likelihood, by generator (the confusion table).

**4.2 Dynamic form: the turn map against an inertial variant.** Curves from r(t+1) = r(t) + alpha (F_n(r(t)) - r(t)) with alpha = 0.25 to
1 (alpha = 1 is v0.1's turn map; alpha < 1: each member re-decides with probability alpha per turn, in expectation), observed for 16
turns at n = 1,000; each curve fitted by the same family at every alpha. "Best" = largest marginal likelihood; RMSE = posterior mean
of tau and F(r) at the probes, over the prior sd.

| family | sigma | true alpha | best: alpha=0.25 | best: alpha=0.5 | best: alpha=0.75 | best: alpha=1.0 | RMSE F, fitted alpha=0.25 | RMSE F, fitted alpha=0.5 | RMSE F, fitted alpha=0.75 | RMSE F, fitted alpha=1.0 |
|---|---|---|---|---|---|---|---|---|---|---|
| beta | 0.03 | 0.25 | 0.88 | 0.09 | 0.01 | 0.02 | 0.49 | 0.63 | 0.72 | 0.75 |
| beta | 0.03 | 0.5 | 0.22 | 0.57 | 0.14 | 0.08 | 0.66 | 0.44 | 0.53 | 0.61 |
| beta | 0.03 | 0.75 | 0.10 | 0.20 | 0.44 | 0.26 | 0.77 | 0.58 | 0.47 | 0.49 |
| beta | 0.03 | 1.0 | 0.06 | 0.12 | 0.22 | 0.60 | 0.79 | 0.66 | 0.50 | 0.46 |
| beta | 0.1 | 0.25 | 0.83 | 0.12 | 0.02 | 0.03 | 0.35 | 0.60 | 0.72 | 0.75 |
| beta | 0.1 | 0.5 | 0.28 | 0.51 | 0.13 | 0.09 | 0.69 | 0.37 | 0.47 | 0.58 |
| beta | 0.1 | 0.75 | 0.13 | 0.29 | 0.30 | 0.28 | 0.87 | 0.51 | 0.36 | 0.39 |
| beta | 0.1 | 1.0 | 0.08 | 0.17 | 0.26 | 0.48 | 1.02 | 0.65 | 0.41 | 0.34 |
| clipnorm | 0.03 | 0.25 | 0.95 | 0.04 | 0.00 | 0.01 | 0.34 | 0.96 | 1.20 | 1.23 |
| clipnorm | 0.03 | 0.5 | 0.12 | 0.78 | 0.07 | 0.02 | 0.75 | 0.30 | 0.61 | 0.85 |
| clipnorm | 0.03 | 0.75 | 0.05 | 0.18 | 0.68 | 0.10 | 0.89 | 0.58 | 0.38 | 0.55 |
| clipnorm | 0.03 | 1.0 | 0.02 | 0.03 | 0.25 | 0.70 | 0.97 | 0.72 | 0.47 | 0.34 |
| clipnorm | 0.1 | 0.25 | 0.92 | 0.07 | 0.00 | 0.01 | 0.37 | 0.97 | 1.23 | 1.30 |
| clipnorm | 0.1 | 0.5 | 0.20 | 0.66 | 0.10 | 0.04 | 0.78 | 0.39 | 0.61 | 0.85 |
| clipnorm | 0.1 | 0.75 | 0.11 | 0.34 | 0.39 | 0.16 | 0.91 | 0.55 | 0.38 | 0.52 |
| clipnorm | 0.1 | 1.0 | 0.04 | 0.19 | 0.24 | 0.52 | 0.98 | 0.69 | 0.46 | 0.38 |

**4.3 The time axis: observing every m-th turn.** Curves from the turn map observed at turns 0, m, 2m, ..., 5m (n = 1,000, sigma = 0.03).
Fits: m known, m wrongly taken to be 1, and m unknown (marginalised over 1, 2, 3).

| family | true turns per observation | fit | tau post sd (prior sd) | F post sd (prior sd) | tau RMSE (prior sd) | F RMSE (prior sd) |
|---|---|---|---|---|---|---|
| beta | 1 | m known | 0.146 | 0.19 | 0.35 | 0.43 |
| beta | 1 | m wrongly taken as 1 | 0.146 | 0.19 | 0.35 | 0.43 |
| beta | 1 | m unknown (marginalised) | 0.137 | 0.33 | 0.35 | 0.48 |
| beta | 2 | m known | 0.025 | 0.18 | 0.29 | 0.44 |
| beta | 2 | m wrongly taken as 1 | 0.007 | 0.11 | 0.26 | 0.65 |
| beta | 2 | m unknown (marginalised) | 0.073 | 0.30 | 0.27 | 0.48 |
| beta | 3 | m known | 0.002 | 0.22 | 0.28 | 0.44 |
| beta | 3 | m wrongly taken as 1 | 0.000 | 0.06 | 0.26 | 0.86 |
| beta | 3 | m unknown (marginalised) | 0.001 | 0.30 | 0.26 | 0.52 |
| clipnorm | 1 | m known | 0.005 | 0.12 | 0.39 | 0.33 |
| clipnorm | 1 | m wrongly taken as 1 | 0.005 | 0.12 | 0.39 | 0.33 |
| clipnorm | 1 | m unknown (marginalised) | 0.020 | 0.31 | 0.41 | 0.46 |
| clipnorm | 2 | m known | 0.010 | 0.17 | 0.47 | 0.40 |
| clipnorm | 2 | m wrongly taken as 1 | 0.000 | 0.06 | 0.37 | 0.74 |
| clipnorm | 2 | m unknown (marginalised) | 0.016 | 0.33 | 0.42 | 0.45 |
| clipnorm | 3 | m known | 0.012 | 0.30 | 0.53 | 0.48 |
| clipnorm | 3 | m wrongly taken as 1 | 0.000 | 0.02 | 0.42 | 0.96 |
| clipnorm | 3 | m unknown (marginalised) | 0.009 | 0.32 | 0.43 | 0.55 |

**4.4 The observation model: multiplicative counting error.** Curves observed as r exp(N(-s^2/2, s^2)), the way crowd counts are wrong,
fitted with additive Gaussian noise of matched overall size or with noise proportional to the level (n = 1,000).

| family | relative counting error | noise model fitted | tau cov90 | F inside cov90 | tau post sd |
|---|---|---|---|---|---|
| beta | 0.1 | additive | 0.88 | 0.50 | 0.003 |
| beta | 0.1 | relative | 0.74 | 0.69 | 0.010 |
| beta | 0.3 | additive | 0.92 | 0.58 | 0.002 |
| beta | 0.3 | relative | 0.90 | 0.84 | 0.010 |
| clipnorm | 0.1 | additive | 0.79 | 0.57 | 0.002 |
| clipnorm | 0.1 | relative | 0.88 | 0.78 | 0.007 |
| clipnorm | 0.3 | additive | 0.76 | 0.58 | 0.012 |
| clipnorm | 0.3 | relative | 0.93 | 0.87 | 0.021 |

**4.5 Design: interventions on r.** SBC with the natural run plus seeded runs (n = 1,000; the same cells feed section 3.5):

| family | sigma | design | calibrated | params | F inside | F outside | RMSE F outside | c90 F outside |
|---|---|---|---|---|---|---|---|---|
| beta | 0.03 | nat | yes | 0.38 | 0.06 | 0.49 | 0.69 | 0.88 |
| beta | 0.03 | p1 | yes | 0.23 | 0.04 | 0.08 | 0.27 | 0.90 |
| beta | 0.03 | p2 | yes | 0.15 | 0.03 | 0.04 | 0.11 | 0.87 |
| beta | 0.03 | p4 | yes | 0.10 | 0.02 | 0.03 | 0.05 | 0.91 |
| beta | 0.1 | nat | yes | 0.57 | 0.16 | 0.46 | 0.61 | 0.90 |
| beta | 0.1 | p1 | yes | 0.47 | 0.12 | 0.16 | 0.37 | 0.90 |
| beta | 0.1 | p2 | yes | 0.45 | 0.11 | 0.12 | 0.21 | 0.90 |
| beta | 0.1 | p4 | yes | 0.35 | 0.09 | 0.09 | 0.15 | 0.89 |
| clipnorm | 0.03 | nat | NO | 0.16 | 0.08 | 0.33 | 0.73 | 0.86 |
| clipnorm | 0.03 | p1 | yes | 0.11 | 0.07 | 0.06 | 0.11 | 0.87 |
| clipnorm | 0.03 | p2 | yes | 0.08 | 0.05 | 0.05 | 0.09 | 0.91 |
| clipnorm | 0.03 | p4 | yes | 0.04 | 0.03 | 0.04 | 0.08 | 0.87 |
| clipnorm | 0.1 | nat | yes | 0.41 | 0.27 | 0.50 | 0.63 | 0.91 |
| clipnorm | 0.1 | p1 | yes | 0.33 | 0.22 | 0.19 | 0.27 | 0.91 |
| clipnorm | 0.1 | p2 | yes | 0.27 | 0.18 | 0.15 | 0.21 | 0.87 |
| clipnorm | 0.1 | p4 | yes | 0.20 | 0.13 | 0.12 | 0.18 | 0.91 |

**4.6 Detectors of the gate.** Section 3.4: the order test against the any-drop rule, and the ever-joined curve.

**Which variant fits best.**

- *Threshold family (4.1):* the generating family comes first in 0.74-0.94 of clipped-normal curves, 0.34-0.86 of beta+atom curves and
  0.23-0.44 of logit-normal curves across the cells; for bimodal crowds the family that comes first is wrong by construction (3.3).
- *Dynamic form (4.2):* the true alpha has the largest marginal likelihood in 0.83-0.95 of curves at alpha = 0.25, 0.51-0.78 at 0.5, 0.30-0.68 at 0.75 and 0.48-0.70 at 1.0 (the turn map). alpha = 0.75
  and 1.0 are the hardest to separate. The clock matters for F: fitting the turn map to inertial curves (alpha < 1) gives an RMSE of F of 0.39-1.30 prior sds, against 0.30-0.49 with the right alpha.
- *Time axis (4.3):* if the number of turns per observation is unknown the posterior sd of F is 0.30-0.33 of the prior sd, against 0.17-0.30 when it is known; assuming it is 1 when it is 2 or 3 gives a posterior
  sd of 0.02-0.11 (over-confident) and an RMSE of 0.65-0.96 against 0.40-0.48.
- *Observation model (4.4):* noise proportional to the level covers F inside the visited range in 0.69-0.87 against 0.50-0.58 for additive noise (nominal 0.90) when the counting error is multiplicative.
- *Design (4.5):* the posterior sd of F outside the visited range is 0.33-0.50 of the prior sd from the natural run alone and falls to
  0.06-0.19 with one seeded run, 0.04-0.15 with two and 0.03-0.12 with four (1 of the 16 design cells is not calibrated).
- *Gate detectors (4.6):* the order test and the any-drop rule tie (3.4).

## 5. Caveats

- **Synthetic.** Nothing here says real crowds obey the law. It says what an aggregate curve could tell us about the law **if** they did,
  under favourable conditions (known denominator, continuous shares, equal turns, known noise). The structural results (3.1) do not
  depend on any prior; every number in 3.2 to 3.5 does.
- **The prior.** Crowds with at least 2% instigators, parameters in the ranges of section 2, smooth threshold families. Smooth families
  flatter extrapolation: real threshold distributions can have atoms and gaps, and Granovetter's own pair (thresholds 0 to 99, one moved
  from 1 to 2: equilibrium 100 against 1, L3964) is the limiting case in which one threshold decides the outcome and no smooth family
  would find it. The numbers are for these generators, not for crowds.
- **Information is relative to a discrete grid prior** and saturates at the grid scale (values near 0.00 mean "to within a cell"); coverage under
  a continuous truth is grid-limited where the posterior is narrower than the grid (the matched rows at sigma = 0 and large n in 3.3).
- **Engines.** The exact and lattice engines are exact; the lattice engine runs only to n = 100 and, at n = 100, with M = 40 datasets per cell
  (a coverage standard error of 0.05), so its "calibrated" there has little power. The synthetic engine is an approximation:
  slightly over-confident where it works (at n = 1,000 the central-90% coverage of the scored quantities ranges from 0.86 to 0.92) and invalid where n sigma is small. Cells marked * rest on it.
  The misspecification and ignition cells with sigma > 0 rest on it too, on the fine grids with S = 1,000 and 800; the misspecification setups have
  their own SBC at the end of 3.3, and the ignition setups were not checked (added at review).
- **The fitted grids.** The beta+atom and logit-normal grids stop at an instigator share z of 0.20 (standard) and 0.22 (fine), while those generators
  draw z up to 0.25, so about 5% of the "matched" curves of 3.3 and 3.5 have a z outside the fitted grid (added at review).
- **Multiple comparisons.** About a dozen quantities per cell and about sixty cells: a few isolated KS p-values below 0.01 are expected
  from an exact engine and are not flagged; the calibration flag uses 0.001 and 3.5 standard errors. Under exact posteriors it fires by chance in at
  most about 2% of cells (11 or 12 KS tests and as many coverages per cell), about one of the sixty (two of the 87 with the review's cells); none of
  the 20 exact and lattice cells fired, and the synthetic engine's flags are far more than chance. The AUC and coverage comparisons are descriptive,
  with marginal intervals and no paired tests; the wrong-family model's deficit against the summaries at (100, 0.03) and (300, 0.03) clears both
  intervals (added at review).
- **Observation model (4.4).** The additive fit uses sigma = 0.3 times the relative error (the error at a level of 0.3), and the two noise models
  are scored on different simulated datasets, not the same ones (added at review).
- **Selection and eligibility** (live crowds; unsaturated pairs) are my definitions and depend only on the observed curves. Quantities
  read "outside the visited range" are defined from the observed level of the curve, not from the truth.
- **The time axis.** Ten equal turns, no clock. Sections 4.2 and 4.3 show that a clock matters; the law as written has none.
- **Ignition.** The label is the realised ignition of two finite crowds; the model-based score is a population-level quantity, so its Brier
  skill is a statement about a mismatched target and the AUC is the fair comparison. The adaptive probe and the seeded runs assume that a
  crowd can be started at an exogenous share and observed again; whether any real event offers that is open (Cantoni et al. moved
  believed attendance, not attendance, L4353, and the scope of their finding is open, L4363).
- **The gate.** One parametrisation of the upper gate (a fraction nu with a Beta window); the order test takes sigma as known (an unknown
  sigma lowers its power); no test was built for the plateau-then-growth trace in the ever-joined curve, so its detectability under noise
  is not measured, only its noise-free frequency.
- **Not tested:** per-member data, heterogeneous response times, network structure (Granovetter's friend weights), more than two parts in
  a merge, and anything about whether a real crowd's F is stable between events.

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.identifiability_crowd_report report --workers 6 --cache /tmp/idcrowd-cache   # rewrites this file; 25 to 40 minutes on six shared cores
    ~/.local/bin/uv run pytest tests/test_identifiability_crowd.py                                                    # about 30 s

Every task seeds itself from the task description, so the numbers do not depend on scheduling or on `--workers`. `--quick` cuts every
sample size (smoke run only).

## Review (2026-11-01)

A second agent's review: re-run, re-derived, and checked for null models, leakage, multiple comparisons, data terms, ledger ids and the strength of the verdict. This section is appended by hand after the `report` run above; a fresh `report` rewrites everything above it and drops it.

**Re-run and re-derivation.**

- *Before the review.* 31 tests passed (19 s), and `report` from the original run's task cache reproduced the previous file byte for byte.
- *A fresh run.* All 157 tasks were then re-run with no cache (823 s on four workers). 150 are bit-identical to the original run. The other seven differ only by the review's changes 2 and 5 below: claim14 gained counts with every old count unchanged, and the six time-axis tasks a corrected RMSE.
- *After the review.* 32 tests pass. The file is written by `report` from 184 tasks (the 27 SBC cells added below), and two `report` runs give identical files.
- *Independent re-derivation.* The code shares only the samplers with the module. Every claim14 count was recomputed by plain iteration and exact rationals: 1,882 igniting pairs of 20,000; 112 flips in 1,018 trials; 495 sandwich pairs with 246 and 178 upper-end moves; no violation. So were all eight rows of the visited-points table.
- *One SBC row re-derived.* The clipped normal at n = 300 with exact counts was recomputed with the likelihood written as a multinomial over cells, not as sequential binomials. It gives min KS p 0.397, coverage 0.88-0.91, joint-likelihood coverage 0.88 and KS p 0.635, and the information row 0.08 / 0.001 / 0.11 / 0.06 / 0.48, all as reported.

**Errors found and fixed (code, tests and this file).**

1. *The engines were said to be right wherever they are used.* The synthetic engine also carries the misspecification and ignition cells with sigma > 0, at every n, without stars. It runs there on fine grids with S = 1,000 and 800, which no SBC cell checked.
   - A new SBC of exactly the misspecification setups (27 cells, `setup="mfit"` in `build_specs`, end of 3.3) passes in 18. It fails in 9: six of the nine sigma = 0.01 cells, the clipped normal and logit-normal at (300, 0.03), and the logit-normal at (1000, 0.03).
   - A differently seeded scratch run flagged 10, nine of them at n <= 1,000 and sigma <= 0.03, so a flag near the boundary is noisy at M = 400.
   - The verdict, section 2 and the caveats now say so. The ignition setups remain unchecked.
   - The same SBC settles the matched rows' low F(0) coverage (0.64 and 0.66). With the truth on the grid, F(0) is covered 0.89 and 0.93. The loss therefore comes from the continuous truth falling between six grid values of z, not from the engine. A first guess at the cause, made during review, was tested and dropped.
2. *Claim 1.2's "strictness" was not what was checked.*
   - The igniting-pair check, that the two stalls differ, is Claim 1.2's equal case. Strictness (unequal stalls merge strictly above the smaller) is now checked in the sandwich pairs: no violation in 484.
   - The verdict also called the four generators ones "the claims were not built on". Three of them (beta, bimodal and clipped normal) are among the families of `models/02`'s own check, 1.8.
3. *The flip rate included pairs in which a flip is impossible.*
   - The text said that two crowds with the same curve "merge with the same host to opposite outcomes in 11%" of pairs. But the redrawn crowd is the host in 355 of the 1,018 trials.
   - A redrawn host cannot flip the outcome: the merge reaches the host's stall only through thresholds at or below it, which the redraw keeps. A new test checks this.
   - All 112 flips are among the 663 trials with a redrawn intruder: 17%.
4. *The ignition comparison was not like for like.* The verdict set the fitted model's AUC over n = 100 to 3,000 (0.71-0.85) against the known-F reference at n = 1,000 (0.85-0.91). At n = 1,000 the matched fitted model reaches 0.80-0.85, against the reference's 0.86-0.88. With the right family the curve predicts nearly as well as knowing F, because the family supplies F above the stall. The verdict now says so; the exact non-identification is unchanged.
5. *The time-axis "F RMSE" was not an RMSE* (`subsample_cell`). It was the median over curves of each curve's RMS error; it is now the RMSE.
   - With m known it is 0.33-0.48 (reported as 0.12-0.31).
   - When m is 2 or 3, assuming m = 1 gives 0.65-0.96, against 0.40-0.48 with m known (reported as 0.55-0.90 against 0.20-0.31).
   - The conclusion stands (the wrong clock is over-confident and wrong), but the gap is smaller.
6. *Ledger glosses and citations.*
   - L4348 was glossed "crackdown cost rises with size". The ledger has the crackdown probability rising, the individual cost falling, and the net cost going either way.
   - L1225 was cited for "Granovetter allows thresholds as counts or shares". That is L3983, now added.
   - "L1225's non-identifiability made exact" had the direction reversed. L1225 says no moment of F fixes the outcome; Proposition B says the outcome curve does not fix F.
   - L4138 and L4139 were cited inside the range L4136-L4140 but were absent from `LEDGER`. Both are added, so the ledger test now covers them.
7. *Smaller items.*
   - The probe at sigma = 0.1 was called "chance-like". Only the matched cell is (0.55 [0.49, 0.61]); the other is 0.67 [0.62, 0.72].
   - "Beyond a few hundred members a larger crowd does not help" is false at sigma = 0.01 (clipped normal 0.13, 0.05, 0.01 at n = 300, 1,000, 3,000). It is now restricted to sigma >= 0.03.
   - "F inside the visited range from n = 100" missed that beta+atom meets the criterion from n = 30.
   - Verdict item 3 quoted an uncalibrated cell (clipped normal, n = 1,000, sigma = 0.03) without its star. Item 4's "calibrated width" now says that it holds where the engine is calibrated.
   - The tau RMSE (0.09-0.38) and seven of the twelve confusion cells behind the verdict's ranges were in no table. Both are now shown.
   - `_range` printed 0.853 and 0.857 as one value, "0.85", beside a table showing 0.86. It now compares the printed strings.
   - Cantoni et al. moved the believed share, not the share itself. "Interventions on r identify" is now restricted to what was shown: within the right family.
   - The docstrings of `dynamic_form_cell` and `subsample_cell` described inside-only probes; both use all probes.
   - New caveats cover the fine-grid engine, the fitted grids' z range (0.22 against the generators' 0.25, about 5% of matched curves), the multiple-comparison arithmetic, and the observation-model cells (sigma = 0.3 times the relative error, scored on unpaired datasets).

**Checked and found sound.**

- *Null models.*
  - SBC: the randomised rank of the truth under an exact grid posterior is uniform. Selecting live curves on the observed data alone leaves it so, and the tempering check rejects a wrong posterior.
  - The gate: the flat latent curve is least favourable for both detectors. For the any-drop rule, every drop of a non-decreasing curve is dominated by the noise's own drop. For the order test it follows from Robertson, Wright & Dykstra. The one-sided controls reject at 1-5%.
  - Ignition: AUC is scored against 0.5 with bootstrap intervals, and the known-F margin is labelled a reference, not a ceiling.
- *Leakage.*
  - No time series is forecast.
  - The summaries' logistic regression is trained on 2,000 pairs drawn under a different seed from the scored ones.
  - Inside and outside are set by the observed level, and the fitted models see only observed curves. The exact engine reads the integer path only at sigma = 0, where it is the observation.
  - The probe and the seeded runs are interventions, and are labelled so.
- *Multiple comparisons.* By chance the calibration flag fires in at most about 2% of cells. None of the 20 exact and lattice cells fired, and the synthetic engine's failures (10 of 24 and 9 of 27) are far beyond chance. The AUC differences are descriptive. The ones the verdict leans on have disjoint marginal intervals, except the one-seeded-run gain at sigma = 0.1, which is now flagged in 3.5.
- *Data and terms.* None are used. Nothing is read from or written to `sim/data/`: the only file read is `docs/ledger.jsonl`, and the optional task cache is a directory the user names. Nothing is downloaded and no personal data is involved, and `sim/data/README.md` rightly does not list this test. `sim/README.md` has no entry for it either (not changed here).
- *Ledger ids.* All 31 ids exist (`test_cited_ledger_ids_exist`), and after item 6 they say what the code assumes.

**Verdict after review.**

- *The exact results stand*, re-derived independently: Propositions A and B, counts against shares, Claims 1.2 and 1.4 on finite crowds, and F above the stall unidentified.
- *Recovery (3.2)* stands, with its stars.
- *Misspecification (3.3).* A wrong family is still fitted confidently and wrongly (coverage 0.52 and 0.57, against 0.83 and 0.86 matched). Part of the matched rows' loss is the engine's in the nine cells where its own SBC fails: mostly sigma = 0.01, plus the logit-normal and clipped normal at sigma = 0.03 with n <= 1,000.
- *Ignition (3.5).* The non-identification is exact. The prediction evidence is weaker than the verdict implied: at n = 1,000, with the right family, the curve nearly matches knowing F. What is refuted is identification without a family, not prediction.
- *The gate (3.4) and the interventions (4.5)* are unchanged.
- *The headline* stands at the strength now stated: the curve does not identify F above its stall, the family, or the ignition criterion.
