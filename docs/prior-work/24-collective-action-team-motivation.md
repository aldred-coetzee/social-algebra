# Prior work 24: From individual drives to group motivation and collective action

Date: 2026-10-29. Survey for `social-algebra`. Not committed.

Aim served (Aldred, 2026-10-29): an algebra of basic human and group drives (curiosity, fear, desire) that compose into equations, yield theorems, and are used to predict or control behaviour. This note asks one question of the collective-action, team and unit-motivation literatures: **how do individual motives become a group's motivation to act, and is there a quantitative rule?** Cross-references: 06 (group dynamics frameworks), 13 (coercion), 18 (collective emotion, contagion, intergroup emotions), 05 (Granovetter thresholds, opinion dynamics), 08 (Tilly, Tarrow, history), 07 (applied control, and the warning about individual-level prediction).

## Summary

1. **Collective-action psychology has the best empirical standing and the weakest algebra.** SIMCA and its successors are path models: three or four named predictors (identity, injustice/anger, efficacy, later moral conviction) with meta-analytic effect sizes. They are regression structures, not composition laws. The aggregation from individual to group is nearly always "mean of members' self-reports", with no rule for how members' states combine.
2. **The clearest multiplicative drive-to-group rule is Karau and Williams's collective effort model** (Klandermans's funnel, Stenner's interaction and Epstein's grievance = hardship x (1 - legitimacy) are the others) (expectancy x instrumentality x valence, applied to group outcomes). It is expressed in words and verified in moderator patterns, not fitted as a single equation. Latane's social impact theory (strength x immediacy x number, with a power-law in number) is the only closed-form group-size law in the cluster.
3. **Group-level quantities that recur are few:** cohesion (social vs task), collective efficacy, grievance (relative deprivation / injustice), identity strength (politicised, fused), significance, and threat. Almost none has an agreed aggregation function. Where a rule is stated, it is mean, dispersion (polarisation), or a threshold (cross-ref 05).
4. **Downward effects are mostly one mechanism again:** salient identity turns the group into a source of appraisal, norms and efficacy beliefs for members (SIMCA, EMSICA, polarisation by social comparison, fusion, 3N network). Verbal in the psychological theories; formal versions exist outside them (Friedkin's influence-network model, Epstein's civil-violence agents, computational emergence models; see the validation corrections below).
5. **Predictive standing is modest.** Medium meta-analytic correlations for the collective-action predictors, small-to-moderate for cohesion and performance, a moderate social loafing effect. No model here predicts an individual's action out of sample in the sense 07 warns about; effect sizes are cross-sectional associations, and the causal share is small.

**Verification note.** Sources are web search results, the Crossref API (which confirms bibliographic records only, not claims) and two page fetches (the PubMed Central page of Iso-Ahola and Dotson 2016, read; the SIMCA PDF fetched but unreadable at drafting). **Validation pass (2026-10-29):** every DOI re-resolved against Crossref; the SIMCA full text (VU Research Portal publisher PDF) and the Varmann et al. 2023 fusion meta-analysis were read, so their numbers below are [read]; corrections are marked in place and logged at the end. Tags: **[read]** = text of the cited page was read this pass; **[abs]** = from abstract, search summary or secondary source this pass; **[std]** = standard account from general knowledge, not checked this pass. Every [std] claim is a candidate for checking before use. Effect sizes not retrieved are marked "not retrieved" rather than recalled.

---

## 1. SIMCA: van Zomeren, Postmes and Spears (2008)

- **Citation:** *Psychological Bulletin* 134(4), 504-535, doi 10.1037/0033-2909.134.4.504 (Crossref confirmed). Precursor: van Zomeren, Spears, Fischer and Leach (2004), "Put your money where your mouth is!", *JPSP* 87(5), doi 10.1037/0022-3514.87.5.649 (Crossref confirmed; the dual-pathway model: efficacy and anger as separate routes) [std on content].
- **Drives fed in:** a sense of injustice (grievance, with anger as the affective form), group efficacy (belief the group can change things), social identity (especially politicised identity). No drive vocabulary in the sense of curiosity/fear/desire; the nearest are anger (approach) and efficacy (expectancy).
- **Aggregation:** a path model. [abs] Three meta-analyses were run, pooling 182 effects, one meta-analysis per predictor; a secondary slide-deck source gives 65 injustice, 53 efficacy and 64 identity samples (unverified). Structure [std]: identity influences collective action directly and via injustice and efficacy; injustice and efficacy each predict action; the group's identity makes the grievance and the efficacy shared rather than personal. "Group" enters as the level of the measured constructs (identification with the group, group efficacy), averaged over respondents. [read, validation] The 65 / 53 / 64 figures are the number of samples (k) per meta-analysis, now confirmed from Table 1 of the paper.
- **Predictive claims and standing:** [read, validation pass, Table 1-3 of the paper] random-effects mean r: **injustice .35 (k = 65), efficacy .34 (k = 53), identity .38 (k = 64)**; equivalent d 0.72-0.83, medium by Cohen. All three highly heterogeneous. **Affective injustice r = .49 vs non-affective/unclear .31**; **politicised identity r = .43 vs non-politicised .34**. Experimental studies gave larger effects than non-experimental for efficacy (.49 vs .31) and identity (.47 vs .36). The authors stress the three were synthesised separately, so no unique (partial) contributions follow from these numbers. Standing: the most cited model in the field; its main weakness, discussed in later work, is that the three predictors overlap and the mediation structure is contested (see 2).
- **Downward effect:** identity determines whose injustice counts as "ours" and whose capability is "our" efficacy; yet the model gives no equation for it.
- **Translation:** operands: a person with a state vector (identification, perceived injustice, anger, efficacy); a group-level label (salient identity). Operator: none; it is a regression from state to propensity for action. A drive algebra could take identity as a gate (a salience switch) on grievance and efficacy.

## 2. EMSICA: Thomas, McGarty and Mavor

