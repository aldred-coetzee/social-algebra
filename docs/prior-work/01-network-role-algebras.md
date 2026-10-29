# Prior work 01: algebraic models of social networks and role structure

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: the network role-algebra tradition.

**Summary of the tradition.** From 1971 onward, a school of mathematical sociologists (White, Lorrain, Boorman, Breiger, Pattison, Boyd, Bonacich, Winship, Mandel, Borgatti, Everett, Doreian) has done much of what social-algebra proposes. Its operands are actors, partitioned into positions. Its basic operators are the kinds of tie between actors (friend-of, boss-of, kin-of). Ties compose as binary relations, and the compound relations ("friend of a boss of") form a semigroup under composition. A *role* is an element of that semigroup, or a class of its elements. Ties from a position to a position form a blockmodel. Homomorphisms between graphs and between semigroups reduce a large network to a small "role structure". The tradition has proved theorems about when such reductions are legitimate (structural, automorphic and regular equivalence, the lattice of equivalences, Galois lattices for person/group duality). Its weaknesses are the same throughout. It is purely relational and almost entirely static. Its operations are composition of ties, plus Boolean union and inclusion: Pattison's mature form is a *partially ordered* semigroup, not a bare semigroup. It has no action operators that change a network. *(Validation note: the kinship branch of the same school, White 1963 and Boyd 1969, does have operators acting on groups. They are permutations of clans, and this survey omits them. See "What it does not cover".)* Its operands are indivisible nodes with no internal state. It is descriptive: it is fitted to an observed network and does not generate predictions of interaction dynamics.

**Method note.** Every entry below has a source I located by search or fetch in this session. The "Verified" line says what was actually seen (publisher page, library record, abstract) and what rests only on secondary citation. Descriptions of mathematical structure marked *(standard account)* come from the field's standard definitions, as I know them, and I did not read the full text of the paper in question. Treat those as to-be-checked against the paper before you rely on them. The abstracts I did read are paraphrased. Full texts were mostly paywalled.

---

## 1. Lorrain & White 1971: structural equivalence

**Citation.** Lorrain, F. & White, H. C. (1971). Structural equivalence of individuals in social networks. *Journal of Mathematical Sociology* 1(1), 49-80. DOI 10.1080/0022250X.1971.9989788.

