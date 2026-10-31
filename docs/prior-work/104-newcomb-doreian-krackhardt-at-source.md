# Prior work 104: the Newcomb fraternity data and Doreian & Krackhardt (2001) at source

Direction: D596 ("Newcomb data and Doreian & Krackhardt at source")

Date: 2026-10-31. Kind: deep-read plus data-location survey. Question: can the n = 3 refutation test in `models/00-v0.md` section 7 (one-negative triangle under-represented against a sign-shuffled null, and converting to balance faster than the all-negative triangle) be run on the Newcomb fraternity data, and what do the people who analysed it as signed triples actually report? Closes the gap file 102 left (D&K read only through one secondary account, ledger L4286, L4445 [sa]).

**Provenance rule.** [read] = I read the primary text this session. [sa] = secondary account. [fig] = a value read off a plotted figure by eye, so approximate. Nothing [sa] or [fig] should be treated as a measurement without a re-computation from the data.

## 0. What was read, and by what route

Both papers are **author-hosted free copies**. Patrick Doreian's own site (patrickdoreian.com/research/signed-networks/, "Download the Research Paper" links, uploaded 2017-12) serves the PDFs publicly over HTTP with no login, paywall or access control. The publisher's own copy (Taylor & Francis) is paywalled and answers 403; Unpaywall still says `is_oa: false`, so **it does not know of this copy**. Nothing was circumvented; the files are scanned page images (no text layer), so I read them page by page as images.

| Work | Status | Route |
|---|---|---|
| Doreian & Krackhardt (2001), "Pre-transitive balance mechanisms for signed networks", *J. Math. Sociol.* 25(1), 43-67, doi:10.1080/0022250X.2001.9990244 (Crossref-confirmed again today: authors Doreian, Krackhardt; vol 25 issue 1 pp 43-67) | **read in full**, all 25 pages including Tables 1-5, Figures 1-2 and the references | `patrickdoreian.com/wp-content/uploads/2017/12/2001-Doreian-Krack-Pre-Transmitive-Balance-Mechanisms-for-Signed-Networks.pdf` |
| Doreian, Kapuscinski, Krackhardt & Szczypula (1996), "A brief history of balance through time", *J. Math. Sociol.* 21(1-2), 113-131, doi:10.1080/0022250X.1996.9990176 (Crossref-confirmed: those four authors, vol 21 issue 1-2, pp 113-131) | **read in full**, all 19 pages | `patrickdoreian.com/wp-content/uploads/2017/12/history-of-balance.pdf` |

**Correction to the brief.** The direction named "Doreian et al. 1996 ... (Social Networks 18)". Social Networks 18 is a different paper, Doreian & Mrvar (1996), "A partitioning approach to structural balance", *Social Networks* 18: 149-168, doi:10.1016/0378-8733(95)00259-6 (Crossref-confirmed), which both papers above cite and which supplies the partitioning method. "A brief history of balance through time" is *Journal of Mathematical Sociology* 21. D&M 1996 itself was **not read**; its method is described in the 1996 history paper, which is what I transcribe. Doreian & Mrvar's later blockmodel-style work on international relations (2015, file 102, already opened) is about alliances, not Newcomb, and reports no Newcomb numbers beyond the one-paragraph D&K summary.

**Licence of what is transcribed.** Both papers are (c) 2001 / 1996 OPA, "published under licence by Gordon and Breach"; copyright is not waived by the author hosting. This file therefore restates definitions and equations in my own words, gives numbers (facts) with page references, quotes only a few words, and **describes rather than transcribes** the tables and figures. Table 4 (the two 17x17 partition matrices), Table 5 (receipt counts per actor per week) and Figures 1-2 (the per-type trajectories) are described, not reproduced.

## 1. The Newcomb data as D&K and the 1996 paper describe it [read]

- **Source study.** Newcomb (1961), *The Acquaintance Process* (Holt, Rinehart and Winston); the rank data as recorded by Nordlie (1958), *A longitudinal study of interpersonal attraction in a natural group setting*, PhD thesis, University of Michigan (unpublished, no DOI). The 1996 paper (p. 114) says the data "are distributed as a part of UCINET".
- **Design.** 17 actors, a "pseudo-fraternity" of strangers housed together; 15 sociomatrices over a 15-week semester (D&K p. 44; 1996 p. 116), collected at weekly intervals "with one exception" (1996 p. 117). In each, every actor ranks the other 16 for affect, a forced rank 1 to 16. The 1996 paper (p. 121, main text) reports that, in Nordlie's collection procedure, members sorted the others into piles including a "dislike" pile, with a bias against using it: seldom more than three negative nominations per person; fn 8 adds that Nordlie reports often only one or two. Nordlie calls those receiving the bottom three nominations "unpopular".
- **At one point there is a two-week gap** between adjacent observations; 1996 fn 11 (p. 124) says "We ignored this." So the authors count **14 transitions across 15 waves**. The original UCINET listing (section 5) names the matrices NEWC0-NEWC15 except NEWC9, so the gap is calendar week 8 to week 10, and D&K's "week 1 ... week 15" are observation indices, not calendar weeks [inference from the listing; D&K do not state the mapping].
- **Actor attributes are lost** for these data (room-mates, floors, etc.), D&K say repeatedly (pp. 46, 56, 65).

