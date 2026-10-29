# Prior work 070: measured coupling matrices for human groups of three or more

Direction: D317

Date: 2026-10-29. Kind: survey. Question: has anyone estimated a coupling (community / VAR / oscillator) matrix for a human group of n >= 3 and reported its eigenvalues or stability? Seeds: Ferrer & Helm 2013; Helm, Sbarra & Ferrer 2012; van de Leemput 2014; Wichers 2016.

**Method and honesty note.** This file is thin by design because the literature is thin, and the session was constrained. The web-search quota ran out partway through (the tool said so), PMC and the ACM and PNAS PDFs sit behind bot checks (reCAPTCHA / 403 / Cloudflare), and the Frontiers PDF that came back was an unrelated individual-VAR paper (Bulteel et al. 2016, read only to discard it). **No primary full text was read this session for any work below.** Everything is [abs] (abstract, or a search summary of it), [std] (standard textbook content, not checked here) or [derived] (my own algebra from a stated form, not in any source). DOIs were checked on Crossref (Helm 2012, Ferrer & Helm 2013, Moulder 2022) or Europe PMC. Cross-references: 20 (dyadic coupling), 27 (measuring drive dynamics), 30 (ecological stability, the May test), 059 and 060 (influence functions; n-actor extensions).

## Summary

1. **Answer: no.** I found no study that fits a coupling matrix to three or more people and reports its eigenvalues, spectral radius or any stability verdict. The nearest is one conference paper on triads that reports network node strengths, not eigenvalues. "Not found" is not "does not exist" (see Unconfirmed), but file 30's claim that nothing exists at S well above 2 stands, and it stands at S = 3 as well.
2. **Three of the four seeds are not about groups.** Helm, Sbarra & Ferrer 2012 and Ferrer & Helm 2013 are dyads (32 couples). van de Leemput 2014 and Wichers 2016 are individual mood series. The seed list tests the ground just short of the question.
3. **Eigenvalues are never the reported quantity** in the dyadic work either. Estimates are per-parameter (self-regulation, coregulation) compared across tasks and people. The stability read-off (eigenvalues of the 2x2 or 4x4 system) would be [derived] from those parameters, not published.
4. The useful output here is a **derivation**: how the stability of a symmetric n-person coupling matrix depends on n, which the algebra can use before any data exist (section 6).

## 1. Helm, Sbarra & Ferrer (2012): coupled linear oscillators in couples

**Citation.** Helm, J. L., Sbarra, D. & Ferrer, E. (2012). Assessing cross-partner associations in physiological responses via coupled oscillator models. *Emotion* 12(4), 748-762. DOI 10.1037/a0025036 (Crossref: confirmed, title, volume, pages). Not open access in this session.

**Their vocabulary.** Interdependence, cross-partner association, synchrony, coupled linear oscillators (after Boker & Nesselroade 2002).

**Drives/operands.** Respiration and heart rate of each partner; not a named drive.

**Operators / equations.** Coupled linear oscillators, the standard second-order form [std], not read: for partner i, x_i'' = eta_i x_i + zeta_i x_i' + gamma_i x_j (+ gamma' x_j'), i.e. self-term, damping, and a cross term from the partner. Exact parametrisation in the paper not verified.

**Theorems or derived predictions.** None. Hypothesis-testing of non-zero coupling.

**Empirical standing.** [abs] 32 couples (secondary press summary, not checked against the paper), three lab tasks; "associations were detectable within all three tasks, with different patterns of coupling within each task". A control (non-partner pairings) showed no synchrony per press coverage [secondary]. Women adjusting more to partners than men did is from the same press coverage. Single lab, one dyad type (heterosexual couples), no predictive validation. Blunt: shows coupling is detectable above a shuffled baseline; says nothing on stability.

**Translation.** Operand: person-state pair. Operator: the cross term gamma, an off-diagonal entry of the coupling matrix. Gives a 2x2 (in first-order form 4x4) matrix per couple, estimated. Group extension is a larger matrix; nobody has estimated one.

## 2. Ferrer & Helm (2013): dyadic differential equations for coregulation

**Citation.** Ferrer, E. & Helm, J. L. (2013). Dynamical systems modeling of physiological coregulation in dyadic interactions. *International Journal of Psychophysiology* 88(3), 296-308. DOI 10.1016/j.ijpsycho.2012.10.013 (Crossref: 2013, vol 88, pp 296-308; the 2012 elsewhere is the online date).

