# Prior work 062: multi-agent homeostatic RL with coupled drive D = D_self + w·D_partner

Direction: D194

Date: 2026-10-29. Kind: model. Cross-references: file 047 (sections 1, 2, 4: the K&G drive function, the telescoping identity, and a first single-sentence extension to coupling), file 19 (sections 12, 14), file 21 (social preferences), file 20 (dyadic coupling). 047 already derived that the identity extends to a fixed-weight joint drive; this file does not repeat that derivation but takes it as given, adds the **game-level** statement (equilibria), and adds a worked model for stability and free-riding.

**Method and honesty note.** Tags: `[read]` = read at source (this session or in 047, said which); `[derived]` = my own algebra this session, checked numerically with numpy (script in the session scratchpad, not kept in the repo); `[from abstract/standard account]` = not read at source. Nothing here is a published result on coupled homeostatic RL unless tagged so. The Python check used plain numpy; sympy was not installed, so the symbolic steps below were done by hand and then confirmed numerically.

Sources re-checked this session:
- Yoshida & Man 2024, arXiv 2412.12103, HTML re-read for the specific questions in section 4 (partner policy, shared parameters, free-riding, w values, limitations). Abstract and metadata confirmed from arxiv.org/abs. `[read]`
- Yoshida & Man 2025, "Homeostatic Coupling for Prosocial Behavior", arXiv 2506.12894. Abstract only. `[from abstract]`
- Keramati & Gutkin 2014: relied on 047's full reading of the eLife XML. Not re-read.

DOIs confirmed through Crossref this session:
- Rosen 1965, Econometrica 33(3):520-534, doi:10.2307/1911749.
- Monderer & Shapley 1996, Potential games, Games and Economic Behavior 14:124-143, doi:10.1006/game.1996.0044.
- Bergstrom, Blume & Varian 1986, On the private provision of public goods, J. Public Economics 29:25-49, doi:10.1016/0047-2727(86)90024-1. (The DOI I first tried from memory, ...90019-1, did not resolve; the search result is the one used.)
- Becker 1974, A theory of social interactions, J. Political Economy 82:1063-1093, doi:10.1086/260265.
- Fehr & Schmidt 1999, QJE 114:817-868, doi:10.1162/003355399556151.

**Summary.**
1. **The reward/drive equivalence holds in the multi-agent case at the level that matters.** For any fixed (even state-dependent) coupled drive that is a function of the joint state, each agent's discounted-reward ordering of its own policies, holding the others fixed, equals its discounted-drive ordering. It follows that the **Nash equilibria of the reward game and of the drive game are the same set**. The equivalence does not make the multi-agent problem single-agent: the others' policies change, and learning is non-stationary. `[derived]`
2. **It fails when the coupling weight is itself a state that actions can change**, and when the coupled drive is not one fixed function at both ends of a step. 047 gave the correction term; here it is placed in the model as a rule: w belongs in the operator, not the state, unless the correction is carried. `[derived]`
3. **Coupling does not by itself cause instability; it moves the equilibrium.** In the worked model (separable quadratic drives, a public-good effort game) gradient play has a real, strictly positive spectrum for every w that keeps the game well-posed. What coupling does is shift the equilibrium effort up, toward the team optimum, and reduce free-riding without removing it for w < 1. `[derived]`
4. **Free-riding persists for any w below the team value.** At w = 0 the shortfall relative to the team optimum is a fixed function of the cost-to-benefit ratio and approaches 1/N for large effort cost. A weight of 1 is the team game and removes it exactly. `[derived]`
5. **Simultaneous best-response dynamics, not gradient play, can diverge, and coupling lowers the threshold.** The condition is (N−2)·b²·v < k². `[derived]`
6. **Yoshida & Man's experiments cannot show any of this**: in the food-sharing task only the possessor acts; the grid partner is fixed; and the 2-D field shares network weights across agents. Only w = 0.5 is stated (for food sharing; the mobile environments give no value). No free-riding, stability or convergence discussion appears. `[read]` *(Validation 2026-10-29: this item first said shared weights "by itself turns the training objective into a team objective whatever w is". That was wrong on two counts, see section 6: independent PPO learners with tied weights do not follow the gradient of the summed return, and the paper's own 2-D field None condition, shared weights with no coupling, showed no prosocial behaviour.)*

---

## 1. The sources, what they stated, what they did not

**Keramati & Gutkin (2014)** `[read, via 047]`. D(H) = (Σ|h*_i − h_i|^n)^{1/m}; r = D(H_t) − D(H_{t+1}); proposition: for γ < 1, argmin of discounted drive sum = argmax of discounted reward sum over trajectories ending at the setpoint, via SD_R = D_0 + (γ−1)·SD_D. Single agent, physiological variables. See 047 for the exact form, three errors in the paper's text, and the generalisations (terminal state free; infinite horizon).

