# Prior work 060: n-actor and network extensions of dyadic models

Direction: D190

Date: 2026-10-29. Kind: survey. Question: what is known about fixed points, stability and synchrony of the dyadic coupling models (file 20) as functions of the number of actors n and the network structure.

**Method and honesty note.** Read at source in full this session (PDFs downloaded and text-extracted): Fernández-Rosales, Liebovitch & Guzmán-Vargas 2015 (PLOS ONE); Alderisio, Fiore, Salesse, Bardy & di Bernardo (arXiv v4 of the Sci. Rep. paper); Marvel, Kleinberg, Kleinberg & Strogatz (arXiv 1010.1814, the preprint of the PNAS paper; the PNAS text itself was not opened); Bielczyk, Foryś & Płatkowski section 5 (arXiv 1202.2338). Liebovitch et al. 2008 was read in file 20, not re-read here. Everything tagged [std] is standard textbook content from my background, not checked this session. Tags: **[read]** read at source; **[abs]** abstract or search summary; **[std]** standard account; **[derived]** my own calculation from a stated equation, not in the source. DOIs confirmed on Crossref unless listed in Unconfirmed.

Cross-references: file 20 (dyadic skeleton, Liebovitch 2008, Bielczyk delay triad, HKB, Boker), file 40 (compositional dynamics), file 29 (animal collective behaviour).

## Summary

