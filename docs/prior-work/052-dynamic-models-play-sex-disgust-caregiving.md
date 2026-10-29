# Prior work 52: dynamic models of play, human sexual motivation, disgust and caregiving depletion

Direction: D134

Date: 2026-10-29. Survey for the social-algebra strand. Question (research-map D134, from file 42): is there a dynamic model (state variable, update rule, satiation or decay, trigger, coupling) of play, human sexual motivation, disgust, or caregiving depletion? Seeds: Burgdorf & Panksepp 2006; Spinka, Newberry & Bekoff 2001; Tybur et al. 2013; Schaller & Park 2011; Toates; Ågmo; Pellis. Cross-references: 42 (the verdicts this file revises), 16 (Hull-Spence product form), 17, 22, 29, 33, 40, 46 (Atkinson-Birch), 25 (pathogen-culture link, not repeated).

**Headline.** File 42 said "no dynamics law" for all four. That is right for play and for caregiving depletion *as psychology*, but it missed three things that change the picture: (a) there **is** a published ODE model of sexual response, Blyuss & Kyrychko 2023 (an excitable FitzHugh-Nagumo-type system with a refractory dip), though it is male, phenomenological and unfitted; (b) Toates 2009 states the human sexual-motivation dynamic precisely enough to be written down (positive feedback, then post-orgasm negative feedback, with satiety *raising* later incentive power) though he writes no equation; (c) the nearest formal **disgust** dynamics are not in the disgust literature at all: they are the behavioural-epidemiology models (Funk, Gilad & Jansen 2010), where an "awareness" compartment spreads and decays like a disease, and Nesse's cost-ratio threshold. Caregiving depletion has a genuine stock-and-flow model for work burnout (Homer 1985; Veldhuis et al. 2020) and a genuine reserves-based dynamic game for animal parental care (Barta et al. 2002; McNamara et al. 2000), and no one has joined them for human caregiving. Play has the best quantitative regularity (isolation-duration dose-response in rats) and still no equation.

