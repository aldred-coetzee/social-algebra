# Prior work 070: measured coupling matrices for human groups of three or more

Direction: D317

Date: 2026-10-29. Kind: survey. Question: has anyone estimated a coupling (community / VAR / oscillator) matrix for a human group of n >= 3 and reported its eigenvalues or stability? Seeds: Ferrer & Helm 2013; Helm, Sbarra & Ferrer 2012; van de Leemput 2014; Wichers 2016.

**Method and honesty note.** This file is thin by design because the literature is thin, and the session was constrained. The web-search quota ran out partway through (the tool said so), PMC and the ACM and PNAS PDFs sit behind bot checks (reCAPTCHA / 403 / Cloudflare), and the Frontiers PDF that came back was an unrelated individual-VAR paper (Bulteel et al. 2016, read only to discard it). **No primary full text was read this session for any work below.** Everything is [abs] (abstract, or a search summary of it), [std] (standard textbook content, not checked here) or [derived] (my own algebra from a stated form, not in any source). DOIs were checked on Crossref (Helm 2012, Ferrer & Helm 2013, Moulder 2022) or Europe PMC. Cross-references: 20 (dyadic coupling), 27 (measuring drive dynamics), 30 (ecological stability, the May test), 059 and 060 (influence functions; n-actor extensions).

## Summary

1. **Answer: no.** I found no study that fits a coupling matrix to three or more people and reports its eigenvalues, spectral radius or any stability verdict. The nearest is one conference paper on triads that reports network node strengths, not eigenvalues; validation added a second near miss, a mother-father-adolescent affect network (Bodner et al. 2018, section 5), also without eigenvalues in its abstract. "Not found" is not "does not exist" (see Unconfirmed), but file 30's claim that nothing exists at S well above 2 stands, and it stands at S = 3 as well.
2. **None of the four seeds is about a group of three or more.** Helm, Sbarra & Ferrer 2012 and Ferrer & Helm 2013 are dyads (Ferrer & Helm's abstract gives 32 couples; Helm 2012's abstract gives no sample size). van de Leemput 2014 and Wichers 2016 are individual mood series. The seed list tests the ground just short of the question.
3. **Eigenvalues are never the reported quantity** in the dyadic work either. Estimates are per-parameter (self-regulation, coregulation) compared across tasks and people. The stability read-off (eigenvalues of the 2x2 or 4x4 system) would be [derived] from those parameters, not published.
4. The useful output here is a **derivation**: how the stability of a symmetric n-person coupling matrix depends on n, which the algebra can use before any data exist (section 6).

## 1. Helm, Sbarra & Ferrer (2012): coupled linear oscillators in couples

**Citation.** Helm, J. L., Sbarra, D. & Ferrer, E. (2012). Assessing cross-partner associations in physiological responses via coupled oscillator models. *Emotion* 12(4), 748-762. DOI 10.1037/a0025036 (Crossref: confirmed, title, authors, volume, issue, pages; PMID 21910541). Not open access in this session.

**Their vocabulary.** Interdependence, cross-partner association, synchrony, coupled linear oscillators (after Boker & Nesselroade 2002).

**Drives/operands.** Respiration and heart rate of each partner; not a named drive.

**Operators / equations.** Coupled linear oscillators, the standard second-order form [std], not read: for partner i, x_i'' = eta_i x_i + zeta_i x_i' + gamma_i x_j (+ gamma' x_j'), i.e. self-term, damping, and a cross term from the partner. Exact parametrisation in the paper not verified.

**Theorems or derived predictions.** None. Hypothesis-testing of non-zero coupling.

**Empirical standing.** [abs, PubMed abstract checked in validation] Romantic partners, three lab tasks, sample size not stated in the abstract (32 couples is the Ferrer & Helm 2013 sample and comes from press coverage here; same lab and measures, but same sample not verified); "associations were detectable within all three tasks, with different patterns of coupling within each task". A control (non-partner pairings) showing no synchrony, and women adjusting more to partners than men, come only from press coverage [secondary]; neither is in the abstract. Single lab, one dyad type (heterosexual couples), no predictive validation. Blunt: shows coupling is detectable above a shuffled baseline; says nothing on stability.

**Translation.** Operand: person-state pair. Operator: the cross term gamma, an off-diagonal entry of the coupling matrix. Gives a 2x2 (in first-order form 4x4) matrix per couple, estimated. Group extension is a larger matrix; nobody has estimated one.

