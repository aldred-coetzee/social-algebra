# Prior work, cluster 29: animal groups as systems of interacting drives

Date: 2026-10-29. Strand: social-algebra. Extends `09-biology-ecology.md` (Vicsek, Couzin 2002/2005, Sumpter, Seeley basics, Ballerini, primates, Hinde, evolutionary game theory, Price); this file does not repeat those and goes into models with state variables, explicit equations and derived results.

## Verification status

- **Confirmed** = title, authors, venue, year resolved at api.crossref.org by DOI (or by bibliographic query that returned the DOI). 22 works below.
- **Equation forms are the standard textbook/review forms, tagged [standard account]**, written from general knowledge, NOT re-derived from full text. Tag [read] means I read the abstract or a search summary of the paper, not the full paper. No full text of any paper was read in this pass. Treat every equation as "check before building on".
- **Validation pass 2026-10-29** (see log at end): every DOI re-resolved at Crossref; abstracts read (Europe PMC) for Marshall 2009, Seeley 2012, Couzin 2011, Rosenthal 2015, Flack 2006, Strandburg-Peshkin 2015, Harcourt 2009, Jolles 2017, Muro 2011, Ward 2011; **full text of Pais et al. 2013 read, including its equation images**, and the deadlock-breaking threshold re-derived and simulated. Tags added by that pass: [read: abstract], [read: full text], [derived].
- Corrections found while verifying: Muro et al. 2011 is in *Behavioural Processes*, not a journal of economics; Flack et al. 2006 is DOI 10.1038/nature04326; Pratt 2005 is DOI 10.1093/beheco/ari020; Harcourt 2009 is DOI 10.1016/j.cub.2008.12.051; Couzin 2011 is DOI 10.1126/science.1210280 (not the Seeley 2012 DOI, which is 10.1126/science.1210361).

## Headline

Animal-group work is the best existing source of **explicit, analysable equations for what the strand calls drives**. The pattern is consistent: each individual carries a graded internal variable (a stimulus level, a threshold, a commitment, a fear/startle state, an attraction weight); interactions are *rules that read other individuals' signalled states and update one's own*; group-level results (division of labour, deadlock-breaking, cascades, robustness) are theorems or bifurcations in the induced dynamics. The nearest thing to an "algebra" is the **compartmental commitment model** (uncommitted/committed-A/committed-B with discovery, recruitment, abandonment, cross-inhibition), which is a small set of composable operators on a state vector. Transfer to humans is strongest for *structure* (threshold, cross-inhibition, quorum, policing) and weakest for *parameters*.

---

## A. Social insects

### A1. Response-threshold division of labour: Bonabeau, Theraulaz, Deneubourg 1996; Beshers and Fewell 2001