- **Citations:** Thomas, McGarty and Mavor (2009), "Aligning identities, emotions, and beliefs to create commitment to sustainable social and political action", *Personality and Social Psychology Review*, doi 10.1177/1088868309341563 (Crossref confirmed); Thomas, Mavor and McGarty (2012), "Social identities facilitate and encapsulate action-relevant constructs: a test of the social identity model of collective action", *Group Processes and Intergroup Relations* 15(1), 75-88 (online 2011, print 2012), doi 10.1177/1368430211413619 (Crossref confirmed); Thomas, Louis and McGarty (2022), Cambridge Handbook of Political Psychology chapter "Collective Action for Social Change", doi 10.1017/9781108779104.034 (Crossref confirmed, content not read).
- **Core idea [abs]:** EMSICA (encapsulated model of social identity in collective action) says that identity does not just add a path alongside injustice and efficacy, as SIMCA has it; it encapsulates them: perceived injustice and group efficacy are appraised through the lens of the salient identity and act on action via the identity. Social identity processes can both facilitate and encapsulate other action-relevant constructs.
- **Evidence [abs]:** three samples (N = 305, multigroup SEM); both SIMCA and EMSICA fit well, so the data do not discriminate strongly between them, and the path from group efficacy to action was small. Later applications (Gezi Park protest identity; an extended version adding threat and contact for Islamist terrorism support in Indonesia) [abs].
- **Why it matters:** this is the first model in the cluster to say how a group-level variable (identity) restructures individual appraisals. It is a structural claim about the topology of influence between variables, which is a statement an algebra can express (identity as a modifier operator applied to the other drives) even though the evidence does not yet force it.
- **Translation:** `identity` as an operator on appraisal rather than as one more operand.

## 3. Agostini and van Zomeren (2021): the dual chamber model

- **Citation:** *Psychological Bulletin* 147(7), 667-700, doi 10.1037/bul0000256 (Crossref confirmed; title: "Toward a comprehensive and potentially cross-cultural model of why people engage in collective action: a quantitative research synthesis of four motivations and structural constraints").
- **Content [abs]:** 1,235 effects, 403 samples, N = 123,707; four motivations synthesised into a "dual chamber model" together with structural constraints. The four are identity, injustice, efficacy and morality (moral conviction, the new addition) [abs, validation pass: confirmed from the abstract via search summary]; all four had unique, positive, medium-sized effects, with emotional injustice and politicised identification the strongest specific forms, and meta-analytic SEM supporting the added value of morality [abs]. Effect sizes smaller for behavioural than non-behavioural measures of collective action; the causal vs non-causal distinction did not significantly moderate the predictor-action relations [abs from supplementary-materials summary].
- **Standing:** the current large-sample update to SIMCA. Per-predictor r not retrieved.
- **Translation:** supplies the candidate list of group-action motives and a statement that structural constraints (opportunity, repression) are a separate chamber; this matches the algebra's likely split between drives and the environment's gating (cross-ref 13 on coercion).

## 4. Klandermans: demand and supply of protest, and participation as expectancy-value

- **Citation:** Klandermans (1984), "Mobilization and participation: social-psychological expansions of resource mobilization theory", *American Sociological Review*, doi 10.2307/2095417 (Crossref confirmed); book *The Social Psychology of Protest* (1997) [std]. Simon and Klandermans (2001), "Politicized collective identity", *American Psychologist* 56(4), doi 10.1037/0003-066X.56.4.319 (Crossref confirmed).
- **Drives fed in [std]:** grievances, identity, efficacy, ideology (the demand side); the mobilising campaign and its costs and benefits (the supply side).
- **Aggregation [std]:** participation is modelled in four steps, each a conditional probability: being sympathetic, being the target of a mobilisation attempt, being motivated, overcoming barriers. Overall participation is the product of the step probabilities. Motivation within the third step is expectancy-value: collective motives (value of the collective goal x expectancy that it is achieved), social motives (reaction of significant others), reward motives. This is a real equation-shaped rule, a product of conditionals with a sum-of-motives core, and it is the closest thing in the cluster to a decomposition one could use as an algebraic term. Not read this pass.
- **Standing:** the multiplicative funnel is a framework, not a fitted model; its steps have been measured in individual protest studies (e.g. the Dutch peace movement) [std]. Simon and Klandermans extend it: politicised collective identity emerges in a three-party struggle among group, opponent, and the wider public [std].
- **Downward effect:** social motives are the group's pressure on the individual; the identity becomes politicised through the struggle.
- **Translation:** operand: person with sympathy/motivation/barrier state; operator: `mobilise(movement, person)` gated by reach; the funnel form maps onto composition of conditional operators.

## 5. Relative deprivation: Gurr (1970) and Smith et al. (2012)

- **Gurr, *Why Men Rebel*, Princeton, 1970** [std; not read; the search did not return the propositions]. Relative deprivation is the perceived discrepancy between value expectations and value capabilities. Three patterns: decremental, aspirational, progressive [std]. The propositions [std, unverified]: the intensity and scope (share of population affected) of deprivation drive the potential for collective violence; justification (belief violence is warranted) and the group's institutional strength and the regime's coercive control shape whether potential becomes action. This is written as a chain of verbal proportionalities rather than a formula.
- **Standing:** [abs] a critical assessment of Gurr's own tests called the results inconclusive because the multi-nation sample forced general measures, leaving a "misery model" (objective decline) equally able to explain the data; his narrower US ghetto-riots test was an attempt to fix that. Postcolonial cases with high deprivation but little rebellion are cited as a challenge [abs]. A progressive-deprivation J-curve test on the urban riots exists (APSR) [abs, title only].
- **Smith, Pettigrew, Pippin and Bialosiewicz (2012):** "Relative deprivation: a theoretical and meta-analytic review", *PSPR* 16(3), 203-232 (online December 2011), doi 10.1177/1088868311430825 (confirmed). [abs, Crossref abstract, validation pass] **210 studies comprising 293 independent samples, 421 tests, 186,073 respondents** (so 293 is samples, not studies, as the draft had it). RD results across outcomes are "often weak and inconsistent"; RD measures that (a) include justice-related affect, (b) match the outcome's level of analysis (group RD for group outcomes such as collective action) and (c) are of higher quality yield significantly stronger relationships. This confirms the draft's recollection that the affective component and level-matching matter. Per-outcome effect sizes (including for collective action): not retrieved.
- **Drives fed in:** frustration/anger from perceived gap; a comparison drive (reference group choice). **Aggregation:** share of population affected (scope) is a proportion, the closest thing to a population aggregation.
- **Translation:** a gap operator `gap(expected, actual)` producing anger; the aggregate is a fraction of members over threshold, which links directly to Granovetter (05).

