# Prior work 088: negativity-threshold sign, divorce-prediction accuracy, and which love ODEs were ever fitted

Direction: D187
Date: 2026-10-29. Kind: cross-check (with a data catalogue of the accuracy figures). Questions: (1) which couples had the lower negativity threshold; (2) what are the real divorce-prediction accuracies and how were they obtained; (3) which coupled-ODE love models were ever fitted to data. Cross-references: `059` (read the same 1999 paper; this file re-reads it independently), `20-dyadic-coupling.md` sections 1-2 (superseded on the threshold sign, see 059), `080`, `079`, `060`, `061`.

**Method and honesty note.** PDFs were downloaded and extracted with `pdftotext`, then the quoted passages read. Tags: **[read]** = primary text fetched and read by me; **[read: press]** = a university press release read, not the paper; **[abs]** = abstract/record only; **[sa]** = secondary account, not read at source; **[derived]** = my arithmetic from stated figures, not in the source. Nothing tagged [sa] or [abs] is used to fix an equation or a number below.
Not obtained: Gottman, Coan, Carrere and Swanson 1998; Strogatz 1988 (the only copy found was on a host that refused the connection) and Strogatz 1994; Kim, Capaldi and Crosby 2007 (abstract only; PMC served a bot-check page); Madhyastha, Hamaker and Gottman 2011 (abstract only); Steele, Ferrer and Nesselroade 2014 (abstract only).
*Validation pass (2026-10-30) obtained and read four texts the first pass did not:* Heyman and Slep 2001 (the PMC article page, fetched as plain HTML), Carrere et al. 2000, Carrere and Gottman 1999, and Buehlman, Gottman and Katz 1992 (all three as PDFs from johngottman.net). Their tags are upgraded below and the numbers corrected where they differed.

## Summary

1. **Threshold sign: settled, and 059 is right.** In Gottman, Swanson and Murray 1999, couples who later divorced had a more negative husband negative threshold (mean -7.71 vs -5.36, F(1,123) = 8.25, p < .01). A husband had to become more hostile before the wife's behaviour moved. Stable couples respond to milder negativity. [read]. The ambiguity is in the paper's own wording: its **abstract** says the divorcing couples had a "lower negative threshold" (lower on the number line, i.e. more negative), while the **body** says that if the threshold "is set lower (a smaller negative number on the x-axis)" for stable marriages this is the "marital negativity detector" effect. The same word "lower" is used for opposite ends in the same paper. Only the husband's threshold was significant; the wife's was not (F = 0.03). In the three-group analysis (happy stable, unhappy stable, divorced) the threshold was not significant (F = 2.22) and not monotone (-5.94, -5.29, -7.71).
2. **No divorce-accuracy figure I could trace is an out-of-sample test.** Every classification percentage in the Gottman-Levenson papers I read is a discriminant function (or group comparison) fitted and scored on the same couples, with predictors selected by univariate significance on the same data. Where the paper gives enough counts, the headline accuracy is often no better than, or below, the accuracy of always answering "stays married" (section 3; this includes both Carrere et al. 2000 figures, 87.4% against a null of 92.6% and 81% against 83.2%). The one cross-validation study (Heyman and Slep 2001, on other data) was read in the validation pass: positive predictive value fell from 65% on the build half to 29% on the hold-out half, and to 21% at a realistic 16% prevalence [read].
3. **The 94% / 93.6% figure belongs to a different instrument and sample from the one the threshold model uses.** It is Buehlman, Gottman and Katz 1992, an Oral History Interview coding study of families with a 4-5-year-old child (56 recruited, 52 reported), 3-year follow-up, not the lab conflict-discussion model (section 3.4). The 93.6% is 44 of **47** couples classified in-sample by a nine-predictor discriminant function, with 7 divorces; always answering "stays married" scores 40/47 = 85.1% [read]. Gottman's own FAQ says the 94% claim "has become a source of confusion".
4. **No coupled-ODE love model has been fitted to data in the strict sense.** Strogatz (teaching model), Sprott (explicitly illustrative) and Bielczyk et al. (pure theory) have no data. Rinaldi 1998 calibrates by hand, from "personal estimates", against 23 subjectively graded poems, with one fitted scalar (a 20% time stretch). What *has* been fitted are Gottman-Murray's coupled *difference* equations (per couple), a threshold-autoregressive re-estimate of them on three dyads, and, by abstract only, dyadic differential-equation models on daily affect ratings (Steele et al. 2014; the abstract does not say "latent" or "oscillator", which the first pass added). The independent fits that exist point toward *weak or absent* partner coupling (section 4). The claim covers the Strogatz-Sprott-Rinaldi line only; other dyadic affect ODEs have been fitted (section 6, validation note).

---

## 1. Citations (DOIs resolved on Crossref 2026-10-29)

