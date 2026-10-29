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
