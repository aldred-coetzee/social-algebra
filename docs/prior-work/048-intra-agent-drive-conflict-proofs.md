# Prior work 048: formal models of conflict between drives inside one agent, with proved equilibrium or switching results

Direction: D085

Date: 2026-10-29. Survey for the social-algebra strand. Question: which formal models of conflict between drives inside one agent come with *proved* equilibrium, bifurcation or switching results, as opposed to simulation? Context: Aldred's aim of "an algebra which expresses basic human drives and group drives, which we can compose into equations, which we can then use to start making theorems".

**Method and honesty note.** Read at source this session (PDF downloaded and text-extracted, so equations are transcribed, not paraphrased from a summary): Reverdy & Koditschek, arXiv:1703.01662v2 (model, Definition 1, Theorems 2 and 3, proof of Theorem 2 outlined); Pais et al. 2013 (White Rose copy; model description, bifurcation statements, not the supplementary proofs); Bogacz et al. 2006 (Eqs 14, 18, 21, 22 and the balance statement). Read at abstract level only: Hughes et al. 2018 (arXiv abstract), Rabinovich et al. 2001, the Arizona 2019 seminar abstract, Thompson & Reverdy arXiv:2109.13408 (search summary; the PDF fetch returned compressed bytes). Gul-Pesendorfer and Fudenberg-Levine are tagged [standard account]; their deep-reads are D094 and D095, not here. DOIs checked against Crossref where given.

**Headline: the two seeds do not fit the question.** Hughes et al. 2018 and Helbing, Farkas & Vicsek 2000 are not models of conflict between drives inside one agent with proved results. Hughes is a multi-agent reinforcement-learning paper whose inequity-averse reward is a Fehr-Schmidt-type shaping term, with empirical results on gridworld benchmarks and no theorem; Helbing 2000 is a simulation paper whose single "panic" parameter mixes two forces (file 23 section 3, "none provable"). Neither is the right anchor. The real answer to the question is a small cluster: **the Reverdy-Koditschek motivation dynamics (the only drive-labelled model here with stated theorems), the Seeley/Pais honeybee-derived decision dynamics it borrows, and the Usher-McClelland/Bogacz competing-accumulator reduction**. Everything else with a proof is in economics (axiomatic representation theorems, files 36 and D094-D096), where the proof is about preference representation, not state dynamics.

---

## 1. Reverdy & Koditschek: a dynamical system for prioritizing and coordinating motivations

**Citation.** Reverdy, P. & Koditschek, D. E., "A dynamical system for prioritizing and coordinating motivations", arXiv:1703.01662v2 [math.DS], 8 Mar 2018. https://arxiv.org/abs/1703.01662 [read]. Journal successor: Reverdy, P., Vasilopoulos, V. & Koditschek, D. E., "Motivation dynamics for autonomous composition of navigation tasks", *IEEE Trans. Robotics* 37(4), 1239-1251, 2021 [citation from search results (Arizona, UPenn, MIT CSAIL pages); the DOI was not confirmed by Crossref; not read]. The arXiv paper cites the journal paper as "in preparation".

**Their vocabulary.** Task, motivation state, value (urgency), drive (psychology sense: "the animal can be said to have drives which motivate it to perform actions that reduce those drives"), deadlock, undecided motivation, stop signal, limit cycle, Hopf bifurcation, relaxation oscillation.

**Drives/operands [read].** Agent position x in D (a domain in R^d); motivation m in the N-simplex Delta_N = {m in R^(N+1): m_i >= 0, sum m_i = 1}, with m_i the motivation to perform task i and m_U the "undecided" motivation (no task); value v_i in R+ per task, "its current urgency". Each task i has a goal x*_i and a distance function phi_i(x) = (1/2)||x - x*_i||^2 (Eq. 1). The paper explicitly relates v-dynamics to "drive reduction theory", so v_i is the drive level and m the competition state among drives.