- Gottman, J. M., Swanson, C., and Murray, J. D. (1999). The mathematics of marital conflict: dynamic mathematical nonlinear modeling of newlywed marital interaction. *J. Family Psychology* 13(1):3-19. doi 10.1037/0893-3200.13.1.3. [read: abstract, theory section, results, Tables 1-2]
- Gottman, J. M., and Levenson, R. W. (1992). Marital processes predictive of later dissolution: behavior, physiology, and health. *JPSP* 63(2):221-233. doi 10.1037/0022-3514.63.2.221. PDF on the Berkeley Psychophysiology lab site (bpl.studentorg.berkeley.edu/docs/). [read: method, results, Table 3, discriminant section]
- Gottman, J. M., and Levenson, R. W. (1999). Rebound from marital conflict and divorce prediction. *Family Process* 38(3):287-292. doi 10.1111/j.1545-5300.1999.00287.x. [read in full]
- Gottman, J. M., and Levenson, R. W. (2000). The timing of divorce: predicting when a couple will divorce over a 14-year period. *J. Marriage and Family* 62(3):737-745. doi 10.1111/j.1741-3737.2000.00737.x. [read: methods, results, discussion; OCR is rough]
- Buehlman, K. T., Gottman, J. M., and Katz, L. F. (1992). How a couple views their past predicts their future: predicting divorce from an oral history interview. *J. Family Psychology* 5(3-4):295-318. doi 10.1037/0893-3200.5.3-4.295 (Crossref-confirmed). PDF at johngottman.net. [read: abstract, subjects, procedures, results, Table 7] (added in validation; this is the source of the 93.6%.)
- Gottman, J. M., and Levenson, R. W. (1999). What predicts change in marital interaction over time? A study of alternative models. *Family Process* 38(2):143-158, doi 10.1111/j.1545-5300.1999.00143.x (Crossref-confirmed). Its companion "How stable is marital interaction over time?" is 38(2):159-165, doi 10.1111/j.1545-5300.1999.00159.x (downloaded, not used). [read: the passages quoted in section 3.4 and footnote 1 only]
- Gottman, J. M., Coan, J., Carrere, S., and Swanson, C. (1998). Predicting marital happiness and stability from newlywed interactions. *J. Marriage and the Family* 60(1):5- (Crossref gives first page 5 only; the papers that cite it give 5-22 and 5-27). doi 10.2307/353438. [not read]
- Carrere, S., Buehlman, K. T., Gottman, J. M., Coan, J. A., and Ruckstuhl, L. (2000). Predicting marital stability and divorce in newlywed couples. *J. Family Psychology* 14(1):42-58. doi 10.1037/0893-3200.14.1.42. [read in validation: abstract, predictive-validity section; PDF at johngottman.net]
- Carrere, S., and Gottman, J. M. (1999). Predicting divorce among newlyweds from the first three minutes of a marital conflict discussion. *Family Process* 38(3):293-301. doi 10.1111/j.1545-5300.1999.00293.x. [read in validation: abstract, results pp. 296-298, Tables 2-3; scanned PDF read page by page]
- Heyman, R. E., and Smith Slep, A. M. (2001). The hazards of predicting divorce without crossvalidation. *J. Marriage and Family* 63(2):473-479. doi 10.1111/j.1741-3737.2001.00473.x. PMC1622921. [read in validation: introduction, method, results, Tables 1 and 3]
- Kim, H. K., Capaldi, D. M., and Crosby, L. (2007). Generalizability of Gottman and colleagues' affective process models of couples' relationship outcomes. *J. Marriage and Family* 69(1):55-72. doi 10.1111/j.1741-3737.2006.00343.x. PMC1828692. [abs]
- Coan, J. A., and Gottman, J. M. (2007). Sampling, experimental control, and generalizability in the study of marital process models. *J. Marriage and Family* 69(1):73-80. doi 10.1111/j.1741-3737.2006.00344.x. [existence and authorship from Crossref only; not read] (added in validation: the first pass said this reply was "not found".)
- Kim, H. K., and Capaldi, D. M. (2007). Generalizability issues in observational studies of couples: sample characteristics and task design. *J. Marriage and Family* 69(1):86-91. doi 10.1111/j.1741-3737.2006.00346.x (Crossref lists these two authors). [not read]
- Matthews, L. S., Wickrama, K. A. S., and Conger, R. D. (1996). Predicting marital instability from spouse and observer reports of marital interaction. *J. Marriage and the Family* 58(3):641-. doi 10.2307/353725. [Crossref only; not read] (added in validation: Carrere and Gottman 1999 cite it as the replication "in another laboratory", which is very likely the Iowa State work the FAQ refers to.)
- Gottman Institute, Research FAQ, gottman.com/about/research/faq/. [read]
- Strogatz, S. H. (1988). Love affairs and differential equations. *Mathematics Magazine* 61(1):35 (one page). doi 10.1080/0025570x.1988.11977342. [not read; known only through Rinaldi, Sprott and Bielczyk]
- Rinaldi, S. (1998). Laura and Petrarch: an intriguing case of cyclical love dynamics. *SIAM J. Applied Mathematics* 58(4):1205-1221. doi 10.1137/s003613999630592x. [read: abstract, sections 1-4 including calibration; the singular-perturbation analysis skimmed, not checked]
- Sprott, J. C. (2004). Dynamical models of love. *Nonlinear Dynamics, Psychology, and Life Sciences* 8(3):303-314. PDF at sprott.physics.wisc.edu/pubs/paper277.pdf. No DOI found. [read: abstract, introduction, nonlinear triangle section, conclusions]
- Bielczyk, N., Foryś, U., and Płatkowski, T. (2013). Dynamical models of dyadic interactions with delay. *J. Mathematical Sociology* 37(4):223-249. doi 10.1080/0022250x.2011.597279 (Crossref-confirmed; added in validation). Preprint arXiv:1202.2338. [read: abstract and section 1 of the preprint; not re-derived]
- Hamaker, E. L., Zhang, Z., and van der Maas, H. L. J. (2009). Using threshold autoregressive models to study dyadic interactions. *Psychometrika* 74(4):727-745. doi 10.1007/s11336-009-9113-4. Open access. [read: abstract, model section, empirical illustration]
- Madhyastha, T. M., Hamaker, E. L., and Gottman, J. M. (2011). Investigating spousal influence using moment-to-moment affect data from marital conflict. *J. Family Psychology* 25(2):292-300. doi 10.1037/a0023028. [abs]
- Steele, J. S., Ferrer, E., and Nesselroade, J. R. (2014). An idiographic approach to estimating models of dyadic interactions with differential equations. *Psychometrika* 79(4):675-700. doi 10.1007/s11336-013-9366-9. [abs]

---

## 2. Cross-check A: which couples had the lower negativity threshold

### 2.1 What the model's threshold is [read]

Gottman, Swanson and Murray 1999 use an "O-Jive" influence function: zero influence of the partner's previous score inside a band around zero, a fixed positive influence beyond the positive threshold, a fixed negative influence beyond the negative threshold (Fig. 1A). The paper defines the negative threshold as "that point at which the husband's negativity has a major impact on the wife's behavior." Scores are weighted SPAFF totals per 6-second block, "a potential range of -24 to +24" (rechecked in validation [read]); 150 blocks per spouse per 15-minute discussion.

### 2.2 The primary text [read, Results, "Negative threshold"]

> "The husband's negative threshold was a significant predictor of divorce, F(1, 123) = 8.25, p < .01, in the predicted direction. In the first few months of marriage, couples who eventually divorced initially had a negativity threshold more negative than couples whose marriages turned out to be stable. A 'more negative' negativity threshold means that, for example, a husband has to become more hostile before he gets a response from his wife."

Table 1 [read]: husband negative threshold, stable -5.36, unstable (divorced) -7.71, F = 8.25**, df 1,123. Wife negative threshold: stable -6.23, divorced -6.06, F = 0.03. Husband positive threshold 8.45 / 6.65, F = 2.49 (n.s.); wife positive threshold 8.25 / 7.24, F = 0.71 (n.s.). Groups: 108 stable (complete data) vs 17 divorced.

The paper's worked example [read]: "a wife in a marriage that later turned out to be stable had initially reacted to her husband's defensiveness, whereas in a marriage that dissolved, the wife did not react until he became contemptuous, a more negatively weighted behavior." The authors call it "a spouse effect rather than a couple effect."

### 2.3 Where the confusion comes from [read]

- **Abstract:** couples who divorced had "lower negative threshold in the influence function." Lower on the number line = more negative = larger magnitude = slower to respond.
- **Body, theory section:** "If the threshold for negativity is set lower (a smaller negative number on the x-axis) for newlywed marriages that eventually wind up stable and happy, this could be called the marital negativity detector effect." Here "lower" is used for the *stable* couples and means smaller in magnitude.
- The two uses are opposite. The data are unambiguous (the table), the prose is not. Survey 20's "unconfirmed" flag was reasonable on the abstract alone; 059's resolution stands.

### 2.4 Effect size and size of the evidence [derived]

F = 8.25 on 1 and 123 df gives r = sqrt(F/(F+df)) = 0.25, and from the group sizes (108, 17) a standardised difference d of about 0.75. That is a single p < .01 among ten parameters tested in Table 1 (five per spouse, ten tests), of which four reach p < .05 (the uninfluenced steady states at F = 14.86 and 18.40 are far stronger; the husband's influenced steady state, F(1,106) = 4.36, is weaker than the threshold; husband inertia is a trend at F = 3.07). *Corrected in validation: the first pass called the threshold "the weakest of the significant ones".* With 17 events the interval around d is wide. No correction for multiple tests is reported. The paper itself notes the hypothesis was posed in advance (Hendrix vs Wile on whether adapting to negativity is dysfunctional), so the direction was predicted, which helps.

### 2.5 A transcription inconsistency inside the paper [read]

The Results text reports the husband's *influenced* steady state as -1.89 (divorced) vs 0.72 (stable). Table 1 gives those values (-1.89, 0.72) against the *uninfluenced* steady state, and gives the husband influenced steady state as -1.49 vs 0.71, F(1,106) = 4.36. So the text mislabels uninfluenced values as influenced for the husband (the wife's influenced values, -1.95 and -0.65, match the table). Numbers taken from the prose of this paper should be checked against the table.

### 2.6 Group size and composition

Dyad (n = 2) only. Sample [read, rechecked in validation]: 130 newlywed couples from the Puget Sound area, recruited 1989-1992 by newspaper advertisement, first marriage for both, married within 6 months of participating, childless; followed 3 to 6 years (three cohorts); 17 divorced. 125 couples entered the divorce analyses (couples with fewer than 10 zero-scored blocks in a half could not be estimated). *Corrected in validation: the first pass said "Seattle, married under nine months".* Husband and wife are separate parameters; the threshold finding is gender-specific in this sample (husband only), with no reason offered in the paper beyond a "spouse effect". Nothing about groups larger than two. Composition: heterosexual couples in this paper; 059 notes the 2003 paper extends the form to same-sex couples.

