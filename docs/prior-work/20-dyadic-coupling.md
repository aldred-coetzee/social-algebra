# Prior work 20: Dynamical models of dyadic coupling (one person's state changing another's, with equations)

Date: 2026-10-29. Survey for `social-algebra`. Not committed.

Aim served (Aldred, 2026-10-29): an algebra of basic human and group drives (curiosity, fear, desire) that compose into equations, yield theorems, and predict or control behaviour. Surveys 15-19 found drive dynamics for single agents. This note covers the missing piece: **drives between people**, with equations.

## Summary

1. **Between-person coupling does have equations, and they all share one skeleton:** each person's next state (or rate of change) = own inertia + pull toward an own set point + a function of the partner's state. Gottman-Murray, Strogatz, Rinaldi, Felmlee-Greenberg, Boker coupled oscillators and Butler's TIES are the same skeleton with different choices for the last term (see "Common skeleton").
2. **The coupled state is almost always one scalar per person: affect or "love/positivity".** No *dyadic* model found couples fear, desire or curiosity as separate drives. *(Corrected in validation: at group scale, fear contagion does have equations and an empirical test: the ASCRIBE family, Bosse et al. 2013, and Tsai et al. 2013, covered in surveys 18 and 23. Rinaldi's Laura-Petrarch model also couples love to a second state, inspiration, and Sadler couples two dimensions.)* Attachment appears as a parameter or moderator that sets coupling strength (Rinaldi's "secure/insecure", Sbarra-Hazan, Coan, Butner et al. 2007), not as a coupled state.
3. **Theorems exist, mostly for the 2-variable system:** fixed points, stability and Hopf bifurcations (Strogatz, Rinaldi, Bielczyk et al.), pitchfork bifurcation and a no-limit-cycle theorem (Liebovitch et al. 2008), steady states and null-cline intersections (Gottman). *(Corrected in validation: the first draft said nothing exists for n > 2 bar one delay example.)* Three-person models with equations exist (Bielczyk et al. delay triads, Bagarello-Oliveri's operator triangle, Dercole-Rinaldi's chaotic triangle, Sprott), and Liebovitch et al. report numerics for 3-10 actors (all-competitive networks split into two opposed camps). What is missing is n-person *theorems* and any n-person fit to data.
4. **Prediction is the weak spot.** The headline "94% divorce prediction" was a fit; cross-validation, base rates and one independent test (Kim, Capaldi and Crosby 2007) cut it down. The equations are fitted to a couple's data, not derived from a law.
5. **The statistical counterpart (APIM) is a cross-lagged regression:** the same skeleton with the dynamics removed. It is how most dyad data is actually analysed.

**Verification note.** I opened source text in full only for Bielczyk, Foryś and Płatkowski (arXiv 1202.2338), which restates Strogatz's and Felmlee-Greenberg's equations. Everything else is from web search results (abstracts, library pages, blogs) on 2026-10-29. DOIs were checked against Crossref. *Validation pass (2026-10-29) additionally read at source:* Murray, *Mathematical Biology I* ch. 5 (Gottman-Murray equations); Gottman et al. 2003 (*J. Homosexuality*, repair/damping model); Rinaldi 1998 (Laura-Petrarch equations); Liebovitch et al. 2008 (accepted manuscript); Kelso's Scholarpedia HKB entry; Bielczyk et al. re-read for the theorems and triad. Tags: **[read]** = read at source (or at a source that quotes the equation, named); **[abs]** = from abstract or search summary; **[std]** = standard account from general knowledge, not checked this pass (repeated in Unconfirmed).

---

## 1. Gottman-Murray: difference-equation models of marital interaction

