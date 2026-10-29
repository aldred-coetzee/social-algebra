# Prior work 061: the coupled damped oscillator, its partner-velocity term, and HKB

Direction: D191

Date: 2026-10-29. Survey for the social-algebra strand. Question: what do the two coupling parameters of the coupled damped linear oscillator (partner displacement, partner velocity) mean, and how does that relate to the Haken-Kelso-Bunz (HKB) coupling-induced bifurcation? Builds on file 20 section 5 and section 9, which had these as standard account only.

**Method and honesty note.** Primary Boker & Laurenceau 2006/2007, Steele & Ferrer 2011 and Helm, Sbarra & Ferrer 2012 are paywalled and were NOT read; none has an open copy I could reach. What was read at source this session, via NCBI efetch full text and GitHub raw files:
- Hu, Boker, Neale & Klump (2014), author manuscript PMC7480173: states the single and coupled oscillator equations and interprets every parameter, with simulations. Boker is a co-author, so this is the closest primary statement of the Boker model available.
- Butler & Kuelz, `rties` R package vignette `coupled_oscillator_V05` (raw Rmd from github.com/cran/rties): states the dyadic model, with partner displacement and partner velocity terms and their interpretation.
- Slowinski, Al-Ramadhani & Tsaneva-Atanasova (2020), PMC6986925: HKB oscillator and coupling function, with delays.
- Avitabile, Slowinski, Bardy & Tsaneva-Atanasova (2016), PMC4903117: full HKB system, bifurcation analysis.
- Ferrer & Steele 2010 conference slides (CILVR, PDF): Greek letters were lost in text extraction, so only the equation shape is usable.
- Kelso (2008), "Haken-Kelso-Bunz model", *Scholarpedia* 3(10):1612: read at source in the 2026-10-29 validation pass (fetched with the expired certificate ignored).
Tags: [read] = read at source named; [derived] = my own algebra from [read] equations, checked for consistency with the sources but not published by them; [std] = standard account, not checked.

**Summary.** (1) The "partner-velocity term" is real and has a clean reading: in `x'' = eta*x + zeta*x' + gamma_x*y + gamma_xdot*y'`, the partner's displacement shifts frequency/phase, the partner's velocity shifts damping/amplification, and in a symmetric dyad velocity coupling adds directly to the damping of the sum and difference modes. So it can turn a co-regulating dyad into a co-dysregulating one [derived]. (2) HKB's coupling term `(a + b(x1-x2)^2)(x1' - x2')` is a velocity-difference coupling, the same family; the HKB bifurcation is a result about two nonlinear oscillators and a frequency control parameter, not a property of the linear model; HKB 1985 itself found linear position or velocity coupling inadequate to produce it (per Kelso 2008). (3) The linear model has no bifurcation of its own; the only qualitative regime change is the sign of damping. (4) Evidence that coupling terms improve prediction of real affect/physiology is thin and mostly in-sample.

---

## 1. Single damped linear oscillator (the self term)

**Source.** Hu, Boker, Neale & Klump (2014), "Coupled latent differential equation with moderators: Simulation and application", *Psychological Methods* 19(1):56-71, doi 10.1037/a0032476 (DOI resolved on Crossref; Crossref gives the published title, the PMC author manuscript is titled "Latent Differential Equation with Moderators: Simulation and Application"). [read, PMC7480173]

Equation 1 [read]: `x'' = eta*x + zeta*x' + e`, with x the displacement from equilibrium, `eta` the regression coefficient of x on x'', `zeta` that of x' on x''.

Their stated interpretation [read, verbatim in substance]:
- `eta` is the frequency parameter. "In a self-regulation system, eta is a negative number, indicating that when the system is away from its equilibrium, it will accelerate towards the equilibrium. If eta is a positive number, no regulation occurs."
- `zeta` is the damping parameter. `zeta < 0`: oscillation fades; `zeta = 0`: constant amplitude; `zeta > 0`: amplitude grows.
- Oscillation requires `eta < 0` and `eta + zeta^2/4 < 0` (their wording). Period (Equation 2): `lambda = 2*pi / sqrt(-(eta + zeta^2/4))`.
- Note the sign convention: negative `eta` and negative `zeta` mean regulation and damping. The sign flip against the textbook form `x'' + c x' + k x = 0` (c, k > 0) is a source of confusion; here `eta = -k`, `zeta = -c`.
- The equilibrium is assumed constant; a non-constant equilibrium must be modelled first and the oscillator fitted to residuals [read, Hu et al. citing Boker & Bisconti 2006].

## 2. Coupled form: partner displacement and partner velocity

**Hu et al. Equation 4** [read], unidirectional coupling of x onto y:

    x'' = eta_x * x + zeta_x * x' + e_x
    y'' = eta_y * y + zeta_y * y' + gamma_x * x + gamma_xdot * x' + e_y

The same paper describes the bidirectional case as two single oscillators plus coupling terms in both directions (their Figure 3, image not read) and calls the gammas "the intrinsic regulation of each variable, as well as the extrinsic drive from the other variable".

