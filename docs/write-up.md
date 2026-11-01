# social-algebra: write-up

_2026-11-01. The closing account of a three-day strand (2026-10-29 to
2026-11-01). Written for a reader who was not there. Every number below is
taken from a file in this repo that carries its own rule, counts and
caveats; the file is named where the number appears._

## 1. What was attempted

Aldred's aim, in his words assembled on 2026-10-29: an **algebra of
drives**, of persons and of groups, composed into an **equation set** with
theorems, usable to **predict or steer outcomes** at three scales,
membership, group and crowd, including positively, and sensitive to group
size, composition and definition. Existing societies and groups were to
be the working models; the equations were to be tested first on a
modelled population built independently of them, then on data. "Drives as
primitives" was declared a working hypothesis to be tested, not assumed.
Curiosity, fear and desire were examples, not the list.

The first outcome chosen for the equations (Aldred, 2026-11-01) was
**activity**: how much a group does and whether it runs away. Holds and
splits were to be a second layer the model produced.

## 2. What was done

**A validated survey.** 118 files in `docs/prior-work/`, each written by
one agent and checked by a separate one that resolved every DOI at
Crossref, read the source where it could, and appended a validation log.
Fourteen traditions first (network and role algebras, kinship algebras,
acts as operators, logics and institutions, influence and opinion
dynamics, group dynamics, cybernetics and reflexive control, history,
biology and ecology, economics and politics and anthropology and
linguistics, classical statecraft, narrative and games and AI agents,
family systems and persuasion and coercion, mathematical structures),
then targeted dives from a research map of about six hundred directions
(`docs/research-map.md`). The ledger, `docs/ledger.jsonl`, holds 5,817
claims, each tagged by kind, provenance (read, standard account, or
derived), scale and era. A whole-corpus audit resolved 2,125 DOIs; one is
flagged unresolvable. Licensing of everything quoted or transcribed is
recorded per file (`docs/licensing.md`).

The survey's framing finding, from its first day and never overturned:
**drive dynamics exist for single agents, act algebras exist for groups,
and nobody has joined them.** The nearest joins are Gottman's coupled
affect equations for couples, structural balance for triads, consensus
and coupling spectra for teams, and Granovetter's threshold model for
crowds.

**An equation set, v0 to v0.3** (`models/00-v0.md`). Three drives per
person: a set point, a gated affiliation or coupling term, and a goal
term. Update laws adopted per size from the works above, with a sign
registry for the gated laws and a validity record (class, era, medium,
independence, re-test) for every adopted form. Theorems that are ours and
were checked: a no-split certificate, a decoupling limit (corrected after
the simulator exposed its first statement), a monotone cascade bound, a
merge closure, an activity certificate (one attracting steady state when
the spectral radius of the coupling is below one, unbounded growth when
it is not), a reactive-newcomer condition, and a one-sided-gate
identifiability limit. `models/01-composition-and-levers.md` gives exact
laws for splitting, merging and adding a member, with eight steering
levers. `models/02-our-claims.md` gives Claim 1, that a group's drive
state is a threshold distribution, with a merge sandwich and an ignition
condition, and places it against the prior art (Granovetter; Topkis and
Milgrom and Roberts; Macy and Evtushenko; Granovetter and Soong; Oliver,
Marwell and Teixeira).

