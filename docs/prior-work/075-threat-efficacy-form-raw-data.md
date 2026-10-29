# Prior work 075: product vs additive vs minimum forms of threat x efficacy, tested on raw data

Direction: D411

Date: 2026-10-29. Kind: data. Question (research map D411): is the threat x efficacy combination in fear-appeal / protection-motivation theory a product, an additive sum or a minimum, when tested on raw data rather than on authors' verbal summaries? Seeds: Witte & Allen 2000; Floyd et al. 2000; Milne, Sheeran & Orbell 2000; Fogg 2009. From file 35 (sections 1, 2, 4), which noted "multiplication is claimed constantly and almost never tested as multiplication".

**Method and honesty note.** Web search was unavailable this run (the shared search budget was spent), so there was no literature search. Everything below comes from (a) the OSF public API and Crossref, fetched directly, and (b) my own arithmetic on two public datasets I downloaded. Paper full texts (Witte & Allen, Floyd, Milne, Fogg) were NOT read. (Validation pass, 2026-10-29: Bigsby & Albarracín 2022 was then read in full via the NCBI PMC record PMC12437762, and the section 3 inferences checked against it; the Kaspar & Keller preregistration and R script were re-read and every section 4 number recomputed.) Tags: `[read]` = a number I read in a file I opened or recomputed myself; `[mine]` = my own computation, exploratory, not preregistered and not peer-reviewed; `[standard account]` = background carried from file 35. Scratch files are in the session scratchpad, not the repo.

## 1. Headline

1. **No participant-level data exists for the classic meta-analyses.** Floyd 2000, Milne 2000, Witte & Allen 2000 and Tannenbaum 2015 publish study-level effects only; I found no public raw data for any of them (Crossref record of Tannenbaum 2015 lists no data link). So "tested on raw data" has to mean one of two substitutes: effect-level tables (section 3) or recent open participant-level experiments (section 4).
2. **Effect-level data favour an interaction in sign, not in a specific form.** In the Bigsby & Albarracin effect table, 14 of 17 within-study low-vs-high-efficacy contrasts show a larger threat effect under high efficacy (mean difference +0.55 d `[mine]`), and the threat effect is negative (a sign flip) in 9 of the 17 low-efficacy cells. That is the EPPM prediction; a pure product through the origin (zero threat effect at zero efficacy) and a pure additive form (constant threat effect) both fail the sign flip, which is more EPPM-like (a mode switch) than any smooth product.
3. **The one large open participant-level dataset I could test (Kaspar & Keller, N = 1,450) does not support multiplication.** Among perceived threat T and perceived efficacy E, the additive model beats product-only and min-only by a wide margin, and the T x E coefficient is slightly *negative* (sub-additive) `[mine]`. Caveat: observational (perceived measures), threat near ceiling, efficacy manipulation weak. A null, not a refutation of the EPPM.
4. **The 2 x 2 designs in this literature cannot separate product from min anyway** (section 5). A tested form needs at least three levels per factor.

## 2. Catalogue of datasets