**rties vignette** (Butler & Kuelz, `rties` package) [read] fits, per dyad and per partner type, the regression of the second derivative on four terms: own state, own first derivative, partner state, partner first derivative, with no intercept, giving 8 parameters. Its labels:
- own state: "related to the frequency of oscillations"
- own first derivative: "damping/amplification"
- partner state: "coupling with respect to frequency"
- partner first derivative: "coupling with respect to damping/amplification"
Negative own-derivative = damping, "the tendency for the state variable to converge back to homeostatic levels"; positive = amplification; zero = constant amplitude. It defines co-regulation as partners' mutual influence having "a homeostatic effect, resulting in both partners returning to a stable set-point following some disruption", and co-dysregulation as influence that "results in increasingly volatile fluctuations away from a set-point" (citing Butler & Randall 2013; Reed, Barnard & Butler 2015).

**Ferrer & Steele 2010 slides** [read, equation shape only]: the Boker & Laurenceau (2006) model is shown as two equations, one per partner, each with own-displacement and own-velocity terms plus a parenthesised sum of partner-displacement and partner-velocity terms. Greek symbols lost in extraction; the structure matches Hu Eq. 4 made symmetric. Not a transcription of the original.

**Original Boker & Laurenceau equations** are NOT read. File 20 and this file rely on Hu et al. and rties as downstream statements of the same model. Treat as likely identical in form, unconfirmed in detail (the original may constrain or parameterise the couplings differently).

## 3. What the coupling parameters mean

**Hu et al. simulation results** [read]:
- `gamma_x = 0, gamma_xdot > 0`: "phase synchronizing effect of x on y (0 degree offset)". `gamma_xdot < 0`: "phase desynchronizing effect (180 degree offset)". Magnitude sets how fast y is (de)synchronised.
- `gamma_xdot = 0, gamma_x > 0`: "y is dragged back by x (270 degree offset)"; `gamma_x < 0`: "pushed forward by x (90 degree offset)".
- Both nonzero: an offset set by the signs and relative sizes.

**Derived check** [derived]. Drive y with x = cos(w t) and solve the steady state of the y equation: y = Re[H e^{iwt}] with `H = (gamma_x + i w gamma_xdot) / (-w^2 - eta_y - i w zeta_y)`. At resonance (`w^2 = -eta_y`), with damped `zeta_y < 0`, the denominator is `+i w |zeta_y|` (phase +90 degrees). A velocity coupling `gamma_xdot > 0` has numerator phase +90 degrees, so net 0 degrees: in phase, as Hu et al. report. A pure displacement coupling `gamma_x > 0` has numerator phase 0, net -90: y lags x by a quarter cycle, which is Hu's "dragged back" (their 270 is the same thing as -90). Agreement is at resonance only; away from resonance the offsets differ and Hu's statements are simulation descriptions, not general.

**Reading for an algebra.**
- Partner displacement = the partner's current level pulling my acceleration, i.e. a shared restoring force (spring). In the symmetric case it changes the modes' frequency parameters and phase but not their damping coefficients [derived, Section 4]; it is not energy-neutral in general (Section 4 shows it can still destabilise a mode, and a one-way spring coupling can do net work on the driven partner).
- Partner velocity = the partner's rate of change pushing my acceleration, i.e. a shared friction (or anti-friction) term. It changes damping, the energy balance.

## 4. Stability under coupling (derived)

[derived] Take the symmetric bidirectional case, same parameters both sides:

    x'' = eta*x + zeta*x' + gamma*y + g*y'
    y'' = eta*y + zeta*y' + gamma*x + g*x'

Sum and difference modes decouple: `u = x + y` obeys `u'' = (eta + gamma) u + (zeta + g) u'`; `v = x - y` obeys `v'' = (eta - gamma) v + (zeta - g) v'`. Each is a single damped oscillator, so by the Section 1 rules both modes are stable iff `zeta + g < 0`, `zeta - g < 0`, `eta + gamma < 0`, `eta - gamma < 0`, i.e. `zeta + |g| < 0` and `eta + |gamma| < 0`.

Consequences (all [derived], valid only in the symmetric linear case):
- A dyad whose members are each individually damped (`zeta < 0`) is co-regulating only if `|g| < |zeta|`. Beyond that one mode amplifies: co-dysregulation. The in-phase mode has coefficient `zeta + g` and the anti-phase mode `zeta - g`, so `g > 0` makes the in-phase mode the less damped (the first to amplify) and `g < 0` does the same for the anti-phase mode. Positive velocity coupling therefore favours in-phase synchrony persisting and negative favours anti-phase, consistent with the Hu et al. sign results.
- Displacement coupling shifts the mode frequencies to `eta +/- gamma` and splits them: the two modes oscillate at different frequencies, producing beating. It can also destabilise: if `eta + |gamma| >= 0`, one mode has no restoring force.
- The asymmetric case (different damping and couplings per partner) mixes the modes; stability then requires the characteristic polynomial of the 4-dimensional system, not derived here.
- There is no bifurcation in the HKB sense here; the model is linear, so the qualitative change is the sign flip of a mode's damping, i.e. a Hopf-type loss of stability of the equilibrium at `zeta +/- g = 0`. The oscillator then grows without bound (no limit cycle). Real data cannot grow without bound, so a linear fit of an amplifying dyad is a local approximation only.

