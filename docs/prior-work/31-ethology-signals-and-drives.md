# Prior work 31: ethology of signals, releasers and drive interaction

Date: 2026-10-29. Strand: social-algebra. Cluster: how one animal's signal or act triggers or changes another's drive state, i.e. signals as operators on the receiver's drive. Cross-references: Lorenz's hydraulic model, Tinbergen's hierarchy and Dollard-Miller conflict types are in `16-formal-models-of-motivation.md` (not repeated); winner/loser effects and dominance dynamics are in `06` and `09` (cross-referenced only); Maynard Smith-Price games are in `09` A1.

**Method and honesty note.** (Validated 2026-10-29; see the log at the end. Tags added in validation say so.) Bibliographic details (author, title, venue, year, DOI) were confirmed against Crossref for the entries marked "Crossref OK". Content was **not** read at source for any entry except where stated; the abstracts reached this session were: Penn & Szamado 2020 (PMC abstract and fetch, partial), Preston & de Waal 2002 (fragments via search), Enquist & Leimar 1983 (secondary descriptions). Everything else is `[standard account]` (textbook knowledge, not checked this session) or `[from abstract/secondary]`. Treat all effect-on-receiver statements as the field's standard account, to be checked against primaries before anything is built on them. No equation here was re-derived.

**Summary.**
1. Ethology supplies the clearest "signal as operator on another's drive" material in biology, but it states the operator in **words and in game-theoretic payoffs, never as a drive-state transformation**. The receiver's drive is almost always latent: inferred from behaviour change, not measured. The best direct measures are physiological (cortisol, testosterone, heart rate), and they exist for only a few operators (consolation, winning).
2. The one early formal "composition of drives" theory is Tinbergen/Hinde's conflict model (displacement, redirection, ambivalence). It is a qualitative rule set, partly abandoned by Hinde himself.
3. The formal results that exist (war of attrition, sequential assessment, Grafen's handicap model) are about **equilibrium signalling strategy**, not about the effect of a signal on a drive. They give theorems about what signals can be honest and how long contests last, which is a different thing from a transition law for drive.
4. The signal-operator vocabulary (threat, appease, submit, alarm, play-frame, groom, reconcile, console) is well attested; operator **composition** (threat then appease; play-frame then bite) is described, not axiomatised.

---

## 0. Framing: Tinbergen's four questions

**Citation.** Tinbergen, N. (1963). On aims and methods of ethology. *Z. Tierpsychol.* 20, 410-433. DOI 10.1111/j.1439-0310.1963.tb01161.x. Crossref OK.

- **Claim `[standard account]`.** Any behaviour has four distinct questions: causation (proximate mechanism, including the drive state and releasing stimuli), survival value (function), ontogeny, evolution (phylogeny).
- **Use for this strand.** An algebra of drives sits in question 1 (causation) but cannot ignore question 2: a signal operator exists because it pays the sender. That is why every operator below carries both a drive-effect on the receiver and a payoff reason for the sender. Mixing the two is the commonest error in the literature (see section 7).
- **Operand/operator.** Not an operator source; it is a discipline for specifying one. Each operator in the inventory should be written with all four columns: mechanism, function, development, origin.

---

## 1. Sign stimuli, releasers, the innate releasing mechanism, supernormal stimuli

**Citations.**
- Tinbergen, N. & Perdeck, A. C. (1951). On the stimulus situation releasing the begging response in the newly hatched herring gull chick. *Behaviour* 3, 1-39. DOI 10.1163/156853951x00197. Crossref OK (year shown 1951; the issue is dated 1951 in Crossref).
- Lorenz, K. & Tinbergen, N. (1939). Taxis und Instinkthandlung in der Eirollbewegung der Graugans. *Z. Tierpsychol.* 2, 1-29. DOI 10.1111/j.1439-0310.1939.tb01558.x. Crossref OK (title and Lorenz as first author confirmed; the page range is `[standard account]`).
- Tinbergen, N. (1948). Social releasers and the experimental method required for their study. *Wilson Bulletin* 60(1), 6-51. No DOI (JSTOR 4157642). Confirmed against SORA (sora.unm.edu, full-text PDF of pp. 6-51) in validation; a review of the experimental evidence on releasers, answering Rand's criticisms of Lorenz and Tinbergen `[from catalogue description]`.

**Drives.** Feeding (begging), parental care, aggression, reproduction; the receiver's drive is primed (in the classical account) and the sign stimulus releases the action.

**Act/signal.** A sender-side structure or act (red spot on the gull's bill; zig-zag dance of the stickleback male; a model with the key features of a rival's red belly) that is a small subset of the full stimulus situation.

**Effect on receiver `[standard account]`.** An innate releasing mechanism (IRM) is a perceptual filter tuned to the sign stimulus. When the stimulus is present **and** the relevant action-specific energy is high enough, the fixed action pattern fires. Lorenz's version: the IRM acts as a lock on the energy reservoir (see 16 section 2 for the hydraulic form). Threshold lowers with deprivation; "vacuum activity" occurs when energy is high enough that no stimulus is needed. Tinbergen & Perdeck found that pecking rate in chicks is driven by a few stimulus dimensions (a red patch, contrast, a narrow downward-pointing bill), and that models can exceed the natural parent's bill in effectiveness `[standard account]`.

**Supernormal stimuli `[standard account]`.** An artificial stimulus can elicit a stronger response than the natural one (the gull-chick red-spot rods; oystercatcher eggs and giant dummy eggs). This is the clearest evidence that the response is graded in stimulus features, i.e. the receiver computes something like a weighted sum, not a match to a template.

**Formal model.** None beyond the hydraulic form in 16. The implicit law is: response = f(stimulus features, internal level), with threshold reducing as internal level rises (Lorenz) and with stimulus features summing (law of heterogeneous summation, Seitz; `[standard account]`).

**Empirical standing.** The sign-stimulus finding is robust in the classical species. The IRM as a literal innate perceptual device has been softened: learning shapes many releasers (Hinde, and the ontogeny question above); the "energy" reservoir has been criticised and mostly dropped (16 section 2).

**Human analogue.** Infant cues (the "baby schema" of Lorenz), facial features, red in dominance contests; evidence is mixed and mostly correlational. `[standard account]`. Supernormal stimuli are regularly invoked for processed food and media; mostly an analogy, not an experiment.

**Translation.** Operand: receiver with drive level d_i. Operator: releaser R acting on drive i. Law: output behaviour = threshold(d_i + gain(R)). This is the **simplest signal operator**: it does not change the drive, it **gates** its expression. Contrast with the operators in sections 2-7, which change the drive. The algebra needs both kinds: gates (release) and shifts (activate or inhibit).

---

## 2. Conflict behaviour: displacement, redirection, ambivalence (Tinbergen; Hinde)

**Citations.**
- Tinbergen, N. (1952). "Derived" activities; their causation, biological significance, origin, and emancipation during evolution. *Q. Rev. Biol.* 27, 1-32. DOI 10.1086/398642. Crossref OK.
- Hinde, R. A. (1953). The conflict between drives in the courtship and copulation of the chaffinch. *Behaviour* 5, 1-31. DOI 10.1163/156853953x00014. Crossref OK (page range `[standard account]`).
- Hinde on abandoning energy models: Hinde, R. A. (1960). Energy models of motivation. *Symp. Soc. Exp. Biol.* 14, 199-213. Not checked (Unconfirmed).

**Drives.** Two or more simultaneously active, incompatible drives: attack and flight in a territorial boundary dispute; sexual and aggressive in courtship.

**Act/signal.** The behavioural **output of the conflict**: displacement activity (a "irrelevant" act such as grooming, feeding, nest-building in the middle of a threat display), redirected aggression (attacking a third party or object), ambivalent postures (intention movements of both tendencies at once), and alternation.

**Effect on receiver `[standard account]`.** The conflict products are themselves read by conspecifics as signals of the sender's state: they leak the underlying motivational mix. Tinbergen's early theory (1952): when two drives are simultaneously aroused and mutually inhibit each other, their energy can discharge into a third, unrelated system ("sparking over"), hence displacement. Hinde's reworking (from 1953 onwards) found that displacement acts in chaffinches and other species were better explained by **disinhibition** (the two conflicting drives each inhibit a third tendency, and removing that inhibition lets it appear) and by changes in the reactivity of the system, rather than by transfer of energy. Hinde's own review dropped energy language `[standard account]`.

**Formal model.** Qualitative. In operator terms this is the first **composition rule** for drives:
- both drives high, both mutually inhibit: output = ambivalent posture, alternation, or displacement;
- one drive dominant: output = that drive's act, with leakage;
- drive A inhibited by an external factor: output may be redirected to a different target (redirected aggression), i.e. target is an argument of the act, separable from the drive.
Dollard-Miller's gradient model (16 section 3) gives the same pattern quantitatively for approach-avoidance. Lorenz's psychohydraulic model gives the energy form (16 section 2). The ethology adds that **the combination is observable and communicated**. No theorems.

**Empirical standing.** Ambivalent and displacement behaviour is broadly documented in birds, fish and primates; the mechanism (sparking-over versus disinhibition) was contested and Hinde's reworking is the standard modern view `[standard account]`. In primates, displacement behaviours (self-scratching) have been used as behavioural measures of anxiety, validated by pharmacology and cortisol in some work (not checked here).

**Human analogue.** Self-directed behaviour under social stress (scratching, fidgeting) and redirected aggression ("kick the dog") are standard analogues; the primate-anxiety link is the better evidenced one `[standard account]`.

**Translation.** Operand: an agent with a drive vector, not a scalar. Operator: conflict composition, a binary function on two drive levels producing either a mixed output or a displaced output. This is the closest early "equation of drives" in the literature, and also the cautionary tale: the energy interpretation failed, so a law stated as "energy flows" should be stated as "inhibition relations among drives" if it is to survive.

---

## 3. Ritualisation: how acts become signals

**Citation.** Huxley, J. (1966). A discussion on ritualization of behaviour in animals and man: introduction. *Phil. Trans. R. Soc. Lond. B* 251, 249-271. DOI 10.1098/rstb.1966.0010. Crossref OK (validation: Huxley, "Introduction", vol. 251, pp. 249-271, 1966). Huxley credits the concept to Selous (1901) `[from secondary]`. Tinbergen's 1952 paper above and Tinbergen's *The Herring Gull's World* (1953) develop it `[standard account]`.

**Drives.** The drives behind the original act (aggression, feeding, courtship), whose behavioural expression is progressively changed.

**Act/signal.** An ordinary act (an intention movement, a displacement activity, an autonomic response such as pupil or fur change) evolves into a stereotyped, exaggerated, simplified display.

**Effect on receiver `[standard account]`.** Under ritualisation the signal is selected to be conspicuous and unambiguous (exaggeration, repetition, stereotypy, rhythmic form), so its effect on the receiver becomes more reliable. The signal's content is the sender's motivational state (what the original conflict leaked); the receiver's reaction is whatever drive change the receiver's mechanism ties to that content.

**Formal model.** None in the classical literature. Later, signalling theory (sections 5-7) supplies a payoff framework; the evolution of a signal from a cue is analysed in sender-receiver games (Maynard Smith & Harper, *Animal Signals*, 2003, book, not checked).

**Empirical standing.** Comparative method (homologies across related species) provides the evidence; it is descriptive and historical, not experimental `[standard account]`.

**Human analogue.** Facial expressions as ritualised, Darwin-style; ritual in human groups is argued to be analogous (Huxley's volume includes human cases, e.g. Erikson on ontogeny of ritualisation in man, from the search result above). Mostly analogy.

**Translation.** This is the origin of **operators**: an operator in the algebra is a ritualised act, with a stable form, and its effect is defined by a receiver mechanism. It tells us that the **operator set is not arbitrary**: it is the set of acts whose form has been stabilised by selection on both sides. So the primitive operators can be listed from the behavioural catalogue, which is the inventory in section 12.

---

## 4. Aggression, appeasement, submission (Lorenz and critics)

**Citations.**
- Lorenz, K. (1963/1966). *On Aggression* (German original *Das sogenannte Böse*, 1963). Book. Not checked.
- de Waal, F. B. M. (1986). The integration of dominance and social bonding in primates. *Q. Rev. Biol.* 61, 459-479. DOI 10.1086/415144. Crossref OK (page range `[standard account]`).
- Hinde as critic of the instinct-and-energy view: not checked individually (Unconfirmed).

**Drives.** Aggression; fear/flight; in the receiver of an appeasement signal, the aggressive drive is the target.

**Act/signal `[standard account]`.** Lorenz argued that aggression is a spontaneous drive that accumulates and needs discharge, and that species with strong weapons evolved **inhibitory appeasement displays** (e.g. wolf offering its neck, an example from Lorenz's popular writing whose observational basis is itself questioned and not checked here, "turning the vulnerable part") that **switch off** the aggressor's attack. Submission, bared-throat, lowered posture, and in primates grooming offers and "bared-teeth" displays serve similar roles.

**Effect on receiver `[standard account]`.** Lorenz claimed the receiver's attack is inhibited by the signal (inhibition rather than redirection), and that human beings lack such inhibitions toward conspecifics because we evolved weak weapons. This last step is the weakest.

**Critics `[standard account]`.** (i) The hydraulic drive is not supported by neuroscience or by the failure to find a build-up of aggression without stimulation. (ii) Appeasement does not always stop attack: wolves and other canids sometimes kill submissive animals, and the "inhibition" is statistical not absolute. (iii) Adaptive explanations (the signal works because the aggressor gains by not fighting, i.e. games of conflict, section 5) replace the Lorenzian "for the good of the species" reading. de Waal (1986) argues that dominance and bonding are integrated, so submission is part of a relationship, not a switch.

**Formal model.** The "switch-off" is not formalised by Lorenz. In game terms (Maynard Smith & Price 1973, see `09` A1) submission is the Retaliator/Bourgeois conventional settlement; appeasement is the loser's strategy of conceding.

**Empirical standing.** Submission displays reducing attack is well supported as an average effect; the strong claim of a universal innate inhibition is not.

**Human analogue.** Apology, deference, gaze aversion, smile-as-appeasement. Evidence for human appeasement displays exists (embarrassment as appeasement is an argued proposal, not checked here).

**Translation.** Operator: **Appease(a→b)**: lowers b's aggressive drive toward a; operand a's role changes from target to non-target. Operator is **context-dependent** (works when b's aggression is within a certain range and when relationship is stable). Stated as a probability shift, not a deterministic switch.

---

## 5. Threat displays and fighting: war of attrition; sequential assessment

**Citations.**
- Maynard Smith, J. (1974). The theory of games and the evolution of animal conflicts. *J. Theor. Biol.* 47, 209-221. DOI 10.1016/0022-5193(74)90110-6. Crossref OK.
- Parker, G. A. (1974). Assessment strategy and the evolution of fighting behaviour. *J. Theor. Biol.* 47, 223-243. DOI 10.1016/0022-5193(74)90111-8. Crossref OK.
- Enquist, M. & Leimar, O. (1983). Evolution of fighting behaviour: decision rules and assessment of relative strength. *J. Theor. Biol.* 102, 387-410. DOI 10.1016/0022-5193(83)90376-4. Crossref OK.

**Drives.** Aggression (or resource-holding motivation) versus fear/retreat, each tied to cost.

**Act/signal.** Threat display, repeated display or escalating phases ending in physical contact. In the war of attrition the display is the **cost-accumulating persistence**: the one that persists longer wins, and each pays the cost of the shorter persistence.

**Effect on receiver `[standard account]` and `[from secondary]` for Enquist & Leimar.** In the war of attrition (Maynard Smith 1974) the contest is a waiting game where each contestant picks a persistence time, the longer wins, both pay the shorter time; the ESS is a **random persistence with exponential distribution**: the cost a contestant is prepared to pay, x, is drawn from p(x) = (1/V) exp(-x/V), mean V (the resource value); with cost linear in time at rate c, persistence time is exponential with mean V/c `[standard account; corroborated by secondary sources in validation; 1974 paper not read (scanned PDF)]`. It is a mixed strategy; no pure persistence time can be an ESS, since x is beaten by x+ε. Maynard Smith (1974) introduced the model; the general uniqueness and stability treatment is Bishop & Cannings (1978), *J. Theor. Biol.* 70, 85-124, DOI 10.1016/0022-5193(78)90304-1 (Crossref OK). Note: in the pure war of attrition a contestant gains **no information** from the opponent's display, so it is a model of cost display, not of assessment. In sequential assessment (Enquist & Leimar 1983), each contestant gradually accumulates information about the opponent's relative strength through the costs it suffers; the contest ends when one individual's estimate is reliable enough that it judges itself the loser and quits. Predictions from the secondary descriptions (confirmed in validation against several secondary sources, not the paper): **fights between near-equal opponents last longer and are more variable in length, and the slightly weaker contestant sometimes wins; higher assessment error lengthens fights; contests escalate through phases of rising cost and accuracy with no de-escalation; injury is rare**. Empirical support is mixed: contest duration falling with size asymmetry is common, but the full set of predictions is rarely met. Parker (1974) gave the related assessment model in which contestants assess resource-holding potential (RHP) against a threshold.

**Formal model and theorems.** These are real games with **real theorems**: the mixed ESS of the war of attrition, the relation of fight duration to asymmetry in sequential assessment, the expected cost bounds. They are theorems about **equilibrium persistence and decision rules**, not about drive transformations. But the **hidden state** is exactly an algebra's operand: each contestant's estimate of the difference in strength, updated by each round of display. That is a belief-state update operator.

**Empirical standing.** Sequential assessment has support in a number of taxa (contest duration decreasing with size asymmetry); the pure war of attrition is rarer; the choice between self-assessment and mutual-assessment is an active empirical debate `[standard account]` (secondary sources above point to such a debate, e.g. "Dominance, Sharing, and Assessment in an Iterated Hawk-Dove Game", arXiv 1907.02160, not read).

**Human analogue.** Escalating confrontations, negotiation brinkmanship, and strikes as wars of attrition; formal analogues in economics, no systematic test here.

**Translation.** Operator: **Threat(a→b)**: each exchange updates b's (and a's) estimate of relative strength and of the cost of continuing; the contest terminates when a threshold is crossed. Operand: a belief about relative ability plus an accrued cost. This gives a **dynamic with a stopping rule**, a rare thing: the closest to a "theorem" about an operator sequence in this cluster.

---

## 6. Honest signalling: the handicap principle and its critics

**Citations.**
- Zahavi, A. (1975). Mate selection: a selection for a handicap. *J. Theor. Biol.* 53, 205-214. DOI 10.1016/0022-5193(75)90111-3. Crossref OK.
- Grafen, A. (1990). Biological signals as handicaps. *J. Theor. Biol.* 144, 517-546. DOI 10.1016/S0022-5193(05)80088-8. Crossref OK.
- Szamado, S. (2011). The cost of honesty and the fallacy of the handicap principle. *Anim. Behav.* 81, 3-10. DOI 10.1016/j.anbehav.2010.08.022. Crossref OK.
- Penn, D. J. & Számadó, S. (2020). The Handicap Principle: how an erroneous hypothesis became a scientific principle. *Biol. Rev.* 95, 267-290. DOI 10.1111/brv.12563. Crossref OK in validation (online 2019-10-23; volume 95 is 2020). PMC7004190.

**Drives.** Whatever the signal reports: condition, intent, resource-holding potential. Honest signalling concerns whether a signal can be trusted to change the receiver's drive.

**Act/signal.** A costly trait or display (peacock tail, stotting, roaring) whose cost is claimed to guarantee reliability.

**Effect on receiver.** `[from abstract/secondary]` Receivers shift their mating or fighting decision in response to the signal's strength; the question is why receivers believe it.

**Formal model.** Zahavi (1975) proposed verbally that the signal must be costly (a handicap) to be honest. Grafen (1990) gave the formal strategic-choice model (signaller of quality q chooses signal level a; receiver responds with a function of the signal; equilibrium requires the marginal cost of signalling to differ with quality so that higher-quality senders signal more) `[standard account]`; it was widely taken as vindicating the handicap principle. Penn & Számadó (2020) argue `[read, abstract, re-read in validation]` that Grafen's models do not support Zahavi's handicap hypothesis but do support Zahavi's second (1977) hypothesis, condition-dependent signalling (individuals adjust investment in the signal to their condition, so honesty arises from efficient optimal investment rather than waste); that theoretical work shows "signalling costs paid at the equilibrium are neither sufficient nor necessary to maintain signal honesty"; that honesty can evolve through differential benefits as well as differential costs; and that the Handicap Principle should be retired. The formulation that what matters is the **cost of cheating (off-equilibrium) rather than the cost paid at equilibrium** is the thesis of Számadó (2011) by its title and standard account `[not read]`; the earlier draft attributed it to the 2020 abstract, which does not state it in those words.

**Theorems.** Grafen's result is an existence-and-form theorem about signalling equilibria: a monotone signal function with differential cost. Penn & Szamado dispute its interpretation, not its mathematics.

**Empirical standing.** Honest signalling is empirically common; the specific "signal must be wasteful" claim is not well supported; honesty usually depends on shared interest, cost differentials, or index (unfakeable) signals `[standard account]`.

**Human analogue.** Costly signalling in human behaviour (conspicuous consumption, religious costly displays) is a large literature (not checked); the Penn & Szamado critique applies equally.

**Translation.** For the algebra: the **trust** of a signal is a property of the operator and its context (cost differential, shared interest), not of the signal alone. An operator **Signal(a→b, s)** changes b's drive **only if** b's response rule treats s as informative. Honesty becomes an ESS condition on operator pairs (send, receive). This gives a natural place for theorems: "operator pair (S,R) is stable iff differential-cost condition holds".

---

## 7. Alarm calls with referential content; audience effects

**Citations.**
- Seyfarth, R. M., Cheney, D. L. & Marler, P. (1980). Monkey responses to three different alarm calls: evidence of predator classification and semantic communication. *Science* 210, 801-803. DOI 10.1126/science.7433999. Crossref OK.
- Seyfarth, R. M., Cheney, D. L. & Marler, P. (1980). Vervet monkey alarm calls: semantic communication in a free-ranging primate. *Anim. Behav.* 28, 1070-1094. DOI 10.1016/S0003-3472(80)80097-2. Crossref OK.
- Marler, P., Dufty, A. & Pickert, R. (1986). Vocal communication in the domestic chicken: II. Is a sender sensitive to the presence and nature of a receiver? *Anim. Behav.* 34, 194-198. DOI 10.1016/0003-3472(86)90023-0. Crossref OK (added in validation as the audience-effect primary).
- Karakashian, Gyger & Marler (1988) audience effect on alarm calling: cited by later work as foundational, not checked (Unconfirmed).

**Drives.** Fear/vigilance and flight in the receiver; kin and group protection in the sender.

**Act/signal `[standard account]`.** Vervets give acoustically distinct alarm calls for leopards, eagles and snakes; playback experiments showed monkeys respond with the appropriate escape (up a tree for leopard, look up or hide for eagle, look down for snake) without seeing the predator. The title of the Science paper says as much (predator classification, semantic communication).

**Effect on receiver.** The call acts as a **specific releaser of a specific fear response** (fear as a vector, with targeted action). The receiver's drive is not "general arousal" but a tagged one.

**Audience effects `[standard account]`.** Calling rates vary with who is present (more calling when an audience, kin or offspring are nearby; less when alone) in chickens (Marler, Dufty & Pickert 1986) and other species, which is evidence that the sender conditions its signal on the audience's identity and so the operator has an argument (the receiver) it depends on.

**Formal model.** None specific; sender-receiver signalling games cover it (the "functionally referential" status is debated: whether calls encode the referent or the sender's arousal; `[standard account]`).

**Empirical standing.** Playback experiments are the strongest evidence in the cluster for a signal changing a specific behavioural response; whether the call is "referential" in the linguistic sense remains contested.

**Human analogue.** Warning, rumour, panic transmission; see section 11 (contagion).

**Translation.** Operator: **Alarm(a→group, threat-type)**: raises fear/vigilance in receivers with a content tag selecting the action. The operator set must be **typed** (leopard-alarm, eagle-alarm), which suggests drive operators carry a type parameter, not just a magnitude.

---

## 8. Play signals as meta-signals

**Citation.** Bekoff, M. (1995). Play signals as punctuation: the structure of social play in canids. *Behaviour* 132, 419-429. DOI 10.1163/156853995x00649. Crossref OK (page range `[standard account]`).

**Drives.** Playfulness; aggression and predation drives in the actions that are performed in play.

**Act/signal `[standard account]`.** The play bow and other play signals are performed before or between actions (biting, chasing, mounting) that would otherwise be agonistic or sexual. Bekoff's "punctuation" title says signals mark the action as play and are interspersed to maintain the frame, especially before ambiguous or injurious acts.

**Effect on receiver.** The signal changes how the **next acts are read**: a bite after a bow is not read as aggression. It acts on the receiver's **interpretation function** (the map from act to drive response), rather than on the drive directly. That is a **second-order operator**.

**Formal model.** None found. The idea that a signal modifies the mapping from other signals is the structure a "meta-operator" needs.

**Empirical standing.** Observational and descriptive; strong in canids; the model of play bows preceding ambiguous acts is the common finding; the mechanism (what changes in the receiver) is not measured. Modern work on rapid mimicry in play (Palagi et al. 2015, *R. Soc. Open Sci.*, DOI 10.1098/rsos.150505; Crossref returned the title "Rapid mimicry and emotional contagion in domestic dogs", not read) is adjacent.

**Human analogue.** Joking markers, laughter, "just kidding" tagging; plausible and extensively discussed; not checked here.

**Translation.** Operator: **Frame(a→b, mode)**: changes the interpretation function for a's following acts, i.e. an operator acting on the operator set. In the algebra this is a **context or modal operator**: Frame(play)∘Bite ≠ Bite. This is among the most useful finds for the strand, since it shows that the algebra needs operators acting on operators (higher-order).

---

## 9. Grooming as currency; biological markets

**Citations.**
- Dunbar, R. I. M. (1991). Functional significance of social grooming in primates. *Folia Primatol.* 57, 121-131. DOI 10.1159/000156574. Crossref OK.
- Noe, R. & Hammerstein, P. (1994). Biological markets: supply and demand determine the effect of partner choice in cooperation, mutualism and mating. *Behav. Ecol. Sociobiol.* 35, 1-11. DOI 10.1007/BF00167053. Crossref OK.
- Noe, R. & Hammerstein, P. (1995). Biological markets. *Trends Ecol. Evol.* 10, 336-339. DOI 10.1016/s0169-5347(00)89123-5. Crossref OK.
- Barrett, L., Henzi, S. P., Weingrill, T., Lycett, J. E. & Hill, R. A. (1999). Market forces predict grooming reciprocity in female baboons. *Proc. R. Soc. B* 266, 665-670. DOI 10.1098/rspb.1999.0687. Crossref OK (authors corrected in validation: the draft listed "Lee, P. C. & Whiten, A.", who are not authors).
- Fruteau, C., Voelkl, B., van Damme, E. & Noë, R. (2009). Supply and demand determine the market value of food providers in wild vervet monkeys. *PNAS* 106, 12007-12012. DOI 10.1073/pnas.0812280106. Crossref OK. Added in validation.

**Drives.** Affiliation/bond maintenance, safety through allies, hygiene, status.

**Act/signal `[standard account]`.** Grooming is both a service (removes parasites) and a social currency exchanged for tolerance, coalition support, access to infants or food. Dunbar relates grooming time to group size and social cohesion.

**Effect on receiver.** Reduces arousal and aggression (endorphin explanations are argued in the literature, not checked here), and creates a debt or alliance credit.

**Formal model.** Biological markets: partners choose among alternatives, and the **value of a commodity depends on supply and demand**. Predictions in Noe & Hammerstein's framework `[standard account]`: when the supply of a commodity (grooming from a high-rank animal, say) is scarce, its price rises; individuals with scarce commodities get more of the other commodity in return; and partner choice, not mere payoff reciprocity, structures exchanges. Barrett et al. (1999) `[from abstract, via secondary in validation]` studied four chacma baboon troops in two populations differing in contest competition: grooming time was reciprocated within dyads in all troops, time-matching was tighter where grooming could not be exchanged for other commodities, and a rank effect (lower-ranked partner grooms more) appeared in only one of the two high-competition troops. That is support for market-dependent **exchange rates**, not a direct supply/demand price test. The clean experimental test is Fruteau et al. (2009) `[read, abstract]`: a low-ranking female vervet made the sole food provider received more grooming; when a second provider was introduced, the first lost part of that gain, i.e. her grooming "price" fell as supply rose.

**Empirical standing.** Several supportive studies (baboons; vervets with experimental manipulation of supply, Fruteau et al. 2009; cleaner fish); failures and ambiguities exist (not reviewed here).

**Human analogue.** Social exchange, favours, gossip as grooming (Dunbar's hypothesis, from general knowledge, not checked), labour and marriage markets.

**Translation.** Operator: **Groom(a→b)**: raises b's affiliative/trust state toward a, lowers b's aggression, adds to a ledger (a debt); its value is **price-like** and set by relative supply. Biological markets is the only part of this cluster with **comparative-statics predictions**, which are theorems of the supply/demand kind. A usable algebraic form: currency operators with a conserved-ish ledger.

---

## 10. Reconciliation and consolation

**Citations.**
- de Waal, F. B. M. & van Roosmalen, A. (1979). Reconciliation and consolation among chimpanzees. *Behav. Ecol. Sociobiol.* 5, 55-66. DOI 10.1007/BF00302695. Crossref OK.
- Aureli, F., Cords, M. & van Schaik, C. P. (2002). Conflict resolution following aggression in gregarious animals: a predictive framework. *Anim. Behav.* 64, 325-343. DOI 10.1006/anbe.2002.3071. Crossref OK.
- Fraser, O. N., Stahl, D. & Aureli, F. (2008). Stress reduction through consolation in chimpanzees. *PNAS* 105, 8557-8562. DOI 10.1073/pnas.0804141105. Crossref OK.

**Drives.** Affiliation versus lingering aggression and anxiety after a fight; relationship value.

**Act/signal `[standard account]`.** Reconciliation: friendly contact between former opponents soon after conflict (kiss, embrace, grooming). Consolation: contact from a third party to a victim.

**Effect on receiver.** Restores tolerance and reduces post-conflict anxiety; Aureli et al.'s framework `[standard account]` predicts that reconciliation is more likely when the relationship is valuable (value) and secure, and that it reduces the risk of renewed attack (the "valuable relationships hypothesis"). Fraser et al. (2008) `[read, abstract]`: consolation (post-conflict affiliation from a third party to the recipient of aggression) reduced **behavioural** measures of stress in recipients; it was more likely when reconciliation had not occurred (so it may substitute for reconciliation) and between partners with more valuable relationships. de Waal & van Roosmalen (1979) `[from abstract, via secondary]`: former opponents preferentially contacted each other rather than third parties, soon after the fight (kiss linked to reconciliation, embrace to consolation); they named contact between former opponents "reconciliation" and contact of the aggressed party with a third animal "consolation". Wild chimpanzees (Budongo) reconcile less than the captive Arnhem colony, and consolation was not confirmed there `[from secondary]`.

**Formal model.** Only a predictive framework (Aureli et al.), no equations; the testable hypotheses are conditional probabilities.

**Empirical standing.** Strong in primates; the strongest evidence of a **repair operator** in the cluster. Extension to non-primates is more varied.

**Human analogue.** Apology and repair; empirical child-development research exists; not checked.

**Translation.** Operator: **Reconcile(a↔b)**: restores a pair's relationship state and lowers post-conflict anxiety (the drive effect); **Console(c→b)**: lowers b's stress. The first is a **relation-restoring operator**; important because the algebra has to model what happens after harmful acts, not only the acts.

---

## 11. Emotional contagion and empathy: the perception-action model

**Citation.** Preston, S. D. & de Waal, F. B. M. (2002). Empathy: its ultimate and proximate bases. *Behav. Brain Sci.* 25, 1-20 (target article; the full volume 1-71 with commentary). DOI 10.1017/S0140525X02000018. Crossref OK.

**Drives.** Any affective state that is expressed (fear, distress, joy); the target is the observer's own state.

**Act/signal `[read, abstract, in validation]`.** Perceiving an object's state activates the subject's corresponding representations, which in turn activate somatic and autonomic responses: the Perception-Action Model (PAM). Preston & de Waal frame this as supporting alarm, social facilitation, vicariousness of emotions, mother-infant responsiveness and the modelling of competitors and predators, and as explaining the empirical effects of similarity, familiarity, past experience, explicit teaching and salience; interaction with prefrontal functioning explains different levels of empathy across species and ages.

**Effect on receiver.** The observer's state shifts toward the target's. No sign or message is needed beyond the expression; the effect is automatic, graded by familiarity and similarity.

**Formal model.** Conceptual. Not a mathematical model; no theorems. A candidate algebraic form is the **coupling** of two drive vectors with a coupling weight set by similarity and familiarity.

**Empirical standing.** Contagion is well established in rodents and primates (fear contagion, yawn contagion) with debate on the empathy interpretation `[standard account]`; PAM is influential and contested, with commentary in the same issue.

**Human analogue.** Direct; mimicry, mood contagion, panic; the human literature is large and is handled in `18`.

**Translation.** Operator: **Couple(a,b,w)**: b's state moves toward a's with weight w(similarity, familiarity). This is the **linear-averaging** operator, the same form that opinion dynamics uses (`05`); the ethology gives the weight's determinants.

---

## 12. Dominance signals and the winner effect (cross-reference)

Winner/loser effects, dominance formation and the physiology are covered in `06` (lines on winner/loser effects, Chase et al.) and `09` (dominance-formation dynamics). Additions confirmed here:
- Hsu, Y., Earley, R. L. & Wolf, L. L. (2006; Crossref shows year 2005 for the online issue). Modulation of aggressive behaviour by fighting experience: mechanisms and contest outcomes. *Biol. Rev.* 81, 33-74. DOI 10.1017/S146479310500686X. Crossref OK. Reviews winner and loser effects `[standard account]`.
- Fawcett, T. W. & Johnstone, R. A. (2010). Learning your own strength: winner and loser effects should change with age and experience. *Proc. R. Soc. B* 277, 1427-1434. DOI 10.1098/rspb.2009.2088. Crossref OK; `[read, abstract]` (added in validation). Individuals that do not know their own strength track wins and losses; adaptive behaviour then **generates** winner and loser effects, which should change with age and experience (naive individuals aggressive with strong loser effects; experienced ones more moved by wins). This is an explicit **state-update law** (a posterior over own strength, updated per contest outcome) driving a behavioural tendency.
- Oyegbile, T. O. & Marler, C. A. (2005). Winning fights elevates testosterone levels in California mice and enhances future ability to win fights. *Horm. Behav.* 48, 259-267. DOI 10.1016/j.yhbeh.2005.04.007. Crossref OK (page range `[standard account]`). The title states the physiological link: winning raises testosterone and later winning chances. Read at title level only.

**Translation.** Operator: **Win(a,b)** acts on the *sender-side* drive state of a (raises aggression/confidence, mediated by androgen), and **Lose(b,a)** lowers b's. The act's effect is on the actors themselves, as a self-operator, and the receiver of the *display* is the audience. Dominance signals (badges, postures) are the observable output of these state changes.

---

## Inventory of signal operators

| Operator | Source | Target-drive effect | Evidence |
|---|---|---|---|
| Release (gate) | Tinbergen, Lorenz | Lets a ready response fire; threshold lowers with internal level | Strong in classical species (Tinbergen & Perdeck) |
| Supernormal release | Tinbergen | Graded: stronger stimulus, stronger response | Strong, classical |
| Conflict leakage (ambivalent, displaced, redirected) | Tinbergen 1952; Hinde 1953 | Emits signal of two-drive conflict; shifts target | Descriptive; mechanism revised |
| Ritualised display | Huxley 1966; Tinbergen | Stabilises a cue into a signal with reliable effect | Comparative method |
| Appease / submit | Lorenz; de Waal 1986 | Lowers receiver's aggression toward sender | Moderate; not absolute |
| Threat (assessment) | Parker 1974; Enquist & Leimar 1983 | Updates opponent's estimate of relative strength; opponent quits when its estimate crosses a threshold | Theory strong; assessment tests mixed |
| Persist (cost display) | Maynard Smith 1974; Bishop & Cannings 1978 | Accrues cost; no information transmitted; quit time random (exponential) | Pure war of attrition rarely fits data |
| Costly/honest signal | Zahavi 1975; Grafen 1990; Penn & Szamado 2020 | Receiver shifts choice if signal is informative | Honesty common; handicap form disputed |
| Alarm (typed) | Seyfarth, Cheney & Marler 1980 | Raises vigilance/fear with specific action | Playback experiments |
| Play frame | Bekoff 1995 | Changes reading of following acts | Observational |
| Groom | Dunbar 1991; Noe & Hammerstein 1994; Barrett 1999; Fruteau 2009 | Raises affiliation, lowers aggression, creates ledger | Several tests; price-like (experimental in Fruteau 2009) |
| Reconcile | de Waal & van Roosmalen 1979; Aureli 2002 | Restores tolerance; lowers anxiety | Strong in primates |
| Console | de Waal & van Roosmalen 1979; Fraser 2008 | Lowers victim's stress | Moderate (chimpanzees) |
| Couple (contagion) | Preston & de Waal 2002 | Moves receiver's state toward sender's | Strong for contagion; interpretation debated |
| Win / lose | Hsu 2006; Oyegbile & Marler 2005; Fawcett & Johnstone 2010 | Shifts actor's own aggression/confidence (androgen); modelled as Bayesian update of own-strength estimate | Good in several taxa |

---

## What exists vs what does not

**Exists.**
- A rich, well-evidenced **catalogue of signal operators** with named behaviours, functions and some measured effects.
- Genuine **game-theoretic theorems** about signalling equilibria and contest durations (war of attrition, sequential assessment, Grafen's model) and a comparative-statics theory of exchange (biological markets).
- A **qualitative composition rule** for simultaneous drives (conflict, displacement, ambivalence) from Tinbergen and Hinde.
- Evidence that operators have **types** (alarm) and **context arguments** (audience, relationship value).
- The idea of a **meta-operator** (play frame) that changes how other operators are read.

**Does not exist.**
- No formal **transition law for motivational (drive) state** as a function of a received *conspecific signal*, stated as a drive transformation; in classical ethology receiver drive is inferred from behaviour, not modelled. **Narrowed in validation:** formal *state*-transition laws do exist next door and are the natural substrate for one. (a) Belief updates in contests: sequential assessment (Enquist & Leimar 1983) and Bayesian self-assessment (Fawcett & Johnstone 2010) update an estimate of relative or own strength per round or per contest, and behaviour follows the estimate. (b) State-dependent behavioural ecology: McNamara & Houston (1986), *Am. Nat.* 127, 358-378, DOI 10.1086/284489, and Mangel & Clark (1986), *Ecology* 67, 1127-1138, DOI 10.2307/1938669 (both Crossref OK, not read), with Houston & McNamara, *Models of Adaptive Behaviour* (1999, book), give dynamic programming over an internal state x with explicit transition x(t+1) = f(x(t), action, environment) and state-dependent optimal policies; reserves, hunger and condition are exactly drive-like operands. (c) Information-as-Bayesian-update of the receiver in signalling economics: Bradbury & Vehrencamp (2000), *Anim. Behav.* 59, 259-268, DOI 10.1006/anbe.1999.1330 (Crossref OK; Bayesian framing `[standard account, not read]`). (d) Mood as a running estimate of environmental quality updated by experience: Mendl, Burman & Paul (2010), *Proc. R. Soc. B* 277, 2895-2904, DOI 10.1098/rspb.2010.0303 `[read, abstract]`; Nettle & Bateson (2012), *Curr. Biol.* 22, R712-R721, DOI 10.1016/j.cub.2012.06.020; Trimmer et al. (2013), *Behav. Sci.* 3, 501-521, DOI 10.3390/bs3030501 (Crossref OK, not read). What is missing is the join: a signal from b entering a's state-transition function as an input, with the drive vector as the state.
- No **algebra of signals**: no closure, no identities, no composition rules for sequences (threat then appease; play frame then bite), only descriptions.
- No quantitative **drive scales**: ethology's drives are ordinal at best.
- The one early composition-of-drives theory used **energy**, which was abandoned; the replacement (inhibition and disinhibition) was never turned into a calculus.
- Almost no work at group level: the cluster is dyadic, with exceptions in markets and contagion.
- Animal evidence "base applicable" to humans is plausible for contagion, repair and exchange, and weaker for Lorenzian aggression claims.

**Implication for the strand.** The operators are there to be taken as primitives; the missing parts (composition, higher-order operators, and the join of signals into a drive-state update law) are what the algebra would have to supply. The update law need not be invented from scratch: state-dependent dynamic models (McNamara & Houston; Mangel & Clark) and Bayesian assessment models supply the form, with the signal as an input to the transition function. Candidates to carry forward: gate versus shift operators (section 1), typed operators (7), meta-operators (8), ledger operators (9), repair operators (10), coupling (11).

---

## Unconfirmed

- Lorenz, *On Aggression* (1963/1966) and Hinde's critiques: books and critiques not searched.
- Hinde (1960) Energy models of motivation, *Symp. Soc. Exp. Biol.* 14, 199-213: searched in validation, not found in Crossref or the catalogues reached; a Penguin anthology (1971) reprints "Critique of energy models of motivation / R. A. Hinde", and one catalogue gives a 1965 date. Very probably real; details unconfirmed. The claim that Hinde abandoned energy models is the standard account and consistent with Hinde 1953.
- Audience-effect papers beyond Marler, Dufty & Pickert 1986 (Karakashian, Gyger & Marler 1988; Evans & Marler; Cheney & Seyfarth 1985, 1990 book): not checked.
- Maynard Smith & Harper (2003) *Animal Signals*: book, not checked.
- Seitz's law of heterogeneous summation: from memory.
- Waller & Dunbar (silent bared-teeth display) and appeasement-embarrassment literature: query returned nothing, not pursued.
- Grooming-endorphin and "grooming as gossip" claims: from memory.
- Tinbergen & Perdeck: Crossref shows year 1951; commonly cited as 1950. Left as Crossref states.

---

## Clearly missing important work (added in validation)

- Dawkins, R. & Krebs, J. R. (1978). Animal signals: information or manipulation? In Krebs & Davies (eds), *Behavioural Ecology*, 1st ed., 282-309; and Krebs & Dawkins (1984), Animal signals: mind-reading and manipulation (2nd ed.). Book chapters, not checked. The founding statement that a signal is the sender's means of **manipulating the receiver's behaviour**, i.e. the strand's "signal as operator on another's drive" in its own words.
- Maynard Smith, J. & Harper, D. (2003). *Animal Signals*. OUP. The standard classification (index, handicap, minimal-cost, conventional signals) that an operator inventory should be typed against. Book, not checked.
- Searcy, W. A. & Nowicki, S. (2005). *The Evolution of Animal Communication: Reliability and Deception in Signaling Systems*. Princeton. Book, not checked.
- Bradbury, J. W. & Vehrencamp, S. L. (2011). *Principles of Animal Communication*, 2nd ed. Sinauer. The receiver-side, decision-theoretic treatment (signals as updates to the receiver's estimates). Book, not checked.
- State-dependent models (McNamara & Houston 1986; Mangel & Clark 1986; Houston & McNamara 1999) and animal mood models (Mendl et al. 2010; Nettle & Bateson 2012; Trimmer et al. 2013): see "Does not exist" above; they bear directly on the transition-law gap.
- Payne, R. J. H. & Pagel, M. (1996). Escalation and time costs in displays of endurance. *J. Theor. Biol.* 183, 185-193. DOI 10.1006/jtbi.1996.0212. Crossref OK, not read. The cumulative-assessment alternative to Enquist & Leimar, central to the self- versus mutual-assessment debate noted in section 5.

## Validation log (2026-10-29)

Method: every DOI resolved at api.crossref.org/works/<doi>; abstracts read via Europe PMC / PubMed where reachable; other content checked against secondary sources by web search. Tags: [read] only where an abstract was actually read in validation.

- Tinbergen 1963 ✓ (Crossref).
- Tinbergen & Perdeck 1951 ✓ (Crossref 1951; content standard account).
- Lorenz & Tinbergen 1939 ✓ (Crossref, pp. 1-29 confirmed).
- Tinbergen 1948 ✎ corrected: moved out of Unconfirmed; confirmed via SORA/JSTOR, Wilson Bull. 60(1), 6-51.
- Tinbergen 1952 ✓ (Crossref).
- Hinde 1953 ✓ (Crossref, pp. 1-31 confirmed).
- Hinde 1960 ? unconfirmed: not found in Crossref; reprint and a conflicting 1965 date found.
- Huxley 1966 ✎ corrected: DOI found, 10.1098/rstb.1966.0010; pp. 249-271 confirmed by Crossref.
- Maynard Smith & Harper 2003 ? book, not checked.
- Lorenz 1963/1966 ? book, not checked; wolf example flagged as Lorenz's claim.
- de Waal 1986 ✓ (Crossref; author field empty in Crossref, title/venue/pages match).
- Maynard Smith 1974 ✎ corrected: DOI resolves; ESS stated precisely (cost exponential with mean V, time mean V/c), noted that no information passes, Bishop & Cannings 1978 added for the general proof; 1974 text not read (scanned PDF).
- Parker 1974 ✓ (Crossref).
- Enquist & Leimar 1983 ✎ corrected: predictions expanded and empirical support marked mixed (secondary sources).
- arXiv 1907.02160 ? not checked (named as not read in the draft).
- Zahavi 1975 ✓ (Crossref).
- Grafen 1990 ✓ (Crossref; model description standard account).
- Számadó 2011 ✓ (Crossref; not read); now credited with the cost-of-cheating formulation.
- Penn & Számadó 2020 ✎ corrected: DOI confirmed by Crossref (online 2019); abstract read; the "differential marginal cost of cheating" sentence was not in the abstract and was reattributed.
- Seyfarth, Cheney & Marler 1980 (Science) ✓ (Crossref).
- Seyfarth, Cheney & Marler 1980 (Anim. Behav.) ✓ (Crossref).
- Audience effects ✎ corrected: Marler, Dufty & Pickert 1986 added (Crossref); others remain unconfirmed.
- Bekoff 1995 ✓ (Crossref, pp. 419-429 confirmed).
- Palagi et al. 2015 ✓ (Crossref).
- Dunbar 1991 ✓ (Crossref).
- Noë & Hammerstein 1994 ✓ (Crossref).
- Noë & Hammerstein 1995 ✓ (Crossref).
- Barrett et al. 1999 ✎ corrected: two of five authors were wrong (Lee, Whiten replaced by Lycett, Hill); finding restated from abstract (reciprocity and time-matching; rank effect in one troop only), no longer described as a supply/demand price result.
- Fruteau et al. 2009 ✎ added (Crossref; abstract read) as the experimental market test.
- de Waal & van Roosmalen 1979 ✓ (Crossref); definitions confirmed from abstract via secondary.
- Aureli, Cords & van Schaik 2002 ✓ (Crossref; framework content standard account).
- Fraser, Stahl & Aureli 2008 ✓ (Crossref; abstract read, behavioural stress measures confirmed, findings added).
- Preston & de Waal 2002 ✓ (Crossref; abstract read, PAM description corrected in detail).
- Hsu, Earley & Wolf 2006 ✓ (Crossref).
- Oyegbile & Marler 2005 ✓ (Crossref).
- Fawcett & Johnstone 2010 ✎ added (Crossref; abstract read).
- Seitz's law of heterogeneous summation ? not checked.
- Operator inventory ✎ corrected: Threat was attributed to Maynard Smith 1974 (whose model has no assessment) and Persist was given a threshold-quit rule that belongs to Enquist & Leimar; both fixed. No invented operators found; all fifteen map to cited sources.
- "No transition law for the receiver's drive state" ✎ corrected: narrowed; state-dependent dynamic models, Bayesian assessment and mood models supply transition laws for internal state, missing only the signal-as-input join.
- No fabrications found; nothing removed.

**Verdict.** Bibliographically sound: every DOI given resolves to the stated work, and the one hard error was a half-wrong author list (Barrett et al. 1999). The content is a reliable standard account, but it overstated two things: a market "price" result attributed to Barrett et al., and the absence of any formal state-transition law, which is true only of classical ethology and false of state-dependent behavioural ecology next door. Treat effect-on-receiver claims as textbook-level until primaries are read.

## Licences of quoted and transcribed material (2026-10-30)

No passage is quoted at length, no table or figure is transcribed, and no dataset is used. The one unattributed quoted phrase flagged in the audit ("ready to go", section 1) was replaced with the file's own wording. The audit's "check" item (whether any "standard account" sentence derives from Wikipedia) is recorded, not changed: the file cites no Wikipedia page and the prose is the file's own paraphrase, but the passages are unsourced, so the four-questions wording in section 0 and the human-analogue paragraphs should be compared with Wikipedia before publication.

- Tinbergen (1963), *Z. Tierpsychol.* 20; Tinbergen & Perdeck (1951), *Behaviour* 3; Lorenz & Tinbergen (1939); Tinbergen (1952), *Q. Rev. Biol.* 27; Hinde (1953); Huxley (1966), *Phil. Trans.*; de Waal (1986); de Waal & van Roosmalen (1979); Bekoff (1995); Dunbar (1991); Noe & Hammerstein (1994, 1995); Zahavi (1975); Grafen (1990); Maynard Smith (1974); Parker (1974); Enquist & Leimar (1983); Bishop & Cannings (1978); Payne & Pagel (1996); Szamado (2011); Seyfarth, Cheney & Marler (1980, two papers); Marler et al. (1986); Barrett et al. (1999); Fruteau et al. (2009); Aureli et al. (2002); Fraser et al. (2008); Preston & de Waal (2002); Hsu et al. (2006); Fawcett & Johnstone (2010); Oyegbile & Marler (2005); McNamara & Houston (1986); Mangel & Clark (1986); Bradbury & Vehrencamp (2000); Mendl et al. (2010); Nettle & Bateson (2012); Palagi et al. (2015): not determined; publisher copyright presumed. Used as citations with DOI, plus the file's own paraphrase of their findings; no text reproduced. The one exact formula (the war-of-attrition persistence density, Maynard Smith 1974) is a restated equation.
- Tinbergen (1948), *Wilson Bulletin* 60: not determined; publisher copyright presumed (the full text was consulted at SORA, sora.unm.edu). Used as a citation and a description only.
- Penn & Szamado (2020), *Biol. Rev.* 95 (PMC7004190); Trimmer et al. (2013), *Behav. Sci.* 3 (MDPI): possibly open-access licences (the latter likely CC BY), not determined here. Used as citations and paraphrase of the abstract only.
- Crossref metadata (DOIs, titles, years): bibliographic facts, no licence restriction on the facts used.
- Wikipedia: no text taken from it, as far as established (see the check item above).
