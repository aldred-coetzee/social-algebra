# Prior work 063: French, DeGroot, Friedkin-Johnsen and Hegselmann-Krause at source, and which convergence theorems carry over to a vector of drives with stubbornness as an anchor

Direction: D208

Date: 2026-10-29. Kind: deep-read. Cross-references files 05 (influence and opinion control), 16 (formal models of motivation), 20, 23 and 50, and does not repeat their bibliographies.

**Method and honesty note.** What was read in full at source this session, tagged [read]: Hegselmann & Krause 2002 (JASSS PDF: the model section, the "results" section and the whole appendix of theorems); Proskurnikov & Tempo 2017 Part I and 2018 Part II (arXiv PDFs; these are tutorials, so they count as a primary source for the *statements* of theorems and a secondary source for who proved them first); Parsegov, Proskurnikov, Tempo & Friedkin 2017 (arXiv v5 PDF: the model, Theorems 2 and 3, Remarks 1 and 3, the identification section header). Not read at source, and tagged [standard account] or [not read]: French 1956, Harary 1959, DeGroot 1974 (the equation is known from the secondary papers above), Friedkin & Johnsen 1990 and 1999, Lewin 1936/1951, Festinger 1950, McClelland 2004, Bosse et al. 2015. The fetches for Bosse et al. (Springer redirect, CoMSES page without equations) and McClelland (Academia 403) failed, so **no equation of either is transcribed here**. DOIs resolved at Crossref this session are marked [Crossref]; one DOI I first guessed for McClelland resolved to an unrelated paper and was discarded, which is the reason the guess rule exists.

**The question, restated.** Aldred's target is an algebra of drives (curiosity, fear, desire) of persons and groups, with equations, theorems, prediction and control. The linear-averaging family is the one mature body of theorems about *a state vector plus an influence graph*. The question is how much of it survives when (a) the state of each agent is a vector of drives, not one opinion, and (b) "stubbornness" means an anchor: a pull towards a fixed baseline. Short answer: **everything survives if drives do not interact within a person; most of it survives if they do, with a single clean stability condition (rho(Lambda W) rho(C) < 1); almost none of the nonlinear (bounded-confidence) results survive in the form needed, and the asymmetric, heterogeneous case is described by its own reviewers as unsolved.** Details below.

---

## 1. Citations and verification

| Work | Citation | Verification |
|---|---|---|
| French 1956 | French, J. R. P. Jr. (1956). A formal theory of social power. *Psychological Review* 63(3), 181-194. doi:10.1037/h0046123 | [Crossref] metadata only. Paper **not read**. |
| Festinger 1950 | Festinger, L. (1950). Informal social communication. *Psychological Review* 57(5), 271-282. doi:10.1037/h0056932 | [Crossref] metadata only. **Not read.** |
| DeGroot 1974 | DeGroot, M. H. (1974). Reaching a consensus. *JASA* 69(345), 118-121. doi:10.1080/01621459.1974.10480137 | [Crossref] metadata only. **Not read**; the theorem is read as restated in H&K 2002 Appendix and P&T 2017. |
| Friedkin & Johnsen 1990 | Friedkin, N. E. & Johnsen, E. C. (1990). Social influence and opinions. *J. Math. Sociol.* 15(3-4), 193-206. doi:10.1080/0022250X.1990.9990069 | [Crossref] pages 193-206 (file 05 notes a 193-205 variant). **Not read**; theorem read as restated in H&K 2002 (Theorem 3, citing "Friedkin and Johnsen 1990, Appendix") and P&T 2017. |
| Friedkin & Johnsen 1999 | "Social influence networks and opinion change", in Thye, Lawler, Macy & Walker (eds), *Advances in Group Processes* 16, 1-29 | Cited as [125] in P&T 2017 [read, reference list]; page range from my background, not checked; no DOI sought. **Not read.** |
| Hegselmann & Krause 2002 | Hegselmann, R. & Krause, U. (2002). Opinion dynamics and bounded confidence: models, analysis and simulation. *JASSS* 5(3), 2. https://www.jasss.org/5/3/2.html (PDF at /2/2.pdf) | **Read** (full PDF fetched; text extracted). JASSS has no DOI. |
| Proskurnikov & Tempo 2017 | A tutorial on modeling and analysis of dynamic social networks. Part I. *Annual Reviews in Control* 43, 65-79. doi:10.1016/j.arcontrol.2017.03.002 [Crossref]; arXiv:1701.06307 | **Read** (sections 3, 5, 6). |
| Proskurnikov & Tempo 2018 | ... Part II. *Annual Reviews in Control* 45, 166-190. doi:10.1016/j.arcontrol.2018.03.005 [Crossref]; arXiv:1801.06719 | **Read** (section 4, bounded confidence). |
| Parsegov et al. 2017 | Parsegov, S. E., Proskurnikov, A. V., Tempo, R. & Friedkin, N. E. (2017). Novel multidimensional models of opinion dynamics in social networks. *IEEE Trans. Autom. Control* 62(5), 2270-2285. doi:10.1109/TAC.2016.2613905 [Crossref]; arXiv:1505.04920 (v5) | **Read** (sections IV-V, proofs sketched in the appendix not checked line by line). |
| Bosse et al. 2015 | Bosse, T., Duell, R., Memon, Z. A., Treur, J. & van der Wal, C. N. (2015). Agent-based modeling of emotion contagion in groups. *Cognitive Computation* 7(1), 111-136. doi:10.1007/s12559-014-9277-9 [Crossref; Crossref dates it online 2014-06-14] | Metadata and a two-sentence abstract only. **Not read.** |
| McClelland 2004 | McClelland, K. (2004). The collective control of perceptions: constructing order from conflict. *Int. J. Human-Computer Studies* 60, 65-99. doi:10.1016/j.ijhcs.2003.08.003 [Crossref] | Metadata only. **Not read.** A later chapter by the same author, "Understanding Collective Control Processes" (in *Purpose, Meaning, and Action*, 2006, pp. 31-56, doi:10.1007/978-1-137-10809-8_2 [Crossref]), exists and also was not read. |
| Lewin 1936 / 1951 | Lewin, K. (1936) *Principles of Topological Psychology*; (1951) *Field Theory in Social Science* | Not read; file 16 section 4 holds what exists. |
| Surveys of bounded confidence in vector form | Lorenz, J. (2007). Continuous opinion dynamics under bounded confidence: a survey. *Int. J. Mod. Phys. C* 18, 1819-1838. doi:10.1142/S0129183107011789 [Crossref] | Metadata only; **not read**. Listed because it is the standard survey of the multidimensional case. |

