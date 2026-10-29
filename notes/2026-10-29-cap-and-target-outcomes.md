# Aldred's answers: the batch cap, and what the equations are for

_2026-10-29, relayed by next-pattern, in his words._

**Cap:** *"Pause after each batch and ask me if we should do the next."*
This replaces both his earlier "don't wait for me between batches" and
next-pattern's one-per-day default. A batch ends with the ten-line report
and the question; nothing starts until he says yes in this session.

**Target outcomes, verbatim:** *"if we can identify the correct variables,
then we should be able to moderate an outcome or produce a result at a
crowd level, at a wider society level, at a group membership level. … I
would imagine a lot of this has already been done to a degree in marketing
practices, in power structures, in military groups, in organizations, in
governments, in organized religion groups. So I'm not sure whether it's
been formalized, but I'm quite sure there's a lot of research in that area.
I'd also be interested to see how we could use this to change the behavior
of a group and influence things in a positive way. Or how we can, in a
positive way, make a group more efficient, and so on. I'm also interested
to see how this would change with group size, and group makeup, or
definition of a group."*

**What this changes:**

- **Three scales** on every `empirical-result` ledger line: `membership`
  (who joins, stays, leaves, conforms), `group` (cohesion, decision, split,
  efficiency), `crowd` (adoption, mobilisation, opinion at society scale).
  "Efficiency" is undefined; collect how each tradition measures it rather
  than choosing one.
- **A new research-map cluster O, applied practice**: marketing and
  persuasion at scale, power and authority structures, military cohesion
  and command, organisational design, government and policy nudging,
  organised religion (recruitment, retention, schism). For each: the
  variables manipulated, the outcome measured, out-of-sample evidence, and
  whether any formal model underlies it. The ledger should show which parts
  have equations and which only doctrine.
- **Two cross-cutting questions answered per cluster, not once:** group
  size (layers, scaling laws, how operators and outcomes change with n) and
  group composition and definition (heterogeneity, boundary and membership
  rules, what makes a set of people a group at all).
- **Positive steering is in scope**: interventions with evidence of
  improving group outcomes (efficiency, wellbeing, decision quality), not
  only control. An `ethics` field on each claim: `consent` | `manipulation`
  | `n/a`.

**Later the same day, also via next-pattern:** *"I imagine we also are
examining texts to do with sociological texts and theories of knowledge and
that kind of thing. And I would imagine social control is a topic that has
been heavily researched ever since we had the first social group, really.
So there should be a lot of information available that we can utilize."*
Two clusters added to the research map: **Q, social control** as a
tradition in its own right across the whole span, and **R, sociology of
knowledge and social epistemology** (how a group fixes what counts as true,
and which drives and operators that works through).

**Also the same day, via next-pattern:** *"we need to also keep it clear on
what we're trying to achieve and recognize that we have working models of
societies, of different societies all over the world. It may be worth
looking at commonalities and seeing what we can abstract from that, and
also perhaps identify groups that behave better than others and look at
the differences. And that may help us to identify the factors that
influence things in both a positive and a negative way."* Two
consequences: a dated **"What we are trying to achieve"** paragraph at the
top of `CLAUDE.md`, mirrored at the top of `docs/research-map.md`, restated
in one line at the start of every batch report so drift is visible; and a
high-priority **comparative cluster S**: existing societies and groups as
working models (cross-cultural data and universals; groups that perform
better and why; natural experiments and divergences), whose first job is a
table of the outcome measures used, so Aldred can choose what "behave
better" means rather than have it chosen for him.

**Aldred's checklist, later the same day**, naming prior work he expects
mapped (sociophysics and opinion dynamics as the closest existing algebra
of group behaviour; Granovetter thresholds; Schelling and Axelrod; Simmel
and Dunbar on size; Pentland), and two hard parts: *"data and
reflexivity. Group behaviour is difficult to measure cleanly, and people
change their behaviour once they know they're being modelled, so
relationships that held in the data stop holding."* And the question to
answer early: *"what would an algebra give you that simulation doesn't? If
the answer is composition, meaning rules for what happens when two groups
merge or one splits, that's a real gap. Most existing work simulates rather
than composes."* The named works are covered (05, 066, 07, 09, 11, 22);
reflexivity in his sense (Merton, Hawthorne, Goodhart, Lucas, performativity)
was NOT covered and is now cluster T with the composition-versus-simulation
cross-check, which also becomes a standing question for the synthesis.

**Evening, after iteration 1 landed (120 agents, 12.5M tokens):** Aldred:
*"I agree, this token spend is wasteful, let's go targeted and let's test
across at least three group sizes."* Broad batches stop. Research is now
pulled by a first draft equation set (v0) and tested at three sizes that
straddle the known thresholds — n = 3 (triad), n ≈ 8–12 (team), n ≈ 100+
(crowd) — against one outcome common to all three: **does the group hold
together or split, and who leaves**, so equations fitted at one size are
tested at the others (the composition test). Composition at fixed size is
varied only after the size test. Batch 2 is twelve targeted directions;
the proposal is `docs/batches/2026-10-29-iteration-1-report-and-batch-2-proposal.md`.

**2026-10-30, after the batch-2 report and the licensing check:** Aldred:
*"write v0 and run the nine reads."* Both at once: `models/00-v0.md` is
written against the ledger as it stands, with every term resting on an
`sa` line marked inadmissible; batch 3 is exactly the nine deep-reads
(research-map cluster V, D587–D595, files 095–103). When they land, v0's
provenance is updated and the inadmissible marks lifted where the read
confirms the claim.
