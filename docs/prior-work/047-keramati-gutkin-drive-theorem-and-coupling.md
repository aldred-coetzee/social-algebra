# Prior work 047: the Keramati-Gutkin drive function and theorem, the coupled-drive extension, and the active-inference framing

Direction: D082

Date: 2026-10-29. Kind: deep-read. Cross-references: file 16 (section on Keramati-Gutkin and the validation log), file 19 (sections 12 and 14), file 20 (dyadic coupling). Nothing in those files is repeated unless it is being corrected.

**Method and honesty note.** Tags: `[read]` = read at source this session; `[derived]` = my own algebra or numerics this session, not a published result; `[from abstract/standard account]` = not read at source.

Read at source:
- Keramati & Gutkin 2014 (eLife) in full from the JATS XML (`elife-04811-v1.xml` at github.com/elifesciences/elife-article-xml). Equations were taken from the MathML, not from a text extraction, so exponents and roots are exact.
- Keramati & Gutkin 2011 (NeurIPS) main text, from the proceedings PDF. Its supplement, which holds Propositions 1-3, was not accessed.
- Yoshida & Man 2024 (arXiv 2412.12103) in full, including the appendices.
- Juechems & Summerfield 2019, author-accepted manuscript from Oxford ORA, in full.
- Pezzulo, Rigoli & Friston 2015, PMC text, searched for drive and preference content. Equations did not survive text extraction, so a missing equation here means unconfirmed, not absent.
- Smith, Friston & Whyte 2022 (PMC), for the expected-free-energy form only.

Not read at source: Friston 2010, and Yoshida et al. 2025 (arXiv 2507.04998) and Yoshida & Man's follow-up (arXiv 2506.12894), both abstract only.

DOIs confirmed through Crossref: 10.7554/eLife.04811; 10.1016/j.tics.2019.07.012 (TICS 23(10):836-850); 10.1016/j.pneurobio.2015.09.001 (Prog Neurobiol 134:17-35); 10.1038/nrn2787 (Nat Rev Neurosci 11(2):127-138); 10.1016/j.jmp.2021.102632 (J Math Psychol 107, 2022).

**Summary.**
1. The drive function and the theorem are now fixed exactly (sections 1 and 2).
2. The theorem is a telescoping identity. It is true for any bounded drive function, and in the infinite-horizon case it does not even need a reachable setpoint (section 2). That is why it extends to a coupled drive D_self + w·D_partner.
3. The extension is clean only under conditions: a fixed w, a single shared potential, and terminal handling. The conditions are listed in section 4, and the cases where it fails are the interesting part for the algebra.
4. Three small errors in the eLife paper were found. The "Euclidean" statement is wrong, one printed inequality has the wrong sign, and one special-case label looks garbled (section 1).
5. In active inference, a drive is the negative log of a prior-preference density, and there is no drive-difference reward. K&G's theorem is the exact statement that a discounted potential-difference reward equals, up to an affine map, a discounted state cost (section 6).

---

## 1. Keramati & Gutkin: the drive function, exactly

**Citations.**
- Keramati, M. & Gutkin, B. (2014). Homeostatic reinforcement learning for integrating reward collection and physiological stability. *eLife* 3:e04811. doi:10.7554/eLife.04811.
- Keramati, M. & Gutkin, B. (2011). A reinforcement learning theory for homeostatic regulation. *Advances in Neural Information Processing Systems 24*, pp. 82-90. https://proceedings.neurips.cc/paper/2011/file/9778d5d219c5080b9a6a17bef029331c-Paper.pdf. I found no DOI for it and did not guess one.

**Their vocabulary.** Homeostatic space; physiological state H_t; setpoint H*; drive D(H_t); outcome K_t; sum of discounted drives (SDD) and sum of discounted rewards (SDR). Also "stepping back from the brink", the hyper-palatability term T, and orosensory approximation K̂.

**Drive/operands.** The state is a vector of N regulated variables H_t = (h_1,t, ..., h_N,t), and the setpoint is H* = (h*_1, ..., h*_N). Outcomes are vectors K_t, applied as H_{t+1} = H_t + K_t. There is one operand type, the internal state. An outcome is an additive operator on the state.

**Equations `[read]`** (eLife numbering).

