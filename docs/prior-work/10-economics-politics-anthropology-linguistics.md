# Prior work: economics, political science, non-kinship anthropology, linguistics, network statistics

Date: 2026-10-29. Survey for the `social-algebra` strand. Aim (Aldred): identify the mechanics of a social group as operators and operands, to model interactions later.

## Summary

This cluster does not contain one algebra of groups, but it contains most of the pieces, and in very different degrees of formality.

- **Formal, fully specified, predictive:** cooperative game theory and power indices (operand: set of players, characteristic function; operator: coalition formation, marginal contribution); Jackson-Wolinsky network formation (operand: graph; operators: add link, sever link); SAOMs, ERGMs and relational event models (operand: network state; operators: one tie change, one dyadic event, each with an explicit rate/probability law). These are the nearest thing to a calculus of "what can happen next".
- **Formal but with only one kind of operand:** veto-player theory, selectorate theory, Axelrod's conflict of interest. Operands are actors with positions or loyalties; the "operator" is a decision rule, not a set of moves.
- **Informal but the right operator vocabulary:** Mauss, Sahlins, van Gennep/Turner, Barth, Bailey, Boissevain, Goffman-style face work. These name the moves (give, receive, reciprocate; separate, liminal, incorporate; transact, manage, broker) and none gives a closed notation.
- **One half-formal grammar worth copying:** Crawford and Ostrom's ADICO syntax is the only item here that is literally a grammar for statements about what actors may/must do. Brown-Levinson's weightiness formula is the only one that gives an additive "cost of a move" law.
- **Verification note.** Bibliographic records were verified through the Crossref API (DOIs below). Content claims were verified from fetched primary text only for Akerlof-Kranton (full equations, from the paper PDF); everything else rests on secondary pages, search abstracts, or reviews and is labelled. Items not confirmed at all are listed under "Unconfirmed". The much-quoted CIA "90 percent" figure for Bueno de Mesquita could not be traced to a primary document (see item 3).

Entry count: 27 numbered entries (A politics 1-6, B economics and game theory 7-13, C anthropology 14-18, D linguistics 19-21, E network statistics 22-25, F additions 26-27), plus an Unconfirmed list.

---

## A. Political science

### 1. Riker, *The Theory of Political Coalitions* (1962)
- **Citation:** William H. Riker, *The Theory of Political Coalitions*, Yale University Press, 1962.
- **Verification:** Existence confirmed via reviews in Crossref: Midwest J. Political Science 1963, doi:10.2307/2109034; Western Political Quarterly 1963, doi:10.2307/445870. Wikipedia page https://en.wikipedia.org/wiki/The_Theory_of_Political_Coalitions exists (not read in detail).
- **Their vocabulary:** winning coalition, minimal winning coalition, size principle, zero-sum n-person game, side payments.
- **Operands (translated):** a set of players with weights (votes) and a winning rule; a coalition is a subset.
- **Operators (translated):** "join/form a coalition"; the output is the subset that forms. Formal: von Neumann-Morgenstern n-person zero-sum game with side payments; size principle is a theorem within that setting: with full information, zero-sum payoffs, and rational players, only minimal winning coalitions form. A derivation, not a notation.
- **Predictive/control claim:** coalitions will be minimal winning. Held up partly. Search-retrieved abstracts: Butterworth (1971, APSR) argued the derivation unsound in general; Shepsle (1974) replied that under a reasonable solution concept it holds; Laakso (1972) found support in Finnish roll calls; a review cites Mitchell and Nyblade (2006) finding roughly two-fifths of majority coalitions were oversized. Net: a baseline, frequently violated once policy matters (see 5).
- **Limits:** zero-sum and full-information assumptions; no policy content; no dynamics; no roles beyond "member".
- **Relevance:** the first clean case of "operand = subset of a weighted set, operator = form/dissolve". Shows what assumptions buy a theorem.

