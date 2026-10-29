# Prior work 43: wiring diagrams, decorated and structured cospans, network models, open games as a group-as-composite law

Direction: D025

Date: 2026-10-29. Survey for the social-algebra strand. Question (D025): do wiring diagrams, decorated cospans, network models and open games give a "group as a composite with an interface" law usable for drive equations? Includes a worked open-dynamical-systems example (section 8, checked by computer algebra, not just by hand). Cross-references, not repeated: file 14 section 3 (outline of Spivak, Fong, Baez-Fong, network models), file 40 sections 1a, 1b and the open-games entry (Vagner-Spivak-Lerman abstract/intro, Libkind et al., Ghani et al. Definition 3). This file goes back to the sources and transcribes the definitions and composition formulas.

**Method and honesty note.** Primary sources were downloaded as PDFs from arXiv and converted to text with `pdftotext`; the text is what was read, so these are real at-source readings, not summaries by a fetch model. What was and was not read:

- Spivak 2013 (arXiv:1305.0297): introduction, section 2 (Definitions 2.1.2, 2.2.1, Examples 2.1.7, 2.2.10) and section 6 in full. Sections 3 to 5 (invariants, typed operad, closed operads/recursion) skimmed only by heading.
- Vagner-Spivak-Lerman (arXiv:1408.1598v2): introduction; Definitions 2.9, 2.13, 3.1, 3.8, 4.2, 5.4; Remarks 2.10 to 2.12; Example 4.1; Propositions 4.5 and 5.5 (statements; the proofs only skimmed).
- Fong 2015 (arXiv:1502.00872v3): sections 1, 3 (Definition 3.1, Proposition 3.2, Theorem 3.4) and the circuit example in section 5. Section 4 and the appendix not read.
- Fong thesis (arXiv:1609.05382): abstract, table of contents and the chapter summaries only. The chapters themselves were not read.
- Baez-Fong 2018 (arXiv:1504.05625v6): abstract, Theorem 1.1, Definition 7.6, Theorem 7.7 and the power-functional passages of the introduction. Not the proofs.
- Baez-Pollard 2017 (arXiv:1704.02051v5): Definitions 13 and 14, Lemmas 15 and 16, Theorems 17, 18 and 23, the black-boxing example, and the conclusions.
- Baez-Foley-Moeller-Pollard (arXiv:1711.00037v4): introduction, Definition 2, Theorem 3, Theorem 49, Example 53. Not the Grothendieck-construction machinery.
- Baez-Courser (arXiv:1911.04630v3): abstract and introduction only.
- Baez-Courser-Vasilakopoulou (arXiv:2101.09363v4): abstract, introduction, Theorems 3.1 and 4.1, and section 6.4 (the argument that open dynamical systems are not a structured-cospan case) in full.
- Ghani-Hedges-Winschel-Zahn (arXiv:1603.04641v3): Definitions 3 and 9, Theorem 1, conclusions.
- Fong-Spivak, Seven Sketches (arXiv:1803.05316v3): section 6.5 introduction and Definition 4.2 only. The book is 360 pages; the rest was not read.
- Myers, Categorical Systems Theory, **draft dated 3 September 2023** (davidjaz.com/Papers/DynamicalBook.pdf, self-described "work in progress"): preface, Definitions 1.2.1.2, 1.2.2.1, 1.3.1.1, 1.3.1.2, 1.3.2.8, the parallel product and the chapter list. Chapters 3 to 6 (behaviours, double categories, steady-state matrices, doctrines) were NOT read and are D026's job. This is a draft; later versions may differ.

DOIs resolved through the Crossref API on 2026-10-29. Where a paper has none (arXiv-only) that is stated.

## 0. The answer, up front

**There is a proven, usable composition law with an interface, in four different forms, and none of the four is a drive theory.** What each gives:

1. **Directed wiring (Vagner-Spivak-Lerman 2015; Myers draft).** A group is a box with typed input and output ports; its dynamics is obtained from the members' dynamics by a formula. This is a functorial law (proved: Proposition 4.5, "G is a W-algebra"). It composes *equations*. For a linear module it reduces to one matrix identity (section 3), which is checked in section 8.
2. **Undirected variable-sharing (Fong; Baez-Pollard).** Interfaces are sets of *terminals* identified with state variables; composing glues the apex by a pushout and **adds the vector fields**. This is a functorial law (Baez-Pollard Theorems 17, 18). It also gives the only genuine "property composes" theorem in the set: **steady-state relations compose by relational composition** (Baez-Pollard Theorem 23). It says nothing about stability.
3. **Network models (Baez-Foley-Moeller-Pollard 2020).** A group-forming law for *static* networks only: overlay edges, take disjoint unions, relabel. No dynamics.
4. **Open games (Ghani-Hedges-Winschel-Zahn 2018).** Interface (X, S) to (Y, R) with a **backward** channel; composition is sequential and parallel; the property that composes is the **Nash best-response relation**. Not dynamical, and the solution concept is baked into the definition (the authors say so).

**What none of them proves:** that stability, boundedness, convergence, dissipativity or any other property of the composite follows from properties of the members. The theorems are *functoriality* theorems: "wiring then interpreting equals interpreting then wiring". I searched the Vagner-Spivak-Lerman text for stability, equilibrium, Lipschitz and existence and found no hits (grep, 2026-10-29). Baez-Pollard black-box steady states and say explicitly that its proof "sidesteps" the question of multiple steady states. So the framework is a **bookkeeping calculus for composing equations**, not (yet) a theorem generator for dynamics. A certificate calculus (passivity, small gain, contraction) is a separate layer, and D027 and D030 check whether it composes along these diagrams.

For Aldred's aim ("compose drives into equations"), the useful part is real but narrow: it removes ambiguity about *what the group's equations are* given the members' equations and who listens to whom.

## 1. Spivak 2013: the operad of wiring diagrams

**Citation.** D. I. Spivak, "The operad of wiring diagrams: formalizing a graphical language for databases, recursion, and plug-and-play circuits", arXiv:1305.0297 [cs.DB], v1, 1 May 2013. arXiv-only (no journal DOI found; none claimed). Confirmed by reading the PDF.

**Their vocabulary.** Operad (always "symmetric colored operad" or multicategory, Warning 2.1.1), singly-typed star, wire, cable, cospan, wiring diagram (WD), outer star, inner stars, algebra on an operad, relational S-algebra Rel_A, closed operad, plug-and-play.

**Drives/operands.** None. Operands are finite sets of wires ("stars"); the semantic algebra shown is relations on a set A (database queries, digital circuits).

**Operators / equations, as stated.**

- [read] Definition 2.1.2: an operad O has objects Ob(O); for each object y, finite set n and n-indexed family x of objects, a set O_n(x; y) of morphisms; identities id_x in O_1(x; x); and a composition function

  `∘ : O_n(y; z) × ∏_{i∈n} O_{m_i}(x_i; y(i)) → O_m(x; z)`

  with the laws `φ ∘ (id_{x_1}, ..., id_{x_n}) = φ`, `id_y ∘ φ = φ`, and associativity (footnote 2, a commuting diagram). Spivak's own slogan: "a wiring diagram of wiring diagrams is a wiring diagram".
