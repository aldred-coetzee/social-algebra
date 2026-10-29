# Prior work 94: circularity and identifiability, testing a model on simulated data without baking the answer in

Direction: D551

Date: 2026-10-29. Kind: cross-check. Question: what do simulation-based calibration (SBC), parameter recovery and model recovery actually certify, and what do they not, when the algebra's drive equations will be tested on data simulated from the algebra itself? Seeds: Talts et al. 2018 (SBC); Wilson & Collins 2019. Cross-references: 79 (identifiability and power of drive equations), 81 (minimal sim), 27 (measuring drive dynamics), 87 (cohesion measurement lags).

**Method and honesty note.** Downloaded as PDF and text-extracted, so read by me and not through a summarising model:
- Talts, Betancourt, Simpson, Vehtari & Gelman, arXiv:1804.06788v2 (21 Oct 2020). Read in full, body Sections 1-7. **Not read:** the appendices (code listings, the proof of Theorem 1 in Appendix B).
- Wilson & Collins, eLife 2019;8:e49547, DOI 10.7554/eLife.49547 (Crossref confirmed: title, authors, 26 Nov 2019). Read in full, main text and Boxes 1-7. **Not read:** Appendices 1-4.
- Modrák et al., arXiv:2211.02383v3 (19 Oct 2023); published as *Bayesian Analysis* 20(2):461-488 (2025), DOI 10.1214/23-BA1404 (Crossref confirmed 2026-10-30; the arXiv v3 text is what was read). Read the abstract, Sections 1-2 and the theory of data-dependent test quantities (3.3, 3.4), and Sections 6.1-6.3. **Not read:** the case studies (4, 5), the proofs, and parts of Sections 2 and 3.
- Gelman et al., "Bayesian workflow", arXiv:2011.01808v1. Read Sections 4.1-4.3 only. The other sections were not read.

**Not read, so any claim about them is [sa]:** Cook, Gelman & Rubin 2006 (Crossref confirms 10.1198/106186006X136976, *J. Comput. Graph. Stat.* 15, 675-692); Palminteri, Wyart & Koechlin 2017 (the TICS falsification paper, "The importance of falsification in computational cognitive modeling"; Crossref confirms 10.1016/j.tics.2017.03.011, TICS 21, 425-433, but HAL refused the fetch); Säilynoja et al. (downloaded, only the abstract inspected); Schad et al. on principled workflow; Grimm et al. on pattern-oriented modelling; and the simulation-based-inference literature (Cranmer et al.; Hermans et al.). I did not locate a published-journal version of Talts et al.; I cite the arXiv version, and Modrák et al. cite it as "Talts et al. 2020", which matches v2. No DOI was verified for it, so none is given.

None of these sources concerns social groups or drives. **Everything below about the algebra is my application, tagged [derived]. Nothing here is an empirical result about people, so there is no scale of result (membership, group or crowd) to report, and no intervention, consensual or manipulative.**

---

## 1. Talts et al. (arXiv 1804.06788v2): simulation-based calibration

**Citation.** Talts, S., Betancourt, M., Simpson, D., Vehtari, A., Gelman, A. Validating Bayesian inference algorithms with simulation-based calibration. arXiv:1804.06788 (v2, 2020).

**Their vocabulary.** Joint distribution pi(y, theta) = pi(y | theta) pi(theta); ground truth (theta-tilde); data-averaged posterior; rank statistic; calibration; thinning; effective sample size.

**Drives/operands.** None. A procedure for checking a Bayesian computation.

**What SBC is [read].**
- Procedure: draw theta-tilde ~ pi(theta); draw y-tilde ~ pi(y | theta-tilde); draw L posterior samples {theta_1..theta_L} ~ pi(theta | y-tilde); compute the rank r = sum_l I[f(theta_l) < f(theta-tilde)] in [0, L] for a chosen one-dimensional f. Repeat N times and test whether the ranks are uniform on {0..L}.
- **Theorem 1 [read statement, proof not read]:** for exact posterior draws, "The rank statistic of any one-dimensional random variable over theta is uniformly distributed over the integers [0, L]." The motivating identity is Eq. (1): integrating the exact posterior over the joint returns the prior.
- Practicalities [read]: a 99% band from the 0.005 and 0.995 quantiles of Binomial(N, 1/(L+1)); keep N/B near 20 when binning; thin MCMC output by ceil(N/N_eff) (their Algorithm 2) because autocorrelation produces spikes at the extreme ranks; the ECDF-difference plot for small deviations.
- Diagnostic shapes [read]: a "cap" histogram means the computed posterior is overdispersed; a "U" means underdispersed; a skew means bias in the opposite direction.
- Experiments [read]: L = 100 posterior draws throughout; N = 10,000 for the first three, N = 1000 for INLA. A deliberately wrong prior on beta (fitted N(0,1), generated N(0,10^2)) gives a U shape. The centred eight-schools model under HMC is biased in tau: the Figure 10 caption says "towards larger values of τ than were used to generate the data", while the Section 6.2 prose says the samples "are biased below the prior samples"; the paper is internally inconsistent on the direction, and only the existence of the bias should be relied on. ADVI strongly biased on a simple linear regression. INLA slightly biased on Kenyan HIV prevalence mapping (N = 1000, ECDF deviation at low ranks).

