# Prior work 091: group size, how operators and outcomes change with n

Direction: D559 (kind: survey, with deep-read of the primaries that were open). Date: 2026-10-29. Not committed.

Aim served (Aldred, 2026-10-29): an algebra of basic human and group drives that compose into equations, yield theorems, and are used to predict or control behaviour. This note asks: **where does the number of members n (or N) enter, in what functional form, what is proven versus fitted, and does the n-dependence reduce to drives of persons?** Cross-references: 09/22 (Dunbar social brain, not repeated at length), 10 (Olson, not read here), 24 (Karau and Williams, not read here), 66 and 70 (aggregation and coupling), 86 (Condorcet and majority), 87 (cohesion measurement).

## Provenance and honesty note

Tags: **[read]** = I fetched the full text and read it myself; **[read, part]** = read the sections named; **[sa]** = secondary account only (search summary or background), and nothing [sa] may feed an equation. DOIs were resolved at Crossref (api.crossref.org/works/<doi>) this session.

**Read at source (8):**
1. Bettencourt et al. 2007 (PNAS, PMC full text). The original drafting copy dropped the displayed equations (1 to 4); **validation 2026-10-30 read the publisher PDF (author-hosted copy, mae.engr.ucdavis.edu/dsouza/Bettencourt2007.pdf) and the displayed equations 1 to 4 are now read**, so the earlier [rebuilt from read text] tags are lifted.
2. Arcaute et al. 2015 (J R Soc Interface, PMC full text), main text; supplement not read.
3. Lindenfors, Wartel and Lind 2021 (Biol Lett, PMC full text); supplement and R code not read.
4. Zhou, Sornette, Hill and Dunbar 2005 (Proc R Soc B, PMC full text), through the Discussion.
5. Dunbar 1993 (BBS) **unedited preprint** hosted at mnytud.arts.unideb.hu/tananyag/dunbar.htm, read to the Discussion. The preprint states it is not the quotable final draft; commentaries and Author's Response not read.
6. Kao and Couzin 2014 (Proc R Soc B, PMC full text), main text; electronic supplement (the derivations of the M-cue conditions) not read.
7. Centola, Becker, Brackbill and Baronchelli 2018 (Science), **accepted manuscript** (City Research Online, openaccess.city.ac.uk/id/eprint/20031), main text and figure captions. Validation note: that CRO file also carries the Supplementary Materials; the validator read the IRB/consent statement, the Materials and Methods on confederates, and the supplementary text on N-dependence; the rest of the supplement (Fig. S7 conservative bias) is still [sa].
8. Esteban and Ray 2001 (APSR), publisher PDF from Ray's site, in full including the proofs of Propositions 1 and 2.
Also read in part: Isaac, Walker and Williams 1994 (J Public Econ, PDF): abstract, introduction, section 2, Observations 1 to 4 and the section 7 summary; the section 5 explanations and the appendices were not read.

**Not read (paywalled or no open copy found), so every claim about them is [sa]:** Olson 1965 (book); Karau and Williams 1993 (JPSP 65(4):681, doi 10.1037/0022-3514.65.4.681); Latané, Williams and Harkins 1979 (JPSP 37(6):822, doi 10.1037/0022-3514.37.6.822); Latané 1981 (Am Psychol 36(4):343, doi 10.1037/0003-066x.36.4.343); Caplow 1957, "Organizational Size", Admin Sci Q 1(4):484-505, doi 10.2307/2390870 (record confirmed at Crossref, text not seen); Dunbar 1992 (J Hum Evol 22:469, doi 10.1016/0047-2484(92)90081-J, record confirmed); Marwell and Oliver 1993. Seeds D559 named Olson, Karau and Williams, Caplow: **none of these three could be read**, and I did not substitute secondary accounts. Where I report what they say, it is from the reading of papers that quote them (Esteban and Ray quote Olson directly; that is the only Olson text I have).

---

## 1. Urban scaling: Bettencourt et al. 2007, and why it fails as a law of group size

**Citation.** Bettencourt LMA, Lobo J, Helbing D, Kuhnert C, West GB (2007). Growth, innovation, scaling, and the pace of life in cities. *PNAS* 104(17):7301-7306. doi 10.1073/pnas.0610172104 (Crossref confirmed). PMC1852329. [read]

**Scale.** Crowd/population scale (cities of order 10^4 to 10^7 people), aggregate economic and demographic indicators. Observational cross-section. No intervention; the paper's policy remark is a ranking device, "new indices of urban rank according to deviations from the predictions of scaling laws". Not a membership or group-decision result.

**Their vocabulary.** "Universality classes", "increasing returns", "economies of scale", "pace of life", "social currencies", "urban metabolism". City is "integrated economic and social units, usually referred to as unified labor markets" i.e. MSAs (US), LUZs (EU), UAUs (China). [read]

**Operands.** N, city population; Y, an indicator (wages, patents, road surface, crimes). No persons with states; no drives. The paper says only that superlinear exponents reflect "knowledge spillovers" and "social interactions", never modelled. [read]

