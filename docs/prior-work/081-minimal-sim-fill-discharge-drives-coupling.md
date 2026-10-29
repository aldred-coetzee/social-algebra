# Prior work 081: specification of a minimal `sim/`, N agents with K fill-and-discharge drives and pairwise coupling

Direction: D536

Date: 2026-10-29. Kind: model. No code in the repo; the numerical checks below were run in a scratchpad (numpy/scipy) and are tagged [computed]. Cross-references: 16 section 2 (Lorenz, no equations), 53 (despair as gain collapse), 62 (coupled homeostatic drive), 66 (Granovetter read in full, aggregation rules), 68 (Epstein), 69 (quorum), 70, 72.

**Method and honesty note.** Tags: **[read]** read at source this session; **[derived]** my own algebra; **[computed]** numerical check run this session; **[standard account]** not checked this session. Read at source: Helbing, Farkas & Vicsek 2000 (arXiv cond-mat/0009448v1, the preprint of the Nature paper, whole text; the published Nature version may differ in detail). Granovetter 1978 was read in full in file 66 and is cited from there. **Not read**: Mirollo & Strogatz 1990 (the Cornell PDF returns 403; arXiv does not carry it) and Strogatz & Mirollo 1988 (Physica D; abstract level only). The web-search budget was exhausted mid-task, so no extra confirmation was possible. Everything attributed to those two is [standard account].

DOIs confirmed through Crossref this session: 10.1086/226707 (Granovetter 1978, AJS 1978-05), 10.1038/35035023 (Helbing, Farkas, Vicsek, *Nature* 407, Sept 2000, "Simulating dynamical features of escape panic"), 10.1137/0150098 (Mirollo & Strogatz, "Synchronization of Pulse-Coupled Biological Oscillators", *SIAM J. Appl. Math.* 50(6):1645-1662, 1990), 10.1016/0167-2789(88)90074-7 (Strogatz & Mirollo, "Phase-locking and critical phenomena in lattices of coupled nonlinear oscillators with random intrinsic frequencies", *Physica D* 31:143-168, 1988), 10.1088/0305-4470/21/13/005 (Strogatz & Mirollo, "Collective synchronisation in lattices of nonlinear oscillators with randomness", *J. Phys. A* 21:L699, 1988), 10.1103/PhysRevE.51.4282 (Helbing & Molnar 1995, social force model, not read), 10.1103/PhysRevLett.75.1226 (Vicsek et al. 1995, not read). A DOI I tried from memory for Strogatz 1988 (10.1016/0167-2789(88)90098-3) did not resolve; the Crossref search result is the one used.

**Seed ambiguity.** The map says "Strogatz 1988". Two 1988 Strogatz & Mirollo papers exist (above), both about Kuramoto-type oscillators with random frequencies on lattices, not about fill-and-discharge. The fill-and-discharge result is the 1990 Mirollo-Strogatz paper. I treat the 1990 paper as the intended structural seed and the 1988 pair as the continuous-phase (Kuramoto) comparison.

---

## Summary

