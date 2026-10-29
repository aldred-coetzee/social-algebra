# Prior work 41: self-conscious, moral and relational drives

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: the drives that exist only because other people exist (shame, guilt, pride, envy, jealousy, gratitude, trust, revenge and forgiveness, outrage, embarrassment, compassion, humiliation) and every dynamic or formal model of them. Context: Aldred's clarified aim, a new or updated equation set covering the full range of human and group drives, with curiosity, fear and desire only examples.

**Cross-references, not repeated.** File 21 holds Fehr-Schmidt, Bolton-Ockenfels, Charness-Rabin, Rabin 1993, Kirchsteiger/Mui on envy, Battigalli-Dufwenberg guilt aversion, Charness-Dufwenberg promises. File 17 holds curiosity/fear/desire. File 27 holds Brady et al. 2017 (moral contagion, +20% diffusion per moral-emotional word). File 22 holds oxytocin-and-trust (failed replications) and loneliness. File 39 holds deterrence. File 15 holds Plutchik's trust and the BUCET "trusting". File 31 holds signal honesty (relevant to embarrassment as a signal). File 24 holds sacred values and devotion (Atran and Gomez).

**Method and honesty note.** Tags: `[read]` = read at source this session; `[abstract]` = abstract read (via Europe PMC); `[standard]` = standard account from background knowledge, not checked this session and needing a primary-text check before anything is built on it. `[secondary]` (added in validation) = confirmed against a secondary source quoting or summarising the paper, not the paper itself. Only Nowak & Roch (2007) was read in full text (PMC2197219, model and results sections). All DOIs below were returned by Crossref for the title searched, except where marked. Where Crossref returned a preprint, SSRN or a reprint DOI rather than the journal version, that is said.