1. **The n-actor literature in psychology is thin and almost entirely numerical.** The one direct network generalisation of a dyadic drive-coupling model with equations is Fernández-Rosales et al. 2015 (Gottman-Liebovitch skeleton on a small-world network). It has no fixed-point or stability analysis, one parameter setting (m = 2, |c| = 3), and no data. The 2008 "3-10 actors" result in file 20 is the only other n > 2 result in that skeleton.
2. **The strongest n-actor result with human data is not a drive model at all:** Alderisio et al. 2017 put 7 people on four visual-coupling graphs and fit a Kuramoto network. The graph ordering of synchrony (complete and star above ring and path) was reproduced, but with the coupling constant fitted separately to each group (1.25 and 4.40), n = 7 and two groups.
3. **The one real theorem about many actors with signed ties is Marvel et al. (dX/dt = X squared):** for generic symmetric initial X, finite-time blow-up into rank one, i.e. two factions, with the faction partition given in closed form by the signs of the leading eigenvector. It is a relation-state model (the operand is the tie, not a person's drive), and its factions are a prediction about ties, not about behaviour.
4. **What is missing, bluntly:** a general stability criterion for the Gottman-Liebovitch skeleton on an arbitrary graph, any fit of an n-person drive model to data, and any model where the coupling graph is itself driven by the drives (adaptive networks of opinions do exist, see section 6). A simple sufficient stability condition falls out of Eq. 1 of the 2015 paper by linearising (section 6, [derived]); the conflict-model papers do not state it, but Eq. 1 has the form of a continuous Hopfield network and of signed saturating opinion dynamics, where the same linearisation is standard (validation note, section 6).

---

## 1. Fernández-Rosales, Liebovitch & Guzmán-Vargas 2015: the Gottman-Liebovitch skeleton on a small-world network

**Citation.** Fernández-Rosales I. Y., Liebovitch L. S., Guzmán-Vargas L. (2015). The Dynamic Consequences of Cooperation and Competition in Small-World Networks. *PLoS ONE* 10(4): e0126234. doi:10.1371/journal.pone.0126234 (Crossref pages not returned; DOI and the printed PDF confirm). Data: figshare "Conflict Model of Actors Network", figshare.com/articles/Conflict_Model_of_Actors_Network/1297891 (listed in the paper's data statement; I did not open it). This resolves the "title only" entry for the 2013 slides in file 20: the 2013 deck is the conference version (IPN repository, Fernandez_CCSIPN2013.pdf, not opened); the journal paper is the source.

**Their vocabulary.** Actors as nodes; "activity" x_i(t), glossed "emotional affect"; "inertia to neutral state"; "influence strength" c_j; cooperative actor (c_j > 0) and competitive actor (c_j < 0), following Deutsch (goals positively or negatively correlated); "strong feedback" (m < |c|); "coefficient of imbalance"; "global/local/neighbourhood distance".

**Drives/operands.** One scalar per actor (affect). No separate drive vector. Cooperation versus competition is a **sign attached to the source actor j**, not to the pair: every outgoing influence of j has the sign of c_j.

**Equations [read].**
- Eq. 1: dx_i/dt = −m_i x_i(t) + Σ_{j=1..N} a_ij c_j tanh(x_j(t)). m_i the relaxation coefficient; a_ij the adjacency matrix; c_j the influence strength of actor j. For convenience m_k = m > 0 and |c_k| = c for all k. "A strong interaction (or strong feedback) is attained if m < c."
- Network: Newman-Watts-Strogatz. Start from a ring with each actor joined to two nearest neighbours either side (degree 4), then add (not rewire) edges between random pairs with probability p ("no edges are rewired"). [Validation: the phrase "N k0 p is the mean excess connectivity" could not be found in the HTML text this pass; it may sit in an equation image. Kept, unverified.]
- r = N_{+c}/N, the fraction of cooperators (r = 0 all competitive, r = 1 all cooperative).
- Eq. 2: x+ = (1/N+) Σ_{x_i>0} |x_i|, x− = (1/N−) Σ_{x_i<0} |x_i|.
- Eq. 3: coefficient of imbalance φ = |x+ − x−| / (x+ + x−); 0 for a symmetric final distribution, 1 when all final states share a sign.
- Eq. 4: global distance δ_G = [2/(N(N−1)) Σ_{i>j} |x_i − x_j|] averaged over s realisations.
- Eqs. 5-6: local distance δ_L (over each node and its neighbours, including itself) and neighbourhood distance δ_N (neighbours only, so it relates to clustering).
- Simulation: m = 2, |c_j| = 3, x_i(0) uniform on [−1, 1], 4th-order Runge-Kutta over 50 × 10^3 steps, N = 512 in the showcase figures, 441 (p, r) grid points, 10 realisations for the distributions.

**Theorems or derived predictions.** None proved; the paper says "numerical simulations" throughout and gives no stability analysis. Reported numerical results [read]:
- Final states are independent of initial values (scatter of x(t_f) against x(t_i) shows "strips", no correlation).
- r near 0 or near 1 (one type dominates): broad, multi-peaked distribution of final states, "stable clusters" of like-valued neighbours (narrow bands when competitive, wider bands when cooperative), largest divergence between actors.
- r near 0.5: narrow, smooth distribution; many clusters stay unstable; smallest distances. The authors' explanation: in a cooperative-competitive dyad the 2008 two-actor model oscillates and then settles to a neutral value, so mixed neighbourhoods are pulled toward neutral. That is an argument by analogy, not a proof.
- High p and high r: φ near 1, because long-range links tie distant cooperators into one all-positive or all-negative block.
- δ_L and δ_N rise with p (long links create local disparity) and fall with r.
- Size: δ_G, δ_L, δ_N grow slowly for very small N then saturate, "all large systems, N > 256, have similar properties".
- Headline: for intermediate p, roughly equal numbers of cooperators and competitors give the narrowest distribution and the smallest local and global distances.

**Inconsistency worth knowing.** The text discussing Fig. 6 puts the smallest **global** distance at **p = 0** and r near 0.5 ("For global distance, we observe the smallest value when p = 0 and r ≈ 0.5"), while the closing summary says the effect is "for intermediate values of p". Local minima in δ_L, δ_N are "shallow". The headline (intermediate p) is therefore a trade-off claim between local and global measures, not a minimum of every measure. [read]

**Empirical standing.** None: pure simulation, one (m, c) pair, ten realisations per cell, no data. The abstract calls the findings "new testable predictions". No test found. No replication or sensitivity analysis to m/c, to other graph families, or to heterogeneous c_j magnitudes. Cited by later work not checked.

**Operand/operator translation.** Operand: actor with one scalar affect state. Operator: pairwise saturating influence tanh with a sign fixed by the sender. The sign-on-the-sender design means the model cannot express a pair who cooperate with each other and compete with a third party; that needs c_ij, an edge label. This is the main structural limitation to fix in any generalisation.

---

## 2. Liebovitch et al. 2008, summary of the n > 2 content (from file 20, not re-read)

Two-actor model x' = m1 x + b1 + c1 tanh(y) (and symmetric), pitchfork at c1 c2 = 1 (rescaled), Theorem 1 no limit cycles, and Section 3.7 numerics for 3-10 actors showing all-negative feedback splits the network into two opposed camps [read in file 20]. Doi 10.1016/j.physa.2008.07.020 (reconfirmed on Crossref this session). Follow-up with delay: Rojas-Pacheco, Obregón-Quintana, Liebovitch & Guzmán-Vargas (2013), "Time-delay effects on dynamics of a two-actor conflict model", *Physica A* 392: 458-467, doi 10.1016/j.physa.2012.09.021 (confirmed; title differs from the one given in file 20, which should be corrected). Two actors only.

---

## 3. Alderisio, Fiore, Salesse, Bardy & di Bernardo 2017: seven people on four graphs, Kuramoto fit

**Citation.** Alderisio F., Fiore G., Salesse R. N., Bardy B. G., di Bernardo M. (2017). Interaction patterns and individual dynamics shape the way we move in synchrony. *Scientific Reports* 7, article 6846. doi:10.1038/s41598-017-06559-4 (DOI confirmed on Crossref; article number corrected from 6847 to 6846 per the Crossref record in validation). Preprint arXiv:1607.02175 v4, read in full. Note: the Sci. Rep. abstract and the arXiv abstract word the result slightly differently (the journal stresses group homogeneity).

**Their vocabulary.** "Visual coupling", "interaction pattern", "group homogeneity" (spread of natural frequencies, coefficient of variation c_v), "individual/group/dyadic synchronisation index", "cluster phase (Kuramoto order parameter)".

**Drives/operands.** Not drives. Operand: a person's hand-oscillation phase θ_k and preferred frequency ω_k, measured eyes-closed. The "coupling" is a task instruction (look at these others).

**Design [read].** Two groups of seven (Group 1: closer natural frequencies; Group 2: more heterogeneous). Four graphs by gaze instruction: Complete (look at the centre, see everyone), Ring (see exactly two partners), Path (ring with one link cut, two end players with one partner), Star (peripheral players see only the central one, who sees all). Eyes-closed baseline trials (16 trials Group 1, 10 Group 2) and eyes-open trials of 30 s, 10 per topology. Phase by Hilbert transform.

**Equations [read].**
- Eq. 1: cluster phase q'(t) = (1/N) Σ_k e^{jθ_k(t)}, q(t) = atan2(Im q', Re q').
- Relative phase φ_k(t) = θ_k(t) − q(t); time average φ̄'_k = (1/T)∫ e^{jφ_k(t)} dt (Eq. 2).
- Eq. 3: individual synchronisation index ρ_k = |φ̄'_k| in [0, 1].
- Eq. 4: group synchronisation index ρ_g(t) = |(1/N) Σ_k e^{j(φ_k(t) − φ̄_k)}|; Eq. 5 its time average ρ_g.
- Eq. 6: dyadic index ρ^d_{h,k} from φ^d_{h,k} = θ_h − θ_k.
- Model (numbered (7) in the Methods though the text cites "equation (8)"): dθ_k/dt = ω_k + (c/N) Σ_{h=1..N} a_kh sin(θ_h − θ_k), k = 1..N, with a_kh = 1 if k and h look at each other, else 0; one coupling strength c for all, "set ... to match the values of group synchronisation indices ρ_g observed experimentally", c = 1.25 (Group 1) and c = 4.40 (Group 2).

**Results [read].**
- Experimental data (2 group × 4 topology mixed ANOVA, Greenhouse-Geisser): topology F(1.648, 19.779) = 29.447, p < 0.01, η² = 0.710; group not significant; **Group × Topology interaction significant**, F(1.648, 19.779) = 3.908, p < 0.05, η² = 0.246, the topology effect stronger in the less homogeneous Group 2 (its Path graph lowest). [added in validation, read]
- A 2 (group) × 4 (topology) mixed ANOVA on simulated data: topology effect F(3, 36) = 5.946, p < 0.01, η² = 0.331 (advantage for Complete); group effect not significant; **interaction not significant (F(3,36) = 0.163, p = 0.920)**. The authors state: "in its current form it fails in modulating the topology effect by variations in the group homogeneity".
- Experiment versus simulation: no effect of data origin (Group 1: F(1,12) = 0.206, p = 0.658; Group 2: F(1,12) = 0.619, p = 0.447); topology effect present in both; Complete and Star above Ring and Path (Bonferroni p < 0.01).
- Visually connected dyads synchronise most (the highest ρ^d for 99 % of participants in Group 1, 94 % in Group 2; t(117.970) = −8.872, p < 0.01).
- Correlation of individual frequency variability with synchrony index negative: Complete graph R = −0.69, p < 0.01 (model −0.88); Ring R = −0.14, p = 0.62 (model −0.66, p < 0.01); Path R ≈ 0, p = 0.83 (model −0.45); Star R = −0.45, p = 0.11 (model −0.55).
- Path graph: the more homogeneous group (Group 1) synchronised better.
- Model fails when frequencies are close and c is too high (Group 1 at c = 4.40) or frequencies are far and c is too low (Group 2 at c = 1.25).

**Theorems or derived predictions.** None proved here; the paper cites the network-science point that synchronisation depends on the structure of the interconnections to its refs [44, 45] (Albert & Barabási 2002, *Rev. Mod. Phys.* 74: 47-97; Newman, Barabási & Watts 2006, *The Structure and Dynamics of Networks*), and lists Arenas et al. 2008 as ref [46]. It does **not** cite Pecora & Carroll 1998 (corrected in validation; the MSF link is mine, [std]).

**Graph-theoretic check [derived, not in the paper].** Algebraic connectivity (second-smallest Laplacian eigenvalue λ2, the quantity that governs diffusive-coupling synchronisation [std]) for these four graphs at N = 7, unit weights: Complete 7.0, Star 1.0, Ring 0.753, Path 0.198 (computed this session). The ordering Complete > Star > Ring > Path matches the human ordering (Complete and Star above Ring and Path) without any fitted parameter, which is a stronger and cheaper statement than the paper's fitted-c ANOVA. The paper does not make it. Caveat: n = 7, four graphs, and the experiment separated only {Complete, Star} from {Ring, Path} (Bonferroni p < 0.01); Complete versus Star and Ring versus Path were not resolved, so this is one data point supporting a standard theorem, not a test of it. (Corrected in validation: the earlier text said Star versus Ring was not significant, which is the one ordering the paper did report.)

**Empirical standing.** One lab, two groups of seven, 30-second trials; physical motor task with no stakes, no emotion, no social relationship among participants (students in a lab). The authors' own limitations: groups differ in sex, weight, size, education, and "social factors and personality traits" are unmeasured; they report preliminary evidence from a computer-mediated (non-social) set-up that topology matters there too, which suggests the effect is largely kinematic coupling, not social. No replication found. The fitted c differs 3.5-fold between groups, so c is not a stable property of "people looking at each other"; this is the central weakness for using the model as an operator.

**Operand/operator translation.** Operand: phase and natural frequency (a person's own rhythm). Operator: sin(θ_h − θ_k) weighted by an adjacency a_kh (who attends to whom). Directed adjacency is the right object here (a_kh need not equal a_hk) though the study used symmetric graphs only. Natural frequency ω_k is the closest thing in the model to an individual "set point" in the file 20 skeleton, and heterogeneity of ω_k versus c is the standard order parameter for the onset of synchrony.

---

## 4. Kuramoto theory the above rests on (standard account; not read this session)

- Strogatz S. H. (2000). From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators. *Physica D* 143: 1-20. doi:10.1016/s0167-2789(00)00094-4 (confirmed). Acebrón J. A. et al. (2005). The Kuramoto model: a simple paradigm for synchronization phenomena. *Rev. Mod. Phys.* 77: 137-185. doi:10.1103/revmodphys.77.137 (confirmed). Arenas A., Díaz-Guilera A., Kurths J., Moreno Y., Zhou C. (2008). Synchronization in complex networks. *Physics Reports* 469(3): 93-153. doi:10.1016/j.physrep.2008.09.002 (confirmed, full author list confirmed on Crossref). Pecora L. M., Carroll T. L. (1998). Master stability functions for synchronized coupled systems. *Phys. Rev. Lett.* 80: 2109-2112. doi:10.1103/physrevlett.80.2109 (confirmed).
- [std] Mean-field Kuramoto dθ_i/dt = ω_i + (K/N) Σ_j sin(θ_j − θ_i); for a unimodal symmetric frequency density g the incoherent state loses stability at K_c = 2/(π g(0)), and partial synchrony grows continuously above it. The master stability function reduces synchronisation of identical coupled units on a network to the eigenvalues of the coupling Laplacian: stability depends on the **smallest non-zero eigenvalue (algebraic connectivity)** and, in some systems, the **eigenvalue ratio** (spread). These are the n- and structure-dependent theorems that exist and that the dyadic psychology models have not borrowed. (The [std] summary above is recollection in our own words, attributable to Strogatz 2000 and Acebrón et al. 2005 for Kuramoto and Pecora & Carroll 1998 for the master stability function; not copied from Wikipedia or any other article.)
- Direct empirical anchor for human crowds: Néda Z., Ravasz E., Brechet Y., Vicsek T., Barabási A.-L. (2000). The sound of many hands clapping. *Nature* 403: 849-850. doi:10.1038/35002660 (confirmed; contents not read, [std] recollection: audience clapping alternates between synchronised and incoherent states, with a period-doubling link to the rhythm).
- Group rocking chairs and cluster-phase measures: Richardson M. J., Garcia R. L., Frank T. D., Gergor M., Marsh K. L. (2012) "Measuring group synchrony: a cluster-phase method for analyzing multivariate movement time-series", *Frontiers in Physiology* 3: 405, doi:10.3389/fphys.2012.00405 (resolved and confirmed on Crossref in validation; reference [25] in Alderisio), and Frank T. D., Richardson M. J. (2010), "On a test statistic for the Kuramoto order parameter of synchronization: an illustration for group synchronization during rocking chairs", *Physica D* 239(23-24): 2084-2092, doi:10.1016/j.physd.2010.07.015 (resolved and confirmed on Crossref in validation; contents not read). Richardson et al. 2007, "Rocking together" doi:10.1016/j.humov.2007.07.002 (confirmed; in file 20).

---

## 5. Structural balance as a many-actor dynamics: Marvel, Kleinberg, Kleinberg & Strogatz

**Citation.** Marvel S. A., Kleinberg J., Kleinberg R. D., Strogatz S. H. (2011). Continuous-time model of structural balance. *PNAS* 108(5): 1771-1776. doi:10.1073/pnas.1013213108 (Crossref). Read: preprint arXiv:1010.1814, "Analysis of a continuous-time model of structural balance" (differences from the journal version not checked). The model comes from Kułakowski K., Gawroński P., Gronek P. (2005), "The Heider balance: a continuous approach", *Int. J. Modern Physics C* 16(5): 707-716, doi:10.1142/s012918310500742x (confirmed on Crossref in validation; not read, attribution [read] in the Marvel preprint).

**Their vocabulary.** Structural balance (Heider; Cartwright & Harary): a signed complete graph is balanced when each triangle has an odd number of positive edges; equivalently two factions (one possibly empty), positive inside, negative across. (Definition after Heider 1946 and Cartwright & Harary 1956; Harary 1953 for the two-faction form; our own wording, not copied from any encyclopedia article.)

**Operands.** The tie: X is a real symmetric n × n matrix, x_ij the friendliness (+) or unfriendliness (−) between i and j. The diagonal x_ii is read as self-approval. There are no drives and no persons-as-state.

**Equations [read].**
- Eq. 1: dX/dt = X². Entrywise Eq. 2: dx_ij/dt = Σ_k x_ik x_kj (friend-of-friend pushes ij positive; friend-of-enemy pushes negative).
- Solution: X(0) = Q D(0) Qᵀ with eigenvalues λ1 ≥ λ2 ≥ … ≥ λn; each eigenvalue obeys ℓ_k(t) = λ_k/(1 − λ_k t) (Eq. 3); equivalently X(t) = X(0)[I − tX(0)]⁻¹ (Eq. 4).
- Blow-up time t* = 1/λ1; X(t)/‖X(t)‖ → X* = ω1 ω1ᵀ (Eq. 5), the rank-one matrix of the leading eigenvector.

**Theorems [read].**
- If (1) λ1 > 0, (2) λ1 ≠ λ2, (3) all components of ω1 are nonzero, then the system blows up at t* = 1/λ1 with sign pattern given by the faction partition S = {k: ω1k > 0}, T = {k: ω1k < 0}: two internally friendly cliques joined by all-unfriendly ties. (2) and (3) hold with probability 1 for an absolutely continuous initial distribution; (1) holds with probability tending to 1 as n grows.
- For random symmetric initial matrices with entries independent and symmetric about a mean µ: **µ > 0 yields all-positive, µ ≤ 0 yields two cliques that split the network evenly.** The abstract draws the consequence that the initial amount of friendliness in large networks decides between "intractable conflict" and "global harmony".
- The n(n+1)/2 variables reduce to n via n(n−1)/2 constants of motion.

**Empirical standing.** The authors evaluate the model on empirical data, reported in the paper, but I did not read that section; I cannot say how well it fits. Blunt caveats: finite-time blow-up is a mathematical artefact (relationships do not diverge), so the model gives the **final sign pattern**, not magnitudes; it applies only to complete graphs; it uses symmetric ties, so it cannot express a one-way grievance; and the µ > 0 versus µ ≤ 0 threshold is a statement about random initial matrices, not about any measured group. The related discrete-time model is Antal, Krapivsky & Redner (2005), *Phys. Rev. E* 72, 036121, doi:10.1103/physreve.72.036121 (confirmed; contents not read): single-edge sign flips can get stuck in "jammed" unbalanced states, which Marvel et al. note as the motivation.

**Related theorem for consensus with antagonism.** Altafini C. (2013). Consensus problems on networks with antagonistic interactions. *IEEE Trans. Automatic Control* 58(4): 935-946. doi:10.1109/tac.2012.2224251 (confirmed). [abs, from search summaries]: for linear opinion dynamics with signed edge weights, convergence to a non-trivial consensus is possible if and only if the graph is structurally balanced, in which case the agents reach "bipartite consensus" (equal magnitude, opposite sign across the two camps); if not balanced the state converges to the origin. Not read at source. This is the clean theorem form of Liebovitch et al.'s "two opposed camps" numerical observation, for the linear case.

**Operand/operator translation.** Operand: a signed relation. Operator: the matrix product X² (composition of relations). That the update is literally the square of the relation matrix is the only place in this survey where the dynamics is itself a matrix-algebra operation, and it is the most directly "algebraic" object found. It does not take drives as inputs.

---

## 6. What follows from Eq. 1 of the 2015 paper by linearisation [derived]

None of this is stated in the paper; it is routine calculus on Eq. 1 and should be treated as a conjecture-grade note until checked.

- Eq. 1 has the origin as a fixed point (tanh(0) = 0). The Jacobian there is J = −m I + A C, with C = diag(c_j) and A the adjacency matrix (tanh'(0) = 1).
- The origin is locally stable iff all eigenvalues of A C have real part below m. A sufficient condition is that the spectral radius ρ(A C) < m.
- For |c_j| = c this gives the bound ρ(A C) ≤ c · ρ(A) ≤ c · k_max, where k_max is the maximum degree. In the paper's setting k_min = 4 (ring with two neighbours each side) and m = 2, c = 3, so for the all-cooperative network (A C = 3A, ρ = 3 × mean degree-ish ≥ 12) the origin is unstable by a wide margin, so the stable "strong feedback" regime the authors invoke is the instability regime of the origin. Their remark "strong interaction if m < c" is the dyadic version: with a single link the condition is c > m (rescaled c1 c2 > 1 in the 2008 notation).
- Boundedness: since |tanh| ≤ 1, x_i' ≤ −m x_i + c k_i and x_i' ≥ −m x_i − c k_i, so every trajectory enters and stays in the box |x_i| ≤ c k_i / m. This bounds the final-state spreads in Fig. 4-5 and is why increasing degree (p) widens the possible range of states.
- Consequence for the "mixed is calmest" finding: for r = 0.5 with random sign placement A C is a signed random matrix, whose spectral radius is typically smaller than the all-same-sign case (the all-positive case has a Perron eigenvalue at least the mean degree, equal to it only for a regular graph; corrected in validation). So the origin is **closer to stable** in mixed networks. This may explain the narrower final distribution at r = 0.5 more directly than the dyad-oscillation story; it predicts that the effect disappears when m is large relative to c k, and that it depends on the spectral radius of A C rather than on the ratio r as such. Testing this needs a rerun of the simulation with ρ(A C) computed; the code and the data are on figshare and not examined. Treat as a hypothesis.

**Validation note: this linearisation is not new outside the conflict-model papers.** Eq. 1, dx_i/dt = −m x_i + Σ_j a_ij c_j tanh(x_j), is the continuous-time graded-response network of Hopfield J. J. (1984), "Neurons with graded response have collective computational properties like those of two-state neurons", *PNAS* 81(10): 3088-3092, doi:10.1073/pnas.81.10.3088 (confirmed on Crossref), with weight matrix W = A C; stability of the origin from the spectrum of −mI + W is textbook there [std]. Signed networks with a saturating nonlinearity and a bifurcation of the neutral state set by adjacency eigenvalues are the subject of Bizyaeva A., Franci A., Leonard N. E. (2023), "Nonlinear opinion dynamics with tunable sensitivity", *IEEE Trans. Automatic Control* 68(3): 1415-1430, doi:10.1109/TAC.2022.3159527 (confirmed on Crossref; contents from background, not read this pass). Co-evolving (adaptive) networks where node states rewire ties exist for opinions, e.g. Holme P., Newman M. E. J. (2006), "Nonequilibrium phase transition in the coevolution of networks and opinions", *Phys. Rev. E* 74: 056108, doi:10.1103/PhysRevE.74.056108 (confirmed on Crossref; not read). So the claim stands only in the narrow form: the Gottman-Liebovitch conflict-model papers do not state it.

---

## 7. Triads and small n with equations (cross-check of file 20)

Bielczyk, Foryś & Płatkowski, *J. Math. Sociol.* 37: 223-249 (2013), doi:10.1080/0022250x.2011.597279 (confirmed). Section 5 read.
- Triad (Eq. 23): r' = a11 r + a12 j; j' = a21 r(t − τ) + a22 j + a23 p(t − τ); p' = a32 j + a33 p (Romeo and Paris do not interact directly). Eq. 24 is the variant with the delay on Juliet's self-term.
- **Reduction [read]:** in model (23), if the two men have the same self-attitude (a11 = a33 = a), setting s = a21 r + a23 p gives (their Eq. 25) j' = a22 j + s(t − τ), s' = (a12 a21 + a23 a32) j + a s, so Juliet interacts with an "averaged" man and **at most one stability switch** is possible. Their example of three switches, a11 = −28, a12 = −74, a21 = 76, a22 = −35, a23 = 76, a32 = −42, a33 = −28, is for **model (24)** (delay on Juliet's self-term), and note a11 = a33 there: equal self-attitudes do not rule out multiple switches in (24). (Corrected in validation: the earlier text said multiple switches need the men to differ and presented the example as if it did; the reduction holds only for (23).) The parameters have no empirical referent.
- Method for building n-switch triads from a dyad: embed the dyad with a32 = a12, a33 = a11, a23 = a21 so the triad is symmetric about the R-P axis [read]. No general n-person theorem.

The star generalises as the reduction: a hub interacting with leaves whose self-attitudes are equal sees one "averaged" partner. This is the only exact dimension-reduction result for n > 2 in the dyadic family; it generalises to a star with any number of equal leaves [derived: s = Σ a_{hub,leaf} x_leaf closes the system when leaves share a self-term and have no mutual coupling]. Not in the paper for n > 3.

---

## 8. Cross-check of file 20's HKB entry for n oscillators

File 20 gives HKB for two oscillators (Haken, Kelso & Bunz 1985, doi:10.1007/bf00336922; `φ' = −a sin φ − 2b sin 2φ`). The literature extending coupling-induced bifurcation to groups that I could confirm exists is Zhang M., Beetle C., Kelso J. A. S., Tognoli E. (2019), "Connecting empirical phenomena and theoretical models of biological coordination across scales", *J. R. Soc. Interface* 16(157): 20190360, doi:10.1098/rsif.2019.0360 (Crossref confirms the title and venue only; not read). I cannot state what it proves for n > 2. For many-body human coordination with data, Alderisio et al. above is the one read paper. Treat HKB-at-n as an open item (see Unconfirmed).

---

## Common structure across the n-actor extensions

| Piece | Dyadic form (file 20) | n-actor form found |
|---|---|---|
| Operands | scalar state per person | scalar per node (affect, phase, or tie matrix) |
| Self-term | −m x_i, or ω_k | same, per node |
| Coupling | f(partner state) | Σ_j a_ij f(x_j): graph as a free parameter |
| Sign of influence | sign of c | on the **sender** (Fernández-Rosales), on the **edge** (Altafini, Marvel), absent (Kuramoto) |
| Stability tool | 2 × 2 Jacobian, trace and determinant | Jacobian −mI + AC [derived]; Laplacian λ2 (Kuramoto, MSF) [std]; eigen-decomposition (Marvel) |
| Structure effect | none | reported numerically (Fernández-Rosales); confirmed on 7 people (Alderisio); proved for signed ties (Marvel, Altafini) |

## What exists vs what does not

**Exists.**
- A numerical n-actor version of the Gottman-Liebovitch skeleton on a small-world graph (up to 512 actors), with explicit equations and a published data set of simulation runs.
- A small human experiment (N = 7, two groups) in which graph structure changes group synchrony, with a Kuramoto fit that reproduces the ordering of topologies but not the group-by-topology interaction.
- Exact theory for sign-structured many-actor dynamics: finite-time two-faction outcome for dX/dt = X² and bipartite consensus for linear signed networks.
- Standard network-synchronisation theory (Kuramoto onset, master stability function, algebraic connectivity) available to import.
- An exact dimension-reduction for a star-shaped triad with equal self-attitudes.

**Does not exist (as far as I found).**
- A stability criterion in the psychology literature for the n-actor Gottman-Liebovitch skeleton on an arbitrary graph; the linearisation in section 6 is my own calculation.
- Any n-person drive model (vector of drives per person, such as fear and curiosity) fitted to behavioural data.
- Heterogeneous, edge-labelled influence (c_ij) combined with a network in the same published model **within the conflict-model line**. (Qualified in validation: outside it, Altafini 2013 and Bizyaeva et al. 2023 put signs on edges of an arbitrary graph.)
- An adaptive network where the **drives** change who is connected (the Marvel model changes ties but not drives; Fernández-Rosales fixes the graph). (Qualified in validation: opinion-tie co-evolution models exist, e.g. Holme & Newman 2006; none found with drives.)
- Replication of any of the above; every n-actor psychological result here comes from a single group of authors or a single experiment.
- Group-level fits of coupling strength that are stable across groups (Alderisio's c differs 3.5-fold).

**For the algebra.** The graph becomes a first-class operand beside persons and drives: the adjacency (or signed, directed weight matrix) is an element, and "composition of influence along paths" is matrix multiplication, as in Marvel's X². Eq. 1's decomposition (self-relaxation, plus graph-weighted bounded influence) is the right shape for a "social operator". The two quantities worth promoting to named invariants are the spectral radius of the signed coupling matrix (stability of neutrality) and the leading eigenvector's sign pattern (the faction partition), because both are computed from the algebra's own objects.

## Unconfirmed

- Fernández-Rosales et al.: Crossref gives article e0126234 (vol 10, issue 4). The "N k0 p" phrase not located in the HTML text. Figshare dataset not opened. The 2013 IPN conference deck (Fernandez_CCSIPN2013.pdf) not opened.
- Marvel et al.: the PNAS version was not opened, only the arXiv preprint; the empirical-data section was not read. Kułakowski et al. 2005 not read. Search results also offered a different DOI for the PNAS paper (10.1073/pnas.1018901108, apparently wrong); Crossref returns 10.1073/pnas.1013213108.
- Altafini 2013, Pecora-Carroll, Arenas et al., Strogatz 2000, Acebrón et al., Néda et al., Antal et al.: DOIs confirmed on Crossref, contents [abs] or [std] only.
- Frank & Richardson 2010 and Richardson et al. 2012: DOIs now resolved (section 4); contents not read.
- Liebovitch et al. 2008: authors (Liebovitch, Naudot, Vallacher, Nowak, Bui-Wrzosinska, Coleman), *Physica A* 387(25): 6360-6378 confirmed on Crossref; the "3-10 actors" content is carried from file 20 and was not re-checked in validation.
- Hopfield 1984, Bizyaeva et al. 2023, Holme & Newman 2006 (added in validation): DOIs confirmed, contents from background, not read.
- Zhang, Beetle, Kelso & Tognoli 2019: what it proves for n oscillators is unknown to me.
- Section 6 and the algebraic-connectivity check in section 3 are my derivations; the numbers for the four graphs were computed this session with a short script, the stability reasoning is textbook but not machine-checked. The suggested explanation of the r = 0.5 result in terms of ρ(A C) is a hypothesis, not tested.
- The correction to file 20 (title of the Rojas-Pacheco et al. paper) was observed here; file 20 was not edited.

## Validation log (2026-10-29)

Every DOI resolved at api.crossref.org this pass. Read at source this pass: PLOS ONE HTML of Fernández-Rosales et al.; arXiv 1607.02175v4 (Alderisio, text-extracted); arXiv 1010.1814 (Marvel, text-extracted); arXiv 1202.2338 (Bielczyk, section 5). The web-search budget ran out early in this pass, so the "does not exist" claims were tested against known literature and Crossref-resolved counterexamples rather than by fresh searches.

- ✓ Fernández-Rosales, Liebovitch & Guzmán-Vargas 2015, PLOS ONE 10(4): e0126234: authors, title, Eq. 1 definitions, m = 2, |c_j| = 3, RK4, 50 × 10^3 steps, 512 actors, 441 grid points, 10 realisations, "N > 256", "shallow", p = 0 minimum, Deutsch, figshare all confirmed. ✎ The p = 0 remark is in the text on Fig. 6, not shown to be in the caption; figshare URL added. "N k0 p" not located.
- ✓ Liebovitch et al. 2008, Physica A 387: 6360-6378: DOI, six authors confirmed; content carried from file 20, not re-checked.
- ✓ Rojas-Pacheco, Obregón-Quintana, Liebovitch & Guzmán-Vargas 2013, Physica A 392(3): 458-467: title and authors confirmed.
- ✎ Alderisio, Fiore, Salesse, Bardy & di Bernardo 2017, Sci. Rep. 7: article number 6847 → **6846**. All reported F, p, η², R, t, 99 %/94 %, c = 1.25/4.40, trial counts confirmed against the preprint. ✎ It does not cite Pecora & Carroll; the structure point is cited to Albert & Barabási and Newman et al. ✎ The Star-versus-Ring caveat was backwards. Experimental Group × Topology interaction (significant) added.
- ✓ Strogatz 2000, Physica D 143: 1-20.
- ✓ Acebrón et al. 2005, Rev. Mod. Phys. 77: 137-185.
- ✓ Arenas, Díaz-Guilera, Kurths, Moreno & Zhou 2008, Phys. Rep. 469: 93-153 (full author list now confirmed).
- ✓ Pecora & Carroll 1998, PRL 80: 2109-2112.
- ✓ Néda, Ravasz, Brechet, Vicsek & Barabási 2000, Nature 403: 849-850 (contents [std]).
- ✎ Richardson, Garcia, Frank, Gergor & Marsh 2012, Front. Physiol. 3: 405: DOI 10.3389/fphys.2012.00405 resolved and added.
- ✎ Frank & Richardson 2010, Physica D 239(23-24): 2084-2092: DOI 10.1016/j.physd.2010.07.015 resolved, full title added.
- ✓ Richardson, Marsh, Isenhower, Goodman & Schmidt 2007, Hum. Mov. Sci. 26: 867-891.
- ✓ Marvel, Kleinberg, Kleinberg & Strogatz 2011, PNAS 108(5): 1771-1776: Eqs. 1-5, the three conditions, µ > 0 / µ ≤ 0 with an even split, n(n+1)/2 → n reduction and the balance definition all confirmed in the preprint. The alternative DOI 10.1073/pnas.1018901108 is Srinivasan's commentary in the same issue, so it was rightly rejected.
- ✎ Kułakowski, Gawroński & Gronek 2005, IJMPC 16(5): 707-716, "The Heider balance: a continuous approach": title, pages and DOI added.
- ✓ Antal, Krapivsky & Redner 2005, PRE 72: 036121.
- ✓ Altafini 2013, IEEE TAC 58(4): 935-946 (theorem statement [abs]/[std], consistent with the known result).
- ✎ Bielczyk, Foryś & Płatkowski 2013, J. Math. Sociol. 37(4): 223-249: Eqs. 23-25 and the parameters confirmed. The three-switch example belongs to model (24) and has a11 = a33, so the claim that "multiple switches need the men to differ" was wrong as stated and has been restricted to model (23).
- ✓ Haken, Kelso & Bunz 1985, Biol. Cybern. 51: 347-356.
- ✓ Zhang, Beetle, Kelso & Tognoli 2019, J. R. Soc. Interface 16: 20190360 (contents unread, still ?).
- ✎ Section 6 [derived]: the algebra checks (the Jacobian, the ρ bound, the box bound, λ2 values 7, 1, 0.753, 0.198 recomputed as 2 − 2cos(2π/7) and 2 − 2cos(π/7)). Perron eigenvalue "equal to" → "at least" the mean degree. The claim that "the literature does not state it" is narrowed: Eq. 1 is a Hopfield 1984 network, and Bizyaeva, Franci & Leonard 2023 and Holme & Newman 2006 were added as counterexamples to the claims of novelty and absence (DOIs confirmed, not read).
- ✗ No fabricated works found. Nothing was deleted.

**Verdict.** The survey is largely accurate. The citations are real and correctly authored, and the numbers from the four papers read at source match them. It had one wrong article number (Alderisio, 6846), one misattributed citation (Pecora & Carroll is not cited by Alderisio), a reversed caveat about which topology orderings were significant, and a misreading of the Bielczyk three-switch example. Its "nothing exists" claims were overstated outside the conflict-model literature: Hopfield networks, signed nonlinear opinion dynamics and opinion-tie co-evolution already supply the stability analysis, the edge-signed coupling and the adaptive networks it says are missing. They are now qualified.

## Cross-checks (2026-10-29)

Direction D190. Each claim here was grepped against the other files in this directory (not edited). One primary source was re-read (arXiv 1202.2338, text-extracted) to settle the one real conflict. Files that do not mention these works (no Marvel, Fernández-Rosales, Hopfield, Pecora-Carroll, Kułakowski or Antal hits anywhere else) are listed under "No overlap".

### Agreements

- **Liebovitch et al. 2008 (section 2 here; file 20 section 4b, around line 76; file 082 section 1.5; file 059 lines 26 and 253).** Same authors, journal, volume, pages and DOI 10.1016/j.physa.2008.07.020. Same model (tanh coupling), same pitchfork at c1 c2 > 1 (rescaled), same Theorem 1 (no limit cycles), same 3-10 actor numerics (all-negative feedback splits into two opposed camps). Convention difference only: file 20 writes the inertia as m < 0 in `x' = m x + ...`; this file writes `-m x` with m > 0 (Fernández-Rosales Eq. 1). The condition |c| versus |m| ("strong feedback m < c") is the same in both. File 20's "mixed feedback gives transient oscillations" matches the argument in section 1 here that mixed dyads settle to neutral after oscillating.
- **Fernández-Rosales et al. 2013 slides (section 1 here; file 20, around line 76).** File 20 lists them as "title only, conference slides"; this file's section 1 resolves them to the 2015 PLOS ONE paper and agrees the 2013 deck is the conference version. File 20 also says "no n-person fit to data" and "no general n-person theorem" (lines 11, 181); consistent with Summary item 4 and the "Does not exist" list here.
- **Alderisio et al. 2017 (section 3 here; file 070 lines 71, 110).** Same citation (Sci. Rep. 7, 6846, DOI 10.1038/s41598-017-06559-4), same description (7 people, Kuramoto network, four graphs, two groups, one fitted coupling constant per group). File 070 says it "estimates one scalar", which is the same limitation as "fitted c differs 3.5-fold" here. File 070 itself records "consistent with file 060".
- **Bielczyk, Foryś & Płatkowski (section 7 here; file 20 section 4, lines 66-71; file 070 line 74).** Same arXiv number, same journal version (J. Math. Sociol. 37(4): 223-249, doi 10.1080/0022250x.2011.597279), same triad (Romeo and Paris do not interact, Juliet links both), same averaged-partner reduction `s = a21 r + a23 p` with at most one switch, same existence of a three-switch triad. File 070 agrees it is theory only.
- **Altafini 2013 (section 5 here; file 23 section 10, lines 448-475; file 05 line 392; file 063 line 171).** Same citation and DOI 10.1109/TAC.2012.2224251. Same result: bipartite consensus iff structurally balanced, otherwise convergence to zero. Both files mark the content as standard account or abstract, not read at source. File 23 says "a theorem linking Heider balance to dynamics", the same reading as the "clean theorem form" of the two-camp observation here.
- **Kuramoto and synchronisation references (section 4 here; file 23 section 5, lines 243-272, 772).** Same DOIs for Acebrón et al. 2005, Strogatz 2000 and Néda et al. 2000. Same formula `K_c = 2/(pi g(0))` for a symmetric unimodal g. Both mark it standard.
- **HKB (section 8 here; file 20 line 110, file 061 lines 98, 158).** Same equation `phi' = -a sin phi - 2b sin 2phi`, same DOI 10.1007/bf00336922. Richardson et al. 2007 (doi 10.1016/j.humov.2007.07.002) is cited in files 20, 061 and here with the same DOI. File 061 reads Kelso 2008 at source; this file only cites the equation from file 20.
- **Structural balance (section 5 here; file 03 section 4, line 88; file 06 line 18).** Compatible. This file states balance for a complete signed graph (each triangle has an odd number of positive edges, two factions, one possibly empty); file 03 states the Harary / Cartwright-Harary theorem for any signed graph (two-set partition, positive within, negative between). The complete-graph case here is a special case of file 03's statement. File 03's note that Davis's clusterability allows more than two clusters does not conflict: Marvel's model produces exactly two.
- **Spectral radius as the stability quantity (section 6 here; files 062 line 177, 063 line 187, 070 line 11).** Files 062 and 063 use the same spectral-radius criterion for N > 2 coupling; file 070 asks for exactly the computation (eigenvalues of an estimated coupling matrix) that section 6 here does by hand for Eq. 1. File 048 line 160 already records that "Bizyaeva, Franci and Leonard 2023" is cited here, not read in either file, and calls the novelty narrowing "unresolved for the Franci-Leonard line"; this file agrees (contents "from background, not read").
- **Holme & Newman 2006 (section 6 here; file 05 line 391).** File 05 names Holme-Newman coevolution as belonging to its cluster, "not searched, not cited"; no claim there conflicts with this file's counterexample use.

### Contradictions

1. **Bielczyk et al. triad, when multiple stability switches are possible.**
   - Here (section 7): the reduction to at most one switch holds only for model (23); the three-switch example (a11 = a33 = -28 and so on) is for model (24) and has equal self-attitudes, so "equal self-attitudes" does not rule out multiple switches in (24).
   - File 20 (line 71): "with equal self-attitudes in R and P, the triad reduces to a dyad ... at most one switch. Without that symmetry they construct a triad (system 24) with three stability switches, so the reduction is conditional." This implies the three-switch example breaks the symmetry; line 70 says similarly that multiple switches need a partner who delays reaction to their own state.
   - Source check (arXiv 1202.2338, around eqs. 23-25 and the paragraph after): the paper gives the reduction for model (23) with a11 = a33 = a, then the three-switch parameters a11 = -28, a12 = -74, a21 = 76, a22 = -35, a23 = 76, a32 = -42, a33 = -28 for model (24). So a11 = a33 in the counterexample. **Verdict: this file (060) is right; file 20 line 71 is misleading** (the conditionality is about which model carries the delay, not about asymmetric self-attitudes). The source is itself loose: it says "numerical results for the second model (25)" where (24) is meant. File 20 was not edited.
2. **Title of Rojas-Pacheco et al. 2013 "differs from the one given in file 20".**
   - Here (section 2 and the last Unconfirmed bullet): the title given in file 20 should be corrected.
   - File 20 (line 76 and the missing-works line 254), as it stands, gives **no title** for this paper, only authors, journal, volume, pages, DOI and "(delay gives oscillations)". The git history (commit 1543469) shows no other title. **Verdict: this file's remark is stale; there is nothing in file 20 to correct.** The title given here ("Time-delay effects on dynamics of a two-actor conflict model") was confirmed on Crossref in validation and stands. Not a factual conflict, a mistaken statement in this file; resolved.

### Qualifications that are not contradictions

- **Altafini's connectivity assumption.** Section 5 here states "convergence to a non-trivial consensus is possible if and only if the graph is structurally balanced" without a connectivity hypothesis. File 23 (validation correction, lines 463-475) states the theorem for a **connected** (strongly connected, if directed) signed graph and notes that without connectivity neither branch holds. File 23 is the more careful statement; the section 5 sentence should be read with that assumption. Both are [abs]/[std], so unresolved against the primary paper (not opened here).
- **Section 3 here versus file 070 on "nearest n >= 3 result".** File 070 (line 71) calls Alderisio the closest numerical n >= 3 human-data result and file 070 line 11 says no study fits a coupling matrix and reports eigenvalues; this file says the same ("any fit of an n-person drive model to data" does not exist). Not a conflict, but note that the Alderisio fit is of a scalar on a known graph, as file 070 states.

### No overlap found

Fernández-Rosales 2015, Marvel et al. 2011, Kułakowski et al. 2005, Antal et al. 2005, Hopfield 1984, Pecora & Carroll 1998, Arenas et al. 2008, Frank & Richardson 2010, Richardson et al. 2012 and Zhang et al. 2019 appear in no other file in this directory by name (grep on surname, with accent variants). Nothing to cross-check for them beyond what is above. The claim in section 5 that dX/dt = X^2 gives two factions has no counterpart elsewhere, so it rests on this file's reading of arXiv 1010.1814 alone.

## Licences of quoted and transcribed material (2026-10-30)

Short quotations in this file are a few words to one sentence each and are attributed. Equations are restated in our notation. No table or figure from any source is reproduced.

| Source | Licence as determined | How used |
|---|---|---|
| Fernández-Rosales, Liebovitch & Guzmán-Vargas 2015, PLOS ONE 10(4): e0126234 | CC BY 4.0 (PLOS ONE policy, from knowledge; not re-checked on the article page) | Short quotations (e.g. "strong interaction", "N > 256", "shallow"); restated Eqs. 1-6; description of results. Read as HTML on the journal site. |
| Fernández-Rosales et al. figshare dataset "Conflict Model of Actors Network" (figshare.com/articles/Conflict_Model_of_Actors_Network/1297891) | Not determined; check the figshare record (figshare default is CC BY 4.0 but unconfirmed) | Dataset citation only; the dataset was not opened and none of its contents are used. Check before any reuse. |
| Alderisio et al. 2017, Sci. Rep. 7: 6846 (read as arXiv 1607.02175 v4) | Not determined for the arXiv version (arXiv licence not recorded); Sci. Rep. is normally CC BY 4.0, unconfirmed | One short quotation ("in its current form it fails in modulating..."); restated Eqs. 1-7; reported statistics and fitted values (facts). |
| Marvel, Kleinberg, Kleinberg & Strogatz 2011, PNAS 108(5) (read as arXiv 1010.1814) | Not determined; publisher copyright presumed for PNAS, arXiv licence not recorded | Restated Eqs. 1-5 and theorem conditions in our words; one phrase from the abstract ("intractable conflict", "global harmony"). |
| Bielczyk, Foryś & Płatkowski 2013, J. Math. Sociol. (read as arXiv 1202.2338) | Not determined; publisher copyright presumed (arXiv licence not recorded) | Restated Eqs. 23-25 and the quoted parameter values of the example (facts). |
| Liebovitch et al. 2008, Physica A 387 | Not determined; publisher copyright presumed (Elsevier) | Summary carried from file 20; no quotation. |
| Altafini 2013, IEEE TAC 58(4) | Not determined; publisher copyright presumed (IEEE); not read, abstract-level summary only | Description of the theorem in our words. |
| Kuramoto, MSF and other [std] items (Strogatz 2000, Acebrón et al. 2005, Arenas et al. 2008, Pecora & Carroll 1998, Néda et al. 2000, Hopfield 1984, Bizyaeva et al. 2023, Holme & Newman 2006, Antal et al. 2005, Kułakowski et al. 2005, Richardson et al., Frank & Richardson 2010, Zhang et al. 2019, Haken, Kelso & Bunz 1985) | Not determined; publisher copyright presumed | Citation and restated standard formulas only; not read this session; no quotation. |
| Structural balance definition (Heider 1946; Cartwright & Harary 1956; Harary 1953) | Facts and definitions; our own wording | Description; no Wikipedia text used. |
| Crossref metadata (DOIs, authors, pages) | Facts; Crossref metadata is released CC0 | Citation data. |

Access note: all PDFs and HTML read for this file were open copies (PLOS ONE open access, arXiv preprints); nothing behind an access control was used.
