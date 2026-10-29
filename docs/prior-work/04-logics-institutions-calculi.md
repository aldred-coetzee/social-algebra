# Prior work, cluster 4: logics, grammars and calculi of social action and institutions

Date: 2026-10-29

**Summary.** A large body of formal work already treats parts of what social-algebra wants. Operands (agents, roles, coalitions) and operators (speech acts, announcements, norms, joint actions) are all formalised somewhere. The pieces are mostly *logics*: they have a state-transition or satisfaction semantics, with "operators" in the modal sense, not an algebra with a carrier set and equational laws on social objects. The closest approaches to an algebra are Milner's bigraphs (an algebra of structure and reaction, not applied to society), Hansen-Ghrist sheaves (an operator, the sheaf Laplacian, but only on opinion dynamics), and the Institutional Grammar (a notation, with no operator algebra). No work found here supplies one typed algebra whose operands are people, roles and groups and whose operators are the things they do to each other, with laws. The pieces exist; the unification does not appear in this cluster.

**Verification note.** Every citation below was found through a web search that returned a bibliographic record, abstract or publisher/repository page (URLs given). I did not read most full texts. Descriptions of formal structure marked "(standard definition)" are the well-known textbook form of the system and were not re-checked line by line against the primary paper; descriptions marked "(source)" come from the abstract or page retrieved. Treat the formal sketches as a guide to be checked before being relied on in the algebra's own notes.

---

## 1. Crawford & Ostrom 1995: the Grammar of Institutions (ADICO)

- Citation: Sue E. S. Crawford and Elinor Ostrom, "A Grammar of Institutions", *American Political Science Review* 89(3): 582-600, 1995.
- Verified at: https://ideas.repec.org/a/cup/apsrev/v89y1995i03p582-600_09.html (bibliographic record and abstract).
- **Operands.** Institutional statements (text), parsed into components. The things referred to are actors by *attribute* (Attribute = who the rule applies to), not individuals.
- **Operators / structure.** A syntax, not an operator algebra. Statement types: rules (ADICO), norms (ADIC), shared strategies (AIC). (Corrected in validation: norms lack only the Or-else, not the Deontic; the earlier text had "AICO".) Components: **A**ttribute, **D**eontic (may/must/must not), a**I**m, **C**ondition, **O**r else (sanction). Siddiki et al. 2011 added **B** (oBject, the receiver of the action), giving ABDICO (S. Siddiki, C. M. Weible, X. Basurto, J. Calanni, "Dissecting Policy Designs: An Application of the Institutional Grammar Tool", *Policy Studies Journal* 39(1): 79-103, 2011). [from abstract/standard account]
- **Captures.** A uniform way to decompose written rules into comparable parts; a basis for coding large corpora of institutions.
- **Limits.** Descriptive coding scheme. No semantics of composition, no way to combine statements, no state change. Says nothing of what actors do to one another beyond the Aim field. Primarily regulative.
- **Relevance.** Gives a field-tested vocabulary for *rules*, which could be the structure of an operator's precondition and sanction. Not an algebra.

## 2. Institutional Grammar 2.0 (Frantz & Siddiki)

