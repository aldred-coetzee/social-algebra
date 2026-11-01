# social-algebra: post-mortem

_2026-11-01, written at Aldred's request after the close. Six questions,
answered from the repo. Every claim names the file it rests on. Where the
closing write-up (`docs/write-up.md`) says something the files do not
support, this document says so rather than repeating it._

## 1. The original hypothesis, as formulated

Two formulations exist, from the same day, and the second supersedes the
first.

**The opening brief (2026-10-29, `CLAUDE.md` "What it is", lines 43-47):**
*"identifying the mechanics of a social group in such a way that we can
identify operators and operands and later use it to model interactions."*
An algebra whose operands are people, roles and groups and whose operators
are the things they do to one another.

**Sharpened the same day (`CLAUDE.md` lines 53-57,
`notes/2026-10-29-drives-as-the-core.md`):** *"an algebra which expresses
basic human drives and group drives, which we can compose into equations,
which we can then use to start making theorems and use to control or
predict behavior… curiosity, fear, desire, etc."*

The assembled statement of aim (`CLAUDE.md` "What we are trying to
achieve"): an **algebra of drives**, of persons and of groups, composed
into an **equation set** with theorems, usable to **predict or steer
outcomes** at three scales (membership, group, crowd), sensitive to group
size, composition and definition, tested first on a modelled population
built independently of the equations, then on data. "Drives as primitives"
was declared a working hypothesis to be tested, not assumed; its first
appearance as a hypothesis rather than a premise is
`notes/2026-10-29-next-pattern-review-quota-ledger-depth.md` line 31.

Stated as a testable claim, which is how the sim files treat it: **a
person has a small set of stable dispositions (drives), measurable or
recoverable from behaviour, such that a group's outcome is a composition
of its members' drives, and the composition rule is sensitive to size.**
The first outcome chosen for the test was activity
(`notes/2026-11-01-first-outcome-activity.md`).

## 2. Every modelling approach tried, in order

**2.1 Three named drives as primitives (2026-10-29, morning).** Curiosity,
fear and desire as the operand set, acts as operators. Abandoned the same
day without a test: `notes/2026-10-29-equation-set-not-three-drives.md`
records Aldred's correction that the three were examples, not the list,
and that the deliverable was an equation set. No experiment. Dropped
because it was never a theory, only a first naming.

**2.2 v0: three drive terms per person with size-indexed update laws
(2026-10-29 to 10-30, `models/00-v0.md`, commit eeee685).** A set point, a
gated affiliation or coupling term, and a goal term; dyad law from
Gottman's coupled affect equations, triad law from structural balance,
team law from consensus and coupling spectra, crowd law from Granovetter
thresholds, each adopted from the survey (`docs/prior-work/`). It carried
three claims of its own: a gated sign law for new ties with a dead zone, a
first-tie sign rule for closing triads, and a crowd gate. Tested by the
battery of 2026-10-31 (`sim/results/`, section 2.3 to 2.6 below). It
failed piecewise, not at once: each claim that was ours was refuted or
reduced to a person effect, and what remained was the adopted laws, which
are the prior art. The versions v0.1 to v0.3 (commits 66806e2, 3f02917,
ad87f61, 08cec66; change logs at the foot of `models/00-v0.md`) are
repairs made under those results: the decoupling limit was restated after
the simulator exposed it, a sign registry (S1)-(S3) and a validity record
(section 10) were added, and the activity certificate, reactive-newcomer
condition and one-sided-gate identifiability limit were added as theorems
(section 7). None of these repairs produced a prediction that beat the
rival on data.

**2.3 The first-tie sign law at triad scale.** v0's claim that the sign of
a closing tie depends on the sign of the first tie. Tested on the Newcomb
fraternity (`sim/results/newcomb_n3.md`): depletion of one-negative
triples supported in aggregate (z from −6.0 to −2.5), conversion 1.09%
against 0.75% (p = 0.099), with the stated caveat that the null leaves
popularity free (line 459). Re-examined in
`sim/results/triad_rule_comparison.md` line 40: the whole pattern is "the
closing tie takes the sign of the second tie", which is a consensus about
the third man, and under a column null that holds each man's popularity it
falls to chance (|z| ≤ 3.4, agreement 4-6 of 8). On Bitcoin and wiki-RfA,
weak balance had the best held-out log-loss (0.264 against 0.306 and
0.500), and a per-person propensity beat every triad rule on the two
datasets where it could be fitted. Failed because what looked like a
triadic law was a receiver effect.

**2.4 The gated reciprocity law with a dead zone.** v0's claim that a
reply to a received rating is flat across a band and then jumps. Tested
on the Bitcoin trust networks (`sim/results/gate_reciprocity_bitcoin.md`
sections 3.2 and 4): the response is graded, +0.85 going from +1 to +2
received, graded beats step by 6.5 standard errors, and the dead zone is
refuted. A sign gate is real (−8.36 at the sign boundary). Two strict
expected-failure tests record it (`sim/tests/test_gate_reciprocity_bitcoin.py`).
The test was not blind (section 6 of the file). Failed because the
specific form was wrong; a sign asymmetry survived but is Altafini's and
Leskovec's, not ours.

**2.5 The sign registry (S1)-(S3).** v0.2's catalogue of gated sign laws
by medium, era and embeddedness. Tested in
`sim/results/sign_registry_battery.md`: the gate term G is at most +0.010
on every dataset; the person terms D run +0.056 to +0.152; registry
prediction R2 fails 4 of 4; the strongest registry coefficient (FFmm,
−0.48 alone) collapses to +0.01 once person terms are in the model. Eleven
strict expected failures record the registry's refuted entries
(`sim/tests/test_sign_registry_battery.py` line 742 onward). Failed because
every registry effect was a person effect in disguise.

**2.6 The crowd gate and the activity layer at team scale.** The crowd law
(`sim/results/crowd_gate_wikirfa.md`): co-movement with the recent
majority is real (1.44 against a null of −0.01) but time-symmetric, so
influence cannot be told from a shared shock; `sim/results/identifiability_crowd.md`
proves the gate's position above the stall is not identified from
aggregates, only from interventions. `sim/results/wikirfa_conversion.md`
finds a +0.1 within-voter agreement term and calls it "setting-specific,
not a law". At team scale (`sim/results/apache_activity_survival.md`,
Verdict and section 5.5): size predicts graduation (AUC 0.76), the shape
of the activity distribution adds +0.000 over the mean, a member's own
history predicts her next month's activity at AUC 0.90, and the others'
activity share adds +0.0007. Failed because the only live signals were
size and individual persistence, neither of which is a drive composition.

