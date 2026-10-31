# Status

_Updated 2026-10-29._

Scaffolded 2026-10-29: brief, `notes/`, `models/`, `docs/`. On GitHub
(private) at `aldred-coetzee/social-algebra`. Model pinned to Fable 5.1 for
this project (see `CLAUDE.md`).

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
data; cluster Y on the map (D609–D614). Started: D609 (group state as a
distribution; merged-crowd equilibrium numerics) and D610 (modern
explicit-sign and split datasets with licences). Slip
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