## 2. How signs were derived: a modelling choice, made by the authors [read]

This matters for the n = 3 test, because the brief's "explicit signs" do not exist in this dataset.

- **Recoding used in both papers:** ranks 1-4 become +1 (L, "likes"), ranks 14-16 become -1 (D, "dislikes"), ranks 5-13 become 0 (null). So every actor sends exactly **4 positive, 3 negative, 9 null** ties in every wave, by construction (D&K p. 45, p. 49; 1996 p. 120-121).
- **Why 4 and 3.** (a) For reciprocity, the 1996 paper searched for weights on ranks that maximise reciprocity relative to chance and found the optimum gives weight 15 to ranks 1-4 and 0 to ranks 5-16 (1996 Table 1, p. 121; ranks 1 and 16 were anchors at 15 and 0, not optimised, p. 118), "without loss of generality" a 1/0 coding with four 1s; (b) for the negative end, Nordlie's report that at most three negatives were typically named. Footnote 9 (1996, p. 121): the qualitative results also hold for top 3 / bottom 3 and top 3 / bottom 2.
- **Consequences stated by the authors.** Fixed out-degree of each sign per actor means the per-wave count of positive ties is always 68 and of negative ties always 51 (D&K p. 61, 51 negative ties). D&K themselves call the recoding "a major data problem" (p. 64): a man ranking 16 others cannot be told from his ranks alone to dislike all of them or merely like none; "It would be far better if we had explicit evidence for positive and negative ties rather than use a recoding of ranks" (p. 64). Their closing demand is that future data collection record negative ties explicitly (p. 66).
- **For this repo:** the sign is *derived*, the derivation is the authors' modelling choice, and a different cut (top 3 / bottom 3, or bottom 3 only as negatives) is a legitimate sensitivity check. Absence is **not** coded negative here, unlike Askarisichani (file 102): null ties are a third state. That repairs the main objection (L4429) to using the Askarisichani firm as the n = 3 test.

## 3. Doreian & Krackhardt 2001: what was actually done [read]

### 3.1 Objects counted: ordered triples, not triangles

The unit is the **triple (i, j, k)**: ordered, directed, signed ties i->j and j->k, the "pre-transitive condition", and the completion tie i->k (D&K p. 44, 48). Label each of the three ties L (+) or D (-); eight triple types by tie sign order, written (i->j)(j->k)(i->k). Balance column in their Table 1 (stated in my words): a triple is Heider-balanced when the product of the three signs is positive, i.e. an even number of D. That gives balanced LLL, LDD, DLD, DDL; imbalanced LLD, LDL, DLL; and DDD (three negatives) is **imbalanced under Heider's 2-balance but balanced under Davis's k-balance**, which they mark "yes/no" (p. 48 writes "k ≥ 2", pp. 55, 56, 64 write "k > 2"; an all-negative triple needs three plus-sets, so k ≥ 3 is the operative reading). Triples are counted over **all** (i, j, k), not conditioned to be independent (fn 8, p. 49); they note the triples are not independent.

Mapping to v0's undirected triangle types: one-negative triangle = {LLD, LDL, DLL}; all-negative = DDD; two-negative = {LDD, DLD, DDL}; all-positive = LLL. The mapping loses the direction of the missing completion, and D&K show the direction matters (section 3.3).

### 3.2 The null model: the shuffle the n = 3 test names [read]

D&K p. 49 and p. 51. They "simulated" the construction of triples **10,000** times (p. 49; the text does not say "per wave" in so many words, but Figure 1 gives a p(obs > random) for every week, so a per-wave comparison is implied): random sociomatrices in which each actor's 16 ranks are assigned to the 16 other actors at random, then recoded top 4 = +1, bottom 3 = -1, rest 0 (so each actor keeps exactly 4 L and 3 D out-ties; "fixed out-degrees for both positive and negative ties"). Triple-type counts from the same recoding are compared with the simulated counts, and the statistic is **p(obs > random)**: the share of the 10,000 draws in which the observed count of a type exceeds the simulated count. At alpha = .05 they call a count significant when it exceeds the simulated count in more than 9,500 or fewer than 500 of the draws (p. 51), i.e. above 0.95 significantly **more** than chance, below 0.05 significantly **fewer**. This **is** a row-wise sign-shuffle null with the degree-sign margins held; the Askarisichani degree-preserving null (file 102) was not. D&K's footnote 9 concedes a null that also preserves received ties (popularity) was not used.

