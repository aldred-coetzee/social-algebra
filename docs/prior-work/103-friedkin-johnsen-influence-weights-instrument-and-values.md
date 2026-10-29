# Prior work 103: how Friedkin and Johnsen measured the influence weights, and what values they take (chapter 4 is paywalled; the instrument is read at source in the same authors' open work)

Direction: D595

Date: 2026-10-29. Kind: deep-read. Question: in Friedkin & Johnsen 2011, *Social Influence Network Theory*, ch. 4, how were the influence weights a_ij measured in groups, with what instrument, and what fitted values came out, so that v0's signed weights have an empirical referent. Cross-references 05, 63, 74, 87, 90, 91.

## Short answer

1. **Chapter 4 itself could not be read.** It is paywalled (Cambridge Core shows only a summary and one sentence; Unpaywall and OpenAlex both say closed; no author-hosted copy turned up). I did not use unauthorised copies. Every claim about what chapter 4 contains is therefore [sa] from the publisher's summary.
2. **The instrument is read at source anyway**, in the same authors' later open-access paper and its supplement: Friedkin, Jia & Bullo 2016 uses "the same design" as the book (their words), and the supplement prints the chip form. The weights are **post-discussion self-reports: 100 chips divided among the other group members, plus a "did not influence me" pile that becomes the self-weight.** Nonnegative, row-sum 1.
3. **Fitted values from chapter 4 are not obtained.** What is read: the mean self-weight in tetrads (about 0.64), and prediction accuracy of the model with measured W (correlation 0.87 with final opinions).
4. **For v0:** the instrument cannot produce a negative weight, so **signed weights have no referent in this tradition's data.** Do not cite Friedkin-Johnsen as an empirical basis for a negative a_ij. It supports only nonnegative, row-normalised, self-reported influence on one scalar opinion in groups of 2 to 4.

## 1. Citations and verification

| Work | Citation | Verified |
|---|---|---|
| Friedkin & Johnsen 2011 | Friedkin, N. E. & Johnsen, E. C. (2011). *Social Influence Network Theory: A Sociological Examination of Small Group Dynamics.* Cambridge University Press. doi:10.1017/CBO9780511976735 | Crossref resolves (monograph, ISBN 9780511976735 online). |
| Ch. 4 | "Assessing the Model", pp. 80-112. doi:10.1017/CBO9780511976735.005 | Crossref resolves, pages 80-112. Cambridge Core page: summary only. Unpaywall: `oa_status closed`, no repository copy. |
| Front matter | Preface, table of contents, list of tables and figures; free PDF at assets.cambridge.org (9781107002463_frontmatter.pdf) | Fetched and read in full. |
| Friedkin, Jia & Bullo 2016 | "A theory of the evolution of social power: natural trajectories of interpersonal influence systems along issue sequences." *Sociological Science* 3, 444-472. doi:10.15195/v3.a20 | Crossref resolves (Friedkin, Jia, Bullo; 2016; 3:444-472). Open PDF read in full; supplement `SocSci_v3_444to472_supp.pdf` read in section S3. Licence: Creative Commons Attribution, stated on the article's first page (corrected 2026-10-30; this row first said no licence was stated). Credit: Friedkin, Jia & Bullo, *Sociological Science*, CC BY. |
| Friedkin & Bullo 2017 | "How truth wins in opinion dynamics along issue sequences." *PNAS* 114(43), 11380-11385. doi:10.1073/pnas.1710603114 | Crossref resolves. PNAS site returned 403; PMC5664530 page was fetched through a summarising fetch tool, so its numbers are tagged [fetched, summarised] and nothing here depends on them. |
| Bruggeman 2018 | Bruggeman, J. (2018). "Consensus, cohesion and connectivity." *Social Networks* 52, 115-119. doi:10.1016/j.socnet.2017.06.001 (arXiv:1602.00614v8) | Crossref resolves; issue dated January 2018 (online 2017; the DOI carries 2017, which is where the earlier "2017" came from). Read the susceptibility sentence and its three references in the arXiv v8 text, not the journal version. |
| Ravazzi et al. 2018 | Ravazzi, C., Hojjatinia, S., Lagoa, C. M. & Dabbene, F. (2018). "Randomized opinion dynamics over networks: influence estimation from partial observations." arXiv:1804.07220 (preprint; authors confirmed on the arXiv record) | Read the one sentence on how the weights were "measured". A secondary description of the instrument, consistent with the primary one. |

