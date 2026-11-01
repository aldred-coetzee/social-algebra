# Prior work 27: measuring drive and affect dynamics in people and groups

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: how drive-like quantities are measured and estimated over time, and how well. This serves the aim in `notes/2026-10-29-drives-as-the-core.md`: an algebra of drives that supports theorems and prediction or control. Prediction needs a measurable state. This file asks which states are.

**Method note.** Every DOI below was confirmed against the Crossref API (`api.crossref.org/works`) in this session; the DOI is the record I checked, and I list it. Numbers come from abstracts or summaries returned by fetch/search tools (a small summarising model sits between me and the page), not from my own reading of full texts. So nothing is tagged **[read]**. Everything is **[from abstract/standard account]** unless marked otherwise. Equations are the field's standard forms written from memory of the standard account and must be checked against the paper before use. "Drive" is used loosely here: almost all of this literature measures **affect** (valence/arousal), a symptom of a drive state, not the drive itself. That substitution is the main finding of the file (section K).

**Validation note (2026-10-29, second pass).** Every DOI was re-resolved against Crossref; all resolve. Numbers marked **[read]** were checked against the paper's own abstract or full text (PMC, Frontiers) through a fetch tool in the validation pass; still not a cover-to-cover reading. Corrections are listed in the validation log at the end.

**Summary.** Affect can be sampled in daily life, and its mean level, within-person variance and (weaker) autocorrelation can be estimated with acceptable reliability from tens to hundreds of prompts per person. Derived "dynamics" parameters (inertia, instability) correlate only about -.15 to -.2 with well-being and add little beyond mean and variance. Network and graphical-VAR models of symptoms replicate poorly. Implicit motives can be coded from stories but with low internal consistency, moderate retest, and near-zero correlation with questionnaires. Text-based emotion measures work as aggregate signals and are weak as individual or causal measures. Early-warning signals of transitions have one positive group-level human-affect study, a weak individual-level follow-up, and a 2024 review by the same research line concluding there is little support for them clinically. Group-level states are measured almost only as the aggregate of individual self-reports, plus a few lab studies of contagion. Momentary self-report measures of some named drive-like states do exist (state anxiety, craving, state curiosity, momentary communal and power motivation), but with modest within-person reliability (about .3 to .7 for momentary motives) and little validation against behaviour; there is no instrument that measures a named drive on a common, behaviour-validated scale that would let drives be compared or composed, and none at group level. *(Corrected in validation: the first draft said no validated momentary measure of a named drive exists at all, which overstated it.)*

---

## A. Experience sampling and ecological momentary assessment

**Citations.**
- Csikszentmihalyi, M. & Larson, R. (1987). Validity and reliability of the experience-sampling method. *J. Nervous and Mental Disease* 175(9), 526-536. DOI 10.1097/00005053-198709000-00004 (confirmed in validation). Reprinted in *Flow and the Foundations of Positive Psychology* (2014), DOI 10.1007/978-94-017-9088-8_3. Also Larson & Csikszentmihalyi chapter in *The Experience of Psychopathology*, Cambridge UP 1992, DOI 10.1017/cbo9780511663246.006.
- Vachon, H., Viechtbauer, W., Rintala, A. & Myin-Germeys, I. (2019). Compliance and retention with the experience sampling method over the continuum of severe mental disorders: meta-analysis and recommendations. *J. Medical Internet Research* 21(12), e14475. DOI 10.2196/14475 (confirmed in validation).- Shiffman, S., Stone, A. A. & Hufford, M. R. (2008). Ecological momentary assessment. *Annual Review of Clinical Psychology* 4, 1-32. DOI 10.1146/annurev.clinpsy.3.022806.091415.
- aan het Rot, M., Hogenelst, K. & Schoevers, R. A. (2012). Mood disorders in everyday life: a systematic review of ESM/EMA studies. *Clinical Psychology Review* 32, 510-523. DOI 10.1016/j.cpr.2012.05.007.
- Cranford, J. A., Shrout, P. E., Iida, M., Rafaeli, E., Yip, T. & Bolger, N. (2006). A procedure for evaluating sensitivity to within-person change: can mood measures in diary studies detect change reliably? *Personality and Social Psychology Bulletin* 32, 917-929. DOI 10.1177/0146167206287721.

**What is measured.** Self-reported state (mood, activity, company, location, motivation items) at random, fixed or event-contingent moments, via beeper or phone. The ESM tradition (Csikszentmihalyi) targets experience in context, including flow, which is a motivational state. EMA (Shiffman) targets symptoms and behaviour in real environments to avoid recall bias.

**Model/estimator.** None inherent. It is a sampling design. Data are analysed with multilevel models: y_{ti} = mu_i + e_{ti}, with person-level mu_i and within-person variance. The reliability concept that matters is *within-person* reliability (Cranford et al.): whether a scale detects change within a person, not whether it separates people. [from abstract/standard account]

**Reliability and validity.** Reported across the literature: compliance is design-dependent. A meta-analysis of ESM in mental-health samples (Vachon et al. 2019, JMIR; DOI confirmed, findings from a search summary) reports compliance rising with fixed schedules, higher incentives, fewer prompts per day and longer intervals, and falling with psychosis and with a higher proportion of men. A 2024 student EMA study reported mean compliance 76.9% (SD 27.7%) (search result, not verified). I could not confirm any single benchmark within-person reliability figure. The standard working number in the field is that multi-item momentary affect scales reach within-person reliability around .6 to .8, but this is **recalled, not found**. Treat as unconfirmed.

