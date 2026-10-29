# Prior work 061: the coupled damped oscillator, its partner-velocity term, and HKB

Direction: D191

Date: 2026-10-29. Survey for the social-algebra strand. Question: what do the two coupling parameters of the coupled damped linear oscillator (partner displacement, partner velocity) mean, and how does that relate to the Haken-Kelso-Bunz (HKB) coupling-induced bifurcation? Builds on file 20 section 5 and section 9, which had these as standard account only.

**Method and honesty note.** Primary Boker & Laurenceau 2006/2007, Steele & Ferrer 2011 and Helm, Sbarra & Ferrer 2012 are paywalled and were NOT read; none has an open copy I could reach. What was read at source this session, via NCBI efetch full text and GitHub raw files:
- Hu, Boker, Neale & Klump (2014), author manuscript PMC7480173: states the single and coupled oscillator equations and interprets every parameter, with simulations. Boker is a co-author, so this is the closest primary statement of the Boker model available.
- Butler & Kuelz, `rties` R package vignette `coupled_oscillator_V05` (raw Rmd from github.com/cran/rties): states the dyadic model, with partner displacement and partner velocity terms and their interpretation.
- Slowinski, Al-Ramadhani & Tsaneva-Atanasova (2020), PMC6986925: HKB oscillator and coupling function, with delays.
- Avitabile, Slowinski, Bardy & Tsaneva-Atanasova (2016), PMC4903117: full HKB system, bifurcation analysis.
- Ferrer & Steele 2010 conference slides (CILVR, PDF): Greek letters were lost in text extraction, so only the equation shape is usable.
Tags: [read] = read at source named; [derived] = my own algebra from [read] equations, checked for consistency with the sources but not published by them; [std] = standard account, not checked.

**Summary.** (1) The "partner-velocity term" is real and has a clean reading: in `x'' = eta*x + zeta*x' + gamma_x*y + gamma_xdot*y'`, the partner's displacement shifts frequency/phase, the partner's velocity shifts damping/amplification, and in a symmetric dyad velocity coupling adds directly to the damping of the sum and difference modes. So it can turn a co-regulating dyad into a co-dysregulating one [derived]. (2) HKB's coupling term `(a + b(x1-x2)^2)(x1' - x2')` is a velocity-difference coupling, the same family; the HKB bifurcation is a result about two nonlinear oscillators and a frequency control parameter, not a property of the linear model. (3) The linear model has no bifurcation of its own; the only qualitative regime change is the sign of damping. (4) Evidence that coupling terms improve prediction of real affect/physiology is thin and mostly in-sample.

---

## 1. Single damped linear oscillator (the self term)

**Source.** Hu, Boker, Neale & Klump (2014), "Coupled latent differential equation with moderators: Simulation and application", *Psychological Methods* 19(1):56-71, doi 10.1037/a0032476 (DOI resolved on Crossref). [read, PMC7480173]

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
- Partner displacement = the partner's current level pulling my acceleration, i.e. a shared restoring force (spring). It changes frequency and phase but not energy balance.
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

The self term is a hybrid Van der Pol (alpha) and Rayleigh (beta) nonlinear damping, with `gamma` the linear (anti-)damping: a limit-cycle oscillator, not the linear damped oscillator of Section 1. `omega` relates to the natural/pacing frequency. The coupling is a function of the velocity difference, scaled by a linear (a) and a quadratic (b) function of the position difference. So it is a partner-velocity term, with a state-dependent gain. For comparison, the Boker-style term is partner velocity with constant gain, entering at the same place (acceleration). Slowinski et al. use this form with delays: `(x_i'(t) - x_j'(t - tau_j))(a + b(x_i(t) - x_j(t - tau_j))^2)` [read], fixing alpha = 12.457, beta = 0.007095, gamma = 0.641 at "experimentally validated" values from their reference [29] (not independently checked).

**Sign** [read, Avitabile et al.]: in the (a, b) plane, in-phase is stable when both are negative (third quadrant: "in-phase oscillations are now stable, while anti-phase solutions are unstable") and the converse bistability sits where a is positive; phase-locked intermediate relative phases arise only in the second and fourth quadrants. So negative `a, b` is dissipative coupling on the velocity difference: it damps any difference between the two, which is the same mechanism as `g > 0` in Section 4 acting on the in-phase mode, with the sign convention reversed by the side of the equation the term sits on. Consistent, not identical.