- **Citations (DOIs confirmed):** Cook, Tyson, White, Rushe, Gottman and Murray (1995), "Mathematics of marital conflict", *J. Family Psychology* 9:110-130, doi 10.1037/0893-3200.9.2.110. Gottman, Swanson and Swanson (2002), "A general systems theory of marriage: nonlinear difference equation modeling of marital interaction", *Personality and Social Psychology Review* 6(4):326-340, doi 10.1207/s15327957pspr0604_07. Gottman, Murray, Swanson, Tyson and Swanson, *The Mathematics of Marriage*, MIT Press, 2002, doi 10.7551/mitpress/4499.001.0001. (Some listings say 2005 for the paperback; Crossref says 2002.)
- **State variables:** one scalar per spouse per turn of talk: the "positivity/negativity" of each speaker's turn, from coded video: positive-minus-negative RCISS speaker codes in Cook et al. and Murray ch. 5 [read], weighted SPAFF (Specific Affect) codes, range -24 to +24, in the 2003 paper [read].
- **Coupling equations [read, Murray, *Mathematical Biology I*, 3rd ed. 2002, ch. 5, eqs. 5.4-5.5, co-author of the model; archive.org text]:**
  `W_{t+1} = I_HW(H_t) + r_1 W_t + a`, `H_{t+1} = I_WH(W_{t+1}) + r_2 H_t + b`.
  *(Validation correction: the first draft, following a blog, had `I_WH(W_t)` in the husband's equation. The source uses `W_{t+1}`: turns alternate, the wife speaks first, and the husband responds to the turn just spoken. The asymmetry is deliberate.)* `r_i` is **emotional inertia**; the **uninfluenced steady state** is `a/(1-r_1)` (stable iff `|r_1| < 1`) [read]. Uninfluenced parameters are estimated by least squares on the ~15% of turns where the partner scored 0; the influence function is then the averaged residual at each partner score [read]. Score 0 has zero influence by assumption [read].
  **Influence-function forms [read, Murray ch. 5]:** (a) **bilinear** ("two-slope"): two lines through the origin, one slope for partner positivity and one for negativity; (b) **ogive / sigmoid approximated by piecewise-constant segments**: no influence inside a band around zero, a constant positive (negative) push once the partner passes a positive (negative) threshold. "A more reactive spouse has a lower threshold of response." Murray says both are used; Cook et al. (1995) estimated the function empirically and summarised it as two-slope [read]. Gottman et al. (2003, *J. Homosexuality* 45(1):65-91, read in full via a Berkeley lab copy) report the bilinear form fits their data best and add **repair and damping terms**: `N_{t+1} = r_1 N_t + a + I_{P→N}(P_t) + E_PR R(K_P) + E_PD D(K_P)` (and symmetrically), where `R` is a trigger that jumps the series up by effectiveness `E` once negativity passes threshold `K`, and `D` is its mirror for positivity; adding them "improved the fit of the model by an order of magnitude" [read]. Note that this later paper writes both influence terms at lag `t`, not `t+1`.
  **Threshold finding: direction contested.** Murray ch. 5 says couples who later divorced (newlywed study, Gottman et al. 1999/2002) "initially had more negative uninfluenced husband and wife steady states, more negative influenced husband steady state and lower negative threshold in the influence function" [read]. The first draft said the opposite, that *good* couples had the low negativity threshold (from a blog; this is also the popular reading). Whether "lower" means a smaller magnitude or further down the negative axis is not resolved in what was read; treat the sign of this result as unconfirmed.
- **Derived results:** analysis by phase space and null-clines; the steady states are intersections of the two null-clines, split into **uninfluenced** and **influenced** stable steady states (attractors) [abs, UBC course page on the book]. Cook et al.: unstable marriages show a **mismatch of husband and wife influence functions** at time 1 [abs]. The 2002 abstract frames it as a way to predict divorce or stability from interaction, "general for any time series for two individuals" [abs]. The book reports a "marriage experiment" lowering or raising heart rates to see which parameters move [abs].
- **Empirical fitting and standing.** Parameters are fitted per couple from a short conversation (the Cook et al. description: fit equations to a couple, simulate other conditions, test them experimentally [abs]). The coded affect is noisy, so fits are of the couple, not tested out of sample in anything I found.
  - **Prediction claims:** Gottman's FAQ states the 93.6% accuracy was for a 1992 study and calls the 94% figure "a source of confusion"; says six of seven studies were predictive, the first being post hoc [read, gottman.com FAQ]. Note that page does not mention Heyman.
  - **Critique:** Heyman and Smith Slep (2001), "The hazards of predicting divorce without crossvalidation", *J. Marriage and Family* 63(2):473-479, doi 10.1111/j.1741-3737.2001.00473.x. Abstract [read, Europe PMC record of the author manuscript]: names Gottman, Coan, Carrere and Swanson (1998) as its example; prior studies ignored cross-validation and the prevalence of divorce; on archival data "accuracy and predictive value drops precipitously during crossvalidation". The numbers (528 people from the 1985 National Family Violence Survey; positive predictive value 65% on the fitting half, 29% on the hold-out half, 21% at a 16% base rate) come only from a secondary write-up and are unchecked. Note the critique is a demonstration on *other* data, not a re-analysis of Gottman's.
  - **Independent test:** Kim, Capaldi and Crosby (2007), *J. Marriage and Family* 69(1):55-72, doi 10.1111/j.1741-3737.2006.00343.x. 85 at-risk community couples (Oregon Youth Study), affect measured around age 21, status ~2.5 years on; men's rejection of influence, lack of men's de-escalation, and women's negative start-up did not predict relationship status [abs]. These are the 1998 affective-process variables (Gottman, Coan, Carrere and Swanson 1998, *J. Marriage and the Family* 60(1):5-22, doi 10.2307/353438), not the difference-equation parameters themselves. Reply: Coan and Gottman (2007), "Sampling, experimental control, and generalizability in the study of marital process models", *JMF* 69:73-80, doi 10.1111/j.1741-3737.2006.00344.x (argue the sample is too specialised); rejoinder Kim and Capaldi (2007), *JMF* 69:86-91, doi 10.1111/j.1741-3737.2006.00346.x. **I found no independent out-of-sample test of the difference-equation model's own parameters.** (Stanley et al. on Gottman's reliability: not found; see Unconfirmed.)
  - **The model's own prediction paper (missing from the first draft):** Gottman, Swanson and Murray (1999), "The mathematics of marital conflict: dynamic mathematical nonlinear modeling of newlywed marital interaction", *J. Family Psychology* 13(1):3-19, doi 10.1037/0893-3200.13.1.3: the newlywed fit whose parameter-divorce associations Murray summarises (above). Not opened.
- **Independent reuse of the model:** Liebovitch, Peluso, Norman, Su and Gottman (2011), "Mathematical model of the dynamics of psychotherapy", *Cognitive Neurodynamics* 5:265-275, doi 10.1007/s11571-011-9157-x, and Peluso et al. (2012), *Psychotherapy Research* 22:40-55, doi 10.1080/10503307.2011.622314: the same equations fitted to therapist-client sessions [title/abs only]. Liebovitch et al. (2008, section 4b below) write a continuous version.
- **2 to n people / groups:** The form extends mechanically (a vector state, an `I_ij` per ordered pair). No n-person Gottman fit to data was found; the nearest is Liebovitch et al.'s continuous version, run numerically for 3-10 actors (section 4b). Pairwise influence functions in a group give n(n-1) functions to fit.
- **Translation:** operands: person with one affect scalar; operator: the influence function `I_ij`, a nonlinear unary map from the sender's state to a *push* on the receiver. Parameters per person: set point, inertia. Threshold form means the operator is not linear, so operators do not compose by matrix product.

## 2. Strogatz 1988 and Rinaldi: love as coupled differential equations

- **Strogatz (1988)**, "Love affairs and differential equations", *Mathematics Magazine* 61(1):35, doi 10.1080/0025570x.1988.11977342; developed in *Nonlinear Dynamics and Chaos* (1994), pp. 138-140 (as cited by Bielczyk et al., who give the year of the Math. Magazine paper as 65(1); Crossref says volume 61).
  - **State:** R(t), J(t), feeling of Romeo and Juliet toward the other (positive love, negative hate).
  - **Equations [read, via Bielczyk et al. eq. 1]:** `R' = aJ`, `J' = -bR`, a, b > 0 (Romeo echoes Juliet; Juliet flees Romeo's love). A harmonic oscillator, equilibrium (0,0) a **centre**: endless love-hate cycles. General linear form `r' = a11 r + a12 j`, `j' = a21 r + a22 j`, stable iff trace A < 0 and det A > 0 [read, eq. 3, 7]. Sign of (a11, a12) (own feelings, partner's feelings) names the types. *(Validation correction: the first draft gave Bielczyk et al.'s labels as if they were Strogatz's.)* Strogatz's book exercise (dR/dt = aR + bJ) names them **eager beaver** (+,+), **narcissistic nerd** (+,-), **cautious (or secure) lover** (-,+) and **hermit** (-,-) [abs, two secondary course pages; the book not opened]. Bielczyk et al. keep "eager beaver" and "cautious lover" (quoting Strogatz) but coin their own **narcissus** (+,-) and **"stoic lover"** (-,-) [read].
  - **Theorems:** standard 2x2 linear stability; here nothing new, and Strogatz said it was a teaching model. **Standing:** none empirical; a pedagogical device.
- **Rinaldi:** Rinaldi (1998), "Laura and Petrarch: an intriguing case of cyclical love dynamics", *SIAM J. Appl. Math.* 58:1205-1221, doi 10.1137/s003613999630592x; Rinaldi and Gragnani (1998), "Love dynamics between secure individuals: a modeling approach", *Nonlinear Dynamics, Psychology, and Life Sciences* 2:283-301, doi 10.1023/a:1022935005126.
  - **State:** love of each partner (Laura-Petrarch model has three ODEs: two loves plus the poet's "inspiration") [read].
  - **Equations [read, Rinaldi 1998 SIAM, eqs. 1-5, JSTOR copy]:**
    `L' = -α1 L + R_L(P) + β1 A_P`,
    `P' = -α2 P + R_P(L) + β2 A_L / (1 + δ Z)`,
    `Z' = -α3 Z + β3 P`,
    with `R_P(L) = β2 L` (linear) and `R_L(P) = β1 P (1 - (P/γ)²)` (cubic: rising then falling for P > 0 as Laura rebuffs pressure; reversed for P < 0 as pity overcomes antagonism). The `-α x` term is **forgetting**; `A` is the partner's **appeal** (Petrarch's is negative); inspiration `Z` is an exponentially weighted integral of P and **damps** Petrarch's response to Laura's appeal. All Greek letters positive. Rinaldi says the cubic is chosen for convenience and results are robust to perturbations of it [read].
  - **General form across Rinaldi's papers** [std]: `x_i' = -α_i x_i + R_i(x_j) + I_i(A_j)`, with a reaction function to love and an instinct function to appeal. The personality labels **secure** (reaction rises with partner's love), **insecure** (reaction falls past a threshold), **biased** (appeal perceived as larger when in love) come from Rinaldi and Gragnani 1998 and later papers [abs, IIASA blog; equations of those papers not opened].
  - **Derived results:** explicit conditions for a globally stable slow-fast **limit cycle** when inspiration is slow [abs]; "secure" couples follow a standard path to a positive plateau; a single insecure partner is enough for an unbalanced regime and possible breakup; insecure plus biased gives recurrent ups and downs; love triangles can be chaotic [read, IIASA blog, which states no empirical validation].
  - **Fitting:** the Laura-Petrarch model is calibrated to about 20 years of Petrarch's poems, and cross-checked against a stylistic analysis (F. Jones) [abs]. One case, one author's reading.
- **Further Rinaldi line (missing from the first draft, DOIs confirmed):** Rinaldi (1998), "Love dynamics: the case of linear couples", *Applied Mathematics and Computation* 95:181-192, doi 10.1016/s0096-3003(97)10081-9; Dercole and Rinaldi (2014), "Love stories can be unpredictable: *Jules et Jim* in the vortex of life", *Chaos* 24:023134, doi 10.1063/1.4882685 (a **love triangle written as ODEs with chaotic dynamics**) [title/abs]; and the monograph Rinaldi, Della Rossa, Dercole, Gragnani and Landi (2015), *Modeling Love Dynamics*, World Scientific, doi 10.1142/9656 [title only].
- **2 to n:** triangles are in Rinaldi's line with equations (Dercole and Rinaldi 2014), in Sprott (2004, "Dynamical models of love", *Nonlinear Dynamics, Psychology, and Life Sciences* 8(3); DOI not found; triangle equations and a chaotic solution in his lecture slides [abs]), in Bagarello and Oliveri (2010, section 4) and in Bielczyk et al. (below). **Translation:** operand: scalar love per person; operator: reaction function R, whose *shape* is the personality. Attachment style appears here as a parameter of the operator, not a state.

## 3. Felmlee and Greenberg 1999: ideals plus partner difference

- **Citation:** Felmlee and Greenberg (1999), "A dynamic systems model of dyadic interaction", *J. Mathematical Sociology* 23(3):155-180, doi 10.1080/0022250x.1999.9990218. Application chapter: Felmlee (2006), doi 10.1093/oso/9780195172188.003.0028.
- **State:** each partner's behaviour/state R(t), J(t) [abs].
- **Equations [read, via Bielczyk et al. eq. 2, which cites it as ref 6]:** `R' = c[R* - R] + d[J - R]`, `J' = e[J* - J] + f[R - J]`. R*, J* are each person's ideal. c, e: pull to own ideal; d, f: pull toward matching the partner. Coefficients may be negative (contrarian, cooperator).
- **Derived results:** equilibrium is a compromise between own ideal and partner's; both cooperative gives approach to equilibrium; an uncooperative partner often (not always) gives instability; mutual cooperation can be stable yet unsatisfying [abs].
- **Standing:** the 1999 paper fitted the model to data (fit details not seen); the 2006 chapter applies it. Later literature treats it as foundational [abs].
- **Translation:** this is the cleanest form of the "set point plus partner" skeleton: attractor to own ideal and attractor to partner's current state. **Operator:** `match(i, j)` with gain d; **operand:** state and ideal per person.

## 4. Delay models and a triad: Bielczyk, Foryś and Płatkowski

- **Citation:** Bielczyk, Foryś and Płatkowski, "Dynamical models of dyadic interactions with delay", arXiv:1202.2338 (2012). Read in full. Journal version (confirmed in validation): *J. Mathematical Sociology* 37(4):223-249 (2013), doi 10.1080/0022250x.2011.597279. Companion: Bielczyk, Bodnar and Foryś (2012), "Delay can stabilize: love affairs dynamics", *Applied Mathematics and Computation* 219:3923-3937, doi 10.1016/j.amc.2012.10.028.
- **Equations [read]:** `r' = a11 r(t-τ11) + a12 j(t-τ12)`, `j' = a21 r(t-τ21) + a22 j(t-τ22)` (their eq. 4).
- **Theorems [read; re-checked in validation]:** with one delay, for `|a12 a21| < |a11 a22|` there is at most one stability switch (Thm 1); for `|a12 a21| > |a11 a22|` and suitable parameter intervals, any number n of stability switches exist (Thm 2), via Hopf bifurcation. For the form where only the partner's state is delayed (their system 6), Thm 3 gives no switches when `|a12 a21| < |a11 a22|` and at most one otherwise. Remark 2: adding a delay to Strogatz's centre makes the states diverge except for a measure-zero set of delays. Their reading: the joint strength of reactions to the *partner* matters more than to oneself; multiple switches need a partner who reacts with delay to *their own* state. A delay can stabilise an unstable relationship.
- **Triad [read]:** adds a third person (Paris) with R and P not interacting, Juliet linking both (eqs. 23-24); with equal self-attitudes in R and P, the triad reduces to a dyad with an "averaged" man `s = a21 r + a23 p` and at most one switch. Without that symmetry they construct a triad (system 24) with **three** stability switches, so the reduction is conditional [read]. Their ref 1 for 3-person models without delay is Bagarello and Oliveri (2010), below.
- **Standing:** pure mathematics, no data. **Value for us:** a worked 2-to-3 step (not the only one: see 4b and Rinaldi), and the averaging reduction is the sort of theorem we want: *an aggregate of partners with equal self-attitude acts as one partner*.

## 4b. Beyond two: Liebovitch et al. conflict models and Bagarello's operator models (added in validation)

- **Liebovitch, Naudot, Vallacher, Nowak, Bui-Wrzosinska and Coleman (2008)**, "Dynamics of two-actor cooperation-competition conflict models", *Physica A* 387(25):6360-6378, doi 10.1016/j.physa.2008.07.020 [read, accepted manuscript]. A continuous version of the Gottman skeleton explicitly: `x' = m1 x + b1 + c1 tanh(y)`, `y' = m2 y + b2 + c2 tanh(x)`, with `m < 0` the "inertia", `b` the uninfluenced state, and the sign of `c` meaning cooperation (+) or competition (-). Results: feedback weaker than inertia (`|c| < |m|`) leaves both actors neutral; for `c1 c2 > 1` (rescaled) a **pitchfork bifurcation** creates two attractors (both positive or both negative); **Theorem 1: no limit cycles** for two actors (Lyapunov argument in the competitive case). **Section 3.7, 3-10 actors (numerical, preliminary):** with all-negative feedback the network **spontaneously splits into two camps** of opposite emotional state, the neutral point being a higher-dimensional saddle; mixed feedback gives transient oscillations. A worked n > 2 result in this exact skeleton, which the first draft said did not exist. Follow-up: Rojas-Pacheco, Obregón-Quintana, Liebovitch and Guzmán-Vargas (2013), *Physica A* 392(3):458-467, doi 10.1016/j.physa.2012.09.021 (delay gives oscillations); an N-actor network version exists in conference slides (Fernández Rosales, Liebovitch, Guzmán-Vargas 2013) [title only].
- **Bagarello and Oliveri (2010)**, "An operator-like description of love affairs", *SIAM J. Appl. Math.* 70(8):3235-3251, doi 10.1137/10079985x [abs, Crossref]. Uses the **occupation-number representation** from quantum mechanics: love levels are eigenvalues of number operators, dynamics generated by a Hamiltonian [abs; the Hamiltonian's form std, not opened]. Two actors: periodic (linear) or periodic/quasi-periodic (nonlinear) solutions; then a **love triangle** (Alice, Bob, Carla) with analytical conditions for periodic vs quasi-periodic solutions in the linear case [abs]. Of direct interest for an *algebra*: it is the one line in this survey where the people and interactions are operators in an algebra, not coefficients. Same authors extend it to crowds and ecosystems (Bagarello, Gargano, Oliveri 2015, doi 10.1016/j.apm.2014.10.038).

## 5. Boker and Laurenceau: coupled damped oscillators

- **Citations:** Boker and Laurenceau (2006), "Dynamical systems modeling: an application to the regulation of intimacy and disclosure in marriage", in *Models for Intensive Longitudinal Data*, Oxford, doi 10.1093/acprof:oso/9780195173444.003.0009 pp. 195-218. Boker and Laurenceau (2007), "Coupled dynamics and mutually adaptive context", in Little, Bovaird and Card (eds.), *Modeling Contextual Effects in Longitudinal Studies*, Erlbaum (book doi 10.4324/9780203936825; chapter not separately resolved). Method foundation (confirmed in validation): Boker and Nesselroade (2002), "A method for modeling the intrinsic dynamics of intraindividual variability: recovering the parameters of simulated oscillators in multi-wave panel data", *Multivariate Behavioral Research* 37(1):127-160, doi 10.1207/s15327906mbr3701_06. *(Correction: it is a single-person damped-oscillator estimation method, not a coupled-oscillator paper as the first draft implied.)*
- **State:** daily self-reported intimacy/disclosure per partner, and its first and second derivatives (estimated by local linear approximation) [abs].
- **Equations:** not read at source (the vignette URL 404ed). Standard [std]: per person, `x'' = η x + ζ x' + (coupling) y + (coupling) y'`, where η < 0 is the frequency/restoring term pulling toward equilibrium, ζ < 0 is damping, and the partner's displacement (and sometimes velocity) enters additively. Damping decides between **co-regulation** (return to a set point after disruption) and **co-dysregulation** (growing volatility) [abs, rties vignette summary].
- **Empirical:** fitted to daily diaries and physiology: couples' daily affect (Steele and Ferrer 2011, "Latent differential equation modeling of self-regulatory and coregulatory affective processes", *Multivariate Behavioral Research* 46(6):956-984, doi 10.1080/00273171.2011.625305, DOI confirmed in validation), intimacy (Boker and Laurenceau 2006) [abs]; Helm, Sbarra and Ferrer (2012), "Assessing cross-partner associations in physiological responses via coupled oscillator models", *Emotion* 12(4):748-762, doi 10.1037/a0025036, coupled linear oscillators on respiration and heart rate over three lab tasks. Ferrer and Helm (2013), *Int. J. Psychophysiology* 88:296-308, doi 10.1016/j.ijpsycho.2012.10.013, "Dynamical systems modeling of physiological coregulation in dyadic interactions" (year of publication 2013 on Crossref; the 2012 on the ScienceDaily page is the online date). Standing: parameters estimable; effects modest and context-dependent [abs]; no predictive validation I found.
- **Attachment as a moderator of coupling (missing from the first draft):** Butner, Diamond and Hicks (2007), "Attachment style and two forms of affect coregulation between romantic partners", *Personal Relationships* 14:431-455, doi 10.1111/j.1475-6811.2007.00164.x [title only]: attachment style moderating dyadic affect coupling in daily data, the empirical counterpart to treating attachment as a coupling gain.
- **Translation:** the operand has a *rate* as well as a level, so a person's state is (x, x'). The partner's term is a linear coupling operator; for one uncoupled oscillator, the fixed point is stable iff the damping coefficient ζ is negative (with coupling, stability is a property of the 4x4 system, not of each ζ alone). This is the nearest to an "equation of drives" for affect.

## 6. Butler: emotional coregulation and TIES

- **Citation:** Butler and Randall (2013), "Emotional coregulation in close relationships", *Emotion Review* 5(2):202-210, doi 10.1177/1754073912451630 (online 2012). Framework: Butler (2011), "Temporal interpersonal emotion systems: the 'TIES' that form relationships", *Personality and Social Psychology Review* 15(4):367-393, doi 10.1177/1088868311411164 (DOI confirmed in validation). Computational follow-up: Butler et al. (2017), "Computational temporal interpersonal emotion systems", in *Computational Social Psychology*, doi 10.4324/9781315173726-7 [title only].
- **Content:** coregulation = two-way linkage between partners' oscillating emotional channels, arousal and calming alternating so both stay in a healthy range. In the author reply, TIES describes people in an exchange as an interconnected system; coregulation is the state of **coupled damped oscillations converging on a stable level** [abs].
- **Equations:** conceptual; points to Boker-type oscillator models for the formalisation [abs]. **Standing:** theory paper; supporting data are physiological and diary studies.
- **Translation:** the interesting extra is that *regulation of fear/arousal* is the explicit target (calming), the closest any model gets to coupling a named drive.

## 7. Sbarra and Hazan: coregulation, dysregulation, attachment

- **Citation:** Sbarra and Hazan (2008), "Coregulation, dysregulation, self-regulation: an integrative analysis and empirical agenda for understanding adult attachment, separation, loss, and recovery", *Personality and Social Psychology Review* 12:141-167, doi 10.1177/1088868308315702.
- **Content [std]:** attachment bonds act as a physiological and behavioural regulatory system; proximity coregulates, separation produces dysregulation, then recovery via self-regulation. Verbal model, no equations. **Standing:** widely cited review; empirical agenda, not a tested model.
- **Translation:** gives the case for attachment as a *coupling gain* (how strongly one person's regulation depends on the other), and for "loss" as removing the coupling term.

## 8. Coan: social baseline theory as a coupling model

- **Citations:** Coan, Schaefer and Davidson (2006), "Lending a hand: social regulation of the neural response to threat", *Psychological Science* 17:1032-1039, doi 10.1111/j.1467-9280.2006.01832.x. Social baseline theory: Beckes and Coan (2011), "Social baseline theory: the role of social proximity in emotion and economy of action", *Social and Personality Psychology Compass* 5(12):976-988, doi 10.1111/j.1751-9004.2011.00400.x (confirmed in validation).
- **Finding [abs]:** 16 married women under threat of electric shock held their husband's hand, a stranger's hand, or nothing: spouse's hand gave pervasive attenuation of threat-related neural activation, stranger's hand more limited; marital quality moderated it. A 2020 test of the vmPFC mediation (n = 110) found no support for that mediator: Beckes, Medina-DeVilliers and Coan, "The social regulation of emotion: inconsistencies suggest no mediation through ventromedial prefrontal cortex", *Social Neuroscience* 16(1):6-17 (2021 issue), doi 10.1080/17470919.2020.1767686 [abs; title and DOI confirmed, n not checked].
- **Equation:** none. Verbal form [std]: the brain assumes proximity to others, so company lowers the cost (metabolic) of coping with a threat. As a coupling, it is a *fear-damping operator*: partner presence `P` multiplies down the threat response, `fear' = f(threat) * (1 - g(P, closeness))`.
- **Translation:** the only evidence here for a **specific drive (fear/threat) being modulated by a partner**. Operator: `presence(j → i)`, gain from relationship quality. Standing: replicable in small samples; the mechanism claim is contested.

## 9. Interpersonal synchrony: Kelso, HKB, Schmidt and Richardson

- **HKB:** Haken, Kelso and Bunz (1985), "A theoretical model of phase transitions in human hand movements", *Biol. Cybernetics* 51:347-356, doi 10.1007/bf00336922. Two coupled nonlinear oscillators reduce to one equation for the **relative phase** φ, with a potential having stable states at in-phase (φ=0) and anti-phase (φ=π) coordination; as movement frequency rises, anti-phase loses stability and switches to in-phase (a **bifurcation**) [abs/std]. **Confirmed in validation [read, Kelso (2008), "Haken-Kelso-Bunz model", *Scholarpedia* 3(10):1612, doi 10.4249/scholarpedia.1612]:** `φ' = -a sin φ - 2b sin 2φ`, potential `V(φ) = -a cos φ - b cos 2φ`; rescaled `φ' = -sin φ - 2k sin 2φ` with `k = b/a` falling as movement frequency rises. Both 0 and π are stable for `k > 0.25`; at `k_c = 0.25` anti-phase loses stability and the system switches to in-phase; the reverse switch does not occur (hysteresis).
- **Social extension:** Schmidt, Carello and Turvey (1990), "Phase transitions and critical fluctuations in the visual coordination of rhythmic movements between people", *J. Exp. Psychol: Human Perception and Performance* 16(2):227-247, doi 10.1037/0096-1523.16.2.227 (DOI, title and pages confirmed on Crossref). Two people swinging legs side by side show the same dynamics as inter-limb coordination [abs].
- **Review chapter:** Schmidt and Richardson (2008), "Dynamics of interpersonal coordination", in Fuchs and Jirsa (eds.), *Coordination: Neural, Behavioral and Social Dynamics*, Springer, pp. 281-308, doi 10.1007/978-3-540-74479-5_14. Also Richardson, Marsh, Isenhower et al. (2007), "Rocking together", *Human Movement Science* 26:867-891, doi 10.1016/j.humov.2007.07.002: intentional and unintentional coordination [abs].
- **State:** a phase, not an affect. **Theorems:** bifurcation and stability of relative-phase states; **standing:** strongest empirically of anything here (reproducible lab predictions, e.g. the switch), but about movement, not drives.
- **Translation:** the only model here where coupling gives *qualitative* predictions confirmed in the lab (which joint states are stable, when they switch) from a single equation; n-oscillator generalisations (Kuramoto) exist and are covered with theorems in survey 23.
- **Boker, Rotondo, Xu and King (2002)**, windowed cross-correlation for interpersonal synchrony, *Psychological Methods* 7:338-355, doi 10.1037/1082-989x.7.3.338: a measurement tool rather than a model.

## 10. Physiological linkage: Palumbo et al. 2017

- **Citation:** Palumbo, Marraccini, Weyandt, Wilder-Smith, McGee, Liu and Goodwin, "Interpersonal autonomic physiology: a systematic review of the literature", *Personality and Social Psychology Review* 21(2):99-141, doi 10.1177/1088868316628405 (Crossref gives 2016 online; the issue is 2017).
- **Content [abs]:** reviews studies of the interdependence of two or more people's autonomic activity ("physiological synchrony"/"linkage"); aims to standardise terms and flags theoretical, methodological and statistical problems. It is a review, not a model.
- **Value:** the measured thing (heart rate, skin conductance, respiration) is the nearest to a *drive-adjacent* state we can observe in both partners, and the review says analysis methods disagree. Tools: McAssey, Helm, Hsieh et al. (2013), *Methodology* 9:41-53, doi 10.1027/1614-2241/a000053 (methods for detecting synchrony) [abs].

## 11. Vallacher, Nowak: dynamical social psychology

- **Citations:** Vallacher and Nowak (2008), "The dynamics of human experience: fundamentals of dynamical social psychology", in Guastello, Koopmans and Pincus (eds.), *Chaos and Complexity in Psychology*, Cambridge, pp. 370-401, doi 10.1017/cbo9781139058544.013; Vallacher, Coleman and Nowak (2011), "Dynamical systems theory: applications to peace and conflict", doi 10.1002/9780470672532.wbepp093.
- **Content [std/abs]:** attractors, coupling and self-organisation as the concepts for social judgement, relationships and conflict (intractable conflict as a strong attractor). Mostly framework and cellular-automaton simulations (social impact theory and the Nowak line), few fitted equations. I did not open it. A partial overlap with survey 05 (opinion dynamics).

## 12. Sadler et al.: interpersonal complementarity dynamics

- **Citation:** Sadler, Ethier, Gunn, Duong and Woody (2009), "Are we on the same wavelength? Interpersonal complementarity as shared cyclical patterns during interactions", *J. Personality and Social Psychology* 97:1005-1020, doi 10.1037/a0016232. Review chapter: Sadler, Ethier and Woody (2010), doi 10.1002/9781118001868.ch8.
- **State:** two continuously coded dimensions per person, **dominance and warmth** (the interpersonal circumplex), rated by observers with joysticks (CAID method) [abs].
- **Result [abs]:** complementarity is **correspondence on warmth, reciprocity (opposition) on dominance**; partners alter behaviours in complementary ways. Cyclical patterns shared by partners are the unit. Equations: not seen (dynamic regression/oscillator style estimation [std]).
- **Translation:** the only empirical result that says the **coupling sign differs by dimension**: warmth matches, control complements. For our algebra: operators on a 2D state, with a sign matrix.

## 13. Kenny's Actor-Partner Interdependence Model (APIM)

- **Citation:** Cook and Kenny (2005), "The Actor-Partner Interdependence Model: a model of bidirectional effects in developmental studies", *Int. J. Behavioral Development* 29:101-109, doi 10.1080/01650250444000405. Book: Kenny, Kashy and Cook (2006), *Dyadic Data Analysis*, New York: Guilford (no DOI; existence confirmed in validation by two reviews with DOIs, Coryn 2007, doi 10.1177/1098214007300894, and Newman 2008, doi 10.1177/1094428108324689).
- **Form [std]:** `Y1 = a·X1 + p·X2 + e1`, `Y2 = a·X2 + p·X1 + e2`; **actor effect** a (own predictor on own outcome), **partner effect** p, and correlated residuals. With repeated measures, lagged versions give cross-lagged panel (actor and partner autoregression), the discrete form of the Gottman skeleton with a linear influence function.
- **Standing:** the standard statistical tool; tests whether partner effects exist and are equal, with no dynamics (no set point, no stability result), so it estimates the coupling gain, not the law.
- **Translation:** it supplies the **vocabulary actor/partner**, and a ready estimation method for the linear-gain version of any operator in this note.

---

## Common coupling skeleton

For persons i = 1..n with scalar state x_i (affect, love, positivity, arousal):

`x_i(t+1) = x_i(t) + α_i (s_i − x_i(t)) + Σ_{j≠i} C_ij(x_j(t))`  (discrete)
`x_i' = α_i (s_i − x_i) + Σ_j C_ij(x_j)`  (continuous)

with three ingredients in every model:
1. **Self term:** inertia/persistence or damping toward an own **set point/ideal** s_i (Gottman r and w, Rinaldi forgetting, Felmlee R*, Boker η/ζ, Butler's stable level).
2. **Coupling operator C_ij:** how j's state pushes i. Variants: constant gain (Strogatz, Felmlee, APIM, Boker: linear); **bilinear or thresholded ogive** (Gottman), plus Gottman's later **trigger terms** (repair/damping) that fire on the receiver's own threshold; **saturating tanh** (Liebovitch); **operator-valued** (Bagarello); **non-monotone** reaction function (Rinaldi insecure); **phase-lag** (HKB); **delayed** (Bielczyk).
3. **Parameters live on the person and the ordered pair,** not the state: the "personality" is the operator's shape and gain.

Common derived results: fixed points and their stability from the 2x2 Jacobian; oscillation (centre/limit cycle) when cross-coupling signs are opposite; loss of stability when the cross-gain product outweighs the self-damping product (det A = a11 a22 - a12 a21 turning negative in the undelayed linear case; Bielczyk's `|a12 a21|` vs `|a11 a22|` comparison plays the analogous role for how many delay-induced switches can occur; Liebovitch's pitchfork at `c1 c2 = 1` is the nonlinear version).

## Which drives have been coupled

| Drive / state | Coupled between people? | Where |
|---|---|---|
| Affect (valence) | Yes, equations and data | Gottman-Murray, Boker, Felmlee, APIM, Butler |
| Love / liking (a desire-like or attachment-like scalar) | Yes, equations; little data; triangles too | Strogatz, Rinaldi, Sprott, Bagarello-Oliveri |
| Conflict state (cooperation/competition) | Yes, equations, 2 to 10 actors, no data | Liebovitch et al. 2008 |
| Arousal / physiology | Yes, data and oscillator fits | Palumbo review, Ferrer and Helm, Helm et al. |
| Fear / threat | Dyad: only one-way damping by a partner's presence (no equation). Group: fear contagion with equations and a crowd test | Coan; ASCRIBE (Bosse et al. 2013), Tsai et al. 2013 (surveys 18, 23) |
| Attachment | As a parameter (coupling gain), never a state | Rinaldi (secure/insecure), Sbarra-Hazan |
| Desire as such, curiosity | **No** between-person model found (searched only in passing in validation) | none |
| Dominance and warmth | Yes, observational dynamics | Sadler |
| Movement phase | Yes, strongest data | HKB, Schmidt-Richardson |

## What exists vs what does not

**Exists:**
- A well-understood two-person template (self term plus coupling operator), with nonlinear thresholds, delay and oscillation all studied, and fixed-point/stability/bifurcation results for the 2-variable case.
- Fitting methods for dyad time series (difference equations, oscillators, APIM), and one strong lab result for coupling-induced bifurcation (HKB).
- A qualitative vocabulary of personalities as operator shapes (eager beaver, cautious, secure, insecure).

**Does not exist (in what I found):**
- **Any *dyadic* model of fear, desire or curiosity as separate coupled drives.** Dyad models couple a single valence scalar. (Group-scale fear contagion does exist: surveys 18 and 23.)
- **n > 2 theory beyond small cases:** three-person models with equations (Bielczyk delay triads, Bagarello-Oliveri, Dercole-Rinaldi, Sprott) and 3-10 actor numerics (Liebovitch et al. 2008) exist, plus one conditional aggregation result (Bielczyk's averaged partner). No general n-person theorem, no fitted network version of Gottman.
- **Composition laws:** no result says how two coupling operators compose (C_ij after C_jk), nor an algebra of them. The operators are parameterised functions, not elements of a structure.
- **Trusted prediction.** The critique showed on other data that divorce-prediction accuracy collapses under cross-validation and realistic base rates, and the 1998 affective-process variables failed one independent test (with a published dispute over that sample). The difference-equation parameters themselves have not been tested out of sample. Control claims exist only as therapy rationale (e.g. lower the negativity threshold).
- **Population-level parameter values.** Models are fitted per couple; I found no table of typical set points, inertias or influence functions across couples.

**Take for the algebra:** the skeleton is adoptable as written, and the right move is to generalise the single scalar to a vector of drives, the pairwise operator to an n x n family, and to treat "personality" as the operator's shape. Nothing in this literature has done the vector-of-drives step, so it would be new work, not a port. Two precedents to read before building: Bagarello and Oliveri's operator formalism (people and interactions as operators, not coefficients) and Liebovitch et al.'s n-actor tanh model (the Gottman skeleton on a network).

---

## Unconfirmed

- Sign of the Gottman negativity-threshold finding: Murray says divorcing newlyweds had the "lower negative threshold"; blogs and popular accounts say stable couples did. Needs Gottman, Swanson and Murray (1999) or the book.
- Gottman FAQ statements (93.6% figure, "six of seven studies"): from the first draft's reading of gottman.com, not re-opened.
- Rinaldi personality classes (secure, insecure, biased) and their equations: IIASA blog and abstracts only.
- Boker-Laurenceau second-order coupled equation and the partner-velocity term: standard account only (no open copy of Boker and Laurenceau 2006, Helm et al. 2012 or Steele and Ferrer 2011 was reachable). Boker and Laurenceau (2007) chapter: book DOI only.
- Strogatz's own type names (narcissistic nerd, hermit): from two secondary course pages, book not opened.
- Heyman and Slep numeric figures (528 people; PPV 65% to 29%, 21% at 16% base rate): one secondary write-up only; abstract read, paper not opened.
- Stanley et al. on Gottman's reliability: query returned nothing relevant; not cited.
- Sprott (2004) "Dynamical models of love", *NDPLS* 8(3): no DOI found on Crossref; existence from citations and the author's lecture slides.
- Bagarello and Oliveri (2010): abstract only; Hamiltonian form not seen.
- Liebovitch et al. N-actor network extension (Fernández Rosales et al. 2013 slides): title only.
- Sadler 2009 abstract details and estimation method: title/DOI confirmed, abstract not seen.
- Vallacher and Nowak content: from titles only.
- Sbarra and Hazan content: from the standard account.
- Coan et al. 2006 sample (16 married women) and the 2020 test's n = 110: from abstracts/search summaries.

## Validation log (2026-10-29)

Every DOI in the file was resolved on Crossref; all resolved to the stated work.

- Cook, Tyson, White, Rushe, Gottman and Murray 1995 (*J. Family Psychology* 9(2):110-130): ✓ (the validation brief's "J. Math. Psychol." was wrong; the file was right)
- Gottman, Swanson and Swanson 2002 (*PSPR*): ✓
- Gottman, Murray et al. 2002, *The Mathematics of Marriage*: ✓ citation; ✎ equations corrected: husband's influence term is `I_WH(W_{t+1})`, not `I_WH(W_t)` (read in Murray ch. 5); influence-function forms (bilinear, piecewise-constant ogive) now from source; repair/damping terms added (Gottman et al. 2003)
- Gottman negativity-threshold claim ("good couples had a low threshold"): ✎ contradicted by Murray's text; moved to Unconfirmed as contested
- Gottman, Coan, Carrere and Swanson 1998 (*JMF* 60(1):5-22): ✓
- Heyman and Smith Slep 2001: ✓ citation and abstract read; ✎ added that it uses other data and names Gottman et al. 1998; numbers stay unconfirmed
- Kim, Capaldi and Crosby 2007: ✓ (85 couples, ~2.5 years, null results confirmed from abstract); ✎ added Coan and Gottman 2007 reply and Kim and Capaldi 2007 rejoinder
- Strogatz 1988 (*Math. Magazine* 61(1):35): ✓; equations ✓ via Bielczyk; ✎ type names: "narcissus" and "stoic" are Bielczyk's coinages, Strogatz's are narcissistic nerd and hermit
- Strogatz 1994 book pp. 138-140: ? not opened (citation via Bielczyk)
- Rinaldi 1998 Laura and Petrarch (*SIAM J. Appl. Math.* 58(4)): ✓; ✎ equations now read at source (forgetting, cubic reaction, appeal damped by inspiration 1/(1+δZ))
- Rinaldi and Gragnani 1998 (*NDPLS* 2(4)): ✓ citation; personality classes ?
- Felmlee and Greenberg 1999: ✓; equations ✓ via Bielczyk eq. 2 (secondary)
- Felmlee 2006 chapter: ✓ (pp. 409-422 added)
- Bielczyk, Foryś and Płatkowski: ✓ theorems re-checked; ✎ journal version found (*J. Math. Sociol.* 37:223-249, 2013); ✎ triad: averaging needs equal self-attitudes, and an asymmetric triad has three switches; ✎ partner-delay theorem stated fully
- Boker and Laurenceau 2006: ✓; equation ? (standard account)
- Boker and Laurenceau 2007: ✎ book located, chapter DOI not found
- Boker and Nesselroade 2002: ✎ resolved (*MBR* 37(1):127-160); it is a single-oscillator method paper, not coupled oscillators
- Steele and Ferrer 2011: ✎ resolved (*MBR* 46(6):956-984)
- Helm, Sbarra and Ferrer 2012: ✓ (volume and pages added)
- Ferrer and Helm 2013: ✓
- Butler and Randall 2013: ✓
- Butler 2011 TIES: ✎ resolved (*PSPR* 15(4):367-393)
- Sbarra and Hazan 2008: ✓ citation; content ? (standard account)
- Coan, Schaefer and Davidson 2006: ✓
- Beckes and Coan 2011: ✎ resolved (*SPPC* 5(12):976-988)
- Beckes, Medina-DeVilliers and Coan 2020: ✎ title, DOI and venue added
- Haken, Kelso and Bunz 1985: ✓; ✎ potential and equation of motion confirmed at source (Kelso 2008 Scholarpedia), critical k = 0.25 added
- Schmidt, Carello and Turvey 1990: ✓ (pages confirmed)
- Schmidt and Richardson 2008: ✓ (editors, pages added)
- Richardson et al. 2007: ✓
- Boker, Rotondo, Xu and King 2002: ✓
- Palumbo et al. 2017: ✓
- McAssey et al. 2013: ✓
- Vallacher and Nowak 2008: ✓ (book and pages added); content ?
- Vallacher, Coleman and Nowak 2011: ✓
- Sadler et al. 2009, Sadler, Ethier and Woody 2010: ✓ citations; estimation method ?
- Cook and Kenny 2005: ✓; APIM form ✓ (standard, uncontroversial)
- Kenny, Kashy and Cook 2006: ✎ confirmed as a Guilford book via two reviews
- Gottman FAQ: ? not re-opened
- Summary claim "no between-person model of fear": ✎ narrowed to dyads; fear contagion models with equations exist at group scale (surveys 18 and 23)
- Summary claim "nothing beyond n = 2 bar one delay example": ✎ wrong; triangles with equations (Bagarello-Oliveri 2010, Dercole-Rinaldi 2014, Sprott 2004) and 3-10 actor numerics (Liebovitch et al. 2008) exist
- Fabrications: none found; nothing removed

**Added as missing:** Gottman, Swanson and Murray 1999 (the newlywed model fit); Murray *Mathematical Biology I* ch. 5; Gottman et al. 2003 (repair/damping); Coan and Gottman 2007; Kim and Capaldi 2007; Liebovitch et al. 2008 and Rojas-Pacheco et al. 2013; Liebovitch et al. 2011 and Peluso et al. 2012 (therapist-client reuse of Gottman's model); Bagarello and Oliveri 2010; Rinaldi 1998 linear couples; Dercole and Rinaldi 2014; Rinaldi et al. 2015 monograph; Sprott 2004; Butner, Diamond and Hicks 2007; Butler 2011 and Butler et al. 2017; Bielczyk, Bodnar and Foryś 2012; Kelso 2008.

**Verdict.** Bibliographically reliable: every DOI resolved to the stated work and nothing was fabricated. The equations were less safe. The one the algebra would most likely copy, Gottman-Murray, was taken from a blog with the husband's lag wrong, and one headline finding (which couples have the low negativity threshold) is contradicted by the model's co-author. The survey's two strongest "does not exist" claims, nothing beyond two people and no coupled fear, were too broad: n-person models with equations exist and fear contagion is modelled at group scale, though n-person theorems and fitted n-person models are still absent.
