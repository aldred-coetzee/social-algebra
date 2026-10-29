# Prior work 098: is partner coupling real once inertia and set point are fitted? Madhyastha et al. 2011, Steele & Ferrer, and the open refits

Direction: D590
Date: 2026-10-29. Kind: deep-read. Cross-references: `088` (sections 1, 4: the abstract-only status of both target papers), `059`, `061` (Steele & Ferrer abstracts, Ferrer & Steele slides), `080` (Madhyastha sample sizes), `20-dyadic-coupling.md`.

## Method and honesty note (read this first)

**Neither target paper could be read.** Madhyastha, Hamaker & Gottman (2011) is closed access (APA; the Utrecht repository record, read through its REST API, says "Publisher version ... accessType: Closed Access"); Steele, Ferrer & Nesselroade (2014, Psychometrika; Cambridge page shows abstract and "Get access" only; Europe PMC says not in PMC, Unpaywall says no OA copy); Steele & Ferrer (2011, MBR; T&F returns 403, PubMed record is abstract only, Europe PMC "inPMC: N"). Routes tried: Crossref, OpenAlex, Unpaywall, Europe PMC, PubMed efetch, the Utrecht repository, publisher pages, web searches for author copies. Semantic Scholar rate-limited (429). Google Scholar returned 429. **Everything below about the three target papers is therefore [abs] (abstract only) and no number from them feeds anything.**

What *was* read at source in full, and carries the weight of this file:

- **de Haan-Rietdijk, Gottman, Bergeman & Hamaker (2016)**, Psychometrika 81(1):217-241, doi 10.1007/s11336-014-9417-x. Open (PMC4764683, fetched as full-text XML). Its Application 1 is an **independent refit of the Gottman newlywed data by the same group that wrote Madhyastha et al. (Hamaker is on both)**, using a different estimator (Bayesian multilevel threshold-VAR, BUGS) with inertia and set point (threshold) in the model and a partner term. This is the nearest thing to the Madhyastha result that can be read in full. **Caveat: same data, so it is a refit, not a replication.** [read]
- **Sels, Ceulemans, Bulteel & Kuppens (2016)**, Frontiers in Psychology 7:283, doi 10.3389/fpsyg.2016.00283 (CC BY; PMC4786571). Independent data (50 couples, experience sampling), per-couple VAR with own-lag terms. [read in full text]
- **Ferrer & Steele (2010) conference slides**, cilvr.umd.edu/Conference2010/CILVRposts2010/Ferrer_post.pdf. An early version of the Steele-Ferrer programme. Equation shapes and dyad counts legible; Greek lost in extraction for the oscillator equation, intact for the first-order Felmlee-Greenberg models. [read]
- Hamaker, Ceulemans, Grasman & Tuerlinckx (2015), Emotion Review 7(4):316-322, doi 10.1177/1754073915590619 (KU Leuven PDF). Read only for what it says about these studies; it only cites them. [read, partial]

Tags: **[read]** read at source; **[abs]** abstract or record only; **[derived]** my arithmetic from stated figures; **[sa]** secondary account (quoted by a paper I read; not the primary).

**Seed correction.** The seed DOI `10.1037/a0023923` is wrong: Crossref resolves it to Loaiza et al., *J. Exp. Psychol.: Learning, Memory, and Cognition* 37(5):1258-1263. The Madhyastha et al. DOI is **10.1037/a0023028** (Crossref: *J. Family Psychology*, 292-300, authors Madhyastha, Hamaker, Gottman; 088 had it right). "Steele & Ferrer 2011/2014" are **two different papers**, not one: 2011 is Steele & Ferrer, MBR 46(6):956-984, doi 10.1080/00273171.2011.625305 (damped linear oscillator as latent differential equation, daily affect); 2014 is Steele, Ferrer & Nesselroade, Psychometrika 79(4):675-700, doi 10.1007/s11336-013-9366-9 (AICc classification of dyads over differential-equation models). Both DOIs resolved on Crossref 2026-10-29.

## Summary

1. **At lag 6 seconds in marital conflict talk, the linear partner term is estimated at zero, with narrow intervals.** In the independent refit, the mean partner coefficient is 0.007 (95% CrI -0.020 to 0.035) for the husband (from the wife) and 0.018 (-0.007 to 0.044) for the wife [read]. Own-state inertia is 0.26 to 0.61 in the same model [read]. The partner term is excluded from zero in only 10.1% of couples' individual intervals for husband-to-wife influence (the wife's equation, β_W) and 6.2% for wife-to-husband (β_H) [read; direction labels corrected in validation, see log], against 5% expected by chance if every true coupling were zero [derived]. This matches the Madhyastha abstract's own phrasing: "only slightly greater than what would be expected by random association" [abs].
2. **At the scale of hours (experience sampling), 64% of 50 couples show no significant partner effect; the 36% that do are not a pattern.** Direction, valence, who-influences-whom all vary by couple [read]. Whether 36% exceeds chance is not settled by the paper (eight partner slopes per couple, no correction); under independence of the eight tests chance alone would give 34% [derived], though the tests are correlated, so true chance is lower.
3. **At the scale of days, the Steele-Ferrer line is split.** 2011 abstract reports coupled influences for positive and negative daily affect; the 2014 abstract reports that "the most likely interaction style was that of independence, without evidence of emotional interrelations" [abs]. The 2010 slides give independence as the largest single best-fit type (77 of 140 assigned dyads, 55%; 26% of 300) [read; [derived] percentages]. Models and samples differ, and I could not read either, so I do not resolve this.
4. **"Real once inertia and set point are fitted" has a different answer from "real before they are fitted".** The same group's framing is that for many people "initial state and emotional inertia dictate the outcome ... far more than the moment-to-moment affect of the spouse" [abs, Madhyastha]. The refit supports the arithmetic: inertia (0.26-0.61) is roughly 6 to 90 times the partner term, comparing interval limits with point estimates [derived].
5. **What *is* shared between partners is the set point, not a lagged influence.** Spouses' fitted thresholds correlate r = .60 (CrI .46 to .73); their lower-state inertias r = .25 (.05 to .45); upper-state inertias r = .09 (-.15 to .33) [read]. A couple resembles itself in where it settles without the partners moving each other in the moment.

