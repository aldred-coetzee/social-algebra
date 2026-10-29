# Prior work, cluster 25: drives at the scale of cultures, and the evolution of norms

Date: 2026-10-29. Strand: social-algebra. Scope: drives (fear, status, belonging, desire for security) at the scale of whole cultures and populations, and how they shape and are shaped by norms. Cross-references: 08 (history, cliodynamics), 09 (biology: replicator equation, Price equation, Hawk-Dove), 04 (institutions, Ostrom as logic), 17 (terror management, if covered there), 18 (collective emotion).

## Summary

Verification status. Existence, authors, venue and year were confirmed for each entry marked "confirmed" via the Crossref API (api.crossref.org) or a fetched page. Equations are the standard textbook forms, tagged **[standard account]** (stated from general knowledge, not re-derived from full text) or **[from abstract]**. No primary full text was read for any entry (one attempted PDF fetch failed: certificate error; another returned binary). Treat every formula as needing a source check before it enters a model. Items not confirmed are in "Unconfirmed".

**Validation pass (2026-10-29)**: every DOI re-resolved via Crossref; the Roos et al. 2015 author PDF and two follow-ups (De, Nau & Gelfand 2017; De, Nau, Pan & Gelfand 2018) were **read in full text** and are tagged **[read]**; other claims checked against abstracts or secondary sources and tagged accordingly. The main correction: the closing claim that threat, conformism and stability have never been composed is **partly false** (see A2, Candidate law 3, and the validation log).

What this cluster offers the drive algebra:

1. **One real fear-to-structure law, with an evolutionary model behind it**: threat raises norm strength (tight/loose; Gelfand, Roos). It is the nearest thing in the literature to "a drive (fear) at population scale determines a structural parameter (norm tightness)". The empirical base is a 33-nation correlation (since extended to US states, 68 countries and 86 non-industrial societies); the model is an agent-based evolutionary simulation on a lattice whose result is driven by a concave fitness function (see A2). Both are thinner than the citation count suggests.
2. **The only genuine theorems**: Young / Kandori-Mailath-Rob stochastic stability (which convention a noisy population settles on), Henrich-Boyd conformist transmission (equations for how a behaviour spreads and when punishment is stable), and replicator/ESS results already covered in 09. These are theorems about *conventions and transmission*, not about drives. Drives enter only as payoffs or error rates.
3. **Descriptive theory with no calculus**: Inglehart (security -> values), Reddy/Rosenwein/Stearns (cultures permit different emotions), Boehm (egalitarian group drive), honour cultures, pathogen stress. Each names a causal arrow from an environmental or institutional condition to a distribution of motives. None is stated so that two such arrows can be composed.
4. **Cross-cultural findings are the weakest evidence in the strand.** Small numbers of countries, self-report scales, confounded predictors (climate, history, wealth, institutions, colonial borders). Be blunt about this when turning any of them into an axiom: treat each as a hypothesis with a settable coefficient, not a law.

Entries: 14 main sections. After validation, 4 items remain unconfirmed (see Unconfirmed); the 5 originally listed there were all confirmed.

---

## A. Threat, tightness and the fear-to-structure law

### A1. Gelfand et al. 2011, "Differences Between Tight and Loose Cultures: A 33-Nation Study"

- Citation: M. J. Gelfand and 44 co-authors (45 authors in Crossref), Science 332(6033), 1100-1104, 2011. DOI 10.1126/science.1197754 (confirmed, Crossref). Sample: 33 nations; the respondent count is "almost 7,000" in press coverage; the commonly cited N = 6,823 was not verified at source.
- **Drive(s)**: fear of collective threat (conflict, disaster, disease, scarcity, density) driving a collective demand for order; the individual-level counterpart is need for structure / intolerance of deviance.
- **Law**: **[from abstract and standard account]** a culture's "tightness" (strength of norms, low tolerance of deviance) is higher where ecological and historical threat is higher: population density, resource scarcity, history of territorial conflict, disasters and disease. Tightness was measured by a questionnaire (strength of norms, punishment of deviance, situational constraint) across 33 nations. Tight cultures show more autocracy and stricter law enforcement [standard account; correlate list not read; "synchrony" was in an earlier draft of this entry and is from Gelfand's later work, not verified as a 2011 finding, so removed]. The abstract frames tightness as part of a *multilevel system* linking ecological and historical threat, societal institutions, everyday situational strength and individual psychology [from abstract]; the "self-reinforcing loop" reading is this note's, not a stated model.
- **Theorems**: none. It is a cross-sectional correlational study.
- **Evidence and robustness**: 33 countries, one questionnaire, country as the unit. Concerns, stated as standard objections and not from a read critique: ecological fallacy (national mean vs individual), confounding by wealth and state capacity, survey-equivalence across languages, and small-n regression with many predictors. Later work has extended coverage, all confirmed in Crossref (titles and venues, not read): Harrington & Gelfand 2014, "Tightness-looseness across the 50 United States", PNAS 111(22), 7990-7995, DOI 10.1073/pnas.1317937111; Uz 2015, "The Index of Cultural Tightness and Looseness Among 68 Countries", J. Cross-Cultural Psychology 46(3), 319-335, DOI 10.1177/0022022114563611; Jackson, Gelfand & Ember 2020, "A global analysis of cultural tightness in non-industrial societies", Proc. R. Soc. B 287, DOI 10.1098/rspb.2020.1036 (86 societies; per HRAF hypothesis pages, food scarcity and pathogens predict tightness, natural disasters do not — so the threat bundle is not uniform). The direction (threat -> tight) is plausible and recurs in other literatures (e.g. cliodynamic work in 08); the *magnitude* and *causal direction* are not established.
- **Operand/operator translation**: operand = a group with a scalar or small vector state `tightness` and a threat input `T`. Operators: `threaten(T)` (raises threat), `relax(T)`. Law: `tightness' = f(tightness, T)`, with f monotone in T. Individual drive "fear" aggregates to group state; the group state in turn sets the *punishment operator's* strength (see A2).