**Yoshida & Man (2024)** `[read]`. Verbatim items confirmed this session:
- Coupling: "D = D_possessor + w D_partner", with "the weighting factor w=0.5".
- Reward: r_{t+1} = β(D_t − D_{t+1}), "the internally perceived reduction of deviations from homeostatic setpoints".
- Drive in the food-sharing task: D_possessor = −ln P*(s_t^i) (Appendix B.1).
- Food sharing: "only the Possessor takes actions"; the Partner is passive. Condition "none": "The Possessor optimizes only for its own homeostasis."
- Grid: the Partner is fixed to the left side of the grid (whether it learns is not said on the page).
- 2-D field: "all agents were trained in a situation where the network weights were shared"; Section 3 (Appendix A): "we optimized the network weights and shared the acquired experience with all agents to facilitate learning".
- 2-D field: "there is no distinction between Partners and Possessors, as both agents can move and act freely" (identical roles). Section 3.1, covering both mobile environments: "No prosocial behavior was observed in the None and Cognitive conditions"; prosocial behaviour is shown for the Affective condition (Fig. 5B). n = 20 runs. Algorithm: PPO with an MLP encoder and LSTM. (Added in validation 2026-10-29, `[read]`.)
- Only w = 0.5 is reported, and only for the food-sharing task; the mobile-environment text states no value. The page has no limitations section; Section 4 closes with a pointer to going beyond "giving agents direct access to partners' internal states".
- No mention of free-riding, stability, convergence, or a selfish agent beyond the "none" condition.

**Yoshida & Man (2025)**, arXiv 2506.12894 `[from abstract]`: adds learned empathy, where agents decode a partner's displayed emotion to infer the internal state and so reconstruct D_partner. No theorem claimed in the abstract.

**What neither paper contains:** a statement about equilibria, about two learning agents each with a coupling weight, or about what w does to stability. Those are the content of sections 3 to 5.

---

## 2. The model, specified

### 2.1 Objects

- Agents i = 1..N. Agent i has state x_i ∈ R^{d_i} with setpoint x_i* (translate so x_i* = 0 when convenient).
- **Own drive**: D_i(x_i) = (Σ_k |x_{i,k}|^n)^{1/m}, K&G's form (047 section 1). The special case n = 2, m = 1 gives D_i = Σ_k x_{i,k}², separable, with no cross-variable interaction (047: cross-drive interaction lives entirely in m > 1). The worked model below uses it for tractability and so isolates the effect of the *inter-agent* coupling from the *intra-agent* one.
- **Coupling matrix** W ∈ R^{N×N}, W_ii = 1, W_ij = w_ij. In the pairwise form of Yoshida & Man, W = [[1, w],[w, 1]] for a symmetric pair, and the possessor's row is (1, w).
- **Coupled drive of agent i**: D^i(x) = Σ_j W_ij·D_j(x_j). Optionally a nonlinear form D^i = f_i(D_1(x_1), ..., D_N(x_N)) with f_i continuous and bounded below.
- **Reward**: r^i_t = β_i·(D^i(x_t) − D^i(x_{t+1})) = β_i·Σ_j W_ij·ρ^j_t, where ρ^j_t = D_j(x_{j,t}) − D_j(x_{j,t+1}) is agent j's own drive reduction. (Linearity in W is exact. `[derived]`)
- **Dynamics**: x_{t+1} = F(x_t, a_t) with a_t = (a_1,..,a_N) the joint action. Policies π_i. Discount γ_i < 1.
- **Objectives**: V_i(π) = E[Σ_t γ^t r^i_t], and the drive version S_i(π) = E[Σ_{t≥0} γ^t D^i(x_{t+1})].
- **Signals** (cognitive empathy, learned empathy): D^i is evaluated on an estimate x̂_j = g_i(o_i), where o_i is what i observes of j. The identity below then applies to the observation-based function, see 3.4.

### 2.2 Reduction to the 2024 paper

Possessor = agent 1 with row (1, 0.5). Partner = agent 2, passive in food sharing. The "affective" condition is W_12 = 0.5; "none" is W_12 = 0; "cognitive" is W_12 = 0 with x_2 in the possessor's observation. The surprise-form drive −ln P* gives e^{−D^1} = P*(s_1)·P*(s_2)^w, i.e. coupling is a tempered product of preference densities (047 section 4).

---

## 3. Does the reward/drive equivalence hold? Statements and proofs

All `[derived]` unless marked. Throughout, the drive functions are bounded below and the horizon is infinite with γ < 1, or finite with the terminal term kept.

### 3.1 Per-agent identity

For agent i, with D^i fixed:
V_i = D^i(x_0) + (γ−1)·S_i − (tail term that tends to 0 as the horizon grows, for bounded D^i).

(With the reward scale β_i of 2.1 the whole right side is multiplied by β_i > 0, which changes no ordering.)

Proof: Abel summation of r_t = D^i_t − D^i_{t+1}, as in K&G's S4-S5 with the terminal correction in 047. The identity holds pointwise on each trajectory, so it holds in expectation, for any dynamics and any joint policy.

### 3.2 Best responses coincide

