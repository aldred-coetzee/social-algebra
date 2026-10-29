# Prior work 14: mathematical and computer-science structures for people, roles and groups

Date: 2026-10-29. Cluster: maths and CS formalisations, outside the cases other agents cover (role semigroups/blockmodels, kinship, modal/deontic/epistemic logics, bigraphs, sheaf opinion dynamics, ologs, opinion dynamics).

**Provenance rule.** Bibliographic facts (title, authors, venue, DOI/arXiv) below were confirmed this session by search or fetch; the source URL is given per entry. The algebraic descriptions (signatures, axioms) are the standard definitions as I know them; I fetched abstracts, not full texts, so treat any axiom as "check against the paper before relying". Where I could not confirm a source it is under "Unconfirmed" at the end.

## Summary

Nobody has built a single "algebra of people, roles and groups", but every ingredient exists as a mature, separately developed structure, mostly outside social science:

- **Carrier structures for operands** that are genuinely usable: the AGR/Aalaadin triple (agent, group, role) from multi-agent systems; the RBAC96/ANSI relational model (users, roles, permissions, with a role partial order); Wille's concept lattices (formal contexts of persons x attributes or persons x events; *validation note: no section below covers this; the social-network use is Freeman and White 1993, see "Missing work"*); hypergraphs/simplicial complexes (a group is a hyperedge/simplex). Of these, AGR is the only one that names agents, roles and groups as three distinct sorts (*validation correction: RBAC96 has users, roles, permissions and sessions; it has no group sort*).
- **Composition operators** that are genuinely algebraic: operads/wiring diagrams and decorated cospans (Spivak; Fong; Baez-Fong). These give a rigorous "put groups together into a bigger group, with interfaces" operation. Not applied to human *organisations as social structures*; the applications are circuits, databases, dynamical systems and engineered systems of systems. *Validation note:* the nearest are Baez, Foley, Moeller, Pollard's network-model operads (teams of heterogeneous agents, from a search-and-rescue case study) and compositional game theory (open games compose strategic interactions between players); see "Missing work".
- **Ontological accounts** of what a role and a group *are* (DOLCE roles; Ritchie's structuralism; W3C ORG) are good at deciding what the sorts should be, and give no operators.
- **Quantum-like social science** is not a literal algebra of persons; it is a probability/decision model for one agent's judgments. Do not adopt it as a carrier.

---

## 1. Higher-order networks: hypergraphs and simplicial complexes

### 1a. Battiston et al. 2020
- **Citation:** F. Battiston, G. Cencetti, I. Iacopini, V. Latora, M. Lucas, A. Patania, J.-G. Young, G. Petri, "Networks beyond pairwise interactions: structure and dynamics", *Physics Reports* 874, 1-92 (2020).
- **Verified:** https://arxiv.org/abs/2006.01764 ; DOI 10.1016/j.physrep.2020.05.004.
- **Their vocabulary:** higher-order interactions, group interactions, hyperedge, simplex, facet, clique complex, bipartite (incidence) representation, higher-order Laplacian, simplicial/hypergraph "contagion", "synchronization".
- **Operands:** nodes (units) and *groups of nodes of any size*, as hyperedges (arbitrary subsets of V) or simplices (subsets closed under taking subsets).
- **Operators / algebraic structure:** a hypergraph is H = (V, E) with E a subset of the power set P(V). A simplicial complex K is a downward-closed family of subsets (the axiom: sigma in K and tau subset of sigma implies tau in K). Algebra proper: incidence matrices B_k, boundary operators d_k with d_{k-1} d_k = 0, and higher-order (Hodge) Laplacians L_k = d_{k+1} d_{k+1}^T + d_k^T d_k acting on k-chains. Dynamics are defined by these operators. There is no composition law on groups themselves; "operators" here are linear maps on functions of simplices, not operations *by* people on one another. [from abstract/standard account]
- **What it captures:** that a group interaction is not reducible to the set of pairs in it; size-dependent effects (critical-mass thresholds, explosive transitions).
- **Limits:** groups are unlabelled subsets. No roles, no direction, no difference between "a chairs b, c, d" and "a, b, c, d meet". Simplicial closure forces every subgroup to be an interaction, which is false for committees. Hypergraphs lift that but lose the Hodge machinery.
- **Relevance:** the natural *membership layer* carrier: a group = element of P(V) with a set-algebra (union, intersection, containment) for free. Insufficient alone; combine with roles (see AGR, RBAC).

### 1b. Iacopini et al. 2019
- **Citation:** I. Iacopini, G. Petri, A. Barrat, V. Latora, "Simplicial models of social contagion", *Nature Communications* 10, 2485 (2019).
- **Verified:** https://arxiv.org/abs/1810.07031 ; DOI 10.1038/s41467-019-10431-6.
- **Vocabulary:** simplicial contagion, infection via 2-simplices (triangles) with rate beta_Delta in addition to pairwise rate beta, bistability, discontinuous transition.
- **Operands:** individuals with state S or I, group-of-three simplices.
- **Operators:** a stochastic update rule on a simplicial complex: a susceptible node becomes infected at a rate that sums a pairwise term and a term per triangle whose other two vertices are both infected; recovery at rate mu. No algebraic closure properties. [from abstract/standard account]
- **Captures:** social reinforcement (adoption needs more than one exposed neighbour), hence critical mass.
- **Limits:** a dynamics, not a notation; people differ only by state.
- **Relevance:** evidence that "group acts on member" must be a primitive, not derived from pairs. A concrete test case any social algebra should be able to express (an operator whose effect depends on the *group* it acts through).

### 1c. Lambiotte, Rosvall, Scholtes 2019; Bick et al. 2023 (supporting surveys)
- Lambiotte, Rosvall, Scholtes, "From networks to optimal higher-order models of complex systems", *Nature Physics* 15, 313-320 (2019). DOI 10.1038/s41567-019-0459-y ; preprint https://arxiv.org/abs/1806.05977. Argues that memory/path structure (higher-order Markov, not only hyperedges) is another route beyond pairs.
- Bick, Gross, Harrington, Schaub, "What are higher-order networks?", *SIAM Review* 65(3), 686-731 (2023). DOI 10.1137/21M1414024 ; https://arxiv.org/abs/2104.11329. Taxonomy of higher-order structures; useful as an index.

---

## 2. Multilayer / multiplex / temporal networks as tensors

- **Citation:** M. De Domenico, A. Sole-Ribalta, E. Cozzo, M. Kivela, Y. Moreno, M. A. Porter, S. Gomez, A. Arenas, "Mathematical formulation of multilayer networks", *Phys. Rev. X* 3, 041022 (2013).
- **Verified:** https://arxiv.org/abs/1307.4977 ; DOI 10.1103/PhysRevX.3.041022. Companion review: M. Kivela, A. Arenas, M. Barthelemy, J. P. Gleeson, Y. Moreno, M. A. Porter, "Multilayer networks", *J. Complex Networks* 2, 203-271 (2014), DOI 10.1093/comnet/cnu016, https://arxiv.org/abs/1309.7233.
- **Vocabulary:** layers, aspects, multilayer adjacency tensor, supra-adjacency matrix, multiplex, interlayer coupling.
- **Operands:** state nodes (node, layer) pairs; edges between them. Layers can index relation type (friend, colleague, kin) or time.
- **Operators / structure (standard, from the paper's framework; abstract confirmed, formulas not re-read):** a rank-4 adjacency tensor M with entries M^{i alpha}_{j beta} (node i in layer alpha to node j in layer beta), built from a tensor product of the vector spaces of nodes and layers, with Kronecker/tensor-contraction operations generalising degree, centrality, modularity and diffusion. Standard linear algebra (tensor product, contraction), no new axioms. [from abstract/standard account]
- **Captures:** several kinds of tie over the same people, and time, in one object; coupling across layers.
- **Limits:** edges are numeric weights; a tie type is a layer index, not an operator with composition. Layers do not compose (no "friend of colleague" calculus), groups are not first-class, roles are absent.
- **Relevance:** the **right way to represent "the same people under several relation types"**; a social algebra's relations-as-operators can be represented as *matrices on the person space*, with layers as a family of operators, which is exactly this tensor. Good as the *representation* of an algebra of relations, not the algebra itself.

---

## 3. Operads, wiring diagrams, decorated cospans

### 3a. Spivak 2013
- **Citation:** D. I. Spivak, "The operad of wiring diagrams: formalizing a graphical language for databases, recursion, and plug-and-play circuits", arXiv:1305.0297 [cs.DB] (2013). Preprint only on the page checked.
- **Verified:** https://arxiv.org/abs/1305.0297 (DOI 10.48550/arXiv.1305.0297).
- **Vocabulary:** boxes with input/output ports, wiring diagram, operad, plug-and-play.
- **Operands:** boxes (systems) with typed interfaces (finite sets of typed ports).
- **Operators and structure (standard):** colored operad W. Objects: interfaces. Operations: a wiring diagram with n inner boxes and one outer box, W(X_1,...,X_n; Y). Composition: nest diagrams inside inner boxes. Axioms: associativity of composition, unit identity wiring, equivariance under permuting inputs. Algebras of the operad assign to each box a set (e.g. behaviours) and to each diagram a function from the product of inner behaviours to outer behaviour. Related: Vagner, Spivak, Lerman, "Algebras of open dynamical systems on the operad of wiring diagrams" (surfaced in search; not fetched). [from abstract/standard account]
- **Captures:** compositionality: how a system built from parts presents one interface to the outside; hierarchical nesting.
- **Limits:** the wiring is *static and typed*; people-as-boxes would need to rewire as relationships change. No application to organisations found (search for one returned engineering uses only).
- **Relevance:** **strongest candidate for the group-formation operator**: "a group is the composite of members with its own external interface (the role it presents to other groups)". Operands = people or groups as boxes; composition = nesting groups in groups, giving the multi-level hierarchy for free. Does not specify what a person is.

### 3b. Fong 2015, Fong 2016, Baez-Fong 2018
- **Citations:** B. Fong, "Decorated cospans", *Theory and Applications of Categories* 30(33), 1096-1120 (2015), https://arxiv.org/abs/1502.00872. B. Fong, "The algebra of open and interconnected systems", DPhil thesis, Oxford, arXiv:1609.05382, https://arxiv.org/abs/1609.05382. J. C. Baez, B. Fong, "A compositional framework for passive linear networks", *Theory and Applications of Categories* 33(38), 1158-1222 (2018), https://arxiv.org/abs/1504.05625.
- **Vocabulary:** open system, cospan X -> N <- Y, decoration, hypergraph category (special commutative Frobenius monoid on every object), corelation, black-box functor.
- **Operands:** finite sets of terminals (interface) as objects; morphisms are open systems.
- **Operators and structure:** given a category C with finite colimits and a lax monoidal functor F : (C, +) -> (Set, x), objects of the new category are those of C and morphisms X -> Y are isomorphism classes of cospans X -> N <- Y with an element of F(N). Composition by pushout of cospans, decorations combined via F. Result: a symmetric monoidal category (hypergraph category) with the Frobenius structure (copy/merge/discard/create) on each object. A black-box functor forgets internals and keeps behaviour.
- **Captures:** gluing open systems at shared terminals; the "interconnection" operator is the pushout; behavioural semantics by functor.
- **Limits:** systems are physical/formal (circuits, Markov processes, reaction networks); the composition is "identify terminals", not "A does something to B". *Validation:* "Fong notes Petri nets as an instance" was not checked against the thesis; open Petri nets are treated in later work (Baez, Courser, Vasilakopoulou, "Structured versus decorated cospans", *Compositionality* 4 (2022), arXiv:2101.09363, which also generalises decorations to a pseudofunctor into Cat and gives a symmetric monoidal double category).
- **Relevance:** the hypergraph-category structure (*merge, copy, discard* on each object) is a very close match to what "people joining, splitting, leaving a group" do. Treat as the **ambient category**, not the carrier.

### 3c. Operads for design (context)
- Foley, Breiner, Subrahmanian, Dusel, "Operads for complex system design specification, analysis and synthesis", *Proc. R. Soc. A* 477 (2021), DOI 10.1098/rspa.2021.0099 ; https://arxiv.org/abs/2101.11115. Baez, Foley, "Operads for designing systems of systems", *Notices of the AMS* 68(6), 1005-1007 (2021), https://arxiv.org/abs/2009.12647. Both engineering.
- *Added in validation:* J. C. Baez, J. Foley, J. Moeller, B. Pollard, "Network models", *Theory and Applications of Categories* 35(20), 700-744 (2020), arXiv:1711.00037. A network model is a lax symmetric monoidal functor from a free symmetric monoidal category to Cat; each yields an operad whose operations build networks of typed agents (vertices = agents, edges = communication channels), from a search-and-rescue case study (boats, planes, drones). This is the nearest operadic treatment of *teams of agents*, still engineered, not social.
- Spivak 2013 itself motivates wiring diagrams with Minsky's *Society of Mind* and suggests extending to interactions among humans and machines, without developing it.
- Validation search (2026-10-29) also found **no operadic treatment of social organisations as such**. The gap stands, but narrowed: see compositional game theory under "Missing work".

---

## 4. Quantum-like social science

### 4a. Haven and Khrennikov, *Quantum Social Science* (2013)
- **Citation:** E. Haven, A. Khrennikov, *Quantum Social Science*, Cambridge University Press, 2013, ISBN 978-1-107-01282-0, 279 pp.
- **Verified:** Cambridge catalogue https://www.cambridge.org/core/books/quantum-social-science/preface/761E77E20744AF48B5DEF82460744895 (copyright page confirms 2013, ISBN).
- **Vocabulary:** quantum-like, state vector/density operator, observable, superposition, interference, contextuality, order effects, "mental state".
- **Operands:** the *mental state of one decision-maker or one market*, as a vector in a complex Hilbert space (or probability amplitudes).
- **Operators:** self-adjoint operators as questions/observables; projections; unitary evolution; measurement with state collapse (Luders rule). Algebra: the (non-commutative) operator algebra B(H); the non-commutativity of two projections models order effects in survey answers.
- **How literal is it?** Not literal about people. The books are explicit that "quantum-like" means the *mathematics* of quantum probability is used, with no claim that brains are quantum physical systems. The state is one agent's belief/judgment state, not a society. Applications covered: decision paradoxes, finance, economics, brain science.
- **Limits:** mostly one agent at a time; a population is modelled by a *product* or *mixture*, with no native roles or groups. The claim of unique explanatory power has been contested in open peer commentary (see 4b). *Validation correction:* not exclusively one-agent. Khrennikov's "social laser" programme (arXiv:1512.05386, 2015; Khrennikov, Alodjants, Trofimova, Tsarev, *Entropy* 20(12), 921, 2018) models a population of "social atoms" exchanging quanta of a social-information field, with creation and annihilation operators and Bose-Einstein statistics for bandwagon effects. Still no roles or groups as sorts, and heavily metaphorical, but it is a population-level operator formalism.
- **Relevance:** only one transferable idea: **order-dependence as non-commutativity** (answering a then b differs from b then a). That is a genuine algebraic fact a social algebra of "acts" may want (e.g. who is told first). The Hilbert-space carrier is not recommended for operands.

### 4b. Busemeyer and Bruza 2012; Pothos and Busemeyer 2013
- J. R. Busemeyer, P. D. Bruza, *Quantum Models of Cognition and Decision*, Cambridge University Press, 2012, DOI 10.1017/CBO9780511997716 (catalogue: https://resolve.cambridge.org/core/books/quantum-models-of-cognition-and-decision/75909428F710F7C6AF7D580CB83443AC). Uses entanglement for non-reductionist cognition models; again one-agent.
- E. M. Pothos, J. R. Busemeyer, "Can quantum probability provide a new direction for cognitive modeling?", *Behavioral and Brain Sciences* 36(3), 255-274 (2013), DOI 10.1017/s0140525x12001525. With open commentaries that dispute the stronger claims (e.g. Gelman and Betancourt).
- *Added in validation (from knowledge, not fetched):* Z. Wang, T. Solloway, R. M. Shiffrin, J. R. Busemeyer, "Context effects produced by question orders reveal quantum nature of human judgments", *PNAS* 111(26), 9431-9436 (2014). The "QQ equality", a parameter-free prediction of the non-commuting-projector model of question order effects, tested on 70 national surveys. This is the strongest empirical support for the one idea section 4a says is transferable, so cite it rather than the books for that point.

---

## 5. Role-based access control (RBAC) as a formal algebra

### 5a. Sandhu et al. 1996 (RBAC96 family)
- **Citation:** R. S. Sandhu, E. J. Coyne, H. L. Feinstein, C. E. Youman, "Role-Based Access Control Models", *IEEE Computer* 29(2), 38-47, Feb 1996.
- **Verified:** volume/pages confirmed across several sources (DOI 10.1109/2.485845 is the usual citation but was not confirmed by search; see Unconfirmed). Full text read in validation from NIST: https://csrc.nist.gov/csrc/media/projects/role-based-access-control/documents/sandhu96.pdf.
- **Vocabulary:** user, role, permission, session, role hierarchy, constraints (separation of duty), cardinality.
- **Operands (sorts):** U (users), R (roles), P (permissions), S (sessions).
- **Operators and structure (standard definition):** [read]
  - UA subset of U x R (user assignment), PA subset of P x R (permission assignment), many-to-many.
  - RH subset of R x R, a **partial order** (reflexive, antisymmetric, transitive) with r1 >= r2 meaning r1 inherits all permissions of r2; RBAC1.
  - session map user(s) in U, roles(s) subset of {r : exists r' >= r with (user(s), r') in UA}: a session may activate any role **junior** to (or equal to) a role the user is assigned. *Validation correction:* the survey had `r' <= r`, which would let a user activate roles *senior* to their own; checked against the paper's RBAC1 definition and its gloss "any combination of roles junior to those the user is a member of".
  - constraints (RBAC2): static/dynamic separation of duty (mutually exclusive roles), cardinality, prerequisite roles, as predicates over UA, PA and sessions; RBAC3 = RBAC1 + RBAC2 (the "consolidated model"). RBAC0 is the base (U, R, P, S, UA, PA, user, roles).
  - Authorisation: session s has the permissions of its roles and of every role junior to them: union over r in roles(s) of {p : exists r'' <= r with (p, r'') in PA}.
  - The paper also introduces **administrative roles and permissions** (who may change UA, PA, RH), developed as ARBAC97 (see 5d).
- **Captures:** the cleanest *existing* formal separation of person vs role vs capability, with an order on roles and constraints (mutual exclusion, cardinality).
- **Limits:** static assignment relations (no verbs between people); roles are *permission bundles*, not social positions; no group sort in the base model (groups appear in later extensions); no notion of one person acting on another.

### 5b. NIST proposal and ANSI/INCITS 359-2004
- **Citations:** D. F. Ferraiolo, R. Sandhu, S. Gavrila, D. R. Kuhn, R. Chandramouli, "Proposed NIST standard for role-based access control", *ACM Transactions on Information and System Security* 4(3), 224-274 (Aug 2001), DOI 10.1145/501978.501980 (venue confirmed in validation). ANSI/INCITS 359-2004 *Information Technology - Role Based Access Control*, effective 3 Feb 2004 (confirmed via https://xml.coverpages.org/ni2004-04-05-a.html and NIST page https://csrc.nist.gov/projects/role-based-access-control).
- **Structure:** Core RBAC, Hierarchical RBAC (general = arbitrary partial order; limited = each role has at most one immediate descendant, i.e. an inverted tree), Static Separation of Duty, Dynamic Separation of Duty. Standard defines **functional specification**: administrative commands (AddUser, DeleteUser, AssignUser, DeassignUser, GrantPermission, RevokePermission, AddInheritance, DeleteInheritance, CreateSsd/Dsd set, ...), review functions (AssignedUsers, AssignedRoles, AuthorizedUsers, ...), and system functions (CreateSession, AddActiveRole, CheckAccess). Each given as pre/post-conditions over the relation sets. [from abstract/standard account]
- **Relevance to an algebra:** the administrative commands are literally an **operator signature over a state of (U, R, P, UA, PA, RH)**: a small state-transition algebra. This is the closest existing thing to "operators that act on the structure of a group of people". It is about *managing* access, not social behaviour, but the pattern (state = sorted relational structure; operators = guarded updates; invariants = constraints) is directly reusable.

### 5c. Aside: lattice view
- Role hierarchy as a partial order, and dominance/lattice models of information flow underlie much RBAC theory: D. E. Denning, "A lattice model of secure information flow", *Communications of the ACM* 19(5), 236-243 (1976), DOI 10.1145/360051.360056 (confirmed in validation).

### 5d. ARBAC97 (added in validation, from knowledge; citation not fetched)
- R. Sandhu, V. Bhamidipati, Q. Munawer, "The ARBAC97 model for role-based administration of roles", *ACM TISSEC* 2(1), 105-135 (1999).
- Three sub-models: URA97 (user-role assignment), PRA97 (permission-role assignment), RRA97 (role-role, i.e. hierarchy, administration). Administrative roles are separate from regular roles; relations `can_assign(admin_role, prereq_condition, role_range)` and `can_revoke(admin_role, role_range)`, where the prerequisite condition is a Boolean expression over role membership and the range is an interval in the role hierarchy.
- **Relevance:** this is the clearest existing case of **operators whose application is itself governed by roles**: who may put whom into which role, conditional on what roles the target already holds. Directly the shape of "A appoints B to role r in group G", and a better template for guarded social operators than the ANSI command list alone.

---

## 6. Social-role ontologies and organisation vocabularies

### 6a. Masolo et al. 2004
- **Citation:** C. Masolo, L. Vieu, E. Bottazzi, C. Catenacci, R. Ferrario, A. Gangemi, N. Guarino, "Social roles and their descriptions", in *Principles of Knowledge Representation and Reasoning: Proceedings of KR 2004*, AAAI Press, pp. 267-277.
- **Verified:** https://istc.cnr.it/it/content/social-roles-and-their-descriptions (abstract). No free full text located.
- **Vocabulary:** social individual, social concept (reified), role, description (collectively accepted), context, DOLCE ("Descriptions and Situations" extension), anti-rigid, founded (depends on a relation to another entity).
- **Operands:** endurants (persons), social objects/roles as *concepts*, descriptions that define them.
- **Operators/structure:** a **first-order theory**, not an algebra. Roles are anti-rigid, dependent on a context (description). An entity "plays" a role (a ternary-like relation with time and context); a role is classified, not constituted, by the filler. Multiple fillers per role; one person multiple roles.
- **Captures:** the exact difference between a person (stable) and a role (contingent on a relation and a social convention); counts-as.
- **Limits:** no operators and no dynamics; purely definitional.
- **Relevance:** decides the sorts: *role is not a subtype of person and not a property of a person*; it is a relational entity with a defining description. Use it to settle what a role operand is.

### 6b. W3C ORG ontology
- **Citation:** D. Reynolds (ed.), "The Organization Ontology", W3C Recommendation, 16 January 2014 (Government Linked Data WG).
- **Verified:** search summary of the Recommendation and errata (https://www.w3.org/2011/gld/org-errata). Primary spec page not fetched.
- **Classes:** Organization, FormalOrganization, OrganizationalUnit, Membership, Role, Post, Site, ChangeEvent, OrganizationalCollaboration. **Key modelling move:** Membership is a reified n-ary relation (member, organization, role, period).
- **Limits:** a vocabulary (OWL/RDF), no operators. Errata note a modelling mistake: org:holds/org:heldBy were wrongly made sub-properties of memberOf/hasMember, i.e. confusing holding a post with being a member (confirmed in validation at https://www.w3.org/2001/sw/wiki/Org_Errata, erratum 1; fix: the sub-property axioms were removed).
- **Relevance:** a useful sanity check: reify membership as a ternary or quaternary relation (who, which group, in which role, when).

### 6c. Boella and van der Torre (roles in normative MAS)
- Search found the tutorial "Roles from Different Angles" (Boella, Hulstijn, van der Torre) and papers on counts-as and delegation of power (DEON 2006, LNCS 4048; PRIMA 2008). Their position, per snippets: roles carry powers and norms, several agents may enact one role, one agent several roles. Normative/deontic logic is covered by another agent.
- *Resolved in validation:* G. Boella, L. van der Torre, "The ontological properties of social roles in multi-agent systems: definitional dependence, powers and roles playing roles", *Artificial Intelligence and Law* 15(3), 201-221 (2007), DOI 10.1007/s10506-007-9030-8. Three properties: a role is defined inside the institution that defines it; it gives the agent playing it powers (e.g. to create commitments for the institution and other roles); roles can play roles. Formalised in input/output logic. Relevant: "roles play roles" is a recursion the AGR carrier does not allow.

### 6d. Ritchie, Uzquiano: what a group is
- **Ritchie:** K. Ritchie, "What are groups?", *Philosophical Studies* 166(2), 257-272 (2013). Argues four views (non-singular pluralities, fusions, aggregates, sets) each fail at least one of six adequacy criteria; proposes **groups as realisations of structures**: a structure's functionally defined nodes/places are occupied. (Confirmed via search summaries; https://diversityreadinglist.org/?p=3735.) *Validation addition:* Ritchie's later "Social structures and the ontology of social groups", *Philosophy and Phenomenological Research* 100(2) (2020), confirmed as existing, narrows this: only *organised* groups (her "Type 1", e.g. committees, teams) are realisations of structures; *feature* groups (her "Type 2", e.g. a race or gender group) are not. So the structure-plus-occupants carrier covers organised groups only (Type 1/Type 2 labels from knowledge, not fetched).
- **Uzquiano:** G. Uzquiano, "Groups: toward a theory of plural embodiment", *Journal of Philosophy* 115(8), 423-452 (2018), DOI 10.5840/jphil2018115825; https://research-repository.st-andrews.ac.uk/handle/10023/18222. A group at a time is just its members arranged in a complex condition.
- **Why it matters:** the *set* carrier fails: the same members can be two different groups; a group persists through changing membership; membership has no structure. Ritchie's structure-plus-occupants is precisely **(a graph/relational structure with typed slots) + (an assignment of persons to slots)**, i.e. the same shape as AGR and RBAC. Convergence of three independent traditions on one carrier shape.
- **Limits:** no operators; the philosophy defines identity conditions only.

---

## 7. Multi-agent organisation models

### 7a. AGR / Aalaadin (Ferber and Gutknecht) *highly relevant*
- **Citations:** J. Ferber, O. Gutknecht, "A meta-model for the analysis and design of organizations in multi-agent systems", *Proc. 3rd Int. Conf. on Multi-Agent Systems (ICMAS-98)*, Paris, 1998, pp. 128-135, IEEE Computer Society. J. Ferber, O. Gutknecht, F. Michel, "From agents to organizations: an organizational view of multi-agent systems", in *Agent-Oriented Software Engineering IV (AOSE 2003)*, LNCS 2935, Springer, pp. 214-230, DOI of volume 10.1007/b95187.
- **Verified:** AOSE 2003 pages 214-230 confirmed via DBLP https://dblp.org/pid/86/1212 and citing papers. *Validation correction:* the survey cited arXiv:1506.09032 (Abbas, Shaheen, Amin, "Organization of multi-agent systems: an overview", 2015) as confirming the AALAADIN/AGR relationship; its abstract does not mention AGR, so that citation is removed as evidence. The AGR = AALAADIN identity and "group as the basic unit of agent aggregation, each agent in one or more groups" are confirmed by later citing texts; the communication rule ("two agents can communicate only if they belong to the same group") is confirmed only by a truncated French thesis summary. The full text was not obtained in either pass (HAL returns 403); everything else below is from knowledge.
- **Vocabulary:** agent, group, role, group structure, organisational structure, "organisational reflection", OCMAS.
- **Operands (three sorts):** Agent (an active communicating entity, no constraint on internals), Group (an atomic set of agents, a context for interaction; an agent may belong to several groups; groups may overlap), Role (an abstract representation of a function/service/identity of an agent *within a group*). [from abstract/standard account]
- **Structure (standard):** roles are **local to a group** (a role "buyer" in group G1 is different from "buyer" in G2); an agent can hold several roles, in several groups; communication is only possible between agents sharing a group; group structure = set of roles + role cardinalities + a graph of allowed interactions between roles. Entering a group = requesting a role (group-manager role mediates). In the 2003 version, an organisation structure is the abstract description (roles, interaction graph), and an organisation is a structure plus its concrete agents, like Ritchie's realisation.
- **Operators:** the *primitives* are: create a group, join a group (acquire a role), leave a group, request/leave a role. These are stateful, guarded operations on the triple (A, G, R) and its membership relation. *Validation note:* the papers state these as a model, not as an operator algebra. The concrete operator names come from the MadKit platform API (createGroup, requestRole, leaveRole, leaveGroup, sendMessage), from knowledge and not checked. No composition laws or equations between them are defined.
- **Captures:** a precise, minimal sort system for exactly the problem set (people, roles, groups) with scoping rules (role-in-group), overlap, and a closure principle: communication through shared groups.
- **Limits:** no semantics for what agents *do to* one another beyond message passing; no dynamics of influence; no operator composition laws; groups are flat (the model is "atomic groups"; hierarchy only by agents belonging to groups at several levels); no norms (add MOISE/OperA).
- **Relevance:** **the best single candidate for the carrier structure.** Take (Agent, Group, Role) with role-local-to-group scoping and the join/leave/create operators; treat the interaction graph of a group structure as the place where social operators (relations on roles) live.

### 7b. OperA (Dignum)
- **Citation:** V. Dignum, "A model for organizational interaction: based on agents, founded in logic", PhD thesis, Utrecht University, awarded 12 January 2004 (SIKS; ISBN 90-393-3568-0).
- **Verified:** https://dspace.library.uu.nl/handle/1874/890; SIKS Dissertation Series 2004-1; supervisors J.-J. Meyer, F. Dignum, H. Weigand. (ISBN not re-checked.)
- **Structure (confirmed in validation from OperA papers, not the thesis text):** three models. The *organisational model* defines the society's roles, interaction structure (scenes/scripts), norms and communication. The *social model* populates it with agents through **social contracts** (commitments between an agent and the society about enacting a role). The *interaction model* records **interaction contracts** (commitments between role-enacting agents about how they will interact). Contracts are expressed in a deontic-temporal logic (LCR, from knowledge). [from abstract/standard account]
- **Relevance:** adds a contract layer (an agent *commits* to a role, and role-enactors commit to each other) on top of AGR-like structure. That makes commitments, not messages, the unit of social action, which links to Singh (see "Missing work").

---

## 8. Actors, Petri nets, process mining

### 8a. Hewitt's Actor model
- **Citation:** C. Hewitt, P. Bishop, R. Steiger, "A universal modular ACTOR formalism for artificial intelligence", *Proc. IJCAI-73*, pp. 235-245 (some records give 235-244).
- **Verified:** https://ijcai.org/proceedings/1973/31 ; PDF https://worrydream.com/refs/Hewitt_1973_-_A_Universal_Modular_Actor_Formalism_for_Artificial_Intelligence.pdf.
- **Operands:** actors, each with a mailbox/address. **Operators (standard):** on receiving a message an actor can (a) send messages to known actors, (b) create new actors, (c) designate how it will handle the next message (become). No shared state; asynchronous; message order not guaranteed. Agha's *Actors* (MIT Press, 1986) gives the operational semantics (I did not verify the catalogue entry beyond the MIT handle 1721.1/6952). [from abstract/standard account]
- **Captures:** "entities that do things to each other by sending messages, can create others, and change their own behaviour": three primitives, no more.
- **Limits:** no sort for group or role (those are patterns of address-knowledge); no social semantics.
- **Relevance:** a minimal operator signature for *person acts on person*: send(a, b, m), create(a), become(a, behaviour). Useful as a floor for the operator vocabulary; it is the formalism that treats "the people" as the only primitives.

### 8b. van der Aalst: social network mining from event logs
- **Citation:** W. M. P. van der Aalst, H. A. Reijers, M. Song, "Discovering social networks from event logs", *Computer Supported Cooperative Work* 14(6), 549-593 (2005), DOI 10.1007/s10606-005-9005-9; https://research.tue.nl/en/publications/discovering-social-networks-from-event-logs/ ; earlier: "Mining social networks: uncovering interaction patterns in business processes", BPM 2004, LNCS 3080, pp. 244-260.
- **Vocabulary:** originator, handover of work, subcontracting, working together, similar tasks, MiSoN tool.
- **Operands:** persons/originators and activities in an event log.
- **Operators:** relation-defining metrics: handover of work (a -> b when a's completion is followed by b's task in the same case), subcontracting, joint cases, similar activity profiles. Each yields a weighted directed graph over originators.
- **Captures:** a catalogue of **empirical relation types** between people derived from behaviour traces, i.e. candidate primitive "operators" (hand over to, work with, delegate to).
- **Limits:** relations are *descriptive statistics*, not operators; no composition. Petri-net/workflow background not covered; open Petri nets as compositional processes are in the structured/decorated cospan literature (3b).
- **Relevance:** gives a measured list of what relations between people in organisations are actually observed.

---

## What this cluster already covers

- **Sorts**: three distinct sorts (agent/person, group, role) with a scoping rule (role-in-group) and overlap permitted: AGR. A fourth, permission/capability: RBAC. A relational (not subtype) account of role: Masolo/DOLCE. A structure-plus-occupants account of group: Ritchie. Reified membership: ORG.
- **State and update**: guarded operations (create/join/leave group; assign/deassign user, grant permission) on a sorted relational state with invariants: RBAC/ANSI and AGR.
- **Order on roles**: role hierarchy as a partial order, with constraints: RBAC.
- **Group formation as composition**: nesting with an external interface; a hypergraph category with merge/copy/discard: operads and decorated cospans. Group interaction as irreducible to pairs: hypergraphs/simplices.
- **Several relation types over the same people, and time**: multilayer tensor.
- **Order-dependence as non-commutativity**: the transferable idea from quantum-like models.
- **Minimal act vocabulary for entities**: send, create, become: Actors.
- **Empirically observed relations between people**: handover, subcontracting, working-together: van der Aalst.

## What it does not cover

- **Operators that act on people as social acts.** Every structure *in this cluster* either manages membership/permissions (RBAC, AGR), or sends messages (Actors), or computes statistics (process mining), or evolves a state vector (quantum). *Validation correction:* the original claim that "nothing defines social acts as operators with composition laws" does not survive outside this cluster. Singh's commitments define create, discharge, cancel, release, delegate (change debtor) and assign (change creditor) as operations on C(debtor, creditor, antecedent, consequent): social acts as typed operators on a social state, though without an equational theory. Pörn's influence operators and the Kanger-Lindahl theory of normative positions give modal operators for "a sees to it that b ...". Dynamic epistemic logic's action models (Baltag, Moss, Solecki 1998) are operators on group epistemic states that *do* compose: the sequential composition of two action models is an action model, so "tell a privately, then announce publicly" has a computed product. Compositional game theory composes strategic interactions sequentially and in parallel. What remains missing is narrower: a single algebra that combines these act-operators with the agent/group/role sort structure and gives equations (identity, inverse where it exists, commutation laws) for interpersonal acts such as "A advises B" or "A introduces B to C".
- **Composition laws for social relations**: no one has the table "friend-of-colleague = ?" outside the role-semigroup/kinship work covered by other agents.
- **Operads or hypergraph categories applied to human organisations**: none found, confirmed by a second search in validation. The nearest are engineering systems-of-systems papers, network-model operads for teams of agents (Baez, Foley, Moeller, Pollard 2020), and open games for strategic interaction.
- **Groups as operands that can be acted on and that act** while keeping their member structure: AGR groups are contexts, not actors; hypergraph groups are unlabelled sets; operad boxes could do it but nobody has done so for people.
- **Time and identity change** (a group persisting through membership change, a person's role changing): named by Ritchie, partly handled by temporal multilayer networks, but no algebra.
- **Quantum social science is not what it sounds like.** In its mainstream (Busemeyer, Pothos) it is single-agent probability with a Hilbert-space dress; Khrennikov's social laser is population-level but metaphorical. Do not build on it beyond the non-commutativity idea (Wang et al. 2014).
- I did not find any work that unifies sorts and operators; that is where a social algebra would sit. (Holds after validation, with the act-operator work above as the main input it would draw on.)

**Recommended carrier shape** (my judgement, to be tested against the notes): the AGR triple (Agent, Group, Role with role-local-to-group scoping), reified membership as a quaternary relation (agent, group, role, time) per W3C ORG, a role partial order per RBAC, and group-as-composite with interface per the operad route. Relations between people live as a family of matrices or operators on the agent space (multilayer tensor).

## Missing work (added in validation)

Citations from knowledge unless marked; check before quoting.

- **Commitments.** M. P. Singh, "An ontology for commitments in multiagent systems: toward a unification of normative concepts", *Artificial Intelligence and Law* 7, 97-113 (1999) (confirmed by search). Operations on commitments C(debtor, creditor, ...): create, discharge, cancel, release, delegate, assign; the six-operation list is confirmed from Singh's own later slides, not the 1999 text. **The most direct counterexample to "no social acts as operators".**
- **Influence and normative positions.** I. Pörn, *Action Theory and Social Science: Some Formal Models*, Synthese Library 120, Reidel, 1977. Operators for "a brings it about that" and "a influences b to ...".
- **Institutional power / counts-as.** A. J. I. Jones, M. Sergot, "A formal characterisation of institutionalised power", *Logic Journal of the IGPL* 4(3), 427-443 (1996).
- **Action models.** A. Baltag, L. S. Moss, S. Solecki, "The logic of public announcements, common knowledge, and private suspicions", *TARK 1998*. Group-level epistemic acts as operators with product update and closure under sequential composition.
- **Compositional game theory.** N. Ghani, J. Hedges, V. Winschel, P. Zahn, "Compositional game theory", *LICS 2018*, arXiv:1603.04641. Open games composed sequentially and in parallel in a symmetric monoidal category; the nearest categorical treatment of interactions *between people*.
- **Network-model operads.** Baez, Foley, Moeller, Pollard 2020 (confirmed; see 3c).
- **ARBAC97** (see 5d).
- **Galois lattices for social networks.** L. C. Freeman, D. R. White, "Using Galois lattices to represent network data", *Sociological Methodology* 23, 127-145 (1993). The social use of the Wille concept lattices named in the summary but never given a section.
- **Roles in conceptual modelling.** F. Steimann, "On the representation of roles in object-oriented and conceptual modelling", *Data & Knowledge Engineering* 35(1), 83-106 (2000). The standard CS account of role vs type.

## Unconfirmed (do not cite without checking)

- DOI 10.1109/2.485845 for Sandhu et al. 1996: the usual citation, not returned by any search in either pass. Bibliographic details and the definitions themselves are confirmed.
- ICMAS-98 paper: pages and venue confirmed from bibliographic lists; no full text, DOI or stable PDF (HAL returns 403).
- AGR primitive operation names (MadKit API) and the exact wording of the AGR axioms: full text not obtained.
- Ritchie 2020, PPR 100(2): existence and venue confirmed; issue number and the Type 1/Type 2 terminology are from knowledge.
- OperA as defined in the thesis itself (structure confirmed from 2002-era OperA papers only).
- Agha, *Actors* (MIT Press 1986): catalogue handle only.
- Vagner, Spivak, Lerman: confirmed in validation as *Theory and Applications of Categories* 30(51), 2015 (TAC PDF at emis.univie.ac.at); contents not read.
- Fong's thesis treatment of Petri nets: not checked.
- All axioms and signatures in sections 2, 3, 7 were written from standard knowledge. Section 5a was checked against the full text in validation.

## Relation algebra: Tarski, Maddux, and Allen's interval algebra (§relation algebra)

- Tarski, A. (1941). "On the calculus of relations." *Journal of Symbolic Logic* 6(3): 73-89. DOI 10.2307/2268577; https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/on-the-calculus-of-relations/B9D891E98083640149CFAD0547E69CF3 (metadata confirmed; full text paywalled, copy at https://www.cl.cam.ac.uk/teaching/1011/Databases/Tarski_1941.pdf not read).
- Tarski, A. & Givant, S. (1987). *A Formalization of Set Theory without Variables*. AMS Colloquium Publications 41 (library records agree on 41).
- Maddux, R. D. (2006). *Relation Algebras*. Studies in Logic and the Foundations of Mathematics 150, Elsevier, xxvi+731 pp. https://shop.elsevier.com/books/relation-algebras/maddux/978-0-444-52013-5
- Allen, J. F. (1983). "Maintaining knowledge about temporal intervals." *CACM* 26(11): 832-843. DOI 10.1145/182.358434; PDF https://cse.unl.edu/~choueiry/Documents/Allen-CACM1983.pdf

**Their vocabulary**: relation algebra; Boolean operations; relative product (composition); converse; identity; representable algebra; composition table; base relation.

**Operands**: binary relations on a set (the concrete model), or elements of an abstract algebra axiomatised to mimic them. In Allen, operands are sets of the 13 basic interval relations.

**Operators** and structure:
- A relation algebra is a Boolean algebra (join, meet, complement) with an associative composition `;`, a unary converse, and an identity element, obeying Tarski's equations [from abstract/standard account]. Tarski 1941 gave a first axiomatisation that was not purely equational; the equational one followed by 1943 [from search summary].
- Not every abstract relation algebra is representable as relations on a set [standard account].
- Allen 1983: 13 mutually exclusive base relations between intervals, 2^13 possible disjunctions, converse, and a 13x13 composition table giving, for each pair, the set of base relations possible between the outer intervals [read for the 13 and the table; the algebra being a relation algebra is standard account].
- **Boolean-matrix role semigroups** (Lorrain & White 1971; Boorman & White 1976): a Boolean matrix over a finite set is a binary relation, and Boolean matrix product is relational composition. So the role semigroup generated by the observed relations is a *subsemigroup* of the composition reduct of the full relation algebra on the actor set (a subreduct, not the reduct itself), with identity added if a monoid is wanted; the blockmodel role structures of Boorman & White are further homomorphic images of it (see 01). It lacks complement, meet and converse in the signature, though the matrices underneath admit all of them. Following from the definitions, not from a source that states it.

**Limits**: Pure structure; says nothing of what the relations mean. Complement is often unnatural for social ties ("not a friend" is not a role). Composition tables for many-relation systems get large, and non-representable algebras are a trap if the intended model is people.

**Relevance to social-algebra**: This is the precedent for "operators and operands and a table". It is one candidate form for a first model: a finite relation algebra, or a composition subreduct of one, with Allen as a worked template (base relations, converse, a table, constraint propagation). Whether to adopt it is open. The converse is the real design point: "A advises B" has the converse "B is advised by A", which role semigroups ignore.

Unconfirmed: Tarski's text and the axioms; Tarski & Givant and Maddux contents; Lorrain-White and Boorman-White citations and the reduct claim against their text; that Allen's algebra is a relation algebra (Ladkin & Maddux, Ligozat); the 13x13 table was not re-checked in the PDF.

_Added 2026-10-29 after the second pass, on next-pattern's direction; this entry has not itself been second-passed. Provenance tags as marked._

## Validation log (2026-10-29)

- Battiston et al. 2020, *Phys. Rep.*: ✓
- Iacopini et al. 2019, *Nat. Commun.*: ✓
- Lambiotte, Rosvall, Scholtes 2019, *Nat. Phys.*: ✓
- Bick et al. 2023, *SIAM Review*: ✓
- De Domenico et al. 2013, *PRX*: ✓ (tensor description is standard and right)
- Kivelä et al. 2014, *J. Complex Netw.*: ✓
- Spivak 2013, arXiv:1305.0297: ✓; ✎ noted its own Society-of-Mind and human/machine remark
- Vagner, Spivak, Lerman: ✎ resolved to TAC 30(51), 2015
- Fong 2015, *TAC*: ✓; ✎ Petri-net remark softened, structured-vs-decorated cospans (2022) added
- Fong 2016 thesis: ✓
- Baez and Fong 2018, *TAC*: ✓
- Foley et al. 2021, *Proc. R. Soc. A*: ✓
- Baez and Foley: ✎ venue added (*Notices AMS* 68(6), 2021)
- Haven and Khrennikov 2013: ✓; ✎ the "one agent only" claim corrected (social laser)
- Busemeyer and Bruza 2012: ✓
- Pothos and Busemeyer 2013, *BBS*: ✓
- Sandhu et al. 1996 (RBAC96): ✎ session-activation inequality reversed (wrong direction), RBAC0–3 and administrative roles made precise; DOI ? unconfirmed
- Ferraiolo et al. 2001: ✎ venue confirmed (*ACM TISSEC* 4(3), 224-274)
- ANSI/INCITS 359-2004: ✓; ✎ "limited hierarchy" made precise
- Denning 1976: ✎ moved from Unconfirmed to confirmed
- Masolo et al. 2004: ✓ (abstract-level)
- W3C ORG 2014: ✓; ✓ errata claim confirmed
- Boella and van der Torre: ✎ resolved to *AI & Law* 15(3), 2007
- Ritchie 2013: ✓; ✎ later 2020 paper confirmed and its Type 1/Type 2 restriction added
- Uzquiano 2018: ✓
- Ferber and Gutknecht 1998 (ICMAS): ✓ bibliographic; ? full text
- Ferber, Gutknecht, Michel 2003: ✓; ✗ removed arXiv:1506.09032 as supporting evidence (it does not mention AGR); ? operator names
- Dignum 2004: ✓; ✎ OperA structure (three models, social and interaction contracts) corrected and confirmed from OperA papers
- Hewitt, Bishop, Steiger 1973: ✓
- Agha 1986: ? catalogue only
- van der Aalst, Reijers, Song 2005, and BPM 2004: ✓
- Closing verdict: ✎ "nothing defines social acts as operators with composition laws" corrected; the operads gap stands, narrowed
- Added: ARBAC97, Wang et al. 2014, network-model operads, Singh, Pörn, Jones-Sergot, Baltag-Moss-Solecki, compositional game theory, Freeman-White, Steimann

**Verdict.** No fabricated works were found. Every citation exists, and bibliographic details were right apart from one evidential URL that did not support what it was cited for. The algebra was mostly sound but had one real error: the reversed RBAC1 session inequality, which is the kind of error that would propagate into a carrier definition. The weakest part was the closing gap claim, which held only within this cluster and was overstated against work in logic and multi-agent systems.