**Failures.** Reactivity (measuring changes the state), compliance bias (people in the worst states skip prompts), item-wording and response styles shifting over a session, short-timescale only (days to weeks of dense data), burden. Self-report of a *drive* (hunger, curiosity) at a moment is not validated against behaviour in most studies. Exceptions worth knowing (added in validation): momentary craving in EMA prospectively relates to smoking lapses (Shiffman, Paty, Gnys, Kassel & Hickcox 1996, *J. Consulting and Clinical Psychology* 64(2), 366-379, DOI 10.1037/0022-006x.64.2.366); daily state curiosity was measured by diary in Kashdan & Steger (2007, *Motivation and Emotion* 31, 159-173, DOI 10.1007/s11031-007-9068-7); and Schönbrodt, Zygar-Hoffmann, Nestler, Pusch & Hagemeyer (2022, *Behavior Research Methods* 54(4), 1869-1888, DOI 10.3758/s13428-021-01701-7) estimated the reliability of *momentary motive* scales in couples' ESM (communal, independence, power motivation): within-person, between-moment reliabilities .28 to .72, with communal about .63-.72 and power .40/.54 in two samples (n = 130 and 508 persons) **[read]**. State anxiety (STAI-S; Spielberger 1983, PsycTESTS DOI 10.1037/t06496-000) is a long-established state measure of a fear-related state, though built for repeated sessions rather than dense sampling. Lydon-Staley, Zhou, Blevins, Zurn & Bassett (2021, *Nature Human Behaviour* 5, 327-336, DOI 10.1038/s41562-020-00985-7) instead measured curiosity *behaviourally*, as Wikipedia browsing networks of 149 people over 21 days.

**What it gives an algebra.** The only practical way to put numbers on a drive-like state in a living person at the minutes-to-hours scale. Fix the unit of observation as "a self-reported intensity at time t". It does not give a drive; it gives a report.

---

## B. Affect dynamics: set point, variability, instability, inertia

**Citations.**
- Kuppens, P., Oravecz, Z. & Tuerlinckx, F. (2010). Feelings change: accounting for individual differences in the temporal dynamics of affect. *J. Personality and Social Psychology* 99(6), 1042-1060. DOI 10.1037/a0020962.
- Kuppens, P., Allen, N. B. & Sheeber, L. B. (2010). Emotional inertia and psychological maladjustment. *Psychological Science* 21(7), 984-991. DOI 10.1177/0956797610372634.
- Houben, M., Van Den Noortgate, W. & Kuppens, P. (2015). The relation between short-term emotion dynamics and psychological well-being: a meta-analysis. *Psychological Bulletin* 141(4), 901-930. DOI 10.1037/a0038822.
- Dejonckheere, E., Mestdagh, M., Houben, M., Rutten, I., Sels, L., Kuppens, P. & Tuerlinckx, F. (2019). Complex affect dynamics add limited information to the prediction of psychological well-being. *Nature Human Behaviour* 3, 478-491. DOI 10.1038/s41562-019-0555-0.
- Lapate, R. C. & Heller, A. S. (2020). Context matters for affective chronometry (Matters Arising on the above). *Nature Human Behaviour* 4, 688-689. DOI 10.1038/s41562-020-0860-7.
- Kuppens, P. & Verduyn, P. (2015). Looking at emotion regulation through the window of emotion dynamics. *Psychological Inquiry* 26(1), 72-79. DOI 10.1080/1047840x.2015.960505.

**What is measured.** Four time-series features of a person's affect ratings: (1) *home base / set point* (mean), (2) *variability* (within-person SD), (3) *instability* (mean squared successive difference, MSSD, which mixes variance and autocorrelation), (4) *inertia* (lag-1 autocorrelation).

**Model/estimator.** DynAffect treats valence and arousal as a stochastic process pulled to a home base. In the standard account it is an Ornstein-Uhlenbeck process: dX_t = -theta (X_t - mu) dt + sigma dW_t, with mu the home base, theta the attractor strength (inverse of inertia), sigma the sensitivity to perturbation, fitted in a Bayesian multilevel framework (Oravecz, Tuerlinckx & Vandekerckhove 2011, cited in the Kuppens abstract page, not checked). The equation form is **[from abstract/standard account]**; the abstract confirms home base, variability, attractor strength. In discrete time the AR(1) analogue is x_t = c + phi x_{t-1} + e_t with inertia = phi.

**Numbers.** Houben et al.: 793 effect sizes from 79 articles, N = 11,381, three-level meta-analysis. Pooled associations with (low) well-being: variability rho = -.178, instability rho = -.205, inertia rho = -.151; stronger for negative emotions than positive **[read: abstract]**. Dejonckheere et al.: 15 studies, 1,777 participants; dynamics measures are strongly interrelated and add "little added value over mean levels of positive and negative affect" **[read: abstract]**, i.e. little to prediction of life satisfaction, depressive symptoms and borderline symptoms once mean and variance of positive and negative affect are in the model (I did not obtain the R^2 increments).

**Failures.** The 2019 paper is a direct hit on the programme "dynamics parameters as person descriptors": mean and variance carry nearly all the predictive information for well-being. Lapate & Heller reply that the conclusion depends on context and that recovery after events matters more than the global autocorrelation. Parameters are estimated from 50 to 100+ points per person and are noisy. Note also that the outcomes are questionnaires, so the claim tested is cross-sectional prediction of a trait-like score, not prediction of the next state. That is a different question from the one the algebra asks.

**What it gives an algebra.** A ready-made *per-person state-space shape*: a level, an attractor, a restoring rate, a noise scale. An algebra of drives could use the OU form as the free dynamics of a drive (decay to a set point) with acts as impulses. The data show the set point and noise scale are what carry predictive information; the restoring rate adds little in questionnaire prediction (but see Lapate & Heller). It does not tell you what the drive is a drive *for*.

---

## C. Network psychometrics and dynamical systems views of mental states

**Citations.**
- Borsboom, D. & Cramer, A. O. J. (2013). Network analysis: an integrative approach to the structure of psychopathology. *Annual Review of Clinical Psychology* 9, 91-121. DOI 10.1146/annurev-clinpsy-050212-185608.
- Epskamp, S., Borsboom, D. & Fried, E. I. (2018). Estimating psychological networks and their accuracy: a tutorial paper. *Behavior Research Methods* 50, 195-212. DOI 10.3758/s13428-017-0862-1.
- Epskamp, S., Waldorp, L. J., Mottus, R. & Borsboom, D. (2018). The Gaussian graphical model in cross-sectional and time-series data. *Multivariate Behavioral Research* 53, 453-480. DOI 10.1080/00273171.2018.1454823.
- Bulteel, K., Tuerlinckx, F., Brose, A. & Ceulemans, E. (2016). Using raw VAR regression coefficients to build networks can be misleading. *Multivariate Behavioral Research* 51, 330-344. DOI 10.1080/00273171.2016.1150151.
- Bringmann, L. F. & Eronen, M. I. (2018). Don't blame the model: reconsidering the network approach to psychopathology. *Psychological Review* 125(4), 606-615. DOI 10.1037/rev0000108. (Two authors, not "et al."; corrected in validation.)
- Forbes, M. K., Wright, A. G. C., Markon, K. E. & Krueger, R. F. (2017). Evidence that psychopathology symptom networks have limited replicability. *J. Abnormal Psychology* 126(7), 969-988. DOI 10.1037/abn0000276 (resolves to the article itself in Crossref) and preprint 10.31234/osf.io/erw8m.

