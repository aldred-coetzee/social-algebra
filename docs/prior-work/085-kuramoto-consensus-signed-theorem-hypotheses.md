# Prior work 085: hypotheses of the Kuramoto, Dörfler-Bullo, Altafini and Olfati-Saber theorems

Direction: D215

Date: 2026-10-29. Kind: cross-check. Question: what exactly must hold for each of four theorems that file 23 leans on (Kuramoto critical coupling, Dörfler-Bullo, Altafini, Olfati-Saber & Murray) to apply, and which of those hypotheses a social group could meet? Cross-references: 23 (collective dynamics; sections 5 and 10), 06/07 (control), 74 (FJ/DeGroot controllability), 86 and D217 (Kuramoto fitted to human data is NOT done here).

**Method and honesty note.** Texts downloaded and extracted with `pdftotext`/XML parsing, not via a summarising model; scratch copies in the session scratchpad. Provenance of each:

| Work | Status | What was read |
|---|---|---|
| Dörfler & Bullo 2011 (arXiv:1011.3878v2) | **[read]**, intro, sections 2-4 incl. Theorem 4.1 and proof of necessity; section 5 (inertia) only skimmed | enough for every claim below |
| Acebrón et al. 2005 (RMP 77:137, publisher-layout copy) | **[read]**, section II (Kuramoto's derivation, stability of incoherence, finite-size effects) and section IV.A (short-range models); sections III, V-VII (noise, extensions, applications) NOT read in full | enough for the K_c claims |
| Olfati-Saber & Murray 2004 | **[read]**, both the submitted preprint (Caltech, April 23 2003) and, at validation (2026-10-30), the **published TAC 49(9):1520-1533** from the Caltech authors repository (authors.library.caltech.edu/records/t2gnt-vd720); theorem statements checked in both. They differ on Theorem 1 (see section 3) | |
| Altafini 2013 (IEEE TAC 58:935) | **NOT READ.** Paywalled (Unpaywall: closed; Semantic Scholar: closed); the author's Linköping PDF is listed in search results but the host does not resolve from this machine; SISSA repository blocked (403/Cloudflare). Every claim about this paper is **[sa]** or is a restatement by a paper I did read, said so each time | |
| Altafini 2012, *PLoS ONE* 7(6):e38135 (open access) | **[read] in full** (manuscript XML; equations did not survive extraction, so equation numbers are cited but formulas below are reconstructed from the prose and from papers that restate them, and marked) | this is Altafini's own, open, earlier statement of the same idea, NOT the 2013 theorem paper |
| Strogatz 2000 (Physica D 143:1-20) | **[read] at validation** (2026-10-30), publisher PDF hosted on a UCSD course page; sections 4-5 and 8-9 (K_c derivation, open problems, stability of incoherence, Landau damping) and the conclusion | was "NOT READ" in the first pass |
| Proskurnikov, Matveev & Cao 2016 (arXiv:1508.05034v1) | **[read]**, introduction, sections II-IV and Theorem 1 with Example 1 | read because it restates and corrects Altafini's hypotheses |
| Valcher & Misra 2014 (*Syst. Control Lett.* 66:94-103, DOI 10.1016/j.sysconle.2014.01.006); Liu, Chen, Başar & Belabbas 2017 (*IEEE TAC* 62(12):6168-6182, DOI 10.1109/TAC.2017.2700523; read as arXiv:1512.07150v1, then titled "Exponential Convergence of the Discrete-Time Altafini Model") | **[read]** introductions (Valcher-Misra as the author's accepted manuscript, dei.unipd.it/~meme); Liu et al. also section 2 (Assumption 1, Proposition 1) | restate Altafini 2013's result |

Crossref-verified DOIs: Dörfler-Bullo 10.1137/10081530X (SIADS 10:1070-1099, 2011); Acebrón 10.1103/RevModPhys.77.137; Olfati-Saber & Murray 10.1109/TAC.2004.834113; Strogatz 10.1016/S0167-2789(00)00094-4; Altafini 2013 10.1109/TAC.2012.2224251; Altafini 2012 10.1371/journal.pone.0038135; Strogatz & Mirollo 10.1007/BF01029202; Strogatz, Mirollo & Matthews 10.1103/PhysRevLett.68.2730; Proskurnikov et al. 10.1109/TAC.2015.2471655 (TAC 61(6):1524-1536, 2016); Valcher & Misra 10.1016/j.sysconle.2014.01.006; Liu et al. 10.1109/TAC.2017.2700523. Added at validation: Dietert, Fernandez & Gérard-Varet 10.1002/cpa.21741 (CPAM 71:953-993, 2018); Dörfler, Chertkov & Bullo 10.1073/pnas.1212134110 (PNAS 110:2005-2010, 2013).

**Summary of the cross-check.**
1. Kuramoto's `K_c = 2/(π g(0))` is the onset of *partial* synchrony in the N → ∞, all-to-all, symmetric-unimodal-g limit. It is **not** the threshold Dörfler-Bullo prove. D-B's `K > ω_max - ω_min` is the threshold for *full frequency locking with phase cohesiveness*, worst case over all distributions on a bounded support, any finite n, all-to-all. File 23 lists them together as "Kuramoto K_c"; they are different quantities and for a Lorentzian g they differ in kind (onset finite, full locking never).
2. Olfati-Saber & Murray: **Theorem 1 of the 2003 preprint ("strongly connected iff rank(L) = n-1") is false as written** (a two-node one-way edge has rank n-1 and is not strongly connected); **the published 2004 paper already states only the true forward direction** ("If G is strongly connected, then rank(L) = n-1", with the "iff" kept only for undirected graphs, Remark 4), so cite the published version and the error disappears. The repair file 23 does need: the "switching" theorem is not about general switching: every graph in the switching family must be *strongly connected AND balanced* at all times.
3. Altafini's "unbalanced → everything goes to zero" is right only for strongly connected graphs. Proskurnikov-Matveev-Cao give a three-agent counterexample on a non-strongly-connected graph, and report that Altafini's time-varying result silently needed weight-balance. I could not confirm the latter against Altafini's text.
4. None of the four is an empirical result. Not one of the papers read fits a parameter to human data.

---

## 1. Kuramoto's critical coupling (Kuramoto 1975/1984, via Acebrón 2005 and Dörfler-Bullo 2011)

**Citations.** Acebrón, J. A., Bonilla, L. L., Pérez Vicente, C. J., Ritort, F., Spigler, R. (2005). The Kuramoto model: a simple paradigm for synchronization phenomena. *Rev. Mod. Phys.* 77, 137-185. DOI 10.1103/RevModPhys.77.137. Kuramoto's own 1975 and 1984 texts were **not read**; everything about them is as reported by Acebrón [read] and Dörfler-Bullo [read].

**Their vocabulary.** Natural frequency, coupling, order parameter, incoherence, partial synchronisation, phase locking, mean-field coupling.

**Model [read, Acebrón eq. 1].** `dθ_i/dt = ω_i + Σ_j K_ij sin(θ_j - θ_i)`, i = 1..N, with ω_i drawn from density g(ω). The solved case is mean-field `K_ij = K/N`. Order parameter `r e^{iψ} = (1/N) Σ_j e^{iθ_j}`; the dynamics rewrites as `dθ_i/dt = ω_i + K r sin(ψ - θ_i)` [read]. Dörfler-Bullo write the same model with sign convention `θ̇_i = ω_i - (K/n) Σ_j sin(θ_i - θ_j)` [read, their eq. 1.1].

**Derivation and result [read, Acebrón section II.A].** In the limit N = ∞ with g(ω) = g(-ω) (a rotating frame removes the mean), partial synchronisation requires the self-consistency condition `1 = K ∫_{-π/2}^{π/2} cos²θ g(K r sin θ) dθ` (their eq. 12). Setting r = 0 gives
`K_c = 2 / (π g(0))`  (their statement, "first found by Kuramoto (1975)").
For the Lorentzian `g(ω) = (γ/π)/(γ² + ω²)`: `K_c = 2γ` and `r = sqrt(1 - K_c/K)` exactly for K > K_c. For general g: `r ~ sqrt( -16 (K - K_c) / (π K_c⁴ g''(0)) )` as K → K_c [read, eq. 14].

**Hypotheses that must hold, and what the sources say about each.**

| Hypothesis | Status in the sources |
|---|---|
| Phase (circular) scalar state, one oscillator per person | by definition |
| Coupling is sinusoidal, symmetric, all-to-all with equal weight K/N | for non-mean-field coupling Acebrón says the order parameter "is less useful" and "short-range couplings present formidable difficulties", "present knowledge … still quite modest" [read] |
| N = ∞ | finite N: order-parameter fluctuations scale as N^(-1/2); Daido found rms fluctuation ∝ [(K_c - K) N]^(-1/2) below K_c and (K - K_c)^(-1/8) N^(-1/2) above [read, as reported]. Balmforth & Sassi: sampling a finite frequency set can produce time-periodic synchronisation even for unimodal g, effects absent at N = ∞ [read, as reported] |
| g symmetric, unimodal (even, non-increasing for ω > 0) for the *stability* statement | with g''(0) > 0 the bifurcation is subcritical (first-order) rather than supercritical, per eq. 14's sign condition [read]; for bimodal g Acebrón devotes a separate bifurcation analysis |
| Noise-free, no delay, no inertia | noise, delay and inertia each change K_c (e.g. with white noise of strength D, `K_c = 2D + 2γ` for Lorentzian g; with small inertia m the critical coupling of their eq. 112 "increases with m"; "increasing any of the quantities m, D, ε (inertia, noise, frequency spread) makes it more difficult to synchronize") [read in Acebrón sections III and V.D at validation; the underlying papers, e.g. Acebrón et al. 2000 for inertia, not read] |

**Stability, as reported by Acebrón [read] and Strogatz 2000 [read]; the 1991/1992 primary papers not read.** For unimodal g, incoherence is *neutrally* stable (spectrum on the imaginary axis) for K < K_c, not asymptotically stable, though the linearised order parameter decays by a Landau-damping-like mechanism (Strogatz, Mirollo & Matthews 1992); a positive eigenvalue appears for K > K_c. Strogatz 2000 [read]: "the incoherent state of the Kuramoto model can never be linearly stable — it is either unstable or neutrally stable", and the linear stability of the partially synchronised branch "is still unsolved, 25 years after Kuramoto first posed it". Acebrón (2005): "a rigorous proof of its stability is still missing". **Later proved, at least locally**: Dietert, Fernandez & Gérard-Varet (2018, CPAM 71:953-993) prove local asymptotic stability of partially locked states (weak topology, analytic frequency marginals) by Landau damping [sa: arXiv abstract only, not read].

**What changes with n.** (a) The theorem is an N → ∞ statement; at finite N the sharp threshold becomes a smeared crossover with r ~ O(N^-1/2) noise floor [read]. (b) On a **lattice**, Strogatz & Mirollo (1988a, b), as reported by Acebrón: "no phase locking can occur at any finite dimension", so mean-field `K_c` does not transfer to a group with only local ties; in one dimension with Gaussian ω_i the probability of phase locking vanishes as N → ∞ unless K grows like √N [read, as reported]. For a social group with bounded-degree ties the mean-field threshold is therefore the wrong object as N grows.

**What changes with composition.** g(0) is the density of natural frequencies at the mean: a more homogeneous group (narrow g, large g(0)) has *lower* K_c. Bimodal g (two sub-populations with different rhythms) breaks the formula and the transition type [read]. Kuramoto gives no "definition" dependence: who counts as an oscillator is set by the modeller.

**Scale and consent.** Crowd (the applause example in Acebrón's introduction is described qualitatively, no data [read]). The theorem concerns no intervention.

**Empirical standing.** The sources read contain no fit of K to human data; D217 owns that question. Acebrón's applications sections (neural networks, Josephson junctions, lasers, chemical oscillators) were not read, so effect sizes and agreement with experiment in physical systems are **not** established here.

**Operand/operator translation.** Operand: a phase θ_i plus an intrinsic frequency ω_i. Operator: pairwise sinusoidal coupling `K sin(θ_j - θ_i)`. Derived quantity: the mean-field order parameter r. An algebra could use the form `ω_i + K r sin(ψ - θ_i)` as the group-to-member "downward" operator, but only for phase variables.

---

## 2. Dörfler & Bullo (2011): explicit critical coupling for finite n

**Citation.** Dörfler, F., Bullo, F. (2011). On the critical coupling for Kuramoto oscillators. *SIAM J. Appl. Dyn. Syst.* 10(3), 1070-1099. DOI 10.1137/10081530X. Read: arXiv:1011.3878v2 (5 May 2011).

**Their vocabulary.** Phase cohesiveness, phase synchronisation, frequency synchronisation, exponential synchronisation, arc `Δ(γ)`.

**Definitions [read].** `Δ(γ)` = angle arrays contained in an arc of length γ; phase cohesive if `θ(t) ∈ Δ̄(γ)` for all t; exponential frequency synchronisation if all `θ̇_i` converge exponentially to a common value; exponential synchronisation = phase cohesive + frequency synchronised. Lemma 2.1: if θ ∈ Δ̄(γ) then `r(θ) ∈ [cos(γ/2), 1]`.

**Theorem 4.1 [read, quoted].** For `θ̇_i = ω_i - (K/n) Σ_j sin(θ_i - θ_j)` the following are equivalent:
(i) `K > K_critical := ω_max - ω_min`;
(ii) there is `γ_max ∈ (π/2, π]` such that the model synchronises exponentially "for all possible distributions of the natural frequencies supported on [ω_min, ω_max] and for all initial phases θ(0) ∈ Δ(γ_max)";
(iii) there is `γ_min ∈ [0, π/2)` such that the model has a locally exponentially stable synchronised trajectory in `Δ̄(γ_min)` "for all possible distributions … supported on [ω_min, ω_max]".
Then `sin γ_min = sin γ_max = K_critical / K`, and: (1) `Δ̄(γ)` is positively invariant for γ in `[γ_min, γ_max]`; (2) `1 ≥ r_∞ ≥ cos(γ_min/2) = sqrt( (1 + sqrt(1 - (K_critical/K)²)) / 2 )`; (3) the sync frequency is the mean `ω_avg`, rate no worse than `λ_fs = K cos γ` given cohesiveness in `Δ̄(γ)`, γ < π/2; (4) for identical ω_i = s, phases synchronise at rate no worse than `K sinc(γ)`.

**Hypotheses, stated plainly.**
- Complete graph with equal weights K/n (eq. 1.1). Not a network theorem. (The same authors' other work on general graphs is not read here.)
- First-order oscillators, sinusoidal coupling, no noise.
- ω_i supported on a **compact** interval. D-B note [read, citing Verwoerd & Mason] that "K_critical is not finite for unbounded natural frequencies", so for a Gaussian or Lorentzian population no finite K gives full locking.
- **The "necessary" half is a worst-case statement over all distributions on the interval**, proved using a bipolar (two-point) distribution. For a specific g the bound is "only sufficient and possibly a factor 2 larger than the necessary bound" `K > n(ω_max - ω_min)/(2(n-1))` [read, eq. 3.3 and section 4.1]. This confirms file 23's caveat.
- Initial phases in `Δ(γ_max)`, an arc less than a half circle for γ_min but up to nearly a full circle for γ_max.

**Relation to Kuramoto.** D-B are explicit that Kuramoto's `2/(π g(0))` is the *onset* from incoherence, whereas their bound concerns the "ultimate stage" (full locking). For uniform g on [-1, 1], numerical averages over 1000 draws for n up to 300 [read, Fig. 4.1] converge to the exact locking threshold `4/π ≈ 1.27`, which equals `2/(π·0.5)`, the Kuramoto onset; the D-B sufficient bound converges to 2, the necessary bound to 1. So for a *bounded flat* population all three notions are within a factor 2; for a population with tails they are not comparable at all.

**What changes with n.** The D-B bound is independent of n. Earlier Lyapunov bounds scaled with n (their section 3.2: "none of these bounds scales independently of n"). The necessary bound `n(ω_max - ω_min)/(2(n-1))` tends from 1×width at n = 2 (exact: bound is tight, Example 2.2) to 0.5×width. Because `ω_max - ω_min` is a sample range, it **grows with n** for any distribution with unbounded support: in a larger sampled group, full locking is harder. The exact (implicit, Verwoerd-Mason / Mirollo-Strogatz / Aeyels-Rogge) threshold sits near the sufficient bound for small n and near the necessary bound for large n [read, section 4.1].

**What changes with composition.** Everything enters through `ω_max - ω_min`, so one outlier sets the threshold: heterogeneity is measured by range, not variance.

**Scale / consent.** Group cohesion, as a mathematical property of a model. No human data; no intervention.

**Empirical standing.** None; a theorem. The paper's applications are power networks, Josephson junctions, deep brain stimulation [read, introduction].

**Operand/operator translation.** Operand: phase with a frequency range. Operator: global mean-field coupling. The useful new object for an algebra is the *performance* triple (γ, r_∞, λ), which gives a guaranteed cohesion level as a function of the ratio `K_critical/K`: a rare example of an explicit quantitative guarantee, but only on a complete graph of phases.

---

## 3. Olfati-Saber & Murray (2004): consensus with switching topology and delays

**Citation.** Olfati-Saber, R., Murray, R. M. (2004). Consensus problems in networks of agents with switching topology and time-delays. *IEEE Trans. Autom. Control* 49(9), 1520-1533. DOI 10.1109/TAC.2004.834113. **Read: the preprint** at `cds.caltech.edu/~murray/preprints/om04-tac.pdf` (header: "Submitted", April 23 2003) **and, at validation, the published version** (Caltech authors repository, `OLFieeetac04.pdf`). Theorem numbers 1-10 are the same in both; differences noted below.

**Their vocabulary.** Consensus, decision value, balanced digraph, disagreement function, mirror graph, algebraic connectivity, Fiedler eigenvalue.

**Setting [read].** `G = (V, E, A)` weighted digraph, `a_ij ≥ 0`, Laplacian `L = Δ - A` with `Δ_ii = deg_out(v_i) = Σ_j a_ij` (eq. 12). Protocol (A1): `u_i = Σ_{j∈N_i} a_ij (x_j - x_i)`, so `ẋ = -L x` (eq. 6). Average consensus: all `x_i → Ave(x(0))`.

**Statements [read], with hypotheses.**
- **Theorem 1 (preprint)**: "G is strongly connected if and only if rank(L) = n - 1." **This is false as stated.** Counterexample (my own, not from a source): n = 2, `a_12 = 1`, `a_21 = 0`; `L = [[1, -1], [0, 0]]` has rank 1 = n-1 but there is no path from node 2 to node 1. Strong connectivity implies rank n-1, not conversely (rank n-1 holds iff a rooted spanning tree exists). The paper's later proofs use only the forward direction (Corollary 1: strongly connected ⇒ simple zero eigenvalue ⇒ consensus), which is true. File 23's wording ("strongly connected balanced digraphs") already uses the correct sufficient condition. **The published version corrected it** [read, published p. 1524]: "If G is strongly connected, then rank(L) = n − 1", and Remark 4 keeps the "iff" only for undirected graphs (connected iff rank n − 1), which is true.
- **Corollary 1**: strongly connected ⇒ (A1) solves *a* consensus problem (agreement on some value).
- **Corollary 2**: if `γ` is a nonnegative left null vector of L, the decision value is `Σ γ_i x_i(0) / Σ γ_i`, a weighted average with the *influence weights set by the graph*, in the convex hull of initial values.
- **Definition 1**: node balanced if `deg_in = deg_out`; graph balanced if all nodes are. "Any undirected graph is balanced."
- **Theorem 4 / 5 / 6**: for a **strongly connected** digraph, (A1) solves *average* consensus iff `G` is balanced iff `1ᵀ L = 0` iff `Σ u_i = 0 ∀x`. Theorem 6 (equivalences) does not need connectivity.
- **Theorem 8**: (preprint wording; the published statement says only "strongly connected digraph" but sits in section VIII, which is about balanced graphs, and its proof uses balance through the mirror-graph theorem 7) balanced and strongly connected ⇒ disagreement `δ` obeys `||δ(t)|| ≤ ||δ(0)|| exp(-κ t)` with `κ = λ_2(Ĝ)`, the Fiedler eigenvalue of the **mirror graph** (the undirected graph with Laplacian `(L + Lᵀ)/2`); `V(δ) = ½||δ||²` is a Lyapunov function. The authors comment: "a network with dense interconnections solves an agreement problem faster than a connected but sparse network."
- **Theorem 9 (switching)**: the family is `Γ_n = {G : G strongly connected and balanced}` (preprint eq. 31; same wording in the published version [read]); "for any arbitrary switching signal s(·)" among members of `Γ_n`, the state converges to `Ave(x(0))`, with rate at least `κ* = min_{G∈Γ_n} λ_2(Ĝ)`. **The theorem does not cover switching among graphs that are individually disconnected** (that is the Jadbabaie-Lin-Morse / joint-connectivity case, which the authors contrast with theirs in section 3).
- **Theorem 10 (delay)**: equal delay τ on every link, `G` **undirected and connected**: (A2) `u_i(t) = Σ a_ij [x_j(t-τ) - x_i(t-τ)]` solves average consensus iff `τ ∈ (0, τ*)` with `τ* = π / (2 λ_max(L))`; at `τ = τ*` there is a stable oscillation of frequency `λ_max`. Using `λ_max ≤ 2 d_max` (Geršgorin) a sufficient condition is `τ ≤ π / (4 d_max)`. File 23's version is correct for the equal-delay undirected case; it does **not** extend to unequal delays or directed graphs in this paper.

**What changes with n.** `λ_2` and `λ_max` depend on topology, not on n directly. For a given degree sequence, `τ*` shrinks as the *largest degree* grows: "networks with nodes that have relatively high out-degrees cannot tolerate" long delays [read]. In a complete graph on n nodes with unit weights `λ_2 = λ_max = n`, so convergence speeds up with n while `τ*` shrinks like 1/n. Sparse cycles are slow ("a relatively slow way").

**What changes with composition/definition.** Balance (`deg_in = deg_out` per node) is a *composition* condition: every member must be heard as much as they speak. A hub with high in-weight and low out-weight (a leader who is listened to but listens little) breaks it, and then the decision value is the Corollary-2 weighted average, not the mean.

**Scale/consent.** Group agreement/decision (engineering: vehicles, UAVs, sensors [read]). The "intervention" is protocol design for agents that obey it by construction. Applied to people this means editing who attends to whom, which is a manipulation of the graph, not a consent-based intervention; nothing in the paper treats humans.

**Empirical standing.** The paper has simulations only. None involve social data.

**Operand/operator translation.** Operand: a scalar `x_i`. Operator: the Laplacian `-L`, with the balanced/unbalanced distinction deciding whether the group's mean is conserved. The conserved-mean fact (`Σ ẋ_i = 0` iff balanced) is the only part with a clean algebraic content for the algebra: it says "interaction only redistributes, never creates, the quantity", a conservation law.

---

## 4. Altafini: consensus with antagonistic interactions

**Citations.** (a) Altafini, C. (2013). Consensus problems on networks with antagonistic interactions. *IEEE TAC* 58(4), 935-946. DOI 10.1109/TAC.2012.2224251. **Not read; [sa].** (b) Altafini, C. (2012). Dynamics of opinion forming in structurally balanced social networks. *PLoS ONE* 7(6), e38135. DOI 10.1371/journal.pone.0038135. **[read] in full.** (c) Proskurnikov, A. V., Matveev, A. S., Cao, M. (2016). Opinion dynamics in social networks with hostile camps: consensus vs. polarization. *IEEE TAC* 61, 1524-1536. DOI 10.1109/TAC.2015.2471655; read as arXiv:1508.05034v1 (a restatement of (a)'s model and results, with corrections).

**The model of (a), as restated in (c) [read in (c); not checked against (a)].** `ẋ = -L[A] x` with signed Laplacian `L_jk = -a_jk (j≠k)`, `L_jj = Σ_m |a_jm|`, i.e. `ẋ_j = Σ_k |a_jk| (sgn(a_jk) x_k - x_j)`: an agent is pulled toward a friend's opinion and toward the *negative* of an enemy's. Assumptions in (c)'s account of (a): no self-loops, **digon sign-symmetry** (`a_jk a_kj ≥ 0`, i.e. two people never perceive opposite signs of one tie).

**Definitions [read in (c)].** Structurally balanced (SB): nodes split into two hostile camps, `a_jk ≥ 0` within camps and `≤ 0` across. For a digon-symmetric strongly connected graph, SB iff every directed cycle is positive. Modulus consensus: `lim |x_i(t)| = x*` for all i.

**The theorem and what is actually required.**
- Reported by (c) [read] as Altafini's static result: for a **strongly connected** graph the protocol is *stabilising* (`−L` Hurwitz, all states → 0) unless the graph is SB; if SB, bipartite consensus (two opposite values; consensus if one camp is empty) [(c), citing Altafini; I have not seen Altafini's proof]. For SC graphs, `L` has no zero eigenvalue iff the graph is *not* SB (attributed to Altafini's Lemma 2).
- Valcher & Misra (2014), introduction [read, accepted manuscript]: "if the signed, weighted and connected communication graph … is structurally balanced, then the agents reach bipartite consensus … if … not structurally balanced, the only agreement … is the trivial one, where all the agents' states converge to zero." Note "connected" there; the directed/undirected distinction is not stated in that summary.
- For the undirected balanced case the limit is `x_i(∞) = σ_i (1/n) Σ_j σ_j x_j(0)` with `σ_i = ±1` the camp indicator (file 23's formula, the gauge transform `x → diag(σ) x`). I could not verify this against Altafini; it is consistent with Lemma 1 of (c), which gives `lim x = ρ vᵀ x(0)` with `ρ_i = ±1`, v a left null vector. **[sa]** for the exact formula.

**Corrections found in the read material [(c), Section I and Theorem 1].**
1. **Strong connectivity is needed for "unbalanced ⇒ zero".** (c) Theorem 1 [read]: for constant A the protocol is stabilising iff the graph "is neither SB itself nor contains an ISB (in-isolated structurally balanced) subgraph"; bipartite consensus iff the graph is SB and quasi-strongly connected (has a root). Example 1 [read]: three agents, `a_12 = a_21 = -1` (agents 1, 2 mutually hostile), `a_31 a_32 > 0` (agent 3 follows both); not SB, but agents 1, 2 form an SB subgraph that ignores agent 3, so `x_1 = -x_2 = ξ` persists and there is **no** modulus consensus. Equilibria `(ξ, -ξ, ρξ)` with `ρ = (a_31 - a_32)/(|a_31| + |a_32|)`. So an unbalanced group does *not* always decay to zero if some sub-clique is isolated from outside influence.
2. **Altafini's time-varying result is restricted.** (c): "In [28] this problem was considered only for the very special case where the graph is constantly strongly connected, has time-invariant signs of the arcs and also weight-balanced (this assumption was not explicitly mentioned, but in fact was used in the proof which appeals to [44, Theorem 9])." That is (c)'s reading of Altafini 2013; I could not check it.
3. Liu, Chen, Başar & Belabbas, introduction [read]: for *repeatedly jointly strongly connected* sequences of signed digraphs with positive self-arcs, the discrete-time model reaches **modulus consensus** regardless of sign structure (Proposition 1 there, citing Theorem 2.1 of Meng et al.); "different types of structural balance correspond to different clusterings of opinions".

**Altafini 2012 (PLoS ONE) [read], what it assumes and claims.**
- Opinions `x ∈ ℝⁿ` obey `ẋ = f(x)` with `x = 0` a fixed point ("no opinion is formed unless at least one individual already has an opinion"). Influence of j on i is the partial derivative `∂f_i/∂x_j`; **sign stability**: its sign is the same everywhere in opinion space ("friends are friends in the good and in the bad moments"); sign symmetry (no digon with opposite signs). Own-opinion term is a decay (`opinions are gradually forgotten`), which keeps ODEs bounded.
- Result: such a system is **monotone** (order-preserving for an orthant order) iff every semicycle of the signed digraph is positive, i.e. iff the graph is structurally balanced (Kamke condition); with an irreducible (strongly connected) sociomatrix it is *strongly* monotone: a single seeded opinion eventually pulls every member to a side, "no individual can remain neutral". The balanced network is "dynamically identical, up to a gauge transformation" to the all-friends network.
- **What is assumed, not tested.** "The key assumption … that the opinions of friends exercise a positive influence and those of enemies a negative one, is realistic in this context"; fixed topology and fixed signs; the application is two-party assemblies, with the US Congress debt-ceiling deadlock of Summer 2011 cited as an illustration. No data are fitted. Simulations use a functional form in the supplementary text (not read).
- **Heider versus Cartwright-Harary [read]**: balance of all triads (length-3 cycles) is weaker than balance of all cycles on a graph that is not complete; the supplement gives a graph where all 3-cycles are positive and the network is still unbalanced. Altafini uses the Cartwright-Harary (all semicycles) condition. This is the relevant fact for D207.
- Non-balanced example: simulation shows sustained oscillations, "unfeasible for a monotone system" (Fig. S, caption) [read]. This is a simulation of an example, not a theorem.

**Hypotheses for the algebra, collected.** Fixed signs; fixed topology (or, in (c), uniformly strongly connected time-varying graphs); sign-symmetric ties; scalar real opinion; for the clean "balanced iff bipartite consensus, else zero" dichotomy, a strongly connected graph. Real social ties flip sign, are not symmetric in sign, and many groups contain mutually hostile pairs that are shielded from the rest, which is exactly the ISB subgraph case.

**What changes with n.** Nothing in the statements depends on n except through connectivity; deciding whether a signed graph is balanced is computable in O(edges) by two-colouring, so scale is not an obstacle. The larger the group, the less likely a *global* split into exactly two camps is exact: balance is a property that fails on the first inconsistent triangle, and (a)/(b) say nothing about approximate balance.

**What changes with composition.** The number of camps is fixed at two; three or more mutually hostile factions are, by definition, unbalanced, and the theorem then says the strongly connected group's opinions go to zero (or, with ISB subgraphs, does not give modulus consensus).

**Scale/consent.** Group decision/opinion polarisation (membership of the camp is given, not predicted). An "intervention" would be flipping a node's signs (the "gauge transformation", described in (b) as a person changing party, which causes a "rapid transient in which the individuals adopt the views of their new friends"); in practice this is persuasion or defection, not a lever one can pull with consent.

**Empirical standing.** (c) states "We are currently working with sociologists to test the theoretical results … using data from human social groups"; no such test is reported in that paper. (b) is qualitative. I found no validation in anything read.

**Operand/operator translation.** Operand: scalar opinion `x_i` with a camp label `σ_i`. Operator: the signed Laplacian; the camp structure is a two-colouring of the signed graph, and the gauge transformation `diag(σ)` is an automorphism of the dynamics. This is the strongest purely algebraic content in the four: **balance means the signed dynamics is conjugate to the unsigned dynamics**. It does not tell us how signs arise.

---

## 5. Strogatz (2000), "From Kuramoto to Crawford"

**Citation.** Strogatz, S. H. (2000). From Kuramoto to Crawford: exploring the onset of synchronization in populations of coupled oscillators. *Physica D* 143(1-4), 1-20. DOI 10.1016/S0167-2789(00)00094-4.

**[read] at validation (2026-10-30)**, from a copy of the publisher PDF on a UCSD course page (the first pass could not fetch it). Confirms, in Strogatz's own derivation (section 4): the self-consistency equation `1 = K ∫ cos²θ g(Kr sin θ) dθ`, `K_c = 2/(π g(0))` as "Kuramoto's exact formula for the critical coupling at the onset", supercritical iff `g''(0) < 0`, and `r = sqrt(1 - K_c/K)` for the Lorentzian. Section 8: incoherence is never linearly stable, only neutrally stable for K < K_c; section 5 lists finite-N fluctuations and the stability of the partially locked branch as open (2000). Nothing in this file depended on it; it now corroborates section 1 independently of Acebrón.

---

## What exists vs what does not

**Exists (read):** an exact onset threshold for mean-field Kuramoto with symmetric unimodal g at N = ∞ (Kuramoto, as reported); an exact, n-independent, worst-case sufficient-and-necessary locking threshold on a complete graph with bounded frequencies (D-B); a clean conservation-of-average theorem for balanced digraphs and a rate bound by the mirror-graph Fiedler value (Olfati-Saber & Murray; preprint and published version); a theory in which structural balance makes signed opinion dynamics conjugate to unsigned dynamics (Altafini 2012, Proskurnikov et al. 2016).

**Does not exist (in what was read):** any Kuramoto K_c, any consensus rate, or any balance-implies-polarisation law fitted to human data; any version of D-B that is noisy or uses person-level heterogeneity beyond the range (a non-complete-graph version *does* exist: Dörfler, Chertkov & Bullo 2013, PNAS 110:2005-2010, a sync condition for general graphs [sa: not read; found by search at validation]); any treatment of group-size dependence for social groups (the N-dependence results concern lattices or random samples of frequencies); any theorem for ≥ 3 factions in the papers read (search at validation found the combinatorial notion, Davis's *weak balance*, which allows more than two factions [read, as reported in Proskurnikov & Tempo 2018, arXiv:1801.06719], and later Laplacian clustering papers, e.g. Thota, Tripathy & Pal, arXiv:2408.07559 [abstract only]; no dynamical k-faction theorem was confirmed); any account of where a sign or a coupling weight comes from.

## Unconfirmed

- Altafini 2013 (the theorem paper) was not read; re-tried at validation: the Linköping copy (`users.isy.liu.se/.../bipartite_consensus.pdf`) does not resolve from this machine (DNS failure for curl and WebFetch), Unpaywall reports no OA copy, no arXiv version. Every statement about its hypotheses is via Valcher-Misra, Liu et al. or Proskurnikov et al. The claim that its time-varying proof silently used weight-balance is Proskurnikov et al.'s, not verified. The exact limit formula `x_i(∞) = σ_i (1/n) Σ σ_j x_j(0)` stays [sa] and must not feed an equation.
- Kuramoto 1975/1984, Strogatz-Mirollo 1988a,b and 1991, Strogatz-Mirollo-Matthews 1992, Daido, Balmforth-Sassi: all via Acebrón (and, for some, Strogatz 2000) only.
- Dietert, Fernandez & Gérard-Varet 2018 (stability of partially locked states) and Dörfler, Chertkov & Bullo 2013 (non-complete graphs): existence and authorship confirmed by Crossref; content from abstracts only.
- Acebrón sections V-VII other than V.D (inertia) and the applications were not read; nothing here rests on them.

---

## Does it reduce to a drive basis?

**Partly, and less than file 23 suggested.**

*Reduces to a drive of a person:* (i) Kuramoto's `ω_i` is a person's own intrinsic rate, if one reads a cyclic urge (an ultradian craving, a speaking rhythm) as a rotating phase: this is the "drive" in the model, and in Dörfler-Bullo its dispersion `ω_max - ω_min` is the quantity the whole cohesion guarantee is expressed in. (ii) Altafini 2012's own-opinion term (opinions "gradually forgotten") is a restoring drive toward 0 [read]. (iii) The sign `sgn(a_ij)`, attraction toward or repulsion from j's state, could be read as a person-level affiliation versus rivalry drive directed at j, but **no source derives it that way**; it is an input.

*Does not reduce:* (a) the coupling constant K and the weights `a_ij` are properties of pairs or of the graph, not of either person; (b) the order parameter r, the Fiedler value λ_2, the balance condition and the weighted decision value `Σ γ_i x_i / Σ γ_i` are group-level quantities that no individual drive determines (balance is a global combinatorial property of all cycles); (c) the state spaces are mismatched with drive variables: a Kuramoto state is a circular phase with no bounded "level", a consensus state is an unanchored scalar with no setpoint (balanced Laplacian dynamics conserves the mean, so there is no restoring term at all), while hunger-type drives are bounded levels with set points; (d) the conservation law (`1ᵀ L = 0`) and the gauge symmetry of balance are structural facts of the *interaction graph*, which a drive basis would have to *produce*, not assume. Everything here takes the interaction structure as given, so these theorems cannot test "drives as primitives": they are conditional on a graph and a coupling that drives are supposed to explain.

## What does it predict or control, and how well?

**It predicts nothing about people that has been checked.** Each theorem predicts a mathematical outcome under hypotheses, and no paper read reports out-of-sample human data or an effect size.

- **Kuramoto / Dörfler-Bullo:** predicts the existence and cohesion level of synchrony in a model population: `r_∞ ≥ sqrt((1 + sqrt(1 - (K_critical/K)²))/2)` (D-B, n-independent, worst case), onset at `2/(π g(0))` (Kuramoto, N = ∞). Controls: raising K or narrowing the frequency range. Evidence: numerical sampling in D-B only (uniform g, n ≤ 300); the review's physical applications not read. For a human group: none read here (D217).
- **Olfati-Saber & Murray:** predicts which value a balanced strongly connected group converges to (the mean), how fast (`κ = λ_2` of the mirror graph) and the largest tolerable equal delay (`π/(2 λ_max)`), by design of the protocol. Evidence: simulations of engineered agents only. As a control of people it is graph editing, i.e. manipulation of who listens to whom.
- **Altafini:** predicts polarisation into two opposite camps iff balanced and connected (no decay to zero), else decay or, in Proskurnikov et al.'s counterexample class, persistent isolated polarised pairs. Evidence: qualitative simulations and a political illustration (Altafini 2012); Proskurnikov et al. report an unfinished attempt with sociologists. **Failures known on paper, not in data:** the dichotomy breaks without strong connectivity (Example 1); the model cannot represent three or more factions, sign changes over time, or asymmetric-sign ties; the 2013 time-varying extension is questioned by a later paper.

For the algebra: these four results are useful as *conditional lemmas* (the form of the guarantees, the conservation law, the gauge symmetry) and unusable as *calibrated predictions*. They are scale-wise crowd/group-level (applause, committee polarisation) and none addresses membership.

## Validation log (2026-10-30)

- ✓ Dörfler & Bullo 2011, SIADS 10(3):1070-1099, DOI resolves. Re-read arXiv:1011.3878v2: Theorem 4.1 (i)-(iii) and statements 1-4, eq. 3.3, "not finite for unbounded natural frequencies" (citing Verwoerd & Mason), "only sufficient and possibly a factor 2 larger", Fig. 4.1 (n ≤ 300, 1000 runs, exact bound → 4/π), "none of these bounds scales independently of n": all as stated.
- ✓ Acebrón et al. 2005, RMP 77:137-185, DOI resolves. Re-read publisher-layout copy: eq. 12, K_c = 2/(πg(0)) "first found by Kuramoto (1975)", Lorentzian r, eq. 14, sub/supercritical sign of g''(0), Daido scalings, Balmforth-Sassi, Strogatz-Mirollo lattice result and K ≈ √N, "less useful", "formidable difficulties", "quite modest", "rigorous proof … still missing", noise K_c = 2D + 2γ, inertia K_c "increases with m": all as stated (noise and inertia now read directly, not by grep).
- ✎ Olfati-Saber & Murray 2004, TAC 49(9):1520-1533, DOI resolves. Preprint re-read (Theorems 1, 4, 5, 8, 9, 10, Corollaries 1-2, Geršgorin bound, quotes) and found accurate. **Published version obtained and read** (Caltech authors repository): its Theorem 1 states only the forward direction, so the "iff" error is the preprint's alone; summary item 2 and section 3 corrected. Published Theorem 8 omits the word "balanced" from its statement (balance is the section's standing context); noted. Theorem 9's family and Theorem 10 identical.
- ? Altafini 2013, TAC 58(4):935-946, DOI resolves; text still unobtainable (host does not resolve, no OA). Stays [sa].
- ✓ Altafini 2012, PLoS ONE 7(6):e38135, DOI resolves. Re-read manuscript XML: "good and in the bad moments", sign symmetry, "gradually forgotten", "no individual can remain neutral", gauge transformation, Kamke condition, Cartwright-Harary vs Heider with Fig. S4, debt-ceiling illustration, "unfeasible for a monotone system", "rapid transient": all as stated.
- ✓ Proskurnikov, Matveev & Cao 2016, TAC 61(6):1524-1536, DOI resolves. Re-read arXiv:1508.05034v1: Theorem 1, Example 1 with ρ = (a31 − a32)/(|a31| + |a32|), digon sign-symmetry, Lemma 2 attribution to [28, Lemma 2], the "not explicitly mentioned" quote with [28] = Altafini 2013 and [44] = Olfati-Saber & Murray 2004, "working with sociologists": all as stated.
- ✎ Valcher & Misra: full citation added (Syst. Control Lett. 66:94-103, 2014, DOI resolves); quote checked verbatim in the accepted manuscript.
- ✎ Liu, Chen, Başar & Belabbas: full citation added (TAC 62(12):6168-6182, 2017, DOI resolves; arXiv v1 had a narrower title); Proposition 1 (citing Meng et al. Theorem 2.1), Assumption 1 (a_ii > 0) and the "different clusterings" quote checked — Proposition 1 is in section 2, not the introduction.
- ✎ Strogatz 2000, Physica D 143:1-20, DOI resolves. **Now read** (first pass: 403); section 5 rewritten; it independently confirms the K_c derivation and the open stability problem as of 2000.
- ✓ Strogatz & Mirollo 1991 (J. Stat. Phys. 63:613-635) and Strogatz, Mirollo & Matthews 1992 (PRL 68:2730-2733): DOIs resolve, authors match; content still via reviews only.
- ✎ "Whether the partially synchronised branch was proved stable after 2005": tested by search — yes, locally (Dietert, Fernandez & Gérard-Varet 2018, DOI resolves; abstract only, [sa]). Added to section 1.
- ✎ "Does not exist" list: tested by search. D-B on non-complete graphs **does** exist (Dörfler, Chertkov & Bullo 2013, PNAS, DOI resolves; not read) — corrected. ≥ 3 factions: weak balance exists as a graph notion; no dynamical k-faction theorem confirmed — qualified.
- No fabrications found; nothing deleted.

Sources opened this pass: 10 primary texts (Dörfler-Bullo arXiv; Acebrón RMP copy; Olfati-Saber-Murray preprint and published; Altafini 2012; Proskurnikov et al. arXiv; Liu et al. arXiv; Valcher-Misra manuscript; Strogatz 2000; Proskurnikov-Tempo tutorial for weak balance), plus 14 Crossref DOI records and arXiv metadata for 4 papers.

**Verdict.** The file is accurate and unusually careful: every quotation and theorem statement checked against the primary text matched, and no citation was fabricated. The one material correction is that the Olfati-Saber & Murray "iff" error belongs only to the 2003 preprint — the published paper states the true one-directional result — and two of the "does not exist" claims were too strong. Altafini 2013 is still unread, so the exact bipartite-consensus limit formula remains [sa] and must not feed an equation.

## Cross-checks (2026-10-30)

Grep of `docs/prior-work/*.md` (excluding this file) for Kuramoto, Dörfler, Olfati, Altafini, Strogatz, Acebrón, Proskurnikov, Valcher, Laplacian, structural balance, Fiedler and gauge. Files that overlap: 03 §4, 023 §5 and §10, 060 §3-§5, 074 (reference list), 083 §2.4, 084, 090 (Altafini summary), 070 (Alderisio). Nothing else states these works or equations.

**Agreements.**
- `K_c = 2/(π g(0))` and `K_c = 2γ` for the Lorentzian: 060 §4 [std], 023 §5 [standard], this file §1 [read]. Strogatz 2000 read at validation confirms it.
- Incoherence is linearly unstable above K_c and only neutrally stable below: 023 §5 (validation correction) and this file §1.
- Olfati-Saber & Murray: `ẋ = -Lx`, and average consensus for strongly connected balanced digraphs, with switching restricted to that family: 023 §10 [standard], 074 (reference list, DeGroot continuous time) and this file §3.
- Altafini's dichotomy as summarised in 090 (Abelson / signed section): balanced with a spanning tree gives polarisation; strongly connected and imbalanced gives decay to zero. This matches the corrected form in this file §4 point 1.
- Altafini's limit `σ_i (1/n) Σ σ_j x_j(0)` is unverified: 023 §10 marks it standard; this file marks it [sa]; 083 §2.4 finds that Meng et al.'s theorems do not support the zero claim. All three agree it must not feed an equation.
- Altafini 2013 is not read in any file. 060 §5, 083 §2.4, 023 §10 and this file all mark it [sa] or abstract only.
- Structural balance: 03 §4 (Cartwright-Harary, all cycles) and 023 §5 (complete graph, two factions) agree; 060 §5 says they are compatible. 085 adds digon sign-symmetry, which 03 §4 does not state.
- Alderisio et al. 2017 (Kuramoto fit to seven people, two groups): 060 §3 [read, arXiv v4] and 070 agree on the citation and the description. This file does not read it.

**Contradictions.** Each is recorded with both claims. None is resolved here.
1. **Altafini's connectivity hypothesis.** This file §4 (correction 1, Proskurnikov et al. Example 1 [read]): the balanced-iff-consensus, unbalanced-to-zero dichotomy needs strong connectivity; an unbalanced group with an isolated sub-clique keeps its state. 023 §10 (validation-corrected): "connected (strongly connected, if directed)". 060 §5: "convergence to a non-trivial consensus is possible if and only if the graph is structurally balanced", with no connectivity hypothesis; 060 itself flags the omission. Verdict: **unresolved.** Altafini 2013 is unread, and the validation log settles Proskurnikov's Example 1 only, not Altafini's own statement.
2. **Kuramoto K_c versus Dörfler-Bullo's threshold.** This file §2 and summary item 1: different quantities (onset of partial synchrony versus full locking with phase cohesion; D-B's "Relation to Kuramoto" passage, read, says the same). 023 §5 and §10 and the summary table in 023 (near line 663) list "Kuramoto threshold, Dorfler-Bullo" as one theorem row. Verdict: **unresolved** in the file's framing. The D-B text as read supports this file, but the validation log does not record that passage as checked.
3. **Scope of "no Kuramoto fit to human data".** This file (Does it predict? and "Does not exist (in what was read)") says no sources read fit K to human data. 060 §3 reports Alderisio et al. 2017 fitting K to seven people, with 1.25 and 4.40 per group, from a preprint 060 read. Verdict: **no factual conflict**, because this file's claim is scoped to its own reading. But D217 must cite 060 §3 as an existing fit, not as absent.
4. **Altafini's zero limit.** 023 §10 and 060 §5 state "otherwise all states go to zero" without qualification. This file §4 (point 1) and 083 §2.4 say the zero claim is not established for the non-strongly-connected case. Verdict: **unresolved**, pending Altafini 2013.

**Ledger lines** (returned to the orchestrating step; kept here only as the cross-check record).
- Drives: (i) Kuramoto ω_i as a person's intrinsic rate, if a cyclic urge is read as a rotating phase, this file §5 [sa, file's own reading]; (ii) Altafini 2012 own-opinion decay as a restoring drive toward 0, this file §5 [read]; (iii) sign of a tie as affiliation versus rivalry, no source derives it, this file §5 [sa, file's own reading].
- Equations: model `dθ_i/dt = ω_i + Σ K_ij sin(θ_j − θ_i)` and its mean-field form [read, Acebrón eq. 1]; self-consistency (Acebrón eq. 12) [read]; `K_c = 2/(π g(0))` [read, duplicated in 060 §4 and 023 §5]; Lorentzian `r = sqrt(1 − K_c/K)` [read, duplicated in 023 §5]; eq. 14 asymptotic `r` [read]; noise `K_c = 2D + 2γ` [read at validation, Acebrón §III/V.D]; D-B `K_critical = ω_max − ω_min` and `sin γ = K_critical/K` [read, Thm 4.1]; D-B `r_∞ ≥ sqrt((1 + sqrt(1 − (K_crit/K)²))/2)` [read]; D-B `K > n(ω_max − ω_min)/(2(n − 1))` [read, eq. 3.3]; OS&M `ẋ = −Lx`, `L = Δ − A` [read, eqs 6, 12; duplicated in 074 as standard]; OS&M Thm 8 rate `κ = λ_2` of the mirror graph [read]; OS&M Thm 10 `τ* = π/(2 λ_max)` and `τ ≤ π/(4 d_max)` [read; the second is this file's Geršgorin step]; Altafini-as-restated `ẋ = −L[A]x`, `L_jk = −a_jk` [read in Proskurnikov et al.; the same model appears as Abelson in 090]; Altafini limit `σ_i (1/n) Σ σ_j x_j(0)` [sa; not to feed an equation].
- Definitions: arc `Δ(γ)` and phase cohesiveness, Lemma 2.1 `r ∈ [cos(γ/2), 1]` [read, D-B §2]; structural balance with digon sign-symmetry, Cartwright-Harary form [read in Proskurnikov and Altafini 2012; dup 03 §4]; balanced digraph `deg_in = deg_out` and mirror graph `(L + Lᵀ)/2` [read, OS&M Def. 1 and Thm 8; dup 023 §10 "balanced digraphs" as standard]; modulus consensus and ISB subgraph [read, Proskurnikov et al. Thm 1]; order parameter `r e^{iψ} = (1/N) Σ e^{iθ_j}` [read, Acebrón].
- Empirical results: D-B numerical sampling, uniform g on [−1, 1], n ≤ 300, 1000 draws, converging to `4/π` [read, Fig. 4.1; controlled: frequency spread and K]; Acebrón's qualitative applause example, no data [read, crowd]; Altafini 2012 simulations and the debt-ceiling illustration, no data fitted [read, group]; OS&M simulations of engineered agents only [read]; Proskurnikov et al.'s statement that they are "working with sociologists", no test reported [read]; Alderisio et al. 2017, Kuramoto fit to seven people, `c = 1.25` and `4.40` per group, graph ordering reproduced [sa here; read in 060 §3, dup 060 §3].

**Verdict on this cross-check.** No file contradicts this file's equations or citations. Three points stay open: the connectivity hypothesis of Altafini's theorem (contradiction 1, the same as 060 §5 versus 023 §10), the K_c versus D-B framing in 023 (contradiction 2), and the Alderisio fit that D217 must take up (contradiction 3). Altafini 2013 remains unread, so every claim tied to it stays [sa].
