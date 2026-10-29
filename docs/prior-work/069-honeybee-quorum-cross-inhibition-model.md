# Prior work 069: honeybee commitment model, pitchfork threshold, N-option form and deadlock-breaking, remapped to committees

Direction: D297 (kind: model; merged from 09 honeybee model and 29 Pais/Seeley cross-check). Date: 2026-10-29. Strand: social-algebra.

**Method.** The primary source for the N-option form was read in full (Reina, Marshall, Trianni, Bose, arXiv 1611.07575v2 = Phys Rev E 95, 052411, downloaded as PDF and text-extracted; equations transcribed below, tagged [read]). Pais et al. 2013 equations were already read from full text in file 29 and are cited, not re-read; the PLoS ONE HTML renders equations as images, so a re-fetch gave structure only. Everything tagged [derived] I derived by hand this session and checked numerically (numpy/scipy, finite-difference Jacobians, ODE integration); scripts are in the session scratchpad, not the repo. Seeley 2010 (book), Seeley and Visscher 2004, Sumpter 2010 (book) were not read; see Unconfirmed. Couzin et al. 2005 was confirmed by search summary only (abstract-level).

DOIs confirmed at Crossref this session: Reina et al. 2017 10.1103/PhysRevE.95.052411; Couzin et al. 2005 10.1038/nature03236; Seeley et al. 2012 10.1126/science.1210361; Pais et al. 2013 10.1371/journal.pone.0073216. My recalled DOI for Seeley and Visscher 2004 (10.1007/s00265-004-0798-7) returned nothing at Crossref and is **not** used.

## 1. The model as a state-space flow

**Operands [read].** A swarm of scouts is partitioned into N+1 sub-populations by proportion: x_u (uncommitted) and x_i (committed to option i), with x_u = 1 - sum_i x_i. Each option has a quality v_i. A "decision" is the first x_i to reach a quorum threshold (Reina 2017, Sec. II A, citing quorum literature).

**Four transition operators [read], general form (Reina Eq. 1 / A1):**

    dx_i/dt = gamma_i x_u  -  alpha_i x_i  +  rho_i x_i x_u  -  x_i * sum_{j=1..N} x_j beta_ji

- gamma_i: discovery (uncommitted -> i, spontaneous, linear in x_u).
- alpha_i: abandonment (i -> uncommitted, spontaneous, linear in x_i).
- rho_i: recruitment (uncommitted -> i, interaction: needs an i-committed bee and an uncommitted one, bilinear).
- beta_ji: cross-inhibition from j onto i (i -> uncommitted, interaction, bilinear x_i x_j). Reina's adjacency factor sets beta_ii = 0 (no self-inhibition; "in accordance with behavioural results", citing Seeley 2012).

So the whole mechanism is two linear (individual) operators and two bilinear (pairwise) operators on one simplex. Inhibited bees return to *uncommitted*, not to the rival option; that is the structural difference from direct-switching (file 29 B2, Marshall 2009).