### 2.7 Scale and consent/manipulation

Scale: **membership** (the couple's own stay/leave outcome, divorce) predicted from a **dyadic** interaction parameter. No intervention: observational. The paper proposes, but does not test, "resetting the marital negativity detector" in therapy; that would be an intervention with consent (couple therapy), still a hypothesis.

---

## 3. Cross-check B: divorce-prediction accuracy figures, traced to source

### 3.1 The 1992 paper: what was actually predicted [read]

Gottman and Levenson 1992 (73 couples, 1983 to 1987). Couples were classed as *regulated* (both spouses' cumulative positive-minus-negative RCISS speaker-code slopes significantly positive; 42 couples) or *nonregulated* (31). The class definition does not use the outcome, which is its strength. Outcomes over four years: 36 of 73 considered dissolution; 18 (24.7%) separated; **9 divorced** (the paper prints "12.5%"; 9/73 is 12.3%, used below). The authors call the cascade (consider, separate, divorce) "preliminary" and say the low base rate "resulted in a fairly small pool of divorced couples."

Table 3 [read]: considered dissolution 33.0% (regulated) vs 71.0% (nonregulated), z = 3.18; separation 16.7% vs 36.8% (text: 7 of 42 vs 11 of 31), z = 1.84, p = .032; **divorce 7.1% (3 of 42) vs 19.0% (6 of 31), z = 1.57, p = .058, "approached" significance.** The authors say, consistent with their cascade model, that the typology "was better at discriminating precursor variables than the more rarely occurring criterion events." A Fisher exact test on 6/31 vs 3/42 gives two-sided p about 0.16 [derived]. Continuous slopes correlate -.28 (husband) and -.32 (wife) with divorce.

Treated as a divorce classifier [derived from those counts]: predicting divorce for nonregulated couples gives sensitivity 6/9 = 67%, specificity 39/64 = 61%, positive predictive value 6/31 = 19%, overall accuracy 45/73 = 62%. Always answering "stays married" gives 64/73 = **87.7%**. So the paper's own divorce result is a modest risk ratio (2.7), not a 90%-class prediction.

The discriminant analyses in that paper (Table 5) classify couples into the regulated/nonregulated *types*, not into divorced/stable; the authors call them "exploratory." (Their percentages correct for the types run from 71.4 to 100, per group, Table 5 [read].) They do not produce the 93.6% figure. I found no 93.6% anywhere in the 1992 text.

### 3.2 The 1999 "Rebound" paper: 82.6% and 92.7% [read in full]

Same 79-couple Bloomington sample, 73 followed up at four years. Two discriminant function analyses (one per conversation). "Codes were entered into the discriminant function only if their univariate F-ratios were statistically significant." Conflict conversation: four codes entered (husband interest, husband contempt/disgust, wife interest, wife sadness), canonical r = .43, chi-square(4) = 13.23; **82.6% correct**. Positive conversation: four codes (husband anger, husband contempt/disgust, wife affection, wife anger), canonical r = .59, chi-square(4) = 27.56; **92.7% correct.** Table 1 means: for example in the positive conversation husband contempt 2.05 (together) vs 11.14 (divorced); wife affection 2.52 vs 5.86 (the divorced wives were *more* affectionate, which the authors explain post hoc as compliance in the face of contempt).

What is not in the paper: the number of divorces (the 1992 paper's 9 of 73 is the same sample and follow-up, so I use it as the assumed count, [derived], flagged), the analysed N (the paired t-tests have 71 df, so about 72 couples had both conversations), sensitivity, specificity, or any hold-out or leave-one-out. The candidate pool is stated by the coding scheme: each speech act was coded neutral, one of five negative affects or one of four positive affects, so **nine codes per spouse, 18 per conversation** were candidates for each function [read; corrected in validation from "roughly 18 SPAFF codes per spouse"]. The authors say "until there is further research, we cannot draw conclusions" about order effects, and also note the two conversations were not counterbalanced.

[derived] Selecting 4 predictors from 18 screened (nine affect codes by two spouses, per conversation) for 9 events is a regime where in-sample accuracy is expected to be inflated; and if the divorce rate was 12.3%, the trivial rule scores 87.7%, so **82.6% from the conflict conversation is below the do-nothing rate** (92.7% is above it by 5 points). The discriminant default of equal priors would trade sensitivity for specificity, so this comparison shows the percentage is not a sufficient summary, not that the function is useless.

### 3.3 The 2000 "Timing" paper: 83.5, 86.2, 88.5, 75.0, 95, 89.5 and a "93%" abstract [read]

Same sample, followed 14 years: 22 of 79 (27.8%) divorced; 9 early (mean 7.4 years of marriage), 13 later (mean 13.9 years). Reported correct classifications (all discriminant functions, in-sample, canonical r given):

| Model | Outcome | Reported % correct | Predictors | Note |
|---|---|---|---|---|
| Positive affect + T1 satisfaction | early divorce | n.s. (r = .31, chi-square(6) = 6.84 ns) | | fails |
| Negative affect (RCISS) + T1 satisfaction | early divorce | 83.5 (r = .52, chi-square(12) = 22.36) | 12 | df of univariate F = (1,77), so N = 79 |
| Same, interaction only (RCISS) | early divorce | 83.5 (r = .51, chi-square(10) = 21.26) | 10 | |
| Positive affect + satisfaction T1, T2 + thoughts of divorce and separation | later divorce | 88.5 (r = .73, chi-square(11) = 33.82) | 11 | **includes Time-2 satisfaction and thoughts of divorce, which are cascade steps toward the outcome**; univariate df (1,50), so N about 52 |
| Negative affect (RCISS) + the same non-interactive predictors | later divorce | 86.2 (r = .73, chi-square(18) = 35.08) | 18 | the text says "the noninteractive variables did all the work"; every interactive univariate F was n.s. |
| Positive SPAFF codes only | later divorce | 75.0 (r = .50, chi-square(4) = 13.99) | 4 | df (1,50), N about 52 |
| Four Horsemen RCISS codes | early vs later among the 20 divorcers with data | 95 (r = .85, chi-square(8) = 18.03, p = .021) | 8 | univariate df (1,18): 8 predictors for 20 couples |
| Husband negative SPAFF, events-of-day | early vs later | 89.5 (r = .73, chi-square(4) = 11.36, p = .023) | 4 | df (1,17), 19 couples; the only significant one of a set of models built per spouse |

*Corrected in validation (all rows re-read from the scanned pages 740-742): the first pass had no 86.2% row and attached "did all the work" to the 88.5% model; it belongs to the 86.2% negative-affect model.*

[derived] For early divorce the null rule (everyone stays) scores 70/79 = **88.6%**, above the reported 83.5%. The 95% figure rests on about 20 couples and eight predictors. The abstract says "The model predicted divorce with 93% accuracy"; **93% appears nowhere in the body** (validation: the scanned pages 737-744 were read as images, not OCR, and no sentence or figure gives 93%; the reported percentages are those in the table above). It should not be quoted.

Substantive result worth keeping [read]: *different mechanisms predicted different divorces.* Early divorce followed high negativity (criticism, defensiveness, contempt, stonewalling); later divorce followed the *absence* of positive affect, and not high negativity. Interaction variables were "about five times more powerful" than non-interactive ones (stated, not tested). Power for the timing contrasts is "relatively low" in the authors' words.

### 3.4 The 94% / 93.6% figure [read: FAQ and 1999 text; derived arithmetic]

- Gottman's FAQ [read]: "Statements about the 94% accuracy rate of divorce prediction have become a source of confusion. What Dr. Gottman is able to say is that a particular couple is behaving like the couples that were in the group that got divorced in his 1992 study (Buehlman, K., Gottman, J.M., & Katz, L.), a study in which Dr. Gottman predicted with 93.6% accuracy which couples would divorce." It adds that seven studies explored divorce, "six of the seven studies have been predictive," the first being post hoc (1980 data mining), and that "for the Gottman, Katz and Hooven study... picked out all seven divorced couples out of 56." So the 93.6% belongs to the Buehlman et al. sample (56 families recruited, 47 couples classified, 7 divorces), not to the 73/79-couple lab-conflict study and not to the newlywed model.
- Gottman and Levenson 1999 ("What predicts change") [read, p. 5-ish]: Buehlman et al. (1992) "later reported that their observational coding of this interview in another longitudinal study with 56 couples predicted divorce with 94% accuracy over a 3-year period." Same figure, same sample size.
- Buehlman, Gottman and Katz 1992 itself [read in validation]: 56 families recruited (target child aged 4-5); the abstract reports "52 married couples"; at the 3-year follow-up "13.5% of the couples we were able to contact had divorced". Nine Oral History predictors, chosen by a principal components analysis, entered a discriminant function: canonical r = .75, chi-square(8) = 35.45. Table 7: 40 married (37 correct, 3 called divorced) and 7 divorced (7 correct), "93.62%" = 44/47. So the first pass's guess (44/47) was right; its null rate was not. [derived] Always answering "stays married" scores 40/47 = **85.1%**; sensitivity 100%, specificity 92.5%, PPV 7/10 = 70%, all in-sample with 9 predictors for 7 events. Time-1 marital satisfaction alone gave a non-significant function (r = .32).
- The FAQ's "urn" argument (the probability of picking the 17 divorces out of 147 at 90% accuracy by chance is about 1e-19) tests whether predictors carry *any* information about the group split. It does not give out-of-sample accuracy, because it does not allow for choosing the predictors on the same data.
- The FAQ says Conger's group at Iowa State "replicated some of Gottman's divorce prediction studies." [read, stated by the FAQ.] Validation: Carrere and Gottman 1999 cite Matthews, Wickrama and Conger 1996 (*J. Marriage Fam.* 58:641, doi 10.2307/353725) as the replication "in another laboratory"; its title predicts marital *instability*, not divorce. Not read, so what it replicated is unverified.
- What the FAQ does not mention: Heyman and Slep, or Kim et al.

### 3.5 Newlywed study: 87.4% / 81% [read in validation]

University of Washington release, 27 March 2000 [read: press]: Oral History Interview, **95 newlywed couples**, **87% accuracy at four to six years, 81% at seven to nine years; 16 of 95 divorced.** The release says the divorce rate was below the national average and the sample "likely self-selected."
Carrere et al. 2000 itself [read in validation]: two discriminant functions on Oral History codes. **Time 2 (1995): 7 of 95 divorced**; six predictors, "chosen on the basis of which were most effective in predicting membership in the divorced group" (six because there must be fewer predictors than cases in the smallest group); 6 of 7 divorces and 77 of 88 married correct, **87.4%**, canonical r = .42, chi-square(6) = 17.35. **Time 3 (1998): 16 of 95 divorced**; 11 predictors; 13 of 16 and 64 of 79 correct, **81%**, r = .53. No hold-out or cross-validation. [derived] The do-nothing rule scores 88/95 = **92.6%** at Time 2 and 79/95 = **83.2%** at Time 3, so **both figures are below it**; PPV is 6/17 = 35% and 13/28 = 46%. *Corrected in validation: the first pass, from the press release, set the 87% against the Time-3 null (83.2%) and called it 4 points above; the 87% is the Time-2 result, where only 7 had divorced.*
The "first three minutes" paper (Carrere and Gottman 1999) [read in validation]: 124 couples (t-tests on 122 df), six years; the results are group comparisons of affect per 3-minute block (Tables 2-3) and repeated-measures trends, and **no classification accuracy is reported.** The 17 divorces is from the press release; I did not find the count on the pages I read.
Also stated in `change99` [read; rechecked in validation, p. 150]: footnote 1: "the ability of these six SPAFF codes for each spouse to predict divorce at Time-2 in a discriminant function analysis yielded a canonical R of .62, with chi-square(12) = 29.59, p = .0032. The percent correct classification was 91.18%": another in-sample discriminant figure on the same Bloomington sample. The footnote does not say on which occasion the six codes were measured.

### 3.6 Heyman and Slep 2001, the cross-validation critique [read in validation]

Abstract [read]: earlier studies such as Gottman et al. (1998) "overlooked the need to crossvalidate prediction equations and to consider divorce prevalence." Using archival data (not Gottman's), they find "accuracy and predictive value drops precipitously during crossvalidation."
Body [read in validation, PMC1622921]: data are the 1985 National Family Violence Survey (telephone interviews, n = 6,002), which is **cross-sectional**, unlike Gottman's prospective data, as the authors say. They drew 176 divorced and 352 married or cohabiting participants (528 individuals, a 33% divorce prevalence chosen to parallel the "artificially imposed prevalence of 33% by Gottman et al.'s procedures") and split them at random into development and crossvalidation halves of 88 + 176. A logistic regression with an ROC-chosen cut-point classified the development half at **90% correct, sensitivity 92%, specificity 89%, PPV 65%**. On the crossvalidation half (Table 1; 62 dropped for missing data): 17 true positives, 42 false positives, 20 false negatives, 123 true negatives: **69.31% correct, sensitivity 45.95%, specificity 74.55%, PPV 28.81%, NPV 86.01%.** Reweighted to a 16% prevalence, PPV fell to **20.99%**, against a base rate of 16%. They also note that 15 published studies had predicted who divorces, with accuracies of 67% to 95%. *The numbers the first pass held as [sa] are confirmed; two details are added: the sample is of individuals in a cross-sectional survey, and the build-half PPV was 65%.* Two things transfer. The paper's *method* (build on half, test on half, report PPV at the real base rate) is the missing step in the Gottman-Levenson papers. And the paper uses a different data set, so it shows that the inflation is possible, not that it occurred in Gottman's data.

### 3.7 Independent replication: Kim, Capaldi and Crosby 2007 [abs]

85 at-risk community couples, married or cohabiting (Oregon Youth Study, per a search summary of the reply [sa]; the abstract says only "at-risk backgrounds"), affect at about age 21, relationship status and satisfaction about 2.5 years later. "The major findings of Gottman et al. failed to replicate": men's rejection of influence, lack of men's de-escalation of partners' negative affect, and women's negative start-up did not predict relationship status. This tests the 1998 variables, not the difference-equation parameters. A published comment and reply exist in the same issue: Coan and Gottman 2007, 69(1):73-80, doi 10.1111/j.1741-3737.2006.00344.x, and Kim and Capaldi 2007, 69(1):86-91, doi 10.1111/j.1741-3737.2006.00346.x, PMC1832156, on sample and task generalisability (neither read; existence from Crossref). The sample is different in age, risk and outcome definition (status includes cohabiters), so a non-replication here is weaker evidence than a failure in a matched sample.

### 3.8 Base-rate arithmetic for any claimed accuracy [derived]

PPV = sens x p / (sens x p + (1 - spec)(1 - p)). With sens = spec = 0.90: base rate 12.3% gives PPV 56%; 18% gives 66%; 28% gives 78%. For the 1992 regulated/nonregulated rule (sens 67%, spec 61%): 19% at 12.3% prevalence. Any statement "X% accuracy" with no stated sensitivity, specificity, prevalence and out-of-sample design cannot be used as a prediction claim for the algebra.

---

## 4. Cross-check C: Strogatz vs Gottman, and which love ODEs were ever fitted

### 4.1 What Strogatz's model is [read via others; Strogatz himself not read]

- Rinaldi 1998 [read]: "the only exception being a contribution by Strogatz [1] who reports (in a one-page paper entitled 'Love Affairs and Differential Equations') his success in teaching harmonic oscillators by making reference to Romeo and Juliet."
- Sprott 2004 [read]: "Although Strogatz's model was originally intended more to motivate students than as a serious description of love affairs, it makes several interesting and plausible predictions"; "essentially the same model was described earlier by Rapoport (1960)" (Rapoport, *Fights, Games and Debates*, Univ. of Michigan Press), and studied by Radzicki (1993) [citations as given by Sprott; those two not opened].
- Bielczyk et al. [read, quoting Strogatz]: "R loves J, J is a fickle lover. The more R loves her, the more J wants to run away and hide. When R gets discouraged and backs off, J begins to find him strangely attractive. R on the other hand tends to echo her." Equations, as stated by Bielczyk et al.: R' = a J, J' = -b R, with a, b > 0; the origin is a centre; "other nontrivial cases lead to divergent solutions." Bielczyk cite the year/volume as Math. Magazine 65(1); Crossref (and Rinaldi's reference list) say 61(1). Bielczyk attribute the quotation jointly to Strogatz 1988 and Strogatz 1994 (pp. 138-140), so which of the two it comes from is not settled by them. General linear form (their eq. 3, after shifting to the equilibrium) r' = a11 r + a12 j, j' = a21 r + a22 j, with the sign cases named "eager beaver", "cautious lover", "narcissus" and "stoic lover". [Strogatz attribution: sa; the equations as printed by Bielczyk: read, rechecked in validation.]
- Verdict: a teaching device with **no data** and no claim of fit. It is not in competition with Gottman's model empirically; it is a different class (continuous, linear, no thresholds, no partner-specific nonlinearity, no noise).

### 4.2 Rinaldi 1998: the only "fit" among the ODE love models, and what it was [read]

Model [read, eqs. 1-3 and 6-8]: L (Laura's love), P (Petrarch's love), Z (Petrarch's poetic inspiration):
dL/dt = -alpha1 L + R_L(P) + beta1 A_P; dP/dt = -alpha2 P + R_P(L) + beta2 A_L/(1 + delta Z); dZ/dt = -alpha3 Z + beta3 P. R_P(L) = beta2 L (linear); R_L(P) = beta1 P (1 - (P/gamma)^2), a cubic chosen "due to convenience" (Rinaldi's words), with a positive maximum for P > 0 (flattered, then rebuffs) and a negative minimum for P < 0 (pity). All Greek letters positive constants, with gamma = delta = 1 by scaling P and Z; A_P, A_L the "appeal" of each person (signs opposite: A_L = 2, A_P = -1).
Data [read]: Jones's grades (from -1 to +1) of 23 securely dated poems of 1330-1347, assigned by a "subjective evaluation"; Rinaldi's own words: "noisy data, because each point... is affected by a horizontal error due to the uncertainty of the date of the poem, and by a vertical error due to Jones's subjective evaluation."
Calibration [read]: "all available information comes from a series of poems. Therefore the values given to the parameters in this section do not pretend to be the 'correct' ones. They are only my personal estimates based on the feelings and impressions I had when reading the Canzoniere." Parameters fixed by inequalities from the poems (alpha1 = 3 alpha2, alpha3 = alpha2/10, beta1 = alpha2, beta2 = 5 alpha2, beta3 = 10 alpha2, A_L = 2, A_P = -1), giving (alpha1, alpha2, alpha3) = (3, 1, 0.1) with time unit one year. Simulated period was about 20% longer than Jones's, "I have therefore increased" the rates, giving alpha1 = 3.6, alpha2 = 1.2, alpha3 = 0.12, beta = (1.2, 6, 12). "The fit is very good, actually as good as that which is usually obtained when calibrating models of electrical and mechanical systems," but he shows no residuals, uses the grade as proportional to P, and says he does not show further improvement "because I do not want to give the impression that I believe that Petrarch had been..." (sentence cut across the page in my text; the sense is that he does not wish to over-claim).
Reading [rechecked in validation]: Jones fitted his cycle to the 23 securely dated poems and then used that cycle, with historical information, to date the undated poems. Rinaldi says his constants were set from "all the poems of the Canzoniere, and not from the particular 23 poems analyzed by Jones", so that the model is "independent" of Jones's result; the only quantity matched to the 23 points is the period, by one 20% time stretch. The comparison with the 23 points is therefore a check on the period and phase, made by eye, with no residuals; the independence rests on Rinaldi's impressions of the poems, which are not blind to the poems' content. Its value is qualitative: a limit cycle in the poet's love with a period of slightly under four years is reproduced, and Rinaldi shows by continuation (LOCBIF) that the cycle survives one-at-a-time parameter changes of 19% to 134% before a supercritical Hopf bifurcation removes it. *Corrected in validation: the first pass said the 23 points "were themselves used by Jones to date the other poems, so the dated points are not independent tests"; it was the cycle drawn through them that Jones used, and Rinaldi claims independence for his constants. A German teaching text ("ChaosLiebe", Uni Wuppertal) that the first pass cited was not found by search and is moved to Unconfirmed; it added nothing.*
Scale: **individual** (one person's emotional trajectory) with a second person's response modelled; **n = 2 actors plus one internal state (Z)**; no group.

### 4.3 Sprott 2004 [read]

"Following a suggestion of Strogatz, this paper examines a sequence of dynamical models involving coupled ordinary differential equations... linear system of two individuals... love triangles and finally... nonlinearities, which are shown to produce chaos." Stated aim is to illustrate complexity; the conclusion calls the models "gross simplifications since they assume that love is a simple scalar variable and that individuals respond in a consistent and mechanical way." The chaos example (Eq. 5, three actors but four state variables, since Romeo's love for Juliet and for Guinevere are separate: a = -3, b = 4 for Romeo; e = 2, f = -1 for Guinevere; c = -7, d = 2 for Juliet; largest Lyapunov exponent 0.380) has *no data of any kind.* **n changes the qualitative behaviour (linear dyad: centre/node/focus; nonlinear triangle: chaos), which is the only n-dependent result in the set, and it is purely theoretical.**
Bielczyk et al. [read: abstract]: theorems about delay-induced stability switches, "Some generalizations to triadic interactions"; no data in the part I read.

### 4.4 What has been fitted, with the honest ranking

| Model | Form | Data | Fit type | Result |
|---|---|---|---|---|
| Strogatz 1988 | linear ODE | none | n/a | teaching |
| Sprott 2004 | ODE, triangles | none | n/a | illustrative |
| Bielczyk et al. | delay ODE | none | n/a | theory |
| Rinaldi 1998 | 3 ODEs, cubic reaction | 23 graded poems | hand calibration, one fitted scalar | qualitative match [read] |
| Gottman-Murray 1999 | difference eq., O-jive | 125 couples, 150 blocks each | per-couple least squares + ogive | parameters differ by outcome in-sample [read] |
| Hamaker et al. 2009 | TAR regimes | 3 dyads, 3 conversations each, 2-s SPAFF scale -12..12 | BIC model choice | step (regime) form beats partner-slope form for all 6 persons [read] |
| Madhyastha et al. 2011 | GM model by TAR/BIC | 124 couples and 130 newlyweds [abs] | BIC across influence forms | influence "only slightly greater than random association"; "one model does not fit all couples"; for many people initial state and inertia matter more than the partner's moment-to-moment affect [abs] |
| Steele et al. 2014 | dyadic differential-equation models | daily affect ratings, romantic couples [abs] | AICc per dyad, AICc-weighted parameter averaging | "the most likely interaction style was that of independence, without evidence of emotional interrelations between the two individuals in the couple"; averaged parameters had "modest" relations to satisfaction and status [abs] |

Hamaker et al. details [read]: the Gottman-Murray model is shown to be "a special case of the threshold autoregressive (TAR) model," which lets standard TAR estimation and model selection apply. Their empirical example uses two heterosexual couples and one pair of female friends. Winning model for every person: influence function B (a step function, with regimes) with unequal residual variances, two or three regimes, and "the partner's score does not help to further predict the observations within the regimes." Table 4 [all six rows read in validation]: R-squared 0.51 to 0.64, inertia estimates (alpha1) 0.68 to 0.77 with bootstrap SE 0.02, thresholds on the 2-second -12..12 scale of 0 to 7. Each pair held three 15-minute conversations (neutral, negative, positive), analysed together. All three dyads had influenced steady states in the positive quadrant; one dyad had two nearby stable states. This is an in-sample illustration of an estimator, not a test of the model: no outcome, three dyads, nonclinical couples.

Reading across: the only data-driven items that bear on the coupling term suggest it is small relative to inertia and set point in observed affect series (abstract-level for two of them). That is a threat to any algebra whose primitives are *coupling operators between persons*, and I flag it as such, not as a settled finding.

### 4.5 Group size and composition across this file

All empirical results here are dyads (n = 2): heterosexual married couples in Bloomington (newspaper-recruited, 79 couples) and Seattle (newlyweds), an at-risk Oregon sample (Kim), and in Hamaker et al. two couples and one friend pair (the only non-couple composition). Rinaldi's is a pair with one-sided love. Sprott's triangle is the only n = 3 result and it is simulated. For n > 2 there is no data in this file.

---

## 5. Operand/operator translation for the algebra

| Their object | Candidate in the algebra | Status |
|---|---|---|
| Weighted SPAFF valence per speaker per block | A person's expressed-affect scalar per time step (an observable, not a drive) | read |
| Uninfluenced steady state a/(1 - r) | The person's baseline (set point) | strongest divorce correlate in-sample (F = 14.86, 18.40) |
| Inertia r | Persistence of the person's own state | not predictive of divorce in 1999 |
| Influence function I(partner score), O-jive with negative and positive thresholds | A coupling operator with dead zone and saturation | only the husband's negative threshold predicted divorce |
| Negative threshold | A gating level on incoming negativity (perceptual/attention), not a drive | direction established, size modest |
| Regulated vs nonregulated (positive/negative balance over time) | A scalar class of the dyad from the *slope* of cumulative positive-minus-negative | weak on the hard outcome (OR about 3 at p = .058) |
| Rinaldi's forgetting, appeal, reaction R(.), inspiration Z | decay toward 0, an exogenous input, a person-specific nonlinear response, a slow integrator | hand-calibrated only |
| Divorce | An absorbing state of the dyad (an exit event), downstream of the dynamics | rare: 7-28% over 4-14 years in these samples |

---

## 6. What exists vs what does not

**Exists.** (a) A defined, printed threshold parameter with a clear direction (divorcing husbands needed more hostility before the wife responded), significant once, in-sample, among ten tests. (b) Several in-sample classification percentages (82.6, 92.7, 83.5, 86.2, 88.5, 91.18, 95, 93.6, 94, 87) from discriminant functions with predictors screened on the same data, mostly on a single 79-couple sample. (c) One published cross-validation critique with a method that works (build on one half, test on the other). (d) One failed independent test of the 1998 variables (Kim et al.). (e) Qualitative demonstrations that two-variable coupled ODEs can cycle and three-actor nonlinear ones can be chaotic, with no data. (f) A statistical bridge between Gottman-Murray and standard TAR models, which makes model selection by BIC possible.

**Does not exist (in what I read).** A hold-out or cross-validated divorce prediction from the *model parameters* (thresholds, steady states); any reported sensitivity/specificity/PPV from the Gottman-Levenson papers (Buehlman et al. 1992 and Carrere et al. 2000 do print classification tables, from which they can be derived, section 3.4-3.5); a replication of the husband-threshold finding; a fitted love ODE with out-of-sample prediction; any fitted model with n > 2 actors; any model with drives (curiosity, fear, desire) as separate variables; any data on whether changing a threshold changes outcome.
*Validation search (2026-10-30), two web searches:* no independent replication or cross-validation of the Gottman-Murray threshold parameters turned up, which supports the first two negatives as "not found" rather than proven absent. The ODE search turned up dyadic differential-equation fits beyond Steele et al. 2014 that this file does not cover, e.g. Boker and Laurenceau 2006 (book chapter, "Dynamical systems modeling: an application to the regulation of intimacy and disclosure in marriage", doi 10.1093/acprof:oso/9780195173444.003.0009, Crossref only, not read), and a fractional-order love model said to be checked against questionnaire data (Talabi et al. 2019, not verified). None found reports an out-of-sample test, but "no coupled-ODE love model has been fitted to data" (Summary 4) holds only for the Strogatz-Sprott-Rinaldi line; affect-dynamics ODEs have been fitted to couples' data.

## 7. Unconfirmed

- Gottman, Coan, Carrere and Swanson 1998 (130 couples, 17 divorced, the affective variables Kim et al. tried to replicate): not read; accuracy claims for it, including whether it reports cross-validated or in-sample figures, are unknown to me. Heyman and Slep say its procedures imposed a 33% divorce prevalence; that is their account, not checked against the paper.
- Strogatz 1988 itself; Strogatz 1994 pp. 138-140; Rapoport 1960; Radzicki 1993.
- The analysed N and the divorce count in the Rebound paper (assumed 9 of 73 from the 1992 paper; the 82.6% versus 87.7% comparison depends on it).
- Madhyastha et al. 2011 and Steele et al. 2014 beyond their abstracts.
- Matthews, Wickrama and Conger 1996: identified in validation as the probable Iowa replication; not read, so what it replicated is unverified.
- Coan and Gottman 2007 and Kim and Capaldi 2007 (comment and reply): found on Crossref in validation; content not read. "Oregon Youth Study" as the Kim et al. sample: search summary only [sa].
- The 17 divorces in Carrere and Gottman 1999: press release only.
- "ChaosLiebe" (Uni Wuppertal), a German teaching text the first pass cited as restating Rinaldi's parameters: no URL was recorded and a search did not find it. Nothing rests on it.
- Boker and Laurenceau 2006 and other dyadic ODE fits outside this file (section 6): not read.
- The 2003 paper's (repair/damping; same-sex couples) parameter values: read in 059, not re-read here.

---

## Does it reduce to a drive basis?

**Partly, and only the least predictive parts.**

- **Reduces plausibly.** The *uninfluenced steady state* (baseline affect each person brings) behaves like a drive-level or set point, and *inertia* like relaxation toward it; Rinaldi's forgetting term (-alpha x) is literally decay toward zero and his *inspiration* Z is a slow integrated state, and his appeals A are exogenous inputs that drive the state. These are drive-style terms (set point, decay, input). They are also the best divorce correlates in-sample (steady states F = 14.86 and 18.40), and the independent evidence (Madhyastha, abstract) says initial state and inertia matter more than partner coupling for many people. So a set-point-and-decay description of *persons* carries most of the signal there is.
- **Does not reduce.** (i) The **threshold** is a gating parameter on incoming signals (how much partner negativity is needed before the response engages), not a drive; it would need an operator on the *coupling*, not a drive variable. It is also the single parameter with a well-defined direction in the divorce data, but only for husbands. (ii) The **outcome** (divorce) is a decision of two people plus external constraints. Gottman and Levenson 2000 themselves cite reasons for divorce (growing apart; losing closeness) and for staying (raising children) that are not in the affect series. Later divorce was predicted by *absence* of positive affect and by Time-2 satisfaction and thoughts of divorce, i.e. by a state variable already describing the outcome trajectory. (iii) **Rinaldi's reaction function** R_L(P) with flatter-then-rebuff-then-pity is a hand-drawn relationship-specific response, "due to convenience". It would have to be derived from drives (flattery, fear of overreach, compassion), and no one has done that. (iv) The **valence scalar** collapses interest, fear, anger, contempt and affection into one weighted sum; the 1999 Rebound paper shows the codes behave differently (wife affection higher in couples who divorced). A drive basis needs separate channels, and these papers' own coded data contain them but the models do not use them. (v) The cascade and the early/late divorce split show at least two routes (negativity-driven and positivity-absent) that a single valence axis conflates.
- **Not tested at all:** drives as the primitives. No paper here posits one; the working hypothesis is neither supported nor refuted by this tradition.

## What does it predict or control, and how well?

- **Predicts (claimed):** divorce or stability of a couple. Evidence in the papers read is all in-sample. Reported accuracies of 75 to 95% come from discriminant functions fit and scored on the same 73 to 79 couples with predictors chosen by univariate significance, and, where counts are available, are at or below the accuracy of always answering "stays married" (82.6% vs 87.7% for the Rebound conflict result under the assumed count; 83.5% vs 88.6% for early divorce; the 1992 regulated/nonregulated rule is 62% accurate with 19% PPV). The 93.6%/94% headline is a separate Oral History study (47 couples classified, 7 divorces, 9 predictors, null rate 85.1%), and the newlywed Oral History figures (87.4%, 81%) are both below their null rates (92.6%, 83.2%). The one cross-validation (Heyman and Slep, other and cross-sectional data, [read]) found a steep drop (PPV 65% to 29%, 21% at 16% prevalence); the one independent replication attempt (Kim et al., at-risk sample, abstract only) found three of the 1998 predictors did not predict status.
- **Effect sizes actually reported:** husband negative threshold r about 0.25, d about 0.75 (derived from F = 8.25); regulated vs nonregulated divorce 19.0% vs 7.1% (risk ratio 2.7, Fisher p about .16); considered dissolution 71% vs 33% (the strongest of the outcome contrasts, and the least costly outcome).
- **Controls:** nothing. Gottman and colleagues propose resetting the "marital negativity detector" and say they are running intervention experiments in which the couple's second discussion is changed by targeting a model parameter; I found no result. Therapy relapse and help-seeking delay are offered as explanations by analogy only.
- **Failures and limits:** low base rates (12 to 28% divorce in these samples) and small event counts (9, 17, 22); outcome-tuned measurement (059: the SPAFF code weights came from earlier divorce prediction work); inconsistent lag conventions across papers (059); text/table mismatch in the 1999 paper; an abstract accuracy not found in the body; a failed independent replication of related variables; and independent fits of the dyadic models finding little partner coupling (Madhyastha, Steele, abstract-level). The fitted ODE love models (Rinaldi) predict nothing out of sample and were calibrated by taste to 23 subjectively graded points. Scale throughout is dyadic-to-membership (will this couple leave) with no consent-based or manipulative intervention tested.

## Validation log (2026-10-30)

Every DOI was resolved at api.crossref.org/works/<doi>; titles, authors, volumes and pages matched unless noted. Legend: ✓ confirmed as written; ✎ corrected in place; ? unconfirmed; ✗ removed.

- ✎ Gottman, Swanson and Murray 1999 — PDF re-read: Table 1 and 2 values, the F's, both "lower" passages, the defensiveness/contempt example and the -1.89/0.72 text-table mismatch all confirmed. Fixed: sample is "married within 6 months", Puget Sound, 130 couples (125 analysed), 3-6 years, not "Seattle, married under nine months"; the threshold is not the weakest significant parameter (husband influenced steady state, F = 4.36, is weaker; four reach p < .05); -24..+24 scale now [read].
- ✎ Gottman and Levenson 1992 — PDF read: 42/31 split, Table 3 percentages, z's, p's, slope correlations, "approached", "fairly small pool", "exploratory" confirmed; no 93.6% in the text. Fixed: the paper prints 12.5% for 9/73.
- ✎ Gottman and Levenson 1999, Rebound — scanned PDF read page by page: 82.6% and 92.7%, codes, chi-squares, Table 1 means, order and compliance passages confirmed. Fixed: 9 codes per spouse, 18 per conversation screened (not "roughly 18 per spouse" or "about 36").
- ✎ Gottman and Levenson 2000, Timing — scanned PDF read page by page: sample, 22/79, 9 early and 13 later, 83.5/88.5/75.0/95/89.5 confirmed; 93% is absent from the body (now settled, not "OCR rough"). Fixed: added the missing 86.2% row and moved "noninteractive variables did all the work" to it from the 88.5% row; added the chi-squares and df.
- ✓ Gottman and Levenson 1999, What predicts change — the 94%/56-couple sentence (p. 145) and footnote 1 (91.18%, p = .0032, p. 150) confirmed; subtitle added to the citation.
- ✓ Gottman and Levenson 1999, How stable — Crossref only; not used.
- ✎ Buehlman, Gottman and Katz 1992 — added as a citation and read: 93.62% = 44/47, 7 divorces, 9 predictors, r = .75. Fixed: the null rate is 40/47 = 85.1%, not 49/56 = 87.5%; the abstract says 52 couples.
- ✎ Carrere et al. 2000 — read (was press release only). Fixed: 87.4% is the Time-2 result with 7 of 95 divorced (null 92.6%), not 4 points above the Time-3 null; 81% at Time 3 is also below its null (83.2%); predictors chosen on the outcome; no cross-validation.
- ✓ Carrere and Gottman 1999 — read: no classification accuracy reported, 124 couples (t on 122 df). Upgraded from press release.
- ✓ Heyman and Smith Slep 2001 — read in full on PMC: every number held as [sa] confirmed (528, split half, 90%, 28.81% PPV, 45.95% sensitivity, 74.55% specificity), plus build-half PPV 65%, 16%-prevalence PPV 20.99%, cross-sectional individual-level data. Upgraded to [read].
- ✓ Kim, Capaldi and Crosby 2007 — abstract confirmed; "Oregon Youth Study" marked [sa].
- ✎ Coan and Gottman 2007; Kim and Capaldi 2007 — the first pass said the Coan-Gottman reply was "not found"; it is on Crossref (69(1):73-80). Both added with DOIs; not read.
- ? Matthews, Wickrama and Conger 1996 — added as the probable Iowa replication; Crossref only.
- ✓ Gottman Institute FAQ — every quotation re-fetched and confirmed (94% "confusion", 93.6%, seven studies, six predictive, 1980 post hoc, 7 of 56 for "Gottman, Katz and Hooven", the 17-of-147 urn, Conger). It does not mention Heyman, Slep, Kim, Capaldi or cross-validation.
- ? Strogatz 1988 — exists (Crossref, Math. Mag. 61(1):35); not read; attribution stays [sa].
- ✎ Rinaldi 1998 — read: quotations, parameters, 20% stretch, "convenience", "personal estimates", the fit sentence confirmed. Fixed: the reading of the 23 points (Jones dated the *undated* poems from his cycle; Rinaldi claims his constants come from the whole Canzoniere); added gamma = delta = 1 and the robustness range.
- ✎ Sprott 2004 — read: quotations, Rapoport, Radzicki, chaos parameters, Lyapunov 0.380 confirmed; no DOI on Crossref. Added that Eq. 5 has four state variables.
- ✎ Bielczyk, Foryś and Płatkowski — preprint read: quotation, equations, 65(1) citation confirmed. Added the published version (J. Math. Sociol. 37:223-249, 2013, DOI) and that the quotation is credited jointly to Strogatz 1988 and 1994.
- ✎ Hamaker, Zhang and van der Maas 2009 — read (Cambridge Core PDF): special-case result, three pairs, -12..12 2-second scale, step model best for all six persons, "does not help" quotation confirmed. Fixed: R-squared 0.51-0.64 with all six rows (first pass had 0.51-0.61, dyad 3 unread).
- ✓ Madhyastha, Hamaker and Gottman 2011 — abstract confirmed (N = 124 and 130, "only slightly greater than ... random association", "one model ... does not fit all couples").
- ✎ Steele, Ferrer and Nesselroade 2014 — abstract checked: the quotation was a paraphrase and "latent differential equations" is not in the abstract; replaced with the abstract's words.
- ✗ "ChaosLiebe" (Uni Wuppertal) — not found by search, no URL recorded; moved to Unconfirmed (not called fabricated, but it cannot be checked and nothing rests on it).

Sources opened by me in this pass: 17 (12 primary papers: Gottman-Swanson-Murray 1999, Gottman-Levenson 1992, Rebound 1999, Timing 2000, Change 1999, Buehlman 1992, Carrere 2000, Carrere-Gottman 1999, Heyman-Slep 2001, Rinaldi 1998, Sprott 2004, Hamaker 2009, plus the Bielczyk preprint, the Gottman FAQ, and the Europe PMC abstracts of Madhyastha, Steele and Kim), besides the Crossref records.

**Verdict.** The file's main findings hold, and the full texts make them stronger: the threshold sign is right, every divorce-accuracy figure is an in-sample discriminant, and Heyman and Slep's cross-validation numbers are now read rather than second-hand. The errors were in the details. The worst was the newlywed Oral History result, where 87.4% was set against the wrong follow-up and called above chance when it is below it. Smaller ones were a missing row and a misplaced quotation in the Timing table, the wrong null rate for the 93.6% (now 85.1% on 47 couples), the 1999 sample's eligibility criterion, the count of screened codes, and an overstatement of what Rinaldi's 23 points do. Nothing still tagged [sa] feeds an equation, and the "no fitted ODE" claim now applies only to the Strogatz-Sprott-Rinaldi line.

## Cross-checks (2026-10-30)

Checked against the other prior-work files: a grep of every file in this directory for the same works, authors and numbers, then a read of the three files that cite these works most (`059`, `080`, `20-dyadic-coupling.md`), and the ledger lines already seeded from them (`docs/ledger.jsonl`). Ledger lines were returned to the orchestrator, not written to `docs/ledger.jsonl`. Nothing committed.

### Agreements

- **Threshold numbers.** `059` (summary item 1, section 5.2) and this file agree on the husband negativity threshold (-7.71 divorced, -5.36 stable, F(1,123) = 8.25, p < .01), the wife's null (F = 0.03), and the three-group test (-5.94, -5.29, -7.71; F = 2.22, n.s.).
- **Steady states.** `059` and this file agree on uninfluenced steady states separating the groups (F = 14.86 and 18.40).
- **Heyman and Slep 2001.** `20-dyadic-coupling.md` section 2 and this file agree on build-half PPV 65%, cross-validation PPV 28.81% (29%), and 21% at 16% prevalence.
- **93.6% attribution.** `20-dyadic-coupling.md` section 2 and this file agree that the Gottman FAQ ties the 93.6% to the 1992 Buehlman, Gottman and Katz study, and that the 94% figure is the same study.
- **Kim, Capaldi and Crosby 2007.** `20` and this file agree on pages 55-72, n = 85 at-risk couples, and the null for the 1998 affective variables.
- **Gottman, Swanson and Murray 1999 sample.** `080` section 1, `059` and this file agree on 130 recruited, 125 analysed, 17 divorced, 150 six-second blocks per spouse, and the -24 to +24 SPAFF score.
- **Hamaker, Zhang and van der Maas 2009.** `080`, `059` and this file agree that the Gottman-Murray model is a special case of the TAR model, with three dyads.
- **Strogatz's equations.** `20` section 2 and this file agree on R' = aJ, J' = -bR as printed by Bielczyk et al., and on the Math. Magazine volume discrepancy (61 in Crossref, 65 in Bielczyk).
- **Bielczyk et al. 2013 journal citation.** `20`, `060` and this file agree: J. Math. Sociol. 37(4):223-249, doi 10.1080/0022250x.2011.597279.
- **Rinaldi 1998.** `20` section 2 and this file agree on the SIAM citation, the cubic reaction term, the forgetting term and the damped response through Z.
- **Steele et al. 2014 finding.** `070` (line for the AICc model selection, independence most common) agrees with the abstract as read here.
- **Madhyastha et al. 2011 sample.** `080` and this file agree on 124 couples and 130 newlyweds (abstract only, in both).
- **Carrere et al. 2000.** `080` and this file agree on the journal citation, pages 42-58, and doi 10.1037/0893-3200.14.1.42.

### Contradictions

1. **Direction of the threshold finding.** `20-dyadic-coupling.md` section 1 and section 6 (Murray ch. 5 quoted; "treat the sign as unconfirmed") against `059` summary item 1 and this file, section 2 (Table 1 read at source: divorcing husbands had the more negative threshold). **Verdict: settled** by the table and both "lower" passages read in the validation log above. `20` was written before the primary text was read and still says unconfirmed; it should be updated.
2. **Whether the 94% figure was tested out of sample.** `20-dyadic-coupling.md` section 1, item 4 says cross-validation, base rates and one independent test "cut it down". This file, section 3.4 and 3.6, says Heyman and Slep used other, cross-sectional data and show that inflation is possible, not that it occurred in Gottman's data, and that the 93.6% study has no hold-out test. **Verdict: unresolved.** The `20` wording overstates what the critique shows about this figure.
3. **Gottman, Coan, Carrere and Swanson 1998, end page.** `080` section 1 gives 5-22 (its own note says end page from memory). This file gives Crossref's 5 only and notes that citing papers give 5-22 and 5-27. **Verdict: unresolved**, and nothing in either file depends on the end page.
4. **Sample size in the threshold study.** `059` (contradiction item 3) and `080` section 1 seemed to conflict on 124 against 125. This file resolves it as two different studies: 124 for Madhyastha et al. (abstract), 125 analysed in Gottman, Swanson and Murray (read). **Verdict: settled** by the read of the 1999 paper; the ledger line `L0878` can close.
5. **Identity of the "Psychometrika idiographic dyad" paper.** `070` section 5 lists it with no authors or DOI; `061` cites it as Steele and Ferrer. This file identifies it from Crossref as Steele, Ferrer and Nesselroade 2014, Psychometrika 79(4):675-700, doi 10.1007/s11336-013-9366-9; the content is abstract only. **Verdict: identity settled**, content still sa.

### Notes on provenance (not contradictions)

- `20` section 2 says Heyman and Slep's paper was not opened and Sprott's chaos example comes from lecture slides. Both are now read in full (here, validation log). Those lines in `20` are superseded.
- `20` says the Bielczyk arXiv preprint was read in full; this file read only its abstract and section 1. Any claim resting on the rest of the preprint is not checked here.
- `059` calls the negative threshold "the weak link"; this file says it is not the weakest of the significant parameters (the husband's influenced steady state, F = 4.36, is weaker). Both count the same four p < .05 parameters; the disagreement is about emphasis.
- The Kim et al. sample label "Oregon Youth Study" is `[abs]` in `20` and `[sa]` here (search summary of the reply). The label is not verified.

### Ledger

Lines for the ledger were returned to the orchestrator with `provenance`, `dup_of_file` and `cluster` F (research map section F, D187). Derived numbers (null-rule accuracies, PPV arithmetic, r and d) are tagged `derived` and may not feed v0 without the derivation shown. Lines from Steele et al. 2014, Madhyastha et al. 2011, Kim et al. 2007 and the Gottman-Levenson 1992/1999 classification counts are not `read` and stay out of any equation.