**The central cross-check: what the paper itself says SBC does not do [read].**
- The paper says outright that "this calibration is limited exclusively to the computational aspect of our analysis. It offers no guarantee that the posterior will cover the ground truth for any single observation or that the model will be rich enough to capture the truth at all." Model validity against reality is assigned to posterior predictive checks.
- SBC "requires just one assumption: that we have a generative model for our data." That is the circularity in one line. The generator and the fitted model are the same object by construction, so a pass says the code and sampler agree with the model, and says nothing about whether the model resembles the world.
- A single ground-truth recovery is flawed (Section 2, worked example): with y ~ N(mu, 1), mu ~ N(0, 1), true mu = 0 and an extreme y = 2.1, the correct posterior N(1.05, 0.5^2) puts the truth more than two SDs out, while a wrongly coded variance-10 version gives N(1.05, 5^2) and "recovers" it. So one recovery run can fail the correct code and pass the broken code.
- Stated limits [read]: viewing histograms is hard with many parameters; chi-squared tests "did not perform particularly well"; only one-dimensional summaries are checked; the cost is N full fits.

**Cross-check against the later literature.** Modrák et al. (section 4 below) show that the commonly believed limit (SBC cannot detect a program that returns the prior and ignores the data) is true only when the test quantity depends on the parameters alone. Talts et al. do not state that belief themselves in the sections I read; the belief is attributed in Modrák et al. to other papers. **Where they differ, Modrák et al. is right and it extends Talts.**

**Small errata noticed in the text [read]:** the Section 6.2 prose refers to Figure 11b for the centred-model bias where the figure for that result is Figure 10. Section 4.2 describes the autocorrelation signature as spikes at the boundaries, while Section 5.1 calls it the U shape (the same appearance, different words). Neither affects the method.

**Empirical standing.** It is a methods paper whose "evidence" is a handful of designed failures in standard statistical models, all of which it correctly flags. It has not been run on any behavioural or social model in the text I read.

**Group size / composition.** The only place anything like group count enters is the eight-schools example (J = 8 groups). There the paper finds the centred parameterisation funnels and biases tau. [derived] This is the relevant warning for the algebra: a hierarchical model with few groups per population, or few members per group, gives exactly the geometry where the sampler, rather than the model, fails, and SBC is how to see it.

---

## 2. Wilson & Collins (eLife 2019): ten simple rules

**Citation.** Wilson, R. C., & Collins, A. G. E. (2019). Ten simple rules for the computational modeling of behavioral data. *eLife* 8:e49547. DOI 10.7554/eLife.49547.

**Their vocabulary.** Simulate; model-independent measures; parameter recovery; model recovery; confusion matrix; inversion matrix; model validation; latent variable.

**Drives/operands.** The worked example is a two-armed bandit (T = 1000, reward probabilities 0.2 and 0.8) with five models: random responding, noisy win-stay-lose-shift, Rescorla-Wagner (learning rate alpha, inverse temperature beta), choice kernel, and Rescorla-Wagner plus choice kernel. No drives as such. Reward-seeking appears only as a learning rule.

**The workflow [read].** Design the experiment and the models together; simulate; check parameter recovery; check model recovery; fit real data; validate the winning model by simulating it with its fitted parameters; only then analyse latent variables; report everything.

**Equations as printed [read]** (symbols given in plain text):
- Rescorla-Wagner (Eq. 3): Q_{t+1}^k = Q_t^k + alpha (r_t - Q_t^k).
- Softmax (Eq. 4): p_t^k = exp(beta Q_t^k) / sum_i exp(beta Q_t^i).
- Choice kernel (Eq. 5): CK_{t+1}^k = CK_t^k + alpha_c (a_t^k - CK_t^k).
- BIC (Eq. 10): BIC = -2 log LL-hat + k_m log(T).
- Side bias (Eq. 11): p_t^left = 1 / (1 + exp(beta (Q^right - Q^left - B))).
- Log-likelihood (Eq. 8): LL = sum_t log p(c_t | d_{1:t-1}, s_t, theta_m, m).

