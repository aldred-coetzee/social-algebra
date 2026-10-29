# Prior work 03: interaction as operator (social psychology and sociology)

Date: 2026-10-29 (validated the same day; see the log at the end)

**Summary.** Nearly every theory in this cluster treats an act between people as something that changes a state: a sentiment vector (Affect Control Theory), a sign on an edge (balance theory), an expectation advantage (expectation states), a dependence or power value (exchange theory), a position on a two-axis circle (interpersonal circumplex), or a Boolean or real-valued readiness to choose (Lefebvre). Very few state the acts as a closed set of operators with composition laws. The closest to a real algebra are Lefebvre's reflexive model (explicit Boolean and real-valued functions over nested images of agents, and in the 1982 book a mapping from a group's relation graph to a Boolean polynomial) and balance theory (sign multiplication on a signed graph, the two-element group). Affect Control Theory is the closest to "acts as transformations of actor state"; its transformation is a fixed polynomial map fitted by regression, not an algebraic law derived from axioms. Fiske's relational models are more than a typology: each model is identified with a measurement structure (nominal, ordinal, interval, ratio) and so with a group of admissible transformations, but there are no operators for acts. Emerson's power-dependence theory derives a closed list of exactly four balancing operations from two equations. Nothing here has persons, roles and groups as operands with a general, closed set of social acts as operators. Method note: web search in this session returned mostly abstracts, catalogue records and Wikipedia; primary texts were generally not opened by the original author. The validation pass opened Emerson (1962) and Bulitko (2002) in full and checked every DOI against Crossref. Where a detail could not be confirmed it is under "Unconfirmed".

Confirmation labels used: **[verified]** = a source in this session stated it; **[secondary]** = confirmed only via a citing source or catalogue; **[validator]** = stated from the validator's own knowledge of the literature, not re-confirmed against a source in this session.

---

## 1. Fiske: Relational Models Theory

