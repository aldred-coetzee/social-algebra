# Prior work 07: applied and engineering approaches to steering and predicting groups

Date: 2026-10-29. Cluster: cybernetics, doctrine, organisation design, simulation.

## Summary

Steering groups is not new, and it has been formalised many times. The
formalisations split into three families. (1) Control-theoretic: groups are
systems with state, disturbances and regulators (Wiener, Ashby, Beer,
Forrester, Meadows). (2) Game-theoretic and rule-design: groups are players
with preferences and the designer chooses the rules (mechanism design,
reflexive game theory, coalition games, Axelrod). (3) Simulation: groups
emerge from rules on individuals (Sugarscape, Axelrod's culture model).

Only two items here have anything resembling an operator algebra over social
operands: Lefebvre's reflexive game theory (Boolean algebra over choices, with
alliance as product and conflict as sum) and cooperative game theory
(coalitions as sets, a characteristic function over them). Everything else is
either verbal doctrine, differential equations over aggregate quantities, or
simulation code. The empirical record on prediction is poor at the individual
level and mixed at the aggregate level.

**Method note.** Sources were found by web search and page fetches on
2026-10-29. Many details come from Wikipedia summaries or abstracts rather
than the primary text, and this is flagged per entry. Primary texts were not
read for any entry. Items I could not confirm are in "Unconfirmed" at the end.

---

## 1. Wiener: cybernetics applied to society

- **Citation.** Norbert Wiener, *The Human Use of Human Beings: Cybernetics and
  Society*. Boston: Houghton Mifflin, 1950; revised edition 1954.
- **Verified at.** https://en.wikipedia.org/wiki/The_Human_Use_of_Human_Beings
  and library catalogue records (publisher and date confirmed by search
  results, e.g. https://www.computerhistory.org/collections/catalog/102622273).
  Full text copy located but not read: https://bob.cs.ucdavis.edu/assets/ecs188/weiner_humanuse.pdf
- **Their vocabulary.** Message, communication facility, feedback, learning,
  homeostasis, negentropy, pattern. Wiener's thesis, as summarised: society
  "can only be understood through a study of the messages and the
  communication facilities which belong to it."
- **Operands (translated).** Persons, machines and institutions as
  message-sending and receiving nodes; messages themselves.
- **Operators (translated).** Send, receive, feed back, adjust. Formal
  structure: none in this book. It is a popular, informal exposition; the
  mathematics lives in his other work (not examined here). [from abstract/standard account]
- **Predictive/control claim.** Not a predictive claim. A framing claim:
  social order is maintained by communication loops, and breakdown of
  communication is breakdown of order. He warns about automation and about
  machines escaping supervision.
- **Limits.** Informal; no social operators defined; the analogy from
  organism to society is asserted rather than derived.
- **Relevance.** Origin of the "group as a communicating system" frame.
  Suggests messages are first-class operands, not just people.

## 2. Ashby: law of requisite variety

- **Citation.** W. Ross Ashby, *An Introduction to Cybernetics*. London:
  Chapman & Hall, 1956, ch. 11, pp. 206-208 for the law. Also Ashby, "Requisite
  Variety and its Implications for the Control of Complex Systems",
  *Cybernetica* 1(2): 83-99, 1958.
- **Verified at.** https://en.wikipedia.org/wiki/Variety_(cybernetics) (formal
  statement, page numbers); https://en.wikipedia.org/wiki/An_Introduction_to_Cybernetics .
  The book's own wording is "only variety can destroy variety" (p. 207); the
  survey originally dropped "only". (Validator, from knowledge of the text.)
  The Operators wording below follows the Wikipedia article "Variety
  (cybernetics)", CC BY-SA 4.0.
- **Their vocabulary.** Variety (log of number of distinguishable states),
  disturbance, regulator, outcome.
- **Operands.** Sets of distinguishable states of a disturbance source, of a
  regulator, and of outcomes.
- **Operators.** A regulator's response is a function of the disturbance.
  Formal and exact: with variety V = log2(number of states), V_O >= V_D - V_R.
  Entropy form: H(E) >= H(D) - H(R). Derived for a two-player game in which
  the regulator sees the disturbance and plays a deterministic strategy. [from abstract/standard account]
- **Predictive/control claim.** A necessary condition: a controller cannot
  reduce outcome variety below disturbance variety minus its own. Necessary,
  not sufficient (standard gloss on Ashby 1956, ch. 11, pp. 206-208). It is a theorem about a model, not an empirical claim
  about societies.
- **Limits.** Variety depends on the observer's powers of discrimination.
  Applications to organisations and nations are later interpretation (Beer
  and others), not part of the formal result.
- **Relevance.** A hard constraint any social algebra should be able to state:
  how much of a group's state can an operator set cover? Gives a counting
  argument for why simple control of complex groups fails.

## 3. Beer: Viable System Model and Project Cybersyn

- **Citations.** Stafford Beer, *Brain of the Firm* (1972); *The Heart of
  Enterprise* (1979); *Diagnosing the System for Organizations* (1985).
  Eden Medina, *Cybernetic Revolutionaries: Technology and Politics in
  Allende's Chile* (Cambridge, MA: MIT Press, 2011).
