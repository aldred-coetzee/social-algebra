# Prior work 22: neuroscience and physiology of social drives and their coupling

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: the biology of social drives, meaning what grounds a drive's existence, its set point, and its coupling between individuals. Serves the aim of an algebra of basic human and group drives that composes into equations, supports theorems, and is used to predict or control behaviour.

**Method note.** Every DOI below was confirmed against the Crossref API in this session (title, year and journal matched). No full text was read. Descriptions are **[from abstract/standard account]** unless a line says otherwise; nothing here is **[read]**. Effect sizes are quoted only where a search result stated them, and each says so. Replication notes come from search results and the field's standard account, not from my reading of replication papers. Items I could not tie to a confirmed record are in "Unconfirmed" at the end.

**Validation pass (2026-10-29).** A second agent re-checked every DOI in the draft (about 67) plus 11 added ones against Crossref, read abstracts (Europe PMC) for the key quantitative items, and read the relevant passages of the full text of Tomova 2020 and Walum 2016. Tags now used: **[read]** = the passage was read in the paper itself; **[abstract read]** = the abstract was read; anything else is as the original author left it. Corrections are marked "(corrected in validation)". The log is at the end.

**Summary.** Only one family of social drives has anything like a homeostatic grounding: the need for social contact (rodent circuit work, two small human deprivation studies, and a large loneliness literature). It has a detector, a set point in the framing, and an effector in animals; since 2025 it also has a mouse circuit for the *satiety* side (Liu et al. 2025, added in validation), and the human craving result is weaker than first reported here (its preregistered brain test was null; see A2). Everything else splits into three groups. (1) Solid in animals, thin in humans: social defeat, observational fear learning, social buffering. (2) Real but small, and oversold: oxytocin, the dual-hormone hypothesis, social-pain overlap, mirror neurons. (3) Coupling between individuals at the brain level (hyperscanning) has correlational results, a live methodological critique, and no causal operator. Nothing here gives a numeric coupling coefficient between two people's drive states that could be used as an algebra constant. The closest are behavioural, not neural.

---

## A. Social contact as a homeostatic need

### A1. Matthews & Tye 2019: social homeostasis

**Citation.** Matthews, G. A. & Tye, K. M. (2019). Neural mechanisms of social homeostasis. *Annals of the New York Academy of Sciences* 1457, 5-25. DOI 10.1111/nyas.14016 (confirmed). Open copy: PMC7593988.

- **Drive supported.** Social contact / belonging, as a regulated quantity.
- **Structure [from abstract/standard account].** Three-part control loop borrowed from energy and fluid balance: a detector of the quantity and quality of social contact, a control centre that compares it with a set point, and effectors that raise or lower social seeking. Later papers (Lee, C. R., Chen, A. & Tye, K. M. (2021), The neural circuitry of social homeostasis: consequences of acute versus chronic social isolation, *Cell* 184, 1500-1516, DOI 10.1016/j.cell.2021.02.028, confirmed in validation, PMC8580010; Bales et al. 2023, PMC10036751, not re-checked) restate it this way and ask what sets an individual's set point. Lee et al. 2021 [abstract read] add two things the algebra needs: contact is negative-valence when in **excess**, not only positive when deficient (a two-sided set point), and chronic deficit **moves the set point**, so that the old optimum is then experienced as surplus. The review is a framework and a proposal, built on rodent isolation work; the abstract says parallel overlapping circuits are proposed, not shown. Tye's lab reports dorsal raphe dopamine neurons in mice becoming more responsive to social contact after isolation, offered as a candidate effector (Matthews, G. A. et al. (2016), Dorsal raphe dopamine neurons represent the experience of social isolation, *Cell* 164, 617-631, DOI 10.1016/j.cell.2015.12.040, added and confirmed in validation).
- **Added in validation: Liu, D. et al. (2025).** A hypothalamic circuit underlying the dynamic control of social homeostasis. *Nature* 640, 1000-1010. DOI 10.1038/s41586-025-08617-8 (confirmed; Dulac lab). [abstract read] Two previously uncharacterised neuron populations in the mouse preoptic hypothalamus, one active during isolation and driving social need, the other active during reunion "rebound" and driving **social satiety**; the two are directly connected; mice need touch to register others' presence and fulfil the need; strain differences in isolation sensitivity (FVB/NJ high, C57BL/6J moderate). This is the strongest circuit evidence for a homeostatic loop with both a need and a satiety arm, from a second lab independent of Tye's. Still mouse only.
- **Coupling between individuals.** None in the framework itself. The partner is a source of the input signal.
- **Replication standing.** Rodent isolation-circuit findings were single-lab-heavy (the Tye lab) until Liu et al. 2025 (Dulac lab) found a different, hypothalamic, node of the same loop. The framework is a hypothesis with good analogies and no human quantification of the set point.
- **Operand/operator.** Operand: a person with state variable `c` (contact level) and set point `c*`, deficit `d = c* - c`. Operators: an affiliation act by or toward the person raises `c`; isolation lets `c` decay. The deficit drives approach acts, exactly as hunger drives eating. This is the cleanest biological primitive in the cluster.

### A2. Tomova et al. 2020: social craving after isolation

**Citation.** Tomova, L., Wang, K. L., Thompson, T., Matthews, G. A., Takahashi, A., Tye, K. M. & Saxe, R. (2020). Acute social isolation evokes midbrain craving responses similar to hunger. *Nature Neuroscience* 23, 1597-1605. DOI 10.1038/s41593-020-00742-z (confirmed; an author correction exists, 10.1038/s41593-021-01004-2).

- **Design [read].** Within-subject, N=40 (27 women), 18-40 years, socially connected (people living alone or scoring high on loneliness were excluded, per the preprint). 10 hours alone with no social media, email or fiction, versus 10 hours fasting, and a baseline day, each followed by fMRI with food, social and control (flower) cues. Preregistered on OSF (osf.io/cwg9e).
- **Result [read] (corrected in validation).** Self-report after isolation versus its start: social craving t(39) = 5.00, loneliness 5.17, discomfort 5.57, dislike of isolation 4.13, happiness −4.21, all p < .001; 36 of 40 felt lonelier. For comparison, food craving after fasting was t(36) = 17.40, so the social deficit is real but far weaker on this measure than hunger. **The preregistered brain test was null:** in the anatomically defined SN/VTA, responses to social cues were not higher after isolation than after fasting (b = 0.006, P = 0.50), while food cues after fasting were (P = 0.002). The isolation effect for social cues appeared only in an **exploratory** functionally localised midbrain ROI. Within the anatomical SN/VTA, the response to social cues correlated with one craving measure (questionnaire, r(38) = 0.36, P = 0.011) but not the other (in-task rating, r = 0.054). Multivoxel decoding trained on food-after-fasting generalised to social-after-isolation. Striatal and cortical patterns separated food from social craving. The earlier wording here ("midbrain response resembled the food response") follows the abstract and overstates the preregistered result.
- **Set point / quantitative structure.** Dose-response in time is not mapped: one duration (10 hours), one condition. It shows a deficit state exists and is cue-reactive; it does not give a decay rate, a ceiling, or a satiation curve.
- **Replication standing.** No independent fMRI replication found. The self-report part is partly echoed by **Stijovic, A. et al. (2023)**, Homeostatic regulation of energetic arousal during acute social isolation: evidence from the lab and the field, *Psychological Science* 34, 537-551, DOI 10.1177/09567976231156413 (added and confirmed in validation) [abstract read]: 8 h isolation versus 8 h food deprivation in the lab (N = 30 women) lowered energetic arousal and raised fatigue comparably to fasting; a preregistered COVID-lockdown field study (N = 87) replicated the energy drop only for people living alone or high in sociability. The craving ratings are the solid part; the midbrain result is the fragile part (null in the preregistered ROI).
- **Operand/operator.** Supports `d` growing with time since contact, and a "cue" operator (seeing social cues) that reads out `d`. Does not support quantitative parameters.

