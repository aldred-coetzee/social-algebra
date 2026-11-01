# Status

_Updated 2026-11-01, at the close of the strand._

**Closed with a write-up on 2026-11-01: `docs/write-up.md`.** Aldred, after
the day's three experiments and the question "is it worth continuing":
"Ok write up." The strand ran from 2026-10-29 to 2026-11-01. Its history,
with every decision and its reasoning in date order, is
`docs/history-2026-10-29-to-11-01.md`; the dated `notes/` carry the why of
each turn.

## The finding, in one paragraph

Drives as pre-measured dispositions can be recovered from behaviour when
the right channel is observed (ties, not activity), but they carry little
of a group's outcome. What a person did last time carries most of it, and
composing drives linearly fails even when the true drives are known. The
data supports a state algebra (current behaviour, coupling, structure),
which is the Gottman and Granovetter form the equation set already
adopted, not a trait algebra. Nothing proves the aim impossible; three
pre-registered tests and a favourable synthetic world found no evidence
for drives, as distinct from states, as the primitives.

## What stands

- **Survey:** 118 validated files in `docs/prior-work/`, coverage map
  `docs/research-map.md`, synthesis `docs/synthesis.md`, ledger
  `docs/ledger.jsonl` (5,817 claims with provenance), licensing audit
  `docs/licensing.md`. 2,125 DOIs resolve; one is flagged.
- **Equation set:** `models/00-v0.md` (v0.3), `models/01-composition-and-levers.md`,
  `models/02-our-claims.md`. The theorems are checked; v0.3 was not given
  an outside audit (token cost).
- **Simulator:** `sim/`, uv-managed; 681 tests collected, 16 expected
  failures that record refuted published claims. Every result file in
  `sim/results/` carries its rule, counts, intervals and caveats. Data is
  local-only under `sim/data/` with checksums in `sim/data/README.md`;
  the Newcomb copy is CC BY-NC-ND and must not be redistributed.
- **Decisive results:** `sim/results/apache_fitted_case.md` (criterion
  not met, Opus-reviewed), `sim/results/synthetic_population_identifiability.md`
  (drives recoverable via ties only; composition fails even for the
  oracle), `sim/results/szekely_composition.md` (measured SVO weak; rates
  dominate; no composition rule beats the mean).

## Open, if anyone returns

- **Open modelling decisions** in `models/00-v0.md` section 9 (activity
  instrument per size, Person sort for non-humans, Object and Setting
  sorts, coupling symmetrisation, two-sided gate settings).
- **The one unconfirmed lead:** conversation concentration on Apache
  (+0.083 AUC over size, on already-seen podlings). Podlings started after
  July 2021 would confirm or kill it.
- **Group size with measured drives:** no public dataset found with both.
- **Unrun designs:** the dyad and crowd pre-registered tests in
  `models/00-v0.md` section 8.
- **The reframing**, chosen knowingly or not at all: a state algebra of
  person rates plus coupling, aimed at steering. Smaller and more
  derivative than the aim set out.

## Housekeeping

**Ready to be made public, since 2026-11-01.** Licence chosen and added:
MIT for `sim/` (`LICENSE`), CC BY 4.0 for everything else
(`LICENSE-CC-BY-4.0`); reasoning in `docs/licensing.md`. The licensing
audit now covers every file (the 2026-10-30 pass plus a 2026-11-01 pass
over the files added after it). No email address, secret or dataset is
tracked; `sim/data/` is ignored except its README. Flipping visibility on
GitHub is Aldred's step.

Auto-compaction at 200k tokens is set in this project's
`.claude/settings.json` and globally (`CLAUDE.md`, "Context size"). The
Remote Control unit `claude-rc-social-algebra` stays installed. Token spend
over the strand was about 86M, of which about 1M was the three decisive
experiments.