**Equations.**
- Y(t) = Y0 N(t)^beta (eq. 1, "Y0 is a normalization constant"). [read, validation: publisher PDF; also restated as Arcaute eq. 1.1]
- Taxonomy (Table 2), [read]: beta < 1 (about 0.8), "Optimization, efficiency", biological, sigmoidal growth with a population limit; beta = 1, "Individual maintenance", exponential; beta > 1 (about 1.1 to 1.3), "Creation of information, wealth and resources", boom/collapse via finite-time singularity.
- Exponents, 95% CI, adj R^2 (Table 1), [read]: new patents 1.27 [1.25,1.29], 0.72, 331 US MSAs 2001; inventors 1.25; private R&D employment 1.34 [1.29,1.39]; total wages 1.12 [1.09,1.13], 0.96; GDP China 1.15 [1.06,1.23]; GDP EU 1.26 [1.09,1.46], R^2 0.64; serious crimes 1.16 [1.11,1.18]; new AIDS cases 1.23; total housing 1.00; total employment 1.01; household electricity 1.00 (Germany) and 1.05 (China, CI [0.89,1.22]); gasoline stations 0.77; road surface 0.83 [0.74,0.92], n = 29; cables 0.87.
- Pace of life: "characteristic times are predicted to scale as N^(1-beta), whereas rates scale as their inverse, N^(beta-1)"; walking speed exponent **0.09 +/- 0.02, R^2 = 0.80**; resistive loss beta = 1.11 +/- 0.06. [read]
- Growth: Y = R N + E (dN/dt), with R the per-capita maintenance cost and E the cost to add one person. Eq. 2 as printed: dN/dt = (Y0/E) N^beta - (R/E) N. Eq. 3: N(t) = [Y0/R + (N^(1-beta)(0) - Y0/R) exp(-(R/E)(1-beta)t)]^(1/(1-beta)). Eq. 4: t_c = -(E/((beta-1)R)) ln[1 - (R/Y0) N^(1-beta)(0)], approximately (E/((beta-1)R)) / N^(beta-1)(0). [read, validation: publisher PDF] Solutions stated in the text: beta < 1 gives a carrying capacity N_inf = (Y0/R)^(1/(1-beta)); beta = 1 gives N(t) = N(0) exp((Y0-R)t/E); beta > 1 with N(0) < (R/Y0)^(1/(beta-1)) gives unbounded growth reaching infinity in finite time t_c; with N(0) > that value, stagnation and collapse. Cycle spacing t_i proportional to t_c, about 1/N_i(0)^(beta-1); "t_c is about 50 tau nu^(1-beta) years" with E/R about tau x 20 years and N_i(0) about nu x 10^6. [read]
- Fit: New York relative growth shows super-exponential periods, "observations are well fit by Eq. 4, with beta = 1.09" (one city, a few cycles). [read]

**What changes with n.** Everything is a function of N by construction. The theorem content is the **sign of (beta - 1) selects the regime**: below 1 saturation, at 1 exponential, above 1 finite-time blow-up that only repeated "innovation" resets. That is a derived result from two assumptions (power-law yield, linear maintenance cost) and is the only theorem-like object in this file.

**What changes with composition or definition.** The authors concede it: "More detailed definitions of city boundaries are desirable"; "we have not addressed the issue of location". Arcaute et al. then show the exponents move with the definition (section 2).

**Empirical standing, blunt.** In-sample fits on the authors' own definitions are tight (R^2 0.72 to 0.96 for the main wealth and innovation series). Robustness to the unit of aggregation is what fails (section 2). The beta for patents, 1.27, is the exponent the whole "innovation is superlinear" claim rests on, and Arcaute's reanalysis shows it flips with a population cut-off.

**Translation.** n enters as an exogenous scale variable and the output is a per-capita rate N^(beta-1). In an algebra this is a *scale operator* acting on an aggregate, not an operator on persons. It supplies no drive. It is useful as the claim to be tested: "per-capita rate of a social output rises with n". The test must fix the boundary rule first.

---

## 2. Cross-check: Arcaute et al. 2015, scaling exponents are not stable under city definition

**Citation.** Arcaute E, Hatna E, Ferguson P, Youn H, Johansson A, Batty M (2015). Constructing cities, deconstructing scaling laws. *J R Soc Interface* 12(102):20140745. doi 10.1098/rsif.2014.0745 (Crossref confirmed). PMC4277074. [read, main text]

**Scale.** Crowd/population, England and Wales, 2001 census (8850 wards), patents 2000-2011. Observational.

**Method [read].** Cluster adjacent wards with density >= rho0 for integer rho0 in [1,40] persons/ha (40 realizations); add wards whose largest commuting flow to a cluster exceeds tau0 in {0,5,...,100}%; impose minimum cluster population N0 in {0, 10^4, 5x10^4, 10^5, 1.5x10^5}; "more than 2x10^4 realizations of systems of cities". Reference definition rho_c = 14 persons/ha (Zipf distribution of city sizes holds; set just before Liverpool and Manchester merge).

**Findings [read].**
- "Most urban indicators scale linearly with city size, regardless of the definition of the urban boundaries. However, when nonlinear correlations are present, the exponent fluctuates considerably." Sublinear road and path area, and superlinear patents and managers, do not show the expected regime ("sometimes into the wrong regime").
- **Patents:** with minimum population 10^4 the exponent is superlinear at 95%; with 5x10^4, "linearity cannot be rejected". Many cities, some over 1.8x10^5 people, have zero patents in ten years, so the measure is "unable to present a quantifiable measure" for them. Cambridge, Guildford, Newbury, Slough lead per capita, not the largest cities.
- **Total income:** the heat map over (density, commuting thresholds) is homogeneous; "population size does not convey any information on agglomeration effects".
- **London** is classified as a dragon-king (statistical test in the supplement, not read); the authors suggest "a two-system theory of cities" might emerge (global hubs treated separately from domestic cities). [wording corrected in validation]
- With the LUZ definition (21 E&W cities) the results "do not corroborate the expected behaviour".

**Verdict between the two papers.** Bettencourt's exponents are right for the units Bettencourt used, in the countries he used; Arcaute shows they are not a property of N alone but of N together with the boundary rule and the minimum-size cut. Arcaute's claim is about England and Wales; it does not by itself falsify US results. I did not search for published replies from the Bettencourt side, so "settled" would be unearned.

**Translation.** The consequence for an algebra is general: **a group-size law needs its membership rule as an argument.** Y = f(N; boundary rule, minimum size), not f(N).

---

## 3. Dunbar layers: the 1993 regression, the 2005 layer ratio, and the 2021 deconstruction

### 3a. Dunbar 1993 (preprint)