Identifiability caveat [read, Hu et al.]: "When eta_x = eta_y, the estimation breaks down" because with equal intrinsic frequencies one cannot tell coupling from two similar self-regulations. Accurate estimation held only for `gamma_xdot` in roughly -0.1 to 0.1 and `gamma_x` in roughly -0.02 to 0.02 at `eta` about -0.05, with `gamma_x` systematically over-estimated. These ranges are specific to their simulated condition (stated by them). The practical meaning: partner coupling is estimable only when the partners' own tempos differ and the coupling is smaller than the self-regulation.

## 5. HKB: coupling-induced bifurcation

**Haken, Kelso & Bunz (1985)**, "A theoretical model of phase transitions in human hand movements", *Biological Cybernetics* 51:347-356, doi 10.1007/BF00336922 (resolved on Crossref; the paper itself was not read). Equations below are read in the open follow-up papers.

**Oscillator and coupling** [read, Avitabile et al. 2016, *Biol. Cybern.* 110:201-216, doi 10.1007/s00422-016-0691-9; and Slowinski et al. 2020, *SIAM J. Appl. Dyn. Syst.* 19, doi 10.1137/19M1279381]:

    x1'' + x1'(alpha*x1^2 + beta*x1'^2 - gamma) + omega^2 * x1 = I12
    x2'' + x2'(alpha*x2^2 + beta*x2'^2 - gamma) + omega^2 * x2 = I21
    I12 = (a + b*(x1 - x2)^2) * (x1' - x2')
    I21 = (a + b*(x2 - x1)^2) * (x2' - x1')

The self term is a hybrid Van der Pol (alpha) and Rayleigh (beta) nonlinear damping, with `gamma` the linear (anti-)damping: a limit-cycle oscillator, not the linear damped oscillator of Section 1. `omega` relates to the natural/pacing frequency. The coupling is a function of the velocity difference, scaled by a linear (a) and a quadratic (b) function of the position difference. So it is a partner-velocity term, with a state-dependent gain. For comparison, the Boker-style term is partner velocity with constant gain, entering at the same place (acceleration). Slowinski et al. use this form with delays: `(x_i'(t) - x_j'(t - tau_j))(a + b(x_i(t) - x_j(t - tau_j))^2)` [read]; they credit the coupling to HKB 1985, the delayed version to Varlet et al. (2012, *PLoS One* 7:e29772) and its analysis to Słowiński, Tsaneva-Atanasova & Krauskopf (2016, *Eur. Phys. J. Spec. Top.* 225:2591-2600, doi 10.1140/epjst/e2015-50327-6, resolved). They fix alpha = 12.457, beta = 0.007095, gamma = 0.641 as "experimentally validated parameter values" [read], citing their [29] = Kay, Kelso, Saltzman & Schöner (1987), *J. Exp. Psychol. Hum. Percept. Perform.* 13:178-192, doi 10.1037/0096-1523.13.2.178 (resolved; values not checked in Kay et al.).

**Sign** [read, Avitabile et al., at their fixed intrinsic parameters]: in the (a, b) plane, first quadrant (both positive): "anti-phase coordination is the only stable state"; third quadrant (both negative): "in-phase oscillations are now stable, while anti-phase solutions are unstable"; phase-locked intermediate relative phases arise in the second and fourth quadrants (stable in the fourth, unstable in the second). So negative `a, b` is dissipative coupling on the velocity difference: it damps any difference between the two. In Section 4's notation, moving I12 into `x1'' = ...` gives a partner-velocity coefficient `g = -a` (and adds `+a` to own damping) [derived], so negative `a` is `g > 0`, the case Section 4 finds favours the in-phase mode. Consistent, not identical: HKB's gain is state-dependent and its self term is a limit cycle.

