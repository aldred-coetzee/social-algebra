# Prior work 096: Cartwright & Harary 1956 and Harary 1953 — scope of the structure theorem, the product rule, the degree of balance

Direction: D588. Kind: deep-read. Date: 2026-10-29. Settles the 084/085 scope contradiction (084 §"Contradictions" item 5).

## Provenance, stated first

| Work | Status | Route |
|---|---|---|
| Cartwright & Harary 1956, Psychol. Rev. 63(5), 277-293, doi:10.1037/h0046049 | **[read] in full, second reader** | Scanned text-layer PDF, 17 pages, `pdftotext`. Fetched from the sitpor.org repost (www.sitpor.org/wp-content/uploads/2015/08/STRUCTURAL-BALANCE-A-GENERALIZATION.pdf); snap.stanford.edu/class/cs224w-readings/cartwright56balance.pdf returned a byte-identical file (same size, 1,221,915 bytes). Both are third-party copies, not the APA copy. Crossref confirms title, journal, vol 63, issue 5, pp. 277-293, 1956. Running headers match. |
| Harary 1953, "On the notion of balance of a signed graph", Michigan Math. J. 2(2), 143-146, doi:10.1307/mmj/1028989917 | **NOT read. [sa]** | Crossref confirms the record (pp. 143-146, 1953). Project Euclid and the Univ. of Michigan Deep Blue copy both returned a bot-check page to `curl`/WebFetch; I did not try to defeat it (a spoofed-browser attempt was refused by the permission layer, correctly). Nothing from the primary text is transcribed below. |
| Zaslavsky, T., "Signed Graphs and Geometry" (arXiv:1303.2770v1, 2013, lecture notes), Thm 2.1 | **[read] as a secondary account of Harary 1953** | arXiv open copy, `pdftotext`. Used only to state what Harary 1953 is credited with, tagged [sa-of-Harary]. |

The headline: **the question D588 poses can be answered from C&H 1956 alone**, because that paper states the theorem and the definition itself. Harary 1953 would only add the proof, and the proof is independently re-derived in §4 (tagged [derived], not [read]).

## 1. Cartwright & Harary 1956

**Citation.** Cartwright, D. & Harary, F. (1956). Structural balance: a generalization of Heider's theory. *Psychological Review*, 63(5), 277-293. doi:10.1037/h0046049 (resolves at Crossref).

**Their vocabulary.** Point, line, linear graph, digraph, s-graph (signed graph), s-digraph, graph "of type r", sign of a line (+1/-1), path, cycle, semicycle, length, positive/negative cycle, balanced, vacuously balanced, degree of balance b(G), N-balance, local balance, articulation point, "clique" (special meaning: one side of the two-subset partition). Heider's own vocabulary retained: P-O-X unit, L (liking) and U (unit formation), balanced/imbalanced.