| ID | Source | Access | Licence | Unit | Variables | Usable for |
|---|---|---|---|---|---|---|
| A | OSF node `h9fyd`, "Self- and Response Efficacy Information in Fear Appeals" (OSF contributors Elisabeth Bigsby, Dolores Albarracín, Daniel J. O'Keefe); the paper is Bigsby & Albarracín 2022, *J. Communication* 72(2), 241-263, DOI 10.1093/joc/jqab048 (Crossref-confirmed; authors Bigsby and Albarracín only; its footnote 3 links this OSF node as the project's data) | https://osf.io/h9fyd/ ; files `Table 1 Data.xlsx` (https://osf.io/download/ns24u/), `Table 2 Data.xlsx` (https://osf.io/download/8zer7/) | none stated on the node (`node_license` null) | effect size (study cell) | manuscript, response-efficacy Y/N, self-efficacy Y/N, topic, d, N | within-study low/high efficacy contrasts (section 3) |
| B | Kaspar & Keller, "Disentangling Self- and Response Efficacy in Fear Appeals" (OSF node `wcxvg`; creator Lisa Kaspar; created 2025-02-11, modified 2026-03-18) | https://osf.io/wcxvg/ ; `data.xlsx` (https://osf.io/download/fn4qe/), `Codebook.xlsx` (empty sheet when I opened it), `data_analysis_osf.R`, `Preregistration_Kaspar_Keller.pdf` | none stated | participant (1,453 rows; 1,450 complete on the scales used) | condition `rand` (NSNR, NSPR, PSNR, PSPR, CONTR), self-efficacy (5 items), response efficacy (5), severity (3), susceptibility (3), fear (3), hope (3), behavioural intention (16), emotions, credibility, SES | threat x efficacy functional form (section 4) |
| C | Cheng & Toivo, fear appeals in Cantonese-English bilinguals (OSF `y45mb`) | https://osf.io/y45mb/ ; `1_dat_9_2_24.csv`, `2_dat_3_3_25.csv`, `join_dat.csv`, `data_codebook.xlsx`, R markdown | none stated | participant | sun-protection (melanoma) fear appeal; fear ratings (6 items), behaviour items, LexTALE language scores | a language-by-fear test; **no threat x efficacy factorial seen**; not used |
| D | "Towards consensus on fear appeals" (OSF `a2v46`, created 2018-03-07, modified 2022-05-31) | https://osf.io/a2v46/ | none | none | the project has no files in osfstorage; one wiki page not read | nothing; follows the 2018 Health Psychology Review debate |
| E | Kok et al. 2018 project (OSF `sdp5h`) | https://osf.io/sdp5h/ | none | none | three files: R script and plots "fear appeal visualisations" only | visualisation of Kok et al.'s case; no raw data |
| F | Tannenbaum et al. 2015 / Witte & Allen 2000 / Floyd et al. 2000 / Milne et al. 2000 | journal only | publisher | study | effect sizes in printed tables | not obtained; would need transcription from the PDFs |

Dataset A is a different object from the one the Tannenbaum team coded. The paper's authors are Bigsby (Illinois at Urbana-Champaign, per the paper) and Albarracín (Penn); O'Keefe is an OSF contributor, not a paper author. The paper says its search "began with the list of studies identified in Tannenbaum et al.'s (2015) meta-analysis" with different inclusion criteria `[read]`, so it shares an ancestry with Tannenbaum but is a *separate* meta-analysis of efficacy information (k = 158, N = 19,736). **N in table 1 is the comparison's total N, not a group N**: the column sums to 19,551 over 157 rows, against the paper's 19,736 over k = 158 (one comparison absent from the file or entered differently) `[mine]`. Several rows repeat a study's N (e.g. N = 114 for each Fukada 1975 comparison).

## 3. Dataset A: what the effect table can and cannot say

**What the columns mean (confirmed against the paper `[read]`).** In table 1, d is the bias-corrected standardized mean difference between a fear appeal (Bigsby & Albarracín 2022, J. Communication 72(2), DOI 10.1093/joc/jqab048, defines it as including "or stronger fear appeal") and a comparison group (the same paper defines it as "no message, message that was not a fear appeal, or weaker fear appeal") on intentions and/or behaviour, averaged to one d per sample; positive means the fear treatment did better. The Y/N flags code presence of efficacy information (the paper codes positive / negative / absent; the file keeps only Y/N). So the original inference (d = threat effect within the stated efficacy condition) holds. Table 1 has 157 usable d-rows. Table 2 is a different quantity: k = 19, N = 2,166, high-fear cells only, d = positive efficacy information vs negative or no efficacy information; it holds no low-fear comparison.

**Pooled by flag `[mine]`** (unweighted mean d; N-weighted in brackets; "RE" = response efficacy flag, "SE" = self-efficacy flag):
- neither (N,N): 70 rows, 0.13 [0.19]
- RE only (Y,N): 44 rows, 0.59 [0.60]
- SE only (N,Y): 7 rows, 0.22 [0.31]
- both (Y,Y): 36 rows, 0.34 [0.33]

For comparison, the paper's own weighted mixed-effects meta-regression found that only positive response-efficacy information moderated d; the both-efficacies combination did not differ significantly from no efficacy information, which the authors call "surprising" `[read]`. These pools mix studies and are confounded by topic, so only the contrast "efficacy present vs absent" (roughly 0.1-0.2 vs 0.3-0.6) is suggestive. The oddity that "both" is lower than "RE only" is reported as found; it is exactly what an additive sum of efficacies cannot give, and a reason not to read pooled flags as a factorial.

