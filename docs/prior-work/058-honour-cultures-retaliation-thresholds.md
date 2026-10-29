# Prior work 058: honour cultures, retaliation thresholds and how insult rates feed violence

Direction: D181

Date: 2026-10-29. Survey for the social-algebra strand. Kind: deep-read. Question: what is the retaliation-threshold structure of honour cultures, and how do insult rates feed violence? Seeds: Nisbett & Cohen 1996; Gould 2003; Leung & Cohen 2011; Cooney 1998. Builds on 25 (B2) and 39 (section 13); it does not repeat them.

**Method and honesty note (read this first).** The brief asked for primary sources read in full. That was mostly not possible. The book-length sources (Nisbett & Cohen 1996, Gould 2003, Cooney 1998) are paywalled or not online here; the JPSP/PSPB/ASR papers returned 403 or a 404 (the GVSU copy of Cohen et al. 1996 is dead), and one attempted download was blocked by the sandbox classifier (I had passed `-k` to curl; I did not retry with TLS checks off). So **nothing below is tagged [read] at primary-source level.** What I have is: Crossref metadata (DOIs confirmed), abstracts and publisher descriptions via search summaries, and one secondary source that does give test statistics from the 1996 paper (Ulrich Schimmack, "Social Psychology Textbook audiT: Culture of Honor", Replication Index blog, 2019-01-11, https://replicationindex.com/2019/01/11/social-psychology-textbook-audit-culture-of-honor/; fetched and read, and re-read in validation). Tags used: `[abstract/summary]` = a search-result or publisher summary of the source; `[audit]` = statistics as quoted by the Replication Index audit of Cohen et al. 1996, itself secondary; `[standard account]` = background knowledge, unchecked this session; `[my inference]` = my own derivation, not from any source. No equation appears in any source I could reach. The seeds are verbal theories with a few regression-style empirical results, not formal models.

**Summary.**
1. **No source states a retaliation threshold as a number or an equation.** The "threshold" is a construct inferred from the pattern: the same insult triggers a response in honour-culture men and not in others. It is measured only indirectly (anger, physiology, hallway distance, story endings, norm attitudes). So the algebra would be introducing the threshold parameter, not importing it.
2. **The best-known lab evidence is weaker than its textbook reputation.** Per Schimmack's audit (Replication Index, 2019), only the "chicken game" result in Cohen et al. 1996 is clearly significant (t(142) = 3.45, p < .001); self-reported anger was not (p between .10 and .15); the hormone effects rest on planned contrasts at p < .03. The audit states it knows of no replication of these experiments. I found none either, in two searches, and no meta-analysis.
3. **The field and archival evidence has more weight** for the existence of regional differences in argument-related homicide and honour-related leniency, and the sources that bear on how insults become violence structurally (Gould, Cooney) are about **status ambiguity and third parties**, not about individual thresholds. These two give the algebra its operators; the psychology gives it a parameter.

---

## 1. Cohen, Nisbett, Bowdle & Schwarz (1996): the insult experiments

**Citation.** Cohen, D., Nisbett, R. E., Bowdle, B. F., & Schwarz, N. (1996). Insult, aggression, and the Southern culture of honor: An "experimental ethnography". *Journal of Personality and Social Psychology*, 70(5), 945-960. DOI 10.1037/0022-3514.70.5.945 (Crossref confirmed, issued 1996-05). Abstract also on the Russell Sage page, https://www.russellsage.org/node/4521 (which lists Nisbett first; Crossref and the journal list Cohen first).

**Their vocabulary.** Culture of honor; masculine reputation; insult; threat to reputation; "insult-aggression cycle"; being "primed for aggression"; experimental ethnography.

**Drives/operands.** Operand: a man (University of Michigan students raised in the North or South) with a reputation stake. Drive: restoration or defence of status/reputation. Group parameter: region of upbringing.

**Procedure** `[abstract/summary]`. Three experiments. A confederate bumps the participant in a corridor and says a derogatory word (reported in the abstract as "asshole"). Controls are not bumped or insulted. Outcomes: thoughts and emotion (anger, perceived threat to masculine reputation), cortisol and testosterone, and behaviour (completing a violent-or-not story; the hallway "chicken" game in which the participant and an approaching confederate walk toward each other).

**Results `[audit]`** (as quoted by the Replication Index; I did not see the primary tables):
- Study 1, anger rating: Southerners 3.05, Northerners 2.34, F(41) = 1.61, p between .10 and .15 (not significant; "F(41)" is as printed in the audit). The audit adds that Experiments 2 and 3 gave weak and inconsistent anger results, so none of the three studies significantly supports the anger claim.
- Study 1, violent story endings: region by insult interaction F(1,78) = 7.65, p < .005. Means 2.30 (Southern insult), 1.40 (Southern control), 1.73 (Northern insult), 2.05 (Northern control). Study 2 used a different scenario and found no significant effects (all Fs < 1).
- Study 2 hormones, planned contrasts: cortisol t(165) = 2.14, p < .03; testosterone t(165) = 2.19, p < .03. Testosterone change +12% (insulted Southerners), +4% (control Southerners), +6% (insulted Northerners), +4% (control Northerners). Search summaries also quote cortisol +79% vs +42% (insulted vs control Southerners) and +33% (insulted Northerners); the audit gives no cortisol percentages, I could not tie any of them to a primary table, and they are inconsistent across summaries. Treat the cortisol percentages as unconfirmed.
- Chicken game: a +3, -1, -1, -1 contrast (insulted Southerners against the other three cells, so strictly a focused contrast rather than an omnibus interaction), t(142) = 3.45, p < .001 `[audit]`. Distances, as quoted in the audit: Northerners, insulted or not, stood aside at about 5 ft; uninsulted Southerners at about 9 ft; insulted Southerners pushed on to about 3 ft `[audit]`.

**Operators / equations.** None stated. Only the verbal cycle: insult diminishes reputation, the man responds with aggression or dominance to restore it `[abstract/summary]`.

**Theorems or derived predictions.** Prediction: region by insult interaction on threat appraisal, physiology and aggression. No formal derivation.

**Empirical standing (blunt).** The audit's criticisms: the published account is an idealised recollection; many dependent variables with mixed results; hormone effects only in planned contrasts, not omnibus tests; significant-versus-nonsignificant comparisons made without testing the difference; and a lab bump is not evidence of readiness to kill. It states that, to its author's knowledge, the experiments have never been replicated. I found no replication or registered report, and no meta-analysis. Adjacent partial support: IJzerman, van Dijk & Gallucci (2007), a Dutch train-station field experiment with 42 men, found insulted men who endorsed honour norms reported more anger and less joy, fear and resignation than insulted low-honour men (*Emotion* 7(4), 869-875, DOI 10.1037/1528-3542.7.4.869, Crossref confirmed; results and N = 42 from a search summary, not checked against the paper). That is an individual-differences result in a different country, not a replication of the regional effect.

**Translation.** `insult(a,b)` is a state-changing operator on b's `reputation` operand. The paper supports the claim that the *response function* to the same operator differs by a person parameter. It gives no functional form: a candidate for the algebra's "threshold" is simply the response-curve crossing point, which here is only observable as a step between two groups.

---

## 2. Nisbett & Cohen (1996) *Culture of Honor*, with Nisbett (1993) and Cohen & Nisbett (1994, 1997)

**Citations.**
- Nisbett, R. E., & Cohen, D. (1996). *Culture of Honor: The Psychology of Violence in the South*. Westview Press. Reissue DOI 10.4324/9780429501142 (Crossref confirmed; chapter DOIs such as 10.4324/9780429501142-1, -4, -6 exist). Not read.
- Nisbett, R. E. (1993). Violence and U.S. regional culture. *American Psychologist*, 48(4), 441-449. DOI 10.1037/0003-066X.48.4.441 (Crossref confirmed). Abstract via NCJRS.
- Cohen, D., & Nisbett, R. E. (1994). Self-protection and the culture of honor: Explaining Southern violence. *Personality and Social Psychology Bulletin*, 20(5), 551-567. DOI 10.1177/0146167294205012 (Crossref confirmed, pages included; issued 1994-10). Crossref abstract read: three surveys show Southern White males endorse violence not unconditionally but for self-protection, defence of honour and socialising children; the authors tie this to Southern gun ownership and homicide types.
- Cohen, D., & Nisbett, R. E. (1997). Field experiments examining the culture of honor: The role of institutions in perpetuating norms about violence. *Personality and Social Psychology Bulletin*, 23(11), 1188-1199. DOI 10.1177/01461672972311006 (Crossref confirmed, pages included).

**Their vocabulary.** Culture of honor; herding economy; reputation for toughness; argument-related versus felony-related homicide; institutions (employers, newspapers, law) that perpetuate the norm.

**Drives/operands.** Reputation and self-protection under weak state protection. Operands: men, and institutions that either sanction or excuse retaliation.

**Law (verbal).** `[abstract/summary]` for the shape: herders' wealth is mobile and can be lost overnight, so they cultivate a reputation of being not to be trifled with, signalled through public quarrels; Scots-Irish settlers carried this to the South and to western areas settled from it. The 1993 abstract: homicide among white males is more common in the South and in western regions initially settled by southerners; the regional gap is not fully explained by poverty; the slavery-history and imitation-of-Black-violence explanations are challenged by the evidence. A university summary (Michigan News, 1997) reports the gap is in argument-related homicide, not felony-related homicide (strangers) `[abstract/summary]`.

**Field experiments (1997)** `[abstract/summary]`: Study 1, employers across the U.S. received letters from an applicant who said he had killed someone in an honour-related conflict; Southern and western firms responded with more understanding and warmth, with controls showing the sympathy was specific to honour-related violence, not crime in general. Study 2, newspapers given facts about a stabbing after a family insult; Southern and western papers wrote more sympathetic, more justifying stories. Sample sizes and tests not seen.

**Operators / equations.** None. The nearest to an operator is institutional: third parties' reaction to a retaliation either validates or punishes it (this is where the "threshold" is held in place: it is socially maintained, not private).

**Theorems/predictions.** Verbal: (i) honour-culture regions show more argument-related homicide, not more felony homicide; (ii) institutions in those regions treat honour-related violence more leniently; (iii) individual men's norm-endorsement predicts response to insult. (i) is an aggregate pattern that supports existence of a threshold difference at population level, with the usual ecological-fallacy caveat.

**Empirical standing.** The regional homicide pattern for white males and argument-related killings is the sturdiest claim, because it is observational data at scale, but it is correlational and open to confounds (economics, guns, climate, migration). The herding origin is a historical inference; a direct test, Chu, Rivera & Loftin (2000), "Herding and homicide: an examination of the Nisbett-Reaves hypothesis", *Social Forces* 78(3), 971-, DOI 10.2307/3005938, exists (Crossref confirmed) but I could not read its result, nor Rivera, Chu & Loftin (2002), *Int. J. Sociology and Social Policy* 22(7/8), 109-121, DOI 10.1108/01443330210790111, which evaluates the "Nisbett-Cohen thesis" on strong communities and homicide. **Their conclusions are unconfirmed; do not cite them as supporting or refuting.** Baller, Zevenbergen & Messner (2009), "The heritage of herding and southern homicide: examining the ecological foundations of the code of honor thesis", *J. Research in Crime and Delinquency* 46(3), 275-300, DOI 10.1177/0022427809335164 (Crossref confirmed), is a later test. Its abstract (Crossref, read): county-level FBI Supplementary Homicide Reports on argument-related White male offenders, 1983-1998; a positive interaction between the 1850 Presbyterian-church share (Scots-Irish proxy) and 1850 cattle and pigs per capita, and a negative effect of 1850 crop production; the authors call this "highly consistent with the herding thesis". So the herding hypothesis has at least one supportive ecological test; Chu et al. (2000) remains unread.

Also relevant: Brown, Osterman & Barnes (2009), School violence and the culture of honor, *Psychological Science* 20(11), 20(11), 1400-1405, DOI 10.1111/j.1467-9280.2009.02456.x (Crossref confirmed). Abstract (Crossref, read): controlling for demographics, high-school students in honour states were more likely to report bringing a weapon to school in the past month, and honour states had more than twice as many school shootings per capita over a 20-year period. The authors interpret school violence as retaliation for social-identity threat. State-level, ecological, and "honour state" is the authors' classification.

**Translation.** This is where **insult rate** and **violence** connect at the population level: if the fraction of insults answered with violence is higher, argument-related homicide rises while felony homicide does not. The sources give the *pattern*, not the rate function.

---

## 3. Gould (2003) *Collision of Wills*, and Gould (2000)

**Citations.**
- Gould, R. V. (2003). *Collision of Wills: How Ambiguity about Social Rank Breeds Conflict*. University of Chicago Press (posthumous). DOI 10.7208/chicago/9780226305516.001.0001 (Crossref confirmed). Publisher chapters: "Conflict, Honor, and Hierarchy"; "Dominance Relations"; "Strife out of Symmetry"; "Solidarity and Group Conflict"; "Conflict and Social Structure"; "Honor and the Individual" (publisher page). Not read.
- Gould, R. V. (2000). Revenge as sanction and solidarity display: An analysis of vendettas in nineteenth-century Corsica. *American Sociological Review*, 65(5), 682-704. DOI 10.1177/000312240006500504 (also 10.2307/2657542; Crossref confirmed both, pages included). A related Gould paper, "Collective violence and group solidarity: evidence from a feuding society" (ASR 64(3), 356-380, 1999; DOI 10.1177/000312249906400303, Crossref confirmed), not read.
- Reviews located (not read): Stinchcombe, *AJS* 110(1), 231-232, 2004, DOI 10.1086/424624; Senechal de la Roche, *Contemporary Sociology* 34(1), 68-69, 2005, DOI 10.1177/009430610503400146 (both Crossref confirmed).

**Their vocabulary.** Rank ambiguity; symmetry; dominance relations; honour; hierarchy; solidarity; sanction; solidarity display.

**Drives/operands.** Dominance/status as the driver. Operands: dyads and kin groups with a (possibly ambiguous) rank ordering.

**Core claim `[abstract/summary]`:** conflict is more likely between social equals or friends than between people whose rank is settled, because violence typically arises when someone wants dominance, even without a substantive grievance; when rank is ambiguous, perceptions of asymmetry can be contested and people fight to settle it. Honour is treated as a real stake: an insult is felt as dishonour even absent concrete harm (publisher/blurb level). Small disputes (debts, insults, queue-cutting) escalate through this mechanism.

**Gould (2000) results** (abstract, read via Crossref in validation; the summary below matches it): vengeance is framed as a purposeful sanction against collective aggression, not a prescribed response to any aggression; vengeance was rare (it typically occurred when the original incident involved collaboration or violence against non-disputants); vengeance rarely extended beyond the nuclear family, and when it did, distant kin were the actors; targets were selected on specific acts of solidarity, not abstract collective responsibility, and revenge was calibrated to show the aggrieved family's cohesion equalled the offender group's; Gould calls vendettas "highly strategic yet altruistic". Data: court records, Corsica. This **contradicts the picture of honour as an automatic low-threshold reflex**: in the archival record, retaliation was conditional and strategic.

**Operators / equations.** None found (no formal model in what I could reach). Verbal operator: `contest(a,b)` to settle an ambiguous rank; `avenge(g1,g2)` conditioned on collaborative aggression.

**Theorems/derived predictions.** (i) P(conflict) is higher in symmetric dyads than in asymmetric ones. (ii) Revenge probability depends on the *group character of the original act* (collaboration, non-disputant victims), not on the injury alone. Both are testable empirical regularities, not deductions.

**Empirical standing.** Corsican court records (single case); the 2003 book's breadth (murders, feuds, revolutions) is praised in reviews I saw only in summary. Not replicated by independent data as far as I found. A caution on the main claim: "equals fight more than unequals" has the base-rate problem that interactions between equals are more frequent; I could not check whether Gould conditions on contact.

**Translation.** Insult as an operator on *rank*, not just reputation. Gould supplies the missing second argument of the threshold: the response to an insult depends on whether the ordering of the pair is settled. `insult(a,b)` raises b's response where `rank(a,b)` is ambiguous and lowers it where settled (my reading of his thesis, `[my inference]`).

---

## 4. Cooney (1998) *Warriors and Peacemakers*, and Phillips & Cooney (2005)

**Citations.**
- Cooney, M. (1998). *Warriors and Peacemakers: How Third Parties Shape Violence*. New York University Press. DOI 10.18574/nyu/9780814723678.001.0001 (Crossref confirmed; the DOI is on the 2020 online edition). Not read.
- Phillips, S., & Cooney, M. (2005). Aiding peace, abetting violence: Third parties and the management of conflict. *American Sociological Review*, 70(2), 334-354. DOI 10.1177/000312240507000207 (Crossref confirmed). Abstract not obtained.
- Cooney, M. (1997). The decline of elite homicide. *Criminology* 35(3), 381-407. DOI 10.1111/j.1745-9125.1997.tb01222.x (Crossref confirmed; not read, listed as related).

**Their vocabulary.** Third parties; social control; partisanship; Black's paradigm (the book contents list "Black's Theoretical Paradigm"); authority strong versus weak; group boundaries.

**Core claim `[abstract/summary]`:** homicide is best explained not by the killer's and victim's characteristics but by who surrounds them: family, friends, neighbours, onlookers, police, judges. Third parties can be a source of peace or violence depending on configuration. Violence flourishes when authority is very strong or very weak, when third-party ties are strong, and when boundaries between groups are sharply defined. Scope: social control of homicide in over 30 societies, plus interviews with several dozen prisoners for murder or manslaughter (library/CV descriptions).

**Operators / equations.** None found. Verbal operators: `side_with(c, a)`, `mediate(c; a,b)`, `ignore`. This is the part of the literature closest to an algebraic object: a third-party function that maps a dyadic dispute and an observer configuration to escalation or settlement.

**Theorems/predictions.** Non-monotonic: violence at both high and low authority (a U-shape in authority strength), increasing with tie strength and boundary sharpness. Stated as a regularity across societies, from a summary. **Whether this is a statistical result or a typological claim I cannot tell.**

**Empirical standing.** Comparative-ethnographic and interview data; no quantitative test I could confirm. Cooney and Phillips' later work tests Donald Black's geometry of law (CV), not checked.

**Translation.** The strongest connection to the pre-existing algebra: a **third-party operator** whose configuration (not the dyad's drives) sets whether an insult-retaliation sequence ends or continues. It also dovetails with Cohen & Nisbett 1997 (institutions excuse retaliation) and with Gould 2000 (retaliation conditional on group character).

---

## 5. Leung & Cohen (2011): honour, face and dignity as cultural logics

**Citation.** Leung, A. K.-Y., & Cohen, D. (2011). Within- and between-culture variation: Individual differences and the cultural logics of honor, face, and dignity cultures. *Journal of Personality and Social Psychology*, 100(3), 507-526. DOI 10.1037/a0022151 (Crossref confirmed, issued 2011-03, pages included). Abstract read via Semantic Scholar; open-access copy listed at https://ink.library.smu.edu.sg/soss_research/1026 (not fetched).

**Their vocabulary.** Cultural logic; Culture x Person x Situation (CuPS); honour (respect for the individual as member of a specific group), face (hierarchy, in-group harmony, modesty), dignity (inalienable individual worth, personal accountability) `[abstract/summary]`.

**Result (abstract, read).** Two experiments with participants from honour, face and dignity cultures: the same "type" of person who was most helpful, honest and likely to behave with integrity in one culture was the "type" least likely to do so in another. The abstract names honour-related violence and individual worth as inalienable versus socially conferred as central concepts; the definitions of the three logics given above are from summaries, not the abstract. I did not obtain the traits, sample sizes or effect sizes.

**Operators / equations.** None.

**Relevance to the threshold.** The key point for the algebra: the *same* individual trait maps onto behaviour differently under different cultural logics, so a person-level "threshold" scalar is the wrong type; it must be a function of (person, culture, situation). This is the only seed that warns against a universal scalar threshold, and it is the reason the later translation below makes the threshold a function.

**Empirical standing.** Two experiments (abstract-level); cited for measurement-model follow-up by Yao et al. (2017), *Management and Organization Review* 13(4), listed by search only.

---

## 6. Further sources located (not read; for the next pass)

- Gul, P., Cross, S. E., & Uskul, A. K. (2021). Implications of culture of honor theory and research for practitioners and prevention researchers. *American Psychologist*, 76(3), 502-515. DOI 10.1037/amp0000653 (Crossref confirmed; open access per Semantic Scholar, but the PDF fetch returned no text). Abstract (read via Semantic Scholar): relative to Whites in northern states, White populations in southern and western states have higher intimate-partner violence, more school shootings and lower mental-health help-seeking; it also reviews Latinx groups as a culture of honour. It is the likeliest single source for a current review of replications and should be read next.
- Cohen, D., Vandello, J., Puente, S., & Rantilla, A. (1999). "When you call me that, smile!" How norms for politeness, interaction styles, and aggression work together in Southern culture. *Social Psychology Quarterly*, 62(3), 257-. DOI 10.2307/2695863 (Crossref confirmed). Not read. Notable: politeness and aggression as a coupled norm pair, which would be directly relevant to the threshold structure (courtesy lowers the rate of provocations; the threshold for responding to a provocation is low).
- Vandello, J. A., & Cohen, D. (2003). Male honor and female fidelity: Implicit cultural scripts that perpetuate domestic violence. *JPSP* 84(5), 997-1010. DOI 10.1037/0022-3514.84.5.997 (Crossref confirmed). Not read.
- Vandello, J. A., Cohen, D., & Ransom, S. (2008). U.S. Southern and Northern differences in perceptions of norms about aggression: Mismatches between attitudes and behavior. *J. Cross-Cultural Psychology* 39(2), 162-177. DOI 10.1177/0022022107313862 (Crossref confirmed). Not read; the title implies a pluralistic-ignorance mechanism that would keep a threshold in place beyond individual preference.
- Cohen, Vandello & Rantilla (1998), "The sacred and the social: cultures of honor and violence", in *Shame* (OUP), 261-282, DOI 10.1093/oso/9780195114799.003.0014 (Crossref confirmed; Crossref lists the authors as Cohen, Vandello & Rantilla). Not read.

---

## 7. A candidate formalisation (my inference, not from any source)

No seed gives equations, so the following is mine and unvalidated; it is offered only because the direction asked how insult rates feed violence. It is flagged here so nobody mistakes it for a literature result.

Let a population have insult rate `lambda` (insults per person per unit time), and a person-by-situation response probability `r = F(s; theta, c)` where `s` is insult severity, `theta` the person's retaliation threshold (a free parameter), and `c` the cultural/rank context (Leung & Cohen: the map from `theta` to behaviour depends on `c`; Gould: depends on rank ambiguity; Cooney: depends on third-party configuration). A retaliation is itself an insult/injury to the first party, generating on average `k` follow-on provocations. Then a retaliation chain is a branching process with mean offspring `m = r * k`: chains die out for `m < 1` and can sustain (feuds) for `m >= 1`. On this reading:
- Honour cultures differ in `r` (lower `theta`) and in third-party effects on `k`.
- The Gould finding that Corsican revenge was rare and conditional on group character says `r` was low overall in that setting, so an honour *norm* does not imply `m >= 1`.
- Cooney's U-shape in authority would have to enter through `k` (third-party escalation or de-escalation), not `theta`.
This is a conjecture; no data in the sources constrains `k`, and there is no source test of an `m` threshold.

---

## What exists versus what does not

**Exists.**
- A well-cited verbal theory linking mobile wealth + weak state protection to a low private threshold for responding to insult (herding hypothesis).
- Regional differences in argument-related homicide among white US men and in institutional leniency toward honour-related violence (observational, field letters).
- A dated lab paradigm (bump and insult) with one clearly significant behavioural result and weaker hormone/self-report results, unreplicated.
- A sociological account (Gould) that rank ambiguity, not just reputation, drives disputes; and archival evidence that retaliation in a vendetta culture was conditional.
- A third-party account (Cooney) of what ends or extends violence; a three-way cultural typology (Leung & Cohen).

**Does not exist (in what I found).**
- A quantitative threshold: no source estimates a threshold distribution, an insult-rate to violence-rate function, or a branching-type escalation condition.
- Any formal model (equation or game) by these authors; the formalisations that exist (Hawk-Dove with reputation, deterrence) are other people's and were not tied to these data here.
- A replication, registered report or meta-analysis of the insult experiments.
- Any individual-level prediction of who will retaliate; the evidence is group-contrast.
- Longitudinal evidence that lowering insult rates lowers violence in these cultures.

## Unconfirmed

- All numbers marked `[audit]` or `[abstract/summary]` are unchecked against the primary papers (the `[audit]` figures were re-checked against Schimmack's post and match it). The cortisol percentage figures are inconsistent across summaries and absent from the audit.
- IJzerman et al. 2007: N = 42 and the emotion results are from a search summary.
- The Michigan News (1997) summary on argument- versus felony-related homicide was not re-fetched; the pattern itself is consistent with the Cohen & Nisbett 1994 and Baller et al. 2009 abstracts.
- Findings of Chu, Rivera & Loftin 2000 and Rivera, Chu & Loftin 2002 (herding and strong-communities tests) were not obtained (no abstract in Crossref or Semantic Scholar; publisher pages 403). Baller et al. 2009 is now confirmed as supportive at abstract level.
- Findings of Phillips & Cooney 2005 not obtained; Cooney's U-shape in authority is from a publisher-level summary.
- Whether Gould's thesis controls for exposure (how often equals meet) is unknown.
- Details of the three Leung & Cohen cultural logics' measurement and effect sizes.
- Sample sizes in Cohen et al. 1996 (degrees of freedom suggest about 80, 167 and 144 in the relevant tests, from the audit, not the paper).
- Brown, Osterman & Barnes' definition of an "honour state" and the effect sizes (only the headline "more than twice" and "more likely" are known).
- Whether the "Southerners politeness" finding (Cohen et al. 1999) couples to threshold or to provocation rate.

## Validation log (2026-10-29)

Every DOI was resolved at api.crossref.org; titles, authors, venue, volume, issue and pages checked against the record. Abstracts were read where Crossref or Semantic Scholar carried them. No primary full text could be fetched (deepblue, Sage, APA, OUP all 403/404), so nothing here is upgraded to [read] at full-text level. The web-search budget for this turn was exhausted before validation began, so the "nothing exists" claims (no replication or meta-analysis of the 1996 experiments; no quantitative threshold model) could **not** be re-tested by search; they stand as the original author's two-search result.

- ✓ Cohen, Nisbett, Bowdle & Schwarz 1996, JPSP 70(5) 945-960. ✎ credited the audit to its author (Ulrich Schimmack, Replication Index, 2019-01-11) and added its URL; chicken-game contrast described correctly as a +3,-1,-1,-1 focused contrast; distances (Northerners ~5 ft) added from the audit; noted the audit says no study of the three supports the anger claim. All [audit] numbers re-checked against the post and match.
- ✓ Nisbett & Cohen 1996 / 2018 reissue, DOI 10.4324/9780429501142.
- ✓ Nisbett 1993, Am. Psychologist 48(4) 441-449. Abstract not obtainable (elided by publisher).
- ✎ Cohen & Nisbett 1994, PSPB 20(5) 551-567: pages now Crossref-confirmed; abstract read and summarised.
- ✎ Cohen & Nisbett 1997, PSPB 23(11) 1188-1199: pages Crossref-confirmed. Study details still abstract-level.
- ✎ Chu, Rivera & Loftin 2000, Social Forces 78(3) 971-: page added. Findings still unconfirmed.
- ✎ Rivera, Chu & Loftin 2002, IJSSP 22(7/8) 109-121: volume and pages added. Findings unconfirmed.
- ✎ Baller, Zevenbergen & Messner 2009, JRCD 46(3) 275-300: DOI found and confirmed (10.1177/0022427809335164); abstract read, which shows it supports the herding thesis. Moved out of "content unconfirmed".
- ✎ Brown, Osterman & Barnes 2009, Psych. Sci. 20(11) 1400-1405: pages added; abstract read and matches the summary.
- ✓ IJzerman, van Dijk & Gallucci 2007, Emotion 7(4) 869-875 (venue and pages added). N = 42 and results unconfirmed.
- ✓ Gould 2003, Collision of Wills, DOI confirmed.
- ✎ Gould 2000, ASR 65(5) 682-704: pages confirmed; abstract read; wording tightened to the abstract ("nuclear family", targets chosen on specific acts of solidarity, "highly strategic yet altruistic").
- ✎ Gould 1999, ASR 64(3) 356-380: Crossref-confirmed.
- ✎ Stinchcombe 2004 AJS 110(1) 231-232 and Senechal de la Roche 2005 CS 34(1) 68-69: confirmed, pages added.
- ✓ Cooney 1998, Warriors and Peacemakers (DOI on the 2020 online edition; Crossref lists no author, publisher record does). U-shape claim still a summary.
- ✓ Phillips & Cooney 2005, ASR 70(2) 334-354. Abstract still unobtainable (elided).
- ✎ Cooney 1997, Criminology 35(3) 381-407: pages added.
- ✎ Leung & Cohen 2011, JPSP 100(3) 507-526: pages confirmed; abstract read; noted that the definitions of the three logics come from summaries, not the abstract.
- ✎ Gul, Cross & Uskul 2021, Am. Psychologist 76(3) 502-515: pages fixed (was "502-"); abstract read and confirms the summary; it adds "southern and western" and a Latinx section.
- ✎ Cohen, Vandello, Puente & Rantilla 1999, SPQ 62(3) 257-: first page added.
- ✎ Vandello & Cohen 2003, JPSP 84(5) 997-1010: pages added.
- ✎ Vandello, Cohen & Ransom 2008, JCCP 39(2) 162-177: volume, issue and pages added.
- ✎ Cohen, Vandello & Rantilla 1998, in Shame (OUP) 261-282: pages added.
- ? Michigan News 1997 summary and Russell Sage abstract page: Russell Sage page fetched (matches the summary; it lists Nisbett first). Michigan News not re-fetched.
- ? Cortisol percentages (+79/+42/+33%): not in the audit and not traceable; remain unconfirmed.

**Verdict.** The survey is sound and unusually honest about what it did not read: all 24 DOIs resolve to the works and authors claimed, and no fabrication was found. The fixes are bibliographic (pages, volumes, one missing DOI) and attributional (the audit is now credited to Schimmack); the one change of substance is that Baller et al. 2009, previously "unconfirmed", supports the herding thesis at abstract level. The claims of absence (no replication, no formal threshold model) were not re-tested this pass because the search budget was spent.

## Cross-checks (2026-10-29)

Checked against the other prior-work files by grep on authors, works, numbers and terms. Overlaps are confined to files 25, 39, 68 and 41; other hits (02 S. H. Gould on kinship, 10 Gouldner, 09 Ballerini) are different people or works. Web search was unavailable (budget used up), so the one tension below could not be checked at source.

**Agreements**
- 25 (section B2): same four citations for Nisbett & Cohen 1996 (DOI 10.4324/9780429501142), Cohen et al. 1996 (JPSP 70(5) 945-960), Leung & Cohen 2011 (JPSP 100(3) 507-526) match 058 sections 1, 2 and 5. Both say the herding-origin story is a historical inference and the experiments are unreplicated, with no replication found in one search. Both credit the Replication Index audit (2019).
- 25 (B2 Law and Translation): 25 has the low retaliation threshold as a cultural parameter, with `insult(a,b)` and `retaliate(b,a)` operators and a distribution over thresholds. 058 section 1 Translation and section 7 treat the threshold the same way, and 058 section 5 refines it into a function of (person, culture, situation).
- 25 (B2 Evidence): Leung & Cohen's typology "cuts against a reading of culture as one scalar". This agrees with 058 section 5.
- 39 (section 13): Gould 2003 DOI and the Stinchcombe 2004 AJS review match 058 section 3. Both say Gould is the one honour/feud source with a testable comparative static (conflict peaks where rank is ambiguous, between near-equals) and use the Corsican vendetta records. Both say the books were not opened.
- 39 (section 13) and 058 sections 3 and 7: both frame honour-driven retaliation as a repeating cycle that a third party or settlement operator must break. 39 uses `Avenge`/`Settle` (Boehm) and 058 uses `avenge`/`side_with`/`mediate` (Gould, Cooney).
- 68 (header): cross-references 58 as honour-culture retaliation thresholds. Consistent with 058's finding that there is no quantitative threshold. 068's Granovetter-form threshold theta_i gives a ready parameterisation, which 058 section 7 (`theta`) lacks.
- 41 (section E, revenge) and 21 (commitment-device emotions): treat retaliation as a deterrence/commitment mechanism. This agrees with the herding rationale in 058 section 2. These files do not cover the same works, so no numbers are comparable.
- 15 and 50: Reiss lists honor and vengeance as drives (50: "Reiss only", no independent support). No conflict with 058, which treats honour as a cultural threshold parameter and not a drive.

**Contradictions or tensions**
- 25 (section B2, Law) says that, per the abstract (via search snippet), Southern men "were more upset", while 058 section 1 says self-reported anger was not significant (p between .10 and .15) per the audit. Also, 25 says the audit found "some field-study differences" non-significant, while 058 says the audit's non-significant results are about the lab experiments. Verdict: unresolved, probably not a true contradiction. "Upset" in the abstract most likely refers to the cortisol rise and not to the anger self-report, but this could not be confirmed at source. 058's more specific wording (anger rating n.s.; cortisol and testosterone only in planned contrasts) is the safer one to cite. Neither file read the primary tables.
- 25 (B2) leaves the cortisol and testosterone rises as `[standard account, not read]`. 058 gives audit-sourced figures (testosterone +12% vs +4%/+6%/+4%; t(165) = 2.14 and 2.19) and flags the cortisol percentages as untraceable. This is a difference in sourcing depth, not a contradiction. 058 supersedes 25 for these numbers, with the audit as a secondary source.
- 39 (section 13) uses Gould's Corsican records to support "conflict is most likely where rank is ambiguous". 058 section 3 reads Gould (2000) as showing that revenge was rare and conditional on the group character of the original act, so "honour as an automatic low-threshold reflex" is contradicted. These are different Gould works (2003 book vs ASR 2000 paper) on the same data, and the claims are compatible. 39 does not mention the conditionality, so cite both together. No file is wrong.

No file contradicts 058 on any DOI, author list, page range or number. Files 43-57, 59-67, 69-82 contain no overlapping works.

## Licences of quoted and transcribed material (2026-10-30)

Audit verdicts for this file were all "check"; no text was changed. Checks: the Gould (2000) paragraph, the Gould (2003) and Cooney (1998) scope sentences are paraphrases in this file's own wording with the source labelled `[abstract/summary]`; the cited figures (30 societies, several dozen prisoners) are facts. The `-k` curl attempt described in the method note was blocked by the sandbox and not retried; no access control was bypassed and no paywalled text was obtained.

- **Crossref metadata** (DOIs, authors, volumes, pages, titles): facts; Crossref metadata is released as CC0. Used as citations only.
- **Cohen, Nisbett, Bowdle & Schwarz (1996), JPSP 70(5), abstract**: not determined; publisher copyright presumed (APA). Used as description of the procedure plus one single-word quotation (the insult word).
- **Schimmack (2019), Replication Index blog, "Social Psychology Textbook audiT: Culture of Honor"**: not determined; copyright presumed to the author. Used as dataset citation of test statistics (t, p, percentage changes), stated as numbers, no passages copied.
- **Nisbett & Cohen (1996), Nisbett (1993), Cohen & Nisbett (1994, 1997)**: not determined; publisher copyright presumed. Used as description of claims from summaries; nothing quoted.
- **Gould (2000), ASR 65(5), abstract**: not determined; publisher copyright presumed (SAGE). Used as description in this file's own words, with one three-word quotation ("highly strategic yet altruistic").
- **Gould (2003), *Collision of Wills*, publisher description**: not determined; publisher copyright presumed (University of Chicago Press). Used as description.
- **Cooney (1998), *Warriors and Peacemakers*; Phillips & Cooney (2005); Cooney (1997)**: not determined; publisher copyright presumed (NYU Press, ASA/SAGE, ASC/Wiley). Used as description of scope and claims; book-contents term "Black's Theoretical Paradigm" cited as a title.
- **Baller, Zevenbergen & Messner (2009), JRCD 46(3), abstract**: not determined; publisher copyright presumed (SAGE). Used as description with one short quotation ("highly consistent with the herding thesis").
- **Chu, Rivera & Loftin (2000); Rivera, Chu & Loftin (2002)**: citation only.
- **Leung & Cohen (2011), JPSP, abstract**: not determined; publisher copyright presumed (APA). Used as description of the result in the file's own words.