- [read] Example 2.1.7 (main operad S): objects are finite sets. A morphism φ : X_1, ..., X_n → Y is a **cospan** of finite sets `X_1 ⊔ ... ⊔ X_n --f--> C <--g-- Y`, taken up to isomorphism of C (renaming cables). Composition is "taking the pushout P of the middle square" (display (7)); the composite is the cospan `⊔_i ⊔_j X_{i,j} → P ← Z`.
- [read] Definition 2.2.1 and Example 2.2.10: an **algebra** on an operad is an operad functor O → Sets. Rel_A(X) = P(A^X), the |X|-ary relations on A. For a wiring diagram φ the image Rel_A(φ)(R_1, ..., R_n) is obtained by forming the pullback Q of `R_1×...×R_n → A^{X_1⊔...⊔X_n} ← A^C` and taking the image of Q in A^Y ("φ-conjunction"). The text says Rel_A "respects the composition formula (7)" because epi-mono factorisations in Set are unique.
- [read] Section 1: the paper motivates the framework with Minsky's *Society of Mind* and says the same hierarchical structures "can be extended beyond the individual to encompass interactions between multiple humans and machines". It then offers the relational algebra as "a crude model for agencies in the brain: we simply think of each agency as maintaining a relationship on its inputs. For example a person might be said to maintain a relationship between what she sees, hears, feels, and does; this can be represented as a 4-ary relation." This is as far as it goes toward people; no development.

**Theorems or derived predictions.** Section 3 conjectures that there are no non-trivial invariants of relations natural in wiring diagrams; formally, Conjecture 3.1.6 states that Rel_A is *quotient-free* (any epimorphism of algebras out of Rel_A is an isomorphism or lands on the terminal algebra). Reading this as "no simplifying summary statistic survives wiring" is my gloss. Lemma 4.1.2 extends the Rel_A to a single algebra Rel on the typed operad T; Proposition 4.3.1 lifts Rel to join-semilattices for disjunctive queries (validation correction: the earlier text credited the extension to Proposition 4.3.1). Section 5: S and T are closed operads, giving recursion (factorial example) and "plug-and-play". Not read in detail.

**Empirical standing.** A mathematical framework paper; no empirical claim to test. Open mathematical questions are listed in Section 6.1 (for instance whether Rel_A can be characterised).

**Operand/operator translation.** *Operand*: a person or group as a "star", a finite set of typed wires (what it senses and does). *Operator*: a wiring diagram nesting members inside a group box. The law "a group of groups is a group" is the operad associativity, and it is proved. **Limit:** semantically the algebra is *relations*, which carry no time; the dynamical algebras come in the next paper.

## 2. Vagner, Spivak, Lerman 2015: open dynamical systems on the wiring operad

**Citation.** D. Vagner, D. I. Spivak, E. Lerman, "Algebras of open dynamical systems on the operad of wiring diagrams", *Theory and Applications of Categories* 30 (2015), 1793-1822. DOI 10.70930/tac/7tz1nkbd (Crossref-confirmed). arXiv:1408.1598v2. Read at source.

**Their vocabulary.** Box, input port, output port, typed finite set (TFS), wiring diagram, "no passing wires", open dynamical system (ODS), state space, readout, W-algebra, algebras G (general) and L (linear). Boxes in the tank example are salt tanks.

**Drives/operands.** None. The worked example is salt in interconnected tanks (a textbook problem from Boyce and DiPrima).

**Operators / equations, as stated.**

- [read] Definition 2.9 (open dynamical system): smooth manifolds M (state), U^in, U^out; a pair of maps `f^in : M × U^in → TM` (with f^in(m,u) in T_m M) and `f^out : M → U^out`. **Note the readout depends on the state alone, not on the input.** The linear case takes Euclidean spaces and linear f.
- [read] Remark 2.12 (the whole idea in one line): feeding a readout back to an input is substitution, `F'(m, a) := F(m, a, g_B(m))`. The two-system version: `F'(m_1, m_2, a) := (F_1(m_1, a, g_B(m_2)), F_2(m_2, g_1(m_1)))`.
- [read] Definition 3.1: a **box** is X = (X^in, X^out), a pair of typed finite sets. A **wiring diagram** Φ : X → Y is a triple (X, Y, ϕ) with ϕ a typed bijection

  `ϕ : X^in + Y^out → X^out + Y^in`

  satisfying **no passing wires**: `ϕ(Y^out) ∩ Y^in = ∅`, equivalently `ϕ(Y^out) ⊆ X^out`. It decomposes as `ϕ^in : X^in → X^out + Y^in` and `ϕ^out : Y^out → X^out`. The bijection means every inner input is fed by exactly one source, no port is left dangling, and nothing is split.
- [read] Remark 3.7 explains the no-passing-wires condition: it prohibits wires going straight across the outer box, "a loop emerges because the inner diagram has a (prohibited) passing wire" (Figure 5b). The Seven Sketches text (section 6.5) says the authors "realized that in order for feedback to make sense, the wiring diagrams could not involve ... 'passing wires'".
- [read] Definition 3.8: monoidal product `X_1 ⊕ X_2 := (X_1^in + X_2^in, X_1^out + X_2^out)`, unit the closed box 0 = (∅, ∅). Proposition 3.11: (W, ⊕, 0) is a symmetric monoidal category; the operad O_W comes from it by Definition 2.1.
- [read] Definition 4.2 (algebra G): for a box X, `G(X) = {(S, f) | (S, X^in, X^out, f) is an open system}`. For Φ = (X, Y, ϕ), `G(Φ)(S, f) = (S, g)`: the state space is **unchanged**, and g = (g^in, g^out) is defined by commuting diagrams (10): `g^out = ϕ^out ∘ f^out`, and `g^in(s, y) = f^in(s, ϕ^in(f^out(s), y))`. In words: **read out the members, route through the wiring, feed the routed signals to the members' input slots, and expose a subset of readouts.** Coherence map `µ((S,f),(S',f')) = (S+S', f×f')` (disjoint union of state variables, product of vector fields). Proposition 4.5: (G, µ) is a lax monoidal functor, i.e. a W-algebra.
- [read] Definition 5.4 (algebra L, linear systems): writing a linear system in blocks `f = [[f^{S,S}, f^{S,X}], [f^{X,S}, 0]]`, the wired system has

  `g^{S,S} = f^{S,X} ϕ^{X,X} f^{X,S} + f^{S,S}`  (the text gives this as the example of reading (13) off diagram (10)).

  The block `f^{S,X}` is how inputs push the state, `f^{X,S}` is the readout, and `ϕ^{X,X}` is the part of the wiring that routes inner outputs to inner inputs. Proposition 5.5: L is a W_Lin-algebra.
- [read] Example 4.1: the tank problem is `Q̇_1 = −.1 Q_1 + .075 Q_2 + 1.5`, `Q̇_2 = .1 Q_1 − .2 Q_2 + 3`. The point made is that "each box in a wiring diagram should only 'know' about its own inputs and outputs, and not how they are connected to others" (the derivation of the coupled equations used a hidden step, which the wiring diagram makes explicit).

**Theorems or derived predictions.** Propositions 3.11, 4.5, 5.5 only (the structural ones). **No dynamical-property theorem.** No claim about stability or existence of solutions was found by text search.

**Empirical standing.** Mathematics; the tank example is a worked exercise, not a data fit. Published in a mainstream category-theory journal; follow-ups are Libkind et al. (file 40) and Myers (below).

**Operand/operator translation.** *Operand*: a drive module (or a person, or a group) = an open system with input ports (what it listens to) and output ports (what it displays). *Operator*: a wiring diagram, which says who listens to whom. Group = the wiring applied to its members. **Three consequences for the algebra**, all [read] from the definitions:

1. **No instantaneous reflex.** Readout is a function of the state alone. An "automatic" response (percept to action in zero time) cannot be a direct input-to-output map; it must go through a state variable (a fast variable). This is a *design constraint that rules out algebraic loops*, and it is a modelling stance, not a fact about people.
2. **Directedness is built in.** Ports are inputs or outputs; influence is asymmetric by construction. Non-reciprocal influence (A is moved by B's fear, B is not moved by A's) is trivially expressible. (Contrast the passive-network framework, section 5.)
3. **The wiring is part of the group, the members' equations are not.** "Group structure" and "member drives" are separated cleanly, exactly the separation Aldred wants (operands and operators). The wiring is static: nobody rewires during the run (see Limits).