1. **Lorenz gives no equations, so any "fill-and-discharge" law is a formalisation by us, not a test of his model** [file 16, read as secondary]. The smallest honest formalisation is one scalar level x in [0,1] per drive, with fill rate r and discharge rate s: dx/dt = r(1-x) - s x. It is **provably bounded** in [0,1] whenever r, s >= 0 [derived]. All coupling must enter through r and s and be clipped non-negative to keep that guarantee.
2. **Despair as a bifurcation needs a second variable with a steeper threshold than the act threshold.** A one-variable fill-discharge cell has a unique equilibrium for any monotone act function [derived]. Adding an efficacy variable u (discharge effectiveness) that collapses when x is high gives an S-shaped equilibrium curve with a saddle-node fold, bistability and hysteresis in the fill rate r [computed]: with the parameters in section 3, the high-drive branch exists from r about 0.22 (three roots at r = 0.22, one at r = 0.21; backward sweep falls between 0.22 and 0.21) and the low branch is lost between r = 0.65 and 0.66 (forward sweep) [re-computed in validation, 0.01 steps]. The loop is real but its width is set by my parameter choice; it is a demonstration that the structure can bifurcate, not evidence that people do.
3. **Cascade thresholds reduce exactly to Granovetter's map.** If drive equilibration is fast relative to the social update, each agent's act threshold in the fraction acting is a monotone function of its own private threshold, and the population obeys phi' = G(phi), the Granovetter cumulative-distribution map [derived]. File 66's results (monotone convergence to the least fixed point, no oscillation, discontinuity of outcome in the mean) transfer unchanged. Oscillation appears only when the quasi-static assumption is dropped.
4. **Fill-and-discharge with pulse coupling is a known object: Mirollo-Strogatz.** Their model (identical integrate-and-fire oscillators, concave rising state, instantaneous pulse on firing; after Peskin's 1975 cardiac-pacemaker model) has a theorem that identical all-to-all oscillators synchronise from almost all initial conditions [abstract read via Crossref in validation; the concavity condition and proof not read]. This is the right null result for the sim's synchrony question (cascades in time, not only in the fraction acting), and it fails to carry over once agents are heterogeneous or the coupling is not excitatory [standard account; check the paper before relying].
5. **Helbing et al. 2000 is not a drive model, but it is the only one of the four seeds that shows a behavioural pathology from raising a single drive-like parameter.** The "faster-is-slower" effect, a falling throughput as desired speed v0 rises, comes from friction at a bottleneck, not from any internal state [read]. It is a pass/fail pattern for a sim, not a source of drive laws.
6. **What a minimal sim can legitimately claim:** bounded state, existence of hysteresis in a stressor load, existence of a cascade threshold in coupling strength. **What it cannot claim:** any of these are properties of people. Section 7 lists the falsifying checks that separate "the code is right" from "the model is right".

---

## 1. The sources

### 1.1 Lorenz (psychohydraulic) and Tinbergen: the structure, not the equation

Lorenz, K. (1950). The comparative method in studying innate behaviour patterns. *Symposia of the Society for Experimental Biology* 4:221-268. Tinbergen, N. (1951). *The Study of Instinct*. Oxford. Not re-read; file 16 section 2 holds the account: a reservoir fills with action-specific energy, a valve opens under a releasing stimulus, flow produces the act. No equations in either [file 16; standard account]. Empirical standing, blunt: the accumulate-and-discharge picture was abandoned in the 1950s-60s because aggression and other acts did not rise reliably with time since last performance [file 16, secondary]. So the sim's discharge cell is a structural convenience with a known weak empirical record. It earns its place only if it produces the despair and cascade behaviours below that no other minimal cell does.

### 1.2 Granovetter 1978 [read in file 66]

Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology* 83(6):1420-1443. DOI 10.1086/226707.

- Each actor has a scalar threshold x in [0,1]: the share of others acting at which the actor acts. r(t+1) = F[r(t)], where F is the cumulative distribution of thresholds (p. 1425). Equilibrium F(r) = r at the first crossing from above (p. 1427) [read, 066].
- F is non-decreasing, so iteration from r(0) converges monotonically to the least fixed point above the start; no oscillation [derived, 066]. For normal thresholds with mean 25, the fold is at sigma about 12.2 (computed 12.222 in 066) [computed, 066].
- Empirical standing (blunt): the paper is a formal illustration with no data fit. It has been applied post hoc in many fields. The threshold distribution is not independently measured in the cited uses (see 075, 076 for the data-side attempts in this strand).

### 1.3 Helbing, Farkas & Vicsek 2000 [read, arXiv preprint]

Helbing, D., Farkas, I. & Vicsek, T. (2000). Simulating dynamical features of escape panic. *Nature* 407:487-490. DOI 10.1038/35035023. arXiv cond-mat/0009448v1.

**Their vocabulary.** "Self-driven many-particle system", "desired velocity", "acceleration time", "psychological repulsive force", "body force", "sliding friction", "panic" = the parameter p in the mixing rule below (the preprint says p_i "reflects the degree of panics of individual i"), "faster-is-slower effect", "clogging", "herding" [read].

**Equations, transcribed [read]:**

- (1) m_i dv_i/dt = m_i (v_i^0(t) e_i^0(t) - v_i(t)) / tau_i + sum_{j != i} f_ij + sum_W f_iW. Desired speed v_i^0, desired direction e_i^0, relaxation (acceleration) time tau_i.
- (2) f_ij = { A_i exp[(r_ij - d_ij)/B_i] + k g(r_ij - d_ij) } n_ij + kappa g(r_ij - d_ij) Delta v_ji^t t_ij. Here r_ij = r_i + r_j, d_ij = |r_i - r_j|, n_ij the unit vector from j to i, t_ij the tangent, g(x) = 0 if the pedestrians do not touch (d_ij > r_ij) and x otherwise.
- (3) f_iW = { A_i exp[(r_i - d_iW)/B_i] + k g(r_i - d_iW) } n_iW - kappa g(r_i - d_iW)(v_i . t_iW) t_iW.
- (4) e_i^0(t) = N[ (1 - p_i) e_i + p_i < e_j^0(t) >_i ], with N(z) = z/|z| and <.>_i the mean over neighbours within radius R_i. Individualistic if p_i is low, herding if high; "p_i reflects the degree of panic of individual i".
- Parameters stated: m = 80 kg, tau = 0.5 s, A = 2e3 N, B = 0.08 m, k = 1.2e5 kg s^-2, kappa = 2.4e5 kg m^-1 s^-1, v^0 about 0.6 (relaxed), 1 (normal), up to 1.5 m/s (nervous), above 1.5 m/s "in a rush"; diameters uniform on [0.5, 0.7] m [read]. A, B and the flow through a 1 m door (0.73 persons/s at v^0 about 0.8 m/s) were used to calibrate; the clogging and faster-is-slower results were not fitted to data.

**Drives/operands.** The only drive-like operand is v^0 (urgency) and p (herding weight). Both are inputs set by the experimenter. Neither has dynamics; nothing fills or discharges.

**Theorems / derived predictions.** None proved. Claimed by simulation [read]: (i) irregular arch-like clogging for v^0 above 1.5 m/s; (ii) faster-is-slower "if the friction parameter kappa is large enough"; (iii) jamming can occur at widenings; (iv) best escape at an intermediate p (neither pure individualism nor pure herding).

**Empirical standing, blunt.** The authors state "we could not find suitable data on escape panics to test our model quantitatively" and call for data [read]. Faster-is-slower has since been tested in laboratory and animal experiments (e.g. mice, sheep, pedestrians), with mixed outcomes (found in some, not others); I have **not** confirmed any such study this session, so that is [standard account] only (Unconfirmed, section 9). Also, the "panic" interpretation of p is a label: eq. 4 is a Vicsek-style alignment weight, and nothing in the paper measures fear.

**Translation.** Operand: a pedestrian with a fixed desired speed and a herding weight. Operator: none beyond force addition. Use for the sim: it shows that a 1-parameter "urgency" dial can flip a system from smooth to pathological *when a shared bottleneck resource exists*. In the algebra that is a resource-coupling operator, not a drive operator.

### 1.4 Mirollo & Strogatz 1990 and Strogatz & Mirollo 1988 [1990: abstract read (Crossref) in validation; body not read. 1988: not read]

Mirollo, R. E. & Strogatz, S. H. (1990). Synchronization of pulse-coupled biological oscillators. *SIAM J. Appl. Math.* 50(6):1645-1662. DOI 10.1137/0150098.

Abstract (Crossref, read in validation): the model is "based on Peskin's model of the cardiac pacemaker" (Peskin 1975, *Mathematical aspects of heart physiology*, Courant Institute, pp. 268-278), "a population of identical integrate-and-fire oscillators"; "when a given oscillator fires, it pulls the others up by a fixed amount, or brings them to the firing threshold, whichever is less"; "for almost all initial conditions, the population evolves to a state in which all the oscillators are firing synchronously". Credit: the model is Peskin's; the all-N almost-everywhere synchrony theorem is Mirollo & Strogatz's. Model as the field states it, beyond the abstract [standard account]: each of N oscillators has a state x_i in [0,1] rising as x = f(phi), where phase phi in [0,1] advances at unit rate and f is smooth, increasing, concave down (f(0)=0, f(1)=1). When x_i reaches 1 the oscillator fires and resets to 0, and every other oscillator's state jumps by epsilon (x_j -> min(1, x_j + epsilon)); those pushed to 1 fire together (absorption). Claimed theorem: for all N, and for almost all initial conditions, the system synchronises (all fire together) [standard account]. The structural point: concave-down charging (fast rise then slow approach, as in x' = r(1-x)) makes a pulse advance a laggard's phase *more* than it advances the leader's, so phases collapse. This is the same equation family as the fill cell below, in the hard-threshold limit.

