# Prior work 068: Epstein's civil-violence rule, recast as grievance composed with fear

Direction: D254

Date: 2026-10-29. Kind: model. Brief: replicate Epstein's civil-violence rule, recast it as a composition of grievance and fear, and look for analytic phase results. Seeds: Epstein 2002. From: 24.

**Method and honesty note.** Epstein (2002) was read in full at source (PMC128592 full text; the five displayed equations are images in PMC and were each downloaded and read as images, so they are transcribed exactly, tagged [read]). The replication in section 3 is my own quick re-implementation from the paper's text, run in scratch space, not in the repo, single seeds and short runs: indicative, not a validated replication. The mean-field algebra in section 4 is derived here ([derived]); it was checked numerically but not against the published figures. Follow-up literature: Thron & Jackson (arXiv preprint, read in full), Ormazabal et al. (PRE, read the abstract, introduction and phase-diagram passages), Zou et al. 2012 and Fonoberova et al. 2019 (abstracts only, [from abstract]).

Cross-references: 24 (collective action; this model was added there in validation), 05 (Granovetter thresholds), 39 (deterrence), 58 (honour-culture retaliation thresholds), 60 (n-actor extensions), 23 and 29 (collective dynamics).

---

## 1. Primary source

**Citation.** Epstein, J. M. (2002). Modeling civil violence: an agent-based computational approach. *Proceedings of the National Academy of Sciences* 99 (suppl. 3), 7243-7250. doi:10.1073/pnas.092080199 (Crossref confirmed, issue "suppl_3"). Full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC128592/ (open on PMC; the PNAS site itself is behind a bot wall).

**Their vocabulary.** Agents (general population) and cops; active versus quiescent; hardship H, legitimacy L, grievance G, risk aversion R, estimated arrest probability P, net risk N, threshold T, vision v, jail term, "deception" (private grievance hidden), "tension", "ripeness". Epstein states that "no political or social order is represented in the model" and "the dynamics of decentralized upheaval, rather than its political substance, is the focus". He also states plainly "I make no pretense to measuring model variables such as perceived hardship or legitimacy."

**Drives/operands.** There is no drive vocabulary as such. The operands are agent attributes: H (exogenous, per agent, U(0,1)), L (exogenous, equal across agents, varied 0 to 1 in runs), R (per agent, U(0,1), fixed for life), and the local count of cops and active agents within vision. G is a felt grievance; N is a felt fear (risk-weighted). Both are internal graded states, so this is the nearest existing formal object to "two drives composed into an action rule" that the survey has found.

**Operators / equations, exact.**

- Grievance [read]: G = H(1 - L). The text: "Grievance is the product of perceived hardship (H) and perceived 'illegitimacy', if you will (1 - L)." Justification given is intuition only (British legitimacy in the Blitz, L = 1, so no grievance despite extreme hardship).
- Arrest estimate [read, image]: P = 1 - exp[-k (C/A)_v]. k is "set to ensure a plausible estimate (of P = 0.9) when C = 1 and A = 1"; Table 2 gives k = 2.3 (approximately ln 10 = 2.3026, so P ≈ 1 - 0.1^(C/A), which is how Thron & Jackson write it as their eq. 4 [read]; with k = 2.3 exactly, P(C = A = 1) = 0.8997). A counts the agent itself, so A is at least 1.
- Net risk [read]: N = R P (stated as the alpha = 0 case of N = R P J^alpha, J the jail term; alpha = 0 in the paper, hence no deterrent effect of longer jail terms).
- Agent rule A [read, image]: if G - N > T be active; otherwise, be quiescent. T is a non-negative threshold ("could be zero"), set to 0.1 in all runs. Table 1: Q to A if G - N > T; A to Q if G - N <= T. So the rule has no memory: it is re-evaluated each activation.
- Cop rule C [read, image]: inspect all sites within v* and arrest a random active agent.
- Movement rule M [read, image]: move to a random site within your vision (both agents and cops). Asynchronous random-order activation.
- Jail [read]: arrested actives get a term drawn from U(0, J_max); agents leave jail exactly as aggrieved as they entered.
- Interpretation [read]: G - N is "the expected utility of publicly expressing one's private grievance" and T "the expected utility of not expressing it (preference falsification, in Kuran's terminology)". Individual rationality is "local": the agent's calculation excludes the effect of its own act on the social order.
- Tension index [read]: ripeness = (mean G)(mean fraction quiescent) / (mean R). Epstein gives it as a candidate warning indicator ("a buildup of tension precedes each outburst") and shows it in one run only.