**Their vocabulary.** Self-regulation, coregulation, dyadic system of differential equations (Felmlee & Greenberg 1999).

**Operators / equations.** [abs] "a system of differential equations developed for dyadic research (Felmlee and Greenberg, 1999)", with "parameters representing self-regulation and coregulation for each individual in the dyad", fitted directly to each dyad, distributions of parameters examined, compared across three tasks, and parameters related to those from a similar model on daily self-reported affect. Equation form not read.

**Empirical standing.** [abs] 32 couples, heart rate and respiration. Per file 20, effects modest and context-dependent. Blunt: parameters estimable per dyad; the link to daily-affect parameters is an association across 32 couples, not a prediction.

**Translation.** As section 1. The per-dyad fit is the template that a triad would need; it is a dyad-only study.

## 3. van de Leemput et al. (2014) and Wichers et al. (2016): the stability-from-data tests, not groups

Already treated in 27 (numbers, failures) and 30 (design). Restated only for the stability link. van de Leemput et al. 2014, *PNAS* 111(1), 87-92, DOI 10.1073/pnas.1312114110 (Europe PMC: found, PMC3890822); Wichers et al. 2016, *Psychother Psychosom* 85, 114-116, DOI 10.1159/000441458.

**What they test.** [abs, via 27 and 30] Rising autocorrelation, variance and cross-emotion correlation in individual emotion series predicts transitions into or out of depression. This is the data-side use of the eigenvalue idea: for x_{t+1} = A x_t + e [std], lag-1 autocorrelation of the slowest mode tends to its eigenvalue, so |lambda_max| -> 1 shows as rising autocorrelation and variance [std; not read in either source this session].

**For this question.** Both are person-level; the "system" is the person's emotion set. The matrix A (a VAR(1) community matrix) is not reported as a matrix. Later work (27: Helmich 2023, 2024) finds the signals weak as prediction. So the only eigenvalue-flavoured human test uses a proxy for the eigenvalue, on individuals, and the proxy is contested. PMC full text of van de Leemput was not retrievable this session (bot check), so no passage is quoted.

## 4. The one group-of-three measurement found: Moulder, Duran & D'Mello (2022)

**Citation.** Moulder, R. G., Duran, N. D. & D'Mello, S. K. (2022). Assessing multimodal dynamics in multi-party collaborative interactions with multi-level vector autoregression. *Proceedings of the 2022 International Conference on Multimodal Interaction (ICMI '22)*. DOI 10.1145/3536221.3556595 (Crossref: confirmed, issued 2022-11-07). Full text returned 403; only the abstract summary was read [abs].

**Their vocabulary.** Multi-level VAR (mlVAR), dynamic network, in-strength, out-strength, synchrony, controller / primary contributor / secondary contributor.

**Drives/operands.** Nine signals per user: positive and negative valence, skin conductance, heart rate, gaze fixation duration, gaze dispersion, head acceleration, facial expressiveness, speech rate. Not drives, but affect, arousal, attention and expression: the layer a drive would sit beneath.

**Operators / equations.** [abs] mlVAR, a lagged regression network; lag order, centring, and whether the network is within-person or across the triad's members not stated in the summary. The network metrics are node in-strength and out-strength (column and row sums of absolute or signed coefficients, definition not read) and "synchrony". No eigenvalue or stability analysis is mentioned in the abstract.

**Theorems or derived predictions.** None. Role classification from node metrics.

**Empirical standing.** [abs] 201 users in 67 triads, 15-minute collaborative task. Roles distinguishable by the metrics; a feedback loop in which skin conductance is driven by gaze and speech. Single task, lab, conference paper, no replication seen; roles are reported as distinguished but the check against an independent role label is not known to me.

**Translation.** This is the only found estimate of a directed influence structure among three people that is, in form, a coupling matrix (here an mlVAR network over many signals). Operand: the (person, signal) pair. Operator: the lagged coefficient. The missing step is exactly the one D317 asks for, computing the spectrum of the estimated matrix and checking it against a stationarity bound. mlVAR requires stationarity as an assumption [std], so the fitted model was presumably stable, but that is not reported in what I read.

## 5. Adjacent but not the answer