**Citation.** Dunbar RIM (1993). Coevolution of neocortical size, group size and language in humans. *Behav Brain Sci* 16(4):681-694 (target article; 681-735 with commentary). doi 10.1017/S0140525X00032325 (Crossref confirmed). **Read: the unedited preprint**, not the final text. Predecessor: Dunbar 1992 J Hum Evol 22:469-493, [sa] (not read; the 1993 paper restates its regression).

**Scale.** Membership/group; cross-species regression, then ethnographic census of human groupings. Observational.

**Equations [read, preprint].**
- log(N) = 0.093 + 3.389 log(CR) (eq. 1), N = mean group size, CR = neocortex volume / rest-of-brain volume, 36 primate genera, reduced major axis, r^2 = 0.764, t34 = 10.35.
- Human CR = 4.1 (neocortex 1006.5 cc, brain 1251.8 cc), "about 50% larger than the maximum value for any other primate". Predicted N = **147.8, 95% CI 100.2 to 231.1**. Alternative indices give 107.6 to 248.6. The author says extrapolation beyond the X range "is frowned on" and justifies it as "exploratory rather than explanatory".
- G = -0.772 + 0.287 N (eq. 2), G = percent of day grooming, 22 catarrhine species in stable groups, r^2 = 0.589; the human prediction needs about 42% of the time budget (28% to 66% across the CI); about 20% is "an absolute upper limit" seen in primates. A group of 200 would need 56.6%. So **grooming time is linear in n**; this is the time-budget argument for language.
- Conversation groups: language should be 147.8/53.5 = 2.76 times as efficient as grooming, so conversation groups of about 3.8 (one speaker plus 2.8 listeners). Observed: restaurant bookings mean 3.8 (n = 3070, Cohen 1971 as reported); refectory conversations asymptote about 3.4, splitting at multiples of about four ("Dunbar and Duncan, submitted", not independently available).
- Census of human groupings (Table 1): three size classes, camps 30 to 50 (mean 37.7), intermediate 100 to 200 (mean 148.4, range 90 to 221.5, N = 9; 134.8 over N = 15), tribes 500 to 2500 (mean 1154.7). Armies: 20th-century company mean 179.6, "does not differ significantly from the 147.8". Hutterites split around 150 because peer pressure alone fails beyond it (Dunbar citing Hardin 1988; the mean of the 51 Schmedenleut communities (spelling as printed) is 106.9, citing Mange and Mange 1980); Naroll's threshold at settlement size about 500 for authoritarian officials; Forge's 150 for kinship-based cohesion in New Guinea.
- Within 50 to 500 members "a marked negative effect of group size on both group cohesion and job satisfaction (absenteeism and turnover)" (citing Indik 1965; Porter and Lawler 1965; Silverman 1970, [sa] for those).

**Why it matters for the algebra.** The *form* of n-dependence is a capacity constraint: the number of dyadic bonds a person can service, with bonding time linear in n. That is an individual-level resource (a time budget), which is the one place in this file where n-dependence plausibly reduces to something drive-like (bonding effort against a budget).

### 3b. Zhou et al. 2005, a hierarchy of preferred sizes

**Citation.** Zhou W-X, Sornette D, Hill RA, Dunbar RIM (2005). Discrete hierarchical organization of social group sizes. *Proc R Soc B* 272:439-444. doi 10.1098/rspb.2004.2970 (Crossref confirmed; the Crossref date is 2005-02-17). PMC1634986. [read]

**Scale.** Membership, individual network layers and community sizes; descriptive.

**Findings [read].** 61 group sizes pooled from literature (support cliques, sympathy groups, bands, communities, mega-bands, tribes). Mean layer sizes S0..S6 = 1, 4.6, 14.3, 42.6, 132.5, 566.6, 1728; successive ratios 4.58, 3.12, 2.98, 3.11, 4.28, 3.05, mean 3.52. Log-periodicity from a Lomb periodogram of the (H,q)-derivative D_q^H f(s) = [f(s) - f(qs)] / [(1-q)s]^H: peak at omega1 = 5.40, preferred ratio lambda = exp(2 pi/omega1) about 3.2, confidence 0.993 under white noise (about 0.99 with Hurst 0.6, falls to 0.85 with Hurst 0.7); synthetic-null probability of chance 0.024 (and 77/10^4 for the two-peak test). Christmas-card data (42 UK subjects) give omega about 5.2, lambda about 3.3 for layers below 150. Military hierarchies also show a factor of about 3.

**Limits stated by the authors.** "At present, there is no obvious reason why a ratio of three should be important." They do not know whether the constraint is cognitive or time-budgeting. The sample pools studies that define "group" differently ("irrespective of how the social network itself was defined").

**Translation.** If the layers are real, n is not continuous: **an index set of preferred sizes {about 4, 14, 43, 133, 567...}** with a geometric ratio. An algebra could carry layer ℓ as an argument rather than n. There is no equation producing the ratio.

### 3c. Lindenfors, Wartel and Lind 2021, deconstruction

**Citation.** Lindenfors P, Wartel A, Lind J (2021). 'Dunbar's number' deconstructed. *Biol Lett* 17(5):20210158. doi 10.1098/rsbl.2021.0158 (Crossref confirmed). PMC8103230. [read]

**Findings [read].** Bayesian and phylogenetic GLS regressions of group size on neocortex and rest-of-brain, n = 71 species (and 126, 142 on brain/body). Estimated human group size: Bayesian **69.2 (95% interval 3.8 to 292.0)** for the model they call best; 108.6 [4.6, 520.0]; 79.8; 79.1. GLS 16.4 [2.1, 127.7]; 42.0 [5.2, 336.3]; 23.6; 23.8. One supplementary estimate came "close to 150" (134.0, interval 7.0 to 583.2). They note these are means, not bounds. Conclusion: "A cognitive limit on human group size cannot be derived in this manner." They add that the neocortex-group size correlation has been replicated but "often not finding a significant relationship", mostly on shared brain data, and that primate group size is mostly socio-ecological (foraging, predation).