**What they claim and what supports it [read].**
- Simulate with model-independent measures first. "Distinguishing between models on the basis of qualitative patterns in the data is always preferable to quantitative model comparison." Also: "computational modeling is rarely informative when there is no evidence of an effect in model-independent analyses of behavior." This is the direct answer to circularity: choose signatures that can be computed on data without fitting the model.
- Parameter recovery (Box 4): alpha ~ U(0,1), beta ~ Exp(10), T = 1000, 1000 repetitions, maximum-likelihood fit. Recovery is good overall, and best for 1 < beta < 10. Recovery of alpha is worse when beta is outside that range. They advise matching the simulated parameter range to the range obtained from real fits, or from prior literature.
- Parameter trade-off: look at correlations between recovered parameters; if the simulated ones were uncorrelated and the recovered ones are correlated, the parameters trade off, which "can sometimes be avoided by reparameterizing the model or redesigning the experiment". Where unavoidable, report it.
- Modelling a nuisance parameter improves recovery of the important ones (Box 6): adding a side bias B to the fit greatly improved recovery of alpha and beta (10 independent bandits in 50-trial blocks).
- Model recovery (Box 5): the confusion matrix p(fit model | simulated model). With beta priors Exp(1) the diagonal for models 3, 4, 5 was only 0.54, 0.54, 0.30; raising all softmax parameters by 1 (less noise) lifted it to 0.94, 0.93, 0.72. Their conclusion: "Models that are identifiable in one parameter regime may be impossible to distinguish in another!" They also define the inversion matrix p(simulated model | fit model) by Bayes rule, which is the quantity relevant when interpreting a fit to real data (Box 5 panel C, with a uniform prior over models, 0.54 for model 1 against 0.84 in panel D).
- Validation (Rule 9 and Box 7): a model that fits better by likelihood can fail to reproduce the effect when simulated with its fitted parameters. In the Palminteri et al. example, recounted in the Rule 9 main text (not in Box 7), data from an RL agent on a reversal task are fitted better by a choice-kernel model than by win-stay-lose-shift, but the choice-kernel model, being insensitive to reward, cannot reverse when simulated. In Box 7 the state-based RL model has higher likelihood on blind-agent data than on its own data, because of differing noise. Their lesson: "measures of model-fit and model comparison cannot replace a thorough validation step, which can contradict them."
- Power for group differences can be obtained by simulating and recovering for a proposed effect size.

**The honest limits as the authors state them [read].** "Even successful parameter recovery represents a best-case scenario" and "the elephant in the room with all model comparison is that it only tells you which of the models you considered fits the data best." And on validation, "exactly what it means for a model to 'fail' the validation step is not well defined… there is no rule of thumb."

**Erratum, text as printed [read].** The power paragraph says power is "the frequency with which the statistical tests detect no effect given that the effect is there." That is reversed; power is the frequency with which they detect the effect. The sense is obvious from context, and the mistake does not touch the method.

**Empirical standing.** An advice article, not a tested procedure. The numbers in the boxes come from the authors' own simulations on a toy task. I found no meta-analysis testing whether following the rules improves replication, and I did not search for one beyond these texts.

**Group size / composition.** None. The only size variable is trials T per subject, held at 1000 in the examples (the side-bias demonstration uses 50-trial blocks). The paper does not vary T, so it gives no rule for how recovery degrades as data shrink; file 79 derives that for the drive setting.

---

## 3. Gelman et al., Bayesian workflow (Sections 4.1-4.3 only)

**Citation.** Gelman, A., Vehtari, A., Simpson, D., Margossian, C. C., Carpenter, B., Yao, Y., Kennedy, L., Gabry, J., Bürkner, P.-C., Modrák, M. (2020). Bayesian workflow. arXiv:2011.01808.

**Claims relevant here [read].**
- Fake-data simulation is "arguably, the only point where we can directly check that our inference on latent variables is reliable." For a drive model the drive levels are exactly the latent variables, so this is where the check has to happen.
- A model that recovers well from fake data generated by itself has shown nothing about real data, but one that cannot recover even then is hopeless; in the authors' words, "Fake-data simulations provide an upper bound of what can be learned about a latent process." The same point as Wilson & Collins' best-case remark.
- Recovery of a single truth point is unreliable; SBC and single-point benchmarking "are two ends of a spectrum".
- Parameter-space dependence: the example of a sum of declining exponentials is informative when the exponents are well separated and "not so informative when the two components are close". They note the same instability in differential-equation models, which is the form drive equations take. They suggest fitting real data first, then drawing parameters from that posterior for the fake-data checks, while admitting "the statistical properties of such a procedure are unclear."
- A practical conflict: wide, weakly informative priors make SBC generate extreme data sets (their example is air-pollution data "denser than a black hole"). The suggestion is to estimate parameters from real data and widen slightly for the SBC prior.
- Deliberate misspecification (Section 4.3): fit a normal-error regression to data generated with t4 errors. "This will then fail simulation-based calibration… but the interesting question here is, how bad will these inferences be?" This is the closest thing in these texts to a model-independent generator: the generator is a different model from the fitted one, and the question measured is the size of the damage.

---

## 4. Modrák et al. (arXiv 2211.02383v3): the choice of test quantities

**Citation.** Modrák, M., Moon, A. H., Kim, S., Bürkner, P., Huurre, N., Faltejsková, K., Gelman, A., Vehtari, A. (2023). Simulation-based calibration checking for Bayesian computation: the choice of test quantities shapes sensitivity. arXiv:2211.02383 (v3).