**Limits.** (a) Static wiring: ϕ is fixed, so relationships that appear, break or switch while the system runs need either a time-varying ϕ (outside the framework) or a hybrid layer (D031). (b) Smooth manifolds and ODEs, so thresholds and discrete decisions need a different semantic algebra. (c) Group membership changes (people joining) change the box and therefore need a different diagram.

## 3. Myers, Categorical Systems Theory (draft of 2023-09-03)

**Citation.** D. J. Myers, *Categorical Systems Theory*, book draft, last updated 3 September 2023, https://www.davidjaz.com/Papers/DynamicalBook.pdf (open access; self-described "work in progress ... Use at your own peril!"). Not peer-reviewed. No DOI. Only chapter 1 and the preface were read for this file; D026 owns the rest.

**Their vocabulary.** System, interface, **composition pattern**, lens, arena, passforward/passback, wiring diagram, systems theory, doctrine (chapter 6), "behaviours".

**Operators / equations, as stated.**

- [read] The preface lists the guiding ideas: a system interacts with its environment only through an interface; the environment needs to know only what happens at the interface; interfaces connect by "composition patterns"; given a pattern and systems with those interfaces "we should have a composite system".
- [read] Definition 1.2.1.2: a deterministic system S is a lens `(update_S, expose_S) : (State_S, State_S) ⇆ (In_S, Out_S)` with `expose_S : State_S → Out_S` and `update_S : State_S × In_S → State_S`. The pair (Out_S, In_S) is the system's interface. Definition 1.2.2.1: a differential system has `ds_k/dt = update_S^k(s, i)` over R^n with m parameters and k exposed variables.
- [read] Definition 1.3.1.1: a lens `f = (f, f♯) : (A⁻, A⁺) ⇆ (B⁻, B⁺)` consists of a passforward `f : A⁺ → B⁺` and a passback `f♯ : A⁺ × B⁻ → A⁻`. Definition 1.3.1.2: lens composite has passforward `g∘f` and passback `(a⁺, c⁻) ↦ f♯(a⁺, g♯(f(a⁺), c⁻))`.
- [read] Section 1.3.2 (stated in the text): a system composed with a lens `w = (w, w♯) : (In_S, Out_S) ⇆ (I, O)` is a new system with the **same states** and interface (I, O); wiring diagrams are special lenses. In symbols (my unfolding of Definitions 1.2.1.2 and 1.3.1.2): `update'(s, i') = update_S(s, w♯(expose_S(s), i'))` and `expose'(s) = w(expose_S(s))`. This is the same formula as VSL (Definition 4.2). The parallel product of systems is the product of states, inputs, outputs, with `update((s_1,s_2),(i_1,i_2)) = (update_1(s_1,i_1), update_2(s_2,i_2))`. Wiring a group = parallel product, then a lens.
- [read] Definition 1.3.2.8 (a definition, not an example): a "City" in a multi-city SIR model is a differential system with state (S, I, R), input (inflow, outflow) in R^3 × R^3, exposing the whole state; update `(−k_1 S I + inflow_1 − outflow_1, k_1 S I − k_2 I + inflow_2 − outflow_2, k_1 I + inflow_3 − outflow_3)`. The third component is printed `k_1 I` in the 2023-09-03 draft, almost certainly a typo for `k_2 I` (recovery must balance the −k_2 I in the second line). Definition 1.3.2.9: a population-flow graph (edges labelled by 3×3 real diagonal matrices) specifies the wiring.
- [read] The opening of chapter 1 uses a *fear* example in passing: "Seeing a scary snake can make me recoil and feel fear, but seeing a cute snake plushie can make me go over and start to pet it." This is motivation, not a model.

**Theorems or derived predictions.** Not read (chapters 3 to 6 contain behaviours, double categories, "steady states compose according to the laws of matrix arithmetic" in the chapter 5 heading, and the port-plugging doctrine in 6.3). Do not rely on this file for them.

**Empirical standing.** An unfinished textbook. Libkind and Myers' 2025 follow-up ("Towards a double operadic theory of systems", arXiv:2505.18329) was named in a search result only; not read.

**Operand/operator translation.** Identical to section 2, with the advantage of a cleaner presentation: "wiring a group" is *lens composition*, and the passback lets a wiring carry a signal in the reverse direction (relevant to open games, section 7).

## 4. Fong: decorated cospans, thesis

**Citations.** B. Fong, "Decorated cospans", *Theory and Applications of Categories* 30(33) (2015), 1096-1120, DOI 10.70930/tac/8cw8rvm2 (Crossref-confirmed), arXiv:1502.00872v3. B. Fong, "The algebra of open and interconnected systems", DPhil thesis, University of Oxford, 2016, arXiv:1609.05382. The thesis has no DOI in Crossref (none claimed).

**Their vocabulary.** Cospan X → N ← Y, decoration, F-decorated cospan, hypergraph category (special commutative Frobenius monoid on each object), corelation, black-boxing.

**Operators / equations, as stated (Fong 2015, [read]).**