For the conditional completion probability they define: given a pre-transitive condition (a fixed pair of signs for i->j, j->k), p_bal = d / (b + d) where d counts completions making the triple balanced and b counts completions inconsistent with balance. They compare it with the chance expectation EV (Table 2, p. 52): with N_L = 4 positive and N_D = 3 negative out-ties per actor among N_A = 16 others, the chance probability that i->k is L given i->j is L is (N_L - 1)/(N_A - 1) = 3/15; given i->j is D, N_L/(N_A - 1) = 4/15; D given L is N_D/(N_A - 1) = 3/15; D given D is (N_D - 1)/(N_A - 1) = 2/15. Their plotted statistic is delta = p_bal - EV (Figure 2).

### 3.3 Reported results, by triple type, over 15 weeks

Numbers below marked [fig] are read by eye from D&K's Figures 1 and 2 as described in their text (pp. 50-55); only the text-stated numbers are exact.

**Figure 1 (p(obs > random)), stated in the text, p. 51:**

| Type | Heider status | Trajectory (text, p. 51) | Supports balance? |
|---|---|---|---|
| LLL | balanced | 1.0 at week 1 and never departs | supports (weak form: always present) |
| LDD | balanced | slightly below 0.9 at week 1, 1.0 from week 2 | supports |
| LDL | imbalanced | starts at 0.0 and stays | supports |
| LLD | imbalanced | very close to 0, significant at outset, 0 from week 2 | supports |
| DLL | imbalanced | about 0.5 (not significant), spike at week 3, then towards 1.0; always more than chance from week 6 on | **contradicts** |
| DDD | imbalanced (2-bal); balanced (k-bal) | much higher start, reaches 1.0 at week 5, before DLL does | contradicts for 2-balance; supports for k-balance |
| DLD | balanced | proportion moves to zero; fewer than chance, significant from week 5 | **contradicts** |
| DDL | balanced | slightly above 0 at the start (already significant), "departs dramatically from 0 in week 2", then to zero; fewer than chance, significant from week 5 | **contradicts** |

Authors' own summary of Figure 1: "all of the trajectories reach the extreme values of 1 or 0 well before the end of the study period", with the dynamics "essentially over by weeks 5 or 6" (pp. 51-52). So **by wave 5 or 6 each triple type is either always above or always below its shuffled null, and does not change afterwards**.

**Figure 2 (delta = p_bal - EV) and p_bal, p. 54, text only:**
- LLL: delta starts just above 0.1, ends slightly below 0.2; p_bal about 0.3-0.4 [fig/text]. A small increase.
- LDD: delta from about 0.0 to about 0.5; p_bal from just above 0.2 to close to 0.7 [text]. Unequivocal rise; this is the main balanced mover.
- DDL: delta from just above -0.1, diminishing; p_bal from 0.2 to 0.1. DLD: delta ends below -0.1, p_bal slightly above 0.
- LLD: delta from about -0.05 to about -0.2; p_bal from 0.15 to 0. LDL: delta from just above -0.1 to about -0.2; p_bal from just above 0.1 to close to 0.
- DLL (imbalanced, contradicts): delta from about 0 to just above 0.1; p_bal from slightly below 0.3 to slightly under 0.4.
- DDD (imbalanced under 2-balance, contradicts): delta from just above 0 to below 0.4; p_bal from just above 0.3 to below 0.7.
- Authors' tally (p. 55, 56, Table 3): of the four Heider-balanced types two (LLL weakly, LDD) increase and two (DLD, DDL) decrease; of the three Heider-imbalanced types (excluding DDD) two (LLD, LDL) decrease and one (DLL) increases; DDD increases. Net: "overall, the change in the incidence in triples consistent with the FSBH is larger than the change in the triples inconsistent with the FSBH", so the aggregate rise in balance is a **net change over offsetting mechanisms**, not a uniform tendency.

**The empirical regularity D&K extract (p. 56-57), stated by them as three claims:** (1) for all triple types whose **first** tie i->j is positive, balance theory is supported; (2) "if the LLL triple is defined as balanced" there is additional strong support for the Davis version (so printed, p. 57; LLL is balanced under every definition, so this is almost certainly a misprint for DDD); (3) for the types whose first tie is **negative**, balance theory is contradicted. Their reading of the sign of the first tie as the driver is explicitly called "interesting", not proved.

### 3.4 The mechanisms they propose (the "pre-transitive" mechanisms) [read]