Strogatz & Mirollo (1988) are Kuramoto-type papers (continuous phases, random natural frequencies, lattice coupling). The Kuramoto result "partial synchrony appears at K_c = 2/(pi g(0)) for a symmetric unimodal frequency density g" is [standard account], and I did not read it in those papers. Kuramoto (1984), *Chemical Oscillations, Waves, and Turbulence* (Springer) is the original.

**Empirical standing, blunt.** Fireflies are the motivating example; evidence for integrate-and-fire pulse coupling in fireflies is partial and species-specific [standard account]. No evidence is known to me that human drive discharges synchronise by this mechanism. Pulse-coupled models are used here as mathematics: they show which cascade/sync behaviours are *generic* for fill-and-discharge cells, so they set the null the sim should reproduce first.

---

## 2. The minimal model specified

Notation: i, j in {1..N} agents; k, l in {1..K} drives. Time continuous. No code; this is a specification for a later `sim/`.

**State.** x_ik in [0,1]: level of drive k in agent i (0 = fully discharged, 1 = full). Optional: u_ik in [0,1], efficacy of discharge for that drive (section 3). Optional: parameter set theta_ik (act threshold).

**Act function.** a_ik = sigma(beta (x_ik - theta_ik)), sigma the logistic. a in (0,1), the intensity of acting on drive k. beta large approximates the hard threshold of Lorenz's valve and of Mirollo-Strogatz firing.

**Fill rate.** r_ik = [ rho_ik + sum_{j != i} sum_l W^{kl}_{ij} a_jl ]_+ , where [z]_+ = max(z, 0). rho_ik is the intrinsic load (the stressor; deprivation clock). W^{kl}_{ij} is the pairwise coupling: the effect of agent j acting on drive l on the fill rate of i's drive k. Signs: W > 0 provocation or contagion (fear in j raises fear in i), W < 0 soothing.

**Discharge rate.** s_ik = c_k u_ik a_ik + [ sum_{l != k} C^{kl}_i a_il ]_+ . The first term is "acting on drive k relieves it". C is within-agent cross-drive relief (acting on desire discharges curiosity? The sign and size are unknown; see file 49 for measured magnitudes).

**Dynamics.** dx_ik/dt = r_ik (1 - x_ik) - s_ik x_ik.

