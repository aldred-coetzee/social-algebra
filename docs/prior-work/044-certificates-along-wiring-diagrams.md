# Prior work 44: do passivity, dissipativity, ISS and contraction certificates compose along wiring diagrams?

Direction: D027

Date: 2026-10-29. Survey for the social-algebra strand. Question (research map D027): *is it open that passivity, dissipativity, ISS or contraction certificates compose along wiring diagrams?* Seeds: Baez & Fong; Arcak; Lohmiller & Slotine; Sontag; Jiang, Teel & Praly; Willems. Builds on file 40 (sections 1, 4, 5, 6 and the "Unconfirmed" gap on dissipativity along O_W) and does not repeat it.

**Method and honesty note.** Downloaded and read as text from arXiv this session (so tagged `[read]` where I cite a statement): Capucci & Myers 2026 (Sections 1, 4.1-4.3, 5, key definitions; the appendix on the double-categorical construction was only skimmed); Forni & Sepulchre 2013 (Definition 4, Theorems 2-4 and Examples 1-2; proofs not checked); Angulo & Slotine 2016 (statement and Theorem 1; proofs not checked); Baez & Fong abstract and introduction; Vagner-Spivak-Lerman and Schultz-Spivak-Vasilakopoulou abstracts plus keyword searches of the full text for stability terms; Kawano & Bullo abstract. Classical theorems (Sontag, Jiang-Teel-Praly, Lohmiller-Slotine, Moylan-Hill, Arcak) were **not** re-read here: they are `[standard account]` and file 40 holds their DOIs. DOIs below were resolved at `api.crossref.org/works/<doi>` unless marked arXiv-only.

## Verdict on D027, stated first

**Not open in the way file 40 framed it, and not closed either.** File 40 said no general theorem of the form "dissipativity / contraction composes along wiring diagrams in the O_W sense" could be confirmed. Corrected position after this pass:

| Certificate | Composition along a wiring diagram, in a categorical shell | Status |
|---|---|---|
| ISS / LISS Lyapunov function | **Yes, in outline.** Capucci & Myers (arXiv April 2026) give a rule COMP: certified wiring diagrams act on certified machines, preserving certification, with ISS Lyapunov functions as an instance. | Preprint (ACT 2026 submission), new, unreviewed as far as I can tell. Only the **sequential** case is worked; no feedback/small-gain theorem is derived. |
| Lyapunov stability of flows / coalgebras | Categorical Lyapunov theorem (axiomatic setting for stability), Ames-Moeller-Tabuada 2025; Ames-Mattenet-Moeller 2025. | Abstract only read. Concerns existence of Lyapunov morphisms, not composition along wiring diagrams. |
| Passivity (linear, circuits) | Passive linear circuits form a category and the black-box functor to Lagrangian relations is monoidal and a hypergraph functor (Baez & Fong). | `[read]` abstract and intro. Closure of a class under composition, not a dissipation-inequality theorem. |
| Passivity / dissipativity (nonlinear, storage function) | **No categorical statement found.** Classical feedback-interconnection theorems exist outside any wiring-diagram formalism; the differential version is in Forni-Sepulchre. | Open as a categorical result. |
| Contraction | **No categorical statement found.** Classical modular combination theorems (Lohmiller-Slotine, Slotine, Russo et al.) and a network sign-stability result (Angulo-Slotine) exist. | Open as a categorical result. |

So the true gap, narrowed: **the nonlinear passivity/dissipativity and contraction certificates have no operadic or lens-theoretic composition theorem that I could find; the ISS certificate has a first one, six months old, with only the cascade case worked.** Everything below supports that.

---

## 1. Capucci & Myers (2026): assume-guarantee and ISS Lyapunov functions as certified lenses

**Citation.** Capucci, M., Myers, D. J. (2026). Compositionality of Lyapunov functions via assume-guarantee reasoning. arXiv:2604.03017 [cs.LO], 3 April 2026; "Submitted to ACT 2026" on the title page. Strathclyde / Topos Institute. Verified at arxiv.org/abs/2604.03017 (downloaded and read). No DOI (preprint). Funded by ARIA grants MSAI-PRO-01 and MSAI-PRO-14.

