# Prior work 40: the mathematics that could make drive equations compose

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: the mathematical frameworks in which a system built by gluing smaller systems inherits its properties from the parts. Context: Aldred's aim, "an algebra which expresses basic human drives and group drives, which we can compose into equations, which we can then use to start making theorems". Files 16, 19 (drive equations), 20 (dyads), 23 (collective dynamics, mean-field games) say what the equations are; this file is about the glue.

**Cross-references, not repeated.** File 14 §3 covers operads, wiring diagrams and decorated cospans in outline (Spivak, Fong, Baez-Courser); this file goes into what they give to *dynamics* and adds Myers' and Libkind's work. File 04 covers logics, DEL, bigraphs; file 23 covers mean-field games, potential games, Kuramoto and consensus (Olfati-Saber, Altafini), so those are only pointed at here.

**Method and honesty note.** Read at source this session: Vagner-Spivak-Lerman (abstract and introduction, arXiv PDF); Ghani et al. open games (Definition 3 and the introduction, arXiv PDF); Libkind et al. (abstract and metadata, arXiv PDF); Myers' book draft (preface, Definition 3.5.2.1 and the statement of the compositionality theorem, from the 3 Sept 2023 PDF). Everything else is `[from abstract]` (abstract or search-result summary seen this session) or `[standard account]` (textbook knowledge, not re-checked here; state theorems as the field states them and verify against the primary before building on them). DOIs were resolved through the Crossref API by title/author search; each DOI below was returned by Crossref for the stated title and year. Books without DOIs say so.

**Summary.** Two quite different things can "compose", and the literature splits cleanly on them.

1. **Structure composes by construction.** Categorical systems theory (Vagner-Spivak-Lerman, Myers, Libkind) gives a precise answer to "what does it mean to build a system from parts": components have interfaces, wiring patterns connect interfaces, and the whole is a function of the parts and the pattern, with laws (nesting commutes, simulation commutes). It is the best candidate for the algebra's *composition operator*. It says nothing about whether the composite is stable or does anything sensible.
2. **Properties compose only under certificates.** Stability of a composite does not follow from stability of the parts (switching and feedback break it). What does follow is: if each part carries a certificate of a particular kind (passivity or dissipativity with a storage function, an input-to-state gain, a contraction metric, monotonicity) and the wiring satisfies a stated condition (symmetric graph, loop gain below one, series/hierarchical structure), then the whole inherits a property. This is the only place in this cluster where "theorems about a group follow from properties of its members" is actually available, and it is control theory, not category theory.

The algebra therefore wants both: a categorical shell for the wiring and a certificate calculus inside it. No one has joined them for passivity or contraction in a general form that I could confirm (see Unconfirmed). A search for applications of categorical systems theory or open games to motivation, emotion or drives found nothing; the nearest hit was a critique that open games lack a notion of player agency. The ground is open, and that cuts both ways: no prior art to lean on and no one has shown it works.

*Validation correction (2026-10-29):* the "agency" paper is not a critique but a fix (Capucci, Ghani, Ledent, Nordvall Forsberg, "Translating extensive form games to open games with agency", *EPTCS* 372 (2022) 221-234, DOI 10.4204/EPTCS.372.16, arXiv:2105.06763). And "nothing applied to social dynamics" is too strong for contraction: contraction has been applied to **opinion dynamics** (e.g. Ofir, Ovseevich, Margaliot, "Contraction and k-contraction in Lurie systems with applications to networked systems", *Automatica* 159 (2024) 111341, DOI 10.1016/j.automatica.2023.111341, with a nonlinear opinion-model example; Wankhede, Mandal, Martínez, Tallapragada, arXiv:2404.04912, 2024, contraction for utility-maximising opinion agents), and control-theoretic network tools are surveyed for social networks in Proskurnikov & Tempo (2017/2018, *Annual Reviews in Control* 43, 65-79, DOI 10.1016/j.arcontrol.2017.03.002; Part II 45, 166-190, DOI 10.1016/j.arcontrol.2018.03.005). The validation search still found no application of passivity, port-Hamiltonian or operadic composition to **drives, motivation or emotion** specifically. Nearest compositional-agent work: St Clere Smithe, *Mathematical Foundations for a Compositional Account of the Bayesian Brain* (DPhil thesis, arXiv:2212.12538), categorical but about inference, not drives.

---

## 1. Categorical systems theory: wiring diagrams and systems theories

### 1a. Vagner, Spivak & Lerman (2015)

**Citation.** Vagner, D., Spivak, D. I., Lerman, E. (2015). Algebras of open dynamical systems on the operad of wiring diagrams. *Theory and Applications of Categories* 30, 1793-1822 (volume and pages confirmed via Crossref in validation). DOI 10.70930/tac/7tz1nkbd. arXiv:1408.1598 `[read]` (abstract and introduction). Scope note: VSL treat **continuous-time** systems (ODEs) only; discrete-time (Moore-machine) algebras on wiring diagrams appear in Myers (§1c) and Libkind et al. (§1b).

**Their vocabulary.** Black box with input and output ports; wiring diagram; operad **O_W** whose objects are boxes and whose morphisms are wiring diagrams; W-algebra; internal state controlled by inputs, producing outputs.

**Drives/operands.** None; the example is tanks connected by pipes. The operands are *open dynamical systems*: a state space, an input port type, an output port type, a dynamics ẋ = f(x, u), and a readout y = r(x).

**Operators / equations.** `[read]` abstract: they define a symmetric monoidal category W, build an operad O_W whose morphisms are wiring diagrams ("the algebraic rules for interconnection"), and define two O_W-algebras: **G** (general systems of differential equations "in which an internal state is controlled by inputs and produces outputs") and **L** (linear systems). The operator is *wiring-diagram application*: an algebra assigns to each box type a set of systems and to each wiring diagram a function composing systems into one. Operad laws: wiring diagrams themselves compose (a diagram of diagrams is a diagram), and the algebra respects that, so nested construction and flat construction agree. This is the "hierarchy" property.

**Theorems or derived predictions.** The theorem is that G and L *are* O_W-algebras, i.e. that interconnection is associative and unital at the level of ODEs, so that, in the abstract's words ("at different levels of granularity", Vagner, Spivak, Lerman 2015), a tank system and its sub-assemblies are related by algebraic equations. It is a well-definedness theorem. It predicts no behaviour.

**Empirical standing.** Pure mathematics; tank/fluid example only. Nothing empirical to assess.

**Operand/operator translation.** *Operand*: a drive module with an interface (what it reads: percept, other people's acts, other drives' output; what it exposes: urge, act). *Operator*: wiring a set of modules into a bigger module; a person = a wiring of drive modules, a dyad = a wiring of two persons, a group = a wiring of N persons, and these are all the *same operator*. That unification of levels is what Aldred's "person, two people, group built by gluing" needs and it is the reason to adopt this shell. **Gives**: one composition operator with associativity and nesting laws for free; levels (drive, person, dyad, group) as nested wirings. **Costs**: you must declare the interface of each drive (what is a "port" for curiosity?), and you must decide whether acts are signals on wires (continuous) or events (see §7, §3); the framework is mute on both.

### 1b. Libkind et al. (2022), operadic modelling and AlgebraicDynamics