**Value-sensitive parameterisations.**
- Pais et al. 2013 (N=2, from file 29, [read] there): gamma_i = rho_i = v_i, alpha_i = 1/v_i, beta = sigma constant (value-independent).
- Reina et al. 2017 (N options) [read, Eq. 2]: gamma_i = k v_i, alpha_i = k / v_i, rho_i = h v_i, **beta_ji = h v_j** (the inhibitor's quality, because an advocate of a good option inhibits harder). Control parameter **r = h/k**, the ratio of interaction (signalling) to spontaneous (individual) transitions; dimensionless time tau = k t. In these units, for equal qualities v:

      dx_i/dtau = v x_u - x_i/v + r v x_i x_u - r v x_i sum_{j!=i} x_j        (R)

  (this is Reina Eq. 3 / D3 specialised; I rewrote it with the sum explicit). Reina notes that with r = 1 and beta = const it collapses to Pais's form (Eq. A3 discussion).
- Reina also states the requirement v >= 1 [read, App. B]: below it some states go negative and are not biologically meaningful.

## 2. The pitchfork threshold, re-derived (N = 2, Pais parameterisation)

[Derived; agrees with Pais Eq. 4 and with the check already in file 29.] Symmetric point x_A = x_B = x, U = 1 - 2x. The eigenvalue for an antisymmetric perturbation (delta x_A = -delta x_B) is lambda = rho U - alpha = vU - 1/v, because the sigma terms cancel. lambda = 0 gives U = 1/v^2, x = (v^2-1)/(2v^2); substituting into the equilibrium condition leaves sigma x^2 = v U, hence

    sigma* = 4 v^3 / (v^2 - 1)^2     (exists only for v > 1; ~ 4/v for large v).

Below sigma*, one stable symmetric attractor (deadlock); above, the symmetric point is a saddle and two attractors appear (pitchfork). Numerical confirmation this session: v = 2, sigma* = 3.56; sigma = 3.2 settles at (0.381, 0.381), sigma = 3.91 at (0.488, 0.262).
Reading: **equal high-value options are broken, equal low-value options deadlock**; the stop signal's required strength falls as the options get better. For v <= 1 no sigma breaks the tie.

## 3. The N-option form: what changes

### 3a. The Pais parameterisation cannot break N >= 3 ties [read + derived]

Reina App. B proves (from the reduced system, via a discriminant condition, Eq. B1) that with r = 1 and N = 3 equal options, the non-symmetric equilibria exist only for a *negative* beta: [read, Eq. B4] 8v^3/(1-4v^2) < beta < 0 (for v > 1/2). Since cross-inhibition needs beta >= 0, the only real, stable equilibrium is the symmetric deadlock. N = 2 reduces to Eq. B2 (4 alpha gamma rho / (rho - alpha)^2) and B3 (the sigma* above), so the binary pitchfork is a special case that does not generalise.
[Derived check] Integrating the Pais parameterisation at N = 3 (v = 2, 5) and N = 4 (v = 5) with beta from 0.5 to 50 always converged to the symmetric split ((0.30,0.30,0.30) at beta 0.5, v = 2; (0.118)^3 at beta 50). Consistent with the paper.
**Mechanism (my reading):** with beta constant, an option's inhibition load grows with the *number* of rivals, but so does the uncommitted pool each rival feeds from; the same N-dependence cannot be offset by raising beta alone. Reina's fix decouples signalling (h, interaction) from individual exploration (k) and makes beta scale with v, so the single dial is r.

### 3b. Symmetric N options: two bifurcations in r

[Derived, from (R).] Symmetric point x_i = x, u = 1 - N x. Jacobian J = (a - b) I + b 11^T with
 a = -v - 1/v + r v (u - N x),   b = -v - 2 r v x.
Eigenvalues: a + (N-1) b (the "total commitment" direction, stable) and **a - b, with multiplicity N-1** (every between-option perturbation):

    lambda_between = -1/v + r v ( u - (N-2) x ).

Deadlock loses stability (second bifurcation, r2) when lambda_between = 0, i.e. u - (N-2)x = 1/(r v^2). With w = 1/(r v^2), that gives x = (1-w)/(2(N-1)), and the equilibrium condition collapses to a quadratic in w:

    A w^2 + B w - c^2 = 0,   c = 1/(2(N-1)),   m = N v^2,
    A = c(1+m) - (2N-1) c^2,   B = v^2 - c(2+m) + 2(2N-1) c^2,
    r2 = 1/(w v^2) with w the positive root.

Checked two ways: numerically scanning r for the sign change of lambda_between, and by closed form. Selected values (v = 2 / v = 5): N=2: 1.25 / 0.44; N=3: 5.08 / 4.19; N=4: 12.96 / 12.16; N=6: 40.87 / 40.14; N=8 (numeric): 84.8 / 84.1. For N = 2 at r = 1 the pitchfork falls at v = 1 + sqrt(2), the Reina-parameterisation analogue of sigma*.
Large-v behaviour [derived, fit to the table]: r2 -> approximately 2(N-1)(N-2) from above (e.g. 4.19, 12.16, 24.15, 84.13 at v = 5 against 4, 12, 24, 84). So r2 is **quadratic in N**, and the dependence on quality fades as v grows. [read] Reina states the same: "r1 grows quasi-linearly with N, r2 grows quadratically"; the influence of v decreases quadratically (his Eq. D4, whose printed form did not survive text extraction, so I do not transcribe it; the quadratic above is my own and matches his statements).

First bifurcation r1 (saddle-node: decided states appear while deadlock is still stable). [Derived numerically by bisection on whether a trajectory from a biased start reaches a decided state; approximate to about 0.01.] v = 2 / v = 5: N=3: 2.98 / 1.75; N=4: 4.49 / 3.12; N=5: 5.92 / 4.56. Roughly linear in N, as Reina says. The analytic form is Reina Eq. D2/D4, not transcribed here.

**Phase structure [read].** For N = 3, three phases in r: (I) r < r1, deadlock the only attractor; (II) r1 < r < r2, deadlock coexists with a stable decision for each option (hysteresis; noise or a bias is needed to leave deadlock); (III) r > r2, deadlock is a saddle, stable only along the line x_1 = x_2 = x_3, and a random one of the N options is chosen. For odd N >= 5 extra unstable saddles appear between r1 and r2; they do not change the three macro-phases. No periodic attractors (Reina, Fig. 2 caption).

**Consequence [read, Reina's own reading]:** too many equal options preclude breaking the tie at a given signalling ratio; the cost of tie-breaking rises as N^2. "This result suggests a limit on the maximum number of equal options that can be concurrently evaluated."

### 3c. Best-of-N (one superior, N-1 equal inferior)

[Read, Eq. 3 / A9.] With kappa = v_inferior / v_best, x_A = best, x_B = pooled inferior:

    dx_A/dtau = v x_u - x_A/v + r v x_A [ x_u - kappa x_B ]
    dx_B/dtau = (N-1) kappa v x_u - x_B/(kappa v) + r v x_B [ kappa x_u - ((N-2)/(N-1)) kappa x_B - x_A ]
    x_u = 1 - x_A - x_B

(the reduction aggregates the N-1 inferior sub-populations; Reina states it is qualitatively correct for arbitrarily large N). Four parameters: N, v, kappa, r. [Read] Five phases (A-E) for N = 3 in (r, kappa): at low r there is a single attractor, but the best option's share may be too small to reach quorum; the "dark" low-share region grows with N and shrinks as kappa falls (options more different). Reported timing check: k = 0.1, h = 0.3, v = 10, N = 3 gives convergence on field-experiment timescales if t is read in hours. Abstract's headline [read]: the key parameter is the *relative time spent discovering vs signalling*, with **conflicting pressures** - symmetric choice wants high r (r2 grows with N^2) and best-of-N wants moderate r (too much signalling locks in an inferior early leader) - resolvable by a **time-dependent signalling strategy**.

Weber-law property [read, Fig. 6b]: for N = 2 the minimum value difference separating two options scales with the mean value, Delta v ~ v-bar, with coefficient set by r (by sigma in Pais).

## 4. Empirical standing (blunt)

- The structure (discovery, abandonment, recruitment, stop-signal) is empirically grounded in bees: Seeley et al. 2012 (Science 335, 108-111) observed stop signals aimed at dancers for rival sites [read: abstract, file 29]. The pitchfork/deadlock result is analytic and checked above.
- **The value-sensitive parameterisation (gamma = rho = v, alpha = 1/v, beta ~ v) is an assumption, not a fit.** Reina says so ("we assume ..."). The N-option results (r1, r2, N^2 law) are model predictions with, as far as I found, **no direct experimental test of the N^2 scaling or of phase II hysteresis**. Empirical references for multi-option choices in bees and ants are cited by Reina (refs 21-25) but I did not read them.
- Reina 2023 (Commun Phys; arXiv 2211.09531; abstract only seen) compares cross-inhibition with voter models and finds consensus robust to inflexible ("zealot") individuals and asocial agents, whereas one zealot blocks voter-model consensus. That is a model result, not a human test.
- Human committees: the model is cited as an analogy ("committees of medical experts", Reina's refs 8, 9) with no fitted human data in the source. I found **no human experiment** testing cross-inhibition or the r threshold.

## 5. Remapping to human committees (a proposal; none of this is validated)

| Honeybee object | Committee object | Note |
|---|---|---|
| x_i | share of members publicly committed to proposal i | Operand. Commitment must be observable, as dance and stop signal are. |
| x_u | undecided / listening members | The pool that all four operators pivot on. |
| v_i | perceived value of proposal i, as each member evaluates it | Single shared v is the strong assumption; humans disagree on v. |
| gamma | independent discovery: a member brings in or adopts an option unprompted | Curiosity/search term (file 29 §Liang: scouts vs recruits). |
| alpha = k/v | lapse of commitment unaided; faster for poor options | A motivation-decay operator; "drive fade". |
| rho = h v | advocacy: a member recruits an undecided | Bilinear, needs contact. |
| beta_ji = h v_j | blocking: a member of camp j sends an opponent of j back to undecided | Note it sends to *undecided*, not to the blocker's side. |
| r = h / k | social-to-independent ratio: how much of a member's time goes into lobbying vs fact-finding | The control knob; the same h scales advocacy and blocking, so a group that lobbies more also blocks more. |
| quorum | the threshold at which the chair/rules declare a decision | A separate, exogenous parameter. |

Predictions the model would make for committees, **each conditional on the human mapping and untested**:
1. Equal-quality proposals with low lobbying (r < r1) stalemate, with everyone drifting to undecided mixtures; raising r (more informal contact) breaks the tie, at random.
2. The needed r for a tie among N equal options grows ~N^2, so a long shortlist of near-equals stalls; shortening the list is cheaper than raising lobbying.
3. Hysteresis in phase II: an inert committee stays inert unless shocked; a small bias then tips it.
4. Lobbying has a cost in best-of-N: high r speeds consensus but lets an early inferior proposal win; low r keeps the true best discoverable. Time-dependent r (explore first, then lobby) is the model's own remedy, matching the common practice of an information phase before a debate phase.
5. Low-value deadlock (v <= 1 in Pais's form) cannot be cured by blocking: when no option is attractive, stronger opposition does not make a choice, only gridlock. In algebra terms the committee needs a *value-raising* operator, not a *blocking* operator.

**Operator inventory in the algebra's terms.** Linear operators on one agent's state: discover (u -> i), lapse (i -> u). Bilinear pair operators: recruit (i, u -> i, i), block (j, i -> j, u). Both kinds are Markov-type transition operators on a categorical state; the ODE is their mean-field limit. The model's group-level quantities (r, quorum) are parameters of the interaction operators, not drives, which fits file 29's conclusion that the cluster gives structure, not a new drive.

**Open composition issue.** All terms are mean-field and well-mixed: any committee has a network (who can speak to whom); Reina's A matrix is the placeholder for it (a_ij in {0,1}) and he sets it to all-ones off-diagonal. A non-trivial A is the natural entry point to the algebra (coupling to file 60-style network extensions).

## 6. Seeds not read (state of each)

- **Seeley 2010, *Honeybee Democracy*** (Princeton UP): book; existence confirmed in file 09; not read. It is the natural-history account behind the model.
- **Seeley and Visscher 2004**, Behav Ecol Sociobiol 56(6), 594-601: bibliographic record only found (Dutch library listing); abstract and DOI not found. Quorum size (reported in secondary accounts as roughly 10-20 bees at the site) is not confirmed.
- **Sumpter 2010**, *Collective Animal Behavior*, Princeton UP: not looked up.
- **Couzin, Krause, Franks, Levin 2005**, Nature 433, 513-516 (DOI confirmed): per search summary, uninformed/less informed individuals; larger groups need a smaller informed share; consensus without knowing who is informed. Not read; it is a movement model without a stop-signal operator, so it feeds D301 rather than this model.

## 7. What exists vs what does not

Exists: a closed, small set of transition operators on a simplex with an analytic bifurcation structure; an exact N=2 threshold; an N-option generalisation with two bifurcations, hysteresis and an N^2 deadlock cost; a tuned control parameter r; a plausible empirical correlate (stop signals) for one operator; a clear failure of the naive binary parameterisation at N >= 3.
Does not exist: any human fit of v, r, quorum or the transition rates; a test of the N^2 law or hysteresis in any animal; heterogeneous agents (all scouts identical); network structure; any treatment of *why* an agent values an option (v is given, not generated by drives). In the strand's terms, this is a decision machine that takes drives as input (v) and says nothing about them.

## Unconfirmed

- Reina Eq. D4 closed form (garbled in text extraction); my quadratic for r2 replaces it and is verified numerically only for the cases listed.
- r1 values are numerical, approximate, and depend on my "decided state" criterion.
- Seeley and Visscher 2004 DOI and quorum size; Sumpter 2010 details; Reina's refs 8, 9, 21-25.
- The human-committee table is a mapping proposal, not sourced.