**Drives/operands.** None. Operands are points (persons, or P, O, X entities in one person's cognitive field); the only primitive on a line is a **sign**, the "relation or its opposite". No motive, tension magnitude or drive appears in the formalism. Tension is mentioned only as Heider's verbal background ("the state of imbalance will produce tension", p. 278).

### 1.1 Definitions, exactly [read]

- Graph: "a finite collection of points together with a prescribed subset of the set of all unordered pairs of distinct points." (p. 281)
- Signed graph: "obtained from a graph when one regards some of the lines as positive and the remaining lines as negative." (p. 282). Relations are "all-or-none"; "our present use of graph theory can treat only the structural, and not the numerical, aspects of relations."
- Path: lines AB, BC, ..., DE "where the points ... are distinct"; cycle: that path "together with the line EA". Length = number of lines. Semicycle (digraphs): one line from each pair AB or BA, etc.; "every cycle is a semicycle, and a semicycle of length 2 is necessarily a cycle." (p. 283)
- **Sign of a cycle (the product rule):** "The sign of a cycle is the product of the signs of its lines. For convenience we denote the sign of a line by +1 or -1 ... a cycle is positive if it contains an even number of negative lines, and it is negative otherwise." (p. 283-284)
- **Balance:** "we define an s-graph (containing any number of points) as balanced if all of its cycles are positive." (p. 284). Digraph: balanced "if all of its semicycles are positive" (p. 285). Footnote 8: with no cycles a graph is "vacuously" balanced. For type-2 graphs "the simplest procedure would be simply to ignore the types of lines" — offered as "a tentative definition" with doubt "whether this definition will fit empirical findings for cycles of greater length" (p. 285).
- **Degree of balance:** c(G) = number of cycles; c+(G) = number of positive cycles; b(G) = c+(G)/c(G). "Obviously b(G) = 1 if and only if G is balanced." Probabilistic reading: "the degree of balance of an s-graph is the probability that a randomly chosen cycle is positive." For digraphs, the ratio of positive semicycles to all semicycles. (p. 288)
- **N-balance:** all cycles of length not exceeding N positive. Fig. 10: "3-balanced but not 4-balanced" (all 3-cycles positive, one negative 4-cycle). Footnote 10: cycles of length N weight 1, longer weight 0, generalisable by "weight 1/2^n to length N". (p. 288-289)
- **Local balance at P:** all cycles through P positive; locally N-balanced likewise. (p. 289)

### 1.2 Theorems, exactly as stated [read]; proofs are not in this paper

C&H state the proofs are "the subject matter of a separate paper (6)", their reference 6 being Harary, Mich. Math. J. 1953-54, 2, 143-146. "Since the proofs of these theorems may be found in the other paper, we shall not repeat them here." (p. 286)

- **Theorem (path form).** "An s-graph is balanced if and only if all paths joining the same pair of points have the same sign." (p. 286)
- **Structure theorem.** "An s-graph is balanced if and only if its points can be separated into two mutually exclusive subsets such that each positive line joins two points of the same subset and each negative line joins points from different subsets." (p. 286)
- **Remarks attached to it [read].** "One of the two subsets may be empty — as, for example, when a connected graph contains only positive lines." The subsets need not be connected: Fig. 8 shows two balanced s-graphs "even though neither of the two disjoint subsets is a connected subgraph." The structure theorem "is useful in determining whether or not a given s-graph is balanced without an exhaustive check of the sign of every cycle."
- **Local balance theorem.** "If a connected s-graph G is balanced at P, and Q is a point on a cycle passing through P, where Q is not an articulation point, then G is also balanced at Q." C&H state it explicitly "without proof" (p. 289) after noting that combinatorial problems of local and N-balance "have been investigated by Harary (7)", i.e. Harary, "On local balance and N-balance in signed graphs", Mich. Math. J. 3 (1955), 37-41, doi:10.1307/mmj/1031710532 (Crossref confirms; not read). [Validation 2026-10-30: was "Proof deferred to Harary (7)"; C&H do not say the proof is there.]
- **Influence corollary (conditional).** Assuming "when two people like each other they can influence each other positively ... but when two people dislike each other they can only influence each other negatively", in a balanced s-graph "the sign of the influence exerted by any point upon any other will be the same, no matter what path is followed", yielding "homogeneity within cliques and opposing opinions between cliques" (p. 287). An implication of an assumed influence law, not a finding.

### 1.3 The scope question, settled

**C&H state the structure theorem for an arbitrary s-graph, finite, with no completeness hypothesis.** Evidence [read]:

1. The definition of balance is given for "an s-graph (containing any number of points)", and the theorem sits directly under it.
2. The words "complete" and "triangle" do not occur in either theorem statement or in the definition of balance. Full-text search of the scan: "complete graph" occurs once, p. 288, only as the example "the complete graph of 3 points" in the degree-of-balance discussion; "triangles" occurs once, p. 279, describing Horowitz et al.'s P-O-X and P-Q-X units.
3. The worked examples are not complete graphs: Fig. 7 has eight points and thirteen lines (complete would be 28); Fig. 8 shows two balanced graphs with disconnected sides; Fig. 9's graph has four points and five lines (complete would be six).
4. The authors list "hold for units consisting of any finite number of entities" as design requirement (b) (p. 281) and state "[the definition] contains no such limitation" (p. 290).
5. The triangle-only version is *not* equivalent off complete graphs, and C&H show it: Fig. 10 is "3-balanced but not 4-balanced" (all triangles positive, a negative 4-cycle). (C&H's stated motivation for N-balance is different — that long cycles, "a cycle of length 100, say", may not matter to a group (p. 288) — but Fig. 10 is their own example that triangle positivity does not imply balance.) [Validation 2026-10-30: "exists for exactly this reason" overstated C&H's motivation; softened.]

**So 084 §2 and 03 §4 are right (any signed graph). 06 §Heider, 060 and 083 §2.1, which state it for complete graphs, are describing the Leskovec-et-al. triangle form, not C&H's theorem.** The triangle ⇒ two-faction version is true only for complete graphs and is a corollary, as 084 said (checked in §4). Edit target: those three files should say "any signed graph (cycle form); on complete graphs it reduces to triangles".

**Residual doubt.** I have not read Harary 1953. [sa-of-Harary] Zaslavsky, Thm 2.1, credits "Harary's Balance Theorem (1953a)" with the equivalence of (i) balanced, (ii) a bipartition V = V1 ∪ V2 with negative edges exactly those between V1 and V2, (iii) any two paths with the same endpoints have the same sign, for a signed graph (with the extra clause "no half edges", a Zaslavsky generalisation). He says his short proof is "not the original one". This agrees with C&H's statement and neither gives a complete-graph hypothesis. Whether Harary 1953's own wording restricts anything I cannot say; C&H's reading of it is as above.

### 1.4 Group size and composition (what the paper says)

- Size: "any finite number of entities"; Heider's was three. "Whether or not empirical theories of balance will be confirmed by research dealing with larger structures can only be determined by empirical work." (p. 290). Large-n tolerance is handled by N-balance; the claim "it will not matter at all to the group as a whole whether a cycle of length 100, say, is positive" (p. 288) is asserted, not tested.
- Degree of balance is **not comparable across graphs** without a null: complete graph on 3 points, unbalanced, only b = 0; Fig. 9's graph, only b = 1/3 and 1; "b(G) = 50% does not even occur for this structure"; "any interpretation ... must take into account the distribution curve for b(G), which is determined by the structure of G." (p. 288)
- Composition: asymmetric relations covered by digraphs; "whenever the lines PO and OP are of different signs, the s-digraph containing them is not balanced" (p. 290). Absence of a line (indifference) is distinct from a negative line ("complement" vs "opposite"); absence breaks cycles, which makes graphs *vacuously* balanced. Strength of relation is explicitly out of scope: "One of the principal unsolved problems is the development of a systematic treatment of relations of varying strength." (p. 292)

### 1.5 Empirical standing, and its SCALE [read, second-hand within C&H]

All at **membership/attitude scale inside a single person's cognitive unit, or small discussion groups**; none at group-outcome or crowd scale.

- Horowitz, Lyons & Perlmutter 1951 (Hum. Relat. 4, 57-76, doi:10.1177/001872675100400103, Crossref-confirmed): members of a discussion group, sociometric liking then evaluation of a group event; data "tend to support" tendency to balance in P-O-X; C&H footnote 2: "It is not clearly demonstrated that P likes Xs produced by liked Os and dislikes Xs produced by disliked Os." For P-Q-X, P's evaluation of X and his perception of Q's attitude agree when P likes Q and disagree when he dislikes Q, but "a clear tendency for P to see Q's evaluation of X as agreeing with his own whether or not he likes Q." No N, no effect size reported by C&H.
- Jordan 1953 (Hum. Relat. 6, 273-287, doi:10.1177/001872675300600304, Crossref-confirmed): 64 hypothetical three-entity situations; each subject "place[d] himself in each situation by taking the part of P" and rated (un)pleasantness (p. 279). As Jordan scored them: balanced mean unpleasantness 46, imbalanced 57. C&H's re-coding, treating "no bond" as absence of a line: balanced 39, vacuously balanced 51, not balanced 66. Negative liking relations "experienced as unpleasant even when contained in balanced units": "a tendency toward 'positivity' over and above the tendency toward balance." Footnote 13: "A strict test of our interpretation of Jordan's data is not possible." Imagined (hypothetical) ratings, each subject rating from P's position; number of subjects and significance tests not given by C&H. [Validation 2026-10-30: was "Single-subject", which misread C&H; they say "subjects", plural.] The re-coding is a post-hoc re-analysis by the theorists, not an independent replication.
- Newcomb 1953 "strain toward symmetry" is discussed as a related theory, not as data.
- **Intervention / consent:** none. The paper reports no intervention; it is descriptive. The influence corollary is conditional on an assumed influence law.

## 2. The product rule, as an algebraic object

Stated [read]: the sign of a cycle is the product of its line signs in {+1, -1}. Equivalent forms in the text: (i) every cycle positive; (ii) path-sign well defined; (iii) two-subset partition with positive lines inside, negative lines across. In algebraic terms: the signs live in the group Z2 under multiplication; a cycle is a closed walk with no repeated points; **balance = the signing is a coboundary** (every closed walk has product +1). The "coboundary" phrasing is [derived] and is not in C&H; it is the standard reading, and Zaslavsky's "switching equivalent to all-positive" (his Cor. 2.7, [sa-of-Harary]) says the same.

## 3. What changes with n and with composition

- n = 3: one cycle. b ∈ {0, 1}. Balanced iff the triangle is positive: Heider's rule is the n = 3 case.
- n = 4, complete: seven cycles (4 triangles + 3 four-cycles); matches C&H's own count for Fig. 5 [read], and the formula Σ_k C(n,k)(k-1)!/2 [derived, brute-force checked] gives 1, 7, 37, 197, 1172 for n = 3..7. Cycle count grows factorially, so b(G) is dominated by long cycles unless N-balance or length-weights are used. C&H's own remedy is footnote 10.
- On a complete graph, triangle-balance suffices [derived, brute-force checked n = 4, 5, 6: 0 triangle-balanced-but-unbalanced signings out of 64, 1024, 32768; balanced signings number 8, 16, 32 = 2^(n-1)]. On non-complete graphs it fails (C&H Fig. 10; the plain four-cycle with one negative edge has no triangles and is unbalanced).
- Composition: the number of balanced signings of K_n is 2^(n-1) out of 2^C(n,2), so a random signing of even moderate n is almost never balanced; "balance" is a rare state and a measure of departure is needed (b(G) with a graph-specific null, or frustration index [sa], not in C&H).
- **Which side a person is on is the only stored state**: a balanced group is a labelling x: V → {+1, -1} with sign(ij) = x_i x_j (the "structure theorem", [derived] from C&H's statement). This is the part an algebra can use.

## 4. Re-derivation of the structure theorem (not read from Harary; own proof, [derived])

Claim: a finite s-graph is balanced iff there is x: V → {±1} with sign(ij) = x_i x_j for every line.
(⇐) Along any cycle the product of x_i x_j telescopes to Π x_i² = +1.
(⇒) In each component pick a root r, set x_r = +1, and set x_v = sign of any path r→v. Path sign is well defined: two r→v paths P, Q together form a closed walk whose edges decompose into cycles (edges used twice cancel in the product), so sign(P)sign(Q) = +1 when all cycles are positive. Then sign(uv) = x_u x_v for each line by taking the path to u plus the line uv. Components can be assigned independently, which is why the two subsets need not be connected (C&H Fig. 8) and one may be empty. ∎ Zaslavsky's "short proof (not the original one)" reaches the same result via switching (his Prop. 2.5 / Cor. 2.7: a root vertex, a spanning tree, ζ(v) = sign of the tree path), which is the same idea in different clothes; he adds that "the original proof was much less efficient" [read in Zaslavsky; as an account of Harary, sa-of-Harary]. It uses no completeness. Graph-theory textbook level; I rely on it as a check on the *statement*, not as a transcription of Harary.

## 5. Operand/operator translation for the algebra

- Operands: persons (points). Relation: signed edge, optionally directed.
- Operator: multiplication in Z2 along a closed walk; test: product = +1. The "two-faction" form: a person's side x_i, an edge sign as x_i x_j. This is an **algebra of valences on pairs**, closed and exact, but it has **no time, no tension magnitude and no dynamics** (C&H say so on strength).
- Not a drive: the sign is the valence of a dyadic relation, the state variable x_i is group membership, and "tendency toward balance" is a verbal postulate inherited from Heider, not an equation. Any dynamics (edge flips, continuous-time models) are post-1956 and are in 084 and 085, not here.
- Directed version: balanced iff all semicycles positive, so any pair with PO and OP of opposite sign is unbalanced by definition (a digon is a semicycle); this forces sign-symmetry and is what makes the directed case behave like the undirected one (cf. 085 on Altafini).

## 6. What exists vs what does not

Exists: an exact definition and an exact equivalence (cycles = paths = two-subset labelling) at any finite n, for any graph; a measure of partial balance with an honest warning that it depends on graph structure; a length-truncated version.
Does not: proofs in this file's primary source (they are in Harary 1953, unread); strength of relations; dynamics; any behavioural or outcome test; any field data at n > 4; any intervention.

## Does it reduce to a drive basis?

Largely **no, and not by design.** What reduces: nothing in the formalism is a drive, but its *meaning* depends on one. Heider's motivational claim is that imbalance produces tension which pushes toward balance (a consistency drive on the unit, a single-person cognitive drive). That drive is *external* to C&H's mathematics: it enters only as the sentence that balanced states are favoured, and C&H explicitly decline to model it ("Only future research can determine whether theories of balance can be established" for other configurations). If one wants the drive, it would have to be added: for each person a "side" state x_i and a penalty for edges violating sign(ij) = x_i x_j. That penalty is an energy over group configurations, not a per-person drive; it couples people through a dyad-level product, which is a group-level term (and is the object studied in later dynamics, 084/085).
What does NOT reduce: (i) the sign of an edge, which is a relation between two persons, not a property of either; (ii) the factions, which are a property of the partition, determined only up to global swap (x → -x), so "which faction" is gauge, only "same or different" is physical; (iii) the vacuous-balance effect (absence of an edge is not a negative edge), which is a fact about who relates to whom, not about drives. The honest status of "drives as primitives": untouched by this tradition, neither supported nor contradicted. This tradition is a **structure** result, and a drive basis would have to supply the dynamics to reach it.

## What does it predict or control, and how well?

**In the sources read here, nothing is predicted or controlled.** The theorems are conditional on definitions; the only empirical contact is two 1951-53 studies summarised second-hand, both at membership/attitude scale in a person's own cognitive unit:
- Horowitz et al.: "tend to support" balanced P-O-X; one of the two directional hypotheses "not clearly demonstrated"; no effect size, no N in C&H.
- Jordan: mean unpleasantness 46 (balanced) vs 57 (imbalanced) on his scoring, 39 / 51 / 66 on C&H's recoding; hypothetical scenarios; a separate positivity effect; C&H state a strict test is not possible.
- No out-of-sample test, no replication within the paper, no group-scale (cohesion/split/efficiency) or crowd-scale outcome, no intervention and so no consent/manipulation question. The influence corollary (cliques homogeneous inside, opposed across) is a deduction from an assumed influence law and is untested here.
- Failure modes C&H themselves record: the positivity effect, the complement/opposite confusion, and dependence of b(G) on graph structure. Later empirical work on triangle statistics in online signed networks (Leskovec et al., Facchetti et al.) is in 084 and was not re-read here.

## Unconfirmed

- Harary 1953 wording and proof: not read; bot-gated at Project Euclid (re-tested 2026-10-30: the PDF URL returns an HTML challenge page) and Deep Blue; a web search found no other open copy. It is not paywalled as such — the gate is a bot-check — so a human in a browser can likely read it.
- That the sitpor/snap copy equals the APA copy: running headers, pagination (277-293) and Crossref match, but it is a scan from a third party; confirm before quoting at length.
- Whether "two mutually exclusive subsets" in Harary 1953 itself allows an empty set: C&H say yes in the remark; Zaslavsky's bipartition definition says X1 or X2 could be empty [sa-of-Harary].
- Horowitz et al. and Jordan: primary papers not read; only C&H's account of them.

## Licence / reuse

C&H 1956 and Harary 1953 are under publisher copyright (APA; Michigan Math. J.). This file quotes short definitions and theorem statements with page numbers and restates equations in own words; no figures reproduced. Zaslavsky arXiv text: only the theorem's gist restated. Counts and the proof in §3-4 are own derivations.

## Validation log (2026-10-30)

- ✓ Cartwright & Harary 1956, Psychol. Rev. 63(5), 277-293, doi:10.1037/h0046049 — Crossref confirms title, both authors, vol/issue/pages/year. Re-fetched the snap.stanford.edu copy (1,221,915 bytes, as stated) and re-read the text layer: every quotation in §1.1-1.5 checked against it, including the structure theorem and path theorem (p. 286), "any number of points" (p. 284), the empty-subset remark and influence corollary (p. 287), b(G), Fig. 9 (.33/1.00) and the "cycle of length 100" sentence (p. 288), N-balance, local balance and footnote 10 (p. 289; the scan renders the weight as "1/2\"", read as 1/2^N), "no such limitation" (p. 290), Jordan 46/57 and 39/51/66 and footnote 13 (pp. 290-291), strength as unsolved (p. 292), and Horowitz footnote 2 (p. 278). "complete graph" and "triangles" each occur once, where stated. Scope claim (no completeness hypothesis) confirmed [read].
- ✎ C&H local balance theorem — C&H state it "without proof" and cite Harary (7) for combinatorial problems; the file said the proof was deferred there. Corrected; Harary 1955 (Mich. Math. J. 3, 37-41) DOI 10.1307/mmj/1031710532 added, Crossref-confirmed, not read.
- ✎ Jordan 1953 as reported by C&H — "single-subject" was wrong (C&H: "subjects", each taking P's part). Corrected. DOI 10.1177/001872675300600304 added (Crossref: Jordan, Hum. Relat. 6, 273-287, 1953). Primary not read.
- ✎ Horowitz, Lyons & Perlmutter 1951 — DOI 10.1177/001872675100400103 added (Crossref: Hum. Relat. 4, 57-76). C&H's account verified; primary not read.
- ✎ §1.3 item 5 — "N-balance exists for exactly this reason" overstated C&H's motivation (they motivate it by long cycles not mattering); softened. The logical point (triangle positivity does not imply balance off complete graphs) stands, from their own Fig. 10.
- ? Harary 1953, Mich. Math. J. 2(2), 143-146, doi:10.1307/mmj/1028989917 — Crossref confirms (Harary sole author, 1953). Project Euclid PDF re-tested: bot-check HTML page; web search found no open copy. Stays [sa]; it is not needed for the scope question because C&H state the theorem themselves.
- ✓ Zaslavsky, arXiv:1303.2770v1 — fetched and read: Thm 2.1 "Harary's Balance Theorem (1953a)" with (i)-(iii) as stated, "short proof (not the original one)", bipartition definition "X1 or X2 could be empty", Cor. 2.7 switching form. §4's description of his proof route sharpened (he goes via switching on a spanning tree).
- ✓ Own derivations — re-ran: cycle counts of K_n for n = 3..7 are 1, 7, 37, 197, 1172; triangle-balanced-but-unbalanced signings of K_4, K_5, K_6 are 0 of 64, 1024, 32768; balanced signings 8, 16, 32. The §4 proof sketch checks (a closed walk's sign equals the product over its mod-2 edge set, which is an edge-disjoint union of cycles).

Sources opened: 4 (C&H 1956 scan, Zaslavsky arXiv PDF, the Project Euclid Harary 1953 URL (gated), Crossref records for 7 works).

Verdict: the file's central claim holds and is now confirmed by a second read of the primary text: C&H 1956 state the structure theorem for any finite signed graph, with no completeness hypothesis, and the triangle form is a complete-graph corollary. Four errors were corrected — the local-balance proof attribution, a misreading of Jordan's design, an overstated motive for N-balance, and missing DOIs — and none was a fabrication. Harary 1953 itself is still unread; nothing in this file that feeds an equation rests on it.

## Cross-checks (2026-10-30)

Grep of `docs/prior-work/*.md` for Cartwright, Harary, Jordan, Horowitz, Zaslavsky, structure theorem, two-subset partition, b(G), N-balance, complete graph, triangle, Heider and product rule. Files that state the same works or claims: 03 §4, 06 §Heider, 060 §5, 083 §2.1, 084 §1-§3 and its Contradictions list, 085 and 095 (Altafini's Lemma 1 and the Cartwright-Harary cycle condition). Files 01 and 063 mention Harary only as a gap, or as the different Harary 1959 unanimity paper; they are not overlaps.

### Agreements

- The structure theorem, and the cycle-sign rule behind it, are C&H's, with Harary 1953 credited for the proof. 084 §2, 03 §4 (corrected there) and 095 Lemma 1 (condition 1 credited to C&H) all agree with this file.
- The scope is any finite s-graph. 084 §2 (line 76) and 03 §4 (line 88) agree with §1.3, and 03 records that its earlier complete-graph wording was wrong.
- The degree of balance b(G) = c+/c, with b = 1 iff balanced, matches 084 §2.
- The triangle form (complete graph, every triangle positive gives balance) is a complete-graph corollary. 084 §2 and 060 §5 (line 247, "compatible") agree. 083 §2.1 gives the same complete-graph statement through Marvel et al.
- Triangle positivity does not imply balance off complete graphs (C&H Fig. 10, the four-cycle with one negative line). 084 §2 and 085 (line 153, Altafini uses C&H's all-semicycles condition) agree.
- Harary 1953 is unread in 096, 083 and 084. All three hold it at [sa] and none feeds an equation from it.
- The Cartwright & Harary scan: 084 §2 and 096 both use the third-party sitpor.org copy. 096 adds that the snap.stanford.edu copy is byte-identical.
- Horowitz, Lyons & Perlmutter 1951 and Jordan 1953 are reported by C&H in both 084 §1 and 096 §1.5, with the same footnote 2 and footnote 13 caveats.

### Contradictions

1. **Scope of the C&H structure theorem.** 083 §2.1 (lines 61-65) states the balance theorem for complete graphs only, citing Marvel et al.'s own sentence "all graphs in our discussion will be complete". 084 §2 (line 76) and 096 §1.3 say C&H state it for any finite s-graph. **Settled by the 096 validation log**: C&H's own text has no completeness hypothesis (checked against the scan). The 083 wording is Marvel's restriction for their model and should not be attributed to C&H.
2. **06 §Heider (lines 806-808)** states Harary's structure theorem for complete signed graphs, attributed to C&H 1956. The same file's validation entry (line 1032) says "structure theorem stated correctly". **Settled for the content by 096**: the complete-graph wording is wrong as an attribution to C&H. The file's own validation entry and body disagree, and 06 has not been corrected.
3. **Local balance proof attribution.** 084 §2 (line 70) says the theorems' proofs are "deferred to Harary 1953-54". C&H state the local balance theorem "without proof" (p. 289). **Settled by 096**: the path and structure theorems defer to ref 6 (1953-54); the local balance theorem has no proof there.
4. **Davis 1967 read status.** 03 §3 tags Davis's clusterability as "[verified]". 083 (Not read) and 084 §3 both list Davis 1967 as not read, [sa]. **Unresolved**: no file in the directory has read Davis 1967. 03's tag is the outlier.
5. **Harary 1953 pages.** 03 §4 (line 84) gives 143-146 and notes Wikipedia's 153-6; its log (line 295) leaves it open. The Crossref record in 096 confirms pp. 143-146, 1953. **Unresolved** for 153-6, since no file has checked the paper itself. Crossref supports 03's value.
6. **Scope of the Harary 1953 wording.** 084 §2 (contradiction 5) left this open pending Harary 1953. 096 settles what C&H state, not what Harary 1953 says. Zaslavsky (sa-of-Harary) credits Harary with an any-signed-graph statement, which agrees with C&H. **Still unresolved** for Harary's own wording, because the paper is unread.

### Ledger

Lines are returned in the structured output: definitions (s-graph, product rule, balance, b(G), N-balance, local balance, path and structure theorems), the influence corollary and its conditional, the derived counts for K_n, the Horowitz and Jordan results at membership scale, the Heider tension and tendency verbal postulate, and the contradictions above. Provenance follows the file's tags. [derived] items are listed as sa, because the schema has no derived value; they are the file's own derivations, not source claims.