**Reduced relative-phase form** [read via file 20, Kelso (2008) Scholarpedia; not re-read this session because the Scholarpedia server's certificate had expired]: `phi' = -a sin(phi) - 2b sin(2phi)`, potential `V(phi) = -a cos(phi) - b cos(2phi)`, rescaled with `k = b/a`; both in-phase (phi = 0) and anti-phase (phi = pi) stable for `k > 0.25`; at the critical `k_c = 0.25` anti-phase loses stability and the system switches to in-phase, with hysteresis. In that reduction `k` falls as movement frequency rises, so frequency is the control parameter. Reduction by slowly varying amplitudes and rotating-wave approximation [read, Avitabile et al.: "all previous studies have followed a line of analysis based on slowly varying amplitudes and rotating wave approximations"]. The a and b of the reduced phase equation are not the same quantities as the coupling coefficients in I12; the mapping (including a sign change) is not checked here.

**What the full-system analyses add** [read]:
- Avitabile et al.: the four-dimensional system has regimes the reduced equation cannot show: stable phase-locked solutions spanning a wide range of relative phases, bistability between several patterns, differing amplitudes. They add the point that in the original-parameter region (from reference [22], Kelso's data) stable in-phase and anti-phase "coexist". Their abstract frames this as: relaxing the constant-amplitude assumption "allows for much richer coordination dynamics".
- Slowinski et al.: with a phenomenological coupling `F` (above), the model gives only a qualitative account of the loss of anti-phase stability as frequency rises; a neurologically motivated coupling `G = eps*[(x_i - (1-r) x_i(t-tau1) - r x_j(t-tau2)) - delta/3 * (...)^3]`, with cross-talk `r`, nonlinearity `delta`, strength `eps` and delays tau, gives a quantitative account of both amplitude drop and loss of anti-phase stability. Delay near 0.08 s gives bistable in-phase/anti-phase at low frequency that collapses to in-phase as omega rises. Delay matters: it "increases the size of parameter regions of bistability". These are model comparisons against the published finger-movement findings, not new experiments.

## 6. Empirical standing

- **HKB**: a strong behavioural result for finger and limb movement (anti-phase to in-phase switch as frequency rises, with hysteresis), replicated across labs and extended to interpersonal pendulum and rocking-chair pairs (Schmidt et al. 1998; Richardson et al. 2007; found in search result summaries, [abs], not read). It is a result about rhythmic movement phase, not affect, and the move to emotion or drive is an analogy.
- **Hu et al. (2014)**: real data are 63 women (hormones, eating, negative affect), not dyads; coupling is between two variables of one person. Table 5 [read]: AIC 2271.8 (all four coupling terms), 2268.4 (velocity coupling only), 2281.6 (uncoupled). The velocity-only model fits best. Reported coupling estimates (estradiol velocity into eating `gamma_xdot` = 0.049 (SE 0.016); eating velocity into estradiol = -0.062 (SE 0.022)). Authors' interpretation: estradiol "synchronizes" eating and eating "desynchronizes" estradiol. A between-person shuffle test found no spurious coupling. It supports that velocity coupling can be recovered in real data; it does not touch a dyad.
- **rties vignette example** [read]: on the package's example data the coupled model explains on average R^2 of 0.72 versus 0.69 for the uncoupled, a gain of about 2%; the vignette's own remark: "coupling is not critical for describing the dynamics of the system", though the small gain "may predict system variables ... better". An illustration on example data, not a finding.
- **Helm, Sbarra & Ferrer (2012)**, *Emotion* 12(4):748-762, doi 10.1037/a0025036 (resolved on Crossref): couples' respiration and heart rate over three lab tasks, coupled linear oscillators. Abstract-level only [abs]: partner associations were detectable in all three tasks, with a different coupling pattern in each. No open full text; effect sizes not read.
- **Steele & Ferrer (2011)**, *Multivariate Behavioral Research* 46(6):956-984, doi 10.1080/00273171.2011.625305 (resolved): daily affect in couples, latent differential equations. Not read.
- **Ferrer & Steele (2010) slides** [read]: with 300 dyads (60-90 daily emotion reports) and first-order models of the Felmlee-Greenberg type, "independent" members was the best-fitting type for the largest group (77 dyads), "cooperative" 6, "contrarian" 11, one-uncooperative-one-dependent 42+4 (140 dyads with a single best model; 159 more showed a differential fit pattern and were assigned by a clustering step). Different model family (first order, no partner velocity), but it shows coupling is not the modal best fit in daily affect.
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

Does not exist (as far as I could verify):
- A published stability analysis of the Boker-Laurenceau model with partner-velocity coupling (the condition above is derived here; no source states it).
- A validated link from the linear affect-oscillator parameters to the HKB `a, b` parameters, or any test for a coupling-induced bifurcation in affect or fear data.
- Out-of-sample prediction of dyadic outcomes from fitted couplings.
- A drive-specific application: the data fitted are intimacy, daily affect, respiration, heart rate; none is fear, hunger or another named drive.
- Any treatment of more than two oscillators or of coupling topology in this family (the dyad-only restriction).

## Unconfirmed

- Exact form of the original Boker & Laurenceau (2006, 2007) equations, including any constraints, and the exact definition of the "coupling parameter" in each. Their book chapters were not reachable.
- The Steele & Ferrer (2011) and Helm et al. (2012) specifications and effect sizes.
- The mapping between HKB's coupling coefficients (a, b in I12) and the reduced relative-phase a, b, including sign.
- HKB 1985 original text; the Scholarpedia equations in Section 5 were taken from file 20's read, not re-read.
- The experimental-parameter values of alpha, beta, gamma used by Slowinski et al. (from their reference [29]).
- The Schmidt/Richardson pendulum and rocking-chair studies: search summary only.
- Hu et al.'s figure descriptions of the bidirectional model (Figure 3 not read as an image).

## Validation log

- DOIs resolved on Crossref 2026-10-29: 10.1037/a0025036 (Helm et al., Emotion 12:748-762), 10.1037/a0032476 (Hu et al., Psychol Methods 19:56-71), 10.1080/00273171.2011.625305 (Steele & Ferrer, MBR), 10.1007/BF00336922 (HKB 1985), 10.1007/s00422-016-0691-9 (Avitabile et al.), 10.1137/19M1279381 (Slowinski et al.), 10.1080/10407413.2018.1438196 (Nordham et al.; located, not used), 10.1007/s11336-013-9366-9 (Steele, Ferrer & Nesselroade, Psychometrika 79:675-700, seen on the publisher page, paywalled).
- Open text used: PMC7480173, PMC6986925, PMC4903117 (NCBI efetch); `rties` vignette Rmd (github.com/cran/rties); Ferrer & Steele slides (cilvr.umd.edu/Conference2010/CILVRposts2010/Ferrer_post.pdf).
