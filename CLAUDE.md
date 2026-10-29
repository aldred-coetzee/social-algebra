# social-algebra

This file is the standing brief. Keep it current — each session starts with
no memory of the last, and the repo is the only continuity. Environment and
working-style rules are in `~/.claude/CLAUDE.md` and are not repeated here.

**Started 2026-10-29. A thinking strand, not an app.** No server. Code only under `sim/` (Python; approved by Aldred 2026-10-29, to test the equations by reproducing published results and fitting open data). Its own
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