---

## 2. The unified object, as H&K 2002 and P&T state it [read]

Everything in this family is one map on a state array with a row-stochastic matrix.

**General model (H&K 2002, eq. GM) [read].** Agents i = 1..n, opinions x_i(t) in R, weights a_ij >= 0 with sum_j a_ij = 1 (self-weight a_ii included):

    x_i(t+1) = a_i1 x_1(t) + ... + a_in x_n(t)      (2.1)
    x(t+1)  = A(t, x(t)) x(t)                        (GM)

Specialisations, all verbatim from the paper:
- Classical (French-DeGroot): `x(t+1) = A x(t)`, A fixed stochastic (CM).
- Friedkin-Johnsen: `x_i(t+1) = g_i x_i(0) + (1 - g_i)(a_i1 x_1(t) + ... + a_in x_n(t))`, i.e. `x(t+1) = G x(0) + (I - G) A x(t)` (FJ), G = diag(g_i), 0 <= g_i <= 1. "Agent i adheres to his initial opinion to a certain degree g_i and by a susceptibility of 1 - g_i the agent is socially influenced." G = 0 gives CM. [read]
- Time-variant: `x(t+1) = A(t) x(t)` (TV).
- Bounded confidence: `I(i,x) = { j : |x_i - x_j| <= eps_i }`, `x_i(t+1) = |I(i,x(t))|^{-1} sum_{j in I(i,x(t))} x_j(t)` (BC); weight a_ij(x) = 1/|I| on I and 0 off it. [read]

**Notation reconciliation (important when reading across papers).** H&K stubbornness g_i = P&T's (1 - lambda_i), where P&T write the Friedkin-Johnsen model as

    x(k+1) = Lambda W x(k) + (I - Lambda) u          (P&T 2017 eq. 20) [read]

with Lambda = diag(lambda_i) the *susceptibility*, W stochastic, u a constant vector of "prejudices". Agent i is **stubborn** if lambda_i < 1, **totally stubborn** if lambda_i = 0; with u = x(0) it is exactly H&K's FJ. P&T state that Friedkin and Johnsen "traditionally" take u = x(0) and the coupling 1 - lambda_i = w_ii (anchorage equals self-weight), and **deliberately do not adopt that coupling**: "allowing the prejudices and initial opinions to be independent; the same holds for the matrices Lambda and W." [read, P&T 2017 section 6]. This matters for us: **u can be a baseline or set point that is not the starting state.** Terminology collision to avoid: P&T's "oblivious" is an agent that is neither stubborn nor influenced by a stubborn agent; "stubborn" in the old DeGroot-with-zealots literature is the totally stubborn case.

**Continuous-time cousins [read, P&T 2017 sec 4-5].** Abelson: `dx_i/dt = sum_j a_ij (x_j - x_i)`, i.e. `dx/dt = -L[A] x`. Taylor model with anchor: `dx_i/dt = sum_j a_ij (x_j - x_i) + gamma_i (u_i - x_i)`, gamma_i >= 0 (eq. 14), i.e. `dx/dt = -(L[A] + Gamma) x + Gamma u` (eq. 15). Agent i is "prejudiced" if gamma_i > 0; if u_i = x_i(0) and a_ij = 0 the agent is stubborn, x_i(t) = u_i.

---

## 3. Theorems for the linear family, stated at source

### 3.1 DeGroot / French (no anchor)