Fix the other agents' policies π_{−i}. Then x_0 is independent of π_i (the start state is given), so D^i(x_0) is a constant, and V_i = const − (1−γ)·S_i. Therefore **argmax_{π_i} V_i(π_i, π_{−i}) = argmin_{π_i} S_i(π_i, π_{−i})** for every π_{−i}.

### 3.3 Equilibria coincide

A profile is a Nash equilibrium of the reward game iff each π_i is a best response to π_{−i} for V_i; by 3.2 that is the same condition as being a best response for −S_i. So the Nash sets of the reward game and of the drive game are identical. If the start state is random with a law that does not depend on policies, the same holds in expectation over x_0.

What this does **not** give: uniqueness, existence in learned (parametrised) policy classes, convergence of learning, or any statement about what the drive game's equilibria look like. Sections 4 to 5 supply the last for one model.

### 3.4 When the equivalence breaks

1. **Time-varying weight** `[derived]`. If the reward at step t uses weight w_t: r_t = D(x_t; w_t) − D(x_{t+1}; w_t), then the sum differs from the telescoped drive sum by Σ_{t≥1} γ^{t−1}(w_t − w_{t−1})·D_{p,t}, with D_{p,t} the partner's drive (047 section 4). So if w is relationship strength, trust or attachment and actions change it, the reward is **not** a drive difference of any one function and the equivalence is lost. Rule for the model: **w lives in the operator (a parameter), not the state.** If the algebra needs a dynamic w, it must carry the correction term, or define the reward as the drive difference of the *new* weight at both ends.
2. **Different functions at the two ends of a step.** Any reward of the form D'(x_t) − D''(x_{t+1}) with D' ≠ D'' (for instance a partner estimate that is updated between the two evaluations) is not a potential difference. With learned empathy, D^i is evaluated on x̂_j. If the decoder g_i changes during learning, the reward is no longer a difference of one function; the identity holds only relative to the decoder at a frozen moment.
3. **Reward computed from the observation, not the state.** If D^i is a function of o_i (noisy, partial) the identity holds for S_i defined on o_i, not on the true state, so "minimise discounted true drive" is not what the agent optimises.
4. **Not a failure**: nonlinear coupling D^i = f(D_1, ..., D_N), a negative w (rivalry), or an inequity-aversion term such as Fehr-Schmidt's `[from abstract/standard account]` (a loss on max(x_j − x_i, 0) and on max(x_i − x_j, 0)) written over drives: D^i = D_i + w·D_j + λ·|D_i − D_j|. Each is a single function of the joint state, so the identity holds verbatim. What changes is the *shape* of the game, not the identity.

### 3.5 What the equivalence does and does not show for the algebra

It shows that **"agent i optimises coupled reward" and "agent i minimises coupled drive" are one object**. So the algebra can state the coupling at the level of drives (a linear operator W on the vector of agent drives) and inherit the reward form free. It does not show that the coupled system is cooperative: with W_ij < 1 or W not a common vector the agents have different objectives, and the right tool is game theory, which section 4 uses.

---

## 4. Worked model: public-good effort with homeostatic agents

A model chosen because it is the simplest one where own cost, shared benefit and coupling all appear, and where free-riding has a definite meaning.

### 4.1 Setup

- Each agent chooses effort e_i ≥ 0 (continuous, one shot, or a per-step choice in a stationary problem).
- Public good g = Σ_j e_j reduces every agent's deficit in a regulated variable h: h_i = a − b·g, with a > 0 the initial deficit and b > 0 the benefit per unit effort.
- Effort has a private cost in a second regulated variable (energy): c_i = k·e_i, k > 0, setpoint 0.
- Own drive: D_i = (a − b·g)² + (k·e_i)². This is K&G's form at n = 2, m = 1 (separable): the two variables do not interact, which keeps the inter-agent effect isolated.
- Coupled objective of agent i: U_i = D_i + Σ_{j≠i} w_ij·D_j. Take w_ij = w_i, one weight per agent applied to all others, and define v_i = 1 + (N−1)·w_i.

Note e_j enters D_j through g (shared benefit) and through its own energy term; agent i's effort does not appear in D_j's energy term. That is what makes the cost private.

### 4.2 First-order conditions and equilibrium `[derived]`

∂U_i/∂e_i = −2b·v_i·(a − b·g) + 2k²·e_i = 0, so

e_i·(k² + b²·v_i) = b·v_i·(a − b·Σ_{j≠i} e_j).

For the symmetric case (all w_i = w, v = 1 + (N−1)w):

**e(w) = a·b·v / (k² + N·b²·v)**, total effort g = N·e.

Cases:
- Selfish, w = 0, v = 1: e_0 = ab/(k² + Nb²).
- Team, w = 1, v = N: e_1 = abN/(k² + N²b²). With w = 1 every agent minimises the same function Σ_j D_j, so this is the team optimum (a strictly convex problem, unique minimiser).

**Free-riding ratio** (total selfish effort over total team effort):
g_0/g_1 = (k² + N²b²) / (N·(k² + N b²)).

