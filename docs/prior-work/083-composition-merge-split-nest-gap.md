# Prior work 083: composition versus simulation (merge, split, nest)

Direction: D584 (kind: cross-check)

Date: 2026-10-29. Strand: social-algebra. Question: what is actually established when two groups MERGE, one SPLITS, or groups NEST; what each result can and cannot compose; and which composition laws exist nowhere. This is the early answer to "what would an algebra give that simulation does not". Cross-references, not repeated: 04 sec 8 and 13 (coalition logic, bigraphs), 10 (Riker), 14 sec 3 (operads, cospans), 20 sec 4b and 060 (Liebovitch, Marvel), 23 sec 10 (Altafini), 29 sec E2 (Aureli), 40 (operadic dynamics), 37 (fusion).

**Method and provenance.** Fetched as PDF or page and read in the scratchpad, tag `[read]`: Apt and Witzel 2009 (arXiv 0709.0435v3, all statements and proofs outlines through sec 7); Marvel et al. (arXiv 1010.1814v1, main text and Theorem 2 statement; appendix proofs not checked); Antal, Krapivsky and Redner (arXiv physics/0605183, main text); Meng, Shi, Johansson, Cao and Hong (arXiv 1402.2766, later version titled as the Automatica paper; statements read, proofs skimmed); Blondel, Hendrickx and Tsitsiklis (arXiv 0807.2028v4, Theorem 1 and its proof, experimental section); Aureli et al. 2008 (JSTOR scan on eva.mpg.de; framework section, not the supplements); Niwa 2004 (arXiv q-bio/0402003, introduction, data and model description); Palla, Barabasi and Vicsek (arXiv 0704.0744, complete, it is short); Hill, Bentley and Dunbar 2008 (PMC HTML, abstract, introduction, start of methods and Table 1); Spivak 2013 (arXiv 1305.0297, definitions, algebra definition, sec 6); Fong (arXiv 1502.00872, Theorems 3.4 and 4.1 and the graph and resistor examples); Baez, Foley, Moeller and Pollard (arXiv 1711.00037v4, abstract, intro, Theorem 3, Theorem 49); Milner, *Pure bigraphs* (Cambridge TR 614, abstract, intro, Defs 8.12 to 8.14, Theorem 4.6); Clarke 2016 (PhilSci archive preprint, sec 3). So 14 primary texts were read, four of them (Milner, Spivak, Baez et al., Aureli) in selected sections rather than end to end.

**Not read, left `[sa]` (secondary account or standard account): Altafini 2013 (publisher and author-page copies unreachable from this box), Harary 1953 (Project Euclid answered with a bot-protection page; not circumvented), Zachary 1977 (JSTOR/Chicago paywall), Bonabeau, Dagorn and Freon 1999 (PMC copy blocked; the model is read only as Niwa describes it), Liebovitch et al. 2008 (paywalled Physica A), Aumann and Dreze 1974, Hart and Kurz 1983, Davis 1967.** No `[sa]` claim feeds an equation below.

DOIs verified at Crossref this session: Apt and Witzel 10.1142/s0219198909002352; Antal et al. 10.1016/j.physd.2006.09.028; Marvel et al. 10.1073/pnas.1013213108; Meng et al. 10.1016/j.automatica.2016.06.022; Blondel et al. 10.1109/tac.2009.2031211; Aureli et al. 10.1086/586708; Niwa 10.1016/j.jtbi.2004.01.011; Palla et al. 10.1038/nature05670; Hill et al. 10.1098/rsbl.2008.0393; Baez et al. 10.70930/tac/e0rrdvk5; Fong 10.70930/tac/8cw8rvm2; Clarke 10.1093/bjps/axv008; Altafini 10.1109/tac.2012.2224251; Zachary 10.1086/jar.33.4.3629752; Harary 10.1307/mmj/1028989917; Bonabeau et al. 10.1073/pnas.96.8.4472. Spivak 2013 and Milner TR 614 have no DOI (arXiv and Cambridge report number are the identifiers).

## Summary

