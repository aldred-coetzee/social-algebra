# Claim ledger

_Started 2026-10-29 on next-pattern's direction, so that "deep enough" is measurable._

`docs/ledger.jsonl` holds one line per claim the equation set might rest
on. Every dive adds lines; the cross-check marks duplicates; the batch
report gives the yield per cluster.

## Line schema

```json
{"id":"L0001","kind":"equation","statement":"one line","source":"16 §4","work":"Keramati & Gutkin 2014, doi 10.7554/eLife.04811","provenance":"read","status":"open","cluster":"C","added":"2026-10-29","batch":1,"dup_of":null,"scale":"group","ethics":"n/a","note":""}
```

- `kind`: `drive` | `equation` | `empirical-result` | `contradiction` | `definition`
- `provenance`: `read` (the agent fetched and read the primary text) or
  `sa` (abstract or standard account). A validator may upgrade `sa` to
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
- `ethics`: `consent` | `manipulation` | `n/a` — whether the intervention
  or finding steers people with or without their consent. Positive
  steering (improving efficiency, wellbeing, decision quality) is in scope.

## Convergence rule

A cluster of the research map is **closed** when a batch of its directions
adds fewer than one new `open`-or-`adopted` claim per five directions, or
when its directions are exhausted. The research is **deep enough** when
every cluster is closed and every claim the equation set rests on is
`read`.

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