## 2. Provenance

| Item | Tag |
|---|---|
| Chip instrument wording and procedure (supplement S3) | [read] primary |
| Model equations 1-8 as used in FJB 2016 | [read] |
| FJB 2016 prediction tables 1-3, design, n | [read] |
| Ch. 4 contents (experiments on dyads, triads, tetrads; standard vs optimized model; fitted vs reported susceptibilities) | [sa] from the Cambridge summary, re-fetched 2026-10-30 and consistent; the table of contents and figure list [read]. The figure list adds that the experiments used **communication networks** in tetrads, triads and dyads (Fig. 4.1), so not every pair could talk directly |
| Ch. 4 fitted susceptibilities, subjective-weight match, baseline comparison results | **not obtained** |
| PNAS 2017 numbers | [fetched, summarised] |

## 3. The instrument [read]

**Design (FJB 2016, "Experiment Design and Measurement Models").** Subjects are randomly assigned to small groups (dyads, triads or tetrads). An issue is posed. Each subject records an initial position privately. A group discussion is opened and ends when the group has reached settled opinions. After discussion, each subject reports final opinion and fills the influence form. FJB state that Friedkin and Johnsen "elaborated the design" with the post-discussion self-report, and that FJB use "the same design" as the book.

**Issues.** Choice dilemmas (Stoner 1961, a master's thesis; Wallach, Kogan & Bem 1962, *J. Abnormal and Social Psychology* 65:75-86, as cited in the FJB supplement): the minimum chance of success the subject would require before choosing a riskier, more rewarding option, on a 0 to 100 percent scale in steps of 5. In FJB each group of four discussed 15 issues drawn from 18, in random order.

**Influence form, restated from supplement S3 [read].**
- Step one: the subject imagines 100 chips, "each chip represents influence upon your final opinion". Pile 1 is the extent to which the discussion influenced the final opinion; Pile 2 is the extent it did not. The two total 100.
- Step two: the Pile 1 chips are distributed among the three other group members, labelled by seat. A person who did not influence the subject gets none. The allocation should show the extent of each person's influence on the subject's opinion.

**From chips to W [read, main text].** FJB divide the chips allocated by i to j by 100 to give a distribution of relative weights, and the main-diagonal value w_ii is the measure of closure to influence and "ongoing attachment to his or her initial opinion". The model then sets a_ii = 1 - w_ii, the "openness to influence". The text says the weights are w_ij with 0 <= w_ij <= 1 and the sum over j of w_ij = 1 for each i. By the form, w_ii is the Pile 2 share and the off-diagonal w_ij are the Pile 1 chips given to j, over 100.

**Properties of this instrument, stated flatly.**
- **Nonnegative by construction.** A chip count cannot be negative. There is no way to report "this person pushed me away from where they stood". Disliking, contrarianism or reactance would be reported, at best, as zero.
- **Row-normalised by construction.** Whatever i gives to j is taken from what i can give to others and to self. Influence is zero-sum within a row. That is a property of the form, not a finding about people.
- **Retrospective and self-reported.** It is collected after the final opinion is given, and asks about influence "upon your final opinion". It measures reported realised influence on one outcome, not a standing susceptibility to a specific source. The same subject on another issue gives another W (section 6).
- **One scalar issue at a time.** Each W belongs to one issue.
- **Ties the diagonal to the weights.** a_ii = 1 - w_ii is an assumption of the "standard model". Per the Cambridge summary, chapter 4 also fits an "optimized model" in which susceptibilities are estimated, and compares them with the subjects' reported self-weights. Parsegov et al. and Proskurnikov and Tempo (file 63) decouple the two.

## 4. The model that the weights feed [read, FJB 2016 eqs 1-8]

For n members, with A = diag(a_ii), a_ii = 1 - w_ii, and W the row-stochastic chip matrix:

    x(k+1) = A W x(k) + (I - A) x(0)
    V = sum over k of (A W)^k (I - A) = (I - A W)^{-1} (I - A)        (when 0 < A < I)
    x(inf) = V x(0),  V row-stochastic, entries in [0,1]
    influence centrality of j:  C_j = (1/n) * sum over i of v_ij        (sums to 1)

"With no fitting", FJB write, the predicted final opinions are x(inf) = V x(0): W is measured, not estimated. This is the same equation file 63 records from Hegselmann and Krause, written in Friedkin's notation. Nothing new at the level of equations; the new content is the instrument.

## 5. Values and fit that are read

All from FJB 2016, 30 tetrads (n = 4), 15 issues each, undergraduates at a large US West Coast university, randomly assigned [read].

- **Mean self-weight.** In the regression of w_ii(s+1) on prior issues (issues 2 to 15, n = 1,680 person-issue observations), the constant-only model has constant **0.643** (standard error 0.016) [read, Table 2 col. a]. So the typical subject reports about 64 percent of the weight on the own initial position, 36 percent spread over the other three. The four-person ceiling noted in FJB: the weight a_ii w_ii that i gives to own updated opinion has maximal value 0.25.
- **Prediction with measured W.** Observed vs predicted final opinion: Pearson 0.872; observed vs predicted opinion change 0.811; an alternative predictor of change, 0.915 [read].
- **Regression of observed final opinion on the F-J prediction** (n = 1,800, random-intercept multilevel; Table 1): slope 0.897 (se 0.018) with constant 5.53 in col. b; adding initial opinion gives F-J slope 1.157 (se 0.032) and initial-opinion coefficient -0.282 (se 0.031), log likelihood moving from -8579.8 (constant only) to -7329.0 to -7241.1 [read]. Read: the prediction is strongly informative, but with the initial opinion included the F-J prediction is over-scaled (slope above 1) and initial opinion has a negative residual coefficient, so the model underweights movement away from where people started.
- **Observed settlement times** 3 to 27 minutes, median 11 [read]; the model's predicted convergence time is a log iteration count.
- **PNAS 2017** [fetched, summarised]: 161 subjects in 45 groups (19 triads, 26 tetrads), eight problems, 1,288 individual observations; correlation of observed and predicted final opinions 0.939, of changes 0.873. It reports no susceptibility value. Treat as indicative only.

## 6. Group size, composition and stability of the weights

- **n.** Everything read is n = 2 to 4. FJB are n = 4 only. The book's experiments are dyads, triads and tetrads [sa]. The instrument gives a full n x n matrix, which is why it is feasible only for small n; Ravazzi et al. 2018 say that the chip method is "not viable in case of large networks" [read, one sentence]. **No weight was measured in a group above 4 in anything read.** Self-weight at n = 4 (0.64) cannot be carried to larger n: chips are split over n - 1 others, so row-sum structure changes with n.
- **Composition.** Undergraduates, strangers, randomly assigned, a single short-session task with no stakes and no shared past. No kin, no hierarchy, no existing relationships. FJB also vary a consensus pressure (high or low), imposed over all 15 issues of a group [read, S3]; the effect of that pressure on the weights was not located in the text I read.
- **Weights are not constants.** FJB's central finding is that a person's closure w_ii on the next issue rises with their influence centrality on the last: the effect of C_i(s) on w_ii(s+1) is 0.336 (se 0.104), and of the time-average T_i(s) is 0.404 + 0.095 s [read, Table 2]. Caveat on the source, found in validation: Table 2 col. b also prints an s x C_i(s) interaction of 0.171 (se 0.012) with no significance mark, while the text says the C_i effect is "constant along the issue sequence"; the table and text do not agree, so quote the 0.336 with that caveat. Self-weights polarising toward n - 1 at 0 and one at 1, "with rare exceptions", is the result of the authors' computational analyses of the model (supplement S1), reported in the main text [read]; it is a property of the model, not an observation. So an a_ij is **a state variable that moves with outcomes of the process**, not a parameter of a pair. An equation that fixes a_ij is, on the authors' own data, a one-issue snapshot.
- **Scale of every result.** Membership: not studied. **Group: decision and opinion settlement in 2 to 4 person groups on a scalar judgement; the unit is the person-issue.** Crowd: none. Intervention: none in the data read. The consent-or-manipulation question does not arise as an intervention; the only manipulation is the consensus-pressure instruction, which is a manipulation of the setting by the experimenter, not an influence strategy.

## 7. A figure to avoid

Bruggeman 2018 (arXiv v8) writes that susceptibility "turned out to be in the range 0.3 to 0.5 under experimental conditions", citing three papers (Moussaïd et al. 2015; Moussaïd et al. 2013; Soll and Larrick 2009) [read]. Those are advice-taking and judgement-revision experiments, **not Friedkin-Johnsen chip data**. It is not a Friedkin-Johnsen value. (Corrected 2026-10-30: this line first said the range "sits oddly" with the 0.36 off-diagonal share read above, 1 - 0.643; 0.36 lies inside 0.3 to 0.5, so the two agree numerically. The agreement is a coincidence of two different instruments, not a confirmation.) Do not quote it as a fitted a_ii for this tradition.

## Does it reduce to a drive basis?

**What reduces, loosely.** The diagonal. w_ii, the weight on one's own initial position, is a person-level quantity that behaves like a stubbornness or closure parameter. It can be read as a single scalar of a person: how strongly the person is anchored to what they already hold. On the data read it is itself moved by outcomes (success at influencing raises it), so it looks like a drive-like state with feedback. This is a reading imposed by us. Friedkin and Johnsen call it a cognitive weighing, a "dynamic social cognition mechanism" [read, Preface], not a drive; nothing in the instrument distinguishes closure from, say, confidence, status or fear of losing face.

**What does not reduce.**
- The off-diagonal weights a_ij. They are reports of who influenced whom on one issue; there is nothing in the instrument that says why. They could arise from competence, status, liking, attention, seating or speaking time, and the form does not separate these. Mapping them to a drive of the influenced person (curiosity, fear, affiliation) would be an addition, not a reading.
- The row-sum constraint. It makes influence a conserved resource within a person; no drive structure explains it. It is how the form is filled in.
- Everything signed. No negative weights are measured.
- The unit of analysis. The model is about positions on a scalar issue, not about states of a person at all.

So: the F-J weights are an **interaction-structure** primitive (a coupling matrix reported by the members), with one diagonal entry that has a drive-like reading. The hypothesis that drives are the primitives is neither supported nor refuted by this tradition. It says nothing about drives.

## What does it predict or control, and how well?

- **Predicts:** the final position of each member after discussion, given the initial positions and each member's own post-discussion chip report. Correlation 0.872 with observed final opinion, 0.811 with changes, in 30 tetrads over 15 issues; the PNAS 2017 summary reports 0.939 and 0.873 in 45 triads and tetrads [fetched, summarised].
- **Out-of-sample:** not in the sense a drive modeller needs. The same group of authors reports the same kind of fit across their own experiments (FJB: "as they have in previous experiments"), but W is collected **after** the discussion and refers to influence on the final opinion, which is the quantity being predicted. The prediction is therefore not a forecast made from information available before the discussion. Predicting W in advance from anything else is not done in anything I read (the 2018 Ravazzi et al. estimation work starts from the same problem). The book's baseline (mean of initial opinions) comparison is in chapter 4 and was not read.
- **Effect size:** the correlations above are of a model that is given a lot of the answer (initial opinion carries most of final opinion in these data; I could not find a no-influence baseline correlation in the text I read, so I cannot say how much the weights add). Slope 0.897 and 1.157 depending on the controls; with initial opinion in the model the coefficient on it is -0.282, so the model does not fully capture its own dependence on the start.
- **Controls / interventions:** none tested in the data read. The theory implies leverage (a change in one member's loop value changes all flows in a strongly connected group), and FJB's data show closure rising with earlier influence, i.e. the system is self-reinforcing toward one dominant member. That is a prediction about the weights' dynamics in tetrads, tested on 30 groups of student strangers.
- **Failures and limits:** n of 2 to 4 only; single scalar issue; strangers in a lab; weights measured from the people being predicted; nonnegative weights only; no replication by an independent group found in this session (every study read is Friedkin's group; independent tests are for D210).

## Unconfirmed

- Everything in chapter 4: the three experiments' sample sizes and details, the fitted susceptibilities, their match to subjective self-weights, the baseline comparison, the dyad and triad results.
- Whether the book's design is exactly the supplement's chip form (FJB say "same design"; a reader of the book should check).
- The PNAS 2017 numbers beyond the summary.
- Any effect of the consensus-pressure condition on the weights.
- Whether any independent group collected chip-type influence matrices. Tested 2026-10-30 with two web searches: none found; the nearest, Moussaïd, Noriega Campero & Almaatouq 2018 (*PLOS ONE*, PMC5770023), models influence networks in triads but was not checked for a chip instrument, so this is "not found", not "does not exist".

## Ledger recommendation

Mark the claim that "F-J weights have been measured" as true only for: nonnegative, row-stochastic, post-discussion self-reported weights, n = 2 to 4, one scalar issue. Mark "signed or antagonistic weights measured in groups" as **no source found here**. Re-open chapter 4 only through a library copy; if one is available, the items to extract are the fitted susceptibility distributions (Figure 4.4, histograms by group size; Table 4.10), the derived-versus-reported susceptibilities (Figure 4.3), the baseline comparison, the dyad versus tetrad comparison, and the communication-network conditions (Figure 4.1).

Sources opened: Cambridge Core chapter page, Cambridge front-matter PDF, FJB 2016 PDF and supplement, arXiv 1602.00614 and 1804.07220 (relevant sentences), PMC5664530 (summarised), Crossref and OpenAlex and Unpaywall records.

## Validation log (2026-10-30)

- ✓ Friedkin & Johnsen 2011, book: Crossref resolves doi:10.1017/CBO9780511976735, CUP, 2011; the abstract carries "dynamic social cognition mechanism", as quoted.
- ✓ Chapter 4 "Assessing the Model", pp. 80-112, doi:...005: Crossref resolves. The Cambridge summary was re-fetched (paywalled; summary only) and agrees with the file. Every ch. 4 claim stays [sa].
- ✓ Front matter PDF: re-read. Figure 4.4 is "Histograms of derived susceptibility values in dyads, triads, tetrads". ✎ Added Fig. 4.1 (communication networks), Fig. 4.3 and Table 4.10 to the items to extract.
- ✎ Friedkin, Jia & Bullo 2016: DOI, authors and pages confirmed. Main PDF and supplement S3 re-read. Every number in sections 3-5 was checked against the text: 0.643 (0.016), n = 1,680, 0.872, 0.811, 0.915, 0.897 (0.018), 1.157 (0.032), -0.282 (0.031), log-likelihoods, 3-27 min with median 11, the 0.25 ceiling, the chip form, 15 of 18 issues, the 5% scale steps, the "same design" and "with no fitting" wording. ✎ Two corrections: the licence is CC BY (the file had said none was stated); and the Table 2 interaction s x C_i = 0.171 contradicts the text's "constant" effect, now flagged. ✎ The polarisation result is now labelled as the model's computational result.
- ✎ Friedkin & Bullo 2017 PNAS: Crossref confirms 114(43):11380-11385. The PMC text was blocked to direct fetch. The summarising fetch again gave 161 subjects, 45 groups (19 triads and 26 tetrads), 8 problems, 1,288 observations, 0.939 and 0.873, and these agree with each other (161 x 8 = 1,288). The tag stays [fetched, summarised].
- ✎ Bruggeman: year corrected from 2017 to 2018 (Social Networks 52, January 2018 issue). The susceptibility sentence was read verbatim in arXiv v8, with refs 13, 17 and 18 = Moussaïd et al. 2015 PNAS, Moussaïd et al. 2013 PLOS ONE, Soll & Larrick 2009 JEP:LMC, as stated. ✎ The section 7 claim that 0.3-0.5 "sits oddly" with 0.36 was wrong, because 0.36 is inside the range. Corrected.
- ✓ Ravazzi, Hojjatinia, Lagoa & Dabbene 2018: arXiv record confirmed. "not viable in case of large networks" was read verbatim. Authors added.
- ✓ Stoner 1961 and Wallach, Kogan & Bem 1962: cited as the FJB supplement cites them. Not opened, and nothing load-bearing rests on them. ✎ Wallach's co-authors added.
- ? Independent chip-matrix replication: searched, none found. It stays in Unconfirmed, with the nearest candidate named.

Sources opened this pass: 7. Read myself: FJB 2016 main PDF, FJB supplement, Bruggeman arXiv v8, Ravazzi arXiv, the CUP front-matter PDF. Seen only in part: the Cambridge chapter summary page, and PMC5664530 through a summarising fetch. Also opened: 5 Crossref records, the arXiv API and 2 web searches.

Verdict: the file is accurate where it says [read]. Every number from FJB 2016 matches the source, and the central conclusion holds: the chip instrument cannot yield a negative or non-row-normalised weight. Four things were corrected: the Bruggeman year, the FJB licence, a false "inconsistency" in section 7, and an unflagged table-versus-text conflict in FJB Table 2. Nothing was fabricated. Chapter 4 remains unread (paywalled), so no fitted book value may feed an equation; the 0.643 self-weight is [read], but only for student tetrads.

## Cross-checks (2026-10-30)

Checked against the other prior-work files by grep for the same authors (Friedkin, Johnsen, Bruggeman, Ravazzi, Moussaid, Soll, Parsegov, Proskurnikov), the same equations and the same numbers. Files read at the lines cited: 05, 063, 074, 090, 102.

**Agreements**
- The FJ map and its fixed point, x(inf) = (I - AW)^{-1}(I - A) x(0), match 05 section 4 (line 96), 090 section 3 (Part II eqs 43-44), 074 section 4.1, and 063 section 3.2 (H&K Theorem 3 with M = (I - G)A, G = I - A). Same object in four notations.
- The convention a_ii = 1 - w_ii matches 05 section 4 ("Friedkin's own specification"), and 063 section 2 (stubbornness g_i = 1 - lambda_i, so w_ii = stubbornness, a_ii = susceptibility). 05 and 074 both say the tie is an assumption, not a law; 103 agrees, and says chapter 4 fits an optimized model that decouples the two.
- The "validated for small and medium-size groups" sentence (P&T 2017 section 6, quoted in 063 section 7, 090 section 5, 05 section 4) is consistent with 103: every measured W read is from Friedkin's own group (FJB 2016, Friedkin a co-author). Independence is still open, as the other files say.
- 090 line 204 (narrowed 2026-10-30) reports the same chip-allocation design for dyads, triads and tetrads, tagged [sa]. 103 reads the primary source (FJB 2016 supplement S3), so the tag there can be upgraded to [read] for the instrument; the chapter-4 claim stays [sa].
- No file reports a negative or signed influence weight measured in a group. 090 section 5 and 05 section 4 say the basic form has no negative influence. Consistent with 103's "no source found".
- 074 section 4.1 calls distinct self-weights "a strong assumption for a social group". 103 gives person-level, state-dependent closure (C_i effect, Table 2), so self-weights are not fixed per person. This supports 074's caution without contradicting it; 103 reports no between-person variance, so it does not settle how far apart the self-weights are.
- No file cites Ravazzi et al. 2018 or Bruggeman 2018 with a claim that conflicts with 103. Moussaid appears in 29 (human crowds, unverified), which is not the Moussaid 2013 judgement study 103 cites.

**Contradictions, recorded not resolved**
- C1. 103 section 6 and ledger: "signed or antagonistic weights measured in groups: no source found". 102 section 1 (via Doreian & Mrvar 2015 section 2.3 [sa]) reports a signed friend/enemy sentiment network in the Newcomb fraternity data, measured in a group (Doreian & Krackhardt 2001). Possible reading: sentiment (liking) is not influence, so the two claims are about different quantities. Unresolved; both claims stand as written.
- C2. 063 section 7 (line 196): "the only FJ-family model tied to measured data that I could see is Parsegov et al. Example 2" (four persons, W from Friedkin & Johnsen 1999, [15] in Parsegov). 103: 30 tetrads with measured chip W (FJB 2016), which 063 did not cite. Likely a scope gap in 063 rather than a conflict. Unresolved; 063 is not edited here.
- C3. Internal to 103: Table 2 col. b interaction s x C_i(s) = 0.171 (se 0.012, unmarked) against the text's "constant along the issue sequence". Already flagged in 103 section 6 and the validation log; not resolved there, not resolved here.

**Ledger lines** (the file's own provenance tags kept; [sa] items and [fetched, summarised] are marked as such)

Drives. None named in the source. The closure weight w_ii ("ongoing attachment to his or her initial opinion") is a candidate drive-like scalar. That is this file's reading, not the source's.

Equations and definitions:
- x(k+1) = A W x(k) + (I - A) x(0), with A = diag(a_ii), a_ii = 1 - w_ii [read, FJB 2016 eqs 1-8]. Dup of 05 section 4 line 96, 063 section 3.2, 090 section 3, 074 section 4.1.
- V = (I - AW)^{-1}(I - A); x(inf) = V x(0); V row-stochastic [read]. Dup of the same four.
- Influence centrality C_j = (1/n) sum_i v_ij [read]. Not duplicated. Related to Golub-Jackson's leverage vector pi (05 section 2, line 79), which is a different quantity and not stated as the same.
- W from chips: w_ij = chips i gives j / 100, w_ii = Pile 2 / 100; row-stochastic and nonnegative [read, FJB 2016 and supplement S3]. The generic definition is dup of 05 section 2 line 77; the chip mapping is new.
- a_ii = 1 - w_ii, "openness" a_ii and "closure" w_ii [read]. Dup of 05 section 4 line 96 and 063 section 2 line 48 (stubbornness = 1 - lambda).

Empirical results (group scale, n = 2 to 4 only, all Friedkin's group, all undergraduate strangers):
- Mean self-weight 0.643 (se 0.016), constant-only regression of w_ii(s+1), 30 tetrads, n = 1,680 person-issues [read, FJB 2016 Table 2 col. a]. Size dependence: n = 4 only; the chip split changes with n. Not duplicated.
- Predicts observed final opinion with measured W: Pearson 0.872; changes 0.811; an alternative predictor of change 0.915 [read]. Controls: initial opinion carries most of the outcome, no no-influence baseline correlation was read. Not duplicated.
- Regression of final opinion on F-J prediction (n = 1,800, multilevel): slope 0.897 (0.018) with constant 5.53; with initial opinion the F-J slope is 1.157 (0.032) and the initial-opinion coefficient -0.282 (0.031) [read, Table 1]. Not duplicated.
- Influence centrality of i at s on closure at s+1: 0.336 (se 0.104) [read, Table 2; see C3]. Not duplicated.
- Settlement time 3 to 27 minutes, median 11 [read]. Not duplicated.
- PNAS 2017: 161 subjects, 45 groups (19 triads, 26 tetrads), 8 problems, 1,288 observations; r 0.939 final, 0.873 change [fetched, summarised]. Not duplicated.
- Chapter 4 experiments (dyads, triads, tetrads; standard vs optimized model; fitted susceptibilities) [sa]. Dup of 090 line 204 (same [sa] claim); the fitted values were not obtained.
- Chip method "not viable in case of large networks" [read, Ravazzi et al. 2018, one sentence]. Scope claim about n. Not duplicated.
- Bruggeman 2018: susceptibility "0.3 to 0.5 under experimental conditions" [read, arXiv v8]. Advice-taking studies (Moussaid 2015, Moussaid 2013, Soll & Larrick 2009), not FJ data. Not duplicated; do not quote as a_ii for this tradition.

Scale and ethics: all empirical lines are group scale; no membership, crowd or intervention data read. Ethics: no manipulation by the authors beyond the consensus-pressure instruction (S3), which was not located in the text read. Marked n/a throughout; the consent status of the student participants was not checked.

Cluster letter not assigned here.

Not committed. Only this file was edited.