**Within-study contrasts `[mine]`** (d at low efficacy -> d at high efficacy; every pair is read from table 1):

| Study cell | low -> high |
|---|---|
| Chen & Yang 2019 | 1.37 -> 2.44 |
| Chu 1966 (low vs high of three levels) | 0.37 -> 1.70 (medium 0.52) |
| Kleinot & Rogers 1982 | 0.77 -> 1.15 |
| Fukada 1975, low credibility | -0.08 -> 0.48 |
| Fukada 1975, high credibility | 0.63 -> 0.69 |
| Ordonana et al. 2009 | 0.48 -> 0.52 |
| Rogers & Mewborn 1976 | -0.04 -> 0.41 |
| Roskos-Ewoldsen et al. 2004 | 0.13 -> 0.47 |
| Self & Rogers 1990 | -0.55 -> 0.64 |
| Smalec & Klingle 2000 | -0.60 -> 1.39 |
| Smerecnik & Ruiter 2010 | -0.18 -> 0.76 |
| Wong & Cappella 2009 (perceived low vs high efficacy; both rows flagged Y,Y, so a measured split, not a manipulation) | -0.01 -> 0.82 |
| Sturges & Rogers 1996: children / teens / adults | 0.24 -> 0.15; -0.23 -> 0.49; -0.29 -> 0.53 |
| Sprinkle et al. 2006 | -0.07 -> -1.22 (reversed) |
| van Bavel et al. 2019 (N about 1,010 per comparison) | 0.12 -> 0.01 (reversed; the largest study) |

Summary of the 17 contrasts: mean low-efficacy d = 0.12, mean high-efficacy d = 0.67, mean difference +0.55 (median +0.56), 14 positive, 3 non-positive-direction (children, Sprinkle, van Bavel). Nine of 17 low-efficacy cells have d below zero. (Recomputed in validation: 17 contrasts, means 0.121 and 0.672, mean difference 0.551, median 0.56, 14 positive, 9 negative low-efficacy cells.) **Bluntly:** the pattern is consistent with the EPPM sign flip, but (i) most contrast cells come from small comparisons (total N 22-60 per comparison; the standard error of d at total N = 22 is about 0.43), so the negatives are within noise individually; the larger ones (Chen & Yang 244, Chu about 240, Wong & Cappella about 277) all have positive low-efficacy d; (ii) the largest contrast by far (van Bavel, N about 1,010 per comparison) goes the wrong way, as do the small Sturges children cells (N 60/63) and Sprinkle; (iii) publication selection is untested here; (iv) Wong & Cappella's "efficacy" is perceived, not manipulated.

**One 2 x 2 in the table, Wurtele & Maddux 1987** (N = 40 per cell) `[read]`: no efficacy 1.42; self-efficacy only -0.12; response efficacy only 0.74; both 1.22. The largest threat effect sits in the *no-efficacy* cell. That contradicts both product and EPPM and agrees with neither min nor sum; it is one small study, but it is the only full factorial with both efficacies crossed in this table, and it is not monotone in efficacy.

**What this does to the forms.** Let b = effect of the threat manipulation, E = efficacy level:
- additive: b is independent of E. Rejected in direction by the mean difference +0.55, not rejected study by study (most CIs are wide).
- product (b = k E, E>=0): predicts b = 0 at E = 0 and monotone increase. The data show b < 0 at E = 0 in about half the cells; product has no natural way to give a negative.
- minimum (response = min(T, E)): predicts the threat manipulation does nothing when E is the binding constraint, so b = 0 at low E, again not negative.
- the EPPM's gated rule (danger control iff E exceeds T, else fear control) *can* give a sign flip at low E. File 35's "no one has shown a clean sign-flip meta-analytically" stands; this table shows the sign of the point estimates but not that the flip survives noise.

## 4. Dataset B (Kaspar & Keller): a participant-level test on 1,450 people