**Boundedness theorem [derived].** If r_ik >= 0 and s_ik >= 0 for all time, then [0,1]^{NK} is forward invariant: at x_ik = 0 the derivative is r_ik >= 0, at x_ik = 1 it is -s_ik <= 0, so no trajectory leaves. Because the clip [.]_+ and the nonnegative sigmoid enforce r, s >= 0, **boundedness holds for any W, C of any sign and size** and any N. The right side is Lipschitz away from the clip kinks (the clip is Lipschitz), so solutions exist and are unique. This is the one unconditional result and it is the first automatic property test for the sim (D541).

**What boundedness does not give.** It does not give convergence (limit cycles and chaos are not excluded), uniqueness of equilibrium, or small gain. Section 4 shows what can be said about convergence.

**Operator reading.** An *act* is the operator that lowers the actor's own x and raises neighbours' r. A *signal* in the algebra is W entries. The model has one primitive per ordered pair of (agent, drive) and no relational operand other than W.

---

## 3. Despair bifurcation: efficacy collapse [derived, computed]

Single drive, single agent, fill r as the control parameter. Add efficacy u in [0,1]:

dx/dt = r(1 - x) - c u a(x) x
du/dt = mu (1 - u) - nu u h(x)

with a(x) = sigma(B (x - tha)) and h(x) = sigma(B (x - thh)). The collapse threshold must exceed the act threshold, thh > tha: acting begins first; if the drive nonetheless stays high, efficacy decays. This matches the verbal structure of learned helplessness as gain collapse (file 53) and is **my construction**, not a published equation.

**Quasi-static curve [derived].** Setting du/dt = 0: u* = mu / (mu + nu h(x)). The x-equilibria solve r (1 - x) = c mu a(x) x / (mu + nu h(x)). The left side decreases linearly in x. The right side rises at tha, then **falls** at thh as h switches on and u* drops. Where the falling stretch is steep enough the curves cross three times. A one-variable cell (u fixed) has monotone right side and so exactly one equilibrium [derived]; the second variable is therefore necessary, not decorative.

**Numerical check [computed].** Parameters B = 25, tha = 0.3, thh = 0.6, c = 1, mu = 0.5, nu = 5.

| r | equilibria x (solved by root-finding) |
|---|---|
| 0.05 to 0.20 | one, x about 0.24-0.30 |
| 0.25 | 0.310, 0.600, 0.726 |
| 0.30 | 0.322, 0.575, 0.765 |
| 0.40 | 0.347, 0.544, 0.814 |
| 0.50 | 0.374, 0.518, 0.846 |
| 0.70 | one, x about 0.885 |

Full 2-D integration confirms the outer branches are attractors at r = 0.4: from (x, u) = (0.1 to 0.62, 1) the state goes to (0.347, 0.982); from (0.9, 1) it goes to (0.814, 0.091). Quasi-static sweeps of r: forward from 0.1 (steps of 0.01) jumps from x = 0.45 (r = 0.65) to 0.879 (r = 0.66); backward from 0.7 stays high down to r = 0.22 (x = 0.687) and drops to 0.299 at r = 0.21. So the hysteresis loop spans roughly r in [0.215, 0.655] [re-computed in validation; the original text gave the forward jump at r = 0.68 and the backward drop at r = 0.20, i.e. a coarser step]. The middle branch is a saddle: Jacobian eigenvalues at (x, u) = (0.544, u*) and r = 0.4 are +0.82 and -3.05 [computed in validation]. Three observations: the high branch is a "despair" state with efficacy u about 0.09, i.e. drive high and ineffective; recovery needs r to be lowered far below the level that caused the collapse; and the middle branch is the unstable threshold, so **a pulse of discharge (a successful act, outside help) can tip the agent back if it arrives between the middle and high branch values, which is the control lever**. All of this is computed on one hand-picked parameter set.

**Early-warning prediction (testable, from file 53 section 4).** Near the fold, recovery rate from small perturbations of x should slow, and variance and lag-1 autocorrelation of x under noise should rise. The sim can check this in a few lines; doing so tests the code against textbook critical slowing down, not people.

**Empirical standing, blunt.** Learned helplessness has human analogues with weak and contested effect sizes (file 53). Hysteresis in depression is a hypothesis (van de Leemput et al. 2014, file 53), with little direct test. Do not read this section as evidence for bistable human despair.

---

## 4. Cascade thresholds in the coupled population [derived]

Single drive per agent, the u-free cell, so a_i = a(x_i). Assume (a) homogeneous coupling W_ij = w/(N-1) (a mean-field, complete graph), (b) x_i equilibrates fast relative to the social update, so x_i = x*(r_i) the unique equilibrium for fill rate r_i, (c) acting is thresholded: agent acts iff x_i >= theta_i (beta large).

Let phi be the fraction acting. Then r_i = [rho_i + w phi]_+ . The equilibrium level satisfies r (1 - x) = c a(x) x. Define R(theta) = c a(theta) theta / (1 - theta) (u = 1): the fill rate at which the equilibrium level equals theta. x* is increasing in r (the cell has a unique equilibrium, increasing r moves the left side up) [derived], so agent i acts iff rho_i + w phi >= R(theta_i), i.e. iff