1. **Four different things get called "merge", and no source composes all four.** (a) A partition of people changes (Apt and Witzel). (b) Signed ties between people resolve into factions (Heider/Cartwright-Harary dynamics: Antal et al., Marvel et al.). (c) States of members converge into clusters (Blondel et al.; Meng et al.). (d) Interfaces and wires are glued (operads, cospans, bigraphs). Each is rigorous about its own object and silent about the others.
2. **The strongest theorems are about structure and say nothing about drive levels.** Apt and Witzel prove termination and order-independence of merge/split sequences for partitions; Milner proves bisimilarity is a congruence; Spivak and Baez et al. prove associativity of wiring. None of these has a variable that could be fear or curiosity. The slot where a drive-state composition law would sit exists in every framework (a preference relation, a decoration functor, an operad algebra, a reaction rule) and is **filled by an assumption in every source**.
3. **Split is the weakest operation everywhere.** Operads compose many into one (Spivak's operations have n inner boxes and one outer box). Apt and Witzel's split rule needs a preference relation handed in. Marvel et al. give a closed form for who ends up in which faction but not when a real group would split, and say the divergence is not to be read as dynamics. No source gives a law for how a group's state divides among its fragments.
4. **Size changes the regime, empirically, and no theory predicts how.** Palla et al. find large groups last longer if membership churns and small groups last longer if it is static. Blondel et al. find cluster count grows with the width of the opinion range, not with n. Antal et al. find time to balance ~ ln N under constrained dynamics, but under local dynamics it ranges from ~ ln N (p > 1/2) through ~ N^(4/3) (p = 1/2) to ~ e^(N^2) (p < 1/2). None of these is a composition law in n.
5. **Nothing here is an intervention study.** No result on steering a merge or split with consent or by manipulation exists in these sources; the only steering proposal (Marvel et al.) is a hypothetical three-step attention strategy.
6. **What an algebra gives that simulation does not, in this evidence**: proofs for all instances (termination and uniqueness, Apt and Witzel Theorem 15; generic outcome, Marvel Theorem 2 and closed form eq 4; congruence, Milner Theorem 4.6) and decomposition (Blondel: once clusters sit at distance >= 1 the system splits into independent subsystems). **What simulation still does that the algebra does not**: the observed cluster spacing near 2.2 in Krause's model is not proved; Blondel et al.'s Theorem 2 proves that a *stable* equilibrium with equal-weight clusters needs spacing >= 2, which they say "comes close to a full explanation", but nothing guarantees the dynamics reach a stable equilibrium. Marvel et al.'s Zachary result needed a tuned offset.

---

## 1. Apt and Witzel: merge and split rules on partitions

**Citation.** Krzysztof R. Apt and Andreas Witzel, "A generic approach to coalition formation", *International Game Theory Review* 11(3): 347-367 (2009). arXiv:0709.0435v3. DOI 10.1142/s0219198909002352 (Crossref). Read at arXiv v3.

**Their vocabulary.** Players N = {1..n} (the "grand coalition"); coalition = non-empty subset; collection = family of disjoint coalitions; partition = collection covering N; comparison relation; merge rule; split rule; defection function D; stable partition; "frame" C[P].

**Drives/operands.** Operand: a partition P of a finite player set. No drives. Preferences enter only through a comparison relation on partitions, induced from a coalition value v(A) (TU-game), from individual payoffs phi, or from hedonic preferences (each player ranks the sets containing them) [read].

**Operators / equations [read].**
- Comparison relation: irreflexive, transitive, and monotone in two senses: (m1) A ▷ B and C ▷ D imply A∪C ▷ B∪D for disjoint supports; (m2) A ▷ B implies A∪C ▷ B∪C.
- merge: {T1..Tk} ∪ P → {∪Tj} ∪ P, applicable where {∪Tj} ▷ {T1..Tk}. split: {∪Tj} ∪ P → {T1..Tk} ∪ P, applicable where {T1..Tk} ▷ {∪Tj}. Both use ▷ "locally".
- Note 2: every iteration of merge/split terminates (finite number of partitions, ▷ strictly increasing).
- Orders on value multisets tested: utilitarian (sum), Nash (product), leximin satisfy (m1) and (m2) (Note 3). **Fail**: the average order (counterexample a={3}, b={2,2,2,2}, c={1,1,1,1}, d={0}: a▷b and c▷d but a∪c ⋫ b∪d); the elitist (max) and egalitarian (min) orders fail (m2). Majority order on payoff vectors is not transitive.
- Definition 9: a partition P is D-stable if C[P] ▷ C for all C ∈ D(P) with C[P] ≠ C. Dp allows all partitions of N, Dc all collections.
- Theorem 10: P is Dp-stable iff ▷-maximal; exists if ▷ is semi-linear. **Dc-stable partitions need not exist** even for semi-linear ▷ (Example 11, N = {1,2,3}).
- Lemma 13: P is Dc-stable iff (i) {A∪B} ▷ {A,B} for disjoint A, B inside one block Pi and (ii) {T}[P] ▷ {T} for every P-incompatible coalition T.
- **Theorem 15**: if P is Dc-stable then (i) P is the outcome of every iteration of merge and split rules from any starting partition; (ii) P is the unique Dp-stable partition; (iii) the unique Dc-stable partition. Credit: the authors say it generalises Apt and Radzik 2006 (arXiv cs.GT/0605132, `[sa]`), where it was proved for TU-games under the utilitarian order, and where it was also shown that **a unique outcome of all merge/split iterations can exist without being Dc-stable**: Dc-stability is sufficient for confluence, not necessary.
- Theorems 6 and 7: a value-based order and a payoff-based order do not in general correspond (only the utilitarian order is invariant), even for anonymous games.
- Composition of games (taken from Owen, *Game Theory*, 3rd ed. 2001, p. 241, their ref [13]): (⊕vi)(A) = Σ vi(Pi ∩ A); Apt and Witzel's own "semi-union" subtracts epsilon > 0 on blocks-crossing coalitions, so that for **strictly superadditive** component games P is Dc-stable (sec 7.1). Examples 16 and 17 construct games for which a prescribed P is the outcome.
- Sec 7.2 hedonic example: each player prefers a larger set of "friends" in P and dislikes anyone not a friend; then P is Dc-stable and every merge/split run ends at P. Sec 7.3: an exchange-economy game gives the same.

**Theorems / derived predictions.** Exactly the above; all are about the abstract rewriting system. The authors relate the approach to abstract reduction systems and Newman's Lemma [read].

**Empirical standing.** None. No data. The stable partitions in sec 7 are **constructed** so the theorem applies (the game is built from P). Blunt: this shows the sufficient conditions are satisfiable, not that any real group has them.

**Scale / consent.** Group scale (partition of players); voluntary by construction: a rule fires only when the new partition is preferred. No manipulation channel exists in the model.

**Group size and composition.** n is arbitrary; the state space is the Bell number of partitions, so termination is guaranteed but not fast. What breaks is not size but the **form of the order**: an order based on average payoff violates (m1), so merging A with an unrelated group C can reverse a preference between A and B. That is a composition-dependence result.

**Operand/operator translation.** Operand: partition of people. Operators: merge, split, each guarded by a local preference test. A merge/split run is a rewriting system with a unique normal form (when Dc-stable), so it behaves like a **closure** operator, not like a group action: Theorem 15(i) says the final partition is independent of the start, so merge and split are **not invertible** and carry no history. [derived from Theorem 15]

---

## 2. Signed ties: balance, factions and schism

### 2.1 Cartwright-Harary balance (static)

**Statement, as restated by sources I read.** Marvel et al. [read]: a complete signed graph is balanced if every triangle has an odd number of positive edges; "any balanced graph can be partitioned into two factions" (all positive inside, all negative across; one faction may be empty), citing Cartwright and Harary. Antal et al. [read]: "on a complete graph balanced societies are remarkably simple: either all individuals are mutual friends ('utopia'), or the network segregates into two mutually antagonistic but internally friendly cliques"; and the probability that a random assignment is balanced "would vanish exponentially with system size". The primary Harary 1953 (DOI above) is `[sa]`; the theorem is stated here only through these two papers.

**Derived merge law [derived from the restated theorem, not from a source].** For a complete balanced graph, s_ij = sigma_i sigma_j for a sign vector sigma. Merge two balanced groups (sigma on G1, tau on G2) by adding all cross ties s_ij. The union is balanced iff there is a single global sign eps with s_ij = eps sigma_i tau_j for all cross pairs. So **balance is not closed under merge**: closure holds only when the cross-tie sign matrix has rank one in sign pattern. A generic merge of two balanced groups is unbalanced, and what follows is decided by dynamics (2.2, 2.3). No source states this closure condition; it is a two-line consequence worth proving in the model files.

**Scale.** Group (ties among members). **Size/composition.** Applies to **complete** graphs only (Marvel: "all graphs in our discussion will be complete"). Three or more factions are not balanced in this sense; the weaker clusterability notion (Davis 1967) is `[sa]` and not read.

### 2.2 Antal, Krapivsky and Redner: discrete dynamics

**Citation.** T. Antal, P. L. Krapivsky, S. Redner, "Social balance on networks: the dynamics of friendship and enmity", *Physica D* 224(1-2): 130-136 (2006). arXiv:physics/0605183. DOI 10.1016/j.physd.2006.09.028. [read]

**Operators [read].** Link variable s_ij = +1 (friends) or -1; triad balanced iff s_ij s_jk s_ki = +1. Local triad dynamics (LTD): pick an imbalanced triad at random; if it has one unfriendly link, with probability p make that link friendly, with probability 1-p make a friendly link unfriendly; if it has three unfriendly links, make one friendly. "This change is made irregardless if other triads become imbalanced as a result". Constrained triad dynamics (CTD): pick an imbalanced triad and a random link in it; flip only if the total number of imbalanced triads decreases, or with probability 1/2 if it is unchanged.

**Results [read].** LTD: a finite network always reaches balance (balanced states are absorbing), with time T_N ~ e^(N^2) for p < 1/2, ~ N^(4/3) for p = 1/2, ~ (2p-1)^(-1) ln N for p > 1/2 (eq 13); in the infinite-network rate equations the state is a frustrated steady state for p < 1/2 and utopia for p > 1/2, approached as a power law at p = 1/2. CTD: balance reached in time ~ ln N; the final state shifts from two near-equal cliques (for initial friendly density rho_0 < 0.4) to utopia at rho_0* about 2/3 (simulation), whereas a mean-field argument predicts 1/2. In a large balanced society <delta^2> = 2 rho_inf - 1 where delta = (C1 - C2)/N.

**Empirical standing.** Simulation only. An illustrative narrative of the build-up to World War I alliances (their Fig 10), not a test. Marvel et al. [read] note earlier discrete models "contained so-called jammed states that could trap a social network before it reached a two-faction configuration", citing Antal, Krapivsky and Redner, *Phys. Rev. E* 72: 036121 (2005), DOI 10.1103/physreve.72.036121, and Marvel, Strogatz and Kleinberg, *Phys. Rev. Lett.* 103: 198701 (2009), DOI 10.1103/physrevlett.103.198701 (both Crossref-verified, both `[sa]`). **Jammed states are not discussed in the Physica D paper read here** (no occurrence in the text); credit them to those two papers.

**Scale / size.** Group (ties). **Size-dependent**: time to balance ~ ln N under CTD and under LTD with p > 1/2, but algebraic or exponential in N for LTD with p <= 1/2; phase structure depends on initial friendly density (CTD) and on p versus 1/2 (LTD).

### 2.3 Marvel, Kleinberg, Kleinberg and Strogatz: dX/dt = X squared

**Citation.** S. A. Marvel, J. Kleinberg, R. Kleinberg, S. H. Strogatz, "Continuous-time model of structural balance", *PNAS* 108(5): 1771-1776 (2011). DOI 10.1073/pnas.1013213108. Read at arXiv:1010.1814v1 ("Analysis of a continuous-time model of structural balance"); the PNAS text was not opened, so page and title differences are unchecked.

**Equations [read].** X is a real symmetric n x n matrix of friendliness; dX/dt = X^2 (eq 1), i.e. dx_ij/dt = Σ_k x_ik x_kj (eq 2). Solution X(t) = X(0)[I - t X(0)]^(-1) (eq 4) = Q D(t) Q^T with l_k(t) = lambda_k / (1 - lambda_k t) (eq 3). If (1) lambda_1 > 0, (2) lambda_1 ≠ lambda_2, (3) all components of the leading eigenvector omega_1 nonzero, then X blows up at t* = 1/lambda_1 and X(t)/||X(t)|| → X* = omega_1 omega_1^T (eq 5): **the two factions are S = {k : omega_1k > 0} and T = {k : omega_1k < 0}**, two all-friendly cliques joined by a complete bipartite graph of unfriendly ties. Conditions (2) and (3) hold with probability 1 for an absolutely continuous X(0); (1) holds with probability tending to 1 as n → infinity (Theorem 3: Pr(lambda_1 <= 0) is exponentially small in n). If lambda_1 <= 0, X(t) → 0 and the end state is one large friend clique (all but at most a few).
Large-n rescaled system dX/dt = n^(-1) X^2 with off-diagonal entries of mean mu and variance sigma^2: **Theorem 2**: lim_{n→∞} x_ij(t) = a_ij - mu + mu/(1 - mu t) with probability 1 for t in [0, 1/K). Result: **mu > 0 evolves to all-positive; mu <= 0 evolves to two equal-sized all-positive cliques with all cross ties negative**.

**Empirical standing, blunt.** (i) Zachary karate club (34 members, the club split into two clubs): after subtracting 0.58 from every capacity (stated as "the minimal downward displacement necessary ... for the resulting separation to be correct for all but 1 of the 34 club members") the model reproduces the real split with one error, the same division Zachary's own method found (which also misclassified one of 34); alternatively substituting -11 for the zero capacity between the two leaders gives the same factions. **The offset was chosen to make the answer correct; this is a fit, not a prediction.** (ii) Axelrod and Bennett's 1939 propensity x size x size matrix for 17 countries in WWII: correct Allied/Axis split except Denmark and Portugal (15 of 17), with the authors noting Axelrod and Bennett's own landscape theory "does slightly better" (only Portugal wrong). The matrices were converted to "friendliness" by the authors. No out-of-sample test. The authors: the model "is a mathematical cartoon ... not designed for quantitative prediction", and the finite-time divergence is not to be read as dynamics: the focus is "the pattern of signs", which "eventually stabilizes at a point before the divergence".

**Scale / consent.** Group (member ties) and inter-group (nations). Suggested intervention, **hypothetical only**: (i) direct the network's attention away from its divided status, (ii) encourage friendships across the divide, (iii) return to the issue, raising mean friendliness; the authors link this to Pettigrew's prejudice-reduction proposal (`[sa]`, not read). That is attention steering, not a consent-based protocol, and it is untested here.

**Group size and composition.** Large-n limit is where the clean transition mu = 0 lives; for small n the "exceptional set" (lambda_1 <= 0) has non-negligible probability; complete graphs only. Faction membership depends on **which members' ties are in X(0)**, so composition of the initial matrix, not the group label, decides the split.

**Operand/operator translation.** Operand: a signed relation matrix. Operator: X ↦ X^2, relation composition (friend of a friend) fed back into the relation. This is an algebraic operator on relations, the one genuinely algebraic split/merge-of-ties object found. It produces a **partition into two** from continuous ties; it does not produce a time or a drive.

### 2.4 Altafini and Meng et al.: antagonistic consensus

**Altafini 2013** (IEEE TAC 58(4): 935-946, DOI 10.1109/tac.2012.2224251) is `[sa]`: both the author-page copy and the repository copy were unreachable. What I read about it is **Meng et al.'s description**: Altafini assumes a node "receives the opposite of the true state of its neighboring node" so that an antagonistic input has the form -(x_i + x_j) in place of -(x_i - x_j); fixed topology, continuous time (Remark 2.1 and introduction) [read].

**Meng et al.** (Automatica 73: 110-116, 2016, DOI 10.1016/j.automatica.2016.06.022; read as arXiv:1402.2766, a later version of the text). Model [read]: x_i(k+1) = Σ_{j in N_i(k)} a_ij(x,k) x_j(k); Assumption 2.1: a_ii >= lambda, Σ_j |a_ij| = 1, a_ij >= lambda for cooperative neighbours, a_ij <= -lambda for antagonistic ones. Theorem 2.1 (unidirectional, uniformly jointly strongly connected): limits exist and |x_i| → M* common. Theorem 2.2 (bidirectional, infinitely jointly connected): same. **Definition 2.2**: the sign-consistent signed total graph G* is structurally balanced if V splits into two non-empty subsets with positive arcs inside and negative arcs between. **Theorem 2.3**: with G* structurally balanced and every negative arc appearing infinitely often, x_i → M* on V1 and -M* on V2 ("bipartite consensus"). A counterexample (3 nodes, fixed graph, quasi-strongly connected) shows consensus in absolute value fails with only a directed spanning tree.

**What it composes.** Two antagonistic groups, each internally agreeing, held at opposite signed values of equal magnitude. Group = a side of the balanced bipartition. Merge of a third group: not treated. If balance fails, only the moduli converge (Theorems 2.1 and 2.2); the sign pattern is not determined by the theorems. In their own unbalanced Kuramoto example all states converge to zero (simulation, not theorem).

**Empirical standing.** None; a discrete Kuramoto simulation illustrates. Opinion/crowd-scale abstraction.

### 2.5 Krause/Hegselmann-Krause: merging by averaging (cluster formation)

**Citation.** V. D. Blondel, J. M. Hendrickx, J. N. Tsitsiklis, "On Krause's multi-agent consensus model with state-dependent connectivity", *IEEE TAC* 54(11): 2586-2597 (2009). arXiv:0807.2028v4. DOI 10.1109/tac.2009.2031211. [read]

**Equation [read].** x_i(t+1) = Σ_{j : |x_i(t) - x_j(t)| < 1} x_j(t) / Σ_{j : |x_i(t) - x_j(t)| < 1} 1 (eq 1): each agent averages the opinions within distance 1 (itself included).
**Theorem 1 [read]**: every x_i(t) converges to a limit in finite time, and for any i, j either x*_i = x*_j or |x*_i - x*_j| >= 1. Facts used: the smallest opinion is non-decreasing, the largest non-increasing; if two consecutive sorted opinions are at distance >= 1 at some time, they stay so, "the system can then be decomposed into two independent subsystems". Average is **not** preserved and the variance can increase.
**Composition content.** Clusters are the "merged groups". Once separated by >= 1 they never interact again: a **decomposition (split) law with a permanent boundary**. Opinions confined to an interval of length L converge to at most ceil(L)+1 clusters; the observed number grows about linearly in L with coefficient slightly below 1/2 (inter-cluster distance near 2.2, "slightly larger than 2"). The introduction says no explanation or nontrivial lower bound was available before this paper; their own **Theorem 2 [read]** then proves: an equilibrium is stable (robust to a perturbing agent of vanishing weight) iff every two clusters A, B either have equal weights and distance >= 2, or unequal weights and distance > 1 + min(W_A, W_B)/max(W_A, W_B). The authors: this "comes close to a full explanation of the observed inter-cluster distances of about 2.2", but "there is no guarantee that the system (1) will converge to a stable equilibrium". Experimentally a single cluster for L below about 5.1; provable (odd n, uniformly spaced start) only below about 3.833. Convergence time is bounded by c(n) but "an upper bound independent of n is not possible", even with all opinions in a fixed interval.
**Composable only in the simplest case.** Two isolated point clusters closer than 1 merge in one step at their weight-centre m = (W_A x_A + W_B x_B)/(W_A + W_B): every agent then averages over both [derived from eq 1; the proof of Theorem 2 uses the same centre of mass and the one-cluster case (x̃δ + x_A W_A)/(δ + W_A)]. With spread-out opinions, or a third group within range, the outcome depends on the whole configuration, the average is not preserved, and there is no closed-form merge rule.
**Empirical standing.** None (no data). Scale: opinion/crowd.
**Size.** Cluster count tracks the opinion range L, not n; convergence time grows with n in worst cases; the countable-agent version fails Theorem 1.

---

## 3. Fission-fusion in animal groups and group-size laws

### 3.1 Aureli et al. 2008

**Citation.** F. Aureli, C. M. Schaffner, C. Boesch, S. K. Bearder and 15 co-authors, "Fission-fusion dynamics: new research frameworks", *Current Anthropology* 49(4): 627-654 (2008). DOI 10.1086/586708. Read from the JSTOR scan (framework section).

**Their vocabulary [read].** Kummer's (1971) term used for taxa that "change the size of their groups by means of the fission and fusion of subunits (called parties or subgroups)". They propose abandoning "fission-fusion societies" as a modal type and using "fission-fusion dynamics" for "the extent of variation in spatial cohesion and individual membership in a group over time". Three dimensions: temporal variation in (1) spatial cohesion, (2) party size, (3) party composition (Fig 1: X, Y, Z axes). "Higher-FF" and "lower-FF" are positions in this space, "not an actual dichotomy". Multilevel societies (hamadryas baboons) are a separate region of the space.

**Operators / equations.** None. Their proposal for quantification is **null models by spatially explicit agent-based simulation** of animals foraging in a resource landscape, compared with observed association patterns [read].

**Cross-check result.** File 29 sec E2 described the operand as "a partition of the individuals" with "a partition lattice the natural formalism". Aureli et al. contain no partition formalism: their operand is three scalar variabilities. The partition lattice is the earlier survey's suggestion; where partitions with merge/split rules are formalised is Apt and Witzel (sec 1 above). Verdict: 29's operators (Fission, Fusion) are right as description; the formalism claim was not in the source.

**Empirical standing.** Comparative framework; the paper is a research programme. Scale: group (animal). Humans are noted as higher-FF "typical of modern humans, including hunter-gatherers" (cited to Marlowe 2005, `[sa]`).

### 3.2 Bonabeau-Dagorn school model as reported by Niwa; Niwa's own scaling

**Citation.** H.-S. Niwa, "Space-irrelevant scaling law for fish school sizes", *J. Theor. Biol.* 228(3): 347-357 (2004). arXiv:q-bio/0402003. DOI 10.1016/j.jtbi.2004.01.011. [read]. The original Bonabeau, Dagorn, Freon (PNAS 96(8): 4472-4477, 1999, DOI above) is `[sa]`; only Niwa's description was read.

**As Niwa describes [read].** Bonabeau and Dagorn (1995): schools move between sites and **merge when they meet**; splitting is replaced by reinjection of a fraction of each school as single individuals, total number fixed; mean-field gives a truncated power law with exponent -3/2. Niwa: the size distribution depends on school size only through the ratio of size to the expected size of the schools an arbitrary individual is in; **expected size is linear in the ratio of population density to the breakup rate of schools**; empirical exponents range 0.7 to 1.8; the number-weighted distribution W(N) decays as a power law with exponent about -1 truncated at a cut-off, while the individual-weighted P(N) = N W(N) is thin-tailed; scaling collapse over five data sets (northern anchovy, Japanese sardine, tropical tuna free-swimming and at FADs, herring); independent of spatial dimension in simulation.

**What it composes.** The **distribution over group sizes** under repeated merge and break-up, not membership. Break-up is an exogenous rate; nothing inside the school causes it.

**Empirical standing.** Scaling collapse on five fisheries data sets (catch per set, acoustic surveys); fits the shape, does not predict which school splits when. Scale: group (animal, fish), not human. No consent notion.

**Size.** The law is *about* n: truncated power law with cut-off set by density over break-up rate.

### 3.3 Hill, Bentley and Dunbar: nesting ratios

**Citation.** R. A. Hill, R. A. Bentley, R. I. M. Dunbar, "Network scaling reveals consistent fractal pattern in hierarchical mammalian societies", *Biology Letters* 4(6): 748-751 (2008). DOI 10.1098/rsbl.2008.0393. Read at PMC (abstract, introduction, Table 1).

**Result [read].** Successive layers of social organisation have a scaling ratio of "almost exactly 3" for elephant, gelada and hamadryas, 3.8 for orca (Horton-Strahler method of Hamilton et al. 2007, `[sa]`); human hierarchies are described (via Zhou et al. 2005 and Hamilton et al. 2007, both `[sa]`) with ratios "between three and four". Table 1 example: gelada mean 345.3, 99.3, 27.9, 12.2, 5.1 across community, band, team, one-male unit, clique. The authors: "the origin of the hierarchical, fractal-like organisation ... [is] a fundamental question".

**What it composes.** A nesting law on **sizes** only: layer k+1 is about 3 times layer k. No state, no tie, no mechanism. Scale: group, non-human, descriptive.

---

## 4. Empirical group evolution: Palla, Barabasi and Vicsek

**Citation.** G. Palla, A.-L. Barabasi, T. Vicsek, "Quantifying social group evolution", *Nature* 446(7136): 664-667 (2007). arXiv:0704.0744. DOI 10.1038/nature05670. [read, complete]

**Data [read].** Co-authorship: Los Alamos cond-mat archive, 142 months, over 30,000 authors. Mobile phone: complete call record of a company's customers for 52 weeks (two-week accumulations), over 4 million users. Communities by clique percolation (CPM; parameters k and a weight threshold w*, so "group" is an algorithm output); overlapping communities allowed. Within-community mean link weight over between-community: 2.9 (co-authorship), 5.9 (phone).

**Operators [read].** Events in a community's life: grow, contract, **merge, split**, birth, death. Matching of communities between t and t+1 via the CPM communities of the **joint graph** (union of the two snapshots): a joint community containing one community from each step is matched; if more than one, matched in descending order of relative node overlap. Autocorrelation C_A(t) = |A(t0) ∩ A(t0+t)| / |A(t0) ∪ A(t0+t)| (eq 1). Stationarity zeta = average of C(t, t+1) over the lifetime (eq 2); 1 - zeta = average fraction of members changed per step. Lifetime tau* is a "fitness".

**Findings [read].** Larger communities have faster-decaying C(t) (higher member turnover). For **small** communities the highest average lifetime is at zeta close to 1 (static membership); for **large** communities the peak is shifted to low zeta (continually changing membership). A member's probability of leaving rises with w_out / (w_in + w_out); a community's lifetime falls for large W_out / (W_in + W_out) (phone), with a maximum at intermediate outside collaboration for co-authors. Communities near size 30-35 are the most geographically (zip-code) homogeneous in the phone data.

**Empirical standing, blunt.** Two very large observational data sets giving the same qualitative size-by-stationarity pattern; **no merge or split rates, no composition law, and no out-of-sample prediction of a merge or split are reported in the text I read** (effect sizes live in figures, not extracted). The events are defined by the matching algorithm, so "merge" and "split" are as much method as phenomenon. Phone and co-authorship ties are not sentiment ties. No intervention.

**Scale.** Membership (leave probability), group (lifetime, stationarity, merge/split events). **Size/composition: the central finding**: the optimal composition policy reverses with group size.

---

## 5. Structural composition frameworks (no quantities)

### 5.1 Spivak: operad of wiring diagrams

**Citation.** D. I. Spivak, "The operad of wiring diagrams: formalizing a graphical language for databases, recursion, and plug-and-play circuits", arXiv:1305.0297 (2013). Preprint. [read: definitions, sec 6]

**Definitions [read].** Operad O: objects; for finite n, x : n → Ob(O), y: a set O_n(x; y) of morphisms; identities id_x; composition formula O_n(y;z) × Π_{i in n} O_{m_i}(x_i; y(i)) → O_m(x; z); identity law and an associative law. Slogan: "a wiring diagram of wiring diagrams is a wiring diagram". Algebra on O: an operad functor O → Sets; "the algebra ... assigns to each agency ... a set of possible states, and ... a rule by which a state on any given whole emerges from the states on its constituent parts" (sec 6.2). Wiring diagram operad: morphisms are cospans in Fin of the form X → C ← Y; objects are finite sets (interfaces). Sec 6.1 lists as future work that S "can perhaps be lifted to something like an operad object in Cat" and that "aggregation, such as taking sums or averages" is not yet understood in the framework.

**What it composes.** Interfaces and wires: nesting to any depth, associative. **Many-to-one only.** No operation takes one box to several. The state-composition law is **the choice of algebra**, not part of the operad.

### 5.2 Fong: decorated cospans

**Citation.** B. Fong, "Decorated cospans", *Theory and Applications of Categories* 30: 1096-1120 (2015). arXiv:1502.00872. DOI 10.70930/tac/8cw8rvm2. [read]

**Statement [read].** C with finite colimits, (D, ⊗) braided monoidal, (F, phi) : (C, +) → (D, ⊗) lax braided monoidal. Theorem 3.4: F-Cospan, with objects those of C and morphisms a cospan X → N ← Y plus an element 1 → F N, is a symmetric monoidal **hypergraph category** (every object carries a special commutative Frobenius monoid), with Cospan(C) embedded. Composition: pushout over the shared foot (gluing), decoration composed through F. Theorem 4.1: a monoidal natural transformation between such functors gives a hypergraph functor, i.e. semantics. Worked example: graphs (gluing graphs along chosen vertices) and resistor networks, where semantics = Ohm's law (the power Q(psi) = Σ_e (psi_t(e) - psi_s(e))^2 / r(e)) and the Frobenius maps act as perfectly conducting wires (Kirchhoff).

**What it composes.** The **merge of two systems by identifying shared nodes**. The nodes could be people; the decoration is any structure the functor F supplies. Both multiplication (join wires) and comultiplication (split a wire) exist **for wires/ports**, so a morphism from an interface into a sum of interfaces exists. **What is not given: when to split, and how a decoration divides over the pieces.** Pushforward along a map f : N → P that identifies two nodes needs F(f), and F(f) for a non-injective f is exactly "how do the states of two merged members combine" (sum, mean, max, product are all admissible). [derived, from Theorem 3.4's hypotheses]

### 5.3 Baez, Foley, Moeller and Pollard: network models

**Citation.** J. C. Baez, J. Foley, J. Moeller, B. S. Pollard, "Network models", *Theory and Applications of Categories* 35: 700-744 (2020). arXiv:1711.00037v4. DOI 10.70930/tac/e0rrdvk5. [read]

**Statement [read].** A one-coloured network model is a lax symmetric monoidal functor F : S → Mon. Theorem 3 unpacks it: sets F(n) ("networks with n vertices"), identities e_n, an **overlay** ∪ : F(n) × F(n) → F(n) (a monoid), S_n actions, and a **disjoint union** ⊔ : F(m) × F(n) → F(m+n), with the equations: e_n ∪ g = g; g1 ∪ (g2 ∪ g3) = (g1 ∪ g2) ∪ g3; sigma(g1 ∪ g2) = sigma g1 ∪ sigma g2; (g1 ∪ g2) ⊔ (h1 ∪ h2) = (g1 ⊔ h1) ∪ (g2 ⊔ h2); e_m ⊔ e_n = e_{m+n}; ⊔ associative. Theorem 49: the network operad has O_F(n1..nk; n) = S_n × F(n) when n1+...+nk = n, empty otherwise: operations are "ways of assembling a network of the given kind from smaller parts". Origin: vertices as planes, boats and drones in a search-and-rescue mission.

**What it composes.** Two groups on disjoint members: side by side (⊔) then add a connecting network g ∈ F(n) by overlay (∪). Associative, with an identity. Examples include directed multigraphs and coloured vertices (different types of agent). **Inter-group ties are supplied by the chooser of g, not derived**; no split; no states.

### 5.4 Milner: pure bigraphs

**Citation.** R. Milner, *Pure bigraphs*, Cambridge Computer Laboratory TR 614 (2005). [read: abstract, introduction, Defs 8.12 to 8.14, Theorem 4.6 statement]

**Statement [read].** Bigraphs are "graphs whose nodes may be nested, representing locality, independently of the edges connecting them". Place graph = nesting of regions, nodes, sites; link graph = connectivity independent of nesting ("links often cross node boundaries"). Composition and tensor product as arrows between interfaces. Parallel product G0 ‖ G1 keeps regions separate; **prime product G0 | G1 = merge(G0 ‖ G1)** where merge : m → 1 maps m sites to one root: "The parallel product keeps their regions separate, while the prime product merges them" (Def 8.14). Both products are associative with unit ε. Bigraphical reactive systems add reaction rules; **Theorem 4.6**: in a wide reactive system with RPOs and the standard transition system, wide bisimilarity is a congruence (a0 ~ a1 implies C a0 ~ C a1); Milner states it here and gives the proof in Leifer and Milner, Cambridge TR 598 (2004), his ref [30] (`[sa]`). Running example: pure CCS. The agent example (Fig 1) is agents, "perhaps humans equipped with devices", in rooms and buildings; the abstract names pervasive computing and biological systems, and the text says "continuous events and stochastic behaviour must also be modelled".

**What it composes.** Nesting (the place graph is a forest of arbitrary depth), merge of regions, and links across nesting boundaries, **with dynamics (reaction rules) and a theorem that behavioural equivalence survives embedding in any context**. This is the only source here with composition, nesting, rewiring and a compositionality theorem together. **No quantities in pure bigraphs**: a control has an arity, not a level; a continuous drive state would have to be encoded as a sort or an atomic control, losing the arithmetic. Rates were added later: Krivine, Milner and Troina, "Stochastic bigraphs", *ENTCS* 218: 73-96 (2008), DOI 10.1016/j.entcs.2008.10.006 (Crossref-verified; content `[sa]`, found by search, not read) give a stochastic semantics to bigraphical reactive systems. That puts rates on reactions, not levels on nodes.

### 5.5 Clarke on the multilevel Price decomposition

**Citation.** C. Clarke, "Multi-level selection and the explanatory value of mathematical decompositions", *Brit. J. Phil. Sci.* 67(4): 1025-1055 (2016). DOI 10.1093/bjps/axv008. Read as PhilSci-Archive preprint, sec 3. The Price (1972) and Hamilton (1975) originals are `[sa]`.

**Statement [read].** For a population partitioned into collectives g: **Cov(w, z) = Cov[Exp_g(w), Exp_g(z)] + Exp[Cov_g(w, z)]** (eq 1): total character-fitness covariance = between-collective covariance of collective means + the average within-collective covariance. Clarke: "the multi-level Price decomposition is a mathematical theorem, guaranteed by the logic of covariance and of expectation"; his thesis is that its terms measure the effect of a causal intervention only when sharing of collective resources is "subtractable" (so less than Sober and Wilson claim).

**What it composes.** The one **exact nesting law** found: statistics of a population decompose additively over any partition, for any partition, at any size. It is an identity, not a dynamic, and it says nothing about merging two groups, though the formula tells you how the two terms change if you recompute the partition. Scale: population/group statistics.

---

## Inventory: what composes, what does not

| Operation | Object | What is established | Source (tag) | What it cannot do |
|---|---|---|---|---|
| Merge / split sequences | partition of members | termination; unique normal form under Dc-stability; stable partition may not exist | Apt-Witzel (read) | no drive levels; start-independent so non-invertible; order ▷ must be supplied |
| Merge of balanced groups | signed ties | static: balanced = two factions; closure only under a rank-one cross-tie sign pattern | Marvel, Antal restating Harary (read; Harary sa); closure condition derived | no dynamics for the cross ties; 3+ factions absent |
| Faction formation | signed ties | which side each member ends on (sign of omega_1), generic, finite-time; transition at mu = 0 | Marvel (read) | not when; magnitudes diverge; complete graphs only; fitted offset on Zachary |
| Discrete schism | signed ties | ln N time under CTD; LTD time ln N to e^(N^2) by p; CTD transition near rho_0 = 2/3 | Antal (read); jammed states: Antal et al. 2005 PRE, Marvel et al. 2009 PRL (sa) | simulation and heuristic scaling only |
| Bipartite consensus | signed ties + states | two antagonistic groups at +M*, -M* given balance | Meng; Altafini (sa) | needs balance; no merge of a third group |
| Cluster merging | scalar opinions | clusters separated >= 1; permanent decomposition; stable equilibria need spacing >= 2 (equal weights) | Blondel (read) | merge position is the weight-centre only for isolated point clusters; convergence to a stable equilibrium not guaranteed, so spacing near 2.2 not proved |
| Wiring / nesting | interfaces | associative composition, deep nesting | Spivak, Baez (read) | many-to-one only; no state law; no dynamics |
| Gluing members | nodes of a system | pushout composition with decorations; Frobenius split of wires | Fong (read) | decoration pushforward F(f) is unconstrained |
| Reconfiguration with nesting | place + link graph | reaction rules; bisimilarity congruence | Milner (read) | no quantities (stochastic bigraphs add rates, sa) |
| Nested statistics | any partition | Cov decomposes exactly over partition | Clarke (read) | identity, not dynamics; contested causal reading |
| Size distribution | multiset of sizes | merge + break-up gives truncated power law; scale = density / break-up rate | Niwa (read), Bonabeau (sa) | break-up exogenous; fish only |
| Nesting sizes | layer sizes | ratio about 3 | Hill (read) | no mechanism; hierarchies only; no states |
| Event statistics | communities | size-dependent stability reversal | Palla (read) | no rates; definition-by-algorithm; no prediction |

### Composition laws that exist nowhere in what was read

1. **Merge law for group drive state**: given group A with drive distribution on n_A members and group B on n_B, the drive distribution of A ⊕ B. The only states-merging dynamics read (Krause averaging) gives the weight-centre for two isolated point clusters and nothing in general: it does not conserve the mean, and for spread-out opinions there is no closed-form cluster location.
2. **Split law for group state**: how a group's ties and drive state divide among its fragments, and a cause for when. Marvel gives who, not when or what state.
3. **A downward constraint law** across nested levels (group state fixing members' admissible drives) that is empirically tested. Hill gives size ratios; Clarke/Price gives a statistical identity; neither is a state-constraint law. (File 067 collects the downward-function proposals; none of the nesting sources here tests one.)
4. **Associativity and commutativity of merge for states**: whether (A⊕B)⊕C = A⊕(B⊕C) for ties-plus-states. For partitions, Apt-Witzel prove confluence under Dc-stability, a sufficient condition (Apt and Radzik show confluence can hold without it); for discrete tie dynamics, jammed states (Antal et al. 2005, Marvel et al. 2009, `[sa]`) make outcomes path-dependent, so the answer is no in general; for state averaging, no result.
5. **A group (inverse) structure**: Theorem 15(i) implies merge-then-split does not recover the start. No law relates a merge to a split that undoes it, so "algebra" here means a rewriting system or monoid, not a group, unless a different definition of split is supplied. [derived]
6. **Overlap**: a member in two groups with different group drives. CPM allows overlap (Palla); network-model overlay ∪ is on one node set; nothing says what the member's drive is.
7. **Size-indexed composition law**: any law with n as a parameter for drives. Only distributional laws (Niwa) and empirical regime flips (Palla) exist.
8. **A steering result**: a merge or split induced by an intervention, measured, and classified as consent-based or manipulative. None.
9. **Three or more factions** in a dynamical signed-tie law with a proof (Marvel and Antal are two-faction; the Davis generalisation is unread). Search check: Shang, "On the structural balance dynamics under perceived sentiment", *Bull. Iranian Math. Soc.* 46: 717-724 (2020; online 2019), DOI 10.1007/s41980-019-00286-4 (Crossref-verified), reportedly obtains **at most four factions** for almost all initial conditions in a non-autonomous variant of dX/dt = X^2. Not read, `[sa]`; it weakens "nowhere" to "not in what was read", and it is still a bound, not a law for k factions.

### Cross-check verdicts on earlier files

- **29 sec E2 (Aureli)**: operand as partition lattice is not in Aureli; right in spirit, wrong as attribution; Apt-Witzel is the partition formalism. Author list: Crossref gives Aureli, Schaffner, Boesch, Bearder as the first four of 19.
- **23 sec 10 (Altafini)**: the formulation -(x_i + x_j) is confirmed by Meng's description. The claim "iff balanced, else all states go to zero" is **not** supported by Meng's theorems, which for a different (discrete, row-normalised) model give: moduli converge to a common M* >= 0 without balance (their unbalanced simulation happens to go to zero; the theorems do not force it), and +M*/-M* with balance. Whether Altafini's continuous Laplacian gives zero remains `[sa]`; do not treat "iff / zero" as established until the primary is read.
- **14 sec 3 (operads as "strongest candidate for the group-formation operator")**: the limit "static and typed" is right. Added: the operad is many-to-one and the state law is the algebra, not the operad; merging members is decorated cospans (pushout), not operad composition; rewiring with nesting is in bigraphs.
- **04 sec 13 (bigraphs "closest to the form")**: form confirmed; **quantities absent**; the congruence theorem holds for given reaction rules, so drives would have to be expressed as discrete controls.
- **20/060 (Liebovitch camps)**: not re-read; Liebovitch's all-negative-feedback numerics (3-10 actors, tanh coupling) and Marvel's X^2 composition both end in two camps by different mechanisms. File 060's reading of the mu > 0 / mu <= 0 rule is **confirmed**; what it omits is that the sign pattern stabilises shortly before a finite-time blow-up of the magnitudes and that the Zachary agreement used a fitted offset.
- **Vocabulary hazard (relevant to 37)**: "fusion" and "merge" mean five different things here: Aureli's party fusion (spatial membership), Whitehouse and Swann identity fusion (psychological, file 37), Apt-Witzel merge (union of coalitions), Milner's merge (collapse of roots), Palla's merge (matched community events). The algebra needs distinct operator names.

## What an algebra gives that simulation does not (evidence-based)

For: (a) statements true of all instances, which no run can give: Apt-Witzel Theorem 15, Milner Theorem 4.6, Marvel's closed form and probability-1 statements that resolved the open problem left by simulation with jammed states. (b) Reuse: operad and network-model associativity lets sub-results be nested. (c) Diagnosis: the algebraic framing exposes where assumptions hide (the order ▷, the functor F, the algebra of the operad), which a simulation would bury in code.
Against: (a) In every framework above the hard part (the law for drive states) is an input. (b) Where results are empirical (Zachary fit, Krause spacing 2.2, Palla's regime flip) the simulation or data runs ahead of the algebra. (c) No framework contains the quantity the strand cares about. So today an algebra buys **structure with guarantees and an empty slot**; a simulation buys **numbers without guarantees**; the gap is the content of the slot.

## Does it reduce to a drive basis?

**Partly, and mostly not at the level of the composition laws.**
- *What reduces or plausibly reduces to drives of persons.* The triggers and targets of merging and splitting. Apt-Witzel's hedonic example is an explicit individual preference (each player "prefers a larger set of his friends" and "dislikes" strangers) generating the order that makes a partition stable. Marvel/Antal's balance dynamics are described by the authors (Marvel et al. 2011, PNAS, and Antal, Krapivsky and Redner 2006, Physica D; which paper carries which phrase is not pinned and needs a re-check) as "the urge to make one's friendships and rivalries consistent" and "a social desire to avoid imbalanced triads": a consistency drive over triads, which is a relational drive (not in the person-level drive lists). Palla's commitment ratio w_out/(w_in+w_out) behaves like competing attachments pulling a member in and out (association only). Bounded confidence in Krause's model is a threshold on perceived distance, a candidate for an openness or curiosity parameter, not a drive in the taxonomies. Fish merge on encounter and break up at a rate; cohesion versus escape drives are plausible hidden content of the rates, but nothing read derives them.
- *What does NOT reduce.* (i) Apt-Witzel's termination and uniqueness theorems are properties of the order (transitivity, monotonicity) and hold for any drive-generated order that satisfies them; the average-payoff order fails (m1) whatever its drive origin. (ii) The operad, cospan, network-model and bigraph laws are compositional constraints on any drive model. (iii) The balance theorem is combinatorial (Z2 sign multiplication). (iv) The Price/covariance decomposition is an identity. (v) Hill's ratio of about 3 has no mechanism. (vi) Palla's size-dependent stability reversal is a group-level regularity with no person-level derivation in the sources.
- *Implication for the working hypothesis.* Drives sit at the **generator** level (what makes a preference, a tie, an attraction) but the **composition laws constrain which drive models are admissible** (closure, confluence, associativity, a defined pushforward under member identification), and they are drive-independent. A drive basis alone does not determine the merge or split law; it needs the stated constraints, and nobody has combined the two.

## What does it predict or control, and how well?

- **Marvel et al.**: Zachary split reproduced with 1 error in 34 **after** a tuned offset of 0.58 (or a substituted -11 between leaders); WWII alignment 15 of 17 countries with the authors' conversion of a landscape-theory matrix, versus 16 of 17 for the original landscape theory. In-sample, hand-converted inputs, no out-of-sample test; the authors disclaim quantitative prediction. Predicts **membership of factions**, not timing.
- **Palla et al.**: associations on two data sets of >30,000 and >4 million people: lifetime by size and stationarity; leave probability by commitment ratio. No held-out prediction of merges/splits in the text read; effect sizes are in figures not extracted.
- **Niwa**: scaling collapse across five fish data sets; predicts the **shape** of the size distribution; not which school splits.
- **Hill et al.**: ratio about 3 for three taxa, 3.8 for orca; descriptive.
- **Blondel et al.**: provable separation >= 1; stable equilibria need >= 2 for equal weights (Theorem 2), close to the observed 2.2 but without a guarantee of reaching one; no empirical test.
- **Apt-Witzel, Spivak, Fong, Baez et al., Milner**: no empirical test; guarantees only.
- **Control.** Nothing here controls a real group. Marvel et al.'s attention-steering proposal is hypothetical; Apt-Witzel's merges are voluntary by construction. Whether any steering of merge or split works by consent or manipulation is unanswered by this literature.
- **Failures and limits noted by authors**: jammed states in discrete balance dynamics (Antal et al. 2005, Marvel et al. 2009, as cited by Marvel et al. 2011), exponential time to balance for LTD with p < 1/2, non-existence of Dc-stable partitions (Example 11), the failure of Theorem 1 for countably many agents, quasi-strong connectivity insufficient for modulus consensus (Meng counterexample), unexplained cluster spacing (Blondel).

## Unconfirmed

- Altafini 2013: theorem statements, the continuous model, the zero-limit claim for unbalanced graphs (unread).
- Harary 1953 and Cartwright-Harary 1956: the balance theorem itself (taken from Marvel and Antal). Davis 1967 clusterability.
- Zachary 1977: the max-flow/min-cut prediction of the club split often attributed to it (not read; Marvel et al. use his capacity matrix).
- Bonabeau, Dagorn, Freon 1999: the exponent -3/2 and its dimension dependence (only as Niwa reports).
- Liebovitch et al. 2008 Section 3.7 (carried from 20).
- Kulakowski, Gawronski and Gronek 2005 (origin of dX/dt = X^2), Pettigrew's contact work, Marlowe 2005, Zhou et al. 2005, Hamilton et al. 2007, Aumann-Dreze, Hart-Kurz, Riker's size principle (in 10), Price 1972, Okasha 2006.
- A later reanalysis of hamadryas layers reported by a search result (mean ratio 3.28 without the clan layer, 6.17 with it): not read; do not use.
- Whether any human group-fission dataset with a tested rule exists (searches here did not find one; Zachary is the single canonical case and is n = 34). Re-searched 2026-10-30: Walker and Hill, "Causes, consequences, and kin bias of human group fissions", *Human Nature* 25: 465-475 (2014), DOI 10.1007/s12110-014-9209-0 (Crossref-verified), is a cross-cultural review of fissions with a kin-assortment index tested on Ache and Piaroa fissions, per the search summary. Not read, `[sa]`; it is the nearest candidate and should be read before "none exists" is repeated.
- Apt and Radzik 2006 (arXiv cs.GT/0605132): the TU-game original of Theorem 15 and the non-Dc-stable unique-outcome example, known only through Apt and Witzel's statement.
- Leifer and Milner 2004 (Cambridge TR 598): the proof of Milner's Theorem 4.6.
- Hill et al. Table 1 values (gelada 345.3, 99.3, 27.9, 12.2, 5.1) and the Horton-Strahler method: not re-opened in the 2026-10-30 validation (PMC returned a bot check, Europe PMC full text a 500); only the abstract was re-read.
- Whether a cospan/bigraph model of a human group with drive decorations has been published (none found; absence is only as strong as the search).

## Validation log (2026-10-30)

Every DOI below was resolved at api.crossref.org this pass; title, authors, venue, volume and pages matched unless noted. "Opened" means the primary text was fetched and the cited passages were read by the validator.

- ✎ Apt and Witzel 2009 (opened, arXiv v3): Note 2, Note 3, the average/elitist/egalitarian counterexamples, the majority-order intransitivity, Def 9, Thm 10, Ex 11, Lemma 13, Thm 15 and the sec 7.2 hedonic example all match. Fixed: the game composition is Owen's (2001, p. 241), not theirs; the semi-union result needs strictly superadditive games; Thm 15 generalises Apt and Radzik 2006, which also shows Dc-stability is sufficient but not necessary for a unique outcome (composition law 4 reworded).
- ✎ Antal, Krapivsky and Redner 2006 (opened): the CTD ln N time, the rho_0 < 0.4 and about 2/3 thresholds, the mean-field 1/2, <delta^2> = 2 rho_inf - 1, "irregardless" and the WWI Fig 10 all match. Fixed: the LTD rule (p applies only to one-unfriendly triads); the CTD rule (flip if the count decreases, or with probability 1/2 if unchanged); finite-N LTD times e^(N^2), N^(4/3) and ln N added. **Jammed states do not appear in this paper.** The summary, inventory and failures list credited them to it; they now go to Antal et al. 2005 PRE and Marvel et al. 2009 PRL (both DOIs verified).
- ✎ Marvel, Kleinberg, Kleinberg and Strogatz 2011 (opened, arXiv v1): eqs 1-5, the three conditions, Thm 2, Thm 3, the 0.58 offset, the -11 substitution, Denmark/Portugal, the "cartoon" quote and the attention strategy all match. Added: Zachary's own method also misclassified 1 of 34; the sign pattern stabilises *before* the blow-up (the 060 cross-check verdict is corrected to say so).
- ✎ Meng, Shi, Johansson, Cao and Hong 2016 (opened, arXiv v2): Assumption 2.1, Thms 2.1-2.3, Def 2.2, the 3-node counterexample and Remark 2.1 match. Added: in their unbalanced simulation all states go to zero, which the theorems do not force.
- ✎ Blondel, Hendrickx and Tsitsiklis 2009 (opened, arXiv v4): eq 1, Thm 1, Prop 2 decomposition, mean not preserved, ceil(L)+1, 5.1 and 3.833, no n-independent time bound and the countable-agent failure all match. **Corrected**: the file said the 2.2 spacing has "no explanation or nontrivial lower bound". That is the paper's description of the state of the art *before* it. Its own Thm 2 proves that stable equilibria need spacing >= 2 for equal weights, or > 1 + min/max weight otherwise, which the authors say "comes close to a full explanation"; what remains open is convergence to a stable equilibrium. Also corrected "merged position not a function of parts": two isolated point clusters merge at their weight-centre.
- ✓ Niwa 2004 (opened): the Bonabeau-Dagorn description, the -3/2 mean-field exponent, density/break-up linearity, the 0.7-1.8 range, five data sets and dimension independence match (the fitted exponent is beta = 0.996 ± 0.015).
- ✓ Palla, Barabasi and Vicsek 2007 (opened): data sizes, 2.9/5.9, the joint-graph matching, zeta, the size-by-stationarity reversal, w_out/(w_in+w_out) and the 30-35 zip-code peak match.
- ✓ Aureli et al. 2008 (opened, eva.mpg.de scan): Kummer's term, "extent of variation...", three dimensions, "not ... an actual dichotomy", agent-based null models and the Marlowe 2005 humans line match. Crossref gives 19 authors, with Aureli, Schaffner and Boesch first (the workshop organisers) and the rest alphabetical, Bearder fourth.
- ? Hill, Bentley and Dunbar 2008: the abstract was re-read via the Europe PMC API ("almost exactly 3", 3.8 for orca, "between three and four" for humans, "fundamental question"). The full text was blocked (PMC bot check, Europe PMC 500), so the Table 1 values were not re-checked and stay as the earlier pass read them.
- ✓ Spivak 2013 (opened, arXiv 1305.0297): the slogan, the sec 6.1 future work (operad object in Cat, "sums or averages") and the sec 6.2 states quote match. No DOI (preprint).
- ✓ Fong 2015 (opened, arXiv 1502.00872): Thm 3.4 hypotheses (finite colimits, braided monoidal D, lax braided monoidal F), the hypergraph category, Thm 4.1 and the resistor power Q(psi) match. TAC DOI verified.
- ✓ Baez, Foley, Moeller and Pollard 2020 (opened, arXiv v4): the Thm 3 equations (the file lists a subset of the 12), Thm 49 and the search-and-rescue origin match.
- ✎ Milner 2005, TR 614 (opened): the abstract, Def 8.14 quote, Thm 4.6 and Fig 1 match. Credit added: the Thm 4.6 proof is in Leifer and Milner TR 598. Nuance added: Krivine, Milner and Troina 2008 "Stochastic bigraphs" (DOI verified, not read) adds rates.
- ✓ Clarke 2016 (opened, PhilSci 10939 preprint): the decomposition Cov = Cov[Exp_g] + Exp[Cov_g], the "mathematical theorem, guaranteed by the logic of covariance and of expectation" quote and the subtractability thesis match (fitness is written omega in the source). BJPS DOI verified.
- ✓ Altafini 2013: DOI verified; content stays `[sa]`, correctly flagged.
- ✓ Harary 1953: DOI verified (Michigan Math. J. 2, 1953; the first lookup failed transiently, the retry resolved it); content stays `[sa]`.
- ✓ Zachary 1977: DOI verified (J. Anthropol. Res. 33(4): 452-473); `[sa]`.
- ✓ Bonabeau, Dagorn and Freon 1999: DOI verified (PNAS 96(8): 4472-4477); `[sa]`.
- Absence tests: "three or more factions" is weakened by Shang 2019/2020 (at most four factions, `[sa]`); "no tested human fission rule" now has Walker and Hill 2014 as the nearest candidate (`[sa]`); "no quantities in bigraphs" now separates pure bigraphs from stochastic bigraphs. No cospan or bigraph model of a human group with drive decorations turned up.

Sources opened this pass: 14 (13 full texts plus the Hill abstract). Fabrications: none found; every cited work exists with the stated authors.

**Verdict.** The file is substantially accurate. Its quotations, equations and theorem statements check out against the primary texts for every source that was opened. Two errors mattered. Jammed states were misattributed to the Antal Physica D paper. And Blondel et al. were reported as saying the 2.2 cluster spacing is unexplained, when their own Theorem 2 nearly explains it, which also corrects the "no merge rule" claim for isolated clusters. Both are fixed. Nothing `[sa]` feeds an equation, and the "nowhere" claims are now hedged where a search found partial counter-examples.

## Cross-checks (2026-10-30)

Grepped against the other files in `docs/prior-work/` by author, title, equation and number. Nothing else in the directory was edited. Overlap is with 04, 05, 08, 09, 14, 29, 040/40, 043, 055, 060, 063, 084, 085, 089, 091 and 42. Files 01-03, 06-07, 10-13, 15-22, 23 (via 060's cross-check) and most of the rest have no overlap with these works.

### Agreements

- **Marvel et al. (dX/dt = X^2).** Eqs 1-5, the three conditions, the two-faction partition and the mu > 0 / mu <= 0 rule all match 060 section 5. 060 said its empirical section was not read; this file reads it (Zachary offset 0.58; WWII 15 of 17).
- **Balance, complete graphs.** 084 section 2 (Cartwright and Harary 1956, read in full) gives the two-faction statement. 084 states the theorem for all cycles and treats the triangle form as a corollary for complete graphs. This file uses the complete-graph form only, so the two are consistent. Attribution to Harary 1953 stays `[sa]`.
- **Jammed states.** 084 and 060 cite Antal et al. 2005 (PRE) and Marvel et al. 2009 (PRL) without content. That agrees with this file's correction that jammed states are not in the Physica D paper.
- **Meng et al. Thm 2.1 (modulus consensus).** 085 section 4 (Liu et al., Proposition 1, citing Meng Thm 2.1) states the same result.
- **Price decomposition as an identity.** 09 section B2 and the summary at 09 line 12 say the Price equation is "an identity, not a model". Clarke eq 1 in this file is consistent with that.
- **Ratio about 3, no mechanism.** 091 section 3b (Zhou, Sornette, Hill and Dunbar 2005, read: pooled mean ratio 3.52, "no obvious reason") agrees on the absence of a mechanism. 091 does not contain the 2008 taxon values.
- **Krause cluster count.** 05 (roughly 1/(2d) clusters on [0,1] at threshold d) agrees with Blondel et al.'s coefficient slightly below 1/2 at threshold 1. The 2.2 spacing appears in no other file.
- **Operads and wiring diagrams.** 14 section 3a and 40 section 1a agree on n inner boxes with one outer box, associativity, and the state law sitting in the algebra. 14 section 3c calls a network model a lax symmetric monoidal functor to Cat; this file's one-coloured case (to Mon) is a specialisation of that, not a conflict.
- **Decorated cospans.** 043 section 4 (Fong 2015, Def 3.1, Prop 3.2 and Thm 3.4 read) agrees with composition by pushout over the shared feet.
- **Bigraphs.** 04 section 13 agrees that bigraphs are closest to the form, that Milner's stated motivation was ubiquitous computing, and that no bigraph model of a human group was found.
- **Fission-fusion definition.** 29 E2 (standard account, same DOI) describes the same definition: variation over time in spatial cohesion and individual membership.

### Contradictions (unresolved, both claims recorded)

1. **Altafini: "bipartite consensus iff structurally balanced, otherwise convergence to zero".**
   - Claim A (060 section 5, `[abs]`/`[std]`; repeated in 23 section 10 as cited at 060 line 244): "iff balanced ... otherwise convergence to zero". 090 section 5 says "strongly connected and structurally imbalanced gives stability to zero; otherwise convergence into clusters (Theorem 29)". 060 line 263 and 085 section 4 disagree on the connectivity hypothesis.
   - Claim B (083 section 2.4 and the verdict on 23 above): Meng et al.'s theorems give only the sufficiency direction (balanced with negative arcs appearing infinitely often gives bipartite consensus). The zero claim is not established by them.
   - 085 section 4 [read] reports Altafini 2012 (PLoS ONE, read in full) and Proskurnikov, Matveev and Cao 2016 (read): for strongly connected graphs an unbalanced graph gives zero; a non-strongly-connected counterexample exists.
   - Verdict: **unresolved**. The 2013 TAC text is unread by every file (`sa`), so the claim cannot be settled here.

2. **Aureli et al. 2008: operand is a partition.**
   - Claim A (29 E2, `[standard account]`, author list from memory): "operand = partition of the individuals ... a partition lattice is the natural formalism".
   - Claim B (083 section 3.1, read from the JSTOR scan): Aureli et al. use three scalar variabilities (cohesion, party size, party composition) and no partition formalism.
   - Verdict: **unresolved**. The validation log of 29 checks the author list and the DOI, not this point. This file's reading is from the primary text and is the stronger source for what Aureli says; 29's wording should be corrected or attributed to Apt and Witzel.

### Duplicates and overlaps

- Marvel eqs 1-5 and the faction rule: already in 060 section 5 (`dup_of` set on the ledger lines).
- Price identity: 09 section B2.
- Ratio about 3 with no mechanism: 091 section 3b (different work, Zhou et al. 2005).
- Fission-fusion definition: 29 E2 (see contradiction 2).
- Milner, bigraphs and the no-human-model finding: 04 section 13.
- Operad and wiring: 14 section 3a, 40 section 1a. Network model: 14 section 3c. Decorated cospans: 043 section 4.
- Krause clusters: 05 (Hegselmann-Krause description; different paper).

### Namesakes (no overlap, do not conflate)

- Bonabeau in 42 section 1.2 and 29 A1 is Bonabeau, Theraulaz and Deneubourg (1995/1996). This file's Bonabeau, Dagorn and Freon (1999) is a different paper and a school-merging model.
- Clarke in 08 is Clarke and Stone (2008, selectorate critique). This file's Clarke (2016, BJPS) is a different author.

### Not in any other file (no cross-check possible)

Palla et al. 2007, Niwa 2004, Zachary 1977, Blondel et al. 2009, Apt and Witzel 2009, Shang 2019/2020 (89 mentions a different Shang, a 2006 purge), Walker and Hill 2014, Hill et al. 2008 taxon values, Spivak-only results beyond 14/40.

### Related, not duplicated

- 084 section 5 read Facchetti, Iacono and Altafini (PNAS 2011): global balance as a spin-glass ground state. It bears on the balance-closure question in section 2.1 here but is not cited in this file.
- 084 section "What does it predict or control" notes Askarisichani et al. 2019 (abstract read): an unbalanced configuration resists change. That is a dynamics result for the Antal and Marvel models, not yet cited here.

Ledger lines for this direction are returned in the structured output and have not been committed.

## Licences of quoted and transcribed material (2026-10-30)

Quotations in this file are short phrases (under 60 words each) with citation. Numbers and equations are facts or restated in the file's own notation. No table, dataset or paywalled text is reproduced.

- Apt and Witzel 2009 (arXiv 0709.0435): arXiv licence not determined; publisher copyright presumed. Short quotations and restated definitions.
- Marvel et al. 2011 (PNAS, arXiv 1010.1814): licence not determined; publisher copyright presumed. Two short quoted phrases (attributed above) and restated dynamics.
- Antal, Krapivsky and Redner 2006 (arXiv physics/0605183): not determined; publisher copyright presumed. Short quotations, restated dynamics.
- Meng et al. (arXiv 1402.2766), Blondel et al. (arXiv 0807.2028): not determined; publisher copyright presumed. Restated statements.
- Aureli et al. 2008 (Current Anthropology): publisher copyright, paywalled. Short quotations only. The JSTOR scan on eva.mpg.de should be confirmed as a copy the project may hold, or its origin recorded; the scan is not redistributed in the repo.
- Niwa 2004 (arXiv q-bio/0402003): not determined; publisher copyright presumed. Five fisheries data sets cited by name with fitted exponents (dataset citation); raw data not reproduced; data terms not recorded.
- Palla, Barabasi and Vicsek 2007 (arXiv 0704.0744): not determined; publisher copyright presumed. Dataset citation only: cond-mat co-authorship records (arXiv terms not recorded) and a company's mobile-phone call records (private operator data, not redistributed, terms not recorded); only summary statistics (weight ratios) reported.
- Hill, Bentley and Dunbar 2008 (Biology Letters, PMC): licence not checked; publisher copyright presumed. Five Table 1 values for gelada (mean 345.3, 99.3, 27.9, 12.2, 5.1) given as facts with citation, a description of a table row; values not re-checked against the full text. Short quotations.
- Spivak 2013 (arXiv 1305.0297), Fong (arXiv 1502.00872), Milner TR 614, Clarke 2016: not determined; publisher copyright presumed. Restated definitions and theorems.
- Baez, Foley, Moeller and Pollard (Theory and Applications of Categories 35, arXiv 1711.00037): journal licence not recorded here; publisher copyright presumed. Six of the equations of Theorem 3 restated in the file's own notation, a subset, with citation.
- Zachary 1977 karate-club capacity matrix (via Marvel et al. 2011): not determined; publisher copyright presumed (paywalled). Results only; matrix not reproduced and not held in the repo.
- Axelrod and Bennett 1939 propensity matrix, 17 countries (via Marvel et al. 2011): not determined; status of 1939 source unknown. Described and scored only, not reproduced.
- Sources read only at second hand (Altafini, Harary, Bonabeau et al., Liebovitch et al., Aumann and Dreze, Hart and Kurz, Davis): not determined; publisher copyright presumed. Cited, not quoted.