**What is measured.** Symptoms or states as nodes; edges are partial correlations (cross-sectional Gaussian graphical model, regularised by graphical lasso) or lagged regression coefficients (time-series graphical VAR). Centrality indices rank "influential" nodes.

**Model/estimator.** Cross-sectional: precision matrix Theta = Sigma^{-1}, edge weight = -Theta_ij / sqrt(Theta_ii Theta_jj), estimated with L1 penalty. Time series: multivariate VAR(1), x_t = Phi x_{t-1} + e_t, with a temporal network from Phi and a contemporaneous network from the residual covariance. [from abstract/standard account]

**Numbers and failures.** Forbes et al., two US epidemiological samples (n = 9,282 and n = 8,841), depression and generalised-anxiety symptoms: association networks stable; the three conditional-independence network types replicated poorly; 44% of symptoms were "most influential" on at least one centrality index across six networks; only 13-21% of edges were consistently estimated across networks **[read: abstract]**. They suggest symptom measurement error. (Sample sizes are from the first draft and were not re-checked; the abstract names the surveys, NCS-R and NSMHWB, not the n.) Bulteel et al. show raw VAR coefficients can mislead network inferences. Bringmann et al. defend the approach as a model class while granting the estimation problems. Centrality is not shown to identify intervention targets.

**What it gives an algebra.** The VAR coefficient matrix Phi is the nearest existing thing to a *linear interaction law among states within one person*: how a rise in one state at t shifts others at t+1. If drives were measurable, Phi would be the estimate of drive-to-drive coupling (fear suppresses curiosity). The replication record says the edge-level structure is not yet trustworthy at typical sample sizes. It also assumes stationarity and linearity, and the stationarity assumption fails exactly when a regime shift occurs.

---

## D. Idiographic versus nomothetic: ergodicity and dynamic SEM

**Citations.**
- Molenaar, P. C. M. (2004). A manifesto on psychology as idiographic science. *Measurement* 2(4), 201-218. DOI 10.1207/s15366359mea0204_1.
- Fisher, A. J., Medaglia, J. D. & Jeronimus, B. F. (2018). Lack of group-to-individual generalizability is a threat to human subjects research. *PNAS* 115(27), E6106-E6115. DOI 10.1073/pnas.1711978115.
- Asparouhov, T., Hamaker, E. L. & Muthen, B. (2018). Dynamic structural equation models. *Structural Equation Modeling* 25(3), 359-388. DOI 10.1080/10705511.2017.1406803.
- Hamaker, E. L., Asparouhov, T., Brose, A., Schmiedek, F. & Muthen, B. (2018). At the frontiers of modeling intensive longitudinal data: dynamic structural equation models for the affective measurements from the COGITO study. *Multivariate Behavioral Research* 53, 820-841. DOI 10.1080/00273171.2018.1446819.

**What is measured / argued.** Molenaar: a process is *ergodic* if between-person structure equals within-person structure; psychological processes generally are not (non-stationary, heterogeneous), so group findings do not license individual claims, and conversely. Fisher et al.: six repeated-measures data sets, each 87 to 94 participants with equal numbers of assessments per person; group and individual central tendencies agreed to some degree, but "the variance around the expected value was two to four times larger within individuals than within groups" **[read: abstract]** (first draft said "than between groups"; corrected).

**Model/estimator.** DSEM is multilevel time-series modelling with latent variables in Bayesian estimation (Mplus): level 1, y_{ti} = mu_i + phi_i (y_{t-1,i} - mu_i) + e_{ti}, with person-specific mu_i, phi_i, and residual variance, all random effects at level 2 and predicted by person covariates. It is the estimator that carries "the dynamics of a person, drawn from a population of dynamics". [from abstract/standard account]

**Failures.** Fisher et al. is about as strong a warning as exists for the aim: a law fitted on the group may not hold for any single person, so an algebra whose operators are fitted from group data cannot be assumed to apply to an individual. DSEM mitigates by allowing heterogeneity, at the cost of needing many time points per person and assuming stationarity after detrending.

**What it gives an algebra.** The statistical *type* of an estimable drive law: population-level hyperparameters over person-level parameters. In algebra terms, operators have person-indexed coefficients. That suggests laws should be stated with parameters that vary by person and be tested by hierarchical estimation, not stated as universal constants. Compare file 07's finding that individual-level prediction has a poor record.

---

## E. Measuring motives: implicit versus explicit

**Citations.**
- McClelland, D. C., Koestner, R. & Weinberger, J. (1989). How do self-attributed and implicit motives differ? *Psychological Review* 96(4), 690-702. DOI 10.1037/0033-295x.96.4.690.
- Spangler, W. D. (1992). Validity of questionnaire and TAT measures of need for achievement: two meta-analyses. *Psychological Bulletin* 112(1), 140-154. DOI 10.1037/0033-2909.112.1.140.
- Schultheiss, O. C., Liening, S. & Schad, D. (2008). The reliability of a Picture Story Exercise measure of implicit motives: estimates of internal consistency, retest reliability, and ipsative stability. *J. Research in Personality* 42, 1560-1571. DOI 10.1016/j.jrp.2008.07.008.
- Köllner, M. G. & Schultheiss, O. C. (2014). Meta-analytic evidence of low convergence between implicit and explicit measures of the needs for achievement, affiliation, and power. *Frontiers in Psychology* 5, 826. DOI 10.3389/fpsyg.2014.00826.
- Schultheiss, O. C. & Brunstein, J. C. (eds.) (2010). *Implicit Motives*. Oxford UP. DOI 10.1093/acprof:oso/9780195335156.001.0001 (record only).