phi >= phi_i* := (R(theta_i) - rho_i) / w   (for w > 0; for w < 0 the inequality reverses and the map below is decreasing, so the Granovetter results do not transfer: validation note).

If the heterogeneity (rho_i, theta_i) induces a CDF H(.) of phi_i* over the population, then

phi_{n+1} = G(phi_n) := H(phi_n).

This is **exactly Granovetter's map r(t+1) = F[r(t)]** (file 66, section 1) with F = H; the threshold distribution is derived from drive parameters rather than primitive. Consequences, all from 066 [derived there]: monotone convergence to the least fixed point at or above the starting fraction; **no oscillation**; **cascade iff there is a seed fraction phi_0 such that G(phi) > phi on [phi_0, phi_f)** and the final fraction is the first crossing from above; the outcome is discontinuous in the mean of phi_i*. Stated in sim terms, the cascade threshold in coupling strength w_c is the smallest w for which H(phi) = phi has a solution above the seed; if phi_i* happens to be normal on the 0-100 scale with mean 25, the fold is at sigma about 12.2, as computed in 066.

**What the quasi-static assumption hides.** If x_i relaxes on a time comparable to the social update (relaxation rate about r + c a), the dynamics are no longer a 1-D map: delayed fill gives a lag, and with a hard threshold and reset (Mirollo-Strogatz) one gets pulses and, for identical agents, synchrony [standard account]. The sim should therefore run both regimes and show which regime a claim lives in. The prediction to test against the analytic G: for a fast relaxation parameter, simulated final fractions equal the fixed points of H to numerical precision.

**Network version.** Replacing the complete graph by a sparse graph changes the criterion to Watts's percolation condition (file 66 section 2). The sim should first replicate the complete-graph case and only then move to sparse graphs.

