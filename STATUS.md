# Status

_Updated 2026-11-01._

Scaffolded 2026-10-29: brief, `notes/`, `models/`, `docs/`. On GitHub
(private) at `aldred-coetzee/social-algebra`. Model pinned to Fable 5.1 for
this project (see `CLAUDE.md`).

## Where we are (2026-11-01): the fitted case did not meet its criterion

The single pre-registered test that was to decide whether the team-scale
activity layer continues has run: `sim/results/apache_fitted_case.md`,
code `sim/models/apache_fitted_case.py`, tests
`sim/tests/test_apache_fitted_case.py`. Rule written into the file before
any number was computed (`report` refuses to run without it). Apache
Incubator podlings started 2003–12 train, 2013–21 test, scored once.

| model | held-out AUC | held-out log-loss |
|---|---|---|
| base rate | 0.500 | 0.540 |
| A size only | 0.764 | 0.454 |
| B size + first-year growth | 0.778 | 0.451 |
| C size + growth + start year | 0.775 | 0.457 |

B − A in AUC is +0.014, 95% bootstrap [−0.033, +0.063]; log-loss −0.002.
The criterion (B beats A by more than 0.02 AUC **and** lower log-loss) is
**not met**: only the log-loss half holds. A separate Opus review recomputed
the numbers from the frozen predictions (B − A is exactly 21/1470), found
no leakage (standardisation and ridge fit on training rows only; the
landmark table pools nothing across podlings), and confirmed from the
transcript that the rule was written four seconds before the first fit.
Its one wording finding: `models/00-v0.md` §8 "Team" says "does not beat
size alone" with no margin; the applied criterion is the 2026-11-01
brief's, with the 0.02 margin, and §8 now says so.

What the result means, and does not: first-year growth adds nothing that
this test can see beyond size, on a test set of 91 podlings (21 retired)
whose noise is wider than the margin. Size predicting graduation is close to
a tautology and supports no mechanism. The secondary conversation-lead
result (AUC +0.083 [+0.018, +0.152] over size) is the lead from the
in-sample file re-scored on podlings that file had already seen, found in a
42-variant search; it is a lead, not a confirmation. Nothing here touches
the certificate theorems (7.5–7.7), which the dataset cannot reach.

**Per the plan Aldred approved with "Go": if the criterion failed, stop and
write up.** The decision is his. Options as this session sees them:
(1) stop here and write up, the repo as it stands being the write-up;
(2) one more test on a different dataset or size (the dyad or crowd tests
of v0.3 §8), at similar cost (about 2M tokens each); (3) chase the
conversation lead on podlings started after July 2021, which is the only
new-data confirmation available at this scale. Token spend to date is
about 85M. No new research batches are planned.

Housekeeping the same day: auto-compaction at 200k tokens set in this
project's settings and globally (`CLAUDE.md`, "Context size").

## Prior-work survey (in progress)

Aldred, 2026-10-29: this is not novel — research what exists, store it,
validate it. Then twice: look further afield, other disciplines, history.
Result: fourteen surveys in `docs/prior-work/`, one per tradition. Each was
written by one agent from web sources and then given a **second pass** by a
separate agent that checks every citation and formal claim, corrects the file
in place and appends a `## Validation log`.

| File | Tradition | Second pass |
|---|---|---|
| 01 | network and role algebras | done |
| 02 | kinship algebras | done |
| 03 | acts as operators (Fiske, ACT, Lefebvre, balance, exchange) | done |
| 04 | logics, institutions, calculi | done |
| 05 | influence, opinion, control | done |
| 06 | group-dynamics frameworks | done |
| 07 | applied control (cybernetics, reflexive control, prediction limits) | done |
| 08 | history | done |
| 09 | biology and ecology | done |
| 10 | economics, politics, anthropology, linguistics | done |
| 11 | classical theory and statecraft | done |
| 12 | narrative, games, AI agents | done |
| 13 | family systems, persuasion, coercion | done |
| 14 | maths and CS structures | done |

All fourteen have had the second pass (completed 2026-10-29). Residual doubts are in each file's Unconfirmed section; treat anything there as unchecked.

**Survey is closed at fourteen** (next-pattern's direction, 2026-10-29): no
new tradition files unless the synthesis exposes a hole that matters for
operators and operands specifically.

**Also 2026-10-29, after next-pattern's independent check** (all 292 DOIs
resolved; no invented reference): fixes applied; every structural claim
tagged `[read]` or `[from abstract/standard account]` (almost all the
latter, so formal descriptions are textbook forms, not read at source);
duplicated works reduced to one primary entry with cross-references; three
short entries added and **not** second-passed: role theory (06), White's
*Identity and Control* (01), relation algebra and Allen (14).