### A3. Cacioppo: loneliness as an aversive signal

**Citations.**
- Cacioppo, J. T. & Cacioppo, S. (2018). Loneliness in the modern age: an evolutionary theory of loneliness (ETL). *Advances in Experimental Social Psychology* 58, 127-197. DOI 10.1016/bs.aesp.2018.03.003 (confirmed; an uncertain five-author attribution in the first draft removed in validation).
- Cacioppo, J. T. & Hawkley, L. C. (2009). Perceived social isolation and cognition. *Trends in Cognitive Sciences* 13, 447-454. DOI 10.1016/j.tics.2009.06.005 (confirmed).
- Hawkley, L. C. & Cacioppo, J. T. (2010). Loneliness matters. *Annals of Behavioral Medicine* 40, 218-227. DOI 10.1007/s12160-010-9210-8 (confirmed).
- Cacioppo, J. T. et al. (2009). In the eye of the beholder: individual differences in perceived social isolation predict regional brain activation to social stimuli. *J. Cognitive Neuroscience* 21, 83-92. DOI 10.1162/jocn.2009.21007 (confirmed).
- Holt-Lunstad, J., Smith, T. B. & Layton, J. B. (2010). Social relationships and mortality risk: a meta-analytic review. *PLoS Medicine* 7(7), e1000316. DOI 10.1371/journal.pmed.1000316 (confirmed).
- Baumeister, R. F. & Leary, M. R. (1995). The need to belong. *Psychological Bulletin* 117, 497-529. DOI 10.1037/0033-2909.117.3.497 (confirmed).

- **Drive supported.** Belonging, framed as a signal like hunger or thirst. ETL [from abstract/standard account]: loneliness is an aversive state that motivates repair of social connection, like pain motivates protection of the body; it also raises threat vigilance (Cacioppo & Hawkley 2009).
- **Quantitative structure.** The UCLA Loneliness Scale is a continuous measure. The set point is subjective (perceived, not objective, isolation), which is the key finding: the same objective contact gives different deficit depending on the person's expectation. That fits a person-specific `c*`. Heritability of loneliness is reported in the ETL line of work (twin studies; Spithoven, A. W. M., Cacioppo, S., Goossens, L. & Cacioppo, J. T. (2019), *Perspectives on Psychological Science* 14, 376-396, DOI 10.1177/1745691618812684 is the genetics paper; I did not read its figures).
- **Mortality figure [abstract read].** Holt-Lunstad 2010: across 148 studies (308,849 participants), random-effects OR = 1.50 (95% CI 1.42-1.59) for survival with stronger social relationships. Observational; confounded by health and by measure. Strong as population-level evidence that contact matters; weak as evidence for a specific mechanism.
- **Replication standing.** Epidemiological associations are robust and large in number. The brain-imaging findings (e.g. reduced ventral striatum response to pleasant social pictures in the lonely, from the 2009 paper) are small-sample fMRI; I know of no preregistered replication. The ETL itself is a theory, not tested by intervention.
- **Operand/operator.** Loneliness is the felt readout of `d`. It also feeds a second variable, threat vigilance, which couples the belonging drive to the fear drive (a cross-drive operator: raising `d` raises sensitivity to threat cues). This is the best-supported drive-to-drive coupling found in this cluster, but "best-supported" here means correlational.

### A4. Social baseline theory

**Citations.**
- Beckes, L. & Coan, J. A. (2011). Social baseline theory: the role of social proximity in emotion and economy of action. *Social and Personality Psychology Compass* 5, 976-988. DOI 10.1111/j.1751-9004.2011.00400.x (confirmed).
- Coan, J. A., Schaefer, H. S. & Davidson, R. J. (2006). Lending a hand: social regulation of the neural response to threat. *Psychological Science* 17, 1032-1039. DOI 10.1111/j.1467-9280.2006.01832.x (confirmed).
- Saxbe, D. E., Beckes, L., Stoycos, S. A. & Coan, J. A. (2020; online 2019). Social allostasis and social allostatic load. *Perspectives on Psychological Science* 15, 469-482. DOI 10.1177/1745691619876528 (confirmed).
- Hostinar, C. E., Sullivan, R. M. & Gunnar, M. R. (2014). Psychobiological mechanisms underlying the social buffering of the HPA axis. *Psychological Bulletin* 140, 256-282. DOI 10.1037/a0032671 (confirmed).

- **Claim [from abstract/standard account].** The brain's default assumption is proximity to others, so company lowers the metabolic cost of coping: threat is cheaper to meet with others present. Coan 2006 (small fMRI study, married women, spouse's hand held): reduced threat-region activation to the threat cue with the spouse's hand, less with a stranger's; the effect scaled with reported marital quality (in right anterior insula, superior frontal gyrus and hypothalamus, spouse condition only). N = 16 married women [abstract read].
- **Saxbe et al. 2020 (abstract-level, via search).** Social groups act as regulatory systems; allostatic load can accumulate inside groups, not only individuals, and the paper offers a model for how relationship dysfunction operates through that. This is the closest published thing to a group-level drive variable with a cost term.
- **Coupling between individuals.** A buffering operator: presence of a partner scales down the partner's threat response. In animals this is replicated widely (Hennessy et al. 2009, DOI 10.1016/j.yfrne.2009.06.001; Kikusui et al. 2006, DOI 10.1098/rstb.2006.1941, both confirmed, not read). In humans Hostinar et al. is a review of cortisol-buffering studies, with mixed effects and strong dependence on relationship type and age.
- **Replication standing.** The animal buffering literature is broad. The human fMRI hand-holding result is small-N and, to my knowledge, not been replicated at scale. The economy-of-action framing is a theory.
- **Operand/operator.** Operator: `buffer(partner, person)` multiplies the person's threat-response gain by a factor below 1, with the factor depending on relationship quality. Group-level: allostatic load as a summed cost over a group's members. Neither has a published fitted parameter.

### A5. Social pain and the pain overlap