- Definition 3.1: given a category C with finite colimits and a lax monoidal functor `(F, ϕ) : (C, +) → (D, ⊗)`, an F-decorated cospan is a cospan `X --i--> N <--o-- Y` in C together with an element `s : 1 → F N` (the "decoration"). A morphism is a map of cospans n : N → N' with `F n ∘ s = s'`.
- Proposition 3.2: there is a category FCospan; objects are those of C; morphisms are isomorphism classes of F-decorated cospans. Composition is the pushout `N +_Y M` of cospans paired with the composite decoration

  `1 → 1 ⊗ 1 --s⊗t--> F N ⊗ F M --ϕ_{N,M}--> F(N+M) --F[j_N, j_M]--> F(N +_Y M)`.

  Remark 3.3: "the copair [j_N, j_M] ... encodes the identification of the image of Y in N with the image of the same in M, and so describes merging the 'overlap' of the two decorations". The identity decorated cospan has the empty decoration `1 → F∅ → F X`.
- Theorem 3.4: if F is lax **braided** monoidal into a braided monoidal (D, ⊗), FCospan is symmetric monoidal and a hypergraph category, and there is a wide embedding Cospan(C) ↪ FCospan.
- Section 5 (circuits): the decoration for a resistor network on node set N is a (0,∞)-labelled graph; the semantics is the linear subspace `{(φ, ∇Qφ) | φ ∈ R^N}` with power function `Q(ψ) = Σ_e (1/r(e)) (ψ_{t(e)} − ψ_{s(e)})²`; the Frobenius structure encodes "perfectly conductive wires, forcing the potentials at all nodes they connect to be equal, and the sum of incoming currents to equal the sum of outgoing currents".

**Theorems.** Theorem 3.4 above; Theorem 4.1 (functors between decorated cospan categories from monoidal natural transformations; not read in detail). The thesis adds decorated *corelations* (every hypergraph category is one, per its abstract), a signal-flow/LTI chapter with a "structural characterisation of controllability" (chapter 5; abstract and chapter list only), and the passive-network chapter 6.

**Known correction.** Baez-Courser-Vasilakopoulou (2022, section 3 below) state: "many applications of decorated cospans were flawed", because a functor into **Set** cannot decorate the apex with a *graph* (two graphs on the same node set but different edge sets are distinct decorations, which blocks lax monoidality); the repair needs decorations in a **category** (pseudofunctors into Cat) and a double category rather than a category. Anything that uses Fong 2015 for labelled-graph or Petri-net decorations should be read through that correction.

**Empirical standing.** Pure mathematics with engineering applications (circuits, Markov processes, Petri nets). The framework has been applied in the AlgebraicJulia software stack (file 40), but no social application.

**Operand/operator translation.** *Operand*: a "terminal" set (a set of interface variables); morphism: a system whose internal nodes include those terminals. *Operator*: composition = **glue along shared terminals**, merging overlapping state. The characteristic law is *identification*, not *signalling*: two systems that share a terminal share a variable. For a group this is the natural law for **pooled** quantities (morale, a shared resource, a common level of arousal) and **not** for "A sees B's face".

## 5. Baez-Fong 2018, passive linear networks

**Citation.** J. C. Baez, B. Fong, "A compositional framework for passive linear networks", *Theory and Applications of Categories* 33 (2018), 1158-1222. DOI 10.70930/tac/zdyktmkc (Crossref-confirmed). arXiv:1504.05625v6. Read: abstract, Theorem 1.1, Definition 7.6, Theorem 7.7 and the introduction's discussion of power.

**Their vocabulary.** Circuit with boundary, Dirichlet form, power functional, principle of minimum power, symplectic vector space, **Lagrangian relation**, black box functor, hypergraph functor, corelation.

**Operators / equations, as stated.**

- [read] Theorem 1.1: "There exists a hypergraph functor, the black box functor `□ : Circ → LagRel`, mapping a finite set X to the symplectic vector space `F^X ⊕ (F^X)*` it generates, and an open circuit (N, E, s, t, r, i, o) to the Lagrangian relation `⋃_{v∈Graph(dQ)} S_{t i(v)} × S_{o(v)}` ..., where Q is the circuit's power functional." (Written here as the paper states it; ASCII transcription of the notation.) Theorem 7.7 repeats it for the composite of decorated-cospan and corelation functors in Definition 7.6.
- [read] Introduction: the power dissipated on edge e is `(1/r(e)) (φ(t(e)) − φ(s(e)))²`, and the total power dissipated is twice `P(φ) = ½ Σ_e (1/r(e)) (φ(t(e)) − φ(s(e)))²` (the ½ is the authors' convenience; validation corrected a misplaced factor of two here), and the "principle of minimum power" says that with boundary potentials fixed, the interior potentials choose to minimise it; the resulting boundary function Q on R^{∂N} is again a Dirichlet form, called the power functional, and "this behavior is completely determined by the power functional".

**Theorems.** As above; the paper's claim is that black-boxing is functorial: "we can compute the black boxed version of a circuit made of parts by computing the black boxed versions of the parts and then composing them".

**Empirical standing.** Mathematics, with a standard physical subject matter (the model is Ohm's and Kirchhoff's laws). The authors state the restriction: "We only study circuits built from passive components: that is, those that do not produce energy."

**Operand/operator translation, and why it matters here.** This is the nearest thing in the set to a **conserved-quantity** composition law with a **variational principle** that composes (minimum power). Its structure rests on the Dirichlet form being a **symmetric** quadratic form (reciprocity: current from a to b responds as current from b to a) and on **no energy sources**. [inference, flagged] A social analogue would be *reciprocal, dissipative* coupling: influence that is symmetric and loses something. Fear contagion with a leader, predator and prey, anything driven (energy sources) and anything non-reciprocal is outside this theorem. The result is therefore a good *template* for what a proved composition theorem looks like, and a bad *fit* for most of the drives in files 16 to 23.

## 6. Baez-Pollard 2017, reaction networks: open dynamical systems by gluing

**Citation.** J. C. Baez, B. S. Pollard, "A compositional framework for reaction networks", *Reviews in Mathematical Physics* 29(9) (2017), 1750028. DOI 10.1142/S0129055X17500283 (Crossref-confirmed). arXiv:1704.02051v5. Read at source (definitions, theorems, example, conclusions).

**Their vocabulary.** Reaction network, Petri net, rate equation, law of mass action, open reaction network, open dynamical system, gray-boxing, black-boxing, steady state, semialgebraic relation.

**Drives/operands.** Species concentrations (chemistry; the SIRS epidemic model is the first example). No drives.

**Operators / equations, as stated.**

- [read] Definition 13: concentrations obey the rate equation `dc(t)/dt = Σ_{τ∈T} r(τ) (t(τ) − s(τ)) c(t)^{s(τ)}`, i.e. `dc/dt = v^R(c)` with `v^R(c) = Σ_τ r(τ)(t(τ) − s(τ)) c^{s(τ)}` (equation (8)), where `c^{s(τ)} = ∏_σ c_σ^{s(τ)(σ)}`.
- [read] Definition 14: an **open dynamical system from X to Y** is a cospan of finite sets `X --i--> S <--o-- Y` together with an algebraic vector field v on R^S. The **open rate equation** is `dc/dt = v(c(t)) + i_*(I(t)) − o_*(O(t))`, with `i_*(I)_σ = Σ_{x: i(x)=σ} I_x`.
- [read] Lemma 15: the functor D : FinSet → Set sends S to the algebraic vector fields on R^S and a function f : S → S' to `D(f)(v) = f_* ∘ v ∘ f^*` (pullback f^* copies a value to all preimages; pushforward f_* **sums** over fibres). Lemma 16: D is lax symmetric monoidal with `δ(v, v') = i_* ∘ v ∘ i^* + i'_* ∘ v' ∘ i'^*` (add vector fields on a disjoint union).
- [read] Theorem 17: category **Dynam**: objects finite sets; morphisms equivalence classes of open dynamical systems; **composite** is the cospan `S +_Y S'` with the vector field obtained by applying `D(S) × D(S') --δ--> D(S+S') --D([j,j'])--> D(S +_Y S')` to (v, v'). Dynam is a hypergraph category. Theorem 18: gray-boxing `RxNet → Dynam` (open reaction network to its vector field) is a symmetric monoidal functor.
- [read] Theorem 23: **black-boxing** is a symmetric monoidal functor `Dynam → SemiAlgRel` sending an open dynamical system to the relation between input and output concentrations and inflows/outflows that it imposes **in steady state**. The target category has semialgebraic relations as morphisms, closed under composition by the Tarski-Seidenberg theorem. The worked example (equations (15) to (17)) black-boxes two reaction networks and the composite; the text says the reader should check `□(F'F) = □(F')□(F)` by composing the relations.

**Theorems or derived predictions.** Theorems 17, 18, 23. Plus a caveat the authors state themselves: "Even for relatively simple 'closed' reaction networks ... multiple steady states may be possible"; their functoriality proof "sidesteps this issue". They also compare with Spivak's black-boxing to Rel: "None of his results subsume ours, but they are philosophically very close. Both are doubtless special cases of a more general theorem that is yet to be formulated."

**Empirical standing.** Mathematics; the SIRS and chemistry examples are textbook models, not fits. Deficiency-zero and deficiency-one theorems (Horn, Jackson, Feinberg), which are the standard source of *qualitative* results for reaction networks, are cited in the introduction as the part of the literature this framework does not yet reproduce compositionally.

**Operand/operator translation.** *Operand*: a finite set of terminals; a morphism is a state space plus a vector field, with some state variables named as terminals. *Operator*: glue along terminals, **sum the vector fields**. The summing law is a statement that *contributions to a shared variable add*, which is the structure of a mass-action or "pooled" drive (several drives write to one shared level). The clean theorem is Theorem 23: **a group's set-points (steady states) in terms of its members' steady-state relations are obtained by composing relations** (existential projection of the shared variables). That is a proved *property-level* composition law, and the only one of its kind in this file. Its scope is steady states, not stability, and not oscillation.

## 7. Network models, structured cospans, and open games

### 7a. Network models (Baez, Foley, Moeller, Pollard)