- **Alderisio et al. (7 people, Kuramoto network on four graphs).** Read in full in 060. Fitted a single coupling constant per group on a known graph, not a free matrix and not eigenvalues. Closest numerical n >= 3 result with human data, but it estimates one scalar.
- **Group physiological synchrony and cohesion (N = 261, Frontiers in Human Neuroscience 2022, multidimensional recurrence quantification on inter-beat intervals).** [abs, search summary] Compares synchrony before and during group interaction, relating change to reported cohesion. A scalar synchrony index per group; no coupling matrix. Citation details not verified: treat as a lead.
- **Dyadic idiographic ODE fitting** (Psychometrika paper, AICc model selection per couple; independence the most common pattern) [abs, search summary; authors and DOI not verified]. If "independence is most common" holds, the dyadic coupling that exists is often zero per couple, which matters for the stability question.
- **Triadic theoretical extensions** (Bielczyk, Foryś & Płatkowski, arXiv 1202.2338; parental-influence love models). Theory only, no data (see 060).

## 6. What the algebra can do before the data exist [derived]

Not from any source; my calculation, for the linear model dx/dt = A x with n actors, A = a I + b (J - I), J the all-ones matrix (exchangeable actors, diagonal a = self-term, every off-diagonal b = pairwise coupling).

- Eigenvalues: **a + (n-1) b** once (the shared mode, eigenvector all ones), and **a - b** with multiplicity n-1 (the contrast modes, eigenvectors summing to zero).
- Continuous-time stability needs both negative: a + (n-1) b < 0 and a < b. With a < 0, the group-wide mode destabilises when b > -a/(n-1) for b > 0. **The tolerable uniform pairwise reinforcement falls as 1/(n-1)**: with a = -1, b = 0.4 is stable for n = 3 (eigenvalue -0.2), marginal at n = 3.5 and unstable at n = 4 (eigenvalue +0.2). Positive uniform coupling (mutual excitation, contagion) gets less safe with size; negative b (mutual inhibition) destabilises the contrast modes instead when b < a, i.e. when mutual damping exceeds self-damping. Discrete-time (VAR(1)) analogue: |a + (n-1) b| < 1 and |a - b| < 1.
- This is the n-scaling that file 30's May criterion expresses with random coupling; the exchangeable case is the deterministic counterpart and needs no random-matrix result. It is a prediction, not a measurement.
- For a dyad (n = 2) the same form gives eigenvalues a + b and a - b: the in-phase and anti-phase modes. This is what a fitted couple's 2x2 matrix would be read through, and nobody reports it.

## What exists vs what does not

**Exists.** Estimable per-dyad coupling parameters in physiology and daily affect (1, 2). Individual-level critical-slowing proxies for the eigenvalue (3), weak as prediction (27). One n = 3 mlVAR network of mixed signals with node-level metrics (4). A seven-person Kuramoto fit with a scalar coupling (060).

**Does not exist (as far as I found).** An estimated n >= 3 coupling matrix for a named affect or drive with its eigenvalues reported. Any stability verdict on a measured human group matrix. Any replication of a group-level matrix. Any test of the A = aI + b(J-I) scaling above. Group data with enough time points per member: a 15-minute triad session yields few observations per cell for a 3x3 or 27x27 matrix, so this may be a data-volume problem as much as a literature gap [inference, not checked].

## Unconfirmed

- Moulder 2022: everything beyond the abstract (lag, definition of strength, whether any eigenvalue or stationarity check is reported, effect sizes). The most likely single place to find a group matrix; read it first.
- Helm 2012 and Ferrer & Helm 2013: parameter equations and estimates (only abstracts and press summaries seen). The 32-couple figure and the sex difference come from press coverage / search summaries.
- The exact oscillator parametrisation in section 1 is [std].
- The 2022 Frontiers synchrony-cohesion paper and the Psychometrika idiographic dyad paper: located only through search summaries; no DOI checked.
- van de Leemput 2014 and Wichers 2016 were not re-read; they rest on 27 and 30.
- Unsearched (quota ran out): multilevel VAR for families (Sels, Kuppens and colleagues' interpersonal emotion dynamics work), team physiological synchrony (Gordon et al.), dynamic structural equation models for triads, social relations model with time. A follow-up search should target these and "three or more" family and team EMA with VAR.