## 2. Ferrer & Helm (2013): dyadic differential equations for coregulation

**Citation.** Ferrer, E. & Helm, J. L. (2013). Dynamical systems modeling of physiological coregulation in dyadic interactions. *International Journal of Psychophysiology* 88(3), 296-308. DOI 10.1016/j.ijpsycho.2012.10.013 (Crossref: 2013, vol 88, issue 3, pp 296-308; PMID 23107993; the 2012 elsewhere is the online date).

**Their vocabulary.** Self-regulation, coregulation, dyadic system of differential equations (Felmlee & Greenberg 1999).

**Operators / equations.** [abs] "a system of differential equations developed for dyadic research (Felmlee and Greenberg, 1999)", with "parameters representing self-regulation and coregulation for each individual in the dyad", fitted directly to each dyad, distributions of parameters examined, compared across three tasks, and parameters related to those from a similar model on daily self-reported affect. Equation form not read.

**Empirical standing.** [abs; "individuals in 32 couples", Felmlee and Greenberg 1999, self-regulation/coregulation, three tasks and daily self-reports of affect all confirmed in the PubMed abstract in validation] 32 couples, heart rate and respiration. Per file 20, effects modest and context-dependent. Blunt: parameters estimable per dyad; the link to daily-affect parameters is an association across 32 couples, not a prediction.

**Translation.** As section 1. The per-dyad fit is the template that a triad would need; it is a dyad-only study.

## 3. van de Leemput et al. (2014) and Wichers et al. (2016): the stability-from-data tests, not groups

Already treated in 27 (numbers, failures) and 30 (design). Restated only for the stability link. van de Leemput, Wichers, Cramer, Borsboom, Tuerlinckx, Kuppens, van Nes, ... Scheffer 2014, *PNAS* 111(1), 87-92 (online 2013-12-09), DOI 10.1073/pnas.1312114110 (Crossref confirmed; Europe PMC PMC3890822); Wichers, Groot & Psychosystems, ESM Group, EWS Group 2016, *Psychother Psychosom* 85(2), 114-116, DOI 10.1159/000441458 (Crossref confirmed; a single-patient case study).

**What they test.** [abs, via 27 and 30] Rising autocorrelation, variance and cross-emotion correlation in individual emotion series predicts transitions into or out of depression. This is the data-side use of the eigenvalue idea: for x_{t+1} = A x_t + e [std], lag-1 autocorrelation of the slowest mode tends to its eigenvalue, so |lambda_max| -> 1 shows as rising autocorrelation and variance [std; not read in either source this session].

**For this question.** Both are person-level; the "system" is the person's emotion set. The matrix A (a VAR(1) community matrix) is not reported as a matrix. Later work (27: Helmich 2023, 2024) finds the signals weak as prediction. So the only eigenvalue-flavoured human test uses a proxy for the eigenvalue, on individuals, and the proxy is contested. PMC full text of van de Leemput was not retrievable this session (bot check), so no passage is quoted.

## 4. The one group-of-three measurement found: Moulder, Duran & D'Mello (2022)

**Citation.** Moulder, R. G., Duran, N. D. & D'Mello, S. K. (2022). Assessing multimodal dynamics in multi-party collaborative interactions with multi-level vector autoregression. *Proceedings of the 2022 International Conference on Multimodal Interaction (ICMI '22)*, pp. 615-625. DOI 10.1145/3536221.3556595 (Crossref: confirmed, issued 2022-11-07). Open access (CC BY per Semantic Scholar/Unpaywall), but the ACM PDF sits behind a Cloudflare check; only the full abstract was read [abs], and in validation every abstract claim below (9 signals, 201 users, 67 triads, 15 minutes, in-strength/out-strength/synchrony, three roles, skin-conductance feedback) was checked against it.

**Their vocabulary.** Multi-level VAR (mlVAR), dynamic network, in-strength, out-strength, synchrony, controller / primary contributor / secondary contributor.

**Drives/operands.** Nine signals per user: positive and negative valence, skin conductance, heart rate, gaze fixation duration, gaze dispersion, head acceleration, facial expressiveness, speech rate. Not drives, but affect, arousal, attention and expression: the layer a drive would sit beneath.

