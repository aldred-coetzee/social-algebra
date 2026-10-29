# Prior work 17: the science of specific drives (curiosity, fear, desire, and candidates)

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: drives as dynamical quantities, with triggers, dynamics, interactions and social spread. This serves the new aim: an algebra of basic human and group drives that composes into equations, supports theorems, and is used to predict or control behaviour.

**Method note.** Every citation below has a bibliographic record I found by search in this session (publisher, PubMed, PMC, university repository, or arXiv). No full text was read except where stated. So every description is **[from abstract/standard account]** unless a line says **[read]**. Nothing here is tagged **[read]**. Equations are written from the field's standard accounts and must be checked against the paper before use. "Replication status" notes come from search results, not from my own reading of the replication papers.

**Summary.** The drive literature is large, mostly verbal, and weakly formal. Only reinforcement-learning curiosity (Schmidhuber, Oudeyer, Pathak) has executable equations. The defensive-imminence account of fear (Fanselow, Mobbs) is an ordinal staging plus borrowed RL vocabulary, with no equations confirmed, and Berlyne's inverted U is a qualitative curve (the two-sigmoid form is the standard account). *(Corrected in validation: the draft credited all three with "real mathematics".)* The rest (desire, status, belonging, power, anger) is verbal theory plus experiments, several with replication problems. Almost nothing treats a drive as a quantity held by a person and acted on by another person's acts. That is the gap social-algebra would fill. The one sociological finding that bears directly on the aim: drives spread between people (emotion contagion, fear learning by observation and instruction, mimetic desire), but the formal treatments of that spread are thin.

---

## A. Curiosity

### A1. Berlyne: collative variables and the inverted U

**Citation.** Berlyne, D. E. (1960). *Conflict, Arousal, and Curiosity*. McGraw-Hill. Also Berlyne (1970), "Novelty, complexity, and hedonic value", *Perception & Psychophysics* 8(5), 279-286, DOI 10.3758/BF03212593 *(confirmed via Crossref in validation)*.