## 6. Jasper: emotions in social movements

- **Citations:** Jasper (1998), "The emotions of protest: affective and reactive emotions in and around social movements", *Sociological Forum* 13(3), 397-424, doi 10.1023/A:1022175308081 (Crossref confirmed in the validation pass; the record has no title field, which is probably why the drafting lookup looked like a failure). Jasper (2014), "Emotions, sociology, and protest", in von Scheve and Salmela (eds), *Collective Emotions*, OUP, doi 10.1093/acprof:oso/9780199659180.003.0023 (Crossref confirmed; same volume as 18 section 3).
- **Content [std]:** a taxonomy of emotions in movements: reflex (short-term, like anger at an event), affective loyalties (love, trust), moods, and moral emotions (shame, pride, indignation). Key mechanisms named: **moral shock** (an event that makes someone ready to act) and the **moral battery** (opposed emotions, such as anger and hope, that sustain participation). No equations.
- **Aggregation / downward effect:** none formal; the movement manufactures emotions through rhetoric and ritual and thereby changes members' drives. 18 covers transmission; here the point is that Jasper names the drive-like pairings (anger/hope, fear/trust) that a drive algebra would need to represent as opposed pairs.
- **Standing:** a conceptual framework, no meta-analytic support [std].
- **Translation:** a pair of opposed drives held in balance (cf. Smaldino on Brewer, 18 section 4); the moral battery is the one place in this cluster where drive conflict, not drive sum, is named as the motor.

## 7. Collective effort model, social loafing, Ringelmann, Latane

- **Karau and Williams (1993):** "Social loafing: a meta-analytic review and theoretical integration", *JPSP* 65(4), 681-706, doi 10.1037/0022-3514.65.4.681 (Crossref confirmed).
- **Drives fed in [abs]:** expectancy (that effort leads to performance), instrumentality (that performance leads to outcomes), valence of outcomes, now applied to group outcomes and to the member's identification with the group. [abs] "two key elements determine individuals' levels of motivation when working in a group: their expectations regarding their ability to reach the goal and the value they assign to the goal." The CEM's base is expectancy-value, social identity and self-validation theories.
- **Aggregation [std]:** motivation = expectancy x instrumentality x valence, evaluated where outcomes are group-level, and an individual's effort falls when their own contribution cannot be identified or evaluated, or when they expect others to carry the task. Stated in words and tested by moderators, not fitted as one equation. This is the only explicit multiplicative drive rule in the cluster.
- **Standing [abs]:** 78 studies; the review found loafing robust and generalising across tasks and populations, with a moderate effect. Moderators named: evaluation potential, expectations of co-workers, task meaningfulness, culture. Greater loafing in men than women, in Western than Eastern samples, on simple than complex tasks [abs, secondary]. Effect size: about 0.44 (d or g) per several secondary sources, consistent with the authors' "moderate" [abs, secondary only; primary table not read]. Simms and Nichols (2014) review (JMPP 15(1)) exists as a reference, not read [abs].
- **Ringelmann (1880s) and Ingham et al. (1974):** the rope-pulling effect, in which per-person output falls as group size rises. Ingham, Levinger, Graves and Peckham (1974), "The Ringelmann effect: studies of group size and group performance", *JESP*, doi 10.1016/0022-1031(74)90033-X (Crossref confirmed) separated coordination loss from motivation loss [std on method]; the loss is mostly coordination in the lab pulling task and a motivational share is the residual [std].
- **Latane, Williams and Harkins (1979):** "Many hands make light the work", *JPSP* 37(6), 822-832, doi 10.1037/0022-3514.37.6.822 (Crossref confirmed), the loafing application. The theory itself and its power law are stated in **Latane (1981), "The psychology of social impact", *American Psychologist* 36(4), 343-356, doi 10.1037/0003-066X.36.4.343** (Crossref confirmed; added in validation). Social impact theory [std, power-law form I = s N^t with 0 < t < 1 confirmed by secondary sources]: the effect of others on a target is a function of strength x immediacy x number, with the number term a power function with exponent below 1 (diminishing returns); in loafing the "target" is the task and the sources are the co-workers who share the load, so effort per person falls with group size on a decelerating curve.
- **Downward effect:** the group dilutes each member's marginal responsibility and the instrumentality of own effort (diffusion), and, in the other direction, identification raises the valence of group outcomes (the collective-effort gain).
- **Translation:** the best candidate for a literal drive composition: `effort = E x I x V`, with group size `N` entering through `I` and through the dilution exponent. Operand: person-with-expectancy; operator: `join(group)` multiplies `I` by a factor decreasing in `N` unless evaluation makes contribution identifiable.

## 8. Steiner: group productivity

- **Citation:** Steiner (1972), *Group Process and Productivity*, Academic Press [std; not read; no search this pass].
- **Rule [std]:** actual productivity = potential productivity - process loss. Potential is set by the task and members' resources; process loss is coordination loss plus motivation loss. Tasks are typed: **additive** (sum of members' output), **disjunctive** (best member decides), **conjunctive** (weakest member decides), **compensatory** (average), **discretionary** (group chooses how to combine), crossed with divisible/unitary and maximising/optimising. For the algebra this is the only explicit table of **aggregation functions** keyed to task type: sum, max, min, mean.
- **Standing:** the classification is a standard teaching framework and the motivation-loss term is what Ringelmann/Latane/Karau-Williams address. Not tested as a single fitted model [std].
- **Translation:** a table of aggregation operators `sum`, `max`, `min`, `mean` selecting how member contributions combine into group output. Directly usable as the answer to "what does the group's X mean": it depends on the task structure, and the algebra should carry the aggregation as an explicit, named operator rather than assume mean.

