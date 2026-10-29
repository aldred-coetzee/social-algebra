# Prior work 02: algebraic and formal models of kinship and social structure

Date: 2026-10-29. Cluster: anthropology. Validated the same day (log at the end).

**Method note.** Bibliographic facts below were found in a real source (URL given). Where the mathematical description comes from a secondary summary (nLab, a catalogue, an abstract) that is said. Where it rests on standard mathematics or on the validator's knowledge of the field rather than a fetched source, it says so. Several publisher and JSTOR pages were unreachable (503, blank, or paywalled), so no primary text of Weil, Bush, White, Courrège, Lounsbury or Read was read, by either the author or the validator. Treat the algebra descriptions as a map to check against the primary texts, not as a quotation of them.

## Summary of the tradition

Formal kinship theory splits into three strands. (1) **Alliance algebra**: marriage classes are a finite set; descent and marriage rules are permutations of it; the group they generate encodes the system (Weil 1949, Bush, Kemeny-Snell-Thompson, White 1963, Courrège 1965, Liu, Boyd, Tjon Sie Fat, Lawvere's categorical restatement). (2) **Terminology algebra**: kin terms are symbols; relations between terms compose under a product; the question is what rules generate a given terminology and how they map onto genealogy (Lounsbury and Scheffler reduction rules, Gould, Read and the KAES software, Tjon Sie Fat). (3) **Narrative operator formulas**, the odd one out: Lévi-Strauss's canonical formula of myth, which has operators and operands but acts on mythic terms, not on people. The tradition is mature, partly rigorous, and almost entirely about **static classificatory structure** (who may marry whom, what a person calls whom), not about **interaction dynamics** (what one agent does to another and what results). A fourth line, which leaves kinship for networks, starts from White 1963 and runs through Lorrain and White 1971 and Boorman and White 1976 into role algebras of networks; it belongs to cluster 01 and is only pointed at here.

---

## 1. André Weil's appendix (1949)

- **Citation.** A. Weil, "Sur l'étude algébrique de certains types de lois de mariage (Système Murngin)", appendix to Part One (ch. XIV) of C. Lévi-Strauss, *Les structures élémentaires de la parenté*, PUF, 1949, pp. 278-285 (page range corroborated by a JSTOR chapter on permutation models, https://www.jstor.org/stable/jj.8441728.1; nLab's pp. 257-263 refer to the 1967 second edition). English: "On the algebraic study of certain types of marriage laws (Murngin system)", in *The Elementary Structures of Kinship*, Beacon Press, 1969, ch. XIV, beginning p. 221 (end page not confirmed).
- **Sources found.** nLab kinship page https://ncatlab.org/nlab/show/kinship; BnF note https://bnf.fr/fr/mediatheque/des-lois-du-mariage-bourbaki ("principes mathématiques simples qu'on peut résumer en parlant de structure de groupe"); the Stony Brook note https://www.math.stonybrook.edu/~tony/whatsnew/oct09/vanuatu2.html; the Chinese-language abstract of a Liu study https://lawdata.com.tw/tw/detail.aspx?no=220627. No primary scan was read.
- **Operands.** Marriage classes (sections): the Murngin system has eight, and Weil treats them as elements of a finite set. Individuals are not operands; each belongs to a class.
- **Operators.** Maps sending a man's class to the class of his wife and a parent's class to the class of the children. Weil's key requirement (secondary summaries): these maps must be **permutations** of the set of classes, and the system is then summarised by the **permutation group** they generate. The lawdata abstract adds that Weil stated formal conditions a class system must meet (each member has exactly one permitted marriage type; a man may marry his mother's brother's daughter) and used **addition of n-tuples modulo 2** to test Lévi-Strauss's hypothesis about the Murngin eight-section system, which conflicted with those conditions. Encoding classes as vectors over Z/2 means representing the class set as an elementary abelian 2-group on which the marriage and descent maps act. *Corrected 2026-10-29:* the draft said Weil identifies the Murngin group as "dihedral-type, order 8 or 16"; no source supports a specific group, and the only described method is the abelian mod-2 coding, so the claim is moved to Unconfirmed.
- **What it captures.** Whether a stated marriage rule is consistent; what a rule implies (which cousin types become marriageable); the translation of prescriptive rules into group-theoretic conditions such as commutation of the generating permutations (see 2 for the exact conditions in the modern form).
- **Limits.** Classes are pre-given and coarse. No individuals, no relationships other than marriage and descent, no time, no choice. It explains the Murngin ideal, not what Murngin people do. The lawdata abstract records that White (1963) acknowledged his structural analysis failed for unilateral cross-cousin societies such as Purum and Murngin (reasons attributed to White and Reid 1967), and Liu then reopened Murngin (see 3). *Corrected:* the draft attributed this to arXiv:1807.00602, which is an unrelated paper on a genealogical query language.
- **Relevance.** Weil is the origin of "kinship as a group acting on a finite set". It is a precedent for operators-as-permutations, which is the nearest the tradition gets to what the owner describes. It does not model interactions and its operators are fixed by rule, not performed by agents.

## 2. Courrège (1965), the axiomatisation

- **Citation.** P. Courrège, "Un modèle mathématique des structures élémentaires de parenté", *L'Homme* 5(3-4), 1965, pp. 248-290. Title and pages confirmed from Persée's table of contents for the issue, https://www.persee.fr/issue/hom_0439-4216_1965_num_5_3 (section "La parenté : psychanalyse et mathématiques"). The variant "Un modèle de mathématique…" in the Selz-Laurière bibliography (https://numdam.org/item/MSH_1987__97__57_0/) is a citation error. English translation in P. Ballonoff (ed.), *Genetics and Social Structure*, Dowden, Hutchinson & Ross, 1974 (per nLab).
- **Source for the claim.** nLab kinship page: "the axiomatics was proposed in Courrège (1965)".
- **Operands / operators.** Per nLab's modern rendering: a kinship system is a triple (S, ω, μ) with S a finite set of marriage classes and two permutations of S: the **conjugal** function ω (men of class x marry women of class ω(x)) and the **matrilineal** function μ (children of mothers in class x are in class μ(x)). The patrilineal function is then π = μω (a father in x has a wife in ω(x), whose children are in μ(ω(x))). Since ω and μ are arbitrary permutations, S is exactly a finite set with an action of the **free group F₂ = ⟨ω, μ⟩**; the "group of the system" is the image of F₂ in Sym(S), i.e. F₂ modulo the kernel of the action. Exogamy is ω ≠ id; restricted exchange is ω² = id (otherwise generalised exchange); marriage with the matrilateral cross-cousin is admissible iff ωμ = μω, with the patrilateral cross-cousin iff ωμ = μω⁻¹; under the first, the second holds iff exchange is restricted. Irreducible means the action is transitive on S; regular means in addition it is free (so |S| equals the group order). *Validator check:* the MBD condition was re-derived: ego in μ(y), mother's brother in y, his daughter in μω(y), ego's wife in ωμ(y); equal for all y iff ωμ = μω. The definitions of transitive/free are standard group-action terms; that nLab uses exactly these names for them was not quoted in the fetch.
- **What it captures.** The group-theoretic content of elementary systems, with a clean taxonomy (restricted vs generalised exchange, matri/patrilateral).
- **Limits.** Same as Weil: classes only. Courrège's primary text was not read; the details above are nLab's reformulation and may differ from Courrège's own axioms.
- **Relevance.** Gives the cleanest formal statement of "a society's mechanics is a finite group action". Directly reusable as a vocabulary, but it is a theory of the rule, not of interaction.

## 3. Bush, Kemeny-Snell-Thompson, Liu, Boyd and the matrix/semigroup extensions

- **R. R. Bush.** The lawdata abstract (https://lawdata.com.tw/tw/detail.aspx?no=220627) credits Robert R. Bush with developing Weil's method, introducing operators, and using **permutation matrices**; a search summary describes Bush's work as an undated mimeographed manuscript. A bookseller listing (https://www.abebooks.com/Anatomy-Kinship-Mathematical-Models-Structures-Cumulated/32119763537/bd) says White's *An Anatomy of Kinship* has "appendices by André Weil and Robert R. Bush". *Resolved 2026-10-29:* the draft saw a conflict with the Sage entry, which says an appendix is Cynthia A. White's translation of part of Lévi-Strauss ch. 14. There is none: ch. XIV of *Les structures élémentaires* is the appendix containing Weil's text, so the book reprints Weil (translated) and Bush side by side. Bush's own title and date remain **unconfirmed**.
- **Kemeny, Snell and Thompson.** *Introduction to Finite Mathematics*, Prentice-Hall, 1957 (some catalogues 1956; 2nd ed. 1966); catalogue https://catalogosiidca.csuca.org/Record/UCR.000292512?lng=en. *Partly resolved:* the lawdata abstract states that Kemeny, Snell and Thompson first organised prescriptive marriage systems into a **set of axioms**, from which White derived the admissible structures; a reader review (https://beta.thriftbooks.com/w/introduction-to-finite-mathematics_john-g-kemeny/608297) mentions the book's permutation-group treatment of marriage laws. The chapter and section were not located; one table of contents ends with "Applications to behavioral science problems", which is the likely home.
- **P.-H. Liu.** *Murngin: A Mathematical Solution*, Monograph Series B no. 2, Institute of Ethnology, Academia Sinica, Taipei, 1970. https://ianthro.ioe.sinica.edu.tw/edit_book/murngin-a-mathematical-solution/ (catalogue only). nLab also lists "Theory of groups of permutations, matrices and kinship: a critique of mathematical approaches to prescriptive marriage systems", *Bulletin of the Institute of Ethnology, Academia Sinica* 26 (1968) 29-38, and *Foundations of Kinship Mathematics*, Academia Sinica, 1986. The lawdata abstract says Liu offers a new method for prescriptive marriage systems after White's failure (*corrected*: the draft gave arXiv:1807.00602 as the source for this; that paper is unrelated).
- **Boyd.** J. P. Boyd, "The algebra of group kinship", *Journal of Mathematical Psychology* 6 (1969) 139-167 (nLab; Boyd 1969 is also cited among kinship model-builders in an IRD paper on Dravidian kinship, https://horizon.documentation.ird.fr/exl-doc/pleins_textes/pleins_textes_4/colloques/27044.pdf). J. P. Boyd, J. H. Haehl and L. D. Sailer, "Kinship systems and inverse semigroups", *Journal of Mathematical Sociology* 2(1), 1972, 37-61 (title as given in a PKRU SciTech reference list; nLab shortens it to "Kinship and inverse semigroups"). Later: Boyd, "The universal semigroup of relations", *Social Networks* 2(2), 1979, 91-117, and *Social Semigroups*, George Mason UP, 1991 (both via nLab).
- **Structure.** Matrix representations of the permutation group (Bush, Liu); **inverse semigroups** (Boyd et al.). By the Wagner-Preston theorem, inverse semigroups are exactly semigroups of partial bijections, which fits relations such as "wife of" that are defined only on part of the population; that this was the 1972 paper's motivation is the validator's inference from the title, not source-checked.
- **Limits.** As Weil.
- **Relevance.** Shows the move from group to matrix/semigroup, which is the move needed to allow partial or non-invertible operations. Useful precedent for semigroups of social actions; Boyd 1991 carries it out of kinship into social relations generally.

## 4. Harrison C. White, *An Anatomy of Kinship* (1963)

- **Citation.** H. C. White, *An Anatomy of Kinship: Mathematical Models for Structures of Cumulated Roles*, Prentice-Hall, Englewood Cliffs, 1963, Prentice-Hall Series in Mathematical Analysis of Social Behavior, 180 pp. Catalogue https://katalog.muni.cz/Record/MUB01006462277/Description; Sage encyclopedia https://sk.sagepub.com/ency/edvol/embed/socialtheory/chpt/white-harrison.
- **Follow-on.** F. Lorrain and H. C. White, "Structural equivalence of individuals in social networks", *Journal of Mathematical Sociology* 1(1), 1971, 49-80, DOI 10.1080/0022250X.1971.9989788 (confirmed against the Crossref record). Correctly placed as the follow-on: it moves from kinship classes to individuals in arbitrary networks.
- **Operands.** In the main model, **clans** (marriage classes); the Sage entry describes the book as modelling kinship as networks of links between persons defined by their positions.
- **Operators.** *Corrected 2026-10-29.* The draft said the 1963 book composes role relations as a semigroup of Boolean matrices. That is the 1971 paper and Boorman and White 1976, not the 1963 book. The 1963 model, following Kemeny-Snell-Thompson's axioms (lawdata abstract; the axiom list is the validator's knowledge of the standard account, not source-checked), is: a society divided into n clans; each clan's men marry women of exactly one clan, a permutation W; children's clan fixed by the father's clan, a permutation C; no marriage within the clan; every person has relatives in every clan (transitivity); and whether two related people share a clan depends only on the kind of relationship, not on the clan (regularity). W and C are written as n×n **permutation matrices**, kin relations are words in W and C, and the axioms make the group they generate act regularly, so it has order n; admissible systems are classified as groups of order n with two distinguished generators. This is the same F₂-action as Courrège's, with patrilineal rather than matrilineal descent as the second generator. "Cumulated roles" in the title refers to compound relations built by composing W and C (and their inverses), which is where the 1971 relational semigroup grew from.
- **What it captures.** The compositional algebra of kin relations ("my father's sister's son"), the classification of prescriptive systems by group, and, through the 1971 follow-on, the origin of structural equivalence and blockmodelling in network science.
- **Limits.** By White's own account (lawdata abstract), the analysis failed on unilateral cross-cousin systems (Purum, Murngin). Clans are positions in a pre-given structure, not agents acting.
- **Relevance.** **High.** The 1963 group model plus the 1971 semigroup of relations is the closest ancestor of "operands are roles, operators are role relations that compose". The line from this tradition into the owner's goal runs through blockmodelling and relational algebra of networks (Boorman and White 1976; Pattison 1993; cluster 01).

## 5. Lawvere: categorical restatements

- **Sources.** nLab kinship page (above). F. W. Lawvere, "Kinship and mathematical categories", in R. Jackendoff, P. Bloom and K. Wynn (eds), *Language, Logic, and Concepts: Essays in Memory of John Macnamara*, MIT Press, 1999, pp. 411-425; Lawvere and S. H. Schanuel, *Conceptual Mathematics*, Cambridge UP, 1997, pp. 162-163. Citations via nLab; originals not fetched.
- **Structure (nLab).** The category of kinship systems (S, ω, μ), with maps commuting with both permutations, is equivalent to the topos of finite F₂-sets. A "society" in Lawvere's sense is a set with mother and father endofunctions m and f, i.e. an action of the free monoid on {m, f} (a presheaf on that one-object category). Here the elements are **individuals**, not classes.
- **Relevance.** Shows that category theory is already a worked-out home for this algebra. Its operators remain mother/father/marriage maps. Does not model interaction.

## 6. Tjon Sie Fat

- **Citations** (https://www.universiteitleiden.nl/en/staffmembers/franklin-tjon-sie-fat/publications):
  - F. E. Tjon Sie Fat, 1998, "On the Formal Analysis of 'Dravidian', 'Iroquois', and 'Generational' Varieties as Nearly-Associative Combinations", in M. Godelier, T. R. Trautmann and F. E. Tjon Sie Fat (eds), *Transformations of Kinship*, Smithsonian Institution Press, pp. 59-93. (*Corrected*: editors were given as Tjon Sie Fat and Godelier only.)
  - Tjon Sie Fat, 1998, "Local Rules and Global Structures: Models of Exclusive Straight Sister-Exchange", in T. Schweizer and **Douglas R.** White (eds), *Kinship, Networks, and Exchange*, Cambridge University Press, pp. 261-276 (https://www.cambridge.org/core/books/abs/kinship-networks-and-exchange/local-rules-and-global-structures-models-of-exclusive-straight-sisterexchange/2331FD09CD9ED18ACB6BAE1B3CF5D32C). Not Harrison White.
  - Tjon Sie Fat, 1999, "Trajectoires et transformations: les automates d'arbres binaires pour l'analyse des variations terminologiques", in Descola and Hamel (eds), *La Production du social*, Fayard, pp. 419-432.
- **Operands / operators** (from titles only; abstracts unavailable): kin terms combined by a product that is only **nearly associative**; **binary tree automata** to describe variation between terminologies. Beyond the titles, the structure is not source-checked.
- **What it captures.** Variation among terminological types (Dravidian/Iroquois/Generational) as perturbations of one algebraic structure, and local-to-global emergence in sister-exchange.
- **Limits.** Terminologies and exchange rules, not interaction.
- **Relevance.** The "nearly-associative" idea is useful: a social operator algebra may fail associativity and still be tractable. The automata approach is the closest this cluster gets to a computational treatment of variation, but it acts on terms, not on agents.

## 7. Lounsbury and Scheffler: componential analysis and reduction rules

- **Citations.**
  - F. G. Lounsbury, "The structural analysis of kinship semantics", in H. G. Lunt (ed.), *Proceedings of the Ninth International Congress of Linguists*, Mouton, The Hague, 1964, pp. 1073-1093 (https://tlopo.clld.org/sources/Lounsbury1964a and https://contentas.bibl.u-szeged.hu/Record/misc67975/Details).
  - Lounsbury, "A formal account of the Crow- and Omaha-type kinship terminologies", in W. H. Goodenough (ed.), *Explorations in Cultural Anthropology*, McGraw-Hill, 1964, pp. 351-393 (https://baul.fahho.mx/Record/37502; the title varies in citations).
  - H. W. Scheffler and F. G. Lounsbury, *A Study in Structural Semantics: The Siriono Kinship System*, Prentice-Hall, Englewood Cliffs, 1971, vii + 260 pp. (https://finlit.finna.fi/Record/helka.9912241343506253/HREF).
- **Operands.** Genealogical kin types, written as strings of primitive relations (F, M, B, Z, S, D, H, W).
- **Operators.** **Equivalence ("reduction") rules** on kin-type strings: merging rules (e.g. same-sex siblings equivalent as linking relatives), half-sibling rules, and the **skewing** rules of Crow-Omaha systems, which equate kin types of **different generations**: the main Omaha rule extends MB to MBS, the main Crow rule FZ to FZD (Whiteley and McConvell 2021, https://openresearch-repository.anu.edu.au/items/1034bd46-5e18-433d-ae9f-4eb165afb360). Each term has a focal genealogical definition and is extended to distant kin by the rules (Trobriand article found via search). *Corrected:* the draft described skewing as collapsing "a linking relative with a descendant of the same lineage", which misstates it. Reading the rules as a **string-rewriting system** on the free monoid of genealogical steps, with terms as classes of the induced congruence-like relation, is the validator's and author's framing, not Lounsbury's wording; it is accurate in substance, with the caveat that the rules are context-sensitive (they apply to a relative "as a linking relative" and depend on the sex of the linking relative), so it is a rewriting system, not a monoid presentation.
- **What it captures.** The extension problem: how a term applies from close to distant kin. Skewing rules are a genuine, non-trivial operator algebra (non-group, collapsing, generation-shifting).
- **Limits.** A Japanese paper (https://kuins.repo.nii.ac.jp/record/1114/files/24-10.pdf, via search) says the method was hard to apply by hand and not widely used. Genealogy-bound: it presumes biological/affinal primitives and explains terms, not behaviours.
- **Relevance.** Reduction rules are the earliest real "operators on relation strings" and are the template for a rewriting-system presentation of social relations. They do not model interactions.

## 8. Sidney H. Gould and Kronenfeld

- **Citations.** S. H. Gould, *A New System for the Formal Analysis of Kinship*, ed. D. B. Kronenfeld, University Press of America, 2000 (https://catalog.hathitrust.org/Record/004102368). Kronenfeld, *Fanti Kinship and the Analysis of Kinship Terminologies*, University of Illinois Press, 2009 (https://www.press.uillinois.edu/books/?id=c033704). Kronenfeld, *Types of Kinship Terminological Systems and How to Analyze Them: New Insights from the Application of Sidney H. Gould's Analytic System*, Brill (Brill Research Perspectives in Humanities and Social Sciences), 2022, ISBN 978-90-04-46802-3 (https://escholarship.org/uc/item/1r2456gx; https://www.oeaw.ac.at/resources/Record/993583118004498).
- **What is established.** Gould's system is a distinctive formal analytic system for kin terminologies; Kronenfeld's 2022 abstract says it implies constraints on future analytic approaches and points to distributed collective cognitive systems. **What algebraic structure Gould uses is still unknown** after validation.
- **Relevance.** Not assessed beyond its existence. Included as a flagged gap.

## 9. Dwight Read, Leaf, KAES and the Kinship Algebra Modeller

- **Citations.**
  - D. W. Read, "An algebraic account of the American kinship terminology", *Current Anthropology* 25(4), 1984, 417-449 (with comments, e.g. Buchler and Fischer; JSTOR not read).
  - D. Read and C. Behrens, "KAES: An expert system for the algebraic analysis of kinship terminologies", *Journal of Quantitative Anthropology* 2, 1990, 353-393.
  - D. Read, M. D. Fischer and M. J. Leaf, "What Are Kinship Terminologies, and Why Do We Care? A Computational Approach to Analyzing Symbolic Domains", *Social Science Computer Review* 31(1), 2013, 16-44, DOI 10.1177/0894439312455914 (https://kar.kent.ac.uk/31546).
  - D. W. Read, "The algebraic logic of kinship terminology structures", *Behavioral and Brain Sciences* 33(5), 2010, 399-401, DOI 10.1017/S0140525X10001378 (a commentary on D. Jones's target article; https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/algebraic-logic-of-kinship-terminology-structures/4B97448FF1FA6222479AE9CF154E64F8).
  - G. Bennardo and D. Read, "Cognition, algebra, and culture in the Tongan kinship terminology", *Journal of Cognition and Culture* 7, 2007, 49-88.
  - M. J. Leaf and D. Read, *Human Thought and Social Organization: Anthropology on a New Plane*, Lexington Books, 2012, xvii + 458 pp. (https://quaibranly.fr/en/explore-collections/base/Bibliography/action/show/notice/000194095-human-thought-and-social-organization-anthropology-on-a-new-plane).
  - Leaf and Read, *Introduction to the Science of Kinship*, Lexington Books, 2021 (mentioned on Read's author page; not independently fetched).
  - Software page: KAM, https://csac.anthropology.ac.uk/Research/KAM.
- **Operands.** Kin term symbols (a finite set).
- **Operators.** A **binary product** on the terms ("a structure consisting of a set of symbols (kin terms) interconnected through a binary product"), generated from **primary kin terms** and given its particular shape by **structural equations**; terminologies differ by their primary terms and equations (Read's later abstracts). The generated structure is the **kin term map**. Read's framework is grounded in a family space of parent-child, spouse and sibling positions; genealogical meanings are derived from the algebra, not assumed (KAM description). *Corrected:* the draft's "monoid-like structure … partly commutative on the 'parent' chain" has no source and is removed; the exact generators and equations of the 1984 American algebra are in Unconfirmed.
- **What it captures.** Whole terminologies as generated algebras; automatic building of the algebra from informant data (KAES/KAM); an account of why the American terminology has its shape.
- **Limits.** Terminology only; synchronic; explains kin-term computation ("how two people are related through a third", 2013 abstract). Kronenfeld's BBS commentary (https://www.cambridge.org/core/product/B13FF9FA05CE831B908A28391B110FA4) addresses Jones's analysis, not Read directly; critiques of Read sit elsewhere and were not read.
- **Relevance.** **High on method, low on subject.** It is the only tradition here with working software that builds an algebra from observed data and checks consistency. The idea that kin-term computation is "symbolic computation" is close to the owner's idea. It still covers terms for relatives, not people acting on one another.

## 10. Héran, *Figures de la parenté* (2009)

- **Citation.** F. Héran, *Figures de la parenté: une histoire critique de la raison structurale*, Presses universitaires de France, coll. "Sociologies", Paris, 2009, about 645 pp. (https://www.universalis.fr/encyclopedie/francois-heran/ and https://en.wikipedia.org/wiki/Fran%C3%A7ois_H%C3%A9ran). English edition *The Fabric of Kinship* listed as forthcoming from Bardwell Press, not confirmed published.
- **What is established.** Reassesses Lévi-Strauss's debt to Granet; constructs a universal genealogical representation tool; argues that modelling does not choose between the mechanisms (gift, debt, interest, male domination, mathematical logic) that anthropologists have proposed. Whether it discusses Weil, Courrège or White in detail was not confirmed by author or validator.
- **Relevance.** A historical and critical source, not a new algebra. Useful for the critique of what formal models can and cannot decide.

## 11. Lévi-Strauss's canonical formula of myth, Maranda, Petitot, Morava

- **Original.** C. Lévi-Strauss, "The structural study of myth", *Journal of American Folklore* **68**(270), 1955, 428-444; formula on p. 442. *Corrected:* the draft gave volume 78; the 1955 volume is 68 (confirmed by a contemporary review citing "68 [1955], 428-444" and by the page header of a scan).
- **Formula.** f_x(a) : f_y(b) ≃ f_x(b) : f_{a⁻¹}(y). Notation, per a review of Maranda's volume: ":" means "transforms itself into", "::" (here ≃) means "is a resemblance between two transformations".
- **Formalisations.**
  - P. Maranda (ed.), *The Double Twist: From Ethnography to Morphodynamics*, University of Toronto Press, 2001 (https://cbra.library.utoronto.ca/items/show/9628).
  - J. Petitot, "Approche morphodynamique de la formule canonique du mythe", *L'Homme* 28(106-107), 1988, 24-50; and "A morphodynamical schematization of the canonical formula for myths", in Maranda 2001, pp. 267-311.
  - J. Morava, "On the canonical formula of C. Lévi-Strauss", arXiv:math/0306174 (June 2003), reading the formula through an anti-automorphism of the **quaternion group of order 8**; and "On the canonical formula of C Lévi-Strauss, II", arXiv:2002.12813 (27 Feb 2020), a model based on the **binary octahedral group**. Both abstracts confirmed.
  - W. Wildgen, 2023 reassessment in *Esse* (USP), https://revistas.usp.br/esse/en/article/view/209348 (catastrophe-theory reading).
- **Operands.** Mythic terms (a, b) and functions (x, y).
- **Operators.** Function application and inversion (a⁻¹); in Morava's reading, group elements with an anti-automorphism.
- **What it captures.** An explicit operator formula for a transformation relation between pairs, with an inversion step that swaps a term and a function.
- **Limits.** Lévi-Strauss gave no definitions precise enough to fix the mathematics; every formalisation is an interpretation. No evidence it has been applied to social interaction rather than myth.
- **Relevance.** Low for the stated aim; a rare example of an anthropologist writing an operator formula explicitly, but it acts on myth components.

## 12. Others that matter

- **Hage and Harary.** P. Hage and F. Harary, *Structural Models in Anthropology*, Cambridge University Press, 1983 (https://www.cambridge.org/core/books/structural-models-in-anthropology/4910E3EF1D33C2CA99AC132F4405DFE2); *Island Networks*, Cambridge, 1996; and "The logical structure of asymmetric marriage", *L'Homme* 36(139), 1996, 109-124 (nLab). Graph-theoretic models of kinship logic, exchange, and networks. Relevance: graphs, not algebra of operators.
- **Harary and Douglas R. White**, "P-Systems: A Structural Model for Kinship Studies", *Connections* 24(2), 2001, 35-46 (nLab; not fetched). Douglas R. White, not Harrison.
- **Haddad and Sureau**, "Les groupes, les hypergroupes et l'énigme des Murngin", *Journal of Pure and Applied Algebra* 87 (1993) 221-235 (nLab); hypergroups for Murngin, i.e. multivalued products where the class of a relative is not unique. Not fetched.
- **Otter and Porter**, "A unified framework for equivalences in social networks", arXiv:2006.10733 (June 2020): uses functoriality to unite positional and role analysis, defining a role as an equivalence class of compound relations. A network paper, descended from Lorrain and White; belongs with cluster 01.
- **Ambrym (Vanuatu).** The Stony Brook note (https://www.math.stonybrook.edu/~tony/whatsnew/oct09/vanuatu2.html) reports a marriage system with the non-commutative group S₃ at its core (from K. M. Rio, *The Power of Perspective*, Berghahn, 2007), and the Sartre vs Lévi-Strauss debate over the Ambrym diagram. A worked example that a non-abelian group is needed.
- **Chui, Grüninger, Wong**, "An Ontology for Formal Models of Kinship", *Formal Ontology in Information Systems* (FOIS 2020), *Frontiers in Artificial Intelligence and Applications* 330, pp. 92-106, DOI 10.3233/FAIA200663 (confirmed): a first-order-logic ontology built on anthropology's "atemporal algebraic models", used to check definitions from Canadian legal texts and data-collection documents.

## 13. Missing from the draft (added by validation; not read)

- **S. A. Boorman and H. C. White**, "Social structure from multiple networks. II. Role structures", *American Journal of Sociology* 81(6), 1976, 1384-1446: the role semigroup of a network (composition of Boolean relation matrices, reduced by homomorphism). This, not the 1963 book, is where "semigroup of composing role relations" lives. Citation from the validator's knowledge.
- **P. Pattison**, *Algebraic Models for Social Networks*, Cambridge UP, 1993: the standard treatment of role algebras, partial orders of relations, and their decomposition. Citation from the validator's knowledge.
- **J. P. Boyd**, *Social Semigroups*, 1991 (above, via nLab): generalises the kinship semigroups to social relations.
- **P. Ballonoff (ed.)**, *Genetics and Social Structure*, 1974 (via nLab): the anthology carrying the Courrège translation and other mathematical kinship papers.
- **F. E. Tjon Sie Fat**, doctoral thesis on simple models of elementary structures (Leiden, c. 1990): the validator recalls *Representing Kinship: Simple Models of Elementary Structures*; a search did not confirm it, so check before citing.
- **J. Cargal**, "An analysis of the marriage structure of the Murngin tribe of Australia", *Behavioral Science*, 1996 (seen in a reference list during validation): a direct mathematical treatment of the Murngin case.

---

## What this tradition already covers

1. **Operators and operands in the literal sense.** The alliance algebra has them: finite sets of marriage classes as operands, marriage and descent as permutations, the generated group as the structure (Weil, KST, White 1963, Courrège). Read's terminology algebra has kin terms as operands and a binary product as operator. The network line (Lorrain and White 1971, Boorman and White 1976, Boyd) has positions or individuals as operands and composing relations as operators, organised as a semigroup.
2. **Composition of relations.** "A's brother's wife" is a product, and the question of what the product rules are has been formalised several times over: permutation groups, rewriting with reduction rules, inverse and relational semigroups, hypergroups, nearly-associative products.
3. **Rigorous classification of static systems.** Restricted vs generalised exchange, regular vs irreducible, Crow-Omaha skewing, Dravidian vs Iroquois, and so on.
4. **Algebra with tooling.** KAES/KAM builds the algebra from data. Chui et al. formalise it in first-order logic.
5. **Category-theoretic restatement.** Lawvere's topos of F₂-sets and actions of the free monoid on {mother, father}.
6. **The idea that groups of people have a hidden operator structure** is the founding idea of the field, not new.

## What it does not cover

1. **Interaction.** Operators here are kinship relations, or rules relating classes; none are things people **do** to one another (persuade, give, defer, exclude, introduce). There is no algebra of acts, no state change as a result of an act.
2. **Individuals as agents.** Operands are mostly classes, positions or terms. Individuals do appear (Lawvere's "society", Lorrain and White's networks), but only as points under fixed relations, never as actors with a history. *Softened at validation:* the draft said individuals are outside the model entirely, which Lawvere and Lorrain-White contradict.
3. **Groups as operands that merge, split, or nest.** Not found anywhere in this cluster. Groups appear only as classes under a fixed action.
4. **Dynamics.** Almost everything is atemporal (Chui et al.'s abstract calls anthropology's kinship models "atemporal algebraic models"). The nearest exceptions are Tjon Sie Fat's tree automata, which treat variation between terminologies, and his local-rules-to-global-structure models of sister exchange.
5. **Roles beyond kinship.** White's composition of relations generalises in principle, and became network role analysis (Boorman and White, Pattison, Boyd), but this cluster does not extend to power, trust, obligation or conversation.
6. **Empirical fit.** The Murngin case shows the problem: the formal model of the rule and observed practice diverged, and by his own account White's analysis failed on unilateral cross-cousin systems.
7. **Agreed formalism.** There is no single algebra; Weil/Bush/Courrège, White, Lounsbury/Scheffler, Read, Gould, Tjon Sie Fat and Lévi-Strauss's myth formula use incompatible frameworks. (The alliance strand is the exception: Weil, KST, White and Courrège are the same F₂-action in different notation.)

**Blunt verdict.** The owner's idea is not novel at the level of "operators and operands for social structure". It has been done for kinship for about 75 years. What this cluster does **not** contain is an algebra of *social acts between persons, roles and groups with interaction dynamics*. The most useful reusable pieces are Weil/Courrège/White (group actions on classes), Lorrain-White and Boyd (semigroups of composing relations, structural equivalence, partial operations), Lounsbury (rewriting rules with collapsing behaviour), Read (data-driven algebra construction and software) and Tjon Sie Fat (near-associativity). Other clusters (network role algebra, relational sociology, process calculi, speech-act formalisms) must be checked for the interaction side before any claim of novelty.

---

## Unconfirmed

- **Bush's appendix.** His role and its inclusion in White 1963 are corroborated (lawdata abstract; bookseller listing); the exact title and date of the mimeo are not.
- **Kemeny, Snell and Thompson's kinship section.** Corroborated by one secondary abstract (lawdata) and a reader review; chapter, section and edition not located.
- **White 1963's axiom list as given in section 4.** From the validator's knowledge of the standard account (and consistent with the lawdata abstract), not from the book.
- **The group of Weil's Murngin analysis.** The draft's "dihedral-type, order 8 or 16" has no source; only the mod-2 vector coding is attested.
- **Generators and structural equations of Read's 1984 American algebra.** Only the general shape (primary terms, binary product, structural equations, kin term map) is attested.
- **Boyd, Haehl and Sailer's motivation** for inverse semigroups (inferred from the title).
- **Liu 1968 and 1986; Lawvere 1999; Harary and D. R. White 2001; Haddad and Sureau 1993; Courrège's English translation.** Known only via nLab's reference list (Lawvere's volume is a well-known MIT Press book, so low risk).
- **Gould's algebraic structure.** The books exist; their formal content was not retrievable.
- **Héran's treatment of Weil, Courrège, White.** Not confirmed.
- **Tjon Sie Fat's thesis** (section 13).
- **Primary scans.** None of Weil, Bush, White, Courrège, Lounsbury, Gould, Read or Petitot was read directly; all descriptions are from catalogue records, abstracts, nLab and secondary summaries.

## Validation log (2026-10-29)

- Weil 1949: ✎ corrected (1949 pages corroborated, nLab's are the 1967 edition; English end page dropped; unsourced "dihedral, order 8 or 16" moved to Unconfirmed; mod-2 method kept; White-failure claim re-sourced from the misattributed arXiv:1807.00602 to the lawdata abstract).
- Courrège 1965: ✎ corrected (title confirmed on Persée, variant is a citation error; ω conjugal and μ matrilineal rather than generic "descent"; π = μω, PCC condition, image-of-F₂ quotient and English translation added; MBD condition re-derived).
- Bush: ✎ corrected (the supposed source conflict is not one, since ch. XIV is Weil's appendix); title still ?.
- Kemeny-Snell-Thompson 1957: ✎ partly resolved (axiomatisation corroborated by one secondary source); section ?.
- Liu 1970 (and 1968, 1986): ✎ corrected (1968 full citation added; arXiv misattribution removed); 1968/1986 ? via nLab only.
- Boyd 1969: ✎ resolved (J. Math. Psych. 6, 139-167; nLab plus an independent bibliography).
- Boyd, Haehl, Sailer 1972: ✓ (title variant noted); inverse-semigroup motivation ? (Wagner-Preston fit added as inference).
- White 1963: ✎ corrected (the 1963 model is permutation matrices W, C acting regularly on clans, not a Boolean-matrix semigroup; that belongs to 1971/1976).
- Lorrain and White 1971: ✓ (DOI confirmed via Crossref; correctly placed as the follow-on).
- Lawvere 1999 / Lawvere-Schanuel 1997: ✎ (full citation added); ? via nLab only.
- Tjon Sie Fat 1998 (two) and 1999: ✎ corrected (*Transformations of Kinship* editors are Godelier, Trautmann and Tjon Sie Fat; Schweizer's co-editor is Douglas R. White).
- Lounsbury 1964 (two), Scheffler and Lounsbury 1971: ✎ corrected (skewing equates kin types of different generations, e.g. Omaha MB to MBS, Crow FZ to FZD; rewriting framing kept with a context-sensitivity caveat).
- Gould 2000 / Kronenfeld 2009, 2022: ✓ bibliographic (Brill series and ISBN added); formal structure ?.
- Read 1984, Read and Behrens 1990, Read-Fischer-Leaf 2013, Read 2010, Bennardo and Read 2007, Leaf and Read 2012: ✓ bibliographic; ✎ unsourced "partly commutative monoid" claim removed; 2021 book ?.
- Héran 2009: ✓ bibliographic; treatment of the mathematicians ?.
- Lévi-Strauss 1955: ✎ corrected (volume 68, not 78).
- Maranda 2001, Petitot 1988/2001, Wildgen 2023: ✓ as cited (not re-fetched).
- Morava 2003, 2020: ✓ (both abstracts confirmed).
- Hage and Harary 1983, 1996: ✓ (1996 L'Homme paper added).
- Harary and White 2001: ✎ (Douglas R. White; Connections 24(2) 35-46); ? via nLab.
- Haddad and Sureau 1993: ✎ (pages added); ? via nLab.
- Otter and Porter 2020: ✎ (title and abstract supplied; it is a network paper).
- Rio 2007 / Ambrym: ✓ as cited (not re-fetched).
- Chui, Grüninger, Wong 2020: ✓ (DOI, pages and abstract confirmed).
- Added as missing: Boorman and White 1976, Pattison 1993, Boyd 1991, Ballonoff 1974, Tjon Sie Fat thesis (?), Cargal 1996.
- Removed: none. No fabricated work was found; the errors were misattributions, a wrong volume number, mis-stated mathematics and unsourced specifics.

**Verdict.** The bibliography is sound: every cited work exists, and the errors were a wrong volume (Lévi-Strauss), wrong co-editors (Tjon Sie Fat), and a claim sourced to an unrelated arXiv paper. The mathematics needed more correction than the citations. The most consequential error was placing a Boolean-matrix role semigroup in White 1963, which is a permutation-group model on clans, and that error had propagated into the "covers" list and the verdict. Treat the alliance-algebra descriptions as reliable in form. Treat the terminology-algebra details (Read, Gould, Tjon Sie Fat) as outlines only until the primary texts are read.