- **Verified at.** https://en.wikipedia.org/wiki/Viable_system_model (works,
  structure); https://en.wikipedia.org/wiki/Project_Cybersyn (components,
  dates, use); review of Medina at https://muse.jhu.edu/article/522475/pdf
  (seen in search results, not opened). Facts and wording in this section
  follow the Wikipedia articles "Viable system model" and "Project
  Cybersyn", CC BY-SA 4.0.
- **Their vocabulary.** Viable system, System 1 to 5, recursion, variety,
  algedonic signal (pain/pleasure alert), homeostat, operations room.
- **Operands (translated).** Organisational units (System 1: operational
  parts, each itself a viable system), coordination, control, intelligence
  and policy functions, plus the environment. Recursion means the same
  description applies at every level.
- **Operators (translated).** Coordinate (S2), allocate resources and audit
  (S3, S3*), scan environment (S4), set policy and balance present against
  future (S5), escalate algedonic alert. Formal structure: partly formal. The
  VSM is presented with principles, axioms, a recursive system theorem and a
  law of cohesion, and a triple measure (actuality, capability, potentiality)
  with derived ratios. It is a rule-based design framework, not a calculus
  with defined composition. [from abstract/standard account]
- **Predictive/control claim.** Any viable organisation must contain these
  five functions (claimed). Cybersyn: CHECO (economic simulator), Cyberstride
  (factory monitoring), Cybernet (telex), Opsroom, built 1971-73. In use,
  only Cybernet was regularly used; during the October 1972 truckers' strike
  it helped coordinate transport. Only about twenty factories were connected;
  the project ended with the coup in September 1973.
- **How it held up.** No independent test of the VSM's central claim is cited
  in the pages I read. Medina argues the VSM was a heuristic for action, not
  an exact model of the economy. Critics read it as top-down centralisation
  (deviations up, corrections down); defenders dispute this.
- **Limits.** Largely unfalsifiable as stated (any surviving organisation can
  be mapped onto five functions after the fact). Per-factory modelling was
  slow: one engineer per factory.
- **Relevance.** The strongest example of a role-and-channel structure with
  recursion. Recursion (a group member is itself a group) is something the
  algebra must decide on early.

## 4. Lefebvre: reflexive control (doctrine)

- **See 03 §3** for Lefebvre's algebra (reflexive game theory, the Boolean
  alliance/conflict polynomial, decision equation, the two ethical systems).
  Unique to this file's angle: the military doctrine below.
- **Citations.**
  - Timothy L. Thomas, "Russia's Reflexive Control Theory and the Military",
    *Journal of Slavic Military Studies* 17(2): 237-256 (2004).
    DOI 10.1080/13518040490450529 (DOI as given on the Wikipedia reflexive
    control page; the procon.bg listing gives volume and pages with no DOI,
    and links the PDF at www.rit.edu/~cmmc/conferences/2007/literature/Thomas_2004.pdf).
  - V. A. Lefebvre, "Reflexive analysis of groups", in S. Argamon and N. Howard
    (eds.), *Computational Methods for Counterterrorism*, Springer, 2009,
    pp. 173-210.
- **Doctrine side (Thomas 2004).** Reflexive control, as described: passing
  specially prepared information to an opponent so that the opponent
  voluntarily makes the decision the initiator wants. Komov's list of
  elements (as relayed by Thomas) is longer than the four given here
  originally: distraction, overload, paralysis, exhaustion, deception,
  division, pacification, deterrence, provocation, suggestion, pressure
  (validator, from knowledge of Thomas 2004; not re-read).
  Informal, no formal model in the doctrine itself.
- **Predictive/control claim.** The doctrine claims decisions of an
  adversary can be steered by shaping the information that feeds them.
  Examples cited (Operation Mincemeat, Cold War missile disinformation) are
  anecdotes, not tests.
- **How it held up.** No systematic empirical validation of RGT found; see 03 §3
  for the critiques.
- **Relevance.** High. Key lesson: operands include a subject's model of
  others, not just the subject.

## 5. Forrester and the Meadows team: system dynamics

