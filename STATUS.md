# Status

_Updated 2026-11-05: the repo is public. The strand closed 2026-11-01._

**Final state, 2026-11-01: closed; reduces to existing work.** Close-out
done the same day: record corrections (the 16 expected failures, the
oracle under C2), the Apache review recovered into its results file,
caveat headers on the Szekely and Bitcoin results, the dyad test listed
as designed-not-run, an oracle validity check (the generator carries
memory in its relationship state and exit streak; with both removed C2
still fails at n = 8 and 25, Review section of
`sim/results/synthetic_population_identifiability.md`), and an article
draft at `docs/article-draft.md`. Nothing is left to run.

**Closed with a write-up on 2026-11-01: `docs/write-up.md`.** Aldred, after
the day's three experiments and the question "is it worth continuing":
"Ok write up." The strand ran from 2026-10-29 to 2026-11-01. Its history,
with every decision and its reasoning in date order, is
`docs/history-2026-10-29-to-11-01.md`; the dated `notes/` carry the why of
each turn. **A post-mortem, `docs/post-mortem.md` (2026-11-01, asked for
by Aldred after the close), answers six questions from the repo: the
hypothesis as formulated, every approach in order and why it failed, the
category of the conclusion (it reduces to existing work), what survived,
the overlapping literature, and whether the negative is writeable up.
It also named two places where the write-up overstated the files: the
Apache fitted-case review was not recorded in its results file, and the
16 expected failures record refuted claims of v0, not of published work.
Both were corrected at the close-out the same day.**

## The finding, in one paragraph

Drives as pre-measured dispositions can be recovered from behaviour when
the right channel is observed (ties, not activity), but they carry little
of a group's outcome. What a person did last time carries most of it, and
composing recovered drives linearly fails at every size; given the true
drives the same rule beats person rates at n = 8 only. The
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
- **Simulator:** `sim/`, uv-managed; 681 tests collected, 16 strict
  expected failures: 13 record refuted claims of v0's own (two dead-zone,
  eleven sign-registry), 3 record Leonard's Table 1 transverse condition,
  which our reduction could not reproduce. Every result file in
  `sim/results/` carries its rule, counts, intervals and caveats. Data is
  local-only under `sim/data/` with checksums in `sim/data/README.md`;
  the Newcomb copy is CC BY-NC-ND and must not be redistributed.
- **Decisive results:** `sim/results/apache_fitted_case.md` (criterion
  not met; the Opus review of it, recovered from the subagent transcript
  at the close-out, is now the file's Review section),
  `sim/results/synthetic_population_identifiability.md`
  (drives recoverable via ties only; composition of recovered drives
  fails at every size; the oracle passes C2 at n = 8 only, a correction
  made at the close-out to a flat "fails even for the oracle"; a
  memoryless re-run at the close-out, Review section, finds the
  person-rates advantage is not built from the generator's memory),
  `sim/results/szekely_composition.md` (measured SVO weak; rates
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
  `models/00-v0.md` section 8. **The dyad test is designed and not run.**
  It needs a public dyadic expressed-affect series with a lag; the
  Gottman SPAFF series are not public and the Sels smartphone samples
  are the authors'. The one candidate named in section 8, K-EmoCon
  (16 dyads, Zenodo), was named from memory and its DOI, licence and
  fit were never checked.
- **The reframing**, chosen knowingly or not at all: a state algebra of
  person rates plus coupling, aimed at steering. Smaller and more
  derivative than the aim set out.

## Housekeeping

**Public since 2026-11-05** (Aldred flipped the visibility on GitHub;
confirmed from outside the same day, the API reports `visibility:
public`). The sweep was repeated at the flip: no email address, secret
or dataset in any tracked file; the nine files changed after the
2026-11-01 audit (post-mortem, article draft, the four results-file
additions, write-up, STATUS, README) hold only our own words and short
quotations of Aldred's; `worklog/` holds counts only, no prompt text.
One thing a public git history always shows and this one does: the
author email on every commit (268 of them). Nothing was done about it;
changing it would mean another history rewrite and force-push, which is
Aldred's call. Licence chosen and added 2026-11-01:
MIT for `sim/` (`LICENSE`), CC BY 4.0 for everything else
(`LICENSE-CC-BY-4.0`); reasoning in `docs/licensing.md`. The licensing
audit now covers every file (the 2026-10-30 pass plus a 2026-11-01 pass
over the files added after it). No email address, secret or dataset is
tracked; `sim/data/` is ignored except its README.

**Commit history is clean of AI trailers since 2026-11-01.** The
harness's `Co-Authored-By` trailer had been added to 115 commits against
the global rule; the history was rewritten (tree unchanged) and
force-pushed by Aldred from Termux, because this session's permission
layer refuses force-pushes. Commits here carry no trailer.

Auto-compaction at 200k tokens is set in this project's
`.claude/settings.json` and globally (`CLAUDE.md`, "Context size"). The
Remote Control unit `claude-rc-social-algebra` stays installed. Token spend
over the strand was about 86M, of which about 1M was the three decisive
experiments.