**Citations.**
- Eisenberger, N. I., Lieberman, M. D. & Williams, K. D. (2003). Does rejection hurt? An fMRI study of social exclusion. *Science* 302, 290-292. DOI 10.1126/science.1089134 (confirmed).
- Eisenberger, N. I. (2012). The neural bases of social pain. *Psychosomatic Medicine* 74, 126-135. DOI 10.1097/psy.0b013e3182464dd1 (confirmed). Also Eisenberger (2015), *Annual Review of Psychology* 66, DOI 10.1146/annurev-psych-010213-115146 (confirmed).
- Kross, E. et al. (2011). Social rejection shares somatosensory representations with physical pain. *PNAS* 108, 6270-6275. DOI 10.1073/pnas.1102693108 (confirmed).
- Woo, C.-W. et al. (2014). Separate neural representations for physical pain and social rejection. *Nature Communications* 5, 5380. DOI 10.1038/ncomms6380 (confirmed).
- Iannetti, G. D., Salomons, T. V., Moayedi, M., Mouraux, A. & Davis, K. D. (2013). Beyond metaphor: contrasting mechanisms of social and physical pain. *Trends in Cognitive Sciences* 17, 371-378. DOI 10.1016/j.tics.2013.06.002 (confirmed).
- Lieberman, M. D. & Eisenberger, N. I. (2015). The dorsal anterior cingulate cortex is selective for pain. *PNAS* 112, 15250-15255. DOI 10.1073/pnas.1515083112 (confirmed).

- **Claim.** Exclusion activates dACC (and anterior insula) as physical pain does; so social disconnection uses the pain alarm system, and loneliness and rejection "hurt". [from abstract/standard account]
- **Critique and standing.** The overlap claim rests on reverse inference from dACC activation, which responds to many things. Woo 2014 [abstract read]: trained pattern classifiers on 60 participants (heat pain versus warmth, ex-partner photos versus friend photos) separated each condition from its control at 92% (pain) and 80% (rejection) in out-of-sample individuals, each classifier at chance on the other condition, the two representations uncorrelated even in dACC, and with distinct resting-state connectivity in a separate sample (N = 91). Note the rejection manipulation was viewing an ex-partner after an unwanted break-up, not Cyberball exclusion. That is strong evidence against identical neural substrates, though it leaves open that both feed a common affective system. Iannetti et al. 2013 argue the overlap is metaphor-level. Lieberman & Eisenberger 2015 argue the other way with large-scale meta-analytic reverse inference. This is an unresolved dispute; the weight of the pattern-classifier evidence now favours "overlapping alarm function, distinct representations".
- **Operand/operator.** What is usable for the algebra is not shared anatomy but the functional claim: exclusion acts raise an aversive signal in the target, which motivates repair. That claim is supported behaviourally (a large ostracism literature, not surveyed here) independent of the dACC dispute. Operator: `exclude(a, b)` raises `d` in b.

---

## B. Neuropeptides and hormones

### B1. Oxytocin and vasopressin

**Citations.**
- Kosfeld, M., Heinrichs, M., Zak, P. J., Fischbacher, U. & Fehr, E. (2005). Oxytocin increases trust in humans. *Nature* 435, 673-676. DOI 10.1038/nature03701 (confirmed).
- Walum, H., Waldman, I. D. & Young, L. J. (2016). Statistical and methodological considerations for the interpretation of intranasal oxytocin studies. *Biological Psychiatry* 79, 251-257. DOI 10.1016/j.biopsych.2015.06.016 (confirmed).
- Nave, G., Camerer, C. & McCullough, M. (2015). Does oxytocin increase trust in humans? A critical review of research. *Perspectives on Psychological Science* 10, 772-789. DOI 10.1177/1745691615600138 (confirmed).
- Lane, A., Luminet, O., Nave, G. & Mikolajczak, M. (2016). Is there a publication bias in behavioural intranasal oxytocin research on humans? *J. Neuroendocrinology* 28. DOI 10.1111/jne.12384 (confirmed).
- Leng, G. & Ludwig, M. (2016). Intranasal oxytocin: myths and delusions. *Biological Psychiatry* 79, 243-250. DOI 10.1016/j.biopsych.2015.05.003 (confirmed).
- Mierop, A. et al. (2020). How can intranasal oxytocin research be trusted? *Perspectives on Psychological Science* 15. DOI 10.1177/1745691620921525 (confirmed).
- Young, L. J. & Wang, Z. (2004). The neurobiology of pair bonding. *Nature Neuroscience* 7, 1048-1054. DOI 10.1038/nn1327 (confirmed). Insel, T. R. & Young, L. J. (2001). The neurobiology of attachment. *Nat. Rev. Neurosci.* 2, 129-136. DOI 10.1038/35053579 (confirmed).
- Heinrichs, M. et al. (2003). Social support and oxytocin interact to suppress cortisol and subjective responses to psychosocial stress. *Biological Psychiatry* 54, 1389-1398. DOI 10.1016/s0006-3223(03)00465-7 (confirmed).
- Feldman, R. (2017). The neurobiology of human attachments. *Trends in Cognitive Sciences* 21, 80-99. DOI 10.1016/j.tics.2016.11.007 (confirmed).

- **What is solid.** In prairie voles, oxytocin and vasopressin receptor systems underpin pair bonding (Young & Wang 2004; Insel & Young 2001 [standard account]); this is a genuine animal result, not that human social behaviour follows from it. In humans, oxytocin has real roles in birth and lactation, and endogenous oxytocin is linked to parent-infant synchrony (Feldman, Gordon & Zagoory-Sharon, *Developmental Science* 14, 752-761, online 2010, print 2011, DOI 10.1111/j.1467-7687.2010.01021.x, confirmed, not read), though plasma and salivary assay validity is itself disputed.
- **What failed (corrected in validation).** Intranasal oxytocin as a switch for trust, cooperation or social cognition in humans. **Walum et al. 2016 [read]** is the source of the power figures: from published meta-analyses they take a sample-weighted mean effect of d = 0.28 and a median N of 49 for healthy-subject studies, giving average power of **16%** (12% for clinical trials, median N 26, d = 0.32); 80% power would need N ≈ 352. With prestudy odds R = 0.10, the positive predictive value is **at most 24%** before any bias, falling to 17% with ten uncorrected tests; they conclude most published intranasal findings likely do not represent true effects. (The first draft attributed the 16% to Lane et al.; that was wrong.) **Lane et al. 2016 [abstract read]** is a file-drawer confession from one lab: eight studies on 453 subjects (2009-2014), only five publications, only one reporting a null. **Mierop et al. 2020 [abstract read]**: in a systematic review of interactive intranasal effects in healthy samples, replications were rarely attempted and largely unsuccessful, significance was unrelated to sample size, and power was critically low. Nave et al. 2015 conclude the trust effect is not supported. Leng & Ludwig 2016 add that little intranasal oxytocin may reach the brain.
- **Coupling.** The key remaining claim is that hormones are a channel between people (touch, gaze, parenting raise oxytocin in both). Evidence is correlational in the parent-infant case, with assay doubts.
- **Operand/operator.** Not usable as a numeric operator on humans. Safe statement: a hormone can mediate a pair-bond variable in voles. Anything of the form "oxytocin level X gives trust Y" should not enter the algebra.

### B2. Dopamine and social reward / status

