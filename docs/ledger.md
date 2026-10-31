# Claim ledger

_Started 2026-10-29 on next-pattern's direction, so that "deep enough" is measurable._

`docs/ledger.jsonl` holds one line per claim the equation set might rest
on. Every dive adds lines; the cross-check marks duplicates; the batch
report gives the yield per cluster.

## Line schema

```json
{"id":"L0001","kind":"equation","statement":"one line","source":"16 §4","work":"Keramati & Gutkin 2014, doi 10.7554/eLife.04811","provenance":"read","status":"open","cluster":"C","added":"2026-10-29","batch":1,"dup_of":null,"scale":"group","ethics":"n/a","note":""}
```

- `kind`: `drive` | `equation` | `empirical-result` | `contradiction` | `definition`.
  `equation` only when the line states a formula; a prose result is an
  `empirical-result` or a `definition`. A `contradiction` is a conflict
  between two SOURCES, with both named; a file's caveat about its own
  reading is a `note`, not a contradiction. Each line pins ONE claim to ONE
  work; a sentence that groups two sources becomes two lines.
- `provenance`: `read` (the agent fetched and read the primary text **in
  full**; a preprint standing in for a chapter must say so in `note`),
  `sa` (abstract or standard account), or `derived` (our own derivation,
  with the derivation's file§ in `source`; may feed v0 only with the
  derivation shown and checked). A validator may upgrade `sa` to
  `read` only by opening the source itself. **Nothing `sa` feeds an
  equation.** If a text is paywalled the line says so and stays `sa`.
- `status`: `open` | `adopted` | `rejected` | `duplicate`
- `contradiction` lines carry both sources in `note` and stay `open` until
  a deep-read settles them.
- `empirical-result` lines record what a tradition actually predicts or
  controls, and how well, out of sample: the scoring material for the
  equation set. They carry `scale`: `membership` (join, stay, leave,
  conform) | `group` (cohesion, decision, split, efficiency) | `crowd`
  (adoption, mobilisation, opinion at society scale) — Aldred's three
  target scales (`notes/2026-10-29-cap-and-target-outcomes.md`).
- `era`: the years the data were collected (e.g. `1956`, `1989-1992`,
  `2019`), or `theory` for a result with no data; `medium`: `face-to-face`
  | `online` | `mixed` | `animal` | `n/a`. Added 2026-10-31 for fluidity
  (`notes/2026-10-31-go-on-all-and-fluidity.md`): magnitudes are era- and
  medium-bound and must be re-estimated; forms are not.
- `ethics`: `consent` | `manipulation` | `n/a` — whether the intervention
  or finding steers people with or without their consent. Positive
  steering (improving efficiency, wellbeing, decision quality) is in scope.

## Convergence rule (replaced 2026-10-29, next-pattern)

The first rule (a cluster closes when a batch adds fewer than one new claim
per five directions) cannot bite at extraction grain: iteration 1 yielded
14–43 new lines per direction in every cluster. The unit is now the draft
equation set itself. **Once v0 exists, the ledger claims it rests on are the
unit, and the research is deep enough when every one of them is `read` and
unrefuted.** Each v0 term names its ledger line(s); a term resting on an
`sa` line, or on a line with an open contradiction, is not yet admissible.

## v0 scope guard (next-pattern, 2026-10-29)

One outcome (hold together or split, and who leaves); three sizes (3,
8–12, 100+); the fewest drives the evidence forces; every term credited;
and a stated test for each size — what observation would refute it —
BEFORE any simulation code. The no-circularity rule of
`notes/2026-10-29-modelled-population-testbed.md` applies from the first run.

## Hygiene before v0 draws on the ledger

Duplicates stay marked, not deleted. Contradictions that touch cohesion,
split or exit are resolved first, by deep-read, because v0 depends on
them; all other contradictions wait.

## Seeding, 2026-10-29

Seeded by one Haiku agent per file from the forty iteration-1 files
(`batch: 1`) and the eleven earlier surveys that hold the equation-set
sources (`batch: 0`, cluster marked `*` because it is the extractor's guess;
those surveys predate the map). 2,770 lines: 856 equations, 720 empirical
results, 469 definitions, 401 drives, 324 contradictions; 1,268 `read`,
1,502 `sa`; 654 marked duplicate of an earlier file. **Caveats:** lines are
extracted, not yet audited — next-pattern audits twenty at random every
third batch; "read" is copied from the file's own tag; duplicate marking
depends on the file's cross-check section, so it undercounts.

Per-cluster yield of iteration 1 (new, non-duplicate lines per direction)
is in `docs/batches/2026-10-29-iteration-1-report-and-batch-2-proposal.md`.
By the convergence rule nothing is near closing: every cluster yielded far
more than one new claim per five directions, which says the corpus is far
from exhausted — and also that the rule, as a stopping criterion, will not
bite while extraction is this fine-grained. A coarser unit (claims the
equation set would rest on, not every definition) is needed before the rule
means "deep enough".

## Audit, 2026-10-29 (next-pattern, twenty lines, seed 20261029)

Extraction faithful: 19/20 supported by their file, 17/17 works exist,
6/7 `read` tags honest, every checkable number and equation matched the
paper. Four habits fixed by a Haiku pass and the rules above: prose
results tagged `equation`; own derivations tagged `sa`; caveats recorded
as contradictions; two sources pinned to one line.

Hygiene pass applied 2026-10-29 (38 Haiku agents over 1684 lines):
522 kind changes (contradiction->note 231, equation->empirical-result 191, equation->definition 42, empirical-result->note 19, definition->equation 18, equation->note 15, definition->empirical-result 2, drive->definition 2, definition->note 1, contradiction->empirical-result 1),
228 provenance changes to `derived`, 232 contradictions demoted to
note, 470 lines split (originals kept with `status: split`). Now
3795 lines: definition 550, empirical-result 1068, equation 812, note 330, drive 443, contradiction 122; provenance read 1514, sa 1515, derived 296.