---

## 1. Citations

- Madhyastha, T. M., Hamaker, E. L., & Gottman, J. M. (2011). Investigating spousal influence using moment-to-moment affect data from marital conflict. *Journal of Family Psychology* 25(2):292-300. doi 10.1037/a0023028 (Crossref-confirmed). PMID 21480708. Closed access. Abstract read via PubMed efetch. [abs]
- Steele, J. S., & Ferrer, E. (2011). Latent differential equation modeling of self-regulatory and coregulatory affective processes. *Multivariate Behavioral Research* 46(6):956-984. doi 10.1080/00273171.2011.625305 (Crossref-confirmed, Crossref has 41 references, no abstract). PMID 26736119. Abstract read via PubMed efetch. [abs]
- Steele, J. S., Ferrer, E., & Nesselroade, J. R. (2014). An idiographic approach to estimating models of dyadic interactions with differential equations. *Psychometrika* 79(4):675-700. doi 10.1007/s11336-013-9366-9 (Crossref-confirmed; 56 references; the Crossref record carries a Cambridge-terms licence start date of 2025-01-01, not an open licence). Abstract from Crossref and the Cambridge page. [abs]
- de Haan-Rietdijk, S., Gottman, J. M., Bergeman, C. S., & Hamaker, E. L. (2016). Get over it! A multilevel threshold autoregressive model for state-dependent affect regulation. *Psychometrika* 81(1):217-241. doi 10.1007/s11336-014-9417-x (Crossref-confirmed). PMC4764683. [read: introduction to the couples application, model, results, Table 4]
- Sels, L., Ceulemans, E., Bulteel, K., & Kuppens, P. (2016). Emotional interdependence and well-being in close relationships. *Frontiers in Psychology* 7:283. doi 10.3389/fpsyg.2016.00283. PMC4786571. CC BY. [read: whole text through Table 2 and the limitations paragraph start]
- Ferrer, E., & Steele, J. (2010). Modeling affect dynamics in dyadic interactions using differential equation models. Slides, Advances in Longitudinal Methods conference, College Park MD, 17-18 June 2010. cilvr.umd.edu/Conference2010/CILVRposts2010/Ferrer_post.pdf. [read]
- Felmlee, D. H., & Greenberg, D. F. (1999). A dynamic systems model of dyadic interaction. *Journal of Mathematical Sociology* 23(3):155-180. doi 10.1080/0022250X.1999.9990218 (Crossref-confirmed 2026-10-29). Cited in the slides, with Felmlee (2006), as the source of the first-order dyadic models. [sa: via the slides; not read]
- Gottman, J. M., Swanson, C., & Murray, J. D. (1999). The mathematics of marital conflict: Dynamic mathematical nonlinear modeling of newlywed marital interaction. *Journal of Family Psychology* 13(1):3-19. doi 10.1037/0893-3200.13.1.3 (Crossref-confirmed). The newlywed data source and the influence-function models: see `059`, `088`. Not re-read here.

---

## 2. Madhyastha, Hamaker & Gottman (2011)

### 2.1 What the abstract says [abs]

> "Gottman and colleagues proposed using a dynamical systems model to study dyadic interaction in marriage. In this model, each spouse's affect in each 6-s window is described as a function of an uninfluenced linear steady state and a nonlinear influence function of the partner's affect in the previous window. Recently, an alternative parameter estimation procedure for the equations of marriage was introduced, which is based on threshold autoregressive models. We apply this estimation procedure to data from a study of couples (N = 124) and newlyweds (N = 130) to compare different forms of spousal influence using the Bayesian information criterion. Although results show some statistically significant evidence for influence, this is only slightly greater than what would be expected by random association. One model of influence does not fit all couples. This suggests that for many people initial state and emotional inertia dictate the outcome of the conflict discussion far more than the moment-to-moment affect of the spouse. This latter finding is in conflict with most models of couples' interaction, which suggest that the outcome of conflict discussions are determined by the nature of the couples' mutual influence processes." (PubMed abstract, PMID 21480708)

Abstract-level content: two samples (124 "couples", 130 "newlyweds"); model selection by BIC over forms of influence, fitted per couple, with the set point ("uninfluenced linear steady state") and inertia in every model; headline result: significant influence barely above chance; no single influence form fits all couples.

### 2.2 What I could not obtain

The per-couple counts of couples whose BIC prefers an influence model over no influence; the number of influence forms compared; the BIC differences; the "slightly greater than random" figure itself; whether the 124-couple sample is the same as, or different from, the newlywed sample (`088`, `080`, `059` disagree about the figure of 125 vs 124 vs 130; I cannot settle this from the abstract). **All of these are unread and must not be filled from any other paper.**

### 2.3 What the refit says the paper did [sa, via de Haan-Rietdijk 2016, which I read]

"Madhyastha et al. (2011) analyzed these data using single-person TAR and AR models for each spouse, rather than a multilevel model. In their approach, the focus was on the way spouses influenced each other (and whether or not this influence was state-dependent), while inertia was always modeled as a fixed trait of the person." This is a statement by the refit's authors (Hamaker is common to both papers), tagged [sa] for what it says about Madhyastha.