- Fiske, A. P. (1991). *Structures of Social Life: The Four Elementary Forms of Human Relations*. New York: Free Press. Catalogue records confirm title, publisher, 1991 (e.g. https://simonandschuster.com.au/books/Structures-of-Social-Life/Alan-page-Fiske/9780029066874). [verified, catalogue]
- Fiske, A. P. (1992). The four elementary forms of sociality: Framework for a unified theory of social relations. *Psychological Review*, 99(4), 689-723. doi:10.1037/0033-295X.99.4.689 (Crossref confirms). Abstract read via OpenAlex. [verified, abstract only; full article not read]

**Operands.** People, within dyads or groups; the "relationship" between them is the thing modelled.

**Operators and formal structure.** There are no operators for acts. Four *relational models* (Communal Sharing, Authority Ranking, Equality Matching, Market Pricing) are the elementary forms; the 1992 abstract says people treat category members as equivalent, attend to positions in a linear ordering, keep track of imbalances, and orient to ratio values respectively. Wikipedia (https://en.wikipedia.org/wiki/Relational_models_theory), citing Fiske 1992, gives the mapping to measurement scales: CS ~ nominal (categorical), AR ~ ordinal (linear ordering), EM ~ interval (balance kept by addition and subtraction), MP ~ ratio (proportions, multiplication, division, distributive law, a zero origin) (wording follows the Wikipedia article 'Relational models theory', CC BY-SA 4.0). [secondary] This is not merely a loose analogy: Fiske builds it on measurement theory (Stevens; Krantz, Luce, Suppes & Tversky), so each model carries a definite mathematical structure (an equivalence relation; a linear order; an ordered additive group; a ratio structure) [validator]. The IEP entry (https://iep.utm.edu/r-models/) adds the consequence that the models form a descending chain of symmetry groups (MP's admissible transformations are a subgroup of EM's, EM's of AR's, AR's of CS's) [verified, but the IEP presents this as its own analysis, not attributed to Fiske]. Fiske's main empirical claim is that cultures implement the models differently, and that models combine and nest. [from abstract/standard account]

**What it captures.** A small, empirically tested classification of how people structure relations and of the transfers (sharing, deference, turn-taking, pricing) appropriate to each; per the 1992 abstract, supported by ethnographic fieldwork and 19 experimental studies using 7 methods across 5 cultures. [verified]

**Limits.** Structure of relations, not a calculus of acts. No composition rules for how models combine, no state change, no dynamics. The scale-type structure says which arithmetic is meaningful within a relation type, not what happens when acts occur.

**Relevance.** Strong as a source of *relation types* (the labels on edges) and, more sharply than the original draft said, as a precedent for giving each relation type its own algebraic structure and invariance group. Does not provide operators.

---

## 2. Heise: Affect Control Theory (ACT)

- Heise, D. R. (2007). *Expressive Order: Confirming Sentiments in Social Actions*. New York: Springer. doi:10.1007/978-0-387-38179-4 (Crossref confirms title and year). Description at https://www.springer.com/gp/book/9780387381770 (three parts: plain-language, mathematical derivations, research programme and software). [verified]
- Heise, D. R. (1979). *Understanding Events: Affect and the Construction of Social Action*. Cambridge University Press. Listed in https://en.wikipedia.org/wiki/Affect_control_theory. [secondary]
- Averett, C. P., & Heise, D. R. (1987). Modified social identities: Amalgamations, attributions, and emotions. *Journal of Mathematical Sociology*, 13(1-2), 103-132. doi:10.1080/0022250X.1987.9990028 (Crossref confirms). [verified]
- Software: Interact (Heise; guide mirrored at https://cs.uwaterloo.ca/~jhoey/research/ACTBackup/public_files/InteractGuide.pdf). Franklin Research ACT bibliography: https://act.franklinresearch.uga.edu/ . [verified, existence]
- Later probabilistic work: Hoey, J., Schröder, T., & Alhothali, A. (2013). Bayesian Affect Control Theory. *2013 Humaine Association Conference on Affective Computing and Intelligent Interaction*, 166-172. doi:10.1109/ACII.2013.34 (Crossref confirms; author order corrected). [verified]

**Operands.** Identities (actor, object person), behaviours, and settings, each with a three-number EPA profile: Evaluation, Potency, Activity (semantic-differential scores). Two layers: fundamental *sentiments* (stable cultural meaning) and *transient impressions* (current, event-driven).

**Operators and formal structure.** An event is an actor-behaviour-object (plus setting) tuple, descended from Gollob's (1968) subject-verb-object impression-formation work. Impression-formation equations map the pre-event transient vector plus the event to a post-event transient vector; Wikipedia describes them only as "non-linear equations obtained through empirical studies" (wording follows the Wikipedia article 'Affect control theory', CC BY-SA 4.0). [verified] Their form [validator]: one regression per post-event value (nine for actor, behaviour, object), each on the nine pre-event EPA values plus a selected set of two- and three-way product terms (e.g. behaviour-evaluation times object-evaluation), estimated per culture. So the event operator is a fixed polynomial map on R^9 (R^3 per element), not an arbitrary black box. Deflection is the sum of (possibly weighted) squared differences between transient impressions and fundamental sentiments [validator; Wikipedia says only "distances in EPA space" (Wikipedia 'Affect control theory', CC BY-SA 4.0)]. Actors choose the behaviour minimising deflection; because the equations are linear in the behaviour's own EPA values once actor and object are fixed, deflection is quadratic in the behaviour and the optimum has a closed-form solution, which is the sense in which the optimum is derived by calculus (the validator's gloss, not a quotation from a named source) [validator]. Reidentification is a second operation: reassigning identities to reduce deflection. [from abstract/standard account]

**What it captures.** A quantitative, cross-culturally parameterised dictionary of identities and behaviours; predictions of which act is appropriate, which emotions arise, and when relabelling occurs. It is the only theory in the cluster with a working simulator on a large vocabulary of social acts.

**Limits.** No closed composition law beyond iterating the map, no inverse, and the coefficients are regression fits per culture and dataset. State is only affective meaning; no group structure beyond actor and object, no obligations, resources, roles-as-positions, or time except through successive events. It models *what is expected to be done to confirm sentiment*, not the structure of the group.

**Relevance.** The closest existing "act as a transformation on actor state" programme and the one to learn most from; it already has the actor-act-object event grammar. It does not give a group-level algebra, but its dictionaries and fitted equations could supply parameters.

---

## 3. Lefebvre: Algebra of Conscience and reflexive models

- Lefebvre, V. A. (1982). *Algebra of Conscience: A Comparative Analysis of Western and Soviet Ethical Systems*. Dordrecht: Reidel (Theory and Decision Library). Confirmed by catalogue hits; 2nd, expanded edition (Kluwer, 2001): https://link.springer.com/978-0-7923-7121-2 (also https://link.springer.com/978-90-481-5751-8). The series volume number (26) and editor (Rapoport) given in the draft were not confirmed. [verified, catalogue/description]
- Lefebvre, V. A. (1980). An algebraic model of ethical cognition. *Journal of Mathematical Psychology*, 22(2), 83-120. doi:10.1016/0022-2496(80)90014-0 (Crossref). [verified]
- Lefebvre, V. A. (1985). The golden section and an algebraic model of ethical cognition. *Journal of Mathematical Psychology*, 29(3), 289-310. doi:10.1016/0022-2496(85)90010-0 (Crossref). [verified]
- Lefebvre, V. A., "The law of self-reflexion", Cogprints 2927: https://web-archive.southampton.ac.uk/cogprints.org/2927/1/The_Law_of_Self-Reflexion.pdf . Exists (search hit); the PDF returned 403 and was not read. [secondary]
- Lefebvre, V. A. (1991). *Formula of Man* (Moscow: Progress, in Russian) and (1995) "The anthropic principle in psychology and human choice", *Psycoloquy* 6(29): the sources Bulitko cites for the readiness function. [secondary, via Bulitko]
- Bulitko, V. K. (2002). On successive approximations to the choice problem and logic. arXiv:math/0205325. Read in full: states Lefebvre's function, its four axioms and its Boolean form. [verified]
- Umpleby, S. (2016), "Vladimir Lefebvre's theory of two systems of ethical cognition", cited on https://en.wikipedia.org/wiki/Vladimir_Lefebvre; venue not found. [secondary]

**Operands.** Agents (subjects), each carrying an image of themselves and of other agents; states are real values in [0,1] (readiness, i.e. probability, of choosing the positive pole of a binary choice) or Boolean (0/1) in the discrete case. Nesting: agent, image of agent, image of image.

**Operators and formal structure.** Explicit and formal. In the later model (1990s; Bulitko's sources are 1991 and 1995) a subject is a function [from abstract/standard account]

  X1 = f(x1, x2, x3) = x1 + (1 - x1)(1 - x2) x3,  all variables in [0,1].

The draft's formula is **correct** (validator check: it satisfies all four axioms below and reproduces Bulitko's worked values f(0.4,0.4,0.4) = 0.544 and f(0.5,0.5,1) = 0.75). Interpretation, per Bulitko [verified]: X1 is the readiness to choose the positive pole, x3 is the subject's intention (plan) to choose it, and x1, x2 are the world's influences on the subject. Reading the formula: x1 pushes straight to the positive pole; failing that, the intention x3 goes through only to the extent that x2 does not block it, so x2 acts as a veto on intention (pressure toward the negative pole). Lefebvre's axioms [verified]: free choice f(0,0,x3) = x3; credulity f(0,1,x3) = 0; non-evil-inclination f(1,x2,x3) = 1; simplicity (f affine in each argument separately). In the Boolean case the first three axioms fix f uniquely as f = (x3 → x2) → x1, i.e. x1 OR (x3 AND NOT x2); the real formula is exactly the multilinear extension of that Boolean function, which is what the simplicity postulate forces [verified, Bulitko; equivalence checked by validator]. A reflexive agent is obtained by substituting images into the arguments (x3 itself being the agent's image of its own choice), so the nesting is literal function composition.

The 1982/1980 "algebra of conscience" is a different and, for this project, more directly relevant construction [validator; see Unconfirmed]: a group is a complete graph whose edges are alliance or conflict; a decomposable graph is written as a Boolean polynomial with alliance and conflict as the two operations (the assignment swapped between the two "ethical systems"), and each agent's self-evaluation is read off the polynomial. That is a relation-to-operator mapping on a whole group.

Group-graph formalism of the 1982 form, as stated in Tarasenko (arXiv:1011.3397, section 2; full text read by the validator, not Lefebvre's *Lectures*): alliance is conjunction (product), conflict is disjunction (sum); a graph becomes a polynomial only if decomposable (validator's guess, unchecked: the forbidden four-subject graph is the induced path P4, so decomposable graphs would be the cographs; cf. Batchelder & Lefebvre, *J. Math. Psych.* 26: 124-148, 1982); the polynomial is stratified and folded with P^W = P + W-bar; each subject's variable satisfies the decision equation x = Ax + Bx-bar, solvable iff A contains B, with solutions A >= x >= B, otherwise "frustration"; the inverse task (reflexive control) finds influences that make a target alternative the solution. Per Umpleby 2016 (read), the two ethical systems come from whether the combination rule is addition or multiplication; which operation gives which system is not confirmed from the primary text. Related: Lefebvre, *Lectures on the Reflexive Games Theory* (Leaf & Oaks 2010), not read. For the military doctrine of reflexive control see 07 §4.

**What it captures.** Reflexive nesting (what A thinks B thinks A will do) as a literal algebraic structure; two normative "ethical systems" (one raises self-esteem by resolving conflict, the other by dramatising it) as differing forms of the function. Applied claims to Soviet-US negotiation modelling are on Wikipedia only.

**Limits.** Formal but narrow: binary choices, a particular function family, a conflict/ethics focus. Operators act on a single decision, not on a repertoire of social acts; roles and ongoing relations are not primitive. Whether the axioms describe anything fundamental is contested: Bulitko calls Lefebvre's justification "appealing" but not "bullet-proof" and criticises the simplicity postulate [verified]; a philosophy paper criticises the approach as misidentifying the structure of conscience (https://philarchive.org/rec/ZAICAA) [secondary, not read].

**Relevance.** The only work here with explicit algebraic operators over nested agent images, and (in the 1982 form) over a group's relation graph, so a direct predecessor for any "algebra of social agents". It gives *decision* algebra, not the *interaction* operators between persons.

---

## 4. Heider, Cartwright & Harary: balance theory

- Heider, F. (1946). Attitudes and cognitive organization. *The Journal of Psychology*, 21(1), 107-112. doi:10.1080/00223980.1946.9917275 (Crossref). Full text: https://psychclassics.yorku.ca/Heider/attitudes.htm . [verified]
- Heider, F. (1958). *The Psychology of Interpersonal Relations*. New York: Wiley. [verified, catalogue-level]
- Cartwright, D., & Harary, F. (1956). Structural balance: A generalization of Heider's theory. *Psychological Review*, 63(5), 277-293. doi:10.1037/h0046049 (Crossref). PDF: https://www.sitpor.org/wp-content/uploads/2015/08/STRUCTURAL-BALANCE-A-GENERALIZATION.pdf . [verified]
- Davis, J. A. (1967). Clustering and structural balance in graphs. *Human Relations*, 20(2), 181-187. doi:10.1177/001872676702000206 (Crossref). [verified]
- Harary, F. (1953-54). On the notion of balance of a signed graph. *Michigan Mathematical Journal*, 2(2), 143-146. (Wikipedia's balance-theory page gives pp. 153-6; most bibliographies and the signed-graph literature give 143-146.) [secondary]

**Operands.** Persons (and objects X) as nodes of a signed graph; Heider's P-O-X triad.

**Operators and formal structure.** One edge-level object: a sign in {+, -}. The sign of a path or cycle is the product of its edge signs (the two-element group under multiplication). A cycle is balanced if the product is positive; a signed graph is balanced if every cycle is. Structure theorem (Harary 1953; Cartwright & Harary 1956): **any** signed graph, not only a complete one, is balanced iff its nodes partition into two sets (one possibly empty) with positive edges within and negative between; equivalently, iff every two paths between the same pair of nodes have the same sign. [verified; the draft wrongly restricted it to complete graphs] Cartwright & Harary also handle directed graphs (balance on semicycles) and define a degree of balance as a proportion of positive cycles [validator]. Davis's clusterability weakens balance to "no cycle with exactly one negative edge", allowing more than two clusters. [verified] There is no operator for acts; "acts" appear only as sign changes that restore balance (Heider's motivational claim and later dynamic models). [from abstract/standard account]

**What it captures.** Local-to-global structure: constraints on cycles give a global partition of a group. A genuine mathematical structure (signed graphs, the group Z/2, product rule) with theorems.

**Limits.** One relation type, two values; no intensity (Flament critique per Wikipedia), no acts, and graph balance may not equal Heider's psychological balance (Anderson critique per Wikipedia). Dynamics are not part of the formal core.

**Relevance.** A working proof that sign multiplication on a relation graph yields group-level structure. Useful as the "static constraint" layer under an act algebra; not an act algebra itself.

---

## 5. Bales: Interaction Process Analysis and SYMLOG

- Bales, R. F. (1950). *Interaction Process Analysis: A Method for the Study of Small Groups*. Cambridge, MA: Addison-Wesley. Confirmed via https://en.wikipedia.org/wiki/Robert_F._Bales and https://bbi.syr.edu/projects/masters-series-on-field-research/interview-with-professor-robert-freed-bales/ (twelve categories). [verified]
- Bales, R. F., & Cohen, S. P. (1979). *SYMLOG: A System for the Multiple Level Observation of Groups*. New York: Free Press. Cited as Bales & Cohen 1979 in https://ese-journals.unisalento.it/index.php/psychofenia/article/view/i17201632vIVn6p79 ; publisher [validator]. [secondary]
- Bales, R. F. (1999). *Social Interaction Systems: Theory and Measurement*. New Brunswick, NJ: Transaction. [secondary]
- SYMLOG dimension description: https://sk.sagepub.com/ency/edvol/embed/processes/chpt/symlog and https://www.symlog.com/UsingSymlog/SYMLOGInDepth.aspx . [verified]

**Operands.** Group members; individual acts observed and coded.

**Operators and formal structure.** A coding scheme, not an algebra. IPA classifies each act into one of twelve categories (counts per member); SYMLOG places members (and acts, via rated items) in a three-axis space: Upward-Downward (dominance-submissiveness), Positive-Negative (friendliness-unfriendliness), Forward-Backward (acceptance-non-acceptance of task-oriented authority). The draft's reading of "26" was wrong [validator]: with three values (pole, neutral, other pole) on each of three axes there are 3^3 = 27 cells, i.e. 26 named directions (U, UP, UPF, ..., B) plus the neutral centre, and the 26 rating items are one per direction. So the items and the directions are the same 26. [from abstract/standard account]

**What it captures.** A measurement taxonomy of acts and a geometry for positions; basis for empirical group diagnosis and consulting.

**Limits.** Descriptive; no transformation law from act to state. Acts are labels, not operators.

**Relevance.** Candidate vocabulary and dimensional skeleton for acts, with decades of coding practice; the 3x3x3 lattice is a ready-made finite act space.

---

## 6. Interpersonal circumplex and complementarity (Leary, Kiesler, Wiggins)

- Leary, T. (1957). *Interpersonal Diagnosis of Personality*. New York: Ronald Press. Originator of the interpersonal circle per https://en.wikipedia.org/wiki/Interpersonal_circumplex ; publisher [validator]. [secondary]
- Kiesler, D. J. (1983). The 1982 interpersonal circle: A taxonomy for complementarity in human transactions. *Psychological Review*, 90(3), 185-214. doi:10.1037/0033-295X.90.3.185 (Crossref confirms; the draft's inferred DOI was right). [verified]
- Wiggins, J. S. (1979). A psychological taxonomy of trait-descriptive terms: The interpersonal domain. *Journal of Personality and Social Psychology*, 37(3), 395-412. doi:10.1037/0022-3514.37.3.395 (Crossref). [verified]
- Wiggins, J. S. (1996). An informal history of the interpersonal circumplex tradition. *Journal of Personality Assessment*, 66(2), 217-233. doi:10.1207/s15327752jpa6602_2 (Crossref). [verified]
- Carson, R. C. (1969). *Interaction Concepts of Personality*. Chicago: Aldine. Cited in the draft for complementarity, not listed; [validator].

**Operands.** An interpersonal act or style, positioned on a circle.

**Operators and formal structure.** Two orthogonal axes (vertical: agency, status, dominance; horizontal: communion, affiliation, warmth), usually eight octants (Kiesler's 1982 circle has sixteen segments), plus a radius for intensity. Any behaviour is a weighted combination of the two axes. *Complementarity* (Carson 1969; Kiesler 1983): reciprocity on the vertical axis (dominance invites submission) and correspondence on the horizontal (warmth invites warmth, hostility invites hostility). This is the nearest thing here to a rule "act a elicits act f(a)". Formally it is reflection of the circle in the horizontal axis (negate the vertical coordinate, keep the horizontal), an involution: applied twice it returns the original act. No source found presents it as an operator or examines that structure. [from abstract/standard account]

**What it captures.** A compact two-dimensional geometry of acts with an empirically supported pairing rule for dyadic exchange.

**Limits.** Dyadic; the rule is a tendency, not a law; octants are conventional; no groups, no persistence of relation state beyond a personality trait reading.

**Relevance.** A concrete, small act space with a response rule. Good candidate seed for a dyadic act table. See also Benjamin's SASB under "Missing", which is the more operator-like descendant.

---

## 7. Expectation states and status characteristics theory

- Berger, J., Cohen, B. P., & Zelditch, M. (1972). Status characteristics and social interaction. *American Sociological Review*, 37(3), 241-255. doi:10.2307/2093465 (Crossref). [verified]
- Berger, J., Fisek, M. H., Norman, R. Z., & Zelditch, M. (1977). *Status Characteristics and Social Interaction: An Expectation-States Approach*. New York: Elsevier. Catalogue: https://libcat.library.tamu.edu/Record/in00000331596 . [verified]
- Fisek, M. H., Berger, J., & Norman, R. Z. (1991). Participation in heterogeneous and homogeneous groups: A theoretical integration. *American Journal of Sociology*, 97(1), 114-142. doi:10.1086/229742 (Crossref confirms volume and pages that the draft had from memory). [verified]

**Operands.** Group members, characterised by states on status characteristics (two or more differentially valued states of a trait); task outcomes.

**Operators and formal structure.** Characteristics are linked, through "burden of proof" and relevance links, to task outcome, producing a graph of positive and negative paths from each member to the outcome. Expectations are aggregated across paths, and the basic expectation assumption makes a member's participation ranking a function of expectation advantage (Wikipedia: "a direct function of p's expectation advantage over o"; wording follows the Wikipedia article 'Expectation states theory', CC BY-SA 4.0). The combining function [validator]: each path of length i gets a strength f(i), decreasing with length; positive paths combine as e+ = 1 - Π(1 - f(i)), negative paths as e- = -[1 - Π(1 - f(i))], a member's aggregate is e+ + e-, and expectation advantage is the difference between two members' aggregates (the "organized subsets" principle). The process is *aggregation*, not composition of acts. [from abstract/standard account]

**What it captures.** How status differences (gender, race, expertise) produce a power-and-prestige order in task groups, and quantitative predictions of participation rates.

**Limits.** Operands are *status states*, not acts. The only "act" (an interaction opportunity or performance output) is an input to the aggregation; there is no general operator set, no relational types beyond status, and it is confined to task-oriented small groups.

**Relevance.** A well-tested formal sub-model for one operator type (status updating from interaction); cannot stand as the algebra.

---

## 8. Emerson, Willer: power-dependence and network exchange

- Emerson, R. M. (1962). Power-dependence relations. *American Sociological Review*, 27(1), 31-41. doi:10.2307/2089716 (Crossref). Full text read: https://umsl.edu/~keelr/3210/resources/emerson_power_depend.pdf . [verified]
- Emerson, R. M. (1976). Social exchange theory. *Annual Review of Sociology*, 2, 335-362. doi:10.1146/annurev.so.02.080176.002003 (Crossref confirms the pages the draft had from memory). [verified]
- Willer, D., & Anderson, B. (Eds.) (1981). *Networks, Exchange and Coercion: The Elementary Theory and Its Applications*. New York: Elsevier. First appearance of Elementary Theory per the SAGE entry "Willer, David" (https://sk.sagepub.com/ency/edvol/embed/socialtheory/chpt/willer-david). [secondary]
- Markovsky, B. (2005). Network exchange theory. In G. Ritzer (Ed.), *Encyclopedia of Social Theory*. SAGE. doi:10.4135/9781412952552.n204 (Crossref gives 2005, not the draft's 2007; pages 531-534 not confirmed). [verified, year corrected]
- Markovsky, B., Willer, D., & Patton, T. (1988). Power relations in exchange networks. *American Sociological Review*, 53(2), 220-236. doi:10.2307/2095689 (Crossref confirms ASR venue). A later chapter version: https://scholarcommons.sc.edu/socy_facpub/24 (Praeger 1999, pp. 87-108). [verified]

**Operands.** Actors (individuals or collectivities), exchange relations, resources, positions in an exchange network.

**Operators and formal structure.** Emerson (1962), read in full [verified]: dependence D_ab of A on B is directly proportional to A's motivational investment in goals mediated by B and inversely proportional to the availability of those goals to A outside the A-B relation; power P_ab is the resistance by B that A can potentially overcome; the premise is **P_ab = D_ba**, and a relation is the pair P_ab = D_ba, P_ba = D_ab. Balance is P_ab = P_ba; power advantage is P_ab - P_ba; cohesion is the average of D_ab and D_ba. From this notation Emerson derives "exactly four generic types of balancing operation" for an imbalance favouring A: (1) B withdraws motivational investment (withdrawal); (2) B cultivates alternatives (network extension); (3) B "gives status" to A, the more powerful party (A's investment in B rises; corrected 2026-10-29, checked against the 1962 text: "the third is based upon 'giving status' to A"); (4) A is denied alternatives (coalition and group formation, where two weaker actors unite and act as one). That is a small, closed, derived operator set, more than the draft (which had not verified it) credited. NET/Willer: a formal theory with defined terms and axioms, power measured by the Graph-theoretic Power Index (path counting: odd-length non-intersecting paths add advantage, even-length subtract), with resistance and vulnerability concepts. Acts are *exchanges* (offers, transactions); the result is a resource flow and a power profile for positions. [read]

**What it captures.** How network *structure* determines relative power in exchange; strong experimental programme.

**Limits.** One kind of act (resource exchange); no affect, norms or multiple relation types in the core; power is a derived measure of position. GPI is restricted to some network types (per a CRISP summary). Emerson's dependence is only ordinally specified ("the precise nature of this joint function is an empirical question").

**Relevance.** A mature precedent for graph-structure-to-outcome calculi, and Emerson's four operations are a genuine small operator set on a relation, including one (coalition) that turns two actors into a single group actor.

---

## 9. Kemper: status-power theory of emotions

- Kemper, T. D. (1978). *A Social Interactional Theory of Emotions*. New York: Wiley. [secondary; publisher validator]
- Scheve, C. von, & Kemper, T. D., handbook chapter preprint (https://www.polsoz.fu-berlin.de/soziologie/arbeitsbereiche/emotionen/team/Professur/preprints/Scheve_Kemper_HdE_preprint.pdf). Not text-extractable; nothing used from it. [unread]
- Thamm, R. (2004). Towards a universal power and status theory of emotion. In J. H. Turner (Ed.), *Theory and Research on Human Emotions* (Advances in Group Processes, 21), 189-222. Emerald/Elsevier. doi:10.1016/S0882-6145(04)21008-6. **Corrected:** the draft attributed this chapter to Kemper; Crossref and the Emerald record give the author as Robert Thamm, building on Kemper's dimensions. Kemper's own chapter in that volume is on Weber and Coleman. [verified]

**Operands.** Actors in a dyad; relation described by two relational dimensions.

**Operators and formal structure.** Status (voluntary compliance, deference given) and power (coercion, involuntary compliance) are the two relational channels; acts confer or withdraw status and use power, and the predicted emotion depends on whether the amount received is in excess, adequate or deficient and on who is held responsible (self, other, third party) [secondary/validator]. This is a cross-classification table, not an algebra. [from abstract/standard account]

**What it captures.** A mapping from a relational act (status given, status withheld, power used) to an emotion, a compact act-to-state table.

**Limits.** Emotion-centred; dyadic; no composition of acts; an informal, partly empirically supported scheme.

**Relevance.** Provides a small act-by-position table, similar in spirit to the operator tables the owner envisages, but only for emotions. Thamm (2004) is the attempt to universalise it to group structures.

---

## 10. Fararo and Skvoretz: mathematical sociology and E-state structuralism

- Fararo, T. J. (1973). *Mathematical Sociology: An Introduction to Fundamentals*. New York: Wiley-Interscience. Catalogue: https://lib.ecu.edu/catalog-preview/catalog/357754 . [verified]
- Fararo, T. J. (1989). *The Meaning of General Theoretical Sociology: Tradition and Formalization*. Cambridge University Press (ASA Rose Monograph). ISBN 9780521372589. [verified]
- Fararo, T. J., & Skvoretz, J. (1986). E-state structuralism: A theoretical method. *American Sociological Review*, 51(5), 591-602. doi:10.2307/2095486 (Crossref confirms; moved out of Unconfirmed). [verified]
- Fararo, T. J., Skvoretz, J., & Kosaka, K. (1994). Advances in E-state structuralism: Further studies in dominance structure formation. *Social Networks*, 16(3), 233-265. doi:10.1016/0378-8733(94)90007-8 (Crossref; year and co-authors corrected from the draft's "Fararo 1994?"). [verified]
- Skvoretz, J., Faust, K., & Fararo, T. J. (1996). Social structure, networks, and E-state structuralism models. *Journal of Mathematical Sociology*, 21(1-2), 57-76. doi:10.1080/0022250X.1996.9990174 (Crossref). [verified]
- Overview: https://en.wikipedia.org/wiki/Thomas_Fararo describes E-state structuralism as combining network theory with process, "E" for expectations (wording follows the Wikipedia article 'Thomas Fararo', CC BY-SA 4.0). [verified]

**Operands.** Actors in a network with expectation states (statuses); dyadic ties.

**Operators and formal structure.** Programme-level only: expectation states combined with network/structure processes, using stochastic process models of dominance-structure formation (each interaction event, such as an attack or deference, updates dyadic expectation states, and the hierarchy emerges from the sequence) [validator for the event-update gloss]. The formal state space and transition rules were not retrieved, so they are not described. [from abstract/standard account]

**What it captures.** A bridge between expectation states and emergent network structure (dominance hierarchies) with formal process models.

**Limits.** Not verified in detail here.

**Relevance.** Likely the closest sociological programme to "interaction sequences generating structure", worth a second pass with the 1986 and 1994 papers in hand.

---

## 11. Additions found (not in the brief)

- Lorrain, F., & White, H. C. (1971). Structural equivalence of individuals in social networks. *Journal of Mathematical Sociology*, 1(1), 49-80. doi:10.1080/0022250X.1971.9989788 (Crossref). [verified] The paper builds a category/semigroup of relations by composition and defines structural equivalence as having the same ties to all others. This is the **algebra of relations** line; with White, H. C., Boorman, S. A., & Breiger, R. L. (1976). Social structure from multiple networks. I. Blockmodels of roles and positions. *American Journal of Sociology*, 81(4), 730-780. doi:10.1086/226141 (Crossref). [verified] Relation composition (A is friend of B, B is boss of C, so A is friend-of-boss of C) is the nearest existing thing to operators-as-composition on persons. Covered in depth in `01-network-role-algebras.md`; flagged here because it is the strongest lead for the owner's aim.
- Harary, F., Norman, R. Z., & Cartwright, D. (1965). *Structural Models: An Introduction to the Theory of Directed Graphs*. New York: Wiley. [validator; not searched]

---

## What this cluster already covers

- **Acts as state transformations with a working model:** Affect Control Theory. Event grammar actor-behaviour-object, a fitted polynomial map on EPA vectors, deflection minimisation with a closed-form optimum, simulator, cross-cultural dictionaries.
- **Explicit algebra over nested agent images:** Lefebvre's reflexive model, with Boolean and [0,1]-valued functions fixed by four axioms; in the 1982 form, a group's alliance/conflict graph as a Boolean polynomial.
- **Group-level structure from local relation signs:** balance theory, with Z/2, the product rule and the two-set partition theorem for any signed graph.
- **Relation types with their own algebraic structure:** Fiske (four forms identified with nominal, ordinal, interval and ratio structures and a nested chain of invariance groups).
- **A small derived operator set on a relation:** Emerson's four balancing operations, derived from P_ab = D_ba.
- **Typologies of act types:** Bales/SYMLOG (12 act categories; 26 directions in a 3x3x3 space), circumplex (two axes, eight octants), Kemper (status and power acts to emotions).
- **A response rule between acts:** circumplex complementarity (an involution on the circle; informal, dyadic).
- **Structure-to-outcome calculi:** expectation states (path aggregation to participation), exchange networks (position to power index). [from abstract/standard account]

## What it does not cover

- **No single theory has persons, roles and groups all as operands with a general, closed set of social acts as operators and stated composition laws.** Lefebvre is the nearest in rigor but is about a binary decision; ACT is nearest in scope of acts but its transformation is fitted, and the actors are a pair.
- **No inverse, identity, associativity or closure analysis** of acts (what undoes a favour, whether "thank" after "give" equals "give" then "thank") in any of these. The genuine groups that do appear (Z/2 on edge signs in balance theory; the invariance groups behind Fiske's scale types) act on relation values, not on acts.
- **Groups as operands** are nearly absent: groups appear as graphs, partitions or polynomials, not as elements acted on. Partial exceptions: Emerson's coalition operation turns a set of actors into one actor, and Lefebvre's 1982 polynomial is a whole-group object.
- **Roles and positions as algebra:** only in the network-algebra line (Lorrain and White, White et al.), which is outside this cluster.
- **Time and sequence:** ACT handles event sequences, and E-state structuralism models sequences generating hierarchy; the others are mostly static or equilibrium.
- **Obligation, norm and commitment** as persistent state are not primitive anywhere here.
- Bales, Kemper and the circumplex are typologies or geometries and must not be described as algebras; Fiske has mathematical structure per relation type but no act operators.

## Missing from this survey (listed, not researched)

- Benjamin, L. S. (1974). Structural Analysis of Social Behavior (SASB), *Psychological Review*, 81, 392-425: a three-surface circumplex (focus on other, focus on self, introject) with named predictive principles (complementarity, introjection, antithesis) that are close to explicit operators on acts.
- Thibaut & Kelley (1959), *The Social Psychology of Groups*, and Kelley et al. (2003), *An Atlas of Interpersonal Situations*: interdependence theory, with outcome matrices and their decomposition (actor control, partner control, joint control) and transformations of the given matrix.
- Coleman, J. S. (1990), *Foundations of Social Theory* (and the 1973 linear system of action): actors, resources, control and interest as a linear exchange system.
- Gottman, Murray et al. (2002), *The Mathematics of Marriage*: dyadic influence functions as difference equations.
- Formal social-influence models (French 1956; DeGroot 1974; Friedkin & Johnsen): see `05-influence-opinion-control.md`.
- Doreian & Mrvar's signed blockmodelling (generalised balance for many clusters) and Heise's Event Structure Analysis (act sequences with prerequisite logic).
- Lawler's affect theory of social exchange and Ridgeway's status construction theory, the main formal descendants of the exchange and expectation-states lines.

---

## Unconfirmed

- **Fiske's own wording** for the CS/AR/EM/MP to nominal/ordinal/interval/ratio mapping, and his explicit use of Krantz-Luce-Suppes-Tversky measurement theory: the validator is confident Fiske makes the mapping himself (1991, 1992), but the only source text seen in this session is Wikipedia citing Fiske 1992, and IEP presents the symmetry chain as its own analysis.
- **ACT equation form**: the regression-with-interaction-terms description, the weighted squared deflection and the closed-form optimal behaviour are from the validator's knowledge of Heise (2007, Part II); not quoted from a source here. The draft's label "modified Gollob model" was not found anywhere and is dropped.
- **Lefebvre's variable meanings** beyond Bulitko's "x1 and x2 represent the world influence": Lefebvre's own glosses (Cogprints PDF, 1991 and 1995 sources) not read.
- **Lefebvre 1982 relation-graph polynomial** (alliance/conflict graph to Boolean polynomial, decomposability condition, the swap between ethical systems): validator's knowledge of the book and the 1980 JMP paper, not read in this session. Check the 1980 paper before relying on it.
- **Lefebvre, Algebra of Conscience 1982, series volume number and editor** (draft: TDL vol. 26, ed. Rapoport); and the draft's claim that Part 2 of the 2nd edition generalises 2x2 game theory with outcomes marked positive or negative.
- **Expectation-states combining function** (path strengths f(i), the organized-subsets formula): validator's knowledge; source is usually given as Berger, Norman, Balkwell & Smith (1992, ASR), not checked.
- **SYMLOG 26 directions / 27 cells**: validator's knowledge; the cited SYMLOG pages were not re-read.
- **Harary 1953 pages** (143-146 vs Wikipedia's 153-6) and year (1953 vs 1954 issue date).
- **Markovsky (2005) page range** 531-534.
- **Publishers from validator knowledge only**: Leary 1957 (Ronald), Bales & Cohen 1979 (Free Press), Kemper 1978 (Wiley), Carson 1969 (Aldine), Harary-Norman-Cartwright 1965 (Wiley).
- **Umpleby (2016)** venue.
- **Scheve and Kemper Handbook of Emotions chapter**: PDF not readable; contents not used.
- **ZAICAA critique of Lefebvre** on PhilArchive: not read.

---

## Validation log (2026-10-29)

Method: every DOI resolved against Crossref; Emerson (1962) and Bulitko (2002) read in full; Fiske 1992 abstract read via OpenAlex; Wikipedia (ACT, balance theory, relational models), IEP and search results for the rest.

1. Fiske 1991 *Structures of Social Life* — ✓ confirmed.
2. Fiske 1992 *Psych Rev* 99(4) — ✓ confirmed (DOI, abstract, "19 experimental studies"); ✎ corrected the analysis: the scale-type mapping is formal structure, not a "loose analogy".
3. Heise 2007 *Expressive Order* — ✓ confirmed (DOI).
4. Heise 1979 *Understanding Events* — ✓ confirmed (secondary); ✎ full subtitle added.
5. Averett & Heise 1987 — ✓ confirmed (DOI, issue).
6. Interact / Franklin ACT site — ✓ existence.
7. Hoey et al. 2013 — ✎ corrected author order (Hoey, Schröder, Alhothali) and added pages.
8. ACT impression-formation, deflection, optimum — ✎ form supplied from validator knowledge (? in Unconfirmed); "modified Gollob" ✗ removed as unsourced.
9. Lefebvre 1982 *Algebra of Conscience* — ✓ confirmed; ? series number and editor moved to Unconfirmed.
10. Lefebvre 1980 *JMP* — ✎ corrected from [secondary] to verified, full citation and DOI added.
11. Lefebvre 1985 *JMP* — ✎ same.
12. Lefebvre "Law of self-reflexion" (Cogprints) — ? exists, unread (403).
13. Lefebvre's formula X1 = x1 + (1 - x1)(1 - x2)x3 — ✓ confirmed correct, with axioms; ✎ source corrected to Bulitko, interpretation and Boolean form (x3 → x2) → x1 added.
14. Bulitko 2002 arXiv — ✎ corrected: author is V. K. Bulitko, the paper was read, not "not decoded".
15. Umpleby 2016 — ? venue unconfirmed.
16. Heider 1946 — ✓ confirmed.
17. Heider 1958 — ✓ confirmed.
18. Cartwright & Harary 1956 — ✓ confirmed; ✎ structure theorem corrected (any signed graph, not only complete; one class may be empty).
19. Davis 1967 — ✓ confirmed (DOI added).
20. Harary 1953 — ✎ pages and volume added; ? 143-146 vs 153-6 discrepancy.
21. Bales 1950 — ✓ confirmed.
22. Bales & Cohen 1979 — ✓ confirmed (secondary), publisher from validator.
23. Bales 1999 — ✓ confirmed (secondary).
24. SYMLOG "26" — ✎ corrected: 26 items are one per direction of the 3x3x3 space.
25. Leary 1957 — ✓ (secondary), publisher from validator.
26. Kiesler 1983 — ✓ confirmed, DOI resolved (the inferred DOI was correct).
27. Wiggins 1979 — ✓ confirmed (title, pages, DOI), moved out of Unconfirmed.
28. Wiggins 1996 — ✓ confirmed; ✎ title added.
29. Berger, Cohen & Zelditch 1972 — ✓ confirmed, DOI added.
30. Berger et al. 1977 — ✓ confirmed.
31. Fisek, Berger & Norman 1991 — ✓ confirmed, volume and pages from memory were right.
32. Emerson 1962 — ✓ confirmed and read; ✎ P_ab = D_ba and the four balancing operations now stated (were unverified), DOI added.
33. Emerson 1976 — ✓ confirmed, pages from memory were right.
34. Willer & Anderson 1981 — ✓ (secondary).
35. Markovsky, Encyclopedia of Social Theory — ✎ year corrected 2007 → 2005.
36. Markovsky, Willer & Patton 1988 — ✓ confirmed (ASR 53(2)), moved out of Unconfirmed.
37. Kemper 1978 — ✓ (secondary).
38. Scheve & Kemper preprint — ? unread.
39. "Kemper 2004, Toward a universal power and status theory of emotion" — ✎ corrected: the chapter is by Robert Thamm, pp. 189-222.
40. Fararo 1973 — ✓ confirmed.
41. Fararo 1989 — ✓ confirmed.
42. Fararo & Skvoretz 1986 *ASR* — ✓ confirmed (was Unconfirmed), DOI added.
43. "Fararo 1994?" — ✎ corrected to Fararo, Skvoretz & Kosaka 1994, pp. 233-265.
44. Skvoretz, Faust & Fararo 1996 — ✓ confirmed, volume and pages added.
45. Lorrain & White 1971 — ✓ confirmed, DOI added.
46. White, Boorman & Breiger 1976 — ✓ confirmed, volume 81(4) 730-780 added.
47. Harary, Norman & Cartwright 1965 — ? not checked.
48. Closing verdict — ✎ corrected "Balance theory's Z/2 is the only genuine group", "groups as operands essentially absent", and the Fiske "typology" label; added Emerson's operator set.

No fabricated works were found. One misattribution (Thamm's chapter given to Kemper) was the only bibliographic error that changed who wrote something.

**Verdict.** Bibliographically the survey is sound: every work exists, and every from-memory volume and page detail that could be checked was right; the errors were one misattributed chapter, one wrong year, one wrong author order and one incomplete co-author list. The analytical layer was weaker than the citations: it misstated the balance-theory structure theorem (restricting it to complete graphs), misread SYMLOG's 26, and systematically underclaimed formal structure (Fiske's scale types, Emerson's derived four operations, Lefebvre's group-level polynomial), which matters because those are exactly the precedents the algebra could build on. Lefebvre's formula, the item most at risk, is correct.

---

## Licences of quoted and transcribed material (2026-10-30)

Nothing in this file is a transcribed table or dataset. Every use is a short quotation, a restated equation or a description. Citations, facts and numbers are free.

- **Wikipedia, 'Affect control theory'**: CC BY-SA 4.0. Two short quotations (6 and 4 words) in section 2, now marked.
- **Wikipedia, 'Expectation states theory'**: CC BY-SA 4.0. One short quotation (10 words) in section 7, now marked.
- **Wikipedia, 'Relational models theory'** (citing Fiske 1992): CC BY-SA 4.0. Close paraphrase of the model-to-measurement-scale mapping in section 1, now marked.
- **Wikipedia, 'Thomas Fararo'**: CC BY-SA 4.0. Close paraphrase of the E-state structuralism description in section 10, now marked.
- **Wikipedia, 'Vladimir Lefebvre'**, 'Interpersonal circumplex', 'Robert F. Bales', 'Affect control theory' (publications list): CC BY-SA 4.0. Used only as the place a citation or fact was found; no wording taken.
- **Bulitko (2002), arXiv:math/0205325**: arXiv licence for this paper not recorded; not determined; publisher copyright presumed. Used as restated equation (the readiness function, its four axioms, worked values), not copied text. Record the licence before this goes public.
- **Tarasenko, arXiv:1011.3397, section 2**: arXiv licence not recorded; not determined; publisher copyright presumed. Used as a restated summary of the group-graph formalism. Record the licence before this goes public.
- **Emerson (1962), Am. Sociol. Rev. 27(1)**: publisher copyright (ASA/JSTOR). Full text was read from a hosted copy (umsl.edu) whose provenance is not recorded; check that it is a legitimately provided copy. Used as restated equations (P_ab = D_ba) and a description of the four balancing operations, plus one short phrase.
- **Fiske 1992, Psychological Review**: publisher copyright (APA). Abstract only; used as description.
- **Heise (2007, Springer), Lefebvre (1980, 1982, 1985), Heider (1946, 1958), Cartwright & Harary (1956), Davis (1967), Harary (1953), Bales, Leary, Kiesler, Wiggins, Berger et al., Kemper, Thamm, Fararo and Skvoretz, Lorrain and White, White et al.**: not determined; publisher copyright presumed. Cited only, with restated results in our own words; no quotation or transcription.
- **Heider (1946)** full text at psychclassics.yorku.ca: linked, not reproduced.
- **IEP, 'Relational models'**: not determined; publisher/author copyright presumed. Cited for the symmetry-chain observation, restated.
- **Umpleby (2016), SAGE/SYMLOG pages, CRISP summary**: not determined; publisher copyright presumed. Cited and paraphrased only.