### A2. Roos, Gelfand, Nau & Lun 2015, "Societal threat and cultural variation in the strength of social norms: An evolutionary basis"

- Citation: P. Roos, M. Gelfand, D. Nau, J. Lun, Organizational Behavior and Human Decision Processes 129, 14-23 (2015). DOI 10.1016/j.obhdp.2015.01.003 (confirmed, Crossref; the author PDF's running head says volume 127, Crossref says 129 — trust Crossref). **Full text read** (author copy, cs.umd.edu/~nau/papers/roos2015societal.pdf).
- **Drive(s)**: fear of external threat as an exogenous environmental parameter; the evolving trait is willingness to adhere to and punish deviation from norms.
- **Model [read]**: an agent-based simulation, not an analytic model.
  - Population on a 50x50 lattice, periodic boundary, von Neumann neighbourhood (4 neighbours). Each step: birth of a random-strategy agent in an empty site; base payoff 30; each agent plays 4 games; punishment phase; fitness; reproduction into an empty neighbouring site with probability = fitness; mutation (rate μ = 0.1) to a random strategy; death (rate d = 0.1).
  - **Threat is a payoff shift**: `p = base_pay - s + x`, with `s` the threat level and `x` the game-plus-punishment payoff.
  - **Fitness is concave**: `f(p) = 1 - exp(-0.1 p)`. Results reported as qualitatively the same under linear-logarithmic and sigmoid fitness.
  - Study 1, public goods game: contribute `c = 1`, multiplier `r = 3`; punishment costs the punisher `λ = 1/2` and fines the target `ρ = 3/2`. Contribution strategies C (always), D (never), O (opportunist: cooperates if Responsible minus Antisocial punishers in the group exceeds `c/ρ`). Punishment strategies R (responsible: punish defectors), A (antisocial), S (spiteful: punish all), N (none): 12 strategies.
  - Study 2, two-player pure coordination game on norms A and B (payoff about 2 for matching, 0 otherwise, inferred from the paper's Fig. 7 caption: four coordinated games pay 8, random play pays 4); punishment types E-A, E-B (enforce A or B), S, N; opportunists match the partner's enforcement reputation.
  - **Main result**: long-run proportions of norm-adherers and responsible / norm-enforcing punishers rise with `s` in both games; a sudden threat rise raises norm strength quickly, removal lowers it more slowly. **The mechanism, stated by the authors, is the concavity of `f`**: at high threat agents sit on the steep part of the fitness curve, so the extra payoff from cooperating or coordinating matters more. Extreme `s` makes outcomes trivial (extinction or neutral drift).
- **What this means for the algebra**: in this model "fear" is not a drive inside the agents at all. It is a subtraction from everyone's baseline payoff, and the tightness result is a theorem about diminishing returns, not about fear. A drive algebra importing it should write the law as `tightness*(s) increasing in s because f'' < 0`, and note that any concave utility gives the same direction.
- **Follow-ups, read [read]**:
  - De, Nau & Gelfand 2017, "Understanding Norm Change: An Evolutionary Game-Theoretic Study", Proc. AAMAS 2017 (arXiv 1704.04720; full text read). Tightness is modelled as a *need for coordination* `c` in a payoff matrix `M = c*M_coord + (1-c)*M_fixed`, motivated explicitly by threat (citing Roos 2015). Theorem 1: if norm B pays more (`b > a`), B is an ESS, and A is *also* an ESS when `c >= (b-a)/b`. So a tight society can stay locked on the inferior norm while a loose one switches. Simulations: high `c` evolves **high cultural inertia and a low exploration rate**.
  - De, Nau, Pan & Gelfand 2018, "Tipping Points for Norm Change in Human Cultures", SBP-BRiMS, LNCS, DOI 10.1007/978-3-319-93372-6_7 (confirmed; arXiv 1804.07406 read). Replicator dynamics with fitness `f_i = (1-m) u_i + m θ_i(x,k)`, where `θ_i = [1 + exp(-k(x_i - 0.5))]^(-1)` is a conformism term and `m` is the weight of conformist transmission (tight = high m). Derives conditions for tipping points in norm change as a function of `m`, `k` and the payoff gap.
  - arXiv 1606.02570 (Nau et al., "Using Game Theory to Study the Evolution of Cultural Norms"), skimmed: a tutorial summarising Roos 2015 with the same parameters.
- **Theorems**: Roos 2015 has none (simulation). De et al. 2017 has an ESS theorem (above). "Societal threat as a moderator of cultural group selection" (Behavioral and Brain Sciences 39, 2016, DOI 10.1017/s0140525x15000114; authors Gelfand, Roos, Nau, Harrington, Mu, Jackson, confirmed) is a BBS commentary; content not read.
- **Evidence and robustness**: it is a model, so its support is internal consistency plus the match to A1. It shows threat *can* select for tightness, given concave fitness; it does not show it did.
- **Operand/operator translation**: the best existing bridge for the strand. Operand = population with a norm-strength state; environment parameter `T`; operators `adhere`, `punish(deviant)`; fixed-point or ESS selection gives `tightness*(T)`. This is a *law* (an equilibrium map from a fear input to a structure) of exactly the kind Aldred asked for, with a published formal home.

---

## B. Environment and motive: pathogens, honour, ecology

### B1. Fincher, Thornhill, Murray & Schaller 2008, "Pathogen prevalence predicts human cross-cultural variability in individualism/collectivism"

- Citation: C. L. Fincher, R. Thornhill, D. R. Murray, M. Schaller, Proc. R. Soc. B 275(1640), 1279-1285, 2008. DOI 10.1098/rspb.2008.0094 (confirmed, Crossref, all four authors).
- **Drive(s)**: disgust / pathogen avoidance. Hypothesis: where infectious disease is common, norms that limit contact with outgroups and enforce conformity (collectivism, ethnocentrism) protect health.
- **Law [from abstract]**: regional historical pathogen prevalence correlates strongly and positively with collectivism and negatively with individualism across worldwide survey datasets, and "the correlations remain significant even when controlling for potential confounding variables". (An earlier draft said "about 70 countries"; the count varies by dataset and was not verified.)
- **Theorems**: none.
- **Evidence and robustness, bluntly**: contested. Currie & Mace 2012, "Analyses do not support the parasite-stress theory of human sociality", Behavioral and Brain Sciences 35(2), 83-85 (DOI 10.1017/s0140525x11000963, confirmed): a commentary on Fincher & Thornhill's 2012 BBS target article; per its abstract, a re-analysis of the target article's data finds no evidence for a strong, universal relationship between parasite stress and sociality variables, nor for the proposed causal mechanism [from abstract]. Hruschka & Henrich 2013, "Institutions, parasites and the persistence of in-group preferences: a cross-national analysis", PLoS ONE 8(5), e63642, DOI 10.1371/journal.pone.0063642 (confirmed; abstract read): 122 countries, three measures of in-group favouritism; **government effectiveness** predicts in-group favouritism after controlling for pathogen stress and region, with reverse-causality and instrumental-variable checks, while pathogen stress gives inconsistent results once institutions are controlled and little association within world regions [from abstract]. Hruschka & Henrich 2013, "Economic and evolutionary hypotheses for cross-population variation in parochialism", Frontiers in Human Neuroscience 7 (DOI 10.3389/fnhum.2013.00559, confirmed; not read). Hruschka, Efferson, Jiang, Falletta-Cowden, Sigurdsson et al. 2014, "Impartial Institutions, Pathogen Stress and the Expanding Social Network", Human Nature 25(4), 567-579 (DOI 10.1007/s12110-014-9217-0, confirmed; not read). The gist, that institutions absorb much of the pathogen effect, is now **supported at abstract level** by the PLoS ONE paper. Verdict for the strand: a hypothesis for a drive (disgust) -> structure arrow, with an unresolved competitor (institutions, wealth). Do not use as an axiom.
- **Translation**: operand = population with pathogen load `P`; law `collectivism' = g(P)`, same form as A1. Notably, A1 and B1 are two *different* drives (fear of attack, fear of contagion) feeding the *same* structural variable (tight, conformist). That suggests the algebra can have several drive inputs map into one group-structure output.

### B2. Honour cultures: Nisbett & Cohen; Cohen, Nisbett, Bowdle & Schwarz 1996; Leung & Cohen 2011; Uskul and colleagues

- Citations: Nisbett & Cohen, *Culture of Honor: The Psychology of Violence in the South*, Westview, 1996 (book; confirmed via the Routledge reissue in Crossref, DOI 10.4324/9780429501142). Cohen, Nisbett, Bowdle & Schwarz, "Insult, aggression, and the southern culture of honor: An 'experimental ethnography'", JPSP 70(5), 945-960, 1996, DOI 10.1037/0022-3514.70.5.945 (confirmed). Leung & Cohen, "Within- and between-culture variation: Individual differences and the cultural logics of honor, face, and dignity cultures", JPSP 100(3), 507-526, 2011, DOI 10.1037/a0022151 (confirmed). Uskul, Kitayama & Nisbett, "Ecocultural basis of cognition: Farmers and fishermen are more holistic than herders", PNAS 105(25), 8552-8556, 2008, DOI 10.1073/pnas.0803874105 (confirmed; this paper is about cognition, not honour). Uskul & Cross, "The social and cultural psychology of honour: What have we learned from researching honour in Turkey?", European Review of Social Psychology 30(1), 39-73, 2019 (online 2018), DOI 10.1080/10463283.2018.1542903 (confirmed, Crossref; not read).
- **Drive(s)**: status/reputation defence, with a threshold of retaliation as the cultural parameter.
- **Law [standard account]**: where wealth is mobile and easily stolen (herding) and state protection is weak, a reputation for retaliation deters theft; the culture then trains a low threshold for responding to insult. Cohen et al. 1996 report three lab experiments in which a confederate bumped and insulted the participant; Southern men were more likely than Northern men to think their masculine reputation threatened and were more upset [from abstract via search snippet]; the cortisol and testosterone rises and more aggressive follow-up behaviour are [standard account, not read]. No direct or registered replication of the insult paradigm was found in this pass (one search); a textbook audit (replicationindex.com, 2019) notes some field-study differences were non-significant. Treat as unreplicated rather than as failed.
- **Theorems**: none directly; the logic is a deterrence / signalling game that could be written as a Hawk-Dove variant with reputation (see 09 A1). No source for that formalisation found here.
- **Evidence and robustness**: the experimental results are a few samples from one US region; the herding-origin story is a historical inference. Uskul's Turkish work tests the ecology-to-psychology step in a natural experiment, but the Black Sea study measures cognition and interdependence, not honour. The direct honour work in Turkey is reviewed in Uskul & Cross 2019 (confirmed above; not read). Honour and "face" and "dignity" as three types is Leung & Cohen's typology, with explicit attention to within-culture variation, which cuts against a reading of culture as one scalar.
- **Translation**: operand = person with a `retaliation threshold` and a `reputation` state; group with a distribution over thresholds. Operators: `insult(a,b)`, `retaliate(b,a)`. The population-level feature is how the *distribution of thresholds* is selected by the value of mobile assets and the strength of third-party enforcement. A second case of environment -> drive-parameter -> structure.

---

## C. Cultural evolution: transmission rules and their equations

### C1. Boyd & Richerson 1985 and Henrich & Boyd 1998, conformist and biased transmission

- Citations: R. Boyd and P. J. Richerson, *Culture and the Evolutionary Process*, University of Chicago Press, 1985 (book; existence confirmed via contemporary reviews indexed in Crossref, e.g. DOI 10.2307/1367778). J. Henrich and R. Boyd, "The Evolution of Conformist Transmission and the Emergence of Between-Group Differences", Evolution and Human Behavior 19(4), 215-241, 1998, DOI 10.1016/S1090-5138(98)00018-X (confirmed). J. Henrich and R. Boyd, "Why people punish defectors: Weak conformist transmission can stabilize costly enforcement of norms in cooperative dilemmas", Journal of Theoretical Biology 208(1), 79-89, 2001, DOI 10.1006/jtbi.2000.2202 (confirmed, Crossref).
- **Drive(s)**: the *drive to conform* (social-learning bias toward the majority) and the *drive to copy the successful or admired*. Not usually called drives in the literature; they are learning biases, but they function as drives for the algebra's purposes (they push the population state).
- **Equations [standard account, not read at source]**:
  - Unbiased transmission: `p' = p`. No change except drift; the null.
  - Conformist transmission, with a learner who samples three models: `p' = p + D p(1-p)(2p-1)` **[confirmed against a secondary source quoting Boyd & Richerson's equation: PMC8403876]**. `D > 0` is conformity, `D = 0` unbiased copying, `D < 0` anticonformity. With `D > 0`, fixed points p = 0, 1/2, 1; 1/2 unstable, 0 and 1 stable. A conformist population amplifies whichever variant is already in the majority. The same secondary source reports a generalisation to n >= 3 models and m >= 2 variants with the same convergence under conformity.
  - Payoff or success-biased and prestige-biased transmission: the weighted-copying form below is **this note's stylisation, not Boyd & Richerson's equation**. Their "indirect bias" models adoption of a trait through an *indicator* trait of the model (e.g. prestige), with its own runaway dynamics; that form was not checked. Stylised: copy model j with probability proportional to a weight `w_j` (payoff or prestige), so `p' = sum_j w_j x_j / sum_j w_j` with `x_j` the variant held by j.
- **Theorems** [standard account, from the titles above]: Henrich & Boyd 1998 show conformist transmission, by pushing populations toward local majorities, maintains differences between groups even under migration. Henrich & Boyd 2001 show that adding even weak conformism makes costly punishment of defectors (and punishment of non-punishers) evolutionarily stable, where without it punishment is unstable. This is the formal support for "norms are stabilised by conformity", and is a genuine theorem-bearing result, not just an empirical one.
- **Evidence and robustness**: the maths is solid as maths; the empirical claim that humans are conformist in the strong "frequency-dependent" sense is mixed and is not examined here (no source read). As models they are the best-developed population-level equations in this cluster.
- **Translation**: operand = a population state vector of variant frequencies (or norms), `p`. Operators are the transmission rules themselves: `conform(D)`, `copy_prestige(w)`, `copy_payoff(w)`; each is a map on frequency distributions, so they compose by function composition. Fear-driven tightness (A) could be modelled as raising D, which is a testable composition (see Candidate laws).

### C2. Henrich & Gil-White 2001, prestige; Cheng et al. 2013, prestige vs dominance

- Citations: J. Henrich and F. J. Gil-White, "The evolution of prestige: freely conferred deference as a mechanism for enhancing the benefits of cultural transmission", Evolution and Human Behavior 22(3), 165-196, 2001, DOI 10.1016/S1090-5138(00)00071-4 (confirmed). J. T. Cheng, J. L. Tracy, T. Foulsham, A. Kingstone, J. Henrich, "Two ways to the top: Evidence that dominance and prestige are distinct yet viable avenues to social rank and influence", JPSP 104(1), 103-125, 2013, DOI 10.1037/a0030398 (confirmed).
- **Drive(s)**: the **status drive**, split into two routes: *dominance* (induces fear, secures deference by threat) and *prestige* (earns deference by being a valued source of skill and information, induces admiration and imitation). One drive, two operators, with different emotional signatures in the followers.
- **Law [from titles and standard account]**: prestige is a human adaptation for acquiring information from skilled others; followers freely confer deference in exchange for access. Cheng et al. report that both dominant and prestigious individuals attain influence in groups, but they differ in how followers feel and why they defer. Cheng et al.'s own claim in the title is that the two are "distinct yet viable".
- **Theorems**: none stated. Henrich and Gil-White's argument is verbal plus an evolutionary rationale.
- **Evidence and robustness**: Cheng et al. **[from abstract, via search summaries]**: two studies with university students in small lab groups. Study 1: in newly formed groups, both dominance and prestige predicted perceived and actual influence; prestigious individuals were liked, dominant ones were not. Study 2 (eye tracking): both dominant and prestigious targets drew more visual attention than targets low on either. Sample sizes not read. One population (students at one Canadian university), so generalisation is open. The dominance/prestige dichotomy has been widely used, but it is a clean typology and real leaders mix both; claim stays at "two routes exist".
- **Translation**: operand = person with `rank` in a group. Operators `dominate(a,b)` (works through b's fear), `admire(b,a)` / `defer(b,a)` (works through b's desire for information or skill). This gives the algebra a concrete case of **the same output (deference) produced by different drives** and of an operator whose *effect on the target depends on which drive it engages*.

### C3. Boehm 1999, reverse dominance hierarchy

- Citation: C. Boehm, *Hierarchy in the Forest: The Evolution of Egalitarian Behavior*, Harvard University Press, 1999 (DOI 10.4159/9780674028449, confirmed in Crossref by title). The original statement: C. Boehm, "Egalitarian Behavior and Reverse Dominance Hierarchy [and Comments and Reply]", Current Anthropology 34(3), 227-254, 1993, **DOI 10.1086/204166** (confirmed, Crossref; the DOI tried earlier, 10.1086/204190, is an Errata notice in 34(4)).
- **Drive(s)**: the individual drive to dominate, and the **group drive to prevent being dominated**. Boehm's claim: in mobile forager bands the dominance drive is present in each person, and the group collectively suppresses it by coalitions against would-be alphas (ridicule, ostracism, execution), so the group inverts the hierarchy.
- **Law [standard account]**: egalitarian order is not the absence of the dominance drive but an *active equilibrium* maintained by a coalition drive against it. Its stability condition, as this note formalises it (Boehm states it verbally, not as an inequality), is that the subordinate coalition's strength exceeds the aspirant's: a threshold rule, "coalition power > individual power".
- **Theorems**: none. Related formal models exist (e.g. the evolution of leveling via punishment/coalition games), but I did not find a specific confirmed model here; not cited.
- **Evidence and robustness**: ethnographic synthesis of forager societies (Boehm used a cross-cultural sample; sample contents not checked here). The inference to Pleistocene social life is the usual weakness of this kind of reconstruction.
- **Translation**: this is the cleanest example in the cluster of a **group drive composed from individual drives with a defined operator**: `coalesce(S, a)` = a subset S of the group acts jointly on member a, and its effect is `suppress(a)` when |S| power > a's. The group drive "resist domination" is not a separate primitive; it emerges from many individuals' fear of being dominated plus a coordination operator.

---

## D. Existential security and value change

### D1. Inglehart & Baker 2000, "Modernization, Cultural Change, and the Persistence of Traditional Values"

- Citation: R. Inglehart and W. E. Baker, American Sociological Review 65(1), 19-51, 2000. DOI 10.2307/2657288 (confirmed). Fuller statement: Inglehart & Welzel, *Modernization, Cultural Change, and Democracy*, Cambridge University Press, 2005 (confirmed, DOI 10.1017/CBO9780511790881). Also **P.** Norris & R. Inglehart, *Cultural Backlash*, Cambridge University Press, 2019 (confirmed, DOI 10.1017/9781108595841; the first author is Pippa Norris, earlier given as "N. Norris").
- **Drive(s)**: need for **security** (physical, economic) as a gate on higher-order motives. Inglehart's scarcity hypothesis: people prioritise what is scarce, so security-poor conditions give *survival values* (traditional authority, in-group cohesion, xenophobia) and security-rich conditions give *self-expression values* (autonomy, tolerance, participation). It is Maslow-like, applied at the level of societies and cohorts.
- **Law [standard account]**: a value dimension (survival vs self-expression) moves with a measure of existential security, with a **generational lag** (the "socialization hypothesis": formative-years conditions fix priorities) so the response is slow. Also path dependence: religious heritage shapes the trajectory.
- **Theorems**: none.
- **Evidence and robustness**: World Values Survey, many waves and countries; the two-axis "cultural map" is a heavily cited result. Criticisms (standard, not individually verified): the survey items load differently across cultures, the causal arrow security -> values is hard to separate from the reverse and from third factors, and the later "backlash" claim says insecurity can *reverse* the trend, which is the A1 law again from another direction. Of the cross-cultural claims here this one is the best supported by data volume, and still correlational.
- **Translation**: operand = society with a state `S` (existential security) and a value vector. Law: `values' = h(values, S_lagged)`, with a lag operator. Inglehart's survival values and Gelfand's tightness are close to the same structural variable measured differently; the algebra should not make two primitives out of them without evidence that they differ.

### D2. Hofstede (measurement only)

- Citation: G. Hofstede, *Culture's Consequences: International Differences in Work-Related Values*, Sage, 1980 (confirmed via reviews indexed in Crossref, e.g. DOI 10.2307/2066725); 2nd ed. 2001 (not checked). Critique: B. McSweeney, "Hofstede's Model of National Cultural Differences and their Consequences: A Triumph of Faith - a Failure of Analysis", Human Relations 55(1), 89-118, 2002, DOI 10.1177/0018726702551004 (confirmed; not read). The dimensions as usually stated: power distance, individualism-collectivism, masculinity-femininity, uncertainty avoidance, and later long-term orientation and indulgence-restraint. Based originally on a survey of one multinational firm's employees.
- **Drive(s)**: none explicitly; "uncertainty avoidance" is nearest to fear/need for structure, "power distance" to acceptance of dominance.
- **Role in the strand**: **measurement**, not theory. Useful as candidate coordinates for a cultural state vector, and for fixing units when a law needs a number. Standard critique (McSweeney 2002, title-level only): that the dimensions are derived from one company and treat the nation as the unit of culture.
- **Theorems**: none.

---

## E. History of emotions: which drives a culture permits

### E1. Reddy, Rosenwein, Stearns

- Citations: W. Reddy, *The Navigation of Feeling: A Framework for the History of Emotions*, Cambridge University Press, 2001 (confirmed, DOI 10.1017/CBO9780511512001). B. H. Rosenwein, "Worrying about Emotions in History", American Historical Review 107(3), 821-845, 2002, DOI 10.1086/ahr/107.3.821 (confirmed). P. N. Stearns and C. Z. Stearns, "Emotionology: Clarifying the History of Emotions and Emotional Standards", AHR 90(4), 813-836, 1985, DOI 10.2307/1858841 (confirmed).
- **Drive(s)**: emotions and their *expression rules*; not drives in the strict sense, but they govern which drives may be expressed, to whom, and when.
- **Concepts [standard account, not read at source]**:
  - Stearns's **emotionology**: the standards a society holds for emotion and its expression, distinguished from the emotions people actually have. Gives the algebra a split between *norm about a drive* and *drive as felt*.
  - Reddy's **emotional regime**: the set of normative emotions and the official rituals and practices that enforce them, with **emotives** (speech acts that both describe and change emotion) and **emotional suffering** when a person cannot comply. A regime is stable if it does not generate too much suffering; Reddy proposes a *good* regime provides **emotional refuges**. His French Revolution case study (regime of sensibility) is the worked example.
  - Rosenwein's **emotional communities**: groups with shared valuations of emotions and expression modes; a person belongs to several at once.
- **Theorems**: none; this is qualitative historiography.
- **Evidence and robustness**: archive-based interpretation, not testable in the statistical sense. The central methodological debate (whether emotions are universal and only expression varies, or constructed) is unresolved and is the same fault line as in 15.
- **Translation**: this is the part of the cluster that bears most directly on the algebra's grammar. It gives a three-level structure: **drive** (felt, person), **norm about the drive** (emotionology, group), **enforcement and relief mechanisms** (regime and refuge). In algebra terms: a group operand carries a `permission` function over drives; a person's expression is `express(drive, context)` filtered by the permission; `suffering` is a discrepancy `drive - permitted_expression`, usable as a state variable that predicts regime change (Reddy's claim).

---

## F. Evolution of norms in game theory

### F1. Young 1993, "The Evolution of Conventions"; Kandori, Mailath & Rob 1993

- Citations: H. P. Young, Econometrica 61(1), 57-84, 1993. DOI 10.2307/2951778 (confirmed). M. Kandori, G. Mailath, R. Rob, "Learning, Mutation, and Long Run Equilibria in Games", Econometrica 61(1), 29-56, 1993. DOI 10.2307/2951777 (confirmed). Book-length: Young, *Individual Strategy and Social Structure: An Evolutionary Theory of Institutions*, Princeton, 1998 (confirmed, DOI 10.1515/9780691214252).
- **Drive(s)**: none explicit. Agents best-respond to a sample of past play (a drive to match, i.e. payoff-seeking), plus random error ("trembles", mutation).
- **Model and theorems** [from search summary of the paper and standard account]: **adaptive play**: each period each agent draws a sample of past plays (of size k from the last m) and best-responds, with probability epsilon makes a random choice. The unperturbed process converges almost surely to a pure strategy Nash equilibrium (a *convention*) for a large class of games including coordination and common-interest games (confirmed in the search summary). With small epsilon, the perturbed process is a regular Markov chain with a unique stationary distribution; as epsilon -> 0 it concentrates on **stochastically stable** states, found via minimum-cost "resistance trees" (the Freidlin-Wentzell technique, a standard-account statement). In a 2x2 coordination game the stochastically stable convention is the **risk-dominant** one [Young: from the paper's introduction via search summary, which says stochastically stable equilibria are "essentially the same" as risk-dominant ones in 2x2 games but differ in general games; KMR: standard account]. Conditions matter and were not read: Young's result needs *incomplete* sampling (sample small relative to memory), KMR's needs a large enough population. For bargaining (Nash demand game), Young's later chapter shows the Nash bargaining solution arises as the stochastically stable division [from a review snippet, chapter not read].
- **Evidence and robustness**: the theorems are mathematical, not empirical. Known caveat (standard, not verified here): waiting times for the selected convention can be astronomically long in large populations, so the long-run selection can be irrelevant to observed history; local interaction can fix this.
- **Translation**: this is the formal engine for "which norm wins". Operand = population with a convention state; operator = `perturb(epsilon)` and `adapt(k,m)`. It is a theorem generator: given the payoffs and the noise structure, predict which convention is long-run stable. If tightness (A) is modelled as lower epsilon (fewer deviations) and weaker local-interaction diversity, Young's machinery says which norm a tight society locks in, and why loose societies stay churning. **Correction**: the qualitative half of this link *is* published. De, Nau & Gelfand 2017 (A2, read) show that a high need for coordination evolves a **low exploration rate** and high cultural inertia, and that a tight society can stay on an inferior ESS. What remains unpublished, as far as this pass found, is the use of Young/KMR stochastic-stability machinery (resistance trees, epsilon -> 0) with a threat-dependent noise rate.

### F2. Bicchieri, social norms as conditional preferences

- Citation: C. Bicchieri, *The Grammar of Society: The Nature and Dynamics of Social Norms*, Cambridge University Press, 2006 (confirmed, DOI 10.1017/CBO9780511616037; Crossref online date Dec 2005).
- **Drive(s)**: **conditional preference for conforming**, driven by two expectations about others: *empirical* (most others do X) and *normative* (most others think I ought to do X, and may sanction me).
- **Law [standard account, formula from memory, flag for verification]**: a person follows norm x if (1) she knows the norm applies, (2) she has the empirical expectation and (3) the normative expectation (or believes others hold it), and her utility is `U_i = pi_i(s) - k_i * max over other-players' strategies of the loss others suffer when she deviates, 0`, with `k_i` a sensitivity to the norm. **Still unverified after validation**: one search did not find the formula; its usual statement is `U_i(s) = π_i(s) − k_i · max_{s_{-j} ∈ L_{-j}} max_{m≠j} max(π_m(s_{-j}, N_j(s_{-j})) − π_m(s), 0)` (from memory, same caveat) — the formal version is in the 2006 book and Bicchieri 2010, "Norms, preferences, and conditional behavior", Politics, Philosophy & Economics (not checked). The point: **norm following is a function of beliefs about others**, so changing beliefs (not payoffs) changes behaviour.
- **Theorems**: none; the book is conceptual with formal utility.
- **Evidence and robustness**: supported by experiments (dictator-game variants) in Bicchieri's own work and others; not read here.
- **Translation**: the nearest to an operator-level definition of a norm. Operand = person with beliefs `E(others do x)`, `N(others expect x)`, and parameter `k`. Operators: `inform(b, claim)` changes beliefs; `sanction`. A norm change is a *belief-revision* operator on a group, making Bicchieri a link to the epistemic logics in 04.

### F3. Ostrom, commons governance

- Citations: E. Ostrom, *Governing the Commons*, Cambridge University Press, 1990 (confirmed, DOI 10.1017/CBO9780511807763). E. Ostrom, "Collective Action and the Evolution of Social Norms", Journal of Economic Perspectives 14(3), 137-158, 2000. DOI 10.1257/jep.14.3.137 (confirmed).
- **Drive(s)**: self-interest versus a conditional willingness to cooperate and punish (she argues for "conditional cooperators" and "willing punishers" against the pure selfish-maximiser).
- **Law [standard account]**: commons can be sustained by self-organisation, not just privatisation or central rule, when design features hold: clear boundaries, rules matched to local conditions, participation in rule-making, monitoring, graduated sanctions, conflict resolution, recognition of rights to organise, nested enterprises (Ostrom's eight design principles; list from memory). The 2000 paper stresses that reputation and norm strength co-evolve with the structure of the game.
- **Theorems**: none from Ostrom; formal models (repeated games, Henrich-Boyd C1) supply theorems for parts of it. The design principles are an empirical regularity from many cases (a case-study meta-analysis), with later critique on selection of cases (standard remark, unverified). The main empirical re-test is Cox, Arnold & Villamayor Tomás 2010, "A Review of Design Principles for Community-based Natural Resource Management", Ecology and Society 15(4), 38, DOI 10.5751/ES-03704-150438 (confirmed; not read; generally read as broadly supporting the principles with some refinements).
- **Evidence and robustness**: a large case base; robust as a *description of what survived*. As a causal prediction it is weaker.
- **Translation**: group operand with `rule` set R; operators `monitor`, `sanction`, `amend(R)`. The design principles are *invariants* a group must satisfy, i.e. a predicate on group structure, which fits a type-system view (see 04).

---

## Candidate laws linking drives to norms at population scale

These are drawn from, or suggested by, the entries above. Each has the form of a hypothesis with a settable parameter. None is established as a theorem.

1. **Threat -> tightness (fear-to-structure).** `tightness* = f(T)`, f increasing; `T` aggregates conflict, disaster, density, scarcity (A1, A2). Slow dynamics; operator `threaten`, `relax`. Source status: model plus correlation.
2. **Contagion-fear -> conformity.** `conformity = g(P)` (B1). Source status: contested; may be absorbed by institutions.
3. **Tightness raises conformist weight and punishment.** `D' = D + a * tightness`, `punish_strength' = ...`. Combine with Henrich-Boyd (C1): conformity and punishment stabilise whatever norm is the majority. **Corrected**: the earlier claim that "this composition is not published" is wrong in substance. De, Nau, Pan & Gelfand 2018 already compose tightness with a conformist-transmission weight `m` inside replicator dynamics and derive tipping points; De, Nau & Gelfand 2017 compose threat-motivated need for coordination `c` with ESS analysis and evolved exploration rates (A2, both read). What is still open: tying `m` or `c` *endogenously* to the threat level `s` of Roos 2015 in one model, using Boyd & Richerson's `D` rather than De et al.'s logistic conformism term, and adding Young-style stochastic stability. That narrower composition remains the clearest "compose into equations" move, and the Gelfand-Nau group is the obvious prior art to cite and check first.
4. **Security gates values, with a lag.** `values_t = h(values_{t-1}, S_{t-L})` (D1). Source status: correlational.
5. **Two routes to deference.** `deference(a,b)` can arise from `dominate` (b's fear) or `prestige` (b's desire for skill); they are distinct operators with different follower states (C2).
6. **Egalitarian order as a standing coalition.** `coalesce(S,a)` suppresses `a`'s dominance when `power(S) > power(a)` (C3). A group drive derived from individual fear of domination.
7. **Mobile assets plus weak enforcement -> low retaliation threshold.** (B2.) Source status: ethnographic and experimental, one region mainly.
8. **Permission over drives.** A group carries a map from drives to permitted expression; `suffering = drive - permitted` predicts regime pressure (E1). Qualitative.
9. **Conventions: noisy adaptive play selects the risk-dominant convention** (F1). A theorem about conventions, available to import wholesale into any model where "which norm" is a coordination game.
10. **Norm-following depends on beliefs about others, not just payoffs.** (F2.) Gives the algebra an epistemic operator for norm change.

Observation: laws 1, 2, 4 and 7 have the same shape (an environmental condition sets a group parameter on a slow clock), while 3, 5, 6, 9 and 10 are interaction-level rules. The algebra probably needs two layers: **slow environment-to-parameter maps** and **fast operator rules**, with Young and Henrich-Boyd providing the stability theory linking the layers.

---

## What exists vs what does not

**Exists**
- Replicator / ESS machinery, imported from 09, with the conformist and prestige-biased transmission equations (C1).
- Proven results on which convention a noisy population settles on (F1) and on when costly punishment is stable under weak conformism (C1).
- A published evolutionary model that makes norm strength a function of threat (A2), and many correlational findings pointing the same way (A1, B1, D1).
- Published models that couple tightness to conformist transmission, exploration rate and norm-change dynamics, with an ESS theorem (De, Nau & Gelfand 2017; De, Nau, Pan & Gelfand 2018; reviewed in Pan, Gelfand & Nau 2021, American Psychologist 76(6), 1054-1066, DOI 10.1037/amp0000851, confirmed, not read). Gelfand et al. 2021, Lancet Planetary Health 5(3), e135-e144, DOI 10.1016/S2542-5196(20)30301-6 (confirmed, not read), pairs a COVID-19 cross-national analysis with an evolutionary game model reported (search summary only) to show tight groups cooperate faster under threat.
- A rich typology of status routes (C2), egalitarian leveling (C3), honour (B2), emotional regimes (E1) and conditional norm-following (F2).

**Does not exist (as far as this survey found)**
- A calculus in which drives are operands and composition is defined; every item here treats drives as environment inputs or parameters, not as first-class algebraic objects.
- A single model in which threat *endogenously* sets the conformity weight and noise rate and Young/KMR stochastic stability then selects the convention. The pairwise pieces exist (threat -> norm strength in Roos 2015; tightness -> conformism, inertia, exploration in De et al. 2017/2018); the full chain was not found. (Corrected from an earlier, broader "no model composes these" claim.)
- Convincing causal identification for the cross-cultural claims. Where there is evidence, it is cross-sectional, small-n, and confounded; pathogen stress is the clearest case of a headline result that is under dispute (B1).
- Formal versions of the history-of-emotions concepts (E1). They are verbal; the permission / suffering reading in law 8 is this note's translation, not a published model.
- A dynamics of how drives themselves change under culture. The literature models cultures *selecting among* behaviours; a culture reshaping the intensity of a drive in individuals (as Reddy and Inglehart suggest) is only verbally described.
- Prediction records. None of these frameworks has a forecasting track record at the population level comparable to what is claimed for them.

## Unconfirmed

All five items previously listed here were confirmed in the validation pass and moved into their entries (Boehm 1993, McSweeney 2002 and the books, Uskul & Cross 2019, the tight/loose extensions). Remaining unconfirmed:

- Gelfand et al. 2011 respondent count N = 6,823: widely cited, not seen at source (press says "almost 7,000").
- Bicchieri's norm-based utility formula (F2): not found in one search; stated from memory.
- "Pan, Gelfand & Nau 2021 PNAS" on tightness as an adaptive response (named in the validation brief): **not found**. The 2021 Pan-Gelfand-Nau paper is in *American Psychologist* (above); no PNAS paper by these three on this topic turned up in Crossref or web search. Likely a conflation.
- Boyd & Richerson's indirect (prestige) bias equations: not checked; C1 gives a stylised form only.

## Missing work worth adding (found during validation)

- De, Nau & Gelfand 2017 (AAMAS) and De, Nau, Pan & Gelfand 2018 (SBP-BRiMS): the closest existing compositions of tightness with conformism and stability. Now summarised in A2; they deserve their own entry.
- Pan, Gelfand & Nau 2021, American Psychologist (DOI 10.1037/amp0000851): the group's own review of its EGT models.
- Hruschka & Henrich 2013, PLoS ONE (DOI 10.1371/journal.pone.0063642): the strongest institutional counter-evidence to pathogen stress; now in B1.
- Jackson, Gelfand & Ember 2020, Proc. R. Soc. B: tightness tested outside modern nation-states (86 societies), with threat types diverging; now in A1.
- Fincher & Thornhill 2012, Behavioral and Brain Sciences target article on parasite stress (the article Currie & Mace answer); not checked.
- Cox, Arnold & Villamayor Tomás 2010 (Ostrom's design principles re-tested); now in F3.

## Validation log (2026-10-29)

- A1 Gelfand et al. 2011 — ✎ corrected (44 not 42 co-authors; pages added; "synchrony" finding removed as unverified-for-2011; "self-reinforcing loop" relabelled as this note's reading; extensions confirmed and added; N = 6,823 left unconfirmed).
- A2 Roos, Gelfand, Nau & Lun 2015 — ✎ corrected and **[read]** (full model reconstructed: lattice ABM, threat as payoff shift `s`, concave fitness `1 − e^{−0.1p}`, PGG and coordination games; mechanism is diminishing returns, not fear).
- A2 follow-ups (De et al. 2017, 2018) — ✎ upgraded from titles to **[read]**; ESS theorem and conformism fitness quoted.
- A2 BBS 2016 commentary — ✓ (authors added).
- B1 Fincher et al. 2008 — ✎ corrected ("about 70 countries" removed; authors and pages confirmed; law now from abstract).
- B1 Currie & Mace 2012 — ✎ corrected (it is a BBS commentary re-analysing Fincher & Thornhill 2012; abstract read).
- B1 Hruschka & Henrich 2013 PLoS ONE — ✎ added (the paper the brief named; abstract read; supports the institutions reading).
- B1 Hruschka & Henrich 2013 Frontiers — ✓. Hruschka et al. 2014 — ✓ (authors and pages added).
- B2 Nisbett & Cohen 1996 book — ✓ (confirmed via reissue). Cohen et al. 1996 — ✓ (abstract-level; physiological claims still standard account). Leung & Cohen 2011 — ✓. Uskul et al. 2008 — ✓ (DOI added). Uskul & Cross 2019 — ✓ (moved from Unconfirmed). Honour replications — ? none found in one search.
- C1 Boyd & Richerson 1985 — ✓. Conformist equation — ✓ (secondary source). Prestige/payoff-bias formula — ✎ relabelled as this note's stylisation. Henrich & Boyd 1998, 2001 — ✓.
- C2 Henrich & Gil-White 2001 — ✓. Cheng et al. 2013 — ✎ (results added from abstract).
- C3 Boehm 1999 — ✓. Boehm 1993 — ✎ resolved (DOI 10.1086/204166; earlier DOI was an errata). Threshold inequality relabelled as this note's.
- D1 Inglehart & Baker 2000 — ✓. Inglehart & Welzel 2005 — ✓. Norris & Inglehart 2019 — ✎ corrected (Pippa, not "N.", Norris).
- D2 Hofstede 1980 — ✓. McSweeney 2002 — ✓ (moved from Unconfirmed).
- E1 Reddy 2001, Rosenwein 2002, Stearns & Stearns 1985 — ✓.
- F1 Young 1993, KMR 1993, Young 1998 — ✓ (risk-dominance claim confirmed from Young's introduction, with conditions noted). Tightness-as-low-epsilon "conjecture" — ✎ corrected (qualitatively published by De et al. 2017).
- F2 Bicchieri 2006 — ✓ book; ? formula.
- F3 Ostrom 1990, 2000 — ✓. Cox et al. 2010 — added.
- "Pan, Gelfand & Nau 2021 PNAS" — ? not found; the 2021 paper is American Psychologist.
- Closing claim (composition unpublished) — ✎ corrected: pairwise compositions exist; only the full threat -> conformity/noise -> stochastic-stability chain is unfound.
- Closing verdict (two layers: slow environment-to-parameter maps, fast operator rules) — ✓ stands, and De et al. 2017/2018 are an existing instance of exactly that layering.
- Fabrications: none found; ✗ removed: only the unsupported "synchrony" finding.

**Verdict.** Citations are reliable: every DOI resolved, no fabricated works, and the errors were minor (a co-author count, an initial, a wrong DOI already flagged by the author). The substantive weaknesses were interpretive: the survey under-read the Gelfand-Nau modelling programme, so it presented as unpublished a composition that the same group has partly done, and it missed that the Roos result rests on concave fitness rather than on anything fear-specific. Formulas other than the conformist-transmission equation and the Roos/De models remain standard-account and should be source-checked before entering a model.