1. **Balance / signed transitivity with the first tie doing the work.** Rapoport's four aphorisms: "friend of a friend is a friend" and "enemy of a friend is an enemy" are supported in the data (first tie positive: i likes j, so j's friend is i's friend, and j's enemy is i's enemy); "friend of an enemy is an enemy" and "enemy of an enemy is a friend" are **not** (pp. 57, 60).
2. **Competition for k (rivalry).** Where i dislikes j and j likes k, if i is also inclined to like k then i and j are rivals for k's attention; "the balance mechanism of i disliking k ... is dominated by a competition mechanism" (p. 57). This accounts for DLL rising and DLD falling.
3. **Differential popularity and differential unpopularity (attribute recognition).** Some actors k have attributes recognised in the same way by many others, so i and j agree on k regardless of whether they like each other (p. 60, p. 64); in the data the triples with high or rising p_bal are those where i and j agree in their ties to k (both like or both dislike). This mimics balance and is non-structural; the authors extend the Feld and Elmore (1982, *Social Psychology Quarterly* 45: 77-85, doi:10.2307/3033928, Crossref-confirmed) result (popularity inequality can generate apparent transitivity) to signed networks.
4. **Macro-structure (plus-sets) constraining ties.** At least three mutually hostile plus-sets forces many DDD triples (Davis k-balance); the final partition (D&K Table 4 lower panel, reproducing 1996 Table 3) is 4 clusters: one large plus-set of 13, singletons {C} and {J}, and the dyad {O, P} (1996 p. 125 and fn 15; under k = 2, {C, J, O, P} form the second plus-set), with the large set sending virtually all its negatives to {C, J, O, P} (D&K p. 62).

They do **not** give a coupling law between mechanisms: "We do not know how to formally specify the coupling of a structural balance mechanism with a joint recognition of attributes mechanism" (p. 65). They write that balance "might not be the dominant story" (p. 65), that disentangling the mechanisms lies outside the study's scope given the data (p. 65), and that without data on positive and negative ties and on attributes it "is impossible" (p. 66).

### 3.5 The popularity/unpopularity numbers [read, text only]

Received negative ties (D&K section 4.3, pp. 61-62): per wave there are 51 negative ties in total. At week 1 received negatives range from 0 to 8 per actor; actors L and Q receive none in any wave; D received at most one from week 2; actor J ends "disliked by everyone" (16 of 16 by the last week; 8 at week 2, 11 by week 4); P went from 2 to 12; C reached 9 by week 7. In week 12, actors C, J, O and P together received 43 of the 51 negative choices, and none of them received more than one positive. At the final wave the **three** actors J, P and C received 37 of the 51 (p. 61); O, who received 9 in weeks 11 and 12, is not in that 37. Actor H received the most negatives at week 1 (8) and fell "dramatically" after week 5; A and N each started with 5. The authors read this as polarisation: a few actors become consensus-disliked while most receive none.

## 4. The 1996 paper: reciprocity, transitivity and balance over the 15 waves [read]