**Verified.** The DOI, volume and pages came from search results. A search result also quotes the definition (two objects are structurally equivalent if, for any morphism and any object, they relate to that object in the same ways). Several secondary sources cite it as the origin of structural equivalence and of blockmodeling (Wikipedia's *Blockmodeling* page says so). The T&F page returned 403, so I did not read the abstract at the source. A copy of the PDF exists on a university course site: https://ucilnica.fri.uni-lj.si/pluginfile.php/1147/course/section/1510/Lorrain%20and%20White%20-%20Structural%20equivalence%20of%20individuals%20in%20social%20networks%2C%201971.pdf. I did not read it. *(Validation: Crossref confirms the DOI, volume and pages. It also records a reprint in S. Leinhardt (ed.), *Social Networks: A Developing Paradigm* (Academic Press 1977), pp. 67-98.)*

- **Operands.** Individuals (objects) in a multi-relational network. In the paper's own formulation the network is a category-like structure of objects and morphisms (relations).
- **Operators.** Relations as morphisms. Their compositions give compound relations, which form a semigroup *(standard account)*. The paper uses a category-theoretic idiom ("morphism", "functorial mapping"). One search hit quotes a "functorial mapping" description, but I could not tell whose paper that was, so I do not rely on it.
- **What it captures.** Two individuals are structurally equivalent if they have identical ties to every other object. Equivalence classes of individuals are the positions. The paper presents this as the mathematical form of the social-role concept.
- **Limits.** Structural equivalence is very strict: it requires the *same* alters, not merely alters of the same kind. This motivated automorphic and regular equivalence (below). It is purely relational and static.
- **Relevance.** This is the founding paper for the entire tradition. A person reading "operators and operands" in the owner's brief and reaching for relations as operators is reinventing its starting point.

## 2. White, Boorman & Breiger 1976 (Part I) and Boorman & White 1976 (Part II)

**Citations.**
- White, H. C., Boorman, S. A. & Breiger, R. L. (1976). Social structure from multiple networks. I. Blockmodels of roles and positions. *American Journal of Sociology* 81(4), 730-780. DOI 10.1086/226141.
- Boorman, S. A. & White, H. C. (1976). Social structure from multiple networks. II. Role structures. *American Journal of Sociology* 81(6), 1384-1446. DOI 10.1086/226228.

**Verified.** Part I: abstract and DOI read at https://experts.arizona.edu/en/publications/social-structure-from-multiple-networks-i-blockmodels-of-roles-an/. Part II: volume, pages and DOI come from a search result citing the academia.edu copy (https://www.academia.edu/93734875/Social_Structure_from_Multiple_Networks_II_Role_Structures). The page returned 403 on fetch, so the DOI has one secondary source. Part II's content is taken from Part I's abstract (which says Part II shows how role structures are derived from the blockmodels) and from a later reply by Boorman & Arabie (see section 6).

- **Operands.** Part I: actors, partitioned into positions, observed over several kinds of tie (up to 8 tie types, 15 time periods, 100 people in the case studies). Part II: positions, and the tie types between them.
- **Operators.** Part I: the observed ties (binary relations on actors), grouped into blocks. A blockmodel is a reduced "image" matrix per tie type, with entries 0 or 1 by a density criterion (zeroblock / oneblock). Part II: the images are multiplied with Boolean matrix multiplication. Closing the image matrices under Boolean product gives a finite semigroup, the *role structure*. This is the standard account, and it is correct. *(Validation correction: the role structure is a homomorphic image of the full network's semigroup only under conditions. It is one when the blocking is a structural equivalence (a "lean fit") or a regular equivalence (White & Reitz 1983). It is not one in general for blockmodels with a density threshold or a "fat fit". The original sentence stated it unconditionally.)* Boorman & White also derive homomorphic reductions of the semigroup to a smaller one, and the 1980 reply (Boorman & Arabie, AJS; reprinted 1981) says their comparison of two structures uses the lattice join of congruences of a free semigroup (the "joint reduction").
- **What it captures.** What the compound ties of one group look like once actors are collapsed to positions, and which compositions are equivalent. It gives a calculus of "my friend's enemy is my enemy"-type identities for a particular group, with six case studies per the summary.
- **Limits.** It is a descriptive fit to one observed group. Each tie type is binary. Semigroup size explodes with the number of tie types. The result is sensitive to the density threshold for blocks, as the critique literature (Bonacich, Winship & Mandel) points out.
- **Relevance.** This is the nearest match to "operators and operands". If the owner's meaning is "ties compose, and the composition table is the algebra", it already exists here, 50 years ago.

## 3. White & Reitz 1983: regular equivalence; Borgatti & Everett 1989: lattice of regular equivalences

**Citations.**
- White, D. R. & Reitz, K. P. (1983). Graph and semigroup homomorphisms on networks of relations. *Social Networks* 5(2), 193-234. DOI 10.1016/0378-8733(83)90025-4 (Crossref).
- Borgatti, S. P. & Everett, M. G. (1989). The class of all regular equivalences: algebraic structure and computation. *Social Networks* 11(1), 65-88. DOI 10.1016/0378-8733(89)90018-X (Crossref).

**Verified.** White & Reitz: details and abstract text from search results (secondary: R `blockmodeling` package docs, Hanneman's online text, and others). No fetch of the paper itself. Borgatti & Everett: the abstract quoted in search results ("we explore the structure of the set of all regular equivalences (White and Reitz 1983) proving that it forms a lattice"); a PDF was claimed at https://webarchive.lib.cuhk.edu.hk/20210324140943mp_/http:/www.cse.cuhk.edu.hk/~cslui/CMSC5734/borgatti_1989_equivalences.pdf. I did not read it. *(Validation: when fetched, that URL returns an HTML page, not a PDF.)*

- **Operands.** Actors (points of a multigraph), then the relations themselves.
- **Operators.** Part one: graph homomorphisms on actors. Part two: the semigroup of relations under composition, and its reductions. The aim was to formalise social role as "regularities in network patterns", and the paper links the two kinds of homomorphism.
- **Regular equivalence.** Two actors are equivalent when they are "equally related to equivalent others". Borgatti & Everett prove that the set of regular equivalences forms a lattice. *(Validation correction: the maximal regular equivalence was already computable by White & Reitz's method (REGE). Borgatti & Everett's contribution is a way to compute **other** elements of the lattice, and it can also recover structural, automorphic and Winship-Pattison equivalence. The original credited them with the maximal one.)* Borgatti, Boyd & Everett (1989, "Iterated roles") show that a regular equivalence of a regular equivalence is regular.
- **Limits.** Regular equivalence says nothing about the *content* of the relation, and it is defined on binary, unsigned, static ties. *(Validation correction: the original said "many networks admit only the trivial regular equivalences". That is backwards. The trouble is that regular equivalences are plentiful and the maximal one is often uninformative. In an undirected graph with no isolates, putting everyone in one class is already regular. Exact regularity also seldom holds in real data: Boyd & Jonas 2001, "Are social equivalences ever regular?", *Social Networks* 23(2), 87-123.)* Regular equivalence is a property of a given graph, not an operation that acts on it.
- **Relevance.** Defines "role" as a class of actors whose neighbours are similar. This is close to the sense in which the owner wants roles as operands. The lattice result gives an exact algebraic structure on the *space of possible role assignments*, not on interactions.

## 4. Breiger & Pattison 1986: cumulated social roles; Pattison 1993: *Algebraic Models for Social Networks*

**Citations.**
- Breiger, R. L. & Pattison, P. E. (1986). Cumulated social roles: the duality of persons and their algebras. *Social Networks* 8(3), 215-256. DOI 10.1016/0378-8733(86)90006-7.
- Pattison, P. E. (1993). *Algebraic Models for Social Networks*. Structural Analysis in the Social Sciences 7. Cambridge University Press. ISBN 0521365686. DOI 10.1017/CBO9780511571220.
- Pattison, P. E. & Wasserman, S. (1995). Constructing algebraic models for local social networks using statistical methods. *Journal of Mathematical Psychology* 39(1), 57-72. DOI 10.1006/jmps.1995.1005. *(Added in validation from Crossref. It was in Unconfirmed.)*
- Pattison, P. E., Wasserman, S., Robins, G. & Kanfer, A. M. (2000). Statistical evaluation of algebraic constraints for social networks. *Journal of Mathematical Psychology* 44(4), 536-568. DOI 10.1006/jmps.1999.1261. *(Added in validation from Crossref. It was in Unconfirmed.)*

**Verified.** Breiger & Pattison: citation and abstract at https://experts.arizona.edu/en/publications/cumulated-social-roles-the-duality-of-persons-and-their-algebras/. Pattison: preface and chapter list read at https://www.cambridge.org/core/books/abs/algebraic-models-for-social-networks/preface/5FD33FC09D80601B325C15C7F2A9BF36. Chapters: 1 Algebraic representations for complete social networks; 2 ... for local social networks; 3 Comparing algebraic representations; 4 Decompositions of network algebras; 5 An analysis for complete and local networks; 6 Time-dependent social networks; 7 Algebras for valued networks; 8 Issues in network analysis. Appendices cover mathematical terms and proofs. Page count differs between sources (310 or 336); I did not settle which. The preface does not itself name semigroups or lattices, so the structure claims below come from the chapter titles and the abstracts.

- **Operands.** Actors considered each in turn as *ego*, so the object is the local network around one person. The "cumulated person hierarchy" is built from each ego's ties.
- **Operators.** Compound relations as before (a semigroup of relations). Breiger & Pattison derive graph and semigroup homomorphisms for three algebras of 81, 43 and 93 elements. A person's algebra is paired with the persons it describes: the *duality of persons and their algebras*. Pattison's book extends this to *local role algebras* for ego-centred networks, to time-dependent networks (ch. 6) and to valued networks (ch. 7). Pattison's later statistical work is Pattison & Wasserman 1995 and Pattison et al. 2000 (cited above). *(Validation: in Pattison's treatment the algebra is a **partially ordered** semigroup, with relations ordered by inclusion, and this order is central to her comparisons and decompositions. The survey should not reduce it to "a semigroup".)*
- **What it captures.** The structure of compound ties from the standpoint of each person, with Padgett's Florentine data as the worked example (confirmed in the 1986 abstract). *(Validation correction: the original also said the 1986 paper "supplies a statistical way to say which compound relations hold". The 1986 abstract says nothing of the kind. That is the 1995/2000 statistical work.)*
- **Limits.** Still compound-tie algebra: the operators are ties and their composition. The valued-network and time chapters extend the *data*, but the algebra remains a descriptive summary of an observed network, not a transition system that generates new states. The abstract states the tradition's two lines (role from the individual actor's viewpoint, and the link between graph and semigroup homomorphisms) as its subject.
- **Relevance.** This is the highest-priority book to read for the owner: it is the most developed statement of "an algebra whose operands are actors and whose operators are their ties". The ego-centred "local role algebra" is precisely the actor-as-origin viewpoint.

## 5. Pattison & Breiger 2002: lattices and dimensional representations; Breiger 1974: duality of persons and groups

**Citations.**
- Breiger, R. L. (1974). The duality of persons and groups. *Social Forces* 53(2), 181-190. DOI 10.1093/sf/53.2.181.
- Pattison, P. E. & Breiger, R. L. (2002). Lattices and dimensional representations: matrix decompositions and ordering structures. *Social Networks* 24(4), 423-444. DOI 10.1016/S0378-8733(02)00015-1.

**Verified.** Breiger 1974: bibliographic details and description from search results (OUP issue index, and secondary descriptions). Pattison & Breiger 2002: citation, DOI and abstract at https://experts.arizona.edu/en/publications/lattices-and-dimensional-representations-matrix-decompositions-an/.

- **Operands.** Two linked sets: persons and the groups (or organisations and agendas) they belong to, as a two-mode incidence matrix.
- **Operators.** Multiplying the incidence matrix by its transpose gives person-by-person or group-by-group co-membership. This is a matrix product, not a semigroup of compound ties. The 2002 paper compares two representations of the dual structure, vector space (dimensional) and lattice, and argues they are fundamentally similar.
- **What it captures.** The Simmelian duality: groups defined by their members and members by their groups. It converts two-mode data to one-mode networks.
- **Limits.** Static affiliation. No operators acting on people or groups.
- **Relevance.** Directly relevant to the owner's "people, roles and groups" as *co-operands*. It treats persons and groups symmetrically, which the semigroup tradition does not.

## 6. Bonacich, Boorman & Arabie, Winship & Mandel: the critique and repair of the semigroup approach

**Citations.**
- Bonacich, P. (1980). The "common structure semigroup," a replacement for the Boorman and White "joint reduction". *American Journal of Sociology* 86(1), 159-166. DOI 10.1086/227208. *(Venue confirmed in validation via Crossref.)*
- Boorman, S. A. & Arabie, P. (1980). Algebraic approaches to the comparison of concrete social structures represented as networks: reply to Bonacich. *American Journal of Sociology* 86(1), 166-174. DOI 10.1086/227209. *(Validation correction: this is the original publication. The NCJRS item NCJ 88434, dated 1981, is a reprint as Appendix C of P. Arabie, *Blockmodel Techniques for Criminal Justice Research*.)*
- Winship, C. & Mandel, M. (1983). Roles and positions: a critique and extension of the blockmodeling approach. In S. Leinhardt (ed.), *Sociological Methodology* 14 (1983-1984), 314-344. San Francisco: Jossey-Bass. DOI 10.2307/270911 (Crossref; end page from a secondary reference list).
- Related: McConaghy, M. J. (1981), "The common role structure: improved blockmodeling methods applied to two communities' elites", *Sociological Methods & Research* 9(3), 267-285. Pattison, P. E. (1981), "Equating the 'joint reduction' with blockmodel common role structure: a reply to McConaghy", *SMR* 9(3), 286-302. Both confirmed via Crossref.

**Verified.**
- Boorman & Arabie: the NCJRS abstract at https://www.ncjrs.gov/App/Publications/abstract.aspx?ID=88434. It states that blockmodel algebras lie in the congruence lattice of a free semigroup, that comparison uses the lattice union (the "joint reduction"), and that the union is also a semigroup. The reply addresses Bonacich's objection that the joint reduction can fail to be generator-preserving.
- Bonacich: the original survey found only its existence. Validation found it in Crossref (above). The 1981 Pattison paper the survey cited is a reply to **McConaghy**, not to Bonacich, although it cites Bonacich.
- Winship & Mandel: Crossref confirms the venue, volume 14 and start page 314. Borgatti & Everett (1992) cite it among critiques that blockmodel interpretations do not capture role as well as position. *(Validation: the "extension" in the title is a local, role-set-based role equivalence, in which each actor is characterised by the compound relations it sends. Ostoic's R `multiplex` work builds directly on it. It is more than a critique.)*

- **Operands/operators.** As section 2: semigroups of compound relations, now compared and combined across several groups (lattice of congruences).
- **What it captures.** How to compare the role structures of *different* populations, via a common reduction. The congruence-lattice framing makes the space of role structures itself an algebraic object.
- **Limits.** The central dispute is that the joint reduction can destroy the generators (the basic ties), so the "common structure" has no sociological reading. Winship & Mandel's critique, as cited, is that the classical approach captures *position* well and *role* poorly.
- **Relevance.** A warning of the problem the owner will meet: composing relations across groups does not automatically yield a meaningful common algebra.

## 7. Boyd 1991: *Social Semigroups*

**Citation.** Boyd, J. P. (1991). *Social Semigroups: A Unified Theory of Scaling and Blockmodelling as Applied to Social Networks*. Fairfax, VA: George Mason University Press. ISBN 0913969346. xii + 267 pp.

**Verified.** The library record details (publisher, ISBN, page count, LCCN 90025957) come from a search-result summary of catalogue entries (e.g. https://quaibranly.fr/en/explore-collections/base/Bibliography/action/show/notice/000068315-social-semigroups-a-unified-theory-of-scaling-and-blockmodelling-as-applied-to-social-networks). The ECU catalogue page returned 503. Boyd's UC Irvine profile (https://faculty.sites.uci.edu/johnboyd/) says his current work fits discrete semigroups to network data by simulated annealing. I did not read the book.

- **Operands.** Network data (matrices of relations) fitted by a semigroup.
- **Operators.** Semigroup elements, with the product of the semigroup standing in for composition of relations. The subtitle says "scaling" (embedding in a metric space) is unified with blockmodelling. How exactly he unifies them I could not verify.
- **What it captures.** The fit of an *abstract* semigroup to data, by an optimisation method, so the algebra is estimated rather than read off from a partition.
- **Limits.** Descriptive fit. Again a static semigroup of relations.
- **Relevance.** Moderate. It is the tradition's attempt to treat the semigroup as the primary object, which is nearer the owner's "the algebra is the goal" than the blockmodel papers are.

## 8. Doreian, Batagelj & Ferligoj 2005: generalized blockmodeling

**Citation.** Doreian, P., Batagelj, V. & Ferligoj, A. (2005). *Generalized Blockmodeling*. Structural Analysis in the Social Sciences 25. Cambridge University Press. ISBN 0521840856. xv + 384 pp.

**Verified.** Details from search results (a bookseller, a library record, and Žiberna's paper describing the book's ideas). *(Validation: Open Library confirms CUP and ISBN 0521840856, but records the publication date as November 2004. "2005" is the conventional citation year.)* I did not read the book or a publisher abstract.

- **Operands.** Actors in a network (one- or two-mode, binary or valued), assigned to positions.
- **Operators.** None algebraic as such. It is an *optimisation framework*: pick a criterion function measuring how far each block departs from an "ideal block" type (complete, null, row-regular, column-regular, and others), then search over partitions. Structural and regular equivalence become special cases of ideal-block patterns. A chapter on balance theory in signed networks uses semirings (a Cambridge Core chapter title and excerpt, not read in full).
- **What it captures.** Positions and the pattern of block types between them, fitted directly to data without transforming it.
- **Limits.** It is a clustering method, not an algebra of actions. The semigroup is no longer the centre of the account.
- **Relevance.** Useful for how to *fit* a role model to observed data, if the algebra later has to be estimated. Not an answer to the algebra itself.

## 9. Galois lattices and formal concept analysis

**Citations.**
- Freeman, L. C. & White, D. R. (1993). Using Galois lattices to represent network data. *Sociological Methodology* 23, 127-(146?). DOI 10.2307/271008. *(Validation: Crossref confirms the authors, volume and start page. The end page is unconfirmed.)*
- Freeman, L. C. (1996). Cliques, Galois lattices, and the structure of human social groups. *Social Networks* 18(3), 173-187. DOI 10.1016/0378-8733(95)00271-5 (Crossref).
- Freeman, L. C. & Duquenne, V. (1993). A note on regular colorings of two mode data. *Social Networks* 15(4), 437-441. DOI 10.1016/0378-8733(93)90016-E (Crossref).
- Wille, R. (1982). Restructuring lattice theory: an approach based on hierarchies of concepts. In I. Rival (ed.), *Ordered Sets*, 445-470. Dordrecht: Reidel/Springer. (Reprinted in LNCS 5548, 2009, 314-339.)
- Ganter, B. & Wille, R. (1999). *Formal Concept Analysis: Mathematical Foundations*. Springer. ISBN 3540627715 (as I found it: 3-540-62771-5). Translation of the 1996 German original.

**Verified.** Freeman & White: bibliographic details from several reference lists in search results (arXiv nlin/0509007 and others), and a secondary description that they apply Galois lattices to agents and the social events they attend. I did **not** find the paper itself or its abstract. Freeman 1996: one listing (manuscript.isc.ac) only. Freeman & Duquenne: one reference list only (arXiv 1801.03385), which in the same list garbled the Freeman-White entry, so treat the details as provisional. Wille 1982: bibliographic details and the abstract's gist from search results (puma.uni-kassel.de listing and a summary), one source disagrees on whether the term dates from 1981. Ganter & Wille: Springer link https://link.springer.com/doi/10.1007/978-3-642-59830-2 appears in search results.

- **Operands.** A binary incidence relation between two sets (objects and attributes: actors and events, persons and groups).
- **Operators.** None acting on people. The structure is a *complete lattice* of "formal concepts" (pairs of an object set and an attribute set that determine each other) under the Galois connection given by the incidence relation. Meet and join are the lattice operations.
- **What it captures.** A hierarchical, overlapping classification of actors by their events and of events by their actors, in one picture (the same duality as section 5, with the precise order structure).
- **Limits.** Binary static data. The lattice represents the incidence data exactly, and it can be very large. There are no operators on people or on the lattice that model change.
- **Relevance.** Provides a rigorous algebra for the person-group *containment* side of the owner's structure, but not for what people do to one another.

## 10. Category-theoretic treatments

**Citations.**
- Otter, N. & Porter, M. A. (2020). A unified framework for equivalences in social networks. arXiv:2006.10733 (preprint; no journal venue on the arXiv page).
- Motamed, N., Otter, N. & Roff, E. (2026). Coalgebraic analysis of social systems. arXiv:2602.23211 (v1 26 Feb 2026, v2 28 Feb 2026).
- Sallach, D. L. (2011). Categorial Social Analysis. Talk slides, CT2011 (Coimbra), https://www.mat.uc.pt/~ct2011/talks/Sallach.pdf. *(Validation: the PDF resolves. The talk itself says it is "more a description of a research program than a presentation of results". It is not a model.)*

**Verified.** The first two: arXiv abstract pages fetched. The Otter-Porter PDF was fetched but returned as compressed binary, so I read **only the abstract**: a position is an equivalence class of nodes with similar ties, a role is an equivalence class of compound relations connecting the same pairs of nodes, and the method is motivated by functoriality. The Motamed et al. abstract says they extend role and positional analysis from graphs to hypergraphs using universal coalgebra, and prove a general functoriality theorem which, for graphs, reproduces a known folklore observation about compatibility of positional and role analysis. The Sallach item was not opened.

- **Operands.** Graphs (and hypergraphs, in the 2026 paper) as objects of a category, with graph homomorphisms as morphisms. Coalgebras as the framework for "systems".
- **Operators.** Functors between categories of networks, so that positional reduction and role reduction commute. *(Validation correction: the original said this is "the first treatment that ties position and role together in a single formal framework". That overclaims. White & Reitz 1983, Breiger & Pattison 1986 and Pattison 1993 all relate graph homomorphisms (positions) to semigroup homomorphisms (roles). The Motamed et al. abstract itself calls the graph case "a known observation" (folklore). What is new is a functorial formulation, and in 2026 the extension to hypergraphs. Otter & Porter is on arXiv only, labelled a working paper, single version, June 2020.)*
- **What it captures.** The compatibility of the two halves of the Lorrain-White programme, in a category-theoretic language.
- **Limits.** Still graphs of binary ties, with a descriptive purpose (classification of nodes and their relations). Preprints, not peer-reviewed as far as I could confirm.
- **Relevance.** This is where the owner's project, if it is categorical, meets existing work. It is also the closest to a *modern* version of the same idea, and its authors are active now.

---

## What this tradition already covers

- **Relations as operators, composition as the operation, semigroup as the structure.** Lorrain-White 1971 onward: it is the foundation, and it is thoroughly worked.
- **Roles as elements or classes in that semigroup,** and positions as classes of actors, with theorems on when reductions are homomorphisms (Lorrain & White, Boorman & White, White & Reitz).
- **The space of possible role assignments as a lattice** (Borgatti & Everett), and of role structures as a congruence lattice (Boorman & White, Boorman & Arabie).
- **Ego-centred algebras** (Breiger & Pattison, Pattison's local role algebras), plus extensions to time-dependent and valued networks (chapters of Pattison 1993).
- **Persons-and-groups duality** as a lattice or matrix factorisation (Breiger, Freeman & White, Pattison & Breiger 2002, Wille's concept lattices).
- **Fitting an abstract algebra to data** (Boyd) and **optimising a fit by ideal-block types** (Doreian et al.).
- **Category-theoretic formulation** of position/role compatibility (Otter & Porter 2020; Motamed et al. 2026).

## What it does not cover

- **Operators that act on the group.** Everything above is a calculus of *kinds of tie* and their composition. I found none in this cluster where an operator transforms a group's state (admit, expel, promote, introduce, split a group). The semigroup elements describe who is related to whom through whom, not what one actor does to another's standing. *(Validation qualification: this holds for the network-semigroup papers surveyed. It does **not** hold for the school as a whole. In H. C. White's *An Anatomy of Kinship* (1963) and Boyd's "The algebra of group kinship" (*J. Math. Psych.* 6(1), 139-167, 1969, DOI 10.1016/0022-2496(69)90032-7, Crossref-confirmed), marriage and descent rules are permutations acting **on clans**. Groups are the operands, the operators generate a permutation group, and the group's structure classifies the society. These are still structural rules rather than admit/expel/split, but they are operators on groups, written by the founders of this tradition. The survey should have covered them.)*
- **Dynamics or interaction models.** Static algebra of observed structure. Pattison's time-dependent chapter (ch. 6) is the one place it reaches towards dynamics; I have only the chapter title, not its content. That chapter must be read before this claim is final. *(Validation qualification: "static" is broadly fair for the semigroup line, but it overstates the case for the school. H. C. White's *Chains of Opportunity* (1970) models vacancies moving through positions as a Markov process. It is a dynamic model of mobility, close to a "promote" operator, though it is not algebraic in the semigroup sense. Doreian & Stokman (eds.), *Evolution of Social Networks* (1997), treats blockmodels over time.)*
- **Internal state of operands.** Actors are points. The equivalences are about ties only, with no notion of an actor's attributes, resources, beliefs or obligations.
- **Roles as things people hold and enter into, as against positions in a pattern of ties.** Here "role" means an element of the semigroup of compound relations. Roles as normative bundles of rights and duties are outside this tradition, and I have not looked for a formal treatment of them in this cluster.
- **Prediction.** The algebra is derived from data and summarises it. I found no treatment where the algebra is given first and used to predict outcomes.
- **Groups as operands in their own right.** Groups appear as the second mode of a two-mode incidence (sections 5, 9), or as blocks of a partition. Operations between groups (merger, schism, alliance) are not in the cluster I surveyed.

**Blunt conclusion.** The owner's belief is correct that it is not novel in its *first half*: an algebra with people as operands and ties as operators, whose composition table is the object of study, is the Lorrain-White to Pattison semigroup tradition, 1971-1993, with recent categorical restatements. The *second half*, operators that are actions rather than ties and a use of the algebra to model interactions, I did not find in this cluster. That is not evidence that nobody has done it. *(Validation: the first half stands. The second half needs one qualification. Operators whose operands are groups do exist in this school's kinship algebras (White 1963, Boyd 1969), as permutations on clans. Dynamic models of movement between positions exist too (White 1970). Neither is an algebra of actions such as admit, expel or split, so the gap is real. But it is narrower than "no operator acts on groups".)* Other clusters (game theory, rewriting systems, process algebras, agent-based models) may hold it.

---

## Unconfirmed

These are things I believe exist or that surfaced in search, but I could not confirm a source for the specific claim.

- ~~Bonacich 1980~~, ~~Pattison et al. 2000 / Pattison & Wasserman 1995~~ and ~~Winship & Mandel~~ were here originally. Validation confirmed all of them via Crossref and moved them into sections 4 and 6.
- **Freeman & White 1993, end page** (146 as given). Only the start page 127 is confirmed.
- **Wasserman & Faust (1994), *Social Network Analysis: Methods and Applications*, ch. 11 "Relational algebras"**. Table of contents confirmed from Cambridge Core listings (ch. 9 Structural equivalence, 10 Blockmodels, 11 Relational algebras, 12 Network positions and roles). I did not read the chapter, so I cannot say how much semigroup material it contains. It is a textbook treatment worth reading first.
- **Contents of White & Reitz 1983 and Lorrain & White 1971 beyond the abstracts and secondary citations.** No full text was read.
- **Any treatment of dynamics in Pattison 1993 ch. 6.** Chapter title only.
- **Harary-style signed-graph balance as semigroup or semiring, and Kronenfeld-type kinship algebras.** I searched and found nothing citable about either, so I list them as possible gaps rather than findings. Kinship algebras and balance theory are natural neighbours of this cluster that I did not cover.
- **Hage & Harary, and other anthropological relation-algebra work** (kinship as a semigroup), were not searched specifically and should go to the anthropology cluster.

---

## Validation log (2026-10-29)

Checked against Crossref metadata, the arXiv abstract pages, the Arizona research-portal abstracts, Open Library and the validator's own knowledge of the mathematics. No full texts were read, so this pass also rests on abstracts and metadata.

- Lorrain & White 1971: ✓ confirmed (Crossref). 1977 reprint added.
- White, Boorman & Breiger 1976 (I): ✓ confirmed (Crossref).
- Boorman & White 1976 (II): ✎ corrected. The citation is confirmed. The role structure is a homomorphic image only under lean-fit or regular blockings, and the original stated this unconditionally.
- White & Reitz 1983: ✓ confirmed. DOI added.
- Borgatti & Everett 1989: ✎ corrected. Their algorithm computes non-maximal lattice elements; the maximal one was White & Reitz's. "Only trivial regular equivalences" was reversed. The CUHK "PDF" link is HTML.
- Breiger & Pattison 1986: ✎ corrected. The statistical-method claim belongs to the 1995/2000 papers, not this abstract.
- Pattison 1993: ✓ confirmed. ✎ The partially ordered semigroup was noted.
- Pattison & Wasserman 1995: ✓ confirmed, moved from Unconfirmed.
- Pattison, Wasserman, Robins & Kanfer 2000: ✓ confirmed, moved from Unconfirmed.
- Breiger 1974: ✓ confirmed.
- Pattison & Breiger 2002: ✓ confirmed.
- Bonacich 1980: ✎ venue confirmed (AJS 86(1):159-166), moved from Unconfirmed.
- Boorman & Arabie: ✎ corrected. The original is AJS 1980, 86(1):166-174. The 1981 NCJRS item is a reprint.
- Pattison 1981: ✎ corrected. It is a reply to McConaghy, not to Bonacich. McConaghy 1981 added.
- Winship & Mandel 1983: ✎ volume 14 and pages 314-344 confirmed. Its extension (role-set equivalence) noted.
- Boyd 1991: ✓ confirmed (Open Library: GMU Press, ISBN, xii+267 pp).
- Doreian, Batagelj & Ferligoj 2005: ✓ confirmed. Note the 2004 imprint date.
- Freeman & White 1993: ✓ confirmed (DOI added). ? The end page is unconfirmed.
- Freeman 1996: ✓ confirmed.
- Freeman & Duquenne 1993: ✓ confirmed.
- Wille 1982: ✓ consistent with known record. Not re-fetched.
- Ganter & Wille 1999: ✓ consistent with known record. Not re-fetched.
- Otter & Porter 2020: ✓ confirmed (arXiv, working paper, v1 only). ✎ The "first unified framework" overclaim was removed.
- Motamed, Otter & Roff 2026: ✓ confirmed. arXiv:2602.23211, v1 26 Feb and v2 28 Feb 2026, cs.SI/math.CT, abstract as described.
- Sallach 2011: ✓ exists (slides resolve). It is a research programme, not results.
- Wasserman & Faust 1994: ? left in Unconfirmed as written (chapter content unread).
- Nothing was found to be fabricated. ✗ none removed.

**Clearly missing (listed, not researched):** H. C. White, *An Anatomy of Kinship* (1963). Boyd 1969, "The algebra of group kinship" (Crossref-confirmed). H. C. White, *Chains of Opportunity* (1970). Borgatti, Boyd & Everett 1989, "Iterated roles". Boyd & Jonas 2001, "Are social equivalences ever regular?". Everett & Borgatti on automorphic and regular colorations (1990s). Doreian & Stokman (eds.) 1997, *Evolution of Social Networks*. Cartwright & Harary 1956 on structural balance. Ostoic's `multiplex` R package and papers (algebraic analysis of multiplex networks, arXiv 1911.13037).

**Verdict.** The bibliography is sound. Every cited work exists, and most details were right or merely incomplete. The original's "unconfirmed" items all turned out to be real. The mathematical summaries are mostly accurate, with three substantive errors: the unconditional homomorphism claim, Borgatti & Everett's contribution, and the "trivial regular equivalence" reversal. One overclaim was fixed, the "first unified framework" for Otter & Porter. The closing verdict is directionally right but too strong. The same school has operators on groups (kinship permutation algebras) and dynamic position models (vacancy chains), so "no operator acts on the group" holds only for the network-semigroup line, not for the tradition.