**Heterogeneity versus control.** Two populations with the same mean phi_i* can differ in outcome (Granovetter's point, 066). The practical consequence for control: shifting the mean does not predict the cascade; what matters is the lower tail of H near the seed. This is the one place the minimal sim gives a falsifiable *intervention* statement.

---

## 5. Coupling signs and the three behaviours to look for

With K >= 2 drives and cross-drive entries, three qualitative regimes can appear, all as properties of the model not of people:

1. **Winner-take-all within an agent**: C^{kl} large positive for k != l (acting on l discharges k, or the reverse inhibits). Yields mutual exclusion of acts, the "conflict" of file 48. Reference results (from 048 and 062): for fixed weight coupling the equilibria are the Nash equilibria of the joint game [derived, 062].
2. **Contagion**: W^{kk}_{ij} > 0. This is the cascade of section 4.
3. **Soothing**: W^{kl} < 0 for the matching drive (fear in j reduces fear in i, e.g. via safe-base). This damps cascades; the critical w_c rises.

The sim's first matrix of tests: sweep a single scalar gain on W from negative to positive across N = 2, 10, 100, 1000 and show regime changes against the analytic H-map of section 4 and the boundedness result.

---

## 6. Where Helbing et al. and Strogatz enter the sim

- **Helbing**: not as a force model (this sim has no space) but as the *resource-coupling pattern*. A shared limited exit throughput is a third kind of coupling: agents' discharge s_i is reduced by others' simultaneous acting, s_i = c u a_i x_i / (1 + gamma sum_j a_j), a congestion term. This produces a faster-is-slower analogue: raising urgency (rho, fill) raises a, which lowers per-agent discharge, so mean discharge can fall as urgency rises. Check numerically in the sim; **I did not run this and it is not claimed**. It is the first extension to add and is flagged as an assumption not a source result.
- **Helbing eq. 4 (p mixing)** corresponds to a convex combination of "own signal" and "neighbour average" in the choice of target; in the sim the same form can set the influence on a_i: effective drive x~_i = (1-p_i) x_i + p_i <x_j>_i. This is the same structure as the consensus aggregators in file 66 (weighted mean toward neighbours) and the stubbornness weights of file 63.
- **Strogatz / Mirollo**: the sync test and the Kuramoto-style order parameter R = |(1/N) sum_j exp(i phi_j)| for oscillating drives (a drive that fills, fires, resets). The prediction to check is the Mirollo-Strogatz one: identical agents synchronise; heterogeneity of rho spreads the phases, and above a critical width of the rho distribution synchrony is lost, the Kuramoto-type threshold. The functional form of the critical width in this model is not known; do not import 2/(pi g(0)) without deriving it.

---

## 7. Falsifying checks (pass/fail), separating code correctness from model correctness

**Code correctness (should always pass):**
1. Bounded: for random W, C of either sign and N up to 1000, all x_ik remain in [0,1] to integration tolerance. [derived guarantee]
2. K = 1, N = 1, no coupling, u = 1: the equilibrium solves x = r/(r + c a(x)); matches an independent root-finder to 1e-6. (Not the section 3 table: that table is for the u-dynamic cell, whose equilibria solve r(1-x) = c mu a(x) x/(mu + nu h(x)); corrected in validation.)
3. u fixed: exactly one equilibrium for a monotone act function across a grid of parameters (the section 3 claim).
4. With the despair extension: the saddle-node fold in r matches the analytic fold from the quasi-static curve (existence of three roots between the folds) and hysteresis appears in sweeps, with slowing of recovery near the fold.
5. Mean-field cascade: simulated final fraction acting equals the least fixed point of H for fast relaxation, and sigma_c reproduces the 066 value 12.2 when H is set to the normal CDF with mean 25.
6. Pulse-coupled limit: identical agents in the hard-threshold, reset version synchronise from random starts (Mirollo-Strogatz).

**Model correctness (can fail, and failure is informative):**
7. Whether cascade-threshold w_c predicted from fitted drive parameters matches an observed outcome in any real data set. None is attached yet; 075 and 076 list candidate data.
8. Whether hysteresis is observed in a longitudinal stress-response record (needs repeated measures spanning the fold; none identified).
9. Whether faster-is-slower occurs in a real bottleneck; the sim reproduces the congestion term only by construction.

Candid status: checks 1-6 test the implementation. They cannot show the model describes anyone. Of the model-correctness checks, none has data yet.

---

## 8. What exists vs what does not

**Exists:**
- A bounded, positively-invariant fill-discharge cell (derived here; standard in compartment and population models).
- Granovetter's monotone-map cascade theory (read, 066) and its extension to sparse graphs (Watts, 066).
- Helbing et al.'s simulation showing clogging and faster-is-slower at a bottleneck, with the equations (read here) and a call for data.
- Mirollo-Strogatz synchrony of pulse-coupled oscillators, and the Kuramoto family (not read here).
- Early-warning statistics near a fold (Scheffer, van de Leemput; file 53).

**Does not exist, as far as found:**
- A published fill-and-discharge *social* model with K drives, pairwise coupling matrices and a proof of boundedness plus cascade criterion; this file's section 2-4 is my construction, assembled from the above.
- An empirical estimate of any W^{kl}_{ij} for a human dyad that could populate the coupling matrix (the 049 and 070 searches found only dyadic or sub-drive magnitudes).
- A published test of any fill-and-discharge drive cell against human data.
- Evidence that human despair is bistable with hysteresis rather than a continuous decline.
- A derivation of the sync-loss threshold for the specific cell used here.

---

## 9. Unconfirmed

- Mirollo & Strogatz 1990: model details and the theorem are [standard account]; the 403 on the Cornell PDF prevented reading. The exact conditions (concavity, N, "almost all initial conditions", absorption rules) must be confirmed before building on them.
- The Strogatz & Mirollo 1988 content (what was proved for lattices, random pinning) was not read; the seed's year may refer to one of these or to another Strogatz 1988 item.
- Whether the Nature version of Helbing et al. changes parameters or figures relative to the preprint read here.
- Experimental tests of faster-is-slower: existence now partly confirmed in validation by Crossref title/author resolution only (not read): Garcimartín, Pastor, Ferrer, Ramos, Martín-Gómez & Zuriguel (2015), "Flow and clogging of a sheep herd passing through a bottleneck", *Phys. Rev. E* 91:022808, DOI 10.1103/PhysRevE.91.022808; Pastor, Garcimartín, Gago, Peralta, Martín-Gómez, Ferrer et al. (2015), "Experimental proof of faster-is-slower in systems of frictional particles flowing through constrictions", *Phys. Rev. E* 92:062817, DOI 10.1103/PhysRevE.92.062817; Saloma, Perez, Tapang, Lim & Palmes-Saloma (2003), "Self-organized queuing and scale-free behavior in real escape panic", *PNAS* 100:11947-11952, DOI 10.1073/pnas.2031912100 (mice; abstract read: it tests arch formation, queuing and burst-size distributions, not faster-is-slower as such). The "mixed outcomes" characterisation is still unchecked.
- Whether the section 3 hysteresis width is robust: a one-parameter-set demonstration only; a systematic scan over (tha, thh, nu, mu, B) was not done.
- The quasi-static equilibrium claim "x* increasing in r" is derived for the u = 1 cell with a monotone a; checked analytically, and the root table is consistent, but not tested across random parameters.
- The congestion extension (section 6) has not been simulated.
- ~~Whether the middle branch is a saddle~~: resolved in validation, eigenvalues +0.82 and -3.05 at r = 0.4 (one parameter set only).

---

## Validation log (2026-10-29)

Every DOI re-resolved at api.crossref.org this pass; the Helbing preprint (arXiv cond-mat/0009448v1) re-extracted with pdftotext and checked line by line; section 3 re-computed independently in a scratchpad. The web-search budget was exhausted at the first query, so no "nothing exists" claim in section 8 could be tested by search; they stand as the author's, untested.

- ✓ Granovetter 1978, AJS 83(6):1420-1443, 10.1086/226707 (Crossref: Granovetter, 1978-05). Page cites (1425, 1427) and sigma_c 12.2 / 12.222 match file 066, which read the scan.
- ✓ Helbing, Farkas & Vicsek 2000, *Nature* 407(6803):487-490, 10.1038/35035023 [read, preprint]. Eqs. 2-4, m = 80 kg, tau = 0.5 s, A = 2e3 N, B = 0.08 m, k = 1.2e5, kappa = 2.4e5, v0 0.6 / 1 / <1.5 m/s, diameters [0.5, 0.7] m, 0.73 persons/s through 1 m at v0 about 0.8, "could not find suitable data", faster-is-slower "if the friction parameter kappa is large enough", clogging above 1.5 m/s, jamming at widenings, optimal mixture of individualism and herding: all match the text. ✎ added the paper's own wording for p_i.
- ✎ Mirollo & Strogatz 1990, SIAM J. Appl. Math. 50(6):1645-1662, 10.1137/0150098 (Crossref: 1990-12). Abstract read via Crossref: model, pulse rule and almost-all synchrony confirmed; ✎ added credit to Peskin (1975) for the underlying model, which the file omitted. Concavity condition and proof still [standard account].
- ✓ Strogatz & Mirollo 1988, Physica D 31(2):143-168, 10.1016/0167-2789(88)90074-7: title, authors, venue confirmed; content not read (no abstract at Crossref).
- ✓ Strogatz & Mirollo 1988, J. Phys. A 21(13):L699-L705, 10.1088/0305-4470/21/13/005: confirmed; content not read. (File gave "L699" only; full range added here.)
- ✓ Helbing & Molnár 1995, PRE 51(5):4282-4286, 10.1103/PhysRevE.51.4282: confirmed; not read, cited only.
- ✓ Vicsek, Czirók, Ben-Jacob, Cohen & Shochet 1995, PRL 75(6):1226-1229, 10.1103/PhysRevLett.75.1226: confirmed; not read, cited only.
- ? Lorenz 1950 (Symp. Soc. Exp. Biol. 4:221-268), Tinbergen 1951 (*The Study of Instinct*, Oxford), Kuramoto 1984 (Springer): no DOIs; details agree with the standard bibliography but were not fetched this pass (search budget exhausted).
- ? van de Leemput et al. 2014: cited through file 053, which resolved it (PNAS 111(1):87-92, 10.1073/pnas.1312114110); not re-checked here.
- ✎ Section 3 numbers: root table reproduced to three decimals at every listed r; attractors at r = 0.4 reproduced ((0.347, 0.982) and (0.814, 0.091)). ✎ Sweep fold locations corrected (forward jump at 0.65-0.66, not 0.68; backward drop at 0.22-0.21, not 0.20); summary point 2 corrected to match. ✎ Middle branch confirmed a saddle (eigenvalues +0.82, -3.05), moved out of Unconfirmed.
- ✎ Section 7 check 2 pointed at the wrong table (the u-dynamic one); corrected.
- ✓ Derivations: boundedness on [0,1] (sign of the vector field at the faces), uniqueness of the u = 1 equilibrium for monotone a, R(theta) and the reduction to a Granovetter map all check. Note the reduction phi >= (R(theta_i) - rho_i)/w assumes w > 0; for w < 0 the inequality flips and H is a survival function, so soothing coupling does not give the monotone-increasing map.
- ✎ Faster-is-slower experiments: three studies resolved at Crossref and added to Unconfirmed with what is and is not read.
- No fabrications found; nothing deleted.

**Verdict.** The file is accurate where it claims to have read: the Helbing transcription matches the preprint exactly, every DOI resolves to the stated authors, venue and year, and the derived results hold. The computed hysteresis numbers were right in substance but the sweep fold locations were reported on a coarser grid than stated and have been tightened; the Mirollo-Strogatz entry was upgraded from standard account to abstract-read and now credits Peskin for the model. The section 8 absence claims remain untested by search this pass.

---

## Cross-checks (2026-10-29)

Compared against the other files in this directory by grep and by reading the overlapping sections. The one contradiction was checked against the primary source (Helbing, Farkas & Vicsek 2000, arXiv cond-mat/0009448v1, pdftotext of the preprint). No other file was edited.

### Agreements

- **Granovetter 1978** (this file 1.2, 4; file 066 sections 1-2; file 05 section 10). Same citation (AJS 83(6):1420-1443, 10.1086/226707); same map r(t+1) = F[r(t)] (p. 1425); same equilibrium at the first crossing from above (p. 1427); same monotone, no-oscillation consequence; same sigma_c about 12.2 (066 computed 12.222) for normal thresholds with mean 25; same "no fit to data" standing. The Watts sparse-graph extension (this file 4; 066 section 2) agrees.
- **Helbing, Farkas & Vicsek 2000** (this file 1.3, 6; file 23 section 3; file 048 line 154; file 05 section 16). Same citation and DOI 10.1038/35035023; same eq. 1-4 form; `p_i` is the paper's "degree of panics" (file 23's validation made the same correction from "nervousness"); faster-is-slower conditional on friction kappa being large enough; clogging above 1.5 m/s; best escape at an intermediate individualism/herding mixture; simulation only, no theorem, no data fit. File 048 explicitly cross-notes agreement with this file's 1.3.
- **Faster-is-slower experiments** (this file 9; file 23 section 3). Both cite Garcimartin et al. 2015, Phys. Rev. E 91:022808, 10.1103/PhysRevE.91.022808. Both say the human evidence is mixed or condition-dependent, and both mark that as unconfirmed or standard account. File 23 additionally lists Soria et al. 2012 (ants), Garcimartin et al. 2014 and Zuriguel et al. 2014; none conflicts with this file, and 081's "mixed outcomes unchecked" is consistent with file 23's own "[standard]".
- **Kuramoto K_c = 2/(pi g(0))** (this file 1.4, 6; file 23 section 2). Same formula, both [standard account]. This file's warning not to import it for the fill cell without a derivation is compatible with file 23.
- **Lorenz and Tinbergen** (this file 1.1; file 16 section 2; file 31). Both: no equations in the source; reservoir, valve, releasing stimulus; the hydraulic picture abandoned in the 1950s-60s on the evidence that aggression does not reliably rise with time since the last bout, both marked secondary or standard account.
- **Despair as a tipping point** (this file 3; file 053 sections 1, 4). Both treat van de Leemput et al. 2014 (PNAS 111(1):87-92, 10.1073/pnas.1312114110) as supporting alternative stable states only at abstract level, and both call hysteresis in human mood a hypothesis. File 053 "Does not exist (a)" (no published equation coupling a control or efficacy variable to a bistable drive state) agrees with this file's "my construction"; file 053 line 190 cross-notes that 081 labels its model as such. The critical-slowing-down signs (rising autocorrelation, variance, slower recovery) agree.
- **Boundedness, equilibria and Nash** (this file 5.1; file 062 section 3.3). Fixed-weight coupled drives give a drive game whose Nash sets equal those of the reward game (062 3.3); this file's citation of that is correct as far as it goes. 062 adds that this gives no uniqueness or convergence, and this file makes no claim to either.
- **Absence of coupling-matrix data** (this file 8; files 049, 070). This file says only dyadic or sub-drive magnitudes were found; 070 summary 1-3 (no fitted matrix for n >= 3, no eigenvalues reported) and 049 summary (only exclusion-to-need-threat is well quantified) agree. File 082 has nothing on these topics to conflict with.
- **Mirollo & Strogatz 1990 / Strogatz & Mirollo 1988**: no other file in this directory discusses them (grep for Mirollo, Peskin, integrate-and-fire and pulse-coupled finds only file 23's Strogatz-Mirollo 1991 and Strogatz-Mirollo-Matthews 1992 entries, which are different papers on Kuramoto incoherence). No overlap to check; 081 section 9 correctly leaves these as standard account.

### Contradictions

1. **Do Helbing's urgency and herding parameters have dynamics?**
   - Here (section 1.3, "Drives/operands" and "Translation"; summary point 5): `v^0` and `p` are "inputs set by the experimenter. Neither has dynamics; nothing fills or discharges", and faster-is-slower arises from bottleneck friction "not from any internal state".
   - File 23 section 3: the paper gives an impatience law, v_i^0(t) = [1 - p_i(t)] v_i^0(0) + p_i(t) v_i^max with p_i(t) = 1 - vbar_i(t)/v_i^0, a positive-feedback loop (waiting raises desired speed, which worsens clogging, which lengthens waiting). File 23's operand list also carries `(x_i, v_i, p_i, v_i^0)`.
   - Primary source checked: the arXiv preprint text reads "One may describe this by increasing the desired velocity according to v_i^0(t) = [1 - p_i(t)] v_i^0(0) + p_i(t) v_i^max ... The time-dependent parameter p_i(t) = 1 - vbar_i(t)/v_i^0 ... is a measure of impatience. Altogether, long waiting times increase the desired velocity, which can produce inefficient outflow. This further increases the waiting times, and so on, so that this tragic feedback can eventually trigger panics." The preprint also headlines the effect as "Faster-Is-Slower Effect due to Impatience".
   - **Verdict: file 23 is right; this file is wrong on this point.** In the paper `v^0` and `p` are state-dependent (a slow, history-driven impatience variable that rises while the agent is blocked), so the paper does contain a drive-like variable that fills with waiting. It is not a fill-and-discharge cell (no discharge law, and it is an output-driven feedback rather than a bounded level), and the eq. 4 herding weight is a fixed `p_i` in the core model, but "no dynamics" and "not from any internal state" overstate. The conclusion that Helbing is a resource-coupling pattern rather than a drive model stands, but the impatience loop is closer to this file's section 3 efficacy-collapse feedback than the text admits. A fix in section 1.3 would reword to "p_i and v^0 are fixed in the core model; an optional impatience law makes them time-dependent."

No other contradictions found. Checked and not contradictory: sigma_c, citation details, the Kuramoto formula, the Lorenz abandonment account, and file 23's and 053's "no equations" or "does not exist" statements.
