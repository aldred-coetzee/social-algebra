# Prior work 39: deterrence, coercion and fear as instruments between groups

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: the strategic use of drives (fear, resolve, honour) by and against groups and states. Aim (Aldred): "an algebra which expresses basic human drives and group drives, which we can compose into equations... theorems... control or predict behavior."

**Cross-references, not repeated.** 07 (reflexive control, Lanchester: the control-theory side of manipulating an opponent's decision), 11 (Kautilya, Sun Tzu, Clausewitz: the pre-formal inventory of coercive moves), 24 (cohesion, collective action: the unit-level motive that "will to fight" below builds on), 13 (coercion in families and persuasion), 21 (psychological games and reciprocity), 17/18 (fear itself; collective emotion), 28 (ecology of fear: predation risk as the biological analogue of a deterrent threat).

**Method and honesty note.** What was **[read]** at source this session: Kydd & Walter 2006 (full text PDF from the Belfer Center), Spiller 1988 (PDF, text extracted; read the sections on Marshall's interview claims). Everything else is **[from abstract/standard account]**: search summaries or my background knowledge, with no primary text opened. Equations written from standard accounts are the field's textbook forms; check against the primary before building on them. The Crossref check passed for every DOI listed; books without a DOI are marked "no DOI checked". WebFetch of the Rand page and the Fearon 1995 PDF failed (403 / network), so the Fearon 1995 content is secondary. In validation (2026-10-29) the RAND RR-2341 PDF was read via the Internet Archive, Kydd & Walter's Figure 1 and Spiller were re-checked at source, and every DOI was re-resolved; see the log at the end.

## Summary

1. **This is the first cluster where the drives are used as instruments, and it has real theorems.** Deterrence and bargaining theory are formal: threats, resolve, fear and honour appear as payoffs, types and beliefs, and the results are equilibrium theorems (existence conditions, comparative statics). The price is that the underlying "drive" is a *payoff or a type* (a number in a utility function or a private variable), fixed for the duration of the game. What *does* move over time in this literature is the **belief** about resolve and the **accumulated cost or risk**: war-of-attrition crisis models (Fearon 1994, with audience costs rising as the crisis lasts; Powell's brinkmanship, where holding firm raises the risk of disaster) and the learning-while-fighting models (Wagner 2000, Filson & Werner 2002, Slantchev 2003, Powell 2004, Smith & Stam 2004) are dynamic in exactly that sense. No model found here lets the drive *itself* rise and decay under actions. (Validation correction: the first draft said resolve was never dynamic, which overstated the gap.)
2. **A typed operator set exists and is the best find: Kydd & Walter's five strategies.** Attrition, intimidation, provocation, spoiling and outbidding are placed on two coordinates: *what the audience is uncertain about* (power, resolve, trustworthiness) crossed with *who the audience is* (enemy government, own population). All six cells are filled; attrition spans two (power and resolve, aimed at the enemy). That is a genuine operator signature, `[read]` (Figure 1 of the paper, checked in validation).
3. **Resolve is the central "drive" operand, and it is mostly a private type.** Audience costs, brinkmanship, perfect deterrence and outbidding all reduce to: an agent has a hidden resolve; actions are costly signals of it; others update. This is the same object as the Bayesian type in file 21, now with a body of strategic results.
4. **The empirical record is split sharply by method.** Formal results are sound as mathematics; the empirical support for the behavioural predictions (audience costs, prospect-theory in crises, morale ratios) is contested, and one famous number (Marshall's 15-25% firing rate) rests on data that probably did not exist.
5. **What is missing is exactly what the aim needs:** a fear/resolve variable that is itself a dynamic state (not just a fixed type with evolving beliefs about it), and a way to compose deterrent, compellent and signalling acts in one equation. The pieces are rigorous but isolated games.

---

## 1. Schelling: strategy of conflict, deterrence versus compellence, threats that leave something to chance

**Citations.** Schelling, T. C. (1960). *The Strategy of Conflict*. Harvard University Press. Schelling, T. C. (1966). *Arms and Influence*. Yale University Press. No DOI checked (books).

**Their vocabulary.** Commitment, credibility, focal point, "threat that leaves something to chance", deterrence ("keep someone from doing something"), compellence ("make someone do something"), "the power to hurt", brinkmanship as "manipulation of shared risk", salami tactics. `[standard account]`

**Drives/operands.** Players with preferences in a mixed-motive game; fear is not a drive but the expected disutility of the threatened punishment. Resolve appears as the willingness to carry out; it is made credible by *commitment*, i.e. by shrinking one's own options (burning bridges, the tripwire). `[standard account]`

**Operators / equations.** No equations in the sense of this survey: Schelling's contribution is a vocabulary of *moves*: threat, promise, commitment, tripwire, hostage, limited-retaliation, "threat that leaves something to chance" (a threat whose execution is probabilistic and not wholly under the threatener's control). Distinguished: deterrence is passive and open-ended in time; compellence is active and needs a deadline; compellence tends to be harder because the target must visibly yield. `[standard account]` The threat-leaves-something-to-chance idea is the ancestor of Powell's formal brinkmanship (section 3).

**Theorems.** None in the text; later work formalised pieces (the paradox that irrationality or lost control can *raise* credibility: a rational actor cannot credibly commit to an irrational retaliation, so the threat must be made by a mechanism, not a choice). `[standard account]`

**Empirical standing.** Foundational and widely taught; its predictions were not tested as a unit. Specific claims (compellence harder than deterrence) have mixed evidence; see Pape and Byman & Waxman (section 6a). Be blunt: it is a typology of moves with strong intuition and almost no quantitative content.

**Translation.** *Operators: Deter(a,b,x), Compel(a,b,x), Commit(a), Escalate-risk(a)*. Each takes an action x of the target and a cost the issuer can impose. The "something left to chance" operator is a *probabilistic* operator on a shared state, which is a natural non-deterministic element of an algebra.

---

## 2. Kahn: escalation ladder

**Citation.** Kahn, H. (1965). *On Escalation: Metaphors and Scenarios*. Praeger. No DOI checked. `[standard account]`

**Vocabulary.** 44 rungs in seven groups separated by thresholds, from "subcrisis manoeuvring" (rung 1, "Ostensible Crisis") through traditional, intense and bizarre crises to exemplary, military and civilian central wars (the count and grouping is the common textbook description; wording may follow Wikipedia's article on the escalation ladder, CC BY-SA 4.0, source not confirmed, re-derive from Kahn 1965 directly). Thresholds ("firebreaks") between groups.

**Structure.** An ordered set of states with transitions that raise the cost and the risk; the claim is that both sides move along a *shared* ladder and that credible control means the ability to stop at a rung. No equations. It is an ordinal scale of coercive intensity, a total (partial-order-free) ordering that gives a ready sort for an "intensity" attribute on acts.

**Empirical standing.** Illustrative, not tested; later quantitative escalation scales (e.g. event-data scales like COW/MID hostility levels) are the empirical descendants. Not verified here.

**Translation.** A *state variable* with a discrete ordered range and a set of operators that move up and down it. If the algebra wants an ordinal level for "how coercive is the current relation", this is the precedent.

---

## 3. Powell: nuclear deterrence and brinkmanship as a formal game

**Citation.** Powell, R. (1990). *Nuclear Deterrence Theory: The Search for Credibility*. Cambridge University Press. doi:10.1017/CBO9780511551598, confirmed via Crossref (title there: "Nuclear Deterrence Theory"). Powell, R. (1988). "Nuclear brinkmanship with two-sided incomplete information." *APSR* 82(1): 155-178, doi:10.2307/1958063, confirmed via Crossref (it is *earlier* than the book, not later as the draft said). Powell, R. (2015). "Nuclear brinkmanship, limited war, and military power." *International Organization* 69(3): 589-626 `[from abstract]`.

**Vocabulary.** Risk of mutual destruction as an *exogenous probability of losing control* in each period of a crisis; "contest of nerves"; "balance of resolve"; the "credibility problem" (a rational leader will not carry out a suicidal retaliation). `[from abstract/standard account]`

**Drives/operands.** Two players; each has a *cost of conflict* (resolve) which is private; a state variable, the probability that the crisis ends in disaster, rises as players hold out. Resolve is the drive-like variable; it is a number, with a distribution over types. `[from abstract]`

**Operators / equations.** The model is a sequential game (a war of attrition in risk): each period each side chooses to back down or hold; holding raises the shared risk of catastrophe. Equilibrium: each player has a resolve threshold; the one whose cost of conflict is lower holds out longer. The exact payoffs and equilibrium strategies are **not stated here** because they were not read. `[from abstract]`

**Theorems or derived predictions.** Powell (2015) `[from abstract]`: the more likely the balance of resolve is to favour the defender, the less military power the challenger brings to bear; and a formal stability-instability paradox, in which a less stable balance makes high-intensity conflict less likely but lower-level conflict more likely. The draft's further claim that a player may be less likely to prevail the more resolve it has was not found in any abstract checked and is moved to Unconfirmed.

**Empirical standing.** The brinkmanship models are theory, tested only by case study. Related formal work: Kenkel & Schram (2024), "Uncertainty in crisis bargaining with multiple policy options," *AJPS* 69: 194-209, doi:10.1111/ajps.12849 (confirmed via Crossref), find `[from abstract]` that when actors can also use low-level costly options (sanctions, strikes), *greater* private willingness to fight can go with a *lower* probability of war or a worse settlement. (Validation correction: the draft had this paper saying the reverse, that more resolved actors take more risk and do better.)

**Translation.** *Operand: agent with private resolve r and a shared risk state p.* *Operator: Hold = (raise p by δ, reveal that r exceeds the current threshold); Back-down = terminate with a loss.* This is the closest in the cluster to a drive-dynamics equation: a "resolve" threshold crossed by a rising shared hazard. Time and hazard are explicit, and the accumulated risk is endogenous (it rises because players choose to hold), even though the per-step hazard is a parameter.

---

## 4. Perfect deterrence theory (Zagare & Kilgour)

**Citations.** Zagare, F. C. & Kilgour, D. M. (2000). *Perfect Deterrence*. Cambridge University Press. doi:10.1017/cbo9780511491788, confirmed via Crossref. Zagare & Kilgour (1993). "Asymmetric deterrence." *International Studies Quarterly* 37: 1-27, doi:10.2307/2600829, confirmed via Crossref.

**Vocabulary.** *Capability* and *credibility* as the two components of a threat; "Perfect Deterrence Equilibrium", "Sure-Thing Deterrence Equilibrium", attack and bluff equilibria; unilateral and mutual direct deterrence, extended deterrence. `[from abstract/search]`

**Drives/operands.** Players with ordinal payoffs over outcomes (Status Quo, Conflict, Capitulation, etc.), possibly with incomplete information about the other's type. The "drive" is the preference ranking: a *credible* threat is one whose execution the threatener prefers, i.e. a payoff condition, not a psychological state. `[from search]`

**Operators / equations.** Games in extensive form with subgame-perfect equilibria. The existence conditions are inequalities on ordinal payoffs (the challenger's utility for the status quo against conflict, and the defender's utility for retaliating). I could not retrieve the statement of the conditions; **not stated here**. `[from abstract]`

**Theorems.** Yes, in the formal sense. From the book's table of contents (Cambridge sample PDF, checked in validation): *capability is a necessary condition* for deterrence (ch. 10.1), and the theory rests on a "credibility principle" (threats must be ones the threatener would rationally carry out). Reported by the publisher: classical deterrence's deterministic threats require commitment to irrational acts, and when all-out war is the worst outcome for both, mutual deterrence is *unlikely* (the paradox the book sets out to resolve); credible threats to respond can sometimes make an attack more likely and incredible threats can sometimes promote peace (the "deterrence paradoxes"). The book's central results are existence theorems for the deterrence equilibria under stated payoff orderings. `[from abstract]`

**Empirical standing.** The authors present case applications (Cuban missile crisis, Arab-Israeli, Korea). Case-based support; no systematic statistical test I found. The theory's *form* is the strongest part: it makes "is deterrence stable?" a decidable condition on payoffs.

**Translation.** *Operand: a 2-player game form with a payoff ordering.* The theory gives a **stability predicate**: given orderings, does the status quo hold. In the algebra, that is a *theorem-bearing relation on a pair of agents*, the nearest model to "predict whether deterrence holds". It treats credibility as a derived property, not a primitive: a clean separation worth keeping.

---

## 5. Audience costs and resolve signalling (Fearon 1994 and the dispute)

**Citations.** Fearon, J. D. (1994). "Domestic political audiences and the escalation of international disputes." *APSR* 88(3): 577-592, doi:10.2307/2944796, confirmed via Crossref. Weeks, J. L. (2008). "Autocratic audience costs: regime type and signaling resolve." *International Organization* 62(1): 35-64, doi:10.1017/s0020818308080028. Tomz, M. (2007). "Domestic audience costs in international relations: an experimental approach." *International Organization* 61(4): 821-840, doi:10.1017/s0020818307070282. Snyder, J. & Borghard, E. (2011). "The cost of empty threats: a penny, not a pound." *APSR* 105(3): 437-456, doi:10.1017/s000305541100027x. Kertzer, J. & Brutger, R. (2016). "Decomposing audience costs: bringing the audience back into audience cost theory." *AJPS* 60(1): 234-249, doi:10.1111/ajps.12201. Trager, R. (2015). "Diplomatic signaling among multiple states." *Journal of Politics* 77(3): 635-647, doi:10.1086/681259. Slantchev, B. (2005). "Military coercion in interstate crises." *APSR* 99(4): 533-547, doi:10.1017/s0003055405051865. Slantchev, B. (2006). "Politicians, the media, and domestic audience costs." *ISQ* 50: 445-477, doi:10.1111/j.1468-2478.2006.00409.x. Fearon, J. D. (1997). "Signaling foreign policy interests: tying hands versus sinking costs." *Journal of Conflict Resolution* 41(1): 68-90, doi:10.1177/0022002797041001004. Trachtenberg, M. (2012). "Audience costs: an historical analysis." *Security Studies* 21: 3-42, doi:10.1080/09636412.2012.650590; Slantchev (2012) "Audience cost theory and its audiences," *Security Studies* 21: 376-382, doi:10.1080/09636412.2012.706476. All DOIs confirmed via Crossref in validation (Kertzer-Brutger print year 2016 per Crossref).

**Vocabulary.** *Audience cost* (a leader's domestic penalty for making a threat and then backing down), *tying hands* versus *sinking costs* (Fearon 1997), resolve, escalation, "costly signal". `[from abstract/standard account]`

**Drives/operands.** Two states; each leader has a private cost or value for the issue (resolve) and a domestic audience that will punish a retreat after a public threat. Fear in the audience (of being led by a bluffer) is modelled as a *penalty* on the leader, not as an emotion. `[from abstract]`

**Operators / equations.** Fearon's game is a **continuous-time political war of attrition**: at each moment each leader chooses to attack, back down or keep escalating, with private information about its value for war versus settlement; a leader who backs down pays an audience cost that **increases with the length of the public confrontation**, a(t) rising in t. Holding on is therefore a costly signal whose price grows over time, and the opponent updates its belief about resolve as the crisis continues. Closed-form equilibrium not read. `[from abstract]`

**Theorems.** `[from abstract]` Once a crisis is under way, observable capabilities and interests have no direct effect on who backs down (they are priced in at the start); the side able to generate larger audience costs (e.g. a democracy) is always less likely to back down. (Validation correction: the draft described a discrete escalate/back-down sequence with a fixed cost a and claimed a result about "fewer disputes ending in war", which is not in the abstract; the rising-cost attrition structure was missing.) Critique: the model assumes the audience cost rather than deriving it, and the inference that democracies are "more credible" rests on unmodelled links between regime type and cost size; Slantchev (2006) is the paper that tries to derive audience costs (from media and electoral accountability). The draft attributed the critique to Slantchev 2005, which is about military moves as signals that both sink costs and tie hands.

**Empirical standing.** Contested; be blunt.
- Tomz (2007) survey experiments (US, UK) show that respondents penalise leaders who threaten and then back down: audience cost *attitudes* exist. `[from standard account]`
- Weeks (2008) argues some autocracies also face costs; the democracy-only claim is weakened.
- Snyder & Borghard (2011), whose title is the source of "a penny, not a pound" (confirmed via Crossref), find that leaders rarely invoke audience costs in real crises and that the effect is small. Trachtenberg's historical analysis (2012) is similarly sceptical; Slantchev's (2012) reply in the same journal disputes it. `[from search]`
- Kertzer & Brutger decompose the effect and find *inconsistency* costs differ from *belief* costs.
Net: the *attitude* is real in surveys; its effect on actual crisis outcomes is unproven.

**Translation.** *Operator: PublicThreat(a, b, x) creates a binding cost on a with respect to an audience Z; Retreat(a) then pays that cost.* This is a genuine **three-party operator** (leader, adversary, audience), which most of the earlier survey's dyadic operators lack. The audience is itself a group operand holding a punishment disposition.

---

## 6. Bargaining model of war and its causes (Fearon 1995, Powell 2006)

**Citations.** Fearon, J. D. (1995). "Rationalist explanations for war." *International Organization* 49(3): 379-414, doi:10.1017/s0020818300033324, confirmed via Crossref. Powell, R. (2006). "War as a commitment problem." *International Organization* 60, doi:10.1017/s0020818306060061, confirmed via Crossref.

**Vocabulary.** Bargaining range, costly war, private information and incentives to misrepresent, commitment problems (including preventive war and first-strike advantage), issue indivisibility. `[from abstract/standard account]`

**Operators / equations (textbook form, `[standard account]`; not read).** Two states A, B dispute a good normalised to 1. War is a lottery: A wins with probability p, and each side pays a cost of war, c_A and c_B, both positive. Expected war payoffs: A gets p - c_A; B gets (1 - p) - c_B. Any settlement x to A with p - c_A < x < p + c_B (the *bargaining range*, of width c_A + c_B) is preferred by both to war. So with complete information and perfect commitment, war is inefficient and should not happen.

**Theorems / derived predictions.** The "Fearon theorem" is a *no-go result*: war occurs only if the standard conditions fail. Three failure modes: (1) **private information with incentives to misrepresent** (both sides want to appear strong, so cheap talk fails, and bargaining gives each a reason to bluff, risking war), (2) **commitment problems** (a rising power cannot credibly promise not to renege on a bargain when its power grows; a first-strike advantage causes a preventive-war incentive), (3) **indivisibility** (Fearon himself finds this the weakest explanation, since issues can usually be linked). Powell (2006) strengthens (2): shifts in power with imperfect commitment make war a rational choice even under complete information. `[from abstract/search]`

**Dynamic extensions: bargaining and learning while fighting (added in validation, `[from abstract/standard account]`).** War is modelled as a sequence of battles during which offers continue; each battle's outcome reveals information about relative power or resolve, beliefs update, and war ends when beliefs converge enough for a settlement. Wagner, R. H. (2000). "Bargaining and war." *AJPS* 44: 469-484, doi:10.2307/2669259. Filson, W. & Werner, S. (2002). "A bargaining model of war and peace: anticipating the onset, duration, and outcome of war." *AJPS* 46: 819-837, doi:10.2307/3088436. Slantchev, B. (2003). "The principle of convergence in wartime negotiations." *APSR* 97: 621-632, doi:10.1017/s0003055403000911. Powell, R. (2004). "Bargaining and learning while fighting." *AJPS* 48(2): 344-361, doi:10.1111/j.0092-5853.2004.00074.x. Smith, A. & Stam, A. (2004). "Bargaining and the nature of war." *JCR* 48: 783-813, doi:10.1177/0022002704268026. Langlois, C. & Langlois, J.-P. (2009). "Does attrition behavior help explain the duration of interstate wars?" *ISQ* 53: 1051-1073, doi:10.1111/j.1468-2478.2009.00568.x. All DOIs confirmed via Crossref. These are the field's answer to "is resolve dynamic?": the type is fixed but the belief about it, and the war's accumulated cost, evolve.

**Empirical standing.** Direct tests are few. One experimental study found by search (not identified; possibly Quek's lab experiments) reports that the commitment problem sharply increases the incidence of conflict in the lab, while private information with shifting power has no significant effect there; unconfirmed. The theory is regarded as the organising framework of formal IR, but its mechanisms are hard to separate in field data, so "which of the three" is usually argued by case, not estimated.

**Translation.** This is the most reusable **theoretical skeleton**: two agents, a prize, war-as-lottery with costs, and a settlement set. In the algebra, an interaction is a *bargaining* that has a **feasible set** and a three-way taxonomy of how it fails. The failure taxonomy (information, commitment, indivisibility) is a ready-made classification of why an operator application does not reach its fixed point.

---

## 6a. Coercion theory: punishment versus denial (Pape; Byman & Waxman) — added in validation

**Citations.** Pape, R. A. (1996). *Bombing to Win: Air Power and Coercion in War*. Cornell University Press (Crossref has the 2019 Cornell open-access re-issue, doi:10.7591/9780801471513). Byman, D. & Waxman, M. (2002). *The Dynamics of Coercion: American Foreign Policy and the Limits of Military Might*. Cambridge University Press (RAND Studies in Policy Analysis; RAND CB400); no DOI found, existence confirmed via publisher and catalogue records. Related: Byman & Waxman (2000), "Kosovo and the great air power debate," *International Security* 24(4): 5-38, doi:10.1162/016228800560291 (Crossref).

**Content `[from search/standard account]`.** Pape sorts coercive air strategies into four: **punishment** (raise civilian costs), **risk** (Schelling's gradually escalating punishment), **decapitation** (strike leadership) and **denial** (make the target's military strategy fail). Across cases from the Spanish Civil War to Desert Storm he finds punishment rarely if ever coerces and denial is what works when coercion works at all ("Denial can work, but strategic bombing is not the best way to achieve it"). Byman & Waxman argue against the success/failure dichotomy and against Pape's single-mechanism view: coercion is a *dynamic* contest in which the adversary counter-coerces, and its outcome is shaped by escalation dominance, coalition and domestic constraints, and the target's ability to neutralise threats.

**Translation.** Two operators distinguished by *what they act on*: Punish(a,b) lowers b's payoff from continuing; Deny(a,b) lowers b's probability of success. In the bargaining frame of section 6, punishment moves c_B and denial moves p. That is the cleanest mapping in the cluster from a coercive act onto a parameter of the base model.

---

## 7. Terrorism as strategic fear production (Kydd & Walter)

**Citations.** Kydd, A. & Walter, B. (2006). "The strategies of terrorism." *International Security* 31(1): 49-80, doi:10.1162/isec.2006.31.1.49, confirmed via Crossref, **[read]** (full text). Kydd, A. & Walter, B. (2002). "Sabotaging the peace: the politics of extremist violence." *International Organization* 56(2), doi:10.1162/002081802320005487, confirmed via Crossref `[from abstract]`. Related: Pape, R. A. (2003). "The strategic logic of suicide terrorism." *APSR* 97(3), doi:10.1017/S000305540300073X, confirmed via Crossref in validation.

**Their vocabulary `[read]`.** "Costly signaling"; "cheap talk is insufficient"; three subjects of uncertainty (power, resolve, trustworthiness) and two targets of persuasion (the enemy government, the domestic population); "zealots versus sellouts".

**Drives/operands `[read]`.** Terrorist group (a weak actor), a target government, the group's own population, rival groups. The core claim: "terrorist violence is a form of costly signaling. Terrorists are too weak to impose their will directly by force of arms." Attacks are costly to bluffers and so reveal type.

**Operators (the typed set) `[read]`.**

Mapping per the paper's Figure 1 (re-checked against the PDF in validation; the draft had provocation's audience and uncertainty wrong):

| Strategy | Target of persuasion | Subject of uncertainty | What the audience is made to believe |
|---|---|---|---|
| Attrition | enemy | power **and** resolve (spans two cells) | the group is strong and resolute enough to impose considerable costs if a policy continues |
| Intimidation | own population | power | the group can punish disobedience and the government is too weak to stop it |
| Outbidding | own population | resolve | this group has greater resolve to fight the enemy than rivals ("zealots" versus "sellouts") |
| Spoiling | enemy | trustworthiness | moderates on the group's own side are weak and untrustworthy, undermining a peace deal |
| Provocation | own population | trustworthiness (of the enemy government) | goaded into indiscriminate retaliation, the government reveals itself as so "evil" that the group's radical goals are justified |

Provocation acts *through* the enemy (it must be induced to retaliate) but the audience being persuaded is the group's own population.

The conditions for each are given qualitatively in the paper: attrition is cheaper against democracies and for groups able to bear retaliation; provocation needs a government capable of middling brutality (a genocidal government makes it fail); spoiling is best countered by trust-building and third-party enforcement; outbidding requires two or more rival parties and a population that cannot tell zealots from sellouts. `[read]`

**Theorems or derived predictions.** The paper contains no formal proofs; it is a typology with stated scope conditions and some case support (Hamas/Fatah, Algeria, Israel-Palestine). Responses are matched per strategy: the best response to attrition is not the best response to outbidding. `[read]`

**Empirical standing.** Used widely as an organising framework; Bloom's (2005) outbidding work and later quantitative tests are mixed (outbidding in particular has been disputed in cross-national tests, not verified here). The paper itself offers case illustrations, not statistical tests.

**Translation.** *Direct operator candidates.* Each strategy is an operator `T_s(g, a1, a2)` from a weak group g onto audience a2, with an effect on a2's belief about g's *power/resolve/trustworthiness*. The signature (uncertainty-type × audience-type) is a **3 x 2 grid with every cell filled**: attrition covers both enemy cells for power and resolve, and the other four strategies take one cell each. (Validation correction: the draft said five of six cells were filled and called power-to-own-population the empty cell; that cell is intimidation.) The interesting algebraic fact is the reverse: one operator (attrition) is not cell-specific, i.e. the enemy is not asked to distinguish power from resolve. The paper notes the list is not exhaustive (it omits advertising and retaliation, footnote 30). This is the clearest example in the survey of "operators on beliefs about drives".

---

## 8. Psychology of threat perception (Jervis) and the security dilemma

**Citations.** Jervis, R. (1968). "Hypotheses on misperception." *World Politics* 20(3): 454-479, doi:10.2307/2009777, confirmed via Crossref. Jervis, R. (1976). *Perception and Misperception in International Politics*. Princeton University Press (no DOI checked). Jervis, R. (1978). "Cooperation under the security dilemma." *World Politics* 30(2): 167-214, doi:10.2307/2009958, confirmed via Crossref in validation.

**Vocabulary `[standard account]`.** Security dilemma (one state's defensive measures look offensive to another and trigger an arms race), spiral model versus deterrence model, offence-defence balance, cognitive consistency, "the inherent bad faith model", the tendency to see the other's behaviour as more centrally planned than one's own.

**Drives/operands.** States as perceivers; fear arises from *inferred intent* under uncertainty. The key operand is *perceived intent* of the other; the key operator is *signal interpretation* with biased priors.

**Operators / equations.** Verbal. The 1978 article (read in no part here) formalises the security dilemma as a 2×2 game (cooperate/defect on armament) together with two variables: whether offence or defence has the advantage, and whether offensive and defensive postures can be distinguished. Four "worlds" follow. `[standard account]`

**Theorems.** None. The four-world classification is a case analysis: the dilemma is worst when offence is favoured and postures are indistinguishable, and weakest when defence is favoured and distinguishable.

**Empirical standing.** The perception findings (confirmation bias, assimilation to prior beliefs) are consistent with general psychology; the spiral-versus-deterrence contrast is influential but its tests are mostly historical cases. Rational-choice theorists have shown that the security dilemma and spirals can arise from rational behaviour without misperception (Kydd 1997 "Game theory and the spiral model", *World Politics*, and Kydd 2005 *Trust and Mistrust in International Relations*; Glaser 1997 "The security dilemma revisited"; `[standard account]`, not checked), which weakens Jervis's psychological necessity.

**Translation.** *An operator on a pair's mutual perceived-intent state*: Arm(a) raises a's capability and, depending on a parameter pair (offence-defence, distinguishability), raises or does not raise b's fear of a. The two-parameter taxonomy is a compact **parameterisation of when fear spirals**, a candidate for a dynamical system: fear_b' = f(a's observed capability, a parameter).

---

## 9. Prospect theory in international relations (Levy, McDermott)

**Citations.** Levy, J. S. (1992). "Prospect theory and international relations: theoretical applications and analytical problems." *Political Psychology* 13(2): 283-310, doi:10.2307/3791682, confirmed via Crossref. McDermott, R. (2004). "Prospect theory in political science: gains and losses from the first decade." *Political Psychology* 25(2): 289-312, doi:10.1111/j.1467-9221.2004.00372.x, confirmed via Crossref. Foundation: Kahneman & Tversky (1979), see file 16 and others.

**Vocabulary.** Reference point, domain of losses versus gains, loss aversion, framing, risk-seeking in losses. `[from abstract/standard account]`

**Equations (standard, `[standard account]`).** Value function v(x) = x^a for x >= 0, v(x) = -lambda (-x)^b for x < 0, with lambda about 2.25, a, b about 0.88 (Tversky and Kahneman 1992 estimates, not re-checked here). Weighted probability function pi(p). Decisions maximise sum of pi(p_i)v(x_i).

**Theorems / derived predictions.** Leaders who see themselves in a domain of losses (relative to a reference point) are predicted to accept more risk, including escalation, to avoid a certain loss; those in the domain of gains are risk-averse, so status-quo powers are cautious and revisionists in decline are dangerous. Levy identifies the key difficulty: the reference point is not given by the theory and can be set by the status quo, an aspiration, or an expectation, so predictions depend on how the analyst chooses it. `[from abstract]`

**Empirical standing.** Lab evidence for loss aversion is strong but with mixed replication of the *framing effect* sizes and a debate about the size of lambda; the IR applications are mostly retrospective case readings, and the reference-point problem makes them hard to falsify. McDermott's review (a decade of applications) acknowledges this. Be blunt: elegant, with a free parameter (the reference point) that absorbs the evidence.

**Translation.** This gives a **loss-framed fear operator**: a state's risk attitude is a function of the *sign of its position relative to a reference*. In the algebra, that means a fear/risk drive that is not a scalar but depends on a *reference state*: a binary regime switch (gain/loss) with a continuous value function.

---

## 10. Morale and will to fight (RAND)

**Citations.** Connable, B., McNerney, M. J. & Marcellino, W. et al. (2018). *Will to Fight: Analyzing, Modeling, and Simulating the Will to Fight of Military Units*. RAND RR-2341, doi:10.7249/RR2341, confirmed via Crossref (authors listed as Connable, McNerney, Marcellino). McNerney, M. J., Connable, B., Zimmerman, S. R. et al. (2018). *National Will to Fight: Why Some States Keep Fighting and Others Don't*. RAND RR-2477, doi:10.7249/RR2477, confirmed via Crossref. The user's brief said "2018/2019"; Crossref gives 2018 for both.

**Vocabulary `[read]` (RR-2341 PDF via the Internet Archive, read in validation).** Will to fight is "the disposition and decision to fight, to act, or to persevere when needed" (the draft's "to keep fighting, and to win" wording is not the report's definition). Five levels (individual, unit, organization, state, society); three categories (motivations, capabilities, culture); 29 factors and 61 subfactors, each rated for *durability* (low/mid/high). The companion national model (RR-2477) has 15 variables `[from search]`.

**The 29 factors `[read]`, Table S.1 (described, not transcribed).** The table in the report's summary lists the 29 factors by level and category; see RR-2341 Table S.1 for the full list. The counts are individual 7, unit 7, organization 7, state 5, society 3, split between motivations, capabilities and culture. The factors the algebra needs here are unit cohesion (social vertical, social horizontal, task), unit control, desperation, and leadership at each level.

**Drives/operands.** A *factor model*, not an equation. The central finding `[read]`: "unitary theories of will to fight [are] unreliable"; cohesion and morale "are no more or less important than any other factor in the general model". (The draft's quoted sentence was a paraphrase from a summary, not the report's words.)

**Operators / equations `[read]`.** Explicitly none, and explicitly *not additive*: "Will to fight should never be considered simply as a sum, average, or weighted average of the factors"; a single factor (e.g. desperation rated 5, leadership rated 1) can override all others. The report recommends including will to fight in war games and simulations.

**Theorems.** None.

**Empirical standing.** Based on literature review, interviews and 14 coded war cases from World War I onward (findings drawn from 10 of them) `[read]`; not a validated predictive model. The reports are policy-grade synthesis. An observation useful for the algebra: the report's central finding is a *negative* one against single-factor (cohesion) models, relevant to file 24.

**Translation.** *Operand: unit with a vector of factors across five nested levels.* The nesting individual-unit-organisation-state-society is a ready **hierarchy of operands** for the algebra, with each level a different group-size sort. The composition rule is the missing part, and it is the part the algebra would have to supply; the report's own constraint is that it must be non-additive, with veto-like factors (closer to a min or a weakest-link rule than a weighted sum).

---

## 11. Fear of combat: Marshall's ratio of fire, Grossman, and the debunking

**Citations.** Marshall, S. L. A. (1947). *Men Against Fire: The Problem of Battle Command in Future War*. Infantry Journal/Morrow (no DOI checked). Spiller, R. J. (1988). "S.L.A. Marshall and the ratio of fire." *RUSI Journal* 133(4), pp. 63-71, doi:10.1080/03071848808445332 (confirmed via Crossref in validation). `[read]` (PDF, from a copy hosted at gwern.net; re-read in validation). Grossman, D. (1995). *On Killing: The Psychological Cost of Learning to Kill in War and Society*. Little, Brown (no DOI checked).

**Marshall's claim `[read, via Spiller]`.** From interviews with rifle companies fresh from combat, Marshall concluded that only one soldier in four fired his weapon while in contact with the enemy (Spiller's paraphrase); Marshall's own words: in an average experienced company "the number engaging with any and all weapons was approximately 15 per cent", rarely above 25 per cent even in the most aggressive companies. Spiller records that after a tour in Korea Marshall reported to the Secretary of the Army in April 1951 that the ratio "had risen beyond 55 per cent both in night defense and daytime attack". (Validation correction: the draft placed the 55% in "some night actions per Marshall's later preface".)

**The debunking `[read]`.**
- Marshall claimed to have interviewed "approximately" 400 infantry rifle companies; that number "tended to change over the years": 603 in 1952, "something over 500" five years later.
- On Marshall's own method (two to three days per company's one day of combat), the most generous calculation would have finished about 400 interviews around October-November 1946, about when he was writing the book.
- John Westover, who attended the interviews, does not recall Marshall ever asking who had fired; nor ever talking about weapon-use ratios. Marshall's surviving field notebooks show no statistical compilations. Spiller's conclusion: the "systematic collection of data" that made the ratio authoritative "appears to have been an invention".
- Spiller adds a caution: absence of evidence is "only negative proof"; he then tests the claim against the character of infantry combat itself (asymmetry: not all of a company is engaged at once; terrain; roles).
- An unnamed commentary found by search (source not recorded) notes that the claim that Marshall did no research at all is sometimes overstated and that Spiller allows that interviews did take place; this is consistent with the PDF's own caution.

**Grossman `[from search/standard account]`.** *On Killing* builds on Marshall (and on historical reports of unfired muskets) to argue that most people have a strong innate resistance to killing and that training overcomes it. Because the book relies on Marshall's figure, the Spiller critique weakens the empirical base; whether the broader thesis stands on other evidence was not checked here. A search for a "Williams critique" returned nothing and is **not** claimed here.

**Empirical standing.** The 15-25% figure should not be used as a parameter. The qualitative point (many soldiers do not fire, for reasons including role, terrain and fear) stands on other evidence but with no stable ratio.

**Translation.** A cautionary tale for the algebra: a scalar "fear removes X% of effective action" is exactly the type of number that is cited as a law and rests on unrecoverable data. A parameter attached to a fear operator must have a traceable data source.

---

## 12. Civil war: control, collaboration and violence (Kalyvas)

**Citations.** Kalyvas, S. N. (2006). *The Logic of Violence in Civil War*. Cambridge University Press, doi:10.1017/cbo9780511818462, confirmed via Crossref in validation. Kalyvas, S. & Kocher, M. (2007). "How 'free' is free riding in civil wars?: violence, insurgency, and the collective action problem." *World Politics* 59(2), doi:10.1353/wp.2007.0023, confirmed via Crossref. Berman, E., Shapiro, J. & Felter, J. (2008). "Can hearts and minds be bought? The economics of counterinsurgency in Iraq." NBER w14606, doi:10.3386/w14606, confirmed via Crossref. Lyall, J., Blair, G. & Imai, K. (2013). "Explaining support for combatants during wartime: a survey experiment in Afghanistan." *APSR* 107, doi:10.1017/s0003055413000403, confirmed via Crossref.

**Vocabulary `[from search]`.** Zones of control (fragmented versus near-hegemonic), collaboration, selective versus indiscriminate violence, denunciation, "joint production" of violence by political actors and civilians.

**Drives/operands.** Armed actors and civilians; the civilian's drive is survival, so fear of the controlling actor determines collaboration. Information is the scarce good.

**Operators / equations.** A verbal cycle with a verifiable shape: control fosters collaboration, collaboration yields information, information enables selective violence, selective violence generates more control. In contested zones, collaboration is harder, so actors use selective violence to consolidate control. `[from search]` The book's explicit formal element (a threshold on control at which selective violence becomes possible, and a "joint production" model of denunciation) was not retrieved; not stated.

**Theorems / predictions `[standard account]`.** Kalyvas divides territory into five zones from full incumbent control (zone 1) through parity (zone 3) to full insurgent control (zone 5). The key prediction concerns **selective** violence: it is most likely where one actor has **dominant but incomplete** control (zones 2 and 4), because defection (denunciation) is then both feasible for civilians and useful to the actor; it is low under full control (no need) and, counter-intuitively, low at parity (civilians will not denounce when either side could retaliate). **Indiscriminate** violence is the resort of actors lacking information, typically where they lack control, and Kalyvas argues it is usually counterproductive. (Validation correction: the draft said "violence is highest under near-hegemonic control" without restricting it to selective violence and omitted the low-at-parity prediction.)

**Empirical standing.** Widely cited, with many tests and extensions; support is mixed by case. Kalyvas & Kocher test the collective-action claim in Vietnam. Berman et al. (Iraq) find that small-scale reconstruction spending is associated with less insurgent violence `[standard account]`. Lyall et al. (Afghanistan survey experiment, endorsement method) find an asymmetry `[standard account]`: harm inflicted by ISAF reduces support for ISAF and raises it for the Taliban, while Taliban-inflicted harm does not translate into comparable gains for ISAF. Not verified beyond titles and DOIs; blunt: the control-collaboration cycle is the best-motivated loop here but is validated only at the case-study level.

**Translation.** A **fear-driven feedback loop between a group and a population**: control (a state variable of a territory) → collaboration (a population disposition) → information → violence → control. This is a closed loop with four named stages and so a natural target for a dynamical-systems form in the algebra; each arrow is an operator.

---

## 13. Honour, revenge and feud cycles

**Citations.** Boehm, C. (1984). *Blood Revenge: The Anthropology of Feuding in Montenegro and Other Tribal Societies*. University Press of Kansas (reissued by Penn Press as *Blood Revenge: The Enactment and Management of Conflict in Montenegro and Other Tribal Societies*); no DOI checked. Fieldwork dates from the HRAF record: 1963-1966, 1975. Existence confirmed in validation via reviews (e.g. Hoebel, *Man* 20, 1985, doi:10.2307/2802465). Black-Michaud, J. (1975). *Cohesive Force: Feud in the Mediterranean and the Middle East*. Oxford: Blackwell; no DOI, existence confirmed via contemporary reviews (Bailey, *Man* 10, 1975, doi:10.2307/2800179; Allen, *American Anthropologist* 78, 1976). Gould, R. V. (2003). *Collision of Wills: How Ambiguity about Social Rank Breeds Conflict*. University of Chicago Press, doi:10.7208/chicago/9780226305516.001.0001, confirmed via Crossref (reviewed by Stinchcombe, *AJS* 110, 2004).

**Black-Michaud and Gould, added in validation `[standard account]`.** Black-Michaud argues feud under ecological scarcity is *interminable* in principle: settlements are truces, and the feud is a "total" social relation that organises (is a "cohesive force" for) the groups it divides. Gould's thesis is that conflict, including vendetta (he uses nineteenth-century Corsican records), is most likely where **relative rank is ambiguous**, i.e. between near-equals, and least likely in clearly asymmetric relationships. Gould's is the one model in this section with a sharp, testable comparative static: violence is highest when the rank difference is near zero.

**Vocabulary `[from search]`.** Feud, blood revenge, moral sanction, tribunal of elders, settlement; honour.

**Drives/operands.** Lineages/kin groups as the operand; honour as a group-held stake that obliges retaliation. Boehm argues that in the absence of central authority, feuding functions as a moral sanction (a deterrence mechanism with no state). `[from search]` (The draft's further claim that it reduces population pressure on land could not be confirmed and is moved to Unconfirmed.)

**Operators / equations.** None found. Boehm traces the trajectory of feuds, the decisions at each point, and where they end or escalate, and describes a settlement mechanism by elders, with a general theory in the later chapters. `[from search]` Not read.

**Theorems.** None.

**Empirical standing.** Ethnographic, single-region, with cross-cultural comparison; no quantitative model. Contested as to whether feud "works" as deterrence versus as a self-perpetuating cycle.

**Translation.** The feud is **deterrence without a third party**: retaliation obligation (the honour operator) makes each group's threat credible by *social* commitment, and a settlement operator (mediation) breaks the cycle. It supplies two operators, `Avenge(g1,g2)` and `Settle(g1,g2,mediator)`, with the first reproducing itself unless the second intervenes. Same structure as the tit-for-tat family in other files.

---

## What exists vs what does not (blunt)

**Exists.**
- Theorem-bearing models of threat and resolve as payoffs/types: bargaining model of war (Fearon, Powell), perfect deterrence (Zagare & Kilgour), brinkmanship (Powell), audience costs (Fearon). Sound mathematics; weakly tested empirically.
- A typed operator set for fear-production: Kydd & Walter's five strategies, `[read]`.
- Qualitative feedback loops with named stages (Kalyvas's control-collaboration-information-violence cycle).
- Ordinal scales (Kahn's ladder) and risk-attitude regime switches (prospect theory).
- A debunking that is itself a lesson (Spiller on Marshall) `[read]`.

**Does not exist (as far as this survey found).**
- A **fear or resolve variable that is itself a dynamic state**, rising and decaying under actions. Resolve is a fixed private type; fear is a payoff. What is dynamic is the *belief* about resolve and the *accumulated* cost or risk: Fearon's (1994) audience costs rising over a crisis, Powell's brinkmanship risk rising as players hold (endogenous in total, with an exogenous per-step hazard), and the learning-while-fighting models of section 6. These are the nearest precedents and should be the starting point for any dynamic version.
- Any composition law over several threats or several audiences at once.
- A validated predictive model: RAND's will-to-fight model is an assessment framework; the most precise numbers (Marshall's ratio) are untrustworthy.
- Group-level fear as an emergent state: all models treat the state or group as a unitary actor with its own utility (the cohesion problem in file 24 is skipped).
- A clean separation between a *drive* and a *belief about a drive*: every model here puts the action at the level of beliefs about types.

## Unconfirmed

- Exact payoffs, equilibrium conditions and propositions of Powell (1990), Zagare & Kilgour (2000), Fearon (1994) and Fearon (1995): not read; textbook forms only for the war lottery. Fearon 1995's three mechanisms and the bargaining range (p - c_A, p + c_B) match the standard account and are internally consistent, but were not read at source.
- Powell: the claim that a player may be less likely to prevail the more resolve it has (paraphrase of an unsourced draft claim) — not found in any abstract checked (Powell 1988, 2015); possibly a garbled version of Kenkel & Schram's result.
- The RAND national (RR-2477) 15-variable list: count confirmed by search, list not retrieved.
- Kahn's count of 44 rungs and seven groups: textbook account, not rechecked.
- Jervis 1976: no DOI checked (book).
- Pape 1996 and Byman & Waxman 2002: existence confirmed, content from search summaries and standard account only.
- Kalyvas's five-zone model and selective-violence predictions: standard account, book not opened.
- Boehm: the claim that feuding reduces population pressure on land (from the draft, source not found).
- Black-Michaud and Gould theses: standard account, books not opened.
- The lab experiment on commitment versus information problems in section 6: study not identified.
- Grossman critiques (a "Williams critique" returned nothing).
- Bloom (2005) and tests of outbidding; Kahneman & Tversky parameter values (standard TK 1992 values, carried from standard account).
- Kydd 1997, Glaser 1997 (rational security dilemma): cited from standard account, DOIs not checked.

## Missing important work (noted in validation)

- **Snyder, G. H. (1961).** *Deterrence and Defense* — origin of the deterrence-by-denial versus deterrence-by-punishment distinction that Pape's coercion typology inherits.
- **George, A. & Smoke, R. (1974).** *Deterrence in American Foreign Policy*; **George (1991)** *Forceful Persuasion* — coercive diplomacy as a set of variants (try-and-see, gradual turning of the screw, ultimatum).
- **Huth, P. (1988).** *Extended Deterrence and the Prevention of War*; Huth & Russett's quantitative tests — the main statistical evidence on when deterrence holds.
- **Schultz, K. (2001).** *Democracy and Coercive Diplomacy* — the opposition party as the audience that makes threats informative.
- **Mercer, J. (1996).** *Reputation and International Politics*; **Press, D. (2005).** *Calculating Credibility* — whether past resolve carries forward, i.e. whether resolve has memory at all; directly relevant to a dynamic resolve variable.
- **Sechser, T. (2010)** "Goliath's curse" and **Downes & Sechser (2012)** on compellent threats — empirical tests of Schelling's compellence claims.
- **Fearon, J. D. (1994).** "Signaling versus the balance of power and interests," *JCR* 38: 236-269, doi:10.1177/0022002794038002004 (Crossref) — the companion to the audience-costs paper.
- **Powell, R. (2004).** "The inefficient use of power: costly conflict with complete information," *APSR* 98: 231-241, doi:10.1017/s000305540400111x (Crossref).
- **Maynard Smith (1974)** war of attrition — the biological ancestor of every attrition model here, cited by Kydd & Walter themselves; links to file 28.
- Emotions in IR as dynamic states: **Mercer (2010)** "Emotional beliefs," *IO*; **Hall (2015)** *Emotional Diplomacy* — the nearest attempts to treat fear and anger as states rather than payoffs.

## Validation log (2026-10-29)

Method: every DOI re-resolved at api.crossref.org; Kydd & Walter (PDF, Figure 1 rendered), Spiller (PDF) and RAND RR-2341 (PDF via Internet Archive) read at source; the rest checked against abstracts, publisher pages and search summaries.

- Schelling 1960, 1966 — ✓ (books; standard account)
- Kahn 1965 — ✎ corrected (group names mixed rung and group labels)
- Powell 1990 — ✓ DOI
- Powell 1988 brinkmanship (APSR) — ✎ corrected (was "later", year/DOI missing; is 1988, doi:10.2307/1958063)
- Powell 2015 — ✎ added citation; stability-instability claim ✓ against abstract; "less likely to prevail with more resolve" ? unconfirmed
- Kenkel & Schram 2024 — ✎ corrected (finding stated backwards; DOI added)
- Zagare & Kilgour 2000, 1993 — ✓ DOIs; ✎ added capability-necessary and paradox statements from TOC/publisher
- Fearon 1994 — ✓ DOI; ✎ corrected (model is a continuous-time war of attrition with audience costs rising over time; invented "fewer disputes ending in war" result removed; actual comparative statics added)
- Weeks 2008, Tomz 2007, Trager 2015 — ✓ (full titles/pages added)
- Snyder & Borghard 2011 — ✓ ("a penny, not a pound" is their title)
- Kertzer & Brutger — ✎ corrected (print year 2016, AJPS 60(1))
- Slantchev 2005 — ✎ corrected (the "audience costs assumed, not derived" critique was misattributed to it; Slantchev 2006 ISQ added)
- Trachtenberg 2012, Slantchev 2012 — ✎ DOIs added
- Fearon 1995 — ✓ DOI; three mechanisms and bargaining range ✓ against standard account (not read)
- Powell 2006 — ✓
- Wagner 2000, Filson & Werner 2002, Slantchev 2003, Powell 2004, Smith & Stam 2004, Langlois & Langlois 2009 — ✎ added (learning-while-fighting), DOIs ✓
- Experimental commitment-vs-information study — ? unconfirmed (not identified)
- Pape 1996 — ✎ added (was "no source found"); Pape 2003 — ✎ DOI found (10.1017/S000305540300073X)
- Byman & Waxman 2002 — ✎ added (was "no source found"; CUP/RAND, no DOI)
- Kydd & Walter 2006 — ✓ DOI; ✎ corrected (provocation's audience is own population and its uncertainty is the government's trustworthiness, not "enemy government"; attrition covers power and resolve; intimidation is power only; all six cells filled, not five)
- Kydd & Walter 2002 — ✓
- Jervis 1968 — ✓; Jervis 1978 — ✎ original DOI found (10.2307/2009958); Jervis 1976 ✓ (book)
- Levy 1992, McDermott 2004 — ✓
- RAND RR-2341 — ✓ DOI; ✎ 29 factors now listed [read]; definition corrected; quoted "finding" replaced with the report's wording; non-additivity added
- RAND RR-2477 — ✓ DOI; 15-variable list ? unconfirmed
- Marshall 1947, Grossman 1995 — ✓ (books)
- Spiller 1988 — ✓ (re-read); ✎ DOI added; 55% figure corrected (Korea report, April 1951, not a later preface)
- Kalyvas 2006 — ✎ DOI added; prediction corrected (selective violence, five zones, low at parity)
- Kalyvas & Kocher 2007, Berman et al. 2008, Lyall et al. 2013 — ✓ DOIs; ✎ Lyall et al. finding stated (asymmetry) [standard account]
- Boehm 1984 — ✓ existence; "population pressure" claim ? unconfirmed
- Black-Michaud 1975 — ✎ added (was "not found"; existence confirmed via reviews)
- Gould 2003 — ✎ added (was "not found"; Crossref DOI)
- Kydd 1997 / Glaser 1997 — ✎ added as the uncited "rational-choice theorists"; ? DOIs not checked
- Fabrications removed: none of the citations; one invented result (Fearon 1994 "fewer disputes ending in war") and one inverted finding (Kenkel & Schram) were removed or corrected.

**Verdict.** The bibliography is sound: every DOI the draft gave resolved to the right work, and nothing cited was fabricated. The content is less reliable than the tags suggest: the one table marked [read] (Kydd & Walter) had two of five rows mis-mapped and a wrong "empty cell" inference, two summarised results were wrong (Kenkel & Schram reversed; a Fearon 1994 result invented), and the headline "resolve is never dynamic" overstated a gap that war-of-attrition and learning-in-war models partly fill. Treat everything tagged [from abstract/search/standard account] as a lead to check, not a fact to build on.

## Licences of quoted and transcribed material (2026-10-30)

Rule: citations, facts and numbers are free; quotations short and attributed; tables and lists described rather than transcribed. Nothing below is reproduced beyond short quotation.

- Pape 1996, *Bombing to Win* (Cornell UP; the 2019 re-issue is open access, licence not checked): one 14-word quotation taken from a search summary, not the book. Not determined; publisher copyright presumed. Verify wording and add a page number.
- Kydd & Walter 2006, *International Security* 31(1), Figure 1 (MIT Press): the five-strategy table is a restatement of the figure's content (strategy, audience, uncertainty) in the file's own words, not a copy of the figure. Not determined; publisher copyright presumed. Shorten to prose if the licence is not confirmed.
- RAND RR-2341 (2018) and RR-2477: short quotations (the definition and two findings) and a described factor count. RAND research reports are generally released for free download under a permissive-use notice; exact terms not recorded here. Not determined; publisher copyright presumed. The full Table S.1 listing was removed in this audit.
- Spiller 1988, *RUSI Journal* 133(4) (Taylor & Francis): short quotations and a detailed paraphrase, read from an unofficial web copy. Not determined; publisher copyright presumed. Cite the DOI only; do not link to or redistribute the copy; confirm the copy is a legitimate upload.
- Marshall 1947 (via Spiller): two short quotations. Not determined; publisher copyright presumed.
- Powell 2015, Fearon 1994, Levy 1992, Zagare & Kilgour (Cambridge UP summary): paraphrases of paywalled abstracts, tagged [from abstract]. Not determined; publisher copyright presumed. Facts only; restate in own words when next revised.
- Kahn 1965 escalation ladder, "audience cost" and "security dilemma" definitions: standard-account wording that may track Wikipedia (CC BY-SA 4.0). Source not confirmed; rewrite from Kahn 1965, Fearon 1994 and Jervis 1978.
- Access route: RAND RR-2341 was read through an Internet Archive copy after a 403 on the RAND page. Not confirmed to be a public copy rather than a workaround for an access control; confirm.
- Unsourced quoted phrases (Powell resolve, Boehm population pressure, "never did the research") were unquoted in this audit and kept as unconfirmed paraphrases.