**Verdict between 3a and 3c.** The 1993 interval (100 to 231) comes from a non-phylogenetic regression on 36 genera and treats genera as independent. Phylogenetically controlled fits give intervals spanning two orders of magnitude, so **no particular number is supported as a cognitive limit**. The ethnographic clustering near 150 (Dunbar's Table 1, mean 148.4, N = 9) is a separate piece of evidence that 3c does not address; it rests on a handful of societies and a flexible definition of "intermediate grouping" and has not, in what I read, been tested against a null of no preferred size.

---

## 4. Group decision quality versus n: Kao and Couzin 2014

**Citation.** Kao AB, Couzin ID (2014). Decision accuracy in complex environments is often maximized by small group sizes. *Proc R Soc B* 281:20133305. doi 10.1098/rspb.2013.3305 (Crossref confirmed; published 2014-06-07). PMC4043084. [read, main text]

**Scale.** Group decision; theoretical model, no human or animal data of its own. Majority rule between two options.

**Equations and results [read].**
- Baseline (Condorcet 1785, as they state it): independent voters with r > 0.5 under simple majority give accuracy above r, **monotonically increasing in group size, to perfect accuracy as n goes to infinity**.
- Two-cue model: a low-correlation cue (independently sampled by individuals, reliability r_L) and a high-correlation cue (shared by all, reliability r_H). Each individual follows the low cue with probability p. **Wisdom of crowds holds iff p > 1/(2 r_L)**; otherwise a large group's accuracy tends to **r_H alone**, "this cue can control the group decision even when only a minority of the group uses the cue", i.e. 1/2 < p < 1/(2 r_L). In that regime a **finite, usually small, group size (greater than 1) maximizes accuracy**, because binomial noise in small groups lets them escape the shared cue.
- Fluctuating-reliability model: with probability g reliability is r+eps, with 1-g it is r-eps; wisdom of crowds iff eps < r - 1/2 (one third of environments); otherwise an infinite group attains accuracy g; here optimal size is mostly 1 or infinity.
- Fraction of environments allowing wisdom of crowds under strategies: maximizing 50%, matching 18%, random 0%, versus 31% uncoupled; with M cues, maximizing gives M_L/M, random and majority strategies need M_L/M > 1/(2<r>_L). Combined-correlation environment: wisdom of crowds guaranteed only if p > 1/(2(r_L - eps)); the proportion of environments satisfying it is (8/3) times a double integral, **= 0.076** (about 7.6%). [corrected in validation from the publisher PDF: "8/3" is the prefactor of the integral, not the proportion]

**What changes with n.** Proven within the model (closed-form conditions): the *sign* of d(accuracy)/dn flips on a condition about the information structure (shared versus independent cues), not about n. **n-dependence depends on a composition variable: how correlated members' information is.**

**Empirical standing.** None in the paper for human groups. A model result about animal-style voting. Treat as a theorem about majority aggregation under correlated inputs.

**Translation.** Majority aggregation as an operator whose n-monotonicity is conditional on a correlation parameter between members. In the algebra this is an *argument of the aggregation operator* (correlation of members' inputs), exactly the composition variable D560 will need.

---

## 5. Size thresholds in mobilisation and norm change: Centola et al. 2018

**Citation.** Centola D, Becker J, Brackbill D, Baronchelli A (2018). Experimental evidence for tipping points in social convention. *Science* 360(6393):1116-1119. doi 10.1126/science.aas8827 (Crossref confirmed). Accepted manuscript read from City Research Online (may differ from the published version). [read, main text; supplement not read]

**Scale.** Crowd/group-scale adoption of a convention, small online communities (N from 20 to 30, 194 subjects, 10 groups). Experimental. The intervention is a **committed minority of undisclosed confederates** introduced after a convention formed; subjects gave informed consent to the study (IRB approval; "All players were required to provide informed consent in order to register", supplementary methods, read in validation), and the methods state "users had no way of distinguishing confederates from experimental participants"; no debriefing statement was found in what was read. So: consent to the experiment, manipulation of the target norm by hidden actors.

**Model [read].** Naming game; agents choose the option with the greatest expected reward over a memory of M past interactions; coordination pays, failure is penalised. The predicted critical fraction depends on **memory length M and population N** only. Short memory (M < 5): smaller critical mass; long memory (M > 100): "well below 50%". Simulations over 20 < N < 100,000: for N > 1000 "the predicted tipping point for social change is constant and independent of N" (as a fraction); for 20 < N < 1000 stochastic fluctuation adds uncertainty. "With larger population sizes the critical mass point becomes more exact... approaching 24.3% of the population" (main text); the supplementary text gives "For population sizes from 1000 to 100,000 the tipping point stabilizes at a value of 24.2%" [read, validation]. The 0.1-point difference is the authors' own; neither figure should be quoted to that precision.

**Results [read].** Committed minorities 15% to 35%. Five paired trials: with C < 25%, on average only 6% of the non-committed adopted the alternative by the final round, converts reverted; with 25% <= C <= 31%, the alternative reached the majority (uptake 72% to 100% for 25% to 27%; consensus at 31%). P = 0.01 (Wilcoxon rank sum). Largest unsuccessful minority 21%, smallest successful 25%; in Trial 1 the switch came from adding one person. Calibration: M in [9,13] predicts 80% of subjects' choices; simulation with N = 24, T = 100, M = 12.

**What it rules out.** The text states the result disagrees with models predicting a 10% threshold and agrees with the roughly 30% suggested by Kanter-style qualitative organisation studies. The authors state: "the critical mass value of 25% is not expected to be a universal value."

**What changes with n.** The threshold is a **fraction** in this model and does not depend on N for N > 1000 (an invariance, not a growth law); the absolute number of committed individuals therefore scales linearly with N. Small N has noise rather than a different threshold. **It depends on M (cognition/memory) and on payoffs favouring the established convention.** With a conservative bias toward the established convention, tipping is still predicted "by committed minorities with only marginally larger group sizes", i.e. a slightly larger committed group, not a larger population (Fig. S7; main-text statement read, the figure not read).

**Evidence limits.** One task (naming a picture), short windows, anonymous strangers, rewards that strongly favour coordination, ten groups. The 25% is a property of this payoff and memory structure.

**Translation.** A threshold operator: adoption flips when committed share exceeds theta(M, payoff bias). This is the same shape as Granovetter's rule (66, 86), now with an empirically located theta for one setting.

---

## 6. Group size, free-riding and cooperation: Esteban and Ray 2001, Isaac et al. 1994, with Olson and Karau-Williams as unread seeds

### 6a. Esteban and Ray 2001 (a theorem about n)

**Citation.** Esteban J, Ray D (2001). Collective action and the group size paradox. *Am Polit Sci Rev* 95(3):663-672. doi 10.1017/S0003055401003124 (Crossref confirmed). [read in full, with proofs]

**Scale.** Group mobilisation (probability of winning a contest between interest groups). Theory only; no data. Intervention concept: none; it is a comparative-statics result.

**Olson, as quoted by them [read of the quotation only; Olson's book not read].** "The larger a group is, the farther it will fall short of obtaining an optimal supply of any collective good, and the less likely that it will act to obtain even a minimal amount of such a good." They state the "common wisdom": Olson holds for private prizes and reverses for purely public ones.

**Model [read].**
- Individual utility u(w, a) = w - v(a), v convex increasing, v'(0) = 0; w per-capita benefit.
- Per-capita benefit w_i = lambda P + (1 - lambda) M / N_i, lambda in [0,1] the publicness share. Perceived publicness theta(lambda, N_i) = lambda P / [lambda P + (1 - lambda)(M/N_i)], nondecreasing in N_i.
- Win probability of group i: pi_i = A_i / A (ratio contest), A_i = N_i a_i. First-order condition (1/A)(1 - pi_i) w(lambda, N_i) - v'(a_i) = 0. Equilibrium exists and is unique; a_i = pi_i A / N_i, so individual effort falls with N_i while group effort A_i need not.
- Elasticity of marginal cost alpha(a) = a v''(a)/v'(a). Eq. 12 (holding A fixed): d pi_i/dN_i = (pi_i/N_i) [alpha(a_i) - (1 - theta(lambda, N_i))] / [alpha(a_i) + pi_i/(1 - pi_i)]. [corrected in validation; the earlier draft had 1/pi in place of pi/N. Read from a layout-extracted PDF, so treat the exact form as needing one more look at the page image before it feeds an equation; the sign condition alpha > 1 - theta is unambiguous]
- **Proposition 1.** (a) If inf alpha > 1, win probability is strictly increasing in group size for all lambda, including purely private prizes. (b) More generally, win probability is increasing over a pair of sizes n < n' if theta(lambda, n) >= 1 - inf alpha; automatically true for large enough n if inf alpha > 0 and the good is not fully private, or for lambda near 1.
- **Proposition 2.** The same condition applies to raising one group's size across equilibria; the win probabilities of all other groups fall.
- In the paper's words, "The only point that guarantees the Olson result is the origin of the diagrammatic axes (corresponding to both alpha = 0 and lambda = 0)", a linear cost with a fully private prize; elsewhere below the Figure 1 boundary the Olson result "may or may not be valid, depending on how large the starting group size is". With alpha >= 1 (quadratic cost or steeper) larger groups are more effective whatever the prize. [corrected in validation: the earlier draft listed alpha = 0 alone, and alpha in [0,1] with lambda = 0, as guaranteeing Olson; the paper does not say that]

**Translation.** n enters through **two separate channels**: dilution of the private share M/N_i, and the increasing marginal cost of effort. The sign of the net effect depends on alpha, a property of the individual's effort-cost curve (a motivation-structure parameter). Also: the group is defined by a *shared first-ranked option* and all members are identical (assumed), so heterogeneity is excluded by construction.

### 6b. Isaac, Walker and Williams 1994 (experimental n from 4 to 100)

**Citation.** Isaac RM, Walker JM, Williams AW (1994). Group size and the voluntary provision of public goods: experimental evidence utilizing large groups. *J Public Econ* 54(1):1-36. doi 10.1016/0047-2727(94)90068-x (Crossref confirmed). [read, part: abstract, sections 1 to 2, Observations 1 to 4, section 7]

**Scale.** Group cooperation (token contributions to a group account). Experiment, voluntary contribution mechanism, group sizes 4, 10, 40, 100, ten rounds, extra-credit and cash rewards; students. Intervention: the incentive structure (MPCR), by consent and open instruction.

**Design [read].** Payoff = pi_i (Z_i - m_i) + G(m_i + sum m_j)/N; marginal per-capita return MPCR = [G'(.)/N]/p_i, held at 0.30 or 0.75 across N (and 0.03 in extra cells). Single-period dominant strategy is zero contribution (MPCR < 1); finite-round Nash is complete free-riding.

**Results [read].**
- Obs. 2: for N = 40 and 100, **the positive correlation between MPCR and contributions disappears** over [0.30, 0.75], in contrast to N = 4, 10.
- Obs. 3: at MPCR = 0.30, N = 40 and 100 **contribute more** on average than N = 4 and 10. Obs. 4: at MPCR = 0.75, no discernible difference across N.
- At MPCR = 0.03 with N = 40, contributions are low (the MPCR effect "reappears").
- Abstract: "groups of size 40 and 100 provided the public good more efficiently than groups of size 4 and 10". They conclude that behaviour depends on "a subtle interaction between group size and MPCR rather than simply the sheer magnitude of either"; by period 10, 35% to 40% of subjects are at complete free-riding while a peak of 15% to 20% sits at 100% contribution (section 6, read in part). Standard backward-induction Nash fails.

**Meaning of "pure group size effect".** MPCR is held fixed by scaling G with N. If instead the group-account return shrinks with N, then per-capita return falls and efficiency falls: Isaac et al. 1994 restate the earlier Isaac and Walker (1988) result "that a higher marginal benefit from the public good leads to less free riding" and propose crowding (falling marginal return) as the standard reason large groups do worse. [read in Isaac et al. 1994; Isaac and Walker 1988 itself not read, so [sa] for that paper] So the Olson-style claim "bigger is worse" is actually a claim about *what is held fixed* when n changes.

**Standing.** Replicable in the authors' hands; the claim is limited to students, laboratory VCM, ten rounds. I did not read their explanations (section 5) or the later replications.

### 6c. Olson and Karau-Williams (unread, [sa])

- **Olson 1965** (via 6a's quotations): larger groups worse at collective goods. Esteban and Ray's theorem and the Isaac et al. data both contradict it as a general law.
- **Karau and Williams 1993 (JPSP 65:681)** [sa]: a meta-analytic review of social loafing, 78 studies per a secondary summary; model is the collective effort model (expectancy, instrumentality, valence applied to group outcomes). Secondary summaries say group size moderated loafing, with direction and size not retrievable; one blog quotes "g about 0.44", **unverified and not to be used**. Latané et al. 1979 [sa]: group sizes 2, 4, 6 in shouting and clapping, with pseudogroups separating motivation from coordination loss; a flashcard site quotes 82% (one other person) and 74% (five others), unverified. Ringelmann rope-pulling (about 49% of solo effort in a group of eight, per a blog), unverified. None of this feeds an equation. File 24 has the CEM structure from a different reading.
- **Caplow 1957** (JSTOR 2390870) [sa]: a review of organisational size and structure; not read. Recorded as a pointer only.

---

## Cross-cutting findings (all from what I read)

1. **What is held fixed when n varies decides the answer.** Isaac et al.: hold MPCR fixed and n barely matters or helps; let return fall with n and cooperation falls. Esteban and Ray: the answer flips on alpha and publicness. Kao and Couzin: the answer flips on the correlation between members' information. Arcaute: the answer flips on the city definition and the minimum-size cut. A law of the form f(n) is therefore under-specified; the specification needs (n, what scales with n, the membership rule).
2. **n enters in a small number of distinct functional forms**, each with its own domain: power law Y0 N^beta with sign(beta - 1) selecting the regime (Bettencourt; fragile); log-linear capacity N versus neocortex ratio (Dunbar; wide intervals); linear time cost G = a + bN (Dunbar eq. 2); discrete geometric layer set with ratio about 3 (Zhou); dilution M/N (Esteban and Ray); majority-vote accuracy with monotone or interior-optimum behaviour depending on correlation (Kao and Couzin); a fraction-threshold independent of N above about 1000 but memory-dependent (Centola).
3. **Only three results here are theorems:** the growth regime classification by beta (Bettencourt, conditional on the power law), the group-size reversal conditions (Esteban and Ray, Propositions 1 and 2), and the Condorcet-failure conditions p > 1/(2 r_L) and eps < r - 1/2 (Kao and Couzin). Everything else is a fit.
4. **No source here gives a group-size effect with a verified link to a person-level drive.** The nearest are Esteban and Ray (effort cost curvature) and Centola (best response with memory).

## What exists versus what does not

Exists: a tight in-sample urban scaling corpus whose exponents move with boundary definition; a primate cognition-versus-group-size correlation with a human extrapolation of 148 (CI 100 to 231) that phylogenetic reanalysis puts anywhere between 2 and 520; a pooled finding of layer ratios near 3 with no mechanism; a proved majority-voting n-dependence conditional on information correlation; a proved reversal of Olson's paradox under convex effort cost; a laboratory cooperation experiment to N = 100 that contradicts the free-rider prediction at low MPCR; one experiment locating a 25% tipping fraction in one coordination game.

Does not exist (in what I read): an empirical group-size law for cohesion, fission or decision quality in human groups; any estimate of how loafing scales with n that I could verify (Karau and Williams unread); any mechanism for the ratio of 3; any join/stay/leave data against n in this file; any test that the 25% fraction carries across tasks; any test of the Esteban-Ray condition alpha on real lobbying data.

## Unconfirmed

- Karau and Williams 1993 group-size moderator, direction and magnitude; any effect size. Latané 1979 per-person figures. Ringelmann 49%. All [sa], unread.
- Olson 1965: only the Esteban and Ray quotation was read.
- Caplow 1957: record confirmed, text unseen; "Organizational Size" appears as a literature review in secondary mentions.
- Dunbar 1992 and the final text of Dunbar 1993; the "Dunbar and Duncan, submitted" conversation data (cited in the preprint, not independently seen).
- (Resolved in validation: Bettencourt eqs. 1 to 4 read in the publisher PDF; Kao and Couzin's "8/3" is a prefactor, proportion 0.076; Esteban and Ray eq. 12 corrected, see 6a.)
- Centola supplement Fig. S7 (conservative-bias analysis). The N-dependence text was read in validation.
- Whether Bettencourt's group has replied to Arcaute: one search in validation found no direct reply. The debate continued elsewhere, e.g. Leitão, Miotto, Gerlach and Altmann 2016, "Is this scaling nonlinear?", R Soc Open Sci 3:150649, doi 10.1098/rsos.150649, and Cottineau, Hatna, Arcaute and Batty 2017, "Diverse cities or the systematic paradox of Urban Scaling Laws", Comput Environ Urban Syst 63, doi 10.1016/j.compenvurbsys.2016.04.006 (both records confirmed at Crossref; neither read).
- Whether Zhou's ratio of 3 survives a null for pooled data of this heterogeneity; the authors' synthetic null uniform in ln s is one choice.

## Does it reduce to a drive basis?

**Partly in two places, not elsewhere.**
- *Reduces (person-level motive plus a counting rule):* Esteban and Ray: utility is benefit minus convex effort cost; free-riding is the incentive to withhold effort, and n enters by shrinking the private share M/N and by the shape of the cost curve alpha. This is a desire-versus-effort-cost structure with n as an aggregation parameter. Centola: agents maximise expected coordination reward over a memory of M interactions; the "drive" is the wish to match the partner plus an aversion to the failure penalty, with M as the only cognitive parameter; n and the committed fraction enter as population composition. Dunbar's time budget: bonding effort against a fixed fraction of the day, linear in n (G = -0.77 + 0.287 N).
- *Does not reduce:* Bettencourt's beta (a property of the aggregate, with the "social interaction" mechanism asserted, not modelled; growth uses resource costs R and E, not motives). Zhou's ratio of about 3 (the authors say there is "no obvious reason"). Kao and Couzin's accuracy curve (a property of aggregation under information correlation, not of any drive: r and p are probabilities of being correct and of following a cue). Isaac et al.'s large-group result: 35% to 40% complete free-riders and a 15% to 20% peak of full contributors by period 10 shows heterogeneity of motive, and the paper offers explanations I did not read; the shift with n is not derived from a drive.
- Net: n-dependence in this file is carried mainly by **aggregation, information and boundary structure**, not by drive intensities. If drives are the primitives, n must enter as a parameter of the composition operators (share, correlation, memory, boundary), not as a property of any drive.

## What does it predict or control, and how well?

- **Bettencourt:** predicts cross-sectional indicators per city from N. In-sample R^2 0.72 to 0.96 (patents 0.72, wages 0.96), GDP EU 0.64. The walking-speed prediction (beta - 1 = 0.09) is a genuine derived prediction that matched. Out of the authors' definitions it fails: Arcaute finds most E&W indicators linear, patents' exponent flipping between superlinear and linear on a 10^4 versus 5x10^4 cut, income uninformative, London an outlier. No intervention was tested; the policy use is ranking cities against the fit.
- **Dunbar:** predicted 147.8 (100 to 231) with the observed intermediate ethnographic mean 148.4 (N = 9), which looks like a successful out-of-sample hit but (the note-writer's reading, not a claim in the paper) the human target was identified among several candidate groupings after the prediction was known, and phylogenetic reanalysis gives 16 to 109 with intervals up to 520. The conversation-size prediction (3.8) matched observed 3.8 (restaurant bookings, [as quoted in the preprint]) and about 3.4 (refectory, unpublished at the time). No control use.
- **Zhou:** describes; no prediction tested out of sample.
- **Kao and Couzin:** predicts that small groups can beat large ones under correlated cues. Not tested on data in the paper. Failure is built in: the usual wisdom of crowds holds in only about a third (fluctuating model) to 50% (best strategy) of environments.
- **Centola:** predicts the tipping fraction. Within the paper: for the experiment's own scale (N = 24, M = 12, T = 45 to 100) the model's critical mass is a band of about 20% to 30% (Fig. 3 caption), with 24.3% the large-N limit; observed threshold between 21% (fail) and 25% (success); 10 groups; P = 0.01; 80% of individual choices predicted. A genuine control result: a committed minority above the fraction overturned a convention by hidden confederates. The 10% prediction of a competing model failed. Not shown beyond one naming game.
- **Esteban and Ray:** proves what happens, does not predict magnitudes. Isaac et al. disproves the naive Olson/Nash prediction at N = 40 and 100 for MPCR = 0.30.
- **Overall:** the best-supported steering knob is the committed-minority fraction in a coordination setting (Centola, one setting, small N). The best-supported *negative* result is that a pure n-law for cooperation or size limits is not established.

## Validation log (2026-10-30)

All 14 DOIs in the note resolved at api.crossref.org with matching authors, journal, volume and pages (Kao and Couzin's Crossref title reads "small group size"; the published PDF reads "sizes", as cited). PMC returned a bot-check page for Bettencourt, Kao-Couzin and Zhou, so the validator read other open copies of the same work, named per line.

- ✓ Bettencourt, Lobo, Helbing, Kühnert, West 2007 (PNAS): read in the author-hosted publisher PDF. Table 1 rows, Table 2, walking-speed 0.09 +/- 0.02 (R^2 0.80), t_c about 50 tau nu^(1-beta), New York beta = 1.09 all confirmed. ✎ equations 1 to 4 now read and written out; [rebuilt] tags lifted.
- ✓ Arcaute, Hatna, Ferguson, Youn, Johansson, Batty 2015 (J R Soc Interface): read (Europe PMC full text). 8850 wards, rho0 in {1..40}, N0 cuts, >2x10^4 realizations, rho_c = 14, patents 10^4 vs 5x10^4, >1.8x10^5 with no patents, LUZ 21 cities all confirmed. ✎ "two-regime" corrected to the paper's "two-system theory of cities".
- ✓ Dunbar 1993 (BBS) unedited preprint: read. Eq. 1 (RMA, r^2 0.764, t34 10.35), 147.8 (100.2 to 231.1), 107.6 to 248.6, eq. 2 (r^2 0.589), 42% (28% to 66%), 56.6%, 2.76, 3.8 (3070 bookings), 3.4, Table 1 means, 179.6, Indik et al. all confirmed. ✎ Hutterite claim attributed to Hardin 1988 as cited by Dunbar.
- ✓ Zhou, Sornette, Hill, Dunbar 2005 (Proc R Soc B): checked against the arXiv preprint cond-mat/0403299 (the published PMC text was blocked). 61 sizes, S1..S6, ratios, omega1 = 5.40, lambda 3.20, 0.993/0.99/0.85, 0.024, 77/10000, 42 Christmas-card subjects, omega 5.2, "no obvious reason" all confirmed in the preprint.
- ✓ Lindenfors, Wartel, Lind 2021 (Biol Lett): read. All eight estimates and intervals, the 134.0 (7.0 to 583.2) supplementary estimate, and the conclusion sentence confirmed. Sample sizes are 71/126/142 data points per model.
- ✎ Kao and Couzin 2014 (Proc R Soc B): read in the published PDF (UMass Boston lab copy). p > 1/(2 r_L), 1/2 < p < 1/(2 r_L), eps < r - 1/2 (one third), accuracy g, 50%/18%/0%/31% confirmed. Corrected: "8/3" is the prefactor of an integral and the proportion is 0.076.
- ✎ Centola, Becker, Brackbill, Baronchelli 2018 (Science): read the CRO accepted manuscript, which includes the supplement. 194 subjects, 10 groups, N 20 to 30, 15% < C < 35%, 6%, 72% to 100%, 31%, P = .01, 9 <= M <= 13, 80%, 21%/25%, "not expected to be a universal value" confirmed. Corrected: 24.3% is the large-N limit, not the prediction at N = 24; the supplement says 24.2%; "marginally larger" refers to the committed group; consent and non-disclosure of confederates stated from the methods.
- ✎ Esteban and Ray 2001 (APSR): read in the author-site PDF. u = w - v(a), w = lambda P + (1 - lambda) M/N, theta, Propositions 1 and 2, quadratic-cost reversal confirmed. Corrected: eq. 12 form (pi_i/N_i, not 1/pi), and the Olson-survival statement (only the origin alpha = 0, lambda = 0 guarantees it).
- ✓ Isaac, Walker, Williams 1994 (J Public Econ): read in the UCSD-hosted PDF (abstract, intro, Observations 2 to 4, Fig. 9 text, conclusion). All claims confirmed. ✎ The Isaac and Walker 1988 MPCR claim is now sourced to the 1994 restatement; IW 1988 itself remains [sa].
- ? Olson 1965, Karau and Williams 1993, Latané, Williams and Harkins 1979, Latané 1981, Caplow 1957, Dunbar 1992: records confirmed at Crossref (Olson is a book; no DOI checked). Texts not opened. They remain in Unconfirmed, and nothing from them feeds an equation.
- ? Leitão et al. 2016 and Cottineau et al. 2017: added as pointers after a search for a reply to Arcaute. Records confirmed, texts not read.
- Searches for "nothing exists" claims: no direct Bettencourt reply to Arcaute found (one search); no replication of the 25% tipping fraction in another task found (one search). Both absences hold only as far as one search goes.

Sources opened by the validator: 9 primary texts (Bettencourt PDF, Arcaute, Dunbar preprint, Zhou arXiv, Lindenfors, Kao-Couzin PDF, Centola CRO, Esteban-Ray PDF, Isaac et al. PDF), plus 16 Crossref records.

Verdict: the note is accurate and honest in its provenance. Every work exists and is credited to the right authors, and no fabrication was found. The four substantive errors were all in exact mathematical statements: Esteban and Ray's eq. 12 and the conditions under which Olson's result survives, the Kao and Couzin "8/3", and Centola's 24.3% being read as the prediction at N = 24. These are now corrected. The three listed theorems (Bettencourt regimes, Esteban-Ray Propositions 1 and 2, Kao-Couzin conditions) are confirmed at source and may feed equations. Esteban-Ray eq. 12 should first be checked once against the page image.

## Cross-checks (2026-10-30)

Checked against the other prior-work files by grep for each author, work and key number (Bettencourt, Arcaute, Dunbar, Zhou, Lindenfors, Kao, Couzin, Centola, Esteban, Isaac, Olson, Karau, Latané, Ringelmann, Caplow, Condorcet, Granovetter, MPCR), then the matching passages read. No file was edited except this one. Nothing here resolves a contradiction.

**Agreements**
- Zhou et al. 2005, layer ratio near 3 with no mechanism: `09-biology-ecology.md` §E4 agrees. `083-composition-merge-split-nest-gap.md` §3.3 and its lines 329 and 353 cite §3b of this file and agree.
- Dunbar 1992 and 1993 DOIs, and the 150 figure as contested: `09` §E4 agrees with §3a and §3c. `09` gives the 1993 pages as 681-735 (with commentary); this file gives the target article as 681-694.
- Karau and Williams 1993 DOI, and the expectancy x instrumentality x valence rule: `24-collective-action-team-motivation.md` §7 agrees. `24` tags it [abs] and [std]; this file tags it [sa].
- Latané, Williams and Harkins 1979 and Latané 1981 DOIs: `24` §7 agrees.
- Olson's result holds for private prizes and reverses for public ones: `10-economics-politics-anthropology-linguistics.md` §2 (reversal when jointness of supply is high) agrees in direction with §6a.
- Dunbar's grooming time rising with group size: `31-ethology-signals-and-drives.md` agrees in form, with no coefficients.
- Granovetter-type threshold shape for Centola 2018: `05-influence-opinion-control.md` §12 and the threshold row in `29-animal-collective-behaviour.md` agree in form.

**No overlap**: Bettencourt et al. 2007, Arcaute et al. 2015, Isaac et al. 1994, Esteban and Ray 2001, and Kao and Couzin 2014 appear in no other file. `086` cross-refers to Kao and Couzin as a different paper. Centola-Macy 2007 and Centola 2010 (`05`) are different works from Centola et al. 2018.

**Contradictions, unresolved**
- Patent exponent. Bettencourt et al. 2007 gives 1.27, superlinear, for 331 US MSAs (§1). Arcaute et al. 2015 cannot reject linearity at minimum population 5x10^4 in England and Wales (§2). Scope differs; not settled.
- Human group size. Dunbar 1993 gives 147.8 (100.2 to 231.1) (§3a). Lindenfors et al. 2021 gives 69.2 (3.8 to 292.0) for the preferred model (§3c). Not settled.
- Olson. Larger groups do worse at collective goods, as quoted by Esteban and Ray and marked [sa] here (§6c). Esteban and Ray Proposition 1 and Isaac et al. Observation 3 (MPCR 0.30) point the other way under conditions. Scope differs (provision versus contest). Not settled.
- Centola 2018. The 10% competing-model prediction failed in one setting (§5). Not settled beyond that setting.
- Provenance only. `09` §E4 says Lindenfors 2021 was "not opened"; §3c of this file reads it in full. `09` is not edited here.