**Citation.** Libkind, S., Baas, A., Patterson, E., Fairbanks, J. (2022). Operadic modeling of dynamical systems: mathematics and computation. *Electronic Proceedings in Theoretical Computer Science* 372 (ACT 2021), pp. 192-206 (Crossref-confirmed). DOI 10.4204/eptcs.372.14. arXiv:2105.12282 `[read]` (abstract and author list). Four authors, confirmed by arXiv and Crossref. (The brief's fifth author, Halter, belongs to the *Phil. Trans.* epidemic paper below, which has five authors: Libkind, Baas, Halter, Patterson, Fairbanks.)

**Their vocabulary.** Operad of wiring diagrams; "resource sharer" (undirected composition: systems share variables, as in Willems' interconnection), "machine" (directed, input-output); C-sets (copresheaves) to present the operads; functoriality of Euler's method.

**Operators / equations.** `[read]` abstract: they "reformulate some existing operads of wiring diagrams, add new ones, and describe them with C-sets", treat dynamical systems as algebras of these operads, and show "Euler's method is functorial for undirected systems, extending an earlier result for directed systems". Operationally: a discrete-time simulation of the composed system equals the composition of the discrete-time simulations of the parts. Implementation in Julia on Catlab.

**AlgebraicDynamics.jl.** `[read]` (GitHub README): "a library for compositional dynamical systems", built on Catlab.jl, composition "follows the mathematics of operads and operad algebras", MIT licence, 336 commits, 18 open issues, 14 open PRs at the time of the fetch; the README fetched did not show mechanisms, example systems, or a release date. The documentation does include a worked Lotka-Volterra example ("Lotka-Volterra Three Ways", confirmed in validation); latest tagged release v0.2.2 (31 Oct 2023). **This is the one place in the cluster where composition is executable today**: a drive model written as resource sharers could be simulated by gluing.

**Theorems / empirical standing.** Functoriality of Euler is a correctness theorem for the numerics. Used on epidemic models (Libkind, Baas, Halter, Patterson, Fairbanks 2022, "An algebraic framework for structured epidemic modelling", *Phil. Trans. R. Soc. A* 380(2233), DOI 10.1098/rsta.2021.0309, `[Crossref metadata only]`). No behavioural science.

**Translation.** Resource-sharer composition is the *symmetric* gluing a dyad needs (two people share a "joint situation" variable; neither is cause of the other). Directed machine composition is the one-way influence (a leader's act enters a follower). **Gives**: an executable semantics for the algebra's equations and a test bench: if the algebra's laws are right, simulation of the glued system must match. **Costs**: Julia/Catlab dependency; every model must be an ODE or difference equation with states in R^n (thresholds and discrete modes are outside the basic case).

### 1c. Myers, *Categorical Systems Theory* (book draft)

**Citation.** Myers, D. J. *Categorical Systems Theory.* Draft, last updated 3 Sept 2023, hosted at davidjaz.com/Papers/DynamicalBook.pdf `[read]` (preface; Chapters 1-3 and 5 headings and statements). Not on arXiv, no DOI, not peer reviewed (the preface says "a work in progress... Use at your own peril"). Related: Libkind & Myers, "Towards a double operadic theory of systems", arXiv:2505.18329 (2025; existence and authors confirmed via the arXiv API; no DOI, journal status unconfirmed). **Peer-reviewed anchor for the compositionality theorem** (added in validation): Myers, D. J. (2021). Double categories of open dynamical systems (extended abstract). *EPTCS* 333 (ACT 2020), 154-167, DOI 10.4204/EPTCS.333.11, arXiv:2005.05956 `[from abstract]`: the main theorem constructs covariantly representable indexed double functors to spans, so that "trajectories, steady states, and periodic orbits compose according to the laws of matrix arithmetic". **Priority**: the steady-state case was first shown by Spivak, "The steady states of coupled dynamical systems compose according to matrix arithmetic", arXiv:1512.00802 (2015) `[title only]`; credit Spivak for that idea and Myers for the general version.

**Their vocabulary.** Interface (arena); composition pattern (wiring diagram, lens); **doctrine** of dynamical systems; **systems theory** (a "theory of dynamical systems": an indexed category plus a section, `[read]` Def. 3.5.0.4); behaviour; chart of a behaviour; parameter-setting doctrine.

**Operators / equations.** `[read]` Def. 3.5.2.1: the Euclidean differential systems theory **Euc**: tangent of R^n is R^n, T f(p, v) = Df_p · v, so that a system is a differential equation ṡ = f(s, i) with readout. Variants in the book: deterministic (discrete time, "Moore machine" style), differential, and non-deterministic/stochastic theories (Markov decision processes appear in Chapters 1-2). Composition is wiring-pattern application; behaviours (trajectory, fixed point, periodic orbit) are themselves systems that map into the system, and so compose.

**Theorems.** `[read]` preface, informal statement of the **main compositionality theorem** (Ch. 5): behaviours of a composite can be computed from behaviours of the parts and the wiring pattern; nesting wiring patterns commutes with finding behaviours; composing behaviours with charts is associative. Formally: a representable lax doubly indexed functor (Thm. 5.3.2.1 in the draft; theorem number not re-checked in validation because the PDF host was unreachable). Applies in every systems theory and every doctrine. Note "lax": the theorem supplies comparison maps between the composite of the parts' behaviours and the composite's behaviours; whether those maps are isomorphisms (so that *every* behaviour of the group arises from compatible behaviours of members) is not settled by the word "lax" and was not checked in validation. Read the draft before relying on an equality.

**Empirical standing.** None; draft textbook. Quality of the mathematics is not in question; completeness and stability of the draft are.

**Translation.** This is the principal candidate for the algebra's *definition of a model*. **Gives**: (i) one theory of systems with discrete, continuous and stochastic variants, which bears directly on the open Q4 (is a drive level discrete or real): the algebra could state laws once and instantiate them in more than one systems theory; (ii) a general theorem that *fixed points, orbits and trajectories of the group are computed from those of the members under the wiring*, which is precisely "predict the group's steady states from the members' steady states", at the price of solving the compatibility (the charts must agree on shared wires). **Costs**: it gives existence and construction of behaviours, not their *stability or basin*; a heavy categorical apparatus (double categories, lax indexed functors) to learn; the book is a draft.

**Blunt on all of §1.** The categorical shell is syntax with correct bookkeeping. If the drive equations inside are wrong, the shell composes wrong equations flawlessly. And everything it proves is "how composites relate to parts", never "composite X is stable".

---

## 2. Compositional game theory: open games

**Citation.** Ghani, N., Hedges, J., Winschel, V., Zahn, P. (2018). Compositional game theory. *Proc. 33rd Annual ACM/IEEE Symposium on Logic in Computer Science (LICS '18)*, pp. 472-481 (Crossref-confirmed). DOI 10.1145/3209108.3209165. arXiv:1603.04641v3 `[read]` (introduction, selection functions, Definition 3).

**Their vocabulary.** Open game; play; coplay; **coutility** (value a game passes back to its environment); selection function; best response; strategy profile; contextual composition.

**Operators / equations.** `[read]` Definition 3: an open game G : (X, S) → (Y, R) is a 4-tuple (Σ_G, P_G, C_G, B_G): a set of strategy profiles Σ_G; a **play** function P_G : Σ_G × X → Y (observation to move); a **coplay** function C_G : Σ_G × X × R → S (utility to coutility, the backward flow); and a **best response** function B_G : X × (Y → R) → Rel(Σ_G), where Rel(Σ_G) is the meet-semilattice of endo-relations on Σ_G. X is observations, Y moves, R utilities, S coutilities. Selection functions δ_i : (X_i → R) → P(X_i) are the predecessor idea; with arg max they give Nash equilibria. Composition: sequential (the first game's move becomes the second's observation, the second's coutility becomes the first's utility), parallel (simultaneous), and a string-diagram graphical syntax. The central claim `[read]` is that "the equilibria of larger games should be defined from the equilibria of the component games" and that open games achieve this.

**Theorems.** Open games form a symmetric monoidal category (morphisms taken up to the paper's equivalence of open games), so sequential and parallel composition are associative and unital. What composes is the **best-response function in context**, not the equilibrium set in isolation: a profile of the composite is an equilibrium in a context iff each component's profile is a best response in the context *induced* for it by the other components (for sequential composition, the second game's context depends on the first game's play). So "equilibria of the whole from equilibria of the parts" holds only in this contextual sense; a component's equilibria computed against a fixed, unrelated context do not suffice. (I read the claim, not the proofs.) Standard games (normal form, extensive form with perfect information) embed faithfully in the sense of the same Nash equilibria and off-equilibrium best responses (abstract `[read]`).

**Empirical standing.** Economic models; the authors' own examples (auctions, a Bayesian game). Game-theoretic equilibrium predictions of human behaviour are themselves weak at the individual level (see files 21, 12); open games inherit this and add none.

Follow-ons with DOIs (Crossref-confirmed titles, `[from title/search only]`): Hedges, "Morphisms of open games", *ENTCS* 341 (2018), DOI 10.1016/j.entcs.2018.11.008; Ghani, Kupke, Lambert, Nordvall Forsberg, probabilistic/mixed strategies, *EPTCS* 323 (2020) 95-105, DOI 10.4204/eptcs.323.7; Bolt, Hedges, Zahn, "Bayesian open games", *Compositionality* 5 (2023), DOI 10.32408/compositionality-5-9; Capucci, Gavranović, Hedges, Rischel, "Towards foundations of categorical cybernetics", *EPTCS* 372 (2022), DOI 10.4204/eptcs.372.17 (open games, lenses, learners and backpropagation as one family: parametrised bidirectional processes; it is the bridge to learning agents, cf. Fong-Spivak-Tuyéras "Backprop as functor", DOI 10.1109/lics.2019.8785665).

**Translation.** *Operand*: an "agent-in-context" with observation, choice, utility, and a backward channel. A drive can be the **selection function** (what the agent argmaxes) or the **utility** R: "fear" reshapes R, "curiosity" adds a term. Coutility is a clean place for *what one person's act costs or gives the other*, i.e. social preferences (file 21). **Gives**: composition of *choices* with equilibrium predictions, in the same graphical syntax as §1. **Costs**: it presupposes utilities and argmax selection (one-shot rational choice), which is the very assumption the drive literature (files 16-17) is trying to replace; time is a sequence of games, not continuous dynamics; there is no built-in notion of state evolving through drive reduction. Best read as the *action-selection layer* on top of §1's dynamics, not a replacement.

---

## 3. Port-Hamiltonian systems and power-preserving interconnection

**Citation.** van der Schaft, A., Jeltsema, D. (2014). Port-Hamiltonian systems theory: an introductory overview. *Foundations and Trends in Systems and Control* 1(2-3), 173-378. DOI 10.1561/2600000002 (authors, volume and pages Crossref-confirmed in validation). Background: van der Schaft, *L2-Gain and Passivity Techniques in Nonlinear Control* (Springer; 2nd ed. 2000, DOI 10.1007/978-1-4471-0507-7; 3rd ed. 2017, chapter "Dissipative Systems Theory" DOI 10.1007/978-3-319-49992-5_3). Origins: Maschke, van der Schaft, Breedveld (1992), "An intrinsic Hamiltonian formulation of network dynamics", *J. Franklin Inst.* 329, 923-966, DOI 10.1016/s0016-0032(92)90049-m, and (1995) *IEEE TCAS-I* 42, 73-82, DOI 10.1109/81.372847 (Dirac structures for LC circuits). **Credit for the interconnection theorem**: Cervera, van der Schaft, Baños (2007), "Interconnection of port-Hamiltonian systems and composition of Dirac structures", *Automatica* 43, 212-225, DOI 10.1016/j.automatica.2006.08.014 (Crossref-confirmed; not read).

**Their vocabulary.** Port; effort and flow variables (conjugate pair whose product is power); Hamiltonian H (stored energy); **Dirac structure** (the power-conserving interconnection law); structure matrix J; dissipation R; passive.

**Operators / equations `[standard account]`.** Input-state-output port-Hamiltonian system: ẋ = [J(x) − R(x)] ∇H(x) + G(x) u, y = G(x)ᵀ ∇H(x), with J = −Jᵀ (interconnection, energy-conserving), R = Rᵀ ≥ 0 (dissipation). Energy balance: dH/dt = −∇Hᵀ R ∇H + yᵀ u ≤ yᵀ u, i.e. the system is **passive** with storage H. **Interconnection** through ports by a power-conserving Dirac structure: the composite is again port-Hamiltonian, with Hamiltonian the *sum* of the components' and structure given by the Dirac structure. So composition of such systems is closed, the sum rule is built in, and the composite is passive with storage ΣH_i.

**Theorems / derived predictions.** Closure under power-preserving interconnection; the composite's Hamiltonian is a Lyapunov candidate for free; stability follows at minima of H (energy shaping, Casimirs); passivity-based control (interconnect with a controller to shape H). All `[standard account]`.

**Empirical standing.** Engineering mainstay (mechanical, electrical, robotic systems); not applied to psychology as far as I found. The *form* of the claim is empirically falsifiable only if drive "energy" has a measurable meaning.

**Translation.** *Operand*: a drive as a port-system with a **storage function**: Hull-style "drive" D as a stored deficit, Keramati-Gutkin's drive function (distance of internal state from a setpoint, file 16) as H. File 16 reports that in Keramati-Gutkin reward is drive reduction; that is structurally a dissipation inequality: the storage drops when the agent acts effectively. *Operator*: power-preserving interconnection = "nothing gained or lost in transmission between persons". **Gives**: composition rules that automatically produce a Lyapunov function and a passivity certificate for any gluing, plus a ready vocabulary for *dissipation* (satiation, habituation, fatigue). **Costs**: the *links* are power-conserving (the Dirac structure transmits power without creating or destroying it); the *components* need not conserve anything (R ≥ 0 dissipates, and external ports may inject power). Between people there is no reason motivation is conserved in transmission: persuasion, contagion and provocation *amplify* at the link, which violates the power-preserving constraint unless the amplification is modelled as an explicit source port. Honest reading: take the **passivity/dissipation inequality** (§4), not the physics; note that passivity itself is weaker than port-Hamiltonian structure and does not assume conservation (see §4b). Also needs conjugate variable pairs (effort/flow); for a drive, what is the pair? Unresolved.

---

## 4. Willems: behavioural systems, and dissipativity

### 4a. Behavioural approach

**Citation.** Willems, J. C. (2007). The behavioral approach to open and interconnected systems. *IEEE Control Systems Magazine* 27(6), 46-99. DOI 10.1109/mcs.2007.906923 (volume, issue, pages 46-99 Crossref-confirmed; Crossref has no author field for this record, authorship from the article itself `[standard account]`). Also Willems (1991), Paradigms and puzzles in the theory of dynamical systems, *IEEE Trans. Automatic Control* 36(3), 259-294, DOI 10.1109/9.73561.

**Vocabulary and operators `[standard account]`.** A system is a **behaviour** B ⊆ W^T: the set of all trajectories of the manifest variables compatible with the laws. There is no input/output split by fiat. **Interconnection = variable sharing**: connecting two systems through shared variables w gives B₁ ∩ B₂ (intersection of behaviours on the shared variables); hidden variables are eliminated by projection. "Tearing, zooming, linking".

**Theorems.** Largely for linear time-invariant systems: elimination of latent variables, controllability as patching of trajectories, control as interconnection (a controller is another behaviour; "regular interconnection"). Little general nonlinear theory.

**Translation.** *Operator*: ∩ (conjunction of constraints) and ∃ (projection). This is the right algebra for **mutual** situations: a dyad is not "A drives B", it is a joint behaviour constrained by both people's laws. It lines up with relational/cylindric algebras (file 14 on relation algebra) and with resource sharers in §1b. **Gives**: composition without choosing causal direction; composite constraint sets can be empty (incompatibility = inconsistency = conflict) which is a clean *definition* of impossible co-existence of two sets of drive laws. **Costs**: it describes the set of possible trajectories, not which occurs or how likely; no probability; mostly linear theory.

### 4b. Dissipativity

**Citation.** Willems, J. C. (1972). Dissipative dynamical systems part I: general theory. *Archive for Rational Mechanics and Analysis* 45, 321-351. DOI 10.1007/bf00276493. Part II: linear systems with quadratic supply rate, same journal, 45, 352-393, DOI 10.1007/bf00276494. Hill, D. J., Moylan, P. J. (1976). The stability of nonlinear dissipative systems. *IEEE Trans. Automatic Control* 21(5), 708-711, DOI 10.1109/tac.1976.1101352. Zames, G. (1966). On the input-output stability of time-varying nonlinear feedback systems, Part I, *IEEE TAC* 11(2), 228-238, DOI 10.1109/tac.1966.1098316. Retrospective: Willems (2007), Dissipative dynamical systems, *European Journal of Control* 13(2-3), 134-151, DOI 10.3166/ejc.13.134-151. All pages above Crossref-confirmed in validation. Added in validation, for credit: Moylan, P. J., Hill, D. J. (1978). Stability criteria for large-scale systems. *IEEE TAC* 23(2), 143-149, DOI 10.1109/tac.1978.1101721 (the interconnection-of-dissipative-subsystems theorem); Sandberg, I. W. (1964). A frequency-domain condition for the stability of feedback systems containing a single time-varying nonlinear element. *Bell System Technical Journal* 43, 1601-1608, DOI 10.1002/j.1538-7305.1964.tb04100.x (small-gain, independently of Zames).

**Vocabulary.** Supply rate s(u, y); storage function V ≥ 0; dissipation inequality; available storage and required supply; passivity (s = uᵀy); finite L2-gain (s = γ²|u|² − |y|²).

**Equations `[standard account]`.** A system is **dissipative** w.r.t. supply rate s if there is V ≥ 0 with V(x(t₁)) − V(x(t₀)) ≤ ∫ s(u(t), y(t)) dt along all trajectories. Passive: s = uᵀy. Finite-gain: s = γ²‖u‖² − ‖y‖².

**Theorems (all `[standard account]`).**
- Interconnection: if systems 1 and 2 are dissipative with supply rates s₁, s₂ and the interconnection constraint gives s₁ + s₂ ≤ 0, then V₁ + V₂ is non-increasing along the closed loop; it is a Lyapunov function, and the equilibrium is Lyapunov stable, **provided V₁ + V₂ is positive definite** about the equilibrium (plus radial unboundedness for global, and a detectability/strictness condition for asymptotic stability). The N-subsystem version with a matrix condition on QSR supply rates is Moylan & Hill (1978).
- Passivity: the negative feedback interconnection of passive systems is passive (from the new external inputs to the outputs); parallel interconnection is passive too.
- Small gain (Zames 1966; Sandberg 1964): a feedback loop of finite-gain (input-output, e.g. L2) stable systems with γ₁γ₂ < 1 is finite-gain stable. This is input-output stability; the Lyapunov/state-space version is the ISS form in §5.
- **What passivity is and is not.** Passivity is the existence of a storage function V ≥ 0 with V̇ ≤ uᵀy, i.e. the system never *returns* more than it has been supplied plus what it started with. It does **not** assume conserved energy (dissipation is allowed and typical), and V need not be a physical energy. Systems with a *shortage* of passivity (output-feedback passivity index ρ < 0: V̇ ≤ uᵀy − ρ|y|²) model limited internal amplification and can still be interconnected stably if a neighbour has a matching excess.

**Translation.** This is the **certificate calculus**. *Operand*: each drive module or person carries a certificate (passive with storage V; or L2-gain ≤ γ). *Operator*: wiring; the theorem tells you, from the certificates and the wiring condition alone, whether the composite is stable. **Gives**: the form of theorem the strand wants, "if every member satisfies P and the network satisfies Q then the group satisfies R", with proofs that are short. Concretely: the loop-gain statement is the formal shape of **de-escalation**: if A's reactivity to B and B's to A multiply to < 1, the exchange is guaranteed to stay bounded. The converse is **not** a theorem: a product > 1 means only that the small-gain certificate fails, not that spirals occur (a negative-feedback loop with large gain can be stable, and other certificates may exist). Instability from gain > 1 follows only in special cases, e.g. a linear *positive*-feedback (mutually reinforcing) loop, where loop gain above 1 at zero frequency does give divergence. *(Validation correction: the original said "> 1: no stability certificate exists, and spirals are expected", which overstated a sufficient condition as a necessary one.)* **Costs**: the certificates are sufficient, not necessary, so failing the test proves nothing about the real system; gains must be measured or estimated for real people; strict passivity forbids net internal amplification, so strongly amplifying agents need the gain version or passivity indices, not plain passivity.

### 4c. Group coordination from member passivity

**Citation.** Arcak, M. (2007). Passivity as a design tool for group coordination. *IEEE Trans. Automatic Control* 52(8), 1380-1390 (Crossref-confirmed). DOI 10.1109/tac.2007.902733. Book: Bai, H., Arcak, M., Wen, J. (2011), *Cooperative Control Design: A Systematic, Passivity-Based Approach*, Springer, chapter "Passivity as a design tool for cooperative control", pp. 19-49, DOI 10.1007/978-1-4614-0014-1_2.

**`[from abstract/search]`** *(Validation note: the paper's abstract is not openly available; the text summarised here matches Arcak's Feb 2007 GRASP seminar abstract of the same work, not the published abstract.)* The goal is to steer *differences* between agent outputs to a prescribed set by distributed feedback; "when information flows bidirectionally between neighbours, the passivity properties of the individual components guarantee network stability". Design starts by requiring each agent to be strictly passive with a radially unbounded storage function; the symmetric interconnection structure is preserved by the design. Robust to time-varying topology.

**Translation.** **The single most on-target result for "group theorem from member properties".** *Operand*: agents that are passive. *Operator*: symmetric (reciprocal) coupling on a graph. Result: coordination of the whole. **Costs**: relies on **reciprocity** (undirected, "bidirectional" information flow); one-way influence (a leader, a demagogue, a broadcaster) breaks the symmetric structure, and then different tools (small-gain, §5) are needed. File 23 covers Olfati-Saber and Altafini consensus; Arcak is the passivity generalisation.

---

## 5. Input-to-state stability and small-gain theorems

**Citation.** Sontag, E. D. (1989). Smooth stabilization implies coprime factorization. *IEEE Trans. Automatic Control* 34(4), 435-443. DOI 10.1109/9.28018 (the ISS definition). Jiang, Z.-P., Teel, A. R., Praly, L. (1994). Small-gain theorem for ISS systems and applications. *Mathematics of Control, Signals and Systems* 7(2), 95-120. DOI 10.1007/bf01211469. (Pages Crossref-confirmed.) Added in validation: Jiang, Mareels, Wang (1996), "A Lyapunov formulation of the nonlinear small-gain theorem for interconnected ISS systems", *Automatica* 32, 1211-1215, DOI 10.1016/0005-1098(96)00051-9; and, for **N agents** rather than two, Dashkovskiy, Rüffer, Wirth (2007), "An ISS small gain theorem for general networks", *Math. Control Signals Systems* 19, 93-122, DOI 10.1007/s00498-007-0014-8 (the gain matrix Γ must satisfy a "no cycle amplifies" condition Γ(s) ≱ s; the group-level version this strand would actually use).

**Equations `[standard account]`.** ISS: |x(t)| ≤ β(|x₀|, t) + γ(‖u‖_∞), β a class-KL function, γ class-K. Cascade of ISS systems is ISS; feedback interconnection of ISS systems with gain functions γ₁, γ₂ is ISS (Jiang-Teel-Praly 1994) if γ₁(γ₂(s)) < s for all s > 0 (nonlinear small-gain condition; the cascade result is Sontag's).

**Translation.** ISS is the nonlinear, state-space, non-passivity version of the gain certificate in §4b, and the **cascade property** is the one for hierarchies (leader to followers, organisation chart, parent to child). **Gives**: a bounded-response theorem: a person (or group) whose drive state is ISS w.r.t. external provocation has a response bounded by a gain function of the provocation plus a forgetting term; the nonlinear gain function can encode saturation of a drive. **Costs**: same as §4: sufficient only; gain functions have to be obtained from data, and for individual people data of that quality is not available (file 27).

---

## 6. Contraction theory and network contraction

**Citation.** Lohmiller, W., Slotine, J.-J. E. (1998). On contraction analysis for non-linear systems. *Automatica* 34(6), 683-696. DOI 10.1016/s0005-1098(98)00019-3. Slotine, J.-J. E. (2003). Modular stability tools for distributed computation and control. *Int. J. Adaptive Control and Signal Processing* 17(6), 397-416, DOI 10.1002/acs.754. *(Validation correction: sole author Slotine, not "Slotine & Lohmiller 2001/2003".)* Russo, G., di Bernardo, M., Sontag, E. D. (2013). A contraction approach to the hierarchical analysis and design of networked systems. *IEEE TAC* 58(5), 1328-1331 (a technical note), DOI 10.1109/tac.2012.2223355 (authors, order, pages Crossref-confirmed). Added: Wang, W., Slotine, J.-J. E. (2005). On partial contraction analysis for coupled nonlinear oscillators. *Biological Cybernetics* 92, 38-53, DOI 10.1007/s00422-004-0527-x (partial contraction: convergence to a subspace, i.e. synchronisation, without a unique trajectory). Russo, Di Bernardo, Sontag (2010). Global entrainment of transcriptional systems to periodic inputs. *PLoS Comput. Biol.* 6(4), DOI 10.1371/journal.pcbi.1000739 `[from search]`. Pham, Q.-C., Slotine, J.-J. E. (2007). Stable concurrent synchronization in dynamic system networks. *Neural Networks* 20, DOI 10.1016/j.neunet.2006.07.008 (Crossref confirmed title).

**Equations `[standard account]`.** For ẋ = f(x, t), with Jacobian J = ∂f/∂x: if there is a metric transform Θ(x, t) such that the symmetric part of (Θ̇ + ΘJ)Θ⁻¹ is uniformly negative definite (≤ −λ < 0), then all trajectories converge exponentially to one another at rate λ; the system **forgets its initial condition**. Combinations: parallel, hierarchical (series) and feedback combinations of contracting systems are contracting under stated conditions; these are already in Lohmiller & Slotine (1998, §3), with feedback requiring a bound on the coupling relative to the contraction rates (the skew-symmetric-coupling case is unconditional). Delayed and further modular combinations are in Slotine (2003). Lineage `[standard account, not checked]`: the idea that a negative-definite (symmetric part of the) Jacobian forces trajectories together predates 1998 (Lewis 1949; Demidovich 1961); Lohmiller-Slotine generalised it with the metric Θ. Network version: Russo et al. give conditions for networks whose nodes are contracting and whose interconnection is hierarchical.

**Collective application `[from abstract]` (Rutishauser, Douglas, Slotine 2011, *Neural Computation* 23(3), 735-773, DOI 10.1162/neco_a_00091; arXiv:1105.3106).** Cooperative-competitive **winner-take-all modules** coupled through shared inhibition; contraction theory gives parameter ranges where each module is stable in a high-gain regime and where modules "can be aggregated arbitrarily to form large stable networks"; also parameter ranges that are multistable and retain persistent activity.

**Theorems.** Exponential convergence to a unique trajectory; entrainment to periodic inputs (a contracting system driven by a periodic input converges to a periodic orbit of the same period); stability preserved under defined combinations.

**Empirical standing.** Engineering and neural-circuit models. No empirical test on human drives.

**Translation.** *Operand*: a drive module whose Jacobian is contracting in some metric. *Operators*: series, parallel, feedback combinations as in the modular paper. **Gives**: (i) a *compositional* stability theorem for modules, directly demonstrated for competition-by-shared-inhibition circuits, which is the neural form of the author's gloss, the most urgent drive wins (compare §9); (ii) *prediction*: a contracting person forgets history and settles to the same state under the same inputs, and a group of contracting members entrains to periodic social rhythms (work week, rituals); (iii) a **differential** notion of stability that does not need the equilibrium to be known in advance. **Costs**: contraction on the *whole* (connected, forward-invariant) state space means at most one attractor: all trajectories converge to one another, so an autonomous globally contracting system has at most one equilibrium. *(Validation precision: contraction is a property of a region; a system can be contracting on each of several disjoint invariant regions, one per attractor, so local contraction is compatible with multistability; it then says nothing about the boundaries between basins.)* Human drives with hysteresis, habits, and thresholds are *multistable*, so a globally contracting model is wrong for them in the regime where behaviour changes character; local contraction per basin, partial contraction (Wang & Slotine 2005) and k-contraction (Ofir-Ovseevich-Margaliot, used for opinion dynamics with multiple equilibria) extend, but that is more machinery. Use for the stable regime between switches, not across them.

---

## 7. Hybrid and switched systems

**Citation.** Liberzon, D. (2003). *Switching in Systems and Control.* Birkhäuser (Systems & Control: Foundations & Applications), DOI 10.1007/978-1-4612-0017-8. Liberzon, D., Morse, A. S. (1999). Basic problems in stability and design of switched systems. *IEEE Control Systems* 19(5), 59-70, DOI 10.1109/37.793443. Branicky, M. S. (1998). Multiple Lyapunov functions and other analysis tools for switched and hybrid systems. *IEEE TAC* 43(4), 475-482, DOI 10.1109/9.664150. Hespanha, J. P., Morse, A. S. (1999). Stability of switched systems with average dwell-time. *Proc. 38th IEEE CDC*, 2655-2660, DOI 10.1109/cdc.1999.831330 (added in validation). Dwell time itself is credited to Morse (1996, *IEEE TAC* 41(10), supervisory control of set-point controllers) `[standard account, DOI not checked]`. Goebel, R., Sanfelice, R. G., Teel, A. R. (2012). *Hybrid Dynamical Systems.* Princeton UP, DOI 10.1515/9781400842636.

**Equations `[standard account]`.** Switched system ẋ = f_σ(t)(x), σ piecewise-constant selecting one mode from a family; hybrid system with flow set C and jump set D: ẋ = f(x) on C, x⁺ = g(x) on D (Goebel et al.).

**Theorems `[standard account]`.**
- A switched system can be *unstable even if every mode is stable*; Liberzon-Morse pose three problems: stability under arbitrary switching, under constrained switching, and design of switching.
- Sufficient conditions: a **common Lyapunov function** for all modes (stability under arbitrary switching); **dwell time** (switching slow enough); **multiple Lyapunov functions** (Branicky: each mode's Lyapunov function decreases while that mode is active, and its values at the successive instants when that mode is switched *on* form a non-increasing sequence; *validation correction*: the original "must not increase at switching instants" was imprecise); Lie-algebraic condition (for linear modes all Hurwitz, a **solvable** Lie algebra generated by the mode matrices implies a common quadratic Lyapunov function, hence stability under arbitrary switching; commuting matrices are the simplest case) (Liberzon, Hespanha, Morse 1999, *Systems & Control Letters*, DOI 10.1016/s0167-6911(99)00012-2: "Stability of switched systems: a Lie-algebraic condition", Crossref confirmed).
- Hybrid invariance principles (Goebel et al.), and results for well-posedness, Zeno behaviour (infinitely many jumps in finite time).

**Translation.** *Operand*: a **mode** (which drive currently governs action) together with the continuous states of all drives. *Operator*: threshold crossing triggers the jump x⁺ = g(x) (Hull's reaction threshold sLr, Lorenz-Tinbergen release thresholds, Atkinson-Birch switching, file 16, are all switching rules). **Gives**: the right setting for *threshold* drives and a ready-made list of theorems: dwell time in the algebra's vocabulary is a **refractory period** or **persistence**; stability under arbitrary switching needs a common Lyapunov function, i.e. a single dissipation measure all modes decrease (plausibly "homeostatic distance"), a testable structural claim. **Costs**: hybrid systems do not compose as nicely as ODEs (jump sets interact; Zeno), and most categorical frameworks of §1 treat only smooth dynamics (hybrid theories exist in the literature of hybrid-systems category theory but I did not verify one). Also dwell-time and threshold parameters are unobservable for individuals.

---

## 8. Monotone systems

**Citation.** Smith, H. L. (1995). *Monotone Dynamical Systems: An Introduction to the Theory of Competitive and Cooperative Systems.* AMS Mathematical Surveys and Monographs 41; chapter 3 "Competitive and cooperative differential equations", pp. 31-53, DOI 10.1090/surv/041/03 (Crossref dates the DOI record 2008; the book is 1995). **Credit for the convergence theorems** (added in validation): Hirsch, M. W. (1985). Systems of differential equations that are competitive or cooperative II: convergence almost everywhere. *SIAM J. Math. Anal.* 16, 423-439, DOI 10.1137/0516030; and Hirsch (1988), *J. reine angew. Math.* 383 (strongly monotone systems) `[standard account]`. Angeli, D., Sontag, E. D. (2003). Monotone control systems. *IEEE TAC* 48(10), 1684-1698. DOI 10.1109/tac.2003.817920. Positive feedback: Angeli, D., Sontag, E. D. (2004). Multi-stability in monotone input/output systems. *Systems & Control Letters* 51, 185-202, DOI 10.1016/j.sysconle.2003.08.003; Angeli, Ferrell, Sontag (2004), *PNAS* 101, 1822-1827, DOI 10.1073/pnas.0308265100.

**`[standard account]`.** A system is cooperative if the off-diagonal entries of its Jacobian are non-negative (no variable pushes another downward); competitive if they are non-positive. Cooperative systems preserve an order on initial conditions. For **strongly** cooperative systems (irreducible Jacobian) Hirsch proved that almost every bounded trajectory converges to the set of equilibria (generic convergence; convergence to a single equilibrium needs extra hypotheses, Smith 1995) and that there are no stable non-constant periodic orbits. Competitive systems do *not* share this: in dimension ≥ 3 they can have stable limit cycles. Angeli-Sontag extend to input-output monotone systems: a **negative feedback** loop of monotone systems converges globally if an associated one-dimensional discrete map has a globally attracting fixed point (Angeli & Sontag 2003), and a **positive feedback** loop's equilibria and their stability are read off the intersection of the characteristic curve with the diagonal, giving multistability (Angeli & Sontag 2004; Angeli, Ferrell & Sontag 2004).

**Translation.** Contagion (fear spreads, enthusiasm spreads; file 18) is cooperative coupling; competition for the same resource or attention (drive A suppresses drive B) is competitive coupling. **Gives**: structural theorems depending only on the *signs* of influence, which one can plausibly know without parameter values, a real advantage for a field where numbers are hard; "mixed" feedback loops of the monotone class are analysed with sign-pattern rules. **Costs**: signs only; breaks the moment the coupling changes sign with context (a person's fear amplifies a friend's alarm in one setting and calms them in another).

---

## 9. Winner-take-all, winnerless competition, and the max-plus algebra of urgency

### 9a. Winnerless competition

**Citation.** Rabinovich, M., Volkovskii, A., Lecanda, P., Huerta, R., Abarbanel, H. D. I., Laurent, G. (2001). Dynamical encoding by networks of competing neuron groups: winnerless competition. *Physical Review Letters* 87, 068102. DOI 10.1103/physrevlett.87.068102 (six authors in this order Crossref-confirmed). Review: Rabinovich, M. I., Varona, P., Selverston, A. I., Abarbanel, H. D. I. (2006). Dynamical principles in neuroscience. *Reviews of Modern Physics* 78(4), 1213-1265, DOI 10.1103/revmodphys.78.1213. **Credit for heteroclinic cycling in Lotka-Volterra competition** (added in validation): May, R. M., Leonard, W. J. (1975). Nonlinear aspects of competition between three species. *SIAM J. Appl. Math.* 29, 243-253, DOI 10.1137/0129022; the "stable heteroclinic channel" term is from later Rabinovich-group papers `[standard account]`.

**`[standard account]`.** Generalised Lotka-Volterra: ẋ_i = x_i (σ_i − Σ_j ρ_ij x_j). With asymmetric inhibition one gets a **stable heteroclinic channel**: the state visits saddle points in sequence, each competitor wins in turn (the standard account of winnerless competition, Rabinovich et al. 2001 and later work), with no final winner. Sequences are reproducible and robust to noise, yet sensitive to inputs.

**Translation.** For drives: the pattern "hunger, then curiosity, then affiliation" as a stable cyclic sequence without a global winner; the model is the right structure for **rotation among drives** and for rock-paper-scissors (non-transitive) dominance among people. **Costs**: no empirical test on drives; Lotka-Volterra is a neural-population idealisation.

### 9b. Max-plus (tropical) algebra

**Citation.** Cuninghame-Green, R. A. (1979). *Minimax Algebra.* Lecture Notes in Economics and Mathematical Systems 166, Springer, DOI 10.1007/978-3-642-48708-8. Baccelli, F., Cohen, G., Olsder, G. J., Quadrat, J.-P. (1992). *Synchronization and Linearity: An Algebra for Discrete Event Systems.* Wiley (no DOI found; Crossref returned only a 1994 book review, DOI 10.2307/2583959, which I did not read). Heidergott, B., Olsder, G. J., van der Woude, J. (2005). *Max Plus at Work.* Princeton UP, DOI 10.1515/9781400865239. Butkovič, P. (2003). Max-algebra: the linear algebra of combinatorics? *Linear Algebra and its Applications* 367, 313-335, DOI 10.1016/s0024-3795(02)00655-9 (pages Crossref-confirmed). **Credit** (added in validation): the eigenproblem and steady-state growth rate first appear in Cuninghame-Green, R. A. (1962). Describing industrial processes with interference and approximating their steady-state behaviour. *Operational Research Quarterly* 13, 95-100, DOI 10.1057/jors.1962.10; the max-cycle-mean characterisation is usually credited jointly to Cuninghame-Green and Vorob'ev (1967) `[standard account]`; the **cyclicity theorem** (eventual periodicity) to Cohen, Dubois, Quadrat, Viot (1985), *IEEE TAC* 30(3), 210-220, DOI 10.1109/tac.1985.1103925.

**Equations `[standard account]`** *(wording of this paragraph may follow the Wikipedia articles "Max-plus algebra" and "Tropical semiring", CC BY-SA 4.0; derivation not verified, to be re-derived from Cuninghame-Green 1979, Cohen et al. 1985 and Heidergott et al. 2005)*. The semiring (ℝ ∪ {−∞}, ⊕ = max, ⊗ = +). A max-plus linear system: x_i(k+1) = max_j (A_ij + x_j(k)), i.e. x(k+1) = A ⊗ x(k). **Theorem (the analogue of Perron-Frobenius):** an irreducible matrix A has a unique max-plus eigenvalue λ(A) = the **maximum cycle mean** of the weighted precedence graph (maximum over directed cycles of total weight divided by length); the system grows at asymptotic rate λ (x_i(k)/k → λ for finite initial state), and after a transient it is periodic **up to that linear growth**: x(k+c) = λ^{⊗c} ⊗ x(k), i.e. x(k+c) = x(k) + cλ, with c the cyclicity of the critical graph (Cohen et al. 1985). The state is not literally periodic unless λ = 0. The critical cycles determine long-run behaviour. Composition: matrix products A ⊗ B = max_k (A_ik + B_kj) are the tropical wiring composition. The deformation link: softmax with temperature τ → 0, τ log Σ exp(x_i/τ) → max_i x_i (Maslov dequantisation), so max-plus is the zero-temperature limit of log-sum-exp "soft-argmax" selection used in neural and RL action-selection `[standard account]`.

**Translation.** *Operator*: ⊕ = max is exactly "most urgent drive wins"; ⊗ = + is accumulation along a chain (urgency plus delay, strength plus propagation). **Gives**: a *linear* algebra for argmax selection with an actual spectral theorem (the cycle mean) and an explicit composition product, so some group theorems become graph-algorithmic (the long-run period of a cyclic social process = its heaviest cycle); the temperature deformation connects the algebra to softmax/Boltzmann choice used in the RL models of file 19 and to mean-field games (file 23). **Costs**: a semiring, not a ring: max has no inverse, so there is no cancellation. Stated precisely *(validation correction; the original said inhibition, dissipation and negative influence are "not expressible")*: weights A_ij may be negative, so a negative *offset* is expressible, and λ < 0 gives decay, so dissipation is expressible; what is missing is **inhibition in the sense of non-monotone dependence**: every max-plus linear map (and every min-max-plus map) is order-preserving and additively homogeneous, so raising one input can never lower any output. "Drive A suppresses drive B" therefore needs an extension outside the monotone class (min-max-plus keeps monotonicity and loses the clean eigenvalue theorem in general); it describes timing/rate structure better than amplitude; and it is a *deterministic* idealisation of selection. I did not find max-plus applied to motivation. Treat as a candidate for the selection layer only.

---

## 10. Multi-objective optimisation, Pareto fronts, gradient systems

**Citation.** Marler, R. T., Arora, J. S. (2004). Survey of multi-objective optimization methods for engineering. *Structural and Multidisciplinary Optimization* 26, 369-395, DOI 10.1007/s00158-003-0368-6 (26(6), 369-395, Crossref-confirmed). Pareto and Edgeworth lineage `[standard account]`. Added in validation: Désidéri, J.-A. (2012). Multiple-gradient descent algorithm (MGDA) for multiobjective optimization. *Comptes Rendus Mathématique* 350, 313-318, DOI 10.1016/j.crma.2012.03.014.

**`[standard account]`.** Objectives f₁..f_k (one per drive, to be maximised); an act is **Pareto-optimal** if no other act improves one drive without worsening another; the set of such outcomes is the Pareto front. **Weighted-sum scalarisation** Σ w_i f_i with positive weights yields Pareto-optimal points, but can reach only points on the convex hull of the front: points on non-convex (concave-in-objective-space) stretches are unreachable for any weights; epsilon-constraint and goal programming recover them. Gradient dynamics ẋ = −∇V with V = Σ V_i: V is non-increasing, there are no non-constant periodic orbits, and bounded trajectories have ω-limit sets made of critical points (convergence to a single point needs more, e.g. isolated critical points or analytic V via Łojasiewicz). **Multiple-gradient descent** (Désidéri 2012) converges to Pareto-*stationary* points, which need not be Pareto-optimal without convexity. Non-reciprocal coupling adds a rotational part (Helmholtz-type decomposition of a vector field into gradient and solenoidal parts) producing cycles. Potential games (file 23, §9) are the case where the multi-agent field is a gradient.

**Translation.** *Operand*: a drive as an objective function over acts (or the drive's Lyapunov V_i). *Operator*: sum (potential, weighted sum) or Pareto aggregation. **Gives**: a precise, static statement of **internal conflict** (curiosity and fear have a Pareto front; the weights are the personality) and a theorem-friendly dynamic version (a sum of potentials has a Lyapunov function; reciprocal coupling keeps it gradient; asymmetric influence breaks it, which marks where cycles and chasing come from). **Costs**: the weights carry all the content, so the model is circular unless the weights are measured (file 27); static; "gradient" assumes drives are reciprocal and smooth.

---

## 11. Hypergraph dynamics (pointer only)

File 14 §1 covers hypergraph and simplicial dynamics (higher-order interaction: group actions are not sums of pairwise ones). For the present cluster the useful link is that a hyperedge is the natural *wiring pattern with more than two ports*: an operad (§1) generalises graphs to hyperedge-style composition natively, so hypergraph dynamics and wiring diagrams are two views of one thing. Whether stability certificates (§4-§6) extend to higher-order coupling, I did not find; consensus on hypergraphs exists in the network literature but is not verified here. Unconfirmed.

---

## What exists vs what does not

**Exists (and read, or confirmed to be real):**
- A rigorous theory of *building* systems from interfaces and wiring patterns, with laws (Vagner-Spivak-Lerman; Myers; Libkind), and executable code (AlgebraicDynamics.jl).
- A compositional theory of *choice* (open games), with arg max and Nash equilibria.
- A mature control-theory toolbox of composite-stability theorems keyed to member certificates: passivity and dissipativity, small-gain/ISS, contraction, monotonicity, switching conditions, with at least one directly relevant group result (Arcak: passive agents on a symmetric graph coordinate) and one on competition (WTA modules aggregate stably).
- An algebra of argmax selection with a spectral theorem (max-plus).

**Does not exist (as far as I found):**
- Any application of categorical systems theory, passivity, contraction or port-Hamiltonian composition to human drives, motivation or emotion. Validation searches also found none for drives/emotion; but contraction *has* been applied to opinion dynamics (see the correction under the Summary), so "nothing in social dynamics" would be overstated.
- Any general theorem that links the categorical shell to the certificate calculus: "dissipativity / contraction as a property that composes along wiring diagrams in the O_W sense" (see Unconfirmed). This is the gap the algebra could fill and the place a result would be new.
- A drive-interface convention (what the ports are, what the conjugate variables are).
- Empirical estimates of the gains, storage functions or contraction rates of human drive systems. The gain-product-below-one escalation statement is a *form* of theorem, not a measured fact.
- A hybrid-system version of the categorical composition that handles thresholds, which Aldred's fear/desire switching needs.

**Candidate architecture, for discussion only (not a decision):** a categorical shell for wiring (§1), drives as dissipative modules with a storage function that is the homeostatic distance (§3-§4, linking to file 16), selection by max (§9) or equilibrium (§2), stability claims taken from certificate theorems (§4-§6) for the smooth regime and from switching theorems (§7) across thresholds. Each item has a cost listed above; the biggest are (i) power-conserving links (port-Hamiltonian) and strict passivity versus amplification between people (passivity indices and gain certificates soften this; passivity itself does not assume conservation), (ii) global contraction versus multistability, (iii) max-plus monotonicity: no input can lower an output, so no inhibition, and (iv) the open interface question.

**Questions this raises for Aldred, not assumed:** whether drive levels are continuous (Q4, reopened); whether influence between people is reciprocal by default (decides passivity versus gain-based theorems); whether the algebra's first deliverable is composition laws (shell) or one stability theorem (certificate), since the literature supports doing the second inside the first only by hand.

---

## Unconfirmed (do not cite without checking)

*(Validation, 2026-10-29: all page numbers, the VSL volume, the Halter question, the LV example, van der Schaft-Jeltsema authorship and the Russo et al. author order are now resolved and removed from this list; see the log below.)*

- Myers draft's latest version and its theorem numbering (Thm. 5.3.2.1, Def. 3.5.2.1): the original author read the 3 Sept 2023 PDF; the validation pass could not reach davidjaz.com (TLS error). The draft's existence and title are confirmed by nLab and Topos Institute pages.
- Libkind & Myers (2025), arXiv:2505.18329: existence and authors confirmed; content not read.
- Arcak (2007): published abstract not openly available; the summary is from a seminar abstract of the same work. Exact assumptions (strictly passive agent blocks, undirected graph) are `[standard account]`.
- Slotine (2003) delayed/modular combination conditions and Russo et al. (2013) network conditions: not read.
- Rutishauser et al. (2011): abstract only.
- Baccelli-Cohen-Olsder-Quadrat (1992), Wiley: real (Crossref lists 1994 reviews of it, DOI 10.2307/2583959 and 10.1057/jors.1994.15), no DOI for the book itself.
- Maslov dequantisation / softmax-to-max-plus link: standard, not checked against a source.
- The existence of general dissipativity-along-wiring-diagram theorems: Baez & Fong, "A compositional framework for passive linear networks", *TAC* 33 (2018), 1158-1222, DOI 10.70930/tac/zdyktmkc (Crossref-confirmed) is the nearest I found (passive linear circuits as a category); I did not read it and do not claim it extends to nonlinear or psychological systems.
- A hybrid/threshold version of categorical composition: possible, not located.
- "Shared Protentions in Multi-Agent Active Inference" (Albarracin et al., *Entropy* 2024, DOI 10.3390/e26040303): surfaced by Crossref search on compositional active inference; not read, relevance to categorical composition unknown.

---

## Missing important work (added in validation)

- **Network small-gain for N agents**: Dashkovskiy, Rüffer, Wirth (2007), *MCSS* 19, 93-122, DOI 10.1007/s00498-007-0014-8. The two-system small-gain theorem in §5 does not cover a group; this does, and is the natural certificate for "no cycle of influence amplifies".
- **Interconnected dissipative subsystems**: Moylan & Hill (1978), *IEEE TAC* 23, 143-149, DOI 10.1109/tac.1978.1101721. The N-member version of the §4b interconnection theorem.
- **Compositional steady states / behaviours, peer-reviewed**: Spivak (2015), arXiv:1512.00802; Myers (2021), *EPTCS* 333, 154-167, DOI 10.4204/EPTCS.333.11.
- **Partial contraction (synchronisation)**: Wang & Slotine (2005), *Biol. Cybern.* 92, 38-53, DOI 10.1007/s00422-004-0527-x. The tool for "members converge to a shared state" without a unique trajectory.
- **Control-theoretic social-network dynamics**: Proskurnikov & Tempo, Parts I-II (2017-2018), *Annual Reviews in Control*, DOIs 10.1016/j.arcontrol.2017.03.002 and 10.1016/j.arcontrol.2018.03.005; contraction applied to opinion dynamics (Ofir-Ovseevich-Margaliot 2024, DOI 10.1016/j.automatica.2023.111341).
- **Open games with agency**: Capucci, Ghani, Ledent, Nordvall Forsberg (2022), *EPTCS* 372, 221-234, DOI 10.4204/EPTCS.372.16.
- **Monotone systems, primary credits**: Hirsch (1985), DOI 10.1137/0516030; Angeli & Sontag (2004), DOI 10.1016/j.sysconle.2003.08.003.
- **Max-plus primary credits**: Cuninghame-Green (1962), DOI 10.1057/jors.1962.10; Cohen, Dubois, Quadrat, Viot (1985), DOI 10.1109/tac.1985.1103925.
- **Port-Hamiltonian interconnection theorem**: Cervera, van der Schaft, Baños (2007), DOI 10.1016/j.automatica.2006.08.014.

## Validation log (2026-10-29)

Method: every DOI resolved through `api.crossref.org/works/<doi>`; every arXiv ID through the arXiv API; abstracts of VSL, Ghani et al. and Myers (2021) re-read; the mathematics checked against the standard statements.

- Vagner, Spivak, Lerman 2015 (TAC; arXiv:1408.1598): ✎ corrected (volume 30 / pp. 1793-1822 confirmed; continuous-time scope stated)
- Libkind, Baas, Patterson, Fairbanks 2022 (EPTCS 372; arXiv:2105.12282): ✎ corrected (pages confirmed; "Halter" discrepancy resolved: he is on the Phil. Trans. paper)
- Libkind, Baas, Halter, Patterson, Fairbanks 2022 (Phil. Trans. A): ✎ corrected (title, authors, volume added)
- AlgebraicDynamics.jl: ✎ corrected (Lotka-Volterra example confirmed; release v0.2.2)
- Myers, *Categorical Systems Theory* draft: ? unconfirmed (exists; PDF unreachable, theorem numbering unchecked; "lax" caveat added)
- Libkind & Myers 2025 (arXiv:2505.18329): ✎ corrected (was "DOI confirmed"; it has no DOI)
- Ghani, Hedges, Winschel, Zahn 2018 (LICS; arXiv:1603.04641): ✎ corrected (pages confirmed; compositionality restated as best-response-in-context, not equilibria in isolation)
- Hedges 2018 (ENTCS 341): ✓
- Ghani, Kupke, Lambert, Nordvall Forsberg 2020 (EPTCS 323): ✎ corrected (authors named)
- Bolt, Hedges, Zahn 2023 (Compositionality 5): ✓
- Capucci, Gavranović, Hedges, Rischel 2022 (EPTCS 372): ✓
- Fong, Spivak, Tuyéras 2019 (LICS): ✓
- van der Schaft & Jeltsema 2014 (FnT): ✎ corrected (second author and pages confirmed)
- van der Schaft, *L2-Gain and Passivity* (chapter DOI): ✎ corrected (edition clarified)
- Maschke, van der Schaft, Breedveld: ✎ corrected (1992 and 1995 papers now cited with DOIs)
- Willems 2007 (CSM): ✓ (pages confirmed)
- Willems 1991 (TAC): ✎ corrected (pages added)
- Willems 1972 I and II: ✓
- Hill & Moylan 1976: ✓
- Zames 1966: ✓ (Sandberg 1964 added as co-credit)
- Willems 2007 (EJC): ✓
- Arcak 2007 (TAC): ✎ corrected (pages confirmed; the "abstract" was a seminar abstract, flagged)
- Bai, Arcak, Wen 2011 (chapter): ✓
- Sontag 1989: ✓
- Jiang, Teel, Praly 1994: ✓ (condition written precisely: γ₁(γ₂(s)) < s for s > 0)
- Lohmiller & Slotine 1998: ✓ (combination results located in this paper)
- "Slotine & Lohmiller 2001/2003", modular stability tools: ✎ corrected (sole author Slotine, 2003, pp. 397-416)
- Russo, di Bernardo, Sontag 2013 (TAC): ✎ corrected (author order and pages confirmed; it is a technical note)
- Russo, di Bernardo, Sontag 2010 (PLoS CB): ✓
- Pham & Slotine 2007: ✓
- Rutishauser, Douglas, Slotine 2011: ✓ (DOI and arXiv confirmed; abstract only)
- Liberzon 2003: ✓
- Liberzon & Morse 1999: ✓
- Branicky 1998: ✎ corrected (multiple-Lyapunov condition stated precisely; pages added)
- Goebel, Sanfelice, Teel 2012: ✓
- Liberzon, Hespanha, Morse 1999: ✎ corrected ("commuting-ish" replaced by the solvable-Lie-algebra condition)
- Smith 1995 (MSM 41): ✎ corrected (book year 1995; DOI record dated 2008)
- Angeli & Sontag 2003: ✎ corrected (positive-feedback multistability credited to Angeli & Sontag 2004 / Angeli, Ferrell, Sontag 2004)
- Rabinovich et al. 2001 (PRL): ✓ (six authors confirmed)
- Rabinovich, Varona, Selverston, Abarbanel 2006: ✓
- Cuninghame-Green 1979: ✓ (1962 paper added for priority)
- Baccelli, Cohen, Olsder, Quadrat 1992: ? unconfirmed DOI (book real; no DOI)
- Heidergott, Olsder, van der Woude 2005: ✓
- Butkovič 2003: ✓
- Marler & Arora 2004: ✓
- Baez & Fong 2018 (TAC 33): ✓ (pages added)
- Albarracin et al. 2024 (Entropy): ✓ (exists; relevance still unknown)
- Mathematical claims: ✎ "loop gain > 1 ⇒ spirals expected" (sufficient condition misread as necessary); ✎ "contraction allows only one attractor" (true only for global contraction); ✎ "max-plus has no subtraction so no inhibition/dissipation" (negative weights and decay are expressible; the real limit is monotonicity); ✎ "passivity assumes conserved energy" (passivity is a dissipation inequality with a storage function; conservation is a property of port-Hamiltonian links only); ✎ max-plus "becomes periodic" (periodic up to linear growth); ✎ Hirsch generic convergence needs strong monotonicity; ✎ weighted-sum and gradient-flow statements tightened; ✎ "nothing applied" claim narrowed (contraction is applied to opinion dynamics; nothing found for drives/emotion).
- Fabrications: none found. ✗ removed: none.

**Verdict.** The bibliography is sound: every DOI and arXiv ID resolved to the stated work, and the "from memory" page numbers were all right. The errors were in the mathematics' *direction of implication* and in credit: the small-gain escalation reading turned a sufficient condition into a necessary one, contraction and max-plus limits were overstated, one paper had a phantom co-author, and several theorems were credited to follow-on rather than originating papers. Treat §1's categorical claims as reliable at the level of what is proved (well-definedness and compositionality of behaviours), and use the certificate theorems in §4-§6 only as sufficient conditions.

## Licences of quoted and transcribed material (2026-10-30)

No tables, figures or datasets are transcribed in this file. All quotations are short (under 25 words); equations are restated in our own notation. Licences were not checked per source, so publisher copyright is presumed unless stated.

| Source | Licence as determined | How used |
|---|---|---|
| Vagner, Spivak, Lerman 2015 (arXiv:1408.1598; TAC 30) | not determined; publisher copyright presumed (TAC is open access, licence not checked) | three short quotations from the abstract (under 25 words each); description of the construction |
| Libkind et al. 2022 (arXiv:2105.12282; EPTCS 372) | not determined; publisher copyright presumed (EPTCS is open access, licence not checked) | two short abstract quotations; description |
| AlgebraicDynamics.jl README | MIT (as stated in the README); README text not otherwise licensed here | two short phrases; description |
| Myers, Categorical Systems Theory draft | not determined; copyright presumed | restated definitions and theorem; one short phrase from the preface |
| Myers 2021 (EPTCS 333) | not determined; publisher copyright presumed | one short abstract quotation |
| Ghani, Hedges, Winschel, Zahn 2018 (arXiv:1603.04641) | not determined; publisher copyright presumed | one short quotation; Definition 3 restated, not copied |
| Arcak 2007 (IEEE TAC) | not determined; publisher copyright presumed. The 21-word quotation matches a seminar abstract whose licence is not stated; flagged "check" in the audit, text unchanged | one short quotation; paraphrase |
| Rutishauser, Douglas, Slotine 2011 | not determined; publisher copyright presumed | one short quotation (about 8 words) |
| Rabinovich et al. 2001 line of work | not determined; publisher copyright presumed | a five-word phrase, attributed in the text |
| Max-plus paragraph (section 9b) | possibly derived from Wikipedia ("Max-plus algebra", "Tropical semiring"), CC BY-SA 4.0 if so; marked in the text, unverified | restated equations and theorem statements |
| All other cited works (DOIs, titles, authors, page numbers) | facts and citations, free to use | citation only |