**Citations.**
- Zink, C. F. et al. (2008). Know your place: neural processing of social hierarchy in humans. *Neuron* 58, 273-283. DOI 10.1016/j.neuron.2008.01.025 (confirmed).
- Izuma, K., Saito, D. N. & Sadato, N. (2008). Processing of social and monetary rewards in the human striatum. *Neuron* 58, 284-294. DOI 10.1016/j.neuron.2008.03.020 (confirmed).
- Meshi, D., Morawetz, C. & Heekeren, H. R. (2013). Nucleus accumbens response to gains in reputation for the self relative to gains for others predicts social media use. *Frontiers in Human Neuroscience* 7, 439. DOI 10.3389/fnhum.2013.00439 (confirmed).
- Rilling, J. K. et al. (2002). A neural basis for social cooperation. *Neuron* 35, 395-405. DOI 10.1016/s0896-6273(02)00755-9 (confirmed).

- **Claim (corrected in validation).** Striatal reward regions respond to social rewards (reputation, cooperation) much as to money: Izuma et al. 2008 [abstract read], N = 19, found that gaining a good reputation activated the striatum, overlapping monetary reward ("common neural currency"). Zink et al. 2008 [abstract read] is about *perceiving others' rank*, not about the viewer's own rank: in a simulated hierarchy, viewing a **superior** player engaged attention and salience systems and dorsolateral prefrontal cortex; in an **unstable** hierarchy amygdala and medial prefrontal cortex were added; and the hierarchical consequences of one's performance were of comparable salience to monetary reward. The first draft's "depended on the viewer's own rank" is not what the abstract says. So a status/approval drive may use the general reward system rather than a dedicated circuit.
- **Standing.** Small-N fMRI (Izuma N = 19; Zink N not checked). Replication of the specific rank-by-stability interaction: none that I found. The broader claim that social rewards activate the striatum has multiple supporting studies and is the best-supported item here, but it is the weakest kind of grounding for an algebra: it says social reward is reward, not what the set point or coupling is.
- **Operand/operator.** Operator: `approve(a, b)` is a reward to b (Izuma). Zink supports a separate salience term: others of higher rank, and any rank in an unstable hierarchy, draw more processing. Whether approval from a higher-ranked a is worth more is plausible but not what these papers tested. Quantities undefined.
- **Is status homeostatic? (added in validation).** Anderson, C., Hildreth, J. A. D. & Howland, L. (2015), Is the desire for status a fundamental human motive? *Psychological Bulletin* 141, 574-601, DOI 10.1037/a0038781 (confirmed) [abstract read], argue status is a fundamental motive, distinct from belonging, with well-being depending on status accorded by others. Nothing in it is a set point. A follow-up, Anderson, Hildreth & Sharps (2020), The possession of high status strengthens the status motive, *PSPB* 46, 1712-1723, DOI 10.1177/0146167220937544 (confirmed; title only, not read), reports the opposite of satiation: having status raises the desire for it. If that holds, status behaves like an appetite that grows with consumption, not a homeostatic need, which supports the survey's line that status has no set point.

### B3. Testosterone-cortisol and status

**Citations.**
- Mehta, P. H. & Josephs, R. A. (2010). Testosterone and cortisol jointly regulate dominance: evidence for a dual-hormone hypothesis. *Hormones and Behavior* 58, 898-906. DOI 10.1016/j.yhbeh.2010.08.020 (confirmed).
- Dekkers, T. J., van Rentergem, J. A. A., Meijer, B., Popma, A., Wagemaker, E., Huizenga, H. M. (2019). A meta-analytical evaluation of the dual-hormone hypothesis. *Neuroscience & Biobehavioral Reviews* 96, 250-271. DOI 10.1016/j.neubiorev.2018.12.004 (confirmed; author list confirmed in validation).
- Knight, E. L., Sarkar, A., Prasad, S. & Mehta, P. H. (2020). Beyond the challenge hypothesis: the emergence of the dual-hormone hypothesis and recommendations for future research. *Hormones and Behavior* 123, 104657. DOI 10.1016/j.yhbeh.2019.104657 (confirmed; author list confirmed in validation).
- Eisenegger, C. et al. (2010). Prejudice and truth about the effect of testosterone on human bargaining behaviour. *Nature* 463, 356-359. DOI 10.1038/nature08711 (confirmed). Eisenegger, Haushofer & Fehr (2011), *Trends in Cognitive Sciences* 15, 263-271. DOI 10.1016/j.tics.2011.04.008 (confirmed).
- Mazur, A. & Booth, A. (1998). Testosterone and dominance in men. *Behavioral and Brain Sciences* 21, 353-363. DOI 10.1017/s0140525x98001228 (confirmed).

- **Claim [standard account].** Testosterone relates to status-seeking mainly when cortisol is low; with high cortisol the relation weakens or reverses. Mehta & Josephs 2010: a first demonstration in decision-making competition.
- **Standing.** The meta-analysis (Dekkers et al. 2019) [abstract read]: 30 papers, 33 studies, 49 effect sizes, n = 8,538; outcomes pooled across status, dominance, risk taking, aggression and psychopathy; testosterone × cortisol interaction significant but very small, r = −.061 (p = .026), corroborated by simple-slope meta-analyses; "only marginal support". Robustness analyses showed signs of publication bias, significance inflated by analytic flexibility, and underpowered studies; the authors call for a large preregistered study. Effects were largest for direct status measures (not significantly different from other outcomes) and "seemed larger" for men. This is weak support, and the small effect is at the edge of what bias alone could produce. Be blunt: the dual-hormone hypothesis is not an established mechanism. Eisenegger 2010 (testosterone and fair bargaining offers, expectation effects) is a placebo-controlled result that undercut the popular "testosterone means aggression" account; its own replication record I did not check.
- **Operand/operator.** A status-seeking drive modulated by two hormonal gains is a tidy equation with no empirical coefficient. Do not use as a model.

---

## C. Coupling between individuals

### C1. Hyperscanning and inter-brain synchrony

**Citations.**
- Hasson, U., Ghazanfar, A. A., Galantucci, B., Garrod, S. & Keysers, C. (2012). Brain-to-brain coupling: a mechanism for creating and sharing a social world. *Trends in Cognitive Sciences* 16, 114-121. DOI 10.1016/j.tics.2011.12.007 (confirmed).
- Stephens, G. J., Silbert, L. J. & Hasson, U. (2010). Speaker-listener neural coupling underlies successful communication. *PNAS* 107, 14425-14430. DOI 10.1073/pnas.1008662107 (confirmed).
- Dikker, S. et al. (2017). Brain-to-brain synchrony tracks real-world dynamic group interactions in the classroom. *Current Biology* 27, 1375-1380. DOI 10.1016/j.cub.2017.04.002 (confirmed). Commentary: Parada, F. J. & Rossi, A. (2017), *Frontiers in Human Neuroscience* 11, DOI 10.3389/fnhum.2017.00554 (confirmed; second author added in validation).
- Bevilacqua, D. et al. (2019). Brain-to-brain synchrony and learning outcomes vary by student-teacher dynamics. *J. Cognitive Neuroscience* 31, 401-411. DOI 10.1162/jocn_a_01274 (confirmed).
- Dumas, G. et al. (2010). Inter-brain synchronization during social interaction. *PLoS ONE* 5, e12166. DOI 10.1371/journal.pone.0012166 (confirmed).
- Pérez, A., Carreiras, M. & Duñabeitia, J. A. (2017). Brain-to-brain entrainment. *Scientific Reports* 7. DOI 10.1038/s41598-017-04464-4 (confirmed).
- Hamilton, A. F. de C. (2021). Hyperscanning: beyond the hype. *Neuron* 109, 404-407. DOI 10.1016/j.neuron.2020.11.008 (confirmed).
- Schilbach, L. et al. (2013). Toward a second-person neuroscience. *Behavioral and Brain Sciences* 36, 393-414. DOI 10.1017/s0140525x12000660 (confirmed).
- Nastase, S. A., Goldstein, A. & Hasson, U. (2020). Keep it real. *NeuroImage* 222, 117254. DOI 10.1016/j.neuroimage.2020.117254 (confirmed).