- Bonabeau, Theraulaz, Deneubourg, "Quantitative study of the fixed threshold model for the regulation of division of labour in insect societies", Proc R Soc B 263, 1565-1569 (1996). DOI 10.1098/rspb.1996.0229 (confirmed). Follow-up: Theraulaz, Bonabeau, Deneubourg 1998, "Response threshold reinforcements and division of labour in insect societies", Proc R Soc B 265, 327-332. DOI 10.1098/rspb.1998.0299 (confirmed in validation; Crossref misspells Deneubourg). Also Bonabeau, Theraulaz, Deneubourg 1998, "Fixed response thresholds and the regulation of division of labor in insect societies", Bull Math Biol 60, 753-807, DOI 10.1006/bulm.1998.0041 (confirmed; Crossref lists only Bonabeau, metadata incomplete).
- Beshers and Fewell, "Models of division of labor in social insects", Annu Rev Entomol 46, 413-440 (2001). DOI 10.1146/annurev.ento.46.1.413 (confirmed; Crossref title garbled by small caps).
- **State variables (drives)**: per task j a stimulus s_j (the task's "need"); per individual i and task j a threshold θ_ij (its disposition, "drive strength" inverted).
- **Rule [standard account]**: an inactive individual starts task j with probability per time step T_θ(s) = s^n / (s^n + θ^n), with **n = 2** in Bonabeau et al. 1996 (so T = 1/2 at s = θ: θ is the half-response stimulus); an active individual quits with probability p per step. The 1996 model is **discrete-time**: s(t+1) = s(t) + δ − α·N_act/N (demand grows by δ, work by the active fraction depletes it); the continuous form ds/dt = δ − α·N_act/N is its mean-field limit. The 1998 reinforcement variant: θ_ij ← θ_ij − ξΔt while i performs j, θ_ij ← θ_ij + φΔt while it does not (bounded within [θ_min, θ_max]), producing specialisation. [standard account; equations not re-read in full text by the validator, but the forms are the canonical ones reproduced across the literature]
- **Derived results [standard account]**: with distinct thresholds, low-threshold individuals take up a task first and others are recruited only as stimulus rises, so work is allocated by threshold without any central assignment; the colony keeps stimulus near homeostasis; with reinforcement, initially identical individuals differentiate into specialists. Beshers and Fewell's review contrasts this with foraging-for-work and other models and notes that few predictions have been tested head-to-head.
- **Empirical tests**: Greene and Gordon 2003, "Cuticular hydrocarbons inform task decisions", Nature 423, 32 (DOI 10.1038/423032a, confirmed): harvester ants' task choice depends on encounter rates with others' cuticular hydrocarbon signatures, supporting a stimulus-by-encounter reading. Jeanson and Weidenmuller-style variability reviews exist but not confirmed here.
- **Transfer to humans**: high for the *form* (propensity function of a perceived need, heterogeneous thresholds); the specialisation-by-reinforcement step resembles skill and role lock-in. Humans also set θ strategically, which insects do not.
- **Operand/operator**: operands are (individual, task) pairs carrying a threshold; stimulus is a group-level operand. Operators: Act (probabilistic, gated by threshold), Reinforce (θ update), Deplete (stimulus update by the active set). Explicit and composable.

### A2. Stigmergy and coordinated building: Theraulaz and Bonabeau 1995; Grasse

- Theraulaz and Bonabeau, "Coordination in distributed building", Science 269, 686-688 (1995). DOI 10.1126/science.269.5224.686 (confirmed).
- **State**: the environment itself is the state (partial structure). **Rule [standard account]**: an individual's action is a function of the local configuration of the structure it perceives; its action changes that configuration, which cues the next action by itself or another. Grasse (1959) coined stigmergy (not verified here).
- **Results**: the paper shows via simulation that lattice-swarm builders following local configuration-to-action tables can produce coherent architectures resembling wasp nests; most rule tables yield incoherent shapes, a few yield coordinated ones. This is a *classification of rule sets by outcome*, the closest thing here to a structure theorem, but it is simulation-based.
- **Transfer**: high for institutions, documents, shared artefacts as the medium through which people coordinate without messaging. Wikipedia-style editing, city planning and ledgers are stigmergic.
- **Operand/operator**: operand = the shared artefact state; operator = a local rewrite rule (pattern -> action). This is a rewriting system, which fits `14-maths-cs-structures` territory.

### A3. Quorum sensing in Temnothorax: Pratt 2005 (with Pratt et al. 2002)

- Pratt, "Quorum sensing by encounter rates in the ant Temnothorax albipennis", Behav Ecol 16, 488-496 (2005). DOI 10.1093/beheco/ari020 (confirmed). Earlier: Pratt, Mallon, Sumpter, Franks 2002, "Quorum sensing, recruitment, and collective decision-making during colony emigration by the ant Leptothorax albipennis", Behav Ecol Sociobiol, DOI 10.1007/s00265-002-0487-x (confirmed).
- **State/drive**: an individual's local count of nest-mates met at a candidate site; a threshold on that count; the output switches from slow tandem-run recruitment to fast transport (carrying).
- **Rule [standard account, from titles and the standard account of the species]**: scouts assess sites independently, recruit with tandem runs, and switch to transport when site encounters exceed a quorum threshold. Pratt 2005's title states that the quorum is sensed by *encounter rate*, not by absolute population.
- **Results**: a quorum threshold converts noisy individual assessments into a sharp collective commitment; varying the threshold trades speed against accuracy (also the point of Marshall 2009 below). Not a theorem in the original. Marshall et al. 2009 (B2) analysed a Temnothorax tandem-run model and found it reaches statistical optimality only with parameters depending on both sites' qualities, which they judge biologically unrealistic; the quorum treatment as a decision mechanism is reviewed in Sumpter and Pratt 2009 (see Missing).
- **Transfer**: high structurally (critical-mass, tipping behaviour, "enough people are doing it"); humans have Granovetter-style thresholds in sociology (other cluster).
- **Operand/operator**: operand = individual with a count; operator = Encounter (increments count) and Switch (threshold crossing changes the signalling mode). A threshold operator on a counter.

### A4. Personality and keystone roles in colonies: Jandt et al.; Modlmeier et al. 2014

- Jandt, Bengston, Pinter-Wollman, Pruitt, Raine, Dornhaus, Sih, "Behavioural syndromes and social insects: personality at multiple levels", Biol Rev, Crossref year 2013 (DOI 10.1111/brv.12042, confirmed). Modlmeier, Keiser, Watters, Sih, Pruitt, "The keystone individual concept: an ecological and evolutionary overview", Anim Behav 89, 53-62 (2014). DOI 10.1016/j.anbehav.2013.12.020 (confirmed).
- **State**: individual behavioural type (boldness, aggressiveness, activity) as a stable trait; colony-level composite behaviour ("collective personality").
- **Results [read: titles only; standard account]**: a keystone individual is one whose presence or absence has a disproportionate effect on group function; the review ties individual types to colony performance and to colony-level personality that is not the mean of individuals.
- **Transfer**: high conceptually (the key-person problem, founder/pivot roles); few equations.
- **Operand/operator**: operand carries a type label that biases the gain on every operator it participates in (a "coefficient", not a new operator).

---

## B. Collective decision-making as drive competition

### B1. Honeybee nest-site selection with cross-inhibition: Seeley et al. 2012; Pais et al. 2013

- Seeley, Visscher, Schlegel, Hogan, Franks, Marshall, "Stop signals provide cross inhibition in collective decision-making by honeybee swarms", Science 335, 108-111 (2012). DOI 10.1126/science.1210361 (confirmed).
- Pais, Hogan, Schlegel, Franks, Leonard, Marshall, "A mechanism for value-sensitive decision-making", PLoS ONE 8(9), e73216 (2013). DOI 10.1371/journal.pone.0073216 (confirmed). Generalisation to N options: arXiv 1611.07575 (not DOI-checked in validation; see Unconfirmed).
- **State (drives)**: fractions of the swarm uncommitted (x_U), committed to site A (x_A), committed to site B (x_B); each site has a quality (value) that sets how strongly its advocates recruit.
- **Equations [read: full text of Pais et al. 2013, Eq. 1, deterministic part]**:
  - dx_A/dt = γ_A x_U − α_A x_A + ρ_A x_A x_U − σ_B x_A x_B
  - dx_B/dt = γ_B x_U − α_B x_B + ρ_B x_B x_U − σ_A x_A x_B
  - x_U = 1 − x_A − x_B.
  - γ discovery, α abandonment, ρ recruitment, σ_i cross-inhibition delivered by bees committed to site i (a "stop signal" that turns a dancer for the rival site back to uncommitted). Value dependence, following Seeley et al. 2012: **γ_i = ρ_i = v_i, α_i = 1/v_i**; σ is value-independent (σ_A = σ_B = σ). Pais et al. add multiplicative noise k·sqrt(x_U² + x_A² + x_U²x_A²)·dW_A (similarly for B) to the value-dependent rates; σ carries no noise. A decision is taken when an accumulator reaches a quorum threshold.
- **Derived results [read: full text]**: for **equal values** (v_A = v_B = v) the model "exhibits a pitchfork bifurcation as a function of increasing cross-inhibition rate σ and value v": below a critical σ* there is a single stable symmetric attractor (deadlock); above it that point becomes a saddle and two attractors, one per option, emerge, so one site is chosen at random. The threshold (Pais Eq. 4, attributed to Seeley et al. 2012, where it was first calculated) is **σ* = 4v³ / (v² − 1)²**, which falls with v: equal *high*-value options are broken, equal *low*-value options can deadlock. For **unequal values** the paper describes a saddle-node bifurcation in σ instead. Value-sensitivity: the minimum value difference that the system reliably discriminates satisfies **Δv / v̄ = K** (Pais Eq. 5), "similar to Weber's law", with the coefficient K set by σ (lower σ, lower K).
- **[derived: checked by the validator]** At the symmetric equilibrium x_A = x_B = x, U = 1 − 2x, the eigenvalue for an antisymmetric perturbation (δx_A = −δx_B) is λ = ρU − α = vU − 1/v (the σ terms cancel). λ = 0 gives U = 1/v², x = (v² − 1)/(2v²); substituting into the equilibrium condition vU − x/v + vxU − σx² = 0 leaves σx² = vU = 1/v, so σ* = 1/(v x²) = 4v³/(v² − 1)², matching Eq. 4. Two consequences not stated in the survey: σ* exists only for **v > 1** (for v ≤ 1, λ < 0 for every σ, so equal options of low value deadlock however strong the stop signal); and σ* → 4/v for large v. A forward-Euler simulation at v = 2 (σ* = 3.56) gave a symmetric split (0.41, 0.41) at σ = 0.9σ* and a broken one (0.26, 0.49) at 1.1σ*.
- **Empirical test [read: abstract]**: Seeley et al. 2012 show that nest-site scouts send stop signals (head-butts) to waggle-dancing scouts, targeting those reporting sites other than their own, which is the empirical correlate of σ; their abstract states that "an analytic model shows that cross inhibition ... increases the reliability of swarm decision-making by solving the problem of deadlock over equal sites", so the deadlock-breaking result is originally theirs.
- **Transfer to humans**: very high structurally. Cross-inhibition is the "mutual blocking" of rival camps; the equation set is a compact template for any two-faction commitment process. Parameters for humans are unknown.
- **Operand/operator**: operands = population fractions (a commitment vector on a simplex); operators = Discover, Recruit, Abandon, Inhibit. Each operator is a flow on the simplex with a rate coefficient: close to an algebra of flows, with theorems about fixed points. **This is the most algebra-ready object in the cluster.**

### B2. Optimality and the neural analogy: Marshall et al. 2009

- Marshall, Bogacz, Dornhaus, Planque, Kovacs, Franks, "On optimal decision-making in brains and social insect colonies", J R Soc Interface 6, 1065-1074 (2009). DOI 10.1098/rsif.2008.0511 (confirmed).
- **[read: abstract, plus a summary of the full text]**: in primate brains and insect colonies alike, separate groups gather evidence for options and a choice is made when one reaches a threshold; moving the threshold trades speed for accuracy. The authors take the analysis used for the Usher-McClelland leaky competing accumulator (optimal, i.e. reducing to the drift-diffusion/SPRT procedure, when decay equals inhibition and both are large) and apply it to three colony models: a Temnothorax tandem-running model (after Pratt et al. 2002), and honeybee **indirect-switching** and **direct-switching** models (after Britton et al. 2002). Only the **direct-switching** model, in which committed scouts are recruited straight across to the rival site, approximates the statistically optimal procedure in a biologically plausible way, and only with **zero spontaneous abandonment**; it is then asymptotically optimal (once all scouts are committed the dynamics reduce to one-dimensional diffusion). The indirect-switching model cannot be reduced to one dimension and is not optimal; the Temnothorax model needs parameters depending on both sites' qualities.
- **Correction (validation)**: the earlier text said the result was "the equivalence of cross-inhibitory competition to a sequential-sampling decision rule". The 2009 mechanism is **direct switching by recruitment**, not stop-signal cross-inhibition (described in 2012); the paper only suggests the stop signal might play a similar role, and notes experiments suggest bees may not switch directly. Seeley 2012's cross-inhibition is a *different* mechanism (inhibited bees return to uncommitted, which is closer to the indirect route), so B1 and B2 should not be cited as one result.
- **Why it matters**: it is a *theorem-type* result: an optimality claim, that one colony mechanism reduces under stated parameters to a sequential-sampling decision rule. It is the bridge between an individual-level neural drive model and a group-level one, which is the precise move the strand wants (individual drive algebra and group drive algebra obeying the same laws). The optimality is "could, under conditions", not "do".
- **Transfer**: the group-as-neuron analogy gives a systematic way to port individual-level motivation models (cluster 16) up to groups.

### B3. Shared decision-making in baboons: Strandburg-Peshkin et al. 2015

- Strandburg-Peshkin, Farine, Couzin, Crofoot, "Shared decision-making drives collective movement in wild baboons", Science 348, 1358-1361 (2015). DOI 10.1126/science.aaa5099 (confirmed).
- **State**: each baboon's heading and position (GPS collars on a troop); a preference direction expressed by initiating movement.
- **Result [read: abstract]**: rather than preferentially following dominant individuals, baboons are more likely to follow when *multiple initiators agree*; when directions conflict they choose one direction when the angle between them is large and compromise when it is not. The authors call this shared decision-making, consistent with models of collective motion. (The earlier phrasing "any individual can initiate" is not in the abstract and is softened: the finding is that dominance does not predict who is followed.) The compromise-or-choose split is the empirical counterpart of the bifurcation analysed by Leonard et al. 2012 and Sridhar et al. 2021 (see Missing).
- **Transfer**: consistent with human consensus-by-averaging-until-conflict behaviours (compromise at small disagreement, winner-takes-all at large). That the *same* shape (average then bifurcate) appears in fish models (B4) suggests a recurring motif: smooth averaging below a disagreement threshold, symmetry-breaking above it.
- **Operand/operator**: operand = individual with a preference vector; operator = Follow(weights over neighbours/initiators); the compromise-or-choose behaviour is a non-linear aggregation operator, not a mean.

### B4. Uninformed individuals and democracy: Couzin et al. 2011

- Couzin, Ioannou, Demirel, Gross, Torney, Hartnett, Conradt, Levin, Leonard, "Uninformed individuals promote democratic consensus in animal groups", Science 334, 1578-1580 (2011). DOI 10.1126/science.1210280 (confirmed).
- **State**: a heading with an *informed* subpopulation holding preferences (two opposed groups, differing in size and strength) and an *uninformed* subpopulation with none.
- **Result [read: abstract]**: using theory and experiment, "for a wide range of conditions, a strongly opinionated minority can dictate group choice, but the presence of uninformed individuals spontaneously inhibits this process, returning control to the numerical majority." Experiments on golden shiners. (Press summary, not checked against full text: if the number of uninformed individuals becomes very large, noise erodes the majority's control and coherence.)
- **Relevance**: uninformed individuals are not noise: they behave as the *uncommitted pool* x_U in B1 and damp the influence of committed minorities. It is a worked example of how a non-driven operand changes the stable outcome of the whole system. Directly addresses the claim (for humans and animals) that groups with uninformed members are vulnerable to manipulation.
- **Transfer to humans**: tested in humans in later work (not verified here); the structural claim (swing-voters or uncommitted nodes suppress extreme-minority control) is plausible but human parameters will differ.
- **Operand/operator**: operand types: Informed(pref, strength) and Uninformed; operator: Align(weights). The type of operand changes the group's fixed point.

---

## C. Fear, vigilance, cascades

### C1. Fear contagion through schools: Rosenthal et al. 2015

- Rosenthal, Twomey, Hartnett, Wu, Couzin, "Revealing the hidden networks of interaction in mobile animal groups allows prediction of complex behavioral contagion", PNAS 112, 4690-4695 (2015). DOI 10.1073/pnas.1420068112 (confirmed, authors from Crossref).
- **State**: each fish's *startle* state (a binary or graded alarm response) and, crucially, what it can *see*: a reconstruction of each fish's field of view gives a directed "visual network".
- **Result [read: abstract]**: in schools of ~150 golden shiners the authors track positions and postures, compute each fish's visual field, and fit the mapping from socially generated sensory input to startle response. Individuals use simple, robust measures of neighbours' behavioural change; the resulting networks are weighted, directed and heterogeneous; contagion is "complex, fractional" (not simple one-contact transmission); individuals with **relatively few but strongly connected neighbours are both the most influential and the most susceptible**; and cascades can be predicted at the moment of initiation, before they occur. The "potential control" reading in (c) below is the survey's extrapolation, not a result of the paper.
- **Why it is the key result for fear**: it shows (a) fear is transmitted by a rule keyed to who is perceived to be fleeing, (b) the transmission graph is not fixed but a function of geometry and time (so any algebra of fear must index the graph by state), (c) cascades are *predictable from the network and initial conditions*, i.e. prediction and potential control (move the fish, change the cascade). It is among the few animal-group results with a demonstrated prediction of a drive-driven contagion.
- **Transfer**: structurally high (panic, bank runs, rumours). The human analogue requires an attention or visibility graph, which social-media platforms partly make explicit (unconfirmed here).
- **Operand/operator**: operand = individual with a fear level; operator = Startle-transmit over a state-dependent directed graph; the graph itself is an operand-derived object (a functor of positions).

### C2. Collective vigilance: Pulliam 1973; Ward et al. 2011

- Pulliam, "On the advantages of flocking", J Theor Biol 38, 419-422 (1973). DOI 10.1016/0022-5193(73)90184-7 (confirmed). Ward, Herbert-Read, Sumpter, Krause, "Fast and accurate decisions through collective vigilance in fish shoals", PNAS 108, 2312-2315 (2011). DOI 10.1073/pnas.1007102108 (confirmed).
- **State/rule [standard account]**: Pulliam's model: with n group members each scanning with probability p, the probability that no one scans at an instant falls with n, so each can lower its own vigilance as group size grows while overall detection stays high (the "many eyes" effect). Ward et al. [read: abstract]: speed and accuracy both rise with group size under predation threat; repeated testing found no evidence of especially able individuals, and the authors attribute the gain to self-organised division of vigilance plus social information transfer. (Pulliam's actual model works with scanning intervals and detection time; the "probability no one scans = (1 − p)^n" form is a simplification.)
- **Result**: a quantitative trade-off (vigilance versus feeding) as a function of group size. It is an optimality argument, not a dynamical system.
- **Transfer**: group size and free-riding on vigilance, the "diffusion of responsibility" in bystander research (other cluster).
- **Operand/operator**: operand = individual with a vigilance allocation; operator = Scan (probabilistic); group detector = the logical OR of scans, so group detection is a composition rule with a known probability law.

### C3. Social learning and information cascades

- Giraldeau, Valone, Templeton, "Potential disadvantages of using socially acquired information", Phil Trans R Soc B 357, 1559-1566 (2002). DOI 10.1098/rstb.2002.1065 (confirmed as title and DOI; not read).
- **[standard account]**: copying others is advantageous when private information is costly but, because copied information is not independent, a population can lock into a maladaptive behaviour (information cascade). This is the animal version of the Bikhchandani-Hirshleifer-Welch cascade model (economics cluster).
- **Transfer**: high, same mathematics; the animal literature supplies field cases but not human parameters.
- **Operand/operator**: operand carries a private signal and a public history; operator = Imitate-vs-Use-private, depending on the balance of evidence.

---

## D. Leadership, personality and status

### D1. Boldness and leaders: Harcourt et al. 2009; Jolles et al. 2017

- Harcourt, Ang, Sweetman, Johnstone, Manica, "Social feedback and the emergence of leaders and followers", Curr Biol 19, 248-252 (2009). DOI 10.1016/j.cub.2008.12.051 (confirmed).
- Jolles, Boogert, Sridhar, Couzin, Manica, "Consistent individual differences drive collective behavior and group functioning of schooling fish", Curr Biol 27, 2862-2868 (2017). DOI 10.1016/j.cub.2017.08.004 (confirmed).
- **State**: individual boldness (a stable trait) *and* a feedback variable: how being ahead or behind changes an individual's later behaviour. The Harcourt title names the mechanism: leaders and followers *emerge* from social feedback, i.e. roles are not just trait readouts.
- **Result [read: abstracts]**: Harcourt et al.: in *pairs of sticklebacks*, boldness measured as the propensity to leave cover to look for food; a **Markov chain model** of joint behaviour inferred the individual rules. Each fish was more likely to leave cover if the partner was out and to return if it had returned; bolder fish showed more initiative and less responsiveness, shyer fish followed more faithfully and, as followers, *elicited* stronger leadership in bold partners: leadership "reinforced by positive social feedback". Jolles et al. (stickleback shoals, high-resolution tracking): **sociability** (not boldness) was negatively linked to swim speed and predicted spatial position and leadership; sociability together with exploratory tendency ("boldness" assay) explained foraging performance; the effects emerged from a generic self-organising model of individuals differing in **speed and goal-orientedness**. Correction: the earlier text attributed leadership in both papers to boldness; in Jolles 2017 it is sociability/speed.
- **Transfer**: plausible for human groups (bold/shy and the self-reinforcing nature of early dominance), but without the exact equations I did not read, I cannot say how directly.
- **Operand/operator**: operand carries a trait (boldness) and a role (leader/follower) that is itself updated by the Follow operator (self-reinforcing). Two-layer state: trait fixed, role dynamic.

### D2. Status and the brain: Fernald 2012

- Fernald, "Social control of the brain", Annu Rev Neurosci 35, 133-151 (2012). DOI 10.1146/annurev-neuro-062111-150520 (confirmed).
- **[standard account of the cichlid *Astatotilapia burtoni* work, not read]**: males are either territorial/dominant or non-territorial; change of social status (by social opportunity) changes neuroendocrine physiology within the hour to days (e.g. GnRH-neuron size, steroid levels), i.e. status is a **cause of drive state**, not just an outcome.
- **Why it matters**: gives the clearest biological evidence for a *status -> drive* coupling: the same individual with a different social position has different drive parameters. In an algebra, a role operand modifies the individual's drive gains.
- **Transfer**: human status-physiology literature exists (cortisol and rank; not verified here).

### D3. Policing and robustness: Flack, Girvan, de Waal, Krakauer 2006 (key)

- "Policing stabilizes construction of social niches in primates", Nature 439, 426-429 (2006). DOI 10.1038/nature04326 (confirmed; abstract read via search summary).
- **State**: the networks of grooming, play, proximity and contact-sitting among a captive group (84 pigtailed macaques per Scientific American's coverage); one role variable: *policer* (individuals who intervene impartially in conflicts).
- **Experiment [read: abstract]**: knockout experiments, temporarily removing the small subset who did most policing (press: the three highest-ranking males). Caveat added in validation: the knocked-out individuals were also the most powerful, so the manipulation removes rank as well as policing; how the paper separates the two was not checked in full text. Result: the group's networks became smaller, less diverse and less integrated: reduced mean degree, increased clustering, reduced reach, increased assortativity. Members interacted mostly with familiar partners.
- **Interpretation**: conflict management (policing) is a *robustness mechanism*: it stabilises each individual's ability to build a wide social niche. The authors frame the niche as an individual's local connections in multiple overlapping networks.
- **Derived result**: an empirical knockout *theorem-like* statement: a single role (cheap, rare in frequency) is necessary for a network property. Not a mathematical theorem, but a causal claim established by intervention, which is what "control" means for the strand.
- **Transfer**: high structurally (the function of impartial third-party enforcement). The role of police, mediators, referees, a trusted third party.
- **Operand/operator**: operand = individual with a role label; operator = Intervene(conflict) -> restores baseline. The role is "present or absent" in the group, and the property is a function of that set; an *invariant that is preserved by a specific operator* is the algebraic form of "policing stabilises".

---

## E. Hunting, movement, grouping

### E1. Wolf-pack hunting from simple rules: Muro et al. 2011

- Muro, Escobedo, Spector, Coppinger, "Wolf-pack (Canis lupus) hunting strategies emerge from simple rules in computational simulations", Behav Processes 88, 192-197 (2011). DOI 10.1016/j.beproc.2011.09.006 (confirmed as title; Crossref year 2011). A companion item in J Vet Behav 6, 94 (2011), DOI 10.1016/j.jveb.2010.08.017, is titled per Crossref "Wolf-pack hunting strategy: an emergent collective behavior described by a classical robotic model" (corrected in validation: the earlier title, "...a class of mathematical models", was wrong); single page, apparently a conference abstract.
- **Rules [read: abstract]**: (1) move towards the prey until a minimum safe distance is reached; (2) when close enough, move away from the other wolves that are also close to the safe distance. Agents are autonomous, interchangeable and indistinguishable and need only others' positions; tracking, pursuit and encirclement until the prey stops emerge in simulation, with no communication or hierarchy. Simulation only; no field fit.
- **Transfer**: mostly illustrative: cooperative-looking outcome from two selfish drives (approach, avoid crowding). Maps to attraction/repulsion (Couzin 2002 in 09).
- **Operand/operator**: operand = agent with position; operators = Approach(target), Disperse(others); the outcome is composition of two vector fields.

### E2. Fission-fusion: Aureli et al. 2008

- Aureli et al., "Fission-fusion dynamics: new research frameworks", Curr Anthropol 49, 627-654 (2008). DOI 10.1086/586708 (confirmed as title "Fission-Fusion Dynamics"; author list from memory, only the DOI and title confirmed).
- **[standard account]**: fission-fusion dynamics are variation over time in the spatial cohesion and individual membership of groups; species sit on a continuum; the paper proposes a framework for classifying and comparing them (the "fission-fusion dynamics" being a property of the society's response to costs of grouping).
- **Why it matters here**: it provides an operation pair (Split, Merge) on a group-level operand, with the state (who is in each subgroup) changing over time, and argues that the form of the dynamics depends on the species' ecology. It is the animal precursor to the dynamic-group-membership problem human society also has (households, teams).
- **Operand/operator**: operand = partition of the individuals; operators = Fission, Fusion. A partition lattice is the natural formalism (see cluster 14).

### E3. Cooperative breeding and helping: Hamilton 1964; Clutton-Brock 2002

- Hamilton, "The genetical evolution of social behaviour. I", J Theor Biol 7, 1-16 (1964). DOI 10.1016/0022-5193(64)90038-4 (confirmed). Clutton-Brock, "Breeding together: kin selection and mutualism in cooperative vertebrates", Science 296, 69-72 (2002). DOI 10.1126/science.296.5565.69 (confirmed).
- **Rule [standard account]**: Hamilton's rule rb > c: help is selected for when the relatedness-weighted benefit to the recipient exceeds the cost. Clutton-Brock's review argues that in cooperative vertebrates helping is explained by both kin selection and mutualistic benefits (group augmentation, direct fitness benefits), not kin selection alone.
- **Result**: an inequality, the nearest thing to a theorem about *when a helping drive is favoured*. Hamilton's rule is an exact result under its assumptions; its general validity is debated in the literature (not examined here).
- **Operand/operator**: operand = individual with relatedness to others; operator = Help(i->j), applied iff rb > c. A guard condition on an operator.

---

## Rule motifs that recur across species

| Motif | Where it appears here | Also in `09` | In humans (status in this file) |
|---|---|---|---|
| **Threshold response** (propensity rises with stimulus; heterogeneous thresholds) | A1 task allocation; A3 quorum; B3 compromise-to-choose (an angle threshold) | Centola-Macy | Granovetter-type thresholds in sociology (other cluster; not verified here) |
| **Cross-inhibition / mutual blocking** | B1 stop signals (to uncommitted); B2 is a related but distinct mechanism, direct switching by recruitment | no | Structural analogy only; no human fit found in this pass |
| **Quorum / critical mass** | A3; B1 | Seeley | Plausible, tested elsewhere (not verified) |
| **Alignment/averaging with a disagreement threshold** | B3; B4 | Vicsek, Couzin | Not verified here |
| **Uncommitted pool damping minorities** | B4 | Couzin 2005 | Not verified here |
| **Policing / third-party intervention** | D3 | Hinde, primates | Widely argued; no node-knockout equivalent found here |
| **Contagion over a state-dependent perception graph** | C1 | SIR | Human data on social media exist elsewhere |
| **Role/trait modifies gains; roles reinforced by feedback** | A4; D1; D2 | no | Plausible; unverified |
| **Guarded operator (act iff inequality)** | E3 Hamilton; A1 threshold; A3 quorum | Hawk-Dove | Common in economics |

"Has been shown in human groups" is the weakest column: this pass did not find or verify human tests for each motif. Human evidence belongs to other clusters (05, 06, 07, 10) and should be cross-referenced there, not asserted here.

## What exists versus what does not

**Exists.**
- Explicit state variables and equations for task allocation (A1) and two-option commitment with cross-inhibition (B1), with a verified pitchfork at σ* = 4v³/(v² − 1)² for equal options, and a separate optimality link to sequential-sampling theory for a direct-switching variant (B2). The equation set in B1 is small enough to be treated as an algebra of flows.
- A predictive, empirically tested model of fear contagion over a perception graph (C1).
- A causal intervention result on a role (D3).
- Inequalities with a long track record (E3 Hamilton; C2 Pulliam).
- Strong qualitative evidence that status changes drive-state physiology (D2).

**Does not exist, as far as this pass found.**
- No unified algebra in which curiosity, fear and desire (the strand's named drives) appear as primitives. Animal models use *behavioural* variables (commit, startle, approach, avoid), not a drive taxonomy.
- **Corrected in validation**: the earlier claim that curiosity and desire are "essentially absent" overstated it. They are present as *exploration* and *appetite*, just not under those names: (i) honeybee **scouts are consistent novelty-seekers** across food and nest-site contexts, with brain gene-expression differences in catecholamine, glutamate and GABA signalling; octopamine and glutamate raise scouting and a dopamine antagonist lowers it, and the authors draw the parallel to human novelty-seeking (Liang et al. 2012, Science 335, 1225-1228, DOI 10.1126/science.1213962, confirmed, [read: abstract]); (ii) the scout/recruit split and the discovery rate γ in B1 are an explicit exploration term, separate from the exploitation (recruitment) term ρ; (iii) Jolles 2017 measures an individual "exploratory tendency" that predicts group foraging; (iv) Harcourt 2009's boldness *is* an appetitive measure (leaving cover to look for food), and the response-threshold stimulus s in A1 is a need-like appetitive variable. What is genuinely absent is a model with curiosity and desire as *named, interacting state variables* with their own dynamics.
- No composition laws across the different models: A1, B1, C1 each use their own state spaces; none is expressed as an operator on a common one. (This stands. The nearest partial unification is Marshall et al. 2009 / Pais et al. 2013 placing colony and neural accumulator models in one framework, and Sridhar et al. 2021 treating individual and collective spatial decisions with one bifurcation geometry; neither is a common state space for different drives.)
- No game-theoretic or control-theoretic synthesis that says what interventions drive a group to a target state (apart from D3's removal experiment and C1's cascade prediction).
- No human equivalents of the animal parameters; animal results are structural templates, not quantitative.
- Theorems are mostly local (fixed points, thresholds, inequalities) and rest on mean-field or simulation assumptions; none is a theorem of an algebra.

**Practical implication for the strand.** The best-leveraged animal imports are: (1) the compartmental commitment model as the template for group-level drive competition; (2) the response-threshold form as the template for how an individual drive converts a perceived stimulus to action; (3) the state-dependent perception graph for transmission of fear; (4) role operators with an invariant they preserve (policing). The missing piece, a common state space, is exactly what cluster 15-19 might supply.

## Unconfirmed

- Grasse 1959 (stigmergy) and Bonabeau et al. 1999 "Swarm Intelligence" book: cited from general knowledge, no DOI check.
- (Resolved in validation and removed from this list: Theraulaz et al. 1998 DOI; the B1 pitchfork; the B3 compromise-or-choose result; Harcourt and Jolles mechanisms; author lists, now from Crossref.)
- The details of the cichlid physiology in D2 (timescales, GnRH-neuron size): standard account, Fernald 2012 not read.
- Pratt 2005's mechanism beyond its title (no abstract retrieved in validation): the encounter-rate claim rests on the title.
- The N-option generalisation of B1 (arXiv 1611.07575): identifier not checked.
- Couzin 2011's "too many uninformed individuals" effect: press summary only.
- Flack 2006's separation of policing from rank in the knockout: not read in full text.
- Human tests of the motifs (Dyer et al. 2009 on human leadership and consensus; Helbing et al. 2000 on panic; Granovetter 1978 thresholds; Moussaid et al. on human crowds): known to exist from memory; DOIs not checked in this pass, so not cited as findings.
- Seeley's *Honeybee Democracy* (Princeton UP 2010) and Camazine et al. *Self-Organization in Biological Systems* (2001): books, not checked.

## Missing important work (added in validation; DOIs confirmed at Crossref)

- **Conradt and Roper 2003**, "Group decision-making in animals", Nature 421, 155-158, DOI 10.1038/nature01294. The shared-versus-unshared (despotic) consensus-cost model; the baseline B3 and B4 argue against.
- **Sumpter and Pratt 2009**, "Quorum responses and consensus decision making", Phil Trans R Soc B 364, 743-753, DOI 10.1098/rstb.2008.0204. The general quorum-response function (a steep threshold function of the number already committed) across taxa; the formal statement of A3's operator.
- **Leonard, Shen, Nabet, Scardovi, Couzin, Levin 2012**, "Decision versus compromise for animal groups in motion", PNAS 109, 227-232, DOI 10.1073/pnas.1118318108. Bifurcation analysis of the compromise-or-choose transition in angle between preferred directions; the mathematics behind B3 and the model side of B4.
- **Sridhar, Li, Gorbonos, Nagy, Schell, Sorochkin, Gov, Couzin 2021**, "The geometry of decision-making in individuals and collectives", PNAS 118, e2102157118, DOI 10.1073/pnas.2102157118. Repeated bifurcations as options are approached, the same geometry in individual brains and in groups; the strongest existing case for "individual and group obey the same law".
- **Liang, Nguyen, Mattila, Rodriguez-Zas, Seeley, Robinson 2012**, "Molecular determinants of scouting behavior in honey bees", Science 335, 1225-1228, DOI 10.1126/science.1213962. Novelty-seeking as a stable individual trait in scouts, with a pharmacological handle; the curiosity analogue (see corrected closing claims).
- **Prabhakar, Dektar, Gordon 2012**, "The regulation of ant colony foraging activity without spatial information", PLoS Comput Biol 8, e1002670, DOI 10.1371/journal.pcbi.1002670. Harvester-ant foraging rate regulated by return-encounter rate, analysed as a feedback controller (analogous to TCP); an explicit appetite-regulation equation at colony level.

## Validation log (2026-10-29)

- Bonabeau, Theraulaz, Deneubourg 1996: ✓ (DOI, venue, pages); ✎ noted n = 2 and that the stimulus update is discrete-time.
- Bonabeau, Theraulaz, Deneubourg 1998 (Bull Math Biol): ✓ (Crossref author list incomplete).
- Theraulaz, Bonabeau, Deneubourg 1998 (Proc R Soc B): ✎ moved from Unconfirmed to confirmed, DOI 10.1098/rspb.1998.0299; title is "...reinforcements..."; reinforcement rule written out.
- Beshers and Fewell 2001: ✓
- Greene and Gordon 2003: ✓
- Theraulaz and Bonabeau 1995: ✓
- Pratt 2005: ✓ (existence); ? content beyond title.
- Pratt, Mallon, Sumpter, Franks 2002: ✓ (BES 52, 117-127).
- Jandt et al. 2013/2014: ✓ (Biol Rev 89, 48-67; online 2013).
- Modlmeier et al. 2014: ✓
- Seeley et al. 2012: ✓; ✎ the deadlock-breaking analysis is originally theirs (abstract), not only Pais's.
- Pais et al. 2013: ✎ corrected: equations read from full text (σ indexed by the inhibiting site, γ = ρ = v, α = 1/v, noise term); **pitchfork confirmed** for equal values, saddle-node for unequal; σ* = 4v³/(v² − 1)² re-derived and simulated; Weber form Δv/v̄ = K added; new consequence that σ* exists only for v > 1.
- Marshall et al. 2009: ✎ corrected: the optimal mechanism is direct switching with zero abandonment, not cross-inhibition; indirect switching is not optimal.
- Strandburg-Peshkin et al. 2015: ✓ (abstract confirms majority-of-initiators over dominance, and compromise at small angles / choice at large); ✎ softened "any individual can initiate".
- Couzin et al. 2011: ✓ (abstract confirms majority restoration); ✎ author order (Levin before Leonard).
- Rosenthal et al. 2015: ✓; ✎ author list added, "few but strongly connected neighbours" result added, control reading flagged as extrapolation.
- Pulliam 1973: ✓; ✎ noted the (1 − p)^n form is a simplification.
- Ward et al. 2011: ✓; ✎ authors and mechanism (division of vigilance, no elite individuals).
- Giraldeau, Valone, Templeton 2002: ✓ (not read).
- Harcourt et al. 2009: ✎ corrected: pairs of sticklebacks, Markov chain model, boldness as leaving cover for food; authors added.
- Jolles et al. 2017: ✎ corrected: sticklebacks; sociability and speed (not boldness) predict leadership; authors and pages added.
- Fernald 2012: ✓ (existence); ? cichlid detail not read.
- Flack et al. 2006: ✓ (abstract confirms knockout and network measures); ✎ rank-versus-policing confound flagged.
- Muro et al. 2011: ✓; ✎ rule 2 restated from abstract.
- Muro et al. J Vet Behav 2011: ✎ title corrected ("...classical robotic model").
- Aureli et al. 2008: ✓ (author list now from Crossref, 19 authors).
- Hamilton 1964: ✓
- Clutton-Brock 2002: ✓
- Grasse 1959, Bonabeau et al. 1999, Seeley 2010, Camazine et al. 2001, human-test papers: ? unchanged (books or not looked up).
- arXiv 1611.07575: ? not checked.
- Fabrications found: none (✗ 0).
- Closing claims: ✎ "curiosity and desire essentially absent" corrected (scout novelty-seeking, exploration term γ, exploratory tendency, appetitive boldness); "no common state space" stands.

**Verdict.** The bibliography is reliable: every DOI resolves to the paper claimed and nothing was fabricated. The weak points were in the mechanisms, where the survey worked from summaries: the B1 pitchfork, flagged as a guess, turns out to be correct and now has an exact threshold, but Marshall 2009 was conflated with cross-inhibition and the fish-leadership papers were misattributed to boldness. Treat [read: abstract] statements as sound and [standard account] equations, apart from B1, as still unchecked against full text.
