# Prior work 19: computational agents driven by explicit drives, needs and emotions

Date: 2026-10-29. Survey for the social-algebra strand. New aim (Aldred): an algebra of basic human and group drives (curiosity, fear, desire) that composes into equations, supports theorems, and is used to predict or control behaviour. Cluster: the places where drive dynamics were made executable.

**Method note.** Tags: **[read]** = I extracted the text of the source in this session (full PDF, or a project web page); **[abstract]** = abstract, search snippet or project page only; **[standard]** = the standard account as I know it, not checked against the text. Several PDFs were pulled with `pdftotext`. One fetch returned the wrong paper (see Unconfirmed). Almost nothing in this cluster states its update rules as published equations; where a model's rules are only qualitative, I say so rather than invent an equation.

**Headline.** Drive dynamics have been made executable many times, and the shared skeleton is simple (a level that decays, deficit-driven urgency, a winner-take-all or weighted choice). Composition rules **are** stated in a few places, but only as design equations, never as studied laws: Avila-García and Cañamero's motivation intensity m_i = d_i + d_i·α·c_i (deficit times cue), PSI's expectancy-times-value selection with "intention amalgamation" (one plan serving several motives), and Yoshida and Man's linear coupling of one agent's drive to another's (D = D_self + w·D_partner, section 14). **No theorem about drive composition was found.** The one proved result in the cluster is Keramati and Gutkin's equivalence for a single agent (section 12); ethology's optimal-control theory of motivation (Sibly and McFarland) is the likely place for more, and was not checked (see "Missing work"). Multi-agent drive coupling is rare, recent and empirical. *(Headline revised by the validation pass, 2026-10-29: the original said "no stated laws" for composition and implied no agent-to-agent coupling existed.)*

---

## 1. Dörner's PSI theory and Bach's MicroPsi

**Citations.** Dörner, D. (1999) *Bauplan für eine Seele*; Dörner et al. (2002) *Die Mechanik des Seelenwagens*; Bach, J. (2009) *Principles of Synthetic Intelligence: PSI, an Architecture of Motivated Cognition*, Oxford UP.

**Verified.** Wikipedia's Psi-theory article **[read]**, Bach's book listing and OUP chapter page **[abstract]**, MIT MicroPsi slide deck (URL found, fetch failed on certificate) **[abstract via search snippet only]**. Detje's Bamberg report **[read]** (section 11). The book itself was not read.