- **What was measured.** Stephens 2010: listener brain activity follows the speaker's with a lag, and greater coupling predicts better comprehension (the central result; effect sizes not retrieved). Dikker 2017 [abstract read]: portable EEG on **one class of 12** high-school students across 11 classes in a semester; group synchrony predicted class engagement and "social dynamics", which the authors attribute to shared attention (the link to ratings of teacher and classmates is from a search summary, not read). Hasson et al. 2012 [abstract read] is a programmatic call for a multi-brain frame of reference (coupling via a signal transmitted through the environment), not a data paper. Bevilacqua 2019: synchrony with the teacher predicted learning outcomes, moderated by student-teacher closeness.
- **Critique.** Hamilton 2021 (abstract-level): hyperscanning is hard to interpret; the same stimulus drives both brains, so synchrony can be shared input rather than interaction; analyses need behavioural data and mutual-prediction models. Parada 2017 commented on Dikker's classroom study. Nastase et al. argue for ecological realism, which cuts against the controlled designs behind much of this evidence.
- **Replication.** Mixed. Real-world EEG synchrony has a low signal-to-noise ratio and many analysis choices. I did not find a preregistered replication of Dikker 2017, whose N of 12 in one classroom makes it a demonstration, not an estimate.
- **Operand/operator.** What it supports: a quantity "alignment between a and b" that rises with shared attention and correlates with engagement. What it does not: a causal operator that one person applies to move another's drive. For the algebra it is a candidate measure of coupling strength, not a rule for how drives move.

### C2. Mirror neurons

**Citations.**
- Rizzolatti, G. & Craighero, L. (2004). The mirror-neuron system. *Annual Review of Neuroscience* 27, 169-192. DOI 10.1146/annurev.neuro.27.070203.144230 (confirmed).
- Gallese, V., Fadiga, L., Fogassi, L. & Rizzolatti, G. (1996). Action recognition in the premotor cortex. *Brain* 119, 593-609. DOI 10.1093/brain/119.2.593 (confirmed).
- Gallese, V. & Goldman, A. (1998). Mirror neurons and the simulation theory of mind-reading. *Trends in Cognitive Sciences* 2, 493-501. DOI 10.1016/s1364-6613(98)01262-5 (confirmed).
- Hickok, G. (2009). Eight problems for the mirror neuron theory of action understanding in monkeys and humans. *J. Cognitive Neuroscience* 21, 1229-1243. DOI 10.1162/jocn.2009.21189 (confirmed). Book-length: Hickok (2014), *The Myth of Mirror Neurons* (found by search, a trade book, no DOI).
- Keysers, C. & Gazzola, V. (2014). Hebbian learning and predictive mirror neurons for actions, sensations and emotions. *Phil. Trans. R. Soc. B* 369. DOI 10.1098/rstb.2013.0175 (confirmed).

- **Claim and overclaim.** Neurons in macaque premotor cortex fire both when the animal acts and when it sees the action. The strong form, that mirror neurons explain action understanding, empathy and social cognition, was widely repeated. Hickok's critique (reviewers' summaries only; I did not retrieve the 2009 abstract) says the evidence does not support it and the theory is probably wrong in its strong form. Single-neuron recordings in humans are rare; most human "mirror system" claims are fMRI.
- **Standing.** Weak as a foundation for empathy or emotion contagion. The macaque finding stands as a finding; the explanatory role is contested.
- **Operand/operator.** Do not use as the basis for a contagion operator. If an algebra needs "observing a's act elicits a matching state in b", ground it in behavioural contagion and observational learning (D below), not mirror neurons.

---

## D. Fear transmission and social stress

### D1. Observational fear learning

