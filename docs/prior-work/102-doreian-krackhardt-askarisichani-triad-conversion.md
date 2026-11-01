# Prior work 102: observed conversion of imbalanced triads (Doreian & Krackhardt 2001; Askarisichani et al. 2019)

Direction: D594

Date: 2026-10-29. Kind: deep-read. Question: in longitudinal triad data, which imbalanced triads actually convert to balanced ones, how fast, and does balance predict anything? Feeds v0's signed weights and the n = 3 test.

**Provenance rule applied.** [read] = I fetched and read the primary text this session. [sa] = secondary account. Nothing [sa] may feed an equation.

## What I read, and what I did not

| Work | Status | Route |
|---|---|---|
| Askarisichani, Lane, Bullo, Friedkin, Singh & Uzzi (2019), *Nat. Commun.* 10, 2648 | **read in full** (abstract, Results, Discussion, Methods; Tables 2 and 3 values from the journal's table pages) | Open access (CC BY 4.0), nature.com HTML. Figures 2-7 are images and were **not** readable: the full 16x16 transition matrices, the logit coefficients and the margins plot are not in the text. |
| Doreian & Krackhardt (2001), *J. Math. Sociol.* 25(1), 43-67 | **NOT read. Paywalled.** | Taylor & Francis returns 403. Unpaywall: `is_oa false`, `oa_status closed`, no locations. Semantic Scholar API 429. Search engines found no PDF copy. Everything below on D&K is [sa], taken from one later paper (Doreian & Mrvar 2015, below). |
| Doreian & Mrvar (2015), "Structural balance and signed international relations", *Journal of Social Structure* 16, doi:10.21307/joss-2019-012 (the DOI was minted on the journal's 2019 re-hosting; Crossref gives issued 2015), cmu.edu/joss/content/articles/volume16/DoreianMrvar.pdf | read the passage describing D&K (section 2.3) and the reference list only | This is the [sa] source for D&K. It is a secondary account by one of D&K's own authors. |

**The seed DOI for Askarisichani is wrong.** `10.1126/sciadv.aax8863` returns "Resource not found" from Crossref, and the paper is not in *Science Advances*. Correct: Askarisichani, O., Lane, J. N., Bullo, F., Friedkin, N. E., Singh, A. K. & Uzzi, B. (2019). Structural balance emerges and explains performance in risky decision-making. *Nature Communications* 10, article 2648, published 2019-06-14. doi:10.1038/s41467-019-10548-8 (Crossref-confirmed; matches the corrected citation in file 084). D&K DOI 10.1080/0022250X.2001.9990244 is Crossref-confirmed: title "Pre-transitive balance mechanisms for signed networks", Doreian and Krackhardt, vol. 25, pp. 43-67.

## 1. Doreian & Krackhardt (2001): all [sa], none usable in an equation

**What the one secondary account says (Doreian & Mrvar 2015, section 2.3) [sa].** Using longitudinal data from the Newcomb study (Nordlie, 1958), Doreian and Krackhardt (2001) examined how often each of the triples in Doreian & Mrvar's Figure 1 occurred over time. If there were a universal tendency towards balance, all balanced triples should become more frequent and all imbalanced ones less frequent. They instead found two of the balanced triples became less frequent and two of the imbalanced triples more frequent; the line index of imbalance fell overall but not monotonically. Doreian & Mrvar conclude that "a uniform tendency towards balance was illusory" and that there were "multiple mechanisms in play whose behavior need not be consistent". Same passage [sa]: Hummon & Doreian (2003; *Social Networks* 25, 17-49, doi:10.1016/S0378-8733(02)00019-9) simulated actors behaving as Heider envisioned in groups of various sizes and starting conditions; the trajectories were long, and many simulated groups did not reach balance. Doreian & Mrvar also say (section 7) that a general model of change is hard "for small groups given the limited evidence provided by Doreian and Krackhardt (2001) using temporal data".

**What this does and does not give.** It gives the headline: in the Newcomb fraternity data, balance does not rise triad-type by triad-type; the aggregate imbalance index falls but not monotonically. It does **not** give: which triad types converted, conversion probabilities, N, number of waves, the mechanisms D&K name (the title says "pre-transitive"; an unread, plausible reading is that popularity/reciprocity-type mechanisms act before transitivity, but that is my inference from the title and a search summary, not a reading), or how a signed tie was defined. The search summary also attributes to D&K the finding that differential popularity is a second process alongside cognitive consistency, and that transitivity and balance operate as rival processes; I could not check that against the text. Newcomb group size (my background knowledge, unchecked): small cohorts of about 17 men per year, weekly rankings over a semester. Treat as unverified.

**Scale.** Group (fraternity house, a closed small group) observed through its triads. No intervention.

**Status.** The conversion table the direction asked for **does not exist in my hands**. A reader with library access should read D&K's triad-transition tables before v0 uses any per-type conversion rate.

## 2. Askarisichani et al. (2019): what it is [read]

**Their vocabulary.** Structural balance theory (SBT); "sentiment network"; 16 triad types (the M-A-N directed-triad census); "permitted" triads 300 and 102; "forbidden" triads; "null triad" 003; "classic" balance; "hot hand"; "stability ratio"; "triad count ratio".

**Setting [read].** One medium-sized stock-trading firm, day traders, "an anonymous trading firm", 1 Oct 2007 to 31 Mar 2009, six quarterly periods. Abstract: "employed 66 day traders". >2 million instant messages and >1 million trades (the Results text says "we analyzed 128,323 instant messages, including content, as well as 14,259 trades", from which social IMs were then extracted; the abstract says >2 million IMs and >1 million trades overall; the paper does not reconcile the two sets of figures). Relationships are "flat and non-hierarchical"; traders have "relative autonomy". Per quarter a trader sent on average 228.82 +/- 40.22 IMs to 5.98 +/- 0.48 contacts; mean closeness centrality 0.15 +/- 0.04; mean clustering coefficient 0.35 +/- 0.04. Data are proprietary to the firm ("Data are available from the trading firm"); code at github.com/omid55/longitudinal_structural_balance_theory (the README I fetched is a single line; I did not inspect the repository).

**How a sign is defined: this is the load-bearing caveat [read].** Social IMs are separated from instrumental IMs by a financial-term dictionary (1,000 random IMs hand-checked by a research assistant; no accuracy figure given in the text). A **positive** directed edge i to j exists in a quarter if the IM count between them exceeds a null model (pairwise intensity randomised 10,000 times) at p < 0.01. "Edges between traders that are below the threshold are defined as non-positive or negative ties." So **a negative tie is the absence of a significant positive tie.** No message content is read for hostility. Alternative definitions: thresholds of at least 1, 5 or 10 messages. Robustness: randomly flipping up to 20% of edge polarities (replicas of 5% samples) did not change significance or pattern. The authors justify absence-as-negative by citing prior avoidance-tie work; it is an assumption, not a measured enmity.

**Operands.** A directed signed graph on traders; the unit of analysis is the ordered triple of traders and its 16-type class.

**Operators / equations, exactly as stated [read].**
- Balance of trader i in period t: ratio of triads of type 300 or 102 to all triads (that include i). Regressor is the log of this ratio.
- Transition counts T_ij(t): number of triads of type i at t that are type j at t+1. Transition probability p_ij(t) = T_ij(t) / T_i.(t), "row-stochastic ... conditional on i only, and not on prior states". Stationary distribution = normalised left eigenvector for eigenvalue 1. Transitions use only traders present in both periods.
- Triad count ratio c_xt = (number of type x triads) / (total triads) per period, compared with the stationary distribution (L2-norm distance, Table 2).
- Outcome: p_it = 1 if profit_it > (1/N) sum over t' of profit_it', else 0 (better than the trader's own mean monthly profit). Model: Logit(p_it) = beta_0 + beta_1 b_it, with controls (VIX-based market volatility high/low, trader fixed effects, period fixed effects, average trade value, active trading days, degree centrality, IMs sent), plus a non-parametric regression with 10-fold cross-validation and bootstrapped SEs. Null-model comparison of the coefficient against 10,000 degree- and dyad-preserving randomised networks (Milo et al. swap procedure).
- The four SBT rules as the authors state them: a friend of a friend is a friend; a friend of an enemy is an enemy; an enemy of a friend is an enemy; an enemy of an enemy is a friend. They add that with no violations only triads 300 and 102 exist, and cite Davis for the clustering generalisation that also allows 003. In their text both 003 and the "allowed based on Davis" set are counted when they say ~0.97 of stationary mass is in balanced states.

## 3. Results [read], with scale tags

**Conversion of imbalanced triads (group scale, observed through n = 3 substructures; observational).**
- Stationary distribution of the period-averaged chain, Table 3 [read]: 003 = 0.75; 102 = 0.20; 300 = 0.02; 012 = 0.02; 201 = 0.01; all others 0.00 (rounded; 120D, 120U, 030T, 021D, 021U, 021C, 111U, 111D, 030C, 120C, 210 all 0.00). So classic balanced (300+102) = 0.22; null triad 003 = 0.75; all 13 remaining non-balanced non-null types = 0.03 (012 and 201 are what is left).
- The one conversion rate given in the text: the transition 210 to 300 has probability "~0.3" per quarter (read off the matrices by the authors; the matrices themselves are in Figure 2, an image I could not read). The caption says "Transitions occur from unbalanced to balanced triads but not vice versa", and the text says balanced states 300, 102 and null 003 show "a strong propensity for stability".
- "Notably, although unbalanced triads are moving towards greater balance, these transitions occur slowly; hence, few forbidden triads (201 and 021) remain within our observation period (Table 3)." The text names 201 and 021 as the persisting ones; Table 3 shows 201 = 0.01 and no 021 type above 0.00. The abstract says "one unbalanced configuration resists change". The Results and Discussion identify it as the **null triad 003**, which the classic (300/102) definition counts as forbidden: "The stationarity of the null triad state suggests that forbidden triads remain in the network" (under Table 3) and "certain forbidden triads persist in the system, i.e., the null triad, which had been predicted by Heider" (Discussion). [read, validation 2026-10-30] The 201/021 sentence is a separate, smaller point.
- Stability across time: L2-distance of stationary distribution from the average, Table 2: 0.07, 0.08, 0.06, 0.05, 0.20 for transitions 1-2 to 5-6; stability ratio (share of matrix cells significantly different from randomised) 0.84, 0.92, 0.94, 0.91, 0.83. The last period, which coincides with the 2008-09 crash, is the outlier on distance.
- Against randomised networks: both 102 and 300 are significantly more frequent than in 10,000 randomised networks in all six periods; the null triad 003 is **less** frequent than random would suggest. The observed classic balance b_t is above the randomised expectation in every period, but "the overall ratio of classically balanced triads decreases over time", which the authors tie to the 2008-09 crash ("turtle up" under uncertainty). So the headline "tends to balance" is relative to a null, while the absolute balanced share fell.
- Interval robustness: results hold at monthly to weekly intervals except that at biweekly and weekly intervals there are more 003 triads and a higher probability of transition to 003.

**Balance and performance (membership/individual scale within a group; observational, no intervention).**
- Result: balance is positively associated with a trader being above their own mean monthly profit, p < 0.001 in both the logit and the non-parametric fit; the observed coefficient is outside the 10,000-null distribution (P < 0.001, Fig. 5). "The change from medium to high balance is associated with an almost 30% increase in profits" and "this strong positive relationship holds for over 75% of the data"; for the bottom 25% of the data, "a change in a trader's level of balance has no association with their trading performance". The relationship is described as "superlinear".
- **What is not in the text**: the logit coefficient and its standard error, the odds ratio, the cross-validation error, the number of trader-months, and any out-of-sample accuracy. The "almost 30%" is a read-off from a margins plot (Fig. 6b) described in a caption, not a stated estimate with a CI, and is a change in the probability-of-hot-hand index or profit, which the text does not distinguish clearly.
- Direction of causation: the Results/introduction say "There is temporal evidence that structural balance and performance are mutually reinforcing"; the Methods and Results I read contain **no** lagged or cross-lagged specification that tests this. I could not find the temporal evidence in the text. Treat "mutually reinforcing" as an unsupported claim in the version I read.
- The authors' own mechanism guesses (lower verification costs, social support damping emotional swings, less energy spent on strained ties) are stated as explanations, not tested.

## 4. Group size and composition

- **Size.** One group, n = 66, constant across the study; triads are n = 3 sub-units. No variation in n is analysed, so the paper says nothing about how conversion or the balance-performance link changes with n. The only size-related material is the [sa] note that Hummon & Doreian (2003) simulated groups "of various sizes" and found long trajectories with many not reaching balance.
- **Composition / definition.** Flat, same-rank, voluntary-tie, profit-competing traders; positive tie = communication above a null at p < 0.01; negative = absence. Definition drives the result: a sparse network (mean 5.98 contacts of 65 others) means most triads are empty, hence 003 = 0.75 of the stationary mass. The "0.97 balanced" figure is therefore overwhelmingly the all-absent triad counted as balanced, which is a statement about sparsity, not about resolved antagonism. The sign convention would not transfer to a group where negative ties are expressed hostility.
- **Intervention.** None. All observational; no consent-vs-manipulation question arises. The paper proposes experiments as future work.

## 5. Operand/operator translation for the algebra

- Operand: a signed directed tie weight on each ordered pair in a triad. Askarisichani's tie is a binary significance-thresholded communication indicator, not a drive or a continuous weight, so it gives v0's signed weight an **operational referent only in the weak sense** of "communicates more than chance". It cannot be mapped to liking vs hostility.
- Operator candidate: the empirical 16x16 triad transition matrix P (row-stochastic, quarterly). It is a measured Markov kernel on triad types. It could be used as a target that a drive-based triad dynamic has to reproduce (the 210 to 300 rate ~0.3, the stability of 300/102/003, the persistence of 201). The full P is in an image and the data are not public, so the entries are not available here.
- Falsifier for any "balance is a drive" equation: it must produce (i) balanced triads absorbing, (ii) conversion slow (a quarter-scale rate of order 0.3 for the quickest case), (iii) non-trivial persistence of some forbidden triads, (iv) the null triad dominant under sparsity. Mapping this to a drive requires the unread Figure 2 values.

## What exists vs what does not

- Exists [read]: one two-year, n = 66 field dataset with six quarterly triad censuses, a stationary distribution, a quantitative null-model comparison, and a within-person association of balance with above-own-mean profit.
- Exists [sa]: a Newcomb-fraternity result that triad frequencies do not all move toward balance and imbalance falls non-monotonically.
- Does not exist in what I could access: the D&K per-triad conversion table; a published, public, reusable dataset for Askarisichani (it is proprietary); any specification testing balance causing performance rather than co-varying; any variation in n; any measure where a negative tie means hostility; any replication of the Askarisichani result (one web search on 2026-10-30 found none).

## Unconfirmed

- Everything about D&K beyond the one paragraph quoted: mechanisms, N, waves, tie definitions, conversion rates.
- The meaning of "almost 30% increase in profits" (probability of hot hand vs profit level).
- Whether the "mutually reinforcing" claim has a supporting analysis in the supplement or figures.
- Replication status of either paper. A web search on 2026-10-30 found no replication of the trader study; the nearest is a nation-state signed-network paper (arXiv 2005.06245) using a similar triad Markov model, a different domain, not checked further.

## Does it reduce to a drive basis?

Partly, and only at the level of a single stylised rule. Heider-type balance is a **relational-consistency** pressure on triads (tension reduction), which is a cognitive-drive-like term attached to a person-in-triad; Askarisichani's finding that balanced triads are absorbing and forbidden ones convert slowly is compatible with a weak tension-reduction drive. What does **not** reduce: (a) the sign itself here is communication-above-chance, not a drive or a feeling, so no curiosity, fear or desire appears in the data; (b) 75% of the stationary mass is the empty triad, which is produced by sparse tie formation (an attention/capacity constraint, plausibly a resource limit rather than a drive) rather than by balance; (c) the performance link has plausible non-drive mechanisms (information trust, verification costs) that the authors themselves offer; (d) D&K's reported non-monotone movement, if accurate, says a single balance drive is inadequate and that several mechanisms with inconsistent behaviour are in play. The evidence here neither confirms nor refutes drives as primitives; it fits several non-drive accounts equally well.

## What does it predict or control, and how well?

Predicts: (1) the long-run distribution of triad types (stationary: 003 0.75, 102 0.20, 300 0.02) and which classes persist; (2) a binary indicator that a trader beats their own mean monthly profit, from the log share of balanced triads. Evidence: in-sample, one firm, 66 traders, six quarters. The only out-of-sample element is 10-fold cross-validation within the same firm for the non-parametric fit; no cross-validation score is reported in the text, so predictive accuracy is **unknown**. Effect size: the single quantitative statement is an "almost 30%" change from medium to high balance, read from a plot and ambiguously defined; no coefficient or CI given. Null-model results are strong (P < 0.001) but concern whether balance exceeds chance, not how well it forecasts. Failures and limits: absolute balanced share declined over the crash; the last period's distribution departs most from the average (L2 0.20); the effect is zero for the bottom quarter of balance levels; the sign convention (absence = negative) means "balance" partly measures sparsity; balance vs performance causality is not established; no intervention was tried, so control (steering a group to balance, or improving performance by doing so) is untested. D&K, as reported secondhand, adds a failure of the uniform tendency to balance in Newcomb data.

## Validation log (2026-10-30)

- ✓ Askarisichani, Lane, Bullo, Friedkin, Singh & Uzzi (2019), *Nat. Commun.* 10, 2648, doi:10.1038/s41467-019-10548-8. Crossref confirms title, authors, volume, article number and 2019-06-14. Full text read via Europe PMC (PMC6572859, CC BY). Checked against the text: 66 traders; 228.82 ± 40.22 IMs to 5.98 ± 0.48 contacts; closeness 0.15, clustering 0.35; negative = "non-positive" below the p < 0.01 null threshold, citing avoidance-tie work; 1/5/10-message thresholds; 20% polarity flips; T_ij, p_ij row-stochastic "conditional on i only"; transitions use only traders present in both periods; Table 2 (L2 0.07/0.08/0.06/0.05/0.20; ratios 0.84/0.92/0.94/0.91/0.83); Table 3 stationary values; 210 to 300 "~0.3"; 0.03 / 0.22 / ~0.97; 003 less frequent than random; "turtle up"; the biweekly/weekly 003 caveat; Logit(p_it) = β0 + β1 b_it with the listed controls; 10-fold CV; "almost 30%", "over 75%", "superlinear"; "mutually reinforcing" with no lagged specification anywhere in the text. All confirmed [read].
- ✎ Same paper: "128,323 social IMs" corrected. The text says 128,323 instant messages analysed, before the social ones were extracted.
- ✎ Same paper: the configuration that "resists change" was listed as unresolved. The paper's own text names it as the null triad 003. Moved out of Unconfirmed and stated in section 3.
- ✓ Doreian & Krackhardt (2001), *J. Math. Sociol.* 25(1), 43-67, doi:10.1080/0022250X.2001.9990244. Crossref confirms. Unpaywall: closed. Search found no free copy. Still unread, so every D&K claim stays [sa].
- ✎ Doreian & Mrvar: the year is **2015**, not 2019. JoSS vol. 16; the DOI 10.21307/joss-2019-012 dates from the 2019 re-hosting. I opened the PDF. The section 2.3 quotation is verbatim. The word "limited" comes from section 7, not section 2.3; the wording is now fixed.
- ✓ Hummon & Doreian (2003), *Social Networks* 25, 17-49, doi:10.1016/S0378-8733(02)00019-9. Crossref confirms. Cited only through Doreian & Mrvar [sa]; added the full reference.
- ? Nordlie (1958), an unpublished dissertation cited via Doreian & Mrvar. It has no DOI. The Newcomb cohort size (about 17) remains unverified background.
- ✓ Bad seed DOI 10.1126/sciadv.aax8863: Crossref has no record of it, as the file says.
- ✓ The "no replication" claim was tested with a search. None was found.

Sources opened: 2 primary texts (Askarisichani et al. 2019 full text; Doreian & Mrvar 2015 PDF), plus 5 Crossref records, 1 Unpaywall record and 2 searches.

Verdict: the file is accurate and unusually careful. Every Askarisichani number and quotation I checked matches the published text. The fixes are small: a wrong year for Doreian & Mrvar, an IM count described as "social" when it was the total, and one "unconfirmed" item that the paper itself answers (the persisting forbidden triad is 003). The central caveat holds: D&K is unread and paywalled, so nothing about Newcomb triad conversion can feed an equation. From Askarisichani, only the stationary distribution, the ~0.3 example rate and the Table 2 figures are [read] numbers, and they come with an absence-as-negative sign convention.

## Cross-checks (2026-10-30)

Grep of `docs/prior-work/*.md` (excluding this file) for Askarisichani, Doreian, Krackhardt, Hummon, Newcomb, Nordlie, triad, structural balance, null triad, stationary distribution and the DOIs. Overlapping files: 084 (Heider balance; the main overlap, cites both papers), 083 (one line on the "resists change" result), 03, 06, 13, 060, 095, 096 (balance theory background only).

**Agreements**

- Askarisichani et al. (2019) bibliography matches 084 (Nat. Commun. 10, 2648; doi:10.1038/s41467-019-10548-8).
- Doreian & Krackhardt (2001) bibliography matches 084 (J. Math. Sociol. 25, 43-67; doi:10.1080/0022250X.2001.9990244). Both files record it as unread, and 084 cites its Newcomb claim as [sa].
- The four SBT rules quoted here (friend of a friend, and so on) are the Heider product rule in 084, f_balance = s(u,w) s(v,w).
- Davis weak balance forbids only triangles with exactly one negative edge, so it allows 003 (all absent). 084 and this file agree. Classic balance (300, 102) forbids 003, so 003 is the unbalanced configuration under the strict rule.
- 084 quotes the Askarisichani abstract ("one unbalanced configuration resists change", "balance is positively related to performance", 66 traders, >2 million IMs). This file's read of the full text agrees with those quotes. 084 does not name the configuration; this file names it as 003 (see K4).
- The 084 "dynamics not covered" note and 083 both defer this result to later reading. 083 calls it a dynamics result for the Antal and Marvel models, which is a claim about use, not a conflict.

**Contradictions**

- **K1, duration.** 084 ("over two years") and this file §3 ("one two-year, n = 66 field dataset") versus this file §2 (dates 1 Oct 2007 to 31 Mar 2009, six quarterly periods, about 18 months). Both recorded; **unresolved**. The validation log does not settle it. Check the paper's Methods before any run-length figure is used.
- **K2, message count.** Abstract ">2 million instant messages" versus Results "128,323 instant messages" (this file §2). The paper does not reconcile them; the validation log fixed only the social-versus-total wording. **Unresolved.** 084 carries the abstract figure.
- **K3, sign semantics (definition, not a numerical clash).** 084's signed datasets (Epinions, Slashdot, Wikipedia, international alliances and disputes) use explicit signs: negative means expressed disapproval or dispute. Askarisichani's negative means "not significantly positive" (absence), with no content read. The two are not comparable as signed weights. **Unresolved**; v0 must state which convention its signed weights follow.
- **K4, which configuration resists change.** This file §3 first read the text as naming 201 and 021, then changed this to the null triad 003 at validation. 084 and 083 cite only the abstract. **Settled by the validation log** (the paper's own Discussion names 003). The sentence about 201 and 021 remains as a separate point in the paper.
- **K5, Askarisichani licence.** 084 records CC BY 4.0 as "believed, not verified". This file §2 records it as confirmed (nature.com, open access). Not a conflict; this file supersedes 084 on that point.

**Ledger notes for v0**

- Only [read] items feed equations: the stationary distribution, the Table 2 L2 distances and stability ratios, the 210 to 300 rate (~0.3, read off a figure caption), and the balance-profit association. Newcomb results (R8, R10) stay [sa] and do not feed an equation.
- The drive reading (tension reduction) is this file's inference, not a source claim. Its dup in 084 is the Heider "tension" note.
- Ledger lines are returned to the caller as structured output; this section does not duplicate them.

## Licences of quoted and transcribed material (2026-11-01)

- Askarisichani, Lane, Bullo, Friedkin, Singh & Uzzi 2019, Nat. Commun. 10:2648: CC BY 4.0 (open access; recorded in this file). Used as short quotations, restated equations and definitions (balance ratio, transition probabilities, logit), and Table 2 and Table 3 values (about 15 numerical values, facts; CC BY permits reuse with attribution). Figures 2-7 are not reproduced. The underlying trading-firm data are proprietary to the firm and are not held here; only published statistics are.
- Doreian & Mrvar 2015, J. Social Structure 16 (doi:10.21307/joss-2019-012): licence not determined; publisher copyright presumed. Section 2.3 is paraphrased with three short quotations (each under 15 words); the earlier 120-word quotation was cut in this audit.
- Doreian & Krackhardt 2001 (J. Math. Sociol., paywalled): not read; cited only via the secondary account above. Hummon & Doreian 2003, Nordlie 1958, Davis, Heider and other works named: cited only; not determined; publisher copyright presumed.
- The Newcomb fraternity data are not reproduced or held; only the headline finding as reported secondhand. No Wikipedia-derived text is used in this file (the word "Wikipedia" in the cross-checks names a signed-network dataset, not text).