- Citations: Christopher K. Frantz and Saba Siddiki, "Institutional Grammar 2.0: A specification for encoding and analyzing institutional design", *Public Administration* 99(2): 222-247, 2021, DOI 10.1111/padm.12719. Companion: "Institutional Grammar 2.0 Codebook", arXiv:2008.08937 (https://arxiv.org/abs/2008.08937, latest v5, Oct 2024). Book: Frantz & Siddiki, *Institutional Grammar: Foundations and Applications for Institutional Analysis*, Palgrave Macmillan, 2022 (https://www.palgrave.com/gp/book/9783030863715).
- **Operands.** Institutional statements, now including *constitutive* statements, plus hybrid (regulative+constitutive) and polymorphic statements.
- **Operators / structure.** Three expressiveness levels: IG Core, IG Extended, IG Logico. IG Logico expresses statements in a logic-based, machine-processable form, with nested statements and logical combination of components (source: arXiv codebook summary). Tooling exists (IG Parser, github.com/chrfrantz/ig-parser). [from abstract/standard account]
- **Captures.** Rules, norms, constitutive definitions, and their nesting; computational analysis of policy text.
- **Limits.** Still a coding scheme for *texts*. The Logico level gives logical form but I did not find a compositional algebra of statements or a dynamic semantics of what happens when they are applied.
- **Relevance.** The most mature practical notation for institutional statements. A strong candidate source for "operator specification" fields. Not the algebra.

## 3. Searle: constitutive rules, "X counts as Y in C"

- Citations: John R. Searle, *Speech Acts* (1969), *The Construction of Social Reality* (1995), *Making the Social World* (2010); "Social Ontology: Some Basic Principles", *Anthropological Theory* 6(1), 2006 (these identified in search results as the loci of the formula and the regulative/constitutive distinction).
- Verified at: https://en.wikipedia.org/wiki/Social_ontology ; secondary source discussing the formula and Searle 1995/2010: https://www.argumenta.org/article/two-concepts-constitutive-rules/ . The SEP entry "Social Ontology" exists (first published March 2018) but I could not open the relevant section.
- **Operands.** Entities (people, objects, acts) X, status Y, context C.
- **Operators.** The status-function assignment "X counts as Y in C" (the formula first appears in *Speech Acts*, 1969). It is the base of institutions sustained by collective acceptance (money, marriage, office) (wording follows the Wikipedia article 'Social ontology', CC BY-SA 4.0). In *Making the Social World* (2010) Searle recasts all institutional facts as created by Status Function Declarations and accepts "freestanding" status functions with no X term (corporations, electronic money), so the X-counts-as-Y form is no longer the general case even for him. [from abstract/standard account]
- **Captures.** How institutional facts (roles, ownership, offices) arise by collective acceptance, as distinct from brute facts.
- **Limits.** Informal. Critics say the counts-as form is too narrow a reading of constitutive rules (source: Argumenta).
- **Relevance.** Supplies the *role-assignment* operator conceptually (a person counts as a chair in a meeting). A prerequisite for the algebra, formalised below.

## 4. Formalisations of counts-as: Jones & Sergot; Grossi, Meyer, Dignum

- Citations:
  - A. J. I. Jones and M. J. Sergot, "A Formal Characterisation of Institutionalised Power", *Journal of the IGPL* 4(3): 427-443, 1996, DOI 10.1093/jigpal/4.3.427 (DOI record, DBLP and PhilPapers agree on 427-443; Sergot's own page says 429-445). Located via https://www.ida.liu.se/ext/brs/A/Sergot/webpapers.html .
  - D. Grossi, J.-J. Ch. Meyer, F. Dignum, "Classificatory aspects of counts-as: An analysis in modal logic", *Journal of Logic and Computation* 16(5): 613-643, 2006, DOI 10.1093/logcom/exl027 (Crossref).
  - Grossi, Meyer, Dignum, "The many faces of counts-as: A formal analysis of constitutive rules", *Journal of Applied Logic* 6(2): 192-217, 2008, DOI 10.1016/j.jal.2007.06.008 (https://research.vu.nl/en/publications/the-many-faces-of-counts-as-a-formal-analysis-of-constitutive-rul/).
  - Grossi et al., "Counts-as: Classification or Constitution? An Answer Using Modal Logic", DEON 2006 (https://dspace.library.uu.nl/handle/1874/19680); "Modal logic investigations in the semantics of counts-as", ICAIL 2005 (https://research.vu.nl/en/publications/modal-logic-investigations-in-the-semantics-of-counts-as/); "On the Logic of Constitutive Rules", Dagstuhl 07122 (DOI 10.4230/DagSemProc.07122.23; identifier matches the volume's table of contents, checked 2026-10-29).
- **Operands.** Propositions about states of a normative system / institution; context indexes.
- **Operators.** Jones-Sergot: counts-as as a *conditional* connective (written `A =>_s B`, "A counts as B in institution s") plus an agentive operator for bringing-about; institutional power is the combination "agent does A, which counts as B, so B is officially true" (source: secondary descriptions in AICOL 2015 slides and ESAW 2008 slides). Grossi et al.: three readings of the same expression, from contextual *classification* (a modal-logic construction in which contexts are modal indices), through *proper* contextual classification, to the *constitutive rule* reading (source: JAL abstract; the middle label is from Grossi's slides; the DEON 2006 paper had only two readings). [from abstract/standard account]
- **Captures.** Institutional power, status assignment, and which inference patterns counts-as supports (Jones-Sergot's conditional is transitive but deliberately not reflexive; Grossi et al. separate the readings partly by such properties). The earlier wording "not transitive" was wrong for Jones-Sergot.
- **Limits.** A logic of *facts true in an institution*, not an algebra of agents. Agents are mostly implicit; groups and roles are not first-class.
- **Relevance.** Gives a precise logic for the role-assignment operator. A candidate semantic foundation for "this person occupies this role". Does not provide operators between people.

## 5. Searle & Vanderveken: illocutionary logic

- Citation: John R. Searle and Daniel Vanderveken, *Foundations of Illocutionary Logic*, Cambridge University Press, 1985, xi+227 pp. (paperback 2009, ISBN 9780521108850).
- Verified at: https://www.cambridge.org/core/journals/journal-of-symbolic-logic/article/abs/john-r-searle-and-daniel-vanderveken-foundations-of-illocutionary-logic-cambridge-university-press-cambridge-etc-1985-xi-227-pp/2491BCE6C95F77DB9FC1A0FCD5356969 (review); https://aclweb.org/anthology/J88-2007.pdf (review).
- **Operands.** Propositional contents P.
- **Operators.** Illocutionary forces F as functions applied to contents: F(P). A force is a septuple-style composite of components (illocutionary point, degree of strength, mode of achievement, propositional content conditions, preparatory conditions, sincerity conditions, strength of sincerity) (standard definition; five illocutionary points confirmed by review: assertives, directives, commissives, declarations, expressives). Axioms and laws govern success, satisfaction, and entailment between acts (reviews confirm "axioms and general laws"). [from abstract/standard account]
- **Captures.** The logical form of speech acts and when an act succeeds or is satisfied. Declarations are the acts that change institutional facts.
- **Limits.** An operator on *propositions*; speaker and hearer appear in the context of utterance and the conditions, not as slots of an algebra. There are illocutionary connectives (illocutionary denegation, conjunction of acts, conditional acts), so some composition exists within one utterance, but no theory of groups or of composition across turns.
- **Relevance.** Strongest precedent that "what people do to each other" can be written as operators F(P) with logical laws. Directly relevant: promise, command, request, declare, as base operators.

## 6. Deontic logic and normative positions

- Citations: SEP, "Deontic Logic" (https://plato.stanford.edu/archives/spr2006/entries/logic-deontic/ ; current entry at plato.stanford.edu/entries/logic-deontic/, not opened) and McNamara's supplement "Challenges in Defining Deontic Logic". Sergot, "Normative Positions", in *Handbook of Deontic Logic and Normative Systems* (2013) (https://www.doc.ic.ac.uk/~mjs/publications/NormPos_Handbook.pdf). S. Kanger, "Law and Logic", *Theoria* 38(3): 105-132, 1972; L. Lindahl, *Position and Change: A Study in Law and Logic*, Reidel, 1977; D. Makinson, "On the Formal Representation of Rights Relations", *Journal of Philosophical Logic* 15: 403-425, 1986. (The original pointer, arXiv:2110.04454, does not name these authors in its abstract; citations are given here from the standard record.)
- **Operands.** Propositions, and (in the Kanger-Lindahl line) agent-indexed propositions.
- **Operators.** Standard deontic logic: O (obligatory), P = not-O-not, F = O-not, with O a normal KD box (seriality: O p implies P p) (standard definition). Kanger-Lindahl: combine a deontic operator with an agency operator `Do_a` to enumerate the complete set of *normative positions* of one or two agents regarding a state of affairs: the formal analogue of Hohfeld's rights, duties, powers, liabilities (source: Sergot chapter abstract). Makinson and Sergot noted that the classical theory lacks directedness (to whom the duty is owed). [from abstract/standard account]
- **Captures.** Obligation, permission, rights; the exhaustive typology of two-party normative relations.
- **Limits.** Standard deontic logic has well-known paradoxes (SEP). Normative positions are a classification of relations, not an algebra of acts. Groups are rarely first-class.
- **Relevance.** Hohfeldian positions are the nearest existing *typology of dyadic social relations*. Directly useful as a candidate set of relation types, with the Makinson/Sergot directedness caveat.

## 7. Normative multi-agent systems (social laws; normative system games)

- Citations: Y. Shoham and M. Tennenholtz, "On the Synthesis of Useful Social Laws for Artificial Agent Societies (Preliminary Report)", AAAI-92, pp. 276-281 (https://mlanthology.org/aaai/1992/shoham1992aaai-synthesis); journal version "On social laws for artificial agent societies: off-line design", *Artificial Intelligence* 73(1-2): 231-252, 1995. T. Ågotnes, W. van der Hoek, M. Wooldridge, "Normative System Games", AAMAS 2007 (https://www.ifaamas.org/Proceedings/aamas07/html/pdf/AAMAS07_0042_3a31772ad28b437feed4e14c8c07a40f.pdf). Also Ågotnes, van der Hoek, Rodríguez-Aguilar, Sierra, Wooldridge, "On the Logic of Normative Systems" (Normative Temporal Logic, NTL), Dagstuhl 07122, 2007; IJCAI 2007 version (DOI 10.4230/DagSemProc.07122.24; identifier matches the volume's table of contents, checked 2026-10-29).
- **Operands.** Agent systems as transition systems / Kripke structures; agent goals as CTL formulae.
- **Operators.** A *social law* or *normative system* is a restriction of the transition relation: a set of forbidden transitions (source: Normative System Games abstract). Combining two norms is naturally the union of their forbidden-arc sets (my observation, not claimed by the source), but the paper requires a normative system to be *reasonable* (the remaining relation must stay total, so no state is left without a legal move), and the union of two reasonable systems need not be reasonable. So the reasonable norms form a down-closed family in the powerset of arcs, not a structure closed under union. [from abstract/standard account]
- **Captures.** Design and verification of norms; whether a normative system achieves goals, whether there exists a normative system that is a Nash implementation (NP-complete, source abstract; Pareto-efficiency checking is co-NP-complete).
- **Limits.** Agents are anonymous or abstract; norms apply to a whole system. Computational complexity focus.
- **Relevance.** Shows an operator structure on norms is workable. Not an algebra of interpersonal acts.

## 8. Coalition Logic and ATL

- Citations:
  - Marc Pauly, "A Modal Logic for Coalitional Power in Games", *Journal of Logic and Computation* 12(1): 149-166, 2002, DOI 10.1093/logcom/12.1.149 (Crossref).
  - Rajeev Alur, Thomas A. Henzinger, Orna Kupferman, "Alternating-Time Temporal Logic", *Journal of the ACM* 49(5): 672-713, 2002, DOI 10.1145/585265.585270 (https://www.cis.upenn.edu/~alur/Jacm02.pdf; https://en.wikipedia.org/wiki/Alternating-time_temporal_logic). Conference version FOCS 1997.
- **Operands.** Game frames / concurrent game structures; a finite set of agents; coalitions C as subsets of agents.
- **Operators.** Coalition Logic: modality `[C]φ` = coalition C has a joint action forcing the next state to satisfy φ. Semantics via effectivity functions: for each state, a family E(C) of sets of states that C can force (standard definition; source confirms "[C]φ" and the effectivity semantics). Axiomatisation complete, satisfiability PSPACE-complete (source). ATL: path modalities `<<C>>○φ`, `<<C>>□φ`, `<<C>>φ U ψ`; model checking linear in model and formula size (source). [from abstract/standard account]
- **Captures.** What groups can bring about, with exact conditions on coalitional power: Pauly's representation theorem says the effectivity functions of strategic games are exactly the *playable* ones (outcome-monotone, superadditive, regular, N-maximal, with liveness and safety) (standard). Superadditivity is the composition law: if disjoint C1 can force X and C2 can force Y, then C1 ∪ C2 can force X ∩ Y. Coalitions are just subsets (a Boolean lattice); the structure is in the effectivity function over them, not in the coalitions themselves.
- **Limits.** Capability only, no obligation, no relationship, no role, no attitude. Agents are interchangeable atoms apart from index. No operators that one agent applies to another.
- **Relevance.** Gives a rigorous operand algebra for *groups* (subsets, with ability structure). Reusable. Does not capture interaction between members.

## 9. Logic of agency: stit

- Citations: Belnap, Perloff, Xu, *Facing the Future: Agents and Choices in Our Indeterministic World*, OUP, 2001; Horty & Belnap, "The deliberative stit", *Journal of Philosophical Logic*, 1995. SEP "The Logic of Action" (https://plato.stanford.edu/ENTRIES/logic-action/ , confirms two strands: stit theory and dynamic logic).
- **Operands.** Agents, moments, histories in branching time.
- **Operators.** `[a stit: φ]`, agent a sees to it that φ, defined by agent-choice cells partitioning histories. Independence of agents' simultaneous choices is an axiom (standard definition). [from abstract/standard account]
- **Captures.** Responsibility, agency, what an agent ensures regardless of others.
- **Limits.** Individual agency in a modal framework. No theory of relations between agents beyond independence.
- **Relevance.** The most developed theory of the "agent brings about" primitive. Corrected in validation: Kanger-Lindahl does not build on stit (Kanger's Do/E operator predates it, 1957-72, and stit descends partly from Kanger and Pörn), and ATL comes from temporal logic and game structures, not stit; Coalition Logic and ATL have since been shown embeddable in stit variants (Broersen, Herzig, Troquard 2006).

## 10. Dynamic epistemic logic (public announcement; action models)

- Citations: J. A. Plaza, "Logics of public communications", *Proceedings of the 4th International Symposium on Methodologies for Intelligent Systems*, 1989, pp. 201-216; reprinted *Synthese* 158(2): 165-179, 2007, DOI 10.1007/s11229-007-9168-7. A. Baltag, L. S. Moss, S. Solecki, "The Logic of Public Announcements, Common Knowledge and Private Suspicions", TARK 1998, pp. 43-56; extended as CWI report SEN-R9922 (1999); reprinted in *Readings in Formal Epistemology*, Springer 2016, pp. 773-812 (https://ir.cwi.nl/pub/4497 ; https://scholarworks.iu.edu/dspace/items/091c4363-4700-4b17-8202-8e9daa850d04). Updated journal version: "Logics for Epistemic Actions: Completeness, Decidability, Expressivity", *Logics* 1(2): 97-147, 2023 (arXiv:2203.06744). SEP, "Dynamic Epistemic Logic" (https://plato.stanford.edu/ENTRIES/dynamic-epistemic/). van Ditmarsch, van der Hoek, Kooi, *Dynamic Epistemic Logic*, Springer (Synthese Library 337), 2007.
- **Operands.** Kripke models of multi-agent knowledge (worlds, one accessibility relation per agent).
- **Operators.** Public announcement `[φ]ψ`: ψ holds after the model is restricted to the worlds where φ holds. Action models (Baltag-Moss-Solecki): a model of events with preconditions and per-agent indistinguishability; the *product update* `M x A` is an operator on epistemic models (standard definition; abstract confirms announcements to subgroups, with suspicious outsiders as modalities). Action models themselves compose: BMS define a composition A;B of action models such that updating by A;B equals updating by A then B (up to bisimulation), and the language has nondeterministic choice; this is the standard "composition" result in DEL. [from abstract/standard account]
- **Captures.** Exactly the case "an act changes who knows what", including private and semi-private communication to subgroups and common knowledge in groups.
- **Limits.** Informational state only: no obligation, resources, power, relationship, or time-extended behaviour. Agents are indices.
- **Relevance.** The best existing example of *interactions as operators acting on a structured social state* with a real equational-ish theory (composition of action models). Strong precedent for the target form, for the informational dimension.

## 11. Social choice and judgement aggregation

- Citations: Kenneth Arrow, *Social Choice and Individual Values* (1951; https://en.wikipedia.org/wiki/Social_Choice_and_Individual_Values). Michael Morreau, SEP "Arrow's Theorem" and Christian List, SEP "Social Choice Theory" (bibliographies at https://philpapers.org/sep/arrows-theorem/ and https://philpapers.org/sep/social-choice/). Christian List and Philip Pettit, "Aggregating sets of judgments: An impossibility result", *Economics and Philosophy* 18(1): 89-110, 2002 (https://philarchive.org/rec/LISASO-3 ; https://researchonline.lse.ac.uk/id/eprint/704).
- **Operands.** Preference profiles (n-tuples of linear orders over alternatives); judgement sets (n-tuples of consistent sets of propositions).
- **Operators.** An aggregation function F: profile -> collective order / judgement set. The characterisation is axiomatic: unrestricted domain, weak Pareto, non-dictatorship, independence of irrelevant alternatives (SEP Arrow; list as also given in the Wikipedia article 'Social Choice and Individual Values', CC BY-SA 4.0). Impossibility results state that no F satisfies all axioms (Arrow; List-Pettit under "undemanding conditions", abstract). [from abstract/standard account]
- **Captures.** The axiomatic theory of collective decision over individuals; a precise statement of what group-level operations cannot be.
- **Limits.** One operation (aggregate) of one type; operands are anonymous votes. No roles, no relationships, no dynamics.
- **Relevance.** Models "the group decides" as a function on individual states, with proven constraints: a template for a group-level operator and for proving impossibility statements in the algebra.

## 12. Role and organisation models in multi-agent systems (MOISE+, OperA/OMNI)

- Citations:
  - Jomi F. Hübner, Jaime S. Sichman, Olivier Boissier, "MOISE+: towards a structural, functional, and deontic model for MAS organization", AAMAS 2002, pp. 501-502, DOI 10.1145/544741.544858; and "A Model for the Structural, Functional, and Deontic Specification of Organizations in Multiagent Systems", SBIA 2002, LNCS 2507, pp. 118-128 (https://hal-emse.ccsd.cnrs.fr/emse-00745177). Developed in "Developing organised multiagent systems using the MOISE+ model: programming issues at the system and agent levels", *IJAOSE* 1(3/4): 370-395, 2007, DOI 10.1504/IJAOSE.2007.016266. OperA itself: Virginia Dignum, *A Model for Organizational Interaction: Based on Agents, Founded in Logic*, PhD thesis, Utrecht, 2004.
  - J. Vázquez-Salceda and **F.** Dignum (Frank, not Virginia; corrected), "Modelling electronic organizations", *Multi-Agent Systems and Applications III* (CEEMAS 2003), LNAI 2691, pp. 584-593, DOI 10.1007/3-540-45023-8_56 (https://research.vu.nl/en/publications/modelling-electronic-organizations/). OMNI: V. Dignum, J. Vázquez-Salceda, F. Dignum, "A Model of Almost Everything: Norms, Structure and Ontologies in Agent Organizations", AAMAS 2004 (extended abstract, pp. 1498-1499); full version "OMNI: Introducing Social Structure, Norms and Ontologies into Agent Organizations", ProMAS 2004, LNCS 3346, pp. 183-200 (https://dspace.library.uu.nl/bitstream/handle/1874/11499/dignum_04_model_of_almost_everything.pdf).
- **Operands.** Roles, groups (with sub-groups), goals, plans, missions; in OperA: roles, scenes and landmarks in an interaction structure (Dignum 2004 thesis; OMNI builds on OperA and HARMONIA).
- **Operators.** None algebraic. Specification relations: role inheritance, compatibility, links (acquaintance, communication, authority) between roles; deontic relations binding a role to a mission with permission or obligation under time constraints (source: AAMAS abstract and SCITEPRESS 2004 paper as summarised). Group/role cardinalities. [from abstract/standard account]
- **Captures.** Static organisation structure with roles, authority and obligation links.
- **Limits.** Declarative specifications for engineering agent organisations, not an algebra; no compositional semantics for interactions between people; humans are not the modelling target.
- **Relevance.** The closest existing *operand set* (roles, groups, links, obligations) in engineering practice. The link types (authority, communication, acquaintance) are a ready list of relation primitives.

## 13. Process calculi and bigraphs

- Citations: Robin Milner, Joachim Parrow, David Walker, "A Calculus of Mobile Processes, I and II", *Information and Computation* 100(1): 1-40 and 41-77, 1992, DOI 10.1016/0890-5401(92)90008-4 and 10.1016/0890-5401(92)90009-5 (https://www.lfcs.inf.ed.ac.uk/reports/89/ECS-LFCS-89-85). Robin Milner, *The Space and Motion of Communicating Agents*, Cambridge University Press, 2009, DOI 10.1017/CBO9780511626661 (https://www.cl.cam.ac.uk/archive/rm135/Bigraphs-draft.pdf ; https://openlibrary.org/works/OL15173168W/The_Space_and_Motion_of_Communicating_Agents).
- **Operands.** pi-calculus: processes and names (channels). Bigraphs: a place graph (nesting forest, locality) superposed with a link graph (hypergraph connectivity), with interfaces.
- **Operators.** pi-calculus: parallel composition `P | Q`, restriction `(nu x)P`, prefix `x(y).P`, `x<y>.P`, replication `!P`, choice, with structural congruence and reaction rules (standard definition). Bigraphs: composition and tensor product of bigraphs as arrows between interfaces (a symmetric partial monoidal (pre)category), with an axiomatised term algebra (Milner, "Axioms for bigraphical structure", *MSCS* 2005), with reaction rules `r -> r'` giving a rewriting system (source: book summary describes Space = definitions and algebra, Motion = reactions, behavioural theory). [from abstract/standard account]
- **Captures.** Mobility, locality, who is connected to whom, concurrency. Bigraphs aim at spatial structure plus connectivity (Milner's motivation was ubiquitous computing, with examples of agents moving through buildings); reading them as a person-in-a-group-in-a-place with links is a natural reuse, not Milner's stated target. Corrected from "explicitly aim at ... social structure", which overclaimed.
- **Limits.** Designed for computing systems; applications to social settings are metaphor or modelling case studies. Semantics of mental states, norms and roles absent.
- **Relevance.** Of everything surveyed, bigraphs are the closest to the *form* the owner wants: a genuine algebra (with laws, composition, interfaces) plus reaction operators on a structure that natively has nesting (groups) and linking (relationships). It is worth a dedicated look. I did not find in this search a published bigraphical model of a human social group (search was not exhaustive).

## 14. Sheaf and category-theoretic models

- Citations:
  - Jakob Hansen and Robert Ghrist, "Opinion Dynamics on Discourse Sheaves", arXiv:2005.12798, May 2020 (https://arxiv.org/abs/2005.12798, DOI 10.48550/arXiv.2005.12798). Published in *SIAM Journal on Applied Mathematics* 81(5): 2033-2060, 2021, DOI 10.1137/20M1341088 (Crossref).
  - David I. Spivak and Robert E. Kent, "Ologs: A Categorical Framework for Knowledge Representation", *PLoS ONE* 7(1): e24274, 2012, DOI 10.1371/journal.pone.0024274 (https://pmc.ncbi.nlm.nih.gov/articles/PMC3269434 ; arXiv:1102.1889).
  - Role/position analysis, categorical: F. Lorrain and H. C. White, "Structural equivalence of individuals in social networks", *Journal of Mathematical Sociology* 1(1): 49-80, 1971 (category-theoretic, the origin of the structural-equivalence tradition); and N. Motamed, N. Otter, E. Roff, "Coalgebraic analysis of social systems", arXiv:2602.23211, Feb 2026 (role and positional analysis extended to hypergraphs via universal coalgebra, with a functoriality theorem). Both belong mainly to the neighbouring role-algebra cluster.
  - David L. Sallach, "Categorial Social Analysis", talk at CT2011, Coimbra (https://www.mat.uc.pt/~ct2011/talks/Sallach.pdf): by its own account "more a description of a research program than a presentation of results".
- **Operands.** Hansen-Ghrist: a graph with a *discourse sheaf*: a vector space ("opinion space") at each vertex and edge, with restriction maps along incidences. Ologs: a category whose objects are noun phrases/types and morphisms are functional relations ("aspects").
- **Operators.** Hansen-Ghrist: the sheaf Laplacian `L = delta^T delta` on 0-cochains (opinions); diffusion `dx/dt = -Lx`. Restriction maps model *how one person's opinion is presented to another*, including selective modulation and lying. Controllability, reachability, bounded-confidence and harmonic extension are studied (source). Ologs: functors for aligning ontologies (source). [from abstract/standard account]
- **Captures.** Hansen-Ghrist: a typed, linear-algebraic *operator on a social network*, with edge-specific transformations: the relation between two people is itself a map. Ologs: a categorical *schema* for entities and relations of any domain, social networks included.
- **Limits.** Hansen-Ghrist: one kind of state (opinion vectors, possibly over several topics), continuous-valued, and mostly linear. Corrected in validation: the maps are not always static (Sections 8-9 evolve the restriction maps, "learning to lie" and joint opinion-expression diffusion) and there are nonlinear, bounded-confidence and antagonistic variants. Ologs: a knowledge-representation method, with no dynamics and no theory of social action.
- **Relevance.** Hansen-Ghrist is the cleanest existing instance of "relationships are operators between people's states". Ologs offer a notation for operand types and relations. Neither gives an algebra of social acts.

## 15. Cooperative game theory as an algebra of interactions

- Citations: Lloyd S. Shapley, "A value for n-person games", in *Contributions to the Theory of Games II*, Annals of Mathematics Studies 28, Princeton University Press, 1953, pp. 307-317 (https://encyclopediaofmath.org/wiki/Shapley_value ; the doi.org link returned by search was to a different (Springer) record, so I do not rely on it). Shapley & Shubik 1954, power index (https://sk.sagepub.com/ency/edvol/embed/power/chpt/shapley-value).
- **Operands.** A cooperative game `(N, v)`: a finite player set N and characteristic function `v: 2^N -> R`, `v(empty) = 0`. Games with fixed N form a vector space.
- **Operators.** The Shapley value is a *linear operator* from games to payoff vectors, uniquely characterised by efficiency, symmetry, dummy player and additivity (standard definition; the phrase "defined by a set of axioms" is in the Encyclopedia of Mathematics "Shapley value" entry, encyclopediaofmath.org/wiki/Shapley_value, the first page cited above; page not re-checked). Formula: `phi_i(v) = sum over S in N\{i} of |S|!(n-|S|-1)!/n! * (v(S u {i}) - v(S))`. The Shapley-Shubik index is its restriction to simple (voting) games. [from abstract/standard account]
- **Captures.** The contribution of each member to a coalition, in an axiomatised and linear way. Games add and scale, so there is a genuine linear algebra of games.
- **Limits.** Transferable utility, one-shot, a single scalar value per coalition. No sequence, no communication, no role. Acts of individuals are folded into v.
- **Relevance.** A worked example of "a social quantity as an operator with axioms". Useful if the algebra later needs value attribution; peripheral to the notation question.

## 16. Institutions in the Goguen-Burstall sense (a note on naming)

- Citation: Joseph Goguen and Rod Burstall, "Institutions: Abstract Model Theory for Specification and Programming", *Journal of the ACM* 39(1): 95-146, 1992, DOI 10.1145/147508.147524 (https://courses.grainger.illinois.edu/cs522/sp2016/InstitutionsAbstractModelTheory.pdf ; https://ncatlab.org/nlab/show/institutions).
- This is *not* about social institutions. An institution is a category of signatures with sentence and model functors and a satisfaction relation invariant under change of notation. Relevance: a ready-made way to say "the same algebra over several logics" and to move between them (e.g. a deontic logic, a counts-as logic, and an epistemic logic as institutions with morphisms). Worth knowing about as a possible *integration device* if the algebra ever has to combine several of the logics above. Include only for disambiguation, since the term collides with Ostrom's usage.

---

## What this cluster already covers

- **Rules as structured statements**: ADICO / IG 2.0, with sanction and condition.
- **Role / status assignment** (counts-as): formalised in modal and conditional logics.
- **Speech acts as operators on propositions**: Searle-Vanderveken, with success and satisfaction laws.
- **Obligations, permissions, and the typology of two-party normative relations** (Hohfeld via Kanger-Lindahl-Makinson-Sergot).
- **Group ability**: Coalition Logic effectivity functions and ATL, including an exact algebra (monotone, superadditive) of coalitional power.
- **Information change as operator on a social model**: public announcement, action models, product update.
- **Group decision as a function on individual states**, with impossibility theorems.
- **Norms as operators on system behaviour** (restrictions of transitions), with compliance analysis.
- **Organisation structure in engineering practice**: roles, groups, authority links, missions (MOISE+, OperA).
- **A real algebra of structure and reaction**: bigraphs, with nesting and linking.
- **A relationship as an operator between persons' states**: Hansen-Ghrist (for opinion only).
- **Value attribution to members of a coalition**: Shapley, linear and axiomatic.

## What it does not

Stated bluntly:

1. **No single typed algebra.** Nothing here has one carrier of people, roles and groups with a closed set of operators for what they do to each other and equational laws. Each system formalises one slice (knowledge, ability, obligation, status, opinion, value) in its own logic.
2. **Logics, not algebras.** Most work is modal logic with Kripke-style semantics. "Operators" means modal connectives or state-transformers. The exceptions with algebraic character are bigraphs, action-model composition, sheaves, and cooperative games.
3. **Agents are atoms.** In coalition logic, ATL, DEL, stit and social choice, an agent is an index. Persons with relations to one another (kin, authority, friendship) are not operands. Only MOISE+/OperA and Hansen-Ghrist give relations real structure, and the first is engineering specification while the second covers only opinions.
4. **Dyadic relations are classified, not composed.** Hohfeld positions list the possible relations; no work here gives a calculus where relations compose (A's relation to B composed with B's to C) as in relation algebra.
5. **No combined dimensions.** No framework puts knowledge, obligation, ability and status in one operator calculus. Goguen-Burstall institutions are a candidate integration device but I found no social use of them.
6. **Humans appear as simplified agents.** No treatment of the mechanics of an actual group (hierarchy, norm enforcement, reciprocity, exclusion) as operators, apart from sanction fields in ADICO.
7. **Cluster-boundary caveat.** Kinship algebra, social network role algebra (White-Boorman-Breiger, semigroups of relations), sociological theory and anthropology are outside this cluster and probably contain the closest *algebraic* prior art (relation semigroups, kinship algebra). This survey does not cover them.

**Bottom line for the owner:** the premise "not novel" is correct for the components and the individual operator types (speech acts, announcements, coalitional power, status assignment, norms). It is not established for the unification. Within this cluster, the nearest structural precedents for the *form* are bigraphs (algebraic, reactive, nested) and sheaves on graphs (relations as operators); the nearest for the *content* are Hohfeld/Kanger-Lindahl positions and illocutionary logic.

---

## Unconfirmed

Resolved in validation (2026-10-29) and removed from this list: Grossi et al. 2006 JLC, Pauly 2002 pages, Frantz & Siddiki DOI, Hansen & Ghrist journal reference, Hübner et al. IJAOSE, OperA landmarks, Plaza 1989, Belnap et al. 2001 and Horty & Belnap 1995, Lorrain & White, the coalgebra preprint, Sallach. Details in the log below.

- **Any bigraphical or process-calculus model of a human social group**: not searched for in validation either; absence is not evidence of non-existence (Calder, Sevegnani and colleagues have bigraph models of human/physical spaces that would be the place to look).
- **Institutional Grammar's treatment of nesting/combination under IG Logico**: described from the codebook overview only; whether it defines compositional operators remains unchecked.
- **Plaza 1989 original page range (201-216)**: the 2007 *Synthese* reprint is confirmed by Crossref; the ISMIS proceedings pages are the standard citation but were not seen in a record.

## Missing from this cluster (listed, not researched)

- **Hohfeld**, "Some Fundamental Legal Conceptions as Applied in Judicial Reasoning", *Yale Law Journal* 1913/1917: the source of the positions in section 6, cited only indirectly above.
- **Pörn**, *Action Theory and Social Science* (1977): agency plus *influence* operators of one agent on another; a direct precedent for operators between people.
- **Singh's social commitments** (e.g. "An ontology for commitments in multiagent systems", *AI and Law* 1999) and the commitment-protocol line (Fornara & Colombetti; Yolum & Singh): directed C(debtor, creditor, antecedent, consequent) with create/discharge/cancel/release/delegate/assign operations. Arguably the closest thing in this cluster to typed dyadic operators with a life cycle; its absence is the most important gap.
- **Joint intention and shared agency**: Cohen & Levesque (1990), Levesque, Cohen & Nunes (1990), Grosz & Kraus SharedPlans (1996), Bratman, Tuomela; group attitudes as operands.
- **Electronic Institutions** (Esteva, Rodríguez-Aguilar, Sierra, Noriega, ISLANDER, 2001-) and **Artikis, Sergot & Pitt**, "Specifying norm-governed computational societies", *ACM TOCL* 2009: executable institutions with roles, scenes, powers.
- **Input/output logic** (Makinson & van der Torre 2000) and Boella & van der Torre's normative MAS work: norms as operators on sets of formulas, with an algebraic flavour.
- **Logics of social software and games**: Parikh, "Social Software" (*Synthese* 2002); Pauly's thesis *Logic for Social Software* (2001); van Benthem, *Logic in Games* (2014); Strategy Logic.
- **Lorini, Herzig and colleagues** on logics of institutional/group acceptance and trust, and Horty, *Agency and Deontic Logic* (2001).

## Validation log (2026-10-29)

Method: bibliographic details checked against Crossref, DOI records, publisher/repository pages and abstracts; formal claims checked against those sources (full text of Normative System Games and Hansen-Ghrist read in part) and standard mathematical knowledge. Nothing was found fabricated.

1. Crawford & Ostrom 1995: ✎ corrected — norms are ADIC, not "AICO"; Siddiki et al. 2011 given a full citation.
2. Frantz & Siddiki IG 2.0: ✎ corrected — volume/pages 99(2): 222-247 added, DOI confirmed; book full title and year. Codebook arXiv ✓.
3. Searle (1969/1995/2010/2006): ✎ corrected — added that the formula originates in *Speech Acts* and that Searle 2010 admits freestanding status functions (no X), weakening "counts-as" as the general form.
4. Jones & Sergot 1996: ✎ corrected — pages 427-443 per DOI 10.1093/jigpal/4.3.427 (file had 429-445 as majority). Grossi et al. JLC 2006: ✓ (Crossref; moved out of Unconfirmed). JAL 2008, DEON 2006, ICAIL 2005, Dagstuhl: ✓. ✎ "counts-as is not transitive" was wrong for Jones-Sergot (transitive, not reflexive); middle reading relabelled "proper contextual classification".
5. Searle & Vanderveken 1985: ✓ (seven components, five points correct); ✎ limits softened — illocutionary connectives give some within-utterance composition.
6. Deontic logic / normative positions: ✓ SEP and Sergot chapter; ✎ Kanger 1972, Lindahl 1977, Makinson 1986 given direct citations (the arXiv pointer does not name them); SDL stated as KD.
7. Shoham & Tennenholtz 1992/1995: ✓ (journal pages added). Normative System Games 2007: ✎ corrected — NP-complete problem is *existence* of a normative system that is a Nash implementation, not "whether compliance is a Nash equilibrium"; the "set union is a genuine algebra" observation corrected for the reasonableness constraint (union not closed). "On the Logic of Normative Systems": ✓, authors added.
8. Pauly 2002: ✓ (pages and DOI confirmed via Crossref). ATL 2002: ✓. ✎ effectivity-function properties completed (playability); "coalitions form a lattice and ability composes by union" restated as superadditivity.
9. stit (Belnap, Perloff, Xu 2001; Horty & Belnap 1995 JPL 24(6): 583-644): ✓ confirmed via Crossref. ✎ corrected — the claim that Kanger-Lindahl and ATL "build on" stit is historically wrong.
10. DEL (Plaza; BMS; Logics 2023; van Ditmarsch et al.; SEP): ✓; ✎ added TARK 1998, *Synthese* reprint, *Logics* 1(2): 97-147; action-model composition stated precisely.
11. Arrow 1951; List & Pettit 2002: ✓; ✎ "the algebra of collective decision" softened to "axiomatic theory".
12. MOISE+ (AAMAS 2002, SBIA 2002, IJAOSE 2007): ✓ with full IJAOSE title and DOI. Vázquez-Salceda & Dignum: ✎ corrected — co-author is Frank Dignum, not Virginia; CEEMAS 2003, LNAI 2691. OMNI: ✎ full title and venues (AAMAS 2004; ProMAS 2004). OperA landmarks: ✓ via Dignum 2004 thesis.
13. Milner, Parrow, Walker 1992: ✓ with DOIs. Milner 2009: ✓. ✎ "bigraphs explicitly aim at social structure" overclaimed; algebraic structure stated more precisely.
14. Hansen & Ghrist: ✓ SIAM J. Appl. Math. 81(5): 2033-2060, 2021. ✎ corrected — maps are not always static, opinion spaces are multi-topic, nonlinear variants exist. Spivak & Kent 2012: ✓. Lorrain & White 1971: ✓ (citation supplied). Motamed, Otter, Roff 2026: ✓. Sallach CT2011: ✓ (slides read; research programme, no results).
15. Shapley 1953; Shapley & Shubik 1954: ✓ (axioms and formula correct).
16. Goguen & Burstall 1992: ✓.
Summary and "What it does not": ✓ broadly sound; the omission of commitments (Singh) weakens point 3/4 ("only MOISE+/OperA and Hansen-Ghrist give relations real structure") — commitments are directed, structured dyadic relations.

Counts (per cited work, about 45): ✓ 21 confirmed as written, ✎ 24 corrected or completed (citation details or formal claims), ? 0 works unconfirmed (3 residual detail items listed above), ✗ 0 removed.

**Verdict.** The bibliography is sound: every work exists, and the errors were page ranges, a wrong co-author, and missing venues. The formal sketches are mostly right but carried several confident technical errors (ADICO norm type, stit genealogy, Normative System Games' complexity result and the union "algebra", Hansen-Ghrist's "static linear" maps, counts-as transitivity) that would have misled the algebra's notes; after correction it is usable as a map, while the omission of Singh-style commitments and Pörn's influence operators means its "nobody has operators between people" conclusion is stated more strongly than the cluster supports.

## Licences of quoted and transcribed material (2026-10-30)

Audit result for this file: no passage is long enough to need removal or shortening; all quotation is a short phrase. Equations and axiom lists are restated, not copied. No tables or datasets are transcribed.

- Wikipedia, "Social ontology" (section 3): CC BY-SA 4.0. Used as a verification source; one gloss on collective acceptance follows its wording and is now marked.
- Wikipedia, "Alternating-time temporal logic" (section 8): CC BY-SA 4.0. Cited only. Audit flag "check": the ATL description is attributed to the Alur-Henzinger-Kupferman paper and the standard definition, so no change was made; no wording is known to come from the article.
- Wikipedia, "Social Choice and Individual Values" (section 11): CC BY-SA 4.0. Cited; the Arrow axiom list may follow it, now marked.
- Encyclopedia of Mathematics, "Shapley value" (section 15): not determined; publisher copyright presumed. Six-word phrase quoted ("defined by a set of axioms"), page now named. The Shapley formula is a restated equation.
- SAGE, "Shapley-Shubik" power-encyclopedia entry (section 15): not determined; publisher copyright presumed. Cited only.
- nLab, "institutions", and Goguen and Burstall 1992 (section 16): nLab licence not determined; publisher copyright presumed for the JACM paper. Audit flag "check": the definition is a restated standard definition in our own words, not in quotation marks; text left unchanged.
- Stanford Encyclopedia of Philosophy entries (Arrow's theorem, Deontic Logic, Logic of Action): not determined; publisher copyright presumed. Cited and paraphrased only, no quotation.
- Spivak and Kent, "Ologs", PLoS ONE 7(1): e24274 (section 14): CC BY (PLoS ONE open access), not rechecked on the page. Cited; one short descriptive phrase only.
- Hansen and Ghrist, arXiv:2005.12798; Frantz and Siddiki codebook, arXiv:2008.08937; Motamed, Otter and Roff, arXiv:2602.23211: arXiv licence per paper not determined; copyright presumed. Cited and described; short phrases at most.
- Sallach, CT2011 talk (section 14): not determined; copyright presumed. One short quotation ("more a description of a research program than a presentation of results", under 60 words), attributed.
- All other journal, book and conference sources (Crawford and Ostrom, Searle, Jones and Sergot, Grossi et al., Pauly, Belnap et al., Plaza, Baltag et al., Milner, Shapley, Arrow, List and Pettit, and others): not determined; publisher copyright presumed. Cited by bibliographic record, described in our own words, with at most short quoted terms.
