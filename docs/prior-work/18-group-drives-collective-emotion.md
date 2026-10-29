# Prior work 18: Group-level drives and the transmission of drives between people

Date: 2026-10-29. Survey for `social-algebra`. Not committed. Validated the same day; see the log at the end.

Aim served (Aldred, 2026-10-29): an algebra of basic human and group drives (curiosity, fear, desire) that compose into equations, yield theorems, and are used to predict or control behaviour. This note covers the group-level half: drives that belong to a group, and the transmission of drives between people.

## Summary

1. **Transmission has a standard operator; group drives mostly do not.** Emotional contagion (mimicry, feedback, contagion) is the one well-defined person-to-person transfer operator. It has been written as equations in agent-based models: Schweitzer and Garcia's field model, and the Treur-group model behind ASCRIBE (Bosse et al.), whose update rule is given in section 18. "Group drives" (Bion's basic assumptions, Haidt's hive switch, asabiyya, Brewer's two needs) are named states with no agreed measurement.
2. **Almost every aggregation rule is implicit.** Theories say "the group feels X" without saying whether that means mean, max, threshold or product. The explicit rules are in the computational models (field-mediated sum, weighted average with amplification, threshold) and in Smaldino's identity model (a local frequency count).
3. **Downward causation is mostly one mechanism:** salient identity makes the group a source of appraisal for its members (Mackie et al., Hogg, Reicher's social identity model). It is stated verbally; the equations that exist treat it as a feedback field.
4. **Two opposing drives in balance has few formalisations, not one.** Smaldino et al. 2012 (and Smaldino and Epstein 2015) for Brewer, which collapse the two needs into one preferred group share; and McClelland's PCT conflict, where two references on one variable settle at a gain-weighted virtual reference. **Girard's mimetic mechanism does have formal models** (Sack 2021, with theorems; Antunes 2014; an unpublished scapegoating ABM, 2025), all small and untested against data. Moral panic has none under that name that this pass found.
5. **Empirical standing is poor where the theory is grandest** (Le Bon, Bion, Girard, Haidt) and moderate for the narrow lab-style claims (contagion by mimicry, uncertainty-identity, intergroup emotions, perceived emotional synchrony at gatherings).

**Verification note.** The original pass used web search results only (abstracts, library pages, secondary summaries). The validation pass on 2026-10-29 resolved DOIs through Crossref and read a few texts: the Smaldino et al. 2012 article page, the Bertozzi et al. contagion paper, the Ntika et al. ASCRIBE review, the Goldenberg and Willer comment, and the Thonhauser critique's PMC page. Tags: **[read]** = the validator saw the text itself; **[from abstract]** = abstract, metadata or search summary; **[standard account]** = general knowledge, not checked against a source this pass. Items marked [standard account] that carry weight are repeated in Unconfirmed.

---

## 1. Emotional contagion: Hatfield, Cacioppo and Rapson

- **Citation:** Hatfield, Cacioppo and Rapson (1993), "Emotional contagion", *Current Directions in Psychological Science* 2(3), 96-100, doi 10.1111/1467-8721.ep10770953 [from abstract]; book, *Emotional Contagion*, Cambridge University Press, 1994 (Crossref dates the edition 1993), doi 10.1017/CBO9781139174138 [from abstract]. Review: Hatfield, Bensman, Thornton and Rapson (2014), "New perspectives on emotional contagion", *Interpersona* 8(2), 159-179, doi 10.5964/ijpr.v8i2.162.
- **Shared state:** none at group level. This is a person-to-person transfer; a group-level state appears only by repeated application.
- **Mechanism [from abstract]:** three stages, Mimicry -> Feedback -> Contagion. People automatically and continuously mimic others' expressions, voices, postures and movements; the mimicry feeds back into their own felt emotion moment to moment (the facial-feedback idea). The Emotional Contagion Scale measures susceptibility per person to joy, love, fear, anger and sadness.
- **Aggregation / downward causation:** not specified; the group effect is whatever repeated pairwise transfer produces. No equations in the theory [standard account].
- **Standing:** mimicry and facial feedback are supported in the review's account [from abstract]. Thonhauser (2022), "A critique of the crowd psychological heritage in early sociology, classic phenomenology and recent social psychology", *Continental Philosophy Review* 55(3), 371-389, doi 10.1007/s11007-022-09566-z, argues the "disease model" of automatic, uncontrollable transfer descends from Le Bon and misdescribes how emotion passes [read, PMC page].
- **Translation:** operand: person with a vector of emotion levels; operator: `catch(i, j, e)` weighted by susceptibility of i and expressiveness of j. Natural first operator for the algebra. The ASCRIBE family (section 18) already writes exactly this weighting.

## 2. Kramer, Guillory and Hancock (2014) — Facebook

- **Citation:** "Experimental evidence of massive-scale emotional contagion through social networks", *PNAS* 111(24), 8788-8790, N = 689,003, doi 10.1073/pnas.1320040111 [from abstract]. Editorial Expression of Concern (Verma) published July 2014; Crossref also lists two linked notices dated 3 July 2014 [from abstract].
- **Claim:** reducing positive (or negative) posts in a feed shifted the emotional tone of users' own posts in the same direction, taken as massive-scale contagion without face-to-face contact [from abstract].
- **Standing:** the paper itself calls its effects small, "as small as d = 0.001" [from abstract, quoted in secondary coverage]; one critic (Grohol) put the drop in negative words at about 0.07%. Two critiques are distinct and both matter: **ethics** (no informed consent beyond the terms of service; https://policyreview.info/node/338) and **measurement** (word counts with LIWC 2007, a dictionary tool built for longer texts that misreads negation and sarcasm in short status updates; Panger 2016, "Reassessing the Facebook experiment", *Information, Communication & Society* 19(8), 1108-1126, doi 10.1080/1369118X.2015.1093525) [from abstract]. Treat "contagion exists online" as established in sign, weak in magnitude, and dependent on a crude instrument.
- **Translation:** evidence that the transfer operator can act through a mediated field (the feed) rather than pairwise contact, with a small gain. Gain matters more than existence.

## 3. Collective emotions: von Scheve and Salmela (eds.) 2014

- **Citation:** *Collective Emotions: Perspectives from Psychology, Philosophy, and Sociology*, Oxford University Press, 2014, 447 pp, ISBN 9780199659180 [from abstract]. Reviewed by Cochrane, *Phenomenology and the Cognitive Sciences* 15(3), 467-473, 2016, doi 10.1007/s11097-015-9436-9, who sorts the volume's theories into a taxonomy with objections to each [from abstract].
- **What it is:** a collection rather than one theory. Chapters include social appraisal as a cause of collective emotions (pp. 141-155) and collective pride and shame [from abstract]. Which chapter gives which aggregation rule is Unconfirmed.
- **Translation:** the working distinction (from the standard account [standard account]) is between emotions many people have at once, emotions shared as shared, and emotions of the group as a subject. These are three different sorts of operand: a set of individual states, a mutually known state, and a group-owned state. The algebra must decide which.

## 4. Collective effervescence: Durkheim and Páez et al.

- **Durkheim, *Elementary Forms of Religious Life* (1912)** [standard account]: assembly produces a heightened shared emotional state which binds the group and sacralises its symbols.
- **Páez, Rimé, Basabe, Wlodarczyk and Zumeta (2015)**, "Psychosocial effects of perceived emotional synchrony in collective gatherings", *Journal of Personality and Social Psychology* 108(5), 711-729, doi 10.1037/pspi0000014 [from abstract]. Four studies (two correlational, one semi-longitudinal, one experimental), positive and negative gatherings. Gatherings strengthened collective identity, identity fusion and social integration; **perceived emotional synchrony mediated these effects**; higher synchrony went with stronger emotional reactions, more social support and stronger endorsement of shared beliefs and values. This is the empirical anchor the original pass could not find.
- **Later line [from abstract]:** Wlodarczyk et al. 2020, *Frontiers in Psychology* 11:1721, doi 10.3389/fpsyg.2020.01721 (short perceived-emotional-synchrony scale); Pizarro et al. 2022, *Frontiers in Psychology* 13:974683, doi 10.3389/fpsyg.2022.974683, a **meta-analytic review** of effervescence outcomes at gatherings and demonstrations; Bouchat et al. 2024, *Group Processes and Intergroup Relations* 27(8), 1931-1959, doi 10.1177/13684302231223897, 13 studies, 2,260 participants: group identification and emotional synchrony are distinct constructs, positively associated, each independently predicting outcomes; da Costa et al. 2024, *PSOCIAL* 10(2), e3, doi 10.62174/psocial.11050 [**DOI did not resolve at doi.org in the 2026-10-29 corpus audit; citation unconfirmed**], treat effervescence as perceived emotional synchrony arising bottom-up through shared attention, behavioural synchrony and emotional entrainment.
- **Shared state:** synchrony (alignment of members' states, as perceived by them) plus identification.
- **Aggregation / downward causation:** the measured quantity is *perceived* synchrony, a self-report, not a computed dispersion; reading it as low variance across members is this note's translation, not the authors'. It acts back through increased cohesion and identification (mostly correlational, one experiment) [from abstract].
- **Translation:** a group-level quantity defined on a set of operands (a dispersion, or each member's belief about it), and an operator `synchronise(group, ritual)` that reduces dispersion and raises identification.

## 5. Intergroup emotions theory: Mackie, Devos and Smith (2000)

- **Citation:** "Intergroup emotions: Explaining offensive action tendencies in an intergroup context", *Journal of Personality and Social Psychology* 79(4), 602-616, doi 10.1037/0022-3514.79.4.602 [from abstract]; origin traced to E. R. Smith (1993) [from abstract].
- **Shared state:** group-based emotion: an emotion a person feels because of group membership, appraised on behalf of the group, when identity is salient.
- **Result [from abstract]:** three studies; perceived in-group strength increased anger at the out-group and offensive action tendencies, with anger mediating. Anger and fear were distinct, as were moving against and moving away.
- **Aggregation / downward causation:** no aggregation as such: each member appraises individually on behalf of the group; the group acts on members through salience of identity and the appraisal frame. Emotion and action tendency are tied: anger -> approach/attack, fear -> avoid [from abstract]. Smith, Seger and Mackie (2007, *JPSP* 93(3)) later tested whether group-level emotions are distinct from individual ones and converge within a group [standard account; see Missing].
- **Translation:** a clean operator table candidate: (appraisal of out-group, perceived strength) -> emotion -> action tendency. The one place in this survey where emotion has a defined output in action.

## 6. Group-based emotion and regulation: Halperin, Goldenberg, Gross

- **Process model [from abstract]:** Goldenberg, Halperin, van Zomeren and Gross, "The process model of group-based emotion", *Personality and Social Psychology Review* 20(2), 118-141, 2016 (online 2015), doi 10.1177/1088868315581263. Combines intergroup emotions theory with Gross's process model of regulation: group-based emotions can be regulated at the situation, attention, appraisal and response stages.
- **Collective Emotions [from abstract]:** Goldenberg, Garcia, Halperin and Gross (2020), *Current Directions in Psychological Science* 29(2), 154-160, doi 10.1177/0963721420901574. Defines collective emotions as macro-level phenomena along quality, magnitude and time course. A review; no model in it.
- **Digital emotion contagion [from abstract]:** Goldenberg and Gross (2020), *Trends in Cognitive Sciences* 24(4), 316-328, doi 10.1016/j.tics.2020.01.009.
- **Nonconformity [from abstract]:** Goldenberg et al. (2020), "Beyond emotional similarity: the role of situation-specific motives", *JEP: General* 149, 138-159: people's emotional goals decide whether they converge on others' emotions; empirical, not computational.
- **Amplification [read]:** Goldenberg and Willer (2023), "Amplification of emotion on social media", *Nature Human Behaviour* 7(6), 845-846, doi 10.1038/s41562-023-01604-x, a News & Views on Brady et al. (2023), "Overperception of moral outrage in online social networks inflates beliefs about intergroup hostility", *Nature Human Behaviour* 7(6), 917-927. Three layers of amplification: in expression, in perceivers' reading of each expression, and in their estimate of the collective emotion; algorithms promoting strong expression add a self-reinforcing loop. This is a perceived-aggregate mechanism: members respond to the perceived group state, not the actual one.
- **Computational models (corrected):** Goldenberg-authored computational models do exist, but they model **perception of a group's emotion, not group dynamics**. Goldenberg et al. (2022), "Amplification in the evaluation of multiple emotional expressions over time", *Nature Human Behaviour* 6(10), doi 10.1038/s41562-022-01390-y: nine studies, N = 1,583; people overestimate the mean intensity of a sequence of expressions; a computational model attributes this to stronger memory for the more emotional items, not to nonlinear perception of single faces [from abstract]. Goldenberg, Weisz, Sweeny, Cikara and Gross (2021), "The crowd-emotion-amplification effect", *Psychological Science* (2021; volume and pages not checked): estimated crowd emotion exceeds the true mean, more so with more faces and for anger; attention dwells on the extreme faces [from abstract]. For collective-emotion *formation*, Goldenberg and Willer point to Bosse et al. 2015 (section 18), not to a model of their own [read].
- **Translation:** regulation is the first operator that acts on a drive rather than being one: `regulate(state, stage)`. Perceived-state vs actual-state is a useful two-layer design (operand has a belief about the group's state), and the 2021-2022 papers give that belief a quantitative bias: perceived group mean = actual mean plus an amplification that grows with group size and with the extremity of the most extreme members.

## 7. Crowd psychology: Le Bon to Reicher

- **Le Bon, *La psychologie des foules* (1895)** [standard account]: anonymity, contagion and suggestibility yield a group mind that is irrational and regressive. Thonhauser (2022; section 1) cites McPhail (1991, *The Myth of the Madding Crowd*) and Borch (2012, *The Politics of Crowds*) against it and argues that the crowd "as Le Bon defined it" does not correspond to an actual phenomenon [read, https://pmc.ncbi.nlm.nih.gov/articles/PMC8919694/].
- **Social identity model (SIM) and elaborated model (ESIM):** crowd members act on a shared social identity, which sets both the normative limits of behaviour and who takes part [from abstract]. Reicher's original SIM rests on the St Pauls, Bristol riot of 1980 (Reicher 1984) [standard account]. The *elaborated* model (Reicher, Stott, Drury, from the mid-1990s) treats crowd events as intergroup encounters: a crowd's identity shifts through interaction with another group, typically police, and indiscriminate force perceived as illegitimate produces a shared anti-police identity [from abstract]. Stott, Ball, Drury, Neville, Reicher, Boardman and Choudhury (2018) on the 2011 Haringey riot: behaviour shifted from collective attacks on police to looting; a shared anti-police identity overrode local postcode rivalries; collective empowerment and perceived police incapacity formed a positive feedback loop; the authors say this confirms and extends ESIM [from abstract].
- **Corrected attribution:** the 2005 London bombings belong to a sister model, the social identity model of collective resilience in mass emergencies (Drury, Cocking and Reicher) [standard account], not to ESIM. A Hillsborough application was not confirmed; see Unconfirmed.
- **Aggregation / downward causation:** identity is the state; the crowd's identity is changed by how outsiders treat it, and the changed identity changes what counts as legitimate action. An explicit feedback loop with a second group, stated verbally.
- **Standing:** ESIM has case and field support, mostly qualitative; it has displaced Le Bon in the field's own account.
- **Translation:** operand: group with an identity-and-norm state; operator: `treat(group_B, group_A)` (e.g. indiscriminate force) -> shift in A's identity boundary. A state transition triggered by an act of another group. Directly algebraic.

## 8. Bion's basic assumptions

- **Citation:** Bion, *Experiences in Groups* (1961) [standard account]. Group acts as if it were met to depend on a leader (dependency), to fight or flee (fight-flight), or to await a future pair or saviour (pairing); a rational "work group" mode coexists [standard account]. De Felice et al. (2018), "Group, basic assumptions and complexity science", *Group Analysis* 52(1), 3-22, doi 10.1177/0533316418791117, reportedly count five assumptions once post-Bionian proposals are included (the count is unchecked) [from abstract].
- **Shared state:** an unconscious group-level assumption, the group-drive concept most like "group fear/desire" in the aim. Not derived from members; an emergent mode members slip into.
- **Standing [from abstract]:** little empirical confirmation; hard to operationalise. One 2009 dissertation (18 teams, latent profile analysis) supported a two-class dependency/flight model only (dissertation not identified; see Unconfirmed). Pairing has almost no testing. Treat as hypothesis.
- **Translation:** a discrete mode variable of a group (a small finite set, plus work-group). Useful as a state machine; no transition rules in the source.

## 9. Festinger: cohesiveness and social comparison

- **Festinger, Schachter and Back (1950)**, *Social Pressures in Informal Groups* [standard account]: cohesiveness is the total field of forces acting on members to remain; pressures to uniformity of opinion arise from need for confidence in views or for agreement toward group goals.
- **Festinger (1954)**, "A theory of social comparison processes", *Human Relations* 7(2), 117-140, doi 10.1177/001872675400700202 [from abstract]: drive to evaluate oneself accurately; uses others as yardstick when no objective standard exists; compares with similar others; the need for similar comparison pushes groups toward uniformity. Stated as numbered hypotheses, corollaries and derivations [standard account].
- **Shared state:** cohesiveness (resultant of forces) and the uniformity pressure.
- **Aggregation:** "total of forces" is a definitional sum, not an operational one; the 1950 study measured cohesiveness through sociometric choices [standard account]. Downward: pressure on deviants to conform or leave.
- **Translation:** a drive stated at both levels (individual drive to compare; group pressure to uniformity) in a hypothesis-structured, nearly axiomatic form. Closest in form to what the algebra wants. Later opinion dynamics (note 05) are this made quantitative.

## 10. Hogg's uncertainty-identity theory

- **Citation:** Hogg (2007), "Uncertainty-identity theory", *Advances in Experimental Social Psychology* 39, 69-126, doi 10.1016/S0065-2601(06)39002-8 [from abstract].
- **Claims [from abstract]:** self-uncertainty motivates group identification; shown across numerous minimal-group lab studies; moderated by entitativity (clear, cohesive groups reduce uncertainty more; fuzzy groups do not). Hogg extends to claim that under high uncertainty entitative groups become orthodox, hierarchical and dissent-suppressing. Extremism link is a theoretical extension; a 2025 review is reported to say uncertainty predicts adoption of radical ideas, not violence (https://nps.edu/documents/110773463/161101134/CTX-FALL-2025-C%CC%8Cavlovic%CC%81.pdf; not opened by the validator).
- **Drive:** reduction of self-uncertainty (individual drive, curiosity's opposite pole) satisfied by group membership. Group property: entitativity.
- **Translation:** the cleanest "drive -> group choice" law in this note: `join(person, group)` has strength = f(uncertainty of person, entitativity of group). Entitativity is the group-level quantity. Composable with Brewer's rule. Note the law is verbal; f has no stated form.

## 11. Brewer's optimal distinctiveness

- **Claim [from abstract]:** two opposing needs, inclusion/assimilation and differentiation; social identification is strongest at the level of inclusiveness that resolves the conflict between them (Brewer 1991, "The social self: on being the same and different at the same time", *PSPB* 17(5), 475-482, doi 10.1177/0146167291175001; review Leonardelli, Pickett and Brewer 2010, *Advances in Experimental Social Psychology* 43, 63-113). Verbal; no equation in the sources found.
- **Formal statement [read].** Smaldino, Pickett, Sherman and Schank (2012), "An agent-based model of social identity dynamics", *JASSS* 15(4):7, https://www.jasss.org/15/4/7.html. Well-mixed version: each agent sees global identity frequencies d_g = n_g/N and switches to the identity g minimising |d_g - d*|; keeps its own if among the tied best; otherwise ties random. Spatial version: L x L lattice (L = 50 in examples), neighbourhood a (2r+1) x (2r+1) square including the agent, local frequencies, asynchronous random-order updating. Error: with probability 0.01 an agent picks a random identity, for 4,500 steps, then 500 error-free steps. Naive prediction k* = round(1/d*); well-mixed equilibrium k*(d*) = floor(1/(2d*)) + 1, always fewer identities than 1/d*, so agents never reach optimal distinctiveness, and for d* > 0.5 the population collapses to one identity. Local overlapping neighbourhoods get much closer to the optimum (for d* < 0.3 with larger r). One motive only: the two needs are collapsed into a single preferred share d*.
- **Second model:** Smaldino and Epstein (2015), "Social conformity despite individual preferences for distinctiveness", *Royal Society Open Science* 2(3):140437, doi 10.1098/rsos.140437: agents who each want to be a set distance from the mean end up conforming [from abstract; mechanism standard account].
- **Translation:** a per-person target (a preferred group share d*) and a best-response operator. A drive expressed as a set-point. The model to copy for "two opposing drives in balance", with the caveat that it encodes the balance point, not the two drives.

## 12. Sherif and realistic conflict

- **Claim [standard account]:** conflict arises from competition over scarce resources; contact alone does not reduce hostility; superordinate goals requiring cooperation do. Robbers Cave, 22 boys [standard account].
- **Standing:** criticised for sample and experimenter involvement. Tyerman and Spencer (1983), "A critical test of the Sherifs' Robbers Cave experiments", *Small Group Behavior* 14(4), doi 10.1177/104649648301400407: with scout troops who already knew each other, in-group solidarity did not rise under competition (it fell), while hypotheses on ego involvement and response to appeals for cooperation were largely supported [from abstract]. Social identity theory is the rival (the out-group's mere existence suffices).
- **Translation:** the best-formed intergroup operators: `compete(A,B,resource)` raises hostility; `cooperate(A,B,superordinate_goal)` lowers it; `contact(A,B)` alone has no effect. A rare statement of an operator with a null case; Tyerman and Spencer suggest prior acquaintance is a moderator.

## 13. Moral panic: Cohen, Goode and Ben-Yehuda

- **Cohen, *Folk Devils and Moral Panics* (1972)** [standard account]: moral entrepreneurs, folk devils, media amplification, and a staged sequence; the stage list was not confirmed against the book. Cohen draws on Wilkins's deviancy amplification spiral (1964), a verbal positive-feedback loop [standard account].
- **Goode and Ben-Yehuda (1994)** [standard account]: five criteria: concern, hostility, consensus, disproportionality, volatility; three origin models, grass-roots, elite-engineered, interest-group. Baerveldt, Bunkers, De Winter and Kooistra (1998), "Assessing a moral panic relating to crime and drugs policy in the Netherlands: towards a testable theory", *Crime, Law and Social Change* 29(1), 31-47, doi 10.1023/A:1008208420712, operationalise the criteria [from abstract; the original's "most criteria met" not checked].
- **Formal models:** none found under the name "moral panic" in three searches (original pass plus two by the validator). Nearest formal relatives: the emotion-contagion models of section 18; Glaeser (section 14); and Nizamani, Memon and Galam, "From public outrage to the burst of public violence: an epidemic-like model" (arXiv 1310.0731), five agent types (upset, violent, sensitive, immune, relaxed) in ODEs [from abstract]. None is a moral-panic model by name.
- **Translation:** a group-level state (concern, hostility) out of proportion to the threat, with entrepreneur and target as roles and amplification as a feedback loop. Fits the algebra as a pattern of operators; nothing quantitative exists under this name.

## 14. Girard's scapegoat mechanism and formal models

- **Claim [standard account]:** desire is triangular (subject, model, object); rivalry over scarce objects escalates and spreads; the war of all against all converts to all against one; peace returns only if the excluders unanimously believe the victim guilty. Critics: the origin claims are not verifiable.
- **Formal models of Girard (corrected: they exist):**
  - Sack (2021), "Geometries of Desire: Simulating René Girard's Mimetic Theory", in *Proceedings of the 2020 Conference of the Computational Social Science Society of the Americas*, Springer Proceedings in Complexity, doi 10.1007/978-3-030-83418-0_13. Presents itself as the first computational model of mimetic theory: relationships as directed graphs ("mimetic networks"); simulation finds when the system reaches a "Nash equilibrium of desire" and a tendency to "convergence of desire" on a single object; an appendix gives formal definitions and theorems [from abstract].
  - Antunes (2014), "The Geometry of Desire", AAMAS 2014 (extended abstract, p. 1169): agents revise goals through a Girard-inspired mimetic mechanism (envy, imitation, competition) rather than fitness or novelty [from abstract].
  - Paes (2025), "An agent-based model of scapegoating", NetLogo code with ODD protocol in the CoMSES Computational Model Library (v1.0.1): tension accumulates and spreads on a small-world network; past thresholds, leaders emerge and single out marginal agents; scapegoating lowers collective tension, isolates victims and briefly raises leaders' authority. No peer-reviewed paper found [from abstract].
  - Dupuy as the economics-side extender of Girard remains Unconfirmed.
- **Nearest economic model: Glaeser (2005), "The Political Economy of Hatred", *QJE* 120(1), 45-86** [from abstract]: hatred of out-groups as a supply-and-demand equilibrium; politicians supply stories of out-group crimes, repetition matters more than truth, demand falls when people have private incentive to learn the truth or interact regularly (non-abusively) with the target. A scapegoating model with a different mechanism (political entrepreneurs, not unanimity).
- **Translation:** rivalry as a positive feedback between two operands wanting one object; scapegoating as a phase change from many-against-many to many-against-one with unanimity as threshold. Sack's mimetic network is a ready-made operand (a directed graph of "who models whose desire") with stated equilibrium results; none of these models is tested against data.

## 15. Turchin's asabiyya

- **Cross-reference:** `docs/prior-work/08-history.md` for the main treatment.
- **The model (corrected):** Turchin's frontier model in *Historical Dynamics* (2003) couples a polity's **territory A** (not population) with its average **asabiya S**: dA/dt = c0·A·S·(1 - A/h) - a, and dS/dt = r0·(1 - A/(2b))·S·(1 - S), where h is the spatial scale of power projection, a is geopolitical pressure from the hinterland (not a death rate), and b sets the frontier width: S grows while the polity is small enough to be mostly frontier and decays once A exceeds 2b [from a secondary excerpt; book notation and chapter not checked]. arXiv 1512.07715 is **not** Turchin's source: it is Cheon and Poghosyan, "Spiral orbits and oscillations in historical evolution of empires", *Physica A* 469 (2017) 353-362, which adds a third variable, "metaasabiya" R, and gets spiral orbits [from abstract].
- Turchin gives three ways multilevel selection bears on collective solidarity: intergroup conflict, population and resource constraints, ethnic boundaries [from abstract]. Turchin and Gavrilets co-authored later work (2009, *Social Evolution & History*; Gavrilets, Anderson and Turchin 2010, *Cliodynamics*) [standard account].
- **Translation:** the one named group drive in this survey with its own differential equation. Scalar, one per group, logistic in itself, sign set by the polity's size relative to its frontier. Note 08 holds the validation caveats.

## 16. Collective control: Kent McClelland, perceptual control theory

- **Citations [from abstract]:** McClelland (1994), "Perceptual control and social power", *Sociological Perspectives* 37(4), 461-496: power as alignment of goals among independent control systems, distinct from force, coercion or incentive. McClelland (2004), "Collective control of perception: constructing order from conflict", *International Journal of Human-Computer Studies* 60, 65-99: simulations of closed-loop controllers showing that collective control can stabilise shared variables even when the controllers conflict, and "virtual" actors emerge from it. McClelland (2014), "Cycles of conflict: a computational modeling alternative to Collins's theory of conflict escalation", *Sociological Theory* 32(2), 100-127, doi 10.1177/0735275114536387. McClelland and Fararo (eds.) (2006), *Purpose, Meaning, and Action: Control Systems Theories in Sociology*, Palgrave.
- **The conflict result [from abstract, secondary]:** McClelland's 1993 presentation "Conflictive Control" (reported on Martin Taylor's PCT page, mmtaylor.net/PCT): two control systems holding one variable at different reference levels make it behave as though controlled by a single virtual controller whose gain is the sum of the two gains and whose reference lies between the two. In the standard PCT analysis [standard account] the virtual reference is the gain-weighted mean, r_v = (G1·r1 + G2·r2)/(G1 + G2), while each party's output escalates against the other.
- **Group drive:** none in the Bion sense. Group-level behaviour is the combined outcome of individual set-points on a shared variable. Aggregation rule: gain-weighted mean of references, total gain = sum of gains.
- **Standing:** simulations only; no empirical fit seen. Contents of the 2004 and 2014 papers known only from abstracts.
- **Translation:** drive = (variable, reference, gain). Conflict = two references on one variable, resolved at r_v with escalating effort. The closest fit to "drive as an algebraic object", and a second formalisation of two opposing drives in balance alongside Smaldino. See also notes 05, 07.

## 17. Haidt's hive switch

- **Claim [standard account]:** humans have a "hive switch" that turns off the self and makes us feel part of a larger whole, tied to multilevel selection ("90% chimp, 10% bee"); parochial altruism, not universal love. Source: *The Righteous Mind* (2012), TED talk.
- **Standing [from abstract]:** no peer-reviewed direct tests found; alternatives (approval-seeking, need to belong) explain the same coordination. The effervescence line (section 4) is the best empirical contact. The group-selection premise is contested (Pinker and others against; Sober and Wilson, Wilson and Wilson for) [standard account; not searched].
- **Translation:** a mode switch with triggers (synchrony, awe, ritual) that sets a person's weight on self vs group. Equivalent to a parameter in the aggregation rule.

## 18. Agent-based models of emotion propagation

- **Schweitzer and Garcia (2010)**, "An agent-based model of collective emotions in online communities", *European Physical Journal B* 77(4), 533-545, doi 10.1140/epjb/e2010-00292-1, arXiv 1006.5305 [from abstract]: Brownian agents, each with valence and arousal following stochastic dynamics (relaxation to baseline, a drive term from the field, noise) [mechanism form: standard account]; agents post emotional content to a shared field which feeds back nonlinearly on all; collective emotions appear as a bimodal valence distribution; whether they occur once or recur depends on whether the arousal-field feedback saturates or is superlinear. Garcia, Kappas, Küster and Schweitzer (2016), "The dynamics of emotions in online interaction", *Royal Society Open Science* 3(8):160059: three studies, 207 participants; valence and arousal modelled as relaxation to baseline plus a content-driven force; arousal rises with emotional content of either sign and drops after posting; presented as validating the micro-dynamics of the 2010 model [from abstract].
- **The Treur-group contagion model and ASCRIBE (corrected and completed).**
  - Base model: Bosse, Duell, Memon, Treur and van der Wal (2009), "A multi-agent model for mutual absorption of emotions", ECMS 2009, 212-218, doi 10.7148/2009-0212-0218. Journal form: same authors (2015), "Agent-based modeling of emotion contagion in groups", *Cognitive Computation* 7(1), 111-136, doi 10.1007/s12559-014-9277-9: simulated and mathematically analysed, with absorbing and amplifying variants [from abstract].
  - **ASCRIBE** ("Agent-based Social Contagion Regarding Intentions, Beliefs and Emotions" [standard account for the expansion]) is the Treur group's: Hoogendoorn, Treur, van der Wal and van Wissen (2010), "Modelling the interplay of emotions, beliefs and intentions within collective decision making based on insights from social neuroscience", ICONIP 2010, LNCS, 196-206, doi 10.1007/978-3-642-17537-4_25; journal version Bosse, Hoogendoorn, Klein, Treur, van der Wal and van Wissen (2013), "Modelling collective decision making in groups and crowds: integrating social contagion and interacting emotions, beliefs and intentions", *Autonomous Agents and Multi-Agent Systems* 27(1), 52-84, doi 10.1007/s10458-012-9201-1, which reproduced the 4 May 2010 Amsterdam (Dam Square) panic better with contagion of beliefs, emotions and intentions than without [from abstract].
  - **The equations** [standard account; the product form of γ and the consensus core are confirmed in Ntika et al. and Bertozzi et al., read]. For sender S, receiver R and state q in [0, 1]: contagion strength γ_SR = ε_S · α_SR · δ_R (sender expressiveness × channel strength × receiver openness); total γ_R = Σ_{S≠R} γ_SR; aggregated impact q*_R = Σ_{S≠R} (γ_SR/γ_R) · q_S. Update: q_R(t+Δt) = q_R(t) + γ_R · [ η_R · ( β_R · (1 − (1 − q*_R)(1 − q_R)) + (1 − β_R) · q*_R · q_R ) + (1 − η_R) · q*_R − q_R ] · Δt, where η_R ∈ [0,1] is the tendency to amplify (1) rather than absorb (0) and β_R ∈ [0,1] the bias upward (1) or downward (0). With η_R = 0 it is a pure weighted-average consensus, q̇_R = γ_R (q*_R − q_R), the form Bertozzi et al. analyse.
  - **Validation:** Tsai, Bowring, Marsella and Tambe (IVA 2011, best paper; journal version *JAAMAS* 2013, "Empirical evaluation of computational fear contagion models in crowd dispersions", doi 10.1007/s10458-013-9220-6) compared the Bosse-type model with Durupinar's epidemiological threshold model against video of the Amsterdam incident and a Greek tear-gas protest; the Bosse-type model fitted better (about 14% per agent per frame over a 15 s clip, 12% over 4 s) [read, as reported in Bertozzi et al.]. It was then used in the ESCAPES evacuation simulator (Tsai et al., LAX international terminal). Bertozzi, Rosado, Short and Wang, "Contagion shocks in one dimension", *Journal of Statistical Physics* 158(3), 647-664 (2015; UCLA CAM report 14-36), take the continuum limit of the movement-plus-contagion model (speed ∝ fear) and find shock dynamics related to sticky-particle gas [read].
- **Lee, Park and Moon (AAMAS 2014)**, "Modeling multiple fields of collective emotions with Brownian agent-based model" [from abstract]: extends Schweitzer and Garcia with several fields and a preference parameter; one hypothetical experiment on conditions for extreme polarisation, one reproduction of a real case.
- **Related [from abstract]:** Fan, Xu and Zhao, "Higher contagion and weaker ties mean anger spreads faster than joy in social media" (arXiv 1608.03656, Weibo): anger is more contagious than joy and travels along weaker ties.
- **Standing:** fitted to one incident or to online data; none is a general law. The equations above are the best candidate source for operator definitions.

---

## Candidate list of group drives that recur

| Drive or state | Where | Operand it lives on |
|---|---|---|
| Cohesion / solidarity (asabiyya, cohesiveness, identity fusion) | Festinger, Turchin, effervescence | Group scalar |
| Uniformity pressure | Festinger | Group -> deviant member |
| Uncertainty reduction | Hogg | Person -> group choice |
| Inclusion vs distinctiveness (two opposed) | Brewer, Smaldino | Person set-point |
| Conflicting set-points on one variable | McClelland | Pair of persons on one variable |
| Collective fear / flight | Bion, intergroup emotions, crowd models | Group mode or shared emotion |
| Collective anger / attack | Mackie et al., Bion fight | Group emotion tied to action |
| Dependency (seek a leader) | Bion | Group mode |
| Pairing (hope for a future saviour) | Bion | Group mode |
| Rivalry / mimetic desire | Girard, Sack | Directed graph of persons on objects |
| Scapegoating (unanimous exclusion) | Girard, Cohen, Glaeser | Group -> target |
| Resource competition / hostility | Sherif | Pair of groups |
| Synchrony / unison | Durkheim, Páez | Group dispersion (perceived) |
| Self-submergence (hive switch) | Haidt | Person parameter |
| Curiosity | not found at group level | Gap |

Curiosity and desire in the narrow sense have no group-level counterpart in this cluster; fear and anger do (via appraisal and contagion), and desire appears only as mimetic desire. The table is a list of named states, not evidence that each is a distinct drive: several rows (cohesion, synchrony, self-submergence) may be one construct under three names, and Bouchat et al. 2024 is the only test found of whether two of them separate.

## Known aggregation rules

- **Sum of forces** (Festinger cohesiveness; definitional, not operational).
- **Weighted mean** (contagion models: own state moved toward a strength-weighted mean of others' states; Bosse et al. with η = 0).
- **Weighted mean with nonlinear amplification and bias** (Bosse et al. / ASCRIBE, η and β).
- **Field-mediated sum** (Schweitzer and Garcia): all agents write to a shared field and read from it, nonlinearly; saturating vs superlinear is the stated switch.
- **Threshold / unanimity** (Girard: scapegoat works only with unanimous belief; Goode and Ben-Yehuda: consensus as a criterion; Paes 2025: tension thresholds). Granovetter's threshold model is the standard formal version (see Missing).
- **Local frequency count** (Smaldino et al.: share of identity in neighbourhood against target share).
- **Dispersion / synchrony** (effervescence: measured as perceived synchrony).
- **Gain-weighted mean of references** (McClelland: two controllers on one variable).
- **Perceived, not actual, aggregate** (Goldenberg and colleagues, Brady et al.: members respond to an estimate of the group's state biased upward toward its most extreme members).
- **Mode selection** (Bion: group in one of a small set of modes; no rule for the switch).

## What exists vs what does not

**Exists:**
- A person-to-person transmission operator, with a mechanism and measurable susceptibility (Hatfield et al.), small online effect measured with a crude instrument (Kramer et al.).
- Several explicit agent-based models with equations or rules for emotion propagation (Schweitzer and Garcia, Bosse et al. / ASCRIBE, Lee et al.), each fitted to a narrow case; the Bosse family has a head-to-head video comparison (Tsai et al.) and a continuum analysis (Bertozzi et al.).
- Formalisations of a pair of opposing drives: Smaldino et al. 2012 and Smaldino and Epstein 2015 on Brewer, and the PCT conflict result (McClelland).
- Small formal models of Girard's mimetic mechanism (Sack 2021 with theorems; Antunes 2014; Paes 2025 code), untested against data.
- One differential-equation group drive (Turchin's asabiya, with the caveats in note 08).
- A quantitative bias in how people estimate a group's emotion (Goldenberg et al. 2021, 2022).
- Appraisal -> emotion -> action-tendency mapping for groups (Mackie et al.).
- A verbal but well-tested drive -> group-choice law (Hogg).

**Does not exist (as far as these searches found):**
- A common state vector for group drives, or any agreed list of them. Bion's three, Brewer's two and Festinger's one are separate lists.
- A defined aggregation rule for most "group X" claims; they are asserted, not derived.
- A formal model of moral panic under that name.
- Any treatment of curiosity as a group drive.
- General composition laws: no source says how two different drives or two transmissions combine (does fear plus uncertainty in a group yield dependency?). Theorems exist only inside single models: Smaldino's equilibrium counts, the PCT virtual reference, the Bosse et al. equilibrium analysis, Sack's equilibria of desire, Bertozzi et al.'s shock results.
- Empirical tests of the grand frameworks (Bion, Haidt, Girard); prediction and control are shown only for narrow cases (one evacuation video, one incident, a feed).

## Unconfirmed

- Hatfield, Cacioppo and Rapson 1993/1994 original text: only the 2014 review and abstracts seen.
- Kramer et al.: the full set of reported effect sizes beyond "as small as d = 0.001"; Panger 2016's arguments beyond its title and venue.
- Contents and chapter-level aggregation rules of von Scheve and Salmela 2014.
- Hillsborough as an ESIM case (no source found); the attribution of 7/7 to the collective-resilience model is from the standard account.
- Bion: the 2009 dissertation (not identified); De Felice et al.'s count of five assumptions.
- Cohen's stage list; Wilkins 1964; Baerveldt et al.'s finding that most criteria were met.
- Dupuy's economic extension of Girard; contents of Sack 2021 and Antunes 2014 beyond their abstracts.
- Turchin's equations as printed in *Historical Dynamics* (taken from a secondary excerpt) and the chapter that holds them.
- McClelland 2004 and 2014 content (abstracts only); the 1993 presentation known only through Taylor's description; the gain-weighted formula is the standard PCT result, not seen in McClelland's text.
- Bosse et al. update rule: the full η/β form is the standard account of the 2009/2015 papers; only the γ product and the consensus core were seen in secondary texts.
- Schweitzer and Garcia's explicit stochastic equations (not seen; only the abstract).
- Festinger 1950/1954 and Hogg claims are from summaries; Hogg's effect sizes not seen; the NPS 2025 review not opened.
- Haidt's group-selection debate not searched.

## Missing work worth adding

Bibliographic details below are from the standard account unless a DOI is given; Crossref confirmed Smaldino and Epstein, Sack, Brady et al. 2017 (via the Goldenberg and Willer reference list) and a 2005 conference abstract of Seger, Smith and Mackie.


- **Smith, Seger and Mackie (2007)**, "Can emotions be truly group level? Evidence regarding four conceptual criteria", *JPSP* 93(3), 431-446: the direct empirical test of whether group-level emotion is distinct from individual emotion, converges within groups and regulates behaviour. The most important omission for the aggregation question.
- **Barsade (2002)**, "The ripple effect: emotional contagion and its influence on group behavior", *Administrative Science Quarterly* 47(4); Kelly and Barsade (2001), "Mood and emotions in small groups and work teams": the work-group contagion line.
- **Collins (2004)**, *Interaction Ritual Chains*: "emotional energy" as a drive generated by synchronised interaction, the sociological successor to Durkheim and the target of McClelland 2014.
- **Granovetter (1978)**, "Threshold models of collective behavior", *American Journal of Sociology* 83(6): the canonical threshold aggregation rule.
- **Brady, Wills, Jost, Tucker and Van Bavel (2017)**, *PNAS* 114, 7313-7318: moral-emotional language raises diffusion of political messages within ideological groups.
- **Christakis and Fowler (2008)**, *BMJ*: happiness clustering in the Framingham network, with the homophily-vs-contagion critique that followed.
- **Tsai et al. (2011, 2013)** and **Durupinar et al.** (crowd emotion contagion with personality): the empirical comparison and the rival epidemiological threshold model.
- **Smaldino and Epstein (2015)** and **Sack (2021)**: now cited above; both were missing from the original.

## Validation log (2026-10-29)

Checked against Crossref metadata, arXiv records, abstracts and search summaries, and a few texts read in full or in large part (Smaldino et al. 2012 article page; Bertozzi et al. 2015 preprint; Ntika et al. on ASCRIBE; Goldenberg and Willer 2023; Thonhauser 2022 on PMC). No book was read.

- Hatfield, Cacioppo and Rapson 1993/1994: ✎ corrected (pages 96-100, DOIs added).
- Hatfield et al. 2014 *Interpersona*: ✎ corrected (volume, pages, DOI, title added).
- Thonhauser 2022 (the "2022 critique"): ✎ corrected (author, title, journal identified; same paper as PMC8919694; McPhail and Borch citations confirmed).
- Kramer, Guillory and Hancock 2014: ✎ corrected (volume, pages; "as small as d = 0.001" added; measurement critique separated from ethics).
- Panger 2016: added (✓ Crossref).
- von Scheve and Salmela 2014: ✓.
- Cochrane review 2016: ✎ corrected (pages and DOI added).
- Durkheim 1912: ✓ (standard account).
- Páez et al. 2015: ✎ corrected — the original said the paper "was not found"; it exists (*JPSP* 108(5), 711-729) and its results are now stated.
- Wlodarczyk et al. 2020: ✓.
- Pizarro et al. 2022: ✎ corrected (a meta-analytic review of outcomes, not a measurement paper).
- Bouchat et al. 2024 GPIR meta-analysis: ✎ corrected (authors and pages added; content ✓).
- da Costa et al. 2024 PSOCIAL: ✓ (authors, volume, DOI added).
- Mackie, Devos and Smith 2000: ✓.
- Smith 1993: ✓ (standard account).
- Goldenberg et al. process model: ✎ corrected (2016, 20(2), 118-141; online 2015).
- Goldenberg, Garcia, Halperin and Gross 2020: ✓.
- Goldenberg, Saguy and Halperin "nonconformity": ✎ replaced by the confirmed Goldenberg et al. 2020 *JEP: General* paper on emotional motives; the original attribution could not be matched.
- Goldenberg and Willer 2023: ✓ (read; comment on Brady et al. 2023 confirmed).
- Brady et al. 2023: ✓ (Crossref), moved from Unconfirmed.
- "Goldenberg's computational models": ✎ corrected — they exist (2021 *Psychological Science*, 2022 *Nature Human Behaviour*) but model perception of group emotion, not its dynamics.
- Le Bon 1895: ✓ (standard account).
- McPhail 1991, Borch 2012: ✓ (as cited in Thonhauser), moved from Unconfirmed.
- Reicher SIM / ESIM: ✎ corrected — St Pauls belongs to the original SIM, 7/7 to the collective-resilience model; Hillsborough ? unconfirmed.
- Stott et al. 2018 Haringey: ✓ (authors added).
- Bion 1961: ✓ (standard account).
- De Felice et al. 2018: ✓ existence; ? count of five.
- 2009 Bion dissertation: ? unconfirmed (not identified).
- Festinger, Schachter and Back 1950: ✓ (standard account); ✎ "sum of forces" noted as definitional.
- Festinger 1954: ✓.
- Hogg uncertainty-identity: ✓ (Hogg 2007 citation added); NPS 2025 review ? not opened.
- Brewer 1991: ✓ (DOI added).
- Leonardelli, Pickett and Brewer 2010: ✓.
- Smaldino et al. 2012: ✓ (read; formulas k* = round(1/d*) and floor(1/(2d*)) + 1 confirmed; error schedule and d* > 0.5 collapse added).
- Smaldino and Epstein 2015: added (✓ Crossref).
- Sherif Robbers Cave: ✓ (standard account).
- Tyerman and Spencer 1983: ✎ corrected ("reportedly" removed; finding confirmed from abstract; DOI added).
- Cohen 1972: ✓ (standard account); stage list ?.
- Goode and Ben-Yehuda: ✓ (standard account).
- Dutch moral-panic test: ✎ corrected (Baerveldt et al. 1998; topic is crime and drugs policy, not youth crime).
- Moral panic formal models: ✓ none found under that name (three searches); nearest relative (Nizamani, Memon and Galam outrage ODE model) added.
- Girard formal models: ✎ corrected — "none found" was wrong; Sack 2021, Antunes 2014 and Paes 2025 added.
- Dupuy: ? unconfirmed.
- Glaeser 2005: ✓ (pages 45-86 added).
- Turchin asabiya: ✎ corrected — the equation couples territory and asabiya, the subtracted term is hinterland pressure not a death rate, and arXiv 1512.07715 is Cheon and Poghosyan's metaasabiya extension, not Turchin's source.
- Turchin and Gavrilets 2009/2010: ✓ (standard account).
- McClelland 1993 presentation: ✓ (secondary: Taylor's PCT page confirms the virtual controller with summed gain and intermediate reference).
- McClelland 1994: ✓ (venue added).
- McClelland 2004: ✎ corrected (venue and pages added).
- McClelland 2014: ✓ (DOI added).
- Haidt 2012: ✓ (standard account).
- Schweitzer and Garcia 2010: ✓ (DOI added).
- Garcia, Garas and Schweitzer framework: ? not checked separately.
- Garcia et al. 2016: ✎ corrected (published in *Royal Society Open Science* 3(8), not only arXiv; three studies).
- Bosse, Duell, Memon, Treur and van der Wal 2015: ✓ (volume, pages, DOI added).
- Bosse et al. 2013 Amsterdam incident: ✓ (journal citation added; "2011 on" made specific).
- ASCRIBE: ✎ corrected — authorship resolved (Hoogendoorn, Treur, van der Wal and van Wissen 2010, on the Bosse et al. 2009 base); update equations added; the evacuation comparison is Tsai et al., not Bertozzi et al.
- Bertozzi et al. CAM 14-36: ✎ corrected (authors, title and published version in *J. Stat. Phys.* added).
- Lee, Park and Moon 2014: ✎ corrected (title added; content restated from abstract).
- arXiv 1608.03656: ✓ (authors Fan, Xu and Zhao and the Weibo source added).

**Verdict.** The survey's skeleton is sound and none of its citations was fabricated: every named work that could be looked up exists, and most bibliographic details were right. Its errors are of the "could not find it, so it does not exist" kind, and two of them were load-bearing: it said Girard's mechanism had no formal model (three exist, one with theorems) and that Páez et al. 2015 could not be found (it is a *JPSP* paper central to the effervescence claims); it also misattributed Turchin's equation to an arXiv paper by other authors and mixed two of Reicher's models. Treat its negative claims ("none found", "exactly one") as weak until a second search confirms them.