## Synthesis (done 2026-10-29)

`docs/synthesis.md`: comparison table across the traditions, the four
closest precedents and what each lacks, requirements R1-R11, six candidate
formal homes with fit and cost, and ten open questions. No recommendation.

**Gating questions answered 2026-10-29** (all three defaults taken; see
`notes/2026-10-29-gating-decisions.md`): persons, roles, groups only;
discrete relational state first; discrete nondeterministic turns with
reachability claims.

**Redirected 2026-10-29** (`notes/2026-10-29-drives-as-the-core.md`): the
algebra is to express basic human and group **drives** (curiosity, fear,
desire, …) that compose into equations, for theorems and prediction or
control. This reopens Q4 (drives are graded internal state). The
`models/00` draft was stopped.

**In progress:** drive survey. `docs/prior-work/15`–`19` (taxonomies, formal
models of motivation, curiosity/fear/desire, group drives and collective
emotion, computational drive agents) are written and being second-passed.
Aldred, same day: *"Dig deeper on drives between people and groups and go
wider too… I expect this research phase to be very deep."* So `20`–`27`
were started: dyadic coupling dynamics (Gottman, Strogatz, coregulation),
social preferences and psychological games, neuroscience of social drives,
collective dynamics of driven agents (mean-field games, panic, fear–epidemic
coupling), collective action and team motivation, culture-scale drives and
norm evolution, philosophy of the passions (Spinoza's geometric derivation
of the affects, Hobbes, Hume, rasa, Abhidharma), and measuring drive
dynamics. Then, on *"look at things like predator prey models and what
has been done with animal groups; I assume a lot of that is base
applicable"*: `28` predator–prey and the ecology of fear (with transfers to
human systems), `29` animal collective behaviour in depth, `30` ecological
stability and resilience theorems (May, keystones, regime shifts), `31`
ethology of signals as operators on another animal's drives. Each gets the
same second pass, then one drive synthesis.