- **Drive set [read, Wikipedia].** "A finite set of primary, pre-defined drives (urges)" in three groups. Physiological: food, water, physical integrity. Social: affiliation. Cognitive: uncertainty reduction ("certainty") and competence (task-specific and general). Bach's book description gives the same three groups.
- **State variables and update rules.** Each demand is a level with a target value. An **urge signal arises when the level departs from target and is "proportional to the deviation"** [read, Wikipedia]. Detje describes affiliation as structurally the same as the water level: a level that "slowly sinks over time", rises on each incoming legitimacy (L) signal and falls on each anti-legitimacy (AL) signal [read, Detje]. No numeric decay rates are given in what I read. (Wikipedia's remark that PSI's quantitative claims are "rarely supported by experimental evidence" is about memory-association decay and the width and depth of activation spreading, not about need decay rates. Corrected in validation.)
- **Selection rule [read, Wikipedia; read, Detje].** A *motive* = a drive plus a goal situation. Several are active; one dominates. The choice depends on **urge strength and the anticipated probability of satisfying it**. Detje states it as "a dynamised form of the expectancy-times-value principle" combining importance, urgency and probability of success (competence); intention strength = F(importance, competence, time window, current circumstances). The function F is not given as an equation. The active intention suppresses the others by **lateral inhibition** (inertia), and SelectInt also does **intention amalgamation**: one plan can serve several compatible motives at once (Detje's example: a restaurant visit with friends serves hunger, thirst and affiliation). A **selection threshold** gives the current motive inertia against competitors, and depends on urgency and individual variance.
- **Modulators [read, Wikipedia].** Global parameters: general activation or arousal (action readiness), selection threshold, sampling rate or securing threshold (rate of orientation behaviour), activation and resolution level (width and depth of activation spreading). Emotion is not a separate module: it is "a configurational setting of the modulators", plus the pleasure/distress dimension and the urge assessment.
- **Social coupling.** Affiliation is satisfied by external legitimacy signals (acceptance from other agents) and internal ones (meeting norms); it rises on anti-legitimacy signals and on supplicative signals (requests for help) [read, Wikipedia]. Detje's design [read]: a supplicative signal is an announcement of a potential L-signal ("if you help me, I will be grateful"); helping is a tool for earning L-signals; a lonely agent comes to treat a rich source of L-signals as a place to visit when its L-tank drops, "falling in love", and is frustrated if the source turns to a third agent. Norms are expected to emerge. **But Detje's 2000s experiments were single-agent**: PSI lived alone on its island, and the affiliation need was satisfied by a "Teddy" object and a "kiss" (Küssen) operator, declared in the operator file as a signed delta on the need (`Affili -1`, full satisfaction); the multi-agent implementation was "not yet finished" [read]. Note that PSI operators are thus literally declared state-delta entries, like Sims advertisements. Volkmer and Alsabah later built a PSI multi-agent simulation (section 14).
- **Validation.** Wikipedia says the emotion model has been fitted to human subjects in behavioural experiments and shows personality-type-like performance, and that a parameter set can be fitted to an environment by evolutionary simulation (Dörner and Gerdes 2005, "The Mice' War and Peace", citation seen in a bibliography, paper not found) [abstract]. Detje reports that PSI's behaviour had been compared with human behaviour and with other cognitive architectures in earlier studies (Bartl and Dörner 1998, Detje 2000, Hille 1997, Schaub) [read, as claim; those studies not read].
- **Operand/operator translation.** Operands: demand levels (per agent), motives, goals. Operators: the *operator* in PSI's own sense is a learned action that changes the world and thereby a level; L-signals are directed acts from one agent to another that change the receiver's affiliation level. That is the closest thing here to a binary social operator, and it exists only as a design in the sources I read.

## 2. Cañamero: motivated autonomous agents (Agents '97)

**Citation.** Cañamero, D. (1997). Modeling motivations and emotions as a basis for intelligent behavior. In W. L. Johnson (ed.), *Proc. First Int. Conf. on Autonomous Agents (Agents '97)*, ACM Press, 148-155. DOI 10.1145/267658.267688 (resolved on Crossref in validation). A companion paper, "A hormonal model of emotions for behavior control" (VUB AI-Memo / ECAL 1997), covers the same creatures.

**Verified.** The 1997 paper itself not read. Secondary **[read]**: de Almeida, da Silva and Bazzan (AAAI SS-04-02) describe it. Later Cañamero-group equation **[read]**: Avila-García and Cañamero (2005), "Hormonal modulation of perception in motivation-based action selection architectures", AISB'05 symposium *Agents that Want and Like*, 9-16.

- **Drive set [read, secondary].** The "Abbots" (not "Abbotts") live in "Gridland", a 2-D grid with resources (de Almeida et al. name oxygen and food sources with glucose). Their internal milieu has two kinds of bodily state: **controlled variables**, held by homeostatic processes within a range of stability, and **hormones**, released in emotional reactions, each hormone affecting several variables with its own valence per variable. So the hormone layer is already in the 1997 model, not only in the later papers. Whether the scenario contained "enemies" is not confirmed.
- **Update rules [read, Avila-García and Cañamero 2005, taking the form from Avila-García et al. 2003].** Deficit d_i ∈ [0,1] in an essential variable, incentive cue c_i ∈ [0,1], weight α ∈ [0,1]: **m_i = d_i + d_i·α·c_i**. The cue term is multiplicative with the deficit, not added on its own: with no deficit, a cue has no effect. Each motivation controls one variable toward a set point (100 in their table); each behaviour carries declared effects on the variables (e.g. avoid: +0.2 to temperature and energy deficits). Whether the 1997 paper used this exact form is still unconfirmed.
- **Selection.** Winner-take-all among motivations, compared with "voting-based" policies in the two-resource problem (Avila-García, Cañamero, te Boekhorst, ECAL 2003, LNCS 2801, title confirmed: "Analyzing the performance of 'winner-take-all' and 'voting-based' action selection policies within the two-resource problem") [citation only].
- **Emotion.** Hormone-like second-order modulation of the motivational system, here of perception (exteroceptors and interoceptors) [read, 2005].
- **Social coupling.** Her group's competitive-resource and affective-bonding robot work is multi-agent in the sense of shared resources and attachment; details not read.
- **Validation.** Plausibility of emergent behaviour in simulation and robots; not fitted to human data [abstract/standard].
- **Translation.** Operands: homeostatic variables, motivation intensities. Operators: behaviours as additive shifts on variables.

## 3. Sloman: CogAff and H-CogAff

**Citations.** Sloman, A. (1998) "Damasio, Descartes, Alarms and Meta-management" (Cogprints 717); Sloman, Chrisley and Scheutz, "The architectural basis of affective states and processes" (Sussex figshare, 2023 chapter version).

**Verified.** Abstracts and repository records via search only **[abstract]**.

- CogAff is a schema (grid) of reactive, deliberative and meta-management layers crossed with perception, central processing and action; H-CogAff is its special case for a human-like system, including fast "alarm" mechanisms that interrupt the slower layers. Emotions are classed by which architectural mechanisms are involved. Motivators are generated and compared with each other; negative affect tends to cause avoidance and positive affect persistence (as summarised in a secondary arXiv paper).
- **Update equations: none.** This is an ontology/design-space framework, deliberately not a quantitative model. It is useful to this strand as a *vocabulary of kinds of state and process*, not as a dynamics.
- Validation: argued from conceptual analysis; none empirical.

## 4. Breazeal: Kismet

**Citations.** Breazeal, C. (2002) *Designing Sociable Robots*, MIT Press; Breazeal (2003) Emotion and sociable humanoid robots, *Int. J. Human-Computer Studies* 59. Project pages at groups.csail.mit.edu/lbr/sociable.

**Verified.** The project pages on homeostatic regulation and on the behaviour system **[read]**. Neither page gives any equation or numbers.

- **Drive set [read].** Three: social (motivates interaction with people), stimulation (play with toys), fatigue (rest).
- **State and update [read, qualitative].** Each drive has a set point and a "homeostatic regime" band around it. Unattended, a drive drifts toward under-stimulated; too much or too fast stimulation pushes it toward overwhelmed. The page gives no rates.
- **Affect link [read].** Regime maps to affect: in-regime = contented (positive valence, balanced arousal); under-stimulated = bored then sorrow (negative valence, low arousal); overwhelmed = distress (negative valence, high arousal).
- **Selection [read].** Behaviours compete in a three-level hierarchy. Drive magnitude contributes to a behaviour's activation ("the larger the magnitude of the drive, the more urgently that need must be addressed"). Releasers (perceptual triggers) and emotion processes feed in as well. The arbitration formula is not on the page.
- **Social coupling [read].** The central point: the human caregiver closes the loop. Kismet's expressions let the caregiver infer need and adjust stimulus type or intensity; "withdraw" signals discomfort; turn-taking couples to the person's speech. So the drives of two agents interact **through displayed affect**, by design.
- **Validation.** Demonstrations and some human-subject interaction studies reported in the book [standard]; not read.
- **Translation.** Operands: drives (with a band), the human as an external regulator. Operators: caregiver stimulation (raises or lowers a drive's level, with an optimal intensity band, not "more is better").

## 5. The Sims motive model (Will Wright, Maxis)

**Verified.** Only secondary: a transcript of Game Maker's Toolkit's video "The Genius AI Behind The Sims" and a summary at gameindustrylibrary.com **[abstract]**. **Zubek attribution confirmed in validation** (bibliographically only): Zubek, R. (2010), "Needs-Based AI", chapter 3.8 in A. Lake (ed.), *Game Programming Gems 8*, Course Technology/Cengage, per tables of contents found by search; the chapter text, and so its attenuation curves and scoring formula, was not read. No Maxis primary source found.

- **Drive set.** In The Sims 1: hunger, hygiene, fun, energy, bladder, social, comfort, room. Each a meter from -100 to +100; overall happiness combines them.
- **Update.** Each meter decays at its own rate (tuned to roughly a human day: eight hours' sleep, three meals), and some decay faster during related actions (bladder drops faster while eating). No exact numbers found.
- **Selection: "smart objects advertise".** The world, not the agent, holds the knowledge of what satisfies what. Each object advertises the motive changes it offers; the Sim scores each available interaction by weighting the advertised gain by current need (a bed is worth more when energy is low), then **picks randomly among the top scorers** (summary, secondary). The commonly described nonlinear "attenuation" curves (a given gain counts for more when the need is low) are [standard]; no source in hand gives their form.
- **Social coupling.** The social motive is satisfied through interactions with other Sims; inter-Sim relationship scores exist but I found no source on how they couple drives.
- **Validation.** None; tuned for believable play. (A Spanish-language article, citing a New York Times interview with Wright, says early autonomy was too good and was reduced to keep the player in control. Not verified.)
- **Translation.** This is the clearest *operator* design in the cluster: an interaction is a vector of motive deltas, selected by a need-weighted score. In social-algebra terms, "advertisement" is an operator's declared effect on the operands' state.

## 6. Maslow-based NPC and agent models

**Verified.** Search results only **[abstract]**; none opened.

- No canonical model. Found: Bourassa, Abdellaoui and Parkinson (2011), "Agent-based computer-generated-forces' behaviour improvement", ICAART 2011 vol. 2, 273-280 (SciTePress; title and authors corrected in validation); a Godot-prototype drive-based NPC model using Hull's drive theory and Maslow, with internal variables (hunger, fatigue, social need, safety) modulating simulated neurotransmitters that produce emotion and drive an FSM (SBGames paper); a "pyramid of motivation" of 23 needs from Maslow, ERG and the Reiss Motivation Profile for social-simulation agents (IVA 2016, Western Sydney); SimSim (Charity, Rajesh, Ombok and Soros, arXiv 2008.11258, August 2020), a Sims-inspired sandbox for divergent-search environment design, which describes The Sims as ranking by happiness with needs ordered by Maslow.
- Pattern: Maslow supplies the *set* and an ordering; implementation is weighted utilities, not strict gating. Validation is plausibility. Treat the Maslow claim for The Sims itself as the SimSim authors' framing, not Maxis's.

## 7. EMA (Marsella and Gratch)

**Citations.** Marsella, S. C. and Gratch, J. (2009). EMA: A process model of appraisal dynamics. *Cognitive Systems Research* 10, 70-90.

**Verified.** Full text **[read]** (pdftotext).

- **Not a drive model; an appraisal model.** Operands: an agent's causal interpretation of its situation, with appraisal frames, one per proposition. Variables: desirability, likelihood, unexpectedness, controllability, causal attribution, changeability.
- **Rules [read].** Emotion label by rule: desirability > 0 and likelihood < 1 = hope; > 0 and = 1 = joy; < 0 and < 1 = fear; < 0 and = 1 = sadness; < 0 with other as cause and low controllability = anger; and so on (Table 2). Intensity: "the intensity of a threat is a function of the likelihood of the threat times the utility of the goal that is threatened" (decision-theoretic calculus; quantitative detail deferred to the 2004 papers). **Mood**: per label, sum the frame intensities and pass through a sigmoid to [0,1]; mood-adjusted intensity of a frame = X + Mood(label).
- **Selection [read].** Coping is driven by the most recently accessed frame with the **highest mood-adjusted intensity**. Coping strategies (planning, seek support, resignation, wishful thinking, distancing, shift blame...) act on intentions, beliefs or desirabilities, and so change the next appraisal.
- **Social coupling.** Through attribution (blame, credit) and others' desirabilities; no multi-agent dynamics law.
- **Validation [read, as claim].** "Good consistency" between predicted and human responses in artificial situations (Gratch and Marsella 2005; Mao and Gratch 2006), including emotional dynamics; plus a coping study against human game responses (abstract-level). Authors explicitly say the single worked example is "not a substitute for rigorous experimental validation".
- **Translation.** Operators = cognitive operators and coping strategies acting on a belief/desire/intention state. The closest to a rule-table (appraisal pattern -> emotion label) in the cluster.

## 8. FAtiMA

**Citations.** Dias and Paiva (2005, EPIA) first FAtiMA; later Dias, Mascarenhas and Paiva "FAtiMA Modular" (2014). Search found AAMAS-proceedings and arXiv descriptions.

**Verified.** Secondary descriptions only **[abstract]**.

- Two layers (reactive, deliberative) on OCC appraisal: desirability, desirability-for-others, praiseworthiness; an emotion fires when its variable passes a threshold. Built for FearNot! (a bullying-education game). Aylett and Louchart (AAMAS 2008) add a "double appraisal" so that the action with the greatest emotional impact is chosen for dramatic effect. Later toolkit: open source, dialogue structure for social-emotional agents.
- Drives/needs: FAtiMA's original goals have importance values; no distinct homeostatic drive model in what I saw [abstract]. Multi-agent in that characters hold relationships (like/dislike) and appraise others' events; update equations not read.
- Validation: user studies of believability and empathy in the FearNot! work [standard].

## 9. WASABI (Becker-Asano and Wachsmuth)

**Citations.** Becker-Asano, C. and Wachsmuth, I. (2010). Affective computing with primary and secondary emotions in a virtual human. *Autonomous Agents and Multi-Agent Systems* 20, 32-49.

**Verified.** Full text **[read]**.

- **State.** A reference point in PAD (pleasure, arousal, dominance) space. An emotional impulse (valence from non-conscious or cognitive appraisal) disturbs a homeostasis; "a dynamic process ... continuously drives" values back to balance. Mood is a slower background state: valences decay toward neutral, mood much slower than emotion.
- **Equation [read].** Awareness likelihood of primary emotion pe: w_pe = (1 - (d_pe - θsat_pe)/(θact_pe - θsat_pe)) · i_pe, with θact > θsat: computation starts when d falls below the activation threshold θact and w equals i once d falls below the saturation threshold θsat (defaults in the study: θsat 0.2, θact 0.64). (Symbols renamed in validation: the Greek letters in the PDF extract are garbled, so the original Λ/Φ labels could not be checked; the structure is as stated.) Pleasure and arousal are "continuously driven back" to balance by a process described in an earlier paper (Becker, Kopp and Wachsmuth 2004), not given here; where d_pe is the distance in PAD space between the current point and the emotion's location, i_pe its base intensity (nine primary emotions). Secondary emotions (hope, fears-confirmed, relief) have base intensity 0, must be triggered by cognition, then decay linearly over a "lifetime" (default 10.0) and are weighted by PAD position (mood-congruent).
- **Drives.** Boredom is derived from low arousal / neutral valence; no motivational drive set. This is an affect dynamics (state-space with attractor), not a needs model.
- **Social coupling.** The Skip-Bo card-game scenario with a human opponent; emotions drive facial expression and shape play. No multi-agent coupling law.
- **Validation [read].** Mood-congruent behaviour argued from psychology literature. There **is** a human-subject study in this paper (corrected in validation; the earlier text implied none): 23 students played the card game against MAX in two conditions (11 and 12), and judged MAX significantly older when secondary emotions were simulated. It is a perception study of the agent, not a fit of the dynamics to human data.

## 10. MAMID (Hudlicka)

**Verified.** Abstracts and talk summaries only **[abstract]**. Hudlicka (2002) "This time with feeling: Integrated model of trait and state effects on cognition and behavior", *Applied Artificial Intelligence*; Hudlicka (2005) AAAI Spring Symposium on metacognition.

- A generic method: personality traits and affective states act as **parameters** of a symbolic cognitive architecture (attention, working memory, goal selection, etc.), so "anxious", "aggressive" and "normal" agents are the same architecture with different parameter settings. Separates emotion *generation* from emotion *effects*.
- Not a drive model; relevant because it treats affect as a *parameter vector acting on the machinery*, close to PSI's modulators. Validation: testbed demonstrations [abstract].

## 11. ALMA (Gebhard)

**Verified.** Full text **[read]** in validation (pdftotext). Gebhard, P. (2005) ALMA: A layered model of affect, AAMAS '05, 29-36.

- Three layers by time scale: emotions (short; 24 OCC types), mood (medium; 8 types in PAD octants), personality (long; Big Five). Appraisal rules authored in an XML language (AffectML); personality scales emotion intensity.
- **Mood update [read; corrected in validation].** Not an average. A **default mood** is computed from the Big Five via Mehrabian's mapping to PAD (example: O 0.4, C 0.8, E 0.6, A 0.3, N 0.4 gives P 0.38, A -0.08, D 0.50). The PAD centroid of currently active emotions, the **virtual emotion center**, then moves mood by a **pull and push** function: mood is first attracted toward the center, and once past it is pushed further into the current mood octant, so consistent emotions intensify mood. A "usual mood change time" (10 minutes for their character) sets the speed; emotions decay (linear in the example config). Return toward the default mood is part of the model, but its rule was not extracted.
- Social coupling: none in the model itself. Validation: a plausibility study with human raters (Gebhard and Kipp, IVA 2006, "Are computer-generated emotions and moods plausible to humans?", existence via search). Kipp, Dackweiler and Gebhard (2011), "Designing emotions: an empirical approach to realistic affect simulation", *KI* 25(3), 205-211 (confirmed on Crossref): the claim that they tuned OCC parameters by regression against user ratings is **unconfirmed** (abstract not reached).

## 12. Homeostatic reinforcement learning (Keramati and Gutkin) — the one theorem found

**Citations.** Keramati, M. and Gutkin, B. (2011) NeurIPS; (2014) Homeostatic reinforcement learning for integrating reward collection and physiological stability, *eLife* 3:e04811.

**Verified.** eLife text **[read]** (first ~100,000 of 218,000 characters).

- **State and equations [read, with one caveat].** Internal state H_t; set point H*. Drive D(H_t) = a distance of the internal state from the set point with free exponents m, n (the page extraction garbled the placement; the paper says m = n = 1 reduces to a distance; I could not confirm the exact form). **Reward = drive reduction**: r(H_t, K_t) = D(H_t) - D(H_t + K_t), where K_t is the outcome's effect on the variables.
- **Theorem [read].** With discount γ < 1, the policy that minimises the sum of discounted drives also maximises the sum of discounted rewards (proof via SDR = D(H₀) + (γ-1)·SDD). So reward seeking *is* homeostatic stability, for a single agent under their assumptions. **This is the only proved result I found in the whole cluster.**
- **Choice/risk.** With n > m > 1 the model reproduces dose-dependence, deprivation potentiation, inhibition by irrelevant drives, and risk aversion.
- **Validation [read].** Qualitative agreement with published animal experiments (Mansfield and Cunningham 1980; McFarland 1969; Hodos 1961; Skjoldager et al. 1993; Miller and Kessen 1952); parameters not fitted to a dataset; one prediction (burst of responding after dose reduction) flagged as untested.
- **Multi-agent: none.** Single agent, physiological variables only. Follow-ups: Yoshida, Sprekeler and Gutkin (2025), "Linking homeostasis to reinforcement learning" (arXiv 2507.04998), a perspective, no new theorem in the abstract; Yoshida, Daikoku, Nagai and Kuniyoshi (2024), *Neural Networks* 177:106379, homeostasis as the sole RL objective on a robot [citation only]. The same reward-as-drive-reduction is what Yoshida and Man couple between agents (section 14).
- **Validation note on "the only theorem".** Keramati-Gutkin is the only proved result found *in this cluster*. Adjacent fields have formal results that were not surveyed: ethology's optimal-control treatment of motivational state (Sibly and McFarland 1976; McFarland and Houston 1981) and RL's optimal-reward problem (Singh, Lewis and Barto 2009, CogSci, pp. 2601-2606, which is a *formulation* with experiments, not a theorem). "Only" should be read as "only one found", not "only one exists".

## 13. Computational psychiatry on motivation (Huys, Dayan et al.)

**Verified.** Huys and Dayan (2009), "A Bayesian formulation of behavioral control", *Cognition* 113(3), 314-328, DOI 10.1016/j.cognition.2009.01.008 (resolved on Crossref in validation); text not read **[abstract, secondary]**.

- Secondary description: helplessness formalised as a prior over whether outcomes depend on one's actions (controllability); a pessimistic prior generalises across contexts. Huys, Vogelstein and Dayan (NIPS 21, 2008, 729-736) apply Bayesian RL to depression: helplessness as a prior over outcome entropy, anhedonia as effective reward size [abstract, confirmed].
- A 2025 effort-decision study in depression (Dayan a co-author) finds reduced willingness to exert effort is driven mainly by an effort-acceptance bias, not by changed reward sensitivity [abstract]. A separate study (N = 47) links apathy to less precise priors about action outcomes [abstract].
- Relevance: these are fitted-to-human-data models of *why drive fails to translate into action* (controllability, effort cost). They supply parameters with clinical meaning, and a data-fitting methodology. They model one agent; no drive set.

## 14. Social and multi-agent drive models (PSI; homeostatic coupling)

- **Detje (Bamberg, Sozionik project with Levi, Stuttgart)**: the design in section 1 **[read]**.
- **Volkmer and Alsabah (2022), "Group Cohesion in Multi-Agent Scenarios as an Emergent Behavior", arXiv 2211.02089** **[abstract]**: PSI-based agents with intrinsic needs for group affiliation, certainty and competence; claim: altruism toward in-group agents and adversarial behaviour toward out-group agents emerge; an out-group bias increased in-group cohesion; outliers (cross-group friends) appear; parameters have strong effects. Setup, metrics, run counts not seen. Plausibility only.
- **Yoshida and Man (2024), "Empathic coupling of homeostatic states for intrinsic prosociality", arXiv 2412.12103, NeurIPS 2024 workshop** **[read, HTML; added in validation]**: homeostatic RL agents with reward r = β(D_t − D_{t+1}). **Affective empathy is an explicit coupling law between agents' drives: D = D_self + w·D_partner** (w = 0.5 in the food-sharing task); cognitive empathy is observing the partner's state instead. Claim: prosocial behaviour (sharing) arises only under the coupling. PPO with LSTM; three small environments; no theorem (an informal argument that a self-interested possessor will not share). Follow-up: "Homeostatic coupling for prosocial behavior" (arXiv 2506.12894), agents decode a partner's displayed emotion into an inferred internal state [abstract].
- This (Volkmer-Alsabah for group structure, Yoshida-Man for a stated pairwise coupling) is the nearest thing in the cluster to what Aldred asked. Both are simulation results, not laws; Yoshida-Man's coupling is, however, written as an equation, a weighted sum of drives across agents, and is the closest existing object to a binary social operator on drive states.

## 15. LLM agents given explicit drives or needs (recent; check validity)

**Verified.** arXiv abstract pages only **[abstract]**.

- **D2A, Desire-driven Autonomous Agent: Wang, Chen, Zhong, Ma and Wang, "Simulating human-like daily activities with desire-driven autonomy" (arXiv 2412.06435, Dec 2024, rev. Sept 2025)**: run in the Concordia text simulator; motivation inspired by a Theory of Needs (social interaction, personal fulfilment, self-care), a "desire-driven task generation" step; claims activities more coherent, human-like and "significantly" more rational than other LLM frameworks. Baselines, metrics, and who judged are **not stated in the abstract** (probably LLM-judged; unverified).
- **Emotional Cognitive Modeling with Desire-Driven Objective Optimization (arXiv 2510.13195, Oct 2025)**: pipeline of state evolution, desire generation, objective optimisation, decision, action; claims "superior ecological validity" and decisions closer to human patterns. Experiments in a proprietary environment; human versus LLM-judged not stated.
- **EILS (Tiwari, arXiv 2512.22200, Dec 2025)**: curiosity, stress, confidence as homeostatic control signals on an RL optimiser (entropy, plasticity, trust-region size). A 7-page proposal: the abstract states the gains as a hypothesis and reports no experiments.
- **E-STEER (arXiv 2604.00005)**: steering emotion representations in LLM hidden states; about emotion, not drives.
- **Validity caution.** In all of these the "drive" is text in a prompt or a scalar the prompt reads. The dynamics (decay, satisfaction) are either absent or hand-coded around the model, and "human-likeness" claims are, as far as the abstracts show, relative to other LLM baselines. I could not confirm human-data validation for any. Treat as demonstrations.

---

## Table: drive sets across architectures

| Architecture | Drive / need set | Social drive? | Level model |
|---|---|---|---|
| PSI / MicroPsi | food, water, physical integrity; affiliation; certainty; competence (task, general) | affiliation (L-signals) | level with target; urge = deviation |
| Cañamero 1997 / Avila-García 2003-05 | controlled variables plus hormones (1997, secondary); temperature, energy (2005) | no (later: bonding/resource competition) | deficit d; m = d + d·α·c |
| Kismet | social, stimulation, fatigue | social drive (via caregiver) | set point plus band |
| The Sims 1 | hunger, hygiene, fun, energy, bladder, social, comfort, room | social | meter -100..+100, per-need decay |
| Maslow NPCs | Maslow/ERG/Reiss categories (up to 23 needs) | yes (love/esteem tier) | weighted utilities |
| EMA | none (goals + appraisal) | via attribution | frame intensity, sigmoid mood |
| WASABI | none; affect space (PAD), boredom | no | point in PAD with homeostatic return |
| ALMA | none; emotion/mood/personality layers | no | PAD mood, pull/push toward emotion centroid, Big-Five default |
| MAMID | none; traits/states as parameters | no | parameter vector |
| Keramati-Gutkin | physiological variables | no | distance D(H) from H* |
| Yoshida-Man 2024 | internal (energy) state, homeostatic | yes: D = D_self + w·D_partner | drive-reduction reward |
| Detje / Volkmer-Alsabah PSI | PSI set with affiliation emphasised | affiliation, in-group/out-group | as PSI |
| D2A (LLM) | social interaction, personal fulfilment, self-care | social | prompt text [abstract] |

Note what is *absent* from every set: **curiosity** as an explicit drive appears only as PSI's certainty/uncertainty-reduction (and as a generic term in EILS); **fear** is an emotion label (EMA, Kismet's overwhelmed/distress, WASABI), never a drive; **desire** is a goal or motive, not a state variable, except in the LLM papers where it is generated text.

## The common update-rule skeleton

Across PSI, Cañamero, Kismet, Sims, Keramati-Gutkin and (loosely) WASABI, one shape recurs:

1. **State**: for each need i, a level x_i with a target x_i*. (Sims: signed meter, target near the top; Kismet: a band, not a point.)
2. **Drift**: x_i decays or is depleted over time at a per-need rate (Sims, PSI affiliation, Kismet).
3. **Urgency**: u_i = f(|x_i* - x_i|), usually proportional or a power (PSI "proportional to the deviation"; Keramati-Gutkin D with exponents).
4. **Selection**: pick the behaviour or motive that maximises u weighted by expected satisfaction or success (PSI: expectancy times value over importance, urgency, success probability; Sims: need-weighted advertised gain with random choice among the top; Cañamero group: highest m_i = d_i(1 + α c_i) wins; EMA: highest mood-adjusted intensity). Often with inertia (PSI selection threshold) or a band (Kismet).
5. **Effect**: an action or interaction adds a delta to one or more x_i (Sims advertisements; Cañamero behaviours; Keramati-Gutkin K_t; Kismet caregiver stimulation).
6. **Optional second layer**: a faster or global affect state modulating (1)-(4) (PSI modulators, Cañamero hormones, EMA mood bleed-through, WASABI PAD, MAMID parameters).

In algebra terms: the state is a vector, drift is a flow, an action is a vector shift (an *operator* acting on operands = agents' states), and selection is an argmax. Nothing in the cluster treats composition of those shifts as an object of study. Two composition *rules* exist as design choices: deficit-times-cue (Cañamero group) and plan amalgamation across motives (PSI); and one cross-agent rule, the weighted sum of drives (Yoshida-Man).

## What exists vs what does not

**Exists.**
- Several executable drive models with the same skeleton; a clear catalogue of drive names (PSI's is the most psychologically organised, with a social drive built in).
- Operator-like objects: Sims advertisements (declared state-delta vectors), PSI operators and L-signals, EMA coping strategies, Kismet caregiver stimulation with an optimal band.
- Affect as modulation of control parameters (PSI, MAMID, Cañamero, WASABI): useful for "fear" and "curiosity" as *modes*, not drives.
- One proved equivalence (Keramati and Gutkin: discounted reward maximisation = discounted drive minimisation), for one agent.
- A little contact with data: Keramati-Gutkin's qualitative agreement with animal experiments (not fitted; corrected in validation, the earlier line called it data-fitting), ALMA's reported regression tuning (unconfirmed), WASABI's 23-subject perception study, EMA's human-response comparisons, PSI's reported fits (claim only; not read), computational psychiatry (parameters with clinical meaning, fitted to human data).

**Does not exist (in what I found).**
- **Theorems about composing drives** (what happens when two drives conflict, add, or one is satisfied through another's frustration). Design rules exist (m = d + d·α·c; PSI amalgamation; Konidaris and Barto 2006 on keeping drive levels comparable and adjusting priorities), but nothing in PSI, Cañamero, Kismet, Sims or EMA states a composition law with proved properties. Everything is either a simulation or a design rule.
- **Group-level drives as first-class objects.** Social drives are individual needs for others' signals (affiliation = L-signal level). A group's drive state is only an emergent observation (Volkmer and Alsabah), never a variable.
- **Drive interaction between agents as an operator with algebra.** Kismet couples agent and human by display; PSI affiliation is designed as agent-to-agent signalling but was run single-agent; D2A and similar are prompts. Yoshida and Man (2024) do write an explicit pairwise coupling, D = D_self + w·D_partner, but study it only by simulation. No composition of agent-to-agent drive operators with analysed properties.
- **Curiosity, fear and desire as drives in a common formalism.** Each of the three sits in a different category across the sources (drive, emotion, goal).
- **Control or prediction with guarantees.** No source predicts group behaviour from drive parameters beyond demonstration; no controllability analysis of the drive dynamics (the Keramati-Gutkin result is the nearest, and concerns optimality, not control).
- **Reliable human-data validation of the update equations.** Wikipedia itself notes PSI's quantitative claims (memory decay, spreading widths) are "rarely supported by experimental evidence"; the Sims and Kismet rates are tuned, not measured.

**Implication for the strand.** The skeleton above is a ready-made starting point for the *state, drift, operator, selection* part of an algebra. The open space is exactly what Aldred's aim names: operators between agents (and groups), their composition rules, and statements provable about them. The nearest precedents to mine are PSI's L-signal/supplicative-signal design (agent-to-agent operators on a need level), the Sims advertisement and PSI operator file as operators that declare their effect, Yoshida-Man's weighted drive coupling (a candidate binary operator, already in equation form), and Keramati-Gutkin's proof style (an equivalence over trajectories). Note that Keramati-Gutkin's identity extends directly to a coupled drive D_self + w·D_partner, since it holds for any drive function; that is an observation of this validation pass, not a published result.

---

## Unconfirmed

- **Cañamero 1997 content.** Bibliographic details confirmed (Crossref, DOI 10.1145/267658.267688); the paper itself still not read. The SS04-02-001 PDF is indeed de Almeida, da Silva and Bazzan (confirmed in validation); it is not hers, but it *describes* her Abbots and Gridland and is now used as a secondary source for them. The equation in section 2 is now sourced to Avila-García and Cañamero 2005 [read]; whether the 1997 paper used the same form is unconfirmed.
- **Zubek, "Needs-based AI"**: resolved in validation as chapter 3.8 of *Game Programming Gems 8* (2010), from tables of contents only; chapter text, attenuation curves and scoring not read. No Maxis primary source (Wright's design talks, Sims 1 postmortem) was found.
- **Kipp, Dackweiler and Gebhard 2011** regression tuning of OCC parameters: paper exists, method claim not checked.
- **PSI equations** (the form of F in expectancy-times-value; numeric decay rates; modulator update rules): Bach's book and Dörner's *Bauplan für eine Seele* not read. MIT MicroPsi slides: URL real but the fetch failed with a certificate error.
- **Dörner and Gerdes 2005, "The Mice' War and Peace"** (KogWis 2005): citation seen only in a bibliography list; the paper was not found.
- **FAtiMA Modular (2014)** and Dias and Paiva (2005): named from secondary sources; not opened.
- **MAMID** primary text (Hudlicka 2002) not retrieved.
- **ALMA**: paper read in validation; only the rule for return to default mood was not extracted.
- **Huys and Dayan 2009 (Cognition)**: existence confirmed on Crossref; text not read.
- **Kismet** equations and human-subject studies (Breazeal 2002 book): not read.
- **Maslow NPC papers** (Bourassa 2011, SBGames, IVA 2016): known from search snippets only.
- **LLM papers**: abstracts only; baselines, metrics and human-data claims unchecked.
- **Keramati-Gutkin**: the exact placement of exponents m, n in D(H) could not be checked (extraction garbled again in validation; the paper's own statement is that m = n = 1 gives Euclidean distance, which suggests D = (Σ|h*_i − h_i|^n)^(1/m), but this is inference). The theorem statement (argmin SDD = argmax SDR for γ < 1) and identity SDR = D₀ + (γ−1)·SDD were re-confirmed.

## Missing work (found by the validation pass, not surveyed)

- **Yoshida and Man (2024)**, empathic homeostatic coupling: now added to section 14; the most important omission, since it is an explicit agent-to-agent drive law.
- **Konidaris and Barto (2006)**, "An adaptive robot motivational system", SAB 2006, LNCS 4095, 346-356 [abstract]: drives as possibly conflicting goals, kept comparable, priorities adjusted over the lifetime, feeding multi-reward RL. A composition design.
- **Singh, Lewis and Barto (2009)**, "Where do rewards come from?", CogSci 2009, 2601-2606 [abstract], and the optimal-reward line (Sorg, Singh and Lewis 2010): where intrinsic drives come from, given fitness. A formulation, not a theorem.
- **Ethology's state-space theory of motivation**: Sibly and McFarland (1976, *American Naturalist*, "On the fitness of behavior sequences", details from memory, unconfirmed), McFarland and Houston (1981) *Quantitative Ethology*, Ludlow's mutual-inhibition model of drive competition (1976, unconfirmed), Tyrrell (1993) on action-selection combination rules, Toates (1986, cited by Avila-García) on cue × deficit. This is the literature where explicit, analysed composition rules for drives most likely exist; it is the biggest gap behind the "no laws" claim.
- **Lowe and Ziemke (2011)**, "The feeling of action tendencies", *Frontiers in Psychology* 2:346 [abstract]: emotion as regulation of goal-directed behaviour; conceptual, no drive algebra.
- **Ashby's ultrastable homeostat** (*Design for a Brain*, 1952), cited by Avila-García for the "viability zone": the original formal homeostatic agent.

## Sources

- https://en.wikipedia.org/wiki/Psi-theory
- https://academic.oup.com/book/1947/chapter/141750469
- https://courses.media.mit.edu/2016spring/mass63/wp-content/uploads/sites/40/2015/09/MicroPsi-FutureAI-Spring-2016.pdf
- https://www2.informatik.uni-hamburg.de/tgi/forschung/projekte/sozionik/journal/2/psi4.pdf (Detje)
- https://arxiv.org/abs/2211.02089 (Volkmer and Alsabah)
- https://dblp.uni-trier.de/pid/34/1508.html (Cañamero bibliography); https://uhra.herts.ac.uk/id/eprint/12751/
- https://arxiv.org/pdf/1705.05172 (emotion in RL agents, survey)
- https://groups.csail.mit.edu/lbr/sociable/homeostatic-regulation.html ; https://groups.csail.mit.edu/lbr/sociable/behavior.html
- https://gameindustrylibrary.com/documents/gmtk-the-genius-ai-behind-the-sims ; https://amara.org/videos/cVoJS4OdmVql/en/4330642
- https://arxiv.org/pdf/2008.11258 (SimSim) ; https://www.scitepress.org/Papers/2011/31870/ ; https://staff.cdms.westernsydney.edu.au/~anton/Publications/IVA_2016.pdf
- https://www.cs.uky.edu/~sgware/reading/papers/marsella2009ema.pdf
- https://cs.uwaterloo.ca/~jhoey/teaching/cs886-affect/papers/WASABIAAMAS2010.pdf
- https://arxiv.org/pdf/2103.03020 ; https://aamas.csc.liv.ac.uk/Proceedings/aamas08/proceedings/pdf/paper/AAMAS08_0296.pdf (FAtiMA)
- https://cdn.aaai.org/Symposia/Spring/2005/SS-05-04/SS05-04-009.pdf (MAMID)
- https://www.dfki.de/web/forschung/projekte-publikationen/publikation/1782 ; https://alma.dfki.de/ (ALMA)
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4270100 ; https://proceedings.neurips.cc/paper/2011/file/9778d5d219c5080b9a6a17bef029331c-Paper.pdf
- https://papers.neurips.cc/paper_files/paper/2008/file/d04d42cdf14579cd294e5079e0745411-Paper.pdf (Huys, Vogelstein, Dayan)
- https://web-archive.southampton.ac.uk/cogprints.org/717/index.html ; https://sussex.figshare.com/articles/chapter/The_architectural_basis_of_affective_states_and_processes/23311934
- https://arxiv.org/abs/2412.06435 ; https://arxiv.org/abs/2510.13195 ; https://arxiv.org/abs/2512.22200 ; https://arxiv.org/abs/2604.00005
- https://api.crossref.org/works/10.1145/267658.267688 ; https://cdn.aaai.org/Symposia/Spring/2004/SS-04-02/SS04-02-001.pdf (de Almeida et al., on Abbots)
- https://uhra.herts.ac.uk/id/eprint/12751/1/902177.pdf (Avila-García and Cañamero 2005, read in validation)
- https://cs.huji.ac.il/course/2005/aisemin/articles2006/docs/pa1a3_29.pdf (Gebhard 2005, ALMA, read in validation)
- https://arxiv.org/html/2412.12103v1 ; https://arxiv.org/abs/2506.12894 ; https://arxiv.org/abs/2507.04998 (Yoshida et al.)

## Validation log (2026-10-29)

Independent pass: sources re-fetched where possible, DOIs resolved on Crossref.

- Dörner / Bach PSI — ✎ corrected: selection rule now sourced to Detje [read] (expectancy × value over importance, urgency, success; lateral inhibition; intention amalgamation); modulator names fixed; "rarely supported by experimental evidence" re-attributed to memory decay and spreading, not need decay. Books still unread.
- Detje (Bamberg/Sozionik report) — ✓ read; Teddy/Küssen operator, single-agent status, "verlieben" passage all confirmed; added the declared delta `Affili -1`.
- Cañamero 1997 — ✎ corrected: DOI resolved; hormones are in the 1997 model (secondary); "Abbotts" → Abbots; equation replaced by the published m_i = d_i + d_i·α·c_i from Avila-García and Cañamero 2005 [read], not "deficit plus stimulus term". 1997 text itself ? unconfirmed.
- de Almeida, da Silva, Bazzan (SS-04-02) — ✓ wrong-paper flag was correct; now used as secondary on Abbots.
- Avila-García, Cañamero, te Boekhorst ECAL 2003 — ✓ title confirmed.
- Avila-García and Cañamero 2005 — ✓ read.
- Sloman CogAff — ✓ exists; content [abstract] as stated, not re-read.
- Breazeal / Kismet — ✓ project page re-read; drives, regimes, affect mapping confirmed. 2003 IJHCS 59:119-155 confirmed via WASABI references.
- The Sims / GMTK — ? secondary only, unchanged; attenuation curves marked [standard].
- Zubek "Needs-Based AI" — ✎ resolved: GPG8 (2010) ch. 3.8, from tables of contents; text unread.
- Maslow NPCs — ✎ Bourassa et al. title/authors/venue corrected (ICAART 2011, + Parkinson); SimSim dated 2020 with authors; IVA 2016 and SBGames ? unreachable.
- EMA — ✓ re-read; Table 2, sigmoid mood, X + Mood, highest mood-adjusted intensity, validation caveat all confirmed; Crossref confirms CSR 10(1):70-90.
- FAtiMA — ✓ FAtiMA Modular confirmed (LNCS Emotion Modeling, 2014, DOI 10.1007/978-3-319-12973-0_3); contents still secondary.
- WASABI — ✎ corrected: there is a 23-subject human study (agent judged older); threshold symbols relabelled (θact/θsat) because the original Λ/Φ could not be checked; DOI 10.1007/s10458-009-9094-9.
- MAMID / Hudlicka 2002 — ✓ Crossref (AAI 16:611-641); content [abstract].
- ALMA — ✎ corrected: read in full; mood is a pull/push toward the active-emotion centroid from a Big-Five default, not an average. Kipp et al. 2011 exists; regression claim ? unconfirmed.
- Keramati and Gutkin — ✓ theorem and identity re-confirmed; D(H) exponent form still ?; "only theorem" ✎ qualified to "only one found in this cluster"; "data-fitting" ✎ corrected to qualitative agreement.
- Huys and Dayan 2009; Huys, Vogelstein, Dayan 2008 — ✓ both confirmed (Crossref / NeurIPS).
- 2025 computational-psychiatry abstracts — ? not re-checked.
- Volkmer and Alsabah 2022 — ✓ title, authors, abstract confirmed.
- D2A — ✎ full title and authors added; Concordia simulator.
- arXiv 2510.13195, 2604.00005 — ✓ exist as described.
- EILS — ✎ it is a proposal with no experiments.
- Dörner and Gerdes 2005 — ? still citation-only (Wikipedia names it).
- Added: Yoshida and Man 2024 (explicit agent-to-agent drive coupling), plus a "Missing work" list.
- Nothing was found to be fabricated; no item removed.

**Verdict.** Bibliographically the survey is sound: every work checked exists as cited, apart from minor title and author errors, and its own [read]/[standard] tags were honest. Its substantive claims overreached in one consequential place. "No stated laws of composition and no agent-to-agent coupling" missed published equations, above all Yoshida and Man's D = D_self + w·D_partner, and "the only theorem" holds only for the cluster as searched. Two model descriptions (ALMA mood, Cañamero intensity) were wrong in form and are now replaced from read sources.