## 9. Hackman: team effectiveness

- **Citation:** Hackman (2002), *Leading Teams: Setting the Stage for Great Performances*, Harvard Business School Press [abs/std].
- **Content [abs]:** five conditions: a real (stable, bounded) team, a compelling direction, an enabling structure, a supportive organisational context, available expert coaching. A secondary source adds a fourth enabling condition ("shared mindset") as a later extension, not Hackman's.
- **Drives fed in:** goal meaningfulness, task interdependence, social support. Hackman's earlier job characteristics work (Hackman and Oldham) covered individual motivation; the team model moves to conditions rather than a motivation function [std].
- **Aggregation:** none; it is a conditions model, with team effectiveness defined on three criteria (output acceptable, members' growth, team's capability to work together again) [std]. No equation, and the team-size claim found online (5 to 9) was not verified.
- **Standing:** influential; direct tests of the five-conditions as a whole are sparse [std, unchecked].
- **Translation:** conditions as preconditions on an operator: the group-forming operator succeeds only if boundary, direction, structure, context and coaching predicates hold. Predicates, not scalars.

## 10. Group polarisation

- **Citations:** Myers and Lamm (1976), "The group polarization phenomenon", *Psychological Bulletin* 83(4), 602-627, doi 10.1037/0033-2909.83.4.602 (Crossref confirmed). Isenberg (1986), "Group polarization: a critical review and meta-analysis", *JPSP* 50(6), 1141-1151, doi 10.1037/0022-3514.50.6.1141 (Crossref confirmed). Friedkin (1999), "Choice shift and group polarization", *ASR* 64(6), 856-875, doi 10.2307/2657407 (Crossref confirmed in validation). Proietti on persuasive arguments with bipolar argumentation frameworks [abs, citation not retrieved].
- **Drives fed in:** the desire to be right (informational) and the desire to be liked or to stand well relative to the group (normative).
- **Aggregation [abs/std]:** the group's post-discussion mean shifts further toward the pole already favoured by the pre-discussion mean. Two mechanisms: **persuasive arguments** (members share arguments on the favoured side; the pool contains more arguments for that pole) and **social comparison** (members move to be seen at the favoured pole or slightly past the norm). Isenberg [abs]: both operate, each in the absence of the other; persuasive arguments had a significantly stronger effect; 33 independent effects synthesised. Effect size not retrieved.
- **Formal models:** persuasive arguments has an argumentation-framework formalisation and a multi-agent simulation literature [abs]; Friedkin's is a network-influence choice-shift model [abs]. A 2017 arXiv paper (frame-induced polarisation in small discussion networks) says the theory has never explained how polarisation is traded against pressure toward consensus [abs].
- **Downward effect:** the group's mean position becomes a norm that then moves each member; a stand-in for risky-shift and cautious-shift.
- **Standing:** polarisation by discussion is among the most replicated group phenomena [std]; the discriminating test (split subgroups: comparison predicts widening, arguments predict narrowing) is stated in [abs].
- **Translation:** an operator `discuss(group)` that maps a vector of positions to a more extreme mean with reduced variance. Two named components (informational, normative) give it a parameter structure the algebra can inherit.

## 11. Military unit cohesion, morale

- **Shils and Janowitz (1948):** "Cohesion and disintegration in the Wehrmacht in World War II", *Public Opinion Quarterly* 12(2), 280-315, doi 10.1086/265951 (Crossref confirmed). [abs] German POW interviews; claim: cohesion rested on small primary-group bonds more than Nazi ideology; disintegration set in when the group's integrity or its gratification of members' needs failed. Stouffer et al., *The American Soldier* (1949), four volumes, groups with Shils and Janowitz in arguing social cohesion within the primary group is central to military effectiveness [abs, secondary].
- **Critiques [abs]:** Madej (1978) rejected the primary group as central, crediting skill and organisational efficiency; Bartov argued that heavy losses destroyed primary groups so ideology supplied cohesion; van Creveld combined the primary-group and efficiency accounts; Kuhne favours primary-group solidarity plus institutional discipline and ideology. So the original is a single-case, retrospective interview claim with several serious alternatives.
- **King:** a King 2020 reply in *Armed Forces and Society* ("Broadening the perspective on military cohesion? A reply", doi 10.1177/0095327x20947150, Crossref confirmed) exists. King's own critique (that cohesion is formed in professional training and task performance, not in primary friendships; *The Combat Soldier*, 2013) is from memory [std] and unchecked here.
- **Siebold (2007):** "The essence of military group cohesion", *Armed Forces and Society* 33(2), doi 10.1177/0095327X06294173 (Crossref confirmed; content not retrieved). [std] distinguishes horizontal (peer) from vertical (leader) and social from task cohesion, and treats cohesion as multi-level.
- **Drives fed in:** affiliation, fear of letting down peers (honour/shame), safety, and the leader's legitimacy. **Aggregation:** unit cohesion is a unit-level attribute from members' ratings; no formula. **Downward effect:** primary group norms govern members' fear response and willingness to fight; the group is the immediate source of social reward and punishment.
- **Morale:** no formal quantitative model of morale found this pass; it is used as a construct (confidence in leaders, equipment, comrades, cause) measured by survey [std]. Gap noted below.
- **Translation:** operands: soldier with fear and affiliation; group with cohesion; operator: `lose(member)` and `bond(member, member)`. The decisive empirical lesson for an algebra is the dispute itself: whether the group drive is primary (peer-affiliation) or derived (task and institution).

## 12. Cohesion and performance: meta-analyses

