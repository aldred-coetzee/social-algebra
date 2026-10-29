# Prior work 090: which passivity, small-gain and contraction results survive asymmetric influence

Direction: D028 (deep-read, batch 2). Date: 2026-10-29. Survey for the social-algebra strand. Follows file 40 (sections 4, 4b, 4c, 5, 6), which stated these theorems from standard accounts; this file reads sources.

**Provenance summary.** Tags: [read] = I fetched the full text and read the passage cited; [sa] = standard account or abstract only, not usable for an equation. Read in full or in the relevant sections, as downloaded PDFs (pdftotext): Proskurnikov & Tempo Part I (arXiv:1701.06307) and Part II (arXiv:1801.06719); Dashkovskiy, Rüffer & Wirth (arXiv:math/0506434, v1 2005 preprint of the 2007 paper); Yue & Zelazo 2025 (arXiv:2508.21428) and the balanced-digraph paper (arXiv:2411.05933v3); Wankhede, Mandal, Martínez & Tallapragada (arXiv:2404.04912v2); Song, Slotine & Pham (arXiv:2311.03669, for the restated combination rules); Bai, Arcak & Wen, ACC 2008, which restates Arcak 2007 (open copy). **Not readable (paywalled, no open copy found after Semantic Scholar, Unpaywall, search for author pages and arXiv): Arcak 2007 (IEEE TAC), Russo, di Bernardo & Sontag 2013 (IEEE TAC), Lohmiller & Slotine 1998 (Automatica), Slotine 2003.** Those stay [sa]; for Russo only the abstract was read (Semantic Scholar record). Unpaywall reports both TAC papers `is_oa: false`.

**Headline.** The three tools differ sharply in what asymmetry does to them.
1. **Small-gain / ISS network theorem: survives asymmetry untouched.** The condition is on a nonnegative (non-symmetric) gain matrix and says nothing about reciprocity. [read]
2. **Contraction via a row-sum (infinity) log-norm: survives asymmetry untouched, and also survives signed, antagonistic (negative) influence**, provided the antagonism is weak relative to self-anchoring. [read, Wankhede et al.]
3. **Passivity à la Arcak: does NOT survive.** It rests on the symmetric incidence structure E, Eᵀ of an undirected graph. On a directed graph the feedback path loses passivity unless the graph is balanced; for arbitrary digraphs only a 2025 extension with weaker (constrained) passivity exists. [read]
4. **The Proskurnikov & Tempo tutorials contain no passivity, small-gain or contraction result at all** (grep of full text: zero hits for "passiv", "small-gain", "contraction"). Their asymmetric-influence results are Perron-Frobenius, Markov-chain and Lyapunov arguments, and several break exactly where reciprocity is dropped (time-varying products, bounded confidence). Anyone citing them as a source for the three certificate families is citing the wrong paper. [read]

---

## 1. Arcak 2007: passivity for group coordination (restated, not read at source)

**Citation.** Arcak, M. (2007). Passivity as a design tool for group coordination. *IEEE Trans. Automatic Control* 52(8), 1380-1390. DOI 10.1109/tac.2007.902733 (Crossref-confirmed title, volume, pages). Book form: Bai, H., Arcak, M., Wen, J. (2011), *Cooperative Control Design*, Springer, DOI 10.1007/978-1-4614-0014-1 (not read). The paper itself: **paywalled, not read.**