Same data and the same top-4 / bottom-3 recoding. Methods: reciprocity (a count of reciprocated ties; null by 1000 random permutations of the observed matrix, Hubert's method), transitivity (count of triples not violating the ultrametric transitive condition d_ik <= max(d_ij, d_jk) + 1, same permutation null), and group balance (the imbalance index I_b = positive ties between plus-sets + negative ties within plus-sets, minimised by the Doreian-Mrvar partitioning for k plus-sets).

**Reported results (text numbers exact; plotted values [fig]):**
- **Reciprocity.** Reciprocated ties per wave range from about 30 to about 36 of a possible maximum of 68 (text: "range from 30 to 35"; the plot reaches 36 in weeks 3-5 and 10) [fig]; null median about 17, 95th percentile about 23, 99th about 25 (text). Significantly above chance in every wave; "little discernible trend either up or down" (p. 123). Reciprocity is "established early in the process", already near maximum in week 1, whereas Newcomb said week 3.
- **Transitivity.** Count of non-violating triples rises from about 3050 at week 1 to about 3250 by week 8-9, then plateaus (levels off through the remaining weeks) [fig]; not significant at 5% through week 2, "barely" reaches the 1% level in week 3, clearly above null thereafter (p. 124).
- **Tie turnover (the nearest thing to a transition rate).** Of 14 transitions, the percentage of dyadic ties that changed state (including to and from null) is "slightly above 30%" at the first transition and falls over about the next seven weeks, then holds steady with perhaps a mild rise (p. 124-125). The percent stable rises over the first 8 transitions for positive, null and negative ties alike, then is stable (Figure 3 panels, smoothed) [fig: stability roughly 60-70% for the first transition, roughly 80-90% later; negative ties least stable]. No transition matrix between tie states or between triple types is printed.
- **Imbalance I_b.** Both the k = 2 ("structural") and best-k ("generalised") measures fall across the 15 weeks, not strictly monotonically; plotted (Figure 3, lower left, p. 126) from about 17 at week 1 to about 13 at week 15 for k = 2, and from about 15 to about 10 for generalised [fig]. Text: balance is "clearly supported" for generalised balance (k > 2); less clear for k = 2 and not strictly monotone; the smoothed curves are "unequivocal" for generalised balance (p. 125). First time point: partition into 3 clusters, Table 2 header "Error Score: 15" (p. 127), but the text (p. 125) gives Σ_n = 5 and Σ_p = 15, which sum to 20 under the equal weighting the paper states (p. 120); the source is internally inconsistent and the true first-wave I_b needs recomputing. Last time point: 4 clusters, error score 10 (Table 3). The final structure: by the seventh time point the structure is close to final, and over the last 6 periods C, J, O and P detach (p. 125); under k = 2 they form a plus-set drawing "more than 80%" of the negative ties.
- **Time scales (the authors' discussion).** Reciprocity near-instant (week 1); transitivity about 8-9 weeks; group balance still declining to week 15. They note that Newcomb's own account put reciprocity at week 3, and cite Nakao & Romney (1993, *Social Networks* 15: 109-131, doi:10.1016/0378-8733(93)90001-2, Crossref-confirmed) as finding attraction patterns stabilising at weeks 3-5 [sa, not read].

**What the 1996 paper does not do:** count per-type triples or triangles, report type-to-type conversion, or compare against a sign-shuffle on balanced vs imbalanced triangle frequencies. D&K 2001 was written to fill precisely that gap.

## 5. Where the Newcomb data is, and on what terms

**Do not download into the repo; this section only records locations.** The primary distribution page (the Pajek data site at vlado.fmf.uni-lj.si) refused the connection from the box on 2026-10-31, twice; the validation pass read the Internet Archive's public snapshot of it (web.archive.org, 2024-09-08), which is a public copy, not a bypass of any control.

| Where | What it is | Terms stated |
|---|---|---|
| UCINET dataset "Newcomb Fraternity Networks", via Batagelj & Mrvar's Pajek datasets page, `http://vlado.fmf.uni-lj.si/pub/networks/pub/data/UciNet/UciData.htm#newfrat` (the cited source link; unreachable here) | The original distribution (UCINET format, also readable by Pajek) | Archived listing ("UCINET IV Datasets", NEWFRAT): "Fifteen 17×17 matrices", NEWC0 - NEWC15 except NEWC9, non-symmetric, valued (rankings); "data from week 9 are missing". **No licence or terms statement anywhere on the page.** The 1996 paper (p. 114) says the data "are distributed as a part of UCINET (Borgatti, Everett and Freeman, 1992)" |
| UCI Network Data Repository page `https://networkdata.ics.uci.edu/netdata/html/Newcomb.html` (R `netdata` package v0.5-1 description) | Two `network.series` objects: `newcomb.rank`, **14** networks of rankings 1-16, 1 = first preference, no ties allowed; and `newcomb`, binary networks derived from it, tie i->j if i ranked j 8 or less. The same page says "collected longitudinally over 15 weeks, although data from week 9 are missing" | Page: protected by the Creative Commons licence (link to BY-NC-ND 2.5) **if the source does not specify otherwise**; cites Newcomb (1961), Nordlie (1958), White, Boorman & Breiger ("1977"; the AJS 81: 730-780 article is 1976, doi:10.1086/226141, Crossref-confirmed), Batagelj & Mrvar (2006) |
| R package `networkdata`, dataset `fraternity` (rdocumentation.org page, v0.1.6) | List of **15** igraph objects; weekly rankings, 17 men, fall 1956, week 9 missing; source given as Freeman's `moreno.ss.uci.edu/data#newfrat` (unreachable from the box) | Package DESCRIPTION (v0.2.4, GitHub) says "MIT + file LICENSE", copyright David Schoch: that licenses the package; it cannot grant rights in third-party data and the dataset page states no data terms. The page's paragraph about 475 authors belongs to another dataset |

**Format and content.** Rank-order sociomatrices (17 x 17, off-diagonal ranks 1-16 per row, no ties), one per week. **Ranks, not signs.** The page for the data says the binary version thresholds at rank 8, which is *not* a sign and not what D&K used. A signed derivation of the D&K kind (top 4 = +1, bottom 3 = -1, middle 0) is a modelling choice made by the analyst, tested by the authors for 3/3 and 3/2 variants (1996 fn 9). Nothing in the files records a sign or a dislike label even though Nordlie's procedure had a "dislike" pile; the pile membership is not in the rank file.

**Wave count: settled at 15.** The original UCINET distribution holds **15** matrices, NEWC0-NEWC15 with NEWC9 absent, which matches D&K and the 1996 paper (15 waves, 14 transitions, one two-week gap = weeks 8 to 10) and `networkdata` (15 objects). The UCI page's "14 networks" is the odd one out: either its conversion dropped a matrix or it miscounts (it also says "15 weeks" with week 9 missing, which would leave 14 only if counting weeks 1-15); which, is unconfirmed. Use the UCINET or `networkdata` series, and check the count on load. The UCI page's own note flags "17 men but ranks 1-16" as an inconsistency; it is not (each of 17 men ranks the other 16).

**Can an open repo reuse it? What the terms mean.** The original UCINET/Pajek listing states no terms at all. The only licence statement found is on the UCI mirror: CC BY-NC-ND 2.5, and only "if the source does not specify otherwise"; UCI is a redistributor, so its label may not reflect the custodians' position. If NC-ND does apply, plainly: **BY** = credit the source; **NC** = no commercial use; **ND** = no distribution of adapted versions. So an open repo **may not commit the rank matrices** (redistribution would be non-commercial only, which an open-source licence cannot promise), **nor a derived signed matrix** (a recoding is an adaptation, which ND forbids distributing). It **may** publish what is computed from the data: counts, test statistics, p-values, figures of results. Those are facts about the dataset, not copies of it, and are fine with attribution. Safe course: the repo holds the location, a fetch-and-recode script and the derivation rule, and results; the data file is fetched at run time and git-ignored. The analyses themselves (the two PDFs) are (c) OPA / Gordon and Breach and are paraphrased here, not reproduced. **Action for Aldred, only if the data file itself must ever ship:** ask the UCINET authors (Borgatti, Everett, Freeman) or Batagelj & Mrvar.

## 6. Reported rates and counts, collected [read unless marked]

- Actors 17; waves 15 (14 transitions); ranks 1-16; recode 4 positive, 3 negative, 9 null per actor per wave; so 68 positive and 51 negative ties every wave [D&K pp. 45, 49, 61].
- Null: 10,000 row-wise rank shuffles per wave for triples [D&K p. 49]; 1000 permutations for reciprocity and transitivity [1996 p. 123].
- Chance completion probabilities (Table 2): LL 3/15, LD 3/15, DL 4/15, DD 2/15 as stated in section 3.2 above.
- Triple types significantly **fewer** than the shuffled null by week 5, for the balanced types DLD and DDL; significantly **more** for LLL (all weeks), LDD (from week 2), DLL (from week 6), DDD (to 1.0 by week 5); LLD, LDL significantly fewer from the start [D&K p. 51].
- LDD completion probability p_bal rises from just above 0.2 to close to 0.7; DDL falls from 0.2 to 0.1; LLD falls from 0.15 to 0; DDD rises from just above 0.3 to below 0.7 [D&K p. 54, text].
- Tie turnover: just above 30% of dyadic ties change at the first transition, falling over about seven weeks [1996 p. 124].
- Reciprocated ties 30-36 of 68; null 95th about 23 and 99th about 25 [1996 p. 123].
- Imbalance I_b: first-wave 3-cluster partition error 15 per the table header, 20 per the text's components (inconsistent in the source); final-wave 4-cluster partition error 10 [1996 Tables 2, 3, p. 125].
- Received negative ties: 51 per wave; 43 of 51 to {C, J, O, P} in week 12; 37 of 51 to {J, P, C} at the end; J receives 16 of 16 at the end [D&K pp. 61-62; Table 5 not reproduced].

## 7. Empirical standing (blunt)

- One group, 17 men, one semester, one site, strangers meeting for the first time. That is a **tie-formation / acquaintance** setting, not a mature group.
- Signs are a recoding of ranks, with **fixed** numbers of positive and negative ties per actor, so neither the share of balanced triples nor the share of negative ties can vary: some structure is imposed by the instrument. The shuffle null respects the same constraint, which is why D&K's comparison is fair on that point, but any result about how many negative ties a group "should" have is untestable here.
- The paper's own verdict is negative on a uniform tendency to balance: of eight triple types, the incidence moves in the balance direction for four (LLL weakly, LDD, LLD, LDL), against it for DLL, DLD, DDL, and ambiguously for DDD. The aggregate decline in I_b hides these offsets.
- I could find no replication on a second signed longitudinal dataset in this session. The later work cited by D&K's followers (the 2024 arXiv paper on partial balance cites D&K's finding that "transitivity and balance were both present, but rival processes in the Newcomb fraternity dataset") repeats D&K rather than tests it [sa; paper unidentified, see Unconfirmed].

## 8. What the n = 3 test can and cannot do with this data

**Can.** (a) Test the **under-representation half** of the v0 n = 3 test against a sign-shuffled null of the kind the test names: v0 §7 says only "a sign-shuffled null"; D&K's is one specific choice (row-wise rank shuffle, so each actor's 4 L and 3 D out-ties are kept, received ties are not), 10,000 draws. Choosing it is our specification of v0's test, not something v0 fixed. D&K already did this on directed triples and report the result (section 3.3): LLD and LDL, two of the three one-negative types (both have a positive first tie), are significantly **under**-represented from the start and stay so; **but DLL, also a one-negative triple, is significantly over-represented from week 6 and ends near 1.0** under the same null. So "the one-negative triangle is under-represented" is **supported for two of three directed forms and refuted for the third**, and the third has a stated mechanism (competition for k), not a measurement artefact. v0's weak-balance rule makes DDD an allowed outcome; DDD is over-represented, consistent with the weak rule and contradicting strict balance. (b) Recompute from the rank files, with unchanged derivation, the per-wave count of undirected one-negative vs all-negative **triangles** (not triples) against a row-shuffle null, which D&K did not report; this requires a **symmetrisation rule for undirected signs** (e.g. all three ties among a vertex triple present with a stated rule for reciprocal pairs that disagree), itself a modelling choice to record. (c) Compute the **14 wave-to-wave conversion probabilities** (one of which spans two calendar weeks, 8 to 10) of triangle types directly from consecutive recoded matrices, which neither paper reports; with 17 actors there are 680 vertex triples per wave, so per-type counts at the small types will be a handful.