**Citation.** J. C. Baez, J. Foley, J. Moeller, B. S. Pollard, "Network models", *Theory and Applications of Categories* 35 (2020), 700-744. DOI 10.70930/tac/e0rrdvk5 (Crossref-confirmed). arXiv:1711.00037v4.

**Their vocabulary.** Network model, species (Joyal), overlay, disjoint union, operad of a network model, canonical algebra. The motivating example is a search-and-rescue mission with planes, boats and drones as vertices.

**Operators / equations, as stated ([read]).**

- Definition 2: a one-coloured network model is a lax symmetric monoidal functor `F : S → Mon` (S the symmetric groupoid). Theorem 3 unpacks this to: sets F(n) of "networks with n vertices"; identities e_n; an **overlay** `∪ : F(n)×F(n) → F(n)`; permutations σ; a **disjoint union** `⊔ : F(m)×F(n) → F(m+n)`; with twelve equations (identity, associativity of ∪, σ acts by monoid maps, interchange `(g_1 ∪ g_2) ⊔ (h_1 ∪ h_2) = (g_1 ⊔ h_1) ∪ (g_2 ⊔ h_2)`, etc.).
- Theorem 49: the network operad has operations `O_F(n_1,...,n_k; n) = S_n × F(n)` if `n_1+...+n_k = n`, empty otherwise. Example 53 (canonical algebra): the operation (σ, g) acts on networks h_i ∈ F(n_i) by

  `α(σ, g)(h_1, ..., h_k) = g ∪ σ(h_1 ⊔ ... ⊔ h_k)`.

  In words: place the sub-networks side by side, relabel the vertices, then **overlay the group's own extra edges g**. This is the formal version of "a group is its members plus the ties among them", and the extra edges are exactly what an operator adds.

**Theorems.** Theorem 3, Theorem 49, Example 53 and the canonical-algebra statement. Not dynamical.

**Empirical standing.** Pure mathematics with a designed-application motivation; no empirical content. The introduction itself notes that the sets F(n) can be simple graphs, directed graphs, multigraphs, hypergraphs, coloured graphs and Petri nets.

**Operand/operator translation.** A group-forming operation with an **explicit law for what the group adds** (g) and a proved associativity. *Static*: no drive dynamics and no states. This is a candidate for the "who is tied to whom" layer on top of which a dynamical algebra (section 2) is built, but nobody has combined them in the sources read.

### 7b. Structured cospans, and why open dynamical systems need decorated ones

**Citations.** J. C. Baez, K. Courser, "Structured cospans", *Theory and Applications of Categories* 35 (2020), 1771-1822, DOI 10.70930/tac/dca3obx4 (Crossref-confirmed), arXiv:1911.04630v3 (abstract and introduction read). J. C. Baez, K. Courser, C. Vasilakopoulou, "Structured versus decorated cospans", *Compositionality* 4 (2022), 3, DOI 10.32408/compositionality-4-3 (Crossref-confirmed), arXiv:2101.09363v4.

**Operators / equations, as stated.**

- [read] Baez-Courser abstract: for a functor L : A → X with finite colimits and L a left adjoint, a **structured cospan** is a diagram `L(a) → x ← L(b)` in X; one gets a symmetric monoidal category (a hypergraph category) and "a more fundamental structure: a symmetric monoidal double category where the horizontal 1-cells are structured cospans".
- [read] BCV Theorem 3.1 (statement): for A, X with finite colimits and L preserving them, there is a symmetric monoidal double category `L Csp(X)` with objects those of A, vertical 1-morphisms the morphisms of A, horizontal 1-cells L-structured cospans, 2-morphisms commuting diagrams. Theorem 4.1: under a condition on F, the decorated-cospan double category FCsp (for a symmetric lax monoidal pseudofunctor F : (A,+) → (Cat,×)) is isomorphic to `L Csp(∫F)`, with L a left adjoint to the Grothendieck opfibration.
- [read] BCV section 6.4: for **open dynamical systems** with F = D (vector fields on R^S), the opfibration `U : ∫D → FinSet` has **no left adjoint** (the comma category ∅↓U has no initial object: the only object with a map to (∅, v_∅) is (∅, v_∅) itself, and that has no maps to (S,v) unless v is zero). So Theorem 4.1 cannot apply: "in some cases decorated cospans appear to be necessary". Practical meaning: the structured-cospan route is **not** available for dynamics; use decorated.

**Empirical standing.** Pure mathematics; the epidemiology-flavoured application mentioned in the abstract refers to structured epidemic-model tooling (cited, not read).

### 7c. Open games (Ghani, Hedges, Winschel, Zahn)

**Citation.** N. Ghani, J. Hedges, V. Winschel, P. Zahn, "Compositional game theory", *Proceedings of the 33rd Annual ACM/IEEE Symposium on Logic in Computer Science (LICS '18)*, 2018, pp. 472-481. DOI 10.1145/3209108.3209165 (Crossref-confirmed). arXiv:1603.04641v3. Read: Definitions 3 and 9, Theorem 1, conclusions.

**Their vocabulary.** Open game, play, coplay, best response, strategy profile, utility, **coutility**, context, selection function, string diagram.

**Operators / equations, as stated ([read]).**

- Definition 3: an open game `G : (X, S) → (Y, R)` is a 4-tuple `(Σ_G, P_G, C_G, B_G)`: a set of strategy profiles Σ_G; a **play** function `P_G : Σ_G × X → Y`; a **coplay** function `C_G : Σ_G × X × R → S`; a **best-response** function `B_G : X × (Y → R) → Rel(Σ_G)`. "In general, we impose no conditions whatsoever on these components." X: observations; Y: moves; R: utility; S: **coutility** ("values that are returned to the calling environment by the game so that they can become utility for other processes").
- Definition 9: for `G : (X,S)→(Y,R)` and `H : (Y,R)→(Z,Q)`, the composite `H∘G : (X,S)→(Z,Q)` has `Σ_{H∘G} = Σ_G × Σ_H`, `P_{H∘G}((σ,τ),x) = P_H(τ, P_G(σ,x))`, `C_{H∘G}((σ,τ),x,q) = C_G(σ, x, C_H(τ, P_G(σ,x), q))`, and `((σ,τ),(σ',τ')) ∈ B_{H∘G}(x,k)` iff `(σ,σ') ∈ B_G(x,k')` and `(τ,τ') ∈ B_H(P_G(σ,x), k)`, where `k'(y) = C_H(τ, y, k(P_H(τ,y)))`. The text says coplay composition "can be seen as composition of lenses".
- Theorem 1: Game is a monoidal category, "moreover symmetric monoidal" (monoidal product `(X_1,S_1)⊗(X_2,S_2) = (X_1×X_2, S_1×S_2)`, unit (1,1)). Associativity holds only up to equivalence of strategy profiles ("Open games trivially cannot form a category, because this composition operator is not associative on the nose"); Proposition 3 then gives the category Game of equivalence classes.
- Conclusions ([read], their own limitations): only simultaneous and sequential games, **pure** strategies, and the **solution concept of Nash is built into the definition of an open game**; they call for alternatives, mixed strategies, and subgame-perfect equilibrium.

**Theorems.** Theorem 1; the abstract states that a variety of games are faithfully represented (same Nash equilibria and off-equilibrium best responses); Theorem 2 was not read (the paper has Theorems 1 and 2 only, plus Propositions 1 to 3; validation removed a reference to a non-existent Theorem 3). Nothing about dynamics, learning, or preferences that change.

**Empirical standing.** Formal game theory; the authors' examples are standard toy games (prisoner's dilemma, matching pennies, battle of the sexes, chicken); markets appear only as motivation in the conclusions. (Validation correction: an earlier draft said "duopoly, market".) No behavioural validation. The follow-up (open games with agency, Capucci et al. 2022) is catalogued in file 40 and is D035's direction.