**Operators / equations [read].** State (x, m, v), with x' = f_x(x,m), m' = f_m(m,v), v' = f_v(v,x) (Eqs 3-5).
- Navigation (Eq. 6): x' = -Phi(x) m, with Phi(x) = [F_1(x) ... F_N(x) 0], F_i = -grad phi_i. So the action is the m-weighted convex combination of the task vector fields.
- Motivation (Eq. 7), from Pais et al. 2013: m_i' = v~_i m_U - m_i ( 1/v~_i - v~_i m_U + sigma_i (1 - m_i - m_U) ), with v~_i = v*_i v_i, v*_i > 0 a gain, sigma_i > 0 the stop-signal (cross-inhibition) strength. Term reading given in the paper: v~_i m_U spontaneous commitment, -m_i / v~_i abandonment, v~_i m_i m_U recruitment, -sigma_i m_i (1 - m_i - m_U) the stop signal from options other than i.
- Value (Eq. 8): v_i' = lambda_i ( phi_i(x) - v_i ), so the urgency of a task rises with distance from its goal and relaxes toward it with timescale 1/lambda.
- Two-task symmetric instance (Eq. 9, N=2, goals (1,0) and (-1,0), sigma_1=sigma_2=sigma, v*_1=v*_2=v*, lambda_1=lambda_2=lambda): x' = -m_1(x - x*_1) - m_2(x - x*_2); m_1' = (v*v_1) m_U - m_1( 1/(v*v_1) - (v*v_1) m_U + sigma m_2 ); m_2' symmetric with m_1; v_i' = lambda(phi_i - v_i). Mean-difference coordinates Delta m = m_1 - m_2, mbar = (m_1+m_2)/2, Delta v = v_1 - v_2, vbar (Eq. 10), with epsilon_v = 1/v*, epsilon_lambda = 1/lambda (Eqs 11-17). The system has S_2 symmetry (task interchange) when the two values are equal, "no inherent bias for either underlying task".
- **Definition 1 (symmetric deadlock equilibrium)**: an equilibrium of Eq. 9 of the form (x_1d, x_2d, m_d, m_d, v_d, v_d); exists if there is a point x_d with phi_1(x_d) = phi_2(x_d).

**Theorems [read, statements; Theorem 2 proof outline read].**
- **Theorem 2.** In the limit lambda -> 0 (values slaved to distances, v = phi(x)) the reduced system has a deadlock equilibrium; **for sigma > 6 the dynamics undergo a Hopf bifurcation resulting in stable periodic solutions** at (deadlock equilibrium, epsilon_v,0), where epsilon_v,0 is the unique solution in [0, 1/2] of 4(2 - sigma)^2 eps^2 - 4(2 - sigma) eps + (6 - sigma) = 0. For sigma = 8, epsilon_v,0 = (3 - sqrt 6)/6, about 0.09175. Proof uses the standard Hopf theorem (Lemma 6: Jacobian has a simple pure-imaginary pair; Lemma 7: d Re(lambda)/d eps < 0; Lemma 8: first Lyapunov coefficient negative, so the bifurcation is supercritical).
- **Theorem 3.** "Accepting Conjecture 20, below, for sigma > 6, there exists a stable limit cycle of (11) for sufficiently small, but finite, values of epsilon_lambda and epsilon_v. Equivalently, fixing lambda, there exists a stable limit cycle ... for sufficiently large, but finite, values of v*." Proof by singular perturbation and Poincare-Bendixson on a reduced planar system, then geometric singular perturbation theory.
- Supporting lemmas 13-17: Lyapunov argument that x_2 -> 0 and x_1 enters [-1, 1].
- The Fig. 1 caption labels a region "Theorem 1"; no Theorem 1 statement was found in the extracted text, so treat that label as an artifact of the preprint.

**What is conditional or only numerical.** Theorem 3 rests on **Conjecture 20**, the hyperbolicity of the limit cycle of the layer/reduced problem, which the authors call "numerically corroborated", not proved. The curve epsilon_v*(lambda) for lambda > 0 (Fig. 1) is numerical. The "basin of attraction is quite large" is numerical. The asymmetric case (sigma_1 != sigma_2, lambda_1 != lambda_2) is "numerical experimentation suggests" persistence, unproved. The link between the pitchfork of the motivation subsystem and the Hopf of the closed loop is stated as future work.

**Empirical standing (blunt).** None as psychology. This is robot control. The word "drive" is borrowed from drive-reduction theory (Hull; file 16 sections 1 and 7), and the paper's cited psychology is a textbook (Petri & Govern). No human or animal data constrain sigma, v*, lambda. The value-follows-distance law (Eq. 8) is Hull-style drive reduction, whose psychological record is poor (file 16 section 1). The honeybee mechanism it builds on is empirical in swarms (Seeley et al. 2012), but that is a group of bees, not one mind.

**Operand/operator translation for the algebra.** Operands: agent state (position, motivation simplex point, urgency vector). Operator: the vector-field map "m-weighted convex combination of per-drive policy fields" is a clean composition rule, and the value/motivation subsystem is a closed template for **drive competition with a built-in undecided state**. The proved content is a *regime statement*: two drives of equal urgency at a point equidistant from both goals can deadlock; with strong enough cross-inhibition (sigma > 6) and fast enough feedback the agent instead alternates (a stable cycle between serving drive 1 and drive 2). That is the nearest thing in the literature to a theorem of the form "two drives in conflict produce periodic switching, not a fixed compromise".