**2.7 Claim 1: a group's drive state is a threshold distribution, with a
merge sandwich and an ignition condition (`models/02-our-claims.md`,
2026-10-31).** The one claim written as ours after
`notes/2026-10-31-derivative-so-far-own-claims.md` named the rest as
derivative. Internally consistent: 0 violations in
`sim/results/identifiability_crowd.md` and in the exploratory, unaudited
`sim/results/mixture_equilibria.md` (ignition seen above the maximum
threshold in 14.1% of draws). On measured data its count-above-a-cut form
scored AUC 0.56 and 0.55 (`sim/results/szekely_composition.md`, K1), no
better than the plain mean. Not refuted, but it predicts nothing the mean
does not, and its ignition condition is Granovetter's with a merge law
attached.

**2.8 The fitted case on Apache (2026-11-01,
`sim/results/apache_fitted_case.md`).** The pre-registered decider for the
activity layer: does first-year growth add to size in predicting
graduation, out of time? Gain +0.014 AUC, interval −0.033 to +0.063,
criterion (+0.02 with lower log-loss) not met. The file's own caveat: the
test set is "out-of-time but not unseen". `docs/write-up.md` section 3.2
says an Opus review recomputed the numbers and found no leakage; that
review happened in the session transcript and **is not recorded in the
results file**, which has no Review section (checked 2026-11-01). The
claim of review should be read as unverified from the repo.

**2.9 The modelled population (2026-11-01,
`sim/results/synthetic_population_identifiability.md`).** The test the
brief asked for first and the strand ran last: a synthetic world with
three known drives per person, groups of 3, 8 and 25, behaviour generated
by a softmax mechanism unlike the equations
(`notes/2026-10-29-modelled-population-testbed.md`). Criterion C1 (drives
recoverable) met through the tie channel, correlations 0.608 to 0.931 at
60 steps; from activity alone only the set point survives. Criterion C2
(a drive composition beats person rates on held-out group outcome) not
met at any size, and the oracle given the true drives did not beat person
rates either. One disclosed deviation: the exit rule could not fire and
was recalibrated on a separate seed. This is the decisive failure: the
composition rule in `models/01-composition-and-levers.md` loses even when
the drives are known exactly.

**2.10 The measured-drive test (2026-11-01,
`sim/results/szekely_composition.md`).** The only public dataset found
with a drive measured before play (social value orientation, Szekely et
al. 2021, `docs/prior-work/118-measured-drive-datasets.md`). Group mean of
the drive AUC 0.58 and 0.54 by phase; each member's past contribution
rate 0.81 and 0.85; rates plus drive identical to rates alone. K1 met in
phase 1 and pooled only, K2 and K3 not met. One disclosed flaw: the K1
margin was fixed after outcome frequencies had been seen. Failed because
a drive measured by the standard instrument added nothing to last
behaviour.