Run settings [read, Table 2 and footer]: 40 x 40 torus, initial agent density 0.7, asynchronous updating, T = 0.1, k = 2.3. Run columns (garbled by the PMC table extraction, reading the order as given): cop/agent vision 1.7, 7, 7, 7 | 1.7, 1.7, 1.7; legitimacy 0.89, 0.82, 0.9, 0.8 | 0.9, 0.8, 0.8; max jail 15, 30, infinite, infinite | 15, 15, 15; initial cop density 0.04, 0.04, 0.074, 0.074 | 0, 0, 0.04. Which run produced which figure is not cleanly recoverable from the PMC text; unconfirmed.

**Results reported [read].** All are simulation outcomes, none proved.

1. Individual "deception": aggrieved agents go quiescent when cops are near and active when cops leave.
2. Free assembly catalyses outbursts: a chance cluster of actives lowers local C/A, lowers P, and recruits the mildly aggrieved ("a single spark can cause a prairie fire"). Epstein reads this as the rationale for banning assembly and for curfews.
3. Punctuated equilibrium: long quiet spells broken by outbursts, persisting over 20,000 iterations.
4. Waiting time between outbursts (outburst = more than 50 actives): over 100,000 iterations, mean 60, SD 55; "suggests a Weibull or perhaps Lognormal"; after truncating waiting times under 30, a negative exponential fit with R-squared 0.98, slope -0.07, intercept 3.5 (OLS on logged data). Epstein says rigorous identification is "a suitable topic for future research".
5. Outburst size (total activation): mean 708, SD 230, no distribution identified.
6. "Salami tactics": legitimacy cut from 0.9 to 0.2 in small steps produced no spike; a single cut from 0.9 to 0.7 at t = 77 produced an explosion. Epstein's reading: "It is the rate of change—the derivative—of legitimacy that emerges as salient". (The small steps are "of a percent per cycle". Epstein's text calls the jump "the absolute legitimacy reduction (of 0.30)", but 0.90 to 0.70 is 0.20; the inconsistency is in the source, and which number is the typo is not recoverable from the text.)
7. Cop reductions produce a tipping point under incremental decline of cops, unlike incremental legitimacy decline (Tocqueville: "liberalization is the most difficult of political arts").
8. Model II (two ethnic groups, going active means killing out-group members; births and deaths): with L = 0.8 and no cops, genocide in 30 of 30 runs, victor random (competitive exclusion); peacekeepers deployed early give safe havens; at cop densities of 0 to 0.1 (50 runs per density, 15,000-cycle cap) mean time to genocide rises with peacekeeper density ("the larger the initial force of peacekeepers, the more time one buys") but the SD rises too. Fig. 16 overlays a best linear fit; the text reports no slope or fit statistic, so "linear" is Epstein's plotted fit, not a reported result.

**Theorems or derived predictions.** The paper contains none. Section 4 derives some.

**Empirical standing, blunt.** Epstein does no data fitting; the paper says so. The model is qualitative, a generator of "recognisable macroscopic regularities". Thron & Jackson (below) say the product form G = H(1 - L) "is based solely on a plausibility argument by Epstein, and has never been verified by any empirical studies", and that R and T "have never been subject to statistical study". I did not find a test of the model's quantitative predictions against riot data. See section 5.

---

## 2. Recast: grievance and fear as drives, and the rule as a composition

This is a modelling proposal, built from the equations above. The operand/operator split follows the survey's style (compare 16 and 47).