- **H&K 2002 Appendix, Theorem 1 [read].** Consensus property: for every x(0) there is c with x_i(t) -> c for all i. (i) If any two agents i, j have some k with a_ik > 0 and a_jk > 0, the consensus property holds (credited to DeGroot 1974). (ii) The consensus property holds iff some power A^{t0} has at least one strictly positive column (credited to Berger 1981).
- **H&K 2002 Appendix, Theorem 2 [read].** With A in Gantmacher normal form, diagonal blocks A_i, g essential groups: lim x(t) exists for every x(0) iff all A_i, 1 <= i <= g, are primitive, equivalently iff 1 is the only root of A of modulus 1; consensus iff g = 1 and A_1 primitive. "For the final stable opinion pattern only the initial opinions of essential agents play a role."
- **P&T 2017, Theorem 12 [read]** (cited there to refs [10, 86]). The model x(k+1) = W x(k) is convergent iff all closed strong components of the influence graph G[W] are aperiodic; it reaches consensus iff G[W] is quasi-strongly connected (has a directed spanning tree) and the only closed strong component is aperiodic. **Corollary 13 [read]**: if all self-weights w_ii > 0, the model is convergent, and reaches consensus iff G[W] is quasi-strongly connected. P&T say the second part of Corollary 13 "was proved in [76]" (Harary 1959) "and included, without proof, in [53, Chapter 4]", and add a footnote that "formally, [53, 76] address only the French model, however, the proof uses only the diagonal entries' positivity". That is a primary-text statement on the Harary dispute (D211 owns the settlement; this is one data point for it, not a resolution).
- **P&T 2017 (8) [read].** Under full regularity, `x(k) -> (p_inf^T x(0)) 1`, with p_inf the left eigenvector of W; p_inf,i is French's measure of social power ("the weight of its initial opinion x_i(0) in the final opinion of the group").
- **P&T 2017, Corollary 14 [read].** s >= 1 totally stubborn agents (source nodes) that reach all others: the model converges, and the limit is fully determined by the stubborn agents' opinions; with exactly one stubborn agent reaching all, consensus on its opinion; with two or more, consensus among them is "obviously, impossible".
- **Contraction property [read, P&T 2017].** min_i x_i(k) is non-decreasing and max_i x_i(k) is non-increasing: the profile never leaves the convex hull of the initial profile. The system is Lyapunov stable but never asymptotically stable (eigenvalue 1).

### 3.2 Friedkin-Johnsen (anchor)

- **H&K 2002 Appendix, Theorem 3 [read]** (credited to Friedkin and Johnsen 1990, Appendix). With M = (I - G)A and V(t) = (M^t + sum_{k<t} M^k) G so that x(t) = V(t) x(0): let G != 0 and A irreducible. Then for every x(0) the limit exists and **x(inf) = (I - M)^{-1} G x(0)**. Consensus x(inf) = (c..c) holds iff x_i(0) = c for all i with g_i > 0. H&K gloss (Result 3): "in the case of positive degrees one can expect a consensus only for very special initial profiles", and note a four-agent worked example from Friedkin & Johnsen 1999 p. 6 (initial (25, 25, 75, 85) goes to (60, 60, 75, 75)).
- **P&T 2017, Theorem 21 and Corollaries 22-23 [read].** Split agents into **P-dependent** (prejudiced, lambda_i < 1, or reachable by a walk from a prejudiced agent) and **P-independent**. Then Lambda^11 W^11 is Schur stable (rho < 1) on the P-dependent block; the full model is convergent iff r = n or the P-independent block W^22 is regular; the limit is x(inf) = V [u^1; x^2(inf)] with V = (I - Lambda^11 W^11)^{-1} [(I - Lambda^11) ... Lambda^11 W^12] **stochastic**, so the final opinion of every agent is a convex combination of the prejudices and of the final opinions of the P-independent agents. Corollary 22: asymptotically stable iff every agent is P-dependent, then V = (I - Lambda W)^{-1} (I - Lambda); holds in particular if Lambda < I, or Lambda != I and W irreducible. Corollary 23: convergence iff A = Lambda W is regular. P&T note this "is formulated in [19, 125] without rigorous proof".
- **Taylor / Abelson continuous analogue [read].** Theorem 18 (P&T 2017): the P-dependent block is asymptotically stable ("-(L11 + Gamma11) is Hurwitz") and x^1(inf) = M [u^1; x^2(inf)] with M stochastic. Corollary 19: -(L[A] + Gamma) is Hurwitz iff **every** agent is P-dependent.
- **Theorem 20 (P&T 2017, containment) [read; cited there to ref 115].** For the vector-valued Taylor model with k static "leaders" s_1..s_k in R^d, the following are equivalent: (1) Hurwitz stability; (2) every agent is directly or indirectly influenced by a leader; (3) every agent's final position lies in the convex hull S of the leaders for every choice of leaders and initial conditions. The proof is by projection: for v in R^d, v^T x_i obeys the scalar model, so v^T x_i(inf) >= min over S of v^T s for all v, and S is convex. **This projection argument is the whole reason the linear theorems extend to vectors for free** (see section 5.1).