**A simulator** (`sim/`, Python, uv-managed; 681 tests collected at close, of which 16 are strict expected failures: 13 record refuted claims of v0 itself, two for the dead zone and eleven for the sign registry, and 3 record Leonard's Table 1 transverse condition, which our reduction could not reproduce). It
reproduces the adopted published results before fitting anything, then
fits open data under rules written before any number is computed.

## 3. What was found

Every empirical test was pre-registered: the rule was written into the
results file first, the reporting command refuses to run without it, and
the held-out set was scored once. Independent reviews recomputed the
decisive numbers where the stakes were highest.

### 3.1 The battery (2026-10-31, `sim/results/`)

Four public datasets, four sizes of question. In nothing read in the
survey, and in nothing fitted here, did a drive fix the sign of a tie.
Stable per-person propensities to support or oppose carried most of the
sign variance on Wikipedia adminship votes; the registry's gated sign
law, re-fitted, was a person effect with a residue of a different form.
The crowd gate co-moved with the recent majority on Wikipedia, but
influence could not be told from a shared shock. The first-tie sign law
was refuted on the Bitcoin trust network, where weak balance fit best.
On the Apache Incubator, team size predicted graduation; the mean and
shape of activity did not. Only the set-point term survived every era
and sample.

### 3.2 The fitted case (2026-11-01, `sim/results/apache_fitted_case.md`)

The single test chosen to decide whether the activity layer continued.
Apache Incubator podlings started 2003 to 2012 trained the models, those
started 2013 to 2021 were scored once (91 podlings, 21 retired).

| model | held-out AUC | held-out log-loss |
|---|---|---|
| base rate | 0.500 | 0.540 |
| size only | 0.764 | 0.454 |
| size and first-year growth | 0.778 | 0.451 |
| size, growth and start year | 0.775 | 0.457 |

Growth over size: +0.014 AUC, 95% bootstrap interval from −0.033 to
+0.063. The criterion, a gain above 0.02 with lower log-loss, was not
met. An Opus review recomputed the numbers from the frozen predictions,
found no leakage, and confirmed from the transcript that the rule
preceded the first fit; it lived only in the session transcript until
the close-out of 2026-11-01, when it was copied into the results file
as its Review section. Size predicting graduation is close to a
tautology and supports no mechanism. The interval, not the verdict word,
is the information: the test set's noise is wider than the margin.

### 3.3 The modelled population (2026-11-01, `sim/results/synthetic_population_identifiability.md`)

A synthetic world with three known drives per person, groups of 3, 8 and
25, behaviour generated by a softmax-choice mechanism unlike the
equations (the no-circularity rule of
`notes/2026-10-29-modelled-population-testbed.md`). The question: can
drives be recovered from observables alone, and does a drive model beat
the person-effects rival that won the battery?

Drives were recoverable at every size: correlations with the truth of
0.61 to 0.93 at 60 steps. **But only through the tie channel.** With the
approach and avoid events withheld and only activity observed,
affiliation and aversion fell to between 0.03 and 0.50 and only the set
point survived. That is the battery's pattern exactly: the activity-only
dataset gave size and set point; the signed datasets gave person
propensities.

A ridge composition of the recovered drives did not beat person rates on
held-out group activity or exits at any size (C2 not met at n = 3, 8
and 25). The oracle given the true drives is a mixed picture, not the
flat loss an earlier version of this paragraph claimed (corrected at the
close-out, 2026-11-01, against the file's table): on group activity it
beats person rates at n = 3 and 8 and loses at n = 25; on exits it loses
at n = 3 and wins at n = 8 and 25; applying C2's two conditions to it, it
passes only at n = 8. The file applies C2 to the recovered drives only
and never scores the oracle against it. So the failure is of the
composition rule given recovered drives, and of its linear mean-and-min
form, which the file's own caveat says favours person rates; it is not a
proof that true drives cannot compose. A close-out check (the file's
Review section) found that the generator does carry per-agent memory, a
decaying relationship state and a ten-step exit streak; with both removed,
same seeds and criteria, C2 still fails at n = 8 and 25 and passes only
at n = 3 on three exit events, so the person-rates advantage is not built
from that memory. One deviation is disclosed: the rule's exit condition could
not fire, which was proved before the run and repaired by calibrating the
threshold once on a separate seed.

### 3.4 The measured-drive test (2026-11-01, `sim/results/szekely_composition.md`)

No public dataset was found with a measured drive and more than one group
size (`docs/prior-work/118-measured-drive-datasets.md`). The best was
Szekely, Lipari, Antonioni, Paolucci, Sanchez, Tummolini and
Andrighetto, "Evidence from a long-term experiment that collective risks
change social norms and promote cooperation", Nature Communications 12,
5452 (2021), DOI 10.1038/s41467-021-25734-w, article CC BY 4.0, data on
OSF (wvgk9): 286 people with social value orientation measured before
play, groups of six reshuffled every round, a threshold public-goods game
over 28 rounds. Held-out later rounds within each phase, 345 test
group-rounds.

| model | held-out AUC, phase 1 | phase 2 |
|---|---|---|
| group mean of the measured drive | 0.58 | 0.54 |
| count above a cut (Claim 1's form) | 0.56 | 0.55 |
| each member's past contribution rate | 0.81 | 0.85 |
| rates plus the measured drive | 0.81 | 0.85 |

The measured drive carries a little information in one phase and none in
the other. No composition rule beats the plain mean. Past behaviour
predicts five times better, and the drive adds nothing to it.

## 4. What it means

Read together, the three experiments of the last day and the battery
before them say one thing. **Drives as pre-measured dispositions are
recoverable when the right channel is observed, but they carry little of
a group's outcome. What a person did last time carries most of it.
Composing drives linearly fails even when the true drives are known.**

The data supports a **state** algebra: persons' current behaviour, plus
coupling between them, plus structure (size, thresholds, the spectrum of
the coupling). That is the Gottman and Granovetter form the equation set
already adopted. It does not support a **trait** algebra, which is what
curiosity, fear and desire as primitives would be. The only way to keep
the word "drive" that the evidence allows is to redefine it as a latent
state estimated from behaviour, which is what the winning person-rates
model already is. That dissolves the hypothesis into existing state-space
models rather than extending it.

Nothing here proves the aim impossible. Every real-data test ran on
proxies; the one dataset with a measured drive had one group size and one
drive. The theorems of v0.3 are sound as theorems about coupled linear
systems with thresholds, and the composition laws of `models/01` are
exact. What was not found is any evidence that drives, as distinct from
states, are the primitives from which group outcomes compose.

## 5. What is left, if anyone returns

- **Open decisions** are listed in `models/00-v0.md` section 9: the
  activity instrument per size, the Person sort for non-humans, the
  Object and Setting sorts, symmetrisation of the coupling, the two-sided
  gate settings. (The repository licence, once listed here, was settled
  the same day: MIT for `sim/`, CC BY 4.0 for the text; `docs/licensing.md`.)
- **The conversation-concentration lead** on Apache (concentration of
  development-list talk predicting survival, +0.083 AUC over size on
  already-seen podlings) is the one lead never confirmed on new data;
  podlings started after July 2021 would do it.
- **The size question** for measured drives stays open for want of data.
- **Dyad and crowd pre-registered designs** are written in
  `models/00-v0.md` section 8 and were not run.
- **The reframing**: a state algebra built from person rates and coupling,
  aimed at steering rather than explanation, is a smaller and more
  derivative project than the one set out, and should be chosen knowingly
  if at all.

## 6. Cost and method

About 86 million tokens over three days, roughly 80 million of them in
the survey and its validation, about one million in the three experiments
of the last day. The method that held up: a rule written before any
number, a separate validation pass for every survey file, a ledger with
provenance per claim, a no-circularity rule for the testbed, and
independent recomputation of any number that decided something. The
method that did not: breadth of survey before a single test. The three
decisive experiments cost about one percent of the survey.