**Summary.** Two things stand out.
1. **Almost nothing here has a dynamical equation.** The mature formal models are (a) evolutionary game theory of reciprocity, which gives gratitude, forgiveness, trust and reputation exact rules with proofs, but treats the emotion as a behavioural strategy parameter; (b) a handful of learning models of trust; (c) psychological game theory (file 21) for guilt and envy, which are static and belief-dependent. The emotion psychology (Tangney, Tracy & Robins, Smith & Kim, Keltner, Batson, McCullough) is appraisal-and-action-tendency theory in prose and correlation tables.
2. **There is one genuinely quantitative regularity shared across the cluster: self-conscious emotion intensity tracks the audience's valuation.** Sznycer et al. found shame tracks others' devaluation (r = .67 to .79 within countries; abstract) and pride tracks audience valuation (mean r = +.82 local, +.75 foreign, 16 countries, n = 2,085; abstract). That is a calibration law with a named input (a third party's evaluation) and is the best candidate for a first equation in this cluster. It is an across-item correlation, not a time-course.

---

## A. Shame, guilt, embarrassment, pride (the self-conscious family)

### A1. Tangney, Stuewig & Mashek (2007): moral emotions and moral behaviour
**Citation.** Tangney, J. P., Stuewig, J. & Mashek, D. J. (2007). Moral emotions and moral behavior. *Annual Review of Psychology* 58, 345-372. doi:10.1146/annurev.psych.56.091103.070145 (Crossref match).
**Their vocabulary.** Self-conscious emotions: shame, guilt, embarrassment; positive moral emotions: elevation, gratitude, pride; other-oriented empathy `[abstract]`.
**Appraisal and trigger `[standard]`.** The classic Tangney distinction: shame is a negative evaluation of the global self ("I am bad"), guilt a negative evaluation of a specific behaviour ("I did something bad"). Same transgression can produce either, depending on the attribution.
**Action tendency `[standard]`.** Shame: hiding, withdrawal, denial, and (in the shame-proneness literature) externalised blame and anger. Guilt: confession, apology, reparation, empathy for the victim.
**Dynamics / formal model.** None. Trait measures only (TOSCA-type scenario instruments).
**Evidence, blunt.** The meta-analysis of Tignor & Colvin (2017, doi:10.1111/jopy.12244, `[abstract]`) is the best sceptical check: dispositional guilt correlates positively with pro-social orientation (k = 63, mean r = .13), dispositional shame correlates about zero to slightly negative (k = 47, mean r = -.05, p = .07), and the results depend heavily on test format (scenario vs checklist) and on whether shame and guilt are partialled against each other (semi-partial correlations give stronger effects). So "guilt good, shame bad" is real but small (r around .1), and partly produced by method choices. Baumeister, Stillwell & Heatherton (1994, *Psychological Bulletin* 115, 243-267, doi:10.1037/0033-2909.115.2.243, `[abstract]`) argue guilt is relational: strongest in communal relationships, and serving to enforce mutual concern, redistribute distress, and let less powerful partners get their way.
**Translation.** Operand: an agent with a self-evaluation state and a relationship tie. The shame/guilt split is an attribution switch (global vs specific) that selects between two operators (withdraw(self) vs repair(self→other)). The algebra can carry the switch as a typed argument on the appraisal, no more.

### A2. Tracy & Robins (2004): the self-conscious emotions model
**Citation.** Tracy, J. L. & Robins, R. W. (2004). Putting the self into self-conscious emotions: a theoretical model. *Psychological Inquiry* 15(2), 103-125. doi:10.1207/s15327965pli1502_01 (Crossref match).
**Model `[standard]`, not read.** A decision path of appraisals: (1) is the event relevant to my identity goals? (2) was it congruent or incongruent with them? (3) attributed to internal causes? (4) to stable/global or unstable/specific causes, and controllable? Combinations yield: pride (internal, congruent), then authentic pride if attributed to unstable, controllable effort and hubristic pride if attributed to stable, global ability; shame (internal, incongruent, stable, global, uncontrollable); guilt (internal, incongruent, unstable, specific, controllable). Embarrassment is separate in Tracy & Robins as a non-moral social-evaluation emotion.
**Dynamics.** None. A flowchart is the formalism, and the most algebra-ready object in the cluster: it is a decision tree from appraisal variables to labelled emotions, which could be transcribed directly as a typed function.
**Evidence.** Discriminant structure of authentic vs hubristic pride has replicated in factor analysis of self-report scales `[standard]`. The scale paper is Tracy, J. L. & Robins, R. W. (2007). The psychological structure of pride: a tale of two facets. *JPSP* 92, 506-525. doi:10.1037/0022-3514.92.3.506 (Crossref match; the PsycTESTS record doi:10.1037/t06465-000 is only the instrument). Show your pride: Tracy & Robins (2004), *Psychological Science* 15, 194-197, doi:10.1111/j.0956-7976.2004.01503008.x `[abstract]`: three experiments with US judges showing pride has a distinct, recognisable expression (small smile, head tilted slightly back, expanded posture, arms raised or hands on hips). The **cross-cultural** recognition result is a later paper: Tracy, J. L. & Robins, R. W. (2008). The nonverbal expression of pride: evidence for cross-cultural recognition. *JPSP* 94, 516-530. doi:10.1037/0022-3514.94.3.516 `[abstract]` (Italy, US, and a preliterate group in Burkina Faso).
**Translation.** Appraisal tree as the front end of any self-conscious drive operator.

### A3. Pride as a status signal; dominance vs prestige
**Citations.** Cheng, J. T., Tracy, J. L. & Henrich, J. (2010). Pride, personality, and the evolutionary foundations of human social status. *Evolution and Human Behavior* 31, 334-347. doi:10.1016/j.evolhumbehav.2010.02.004 (Crossref match; content `[standard]`). Cheng, Tracy, Foulsham, Kingstone & Henrich (2013). Two ways to the top: evidence that dominance and prestige are distinct yet viable avenues to social rank and influence. *JPSP* 104, 103-125. doi:10.1037/a0030398 (`[abstract]`). Sznycer et al. (2017). Cross-cultural regularities in the cognitive architecture of pride. *PNAS* 114, 1874-1879. doi:10.1073/pnas.1614389114 (`[abstract]`).
**Claims.** `[standard]` for the 2010 paper: hubristic pride relates to dominance (fear-based rank), authentic pride to prestige (respect-based rank). `[abstract]` for 2013: both dominance and prestige yield influence in newly formed groups, as perceived and as measured behaviourally. `[abstract]` for Sznycer: pride is a programme that forecasts how much audiences will value an act or trait and scales its intensity to the forecast.
**Equation.** Informal: pride intensity ≈ f(forecast audience valuation of act). Estimated across 25 acts and traits and 16 countries as a correlation, not a fitted function (`[abstract]`).
**Evidence and caveats.** The across-culture correlation is between mean ratings across items, a strong aggregate with unknown individual-level fit. Hubristic/authentic pride self-report scales share a common method; causal direction (pride producing rank vs rank producing pride) is not settled by the cross-sectional data.
**Translation.** Pride is an operator-triggering state whose input is a third-party valuation vector (audience × act). Output: advertise(act), pursue(act) and, per Cheng, either dominate or defer-and-teach strategies. The dominance/prestige split is a genuine two-valued operator type on rank acquisition.

### A4. Sznycer et al. (2016): shame tracks devaluation
**Citation.** Sznycer, D., Tooby, J., Cosmides, L., Porat, R., Shalvi, S. & Halperin, E. (2016). Shame closely tracks the threat of devaluation by others, even across cultures. *PNAS* 113, 2625-2630. doi:10.1073/pnas.1514699113 (Crossref match, `[abstract]`).
**Content.** Shame is proposed as a defence with three jobs: deter choices where expected devaluation exceeds benefit, prevent negative information about the self from reaching others, and minimise the damage when devaluation occurs. Test: shame for a trait or act tracks the devaluation it elicits from others (r = .69 US, .79 India, .67 Israel) and, across countries, tracks other countries' devaluation. Specific: sadness and anxiety did not track devaluation.
**Their implied equation.** shame_i(act) ≈ g(D_audience(act)), D = the audience's negative valuation. Tested as correlation across acts, not as a fitted g.
**Link to the sociometer.** Leary, Tambor, Terdal & Downs (1995), *JPSP* 68, 518-530, doi:10.1037/0022-3514.68.3.518 (Crossref match; content `[standard]`): state self-esteem is a gauge of relational value (inclusion). Same shape: self-conscious affect as a monitor of other people's valuation.
**Evidence, blunt.** Cross-cultural convergence on a monotone relation is a good sign. The hypotheses were tested on a small number of countries (three for shame); a later preprint by Sznycer & Landers ("Cross-cultural regularities and variability in the emotion of shame", doi:10.31234/osf.io/zpyrb, 2024) reports variability as well as regularity, which is not read here.
**Translation.** The first quantified operator in the cluster: S_shame(i; act, audience) increases with D(audience, act). Inputs: who sees, what they think.

### A5. Embarrassment and appeasement (Keltner)
**Citations.** Keltner, D. (1995). Signs of appeasement: evidence for the distinct displays of embarrassment, amusement, and shame. *JPSP* 68, 441-454. doi:10.1037/0022-3514.68.3.441. Keltner, D. & Buswell, B. N. (1997). Embarrassment: its distinct form and appeasement functions. *Psychological Bulletin* 122, 250-270. doi:10.1037/0033-2909.122.3.250 (`[abstract]`). Feinberg, M., Willer, R. & Keltner, D. (2012). Flustered and faithful: embarrassment as a signal of prosociality. *JPSP* 102, 81-97. doi:10.1037/a0025403 (`[abstract]`).
**Trigger.** Violation of social conventions or loss of face in front of an audience (Keltner & Buswell's five accounts: loss of self-esteem, concern for others' evaluation, absence of scripts, remedial effects of the display, and the animal appeasement parallel) `[abstract]`.
**Action tendency.** Display (gaze aversion, smile control, face touching, head down) that appeases the audience. Feinberg et al. `[abstract]`: observers read the embarrassment display as a signal of prosociality and respond with more trust and willingness to affiliate; more embarrassable people were more generous.
**Dynamics, formal.** None. The signalling interpretation fits the costly-signal framework of file 31, but no one has written the signal game for embarrassment.
**Evidence.** Experimental studies of moderate size, social-psych style. Keltner 1995 `[abstract]`: five studies; the embarrassment display was distinct from amusement, followed the temporal pattern of facial expressions of emotion, related uniquely to self-reported embarrassment, and was identified by observers, who were more accurate and attributed more emotion when the target was from a lower-status group (female, African-American), as appeasement predicts. No large replication effort is known to me.
**Translation.** Operator: Appease(i→audience), triggered by a norm breach seen by the audience; effect on the audience: raises trust in i, lowers sanction. A one-line rule: if breach observed, then display, then audience trust(i) up and sanction(i) down.

---

## B. Envy, schadenfreude, jealousy

### B1. Smith & Kim (2007): Comprehending envy
**Citation.** Smith, R. H. & Kim, S. H. (2007). Comprehending envy. *Psychological Bulletin* 133, 46-64. doi:10.1037/0033-2909.133.1.46 (`[abstract]`).
**Content `[abstract]`.** Envy proper contains hostility; benign envy is free of it. Envy is defined as "an unpleasant, often painful emotion characterized by feelings of inferiority, hostility, and resentment caused by an awareness of a desired attribute enjoyed by another person or group". The review asks why envy contains hostile feelings and why it "transmutes itself" (into e.g. contempt, depressive affect, or schadenfreude).
**Trigger.** Upward social comparison on a self-relevant domain (Takahashi et al. below add self-relevance and possession as the two inputs).
**Action tendency `[standard]`.** Hostile envy: pull-down (damage or withhold from the envied). Benign: move-up.
**Formal.** None in the review; the economic formalisation is file 21's inequity-aversion models (Fehr-Schmidt disadvantageous-inequity term, Kirchsteiger/Mui). The disadvantageous-inequity coefficient there is the envy parameter.

### B2. Benign vs malicious envy (van de Ven, Zeelenberg & Pieters)
**Citation.** van de Ven, N., Zeelenberg, M. & Pieters, R. (2011). Why envy outperforms admiration. *PSPB* 37, 784-795. doi:10.1177/0146167211400421 (`[abstract]`). Also *The envy premium in product evaluation*, *J. Consumer Research* 37, 984-998, doi:10.1086/657239 (Crossref match; content `[standard]`).
**Content `[abstract]`.** Four studies: benign envy, but not admiration or malicious envy, motivated studying and performance on the Remote Associates Task; and an upward comparison led to benign envy and better performance only when self-improvement was seen as attainable. When improvement seemed hard, comparison gave admiration and no motivation.
**Appraisal switch.** Perceived controllability or attainability of the gap: attainable gives benign (move up), unattainable gives malicious or passive admiration. This is a typed switch on the same trigger, parallel to shame/guilt.
**Dynamics.** None. Effects are between-condition mean differences from small experimental samples.
**Evidence, blunt.** Experimental psychology of this kind (n in the low hundreds, lab tasks) is the replication-risk category. The benign/malicious distinction has been replicated in other labs' scale validations `[standard]`, but I did not check. The paper that introduced the benign/malicious split empirically is van de Ven, N., Zeelenberg, M. & Pieters, R. (2009). Leveling up and down: the experiences of benign and malicious envy. *Emotion* 9, 419-429. doi:10.1037/a0015669 (Crossref match; content `[standard]`).

### B3. Schadenfreude
**Citations.** Leach, C. W., Spears, R., Branscombe, N. R. & Doosje, B. (2003). Malicious pleasure: schadenfreude at the suffering of another group. *JPSP* 84, 932-943. doi:10.1037/0022-3514.84.5.932 (`[abstract]`). Takahashi, H. et al. (2009). When your gain is my pain and your pain is my gain: neural correlates of envy and schadenfreude. *Science* 323, 937-939. doi:10.1126/science.1165604 (`[abstract]`). Cikara, M., Botvinick, M. M. & Fiske, S. T. (2011). Us versus them: social identity shapes neural responses to intergroup competition and harm. *Psychological Science* 22, 306-313. doi:10.1177/0956797610397667 (Crossref match; content `[standard]`: ventral striatum response to rival-team failure).
**Trigger.** Misfortune to an envied or rival target, moderated by inferiority threat to the self or in-group (Leach: soccer fans; schadenfreude rose with interest in the sport and with threat of in-group inferiority; and in Study 2 lower toward a legitimately superior rival (Italy) when a norm of honest, direct expression was made salient, among participants low in soccer interest) `[abstract]`.
**Neural.** Takahashi `[abstract]`: envy engaged the anterior cingulate cortex; schadenfreude engaged the striatum; the ACC activation in the envy study predicted striatal activation in the schadenfreude study. In the same envy-then-schadenfreude chain, the one quantitative statement is a within-subject correlation across two experiments.
**Also.** Bault et al. (2011), "Medial prefrontal cortex and striatum mediate the influence of social comparison on the decision process", *PNAS* 108, 16044-16049, doi:10.1073/pnas.1100892108 (`[abstract]`): striatal activity higher when winning more than a counterpart and lower when winning less.
**Formal.** The sign-flip in the other's payoff: file 21's Levine (1998) spite/altruism model has the right structure (utility rises with other's loss when the other is disliked); not repeated here.
**Translation.** Schadenfreude is the same relation with the sign of ∂U_i/∂(outcome_j) negative, conditional on (rival or envied) status of j. Algebraically a one-term sign change; the harder part is what determines that sign: group membership and self-relevant comparison (Leach, Cikara).

### B4. Jealousy: Buss's sex-difference claim and its critics
**Citations.** Buss, D. M., Larsen, R. J., Westen, D. & Semmelroth, J. (1992). Sex differences in jealousy: evolution, physiology, and psychology. *Psychological Science* 3, 251-255. doi:10.1111/j.1467-9280.1992.tb00038.x (Crossref match; authors confirmed in Crossref; content `[standard]`). DeSteno, D. A. & Salovey, P. (1996). Evolutionary origins of sex differences in jealousy? Questioning the "fitness" of the model. *Psychological Science* 7, 367-372. doi:10.1111/j.1467-9280.1996.tb00391.x (Crossref match; content `[standard]`). Harris, C. R. (2003). A review of sex differences in sexual jealousy, including self-report data, psychophysiological responses, interpersonal violence, and morbid jealousy. *Personality and Social Psychology Review* 7, 102-128 doi:10.1207/s15327957pspr0702_102-128 (unusual form, but it is the registered DOI and resolves; content `[standard]`). Sagarin, B. J., Martin, A. L., Coutinho, S. A., Edlund, J. E., Patel, L., Skowronski, J. J. & Zengel, B. (2012). Sex differences in jealousy: a meta-analytic examination. *Evolution and Human Behavior* 33, 595-614. doi:10.1016/j.evolhumbehav.2012.02.006 (Crossref match; content `[secondary]`, from a summary of the paper, not the paper itself).
**Claim `[standard]`.** Men are more distressed by sexual infidelity (paternity uncertainty), women by emotional infidelity (loss of investment). Measured by forced choice and by physiological reactivity.
**Critique `[standard]`.** (i) Critics argued the effect depends on the forced-choice format. Sagarin et al.'s meta-analysis restricted to **continuous** measures (47 independent samples) nevertheless found a theory-consistent sex difference, small in size (about g = 0.26 for hypothetical scenarios, g = 0.23 across seven samples reporting actual infidelity) and strongest when jealousy or distress was the measured emotion `[secondary]`. So "no difference on continuous measures" is wrong; "smaller than forced choice suggests" is the defensible statement. (ii) A double-shot hypothesis (DeSteno & Salovey): people believe sexual infidelity implies emotional involvement for women and the reverse for men, so belief, not an adapted module, drives the pattern. (iii) Physiological studies had small samples and replication problems. (iv) Cross-cultural results vary. Treat the adaptationist *explanation* as contested; the existence of a small sex difference on continuous measures is supported by the meta-analysis.
**Trigger (cleaner statement).** A third party threatens a valued dyadic bond; the operand is a triad (self, partner, rival).
**Action tendency.** Mate guarding, monitoring, derogation of rival, violence in the extreme `[standard]`.
**Formal.** None. The Descartes passion in file 26 (jealousy as "closer bonds" to another) is the philosophical statement; economics has no accepted jealousy model; the relevant structure is a three-place relation, which is why jealousy is a good test of an algebra: it needs a ternary operand (self, partner, rival) where almost everything else in this cluster is dyadic or audience-based.

---

## C. Gratitude and reciprocity

### C1. McCullough et al. (2001): gratitude as a moral affect
**Citation.** McCullough, M. E., Kilpatrick, S. D., Emmons, R. A. & Larson, D. B. (2001). Is gratitude a moral affect? *Psychological Bulletin* 127, 249-266. doi:10.1037/0033-2909.127.2.249 (`[abstract]`).
**Content `[abstract]`.** Three functions: moral barometer (response to having benefited from another's moral action), moral motive (prompts prosocial behaviour toward the benefactor and others), moral reinforcer (expression encourages the benefactor to behave morally again).
**Trigger.** Another person's intentional act of benefit to me, costly to them. Appraisal inputs `[standard]`: cost to the benefactor, value to me, intent (Tsang and others).
**Action tendency.** Reciprocate to benefactor (downstream) or pass on to others (upstream).
**Supporting experiments.** Bartlett & DeSteno (2006), *Psychological Science* 17, 319-325, doi:10.1111/j.1467-9280.2006.01705.x `[abstract]`: induced gratitude increased costly helping of the benefactor, beyond the effect of general positive affect; Study 2 showed it also increased help to a **stranger** (the upstream case Nowak & Roch model), and Study 3 that the effect dissipated once people were told the true cause of the feeling. Algoe (2012), "Find, remind, and bind", *Soc. Pers. Psych. Compass* 6, 455-469, doi:10.1111/j.1751-9004.2012.00439.x (Crossref match; content `[standard]`): gratitude strengthens relationships.
**Evidence on gratitude interventions, blunt.** Davis et al. (2016), *J. Counseling Psychology* 63, 20-31, doi:10.1037/cou0000107 (`[abstract]`): vs measurement-only control, well-being d = .31 (CI .04 to .58, k = 5), gratitude d = .20 (CI -.04 to .44, k = 4, includes zero); vs an alternative activity, gratitude d = .46 (k = 15), well-being d = .17 (k = 20), anxiety d = .11 (CI includes zero). Small, with wide intervals, and weaker once the comparison activity is active. This is evidence for the trait-level self-help claim, not for the interpersonal reciprocity claim.

### C2. Nowak & Roch (2007): upstream reciprocity, the formal model of gratitude `[read]`
**Citation.** Nowak, M. A. & Roch, S. (2007). Upstream reciprocity and the evolution of gratitude. *Proc. R. Soc. B* 274(1610), 605-610. doi:10.1098/rspb.2006.0125 (Crossref match; full text read via PMC2197219).
**Setup `[read]`.** Each altruistic act costs the donor c and benefits the recipient b, with b > c. Chains: one player initiates; each recipient passes on with probability p to another random player. A strategy S(p, q) has p = probability to pass on (gratitude-related altruism) and q = probability to initiate (spontaneous altruism). Average chain length is 1/(1-p). Cooperativity s = q/(1-p).
**Result 1 `[read]`.** Upstream reciprocity alone does not lead to the evolution of cooperation: "natural selection always reduces the cooperativity, s"; defectors S(0,0) dominate every strategy with s > 0.
**Add direct reciprocity `[read]`.** Let r = probability help is immediately returned to the donor; the recipient then helps another random player with probability (1-r)p. Strategy S(p, q, r). Fitness difference f(x) = αβ/γ with
α = q1(1-r2)(1-p2) - q2(1-r1)(1-p1),
β = (b r2 - c)(1 - r1) - x(b - c)(r2 - r1),
γ as given in the paper (positive when p1, p2 < 1),
and replicator dynamics ẋ = x(1-x)f(x). It reduces to a matrix game with payoff A(Si, Sj) = s_i u_j, where s_i = q_i/[(1-r_i)(1-p_i)] and u_j = (b r_j - c)/(1-r_j) (cooperativity and responsiveness). Invasion barrier against defectors: x̂ = [c/(b-c)]·[(1-r)/r], and x̂ < 1 requires **r > c/b**.
**Stated theorems `[read]`.** If both r1 and r2 exceed c/b, selection favours higher cooperativity; if both are below, lower; if r1 > c/b > r2 and s1 < s2, a stable mixed equilibrium. A strategy is stable against lower-cooperativity invaders if r > c/b. So: "if there is direct reciprocity in a population, then upstream reciprocity will evolve too": p hitch-hikes on r.
**Spatial reciprocity `[read]`.** In a one-dimensional array with imitation updating, spontaneous altruists S(0,1) beat defectors if b/c > 4; gratitude-related S(1,1) beat them if b/c > 10/7; for 0 < p < 1 the threshold is a function h(p).
**Empirical standing.** A theory paper; the behavioural fact it models (upstream reciprocity in experiments) is cited in the paper (Bartlett & DeSteno 2006; others). No test of the model's specific predictions (e.g. p rising with r) is known to me.
**Translation.** The strongest candidate cluster-level theorem. Gratitude is a pair (p, q) of continuous parameters of an agent, and the operator "receive help" updates the agent's disposition to help a third party. The condition r > c/b is a closed-form relation among the group-level reciprocity rate and the cost-benefit ratio. It is the only place in the cluster where a drive parameter is shown, with proof, to be selected for.

### C3. Indirect reciprocity: image scoring and norms (formal reputation dynamics)
**Citations.** Nowak, M. A. & Sigmund, K. (1998). Evolution of indirect reciprocity by image scoring. *Nature* 393, 573-577. doi:10.1038/31225. Wedekind, C. & Milinski, M. (2000). Cooperation through image scoring in humans. *Science* 288, 850-852. doi:10.1126/science.288.5467.850 (`[abstract]`). Panchanathan, K. & Boyd, R. (2004). Indirect reciprocity can stabilize cooperation without the second-order free rider problem. *Nature* 432, 499-502. doi:10.1038/nature02978. Ohtsuki, H. & Iwasa, Y. (2004). How should we define goodness? Reputation dynamics in indirect reciprocity. *J. Theor. Biol.* 231, 107-120. doi:10.1016/j.jtbi.2004.06.005 (`[abstract]`). Nowak, M. A. & Sigmund, K. (2005). Evolution of indirect reciprocity. *Nature* 437, 1291-1298. doi:10.1038/nature04131 (Crossref matches; content `[standard]` unless tagged).
**Rule `[standard]`.** Each agent carries a reputation score; image scoring: a donor gives to a recipient whose score is at least a threshold k, giving raises one's own score, refusing lowers it. Known flaw: refusing to help a bad-reputation recipient lowers your own score, so discriminators are punished. Higher-order norms (Ohtsuki-Iwasa, 4096 candidate norms examined exhaustively, `[abstract]`; the stable ones are the "leading eight" `[standard]`) judge an act by donor action and recipient reputation together, so helping the bad and refusing the bad can be scored differently.
**Evidence.** Wedekind & Milinski `[abstract]`: donations were more frequent to receivers who had been generous earlier, in a setting where direct reciprocity was unlikely. Small lab game; whether image scoring (rather than richer standing norms) is what people use is contested `[standard]`.
**Translation.** Gratitude and trust at group scale share this object: a public score r_j on each agent, updated by operators on observed acts. It is also the mechanism that turns private shame/pride into public stakes.

---

## D. Trust and its dynamics

### D1. Definitions and structure
**Citations.** Rousseau, D. M., Sitkin, S. B., Burt, R. S. & Camerer, C. (1998). Not so different after all: a cross-discipline view of trust. *Academy of Management Review* 23, 393-404. doi:10.5465/amr.1998.926617 (Crossref match; content `[standard]`). Mayer, R. C., Davis, J. H. & Schoorman, F. D. (1995). An integrative model of organizational trust. *AMR* 20, 709-734. doi:10.2307/258792 (Crossref match; the 2006 reprint chapter is doi:10.1093/oso/9780199288496.003.0004).
**Definition `[standard]`.** Rousseau et al.: trust is a psychological state comprising the intention to accept vulnerability based upon positive expectations of the intentions or behaviour of another. Mayer et al.: trustworthiness has three dimensions (ability, benevolence, integrity); trust propensity is a trait; trust leads to risk taking.
**Formal content.** None; a variable-and-arrow model.
**Meta-analytic evidence.** Colquitt, Scott & LePine (2007), *J. Applied Psychology* 92, 909-927, doi:10.1037/0021-9010.92.4.909 (`[abstract]`): 132 independent samples; trustworthiness and trust propensity explain incremental variance in risk taking and performance beyond trust itself; trustworthiness dimensions also predicted affective commitment. Dirks & Ferrin (2002), *J. Applied Psychology* 87, 611-628, doi:10.1037/0021-9010.87.4.611 (`[abstract]`): k = 106; direct leaders (supervisors) are an especially important referent. Johnson, N. D. & Mislin, A. A. (2011). Trust games: a meta-analysis. *J. Economic Psychology* 32, 865-889. doi:10.1016/j.joep.2011.05.007 (Crossref match; SSRN preprint doi:10.2139/ssrn.1702678). Abstract not read.

### D2. The trust game as the unit experiment
**Citation.** Berg, J., Dickhaut, J. & McCabe, K. (1995). Trust, reciprocity, and social history. *Games and Economic Behavior* 10, 122-142. doi:10.1006/game.1995.1027 (Crossref match).
**Setup `[standard]`.** Investor sends x ≤ E from endowment E; the amount is multiplied (tripled); trustee returns y. Subgame-perfect prediction: x = 0 under selfish preferences; observed investment is positive and returns correlate with investment. Trust is x/E, trustworthiness is y/(3x).
**In the algebra.** The trust game is the minimal ordered pair of operators: Send(i→j, x) then Return(j→i, y). The reciprocity models of file 21 (Rabin, Dufwenberg-Kirchsteiger) explain y.

### D3. Trust as learned belief: the closest to a dynamic equation
**Citation.** Chang, L. J., Doll, B. B., van 't Wout, M., Frank, M. J. & Sanfey, A. G. (2010). Seeing is believing: trustworthiness as a dynamic belief. *Cognitive Psychology* 61, 87-105. doi:10.1016/j.cogpsych.2010.03.001 (Crossref match; `[abstract]`).
**Content `[abstract]`.** A repeated trust game with implicit initial trustworthiness cues (faces) crossed with experienced trustworthiness. Both affected investments, independently and synergistically. Reinforcement-learning models were fitted; the conclusion is that trustworthiness is "a belief about probability of reciprocation based initially on implicit judgments, and then dynamically updated based on experiences".
**Equation (generic form, `[standard]`; the paper's fitted variants not read).** Belief b_t about the partner's reciprocation probability updated by prediction error: b_{t+1} = b_t + α(o_t - b_t), o_t = 1 if the trustee reciprocated; initial b_0 set by the prior (face); asymmetric learning rates α+ and α- are the usual competing hypotheses. Investment is a monotone function of b_t.
**Beta-Bernoulli alternative `[standard]`.** The Bayesian equivalent: trust = posterior mean (r+1)/(r+s+2) for r reciprocations and s defections (Jøsang & Ismail, "The Beta Reputation System", Bled eCommerce Conference 2002; Crossref returned a different Jøsang paper, doi:10.1007/978-3-540-45229-4_18, so the Bled paper's DOI is unconfirmed).
**Empirical standing.** One lab study, model comparison on task data; model fit to behaviour, not out-of-sample forecasting of new relationships. King-Casas et al. (2005), *Science* 308, 78-83, doi:10.1126/science.1108062 (Crossref match; content `[standard]`) found caudate signals anticipating partner's intention shifting earlier across rounds of a repeated trust game. Delgado, Frank & Phelps (2005), *Nature Neuroscience* 8, 1611-1618, doi:10.1038/nn1575 (Crossref match; content `[standard]`): prior moral-character information reduced the striatal response to reinforcement, i.e. priors override feedback learning.
**Translation.** Operand: a belief state about a partner (a probability of reciprocation, or a Beta distribution). Operators: Observe(reciprocated) updates the belief; asymmetric α encodes that betrayals weigh more than confirmations (standard claim, mixed evidence).

### D4. Trust repair
**Citation.** Kim, P. H., Ferrin, D. L., Cooper, C. D. & Dirks, K. T. (2004). Removing the shadow of suspicion: the effects of apology versus denial for repairing competence- versus integrity-based trust violations. *J. Applied Psychology* 89, 104-118. doi:10.1037/0021-9010.89.1.104 (Crossref match, `[abstract]`). Schweitzer, M. E., Hershey, J. C. & Bradlow, E. T. (2006), Promises and lies: restoring violated trust, *Organizational Behavior and Human Decision Processes* 101, 1-19. doi:10.1016/j.obhdp.2006.05.005 (Crossref match; content `[standard]`).
**Claims.** Kim et al. `[abstract]`, two studies: trust was repaired better when the mistrusted party apologised for a competence violation but denied culpability for an integrity violation; and, separately, when they had apologised where later evidence showed guilt but denied where later evidence showed innocence. The effects on trusting intentions were mediated by trusting beliefs. Schweitzer et al.: after a violation, trust rebuilds more slowly than it fell; promises alone are less effective than demonstrated trustworthy behaviour over time `[standard]`.
**Dynamics.** Qualitative asymmetry: "trust is built slowly and lost quickly". It is stated verbally; no widely accepted equation of trust repair exists. The asymmetric-learning-rate model of D3 would predict the asymmetry, but nobody has fitted it to repair data that I found.
**Evidence.** Scenario and lab studies, often with students; no large field replication known.

---

## E. Revenge, forgiveness, retaliation

### E1. McCullough et al.: the cognitive systems of revenge and forgiveness
**Citations.** McCullough, M. E., Kurzban, R. & Tabak, B. A. (2013). Cognitive systems for revenge and forgiveness. *Behavioral and Brain Sciences* 36, 1-15. doi:10.1017/S0140525X11002160 (`[abstract]`). McCullough, M. (2008). *Beyond Revenge: The Evolution of the Forgiveness Instinct*. Jossey-Bass (book; the DOI Crossref returned, 10.1080/17439760903509614, is a review of it, not the book). McCullough, Worthington & Rachal (1997). Interpersonal forgiving in close relationships. *JPSP* 73, 321-336. doi:10.1037/0022-3514.73.2.321 (Crossref match; content `[standard]`).
**Model `[abstract]`.** Two linked systems. The **revenge system** imposes retaliatory costs on a cost-imposer so that the aggressor and observers lower their estimate of net benefits from exploiting the retaliator. Its by-product is losing future gains from the target. A **forgiveness system** therefore inhibits revenge and motivates benevolence-signalling to restore a relationship. "The operation of these systems depends on estimating the risk of future exploitation by the harmdoer and the expected future value of the relationship."
**Their schematic function (my reading, not their equation).** P(revenge) rises with E (estimated future exploitation risk) and falls with V (expected value of the relationship): P(forgive) = h(V, E, apology, ...) with ∂h/∂V > 0 and ∂h/∂E < 0. Their paper sketches a computational architecture, which I did not read in full.
**Evidence, blunt.** Meta-analytic: Fehr, Gelfand & Nag (2010), "The road to forgiveness: a meta-analytic synthesis of its situational and dispositional correlates", *Psychological Bulletin* 136, 894-914, doi:10.1037/a0019993 `[abstract]`: 175 studies, 26,006 participants; strongest correlates of forgiveness were perceived intent (r = -.49), state empathy (r = .51), apology (r = .42) and state anger (r = -.41); situational variables explained more than victim dispositions; gender r = .01, age r = .06. These are the empirical weights for h(V, E, apology, ...). McCullough's value-of-the-relationship and apology predictions are supported by correlational and vignette studies `[standard]`; the cost-benefit decomposition has not, as far as I know, been fitted as an equation to field data.
**Revenge does not deliver what people expect.** Carlsmith, Wilson & Gilbert (2008), *JPSP* 95, 1316-1324, doi:10.1037/a0012165 (Crossref match; content `[standard]`): punishers expect revenge to feel good and it prolongs rumination.

### E2. Direct-reciprocity models: tit-for-tat, generous TFT, win-stay-lose-shift
**Citations.** Axelrod, R. & Hamilton, W. D. (1981). The evolution of cooperation. *Science* 211, 1390-1396. doi:10.1126/science.7466396. Molander, P. (1985). The optimal level of generosity in a selfish, uncertain environment. *J. Conflict Resolution* 29, 611-618. doi:10.1177/0022002785029004004. Nowak, M. & Sigmund, K. (1992). Tit for tat in heterogeneous populations. *Nature* 355, 250-253. doi:10.1038/355250a0. Nowak, M. & Sigmund, K. (1993). A strategy of win-stay, lose-shift that outperforms tit-for-tat in the Prisoner's Dilemma game. *Nature* 364, 56-58. doi:10.1038/364056a0. Wu, J. & Axelrod, R. (1995). How to cope with noise in the iterated prisoner's dilemma. *J. Conflict Resolution* 39, 183-189. doi:10.1177/0022002795039001008. Hilbe, C., Chatterjee, K. & Nowak, M. A. (2018). Partners and rivals in direct reciprocity. *Nature Human Behaviour* 2, 469-477. doi:10.1038/s41562-018-0320-9 (all Crossref matches; contents `[standard]`, not re-read this session; file 39 has the deterrence uses).
**Strategies `[standard]`.** Payoffs T > R > P > S. TFT: copy the partner's last move. **Generous TFT:** always reciprocate cooperation; after a defection cooperate with forgiveness probability q, where Nowak and Sigmund's (1992) value is q = min{1 - (T-R)/(R-S), (R-P)/(T-P)}, which gives q = 1/3 for Axelrod's payoffs (T, R, P, S) = (5, 3, 1, 0) `[secondary]`: confirmed against a secondary account that quotes the expression and credits Nowak & Sigmund 1992, and by arithmetic; the Nature paper itself was not read. Credit for the idea of optimal generosity under noise goes earlier to Molander (1985) `[abstract]`, who showed TFT degrades at arbitrarily low noise and that unconditional generosity repairs it. This is the cleanest forgiveness parameter in the literature: forgiveness is a number q in [0,1]. WSLS (Pavlov): repeat your last move if the payoff was R or T, switch if P or S; it beats TFT under noise because it corrects mistakes and exploits unconditional cooperators.
**Theorem-level facts `[standard]`.** TFT is not evolutionarily stable and is fragile to errors (two TFT players locked into alternating retaliation after one mistake); generosity q > 0 repairs that; WSLS wins in some tournament and replicator settings. Hilbe et al. extend to zero-determinant "partner" and "rival" strategies, building on Press, W. H. & Dyson, F. J. (2012), Iterated Prisoner's Dilemma contains strategies that dominate any evolutionary opponent, *PNAS* 109, 10409-10413, doi:10.1073/pnas.1206569109 (Crossref match; not read).
**Empirical standing.** Human subjects in repeated games behave as conditional cooperators with some generosity under noise, but the specific best-fitting strategy depends on the game and feedback; Dreber, A., Rand, D. G., Fudenberg, D. & Nowak, M. A. (2008), "Winners don't punish", *Nature* 452, 348-351, doi:10.1038/nature06723 (Crossref match), found that the most successful players did not use costly punishment `[standard]`. Fischbacher, Gächter & Fehr (2001), *Economics Letters* 71, 397-404, doi:10.1016/S0165-1765(01)00394-9 (Crossref match): about half of subjects are conditional cooperators `[standard]`.
**Translation.** Revenge is the operator Punish(i→j) with cost c_p to i and harm h to j; forgiveness is a continuous parameter q (generosity) or a relationship-value threshold (McCullough). A strategy is a map from histories to operators, and this is the existing formal language closest to an algebra of reciprocal acts. Its limits: emotions appear only as the strategy rule; there is no internal anger state decaying over time.

### E3. Costly and third-party punishment
**Citations.** Fehr, E. & Gächter, S. (2002). Altruistic punishment in humans. *Nature* 415, 137-140. doi:10.1038/415137a. Fehr, E. & Fischbacher, U. (2004). Third party punishment and social norms. *Evolution and Human Behavior* 25, 63-87. doi:10.1016/S1090-5138(04)00005-4 (Crossref match). Herrmann, B., Thöni, C. & Gächter, S. (2008). Antisocial punishment across societies. *Science* 319, 1362-1367. doi:10.1126/science.1153808. Henrich, J., McElreath, R., Barr, A., Ensminger, J., Barrett, C., Bolyanatz, A., Cardenas, J. C. et al. (2006). Costly punishment across human societies. *Science* 312, 1767-1770. doi:10.1126/science.1127333 (Crossref match; content `[standard]`). (The chapter the draft cited, doi:10.7551/mitpress/3232.003.0021, is Richerson, Boyd & Henrich, "Cultural evolution of human cooperation", not a punishment study; removed.)
**Claims `[standard]`.** People punish free-riders at a cost to themselves in one-shot public goods games, and this sustains contribution; punishment is also levied on cooperators in some societies (antisocial punishment, large in some sites and negligible in others). Third-party punishment shows the motive is not only personal revenge.
**Translation.** Indignation as the third-party trigger: i observes j's norm breach against k, i pays cost to punish j. This extends the dyadic revenge operator to a triadic operator with an observer.

---

## F. Indignation and moral outrage

### F1. Crockett (2017) and Brady et al.
**Citations.** Crockett, M. J. (2017). Moral outrage in the digital age. *Nature Human Behaviour* 1, 769-771. doi:10.1038/s41562-017-0213-3 (Crossref match; abstract not retrieved; content `[standard]`). Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A. & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS* 114, 7313-7318. doi:10.1073/pnas.1618923114 (`[abstract]`; also in file 27). Brady, Crockett & Van Bavel (2020). The MAD model of moral contagion. *Perspectives on Psychological Science* 15, 978-1010 doi:10.1177/1745691620917336 (Crossref match; preprint doi:10.31234/osf.io/pz9g6). Brady, McLoughlin, Doan & Crockett (2021). How social learning amplifies moral outrage expression in online social networks. *Science Advances* 7, eabe5641. doi:10.1126/sciadv.abe5641 (Crossref match; preprint doi:10.31234/osf.io/gf7t5).
**Content.** Crockett `[secondary]`: digital media enlarge the triggers of outrage (far more, and more extreme, reported violations than offline life supplies), lower the cost of expressing it, and raise its personal (reputational) reward, so expression can detach from the feeling; the same motive that punishes norm violations can be exploited by engagement-maximising feeds. Brady 2017 `[abstract]`: each moral-emotional word raised diffusion by about 20%, and the effect is bounded by group membership. Brady 2021 `[standard]`: expression of outrage is reinforced by likes and shares, i.e. a reinforcement-learning explanation of escalation.
**Trigger.** An observed norm breach against someone else; audience size and expected approval modulate expression.
**Equation.** Brady 2017's is the only one: a log-linear count model with diffusion rising about 20% per moral-emotional word (file 27). The learning account (expression probability updated by social feedback) is a reinforcement-learning rule of the same form as the trust update in D3, stated in prose and fitted to data in the 2021 study `[standard]`.
**Evidence, blunt.** Observational social-media data on three US issues in 2017 (Twitter), correlational; platform and period specific. Whether outrage expression online equals felt outrage is a separate, open question (Crockett's own point).
**Translation.** Outrage = third-party punish tendency with an audience term; its group-scale dynamics sit in files 18, 23 and 27 (diffusion, contagion).

---

## G. Compassion, empathic concern, empathic distress

### G1. Batson's empathy-altruism hypothesis
**Citations.** Batson, C. D. (2011). *Altruism in Humans*. Oxford University Press. doi:10.1093/acprof:oso/9780195341065.001.0001 (Crossref match). Cialdini, R. B., Brown, S. L., Lewis, B. P., Luce, C. & Neuberg, S. L. (1997). Reinterpreting the empathy-altruism relationship: when one into one equals oneness. *JPSP* 73, 481-494. doi:10.1037/0022-3514.73.3.481 (Crossref match). Maner, J. K., Luce, C. L., Neuberg, S. L., Cialdini, R. B., Brown, S. & Sagarin, B. J. (2002), *PSPB* 28, 1601-1610, doi:10.1177/014616702237586 (the Crossref hit title is "The Effects of Perspective Taking on Motivations for Helping: Still No Evidence for Altruism"; author list is my recollection).
**Claim `[standard]`.** Empathic concern (other-oriented feeling for a person in need) produces motivation whose ultimate goal is the other's welfare, not egoistic relief; Batson ran many experiments where escape was easy and high-empathy people still helped. Cialdini et al.: the effect is explained by self-other overlap (oneness), not altruism; Maner et al.: controlling for overlap, empathy effects vanish. The debate is unresolved.
**Appraisal / trigger.** Perceived need of another, attachment or perspective taking raising concern.
**Formal.** None.

### G2. Empathic distress vs compassion (Singer & Klimecki)
**Citations.** Singer, T. & Klimecki, O. M. (2014). Empathy and compassion. *Current Biology* 24, R875-R878. doi:10.1016/j.cub.2014.06.054 (`[abstract]`). Klimecki, O. M., Leiberg, S., Lamm, C. & Singer, T. (2013). Functional neural plasticity and associated changes in positive affect after compassion training. *Cerebral Cortex* 23, 1552-1561. doi:10.1093/cercor/bhs142 (Crossref match; content `[standard]`).
**Content.** Singer & Klimecki `[abstract]` define empathy as sharing another's feeling while retaining self-other distinction; without it, emotional contagion. `[standard]`: sharing another's suffering produces empathic distress (aversive, self-focused, withdrawal) while compassion (warmth, concern, approach) is a different state; compassion training shifts affect toward the positive (Klimecki).
**Operators.** Empathic distress leads to withdrawal; compassion leads to approach and helping. Two operators from the same trigger, selected by a regulation variable (self-other distinction, positive affect).
**Evidence, blunt.** Small training and fMRI samples; the "distress vs compassion" distinction rests on a handful of group studies from one lab group.

### G3. Empathy is motivated and group-bound
**Citations.** Zaki, J. (2014). Empathy: a motivated account. *Psychological Bulletin* 140, 1608-1647. doi:10.1037/a0037679 (`[abstract]`). Hein et al. (2010), *Neuron* 68, 149-160, doi:10.1016/j.neuron.2010.09.003 (`[abstract]`). Cikara, Bruneau & Saxe (2011), Us and them: intergroup failures of empathy, *Current Directions in Psychological Science* 20, 149-153, doi:10.1177/0963721411408713 (Crossref match; content `[standard]`). Cameron & Payne (2011), Escaping affect, *JPSP* 100, 1-15, doi:10.1037/a0021643 (Crossref match; content `[standard]`: motivated emotion regulation reduces compassion for large numbers of victims).
**Content.** Zaki `[abstract]`: empathy shifts with motives to avoid (suffering, material cost, competition) or approach (positive affect, affiliation, social desirability) engagement. Hein `[abstract]`: soccer fans' costly helping of an in-group member was predicted by anterior insula (empathic concern); not helping an out-group member was predicted by nucleus accumbens activity and negative evaluation of the other.
**Translation.** Empathic concern is gated by group membership and by cost. An algebra needs an explicit coupling-strength parameter between agents (in-group/out-group) that scales the transfer of another's state; this ties into the dyadic coupling terms of file 20.
**Evidence.** The group effect has multiple lab replications of the in-group bias in empathy `[standard]`. Effect sizes not reported here.

---

## H. Humiliation

### H1. Lindner, Hartling and the construct
**Citations.** Lindner, E. G. (2010). *Gender, Humiliation, and Global Security*. Praeger. doi:10.5040/9798400655951 (Crossref match; book content not read). Lindner's *Emotion and Conflict* (2009, Praeger) is cited in the literature (not checked this session). Hartling, L. M. & Luchetta, T. (1999). Humiliation: assessing the impact of derision, degradation, and debasement. *Journal of Primary Prevention* 19, 259-278. doi:10.1023/A:1022622422521 (Crossref match; the Humiliation Inventory instrument record is doi:10.1037/t73672-000).
**Claim `[standard]`.** Humiliation is the enforced lowering of a person or group's standing, perceived as unjust, and (Lindner) a precursor to violence: the key emotion in conflict. Note that the one experimental test below (Ginges & Atran 2008) did **not** find humiliation driving violence. The conceptual separation from shame is that humiliation is something done to you by another and is felt as undeserved.
**Evidence, blunt.** Mostly case-based and theory; measurement is by the Humiliation Inventory and similar; I found no meta-analysis, no experiment that isolates humiliation from other threats to status, and no equation. Lindner's work is influential in conflict-studies but outside the field's experimental mainstream.

### H2. Ginges & Atran: the inertia effect and sacred values
**Citations.** Ginges, J. & Atran, S. (2008). Humiliation and the inertia effect: implications for understanding violence and compromise in intractable intergroup conflicts. *Journal of Cognition and Culture* 8, 281-294. doi:10.1163/156853708x358182 (Crossref match; `[abstract]`: three studies of Palestinians in the West Bank and Gaza. Humiliation produced an **inertia effect**, a tendency to inaction that suppresses violent action and, paradoxically, also suppresses support for compromise. Study 1: more humiliated Palestinians were **less** supportive of suicide attacks; Study 2: a humiliation prime reduced expressed joy at hearing of attacks; Study 3: humiliation by peace deals lowered support for them, while Israeli symbolic compromises that reduced humiliation raised it. Conclusion: humiliation does not seem to contribute to political violence but does suppress support for conflict resolution). Ginges, J., Atran, S., Medin, D. & Shikaki, K. (2007). Sacred bounds on rational resolution of violent political conflict. *PNAS* 104, 7357-7360. doi:10.1073/pnas.0701768104 (`[abstract]`). Atran, S., Axelrod, R. & Davis, R. (2007). Sacred barriers to conflict resolution. *Science* 317, 1039-1040. doi:10.1126/science.1144241 (Crossref match; content `[standard]`).
**Content `[abstract]` (Ginges 2007).** Palestinian and Israeli samples: opposition to compromise over sacred issues rose when material incentives were offered ("backfire") and fell when the adversary made symbolic compromises on their own sacred values.
**Translation.** Humiliation acts as a damper on *all* action (violent or conciliatory), not a driver of retaliation. The relevant repair operator is non-economic: a symbolic act addressing the injured party's standing changes willingness to compromise where payments do not. This is the empirical core of treating humiliation and dignity as a state variable separate from material payoff. Rival explanation: the backfire is general to taboo trade-offs (Tetlock) `[standard]`.
**Evidence.** Field and survey experiments on a few thousand respondents in a specific conflict; the "inertia effect" replication status is unknown to me.

---

## I. Loneliness

Only as needed: loneliness belongs to file 22 (contact deficit, affiliation). Its role in this cluster is as the base: shame, pride and trust all presuppose being valued by others, and the sociometer (A4) says self-esteem is the gauge of that valuation.

---

## J. Closing table: drive → trigger → action tendency (operator) → equation → evidence

| Drive | Trigger (who did what to whom, before what audience) | Action tendency (operator on others) | Known equation | Evidence (blunt) |
|---|---|---|---|---|
| Shame | i's own act or trait is, or may be, devalued by audience A | Hide(i), Appease(i→A), withdraw | Intensity tracks audience devaluation: shame ≈ g(D_A) (Sznycer 2016); no g fitted | r = .67 to .79 across items, 3 countries `[abstract]`; Tignor-Colvin: shame-prosociality r about -.05 |
| Guilt | i's specific act harms j (internal, controllable attribution) | Apologise, repair(i→j), confess | Static: guilt aversion in utility (file 21, Battigalli-Dufwenberg) | Guilt-prosociality r = .13, k = 63; method-dependent |
| Embarrassment | i breaches convention before audience A | Appease(i→A): display that raises A's trust, lowers sanction | None | Lab studies; Feinberg 2012 observers trust embarrassed targets more `[abstract]` |
| Pride (authentic / hubristic) | i's act or trait is valued by audience A (internal attribution) | Advertise(i→A); seek rank by prestige or dominance | Pride ≈ f(forecast audience valuation) (Sznycer 2017) | mean r = .82 local, .75 foreign, 16 countries `[abstract]` |
| Envy (benign / malicious) | j has self-relevant advantage over i | Move-up(i) if attainable; Pull-down(i→j) if not | Fehr-Schmidt disadvantageous term (file 21) | Benign vs malicious: small experiments `[abstract]` |
| Schadenfreude | Misfortune to envied or rival j (esp. out-group, i threatened) | Gloat, withhold help | Sign flip of ∂U_i/∂(outcome_j) (Levine, file 21) | fMRI + survey `[abstract]` |
| Jealousy | Rival r threatens i's bond with partner p | Guard(i→p), derogate(i→r), aggression | None | Small sex difference holds on continuous measures (Sagarin 2012, g ≈ .26 `[secondary]`); adaptationist explanation contested |
| Gratitude | j intentionally benefits i at a cost to j | Reciprocate(i→j); pass on(i→k) | Nowak-Roch: s = q/(1-p); r > c/b `[read]` | Theory proof `[read]`; behavioural effect plausible, specific predictions untested |
| Trust | i's belief that j will reciprocate, from prior and history | Send(i→j, x) | b_{t+1} = b_t + α(o_t - b_t) (RL) or Beta posterior; fitted by Chang 2010 `[abstract]` | One lab study of model fits; meta-analyses of correlates only `[abstract]` |
| Trust repair | j violated i's trust | Apologise or deny; demonstrate | None (qualitative asymmetry) | Scenario studies |
| Revenge | j imposed a cost on i (or kin/ally) | Punish(i→j) at cost | In GTFT, defect after a defection with probability 1-q `[standard]`; McCullough: h(V, E) schematic | Evolutionary theory strong; human fit mixed |
| Forgiveness | j harmed i, but relationship value V high, exploit risk E low, apology given | Inhibit revenge, signal benevolence | GTFT q = min{1-(T-R)/(R-S), (R-P)/(T-P)} (Nowak & Sigmund 1992) `[secondary]`; WSLS rule | Fehr, Gelfand & Nag 2010: intent r = -.49, empathy .51, apology .42, anger -.41 `[abstract]` |
| Indignation / outrage | j breaches norm against k, observed by i and audience | Third-party Punish(i→j), express | Diffusion +20% per moral-emotional word (Brady 2017); RL account of escalation | Observational Twitter data `[abstract]`; Crockett argument `[standard]` |
| Compassion | k suffers; i has low self-focus, perspective taking | Approach, help(i→k) | None | Batson vs Cialdini debate unresolved |
| Empathic distress | Same trigger, with weak self-other separation | Withdraw | None | Small training and fMRI studies |
| Humiliation | j or group G lowers i's (or i's group's) standing unjustly | Inertia: suppresses both violent action and support for compromise (Ginges & Atran 2008); symbolic repair restores support | None | Case-based theory (Lindner) vs survey experiments that find no link to violence (Ginges & Atran 2008 `[abstract]`); Ginges 2007 sacred values `[abstract]` |

---

## K. What exists vs what does not (blunt)

**What exists.**
- One closed-form theorem with proof for a drive in this cluster: Nowak & Roch on gratitude (r > c/b; b/c > 10/7 spatial) `[read]`.
- A forgiveness parameter in evolutionary game theory (q in generous tit-for-tat; win-stay-lose-shift), with robustness results; no human measurement of q as a personal trait.
- Learning models for trust (RL or Beta update), fitted in at least one study, and image-scoring/standing models for reputation.
- A calibration law for shame and pride against audience valuation, cross-culturally, as correlations.
- Appraisal trees (Tracy & Robins; Smith & Kim; van de Ven) that map appraisal values to labelled emotions. These are discrete and typed.
- Static psychological-game models (file 21) of guilt and envy as functions of beliefs and payoffs.
- Large-scale observational evidence on outrage diffusion (Brady) and meta-analyses of correlates for guilt/shame, trust, gratitude interventions.

**What does not exist.**
- **No time-course law for any of these drives.** No accepted equation for how fast shame, anger, envy, gratitude or humiliation rise and decay after a trigger, and no half-life for forgiveness. The affect-dynamics literature (file 27) measures autoregression in general moods. *Corrected:* durations have been **measured**, though not modelled: Verduyn, P. & Lavrijsen, S. (2015). Which emotions last longest and why: the role of event importance and rumination. *Motivation and Emotion* 39, 119-127, doi:10.1007/s11031-014-9445-y (Crossref match; content `[secondary]`): across 27 emotions, shame was among the shortest and guilt outlasted shame; duration rose with event importance and rumination. Computational appraisal models also give emotions explicit decay (Marsella, S. C. & Gratch, J. (2009). EMA: a process model of appraisal dynamics. *Cognitive Systems Research* 10, 70-90, doi:10.1016/j.cogsys.2008.03.005; Crossref match, not read), though with engineered rather than fitted constants.
- **No coupled equation set across these drives.** Nobody has written shame, guilt, pride, envy, trust and revenge in one system where they affect each other (for example, trust falling when envy rises, or pride modulating forgiveness). *Qualified:* coupled dynamical models of **dyadic affect** do exist and were missing from this survey: Gottman, J. M., Murray, J. D., Swanson, C. C., Tyson, R. & Swanson, K. R. (2002). *The Mathematics of Marriage: Dynamic Nonlinear Models*. MIT Press, doi:10.7551/mitpress/4499.001.0001; and Gottman, Swanson & Swanson (2002), A general systems theory of marriage: nonlinear difference equation modeling of marital interaction, *PSPR* 6, 326-340, doi:10.1207/s15327957pspr0604_07 (both Crossref matches; content `[standard]`): each partner's affect is a difference equation with an uninfluenced set point, inertia, and an influence function of the other's last affect, fitted to coded couple conversations. One valence variable per person, not distinct drives, but it is the fitted coupled-affect precedent the algebra should start from.
- **No quantification of audience.** The audience term is the key input for shame, pride, embarrassment and outrage, yet "audience valuation" has been measured only by rating items on a scale. Who counts as audience (size, power, closeness), how multiple audiences combine, and how it decays with distance are all unmodelled.
- **No fitted jealousy, humiliation, indignation or compassion model.** Jealousy and humiliation have no established formalisation (there are scattered evolutionary models of mate guarding and a few one-off game-theoretic jealousy papers, none widely used or fitted to human data); compassion has verbal theory.
- **No validated individual-level prediction.** Everything quantitative is at the item or population level; the trait measures give r around .1.
- **No treatment of triadic operands except as a bolt-on** (third-party punishment, jealousy), which matters because an algebra whose basic operator is dyadic cannot state them.

**Candidate first equations for the algebra (my synthesis, not from any one source).**
1. S_self-conscious(i, act, A) = g(D_A(act)), with g monotone, one per emotion (shame: negative D; pride: positive D). Source for the shape: Sznycer 2016 and 2017.
2. Trust belief update: b ← b + α±(o - b), with α+ ≠ α- the asymmetry parameter. Source: Chang 2010 (generic form).
3. Gratitude as the parameter pair (p, q) with the condition r > c/b. Source: Nowak-Roch `[read]`.
4. Forgiveness as q in generous reciprocity, or h(V, E) in McCullough's form.
5. A typed appraisal front end: attribution (global/specific; attainable/unattainable) selects the operator (shame vs guilt; benign vs malicious envy). Source: Tangney; Tracy-Robins; van de Ven.

---

## Unconfirmed

Revised in validation, 2026-10-29. Items resolved since the draft (GTFT formula, Buss and Maner author lists, and the journal DOIs for Mayer, Kim, Schweitzer, Fehr-Gelfand-Nag, Harris, Brady 2020/2021, Johnson-Mislin, Dreber, Fehr-Fischbacher, Fischbacher-Gächter-Fehr, Hartling-Luchetta) have been moved into the text.

- Jøsang & Ismail (2002), "The Beta Reputation System", Bled eConference: a conference paper with no DOI found in Crossref; existence is well attested but not checked here. The Crossref hit the draft gave (doi:10.1007/978-3-540-45229-4_18) is a different paper (Ismail, Boyd, Jøsang & Russell 2003, "A security architecture for reputation systems").
- GTFT formula: confirmed only via a secondary source and arithmetic; Nowak & Sigmund (1992) not read.
- Sagarin et al. (2012) effect sizes: from a secondary summary, not the paper.
- Crockett (2017): no abstract (it is a short comment); content from secondary summaries.
- Abstracts not retrieved: Johnson & Mislin 2011; Schweitzer et al. 2006; Hein et al. 2010; Cheng et al. 2010; Ohtsuki & Iwasa 2004; Dirks & Ferrin 2002. Claims about these remain `[standard]`.
- Not read at source: Tracy & Robins 2004 decision tree (node order and the treatment of embarrassment are the standard account, unverified); Tangney 2007 in full; McCullough et al. 2013 computational sketch; Chang et al. 2010 fitted model variants (whether asymmetric learning rates won is unverified); Singer & Klimecki details; Lindner's books; Gottman et al. 2002 equations.
- "Carpenter 2012 sex-difference meta-analysis" was listed in the draft's Unconfirmed section but cited nowhere in the text; not located, dropped.
- Replication status of: benign/malicious envy effects, the inertia effect, Feinberg embarrassment signal, Cialdini vs Batson (contested, not replicated away).

## Validation log (2026-10-29)

Method: every DOI resolved against api.crossref.org; abstracts from Crossref, Europe PMC and OpenAlex; Nowak & Roch full text re-read on PMC; targeted web searches for the rest.

- ✓ Tangney, Stuewig & Mashek 2007 (DOI, authors).
- ✓ Tignor & Colvin 2017 (k = 63, r = .13; k = 47, r = -.05, p = .07; moderators, all match abstract).
- ✓ Baumeister, Stillwell & Heatherton 1994.
- ✓ Tracy & Robins 2004 *Psych Inquiry* (exists; tree content still `[standard]`).
- ✎ Tracy & Robins 2004 *Psych Sci* "Show your pride": was credited with cross-cultural recognition; it tested US judges only. Cross-cultural result credited to Tracy & Robins 2008 *JPSP* (added).
- ✎ Authentic/hubristic pride scale: PsycTESTS record replaced by the journal paper, Tracy & Robins 2007 *JPSP*.
- ✓ Cheng, Tracy & Henrich 2010; ✓ Cheng et al. 2013 (abstract matches).
- ✓ Sznycer et al. 2017 PNAS pride (16 countries, n = 2,085, 25 acts/traits, r = +.82 local, +.75 foreign: exact).
- ✓ Sznycer et al. 2016 PNAS shame (r = .69 US, .79 India, .67 Israel; cross-country tracking; sadness/anxiety specificity: exact). ✎ full author list added; 2024 preprint credited to Sznycer & Landers.
- ✓ Leary et al. 1995.
- ✎ Keltner 1995: upgraded to `[abstract]` (five studies; status moderation of perception).
- ✓ Keltner & Buswell 1997 (five accounts match); ✓ Feinberg, Willer & Keltner 2012.
- ✓ Smith & Kim 2007 (definition quoted correctly).
- ✓ van de Ven et al. 2011 PSPB (four studies, attainability in Study 4: exact); ✓ van de Ven et al. 2011 JCR.
- ✎ Leach et al. 2003: honest-expression-norm effect narrowed to its actual conditions.
- ✓ Takahashi et al. 2009; ✓ Cikara, Botvinick & Fiske 2011.
- ✎ Bault et al. 2011: pages were 8478-8483, correct 16044-16049; title added.
- ✓ Buss et al. 1992 (authors now confirmed); ✓ DeSteno & Salovey 1996.
- ✎ Harris 2003: the "malformed" DOI is the registered one and resolves.
- ✎ Sagarin et al. 2012: draft claimed continuous measures show little or no sex difference; the meta-analysis of continuous measures found a small theory-consistent difference. Critique and table row corrected.
- ✓ McCullough et al. 2001 (three functions match abstract).
- ✎ Bartlett & DeSteno 2006: upgraded to `[abstract]`; added the stranger-helping result that links it to upstream reciprocity.
- ✓ Algoe 2012.
- ✎ Davis et al. 2016: pages 20-33 → 20-31; effect sizes match abstract.
- ✓ Nowak & Roch 2007 `[read]`, re-verified at source: upstream alone reduces cooperativity; invasion barrier x̂ = [c/(b-c)][(1-r)/r], x̂ < 1 iff r > c/b; matrix s_i u_j; three two-strategy cases; spatial b/c > 4 (S(0,1)) and b/c > 10/7 (S(1,1)), h(0) = 4, h(1) = 10/7. All exact.
- ✓ Nowak & Sigmund 1998; ✓ Wedekind & Milinski 2000; ✓ Panchanathan & Boyd 2004; ✓ Ohtsuki & Iwasa 2004; ✓ Nowak & Sigmund 2005.
- ✓ Rousseau et al. 1998. ✎ Mayer et al. 1995: journal DOI found (10.2307/258792).
- ✓ Colquitt, Scott & LePine 2007; ✓ Dirks & Ferrin 2002.
- ✎ Johnson & Mislin 2011: journal DOI found.
- ✓ Berg, Dickhaut & McCabe 1995.
- ✓ Chang, Doll, van 't Wout, Frank & Sanfey 2010 (authors, venue, abstract claims exact; fitted variants unread).
- ? Jøsang & Ismail 2002 (no DOI; Crossref hit was a different paper).
- ✓ King-Casas et al. 2005; ✓ Delgado, Frank & Phelps 2005.
- ✎ Kim et al. 2004: journal DOI found; the claim conflated two findings (violation type; later evidence of guilt or innocence), now stated separately from the abstract.
- ✎ Schweitzer, Hershey & Bradlow 2006: journal DOI found.
- ✓ McCullough, Kurzban & Tabak 2013 (abstract quote exact); ✓ McCullough 2008 book (review DOI correctly flagged); ✓ McCullough, Worthington & Rachal 1997.
- ✎ Fehr, Gelfand & Nag 2010: journal DOI found; effect sizes added from abstract.
- ✓ Carlsmith, Wilson & Gilbert 2008.
- ✓ Axelrod & Hamilton 1981; ✓ Molander 1985 (now credited for prior work on generosity); ✓ Nowak & Sigmund 1993; ✓ Wu & Axelrod 1995; ✓ Hilbe, Chatterjee & Nowak 2018.
- ✎ Nowak & Sigmund 1992 GTFT formula: recalled formula confirmed via secondary source quoting it with this attribution, and q = 1/3 at (5,3,1,0); tag `[secondary]`.
- ✎ Press & Dyson 2012: citation and DOI added.
- ✎ Dreber et al. 2008: DOI and authors added. ✎ Fischbacher, Gächter & Fehr 2001: journal DOI. ✓ Fehr & Gächter 2002. ✎ Fehr & Fischbacher 2004: journal DOI. ✓ Herrmann, Thöni & Gächter 2008.
- ✗ "Henrich et al." book-chapter DOI removed: it is Richerson, Boyd & Henrich on cultural evolution, not a punishment study; replaced with Henrich et al. 2006 *Science* "Costly punishment across human societies".
- ✎ Crockett 2017: exists, authorship correct; content broadened (triggers, cost, reward), tag `[secondary]`.
- ✓ Brady et al. 2017. ✎ Brady, Crockett & Van Bavel 2020 and Brady et al. 2021: journal DOIs found.
- ✓ Batson 2011; ✓ Cialdini et al. 1997; ✓ Maner et al. 2002 (authors confirmed).
- ✓ Singer & Klimecki 2014 (self-other distinction vs contagion matches abstract); ✓ Klimecki et al. 2013.
- ✓ Zaki 2014 (motives match abstract); ✓ Hein et al. 2010; ✓ Cikara, Bruneau & Saxe 2011; ✓ Cameron & Payne 2011.
- ✓ Lindner 2010 (exists; unread).
- ✎ Hartling & Luchetta 1999: wrong title; the journal article located (*J. Primary Prevention* 19, 259-278).
- ✎ Ginges & Atran 2008: **content reversed.** Draft said humiliation increases persistence in violent action; the abstract says humiliation produced an inertia effect that *reduced* support for suicide attacks and also reduced support for compromise. H1, H2 and the table corrected.
- ✓ Ginges et al. 2007 (abstract matches); ✓ Atran, Axelrod & Davis 2007.
- ✎ Closing claims: "no time-course" qualified (Verduyn & Lavrijsen 2015 measured durations; EMA has decay); "no coupled system" qualified (Gottman et al. 2002 coupled nonlinear difference equations for dyadic affect, fitted); "no formalisation at all" for jealousy softened.
- Missing work added: van de Ven et al. 2009 *Emotion* (the original benign/malicious envy paper); Tracy & Robins 2008; Gottman et al. 2002 (book and *PSPR*); Verduyn & Lavrijsen 2015; Marsella & Gratch 2009; Henrich et al. 2006; Press & Dyson 2012. Still absent and worth a look: Strogatz-style coupled love ODEs (toy precedents); Fessler's and Gilbert's work on shame as social rank (pride/shame ranking models); Frank's *Passions Within Reason* (1988), the commitment-device account of guilt, anger and envy.

**Verdict.** Bibliographically strong: all 82 DOIs resolve, and every one points at the work claimed except the "Henrich et al." chapter (the draft had already flagged its own preprint, reprint and wrong-paper hits honestly); authorship is right throughout, and the one `[read]` paper (Nowak & Roch) is reported exactly. The weaknesses are in the `[standard]` content tags. Two of them had the finding backwards or misplaced: Ginges & Atran on humiliation, and Sagarin on jealousy measures. One credited a cross-cultural result to the wrong Tracy & Robins paper. Treat every remaining `[standard]` tag as a lead to check, not a finding.