**What is measured.** Three motive dispositions (achievement, affiliation/intimacy, power), the closest thing in psychology to measured *drives* of a social kind. Implicit measure: the Picture Story Exercise (PSE; a descendant of McClelland's TAT) where participants write stories to ambiguous pictures; trained coders score imagery for motive content using a manual (Winter's system for power, Heyns/McClelland for achievement and affiliation). Explicit measure: questionnaires of self-attributed motives.

**Model/estimator.** Coding is a count of scored imagery categories per story, corrected for word count. No dynamical model. McClelland et al.'s claim: implicit motives predict spontaneous operant behaviour over time; self-attributed motives predict responses to specific, immediate demands. [from abstract/standard account]

**Numbers.**
- Köllner & Schultheiss (meta-analysis of 49 papers, 56 samples, 6,151 participants): implicit-explicit correlation corrected for sampling and measurement error rho = .130 overall (95% CI .077-.183), .139 achievement, .116 affiliation, .038 power (n.s.); corrected for sampling error only, .095; raw mean of correlations .073 **[read: abstract and Table 4]**. *(First draft gave r = .088, which matches none of the reported figures; corrected.)* The implicit-explicit gap is real and large, and for power essentially zero.
- Retest of PSE scores: about .60 at one week, .52 at one month, .37 at one year. These are averages from a meta-analysis by Schultheiss & Pang (2007, "Measuring implicit motives", in *Handbook of Research Methods in Personality Psychology*, Guilford, pp. 322-344), as cited in the introduction of Schultheiss et al. 2008, not results of the 2008 study itself (attribution corrected; figures not checked in the chapter). Internal consistency is low and the authors argue that this is expected, because picture-to-picture variation carries validity.
- Spangler 1992: 105 articles; TAT-based measures correlated with outcomes more than questionnaires on average. A secondary source (a critical letter in the APS *Observer*, one side of a debate) quotes average rs of .19 and .22 for two classes of real-world achievement criteria (secondhand; could not confirm which is which). Treat as "r about .2".

**Failures.** Low internal consistency; manual coding is labour-intensive; correlation with outcomes about .2; the two measure families disagree, so "how strong is this person's power drive?" has two answers that barely correlate. Automated coding of PSE text exists but I did not survey it.

**What it gives an algebra.** A genuinely drive-like *trait-level* measure of three social drives, with retest stable enough (about .5 over a month) to treat as slow state. It gives scale and ranking, not an interval-scale quantity with a unit, and nothing at time-scale of minutes. The implicit/explicit gap tells the algebra it needs two components per person: the drive and the self-model of the drive.

---

## F. Text-based measurement of emotion and motive at scale

**Citations.**
- Tausczik, Y. R. & Pennebaker, J. W. (2010). The psychological meaning of words: LIWC and computerized text analysis methods. *J. Language and Social Psychology* 29, 24-54. DOI 10.1177/0261927x09351676. (The LIWC2015 manual, Pennebaker et al., not found in Crossref; **Unconfirmed**.)
- Graham, J., Haidt, J. & Nosek, B. A. (2009). Moral Foundations Dictionary (PsycTESTS record). DOI 10.1037/t48554-000. The paper behind it, "Liberals and conservatives rely on different sets of moral foundations", *JPSP* 96(5), 1029-1046, DOI 10.1037/a0015141 (confirmed in validation).
- Dodds, P. S., Harris, K. D., Kloumann, I. M., Bliss, C. A. & Danforth, C. M. (2011). Temporal patterns of happiness and information in a global social network: hedonometrics and Twitter. *PLoS ONE* 6(12), e26752. DOI 10.1371/journal.pone.0026752.
- Kloumann, I. M., Danforth, C. M., Harris, K. D., Bliss, C. A. & Dodds, P. S. (2012). Positivity of the English language. *PLoS ONE* 7. DOI 10.1371/journal.pone.0029484.
- Dodds, P. S. et al. (2015). Human language reveals a universal positivity bias. *PNAS* 112(8), 2389-2394. DOI 10.1073/pnas.1411678112. Critique: Garcia, D., Garas, A. & Schweitzer, F. (2015). The language-dependent relationship between word happiness and frequency. *PNAS* 112(23), E2983. DOI 10.1073/pnas.1502909112; reply Dodds et al., DOI 10.1073/pnas.1505647112. (Earlier related paper by the same critics: Garcia, Garas & Schweitzer 2012, Positive words carry less information than negative words, *EPJ Data Science* 1, DOI 10.1140/epjds3.)
- Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A. & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS* 114, 7313-7318. DOI 10.1073/pnas.1618923114.
- Burton, J. W., Cruz, N. & Hahn, U. (2021). Reconsidering evidence of moral contagion in online social networks. *Nature Human Behaviour* 5, 1629-1635. DOI 10.1038/s41562-021-01133-5.
- Rathje, S., Van Bavel, J. J. & van der Linden, S. (2021). Out-group animosity drives engagement on social media. *PNAS* 118. DOI 10.1073/pnas.2024292118.
- Kramer, A. D. I., Guillory, J. E. & Hancock, J. T. (2014). Experimental evidence of massive-scale emotional contagion through social networks. *PNAS* 111, 8788-8790. DOI 10.1073/pnas.1320040111.

**What is measured.** Word-frequency scores. LIWC counts words per psychological category (affect, social, power, etc.) per text. The Moral Foundations Dictionary counts words per moral foundation. The hedonometer takes the frequency-weighted mean of crowd-rated happiness scores of words (labMT: about 10,000 words rated on a 1-9 scale by raters recruited on Mechanical Turk). Aggregate over a day or place gives a "happiness" time series.

**Model/estimator.** Hedonometer, standard form: h_avg(T) = sum_i h_i f_i(T) / sum_i f_i(T), with h_i the rated happiness of word i, f_i its frequency in text T. [from abstract/standard account]