**Design (from the preregistration PDF, `[read]`).** Climate-change fear appeal, a written text of about 300 words, recruited on Prolific (GBP 2) and run in LimeSurvey. The preregistration says "almost all items have been translated to German by the authors" and anchors subjective SES to "other people in Germany", so the study appears to be in German; it does not state the stimulus language. The R script records 1,722 finished surveys; its exclusion chain runs 1,708 -> 1,701 -> 1,644 -> 1,453. 2 x 2 + control: self-efficacy information positive (P) vs negative (N) x response-efficacy information positive vs negative, plus a control that reads a neutral essay on natural climate archives, i.e. **no threat and no efficacy information** (not merely a no-efficacy control). Condition codes in the data: NSNR 324, NSPR 294, PSNR 262, PSPR 283, CONTR 290 (counts for rows with a value in `rand`). Outcomes: behavioural intention (16 items, 5-point, pilot alpha .92), hope, fear (3 items each), plus perceived severity, susceptibility, self- and response-efficacy. Threat information is **not** manipulated among the four experimental cells: they share the same threat section, so the 2 x 2 varies efficacy only (the control differs in both). The authors pre-registered excluding manipulation-check failures but, per the R script, did not, because failure rates differed by cell `[read]`; the data file therefore includes them. The preregistered hypotheses were that NSNR is lowest and PSPR highest on intention (H4.1-4.3), the EPPM's "both efficacies needed".

**Data handling `[mine]`.** Scales are item means; "r"-suffixed items appear already reverse-scored in the file (within-scale correlations are all positive, 0.34-0.84). Missing items skipped with a row mean. Complete cases n = 1,450.

**Manipulation check `[mine]`.** The efficacy information barely moved perceived efficacy: perceived response efficacy by cell NSNR 2.47, PSNR 2.37, NSPR 2.77, PSPR 2.88 (1-5 scale); self-efficacy 3.08, 3.17, 3.37, 3.46 (the response-efficacy factor shifted perceived response efficacy by about 0.3-0.5 (0.30 under negative SE, 0.51 under positive SE) and also shifted perceived self-efficacy by about 0.3, while the self-efficacy factor shifted perceived self-efficacy by only about 0.1, so the two are not manipulated independently; recomputed in validation). Perceived severity and susceptibility are about 4.3 on 5 in every cell (ceiling), and mean intention is 3.73-3.83 in every cell (SD 0.80). The preregistered predicted ordering of intention is not seen: PSPR has the *lowest* mean (3.73), NSPR the highest (3.83). Interaction contrast (PSPR-PSNR)-(NSPR-NSNR) = -0.05 on a 5-point scale (SD 0.8); not tested for significance here. **The experimental manipulation did essentially nothing to intention.** So the dataset cannot test the EPPM through the manipulation; it can only be used observationally, through the perceived scales.

**Functional-form fits on the perceived measures `[mine]`**, outcome = mean intention, OLS, n = 1,450. T = mean of (severity, susceptibility) item means; E = geometric mean of self- and response-efficacy (sqrt(S R)); R^2 and AIC (lower is better):

| Model | R^2 | AIC |
|---|---|---|
| T + E (additive) | 0.474 | -1589 |
| T + E + T x E | 0.480 | -1604 |
| T x E only (pure product) | 0.375 | -1341 |
| min(T, E) only | 0.257 | -1090 |
| min(T, E) + T + E | 0.474 | -1588 |

Coefficients with centred T and E: intercept 3.80, T 0.50, E 0.30, T x E -0.084; bootstrap (1,000 resamples) 95% interval for the interaction: -0.132 to -0.034. Within efficacy only: S + R additive R^2 0.303, with S x R 0.324 (coefficient on S x R -0.13; AIC -1181 vs -1224), pure S x R only 0.187, min(S, R) only 0.162.

*Validation re-fit `[mine]`.* All the above reproduced to the stated decimals (AIC absolute values differ by a constant 2 under a different parameter count; differences unchanged). Note that the authors' own analysis (R script) drops four efficacy items after an EFA (self2r, self3, resp1, resp5r) and uses **three items per efficacy scale**; the five-item scales used here are not theirs. With the authors' three-item scales the conclusion is unchanged: T + E R^2 0.476, + T x E 0.480 (centred T x E -0.074, bootstrap 95% -0.123 to -0.021), T x E only 0.374, min only 0.251.

