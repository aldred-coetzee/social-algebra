# Prior work 093: reflexivity as a modelling problem (Merton, Hawthorne, Campbell, Goodhart, Lucas, MacKenzie, Soros, performative prediction)

Direction: D583

Date: 2026-10-29. Survey for the social-algebra strand. Context: Aldred's aim is an algebra of drives, of persons and groups, from which theorems and prediction or control follow. This file asks the prior question: once a model of a group is known to the group, or acted on, does it stay true? If not, the algebra needs the model-knowing step as an operator, not only drives as operands.

## Method and honesty note

Tags: **[read]** = I fetched the primary text myself and read the passages cited (coverage given per work). **[sa]** = second-hand: a search summary, a later author's account, or my memory. **[inference]** = my own reasoning from read text, not a claim from a source. Nothing tagged [sa] is used in any equation below.

Read at source this session (all open copies; nothing is read cover to cover unless stated):

| Work | Copy read | Coverage |
|---|---|---|
| Merton 1948 | JSTOR scan hosted at pbworks (OCR; word spacing broken, quotes below are re-spaced) | pp. 193-199 closely, rest skimmed |
| Levitt & List 2011 | NBER WP 15016 (2009 version), not the AEJ print | abstract, intro, data, regression section, epilogue |
| Campbell | JMDE 2011 reprint of the **1976 Dartmouth occasional paper**, not the 1979 journal text | opening and the whole "Corrupting Effect of Quantitative Indicators" section |
| Perdomo et al. | arXiv 2002.06673v4 (the ICML 2020 paper's long version) | Sections 1-6, no appendices |
| Manheim & Garrabrant 2019 | arXiv 1803.04585v4 | Regressional, extremal, causal, and adversarial sections |
| Soros 2013 | Soros's own site, full text, HTML | sections on reflexivity, human uncertainty principle, markets, boom-bust |
| MacKenzie 2003 | Edinburgh open copy of the *Social Studies of Science* article | performativity passages and conclusion |
| Hardt & Mendler-Dünner 2025 | arXiv 2310.16608v2, survey | Sections 1-3, 7 |
| Rudebusch 2005 | author's PDF | abstract and introduction only |
| McCambridge et al. 2014 | Europe PMC full text | abstract, results, meta-analytic odds ratios, mechanism paragraph |

**Not retrievable, so [sa] only:** Lucas 1976 (the only open copies found were behind a WAF or a maintenance page; I did not try to get round that); Goodhart 1975 (original is a conference paper; only the 1984 reprint is catalogued); MacKenzie 2006 *An Engine, Not a Camera* (book, not open); Grunberg & Modigliani 1954 and Simon 1954 (known here only through Hardt & Mendler-Dünner's account of them); Morgenstern 1928 (same).

DOIs confirmed at Crossref this session: Levitt & List 10.1257/app.3.1.224; Lucas 10.1016/S0167-2231(76)80003-6; Campbell 1979 10.1016/0149-7189(79)90048-X and the reprint 10.56645/jmde.v7i15.297; MacKenzie 2003 10.1177/0306312703336002; McCambridge et al. 10.1016/j.jclinepi.2013.08.015 (J. Clin. Epidemiol. 67(3):267-277); Goodhart reprint 10.1007/978-1-349-17295-5_4 (pp. 91-121). **Corrected 2026-10-30:** Rudebusch 2005 is JMCB 37(2):**245-272**, DOI 10.1353/mcb.2005.0024 (Crossref-confirmed); the working-paper DOI 10.24148/wp2002-02 also resolves. Soros 2013 **does** have a resolving DOI, 10.1080/1350178X.2013.859415 (Crossref: Soros, J. Economic Methodology 20(4):309-329); the earlier note that the DOI pointed at Notturno's commentary was a wrong DOI tried, not a missing one. Grunberg & Modigliani 1954: 10.1086/257604, JPE 62(6):465-478 (Crossref-confirmed). Simon 1954: 10.1086/266513, POQ 18(3):245-253 (Crossref-confirmed). Merton: Antioch Review 8(2), Summer 1948, 193-210, JSTOR 4609267 (Crossref 10.2307/4609267). Perdomo et al.: ICML 2020, PMLR 119:7599-7609 (proceedings page checked); I read the arXiv version. Hardt & Mendler-Dünner's survey is published: *Statistical Science* 40(3):417-436 (2025), DOI 10.1214/25-sts986 (Crossref-confirmed).

## Summary

Seven separate phenomena travel under "the model changes what it models". They are not one thing, and an algebra needs to know which it is carrying:

1. **A belief changes the facts it is about** (Merton; Soros). Mechanism: belief -> action -> outcome. Scale: crowd and membership.
2. **Being measured or watched changes behaviour** (Hawthorne). Mechanism: awareness of observer -> conformity or effort. The best evidence is much weaker than the legend.
3. **A metric used for control stops measuring** (Campbell, Goodhart). Mechanism: agents optimise the indicator, not the thing. Manheim & Garrabrant split this into four sub-mechanisms, only some of which need an adversary.
4. **A statistical relation estimated under one policy breaks under another** (Lucas). Mechanism: behavioural rules depend on the policy. [sa for text; Rudebusch read for the size of the effect.]
5. **A model, once used, makes its own assumptions true** (MacKenzie, Black-Scholes). Mechanism: practitioners use it, so prices converge to it. Partial and reversible.
6. **A formal condition for when a published prediction can still be correct** (Grunberg-Modigliani-Simon fixed point [sa], Perdomo et al. stability [read]).
7. **A formal measure of how much a predictor can steer** (performative power, Hardt, Jagadeesan & Mendler-Dünner 2022 [read, via the survey]), with one real-data lower bound (Mendler-Dünner, Carovano & Hardt 2024, browser-extension randomized experiment on search clicks [read, via the survey and the arXiv abstract]).

Only (6) and (7) are mathematics that lets a model stay valid once known. (1)-(5) are mechanisms plus case evidence. The formal answer, such as it is: a model survives being known if the response of the population to the model is continuous (existence of a self-confirming prediction) and, for convergence by retraining, if that response is **small relative to the curvature of the loss** (epsilon < gamma/beta). Neither condition is checked on human data anywhere I found. (The nearest thing to a measurement on people is a lower bound on performative power of online search, section 6c; that is a size of steering, not an estimate of epsilon or of a contraction constant.)

---

## 1. Merton, "The Self-Fulfilling Prophecy" (1948)

**Citation.** Merton, R. K. (1948). The Self-Fulfilling Prophecy. *The Antioch Review* 8(2): 193-210. JSTOR 4609267. Reprinted in *Social Theory and Social Structure* (1949, [sa]).

**Their vocabulary.** Thomas theorem; definition of the situation; self-fulfilling prophecy; "suicidal prophecy" (the counterpart); in-group and out-group; vicious circle; "reign of error".

**Drives/operands.** None. Operands are *beliefs held about a situation* (a definition) and the *behaviour* it elicits. No drive appears; fear appears only as the anxious student's and depositors' reaction.

**Operators / equations.** No equations. Statements, quoted [read]:
- "If men define situations as real, they are real in their consequences" (W. I. Thomas, quoted at the opening).
- "The self-fulfilling prophecy is, in the beginning, a *false* definition of the situation evoking a new behavior which makes the originally false conception come true."
- "public definitions of a situation (prophecies or predictions) become an integral part of the situation and thus affect subsequent developments. This is peculiar to human affairs. It is not found in the world of nature. Predictions of the return of Halley's comet do not influence its orbit."
- The bank parable: "a rumor of insolvency, once believed by enough depositors, would result in the insolvency of the bank". Note "enough": the parable has a **threshold in the number of believers**, though Merton states no number.
- Footnote 1: the counterpart is the "suicidal prophecy", which "so alters human behavior ... that it fails to be borne out". Not developed.
- Breaking the circle: "The initial definition of the situation which has set the circle in motion must be abandoned." Merton then argues that this is not achieved by education campaigns or good will, which "cannot be turned on and off like a faucet"; he points to institutional change (his example: admission of Black workers to unions removing the scab role). I read the education argument closely and the institutional-change argument only in passing.

**Theorems or derived predictions.** None. The one structural claim: the prophet "will cite the actual course of events as proof that he was right from the very beginning". That is, **the falsification test is defeated by the loop**: a self-fulfilling model cannot be refuted by the outcome it produced.

**Scale of the examples [read].** Crowd/adoption (the bank run: depositors in the hundreds; "enough" is unspecified). Membership (exclusion from unions, schooling, with ethnic in-groups and out-groups). Group/decision (two nations arming because each believes war inevitable). Individual (the examination-neurotic student). Merton does not vary group size in any controlled way.

**Consent vs manipulation.** The loop runs through *uninformed* participants: depositors act on a rumour, not on a model they chose to adopt. The remedy Merton proposes works on structure (rules, institutions), not persuasion, and he argues explicitly against persuasion by information.

**Empirical standing.** Illustrative cases only, no data in this text. Flag: "Last National Bank" is the name in the text I read; it is a fictional parable. The result is a conceptual claim that has since been given formal content (section 6), not an empirical finding.

**Operand/operator translation [inference].** A belief B about a state s is an operand; a *public* B is an operator on s: s' = R(B). Merton's two kinds are the sign of dR/dB (positive: self-fulfilling; negative: suicidal). His threshold remark says R is steep or discontinuous in the share of believers, which matters for section 6 (continuity is exactly what the fixed-point result needs).

---

## 2. Levitt & List, "Was there really a Hawthorne effect at the Hawthorne plant?" (2011)

**Citation.** Levitt, S. D. & List, J. A. (2011). *American Economic Journal: Applied Economics* 3(1): 224-238. DOI 10.1257/app.3.1.224 (Crossref-confirmed). Read: NBER WP 15016 (May 2009). Numbers below may differ in the print version.

**Their vocabulary.** Hawthorne effect; illumination experiments; relay assembly; "a guaranteed methodological heuristic" (they deny that it is one).

**Drives/operands.** Worker output (units completed), light (natural and artificial, foot-candles), an experimenter-change indicator. Mechanism proposed in the folk account, "attention to employees, not work conditions per se" (their quote of the standard reading), is a social-attention drive; they do not model it.

**Operators / equations [read].** Their only equation:

    Output_rt = d1 E_rt + d2 E_rt-1 + b1 t + b2 t^2 + lambda_r + X_rt Phi + eps_rt        (1)

r = room, t = day; E = indicator for an experimentally driven change in artificial light that day; lambda_r room fixed effects; X weather, day-of-week and month indicators, holidays, defective inputs, output-check frequency, whether workers were in their original room; some specifications add room x month x year interactions.

**Findings [read].**
- Day-of-change effect: "statistically insignificant immediate responses"; point estimate negative on the day of change and positive the next, combined "negative, but close to zero". The raw plot appeared to show a slight rise; it disappears with controls.
- "Existing descriptions of supposedly remarkable data patterns prove to be entirely fictional" (abstract): the legend that every change, even dimming, raised output is not in the data.
- Weaker evidence of a subtler effect: output 3-4 percent higher while experimentation was ongoing than pre-experiment baseline (Panel B col. 1), but "the result disappears" with room x month x year interactions; they say it is an open question whether it is a longer-term effect or unobserved confounding.
- Artificial light (the experimenter's lever) raises output more than natural light; the magnitude is under one percent per standard deviation of artificial light. They call this "directionally consistent" and "circumstantial".
- Total light: each foot-candle ~0.0865 units of output; one SD of light 1-2 percent; trivial and insignificant once month-by-year interactions are added.

**Scale and group size.** Group (work-room), outcome is productivity. Workers were women assembling relays and winding coils, in three departments (rooms). I did not find the head-count per room in the text I read, so I cannot say how effect scales with n. Experimenter-level manipulation, workers aware of experimenters (consent not discussed).

**Empirical standing.** The illumination data were recovered and analysed 80 years later; the finding is a negative result for the strong form of the effect. The later Hawthorne relay-room experiments (1927-32) are not reanalysed here.

**Meta-analytic standing [read, McCambridge, Witton & Elbourne 2014].** Systematic review, 19 purpose-designed studies (8 RCTs, 5 quasi-experimental, 6 observational) on being observed or reporting on one's behaviour. Conclusion: "Consequences of research participation for behaviors being investigated do exist, although little can be securely known about the conditions under which they operate, their mechanisms of effects, or their magnitudes." Pooled odds ratios as printed: five trials 1.06 (0.98-1.14); five quasi-experimental 1.07 (0.99-1.17); eight "being observed" studies 1.21 (1.03-1.41); overall unweighted 1.17 (1.06-1.30). The text also prints "1.29; 95% CI 1.06, 1.30" for four observational studies, which looks like a typo in the source. Heterogeneity is high; all but one study are in health sciences (patients and clinicians, not groups); 12 of the 19 gave some statistically significant evidence of an effect. Mechanism: the review *reports*, as "a widespread social psychological explanation" (not as its own finding, and not tested by it), that "Awareness of being observed or having behavior assessed engenders beliefs about researcher expectations. Conformity and social desirability considerations then lead behavior to change in line with these expectations." [✎ 2026-10-30: was presented as the review's own mechanism.] The review also notes the term is mostly used as a post hoc excuse for disappointing results.

**Consent vs manipulation.** [✎ 2026-10-30: overstated before.] The trials mostly test answering questionnaires about one's behaviour; the observational studies compare observed periods with covert or pre-arrival periods. The larger pooled estimates (1.21 for "being observed", 1.29 for observational studies) come from those observational designs, which are also the weakest, so "announced observation gives larger effects" is confounded with design and is not a contrast the review isolates. The effect, where present, is by definition *created by the participant's knowledge* of being studied, so it cannot be measured with that knowledge withheld from the treated arm.

**Operand/operator translation [inference].** An *observation operator* O acting on a person or group adds a small, context-dependent push toward the believed expectation of the observer; its size is not stable enough (OR 1.06 to 1.29 across designs) to be a constant of the algebra. Better as a nuisance term with a wide prior.

---

## 3. Campbell's law (1976/1979)

**Citation.** Campbell, D. T. (1979). Assessing the impact of planned social change. *Evaluation and Program Planning* 2(1): 67-90. DOI 10.1016/0149-7189(79)90048-X. First issued as Occasional Paper #8, Dartmouth Public Affairs Center, December 1976. Read: the 2011 JMDE reprint of the 1976 paper (DOI 10.56645/jmde.v7i15.297). Wording may differ from the 1979 print.

**Their vocabulary.** Planned social change; quantitative social indicators; corruption pressures; "pessimistic laws".

**Drives/operands.** Indicators (clearance rate, test score, body count, production quotas) and the *social processes* they monitor. Agents' drives are implicit: self-preservation and reward (jobs, money, power), stated as "pressure".

**Operators / equations.** None. The law, quoted [read]: "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor." Campbell calls these "two laws"; the text I read does not number them. He introduces them with: "evidence which I take seriously, although it is predominantly anecdotal."

**Examples [read], with scale.**
- Chicago votes versus census: votes (used for jobs and power, guarded) judged more trustworthy than census data (then unused for decisions). Population/institution scale.
- Police clearance rates: under-recording and plea-bargain trades (burglar confessing to unsolved crimes for a lighter sentence). Organisation scale; Nixon-era crime crackdown "had as its main effect the corruption of crime-rate indicators".
- Employment office: counting cases handled gave "quick, ineffective interviews"; counting placements gave "creaming".
- Texarkana performance contracting: contractors "teaching the answers to specific test items", paid on score gains.
- Soviet industrial quotas: weight -> heaviest item; count -> smallest item; value -> single product.
- Vietnam "body count": a verifiable proxy became the goal, "a corruption of the social processes it was designed to reflect".
- Remedies he states: outside evaluators or watchdogs (the Seattle Teachers' Union), and studying indicator systems "relatively immune to distortion" (census, cost-of-living index). On multiple indicators he says commentators "including myself (1969b), assume that the use of multiple indicators, all recognized as imperfect, will alleviate the problem, although Ridgeway (1956) doubts this." [✎ 2026-10-30: the doubt is Ridgeway's; Campbell himself leans toward multiple indicators helping.]

**Empirical standing.** Anecdotal by his own account. Later work (Manheim & Garrabrant below) formalises the mechanism but does not test it on human data. Campbell does not give effect sizes, rates, or dose-response.

**Consent vs manipulation.** The pressure works through the *measured people's own incentives*; no consent issue arises, but the intervention (publish and reward the metric) is itself the cause of the failure.

**Operand/operator translation [inference].** Campbell's law is a statement that any *controller* that reads an indicator and rewards it adds a drive in the measured agents (to move the indicator), which is a new term in their utility function. It cannot be captured by a model with fixed drive coefficients.

---

## 4. Goodhart's law and its formalisation

**Citation (law).** Goodhart, C. A. E. (1975), "Problems of monetary management: the UK experience", in *Papers in Monetary Economics*, Reserve Bank of Australia; reprinted 1984 in *Monetary Theory and Practice*, Macmillan, DOI 10.1007/978-1-349-17295-5_4 (Crossref-confirmed). **Not read.** The wording, as Manheim & Garrabrant quote it (footnote 1, which I read): "any observed statistical regularity will tend to collapse once pressure is placed upon it for control purposes." [sa for Goodhart's own text; read for the quotation as given by M&G.]

**Citation (formalisation).** Manheim, D. & Garrabrant, S. (2019). Categorizing Variants of Goodhart's Law. arXiv:1803.04585v4 (first posted 13 Mar 2018; arXiv metadata checked). [read, nearly in full]

**Credit.** [✎ 2026-10-30] The four categories are not first introduced in this paper. M&G say so: "The four categories of Goodhart effects introduced by Garrabrant", citing Garrabrant, S., "Goodhart Taxonomy", LessWrong (then lesserwrong.com), 30 Dec 2017 [sa: the blog post was not opened]. M&G's contribution is the toy models and the sub-cases (causal sub-cases, cobra effects). M&G also note that Campbell's law "arguably has scholarly precedence" over Goodhart's, citing Rodamar (2018), *Significance* 15, "There ought to be a law! Campbell v. Goodhart" [sa].

**Vocabulary.** Regulator, goal G(s), proxy M(s), threshold selection (s admissible if M(s) >= c); four classes: Regressional, Extremal, Causal, Adversarial.

**Equations [read].**
- Regressional: M = G + normal(mu, sigma^2) (1). "Due to the noise, a point with a large M value will likely have a large G value, but also a large noise value." They say it "cannot be avoided" for an inexact metric.
- Extremal, model insufficiency: M = G(s_i) + G'(s_i) (2). Extremal, regime change: G = M + x if M <= a; G = M + y if M > a (3).
- Causal Goodhart has three sub-cases, by where the regulator intervenes: a shared cause X of metric and goal, an intermediary, or the metric directly. If the regulator "sets M to a specific value", "the relationship between Metric and Goal now no longer holds."
- Ignored shared cause: Metric ~ normal(X, s_m^2), Goal ~ normal(X, s_g^2) (4); ignored additional cause (5), (6).
- Adversarial: "Campbell's Law - Agents select a metric knowing the choice of regulator metric." With M_R = G_R + X and M_A = G_A * X (7), "if X ~ normal(mu, sigma^2), the correlation between G_A and M_A is zero over the full set of states, but becomes positive on the subspace selected by the regulator."
- "Cobra effects" (regulator rewards, agent games the reward) are split into normal and non-causal.

**Theorems or derived predictions.** None proved. The paper is a taxonomy with toy models, no theorems and no data. Its useful content for us: the first three classes **need no adversary and no reflexivity in the human sense**: a regulator's own selection pressure or intervention suffices. Only the fourth class is reflexive. That is, much of what is called "Goodhart" on human systems is ordinary regression to the mean and extrapolation error, and only the Campbell-type residue is a genuine loop.

**Empirical standing.** No datasets. The authors say a "separate forthcoming paper" would relate this to Campbell and Lucas formally, and say the categories "do not match what was originally discussed"; I have not found that paper.

**Scale.** Single regulator, single-dimensional metric; they say multi-metric cases "follow similar dynamics". Group size enters only as "amount of power directed towards optimizing the proxy".

**Operand/operator translation [inference].** The four classes correspond to different algebraic defects: (a) noise in the measurement morphism, (b) domain of validity of a law, (c) a change of structure by the act of control, (d) an agent with its own objective composing with the controller's. Only (c) and (d) are "reflexive".

---

## 5. Lucas critique

**Citation.** Lucas, R. E. (1976). Econometric policy evaluation: a critique. *Carnegie-Rochester Conference Series on Public Policy* 1: 19-46. DOI 10.1016/S0167-2231(76)80003-6 (Crossref-confirmed). **Paywalled / not retrievable. Everything about its text is [sa].**

**What is [sa].** Search summaries and Rudebusch's opening paragraph agree on the content: "the parameters of traditional macroeconometric models depend implicitly on agents' expectations of the policy process and are unlikely to remain stable as policymakers change their behavior" (Rudebusch 2005, p. 245, [read], as a restatement; the 2002 FRBSF working paper, which I opened on 2026-10-30, opens "Lucas (1976) argued that the parameters of traditional macroeconometric models depended implicitly ...", so the wording differs slightly between versions). The page-41 sentence about optimal decision rules is quoted by several search results; I did not see it in any text I read, so I do not reproduce it. The notation y_t+1 = F(y_t, x_t, theta, eps_t), theta = G(lambda) that is usually attached to the paper comes from memory and is **[sa]; do not use**.

**What I read that bears on it.** Rudebusch (2005), abstract and introduction only: US monetary policy rules show estimated discrete shifts over the past decades, yet lagged VAR reduced forms often fail to reject stability, which "appear to contradict the Lucas critique". He reconciles them via a simulation: the parameter shifts the critique predicts are small relative to the size of the historical policy shifts and the "relative insensitivity of the reduced forms of plausible forward-looking macroeconomic specifications to policy shifts". So the critique is logically right but **quantitatively small in that setting**; whether it is large elsewhere is an empirical question. [2026-10-30, read in the 2002 working paper, not the JMCB print:] the conclusion says "At a theoretical level, the Lucas critique is uncontested", that "There is little evidence that the Lucas critique is an important factor in this setting given typical macroeconomic sample sizes", and that "there are parameter configurations and rule shifts that would give the Lucas critique more importance", including shifts "outside the historical experience". So "small" is his, conditional on historical shift sizes and sample sizes.

**Scale.** Aggregate macroeconomy, policy as the intervention. Group size does not enter.

**Consent vs manipulation.** The policy-maker changes the rule; agents adapt rationally (assumed). No consent dimension.

**Operand/operator translation [inference from Rudebusch only].** Lucas's claim in our terms: parameters that depend on a policy are not primitives. The remedy it prescribes is to model the *deep* part that stays fixed (in economics: tastes and technology) and derive the rest. This is an argument **for** a drive-level algebra *if* drives are deep in that sense, and it is the one place in this file where the "drives as primitives" hypothesis gets structural support: reduced-form behaviour is unstable, drive parameters are claimed stable. It is not tested for human drives anywhere I read.

---

## 6. Performative prediction and the fixed-point results

### 6a. Grunberg-Modigliani and Simon (1954): existence of a self-confirming prediction [sa via Hardt & Mendler-Dünner]

**Citations (not read).** Grunberg, E. & Modigliani, F. (1954), The predictability of social events, *J. Political Economy* 62(6): 465-478, DOI 10.1086/257604 (Crossref-confirmed 2026-10-30); Simon, H. A. (1954), Bandwagon and underdog effects and the possibility of election predictions, *Public Opinion Quarterly* 18(3): 245-253, DOI 10.1086/266513 (Crossref-confirmed). Both paywalled; content [sa]. I know them only from Hardt & Mendler-Dünner (2025), which I read.

**The result as that survey states it [read, secondhand about the 1954 papers].** Distinguish private predictions (no causal power) from public ones. Let y in [0,1] be the outcome, y-hat the prediction, and R the response function

    y = R(y-hat)        (1)

A public prediction can still come true iff there is y-hat with y-hat = R(y-hat). "Continuity of R" is the sufficient condition; the proof is Brouwer's fixed point theorem, in one dimension the intermediate value theorem. The survey says Grunberg, Modigliani and Simon thereby answered Morgenstern's (1928) claim that economic forecasts published with authority are necessarily invalidated by their own effects.

### 6b. Perdomo, Zrnic, Mendler-Dünner & Hardt, "Performative Prediction" (ICML 2020)

**Citation.** arXiv:2002.06673 (v4, 26 Feb 2021); *Proc. 37th ICML*, PMLR 119 [sa on the proceedings page]. [read, main text, no appendices]

**Their vocabulary.** Performative; distribution map D(theta); performative risk; performative optimality; performative stability; repeated risk minimisation (RRM, "retraining"); epsilon-sensitivity.

**Operands.** Instances z = (x, y), model parameters theta in a closed convex Theta in R^d, a loss l(z; theta). No drives. The "population" is a distribution.

**Operators / equations [read, verbatim in substance].**
- Distribution map: theta -> D(theta). "Performative risk": PR(theta) = E_{Z~D(theta)} l(Z; theta).
- Performative optimum (Def. 2.1): theta_PO = argmin_theta E_{Z~D(theta)} l(Z; theta).
- Performative stability (Def. 2.3): theta_PS = argmin_theta E_{Z~D(theta_PS)} l(Z; theta). A stable model "minimizes the expected loss on the distribution D(theta_PS) resulting from deploying" it, so retraining returns it unchanged. Stability and optimality are different; "neither implied by nor does it imply" the other.
- Decoupled risk DPR(theta, theta') = E_{Z~D(theta)} l(Z; theta'). Stable: theta_PS = argmin DPR(theta_PS, .). Optimal: theta_PO = argmin DPR(theta, theta).
- epsilon-sensitivity (Def. 3.1): W1(D(theta), D(theta')) <= epsilon ||theta - theta'||_2, W1 the earth-mover (Wasserstein-1) distance.
- Assumptions: A1 beta-joint smoothness; A2 gamma-strong convexity of the loss in theta.
- RRM (Def. 3.3): theta_{t+1} = G(theta_t) = argmin_theta E_{Z~D(theta_t)} l(Z; theta).
- **Theorem 3.5.** If l is beta-jointly smooth and gamma-strongly convex and D is epsilon-sensitive then (a) ||G(theta) - G(theta')||_2 <= epsilon (beta/gamma) ||theta - theta'||_2, and (b) if epsilon < gamma/beta, RRM converges to a unique performatively stable point at a linear rate: ||theta_t - theta_PS||_2 <= delta once t >= (1 - epsilon beta/gamma)^-1 log(||theta_0 - theta_PS||_2 / delta).
- **Proposition 3.6.** The convergence conditions are tight: RRM can fail to converge if the loss is convex but not strongly convex, strongly convex but not smooth, or epsilon >= gamma/beta.
- **Example 3.4.** If D(theta) is a point mass at 0 for theta >= 1/2 and at 1 for theta < 1/2 (discontinuous), no stable point exists, and RRM oscillates 1, 0, 1, 0, ... The performative optimum is theta_PO = 1/2.
- **Example 2.2 (biased coin).** X in {+1,-1}, Y|X ~ Bernoulli(1/2 + mu X + epsilon theta X), f_theta(x) = theta x + 1/2, squared loss. Then theta_PO = mu/(1 - 2 epsilon), theta_PS = mu/(1 - epsilon), supervised theta_SL = mu. So the **self-confirming prediction (stable) and the best prediction (optimal) diverge as the performative strength epsilon grows**.
- Prop. 4.1: a stable point exists for compact Theta, convex jointly continuous loss and epsilon-sensitive D.
- Theorem 3.8 (repeated gradient descent) needs epsilon < gamma/((beta+gamma)(1 + 1.5 eta beta)). Theorem 3.10: finite-sample versions converge to a delta-ball with n_t = O((epsilon delta)^-m log(t/p)) samples at time t (m = dimension of z), under a light-tail moment condition, and for repeated empirical risk minimisation the threshold tightens to epsilon < gamma/(2 beta). [✎ 2026-10-30: was log(1/p) and omitted the halved threshold.]
- **Theorem 4.3.** If the loss is L_z-Lipschitz in z and gamma-strongly convex and D is epsilon-sensitive, then every stable point and every performative optimum satisfy ||theta_PO - theta_PS||_2 <= 2 L_z epsilon / gamma.
- Section 5: strategic classification is a special case. Agents shift features x_S' = x_S - epsilon theta_S under quadratic costs 1/(2 epsilon)||x' - x||^2; this D is epsilon-sensitive.

**Theorems about our question.** This is the one formal treatment of "model stays valid once known" that I read in full text: a stable point is exactly a model that is correct for the population that its own deployment produces. The conditions are: continuity of response (cf. 6a), strongly curved loss, and **a small response of the population to the model relative to the curvature** (epsilon < gamma/beta). Beyond that the loop oscillates or has no stable point.

**Empirical standing, bluntly.** The paper's evidence is a semi-synthetic simulation: a class-balanced subset of a "Kaggle credit scoring dataset" (their reference [22]: Kaggle, "Give Me Some Credit"), a logistic classifier, and a *modelled* response (linear utilities, quadratic costs). The distribution map is assumed, not estimated from behaviour. No human experiment; epsilon is never measured. I read nothing in the main text showing epsilon estimated from real data. The convergence theorems are proved; their applicability to people is untested here.

**Scale.** Population of individuals each responding to a classifier (membership/decision outcomes in lending). Group size enters via the sampling rate n_t and via the Wasserstein sensitivity; there is no group-level interaction among respondents (each individual best-responds independently), so **contagion or conformity between people is outside the model**.

**Consent vs manipulation.** The deployer *steers* by choosing theta; agents respond because it is in their interest. That is manipulation by incentive, with no consent from the people classified.

### 6c. Hardt & Mendler-Dünner, "Performative Prediction: Past and Future" (survey)

**Citation.** Hardt, M. & Mendler-Dünner, C. (2025). Performative Prediction: Past and Future. *Statistical Science* 40(3):417-436, DOI 10.1214/25-sts986. Read as arXiv:2310.16608v2 (20 May 2025). [read: Sections 1-3, 7 and, on 2026-10-30, the opening of Section 8]

**Credit for results reported here.** Performative power and its competition results are Hardt, Jagadeesan & Mendler-Dünner (2022), "Performative Power", NeurIPS 35, DOI 10.52202/068431-1669 (Crossref-confirmed; not opened). The empirical estimate is Mendler-Dünner, Carovano & Hardt (2024), "An engine not a camera: Measuring performative power of online search", NeurIPS 37, DOI 10.52202/079017-1891, arXiv:2405.19073 (Crossref-confirmed; abstract read, body not opened). The collective-action model is Hardt et al. (2023), ICML [sa; not opened, known from the survey's Section 8].

Key points [read]:
- "Learning" (discover the preferences) versus "steering" (move the distribution to one more favourable); the latter is unique to performativity.
- Three differences from the 1950s economic version: parametric (not fully expressive) models, so stability and optimality come apart; performativity can act in features as well as labels; the causal object is the individual-level prediction, which aggregates into a population response.
- **Performative power** (Def. 4): P := sup_{f in F} (1/|U|) sum_{u in U} E dist(z(u), z_f(u)), the largest average change in participants' data points that the firm can cause by choice of action. Properties stated: a monopoly maximises it; ability to personalise increases it; "already two firms lead to zero performative power" when platforms are perfect substitutes (a Bertrand-style result, reported from Hardt et al. 2022). Steering gain is bounded: PR(theta*) - PR(theta_PO) < xi * P.
- Morgenstern, quoted by the survey: the strength of performativity depends on authority and reach, from monopoly forecast to competing forecasts.

**Group-size content here [read].** The strength of performativity grows with the share of the population exposed to a single predictor and falls with competition. Under no interference between units, P(U) >= (|U'|/|U|) P(U') for U' a subset of U, so a measured sub-population effect scales down by its traffic share. [✎ 2026-10-30] It is **not** the only explicit n-dependence: Section 8 ("Algorithmic collective action") models a collective of fractional size alpha in (0,1] that coordinates its data, the firm learning on P = alpha P* + (1 - alpha) P0, with success probability S(alpha) of a planted signal (Theorem 7 there, from Hardt et al. 2023) and the claim that "a collective of vanishing fractional size succeeds with high probability" when the signal is rare. That is a group acting together on a model, though by a fixed agreed strategy, not by members influencing one another over time.

**Empirical standing.** [✎ 2026-10-30: the earlier line said estimation from real data was future work; Section 7, which this file says was read, reports it.] Section 7 cites Mendler-Dünner, Carovano & Hardt (2024): a randomized experiment run by a browser extension on search users found that "distortion of traffic at the first position can be as large as 66% through consistent down ranking", and a worked example converts this into a conservative lower bound of about 30% of a competitor's traffic that Google can influence (Theorem 6, Hardt et al. 2022: performative power >= the causal effect of position, assuming no interference). This is a measured steering size on people, for a platform, not an estimate of epsilon-sensitivity.

**Operand/operator translation for 6 [inference].** Treat a published model M as an operator P_M on the state of a group. Existence of a fixed point: P_M(s) = s. A stable model exists if P is continuous (6a); converges under iterated updating if the Lipschitz constant of P times the curvature ratio is below 1 (6b). That gives a candidate theorem form for the algebra: "a model of group dynamics survives publication iff its induced response operator is a contraction in the appropriate metric". It is not a theorem about drives; it is a constraint on any model that is allowed to be seen.

---

## 7. MacKenzie, performativity of economics (2003 article; 2006 book)

**Citations.** MacKenzie, D. (2003). An equation and its worlds: bricolage, exemplars, disunity and performativity in financial economics. *Social Studies of Science* 33(6): 831-868. DOI 10.1177/0306312703336002 (Crossref-confirmed). [read, performativity passages and conclusion]. MacKenzie, D. (2006). *An Engine, Not a Camera: How Financial Models Shape Markets*. MIT Press. **Not read; [sa].**

**Vocabulary [read].** Performativity (borrowed from Callon; the "Barnesian" strong sense is referenced via Barnes 1983); "social-kind" terms or "human kinds" with "looping effects" (Barnes, Hacking); "bricolage".

**Operands.** Option prices, the Black-Scholes(-Merton) equation, market assumptions (lognormal price movements, no transaction costs, free borrowing, no penalty for short selling).

**Claims [read].**
- "Option pricing theory seems to have been performative in a strong sense: it did not simply describe a pre-existing world, but helped create a world of which the theory was a truer reflection."
- "As an empirical description of patterns of option pricing, the equation started out as only a rough approximation, but then pricing patterns altered in a way that made it more true." Two reasons: the equation was used in arbitrage, and the hypothetical world embedded in it (e.g. frictionless trading) became more real. R. C. Merton is quoted: "reality will eventually imitate theory".
- It is incomplete and reversible: "the performativity of classic option pricing theory is incomplete and historically specific - it did not make itself wholly or permanently true". After the 19 October 1987 crash, fit between prices and the model deteriorated again (citing Rubinstein 1994) and the "volatility skew" appeared; the 1987 fall was, on the lognormal assumption, "grotesquely unlikely" (Jackwerth & Rubinstein 1996 put the probability at 10-160 as printed in the extraction, presumably 10^-160). MacKenzie reads the skew as the market's "collective defence mechanism against systemic risk". The assumption of rational egoism "has not in general been brought fully into being".
- Caution he gives himself: "That the theory can be performative does not imply that it has been performative"; it needs empirical examination.

**Scale.** Market (crowd/adoption). Participants are professional traders and exchange staff, hundreds to thousands; the paper reports no number-of-participants dependence.

**Consent vs manipulation.** Adopters used the model voluntarily because it made money (arbitrage), so the loop ran through informed, self-interested users, unlike Merton's depositors. The model changed the world through *use*, not through persuasion.

**Empirical standing.** One historical case chosen "in part because it seemed a plausible case of performativity" (his words), so a favourable case, not a sample. Quantitative support is from Rubinstein's price comparisons, cited, not shown in what I read. The book is cited in the literature for further cases (e.g. CAPM) but I did not read that. [✎ 2026-10-30: "found no source" was wrong; a search finds one.] The graded terms are MacKenzie's, but from later work, not this article: Mäki ("Saving Austin from MacKenzie", LSE-hosted copy) attributes to MacKenzie (2006, p. 17; 2007, pp. 55-56) a ladder of **generic** performativity (a model is used by participants), **effective** (that use changes economic processes) and **Barnesian** (use makes the process more like the model), with **counterperformativity** (use makes it less like the model) as the opposite; MacKenzie & Bamford develop counterperformativity in *New Left Review* II/113 (2018). All [sa]: neither the book nor these secondary texts were opened here. Earlier wording in this file had the ladder backwards ("strong ... generic"); generic is the weakest rung.

**Operand/operator translation [inference].** A *usable* model of group behaviour is itself a drive-shaper, since it changes payoffs and information. MacKenzie's case shows the loop can raise a model's accuracy (for a while) and then lose it when a mechanism the model omitted (tail risk) becomes salient.

---

## 8. Soros, reflexivity

**Citation.** Soros, G. (2013). Fallibility, reflexivity, and the human uncertainty principle. *Journal of Economic Methodology* 20(4): 309-329, DOI 10.1080/1350178X.2013.859415 (Crossref-confirmed 2026-10-30). [read, author's site, full text; no equations; key quotes re-checked 2026-10-30] Earlier: *The Alchemy of Finance* (1987) [sa, not read].

**Vocabulary [read].** Fallibility ("participants' views of the world never perfectly correspond to the actual state of affairs"); reflexivity ("these imperfect views can influence the situation to which they relate through the actions of the participants"); cognitive function (understand the world, "the direction of causation is from the world to the mind"); manipulative function (affect the world, "from the mind to the world"); human uncertainty principle (fallibility plus reflexivity). "Fallibility is the firstborn: without fallibility there would be no reflexivity."

**Operands.** Participants' views (subjective) and the actual state of affairs (objective). **Operators:** the two functions as opposed arrows. When both run at once, "neither function has a genuinely independent variable - the relationship is circular or recursive."

**Equations.** None. The book-length claims are verbal, with diagrams (Figures 1-4).

**Boom-bust theory [read].** "Every bubble has two components: an underlying trend that prevails in reality and a misconception relating to that trend." Stages (Figure 4): AB trend not yet recognised; BC acceleration; CD testing; DE conviction; EF widening gap; F "moment of truth"; FG "twilight period"; G crossover; GH crash; HI partial recovery. He says booms are slow and busts abrupt. Mechanism examples: leverage and collateral (real-estate boom where "the misconception is that the value of the collateral is independent of the availability of credit").

**Theorems or predictions.** None formal. He says explicitly that universal laws of the kind Popper's scheme demands cannot be had, and that "time- and context-bound generalizations" are what is available. He asserts that the efficient-market hypothesis and his theory are testable alternatives and "that my theory of reflexivity is superior, even in its current rudimentary stage", but he gives no test, only historical cases (1980s real estate, 2007-08, euro crisis) and his own trading record. He calls the framework "rudimentary".

**Empirical standing.** None beyond narrative. Nobody, in the text I read, has fit the boom-bust stages to a dataset; I did not search for third-party tests. A critique and further commentary sit in the same special issue (Notturno 2013 and others), not read.

**Scale.** Markets and policy-market interaction (crowd). Soros notes that Figure 1 handles one participant and "multiple participants would need three dimensions". He offers no result on how the loop strength scales with the number of participants.

**Consent vs manipulation.** Participants act on their own views; authorities interact reflexively with markets (central banks). No consent dimension is discussed.

**Operand/operator translation [inference].** Soros's two functions are exactly the two arrows in a feedback system, and his claim is that equilibrium is the special case where subjective view equals objective state. Formally this is a fixed point again, now of a two-variable system (views, facts). The Grunberg-Modigliani and Perdomo results are the mathematics of the same object, which Soros does not cite in the paper I read.

---

## What exists vs what does not

**Exists.**
- A correct, precise formal statement of when a public prediction can still come true (existence by continuity, section 6a, [sa for 1954 papers]) and when retraining converges to a stable one (Theorem 3.5, [read]). A measure of steering strength (performative power, [read, via survey]).
- A good taxonomy of metric-failure mechanisms with toy equations (Manheim & Garrabrant, [read]); three of the four classes require no reflexivity at all.
- A strongly-qualified documented case of a model making itself true for about 14 years and then not (MacKenzie 2003, [read]).
- A negative result: the textbook Hawthorne effect is not in the original data (Levitt & List, [read]); the broader literature shows a small, heterogeneous effect, odds ratio roughly 1.06-1.2 (McCambridge, [read]).

**Does not exist (in what I found).**
- A measured epsilon (sensitivity of a human group to a published model of itself) from real behaviour. (A measured lower bound on *performative power* does exist, for online search: Mendler-Dünner, Carovano & Hardt 2024. It sizes steering; it is not epsilon.)
- Any treatment of **interacting** groups: the formal results I read treat the respondent population as individuals reacting to one predictor; none has respondents influencing each other over time. Group size enters as audience share (performative power), as sampling n, or as the size alpha of a coordinated collective (algorithmic collective action, survey Section 8), which is a group acting on a model by a fixed shared strategy, not peer influence. [✎ 2026-10-30: the collective-action case was missed.]
- Any result that predicts *which* agents will game a metric and by how much; Campbell's evidence is anecdotal.
- A tested version of Soros's boom-bust stages.
- A formal treatment of the suicidal prophecy beyond Merton's footnote (Perdomo-type theory covers it implicitly through the sign of dD/dtheta, but the examples used are self-fulfilling). MacKenzie's "counterperformativity" names the same direction for models in markets, verbally, not formally [sa].
- Lucas's own text (not read), so no direct check of what he claimed about invariance.

## Unconfirmed

- Exact wording and page of Lucas's key sentence; his notation. Not read.
- Goodhart's original 1975 sentence. Not read (quoted second-hand by Manheim & Garrabrant).
- Grunberg-Modigliani 1954 and Simon 1954 details (exact theorem conditions, any treatment of discontinuous cases). Known only from the 2025 survey.
- MacKenzie 2006 book claims. The generic / effective / Barnesian terms are his (2006 p. 17, 2007 pp. 55-56) per Mäki's account, not checked against MacKenzie's own text.
- Whether the published (AEJ 2011) Levitt-List numbers equal those in the 2009 NBER version read (re-read 2026-10-30 from the NBER PDF; the print was not opened).
- Rudebusch's conclusion is now read in the 2002 working paper and supports "little evidence ... important factor ... given typical sample sizes"; whether the 2005 JMCB print says the same at the same magnitudes is unchecked (Project MUSE copy behind a bot challenge).
- Mendler-Dünner, Carovano & Hardt (2024): the 66% and ~30% figures are as the 2025 survey reports them; the paper's own body was not opened.
- Merton 1948 quotes and MacKenzie 2003 quotes: tagged [read] by the original author; **not re-verified on 2026-10-30**. The only open Merton copy is a JSTOR scan re-hosted on a course site, which this pass did not fetch; the Edinburgh repository copy of MacKenzie 2003 returned a bot challenge / 403.
- Garrabrant's 2017 "Goodhart Taxonomy" post (origin of the four classes): not opened.
- The two threshold remarks (Merton's "enough depositors", the oscillation of Example 3.4) as a link between bank-run multiplicity and the discontinuous response case: **[inference]**, not stated in any text I read.

---

## Does it reduce to a drive basis?

**Mostly not, and that is the finding.** What this tradition contains is not drives; it is a layer *on top of* drives:

- **Reduces to drives (partly).** Hawthorne's mechanism, as McCambridge et al. report the widespread (untested) explanation, is conformity and social desirability given a belief about the observer's expectations. In a drive vocabulary this is a belonging or approval drive acting on a perceived expectation; Levitt and List's folk reading ("attention to employees") is the same. Campbell's corruption pressure is an incentive-seeking drive (jobs, money, power) redirected from the goal to the indicator. Merton's depositors are fear acting on a belief about others' fear. Lucas's stability claim is explicitly that *tastes and technology* (deep parameters) are invariant while behavioural rules are not, which is a drive-primitives claim, but its text is unread and its test is Rudebusch's small-effect simulation.
- **Does not reduce to drives.** (i) The *belief about what others believe* is the operand in Merton, Soros, MacKenzie and Perdomo, not a drive; it is a second-order informational state. (ii) The response map R or D(theta) is a property of a *population plus a model*, not of any one drive; its Lipschitz constant epsilon depends on how many agents see the prediction and how they interact, which no drive-level object supplies. (iii) Goodhart's regressional and extremal classes are statistics (noise, extrapolation), unrelated to drives. (iv) The fixed-point and contraction conditions are properties of the whole feedback system, so they are *theorems about composition*, not about primitives.
- **Consequence for the algebra [inference].** If the algebra is to stay valid once its models are known to the people in it, drives alone are not enough; it needs (a) a belief-about-state operand, (b) a "publish" or "observe" operator mapping a model to a perturbation of drive parameters, and (c) a condition (continuity and contraction) on the composite. Of these only (c) has a published mathematical form.
- This does not refute "drives as primitives"; it says the drive layer is silent on exactly the step this section's tradition is about.

## What does it predict or control, and how well?

- **Merton / Soros:** they predict *that* a belief-outcome loop can exist, not when or how strongly. Merton gives no quantity; Soros asserts superiority over efficient markets without a test. Out-of-sample evidence: none presented. Accuracy: not assessable.
- **Hawthorne:** as a prediction ("any change in light raises output") it failed in the original data (Levitt & List). As a weaker prediction ("being studied shifts behaviour slightly") it is supported with a pooled odds ratio of about 1.06 in trials and 1.2-1.3 in observational designs (McCambridge), but with high heterogeneity, mostly in health settings, and a low-quality literature. It does not control anything; it is a bias to be allowed for.
- **Campbell / Goodhart:** they predict, qualitatively, that rewarding an indicator corrupts it. Evidence is anecdotal (Campbell's own word) with no effect sizes or failure rates. The formal taxonomy (Manheim & Garrabrant) is toy models with no data. Control claim: no reliable intervention beyond independent watchdogs, which Campbell proposes without testing.
- **Lucas:** predicts that reduced-form coefficients shift when policy rules shift. In the single simulation-based assessment I partly read (Rudebusch), real shifts were found in policy rules while reduced forms stayed statistically stable, and the effect is argued to be small. So the critique's qualitative prediction is right and its practical size can be small. Text unread.
- **MacKenzie:** predicts that a widely used model can pull the market toward itself; it did, 1973-1987 by the evidence cited, then lost fit after the 1987 crash. One favourable case. This is the closest the tradition comes to a *successful steering* case, and it also shows the limit: a model that omits a mechanism (tails) is overtaken by it.
- **Performative prediction:** *proved* convergence and distance bounds (for example ||theta_PO - theta_PS|| <= 2 L_z epsilon / gamma) under stated conditions. Verified only in simulation on a modelled response. Failures it explicitly proves: no convergence if epsilon >= gamma/beta, a loss that is merely convex, or a discontinuous map. Control claim: a deployer with performative power P can gain at most xi * P over non-steering. Out-of-sample evidence on people: none for the convergence theorems; one randomized field measurement of steering size (search ranking, Mendler-Dünner et al. 2024, as reported by the survey).
- **Net:** the tradition predicts the *existence and direction* of loops well, their *size* poorly or not at all, and offers one condition (continuity plus a contraction bound) under which a model survives being known. No intervention here is shown to work at group scale, on consent, with a measured effect size.

## Validation log (2026-10-30)

- ? Merton 1948: exists, author and JSTOR/Crossref 10.2307/4609267 confirmed; quotes not re-verified (only open copy is a re-hosted JSTOR scan, not fetched this pass). No equation rests on it.
- ✓ Levitt & List 2011: DOI resolves; NBER WP 15016 re-opened; equation (1), the null day-of-change result, 3-4% Panel B result and its disappearance, 0.0865 units per foot-candle, "entirely fictional" all match.
- ✎ McCambridge, Witton & Elbourne 2014: DOI and all odds ratios (including the printed 1.29 [1.06, 1.30]) confirmed in Europe PMC full text; corrected the mechanism (a "widespread" explanation the review reports, not its own) and the overstated covert-vs-announced contrast.
- ✎ Campbell 1976/1979: both DOIs resolve; JMDE reprint re-opened, law and examples confirmed; corrected the multiple-indicators line (the doubt is Ridgeway's, Campbell leans the other way).
- ✎ Manheim & Garrabrant 2019: arXiv re-opened, equations (1)-(3), (7) and quotes confirmed; added credit that the four classes were introduced by Garrabrant (LessWrong, Dec 2017), as the paper itself says.
- ✓ Goodhart 1975 / 1984 reprint: DOI resolves (pp. 91-121); wording remains [sa] via M&G, which was confirmed verbatim.
- ✓ Lucas 1976: DOI resolves; text still not open, stays [sa]; no open-access copy per Unpaywall.
- ✎ Rudebusch 2005: corrected pages to 245-272 and added DOI 10.1353/mcb.2005.0024; read the 2002 WP conclusion, which supports "small in this setting" with stated caveats.
- ✎ Grunberg & Modigliani 1954; Simon 1954: DOIs found and confirmed, issue numbers added; content stays [sa] (paywalled).
- ✎ Perdomo, Zrnic, Mendler-Dünner & Hardt 2020: arXiv v4 re-opened; Defs 2.1, 2.3, 3.1, Examples 2.2, 3.4, Theorems 3.5, 3.8, 4.3, Props 3.6, 4.1 and the Section 5 best response confirmed; corrected Theorem 3.10's sample size (log(t/p), and epsilon < gamma/(2 beta) for RERM); PMLR pages added; Kaggle dataset named.
- ✎ Hardt & Mendler-Dünner 2025: published venue and DOI added; GMS account, Def. 4, xi * P bound, two-firm result confirmed; corrected the claim that real-data estimation was future work (Section 7 reports Mendler-Dünner, Carovano & Hardt 2024) and the claim that audience share was the only n-dependence (Section 8, collective action of size alpha).
- ✎ Hardt, Jagadeesan & Mendler-Dünner 2022; Mendler-Dünner, Carovano & Hardt 2024: added with Crossref-confirmed DOIs, credited for the results the survey reports.
- ? MacKenzie 2003: DOI resolves; open copy returned a bot challenge, quotes not re-verified. ✎ "No source for generic/effective" was wrong: Mäki attributes the terms to MacKenzie 2006/2007 [sa]; the ladder direction in the old text was corrected.
- ? MacKenzie 2006 book: exists; not opened.
- ✓ Soros 2013: DOI 10.1080/1350178X.2013.859415 resolves to the right paper (the old "no DOI" note was a wrong DOI tried); full text on the author's site re-opened and eight quotes confirmed.
- No fabrications found; nothing deleted.

Sources opened this pass: 9 primary texts (Perdomo et al. arXiv; Hardt & Mendler-Dünner arXiv; Manheim & Garrabrant arXiv; Campbell JMDE reprint; Levitt & List NBER WP; McCambridge et al. Europe PMC; Rudebusch FRBSF WP; Soros author's site; Mendler-Dünner et al. 2024 arXiv abstract), plus Crossref for every DOI. Two attempted and blocked (MacKenzie 2003 Edinburgh copy; Rudebusch at Project MUSE).

Verdict: the file is careful and mostly accurate. Every equation and theorem it relies on (Perdomo et al., the survey's GMS statement, Manheim & Garrabrant, Levitt & List) matches the text. The errors were in the gaps it reported: real-data measurement of performative power and a group-size (collective action) model both exist, in a section the file says it read. There were also three misattributions: Campbell on multiple indicators, the McCambridge mechanism, and Garrabrant's credit for the taxonomy. Merton and MacKenzie 2003 quotes keep the original author's [read] tag but were not re-checked here, so nothing should be built on them until they are.

## Cross-checks (2026-10-30)

Cross-checked against the other prior-work files (grep of names, works and key terms, 2026-10-30). No file in prior-work re-reads any of these works; the overlaps are with this file's topic from other angles. Cluster T (research-map, D583).

**Agreements**
- `092-outcome-measures-of-behaving-better.md` §4 states the Campbell/Goodhart point (a measure used as a target will move) and defers ownership to this file. Agrees; no conflict.
- `066-aggregation-rules-granovetter-kuran-deep-read.md` (Relation to Granovetter) says Granovetter and Kuran share one mathematical object: a population share mapped to an induced share, with a fixed-point condition and stable/unstable roots set by slope versus 1. This is the same structure as the Grunberg-Modigliani fixed point in §6a. Agrees on structure; the two differ in what the map is (threshold aggregation versus a prediction's own effect).
- `038-organisational-motivation.md` (Equations) describes a self-fulfilling loop, practice to behaviour to evidence to assumption. Same loop shape as Merton (§1), in an organisational domain. Agrees on structure; not a source for Merton's claim.

**Not overlaps (same name or topic, different works)**
- `06-group-dynamics-frameworks.md` cites Merton (1957) on the role-set. Different paper from Merton (1948) here.
- `036-axiomatic-economics-of-desire.md` and `021` cite Campbell & Cochrane (1999) on habit. Different Campbell and different subject from Campbell (1976/1979) here.
- `03-interaction-as-operator.md` and `07-applied-control-of-groups.md` use "reflexive" in Lefebvre's sense (reflexive control). Different concept from Soros's reflexivity and from performativity.
- `056` and `042` use "reflexive" for Williams's ostracism stage. Different concept.

**Contradictions**
- UNRESOLVED. Levitt & List (§2, read): the textbook Hawthorne effect (every change raises output) is not in the 1927-32 illumination data; day-of-change effect is insignificant and near zero. McCambridge et al. (§2, read): pooled observation-effect odds ratios of 1.06 to 1.21 across 19 studies. The file reconciles these in "What exists" by reading one as the folk effect and the other as a broader, small, heterogeneous effect, mostly in health settings. That reconciliation is this file's inference, not a validation result, so both claims are recorded as they stand. Neither source is a re-test of the other.
- SETTLED by validation log (2026-10-30). Campbell (§3): multiple indicators. The earlier line attributed the doubt to Campbell; the source attributes it to Ridgeway (1956), and Campbell himself leans toward multiple indicators helping. Corrected in §3 and in the validation log.
- SETTLED by validation log (2026-10-30). McCambridge (§2): the mechanism (conformity and social desirability) was presented as the review's own; it is the "widespread" explanation the review reports, untested by it. Corrected in §2.

**Provenance notes for the ledger**
- The file's "[inference]" items (operand/operator translations, the "reduces to drives" section, the Merton threshold and the Perdomo-Merton link) are not source claims. They are not given ledger lines below, since the provenance field admits only read or sa.
- The Mendler-Dünner, Carovano & Hardt 2024 numbers (66%, about 30%) are tagged in the file as read via the 2025 survey, and the 2024 body was not opened. Recorded as sa in the ledger.

**Ledger lines, structured.** Returned to the orchestrator in the StructuredOutput call and not written to `docs/ledger.jsonl` or `docs/ledger.md` (not edited, per the instruction). Cluster T for all.