---

## 2. Pais et al. 2013 and Seeley et al. 2012: stop-signal cross-inhibition, deadlock and value-sensitivity

**Citations.** Pais, D., Hogan, P. M., Schlegel, T., Franks, N. R., Leonard, N. E. & Marshall, J. A. R. (2013). A mechanism for value-sensitive decision-making. *PLoS ONE* 8(9): e73216. DOI 10.1371/journal.pone.0073216 [Crossref confirmed]; PMC3759446. Seeley, T. D., Visscher, P. K., Schlegel, T., Hogan, P. M., Franks, N. R. & Marshall, J. A. R. (2012). Stop signals provide cross inhibition in collective decision-making by honeybee swarms. *Science* 335, 108-111. DOI 10.1126/science.1210361 [Crossref confirmed; not read].

**Their vocabulary.** Commitment, abandonment, recruitment, cross-inhibition (stop signal), deadlock, value-sensitive, pitchfork, saddle-node, cusp catastrophe, hysteresis.

**Operands.** Fractions of a population committed to alternative A, to B, and undecided (y_A, y_B, y_U); alternative values v_A, v_B; Delta v = v_A - v_B; mean value vbar. Reverdy-Koditschek reinterpret the same equations as one decision-maker's motivation simplex.

**Operators / equations.** The m_i' law of Eq. 7 above is this model (same structure) [read in the Reverdy-Koditschek transcription; the Pais paper's own Eq. 1 was not transcribed here].

**Derived results [read, at the level of the main-text statements; supplementary proofs not read].** (i) For equal alternatives (Delta v = 0) the dynamics exhibit a **pitchfork bifurcation as a function of cross-inhibition rate sigma**: below it, a single stable deadlock attractor with the two alternatives equal; above it, two stable attractors (one per alternative) and a saddle. (ii) For unequal alternatives and varying sigma, a **saddle-node bifurcation**; with both Delta v and sigma varied the bifurcation set is "qualitatively identical to the cusp catastrophe". (iii) The **minimum mean value above which deadlock is broken increases with cross-inhibition strength**: for two equally poor alternatives deadlock persists, for equally good alternatives a decision breaks symmetry (this is the "value-sensitivity"). (iv) **Hysteresis** in Delta v. (v) A Weber-law-like coefficient K controlled by sigma.

**Empirical standing.** Strong for honeybee swarms qualitatively (Seeley et al. 2012 showed that stop signals avoid deadlock in nest-site choice); the mapping to a *single* mind is an analogy asserted by Reverdy-Koditschek, not tested.

**Translation.** Operand: a probability/proportion vector over "active drive i" plus "none". Operator: pairwise cross-inhibition with strength sigma. The proved structure (pitchfork -> cusp) is the exact algebra of "when does conflict between two equal drives resolve into one winning versus stay stuck", with a bifurcation parameter that can be named (inhibition strength) and a value-sensitivity law (the threshold depends on absolute urgency, not just difference).

---

## 3. Competing accumulators: Usher & McClelland 2001; Bogacz et al. 2006

**Citations.** Usher, M. & McClelland, J. L. (2001). The time course of perceptual choice: the leaky, competing accumulator model. *Psychological Review* 108(3), 550-592. DOI 10.1037/0033-295X.108.3.550 [Crossref confirmed; not read]. Bogacz, R., Brown, E., Moehlis, J., Holmes, P. & Cohen, J. D. (2006). The physics of optimal decision making: a formal analysis of models of performance in two-alternative forced-choice tasks. *Psychological Review* 113(4), 700-765. DOI 10.1037/0033-295X.113.4.700 [Crossref confirmed]; PMID 17014301; PDF at sites.engineering.ucsb.edu/~moehlis/moehlis_papers/psych.pdf [read, relevant sections].

**Their vocabulary.** Decay (leak) k, mutual inhibition w, input I_i, decision units, balanced, decision line, drift-diffusion model.

**Operands.** Activities y_1, y_2 of two decision units (competing "option strengths"), inputs I_1, I_2.