Properties: equals 1 when k → 0 (no cost, nobody shirks); tends to 1/N as k²/b² → ∞ (cost dominates); strictly less than 1 for N ≥ 2 and k > 0. Numeric check: N = 2, b = k = 1, a = 1: g_0 = 0.667, g_{0.5} = 0.750, g_1 = 0.800. N = 5, same: 0.833, 0.9375, 0.9615. At N = 2, b = 1, k = 3, w = 0: ratio 0.591 (formula and numerics agree).

So **coupling reduces free-riding monotonically in w and eliminates it only at the team weight**. Shortfall at w = 0.5 (N = 2, b = k = 1): 6% of the team total; at w = 0, 17%.

### 4.3 A degenerate case worth recording

If effort had no private cost in a separate variable, i.e. effort only moved the shared deficit (s_i = a − b·g + k·e_i with the cost entering the same variable as the benefit), the equilibrium would be s_1 = s_2 = 0 for **every** w and there would be no free-riding. The reason is that a reachable common setpoint makes every agent's problem "hit zero", independent of weights. So **free-riding in this class of model requires that the cost is a separate regulated variable, or that the setpoint is not jointly reachable.** `[derived]` This is a modelling point for the algebra: a drive on a variable that other drives cannot also move is what makes conflict.

### 4.4 Sharing game (Yoshida-Man's task, solved) `[derived]`

One resource unit R held by agent 1, who consumes c and passes R − c. Deficits: s_1 = d_1 − c, s_2 = d_2 − (R − c). Agent 1 minimises s_1² + w·s_2². Then

c* = (d_1 − w·d_2 + w·R)/(1 + w). For d_1 = d_2 = d: c* = (d(1−w) + wR)/(1+w), and the passed amount is R − c* = (R − d(1−w))/(1+w).

