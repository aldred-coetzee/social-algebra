# Prior work 16: formal models of drive and motivation

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: mathematical models in which drives already appear in equations. Context: Aldred's new aim, "an algebra which expresses basic human drives and group drives, which we can compose into equations, which we can then use to start making theorems and use to control or predict behavior".

**Method and honesty note.** Read at source this session: only Keramati & Gutkin 2014 (eLife/PMC, first ~100k of 218k characters, via a summarising fetch). The Revelle PDF on the Dynamics of Action exceeded the fetch size limit and was not read. Everything else is `[search/secondary]` (a search-result summary, often of a secondary page) or `[standard account]` (my background knowledge, not checked this session). Equations from standard accounts are stated as the field states them and need checking against the primary text before anything is built on them. Tags per equation below.

**Validation pass, 2026-10-29.** Additionally read at source: Keramati & Gutkin in full (eLife XML, including the proof); Revelle's CTA paper in full (downloaded, so the size limit no longer applied), which gives the Dynamics of Action equations; Revelle's Atkinson lecture handout; Smith, Friston & Whyte (2022) for expected free energy. DOIs resolved via Crossref where given. See the validation log at the end.

**Summary.** Every model in this cluster is a single-agent, state-based law. Drives are scalar or vector quantities, and they combine in one of four ways: multiplicatively (Hull, Atkinson, Vroom), additively with sign (Miller's gradients, prospect theory, Lewin's resultant force), by competition or inhibition (Lorenz/Tinbergen, Gray, Atkinson-Birch), or hierarchically (Powers, Tinbergen, Carver-Scheier). Theorems are rare. What exist are algebraic corollaries (Atkinson's peak at P=0.5, Miller's intersection point, Keramati's discount equivalence). The classic models are single-agent. **Corrected by validation (2026-10-29):** three of them have multi-agent extensions — PCT (collective control: McClelland's virtual controller), active inference (a 2015-2024 multi-agent literature), and Revelle's CTA (a four-person conversation model). So the gap is narrower than first stated: not "no multi-agent version" but "no group-level drive and no multi-agent result validated on people".

---

## 1. Hull: drive-reduction and the behaviour equation

**Citation.** Hull, C. L. (1943). *Principles of Behavior*. Appleton-Century. Revised in Hull (1952), *A Behavior System*. Spence variants: Spence (1956), *Behavior Theory and Conditioning*.