**Claims relevant here [read].**
- The older belief that SBC cannot detect a probabilistic program that "samples from the prior distribution and ignores the information in the data" holds only for test quantities depending on the parameters alone. Theorem 7 (read statement), "Incomplete use of data", is more general: a program that uses the data only through a function t(y) passes SBC against every test quantity that sees the data only through t(y); taking t constant gives the prior-returning program passing against every parameter-only quantity.
- With data-dependent test quantities SBC becomes complete: Theorem 6 (read statement) gives the density-ratio quantity g = pi_post(theta | y) / phi(theta | y), which passes if and only if the implemented posterior equals the true one up to a set of measure zero. It is not usable in practice, as it needs the true posterior, but it motivates the practical default.
- Practical recommendation (Section 6.1): monitor each model parameter and the joint likelihood of the data, plus a few tailored quantities. In their simulations the joint likelihood detected every discrepancy, often with the fewest simulations, though quantities more sensitive for specific problems exist.
- Limits (Section 6.2): a finite set of test quantities cannot rule out every incorrect posterior; more quantities raise multiple-testing risk; precision problems (a nearly correct posterior) need more simulations, with the best sensitivity at the same order of magnitude of simulated datasets as of posterior draws.
- They restate that SBC "has no way to inform us about a discrepancy between the process that generated real data and the assumptions of our statistical model", and that it needs to be combined with posterior predictive checks and residual analysis.
- They also show that SBC and the data-averaged-posterior check are different checks that the literature repeatedly conflated.

**Cross-check verdict.** The claim "SBC detects everything the model can get wrong" is wrong for the original Talts form (parameter-only quantities) and right in principle for the Modrák form, but in both forms the object checked is the agreement between a generator and a program written from the same model. Neither tells you the model is right about people.

---

## 5. What the circularity actually is, and what does and does not break it [derived]

Three distinct things get called "testing on simulated data", and they certify different things.

1. **Computation check (SBC, Talts/Modrák).** Generator = fitted model. Certifies code and sampler. Cannot fail because the model is wrong about people. Mandatory, cheap in comparison with what it protects, and would have caught bugs in any fitting code written for file 79's relaxation-rate and coupling fits.
2. **Identifiability check (parameter recovery, Wilson & Collins; fake-data, Gelman).** Generator = fitted model, but the question is whether the **experiment and sampling design** can pin the parameters down. Certifies a best case. This is what file 79's results are about, and the reasoning is the same: the answer depends on the region of parameter space (beta outside 1-10 in the bandit; close exponents in Gelman's example).
3. **Discrimination and validation (model recovery, qualitative signatures, simulate-with-fit parameters).** Generators = several rival models; the question is whether the data can tell them apart and whether the winner reproduces effects it was not fitted to. This is the only one of the three that bites on the circularity, because the rival models are not the fitted model.