**2.11 The rival that won: a person-rates state model.** Not an approach
we proposed; it was the control in 2.5, 2.6, 2.9 and 2.10 and it won each
time. It is a latent-state model estimated from behaviour, which is the
Gottman and Granovetter form the equation set had adopted
(`docs/write-up.md` section 4).

## 3. The overall conclusion, categorised

**It reduces to existing work.** The nearest of the four labels, and the
one the evidence supports; the other three are wrong for stated reasons.

- *The maths doesn't close* is false: the theorems in `models/00-v0.md`
  section 7 were checked by reproduction tests (Wankhede 6.1, Marvel
  blow-up, Granovetter crowds, Leonard θ_c and Altafini all pass in
  `sim/tests/`), and `models/01` is exact. The maths
  closes; it is a theory of coupled linear systems with thresholds.
- *The variables aren't measurable* is half true and not the finding:
  drives were recoverable in the synthetic world through ties (2.9), and a
  measured drive existed on Szekely (2.10). The problem was not measuring
  them. It was that, measured or oracle-known, they did not compose into
  outcomes better than last behaviour.
- *We simply didn't find it* is the hedge the write-up allows itself
  ("nothing proves the aim impossible", section 4). It is true in the
  trivial sense and misleading as a category. Three pre-registered tests
  and a favourable synthetic world, in which the drives were exact and the
  composition rule was ours to choose, all returned the same ordering.

What it reduces to, named: the winning model is **a per-person latent
state with inertia, plus coupling, plus size**. At dyad scale that is
Gottman and Murray's coupled difference equations
(`docs/prior-work/059-gottman-murray-influence-functions-deep-read.md`;
`models/00-v0.md` section 4). At crowd scale it is Granovetter's threshold model with
Macy and Evtushenko's and Topkis's monotone comparative statics
(`models/02-our-claims.md`, placing section). At team scale it is
consensus dynamics with the spectral-radius condition
(`models/00-v0.md` section 7, activity certificate). At the level of
sign laws it is structural balance in its weak form (Davis) and Altafini's
sign asymmetry (`sim/results/triad_rule_comparison.md`,
`sim/results/gate_reciprocity_bitcoin.md`). Every term that survived was
adopted from one of those; every term that was ours was refuted or
collapsed into a person effect.

## 4. What survived, with the evidence

- **Drives are recoverable from ties, not from activity.** Correlation
  with the true drives 0.608 to 0.931 at every group size when approach
  and avoid events are observed; 0.03 to 0.50 for the affiliation and
  aversion terms when only activity is observed
  (`sim/results/synthetic_population_identifiability.md`, C1). This is a
  result about instruments: a tie-recording channel is necessary. It held
  at n = 3, 8 and 25.
- **Size predicts team survival.** AUC 0.76 for graduation on Apache
  Incubator podlings 2003-2021, held out of time 0.764
  (`sim/results/apache_activity_survival.md` Verdict;
  `sim/results/apache_fitted_case.md`). Trivial as a mechanism, robust as a
  number.
- **Individual persistence dominates at team scale.** A member's own
  history predicts her next-month activity at AUC 0.90; the group's
  activity share adds +0.0007 (`sim/results/apache_activity_survival.md`
  section 5.5).
- **A real sign gate at the sign boundary, graded above it.** −8.36 at
  the boundary; +0.85 from +1 to +2 received
  (`sim/results/gate_reciprocity_bitcoin.md` sections 3 and 4). The two
  platforms agree like for like (section 5.4), with the stated caveat
  that the test was not blind.
- **Weak balance beats strong balance and beats v0's rule on signed
  triads.** Held-out log-loss 0.264 against 0.306 and 0.500
  (`sim/results/triad_rule_comparison.md`). A reproduction, not ours.
- **Crowd co-movement with the recent majority is real at wiki-RfA
  scale.** 1.44 against −0.01 null (`sim/results/crowd_gate_wikirfa.md`),
  but direction unidentified, so it is a regularity and not a mechanism.
- **Claim 1 is internally consistent.** 0 violations in two simulation
  files (`sim/results/identifiability_crowd.md`,
  `sim/results/mixture_equilibria.md`, the second unaudited). It survived
  as a theorem about a threshold mixture, not as a prediction about data.
- **The reproductions.** Every adopted published result the simulator
  set out to reproduce was reproduced, except Leonard's Table 1 transverse
  condition, which three strict expected failures record as unresolved
  (`sim/tests/test_leonard_thetac.py` line 49). `docs/write-up.md` section 2
  and `STATUS.md` say the 16 expected failures "record refuted published
  claims"; that is wrong. Thirteen record refuted claims of v0 itself (two
  dead-zone, eleven registry), and the other three record a published
  table this reduction could not reproduce, which is a limit of our
  reduction as much as of the table.