**Cannot.** (1) **Conversion-rate comparison as stated** (one-negative converts to balanced faster than all-negative): neither paper prints a type-to-type transition table, so it must be recomputed; D&K's p_bal is a **cross-sectional completion** frequency (how often the third tie closes a given pair of ties in the same wave), not a change in a given triangle over time. (2) **Explicit signs**: the signs are a recoding of ranks with fixed counts, by the authors' own admission a "major data problem"; the test therefore sits on a derivation, and any conversion is partly *rank crossing the cut-off*, indistinguishable from noise near the cut. (3) **Isolate drives:** the competition-for-k and popularity mechanisms D&K name produce the same signed-triple frequencies as balance does, and actor attributes are lost, so a failed balance prediction cannot be assigned to a missing drive rather than a missing covariate. (4) **Generalise to n greater than 3**: one group of 17. (5) **Time-scale:** most type frequencies reach their final side of the null by week 5 or 6, so the informative conversion window is the first four or five transitions, when about 30% of dyadic ties are changing; a test confined to later waves would have almost no events. (6) **Rely on aggregate balance falling**: the index declines while two balanced types become rarer, so a falling index would pass or fail the test for the wrong reason.

Verdict for ledger: **L4286 and L4445 move from [sa] to [read]**, and the finding changes shape: not "a uniform tendency is illusory" in the abstract, but a type-by-type split with a named rule (first tie positive: balance supported; first tie negative: contradicted).