**Reduced relative-phase form** [read, Kelso (2008), *Scholarpedia* 3(10):1612, re-read in validation; equations restated in our own notation from Kelso (2008), Scholarpedia 3(10):1612, licence believed CC BY-NC-SA 3.0, not verified]: `phi' = -a sin(phi) - 2b sin(2phi)`, potential `V(phi) = -a cos(phi) - b cos(2phi)`, rescaled to `phi' = -sin(phi) - 2k sin(2phi)` with `k = b/a`; both in-phase (phi = 0) and anti-phase (phi = pi) stable for `k > 0.25`; at the critical `k_c = 0.25` anti-phase loses stability and the system switches to in-phase, with hysteresis. Kelso: `k` "corresponds to the cycle to cycle period", so it falls as movement frequency rises and frequency is the control parameter. Kelso also reports that HKB 1985 considered and rejected simpler couplings: "Linear couplings of position and its first order derivatives (velocity) are inadequate", so a constant-gain velocity coupling alone (the Boker-style term) does not produce the HKB transition. Reduction by slowly varying amplitudes and rotating-wave approximation [read, Avitabile et al.: "all previous studies have followed a line of analysis based on slowly varying amplitudes and rotating wave approximations"]. The a and b of the reduced phase equation are not the coupling coefficients in I12. Kelso (2008) gives the mapping [read; restated, attribution as above]: with coupling `(x1' - x2'){alpha + beta (x1 - x2)^2}` (alpha, beta here = a, b of I12) and oscillation amplitude r, `a_red = -(alpha + 2 beta r^2)` and `b_red = beta r^2 / 2`. So the classical bistable regime (`a_red, b_red > 0`) needs `beta > 0` and `alpha < -2 beta r^2`, i.e. the second quadrant of Avitabile's (a, b) plane; the sign flip on a is explicit.

**What the full-system analyses add** [read]:
- Avitabile et al.: the four-dimensional system has regimes the reduced equation cannot show: stable phase-locked solutions spanning a wide range of relative phases, bistability between several patterns, differing amplitudes. They add that in "a sizeable region of parameter space, stable in-phase and anti-phase solutions coexist" and that "the original set of parameter values based on [22]" lies there; their [22] is HKB 1985. Their abstract frames this as: relaxing the constant-amplitude assumption "allows for much richer coordination dynamics".
- Slowinski et al.: with the phenomenological coupling `F` (above), the model gives only a qualitative account of the loss of anti-phase stability as frequency rises; the neurologically motivated coupling `G = eps*[(x_i - (1-r) x_i(t-tau1) - r x_j(t-tau2)) - delta/3 * (...)^3]`, which they credit to Banerjee & Jirsa (2007, *Biol. Cybern.* 96:265-278, doi 10.1007/s00422-006-0114-4, resolved; Banerjee & Jirsa fixed delta = 1, Slowinski et al. free it), with cross-talk `r`, nonlinearity `delta`, strength `eps` and delays tau, gives a quantitative account of both amplitude drop and loss of anti-phase stability [read]. With tau = 0.08 s there are sizeable parameter ranges where bistable in-phase/anti-phase at low omega gives way to in-phase only as omega rises [read]. The statement that delay "increases the size of parameter regions of bistability" is Słowiński, Tsaneva-Atanasova & Krauskopf (2016), restated in the 2020 paper [read in 2020, 2016 not read]. These are model comparisons against the published finger-movement findings, not new experiments.

## 6. Empirical standing

- **HKB**: a strong behavioural result for finger and limb movement (anti-phase to in-phase switch as frequency rises, with hysteresis), replicated across labs and extended to interpersonal pendulum and rocking-chair pairs (Schmidt, Bienvenu, Fitzpatrick & Amazeen 1998, *J. Exp. Psychol. Hum. Percept. Perform.* 24:884-900, doi 10.1037/0096-1523.24.3.884; Richardson, Marsh, Isenhower, Goodman & Schmidt 2007, "Rocking together", *Hum. Mov. Sci.* 26:867-891, doi 10.1016/j.humov.2007.07.002; both DOIs resolved on Crossref, texts not read; Kelso 2008 also cites Schmidt et al. 1990 for the interpersonal case). It is a result about rhythmic movement phase, not affect, and the move to emotion or drive is an analogy.
- **Hu et al. (2014)**: real data are from Klump et al.'s (2012) Michigan State twin study, 198 female twins with 45 days of ratings and salivary hormones, of whom the 181 with ovulatory cycles were analysed [read] (estradiol, emotional eating, negative affect); not dyads in the social sense; coupling is between two variables of one person. Table 5 [read]: AIC 2271.8 (all four coupling terms), 2268.4 (velocity coupling only), 2281.6 (uncoupled). The velocity-only model fits best. Reported coupling estimates [read, Table 4 and text]: estradiol velocity into eating 0.049 (SE 0.016, p < .05); eating velocity into estradiol -0.062 (SE 0.022, p < .05). Authors' interpretation: "estradiol synchronizes eating, and eating desynchronizes estradiol". A between-person shuffle (pairing one person's hormones with another, non-twin, person's eating) gave coupling estimates peaked at zero with an interval excluding the observed effect. It supports that velocity coupling can be recovered in real data; it does not touch a dyad.
- **rties vignette example** [read]: on the package's example data the coupled model explains on average R^2 of 0.72 versus 0.69 for the uncoupled, a gain of about 2%; the vignette's own remark: "coupling is not critical for describing the dynamics of the system", though the small gain "may predict system variables ... better". An illustration on example data, not a finding.
- **Helm, Sbarra & Ferrer (2012)**, *Emotion* 12(4):748-762, doi 10.1037/a0025036 (resolved on Crossref): couples' respiration and heart rate over three lab tasks, coupled linear oscillators. Abstract-level only [abs]: partner associations were detectable in all three tasks, with a different coupling pattern in each. No open full text; effect sizes not read.
- **Steele & Ferrer (2011)**, *Multivariate Behavioral Research* 46(6):956-984, doi 10.1080/00273171.2011.625305 (resolved): daily positive and negative affect in romantic couples, damped linear oscillator as a latent differential equation. Abstract only [abs, PubMed 26736119]: no within-person damping of relationship-specific affect; coupled influences between partners for both positive and negative affect; for negative affect partners respond to each other's displacement but not to each other's rate of change. That last point is the one direct dyadic test of the partner-velocity term found here, and it is null for negative affect. Full text not read.
- **Ferrer & Steele (2010) slides** [read]: with 300 dyads (60-90 days of daily emotion reports) and first-order models of the Felmlee-Greenberg type, "independent" members was the best-fitting type for the largest group (77 dyads), "cooperative" 6, "contrarian" 11, one-uncooperative-one-dependent 42 + 4. These counts sum to 140. The slides also say 140 dyads showed one model as best fit and 159 a differential fit pattern, followed by a k-means step that "forced" dyads into a model; whether the 140 assigned are the single-best-fit dyads or the result of the clustering is not clear from the slides. Different model family (first order, no partner velocity), but it shows coupling is not the modal best fit in daily affect.
- **Blunt summary**: the oscillator form fits time series from one person or one dyad in-sample; its partner-velocity parameters are fragile (only estimable when partner tempos differ, over narrow ranges, and highly sensitive to the derivative-estimation settings tau and embed, per the rties vignette). I found no out-of-sample prediction of behaviour, outcomes or interventions from fitted couplings in what was reachable, and no replication of specific coupling values. Whether they predict relationship outcomes is asserted as a goal in the vignettes, not shown here.