**Equations `[standard account]`, form confirmed `[search/secondary]`.** (Validation 2026-10-29: primaries still not read; the layering below is the standard textbook account, and the multiplier set is confirmed by Wikipedia's Hull article.)
- 1943: sEr = sHr × D (reaction potential = habit strength × drive). Inhibition (Ir reactive, sIr conditioned) is subtracted to give effective reaction potential.
- 1952: sEr = sHr × D × V × K (V stimulus-intensity dynamism, K incentive; some accounts add J, delay of reinforcement, as a further multiplier). Effective potential subtracts total inhibition İr = Ir + sIr; momentary potential further subtracts sOr, the **behavioural oscillation** (a random, trial-to-trial noise term, not a constant). A response is evoked only when momentary potential exceeds the **reaction threshold sLr**. So the full chain is: respond iff sHr·D·V·K − (Ir + sIr) − sOr > sLr. The different orderings in secondary sources are the same product; multiplication commutes, so the "disagreement" noted earlier was not one.
- Hull-Spence variant: Spence made drive and incentive **additive**, E = H × (D + K) (Spence 1956). The additivity is confirmed `[search/secondary]` (Wikipedia, Kenneth Spence, citing Hilgard 1967); the H multiplier is the standard account. The point of the change: incentive moves behaviour even at zero drive, which Hull's product cannot.

**Variables and combination.** D is a general, non-directional energiser, tied to deprivation (hours without food). sHr is learned and directional. They multiply, so a strong habit does nothing at zero drive, and a strong drive does nothing without a habit. This is the first clean multiplicative drive law.

**Theorems / derived predictions.** The multiplicative form predicts that performance scales with deprivation at fixed habit, and that a high drive intensifies whichever response is dominant (Spence's work on anxiety and paired associates, `[search/secondary]` hit on amphetamine and paired-associates). The Hull-Spence programme used this to predict that high drive helps simple tasks and hurts complex ones, where the dominant response is wrong. Formal derivations were postulate-and-corollary in the 1943 book (a long chain of numbered postulates and theorems `[standard account]`), not mathematical proofs.

**Why abandoned `[standard account]`, not confirmed by the search.** Drive reduction as the definition of reinforcement failed on sweet-taste (saccharin) reward with no need reduced, on latent learning, on electrical brain stimulation, and on exploratory and curiosity behaviour (Harlow, Berlyne), which show reinforcement without a primary drive. A single general D was also never measurable independently of the behaviour it explained. Incentive-motivation theories replaced it.

**Operand/operator translation.** Operand: an organism with state (D, H). Operators: deprivation raises D, reinforcement raises H, drive reduction is the reward. D is a scalar attribute of an agent, not a relation between agents.

---

## 2. Lorenz's psychohydraulic model and Tinbergen's hierarchy

**Citations.** Lorenz, K. (1950, 1950s) papers on instinct; Tinbergen, N. (1951). *The Study of Instinct*. Oxford.

**Model `[search/secondary]`.** Lorenz: action-specific energy accumulates in a reservoir, a valve opens under a releasing stimulus, and the flow produces the fixed action pattern. Explains spontaneous "vacuum" behaviour when pressure builds with no stimulus. Tinbergen: instinct centres arranged in a hierarchy, each blocked until an innate releasing mechanism removes the block, energy passing down a cascade to the behaviour. Tinbergen's definition (quoted in a 1951 paper by Allee et al.): "a hierarchically organized nervous mechanism which is susceptible to certain priming, releasing, and directing impulses".

**Equations.** None. These are diagrams and verbal mechanisms; there is no equation in either model `[standard account]`. This makes them relevant as structure and irrelevant as formalism.

**Combination.** Additive pressure against a threshold (the valve). Hierarchical gating (Tinbergen). Competition among centres at the same level, and mutual inhibition `[standard account]`.

**Theorems.** None. Qualitative predictions: threshold for release falls as time since last performance rises; displacement activities when two centres are in conflict `[standard account]`.

**Empirical standing `[search/secondary]`.** The hydraulic model was abandoned in the 1950s-60s: no evidence of energy accumulation, aggression does not reliably rise with time since last bout. Reframed as a conceptual device. The hierarchical idea survived in later theories as hierarchies of feedback loops (a DTIC report notes this), which links straight to Powers.

**Translation.** Operand: an organism with internal level variables. Operators: stimulus-release, discharge. Of the whole cluster this is the one with a visible "operators on levels" shape, but it has no algebra.

---

## 3. Dollard & Miller: gradients and conflict types

**Citations.** Miller, N. E. (1944). Experimental studies of conflict. In Hunt (ed.), *Personality and the Behavior Disorders*. Miller, N. E. (1959). Liberalization of basic S-R concepts. In Koch (ed.), *Psychology: A Study of a Science*, vol. 2. Dollard & Miller (1950), *Personality and Psychotherapy*. Brown (1948) rat harness experiments.

**Equations `[standard account]`; qualitative form confirmed `[search/secondary]`.** Strength of approach tendency A(d) and avoidance tendency V(d) are decreasing functions of distance d from the goal. Both are often drawn as straight lines, A(d) = a − b·d, V(d) = c − e·d, with the avoidance gradient steeper (e > b). Net tendency N(d) = A(d) − V(d). The search confirmed the steeper avoidance gradient and the vacillation point.

**Combination.** Signed addition of two opposed gradients at each point. Conflict types:
- Approach-approach: two positive goals; the equilibrium is unstable, any small shift tips the choice (the "stable/unstable" reading of equilibrium is from standard accounts).
- Avoidance-avoidance: two negative goals; stable equilibrium between them, the organism tends to hover or leave the field.
- Approach-avoidance: one goal with both valences; the gradients cross at a point where the organism stops and vacillates. Because avoidance is steeper, the organism approaches from a distance and retreats when close.
- Double approach-avoidance: two goals each with both valences. Standard accounts treat it as the other types composed.

**Miller's assumptions `[standard account]`** (1944, restated 1959): (i) approach tendency rises nearer the goal; (ii) avoidance tendency rises nearer the feared goal; (iii) the avoidance gradient is steeper; (iv) the strength of each tendency rises with the drive it is based on, raising the height of the whole gradient (tested by Brown 1948: hunger level for approach, shock strength for avoidance, J. Comp. Physiol. Psychol. 41, 450-465, doi:10.1037/h0055463); (v) when incompatible responses compete, the stronger occurs.

**Theorems / derived predictions.** Corollaries of the slopes: (1) an equilibrium exists where A(d) = V(d): d* = (a − c)/(b − e) = (c − a)/(e − b), which is positive only if avoidance is the stronger tendency at the goal (c > a); far away approach wins, near the goal avoidance wins, so the organism **approaches, stops short and oscillates** about d*. (2) Raising approach drive moves d* closer to the goal; raising avoidance drive moves it away. Both follow from (iv). (3) **Corrected 2026-10-29:** the earlier claim that reducing fear "moves the crossing point more" is false in this linear model, since ∂d*/∂a = −1/(e − b) and ∂d*/∂c = +1/(e − b) are equal in size. The Dollard & Miller therapeutic argument is about the **fear experienced at the new equilibrium**, not the distance: raising approach drive pushes the organism closer, to where avoidance (the steeper curve) is higher, so conflict and fear go up; lowering avoidance moves it closer with fear going down `[standard account]`. This is still the nearest thing in the cluster to a predictive result derived from a composition rule. Miller & Murray (1952), "Displacement and conflict: learnable drive as a basis for the steeper gradient of avoidance than of approach", J. Exp. Psychol. 43, 227-231, doi:10.1037/h0053532, confirmed via Crossref.

**Empirical standing.** Rats in a harness (Brown) support steeper avoidance (`[search/secondary]`). Boyd, Robinson & Fetterman (2011), "Miller (1944) revisited", J. Exp. Soc. Psychol. 47, 1192-1197, doi:10.1016/j.jesp.2011.04.017, found slower movement in avoidance conflicts than in approach conflicts (three experiments, N = 291) `[search/secondary]`. Human use is analogical. Later work (a UMass paper `[search/secondary]`) recasts the gradients as drives rather than response tendencies.

**Translation.** Operands: an agent and a goal located at a distance. Operator: net tendency = approach − avoidance. A good candidate for the two-drive core. Distance is the only structure. "Distance" would have to be reinterpreted for social goals (a person, a role, a status).

---

## 4. Lewin: tension systems, valence, force fields

**Citations.** Lewin, K. (1936). *Principles of Topological Psychology*. Lewin (1951). *Field Theory in Social Science*.

**Equations.** B = f(P, E) (or B = f(S) first) `[search/secondary]`. Force on a person toward a region is a function of valence and psychological distance, f ∝ V/d `[standard account, not confirmed]`; the source to check is Lewin (1938), *The Conceptual Representation and the Measurement of Psychological Forces* (Contributions to Psychological Theory 1(4)), where the standard account places f(P,G) = F(Va(G)/e(P,G)) with valence itself a function of tension, Va(G) = F(t, G). Not read. Resultant force on the person is the vector sum of forces `[standard account]`. Tension t is a state of a person's inner-region; need raises t; valence of environmental regions rises with t `[search/secondary]`.

**Combination.** Vector sum of forces in the life space; tension flows between inner regions across permeable boundaries `[search/secondary]`. Lewin's conflict taxonomy (approach-approach, avoidance-avoidance, approach-avoidance) predates Miller and is the source of the three types.

**Theorems.** None, in the mathematical sense. Lewin used topology and vectors descriptively and never proved a theorem; he wrote that topology was the right language and failed to deliver a calculus `[standard account]`. One secondary source notes that the formalism proved hard to measure and did not generate a sustained research line (commercial page, weak `[search/secondary]`).

**Empirical standing.** Zeigarnik effect (unfinished tasks recalled better, tension) is the best-known test; replication is mixed `[standard account]`. Force-field analysis survived as an organisational-change tool, not as a model.

**Group relevance.** Lewin is the only author in this cluster who studied groups directly (group dynamics, leadership climate, quasi-stationary equilibrium, force-field analysis of change), and he gave groups their own life space `[standard account]`. The group version stays verbal.

**Translation.** Operands: person-regions and environment-regions with valence and tension. Operators: tension flow, valence induction, force summation. The nearest ancestor of the aim's "drive + field of others" idea.

---

## 5. Atkinson: achievement motivation and risk-taking

**Citation.** Atkinson, J. W. (1957). Motivational determinants of risk-taking behavior. *Psychological Review* 64, 359-372, doi:10.1037/h0043445 (Crossref confirmed). Atkinson (1964). *An Introduction to Motivation*.

**Equations `[read]`** in Revelle's lecture handout (personality-project.org/revelle/syllabi/301/achievement.pdf) and Revelle's CTA paper, Eq. 9; the 1957 paper itself not read.
- Tendency to achieve success: Ts = Ms × Ps × Is, with Is = 1 − Ps (incentive value of success equals difficulty), so Ts = Ms·Ps·(1 − Ps).
- Tendency to avoid failure: Taf = Maf × Pf × If, with Pf = 1 − Ps and If = −Ps (the shame of failing an easy task), so Taf = −Maf·Ps·(1 − Ps).
- Resultant: Tr = Ts + Taf = (Ms − Maf)·Ps·(1 − Ps). This is already in the 1957 paper, not a 1964 addition (corrected 2026-10-29).
- Raynor's extension (contingent paths): Tr = Σ_i (Ms − Maf)·P_si·(1 − P_si) + T_ext, summing over the chain of tasks a step leads to, plus extrinsic tendencies `[read, handout]`.
- The task "T = M × P × I" in the brief is the first of these.

**Combination.** Triple product; success and failure-avoidance combine as a signed sum of two products.

**Theorems / derived predictions.** Ps(1 − Ps) peaks at Ps = 0.5, so the success-oriented person (Ms > Maf) prefers tasks of intermediate difficulty. If Maf > Ms the sign flips and the person avoids intermediate tasks and prefers very easy or very hard ones. This is a clean consequence of the algebra (derived in the search result's own words).

**Empirical standing.** Revelle's handout `[read]`: ring-toss studies (Hamilton, Heckhausen) gave an inverted U, but the preferred difficulty peaked at Ps ≈ 0.3-0.4, not 0.5; Feather (1961, 1964) on persistence after failure is the other classic test. The sign-flip for fear-of-failure people is less secure `[standard account]`. The model was extended, not refuted: see section 6.

**Translation.** Operands: an agent with two motive strengths (Ms, Maf) and a task with a probability. Operator: tendency = motive × expectancy × incentive. The task's own property enters (difficulty). The model is a function of the agent and one object.

---

## 6. Atkinson & Birch: The Dynamics of Action

**Citation.** Atkinson, J. W. & Birch, D. (1970). *The Dynamics of Action*. Wiley. Reparameterised and simulated: Revelle, W. "Cues, Tendencies and Actions" (CTA), 1986/2008; R function `cta` in the `psych` package.

**Equations `[read]`** — Revelle (2008 working draft), "Cues, Tendencies and Actions: The Dynamics of Action revisited", personality-project.org/revelle/publications/cta.pdf, read in full via local download on 2026-10-29 (it exceeds WebFetch's size limit, not curl's). The 1970 book itself not read.

Original Dynamics of Action (Revelle's Eqs. 1-6, 9). Elements: instigating force F, action tendency T, consummatory value c, consummatory force C, inhibitory force I, negaction tendency N, resistance value r, force of resistance R.
- dT_i/dt = F_i − c_i·T_i if activity i is ongoing; dT_i/dt = F_i if not. (Consummatory force C = c·T; c = 0 when the action is not being done, and depends on the activity otherwise.)
- So an instigated but unexpressed tendency grows linearly; once expressed it rises to the asymptote T∞ = F/c.
- Negaction: dN/dt = I − R = I − r·N, which always relaxes to N∞ = I/r, whether or not the action occurs (resistance costs effort even when idle).
- Resultant tendency T_r = T − N. **Selection rule: the activity with the greatest resultant tendency is expressed.**
- In the achievement case, F = Ps(1 − Ps)·N_ach and I = Ps(1 − Ps)·N_avoid-failure, which recovers Atkinson 1957 as the static limit.
- Known defect: max-selection makes activities "chatter" (start and immediately stop), so the original needed instigating and consummatory lags.

Revelle's CTA reparameterisation (Revelle 1986; Eqs. 10-13), with vectors C (cues, from the environment), T (tendencies), A (actions) and matrices s (cue→tendency), e (tendency→action), c (consummation of tendencies by actions), i (inhibition among actions, including self-inhibition):
- dT/dt = s·C − c·A
- dA/dt = e·T − i·A
- Selection is no longer a max rule: it emerges from mutual inhibition among actions (the `cta` docs say so explicitly). Revelle gives asymptotes for the uncoupled scalar case as T∞ = sCi/c and A∞ = eC/c (as printed). Re-derived here: setting both derivatives to zero gives A∞ = sC/c and T∞ = i·A∞/e = isC/(ec). The printed forms agree with this only when s = e = 1, so use the derived ones.

**Combination.** Original: max-competition between resultant tendencies, each expressed activity depleting itself. CTA: linear dynamical system with cross-inhibition, a connectionist architecture with tendencies as hidden units. This is hydraulic in spirit, but is a real dynamical system, with a defined resting state.

**Theorems / derived predictions `[standard account]`.** The model derives the time allocation across competing activities (percentages of time spent) and the order in which they appear; persistence and resumption after interruption (the Zeigarnik-like resumption, since the unfulfilled tendency persists); how the strength of a tendency following a long stretch of one activity determines the next. These are results of the solved differential equations, not a theorem list in the strict sense.

**Empirical standing.** Few psychologists could handle the differential equations in the 1970s (Revelle `[read]`) and the model was largely forgotten, though it is arguably the most mature formal drive-dynamics model in the cluster. Revelle & Condon (2015), "A model for personality at three levels", J. Res. Personality 56, 70-81, doi:10.1016/j.jrp.2014.12.006 (Crossref confirmed), builds on it; also Brown & Revelle (2021), "Modeling the dynamics of action", doi:10.1016/B978-0-12-819200-9.00012-0 (cited in the `psych::cta` docs, not checked further). Revelle & Michaels (1976) used the inertial property to reconcile Atkinson with Locke on task difficulty over repeated trials. Evidence for the quantitative predictions is thin `[standard account]`.

**Multi-agent use exists (corrected 2026-10-29) `[read]`.** Revelle's CTA paper has a section "Application to social interactions": four people in a discussion, each with their own cue strength and consummation for talking, and **one person's talking inhibits the others'** through the cross-inhibition matrix (Revelle's Figure 7). Revelle reports it does **not** reproduce Antill's (1974) finding that, as group size grows, extraverts' share of talk rises and introverts' falls. So the cluster's "no multi-agent version" claim was wrong for this model: the matrix form makes adding agents trivial, and the one test of it failed.

**Translation.** Operands: action tendencies, as a vector, of one agent or of several (stacking agents into the vector and letting i couple them). Operators: instigate (cue), consummate (act), inhibit. It is the closest existing thing to "drives as state variables under operators" in the whole cluster.

---

## 7. Expectancy-value: Vroom, Eccles

**Citations.** Vroom, V. (1964). *Work and Motivation*. Eccles, J. S., Wigfield, A. et al. (1983 onward), expectancy-value model of achievement choice.

**Equations.** Force = Σ (Valence × Expectancy × Instrumentality) `[search/secondary]` in the multiplicative product form; the search reports "if any factor is zero, motivation is zero". The sum over outcomes is from the standard account. Eccles: choice and performance depend on expectancy of success and subjective task value (attainment, intrinsic, utility, minus cost); the 1983 form is a product, later work treats it as additive or interactive `[standard account]`.

**Combination.** Multiplicative within an outcome, additive across outcomes.

**Theorems.** None; zero-factor annihilation follows from the form.

**Empirical standing `[standard account]`.** Meta-analyses find the product form adds little over additive fits, and correlations with effort are modest. Eccles's model is widely used in education research; the expectancy-value interaction is often not statistically supported.

**Translation.** Operand: an agent with beliefs and values over outcomes. A repackaging of Atkinson, without dynamics.

---

## 8. Carver & Scheier: control theory of self-regulation

**Citation.** Carver, C. S. & Scheier, M. F. (1981). *Attention and Self-Regulation: A Control-Theory Approach to Human Behavior*. Springer. (1982). Control theory: a useful conceptual framework for personality-social, clinical, and health psychology. *Psychological Bulletin* 92(1), 111-135. (1990) Origins and functions of positive and negative affect: a control-process view, *Psychological Review* 97, 19-35, doi:10.1037/0033-295X.97.1.19 (Crossref confirmed). (1998) *On the Self-Regulation of Behavior*. The "1981 vs 1982" conflict was two different works: the 1981 book and the 1982 *Psych. Bull.* article (the latter as cited in Revelle's CTA references).

**Model `[search/secondary]`.** A negative feedback loop compares a perceived state to a reference value and acts to reduce the discrepancy. A second, meta-level loop monitors the rate of discrepancy reduction; affect is its output: negative affect if progress is slower than needed, positive affect if faster than needed. Negative affect raises effort, positive allows effort to ease.

**Equations.** None in the original; verbal and diagrammatic. A numerical version (Carver & Scheier's) is `[standard account]` only: affect ∝ d(−discrepancy)/dt − expected rate.

**Combination.** Hierarchical (goals nested; higher-level goals set the references of lower ones) and meta-level (affect from the rate of change of the lower loop).

**Theorems.** None. Verbal predictions: affect depends on the first derivative of the discrepancy, which is a distinct claim from the other models (affect is not drive but its rate of reduction).

**Empirical standing.** Supported in some studies of affect and progress; the quantitative rate-affect link is less tested `[standard account]`.

**Translation.** Operands: a perceived state and a reference. Operator: compare, act, monitor rate. Affect as a derived quantity is useful for "fear, desire" as outputs rather than inputs.

---

## 9. Powers: perceptual control theory (PCT)

**Citation.** Powers, W. T. (1973). *Behavior: The Control of Perception*. Aldine. (Newer treatments: Powers 2005, Mansell, Marken.)

**Equations `[search/secondary]` (from an IAPCT PDF that cites the book).** The loop is linear. Perceptual signal p = input function of the input quantity qi. Error e = r − p (reference minus perception). Output o = G·e, with gain G. The environment feeds back: qi = qo + disturbance. At steady state, p ≈ r with error shrinking as gain increases. A hierarchy: the output of a higher-level control system sets the reference signals of lower ones, and the lower perceptions feed the higher perceptions (confirmed `[search/secondary]`).

**Combination.** Strict hierarchy: the only way a higher system acts is by setting a lower reference. No central drive variable. Behaviour is the means; the perception is the controlled quantity.

**Theorems / derived predictions.** The test for the controlled variable: apply disturbances to a hypothesised variable and check whether behaviour opposes them while the variable stays near its reference. The loop equations give stability conditions (gain, delay) `[standard account]`. Fits tracking data very closely in simple tasks (Marken, Powers) `[standard account]`.

**Empirical standing.** Excellent fits on continuous tracking tasks; limited reach into broader psychology; a small community outside mainstream. It supplies a mathematically stated alternative to drive: there is only error from a reference, and "motivation" is the reference value.

**Group relevance — collective control (checked 2026-10-29).** The literature exists and has a name. McClelland, K. (2004). The collective control of perceptions: constructing order from conflict. *International Journal of Human-Computer Studies* 60(1), 65-99, doi:10.1016/j.ijhcs.2003.08.003 (Crossref confirmed; text not read). Also McClelland & Fararo (eds., 2006), *Purpose, Meaning, and Action: Control Systems Theories in Sociology*, Palgrave, with McClelland's chapter "Understanding collective control processes" (doi:10.1007/978-1-137-10809-8_2). McClelland's 1993 "Conflictive Control" demonstration `[search/secondary, mmtaylor.net/PCT]`: two controllers controlling their perception of **one** environmental variable toward **different** references can escalate, yet the variable behaves as if held by a single **virtual controller** whose gain is the sum of the two gains and whose reference lies between the two.

The algebra behind that is short enough to state (derived here, checkable): with proportional outputs o_k = G_k(r_k − q) and q = o_1 + o_2 + d, the steady state is q = (G_1 r_1 + G_2 r_2 + d)/(1 + G_1 + G_2), i.e. a virtual reference equal to the **gain-weighted mean** of the references, with loop gain G_1 + G_2. With integrating outputs (dO_k/dt = G_k·e_k, Powers's usual form), both errors cannot reach zero, so o_1 and o_2 ramp in opposite directions without bound: the escalation. This is the single strongest multi-agent result in the cluster and it is real mathematics.

**Translation.** Operands: perceptual variables, references, error. Operators: compare, output, set reference (down the hierarchy). A tidy compositional structure.

---

## 10. Gray (and Gray & McNaughton): reinforcement sensitivity theory

**Citations.** Gray, J. A. (1970s-80s) reinforcement sensitivity theory; Gray & McNaughton (2000). *The Neuropsychology of Anxiety*, 2nd ed. Oxford.

**Model `[search/secondary]`.** Three systems. Behavioural approach system (BAS): reward and approach, linked with impulsivity and extraversion. Fight-flight-freeze system (FFFS): all aversive stimuli, fear, withdrawal; named in the revision to include freezing. Behavioural inhibition system (BIS): resolves goal conflict (approach and avoidance engaged together), linked to anxiety, with vigilance and risk assessment. The revision removed the conditioned/unconditioned distinction, and separated fear (FFFS) from anxiety (BIS).

**Equations.** None. A qualitative neuropsychological model. Personality questionnaires (BIS/BAS scales, Carver & White 1994, *J. Pers. Soc. Psychol.* 67, 319-333, doi:10.1037/0022-3514.67.2.319, Crossref confirmed) are the measurement route.

**Combination.** Three parallel systems; BIS activates when BAS and FFFS conflict. It is Miller's conflict model re-expressed as a physiological system.

**Theorems.** None.

**Empirical standing.** Large literature of questionnaire correlations; FFFS/BIS separation in questionnaires is contested `[standard account]`.

**Translation.** Operands: three drive-system activations of an agent. Operator: conflict between two activates the third. This is a good taxonomy for "fear, desire, anxiety" as named basic states.

---

## 11. Higgins: regulatory focus

**Citation.** Higgins, E. T. (1997). Beyond pleasure and pain. *American Psychologist* 52(12), 1280-1300, doi:10.1037/0003-066X.52.12.1280 (Crossref confirmed; not read).

**Model.** Promotion focus (ideals, advancement, gains and non-gains, eagerness strategies) versus prevention focus (oughts, security, losses and non-losses, vigilance strategies). Regulatory fit: a strategy matching focus strengthens engagement and persuasion.

**Equations.** None. Value from fit is described as "feeling right", with no formula; fit is a binary matching `[standard account]`.

**Combination.** Two orthogonal chronic or situational dispositions that select strategy.

**Theorems.** None.

**Empirical standing.** Large experimental literature, effect sizes small to moderate, with a replication concern for regulatory-fit effects `[standard account]`.

**Translation.** Operand: an agent with a focus parameter. Operator: fit between focus and strategy.

---

## 12. Prospect theory's value function as a fear-of-loss law

**Citation.** Kahneman & Tversky (1979). Prospect theory: an analysis of decision under risk. *Econometrica* 47(2), 263-291, doi:10.2307/1914185; Tversky & Kahneman (1992). Advances in prospect theory: cumulative representation of uncertainty. *Journal of Risk and Uncertainty* 5, 297-323, doi:10.1007/BF00122574 (both Crossref confirmed). Parameter values `[search/secondary]`; the 1992 PDF URL below now serves an HTML page, not the paper, so not read. The values are the ones universally cited from the 1992 paper, and are the median estimates from its sample, not population constants.

**Equation.** v(x) = x^α for x ≥ 0; v(x) = −λ(−x)^β for x < 0. Estimates α = β = 0.88, λ = 2.25. Probability weighting w(p) with γ = 0.61 for gains and δ = 0.69 for losses (confirmed by calculator pages `[search/secondary]`).

**Combination.** Reference-dependent, asymmetric: losses weigh about 2.25× gains. Overall value = Σ w(p_i) v(x_i).

**Theorems.** Derived: risk aversion in gains (α < 1), risk seeking in losses (β < 1), loss aversion at the reference. The cumulative form satisfies stochastic dominance (an axiomatic result, the paper's selling point `[standard account]`).

**Empirical standing.** One of the best-replicated findings in behavioural decision-making, although the size of λ varies by context (and loss aversion is contested in small stakes) `[standard account]`.

**Translation.** This is not a drive model, but its asymmetry is the cleanest quantitative statement of "avoidance is stronger than approach", the same direction as Miller's steeper gradient. Operand: a prospect relative to a reference. Operator: value, weight.

---

## 13. Homeostatic reinforcement learning (Keramati & Gutkin)

**Citation.** Keramati, M. & Gutkin, B. (2014). Homeostatic reinforcement learning for integrating reward collection and physiological stability. *eLife* 3:e04811. https://elifesciences.org/articles/04811 (PMC4270100). Precursor: NeurIPS 2011.

**Equations `[read]`** — re-read 2026-10-29 from the eLife JATS XML (cdn.elifesciences.org/articles/04811/elife-04811-v1.xml), where the MathML is unambiguous, including the Materials and methods proof.
- Drive (Eq. 1): **D(H_t) = ( Σ_{i=1}^{N} |h*_i − h_{i,t}|^n )^{1/m}** — an m-th root (MathML `mroot` with index m) of the sum of n-th powers. **Corrected:** the survey's "(…)^(m/n)" was wrong. H_t is the physiological state vector, H* the setpoint. The paper says "n > m > 1" is what lets it reproduce its four behavioural phenomena (dose increases reward; deprivation increases reward; irrelevant drives inhibit reward; risk aversion). The paper also says m = n = 1 "reduces to Euclidian distance"; that is the paper's slip — m = n = 1 is the L1 (city-block) distance, and Euclidean is m = n = 2. The paper also identifies drive with surprise, D(H_t) = −ln p(H_t), which is the bridge to active inference (§14).
- Reward (Eq. 2): r(H_t, K_t) = D(H_t) − D(H_{t+1}) = D(H_t) − D(H_t + K_t), with H_{t+1} = H_t + K_t. A sensory-estimate version replaces K_t by K̂_t.
- Discounted sums (Eqs. 3-4): SDD_π(H_0) = ∫ γ^t D(H_t) dt and SDR_π(H_0) = ∫ γ^t r_t dt; discrete forms (S1-S2) SDD = Σ_{t=0}^{w−1} γ^t D(H_{t+1}), SDR = Σ_{t=0}^{w−1} γ^t (D(H_t) − D(H_{t+1})).
- Result (Eq. 5 / Proposition S3): for γ < 1, argmin_π SDD = argmax_π SDR. Proof by telescoping: SDR = D_0 + (γ − 1)·SDD, and γ − 1 < 0 with D_0 fixed. **Condition the survey omitted:** the proof ranges over trajectories in P(H_0) that **end at the setpoint** (D at the final step = D* = 0). For γ = 1 the telescoping gives SDR = D_0 − D_final, independent of the path, so reward-seeking no longer favours stability.
- Hyper-palatability (Eq. 11): r = D(H_t) − D(H_t + K_t) + T, with T > 0 a drive-independent bonus; for the quadratic case it is equivalent to shifting the setpoint up by T/(2K_t), predicting a raised steady state (overeating).

**Combination.** Distance to a setpoint across several physiological dimensions, scalar drive; the policy maximises reduction of drive over time.

**Theorems.** This is the only theorem actually read in the cluster: for discounted return over setpoint-reaching trajectories, reward-seeking is equivalent to minimising discounted deviation from the setpoint. Further claims `[read]`: discounting "motivates animals to follow the shortest path in the space of physiological variables toward the desired setpoint" (a rationale for temporal discounting); anticipatory responding (ethanol-hypothermia tolerance); the rise-fall of responding in oral vs intragastric water delivery; overeating of hyperpalatable food.

**Empirical standing `[read]`.** The paper **reproduces qualitative patterns by simulation**; it does not fit parameters to data. A reviewer in the published decision letter asked that parameters fitted to one dataset be shown to reproduce another and questioned falsifiability. **Scope limit stated by the authors, important for this strand:** the theory "only applies to rewards that have a corresponding regulatory system"; extending it to "social rewards, novelty-induced reward, etc." is left as "a key challenge for the future". So curiosity and social drives are explicitly outside it. Precursor: Keramati & Gutkin (2011), NeurIPS 24, pp. 82-90 (confirmed). It is a formal rehabilitation of Hull: reward as drive reduction, now with a defined drive function and optimal control.

**Translation.** Operand: a physiological state vector with setpoints. Operators: outcome K (adds a vector), policy. Drives are the distance, one agent, no other agents.

---

## 14. Active inference and the free-energy principle

**Citations.** Friston, K., Rigoli, F., Ognibene, D., Mathys, C., FitzGerald, T. & Pezzulo, G. (2015). Active inference and epistemic value. *Cognitive Neuroscience* 6(4), 187-214, doi:10.1080/17588928.2015.1020053. Friston, Lin, Frith, Pezzulo, Hobson & Ondobaka (2017). Active inference, curiosity and insight. *Neural Computation* 29, 2633-2683, doi:10.1162/neco_a_00999. (Both Crossref confirmed.) Parr, T., Pezzulo, G. & Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press, open access (existence certain; not read). Parr & Friston (2019), generalised free energy `[search/secondary]`. Equations below read in Smith, Friston & Whyte (2022), "A step-by-step tutorial on active inference and its application to empirical data", *J. Math. Psychol.* (PMC8956124).

**Equations `[read]`** (Smith, Friston & Whyte 2022, Eqs. 12-13 and Table 2, via a summarising fetch). Two equivalent decompositions of the expected free energy of a policy:
- Epistemic + pragmatic: **G_π = −E_{q(o,s|π)}[ln q(s|o,π) − ln q(s|π)] − E_{q(o|π)}[ln p(o|C)]**. The first term is minus the **epistemic value** (expected information gain about hidden states, equal to an expected KL divergence between posterior and prior over s); the second is minus the **pragmatic value** (expected log-preference over outcomes, with preferences C encoded as a prior p(o|C)). So G(π) = −(epistemic value) − (pragmatic value), as the brief stated.
- Risk + ambiguity: **G_π = D_KL[q(o|π) ‖ p(o|C)] + E_{q(s|π)}[H[p(o|s)]]** — risk (divergence of predicted from preferred outcomes) plus ambiguity (expected entropy of the likelihood).
- Policy selection: prior π_0 = σ(ln E − γG), posterior π = σ(ln E − F − γG), with σ softmax, E a habit prior over policies, F variational free energy, γ a precision.
The survey's original form was right in substance; it is now tagged as read. Curiosity is the epistemic term; once uncertainty is resolved, it vanishes and pragmatic value dominates.

**Combination.** Additive terms inside a single objective. Curiosity and goal-seeking are not separate drives; they are two terms of one quantity, and the balance shifts with uncertainty.

**Theorems / derived predictions.** Epistemic exploration precedes exploitation as uncertainty resolves. Beyond that, the framework is a mathematical principle with proofs in the variational literature (existence of free-energy bound, etc. `[standard account]`), not a testable set of psychological theorems.

**Empirical standing.** Contested. The mathematics is respected; the claim that it is a falsifiable theory of brain and behaviour is disputed (it is often called unfalsifiable as a principle, but specific process models are tested) `[standard account]`. Simulations reproduce exploration, information seeking and some foraging behaviour.

**Group relevance (checked 2026-10-29; existence confirmed via Crossref, texts not read).** A real and growing multi-agent literature:
- Friston, K. & Frith, C. (2015). A duet for one. *Consciousness and Cognition* 36, 390-405, doi:10.1016/j.concog.2014.12.003 — two songbirds with shared generative models reach generalised synchrony; communication as mutual prediction.
- Friston, K. & Frith, C. (2015). Active inference, communication and hermeneutics. *Cortex* 68, 129-143, doi:10.1016/j.cortex.2015.03.025.
- Veissière, Constant, Ramstead, Friston & Kirmayer (2020). Thinking through other minds: a variational approach to cognition and culture. *Behavioral and Brain Sciences* 43, e90, doi:10.1017/S0140525X19001213.
- Kaufmann, R., Gupta, P. & Taylor, J. (2021). An active inference model of collective intelligence. *Entropy* 23(7), 830, doi:10.3390/e23070830 — agent-based model; adding theory of mind and goal alignment improves collective performance.
- Albarracin, M., Demekas, D., Ramstead, M. & Heins, C. (2022). Epistemic communities under active inference. *Entropy* 24(4), 476, doi:10.3390/e24040476 — opinion/echo-chamber dynamics from agents sampling each other.
- Heins, C., Millidge, B., Da Costa, L., Mann, R., Friston, K. & Couzin, I. (2024). Collective behavior from surprise minimization. *PNAS* 121, e2320239121, doi:10.1073/pnas.2320239121 — flocking/schooling from individual EFE minimisation.
- Friston, K., Parr, T., Heins, C., Constant, A. et al. (2024). Federated inference and belief sharing. *Neurosci. Biobehav. Rev.* 156, 105500, doi:10.1016/j.neubiorev.2023.105500.
The one-line glosses are `[standard account]`. It is the framework in the cluster with the most developed route from one agent to several, because each agent's observations include others' actions. Whether any of these defines a group-level preference (drive) that is not reducible to members' preferences was not checked; Veissière et al. and the federated-inference paper are the places to look.

**Translation.** Operands: beliefs (generative model), preferences C (priors over outcomes), policies. Operators: infer, act, expected-free-energy evaluation. Preference C is the "drive": what an agent expects to experience.

---

## 15. Allostasis (Sterling)

**Citation.** Sterling, P. (2012). Allostasis: a model of predictive regulation. *Physiology & Behavior* 106(1), 5-15, doi:10.1016/j.physbeh.2011.06.004 (Crossref confirmed). Earlier: Sterling & Eyer (1988) `[standard account]`.

**Model.** Regulation aims at what the organism will need, not at a fixed set point; the brain predicts and prepares, rather than correcting after the fact. Setpoints vary with context.

**Equations.** None in the cited paper `[search/secondary]` (abstract-level reading only). A formal bridge to active inference exists (the "allostatic regulation" entries in active-inference knowledge bases `[search/secondary]`).

**Combination.** A moving setpoint, set by prediction.

**Theorems.** None.

**Standing.** Widely used in physiology and stress research; as a mathematical object it needs the active-inference or HRL framing to become one.

**Translation.** Where Keramati's H* is fixed, allostasis lets H* be a function of expected context. This matters for a social algebra: other people change what the organism expects to need.

---

## 16. Toates: incentive motivation

**Citation.** Toates, F. (1986). *Motivational Systems*. Cambridge University Press (publisher listing found `[search/secondary]`; the content on incentive motivation was not seen). Related: Toates 1994 chapter and an "incentive motivation processes" reply in the Open University repository.

**Model `[standard account]`.** Motivation = interaction of internal state (deprivation, hormones) and external incentive: behaviour depends on both, in a multiplicative or otherwise interactive way; the incentive value of a stimulus is modulated by internal state (alliesthesia; Cabanac). Toates draws control-system diagrams with a positive-feedback loop for incentive (appetite builds as a cue approaches).

**Equations.** Some mathematical modelling occurs in the book (the catalogue says it covers "mathematical modelling" `[search/secondary]`); I have no equation from it.

**Combination.** State × incentive interaction; positive feedback.

**Standing.** Foundation of later incentive-salience work (Berridge's wanting/liking) `[standard account]`.

**Translation.** The cleanest account of why the same object has different pull depending on state. Operator: state-dependent valuation of an object.

---

## Unconfirmed

Updated 2026-10-29 by the validation pass; resolved items removed.

- Hull 1943/1952 and Spence 1956 primaries: the layered form above is consistent across secondaries but neither book was read.
- Atkinson & Birch (1970) book itself: equations are as Revelle restates them, not from the book.
- Lewin's force formula (Lewin 1938) and the vector-sum rule (standard accounts only).
- Carver & Scheier: any numerical affect formula (the rate-of-progress claim is verbal in the sources seen).
- Parr, Pezzulo & Friston 2022 chapter-level content (EFE equations were read in Smith, Friston & Whyte 2022 instead).
- Tversky & Kahneman (1992) parameter table: values are the universally cited ones, but the PDF was not read.
- McClelland (2004) text; the virtual-controller result is from a description of his 1993 demo plus the derivation given in §9.
- Content of the multi-agent active-inference papers (existence confirmed; glosses from standard accounts).
- Miller's 1944/1959 assumption list (standard account; Brown 1948 confirmed as the drive-height test by title only).
- Effect sizes and replication statements (marked `[standard account]`).

---

## What exists vs what does not

**Exists.**
1. Multiplicative drive laws (Hull, Atkinson, Vroom) with algebraic corollaries, e.g. the Ps = 0.5 peak.
2. A signed composition of two opposed drives with a computable equilibrium and conflict taxonomy (Lewin, Miller). This is the best template for composing "desire" and "fear".
3. Drives as state variables with dynamics and competition (Atkinson-Birch), under-used and the most mature formal drive-dynamics model.
4. A proved theorem linking reward to drive reduction (Keramati-Gutkin), and an information-seeking term that makes curiosity formal (active inference).
5. Hierarchical negative feedback with an exact loop equation (Powers).
6. A reference-dependent asymmetry between loss and gain with measured constants (prospect theory).

**Does not exist.**
1. **A multi-agent version validated on people.** Corrected 2026-10-29: multi-agent versions do exist for three models — PCT collective control (McClelland 2004; the virtual-controller result), active inference (Friston & Frith 2015 through Heins et al. 2024), and CTA (Revelle's four-person conversation, which failed its one test against Antill 1974). Hull, Lorenz, Tinbergen, Miller, Atkinson, Vroom, Carver-Scheier, Gray, Higgins, prospect theory, Keramati and Sterling are single-agent; Keramati & Gutkin explicitly exclude social rewards from their theory's scope. Lewin states groups verbally.
2. **A composition law for drives that is closed.** Every model has its own combination rule (product, signed sum, competition, hierarchy), and no one has asked whether they form one algebra. The rules are not interoperable.
3. **A drive inventory.** The models treat "drive" as generic (D), or pick one (hunger, achievement). Curiosity, fear and desire appear as words (Gray's FFFS and BAS, the epistemic term in active inference, Lewin's valence), never as members of a closed set with defined interactions. No consensus list of basic human drives exists in these formalisms.
4. **Group-level drives.** Nothing here has a drive that belongs to a group and is not the sum of members' drives.
5. **Theorems in the mathematical sense.** The real ones are: Keramati's equivalence (for γ < 1, over setpoint-reaching trajectories), the Atkinson peak, Miller's crossing point, the two-controller virtual-reference result in PCT, and variational bounds in active inference. Hull's "theorems" were deductions from postulates, not proofs.
6. **Control or prediction of social behaviour.** None of these has been validated on interacting people with these equations (the one attempt found, Revelle's CTA conversation model, did not match the data).

**Reading for the strand.** The nearest materials for building drives into the algebra are: the Lewin-Miller signed-gradient composition for pairwise conflict; the Atkinson-Birch/CTA dynamics for a vector of drives with competition and satiation (now stated exactly in §6, and already shown to stack across people); the Keramati-Gutkin form for drive as distance from setpoint (and as surprise); and the epistemic/pragmatic split for curiosity. The social extension (other people as sources of cues, valence and disturbance) is partly built already: McClelland's collective control and the multi-agent active-inference papers are the first things to read at source.

**Clearly missing from this survey (added by validation).**
- McFarland & Sibly (1975), "The behavioural final common path", *Phil. Trans. R. Soc. B* 270, 265-293, doi:10.1098/rstb.1975.0009, and Sibly & McFarland on state-space models of motivation: the ethological formal model of several drives as a state vector with decision boundaries, a direct ancestor of Keramati's H-space.
- Toates & Halliday (1980) and Toates (1975) dynamic control models of feeding/drinking (cited by Revelle as the other dynamic-motivation line).
- French (1956), "A formal theory of social power", *Psychological Review* 63, 181-194, doi:10.1037/h0046123 — Lewin's school's own formal multi-agent model (influence as averaging over a network), the precursor of DeGroot and Friedkin-Johnsen opinion dynamics; the nearest formal answer to "Lewin states groups verbally".
- Juechems & Summerfield (2019), "Where does value come from?", *Trends Cogn. Sci.* 23, 836-850, doi:10.1016/j.tics.2019.07.012 — reward as progress toward homeostatic/goal setpoints, the modern review of the Keramati line.
- Computational curiosity outside active inference: Berlyne (1960); Loewenstein (1994) information-gap theory; Schmidhuber's compression-progress and Oudeyer & Kaplan's learning-progress intrinsic motivation. Not checked here; flagged as a gap for the curiosity drive specifically.

Source URLs found: https://elifesciences.org/articles/04811, https://pmc.ncbi.nlm.nih.gov/articles/PMC4270100, https://www.personality-project.org/revelle/publications/cta.pdf, https://psych.fullerton.edu/mbirnbaum/psych466/articles/Tversky_Kahneman_JRU_92.pdf, https://leeds-faculty.colorado.edu/dahe7472/Higgins%20beyond%20pleasure%20and%20pain%201997.pdf, https://www.frontiersin.org/journals/systems-neuroscience/articles/10.3389/fnsys.2015.00038/full, https://en.wikipedia.org/wiki/Lewin%27s_equation, https://en.wikipedia.org/wiki/Approach-avoidance_conflict, https://www.cambridge.org/9780521318945, https://www.iapct.org/wp-content/uploads/2022/04/PCTunderstanding.pdf, https://www.personality-project.org/revelle/syllabi/301/achievement.pdf.

---

## Validation log (2026-10-29)

Key: ✓ confirmed / ✎ corrected / ? unconfirmed / ✗ removed.

- Hull 1943, 1952 — ✎ layered form stated (product sHr·D·V·K, minus Ir + sIr, minus oscillation sOr, against threshold sLr); the "disagreement" between orderings was not one. Primaries not read.
- Spence 1956 — ✎ additive D + K confirmed (secondary); "could not settle it" removed.
- Lorenz / Tinbergen 1951 — ✓ as described (no equations); not re-checked in depth.
- Miller 1944, 1959; Dollard & Miller 1950 — ✎ assumption list added; prediction (3) "reducing fear moves the crossing point more" was false for the linear model and is rewritten as a claim about fear at equilibrium; oscillation stated.
- Brown 1948 — ✓ Crossref (doi:10.1037/h0055463).
- Miller & Murray 1952 — ✓ Crossref, full citation added.
- Boyd, Robinson & Fetterman 2011 — ✓ (secondary), citation completed.
- Lewin 1936/1951 — ✓ B = f(P,E); ? force formula, source (Lewin 1938) named.
- Atkinson 1957 — ✓ Crossref; ✎ resultant (Ms − Maf)Ps(1 − Ps) is 1957, not 1964; equations now [read] via Revelle; empirical peak at Ps ≈ 0.3-0.4, not 0.5; Raynor extension added.
- Atkinson & Birch 1970 / Revelle CTA — ✎ equations supplied [read]: dT = F − cT (ongoing), dN = I − rN, T_r = T − N, max-selection rule; CTA dT = sC − cA, dA = eT − iA; printed asymptotes re-derived; ✎ multi-agent (four-person) application found.
- Revelle & Condon 2015 — ✓ Crossref; "used it in simulation" softened to "builds on it".
- Vroom 1964, Eccles 1983 — ✓ existence (standard); not re-checked.
- Carver & Scheier — ✎ 1981 book vs 1982 Psych. Bull. article resolved; 1990 Psych. Rev. ✓ Crossref.
- Powers 1973 — ✓ loop equations (secondary, unchanged); ✎ collective control now cited (McClelland 2004 ✓ Crossref; McClelland & Fararo 2006 chapter ✓) with virtual-controller result and derivation.
- Gray; Gray & McNaughton 2000 — ✓ (standard); Carver & White 1994 ✓ Crossref.
- Higgins 1997 — ✓ Crossref.
- Kahneman & Tversky 1979, Tversky & Kahneman 1992 — ✓ Crossref; parameters (α = β = 0.88, λ = 2.25, γ = 0.61, δ = 0.69) ? not read at source, but the standard values; noted as sample medians.
- Keramati & Gutkin 2014 — ✎ drive exponent was wrong: D = (Σ|h* − h|^n)^{1/m}, not ^{m/n}; n > m > 1 added; paper's "Euclidean at m = n = 1" flagged as the paper's slip; proof's setpoint-reaching condition added; "fitted to rodent data" corrected to qualitative simulation; authors' exclusion of social and novelty rewards added.
- Keramati & Gutkin 2011 (NeurIPS) — ✓.
- Friston et al. 2015 (epistemic value), Friston et al. 2017 — ✓ Crossref.
- Parr, Pezzulo & Friston 2022 — ✓ existence; EFE equations ✎ now [read] from Smith, Friston & Whyte 2022 (both decompositions and the policy softmax).
- Friston & Frith 2015 ("A duet for one") — ✓ Crossref; plus Cortex 2015, Veissière et al. 2020, Kaufmann et al. 2021, Albarracin et al. 2022, Heins et al. 2024, Friston et al. 2024 all ✓ Crossref (texts not read).
- Sterling 2012 — ✓ Crossref.
- Toates 1986 — ✓ existence (publisher listing); content ? unchanged.
- Closing verdict — ✎ "no multi-agent version" was wrong for PCT, active inference and CTA; narrowed to "no group-level drive, no multi-agent result validated on people". Missing work listed (McFarland & Sibly, French 1956, Juechems & Summerfield, computational curiosity).
- Fabrications found — none. ✗ nothing removed.

**Verdict.** The survey is honest about its sourcing, and none of its citations was invented; every DOI checked resolved to the work named. Its equations were right in shape but wrong in two places that matter for building on them (the Keramati drive exponent and a false Miller corollary), and its central finding overstated the multi-agent gap, which was the claim most likely to steer the strand. Treat the equations now tagged [read] as usable; treat everything tagged [standard account] as a pointer to a primary, not a foundation.
