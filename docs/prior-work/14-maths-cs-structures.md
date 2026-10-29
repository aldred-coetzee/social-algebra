# Prior work 14: mathematical and computer-science structures for people, roles and groups

Date: 2026-10-29. Cluster: maths and CS formalisations, outside the cases other agents cover (role semigroups/blockmodels, kinship, modal/deontic/epistemic logics, bigraphs, sheaf opinion dynamics, ologs, opinion dynamics).

**Provenance rule.** Bibliographic facts (title, authors, venue, DOI/arXiv) below were confirmed this session by search or fetch; the source URL is given per entry. The algebraic descriptions (signatures, axioms) are the standard definitions as I know them; I fetched abstracts, not full texts, so treat any axiom as "check against the paper before relying". Where I could not confirm a source it is under "Unconfirmed" at the end.

## Summary

Nobody has built a single "algebra of people, roles and groups", but every ingredient exists as a mature, separately developed structure, mostly outside social science:

- **Carrier structures for operands** that are genuinely usable: the AGR/Aalaadin triple (agent, group, role) from multi-agent systems; the RBAC96/ANSI relational model (users, roles, permissions, with a role partial order); Wille's concept lattices (formal contexts of persons x attributes or persons x events); hypergraphs/simplicial complexes (a group is a hyperedge/simplex). Of these, AGR and RBAC are the only ones that already *name* people, roles and groups as three distinct sorts.
- **Composition operators** that are genuinely algebraic: operads/wiring diagrams and decorated cospans (Spivak; Fong; Baez-Fong). These give a rigorous "put groups together into a bigger group, with interfaces" operation. No one has applied them to human groups; the applications are circuits, databases, dynamical systems and engineered systems of systems.
- **Ontological accounts** of what a role and a group *are* (DOLCE roles; Ritchie's structuralism; W3C ORG) are good at deciding what the sorts should be, and give no operators.
- **Quantum-like social science** is not a literal algebra of persons; it is a probability/decision model for one agent's judgments. Do not adopt it as a carrier.

---

## 1. Higher-order networks: hypergraphs and simplicial complexes

### 1a. Battiston et al. 2020
- **Citation:** F. Battiston, G. Cencetti, I. Iacopini, V. Latora, M. Lucas, A. Patania, J.-G. Young, G. Petri, "Networks beyond pairwise interactions: structure and dynamics", *Physics Reports* 874, 1-92 (2020).
- **Verified:** https://arxiv.org/abs/2006.01764 ; DOI 10.1016/j.physrep.2020.05.004.
- **Their vocabulary:** higher-order interactions, group interactions, hyperedge, simplex, facet, clique complex, bipartite (incidence) representation, higher-order Laplacian, simplicial/hypergraph "contagion", "synchronization".
- **Operands:** nodes (units) and *groups of nodes of any size*, as hyperedges (arbitrary subsets of V) or simplices (subsets closed under taking subsets).
- **Operators / algebraic structure:** a hypergraph is H = (V, E) with E a subset of the power set P(V). A simplicial complex K is a downward-closed family of subsets (the axiom: sigma in K and tau subset of sigma implies tau in K). Algebra proper: incidence matrices B_k, boundary operators d_k with d_{k-1} d_k = 0, and higher-order (Hodge) Laplacians L_k = d_{k+1} d_{k+1}^T + d_k^T d_k acting on k-chains. Dynamics are defined by these operators. There is no composition law on groups themselves; "operators" here are linear maps on functions of simplices, not operations *by* people on one another.
- **What it captures:** that a group interaction is not reducible to the set of pairs in it; size-dependent effects (critical-mass thresholds, explosive transitions).
- **Limits:** groups are unlabelled subsets. No roles, no direction, no difference between "a chairs b, c, d" and "a, b, c, d meet". Simplicial closure forces every subgroup to be an interaction, which is false for committees. Hypergraphs lift that but lose the Hodge machinery.
- **Relevance:** the natural *membership layer* carrier: a group = element of P(V) with a set-algebra (union, intersection, containment) for free. Insufficient alone; combine with roles (see AGR, RBAC).

### 1b. Iacopini et al. 2019
- **Citation:** I. Iacopini, G. Petri, A. Barrat, V. Latora, "Simplicial models of social contagion", *Nature Communications* 10, 2485 (2019).
- **Verified:** https://arxiv.org/abs/1810.07031 ; DOI 10.1038/s41467-019-10431-6.
- **Vocabulary:** simplicial contagion, infection via 2-simplices (triangles) with rate beta_Delta in addition to pairwise rate beta, bistability, discontinuous transition.
- **Operands:** individuals with state S or I, group-of-three simplices.
- **Operators:** a stochastic update rule on a simplicial complex: a susceptible node becomes infected at a rate that sums a pairwise term and a term per triangle whose other two vertices are both infected; recovery at rate mu. No algebraic closure properties.
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
- **Operators / structure (standard, from the paper's framework; abstract confirmed, formulas not re-read):** a rank-4 adjacency tensor M with entries M^{i alpha}_{j beta} (node i in layer alpha to node j in layer beta), built from a tensor product of the vector spaces of nodes and layers, with Kronecker/tensor-contraction operations generalising degree, centrality, modularity and diffusion. Standard linear algebra (tensor product, contraction), no new axioms.
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
- **Operators and structure (standard):** colored operad W. Objects: interfaces. Operations: a wiring diagram with n inner boxes and one outer box, W(X_1,...,X_n; Y). Composition: nest diagrams inside inner boxes. Axioms: associativity of composition, unit identity wiring, equivariance under permuting inputs. Algebras of the operad assign to each box a set (e.g. behaviours) and to each diagram a function from the product of inner behaviours to outer behaviour. Related: Vagner, Spivak, Lerman, "Algebras of open dynamical systems on the operad of wiring diagrams" (surfaced in search; not fetched).
- **Captures:** compositionality: how a system built from parts presents one interface to the outside; hierarchical nesting.
- **Limits:** the wiring is *static and typed*; people-as-boxes would need to rewire as relationships change. No application to organisations found (search for one returned engineering uses only).
- **Relevance:** **strongest candidate for the group-formation operator**: "a group is the composite of members with its own external interface (the role it presents to other groups)". Operands = people or groups as boxes; composition = nesting groups in groups, giving the multi-level hierarchy for free. Does not specify what a person is.

### 3b. Fong 2015, Fong 2016, Baez-Fong 2018
- **Citations:** B. Fong, "Decorated cospans", *Theory and Applications of Categories* 30(33), 1096-1120 (2015), https://arxiv.org/abs/1502.00872. B. Fong, "The algebra of open and interconnected systems", DPhil thesis, Oxford, arXiv:1609.05382, https://arxiv.org/abs/1609.05382. J. C. Baez, B. Fong, "A compositional framework for passive linear networks", *Theory and Applications of Categories* 33(38), 1158-1222 (2018), https://arxiv.org/abs/1504.05625.
- **Vocabulary:** open system, cospan X -> N <- Y, decoration, hypergraph category (special commutative Frobenius monoid on every object), corelation, black-box functor.
- **Operands:** finite sets of terminals (interface) as objects; morphisms are open systems.
- **Operators and structure:** given a category C with finite colimits and a lax monoidal functor F : (C, +) -> (Set, x), objects of the new category are those of C and morphisms X -> Y are isomorphism classes of cospans X -> N <- Y with an element of F(N). Composition by pushout of cospans, decorations combined via F. Result: a symmetric monoidal category (hypergraph category) with the Frobenius structure (copy/merge/discard/create) on each object. A black-box functor forgets internals and keeps behaviour.
- **Captures:** gluing open systems at shared terminals; the "interconnection" operator is the pushout; behavioural semantics by functor.
- **Limits:** systems are physical/formal (circuits, Petri nets, reaction networks); the composition is "identify terminals", not "A does something to B". Fong notes Petri nets as an instance, which links to section 8.
- **Relevance:** the hypergraph-category structure (*merge, copy, discard* on each object) is a very close match to what "people joining, splitting, leaving a group" do. Treat as the **ambient category**, not the carrier.

### 3c. Operads for design (context)
- Foley, Breiner, Subrahmanian, Dusel, "Operads for complex system design specification, analysis and synthesis", *Proc. R. Soc. A* (2021), DOI 10.1098/rspa.2021.0099 ; https://arxiv.org/abs/2101.11115. Baez, Foley, "Operads for designing systems of systems", https://arxiv.org/abs/2009.12647. Both engineering; my search found **no operadic treatment of social organisations**. That gap is itself a finding.

---

## 4. Quantum-like social science

### 4a. Haven and Khrennikov, *Quantum Social Science* (2013)
- **Citation:** E. Haven, A. Khrennikov, *Quantum Social Science*, Cambridge University Press, 2013, ISBN 978-1-107-01282-0, 279 pp.
- **Verified:** Cambridge catalogue https://www.cambridge.org/core/books/quantum-social-science/preface/761E77E20744AF48B5DEF82460744895 (copyright page confirms 2013, ISBN).
- **Vocabulary:** quantum-like, state vector/density operator, observable, superposition, interference, contextuality, order effects, "mental state".
- **Operands:** the *mental state of one decision-maker or one market*, as a vector in a complex Hilbert space (or probability amplitudes).
- **Operators:** self-adjoint operators as questions/observables; projections; unitary evolution; measurement with state collapse (Luders rule). Algebra: the (non-commutative) operator algebra B(H); the non-commutativity of two projections models order effects in survey answers.
- **How literal is it?** Not literal about people. The books are explicit that "quantum-like" means the *mathematics* of quantum probability is used, with no claim that brains are quantum physical systems. The state is one agent's belief/judgment state, not a society. Applications covered: decision paradoxes, finance, economics, brain science.
- **Limits:** one agent at a time; a population is modelled by a *product* or *mixture*, with no native roles or groups. The claim of unique explanatory power has been contested in open peer commentary (see 4b).
- **Relevance:** only one transferable idea: **order-dependence as non-commutativity** (answering a then b differs from b then a). That is a genuine algebraic fact a social algebra of "acts" may want (e.g. who is told first). The Hilbert-space carrier is not recommended for operands.

### 4b. Busemeyer and Bruza 2012; Pothos and Busemeyer 2013
- J. R. Busemeyer, P. D. Bruza, *Quantum Models of Cognition and Decision*, Cambridge University Press, 2012, DOI 10.1017/CBO9780511997716 (catalogue: https://resolve.cambridge.org/core/books/quantum-models-of-cognition-and-decision/75909428F710F7C6AF7D580CB83443AC). Uses entanglement for non-reductionist cognition models; again one-agent.
- E. M. Pothos, J. R. Busemeyer, "Can quantum probability provide a new direction for cognitive modeling?", *Behavioral and Brain Sciences* 36(3), 255-274 (2013), DOI 10.1017/s0140525x12001525. With open commentaries that dispute the stronger claims (e.g. Gelman and Betancourt).

---

## 5. Role-based access control (RBAC) as a formal algebra

### 5a. Sandhu et al. 1996 (RBAC96 family)
- **Citation:** R. S. Sandhu, E. J. Coyne, H. L. Feinstein, C. E. Youman, "Role-Based Access Control Models", *IEEE Computer* 29(2), 38-47, Feb 1996.
- **Verified:** volume/pages confirmed across several sources (search result; no DOI confirmed; see Unconfirmed). Full text mirror found: https://wiki.orbit-lab.org/raw-attachment/wiki/Internal/Rbac/RbacResources/00503698.pdf (not read in this session).
- **Vocabulary:** user, role, permission, session, role hierarchy, constraints (separation of duty), cardinality.
- **Operands (sorts):** U (users), R (roles), P (permissions), S (sessions).
- **Operators and structure (standard definition):**
  - UA subset of U x R (user assignment), PA subset of P x R (permission assignment), many-to-many.
  - RH subset of R x R, a **partial order** (reflexive, antisymmetric, transitive) with r1 >= r2 meaning r1 inherits all permissions of r2; RBAC1.
  - session map user(s) in U, roles(s) subset of {r : exists r' <= r with (user(s), r') in UA}.
  - constraints (RBAC2): static/dynamic separation of duty as predicates over UA and sessions; RBAC3 = 1+2.
  - Authorisation: user u may do p in session s iff exists r in roles(s) with (p, r) in PA after closure under the order.
- **Captures:** the cleanest *existing* formal separation of person vs role vs capability, with an order on roles and constraints (mutual exclusion, cardinality).
- **Limits:** static assignment relations (no verbs between people); roles are *permission bundles*, not social positions; no group sort in the base model (groups appear in later extensions); no notion of one person acting on another.

### 5b. NIST proposal and ANSI/INCITS 359-2004
- **Citations:** D. F. Ferraiolo, R. Sandhu, S. Gavrila, D. R. Kuhn, R. Chandramouli, "Proposed NIST standard for role-based access control", DOI 10.1145/501978.501980 (DOI confirmed in search; venue given as *ACM TISSEC* 2001 from my memory, not confirmed). ANSI/INCITS 359-2004 *Information Technology - Role Based Access Control*, effective 3 Feb 2004 (confirmed via https://xml.coverpages.org/ni2004-04-05-a.html and NIST page https://csrc.nist.gov/projects/role-based-access-control).
- **Structure:** Core RBAC, Hierarchical RBAC (general = partial order; limited = tree), Static Separation of Duty, Dynamic Separation of Duty. Standard defines **functional specification**: administrative commands (AddUser, DeleteUser, AssignUser, DeassignUser, GrantPermission, RevokePermission, AddInheritance, DeleteInheritance, CreateSsd/Dsd set, ...), review functions (AssignedUsers, AssignedRoles, AuthorizedUsers, ...), and system functions (CreateSession, AddActiveRole, CheckAccess). Each given as pre/post-conditions over the relation sets.
- **Relevance to an algebra:** the administrative commands are literally an **operator signature over a state of (U, R, P, UA, PA, RH)**: a small state-transition algebra. This is the closest existing thing to "operators that act on the structure of a group of people". It is about *managing* access, not social behaviour, but the pattern (state = sorted relational structure; operators = guarded updates; invariants = constraints) is directly reusable.

### 5c. Aside: lattice view
- Role hierarchy as a partial order, and dominance/lattice models of information flow (Denning 1976) underlie much RBAC theory; I did not fetch a source for Denning and list it as unconfirmed.

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
- **Limits:** a vocabulary (OWL/RDF), no operators. Errata note a modelling mistake: org:holds/org:heldBy were wrongly made sub-properties of memberOf/hasMember, i.e. confusing holding a post with being a member.
- **Relevance:** a useful sanity check: reify membership as a ternary or quaternary relation (who, which group, in which role, when).

### 6c. Boella and van der Torre (roles in normative MAS)
- Search found the tutorial "Roles from Different Angles" (Boella, Hulstijn, van der Torre) and papers on counts-as and delegation of power (DEON 2006, LNCS 4048; PRIMA 2008). Their position, per snippets: roles carry powers and norms, several agents may enact one role, one agent several roles. I could not confirm exact titles for the role-as-institutional-power papers, so I list them under Unconfirmed. Normative/deontic logic is covered by another agent.

### 6d. Ritchie, Uzquiano: what a group is
- **Ritchie:** K. Ritchie, "What are groups?", *Philosophical Studies* 166(2), 257-272 (2013). Argues four views (non-singular pluralities, fusions, aggregates, sets) each fail at least one of six adequacy criteria; proposes **groups as realisations of structures**: a structure's functionally defined nodes/places are occupied. (Confirmed via search summaries; https://diversityreadinglist.org/?p=3735.)
- **Uzquiano:** G. Uzquiano, "Groups: toward a theory of plural embodiment", *Journal of Philosophy* 115(8), 423-452 (2018), DOI 10.5840/jphil2018115825; https://research-repository.st-andrews.ac.uk/handle/10023/18222. A group at a time is just its members arranged in a complex condition.
- **Why it matters:** the *set* carrier fails: the same members can be two different groups; a group persists through changing membership; membership has no structure. Ritchie's structure-plus-occupants is precisely **(a graph/relational structure with typed slots) + (an assignment of persons to slots)**, i.e. the same shape as AGR and RBAC. Convergence of three independent traditions on one carrier shape.
- **Limits:** no operators; the philosophy defines identity conditions only.

---

## 7. Multi-agent organisation models

### 7a. AGR / Aalaadin (Ferber and Gutknecht) *highly relevant*
- **Citations:** J. Ferber, O. Gutknecht, "A meta-model for the analysis and design of organizations in multi-agent systems", *Proc. 3rd Int. Conf. on Multi-Agent Systems (ICMAS-98)*, Paris, 1998, pp. 128-135, IEEE Computer Society. J. Ferber, O. Gutknecht, F. Michel, "From agents to organizations: an organizational view of multi-agent systems", in *Agent-Oriented Software Engineering IV (AOSE 2003)*, LNCS 2935, Springer, pp. 214-230, DOI of volume 10.1007/b95187.
- **Verified:** venue, pages and the AALAADIN/AGR relationship confirmed via bibliographic records and the 2015 overview https://arxiv.org/pdf/1506.09032 ; DBLP https://dblp.org/pid/86/1212. I could not fetch the paper text (the HAL copy returned 403); definitions below are from my knowledge of the model and flagged accordingly.
- **Vocabulary:** agent, group, role, group structure, organisational structure, "organisational reflection", OCMAS.
- **Operands (three sorts):** Agent (an active communicating entity, no constraint on internals), Group (an atomic set of agents, a context for interaction; an agent may belong to several groups; groups may overlap), Role (an abstract representation of a function/service/identity of an agent *within a group*).
- **Structure (standard):** roles are **local to a group** (a role "buyer" in group G1 is different from "buyer" in G2); an agent can hold several roles, in several groups; communication is only possible between agents sharing a group; group structure = set of roles + role cardinalities + a graph of allowed interactions between roles. Entering a group = requesting a role (group-manager role mediates). In the 2003 version, an organisation structure is the abstract description (roles, interaction graph), and an organisation is a structure plus its concrete agents, like Ritchie's realisation.
- **Operators:** the *primitives* are: create a group, join a group (acquire a role), leave a group, request/leave a role. These are stateful, guarded operations on the triple (A, G, R) and its membership relation.
- **Captures:** a precise, minimal sort system for exactly the problem set (people, roles, groups) with scoping rules (role-in-group), overlap, and a closure principle: communication through shared groups.
- **Limits:** no semantics for what agents *do to* one another beyond message passing; no dynamics of influence; no operator composition laws; groups are flat (the model is "atomic groups"; hierarchy only by agents belonging to groups at several levels); no norms (add MOISE/OperA).
- **Relevance:** **the best single candidate for the carrier structure.** Take (Agent, Group, Role) with role-local-to-group scoping and the join/leave/create operators; treat the interaction graph of a group structure as the place where social operators (relations on roles) live.

### 7b. OperA (Dignum)
- **Citation:** V. Dignum, "A model for organizational interaction: based on agents, founded in logic", PhD thesis, Utrecht University, awarded 12 January 2004 (SIKS; ISBN 90-393-3568-0).
- **Verified:** https://dspace.library.uu.nl/handle/1874/890. The thesis page confirms the title and thesis; my search did not confirm OperA detail from the thesis page, but the thesis is the standard OperA reference.
- **Vocabulary (from OperA literature, unverified here):** organisational model (roles, interaction scripts, norms), social model (agent contracts), interaction model.
- **Relevance:** adds a social contract layer (an agent *commits* to a role) on top of AGR-like structure. Detail not verified in this session; low confidence.

---

## 8. Actors, Petri nets, process mining

### 8a. Hewitt's Actor model
- **Citation:** C. Hewitt, P. Bishop, R. Steiger, "A universal modular ACTOR formalism for artificial intelligence", *Proc. IJCAI-73*, pp. 235-245 (some records give 235-244).
- **Verified:** https://ijcai.org/proceedings/1973/31 ; PDF https://worrydream.com/refs/Hewitt_1973_-_A_Universal_Modular_Actor_Formalism_for_Artificial_Intelligence.pdf.
- **Operands:** actors, each with a mailbox/address. **Operators (standard):** on receiving a message an actor can (a) send messages to known actors, (b) create new actors, (c) designate how it will handle the next message (become). No shared state; asynchronous; message order not guaranteed. Agha's *Actors* (MIT Press, 1986) gives the operational semantics (I did not verify the catalogue entry beyond the MIT handle 1721.1/6952).
- **Captures:** "entities that do things to each other by sending messages, can create others, and change their own behaviour": three primitives, no more.
- **Limits:** no sort for group or role (those are patterns of address-knowledge); no social semantics.
- **Relevance:** a minimal operator signature for *person acts on person*: send(a, b, m), create(a), become(a, behaviour). Useful as a floor for the operator vocabulary; it is the formalism that treats "the people" as the only primitives.

### 8b. van der Aalst: social network mining from event logs
- **Citation:** W. M. P. van der Aalst, H. A. Reijers, M. Song, "Discovering social networks from event logs", *Computer Supported Cooperative Work* 14(6), 549-593 (2005), DOI 10.1007/s10606-005-9005-9; https://research.tue.nl/en/publications/discovering-social-networks-from-event-logs/ ; earlier: "Mining social networks: uncovering interaction patterns in business processes", BPM 2004, LNCS 3080, pp. 244-260.
- **Vocabulary:** originator, handover of work, subcontracting, working together, similar tasks, MiSoN tool.
- **Operands:** persons/originators and activities in an event log.
- **Operators:** relation-defining metrics: handover of work (a -> b when a's completion is followed by b's task in the same case), subcontracting, joint cases, similar activity profiles. Each yields a weighted directed graph over originators.
- **Captures:** a catalogue of **empirical relation types** between people derived from behaviour traces, i.e. candidate primitive "operators" (hand over to, work with, delegate to).
- **Limits:** relations are *descriptive statistics*, not operators; no composition. Petri-net/workflow background not covered; a Petri net as a model of process is available through Fong's thesis (3b).
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

- **Operators that act on people as social acts.** Every structure above either manages membership/permissions (RBAC, AGR), or sends messages (Actors), or computes statistics (process mining), or evolves a state vector of one agent (quantum). Nothing defines "A advises B", "A defers to B", "A introduces B to C" as an operation with an algebraic signature, identity element, inverse or composition law. This is the gap, and it is wide.
- **Composition laws for social relations**: no one has the table "friend-of-colleague = ?" outside the role-semigroup/kinship work covered by other agents.
- **Operads or hypergraph categories applied to human organisations**: none found. The nearest are engineering systems-of-systems papers.
- **Groups as operands that can be acted on and that act** while keeping their member structure: AGR groups are contexts, not actors; hypergraph groups are unlabelled sets; operad boxes could do it but nobody has done so for people.
- **Time and identity change** (a group persisting through membership change, a person's role changing): named by Ritchie, partly handled by temporal multilayer networks, but no algebra.
- **Quantum social science is not what it sounds like.** It is not a population-level algebra; it is single-agent probability with a Hilbert-space dress. Do not build on it beyond the non-commutativity idea.
- I did not find any work that unifies sorts and operators; that is where a social algebra would sit.

**Recommended carrier shape** (my judgement, to be tested against the notes): the AGR triple (Agent, Group, Role with role-local-to-group scoping), reified membership as a quaternary relation (agent, group, role, time) per W3C ORG, a role partial order per RBAC, and group-as-composite with interface per the operad route. Relations between people live as a family of matrices or operators on the agent space (multilayer tensor).

## Unconfirmed (not verified this session; do not cite without checking)

- DOI for Sandhu et al. 1996, *IEEE Computer* 29(2). Bibliographic details were confirmed, a DOI was not (the search returned a misleading ACM DOI for a different item).
- Venue and year (ACM TISSEC 2001) for the Ferraiolo et al. proposed NIST standard; the DOI 10.1145/501978.501980 was returned by search but the journal name was not confirmed.
- ICMAS-98 paper: pages and venue are confirmed from bibliographic lists; I did not obtain the full text, a DOI, or a stable PDF (the HAL copy returned 403).
- Boella and van der Torre: exact titles of the role/institutional-power papers; snippets only.
- Ritchie, "Social structures and the ontology of social groups" (a later Ritchie paper cited by others as 2018 or 2020): title and venue not confirmed.
- Dignum OperA content: thesis existence confirmed, OperA details not.
- Agha, *Actors* (MIT Press 1986): catalogue handle only.
- Denning 1976 lattice model of secure information flow: not searched.
- Vagner, Spivak, Lerman (2014) "Algebras of open dynamical systems on the operad of wiring diagrams": surfaced in a search snippet, not fetched.
- All axioms and signatures in sections 2, 3, 5, 7 were written from standard knowledge and not re-read against the full texts.
