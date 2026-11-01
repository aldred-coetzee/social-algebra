# A reciprocity gate on the Bitcoin OTC and Alpha trust networks: is there a dead zone?

_Generated 2026-11-01 by `uv run python -m models.gate_reciprocity_bitcoin_report report` (seed 20261101, 1000 cluster-bootstrap draws, 5 x 10-fold CV repeats, 55 s). Code: `sim/models/gate_reciprocity_bitcoin.py`, `sim/models/gate_reciprocity_bitcoin_report.py`; checks: `sim/tests/test_gate_reciprocity_bitcoin.py`. Ledger ids are lines of `docs/ledger.jsonl` (O-jive L0857, L0853, L0834, L4367; Bitcoin L4567-L4580; embeddedness L4825). Results are computed statistics only; the rating files are local-use-only and are not redistributed (`sim/data/README.md`)._

**What was tested.** `models/00-v0.md` (v0.2; the law is v0.1's) writes the dyad influence as an O-jive (the influence function of Gottman, Swanson & Murray 1999, *J. Family Psychology* 13:3-19, doi:10.1037/0893-3200.13.1.3, as read in L0857): zero while the partner's level lies in a band [K-, K+], a bounded constant beyond each threshold, a function of the partner's LEVEL (sections 3 'D2' and 4.1). 112 section 6.2 carries dead-zone widths into the sign module. The prediction: where one trader rates another, the rating a trader GIVES back has a dead zone in the rating RECEIVED from that counterparty. The data are Bitcoin OTC and Alpha (117 section 3.4, L4567-L4580), 2010-2016: every ordered pair is rated once, 66% of OTC pairs and 71% of Alpha pairs are rated in both directions.

## Verdict

**In short.**

- **Dead zone in the response: refuted on OTC, and on Alpha for every band that reaches +2.** A dead zone is a flat response over a band of small received ratings. On OTC the response is flat over no band that holds two observed ratings; on Alpha every band that reaches +2 is rejected, but the band {-1, +1} is not (17 responses to a -1: -2.3 (1.3) against +1, p = 0.074). After a received +2 the response is +0.85 points above its level after a received +1 on OTC (chi2(1) = 221, p < 1e-10) and +1.06 on Alpha (p = 1e-05); flatness over +1..+4 is rejected at p < 1e-10 on OTC and p < 1e-10 on Alpha. The response climbs 0.83 rating points per received point from the first point (OTC, 95% CI [0.77, 0.89]; Alpha 0.83 [0.64, 1.02]). This refutes the dead zone as a property of the observed response. As a property of the INFLUENCE it needs one more step, because a shared view of the deal (undecided, below) would add slope inside any band; but the O-jive's bounded step would then still show as an excess jump on top of a linear slope, and none is seen between +1 and +4 (increments +0.85, +0.79, +0.89 on OTC, equal: chi2(2) = 0.2, p = 0.898; Alpha +1.06, +0.48, +1.05, p = 0.540; the step from +4 to +5 is smaller, +0.29 on OTC).
- **The O-jive as written fits worse than a graded response with no band.** With bounded constants beyond free thresholds (D, step) it loses out of sample to the graded two-sided form with the band closed (T, graded) by 0.46 squared rating points (6.5 SE) on OTC and 0.59 (3.1 SE) on Alpha. One-sided forms (positive-only, negative-only) lose by 1.2 to 1.7.
- **The best dead-zone fit finds a band of one rating, +1, and that band is concavity, not a zone.** With a graded response beyond the thresholds the fit puts K- at -1 and K+ at +2 in 100% and 100% of OTC bootstrap draws (Alpha 56% and 95%). That fit spans exactly the functions of a no-band curve with two slopes whose knee sits at +2 (a step at +2 plus the slope after it equal one line through +1 plus a change of slope at +2; the residual sums of squares agree to 2e-15); the slopes are 1.03 from +1 to +2 and 0.50 beyond. Moving the knee to +8 (bootstrap median 7, 95% range 4-8) fits better in sample with ONE threshold instead of two: residual sum of squares -432 and BIC -120 on OTC (-263 and -35 on Alpha), and out of sample it is no worse (dead-zone fit minus it: +0.009, +0.3 SE on OTC; +0.206, +1.4 SE on Alpha; exploratory form). Freeing the band gains 0.028 squared points over closing it on OTC (z = 2.3) and nothing detectable on Alpha. The one rating +1 is where the response crosses zero: against the responder's own mean initiating rating the response to +1 is +0.05 (0.05) and to +2 +0.79 (0.09); +1 is the modal rating (56% of all OTC ratings) and, on average, the responders' own habit (mean initiating rating 1.05).
- **The sign gate is real and large.** A negative received rating moves the response by -8.36 (0.34) points against a +1 (Alpha -6.64 (0.65)); 95% of OTC responses to a negative rating are negative, against 2.5% after a positive one. The mildest negative rating, -1, already moves the response by -4.1 points against +1 on OTC (p = 1e-07), so on OTC there is no dead zone on the negative side either; on Alpha the -1 cell (17 responses) is too thin to say.
- **'Bounded constants beyond the threshold' holds only as saturation.** The positive response rises 0.8 per point to +4, more slowly to about +7 (clipped-mirror knee 7, [6, 8]) and not further: the levels at 5-8 and at 9-10 are +3.4 (0.2) and +3.8 (0.4) above +1. The 9-10 ratings are unstable (only 27% of +10 first ratings are answered within a day, 37% within 30 days) and the negative side is near its floor at -10. Between the thresholds nothing is flat.
- **Drift 2010-2016.** The form does not change: in every year with enough pairs (2011-2015 on OTC, 2011-2014 on Alpha) the response at +2 exceeds the response at +1 (on Alpha as a point estimate, individually significant only in 2013), and on OTC the best dead-zone fit is the one-rating band every year. On OTC the 1-4 slope rises modestly: 0.72 (2011), 0.78, 0.84, 0.98, 0.87 (2015), a pooled trend of +0.073 (0.026) per year and +0.064 (0.027) from the yearly estimates (lack of fit p = 0.767). The negative jump and the 9-10 level have pooled trends (+0.92 (0.38) and -1.21 (0.36) per year) that the years do not follow: neither is linear in year (lack of fit p = 0.037 and p = 9e-04; the 9-10 level is highest in 2015), and against the year-to-year scatter their trends are z = +0.9 and -0.6: no drift is shown for either. On Alpha (4 estimable years) the yearly estimates show a trend beyond 2 SE only for the 9-10 level (-1.35 (0.51) per year). 2010 and 2016 hold too few pairs to estimate (51 and 21 on OTC; 7 and 2 on Alpha).

**Thresholds.** K- = -1: any negative rating transmits (100% of OTC draws in the graded fit; the step form spreads over -1: 38%, -2: 51%, -5: 8%). K+ = +2 in the graded fit, i.e. a dead zone of the single rating +1 (OTC draws 100%, Alpha 95%); the literal step form gives K+ = 3: 85%, 4: 15% on OTC because a single step is the best one-step stand-in for a ramp, and its implied band is rejected by the flatness tests. Upper knee of the positive response: 7 ([6, 8]).

**Status of the prediction.**

- *Refuted:* a flat band of small received ratings in the response: over any two or more observed ratings on OTC (the band {+1, +2} in every estimable OTC year), and over any band reaching +2 on Alpha; the 1-4 slope is more than 3 SE above zero in 14 of 16 embeddedness bins (the exceptions, all thin: Alpha, time-respecting count, 10+ common neighbours, 341 rows: 0.56 (SE 0.27); Alpha, static count, 0 common neighbours, 269 rows: 0.30 (SE 0.24)); and a response that is a bounded constant just beyond the thresholds.
- *Supported:* a response that depends on the sign of the received rating (a large jump at zero, K- = -1), grows with the LEVEL of the received rating up to a knee near 7, depends on the level and not on its deviation from the sender's habit, and keeps this form over 2011-2015 and across both platforms.
- *Undecided:* whether the association is reciprocation or two traders' shared view of one trade (the ratings follow one deal; 58% of OTC responses come within 10 minutes and 83% of those repeat the received rating exactly: time order is necessary, not sufficient); a dead zone in the influence hidden under a shared view that is not linear in the received rating; Alpha's band {-1, +1} (17 responses to a -1); whether a band narrower than the scale's one-point resolution exists; the negative side below -1 (321 OTC and 107 Alpha negative received ratings, 67% and 55% of them -10); the 9-10 ratings.

*For v0.2 (proposals, not adopted):* in a rating medium the dyad response is better written as a graded function of the partner's level with a sign jump and a knee than as an O-jive (and so is the influence, unless a shared view that is not linear in the received rating hides a zone); the dead-zone widths theta+ and theta- of 112 section 6.2 should start at 0 here (112 section 6.3 and v0.2 section 4.5 already say so: 'start at 0, wide slack'; those widths act on the accumulated evaluation zbar, which this test reaches only through the received rating); and the response is to the LEVEL of the partner's rating, which is what the O-jive's own form says (v0.2 section 3 'D2').

## 1. Data, terms, definitions

- **Source.** SNAP `soc-sign-bitcoinotc.csv.gz` and `soc-sign-bitcoinalpha.csv.gz` (Kumar, Spezzano, Subrahmanian & Faloutsos 2016, ICDM, doi:10.1109/ICDM.2016.0033; Kumar, Hooi, Makhija, Kumar, Faloutsos & Subrahmanian 2018, WSDM, doi:10.1145/3159652.3159729), public downloads from `https://snap.stanford.edu/data/` kept in the git-ignored `sim/data/bitcoin/`; sha256 `6424ac981dad3a019f697fc1b9fcd85c19d8d9f039797758e9ffb6fea100c373` (OTC, 397,258 bytes) and `3a178611b9c2f39c9a0dc75936f28557317f1733319b49da4838232b3757cd76` (Alpha, 149,480 bytes), byte-identical to a fresh download on 2026-11-01. Terms: none stated by SNAP; treated as not licensed for redistribution and never committed (`sim/data/README.md`; Licensing in `CLAUDE.md`). Checked on every load, matching 117: integer ratings -10..10 with no zero, no ordered pair rated twice, no self-rating.

| platform | ratings | nodes | pairs rated both ways | ordered response pairs | same-timestamp pairs | rows with responder FE | responders |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OTC | 35,592 | 5,881 | 14,100 | 14,100 | 0 | 11,795 | 2,020 |
| Alpha | 24,186 | 3,783 | 10,062 | 2,739 | 7,323 | 2,089 | 405 |

- **Time resolution decides the design.** OTC times are sub-second, so every reciprocated pair has a first and a second rating. Alpha's are whole days (all at 04:00 or 05:00 UTC, local midnight): 7,323 of its 10,062 reciprocated pairs carry one timestamp and cannot be ordered. They are kept out of the time-ordered analysis and analysed separately as unordered pairs with a random orientation (7,323 pairs; section 5.4). Alpha's ordered pairs are therefore all pairs with a gap of a day or more, a sample biased towards slow responses; the like-for-like comparison is OTC with a gap of a day or more (section 5.4).
- **Response pair.** First rater i rated j at t1; responder j rated i at t2 > t1. x = the rating j received from i; y = the rating j gave. One (x, y) per pair. **The gap is short**: on OTC the median is 4.4 minutes, 24% of responses come within a minute, 58% within 10 minutes, 78% within a day, 91% within 30 days. A rating follows one deal (117), so for most pairs the two ratings are two views of one event, one entered seconds or minutes after the other, and the response function below is an association net of the persons' levels, not an isolated causal effect.
- **Controls (primary).** A fixed effect for the RESPONDER, absorbing every time-invariant trait of j (his habit of rating, how he is rated, his general reciprocity); inference clustered by responder (other clusterings in section 3.3). Rows of responders with one response pair cannot inform a fixed effect and are dropped from those fits (16% of OTC pairs). Variations (section 5.1): none; responder and first-rater effects; the responder's habit (the mean of the ratings he gave when he rated first, so uncontaminated by the response mechanism), the first rater's habit and reputation as covariates, from the whole file or from earlier events only; the responder's previous rating (inertia, D1's r_i).
- **Embeddedness** (Leskovec, Huttenlocher & Kleinberg 2010, WWW, doi:10.1145/1772690.1772756; L4825): common neighbours of the pair in the undirected graph of rated pairs, counted either over the whole file (static) or only for neighbours both of whose edges were first rated before the response (time-respecting; primary).
- **Years** are the calendar year (UTC) of the RESPONSE. Cells with fewer than 100 rows are listed, not fitted.