**Reading.** (i) Pure product and pure min lose heavily to the additive baseline on this variable pair; adding the product term to the additive model buys 0.006 in R^2 and with a *negative* sign (sub-additive, diminishing returns as both approach the 5-point ceiling). (ii) This is what a bounded response variable plus a ceiling in T does to any interaction, so it says little about the multiplicative claim as a theory of mechanism. (iii) T has restricted range (mean 4.3 of 5): the data cannot probe the low-threat region where the interaction is claimed to matter. (iv) These are perceived (non-manipulated) measures with a common-method design: T, E and intention come from one questionnaire; correlation T-intention is 0.61, E-intention 0.48, T-E 0.29. (v) The correlational-vs-experimental gap flagged for Floyd et al. in file 35 applies in full. **No claim about causal form should be made from this.**

## 5. Which fits tell the forms apart (the identifiability point)

- A 2 x 2 factorial (low/high threat x low/high efficacy) has four means and three contrasts. A product through the origin, a min and an additive-plus-interaction model can all reproduce the same 2 x 2 table by suitable scaling of "low" and "high". They differ in the *interior*, which needs at least three levels of each factor (or a continuous measured level). Dataset A has one three-level factor (Chu 1966; efficacy 0.37, 0.52, 1.70, convex, but the levels are not equally spaced so this is a single weak datum).
- A significant interaction on a raw scale is scale-dependent: under a monotone transform of the outcome, an interaction can appear or vanish unless it is a crossover (a sign change of the threat effect across efficacy levels). The only interaction form that is scale-free in this sense is the sign flip, which is the claim Witte makes and Kok et al. dispute. That is a reason for the algebra to *state the flip as the primitive* (a gate on E - T, section 2 of file 35) and leave the smooth interaction as a derived or fitted feature.
- Fogg's model (B = M x A x P) is never presented with data at the level of a fitted functional form `[standard account]`; I found nothing in this run that fits product vs additive on its variables. Not resolved.

## 6. Operand / operator translation for the algebra