- **Citations.**
  - Jay W. Forrester, *Industrial Dynamics* (Cambridge, MA: MIT Press, 1961).
  - Jay W. Forrester, *Urban Dynamics* (Cambridge, MA: MIT Press, 1969; later
    reprinted by Pegasus Communications, which the survey had given as the
    original publisher); and "Counterintuitive Behavior of Social Systems",
    *Theory and Decision* 2(2): 109-140 (1971), also in *Technology Review*
    73(3), 1971.
  - Jay W. Forrester, *World Dynamics* (Cambridge, MA: Wright-Allen Press,
    1971). The "1968" date is a confusion with his *Principles of Systems*
    (1968).
  - Meadows, D. H., Meadows, D. L., Randers, J., Behrens, W. W. III, *The
    Limits to Growth*. New York: Universe Books, 1972.
  - Retrospectives: G. M. Turner, "A comparison of The Limits to Growth with
    30 years of reality", *Global Environmental Change* 18(3): 397-411
    (2008) (CSIRO); G. M. Turner, "Is Global Collapse Imminent?", Melbourne
    Sustainable Society Institute Research Paper No. 4 (2014), a working
    paper, not peer reviewed; G. Herrington, "Update to limits to growth:
    Comparing the World3 model with empirical data", *Journal of Industrial
    Ecology* 25(3): 614-626 (2021; online November 2020), DOI
    10.1111/jiec.13084 (volume, pages and DOI from validator's knowledge).
  - Critique: H. S. D. Cole et al. (eds.), *Models of Doom: A Critique of the
    Limits to Growth* (Sussex SPRU; New York: Universe Books, 1973).
- **Verified at.** https://www.systemdynamics.org/origin-of-system-dynamics ;
  https://en.wikipedia.org/wiki/Urban_Dynamics ;
  https://en.wikipedia.org/wiki/The_Limits_to_Growth ;
  https://en.wikipedia.org/wiki/Jay_Wright_Forrester
- **Their vocabulary.** Stock, flow, feedback loop, delay, counterintuitive
  behaviour, overshoot and collapse, policy lever.
- **Operands.** Aggregate quantities: population, housing, industry, pollution,
  resources, capital. People are not individually represented.
- **Operators.** Rates (flows) that are functions of stocks and of other
  stocks, composed into coupled differential or difference equations
  integrated on a computer (DYNAMO). Formal and exact as a model class.
  World3 was built on five variables: population, food production,
  industrialisation, pollution, non-renewable resource use. [from abstract/standard account]
- **Predictive/control claim.** Policies that look sensible can worsen
  outcomes (Urban Dynamics: low-income housing programmes and lower property
  taxes would worsen the shortage of jobs relative to population, per
  Wikipedia's summary; wording follows the Wikipedia article "Urban Dynamics", CC BY-SA 4.0). Limits to Growth: business-as-usual leads to overshoot
  and collapse in the 21st century.
- **How it held up.** Limits to Growth: Turner (CSIRO 2008) found 1970-2000
  data across the model's main variables (population, birth and death
  rates, food, industrial output, services, pollution, resources) closest
  to the standard run, and a poor fit to the comprehensive-technology and
  stabilised-world runs. The 2014 Melbourne paper is **Turner again**, not
  an independent study, updating the same comparison. Herrington (2021)
  found the closest fits were **BAU2** (business as usual with doubled
  resources) **and CT** (comprehensive technology), not the original
  standard run; both show growth stopping around 2030-2040, BAU2 followed
  by decline. So the record is one author twice plus one independent
  update, all comparing trajectories, not out-of-sample tests of turning
  points (no turning point had yet occurred). Against: resource-price predictions did not materialise; critics
  (Passell, Sussex SPRU, J. Simon) called it sensitive to a few assumptions.
  A defender (source not recorded) notes the authors meant predictions only in
  the most limited sense. Urban Dynamics: controversial; I did not obtain a track-record
  assessment beyond that.
- **Limits.** Parameters are partly judgemental; results sensitive to
  structure; aggregation removes the group-level mechanics entirely.
- **Relevance.** A different level: the algebra of flows between populations.
  Useful as a target to which an individual-level algebra should aggregate.
  Not an algebra of interaction.

## 6. March & Simon, and Cyert & March: organisation theory

- **Citations.**
  - James G. March and Herbert A. Simon, *Organizations*. New York: John
    Wiley, 1958 (second edition Blackwell, 1993).
  - Richard M. Cyert and James G. March, *A Behavioral Theory of the Firm*,
    Englewood Cliffs, NJ: Prentice-Hall, 1963 (second edition Blackwell,
    1992).
- **Verified at.** WorldCat record https://search.worldcat.org/title/organizations/oclc/27143917 ;
  https://en.wikipedia.org/wiki/Herbert_A._Simon ;
  https://en.wikipedia.org/wiki/A_Behavioral_Theory_of_the_Firm
- **Their vocabulary.** Bounded rationality, satisficing, inducements and
  contributions, uncertainty absorption, coalition, organisational slack,
  aspiration level, performance programs (March & Simon); and Cyert & March's
  four relational concepts: quasi-resolution of conflict, uncertainty
  avoidance, problemistic search, organisational learning (validator, from
  knowledge of the book).
- **Operands.** Members and sub-groups as a coalition; goals; decision
  premises; slack (resources beyond what keeps groups in).
- **Operators.** Set goals by negotiation among groups; search when
  performance falls below aspiration; accept the first adequate option; use
  slack to absorb shocks. Mostly verbal, but the 1963 book does contain
  computer-simulation models (a duopoly model and a department-store
  price-and-output model), so "informal" understates it. [from abstract/standard account]
- **Predictive/control claim.** Firms behave as satisficing coalitions, not
  profit maximisers. Mostly explanatory.
- **Limits.** Seen by critics as unnecessarily complicated; some defend
  profit maximisation.
- **Relevance.** Provides the vocabulary for bargaining inside a group and
  for slack as a buffer stock (not conserved: it grows in good times and is
  absorbed in bad). Inducements/contributions is an exchange
  operator between a member and a group.

## 7. Mechanism design (Hurwicz, Maskin, Myerson)

- **Citation.** Nobel Prize in Economic Sciences 2007 to Leonid Hurwicz, Eric
  Maskin, Roger Myerson "for having laid the foundations of mechanism design
  theory".
- **Verified at.** https://www.nobelprize.org/prizes/economic-sciences/2007/press-release/ ;
  https://www.kva.se/en/news/ekonomipriset-2007-2/ ; formal structure from
  https://en.wikipedia.org/wiki/Mechanism_design (the Nobel advanced
  information PDF returned 403); wording of the formal structure follows the
  Wikipedia article "Mechanism design", CC BY-SA 4.0.