## 7. Operand/operator translation

- **Operand**: an agent with a drive state pair `(x, x')` (level relative to its setpoint, and its rate). The oscillator is a second-order object: the drive level and its velocity are both part of the state. An algebra restricted to levels cannot express partner-velocity coupling.
- **Operators**: (i) self-regulation `R(eta, zeta)`: restoring force and damping toward the agent's own setpoint; (ii) displacement coupling `S(gamma_x)`: the partner's level pulls my acceleration; (iii) velocity coupling `F(g)`: the partner's rate of change adds to my damping, sign setting in-phase or anti-phase preference. All three are linear and add.
- **Composition law** (derived): in a symmetric linear dyad the sum and difference modes decouple; each mode has effective parameters `(eta +/- gamma, zeta +/- g)`. That is a closed algebraic rule: "the dyad's modes are the eigenmodes of the coupling matrix". Stability is `zeta + |g| < 0, eta + |gamma| < 0`. This is the one small theorem available and it is mine, not the literature's.
- **HKB as the nonlinear version**: the same operators with state-dependent gain on the velocity difference and a limit-cycle self term. The coupling-induced bifurcation is a transition in which relative phase pattern is stable as a control parameter (frequency, equivalently a falling `b/a`) changes. For drives the analogue of the control parameter would have to be named: possibly the tempo of the drive cycle (how fast the drive cycles through arousal and reduction), which no source tested.
- **Mapping to fear** (the use that motivated this direction): a partner's fear level acts as `S` (company shifts my setpoint, a restoring pull toward theirs); the partner's rate of change of arousal acts as `F` (their calming damps mine, their escalation amplifies it). `F` with the wrong sign is the formal definition of panic contagion, `|g| > |zeta|`. This is an interpretive reading, not something the sources fit to fear data.

## 8. What exists vs what does not