**Empirical remark attached to these by the reviewers [read].** P&T 2017 section 6: FJ "has been experimentally validated for small and medium-size groups, as reported in [19, 93, 125-127]" (Friedkin's own group's work; file 05 and direction D210 are the places to check independence). Parsegov et al. 2017 Example 2 uses a model "reconstructed from real data, obtained in experiments with a small group of individuals" via a method in their ref [15] (Friedkin, Proskurnikov, Tempo & Parsegov 2016, *Science* 354, 321-326 per file 05).

---

## 4. Bounded confidence at source

### 4.1 Scalar model, H&K 2002 [read]

- Properties (H&K section 3D, credited to Krause 2000), symmetric uniform eps: (I) order of opinions preserved; (II) a split (|x_i - x_j| > eps) persists forever; (III) if consensus is approached the initial profile is an eps-profile (sorted adjacent gaps <= eps); (IV) for n = 2, 3, 4 consensus iff eps-profile; false for n = 5 (an eps-profile need not reach consensus), true for an *equidistant* eps-profile at n = 5, false at n = 6. "A consensus will be reached in finite time, if there is a consensus at all."
- **Theorem 5 [read, Appendix]:** consensus in finite time if for some h and all m, any two agents i, j have a third k with confidence chains from both to k over the window ((m-1)h, mh). Proof "employs Theorem 4".
- **Theorem 6 [read, Appendix]:** for every initial profile there are a finite t* and a partition into maximal subgroups, each in exact consensus for all t >= t* (first proved by Dittmer 2000/2001 via an eps-chain result). Fragmentation into finitely many clusters is a theorem, not a simulation finding.
- Everything else in H&K section 4 (phase diagrams over eps, asymmetric intervals eps_l != eps_r, "one-sided splits", number of clusters as a function of n and eps) is **simulation**, and H&K say so: "rigorous analytical results are difficult to obtain" for the nonlinear case.

### 4.2 Vector (multidimensional) HK, P&T 2018 Part II [read]

- Definition: x_i(k) in R^m; trusted set I_i(x) = { j : ||x_j - x_i|| <= d } for a chosen norm (eq. 18), update = average over I_i. [read]
- **Theorem 13 [read]:** for **any** norm, the model terminates (reaches a fixed point) in finitely many steps. Proof route: write HK as a time-varying French-DeGroot model with state-dependent stochastic W(k), apply the Lemma-1 convergence conditions, then show finite-time termination by component-wise consensus. Best known bound 2n^4 steps for m >= 2 (Euclidean); lower bound Omega(n^2). [read, with citations to Bhattacharyya-Braverman-Chazelle-Nguyen, Etesami-Basar-Nedic-Touri, Martinsson]
- **What breaks relative to m = 1 [read]:** order preservation has no meaning; connected components of G(x) "can not only split, but also merge" (their tetrahedron example in R^3, Fig. 3, reaches consensus in 3 steps from a three-component start). Also, "two individuals that strongly disagree on the s-th issue ignore each other's positions on all remaining issues", the implicit coupling across issues that the trust ball imposes. **For drives this is the single most consequential structural fact about the nonlinear model**: a large gap in fear between two people shuts off the transmission of curiosity between them.
- **Distance-dependent generalisation [read]:** weights phi(||x_j - x_i||); Theorem 13's convergence holds (without finite-time) for phi in {0} U [a, b] with phi(0) > 0 (Lemma 14); "heterophily" kernels (moderately distant opinions attract more than similar ones) were reported to *facilitate* consensus (cited to [143]).

### 4.3 Bounded confidence with an anchor [read, P&T 2018 section 4.4]

- **Truth-seeking HK (Hegselmann & Krause 2015, *Networks and Heterogeneous Media* 10(3), 477-509, cited as [82]; the 2006 predecessor is [153])**: `x_i(t+1) = (lambda_i / |I_i|) sum_{j in I_i} x_j + (1 - lambda_i) T` with a single common truth T in R^m. **Theorem 17 [read]**: the opinions of all truth seekers (lambda_i < 1) converge to T; agents with lambda_i = 0 either converge to T or freeze at some value with |x_i - T| >= d. Convergence is asymptotic, not finite-time. Open: "when the opinions reach consensus at T in presence of agents with lambda_i = 0 still remains open." Simulation finding quoted from [82]: for some d, consensus is reached with few stubborn individuals and **destroyed as their number increases**.
- **Inertial HK (Chazelle & Wang 2017, *IEEE TAC* 62(8), 3905-3913, cited as [155]; ACC 2016 version doi:10.1109/ACC.2016.7525202 [Crossref])**: `x_i(t+1) = (1 - lambda_i) x_i(t) + (lambda_i/|I_i|) sum_{j in I_i} x_j` (eq. 33). **Theorem 18 [read, stated by P&T]**: if every lambda_i is in {0, 1} the opinions converge. Unlike Theorem 17, the stubborn agents need not share one opinion. Chazelle & Wang extend this to "anchored" HK systems with a mobile and a static part, "equivalent, in some sense, to a special case of the heterogeneous model (20)". P&T do **not** state that general lambda_i in (0,1) with heterogeneous anchors converges.
- **Caveat on time-varying graphs with anchors [read, P&T 2018 footnote 7]**: "opinions in the FJ model with time-varying influence graph can oscillate even when the graph remains strongly connected and some agents have lambda_i < 1" (their ref [97], Proskurnikov-Tempo-Cao-Friedkin, IFAC 2017). So *anchoring does not by itself guarantee convergence once the influence graph moves with the state.*
- **Asymmetric and heterogeneous confidence [read]:** asymmetric scalar intervals [x_i - d + eta_i, x_i + d], eta_i >= 0, eta = max eta_i < d: finite-time termination (Theorem 19, cited [133, 146]). But for heterogeneous left and right endpoints in general (36) "one arrives at a very complicated system, still waiting for thorough analysis", and the heterogeneous-radius multidimensional model (37) "remains a mystery" [P&T quoting 155]. General directed state-dependent graphs can be chaotic or even Turing-complete ("influence systems", Chazelle), though not robustly [P&T 2018, citing Chazelle].
- **Noise [read]:** "small additive noises destroy clusters in the HK model and lead to 'quasi-consensus'" (P&T cite [163]); non-local random interactions restore disagreement. Numerical HK is also reported sensitive to floating-point inaccuracy [82].