**Numbers and failures.**
- Brady et al.: 563,312 social media messages on three polarising issues; each additional moral-emotional word raised diffusion (retweets) by about 20% **[read: abstract]**. Burton et al. found a deliberately implausible "XYZ contagion" model performed no worse than the moral-contagion model, using out-of-sample prediction, model comparison and specification-curve analysis **[read: abstract]**. (The first draft's "counting the letters X, Y and Z" and "six corpora" are not in the abstract and were not checked.) Their argument is that significance testing on noisy, high-dimensional social media data is not sufficient evidence.
- Rathje et al. (2021) report that out-group animosity drove engagement more than moral-emotional words; I did not read the numbers.
- Kramer et al.: 689,003 Facebook users, positive or negative posts down-weighted in feeds; downstream posts shifted in the same direction, with effect sizes "as small as d = 0.001", the largest about d = 0.02 (the drop in positive words when positive posts were reduced) **[read: PMC full text]**. Statistically detectable at scale, negligible per person. Published with ethics controversy.
- Dodds et al. 2015's frequency-independent positivity bias was challenged by Garcia et al. (2015 PNAS letter): their reanalysis against a larger lexicon found the data did not support frequency independence, and they argued the emoticon-based rating scale adds bias. Dodds et al. replied that the critique rests on misconceptions about frequency and rank. *(First draft attributed the critique to "rater acquiescence"; that was not the argument; corrected from search summaries of the letter and reply.)*
- Word-count tools measure *what is said*, not *what is felt*; sarcasm, negation, context and genre swamp small effects. Validity against self-reported mood at the individual level is modest (not checked here; **Unconfirmed**).

**What it gives an algebra.** The only route to group-scale and long time-scale measurement (days to years, millions of people). It measures expressed affect in public text, which is a filtered output of drives, not drive state. Useful for calibrating group-level aggregate dynamics (e.g. spikes, decays after events), not for individual drive estimation. The Burton critique says: before trusting any contagion law fitted to text data, test it against a null predictor.

---

## G. Physiological and digital phenotyping

**Citations.**
- Mohr, D. C., Zhang, M. & Schueller, S. M. (2017). Personal sensing: understanding mental health using ubiquitous sensors and machine learning. *Annual Review of Clinical Psychology* 13, 23-47. DOI 10.1146/annurev-clinpsy-032816-044949.
- Onnela, J.-P. & Rauch, S. L. (2016). Harnessing smartphone-based digital phenotyping to enhance behavioral and mental health. *Neuropsychopharmacology* 41, 1691-1696. DOI 10.1038/npp.2016.7.
- Onnela, J.-P. (2021). Opportunities and challenges in the collection and analysis of digital phenotyping data. *Neuropsychopharmacology* 46, 45-54. DOI 10.1038/s41386-020-0771-3.

**What is measured.** Passive sensor streams (GPS mobility, accelerometer, call and text logs, sleep, typing, voice) used as proxies for mood, social engagement or symptom state. Wearables add heart rate, heart-rate variability, electrodermal activity.

**Model/estimator.** Feature extraction then regression or classifier (supervised learning on self-reported or clinical labels). [from abstract/standard account]

**Numbers and failures.** From search summaries of systematic reviews (2021-2025; I did not open them): four studies reported predictive accuracy of 81-91%, better for personalised or multimodal models; only 9 longitudinal studies of at least 12 weeks met criteria, with sample sizes 45 to 2,200, and only one distinguished depressive *states*; reviews flag heterogeneity, reproducibility, adherence and privacy. High accuracy figures in small, within-sample studies; I found no evidence of robust out-of-sample prediction of an affective or motivational state. Physiological signals are not specific to any emotion (arousal is measurable, valence and drive identity are not) (standard account; **not checked** in this session).

**What it gives an algebra.** A route to continuous, low-burden, observer-side measurement of behavioural *activity* (movement, contact), which maps better onto approach/withdrawal than onto named drives. It is the only candidate for dense longitudinal data with no self-report burden; its link to drive state is statistical and unvalidated.

---

## H. Group-level states: affective tone, contagion, team climate

**Citations.**
- George, J. M. (1990). Personality, affect, and behavior in groups. *J. Applied Psychology* 75(2), 107-116. DOI 10.1037/0021-9010.75.2.107 (the paper introducing *group affective tone*; I first recalled the wrong journal, Crossref corrected it). Follow-up comment: George, J. M. & James, L. R. (1993), *J. Applied Psychology* 78(5), 798-804, DOI 10.1037/0021-9010.78.5.798, on aggregation.
- Bartel, C. A. & Saavedra, R. (2000). The collective construction of work group moods. *Administrative Science Quarterly* 45, 197-231. DOI 10.2307/2667070.
- Barsade, S. G. (2002). The ripple effect: emotional contagion and its influence on group behavior. *Administrative Science Quarterly* 47(4), 644-675. DOI 10.2307/3094912.
- Rime, B. (2009). Emotion elicits the social sharing of emotion: theory and empirical review. *Emotion Review* 1, 60-85. DOI 10.1177/1754073908097189.
- Butler, E. A. (2015). Interpersonal affect dynamics: it takes two (and time) to tango. *Emotion Review* 7, 336-341. DOI 10.1177/1754073915590622.
- Ferrer, E., Steele, J. S. & Hsieh, F. (2012). Analyzing the dynamics of affective dyadic interactions using patterns of intra- and interindividual variability. *Multivariate Behavioral Research* 47(1), 136-171. DOI 10.1080/00273171.2012.640605.
- Hollenstein, T., Lichtwarck-Aschoff, A. & Potworowski, G. (2013). A model of socioemotional flexibility at three time scales. *Emotion Review* 5. DOI 10.1177/1754073913484181.

**What is measured.** Group affective tone: consistent, homogeneous affective reactions among group members, measured as the *mean* of members' self-reported mood, with a within-group agreement check. Team climate: aggregated survey items. Contagion: a confederate acts a mood in a lab group; coders and self-reports measure spread (Barsade, 2002). Dyads: coupled-oscillator or coupled-VAR models of two people's affect.

**Model/estimator.** Group tone = (1/n) sum_i x_i, accepted if within-group agreement exceeds a threshold. Dyadic coupling: x_{t+1}^A = a x_t^A + b x_t^B + e (cross-lagged), or coupled damped oscillator (Ferrer). [from abstract/standard account]

**Numbers and failures.** Barsade: a lab experiment, 2 x 2 design crossing pleasantness and energy, in which a trained confederate enacted one of four moods (cheerful enthusiasm, serene warmth, hostile irritability, depressed sluggishness); contagion was assessed by outside coders' ratings and self-reports; the positive-contagion groups reported better cooperation, less conflict and higher perceived task performance; contagion did not depend on the mood's pleasantness or energy (search summary; no effect sizes obtained). The group-level literature mostly aggregates individual self-reports and treats the average as the group state. This hides what an algebra of *group drives* needs: a measure that is not just a mean of members. I found no instrument that measures a group-level drive (e.g. group curiosity, group fear) as a quantity other than the mean of members' individual states or a survey scale on shared perceptions. Dyadic models need many time points from both partners and have been fitted mostly to couples, parents and children.

**What it gives an algebra.** The aggregation rule (mean plus agreement) is an existing, explicit *composition map* from individual states to a group state, and it is testable: does the mean predict group outcomes better than other statistics (variance, minimum, maximum)? Cross-lagged dyadic coupling is the existing form of "one person's state acts on another's".

---

## I. Critical slowing down as an early-warning signal

**Citations.**
- Scheffer, M. et al. (2009). Early-warning signals for critical transitions. *Nature* 461, 53-59. DOI 10.1038/nature08227.
- van de Leemput, I. A. et al. (2014). Critical slowing down as early warning for the onset and termination of depression. *PNAS* 111(1), 87-92. DOI 10.1073/pnas.1312114110.
- Wichers, M. & Groot, P. C. (2016). Critical slowing down as a personalized early warning signal for depression. *Psychotherapy and Psychosomatics* 85, 114-116. DOI 10.1159/000441458.
- Dablander, F., Pichler, A., Cika, A. & Bacilieri, A. (2023). Anticipating critical transitions in psychological systems using early warning signals: theoretical and practical considerations. *Psychological Methods* 28(4), 765-790. DOI 10.1037/met0000450.
- Smit, A. C., Helmich, M. A., Bringmann, L. F., Oldehinkel, A. J., Wichers, M. & Snippe, E. (2022 preprint). Critical slowing down in momentary affect as early warning signal of impending transitions in depression. DOI 10.31234/osf.io/u6vdg. (Authors confirmed in validation. This is *not* the 41-patient paper; that is the next entry.)
- Helmich, M. A., Smit, A. C., Bringmann, L. F., Schreuder, M. J., Oldehinkel, A. J., Wichers, M. et al. (2023). Detecting impending symptom transitions using early-warning signals in individuals receiving treatment for depression. *Clinical Psychological Science* 11(6), 994-1010. DOI 10.1177/21677026221137006 (confirmed in validation; first draft left it unattributed).
- Helmich, M. A., Schreuder, M. J., Bringmann, L. F., Riese, H., Snippe, E. & Smit, A. C. (2024). Slow down and be critical before using early warning signals in psychopathology. *Nature Reviews Psychology* 3(11), 767-780. DOI 10.1038/s44159-024-00369-y (added in validation).

**What is measured.** Near a tipping point a system recovers more slowly from small perturbations. Observable signatures in the time series: rising lag-1 autocorrelation, rising variance, rising cross-correlation between variables.

**Model/estimator.** Linearising near an equilibrium, x_{t+1} - x* = lambda (x_t - x*) + e; as the dominant eigenvalue lambda approaches 1, AR(1) = lambda rises and Var = sigma^2 / (1 - lambda^2) rises. Estimated in rolling windows. [from abstract/standard account]

**Numbers (van de Leemput; checked against PMC full text in validation, [read]).** General-population sample: 535 analysed of 621 recruited, all female (Belgian twin survey), 13.5% transitioned from normal to a DSM-IV major-depression diagnosis. Patients: 93 analysed of 118, from two treatment studies. Prompts about 10 per day for 5 or 6 days (up to 50-60 measurements). Higher autocorrelation, variance and cross-emotion correlations predicted worsening in the general sample and improvement in patients; the correlation between emotions was the authors' most robust indicator because variance can be confounded by changes in mean or in external noise. The main text reports significance (P < .05) and tertile plots only; effect sizes are in supplementary tables I did not see. The authors say accurate individual risk prediction is unlikely.

**Failures.** Dablander et al. (2023, simulation) find the signals depend strongly on the system's specifics and are very sensitive to noise. Helmich et al. (2023, *Clinical Psychological Science*): 41 depressed individuals starting treatment, EMA over 4 months (about 520 observations each), weekly symptoms over 6 months; rising autocorrelation in at least one variable preceded transitions in 89% of those with a transition but also appeared in 62.5% of those without; rising variance was rare and did not discriminate (about 11% vs 12%); the authors conclude limited value as personalised prediction (from search summaries of the abstract, not read). Helmich et al. (2024, *Nature Reviews Psychology*), from the same group as several of the positive studies, conclude there is little support for critical-slowing-down early-warning signals in clinical psychology and call for prospective, real-time tests. The method assumes a smooth approach to a bifurcation; transitions caused by external shocks are not preceded by slowing.

**What it gives an algebra.** The only *formal* prediction claim in this cluster that is an algebraic consequence of the dynamics: if a drive follows a state equation with a fold bifurcation, then variance and autocorrelation rise before the switch. This is a theorem-shaped statement (a property of the equation) with empirical tests, which is what the aim asks for. The empirical support in human affect is one positive group-level study, weak individual-level follow-ups (autocorrelation rises nearly as often without a transition), a theory paper warning about noise, and a 2024 review judging the clinical case unsupported.

---

## K. Which drive quantities are measurable, and how well

Reliability here is an overall judgment from the numbers above, not a pooled estimate.

| Quantity | Individual | Group | Time-scale | Status |
|---|---|---|---|---|
| Affect level (valence, arousal) by self-report | Yes, acceptable (multi-item, many prompts) | Mean of members | Minutes to weeks | Mature |
| Home base, variability | Acceptable, 50+ points per person | Mean and SD of members | Days to weeks | Mature; these carry most of the predictive content |
| Inertia, instability | Noisy; add little beyond mean and variance | Not defined | Days to weeks | Weak |
| Cross-state coupling (Phi in VAR) | Poor to fair; edge replication 13-21% in cross-sectional networks | Pooled across people, not individual | Days to weeks | Weak, contested |
| Implicit social motives (achievement, affiliation, power) | Fair; retest about .5 at a month, about .4 at a year; ties to behaviour r about .2; implicit-explicit rho about .13 | Not defined | Months to years | Established as a trait |
| Momentary named drive-like states (state anxiety, craving, state curiosity, communal/power motivation) | Exists; momentary motive reliability about .3 to .7; craving linked to lapses; little behavioural validation otherwise | No | Moments to days | Exists, thin; no common scale across drives |
| Named drives on a common, behaviour-validated scale | No instrument | No | n/a | Absent |
| Expressed emotion in public text | Weak per person | Good as aggregate | Hours to years | Established as aggregate |
| Contagion effect (text) | n/a | d = 0.001 in the one experiment; observational estimates disputed | Hours to days | Disputed |
| Physiological/sensor state | Arousal yes; valence/drive identity no; mood prediction unverified out of sample | Not defined | Seconds to weeks | Immature |
| Group affective tone | n/a | Mean plus agreement; lab-validated for mood | Hours to weeks | Established, thin |
| Early-warning signals of transition | Weak; low specificity | Not tested | Weeks (affect) | One positive group-level study; 2024 review: little clinical support |

---

## L. What exists versus what does not (blunt)

**Exists.**
- Reliable measurement of the *level and spread of self-reported affect* in a person at the day-to-week scale, and its aggregation to a group mean.
- A parametric dynamical form (set point, restoring rate, noise) with Bayesian multilevel estimators (DynAffect, DSEM, graphical VAR), usable as the template for a drive's free dynamics.
- A measured trait-level version of three social drives (achievement, affiliation, power) with a documented implicit/explicit split.
- Aggregate text-based indicators of public affect and moral language at scale.
- A theory-derived early-warning prediction (variance and autocorrelation rising before a transition), with one supporting human study and caveats.

**Does not exist.**
- A momentary measure of named drives (curiosity, fear, desire) on a common scale, validated against behaviour, that would let drives be compared or composed. *(Corrected in validation: momentary self-report measures of individual drive-like states do exist, e.g. state anxiety, craving, state curiosity, and momentary communal and power motivation with within-person reliability .28-.72 (Schönbrodt et al. 2022); what is missing is validation against behaviour and commensurability across drives.)*
- Evidence that dynamics parameters beyond mean and variance predict anything much.
- Replicable estimates of drive-to-drive coupling inside a person.
- Evidence that a law fitted on a group holds for an individual (the Fisher et al. result points the other way).
- A group-level measure of a group drive that is not a mean of individual states or a survey scale.
- Reliable, replicated, causal estimates of emotion or drive transmission between people outside the lab (the one large experiment is d = 0.001; the main observational claim failed an XYZ-null test).
- Out-of-sample prediction of an individual's future affective state from passive sensing.

**Consequences for the algebra (for Aldred's decision, not mine).**
1. The mature drive observables today are self-reported valence and arousal and trait motive scores; momentary self-reports of a few named drive-like states exist but are noisy and not on a shared scale. A drive algebra whose primitives are named drives has only a thin, uncalibrated measurement layer. Either the algebra defines its own measurement operationalisations (what counts as "fear level" in an observable) or the first theorems are about structure, not fit.
2. Because set point and variance carry most of the predictive information, the first testable content is the *static* part (levels, aggregation to the group), then OU-style decay, then coupling.
3. Because the data warn against group-to-individual transfer, laws should carry person-indexed parameters and be stated at the population level for what is shared.
4. The early-warning result is the best template for a *theorem with a test*: derive the signature from the state equation, then check it. Its empirical record (low specificity at the individual level) is also a template for how such a theorem can fail.

---

## Unconfirmed

- A within-person reliability benchmark of .6 to .8 for momentary affect scales: recalled, not found. (Related, not checked: Dejonckheere et al. on single-item momentary emotion reliability, reporting measurement error of about a tenth of the scale; venue not confirmed.)
- Pennebaker et al. LIWC2015 manual: no record found in Crossref (the Tausczik & Pennebaker 2010 paper stands in).
- Spangler 1992 criterion correlations of .19 and .22: secondary source (APS *Observer* letter); assignment to criteria not checked.
- PSE retest figures (.60 one week, .52 one month, .37 one year): confirmed as cited in Schultheiss et al. 2008's introduction from Schultheiss & Pang 2007; not checked in the 2007 chapter.
- Forbes et al. sample sizes (9,282 and 8,841): not in the abstract; not re-checked.
- Burton et al. details ("letters X, Y, Z"; "six corpora"): not in the abstract; not checked.
- Helmich et al. 2023 percentages (89% vs 62.5%; 11% vs 12%): from search summaries of the abstract.
- Dejonckheere et al. R^2 increments; Rathje et al. effect sizes; the 2025 passive-sensing reviews; Vachon et al. compliance moderators: from search summaries.
- Oravecz, Tuerlinckx & Vandekerckhove (2011), hierarchical Ornstein-Uhlenbeck model (*Psychometrika*): seen in search results, cited for the OU framing, not confirmed in Crossref (validation pass also could not resolve it).
- Not covered for lack of time: automated PSE coding; the Kalimeri/Garten moral-foundations-at-scale work; Rime's quantitative sharing rates; emotion-regulation dynamics measures beyond the Kuppens & Verduyn pointer.

## Missing work (flagged in validation)

- Momentary drive-like measures, now cited in section A: Schönbrodt et al. 2022 (momentary motive reliability), Kashdan & Steger 2007 (daily curiosity), Shiffman et al. 1996 (craving and lapse), STAI-S, Lydon-Staley et al. 2021 (behavioural curiosity). Still not surveyed: momentary loneliness items in ESM (common, but no dedicated validation study found), craving VAS psychometrics, and the ESM Item Repository.
- Helmich et al. 2024 (*Nat. Rev. Psychol.*), now cited in section I. "Bos et al." critiques of early-warning signals were requested but not located or checked.
- Within/between decomposition in panel data (e.g. Hamaker and colleagues' random-intercept cross-lagged panel model) is the standard companion to section D and is not surveyed here.

## Validation log (2026-10-29)

- Csikszentmihalyi & Larson 1987: ✎ corrected (original JNMD record confirmed, DOI 10.1097/00005053-198709000-00004; moved out of Unconfirmed).
- Shiffman, Stone & Hufford 2008: ✓
- aan het Rot et al. 2012: ✓
- Cranford et al. 2006: ✎ full author list added.
- Vachon et al. 2019: ✎ DOI confirmed (10.2196/14475); moved out of Unconfirmed.
- Kuppens, Oravecz & Tuerlinckx 2010: ✓
- Kuppens, Allen & Sheeber 2010: ✓
- Houben et al. 2015: ✓ [read: abstract] (793/79/11,381; -.178/-.205/-.151 all correct).
- Dejonckheere et al. 2019: ✓ [read: abstract] (15 studies, 1,777; conclusion correct).
- Lapate & Heller 2020: ✎ volume/pages added.
- Kuppens & Verduyn 2015: ✎ issue/pages added.
- Borsboom & Cramer 2013: ✓
- Epskamp, Borsboom & Fried 2018: ✓
- Epskamp et al. 2018 (MBR): ✓
- Bulteel et al. 2016: ✓
- Bringmann et al. 2018: ✎ corrected to Bringmann & Eronen (two authors), 125(4) 606-615.
- Forbes et al. 2017: ✓ [read: abstract] (44%, 13-21% correct); sample sizes ? unconfirmed.
- Molenaar 2004: ✓
- Fisher, Medaglia & Jeronimus 2018: ✎ "within individuals than within groups", not "between groups" [read: abstract]; 2-4x and 87-94 correct.
- Asparouhov, Hamaker & Muthén 2018: ✓
- Hamaker et al. 2018: ✓
- McClelland, Koestner & Weinberger 1989: ✓
- Spangler 1992: ✓ existence; ? .19/.22 unconfirmed.
- Schultheiss, Liening & Schad 2008: ✎ retest figures re-attributed to Schultheiss & Pang 2007 meta-analysis cited in its introduction.
- Köllner & Schultheiss 2014: ✎ r = .088 replaced by rho = .130 corrected (.095 sampling-error-only, .073 raw); power .038 n.s. [read].
- Schultheiss & Brunstein 2010: ✓
- Tausczik & Pennebaker 2010: ✓
- Graham, Haidt & Nosek 2009: ✎ JPSP paper confirmed, DOI 10.1037/a0015141.
- Dodds et al. 2011: ✓
- Kloumann et al. 2012: ✓
- Dodds et al. 2015: ✓
- Garcia, Garas & Schweitzer critique: ✎ wrong paper and wrong argument; the critique is the 2015 PNAS letter (10.1073/pnas.1502909112) on frequency dependence and scale bias, not "rater acquiescence".
- Dodds et al. 2015 reply: ✓
- Brady et al. 2017: ✓ [read: abstract] (563,312; 3 issues; 20%).
- Burton, Cruz & Hahn 2021: ✓ [read: abstract] for the XYZ-contagion result; ? details unconfirmed.
- Rathje et al. 2021: ✓ existence.
- Kramer, Guillory & Hancock 2014: ✓ [read: PMC] (N = 689,003; d as small as 0.001; added max about 0.02).
- Mohr, Zhang & Schueller 2017: ✓
- Onnela & Rauch 2016: ✓
- Onnela 2021: ✓ (Crossref issue date 2020, vol. 46 2021).
- George 1990: ✓; George 1993: ✎ is George & James 1993.
- Bartel & Saavedra 2000: ✓
- Barsade 2002: ✎ design detail added (2 x 2 pleasantness x energy, four enacted moods, coder and self-report).
- Rimé 2009: ✓
- Butler 2015: ✓
- Ferrer & Steele 2012: ✎ third author Hsieh; 47(1) 136-171.
- Hollenstein et al. 2013: ✓
- Scheffer et al. 2009: ✓
- van de Leemput et al. 2014: ✓ [read: PMC] (535/621 female, 13.5%, 93/118, 10/day x 5-6 days, correlations most robust, individual prediction unlikely).
- Wichers & Groot 2016: ✓
- Dablander et al. 2023: ✓
- Smit et al. 2022 preprint: ✎ authors confirmed; separated from the 41-patient paper.
- Helmich et al. 2023 (CPS, 41 patients): ✎ attributed and confirmed; figures added (search summary).
- Helmich et al. 2024: ✎ added.
- Schönbrodt et al. 2022; Kashdan & Steger 2007; Shiffman et al. 1996; Spielberger STAI; Lydon-Staley et al. 2021: ✎ added (DOIs confirmed).
- Oravecz et al. 2011: ? unconfirmed.
- LIWC2015 manual: ? unconfirmed.
- No fabricated works found; nothing ✗ removed.

**Verdict.** Every cited work exists and every DOI resolves, and the large headline figures (Houben, Forbes, Kramer, Brady, van de Leemput, Dejonckheere) are right. The errors were in the secondhand details: a wrong implicit-explicit correlation, a misattributed retest source, a mis-stated critique of the hedonometer, a "between groups" that should be "within groups", and an early-warning section that understated how weak the follow-ups are. The headline claim that no momentary measure of a named drive exists was overstated and has been narrowed to the absence of a behaviour-validated, commensurable one.

## Licences of quoted and transcribed material (2026-11-01)

- All sources in this file (about 70 papers, books and chapters in sections A-I; DOIs listed in the file) were seen through abstracts, PMC or Frontiers open-access text, or search summaries, not copied. Licence not determined; publisher copyright presumed, except the open-access papers noted below. Used as short quoted phrases (each under 30 words, for example "little added value over mean levels of positive and negative affect"), reported numbers (effect sizes, sample sizes, reliabilities, percentages) and equations written in our own standard-form notation.
- Open-access items from which numbers were read: Kramer, Guillory & Hancock 2014 (PNAS, via PMC), van de Leemput et al. 2014 (PNAS, via PMC), Köllner & Schultheiss 2014 (Frontiers in Psychology, open access), Dodds et al. 2011 and Kloumann et al. 2012 (PLoS ONE, open access, normally CC BY), Vachon et al. 2019 (JMIR, open access). The licence is not recorded in this file for any of them; only facts and numbers are taken.
- Table K is our own derived summary of reliability judgements, not a transcription of any source table; the numbers in it are facts taken from the cited studies.
- Datasets: none downloaded or reproduced. The labMT happiness lexicon, LIWC and the Moral Foundations Dictionary are mentioned as instruments only; none of their word lists is reproduced.
- No Wikipedia-derived text is used in this file (Lydon-Staley et al. measured curiosity from Wikipedia browsing; that is a study description, not Wikipedia text).
- No email addresses or personal contact details appear in this file.