At w = 0 the possessor passes only the surplus R − d. At w = 1 it splits R equally. At 0 < w < 1 the passed amount is in between and grows with w. Under the **scarce** case R < d(1−w) the passed amount is negative, i.e. the corner solution (no sharing) applies: **below the critical w = 1 − R/d, no sharing is optimal.** (In general the passed amount is (R − d_1 + w·d_2)/(1 + w), positive iff w·d_2 > d_1 − R, so the threshold does depend on the partner's deficit; an earlier wording, "whatever the partner's deficit", was wrong and was corrected in validation.) This restates the paper's informal claim (a self-interested possessor will not share) with a threshold, and shows why w = 0.5 can look like "prosociality" in one environment and be inert in a scarcer one. Not in the paper: the paper only tested w = 0.5 `[read]`.

---

## 5. Stability `[derived]`

Two dynamics are treated: simultaneous gradient play (the model of a continuously learning agent), and simultaneous best-response iteration (the model of an agent that jumps to the optimum given others' present play).

### 5.1 Gradient play

ė_i = −∂U_i/∂e_i. The pseudo-gradient has Jacobian J = 2k²·I + 2b²·v·1ᵀ, where v = (v_1, ..., v_N) and 1 is the all-ones vector.

- J is a diagonal shift of a rank-one matrix, so its eigenvalues are 2k² (multiplicity N−1) and 2k² + 2b²·Σ_i v_i (once). All are real. All are positive as long as Σ_i v_i > −k²/b², which holds for every nonnegative coupling and for moderate negative ones.
- So **gradient play is locally, and because the system is linear, globally, asymptotically stable at the Nash equilibrium for any non-negative couplings and any heterogeneity in them**, in this model. Coupling does not destabilise it. Numeric check, N = 2 with w = (0, 1) and k = 0.5: eigenvalues of J are 0.5 and 6.5.
- **When is the game an exact potential game** (Monderer & Shapley 1996 `[from abstract/standard account]`)? Iff ∂²U_i/∂e_i∂e_j = ∂²U_j/∂e_j∂e_i, i.e. v_i = v_j. So **equal coupling weights give a potential game**, and (the U_i being costs) the potential's minimiser is the equilibrium, which makes better-response and gradient dynamics converge to it. Unequal weights give a game that is not an exact potential game in these coordinates but is still stable by the spectrum.
- **Rosen's sufficient condition** (Rosen 1965 `[from abstract/standard account]`, diagonal strict concavity, i.e. the symmetric part of J positive definite) is **not implied** by heterogeneous weights. The symmetric part has smallest eigenvalue 2k² + b²·(1ᵀv − ‖1‖·‖v‖) (by the rank-two structure). For v_i unequal, ‖1‖·‖v‖ > 1ᵀv, so for small k it can go negative. Numeric: N = 2, w = (0, 1), k = 0.5, b = 1 gives smallest symmetric eigenvalue 0.338, still positive; at k = 0.2 it is −0.082 (checked in validation with numpy; the expression is the exact eigenvalue, not a bound).
- **Correction (validation 2026-10-29)**: this file first concluded that "uniqueness through Rosen is guaranteed only for equal weights or large enough k". That is wrong. Rosen's diagonal strict concavity is required only for *some* positive weighting r of the players' payoffs `[standard account; Rosen 1965 not opened]`. Taking r_i = 1/v_i gives diag(1/v)·J = 2k²·diag(1/v) + 2b²·11ᵀ, whose symmetric part is positive definite for every positive v (numeric, N = 2, v = (1, 2), k = 0.2: smallest eigenvalue 0.060). So Rosen's condition holds for all non-negative couplings in this model; the unweighted symmetric part is simply the wrong test. (Uniqueness here also follows directly from the linear FOC system.)

### 5.2 Simultaneous best-response iteration

Each agent jumps to its best response each round, all at once (Jacobi iteration). The map has slope s_i = b²·v_i/(k² + b²·v_i) per other agent. In the symmetric case the iteration matrix is −s·(11ᵀ − I), whose spectral radius is (N−1)·s. It converges iff (N−1)·s < 1, that is

**(N − 2)·b²·v < k²**, with v = 1 + (N−1)·w.

- For N = 2 this always holds (nonnegative coupling): two-agent best-response converges.
- For N > 2 it fails once the group is large enough or the coupling strong enough: at k = 0.5, b = 1, N = 5 the spectral radius is 3.20 at w = 0, 3.69 at w = 0.5 and 3.81 at w = 1. At N = 10, w = 0.5, k = 1: 7.6. Coupling raises v and so **lowers the stability threshold**: stronger coupling makes simultaneous best-response oscillate sooner.
- Interpretation `[derived]`: agents who each read "everyone else's effort" and move to the optimum together overshoot, more so the more they care about the group (v large) and the more of them there are. Damped updating e ← (1−α)e + α·BR(e) converges iff α < 2/(1 + (N−1)·s) (symmetric case; corrected in validation from "a learning rate small relative to 1/(1 + b²v/k²)", which is 1 − s and is not sufficient in general, e.g. s = 0.5, N = 10), and sequential updating also restores convergence, in line with the gradient-play result above.

### 5.3 What this means for the claim "coupling stabilises the group"

Not established, and not what the model says. In the model coupling (a) leaves gradient play stable, (b) moves the equilibrium toward the team optimum, (c) makes naive simultaneous best-response less stable. "Stability" must be named by which dynamics. The result cannot be assumed to carry over to deep-RL training (PPO with LSTM), which has neither of these dynamics exactly.

### 5.4 Negative weights `[derived]`

For w < −1/(N−1), v < 0: the agent wants to reduce total effort below zero, so the constrained solution is the corner e = 0 and the interior formulas above stop applying. For −1/(N−1) < w < 0 the model is well-posed: v is positive but below 1, and effort is below the selfish level (e.g. N = 2, w = −0.5, k = b = a = 1: e = 0.25 per agent against 0.333 at w = 0). So rivalry lowers contribution continuously, then switches it off at a threshold, not smoothly to negative values.

---

## 6. The parameter-sharing issue in Yoshida & Man's 2-D field experiment `[derived; corrected in validation 2026-10-29]`

Algebra that stands: with coupled rewards, Σ_i V_i = Σ_j (Σ_i W_ij)·(agent j's own-reward return), i.e. each agent's own return is weighted by its **column sum** c_j = Σ_i W_ij; for a symmetric W with equal weights c_j = 1 + (N−1)w for every j.

What was wrong in the first version: it claimed that sharing network weights and pooling experience makes the training objective Σ_i V_i, so the 2-D field "would show cooperation even for w = 0". Both halves fail.
- **Theory.** The paper trains with PPO `[read]`. Standard parameter sharing with independent learners updates θ by Σ_i E[∇log π_θ(a_i | o_i)·Â_i], each agent's action credited with *its own* advantage. The true gradient of Σ_i V_i(θ) also contains the cross terms ∇log π_θ(a_j | o_j)·Â_i for j ≠ i (how j's action, under the shared θ, changes i's return). Tied weights without those terms are tied independent learners, not a team optimiser. The paper does not say which credit scheme it uses `[read: not stated]`, so the inference cannot be drawn either way from the text.
- **Evidence.** The paper's 2-D field has identical roles and a None condition (no coupling) under the same shared-weights training, and reports "No prosocial behavior was observed in the None and Cognitive conditions" `[read]`. So the experiment does contain an uncoupled control, and that control did not cooperate; the effect of coupling is not confounded with parameter sharing in the way first claimed.

What remains: a single shared policy does constrain all agents to the same mapping from observation to action, which can make symmetric conventions easier to find; that is a weaker point, untested here.

---

## 7. Operand/operator translation for the algebra

- **Operand**: an agent's regulated-state vector with its setpoint; an agent's scalar drive D_i is a derived operand (a norm of deficit).
- **Operator 1, drive coupling**: a matrix W acting on the vector of agent drives, D^i = (W·D)_i. A drive-level linear operator with W_ii = 1. Composition = matrix product only if the second coupling is applied to *coupled* drives (contagion, section 5 of 047's Neumann-series suggestion), which is a design option, not a result of this file.
- **Operator 2, reward**: the difference operator Δ on a drive (r = −ΔD). The identity SDR = D_0 + (γ−1)·SDD is the algebraic statement that Δ and discounted summation are adjoint up to boundary terms. The multi-agent generalisation is that Δ commutes with W when W is constant, and **fails to commute when W is a state**, with the commutator equal to the correction term in 3.4(1).
- **Equilibrium** as a fixed point of the best-response operator on the joint policy. Coupling modifies the best-response operator's slope (s_i above), not its existence.
- **Parameters, not states**: w, k, b, a, N. The laws derived are statements about how these combine: e(w), the free-riding ratio, the stability inequality.
- **Observations to feed back to the algebra**: (a) the cost must be a separate variable for conflict to exist (4.3); (b) the weight must be an operator parameter for the telescoping identity to be available (3.4); (c) "coupling" has two distinct jobs, aligning objectives (4.2) and altering dynamics (5.2), and they move stability in opposite directions.

---

## 8. What exists vs what does not

**Exists.**
- K&G's single-agent identity (proved by telescoping) `[read, 047]`.
- Yoshida & Man's explicit coupled drive and its empirical effect on a possessor's sharing in three small environments (affective coupling is necessary for sharing there) `[read]`.
- Standard game-theory machinery for the shape of the problem: private provision of public goods (Bergstrom-Blume-Varian 1986: existence and uniqueness of the Nash equilibrium of voluntary contribution and its underprovision `[standard account]`; the further statement that altruism narrows but does not close the gap was attributed to them in the first version and is not confirmed as theirs, see Unconfirmed), potential games (Monderer-Shapley 1996), monotone games (Rosen 1965), a general theory of altruistic preference (Becker 1974), inequity aversion (Fehr-Schmidt 1999). I did not read any of these at source this session; I confirmed only that the citations exist.

**Does not exist (found).**
- A statement that the K&G equivalence holds, as a game-level equivalence of equilibria, for coupled homeostatic agents. Section 3.2-3.3 is my derivation; it is a short corollary of the single-agent identity, so a published source may exist that I did not find.
- Any published analysis of stability, free-riding, or equilibrium for homeostatic RL agents with a coupled drive.
- Any experiment that varies w, includes a free-riding payoff structure, or has two learning coupled agents with separate parameters.
- A fit of w to human data.

---

## 9. Unconfirmed

- Whether anyone has published a game-theoretic treatment of drive-reduction reward in multi-agent RL (searched only by direct recall and the two Yoshida-Man papers' pages; **no literature search was run on this**). The statement in section 8 is limited to what I looked at.
- *(Resolved in validation: the 2-D field has a None control, no prosocial behaviour, and identical roles; see sections 1 and 6.)* Still open: whether the PPO update with shared weights credits each agent with its own advantage or a pooled one; the paper does not say.
- Whether the 2025 follow-up (2506.12894) varies w; abstract only.
- The Bergstrom-Blume-Varian and Rosen/Monderer-Shapley statements are given as standard accounts; neither was opened.
- *(Resolved in validation: the unweighted symmetric part goes negative at k = 0.2, but Rosen's weighted condition with r_i = 1/v_i holds for all positive v; see 5.1.)* Rosen's definition with a weight vector is from the standard account; the paper was not opened.
- The Bergstrom-Blume-Varian 'altruism narrows but does not close the gap' statement: not confirmed as appearing in BBV 1986; Becker 1974 or later work (e.g. Andreoni) may be the right credit. Not checked.
- The 'does not exist' claims of section 8 were not tested by a literature search in validation either: the web search budget was exhausted before any query ran.
- The model of section 4 is a one-shot static game, not a Markov game; the claim that its structure transfers to a learned RL policy is untested.
- The Fehr-Schmidt form written over drives (3.4(4)) is my extension, not theirs.

## Links

- https://arxiv.org/abs/2412.12103 ; https://arxiv.org/html/2412.12103v1
- https://arxiv.org/abs/2506.12894
- doi:10.7554/eLife.04811 (K&G 2014)
- doi:10.1006/game.1996.0044 ; doi:10.2307/1911749 ; doi:10.1016/0047-2727(86)90024-1 ; doi:10.1086/260265 ; doi:10.1162/003355399556151

## Validation log (2026-10-29)

- ✎ Yoshida & Man 2024, arXiv 2412.12103, "Empathic Coupling of Homeostatic States for Intrinsic Prosociality" (Naoto Yoshida, Kingson Man; v1 16 Nov 2024): existence, authors and every quoted item in section 1 confirmed on the HTML `[read]`. Corrected: the 2-D field *does* have a None (uncoupled) control with identical roles and shared weights, which showed no prosocial behaviour; w = 0.5 is stated only for food sharing. Section 6's shared-weights inference rewritten; summary item 6 corrected.
- ✓ Yoshida & Man 2025, arXiv 2506.12894, "Homeostatic Coupling for Prosocial Behavior" (same authors, 15 Jun 2025): abstract confirmed; learned decoding of partner emotion via own emotion-generation functions matches.
- ✓ Keramati & Gutkin 2014, eLife 3, doi:10.7554/eLife.04811, "Homeostatic reinforcement learning for integrating reward collection and physiological stability": Crossref resolves, authors match. Telescoping identity re-derived (V = D_0 + (γ−1)S) and correct; content relied on 047, not re-read.
- ✓ Rosen 1965, Econometrica 33(3):520-534, doi:10.2307/1911749: Crossref resolves (title "Existence and Uniqueness of Equilibrium Points for Concave N-Person Games"). ✎ The file's use of it was wrong: weighted diagonal strict concavity (r_i = 1/v_i) holds for all positive couplings; fixed in 5.1.
- ✓ Monderer & Shapley 1996, GEB 14(1):124-143, doi:10.1006/game.1996.0044: Crossref resolves. Exact-potential condition v_i = v_j re-derived correct; ✎ "maximiser" changed to "minimiser" (costs).
- ✎ Bergstrom, Blume & Varian 1986, J. Public Econ. 29(1):25-49, doi:10.1016/0047-2727(86)90024-1: Crossref resolves. The altruism claim attributed to them moved to Unconfirmed.
- ✓ Becker 1974, JPE 82(6):1063-1093, doi:10.1086/260265: Crossref resolves.
- ✓ Fehr & Schmidt 1999, QJE 114(3):817-868, doi:10.1162/003355399556151: Crossref resolves; the description of the two max terms matches their standard form; the drive-level version is correctly labelled as this file's extension.
- Own derivations re-checked by hand and numpy: e(w), free-riding ratio and all its numerics (0.667/0.750/0.800; 0.833/0.9375/0.9615; 0.591; 6% and 17%), gradient-play spectrum (0.5, 6.5), Rosen symmetric eigenvalue 0.338, best-response condition (N−2)b²v < k² and radii 3.20/3.69/3.81/7.6, sharing-game c*, negative-weight example 0.25 vs 0.333, time-varying-w correction term: all ✓. ✎ sharing-game "whatever the partner's deficit" (false in general); ✎ damping bound in 5.2 (exact bound α < 2/(1+(N−1)s)).
- ? "Nothing published" claims (section 8, 9): not testable this pass, web search budget exhausted.

**Verdict.** Citations are all real and correctly credited, and the core algebra (per-agent identity, equal Nash sets, public-good equilibrium, free-riding ratio, stability spectra) checks out. Two substantive errors were corrected: the claim that parameter sharing makes Yoshida & Man's 2-D field a team objective (contradicted by the paper's own None control and by how independent PPO credits actions), and the claim that Rosen's uniqueness condition fails for unequal weights (it holds with Rosen's own weighting). The absence claims remain unverified.

## Cross-checks (2026-10-29)

Method: grepped the other files in this directory for Yoshida/Man, Keramati/Gutkin, Fehr-Schmidt, Hughes, Rosen, Monderer-Shapley, Bergstrom-Blume-Varian, Becker, public goods, free-riding, Nash and best-response, then read the overlapping sections. One primary-source check (arXiv 2412.12103v1 HTML, via WebFetch). No other file edited.

### Agreements

- **Y&M 2024 facts** (D = D_possessor + w·D_partner, w = 0.5 for food sharing only, r = β(D_t − D_{t+1}), PPO + LSTM, no theorem, possessor-only acts): agree with file 19 section 14 and file 047 section 4 ("published coupling"), and with 047's validation log.
- **K&G identity** r = D(H_t) − D(H_{t+1}), SD_R = D_0 + (γ−1)·SD_D: agrees with 047 sections 2-3 and 19 section 12. 062 section 3.1 matches 047 section 4 items 1-2 (terminal term kept).
- **Time-varying w correction** Σ_{t≥1} γ^{t−1}(w_t − w_{t−1})·D_{p,t} and "w is a parameter of an operator, not a state": identical in 047 section 4 item 3 and 062 section 3.4(1).
- **N-agent form** D^i = Σ_j W_ij D_j, r^i = Σ_j W_ij ρ_j: identical to 047 section 4 item 5. Tempered product e^{−D} = P*(s_1)·P*(s_2)^w: same as 047 section 4.
- **Two-agent weights**: 062 section 3.5 (different objectives unless weights are common; w = 1 is the team case) agrees with 047 section 4 item 4 (same ordering iff w_1·w_2 = 1 and w_2 > 0; w_1 = w_2 = 1 is the team).
- **Potential games** (section 5.1): consistent with file 23 section 9. 23 gives the decomposition "payoff = common coordination game + dummy game"; checked here: with equal v, U_i − Φ = (w−1)k²Σ_{j≠i}e_j², a dummy term, for Φ = v(a−bg)² + k²Σe_j², so 062's "exact potential iff v_i = v_j" fits it. 23 says "maximiser of Φ" for payoffs; 062 says "minimiser" for costs. Same statement, opposite sign convention.
- **Simultaneous vs sequential updating** (section 5.2): 23 section 9 states simultaneous updating can cycle while sequential better/best-reply stops at a Nash equilibrium. Agrees with 062's divergence of Jacobi best-response and the sequential fix.
- **Free-riding / underprovision** (section 4): qualitatively consistent with 23 (Bauch & Earn voluntary uptake below group optimum), file 10 section 2 (Olson: large groups under-provide) and file 24 (Olson as the free-riding null model). No numbers shared.
- **Fehr-Schmidt form** (section 3.4(4)): the two max terms match file 23 section on Hughes (α on max(e_j − e_i, 0), β on max(e_i − e_j, 0)) and file 21 section 1 and 6.
- **Fixed-weight equilibria**: file 081 section on coupling ("for fixed weight coupling the equilibria are the Nash equilibria of the joint game [derived, 062]") restates 062 section 3.3 correctly.
- **Existence claims** (K&G has no multi-agent theory; Y&M is the nearest explicit agent-to-agent drive law, simulation only): agree with file 19 sections 12, 14, 16 and 047 section 8. File 082 does not test any claim of 062 section 8.

### Contradictions and slips

1. **Parameter sharing in the 2-D field.** 047 section 4 item 4 says Y&M's shared network weights "sidestep" the game problem; 062 section 6 and summary item 6 say sharing does not make the objective a team objective, and the None control (shared weights, no coupling) showed no prosocial behaviour. Source check: the paper reports "No prosocial behavior was observed in the None and Cognitive conditions" and the 2-D field has a None condition. **062 is right**; 047's wording is too strong (047's own validation log already concedes this).
2. **Condition names.** 047 section 4 lists "Affective and Full" conditions; 062 sections 1 and 2.2 list None, Cognitive, Affective only, and omit Full. Source check: food sharing and grid have None, Cognitive, Affective and Full (Appendix D compares Affective and Full); the 2-D field has only None, Cognitive, Affective. **Not a real contradiction**: both are right for their environments, but 062 section 2.2 should say a Full condition exists in food sharing and grid. The 047 "unresolved" flag is resolved by this.
3. **Cross-reference slip in 062 section 7.** It cites "section 5 of 047's Neumann-series suggestion". The Neumann-series remark is in 047 section 4 item 5; 047 section 5 is Juechems & Summerfield. **047 is right**; correct the pointer to "047 section 4, item 5".
4. **Scope of the Monderer-Shapley use (minor, unresolved in file)**. 23 section 9 states the improvement-path convergence results for finite games; 062 section 5.1 applies "better-response and gradient dynamics converge" to a continuous quadratic game. The conclusion holds here by the explicit spectrum (also in 062), so the result stands, but the potential-game route is cited beyond the finite-game statement in 23. Not tested at source.
5. **Hughes et al. (file 23, 048) vs 062 section 3.4(4)**. Hughes' inequity term acts on temporally smoothed rewards (e_j^t = γλe_j^{t−1} + r_j^t), so it is not a function of the joint drive state at one time. 062's claim that the identity holds "verbatim" applies to 062's own drive-level F-S form, not to Hughes' shaped reward. 062 does not cite Hughes, so no direct conflict; flagged to prevent the two being conflated. Also 062's symmetric λ·|D_i − D_j| is the α = β special case of F-S (23 sets α = 5, β = 0.05 for Hughes' best sweep).

### Not covered elsewhere

Rosen 1965, Bergstrom-Blume-Varian 1986 and Becker 1974 appear in no other file; the 062 claims about them (and the "does not exist" list in section 8) have no cross-check here and remain as in section 9.

## Licences of quoted and transcribed material (2026-10-30)

No passages were removed or shortened in this file; every quotation is under 60 words and attributed. Licences are recorded below as the audit required.

- Yoshida & Man 2024, arXiv 2412.12103 (Section 1 bullet, repeated at sections 6 and the cross-checks): licence not determined; publisher copyright presumed (arXiv licence not stated in the file). Use: short quotations (3 to 18 words each) and one restated equation (`D = D_possessor + w D_partner`), plus numeric values from the experiments.
- Bergstrom, Blume & Varian 1986, J. Public Economics 29:25-49: not determined; publisher copyright presumed. Use: citation only. The 8-word phrase in quotation marks in sections 8 and 9 ("altruism narrows but does not close the gap") is this file's own wording, not a verified quotation from the paper, which was never opened; read it as a paraphrase and do not cite it as a quotation.
- Yoshida & Man 2025 (arXiv 2506.12894), Keramati & Gutkin 2014 (eLife 3, doi:10.7554/eLife.04811), Rosen 1965, Monderer & Shapley 1996, Becker 1974, Fehr & Schmidt 1999, Hughes et al.: not determined; publisher copyright presumed (the eLife paper is likely open access, licence not checked). Use: citations and restated equations or results only; no quotation or table transcription.