---

## 5. Which results carry to a vector of drives with a stubbornness anchor

Setting: n agents, m drives. X(k) in R^{n x m} (row i = agent i's drive vector, x_i(k) in R^m). Anchor U in R^{n x m}: baseline or set point of each drive for each person. Lambda = diag(lambda_i) susceptibility (so 1 - lambda_i is stubbornness / pull to baseline), W an influence matrix.

### 5.1 No cross-drive coupling inside a person: everything carries, per drive [theorem-level, from the sources above]

If each drive d has its own (Lambda_d, W_d, u_d) and the dynamics are `x^d(k+1) = Lambda_d W_d x^d(k) + (I - Lambda_d) u^d`, then the system is m **decoupled** scalar FJ systems, and Theorem 21 / Corollary 22 / the continuous Theorems 18-20 apply column by column. Concretely:
- **Stability** (every agent P-dependent for drive d) holds iff each drive's P-dependence condition holds. With Lambda_d < I for everyone, stable for any W_d.
- **Boundedness / box invariance:** x_i^d(inf) is a convex combination of prejudices and P-independent final values (V stochastic). So drive values stay in [min u^d, max u^d] when initialised there, which gives **bounded drive levels for free**: a property an algebra of non-negative graded drives needs.
- **Influence is factorable:** the limit is `(I - Lambda W)^{-1}(I - Lambda) u`. The map from baselines to equilibrium levels is a matrix V depending on (Lambda, W) only, **not on U**, so equilibrium drive = V U is linear in the baselines. That is an operator-on-operands form in the strict sense: V is a fixed operator, U the operand.
- **Control via P-dependence:** by Corollary 19 and Theorem 20, steering any individual to a target set (the convex hull of the sources) needs only that it be reachable from a source; the target is the hull, not an arbitrary point. This matches the "reachability claims have done better" note in notes/2026-10-29-drives-as-the-core.md.
- **What "same W for every drive" assumes:** the theory with one W lets the same people be influential on fear and on curiosity. Allowing different W_d per drive is still decoupled, so still covered, but then the algebra has m influence graphs rather than one. That is a modelling choice the sources do not make for us.

### 5.2 Cross-drive coupling inside a person: the one extension at source, with its stability condition

**Model [read, Parsegov et al. 2017, eq. 17].**

    x_i(k+1) = lambda_ii C sum_j w_ij x_j(k) + (1 - lambda_ii) u_i,     C in R^{m x m}

with C called the matrix of multi-issues dependence structure (MiDS). C = I_m is the ordinary FJ model. In stacked form (eq. 22):

    x(k+1) = [(Lambda W) (x) C] x(k) + [(I_n - Lambda) (x) I_m] u,

(x) the Kronecker product. **The model applies C *after* averaging the neighbours**: "the ith agent calculates the average sum_j w_ij x_j(k) of its own opinion and those displayed by the neighbors" and C then "adjusts and mixes the averaged topic-specific opinions". The prejudice term is **not** passed through C. C is assumed the same for all agents and independent of the network ("depending on introspective processes, forming an individual's belief system"). Meaning of an entry: c_pq is the contribution of the q-th issue of the averaged opinion to the p-th issue of the updated one.

**Theorem 2 (Stability) [read]:** the model is stable (Lambda W (x) C Schur stable) **iff rho(Lambda W) rho(C) < 1**. Then the limit is

    x'_C = (I_mn - Lambda W (x) C)^{-1} [(I_n - Lambda) (x) I_m] u.            (eq. 23)

If rho(C) = 1, stability equals stability of the plain FJ model, i.e. no oblivious agents. Remark 2: stability holds whenever the FJ model is stable and C is row-stochastic or satisfies ||C||_inf <= 1, but these are not necessary; "the system remains stable whenever rho(C) < rho(Lambda W)^{-1}". Proof is by the Kronecker spectrum lemma (spectrum of A (x) B is the products of eigenvalues) [read, proof of Thm 2 cited via Lemma 4].

**Theorem 3 (Convergence) [read]:** with oblivious agents present (n' < n non-oblivious), the model converges iff C is **regular** (lim C^k exists) and either C_inf = 0 or W^22 is regular; the limit is given by a block formula (eq. 24) involving (I - Lambda^11 W^11 (x) C)^{-1}.

**Invariance [read, Remark 1]:** if C is row-stochastic, box constraints [a, b] on every component are preserved; for [0, 1]^m it suffices that C is substochastic (c_ij >= 0, row sums <= 1); for [-1, 1]^m, ||C||_inf <= 1. More generally any convex set D with C D ⊆ D is invariant.

**Remark 3 [read]:** a more general initial-state map x_i(0) = D u_i leaves stability and convergence conditions unchanged and changes only the formula for the limit.

**What this buys the algebra.**
- **A clean stability margin trading stubbornness against intra-person drive gain.** If C encodes a within-person amplification, say fear feeds fear with gain above 1 (rho(C) > 1), the group is still stable provided rho(Lambda W) < 1/rho(C). Stubbornness (Lambda < I, so rho(Lambda W) < 1) is what *buys room* for self-amplifying drive coupling. Conversely with no anchor (Lambda = I, rho(W) = 1) any rho(C) > 1 destabilises. This is a theorem about the model as written [read]; whether human drive coupling has this form is untested.
- **Signed coupling is allowed.** Parsegov et al. give Example 4 with C_1 = [[0.8, 0.2],[0.3, 0.7]] (positive coupling) and a second example with negative off-diagonal coupling C_2 whose final opinions differ strongly; Theorem 2 only needs the spectral radius, so inhibitory cross-drive coupling (e.g. fear suppressing curiosity) is admissible. [read; the C_2 entries were not transcribed, only its effect]
- **Limitation, stated so we do not over-read it:** C is linear, constant, shared by all agents, and acts on the *social average*, not on the person's own drive history. A model in which a person's fear changes how they weigh others' curiosity (a person-specific, state-dependent C) is not covered by Theorems 2-3.
- **Identification:** Parsegov et al. give two procedures (finite-horizon with T rounds of recorded opinions, and infinite-horizon) reducing estimation of C to convex optimisation, assuming Lambda and W are known. [read: section header and setup only; the optimisation details were not checked]. Their numerical examples are illustrative (fish/salmon attitudes); I found **no application to measured data in that paper**.

### 5.3 Bounded confidence on a drive vector: what carries and what does not

| Property | Scalar HK | Vector HK, no anchor | Vector HK with anchor |
|---|---|---|---|
| Convergence | proved (Thm 6, H&K) | proved, finite-time, any norm (Thm 13, P&T) | proved only for lambda_i in {0,1} (Thm 18) or common T (Thm 17); general lambda_i in (0,1) with heterogeneous anchors: **not stated as proved** in what I read |
| Order preserved | yes | meaningless | meaningless |
| Clusters only split | yes (property II) | **no, components can merge** (R^3 example) | n/a |
| Finite-time | yes | yes | no for truth-seekers (asymptotic) |
| Cluster count / location | simulated, not proved | simulated, not proved | simulated; non-monotone in number of stubborn agents [82] |
| Heterogeneous radii | "mystery" | "mystery" (eq. 37) | not addressed |
| Asymmetric trust | finite-time under bounded asymmetry (Thm 19) | not proved | not proved |

Two further points that matter for design:
1. **Trust gating couples drives through the norm.** With the Euclidean or sup norm, a large gap on one coordinate switches off influence on all of them (P&T 2018, quoted above). If the algebra wants drive-specific gating (trust me about curiosity, not about fear), that is a *different* model: one trust set per coordinate, which is m scalar HK systems and therefore decoupled, with all the scalar results (and none of the cross-drive effects). The sources give no theorem for a hybrid.
2. **Thresholds are exactly what drive models like to have, but they come with no continuity.** HK's discontinuous trust set is why simulations are sensitive (floating-point and small noise, P&T 2018 [read]). The smooth-kernel alternatives (phi) preserve convergence (Lemma 14) but not finite-time termination.

### 5.4 Results that do **not** carry, and why

1. **Consensus.** Anchoring destroys consensus except when all anchored agents already agree (H&K Theorem 3 [read]; in the vector case, with a common coupling C, consensus within an anchor class requires the anchors to coincide in the C-transformed sense). For drives that is a feature: persistent differences in baseline fear are the expected outcome.
2. **Anything with amplification, limit cycles, escalation or satiation.** All the theorems above describe contractions inside the convex hull of anchors and initial states (for C stochastic) or a linear system with spectral radius less than 1 (for general C). There is no theorem in this family for a drive that *rises on its own* (hunger, boredom, ostracism-induced need), for homeostatic restoration towards a set point that moves with state, or for oscillation. The anchor u is constant. This is the main reason file 47's Keramati-Gutkin result and files 53-56 (despair tipping point, boredom, status as anti-homeostatic) are needed alongside.
3. **Asymmetric, expressiveness-weighted transmission.** Emotional contagion is asymmetric (who expresses, who is open). The HK convergence proofs rely on symmetric trust (an undirected influence graph, P&T 2018 section 4.4.3: asymmetric modifications "are much more complicated, and many of their properties observed in experiments are still waiting for mathematical investigation"). The *linear* theory handles asymmetry fully: W is any stochastic matrix, its asymmetry is what gives non-uniform social power p_inf.
4. **Time-varying or state-dependent W with an anchor.** Possible oscillation even on a strongly connected graph with lambda_i < 1 (P&T 2018 footnote 7).
5. **Negative (antagonistic) influence.** Not in this family. Altafini's signed-network model is a separate theorem set (file 05 and direction D215).

### 5.5 Where the psychology literature sits relative to the theorems

- **Lewin 1936/1951 [not read; file 16 section 4 holds the standard account].** Resultant force as a vector sum is a *source of the vocabulary* (state in a space, forces, locomotion) and has no theorem. The linear-averaging family can be read as one precise instance: the "force" on person i's state is `sum_j w_ij (x_j - x_i)` (Abelson form), plus `gamma_i (u_i - x_i)` for the anchor (Taylor form). I take that identification from the form of the equations, not from any author's claim; P&T do not attribute the models to Lewin in the passages I read, though their Part I reference list begins with Lewin's *Frontiers in group dynamics* [read, reference list]. **Do not write "Lewin proved" or "Lewin's model is FJ".**
- **Festinger 1950 [not read].** The standard account: group pressures to uniformity arise from the need to validate opinions by social reality and from locomotion toward group goals; pressure towards uniformity rises with the discrepancy and the cohesion. It is a *qualitative precursor* to French's formal power model. P&T and H&K both date the formal line to French 1956 and Harary 1959 [read: "An early formulation of such a model was given by J.R.P. French in 1956" H&K, "French formulated without proofs several conditions" P&T]. I did not verify Festinger's own formal content; treat the link as historical only.
- **French 1956 [not read].** Per P&T 2017, French's model is the iterated-averaging system on a power graph with positive diagonals and, in the example, uniformly distributed influence; its theorems were stated without proof and proved by Harary (see Corollary 13 above and the footnote caveat). H&K 2002 attribute to French the use of FJ-type models to "estimate from experiments the susceptibility of agents to interpersonal influence". That is H&K's wording and is odd, because FJ is 1990; I cannot verify the sentence and treat it as unreliable.
- **McClelland 2004 [not read].** Only a search-result description is available: two control systems holding one shared environmental variable at different references produce conflict and, per the 1993 talk "Conflictive Control" hosted on M. M. Taylor's PCT page, the variable behaves as if governed by a single **virtual controller whose gain is the sum of the competitors' gains and whose reference lies between theirs** [search/secondary; I could not verify the equation form]. File 16 records McClelland's virtual controller in its validation pass. This is the *only* member of the seed list that is a different mathematical type: **control loops on a shared variable rather than averaging**, and it addresses conflict and escalation, which the averaging family cannot.
- **Bosse et al. 2015 [not read].** Only the abstract is confirmed: an agent-based model of emotion contagion in groups, analysed by simulation and "mathematical analysis", embedded in an "ambient agent" that monitors group emotion and suggests support actions. A second-hand description says it is "thermodynamics based" and "relatively abstract" (Coenen & Broekens, as quoted in a search summary; the PDF was not retrievable). **No Bosse et al. equation is stated here; the direction asked for a transcription and I could not provide one.**

---

## 6. Operand/operator translation

- **Operand:** a pair (agent, drive vector x_i in R^m_{>=0}) together with, per agent, an **anchor** u_i in R^m (baseline/set point) and a **susceptibility** lambda_i in [0,1] (or its complement, stubbornness).
- **Operators:** (a) the **influence operator** W (stochastic, asymmetric allowed), acting on the array by row-averaging; (b) the **anchor operator** x -> (I - Lambda)u + Lambda x, a convex combination of state and baseline; (c) the **intra-person coupling** C (m x m), acting after averaging in the only extension that has theorems; (d) for bounded confidence, a **state-dependent** W(x).
- **Composition law, verified at source:** the one-step map is affine, `x -> (Lambda W (x) C) x + c`. Compositions of affine maps are affine; stability of the composite is determined by the spectral radius of the Kronecker product, which factorises: rho(Lambda W (x) C) = rho(Lambda W) rho(C) [Theorem 2, via the Kronecker spectrum lemma]. That is a *genuine algebraic law of the model*: **the social and the intra-personal parts compose by Kronecker product, and their stability margins multiply.** This is the nearest thing in the family to a theorem about composing two kinds of operator. It is the result most worth carrying into the algebra.
- **Theorem types available now:** existence and form of equilibrium (V U); convergence conditions (graph conditions plus regularity of C); convex-hull / box invariance; stability margin rho(Lambda W) rho(C) < 1; reachability by sources (Theorem 20, Corollary 19). Cross-checks against files: consistent with file 05's statement of FJ (its form `y(t+1) = A W y(t) + (I - A) y(1)` with `A = susceptibility`).
- **Not available:** a dynamics in which a drive grows by itself, or an interaction between a person's drive and the weight they put on others (state-dependent C or Lambda). Both must come from elsewhere in the survey.

---

## 7. Empirical standing (blunt)

- **French-DeGroot:** a mathematical object; its consensus prediction is the thing the field spent forty years explaining the absence of (Abelson's diversity puzzle, H&K intro quoting Abelson 1964: "what on earth one must assume in order to generate the bimodal outcome"). Experimental support for DeGroot-type updating exists but is file 05 / D210 territory.
- **Friedkin-Johnsen:** reviewers say experimentally validated for small and medium groups [read, P&T 2017]. The validations are by Friedkin and co-workers; independence is the open question (D210). In this reading the **only** FJ-family fit to measured data that I could see is Parsegov et al.'s Example 2 on a four-person group, and that model's parameters were fitted to the same experiment.
- **Hegselmann-Krause:** validated by its own simulations; scalar convergence theorems are real. The multidimensional and anchored cases have theorems for convergence but **no theorem for what the clusters are or how many**. No evidence in the sources read of vector HK being fitted to human data.
- **Multidimensional FJ with C:** no fit to data found. A procedure for fitting C exists on paper [read: section heading and set-up]. For a *drive* vector there is, as far as these sources show, no dataset in which both W and a multi-drive state were observed.
- **Application to drives specifically:** none of these papers has a drive as an operand. Opinions are "cognitive orientations towards objects" (P&T). The identification of opinion with drive level is an *assumption of this project*, not a result. A drive (fear) has a physiological and an action-readiness side that an attitude does not.

---

## 8. What exists vs what does not

**Exists (read at source):**
- A precise, complete theory of the *linear* anchored averaging system on a stochastic influence matrix, including the equilibrium formula, stability conditions via P-dependence, and convex-hull confinement, for scalar and vector states (when drive components are decoupled).
- A single published extension with within-agent coupling between components, with a stability iff-condition, a convergence condition and an equilibrium formula (Parsegov et al. 2017).
- Finite-time convergence of vector-valued bounded-confidence dynamics under any norm, and convergence of the anchored cases lambda in {0,1} and common-truth.
- Explicit statements, from the people who work on it, of what is unknown: heterogeneous-radius vector HK, directed state-dependent graphs, general anchored HK with distinct anchors, consensus with zero-susceptibility agents.

**Does not exist (in what I read):**
- A theorem for drives that evolve on their own (growth, satiation, oscillation) under these influence operators.
- A theorem for state-dependent or person-specific cross-drive coupling.
- Asymmetric, expressiveness-weighted bounded confidence with an anchor.
- Any fit of a multi-drive vector model to human data in this family.
- A transcription of the Bosse et al. contagion equations (not retrievable) and McClelland's control-loop equations (not retrievable).

**What the algebra should therefore adopt, and what to test before building:** adopt (anchor, susceptibility, influence matrix, coupling matrix) as the primitive quadruple; adopt the affine one-step map and the Kronecker law rho = rho(Lambda W) rho(C); do **not** adopt bounded confidence as a drive operator until a vector-valued, anchored, asymmetric version has a proof or until data demand it. A decisive cheap test: take the Parsegov model with m = 2 drives and **check by simulation** that equation (23) matches iteration for C with rho(C) > 1 and rho(Lambda W) < 1/rho(C) (the claim in Remark 2). That is a check of the paper's statement, not of psychology.

---

## 9. Unconfirmed

- French 1956: the exact equations, the claim that French's theory is multi-issue or single-issue, and whether his "resultant force" formulation maps onto W x. Only P&T's description was read. File 05's "tied to Lewin" assumptions are unverified here.
- Harary 1959: theorem text not read; P&T 2017 footnote 8 is the only statement I have of what the proof uses. Settlement belongs to D211.
- DeGroot 1974: consensus theorem is as H&K and P&T restate it; the paper itself was not read.
- Friedkin & Johnsen 1990/1999: only restated forms read; the FJ experimental protocol and effect sizes are D210.
- Festinger 1950 and Lewin 1936/51: contents from general knowledge only; no quotes.
- Bosse et al. 2015 and McClelland 2004: not read; their equations are absent from this file. DOIs resolved at Crossref; contents unverified.
- Chazelle & Wang (2017 TAC) and Hegselmann & Krause (2015 NHM) theorems are stated as P&T 2018 reports them; the original proofs and exact hypotheses (for example whether finite-time or only asymptotic, and the precise condition on lambda_i) were not checked. The ACC 2016 version of the former has doi:10.1109/ACC.2016.7525202 [Crossref]; the TAC 2017 DOI was not resolved.
- Lorenz 2007 survey (doi:10.1142/S0129183107011789 [Crossref]) is cited as the standard multidimensional-bounded-confidence survey; not read.
- Whether P&T 2017 Theorem 20's hypothesis list matches the original source (their ref [115]) was not checked.
- Parsegov et al. Theorem 2's "if and only if" is conditional on the model as stated; the proofs in the appendix were skimmed, not verified line by line.
