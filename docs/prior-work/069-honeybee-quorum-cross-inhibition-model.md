# Prior work 069: honeybee commitment model, pitchfork threshold, N-option form and deadlock-breaking, remapped to committees

Direction: D297 (kind: model; merged from 09 honeybee model and 29 Pais/Seeley cross-check). Date: 2026-10-29. Strand: social-algebra.

**Method.** The primary source for the N-option form was read in full (Reina, Marshall, Trianni, Bose, arXiv 1611.07575v2 = Phys Rev E 95, 052411, downloaded as PDF and text-extracted; equations transcribed below, tagged [read]). Pais et al. 2013 equations were already read from full text in file 29 and are cited, not re-read; the PLoS ONE HTML renders equations as images, so a re-fetch gave structure only. Everything tagged [derived] I derived by hand this session and checked numerically (numpy/scipy, finite-difference Jacobians, ODE integration); scripts are in the session scratchpad, not the repo. Seeley 2010 (book), Seeley and Visscher 2004, Sumpter 2010 (book) were not read; see Unconfirmed. Couzin et al. 2005 was confirmed by search summary only (abstract-level).

DOIs confirmed at Crossref this session: Reina et al. 2017 10.1103/PhysRevE.95.052411; Couzin et al. 2005 10.1038/nature03236; Seeley et al. 2012 10.1126/science.1210361; Pais et al. 2013 10.1371/journal.pone.0073216. My recalled DOI for Seeley and Visscher 2004 (10.1007/s00265-004-0798-7) returned nothing at Crossref and is **not** used. [Validation 2026-10-29: the correct DOI is 10.1007/s00265-004-0814-5, confirmed at Crossref: Seeley, Visscher, "Quorum sensing during nest-site selection by honeybee swarms", Behav Ecol Sociobiol 56(6), 594-601. It is Reina's ref 30.]

## 1. The model as a state-space flow

**Operands [read].** A swarm of scouts is partitioned into N+1 sub-populations by proportion: x_u (uncommitted) and x_i (committed to option i), with x_u = 1 - sum_i x_i. Each option has a quality v_i. A "decision" is the first x_i to reach a quorum threshold (Reina 2017, Sec. II A, citing quorum literature).

**Four transition operators [read], general form (Reina Eq. 1 / A1):**

    dx_i/dt = gamma_i x_u  -  alpha_i x_i  +  rho_i x_i x_u  -  x_i * sum_{j=1..N} x_j beta_ji

- gamma_i: discovery (uncommitted -> i, spontaneous, linear in x_u).
- alpha_i: abandonment (i -> uncommitted, spontaneous, linear in x_i).
- rho_i: recruitment (uncommitted -> i, interaction: needs an i-committed bee and an uncommitted one, bilinear).
- beta_ji: cross-inhibition from j onto i (i -> uncommitted, interaction, bilinear x_i x_j). Reina's adjacency factor sets beta_ii = 0 (no self-inhibition; "in accordance with behavioural results", citing Seeley 2012).

So the whole mechanism is two linear (individual) operators and two bilinear (pairwise) operators on one simplex. Inhibited bees return to *uncommitted*, not to the rival option; that is the structural difference from direct-switching (file 29 B2, Marshall, Bogacz, Dornhaus, Planqué, Kovacs, Franks 2009, J R Soc Interface 6, 1065-1074, doi 10.1098/rsif.2008.0511, Crossref-confirmed; Reina's ref 12).

**Value-sensitive parameterisations.**
- Pais et al. 2013 (N=2, from file 29, [read] there): gamma_i = rho_i = v_i, alpha_i = 1/v_i, beta = sigma constant (value-independent).
- Reina et al. 2017 (N options) [read, Eq. 2]: gamma_i = k v_i, alpha_i = k / v_i, rho_i = h v_i, **beta_ji = h v_j** (the inhibitor's quality, because an advocate of a good option inhibits harder). Control parameter **r = h/k**, the ratio of interaction (signalling) to spontaneous (individual) transitions; dimensionless time tau = k t. In these units, for equal qualities v:

      dx_i/dtau = v x_u - x_i/v + r v x_i x_u - r v x_i sum_{j!=i} x_j        (R)

  (this is Reina Eq. 3 / D3 specialised; I rewrote it with the sum explicit). Reina's App. B treats the model of Eq. A3 with r = 1 and constant beta as the Pais parameterisation ("equivalent to the case r = 1"); with r = 1 alone, Reina's own beta = h v is not constant, so both conditions are needed.
- Reina also states the requirement v >= 1 [read, App. B]: below it some states go negative and are not biologically meaningful.

## 2. The pitchfork threshold, re-derived (N = 2, Pais parameterisation)

[Derived; agrees with Pais Eq. 4 and with the check already in file 29.] Symmetric point x_A = x_B = x, U = 1 - 2x. The eigenvalue for an antisymmetric perturbation (delta x_A = -delta x_B) is lambda = rho U - alpha = vU - 1/v, because the sigma terms cancel. lambda = 0 gives U = 1/v^2, x = (v^2-1)/(2v^2); substituting into the equilibrium condition leaves sigma x^2 = v U, hence

    sigma* = 4 v^3 / (v^2 - 1)^2     (exists only for v > 1; ~ 4/v for large v).

Below sigma*, one stable symmetric attractor (deadlock); above, the symmetric point is a saddle and two attractors appear (pitchfork). Numerical confirmation this session: v = 2, sigma* = 3.56; sigma = 3.2 settles at (0.381, 0.381), sigma = 3.91 at (0.488, 0.262).
Reading: **equal high-value options are broken, equal low-value options deadlock**; the stop signal's required strength falls as the options get better. For v <= 1 no sigma breaks the tie.

## 3. The N-option form: what changes

### 3a. The Pais parameterisation cannot break N >= 3 ties [read + derived]

Reina App. B proves (from the reduced system, via a discriminant condition, Eq. B1) that with r = 1 and N = 3 equal options, the non-symmetric equilibria exist only for a *negative* beta: [read, Eq. B4] 8v^3/(1-4v^2) < beta < 0 (for v > 1/2). Since cross-inhibition needs beta >= 0, the only real, stable equilibrium is the symmetric deadlock. N = 2 reduces to Eq. B2 (4 alpha gamma rho / (rho - alpha)^2) and B3 (the sigma* above), so the binary pitchfork is a special case that does not generalise.
[Derived check] Integrating the Pais parameterisation at N = 3 (v = 2, 5) and N = 4 (v = 5) with beta from 0.5 to 50 always converged to the symmetric split ((0.30,0.30,0.30) at beta 0.5, v = 2; (0.118, 0.118, 0.118) at beta 50, v = 2). [Validation re-ran these: confirmed; also v = 5, beta 50 gives 0.169 each at N = 3 and 0.133 each at N = 4.] Consistent with the paper.
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

(the reduction aggregates the N-1 inferior sub-populations; Reina states it is qualitatively correct for arbitrarily large N). Four parameters: N, v, kappa, r. [Read] Five phases (A-E) for N = 3 in (r, kappa): at low r there is a single attractor, but the best option's share may be too small to reach quorum; the "dark" low-share region grows with N and shrinks as kappa falls (options more different). Reported timing check (Fig. 7): k = 0.1, h = 0.3, v = 10, N = 3, kappa in {0.25, 0.5, 0.75} gives convergence on field-experiment timescales if t is read in hours (Reina cites Seeley and Buhrman 2001 for the field times). Note: Reina's App. text says the dark area "decreases with the difference in option's qualities (i.e., higher κ)", which contradicts itself (higher kappa is a *smaller* difference); his Fig. 3 text (low share "if r is small and κ sufficiently high") supports the reading given here. Abstract's headline [read]: the key parameter is the *relative time spent discovering vs signalling*, with **conflicting pressures** - symmetric choice wants high r (r2 grows with N^2) and best-of-N wants moderate r (too much signalling locks in an inferior early leader) - resolvable by a **time-dependent signalling strategy**.

Weber-law property [read, Fig. 6b]: for N = 2 the minimum value difference separating two options scales with the mean value, Delta v ~ v-bar, with coefficient set by r (by sigma in Pais).

## 4. Empirical standing (blunt)

- The structure (discovery, abandonment, recruitment, stop-signal) is empirically grounded in bees: Seeley et al. 2012 (Science 335, 108-111) observed stop signals aimed at dancers for rival sites [read: abstract, file 29]. The pitchfork/deadlock result is analytic and checked above.
- **The value-sensitive parameterisation (gamma = rho = v, alpha = 1/v, beta ~ v) is an assumption, not a fit.** Reina says so ("we assume ..."). The N-option results (r1, r2, N^2 law) are model predictions with, as far as I found, **no direct experimental test of the N^2 scaling or of phase II hysteresis**. Empirical references for multi-option choices in bees and ants are cited by Reina (refs 21-25: Lindauer 1955, Z vergl Physiol 37, 263; Seeley 2010, *Honeybee Democracy*; Seeley and Buhrman 2001, Behav Ecol Sociobiol 49, 416; Franks, Dornhaus, Best, Jones 2006, Anim Behav 72, 611; Robinson, Franks, Ellis, Okuda, Marshall 2011, PLoS ONE 6, e19981; identified from Reina's reference list in validation) but none was read.
- Reina, Zakir, De Masi, Ferrante 2023, "Cross-inhibition leads to group consensus despite the presence of strongly opinionated minorities and asocial behaviour", Commun Phys 6, 236, doi 10.1038/s42005-023-01345-3 (Crossref-confirmed; arXiv 2211.09531; abstract only read). Per the abstract: two opposed factions of inflexible minorities, or individuals switching on individual rather than social information, can hold a population in persistent indecision; compared with the voter model (equal options) and the weighted voter model (unequal options), cross-inhibition alone reaches a stable majority despite such asocial behaviour; mean-field results confirmed with 100 locally interacting robots. [Corrected in validation: the earlier claim that "one zealot blocks voter-model consensus" is not in the abstract and is removed.] A model and robot result, not a human test.
- Human committees: the model is cited as an analogy ("committees of medical experts", Reina's refs 8, 9: Kurvers, Krause, Argenziano, Zalaudek, Wolf 2015, JAMA Dermatol 151, 1346; Wolf, Krause, Carney, Bogart, Kurvers 2015, PLoS ONE 10, e0134269; both are collective-diagnosis studies, not tests of cross-inhibition) with no fitted human data in the source. I found **no human experiment** testing cross-inhibition or the r threshold.

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

- **Seeley 2010, *Honeybee Democracy*** (Princeton UP): book; existence confirmed in file 09 and in validation (Crossref e-book record doi 10.1515/9781400835959; Reina's ref 22); not read. It is the natural-history account behind the model.
- **Seeley and Visscher 2004**, "Quorum sensing during nest-site selection by honeybee swarms", Behav Ecol Sociobiol 56(6), 594-601, doi 10.1007/s00265-004-0814-5 (Crossref-confirmed in validation; Reina's ref 30). Abstract not obtained (publisher elides it; Springer page paywalled). Quorum size (reported in secondary accounts as roughly 10-20 bees at the site) is not confirmed.
- **Sumpter 2010**, *Collective Animal Behavior*, Princeton UP: existence confirmed in validation (Crossref e-book record doi 10.1515/9781400837106, author Sumpter); not read.
- **Couzin, Krause, Franks, Levin 2005**, Nature 433, 513-516 (DOI confirmed): per search summary, uninformed/less informed individuals; larger groups need a smaller informed share; consensus without knowing who is informed. Not read; it is a movement model without a stop-signal operator, so it feeds D301 rather than this model.

## 7. What exists vs what does not

Exists: a closed, small set of transition operators on a simplex with an analytic bifurcation structure; an exact N=2 threshold; an N-option generalisation with two bifurcations, hysteresis and an N^2 deadlock cost; a tuned control parameter r; a plausible empirical correlate (stop signals) for one operator; a clear failure of the naive binary parameterisation at N >= 3.
Does not exist: any human fit of v, r, quorum or the transition rates; a test of the N^2 law or hysteresis in any animal; heterogeneous agents (all scouts identical); network structure; any treatment of *why* an agent values an option (v is given, not generated by drives). In the strand's terms, this is a decision machine that takes drives as input (v) and says nothing about them.

## Unconfirmed

- Reina Eq. D4 closed form (garbled in text extraction); my quadratic for r2 replaces it and is verified numerically only for the cases listed.
- r1 values are numerical, approximate, and depend on my "decided state" criterion.
- Seeley and Visscher 2004 quorum size (DOI now confirmed); Sumpter 2010 contents; contents of Reina's refs 8, 9, 21-25 (identified, not read).
- The claim that no human experiment tests cross-inhibition or the r threshold: the validation pass could not run a confirming search (search budget exhausted), so it rests on the original session's search only.
- The human-committee table is a mapping proposal, not sourced.

## Validation log (2026-10-29)

- ✓ Reina, Marshall, Trianni, Bose 2017, Phys Rev E 95, 052411, doi 10.1103/PhysRevE.95.052411 (Crossref) — re-read arXiv 1611.07575v2 in full: Eq. 1, Eq. 2 (beta_ij = h v_i in Reina's indexing = beta_ji = h v_j here), Eq. 3, A9, B1-B4, v >= 1, three macro-phases, odd-N saddles, five phases A-E, Fig. 6b Weber law, quotes on r1/r2 scaling and "limit on the maximum number of equal options" all match. ✎ App. A3/r = 1 remark tightened; ✎ the paper's own κ parenthetical flagged as self-contradictory.
- ✓ Pais, Hogan, Schlegel, Franks, Leonard, Marshall 2013, PLoS ONE 8, e73216, doi 10.1371/journal.pone.0073216 (Crossref) — sigma* = 4v^3/(v^2-1)^2 matches Reina Eq. B3; numerics (3.56; (0.381,0.381); (0.488,0.262)) reproduced.
- ✓ Seeley, Visscher, Schlegel, Hogan, Franks, Marshall 2012, Science 335, 108-111, doi 10.1126/science.1210361 (Crossref; PubMed abstract): stop signals aimed at dancers for competing sites; is Reina's ref 5 for "no self-inhibition".
- ✓ Couzin, Krause, Franks, Levin 2005, Nature 433, 513-516, doi 10.1038/nature03236 (Crossref; PubMed abstract) — summary matches abstract.
- ✎ Seeley and Visscher 2004, Behav Ecol Sociobiol 56, 594-601 — DOI found: 10.1007/s00265-004-0814-5; quorum size still ?.
- ✎ Reina et al. 2023, Commun Phys 6, 236, doi 10.1038/s42005-023-01345-3 — co-authors added (Zakir, De Masi, Ferrante); unsupported "one zealot blocks voter-model consensus" removed, summary rewritten from the abstract.
- ✎ Marshall et al. 2009, J R Soc Interface 6, 1065, doi 10.1098/rsif.2008.0511 — full citation added.
- ✓ Seeley 2010, *Honeybee Democracy* — exists (Crossref doi 10.1515/9781400835959); not read.
- ✓ Sumpter 2010, *Collective Animal Behavior* — exists (Crossref doi 10.1515/9781400837106); not read.
- ✎ Reina refs 8, 9, 21-25 — identified from the reference list and named; not read, not DOI-resolved.
- ✓ [derived] items — r2 table (N = 2, 3, 4, 6, 8 at v = 2, 5), large-v limit 2(N-1)(N-2), N = 2, r = 1 threshold v = 1 + sqrt 2, and N = 3/4 deadlock under the Pais parameterisation all reproduced independently. r1 values not re-checked.
- ? "No human experiment tests cross-inhibition" — not re-tested (validation search budget exhausted).

Verdict: the file is sound. Every equation transcribed from Reina 2017 matches the source, and every derived number reproduced. The errors were in the secondary items: a wrong summary of Reina 2023's voter-model result (now corrected from the abstract), Reina 2023's missing co-authors, and a Seeley and Visscher 2004 DOI the file said it could not find (now found). Nothing was fabricated.

## Cross-checks (2026-10-29)

Checked against the validated files in this directory (grep for Pais, Reina, Seeley, Marshall, Couzin, Sumpter, cross-inhibition, quorum, pitchfork). Files with overlap: 29, 09, 048, 046, 16, 060, 066, 081. No web check was needed: the one numeric disagreement was settled by recomputation.

### Agreements

- **Pais et al. 2013 equations** (§1, §2 here) agree with 29 §B1 (Eq. 1 deterministic part, gamma = rho = v, alpha = 1/v, sigma value-independent, sigma indexed by the inhibiting site) and with 048 §2 (same Eq. 1 structure; Reverdy-Koditschek Eq. 7 reduces to it).
- **Threshold sigma\* = 4v^3/(v^2-1)^2**, existing only for v > 1 and tending to 4/v, agrees with 29 §B1 (Eq. 4, re-derived there) and 048 §2. The broken-state numbers at sigma ~ 3.9 (about (0.49, 0.26)) agree with 29's simulation at 1.1 sigma\*.
- **Credit for the pitchfork and deadlock result** to Seeley et al. 2012 (Science 335, 108-111) agrees with 29 §B1 ("originally theirs") and 048 §2 ("previously [13] calculated").
- **Marshall et al. 2009** (direct switching, J R Soc Interface 6, 1065-1074) agrees with 29 §B2 and its correction note: a different mechanism from stop-signal cross-inhibition, which sends inhibited bees to uncommitted.
- **Weber-law property** (Delta v ~ v-bar, coefficient set by sigma) agrees with 29 §B1 (Pais Eq. 5) and 048 §2 (K controlled by sigma, lower sigma gives lower K).
- **Citations** agree across files: Seeley 2012 DOI 10.1126/science.1210361 (09 §D5, 29, 048); Seeley and Visscher 2004, Behav Ecol Sociobiol 56(6), 594-601 (09 §D5; this file adds the DOI); Seeley 2010 and Sumpter 2010 as books (09 §D4, §D5); Couzin et al. 2005 summary (09 §D3) and its being a movement model with no stop-signal operator (09, 29).
- **Structural claim** that this is the most algebra-ready object (operators on a simplex) agrees with 29 §B1; 048 §2 reaches the same reading for the single-agent case.

### Contradictions and discrepancies

1. **Symmetric equilibrium at v = 2, sigma = 0.9 sigma\* (29 §B1 vs here §2).** 29 reports (0.41, 0.41) from a forward-Euler run; this file reports (0.381, 0.381). Verdict: **this file is right.** Solving the symmetric equilibrium condition v U - x/v + v x U - sigma x^2 = 0 with U = 1 - 2x at v = 2, sigma = 3.2 gives x = 0.38129 exactly (checked this session). The 0.41 in 29 is probably an unconverged Euler run. The qualitative conclusion in 29 is unaffected. File 29 is not edited.
2. **Equation number of the threshold in Pais 2013.** 29 §B1 calls it Eq. 4; 048 §2 calls it Eq. 3 and says it was illegible in the extraction. Verdict: **unresolved**, but 29 read the equation images from full text and this file (§2) follows 29; the number does not affect any result. Reina's own numbering (B3) is unambiguous.
3. **Direction of the dependence on stop-signal strength (048 §2 iii vs 29/this file).** 048 notes that Pais's introduction says stronger cross-inhibition raises the minimum mean value above which deadlock breaks, while the Fig. 2 caption says the required sigma falls as v rises. This file (§2) and 29 follow the caption version. Verdict: **this file and 29 are right**, because sigma\* = 4v^3/(v^2-1)^2 is decreasing in v (derived and numerically confirmed here); the introduction's wording is the loose one. Consistent with 048's own recommendation.
4. **N-option form, status in 29.** 29 §B1 lists arXiv 1611.07575 as "not DOI-checked". Not a contradiction: this file read it in full and confirmed Phys Rev E 95, 052411 at Crossref. 29's Unconfirmed list can be updated from here.
5. **Parameter scope (048 §2 vs here §3a).** 048 treats the Pais parameterisation as the algebra of "two equal drives resolve or stay stuck". This file shows, from Reina App. B, that the same parameterisation cannot break ties at N >= 3 for any non-negative sigma. This is not a factual conflict, but 048's translation should be read as N = 2 only.

No contradiction was found with 09, 16, 046, 060, 066 or 081: their only overlaps are generic uses of "cross-inhibition" (Atkinson-Birch/CTA in 046 and 16) or of pitchfork and saddle-node bifurcations (060, 066, 081), with no shared equation or number.