**Operators / equations.** [abs] mlVAR, a lagged regression network; lag order, centring, and whether the network is within-person or across the triad's members not stated in the summary. The network metrics are node in-strength and out-strength (column and row sums of absolute or signed coefficients, definition not read) and "synchrony". No eigenvalue or stability analysis is mentioned in the abstract.

**Theorems or derived predictions.** None. Role classification from node metrics.

**Empirical standing.** [abs] 201 users in 67 triads, 15-minute collaborative task. Roles distinguishable by the metrics; a feedback loop in which skin conductance is driven by gaze and speech. Single task, lab, conference paper, no replication seen; roles are reported as distinguished but the check against an independent role label is not known to me.

**Translation.** This is the clearest found estimate of a directed influence structure among three people (see also Bodner et al. 2018 in section 5) that is, in form, a coupling matrix (here an mlVAR network over many signals). Operand: the (person, signal) pair. Operator: the lagged coefficient. The missing step is exactly the one D317 asks for, computing the spectrum of the estimated matrix and checking it against a stationarity bound. mlVAR requires stationarity as an assumption [std], so the fitted model was presumably stable, but that is not reported in what I read.

## 5. Adjacent but not the answer

- **Bodner, Kuppens, Allen, Sheeber & Ceulemans (2018), "Affective family interactions and their associations with adolescent depression: a dynamic network approach", *Development and Psychopathology* 30(4), 1459-1473, DOI 10.1017/S0954579417001699 (Crossref confirmed; online 2017-11-20; PMC5960596).** Added in validation as a test of the "nothing exists" claim. [abs] Mother, father and adolescent during a problem-solving interaction; a network of concurrent and temporally sequenced coded affect among the three members, compared between families with and without a depressed adolescent; anger forms "a more self-sustaining network" in depressed families. A temporal n = 3 influence network of named affect, so a closer fit to the question than section 4 on operands; but the abstract reports no eigenvalue or stability analysis, and the method (coded behaviour sequences, likely not a continuous VAR; per-family or pooled not known) was not read. "Self-sustaining" is the qualitative cousin of a spectral-radius statement. Read this first alongside Moulder.
- **Alderisio, Fiore, Salesse, Bardy & di Bernardo (2017), *Scientific Reports* 7, 6846, DOI 10.1038/s41598-017-06559-4 (Crossref confirmed) (7 people, Kuramoto network on four graphs).** Read in full in 060. Fitted a single coupling constant per group (two groups) on a known graph, not a free matrix and not eigenvalues. Closest numerical n >= 3 result with human data, but it estimates one scalar.
- **Group physiological synchrony and cohesion (N = 261, Frontiers in Human Neuroscience 2022, multidimensional recurrence quantification on inter-beat intervals).** [abs, search summary] Compares synchrony before and during group interaction, relating change to reported cohesion. A scalar synchrony index per group; no coupling matrix. Citation details not verified: treat as a lead.
- **Dyadic idiographic ODE fitting** (Psychometrika paper, AICc model selection per couple; independence the most common pattern) [abs, search summary; authors and DOI not verified]. If "independence is most common" holds, the dyadic coupling that exists is often zero per couple, which matters for the stability question.
- **Triadic theoretical extensions** (Bielczyk, Foryś & Płatkowski, "Dynamical models of dyadic interactions with delay", arXiv 1202.2338, authors and title confirmed on arXiv; parental-influence love models). Theory only, no data (see 060).

## 6. What the algebra can do before the data exist [derived]

Not from any source; my calculation, for the linear model dx/dt = A x with n actors, A = a I + b (J - I), J the all-ones matrix (exchangeable actors, diagonal a = self-term, every off-diagonal b = pairwise coupling).

- Eigenvalues: **a + (n-1) b** once (the shared mode, eigenvector all ones), and **a - b** with multiplicity n-1 (the contrast modes, eigenvectors summing to zero).
- Continuous-time stability needs both negative: a + (n-1) b < 0 and a < b. With a < 0, the group-wide mode destabilises when b > -a/(n-1) for b > 0. **The tolerable uniform pairwise reinforcement falls as 1/(n-1)**: with a = -1, b = 0.4 is stable for n = 3 (eigenvalue -0.2), marginal at n = 3.5 and unstable at n = 4 (eigenvalue +0.2). Positive uniform coupling (mutual excitation, contagion) gets less safe with size; negative b (mutual inhibition) destabilises the contrast modes instead when b < a, i.e. when mutual damping exceeds self-damping. Discrete-time (VAR(1)) analogue: |a + (n-1) b| < 1 and |a - b| < 1.
- This is the n-scaling that file 30's May criterion expresses with random coupling; the exchangeable case is the deterministic counterpart and needs no random-matrix result. It is a prediction, not a measurement.
- For a dyad (n = 2) the same form gives eigenvalues a + b and a - b: the in-phase and anti-phase modes. This is what a fitted couple's 2x2 matrix would be read through, and nobody reports it.