**Operators / equations [read].** Linearised mutual-inhibition model (Eq. 14): dy_1 = (-k y_1 - w y_2 + I_1) dt + c dW_1; dy_2 = (-k y_2 - w y_1 + I_2) dt + c dW_2; y_1(0) = y_2(0) = 0. Rotated coordinates (Eq. 18): x_1 = (y_1 - y_2)/sqrt 2, x_2 = (y_1 + y_2)/sqrt 2. Decoupled Ornstein-Uhlenbeck processes (Eqs 21-22): dx_1 = ( (w - k) x_1 + (I_1 - I_2)/sqrt 2 ) dt + c dW_1'; dx_2 = ( (-k - w) x_2 + (I_1 + I_2)/sqrt 2 ) dt + c dW_2'.

**Theorem-like results [read].** The x_2 process is always a stable O-U process (rate k + w, since -k - w < 0). The x_1 process is stable if k > w and **unstable (self-reinforcing) if w > k**, i.e. when inhibition exceeds decay the winner-takes-all runaway appears along the difference coordinate. When **decay equals inhibition (k = w, "balanced")** the term (w - k) x_1 vanishes and x_1 is a pure drift-diffusion process (the DDM); if k = w is also large relative to noise, the 2-D model approximates the DDM (only approximates, because of threshold effects in 2-D, the authors state). Bogacz et al.'s abstract (via PubMed snippet and search summary) states that five of six models analysed reduce to the DDM, which is optimal for a speed-accuracy trade-off; this is an analytic equivalence under stated parameter conditions.

**Empirical standing.** The DDM fits human and animal choice-time distributions widely (Ratcliff; D089, D090 are the places to take that further), but fit does not distinguish these models from one another; the paper itself says the six models are indistinguishable by their DDM reductions in some regimes. The mapping to *drives* is the translation, not the authors' claim: the accumulators are perceptual evidence, not need states.

**Translation.** Operand: two drive activations y_1, y_2. The balanced condition k = w is a one-line law saying **a drive pair is a pure integrator of its urgency difference exactly when each drive's self-decay equals the other's inhibition of it**; w > k gives winner-take-all (a proved instability), k > w a compromise attractor. That is a two-parameter classification of drive-conflict regimes that is already proved, and it connects with the Miller conflict types in file 16 section 3 (approach-approach unstable, avoidance-avoidance stable).

---

## 4. Other candidates considered