**Their vocabulary.** Generalised Moore machine (state, view v: S -> O, update u: S x I -> S, as a lens); assume-guarantee certificate; tangency (a fibration with a section); loose right module over a symmetric monoidal double category of lenses ("2-algebra of systems"); certified wiring diagram; **slack**; storage function; comparison functions K, K-infinity.

**Drives/operands.** None; this is pure systems theory. The operand is a machine with a distinguished equilibrium and a storage function.

**Operators / equations (stated exactly)** `[read]`:
- Assume-guarantee for a Moore machine, eq. (1.1): `(u, v) |= (phi, alpha) <-> (phi, gamma)` means `phi(s) and alpha(i) => phi(u(s,i))` and `phi(s) => gamma(v(s))`. In words: from a safe state, if inputs satisfy the assumption, the next state is safe, and the observable satisfies the guarantee.
- Proof rule COMP: if a wiring diagram w is itself certified (its outer assumption implies each inner machine's assumptions, and the inner guarantees imply the outer guarantee), then the composite `w . (m1 || ... || mn)` satisfies the outer certificate. Soundness is by lens composition in the category of subsets.
- Proof rule SUBST: if machine S' is certified and S' simulates (coarse-grains) S via sigma, then S is certified (fibrancy of the certified over the uncertified machines).
- Definition 4.6 (ISS): there exist kappa1, kappa2, kappa3 in K-infinity such that for every input a and trajectory x, `|x(t,a)| <= kappa1(kappa2(|x(0)|) e^{-t}) + kappa3(||a||_inf)` for all t >= 0.
- Theorem 4.7 (LISS Lyapunov, attributed to Sontag-Wang, their ref [33, Thm 3.4]): the equilibrium of the open ODE is local ISS precisely when there is a differentiable local storage function phi and kappa1, kappa2 in K with `kappa1(|a|) >= dphi(f(x,a)) + kappa2(phi(x))` for all a, x. Corollary 4.8: global if phi is radially unbounded.
- Eq. (4.7), certified loose map (a certified wiring diagram): `alpha2(w(o1), a2) + kappa(gamma1(o1)) >= alpha1(w#(o1, a2))` and `gamma1(o1) >= gamma2(w(o1))`, with kappa in K-infinity-or-zero called the **slack**. Certified lenses compose by lens composition and **addition of slacks**.
- Eq. (4.9)-(4.10): an equilibrium of an open ODE is LISS iff it is a certified ODE with certificate of the form `alpha(a) >= dphi(f(x,a)) + (id - lambda)(phi(x))` and `phi(x) >= gamma(v(x))`, where the input predicate alpha cannot depend on the state and `id - lambda in K-infinity` (lambda = 0 is allowed).
- Example 4.15 (sequential composition): the lens `s(m,o) = o, s#(m,o,a) = (a,m)` composes two certified ODEs; choose slack kappa with `kappa(gamma1) >= alpha1` (the first component's guarantee must imply the second's assumption); then the cascade is certified with assumption `(alpha1 + alpha2) pi2` and guarantee `gamma1 + gamma2`. This recovers "ISS systems compose sequentially" (Sontag 1989; their ref [33, section 4]).

**Theorems or derived predictions.** The main theorem is structural: symmetric monoidal loose right modules of certified machines over double categories of certified wiring diagrams can be built 2-functorially from fibrations internal to the 2-category of tangencies. The paper states (Section 4.3) that ISS preservation under composition needs two conditions: the composing lens's outer interface must carry a certificate of the form `alpha pi2` (input-only assumption), and there must be "enough slack" to pull through composition.

**What is not in it** `[read]`: the paper does not state the **feedback** case, so neither the small-gain theorem of Jiang-Teel-Praly nor the network version of Dashkovskiy-Ruffer-Wirth is derived. The sole worked composite is the cascade, "a special case of feedback wiring" in the authors' own words, whose assumption chain `kappa(gamma1) >= alpha1` is a one-way implication, not a loop-gain condition. The paper's own Future Work (Section 5) lists POMDPs and supermartingale certificates, not feedback or passivity.

**Empirical standing.** None; a formal paper, new. Not peer-reviewed as read (submission to ACT 2026). Treat as a credible first result by authors who did the earlier generalised-Moore-machine and double-operadic work, not as settled.

**Operand/operator translation.** Operand: a drive module as a machine with an equilibrium (a set-point) and a storage function (distance from set-point, the Keramati-Gutkin drive function of file 16 is the natural instance). Operator: certified wiring. What this gives the algebra: a *typed* proof rule, "the composite is ISS if the wiring is certified and the slack suffices", where the certificate sits in the interface. It supplies the hierarchical case (a leader/follower or parent/child chain) with a categorical proof; it does **not** yet supply the mutual, loop case, which is exactly the de-escalation case of file 40 section 4b.

---

## 2. Ames, Moeller, Tabuada (2025) and Ames, Mattenet, Moeller (2025): categorical Lyapunov theory

**Citations.** Ames, A. D., Moeller, J., Tabuada, P. Categorical Lyapunov Theory I: Stability of Flows. arXiv:2502.15276; published in *Applied Categorical Structures* (2026), DOI 10.1007/s10485-026-09881-z (Crossref-resolved, issued 22 Oct 2026). Ames, A. D., Mattenet, S., Moeller, J. Categorical Lyapunov Theory II: Stability of Systems (title on the PDF reads "Categorical Lyapunov Stability II"). arXiv:2505.22968 (29 May 2025); I did not find a journal DOI.

**Their vocabulary.** "Setting for stability" (axioms for doing Lyapunov theory in a category), Lyapunov morphism, enriched categories (Lawvere metric spaces), F-coalgebra, converse Lyapunov theorem.

**Drives/operands.** None.

**Operators / equations.** `[read, abstracts]` Paper I: with minimal axioms they "define the stability of equilibria, formulate Lyapunov morphisms, and demonstrate that the existence of Lyapunov morphisms is necessary and sufficient for establishing the stability of flows." Paper II: two definitions of a setting for stability for F-coalgebras, a Lyapunov theorem for both and a converse for the richer one. Section 5 of paper II is titled "Monoidal Settings for Dynamic Stability" (contents page; the section was **not** read).

**Theorems.** As stated in the abstracts. Whether the monoidal settings yield "composite of stable systems along a wiring is stable" I could not establish; the contents page suggests the monoidal structure is used for parallel products, not feedback.

**Empirical standing.** None, formal. Peer-reviewed for paper I.

**Translation.** The relevant point is the *shape*: a Lyapunov function as a **morphism** into a reference system. If drive stability certificates are morphisms, then composing them along wiring is functoriality, which is the Capucci-Myers move. Which structure covers the algebra's drive composition is not shown by these papers.

---

## 3. Baez & Fong (2018): passive linear networks as a category

**Citation.** Baez, J. C., Fong, B. A compositional framework for passive linear networks. *Theory and Applications of Categories* 33 (2018) 1158-1222. DOI 10.70930/tac/zdyktmkc (Crossref confirmed). arXiv:1504.05625v6. Abstract and introduction read; the 200k-character body not read in full.

**Their vocabulary.** Passive linear circuit; circuit with boundary; open circuit as a cospan of finite sets with decoration; black box functor; Lagrangian relation; symplectic vector space; hypergraph category; decorated cospan; corelation; power functional; "principle of minimum power."

**Drives/operands.** None. "Passive" here is the engineering sense of the components: they "do not produce energy", so batteries and current sources are excluded.

**Operators / equations** `[read]`:
- The black box functor takes a circuit, forgets internal structure, and keeps the relation between currents and potentials at terminals; two circuits have the same external behaviour iff they impose the same relation. The relation is a Lagrangian linear relation.
- The functor is "symmetric monoidal and indeed a hypergraph functor" (abstract). For resistor circuits, the Lagrangian subspace is `Graph(dQ)`, with Q the circuit's power functional.
- Variable pairs come as flow/effort, tabulated across electronics, mechanics, hydraulics, thermodynamics and chemistry (the table in the introduction).

**Theorems.** The theorem is **functoriality of black-boxing**, not a stability or dissipation-inequality theorem. Circuits built from passive pieces compose into passive circuits in the sense that the class is closed under the category's composition, and composition of circuits maps to composition of Lagrangian relations. The authors say the framework is for the *linear* passive case and name nonlinear resistors, diodes, and sources as excluded (introduction `[read]`).

**Empirical standing.** Textbook circuit theory for the underlying physics; the categorical packaging is a proved theorem in the paper (reviewed journal).

**Operand/operator translation.** The one correct reading of the seed: Baez-Fong show that **a class defined by a passivity-like property (no energy production) is closed under composition in a categorical shell**, and that the external behaviour of the composite is the composite of external behaviours. That is the template for what a drive algebra needs. It does not extend to nonlinear or amplifying systems, so for people, who amplify, it covers only the dissipative part. The effort/flow pair question that file 40 left open is not answered for drives; this paper only shows the pairing exists in physical domains.

---

## 4. Vagner-Spivak-Lerman (2015), Schultz-Spivak-Vasilakopoulou (2019), Libkind et al. (2022): what the wiring-diagram shell guarantees

**Citations.**
- Vagner, D., Spivak, D. I., Lerman, E. Algebras of open dynamical systems on the operad of wiring diagrams. *TAC* 30 (2015) 1793-1822. DOI 10.70930/tac/7tz1nkbd (Crossref). arXiv:1408.1598.
- Schultz, P., Spivak, D. I., Vasilakopoulou, C. Dynamical systems and sheaves. *Applied Categorical Structures* 28 (2020); Crossref issue date shows online 5 April 2019, DOI 10.1007/s10485-019-09565-x. arXiv:1609.08086.
- Libkind, S., Baas, A., Patterson, E., Fairbanks, J. Operadic modeling of dynamical systems: mathematics and computation. *EPTCS* 372 (2022), DOI 10.4204/eptcs.372.14 (Crossref). arXiv:2105.12282.
- Myers, D. J. Double categories of open dynamical systems (extended abstract). *EPTCS* 333 (2021), DOI 10.4204/eptcs.333.11 (Crossref). Only the citation was checked.

**What I confirmed by reading the PDF text.** A keyword search of the Vagner-Spivak-Lerman and Libkind texts for "Lyapunov", "stable", "stability", "dissipat", "passiv" found **no stability result** in either (the VSL matches are the word "establish"). The Schultz-Spivak-Vasilakopoulou abstract and body establish "conditions that ensure totality and determinism compositionally" and no Lyapunov content. So the shell guarantees compositional *well-posedness* (totality, determinism) and, for Libkind et al., functoriality of Euler's method for undirected systems, but **not** compositional stability of any kind.

**Translation.** The operadic shell of file 40 section 1 gives wiring, not certificates. That is why the Capucci-Myers addition matters: it is the first piece I found that fastens a certificate to the shell.

---

## 5. Classical composition theorems keyed to certificates (the content that would be categorified)

These are `[standard account]` unless tagged otherwise; DOIs and Crossref resolution are as in file 40, re-checked now for the ones marked (C).

**5a. Passivity and dissipativity.** Willems 1972 (C, DOI 10.1007/bf00276493); Moylan & Hill 1978 (C, DOI 10.1109/tac.1978.1101721, the N-subsystem interconnection theorem). Statement as file 40 section 4b: dissipative subsystems with supply rates s_i whose interconnection gives `sum s_i <= 0` have `sum V_i` as a non-increasing function on the loop. Passivity is preserved by negative feedback and parallel interconnection. Arcak 2007 (C, DOI 10.1109/TAC.2007.902733): strictly passive agents with a **symmetric** (reciprocal) interconnection coordinate; the published abstract is not open, so this stays `[from seminar abstract]` as in file 40.

**5b. Differential passivity (contraction's cousin).** Forni, F., Sepulchre, R. (2013). On differentially dissipative dynamical systems. arXiv:1305.3456 (preprint of the NOLCOS 2013 paper; I did not resolve a DOI). `[read]`:
- Differential dissipativity lifts the storage function and supply rate to the tangent bundle; with quadratic supply rates it gives **differential passivity**, supply `Q = <delta y, delta u>_{W_x}`. It is tied to incremental stability "in the same way as dissipativity is connected to stability" (abstract).
- Theorem 2: Sigma_1 and Sigma_2 (strictly) uniformly differentially passive with the same tensor W, interconnected by `u1 = -y2 + v1, u2 = y1 + v2`; the interconnection is (strictly) uniformly differentially passive from v to y.
- Theorem 3: the same without uniformity (state-dependent W), differential storage `S = S1 + S2`.
- Theorem 4: with excess of output passivity and bounded trajectories, any two trajectories with the same input have outputs that converge, `lim |y1(t) - y2(t)| = 0`.
- Examples 1-2 give a checkable condition: for `x' = f(x) + g(x)u, y = h(x)`, with `M(x) = d_xx m(x)` and invertible Pi, `M^T d_x[M f] <= 0`, `M g = Pi`, `d_x h^T W = M^T Pi`.
- The paper's own keywords are "Dissipativity, incremental stability, contraction analysis"; in the introduction it motivates the construction as a route to contraction-like properties "without explicitly constructing the distance."
- Note the feedback law: `u1 = -y2, u2 = +y1` is a **skew** coupling, which is the reciprocity assumption in disguise; the theorem does not cover arbitrary asymmetric coupling. (D028 territory, not pursued here.)

**5c. Small gain and ISS.** Sontag 1989 (C, DOI 10.1109/9.28018, ISS and cascade); Jiang, Teel, Praly 1994 (C, DOI 10.1007/bf01211469, small-gain for feedback of ISS systems: the loop of gains satisfies `gamma1 o gamma2 < id`); Dashkovskiy, Ruffer, Wirth 2007 (C, DOI 10.1007/s00498-007-0014-8, general networks, gain operator not amplifying around any cycle). The Capucci-Myers cascade example is the first of these only.

**5d. Contraction.** Lohmiller & Slotine 1998 (C, DOI 10.1016/s0005-1098(98)00019-3); Russo, di Bernardo, Sontag 2013 (C, DOI 10.1109/tac.2012.2223355, hierarchical analysis of networks). Parallel, series and (conditioned) feedback combinations of contracting systems are contracting (Lohmiller-Slotine section 3, `[standard account]`).

**5e. Contraction with signed, asymmetric edges.** Angulo, M. T., Slotine, J.-J. E. Qualitative stability of nonlinear networked systems. *IEEE Trans. Automatic Control* 62(8) (2017) 3881-3884 range not checked; Crossref gives issue date 2017-08, DOI 10.1109/tac.2016.2617780; arXiv:1603.06483. `[read]` Theorem 1: the system `x_i' = f_i(x, t)` with `a_ij = df_i/dx_j` is **contracting** if (i) for reciprocal edges, `a_ji = -b_ij a_ij` for some `b_ij(x,t) > 0` (reciprocal interactions have opposite signs), (ii) self-loops are negative and strong enough: `a_ii = -alpha_i` with `alpha_i > (1/2) sum_{j in N_i} b_ij'/b_ij`, (iii) the graph has no cycles of length 3 or more. Corollary 1: if the asymmetries b_ij are constant, contracting iff-sufficiently `a_ii < 0` and no cycle of length >= 3. They state that, for linear time-invariant functions, the result reduces to the classical sign-stability criterion. Section IV extends to delayed interconnections and to **modules** (sets of nodes). This is a *network-structural* composition theorem for contraction: it needs the **signs and cycle structure** of the wiring, not the numerical gains.

Related: Angulo, Liu, Slotine, Network motifs emerge from interconnections that favour stability. *Nature Physics* (2015), DOI 10.1038/nphys3402 (C); arXiv:1411.5412. `[read, abstract only]` Network motifs are overrepresented patterns; most arise from interconnections that "best exploit the intrinsic stability characteristics of individual nodes", at node and module scale.

**Recent contraction-ISS bridge.** Kawano, Y., Bullo, F. Input-to-state stability implications in contraction theory. arXiv:2607.05640 (v2, 8 July 2026), `[read, abstract only]`: an incremental ISS-type bound on a control system is equivalent to an ISS-type bound on its variational system, and an infinitesimal contraction condition is equivalent to an incremental Lyapunov condition. Not about composition; relevant because it ties the Capucci-Myers certificate (ISS) to contraction, which would be a route to a categorical contraction rule. I did not read beyond the abstract.

---

## 6. Where the gap actually is, and what is still unknown

What a search found (Artifact-style negative result, bounded by what I searched): no paper on a **compositional storage-function theorem for passivity** in the lens/operad shell, and none on **contraction metrics as certificates in a wiring-diagram algebra**. Searches covered "passivity/dissipativity categorical compositional open systems lens storage function Dirac" and "compositional contraction wiring diagram operad hypergraph category". The first returned only engineering port-Hamiltonian papers (and one exergetic port-Hamiltonian modelling language built on an undirected wiring-diagram operad, `[from search summary, not read]`, so I do not know what theorem, if any, it contains); the second returned classical contraction results and an operator-network paper that is about well-posedness. Absence of hits is not proof of absence; arXiv math.CT / math.DS sweeps by name were not done.

Open sub-questions, in decreasing order of tractability for this strand:
1. **Feedback in the certified-lens setting.** Does COMP applied to a feedback wiring recover the Jiang-Teel-Praly small-gain condition as a slack condition? The cascade example suggests the slack kappa plays the role of a gain; a loop would need `kappa o gamma < id` around the cycle. Not shown in the paper; a derivation worth doing by hand.
2. **Passivity as a certified lens.** The supply rate `s(u,y) = u^T y` gives a "dissipation" certificate with input *and* output on both sides, unlike the ISS certificate whose assumption depends on inputs only. Capucci-Myers require the outer assumption to be input-only. Whether passivity fits needs a different certificate shape.
3. **Contraction as a certified lens.** Differential storage functions (Forni-Sepulchre) live on the tangent bundle; the Capucci-Myers framework already uses a *tangency* and the lexicographic order on `(phi, dphi)` pairs, so there is structural room. No statement found.
4. **Whether sign-structure results (Angulo-Slotine) are a wiring-diagram theorem.** Condition (iii), no cycles of length >= 3, is a property of the diagram, which is what a "certified wiring diagram" would encode.

## What exists vs what does not

**Exists:**
- A first categorical composition rule for ISS Lyapunov certificates, with a general proof rule (COMP) and the cascade worked (Capucci & Myers 2026, `[read]`).
- Categorical axiomatisations of Lyapunov theory itself (Ames et al. 2025, abstracts).
- A categorical closure result for passive linear circuits (Baez & Fong, `[read]` abstract and intro).
- Classical compositional theorems for passivity, small-gain/ISS, contraction, differential passivity (Forni-Sepulchre `[read]`), and one graph-structural contraction theorem for signed asymmetric networks (Angulo-Slotine `[read]`).
- The wiring-diagram shell with compositional well-posedness (totality, determinism) but no stability (VSL, SSV, Libkind: keyword search of the text).

**Does not exist (as far as found):**
- A categorical composition theorem for nonlinear dissipativity or passivity with a storage function.
- A categorical composition theorem for contraction.
- A feedback or small-gain theorem inside the certified-lens framework.
- Any application of these to drives, motivation or emotion (unchanged from file 40).
- Peer review or independent use of the 2026 Capucci-Myers preprint.

**For the algebra:** the correct scope statement is "ISS certificates compose along cascades categorically today; loops, passivity and contraction need the classical theorems stated by hand, or new work." That is a workable plan: the hierarchical (cascade) part of a drive algebra can lean on a proved result; the mutual-coupling part has to carry its theorem as a stated assumption.

## Unconfirmed

- Whether Capucci-Myers' later sections/appendix contain a feedback or loop result; the main text I read does not. Appendix A (monoidal double Grothendieck construction) skimmed only.
- Whether Ames-Mattenet-Moeller Section 5 gives composition of stable systems along wirings.
- The exergetic port-Hamiltonian modelling language paper (ScienceDirect, from a search summary): what theorem, if any, it states about storage and wiring diagrams.
- Bakirtzis, Fleming, Vasilakopoulou, Categorical Semantics of Cyber-Physical Systems Theory, *ACM TCPS* 5(3) 2021, DOI 10.1145/3461669 (Crossref resolved): whether it contains any stability certificate composition; not read.
- Fong, Sobocinski, Rapisarda, A categorical approach to open and interconnected dynamical systems, LICS 2016, DOI 10.1145/2933575.2934556 (Crossref resolved): Willems-style behavioural composition; not read, so whether it touches dissipativity is unknown.
- Proofs of Forni-Sepulchre Theorems 2-4 and of Angulo-Slotine Theorem 1 were not checked; statements only.
- Angulo-Slotine TAC page range and Forni-Sepulchre's published conference DOI.
- Dashkovskiy-Ruffer-Wirth, Jiang-Teel-Praly, Moylan-Hill, Lohmiller-Slotine statements: from file 40 and the standard account, not re-read.