**Verified.** Not the book itself. Secondary sources found in search: a Frontiers in Human Neuroscience article (https://www.frontiersin.org/articles/10.3389/fnhum.2016.00536/full), a PMC article (https://pmc.ncbi.nlm.nih.gov/articles/PMC5095118), and the "Computational Curiosity" book draft (https://arxiv.org/pdf/1502.04780). They agree on the points below.

- **Trigger.** Collative variables (novelty, complexity, uncertainty, conflict), so called because they require comparing stimulus elements with each other or with memory.
- **Dynamics.** Arousal potential has an inverted-U relation to hedonic value (the Wundt curve): too little gives boredom, too much gives anxiety, intermediate gives curiosity and pleasure. Standard account: Berlyne explained the U as the difference of two sigmoid systems, a reward system that engages at lower arousal and an aversion system that engages at higher arousal. [from abstract/standard account]
- **Interaction.** In Berlyne's theory, aversion is the high-arousal end of the same arousal-potential dimension, so curiosity and anxiety are one scale, not two drives. This is the cleanest *theoretical* form of "curiosity vs fear" [T]; the curves later measured (A5, Kang 2009, Marin 2016) vary complexity or knowledge, not threat.
- **Social transmission.** None in Berlyne.
- **Empirical standing.** Tested on patterns, paintings and melodies. Marin, Lampatz, Wandl & Leder (2016, *Front. Hum. Neurosci.* 10:536, "Berlyne revisited") found an inverted U between complexity and beauty **for music only**; for paintings beauty rose roughly linearly with complexity, and pleasantness fell with complexity in music (non-significant in paintings). So the curve is not uniformly confirmed. An inverted U in information content also appears in infant looking (A5) and in adult curiosity against confidence (Kang et al. 2009, A2) — these are complexity/knowledge curves, not fear curves.
- **Operand/operator.** Operand: a stimulus with a scalar "arousal potential" and an agent with an optimum. Operator: exposure to a stimulus. Because the optimum moves with experience, exposure changes the agent. That gives a state-changing operator on a person, which the role-algebra tradition lacks.

### A2. Loewenstein 1994: information-gap theory

**Citation.** Loewenstein, G. (1994). The psychology of curiosity: a review and reinterpretation. *Psychological Bulletin* 116(1), 75-98. Record: https://stafforini.com/works/loewenstein-1994-psychology-curiosity-review/.

**Verified.** Citation and abstract-level argument from search results; the CMU PDF's text did not come back.

- **Trigger.** Noticing a gap between what one knows and what one wants to know. Curiosity is a cognitively induced deprivation. Some baseline knowledge is required; one is not curious about what one knows nothing of.
- **Dynamics.** Standard account: curiosity rises with the salience of the gap and, for a fixed reference point, rises as knowledge approaches it (the gap looks closable); closing the gap relieves the deprivation. [from abstract/standard account] *Validation correction:* Loewenstein 1994 does not itself report an inverted U. The inverted U of curiosity against confidence is an empirical result of Kang, Hsu, Krajbich, Loewenstein, McClure, Wang & Camerer (2009), "The wick in the candle of learning", *Psychological Science* 20(8), 963-973 (curiosity peaks at moderate confidence; replicated by Spitzer et al. 2023, who found importance of the information turns it into a negative slope) — secondary sources only.
- **Interaction.** Treated as aversive deprivation like hunger, so it can compete with other deprivations. Not worked out.
- **Social transmission.** Not in the abstract. A speaker can create a gap in another person (teasers, cliffhangers), which makes this an operator on another person's state.
- **Empirical standing.** Widely cited; the gap-and-baseline claim is supported by later work (Kidd & Hayden, below) but I did not check the experimental record.
- **Operand/operator.** Operand: a person's knowledge state and question set. Operator: "open a gap in X", "close a gap in X" as acts between persons. This is a good candidate for the first interaction operator.

### A3. Kidd & Hayden 2015 and Gottlieb et al. 2013: reviews

**Citations.**
- Kidd, C. & Hayden, B. Y. (2015). The psychology and neuroscience of curiosity. *Neuron* 88(3), 449-460. PMC4635443 (https://pmc.ncbi.nlm.nih.gov/articles/PMC4635443).
- Gottlieb, J., Oudeyer, P.-Y., Lopes, M. & Baranes, A. (2013). Information-seeking, curiosity, and attention: computational and neural mechanisms. *Trends in Cognitive Sciences* 17(11), 585-593, DOI 10.1016/j.tics.2013.09.001. PMC4193662 (https://pmc.ncbi.nlm.nih.gov/articles/PMC4193662).

**Verified.** Abstracts and summaries only.

- Kidd & Hayden: no agreed definition of curiosity; they adopt "a drive state for information" and read it through Tinbergen's four questions. They note a shortage of standard tasks that manipulate curiosity.
- Gottlieb et al.: information seeking can be independent of expected payoff; learning itself appears reinforcing; the mechanisms are described as "in their infancy".
- **Reading for the algebra.** The field itself says curiosity is poorly delimited. A formal treatment will have to choose a definition (information-gap, learning-progress, or prediction-error) rather than inherit one.

### A4. Gruber, Gelman & Ranganath 2014

**Citation.** Gruber, M. J., Gelman, B. D. & Ranganath, C. (2014). States of curiosity modulate hippocampus-dependent learning via the dopaminergic circuit. *Neuron* 84(2), 486-496, DOI 10.1016/j.neuron.2014.08.060 *(confirmed via Crossref)*. Record: https://pmc.ncbi.nlm.nih.gov/articles/PMC4252494/.

**Verified.** Findings from the search summary: memory is better for items one is curious about and for incidental material learned during high-curiosity states; midbrain and nucleus accumbens are more active.

- **Interaction found.** Curiosity amplifies learning of unrelated material (curiosity to memory). The search returned nothing on fear or threat in this paper.

### A5. Kidd, Piantadosi & Aslin 2012: the Goldilocks effect

**Citation.** Kidd, C., Piantadosi, S. T. & Aslin, R. N. (2012). The Goldilocks effect. *PLoS ONE* 7(5): e36399, DOI 10.1371/journal.pone.0036399. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3359326/.

**Verified.** Abstract-level from search results: infants aged 7-8 months look away most from sequences rated by an ideal-learner model as very simple or very complex (complexity = negative log probability). The authors read it as a preference for intermediate rates of information intake.

- **Dynamics.** An inverted U in surprisal, fitted by a model, which is more formal than Berlyne's.
- **Empirical standing.** Two experiments with 7-8-month-old infants (72 in total per a press summary, not checked against the methods section). Replication status not checked. Note the variable is information content of visual sequences, not threat.

### A6. Schmidhuber: compression progress

**Citation.** Schmidhuber, J. (2010). Formal theory of creativity, fun, and intrinsic motivation (1990-2010). *IEEE Transactions on Autonomous Mental Development* 2(3), 230-247. PDF copy: https://www.ece.uvic.ca/~bctill/papers/ememcog/Schmidhuber_2010.pdf.

**Verified.** Abstract-level summary from search results. The PDF was not opened.

- **Trigger and dynamics.** An agent has a predictor/compressor of its history and a reinforcement learner. Intrinsic reward is the *improvement* of the compressor, not its error. Standard account: r(t) = C(h, before) - C(h, after), the drop in compressed length (or in code cost) caused by learning from the latest data. [from abstract/standard account]
- **Consequence.** Reward is zero for the fully known and for the unlearnable (noise), and highest in between, which reproduces an inverted U (A1, A5) without postulating it.
- **Social transmission.** None.
- **Operand/operator.** Operand: an agent with a model. Operator: any act that supplies data. Same operator form as A2.

### A7. Oudeyer & Kaplan, and Pathak et al.: intrinsic motivation in RL

**Citations.**
- Oudeyer, P.-Y. & Kaplan, F. (2007). What is intrinsic motivation? A typology of computational approaches. *Frontiers in Neurorobotics* 1:6, DOI 10.3389/neuro.12.006.2007. https://pmc.ncbi.nlm.nih.gov/articles/PMC2533589/.
- Pathak, D., Agrawal, P., Efros, A. A. & Darrell, T. (2017). Curiosity-driven exploration by self-supervised prediction. ICML 2017, pp. 2778-2787; arXiv:1705.05363.

**Verified.** Oudeyer & Kaplan: abstract and a commentary summary (Weber 2008, DOI 10.3389/neuro.12.001.2008) that calls the paper a classification of equations extending the standard reward function. Pathak: arXiv abstract page and the ICML record.

- **Oudeyer & Kaplan.** A typology of intrinsic-reward formulas: novelty, prediction error, learning progress (change in error over time), information gain, and others. Standard account: learning progress is r = E(t - tau) - E(t), the fall in prediction error over a window. [from abstract/standard account] They criticise psychological accounts as non-operational and mutually inconsistent.
- **Pathak et al.** The curiosity reward is the prediction error in a learned feature space, where the features come from an inverse-dynamics model so they ignore parts of the world the agent cannot influence. Standard account: r = (eta/2) * ||phi_hat(s') - phi(s')||^2. [from abstract/standard account] Tested in VizDoom and Super Mario.
- **Reading.** These supply *the only executable curiosity equations in the literature*. They are agent-level, single-agent, and say nothing about people affecting each other's curiosity.

---

## B. Fear

### B1. LeDoux: two systems

**Citation.** LeDoux, J. E. & Pine, D. S. (2016). Using neuroscience to help understand fear and anxiety: a two-system framework. *American Journal of Psychiatry* 173(11), 1083-1093 *(confirmed via Crossref)*. https://ajp.psychiatryonline.org/doi/full/10.1176/appi.ajp.2016.16030353. Critique: https://ajp.psychiatryonline.org/doi/10.1176/appi.ajp.2017.17070818 (2017 letter).

**Verified.** Abstract-level and a news summary (https://www.nimh.nih.gov/news/science-updates/2016/circuitry-for-fearful-feelings-behavior-untangled-in-anxiety-disorders).

- **Claim.** Conscious fear (cortical circuits) and defensive behaviour and physiology (subcortical, largely outside awareness) are separate systems. "Fear" the feeling is not the cause of "fear" the response.
- **Disputed.** A 2017 letter argues feelings and physiology are correlated, one integrated response.
- **Implication.** An algebra must decide whether a drive is the felt state, the behavioural disposition, or both. They can diverge.

### B2. Fanselow & Lester; Mobbs et al.: threat imminence

**Citations.**
- Fanselow, M. S. & Lester, L. S. (1988). A functional behavioristic approach to aversively motivated behavior: predatory imminence as a determinant of the topography of defensive behavior. In R. C. Bolles & M. D. Beecher (eds), *Evolution and Learning*, Erlbaum. *(Reference as recalled; the search returned only later reviews and the Fanselow lab page, https://fanselowlab.psych.ucla.edu/predatory-imminence-continuum.)*
- Mobbs, D., Headley, D. B., Ding, W. & Dayan, P. (2020). Space, time, and fear: survival computations along defensive circuits. *Trends in Cognitive Sciences* 24(3), 228-241, DOI 10.1016/j.tics.2019.12.016. https://resolver.caltech.edu/CaltechAUTHORS:20200204-073015965.

**Verified.** Mobbs et al.: abstract via Caltech and MPI records. Fanselow: lab summary and secondary reviews.

- **Formal structure.** A one-dimensional ordering by proximity of threat: pre-encounter (mild fear, behaviour reorganised, e.g. meal patterns), post-encounter (moderate, freezing; amygdala to ventral PAG), circa-strike (very high, vigorous active defence; dorsolateral PAG and superior colliculus). The post-encounter and circa-strike circuits inhibit each other, giving fast switching.
- **Mobbs et al. 2020** (abstract checked in validation). Decisions vary with spatiotemporal scale of threat: proximal threats narrow the decision space and rely on **model-free** (fast, reflexive) computation; distal threats allow **model-based** computation (affective prospection, replay, planning); the two are intertwined, and model-based processing in safe periods shapes later model-free responses; the goal is a distributed defensive circuit that selects the optimal policy. The "population codes" claim of the earlier draft is not in the abstract and is removed. **No equations in the abstract; whether the full text gives a formal model is unconfirmed** — the RL model-free/model-based split is the formal vocabulary it borrows.
- **Mobbs, Hagan, Dalgleish, Silston & Prévost (2015)**, "The ecology of human fear: survival optimization and the nervous system", *Frontiers in Neuroscience* 9:55, DOI 10.3389/fnins.2015.00055 (added in validation, abstract only). Proposes a Survival Optimization System whose stages run from threat orienting, through threat assessment, to fast fight-or-flight under imminent attack, with the nervous system cast as reducing surprise by simulating threats and building safe environments. Verbal staging, no equations seen.
- **Interaction.** Imminence orders defences; it does not model fear against desire. Circa-strike overrides everything below it.
- **Social transmission.** Not in these papers. See B5.
- **Operand/operator.** Operand: an agent with a scalar imminence input and a mode that is a function of it. Operator: anything that moves imminence (appear, approach, withdraw, warn). This is a natural threshold-mode state machine and the best fit for a discrete-state algebra.

### B3. Öhman & Mineka: the fear module

**Citation.** Öhman, A. & Mineka, S. (2001). Fears, phobias, and preparedness: toward an evolved module of fear and fear learning. *Psychological Review* 108(3), 483-522, DOI 10.1037/0033-295X.108.3.483.

**Verified.** Bibliographic record and summaries only (search results from 1cademy, cybsafe, Wikipedia on preparedness).

- **Claim.** Fear learning is selective: evolutionarily relevant stimuli (snakes, spiders, angry faces) condition faster and extinguish more slowly than neutral ones; the module is automatic and relatively immune to conscious control. Conditioned responses to masked fear-relevant stimuli have been reported. (Wording follows the Wikipedia article 'Preparedness', CC BY-SA 4.0.)
- **Criticism.** Davey (1995, *Behavioral and Brain Sciences* 18(2), 289-297) argued the effect reflects information-processing biases, not preparedness.
- **Empirical standing.** Disputed in the search results; I did not assess it.

### B4. Terror management theory

**Evidence found.** Klein et al. 2022, "Many Labs 4: Failure to replicate mortality salience effect with and without original author involvement", *Collabra: Psychology* 8(1), 35271, DOI 10.1525/collabra.35271 (21 labs, 2,220 participants, target Greenberg et al. 1994) did not reproduce the mortality-salience effect on worldview defence under any condition, so it could not say whether author involvement helps; the authors suggest a false positive or unknown/vanished boundary conditions. Haaf, Hoogeveen, Berkhout, Gronau & Wagenmakers (2023, *AMPPS*, DOI 10.1177/25152459231182318) ran a Bayesian multiverse reanalysis in which most comparisons favoured no effect (https://pure.uva.nl/ws/files/332429930/ManyLabs_4_Reanalysis.pdf; https://www.cos.io/blog/many-labs-4-failure-replicate-mortality-salience-effect-and-without-original-author-involvement). Treger, Benau & Timko (2023), "Not so terrifying after all?", *PLoS ONE* 18(5): e0285267: five failed replications, pooled effect not different from zero (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10168577/). Burke, Martens & Faucher (2010, *PSPR* 14(2), 155-195) meta-analysis supported the effect, but a p-curve analysis (Chen et al. 2022, cited by Arendsen et al.) suggests published effects are inflated. Arendsen, Brugman, van Koningsbruggen & Fransen (2025), *International Journal of Consumer Studies* 49(3) e70056: 70 studies, 125 effects, g = 0.21 [0.14, 0.28] (confirmed in the PDF). Authors of the replication say the result does not prove the effect absent.

- **Original claims (not retrieved in this session).** Greenberg, Pyszczynski & Solomon's theory predicts that reminders of death raise defence of one's culture's worldview and self-esteem. I did not find the original papers; the claim is from the standard account. [from abstract/standard account]
- **Verdict for the algebra.** Treat TMT as contested. Do not use it as a base axiom. The "mortality salience amplifies in-group affiliation" interaction remains unproven.

### B5. Rachman: acquisition paths

**Citation.** Rachman, S. (1977). The conditioning theory of fear acquisition: a critical examination. *Behaviour Research and Therapy* 15(5), 375-387 *(confirmed via Crossref)*. Secondary: LoBue & Rakison (2013) https://www.cmu.edu/dietrich/psychology/infant-cognition-lab/publications/LoBue%20&%20Rakison%20(2013).pdf; Muris & Field (2010) https://link.springer.com/doi/10.1007/s10567-010-0064-1.

**Verified.** Secondary only.

- **Claim.** Three pathways: direct conditioning, observation of others, and verbal information/instruction. Modern theories still adopt the three; Olsson & Phelps (2004), "Learned fear of 'unseen' faces after Pavlovian, observational, and instructed fear", *Psychological Science* 15(12), 822-828 (record confirmed in validation; finding from secondary source) found comparable skin-conductance fear learning across all three, with observational and Pavlovian (not instructed) learning surviving masked presentation.
- **Social transmission.** This is the answer to "does fear spread?": yes, two of three paths are social, and one can pass through a spoken sentence. Strongest social-spread finding in the cluster.
- **Operator.** "Warn(a, b, X)" and "show-fear-at(a, b, X)" are operators that install a fear in b. These are acts in the sense of the prior-work cluster 03 (interaction as operator).

### B6. Fear and judgement

Lerner, J. S. & Keltner, D. (2001). Fear, anger, and risk. *JPSP* 81(1), 146-159. https://greatergood.berkeley.edu/dacherkeltner/docs/lerner.fear.jpsp.2001.pdf. **Verified** by abstract summary.

- Fear leads to pessimistic risk estimates and risk-averse choice; anger to optimism and risk-seeking. Moderated and mediated by appraised certainty and control.
- **Replication.** A registered replication (Lu, Efendic & Feldman) is titled "Mixed evidence for the Appraisal-Tendency Framework" (https://rr.peercommunityin.org/articles/rec?id=772). I did not see effect sizes.
- **Interaction found.** Fear and anger have opposed effects on risk-taking. A fear-to-anger substitution would flip risk posture. This is a useful testable operator relation, with the above caveat.

### B7. Carleton: fear of the unknown

**Citations.** Carleton, R. N. (2016). Fear of the unknown: one fear to rule them all? *Journal of Anxiety Disorders* 41, 5-21, DOI 10.1016/j.janxdis.2016.03.011. Companion: Carleton (2016), Into the unknown, *J. Anxiety Disorders* 39, 30-43. https://instrepo-prod7.cc.uregina.ca/items/5d1d1960-6e1a-4cfd-8619-b9c46ef59ff9.

**Verified.** Abstract only.

- **Claim.** Tests the proposition that fear of the unknown "may be a, or possibly the, fundamental fear" underlying anxiety and neuroticism, using revised criteria for what counts as fundamental. The abstract does not state a verdict. A 2021 cross-sectional test (n = 373, *J. Exp. Psychopathology*, secondary report) found fear of the unknown the strongest unique predictor of anxiety among fear of death, pain and the unknown. Intolerance of uncertainty is the trait measure of this construct.
- **Link to A.** If uncertainty is itself aversive, then Berlyne's and Loewenstein's "gap" is the trigger for both curiosity and fear. That is a hypothesis for the algebra, not a finding.

---

## C. Desire and wanting

### C1. Berridge: incentive salience

**Citation.** Berridge, K. C. & Robinson, T. E. (2016). Liking, wanting, and the incentive-sensitization theory of addiction. *American Psychologist* 71(8), 670-679, DOI 10.1037/amp0000059. PMC5171207 (https://pmc.ncbi.nlm.nih.gov/articles/PMC5171207/).

**Verified.** Abstract and summary text, from search; full text is open access but I did not read it.

- **Claim.** "Wanting" (cue-triggered incentive salience; large, robust, dopamine-dependent mesolimbic systems) is dissociable from "liking" (pleasure; small, fragile, not dopamine-dependent). Addiction is mostly amplified, cue-triggered wanting through long-lasting neural sensitisation in susceptible individuals, with liking not necessarily raised.
- **Trigger.** Learned cues, modulated by physiological state. Standard account: wanting is a product of learned cue value and a state gain (Zhang, Berridge et al. 2009, *PLoS Computational Biology* 5(7): e1000437, record confirmed in validation); equation not retrieved. [from abstract/standard account]
- **Dynamics.** Sensitisation: repeated exposure raises wanting, can leave liking flat. Wanting is non-saturating in a way hunger is not. That is the exact feature of a drive that grows with satisfaction, important for an algebra since many drive models assume satiation.
- **Social transmission.** Not in the abstract. Cues can be other people.

### C2. Elaborated intrusion theory

**Citation.** Kavanagh, D. J., Andrade, J. & May, J. (2005). Imaginary relish and exquisite torture: the elaborated intrusion theory of desire. *Psychological Review* 112(2), 446-467, DOI 10.1037/0033-295X.112.2.446. https://eprints.whiterose.ac.uk/id/eprint/509/.

**Verified.** Abstract-level.

- **Mechanism.** Cue, state or thought triggers an intrusive thought of the target; if pleasant or relieving, it is elaborated; elaboration uses working memory and so competes with other cognitive tasks; imagery is the main product and raises awareness of deficits. Craving is the far end of a continuum of everyday desire.
- **Dynamics and control.** Onset is automatic (intrusion), escalation is voluntary-ish (elaboration), and a working-memory load task can suppress it. That makes it the only desire theory with an explicit lever: an act that occupies working memory reduces desire.
- **Empirical standing.** A later review is reported as saying much research supports the premises. Not checked.

### C3. Girard: mimetic desire

**Sources.** Girard's own books (*Deceit, Desire and the Novel*, 1961, and later) were not retrieved; the description comes from Wikipedia's mimetic-theory page (https://en.wikipedia.org/wiki/Mimetic_theory) and secondary pieces. Treat the theory itself as [from abstract/standard account].

- **Structure.** Triangular: subject, model, object. Desire is copied from the model. The subject and model become rivals for the same object, and escalation can end in scapegoating. (Wording follows the Wikipedia article 'Mimetic theory', CC BY-SA 4.0.)
- **Social transmission.** Inherent. The drive is defined by other people. This is the one drive in the cluster that cannot be written for a single agent.
- **Empirical standing.** Girard's claims are literary and anthropological. I found no experimental test. Livingston, P. (1992), *Models of Desire: René Girard and the Psychology of Mimesis*, Johns Hopkins University Press (year corrected from 2020, which was the PhilArchive record date) is a rigorous reconstruction of Girard against cognitive psychology; not read.
- **Formal models.** *Identified in validation (PDF text extracted):* Antunes, L., Nunes, D. & Coelho, H. (2014). "The Geometry of Desire." *Proc. AAMAS 2014* (Paris), pp. 1169-1172 (https://ifmas.csc.liv.ac.uk/Proceedings/aamas2014/aamas/p1169.pdf). It proposes a BDI-style model of desire acquisition in which agents adopt goals by envy, imitation and competition after Girard (subject/mediator/object, double mediation). It is a **short position/design paper: no equations and no simulation results**. Also found: an unreviewed NetLogo agent-based model of Girardian scapegoating on the CoMSES library (tension spreads on a small-world network; past a threshold, leaders accuse marginal agents; collective tension falls). Neither is a tested mathematical model of mimetic desire.
- **Operand/operator.** Operands: subject, model, object (a three-sort structure). Operators: imitate(a, b) copying b's desire onto a; compete. The triangle is a natural ternary relation; the role algebras in cluster 01 handle only binary ties, so this is where the earlier tradition would strain.

---

## D. Other candidate primaries and their known interactions

### D1. Panksepp's seven systems

Panksepp's affective neuroscience lists seven primary emotional command systems: SEEKING, FEAR, RAGE, LUST, CARE, PANIC/GRIEF, PLAY (framing sentence follows the Wikipedia article 'Jaak Panksepp', CC BY-SA 4.0; the seven names are factual; https://wiki.p2pfoundation.net/Panksepp's_Seven_Basic_Emotions; Wikipedia Jaak Panksepp page; PLoS ONE 2011 summary, https://doaj.org/article/741e0a4592d74458ad61efefd3c74e53). **Verified** at summary level only; I did not find the primary book (Panksepp 1998, *Affective Neuroscience*, OUP, recalled).

- Mapped mainly by brain stimulation, pharmacology and lesions in mammals. He judged evidence insufficient to include social dominance as a primary system.
- **Critique.** Barrett calls the hard-wired-from-birth claim a hypothesis.
- **Reading.** This is the nearest existing candidate for a *basis set* of drives, and its list aligns with Aldred's examples: SEEKING (curiosity and wanting), FEAR, plus CARE, PLAY, RAGE, PANIC/GRIEF (belonging). It also puts curiosity and wanting in one system. That conflicts with the split in this document and should be noted when choosing a basis.

### D2. Status

Anderson, C., Hildreth, J. A. D. & Howland, L. (2015). Is the desire for status a fundamental human motive? A review of the empirical literature. *Psychological Bulletin* 141(3), 574-601, DOI 10.1037/a0038781. https://eclass.uoa.gr/modules/document/file.php/PPP387/Desire%20for%20Status%2C%20Human%20Motive%2C%20APA.pdf. **Verified** by abstract and press summaries.

- Status = respect, admiration and voluntary deference from others. They review hundreds of studies against criteria and conclude the evidence supports the status hypothesis; one criterion is that attaining status improves health and wellbeing.
- **Social by definition.** Status exists only in others' regard, so it is a relation, not a quantity inside a person.
- Panksepp excluded dominance; Anderson et al. include status. The two disagree on whether this is primary.

### D3. Belonging and its threat

- Baumeister, R. F. & Leary, M. R. (1995). The need to belong. *Psychological Bulletin* 117(3), 497-529, DOI 10.1037/0033-2909.117.3.497. https://pubmed.ncbi.nlm.nih.gov/7777651/. **Verified** (abstract). People form attachments readily and resist dissolution; deficits link to poorer health. A 2016 paper argues need for meaning is more basic (found via search; not retrieved).
- Williams' temporal need-threat model of ostracism: reflexive, reflective, resignation stages; Hartgerink, van Beest, Wicherts & Williams (2015, *PLoS ONE* 10(5): e0127002), a meta-analysis of 120 Cyberball studies (n = 11,869), found a large ostracism effect (d > 1.4) generalising across set-ups, but both first and last measures were moderated and time since ostracism did not predict the effect, so weak support for the model's claim that immediate effects resist moderation (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4449005/). **Verified** from the meta-analysis summary. This is a rare drive model with named stages and measured effects, which is what a dynamics section wants.
- **Interaction found.** Exclusion threatens belonging, control, self-esteem and meaningful existence together (the 2025 Cyberball study reported in search, https://link.springer.com/article/10.1007/s12144-025-08409-3).

### D4. Power

Keltner, D., Gruenfeld, D. H. & Anderson, C. (2003). Power, approach, and inhibition. *Psychological Review* 110(2), 265-284. https://www.kellogg.northwestern.edu/academics-research/research/detail/2003/power-approach-and-inhibition. **Verified** by abstract.

- Power brings rewards and freedom, activating approach; reduced power brings threat and constraint, activating inhibition. High power goes with positive affect, reward attention, automatic processing, disinhibition.
- **Standing.** Sabey, Shanklin, Colquitt & Baer (2025), *Psychological Bulletin* 151(10), 1245-1279, DOI 10.1037/bul0000500 (1,712 effect sizes, 813 samples, 269,534 participants). *Corrected in validation:* dissensus, mediational ambiguity and primacy were the **motivation**, not the finding. The meta-analysis concludes the theory is supported, with approach associations larger than inhibition associations and effects on behaviour running indirectly, mostly through affect (abstract summary only). Anderson & Galinsky (2006, *EJSP* 36(4), 511-536) measured power raising optimism and risk-taking.
- **Interaction.** Power moves a person along the approach/inhibition axis, which is also the axis curiosity and fear sit on. So power modulates curiosity-vs-fear by shifting the setpoint. That is an inference from the two literatures, not a finding.
- **Operator.** "Grant/remove power" changes the other's drive balance.

### D5. Anger and frustration-aggression

- Dollard, J., Doob, L., Miller, N., Mowrer, O. & Sears, R. (1939). *Frustration and Aggression*. Yale University Press. Not retrieved; description from study-aid sources, low quality.
- Berkowitz, L. (1989). Frustration-aggression hypothesis: examination and reformulation. *Psychological Bulletin* 106(1), 59-73. https://pubmed.ncbi.nlm.nih.gov/2667009/. **Verified** by abstract.
- **Claims.** Original: aggression is always a consequence of frustration, and frustration always leads to aggression (standard account, not verified in this session). Berkowitz: frustration produces aggressive inclination to the extent it produces negative affect, with aggressive cues (the weapons effect, Berkowitz & LePage 1967: more shocks with guns present, 6.07 vs 4.67 in a study-aid summary) raising the chance of acting. Displacement: aggression shifts to an available, weaker target. Marcus-Newhall, Pedersen, Carlson & Miller (2000), "Displaced aggression is alive and well: a meta-analytic review", *JPSP* 78(4), 670-689: the title states the conclusion, that displaced aggression is a reliable effect (49 studies per secondary sources; effect size not checked). A critique says the reformulation became irrefutable.
- **Social transmission.** Displacement is the social act: frustration in a with source x lands on b. That is a clean operator: displace(a, x to b).
- **Standing.** Mixed; study-aid sources also report catharsis failing (punching bags increased aggression) and I did not verify those.

### D6. Disgust and the behavioural immune system

Schaller, M. & Park, J. H. (2011). The behavioral immune system (and why it matters). *Current Directions in Psychological Science* 20(2), 99-103, DOI 10.1177/0963721411402596. https://www2.psych.ubc.ca/~schaller/SchallerPark2011.pdf. **Verified** by summary.

- **Trigger.** Cues of pathogen presence, over-broad (false positives, e.g. unfamiliar people), more intense when the person feels vulnerable to infection. The summary notes a link between felt vulnerability and lower extraversion.
- **Interaction.** Disease salience and felt vulnerability predict xenophobic attitudes toward unfamiliar outgroups: Faulkner, Schaller, Park & Duncan (2004), "Evolved disease-avoidance mechanisms and contemporary xenophobic attitudes", *Group Processes & Intergroup Relations* 7(4), 333-353 (added in validation; record only). That makes disgust suppressing affiliation to outsiders a measured cell. Disgust suppressing curiosity toward outsiders remains inference.
- **Group level.** Gelfand et al. 2011, *Science* 332, 1100-1104 (https://findanexpert.unimelb.edu.au/scholarlywork/343363-differences-between-tight-and-loose-cultures--a-33-nation-study) places disease and other ecological threats among the distal causes of "tight" cultures with strong norms and little tolerance for deviance (33 nations). Verified only that framing, from record pages. This is the clearest published bridge from a threat drive to a group-level property.

### D7. Play and care

The original survey did not search either. Added in validation (records confirmed, contents from standard account, not read):

- **Play.** Panksepp & Burgdorf (2003), "'Laughing' rats and the evolutionary antecedents of human joy?", *Physiology & Behavior* 79(3), 533-547: juvenile rats emit 50-kHz calls to rough-and-tumble play and to tickling, and seek the tickling hand; Panksepp treats PLAY as a primary system that is suppressed by fear and hunger (play needs safety). That is a theory-level Fear -S-> Play cell. Panksepp 1998 *Affective Neuroscience* (OUP) remains the primary text, unread.
- **Care / attachment.** Bowlby, J. (1969), *Attachment and Loss, Vol. 1: Attachment* (Hogarth/Basic Books): the attachment system is activated by fear, illness or separation and drives proximity-seeking to a caregiver; Ainsworth's Strange Situation is the standard measurement. Taylor, Klein, Lewis, Gruenewald, Gurung & Updegraff (2000), "Biobehavioral responses to stress in females: tend-and-befriend, not fight-or-flight", *Psychological Review* 107(3), 411-429, DOI 10.1037/0033-295X.107.3.411: under stress, especially in females, tending offspring and affiliating with others, proposed to be oxytocin- and opioid-mediated. Schachter, S. (1959), *The Psychology of Affiliation* (Stanford UP): subjects threatened with painful shocks preferred to wait with others, especially others in the same situation. Together these make Fear -A-> Belonging/Care one of the better-supported cells, independent of the contested TMT route.
- No dedicated search was run beyond these; "Bell" in the brief did not resolve to a specific tend-and-befriend author and is not cited.

---

## E. Social transmission across the cluster

- **Emotion contagion.** Kramer, A. D. I., Guillory, J. E. & Hancock, J. T. (2014). Experimental evidence of massive-scale emotional contagion through social networks. *PNAS* 111(24), 8788-8790. https://pmc.ncbi.nlm.nih.gov/articles/PMC4066473/. **Verified** by abstract and summaries: 689,003 Facebook users; reducing positive posts in a feed lowered positive posting and raised negative, and the reverse; no direct interaction or nonverbal cues needed. Effect sizes are very small by the standard account (I did not verify the size), and the study drew an editorial expression of concern about consent.
- **Fear:** Rachman's observational and instructional paths (B5).
- **Desire:** Girard's imitation (C3).
- **Anger:** displacement (D5).
- **Curiosity:** opening an information gap in another person (A2). No transmission study found.
- **Status, power:** relational by definition.

---

## F. Interaction matrix

*Revised in validation (2026-10-29).* Rows act on columns. A = amplifies, S = suppresses, ? = unknown/no evidence found. Evidence strength in brackets: [M] direct measurement, [T] theory only, [I] inference from two literatures. "Unknown" now replaces every cell whose cited source does not show that interaction.

| acts on -> | Curiosity | Fear | Wanting | Status | Belonging/Care | Power | Anger | Disgust |
|---|---|---|---|---|---|---|---|---|
| **Curiosity** | - | curiosity overrides fear: people accept or seek electric shocks to resolve uncertainty (Hsee & Ruan 2016; Lau et al. 2020) [M]; shared trigger via uncertainty (Carleton 2016) [T] | ? (Gruber 2014 shows curiosity -> incidental memory, not wanting) | ? | ? | ? | ? | ? |
| **Fear** | S at high arousal (Berlyne) [T] | - | ? | ? | A affiliation under threat (Schachter 1959) [M, classic]; tend-and-befriend (Taylor et al. 2000) [T + review]; attachment activation (Bowlby 1969) [T]; via mortality salience (TMT) [contested] | ? | ? | ? |
| **Wanting** | same system as curiosity (SEEKING, Panksepp) [T] | hunger, like curiosity, buys shock risk (Lau et al. 2020) [M]; approach-avoidance conflict (Miller/Gray) [T] | - | ? | ? | ? | blocked wanting -> aggressive inclination via negative affect (Berkowitz 1989) [T + experiments] | ? |
| **Status** | ? | ? | ? | - | ? (unmapped) | ? | ? | ? |
| **Belonging** | ? | ? | ? | ? | - | ? | ? | ? |
| **Power** | ? | S: power shifts toward approach, optimism and risk-taking (Keltner 2003 [T]; Anderson & Galinsky 2006 [M]; Sabey et al. 2025 meta-analysis, approach > inhibition [M]) | A approach (Keltner 2003; Sabey et al. 2025) [T, M meta] | ? | ? | - | ? | ? |
| **Anger** | ? | ? | ? | ? | ? | ? | - | ? |
| **Disgust** | S toward outsiders [I] | ? | ? | ? | S affiliation to unfamiliar outgroups (Faulkner et al. 2004; Schaller & Park 2011) [M, attitudes] | ? | ? | - |

Not a cell, but a measured relation: **fear and anger have opposite effects on risk judgement** (Lerner & Keltner 2001; Lu, Efendić & Feldman's registered replication reports mixed evidence). That is two drives acting oppositely on a third quantity, not one acting on the other, so the draft's Fear->Anger and Anger->Fear entries are moved here. Also outside the table: **Fear suppresses Play** (Panksepp) [T].

**Downgraded in validation.** Fear->Power "S inhibition (Keltner 2003)" (Keltner shows power -> inhibition, not fear -> power); Status->Fear "S ?" (no source); Fear->Curiosity "[M infant]" via Kidd 2012 (that study varies information content, not threat); Fear<->Anger (see above); Curiosity->Wanting/incidental learning moved out of the Wanting column.

**Cells with real support.** Curiosity overrides fear of pain (Hsee & Ruan 2016; Lau et al. 2020); hunger does the same (Lau et al. 2020); fear raises affiliation (Schachter 1959, with tend-and-befriend and attachment as theory); power raises approach and risk-taking (Anderson & Galinsky 2006; Sabey et al. 2025); disease cues lower acceptance of outsiders (Faulkner et al. 2004). Also measured but not drive-on-drive: curiosity boosts incidental memory (Gruber 2014); curiosity peaks at moderate confidence (Kang 2009) and infant attention at intermediate complexity (Kidd 2012). Everything else is empty or theoretical.

Not found: any study measuring status against belonging directly (the "status vs belonging" example in the brief).

---|---|---|---|---|---|---|---|---|
| **Curiosity** | - | ? (shares trigger: Carleton, Berlyne) [T] | A learning of incidental material (Gruber) [M]; wanting: ? | ? | ? | ? | ? | ? |
| **Fear** | S at high arousal; peak curiosity is mid-range (Berlyne, Kidd 2012) [T,M infant] | - | ? | ? | A belonging need via threat (TMT) [contested] | S inhibition (Keltner 2003) [T] | opposite risk posture to anger (Lerner & Keltner) [M, mixed replication] | ? |
| **Wanting** | A (SEEKING in Panksepp) [T] | ? approach-avoidance conflict (Gray/Miller) [T] | - | ? | ? | ? | A via frustration when blocked (Berkowitz) [T] | ? |
| **Status** | ? | S ? | ? | - | ? tension: unmapped | ? | ? | ? |
| **Belonging** | ? | ? | ? | ? | - | ? | ? | ? |
| **Power** | ? | S (approach vs threat attention) [T] | A approach (Keltner) [T] | ? | ? | - | ? | ? |
| **Anger** | ? | opposite risk posture [M] | ? | ? | ? | ? | - | ? |
| **Disgust** | S toward outsiders, inferred [I] | ? | ? | ? | S affiliation to outsiders (BIS) [I] | ? | ? | - |

**Cells with real support are few.** Specifically supported: curiosity peaks at intermediate arousal and falls at high arousal (Berlyne; Kidd 2012); curiosity boosts incidental memory (Gruber 2014); fear and anger have opposed effects on risk estimates (Lerner & Keltner, replication mixed); blocked wanting produces anger-type responses (Berkowitz, mechanism via negative affect); power shifts approach versus inhibition (Keltner 2003, under dissensus). Everything else is empty or unmeasured.

Not found: any study measuring status against belonging directly (the "status vs belonging" example in the brief); any measurement of desire against fear in a single paradigm beyond approach-avoidance conflict (cited via a 2016 Bach summary seen in search, not the primary papers).

---

## G. What exists vs what does not

**Exists.**
- Executable single-agent curiosity equations (Schmidhuber, Oudeyer & Kaplan, Pathak). Curiosity as prediction-error or learning-progress reward has code.
- An inverted-U across stimulus complexity, replicated at least in infants and in aesthetic ratings, with partial caveats.
- A mode-by-imminence structure for fear (Fanselow; Mobbs), the closest thing in the cluster to a state machine, but verbal/ordinal: no equations confirmed.
- A defensible candidate basis set (Panksepp's seven), contested on the "hard-wired" claim and on omitting dominance.
- Named transmission paths for fear (Rachman) and measurable emotion contagion (Kramer 2014).
- Verbal but testable models with specific levers: elaborated intrusion (working-memory load suppresses desire), need-threat staging for ostracism.

**Does not exist (in what I found).**
- A formal model in which one person's act changes another person's drive. All drive mathematics found is single-agent (emotion-contagion modelling was not searched, so this is a limit of the search, not a proven absence).
- Drive-by-drive interaction data. The matrix is mostly question marks; no one has measured the pairs systematically. The few measured cells (curiosity vs shock, fear -> affiliation, power -> risk) come from separate paradigms with no common scale.
- A common unit or scale across drives. Curiosity is bits of compression gain, fear is imminence, wanting is dopamine-tied salience, status is deference. None is comparable.
- Settled satiation and decay laws. Wanting may sensitise rather than saturate (Berridge); no cross-drive decay constants.
- A tested mathematical model of mimetic desire. The AAMAS 2014 hit (Antunes, Nunes & Coelho) is a position paper with no equations or results; one unreviewed NetLogo scapegoating model exists.
- A robust reading of terror management: contested after Many Labs 4.
- Group-level drive dynamics beyond tight/loose culture and contagion studies.

**Implication for social-algebra.** The fix for "does it spread" is the relevant piece. The strongest base for a first drive algebra is probably this: operands = persons with a small vector of drive levels; operators = acts (warn, reveal, withhold, grant status, exclude, include, imitate); drive-level laws taken from the few measured cells. But that is a design choice, which depends on the home choice the brief leaves open. It is also a risk: most cells are empty, so any law will be a hypothesis for the algebra to test, not a result inherited from psychology.

---

## Unconfirmed

- Berlyne 1960 primary text; the two-sigmoid derivation is the standard account only. (Berlyne 1970 record now confirmed.)
- Fanselow & Lester 1988 chapter details (pp. 185-212 recalled); whether Mobbs et al. 2020 contains any formal model (abstract has none).
- Dollard et al. 1939 primary text; Marcus-Newhall et al. 2000 effect size (record and conclusion now confirmed); Berkowitz & LePage 1967 shock means (6.07 vs 4.67, study-aid source only).
- Greenberg, Pyszczynski & Solomon original TMT papers (Burke et al. 2010 record now confirmed).
- Zhang, Berridge, Tindell, Smith & Aldridge (2009), *PLoS Comput Biol* 5(7): e1000437 — record confirmed, the multiplicative kappa form not checked; Panksepp 1998 book; Livingston 1992 contents; Gray & McNaughton 2000 *Neuropsychology of Anxiety*.
- Lerner & Keltner replication (Lu, Efendić & Feldman, N = 780): effect sizes and which experiments replicated (PCI RR page blocked).
- The 2025 Cyberball study (s12144-025-08409-3) and the 2016 "need for meaning" paper in D3: not checked.
- Lau et al. 2020 and Hsee & Ruan 2016 findings: records confirmed, findings from abstract/press summaries.
- Play and care: only the anchor works added in validation; no wider search. Gelfand 2011 only partly verified.
- Hatfield, Cacioppo & Rapson on emotional contagion; Carver & White BIS/BAS; Christakis & Fowler network spread of affect: not searched.

## Clearly missing important work (added in validation, not verified in this pass)

- **Formal drive theory itself.** Hull, C. L. (1943), *Principles of Behavior*: reaction potential as a product of drive and habit strength (sEr = D x sHr), the classic multiplicative drive equation; and Keramati, M. & Gutkin, B. (2014), "Homeostatic reinforcement learning for integrating reward collection and physiological stability", *eLife* 3:e04811, which defines reward as drive reduction in a multi-dimensional internal-state space. Both are directly on the strand's aim (drives as composable quantities) and the survey's claim that drive mathematics is scarce has to be read against them.
- **Basic-needs theories.** Deci & Ryan's self-determination theory (autonomy, competence, relatedness); Maslow; Murray's needs. Competing basis sets to Panksepp's seven.
- **Approach/avoidance as an axis.** Gray & McNaughton (2000); Carver & White (1994) BIS/BAS scales; Elliot's approach-avoidance work. Needed for the Power and Fear-Wanting cells.
- **Social spread.** Hatfield, Cacioppo & Rapson (1993/1994), *Emotional Contagion*; Fowler & Christakis (2008, *BMJ*) on happiness spreading in networks; Olsson & Phelps (2007, *Nature Neuroscience*) "Social learning of fear"; Barsade (2002) on group emotional contagion. Section E rests on Kramer 2014 alone without them.
- **Curiosity and anxiety at trait level.** Kashdan and colleagues' multidimensional curiosity work (including a stress-tolerance dimension) and intolerance-of-uncertainty measures (Carleton), the obvious measured link for the Curiosity<->Fear cells.
- **Play and care** beyond the anchors added in D7: Pellis & Pellis on rough-and-tumble play; Feldman / Insel on oxytocin and bonding; Ainsworth's attachment classification.

## Validation log (2026-10-29)

- Berlyne 1960 — ? book not seen; standard account only.
- Berlyne 1970 — ✎ was "not found"; confirmed P&P 8(5) 279-286, DOI 10.3758/BF03212593.
- Marin et al. 2016 (unnamed "2016 study") — ✎ inverted U for beauty only in music; paintings linear; pleasantness claim narrowed.
- Loewenstein 1994 — ✎ citation ✓; inverted U in prior knowledge is not Loewenstein's claim, reattributed to Kang et al. 2009 (added).
- Kidd & Hayden 2015 — ✓.
- Gottlieb et al. 2013 — ✓.
- Gruber, Gelman & Ranganath 2014 — ✎ vol/pages confirmed (Crossref); matrix placement corrected.
- Kidd, Piantadosi & Aslin 2012 — ✓ (n = 72 press figure only); ✎ removed as evidence for a fear cell.
- Schmidhuber 2010 — ✓ (compression-progress reward as compressor improvement matches the standard account; PDF not opened).
- Oudeyer & Kaplan 2007 — ✓.
- Pathak et al. 2017 — ✓ formula r = (eta/2)||phi_hat(s') - phi(s')||^2 in inverse-dynamics feature space matches the paper's standard form.
- LeDoux & Pine 2016 — ✎ vol/pages confirmed via Crossref.
- Fanselow & Lester 1988 — ? chapter not seen.
- Mobbs, Headley, Ding & Dayan 2020 — ✎ abstract checked; model-free/model-based by distance; "population codes" removed; no formal model confirmed.
- Mobbs et al. 2015 — ✎ added (SOS stages).
- Öhman & Mineka 2001 — ✓ record; Davey 1995 ✎ venue added.
- Klein et al. 2022 Many Labs 4 — ✎ title, DOI, target study and conclusion made exact; Haaf et al. 2023 reanalysis named.
- Treger et al. 2023 — ✎ identified (was "a 2023 PLOS ONE set").
- Burke et al. 2010 — ✓ record confirmed.
- Arendsen et al. 2025 — ✎ identified; g = 0.21 confirmed in PDF.
- Rachman 1977 — ✎ pages confirmed via Crossref.
- Olsson & Phelps 2004 — ✓ record confirmed.
- Lerner & Keltner 2001 — ✓; ✎ removed from the matrix as a drive-on-drive cell.
- Lu, Efendić & Feldman (replication) — ? exists (N = 780); results page blocked.
- Carleton 2016 (both) — ✎ abstract's actual claim quoted; draft said abstract gave nothing.
- Berridge & Robinson 2016 — ✓.
- Zhang et al. 2009 — ✎ record confirmed; equation still ?.
- Kavanagh, Andrade & May 2005 — ✓ (record matches; not re-fetched).
- Girard / Wikipedia — ? secondary only, as stated.
- Livingston *Models of Desire* — ✎ year 2020 -> 1992, JHU Press.
- "AAMAS 2014 Girard paper" — ✎ identified: Antunes, Nunes & Coelho, "The Geometry of Desire", pp. 1169-1172; position paper, no equations or results.
- CoMSES scapegoating ABM — ✎ added (unreviewed).
- Panksepp seven systems / 1998 — ? summary level only.
- Anderson, Hildreth & Howland 2015 — ✓.
- Baumeister & Leary 1995 — ✓.
- Hartgerink et al. 2015 — ✎ authors and the actual moderation result added.
- 2025 Cyberball study, 2016 meaning paper — ? not checked.
- Keltner, Gruenfeld & Anderson 2003 — ✓.
- Sabey et al. 2025 meta-analysis — ✎ finding inverted: theory supported; "dissensus" was the motivation.
- Anderson & Galinsky 2006 — ✎ added.
- Dollard et al. 1939 — ? primary not seen.
- Berkowitz 1989 — ✓.
- Berkowitz & LePage 1967 — ? shock means from a study-aid source.
- Marcus-Newhall et al. 2000 — ✎ "sources disagree" resolved: the meta-analysis concludes displaced aggression is reliable.
- Schaller & Park 2011 — ✓.
- Faulkner et al. 2004 — ✎ added; supports Disgust -> outgroup affiliation cell.
- Gelfand et al. 2011 — ? framing only.
- Kramer, Guillory & Hancock 2014 — ✓.
- Hsee & Ruan 2016; Lau et al. 2020 — ✎ added; support the Curiosity -> Fear cell.
- Kang et al. 2009 — ✎ added.
- Panksepp & Burgdorf 2003; Bowlby 1969; Taylor et al. 2000; Schachter 1959 — ✎ added (play and care).
- Interaction matrix — ✎ five cells downgraded to unknown or moved out (Fear->Power, Status->Fear, Fear->Curiosity [M], Fear<->Anger, Curiosity->Wanting); five supported cells added (Curiosity->Fear, Wanting->Fear, Fear->Belonging [M], Power->Fear [M], Disgust->Belonging [M]).
- Closing verdict — ✎ "three bodies with real mathematics" cut to one; "all drive mathematics is single-agent" qualified as a search limit; Hull and homeostatic RL flagged as missed.
- No fabrications found: every cited work exists.

**Verdict.** Bibliographically the survey is sound — every work exists and the recalled volume/page details were right — and it was honest about what it had not read. Its weaknesses were interpretive: it overstated the formality of the fear literature, misread the 2025 power meta-analysis's conclusion, mis-attributed the curiosity inverted U, and filled several matrix cells with sources that do not show the interaction claimed. Use the revised matrix, not the draft's, and treat every [T] cell as a hypothesis.

## Licences of quoted and transcribed material (2026-10-30)

No verbatim quotation over a short phrase, no transcribed table and no dataset is in this file; the audit's flagged items are handled as below.

- Wikipedia, 'Mimetic theory' (B/C3 Girard structure bullet): CC BY-SA 4.0; description of a theory in wording that follows the article, now marked in the text.
- Wikipedia, 'Preparedness' (B3 Ohman & Mineka claim bullet): CC BY-SA 4.0; summary-level description, now marked in the text.
- Wikipedia, 'Jaak Panksepp' (D1 framing sentence): CC BY-SA 4.0; the list of seven system names is factual, the framing is marked in the text.
- P2P Foundation wiki, Panksepp's seven basic emotions (D1): not determined; used as a citation for the factual list only.
- Panksepp (1998), *Affective Neuroscience*, OUP: publisher copyright presumed; cited, not read, nothing reproduced.
- Anderson, Hildreth & Howland (2015), Psychological Bulletin (D2): publisher copyright (APA); abstract-level paraphrase in our own words. Flagged "check": wording to be confirmed as the file's own before the repo is opened.
- Keltner, Gruenfeld & Anderson (2003), Psychological Review (D4): publisher copyright (APA); abstract-level paraphrase, same "check" flag.
- Antunes, Nunes & Coelho (2014), AAMAS: not determined; publisher copyright presumed; described, not quoted.
- All other sources (Berlyne, Gruber et al., Kidd et al., Gottlieb et al., Oudeyer & Kaplan, LeDoux & Pine, Mobbs et al., Klein et al., Haaf et al., Baumeister & Leary, and the rest): not determined; publisher copyright presumed (open-access licences, e.g. PMC or PLoS ONE items, not individually checked). Used as citations with descriptions of findings and figures; no restated equations.