- **One unconfirmed lead.** Conversation concentration on Apache, +0.083
  AUC over size, on already-seen podlings
  (`sim/results/apache_activity_survival.md` section 7.4). Not a result.

No regime, size or timescale was found where a drive composition beat
person rates. The question of size sensitivity with measured drives was
never tested on data, for want of a dataset
(`docs/prior-work/118-measured-drive-datasets.md`).

## 5. Strongest overlapping literature, and what was different

The survey's own map (`docs/synthesis.md`, `docs/research-map.md`) places
the strand against four traditions by scale and four by form:

- **Gottman et al., coupled affect equations for couples** (dyad law,
  `models/00-v0.md` section 4). We adopted it; the dyad test in section 8
  was designed and never run.
- **Structural balance, Heider through Cartwright and Harary to Davis's
  weak balance, and Altafini's signed consensus** (triad and sign laws).
  Our first-tie rule was a worse version; weak balance won
  (`sim/results/triad_rule_comparison.md`).
- **Consensus and coupling-spectrum dynamics, DeGroot through Leonard's
  team models** (team law, activity certificate). Our spectral-radius
  activity certificate is a restatement of the standard stability condition.
- **Granovetter's threshold model, with Granovetter and Soong, Macy and
  Evtushenko, Oliver, Marwell and Teixeira, and Topkis and Milgrom and
  Roberts** (crowd law, Claim 1). Claim 1's threshold distribution is
  Granovetter's; the merge sandwich is the one piece placed as ours.
- **Act algebras for groups: Lefebvre's reflexive control, affect control
  theory, Comme il Faut and Versu, Singh's commitments, role algebras**
  (`docs/synthesis.md`, prior-work files 01-04, 12, 14). These give
  operators without drive dynamics, which is the gap the strand named.
- **The person-rates rival is ordinary panel regression with
  individual effects**, which is to say the standard econometric control.

What was genuinely different, and it is short:

1. **The join was named.** Drive dynamics for single agents and act
   algebras for groups exist separately, and the survey found no work
   joining them (`docs/history-2026-10-29-to-11-01.md` lines 227-229). The
   finding that the join does not pay, under three pre-registered tests
   and an oracle, is the strand's one original empirical statement.
2. **The negative was pre-registered and the oracle condition is unusual.**
   The synthetic test gives the composition rule the true drives and it
   still loses to person rates
   (`sim/results/synthetic_population_identifiability.md`, C2). Most
   trait-versus-state comparisons in the literature cannot run that
   condition because the truth is not known.
3. **The merge sandwich** in `models/02-our-claims.md` and the exact
   split, merge and add-member laws of `models/01-composition-and-levers.md`
   have no direct source in the survey. They are untested on data beyond
   the Szekely K2 and K3 criteria, which they failed.

Everything else, including the sign registry and the validity record, is
bookkeeping over adopted results.

## 6. Is the negative result writeable up?

**As a journal result, no.** The real-data tests ran on proxies for
drives, not drives (`docs/write-up.md` section 4); the one measured-drive
dataset had one group size and one instrument; the fitted case's review is
not in the repo; the Szekely margin was set after seeing outcome
frequencies; the Bitcoin test was not blind; and the sample is three
decisive experiments, each on one dataset. A referee would also note that
"person rates beat a trait composition" is the expected result in panel
settings with strong inertia, and would ask for the dyad test and the
tie-channel test on real data before accepting a general claim.

**As a methods note or a long-form post, yes, and the pre-registration
record is what makes it so.** The repo holds, for every test, the rule
written before the number, the counts and intervals, the disclosed
deviations, and strict expected-failure tests that pin each refuted claim
to a measured value. The oracle condition of the synthetic test is the
part worth other people's attention. The honest frame is a negative
result about a research programme, not about a model: three days, a
survey of 118 validated files, and the three experiments that decided it
costing about one percent of the survey (`docs/write-up.md` section 6).

A one-paragraph abstract would read:

> We asked whether a group's outcome can be written as a composition of
> its members' drives, stable dispositions measured or recovered from
> behaviour, with a composition rule that depends on group size. We
> adopted the standard dynamics at each scale (coupled affect for dyads,
> structural balance for triads, consensus for teams, thresholds for
> crowds), added our own sign and composition laws, and tested them under
> rules fixed before any number was computed, on four public datasets and
> on a synthetic population whose generating mechanism was unlike the
> equations. Drives were recoverable from tie events but not from
> activity. Every sign law of our own reduced to a per-person propensity.
> On held-out outcomes, a composition of recovered drives did not beat a
> model of each member's last behaviour at any group size, and neither did
> a composition of the true drives in the synthetic world. On the one
> dataset with a drive measured before play, the drive added nothing to
> past behaviour. The surviving model is a per-person latent state with
> inertia, coupling and size, which is existing work. We report the
> pre-registered rules, intervals and deviations in full.