- Operand: agent with threat state T and efficacy state E (graded; E decomposable into response and self parts, which dataset B shows moving together: manipulating response efficacy moved perceived self-efficacy as well).
- Operators on the agent: message(dT), message(dE). The contribution of this note: **the data support "E raises the effect of dT" in sign and do not support a specific multiplicative combination rule**. Safe primitives: (1) a monotone additive drive-strength map; (2) a gate on E - T that can reverse the sign of dT; (3) the product as a derived approximation, not an axiom.
- Soft-setting guidance (Aldred's standing preference): the combination rule should be an editable setting of the model (sum, product, min, gated) with a recorded evidence status "not discriminated", not a wall.

## 7. What exists vs what does not

Exists: a public effect-level table with efficacy flags (A) and a 1,450-person participant-level dataset with efficacy crossed (B); both open on OSF, neither with a licence statement. Does not exist (as far as found): participant-level raw data for Floyd, Milne, Witte & Allen, or Tannenbaum; any fear-appeal experiment I could check that crosses 3+ levels of threat with 3+ levels of efficacy; a head-to-head fit of product vs min vs additive on such a design; any data fitting Fogg's M x A x P.

## 8. Unconfirmed

- (Resolved in validation: the meaning of d and N in dataset A, now confirmed from the paper, section 3.)
- Whether Bigsby & Albarracín report the within-study sign flip: they do not analyse it. Their moderator test is a mixed-effects meta-regression on efficacy type (positive RE significant; positive SE, both, and negative types not), and they mention possible boomerang effects of negative efficacy information only as theory (citing Popova 2012; Witte 1992; Kok et al. 2018) `[read]`. The flip analysis in section 3 remains this file's own.
- Witte & Allen (2000, *Health Education & Behavior* 27(5), 591-615, DOI 10.1177/109019810002700506), Floyd, Prentice-Dunn & Rogers (2000, *JASP* 30, 407-429, DOI 10.1111/j.1559-1816.2000.tb02323.x), Milne, Sheeran & Orbell (2000, *JASP* 30, 106-143, DOI 10.1111/j.1559-1816.2000.tb02308.x), Tannenbaum et al. (2015, *Psychological Bulletin* 141, 1178-1204, DOI 10.1037/a0039729) and Fogg (2009, Persuasive '09, DOI 10.1145/1541948.1541999): all Crossref-confirmed; none read; what they say about the combination rule is carried from file 35. One second-hand point, from Bigsby & Albarracín `[read]`: Witte & Allen's final threat x efficacy interaction analysis "was conducted via standard ANOVA and not meta-ANOVA".
- Kok, Peters, Kessels, ten Hoor & Ruiter (2018), "Ignoring theory and misinterpreting evidence: the false belief in fear appeals", *Health Psychology Review* 12(2), 111-125, DOI 10.1080/17437199.2017.1415767 (Crossref-confirmed): the paper behind OSF `sdp5h` (whose title it shares and whose contributors are these five authors). `a2v46` has the same five contributors. Not read.
- Mulilis & Lippa (1990), "Behavioral Change in Earthquake Preparedness Due to Negative Threat Appeals: A Test of Protection Motivation Theory", *J. Applied Social Psychology* 20, 619-638, DOI 10.1111/j.1559-1816.1990.tb00429.x, and Mulilis & Duval (1995), "Negative Threat Appeals and Earthquake Preparedness: A Person-Relative-to-Event (PrE) Model of Coping With Threat", *JASP* 25, 1319-1339, DOI 10.1111/j.1559-1816.1995.tb02620.x (both Crossref-confirmed). The PrE model is named only in the 1995 title; the 1990 paper is a PMT test. That PrE is a threat-relative-to-coping (ratio-like) form, and the closest published precedent to a gated or ratio rule, is inferred from the title only. Content unread.
- Dataset C and the wiki on node `a2v46` unopened beyond the file listing.
- Whether the Kaspar & Keller sample has been analysed in a paper; the preregistered (H4.x) results are not stated in this file. A Crossref bibliographic query found no matching paper; web search was unavailable in the validation pass too, so this is not settled.
- The "does not exist" claims in section 7 (no 3+ x 3+ threat x efficacy design; no fitted test of Fogg's M x A x P) could not be tested by web search in validation (budget spent). They stand as "not found in this run", not as established absences.

## Validation log (2026-10-29)

Web search was unavailable for this pass too (shared budget spent); checks used Crossref, the OSF API, the NCBI PMC record of Bigsby & Albarracín 2022, and a full recomputation from the downloaded OSF files.

- ✎ Bigsby & Albarracín 2022, *J. Commun.* 72, 241-263, DOI 10.1093/joc/jqab048: read in full. Meaning of d confirmed (fear vs no/weaker fear); N corrected from "group N" to the comparison's total N; first author's affiliation corrected (Illinois at Urbana-Champaign, not Iowa); O'Keefe is an OSF contributor, not an author; RE-only pooled mean 0.60 -> 0.59; table 2 described correctly as a different quantity; their own moderator result added.
- ✓ Dataset A (OSF `h9fyd`): files, contributors, null licence confirmed; all 17 within-study pairs and the summary statistics reproduced exactly; Wurtele & Maddux 1987 2 x 2 cells confirmed. ✎ caveats re-stated (most contrasts small but not all; Wong & Cappella's efficacy is perceived; "two largest contrasts" wording corrected).
- ✎ Kaspar & Keller (OSF `wcxvg`, creator Lisa Kaspar): counts, cell means, every R^2, AIC difference, coefficient and bootstrap interval reproduced. Corrected: the stimulus is not stated as English and the study appears German-language; the control group has no threat information either; manipulation shift 0.4-0.5 -> 0.3-0.5; added that the authors used three-item efficacy scales and did not apply their pre-registered manipulation-check exclusion (re-fit with their scales: same conclusion).
- ✓ Witte & Allen 2000, DOI 10.1177/109019810002700506: exists, authorship confirmed (not read).
- ✓ Floyd, Prentice-Dunn & Rogers 2000, DOI 10.1111/j.1559-1816.2000.tb02323.x: exists (not read).
- ✓ Milne, Sheeran & Orbell 2000, DOI 10.1111/j.1559-1816.2000.tb02308.x: exists (not read).
- ✓ Tannenbaum et al. 2015, DOI 10.1037/a0039729: exists, seven authors (not read).
- ✓ Fogg 2009, DOI 10.1145/1541948.1541999: exists (not read).
- ✎ Mulilis & Lippa 1990 / Mulilis & Duval 1995: both exist; the PrE model is named only in the 1995 paper, so the attribution now says so.
- ✓ Kok et al. 2018, DOI 10.1080/17437199.2017.1415767: exists; identified as the paper behind OSF `sdp5h` (added).
- ✓ OSF `y45mb` (Cheng & Toivo), `a2v46` (Peters, Ruiter, ten Hoor, Kessels, Kok; no files): metadata confirmed; content unread.
- ? "Does not exist" claims (3+ x 3+ designs; fits of Fogg's model) and whether Kaspar & Keller is published: untestable without web search; left as "not found".

**Verdict.** The file's data work is sound: every number recomputed from the public files came out as stated, and the inferred meaning of the Bigsby & Albarracín effect sizes is confirmed by the paper. The errors were in description, not arithmetic: the N column, an affiliation, O'Keefe's role, the Kaspar & Keller language and control condition, the size of one manipulation shift, and the attribution of the PrE model; all are fixed in place. The conclusion (sign-level support for an efficacy-dependent threat effect, no support for a specific product or min rule) stands, with its absence claims still untested by search.

## Cross-checks (2026-10-29)

Scope: every other file in this directory was grepped for the works, authors, equations and numbers used here (Witte, Floyd, Milne, Tannenbaum, Fogg, Bigsby, Kaspar, Kok, Peters, Wurtele, Mulilis, EPPM, fear appeal, efficacy). Only `35-behaviour-change-persuasion.md` (file 35) overlaps; no other file in 01-082 discusses fear appeals, PMT or efficacy. Other files were not edited.

### Agreements
- **Citations (file 35 section 1/2 citation blocks and section 4).** Witte & Allen 2000 (*Health Educ. Behav.* 27(5), 591-615, DOI 10.1177/109019810002700506), Floyd et al. 2000 (*JASP* 30(2), 407-429, DOI ...tb02323.x), Tannenbaum et al. 2015 (*Psychol. Bull.* 141(6), 1178-1204, DOI 10.1037/a0039729), Kok et al. 2018 (*Health Psychol. Rev.* 12(2), 111-125, DOI 10.1080/17437199.2017.1415767) and Fogg 2009 (DOI 10.1145/1541948.1541999) are identical here and in file 35.
- **EPPM rule.** File 35 section 2 "Operators / equations": danger control iff efficacy > threat, else fear control; the sign-flip (negative effect of threat at low efficacy) is the contested, distinctive prediction. Matches this file's sections 3 and 5.
- **Sign-flip evidence.** File 35 section 2 "My read": "No one has shown a clean sign-flip meta-analytically." This file's section 3 says the same stands (point-estimate signs only, within noise).
- **Efficacy raises the threat effect.** File 35 (Tannenbaum 2015 summary, section 2): effects larger when messages include efficacy statements; Sheeran 2014: d+ .98 on intention when threat, response and self-efficacy are raised together. This file's pooled-by-flag result (efficacy present about 0.3-0.6 vs absent 0.13) and the 14-of-17 within-study contrasts point the same way.
- **Product claimed, not tested.** File 35 "Does not exist" (section 12 list: "Any tested multiplicative form... a direct multiplicative-vs-additive-vs-min comparison on threat and efficacy is what I did not find") and file 35 section 2 ("stated as a product in the theory but tested in practice as additive main effects"). This file's sections 4-5 supply the first such comparison (additive wins on perceived measures; 2 x 2 cannot discriminate).
- **Fogg.** File 35 section 4: the 2009 paper gives a curve not a formula, the product B = M x A x P is a summary, never fitted. This file's section 5 and section 7: no fit found. Agree. Naming note: file 35 says the 2009 paper's third factor is "trigger" (B = MAT) and "prompt" (MAP) is later; this file writes M x A x P without comment. Not a factual conflict, but should read "trigger/prompt".
- **Milne, Sheeran & Orbell 2000.** File 35 section 1 gave JASP 30(1), 106-143 and listed the DOI as unresolved; this file supplies DOI 10.1111/j.1559-1816.2000.tb02308.x. Re-checked against Crossref: title "Prediction and Intervention in Health-Related Behavior: A Meta-Analytic Review of Protection Motivation Theory", vol 30(1), pp. 106-143, authors Milne, Sheeran, Orbell. Resolves file 35's open item.
- **Floyd 2000 data status.** File 35 notes Floyd's studies are largely correlational/intentions-based; this file's headline 1 (study-level effects only, no raw data) is consistent.
- **Two different meta-analyses.** File 35 section 2 describes Tannenbaum 2015 (127 articles, 248 samples, N = 27,372, d = 0.29). This file's dataset A is Bigsby & Albarracin 2022 (k = 158, N = 19,736), explicitly a separate meta-analysis that started from Tannenbaum's list. No numerical clash.

### Contradictions and tensions
1. **Tannenbaum "no backfire" vs negative cells here.**
   - File 35 section 2 (Tannenbaum 2015, abstract read): "there are no identified circumstances under which they backfire" overall.
   - This file section 3 / headline 2: threat effect negative in 9 of 17 low-efficacy cells of the Bigsby & Albarracin table, read as a possible sign flip.
   - Verdict: **not a true contradiction; unresolved as to meaning.** Different datasets and quantities (Tannenbaum's pooled moderators vs 17 hand-picked within-study low-efficacy cells, mostly N 22-60 with SE of d about 0.43 at the smallest). The negatives are within noise individually, which this file already says. Wording in headline 2 ("the threat effect is negative (a sign flip)") should be read as "negative point estimates" so as not to imply a conflict with file 35. No primary source checked (Tannenbaum full text not read here or in file 35).
2. **Omission, not conflict: Peters, Ruiter & Kok 2013.** File 35 section 2 ([read: abstract]): of six qualifying full-factorial threat x efficacy studies with behaviour as outcome, a significant interaction, threat effect only under high efficacy (d = 0.31), efficacy effect only under high threat (d = 0.71). This file's section 7 says no threat x efficacy experiment crossing levels is available and section 3 treats the interaction evidence as only the Bigsby table; it never cites Peters 2013, which is the closest published factorial-design test and supports the interaction (and, with a null threat effect at low efficacy rather than a negative one, bears on the sign-flip reading). Agrees in direction with section 3's mean difference of +0.55; it should be cited. Note it is also a 2 x 2-type design, so it faces section 5's identifiability limit. Verdict: file 35 is the source to cite; this file's "does not exist" in section 7 stands only for 3+ x 3+ levels and for raw data.
3. **Wurtele & Maddux 1987 vs Peters 2013 pattern.** This file section 3: the only full efficacy-crossed 2 x 2 in table 1 has its largest threat effect (1.42) in the no-efficacy cell, "contradicts both product and EPPM". File 35 (Peters 2013): threat effect only at high efficacy. Verdict: **unresolved**; one small study (N = 40 per cell) against a six-study pooled result, and the Wurtele cell flags are not Peters' inclusion set. Not checked against the primary papers in this pass.

No numerical contradictions were found on any figure that appears in both files. No web primary-source checks were needed beyond the Crossref re-check of the Milne and Floyd records above.

## Licences of quoted and transcribed material (2026-10-30)

- **Bigsby & Albarracín 2022**, *J. Communication* 72(2), 241-263, DOI 10.1093/joc/jqab048. Licence: not determined; publisher copyright presumed (OUP; licence of the PMC copy PMC12437762 not recorded). Use: two short quotations of the paper's coding definitions (4 and 13 words), now attributed in the text of section 3, plus a one-word quotation ("surprising") and restated findings and numbers.
- **OSF node h9fyd** (Bigsby, Albarracín, O'Keefe; files `Table 1 Data.xlsx`, `Table 2 Data.xlsx`). Licence: none stated (OSF `node_license` null); not determined, so no reuse permission is assumed. Use: dataset citation, summary statistics computed by us, and a 15-row table in section 3 of the within-study low-vs-high contrasts (17 pairs of d values). Flagged "check": values are facts and left unchanged, but the licence question should be answered (ask the authors) or the table reduced to a description before the repo is opened.
- **OSF node wcxvg** (Kaspar & Keller; `data.xlsx`, `Codebook.xlsx`, `data_analysis_osf.R`, preregistration). Licence: none stated. Use: dataset citation and aggregate statistics we computed (means, R2, AIC differences, coefficients, bootstrap interval); no rows reproduced. Flagged "check": confirm the statistics may stay before open-sourcing.
- **OSF nodes y45mb, a2v46, sdp5h** (catalogue rows C, D, E). Licence: none stated. Use: dataset citation only; not used in analysis.
- **Tannenbaum et al. 2015, Witte & Allen 2000, Floyd et al. 2000, Milne et al. 2000** (and Crossref records). Licence: not determined; publisher copyright presumed. Use: citation and restated study-level facts only; no text or tables reproduced.