- (1) **D(H_t) = ( Σ_{i=1..N} |h*_i − h_{i,t}|^n )^{1/m}**, with m and n free parameters.
  - The MathML is `mroot(Σ |.|^n, m)`, so the m-th root applies to the sum, and the 2011 paper has the same form: d(H_t) = ᵐ√(Σ|h*_i − h_i,t|ⁿ).
  - In one dimension this is D = |h* − h|^{n/m}.
  - For N > 1 it is a Minkowski-type distance. It is Euclidean at **m = n = 2** (2011 states this).
  - **Correction:** the 2014 text says "for the simple case of m = n = 1, the drive function reduces to Euclidian distance". That is wrong. m = n = 1 is the L1 (city-block) distance, and file 19's inference from that sentence ("D = (Σ|·|^n)^{1/m}") was right about the form but should not have trusted the sentence. Fig. 6 simulations in the 2014 paper use n = 4 (supplement caption); the m used there was not extracted.
- (2) **r(H_t, K_t) = D(H_t) − D(H_{t+1}) = D(H_t) − D(H_t + K_t).** Reward is drive reduction.
- (12) r ≡ dD(H_t+K_t)/dK_t, and (13) r ≅ −K_t·∇D(H_t) + O(∇²D), the first-order Taylor form. The linear approximation reproduces the older "reward = deprivation × magnitude" models (decision field theory, Singh et al. 2010, MOTIVATOR). The nonlinear form predicts an inverted-U utility in outcome size, because overshooting the setpoint makes reward fall and then go negative (Fig. 11).
- (10) r(H_t, K̂_t) = D(H_t) − D(H_t + K̂_t), where K̂ is the sensory estimate of the outcome's effect, so reward is available before digestion.
- (11) r = D(H_t) − D(H_t + K_t) + T, with T > 0 a drive-independent palatability term.
  - For the quadratic case (S6) the paper shows T is equivalent to moving the setpoint to H* + T/(2K_t). `[derived]` check: x² − (x+K)² + T = −2K(x − T/(2K)) − K², which agrees.
  - The paper's label for this case is "m/n = 1". The quadratic case needs n/m = 2, since D = |x|^{n/m}. The label looks garbled or reversed.
- (14) p(H_t) ∝ e^{−D(H_t)} = e^{−(Σ|h*_i − h_{i,t}|^n)^{1/m}}. See section 6.

**Behavioural properties claimed (Eqs 6-9), with the condition n > m > 1.**
- (6) ∂r/∂k_j > 0: reward increases with dose.
- (7) ∂r/∂|h*_j − h_j| > 0: deprivation potentiates reward.
- (8) inhibition by irrelevant drives. The paper prints this as ∂r/∂|h*_i − h_i| > 0 for i ≠ j.
- (9) ∂²r/∂k_j² < 0: concavity, hence risk aversion.

