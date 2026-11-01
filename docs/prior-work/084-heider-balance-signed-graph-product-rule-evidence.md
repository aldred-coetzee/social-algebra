# Prior work 084: Heider balance, the signed-graph product rule, Davis weak balance, Caplow triads, Bowen triangles

Direction: D207

Date: 2026-10-29. Deep-read plus cross-check, merged. Question: which triad rules are algebraic, which are tested, and how well do real signed networks obey balance?

**Provenance rule applied.** A claim is [read] only if I fetched and read the text of the work itself this session. Otherwise [sa] (secondary account: a search summary, a later paper's description, or my background knowledge). Nothing [sa] may feed an equation.

**What I actually read (and what I did not).**

| Work | Status | Route and caveat |
|---|---|---|
| Cartwright & Harary 1956 | **read in full** | Scanned page images with a text layer, fetched from a third-party copy (sitpor.org); the running header and pagination match Psychol. Rev. 63(5), 277-293. Not the publisher's copy. |
| Leskovec, Huttenlocher & Kleinberg 2010, WWW ("Predicting positive and negative links") | **read, nearly all** (sections 1-5) | arXiv:1003.2429. The preprint, not the proceedings text; tables came out of the PDF in column order, so my row/column reading of Tables 6-7 is an inference (flagged below). |
| Leskovec, Huttenlocher & Kleinberg 2010, CHI ("Signed networks in social media") | **read: introduction, summary of findings, Tables 1-3 and the undirected-triad section** (validation pass 2026-10-30 read Table 3 and the surrounding text) | arXiv:1003.2424. Triad counts in section 4 now come from its Table 3. |
| Facchetti, Iacono & Altafini 2011, PNAS | **read in full, main text** (re-opened and checked by the validation pass) | Wayback copy of the PNAS PDF (PNAS content is free after six months). The SI (bounds, rate-distortion detail, Tables S1-S5) was NOT read. |
| Estrada & Benzi, "Are social networks really balanced?" | **read to the "tuning balance" section** | arXiv:1406.2132, the preprint. Published as Phys. Rev. E 90, 042802 (2014), "Walk-based measure of balance in signed networks" (title differs; DOI check below). I did not read the SI or the closing sections; the published numbers may differ from the preprint. |
| Kirkley, Cantwell & Newman 2019, PRE | **read: abstract, sections I-III B (about two thirds)** | arXiv:1809.05140. Did not read the multi-edge prediction results in detail. |
| Chiang et al. 2013 (arXiv:1302.5145) | **grep only**: definitions 6-7 and Theorem 8 lines | Used only as a relay for Davis's theorem; tagged [sa] for Davis. |
| Heider 1946 | **NOT read** (paywalled) | Quoted by C&H 1956 (which I read) at p. 110; those quotes are tagged [read via C&H]. |
| Davis 1967 | **NOT read** (paywalled; no open copy found; not in Unpaywall or Semantic Scholar OA) | [sa] via Chiang 2013, Kirkley 2019, Leskovec 2010a (CHI). Note: Leskovec 2010b (WWW) cites a *different* Davis paper for weak balance, Davis 1963 (AJS), also not read. |
| Caplow 1956, 1968; Simmel 1908; Burt 1992; Bowen | **NOT read** | [sa]. Search summaries only. |

**Verified bibliographic data (Crossref, 2026-10-29).**
- Heider, F. (1946). Attitudes and cognitive organization. *J. Psychol.* 21(1), 107-112. doi:10.1080/00223980.1946.9917275. (Facchetti's reference list says 107-122: a typo; C&H and Crossref say 107-112.)
- Cartwright, D. & Harary, F. (1956). Structural balance: a generalization of Heider's theory. *Psychol. Rev.* 63(5), 277-293. doi:10.1037/h0046049.
- Davis, J. A. (1967). Clustering and structural balance in graphs. *Human Relations* 20(2), 181-187. doi:10.1177/001872676702000206.
- Davis, J. A. (1963). Structural balance, mechanical solidarity, and interpersonal relations. *Am. J. Sociol.* 68(4), 444-462. doi:10.1086/223401. (Added in validation: this is the Davis paper Leskovec 2010b's ref [7] cites for weak balance; the clusterability theorem is the 1967 paper, as cited by Leskovec 2010a, Kirkley and Chiang. Not read.)
- Caplow, T. (1956). A theory of coalitions in the triad. *Am. Sociol. Rev.* 21(4), 489-493. doi:10.2307/2088718. (Crossref records first page 489 only.) Further development: Caplow (1959), *Am. J. Sociol.* 64, 488-493, doi:10.1086/222544. Book: *Two Against One: Coalitions in Triads* (Prentice-Hall, 1968) (no DOI found; citation from file 11 and secondary sources).
- Leskovec, Huttenlocher & Kleinberg (2010a). Signed networks in social media. *CHI 2010*, 1361-1370. doi:10.1145/1753326.1753532. (2010b). Predicting positive and negative links in online social networks. *WWW 2010*, 641-650. doi:10.1145/1772690.1772756.
- Facchetti, Iacono & Altafini (2011). *PNAS* 108(52), 20953-20958. doi:10.1073/pnas.1109521108.
- Estrada & Benzi (2014). *Phys. Rev. E* 90, 042802. doi:10.1103/PhysRevE.90.042802. Preprint arXiv:1406.2132.
- Kirkley, Cantwell & Newman (2019). Balance in signed networks. *Phys. Rev. E* 99, 012320. doi:10.1103/physreve.99.012320.
- Not resolved: Simmel (1908) *Soziologie*; Burt (1992) *Structural Holes*; Bowen (1978) *Family Therapy in Clinical Practice*. Citations taken from the seed list; no DOI sought.
- Chiang, Hsieh, Natarajan, Tewari & Dhillon, "Prediction and clustering in signed networks: a local to global perspective", arXiv:1302.5145 (authors confirmed from arXiv metadata; published JMLR 15 (2014), no DOI). Theorem 8 opened in validation: "Weak balance theory, Davis [1967]" as stated in section 3 below.
- Coalition literature named in section 8 (added in validation, Crossref-resolved, none read): Chertkoff (1967) A revision of Caplow's coalition theory, *J. Exp. Soc. Psychol.* 3, 172-177, doi:10.1016/0022-1031(67)90020-0 (this is the "1967 ScienceDirect" revision); Gamson (1961) A theory of coalition formation, *Am. Sociol. Rev.* 26, 373 (first page per Crossref), doi:10.2307/2090664; Vinacke & Arkoff (1957) An experimental study of coalitions in the triad, *Am. Sociol. Rev.* 22, 406 (first page per Crossref), doi:10.2307/2089158; Komorita & Chertkoff (1973) A bargaining theory of coalition formation, *Psychol. Rev.* 80, 149-162, doi:10.1037/h0034341. Murnighan 1978: two candidates exist (*Behavioral Science* 23, 195-208, doi:10.1002/bs.3830230308; *Psychol. Bull.* 85, 1130-1153, doi:10.1037/0033-2909.85.5.1130); which one the "five-person games" claim refers to is not established.
- Works found while testing this file's "nothing exists" claims (Crossref-resolved; see Unconfirmed): Doreian & Krackhardt (2001), Pre-transitive balance mechanisms for signed networks, *J. Math. Sociol.* 25, 43-67, doi:10.1080/0022250X.2001.9990244; Askarisichani, Lane, Bullo, Friedkin, Singh & Uzzi (2019), Structural balance emerges and explains performance in risky decision-making, *Nat. Commun.* 10, 2648, doi:10.1038/s41467-019-10548-8; Antal, Krapivsky & Redner (2005), Dynamics of social balance on networks, *Phys. Rev. E* 72, 036121, doi:10.1103/PhysRevE.72.036121; Marvel, Strogatz & Kleinberg (2009), Energy landscape of social balance, *Phys. Rev. Lett.* 103, 198701, doi:10.1103/PhysRevLett.103.198701; Marvel, Kleinberg, Kleinberg & Strogatz (2011), Continuous-time model of structural balance, *PNAS* 108, 1771-1776, doi:10.1073/pnas.1013213108.

---

## 1. Heider (1946): the P-O-X unit

**Their vocabulary.** P (person), O (other), X (impersonal entity or event). Two relation types: L (liking/evaluating, positive L or ~L) and U (unit formation: ownership, causation, proximity, belonging, positive U or ~U). "Balanced state", "forces towards this state", "tension".

**Heider's text, as quoted by C&H 1956 (ref 9, p. 110) [read via C&H, not at source].**
- "In the case of two entities, a balanced state exists if the relation between them is positive (or negative) in all respects, i.e., in regard to all meanings of L and U." For three entities Heider says the state is balanced if all three relations are positive, or if two are negative and one positive.
- "If no balanced state exists, then forces towards this state will arise. Either the dynamic characters will change, or the unit relations will be changed through action or through cognitive reorganization. If a change is not possible, the state of imbalance will produce tension (9, pp. 107-109)."

**Drives/operands.** Operand: a single person's cognitive field of three entities, signed relations on the pairs. The only "drive-like" element is the **tendency toward balance** plus **tension** from imbalance. Heider's own later remark that unbalanced states can please (quoted in Estrada & Benzi, from Heider 1958 [read via Estrada-Benzi, secondary]): "there may also be a tendency to leave the comfortable equilibrium, to seek the new and adventurous. The tension produced by unbalanced situations often has a pleasing effect . . . Balanced situations can have a boring obviousness". That is a curiosity-like counter-pull on the same structure.

**Operators/equations.** None numeric. Verbal rule: balanced iff the product of the three signs is positive (all three +, or two - and one +).

**Scale.** Intra-individual cognition (membership scale only in a loose sense: how one person holds relations to two others and an object). Not a group property in Heider.

**Empirical standing at Heider's own scale (all [read via C&H], second-hand).** Horowitz, Lyons & Perlmutter (discussion-group members, sociometric then evaluation of an event): data "tend to support" balanced P-O-X; C&H footnote 2: "It is not clearly demonstrated that P likes Xs produced by liked Os and dislikes Xs produced by disliked Os." Jordan: 64 hypothetical situations, rated unpleasantness; "negative relations were experienced as unpleasant even when contained in balanced units" (a positivity effect separate from balance). C&H's own re-analysis of Jordan (C&H p. 291): balanced 39, vacuously balanced 51, not balanced 66 mean unpleasantness; unreclassified: balanced 46, imbalanced 57. These are hypothetical-scenario ratings by single subjects; no field or behaviour outcome. I did not see Jordan's N or tests.

---

## 2. Cartwright & Harary (1956): the signed-graph product rule [read in full]

**Their vocabulary.** Point, line, graph, digraph, s-graph (signed graph), s-digraph, sign of a line (+1/-1), sign of a cycle, semicycle, balanced, degree of balance, N-balance, local balance, articulation point, "clique" (given a special meaning).

**Definitions, exactly [read].**
- "The sign of a cycle is the product of the signs of its lines. For convenience we denote the sign of a line by +1 or -1 when it is positive or negative." "A cycle is positive if it contains an even number of negative lines, and it is negative otherwise."
- "We define an s-graph (containing any number of points) as balanced if all of its cycles are positive." Digraph version: balanced if all **semicycles** are positive.
- Degree of balance: "c(G) = the number of cycles of G, c+(G) = the number of positive cycles of G, b(G) = c+(G)/c(G)". "the degree of balance of an s-graph is the probability that a randomly chosen cycle is positive." b(G) = 1 iff G balanced.
- N-balance: "an s-graph [is] N-balanced if all its cycles of length not exceeding N are positive." Footnote 10: "regard cycles of length N as having weight 1, and all longer cycles as of weight 0 . . . generalize . . . by assigning weights to each length, e.g., weight 1/2^n to length N." (This is the seed of the length-weighted walk measures of Estrada-Benzi and Kirkley et al.)
- Local balance at P: "all cycles through P are positive."

**Theorems stated (proofs deferred to Harary 1953-54, which I did not read) [read: the statements].**
- "An s-graph is balanced if and only if all paths joining the same pair of points have the same sign."
- **Structure theorem**: "An s-graph is balanced if and only if its points can be separated into two mutually exclusive subsets such that each positive line joins two points of the same subset and each negative line joins points from different subsets." One subset may be empty (e.g. a connected all-positive graph).
- Local balance theorem: "If a connected s-graph G is balanced at P, and Q is a point on a cycle passing through P, where Q is not an articulation point, then G is also balanced at Q."
- Influence corollary (conditional): if positive liking lets people influence positively and negative liking only negatively, then in a balanced graph "the sign of the influence exerted by any point upon any other will be the same, no matter what path is followed", giving "homogeneity within cliques and opposing opinions between cliques". This is a conditional on an assumed influence law, not an empirical finding.

**Cross-check on attribution (matters for later reading).** Leskovec et al. state "Theorem 1 (Cartwright-Harary)" for a **complete** graph whose **triangles** are all balanced (all triangles odd in positives implies two-clique partition). The C&H text I read states the theorem for **all cycles** in any s-graph and does not state the complete-graph/triangle version. The local-to-global triangle form is therefore a corollary (for complete graphs every cycle is generated by triangles), not C&H's wording; attribute the cycle form to C&H and Harary 1953-54. The paper's own scope: "Whether or not empirical theories of balance will be confirmed by research dealing with larger structures can only be determined by empirical work."

**What C&H explicitly leave out [read].** Strength of relations ("our present use of graph theory can treat only the structural, and not the numerical, aspects of relations"); "One of the principal unsolved problems is the development of a systematic treatment of relations of varying strength." They distinguish **complement** ("not liking") from **opposite** ("disliking"): absence of a line vs a negative line. Relations of different types (L and U) are lines of different type in an "s-graph of type 2"; the tentative rule is "simply to ignore the types of lines involved", flagged as untested for longer cycles.

**Group size and composition.**
- Any finite n; "contains no such limitation" as Heider's three. Degree of balance depends on structure: for the complete graph on 3 points b is 0 or 1; for a 4-point graph with five lines (Fig. 9) only .33 and 1.00 are possible; "50% does not even occur". "Any interpretation given to the numerical value of b(G) must take into account the distribution curve for b(G), which is determined by the structure of G." So b(G) is not comparable across graphs of different size or density without a null model.
- Cycles of length 100 "will not matter at all to the group as a whole" is asserted, not tested: this is why N-balance is introduced.
- Composition: unsymmetric relations are covered by digraphs; "whenever the lines PO and OP are of different signs, the s-digraph containing them is not balanced".

**Operand/operator translation.** Operands: persons, with a symmetric or directed signed relation on pairs. The key operator is **multiplication in {+1, -1}** (the group Z2) along a path, with **balanced = every closed path multiplies to +1**. Equivalent forms [read]: path-sign well-defined (potential-like), and two-clique partition (a 2-colouring in which edge sign = product of endpoint colours). Not algebra over drives: the sign is a **valence** of a relation, not a drive.

---

## 3. Davis (1967): weak balance and clusterability [NOT read; [sa]]

**Statement [sa], consistent across three sources I did read.** Leskovec 2010a (CHI; read; the quote below is from this paper, which cites Davis 1967; the WWW paper cites Davis 1963 instead): weak balance "posits that only triangles with exactly two positive edges are implausible in real networks, and that all other kinds of triangles should be permissible"; proposed "as a way of eliminating the assumption that 'the enemy of my enemy is my friend'". Kirkley et al. 2019 (read): "weak balance": "no closed loops in the network with exactly one negative edge"; Davis showed this suffices for clusterability, "any number of disjoint sets such that all edges within sets are positive and all edges between sets are negative"; strongly balanced networks are a subset of weakly balanced ones. Chiang et al. 2013 (Theorem 8 opened and confirmed verbatim in validation): a complete network is weakly balanced iff either all edges are positive, or nodes divide into k clusters (positive within, negative between). The earlier "negative edges per triangle" and "positive edges per triangle" counts used by Leskovec and by Kirkley are different phrasings of the same rule: forbid the single-negative-edge cycle (equivalently the triangle with exactly **two positive** edges, i.e. exactly one negative).

**Careful on wording.** Leskovec says forbidden = "exactly two positive edges" (one negative). Kirkley says "exactly one negative edge". Same triangle. Fine, but note Leskovec's (T2) triangle (CHI Fig. 1 calls it "two enemies with a common friend") is the triangle with two positive edges and one negative: the unbalanced triangle that "the friend of my friend is my enemy" produces. The "enemy of my enemy" triangle is T1 (one positive, two negative), which weak balance **permits** and strong balance requires.

**Algebraic reading (my inference, not in the sources).** Strong balance is a total rule: sign(u,v) = s(u,w)·s(w,v) in Z2, closed under composition. Weak balance is a **partial** rule: + then + gives +, + then - gives -, and - then - gives "unconstrained". It is not a group law; it is a partial operation (or a relation) on {+,-}. The group structure is lost at exactly the cell the data reject.

---

## 4. Leskovec, Huttenlocher & Kleinberg (2010): balance vs status on three online networks [read]

**Their vocabulary.** Signed directed link, sign prediction, triad type (16 for directed: [F|B][F|B][p|m][p|m]), embeddedness (common neighbours), balance, weak balance, status, "theory of triad types" f: {types} -> {+1,-1,0}.

**Data [read].**

| Network | Nodes | Edges | % positive | Meaning of sign |
|---|---|---|---|---|
| Epinions | 119,217 | 841,200 (Table 1 of both papers; the WWW body text says 841,000) | 85.0 | trust / distrust of another user, 1999 to Aug 2003 |
| Slashdot | 82,144 | 549,202 | 77.4 | friend / foe tag, crawled Feb 2009 |
| Wikipedia admin elections | 7,118 | 103,747 | 78.7 | support / oppose vote; 2,794 elections |

SNAP datasets. Scale: **pair and triad within large online communities**; no groups in the face-to-face sense, no consent or manipulation (observational, signs are self-reported ratings or votes).

**Equations, exactly [read].**
- Balance as a triad theory: "structural balance theory posits that (u,v) should have the sign that causes the triangle on u, v, w to have an odd number of positive signs, regardless of edge direction": f_balance(tau) = s-bar(u,w) · s-bar(v,w).
- Status theory: positive edge (x,y) means x regards y as higher status; negative edge, lower status. After orienting the two edges u->w->v with signs adjusted, f_status(tau) = sign(s(u,w) + s(w,v)); "status theory makes no prediction when the two signs cancel out". Note this is an **additive** rule on an ordered set, not the multiplicative Z2 rule.
- Theorem 1 as they state it: complete undirected graph, every triangle with an odd number of positive edges implies a partition into two sets with positive inside, negative across. Theorem 2 (their own, with proof): tournament in which every triple is status-consistent has a total order with positive edges forward and negative edges backward.
- Status heuristic: sigma(x) = d+_in(x) + d-_out(x) - d-_in(x) - d+_out(x) (the text states it as status benefits for each positive link received and each negative link generated, detriments for each negative received and positive generated); predict + if sigma(u) <= sigma(v).

**Results [read].**
- Sign prediction, balanced test set (50% chance), min embeddedness 25, 10-fold CV: logistic regression on 23 features. Epinions error: 11.45% (degree features), 6.64% (16 triad features), 6.58% (all 23), against the best prior (Guha et al.) 14.7%. Wikipedia is "significantly lower" in accuracy; the paper conjectures status plays a stronger role in a "publicly visible voting forum". Triad features help less at low embeddedness. On the full (unbalanced, ~80% positive) data, accuracy is 90-95%, "roughly a 15% absolute improvement over random guessing", AUC about 90% (balanced) and 95% (full).
- Cross-dataset (Table 6; the caption reads "training on the 'row' dataset and evaluating the prediction on the 'column' dataset", so rows = training, columns = test; confirmed in validation, same caption on Table 7): All-23 trained on any network and tested on Epinions or Slashdot scores about 0.925-0.935; on Wikipedia about 0.77-0.80. Good transfer.
- Balance vs learned model: "balance theory consistently disagrees with the learned model (and with status theory) when it predicts that a negative (u,w) and negative (w,v) edge should suggest a positive (u,v) edge", i.e. **enemy-of-my-enemy fails** in all three datasets. Reduced undirected model: learned coefficients agree with balance on every triad type except the "mm" (enemy of enemy) type, "consistent with . . . Davis . . . weak balance".
- Reduced-model accuracy (Table 7, rows = training, columns = test, per caption): hand-set deterministic rules: BalanceDet 0.771 (Epinions), 0.841 (Slashdot), **0.578 (Wikipedia, barely above chance)**; WeakBalance 0.823, 0.870, 0.608; StatusDet 0.808, 0.717, 0.668. Learned balance coefficients: about 0.90 (Epinions), 0.915-0.92 (Slashdot), 0.73-0.76 (Wikipedia), transferring across datasets. Status coefficients transfer poorly: "status properties are more particular to a given dataset".
- **Global tests (Table 8, numbers read in validation).** For balance, maximise satisfied edges over a two-way partition by a single-node-flip heuristic: network 0.834 / 0.811 / 0.781 (Epinions / Slashdot / Wikipedia); permuted signs 0.856 / 0.778 / 0.787; rewired 0.899 / 0.831 / 0.832. The values "are comparable to the total fraction of positive edges" (trivially achieved by one big cluster). The rewired baseline beats the real network on all three; the permuted baseline beats it on Epinions and Wikipedia but not Slashdot. (Correction: the earlier text said both baselines "do as well or better", which is not true for permuted Slashdot.) Note also that 0.834 on Epinions is *below* the trivial one-cluster value of 0.85, so the heuristic did not even reach the trivial solution there. Verdict: "very little evidence for the global presence of structural balance". For status, network 0.791 / 0.822 / 0.854 vs permuted 0.724 / 0.757 / 0.777 and rewired 0.638 / 0.664 / 0.632; "about 80-85%" against 50% for a random ordering, and better than both baselines. They conclude "we can find no significant evidence for the kind of partitioning into factions that balance theory suggests at a global level". **Caveat (validation):** Facchetti et al. (section 5), with an exact ground-state algorithm on the undirected versions of the same three sites, find frustrated fractions of 7.2% / 14.8% / 14.2%, well below the one-cluster values of q = 16.7% / 23.6% / 21.4%. So Leskovec's "no global partition better than trivial" is at least partly a property of their heuristic and of the directed-graph edge count, not a settled fact about the networks.
- CHI paper (read) states the triad-count version: weak balance fits, "triangles with exactly two positive edges are massively underrepresented . . . while triangles with three positive edges are massively overrepresented. In two of the three datasets, triangles with three negative edges are also overrepresented, which is at odds with Heider's formulation". **Table 3 (undirected triads, read in validation)**, described rather than transcribed (Leskovec et al. 2010a, CHI, Table 3; four triad types T3 +++, T1 +--, T2 ++-, T0 ---, each with observed fraction p, sign-shuffled expectation p0 and surprise s). Values used: T3 is observed at 0.870 / 0.840 / 0.702 against expected 0.621 / 0.464 / 0.489 (Epinions / Slashdot / Wikipedia; surprise positive in all three, +1881.1 in Epinions). T2 is observed at 0.052 / 0.077 / 0.080 against expected 0.321 / 0.406 / 0.395 (surprise -2104.8 / -823.5 / -572.6). T1 is observed at 0.071 / 0.072 / 0.207 against expected 0.055 / 0.119 / 0.106 (surprise +249.4 / -175.2 / +289.1). T0 is observed at 0.007 / 0.011 / 0.011 against expected 0.003 / 0.012 / 0.010 (surprise +227.5 / -8.7 / +10.8).

  Triad totals 13,375,407 / 1,508,105 / 790,532. The text: T3 over-represented by "about 40%" in all three; T2 under-represented "by about 75% in Epinions and Slashdot and 50% in Wikipedia"; "none of the datasets follow Heider's theory in both having T1 overrepresented and T0 underrepresented", hence "more consistent with Davis's weaker notion". Note that at the *triad-count* level the enemy-of-enemy triangle T1 is over-represented in Epinions and Wikipedia and under-represented only in Slashdot; the across-the-board "enemy of my enemy fails" finding is the WWW paper's learned-coefficient result (mm type), a different test.
- Negative links help predict positive ones: "up to a factor of 1.5" boost over random on two of three datasets (Section 5 intro only).

**Group size and composition.** The authors note the scale argument directly (CHI paper, read): balance "predictions [are] aggregate rather than absolute", visible only when "accumulated over a large amount of data". Triad predictors improve with embeddedness then partly decline at very high embeddedness. Composition: balance fits better in Epinions and Slashdot (friend/trust semantics) than in Wikipedia (public, consequential votes). Reciprocated links obey balance more strongly but are a small share.

**Operand/operator translation.** The 16-type triad table is a lookup operator: (sign, direction) x (sign, direction) -> expected sign. Balance = multiplicative on undirected signs; status = additive on directed. The data prefer the partial/weak form of the first and a directed additive form of the second, with no single total rule.

---

## 5. Facchetti, Iacono & Altafini (2011): global balance as spin-glass ground state [read, main text]

**Their vocabulary.** Signed graph, frustration, gauge transformation (Toulouse; switching equivalence, Zaslavsky), line index of balance, ground state, MAX-CUT, apparent disorder vs true frustration, Mattis system, rate-distortion.

**Equations, exactly [read].**
- [1] h(s) = sum over edges (i,j) of (1 - J_ij s_i s_j)/2, with J_ij in {+1,-1}, s in {+1,-1}^n.
- [2] delta = min over s of h(s) = min (m - (1/2) s^T J s). "Exactly balanced" iff delta = 0. For connected signed graphs, exactly balanced iff the smallest eigenvalue of the Laplacian L = K - J is zero (citing Kunegis et al.).
- [3] J -> J_sigma = T_sigma J T_sigma, with signature matrix T_sigma = diag(sigma), preserving frustration while reducing negative entries. [4] h(sigma) = m - (1/2) sigma^T J sigma.
- Distortion D = delta/m; rate R = n/m; Shannon bound from the rate-distortion theorem for i.i.d. Bernoulli(q) signs (details in SI, not read).

**Data and results [read].** Epinions, Slashdot, WikiElections, undirected after symmetrisation (n = 131,513 / 82,062 / 7,114; m = 708,507 / 498,532 / 100,321; fraction negative q = 0.167 / 0.236 / 0.214).

Results table (Facchetti et al. 2011, PNAS), described rather than transcribed: for Epinions / Slashdot / WikiElections the upper bound on the ground-state frustration delta_up is 50,806 / 73,604 / 14,245 edges, i.e. delta_up/m = 0.0717 / 0.1476 / 0.1420; the Bernoulli null gives delta_up of 105,520 / 106,163 / 20,880; the share of balanced nodes is 83.71% / 68.29% / 52.94%.

(Bounds delta_low/delta_up 0.993, 0.951, 0.996, so the Epinions and Wikipedia optima are essentially exact.) Null models are far more frustrated (Z test p < 1e-100 in the caption); the real networks lie below the Shannon bound. Claim: "currently available networks are indeed extremely balanced".

**Why, per the authors.** Sign **skewness on nodes**: users with mostly positive or mostly negative edges. A node that is unanimously negative has all its negative edges removed by a gauge transformation: "individuals manifestly recognized as enemies do not add to the structural tension". "Unpopular individuals are easily 'cast away' from the bulk of the community without creating much conflict."

**Cross-check on what the paper does NOT show.** The null model is i.i.d. Bernoulli on the *same graph* (and a hypergeometric reshuffle in the SI). It tests that sign arrangements are better than random placement given q. It does **not** test that the networks satisfy Heider's triangle-level or Davis's prescriptions, and the authors themselves say "systematic predictions of the expected frustration, given the connectivity and the percentage of negative edges, are completely missing". The key reading problem: "extremely balanced" relative to random, not close to zero: delta/m is 7-15% of edges frustrated, and 15-47% of nodes are not tension-free. Moreover a majority-positive graph where everyone is in one big cluster already has delta/m = q = 16.7-23.6%, so the achieved 7.2-14.8% is a reduction from that trivial baseline of roughly 6-9 percentage points (Epinions 16.7 to 7.2, Slashdot 23.6 to 14.8, Wikipedia 21.4 to 14.2). (Corrected in validation: this sentence previously said Leskovec's Table 8 shows the same as the trivial partition; in fact Facchetti's optimum is clearly better than trivial, while Leskovec's heuristic partition is not, which points to the heuristic rather than to the networks.)

**Group size.** Scale is the network (n = 7k to 131k). The paper proves nothing about size dependence; R = n/m enters only through the Shannon bound. Local motif counting (triangle-only) is described as missing "long-range conflicts associated to longer cycles (and larger communities)".

---

## 6. Estrada & Benzi: do all cycles agree? [read to "tuning balance"; preprint]

**Equations [read].** Walk-balance index K = tr exp(A) / tr exp(|A|) = sum_j exp(lambda_j) / sum_j exp(mu_j) (signed vs underlying unsigned adjacency); 0 < K <= 1, K = 1 iff balanced; unbalance U = (1-K)/(1+K); K3 = tr(A^3)/tr(|A|^3) for triangle-only; node index K_i; generalised K(beta) = tr exp(beta A)/tr exp(beta|A|) as an "equilibrium constant". Weights closed walks by 1/k!. Theorem cited: signed network balanced iff spectra of A and |A| match (cited as ref 25, not read).

**Results [read, Table 1].**

Table 1 (Estrada & Benzi), described rather than transcribed; values used, for Epinions / Slashdot / WikiElections. Undirected: share balanced nodes from Facchetti 83.7 / 68.3 / 52.9%; K3 = 0.808 / 0.772 / 0.595; K of order 1e-15 / 1e-7 / 1e-12 (approximate), so U is 100% in each. Directed: K3 = 0.759 / 0.880 / 0.511; K = 0.761 / 0.069 / about 2.2e-5; U = 13.6% / 87.1% / 99.99%.

(The exponents are partly illegible in the PDF text; read as the table's orders of magnitude.) Their reading: by triad index (K3) the networks look balanced, reproducing Facchetti; by a measure weighting **all cycles** they are "very poorly balanced", "although they are more balanced than expected from a random allocation" (reshuffled K ~ 1e-17 Slashdot, 1e-18 Epinions, 1e-9 WikiElections, in the paper's order; Table 1 values checked in validation). Small systems: WWI alliances 1872-1907 K from 0.47 to 0.55 and K = 1 exactly in 1907 (no triad index agreed with this path, K3 = 0.428, 0.5, 0.2, ...); Gahuku-Gama New Guinea subtribes (16 nodes) K3 = 0.735 but K = 0.335 (U = 49.8%), "a moderately balanced network", and balance correlates with geography. They attribute much of the large-network imbalance to all-negative cycles, concordant with Leskovec's overrepresented all-negative triads (directed negative sub-networks U = 100% / 91.4% / 84.3%, not significantly different from reshuffled). **Caution (validation):** in the same passage Estrada-Benzi say Leskovec et al. found "enemy of my enemy" triads "significantly underrepresented" and one-negative triads "overrepresented" in all three networks. That misreports Leskovec CHI Table 3, where the one-negative triad T2 is strongly *under*-represented in all three and the enemy-of-enemy triad T1 is under-represented only in Slashdot. Do not relay Leskovec's triad findings through Estrada-Benzi.

**Cross-check, which is right?** Facchetti's and Estrada-Benzi's headlines ("extremely balanced" vs "very poorly balanced") **do not contradict each other**: they answer different questions about the same data. Facchetti measures the minimum fraction of edges to delete (ground-state frustration), every cycle length weighted equally in effect; Estrada-Benzi measure a spectral ratio that weights short cycles (1/k!) and is **hypersensitive to size**: with n of order 1e5, K is a ratio of sums of exponentials of eigenvalues and falls toward zero (1e-15) as long cycles accumulate even when each short cycle is mostly balanced. (This size-sensitivity explanation is my inference from the form of K and from the 1e-15 values; neither paper tests it.) K itself is not scaled by n or m, so values across networks of different size are not comparable, and the 1/k! weighting has no empirical calibration (Kirkley et al. say exactly this: "there is no way to set the length scale on which loops are discounted"). Leskovec's finding (weak, not strong, balance locally; no global two-faction structure) is consistent with *both*: Heider balance fails locally at "enemy of enemy", and the global partition is not better than a trivial one by Leskovec's heuristic (though Facchetti's exact optimum is; see section 5). The only claim all four support is the soft one: more balanced than sign-shuffled nulls. Claims of "extremely balanced" and of "very poorly balanced" are each artifacts of the measure.

---

## 7. Kirkley, Cantwell & Newman (2019): weak balance, a null that fixes the edges [read, about two thirds]

**Equations [read].** Imbalance as a length-discounted cycle count B(z) = sum_k I_k / z^k with closed walks standing in for cycles. Weak: B_W(alpha) = (1/2) Tr[N (alpha lambda_P I - P)^-1], P and N the positive and negative adjacency matrices. Strong: B_S(z) = (1/4) log( det[zI-(P-N)] / det[zI-(P+N)] ). Free length scale alpha = z/lambda; decay length k0 = 1/ln alpha. They also restate Estrada-Benzi (B_EB = (1-K)/(1+K)) and Singh-Adhikari's version (geometric weights). Null model: **signs shuffled, edge positions fixed, counts of + and - fixed**, which they argue is "essential for proper quantification".

**Results [read].** 70 yearly international-relations networks, 1938-2008 (alliances positive, militarised disputes negative; n = 25-155, median 105; edges median 615; negative share 1.8-45.1%, median 5.5%) and four time points of a 34-student freshman class (rating scale; edges 174-227; negative share 12-14%). All four measures give imbalance below the null for all years (p < 0.05 assuming normality), "most significant . . . during the World War II period", where "strong balance is expected in cases where a network is divided into just two factions". Sign prediction by choosing the sign that maximises balance (single hidden edge), international-relations data: by **accuracy** (Fig. 3), the weak-balance measure B_W "substantially outperforms the other measures and the baseline", but the Estrada-Benzi measure "performs least well . . . and in some cases is actually below the baseline estimate, particularly in the latter half of the data set"; by **normalised mutual information** (Fig. 4), all four measures beat the majority-sign guess (which scores NMI 0 by construction), and "the weak balance measure B_W does best in most years, in some cases by a wide margin". (Corrected in validation: the earlier text said all measures beat the majority baseline in all years; that holds for NMI only, not accuracy.) No absolute accuracy number is given in the text (figures only), and the multi-edge simulated-annealing results I only skimmed.

**Group size and composition.** The paper says networks of ~100 nations and ~34 students are significantly balanced, with larger effect for **polarised, two-bloc** conditions (WWII; "especially pronounced for the three metrics based on the strong notion"), and less extreme values for the students. "If there are three or more factions then the network will, in general, be only weakly balanced" is their definitional argument in the introduction, not an empirical finding.

---

## 8. Caplow (1956, 1968): triad coalitions [NOT read; [sa]]

**Statement [sa] (search summaries only; the wording follows no single source I can name, the primary source is Caplow 1956, Am. Sociol. Rev. 21(4), 489-493, not read; if any sentence derives from a Wikipedia article it is CC BY-SA 4.0 and the article was not recorded).** Triad members differ in strength; stronger members seek to control weaker ones; Caplow enumerated the possible three-person power configurations (the file-11 note says six types) and predicted which pair coalesces. One search summary gives his prediction for A > B > C with A < B + C: only A-C and B-C coalitions form (weaker, or at least the weakest, joins). A later revision (Chertkoff 1967, *J. Exp. Soc. Psychol.*; identified in validation from its ScienceDirect abstract) says it yields identical predictions to Caplow and to Gamson's cheapest-winning-coalition theory for all triad types except A > B > C, A < B + C. I did not see the six types or the equations; I do not know Caplow's own derivation. **No Caplow formula may feed the algebra.**

**Empirical standing [sa].** Gamson (1961) minimum-resource theory is described as making the same predictions as Chertkoff's revision of Caplow for six triad types, plus payoff predictions. Experimental results are mixed (all [sa] from search summaries): a 54-undergraduate experiment favoured equity theory, with "conservative, strong against weak" coalitions; Murnighan (1978, five-person games) favoured Komorita-Chertkoff bargaining theory over Gamson; a Japanese junior-high study found weaker pairs most often coalesced in some types but closer to chance than Vinacke & Arkoff's original data. I could not confirm effect sizes or Ns. Scale: **group (n = 3) decision**, experimental games with imposed resource weights; the "intervention" is the experimenter assigning power, so a manipulation of structure not of drives.

**Group size.** n = 3 exactly. Whether the rule extends to n > 3 is a separate literature (Gamson's minimum resource, Komorita-Chertkoff bargaining) that I did not survey. The sociology of 4-person families appeared in the search results (a Iowa CRISP page) but I did not open it.

**Operand/operator translation.** Operand: three persons with a scalar **resource/power** each. Operator: "which pair merges" as a function of the power vector under a threshold (does a pair exceed the third: A < B + C). This is a **resource-weight** model, not a sign model: no valence, no drive. The algebraically interesting content is the threshold comparison, i.e. a simple game-theoretic coalition structure.

---

## 9. Simmel (1908), Burt (1992), Bowen triangles [NOT read; [sa]]

- **Simmel's dyad/triad** [sa: file 11 and general knowledge; primary source Simmel 1908, *Soziologie*, not read; the labels are the standard secondary-literature summary and may derive from encyclopedia articles, which if Wikipedia would be CC BY-SA 4.0, source not recorded]: the triad introduces the third party roles of mediator (tertius), the one who profits (tertius gaudens), and divide-and-rule. These are *operators on a pair relation* by a third, which is conceptually the operator that balance theory omits (balance only checks a sign product).
- **Burt's structural holes** [sa; primary source Burt 1992, *Structural Holes*, not read; wording is a search-summary paraphrase, and any Wikipedia-derived sentence would be CC BY-SA 4.0, source not recorded]: the actor spanning a hole between two otherwise unconnected contacts gains control benefits. Constraint and effective size are computed from tie strengths. Note the contrast with balance: Burt's indices use **unsigned weights**, and the broker's advantage is in a triad with a **missing** edge, where balance theory is silent (it only constrains closed triangles).
- **Bowen triangles** [sa: search summaries only; primary source Bowen 1978, *Family Therapy in Clinical Practice*, not read; any Wikipedia-derived wording would be CC BY-SA 4.0, source not recorded]: a two-person system under stress "triangulates" a third; "differentiation of self" is the proposed capacity to remain connected without fusion. Search found only that a small review (eight studies, late 1990s) reported some Bowen concepts supported and two instruments built, and that, in the review's own words as the search summary quoted them, "empirical studies . . . mostly focus on the negative effects of triangulation" (review not named in the summary and not opened, so author, year and journal are unknown; quoted second-hand); I found no meta-analysis and did not open any source. Treat Bowen's content as clinical theory without a validated quantitative form; see file 13 for earlier discussion.

---

## 10. Which triad rules are algebraic, which are tested, how well

| Rule | Algebraic form | Read at source? | Tested where, how well |
|---|---|---|---|
| Balance (Heider/C&H): sign of a cycle = product of signs; balanced iff all +1 | Multiplication in Z2; cycle space / gauge group; Boolean-linear (XOR) system; two-clique partition | C&H yes; Heider via quote | Triad counts in 3 online nets: only partly (two-positive triangle strongly under-represented as predicted; all-negative triads over-represented in 2 of 3; enemy-of-enemy coefficient wrong-signed in the learned model). Global two-faction partition: no better than trivial by Leskovec's heuristic, but clearly better than trivial by Facchetti's exact ground state (7-15% vs 17-24% frustrated). Better than sign-shuffled null: yes, by every measure (Facchetti, Estrada-Benzi, Kirkley). |
| Weak balance (Davis): forbid cycles with exactly one negative edge | Partial operation: (-)(-) unconstrained; clusterable into k >= 2 groups | No (sa) | Best-fitting triad rule in online data (Leskovec); best single-sign predictor among balance variants in the nations data (Kirkley; figures only; the sign-prediction tests were run on the international-relations networks, not the freshmen). |
| Status (Leskovec): sign + orientation, additive on an order | Order-theoretic: f = sign(s1 + s2) with ties undefined | Yes | Wins on directed data (global 80-85% of edges ordered vs 50%); transfers poorly across datasets. |
| Degree of balance b(G) = c+/c | Fraction of positive cycles | Yes (C&H) | Not comparable across sizes without a null (C&H, Facchetti). |
| Weighted-walk indices K, B_W, B_S | Matrix functions of P, N | Yes (preprints) | Scale-dependent; weighting arbitrary (Kirkley's point). |
| Caplow coalition by power vector | Threshold on weights | No | Mixed, [sa]. |
| Simmel/Burt/Bowen third-party operators | Not formalised as algebra here | No | Burt: strong in organisational settings per his own work (not checked here); Bowen: thin [sa]. |

---

## Operand/operator translation (summary for the algebra)

1. **A usable law**: along any path of signed ties the relation composes by multiplication in {+1,-1}; a closed path is "tense" iff its product is -1. This is exact, closed, and testable as a constraint. It is a *structure on relations*, so it is the cleanest candidate for a **relation-layer** law that sits beside, not inside, a drive layer.
2. **The data reject the totality of that law at one cell** ("enemy of my enemy"), and prefer a partial operation. A defensible algebra should treat (-)(-) as undefined or as a type-dependent result rather than +.
3. **A second law is needed for directed/status ties**: additive on an ordered set. The online data say the directed rule and the undirected rule are different operators, applicable at different resolutions.
4. **Gauge/switching** is a symmetry: flipping the sign of all edges at a node leaves tension unchanged. This is a free invariance (a theorem about what cannot be distinguished). It also explains why unanimously disliked members do not add tension.

---

## Unconfirmed

- Heider 1946 itself, Davis 1967, Davis 1963, Caplow 1956/1959/1968, Simmel, Burt, Bowen: not read. All claims about them are [sa] or quotations seen inside C&H.
- **C&H 1956 content was not re-checked in validation.** The only open copies are third-party reposts of a paywalled article (sitpor.org, a course-reading mirror); the validation pass did not fetch them, so the [read] tags in section 2 rest on the original pass alone. The definitions (cycle sign = product; balanced iff all cycles positive) agree with how Estrada-Benzi, Kirkley et al. and Leskovec et al. restate them, which the validation pass did read, but the verbatim quotes, page numbers and Jordan's figures (39/51/66, 46/57) are unverified by a second reader.
- The exact six Caplow triad types, his predictions, and any N or effect size in the coalition experiments.
- Facchetti SI (bounds, Tables S1-S5, the proof detail on the Shannon bound).
- Estrada-Benzi: published PRE version vs arXiv preprint; the 1/k! weight theorem proof; the SI results on undirected negative sub-networks.
- Kirkley et al. absolute sign-prediction accuracies (figure-only; the text gives none).
- Harary 1953-54 (proof of the structure theorem); Zaslavsky (1982) on signed graphs; Antal-Krapivsky-Redner (2005) dynamics of balance; Marvel-Strogatz-Kleinberg (2009) energy landscape and Marvel-Kleinberg-Kleinberg-Strogatz (2011) continuous-time model (existence and authors confirmed at Crossref in validation; none opened). The *models* of how tension drives edge flips are therefore not covered here.
- **Corrected in validation: the "no source found" claim on small face-to-face groups (n > 3) was false.** (a) This file itself reports Kirkley et al.'s 34-student freshman class at four time points, significantly more balanced than the sign-shuffled null. (b) Doreian & Krackhardt (2001) test balance mechanisms over time on Newcomb's longitudinal fraternity data (17 men; Nordlie 1958) [sa, search summary; not read]. (c) Askarisichani et al. (2019, *Nat. Commun.*): 66 day traders over two years, affect inferred from >2 million instant messages; abstract (read in validation): "triads of relationships . . . have a propensity towards affective balance, but one unbalanced configuration resists change. Further, balance is positively related to performance. Traders with balanced networks have the 'hot hand'". Effect sizes and which configuration resists change are in the body, not read. Leskovec CHI's "empirical investigations to date have generally focused on small networks" (read) cites a small-group literature not followed here.

---

## Does it reduce to a drive basis?

**Partly, and the reducible part is not the part that has equations.**

What can be recast as a person-level drive: **the tendency toward balance** itself. Heider's "forces towards this state" and "tension" are a consistency motive, and Jordan's ratings (via C&H: unbalanced 66, balanced 39, hypothetical scenarios, one person at a time) are the only [read] evidence of the tension. A drive reading of this: a per-person *consistency* drive, with imbalance as its error signal; and Heider's later remark (via Estrada-Benzi) about a pleasing side of tension is a *curiosity*-like opposite pull on the same signal. So the dynamics could be "each node reduces local frustration with some rate and some competing exploration drive". That is a hypothesis; none of the papers I read fit it. Facchetti, Estrada-Benzi, Kirkley et al. and Leskovec et al. measure static snapshots; none measures drive strength, rates of edge flipping, or tension in the people.

What does **not** reduce to a drive basis, from what I read:
- **The sign itself.** An edge sign is a *valence of a relation* (like/dislike, trust/distrust, vote for/against), not a drive of a person. Epinions "distrust" and Wikipedia "oppose" mean different things; Leskovec says it shows in the fit. A drive basis has to say what produces a sign (approach vs avoidance from a pair of drives?). None of the sources does.
- **The product rule and its gauge symmetry.** These are properties of the relation graph (cycle space over Z2), true whatever the drives are. They hold or fail as a statement about the *joint pattern* of signs, with no need for any drive.
- **Status.** In Leskovec's account a sign is an *assessment of rank* (higher/lower). This is a directed ordering. Whether status is a drive (as in file 55) is a separate question: the data only show the ordering structure.
- **The partition into factions** at group scale is an emergent structure; no source derives it from person-level drives. Kirkley et al. even note causality may run the other way: pre-existing factions (Montagues and Capulets) make the network balanced "by definition".
- **Caplow's coalition rule** is a function of resources (power), not drives, in everything I could see ([sa]).
- **Burt's brokerage** is positional; **Bowen's triangulation** is a clinical process claim.

Net: the *dynamic* motive (consistency, plus a counter-pull) can be written as a drive; the *objects it acts on* (signed relations) and the *laws that constrain them* (product rule, gauge invariance, status order) are a second layer that a drive basis does not generate. This matches the working-hypothesis warning that "drives as primitives" is under test: here at least a relational layer seems to be needed in addition.

---

## What does it predict or control, and how well?

**Predicted (and what the evidence is).**
- **A missing edge's sign from the other edges, at network scale (pair/triad level).** Leskovec: error 6.6% (balanced test set, chance 50%) on Epinions with 23 local features; accuracy 0.92-0.935 on Epinions/Slashdot, 0.77-0.80 on Wikipedia; on the natural ~80%-positive data, 90-95% accuracy and AUC ~95%, i.e. roughly 15 points above guessing "positive". Out-of-sample across datasets: trained on one site, tested on another with small loss (Epinions/Slashdot ~0.92-0.935). This is a *learned* triad model, not the balance rule itself. The pure balance rule, applied deterministically, does worse: 0.77 / 0.84 / 0.58 (Epinions/Slashdot/Wikipedia) against a 0.5 chance baseline, with Wikipedia barely above chance. Weak balance: 0.82 / 0.87 / 0.61. Status: 0.81 / 0.72 / 0.67.
- **A missing sign by maximising balance, in nations** (Kirkley et al.; the sign-prediction tests use the 70 international-relations networks): by NMI all four measures beat the majority-sign guess, weak balance best in most years; by accuracy weak balance "substantially outperforms" the baseline while the Estrada-Benzi measure is sometimes below it; no absolute accuracy given in the text.
- **Which triads over/under-occur** (Leskovec CHI Table 3, read in validation): the two-positive (one-negative) triangle is under-represented by about 75% (Epinions, Slashdot) and 50% (Wikipedia) against a sign-shuffled null; all-positive over-represented by about 40%. Strong balance fails at the all-negative triangle (over-represented in Epinions and Wikipedia) and does not get the enemy-of-enemy triangle consistently (over in two, under in Slashdot). Weak balance fits.
- **Global structure**: contested. Leskovec's heuristic two-way partition is no better than the trivial one-cluster partition; Facchetti's exact ground state is clearly better than trivial (frustrated fraction 7.2 / 14.8 / 14.2% vs 16.7 / 23.6 / 21.4%), though still far from zero. Status's ordering prediction is supported (79-85% vs 50%).
- **Better than random**: yes under every null tried (Facchetti Z test, Estrada-Benzi reshuffle, Kirkley et al. sign-shuffle). The effect size is large relative to the null but the networks are still 7-15% frustrated (Facchetti) or very unbalanced on a cycle-weighted index (Estrada-Benzi).

**Controlled.** Nothing in this tradition is an intervention that works with consent or by manipulation. Estrada-Benzi's "tuning balance" is a mathematical sweep over the inverse-temperature parameter on the index, not an experiment on people; I did not read the rest of that section. The one controlled element is the experimenter's imposed power in Caplow-type coalition games [sa] (a manipulation of structure inside a lab game, not of drives). Heider/C&H note an influence corollary, but it is conditional on an assumed influence law and was not tested.

**Failures.**
- **Enemy of my enemy** fails in all three online datasets in the learned-coefficient test (Leskovec WWW; read); in raw triad counts it is mixed (CHI Table 3).
- **Global faction structure** fails by Leskovec's heuristic, but not by Facchetti's exact optimum (see section 5); treat as contested.
- **Wikipedia**: public, consequential votes; every balance-based predictor drops to the 0.58-0.76 range.
- **Cross-measure disagreement**: "extremely balanced" (Facchetti) vs "very poorly balanced" (Estrada-Benzi) from the same three networks. The measures are not calibrated against any independent criterion (no outcome variable such as dispute duration, group split, or attrition).
- **Little outcome validity in the works read**: none of the six works read links balance level to a group outcome (cohesion, decision, split, efficiency) or to the drive state of a person. The "tension" Heider posits has one weak measurement here (Jordan, via C&H, hypothetical scenarios). Outside them (found in validation): Askarisichani et al. 2019 report balance "positively related to performance" in 66 day traders (abstract read; an individual performance outcome, effect size not read).
- **Dynamics not covered by the works read**: whether imbalanced triads convert to balanced ones over time, and at what rate, is the key test of the drive reading. It has been tested empirically elsewhere (Doreian & Krackhardt 2001 on Newcomb's longitudinal data [sa]; Askarisichani et al. 2019: "a propensity towards affective balance, but one unbalanced configuration resists change", abstract read), and modelled (Antal-Krapivsky-Redner 2005; Marvel et al. 2009, 2011), none opened here.
- **Effect sizes in the small-group literature** (Horowitz, Jordan, Caplow tests) are not available to me from primary text.

**Bottom line.** What exists: an exact, closed product-rule law with a clean theorem (balanced iff two-clique partition; I read C&H's statement), a strong and replicated finding that signed networks are less frustrated than shuffled-sign nulls, a good local sign predictor built on triads, and a documented failure of the totality of the rule (enemy of enemy in the learned model; all-negative triangles over-represented), with the global two-faction result contested between Leskovec's heuristic and Facchetti's exact optimum. Not found in the works read: a drive-level derivation of the rule, an intervention that changes balance in real groups, or a size-calibrated balance index. A balance-to-outcome link does exist outside them (Askarisichani et al. 2019, trader performance; abstract only), so "no predicted outcome" is a gap in this survey, not in the literature.

---

## Validation log (2026-10-30)

All ten original DOIs resolved at api.crossref.org with matching titles, authors, venues and years.

- ✓ Heider 1946, J. Psychol. 21(1) 107-112: bibliographic data confirmed; text paywalled, not read; quotes remain [read via C&H].
- ? Cartwright & Harary 1956: Crossref confirmed; content NOT re-checked (only third-party reposts of a paywalled article exist; not fetched). Section 2 quotes and Jordan's figures rest on the first pass alone. Definitions agree with the restatements in the papers read.
- ✎ Davis 1967: Crossref confirmed, not read, stays [sa]. Added Davis 1963 (AJS 68, 444-462, doi:10.1086/223401), which is the Davis paper Leskovec 2010b actually cites; quote source corrected to Leskovec 2010a.
- ✓ Caplow 1956 (first page 489 at Crossref) and Caplow 1959: confirmed; not read; [sa]. ✎ The anonymous "1967 ScienceDirect" revision identified as Chertkoff 1967; Gamson 1961, Vinacke & Arkoff 1957 and Komorita & Chertkoff 1973 added with DOIs. ? Murnighan 1978: two candidate papers, attribution unresolved.
- ✎ Leskovec et al. 2010b (WWW): read. Table 6/7 orientation confirmed from the captions (row = train, column = test); numbers in Tables 6-7 confirmed. Table 8 read: corrected "both baselines do as well or better" (permuted Slashdot does worse), added the actual values, and noted that Epinions 0.834 is below the trivial 0.85. Epinions edge count 841,200 per Tables (text 841,000).
- ✎ Leskovec et al. 2010a (CHI): read, including Table 3; triad counts and surprise values added; noted that at the triad-count level enemy-of-enemy (T1) is over-represented in two of three datasets, so "fails in all three" applies to the WWW learned-coefficient test only.
- ✎ Facchetti, Iacono & Altafini 2011: read (main text); every number in section 5 checked against Tables 1-2 and the Fig. 2 caption. Corrected the claim that Leskovec's Table 8 shows Facchetti's optimum equals the trivial partition: Facchetti's frustrated fraction (7.2/14.8/14.2%) is clearly below trivial (16.7/23.6/21.4%), so the global-faction "failure" is now marked contested.
- ✎ Estrada & Benzi 2014 (arXiv:1406.2132): read; Table 1, Heider-1958 quote, WWI and Gahuku-Gama values confirmed. Reshuffle order clarified. Added a warning that their passage misreports Leskovec's triad findings.
- ✎ Kirkley, Cantwell & Newman 2019 (arXiv:1809.05140): read the relevant sections; data descriptors and p < 0.05 claim confirmed. Corrected sign prediction: "above baseline in all years" holds for NMI, not accuracy (EB measure sometimes below baseline). Sign prediction was on the nations data only; "three or more factions" relabelled as a definitional argument.
- ✓ Chiang et al. (arXiv:1302.5145): authors confirmed from arXiv; Theorem 8 opened and matches.
- ✓ Simmel 1908, Burt 1992, Bowen 1978: no DOI; remain [sa]; nothing load-bearing rests on them.
- ✎ "Nothing exists" claims tested by search: "no small face-to-face test n > 3" was false (Kirkley's 34 students, already in this file; Doreian & Krackhardt 2001; Askarisichani et al. 2019, abstract read). "No balance-to-outcome link" and "no dynamics tested" qualified to "not in the works read". Antal-Krapivsky-Redner 2005 and Marvel et al. 2009/2011 DOIs resolved.
- ✗ No fabricated works found; nothing deleted.

Sources opened for content in this pass: 7 (Leskovec WWW, Leskovec CHI, Facchetti PNAS, Estrada-Benzi preprint, Kirkley preprint, Chiang preprint, Askarisichani abstract).

**Verdict.** The citations are real and correctly attributed, and the equations quoted from Leskovec, Facchetti, Estrada-Benzi and Kirkley match the texts. The substantive errors were in interpretation: the global two-faction result was presented as a settled failure when Facchetti's exact optimum contradicts Leskovec's heuristic; Kirkley's sign-prediction result was overstated; and "no small-group or outcome evidence" was a survey gap stated as a fact about the literature. The product rule (multiplication in Z2) can feed an equation from the readings of Leskovec, Kirkley and Estrada-Benzi. The C&H verbatim quotes are still single-reader.

## Cross-checks (2026-10-30)

Method: grep of the other files in `docs/prior-work/` for every work, author and number named in this file, and a read of the matching passages. Only this file was edited. The ledger lines were returned to the caller and not written to `docs/ledger.jsonl`. Nothing was committed.

### Agreements

- **Cartwright & Harary cycle rule** (sign of a cycle = product of line signs; balanced iff all cycles positive; digraphs by semicycles): agrees with 03 §4, 06 §Heider, and 085 §4 (Altafini uses the semicycle condition).
- **Structure theorem** (two subsets, positive inside, negative across): agrees with 03 §4 (stated there for any signed graph).
- **Davis weak balance** (forbid cycles with exactly one negative edge; clusterable): agrees with 03 §4 and 083 §2.1. Davis 1967 is not read in any of the three files.
- **Heider 1946 and Cartwright & Harary 1956 bibliography**: agrees with 03 §4 and 06 §Heider.
- **Marvel et al. 2011 DOI and "balanced complete graph = two factions"**: agrees with 083 §2.1 and 060.
- **Altafini 2012 on triads versus cycles** (balance of all triads is weaker than balance of all cycles on non-complete graphs; 085 §4, read): agrees with §2 here, including the point that the triangle form is a corollary for complete graphs.
- **Simmel's triad operators** (tertius, tertius gaudens, divide and rule): 11 §1 and §9 here agree. Both are [sa].
- **Caplow as the triad-coalition-by-power formalisation**: 11 (missing-work entry) and §8 here agree. Both are [sa].
- **Bowen triangulation as clinical theory without a validated quantitative form**: 13 §1 and §9 here agree.
- **Burt brokerage in a triad with a missing tie**: 11 and §9 here agree. Both are [sa].

### Duplicates

Marked `dup_of_file` in the ledger lines: the Heider product rule (03 §4, 06 §Heider), the C&H cycle definition (03 §4, 06), the structure theorem (03 §4), the degree of balance (03 §4), Davis weak balance (03 §4), the Leskovec triangle form (060, 083 §2.1), Caplow (11), Simmel (11), Burt (11), Bowen (13), and the Altafini comparison (085 §4).

### Contradictions (not resolved here)

1. **Enemy of enemy.** The WWW learned-coefficient test fails in all three networks. CHI Table 3 has the enemy-of-enemy triangle over-represented in Epinions and Wikipedia and under-represented in Slashdot. These are different tests. Unresolved.
2. **Estrada-Benzi's account of Leskovec's triad findings** against CHI Table 3. The validation log above already settles that Estrada-Benzi misreport Table 3. Kept open until a second reader checks it.
3. **Global two-faction partition.** Facchetti's exact ground state (frustration 7.2 / 14.8 / 14.2%, below the trivial 16.7 / 23.6 / 21.4%) against Leskovec's heuristic, which is no better than trivial. Unresolved. It touches split, so the ledger hygiene rule puts it first.
4. **Balance level.** Facchetti's "extremely balanced" against Estrada-Benzi's "very poorly balanced", on the same networks. Different measures; no independent criterion. Unresolved.
5. **Scope of the Cartwright & Harary theorem.** This file (single reader of a third-party copy) and 03 §4 say any signed graph. 06 §Heider, 060 and 083 §2.1 state it for complete graphs. Unresolved: Harary 1953 is unread.

### Corrections to be made in the sources (not contradictions)

- **§8 attributes a "six types" list to file 11.** File 11's Caplow entry (line 339) has no such list. The six-type figure comes from one search summary, so it is [sa] with no source file.
- **Antal, Krapivsky and Redner are two papers.** 083 read Physica D 224 (2006), "Social balance on networks: the dynamics of friendship and enmity", arXiv:physics/0605183. §10 here lists PRE 72, 036121 (2005), "Dynamics of social balance on networks", which is unread. Both are real; cite by DOI.
- **Heider 1946 availability.** 03 §4 gives a full-text URL (psychclassics.yorku.ca) and marks the entry verified. §1 here says Heider is paywalled and unread. Not checked here. If that URL holds the 1946 text, Heider's quotes can be read at source.
- **Gamson 1961.** 10 describes it as "proportional payoffs". §8 here cites its minimum-resource predictions. Both belong to the 1961 theory; not a conflict.
- **Caplow 1957** (organisational size) appears in 091 and not here. Not a conflict.
- **Cluster.** The batch report of 2026-10-29 assigns D207 to cluster H. `docs/research-map.md` lists D207 under section G. The ledger lines are tagged G, the map's placement. The next-pattern session should settle it.
- **Davis citation.** Leskovec 2010b (WWW) cites Davis 1963 for weak balance; 2010a (CHI) cites Davis 1967. Both papers exist, as §3 says.

## Licences of quoted and transcribed material (2026-10-30)

Tables in sections 4, 5 and 6 were reduced to prose descriptions of the values used in this audit pass. Dataset licences were not checked; only summary statistics and results are recorded here, never the data.

| Source | Licence as determined | Use in this file |
|---|---|---|
| Cartwright & Harary 1956, Psychol. Rev. 63(5), 277-293 | Not determined; publisher (APA) copyright presumed. Read from a third-party repost (sitpor.org), not the publisher's copy; confirm the repost is not a route around the paywall and cite the DOI, not the repost; re-read from a legitimate copy if in doubt | Short quotations of definitions and theorem statements in section 2; restated equations |
| Heider 1946 / 1958 | Not determined; publisher copyright presumed | Not read; mentioned, and one quotation seen inside Estrada & Benzi |
| Leskovec, Huttenlocher & Kleinberg 2010a (CHI) and 2010b (WWW), arXiv:1003.2424 | Not determined; ACM / IW3C2 copyright presumed; arXiv licence not stated | Short quotations; restated equations; Table 3 described in prose with the values used |
| Facchetti, Iacono & Altafini 2011, PNAS 108(52) | Not determined; PNAS publisher copyright presumed (free access after six months is not a CC licence). Read via a Wayback copy of the PDF; whether it was within the free window is unconfirmed | Short quotations; restated equations; results table described in prose |
| Estrada & Benzi, arXiv:1406.2132 (PRE 90, 042802) | Not determined; arXiv licence not stated; APS copyright for the published version | Short quotations; restated equations; Table 1 described in prose |
| Kirkley, Cantwell & Newman 2019 | Not determined; publisher copyright presumed | Short quotations; restated equations; summary figures |
| Askarisichani et al. 2019, Nature Communications | Not determined; believed CC BY 4.0, not verified. The trader message data is not public and is not in the repo | Abstract-level summary figures only |
| Davis 1967, Caplow 1956 / 1959 / 1968, Chertkoff 1967, Gamson 1961, Simmel 1908, Burt 1992, Bowen 1978, Doreian & Krackhardt 2001, Nordlie 1958 | Not determined; publisher copyright presumed | Citation and description only (mostly not read, [sa]); sections 8 and 9 attributed above, with a CC BY-SA 4.0 caveat for any Wikipedia-derived wording |
| Unnamed review of Bowen studies (search summary) | Not determined; unnamed | One short second-hand quotation of about 11 words in section 9 |
| SNAP datasets soc-Epinions1, soc-sign-Slashdot090221 (Leskovec et al.) | Not determined; SNAP page not checked | Dataset citation: node and edge counts, percent positive |
| SNAP wiki-Elec (Wikipedia admin elections) | Not determined; derived from Wikipedia votes (text CC BY-SA); data licence not checked | Dataset citation: summary statistics and results only |
| Facchetti's undirected versions of the same three networks | Not determined; same underlying sources as above | Dataset citation: n, m and fraction negative |
| Kirkley et al. international-relations and freshman-class networks | Not determined; underlying data sources not named in the file | Dataset citation: summary statistics and results only |
| Newcomb fraternity data (Nordlie 1958; Doreian & Krackhardt 2001) | Not determined | Mentioned only |