## 9. Operand/operator translation for the algebra

- **Operands:** actor (17), signed directed tie with three states {+, 0, -} derived from rank, ordered triple (i, j, k) with its completion tie. Actor attributes would be a fourth operand and are absent.
- **Operators implied:** *completion* C(i->j, j->k) -> i->k with the two input signs selecting the distribution of the output sign. D&K's finding, restated: when i->j = + the completion obeys product-sign (balance); when i->j = - it does not: it follows agreement on k (a popularity/attribute term) and a rivalry term.
- **Does v0's rule survive?** v0's signed weight on the triangle (4.2b)/(5.1) is symmetric in the three ties; D&K show the **first tie is not exchangeable** with the others in this data. A symmetric triangle rule is refuted as stated for directed ties, and any v0 repair should make the sign of the first tie and received-negative counts (popularity) explicit terms.

## 10. What exists vs what does not

- **Exists** [read]: a signed-triple analysis of Newcomb over 15 waves against a row-shuffle null with 10,000 draws; per-type direction of change; a three-mechanism reading; reciprocity, transitivity and imbalance time series; the partition at weeks 1 and 15; the location of the rank data.
- **Does not exist in what I could access:** a printed transition matrix of triple or triangle types; per-wave numeric counts of triples (only plotted proportions); signed-tie ground truth for Newcomb (only ranks); a clear open licence for the rank data (the original Pajek/UCINET page states none; UCI's is conditional CC BY-NC-ND 2.5); a replication on another signed longitudinal dataset.

## 11. Drive basis

The sources frame this as cognitive: Heider tension reduction (balance as a pressure to consistency), with two **non-balance drives** added by D&K: (a) a **competition/rivalry** drive over a valued third party k (a desire-for-attention-of-k term; i dislikes j because j competes for k); (b) a **recognition of attributes** term, i.e. agreement on whom to like or dislike (a social-proof, status-recognition term, close to the status drive in file 055). Reciprocity is a separate, fast norm (Gouldner). None of the three is measured as a drive in the data: only ties are observed, so each drive is an inference from triple frequencies. The data cannot separate a drive for consistency from a drive for rank among peers.

## 12. What it predicts or controls

Predicts, in this one group: the direction of change by triple type and the week (about 5-6) after which each type stays on one side of its shuffled null; reciprocity by week 1; transitivity plateau by week 8-9; imbalance falling through week 15; polarisation onto a small set of consensus-disliked actors. Evidence is in-sample and descriptive, one group, no held-out prediction, no effect sizes with intervals. **Controls:** nothing; no intervention. The one implication for control is negative: pushing a triple toward balance would not work uniformly, since for a negative first tie the completion follows agreement on k, so an intervention would need to change who is seen as popular, not who dislikes whom.

## 13. Unconfirmed

- The terms the UCINET authors or Newcomb/Nordlie's custodians would set (no page states any); why the UCI `netdata` object has 14 networks where the original has 15; the exact mapping of D&K's week indices 1-15 to NEWC0-NEWC15 (inferred, not stated).
- The "2024 arXiv paper on partial balance" in section 7 is not identified by title, authors or arXiv id; the quoted phrase is unverified.
- D&K's "10,000" draws are not stated to be per wave in so many words (implied by Figure 1).
- Whether the signs under a bottom-3-only or top-3 variant change DLL and DDD.
- Which of D&K's one-negative types a v0 undirected triangle should map to when the two non-completion ties disagree in direction.
- Nakao & Romney (1993), Nordlie (1958) and Doreian & Mrvar (1996) are cited, not read.
- Figure-read numbers (all [fig] items) need a recomputation from the data before use.
- The Taylor & Francis reuse terms for the author-hosted copies; I have recorded numbers and paraphrase only.

## Validation log (2026-10-31)

Second pass, independent of the author. Both author-hosted PDFs re-fetched (HTTP 200, public, no login; no text layer, read as page images): D&K pp. 44-45, 48-52, 54-57, 61-62, 64-67; 1996 pp. 114-127. DOIs resolved at api.crossref.org.

- Doreian & Krackhardt 2001, JMS 25(1): 43-67, 10.1080/0022250X.2001.9990244: **confirmed** (Crossref; text read). Sign recode, 10,000-draw row shuffle with fixed L/D out-degrees, Figure 1 trajectories, Table 2 EVs, p_bal values, Table 3 verdicts, first-tie rule: confirmed [read]. Corrected: 37/51 at the end goes to three actors (J, P, C), not C, J, O, P; "dominant story" is p. 65; final partition is {13}, {C}, {J}, {O, P}; "LLL" in claim (2) flagged as a source misprint; "per wave" for the 10,000 draws is implied, not stated.
- Doreian, Kapuscinski, Krackhardt & Szczypula 1996, JMS 21(1-2): 113-131, 10.1080/0022250X.1996.9990176: **confirmed**; the brief's "Social Networks 18" correction is right. Corrected: "with one exception" is 1996 p. 117 not D&K p. 44; fn 8 vs main text on p. 121; first-wave error score inconsistent in source (15 vs 5 + 15); k = 2 imbalance ends near 13, not 11-12. No type-to-type conversion table in either paper: confirmed.
- Doreian & Mrvar 1996, Soc Netw 18: 149-168, 10.1016/0378-8733(95)00259-6: **confirmed** (Crossref; not read).
- Nakao & Romney 1993, Soc Netw 15: 109-131, 10.1016/0378-8733(93)90001-2: **confirmed** (Crossref; not read).
- Feld & Elmore 1982, SPQ 45: 77-85, 10.2307/3033928: **confirmed** (Crossref; D&K reference list read; not read itself).
- White, Boorman & Breiger, AJS 81: 730-780, 10.1086/226141: **confirmed as 1976**, not 1977 as the mirrors print.
- Newcomb 1961; Nordlie 1958: book and thesis, no DOI; **as cited by both papers**, not read.
- 2024 arXiv partial-balance paper: **unidentified**, moved to Unconfirmed.
- UCI Newcomb page: **confirmed** 14 networks, rank-8 binary cut, CC BY-NC-ND 2.5 conditional on the source not saying otherwise.
- Original UCINET/Pajek listing (Wayback snapshot 2024-09-08): **15 matrices**, NEWC0-15 minus NEWC9, **no terms stated**; settles the 14-vs-15 question in favour of 15.
- `networkdata` fraternity: **confirmed** 15 igraph objects; package MIT, no data terms.
- Section 8 vs models/00-v0.md §7: **consistent** in substance; corrected the claim that D&K's shuffle is "the exact null the test names" (v0 names no specific shuffle) and noted the two-week transition.

