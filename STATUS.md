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
between batches."** Research iterations run back to back as workflow
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