**What I read instead.** Bai, He; Arcak, M.; Wen, J. (2008). Adaptive motion coordination: using velocity feedback to achieve parameter convergence. *Proc. 2008 American Control Conference*, 759-764, DOI 10.1109/acc.2008.4586584 (Crossref confirms title, authors and pages 759-764; open copy at skoge.folk.ntnu.no/prost/proceedings/acc08/data/papers/0987.pdf, re-read 2026-10-30). Its Section II.A restates "[10]" = Arcak 2007 (the framework and Arcak's Theorem 1, not its proof). This is the same group restating the framework, so I treat the following as [read] *of the restatement*, [sa] for Arcak's proof.

**Their vocabulary.** Agents i = 1..N, each a state-space block H_i; graph with N nodes and M links, incidence matrix D (N × M, entries +1 / −1 / 0); link difference variables z_k; target compact sets A_k; storage function S_i; "strictly passive".

**Operands / equations [read, restated].**
- Each agent: ẋ_i = y_i + v(t); H_i: ξ̇_i = f_i(ξ_i, u_i), y_i = h_i(ξ_i), with h_i(0) = 0 and f_i(0, u_i) = 0 ⇒ u_i = 0 (their (3)-(5)).
- Hypothesis: each H_i strictly passive with C¹, positive definite, radially unbounded storage S_i(ξ_i): Ṡ_i ≤ −W_i(ξ_i) + u_iᵀ y_i, W_i positive definite (their (6)).
- Coordination law: u_i = −Σ_k d_ik ψ_k(z_k), with ψ_k = ∇P_k(z_k), P_k ≥ 0 vanishing exactly on the target set A_k and growing unbounded at the boundary of the domain G_k (their (7)-(12)).
- Stacked: z = (Dᵀ ⊗ I_p) x; u = −(D ⊗ I_p) ψ(z) (their (15)-(16)).
- Group behaviours guaranteed [restated]: B1 every ẋ_i → v(t); B2 every z_k → A_k. Feasibility needs {A_1 × … × A_M} ∩ R(Dᵀ ⊗ I_p) ≠ ∅.
- The restatement says explicitly that the choice of link orientation does not change results *"because the information flow is assumed to be bidirectional"*.

- What the restatement says Arcak's **Theorem 1** proves: B1 and B2 are achieved with design (3), (4), (7), with region of attraction G = {(z, ξ) | z ∈ G₁ × … × G_M ∩ R(Dᵀ ⊗ I_p)}, **"when the following additional property holds": Property 1** — (D ⊗ I_p) ψ(z) = 0 and z ∈ R(Dᵀ ⊗ I_p) imply z ∈ A₁ × … × A_M (their (17)-(18)). Without Property 1 the trajectories go to the equilibrium set E = {ξ = 0, (D ⊗ I_p) ψ(z) = 0, z ∈ R(Dᵀ ⊗ I_p)}, which can contain undesired configurations. [read, restated]

**The structural reason it needs reciprocity (this file's gloss, not a statement in the sources).** The feedback path is u = −D ψ(Dᵀ x), i.e. a map of the form D Ψ Dᵀ. With ψ a gradient (hence monotone), D Ψ Dᵀ is a symmetric, passive interconnection; the whole theorem is then "passive blocks in feedback with a passive symmetric block". This is the structure the 2024-2025 papers (§2) say is lost for directed graphs.

**Theorems / predictions.** Convergence of group behaviour on a connected, bidirectional graph from strict passivity of members plus the coupling design, with no knowledge of the exact member models — **but reaching the target sets A_k needs Property 1 as well** (corrected 2026-10-30: this line previously said convergence followed "from passivity of members alone"). Arcak's own statement and proof [sa].

**Empirical standing.** Control engineering; no behavioural data. Nothing here is empirical about people.

**Group size.** N appears only through D and the connected-graph assumption; the result is stated for any N. The bound is not N-dependent in the restatement. Composition: members need only be passive and may differ ("heterogeneous"); group composition enters only through the graph being connected and bidirectional.

**Operand/operator translation.** Operand: a member as a strictly passive block with a storage function (a "deficit" that cannot be created from nothing). Operator: reciprocal diffusive coupling on a graph, with a potential P_k per relationship. **Costs:** reciprocity of influence is an assumption, not a derived property of social groups.

---

## 2. Passivity on directed graphs: Yue & Zelazo (2024/2025)

**Citations.** Yue, F.-Y., Zelazo, D. *A passivity analysis for nonlinear consensus on balanced digraphs*, arXiv:2411.05933v3 (25 Jun 2025), preprint submitted to *European Journal of Control*. Yue, F.-Y., Zelazo, D. *A passivity analysis for nonlinear consensus on digraphs*, arXiv:2508.21428v1 (29 Aug 2025), IEEE-conference format. Both preprints; I have not seen a peer-reviewed version. [read]

**Their vocabulary.** Digraph D = (V, E); incidence matrix E = Bₒ + Bᵢ (out- and in-incidence); out-Laplacian Lₒ = Bₒ Eᵀ; balanced = in-degree equals out-degree at every node; globally reachable node; agreement submanifold S = span(1); S-constrained passivity; compensation theorem.

**What they say about the classic framework [read].** The balanced-digraph paper: passivity-based analysis "relies heavily on the symmetric feedback interconnection of the incidence matrix in diffusively coupled networks"; the paper goes on to say that this confines the framework to undirected interconnections, that replacing one incidence matrix gives directed topologies but loses the diffusive coupling property, and that the feedback path may then fail to preserve passivity (paraphrase). Its abstract: passivity-based approaches "are generally not applicable to the directed linear consensus protocol". The second paper: "the research mentioned shares a common implicit assumption: that the underlying graphs of MANs are undirected."

**Equations [read].**
- Definition (digraph paper, Definition 1, eq. (4); the same inequality is Definition 2, eq. (3) in the balanced paper): V̇_i ≤ u_i y_i − ε_i y_i² − δ_i u_i² for a positive semidefinite storage V_i.
- Directed structure (digraph paper, eq. (3)): u = w − z = −Bₒ μ, ζ = Eᵀ y, with w = Bᵢ μ treated as an external input.
- Proposition 3 (balanced paper): for a graph with a globally reachable node, Lₒ and Lₒᵀ have the same kernel iff the graph is balanced. For a general digraph the smallest eigenvalue of sym(Lₒ) is negative, so "the feedback path may lose passivity, even though the edge controllers are output strictly passive."
- **Theorem 1 (balanced paper):** for a network (Σₒ, Π, G_b, w) with balanced digraph G_b and a globally reachable node, output-strictly-passive agents and the passivity conditions of its Propositions 4-5 met: if α ≥ max(Dₒ)/ε, where max(Dₒ) is the maximal out-degree of the graph, then the system is stabilised. The paper notes the result is only sufficient, and stabilises but "does not necessarily ensure average consensus".
- **Theorem 2 (digraph paper):** for a digraph with a globally reachable node, if an S-constrained storage Q(x) exists for the agent relation and a controller relation with storage W and constant ε > 0 satisfy wᵀ Proj_{S⊥}(y) ≥ Q̇ + Ẇ + ε‖Proj_{S⊥}(y)‖², then the network achieves output agreement. This is stated to work "with arbitrary digraphs and any passive agents".
- **Corollary 1 (digraph paper):** for integrator-like agents ẋ_i = u_i, y_i = h_i(x_i) with 0 ≤ h_i′ ≤ m and input-output-passive edge controllers, agreement holds if α ≥ max(Dₒ)·M/2 and γ λ₂ > M/2 with M = max(1, |1 − m|) (λ₂ enters through their (25), ‖Eᵀy‖² = yᵀ L y ≥ λ₂ ‖Proj_{S⊥}(y)‖² with L = E Eᵀ, i.e. the algebraic connectivity of the undirected graph underlying the digraph; traced 2026-10-30, the paper's own definition sentence is in a passage pdftotext garbled). The authors say the conditions are "merely sufficient" and necessity "is left as an open problem."

**Theorems or derived predictions.** Agreement on strongly asymmetric influence networks is certifiable by passivity only with (a) balanced digraphs and strict passivity, or (b) the weaker constrained passivity and a root-node (globally reachable node) condition. Note the conditions involve **out-degree**: the more people an agent influences, the larger the passivity index the coupling must have, so influence hubs are exactly what the bound penalises.

**Empirical standing.** None. Simulations only. Preprints, one group, 2025.

**Group size.** Entering via max(Dₒ) (maximal out-degree) and λ₂ in Corollary 1. In a complete graph max(Dₒ) = n − 1, so the required controller gain grows linearly in n; in a bounded-degree network it does not. [read, derived from the stated condition]

**Operand/operator translation.** Passivity survives asymmetry only conditionally: balanced influence (everyone is influenced by as many as they influence), or strictly weaker certificates. A leader/follower or broadcaster-audience network is not balanced and is outside Theorem 1 (it is inside Theorem 2 if there is a root node).

---

## 3. Small-gain / ISS for networks: Dashkovskiy, Rüffer & Wirth

**Citation.** Dashkovskiy, S., Rüffer, B. S., Wirth, F. R. (2007). An ISS small gain theorem for general networks. *Math. Control Signals Systems* 19, 93-122. DOI 10.1007/s00498-007-0014-8 (Crossref-confirmed). Read: arXiv:math/0506434v1 (21 Jun 2005 preprint; section numbering may differ from the journal). [read]

**Their vocabulary.** Subsystem i is ISS if |x_i(t)| ≤ β_i(|x_i(0)|, t) + Σ_j γ_ij(‖x_j[0,t]‖_∞) + γ(‖u‖_∞), β_i of class KL, γ_ij class K, γ_ii ≡ 0 (their (2.4)). Gain matrix Γ(s) = (Σ_j γ_ij(s_j))_i; a monotone map (s₁ ≥ s₂ ⇒ Γ(s₁) ≥ Γ(s₂)).

**Equations and results [read].**
- **Theorem 4 (small-gain for networks).** If each subsystem is ISS and there is D(s) = ((Id + α₁)(s₁), …, (Id + α_n)(s_n)), α_i ∈ K_∞, such that Γ∘D(s) ≱ s for all s ∈ ℝⁿ₊ \ {0}, then the interconnection ẋ_i = f_i(x_1..x_n, u) is ISS from u to x.
- **Corollary 7 (linear gains).** If ρ(Γ) < 1 for the nonnegative matrix Γ, the interconnection is ISS.
- **Two subsystems:** Γ = [[0, γ₁₂],[γ₂₁, 0]]; ρ(Γ) < 1 iff γ₁₂ γ₂₁ < 1. Nonlinear: γ₁₂∘(Id + α₂)∘γ₂₁∘(Id + α₁)(s) < s for all s > 0.
- **Feed-forward cascades of any length are ISS** (Γ strictly lower-triangular; condition satisfied for arbitrary α).
- **Counterexample (Example 12, as quoted):** the naive condition γ₁₂∘γ₂₁(s) < s alone is not sufficient in the nonlinear case; the robust "Id + α" slack is needed.
- Remark 8: for nonnegative Γ, ρ(Γ) < 1 ⇔ Γs ≱ s for all s ∈ ℝⁿ₊ \ {0}. The further equivalence with Γᵏ → 0 is in the list opening §4.2, not in Remark 8 (location corrected 2026-10-30).
- Remark 15: Γ is just a nonnegative matrix and may be associated with a directed graph G(Γ); irreducible ⇔ G(Γ) strongly connected. Nothing in the theorem assumes γ_ij relates to γ_ji.

**Theorems or predictions.** If the spectral radius of the influence-gain matrix is below one (ρ(Γ) < 1, linear gains), the network's response to external disturbance is bounded by a gain function and initial conditions are forgotten. **Corrected 2026-10-30:** this line used to call ρ(Γ) < 1 "a cycle-gain statement" (every directed cycle's gain product below one). That is not what the paper states and it is not equivalent: with summed linear gains, ρ(Γ) < 1 is strictly stronger than "every simple cycle product < 1" (e.g. a node sitting on two 2-cycles each of product 0.6 gives ρ² = 1.2 > 1 although each cycle is below one). The paper's conditions are ρ(Γ) < 1 (linear) and Γ∘D(s) ≱ s (nonlinear); no cycle condition is stated in the v1 text.

**What asymmetry does.** Nothing breaks. γ_ij ≠ γ_ji is the generic case. A pure one-way chain (a hierarchy) has ρ = 0 and is automatically stable. This is the opposite of passivity. **Costs:** sufficient only; the condition says nothing about what the stable state is, and ρ(Γ) < 1 means the influence loops taken together do not amplify — it forbids a self-reinforcing group (a mob, a panic) by assumption, so it can only certify de-escalation, not analyse escalation.

**Empirical standing.** None. No behavioural data; the gains γ_ij would have to be measured per dyad, and no measurement procedure for human influence gains exists in this source.

**Group size.** The theorem is stated for arbitrary n. Whether ρ(Γ) < 1 holds depends on n through the matrix: with uniform gain g and fully connected n, ρ = (n − 1) g, so the tolerable per-link gain falls as 1/(n − 1) [my arithmetic from Corollary 7, labelled as such]; for a hierarchy it does not depend on n. Composition enters via the graph of Γ.

**Operand/operator translation.** Operand: member with ISS gains from each other member. Operator: the directed influence graph with gain matrix Γ. Theorem: "the gain matrix does not amplify (ρ(Γ) < 1, or Γ∘D(s) ≱ s) ⇒ group is ISS". Gives the form "if every member is ISS and the gain matrix is contractive in this sense then the group is ISS" (not "if every cycle gain is below one"; see the correction above).

---

## 4. Contraction: asymmetric and signed influence

### 4a. Wankhede, Mandal, Martínez & Tallapragada (opinion dynamics with contraction)

**Citation.** Wankhede, P., Mandal, N., Martínez, S., Tallapragada, P. Opinion dynamics for utility maximizing agents: exploring the impact of the resource penalty. arXiv:2404.04912v2 (9 Nov 2024), eess.SY. **Published** (found 2026-10-30): *IEEE Transactions on Control of Network Systems* 12(1), 5-17 (2025), DOI 10.1109/TCNS.2024.3510590 (Crossref-confirmed title, four authors, volume, pages). The text read is the arXiv v2; theorem numbers may differ in the journal version. [read in full where cited]

**Vocabulary.** Expressed opinion z_i, internal preference p_i, importance (stubbornness) w_i > 0, resources r_i > 0, **directed influence graph with real weights a_ik** (a_ik > 0 friend, a_ik < 0 enemy), strongly infinitesimally contracting.

**Equations [read].**
- Utility: U_i(z, p_i) = −(w_i/2)(z_i − p_i)² − (1/2) Σ_k a_ik (z_k − z_i)² − z_i⁴/(4 r_i) (their (1)).
- Dynamics (gradient ascent on own utility): ż_i = −w_i (z_i − p_i) + Σ_k a_ik (z_k − z_i) − z_i³/r_i (their (2)).
- Jacobian: J_ii = −w_i − Σ_{k≠i} a_ik − 3 z_i²/r_i; J_ij = a_ij.
- **Log-norm:** μ_∞(J(z)) = max_i [ −w_i + Σ_{k ∈ N_i^e} 2|a_ik| − 3z_i²/r_i ], N_i^e = the enemies of i. The friends' terms cancel.
- Definition 2.2: f strongly infinitesimally contracting on convex C with rate α if μ(J(z)) < −α for all z in C. Theorem 2.3 (cited from a monograph): then a unique globally exponentially stable equilibrium, with V = ‖z − z*‖.
- **Theorem 4.1 (ultimate boundedness):** opinions are ultimately bounded for all parameters, "does not depend on the type of interactions among agents or the structure of the social network."
- **Assumption A4 (weak antagonistic relations):** w_i > Σ_{k ∈ N_i^e} 2|a_ik| for every i. **Theorem 4.3:** under (A4), a unique globally exponentially stable equilibrium z* exists.
- **Theorem 5.1:** a consensus equilibrium exists iff all m_i (the unique root of S_i(z) = −w_i (z − p_i) − z³/r_i) are equal; so consensus requires preferences p_i of the same sign.
- **Theorem 6.4 (two agents):** with m₁ = m₂ = m and a₁₂(κ₂ − κ₁) − κ₁² > 0 (κ_i = w_i + 3m_i²/r_i), a Hopf bifurcation (periodic orbits) occurs at a₂₁ = a₂₁* = −(κ₁ + κ₂ + a₁₂). The proof uses the Hopf bifurcation theorem, not contraction. Lemma 6.2 (necessary): periodic orbits need a₁₂ < 0 or a₂₁ < 0, a₁₂a₂₁ ≠ 0, and a₂₁ + w₁ + w₂ + a₁₂ < 0. The text says oscillation appears only when at least one agent has an **antagonistic** influence on the other, "similar to the so-called boomerang effect".

**What asymmetry does.** The proofs use only the row-sum bound on J, so a_ik ≠ a_ki costs nothing. This is the cleanest [read] case of a compositional-style certificate that is indifferent to reciprocity. Asymmetry matters instead in the *behavioural* results: the Hopf point depends on the signed pair (a₁₂, a₂₁), and a non-reciprocal pair (one agent pursuing, the other fleeing) is the oscillator.

**Cost to flag.** The contraction proof gives only a *unique* equilibrium; it forbids the multistability that groups with real splits (factions, tipping) show, as file 40 §6 already says. The weak-antagonism condition w_i > Σ 2|a_ik| says: self-anchoring must beat total hostility received. It is a sufficient condition, not a boundary.

**Empirical standing.** Simulations only: a 6-agent network (Fig. 1-2) and the 2-agent Hopf example (Fig. 3). No dataset, no calibration. The model is cited for existence results, not fit.

**Group size.** Theorems 4.1, 4.3 are stated for any n; the A4 condition is per-agent and depends on n only via the sum of enemy weights. Consensus dominance weights σ_i and "price of anarchy" bounds (Thm 5.14, not read in detail) depend on the weights. Group composition: friends versus enemies enters through N_i^e only.

### 4b. Combination rules for contracting systems (Lohmiller & Slotine; Slotine 2003)

**Citation.** Lohmiller, W., Slotine, J.-J. E. (1998). On contraction analysis for non-linear systems. *Automatica* 34(6), 683-696, DOI 10.1016/s0005-1098(98)00019-3 (Crossref-confirmed); Slotine, J.-J. E. (2003). Modular stability tools for distributed computation and control. *Int. J. Adaptive Control and Signal Processing* 17(6), 397-416, DOI 10.1002/acs.754 (Crossref-confirmed). **Both paywalled, not read.** What I read: Song, B., Slotine, J.-J. E., Pham, Q.-C., *Stable Modular Control via Contraction Theory for Reinforcement Learning*, arXiv:2311.03669 (exact title confirmed against the arXiv record 2026-10-30). Section II-D restates the combinations, and attributes them to **Slotine 2003** (its ref. [14]: hierarchical form "Section 3.2 of [14]", feedback form "Section 3.4 of [14]"), not to Lohmiller & Slotine 1998.

**Restated rules [read, secondary].** Two subsystems with differential dynamics δż₁ = A₁₁ δz₁ + A₁₂ δz₂ and δż₂ = A₂₂ δz₂ + A₂₁ δz₁ (block form of their (8)-(11)), self-feedback blocks (11) and coupling blocks (10).
- **Hierarchical combination:** coupling block A₁₂ = 0 (one-way influence). Stable if each self-feedback block is stable and the other coupling is bounded.
- **Feedback combination:** coupling must satisfy A₁₂ = −A₂₁ᵀ (their (13), with the change of metric absorbed in transformations T_y, T_a). That is, **feedback combination is guaranteed only for skew-symmetric (reciprocal, opposite-signed) coupling.**

**What asymmetry does.** One-way (hierarchical) influence is fine and needs no gain condition beyond bounded coupling; mutual influence is guaranteed only when it is of the skew-symmetric form. A general non-reciprocal mutual influence falls outside both rules and falls back on the row-sum log-norm (§4a) or on a small-gain condition (§3).

### 4c. Russo, di Bernardo & Sontag (2013): paywalled

**Citation.** Russo, G., di Bernardo, M., Sontag, E. D. (2013). A contraction approach to the hierarchical analysis and design of networked systems. *IEEE TAC* 58(5), 1328-1331. DOI 10.1109/tac.2012.2223355. Erratum: IEEE TAC 67(8), 4384 (2022), DOI 10.1109/TAC.2022.3169895 (Crossref-confirmed 2026-10-30: "Erratum to 'A Contraction Approach to the Hierarchical Analysis and Design of Networked Systems'", same three authors; that it concerns the Section V example comes from a search result, not read). **Not read.**

**Abstract only [sa], read in the Semantic Scholar record:** "a result is established on the network structure and the properties of the individual component subsystems and their couplings to ensure the overall contractivity of the entire network. Specifically, it is shown that a contraction property on a reduced-order matrix that quantifies the interconnection structure, coupled with contractivity/expansion estimates on the individual component subsystems, suffices to ensure that trajectories of the overall system converge towards each other." Whether the reduced-order matrix has to be symmetric, and what class of coupling is allowed, I **cannot** say. Do not use this paper for an equation.

---

## 5. Proskurnikov & Tempo: what the standard social-network tutorials actually give for asymmetric influence

**Citations.** Proskurnikov, A. V., Tempo, R. (2017). A tutorial on modeling and analysis of dynamic social networks. Part I. *Annual Reviews in Control* 43, 65-79, DOI 10.1016/j.arcontrol.2017.03.002, arXiv:1701.06307. Part II: *Annual Reviews in Control* 45, 166-190, arXiv:1801.06719; DOI 10.1016/j.arcontrol.2018.03.005. **Corrected 2026-10-30:** this entry said Crossref's title for the Part II DOI reads "Part I"; re-queried, Crossref returns "A tutorial on modeling and analysis of dynamic social networks. Part II", vol. 45, pp. 166-190, so there is no metadata error to report. (The mislabel that does exist is in the arXiv PDF of Part I, 1701.06307v2, whose title line prints "Part II" while its abstract says "This paper is the first part of the tutorial".) [read, selected sections]

**Result for the strand: they contain no passivity, no small-gain and no contraction analysis.** A full-text search finds none; the tools are nonnegative-matrix theory, Markov chains, Lyapunov functions. Everything below is their asymmetry content.

**Equations / theorems [read].**
- French-DeGroot: x(k+1) = W x(k), W row-stochastic. Convergent iff all closed strong components of G[W] are aperiodic; consensus iff G[W] is quasi-strongly connected (directed spanning tree) with a single aperiodic closed component (Theorem 12). With positive self-weights w_ii > 0: always convergent; consensus iff directed spanning tree (Corollary 13). Convergence "does not depend on the weights w_ij, but only on the graph G[W]."
- Limit x(∞) = (p∞ᵀ x(0)) 1ₙ, p∞ the left eigenvector of W: the **social power** of each agent. It is non-uniform on asymmetric graphs.
- Abelson (continuous): ẋ = −L[A] x; consensus iff directed spanning tree (Theorem 16); limit p∞ᵀ x(0).
- Friedkin-Johnsen (Part II (43)-(44)): x(k+1) = ΛW x(k) + (I − Λ) u, u = x(0); if ρ(ΛW) < 1, x(k) → x̄ = (I − ΛW)⁻¹ (I − Λ) u.
- Stubborn sources (Corollary 14): s ≥ 1 stubborn agents reaching all others ⇒ convergence. The text before it says that with more than one stubborn agent "consensus among them is, obviously, impossible" (i.e. when they hold different opinions), and Part I §6 shows the final opinion is fully determined by the stubborn agents' opinions.
- **Where reciprocity is needed (Part II):** discrete time-varying products W(k) converge under Lemma 1, whose condition (c) is **type-symmetry in the sign sense**, w_ij(k) > 0 ⇔ w_ji(k) > 0; the continuous time-varying Abelson model converges under Lemma 5's **quantitative** type-symmetry K⁻¹ a_ji(t) ≤ a_ij(t) ≤ K a_ji(t), which the text says can be relaxed to cut-balance and then to non-instantaneous (integral) reciprocity (corrected 2026-10-30: the earlier line attached the K-bound to the discrete products); "in practice, the assumption restricting the interactions among the agents to be bidirectional (or reciprocal) often fails. The dynamics of matrix products without the type-symmetry assumption is a long-standing problem." Convergence of the time-varying Abelson model without reciprocity "remains a nontrivial problem".
- **Bounded confidence:** the Hegselmann-Krause (HK) model's proofs depend on symmetric interaction ("An important property … dramatically simplifying its analysis, is the symmetry of interactions"). Asymmetric intervals [x_i − d + η_i, x_i + d]: the model terminates in finite time if max η_i < d (Theorem 19), with termination time O(n³) + O(n²) ln(1 − ζ), ζ = η/d, and O(n³) in the symmetric case.
- **Signed (Altafini) model:** structurally balanced + directed spanning tree ⇒ polarisation; strongly connected + structurally imbalanced ⇒ stability to zero; otherwise convergence into clusters (Theorem 29). Their 3-agent example (a₁₂ = a₂₁ = −1, a₃₁, a₃₂ > 0) has equilibrium line (ξ, −ξ, ρξ) with ρ = (a₃₁ − a₃₂)/(a₃₁ + a₃₂): neither polarisation nor stability. Structural balance in the cited theory is defined for **sign-symmetric** graphs (friendship and enmity symmetric); Lemma 25: a structurally balanced graph is sign-symmetric.

**Empirical standing, blunt.** The one empirical sentence is: "Numerous experiments with small and medium-size group [84, 85, 205, 206] have confirmed the predictive power of the FJ model, in particular, (44) gives a good approximation for the real distribution of final opinions." That is the authors' summary of other people's experiments; I did not read those experiments and the tutorial gives no effect sizes, sample sizes or out-of-sample tests. [read as a claim; the evidence itself is [sa]]. Everything else is mathematics.

**Group size.** Convergence/consensus conditions are graph conditions (no n). The HK termination bound is polynomial in n (n³). FJ has been tested on "small and medium-size" groups per the authors. Composition: stubborn agents, strong components and the number of root nodes determine the outcome.

**Scale.** Group-scale and crowd-scale opinion (adoption/consensus), not membership.

---

## What changes with group size (n), collected

- Passivity on digraphs (Yue-Zelazo): required controller gain scales with max out-degree, so with n in a dense group, not in a sparse one.
- Small-gain: ρ(Γ) < 1; per-link tolerable gain ∝ 1/(n−1) in a dense uniform network (my arithmetic), independent of n in a hierarchy.
- Contraction row-sum (Wankhede): condition is per-agent, depends on n only through total enemy weight.
- DeGroot/Abelson: graph conditions, no n.
- Bounded confidence: termination time O(n³).
Nothing in the sources states a result for a particular n, a threshold group size, or a dependence of the *drive* parameters on n. Group composition (friends/enemies, stubborn vs susceptible, root vs non-root) enters through graph structure and signed weights, never through psychological type.

## Scale and consent, collected

Every result is a **theorem about an assumed model**; none is an empirical result about humans except the secondary FJ sentence. Scale: opinion/consensus at group or crowd level; none addresses join/stay/leave. Intervention: the control-theory papers "steer" by designing the controller (the coupling law), i.e. the designer chooses the feedback; whether the agents consent is outside the model. In the stubborn-agent results the stubborn source steers everyone downstream without any consent mechanism, which is manipulation by construction (Corollary 14: the final opinion is fully determined by the stubborn agents).

---

## Does it reduce to a drive basis?

Honest reading from what I read:

- **Reduces to drives, partially:** Wankhede et al. is the only source here that writes the agent as a drive-like object: utility with a preference term (stubbornness w_i toward p_i), a social term, and a resource penalty; opinion dynamics as gradient ascent on it. The "drive" is "stay near my own preference" with strength w_i; influence is a second term. Passivity's storage function (Arcak/Bai) can be read as a deficit-like quantity, but nothing in the sources identifies it with a named drive; that mapping is my proposal from file 40, not theirs.
- **Does NOT reduce to drives:** (a) the small-gain and contraction guarantees are properties of the *coupling structure* (cycle gains, row sums, graph connectivity) and hold for any dynamics with the right gains; the drive content of a member plays no role beyond supplying a number (γ_ij, w_i). (b) The Proskurnikov-Tempo models (DeGroot, Abelson, HK) have no drive: an agent is a weighted average of neighbours. FJ has a single anchor (u = x(0)), which is a stubbornness/drive-like parameter but is not derived from anything. (c) Social power p∞ is a structural property of the graph, not a drive of any member. (d) Antagonism (negative a_ik) is imported as a sign; no source derives enmity from a drive such as threat.
- **Conclusion for the hypothesis:** drives are not *needed* for these theorems; they are one possible interpretation of the node parameters. The theorems hold for any node model meeting the certificate. This weakly supports "drives as primitives" only in the sense that nothing here contradicts it, and weakly counts against it in the sense that the main compositional results are drive-blind.

## What does it predict or control, and how well?

- **Predicts (mathematically):** convergence, boundedness, uniqueness of an equilibrium, forgetting of initial conditions, final consensus value (via p∞ or via FJ's (I − ΛW)⁻¹ (I − Λ) u), and oscillation onset (Hopf at a₂₁ = −(κ₁ + κ₂ + a₁₂)). These are model-internal.
- **Controls:** by design of the coupling law (Arcak, Yue-Zelazo) to a target configuration; this is engineering of artificial agents. By stubborn agents the final opinion is determined (Corollary 14).
- **Out-of-sample evidence:** none found in anything I read. The one claim is the secondary FJ sentence above, unquantified ("good approximation"), from experiments I did not read. No effect sizes anywhere.
- **Failures and limits [read]:** passivity fails or needs new machinery on non-balanced digraphs (the authors' own statement); contraction forbids multistability; small-gain forbids self-amplification and is only sufficient; time-varying and bounded-confidence results mostly assume reciprocity or give only partial results without it; nonlinear naive small-gain condition fails without slack (Example 12). Wankhede et al. is simulation only (a 6-agent network and a 2-agent example).
- **Nothing here controls or predicts the behaviour of real people at any scale.**

---

## What exists versus what does not

**Exists [read]:** a small-gain theorem for n subsystems with a non-symmetric gain matrix; a row-sum contraction proof for directed signed opinion dynamics; the statement from two independent sources (Yue-Zelazo, and Bai et al.'s own restatement) that classic passivity coordination assumes bidirectional information flow; a 2025 passivity extension to balanced and to general digraphs with a root node; a DeGroot/Abelson/FJ literature giving graph-conditions for asymmetric influence; a Hopf-bifurcation result (proved with the Hopf theorem, not contraction) for two non-reciprocal agents in the same model whose equilibrium is contraction-certified.

**Does not exist (in what I read or found):** any passivity/small-gain/contraction result for *drives*, motivation or emotion; any estimate of a human ISS gain γ_ij (narrowed 2026-10-30: interpersonal influence *weights* w_ij of the linear FJ model have been elicited from people, by chip-allocation in dyad/triad/tetrad experiments, per Friedkin & Johnsen 2011, *Social Influence Network Theory*, ch. 4 — [sa], from search results, not read; a linear influence weight is not an ISS gain, but it is the nearest measured quantity); any empirical test of a cycle-gain condition on real groups; a necessary-and-sufficient passivity condition on digraphs (the authors say open); a general contraction result for non-reciprocal *mutual* influence with multistability.

## Unconfirmed

- Arcak 2007's own theorem statements and proofs (paywalled): all claims about it rest on the Bai-Arcak-Wen restatement and on Yue-Zelazo's description.
- Russo, di Bernardo & Sontag 2013: only the abstract; whether its reduced-order matrix requires symmetry is unknown.
- Lohmiller & Slotine 1998 / Slotine 2003 combination theorems: seen only through Song et al.'s paraphrase; the A₁₂ = −A₂₁ᵀ feedback rule may be a sufficient special case rather than the full theorem.
- Dashkovskiy et al.: I read the 2005 arXiv v1, not the 2007 journal version; theorem numbers may differ.
- Yue-Zelazo (both) and Song et al.: arXiv preprints; no journal version found. Wankhede et al. is published (TCNS 2025, see §4a) but the journal text was not read; numbering is from arXiv v2.
- Arcak's Theorem 1 as stated in Arcak 2007 itself, including whether Property 1 is a hypothesis of the theorem or of its region-of-attraction clause: known only through Bai-Arcak-Wen's restatement.
- Slotine 2003's feedback-combination rule: the A₁₂ = −A₂₁ᵀ form is Song et al.'s restatement after metric transformations T_y, T_a; whether Slotine 2003 allows a positive scaling (−k A₂₁ᵀ) or a general metric is not checked.
- FJ "numerous experiments … confirmed" ([84, 85, 205, 206] in Part II): the cited experiments not read; follow-ups would be Friedkin & Johnsen 1990/2011.
- The Russo 2022 erratum: DOI now Crossref-checked (TAC 67(8):4384); its content, not read.
- The per-link 1/(n−1) small-gain tolerance and the "max out-degree = n−1 in a complete graph" scaling are my arithmetic from the stated conditions, not claims in the sources.

## Validation log (2026-10-30)

- ✓ Arcak 2007, IEEE TAC 52(8):1380-1390, DOI 10.1109/tac.2007.902733 — Crossref confirms; still paywalled (no open copy found), claims stay [sa] for Arcak's own text.
- ✓ Bai, Arcak & Wen 2011, *Cooperative Control Design*, DOI 10.1007/978-1-4614-0014-1 — Crossref confirms; not read.
- ✎ Bai, Arcak & Wen 2008, ACC, 759-764, DOI 10.1109/acc.2008.4586584 — pages now Crossref-confirmed; re-read open copy; added Property 1 to the restated Theorem 1 (convergence to the target sets is not from passivity alone).
- ✎ Yue & Zelazo, arXiv:2411.05933v3 — authors, quotes, Prop. 3, Theorem 1 confirmed; equation numbers (3)/(4) belonged to the other paper, reattributed.
- ✎ Yue & Zelazo, arXiv:2508.21428v1 — quotes, Theorem 2, Corollary 1 confirmed; λ₂ traced to L = E Eᵀ via their (25).
- ✎ Dashkovskiy, Rüffer & Wirth 2007, MCSS 19(2):93-122, DOI 10.1007/s00498-007-0014-8 — Crossref confirms; (2.4), Thm 4, Cor 7, Rem 8, Ex 12, Rem 15, cascade and n = 2 results confirmed in arXiv v1; removed the "cycle-gain" reading of ρ(Γ) < 1 (not stated, not equivalent); Γᵏ → 0 equivalence relocated to §4.2.
- ✎ Wankhede, Mandal, Martínez & Tallapragada — (1), (2), Jacobian, μ∞, Def 2.2, Thm 2.3 (Bullo monograph), A4, Thms 4.1, 4.3, 5.1, 6.4 confirmed in arXiv v2; found published as IEEE TCNS 12(1):5-17 (2025), DOI 10.1109/TCNS.2024.3510590 (Crossref); Hopf result is not contraction-based; simulations are 6-agent and 2-agent.
- ✎ Song, Slotine & Pham, arXiv:2311.03669 — exact title confirmed; restated rules confirmed and attributed to Slotine 2003 §§3.2, 3.4, not Lohmiller & Slotine 1998.
- ✓ Lohmiller & Slotine 1998, Automatica 34(6):683-696 — Crossref confirms; paywalled, not read.
- ✎ Slotine 2003, IJACSP 17(6):397-416, DOI 10.1002/acs.754 — Crossref confirms; full citation added; paywalled, not read.
- ✓ Russo, di Bernardo & Sontag 2013, IEEE TAC 58(5):1328-1331 — Crossref confirms; no open copy found; abstract only.
- ✎ Russo et al. erratum, DOI 10.1109/TAC.2022.3169895 — Crossref confirms TAC 67(8):4384; moved from unconfirmed to confirmed (content unread).
- ✎ Proskurnikov & Tempo Part I, ARC 43:65-79 — Thms 12, 16, Cors 13, 14 and quotes confirmed; zero hits for passiv/small-gain/contraction confirmed.
- ✎ Proskurnikov & Tempo Part II, ARC 45:166-190 — removed the claimed Crossref "Part I" title error (Crossref reads Part II); type-symmetry conditions separated (Lemma 1 sign form, Lemma 5 K-bound); Thm 19, Thm 29, Lemma 25, Altafini example, FJ (43)-(44) and the experiments sentence confirmed; zero hits for passiv/small-gain/contraction confirmed.
- ? Friedkin & Johnsen 2011 (chip-allocation influence weights) — added as [sa] from search results to narrow a "does not exist" claim; not opened.

Sources opened: 9 primary texts (Proskurnikov & Tempo I and II; Dashkovskiy et al. v1; Yue & Zelazo ×2; Wankhede et al. v2; Song et al.; Bai, Arcak & Wen ACC 2008), plus 12 Crossref records and the arXiv metadata API.

Verdict: The file is substantially accurate and honest about provenance: every cited work exists with the stated authors, every quotation checked is verbatim, and the paywalled works are correctly left [sa]. Two substantive errors were fixed — ρ(Γ) < 1 was misread as a per-cycle gain condition, and Arcak's convergence was overstated as following from member passivity alone (it also needs Property 1) — along with a false Crossref-error claim, a conflated type-symmetry condition, a mis-attributed contraction rule, and the published status of Wankhede et al. No fabrications found.


## Cross-checks (2026-10-30)

Scope: this file checked against the other prior-work files for the same works, authors, equations and numbers. Only the files named below were read, and the sentences checked are the ones quoted. Nothing here was re-read from the sources themselves. Paywalled works stay [sa] as in the body.

**Agreements.**
- Passivity coordination on Arcak's framework assumes reciprocal information flow: 090 §1 (Bai, Arcak & Wen restatement); 040 §4c (abstract, from search); 044 (Arcak entry in the validation section, "both identify reciprocity as the cost").
- Proskurnikov & Tempo Part II: publication details (ARC 45, pp. 166-190, DOI 10.1016/j.arcontrol.2018.03.005) match 063 §1. Theorem 12 (DeGroot convergence) and Corollaries 13 and 14 match 063 §3.1 and its validation log. Theorem 19 (asymmetric bounded-confidence termination) matches 063 §3.
- Friedkin-Johnsen as a single anchor: 090 (FJ fixed point (I − ΛW)⁻¹(I − Λ)u) and 063 §3.2 (x(t+1) = G x(0) + (I − G) A x(t)) describe the same model. 063 notes the notation differs between Hegselmann-Krause and P&T.
- The FJ "validated for small and medium-size groups" sentence is quoted the same way in 090 §5 and 063 §3.2, from P&T 2017 §6.
- Dashkovskiy, Rüffer & Wirth 2007 publication details (MCSS 19(2), 93-122, DOI 10.1007/s00498-007-0014-8): 040 §5 and 044 §5c agree.
- Signed (Altafini) model, 090 §5 Theorem 29 (structurally balanced with a spanning tree gives polarisation): consistent with 085 §4 (Altafini: polarisation into two camps iff balanced and connected). 085 also records the Cartwright-Harary (sign-symmetric) versus Heider distinction, which 090 §5 states as "sign-symmetric".
- The 3-agent signed example, 090 §5 with ρ = (a₃₁ − a₃₂)/(a₃₁ + a₃₂), matches 085 §4's Proskurnikov-Matveev-Cao Example 1 for positive a₃₁, a₃₂. 085 writes |a₃₁| + |a₃₂| in the denominator, which only matters when the signs differ.
- Russo, di Bernardo & Sontag 2013 (DOI 10.1109/tac.2012.2223355) and Lohmiller & Slotine 1998 (DOI 10.1016/s0005-1098(98)00019-3) agree across 040, 044 and 090.

**Contradictions.** The two sources are listed with file§ and a verdict. Verdicts are "settled" only where this file's validation log (2026-10-30) read the primary source.

1. Dashkovskiy et al. condition wording. 040 §5 says the gain matrix must satisfy a "no cycle amplifies" condition; 044 §5c says "gain operator not amplifying around any cycle". 090 §3 says the v1 text has no cycle condition, and ρ(Γ) < 1 is not equivalent to every cycle gain being below one. **Verdict: settled by 090's validation log (v1 read).** The 040 and 044 wording is loose and should be replaced by "Γ(s) ≱ s" when either file is next edited.
2. Feedback combination of contracting systems. 040 §4b and §6 say feedback combinations are contracting under a bound on the coupling, with skew-symmetric coupling unconditional. 044 §5d says "(conditioned) feedback". 090 §4b, from Song et al.'s restatement of Slotine 2003, says feedback is guaranteed only for A₁₂ = −A₂₁ᵀ. **Verdict: unresolved.** Neither Lohmiller & Slotine 1998 nor Slotine 2003 was read; 090's Unconfirmed list says the skew-symmetric rule may be a sufficient special case.
3. Attribution of the combination rules. 040 §4b and 044 §5d attribute the parallel, series and feedback rules to Lohmiller & Slotine 1998 §3. 090 §4b says Song et al. attribute the restated rules to Slotine 2003 §§3.2 and 3.4, not to 1998. **Verdict: unresolved.** Both papers are paywalled. This is an attribution question only, and it has no effect on the form of the result.
4. Arcak's convergence claim. 040 §4c says the coordination result holds "robust to time-varying topology" and needs only passive members on a symmetric graph. 090 §1 says reaching the target sets also needs Property 1. **Verdict: settled by 090's validation log** (Bai, Arcak & Wen 2008 read in full, Property 1 confirmed). The "robust to time-varying topology" phrase in 040 was not checked by this file and is not confirmed.
5. Russo et al. network scope. 040 §6 says Russo et al. give conditions for networks of contracting nodes with hierarchical interconnection. 090 §4c read only the abstract, which mentions a reduced-order matrix. **Verdict: unresolved, not checkable from what was read.** It is not a contradiction of content, only of what was verified.

**Terminology, not a contradiction.** 063 §3.1 uses "contraction property" for the convex-hull monotonicity of P&T 2017 (min non-decreasing, max non-increasing). That is not contraction theory in the sense of §4 here. Use "convex-hull monotonicity" in 063 if that file is next edited.

**Cross-file gap.** Yue & Zelazo, Dashkovskiy's Corollary 7 linear form, and Wankhede et al.'s μ∞ and A4 conditions appear only in this file. 040 cites Wankhede in a reference line without stating its result, so no duplicate exists.

## Licences of quoted and transcribed material (2026-10-30)

No tables, figures or datasets are transcribed; equations are restated, not copied with surrounding text.

- Yue & Zelazo, arXiv:2411.05933v3 and arXiv:2508.21428v1: arXiv preprints; licence not determined (arXiv permits distribution under author-chosen licences, not recorded here); publisher/author copyright presumed. Use: short quotations (each under 60 words; the first shortened in the 2026-10-30 audit, the rest paraphrased) and restated definitions and theorems.
- Bai, Arcak & Wen, ACC 2008 (restating Arcak 2007): not determined; publisher copyright presumed. Use: short quotations and restated theorem. Arcak 2007 itself was not read or quoted.
- Dashkovskiy, Rüffer & Wirth, arXiv:math/0506434v1: licence not determined; copyright presumed. Use: restated condition and theorem, one short quotation.
- Wankhede, Mandal, Martínez & Tallapragada, arXiv:2404.04912v2: licence not determined; copyright presumed. Use: short quotation, restated theorems.
- Song, Slotine & Pham, arXiv:2311.03669: licence not determined; copyright presumed. Use: restated combination rules.
- Proskurnikov & Tempo, arXiv:1701.06307 and arXiv:1801.06719: licence not determined; copyright presumed. Use: short quotations and restated theorems.
- Russo, di Bernardo & Sontag 2013 (abstract via Semantic Scholar record): publisher copyright presumed. Use: short abstract quotation.
- Lohmiller & Slotine 1998; Slotine 2003; Arcak 2007: paywalled, not read; citation only.