**Method and honesty note.** Read at source this session, with text on disk: Toates 2009 (full PDF; the copy was a university course-page upload, authorisation unverified, used for reading only); Funk, Gilad & Jansen 2010 (author preprint PDF, full); Schaller & Park 2011 (author PDF, full); Nesse 2019 (PMC, full, it is a one-page brief); Siviy 2016 (PMC author manuscript, searched not read end to end); Veldhuis et al. 2020 (PMC, intro and model-method sections plus limitations). Read only via a summarising fetch (page text garbled, equations transcribed by the summariser): Blyuss & Kyrychko 2023. Abstract or search-summary level only: Spinka et al. 2001, Bell et al. 2015, Dugatkin & Bekoff 2003, Barta et al. 2002 (journal page blocked, 403), van Leeuwen et al. 2023/2025. **Not located or not read**: Burgdorf & Panksepp 2006 (bibliographic record confirmed only), Tybur et al. 2013 (record confirmed; text not accessed this session, so everything on it is `[standard account]` carried from 42), Homer 1985 (record confirmed; model not read, its content is taken from Veldhuis et al.'s description), Ågmo (see Unconfirmed), Pellis & Pellis 2009 book. Tags: `[read]` = text read at source; `[read, summarised]` = read through a summarising fetch; `[abstract]`; `[standard account]`.

---

## 1. Play

### 1.1 Burgdorf & Panksepp 2006 (seed)

**Citation.** Burgdorf, J., & Panksepp, J. (2006). The neurobiology of positive emotions. *Neuroscience & Biobehavioral Reviews*, 30(2), 173-187. DOI 10.1016/j.neubiorev.2005.06.001 (confirmed, Crossref; the seed's year 2006 is the issue date, volume 30). **Not read.** Content below is `[standard account]` and was not independently confirmed; do not build on it. Their vocabulary (as filed in 42): SEEKING, PLAY, 50 kHz calls as an index of positive affect. Burgdorf, Panksepp & Moskal's later review (found via search, not read) states that frequency-modulated 50 kHz calls are elevated by hedonic stimuli and suppressed by aversive ones `[search summary]`.
- **Equations/theorems.** None known.
- **Translation.** Supplies a measurable *output* for a play-level operand (call rate), not a law.

### 1.2 Siviy 2016 and the isolation dose-response (the best quantitative play regularity found)

**Citation.** Siviy, S. M. (2016). A brain motivated to play: insights into the neurobiology of playfulness. *Behaviour*, 153(6-7), 819-844. DOI 10.1163/1568539X-00003349 (confirmed Crossref; PMC5646690). Also Siviy & Panksepp (2011), *Neurosci. Biobehav. Rev.* 35, 1821-1830, DOI 10.1016/j.neubiorev.2011.03.006 (confirmed; abstract level only).

**Their vocabulary.** "motivational state", "tight regulatory control", "titrated", isolation, habenula activity.

**Drives/operands.** Rat social play (rough-and-tumble) as a motivated behaviour whose amount is a function of prior social isolation.

**Key statements `[read]`.** "Play is quite sensitive to variations in motivational state and is under fairly tight regulatory control. For example, the amount of play observed during a discrete observation period (e.g., 5-15 minutes) can be readily titrated by housing rats in isolation for varied amounts of time (Niesink & Van Ree, 1989; Panksepp & Beatty, 1980; Siviy et al., 1997); a rat that has been isolated for 4 hours will play more than a rat that has not been isolated, and a rat that has been isolated for 24 hours will play more than a rat isolated for 4 hours." Different components saturate at different times: Niesink & Van Ree (1989) report "only 3.5 hours of isolation was necessary to yield a maximal increase in social grooming while at least 24 hours of isolation was needed to reach a maximal increase in pinning." Habenula c-fos is higher after 24 h than 3.5 h isolation, and a 15-minute play opportunity attenuates the increase in the medial part of the lateral habenula; Siviy reports this as the work of van Kerkhof et al. (2013a, not checked here) and reads it as consistent with isolation producing a negative affective state that play relieves.

**Operators/equations.** None. What it gives is the *shape* of an accumulator: monotone in deprivation time, component-specific time constants, relief by consummation. A first-order form (play drive P with deprivation d: P = P_max(1 - e^(-d/tau)), consumed by play) is **my illustration, not in any source**; it fits the two or three data points only qualitatively and tau is not estimated anywhere I found.

**Empirical standing.** The isolation effect is old (Panksepp & Beatty 1980, DOI 10.1016/s0163-1047(80)91077-8, confirmed; Niesink & Van Ree 1989, DOI 10.1016/0028-3908(89)90038-5, confirmed). Blunt caveat: this is **isolation-induced increase in play**, which also confounds a general social-contact drive (grooming rises too, with a different time constant). It is not a clean "play rebound after play is blocked" result; the 2022 barrier study found in search (play blocked, other contact allowed) reported impaired prosocial performance, not rebound `[search summary]`. File 42's "deprivation-rebound" should be worded as "isolation-induced elevation."

**Translation.** Operand `play-level` with deprivation counter is supportable *as a rat finding*; the human case is unsupported here.

### 1.3 Spinka, Newberry & Bekoff 2001 (seed)

**Citation.** Spinka, M., Newberry, R. C., & Bekoff, M. (2001). Mammalian play: training for the unexpected. *Q. Rev. Biol.*, 76(2), 141-168. DOI 10.1086/393866 (confirmed). `[abstract/search summary]` Play raises the versatility of movements for recovering from sudden loss of control (falling, shock); animals induce such situations themselves by **self-handicapping** and role reversal; play is often triggered by novel or unpredictable stimuli. A Polish-journal critique found in search says many derived hypotheses are unverified `[search summary]`.
- **Equations.** None. Verbal functional theory.
- **Useful structure for the algebra.** Play is a *deliberately entered, self-limited loss of control*, i.e. a controlled-risk operator: it lowers the actor's control (handicap) while holding fear-gating on. That is a **relation between two other operands (control, fear)**, not a standalone drive.

### 1.4 Pellis and formal play-fighting models

- Pellis & Pellis's book *The Playful Brain* (2009): only a New Scientist review record located (DOI 10.1016/s0262-4079(09)61133-7); book not read. The 50:50 rule's failure in wolves is already in 42 (Essler et al. 2016).
- **Bell, Bell, Schank & Pellis (2015).** Evolving the tactics of play fighting: insights from simulating the "keep away game" in rats. *Adaptive Behavior*, DOI 10.1177/1059712315607606 (confirmed). `[abstract]` Agent-based model (MASON) of keep-away, parameters from the authors' earlier rat and cricket work; agents need neither fixed action patterns nor outcome prediction to reproduce the tactics. Code listed as not found. This is the only **simulation with parameters from data** for play-like interaction I located; it models defence of an object, so it is a model of *the tactics* of play, not of play *motivation*.
- **Dugatkin & Bekoff (2003).** Play and the evolution of fairness: a game theory model. *Behavioural Processes* 60(3), 209-214, DOI 10.1016/S0376-6357(02)00120-1 (confirmed; DOI corrected from my first guess via Crossref). `[abstract]` Fairness expressed at two developmental stages gives four strategies; if both stages are available, "fair at some stage" is predicted more common than "never fair", and when no strategy is ESS all four can coexist. Payoff structure not read. A genuine game-theory model, about the evolution of a play strategy, not drive dynamics.

### 1.5 Play verdict

Best empirical dynamic: isolation dose-response (rats). Best formal: game and agent-based models of play *tactics*. **No equation for a play drive's time course in any species, and nothing at all for humans.** File 42's "no dynamic law" stands; the correction is that the regularity is isolation-elevation with component-specific time constants, and that play ties more to control and fear (1.3) than to a stand-alone accumulator.

---

## 2. Human sexual motivation

### 2.1 Toates 2009: incentive motivation plus hierarchical control

**Citation.** Toates, F. (2009). An integrative theoretical framework for understanding sexual motivation, arousal, and behavior. *Journal of Sex Research*, 46(2-3), 168-193. DOI 10.1080/00224490902747768 (confirmed). `[read]` (full text).

**Their vocabulary.** incentive, incentive value, sexual motivation, sexual arousal, "wanting" vs "liking", sensitization, hierarchical control, "online" and "offline" processing, excitation and inhibition at several levels, active (goal-directed) vs passive (aversion-related) inhibition, Coolidge effect.

**Drives/operands.** Sexual incentive (a stimulus with learned incentive value), sexual motivation (central state), sexual arousal (a specific neural circuit tied to genital state), behaviour; moderators: hormones, novelty, anxiety, attachment, drugs, stress.

**The model's dynamic core `[read]`** (summary of his earlier basic model, which the paper extends; sentence start is cut by the page break): the incentive "first exerts positive feedback in terms of enhancing motivation but, subsequently, negative feedback reduces motivation as a function of orgasm and ejaculation. Satiety is assumed to strengthen the future power of the incentive in its capacity to trigger sexual motivation." Fig. 1 legend `[read]`: "A sexual incentive triggers sexual motivation (1), as well as affecting hormone levels (9), and is compared with memories of earlier experiences (11). Conditional stimuli (CS) also tend to excite sexual motivation (2). Sexual motivation is sensitized by hormones (7). Inhibition is exerted on sexual motivation (3). ... Information on the consequences of the behavioral and genital reactions feeds back to affect motivation (6) and hormones (10)."

**Operators/equations.** **None.** The model is a labelled box-and-arrow diagram (numbered links with plus or minus signs). The only algebraic statement is a hypothesis about arousal as a **multiplicative modulator**: internal arousal "acts as a modulator of the efficacy with which external information and cognitive interpretations are linked to subjective sexual arousal (i.e., a multiplicative relation exists)" `[read]`. The post-ejaculatory refractory period is described as **domain-specific inhibition** (after Bancroft 1999) and "satiation" is attributed to opioids, serotonin, noradrenaline, with prolactin as a candidate `[read]`. Coolidge effect (novelty restores motivation) is tied to nucleus accumbens dopamine `[read]`.

**Derived predictions.** Qualitative: inhibition operates at three levels (aversion-related, goal-directed, post-ejaculatory), and confusion arises from conflating them; stress strengthens the "hot" system and weakens the "cool" one `[read]`. Sensitization and cross-sensitization with drugs.

**Empirical standing.** Integrative review, "intended to stimulate discussion" (abstract). Nothing quantitative. The component facts (refractory period, Coolidge effect) are well established in male rodents; in humans the refractory period is physiological and the Coolidge effect evidence is thinner (not checked).

**Translation.** (i) Two-stage operator: `incentive -> motivation` is *positive feedback until consummation, then negative feedback with a satiation term that raises later susceptibility*. That is a signed-sequence dynamic, the same shape as Atkinson-Birch consummation (file 46), not a new kind of thing. (ii) Inhibition must be **typed** (reactive/aversive, goal-directed, refractory). (iii) Arousal multiplies the link from cue to subjective state. This tells the algebra that "sexual drive" is not one scalar but a cue-gated, level-typed system.

### 2.2 Bancroft & Janssen: dual control

**Citation.** Bancroft, J., Graham, C. A., Janssen, E., & Sanders, S. A. (2009). The dual control model: current status and future directions. *J. Sex Research* 46, 121-142. DOI 10.1080/00224490902747222 (confirmed). Original: Bancroft & Janssen (2000) DOI 10.1016/s0149-7634(00)00024-5 (confirmed in 42). `[abstract/standard account]` Two systems, sexual excitation and sexual inhibition, with individual-difference propensities (measured by SIS/SES scales: PsycTESTS record found). No dynamics; net drive = E - I at a moment. Toates cites it as the source of the idea that inhibition is domain-specific (post-ejaculatory) vs general (fear).

### 2.3 Blyuss & Kyrychko 2023: an actual ODE model

**Citation.** Blyuss, K. B., & Kyrychko, Y. N. (2023). Sex, ducks, and rock 'n' roll: mathematical model of sexual response. *Chaos* 33(4), 043106. DOI 10.1063/5.0143190 (confirmed Crossref). `[read, summarised]` via the AIP page; the page text was partly garbled and the summariser reported the equations below as "the clearest versions"; **re-check against the PDF before use** (the Sussex preprint host refused the connection).

**Their vocabulary.** physiological arousal u, psychological arousal v, excitable system, canard, separatrix as quasi-threshold, stochastic amplification, Masters-Johnson cycle.

**Equations `[read, summarised]`.**
- u' = f(u) - v + E_u (Eq. 6), physiological arousal.
- v' = eps[(E_v - E_v0) + a u - b v] (Eq. 8), psychological arousal; eps << 1 (slow).
- f piecewise (Eq. 7): f1(u) = a0 + a1 u + a2 u^2 + a3 u^3 for u <= u_B (left and middle branches), f2(u) a quintic polynomial b0 + ... + b5 u^5 on the right branch (the text also writes a right-branch form f_M(u_B) - (u - u_B)^5/5, which does not match the Sec. IV choice). Example in Sec. IV: f1(u) = 167/192 - (33/32)u + (7/16)u^2 - (1/24)u^3; f2(u) = 3/2 - (u - 11/2)^5.
- Stochastic version (Eq. 13): Gaussian white noise with intensities D1, D2 added to both equations.
- E_u = physical stimulation (held constant), E_v = psychological stimulation, E_v0 baseline, a = coupling from u to v, b = return rate to psychological homeostasis. The "-v" term is "letting go" and a Yerkes-Dodson argument.

**Derived results `[read, summarised]`.** The system is excitable (FitzHugh-Nagumo analogy; the authors argue against the cusp-catastrophe reading of earlier modelling by Hubey and by Levin: "associating hysteresis on the amplitude response curve with a cusp catastrophe is not justified"): the middle branch of the u-nullcline is repelling, a separatrix acts as threshold, orgasm is defined by u >= u_B; Hopf bifurcations; trajectories resembling Masters-Johnson are canard-like ("with head" orgasmic, "without head" anorgasmic); after orgasm u dips negative ("a short period of negative physiological arousal immediately following an orgasm, a phenomenon well known from clinical practice"), which they link to post-orgasm penile hyper-sensitivity; the term **refractory period** they credit to Levin; fluctuations near the steady state are Ornstein-Uhlenbeck with analytic variance.

**Empirical standing.** Blunt: **qualitative comparison only**; no parameter fitted to data (illustrative values; the authors propose comparison with clinical measurements as future work), male only (stated aim: the Masters-Johnson model "in human males"; females and Basson's circular model named as the next step), stimulation held constant, threshold by convention. Not replicated or extended by others as far as I searched. A 4D love model (intimacy, passion, two partners; Erbas, found in search) exists but is a generic relationship ODE and was not read.

**Translation.** This is the first time the algebra can borrow a **two-timescale, threshold-with-refractory** operator: fast physiological state u, slow cognitive state v, coupling a, threshold crossing as a discrete event, a post-event undershoot. That template is the same as an arousal-release cycle for any drive with a discrete consummation (not only sex). Cost: it is one person, one episode (minutes), not a drive across days, and it does not contain the social partner except as a constant input E_u, E_v.

### 2.4 Other threads (not read)

- Basson's circular model (2000, DOI 10.1080/009262300278641, confirmed): desire may be *responsive* to arousal and intimacy rather than preceding it; found only via secondary summaries, which also report that in a 2015 sample of 174 women only 19.5% endorsed the partial Basson model, 40.8% a composite and 28.7% linear models `[search summary]`. It is a verbal feedback loop (intimacy -> stimulus -> arousal -> desire -> more receptivity), the only human **loop** structure for desire I found; no equation.
- Ågmo: see Unconfirmed.

### 2.5 Sexual-motivation verdict

File 42 said "excitation minus inhibition, Hull-Spence product, refractory decay physiological, no dynamics." Corrected: there is a verbal incentive-feedback model (Toates), a verbal loop (Basson), and **one published ODE** (Blyuss-Kyrychko), unfitted. No model contains a partner (a coupled second person) with a fitted parameter.

---

## 3. Disgust and the behavioural immune system

### 3.1 Tybur et al. 2013 (seed)

**Citation.** Tybur, J. M., Lieberman, D., Kurzban, R., & DeScioli, P. (2013). Disgust: evolved function and structure. *Psychological Review* 120(1), 65-84. DOI 10.1037/a0030778 (confirmed Crossref). **Text not accessed this session**; `[standard account]` carried from 42: three functional domains (pathogen, sexual, moral), each with its own triggers and outputs. No equations. Not repeated.

### 3.2 Schaller & Park 2011: the closest thing to a gating law

**Citation.** Schaller, M., & Park, J. H. (2011). The behavioral immune system (and why it matters). *Current Directions in Psychological Science* 20(2), 99-103. DOI 10.1177/0963721411402596 (confirmed). `[read]` (full).

**Their vocabulary.** behavioral immune system, pathogen cues, "smoke detector principle", false-positive/false-negative errors, "functional flexibility", perceived vulnerability to infection.

**Drives/operands.** Pathogen avoidance triggered by cues; operand = *perceived vulnerability* (chronic or temporarily raised).

**Operators/equations `[read]`.** Verbal laws only: (1) the system is calibrated to minimise false negatives and so makes many false positives (Nesse 2005 principle: "Household smoke detectors ... are calibrated to minimize the likelihood of (potentially fatal) false-negative errors"); (2) "functional flexibility": responses are stronger "when individuals are relatively [more] vulnerable"; costs of avoidance outweigh benefits when invulnerable and vice versa; (3) temporary elevation by circumstances, e.g. exaggerated media coverage of influenza outbreaks, produces inhibitory effects on social interaction. No equation, but the **structure is a monotone gate: response = g(cue-similarity, vulnerability)**.

**Empirical standing.** The 2011 review is a summary; experimental effects exist but the field's replicability is a concern (not assessed in this paper). The smoke-detector claim was explicitly re-tested: van Leeuwen, Jaeger & Tybur's 2023 review (*Nature Reviews Psychology* 2, 676-687; journal DOI 10.1038/s44159-023-00226-4, confirmed Crossref; preprint DOI 10.31234/osf.io/54d3c, confirmed) concludes that **most evidence for the smoke-detector principle is indirect** and calls for signal-detection tests; the preregistered test (van Leeuwen et al., *Evolution and Human Behavior* 2025, N = 1450; no Crossref record found in this validation, see Unconfirmed) found, per its abstract excerpt, that for only one of four target groups were false-alarm tendencies in sickness detection linked to prejudice `[search summary; not read]`. So the "false-alarm-bias causes prejudice" step is **weakly supported at present**.

### 3.3 Nesse: the threshold as an explicit inequality

**Citation.** Nesse, R. M. (2019). The smoke detector principle: signal detection and optimal defense regulation. *Evolution, Medicine, and Public Health* 2019(1), 1. DOI 10.1093/emph/eoy034 (confirmed). `[read]` (a one-page brief). Original: Nesse (2005), *Evol. Hum. Behav.* 26, 88-105 (cited in the brief; not read here). The 2001 NYAS paper (DOI 10.1111/j.1749-6632.2001.tb03472.x) is a confirmed record.

**Equation `[read]`.** With response cost CR, cost of no response when danger is present CD, and probability of danger pD: "If a response provides complete protection, fitness is maximized by expressing a response whenever **pD > CR/CD**." Example in the text: a response that eliminates a 10,000-calorie cost of a lion attack is "worth its 100-calorie cost whenever pD > 1/100, i.e. whenever the noise indicates a 1% or greater chance that a lion is present." (That up to 99% of such responses are false alarms is the implication; the quoted sentence does not state the 99% figure.) Decision table: hit and false alarm both cost CR; miss costs CD; correct rejection costs nothing. "As the amount of information is increased, as reflected by a wider separation of noise and signal distributions, the percentage of false alarms can be reduced without compromising safety."

**Why it matters for the algebra.** This is the one **closed-form, falsifiable** statement in the whole disgust/immune area, and it is not specific to disgust: it is the trigger rule for *any* cheap-protective-response drive (fear, anxiety, disgust, pain). It also yields a lever: raising CD (perceived vulnerability, Schaller & Park) lowers the threshold pD*, so more false alarms. That is a testable instance of "vulnerability raises disgust sensitivity" and ties 3.2 to a formula. Limits: complete protection assumed; costs are assumed known; no time dynamics.

### 3.4 The nearest dynamics: awareness as a contagion (Funk, Gilad & Jansen 2010)

**Citation.** Funk, S., Gilad, E., & Jansen, V. A. A. (2010). Endemic disease, awareness, and local behavioural response. *J. Theor. Biol.* 264(2), 501-509. DOI 10.1016/j.jtbi.2010.02.032 (confirmed). `[read]` (author preprint, full model section). Review: Funk, Salathe & Jansen (2010), Modelling the influence of human behaviour on the spread of infectious diseases: a review, *J. R. Soc. Interface*, DOI 10.1098/rsif.2010.0142 (confirmed record, not read).

**Their vocabulary.** aware/unaware, spread of awareness, loss/forgetting of awareness, reduced susceptibility (sigma_S), reduced infectivity (sigma_I), reproductive number of awareness.

**Equations `[read]`.** Awareness spreads like an SIS process on top of an SIRS disease. Awareness alone (their Eq. 1): dN+/dt = alpha N+ N-/N - lambda N+ + omega I-, where alpha is the awareness-spread rate, lambda the rate it is lost (forgetting), omega the rate at which infected unaware individuals become aware (the source term coupling awareness to prevalence). Without infection the equilibria are N+ = 0 and N+ = (1 - lambda/alpha) N (Eq. 2); the "basic reproductive number of awareness" is **Ra0 = alpha/lambda**. Infection rates become beta, sigma_S beta, sigma_I beta, sigma_S sigma_I beta depending on the awareness of the susceptible and the infected, with the combined effect assumed multiplicative for tractability: "σS I = σS σI". Disease invasion threshold Rd0 = beta/gamma; if Rd0 < 1 but Ra0 > 1, awareness is endemic and disease is not. With a recovery-rate multiplier (aware infected recover faster) and omega > 0 the invasion condition becomes Rd0 > 1 + (theta - 1) omega / ... (their Eq. 11; the text was partly cut, re-check the denominator before use). First-order awareness generated by infection: N+ ≈ omega I- / (|alpha - lambda|) N ... (their Eq. 4; same caution). The full system is six ODEs (S, I, R by aware/unaware).

**Results `[read]`.** Four qualitatively different mean-field equilibria; awareness that lowers susceptibility, infectivity or infection duration makes persistence of the disease harder; pair-approximation analysis shows what happens when the awareness network and the disease network overlap.

**Empirical standing.** Theoretical; the paper does not fit data. The wider "behavioural epidemiology" literature (Funk et al. 2010 review) exists and some models are fitted, but I did not read them.

**Translation, and why this is the most valuable find.** Disgust and avoidance have **no internal dynamics law in psychology**, but this model provides one *between* people: a drive-relevant state (aware / alarmed) that (i) spreads between neighbours with rate alpha, (ii) decays at rate lambda, (iii) is sourced by direct experience omega, (iv) multiplicatively reduces exposure. That is a two-line **operator signature** for a contagious defensive state, with a threshold alpha/lambda. The same algebraic shape would carry fear (17, 18) and moral outrage. It needs psychology to supply what alpha, lambda and omega are for disgust, and nobody has measured them.

### 3.5 Disgust verdict

No within-person disgust time-course model located (no habituation law: a search for it returned nothing, see Unconfirmed). What exists and is usable: Nesse's threshold inequality, Schaller & Park's monotone vulnerability gate, and Funk et al.'s awareness-contagion ODE. Tybur's three-domain split is a typology (domain tags on operands).

---

## 4. Caregiving depletion

### 4.1 Human caregiving: concepts but no dynamics

Search for dynamical or ODE models of compassion fatigue or caregiver depletion returned only regression and structural-equation studies and verbal frameworks `[search summary]`: for example, a 2002 verbal model of compassion fatigue (Figley, C. R. (2002). Compassion fatigue: psychotherapists' chronic lack of self care. *J. Clin. Psychol.* 58(11), 1433-1441, DOI 10.1002/jclp.10090, confirmed Crossref; not read); a dissertation using SEM on spouse caregivers; a 2026 preprint of 374 nurses with regressions explaining about 8% of variance in the fatigue model. **No dynamic model of caregiving depletion in the compassion-fatigue literature was found.** (Klimecki & Singer's empathic-distress vs compassion distinction is the natural psychological candidate and was not searched this session.)

### 4.2 Homer 1985 and Veldhuis et al. 2020: stock-and-flow burnout

**Citations.** Homer, J. B. (1985). Worker burnout: a dynamic model with implications for prevention and control. *System Dynamics Review* 1(1), 42-62. DOI 10.1002/sdr.4260010105 (confirmed). **Not read**; its content here is only what Veldhuis et al. say of it: it was the first to describe key dynamics of employee burnout, "including the cyclical nature of burnout if no learning occurs", built on Homer's own experience `[read, second-hand]`. Veldhuis, G. A., Sluijs, T., van Zwieten, M. H. J., Bouwman, J., Wiezer, N. M., & Wortelboer, H. M. (2020). A proof-of-concept system dynamics simulation model of the development of burnout and recovery using retrospective case data. *Int. J. Environ. Res. Public Health* 17(16), 5964. DOI 10.3390/ijerph17165964 (confirmed; PMC7459661). `[read]` (method and limitations).

**Their vocabulary.** stock, flow, capacity for effort, load, recovery, demands, effort, performance, causal loop diagram, reinforcing and balancing loop, persona.

**Equations, exactly as they illustrate their simplified model `[read]`.**
1. Capacity for effort(t) = Capacity for effort(t0) + ∫_{t0}^{t} (Recovery - Load) ds. A stock with inflow recovery and outflow load.
2. Effort = Min(Demands, f(Capacity for effort)), a nonlinear cap: "when capacity is high ... a small reduction ... might not restrain the available effort much. However, at some point ... a sharp decline in the ability to invest effort."
3. Demands(t) = Demands(t0) + ∫ [Performance × Effect of performance on demands - Demands(t-1)] / Time to adjust demands dt, a goal-seeking stock (target = extrapolated performance).
The loop: effort -> performance -> demands -> effort is reinforcing ("self-reinforcing process"), while high load drains capacity, lowers effort (balancing). The full model is larger (many loops) and was calibrated against "graphs-over-time from multiple participants" for three personas.

**Empirical standing.** Very weak, and the authors say so: "only a small number of participants", all desk researchers at one Dutch institute, "a proof-of-study ... needs improvement." Calibration is to retrospective recalled trajectories. Not a replicated or predictive model. It is about **work** burnout, not interpersonal caregiving.

**Translation.** It gives the algebra a ready-made **depletion operand**: `capacity` as a stock with load (outflow) and recovery (inflow) and a saturating effort function, plus a self-reinforcing demand loop. In a caregiving setting, "demands" are set by another person's need (the care recipient), which is where the social coupling would enter. Nobody has written that variant.

### 4.3 Animal parental care with reserves: the formal analogue

**Citations.** Barta, Z., Houston, A. I., McNamara, J. M., & Székely, T. (2002). Sexual conflict about parental care: the role of reserves. *American Naturalist* 159(6), 687-705, DOI 10.1086/339995 (all confirmed Crossref). McNamara, J. M., Székely, T., Webb, J. N., & Houston, A. I. (2000). A dynamic game-theoretic model of parental care. *J. Theor. Biol.* 205(4), 605-623, DOI 10.1006/jtbi.2000.2093 (confirmed Crossref; authorship corrected in validation, the earlier "Houston, Barta & Osorno" was wrong). Ewald, McNamara & Houston (2007), Parental care as a differential game: a dynamic extension of the Houston-Davies game, *Appl. Math. Comput.*, DOI 10.1016/j.amc.2007.02.060 (confirmed record). `[search summary, abstract level]`: a pair decides each period whether to care or desert; each parent's decision depends on its **own reserves, its mate's reserves and the time in the season**; Barta et al. is the reserves version; the Houston-Davies 1985 game is the static ancestor and Maynard Smith 1977 the original; a 2013 review (Houston, Székely & McNamara; record not confirmed in validation) notes Maynard Smith's model lacks a consistent account of how care affects future reproduction `[search summary]`.

**Equations.** None read.

**Translation.** This is exactly the missing piece 42 asked for ("a budget"): a **state-dependent reserves variable with a care/desert decision rule and a mate-coupled best response**. It is a model of birds, but the structure maps to two human caregivers sharing a dependant: each has a reserve, each chooses a care level, and the equilibrium depends on both reserves. Whether human reserves behave this way is untested here.

### 4.4 Hobfoll-type loss spirals (verbal)

Conservation of resources theory (Hobfoll): resource loss spirals under chronic stress and gain spirals; a longitudinal experience-sampling study reported momentum and magnitude effects and possible reversal of spirals `[search summary; Hobfoll 2001 not found, not read]`. Qualitative; no ODE found.

### 4.5 Caregiving verdict

Two formal templates exist but have not been joined: (a) a **burnout stock-and-flow** (4.2; one weak fitted example) and (b) a **reserves-and-desertion dynamic game** (4.3; theory). The human interpersonal caregiving case has verbal theory and regression, nothing dynamic.

---

## 5. What exists versus what does not

**Exists (usable as stated, with the caveats given).**
1. Nesse's inequality **pD > CR/CD** as a threshold law for cheap protective responses, which covers disgust and fear and gives a lever (vulnerability raises CD). [read]
2. The Funk-Gilad-Jansen awareness ODE (spread alpha, loss lambda, source omega, multiplicative exposure reduction, threshold alpha/lambda), a ready operator for any contagious defensive state. [read]
3. A two-timescale excitable ODE for sexual response with threshold and refractory undershoot (Blyuss-Kyrychko 2023). [read, summarised; unfitted]
4. A stock-and-flow capacity/load/recovery depletion model (Veldhuis 2020; Homer 1985 second-hand). [read; weakly calibrated]
5. Reserves-dependent care/desertion dynamic games for animal parents (Barta et al. 2002; McNamara et al. 2000; Ewald et al. 2007). [abstract only]
6. The isolation-time dose-response of rat play with component-specific time constants (Siviy 2016). [read]
7. A precise verbal statement of the human sexual-motivation dynamic (Toates 2009): positive then negative feedback, satiety raising later incentive power, typed inhibition. [read]

**Does not exist (to the extent searched).**
1. Any equation for a play drive's time course, in any species; any human play-dynamics model.
2. A *fitted* model of human sexual motivation across days, or any with a coupled partner.
3. Any within-person disgust dynamics (accumulation, habituation, recovery); any fitted disgust parameters (alpha, lambda, omega analogues).
4. A dynamic model of human interpersonal caregiver depletion; a joined burnout-plus-reserves model with a care recipient's need as input.
5. Direct evidence that a false-alarm bias (smoke-detector) *causes* the prejudice the behavioural-immune-system predicts. Current direct tests are weak.
6. Anything that composes these four drives with each other or with fear or status: no coupling coefficients are measured anywhere in this cluster.

**Implication for the algebra (a judgement, not from a source).** For these four drives the algebra would again be *proposing* the dynamics, but it can now propose from **three imported shapes** rather than none: threshold gate (Nesse), contagion with decay (Funk), and fast-slow excitable cycle (Blyuss-Kyrychko), plus one imported depletion stock (Veldhuis). Play is the outlier: its best-supported structure is a relation to control and fear (Spinka) and a deprivation counter, not its own law.

---

## Unconfirmed

- Burgdorf & Panksepp 2006 content (only the record and a later co-authored review's claim on 50 kHz calls). Tybur 2013 content (carried from 42). Homer 1985 content (second-hand only).
- Whether the Blyuss-Kyrychko equations are transcribed correctly (summarised from garbled page text); parameter values and any statements in the truncated Discussion.
- The inequality in Funk et al. Eq. 11 and the exact form of Eq. 4 (partly cut in extraction).
- The equations of Barta et al. 2002 and McNamara et al. 2000 (citations now confirmed); whether any of these have human applications; the Houston, Székely & McNamara 2013 review (record not located).
- van Leeuwen et al. 2025 (*Evol. Hum. Behav.*, N = 1450): no Crossref record found by a bibliographic query; the finding is from a search excerpt only.
- Ågmo: file 42 cites Ågmo 2007, *Functional and Dysfunctional Sexual Behavior*, with chapter DOI 10.1016/b978-012370590-7/50005-0. Validation resolved 50005-0 at Crossref: Ågmo, A. (2007), "The stimulus control of sexual incentive motivation", pp. 147-190 in that book (the "Neural control of sexual behavior" chapter is 50007-4, pp. 231-256). The record is confirmed, but I did not read any Ågmo text, and make no claim about his incentive-motivation arguments beyond what Toates (read) says.
- Disgust habituation or contamination dynamics (Rozin and Nemeroff's laws of contagion and similarity were confirmed only as concepts; no time-course or equation). A search for habituation returned nothing relevant.
- Whether Basson's circular model has been formalised as equations (searched, none found); the figures on women's endorsement (174 women) are from a search summary of a 2015 paper not identified here.
- The 2022 barrier-deprivation study on play, the Erbas 4D love model, Pellis & Pellis 2009 book, Funk-Salathe-Jansen 2010 review, Hobfoll 2001: seen only as search results.
- Human play: no human play-deprivation or play-rebound evidence was searched beyond rodent work; Gray and Geary remain verbal as in 42.

## Validation log (2026-10-29)

Every DOI below was resolved at api.crossref.org/works/<doi>. Content re-read this pass: Nesse 2019 (OUP page), Siviy 2016 (PMC), Blyuss & Kyrychko 2023 (AIP page, through a summarising fetch). Veldhuis 2020 (PMC and MDPI both refused the fetch: captcha, 403) and the Funk, Toates and Schaller & Park texts were not re-read, so their quotes rest on the first pass. The web-search budget ran out partway through this pass, so no claim could be tested by a fresh search.

- ✓ Burgdorf & Panksepp 2006, NBR 30(2) 173-187: record matches; content correctly left as standard account.
- ✎ Siviy 2016, Behaviour 153(6-7) 819-844: record and both quotes match the text [read]. The habenula c-fos finding is now credited to van Kerkhof et al. 2013a, the authors Siviy cites, and is placed in the medial lateral habenula.
- ✓ Siviy & Panksepp 2011, NBR 35(9) 1821-1830: record matches.
- ✓ Panksepp & Beatty 1980, Behav. Neural Biol. 30(2) 197-206; Niesink & Van Ree 1989, Neuropharmacology 28(4) 411-418: records match.
- ✓ Spinka, Newberry & Bekoff 2001, QRB 76(2) 141-168: record matches.
- ✓ Hooper 2009, New Scientist review of Pellis & Pellis *The Playful Brain*: record matches (the reviewer is R. Hooper).
- ✓ Bell, Bell, Schank & Pellis 2015, Adaptive Behavior 23(6) 371-380: record matches.
- ✓ Dugatkin & Bekoff 2003, Behav. Processes 60(3) 209-214: record matches.
- ✓ Toates 2009, J. Sex Res. 46(2-3) 168-193: record matches. Quotes not re-checked here.
- ✓ Bancroft, Graham, Janssen & Sanders 2009, J. Sex Res. 46(2-3) 121-142; Bancroft & Janssen 2000, NBR 24(5) 571-579: records match.
- ✎ Blyuss & Kyrychko 2023, Chaos 33(4) 043106: Eqs. 6, 8 and 13 and the Sec. IV f1 and f2 match. Eq. 7's right branch is a general quintic, and the text's (u-u_B)^5/5 form does not match Sec. IV; the file now says so. The cusp critique is now credited to its targets, Hubey and Levin. The post-orgasm dip is now quoted, and the authors link it to hyper-sensitivity, with "refractory period" credited to Levin. Males only is confirmed, and future work on women and Basson is noted. Hopf, canard with and without head, 2D Ornstein-Uhlenbeck and the separatrix as quasi-threshold are all confirmed verbatim.
- ✓ Basson 2000, J. Sex Marital Ther. 26(1) 51-65: record matches. The 174-women figures remain unconfirmed.
- ✓ Tybur, Lieberman, Kurzban & DeScioli 2013, Psych. Rev. 120(1) 65-84: record matches.
- ✓ Schaller & Park 2011, CDPS 20(2) 99-103: record matches. Quotes not re-checked here.
- ✎ van Leeuwen, Jaeger & Tybur 2023: journal DOI 10.1038/s44159-023-00226-4 found and added (Nat. Rev. Psychol. 2, 676-687 confirmed). The preprint DOI matches.
- ? van Leeuwen et al. 2025, Evol. Hum. Behav.: no Crossref record found; moved to Unconfirmed.
- ✎ Nesse 2019, EMPH 2019(1) 1: the inequality pD > CR/CD and the separation sentence are verbatim [read]. The lion example is now quoted exactly, and "99% are false alarms" is marked as an implication, not the source's sentence.
- ✓ Nesse 2001, Ann. NY Acad. Sci. 935 75-85: record matches.
- ✓ Funk, Gilad & Jansen 2010, JTB 264(2) 501-509; Funk, Salathé & Jansen 2010, JRSI 7(50) 1247-1256: records match. The equations were not re-read here, and the Eq. 4 and Eq. 11 cautions stand.
- ✎ Figley 2002: completed to J. Clin. Psychol. 58(11) 1433-1441, DOI 10.1002/jclp.10090 (confirmed).
- ✓ Homer 1985, Syst. Dyn. Rev. 1(1) 42-62: record matches.
- ✓ Veldhuis et al. 2020, IJERPH 17(16) 5964: authors and title match. The equation quotes were not re-checked (fetch refused).
- ✎ Barta, Houston, McNamara & Székely 2002, Am. Nat. 159(6) 687-705: the volume and pages, flagged earlier as from memory, are confirmed.
- ✎ McNamara et al. 2000, JTB 205(4) 605-623: the **authors were wrong**. It is McNamara, Székely, Webb & Houston, not "Houston, Barta & Osorno"; corrected.
- ✓ Ewald, McNamara & Houston 2007, Appl. Math. Comput. 190(2) 1450-1465: record matches.
- ? Houston, Székely & McNamara 2013 review: not located; marked unconfirmed.
- ✎ Ågmo 2007: DOI 50005-0 resolves to "The stimulus control of sexual incentive motivation", pp. 147-190. Unconfirmed note updated.

**Verdict.** No cited work was fabricated, and every DOI resolves to the work and authors named, with one exception: the McNamara et al. 2000 author list was wrong and is now corrected. The quotes re-read this pass (Nesse, Siviy, Blyuss-Kyrychko) are accurate. The changes were credit fixes (van Kerkhof for the habenula result, Hubey and Levin as the target of the cusp critique) and a tightening of the Blyuss-Kyrychko Eq. 7 transcription. The file's central claims stand. Its "nothing exists" claims could not be re-tested by search this pass and remain as stated "to the extent searched".

## Cross-checks (2026-10-29)

Method: grepped every other file in this folder for the works, authors, equations and numbers used here. Files 42 and 52 overlap most, and 52 was written to revise 42, so differences with 42 are listed as contradictions even where the revision is deliberate. No web check was needed: every disagreement is a revision that rests on text read at source in this file, or a difference in wording or scope. No other file was edited.

### Agreements

- **Tybur et al. 2013 (section 3.1)** and file 42 (disgust bullet, Tybur 2013): same citation (Psych. Rev. 120(1), 65-84, DOI 10.1037/a0030778) and the same three domains (pathogen, sexual, moral). Both mark the content as a standard account.
- **Schaller & Park 2011 (section 3.2)** with 42 (behavioural immune system bullet) and 17 (Schaller & Park entry): same DOI (10.1177/0963721411402596), same claim that perceived vulnerability raises disgust and xenophobia, same smoke-detector false-positive bias. 52 adds that the smoke-detector causal step is weakly supported (van Leeuwen et al. 2023). 25 holds the pathogen-to-culture link, which 52 correctly leaves alone.
- **Funk, Salathe & Jansen 2010 review (section 3.4)** with 42 (disgust / behavioural-epidemic bullet) and 23 (reference list): same DOI (10.1098/rsif.2010.0142), same role as the formal home of avoidance responding to prevalence. 23 and 52 use different Funk papers (23: Funk et al. 2009 PNAS, abstract only; 52: Funk, Gilad & Jansen 2010 JTB, read in full). Their results are compatible. 23 reports that global awareness does not change the epidemic threshold, and 52 has the threshold Rd0 = beta/gamma unchanged when awareness is not sourced by infection (omega = 0).
- **Burgdorf & Panksepp 2006 (section 1.1)** with 22 (references): same DOI (10.1016/j.neubiorev.2005.06.001) and same volume and pages (30, 173-187). 17 and 33 cite the neighbouring Panksepp & Burgdorf 2003 and 2000 papers, which 52 does not use.
- **Play suppressed by fear (sections 1.3 and 1.5)** with 42 (play bullet, table row) and 17 (Panksepp PLAY): all say play needs safety and is suppressed by fear. 52's step is to treat play as a relation to control and fear rather than a stand-alone accumulator.
- **Pellis & Pellis, The Playful Brain (section 1.4)** with 33 (play bullet) and 42: all list the book without a read text. 52 adds only a New Scientist review record.
- **Spinka, Newberry & Bekoff 2001 (section 1.3)** with 42 (play as exploration / learning): same DOI (10.1086/393866) and same self-handicapping and loss-of-control account. Neither file read the paper.
- **Toates and Ågmo (section 2.1)** with 42 (sexual motivation bullet): both say sexual motivation is incentive-driven with no accumulating deficit like hunger, and both give the same Ågmo 2007 chapter DOI (50005-0). 52 read Toates 2009 and found no Hull-Spence product, only a multiplicative arousal modulator. 42 flagged that it had not located a product form in Toates or Ågmo, so the two agree.
- **Isolation dose-response (section 1.2)** with 076 (Tomova 2020, Stijovic 2023): 052's illustrative saturating form P = P_max(1 - e^(-d/tau)) matches 076's candidate form d = D(1 - e^(-t/tau)). Both say no tau has been estimated and no human saturation data exist, and both note the isolation / general social-contact confound.
- **Dynamic games with state (section 4.3)** with 071 (Houston & McNamara dynamic games): both describe equilibria of state-dependent strategies, where the other animal's behaviour is part of the environment. 52 applies this to parental care with reserves, and none of those papers was read in full.
- **Atkinson-Birch (section 2.1, translation)** with 046: 52 says Toates's positive-then-negative feedback has the same shape as Atkinson-Birch consummation. That is consistent with 046, where consummatory force reduces the action tendency while the activity is under way. One nuance for the reader: 046 has no term where satiety raises later incentive power, but 52 reports one for Toates. The "same shape" claim holds for the signed sequence only, not for that satiation-sensitisation term.
- **Empathic distress vs compassion (section 4.1)** with 41 (Singer & Klimecki): 52 names the pair as a candidate not yet searched. 41 holds it as an abstract-level concept with no dynamics, so there is no conflict.

### Contradictions

| Claim in 052 | Claim in the other file | Other file | Verdict |
|---|---|---|---|
| Sections 1.2 and 1.5: the play regularity is "isolation-induced elevation" with component-specific time constants, not a clean deprivation rebound. | 42 (play bullet and table row): "rebound after isolation", a "deprivation-accumulation effect" and "deprivation counter", from the standard account. | 42-social-drives-dynamics-by-drive.md | 052 is right. It read Siviy 2016 at source: grooming saturates at about 3.5 h and pinning needs 24 h or more, and the effect is confounded with general social contact. 42 never read the source. The deprivation counter survives only as a rat finding. |
| Section 2.3 and 2.5: one published ODE of sexual response exists (Blyuss & Kyrychko 2023), a fast-slow excitable system with a refractory dip. | 42 (sexual motivation bullet and table row): "refractory decay (physiological)", no dynamics. | 42-social-drives-dynamics-by-drive.md | 052 is right (supersedes 42). The equations were read through a summarising fetch and then checked against the AIP page in validation. The model is unfitted and male-only. 42 predates the find. |
| Sections 4.1 to 4.5: formal templates exist for depletion (the Veldhuis stock-and-flow and the Barta reserves game), though none for human interpersonal caregiving. | 42 (care / nurturance table row): "Smith-Fretwell tangent and Trivers inequality; no time dynamic". | 42-social-drives-dynamics-by-drive.md | Compatible in scope. 42 is right that no time dynamic exists for human caregiving. 052 adds work-burnout and animal-reserves dynamics from other domains. Neither file has a fitted human model. Treat 052 as narrowing 42. |
| Section 3.5: disgust has usable formal pieces (the Nesse inequality, a vulnerability gate, the Funk awareness ODE). | 42 (disgust table row): "None (typology + smoke-detector gate)". | 42-social-drives-dynamics-by-drive.md | 052 is right (supersedes 42). 42's "None" is true only for within-person time courses, and 052 agrees there is none (section 3.5). The inequality and the ODE are between-person or threshold structures. |
| Section 2.1: Toates 2009 contains no equation; the only algebraic statement is a multiplicative arousal modulator. | 42 (sexual motivation bullet): "Hull-Spence style product of state x incentive is the standard form [see 16]". | 42-social-drives-dynamics-by-drive.md | Resolved in 052's favour for Toates 2009. 16 (Toates 1986 incentive motivation) is `[standard account]` and was not read. 42 itself flags the product form as by analogy and not found in Toates or Ågmo. 052 only shows that the 2009 paper has none. |
| Section 1.1 and 1.5: no equation for a play drive's time course in any species. | 19 (Kismet engineered play drive, listed in 42's table as a play dynamic). | 42-social-drives-dynamics-by-drive.md | Unresolved, and probably a scope difference. 052 means models of a biological play drive. Kismet is an engineered robot drive, which 42's table lists as a dynamic. Not checked against file 19's text. |

### Not checked

- 052 section 3.4 (Funk 2010 Eq. 4 and Eq. 11) was flagged by its own authors as partly cut in extraction. No other file repeats those equations, so nothing here can settle them.
- 050 reports that the ANPS PLAY scale merges partly with SEEKING (r about .50). That is compatible with 052's "play is not a stand-alone accumulator", but 052 does not mention it. Worth a cross-reference in a later edit.
- Veldhuis 2020, Homer 1985, Blyuss & Kyrychko 2023, Barta et al. 2002, Nesse 2019 and Basson 2000 appear in no other file, so no cross-check was possible.
