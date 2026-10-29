# Prior work: economics, political science, non-kinship anthropology, linguistics, network statistics

Date: 2026-10-29. Survey for the `social-algebra` strand. Aim (Aldred): identify the mechanics of a social group as operators and operands, to model interactions later.

## Summary

This cluster does not contain one algebra of groups, but it contains most of the pieces, and in very different degrees of formality.

- **Formal, fully specified, predictive:** cooperative game theory and power indices (operand: set of players, characteristic function; operator: coalition formation, marginal contribution); Jackson-Wolinsky network formation (operand: graph; operators: add link, sever link); SAOMs, ERGMs and relational event models (operand: network state; operators: one tie change, one dyadic event, each with an explicit rate/probability law). These are the nearest thing to a calculus of "what can happen next".
- **Formal but with only one kind of operand:** veto-player theory, selectorate theory, Axelrod's conflict of interest. Operands are actors with positions or loyalties; the "operator" is a decision rule, not a set of moves.
- **Informal but the right operator vocabulary:** Mauss, Sahlins, van Gennep/Turner, Barth, Bailey, Boissevain, Goffman-style face work. These name the moves (give, receive, reciprocate; separate, liminal, incorporate; transact, manage, broker) and none gives a closed notation.
- **One half-formal grammar worth copying:** Crawford and Ostrom's ADICO syntax is the only item here that is literally a grammar for statements about what actors may/must do. Brown-Levinson's weightiness formula is the only one that gives an additive "cost of a move" law.
- **Verification note.** Bibliographic records were verified through the Crossref API (DOIs below). Content claims were verified from fetched primary text only for Akerlof-Kranton (full equations, from the paper PDF); everything else rests on secondary pages, search abstracts, or reviews and is labelled. Items not confirmed at all are listed under "Unconfirmed". The much-quoted CIA "90 percent" figure for Bueno de Mesquita was traced in the validation pass to its primary source (Feder 1987); it says something narrower than the popular version (see item 3).

Entry count: 27 numbered entries (A politics 1-6, B economics and game theory 7-13, C anthropology 14-18, D linguistics 19-21, E network statistics 22-25, F additions 26-27), plus an Unconfirmed list.

---

## A. Political science

### 1. Riker, *The Theory of Political Coalitions* (1962)
- **Citation:** William H. Riker, *The Theory of Political Coalitions*, Yale University Press, 1962.
- **Verification:** Existence confirmed via reviews in Crossref: Midwest J. Political Science 1963, doi:10.2307/2109034; Western Political Quarterly 1963, doi:10.2307/445870 (DOIs of reviews, not of the book). Wikipedia page https://en.wikipedia.org/wiki/The_Theory_of_Political_Coalitions exists (not read in detail).
- **Their vocabulary:** winning coalition, minimal winning coalition, size principle, zero-sum n-person game, side payments.
- **Operands (translated):** a set of players with weights (votes) and a winning rule; a coalition is a subset.
- **Operators (translated):** "join/form a coalition"; the output is the subset that forms. Formal: von Neumann-Morgenstern n-person zero-sum game with side payments; size principle, in Riker's words: "In social situations similar to n-person, zero-sum games with side-payments, participants create coalitions just as large as they believe will ensure winning and no larger." With complete and perfect information this means minimal winning coalitions; Riker's "information effect" predicts oversized coalitions when information is imperfect. A derivation, not a notation.
- **Predictive/control claim:** coalitions will be minimal winning. Held up partly. Search-retrieved abstracts: Butterworth (1971, APSR) argued the derivation unsound in general; Shepsle (1974) replied that under a reasonable solution concept it holds; Laakso, "Riker's 'Size Principle' and its application to Finnish roll-call data", *Scandinavian Political Studies* 7 (1972), found support in 150 roll calls under three cabinets (abstract confirmed in validation); a secondary paper cites Mitchell and Nyblade (2006, not located as a primary; their chapter in Strøm, Müller and Bergman (eds), *Cabinets and Coalition Bargaining*, OUP 2008, is the likely published form) finding roughly two-fifths of majority coalitions were oversized. Net: a baseline, frequently violated once policy matters (see 5).
- **Limits:** zero-sum and full-information assumptions; no policy content; no dynamics; no roles beyond "member".
- **Relevance:** the first clean case of "operand = subset of a weighted set, operator = form/dissolve". Shows what assumptions buy a theorem.

### 2. Olson, *The Logic of Collective Action* (1965)
- **Citation:** Mancur Olson, *The Logic of Collective Action: Public Goods and the Theory of Groups*, Harvard University Press, 1965.
- **Verification:** Crossref has reviews/derivatives (e.g. Land Economics review essay 1967, doi:10.2307/3145551; Hindmoor, *Rational Choice*, doi:10.1007/978-0-230-20997-8_5; these are DOIs of reviews/derivative works, not of the book). The book itself was not located in Crossref this session; the content below is from search-result summaries.
- **Their vocabulary:** collective good, free rider, selective incentive, latent group, privileged/intermediate/latent group by size.
- **Operands:** individuals as contributors to a shared good; group size as a parameter.
- **Operators:** contribute / free-ride; selective incentive (reward or punishment applied to individuals) as the operator that changes the contribute/free-ride payoff. Informal verbal theory with a simple cost-benefit logic.
- **Predictive claim:** large groups under-provide collective goods without selective incentives. Search results report later critique: the size effect can reverse when the good's jointness of supply is high (Chamberlin 1974; Oliver and Marwell's critical-mass work), and size is often empirically an asset (union influence). Olson's argument is that in a large group each member's contribution has a negligible effect on provision and is unnoticeable to others, so rational members free-ride; small ("privileged") groups may provide because one member gains enough to supply alone.
- **Limits:** one-shot, atomistic, no structure inside the group; ignores reciprocity and network structure.
- **Relevance:** supplies the canonical "defect/cooperate under group size" operator pair and the idea that a second-order operator (incentive) acts on the first.