---

## 3. Steele & Ferrer (2011) and Steele, Ferrer & Nesselroade (2014)

### 3.1 2011, MBR [abs]

> "We examine emotion self-regulation and coregulation in romantic couples using daily self-reports of positive and negative affect. We fit these data using a damped linear oscillator model specified as a latent differential equation ... Results indicate an absence of damping of relationship-specific affect within individuals. When both positive and negative affect are modeled at the individual level, the influence of positive affect is greater than that of negative affect. At the dyad level, the findings indicate coupled influences in both positive and negative affect between partners. With regard to positive affect, females are sensitive to their partners' overall displacement from average as well as their rate of change; males are sensitive only to their partners' displacement from average. For negative affect both partners are sensitive to each other's displacement from average, yet there are no coupled influences for rates of change in this dimension." (PubMed, PMID 26736119; abridged by me)

Abstract-level content: set point enters as "displacement from average"; the oscillator has self terms (position, velocity) and partner terms; partner **displacement** coupling reported for both partners and both valences; partner **velocity** (rate-of-change) coupling only for positive affect and only in one direction (the female is sensitive to the male's rate of change; the male is not sensitive to hers), and none for negative. No sample size, estimate, SE or fit statistic is in the abstract. **The abstract does not say how many couples showed the coupling, nor how large it is**, which is what the direction asks for; unread.

### 3.2 2014, Psychometrika [abs]

> "We fitted each model to each of the dyads and the resulting AICc values were used to classify the most likely configuration of interaction for each dyad. ... Results indicated that, within our sample, the most likely interaction style was that of independence, without evidence of emotional interrelations between the two individuals in the couple. Attachment-related avoidance and anxiety showed significant relations with model parameters ... Analysis involving distal outcomes showed modest influences from the individual's level of ideal affect." (Crossref abstract; abridged by me)

Abstract-level content: per-dyad model comparison by AICc over alternative configurations of interaction (the set includes independence, so inertia/set point without coupling is a competitor); parameters then averaged across models by AICc weight; "ideal affect" is the set point; distal outcomes (satisfaction, status) predicted "modestly" from the individual's ideal affect, **not** from the coupling parameters in the abstract's wording. Note (added in validation): the same abstract does report a model-averaged **coregulation** parameter per person and relates it to predictors: males' "own levels of anxiety had positive effects on their levels of dyadic coregulation", and "for females coregulation was negatively influenced by both time in the relationship and their partner's level of avoidance". So "independence" is the modal best-fit type, but the averaged coupling parameter is estimated and varies systematically with attachment; sizes unread.

### 3.3 The 2010 slides: the model family behind the 2014 classification [read]

Verbatim equations from the slides (Felmlee-Greenberg form; x* and y* are each member's ideal-affect set point):

- General: dx/dt = a1 (x* - x) + a2 (y - x); dy/dt = b1 (y* - y) + b2 (x - y)
- Model 1, both cooperative: all four terms, with a1, a2, b1, b2 restricted > 0.
- Model 2, both independent: dx/dt = a1 (x* - x); dy/dt = b1 (y* - y).
- Model 3, both contrarians: dx/dt = -a2 (y - x); dy/dt = -b2 (x - y).
- Model 4, one uncooperative (x), one dependent (y): dx/dt = a1 (x* - x) - a2 (y - x); dy/dt = b2 (x - y).
- Fitted per dyad with SAS PROC MODEL, FIML, ideal affect fixed at .70 for proportional positive affect (the SAS example); N dyads = 300; data are 60 to 90 consecutive daily reports.
- Results: "140 dyads showed one model as best fit; 159 showed a differential fit pattern", then a k-means step forced dyads into a model. Counts: Model 1: 6; Model 2: 77; Model 3: 11; Model 4a (female uncooperative, male dependent): 42; Model 4b: 4. These sum to 140 [derived]; the slides do not say whether the 159 were assigned by the clustering step (flagged already in `061`).
- The slides' own conclusions: "it is difficult to summarize information from the individual (i.e., dyad) to the group", and the analyses "were guided by theoretical models; without any theory this summary is harder".

**This is a different model class from the oscillator of 2011 and from the TAR of Madhyastha.** The "independent" model (Model 2) has a set point and first-order return and no partner term; "cooperative" has the partner term. The best-fit counts say that independence is the largest single type and coupling types (1, 3, 4a, 4b) together are 63 of 140 = 45% [derived], but with model choice done by a clustering heuristic, not a clean likelihood test. Whether the 2014 paper uses these 300 dyads is not stated in anything I read.

---

## 4. The refit I could read: de Haan-Rietdijk et al. 2016, Application 1

### 4.1 Data [read]

129 newlywed couples (Gottman, Swanson & Murray 1999; Gottman, Murray & Swanson 2005); 15-minute conflict discussion; SPAFF coded per second by two observers, averaged over 6-s intervals and coders, T = 150 per spouse. Scores below 0.1 are negative behaviour, above 0.1 positive, 0.1 neutral. "Since we detected no gross violations of stationarity ... we used the raw data."

### 4.2 Model, transcribed [read]

For husband H and wife W in couple i, bivariate multilevel threshold-VAR (husband's equation; "similarly for the wife"):

H(t,i) = τ_H,i + φ_1,H,i (H(t-1,i) - τ_H,i) + β_H,i (W(t-1,i) - τ_W,i) + ε_H,t,i   if H(t-1,i) < τ_H,i
H(t,i) = τ_H,i + φ_2,H,i (H(t-1,i) - τ_H,i) + β_H,i (W(t-1,i) - τ_W,i) + ε_H,t,i   if H(t-1,i) ≥ τ_H,i

with ε ~ N(0, σ²), and φ_1, φ_2 (inertia below / above threshold), τ (the threshold, which also serves as the set point) and β (the partner influence) each having a population mean plus a couple-specific random effect. Eight random effects per couple (four inertias, two thresholds, two β), multivariate normal. "The model allows the inertia parameter to be state-dependent."

Important features for this direction: (i) the partner term is **linear** in the partner's deviation from the partner's own set point; the nonlinear O-Jive influence function of Gottman-Murray is not fitted here; (ii) the partner enters only at **lag 1 = 6 seconds**; (iii) inertia, set point, and a partner term are all in one model, so the question "is coupling real once the other two are fitted" is answered inside a single estimate.

### 4.3 Results, Table 4 and text [read]

| Parameter | Husbands | Wives |
|---|---|---|
| mean inertia, lower (negative) state, γφ1 | 0.61 [0.57, 0.65] | 0.60 [0.56, 0.64] |
| mean inertia, upper (positive) state, γφ2 | 0.29 [0.24, 0.34] | 0.26 [0.20, 0.31] |
| difference γφ2 - γφ1 | -0.32 [-0.39, -0.25] | -0.35 [-0.42, -0.27] |
| mean threshold / set point, γτ | 0.07 [0.006, 0.139] | 0.08 [0.01, 0.15] |
| **mean partner influence, γβ** | **0.007 [-0.020, 0.035]** | **0.018 [-0.007, 0.044]** |

Intervals are 95% credible intervals. Gender comparisons (wife minus husband): γφ1 -0.007 [-0.056, 0.043]; γφ2 -0.03 [-0.11, 0.04]; γτ 0.007 [-0.059, 0.071]. Spouse correlations: rφ1 = .25 [.05, .45]; rφ2 = .09 [-.15, .33]; rτ = .60 [.46, .73]. The paper reports Cohen's d for the inertia difference as 3.9 (men) and 20 (women), computed from between-person variances; I do not use them (a d of 20 is a property of tiny between-person variance of the difference, not a meaningful effect size).

Verbatim on the partner term: "We also found no evidence of (linear) moment-to-moment influence between the spouses, since the 95% credible intervals for the average (level-2) influence in both directions included zero. To check whether this was caused by some couples having an opposite influence pattern of other couples, we also inspected the 95% credible intervals for the individual couples, and these included zero for 89.9% of the husband-to-wife influence parameters, and 93.8% of the wife-to-husband influence parameters. Thus, we concluded that there was little evidence of linear influence between the spouses at this time lag. Note that this result is in line with the previous findings of Madhyastha et al. (2011)."

### 4.4 Derived quantities [derived]

- Approximate standard errors of the mean partner coefficient, from the interval half-width / 1.96: husband about 0.014, wife about 0.013. (A posterior SD is not reported.)
- Share of couples whose individual interval excludes zero: 10.1% and 6.2%. A well-calibrated 95% interval would exclude a true zero about 5% of the time. So there is a small excess at most (10.1% for husband-to-wife), and the paper treats it as little evidence. The shrinkage in a multilevel model pulls individual estimates toward the (near-zero) mean, which would reduce exclusions, so this is not a clean test of per-couple heterogeneity.
- Inertia relative to coupling: 0.26 to 0.61 against an upper bound of 0.044 for the partner term, so own state carries at least 6 times the weight of the partner term at the upper end of the interval and far more at the point estimate [derived]; the exact ratio is not meaningful, the order of magnitude is.
- Scale of units: SPAFF composite on its own scale (neutral 0.1); β is a unit-per-unit slope on the SPAFF composite, not standardised.

### 4.5 What this does and does not settle

It settles, for this dataset, a linear lag-1 (6 s) partner effect on SPAFF composites: near zero, tightly bounded. It does **not** test (a) the nonlinear O-Jive influence function (whose threshold parameter was the one that predicted divorce in `059`/`088`), (b) longer lags, (c) the partner's *velocity*, (d) other channels such as physiology, (e) other populations or tasks. Same data as Madhyastha, so agreement is not independent confirmation of the data-generating process, only of the analysis.

---

## 5. A second open test on independent data: Sels et al. 2016

### 5.1 Design [read]

50 heterosexual couples (100 participants), relationship length 2 months to 35 years (M = 72.06 months, SD = 107.79), age 18-70 (M = 27.75, SD = 10.60); 10 married, 18 cohabiting, 22 living apart. Experience sampling 10 times a day for 7 days, 10:00 to 22:00, simultaneous signals; compliance 92.03% (M = 64.40 signals); on average 48.34 usable lag pairs per couple (overnight lags excluded). Emotions: sliders 0 to 100, four negative items (angry, anxious, depressed, sad) and four positive (relaxed, satisfied, happy, cheerful), averaged within person-centred. Mean gap between signals 1 h 12 min 12 s (SD 29 min).

### 5.2 Model [read]

Per-couple lag-1 VAR: each of four variables (own PE, own NE, partner PE, partner NE) at t regressed on all four at t-1. 16 slopes per couple, 8 actor and 8 partner. Own-lag (actor) terms and intercepts are in the model, so the partner effect is "after all intrapersonal effects ... are taken into account" (their wording). Standardised slopes inspected. A set-point is implicit as the intercept (mean-centred data). Sensitivity: with 48.34 time points, f² needed for power .80 is 0.17 (a medium effect).

### 5.3 Results [read]

- Partner effects significant (p < .05) for at least one of 8 partner slopes in **18 of 50 couples (36%)**. With three predictors (own two emotions plus one partner emotion): 20 of 50 (40%). Restricting to time points when partners had been in contact: 18 of 49 (37%).
- Among the 18: men unidirectionally influence women in 50% (n = 9), women unidirectionally influence men in 39% (n = 7), bidirectional only 11% (n = 2). Similar-emotion paths 50%, opposite-valence paths 28%, both 22%. Both valences predicted in 11%, only negative 39%, only positive 50%. Sign of the influence "could be positive or negative depending on the specific couple". Gender differences in path frequency not significant (Fisher p = .10 and .50).
- The authors' summary: "The majority of couples (64%) did not demonstrate strong signs of emotional interdependence, and couples that did, showed great inter-dyad differences in their specific patterns."
- Slope magnitudes (standardised) are not reported in the text I read, beyond the density measure (mean absolute partner slope) used as predictor; no SEs for individual slopes.

### 5.4 Chance level [derived]

If the eight partner-slope tests were independent at alpha = .05, P(at least one significant) = 1 - 0.95^8 = 33.7%. The observed 36% is about the same. The tests are positively correlated within a couple (the authors cite variance-inflation and multicollinearity problems), which lowers the true chance rate, so 36% is probably somewhat above chance, but the paper does not compute a null rate. This is the same sort of "slightly greater than random" that Madhyastha et al. report on a different timescale.

### 5.5 Does the coupling predict anything? [read]

Couple-level density of partner effects regressed on well-being (multilevel, couple as unit; B, SE, p):

- Life satisfaction: B = 4.91, SE = 2.07, p = .02, 95% CI 0.8 to 9.06.
- Empathic concern: B = -4.12, SE = 1.48, p < .01 (more interdependent, **less** empathic concern).
- Relationship satisfaction: B = -1.79, SE = 1.47, p = .23.
- Depression (CES-D): B = -1.22, SE = 0.83, p = .15.
No gender interactions. Cross-sectional, same-time, not predictive. The authors found relational well-being "not (relationship satisfaction) or even negatively (empathic concern)" related to interdependence, against their own hypothesis. Sender effects (driving the partner), not receiver effects, carried the associations.

---

## 6. Reconciling the three scales

| Study | Scale of data | Lag | Coupling form | Set point / inertia in model | Result on partner coupling | Tag |
|---|---|---|---|---|---|---|
| Madhyastha 2011 | 6 s, 15-min conflict talk | 6 s | influence functions via TAR, BIC | yes | slightly above chance; no single form | [abs] |
| de Haan-Rietdijk 2016 | same, 129 couples | 6 s | linear β | yes (φ1, φ2, τ) | mean β 0.007 and 0.018, CrIs include 0; 10.1% (husband-to-wife) / 6.2% (wife-to-husband) of couples excluded 0 | [read] |
| Sels 2016 | ~1.2 h, 7 days, 50 couples | one signal | linear VAR, 8 partner slopes | own lag in model | 36% of couples any significant | [read] |
| Steele & Ferrer 2011 | daily (60-90 d is the DDIP design per the 2010 slides; the 2011 abstract gives no length) | 1 day (latent derivative) | partner displacement and velocity | yes ("displacement from average") | coupled for + and - affect; velocity coupling null for negative | [abs] |
| Steele et al. 2014 | daily | 1 day | AICc over "several models" (count unread; the 2010 slides have four) | yes | "independence" most likely; averaged coregulation varies with attachment | [abs] |
| Ferrer & Steele 2010 slides | daily, N = 300 dyads | 1 day | Felmlee-Greenberg first-order | yes (x*, y*) | independence largest type (77/140), coupled types 63/140 | [read] |

The 2011 and 2014 Steele abstracts disagree in headline at face value ("coupled" vs "independence"); the likely reasons (model family; selection by AICc penalising extra parameters; sample; coupling in the average vs coupling in the best-fit type) are all things I cannot check without the texts. **Neither abstract is wrong on its own terms, but the question "how many couples, how large" is unanswered by both.**

---

## 7. Group size and composition

- **n = 2 only.** All studies are dyads; nothing here bears on larger groups, and the sources say nothing about how coupling would change with group size. Dyads allow one partner term in each direction; for n members the coupling matrix has n(n-1) off-diagonal entries (Sels fits 8 partner slopes for a dyad of two variables each; this grows fast with n) [derived].
- **Composition.** All couples are heterosexual (Sels's inclusion criterion explicitly; the Gottman sample is husband-wife). Sels: relationship length 2 months to 35 years and cohabitation status varied; no test of those as moderators is reported in the part I read (the authors list age and duration as things they assessed against density; the results text I read does not give the outcome, so I make no claim). Gottman newlyweds: first marriage, within 6 months of wedding (from `088`). Steele programme: dating couples at UC Davis (the project is named "Dynamics of Dyadic Interactions Project" and the contact is dating@ucdavis.edu on the slide); whether this is the whole 2011 and 2014 sample is unread.
- **Definition effects.** What counts as coupling depends on the timescale and on what is held fixed (inertia, set point, own velocity). Sels et al. cite moderators from other work (culture: Schoebi et al. 2010; arranged vs love marriage: Randall et al. 2011; distress, attachment; a serotonin-transporter variant: Schoebi et al. 2012). These are [sa]: cited in the Sels introduction, not read at source.
- **Set-point sharing across spouses** (r = .60 for threshold) is a composition effect: partners are not independent draws from the population; they resemble each other in set point. Whether by selection into the couple, convergence over time, or shared context is not identifiable from these data.

## 8. Scale of every empirical result, and consent or manipulation

- **Scale:** the **membership/dyad** level (the couple as a unit) throughout. Time scales: seconds (conflict talk), hours (ESM), days (diary). No group of three or more, no crowd. No result here is about adoption or mobilisation.
- **Outcome tied to coupling:** none predictive. Madhyastha: none reported in the abstract. Sels: concurrent correlation with well-being. Steele 2014: abstract says parameters predicted "distal outcomes" such as relationship satisfaction and status, with "modest influences" from ideal affect (the set point), not from coupling.
- **Intervention:** none. All observational. No result involves consent or manipulation. A "partner coupling" parameter at a near-zero value gives nothing to steer through the partner's moment-to-moment state.

---

## Does it reduce to a drive basis?

The honest answer from what I read is: **the fitted content is almost entirely person-level; the one interpersonal operator is the one that is empirically weakest.**

- **What reduces to a person-level quantity.** The set point (threshold τ; "ideal affect" x*; "average" in the oscillator) is a homeostatic target of a person, and the inertia (φ) is the strength with which the person returns to it. These are the terms that carry nearly all the explained variation in the refit (inertia 0.26-0.61 against partner 0.007-0.018) [read]. If a "drive" is a regulated level with a restoring force, then set point and inertia are exactly that, and a drive-as-state-with-return model reproduces the fitted content. Strictly, nothing in these papers *identifies* a drive: they identify a mean and a persistence on a valence composite (SPAFF, PANAS-type affect), so the reduction is to "affective set point and regulation strength" and not to a named drive such as curiosity, fear or desire.
- **Inertia is state-dependent**, which a single drive-level scalar does not give for free: persistence is about twice as strong in the negative state (0.61 / 0.60) as in the positive (0.29 / 0.26) [read]. A drive model needs an asymmetric, threshold-dependent return, not a fixed linear decay. That asymmetry is a property of the person's regulation, consistent with fear-like or threat states being stickier, but this is my gloss and not in the sources.
- **What does NOT reduce.** (1) The **shared set point**: spouses' thresholds correlate r = .60 [read]. A dyad has a joint "where it settles" that is not produced by the lagged cross-partner term (which is ~0). Drives of persons alone, with no coupling, would not predict that correlation unless the two persons' drives were already similar; it is a dyad-level fact, either selection or slow convergence, and the data cannot separate them. (2) The **heterogeneity of coupling form**: Madhyastha "one model of influence does not fit all couples" [abs]; Sels: in the 18 couples with an effect, direction and valence path vary couple by couple [read]. A fixed operator "partner pushes me" has no stable sign or channel here. (3) The **timescale dependence** of any coupling. The same dyads that look uncoupled at 6 s might be coupled at the scale of a conversation or a day (Steele-Ferrer), which a drive-primitive hypothesis has to explain by a mechanism (slow variables) that none of these papers supplies.
- **Verdict on the working hypothesis.** The evidence is consistent with "drives (set points and regulation) of persons carry the within-person dynamics" and **gives no support to a moment-to-moment inter-person drive operator**. It does not refute that group-level drives exist (the shared set point is a candidate), and it does not test drives at all, only affect composites. The hypothesis is not confirmed by this tradition.

## What does it predict or control, and how well?

- **Outcome actually predicted.** The conflict-talk and diary models predict the **next observation** of a spouse's own affect, almost entirely from the spouse's own previous state. The partner term adds almost nothing at 6 s (β ≈ 0.01-0.02 on a scale where own inertia is 0.3-0.6) [read]. Nothing in what I read predicts a *couple outcome* (divorce, split) from the partner coupling parameter. The Madhyastha abstract reports no outcome prediction [abs]. The Steele 2014 abstract reports that parameters (the averaged ones) predict distal outcomes with "modest influences", attributing them to the individual's ideal affect [abs]. In the Sels data coupling density correlates with life satisfaction (B = 4.91, SE 2.07) and with lower empathic concern, not with relationship satisfaction, cross-sectionally [read].
- **Out-of-sample evidence.** None for the coupling parameter. de Haan-Rietdijk et al. fit and report within sample (credible intervals, no hold-out). Sels reports power to detect f² = 0.17 within each couple, no hold-out. Madhyastha uses BIC for selection, not prediction [abs]. Cross-timescale agreement (a coupling parameter at 6 s predicting coupling at one day) is not tested anywhere I read.
- **Effect sizes.** Near zero for the partner term at 6 s (β 0.007 and 0.018; upper CrI ends 0.035 and 0.044) [read]; "medium" f² ≥ 0.17 is what Sels' design could detect and 36% of couples exceeded the significance bar on at least one of eight slopes, close to chance [read; derived]. Between-person effect sizes for inertia reported in the refit (Cohen's d 3.9 and 20) are not interpretable as stated.
- **Failures and limits.** (i) The coupling headline differs between the two Steele abstracts: 2011 coupled vs 2014 independence as modal type [abs]; with different models and selection rules this is a disagreement in headline, not a demonstrated failure to replicate, and the 2014 abstract still reports a varying averaged coregulation parameter. (ii) A strong prior from the clinical literature (the mutual influence process drives outcomes) is contradicted by the authors' own data analysis: "in conflict with most models of couples' interaction" [abs]. (iii) The refit is on the same data as Madhyastha, so it adds analysis agreement, not new data. (iv) Control: nothing here shows an intervention on the coupling term changing a couple outcome; with a near-zero estimate there is no lever.

---

## What exists vs what does not

**Exists:** a read estimate of the linear lag-6-s partner coefficient with intervals (0.007 [-0.020, 0.035], 0.018 [-0.007, 0.044]) from a Bayesian multilevel fit with inertia and set point; an independent-data per-couple count at the hours scale (18 of 50 with any significant partner slope; no consistent pattern); read equations for the first-order dyadic model family the Steele-Ferrer line uses, with counts of best-fit types in a 300-dyad diary sample (slides); abstract-level knowledge of the three target papers.

**Does not exist (in what I could read):** the Madhyastha counts and BIC differences; any Steele & Ferrer estimate, SE, N, or per-couple count; a test of nonlinear influence functions in an independent dataset; a hold-out prediction of any couple outcome from a coupling parameter; any group of more than two; anything separating shared-set-point selection from convergence.

## Unconfirmed

- Madhyastha et al. 2011: every figure beyond the abstract; whether N = 124 and N = 130 are disjoint samples.
- Steele & Ferrer 2011: sample size, coupling estimates, SEs, how the oscillator was parameterised (the equations on the slides lost their Greek letters in extraction, so I do not state them).
- Steele et al. 2014: sample, the set of configurations in the AICc comparison beyond the 2010 slides' four, the weights, and whether the 300-dyad sample is the same.
- Whether the 2014 "independence" and 2011 "coupling" conclusions can both be true of the same dyads.
- The 2010 slide counts: 140 vs 159, and whether 77 is a share of 140 or 300 (already flagged in `061`).
- Moderators reported in the Sels results beyond the part I read (age, duration, cohabitation as predictors of density).
- Literature moderators quoted by Sels (culture, attachment, serotonin-transporter variant): [sa].

## Operand/operator translation (for the algebra)

- Operand: a person with a state s on a valence composite, a set point τ, and a pair of regulation strengths (φ_low, φ_high) with a switch at τ. Dyad adds the partner's state and, as a dyad-level attribute, a shared set point (r = .60).
- Operator (within-person): s(t) = τ + φ(s(t-1) - τ) + ε, with φ chosen by which side of τ the state is on [read: the model above]. A usable primitive.
- Operator (between persons): s_A(t) += β (s_B(t-1) - τ_B). **At 6 s the fitted β ≈ 0.01-0.02 [read]; at hours, sign and channel vary by couple [read]; at days, abstracts disagree [abs].** This operator should enter the algebra as a per-dyad, per-timescale parameter with a prior centred at zero, not as a fixed coupling.
- Pending: nothing [sa] or [abs] in this file is used to fix an equation. The two equations stated are from the refit and the slides, both read.

## Validation log (2026-10-30)

- ✓ Madhyastha, Hamaker & Gottman 2011: DOI 10.1037/a0023028 resolves on Crossref (J Fam Psychol 25(2):292-300, three authors as cited); seed DOI 10.1037/a0023923 confirmed to be Loaiza et al., so the seed correction stands. Abstract re-fetched from PubMed (PMID 21480708) and the quotation is verbatim. Unpaywall: no OA copy; a web search found no author copy. Stays [abs].
- ✎ Steele & Ferrer 2011: DOI, authors, MBR 46(6):956-984 confirmed; abstract verbatim (PMID 26736119). Fixed the garbled velocity-coupling gloss in 3.1 (female sensitive to male's rate of change, male not); flagged that "60-90 d" in the section 6 table comes from the 2010 slides, not the 2011 abstract. Unpaywall: closed. Stays [abs].
- ✎ Steele, Ferrer & Nesselroade 2014: DOI, authors, Psychometrika 79(4):675-700 confirmed; Crossref abstract matches. Added what the file left out: the abstract reports a model-averaged coregulation parameter related to attachment anxiety/avoidance and relationship time, which tempers "independence" as the whole story; table no longer says "4 configurations" (the abstract says "several models"). Stays [abs].
- ✎ de Haan-Rietdijk, Gottman, Bergeman & Hamaker 2016: DOI and authors confirmed; full text read from Europe PMC (PMC4764683). Model equation, Table 4 (every value), spouse correlations, d = 3.9/20, T = 150, 129 couples, OpenBUGS, the Madhyastha "fixed trait" sentence and the influence quotation all check verbatim. Corrected: the paper assigns 89.9% (so 10.1% excluding zero) to **husband-to-wife** influence, i.e. β_W, and 93.8% (6.2%) to wife-to-husband, β_H; summary item 1 had attached 10.1% to the husband's coefficient. Section 4.4 already had it right. Derived SEs (0.014, 0.013) and the 6-90x ratio recomputed and correct.
- ✓ Sels, Ceulemans, Bulteel & Kuppens 2016: DOI and authors confirmed; full text read (PMC4786571). 50 couples, demographics, 92.03% compliance, 1 h 12 min 12 s spacing, 10 AM-10 PM, 48.34 time points, f² = 0.17, 18/50 (36%), 20/50 (40%), 18/49 (37%), the 50/39/11, 50/28/22 and 11/39/50 splits, Fisher p = .10/.50, Table 2 B/SE/p/CI for all four outcomes, sender-effect statement, and the cited moderators (Schoebi 2010, Randall 2011) all match.
- ✓ Ferrer & Steele 2010 slides: PDF fetched and read. All four model equations, the SAS restrictions a1,a2,b1,b2 > 0, .70 ideal on proportional affect, FIML, N dyads = 300, 140/159, k-means step, counts 6/77/11/42/4 (sum 140), DDIP 60-90 days, dating@ucdavis.edu and the conclusions quotation match.
- ✓ Hamaker, Ceulemans, Grasman & Tuerlinckx 2015: DOI, authors, Emotion Review 7(4):316-322 confirmed; content not re-read (nothing load-bearing rests on it).
- ✎ Felmlee & Greenberg 1999: existence confirmed, full reference and DOI 10.1080/0022250X.1999.9990218 added; not read, stays [sa].
- ✎ Gottman, Swanson & Murray 1999: existence confirmed, full reference and DOI 10.1037/0893-3200.13.1.3 added; not read.
- Also softened "fails to replicate" under Failures (i) to a headline disagreement between two abstracts with different models.

Sources opened: 4 primary texts (de Haan-Rietdijk 2016 full text, Sels 2016 full text, Ferrer & Steele 2010 slides, PubMed and Crossref abstracts of the three target papers counted as one batch of abstracts), plus Crossref records for 9 DOIs and Unpaywall for 3.

Verdict: the file is accurate and unusually honest about what it could not read; every number it tags [read] checks against the primary text, and no fabrication was found. One real error, a swapped direction label on the 10.1% / 6.2% per-couple exclusion rates in the summary, is fixed; the Steele 2014 abstract was under-reported (it estimates a coregulation parameter that varies with attachment), which now tempers the "independence" headline. The two equations offered to the algebra (the refit's threshold-VAR and the Felmlee-Greenberg form from the slides) were both read at source and may stand.

## Cross-checks (2026-10-30)

Checked by grep against the other files in this directory on the works, authors, equations and numbers above (Madhyastha, Steele, Ferrer, Sels, de Haan-Rietdijk, Hamaker, Felmlee, sample sizes and scales), with the read figures in 059, 080 and 088. No other file was edited. Ledger lines for this file were returned to the orchestrator; provenance is kept as tagged here (`read` or `sa`), and [abs] items are recorded as `sa` because the provenance field has no abs value.

**Agreements**

- Madhyastha, Hamaker & Gottman 2011 (DOI 10.1037/a0023028; N = 124 couples and 130 newlyweds; TAR estimation; BIC): 088 (section 6 table), 080 section 1, 079 and 059 all agree. Abstract only in all of them.
- Madhyastha headline ("only slightly greater than ... random association"; "one model ... does not fit all couples"; initial state and inertia over the partner's affect): 088 section 6 and 098 section 2.1 agree.
- Steele & Ferrer 2011 (MBR 46(6):956-984, doi 10.1080/00273171.2011.625305, PMID 26736119): no within-person damping; partner rate-of-change coupling null for negative affect. 061 and 070 agree with 098 section 3.1. Abstract only in all three.
- Steele, Ferrer & Nesselroade 2014 (Psychometrika 79(4):675-700, doi 10.1007/s11336-013-9366-9): identity and citation agree across 061, 070 and 088. The "independence" headline is the same quoted sentence in 088 section 6 and 098 section 3.2.
- Ferrer & Steele 2010 slides: counts 6 / 77 / 11 / 42 / 4 (sum 140 of 300 dyads), 60-90 daily reports, and the 140-versus-159 ambiguity. 061 and 098 agree, and both leave the ambiguity open.
- Felmlee & Greenberg 1999 (J. Math. Sociology 23(3):155-180, doi 10.1080/0022250X.1999.9990218): 070 section 3 agrees.
- Gottman, Swanson & Murray 1999 sample (130 recruited newlyweds, 125 estimable, 17 divorces, 150 six-second blocks per spouse, first marriages married within 6 months): 059, 080 and 088 agree with one another. 098 cites these only "from 088" and agrees.
- Hamaker, Zhang & van der Maas 2009 (TAR special case; three dyads): 080, 059, 088 and 079 agree. 098 does not cite it.
- de Haan-Rietdijk et al. 2016 as a threshold-model refit of this data: 079 agrees (Crossref). 088's "no independent replication of the threshold parameters" concerns the divorce-prediction parameters and is not contradicted by 098, which refits the newlywed data without testing the husband-threshold direction.
- Direction of the evidence (partner effect small or absent at the scale of seconds, mixed at hours and days): 088 summary item 4 reaches the same direction from the abstracts alone. 098 supplies the read numbers.
- Sels et al. 2016: no other file in the directory cites it. 070 section 8 lists "Sels, Kuppens ... interpersonal emotion dynamics" as unsearched; 098 now supplies that read source, so 070's list can be closed by pointing here.

**Contradictions** (both claims recorded; none resolved here)

1. Size of the Gottman newlywed sample. 098 section 4.1 (read, de Haan-Rietdijk 2016): 129 newlywed couples. 059 section 1 and 080 section 1 (read-059): 130 newlyweds, 125 with estimable models, 17 divorces. 088 section 1 (read): 130 newlywed couples. **Unresolved.** 129 may be an exclusion after screening; neither source says so.
2. Whether Madhyastha's 124 couples are the 130 newlyweds. 098 section 2.2 leaves this open. 088 summary item 4 records it as "settled", but that settles 124 versus 125 as numbers from two papers, not whether the 124 couples are a subset of the newlyweds. 059 contradiction 3 says "probably a different, non-newlywed sample" without having opened the Madhyastha text. **Unresolved.**
3. Distal outcomes in the Steele et al. 2014 abstract. 098 section 3.2 quotes the abstract verbatim: "modest influences from the individual's level of ideal affect", with the averaged coregulation parameter tied separately to attachment. 088 section 6 (abstract): "averaged parameters had 'modest' relations to satisfaction and status". Both read the same abstract. **Unresolved.** Neither has the full text.
4. Scale of the affect variable. 080 section 1 and 059 (read): the Gottman-Swanson-Murray SPAFF weighted score, range -24 to +24 per six-second block. 098 section 4.1 (read, de Haan-Rietdijk 2016): a SPAFF composite averaged over six-second intervals and coders, with neutral at 0.1. These may be the same behavioural record under two scorings, or different variables. **Unresolved.** Until settled, the refit's partner coefficient (0.007, 0.018) cannot be placed on the 1999 scale.

**Noted, not a contradiction.** 088 section 6 (Hamaker et al. 2009, read) found that a step (regime) influence form beat a partner-slope form, with the partner's score not helping within regimes, on three dyads at a two-second scale. 098's de Haan-Rietdijk refit uses a linear partner term on 129 couples at six seconds. Different data, scale and form, and the same direction on the partner term. Neither file tests the other's model.