**Operands per agent i.**
- gamma_i: grievance drive, a scalar in [0,1). It is itself a composite: gamma_i = H_i (1 - L), a product of hardship (an exogenous felt-cost) and attributed illegitimacy (the share of the cost laid at the authority's door). The product has the useful zero: gamma = 0 whenever L = 1, however large H.
- phi_i: fear drive, phi_i = R_i P_i, a product of a trait (risk aversion) and a situational estimate (arrest probability).
- T: a threshold, the "cost of speaking" (Kuran's preference falsification), in this model a global constant.
- Environment variables the agent reads off its neighbourhood: C (cops in sight), A (actives in sight including self).

**Operators.**
1. Attribution: gamma = H (1 - L). Multiplicative, bilinear in the two inputs.
2. Appraisal of danger: P = 1 - exp(-k C/A). A saturating, strictly monotone function of one scalar, the local repression ratio rho = C/A.
3. Trait scaling: phi = R P (multiplicative).
4. Net drive: u_i = gamma_i - phi_i, signed addition of an approach drive and an avoidance drive. This is exactly Miller's approach-minus-avoidance form (16, section 3), with the avoidance term nonlinear in the environment.
5. Gate: action a_i = 1 if u_i > T, else 0. A hard threshold, equivalent to Hull's reaction threshold (16, section 1) or to a Granovetter threshold (05) once u is read as a function of crowd state (below).
6. Social transmission: every active agent in sight raises A, which lowers rho, lowers P, lowers phi for every neighbour. So an active agent *lowers the fear drive of others* while not changing their grievance. Call this operator "safety-in-numbers": phi_j -> phi_j * (1 - exp(-k C/(A+1))) / (1 - exp(-k C/A)), a multiplicative reduction of fear. No operator raises grievance in neighbours (contagion of anger is absent). This asymmetry is a finding about the model, not about people: the only coupling between agents is through fear.
7. Repression: a cop arrests an active agent: removes it from the pool for a random time and raises C/A locally. In the algebra, a sink operator acting on the active set, with no effect on gamma (explicitly: "leaves jail exactly as aggrieved").

**Composition in one line.** a_i = [ H_i (1 - L) - R_i (1 - exp(-k C/A)) > T ].

**Granovetter form, derived here.** For agent i, with g_i = H_i (1 - L) and quantities held fixed, the rule is a threshold in the crowd ratio. The agent is active iff P < (g_i - T)/R_i, that is iff C/A < theta_i where theta_i = -ln(1 - (g_i - T)/R_i) / k, valid when 0 < (g_i - T)/R_i < 1. If g_i - T <= 0 the agent is never active (inert); if (g_i - T)/R_i >= 1 the agent is active for any crowd (extremist). Equivalently, activation needs the actives-to-cops ratio A/C > 1/theta_i = k / (-ln(1 - (g_i - T)/R_i)). So Epstein's rule is a Granovetter threshold model (05) in which the threshold is not a free draw but a computed composition of three attributes, and the "fraction already acting" is replaced by a ratio to the repressive force. This is the cleanest sense in which the rule is "grievance composed with fear": grievance sets how much crowd the agent needs, fear sets how steeply that need rises with the cops' presence.

**What the recast adds to the algebra.** (a) Two drives with opposite signs composing additively into a net propensity, with trait multipliers. (b) A gate that turns the continuous net drive into discrete action, so a drive algebra needs a read-out. (c) An asymmetric coupling: action reduces others' fear. (d) A hidden-versus-expressed split: gamma is private and persistent; action is public and revocable. Epstein's two-screen display is the same distinction, and the dissociation between them (blue left, red right) is his "tipping point" notion.

---

## 3. Replication attempt (mine, indicative only)

Implemented from the paper text in a scratch Python script (not in the repo): 40 x 40 torus, 70% agents, T = 0.1, k = 2.3, H and R uniform, Euclidean vision radius, asynchronous random-order updates, cops move-and-arrest as described, jail terms U(0, J_max), released agents reappear at a random empty site, one seed each, 800 to 2,000 steps. The paper does not specify some details (release site, whether cops move before or after inspecting, tie handling, whether vision is a Euclidean radius), so these are my choices.

| Setting | Rule | Result |
|---|---|---|
| v = 7, L = 0.82, J_max = 30, cop density 0.04, 1,500 steps | Epstein's exponential P | mean actives 0.8, max 16, **no outbursts** |
| v = 7, same, 800 steps | NetLogo-style floor rule P = 1 - 0.1^floor(C/A) | mean actives 33, max 350, 28 outbursts, mean wait 23.7 (SD 6.1) |
| v = 1.7, L = 0.82, J_max = 30, cops 0.04, 2,000 steps | exponential P | mean actives 259, max 371: persistent mass rebellion |
| v = 1.7, L = 0.89, J_max = 15, cops 0.04, 2,000 steps | exponential P | mean actives 64, max 83, hovering at the outburst threshold (6 crossings, mean wait 1.5) |

Reading: with the equations as printed and a wide vision, I did **not** reproduce punctuated outbursts or the mean-60 waiting time. The floor-function rule does produce outbursts. This agrees with Thron & Jackson, who state that Epstein's original response function "has no critical crowd size (and hence exhibits no outbursts)" and that the widely distributed NetLogo Rebellion model uses a floor function that does ([read] in their paper; Wilensky's NetLogo code itself not inspected). I did not reproduce Epstein's waiting-time distribution or his salami-tactics result. One reason it may differ is the unreported details above; another is that the published figures came from code that differs from the printed rule. I cannot tell which from the paper. Treat the replication as **not achieved from the text alone**, with a partial hit once the NetLogo variant is used.

---

## 4. Analytic phase results

### 4.1 Derived here: the homogeneous mean-field response function [derived, checked numerically]

Let g = 1 - L and assume H and R are independent U(0,1) as in the paper, with g > T (otherwise nobody is ever active). The fraction of agents who are active when their arrest estimate is P is the probability that H g - R P > T. Integrating over R first gives a closed form:

- if P < g - T: f(P) = 1 - T/g - P/(2g)
- if P >= g - T: f(P) = (g - T)^2 / (2 g P)

Checks: continuous at P = g - T (both give (g - T)/(2g)); f(0) = 1 - T/g (the maximum active fraction; a fraction T/g of agents is inert, so L_max-style bound: nobody acts when L >= 1 - T because H <= 1); f(1) = (g - T)^2/(2g), the extremist fraction. Thron & Jackson state the same two limits ((G_max - T)^2/(2 G_max) and 1 - T/G_max, [read]) without giving the full f; mine reproduces them.

Corollary (zero-cop critical legitimacy): with H ~ U(0,1) and no cops, anyone can be active only if g > T, i.e. L < 1 - T. For T = 0.1 this is L < 0.9. This explains why Epstein's L = 0.9 runs need other help. Ormazábal et al. report, for a one-dimensional lattice without police, a "dashed line of critical legitimacy Lc = 1 − 2T" [read], which is the boundary where active and passive concentrations are equal (AP to PA phases), obtained by assuming "an average agent" (mean H = 0.5, so mean G = 0.5(1 - L) = T); the same algebra at the mean, but a different quantity from the L < 1 - T bound here. Their all-passive "consensus" phase appears at L = 0.90 for T = 0.10 [read], which is exactly the L >= 1 - T bound above.

### 4.2 Derived here: mean-field fixed points have no bistability [derived, numeric scan]

Closing the loop: let x be the active fraction among non-jailed agents, kappa = k c/rho (cop to agent density times k) in the large-vision limit, so P(x) = 1 - exp(-kappa/x), and x = f(P(x)). Because f is decreasing in P and P is decreasing in x, F(x) = f(P(x)) is increasing in x: positive feedback. F(0+) = (g - T)^2/(2g) > 0, so x = 0 is never a fixed point once extremists exist.

I scanned this numerically, including the finite-vision version with A = 1 + N x (so a lone rioter faces P = 1 - exp(-k C)), for L in {0.5, 0.7, 0.8}, T = 0.1, vision populations N in {10, 30, 107} and cop counts C from 0.05 to 30. In every case there is **exactly one fixed point**: no hysteresis, no saddle-node, no discontinuous jump. As cops rise the fixed point falls steeply but continuously (L = 0.8, T = 0.1, large-vision limit: x = 0.37 at kappa 0.02, 0.12 at kappa 0.028, 0.046 at kappa 0.036, floor of 0.025 = extremist fraction at large kappa). So the homogeneous mean field has a smooth but sharp crossover, not a first-order transition. This matches Thron & Jackson's simulation finding of "no tipping points" and smooth change in behaviour with parameters [read] and is a derived analytic statement, not a published theorem. It leaves out the jail sink and heterogeneity in local cop count.

### 4.3 What produces outbursts: spatial fluctuation, not mean-field instability

Source: Thron, C. & Jackson, E. "Practicality of Agent-Based Modeling of Civil Violence: an Assessment", arXiv:1501.05838 [physics.soc-ph], v1 22 Jan 2015 (Texas A&M University-Central Texas; arXiv comments: presented at the IOSSBR conference, Fall 2012, Biloxi MS, "JSSR 2013, Volume II"); full text read via pdftotext.

Thron & Jackson argue the outbursts in the model are "entirely produced by lapses in cop coverage": cops are placed randomly so cop count in a vision circle is Poisson, and where it happens to be low a knot of actives forms and spreads ([read]). Their analytic claims, stated at the level of argument rather than proof:

- The model is a Markov chain, so waiting times between outbursts are approximately exponential (memoryless) beyond a time window, which gives a mechanism for Epstein's exponential tail.
- The model "exhibits self-organized criticality": instability starts at random sites, is sudden, propagates to neighbours, and relaxes at the origin; hence outburst sizes should be roughly power-law. They support this with ACLED riot-size data for Africa and Nigeria showing heavier-than-exponential tails.
- Their reduced characterisation: all population behaviour is fixed by the activist response function f(y), y = A/C, with four numbers (extremist fraction, inert fraction, critical crowd size, saturation crowd size). They replace Epstein's response by a logistic one (exponent p) in their own implementation ("'Logistic' is the function implemented in this paper"). The logistic function and exponent are their own modification, not Epstein's. (Corrected in validation: the phrase "reduces the number of free parameters" in their abstract refers to the f(y) characterisation, not to the logistic choice.) Their cop rule also differs slightly from NetLogo's (cops arrest before moving), and they use L drawn per agent, unlike Epstein's common L.
- Their simulation sweeps (their own set-up, not Epstein's: 80 x 80 grid, 4,480 agents, 152 cops, vision 7, J_max 100, 1,000 steps, 200 simulations per parameter set; excitable fraction 0.6 to 1.0, etc.): outburst frequency rose about 1000-fold across excitable fraction 0.6 to 1.0; a 10% fall in critical crowd size gave about 25% more outbursts (and about 25% larger peaks); doubling the extremist fraction slightly *reduced* outburst frequency (about 5%), which they attribute to extremists being almost always in jail and call "due to unrealistic features of the model".

Because Epstein himself reported an exponential tail only after truncating the short waits and called the full distribution Weibull or lognormal, and Thron & Jackson's Markov argument gives exponential only "past a certain time window", the two do not conflict, but nothing here is a proof of Epstein's figures.

### 4.4 Statistical-physics treatment

Ormazabal, Urbina, Borotto & Astudillo (2022), "Phase diagram in a one-dimensional civil disorder model", *Physical Review E* 105, 054110, doi:10.1103/physreve.105.054110 (Crossref matched; arXiv:2110.00835). [read, arXiv full text via pdftotext, key passages]: they say "nobody characterized this agent-based model using concepts and tools of statistical physics in its original form"; they simulate a 1-D version with Moore and random neighbourhoods (and do not use Epstein's motion rule), introduce a Potts-like energy, build a phase diagram from agent-state concentrations, report order-disorder phases (without police: active-majority AP, passive-majority PA, a disordered phase, and an all-passive consensus phase; with police: six ordered majority phases, one disordered and the consensus phase) with transitions they describe as continuous, a "principle of minimum grievance", and the critical-legitimacy line L_c = 1 - 2T above. This is the first statistical-physics phase diagram I found for the model, but it is numerical, one-dimensional, and the transition character is read from stationary distributions, not proved.

### 4.5 Coarse-graining

Zou, Fonoberov, Fonoberova, Mezic & Kevrekidis (2012), "Model reduction for agent-based social simulation: Coarse-graining a civil violence model", *Physical Review E* 85, 066106, doi:10.1103/PhysRevE.85.066106 (Crossref confirmed) [from abstract and search summary]: reduces a civil-violence ABM to "only two coarse-grained degrees of freedom: the number of jailed citizens and the number of active ones", cutting computation time "by a factor of approximately 20" [from abstract, re-read on the APS page in validation]. I did not read the reduced equations or any bifurcation analysis; unconfirmed. Fonoberova, M., Mezić, I., Mezić, J., Hogg, J. & Gravel, J. (2019), "Small-world networks and synchronisation in an agent-based model of civil violence", *Global Crime* 20(3-4), 161-195, doi:10.1080/17440572.2019.1662304 (Crossref confirmed) [from abstract via search, not re-read in validation]: adds a Watts-Strogatz small-world network to Epstein's model; reports more frequent large outbursts at low law-enforcement and a synchronisation effect. Full text not read.

---

## 5. What exists versus what does not

**Exists.**
- A fully specified, small, two-drive rule (grievance H(1-L), fear R(1-exp(-kC/A)), net drive threshold) with the coupling between agents through fear alone. Exact equations are read from the primary text.
- An exact closed-form single-agent activation threshold in the crowd ratio (derived here from the printed rule) and an exact mean-field response function f(P).
- A mean-field result that the printed rule has a unique, smooth fixed point, so the model's punctuated dynamics come from spatial fluctuation in cop coverage (matches an independent simulation study).
- Independent argument (Markov chain, self-organised criticality) for exponential waiting times and power-law sizes, and a first statistical-physics phase diagram (1-D).
- A documented fork: the NetLogo Rebellion model uses a floor-function arrest estimate, different from Epstein's printed formula, and that fork is the one that produces outbursts.

**Does not exist (that I found).**
- A replication of Epstein's own waiting-time and size distributions from the printed rule; mine did not reproduce them.
- Empirical estimation of H, L, R, T or P against riot or protest data; Thron & Jackson say there is "no empirical evidence" that any existing sociological measure is suitable as H or L, that the product form is untested, and that there is "no practical or theoretical grounding for determining the value of T".
- A grievance dynamic: G is static (agents leave jail "exactly as aggrieved"); no anger accumulation, no contagion of anger, no habituation, no effect of arrest or repression on grievance (backlash). So the model is a fear-coupling model with a fixed grievance field, not a two-drive dynamical system. Fear is likewise memoryless: P is recomputed from the neighbourhood each step.
- An analytic first-order or second-order transition proof for the 2-D model.
- Group-level drives: no group variable beyond the local counts.
- A fit of the recast algebra to data.

**Implication for the algebra.** The cheap, defensible primitives are the signed net-drive composition (gamma minus phi with trait multipliers), the threshold gate, and the safety-in-numbers coupling operator. The deductions to carry forward are the Granovetter form theta_i = -ln(1 - (g_i - T)/R_i)/k and the unique-fixed-point mean-field result. What would need new equations is the missing half: a grievance state that evolves (see 53 on despair and 58 on honour thresholds for candidate dynamics).

---

## Unconfirmed

- Which run of Table 2 produced which of Epstein's figures; the PMC table extraction is garbled.
- Whether Epstein's published results used the printed exponential rule; I could not reproduce outbursts with it, and Thron & Jackson's claim that the NetLogo version differs was read at second hand (their paper), not by inspecting Wilensky's NetLogo source.
- Thron & Jackson's publication venue: the arXiv record (arXiv:1501.05838, v1 2015) says it was presented at the IOSSBR conference (Fall 2012) and cites "JSSR 2013, Volume II", presumably the conference's journal; no DOI found and the JSSR item was not located (web search budget exhausted in validation). Treat it as conference-reviewed at most.
- Fonoberova et al. 2019: the small-world and synchronisation content is supported by the Crossref title; the "more frequent large outbursts at low law-enforcement" finding was not re-read in validation (publisher page returned 403).
- Zou et al. 2012 and Fonoberova et al. 2019 content beyond their abstracts, including whether any bifurcation or analytic phase result is derived there.
- Ormazabal et al.: transitions are stated "continuous" from their numerical stationary distributions; whether the 2-D model has the same phases is untested there.
- My own replication (single seeds, unspecified details) and my mean-field algebra: the latter is an exact integral I checked at several points, but it assumes H and R uniform and independent, G uniform product with fixed L, and ignores jail and spatial correlation. Not independently checked against the literature beyond the two limits in Thron & Jackson.
- Moro (2016), PLoS ONE 11(4): e0154175, doi:10.1371/journal.pone.0154175, was found (abstract only; Crossref record exists) as an extension of the model type to violent revolutions with a revolutionary organisation; not read, not used above.

## Validation log (2026-10-29)

- ✎ Epstein 2002, PNAS 99 suppl. 3, 7243-7250, doi:10.1073/pnas.092080199: Crossref confirmed (title, sole author, volume, issue suppl_3, pages). Quotes re-checked on PMC128592 [read]: grievance product, Blitz justification, k set for P = 0.9 at C = A = 1 and Table 2 k = 2.3, N = R P J^alpha with alpha = 0, T "could be zero" and 0.1, U(0, J_max) jail, "exactly as aggrieved", Kuran/expected-utility reading, "local" rationality, tension/ripeness, 20,000 iterations, waiting times (threshold 50, 100,000 iterations, mean 60, SD 55, truncation at 30, R² 0.98, slope -0.07, intercept 3.5), size mean 708 SD 230, salami tactics, Tocqueville, Model II (n = 30, L = 0.8, victor random, safe havens). Corrected: k = 2.3 is approximately, not exactly, ln 10; flagged the source's own "0.30" vs 0.90-to-0.70 inconsistency; "rises roughly linearly" reworded to Epstein's plotted linear fit (no fit statistic in text). Equation images not re-read in validation.
- ✎ Thron & Jackson, arXiv:1501.05838 (2015): existence and authorship confirmed on arXiv; full text read via pdftotext. All quoted phrases found. Corrected: "reduce the number of free parameters" was misattached to the logistic choice (it refers to their f(y) characterisation); "no measure of H or L fits" reworded to their actual claim; added their own simulation set-up and the ~5% extremist effect. Venue partly resolved (IOSSBR 2012, "JSSR 2013, Volume II"); no DOI.
- ✎ Ormazábal, Urbina, Borotto & Astudillo 2022, PRE 105, 054110, doi:10.1103/physreve.105.054110: Crossref confirmed; arXiv:2110.00835 full text read. Corrected: L_c = 1 - 2T is their line of equal active and passive concentrations (average-agent assumption), not a no-activity bound; phases with police (six ordered) added; "nobody characterized" and "continuous" confirmed.
- ✓ Zou, Fonoberov, Fonoberova, Mezić & Kevrekidis 2012, PRE 85, 066106, doi:10.1103/PhysRevE.85.066106: Crossref confirmed; abstract re-read on APS (two coarse variables, factor ~20).
- ✎ Fonoberova, Mezić, Mezić, Hogg & Gravel 2019, Global Crime 20(3-4), 161-195: Crossref confirmed; full author list, title and DOI 10.1080/17440572.2019.1662304 added. Findings beyond the title not re-read (publisher 403) → partly in Unconfirmed.
- ✓ Moro 2016, PLoS ONE 11(4) e0154175, doi:10.1371/journal.pone.0154175: Crossref confirmed (title "Understanding the Dynamics of Violent Political Revolutions in an Agent-Based Framework", sole author). Not used in the body.
- ? Wilensky (2004) NetLogo Rebellion model: cited only via Thron & Jackson's ref. [2] and their eq. (5); source code not inspected (already in Unconfirmed).
- ✓ Derived results re-checked: the closed-form f(P) re-derived by hand (both branches, continuity, limits match Thron & Jackson's (G_max - T)²/(2G_max) and 1 - T/G_max with G_max = 1 - L); Granovetter threshold theta_i re-derived; large-vision fixed points recomputed (x = 0.368, 0.121, 0.046, floor 0.025 at kappa 0.02, 0.028, 0.036, large) and a scan over kappa in (0, 1] for L = 0.5, 0.7, 0.8 found exactly one fixed point each. The finite-vision scan and the section 3 replication were not rerun.
- No fabrications found; nothing deleted. The "nothing exists" items in section 5 were not re-tested by search (web search budget exhausted this turn); they stand as the author's "that I found".

**Verdict.** The note is sound: every cited work exists with the stated authors and DOIs, Epstein's equations and numbers check against the PMC text, and the derived mean-field algebra and fixed-point numbers reproduce exactly. The errors were of attribution and paraphrase rather than substance: Ormazábal et al.'s L_c = 1 - 2T is an equal-concentration line, not an activity bound; a Thron & Jackson quote was attached to the wrong claim; and k = 2.3 is only approximately ln 10. The section 5 absence claims remain unsearched in validation.

## Cross-checks (2026-10-29)

Checked by grep against every other file in this directory for Epstein, Thron & Jackson, Ormazabal, Zou, Fonoberova, Moro, Wilensky and the equations and numbers above. Only 067 overlaps in depth; 24, 66, 81, 53 and 58 cite this file or Epstein's rule at summary level. No other file mentions Ormazabal, Zou, Fonoberova or Moro. The primary-source recheck was attempted (PNAS and Europe PMC blocked or errored from the box, so nothing was re-read at PMC128592 this pass).

### Agreements

- **067 section 1 (Epstein equations).** G = H(1 - L); P = 1 - exp[-k (C/A)_v], k = 2.3 (about ln 10, P(1,1) about 0.90); N = R P (J^alpha extension, alpha = 0); Rule A with T = 0.1; 40 x 40 torus, density 0.7, vision 1.7 or 7, cops 0.04, J_max 15/30/infinite; jail leaves agents "exactly as aggrieved"; "no pretense" quote. Same in both. 067 read the Brookings working paper, this file the PNAS text, so the match also confirms the PNAS equations equal the working paper's.
- **067 section 1 (derived threshold).** 067's x_i* = -(1/k) ln(1 - (G_i - T)/R_i) is this file's theta_i (section 2), with the same inert (G - T <= 0) and extremist (G - T >= R) cases. 067 credits the reduction to Thron & Jackson; this file labels it derived here. Consistent, but the credit should be shared: Thron & Jackson sec. 4.1 got there first.
- **067 and this file, Thron & Jackson (arXiv:1501.05838).** Plausibility-only G, R and T unstudied, outbursts from lapses in cop coverage (Poisson), no critical crowd size so no outbursts in the printed form, NetLogo floor form credited to Wilensky (2004) via their ref. 2, extremist fraction (Gmax - T)^2/(2 Gmax) and inert fraction T/Gmax. Venue (IOSSBR 2012, "JSSR 2013, Volume II", no DOI) identical in both.
- **067 results (c), (d), (e).** Punctuated equilibrium over 20,000 iterations, salami tactics (0.9 to 0.2 in small steps no spike; 0.9 to 0.7 at t = 77 explosion), cop reductions tipping: agree with results 3, 6, 7 here. Both note the source's "0.30" versus 0.20 point only here (067 flags it as not in 067).
- **067 "only fear is coupled downward".** Same as operator 6 here. 24 (section 10, Gaps, and its validation correction) says no formal downward function exists in the motivational theories while Epstein is the formal exception; consistent with this file's section 5.
- **067 item 4 and this file section 4.2.** 067 said the mean-field fixed point was not carried out; this file does it (one fixed point, no hysteresis). That fills the gap, not a conflict.
- **066 (line 228) and 24 (line 185).** Epstein's rule as a Granovetter threshold with a state-dependent shift, using G = H(1 - L). Consistent with the Granovetter form in section 2.
- **53 (line 190), 58 (line 225), 81 (header).** These cite this file for the missing grievance dynamic, for the threshold parameterisation theta_i that 58 section 7 lacks, and as a cross-reference respectively. Claims agree; 58 and this file both state no quantitative honour-culture threshold exists.

### Contradictions and tensions

1. **Tension index: buildup or dip.** This file (Tension index bullet) quotes "a buildup of tension precedes each outburst". 067 (section 1) says the true warning is a pronounced dip just before an outburst. Source: per 067's re-extraction of the Brookings working paper, both sentences appear in the same section, buildup first, then "our tension curve dips just at the outset of major explosions. The true warning indicator is this pronounced dip." **Verdict: both are quotations, but this file's phrasing could mislead; the dip is Epstein's stated warning indicator in the working paper. Whether the dip sentence survives in the PNAS text is unresolved** (I could not retrieve the PNAS text this pass: pnas.org returns a bot wall, Europe PMC full text returned a 500). Suggested wording for the bullet: buildup precedes outbursts, but the working paper names a dip as the true indicator. The index definition itself (G x fraction quiescent / mean R) agrees in both. Figure number differs (PNAS Fig. 8, working paper Fig. 7).
2. **Which runs used cop density 0.074.** 067: runs 3-5 (working paper count). This file: columns garbled, read as runs 3 and 4 only. **Unresolved**; the PNAS table cannot be recovered from the PMC extraction, and the two files read different documents.
3. **Do the printed rule's runs produce outbursts.** 067 reports Epstein's outbursts and Thron & Jackson's denial unreconciled. This file's replication found none at v = 7 but persistent or threshold-hovering activity at v = 1.7, leaning toward Thron & Jackson. **Unresolved**: single unseeded runs on my side, and Wilensky's code is uninspected in both files.
4. **Thron & Jackson "no tipping points" versus Epstein's cop-tipping (result 7).** The mean-field scan here (section 4.2) supports Thron & Jackson for the homogeneous version only; 067 lists the tension as open. **Unresolved for the spatial model.**
5. **Wording hazard.** 063 lists "Friedkin & Johnsen 1999" (*Advances in Group Processes*) as a different work from Friedkin 1999 (*ASR*); not an Epstein issue, noted only because 067 flags it. No change needed here.

No numerical contradiction was found in the equations, parameters or quoted Epstein results across files.

## Licences of quoted and transcribed material (2026-10-30)

Audit verdict for this file: five flagged items, all "check"; no text changed.

- **Epstein (2002), PNAS 99 suppl. 3, 7243-7250, doi:10.1073/pnas.092080199 (PMC128592).** Licence: not determined; publisher copyright presumed (free to read on PMC). Used as: short quotations (grievance definition, expected-utility interpretation, k and P = 0.9, salami-tactics sentence, each under 60 words); restated equations (grievance, arrest estimate, agent rule); the agent rule of Table 1 given as a two-line description; Table 2 run settings given as the values actually used (k = 2.3 and the vision, legitimacy, jail and cop-density settings), not reproduced as a table, with the PMC extraction noted as garbled; the variable-name list (about 17 terms) is a list of names, which are facts.
- **Thron & Jackson (2015), arXiv:1501.05838.** Licence: not determined; publisher copyright presumed (arXiv licence for this record not checked). Used as: short quotations, restated equations, description of their reduced model and simulation sweeps. They used ACLED riot-size data for Africa and Nigeria; no ACLED data is carried into this repo (dataset citation only; if figures are added, record the ACLED terms of use).
- **Ormazabal, Urbina, Borotto & Astudillo (2022), Physical Review E 105, 054110, arXiv:2110.00835.** Licence: not determined; publisher copyright presumed (arXiv licence not checked). Used as: description of results; the phase classes (about 9) are a prose paraphrase of the phase diagram, not a copied figure.
- **Zou, Fonoberov, Fonoberova, Mezic & Kevrekidis (2012), Physical Review E 85, 066106.** Licence: not determined; publisher copyright presumed. Used as: two short quotations from the abstract.
- **Fonoberova et al. (2019), doi:10.1080/17440572.2019.1662304.** Licence: not determined; publisher copyright presumed. Used as: citation and description only.
- **Moro (2016), PLoS ONE 11(4) e0154175.** Licence: not determined here (PLOS journals normally publish under CC BY); citation only, not read or used in the body.
- **Kuran, Tocqueville, Brookings material (via file 067).** Cited at second hand; short attributed phrases only.
- **Wikipedia:** no Wikipedia-derived text in this file.