### 3. Bueno de Mesquita, Smith, Siverson and Morrow, *The Logic of Political Survival* (2003), and BdM's forecasting model
- **Citation:** B. Bueno de Mesquita, A. Smith, R. M. Siverson, J. D. Morrow, *The Logic of Political Survival*, MIT Press, 2003. doi:10.7551/mitpress/4292.001.0001. Forecasting: B. Bueno de Mesquita, "A decision making model: its structure and form", *International Interactions* 23 (1997), doi:10.1080/03050629708434909; B. Bueno de Mesquita and F. N. Stokman (eds), *European Community Decision Making* (Yale UP, 1994), ch. 4 "Political Forecasting: An Expected Utility Method", doi:10.12987/9780300158113-007; B. Bueno de Mesquita, D. Newman and A. Rabushka, *Forecasting Political Events: The Future of Hong Kong* (Yale, 1985; reviews doi:10.2307/2131621, 10.2307/1960943, 10.2307/2758844; DOIs of reviews, not of the book).
- **Their vocabulary:** nominal selectorate, real selectorate S, winning coalition W, loyalty norm W/S, revenue R, private vs public goods; for the forecasting model: actors with position, salience, clout (influence), resolve; "median voter" positions; bargaining rounds.
- **Operands:** leader; selectorate S; subset W of S whose support is needed. In the forecasting model: a list of stakeholders, each with a numeric position on an issue, a salience and a clout.
- **Operators:** leader allocates revenue R between public goods and private payoffs to W; supporters defect or stay; challenger offers a better deal. In the forecasting model, iterated pairwise expected-utility comparisons (each actor evaluates challenging each other actor) that shift positions round by round. Selectorate theory is a formal game model with comparative statics. The forecasting model is a computable algorithm; its core expected-utility logic is published (1994 chapter, 1997 *International Interactions* paper; Feder 1987 prints the support rule: A's support for outcome B = A's resources x salience of the issue to A x A's utility for B), but the complete operational version used commercially is not, which is why Scholz et al. had to reconstruct it. [from abstract/standard account]
- **Predictive/control claim:** Selectorate: W/S is the loyalty norm: small W/S means strong loyalty and long leader tenure; small W (in absolute size) favours private goods to the coalition, large W favours public goods (the theory predicts on W for goods and on W/S for loyalty and survival, which the earlier wording ran together) (Wikipedia summary, https://en.wikipedia.org/wiki/Selectorate_theory; Weeks criticises its assumptions about autocracies). Forecasting: widely repeated claim that a declassified CIA assessment rated the model about 90 percent accurate. **Traced to primary text in the validation pass.** Source: Stanley A. Feder, "FACTIONS and Policon: New Ways to Analyze Politics", *Studies in Intelligence* 31(1), Spring 1987, pp. 41-57 (originally Secret/Noforn), reprinted in H. B. Westerfield (ed.), *Inside CIA's Private World* (Yale UP, 1995), pp. 274ff; read from a scan of the reprint. What it says, verbatim: "forecasts done with traditional methods and with Policon were found to be accurate about 90 percent of the time. Thus, while traditional and Policon-based analyses both scored well in terms of forecast accuracy, Policon offered greater detail and less vagueness." Supporting figures: 60 percent of Policon analyses (Oct 1982 - Oct 1985) forecast specific outcomes versus 33 percent of Directorate of Intelligence analyses; "Policon analyses got the bull's-eye twice as often". **So the article supports:** about 90 percent accuracy for Policon in in-house CIA use, 1982-85, across "scores" of issues in over 30 countries. **It does not support:** that the model beat CIA analysts on accuracy (they tied, per the same sentence); any independent or out-of-sample audit (the author was an in-house advocate and no scoring method, case count or criterion for "accurate" is given in the passage); or the name Bueno de Mesquita, which the article never mentions. It describes Policon as "developed by Policon Corp. and used by the CIA under contract from 1982 until 1986"; the link to BdM rests on his own accounts (e.g. *The Predictioneer's Game*, 2009, and the *Foreign Policy* piece the Wikipedia entry https://en.wikipedia.org/wiki/Bruce_Bueno_de_Mesquita footnotes). FACTIONS was a near-identical CIA in-house version (Office of Research and Development). A critic (Walt) is quoted saying most forecasts are proprietary and cannot be verified. Scholz, Calbert and Smith (2011, SciTePress, https://www.scitepress.org/Papers/2011/31215) report that no clear specification is in the open literature, reconstruct it from published sources, and discuss sensitivity and convergence concerns.
- **Limits:** forecasting model is not independently auditable; selectorate theory is regime-level, not interaction-level; positions and salience are scalar inputs that someone must estimate.
- **Relevance:** the most explicit attempt at "list the actors, give each numbers, simulate what each does to each". Useful as a template for an operand record (position, salience, clout, resolve) and a warning that without open specification the track record is unverifiable.

### 4. Shapley-Shubik and Banzhaf power indices
- **Citation:** L. S. Shapley and M. Shubik, "A method for evaluating the distribution of power in a committee system", *APSR* 48 (1954), doi:10.2307/1951053. Shapley, "A value for n-person games", in *Contributions to the Theory of Games II* (1953), doi:10.1515/9781400881970-018. J. F. Banzhaf III, "Weighted voting doesn't work: a mathematical analysis", *Rutgers Law Review* 19(2), 317-343 (1965) (confirmed in validation via multiple citing records; no DOI; the index was anticipated by L. S. Penrose 1946 and re-derived by J. S. Coleman 1971).
- **Their vocabulary:** characteristic function, pivotal player, Shapley value, swing, power index.
- **Operands:** a voting game: players, weights, quota; a coalition is a subset.
- **Operators:** adding a player to a coalition (marginal contribution). Shapley-Shubik power of i = share of orderings of the players in which i is pivotal (turns a losing coalition into a winning one). Banzhaf power of i = number of winning coalitions in which i is a swing (removing i makes it losing), usually normalised by the total swings (or by 2^(n-1) for the absolute index). Difference: Shapley-Shubik weights orderings (permutations), Banzhaf weights coalitions (subsets) equally; the two can rank players differently. Fully formal; closed-form definitions; both standard and confirmed from general knowledge, consistent with Banzhaf's Nassau County application. [from abstract/standard account]
- **Predictive claim:** measures a priori voting power, not behaviour. Known to differ from nominal weight (no claim verified here).
- **Limits:** treats all orderings or all coalitions as equally likely; ignores preferences, so power is context-free.
- **Relevance:** gives a ready-made operator, "marginal contribution of an operand to a coalition", and shows that "weight" and "influence" are different quantities. Directly reusable as one candidate measure.

### 5. Axelrod, *Conflict of Interest* (1970)
- **Citation:** Robert Axelrod, *Conflict of Interest: A Theory of Divergent Goals with Applications to Politics*, Markham, Chicago, 1970. Reviews: doi:10.2307/1958375 (APSR), doi:10.2307/2110125 (Midwest J. Pol. Sci.) (DOIs of reviews, not of the book). Earlier: "Conflict of interest: an axiomatic approach", *J. Conflict Resolution* 11 (1967), doi:10.1177/002200276701100107.
- **Their vocabulary:** conflict of interest, minimal connected winning coalition, policy range.
- **Operands:** actors with positions on a line (e.g. left-right) and a payoff structure over outcomes; conflict of interest is defined as incompatibility of goals.
- **Operators:** coalition choice minimising the spread of positions among members. Formal measurement of conflict (axioms in the 1967 paper); coalition rule is a hypothesis. [from abstract/standard account]
- **Predictive claim:** (from review abstracts) the minimal connected winning (MCW) theory fits the post-war Italian coalitions Axelrod analysed (the "ten cases" count in the first draft was not confirmed); later work questioned the interval-scale assumption and the coding of abstentions. Closely tied to Leiserson's minimal range theory. V. C. H. Chua and D. S. Felsenthal, "Coalition formation theories revisited: an empirical investigation of Aumann's hypothesis", in M. Braham and F. Steffen (eds), *Power, Freedom, and Voting* (Springer, 2008), found Aumann's hypothesis (the formateur builds the coalition maximising its own Shapley value) did worse than closed-minimal-range theory (search-level confirmation).
- **Limits:** a single policy dimension; coalitions as static outcomes.
- **Relevance:** introduces a distance metric between actors as the thing the coalition operator acts on. A candidate primitive: d(a, b) = conflict of interest.

### 6. Tsebelis, *Veto Players* (2002; 1995 article)
- **Citation:** George Tsebelis, "Decision making in political systems: veto players in presidentialism, parliamentarism, multicameralism and multipartyism", *BJPolS* 25 (1995), doi:10.1017/s0007123400007225; *Veto Players: How Political Institutions Work*, Princeton UP, 2002, doi:10.1515/9781400831456.
- **Their vocabulary:** veto player, status quo, winset, absorption rule, policy stability.
- **Operands:** veto players, each with an ideal point and a status quo point in policy space.
- **Operators:** a change from status quo to a new point passes only if every veto player weakly prefers it. Policy stability is **inversely** related to the size of the winset of the status quo (the intersection of the veto players' individual win sets): the smaller that intersection, the more stable policy. Formal, spatial-geometric; the absorption rule (a player whose position lies within the others' win set adds no constraint) is a reduction rule on the operand list. The Wikipedia summary (https://en.wikipedia.org/wiki/Veto_player) states the unanimity condition but not the absorption rule; the rule itself comes from the book, not read here.
- **Predictive claim:** more veto players, or greater distance between them, means less policy change. Wikipedia notes (with "citation needed" on the general claim) that the consensus-democracy inflexibility prediction was not confirmed (McGann and Latner 2013), and that treating coalition partners as veto players is contested.
- **Limits:** one-shot; no cost of getting to agreement; ignores agenda control, which in other work matters more than veto count.
- **Relevance:** a clean example of an operator that is a conjunction over operands, and of a reduction rule (absorption) that simplifies expressions. This is what algebraic structure looks like in political science.

---

## B. Economics and game theory

### 7. Cooperative game theory: the core and coalition structures
- **Citation:** D. B. Gillies, "Solutions to general non-zero-sum games", in *Contributions to the Theory of Games IV* (1959), doi:10.1515/9781400882168-005. R. J. Aumann and J. H. Drèze, "Cooperative games with coalition structures", *Int. J. Game Theory* 3 (1974), doi:10.1007/bf01766876.
- **Their vocabulary:** characteristic function v(S), imputation, core, coalition structure.
- **Operands:** a set N of players; a worth function v on subsets; a partition of N (coalition structure).
- **Operators:** form/dissolve a coalition; divide v(S) among members; blocking (a coalition rejects an imputation if it can do better alone). Fully formal.
- **Predictive claim:** the core predicts which allocations are stable against coalitional deviation; Aumann's hypothesis (as tested by Chua and Felsenthal, search-reported) did worse than minimal-range theories on cabinet data.
- **Limits:** v is exogenous, no sequence, no communication constraints, core can be empty.
- **Relevance:** "stability against blocking coalitions" is the best-developed notion of when a group configuration holds. A candidate invariant.

### 8. Myerson, "Graphs and cooperation in games" (1977)
- **Citation:** R. B. Myerson, *Math. Oper. Res.* 2(3), 225-229, doi:10.1287/moor.2.3.225.
- **Vocabulary:** graph-restricted game, communication structure.
- **Operands:** players plus a graph of who can communicate; a coalition's worth counts only its connected components.
- **Operators:** link addition/deletion changes v; Myerson value allocates. Formal.
- **Claim:** none empirical.
- **Relevance:** the bridge between games on sets and games on networks. Exactly the sort of two-sorted structure (set plus graph) a social algebra needs.

### 9. Jackson and Wolinsky, network formation (1996); Jackson, *Social and Economic Networks* (2008)
- **Citation:** M. O. Jackson and A. Wolinsky, "A strategic model of social and economic networks", *J. Econ. Theory* 71 (1996), doi:10.1006/jeth.1996.0108. M. O. Jackson, *Social and Economic Networks*, Princeton UP, 2008, doi:10.1515/9781400833993. Also Bala and Goyal, "A noncooperative model of network formation", *Econometrica* 68 (2000), doi:10.1111/1468-0262.00155.
- **Vocabulary:** pairwise stability, efficiency, connections model, link formation/severance.
- **Operands:** a graph g on players with a payoff function per player.
- **Operators:** add link ij (needs both consent), delete link ij (unilateral). Pairwise stability: no player gains by deleting an existing link and no pair both gain by adding a missing one. Fully formal. The connections model, u_i(g) = sum over j != i of delta^{t(ij)} - sum over j with ij in g of c (t(ij) = shortest-path distance, 0<delta<1), is confirmed from standard knowledge of the paper (its general form uses w_ij and c_ij). [from abstract/standard account]
- **Claim:** abstract (retrieved via search): there does not always exist a stable network that is efficient. Precisely: no allocation rule that is anonymous and component-balanced guarantees that some strongly efficient network is pairwise stable for every value function; the conflict can be resolved only by rules that violate one of those conditions. Not an empirical claim.
- **Limits:** equilibrium thinking; no timing; payoffs exogenous.
- **Relevance:** the cleanest explicit operator set for relationships: add (bilateral), sever (unilateral). The asymmetry of consent is a structural fact worth putting in the algebra at the start.

### 10. Akerlof and Kranton, "Economics and Identity" (2000)
- **Citation:** *QJE* 115(3), 715-753. doi:10.1162/003355300554881. Full text read.
- **Their vocabulary:** identity, social category C, assignment c_j, prescriptions P, gains and losses in identity.
- **Operands (verified from the paper, Section III.A):** each person j has actions a_j; an assignment c_j of everyone (including j) to social categories C; characteristics epsilon_j; prescriptions P, the behaviour (and ideal attributes) appropriate to each category; categories carry social status.
- **Operators/structure (verified):** U_j = U_j(a_j, a_-j, I_j) and I_j = I_j(a_j, a_-j; c_j, epsilon_j, P). Identity utility rises when one's own and others' actions match the prescriptions for one's assigned category and when one's characteristics match the category ideal. Actions can also change c_j (switch category), P (alter prescriptions) or category status. The paper names worked cases: violating prescriptions draws scorn and ostracism; changing group; advertising and schools as deliberate manipulation of P. It is a utility model with a formal structure; there is no algebra of category change, but the mechanism is explicit. [read]
- **Predictive claim:** equilibrium predictions for gender in the workplace, schooling, poverty and exclusion. Wikipedia (https://en.wikipedia.org/wiki/Identity_economics) lists later applications; no empirical scorecard was gathered here.
- **Limits:** the category set and prescriptions are exogenous inputs; utility maximisation hides the process.
- **Relevance:** among the best fits to the goal. It gives three operand types (person, category, prescription) and three actions on them (act per P, change category, change P). Reads almost as a type signature already.

### 11. Schelling, focal points and segregation
- **Citation:** T. C. Schelling, *The Strategy of Conflict*, Harvard UP, 1960 (prospectus: *J. Conflict Resolution* 2 (1958), doi:10.1177/002200275800200301). "Dynamic models of segregation", *J. Math. Sociology* 1 (1971), doi:10.1080/0022250x.1971.9989794.
- **Vocabulary:** focal point, tacit coordination, salience; tipping.
- **Operands:** agents with a threshold preference over neighbour composition; or players choosing among options without communication.
- **Operators:** move if neighbourhood composition falls below tolerance (segregation); choose the salient option (focal point). The segregation model is an explicit agent-based rule; focal points are informal.
- **Claim:** mild individual preferences produce strong collective segregation. Search results report experimental support for focal points in pure coordination games and much weaker support when interests conflict.
- **Limits:** salience is not derived; it is imported from culture. The segregation rule is stylised.
- **Relevance:** supplies the idea that what coordinates a group is partly a shared salient fact outside the formalism: a "common-knowledge operand".

### 12. Bowles and Gintis
- **Citation:** S. Bowles and H. Gintis, *A Cooperative Species: Human Reciprocity and Its Evolution*, Princeton UP, 2011, doi:10.1515/9781400838837.
- **Vocabulary:** strong reciprocity, altruistic punishment, group competition.
- **Operands:** individuals with social preferences, groups.
- **Operators:** cooperate, punish defectors at personal cost, imitate. Models are formal (evolutionary game / multilevel selection); this entry was verified only as a bibliographic record, content not read.
- **Claim:** not assessed.
- **Relevance:** pairs with Olson: second-order operator (punish). Overlaps with the biology agent's cluster, so left shallow.

### 13. Rubinstein and Spence (bargaining and signalling)
- **Citation:** A. Rubinstein, "Perfect equilibrium in a bargaining model", *Econometrica* 50 (1982), doi:10.2307/1912531. M. Spence, "Job market signaling", *QJE* 87 (1973), doi:10.2307/1882010.
- **Why listed:** the canonical sequential-offer operator (propose/accept/reject) and the canonical costly-signal operator (send a signal whose cost differs by type). Bibliographic records verified only; content not read this session, so no further claims made.
- **Relevance:** candidate primitives for any later interaction layer.

---

## C. Anthropology (non-kinship)

### 14. Mauss, *The Gift*
- **Citation:** Marcel Mauss, *Essai sur le don* (1923-24); English edition in Routledge reissue, doi:10.4324/9781003572350 (2024) (DOI of reprint, not of the original book). Review: *ASR* 1956, doi:10.2307/2088549 (DOI of review, not of the book).
- **Vocabulary:** gift, obligation to give, receive, reciprocate; total prestation.
- **Operands:** persons and groups as exchange partners; objects as carriers of obligation.
- **Operators:** give, receive, return. The three obligations (to give, to receive, to reciprocate) are stated in Mauss's own text (Introduction and ch. 1, on the hau and potlatch); confirmed from standard knowledge of the work. Informal. No formal notation.
- **Claim:** descriptive and comparative, not predictive.
- **Relevance:** gives a minimal operator triple with an obvious composition law: give followed by an obligation to return. The structure of "debt" as a state variable on an ordered pair.

### 15. Sahlins, spectrum of reciprocity
- **Citation:** Marshall Sahlins, "On the sociology of primitive exchange" (1965; in *Stone Age Economics*, Aldine, 1972), doi:10.4324/9781315184951-5 (DOI of a reprint chapter, not of the original).
- **Vocabulary:** generalized, balanced, negative reciprocity.
- **Operands:** pairs of actors with a kinship/residential distance.
- **Operators:** generalised = near-pure gift with no stated return; balanced = direct exchange of customary equivalents; negative = attempt at something for nothing with impunity. The correlation with kinship-residential distance is Sahlins's own model (his concentric "sectors": household, lineage, village, tribe, intertribal), not a later secondary gloss. First published in M. Banton (ed.), *The Relevance of Models for Social Anthropology*, ASA Monographs 1, Tavistock, 1965. Definitions confirmed against standard knowledge; the first draft took them from Wikipedia (https://en.wikipedia.org/wiki/Reciprocity_(cultural_anthropology)). Informal ordinal scale.
- **Claim:** reciprocity type correlates with social distance. Not rigorously tested in what was retrieved.
- **Relevance:** one scalar (distance) selects among a small set of operator variants. A useful design pattern: operator families parametrised by relation type.

### 16. van Gennep and Turner, rites of passage and liminality
- **Citation:** Arnold van Gennep, *Les rites de passage* (1909), English *The Rites of Passage*, Routledge 2013 reissue doi:10.4324/9781315017594 (also Univ. Chicago Press, trans. M. B. Vizedom and G. L. Caffee, 1960; Crossref dates the record 1961, doi:10.7208/chicago/9780226027180.001.0001; DOIs here are of reissues/reprints, not of the 1909 book). Victor Turner, *The Ritual Process: Structure and Anti-Structure*, 1969, Routledge reissue doi:10.4324/9781315134666 (DOI of reprint, not of the 1969 book).
- **Vocabulary:** separation, liminal (transition), incorporation (reaggregation); communitas; liminal persons ("threshold people").
- **Operands:** a person (or cohort) in a status within a group.
- **Operators (this is the key finding for the strand):** a rite of passage is a **status-changing operator composed of three phases**: separation (detach from the old status), liminality (hold in an ambiguous state), incorporation (attach to the new status). Van Gennep's own terms: rites of separation (*séparation*), transition (*marge*, "margin"; *liminaire*) and incorporation (*agrégation*); Turner's *liminal* and *communitas* elaborate the middle phase. Confirmed from standard knowledge; the first draft's source was https://en.wikipedia.org/wiki/Rite_of_passage. Note that the same page points to Pamela Cushing's finding that Outward Bound-type rites fail partly for want of the third stage. Informal, but it is an operator with a typed input (status A, group G) and output (status B, group G'), a distinct intermediate state, and a failure mode (missing incorporation).
- **Claim:** descriptive. Aronson-Mills dissonance work and contrary studies on initiation severity are mentioned on the same page as mixed evidence.
- **Limits:** no calculus; no account of who may authorise the rite; the phase model is a template, not a measurable.
- **Relevance:** very high. This is the best-developed non-kinship operator on membership. It tells the algebra that status change needs a typed intermediate state, an authorising party, and a witness group.

### 17. Douglas, grid-group
- **Citation:** Mary Douglas, *Natural Symbols* (1970), ch. "Grid and group", Routledge reprint doi:10.4324/9780203036051-8 (DOI of reprint chapter, not of the 1970 book).
- **Vocabulary:** group, grid.
- **Operands:** a social environment (or a person's position in it) given as a point in a plane.
- **Operators:** none; it is a classification, not an operator system. Group = strength of collective control; grid = stratification of roles and authority. Source: https://en.wikipedia.org/wiki/Cultural_theory_of_risk.
- **Claim:** worldviews map to quadrants. Wikipedia reports survey tests (Dake) with modest explained variance, plus charges of circularity and opaque definitions (Boholm, van der Linden).
- **Relevance:** gives two coordinates for a group's type that an algebra could use as parameters. Weak as dynamics.

### 18. Barth, Bailey, Boissevain (transactional anthropology)
- **Citation:** Fredrik Barth, *Models of Social Organization*, Royal Anthropological Institute Occasional Paper 23, 1966 (year as given in the brief; a review exists in *Man* 1967, doi:10.2307/2799520; DOI of review, not of the paper). F. G. Bailey, *Stratagems and Spoils: A Social Anthropology of Politics*, Blackwell 1969 (Routledge reissue doi:10.4324/9780429497094; DOI of reprint, not of the 1969 book). Jeremy Boissevain, *Friends of Friends: Networks, Manipulators and Coalitions*, Blackwell 1974 (review *Man* 1977 doi:10.2307/2800815; *AJS* 1978 doi:10.1086/226721; DOIs of reviews, not of the book).
- **Vocabulary:** transaction, entrepreneur, manipulator, broker, coalition (Boissevain), "stratagems and spoils".
- **Operands:** actors as strategic agents with resources, and networks of first-order (direct) and second-order (via others) contacts.
- **Operators:** transact (exchange value), manipulate, broker (bring two others into contact), form a coalition. All informal. Search-sourced summaries only (anthrobase, Boissevain interview); the Barth/Bailey contrast as drafted ("Bailey's actors are moral and rule-bound rather than free maximisers") overstates it: Bailey distinguishes normative rules (publicly professed) from pragmatic rules (how to win), and his actors manipulate pragmatic rules within the bounds of normative ones. Barth's actors are maximisers under constraints and incentives.
- **Claim:** a methodological turn from structural-functionalism toward agency. No predictive claim.
- **Limits:** case-based; no notation shared across studies.
- **Relevance:** supplies the operator "broker" (create a tie between two others), not in the pure game theory above, and the first-order/second-order zone distinction.

---

## D. Linguistics and pragmatics

### 19. Brown and Levinson, politeness theory
- **Citation:** P. Brown and S. C. Levinson, *Politeness: Some Universals in Language Usage*, Cambridge UP, 1987. doi:10.1017/cbo9780511813085.
- **Vocabulary:** positive face, negative face, face-threatening act (FTA), redress, on/off record.
- **Operands:** speaker S, hearer H, an act x.
- **Operators:** perform a speech act, with one of five strategies: bald on-record, positive politeness, negative politeness, off-record, or do not perform the FTA. Weightiness of an FTA: **W_x = D(S,H) + P(H,S) + R_x**, where D is social distance, P is the power H has over S, R_x is the culture-specific rank of imposition of x. The three factors are treated as independent and additive. Definitions confirmed only at secondary level (Wikipedia https://en.wikipedia.org/wiki/Politeness_theory, which prints the sum without symbols; search summaries including Hoebe 2001, who tested it on radio plays and found it predicts strategy choice, more so in longer scenes). The formula as given matches the book (1987, p. 76: W_x = D(S,H) + P(H,S) + R_x, with P(H,S) the power of hearer over speaker), confirmed from standard knowledge in the validation pass; Hoebe (2001) not independently located. [from abstract/standard account]
- **Predictive claim:** higher W leads to a higher-numbered (more indirect) strategy. Reported test (Hoebe 2001) supportive; cross-cultural critics (notably Japanese) call the model Western-biased and over-reliant on fixed hierarchies.
- **Limits:** additivity and independence are assumptions; R is cultural and not measurable independently; face as universal want is contested.
- **Relevance:** the one place where an interaction operator has an explicit cost law: how heavy a move is as a function of the relation (D, P) and the act (R). Exactly the shape needed for modelling interactions: move cost = f(relation, move type).

### 20. Giles, communication accommodation theory
- **Citation:** H. Giles, N. Coupland, J. Coupland, "Accommodation theory: Communication, context, and consequence", in *Contexts of Accommodation*, Cambridge UP, 1991, doi:10.1017/cbo9780511663673.001.
- **Vocabulary:** convergence, divergence, maintenance.
- **Operands:** speaker and interlocutor with a perceived group membership.
- **Operators:** converge (shift speech toward the other), diverge (away), maintain. Informal; shift is measurable on speech features. Not read in detail this session.
- **Relevance:** gives a simple three-valued operator on any pair whose argument is a distance, with convergence reading as solidarity and divergence as differentiation. Candidate for a "similarity-adjusting" operator.

### 21. Eckert and the three waves of variation study
- **Citation:** P. Eckert, "Three waves of variation study: the emergence of meaning in the study of sociolinguistic variation", *Annu. Rev. Anthropol.* 41 (2012), 87-100, doi:10.1146/annurev-anthro-092611-145828.
- **Vocabulary:** indexical field, social meaning, style, persona.
- **Operands:** linguistic variants, social categories and stances.
- **Operators:** use a variant to index a category/stance (third wave); a variant carries a field of potential meanings that speakers recombine. Informal. Only the bibliographic record was verified; content not read.
- **Relevance:** group membership is signalled and constructed through small marked choices; the operator is "index", and its output is a belief in the audience about the speaker's group. Ties to Akerlof-Kranton categories.

---

## E. Statistics of network dynamics

### 22. Exponential random graph models (ERGMs)
- **Citation:** G. Robins, P. Pattison, Y. Kalish, D. Lusher, "An introduction to exponential random graph (p*) models for social networks", *Social Networks* 29 (2007), doi:10.1016/j.socnet.2006.08.002. T. A. B. Snijders, P. Pattison, G. Robins, M. Handcock, "New specifications for exponential random graph models", *Sociol. Methodol.* 36 (2006), doi:10.1111/j.1467-9531.2006.00176.x.
- **Vocabulary:** network statistics (edges, reciprocity, triangles, k-stars), Markov dependence, social circuit dependence.
- **Operands:** a single observed network (graph on actors) plus covariates.
- **Operators:** none in time. The model gives P(Y=y) = exp(theta . s(y)) / kappa(theta), i.e. proportional to exp(sum of theta_k s_k(y)), with kappa a normalising constant summed over all graphs on n nodes (intractable, hence MCMC-MLE), so the "operations" are the counts s_k of local configurations. Formal. Cross-sectional only; the temporal extension is below. [from abstract/standard account]
- **Predictive claim:** statistical fit of an observed network; goodness-of-fit simulation. Prediction of future graphs is not the aim of the cross-sectional version.
- **Limits:** degeneracy with naive Markov terms (probability mass piles onto near-empty or near-complete graphs; Handcock 2003; the 2006 paper's geometrically weighted / alternating statistics are the fix); no process.
- **Relevance:** a catalogue of structural motifs (what local patterns matter) that the algebra's operators should be able to generate.

### 23. Snijders' stochastic actor-oriented models (SAOMs)
- **Citation:** T. A. B. Snijders, "Stochastic actor-oriented models for network change", *J. Math. Sociology* 21 (1996), doi:10.1080/0022250x.1996.9990178. Also the Annual Review/overview PDFs at https://www.stats.ox.ac.uk/~snijders/SAOM_ARStat1.pdf and https://www.stats.ox.ac.uk/%7Esnijders/SnijdersMathSciHum2004.pdf (retrieved through search, not read in full).
- **Vocabulary:** rate function, objective function, ministep, network-behaviour co-evolution.
- **Operands:** a digraph evolving in continuous time, observed at discrete waves; actors with covariates and behaviour variables.
- **Operators (verified in abstract-level summaries):** actors get opportunities to change at rates lambda_i = rho_m * exp(sum alpha_k r_ik(y)); given an opportunity the actor changes **one** outgoing tie, or none (or one behaviour value by one step), choosing among the reachable states x' with multinomial logit probability exp(f_i(x')) / sum over x'' of exp(f_i(x'')), where f_i(beta, x) = sum beta_k s_ik(x) is the objective (evaluation) function; this is maximisation of f plus a Gumbel random term. Later versions split f into evaluation, creation and endowment (maintenance) functions. The structure (rate function, objective function, ministep, logit choice) is confirmed from standard knowledge and Snijders's overview papers. Estimated by method of moments via stochastic approximation (RSiena); maximum-likelihood and Bayesian estimators also exist. Fully formal: a continuous-time Markov chain with a two-stage move (when, then what). [from abstract/standard account]
- **Predictive claim:** reproduces observed network change and supports tests of structural effects (reciprocity, transitivity). The sources retrieved do not give out-of-sample prediction accuracy; I make no claim.
- **Limits:** one tie per ministep; actors myopic; the rate function treats actors independently; requires panel data.
- **Relevance:** the closest existing thing to "operators and operands, then simulate": operand is the graph state, operator is the single-tie ministep, and the objective function is the rule choosing among operators. Highest relevance on the formal side.

### 24. Butts, relational event models (REMs)
- **Citation:** C. T. Butts, "A relational event framework for social action", *Sociol. Methodol.* 38 (2008), doi:10.1111/j.1467-9531.2008.00203.x. R package `relevent`, doi:10.32614/cran.package.relevent.
- **Vocabulary:** relational event (sender, receiver, type, time), event hazard, sufficient statistics.
- **Operands:** actors; a timed, ordered sequence of directed events.
- **Operators:** the event itself (sender acts on receiver). The tie-oriented model gives the hazard of each possible dyadic event given history. Statistics in use: inertia (past events i to j), reciprocity (past j to i), degree-based effects, per search-retrieved vignettes. Fully formal (event history likelihood). Hazard form (confirmed from standard knowledge of Butts 2008): the rate of event a at time t given history A_t is lambda(a, A_t; theta) = exp(theta . u(a, A_t)), log-linear in statistics u of the history; with ordinal (order-only) data the likelihood becomes a multinomial-logit over the next event, and with exact times it is a piecewise-constant hazard (exponential waiting times). [from abstract/standard account]
- **Predictive claim:** predicts the next event's distribution given the history. Software and example outputs retrieved, no out-of-sample accuracy benchmark gathered.
- **Limits:** events only, with no persistent states beyond history summaries; no explicit status or roles.
- **Relevance:** the nearest model of an interaction stream. Take the event as the unit operator, with history-dependent propensities.

### 25. Stadtfeld et al., dynamic network actor models
- **Citation:** C. Stadtfeld, J. Hollway, P. Block, "Dynamic network actor models: investigating coordination ties through time", *Sociol. Methodol.* 47 (2017), doi:10.1177/0081175017709295; C. Stadtfeld and P. Block, "Interactions, actors, and time: dynamic network actor models for relational events", *Sociological Science* 4 (2017), 318-352, doi:10.15195/v4.a14 (corrected: Hollway is not an author of the second paper).
- **Why:** an actor-oriented variant of REM (two-step: sender chooses then receiver) that sits between SAOM and REM. Bibliographic records only.
- **Relevance:** shows the tie-oriented versus actor-oriented design choice is real.

---

## F. Additions beyond the brief

### 26. Crawford and Ostrom, "A grammar of institutions" (1995)
- **Citation:** *APSR* 89(3), 582-600, doi:10.2307/2082975. Reissued in *Understanding Institutional Diversity* (2005) with Ostrom's other work. See also E. Ostrom, *Governing the Commons*, Cambridge UP, 1990, doi:10.1017/cbo9780511807763.
- See 04 §1 for the ADICO syntax, statement types and the Siddiki et al. extension. Unique to this angle: it is the one item in the political-science and economics cluster that is a literal grammar for rules (who must do what, under what condition and sanction), hence a candidate source for the operator schema.

### 27. Gouldner, "The norm of reciprocity" (1960)
- **Citation:** Alvin W. Gouldner, "The norm of reciprocity: a preliminary statement", *ASR* 25(2), 161-178 (April 1960), doi:10.2307/2092623 (Crossref record re-checked in validation).
- **Why:** reciprocity as a norm that creates obligation, bridging Mauss and the game theorists. Not read; no claims made.

---

## Unconfirmed and resolved items

Resolved in the validation pass (2026-10-29):

- **Banzhaf (1965)** — confirmed: *Rutgers Law Review* 19(2), 317-343; now cited in item 4. The RAND 1966 report (doi:10.7249/p3318, "Weighted voting: a mathematical analysis for instrumental judgments", no author in Crossref) is a different item.
- **Searle, *The Construction of Social Reality*** — confirmed from standard knowledge: John R. Searle, Free Press, New York, 1995. Constitutive rules of the form "X counts as Y in context C"; status functions created by collective intentionality and declarations. Content not re-read; its relevance (status-changing operators with authority) stands.
- **Hirschman, *Exit, Voice, and Loyalty*** — confirmed: Albert O. Hirschman, *Exit, Voice, and Loyalty: Responses to Decline in Firms, Organizations, and States*, Harvard UP, 1970. The operator triple (exit, voice, with loyalty as the parameter that delays exit) is the book's own framing.
- **Gouldner (1960)** — confirmed (item 27).
- **Brown-Levinson formula** — confirmed: W_x = D(S,H) + P(H,S) + R_x, 1987, p. 76. P(H,S) is the book's notation (hearer's power over speaker); sources writing P(S,H) are wrong.
- **Bueno de Mesquita "90 percent"** — traced to Feder 1987 and read; see item 3.

Still unconfirmed:

- **Goffman, *Interaction Ritual*** (1967; Routledge reissue doi:10.4324/9780203788387; DOI of reprint, not of the 1967 book); face-work content not read. Belongs to the sociology/social-psychology agents.
- **Hoebe (2001)** test of Brown-Levinson on radio plays: not located; treat as search-hearsay.
- **Mitchell and Nyblade (2006)** "two-fifths oversized": only a second-hand citation found.
- **Pamela Cushing on Outward Bound rites** (item 16): from Wikipedia only.
- **Independent accuracy audit of Bueno de Mesquita's model**: none found. (Tetlock-style tournaments evaluate forecasters, not this model.)

## Clearly missing important work (added in validation)

Bibliographic facts from standard knowledge; content not surveyed here.

- **Political science / coalitions:** W. A. Gamson, "A theory of coalition formation", *ASR* 26 (1961) (proportional payoffs); A. de Swaan, *Coalition Theories and Cabinet Formations* (1973); M. Laver and K. A. Shepsle, *Making and Breaking Governments* (1996) (portfolio allocation); D. P. Baron and J. A. Ferejohn, "Bargaining in legislatures", *APSR* 83 (1989) (sequential proposer model, the dynamic counterpart of Riker); Penrose (1946) and Coleman (1971) for voting power.
- **Economics / games:** R. Axelrod, *The Evolution of Cooperation* (1984); J. F. Nash, "The bargaining problem", *Econometrica* 18 (1950); M. Hechter, *Principles of Group Solidarity* (1987); A. Greif, *Institutions and the Path to the Modern Economy* (2006); J. S. Coleman, *Foundations of Social Theory* (1990) (rights and authority transfers as formal operations, directly on target for "who may act on whom").
- **Anthropology:** M. Gluckman on ritual and conflict; E. R. Leach, *Political Systems of Highland Burma* (1954) (oscillation between group types, a dynamics the grid-group entry lacks); P. M. Blau, *Exchange and Power in Social Life* (1964) and R. M. Emerson, "Power-dependence relations", *ASR* 27 (1962) (exchange-theory power, arguably sociology but the formal bridge from Mauss to networks).
- **Linguistics:** W. Labov, *The Social Stratification of English in New York City* (1966) (first wave); L. Milroy, *Language and Social Networks* (1980) (network density and multiplexity predict vernacular maintenance, the link between section D and section E); R. Brown and A. Gilman, "The pronouns of power and solidarity" (1960) (the two-axis P/D precursor of Brown-Levinson).
- **Network statistics:** P. W. Holland and S. Leinhardt, "An exponential family of probability distributions for directed graphs", *JASA* 76 (1981) (p1, the ERGM ancestor); O. Frank and D. Strauss, "Markov graphs", *JASA* 81 (1986).
- **Forecasting:** B. Bueno de Mesquita, *The Predictioneer's Game* (2009), the popular source of the 90 percent claim; S. A. Feder, "Forecasting for policy making in the post-Cold War period", *Annual Review of Political Science* 5 (2002).

## What this cluster already covers

- **A catalogue of operators on membership and structure, with formal versions:** form/dissolve a coalition (Riker, game theory), add/sever a link (Jackson-Wolinsky), change one tie at a time (SAOM), emit a directed event (REM), veto (Tsebelis), allocate payoffs to a winning set (selectorate).
- **A catalogue of informal operators on status and obligation:** give/receive/return (Mauss), vary reciprocity by distance (Sahlins), separate/hold/incorporate (van Gennep, Turner), transact/broker/manipulate (Barth, Bailey, Boissevain), converge/diverge (Giles), threaten/redress face (Brown-Levinson), index group membership by a variant (Eckert).
- **Typed operands:** person, category, prescription (Akerlof-Kranton); actor with position, salience, clout (BdM); player with weight (power indices); actor with attribute set (ADICO).
- **A cost law for moves:** Brown-Levinson's W; Jackson-Wolinsky's link cost and distance decay.
- **Rules about stability:** the core, pairwise stability, Nash-style equilibria in the models above; unanimity of veto players.
- **Estimation machinery:** ERGM, SAOM and REM show that operator-and-state models can be fitted to real data.

## What it does not cover

- **No single algebra.** Nothing here composes the operators from different families (a rite of passage, a gift, a coalition, a face threat) into a single notation with composition laws. They live in separate formalisms with incompatible operand types.
- **Roles and statuses as first-class operands are scarce.** Only Akerlof-Kranton and ADICO treat category/role explicitly, and neither says how a role changes except through the actor's own choice. The anthropological rites do describe change, but not formally.
- **Operators that change the operators (rules about rules).** Akerlof-Kranton allow actions to change prescriptions P, and ADICO has nested statements, but no theory of the rule-change operator exists in this cluster.
- **Multi-level structure** (person to dyad to group to group-of-groups) is handled by Aumann-Drèze coalition structures and Barth/Boissevain zones, but without a calculus.
- **Authority and legitimacy of an operator** (who can perform a rite, who can declare a status) is absent from the surveyed entries; Searle (1995, now confirmed, not surveyed) and Coleman (1990) are where it lives.
- **Forecasting claims are weak outside statistics.** The one famous "90 percent" forecasting result (BdM) is real but narrow: an in-house CIA figure (Feder 1987) that Policon tied with conventional analysis on accuracy and beat it only on specificity, with no stated scoring method and no independent audit. The statistical models (SAOM, REM) fit and describe; the sources retrieved give no out-of-sample benchmark.
- **The strongest formal results (core, Shapley, veto) are about static stability; the strongest dynamic models (SAOM, REM) have almost no semantic content about what the ties or events mean.** The algebra's opening is to supply typed, meaningful operators to the dynamics machinery, and typed operands to the stability theory.

## Validation log (2026-10-29)

Independent pass: citations checked against Crossref and web search, the BdM claim against the primary Feder text, formal claims against standard knowledge of the literature.

1. Riker 1962 — ✎ corrected: size principle quoted in Riker's wording and the information effect added (the draft implied minimal coalitions follow unconditionally); Laakso 1972 venue added and confirmed; Mitchell-Nyblade marked second-hand.
2. Olson 1965 — ✓ (critique sharpened to jointness of supply; argument stated).
3. Bueno de Mesquita et al. 2003 / forecasting — ✎ corrected: *Forecasting Political Events* is by Bueno de Mesquita, **Newman and Rabushka**, not "Lalman et al."; EC Decision Making editors added; "full specification not released" corrected to "core published, operational version not"; selectorate W vs W/S roles separated; **90 percent claim traced to Feder 1987 and read**: about 90 percent for Policon *and equally for traditional CIA analysis*, in-house, 1982-85, no stated method, BdM not named.
4. Shapley-Shubik 1954 / Shapley 1953 — ✓; Banzhaf 1965 — ✎ moved from Unconfirmed to confirmed, definition added, Penrose/Coleman precedence noted.
5. Axelrod 1970 / 1967 — ✎ corrected: unsupported "ten cases" replaced; Chua-Felsenthal citation completed (2008, *Power, Freedom, and Voting*).
6. Tsebelis 1995 / 2002 — ✎ corrected: policy stability is *inversely* related to winset size (draft said equal to it).
7. Gillies 1959; Aumann-Drèze 1974 — ✓.
8. Myerson 1977 — ✓.
9. Jackson-Wolinsky 1996; Jackson 2008; Bala-Goyal 2000 — ✓; pairwise stability ✓; connections model confirmed; efficiency/stability result stated precisely (anonymous, component-balanced allocation rules).
10. Akerlof-Kranton 2000 — ✓.
11. Schelling 1958 / 1960 / 1971 — ✓.
12. Bowles-Gintis 2011 — ✓ (bibliographic).
13. Rubinstein 1982; Spence 1973 — ✓ (bibliographic).
14. Mauss — ✓; three obligations confirmed as Mauss's own.
15. Sahlins 1965/1972 — ✎ corrected: distance correlation is Sahlins's own sectoral model, not a secondary gloss; 1965 Banton volume added.
16. van Gennep 1909 / Turner 1969 — ✎ corrected: Chicago translation 1960 (Crossref says 1961); French phase terms added; three phases ✓. Cushing claim ? (Wikipedia only).
17. Douglas 1970 — ✓.
18. Barth 1966; Bailey 1969; Boissevain 1974 — ✎ corrected: Bailey characterisation (normative vs pragmatic rules), draft overstated.
19. Brown-Levinson 1987 — ✓ formula W_x = D(S,H) + P(H,S) + R_x confirmed (p. 76); Hoebe 2001 ?.
20. Giles, Coupland and Coupland 1991 — ✓.
21. Eckert 2012 — ✓.
22. Robins et al. 2007; Snijders et al. 2006 — ✓; ERGM form given with normalising constant; degeneracy described.
23. Snijders 1996 SAOM — ✓; ✎ choice rule made explicit as multinomial logit; other estimators noted.
24. Butts 2008 REM — ✓; ✎ hazard form added (log-linear in history statistics).
25. Stadtfeld et al. 2017 — ✎ corrected: the *Sociological Science* paper is Stadtfeld and Block only.
26. Crawford-Ostrom 1995 — ✎ corrected: norm = ADIC (draft garbled as "AICO"); shared strategy = AIC.
27. Gouldner 1960 — ✓ (pages and subtitle added).
Unconfirmed list — Banzhaf, Searle (Free Press 1995), Hirschman (Harvard 1970), Gouldner, B-L formula all resolved ✓; Goffman, Hoebe, Mitchell-Nyblade, Cushing remain ?.
✗ removed: none; no fabricated works found.

**Verdict.** The survey is bibliographically sound: every cited work exists, and the errors are misattributions (Lalman for Newman and Rabushka; Hollway on the wrong paper) and a few formal slips (Tsebelis stability inverted, ADICO norm form garbled, W vs W/S conflated) rather than invention. Its caution about secondary sourcing was justified but in places over-cautious (Mauss, Sahlins, van Gennep, Brown-Levinson are all correct as stated). The most consequential change is to the BdM 90 percent claim, which is real but means "tied with CIA analysts, more specific", not "outperformed them", and comes from an unaudited in-house source.