## 2. Method and the nulls

**Forms** (thresholds on the integer received rating; K+ = the first positive rating on which the positive side is active; K- the first negative one, as the rating -K-). All include a free level (the responder effect). 'step' = a bounded constant beyond the threshold (v0's literal O-jive), 'hinge' = continuous and graded beyond it, 'graded' = a jump AND a slope (nests both). A step or graded side is active AT its threshold; a hinge is zero AT its knot and active from the next rating, so for the hinge K is the knot and the band includes it: the two-sided hinge at the origin has its knots at +1 and -1, the ratings nearest zero, and is flat over both (corrected at review: this form was labelled 'no dead zone').

| family | meaning | free thresholds | what the prediction says |
| --- | --- | --- | --- |
| null | no dependence on x | 0 | no coupling |
| linear | one slope on x, both signs | 0 | the linear partner term (L4367: about 0 for couples) |
| O+ / O- | one-sided: only high (or only low) received ratings matter | 1 | a gate open on one side |
| T | two-sided, thresholds at the origin (K+ = 1, K- = 1): no dead zone for step and graded; the hinge, zero at its knots +1 and -1, is flat over {-1, +1} | 0 | sign matters, size may (graded) |
| D | two-sided with a free band (K-, K+): the O-jive / dead zone (for the hinge the band includes its knots) | 2 | v0.2 section 4.1: zero inside, bounded beyond (step) |
| saturated | one mean per rating bin (14 bins) | 13 mean parameters | reference: no functional form |
| clipped mirror; jump + clipped mirror | linear up to a knee U then flat, without / with a sign jump | 1 | exploratory: suggested by the first look at the means; NOT part of the pre-specified comparison |
| no band, two slopes | T graded plus a change of slope at the rating K on the positive side | 1 | exploratory: the no-band rival with the same function class as the dead-zone fit when K = 2 |

**Comparison.** In-sample least squares with thresholds on a grid, BIC counting each threshold as a parameter; and out-of-sample squared error from 10-fold cross-validation repeated 5 times, in which the thresholds are CHOSEN AGAIN inside each training fold and the held-out row's responder effect is re-estimated from its training rows (held-out rows whose responder has no training row are not scored, for every form, so the comparison is paired). Differences carry a cluster-robust standard error (responder).

**Nulls.** (1) *No response*: y independent of x given the responder effect; the cluster-robust Wald test of all twelve received-rating contrasts. (2) *No dead zone*: the response is flat over the band; tested head-on by Wald tests of equality of the mean response over the observed ratings inside a candidate band (section 3.2), and by whether freeing the band (D) beats the same shape with the band closed (T) out of sample (section 4). (3) *Copying beyond habit*: if a responder drew his rating from his own habit regardless of x, the share of responses equal to x would equal the share of his initiating ratings equal to x; the excess over that is the copy excess (section 3.1). (4) *Exchangeability*: if the two ratings were exchangeable (the same process whichever was entered first), swapping their roles would give the same curve; section 5.6. Two views of one deal give that only if the two views carry equal noise and spread, so a difference is weak evidence of a response, and similarity does not show a shared view (corrected at review: this null was stated as 'only two views of one deal').

**What was and was not fixed in advance.** The family names come from the task (one-sided, two-sided, dead zone). The raw mean response by received rating, and a few responder-fixed-effect contrasts, were looked at BEFORE the model forms were coded; the shapes (step / hinge / graded), the threshold grids (1-10 on each side) and the criteria (BIC; cross-validation with the thresholds re-chosen in each fold) were then fixed in the module and the pre-specified forms were not changed after any comparison was run. The four-number 'profile' summary and the two clipped-mirror forms were chosen from that first look; the no-band two-slope form was added LATER, after the dead-zone fit had returned its one-rating band, to ask what that band is. All of them are labelled exploratory wherever they appear. The test is therefore not blind. What protects the verdict is that it rests on the FAILURE of a prediction the model made before the data (a flat band), on a head-on flatness test that no tuning of a form can rescue, and on out-of-sample comparisons with the thresholds re-chosen inside every training fold.

## 3. The response function

### 3.1 Response by received rating

Responder fixed effects. 'Shift' = the mean response against the response to +1 (cluster-robust SE); 'y - habit' = the response minus the responder's own mean initiating rating (single ratings only); 'copy excess' = share of responses that are exact copies beyond what the responder's habit gives (95% cluster-bootstrap CI); responders who never rated first are left out of those two columns. Overall test of no response: chi2(12) = 2731, p < 1e-10 (OTC); chi2(12) = 452, p < 1e-10 (Alpha).

**OTC** (11,795 rows)

| received x | n | mean y | shift vs +1 (SE) | y - habit (SE) | P(y < 0) | P(y = x) | copy excess |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| -10 | 197 | -9.34 | -10.24 (0.29) | -7.66 (0.46) | 98.0% | 91% | 0.87 [0.80, 0.93] |
| -9..-6 | 7 | -5.29 | -5.83 (2.97) |  | 71.4% |  |  |
| -5..-4 | 13 | -6.54 | -7.55 (0.93) |  | 84.6% |  |  |
| -3..-2 | 27 | -4.96 | -6.25 (0.90) |  | 100.0% |  |  |
| -1 | 50 | -2.82 | -4.08 (0.77) | -3.30 (0.77) | 86.0% | 48% | 0.45 [0.28, 0.60] |
| 1 | 7241 | 1.10 | 0 (ref.) | +0.05 (0.05) | 2.5% | 81% | 0.47 [0.44, 0.50] |
| 2 | 2065 | 1.92 | +0.85 (0.06) | +0.79 (0.09) | 2.8% | 60% | 0.51 [0.49, 0.54] |
| 3 | 941 | 2.73 | +1.64 (0.09) | +1.55 (0.12) | 3.1% | 50% | 0.44 [0.40, 0.48] |
| 4 | 359 | 3.59 | +2.52 (0.13) | +2.44 (0.17) | 3.6% | 45% | 0.42 [0.37, 0.48] |
| 5 | 433 | 3.97 | +2.81 (0.17) | +2.62 (0.20) | 4.4% | 45% | 0.41 [0.37, 0.47] |
| 6 | 90 | 5.47 | +4.37 (0.24) |  | 2.2% | 40% | 0.38 [0.27, 0.50] |
| 7..8 | 146 | 5.77 | +4.77 (0.35) |  | 7.5% |  |  |
| 9 | 37 | 3.41 | +2.28 (1.13) |  | 18.9% | 30% | 0.31 [0.18, 0.48] |
| 10 | 189 | 5.53 | +4.14 (0.43) | +4.55 (0.44) | 8.5% | 42% | 0.40 [0.32, 0.49] |

**Alpha (ordered pairs, gap >= 1 day)** (2,089 rows)

| received x | n | mean y | shift vs +1 (SE) | y - habit (SE) | P(y < 0) | P(y = x) | copy excess |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| -10 | 56 | -8.45 | -8.68 (0.74) | -9.30 (0.93) | 96.4% | 79% | 0.71 [0.54, 0.83] |
| -9..-6 | 2 | -10.00 | -9.57 (0.58) |  | 100.0% |  |  |
| -5..-4 | 7 | -3.00 | -3.98 (1.88) |  | 57.1% |  |  |
| -3..-2 | 12 | -4.83 | -6.69 (1.17) |  | 91.7% |  |  |
| -1 | 17 | -1.71 | -2.33 (1.33) | -2.70 (1.52) | 70.6% | 41% |  |
| 1 | 911 | 1.01 | 0 (ref.) | +0.16 (0.13) | 9.7% | 53% | 0.00 [-0.08, 0.09] |
| 2 | 361 | 1.94 | +1.08 (0.24) | +1.01 (0.21) | 8.3% | 35% | 0.23 [0.16, 0.29] |
| 3 | 253 | 2.56 | +1.53 (0.29) | +1.42 (0.24) | 8.7% | 30% | 0.21 [0.16, 0.27] |
| 4 | 120 | 3.56 | +2.58 (0.28) | +2.13 (0.31) | 5.8% | 28% | 0.24 [0.14, 0.35] |
| 5 | 172 | 3.55 | +2.47 (0.35) | +2.26 (0.34) | 8.7% | 30% | 0.25 [0.17, 0.31] |
| 6 | 31 | 5.42 | +4.74 (0.51) |  | 6.5% | 26% | 0.27 [0.08, 0.46] |
| 7..8 | 67 | 5.75 | +5.29 (0.62) |  | 11.9% |  |  |
| 9 | 19 | 2.21 | +1.33 (1.67) |  | 26.3% | 16% |  |
| 10 | 61 | 4.30 | +3.34 (0.69) | +2.79 (0.66) | 13.1% | 26% | 0.21 [0.09, 0.34] |

The response rises by a near-constant step from +1 to +4 (about 0.8 per point) with no flat stretch, saturates between 5 and 8, and is erratic at 9-10 (few rows, a minority of such ratings is answered, section 3.3). A negative rating turns the response negative in almost every case. Beyond what the responder's habit gives, a third to a half of the responses repeat a positive received rating exactly, at every size from +2 to +10 (OTC copy excess 0.31 to 0.51): the copy share does not grow with size (if anything it falls), the opposite of a gate that opens for large ratings. On Alpha the copy excess at +1 is nil (its ordered pairs are the slow ones; section 5.5 shows that copying decays with the gap). Exact copying is the norm on OTC: 72% of all responses repeat the received rating exactly (83% of the responses within ten minutes, 40% of those a day or more later; 54% when the received rating is above +1); on Alpha's ordered pairs 44% (32% above +1).

### 3.2 Is the response flat over a band? (the defining property of a dead zone)

| band (observed ratings inside it) | df | OTC chi2 | p | OTC contrasts vs +1 | Alpha chi2 | p | Alpha contrasts vs +1 |
| --- | ---: | ---: | ---: | --- | ---: | ---: | --- |
| positive band {1, 2}: response at +2 equals response at +1 | 1 | 220.9 | < 1e-10 | [+0.85] | 19.0 | = 1e-05 | [+1.06] |
| positive band {1, 2, 3}: flat over 1-3 | 2 | 469.3 | < 1e-10 | [+0.85, +1.64] | 41.6 | = 9e-10 | [+1.06, +1.54] |
| positive band {1, ..., 4}: flat over 1-4 | 3 | 723.6 | < 1e-10 | [+0.85, +1.64, +2.53] | 89.0 | < 1e-10 | [+1.06, +1.54, +2.60] |
| positive band {1, ..., 5}: flat over 1-5 | 4 | 856.5 | < 1e-10 | [+0.85, +1.64, +2.53, +2.82] | 100.5 | < 1e-10 | [+1.06, +1.54, +2.60, +2.49] |
| symmetric band of absolute rating 1: response at -1 equals response at +1 | 1 | 28.2 | = 1e-07 | [-4.10] | 3.2 | = 0.074 | [-2.30] |
| symmetric band of absolute rating up to 2: flat over -2, -1, +1, +2 | 3 | 278.1 | < 1e-10 | [-6.57, -4.10, +0.85] | 80.6 | < 1e-10 | [-7.92, -2.30, +1.06] |

Every band that holds two or more observed ratings is rejected on both platforms except the symmetric band {-1, +1} on Alpha, where only 17 responses follow a -1 (the OTC estimate for the same band is -4.1, SE 0.8). A dead zone consisting of the single rating +1 cannot be tested by flatness; it is the zero-crossing discussed in the verdict. The +2 contrast is 15 SE from zero on OTC and 4.5 SE on Alpha.

*A dead zone hidden under a linear association* (added at review). These tests are of the association. If part of it is a shared view of the deal, that part adds slope inside any band, and a dead zone in the influence would be masked; but if the added part is linear over +1..+4, the O-jive's bounded step still shows as an excess increment at K+. The increments of the response from +1 to +2, +2 to +3 and +3 to +4 are +0.85, +0.79, +0.89 on OTC (equal: chi2(2) = 0.21, p = 0.898) and +1.06, +0.48, +1.05 on Alpha (chi2(2) = 1.23, p = 0.540); from +4 to +5 it is +0.29 on OTC and -0.11 on Alpha, smaller, the opposite of a step. No step at +2, +3, +4 or +5 sits on the line. A shared view that is not linear in x could still mask one.

### 3.3 Sign and magnitude

The four-number profile of the response function (exploratory summary; responder fixed effects; cluster-robust SE in parentheses; 95% cluster-bootstrap CI in brackets):

| parameter | OTC | Alpha |
| --- | ---: | ---: |
| slope over received ratings 1-4 (points per point) | +0.83 (0.03) [0.77, 0.89] | +0.83 (0.10) [0.64, 1.02] |
| level shift for 5-8 against +1 | +3.44 (0.15) [3.14, 3.73] | +3.38 (0.34) [2.72, 3.99] |
| level shift for 9-10 against +1 | +3.84 (0.43) [3.03, 4.63] | +2.79 (0.71) [1.33, 4.19] |
| level shift for a negative received rating | -8.36 (0.34) [-8.96, -7.66] | -6.64 (0.65) [-8.03, -5.27] |
| within-responder R2: profile / linear / saturated | 0.350 / 0.341 / 0.376 | 0.203 / 0.198 / 0.238 |

Clustering by first rater or two-way (responder and first rater) leaves the OTC standard errors where they are (slope 1-4: 0.031 by responder, 0.030 by first rater, 0.033 two-way; negative jump 0.34, 0.28, 0.34).

*Sign margin.* After a negative received rating the response is negative in 94.7% of 321 cases (OTC) and 86.0% of 107 (Alpha); after a positive one in 2.5% of 13,779 and 8.1% of 2,632. With responder effects the difference is +0.876 (0.018) (OTC) and +0.753 (0.047) (Alpha).

*Extensive margin* (does he answer at all? OTC; first ratings of the last 30 days dropped): the share of first ratings answered by a rating within a day is 62% for +1, 62% for +2, 52% for +3, 38% for +5, 27% for +10 and 7% for -10 (within 30 days: 70%, 72%, 66%, 52%, 37%, 9%). The probability of answering is flat over +1 and +2, falls steadily with larger ratings and collapses after a negative one. The intensive-margin curve above is therefore estimated on a selected set of responders, selected more tightly at high x; the high bins should be read with that in mind.

### 3.4 Drift by year (response year)

**OTC**

| year | pairs | FE rows | +2 vs +1 | slope 1-4 | 5-8 | 9-10 | negative | dead-zone fit: graded / step |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2010 | 51 | 32 | too few |  |  |  |  |  |
| 2011 | 3,406 | 2,667 | +0.62 (0.10) | +0.72 (0.06) | +3.53 (0.25) | +5.84 (0.62) | -9.81 (0.56) | K+=2, K-=1 / 4, 1 |
| 2012 | 3,723 | 2,941 | +0.71 (0.11) | +0.78 (0.06) | +3.06 (0.33) | +4.50 (0.88) | -7.88 (0.86) | K+=2, K-=1 / 3, 3 |
| 2013 | 4,957 | 3,987 | +0.97 (0.12) | +0.84 (0.06) | +3.24 (0.28) | +2.97 (0.64) | -9.62 (0.44) | K+=2, K-=1 / 3, 2 |
| 2014 | 1,524 | 1,192 | +0.93 (0.20) | +0.98 (0.09) | +3.66 (0.34) | +1.61 (1.53) | -6.98 (0.89) | K+=2, K-=1 / 3, 2 |
| 2015 | 418 | 312 | +1.16 (0.28) | +0.87 (0.15) | +3.51 (0.73) | +7.32 (1.32) | -8.65 (1.61) | K+=2, K-=1 / 4, 1 |
| 2016 | 21 | 6 | too few |  |  |  |  |  |

Linear trend per year over 2011-2015 (pooled, responder FE; its SE allows no year-to-year scatter about the line): slope 1-4 +0.073 (0.026), negative jump +0.92 (0.38), 9-10 level -1.21 (0.36), 5-8 level +0.09 (0.13).

From the yearly estimates of the table (weighted by 1/SE^2; the SE inflated when the years scatter about the line more than their SEs allow; added at review): slope 1-4 +0.064 (0.027) (lack of fit chi2(3) = 1.1, p = 0.767), negative jump +0.40 (0.45) (lack of fit chi2(3) = 8.5, p = 0.037), 9-10 level -0.45 (0.70) (lack of fit chi2(3) = 16.4, p = 9e-04), 5-8 level +0.02 (0.12) (lack of fit chi2(3) = 2.2, p = 0.524).

**Alpha**

| year | pairs | FE rows | +2 vs +1 | slope 1-4 | 5-8 | 9-10 | negative | dead-zone fit: graded / step |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 2010 | 7 | 0 | too few |  |  |  |  |  |
| 2011 | 600 | 344 | +0.73 (0.49) | +0.75 (0.19) | +3.68 (0.58) | +4.62 (0.78) | -7.95 (1.57) | K+=2, K-=1 / 5, 1 |
| 2012 | 879 | 648 | +0.59 (0.46) | +0.78 (0.18) | +2.57 (0.56) | +3.45 (1.50) | -6.84 (1.14) | K+=2, K-=1 / 3, 2 |
| 2013 | 727 | 494 | +2.45 (0.69) | +1.18 (0.20) | +3.81 (0.72) | +4.11 (1.64) | -7.06 (1.40) | K+=2, K-=2 / 2, 2 |
| 2014 | 454 | 355 | +0.29 (0.58) | +0.79 (0.22) | +3.54 (0.67) | -0.28 (1.43) | -5.13 (1.29) | K+=3, K-=2 / 3, 2 |
| 2015 | 70 | 50 | too few |  |  |  |  |  |
| 2016 | 2 | 0 | too few |  |  |  |  |  |

Linear trend per year over 2011-2014 (pooled, responder FE; its SE allows no year-to-year scatter about the line): slope 1-4 +0.123 (0.084), negative jump +1.14 (0.66), 9-10 level -1.23 (0.52), 5-8 level +0.12 (0.33).

From the yearly estimates of the table (weighted by 1/SE^2; the SE inflated when the years scatter about the line more than their SEs allow; added at review): slope 1-4 +0.063 (0.105) (lack of fit chi2(2) = 2.6, p = 0.272), negative jump +0.83 (0.62) (lack of fit chi2(2) = 0.4, p = 0.807), 9-10 level -1.35 (0.51) (lack of fit chi2(2) = 2.1, p = 0.355), 5-8 level +0.07 (0.33) (lack of fit chi2(2) = 2.7, p = 0.262).

On OTC the response at +2 exceeds the response at +1 in every estimable year (z from 4.2 up), and the graded dead-zone fit is the one-rating band every year. On Alpha it is positive in all 4 estimable years but individually significant only in 2013 (SE 0.5-0.7 per year; the pooled test of section 3.2 is the sharper one); the band differs from the one-rating band in 2013, 2014. On OTC the 1-4 slope strengthens modestly; the sign jump and the 9-10 level move from year to year without a trend that survives the scatter (z = +0.9 and -0.6; the 9-10 level is highest in 2015). Corrected at review: this paragraph said the sign jump weakens and the 9-10 level falls, from the pooled trends alone.

## 4. One-sided, two-sided and dead-zone forms compared

In-sample (BIC, within-responder R2) and out-of-sample (10-fold CV mean squared error of the response, in squared rating points). 'params' = mean parameters plus searched thresholds. 'vs best' = difference from the best PRE-SPECIFIED form, with a cluster-robust SE. Exploratory forms are starred.

**OTC** (11,795 rows, 11,795 scored in CV)

| form | thresholds | params | R2 (within) | BIC - best pre-spec. | CV MSE | CV vs best pre-spec. (SE) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| null (no response) |  | 0 | 0.000 | +5318 | 8.651 | +3.270 (0.284) |
| linear (two-sided, no gate) |  | 1 | 0.341 | +414 | 5.576 | +0.195 (0.044) |
| one-sided, positive only, step | K+=3 | 2 | 0.127 | +3742 | 7.550 | +2.169 (0.242) |
| one-sided, positive only, hinge | knot +1 | 2 | 0.160 | +3274 | 7.179 | +1.798 (0.230) |
| one-sided, positive only, graded | K+=2 | 3 | 0.170 | +3142 | 7.119 | +1.738 (0.221) |
| one-sided, negative only, step | K-=-2 | 2 | 0.219 | +2425 | 6.798 | +1.417 (0.105) |
| one-sided, negative only, hinge | knot -1 | 2 | 0.215 | +2476 | 6.767 | +1.386 (0.110) |
| one-sided, negative only, graded | K-=-1 | 3 | 0.237 | +2159 | 6.582 | +1.201 (0.095) |
| two-sided, no dead zone, step | K+=1, K-=-1 | 1 | 0.218 | +2420 | 6.734 | +1.353 (0.106) |
| two-sided at the origin, hinge (knots +1 and -1: flat over {-1, +1}, no jump) | knot +1, knot -1 | 2 | 0.345 | +355 | 5.557 | +0.176 (0.048) |
| two-sided, no dead zone, graded | K+=1, K-=-1 | 3 | 0.362 | +54 | 5.409 | +0.028 (0.012) |
| dead zone (O-jive), step | K+=3, K-=-2 | 4 | 0.321 | +796 | 5.868 | +0.487 (0.065) |
| dead zone (O-jive), hinge | knot +1, knot -1 | 4 | 0.345 | +374 | 5.557 | +0.176 (0.048) |
| dead zone (O-jive), graded | K+=2, K-=-1 | 6 | 0.366 | +0 | 5.381 | best |
| saturated (one mean per rating bin) |  | 13 | 0.376 | -123 | 5.357 | -0.024 (0.032) |
| clipped mirror (exploratory) * | knee U=7 | 2 | 0.346 | +320 | 5.552 | +0.171 (0.042) |
| sign jump + clipped positive mirror (exploratory) * | knee U=6 | 3 | 0.354 | +188 | 5.495 | +0.114 (0.050) |
| sign jump + clipped mirror (exploratory) * | knee U=7 | 3 | 0.370 | -96 | 5.359 | -0.022 (0.020) |
| no band, two slopes on the positive side (exploratory) * | knee K=8 | 5 | 0.372 | -120 | 5.372 | -0.009 (0.028) |

**Alpha** (2,089 rows, 2,089 scored in CV)

| form | thresholds | params | R2 (within) | BIC - best pre-spec. | CV MSE | CV vs best pre-spec. (SE) |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| null (no response) |  | 0 | 0.000 | +471 | 18.951 | +3.972 (0.692) |
| linear (two-sided, no gate) |  | 1 | 0.198 | +17 | 15.139 | +0.161 (0.132) |
| one-sided, positive only, step | K+=2 | 2 | 0.089 | +290 | 17.415 | +2.437 (0.490) |
| one-sided, positive only, hinge | knot +1 | 2 | 0.102 | +261 | 16.970 | +1.991 (0.451) |
| one-sided, positive only, graded | K+=2 | 3 | 0.117 | +233 | 16.735 | +1.757 (0.418) |
| one-sided, negative only, step | K-=-2 | 2 | 0.126 | +204 | 16.689 | +1.711 (0.357) |
| one-sided, negative only, hinge | knot -1 | 2 | 0.118 | +225 | 16.721 | +1.742 (0.350) |
| one-sided, negative only, graded | K-=-1 | 3 | 0.132 | +197 | 16.588 | +1.610 (0.332) |
| two-sided, no dead zone, step | K+=1, K-=-1 | 1 | 0.117 | +219 | 16.860 | +1.882 (0.382) |
| two-sided at the origin, hinge (knots +1 and -1: flat over {-1, +1}, no jump) | knot +1, knot -1 | 2 | 0.199 | +22 | 15.137 | +0.159 (0.124) |
| two-sided, no dead zone, graded | K+=1, K-=-1 | 3 | 0.210 | +0 | 15.008 | +0.030 (0.077) |
| dead zone (O-jive), step | K+=4, K-=-2 | 4 | 0.193 | +54 | 15.595 | +0.617 (0.184) |
| dead zone (O-jive), hinge | knot +1, knot -1 | 4 | 0.199 | +37 | 15.137 | +0.159 (0.124) |
| dead zone (O-jive), graded | K+=2, K-=-1 | 6 | 0.216 | +7 | 14.978 | best |
| saturated (one mean per rating bin) |  | 13 | 0.238 | +2 | 14.816 | -0.162 (0.179) |
| clipped mirror (exploratory) * | knee U=6 | 2 | 0.210 | -5 | 15.029 | +0.051 (0.152) |
| sign jump + clipped positive mirror (exploratory) * | knee U=6 | 3 | 0.207 | +8 | 15.144 | +0.166 (0.175) |
| sign jump + clipped mirror (exploratory) * | knee U=7 | 3 | 0.220 | -25 | 14.892 | -0.087 (0.105) |
| no band, two slopes on the positive side (exploratory) * | knee K=8 | 5 | 0.227 | -28 | 14.773 | -0.206 (0.152) |

\* exploratory, chosen after seeing the means.

**Paired comparisons that carry the verdict** (CV squared error, first minus second, positive = the second is better; cluster-robust SE):

| comparison | OTC | Alpha |
| --- | ---: | ---: |
| D-step vs T-graded | +0.459 (0.070); z = +6.5 | +0.587 (0.191); z = +3.1 |
| D-step vs D-graded | +0.487 (0.065); z = +7.5 | +0.617 (0.184); z = +3.3 |
| T-graded vs D-graded | +0.028 (0.012); z = +2.3 | +0.030 (0.077); z = +0.4 |
| linear vs T-graded | +0.167 (0.039); z = +4.2 | +0.131 (0.111); z = +1.2 |
| T-step vs T-graded | +1.325 (0.111); z = +12.0 | +1.852 (0.376); z = +4.9 |
| T-hinge (flat over {-1, +1}) vs T-graded | +0.149 (0.046); z = +3.2 | +0.129 (0.119); z = +1.1 |
| O+ graded vs T-graded | +1.710 (0.221); z = +7.7 | +1.727 (0.430); z = +4.0 |
| O- graded vs T-graded | +1.173 (0.100); z = +11.8 | +1.580 (0.333); z = +4.7 |
| D-graded vs clipped mirror + jump | +0.022 (0.020); z = +1.1 | +0.087 (0.105); z = +0.8 |
| T-graded vs clipped mirror + jump | +0.050 (0.025); z = +2.0 | +0.117 (0.094); z = +1.2 |
| clipped mirror + jump vs saturated | +0.002 (0.023); z = +0.1 | +0.075 (0.152); z = +0.5 |
| D-graded vs no-band two slopes | +0.009 (0.028); z = +0.3 | +0.206 (0.152); z = +1.4 |
| T-graded vs no-band two slopes | +0.037 (0.033); z = +1.1 | +0.236 (0.153); z = +1.5 |
| no-band two slopes vs saturated | +0.015 (0.020); z = +0.8 | -0.044 (0.128); z = -0.3 |

Reading: (i) the literal O-jive (D, step) loses clearly to the graded two-sided forms; (ii) closing the band (T, graded) costs 0.028 on OTC (z = 2.3), but the dead-zone graded fit with the one-rating band is the same function class as a no-band two-slope curve with its knee at +2, and the no-band two-slope curve with the knee where the data put it (+8 on OTC, +8 on Alpha) is as good out of sample and better by BIC with one threshold instead of two, so what the band buys is a decrease of slope, not a zone; (iii) one-sided forms lose by a wide margin, so both sides respond; (iv) the linear form loses to the two-line form because of the sign jump.

### 4.1 Thresholds: how stable are they? (cluster bootstrap over responders)

| platform | form | K+ (share of draws) | K- (share of draws, >= 2%) | band empty | narrowest band (K+ = K- = 1) | most frequent (K+, K-) |
| --- | --- | --- | --- | ---: | ---: | --- |
| OTC | D, step | 3: 85%, 4: 15% | -1: 38%, -2: 51%, -3: 2%, -5: 8% | 0% | 0% | (3,2): 44%, (3,1): 30%, (4,1): 7% |
| OTC | D, graded | 2: 100% | -1: 100% | 0% | 0% | (2,1): 100% |
| OTC | D, hinge (K = knot) | 1: 100% | -1: 100% | 0% | 100% | (1,1): 100% |
| Alpha | D, step | 2: 13%, 3: 30%, 4: 56%, 6: 1% | -1: 18%, -2: 69%, -5: 8%, -6: 5% | 0% | 0% | (4,2): 38%, (3,2): 22%, (4,1): 13% |
| Alpha | D, graded | 2: 95%, 3: 4% | -1: 56%, -2: 42% | 0% | 0% | (2,1): 53%, (2,2): 41%, (3,1): 3% |
| Alpha | D, hinge (K = knot) | 1: 100% | -1: 99% | 0% | 99% | (1,1): 99% |

For step and graded the narrowest band is empty. For the hinge it is not: a hinge is zero at its knot, so knots at +1 and -1 give those two ratings the same response, and a hinge band is never empty (corrected at review: this table reported the hinge's band as empty in 100% of OTC draws). The continuous dead-zone form takes that narrowest band, flat over {-1, +1}, in 100% of OTC and 99% of Alpha draws, and it loses out of sample to the same form with a sign jump (T, graded) by 0.149 (3.2 SE) on OTC and 0.129 (1.1 SE) on Alpha: the smallest dead zone a continuous O-jive can have is rejected where the -1 cell has rows (OTC), as the flatness test of {-1, +1} says.

Clipped-mirror knee (exploratory): OTC 7 ([6, 8]; draws 6: 38%, 7: 54%, 8: 8%); Alpha 7 ([6, 8]). Knee of the no-band two-slope curve (exploratory): OTC 7 ([4, 8]), Alpha 8 ([2, 8]).

The step form's K+ of 3-4 is not a dead zone: a single bounded step is the best one-step approximation to a ramp, so the search puts it where the ramp is steepest (the profile of RSS against K+ below is lowest at 3 for the step and at 2 for the graded form), and the flatness tests reject the band it implies.

Residual sum of squares by positive threshold K+ (best K- for each), OTC; lower is better:

| K+ | step: RSS - best | graded: RSS - best |
| ---: | ---: | ---: |
| 1 | +7470 (K-=-2) | +326 (K-=-1) |
| 2 | +1484 (K-=-2) | +0 (K-=-1) |
| 3 | +0 (K-=-2) | +761 (K-=-1) |
| 4 | +375 (K-=-2) | +2095 (K-=-1) |
| 5 | +1462 (K-=-2) | +3372 (K-=-1) |
| 6 | +2932 (K-=-2) | +4997 (K-=-1) |
| 7 | +4002 (K-=-2) | +6064 (K-=-1) |
| 8 | +4430 (K-=-2) | +6462 (K-=-1) |
| 9 | +5811 (K-=-2) | +7766 (K-=-1) |
| 10 | +5763 (K-=-2) | +7828 (K-=-1) |

## 5. Variations

**Which model variant fits best.** Among the pre-specified forms the best out-of-sample on OTC is *dead zone (O-jive), graded* and on Alpha *dead zone (O-jive), graded*. On Alpha it is not separable from the no-band two-line form (T, graded; 0.030, z = 0.4); on OTC the margin is 0.028 squared points (z = 2.3) and is the one-rating band, which section 4 shows to be a knee at +2. Overall the best description, pre-specified or not, is a no-band curve: the exploratory two-slope form (BIC -120 against the dead-zone graded fit on OTC, -35 on Alpha) and the sign-jump-plus-clipped-mirror form (3 parameters including the knee) are each within one SE of the saturated reference on both platforms. The variants below change what is held fixed; none restores a dead zone.

### 5.1 Controls

| control set | platform | n | slope 1-4 | 5-8 | negative | dead-zone fit (graded) | best form by BIC | BIC: D graded - T graded |
| --- | --- | ---: | ---: | ---: | ---: | --- | --- | ---: |
| none (pooled) | OTC | 14,100 | +0.82 (0.03) | +3.54 (0.13) | -8.84 (0.28) | K+=2, K-=1 | dead zone (O-jive), graded | -25 |
| none (pooled) | Alpha | 2,739 | +0.80 (0.08) | +3.21 (0.25) | -7.23 (0.57) | K+=2, K-=1 | two-sided, no dead zone, graded | +10 |
| responder FE (primary) | OTC | 11,795 | +0.83 (0.03) | +3.44 (0.15) | -8.36 (0.34) | K+=2, K-=1 | dead zone (O-jive), graded | -54 |
| responder FE (primary) | Alpha | 2,089 | +0.83 (0.10) | +3.38 (0.34) | -6.64 (0.65) | K+=2, K-=1 | two-sided, no dead zone, graded | +7 |
| responder + first-rater FE | OTC | 10,707 | +0.88 (0.03) | +3.63 (0.14) | -7.36 (0.45) | K+=2, K-=1 | dead zone (O-jive), graded | -64 |
| responder + first-rater FE | Alpha | 1,520 | +0.64 (0.10) | +3.36 (0.34) | -6.84 (0.88) | K+=2, K-=1 | two-sided, no dead zone, graded | +16 |
| habit, first rater's habit, reputation (whole file) | OTC | 10,823 | +0.79 (0.03) | +3.39 (0.14) | -7.40 (0.33) | K+=2, K-=1 | dead zone (O-jive), graded | -15 |
| habit, first rater's habit, reputation (whole file) | Alpha | 2,014 | +0.68 (0.07) | +2.68 (0.24) | -6.29 (0.68) | K+=2, K-=1 | two-sided, no dead zone, graded | +8 |
| same, earlier events only | OTC | 7,753 | +0.76 (0.04) | +3.32 (0.16) | -7.71 (0.36) | K+=2, K-=1 | dead zone (O-jive), graded | -14 |
| same, earlier events only | Alpha | 1,537 | +0.65 (0.09) | +2.46 (0.30) | -6.62 (0.73) | K+=2, K-=1 | two-sided, no dead zone, graded | +13 |
| responder FE + previous rating | OTC | 9,504 | +0.83 (0.03) | +3.45 (0.16) | -8.04 (0.34) | K+=2, K-=1 | dead zone (O-jive), graded | -56 |
| responder FE + previous rating | Alpha | 1,887 | +0.83 (0.10) | +3.34 (0.36) | -6.52 (0.67) | K+=2, K-=2 | two-sided, no dead zone, graded | +6 |

The 1-4 slope stays between 0.76 and 0.88 on OTC and between 0.64 and 0.83 on Alpha whatever is controlled, and the dead-zone fit is the one-rating band in nearly every row: the response is not produced by stable differences between raters (stingy raters pairing with stingy ones, popular traders with generous ones). The negative jump moves most (-8.8 to -7.4 on OTC), and that is where the cells are thinnest. Pair-specific confounds (a shared deal, a standing partnership) are not removed by any of these.

### 5.2 The level of the received rating, or its deviation from the sender's habit?

**OTC** (rows with a first-rater habit: 11,121; null MSE 8.44)

| design (responder FE) | CV MSE | vs best (SE) |
| --- | ---: | ---: |
| x bins + linear u | 5.165 | best |
| x bins + u bins | 5.167 | +0.002 (0.003) |
| x bins (saturated in x) | 5.168 | +0.003 (0.004) |
| linear in x | 5.334 | +0.169 (0.062) |
| linear in x and u | 5.334 | +0.170 (0.062) |
| sign(x) + u bins | 5.898 | +0.733 (0.065) |
| linear in u | 6.728 | +1.563 (0.147) |
| u bins (saturated in u) | 6.796 | +1.631 (0.139) |

**Alpha** (rows with a first-rater habit: 1,795; null MSE 20.68)

| design (responder FE) | CV MSE | vs best (SE) |
| --- | ---: | ---: |
| x bins + linear u | 16.352 | best |
| x bins + u bins | 16.459 | +0.107 (0.078) |
| x bins (saturated in x) | 16.460 | +0.109 (0.079) |
| linear in x and u | 16.542 | +0.190 (0.270) |
| linear in x | 16.633 | +0.281 (0.281) |
| sign(x) + u bins | 17.276 | +0.924 (0.289) |
| linear in u | 17.811 | +1.460 (0.388) |
| u bins (saturated in u) | 18.207 | +1.855 (0.424) |

The deviation u = x - (first rater's habit) predicts much worse than the level x, and adds nothing once the level is in: the response is to what was said, not to how unusual it was for him to say it. That matches the form of the O-jive (a function of the partner's level, v0.2 section 3 'D2') and argues against a 'surprise' gate.

### 5.3 By embeddedness

**OTC, common neighbours time-respecting (primary)**

| common neighbours | FE rows | slope 1-4 | 5-8 | 9-10 | negative |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 5,957 | +0.73 (0.04) | +3.26 (0.20) | +4.24 (0.54) | -7.80 (0.52) |
| 1-2 | 3,286 | +0.80 (0.06) | +3.20 (0.23) | +3.26 (0.90) | -8.26 (0.57) |
| 3-9 | 1,848 | +0.90 (0.06) | +3.72 (0.33) | +4.60 (0.79) | -9.16 (0.45) |
| 10+ | 704 | +0.84 (0.14) | +3.18 (0.44) | +2.16 (1.28) | -7.73 (1.10) |

Equality across bins (Wald): slope14: chi2(3) = 6.3, p = 0.098; hi58: chi2(3) = 2.2, p = 0.534; hi910: chi2(3) = 3.5, p = 0.324; neg: chi2(3) = 5.2, p = 0.159.

**OTC, common neighbours static**

| common neighbours | FE rows | slope 1-4 | 5-8 | 9-10 | negative |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 2,453 | +0.70 (0.08) | +3.12 (0.32) | +3.48 (0.81) | -7.38 (0.70) |
| 1-2 | 3,627 | +0.71 (0.06) | +3.06 (0.24) | +3.27 (0.77) | -8.11 (0.55) |
| 3-9 | 3,627 | +0.86 (0.05) | +3.42 (0.30) | +4.45 (0.75) | -8.96 (0.44) |
| 10+ | 2,088 | +0.85 (0.06) | +3.52 (0.27) | +3.79 (0.75) | -7.99 (0.80) |

Equality across bins (Wald): slope14: chi2(3) = 5.8, p = 0.120; hi58: chi2(3) = 2.1, p = 0.555; hi910: chi2(3) = 1.4, p = 0.707; neg: chi2(3) = 4.9, p = 0.180.

**Alpha, common neighbours time-respecting (primary)**

| common neighbours | FE rows | slope 1-4 | 5-8 | 9-10 | negative |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 641 | +0.78 (0.16) | +3.62 (0.47) | +4.60 (1.35) | -6.37 (1.10) |
| 1-2 | 552 | +0.84 (0.16) | +2.96 (0.61) | +3.62 (0.62) | -7.45 (1.10) |
| 3-9 | 555 | +0.92 (0.15) | +4.10 (0.66) | +3.99 (1.16) | -6.71 (1.03) |
| 10+ | 341 | +0.56 (0.27) | +2.48 (0.70) | -0.56 (1.77) | -6.55 (1.42) |

Equality across bins (Wald): slope14: chi2(3) = 1.7, p = 0.638; hi58: chi2(3) = 5.5, p = 0.141; hi910: chi2(3) = 6.0, p = 0.111; neg: chi2(3) = 0.5, p = 0.909.

**Alpha, common neighbours static**

| common neighbours | FE rows | slope 1-4 | 5-8 | 9-10 | negative |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0 | 269 | +0.30 (0.24) | +3.84 (0.65) | +0.88 (2.60) | -5.15 (1.24) |
| 1-2 | 456 | +0.96 (0.18) | +3.26 (0.55) | +4.88 (0.72) | -7.73 (1.32) |
| 3-9 | 639 | +1.12 (0.17) | +3.60 (0.72) | +4.47 (0.90) | -6.08 (1.02) |
| 10+ | 725 | +0.46 (0.15) | +2.58 (0.48) | +0.85 (1.10) | -7.39 (1.25) |

Equality across bins (Wald): slope14: chi2(3) = 14.1, p = 0.003; hi58: chi2(3) = 2.9, p = 0.413; hi910: chi2(3) = 12.2, p = 0.007; neg: chi2(3) = 2.3, p = 0.513.

The shape does not depend on embeddedness in any consistent way. In the time-respecting count (primary) no parameter differs across bins at the 5% level on either platform (smallest p = 0.098: OTC, 1-4 slope). In the static count Alpha 1-4 slope differs (p = 0.003); Alpha 9-10 level differs (p = 0.007); the static count credits a pair with neighbours it only acquired after the response, so it is the weaker measure. The 1-4 slope is positive in all 16 bins: the smallest is 0.30 (SE 0.24; Alpha, static count, 0 common neighbours, 269 rows) and the next 0.46 (SE 0.15). Leskovec et al.'s embeddedness effect concerns triads, not this dyadic response; 112 section 6.5 test 5 (visibility at low embeddedness) is a different question and is not answered here.

### 5.4 By platform

| sample | FE rows | slope 1-4 | 5-8 | 9-10 | negative |
| --- | ---: | ---: | ---: | ---: | ---: |
| OTC, gap >= 1 day | 2,396 | +0.89 (0.10) | +3.42 (0.35) | +2.35 (0.72) | -6.67 (0.58) |
| OTC, gap < 1 day | 8,691 | +0.82 (0.02) | +3.60 (0.12) | +4.71 (0.47) | -9.35 (0.34) |
| Alpha, ordered (gap >= 1 day) | 2,089 | +0.83 (0.10) | +3.38 (0.34) | +2.79 (0.71) | -6.64 (0.65) |
| Alpha, same-day pairs (random orientation) | 6,291 | +0.81 (0.02) | +3.51 (0.15) | +4.90 (0.43) | -7.31 (0.73) |

Like for like the platforms agree: OTC with a gap of a day or more against Alpha's ordered pairs differ by z = slope14 +0.5, hi58 +0.1, hi910 -0.4, neg -0.0; OTC under a day against Alpha's same-day pairs (an arbitrary orientation, so an association rather than a time-ordered response) by z = slope14 +0.4, hi58 +0.5, hi910 -0.3, neg -2.5; beyond 2 SE: neg (z = -2.5, fast and same-day pairs). The full-OTC and full-Alpha columns of section 3 differ mainly because Alpha's ordered pairs are all slow. Reciprocated pairs carrying opposite signs (112 section 6.5 test 4): OTC 358 of 14,100 (2.5%), Alpha 248 of 10,062 (2.5%): rare.

### 5.5 By the gap between the two ratings

**OTC**

| gap | FE rows | slope 1-4 | 5-8 | 9-10 | negative |
| --- | ---: | ---: | ---: | ---: | ---: |
| a: < 10 min | 6,720 | +0.84 (0.02) | +3.62 (0.14) | +5.56 (0.51) | -9.19 (0.57) |
| b: 10 min - 1 d | 2,188 | +0.81 (0.06) | +3.73 (0.20) | +4.92 (0.80) | -8.95 (0.40) |
| c: 1 d - 30 d | 1,642 | +0.81 (0.09) | +3.23 (0.38) | +3.93 (0.78) | -7.42 (0.55) |
| d: > 30 d | 1,245 | +0.94 (0.14) | +3.43 (0.39) | +1.27 (1.01) | -7.21 (0.79) |

Equality across gaps (Wald): slope14: chi2(3) = 0.9, p = 0.834; hi58: chi2(3) = 1.8, p = 0.608; hi910: chi2(3) = 15.8, p = 0.001; neg: chi2(3) = 11.8, p = 0.008.

**Alpha**

| gap | FE rows | slope 1-4 | 5-8 | 9-10 | negative |
| --- | ---: | ---: | ---: | ---: | ---: |
| c: 1 d - 30 d | 1,126 | +0.79 (0.11) | +3.38 (0.40) | +4.53 (0.67) | -6.23 (0.94) |
| d: > 30 d | 963 | +0.89 (0.15) | +3.39 (0.46) | +1.37 (1.04) | -6.91 (0.83) |

Equality across gaps (Wald): slope14: chi2(1) = 0.3, p = 0.556; hi58: chi2(1) = 0.0, p = 0.973; hi910: chi2(1) = 7.2, p = 0.007; neg: chi2(1) = 0.3, p = 0.577.

Copy excess by gap (OTC; 95% cluster-bootstrap CI):

| gap | pairs | copy excess at +1 | at +2 | at +3 |
| --- | ---: | ---: | ---: | ---: |
| < 1 min | 3,443 | 0.82 [0.79, 0.85] | 0.66 [0.61, 0.70] | 0.62 [0.54, 0.70] |
| 1-10 min | 4,770 | 0.67 [0.64, 0.71] | 0.63 [0.59, 0.67] | 0.58 [0.52, 0.65] |
| 10 min - 1 h | 1,346 | 0.55 [0.45, 0.63] | 0.60 [0.51, 0.68] | 0.50 [0.36, 0.61] |
| 1 h - 1 d | 1,437 | 0.35 [0.24, 0.45] | 0.49 [0.41, 0.59] | 0.54 [0.43, 0.63] |
| 1 d - 30 d | 1,820 | -0.14 [-0.27, -0.04] | 0.27 [0.20, 0.35] | 0.25 [0.16, 0.32] |
| > 30 d | 1,284 | -0.64 [-0.81, -0.49] | 0.12 [0.04, 0.19] | 0.14 [0.08, 0.21] |

The slope over 1-4 is the same for responses a minute later and responses a month later; what changes with the gap is how often the response is an exact copy at +1 (high within minutes, 'rate for rate'; below the responder's habit after a day), the 9-10 level (p = 0.001 on OTC, p = 0.007 on Alpha) and, on OTC, the size of the negative jump (p = 0.008). The graded response survives the delay; the exact mirroring does not.

### 5.6 Time-reversed placebo

Swap the roles: regress the EARLIER rating on the LATER one (fixed effect for the first rater). If the two ratings were exchangeable it would be symmetric; two views of one deal give that only with equal noise and spread in the two views (section 2, null 4). OTC reversed: slope 1-4 +0.68 (0.03), 5-8 +3.09 (0.12), 9-10 +3.91 (0.29), negative -3.22 (0.64) (forward: +0.83, +3.44, +3.84, -8.36). Alpha reversed: slope +0.55 (0.07), negative -1.92 (0.70) (forward +0.83, -6.64). The graded positive slope is smaller in reverse but of the same order (+0.68 (0.03) against +0.83 (0.03)), as compatible with a shared view of one deal as with a response. The negative jump is not: a negative first rating is answered by a negative one 95% of the time (OTC; Alpha 86%), but only 47% of the 645 negative responses followed a negative first rating (Alpha 30%). The rest are negative ratings given after a positive one. That asymmetry is what retaliation predicts; it is also what a scam sequence produces (a seller rates the buyer well at the deal, the cheated buyer rates him badly later), and no field of the file separates the two. Neither direction has a dead zone.

### 5.7 Capped responders

At most three response pairs per responder, chosen at random (so that busy responders cannot carry the curve): OTC 5,266 rows, slope 1-4 +0.78 (0.05), negative -9.20 (0.50); Alpha 1,054 rows, slope +0.89 (0.15), negative -6.54 (1.09).

## 6. Caveats

1. **Association, not isolated causation.** The two ratings follow one deal and arrive minutes apart; time order does not remove a shared view of the deal or an agreement to rate each other. The time-reversed check (5.6) finds the negative side asymmetric and the positive slope nearly symmetric. A causal reading of the positive slope needs variation in what a responder knew when he rated, which the file lacks.
2. **The response function is estimated on responders.** Whether a trader answers at all depends strongly on the received rating (3.3), so the shape at high x describes a selected set. The REV2 paper (Kumar et al. 2018) is about fraudulent ratings in these two networks; this file does not say which ratings are fraudulent, and the 9-10 bins are the least stable across years and gaps.
3. **Resolution.** Ratings are integers and none is zero. A flat band narrower than one rating point cannot be seen; the data say only that no band of two or more observed ratings is flat. The 'band' of the best dead-zone fit is one rating, +1, and carries no evidence of a zone.
4. **Thin negative side.** 321 OTC and 107 Alpha received ratings are negative (214 and 59 of them -10). The -1..-5 cells hold 50 or fewer rows each; claims about thresholds below -1 are not supported either way.
5. **Alpha timestamps are days.** 73% of its reciprocated pairs are unorderable and kept out of the ordered analysis; the ordered ones are slow. The platform comparison is made like for like for that reason.
6. **Researcher degrees of freedom and multiple comparisons.** See section 2: the first look preceded the forms. Thresholds are chosen on grids; the CV re-chooses them inside folds, the BIC counts them. No multiple-comparison correction is applied to the many tables of section 5; the conclusions do not rest on any single cell. Checked at review against a Bonferroni correction: the flatness rejections the verdict uses survive it across all 12 flatness tests (largest p = 1e-05, corrected p = 2e-04); D-step against T-graded, across the 14 paired comparisons of a platform, survives it on OTC (corrected p = 9e-10) and survives it narrowly on Alpha (corrected p = 0.030; it sits near the line and moves with the number of CV repeats). The drift claims did not survive the year-to-year scatter and were cut at review (section 3.4); the one kept, the 1-4 slope's, is modest and is one of four parameters tried. The head-on flatness tests are Wald tests, not calibrated against a threshold-search null; the claim that freeing the band helps is the modest one (z about 2 on OTC) and is not leaned on.
7. **One population.** Pseudonymous Bitcoin traders 2010-2016 on two IRC-era web-of-trust sites; the sign means 'trust after a deal'. Not couples (the O-jive's origin), not teams, not Wikipedia.
8. **Ratings are treated as numbers.** The fits are least squares on the rating; no ordinal model was fitted. The two discrete outcomes of sections 3.1 and 3.3 (a negative response; an exact copy) are the checks on the coding, and agree with the numeric picture.

## 7. What this does to the model (proposals, not adopted)

- `models/00-v0.md` section 4.1 and 3 'D2': the O-jive's dead zone is not found in this dyadic rating medium. Where the coupling is measured by a rating of the partner, write I(x) as a graded function with a sign jump and a saturation knee; keep the dead-zone widths as soft settings that start at 0 (112 section 6.3 already says so). The couples evidence for a husband's K- (L0834) is one of ten tests in one cohort and stays quarantined; this result is neither support nor refutation of it, because the medium differs.
- The linear partner term of L4367 (about 0 at 6 s in couples) does not carry over: the linear term here is large (about 0.8 per point) and the sign jump larger still. Bitcoin ratings are a communicated, public, post-deal evaluation, not a moment-by-moment affect; the two media should not share one coupling constant.
- 112 section 6.5 test 4 (symmetry): opposite-sign reciprocated pairs are 2.5% (OTC) and 2.5% (Alpha), so the condition that section sets for using R-A's symmetric layer without a symmetrisation rule holds in this medium; the asymmetry that remains is the time-ordered negative response of 5.6.
- For the sign law (R-X, exchange as sentiment): ratings given after a deal copy the rating received at a rate that does not grow with its size and decays with the delay. That is an exchange-norm term with a delay parameter, not a drive coupling.

## Reproduction

    cd sim
    ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report fetch    # once; sha256-checked, git-ignored
    ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report report   # writes this file (a few minutes; seeded)
    ~/.local/bin/uv run pytest tests/test_gate_reciprocity_bitcoin.py

The verdict above is guarded: `report` refuses to write the file if any of 59 stated facts (signs, orderings, p-value bounds) stops holding.

## Review (2026-11-01)

A second agent's review: re-run, re-derived, and checked for null models, leakage, multiple comparisons, data terms, ledger ids and the strength of the verdict. This section is appended by hand after the `report` run above; a fresh `report` rewrites everything above it and drops it.

**Re-run and re-derivation.** Before the review: 51 passed, 2 strict xfails, 1 opt-in skip, and `report` reproduced the previous file byte for byte apart from the run time. After it: 57 tests, 54 passed, 2 strict xfails, and the end-to-end test passes with `GATE_RECIPROCITY_E2E=1`; two full `report` runs give identical numbers. The headline numbers were re-derived by a script that shares no code with the module (its own pairing from the CSV, explicit within-responder demeaning, its own cluster sandwich and threshold grid): 14,100 OTC and 2,739 Alpha response pairs; 11,795 and 2,089 FE rows; +2 against +1 +0.853 (0.057), chi2(1) = 220.9 (Alpha +1.059 (0.243), 19.0); flatness over +1..+4 chi2(3) = 723.6 and 89.0; -1 against +1 -4.10 (0.77) on OTC and -2.30 (1.29), p = 0.074 on Alpha; the profile 0.834 / 3.439 / 3.839 / -8.362; the sign margin 94.7%, 2.47%, 47.1% of 645; exact copies 71.8% (83.3% within ten minutes); the D-graded band (2, 1) and the knee-at-2 identity exact. All agree.

**Errors found and fixed (code, tests and this file).**

1. *The two-sided hinge was labelled "no dead zone".* A hinge max(x - K, 0) is zero at its knot, so the T hinge (knots +1 and -1) gives -1 and +1 identical design rows. It is flat over {-1, +1}, a dead zone of two observed ratings. Section 4.1 also reported the D-hinge band "empty" in 100% of OTC draws, and a guard asserted it. `Candidate.band_values` and `threshold_distribution` are now shape-aware, the forms are labelled and their knots shown as knots, and a new paired comparison gives the result the label hid: the continuous form with the narrowest band a hinge can have loses to the same form with a sign jump by 0.149 (3.2 SE) on OTC, and by 1.1 SE on Alpha. Fits, thresholds and the order of candidates are unchanged.
2. *The "earlier events only" control set was not.* `spec_summary("cov_prior")` used the first rater's whole-file habit. A new covariate, `habit_first_prior` (his other initiating ratings before the response), replaces it, with a brute-force test. The rows are now OTC 7,753, slope +0.76 (0.04), negative -7.71 (0.36) (was 8,195, +0.77, -7.78) and Alpha 1,537, +0.65 (0.09), -6.62 (0.73) (was 1,635, +0.68, -6.69). No conclusion moves.
3. *Drift was overstated.* The pooled trend's SE allows no year-to-year scatter about the line. The new `year_trend` fits the yearly estimates by weighted least squares, tests lack of fit and inflates the SE by the scatter. On those terms the rise of the OTC 1-4 slope stands (+0.064 (0.027), lack of fit p = 0.77). The negative jump (+0.92 (0.38) per year, pooled) and the 9-10 level (-1.21 (0.36), pooled) are not linear in year (lack of fit p = 0.037 and 0.0009; the 9-10 level is highest in 2015), and their trends are z = +0.9 and -0.6 against the scatter. The verdict said the negative jump moves towards zero and the 9-10 level falls; it now says no drift is shown for either. The guards changed to match.
4. *The verdict was stronger than the numbers on Alpha.* "Flat over no band that holds two observed ratings, on both platforms" was false for Alpha's {-1, +1} (17 responses to a -1; -2.3 (1.3), p = 0.074), which section 3.2 already conceded. The headline, the "Refuted" item and the negative-side sentence now restrict the refutation to OTC and to Alpha's bands that reach +2. A guard pins that the Alpha band is not rejected.
5. *Association, not influence.* The flatness tests refute a dead zone in the observed response. A shared view of the deal (undecided) adds slope inside any band and could mask a dead zone in the influence. The new `increment_test` covers the linear case, where the O-jive's bounded step would still show as an excess increment. None does: increments +0.85, +0.79, +0.89 on OTC (equal, p = 0.90) and +1.06, +0.48, +1.05 on Alpha (p = 0.54), and a smaller one from +4 to +5. The verdict now says what this covers and what stays undecided (a non-linear shared view).
6. *Smaller items.*
   - The symmetry null (section 2, null 4; section 5.6) said that two views of one deal give symmetric curves. They do only if the two views carry equal noise and spread, so it is now an exchangeability null, and the reversed slope (0.68 (0.03) against 0.83 (0.03)) is "smaller but of the same order", not "close to symmetric".
   - The verdict cited 112 section 6.2 for "start at 0, wide slack"; the words are in 112 section 6.3 and v0.2 section 4.5.
   - The copy share "does not depend on size" now reads "does not grow with size" (0.51 at +2, 0.31 at +9).
   - Section 5.5 now names the 9-10 level among what changes with the gap (p = 0.001 on OTC).
   - Section 5.4 names its one like-for-like difference beyond 2 SE (the negative jump, OTC's fast pairs against Alpha's same-day pairs).
   - The module docstring now quotes 117 section 5.1 exactly.
   - `sim/README.md`'s entry for this test was updated to match.

**Checked and found sound.**

- *Null models.* The no-response Wald test, the flatness tests (their null is the prediction itself, so a rejection refutes it) and the copy-excess baseline are implemented as described. The flatness test keeps its size on planted flat data (an existing test).
- *Leakage.*
  - Response pairs need t2 > t1 strictly, with Alpha's ties set aside.
  - The "prior" covariates and the time-respecting embeddedness use strictly earlier events.
  - Cross-validation re-chooses the thresholds inside each training fold and estimates a held-out row's responder intercept from training rows only.
  - The FE sample is selected on row counts, not on outcomes, and the bootstrap resamples whole responders.
  - The whole-file habits and reputation are person-level controls and hold no outcome of the scored row.
  - The folds are random rows: right for comparing forms, and nothing here is a forecast.
- *Multiple comparisons.* Section 5 is not corrected, but the load-bearing tests survive a Bonferroni correction. The verdict's flatness rejections survive across all 12 flatness tests (largest p = 1e-05), and D-step against T-graded on OTC survives across the 14 paired comparisons (corrected p = 9e-10). On Alpha that comparison survives only narrowly (corrected 0.030), and in a one-repeat CV run it did not. Caveat 6 now says so.
- *Data and terms.* Both files match the recorded sha256, sit in the git-ignored `sim/data/` (checked with `git check-ignore`) and have never been committed. Nothing in this file, the module, the report or the tests holds a rating row or a node id (the tests' ratings are synthetic). Use matches `sim/data/README.md`: local only, computed statistics only, and the two Kumar et al. papers credited.
- *Ledger ids.* Every id cited by the three files exists (L0834, L0853, L0857, L4367, L4567-L4580, L4825; `test_cited_ledger_ids_exist`) and says what the code assumes: the counts (L4568, L4570-L4572), one rating per ordered pair (L4571), the O-jive's form (L0857) in the lag-1 dyad law (L0853), and embeddedness as common neighbours (L4825). Reading a received rating as the "partner's level" of L0857 is the test's own operationalisation, not the ledger's (caveat 7).

**Verdict after review.**

- *Dead zone.* The finding stands at a narrower strength. The response has no dead zone on OTC (every band of two observed ratings rejected) or on Alpha over any band that reaches +2. Alpha's {-1, +1} is untested in practice.
- *Influence.* As a claim about influence, the refutation survives a linear shared-view confound (no excess step) and is undecided against a non-linear one.
- *The literal O-jive* loses out of sample (6.5 SE on OTC, 3.1 SE on Alpha; robust to correction on OTC only).
- *The one-rating band* is a knee, not a zone.
- *The sign gate* is large.
- *Drift.* Only a modest rise of the OTC 1-4 slope is shown; the drift claims for the negative jump and the 9-10 level are withdrawn.
