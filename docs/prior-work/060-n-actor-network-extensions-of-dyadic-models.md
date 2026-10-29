# Prior work 060: n-actor and network extensions of dyadic models

Direction: D190

Date: 2026-10-29. Kind: survey. Question: what is known about fixed points, stability and synchrony of the dyadic coupling models (file 20) as functions of the number of actors n and the network structure.

**Method and honesty note.** Read at source in full this session (PDFs downloaded and text-extracted): Fernández-Rosales, Liebovitch & Guzmán-Vargas 2015 (PLOS ONE); Alderisio, Fiore, Salesse, Bardy & di Bernardo (arXiv v4 of the Sci. Rep. paper); Marvel, Kleinberg, Kleinberg & Strogatz (arXiv 1010.1814, the preprint of the PNAS paper; the PNAS text itself was not opened); Bielczyk, Foryś & Płatkowski section 5 (arXiv 1202.2338). Liebovitch et al. 2008 was read in file 20, not re-read here. Everything tagged [std] is standard textbook content from my background, not checked this session. Tags: **[read]** read at source; **[abs]** abstract or search summary; **[std]** standard account; **[derived]** my own calculation from a stated equation, not in the source. DOIs confirmed on Crossref unless listed in Unconfirmed.

Cross-references: file 20 (dyadic skeleton, Liebovitch 2008, Bielczyk delay triad, HKB, Boker), file 40 (compositional dynamics), file 29 (animal collective behaviour).

## Summary

