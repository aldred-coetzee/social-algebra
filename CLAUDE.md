# social-algebra

## What we are trying to achieve

_Assembled from Aldred's words on 2026-10-29; update whenever he refines it, and date the change. Every batch report opens by restating it in one line._

An **algebra of drives**, of persons and of groups, composed into an
**equation set** with theorems, usable to **predict or steer outcomes** at
three scales — membership (who joins, stays, leaves, conforms), group
(cohesion, decision, split, efficiency) and crowd or society (adoption,
mobilisation, opinion) — **including positively** (better-functioning
groups), and **sensitive to group size, composition and definition**.
Existing societies and groups are working models: commonalities to abstract
from, and better-behaving groups to learn the factors from. Tested first on
a modelled population built independently of the equations, then on data.
"Drives as primitives" is the working hypothesis, tested by every dive, not
assumed. **First outcome (Aldred, 2026-11-01): activity** — how much the
group does and whether it runs away — with holds/splits as a second layer
the model produces, not an input (`notes/2026-11-01-first-outcome-activity.md`).

**Closed 2026-11-01 with `docs/write-up.md`** (Aldred: "Ok write up",
after three pre-registered experiments in one day found that drives as
pre-measured dispositions carry little of a group's outcome and that what
a person did last time, plus coupling and structure, carries most of it).
Nothing below is retracted; it is the brief the work was done under. A
session that reopens the strand starts from `STATUS.md` "Open, if anyone
returns" and `docs/write-up.md` section 5, and does not re-run the survey:
the three decisive experiments cost about one percent of it.

This file is the standing brief. Keep it current — each session starts with
no memory of the last, and the repo is the only continuity. Environment and
working-style rules are in `~/.claude/CLAUDE.md` and are not repeated here.

**Started 2026-10-29. A thinking strand, not an app.** No server. Code only under `sim/` (Python; approved by Aldred 2026-10-29, to test the equations by reproducing published results and fitting open data), **after** the research iterations, and in its own `uv`-managed environment, never system packages. Its own
Remote Control session, `claude-rc-social-algebra`, since 2026-10-29 (Aldred:
"we need a session for it"); unit file in `deploy/systemd/`. **Model pinned to Fable 5.1** in
`.claude/settings.json` (2026-10-29, Aldred: Opus is "not good enough to
define research parameters"); the apps stay on Opus, which is the global
default. A session already running when this landed needs `/model fable` once. `STATUS.md` is the honest state.

## What it is

In Aldred's words, 2026-10-29: *"identifying the mechanics of a social group
in such a way that we can identify operators and operands and later use it to
model interactions."* An algebra whose operands are people, roles and groups
and whose operators are the things they do to one another; first the
notation, later the modelling of interactions in it.

The name was chosen over `group-grammar` and `group-mechanics` because
operators and operands make it an algebra, and "social" keeps a mathematical
reader from expecting group theory.

**Sharpened the same day**: the primitives are **drives** (all of them, for persons and groups; curiosity, fear and desire were examples) and the deliverable is a new or updated **equation set**. Aldred: *"an
algebra which expresses basic human drives and group drives, which we can
compose into equations, which we can then use to start making theorems and
use to control or predict behavior… curiosity, fear, desire, etc."* See
`notes/2026-10-29-drives-as-the-core.md`.

**The goal is the algebra, not writing about it.** Aldred, 2026-10-29: *"It
is not about an article; it is about developing the algebra."* Success is a
notation that captures a group's mechanics well enough to model interactions
in it. If articles follow, they are a by-product.

## Layout

    notes/      raw thinking, dated files, one idea per file
    models/     the algebra itself as it takes shape: definitions, operators,
                worked examples, diagrams (D2 or SVG beside the text)
    docs/       anything written up for a reader; docs/prior-work/ is the
                validated survey, docs/research-map.md its coverage map
    sim/        Python models that test the equations (reproduce published
                results first, then fit open data)

## Citation and credit (Aldred, 2026-10-29)

*"Let's be sure to keep citations and accreditation accurate."* Every
result is credited to the people who proposed or proved it, in the work
where they did, and every DOI must resolve to that work. In practice:

- Nothing is cited from memory. A DOI is checked at Crossref before it is
  written down; a guessed DOI that resolves to another paper is worse than
  none.
- Each survey file gets a separate second pass that checks every citation
  and claim and appends a `## Validation log`; only then is it committed as
  validated. Structural claims carry `[read]` (primary text read) or
  `[from abstract/standard account]`; doubtful items go under
  `Unconfirmed`, never into the body as fact.
- Credit the originator, not the populariser (e.g. β-δ discounting is
  Phelps & Pollak before Laibson), and say when an idea or mapping is ours
  rather than the source's.
- Before anything leaves the repo, a whole-corpus DOI audit resolves every
  DOI against Crossref and compares title and authors with the citing line.

## Context size (Aldred, 2026-11-01)

*"Why aren't you compacting at 200k tokens?"* Rule: once a session's
context passes about 200k tokens, say so and recommend `/compact` at the
next safe point, after making sure `STATUS.md` and the dated notes carry
everything a cold session needs; do not wait for the harness's automatic
compaction, which on a 1M-context model fires far later. **The mechanism exists:** Claude Code's
`autoCompactWindow` setting (tokens; `"autoCompactWindow": 200000`), the
`/autocompact 200000` command (saves per model to user settings) and the
`CLAUDE_CODE_AUTO_COMPACT_WINDOW` environment variable. Set to 200000 in
this project's `.claude/settings.json` on 2026-11-01; the global setting for
every session is requested via next-pattern (`box-config`). Found in the
docs at code.claude.com/docs/en/model-config, "Set the auto-compact
window"; this session had not known of it and should have looked.

## Licensing (Aldred, 2026-10-30)

Nothing goes into the repo that could not be reused when it is open-sourced.
Citations, facts and numbers are free. Equations are restated, not copied
with their surrounding text. Quotations are short and attributed. Tables,
figure contents and lists are transcribed only when the source licence
allows (say which licence) or are reduced to a description. Text derived
from Wikipedia is marked as CC BY-SA. Paywalled text is read, never
reproduced; access controls are never circumvented. Every dive records the
licence of anything quoted or transcribed. **Aldred's email address is never
sent to an external service** (an agent passed it to Unpaywall's API on
2026-10-31 as the required contact parameter; harmless, but it broke the
rule): an API that demands an email gets none, and the lookup is skipped. The audit and per-file table
live in `docs/licensing.md`; `notes/2026-10-30-licensing-check.md` has the why.

## How it connects to the rest

- Separate from the writing pipeline. Nothing here is drafted or published
  unless Aldred one day decides to write about it, and then it goes through
  the normal path from the `writing` workspace. This repo is the work.
- Private to start, like the others. Open-sourcing is a licence and a
  visibility flip; nothing personal beyond the thinking itself lives here.

## Not decided

- The form of the first model: set-theoretic, categorical, or plain
  operator tables. Decide from the notes, not up front.
- Whether diagrams are drawn by hand or generated; `publisher`'s roadmap has
  the D2 route.