- **Mullen and Copper (1994):** "The relation between group cohesiveness and performance: an integration", *Psychological Bulletin* 115(2), 210-227, doi 10.1037/0033-2909.115.2.210 (Crossref confirmed). [abs, secondary] the average cohesiveness-performance correlation is small but significant, and the commitment-to-task component carries most of it. Study count conflicts between secondary sources (49 studies in one, "66 studies, 92% positive" in the French source the draft used); neither primary, so both are unconfirmed. Mean r: not retrieved (the draft's recalled r around .25 is not confirmed). [std] Mullen and Copper also argued the performance-to-cohesion direction is at least as strong as the reverse.
- **Beal, Cohen, Burke and McLendon (2003):** "Cohesion and performance in groups: a meta-analytic clarification of construct relations", *JAP* 88(6), 989-1004, doi 10.1037/0021-9010.88.6.989 (Crossref confirmed). [abs] stronger links when performance is behaviour rather than outcome, and efficiency rather than effectiveness; unlike Mullen and Copper, all three cohesion components (interpersonal attraction, task commitment, group pride) were independently related to performance.
- **Carron, Colman, Wheeler and Stevens (2002):** "Cohesion and performance in sport: a meta-analysis", *JSEP* 24(2), doi 10.1123/jsep.24.2.168 (Crossref confirmed). [abs, secondary] moderate positive relation, mainly through task cohesion. Effect size not retrieved.
- **Moderators [abs, Crossref abstract]:** Gully, Devine and Whitney (1995), *Small Group Research* 26(4), 497-520, doi 10.1177/1046496495264003, found level of analysis and task interdependence moderate the link (51 effect sizes from 46 studies).
- **Reading:** cohesion is the single most-claimed group drive; its effect on performance is positive and modest, direction-of-causality contested (success may cause cohesion) [std on the causality point, standard in the literature].
- **Translation:** cohesion as a group-level scalar with at least three components; the output link is a moderated, small gain. The causal arrow can run either way, so the algebra should not treat cohesion as a primitive input without a loop.

## 13. Sport: team dynamics and momentum

- **Iso-Ahola and Dotson:** two papers, conflated in the draft. (a) 2014, "Psychological momentum: why success breeds success", *Review of General Psychology* 18(1), 19-33, doi 10.1037/a0036406; (b) 2016, "Psychological momentum: a key to continued success", *Frontiers in Psychology* 7, doi 10.3389/fpsyg.2016.01328 (the one read via PubMed Central). Both Crossref confirmed in validation. [read] PM is a perceptual force; initial success raises confidence, perceived competence and internal attributions; the raised perceived probability of success raises effort, closing a positive feedback loop; an efficiency principle says interruptions (time-outs) disrupt it; three effects (frequency, duration, intensity of runs). **No equations.** Reported evidence: golf run counts and lengths explained large shares of variance in finishes (91.5% for top-10; circular risk noted: runs and results are the same data); basketball time-out disrupting performance (56% drop reported, Mace et al. 1992); tennis PM model fit best (Jackson and Mosurski 1997). The article is by the model's proponents.
- **Hot hand:** Gilovich, Vallone and Tversky (1985), "The hot hand in basketball: on the misperception of random sequences", *Cognitive Psychology*, doi 10.1016/0010-0285(85)90010-6 (Crossref confirmed). Miller and Sanjurjo (*Econometrica* 2018, "Surprised by the hot hand fallacy?") 86(6), 2019-2047, doi 10.3982/ECTA14943 (Crossref confirmed in validation) show that the conditional-frequency estimator used by Gilovich et al. is biased downward in finite sequences (a streak-selection bias); corrected, the original GVT data show evidence of a hot hand rather than its absence [abs]. Later team-season replications with the correction are mixed [abs]. Contested; the reversal concerns individual shooting, not team momentum.
- **Team-level momentum [abs]:** NBA study found a TV time-out cut the momentum team's subsequent scoring by 11.2%; another (372 games) found more momentum runs for winning teams; a project-team momentum review (Coulon, Barki and Pare) imports the sports concept into management. No meta-analysis located.
- **Drives fed in:** confidence/competence (an efficacy variable) and effort. **Aggregation:** team momentum is a count of scoring runs, not an average of players' states. **Translation:** a positive-feedback loop on efficacy; the algebra needs a state with memory and an interruption operator (`timeout`) that resets it.

## 14. Mobilisation: Tilly, Tarrow, Granovetter

- **Cross-reference only.** Tilly's *From Mobilization to Revolution* (1978) and Tarrow's *Power in Movement* are covered in 08 (history) under political process and resource mobilisation; Granovetter (1978) threshold models are in 05. [std] The relevant rule is the threshold: person i acts if the fraction already acting reaches their threshold; the group outcome is the fixed point of the cumulative distribution of thresholds. It is the only fully formal individual-to-collective aggregation here and a candidate for the algebra's "mobilisation" operator, with the caution that thresholds are not independently measured, so the model is flexible but hard to falsify. Klandermans's supply-side (section 4) is the psychological counterpart to resource mobilisation.

## 15. Terrorism and radical group motivation: Kruglanski's significance quest

- **Citation:** Kruglanski, Gelfand, Belanger, Sheveland, Hetiarachchi and Gunaratna (2014), "The psychology of radicalization and deradicalization: how significance quest impacts violent extremism", *Political Psychology* 35 (S1), 69-93, doi 10.1111/pops.12163 (Crossref confirmed). Book: *The Three Pillars of Radicalization: Needs, Narratives, and Networks* (OUP, 2019) [abs].
- **Drive fed in:** a single primary motive, the **need for personal significance** (to matter, be respected), aroused by loss of significance (humiliation), threatened loss, or opportunity for gain. [abs] Model has three components: **needs** (motivational: the quest for significance sets a goal), **narrative** (ideological: identifies violence as an appropriate means), **networks** (social: group dynamics lead the individual to adopt the ideology and act; the network validates the narrative and rewards members who act).
- **Aggregation:** none formal; the group is the third pillar: it supplies narrative and rewards. In their account the commitment to the goal is relative to the competing goals the person has; extremism arises when the significance goal dominates and suppresses others, a goal-shielding argument [std].
- **Standing:** support is a mix of correlational surveys, small experiments and case studies; the 2014 paper presents "empirical evidence for the model's assumptions" [abs]. A theory that explains extremism by significance loss can explain almost any case after the fact; its predictive record for who radicalises is thin [std assessment, consistent with the base-rate problem in 07].
- **Downward effect:** the network sets what counts as significant and rewards it.
- **Translation:** one scalar drive (significance) with a trigger (loss/threat/opportunity), a channel (narrative selects the means), and a social amplifier (network rewards). Notably the same shape as Mackie et al. in 18: appraisal to action tendency.

## 16. Devoted actors and identity fusion

- **Swann, Jetten, Gomez, Whitehouse and Bastian (2012):** "When group membership gets personal: a theory of identity fusion", *Psychological Review* 119(3), doi 10.1037/a0028589 (Crossref confirmed). [std/abs] Fusion is a visceral sense of oneness with the group in which the personal self and the group self merge, so that group members are felt like family; fused people show **agentic personal self** plus group identity (both stay strong), reciprocity of strength between group and self, and so greater willingness to fight and die for the group.
- **Gomez et al. (2017):** "The devoted actor's will to fight and the spiritual dimension of human conflict", *Nature Human Behaviour* 1, doi 10.1038/s41562-017-0193-3 (Crossref confirmed). [abs] Three factors: commitment to non-negotiable **sacred values** and to the groups the actors are fused with; readiness to forsake kin for them; perceived **spiritual** strength of the in-group over foes mattering more than relative material strength. Sheikh et al. (2016) in *Current Anthropology*, 260 Moroccans, found that those treating sharia as sacred were more willing to use violence and to die [abs]. Sheikh, Gomez and Atran (2016), "Empirical evidence for the devoted actor model", *Current Anthropology*, doi 10.1086/686221 (Crossref confirmed). Atran and Gomez (2018), "What motivates devoted actors to extreme sacrifice, identity fusion, or sacred values?", *BBS* 41, doi 10.1017/S0140525X18001565 (Crossref confirmed) is, as far as the record shows, an open-peer commentary in BBS 41 (the volume carrying Whitehouse's 2018 target article on extreme self-sacrifice), not a target article as the draft said.
- **Standing:** [abs] experiments across five continents show fusion predicts willingness to fight, kill and die; willingness is a self-report intention, which is distant from behaviour. **A meta-analysis exists (added in validation, [read]):** Varmann, Kruse, Bierwiaczonek, Gomez, Vazquez and Kunst (2023), "How identity fusion predicts extreme pro-group orientations: a meta-analysis", *European Review of Social Psychology*, doi 10.1080/10463283.2023.2190267: 90 studies, 106 effects, N = 36,880; fusion r = .50 [.46, .53] with extreme pro-group outcomes, very heterogeneous (I^2 about 90%), versus social identification r = .37; strongest for extreme collective action (r = .61), then willingness to fight/die/sacrifice, then outgroup hostility (r = .43). The fusion-over-identification advantage may hold mainly in published studies. Note the authors include Gomez, a proponent. The original fusion measure paper is Swann, Gomez, Seyle, Morales and Huici (2009), *JPSP*, doi 10.1037/a0013668. Samples are often convenience or special populations (combatants, fans, Libyan revolutionaries) [std].
- **Drives fed in:** belonging/kin-like attachment, sacredness (non-tradeable value, a blocker on cost-benefit), threat to the group. **Aggregation:** none; it is a two-party relation (self to group) that is stronger than the sum of identification and cohesion. **Downward effect:** a fused group takes on kinship's motivational weight: members' own costs count for less than the group's.
- **Translation:** a relation operator `fuse(person, group)` that changes the person's utility from self-regarding to group-regarding; a sacred value as a constraint that removes an option from the choice set rather than a weight, which is a structural statement the algebra can hold directly.

## 17. Populism and threat: Stenner's authoritarian dynamic

- **Citations:** Stenner (2005), *The Authoritarian Dynamic*, Cambridge University Press, doi 10.1017/CBO9780511614712 (Crossref confirmed in validation). Feldman and Stenner (1997), "Perceived threat and authoritarianism", *Political Psychology* 18(4), doi 10.1111/0162-895x.00077 (Crossref confirmed).
- **Claim [abs]:** intolerance results from a stable **authoritarian predisposition** (preference for oneness and sameness over diversity) interacting with **normative threat** (leaders unworthy of trust, beliefs not shared across the community). Without threat, authoritarians are not unusually intolerant; with threat, they become so. The effect is an interaction, not an additive term.
- **Drives fed in:** fear of threat to the group's shared order (not to the person) plus a stable trait-like need for conformity.
- **Aggregation:** population-level prediction: when many people perceive normative threat, the correlation between authoritarianism and intolerance rises across the population; the rise is shared across a society, so the aggregate is a moderated correlation, not a sum.
- **Standing [abs]:** an independent test in Croatia (2010) found the correlation rose under present threat (several sites; not a replication of Stenner's experiments). I found no meta-analysis and no US replication in this pass; Hetherington and Weiler's work was not retrieved. So: one author's strong claim, partial independent support, replication record not established here.
- **Translation:** a product-form rule `intolerance = predisposition x threat`, where predisposition is a person constant and threat a perceived group-level variable. This is the cleanest example in the cluster of a trait x situation product that a drive algebra could express as an interaction operator.

---

## The recurring group drives (synthesis)

| Group-level drive | Where it appears | How it is measured |
|---|---|---|
| **Identity strength / salience** (politicised, fused) | SIMCA, EMSICA, fusion, 3N network | self-report of identification; fusion by pictorial scale |
| **Collective efficacy** | SIMCA, Klandermans (expectancy), momentum | self-report of "our group can"; success runs in sport |
| **Grievance / injustice / relative deprivation** | SIMCA, Gurr, Smith, Jasper | self-report; gap between expected and actual |
| **Anger (approach) and fear (avoid)** | SIMCA (anger), Jasper, 18 (Mackie), Stenner (threat) | self-report emotion |
| **Cohesion** (social, task, pride) | Shils-Janowitz, Mullen-Copper, Beal, Carron | questionnaire; peer ratings |
| **Significance** | Kruglanski | experimentally primed or surveyed loss |
| **Sacredness / moral conviction** | Gomez-Atran, Agostini-van Zomeren | self-report; refusal of trade-offs |
| **Valence of the group outcome x instrumentality** | Karau-Williams, Klandermans | expectancy-value items |
| **Normative threat / uncertainty** | Stenner (and Hogg in 18) | perceived threat to shared order |

The same four or five things recur across fields that rarely cite each other: *identity*, *efficacy*, *grievance/threat*, *cohesion*, *significance/sacredness*. Mapping these onto individual drives (belonging, competence, fairness/anger, safety, status) is the useful reduction; 15 supplies the candidate individual taxa.

## Aggregation rules found

1. **Mean of members' self-reports** (default in SIMCA, EMSICA, cohesion scales): no composition law, a measurement convention.
2. **Task-keyed combination functions** (Steiner): sum, max, min, mean, plus process loss; the only explicit family of aggregators.
3. **Product / expectancy-value** (Karau-Williams; Klandermans's motivation and funnel; Stenner's predisposition x threat): multiplicative composition.
4. **Power-law in group size** (Latane): diminishing marginal weight of each added person.
5. **Threshold fixed point** (Granovetter; 05) and **agent-based threshold with deterrence** (Epstein 2002, added in validation: an agent rebels when grievance G = H(1 - L) minus net risk exceeds a threshold, with arrest risk rising in the local cop-to-rebel ratio [std on the formula]): the population dynamics in the cluster.
9. **Composition models from multilevel theory** (added in validation): Chan (1998) types the functional relation between an individual construct and its group counterpart as additive (mean regardless of agreement), direct consensus (mean licensed by within-group agreement), referent-shift consensus (members rate "we" not "I"), dispersion (variance is the construct) and process models; Kozlowski and Klein (2000) distinguish composition (isomorphic) from compilation (non-isomorphic, e.g. min, max, configuration) emergence. This is the standard methodology vocabulary for exactly the aggregation question this note asks.
6. **Mean shift with variance reduction** (polarisation): a map from a pre-discussion vector to a post-discussion one.
7. **Run counts / state with memory** (momentum): not an average; a feedback loop.
8. **Interaction / gate** (EMSICA identity as encapsulator; fusion; sacred value as a blocker).

## What exists vs what does not

**Exists.**
- Meta-analytic estimates, medium-sized, of identity, injustice and efficacy on collective action (van Zomeren 2008; Agostini and van Zomeren 2021 with 1,235 effects), and a moderate social-loafing effect (78 studies).
- A task-typed list of aggregation functions (Steiner), a multiplicative effort rule (Karau-Williams), a group-size power law (Latane), a threshold fixed point (Granovetter), and two-mechanism models for polarisation.
- A rich qualitative vocabulary of group drives (cohesion, significance, fusion, moral shock), each with at least one survey instrument.

**Does not exist (or I did not find it).**
- **A composition law for drives at the group level.** No field says how two group drives (say cohesion and grievance) combine, conflict or trade off. SIMCA's paths are additive regressions; EMSICA's encapsulation is a structural claim without an operator.
- **A rule for how individual drive levels aggregate to a group drive** other than the mean, a task-typed pick from Steiner's table, or a threshold. *Corrected in validation:* mean vs min vs max vs variance **has** been tested for team composition traits (Bell 2007 meta-analysis, *JAP* 92(3), 595-615, doi 10.1037/0021-9010.92.3.595: the operationalisation moderated the link to performance; e.g. team minimum agreeableness and mean conscientiousness predicted field performance [abs]), and Chan (1998) supplies the typology. What remains absent is such a test for a motivational or drive construct (cohesion, grievance, efficacy) rather than a personality or ability trait.
- **Individual-level forecasting from these models.** The effects are cross-sectional correlations; prediction out of sample of who acts is not demonstrated (in line with 07's warning). Willingness-to-fight and intention measures are the usual outcomes.
- **A formal model of morale.** Not found.
- **A causal tie between cohesion and performance that is not circular** (success increases cohesion).
- **Replication-grade evidence for Gurr's formal propositions, Stenner's dynamic, significance quest and momentum.** Each has partial support and critics; none has a settled meta-analytic effect for its core claim as far as I found.
- **Equations for downward effects in the motivational theories.** SIMCA, EMSICA, Kruglanski, fusion and Jasper state verbally that the group changes the member's drives; none gives a function. *Corrected in validation:* the draft's "none gives a function" was too strong for the cluster as a whole. Friedkin's social influence network theory (cited in section 10) is an explicit function by which the group's positions move each member's (iterated weighted averaging anchored to initial positions [std]); Epstein (2002) makes arrest risk and thus each agent's action depend on local group state; and Kozlowski et al. (2013) argue for, and the team-cohesion literature has begun to use, computational/agent-based models of emergence with feedback. What is missing is a formal downward function for a *drive* (anger, efficacy, significance), not for opinions or behaviour.

Implication for the algebra (suggested, not decided): the literature supplies *operands* (identity, efficacy, grievance, cohesion, significance), a few *operators* in word form (`mobilise`, `join`, `discuss`, `fuse`, `threaten`), and a short list of *aggregation functions* that should be named explicitly in the algebra (sum, min, max, mean, product, threshold). It does not supply laws. Any theorem will be built here, not borrowed.

## Unconfirmed

- Karau and Williams effect size (about 0.44): secondary sources only; primary table not read.
- Mullen and Copper (1994) study count (49 vs 66) and mean r: secondary sources conflict; not retrieved.
- Smith et al. (2012) per-outcome effect sizes, including for collective action: not retrieved (the counts are now confirmed).
- Agostini and van Zomeren (2021) per-predictor r values: not retrieved.
- EMSICA 2012 test details (three samples, N = 305): search summary only.
- Atran and Gomez (2018) BBS: Crossref confirms the item; its status as a commentary rather than target article is inferred from the title and volume, not read.
- Gurr (1970) *Why Men Rebel* propositions, Steiner (1972), Hackman (2002), Stenner (2005), Klandermans (1997), King (2013) *The Combat Soldier*, Stouffer et al. (1949): books, not read or fetched; contents [std]. Hackman's "shared mindset" extension and the 5-to-9 team-size claim: unsourced.
- Isenberg (1986) 33 effects and the stronger persuasive-arguments effect; Sheikh et al. (2016) N = 260: abstract-level only.
- Iso-Ahola and Dotson's reported figures (91.5%, 56% drop, 11.2%): from the proponents' own review, primary studies not checked.
- Hetherington and Weiler on authoritarianism and polarisation: not located; no meta-analysis or failed replication of Stenner's dynamic found either way.
- Chiocchio and Essiembre (2009): citation only, from a search summary.
- Tarrow and Tilly: not searched; see 08.

## Missing work (identified in validation)

- **Olson (1965), *The Logic of Collective Action*** and Oliver and Marwell's critical-mass work: the rational-choice baseline (free-riding, selective incentives) against which every psychological model here is defined; its absence leaves the cluster without the null model. [std]
- **Chan (1998)**, *JAP* 83(2), 234-246, doi 10.1037/0021-9010.83.2.234, and **Kozlowski and Klein (2000)**, chapter in Klein and Kozlowski (eds), *Multilevel Theory, Research, and Methods in Organizations*: the composition/compilation vocabulary for aggregation.
- **Kozlowski, Chao, Grand, Braun and Kuljanin (2013)**, "Advancing multilevel research design: capturing the dynamics of emergence", *Organizational Research Methods* 16(4), 581-615, doi 10.1177/1094428113493119 [abs]: computational modelling of bottom-up emergence.
- **Bell (2007)** team-composition meta-analysis (above): empirical test of mean/min/max aggregation.
- **Epstein (2002)**, "Modeling civil violence: an agent-based computational approach", *PNAS* 99, 7243-7250, doi 10.1073/pnas.092080199: a formal grievance-legitimacy-risk rule for rebellion, the closest existing analogue to a drive equation for collective action.
- **Varmann et al. (2023)** fusion meta-analysis (above).
- **van Zomeren, Kutlaca and Turner-Zwinkels (2018)**, *European Review of Social Psychology* 29, 122-160, doi 10.1080/10463283.2018.1479347: the SIMCA extension adding moral convictions, precursor to Agostini and van Zomeren.
- **Latane (1981)**, the actual source of the social-impact power law (above).

## Validation log (2026-10-29)

- van Zomeren, Postmes and Spears 2008 (SIMCA): ✎ corrected (r values .35/.34/.38 read from the paper; 65/53/64 are k samples, confirmed; affective and politicised moderator r added).
- van Zomeren et al. 2004: ✓
- Thomas, McGarty and Mavor 2009: ✓
- Thomas, Mavor and McGarty 2012: ✎ corrected (volume, pages, online 2011)
- Thomas et al. 2022 handbook chapter: ✎ corrected (authors Thomas, Louis, McGarty)
- Agostini and van Zomeren 2021: ✎ corrected (four motivations confirmed: identity, injustice, efficacy, morality; volume and pages)
- Klandermans 1984: ✓ (content [std], not read)
- Simon and Klandermans 2001: ✓
- Klandermans 1997 book: ? unconfirmed (not fetched)
- Gurr 1970: ? unconfirmed (book; propositions [std])
- Smith, Pettigrew, Pippin and Bialosiewicz 2012: ✎ corrected (293 is samples, from 210 studies; 421 tests, N = 186,073; moderator findings added)
- Jasper 1998: ✎ corrected (DOI 10.1023/A:1022175308081 resolves; moved out of Unconfirmed)
- Jasper 2014: ✓
- Karau and Williams 1993: ✎ corrected (effect about 0.44 now secondary-sourced, not memory)
- Ingham et al. 1974: ✓
- Latane, Williams and Harkins 1979: ✎ corrected (power law attributed to Latane 1981, added)
- Steiner 1972: ? unconfirmed (book; typology is the standard account and matches)
- Hackman 2002: ? unconfirmed (book; extension claims unsourced)
- Myers and Lamm 1976: ✓
- Isenberg 1986: ✓ (abstract-level claims)
- Friedkin 1999: ✎ corrected (DOI 10.2307/2657407 found)
- Shils and Janowitz 1948: ✓
- King 2020: ✓; King 2013 book: ? unconfirmed
- Siebold 2007: ✓ (content [std])
- Stouffer et al. 1949: ? unconfirmed
- Mullen and Copper 1994: ✎ corrected (study count conflicting, recalled r withdrawn to Unconfirmed)
- Beal et al. 2003: ✓
- Carron et al. 2002: ✓
- Gully et al. 1995: ✓ (51 effects, 46 studies confirmed from abstract)
- Iso-Ahola and Dotson: ✎ corrected (2014 RGP and 2016 Frontiers titles were conflated; both DOIs added)
- Gilovich, Vallone and Tversky 1985: ✓
- Miller and Sanjurjo 2018: ✎ corrected (DOI 10.3982/ECTA14943 resolves; reversal stated more exactly)
- Kruglanski et al. 2014: ✓
- Swann et al. 2012: ✓
- Gomez et al. 2017: ✓
- Sheikh et al. 2016: ✎ corrected (DOI added)
- Atran and Gomez 2018: ✎ corrected (DOI found; a commentary, not a target article, inferred)
- Stenner 2005: ✎ corrected (DOI found)
- Feldman and Stenner 1997: ✓
- Closing claim "no equations for downward effects": ✎ corrected (true for the motivational theories, false for the cluster: Friedkin, Epstein, computational emergence)
- Claim "nobody tests mean vs max vs min": ✎ corrected (Bell 2007; Chan 1998)
- Claim "no fusion meta-analysis": ✎ corrected (Varmann et al. 2023, r = .50)
- No fabrications found; ✗ removed: none.

**Verdict.** The survey is bibliographically sound: every DOI it gave resolves to the stated work, and its two "failed" DOIs were in fact correct. Its quantitative content was thin rather than wrong (the recalled numbers that could be checked were close), but its synthesis overreached in three places: it missed a fusion meta-analysis, the composition-model literature that directly answers its aggregation question, and formal downward-effect models it half-cited itself (Friedkin). The overall verdict, that the literature supplies operands and named aggregators but no drive-level laws, survives in narrowed form: formal aggregation and influence functions exist for traits, opinions and behaviour, but not for motivational states.