### 2. Olson, *The Logic of Collective Action* (1965)
- **Citation:** Mancur Olson, *The Logic of Collective Action: Public Goods and the Theory of Groups*, Harvard University Press, 1965.
- **Verification:** Crossref has reviews/derivatives (e.g. Land Economics review essay 1967, doi:10.2307/3145551; Hindmoor, *Rational Choice*, doi:10.1007/978-0-230-20997-8_5). The book itself was not located in Crossref this session; the content below is from search-result summaries.
- **Their vocabulary:** collective good, free rider, selective incentive, latent group, privileged/intermediate/latent group by size.
- **Operands:** individuals as contributors to a shared good; group size as a parameter.
- **Operators:** contribute / free-ride; selective incentive (reward or punishment applied to individuals) as the operator that changes the contribute/free-ride payoff. Informal verbal theory with a simple cost-benefit logic.
- **Predictive claim:** large groups under-provide collective goods without selective incentives. Search results report later critique: the size effect can reverse when the prize is public and indivisible, and size is often empirically an asset (union influence).
- **Limits:** one-shot, atomistic, no structure inside the group; ignores reciprocity and network structure.
- **Relevance:** supplies the canonical "defect/cooperate under group size" operator pair and the idea that a second-order operator (incentive) acts on the first.

### 3. Bueno de Mesquita, Smith, Siverson and Morrow, *The Logic of Political Survival* (2003), and BdM's forecasting model
- **Citation:** B. Bueno de Mesquita, A. Smith, R. M. Siverson, J. D. Morrow, *The Logic of Political Survival*, MIT Press, 2003. doi:10.7551/mitpress/4292.001.0001. Forecasting: B. Bueno de Mesquita, "A decision making model: its structure and form", *International Interactions* 23 (1997), doi:10.1080/03050629708434909; *European Community Decision Making* (Yale UP, 1994), ch. 4 "Political Forecasting: An Expected Utility Method", doi:10.12987/9780300158113-007; Bueno de Mesquita and Lalman et al., *Forecasting Political Events: The Future of Hong Kong* (Yale, 1985; reviews doi:10.2307/2131621, 10.2307/1960943, 10.2307/2758844).
- **Their vocabulary:** nominal selectorate, real selectorate S, winning coalition W, loyalty norm W/S, revenue R, private vs public goods; for the forecasting model: actors with position, salience, clout (influence), resolve; "median voter" positions; bargaining rounds.
- **Operands:** leader; selectorate S; subset W of S whose support is needed. In the forecasting model: a list of stakeholders, each with a numeric position on an issue, a salience and a clout.
- **Operators:** leader allocates revenue R between public goods and private payoffs to W; supporters defect or stay; challenger offers a better deal. In the forecasting model, iterated pairwise expected-utility comparisons (each actor evaluates challenging each other actor) that shift positions round by round. Selectorate theory is a formal game model with comparative statics. The forecasting model is a computable algorithm, but its full specification has not been released.
- **Predictive/control claim:** Selectorate: small W/S regimes have high survival and give private goods; large W/S give public goods and shorter leader tenure (Wikipedia summary, https://en.wikipedia.org/wiki/Selectorate_theory; Weeks criticises its assumptions about autocracies). Forecasting: widely repeated claim that a declassified CIA assessment rated the model about 90 percent accurate. **Provenance is weak.** The Wikipedia entry for BdM (https://en.wikipedia.org/wiki/Bruce_Bueno_de_Mesquita) footnotes it to BdM's own *Foreign Policy* piece "Recipe for Failure", not the CIA document. Search results trace it to Stanley Feder, "Factions and Policon: New Ways to Analyze Politics", reprinted in H. B. Westerfield (ed.), *Inside CIA's Private World* (Yale UP, 1995); one forum comment says the first page states 90 percent for Policon and also 90 percent for standard CIA methods but with more specific predictions. That reading is second-hand and was not checked against the article. A critic (Walt) is quoted saying most forecasts are proprietary and cannot be verified. Scholz, Calbert and Smith (2011, SciTePress, https://www.scitepress.org/Papers/2011/31215) report that no clear specification is in the open literature, reconstruct it from published sources, and discuss sensitivity and convergence concerns.
- **Limits:** forecasting model is not independently auditable; selectorate theory is regime-level, not interaction-level; positions and salience are scalar inputs that someone must estimate.
- **Relevance:** the most explicit attempt at "list the actors, give each numbers, simulate what each does to each". Useful as a template for an operand record (position, salience, clout, resolve) and a warning that without open specification the track record is unverifiable.

### 4. Shapley-Shubik and Banzhaf power indices
- **Citation:** L. S. Shapley and M. Shubik, "A method for evaluating the distribution of power in a committee system", *APSR* 48 (1954), doi:10.2307/1951053. Shapley, "A value for n-person games", in *Contributions to the Theory of Games II* (1953), doi:10.1515/9781400881970-018. Banzhaf (1965): see Unconfirmed.
- **Their vocabulary:** characteristic function, pivotal player, Shapley value, swing, power index.
- **Operands:** a voting game: players, weights, quota; a coalition is a subset.
- **Operators:** adding a player to a coalition (marginal contribution). Shapley-Shubik power of i = share of orderings of the players in which i is pivotal (turns a losing coalition into a winning one). Fully formal; closed-form definitions. Verified from the existence of the cited records; the pivot definition is standard but was not re-read from the paper this session.
- **Predictive claim:** measures a priori voting power, not behaviour. Known to differ from nominal weight (no claim verified here).
- **Limits:** treats all orderings or all coalitions as equally likely; ignores preferences, so power is context-free.
- **Relevance:** gives a ready-made operator, "marginal contribution of an operand to a coalition", and shows that "weight" and "influence" are different quantities. Directly reusable as one candidate measure.

### 5. Axelrod, *Conflict of Interest* (1970)
- **Citation:** Robert Axelrod, *Conflict of Interest: A Theory of Divergent Goals with Applications to Politics*, Markham, Chicago, 1970. Reviews: doi:10.2307/1958375 (APSR), doi:10.2307/2110125 (Midwest J. Pol. Sci.). Earlier: "Conflict of interest: an axiomatic approach", *J. Conflict Resolution* 11 (1967), doi:10.1177/002200276701100107.
- **Their vocabulary:** conflict of interest, minimal connected winning coalition, policy range.
- **Operands:** actors with positions on a line (e.g. left-right) and a payoff structure over outcomes; conflict of interest is defined as incompatibility of goals.
- **Operators:** coalition choice minimising the spread of positions among members. Formal measurement of conflict (axioms in the 1967 paper); coalition rule is a hypothesis.
- **Predictive claim:** (from review abstracts) the minimal connected winning (MCW) theory fits the ten cases analysed; later work questioned the interval-scale assumption and the coding of abstentions. Closely tied to Leiserson's closed minimal range theory, which a comparative study (Chua and Felsenthal, as reported by search) found outperformed Aumann's Shapley-Shubik hypothesis.
- **Limits:** a single policy dimension; coalitions as static outcomes.
- **Relevance:** introduces a distance metric between actors as the thing the coalition operator acts on. A candidate primitive: d(a, b) = conflict of interest.

### 6. Tsebelis, *Veto Players* (2002; 1995 article)
- **Citation:** George Tsebelis, "Decision making in political systems: veto players in presidentialism, parliamentarism, multicameralism and multipartyism", *BJPolS* 25 (1995), doi:10.1017/s0007123400007225; *Veto Players: How Political Institutions Work*, Princeton UP, 2002, doi:10.1515/9781400831456.
- **Their vocabulary:** veto player, status quo, winset, absorption rule, policy stability.
- **Operands:** veto players, each with an ideal point and a status quo point in policy space.
- **Operators:** a change from status quo to a new point passes only if every veto player weakly prefers it. Policy stability = size of the intersection of the veto players' win sets. Formal, spatial-geometric; the absorption rule (a player whose position lies within the others' win set adds no constraint) is a reduction rule on the operand list. The Wikipedia summary (https://en.wikipedia.org/wiki/Veto_player) states the unanimity condition but not the absorption rule; the rule itself comes from the book, not read here.
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
- **Operators:** add link ij (needs both consent), delete link ij (unilateral). Pairwise stability: no player gains by deleting an existing link and no pair both gain by adding a missing one. Fully formal. The connections model (payoff = discounted sum over others by shortest-path distance minus link costs) is from a secondary page and should be checked against the paper.
- **Claim:** abstract (retrieved via search): there does not always exist a stable network that is efficient; resolving this requires allocation rules that are hard to justify. Not an empirical claim.
- **Limits:** equilibrium thinking; no timing; payoffs exogenous.
- **Relevance:** the cleanest explicit operator set for relationships: add (bilateral), sever (unilateral). The asymmetry of consent is a structural fact worth putting in the algebra at the start.

### 10. Akerlof and Kranton, "Economics and Identity" (2000)
- **Citation:** *QJE* 115(3), 715-753. doi:10.1162/003355300554881. Full text read.
- **Their vocabulary:** identity, social category C, assignment c_j, prescriptions P, gains and losses in identity.
- **Operands (verified from the paper, Section III.A):** each person j has actions a_j; an assignment c_j of everyone (including j) to social categories C; characteristics epsilon_j; prescriptions P, the behaviour (and ideal attributes) appropriate to each category; categories carry social status.
- **Operators/structure (verified):** U_j = U_j(a_j, a_-j, I_j) and I_j = I_j(a_j, a_-j; c_j, epsilon_j, P). Identity utility rises when one's own and others' actions match the prescriptions for one's assigned category and when one's characteristics match the category ideal. Actions can also change c_j (switch category), P (alter prescriptions) or category status. The paper names worked cases: violating prescriptions draws scorn and ostracism; changing group; advertising and schools as deliberate manipulation of P. It is a utility model with a formal structure; there is no algebra of category change, but the mechanism is explicit.
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
- **Citation:** Marcel Mauss, *Essai sur le don* (1923-24); English edition in Routledge reissue, doi:10.4324/9781003572350 (2024). Review: *ASR* 1956, doi:10.2307/2088549.
- **Vocabulary:** gift, obligation to give, receive, reciprocate; total prestation.
- **Operands:** persons and groups as exchange partners; objects as carriers of obligation.
- **Operators:** give, receive, return. The three-obligation structure is the usual reading; this was not confirmed against the text this session. Informal. No formal notation.
- **Claim:** descriptive and comparative, not predictive.
- **Relevance:** gives a minimal operator triple with an obvious composition law: give followed by an obligation to return. The structure of "debt" as a state variable on an ordered pair.

### 15. Sahlins, spectrum of reciprocity
- **Citation:** Marshall Sahlins, "On the sociology of primitive exchange" (1965; in *Stone Age Economics*, Aldine, 1972), doi:10.4324/9781315184951-5.
- **Vocabulary:** generalized, balanced, negative reciprocity.
- **Operands:** pairs of actors with a kinship/residential distance.
- **Operators:** generalised = near-pure gift with no stated return; balanced = direct exchange of customary equivalents; negative = attempt at something for nothing with impunity. The kinship-distance correlation was reported by a secondary source; the definitions above come from Wikipedia (https://en.wikipedia.org/wiki/Reciprocity_(cultural_anthropology)) and search summaries, not Sahlins directly. Informal ordinal scale.
- **Claim:** reciprocity type correlates with social distance. Not rigorously tested in what was retrieved.
- **Relevance:** one scalar (distance) selects among a small set of operator variants. A useful design pattern: operator families parametrised by relation type.

### 16. van Gennep and Turner, rites of passage and liminality
- **Citation:** Arnold van Gennep, *Les rites de passage* (1909), English *The Rites of Passage*, Routledge 2013 reissue doi:10.4324/9781315017594 (also Univ. Chicago Press 1961 ed. doi:10.7208/chicago/9780226027180.001.0001). Victor Turner, *The Ritual Process: Structure and Anti-Structure*, 1969, Routledge reissue doi:10.4324/9781315134666.
- **Vocabulary:** separation, liminal (transition), incorporation (reaggregation); communitas; liminal persons ("threshold people").
- **Operands:** a person (or cohort) in a status within a group.
- **Operators (this is the key finding for the strand):** a rite of passage is a **status-changing operator composed of three phases**: separation (detach from the old status), liminality (hold in an ambiguous state), incorporation (attach to the new status). Source: https://en.wikipedia.org/wiki/Rite_of_passage. Note that the same page points to Pamela Cushing's finding that Outward Bound-type rites fail partly for want of the third stage. Informal, but it is an operator with a typed input (status A, group G) and output (status B, group G'), a distinct intermediate state, and a failure mode (missing incorporation).
- **Claim:** descriptive. Aronson-Mills dissonance work and contrary studies on initiation severity are mentioned on the same page as mixed evidence.
- **Limits:** no calculus; no account of who may authorise the rite; the phase model is a template, not a measurable.
- **Relevance:** very high. This is the best-developed non-kinship operator on membership. It tells the algebra that status change needs a typed intermediate state, an authorising party, and a witness group.

### 17. Douglas, grid-group
- **Citation:** Mary Douglas, *Natural Symbols* (1970), ch. "Grid and group", Routledge reprint doi:10.4324/9780203036051-8.
- **Vocabulary:** group, grid.
- **Operands:** a social environment (or a person's position in it) given as a point in a plane.
- **Operators:** none; it is a classification, not an operator system. Group = strength of collective control; grid = stratification of roles and authority. Source: https://en.wikipedia.org/wiki/Cultural_theory_of_risk.
- **Claim:** worldviews map to quadrants. Wikipedia reports survey tests (Dake) with modest explained variance, plus charges of circularity and opaque definitions (Boholm, van der Linden).
- **Relevance:** gives two coordinates for a group's type that an algebra could use as parameters. Weak as dynamics.

### 18. Barth, Bailey, Boissevain (transactional anthropology)
- **Citation:** Fredrik Barth, *Models of Social Organization*, Royal Anthropological Institute Occasional Paper 23, 1966 (year as given in the brief; a review exists in *Man* 1967, doi:10.2307/2799520). F. G. Bailey, *Stratagems and Spoils: A Social Anthropology of Politics*, Blackwell 1969 (Routledge reissue doi:10.4324/9780429497094). Jeremy Boissevain, *Friends of Friends: Networks, Manipulators and Coalitions*, Blackwell 1974 (review *Man* 1977 doi:10.2307/2800815; *AJS* 1978 doi:10.1086/226721).
- **Vocabulary:** transaction, entrepreneur, manipulator, broker, coalition (Boissevain), "stratagems and spoils".
- **Operands:** actors as strategic agents with resources, and networks of first-order (direct) and second-order (via others) contacts.
- **Operators:** transact (exchange value), manipulate, broker (bring two others into contact), form a coalition. All informal. Search-sourced summaries only (anthrobase, Boissevain interview); the Barth/Bailey contrast is that Bailey's actors are moral and rule-bound rather than free maximisers.
- **Claim:** a methodological turn from structural-functionalism toward agency. No predictive claim.
- **Limits:** case-based; no notation shared across studies.
- **Relevance:** supplies the operator "broker" (create a tie between two others), not in the pure game theory above, and the first-order/second-order zone distinction.

---

## D. Linguistics and pragmatics

### 19. Brown and Levinson, politeness theory
- **Citation:** P. Brown and S. C. Levinson, *Politeness: Some Universals in Language Usage*, Cambridge UP, 1987. doi:10.1017/cbo9780511813085.
- **Vocabulary:** positive face, negative face, face-threatening act (FTA), redress, on/off record.
- **Operands:** speaker S, hearer H, an act x.
- **Operators:** perform a speech act, with one of five strategies: bald on-record, positive politeness, negative politeness, off-record, or do not perform the FTA. Weightiness of an FTA: **W_x = D(S,H) + P(H,S) + R_x**, where D is social distance, P is the power H has over S, R_x is the culture-specific rank of imposition of x. The three factors are treated as independent and additive. Definitions confirmed only at secondary level (Wikipedia https://en.wikipedia.org/wiki/Politeness_theory, which prints the sum without symbols; search summaries including Hoebe 2001, who tested it on radio plays and found it predicts strategy choice, more so in longer scenes). I did not retrieve the book's own formula text.
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
- **Operators:** none in time. The model gives P(G) proportional to exp(sum of theta_k s_k(G)), so the "operations" are the counts s_k of local configurations. Formal. Cross-sectional only; the temporal extension is below.
- **Predictive claim:** statistical fit of an observed network; goodness-of-fit simulation. Prediction of future graphs is not the aim of the cross-sectional version.
- **Limits:** degeneracy with naive Markov terms (the 2006 paper's motivation); no process.
- **Relevance:** a catalogue of structural motifs (what local patterns matter) that the algebra's operators should be able to generate.

### 23. Snijders' stochastic actor-oriented models (SAOMs)
- **Citation:** T. A. B. Snijders, "Stochastic actor-oriented models for network change", *J. Math. Sociology* 21 (1996), doi:10.1080/0022250x.1996.9990178. Also the Annual Review/overview PDFs at https://www.stats.ox.ac.uk/~snijders/SAOM_ARStat1.pdf and https://www.stats.ox.ac.uk/%7Esnijders/SnijdersMathSciHum2004.pdf (retrieved through search, not read in full).
- **Vocabulary:** rate function, objective function, ministep, network-behaviour co-evolution.
- **Operands:** a digraph evolving in continuous time, observed at discrete waves; actors with covariates and behaviour variables.
- **Operators (verified in abstract-level summaries):** actors get opportunities to change at rates lambda_i = rho_m * exp(sum alpha_k r_ik(y)); given an opportunity the actor changes **one** outgoing tie (or one behaviour value) to maximise a random-utility objective f_i(beta, y', y) = sum beta_k s_ik(y', y). Estimated by method of moments via stochastic approximation (RSiena). Fully formal: a continuous-time Markov chain with a two-stage move (when, then what).
- **Predictive claim:** reproduces observed network change and supports tests of structural effects (reciprocity, transitivity). The sources retrieved do not give out-of-sample prediction accuracy; I make no claim.
- **Limits:** one tie per ministep; actors myopic; the rate function treats actors independently; requires panel data.
- **Relevance:** the closest existing thing to "operators and operands, then simulate": operand is the graph state, operator is the single-tie ministep, and the objective function is the rule choosing among operators. Highest relevance on the formal side.

### 24. Butts, relational event models (REMs)
- **Citation:** C. T. Butts, "A relational event framework for social action", *Sociol. Methodol.* 38 (2008), doi:10.1111/j.1467-9531.2008.00203.x. R package `relevent`, doi:10.32614/cran.package.relevent.
- **Vocabulary:** relational event (sender, receiver, type, time), event hazard, sufficient statistics.
- **Operands:** actors; a timed, ordered sequence of directed events.
- **Operators:** the event itself (sender acts on receiver). The tie-oriented model gives the hazard of each possible dyadic event given history. Statistics in use: inertia (past events i to j), reciprocity (past j to i), degree-based effects, per search-retrieved vignettes. Fully formal (event history likelihood). The exact hazard equations were not read.
- **Predictive claim:** predicts the next event's distribution given the history. Software and example outputs retrieved, no out-of-sample accuracy benchmark gathered.
- **Limits:** events only, with no persistent states beyond history summaries; no explicit status or roles.
- **Relevance:** the nearest model of an interaction stream. Take the event as the unit operator, with history-dependent propensities.

### 25. Stadtfeld et al., dynamic network actor models
- **Citation:** C. Stadtfeld, J. Hollway, P. Block, "Dynamic network actor models: investigating coordination ties through time", *Sociol. Methodol.* 47 (2017), doi:10.1177/0081175017709295; "Interactions, actors, and time: dynamic network actor models for relational events", *Sociological Science* 4 (2017), doi:10.15195/v4.a14.
- **Why:** an actor-oriented variant of REM (two-step: sender chooses then receiver) that sits between SAOM and REM. Bibliographic records only.
- **Relevance:** shows the tie-oriented versus actor-oriented design choice is real.

---

## F. Additions beyond the brief

### 26. Crawford and Ostrom, "A grammar of institutions" (1995)
- **Citation:** *APSR* 89(3), 582-600, doi:10.2307/2082975. Reissued in *Understanding Institutional Diversity* (2005) with Ostrom's other work. See also E. Ostrom, *Governing the Commons*, Cambridge UP, 1990, doi:10.1017/cbo9780511807763.
- **Vocabulary:** Attributes, Deontic, aIm, Conditions, Or else (ADICO).
- **Operands:** actors with attributes (role, status).
- **Operators (verified at summary level):** an institutional statement is a grammar sentence: Attribute-Deontic (must/may/must not)-aIm-Condition-Or else. Rule = ADICO (has sanction); norm = AIC plus deontic without sanction (AICO in the summary: norms drop the Or-else); shared strategy = AIC. Later work adds oBject (ABDICO) and nested monitoring statements. Source: sources listed in the search result (Siddiki et al. 2011 extension; Watkins and Westphal case study found norms prevalent and meaningful). The original article was not read. A real grammar, applied in empirical coding of policy texts; does not provide dynamics.
- **Claim:** descriptive coding scheme with empirical application in natural-resource governance; no forecasting.
- **Relevance:** high. This is a literal grammar for rules about who must do what to whom, when, under what sanction. A candidate source for the operator schema.

### 27. Gouldner, "The norm of reciprocity" (1960)
- **Citation:** *ASR* 25(2), doi:10.2307/2092623 (record verified in Crossref only).
- **Why:** reciprocity as a norm that creates obligation, bridging Mauss and the game theorists. Not read; no claims made.

---

## Unconfirmed (no source retrieved this session)

- **Banzhaf (1965),** "Weighted voting doesn't work: a mathematical analysis", *Rutgers Law Review*. Crossref query returned nothing matching; only a RAND 1966 report with a similar title (doi:10.7249/p3318, authorship not checked) and a 2021 paper. Banzhaf index defined from general knowledge only; not confirmed here.
- **Searle, *The Construction of Social Reality*** (status function declarations, "X counts as Y in C"). Crossref returned only commentary on Searle. Highly relevant to the strand (constitutive rules are operators that change social status), flagged for the next pass, not cited as verified.
- **Hirschman, *Exit, Voice, and Loyalty*** (1970): Crossref returned only secondary work. A natural operator triple (exit, voice, stay) for a member of a group, not confirmed here.
- **Goffman, *Interaction Ritual*** (Routledge reissue exists, doi:10.4324/9780203788387); face-work content not read. Likely belongs to the sociology/social-psychology agents.
- **Brown-Levinson formula in the original text:** secondary sources agree on the form W_x = D(S,H) + P(H,S) + R_x but notation varies (one source writes P(S,H)).
- **Hechter, Greif, Axelrod's *Evolution of Cooperation*:** not searched.
- **Independent accuracy audit of Bueno de Mesquita's model** beyond those cited in item 3: none found.

---

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
- **Authority and legitimacy of an operator** (who can perform a rite, who can declare a status) is absent except in the unconfirmed Searle item.
- **Forecasting claims are weak outside statistics.** The one famous "90 percent" forecasting result (BdM) is unverifiable from open sources. The statistical models (SAOM, REM) fit and describe; the sources retrieved give no out-of-sample benchmark.
- **The strongest formal results (core, Shapley, veto) are about static stability; the strongest dynamic models (SAOM, REM) have almost no semantic content about what the ties or events mean.** The algebra's opening is to supply typed, meaningful operators to the dynamics machinery, and typed operands to the stability theory.