**Checks `[derived/numeric]`.** I evaluated these on D = (Σ|·|^n)^{1/m} in two dimensions (deficits x_j = −5 and x_i = −3, dose k = 1), for n,m ∈ {(4,2), (3,2), (2,2), (2,1), (4,3), (1.5,1.2), (1,1)}.
- (6), (7) and (9) hold for all pairs with n/m > 1 or m > 1. They are stated for k small enough not to overshoot; the paper's own Fig. 11 shows reward falling when k exceeds the deficit.
- **Eq. 8 as printed has the wrong sign.** The text calls the effect inhibitory, and numerically ∂r/∂|dev_i| is **negative** in every case with m > 1: about −0.91 at (n,m) = (4,2), and about −0.29 at (4,3). It is exactly 0 at m = 1. Analytically: write s = Σ_{i≠j}|dev_i|^n and let a, a' be the deficits in dimension j before and after the outcome. Then r = (s+a^n)^{1/m} − (s+a'^n)^{1/m}, and ∂r/∂s = (1/m)[(s+a^n)^{1/m−1} − (s+a'^n)^{1/m−1}] < 0 exactly when m > 1 and a > a'.
- So the **condition for cross-drive inhibition is m > 1**, not n > m > 1. n > m (more precisely n/m > 1) is what makes the one-dimensional reward concave. No proof of the n > m > 1 claim appears in the paper; it is presented as properties of the form. At (n,m) = (2,2) the model already shows inhibition and (weak) concavity.
- Practical point for any algebra: **cross-drive interaction lives entirely in m.** At m = 1 the drive function is additively separable (a sum of per-variable terms), and drives do not interact at all.

**Operators / equations (learning side).** `[read]` for the 2011 main text.
- 2011 Eq. 8: Q_1(s,a) = [d(H_1)/d(H_0)]·Q_0(s,a). This is the energising update after a motivational shift. Proposition 2 (supplement, not read) says it is exact only when H_1 = c·H_0, c ≥ 0.
- 2011 Eq. 9: V(S_C, k_X) = [d(x*) − d(x*+k_X)] + γ[d(x*+k_X) − d(x*+k_X−l_X)] + γ²[d(x*+k_X−l_X) − d(x*)], the anticipatory-shivering example. Proposition 3 (supplement, not read) states that the optimum is k_X = l_X/2 when γ is not 1 but sufficiently close to 1. `[derived]` check for a quadratic D: ∂V/∂k = 0 gives k = γ·l/(1+γ), which tends to l/2 only as γ → 1. For an L1 drive (n = m = 1) V is piecewise linear and the interior optimum disappears. So the "l/2" result needs both a convex drive and γ near 1.

**Empirical standing (blunt).**
- The 2014 paper is a simulation and theory paper with qualitative agreement to published animal results (progressive-ratio breakpoints, anticipatory responding, rise-fall response pattern, dopamine modulation). It fits no parameters to data.
- No direct test of the exponents m and n was found in the sources read. The paper itself says the drive-reduction form makes the exponent "experimentally testable" and proposes a nonlinear-versus-linear reward design (Fig. 11). I did not search for whether anyone ran it. Marked unconfirmed.
- No replication literature on the theory as such was checked.
- The form has no per-dimension importance weights. Every regulated variable enters symmetrically (the 2014 text mentions no weights). Juechems & Summerfield (section 5) get asymmetry only through p and q.

**Operand/operator translation.** Operand: an agent's state vector, with a setpoint as a fixed attribute. Operator: an additive outcome vector K. Drive is a norm of deficit. Reward is the drop in norm. Everything about the interaction between drives is the single exponent m.

---

## 2. The theorem, exactly, and what it needs

**Statement `[read]`** (eLife Methods, "Rationality of the theory").
- Definition: a homeostatic trajectory is p = {K_0, K_1, ...}. P(H_0) is the set of such trajectories that, started at H_0, **end at H***.
- (S1) SD_D,p(H_0) = Σ_{t=0}^{w−1} γ^t D(H_{t+1}), with H_{t+1} = H_t + K_t.
- (S2) SD_R,p(H_0) = Σ_{t=0}^{w−1} γ^t r_t = Σ_{t=0}^{w−1} γ^t [D(H_t) − D(H_{t+1})].
- Proposition (S3): for any H_0, **if γ < 1, argmin_{p∈P(H_0)} SD_D = argmax_{p∈P(H_0)} SD_R.**
- Proof (as printed, S4-S5): along a trajectory with D_0, D_1, ..., D_w = D(H*) = 0,
  SD_R = D_0 + (γ−1)·(D_1 + γD_2 + ... + γ^{w−2}D_{w−1}) = **D_0 + (γ−1)·SD_D**,
  because the last term of SD_D is γ^{w−1}·D* = 0. D_0 is fixed by the start state and γ − 1 < 0, so the orderings are opposite.
- The main-text continuous versions (Eqs 3-5, written with p(π)^{γt}) are loosely typeset. The discrete Methods version is the one to cite.

**Checked `[derived]`.** The telescoping in S5 is correct. The theorem does not use any property of D except that D(H*) = 0.

**What the theorem actually is.** It is Abel summation: reward is a potential difference, so a discounted sum of potential differences is a function of the start potential and a discounted sum of potentials. It is an identity, not an optimality result about behaviour. Its content is the choice r = ΔD, not the algebra after.

**Generalisations `[derived]`.**
- (a) **Terminal state free.** For any trajectory of length w ending in H_w with drive D_w,
  SD_R = D_0 + (γ−1)·SD_D − γ^w·D_w.
  Check at w = 1: D_0 − D_1 = D_0 + (γ−1)D_1 − γD_1. ✓
  The identity needs D_w = 0 (the paper's end-at-setpoint restriction) for the arg-orderings to coincide exactly when trajectories have different lengths, since γ^w D_w then differs between trajectories.
- (b) **Infinite horizon.** For bounded D and γ < 1, the tail term γ^w D_w → 0, so SD_R^∞ = D_0 + (γ−1)·SD_D^∞. The orderings of policies by discounted reward and by discounted drive then coincide **for every start state, with no requirement that the setpoint be reachable.** The paper's finite-trajectory restriction P(H_0) is stronger than needed.
- (c) **Expectations.** The identity is linear in D, so for stochastic transitions it holds in expectation: E[SD_R] = D_0 + (γ−1)·E[SD_D].
- (d) **γ = 1** gives SD_R = D_0 − D_w, which depends on endpoints only. **γ > 1** reverses the ordering.
- (e) **Shift the drive.** Any D' = D + c has the same trajectory ranking, because rewards are unchanged.

**The setpoint condition, stated plainly.** "Setpoint" enters the theorem in one place, D(H*) = 0 together with trajectories ending at H*. In the infinite-horizon form it is not needed. What stays essential is that reward is the difference of the same drive function at consecutive times.

---

## 3. What the theorem does and does not say about behaviour

- It says that an RL agent given the reward r = ΔD solves the same problem as an agent that minimises discounted deviation. Nothing is learned about which actions are good.
- It says nothing about which D. The substantive claims in the paper (risk aversion, inhibition, anticipation) come from the form of D, Eq. 1, not from the theorem.
- It is not a theorem about stability under learning. The "stepping back from the brink" argument is a simulation plus a verbal argument (probability of z identical consecutive random actions is 2^{−z}; the paper states the result generalises to multi-dimensional spaces without proof).

---

## 4. Does SDR = D_0 + (γ−1)·SDD extend to D_self + w·D_partner?

**The published coupling `[read]`.** Yoshida & Man 2024 (arXiv 2412.12103; NeurIPS 2024 IMOL workshop). Each agent is a homeostat with reward r_{t+1} = β(D_t − D_{t+1}). Affective empathy is the coupled drive **D = D_possessor + w·D_partner** (w = 0.5 in the food-sharing task). Cognitive empathy is only observing the partner's state. Drives used: Experiment 1, D = −ln P*(s) with P*(High) = 0.95 and P*(Low) = 0.05 (so D(High) ≈ 0.051, D(Low) ≈ 3.0); grid and 2-D environments, D = ‖s‖² with β = 100. PPO + LSTM, 20 runs. Result: sharing arises only under affective coupling (Affective and Full conditions). **No theorem.** The only analysis is an informal argument from the transition diagram (Appendix C) that a possessor optimising only its own homeostasis always prefers EAT to PASS.

Note that in Experiment 1 D(High) ≠ 0, so the drive has no zero. Any theorem that needs D(H*) = 0 does not apply to that paper's own setup without the terminal correction (2a) or the infinite-horizon form (2b).

**Answer `[derived]`: yes, with conditions.**
Let x = (x_s, x_p) be the joint state, and D_c(x) = D_s(x_s) + w·D_p(x_p) with w fixed.

1. **Reward linearity.** r_c = D_c(x_t) − D_c(x_{t+1}) = r_s + w·r_p exactly, where r_p is the partner's own drive-reduction. So coupling the drives and coupling the rewards are the same operation.
2. **Identity.** Since D_c is a single function of the joint state, 2a-2e apply verbatim: SD_R^c = D_c(x_0) + (γ−1)·SD_D^c − γ^w D_c(x_w). Equivalently, SD_R^c = SD_R^s + w·SD_R^p, and each term obeys its own identity.
3. **Conditions under which the extension holds.**
   - **Fixed potential.** The same D_c must be used at both ends of every step. w must be a constant parameter. If w varies in time, the telescoping breaks. With r_t = ΔD^{(t)} using the weight w_t, the correction is Σ_{t≥1} γ^{t−1}(w_t − w_{t−1})·D_{p,t} added to the identity. So **if the weight is itself a state that actions can change (relationship strength, trust), the theorem lapses.** For the algebra, w should be a parameter of an operator, not a state variable, unless the correction term is carried.
   - **Nonnegative w for the setpoint form.** For D_c to have a joint minimum of 0 at the joint setpoint, both D's must be ≥ 0 with zero at their setpoints and w ≥ 0. For w < 0 (rivalry, schadenfreude) D_c is minimised by the partner being as far from setpoint as the state space allows. The identity still holds as an identity, and the "setpoint" becomes the spiteful corner. The finite-trajectory form of the theorem (end at the setpoint) is then not meaningful, but the infinite-horizon form is.
   - **A joint setpoint must exist for the finite form.** Resource-conserving settings (Yoshida-Man's single food item) may make D_s = D_p = 0 jointly unreachable, so P(H_0) is empty and the finite proposition is vacuous. The infinite-horizon ordering result still holds.
   - **Control.** The theorem concerns whoever's actions generate the trajectory. If the partner acts, the optimisation is over a game, not a single-agent problem; see below.
4. **Two agents with different weights.** Agent 1 has D^1 = D_a + w_1·D_b, agent 2 has D^2 = D_b + w_2·D_a. The identity holds for each agent separately. The agents have the same ordering over joint trajectories **iff w_1·w_2 = 1** (the vectors (1,w_1) and (w_2,1) are parallel exactly then, and D^2 = w_2·D^1). For w_1 = w_2 = 1 this is the identical-interest (team) case. For w_1·w_2 < 1 (mutual partial altruism, e.g. both 0.5) the agents agree only partially and the problem is a game, so the single-agent argmin/argmax equivalence says nothing about equilibria. Y&M's partner is passive in Experiment 1 and their agents share network weights in Experiment 2 (Appendix A), which sidesteps this.
5. **N agents.** With a weight matrix W (W_ii = 1, W_ij = w_ij), D^i = Σ_j W_ij·D_j and r^i = Σ_j W_ij·ρ_j, where ρ_j = D_j(t) − D_j(t+1) is agent j's own drive reduction. The identity becomes SD_R^i = Σ_j W_ij [D_{j,0} + (γ−1)·SD_{D_j}] (terminal terms aside). So the whole coupling structure is one linear operator W acting on the vector of per-agent drive trajectories. That is the nearest published-compatible object to an "operator on drives". `[derived]`: if each agent also internalises its partners' coupled drives (contagion), the effective matrix would be a Neumann series (I − Ω)^{-1}, where Ω holds the off-diagonal weights, convergent when the spectral radius of Ω is below 1. This is a design suggestion, not a published result.

**What the additive coupling cannot express `[derived/numeric]`.**
- D_s + w·D_p is a **sum of norms**, so the partner's deficit has no effect on the reward value of the agent's own relief: ∂r_self/∂(partner deficit) = 0 exactly. Own-need relief is as rewarding when the partner is starving as when sated.
- A **joint Minkowski aggregation** with m > 1 does produce the interaction: with the partner's deficits as extra coordinates in one (Σ|·|^n)^{1/m}, partner deficit lowers the reward value of own relief, by the same inhibition mechanism as Eq. 8 (negative derivative, numerically confirmed above). This is a different model, with one new exponent, and it gives "you do not enjoy your meal while your child starves" as a consequence rather than a stipulation. It is a candidate alternative to test against, not a published one.
- Y&M's surprise form, D = −ln P*(s), turns the coupling into a **tempered product of preferences**: e^{−D_c} = P*(s_s)·P*(s_p)^w, with w acting as an exponent on the partner's preference density. This links directly to the active-inference reading (section 6).

---

## 5. Juechems & Summerfield 2019: the same drive function, repurposed

**Citation.** Juechems, K. & Summerfield, C. (2019). Where does value come from? *Trends in Cognitive Sciences* 23(10):836-850. doi:10.1016/j.tics.2019.07.012. Read in full from the Oxford ORA author manuscript.

**Their vocabulary.** The reward paradox; homeostatically regulated reinforcement learning (HRRL); value map; cognitive setpoints.

**Equations `[read]`** (Box 2).
- Eq. 1: θ_t = X_t × U + θ_{t−1} × A_θ. The internal state is driven by chosen option features X through a learned map U, plus intrinsic dynamics A_θ (decay in the absence of input, e.g. debt grows, thirst grows).
- Eq. 2: δ_{t+1} = ‖θ_{t+1} − θ*‖_k, printed as the p-th root of Σ|θ_{t+1} − θ*|^q "for p = q". So the printed version is a Minkowski distance with one exponent k = p = q, and the text says a two-parameter version (p ≠ q, the K&G m and n) is needed for diminishing marginal utility.
- Eq. 3: **R_{t+1} = δ_t − δ_{t+1}**, which is K&G's drive reduction exactly. With A_θ = 0 and k = 1, R = X × U.
- Role of k: k < 1 favours single-asset bundles, k = 1 is indifferent between bundles, k > 1 favours mixed bundles. This is the same m-controls-interaction result as section 1.

**Theorems.** None. They cite the K&G equivalence implicitly through "the loss term is mathematically identical to what one would construe as reward".

**Claim relevant to the strand.** The setpoint dimensions are extended from physiology to cognitive goals "such as financial stability, moral worth, physical health", "social status", "social capital". This is asserted, not derived. The social dimensions are one-sentence examples, and they come with no coupling between agents. A small inconsistency: the text says agents "minimise the maximum distance to setpoints" (an L∞ norm), while Eq. 2 is a Minkowski k-norm. Those coincide only as k → ∞.

**Empirical standing.** The paper is an opinion piece. The empirical support cited is fMRI work on value maps in the medial prefrontal cortex and dACC (Juechems and colleagues; I did not read these studies). No claim here has been checked against data.

**Translation.** Same operand (state vector with setpoint) and operator (outcome offsets) as K&G, with the explicit extension that dimensions may be non-physiological. This is the only source read that proposes the same machinery for social-status-like variables, but without any inter-agent term.

---

## 6. The active-inference framing

**Their vocabulary.** Generative model; prior preferences (written p(o|C)); expected free energy G_π; risk; ambiguity; precision; interoceptive inference; allostasis.

**Pezzulo, Rigoli & Friston 2015 `[read]`, text only.**
- It reviews homeostatic regulation inside active inference and says that "priors act as drives or goals to enslave action", that reflexes minimise interoceptive prediction errors with the setpoint supplied by descending predictions, and that "the concept of reward is replaced by the realization of prior preferences".
- "Value is the complement of surprise or prediction error."
- It cites Keramati et al. and does not adopt the drive-difference reward.
- I found no stated drive function in the extracted text. Equations were not extractable, so this is unconfirmed rather than established.

**Friston 2010 `[from abstract/standard account]`.** Nat Rev Neurosci 11:127-138. Free energy F is an upper bound on surprise, F ≥ −ln p(s̃|m). Organisms act to keep sensory states within expected (preferred) bounds. Not read.

**Expected free energy `[read]`** (Smith, Friston & Whyte 2022, Eq. 13):
G_π = D_KL[ q(o|π) ‖ p(o|C) ] + E_{q(s|π)}[ H[p(o|s)] ].
The first term is risk, the divergence from preferred outcomes. The second is ambiguity. There is no variable labelled reward: "preferences are encoded within a specific type of prior probability distribution".

**K&G's own mapping to this framework `[read]`** (2014 Eq. 14 and the "Relationship" section). They propose that drive is equivalent to surprise, p(H_t) ∝ e^{−D(H_t)}, so −ln p = D up to a constant. They add that optimising either objective of their Eq. 5 "corresponds to prescribing a principle of least action applied to the surprise function". They also say the two theories sit at different levels (free energy computational, theirs algorithmic) and use different tools (variational Bayes versus optimal control).

**Corrections and derivations `[derived]`.**
- −ln p = D holds up to the normaliser ln Z: p = e^{−D}/Z. The paper writes proportionality and then equality.
- e^{−D} is a Gaussian only when D is quadratic: m = 1, n = 2 (D = Σ x²), or n/m = 2 in one dimension. At m = n = 1 it is a Laplace density. A Gaussian prior preference with precision matrix Π gives D = ½ (o−o*)ᵀ Π (o−o*). So **the active-inference counterpart of K&G's drive carries per-dimension precision weights, which K&G's form lacks.**
- Substituting p(o|C) ∝ e^{−D(o)} into the risk term: KL[q‖p(o|C)] = −H[q(o|π)] + E_q[D(o)] + ln Z. So per time step, G is expected drive minus outcome entropy plus ambiguity (plus a constant). The policy score sums these over the horizon, undiscounted.
- Comparison with K&G: with γ < 1, K&G's theorem says ranking by discounted reward ΔD equals (reverse) ranking by discounted state cost D. Active inference's risk term is the state-cost form already. So **K&G's identity is the statement that a discounted potential-difference reward is, up to an affine map, the same objective as active inference's discounted preference cost**, minus the entropy and ambiguity terms that give active inference its information-seeking part. That equivalence needs the discount, since active inference has none and the undiscounted K&G reward (γ = 1) depends on endpoints alone. `[derived]`
- Honest verdict on "the active-inference framing": the equivalence is real at the level of one-step state costs, and the two literatures differ on (i) discounting, (ii) exploration (an entropy term versus ε-greedy or softmax), (iii) precision weights versus none.

**Multi-agent active inference.** Not read for this file. Friston & Frith 2015, "A duet for one" (Consciousness and Cognition), is the standard cited example of two coupled generative models; I did not verify its DOI and it is listed under Unconfirmed. In the active-inference language, w in D_s + w·D_p corresponds to an exponent on the partner's preference density, as in section 4.

---

## 7. Operand/operator translation for the algebra

| Piece | Source | Form | Status |
|---|---|---|---|
| Operand: state vector with setpoint | K&G | H ∈ ℝ^N, H* | [read] |
| Operator: outcome offset | K&G | H → H + K | [read] |
| Drive (norm of deficit) | K&G | D = (Σ\|h*−h\|^n)^{1/m} | [read] |
| Reward | K&G, J&S | r = D(H) − D(H+K) | [read] |
| Identity | K&G | SD_R = D_0 + (γ−1)SD_D − γ^w D_w | [read] (w-term derived) |
| Cross-drive interaction | K&G | m > 1 only | [derived] |
| Coupling | Y&M | D_c = D_s + w·D_p | [read] |
| Coupling as one matrix | none | r^i = Σ_j W_ij ρ_j | [derived] |
| Weight consistency (two agents) | none | same ordering iff w_1·w_2 = 1 | [derived] |

---

## 8. What exists vs what does not

**Exists.**
- A drive function with an exact two-exponent form, a one-line telescoping identity linking discounted drive and discounted drive-reduction reward, and simulated agreement with animal phenomena (K&G).
- The same machinery proposed for non-physiological goals (J&S, assertion only).
- A weighted pairwise coupling of drives, simulated, with the result that sharing needs the coupling (Y&M).
- An active-inference reading in which drive is a negative log prior preference (K&G Eq. 14; Pezzulo et al.; EFE form from Smith et al.).

**Does not exist (as far as read).**
- No published theorem for a coupled drive. Everything in section 4 is my derivation. It is elementary, but it does set the conditions for when the coupling operator is well-behaved.
- No game-theoretic result for two coupled homeostats, nor any equilibrium or stability analysis.
- No test of the exponents m and n against data.
- No inter-agent term in J&S, and no adaptive or state-dependent w anywhere.
- No per-dimension weights in K&G's drive.
- No stated mapping between K&G's m, n and active-inference precision.

---

## Unconfirmed

- Whether anyone has run K&G's proposed linear-vs-nonlinear reward experiment (Fig. 11), or fitted m and n to behaviour.
- The proofs of K&G 2011 Propositions 2 and 3 (supplement not accessed). My derivation of the k_X = γl/(1+γ) optimum for a quadratic drive is mine and agrees with the stated l/2 only in the γ → 1 limit.
- Whether Pezzulo et al. 2015 state any drive function; equations were not extractable from the PMC text.
- Friston 2010's formulas (read from abstract and standard accounts only).
- The follow-up Yoshida & Man (arXiv 2506.12894), which adds learned decoding of a partner's emotion, and Yoshida, Sprekeler & Gutkin (arXiv 2507.04998). Abstracts only; neither abstract mentions a theorem.
- Friston & Frith 2015 and the wider multi-agent active-inference literature (DOI not verified here).
- The Juechems fMRI studies cited in J&S.
- The value of m used in K&G's Fig. 6 simulations.

## Sources

- https://elifesciences.org/articles/04811 (JATS XML from github.com/elifesciences/elife-article-xml, `articles/elife-04811-v1.xml`)
- https://proceedings.neurips.cc/paper/2011/file/9778d5d219c5080b9a6a17bef029331c-Paper.pdf
- https://arxiv.org/abs/2412.12103 ; https://arxiv.org/abs/2506.12894 ; https://arxiv.org/abs/2507.04998
- https://ora.ox.ac.uk/objects/uuid:02f3af5e-bc2d-49f5-bf1d-f2e3d7e2f545/files/m912294907691555c3e38afc843306587
- https://pmc.ncbi.nlm.nih.gov/articles/PMC4779150/ ; https://pmc.ncbi.nlm.nih.gov/articles/PMC8956124/