Exists:
- A clean, estimable second-order linear dyadic form with named parameters and an interpretation of each in terms of frequency, damping, and partner influence on each (Hu et al.; rties).
- A derived stability condition for the symmetric case (this file), and the identifiability limits of the coupling parameters in simulation (Hu et al.).
- HKB: a nonlinear coupled-oscillator model with a coupling-induced bifurcation, empirically strong for movement phase; partner-velocity-difference coupling with delays.
- Fitting software (`rties`; OpenMx/LDE in Boker's work).

Does not exist (as far as I could verify; the validation pass could not re-test these with fresh searches because the shared web-search budget was exhausted, so they rest on the original session's searches):
- A published stability analysis of the Boker-Laurenceau model with partner-velocity coupling (the condition above is derived here; no source states it).
- A validated link from the linear affect-oscillator parameters to the HKB `a, b` parameters, or any test for a coupling-induced bifurcation in affect or fear data.
- Out-of-sample prediction of dyadic outcomes from fitted couplings. (Ferrer & Steele's 2010 slides list this as a planned extension, which supports its absence at that date only.)
- A drive-specific application: the data fitted are intimacy, daily affect, respiration, heart rate; none is fear, hunger or another named drive.
- Any treatment of more than two oscillators or of coupling topology in this family (the dyad-only restriction).

## Unconfirmed

- Exact form of the original Boker & Laurenceau (2006, 2007) equations, including any constraints, and the exact definition of the "coupling parameter" in each. Their book chapters were not reachable.
- The Steele & Ferrer (2011) and Helm et al. (2012) specifications and effect sizes (abstracts only).
- HKB 1985 original text; the equations and the a, b mapping in Section 5 are from Kelso (2008) and Avitabile et al. (2016), not from HKB directly.
- Whether Kay, Kelso, Saltzman & Schöner (1987) give exactly alpha = 12.457, beta = 0.007095, gamma = 0.641 (Slowinski et al. attribute them so; Kay et al. not read).
- The Schmidt et al. (1998) pendulum and Richardson et al. (2007) rocking-chair studies: existence and authorship confirmed on Crossref, content not read.
- Słowiński, Tsaneva-Atanasova & Krauskopf (2016): the delay-widens-bistability result is taken from the 2020 paper's restatement.
- Hu et al.'s figure descriptions of the bidirectional model (Figure 3 not read as an image).

## Original session's source log

- DOIs resolved on Crossref 2026-10-29: 10.1037/a0025036 (Helm et al., Emotion 12:748-762), 10.1037/a0032476 (Hu et al., Psychol Methods 19:56-71), 10.1080/00273171.2011.625305 (Steele & Ferrer, MBR), 10.1007/BF00336922 (HKB 1985), 10.1007/s00422-016-0691-9 (Avitabile et al.), 10.1137/19M1279381 (Slowinski et al.), 10.1080/10407413.2018.1438196 (Nordham et al.; located, not used), 10.1007/s11336-013-9366-9 (Steele, Ferrer & Nesselroade, Psychometrika 79:675-700, seen on the publisher page, paywalled).
- Open text used: PMC7480173, PMC6986925, PMC4903117 (NCBI efetch); `rties` vignette Rmd (github.com/cran/rties); Ferrer & Steele slides (cilvr.umd.edu/Conference2010/CILVRposts2010/Ferrer_post.pdf).

## Validation log (2026-10-29)

- ✓ Hu, Boker, Neale & Klump (2014), *Psychol. Methods* 19(1):56-71, doi 10.1037/a0032476: Crossref resolved; PMC7480173 re-read. Equations 1, 2, 4, parameter interpretations, 0/180/270/90 degree results, "breaks down", ranges -0.1~0.1 and -0.02~0.02, over-estimation, Table 5 AICs and coupling estimates all match.
- ✎ Hu et al. sample: "63 women" was wrong; corrected to 198 female twins (Klump et al. 2012 study), 181 ovulatory analysed, 45 days. Shuffle test description tightened. Title note added (manuscript title differs from Crossref's).
- ✓ Butler & Kuelz, `rties` vignette `coupled_oscillator_V05` (package by Butler, Boker as contributor in 5.0.0): all quoted labels, 8 parameters, no intercept, co-regulation/co-dysregulation definitions, 69%/72%/about 2%, "not critical", "highly sensitive" to tau and embed confirmed in the raw Rmd.
- ✎ Ferrer & Steele (2010) CILVR slides: re-read; model counts confirmed (6, 77, 11, 42, 4), but they sum to 140 and the slides do not say the 159 were assigned by the clustering step; reworded as ambiguous. Equation-shape description confirmed.
- ✓ Haken, Kelso & Bunz (1985), *Biol. Cybern.* 51(5):347-356, doi 10.1007/BF00336922: resolved; not read (stated).
- ✎ Avitabile, Słowiński, Bardy & Tsaneva-Atanasova (2016), *Biol. Cybern.* 110:201-216, doi 10.1007/s00422-016-0691-9: resolved, PMC4903117 re-read. Equations (9)-(10) and quotes match. Corrected: first quadrant is anti-phase-only, not "converse bistability"; phase-locked stable only in fourth quadrant; their [22] is HKB 1985, not "Kelso's data"; the sign link to Section 4 restated as `g = -a` rather than "side of the equation".
- ✎ Słowiński, Al-Ramadhani & Tsaneva-Atanasova (2020), *SIAM J. Appl. Dyn. Syst.* 19(1):208-232, doi 10.1137/19M1279381: resolved, PMC6986925 re-read; F, G, parameter values, tau = 0.08 s, qualitative/quantitative contrast match. Corrected credit: G is Banerjee & Jirsa (2007), delayed F is Varlet et al. (2012), the bistability-widening result is Słowiński, Tsaneva-Atanasova & Krauskopf (2016); reference [29] identified as Kay et al. (1987).
- ✎ Kelso (2008), *Scholarpedia* 3(10):1612: now read at source. Reduced equation, potential, k = b/a, k_c = 0.25, hysteresis confirmed. Added the explicit mapping a_red = -(alpha + 2 beta r^2), b_red = beta r^2 / 2 (removing that item from Unconfirmed) and HKB's own rejection of linear velocity coupling.
- ✓ Helm, Sbarra & Ferrer (2012), *Emotion* 12(4):748-762, doi 10.1037/a0025036: resolved; PubMed abstract matches the description.
- ✎ Steele & Ferrer (2011), *MBR* 46(6):956-984, doi 10.1080/00273171.2011.625305: resolved; abstract now read and added (negative affect: partners respond to displacement, not rate of change).
- ✓ Schmidt, Bienvenu, Fitzpatrick & Amazeen (1998), doi 10.1037/0096-1523.24.3.884, and Richardson, Marsh, Isenhower, Goodman & Schmidt (2007), doi 10.1016/j.humov.2007.07.002: existence and authorship resolved on Crossref; content unread, kept as [abs].
- ✓ Banerjee & Jirsa (2007) doi 10.1007/s00422-006-0114-4; Słowiński, Tsaneva-Atanasova & Krauskopf (2016) doi 10.1140/epjst/e2015-50327-6; Kay, Kelso, Saltzman & Schöner (1987) doi 10.1037/0096-1523.13.2.178: resolved (added credits).
- ✓ Nordham, Tognoli, Fuchs & Kelso (2018) doi 10.1080/10407413.2018.1438196 and Steele, Ferrer & Nesselroade (2014) doi 10.1007/s11336-013-9366-9: resolved; listed only, not used.
- ✓ Derived algebra (Sections 3, 4): steady-state transfer function, resonance phases, sum/difference mode decoupling and the stability condition `zeta + |g| < 0`, `eta + |gamma| < 0` re-derived and correct. ✎ Section 3's "displacement coupling does not change energy balance" softened to "does not change mode damping in the symmetric case".
- ? "Does not exist" claims (Section 8): not re-tested; the shared web-search budget was exhausted during this pass.

**Verdict.** The file is substantially sound: its equations, quotations and AIC and coupling figures match the open sources, and the derived stability result checks out. It had one factual error (the Hu et al. sample size), one misreading of Avitabile et al.'s first quadrant, and several misplaced credits in the HKB section (Banerjee & Jirsa, Słowiński et al. 2016, Varlet et al.), all fixed. The Scholarpedia mapping now resolves the HKB sign question, and Steele & Ferrer's null result for partner-velocity coupling in negative affect strengthens the file's "thin evidence" conclusion.

## Cross-checks (2026-10-29)

Compared against the other files in this directory by grep on works, authors, equations and numbers (Boker, Hu, rties/Butler, Helm, Steele, Ferrer, HKB, Kelso, Avitabile, Slowinski, Kay, Alderisio). Other files were not edited. Only files 20, 60, 70 and 79 (plus 80 and 27 in passing) overlap; no other file cites Hu et al., Avitabile, Slowinski, Banerjee & Jirsa or Kay et al.

**Agreements**
- File 20 section 5: the Boker-Laurenceau form `x'' = eta x + zeta x' + coupling*y + coupling*y'`, eta < 0 as restoring/frequency term, zeta < 0 as damping, and co-regulation versus co-dysregulation as the damping question all match Section 1 and 2 here. File 20 marks them [std]; this file supplies the [read] source (Hu et al. 2014; rties).
- File 20 section 5 translation (state is the pair (x, x'); stability of a coupled dyad is a property of the 4x4 system, not of each zeta alone) agrees with Section 4 here, which derives the symmetric case.
- File 20 sections 5 and 9, and files 79 and 70, on Boker & Nesselroade (2002) being a single-oscillator LDE method paper (MBR 37(1):127-160): consistent with this file's use of LDE for Hu et al. and Steele & Ferrer.
- File 20 section 9 on HKB (`phi' = -a sin phi - 2b sin 2phi`, `V = -a cos phi - b cos 2phi`, `k = b/a`, both states stable for k > 0.25, k_c = 0.25, hysteresis, Kelso 2008) is identical to Section 5 here. File 60 section 8 quotes the same reduced equation and the same DOI (10.1007/bf00336922) and pages (51:347-356).
- File 20 and file 70 section 1 on Helm, Sbarra & Ferrer (2012), Emotion 12(4):748-762, doi 10.1037/a0025036: coupled linear oscillators on respiration and heart rate, three lab tasks, different coupling pattern in each. File 70 notes the abstract states no sample size; this file reports no sample size either.
- File 70 section 1 writes the Helm cross term as `gamma x_j (+ gamma' x_j')` [std]; Section 2 here reads the same structure at source in Hu et al. Eq. 4.
- File 20 and file 70 on Steele & Ferrer (2011), MBR 46(6):956-984, doi 10.1080/00273171.2011.625305: same citation. Nothing in other files addresses its null finding on partner rate of change for negative affect (Section 6 here); that point is not contradicted anywhere.
- File 20 section 5 "no predictive validation found" and file 70 "no stability reported, nothing for n >= 3" agree with Section 6 and 8 here.
- File 79 section 5.4 (complex eigenvalues of a coupled pair make the discrete-time to continuous-time inversion non-unique) is compatible with Section 4 here (oscillatory dyad modes) and with the identifiability caveat from Hu et al.; no numbers in common.

**Contradictions and tensions**
1. Scope of the "does not exist" list (Section 8 here, last bullet: "any treatment of more than two oscillators or of coupling topology in this family") against file 60 and file 20.
   - File 60 sections 2 to 3 and 8 and file 20 section 9 (pointing at survey 23) do cover n-oscillator work: Alderisio et al. 2017 (Sci. Rep. 7:6846; 7 people, Kuramoto fit on four graphs), Bielczyk et al.'s triad and the star reduction (file 60), Zhang, Beetle, Kelso & Tognoli 2019 (exists, contents unread).
   - These are Kuramoto, first-order delay or tanh models, not the Boker second-order linear oscillator with partner velocity, so "in this family" is true. File 60 itself states HKB-at-n is open and that no n-person drive model has been fitted.
   - Verdict: not a factual conflict, a wording issue. Read the bullet as "none in the Boker/rties linear second-order family". No primary-source check was needed. File 61's own wording is correct only with that qualifier.
2. File 20 section 5 says the rties vignette URL 404ed and treats the coupling equation as [std]; this file read the vignette Rmd from github.com/cran/rties. Verdict: this file is right and supersedes file 20 on that point (the vignette was reached by a different route); file 20's [std] claims are all confirmed, none contradicted.
3. Possible numeric mismatch: file 70 section 1 says "32 couples" is the Ferrer & Helm 2013 sample, not Helm 2012's; this file's Ferrer & Steele 2010 slide counts (300 dyads, 140 + 159) are a different study. No actual conflict.

No claim in this file was found to be contradicted by a validated file on equations, numbers or attribution, so no web lookup of primary sources was run. Items 1 and 2 are scope and recency, not disagreements about a source.

## Licences of quoted and transcribed material (2026-10-30)

Nothing in this file is Wikipedia-derived. Licences below are as determined in the 2026-10-30 audit; none was verified on the source page unless stated.

- Kelso (2008), "Haken-Kelso-Bunz model", Scholarpedia 3(10):1612: believed CC BY-NC-SA 3.0 (from memory; not verified on the page). Use: restated equations (reduced phase equation, potential, k = b/a, k_c = 0.25, the a_red and b_red mapping) and two very short quotations. Attributed in Section 5. Share-alike and non-commercial terms apply if any passage were copied; the equations are restated. Method note: the page was fetched with an expired TLS certificate ignored (see Source log and Validation log). That is a skipped security check, not a bypassed access control; re-read through a valid route if reproducibility matters.
- Hu, Boker, Neale & Klump (2014), Psychol. Methods 19(1):56-71 (PMC7480173): not determined; publisher copyright presumed (open-access full text via PMC, licence not recorded). Use: restated equations, short quotation, AIC and coupling values cited as numbers.
- Klump et al. (2012) Michigan State twin study, as analysed by Hu et al.: not determined; no data-sharing licence recorded. Use: dataset citation and description only (198 twins, 45 days, 181 analysed); no record-level data in this file.
- Butler & Kuelz, rties package and vignette (CRAN; github.com/cran/rties): not determined; the package licence and the example data licence were not recorded. Use: short quotations of labels and remarks, summary results (R^2 0.72 versus 0.69) cited as numbers; no data reproduced.
- Avitabile, Slowinski, Bardy & Tsaneva-Atanasova (2016), Biol. Cybern. 110:201-216 (PMC4903117): not determined; publisher copyright presumed (open-access licence not recorded). Use: restated equations, short quotations.
- Slowinski, Al-Ramadhani & Tsaneva-Atanasova (2020), SIAM J. Appl. Dyn. Syst. 19 (PMC6986925): not determined; publisher copyright presumed (open-access licence not recorded). Use: restated equations and parameter values, short quotations.
- Haken, Kelso & Bunz (1985), Biol. Cybern. 51:347-356: publisher copyright (Springer); not read. Use: citation only.
- Ferrer & Steele (2010), CILVR conference slides (cilvr.umd.edu, Ferrer_post.pdf): not determined; publisher copyright presumed. Use: model-type labels and counts (77, 6, 11, 42 + 4) cited as facts, with one-word quotations; no table transcribed beyond these.
- Steele & Ferrer (2011), Multivariate Behavioral Research 46(6) (PubMed abstract): publisher copyright (Taylor & Francis); PubMed abstract terms not recorded. Use: abstract-level paraphrase; no verbatim sentences intended, to be confirmed on a re-read.
- Helm, Sbarra & Ferrer (2012), Emotion 12(4) (PubMed abstract): publisher copyright (APA); PubMed abstract terms not recorded. Use: abstract-level paraphrase; no verbatim sentences intended, to be confirmed on a re-read.
- Other cited works (Banerjee & Jirsa 2007; Slowinski, Tsaneva-Atanasova & Krauskopf 2016; Kay et al. 1987; Varlet et al. 2012; Schmidt et al. 1998; Richardson et al. 2007; Nordham et al. 2018; Steele, Ferrer & Nesselroade 2014): publisher copyright presumed. Use: citation only.