1. **The n-actor literature in psychology is thin and almost entirely numerical.** The one direct network generalisation of a dyadic drive-coupling model with equations is Fernández-Rosales et al. 2015 (Gottman-Liebovitch skeleton on a small-world network). It has no fixed-point or stability analysis, one parameter setting (m = 2, |c| = 3), and no data. The 2008 "3-10 actors" result in file 20 is the only other n > 2 result in that skeleton.
2. **The strongest n-actor result with human data is not a drive model at all:** Alderisio et al. 2017 put 7 people on four visual-coupling graphs and fit a Kuramoto network. The graph ordering of synchrony (complete and star above ring and path) was reproduced, but with the coupling constant fitted separately to each group (1.25 and 4.40), n = 7 and two groups.
3. **The one real theorem about many actors with signed ties is Marvel et al. (dX/dt = X squared):** for generic symmetric initial X, finite-time blow-up into rank one, i.e. two factions, with the faction partition given in closed form by the signs of the leading eigenvector. It is a relation-state model (the operand is the tie, not a person's drive), and its factions are a prediction about ties, not about behaviour.
4. **What is missing, bluntly:** a general stability criterion for the Gottman-Liebovitch skeleton on an arbitrary graph, any fit of an n-person drive model to data, and any model where the coupling graph is itself driven by the drives (adaptive networks). A simple sufficient stability condition falls out of Eq. 1 of the 2015 paper by linearising (section 6, [derived]); the literature does not state it.

---

## 1. Fernández-Rosales, Liebovitch & Guzmán-Vargas 2015: the Gottman-Liebovitch skeleton on a small-world network

**Citation.** Fernández-Rosales I. Y., Liebovitch L. S., Guzmán-Vargas L. (2015). The Dynamic Consequences of Cooperation and Competition in Small-World Networks. *PLoS ONE* 10(4): e0126234. doi:10.1371/journal.pone.0126234 (Crossref pages not returned; DOI and the printed PDF confirm). Data: figshare "Conflict Model of Actors Network" (listed in the paper's data statement; I did not open it). This resolves the "title only" entry for the 2013 slides in file 20: the 2013 deck is the conference version (IPN repository, Fernandez_CCSIPN2013.pdf, not opened); the journal paper is the source.

**Their vocabulary.** Actors as nodes; "activity" x_i(t), glossed "emotional affect"; "inertia to neutral state"; "influence strength" c_j; cooperative actor (c_j > 0) and competitive actor (c_j < 0), following Deutsch (goals positively or negatively correlated); "strong feedback" (m < |c|); "coefficient of imbalance"; "global/local/neighbourhood distance".

**Drives/operands.** One scalar per actor (affect). No separate drive vector. Cooperation versus competition is a **sign attached to the source actor j**, not to the pair: every outgoing influence of j has the sign of c_j.

**Equations [read].**
- Eq. 1: dx_i/dt = −m_i x_i(t) + Σ_{j=1..N} a_ij c_j tanh(x_j(t)). m_i the relaxation coefficient; a_ij the adjacency matrix; c_j the influence strength of actor j. For convenience m_k = m > 0 and |c_k| = c for all k. "A strong interaction (or strong feedback) is attained if m < c."
- Network: Newman-Watts-Strogatz. Start from a ring with each actor joined to two nearest neighbours either side (degree 4), then add (not rewire) edges between random pairs with probability p; N k0 p is the mean excess connectivity.
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

**Inconsistency worth knowing.** The Fig. 6 caption puts the smallest **global** distance at **p = 0** and r near 0.5, while the closing summary says the effect is "for intermediate values of p". Local minima in δ_L, δ_N are "shallow". The headline (intermediate p) is therefore a trade-off claim between local and global measures, not a minimum of every measure. [read]

**Empirical standing.** None: pure simulation, one (m, c) pair, ten realisations per cell, no data. The abstract calls the findings "new testable predictions". No test found. No replication or sensitivity analysis to m/c, to other graph families, or to heterogeneous c_j magnitudes. Cited by later work not checked.

**Operand/operator translation.** Operand: actor with one scalar affect state. Operator: pairwise saturating influence tanh with a sign fixed by the sender. The sign-on-the-sender design means the model cannot express a pair who cooperate with each other and compete with a third party; that needs c_ij, an edge label. This is the main structural limitation to fix in any generalisation.

---

## 2. Liebovitch et al. 2008, summary of the n > 2 content (from file 20, not re-read)

Two-actor model x' = m1 x + b1 + c1 tanh(y) (and symmetric), pitchfork at c1 c2 = 1 (rescaled), Theorem 1 no limit cycles, and Section 3.7 numerics for 3-10 actors showing all-negative feedback splits the network into two opposed camps [read in file 20]. Doi 10.1016/j.physa.2008.07.020 (reconfirmed on Crossref this session). Follow-up with delay: Rojas-Pacheco, Obregón-Quintana, Liebovitch & Guzmán-Vargas (2013), "Time-delay effects on dynamics of a two-actor conflict model", *Physica A* 392: 458-467, doi 10.1016/j.physa.2012.09.021 (confirmed; title differs from the one given in file 20, which should be corrected). Two actors only.

---

## 3. Alderisio, Fiore, Salesse, Bardy & di Bernardo 2017: seven people on four graphs, Kuramoto fit

**Citation.** Alderisio F., Fiore G., Salesse R. N., Bardy B. G., di Bernardo M. (2017). Interaction patterns and individual dynamics shape the way we move in synchrony. *Scientific Reports* 7, article 6847. doi:10.1038/s41598-017-06559-4 (DOI confirmed on Crossref; article number is from my memory, not from the retrieved record, see Unconfirmed). Preprint arXiv:1607.02175 v4, read in full. Note: the Sci. Rep. abstract and the arXiv abstract word the result slightly differently (the journal stresses group homogeneity).

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
- A 2 (group) × 4 (topology) mixed ANOVA on simulated data: topology effect F(3, 36) = 5.946, p < 0.01, η² = 0.331 (advantage for Complete); group effect not significant; **interaction not significant (F(3,36) = 0.163, p = 0.920)**. The authors state: "in its current form it fails in modulating the topology effect by variations in the group homogeneity".
- Experiment versus simulation: no effect of data origin (Group 1: F(1,12) = 0.206, p = 0.658; Group 2: F(1,12) = 0.619, p = 0.447); topology effect present in both; Complete and Star above Ring and Path (Bonferroni p < 0.01).
- Visually connected dyads synchronise most (the highest ρ^d for 99 % of participants in Group 1, 94 % in Group 2; t(117.970) = −8.872, p < 0.01).
- Correlation of individual frequency variability with synchrony index negative: Complete graph R = −0.69, p < 0.01 (model −0.88); Ring R = −0.14, p = 0.62 (model −0.66, p < 0.01); Path R ≈ 0, p = 0.83 (model −0.45); Star R = −0.45, p = 0.11 (model −0.55).
- Path graph: the more homogeneous group (Group 1) synchronised better.
- Model fails when frequencies are close and c is too high (Group 1 at c = 4.40) or frequencies are far and c is too low (Group 2 at c = 1.25).

**Theorems or derived predictions.** None proved here; the paper cites the network-science result that synchrony depends on interconnection structure (Arenas et al. 2008, Pecora & Carroll 1998 [std]).

**Graph-theoretic check [derived, not in the paper].** Algebraic connectivity (second-smallest Laplacian eigenvalue λ2, the quantity that governs diffusive-coupling synchronisation [std]) for these four graphs at N = 7, unit weights: Complete 7.0, Star 1.0, Ring 0.753, Path 0.198 (computed this session). The ordering Complete > Star > Ring > Path matches the human ordering (Complete and Star above Ring and Path) without any fitted parameter, which is a stronger and cheaper statement than the paper's fitted-c ANOVA. The paper does not make it. Caveat: n = 7, four graphs, and the order of Star versus Ring was not significant in the experiment, so this is one data point supporting a standard theorem, not a test of it.

**Empirical standing.** One lab, two groups of seven, 30-second trials; physical motor task with no stakes, no emotion, no social relationship among participants (students in a lab). The authors' own limitations: groups differ in sex, weight, size, education, and "social factors and personality traits" are unmeasured; they report preliminary evidence from a computer-mediated (non-social) set-up that topology matters there too, which suggests the effect is largely kinematic coupling, not social. No replication found. The fitted c differs 3.5-fold between groups, so c is not a stable property of "people looking at each other"; this is the central weakness for using the model as an operator.

**Operand/operator translation.** Operand: phase and natural frequency (a person's own rhythm). Operator: sin(θ_h − θ_k) weighted by an adjacency a_kh (who attends to whom). Directed adjacency is the right object here (a_kh need not equal a_hk) though the study used symmetric graphs only. Natural frequency ω_k is the closest thing in the model to an individual "set point" in the file 20 skeleton, and heterogeneity of ω_k versus c is the standard order parameter for the onset of synchrony.

---

## 4. Kuramoto theory the above rests on (standard account; not read this session)

- Strogatz S. H. (2000). From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators. *Physica D* 143: 1-20. doi:10.1016/s0167-2789(00)00094-4 (confirmed). Acebrón J. A. et al. (2005). The Kuramoto model: a simple paradigm for synchronization phenomena. *Rev. Mod. Phys.* 77: 137-185. doi:10.1103/revmodphys.77.137 (confirmed). Arenas A., Díaz-Guilera A., Kurths J., Moreno Y., Zhou C. (2008). Synchronization in complex networks. *Physics Reports* 469(3): 93-153. doi:10.1016/j.physrep.2008.09.002 (confirmed; I did not confirm the full author list, the first author is Arenas). Pecora L. M., Carroll T. L. (1998). Master stability functions for synchronized coupled systems. *Phys. Rev. Lett.* 80: 2109-2112. doi:10.1103/physrevlett.80.2109 (confirmed).
- [std] Mean-field Kuramoto dθ_i/dt = ω_i + (K/N) Σ_j sin(θ_j − θ_i); for a unimodal symmetric frequency density g the incoherent state loses stability at K_c = 2/(π g(0)), and partial synchrony grows continuously above it. The master stability function reduces synchronisation of identical coupled units on a network to the eigenvalues of the coupling Laplacian: stability depends on the **smallest non-zero eigenvalue (algebraic connectivity)** and, in some systems, the **eigenvalue ratio** (spread). These are the n- and structure-dependent theorems that exist and that the dyadic psychology models have not borrowed.
- Direct empirical anchor for human crowds: Néda Z., Ravasz E., Brechet Y., Vicsek T., Barabási A.-L. (2000). The sound of many hands clapping. *Nature* 403: 849-850. doi:10.1038/35002660 (confirmed; contents not read, [std] recollection: audience clapping alternates between synchronised and incoherent states, with a period-doubling link to the rhythm).
- Group rocking chairs and cluster-phase measures: Richardson M. J., Garcia R. L., Frank T. D., Gergor M., Marsh K. L. (2012) "Measuring group synchrony: a cluster-phase method for analyzing multivariate movement time-series", *Frontiers in Physiology* (reference [25] in Alderisio; I did not resolve a DOI), and Frank T. D., Richardson M. J. (2010), *Physica D* 239: 2084-2092, test statistic for the Kuramoto order parameter on rocking-chair data (DOI not confirmed, see Unconfirmed). Richardson et al. 2007, "Rocking together" doi:10.1016/j.humov.2007.07.002 (confirmed; in file 20).

---

## 5. Structural balance as a many-actor dynamics: Marvel, Kleinberg, Kleinberg & Strogatz

**Citation.** Marvel S. A., Kleinberg J., Kleinberg R. D., Strogatz S. H. (2011). Continuous-time model of structural balance. *PNAS* 108(5): 1771-1776. doi:10.1073/pnas.1013213108 (Crossref). Read: preprint arXiv:1010.1814, "Analysis of a continuous-time model of structural balance" (differences from the journal version not checked). The model comes from Kułakowski, Gawroński & Gronek (2005), *Int. J. Modern Physics C* 16 (not read, [abs] via the preprint).

**Their vocabulary.** Structural balance (Heider; Cartwright & Harary): a signed complete graph is balanced when each triangle has an odd number of positive edges; equivalently two factions (one possibly empty), positive inside, negative across.

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
- Consequence for the "mixed is calmest" finding: for r = 0.5 with random sign placement A C is a signed random matrix, whose spectral radius is smaller than the all-same-sign case (the all-positive case has a Perron eigenvalue equal to the mean degree). So the origin is **closer to stable** in mixed networks. This may explain the narrower final distribution at r = 0.5 more directly than the dyad-oscillation story; it predicts that the effect disappears when m is large relative to c k, and that it depends on the spectral radius of A C rather than on the ratio r as such. Testing this needs a rerun of the simulation with ρ(A C) computed; the code and the data are on figshare and not examined. Treat as a hypothesis.

---

## 7. Triads and small n with equations (cross-check of file 20)

Bielczyk, Foryś & Płatkowski, *J. Math. Sociol.* 37: 223-249 (2013), doi:10.1080/0022250x.2011.597279 (confirmed). Section 5 read.
- Triad (Eq. 23): r' = a11 r + a12 j; j' = a21 r(t − τ) + a22 j + a23 p(t − τ); p' = a32 j + a33 p (Romeo and Paris do not interact directly). Eq. 24 is the variant with the delay on Juliet's self-term.
- **Reduction [read]:** if the two men have the same self-attitude (a11 = a33 = a), setting s = a21 r + a23 p gives j' = a22 j + s(t − τ), s' = (a12 a21 + a23 a32) j + a s, so Juliet interacts with an "averaged" man and **at most one stability switch** is possible. Multiple switches need the two men to differ. Their example of three switches uses a11 = −28, a12 = −74, a21 = 76, a22 = −35, a23 = 76, a32 = −42, a33 = −28, which has no empirical referent.
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
- Heterogeneous, edge-labelled influence (c_ij) combined with a network in the same published model.
- An adaptive network where the drives change who is connected (the Marvel model changes ties but not drives; Fernández-Rosales fixes the graph).
- Replication of any of the above; every n-actor psychological result here comes from a single group of authors or a single experiment.
- Group-level fits of coupling strength that are stable across groups (Alderisio's c differs 3.5-fold).

**For the algebra.** The graph becomes a first-class operand beside persons and drives: the adjacency (or signed, directed weight matrix) is an element, and "composition of influence along paths" is matrix multiplication, as in Marvel's X². Eq. 1's decomposition (self-relaxation, plus graph-weighted bounded influence) is the right shape for a "social operator". The two quantities worth promoting to named invariants are the spectral radius of the signed coupling matrix (stability of neutrality) and the leading eigenvector's sign pattern (the faction partition), because both are computed from the algebra's own objects.

## Unconfirmed

- Alderisio et al. article number (6847 here is from memory) and volume page; DOI is confirmed.
- Fernández-Rosales et al.: Crossref pages not retrieved; DOI printed on the article itself. Figshare dataset not opened. The 2013 IPN conference deck (Fernandez_CCSIPN2013.pdf) not opened.
- Marvel et al.: the PNAS version was not opened, only the arXiv preprint; the empirical-data section was not read. Kułakowski et al. 2005 not read. Search results also offered a different DOI for the PNAS paper (10.1073/pnas.1018901108, apparently wrong); Crossref returns 10.1073/pnas.1013213108.
- Altafini 2013, Pecora-Carroll, Arenas et al., Strogatz 2000, Acebrón et al., Néda et al., Antal et al.: DOIs confirmed on Crossref, contents [abs] or [std] only.
- Frank & Richardson 2010 (*Physica D* 239: 2084-2092) and the Richardson et al. cluster-phase method paper: citations taken from Alderisio's reference list; my DOI guess for the former resolved to an unrelated paper and was discarded.
- Zhang, Beetle, Kelso & Tognoli 2019: what it proves for n oscillators is unknown to me.
- Section 6 and the algebraic-connectivity check in section 3 are my derivations; the numbers for the four graphs were computed this session with a short script, the stability reasoning is textbook but not machine-checked. The suggested explanation of the r = 0.5 result in terms of ρ(A C) is a hypothesis, not tested.
- The correction to file 20 (title of the Rojas-Pacheco et al. paper) was observed here; file 20 was not edited.