**Operand/operator translation.** *Operand*: a decision-maker with an observation, a choice, a payoff received, and a payoff passed back to others. *Operator*: sequential and parallel composition. The one feature worth taking: **a backward-flowing channel** (coutility), a pre-existing formal home for "what I get from you becomes what you value". But preferences here are *fixed utility functions*, with no drive dynamics, no decay, no satiation.

## 8. Worked example: two people, fear and desire, wired into a group, then nested

Everything here is derived from the definitions read in section 2 (VSL Definitions 2.9, 3.1, 4.2, 5.4). The example is mine, so it carries no citation. It was **checked by computer algebra and a numerical test**, noted at the end. The parameters (a, b, c, m) are placeholders for the kind of numbers an empirical drive model would estimate; nothing here is a claim about real people.

**Module (a person).** State `x = (F, D)` (fear, desire). Inputs `(u, s, w)`: `u` is the other person's displayed fear, `s` an environmental threat, `w` a reward cue. Output `y = F`, the displayed fear, a function of state only (as Definition 2.9 requires). Linear dynamics (so Definition 5.4 applies):

    dF/dt = −a F + c u + s          (fear decays at rate a, is raised by the other's display and by threat)
    dD/dt = −b D − m F + w          (desire decays at b, is suppressed by own fear at strength m, raised by reward)

Block form: `f^{S,S} = [[−a, 0], [−m, −b]]`, `f^{S,X} = [[c, 1, 0], [0, 0, 1]]` (columns u, s, w), `f^{X,S} = [1, 0]`.

**Group of two.** Parallel product of two modules A and B (`⊕`, state `(F_A, D_A, F_B, D_B)`, block-diagonal), then a wiring diagram Φ: inner inputs `(u_A, s_A, w_A, u_B, s_B, w_B)`, outer inputs `(s_A, w_A, s_B, w_B)`, outer outputs `(y_A, y_B)`, with `ϕ` sending `y_B → u_A`, `y_A → u_B`, and the outer inputs straight through to the threat and reward slots. No passing wires (the outer outputs come from inner outputs).

  **Validation correction (2026-10-29): as written this is not a VSL wiring diagram.** VSL Definition 3.1 requires ϕ to be a *bijection*, and Remark 3.7 says this "prohibits ... split ports". Here each inner output y_A feeds both u_B and the outer output y_A, so ϕ is not injective. The VSL-conformant version gives each module **two output ports**, `y = F` and `y' = F` (both readouts of the state, which Definition 2.9 allows), sends y' to the partner's u and y to the outer box. The resulting matrices are identical to those below, so the arithmetic stands; only the claim that the sketch as drawn satisfies Definition 3.1 was wrong. Myers' lens-based wiring diagrams (section 3) allow copying directly. The formula `g^{S,S} = f^{S,X} ϕ^{X,X} f^{X,S} + f^{S,S}` gives, in the coordinates `(F_A, D_A, F_B, D_B)`:

    [ −a   0    c   0 ]
    [ −m  −b    0   0 ]
    [  c   0   −a   0 ]
    [  0   0   −m  −b ]

i.e. exactly `dF_A = −aF_A + cF_B + s_A`, `dD_A = −bD_A − mF_A + w_A`, and the mirror for B. A symbolic comparison of the formula's output with equations written by hand returned equality.

**What the composite law tells you, and what it does not.**

- Eigenvalues of the composite: `−a + c`, `−a − c`, `−b` (twice). So the group of two is stable iff `|c| < a` (and b > 0); with c ≥ 0, as in the check script, that is `c < a`. That condition mixes a member parameter (a) with a coupling parameter (c): **it is not a function of the interface alone.** The framework delivered the group's matrix; the stability condition came from linear algebra on it, as a theorem about *this* family.
- The same condition is the **small-gain** condition [standard account, not read this session]: the open-loop DC gain from `u` to `y` of one module is `c/a`; the loop gain of two modules wired back to back is `(c/a)²`; it is less than 1 exactly when `|c| < a`. This is the place where a certificate calculus (D027, D030) would hook into the wiring diagram: stability of a composite from *gain certificates* of the parts and a condition on the wiring, without recomputing eigenvalues. Whether that composes in the general nonlinear case is the open question those directions test.
- **Non-reciprocal wiring** is in-framework. If A is raised by B's fear with gain `c_A` and B responds with gain `c_B` (opposite signs allowed: pursuit and avoidance), the 2×2 fear block is `[[−a, c_A],[c_B, −a]]` with eigenvalues `−a ± sqrt(c_A c_B)` (symbolic check). For `c_A c_B < 0` these are complex: the group **oscillates** even though each person alone decays monotonically. A symmetric (reciprocal) network of the Baez-Fong kind cannot produce this, because its form is symmetric. That is a concrete reason to prefer the directed wiring law for social drives.
- The **other three laws** would say different things about the same scene. Under section 6's law, a pooled variable (say group morale M) shared by both people would be obtained by identifying the two M terminals and **summing** the two people's contributions to dM/dt. Under 7a, the same group would be an overlay of two single-vertex networks plus the edge A-B. Under 7c, the same scene as a game would give a best-response relation on choices, with no F or D.

**Nesting (the operad law, checked).** A pair is itself a box with inputs `(s_A, w_A, s_B, w_B)` and outputs `(y_A, y_B)`. Two pairs wired together at the next level (an extra tie: pair 1's `y_B` added into pair 2's `s_A`) give a group of four. **Validation caveat:** *adding* a signal into an input that is also fed from outside merges two wires into one port, which VSL's bijective ϕ forbids, and the copy of `y_B` used for the tie is a split. So the nested test is a test of the general lens form (Myers: passback `w♯` an arbitrary map, here a sum), not of a VSL wiring diagram; the VSL-conformant version would give person A of pair 2 an extra input port for the tie and each person a spare output port. Associativity of the operad (Definition 2.1.2, law 2) says the result equals the flat four-person wiring. This was tested for a **nonlinear** version of the module (`dF/dt = −aF + c tanh(u) + s`, `dD/dt = −bD − mF² + w`, so algebra G rather than L) on 1,000 random states and inputs: the nested system's vector field and readout agreed with the flat wiring's to the floating-point maximum difference of exactly 0 in the test. What this verifies is the implementation of the substitution formula (the shape of Definition 4.2, generalised to lenses that copy and sum), not a case of Proposition 4.5 as stated; for the VSL-conformant variant above the theorem itself is Proposition 4.5. The script was re-run in validation: symbolic equality True, eigenvalues as stated, nested-versus-flat maximum difference 0.

**Reproducibility.** The check script is in the session scratchpad, `/tmp/claude-1000/-home-aldred-projects-social-algebra/1d268f6c-6f44-5e18-a974-0045d46feb88/scratchpad/work/chk.py` (not committed; sympy and numpy via `uv run --with`). It can be re-created from the equations above.

## 9. What exists vs what does not

**Exists (proved, [read]):**

- A law for building a group's dynamics from members' dynamics plus a wiring, closed under nesting (VSL Proposition 4.5; Myers chapter 1, draft). Linear case reduces to one matrix formula. Directed, allows non-reciprocal influence, requires readout without feedthrough.
- A law for gluing systems along shared variables with vector fields added (Baez-Pollard Theorem 17), with a hypergraph-category structure and a proved functor to steady-state relations (Theorem 23).
- A group-forming law for static networks (network models), with explicit overlay of the group's own ties.
- A compositional account of strategic interaction with a backward utility channel (open games), at the cost of fixing the solution concept.
- A repair of the decorated-cospan foundations (Baez-Courser-Vasilakopoulou), and a proof that open dynamical systems need the decorated, not the structured, form.

**Does not exist (not found, within what was read):**

- Any application of these frameworks to **drives** or **human groups** beyond motivating sentences (Spivak 2013 on Minsky and people; Myers on a fear anecdote). This repeats and confirms the finding of file 14.
- Any theorem in these sources deriving **stability, convergence or boundedness of the composite** from the members. Baez-Pollard explicitly sidesteps multiplicity of steady states.
- A **time-varying wiring** (relationships that form and break during the run) or **membership change** within the dynamical framework. Static ϕ only. (Libkind et al. and Myers' later chapters may extend this: D026, D031.)
- A semantic algebra with **thresholds, switching, or stochastic** drive dynamics in the VSL form (G is smooth ODEs). Myers' chapter 2 covers possibilistic and stochastic systems (heading and monad statements seen, not read).
- Any **non-reciprocal analogue of the Baez-Fong variational theorem.** The power-minimisation structure depends on symmetric Dirichlet forms and passivity.
- Any drive-like **state** in an open game; the game's preferences are fixed.

**What this means for the algebra (judgement, flagged).**

1. Use a **VSL/Myers-style directed wiring law** as the candidate for "group as a composite with an interface" because it is the one law in the set that naturally supports asymmetric influence, and the group's equation is *computed*, not postulated. Treat it as the **syntax** for composing drive equations.
2. Add Baez-Pollard's **variable-gluing with summed vector fields** for pooled quantities (morale, resources). They are two different laws, and both are proved, but they are not the same law and nobody in the sources read has put both in one calculus. (Libkind et al.'s "resource sharer" vs "machine" distinction in file 40 is the same split.)
3. Do not expect composition to *prove* anything about the dynamics by itself. Theorems about the group must come from a **certificate layer** on top (D027, D028, D030) or from **steady-state algebra** (Theorem 23).
4. The no-feedthrough rule means every drive must have a state. That forces a **fast variable** for reflexes (e.g. startle), a modelling consequence to be recorded in the algebra's definition.

## Unconfirmed

- Fong thesis (arXiv:1609.05382): only abstract, contents and chapter summaries read. Claims about controllability results (chapter 5) and the corelation theorem are **[from abstract]**.
- Spivak 2013 sections 3 to 5 (typed operad T, closed operads, recursion): not read beyond headings and the Rel extension statement.
- Seven Sketches (Fong and Spivak, CUP 2019, DOI 10.1017/9781108668804, Crossref-confirmed; arXiv:1803.05316v3): section 6.5 introduction and Definition 4.2 only. The co-design chapter (feasibility relations, section 4) may offer a "needs and capabilities" interface that was not explored here.
- Myers (2023-09-03 draft): chapters 3 to 6 not read; the chapter 5 heading "Steady states compose according to the laws of matrix arithmetic" is a heading only. Later releases may differ. The author discrepancy for Libkind et al. noted in file 40 is D026's and was not touched.
- The small-gain statement in section 8 is from the standard control-theory account, not read in any source this session; D027 should check it against Sontag or Jiang-Teel-Praly.
- Whether Baez-Foley-Moeller-Pollard operads have been combined with dynamical algebras by anyone: not found; not searched beyond the files read.
- Libkind and Myers 2025, "Towards a double operadic theory of systems" (arXiv:2505.18329): authorship and title confirmed from the arXiv API in validation (Sophie Libkind, David Jaz Myers; no Baez); not opened. An earlier line here wrongly read "Baez and Libkind-Myers".
- The Fong-Rapisarda-Sobocinski LICS 2016 paper (DOI 10.1145/2933575.2934556, Crossref-confirmed) was returned by a title search for Fong's thesis; it was not read and not used.

## Validation log (2026-10-29)

Method: every DOI resolved at api.crossref.org (title, authors, venue, volume, pages matched); every arXiv source re-downloaded and re-read with `pdftotext` at the cited definitions and quotations; Myers' draft re-fetched from davidjaz.com (dated 3 September 2023, confirmed); section 8's `chk.py` re-run.

- ✎ Spivak 2013, arXiv:1305.0297: existence, author, Definitions 2.1.2, 2.2.1, Examples 2.1.7, 2.2.10, Minsky and "4-ary relation" passages confirmed; corrected: the extension of Rel to T is Lemma 4.1.2, not Proposition 4.3.1 (which is the join-semilattice lift); Conjecture 3.1.6 restated in its formal form (quotient-free).
- ✓ Vagner-Spivak-Lerman, TAC 30 (2015) 1793-1822, DOI 10.70930/tac/7tz1nkbd: Definitions 2.9, 3.1, 3.8, 4.2, 5.4, Remarks 2.12, 3.7, Example 4.1 (tank equations), Propositions 3.11, 4.5, 5.5 all match; grep for stability/equilibrium/Lipschitz/existence returns nothing, as claimed.
- ✎ Myers, Categorical Systems Theory draft (2023-09-03): date, "work in progress ... Use at your own peril!", Definitions 1.2.1.2, 1.2.2.1, 1.3.1.1, 1.3.1.2, snake passage, section 5.2 heading confirmed; corrected "Example 1.3.2.8" to Definition 1.3.2.8 (population-flow graph is 1.3.2.9) and recorded that the source prints `k_1 I` in the third component (apparent typo).
- ✓ Fong, "Decorated cospans", TAC 30(33) (2015) 1096-1120, DOI 10.70930/tac/8cw8rvm2: Definition 3.1, Proposition 3.2 composite, Remark 3.3 quote, Theorem 3.4, section 5 Q(ψ) and the Frobenius quote match.
- ✓ Fong thesis, arXiv:1609.05382: exists; abstract (decorated corelations construct all hypergraph categories) and chapter 5 "Controllability" section confirmed; still abstract-level only, as stated.
- ✎ Baez-Fong, TAC 33 (2018) 1158-1222, DOI 10.70930/tac/zdyktmkc: Theorem 1.1, Definition 7.6, Theorem 7.7, black-boxing quote confirmed; corrected a misplaced factor of two in the power formula and made the "passive components" quote verbatim.
- ✓ Baez-Pollard, Rev. Math. Phys. 29(9) 1750028 (2017), DOI 10.1142/S0129055X17500283: Definitions 13, 14, Lemmas 15, 16, Theorems 17, 18, 23, "sidesteps", "None of his results subsume ours" and the Feinberg/Horn deficiency passage confirmed.
- ✓ Baez-Foley-Moeller-Pollard, TAC 35 (2020) 700-744, DOI 10.70930/tac/e0rrdvk5: Definition 2, Theorem 3 (twelve equations), Theorem 49, Example 53 formula, search-and-rescue motivation confirmed.
- ✓ Baez-Courser, TAC 35 (2020) 1771-1822, DOI 10.70930/tac/dca3obx4: abstract matches.
- ✓ Baez-Courser-Vasilakopoulou, Compositionality 4, 3 (2022), DOI 10.32408/compositionality-4-3: "many applications ... were flawed", the graph-decoration explanation, Theorems 3.1, 4.1, the "appear to be necessary" quote and the no-left-adjoint argument (it sits in section 6.4, "Petri nets with rates") confirmed; the epidemiology mention is in BCV's abstract.
- ✎ Ghani-Hedges-Winschel-Zahn, LICS 2018 pp. 472-481, DOI 10.1145/3209108.3209165: Definitions 3, 9, Theorem 1, conclusions confirmed; corrected: no Theorem 3 exists, examples are prisoner's dilemma/matching pennies etc. not "duopoly", coutility quote made verbatim, Theorem 1 is "monoidal ... moreover symmetric".
- ✓ Fong-Spivak, *An Invitation to Applied Category Theory* (CUP 2019), DOI 10.1017/9781108668804 (Crossref title is the published title; arXiv:1803.05316 is "Seven Sketches in Compositionality"): section 6.5 "passing wires" quote and Definition 4.2 (feasibility relation) confirmed.
- ✓ Libkind-Myers, arXiv:2505.18329: title and authors confirmed via arXiv API; corrected "Baez and Libkind-Myers" in Unconfirmed. Not read.
- ✓ Fong-Sobociński-Rapisarda, LICS 2016, DOI 10.1145/2933575.2934556: Crossref-confirmed (pp. 495-504); unused.
- ✎ Section 8 worked example (own work): algebra and numerics re-run and correct; stability condition corrected to `|c| < a`; the pair wiring splits outputs and the nested tie sums into an input, both outside VSL's bijective ϕ (Definition 3.1, Remark 3.7). Annotated in place with the conformant two-output-port version; matrices unchanged.
- ? "Nothing exists" claims (no application to drives or human groups; no combination of network-model operads with dynamical algebras; no non-reciprocal Baez-Fong analogue): could not be re-tested by web search in this pass (search budget exhausted); they stand as "not found within what was read", as the file already scopes them.

**Verdict.** The file is substantially accurate: all fourteen cited works exist with the stated authors, every DOI resolves to the right paper, and the transcribed definitions, formulas and quotations match the sources, with no fabrications found. The corrections are local: a misattributed Spivak result, a Myers definition misnumbered as an example, a factor-of-two slip in Baez-Fong, a phantom Theorem 3 and wrong example list in Ghani et al., a wrong co-author on the Libkind-Myers line, and, most substantive, the worked example's wiring violated the VSL bijection condition it claimed to follow (fixable without changing any result).

## Cross-checks (2026-10-29)

Method: grepped every other file in this directory for the works, authors, DOIs, equations and numbers used here. Overlaps are with files 14, 40 and 044; 071, 050, 054 and others matched only on name collisions (see the last item). Two primary-source checks were made: Crossref for the VSL volume and issue, and the arXiv PDF of Baez-Foley-Moeller-Pollard (1711.00037v4) for the network-model definitions.

**Agreements**

- **Vagner-Spivak-Lerman 2015** (this file section 2; file 40 section 1a; file 044 section 4). All three give TAC 30, pp. 1793-1822, DOI 10.70930/tac/7tz1nkbd, arXiv:1408.1598. All three scope it to continuous-time ODEs. File 044 section 4 and this file (section 0, section 2 "Theorems") both grepped the text for stability terms and found nothing relevant, so the shell gives functoriality and well-posedness, not stability. File 40 section 1 point 1 says the same ("says nothing about whether the composite is stable").
- **Baez-Fong 2018** (this file section 5; file 14 section 3b; file 044 section 3 and its cross-check list). Same citation (TAC 33, 1158-1222, DOI 10.70930/tac/zdyktmkc). File 044 section 3 agrees on the content: Graph(dQ) with Q the power functional, "do not produce energy", sources and nonlinear parts excluded, symmetric Dirichlet form. Conclusion agrees: a template for a proved composition law, a poor fit for non-reciprocal or driven coupling.
- **Ghani-Hedges-Winschel-Zahn 2018** (this file section 7c; file 40 section 2). Same venue, pages (LICS '18, pp. 472-481), DOI 10.1145/3209108.3209165 and arXiv:1603.04641v3. Same Definition 3 four-tuple (play, coplay, best response), same reading of coutility as the backward channel, and same cost (fixed utilities, argmax or Nash built in).
- **Network models** (this file section 7a; file 14 section 3c). Both cite Baez-Foley-Moeller-Pollard, TAC 35(20), 700-744 (2020), arXiv:1711.00037, and both describe the search-and-rescue motivation (boats, planes, drones) and the operad of networks of typed agents. Primary source check: file 14 says a network model is a lax symmetric monoidal functor into **Cat**, this file says F : S -> **Mon**. Both are right at different scopes: the paper's general definition is F : S(C) -> Cat (line 80 of the pdftotext output) and its Definition 2 for the one-coloured case is F : S -> Mon.
- **Fong 2015, thesis, Baez-Courser-Vasilakopoulou** (this file sections 4 and 7b; file 14 section 3b). File 14 says decorated cospans are "identify terminals, not A does something to B", which is this file's "identification, not signalling". File 14 notes BCV generalise decorations to pseudofunctors into Cat and a double category, matching this file's account of the correction, and its Petri-net remark is consistent with BCV section 6.4 ("Petri nets with rates").
- **Spivak 2013** (this file section 1; file 14 section 3a, file 04). Same arXiv ID 1305.0297, preprint only, and both note the Minsky *Society of Mind* motivation and the human/machine remark that is not developed.
- **"Nothing applied to drives or human groups"** (this file sections 0 and 9; file 14 final lists; file 40 section 1 closing paragraph and Unconfirmed). All three report no application of operads, wiring diagrams or open games to human groups or drives. File 40's open-games search found only the Capucci et al. agency paper.
- **Small gain** (this file section 8; file 044 cross-check and section 6 item 1; file 40 section 5). File 044 states that this file's linear loop gain (c/a)^2 < 1 iff |c| < a is the linear special case of gamma1 o gamma2 < id (Jiang-Teel-Praly 1994, DOI 10.1007/bf01211469). Both treat the statement as standard account, not read at source. This file's Unconfirmed note ("D027 should check it") is discharged only at that level.
- **Certificates not supplied by the shell** (this file section 0 last paragraph; file 044 section 0 and section 4; file 40 section 1 point 2). All agree that stability needs a separate certificate layer, and that the Capucci-Myers 2026 preprint (file 044) is the first piece fastening ISS certificates to the shell, cascade case only. This file's section 0 pointer to D027, D028 and D030 is consistent with that. Nothing in this file contradicts 044's finding that passivity and contraction remain open.
- **Myers, Categorical Systems Theory draft** (this file section 3; file 40 section 1c). Same draft (3 Sept 2023, davidjaz.com, "work in progress ... Use at your own peril!"), no DOI, not peer reviewed, same Libkind-Myers arXiv:2505.18329 (authors and title confirmed, not read). Both describe wiring as composition with a lens.

**Contradictions**

- None found that affect a claim of fact. Items for the record:
  - **VSL issue number.** File 14 section 3 (validation list) gives TAC 30(51); this file gives volume and pages only. Crossref returns volume 30, pages 1793-1822 and no issue field, so the issue could not be confirmed from the primary record. Verdict: no conflict with this file; issue 51 is unresolved.
  - **Myers chapter layout.** This file says chapters 3 to 6 cover behaviours, double categories, steady-state matrices and doctrines, with "doctrine (chapter 6)". File 40 section 1c cites Def. 3.5.0.4 (systems theory), Def. 3.5.2.1 (Euc) and Thm. 5.3.2.1 and calls the doctrine material part of its reading of Chapters 1-3 and 5. These are not strictly incompatible (a systems-theory chapter and a doctrines chapter can both exist) but they were not reconciled against the PDF in this pass. Verdict: unresolved. Neither file's claims rest on it, and this file already says chapters 3 to 6 were not read.
  - **Myers Def. 3.5.2.1 versus Def. 1.2.2.1.** File 40 uses Def. 3.5.2.1 for the Euclidean differential theory and this file uses Def. 1.2.2.1 for a differential system. They are different definitions (a systems theory versus a single differential system), so there is no contradiction.
  - **Name collision, not an overlap.** File 071 cites Pollard (2011) on alarm signals (Kimberly A. Pollard, *Behav. Ecol.*). This file's Pollard is Brendan S. Pollard (Baez-Pollard 2017; Baez-Foley-Moeller-Pollard 2020). Different people and fields. Likewise "Myers" in files 07, 24, 054 and 067 (Myerson, Myers and Lamm, Myers J.) is unrelated to D. J. Myers.