**Citations.**
- Olsson, A. & Phelps, E. A. (2007). Social learning of fear. *Nature Neuroscience* 10, 1095-1102. DOI 10.1038/nn1968 (confirmed).
- Olsson, A., Nearing, K. I. & Phelps, E. A. (2007). Learning fears by observing others: the neural systems of social fear transmission. *SCAN* 2, 3-11. DOI 10.1093/scan/nsm005 (confirmed).
- Olsson, A., Knapska, E. & Lindström, B. (2020). The neural and computational systems of social learning. *Nature Reviews Neuroscience* 21, 197-212. DOI 10.1038/s41583-020-0276-4 (confirmed; author list from memory).
- Haaker, J., Golkar, A., Selbing, I. & Olsson, A. (2017). Assessment of social transmission of threats in humans using observational fear conditioning. *Nature Protocols* 12, 1378-1386. DOI 10.1038/nprot.2017.027 (confirmed; the first draft's co-authors "Maren, Andreatta" were wrong and are corrected in validation).
- Added in validation: Lindström, B., Haaker, J. & Olsson, A. (2018). A common neural network differentially mediates direct and social fear learning. *NeuroImage* 167, 121-129. DOI 10.1016/j.neuroimage.2017.11.039 (confirmed).
- Added in validation: Lindström, B., Golkar, A., Jangard, S., Tobler, P. N. & Olsson, A. (2019). Social threat learning transfers to decision making in humans. *PNAS* 116, 4732-4737. DOI 10.1073/pnas.1810180116 (confirmed).
- Added in validation: Golkar, A., Castro, V. & Olsson, A. (2015). Social learning of fear and safety is determined by the demonstrator's racial group. *Biology Letters* 11, 20140817. DOI 10.1098/rsbl.2014.0817 (confirmed).
- Moved, not a fear paper: Lockwood, P. L., Apps, M. A. J., Valton, V., Viding, E. & Roiser, J. P. (2016). Neurocomputational mechanisms of prosocial learning and links to empathy. *PNAS* 113, 9763-9768. DOI 10.1073/pnas.1603198113 (confirmed). See "Vicarious and prosocial reward" below.

- **Claim [abstract read for Olsson & Phelps 2007 and Olsson, Nearing & Phelps 2007].** A person who watches another receive an aversive stimulus after a cue acquires a conditioned fear response to the cue, with amygdala involvement when observing and when later expressing the fear; learning by instruction produces a similar response but recruits additional (language, explicit-memory) systems. Note that Olsson & Phelps 2007 (*Nat. Neurosci.*) is a **review** proposing a modified conditioning model, not an experiment; the experiment is Olsson, Nearing & Phelps 2007 (*SCAN*). **(Corrected in validation.)** The first draft credited Olsson & Phelps 2007 with a group-membership effect. The empirical source is **Golkar, Castro & Olsson 2015** [abstract read]: in two observational-learning experiments, both fear and safety learning from a racial **in-group** demonstrator were more potent than from an out-group demonstrator.
- **Quantitative structure (corrected in validation).** Fear conditioning has formal learning models (Rescorla-Wagner, Pearce-Hall). The fitted models for *observational fear* are from the Olsson lab: **Lindström, Haaker & Olsson 2018** [abstract read] found direct and social fear learning behaviourally indistinguishable and served by the same amygdala / anterior insula / ACC network, but with different input (amygdala for direct, anterior insula for social), using dynamic causal modelling combined with reinforcement-learning models in which the insula gates learning by surprise (associability). **Lindström et al. 2019** [abstract read], three experiments, n = 120: observational and instructed threat learning both transfer to instrumental avoidance "in a strong and surprisingly inflexible manner", and computational modelling shows different mechanisms for the two. Olsson, Knapska & Lindström 2020 review the computational framing. Parameter values were not retrieved from any of these.
  **Lockwood et al. 2016 is not fear learning** and the first draft was wrong to cite it here: it is reward learning on behalf of another person (participants learned which stimuli earned rewards for self, for another person, or no one). People learned more slowly for others; trait empathy predicted faster prosocial learning and a more selective subgenual ACC prediction error [abstract read].
- **Replication standing.** Fear-conditioning methods are reproducible in principle, and observational fear learning has multiple labs in humans and rodents. Individual-differences claims (empathy and learning rate) are small-sample.
- **Operand/operator.** This is the clearest example of a drive-transmitting operator in the cluster: `observe(b, a's reaction to cue x)` sets b's fear association for x, with a gain that depends on a's identity relative to b (in-group, per Golkar et al. 2015; kin is untested here). Parameterisable in principle from the Olsson lab's fitted reinforcement-learning models (values not yet extracted). The one place where "transmission" is not a metaphor.

### D1b. Vicarious and prosocial reward (split out in validation)

- Lockwood et al. 2016 (citation above). [abstract read] A reinforcement-learning model with separate self and other conditions: learning to benefit another is slower than learning to benefit oneself, and its rate rises with trait empathy. Single study, fMRI.
- **Operand/operator.** Supports a `help(b, a)` learning term whose rate is a person parameter (empathy), smaller than the self-reward rate. It is a statement about learning *for* another, not about a drive passing *from* another, so it does not belong with fear transmission.

### D2. Social defeat and social stress in animals

**Citations.**
- Golden, S. A., Covington, H. E., Berton, O. & Russo, S. J. (2011). A standardized protocol for repeated social defeat stress in mice. *Nature Protocols* 6, 1183-1191. DOI 10.1038/nprot.2011.361 (confirmed; author list confirmed in validation).
- Krishnan, V., Han, M.-H., Graham, D. L., Berton, O., Renthal, W., Russo, S. J., LaPlant, Q., Graham, A. et al. (2007). Molecular adaptations underlying susceptibility and resistance to social defeat in brain reward regions. *Cell* 131, 391-404. DOI 10.1016/j.cell.2007.09.018 (**resolved and confirmed in validation**).

- **Claim.** [abstract read, Krishnan 2007] An inbred population of mice subjected to social defeat separates into "susceptible" and "unsusceptible" subpopulations differing on several behavioural and physiological measures, with signature adaptations in the mesolimbic dopamine circuit; molecular recapitulation of three adaptations of the unsusceptible phenotype is each sufficient to promote resistance. The authors frame this as plasticity in reward circuits "actively maintaining an emotional homeostasis". [standard account, not checked] Susceptible mice show lasting social avoidance, reversible by chronic but not acute antidepressant treatment. Used as a model of depression and social anxiety.
- **Standing.** A widely used, standardised protocol (Golden 2011). Susceptible / resilient dichotomy is a mouse-model construct; translation to human social withdrawal is an analogy.
- **Operand/operator.** Gives a negative-valence operator, `defeat(a, b)`, with persistent, state-changing effects on b (avoidance), and a population split. Useful as evidence that a social act can move a drive state in a lasting way. Not a human quantity.

### D3. Polyvagal theory (and why it is out)

**Citations.**
- Porges, S. W. (2007). The polyvagal perspective. *Biological Psychology* 74, 116-143. DOI 10.1016/j.biopsycho.2006.06.009 (confirmed).
- Added in validation: Grossman, P. & Taylor, E. W. (2007). Toward understanding respiratory sinus arrhythmia: relations to cardiac vagal tone, evolution and biobehavioral functions. *Biological Psychology* 74, 263-285. DOI 10.1016/j.biopsycho.2005.11.014 (confirmed). The original critique, in the same issue as Porges 2007.
- Grossman, P. (2023). Fundamental challenges and likely refutations of the five basic premises of the polyvagal theory. *Biological Psychology* 180, 108589. DOI 10.1016/j.biopsycho.2023.108589 (confirmed).

- **Claim.** A hierarchy of autonomic states (ventral vagal "social engagement", sympathetic, dorsal vagal shutdown) that regulates social behaviour.
- **Standing.** Grossman & Taylor 2007 [abstract read]: RSA is often treated as a direct measure of vagal tone but is confounded by respiration, physical activity and beta-adrenergic tone, and the polyvagal account of the evolution of vagal heart-rate control is inaccurate (it ignores cardiorespiratory synchrony in fish, among other things). Grossman 2023 [abstract read] argues each of the five premises is untenable or highly implausible, and that treating RSA as general vagal tone is a category mistake; it also notes the theory's claim that RSA is absent in reptiles. A 2026 collective critique, "Why the polyvagal theory is untenable: an international expert evaluation…", by Grossman and 38 co-signatories, appeared in *Clinical Neuropsychiatry* 23(1) (February 2026), with Porges's reply ("When a critique becomes untenable…", same issue, pp. 113-128) arguing it attacks a simplified reconstruction. Existence and titles confirmed from the journal's download page and secondary coverage in validation; no DOI checked, content not read. Treat the theory as unsupported by the anatomical and physiological evidence as its critics present it; it remains popular in clinical practice. Do not use it as a source of states or operators.

---

## E. Positive social drives in animals

- Burgdorf, J. & Panksepp, J. (2006). The neurobiology of positive emotions. *Neuroscience & Biobehavioral Reviews* 30, 173-187. DOI 10.1016/j.neubiorev.2005.06.001 (confirmed). Panksepp, J. & Burgdorf, J. (2003). "Laughing" rats and the evolutionary antecedents of human joy? *Physiology & Behavior* 79, 533-547. DOI 10.1016/s0031-9384(03)00159-8 (confirmed).
- Dunbar, R. I. M. (2010). The social role of touch in humans and primates. *Neuroscience & Biobehavioral Reviews* 34, 260-268. DOI 10.1016/j.neubiorev.2008.07.001 (confirmed).
- **Claim [standard account].** Play and tickling in rats evoke 50 kHz vocalisations and are rewarding; Dunbar proposes endorphin-mediated reward for grooming and touch as the bonding mechanism in primates. Panksepp's affective-systems framework (SEEKING, PLAY, PANIC/GRIEF and others) treats these as primary systems; it is influential, and contested in the interpretation of animal affect.
- **Operand/operator.** Supports separating a play/affiliation reward drive from the need-for-contact deficit drive: approach driven by want versus approach driven by lack.

---

## Synthesis for the algebra

### Which social drives have solid biological grounding as homeostatic variables

1. **Need for social contact (belonging).** Best grounded. A framework with a set point (Matthews & Tye; Lee, Chen & Tye 2021 make it two-sided and adaptive), mouse circuits for both need and satiety from two labs (Matthews 2016; Liu et al. 2025), two small human deprivation studies (Tomova: strong self-report, null preregistered midbrain test; Stijovic: energy drop comparable to fasting), a large loneliness literature supporting a person-specific, perception-based set point, and animal isolation effects. Still thin on parameters: no human decay rate, no human satiation curve, no cross-person scaling.

**Test of "only social contact has a homeostatic grounding" (validation).** It survives, with three qualifications. (i) *Social satiety and social fatigue* are not separate drives; they are the other side of the same loop. Liu et al. 2025 give a satiety population in mice; Lee et al. 2021 say excess contact is aversive; Hall & Davis's communicate-bond-belong theory (2016, *Communication Theory* 27, 21-47, DOI 10.1111/comt.12106, confirmed; title and search summary only) models interaction as homeostatic, trading social energy spent against the need to belong; Stijovic 2023 shows energy changes with isolation. So the algebra's contact variable needs a ceiling as well as a floor. (ii) *Status* has a "fundamental motive" case (Anderson et al. 2015) but no set point, and a 2020 paper reports that having status increases the desire for it, an anti-homeostatic pattern. (iii) Krishnan et al. 2007 use "emotional homeostasis" for resilience to defeat, but that is the field's loose usage for stability, not a regulated social quantity. No other social drive in this cluster has a detector-set point-effector account.
2. **Threat / fear.** Solid, but as a learning-and-defence system with quantitative models, not a depleting need. Social transmission is documented (observational fear learning, social buffering).
3. **Physiological stress regulated by company (social buffering).** Solid in animals, mixed in humans.

### Contested

- Social pain as the same system as physical pain (the pattern evidence leans toward distinct representations).
- Status as a dopaminergic reward drive (supported in kind, thin in detail).
- Social baseline / economy of action as a general principle (a theory with a small imaging base).
- Inter-brain synchrony as coupling (replicates as a correlation, interpretation contested).

### Weak or unsupported

- Intranasal oxytocin as a trust or bonding operator in humans (power and bias problems; mixed to failed replication).
- Dual-hormone hypothesis (r about -.06 in meta-analysis, with bias signs).
- Mirror neurons as the basis of empathy or contagion (strong version contested).
- Polyvagal theory (physiological premises challenged by a large group of researchers).

### Blunt: what exists versus what does not

**Exists.** (a) A defensible claim that social contact is a regulated need with a person-specific set point and a cue-reactive deficit state. (b) A transmission mechanism for fear with fitted learning models (Lindström, Haaker & Olsson 2018; Lindström et al. 2019; reviewed in Olsson et al. 2020), and an in-group gain on it (Golkar et al. 2015). Lockwood 2016, cited here in the first draft, is prosocial reward learning, not fear transmission. (c) Animal evidence that social acts (defeat, buffering, isolation) change a lasting drive state in the target. (d) A subjective-versus-objective split for belonging (perceived isolation matters more than contact counts) that tells the algebra to keep the set point on the person, not the relation.

**Does not exist.** (a) Any measured human time course for the contact deficit: how fast it grows, when it saturates, how it varies by person (two single-duration points, 8 h and 10 h, and mouse strain differences only). (b) A reproduced numeric coupling between two people's drive states, for any drive. (c) A homeostatic variable for status, power, curiosity or desire; they have reward-circuit correlates, not set points. (d) A clean hormone-to-drive map: the popular maps (oxytocin to trust, testosterone to dominance) are the weakest in the cluster. (e) Group-level homeostatic variables: group allostatic load (Saxbe) is a proposal, not a measured quantity.

**Design consequence for the algebra.** Treat belonging-deficit as a state variable with a person-specific set point, and fear transmission as an operator with an in-group gain. Leave other drives unanchored in biology, to be defined by their behavioural role, and do not import hormone values as parameters.

---

## Unconfirmed

Resolved in validation and removed from this list: Krishnan 2007 DOI (now 10.1016/j.cell.2007.09.018); Coan N = 16 and Izuma N = 19; Holt-Lunstad figures; author lists for Dekkers, Knight, Olsson 2020, Golden, Haaker (Haaker's was wrong and is fixed). The Olsson & Phelps in-group claim was a misattribution, now credited to Golkar et al. 2015.

- Zink et al. 2008 sample size: not checked.
- Grossman et al. 2026 collective critique and Porges's reply in *Clinical Neuropsychiatry* 23(1): titles and issue confirmed from the journal site and secondary coverage; no DOI, content not read.
- Whether any independent fMRI replication of Tomova 2020 exists: none found; the search was not exhaustive.
- "Reversible by chronic antidepressants" for social defeat: standard account (the usual source is Berton et al. 2006, *Science*), not checked.
- Dikker 2017's link of synchrony to ratings of teacher and classmates: search summary only.
- Bales et al. 2023 (PMC10036751): not re-checked.

## Missing important work (validation)

Added above: Liu et al. 2025 (*Nature*, hypothalamic social need and satiety circuit); Lee, Chen & Tye 2021 (*Cell*, two-sided and adaptive set point); Matthews et al. 2016 (*Cell*, dorsal raphe dopamine neurons and isolation); Stijovic et al. 2023 (*Psych. Science*, isolation lowers energy like fasting); Hall & Davis 2016 (communicate-bond-belong theory, social energy); Lindström, Haaker & Olsson 2018 and Lindström et al. 2019 (fitted models of observational threat learning); Golkar, Castro & Olsson 2015 (in-group gain); Anderson, Hildreth & Howland 2015 (status as a fundamental motive); Grossman & Taylor 2007. Still not covered and worth a look: rodent observational fear and emotional contagion (e.g. Jeon et al. 2010, *Nat. Neurosci.*, ACC in mouse observational fear; Keysers' rat emotional-contagion work); Berton et al. 2006 (*Science*, social defeat and BDNF); empathy-for-pain meta-analyses (Lamm, Decety & Singer 2011) as the human counterpart of vicarious affect; the ostracism literature (Williams) referred to but not cited in A5.

## Validation log (2026-10-29)

- A1 Matthews & Tye 2019 — ✓ (added Lee 2021, Matthews 2016, Liu 2025)
- A2 Tomova 2020 — ✎ corrected: preregistered anatomical SN/VTA test was null (P = .50); effect only in exploratory functional ROI; exact t-values; food craving t = 17.4 for scale [read]
- A3 Cacioppo & Cacioppo 2018 ETL — ✎ corrected author line, pages
- A3 Cacioppo & Hawkley 2009; Hawkley & Cacioppo 2010; Cacioppo 2009 JOCN; Baumeister & Leary 1995 — ✓
- A3 Spithoven 2019 — ✓ (authors, volume added)
- A3 Holt-Lunstad 2010 — ✓ figures confirmed, moved out of Unconfirmed
- A4 Beckes & Coan 2011; Hostinar 2014; Hennessy 2009; Kikusui 2006 — ✓
- A4 Coan 2006 — ✓ N = 16 confirmed
- A4 Saxbe 2020 — ✓ (online 2019 noted)
- A5 Eisenberger 2003, 2012, 2015; Kross 2011; Iannetti 2013; Lieberman & Eisenberger 2015 — ✓
- A5 Woo 2014 — ✓ figures confirmed; ✎ added that rejection was ex-partner viewing, plus resting-state result
- B1 Walum 2016 — ✎ corrected: 16% power and PPV ≤ 24% are Walum's own [read], not Lane's
- B1 Lane 2016 — ✎ corrected: a one-lab file-drawer report (8 studies, 453 subjects), not a power estimate
- B1 Mierop 2020 — ✓ (pages added)
- B1 Kosfeld 2005; Nave 2015; Leng & Ludwig 2016; Young & Wang 2004; Insel & Young 2001; Heinrichs 2003; Feldman 2017 — ✓
- B1 Feldman et al. 2010 — ✎ authors, journal, print year added
- B2 Zink 2008 — ✎ corrected: about perceiving others' rank and stability, not the viewer's own rank; operator revised
- B2 Izuma 2008 — ✓ N = 19 confirmed
- B2 Meshi 2013; Rilling 2002 — ✓
- B3 Dekkers 2019 — ✓ r = −.061, p = .026, n = 8,538 confirmed; authors confirmed
- B3 Mehta & Josephs 2010; Knight 2020; Eisenegger 2010, 2011; Mazur & Booth 1998 — ✓
- C1 Hasson 2012 — ✓ (noted as programmatic, not data)
- C1 Dikker 2017 — ✎ added N = 12, one classroom
- C1 Parada 2017 — ✎ added second author (Rossi)
- C1 Stephens 2010; Bevilacqua 2019; Dumas 2010; Pérez 2017; Hamilton 2021; Schilbach 2013; Nastase 2020 — ✓ (DOIs; Hamilton's content not re-read)
- C2 Rizzolatti & Craighero 2004; Gallese 1996; Gallese & Goldman 1998; Hickok 2009; Keysers & Gazzola 2014 — ✓ (DOIs only)
- D1 Olsson & Phelps 2007 — ✎ corrected: a review, not the source of the in-group effect
- D1 Olsson, Nearing & Phelps 2007 — ✓
- D1 Olsson, Knapska & Lindström 2020 — ✓ authors confirmed
- D1 Haaker 2017 — ✎ corrected author list (Golkar, Selbing, Olsson, not Maren, Andreatta); pages
- D1 Lockwood 2016 — ✎ corrected: prosocial reward learning, not fear learning; moved to D1b; fear-model role given to Lindström 2018/2019
- D2 Golden 2011 — ✓ authors confirmed
- D2 Krishnan 2007 — ✎ resolved: DOI 10.1016/j.cell.2007.09.018 confirmed, abstract read
- D3 Porges 2007; Grossman 2023 — ✓
- D3 Grossman et al. 2026 / Porges reply — ? existence confirmed, no DOI, not read
- E Burgdorf & Panksepp 2006; Panksepp & Burgdorf 2003; Dunbar 2010 — ✓ (DOIs only)
- ✗ removed: none (no fabrications found); one doubtful five-author Cacioppo attribution dropped.

**Verdict.** The bibliography is sound: every DOI in the draft (about 67, all re-checked) resolved to the stated work, and nothing was fabricated. The errors are in what papers were said to show, and they lean toward overstatement: Tomova's headline brain result was its exploratory analysis, while its preregistered test was null; Lockwood 2016 was used as the fitted model of fear transmission when it is about prosocial reward; Zink's rank finding and the oxytocin power figures were attributed loosely. Trust the citations and the overall verdicts (oxytocin, dual-hormone, polyvagal, mirror neurons as weak); check any single-paper claim against its abstract before building on it.

## Licences of quoted and transcribed material (2026-10-30)

Audit result for this file: one item, verdict "check", no text changed. No passage, table, figure or dataset is reproduced; the file restates numbers and findings in its own words, cites DOIs, and carries only a few very short quoted phrases. Licences below were not looked up for each publisher; where nothing was checked the entry says so.

**Provenance of the [read] tags (check item).** The file marks Tomova et al. 2020 and Walum et al. 2016 as [read] (lines 7, 30-31, 98) but did not record how the full text was obtained. That route was not recorded and cannot be reconstructed from the repo; nothing in the file says an access control was bypassed. Before open-sourcing, confirm each was read through a legitimate route (open-access copy, institutional or personal subscription); if not, downgrade the tag to [from abstract/standard account] with the note "readable copy not obtained legitimately; re-read needed". No text is reproduced from either paper, only restated figures (t-values, P values, power and PPV figures, effect sizes).

| Source | Licence as determined | How used |
|---|---|---|
| Tomova et al. 2020, Nature Neuroscience | not determined; publisher copyright presumed | restated statistics and design, citation |
| Walum, Waldman & Young 2016, Biological Psychiatry | not determined; publisher copyright presumed | restated power and PPV figures, citation |
| Matthews & Tye 2019, Ann. N.Y. Acad. Sci. (PMC7593988 cited as open copy) | not determined; PMC deposit, licence not checked | description, citation |
| Lee, Chen & Tye 2021, Cell (PMC8580010 cited) | not determined; publisher copyright presumed | description of abstract, citation |
| Liu et al. 2025, Nature | not determined; publisher copyright presumed | description of abstract, citation |
| Matthews et al. 2016, Cell | not determined; publisher copyright presumed | description, citation |
| Stijovic et al. 2023, Psychological Science | not determined; publisher copyright presumed | restated sample sizes and findings, citation |
| Holt-Lunstad et al. 2010, PLoS Medicine | CC BY (PLoS open access; not re-checked here) | restated figures (148 studies, OR 1.50), citation |
| Coan et al. 2006; Woo et al. 2014 (Nature Communications); Dekkers et al. 2019; Izuma et al. 2008; Zink et al. 2008; Mierop et al. 2020; Lane et al. 2016 | not determined; publisher copyright presumed (Woo 2014 is likely CC BY open access, not checked) | restated figures from abstracts, citation |
| Krishnan et al. 2007; Lindström et al. 2018, 2019; Golkar et al. 2015; Grossman & Taylor 2007; Grossman 2023; Lockwood et al. 2016; Anderson et al. 2015 | not determined; publisher copyright presumed | description of abstract findings, citation |
| All other cited works (DOI-only entries) | not applicable; citation only | bibliographic reference |

Short quoted phrases, all a few words and attributed in the text: "common neural currency" (Izuma 2008), "actively maintaining an emotional homeostasis" (Krishnan 2007), "only marginal support" (Dekkers 2019), "in a strong and surprisingly inflexible manner" (Lindström 2019). Each is a fragment of an abstract, well under 60 words, used for attribution of a claim.

No Wikipedia-derived text and no dataset is used in this file. Crossref metadata (titles, years, journals, DOIs) was used for confirmation; bibliographic facts are free.