- **Their vocabulary.** Type, social choice function, mechanism,
  implementation, incentive compatibility, revelation principle.
- **Operands.** Agents with private types; outcomes (allocation plus
  transfers).
- **Operators.** A mechanism maps reported types to an outcome. Formal and
  exact. Incentive compatible if truthful reporting is optimal. Revelation
  principle: any equilibrium outcome can be reproduced by a direct truthful
  mechanism. Implementation may be dominant-strategy or Bayesian-Nash. [from abstract/standard account]
- **Predictive/control claim.** For a designer who can set the rules, desired
  outcomes can be made equilibria, under stated assumptions.
- **Limits (formal).** Gibbard-Satterthwaite (Gibbard 1973, *Econometrica*
  41: 587-601; Satterthwaite 1975, *JET* 10: 187-217): a deterministic social
  choice function that is onto at least three outcomes and defined on all
  strict preference profiles is strategy-proof (dominant-strategy truthful)
  only if it is dictatorial. Myerson-Satterthwaite (1983, *JET* 29: 265-281):
  in bilateral trade with independent private values whose supports overlap,
  no mechanism is simultaneously Bayesian incentive compatible, interim
  individually rational, budget balanced and ex post efficient. (The survey's
  "without risking forced losses" was a loose paraphrase of individual
  rationality.) Escape routes need extra assumptions (quasilinear utility
  admits VCG mechanisms, which are strategy-proof and efficient but not
  budget balanced).
- **Relevance.** The most mature formal treatment of rules as operators on
  groups of self-interested operands. But it assumes rational agents with
  fixed preferences and a designer with commitment power.

## 8. Thaler & Sunstein: choice architecture

- **Citation.** Richard H. Thaler and Cass R. Sunstein, *Nudge: Improving
  Decisions About Health, Wealth, and Happiness*. New Haven: Yale University
  Press, 2008.
- **Verified at.** Catalogue record https://discover.aclib.us/Record/204774 ;
  https://en.wikipedia.org/wiki/Nudge_(book)
- **Their vocabulary.** Nudge, choice architecture, default, libertarian
  paternalism.
- **Operands.** An individual's decision context: the option set and how it is
  presented.
- **Operators.** Set default, reorder or place options, pre-commit
  (Save More Tomorrow). Informal; defined as any aspect of choice
  architecture that alters behaviour predictably without forbidding options
  or changing incentives much. [from abstract/standard account]
- **Predictive/control claim.** Presentation predictably shifts behaviour.
- **How it held up.** Critics: Gigerenzer says the term has been stretched to
  cover almost anything, which makes it meaningless. The House of Lords
  Science and Technology Committee's *Behaviour Change* report (2011) found
  that non-regulatory measures including nudges, used in isolation, are
  less likely to be effective, and that evidence on population-level
  application was thin (a phrase once attributed to the report was not found in the
  report summaries and has been removed). Meta-analysis: Mertens et al., *PNAS*
  119(1) e2107346118 (2022) reported a mean effect of d ≈ 0.43 across 200+
  studies; Maier et al., *PNAS* 119(31) e2200300119 (2022) argued that after
  correcting for publication bias there is no evidence of an overall effect.
  (Citation details from validator's knowledge.)
- **Limits.** Individual-level; says nothing about interaction within groups.
- **Relevance.** Shows the design lever is often the context, not the agent.
  Contexts may need to be operands.

## 9. Epstein & Axtell: Sugarscape

- **Citation.** Joshua M. Epstein and Robert L. Axtell, *Growing Artificial
  Societies: Social Science from the Bottom Up*. Washington, DC: Brookings
  Institution Press; Cambridge, MA: MIT Press, 1996.
- **Verified at.** https://www.brookings.edu/books/growing-artificial-societies ;
  https://users.monash.edu/~aland/reviews/epstein.rev.html ;
  https://en.wikipedia.org/wiki/Sugarscape
- **Their vocabulary.** Agent, landscape, rule, emergence, generative social
  science.
- **Operands.** Agents on a grid with genetic attributes (vision, metabolism,
  speed) and cells holding a resource (sugar, later spice).
- **Operators.** Local rules: move to the nearest rich cell, metabolise,
  reproduce, trade, fight, exchange cultural tags, transmit disease. Exact as
  code; no algebra of the rules themselves. [from abstract/standard account]
- **Predictive/control claim.** Not prediction. The claim is generative: if a
  macro pattern can be grown from micro rules, the rules are a candidate
  explanation. Group formation, cultural transmission, combat and trade
  emerge.
- **How it held up.** Replication is a known problem: implementations often
  cannot reproduce the book's results exactly (wording follows the Wikipedia article "Sugarscape", CC BY-SA 4.0,
  which cites Leicester replication notes).
- **Limits.** The rule set is chosen by the modeller; many rule sets can give
  the same macro pattern.
- **Relevance.** Evidence that rule sets over simple agents can generate group
  structures. A social algebra could be read as the specification language
  for such rules.

## 10. Axelrod: cooperation tournaments (culture model: see 05)