**What breaks circularity, as far as these texts go:**
- **Rival generators**, including ones that are not drive models (random responding, win-stay-lose-shift and choice-kernel models in Wilson & Collins are non-RL rivals to RL). The confusion matrix and its inversion are the instruments. [derived] The algebra's rivals should be: a no-drive baseline (influence or imitation only, as in 63 and 74), a pure-network-structure model, and a different-timescale drive model.
- **Model-independent measures** computed identically on simulated and real data, chosen **before** fitting. [derived] For drives these must be observable: event counts, thresholds crossed, time-to-return, cross-correlation lags (cf. 27, 87).
- **Posterior-predictive validation on held-out effects**, which is how Palminteri's example is caught.
- **Deliberate misspecification** (Gelman's t4 case): generate from a rival, fit the algebra, measure the damage in the quantity of interest.
- **Parameter ranges taken from real fits** and not from the model's own preferred region (Wilson & Collins; Gelman). This guards against grading the model on easy cases.

**What does not break it:** any amount of recovery on data from the algebra itself, and any SBC pass. The wording for the repo: *a pass certifies the arithmetic, not the theory.*

**Group-size and composition notes [derived; no source varies n].** The sources say nothing about n. The structural implication is only that recoverability depends on the amount of data per parameter and on hierarchy: the eight-schools funnel (J = 8 groups) is the textbook case where the sampler fails when there are few groups. For the algebra, per-group parameters with small n and few groups should be expected to sit in the regime where SBC shows bias and recovery degrades. This is a hypothesis to run, not a result.

**A protocol for the algebra, as a specification only (no code) [derived from the sources above].**
1. Fix the generator (the algebra's equations plus an observation model with measurement noise at the level file 27 says is realistic).
2. Run SBC with parameter-based quantities and the joint likelihood (Modrák), L near 100 effective draws, N in the thousands; thin by effective sample size.
3. Run parameter recovery across ranges taken from real data fits (once files 78 and 80 supply them), plot simulated against recovered, and report correlations between recovered parameters.
4. Run model recovery against the rivals above, report both the confusion and the inversion matrices, across several noise regimes.
5. Validate by simulating with fitted parameters and checking effects not used in the fit.
6. Report all of it, including failures (Wilson & Collins's reporting rules).

---

## What exists vs what does not

**Exists:** SBC with a theorem and a working R implementation (Modrák et al. cite the SBC R package); a clear parameter-recovery and model-recovery recipe with worked toy numbers; a plain statement from each source that recovery is a best-case check.

**Does not exist (in what I read):** any guidance on how much data (here, how many members, groups or time points) is needed for recovery; any application of SBC or model recovery to social, group or drive models in these four texts. **Corrected on validation:** outside them, parameter-estimation and identifiability work on social models does exist, e.g. Borile, Lenti, Ghidini, Monti & De Francisci Morales, "Bias and identifiability in the bounded confidence model", arXiv:2506.11751 (2025), reporting a small-sample bias in the confidence-bound MLE, a persistent bias in the convergence-rate MLE and joint-identifiability problems in some regions; and Lenti, Silvestri & De Francisci Morales, "Variational inference of parameters in opinion dynamics models", arXiv:2403.05358 (2024). Abstracts only, [sa]. No SBC (rank-based) application to a social model turned up in one search; any rule for "good enough" validation (the authors say there is none); any method that certifies a model against reality rather than against itself.

## Unconfirmed

- Palminteri et al. 2017 (the falsification and "simulation-with-fit-parameters" argument): only seen as quoted by Wilson & Collins. Mark [sa]; do not feed any claim from it into an equation.
- Cook, Gelman & Rubin 2006: described only as summarised in Talts et al.
- Whether the Talts et al. paper has a peer-reviewed version. arXiv lists no journal reference, and one search on 2026-10-30 found only the preprint.
- The Modrák et al. case studies (Sections 4-5) and proofs.
- Appendices of Talts et al. and Wilson & Collins.
- Pattern-oriented modelling from agent-based ecology, and simulation-based inference for models with intractable likelihoods: not searched. These are the more natural fit for an algebra whose agents interact, and are the gap to fill next.

## Does it reduce to a drive basis?

This tradition has no drives of its own, so nothing "reduces" in the sense of the question. What it contains, and where it sits relative to a drive basis:
- **Reduces to (or presupposes) a drive model:** nothing. The methods take any generative model. Rescorla-Wagner "learning" and softmax "noise" are the only psychological content, and neither is a drive.
- **Does not reduce, and does not need to:** the tradition is about the relation between a model and its data. It is a test layer. It neither supports nor undermines "drives as primitives"; it can only report whether a drive model is recoverable and distinguishable from rivals.
- **What it says about the working hypothesis:** if drive equations pass parameter and model recovery against non-drive rivals on real data, that is evidence that drives are doing work the rivals cannot; if they pass only against themselves, nothing has been shown. The hypothesis remains untested by this tradition, which only supplies the test.

## What does it predict or control, and how well?

- **Predicts:** nothing about behaviour. It predicts properties of an inference procedure, namely uniform ranks under a correct pairing of generator and sampler (Theorem 1), and, from Modrák et al., that a prior-returning program is detectable with a data-dependent test quantity.
- **Out-of-sample evidence:** for the procedure, a few designed failures, all caught (wrong prior; centred eight-schools; ADVI; INLA, flagged as slightly biased on Kenyan HIV data). For the recipe, toy bandit numbers (e.g. 0.54 versus 0.94 diagonal entries as softmax noise falls). No replication study of the workflow, and no application to people or groups.
- **Effect sizes:** none in the usual sense; the quantities are recovery correlations and confusion-matrix entries, which in the toy example swing from poor to good by changing a noise parameter alone.
- **Failures, as the authors admit:** parameter-only SBC misses data-ignoring programs; a finite set of test quantities cannot cover every error; no model-validity guarantee; no cut-off for a failed validation; "It is an open research question to understand SBC with a small number of draws" (Gelman et al., Section 4.2).
- **Control:** none, and no consent or manipulation question arises.

## Validation log (2026-10-30)

- ✓ Talts, Betancourt, Simpson, Vehtari & Gelman, arXiv:1804.06788v2 (v1 18 Apr 2018, v2 21 Oct 2020; no DOI, no journal reference on arXiv). Full text fetched and read: the procedure, Theorem 1 (appendix statement too), the 0.005/0.995 Binomial band, N/B ≈ 20, ⌈N/N_eff⌉ thinning (Algorithm 2), ∩/∪/skew shapes, the N(1.05, 0.5²) vs N(1.05, 5²) example, "requires just one assumption", "limited exclusively to the computational aspect", PPCs for model validity, the experiments (L, N, priors, ADVI, INLA/Kenya) and the χ² remark all match. The Figure 11b/10 erratum and the "spikes"/"∪ shape" wording are confirmed. ✎ Added the paper's internal inconsistency on the direction of the eight-schools tau bias.
- ✓ Wilson & Collins 2019, eLife 8:e49547, DOI 10.7554/eLife.49547 (Crossref: title, authors, 26 Nov 2019). Full PDF read: Eqs. 3, 4, 5, 8, 10, 11, Box 4 (α ~ U(0,1), β ~ Exp(10), T = 1000, 1000 repeats, 1 < β < 10), Box 5 (Exp(1) priors, diagonals 0.54/0.54/0.30 → 0.94/0.93/0.72, inversion 0.54 vs 0.84), Box 6 (10 bandits, 50-trial blocks), Box 7, all quotes, and the reversed power sentence ("detect no effect") are as stated. ✎ The Palminteri example sits in the Rule 9 text, not in Box 7; clarified.
- ✎ Modrák, Moon, Kim, Bürkner, Huurre, Faltejsková, Gelman & Vehtari: added the published version, *Bayesian Analysis* 20(2):461-488 (2025), DOI 10.1214/23-BA1404 (Crossref confirmed; arXiv lists it). v3 text read: Theorems 6 and 7, Section 6.1 (parameters plus joint likelihood), 6.2 limits, 6.3 conflation, the "no way to inform us" sentence, the SBC R package (Kim et al.), and the attribution of the old belief to other papers (Lee et al., Lueckmann et al., Schad et al., Zhao et al., Ramesh et al., Cockayne et al.; not Talts) all confirmed. ✎ Theorem 7 restated in its general form.
- ✓ Gelman et al. 2020, "Bayesian workflow", arXiv:2011.01808v1 (authors as listed, confirmed on the PDF). Sections 4.1-4.3 read; all quotes (latent variables, "upper bound", "two ends of a spectrum", declining exponentials and ODEs, "statistical properties of such a procedure are unclear", black hole, widen-from-real-data prior, t4) confirmed. ✎ The "few-simulation SBC" line replaced by the exact wording ("small number of draws").
- ✎ Palminteri, Wyart & Koechlin 2017, TICS 21:425-433, DOI 10.1016/j.tics.2017.03.011: authors added (Crossref). Not read; stays [sa].
- ✎ Cook, Gelman & Rubin 2006, JCGS 15:675-692, DOI 10.1198/106186006X136976: existence confirmed via Crossref. Not read; stays [sa].
- ? Säilynoja et al.; Schad et al.; Grimm et al.; Cranmer et al.; Hermans et al.: named without a specific citation and used for nothing; not checked.
- ✎ Added on validation, testing the "does not exist" claim: Borile et al. 2025 (arXiv:2506.11751) and Lenti et al. 2024 (arXiv:2403.05358), authors and titles from arXiv metadata, abstracts only, [sa].

Sources opened: 6 primary texts (four full texts: Talts, Wilson & Collins, Modrák, Gelman; two arXiv abstracts), plus four Crossref records and one search.

Verdict: The file is accurate. Every quotation and number checked against the four texts it claims to have read is correct, and its own errata on Talts and Wilson & Collins are real. The corrections are additions and nuances: the published DOI for Modrák et al., the general form of their Theorem 7, an inconsistency inside Talts on the direction of the tau bias, and the fact that parameter-identifiability work on social (opinion-dynamics) models does exist outside these texts. No fabrications. The equations quoted from Wilson & Collins are [read]; nothing from Palminteri or Cook should feed an equation.

## Cross-checks (2026-10-30)

Checked against the other prior-work files and `docs/ledger.jsonl` (2,770 lines) by grep on the works, authors, equations and numbers named here. Method and provenance tags as in the body above; no source was re-read for this section.

**Works not present elsewhere.** Talts et al., Wilson & Collins, Modrák et al., Gelman et al. ("Bayesian workflow"), Palminteri et al., Cook/Gelman/Rubin 2006, Borile et al. and Lenti et al. appear in no other prior-work file and in no ledger line. Each new ledger line below is therefore not a duplicate of an existing claim, with the exceptions marked.

**Agreements with other files.**
- Recovery depends on the region of parameter space, not only on the model: this file (Wilson & Collins Box 4, beta outside 1-10) agrees with 061 (Hu et al. 2014: estimation accurate only inside narrow ranges of gamma_x and gamma_xdot, and "breaks down" when eta_x = eta_y) and with 079 Section 5.4 (principal-log aliasing for complex eigenvalues, [my simulation]).
- Identifiability of a coupling from self-regulation needs unequal rates: 061 Hu et al. ("estimable only when the partners' own tempos differ") agrees with this file's trade-off reading of Wilson & Collins.
- Parameter-correlation caveat: 053 (Huys et al. 2008: gamma and beta correlated in simulation, so a second task was added) agrees in kind with Wilson & Collins' parameter trade-off advice. Both are stated by their own sources; no conflict.
- Measurement error biases the restoring rate: 079 Section 5.3 [my simulation] and 078 Section 6 both say measurement error pulls a fitted decay or AR coefficient toward or away from truth in the direction the algebra's identifiability section needs. 078 says naive phi is biased toward zero, so k is overestimated; 079 5.3 reports theta_hat above the truth. These are consistent (the two files describe the same attenuation and its effect on k, from opposite sides of the transform); no conflict, but the wording should be checked before v0 cites either.
- Softmax form: Wilson & Collins Eq. 4 is the same formula as 053 Eqs. 3-4 (Huys et al. 2008) and 034 (softmax link, beta as inverse temperature). The formula is identical; the source differs. Marked as duplicate of the formula in 053 (see lines below), not of the work.
- Rescorla-Wagner: Wilson & Collins Eq. 3, Q + alpha(r - Q), is algebraically the same update as 053 Eq. 5, (1 - eps) Q + eps r, with eps = alpha. Same claim in different notation. Marked duplicate of 053 Eq. 5.

**Dependency gap (not a contradiction between sources).** Section 5 protocol step 1 says the generator's measurement noise should be "at the level file 27 says is realistic". File 27 gives no single noise level. It gives within-person reliability as a qualitative range, momentary motive reliability "about .3 to .7", and marks a .6-.8 benchmark for momentary affect as "recalled, not found" (27, Unconfirmed). File 079 Section 5 sets measurement error from a scale's within-person reliability instead. The protocol should name that number and its source before any simulation, per the scope guard in `docs/ledger.md`. Recorded as a note on the protocol, not as a ledger contradiction.

**Internal inconsistency inside Talts et al. (note, not a contradiction).** The file already records this: the Figure 10 caption and the Section 6.2 prose give opposite directions for the eight-schools tau bias. A caveat about one source's own text is a note under the ledger rules, so it stays a note on the empirical line below, and the file's advice to rely only on the bias existing stands.

**Contradictions between sources.** None found in the prior-work files on these works. No cross-file contradiction is open. The only conflicts are inside one source (Talts, above; the file's own errata on Wilson & Collins Box 7 and the power sentence), and these are notes.

**Drives named.** None of the four read sources names a drive; Talts and Wilson & Collins say "Drives/operands: none" and the Wilson & Collins reward-seeking is a learning rule only. Section 5 names the algebra's rivals (no-drive baseline, pure-network, different-timescale drive) as [derived], not as drives from a source. No ledger line of kind `drive` is created from this file.

**Ledger lines (proposed, for `docs/batches/` or the ledger, not written here).** Scale is `n/a` for every line: these are results about an inference procedure and simulated models, with no social outcome, so no consent or manipulation question arises.

| kind | statement | source | work | provenance | dup of |
|---|---|---|---|---|---|
| definition | SBC rank statistic r = sum_l I[f(theta_l) < f(theta~)] for chosen one-dimensional f; uniform on {0..L} under correct posterior | 094 §1 | Talts et al., arXiv:1804.06788v2 | read (body §1-7; appendices not read) | none |
| equation | Theorem 1: the rank statistic of any one-dimensional function of theta is uniform on the integers [0, L] for exact posterior draws | 094 §1 | Talts et al., arXiv:1804.06788v2 | read (statement; proof in App. B not read) | none |
| empirical-result | SBC designed failures caught: wrong prior on beta gives a U shape; ADVI strongly biased on linear regression; INLA slightly biased on Kenyan HIV mapping (N=1000) | 094 §1 | Talts et al., arXiv:1804.06788v2 | read | none |
| empirical-result | Centred eight-schools (J=8) under HMC is biased in tau; direction is stated inconsistently in the paper (Fig. 10 caption vs Section 6.2 prose) | 094 §1 | Talts et al., arXiv:1804.06788v2 | read | none |
| definition | SBC validates computation only, "no guarantee that the posterior will cover the ground truth for any single observation or that the model will be rich enough"; model validity assigned to posterior predictive checks | 094 §1 | Talts et al., arXiv:1804.06788v2 | read | none |
| empirical-result | Single-truth recovery can pass broken code: correct posterior N(1.05, 0.5^2) vs wrong variance-10 version N(1.05, 5^2) both checked against truth with y=2.1 | 094 §1 | Talts et al., arXiv:1804.06788v2 | read | none |
| equation | Parameter recovery (Box 4): alpha ~ U(0,1), beta ~ Exp(10), T=1000, 1000 repeats, ML fit; recovery good overall, best for 1<beta<10, worse for alpha outside | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read (main text and Boxes 1-7; Appendices 1-4 not read) | none |
| equation | Rescorla-Wagner: Q_{t+1}^k = Q_t^k + alpha (r_t - Q_t^k) | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | 053 Eq. 5 (same update, eps = alpha; Huys et al. 2008) |
| equation | Softmax: p_t^k = exp(beta Q_t^k) / sum_i exp(beta Q_t^i) | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | 053 §2 eqs. 3-4 (same formula; Huys et al. 2008) |
| equation | Choice kernel: CK_{t+1}^k = CK_t^k + alpha_c (a_t^k - CK_t^k) | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none |
| equation | Log-likelihood: LL = sum_t log p(c_t given d_{1:t-1}, s_t, theta_m, m) | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none; ML form close to 053 §2 eqs. 3-4 |
| equation | BIC = -2 log LL-hat + k_m log(T) | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none |
| equation | Side bias: p_t^left = 1 / (1 + exp(beta (Q^right - Q^left - B))) | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none |
| empirical-result | Model recovery (Box 5): diagonal of confusion matrix for models 3, 4, 5 is 0.54, 0.54, 0.30 with Exp(1) priors on beta, rising to 0.94, 0.93, 0.72 when softmax parameters are raised by 1 | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none |
| empirical-result | Inversion matrix (Box 5C/D): p(model 1 simulated | fit) 0.54 under the uniform prior against 0.84 in the other panel | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none |
| empirical-result | Modelling a side bias B greatly improved recovery of alpha and beta (10 bandits, 50-trial blocks) | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none |
| empirical-result | Validation (Rule 9): choice-kernel model fits an RL reversal-task agent's data better than win-stay-lose-shift but cannot reverse when simulated with its fitted parameters | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 (reporting Palminteri et al.) | read in Wilson & Collins; Palminteri not read (sa) | none |
| definition | Test quantity: SBC with parameter-only quantities cannot detect a program that samples the prior and ignores the data; a quantity depending on data can | 094 §4 | Modrák et al., arXiv:2211.02383v3 (Bayesian Analysis 20(2) 2025) | read (Sections 1-2, 3.3-3.4, 6.1-6.3; case studies and proofs not read) | none |
| equation | Theorem 6: density-ratio test quantity g = pi_post(theta given y) / phi(theta given y); passes iff the implemented posterior equals the true one up to measure zero | 094 §4 | Modrák et al., arXiv:2211.02383v3 | read (statement; proof not read) | none |
| equation | Theorem 7 (general form): a program that uses data only through t(y) passes SBC against every test quantity seeing data only through t(y) | 094 §4 | Modrák et al., arXiv:2211.02383v3 | read (statement; proof not read) | none |
| empirical-result | Joint likelihood of the data, plus each parameter, detected every discrepancy in their simulations, often with fewest simulations | 094 §4 | Modrák et al., arXiv:2211.02383v3 | read (their simulations; no social application) | none |
| definition | Deliberate misspecification (fit normal-error regression to t4-error data): the question is how bad the inference is, not whether SBC passes | 094 §3 | Gelman et al., "Bayesian workflow", arXiv:2011.01808v1 | read (Sections 4.1-4.3 only) | none |
| definition | Fake-data simulation is the only point where inference on latent variables can be checked directly; it gives an upper bound on what can be learned, not a guarantee on real data | 094 §3 | Gelman et al., "Bayesian workflow", arXiv:2011.01808v1 | read (Sections 4.1-4.3 only) | none |
| definition | Recovery of a single truth point and SBC are "two ends of a spectrum" | 094 §3 | Gelman et al., "Bayesian workflow", arXiv:2011.01808v1 | read (Sections 4.1-4.3 only) | none |
| definition | Model recovery confusion matrix p(fit model given simulated model) and inversion matrix p(simulated model given fit model) by Bayes rule | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none |
| definition | Circularity taxonomy: computation check (generator = fitted model), identifiability check (same generator, design question), discrimination and validation (rival generators) | 094 §5 | this file's derivation | derived (§5; derivation shown in file) | none; not for v0 without the derivation check |
| empirical-result | Power for group differences by simulating and recovering for a proposed effect size (advice, no data) | 094 §2 | Wilson & Collins 2019, eLife 8:e49547 | read | none |

Provenance: the table tags follow the file's own tags. Talts, Wilson & Collins, Modrák and Gelman are `read` for the parts the file says it read, with the appendices and proofs named in `note` on each line; Palminteri is `sa`, as the file says, and so its line (Rule 9 validation) is a `read` Wilson & Collins line reporting it, not an `sa` claim. The `derived` line may feed v0 only with the §5 derivation checked. Nothing `sa` feeds an equation.

**Cross-check verdict.** No duplicate of an existing work. Two formulas duplicated in other files under different sources (softmax Eq. 4, RW Eq. 3/5). One dependency gap (the noise level named by protocol step 1, which file 27 does not supply). One internal inconsistency inside Talts (noted, not a contradiction). No cross-file contradictions open.

## Licences of quoted and transcribed material (2026-10-30)

- Talts et al., arXiv:1804.06788v2: not determined; publisher copyright presumed. Used as short quotations (under 60 words each), restated procedure and theorem statement, and a description of the experiments.
- Wilson & Collins 2019, eLife 8:e49547: eLife is an open-access journal; the article licence was not checked in this file, so not determined; publisher copyright presumed. Used as short quotations, restated equations (3, 4, 5, 8, 10, 11) and a description of the Box 4-6 numbers.
- Modrák et al., arXiv:2211.02383v3 (Bayesian Analysis 20(2), 2025): not determined; publisher copyright presumed. Used as short quotations and restated theorem statements (6, 7).
- Gelman et al., Bayesian workflow, arXiv:2011.01808v1: not determined; publisher copyright presumed. Used as short quotations; the one longer block quotation was cut to a single 16-word sentence with the rest paraphrased in this audit.
- Palminteri et al. 2017, Cook, Gelman & Rubin 2006: not read; cited only. Borile et al. 2025 and Lenti et al. 2024: abstracts only, cited only. Not determined; publisher copyright presumed.
- No datasets, tables or Wikipedia-derived text are used in this file.