## What exists vs what does not

**Exists.** Estimable per-dyad coupling parameters in physiology and daily affect (1, 2). Individual-level critical-slowing proxies for the eigenvalue (3), weak as prediction (27). One n = 3 mlVAR network of mixed signals with node-level metrics (4), and one family-triad temporal affect network described as "self-sustaining" (Bodner 2018, section 5). A seven-person Kuramoto fit with a scalar coupling (060).

**Does not exist (as far as I found).** An estimated n >= 3 coupling matrix for a named affect or drive with its eigenvalues reported. Any stability verdict on a measured human group matrix. Any replication of a group-level matrix. Any test of the A = aI + b(J-I) scaling above. Group data with enough time points per member: a 15-minute triad session yields few observations per cell for a 3x3 or 27x27 matrix, so this may be a data-volume problem as much as a literature gap [inference, not checked].

## Unconfirmed

- Moulder 2022: everything beyond the abstract (lag, definition of strength, whether any eigenvalue or stationarity check is reported, effect sizes). The most likely single place to find a group matrix; read it first.
- Helm 2012 and Ferrer & Helm 2013: parameter equations and estimates (only abstracts and press summaries seen). The 32-couple figure is confirmed for Ferrer & Helm 2013 (abstract) but not for Helm 2012, whose abstract states no n; the sex difference and the non-partner control come from press coverage only.
- Bodner et al. 2018: method, time resolution, whether edges are per family or pooled, and whether any stability quantity is reported. PMC and Europe PMC full text were blocked (reCAPTCHA / 403 / 500) in validation.
- The exact oscillator parametrisation in section 1 is [std].
- The 2022 Frontiers synchrony-cohesion paper and the Psychometrika idiographic dyad paper: located only through search summaries; no DOI checked.
- van de Leemput 2014 and Wichers 2016 were not re-read; they rest on 27 and 30.
- Unsearched (quota ran out): multilevel VAR for families (Sels, Kuppens and colleagues' interpersonal emotion dynamics work), team physiological synchrony (Gordon et al.), dynamic structural equation models for triads, social relations model with time. A follow-up search should target these and "three or more" family and team EMA with VAR.

## Validation log (2026-10-29)

Every DOI resolved at api.crossref.org; abstracts checked at PubMed (Helm 2012, Ferrer & Helm 2013) and Semantic Scholar (Moulder 2022). No full text was readable (ACM Cloudflare, PMC reCAPTCHA, Europe PMC 403/500), so nothing is tagged [read]. The web-search budget was exhausted at the start of this pass; the "nothing exists" claim was tested by DOI lookup of known literature only.

- ✎ Helm, Sbarra & Ferrer 2012, *Emotion* 12(4) 748-762: DOI, authors, venue ✓; quoted abstract sentence ✓ verbatim; the abstract states **no sample size**, so "32 couples" is not confirmed for this paper; the non-partner control and sex difference are not in the abstract (kept as press-only).
- ✓ Ferrer & Helm 2013, *Int J Psychophysiol* 88(3) 296-308: DOI, authors, 32 couples, Felmlee & Greenberg 1999, self-/coregulation, three tasks, daily affect all confirmed in the abstract; issue number added.
- ✎ van de Leemput et al. 2014, *PNAS* 111(1) 87-92: DOI and authorship confirmed; online date 2013-12-09 noted; content rests on files 27/30.
- ✎ Wichers et al. 2016, *Psychother Psychosom* 85(2) 114-116: DOI confirmed; authorship is Wichers, Groot and a consortium author (Psychosystems, ESM Group, EWS Group); issue added.
- ✎ Moulder, Duran & D'Mello 2022, ICMI '22: DOI, authors, issue date ✓; pages 615-625 added; open-access status noted; every abstract claim checked; "the only found estimate" softened in light of Bodner 2018.
- ✎ Alderisio et al. 2017, *Sci Rep* 7, 6846: full citation and DOI added (Crossref confirmed); "two groups" added; consistent with file 060.
- ✓ Bielczyk, Foryś & Płatkowski, arXiv 1202.2338: authors and title confirmed on arXiv.
- ✎ Bodner, Kuppens, Allen, Sheeber & Ceulemans 2018, *Dev Psychopathol* 30(4) 1459-1473 (**added**): a family-triad temporal affect network that the original survey missed; abstract read, method not.
- ? Frontiers in Human Neuroscience 2022 group synchrony-cohesion paper and the Psychometrika idiographic dyad ODE paper: still no authors or DOI; could not search.
- ✓ Section 6 algebra: eigenvalues a+(n-1)b (once) and a-b (n-1 times) of aI+b(J-I) are correct; the worked numbers (-0.2 at n=3, marginal at n=3.5, +0.2 at n=4 for a=-1, b=0.4) and the discrete-time conditions check out.
- ✎ Summary point 2 said "three of the four seeds are not about groups" while its own text showed all four are not about groups of n >= 3; corrected.

**Verdict.** The file is honest and its citations are real: no fabrications, every DOI resolves to the stated authors and venue, and the [derived] algebra is correct. The main corrections are that the 32-couple sample is confirmed only for Ferrer & Helm 2013, not Helm 2012, and that a second near miss exists (Bodner et al. 2018, a mother-father-adolescent temporal affect network) which weakens "the one group-of-three measurement" without overturning the headline: no measured n >= 3 coupling matrix with reported eigenvalues was found. The "nothing exists" claim remains unsearched beyond known literature because the search budget ran out, so it stands as "not found", not "absent".

## Cross-checks (2026-10-29)

Compared against the other validated files by grep on works, authors, equations and numbers. No other file cites Moulder et al. 2022 or Bodner et al. 2018, so sections 4 and 5 (those two) have no overlap to check. Primary source consulted for the one contradiction: the arXiv abstract page for 1202.2338.

### Agreements

- **Helm, Sbarra & Ferrer 2012 (section 1)** agrees with file 20 section 2 "Empirical" and file 061 (Sources and Unconfirmed): same DOI 10.1037/a0025036, *Emotion* 12(4):748-762, respiration and heart rate, three lab tasks, a different coupling pattern in each. File 061 also reports no sample size, consistent with this file's point that the 32 couples belong to Ferrer & Helm 2013.
- **Ferrer & Helm 2013 (section 2)** agrees with file 20 (same DOI 10.1016/j.ijpsycho.2012.10.013, 88:296-308, 2013 being the print year and 2012 the online date) and file 30 section on estimated coupling matrices (cites both Helm papers as dyadic 2x2 or 2k x 2k fits). "Effects modest and context-dependent" is file 20's wording and is tagged [abs] there.
- **Steele & Ferrer 2011 and the dyad literature**: file 061 section on empirical dyads and file 20 are consistent with this file's claim that dyadic parameters are estimated per couple and eigenvalues are not reported.
- **van de Leemput 2014 (section 3)** agrees with files 27 (section I), 30 (human tests, F3), 53 (section 4): DOI 10.1073/pnas.1312114110, *PNAS* 111(1) 87-92, online 2013-12-09, PMC3890822. **Wichers 2016** agrees with 53: DOI 10.1159/000441458, 85(2) 114-116, authorship Wichers, Groot plus the Psychosystems, ESM Group and EWS Group consortia, single-patient (n = 1). The statement that later work (Helmich 2023, 2024) finds the signals weak as prediction agrees with file 27.
- **Alderisio et al. 2017 (section 5)** agrees with file 060 section 3 and its cross-check list: *Sci Rep* 7, 6846, DOI 10.1038/s41598-017-06559-4, 7 people, Kuramoto network, four graphs, two groups, one coupling constant fitted per group (file 060: c = 1.25 and 4.40), so a scalar and not a free matrix.
- **Bielczyk, Foryś & Płatkowski (section 5)**: title, authors and arXiv 1202.2338 agree with files 20 (section 4) and 060 (section 7); "theory only, no data" agrees. Both of those files also give the journal version, *J Math Sociol* 37(4):223-249, doi 10.1080/0022250x.2011.597279, which this file omits (see the contradiction below).
- **Headline "no measured n >= 3 coupling matrix with eigenvalues"** agrees with file 060 ("any fit of an n-person drive model to data" is not found), file 20 section on gaps ("no fitted network version of Gottman"), and file 30 (nothing estimated at group scale, S well above 2, at the resolution a May-type test needs).
- **Section 6 algebra** agrees with file 30 section A3 (Allesina & Tang): for pure mutualism the outlier eigenvalue is (S-1)*C*E - d, which with full connectivity (C = 1), uniform coupling E = b and d = -a is exactly a + (n-1)b. File 30's note that net-negative (competitive) mean coupling shifts the bulk toward instability matches the contrast-mode eigenvalue a - b going positive for b < a. File 062 section 5.2 independently gets the same (N-1) scaling: the symmetric best-response iteration matrix -s(11^T - I) has spectral radius (N-1)s, which is this file's form with a = 0, b = -s. The worked numbers (-0.2, 0, +0.2 at n = 3, 3.5, 4 for a = -1, b = 0.4) were re-added and are correct.
- **File 30's "S well above 2" qualifier** is consistent with this file's extension to S = 3 (Moulder, Bodner are n = 3 but report no eigenvalues).

### Contradictions and refinements

1. **Bielczyk et al. described as "parental-influence love models" (section 5, last bullet) versus files 20 section 4 and 060 section 7.** Files 20 and 060 (both read the paper at source, 060 section 5 of it) describe the triad as Romeo, Juliet and Paris: Romeo and Paris do not interact, Juliet links both (eqs. 23-24), reducing to an averaged partner when self-attitudes are equal and giving three stability switches otherwise. Nothing about parents. The arXiv abstract (checked this session) says only "Some generalizations to triadic interactions are also presented" and is a delay model of dyads. **Verdict: files 20 and 060 are right; the "parental-influence" gloss in 070 is unsupported and should be read as "a third partner linked to a dyad".** Also, 070 should carry the journal citation given in 20 and 060.
2. **Unidentified "Psychometrika idiographic dyad ODE paper" (section 5, fourth bullet) versus file 061 (Sources, DOI list).** Not a conflict but a resolution: file 061 lists Steele, Ferrer & Nesselroade (2014), *Psychometrika* 79:675-700, doi 10.1007/s11336-013-9366-9. Crossref (checked this session) gives its title as "An Idiographic Approach to Estimating Models of Dyadic Interactions with Differential Equations", which fits the description here (per-couple model selection). Authors and DOI should be added to 070; the claim that independence is the most common pattern is not confirmed from that paper but is echoed by file 061's Ferrer & Steele 2010 slides (a 77-dyad "independent" group, the largest of the types counted, out of 140 classified). Verdict: file 061 supplies the citation; the "independence most common" claim stays [abs, search summary].
3. **Level of inference for van de Leemput 2014 (section 3, "person-level" and "individual emotion series") versus files 27, 30 and 53.** The system is the person's emotion set (agreed), but files 27, 30 and 53 stress that the inference is **between-person**: 535 analysed of 621 (all female twins) and 93 of 118 patients, with the signal predicting group-level transition risk and individual prediction judged unlikely (file 27). Wichers 2016 is the within-person n = 1 test (file 53). This file's phrase "rising autocorrelation ... in individual emotion series predicts transitions" could be read as within-person prediction. **Verdict: files 27, 30 and 53 are right on the design; 070 section 3 should say between-person for van de Leemput.** Does not touch the conclusion about group matrices.
4. **"The n-scaling that file 30's May criterion expresses with random coupling" (section 6) versus file 30 section A3.** May's criterion scales as sigma*sqrt(SC) < d (square root of size), while the deterministic exchangeable case here scales as (n-1)b. File 30's own pure-mutualism case, (S-1)*C*E - d, is the true counterpart of this file's result; May's sqrt scaling is the zero-mean random case. Not a conflict in fact, but the sentence conflates the two. Verdict: file 30 is the more precise; refine the sentence to point at its mean-coupling outlier result.

No numerical contradictions were found in the overlapping figures (32 couples, 7 people, DOIs, volumes and pages). Items 1 and 3 are wording fixes in this file; none changes the headline.