Aldred again: *"Still not deep enough, this subject is vast."* Round three,
started 2026-10-29: `32` the language of drives (semantic primes, emotion
lexicons across 2,474 languages, force dynamics), `33` developmental and
attachment control models (Bowlby, Bischof's Zurich model, still-face),
`34` personality as drive parameters and RDoC, `35` behaviour change and
persuasion (fear appeals, BCT taxonomy of 93 techniques), `36` axiomatic
economics of desire (temptation theorems, addiction, lexicographic needs),
`37` ritual, sacred values and awe, `38` organisational motivation (equity,
crowding out, tournaments), `39` deterrence, coercion and strategic fear.
**Queued, not yet started** (concurrency limit): `40` compositional
dynamical systems maths (categorical systems theory, open games,
port-Hamiltonian interconnection, passivity and small-gain theorems,
max-plus selection) — the maths that would make drive equations compose.

Aldred, later the same day: curiosity, fear and desire were examples only;
*"the idea is we formulate a new or updated equation set"*
(`notes/2026-10-29-equation-set-not-three-drives.md`). Added `41`
self-conscious, moral and relational drives and `42` dynamics drive by
drive. The drive synthesis must end in a candidate equation set with every
term traced to a validated source or marked as ours.

**Standing instruction (Aldred, 2026-10-29): "go deeper, don't wait for me
between batches"** — **replaced the same day by Aldred's rule: "Pause after
each batch and ask me if we should do the next"** (`notes/2026-10-29-cap-and-target-outcomes.md`, which also records his target outcomes: three scales, applied practice, group size and composition, positive steering); see `notes/2026-10-29-next-pattern-review-quota-ledger-depth.md`.
**Iteration 1 landed 2026-10-29 evening** (files 043–082, 120 agents,
12.5M tokens; report in `docs/batches/`). **Then Aldred: targeted, not
broad** — v0 equation set tested at three group sizes (3, 8–12, 100+) on one
common outcome (holds together or splits, who leaves). **Batch 2 landed 2026-10-30** (files 083–094; 36 agents, 5.2M tokens;
report and v0 proposal in `docs/batches/2026-10-30-…`). Ledger: 4,299 lines
(seeded from 043–082 and the equation-set surveys, hygiene pass applied,
batch 2 added; rules in `docs/ledger.md`). **Licensing check done 2026-10-30** (Aldred asked before v0): rule in
`CLAUDE.md`, audit and fixes in `docs/licensing.md`; repo licence is his
choice before open-sourcing (CC BY 4.0 text, MIT or Apache-2.0 code).
**Aldred, 2026-10-30: "write v0 and run the nine reads."** **`models/00-v0.md` written 2026-10-30** (320 lines; 84 ledger ids,
58 admissible now, 24 marked ⚠ pending the reads; three drives: set
point, gated affiliation, goal attraction; four candidate theorems, three
refutation tests; merge/split of drive state declared absent). Spot-checked
by this session: the D1 derivation, the θ_c = 2·arccos r identity and its
three numeric checks, and the monotone-cascade theorem all hold. **Batch 3 landed and v0.1 written, 2026-10-30** (files 095–103; 11 of
the nine sources' texts read in full, Harary 1953 not obtained, Mathieu and
Walker & Hill abstract-level). v0.1: 144 ledger ids, 110 admissible, 21 ⚠,
4 dropped; next-pattern's independent audit of v0 applied (citation
hygiene, misquoted 050 basis, two theorems tightened). Changes that
matter: the crowd gate is two-sided (Cantoni's substitutes refute a
universal monotone threshold map); Altafini's dichotomy carries its exact
hypotheses; dyad partner coupling is bounded tiny beside inertia, so
"decoupling" is the rule at dyad scale; 6.1 proved in Euler turns; 6.4
conjecture became a theorem. **Aldred, 2026-10-31: "Go"** on next-pattern's order: (1) `sim/` as
regression tests that reproduce the published results of the five
source-verified equations (Wankhede certificate, Marvel factions,
Granovetter's two crowds, Leonard's θ_c cases), each test citing its ledger
id, Python in a uv environment; (2) then the n = 3 refutation test on the
Newcomb data once D594's lines are read; (3) no new research batch until
both exist. Naming the instruments remains his open decision.
**Done 2026-10-31:** `sim/` regression suite (156 passed, 3 xfail; 6.2
corrected; one Leonard Table 1 claim open) and the Newcomb/Doreian &
Krackhardt read at source (file 104, validated): both papers read, data
are ranks with a stated sign recode, exact sign-shuffle null exists, two
of three one-negative types under-represented and one over-represented
from week 6, no conversion table printed, 15 waves settled, UCI copy
CC BY-NC-ND (results publishable, data file not redistributable). **Aldred, 2026-10-31: "Go on all"** (the five steps, in order, no stop
for a yes; plus fluidity — `notes/2026-10-31-go-on-all-and-fluidity.md`).
Running: the n = 3 Newcomb test in `sim/` (local data only, CC BY-NC-ND);
batch 4 = clusters W (where tie signs come from — the hinge for the drives
hypothesis, D597–D604) and X (drift and datedness, D605–D608), files
105–116. Written by the session: `models/01-composition-and-levers.md` —
split inherits the no-escalation certificate (proved), merge needs a
loop-gain condition (row-sum and block forms, proved), a size law for
mergers, eight steering levers read off the certified laws, and the
validity-column rule. To fold into v0.2 after batch 4.
**Aldred, later 2026-10-31: "this all seems completely derivative… integrate
the current and become less derivative."** Agreed and recorded
(`notes/2026-10-31-derivative-so-far-own-claims.md`): the next model file is
`models/02-our-claims.md`, ours only, each claim with a test on current
data; cluster Y on the map (D609–D614). **Done 2026-11-01:** `models/02-our-claims.md` Claim 1 — group drive
state as a threshold distribution; merge sandwich (never below both
parts, never above the least common pre-fixed point), ignition with latent
pressure, non-reducibility (no summary of the parts gives the merged
equilibrium); proofs ours, numerics exact on 829,756 pairs; audit requested
from next-pattern. The n = 3 Newcomb test ran (`sim/results/newcomb_n3.md`):
symmetric triangle rule refuted for directed ties, strict balance refuted,
weak balance a depletion, conversion undecided; v0.1 §7 updated. File 117
(modern signed and split datasets) written, in validation. **Batch 4 landed 2026-11-01** (files 105–116; 36 agents, 17.2M tokens — deep
reads are the expensive kind; ledger now 5,817 lines, with era and medium).
**The hinge finding (112, 116):** in nothing read do drives fix the sign of a
tie; the same drive state gives opposite signs across settings; person-level
sender/receiver propensities carry most predictable sign variance, with no
mechanism; only the set-point term survives a change of era and sample; for
"holds/splits" the load-bearing content is structure, payoffs and
composition. 112 proposes a registry of gated sign laws with the sign as a
state; 116 proposes the validity column (fields, rules, statuses). v0.1's
empirical base: of 46 lines, 14 rest on pre-2000 data, 4 on post-2015 (all
one Hong Kong march), one newlywed cohort carries 22%.
**v0.2 written 2026-11-01** (`models/00-v0.md`, 421 lines; 411 ledger ids,
300 admissible, 53 ⚠): §0.5 states the hinge; §4.2 the directed first-tie
law with weak balance as a depletion and strict balance only as the
structure theorem; §4.5 the sign registry with the sign as a state; §0.6
and §9.2 the validity record on every term; models/01 and Claim 1 folded;
§5.5 medium and non-human members. Audit requested from next-pattern. **Done 2026-11-01:** the wiki-RfA tie-conversion test
(`sim/results/wikirfa_conversion.md`): 1,201 conversions; repair toward
weak balance 56.7% vs 50.0% null, mostly direction mix; a weak,
setting-specific agreement term, not a law; first-tie asymmetry only when
the negative tie touches the voter. v0.2.1 committed after next-pattern's
audit (scope words restored in the hinge; two-factor directed law).
**Battery landed 2026-11-01** (`sim/results/*.md`, each with its review; suite
615 passed): signs are person propensities plus a small residue — triad
terms add ≤ +0.01 AUC, so the registry has no mechanism beyond person
terms; the crowd gate co-moves with the recent majority on Wikipedia
elections (z 16, 2005–13), substitutes refuted as a net association,
one-sided lower gate, no ignition; the first-tie law (4.2d) refuted on
Bitcoin, weak balance the best single rule; Apache: size predicts
graduation, mean activity and distribution shape do not, growth vs
collapse does; Bitcoin: dead-zone gate refuted, graded response with a
strong sign gate; crowd law identifiable from aggregates only up to the
stall. **Aldred, 2026-11-01: activity first** (`notes/2026-11-01-first-outcome-activity.md`);
holds/splits becomes the produced second layer. next-pattern audited the
battery: numbers stand; four headlines had dropped the files' own
qualifiers (the sign residue is the size of a substantial per-triad
mechanism, not "small"; the Wikipedia gate result is co-movement, not
influence; the Bitcoin dead-zone verdict is about a band on the single
received rating, so (S3)'s dead zone is untested, not refuted; the
identifiability fix needs the right parametric family). **v0.3 written 2026-11-01** (339 lines): activity first with its
instrument per size; holds/splits a produced Layer B; two new theorems
checked by this session — 7.5 activity certificate (ρ(R+Γ) < 1 gives one
globally attracting steady state with coupling only raising activity;
ρ ≥ 1 with irreducible M gives unbounded growth, no bistability) and 7.6
the reactive-newcomer iff; demotions from the battery applied. Not yet
audited (token cost; Aldred's call). **Proposed next and only step: one
fitted case** — Apache Incubator, train on podlings started 2003–12, predict
2013–21 before looking, size + first-year growth vs size alone; about 2M
tokens; result decides whether the project continues. **Decision for Aldred after v0.2:** keep "holds/splits"
as the first outcome, or switch to one where drives are the obvious
variables (conformity/compliance at membership scale; effort/efficiency at
group scale). Slip
the same day: an agent sent Aldred's email to Unpaywall's API; rule added
to CLAUDE.md. Then: v0 provenance update, and the
question of what comes next goes back to him. Research iterations run back to back as workflow
batches from `docs/research-map.md`: dive → separate validation pass →
cross-check against existing files → commit → next batch. No synthesis and
no modelling until Aldred says the research is deep enough
(`notes/2026-10-29-research-before-models-uv.md`). The modelled-population
testbed idea is in `notes/2026-10-29-modelled-population-testbed.md`.

**Depth, not only breadth:** almost every survey so far read abstracts, not
papers. After the drive synthesis names the keystone works (about twenty),
the plan is a deep-read round: one agent per keystone, primary text in full,
equations transcribed and checked. The
first survey's finding that frames this: drive dynamics exist for single
agents, act algebras exist for groups, nobody has joined them.

No algebra of our own yet, deliberately.