- **Rabinovich et al. 2001, winnerless competition.** Rabinovich, M. I., Volkovskii, A., Lecanda, P., Huerta, R., Abarbanel, H. D. I. & Laurent, G. (2001). Dynamical encoding by networks of competing neuron groups: winnerless competition. *Phys. Rev. Lett.* 87, 068102. DOI 10.1103/PhysRevLett.87.068102 [Crossref confirmed]. From the abstract (fetched, [from abstract]): trajectories pass near heteroclinic connections between saddles, so information is carried by paths rather than stable states, with about e(N-1)! encodable patterns for N units. This is a candidate form for *sequential* switching between competing drives (the system never settles on one). The proof content, the heteroclinic-cycle conditions for generalised Lotka-Volterra systems, is standard in the dynamical-systems literature but was **not read here**; to be treated as a follow-up. [standard account / abstract]
- **Thompson & Reverdy, "Drive-based motivation for coordination of limit cycle behaviors"** (Arizona applied-math seminar, 27 Sept 2019; abstract read; and arXiv:2109.13408, "Multi-Agent Recurrent Rendezvous Using Drive-Based Motivation", 2021, abstract via search summary only). Extends the framework from point-attractor tasks to limit-cycle tasks: an attracting set of orbits flowing repeatedly between two Hopf-oscillator limit cycles arising from a bifurcation, with "general results for arbitrary disjoint limit cycles" announced; the multi-agent paper reports analytic bifurcation characterisation plus numerics "suggestive of a strange attractor". Not read at source. [from abstract]
- **Gul & Pesendorfer 2001, "Temptation and self-control", Econometrica 69, 1403-1435** (DOI 10.1111/1468-0262.00252, Crossref confirmed, title only). A representation theorem for preferences over menus with temptation: utility of a menu = max over its items of u(x) + v(x) minus max over the menu of v(y). Proved, but it is an axiomatic preference representation, not state dynamics; no equilibrium of a dynamical system and no switching dynamics. [standard account] Deep-read is D094/D095.
- **Fudenberg & Levine 2006, "A dual-self model of impulse control", AER 96(5), 1449-1476** (DOI 10.1257/aer.96.5.1449, Crossref confirmed; not read). The long-run self pays a cost to restrain a myopic short-run self, giving a game within one agent with an equilibrium; it is the main case of a proved *equilibrium* between two internal selves. [standard account] Deep-read is D094.
- **Miller 1944 / Dollard & Miller 1950 approach-avoidance gradients and Atkinson-Birch dynamics of action**: already treated in file 16 (sections 3 and Atkinson/Revelle) with stated corollaries (equilibrium at d* = (a - c)/(b - e); Atkinson's peak at P = 0.5). Not repeated.
- **Hughes et al. 2018** (the seed). Hughes, E., Leibo, J. Z., Phillips, M. G., Tuyls, K., Duenez-Guzman, E. A., Garcia Castaneda, A., Dunning, I., Zhu, T., McKee, K. R., Koster, R., Roff, H. & Graepel, T. (2018). Inequity aversion improves cooperation in intertemporal social dilemmas. NeurIPS 2018, arXiv:1803.08884 [abstract read]. Inequity aversion is a reward-shaping term inside each agent (Fehr-Schmidt form per file 23), the "conflict" being between own payoff and others' payoffs; the results are empirical across sequential-social-dilemma gridworlds. No theorem.
- **Helbing, Farkas & Vicsek 2000.** Nature 407, 487-490, DOI 10.1038/35035023 [Crossref confirmed]. Read at source in file 23: simulation; no proof. Not a conflict-between-drives model with a proof.

---

## 5. What exists versus what does not

**Exists (with a proof, or an exact analytic reduction):**
- Two competing "motivation" states with an explicit **undecided** state, a proved Hopf bifurcation (Theorem 2, sigma > 6; epsilon_v,0 = (3 - sqrt 6)/6 at sigma = 8, supercritical) and conditional existence of a stable switching cycle (Theorem 3, conditional on Conjecture 20). Single-agent, two drives, symmetric.
- A cross-inhibition model with an analytic pitchfork, saddle-node and cusp structure describing **when two equal drives stay deadlocked versus break symmetry**, and value-sensitivity (Pais et al.).
- An exact decoupling (O-U in difference and sum coordinates) giving **k = w as the integrator condition and w > k as winner-take-all runaway** (Bogacz et al.).
- Preference-representation theorems for temptation (Gul-Pesendorfer) and an equilibrium for the dual-self model (Fudenberg-Levine), with their economic-level validation not checked here.

**Does not exist (as far as found):**
- A proved result for conflict among **three or more** drives with unequal parameters; the Reverdy-Koditschek proofs need N = 2, symmetry, planar workspace and a specific distance function, and the asymmetric case is numerical.
- Any of these models with **parameters fitted to human data on named drives** (curiosity, fear, desire). sigma, v*, lambda, k, w have no empirical priors for human drives.
- A proved link from conflict inside one agent to **conflict between group-level drives**; every proof is for one agent or one swarm treated as one decision-maker.
- A drive-labelled model with **external stimuli** and proofs: Reverdy-Koditschek say responding to stimuli while keeping the cycle is future work.
- Theorems for the seeds: neither Hughes nor Helbing has any.

**Cross-references.** Miller/Atkinson and Keramati-Gutkin in 16; Fudenberg-Levine and Gul-Pesendorfer in 36 and D094/D095; accumulators and first passage in D089; the general question of which compositional-dynamics assumptions drive models violate (Lipschitz, passivity) in 40 and D030. The Reverdy-Koditschek vector field is Lipschitz and has a Lyapunov argument for x; that is a specific assumption check D030 can reuse.

## Unconfirmed

- DOI for Reverdy, Vasilopoulos & Koditschek, IEEE T-RO 37(4), 2021: not confirmed (a guessed DOI failed Crossref; do not use one). The paper itself was not read, so whether Theorems 2-3 are strengthened or Conjecture 20 proved there is unknown.
- Thompson & Reverdy (arXiv:2109.13408) and the 2019 IEEE conference paper: read only via search summaries; the claimed "general results" for arbitrary disjoint limit cycles are unverified.
- Pais et al. supplementary proofs (Text S1) and the paper's own Eq. 1 were not transcribed; the pitchfork/saddle-node statements above are from the main text.
- Usher & McClelland 2001 itself not read; its nonlinearity (threshold-linear activation) and its claim of fit were taken from Bogacz et al.'s description.
- Whether the Rabinovich winnerless-competition conditions (heteroclinic cycle, May-Leonard or generalised Lotka-Volterra) give a stated theorem for N competing drives was not checked.
- Gul-Pesendorfer 2001 representation and Fudenberg-Levine equilibrium statements are from background knowledge.
- Hughes 2018's exact inequity-aversion formulas were read in file 23, not re-read here.