- **Citations.**
  - R. Axelrod, "Effective Choice in the Prisoner's Dilemma", *Journal of
    Conflict Resolution* 24(1): 3-25 (1980).
  - R. Axelrod, *The Evolution of Cooperation*. New York: Basic Books, 1984.
  - Critique: A. Rapoport, D. A. Seale, A. M. Colman, "Is Tit-for-Tat the
    Answer? On the Conclusions Drawn from Axelrod's Tournaments", *PLoS ONE*
    10(7): e0134128 (2015). DOI 10.1371/journal.pone.0134128.
- **Verified at.** https://pmc.ncbi.nlm.nih.gov/articles/PMC4520619 (the critique, fetched).
  The 1980 and 1984 citations are as given in secondary sources in search
  results.
- **Their vocabulary.** Strategy, iterated Prisoner's Dilemma, Tit for Tat,
  tournament, payoff matrix. The culture model (Axelrod 1997) is in 05 §23.
- **Operands.** Strategies (programs).
- **Operators.** Tournament: pairwise iterated play with a payoff matrix.
  Exact as an algorithm. [from abstract/standard account]
- **Predictive/control claim.** Tit for Tat (cooperate first, then copy)
  won both tournaments.
- **How it held up.** Rapoport et al. report Tit for Tat won only 11.0% of
  re-run two-stage tournaments with the original 15 entries, versus 30.0% for
  another program, and that its success depends on format, success criterion
  and payoff values. So the "winning strategy" result is contingent.
- **Relevance.** A compact example of a social operator (iterated play). Culture-model
  operator: see 05.

## 11. Limits of prediction: MusicLab and Fragile Families

- **Citations.**
  - M. J. Salganik, P. S. Dodds, D. J. Watts, "Experimental Study of
    Inequality and Unpredictability in an Artificial Cultural Market",
    *Science* 311: 854-856 (2006). DOI 10.1126/science.1121066.
  - M. J. Salganik et al., "Measuring the predictability of life outcomes with
    a scientific mass collaboration", *PNAS* 117(15): 8398-8403 (2020).
    DOI 10.1073/pnas.1915006117.
- **Verified at.** https://pdodds.w3.uvm.edu/research/papers/years/2006/salganik2006a.pdf ;
  https://acawiki.org/Experimental_Study_of_Inequality_and_Unpredictability_in_an_Artificial_Cultural_Market ;
  https://collaborate.princeton.edu/en/publications/measuring-the-predictability-of-life-outcomes-with-a-scientific-m/ ;
  https://dspace.mit.edu/handle/1721.1/130285
- **Findings.** MusicLab: 14,341 participants downloading unknown songs, some
  seeing others' download counts. More social influence gave more inequality
  and more unpredictability; quality mattered only partly. Fragile Families:
  160 teams built models for six life outcomes using a rich birth-cohort
  dataset; the best predictions "were not very accurate and were only
  slightly better than those from a simple benchmark model" (a regression on
  four variables), and within each outcome error was strongly associated
  with the family being predicted and weakly with the technique. Best
  holdout R² was about 0.2 for the continuous outcomes (GPA, material
  hardship) and much lower for the other four (validator, from memory of
  the paper's Fig. 3; treat the numbers as approximate). The MusicLab paper is
  *Science* 311(5762).
- **Vocabulary and structure.** Empirical experiments, not formal models. No
  operators proposed. [from abstract/standard account]
- **Relevance.** Sets the bar. These are the best-known empirical limits on
  prediction in social systems.

## 12. Cliodynamics and psychohistory

- **Citations.** Isaac Asimov, *Foundation* series (fiction; cultural
  reference only). Turchin's books and model: **see 08 §3.** Forecast
  papers kept here: Turchin, "Political instability may be a contributor in
  the coming decade", *Nature* 463: 608 (2010); Turchin, "Arise
  'cliodynamics'", *Nature* 454: 34-35 (2008); Turchin, "Dynamics of
  political instability in the United States, 1780-2010", *Journal of Peace
  Research* 49(4): 577-591 (2012); Turchin and Korotayev, "The 2010
  structural-demographic forecast for the 2010-2020 decade: A retrospective
  assessment", *PLoS ONE* 15(8): e0237458 (2020) — published, not only a
  preprint. (Details from validator's knowledge.)
- **Verified at.** https://en.wikipedia.org/wiki/Cliodynamics ;
  https://peterturchin.com/the-science-behind-my-forecast-for-2020/ ;
  https://today.uconn.edu/2016/12/using-social-science-to-predict-the-future
  (all via search results or summaries; none read in full). Wording in this
  section follows the Wikipedia article "Cliodynamics", CC BY-SA 4.0.
- **Vocabulary, operands, operators.** See 08 §3 (Turchin's coupled aggregate
  equations); this entry covers the psychohistory framing and the 2010 forecast only.
- **Predictive claim.** In 2010, a ~50-year instability cycle (peaks around
  1870, 1920, 1970) pointed to roughly 2020 as a period of rising instability
  in the US and Western Europe.
- **How it held up.** Popular press treated 2020 as vindication; the 2020
  retrospective is by the authors themselves. This is a single, broad,
  low-resolution call, and no independent formal evaluation was found.
  Critics reject reducing societies to points in phase space and say the
  historical data are too inconsistent.
- **Relevance.** Real attempt at the Asimov programme; works at the scale of
  centuries and populations, far above the interaction level.

## 13. Additions: Lanchester and cooperative game theory

### 13a. Lanchester / Osipov combat models

- **Citation.** F. W. Lanchester, *Aircraft in Warfare* (1916). Priority
  dispute: M. Osipov's 1915 paper in a Tsarist military journal (English
  translation hosted at FSU).
- **Verified at.** https://en.wikipedia.org/wiki/Lanchester%27s_laws ;
  https://math.fsu.edu/~mesterto/NewCourses/MAP5932/2016/PDF/PDF02/Osipov1995aEngagedForces.pdf ;
  https://dupuyinstitute.org/2017/07/03/osipov/
  (priority-dispute and historical wording follows the Wikipedia article
  "Lanchester's laws", CC BY-SA 4.0)
- **Operands.** Sizes of two opposing forces A, B. **Operators.** Coupled
  differential equations. Aimed fire: dA/dt = -βB, dB/dt = -αA, which
  conserves αA² - βB² (the square law: strength goes as effectiveness times
  numbers squared). Unaimed/area fire: dA/dt = -βAB, dB/dt = -αAB, which
  conserves αA - βB (a linear law); Lanchester's own linear law was for
  one-on-one "ancient" combat. The survey's single sentence described only
  the aimed-fire case.
- **Claim and record.** Adopted by US operations researchers for land combat
  models from the 1950s, although Lanchester framed them for air combat. An
  ANZIAM Journal paper (https://journal.austms.org.au/ojs/index.php/ANZIAMJ/article/view/2584)
  states they "have never been validated for complex land battles despite
  numerous attempts". Fits to historical battles exist (Engel 1954 on Iwo
  Jima; Lucas and Turkes 2004 on Kursk and Ardennes, *Naval Research
  Logistics* 51) and typically find neither pure law fits well.
- **Relevance.** Group-versus-group interaction as a two-operand operator on
  group sizes.

### 13b. Cooperative game theory (coalitions)

- **Content.** The characteristic function assigns a value to every subset
  (coalition) of players; solution concepts include the von Neumann-
  Morgenstern stable sets (1944), the Shapley value (1953) and the core
  (Gillies, 1953 thesis, published 1959 in *Contributions to the Theory of
  Games* IV; the survey's "1954" is wrong); the Shapley value averages a
  player's marginal contribution over all orderings.
- **Verified at.** https://encyclopediaofmath.org/wiki/Cooperative_game ;
  https://iam2.metu.edu.tr/sites/iam2.metu.edu.tr/files/iamData/LectureNotes/lecture_notes_on_cooperative_game.pdf ;
  https://economics.brown.edu/sites/g/files/dprerj726/files/papers/2007-11_paper.pdf
  (all from search result summaries; not read in full).
- **Operands.** Players and subsets of players. **Operators.** v: 2^N to the
  reals, and allocation rules. Exact. Set-theoretic.
- **Limits.** Assumes transferable value and exogenous coalitions in the basic
  form. Coalition structures: R. J. Aumann and J. H. Drèze, "Cooperative
  games with coalition structures", *International Journal of Game Theory*
  3: 217-237 (1974) — exists (validator's knowledge); it treats a partition
  of players as given and extends solution concepts to it. Endogenous
  coalition formation is a later literature (e.g. Hart and Kurz 1983).
- **Relevance.** The existing set-theoretic algebra of coalitions. Any social
  algebra with union/intersection of groups overlaps with it.

---

## What this cluster already covers

- **Control as a constraint.** Ashby's law gives a precise bound on regulation.
- **Role/channel structure with recursion.** Beer's VSM.
- **Alliance and conflict as Boolean operators over choices.** Lefebvre's RGT
  and Tarasenko's follow-ups. This is the closest prior art to the target.
- **Rule design for self-interested groups.** Mechanism design, with
  impossibility theorems.
- **Aggregate feedback dynamics.** System dynamics; Lanchester for
  force-on-force.
- **Coalitions as sets with value.** Cooperative game theory.
- **Emergence from local rules.** Sugarscape, Axelrod.
- **Explicit measurement of unpredictability.** MusicLab, Fragile Families.

## What it does not cover

- **No common notation.** Each field has its own operands and operators, and
  none compose across fields.
- **Informal where it matters.** Wiener, March and Simon, Thaler and Sunstein
  and the reflexive-control doctrine are verbal. Beer's rules are
  semi-formal.
- **Operators on relationships.** Mostly the relationship is a parameter
  (alliance edge, payoff), not an object that operators create, destroy or
  transform. Roles as operands, and operations that change roles, are weakly
  represented. [from abstract/standard account]
- **Group-level mechanics with individual detail.** System dynamics erases
  individuals; agent models erase group structure unless it is coded in.
- **Validation.** I found almost no out-of-sample tests of any model. Limits
  to Growth has the best-documented track record here, and even that is argued.
- **Mutual modelling at depth.** RGT captures it for small discrete cases;
  the critique that it ignores levels of reflexion stands in what I read.

## What the evidence says about limits of predicting group behaviour

1. **Social influence makes outcomes path-dependent.** In MusicLab, the same
   songs gave different hit lists in different parallel worlds, and stronger
   influence widened the spread. Even perfect knowledge of the parts did not
   fix the whole.
2. **Rich data and many teams did not help much at individual level.**
   Fragile Families: 160 teams, best models only modestly better than a
   simple benchmark; error driven more by the case than by the method.
3. **Aggregate trend forecasts have fared better, with caveats.** Limits to
   Growth's standard run tracked several indicators for 30-plus years per
   Turner (2008, 2014 — the same author both times); Herrington (2021)
   found the closest fits in two other runs (BAU2, CT), not the original
   standard run. Turchin's 2010 forecast of instability by 2020 is read as
   a hit, but the assessment is by the authors and the call is
   low-resolution. Neither predicts specific events, and none of these is
   a test of the predicted turning points, which lie in the future.
4. **A formal bound exists on control.** Ashby: a regulator needs variety at
   least matching the disturbances; mechanism design adds impossibility
   results (Gibbard-Satterthwaite, Myerson-Satterthwaite).
5. **Famous positive results are contingent.** Tit for Tat's tournament
   victory depends on format, criterion and payoffs (Rapoport et al. 2015).
6. **Doctrine is untested.** Reflexive-control claims rest on historical
   anecdote.

Working implication for the algebra: aim at structure and conditional
statements ("given these operators, these outcomes are reachable or
unreachable"), not point prediction.

## Unconfirmed

Resolved by the validation pass (now in the body): Ashby's wording ("only
variety can destroy variety", p. 207); Medina 2011 MIT Press; Lefebvre's
decision equation and alliance/conflict mapping (from Tarasenko's full
text, not Lefebvre's); *Algebra of Conscience* publisher (D. Reidel 1982);
Turchin's 2008 *Nature* essay (exists); Cyert & March publisher
(Prentice-Hall) and their concepts; nudge meta-analyses; Aumann-Drèze.
Donella Meadows, *Thinking in Systems: A Primer* (White River Junction, VT:
Chelsea Green, 2008) does exist; the original search failure was wrong.
It is a popular primer and adds nothing formal beyond Forrester.

Still open:

- Lefebvre's primary text (*Lectures*, 2010) was not read by anyone in this
  pass; the formalism is as relayed by Tarasenko, a direct collaborator.
- Which operation (sum or product) Lefebvre ties to which ethical system:
  Umpleby says the choice of combination rule generates the two systems but
  the mapping was not read in the primary source.
- Whether Lefebvre's non-decomposable graph is exactly the induced P4 (so
  decomposable = cograph): validator's inference, not from a source.
- Urban Dynamics' specific policy findings (low-income housing, property
  taxes): from Wikipedia's summary only.
- The Cybersyn figure of "about twenty factories" is Wikipedia's; Medina
  not read.
- Lanchester-type models applied to non-military groups; Nobel 2007
  advanced-information PDF (403).
- Several volume/page/DOI details added by the validator from memory are
  flagged inline as such.

## Clearly missing from this cluster

Checked against the sibling surveys (01-10, 14): Schelling, Granovetter
and structural balance (Heider; Cartwright and Harary) are covered
elsewhere. Not covered anywhere in `docs/prior-work/`:

- R. C. Conant and W. R. Ashby, "Every good regulator of a system must be a
  model of that system", *International Journal of Systems Science* 1(2):
  89-97 (1970). The good regulator theorem is the companion to requisite
  variety and bears directly on Lefebvre's point that operands must include
  a subject's model of others.
- Signed-graph balance as the obvious comparison for Lefebvre's
  alliance/conflict graph (covered in 01/05/06, but this file should cross-
  reference it: RGT's graph is a complete signed graph, read as a Boolean
  polynomial rather than tested for balance).
- Batchelder and Lefebvre, "A mathematical analysis of a natural class of
  partitions of a graph", *Journal of Mathematical Psychology* 26: 124-148
  (1982): the graph theory under RGT's decomposability.

## Validation log (2026-10-29)

- Wiener 1950/1954 — ✓
- Ashby 1956 — ✎ quote is "only variety can destroy variety"; pages 206-208; Cybernetica pages added
- Ashby 1958 — ✓
- Beer 1972/1979/1985 — ✓
- Project Cybersyn facts — ✓ (Wikipedia re-checked: ~20 factories, only Cybernet used regularly, Oct 1972 strike)
- Medina 2011 — ✎ moved out of Unconfirmed; MIT Press 2011 confirmed
- Lefebvre, *Algebra of Conscience* — ✎ publisher (Reidel 1982, Kluwer 2001) and subtitle added
- Lefebvre, *Lectures on the Reflexive Games Theory* — ✎ added (Leaf & Oaks 2010); not read
- Lefebvre 1998 "Sketch" — ✓ (existence; text not read)
- Lefebvre RGT formalism — ✎ replaced abstract-level gloss with the actual formalism from Tarasenko arXiv:1011.3397 (alliance = conjunction, conflict = disjunction confirmed; canonical decision equation x = Ax + Bx̄, solvable iff A ⊇ B, solutions A ⊇ x ⊇ B; decomposability; folding via P^W = P + W̄)
- Lefebvre's two ethical systems — ✎ added (previously missing), from Umpleby 2016; operation-to-system mapping ?
- Thomas 2004 — ✓ citation; ✎ Komov list was truncated to four of eleven elements
- Tarasenko arXiv papers — ✓ (1011.3397 read; 1101.0820 title confirmed)
- Forrester, *Industrial Dynamics* — ✓ (publisher added)
- Forrester, *Urban Dynamics* — ✎ publisher was MIT Press, not Pegasus
- Forrester 1971 "Counterintuitive Behavior" — ✓
- Forrester, *World Dynamics* — ✎ 1971 Wright-Allen; "1968" is a confusion with *Principles of Systems*
- Meadows et al. 1972 — ✓
- Turner 2008 — ✎ variables broadened; full citation added
- "2014 Melbourne study" — ✎ is Turner himself, not independent; working paper
- Herrington "2020" — ✎ 2021 (online 2020); best fits were BAU2 and CT, not the standard run
- Cole et al. *Models of Doom* — ✎ added as the SPRU critique's citation
- March & Simon 1958 — ✓
- Cyert & March 1963 — ✎ publisher Prentice-Hall; book does contain simulation models; concepts confirmed
- Slack "conserved quantity" — ✎ overclaim corrected
- Nobel 2007 mechanism design — ✓
- Gibbard-Satterthwaite — ✎ stated precisely (onto ≥3 outcomes, strategy-proof ⇒ dictatorial); citations added
- Myerson-Satterthwaite — ✎ stated precisely (BIC + IR + budget balance + efficiency impossible); citation added
- Thaler & Sunstein 2008 — ✓
- House of Lords "precious little" — ✗ quote removed (not found); finding restated from report summaries
- Nudge meta-analyses — ✎ added Mertens 2022 and Maier 2022
- Epstein & Axtell 1996 — ✓
- Axelrod 1980, 1984, 1997 — ✓
- Rapoport, Seale & Colman 2015 — ✓ (11.0% vs 30.0% confirmed in the paper)
- Salganik, Dodds & Watts 2006 — ✓
- Salganik et al. 2020 (Fragile Families) — ✓; ✎ quoted abstract wording and benchmark added
- Turchin 2003, 2009, 2012 — ✓ (details added)
- Turchin 2010 *Nature* forecast — ✎ added
- Turchin 2008 "Arise 'cliodynamics'" — ✎ moved out of Unconfirmed; exists, *Nature* 454: 34-35
- Turchin & Korotayev 2020 — ✎ published in *PLoS ONE*, not only a preprint
- Lanchester 1916 / Osipov 1915 — ✓; ✎ equations stated; the survey described only the aimed-fire (square) case
- ANZIAM "never validated" — ✓ (quote confirmed; URL added)
- von Neumann-Morgenstern 1944, Shapley 1953 — ✓
- Gillies core — ✎ 1953 thesis / 1959 publication, not 1954
- Aumann & Drèze 1974 — ✎ moved out of Unconfirmed; exists
- Meadows, *Thinking in Systems* — ✎ exists (Chelsea Green 2008); survey's "nothing found" was wrong

**Verdict.** No fabricated works: every citation exists, and the
summaries are mostly faithful at the level of abstracts. The errors are
the kind that come from never opening a primary text: wrong dates and
publishers, truncated lists, loose theorem statements, and — the most
consequential — the Limits to Growth record presented as three
corroborating assessments when two are by the same author and the
independent one picked different scenarios. The Lefebvre section is now
grounded in a full collaborator paper rather than search snippets, and
the original's core claim (alliance = product, conflict = sum) turned out
to be right.

## Licences of quoted and transcribed material (2026-10-30)

- Wiener, *The Human Use of Human Beings* (1950), 18-word quotation in §1:
  publisher copyright (book); wording actually taken from the Wikipedia
  article (CC BY-SA 4.0). Short quotation, kept; to be confirmed against the book.
- Ashby, *An Introduction to Cybernetics* (1956) and 1958 *Cybernetica* paper:
  publisher copyright, not determined; one 4-word quotation ("only variety
  can destroy variety") and a restated equation. Equations restated, not copied.
- Wikipedia articles (Variety (cybernetics), Viable system model, Project
  Cybersyn, Urban Dynamics, Mechanism design, Nudge (book), Sugarscape,
  Cliodynamics, Lanchester's laws): CC BY-SA 4.0. Used as paraphrased
  facts and short wording, attributed in the "Verified at" lines; the
  Nudge definition (§8) and Lanchester prose (§13a) are marked for a check
  of retained wording.
- Thomas (2004), Taylor & Francis: publisher copyright presumed. The list of
  eleven reflexive-control elements in §4 was recalled from memory and is
  retained pending a check against the paper (or reduction to a description).
- Thaler & Sunstein, *Nudge* (Yale UP, 2008): publisher copyright; definition
  restated in our words, no quotation.
- House of Lords Science and Technology Committee, *Behaviour Change* (2011):
  parliamentary publication, licence not checked; finding paraphrased, the
  unverified quotation removed.
- ANZIAM Journal paper on Lanchester models: not determined; publisher
  copyright presumed; one short quotation (under 20 words).
- Salganik et al. (2020, PNAS), Fragile Families abstract: PNAS articles are
  open access under CC BY-NC-ND/CC BY; not determined for this article; one
  short quotation (under 30 words).
- All other works (Forrester, Meadows et al., Simon, Hurwicz/Maskin/Myerson,
  Epstein & Axtell, Axelrod, Rapoport et al., Salganik et al. 2006, Turchin,
  Lanchester, Osipov, von Neumann-Morgenstern, Shapley, Gillies, Aumann &
  Drèze, Conant & Ashby, Batchelder & Lefebvre): not determined; publisher
  copyright presumed; cited only, with facts and numbers restated.
