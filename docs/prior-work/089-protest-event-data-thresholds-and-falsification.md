# Prior work 089: protest event data for threshold and preference-falsification models

Direction: D507 (kind: data). Date: 2026-10-29. Strand: social-algebra.

**Question.** Which protest event datasets (Crowd Counting Consortium, NAVCO, Mass Mobilization Project, Global Protest Tracker) could test Granovetter's threshold equation and Kuran's preference-falsification model, and what do the primary texts actually claim and show?

**Method and provenance (read this first).**

- **[read]** means I fetched the full text or file myself and read the passage cited. For this file that is:
  - Granovetter 1978: full text, from a scanned copy hosted on gwern.net (OCR text, `pdftotext`). Equations transcribed below are from that text. OCR dropped some symbols, so each was checked against the paper's own worked numbers.
  - Kuran 1989 ("Sparks and prairie fires", Public Choice 61:41-74): gwern.net copy (`gwern.net/doc/sociology/preference-falsification/1989-kuran.pdf`). The first pass read sections 1-3.5 and the opening of 4. **The validation pass (2026-10-30) read the abstract, sections 4.1-4.4, 5 (revolutionary potential, eq. 9 and Table 1), the opening of 6, the repression passage in the case discussion and the concluding paragraph.** The rest of sections 6-8 was not read in full. The paper has no appendix.
  - Chenoweth 2020 Carr Center brief on the 3.5% rule: read in full except the technical appendix. Open copy: `hks.harvard.edu/sites/default/files/2024-05/Erica%20Chenoweth_2020-005.pdf`.
  - Chenoweth & Belgioioso 2019 (Nature Human Behaviour): author copy (Harvard DASH; re-read in validation from the Brunel BURA copy, `bura.brunel.ac.uk/handle/2438/19075`). Read: abstract, hypothesis, data, models, results and methods text. The Table 2 coefficients and the SI were not read.
  - González-Bailón et al. 2011 (Scientific Reports): open PDF; abstract, results on thresholds, the discussion lines on bursts, and (in validation) the Methods paragraph on data. SI not read.
  - The Mass Mobilization codebook (Clark & Regan, May 2015): in full. NAVCO 2.0 codebook (2013): inclusion criteria and the variable table. CCC Phase 1 data dictionary: variable descriptions, first part.
- **[data]** means I downloaded the actual data file from Harvard Dataverse and counted rows or categories myself (CCC Phase 1; Mass Mobilization v16). I did not download the NAVCO tab file, the CCC Phase 2 and 3 files, or Phase 3 coding guidelines.
- **[meta]** means Dataverse API metadata (licence, files, dates), fetched directly.
- **[sa]** means not read at source. **Kuran 1991 ("Now Out of Never", World Politics 44:7-48; the named seed) is paywalled and NOT read.** I read only its abstract through the Crossref record. Everything about it beyond that abstract is [sa]. The model I report as "Kuran" is the 1989 paper, an earlier text by the same author on the same private/public-preference framework (it says its own model comes from Kuran 1987a, 1987b). I have not verified that the 1991 paper uses the same equations, and it may differ. Nothing [sa] feeds an equation here.
- Global Protest Tracker was read only through a summarising fetch of its landing page, not downloaded. Claims about it are marked [web page, via summariser].
- DOIs confirmed with Crossref: Granovetter 10.1086/226707; Kuran 1991 10.2307/2010422; Kuran 1989 10.1007/BF00116762 (title, author, Public Choice 61(1):41-74 re-checked against Crossref in validation); Lohmann 1994 10.2307/2950679 (World Politics 47(1):42-101, added in validation); González-Bailón 10.1038/srep00197; Chenoweth & Belgioioso 10.1038/s41562-019-0665-8; Enikolopov, Makarin & Petrova 10.3982/ECTA14281. The first guess at the Chenoweth & Belgioioso DOI (`...0661-1`) returned nothing from Crossref and was dropped; the `...0665-8` form is the one confirmed.

Cross-references: file 24 (collective action and team motivation), 18 (group drives and collective emotion), 23 (collective dynamics of motivated agents), 79 (identifiability and power for drive equations).

**Headline.** The datasets here record **events and aggregate sizes**, not individuals' thresholds, drives or private preferences. Granovetter's equation needs the distribution F of individual thresholds. Kuran's needs private preferences, which are hidden while falsification is active (indirect aggregate measures exist; see section 5). Neither can be fitted directly to any of the four sources. What the data can do is test **aggregate consequences** (momentum, peak participation, defections, cascades of event counts). Those tests exist and are weak or post hoc. Details below.

---

## 1. Granovetter 1978, "Threshold Models of Collective Behavior"

**Citation.** Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology* 83(6): 1420-1443. DOI 10.1086/226707 (Crossref confirmed). **[read, full text]**

**Their vocabulary.** "Threshold": "the number or proportion of others who must make one decision before a given actor does so; this is the point where net benefits begin to exceed net costs for that particular actor." Instigators (threshold 0), radicals, conservatives, "bandwagon" or "domino" effect, "equilibrium", "reverse bandwagon", "pluralistic ignorance".

**Drives/operands.** The operand is an actor with one number, a threshold x. Granovetter says thresholds are "purely behavioral" and "connote nothing about what the actor thinks is the 'right' thing to do". They are "the result of some (possibly complex) combination of costs and benefits", e.g. cost of arrest, benefit of rioting, status loss from reluctance (Matza's delinquent boys). He explicitly **leaves out where preferences come from**: "they do not consider how individuals happen to have the preferences they do."

**Operators / equations [read].**
- Threshold density f(x), c.d.f. F(x) (proportion with threshold <= x); r(t) is the proportion who have joined by t.
- Dynamics: **r(t+1) = F[r(t)]** (his words: "exactly that proportion of the crowd whose thresholds are less than or equal to" r(t)).
- Equilibrium: set r(t+1) = r(t); the equilibrium r_e is where F first crosses the 45 degree line from above, **F(r_e) = r_e**. With no removal of participants, oscillation is impossible and an equilibrium is always reached.
- Worked case, n = 100: thresholds 0,1,2,...,99 (uniform) gives equilibrium 100. Replace the threshold-1 person by a second threshold-2 person: equilibrium 1. Granovetter's point: the two crowds are "essentially identical" on mean and spread, but the outcome differs totally.
- Normal thresholds, mean 25, n = 100: as the standard deviation sigma rises, equilibrium rises slowly to about 6, then at **sigma_c approximately 12.2 jumps to nearly 100**, then declines (limit 50 as sigma goes to infinity). Cause: the normal c.d.f. meets the 45 degree line three, two or one times; at sigma_c two crossings merge.
- Social structure: friends count with weight w. Example: threshold 50%, crowd 100, 48 rioting; with 20 acquaintances of whom 15 riot, friends weighted 2, perceived proportion = 63/120 = 0.525 > 0.5, so he joins although the raw count is 48/100. Needs a sociomatrix plus weights; "attempts to derive these distributions analytically have failed, yielding only unmanageable convolutions"; results by simulation (Danforth).
- **Credit within the paper [read, footnotes].** Granovetter names three co-workers: Christopher Winship for the difference-equation analysis and fig. 1 (fn. 4); Bob Phillips for the normal-distribution analysis behind sigma_c (fn. 6 on p. 1425); Douglas Danforth for the social-structure results and all the computer simulations (fn. 6 on p. 1430). The paper is single-authored; these are his attributions.
- Sampling variability (crowd of 100 drawn from a large population with uniform thresholds, 1% at each value): P(no instigator) = 0.99^100 = 0.37; P(exactly one instigator and no threshold-1 person) approximately 0.14; so 0.51 of crowds end with 0 or 1 rioter. With p = 0.10 per incident of a large riot, P(no large riot in 10 incidents) = 0.9^10 = 0.35.
- Net-benefit curve must cross zero **once** (single-crossing). A curve crossing twice (restaurant too empty or too full) breaks the model; equilibria are then "not guaranteed".

**Theorems or derived predictions [read].** No formal theorems. Derived results: (a) F(r) = r fixed points; (b) outcomes are hypersensitive to the exact distribution, so mean preference does not predict outcome; (c) an equilibrium can be stable (a one-rioter equilibrium survived social-structure perturbations, "rarely exceeds five to 10 rioters") or highly unstable (the full uniform, whose modal result under most friendship structures is one rioter).

**Empirical standing.**
- Granovetter's own paper presents no fit to data. The measurement section says thresholds "are difficult to measure with confidence before the behavior actually occurs" and that the threshold distribution can be inferred from adoption order, "a tautological procedure".
- One test is reported, **second-hand within the paper [read as reported, original not read]**: Dozier (1977), 23 rural Korean villages, month of first adoption of family planning 1964-73, each woman's threshold regressed on covariates in 18 villages, then used in 5 held-out villages. Granovetter's summary: when the regression explained under 50% of threshold variance, predictions were worse than ordinary regression; above 50% "the accuracy of the recursion model improves dramatically", with many predictions "approach[ing] 100% accuracy". He cautions that some regressors "could not have been measured before the time period" and may leak. n = 5 villages out of sample. This is the only out-of-sample number in the paper; Dozier is not read.
- Spilerman's riot data (1961-68) is used as a plausibility illustration for the sampling-variability argument, not a test.
- Other empirical work, unverified here [sa]: Lohmann 1994 (Leipzig Monday demonstrations), Enikolopov et al. 2020 (VK and Russian protests, Econometrica). Not read.

**Operand/operator translation.** Operand: a person with threshold x in [0, 1] (or an absolute count). Operator: the map F on the group's current joined proportion, iterated. The group-level object is the **distribution** F; it is not a function of any one person's drives. Composition: iteration of F (a monotone map), fixed points, and perturbation of F (remove or insert a person, add friend weights).

**What changes with group size n and composition.**
- Granovetter says thresholds "may usefully be described as either proportions or absolute numbers"; the analysis is identical. All worked examples use n = 100.
- **Sample size is itself a source of variance**: small crowds drawn from a fixed distribution have outcomes dominated by whether specific gap-filling people are present. The riot-outcome variance is a function of n and F, and he uses it to explain why larger black populations (more incidents) produced more riots in Spilerman's data.
- Composition = the exact shape of F (gaps, shape, tails), not its mean. Friend density has its largest effect when people know about a quarter of the group (simulation, not explained).
- He flags that the complete-connection assumption fails for large, dispersed events (the 1965 Watts riot as 1,850 separate cases of riot action) and moves to spatial clusters with movement between them.

**Scale of the result.** Theoretical; the illustrations are crowd-scale (riot, adoption in a village). **Consent/manipulation:** the model has no intervention operator. Implicit levers are removal or addition of one person and changes to ties, i.e. an instigator or a gap-filler. Whether that is manipulation or consent is not discussed.

---

## 2. Kuran, preference falsification and the revolutionary threshold

**Citations.**
- Kuran, T. (1989). Sparks and prairie fires: a theory of unanticipated political revolution. *Public Choice* 61(1): 41-74. DOI 10.1007/BF00116762 (Crossref confirmed). **[read, sections 1-5, opening of 6, conclusion; rest of 6-8 not read in full]**
- Kuran, T. (1991). Now out of never: the element of surprise in the East European revolution of 1989. *World Politics* 44(1): 7-48. DOI 10.2307/2010422. **[NOT read; paywalled; only the Crossref abstract read.]**

**Their vocabulary [read, 1989].** Private preference x^i, public preference y^i, "preference falsification", "collective sentiment" Y, "reputational utility", "integrity" utility, "threshold function", "bandwagon", "activists" vs "non-activists", "unanticipated revolution". The 1991 abstract (read via Crossref) says the same distinction between private and public preferences explains why the East European revolution of 1989 surprised everyone, and "political revolutions will inevitably continue to catch the world by surprise".

**Drives/operands [read, 1989].** Society [0,1] on one dimension, two parties (0 governs, 1 opposes). N non-activist individuals, each with exogenous private preference x^i and a weight w^i (weights sum to 1). Two motives explicitly named: **reputational utility** (rewards and punishments for the political stance one declares, plus a benefit rising with party share, "camaraderie, social support, and a sense of importance") and **integrity** (a cost of compromising one's own view). The author says each person's influence on the social order is negligible, so utility from the order itself is dropped.

**Operators / equations [read, 1989; numbering is the paper's].**
- (1) Collective sentiment: Y = sum over i of w^i y^i, weights sum to 1.
- (2) V^i(y^i | x^i) = R(y^i) + N(y^i | x^i).
- (3) R(y^i) = f(s) if y^i = 0; 0 if 0 < y^i < 1; F(S) if y^i = 1, with f(0) > 0, F(0) > 0, df/ds > 0, dF/dS > 0 (s and S are the weighted shares publicly supporting government and opposition).
- (4) N(y^i | x^i) = N(1 - |x^i - y^i|), increasing in its argument; the falsification cost is N(1) - N(1 - |x^i - y^i|).
- (5) Expected shares: s^e + S^e = 1.
- (6) V^i(0 | x^i) = f(1 - S^e) + N(1 - x^i); (7) V^i(1 | x^i) = F(S^e) + N(x^i).
- Threshold function x(S^e): the private preference that makes a person indifferent between 0 and 1; it declines as expected opposition share S^e rises.
- (8) Equilibrium: **S = g(x(S^e))**, where g is the cumulative weighted density of private preferences. Equilibria are where this crosses S = S^e; multiple crossings give multiple equilibria.
- Simplifications the paper imposes: common point expectations, common reputation and integrity functions, and the "independent" option y^i = x^i always dominated.

**Theorems or derived predictions [read, 1989; validation pass].** A single crossing gives a unique stable equilibrium (Fig. 2). New equilibria arise when g or x shifts; the paper's example of a g shift is an economic downturn that makes groups feel relatively deprived (sec. 4.1). A "revolution" is defined as a sudden shift in collective sentiment of more than 0.5 units (sec. 4.2). Section 4.3 states three results, which are the paper's core comparative statics:
  1. A jump in the expected share S^e can **precipitate** a revolution, but only if the stage is already set (an alternative stable equilibrium exists). In Fig. 2 "no expectational jump could start a revolution, however large".
  2. A leftward shift of the threshold function x(S^e) (opposition better at delivering reputational utility, upward F(S) or downward f(s)) can both **set the stage and precipitate**.
  3. An upward shift of the private-preference density g **can set the stage but cannot precipitate** a revolution by itself (Fig. 6: 20% privately at 1, yet S^e = 0 stays an equilibrium). Hence the quoted Narodnaya Volya line, "No village has ever revolted merely because it was hungry".
- (9) **Revolutionary potential** (sec. 5): S* = [d(S^-, S^+) - d(S^-, S^-+)] / D(S), with S^- the status quo, S^+ the alternative stable equilibrium, S^-+ the unstable one between them, D(S) the largest possible jump; range 0 <= S* < 1. Table 1 gives S* = 0, 0.3, 0.8, 0, 0.85, 0.75 for Figs. 2-7 (e.g. Fig. 4: (1 - 0.2)/1 = 0.8). Defined only for cases with at most two stable equilibria.
- The "small shock, bandwagon" story is now read in sec. 6 (opening): a relatively minor event pushes a few to their "boiling point", which "kicks off the latent revolutionary bandwagon".
- **Those who privately prefer the regime most stay longest, because their falsification cost is greatest** (stated in sec. 3, about the Shah's supporters). This is a prediction about ordering of defection by private preference.

**Empirical standing.** Section 2 of the 1989 paper is case evidence (French 1789, Russian 1917, Iran 1978-79) that prediction failed, by quoting contemporaries, not a test of equations (2)-(8). No estimation of x, g or f/F. The case discussion reads France and Iran as a **lessening of repression**, which "in our model shifts the threshold function leftward" (Louis XVI's men had "lost the will to repress"; the Shah's response to Carter's human-rights campaign). The 1991 paper's data are historical (1989) and unread. The rival-measure problem is the key one: **private preferences x are hard to observe while falsification is active**, so g cannot be read off public behaviour. Kuran himself (1989 conclusion) points to Noelle-Neumann's Allensbach work on measuring private preferences and says it "may soon be possible to track the revolutionary potential of a society", while warning that "social predictions interact with the phenomena they predict". Later measurement attempts exist (see section 5, corrected). There are no replications of the model as a model in what I read.

**Operand/operator translation.** Operands: individual with (x^i, w^i); the regime as a leader-fixed party. Operators: declare y in {0,1}; aggregate by weighted sum; fixed-point equation (8). It has the same structure as Granovetter's (iterated monotone map, fixed points) but the threshold is **derived** from two named motives (reputation versus integrity), so it is a rare case in this literature where the threshold has a stated utility form.

**What changes with n and composition.** n enters only through the weights (each w^i very small); because Y is a weighted average, "it is possible for a revolution to be carried out by a small, but influential, share of the population" (sec. 4.2). Composition is g (distribution of private preferences) and the heterogeneity-free assumption on f, F, N. *Corrected in validation:* the first pass said the paper stresses the distribution tail. What the paper actually states is result 3 above: composition (g) alone cannot precipitate; it matters through whether g and x(S^e) have an alternative crossing. Nothing on n in the text read.

**Scale.** Society-wide: a nation's population reduced to one dimension (opposition share). **Consent/manipulation:** the 1989 paper (what I read) says leaders "expose" vulnerability and that regimes repress and indoctrinate; repression is treated as raising the cost of declaring (the f function reflects "selective incentives available to the two parties"), i.e. state coercion is a modelled lever. Whether protest organisers manipulate or inform is not analysed in the part I read.

---

## 3. Datasets (the core of D507)

None of these has individual thresholds. The usable quantities are the ones below. Licence, access and dates are from the Dataverse API [meta] unless marked.

### 3.1 Crowd Counting Consortium (CCC), U.S. protest events

- **Credit [meta]:** Dataverse authors: Phase 1, Erica Chenoweth, Jeremy Pressman and Jay Ulfelder; Phase 2 adds Soha Hammam; Phase 3 adds Christopher Shay. Phase 1 collection drew on Count Love's web crawl (data dictionary).
- **Access:** Harvard Dataverse, `https://dataverse.harvard.edu/dataverse/crowdcountingconsortium/`. Three datasets by phase: 2017-2020 (doi:10.7910/DVN/6OPP7H, `ccc_compiled_20172020.tab`, 36.6 MB, v1, released 2025-10-16), 2021-2024 (doi:10.7910/DVN/9MMYDI, v2, 128 MB), 2025- (doi:10.7910/DVN/RI9JFU, `ccc-phase3-public.csv` 47 MB, **monthly updates**, v18 as of 2026-09-10). **Licence: CC0 1.0** on all three [meta]. Project page: ash.harvard.edu/programs/crowd-counting-consortium/ [fetched via summariser; page states no licence, Dataverse does].
- **Variables [read, data dictionary Phase 1]:** date, locality, state, location_detail, online, type (march, strike, sit-in, counter-protest etc.), macroevent (links a counter-protest to the protest it countered; only retro-filled for the 2020 BLM wave in Phase 1), actors, claims (free text), valence (2 pro-Trump, 1 anti-Trump, 0 other), issues (regex tags), size_text, size_low, size_high, size_mean, **size_cat** (0 unknown; 1 = 1-99; 2 = 100-999; 3 = 1,000-9,999; 4 = 10,000+), arrests, injuries (crowd, police), property_damage, chemical_agents (May-Dec 2020 only), sources, lat/lon (locality centroid only).
- **Size coding [read]:** vague counts converted by rule: "hundreds" becomes 200, "thousands" 2,000, "several" = 3; fudge words ignored. So sizes are orders of magnitude, not counts.
- **Sample [data, my count; recounted in validation]:** Phase 1 has **72,181 events**, dates 2017-01-01 to 2020-12-31. size_cat counts: 0 (unknown) 36,108 (50.0%); 1 = 16,848; 2 = 16,288; 3 = 2,654; 4 = 283. The validation recount (Python csv parser, quoted fields) gives 36,110 (incl. three stored as "0.0") / 16,847 / 16,287 / 2,654 / 283: same total, one or two rows differ by parser. Half of events have no size either way.
- **Collection [read]:** news-crawl of 3,400+ outlets via Count Love from April 2017, plus non-systematic social media; includes reports of upcoming events as well as ex post coverage. Coverage depends on being reported.
- **What it could test:** (i) Chenoweth-Belgioioso "velocity": events per week in a country is directly buildable; "mass" (participants per thousand of population) is only order-of-magnitude. (ii) Counter-protest pairs via macroevent: a rare two-sided mobilisation record, limited to 2020 in Phase 1. (iii) A cascade-size distribution across localities (Granovetter's spatial clusters). **It cannot test:** F(r), because there is no defined group whose joined proportion r(t) can be computed, and no leader-exit or regime-outcome variable (U.S. only).

### 3.2 Mass Mobilization Project (MM)

- **Credit:** David H. Clark (Binghamton) and Patrick M. Regan (Notre Dame), authors of the dataset and the May 2015 codebook.
- **Access:** `https://dataverse.harvard.edu/dataverse/MMdata`; dataset doi:10.7910/DVN/HTTWYL, "Mass Mobilization Protest Data", v5, last published 2022-10-10; files `mmALL_073120_csv.tab`, `mmALL_073120_v16.tab`, `MM_users_manual_0515.pdf`. **Licence: CC0 1.0** [meta]. Dataset description: "protests against governments, all countries, 1990-2020".
- **Definition [read, users' manual May 2015]:** a protest is a gathering of **50 or more people** making a demand of the government; anti-state only. It excludes inter-communal protest, rebel attacks and political rallies tied to elections. Search: Lexis-Nexis for protest/demonstration/riot/mass mobilization in NYT, Washington Post, CSM, Times of London (plus Jerusalem Post for MENA), widened to regional sources if fewer than 100 articles. So **selection is by four anglophone Western papers**.
- **Variables [read]:** country, year, region, start and end date, protester violence (binary), location, number of participants, categorical participation (50-99; 100-999; 1,000-1,999; 2,000-4,999; 5,000-10,000; >10,000), protester identity, up to 4 demands from 7 classes (labour/wage; land/farm; police brutality; political behaviour/processes; price/tax; removal of corrupt person; social restrictions), up to 7 state responses (accommodation, arrests, beatings, crowd dispersal, ignore, killings, shootings), sources, notes. Count rule: "the lower of any estimate at one point in time" but the maximum over a multi-day protest.
- **Sample [data, recounted in validation from the v16 file]:** *Corrected:* the file has **17,145 rows, not 17,145 events.** `protest` is a dichotomous flag (manual: "whether or not there was a protest action in a particular period"), and 1,906 rows are country-periods with protest = 0. **Protest events (protest = 1): 15,239, 166 countries, 1990-2020.** Among events, the categorical participation field is blank for **5,352 (35.1%)**; the first pass's 7,258 (42%) counted the no-protest rows too. Raw `participants` is free text; among events the most common values are "100s" (1,330), "1000s" (1,187), "50+" (1,138), "50" (1,005), "1000" (978), ">50" (936); only 12 events have it blank (the first pass's "blank (1,399)" was mostly no-protest rows). The manual says the categorical indicator was "added part way through coding, not available for all cases".
- **What it could test:** (i) whether accommodation, repression or ignoring in one period predicts mobilisation next period (backfire; see Kuran on repression raising the cost of declaring); (ii) regional wave structure across countries (aggregate cascade); (iii) demand types as a crude proxy for the grievance side of x. **It cannot test** Granovetter's F directly. The lower bound of 50 people truncates the entry level where instigators (threshold 0) would show.

### 3.3 NAVCO (Chenoweth et al.)

- **Access:** NAVCO Data Project on Harvard Dataverse (search of the dataverse API returned 15 datasets). Versions seen [meta]: NAVCO 1.1 (doi:10.7910/DVN/YLLHEE, 323 campaigns 1900-2006, archival), NAVCO 1.2 (doi:10.7910/DVN/0UZOTX), **NAVCO 2.0** (doi:10.7910/DVN/PLXAFY, 250 campaigns 1945-2006, campaign-year; 7 files), NAVCO 2.1 (doi:10.7910/DVN/MHOXDV; "supersedes" 2.0), NAVCO 3.0 (doi:10.7910/DVN/INNYEO; version contents not read), also "Major Episodes of Contention" (doi:10.7910/DVN/JQWQNW, released 2026-06-06, not read) and "External Support for Nonviolent Campaigns" (EX-D). **Licence: CC0 1.0** on 1.1, 1.2, 2.0, 2.1, 3.0 and Major Episodes (re-checked in validation) [meta]. Chenoweth's brief says NAVCO 1.2 (Nov 2019, with Christopher Shay) covers **1945 through 2014** (it does not start in 1900 as 1.1 does).
- **Credit [meta, Dataverse authors]:** NAVCO 1.1, Erica Chenoweth; 1.2 and 2.1, Chenoweth and Christopher Wiley Shay; **2.0, Chenoweth and Orion A. Lewis**; 3.0, Chenoweth, Jonathan Pinckney and Orion A. Lewis; Major Episodes of Contention, Chenoweth and Sooyeon Kang. NAVCO 1.x was built for Chenoweth & Stephan (2011), *Why Civil Resistance Works* (per the brief).
- **Inclusion [read, NAVCO 2.0 codebook]:** "maximalist" campaigns (regime overthrow, end of foreign occupation, self-determination), "mature" with **at least 1,000 observed participants** and a coherent organisation. The codebook admits that "unknown, failed, nonviolent campaigns are necessarily omitted", that the sample is a "consensus population", and that there is "real concern that the campaigns included are biased toward success".
- **Variables [read, 2.0 variable table]:** campaign-year; cyear (onset/ongoing/end/post); prim_method (violent or nonviolent); **camp_size** (0 = 1-999; 1 = 1,000-9,999; 2 = 10,000-99,999; 3 = 100,000-499,999; 4 = 500,000-1 million; 5 = >1 million); camp_orgs (new named organisations that year); camp_conf_intensity (unity, 0-3); rad_flank; nine diversity flags (gender, age, class, urban-rural, ideology, party, region, ethnicity, religion); camp_goals; camp_structure (consensus vs hierarchical); media_outreach; **repression** (0-3) and **discrim** (discriminate vs indiscriminate); parallel-institution flags; **camp_backlash** (1 suppressed; 2 decreased mobilisation; 3 increased mobilisation); **sec_defect** and **state_defect** (security-force and civilian-official defections); regime/campaign external support flags.
- **What it could test:** the defection mechanism that Chenoweth's brief names and links to Kuran and Lohmann: does a step in camp_size precede sec_defect or state_defect in the next campaign-year? That is a coarse test of "a visible majority tips elites". Also backlash versus repression. Annual resolution is far coarser than a day-scale cascade. n is about 250 campaigns, with selection toward large and successful ones.

### 3.4 Global Protest Tracker (Carnegie)

- **[web page; validation pass downloaded the raw HTML (2.6 MB) and searched all of it.]** Covers "the most significant antigovernment protests worldwide since 2017". On the day fetched the page showed 107 significant protests in the last 12 months in 57+ countries and 33 active; "last updated on September 9, 2026". *Corrected:* the first pass (summariser, first fifth of the page) said there was no size field. The full page has a sortable table of **1,054 results** with columns **Start Date, Peak Size** (e.g. "<150"; filter bins Tens / Hundreds / Thousands / Tens of thousands / Hundreds of thousands / Millions), **Motivation, Duration, Violence**, plus trigger, motivation and demand text, and filters by year and Freedom House-style political status (Free / Partly Free / Not Free). **No stated numeric inclusion threshold** and **no data-download link** found in the HTML (searched for csv, xlsx, download, methodology); "© 2026 Carnegie Endowment for International Peace. All rights reserved." So it is a coded episode list with order-of-magnitude peak size and duration, usable for descriptive checks only, with no reuse licence.

### 3.5 Datasets not in the seed list but used by the primary texts

- **SCAD (Social Conflict Analysis Database) + ARCHIGOS**, used by Chenoweth & Belgioioso [read in the paper]: country-day panel for Africa 1990-2014, more than 295,000 country-days, 45 irregular leader exits (24 in the strict version).
- **Spanish 15-M Twitter data**, González-Bailón et al.: 87,569 users, 581,750 protest messages, 30 days (25 April to 25 May 2011). Access to the data was not checked.

**Equation-to-data map.**

| Equation | Needed quantity | Nearest dataset variable | Gap |
|---|---|---|---|
| Granovetter r(t+1) = F[r(t)] | r(t): joined proportion of a defined group; individual thresholds | CCC size_cat/date; MM participants_category; none per person | No defined group, no person-level thresholds, order-of-magnitude sizes |
| Kuran S* (eq. 9) | S^-, S^-+, S^+ (equilibria of g and x) | none | Needs g and x(S^e), so needs private preferences |
| Kuran S = g(x(S^e)) | private preference x, expected share S^e | MM demands; NAVCO diversity flags (not x) | x hidden under falsification; no event dataset measures it |
| Momentum p = m*v | participants per thousand; events per week | CCC (US), SCAD (Africa) | Mass is coarse; outcome (leader exit) absent from CCC and MM |
| 3.5% rule | peak participation / population; success | NAVCO camp_size, outcome | Peak size is a category; measured at or near the outcome |
| Defection cascade | size step then sec_defect | NAVCO annual | Annual resolution; n about 250 |

---

## 4. Chenoweth 2020 and Chenoweth & Belgioioso 2019: the empirical claims actually made

### 4.1 The 3.5% rule (Chenoweth 2020, Carr Center)

**Citation.** Chenoweth, E. (2020). *Questions, Answers, and Some Cautionary Updates Regarding the 3.5% Rule.* Carr Center Discussion Paper 2020-005, Harvard Kennedy School. **[read]**

**Claim as stated [read].** "no government has withstood a challenge of 3.5% of their population mobilized against it during a peak event." Derivation: peak observed participants divided by the country population "during the final year of the campaign", in NAVCO 1.1 (323 campaigns, 1900-2006). "All movements that had at least 3.5% peak popular participation had succeeded. Moreover, all campaigns surpassing this threshold were primarily nonviolent." Peak is "usually either mass demonstrations in the case of nonviolent campaigns, or the maximum total fighters in the case of armed campaigns". Origin: Mark Lichbach (1995, *The Rebel's Dilemma*) had speculated, in a footnote, a 5% figure; Chenoweth first presented 3.5% at TEDxBoulder, September 2013.

**Her own caveats [read].** The figure is "a descriptive statistic based on a sample of historical movements"; "a rule of thumb ... not an iron law"; rule applies to **maximalist** campaigns (overthrow or territorial independence), not reform. Peak, not cumulative, participation. "No one knows whether the rule will hold if people consciously try to mobilize to achieve the threshold." The brief says "there is no way to calculate how much popular support is needed for a movement to succeed without comprehensive opinion polling".

**Exceptions [read].** NAVCO 1.2: Brunei 1962 (4,000 participants, 4% of population, an armed revolt, 10 days) and, post-2006, Bahrain 2011-14 (100,000 people, over 6%, failed). She attributes both to "small monarchies with access to overwhelming foreign military reinforcement" and says participation was short-lived.

**Table reproduced from the brief [read], success rate by peak popular participation.** *Corrected in validation:* the brief does state the base. The figure beside the table is sourced "NAVCO 1.2 (Chenoweth & Shay 2019)", and footnote 13 says "One violent campaign in Brunei brings the total number of campaigns surpassing 3.5% peak popular participation to 18. That's about 4.6% of the total of 389 maximalist campaigns from 1945-2013." So the table is **all 389 maximalist campaigns, violent and nonviolent, NAVCO 1.2, 1945-2013**:

| Peak participation | Obs. | Success rate |
|---|---|---|
| at least 3.5% | 18 | 88.89% (16 of 18) |
| 1% to 3.5% | 41 | 60.98% |
| 0.25% to 1% | 92 | 45.65% |
| 0.06% to 0.25% | 95 | 45.25% |
| 0.015% to 0.06% | 66 | 24.24% |
| 0.0035% to 0.015% | 44 | 9.09% |
| below 0.0035% | 24 | 4.17% |
| missing | 9 | 33.33% |

Significance "p<.003" (test not stated in the brief). Total 389 observations (the rows sum to 389). She also states that "Among all maximalist nonviolent campaigns that did succeed, 83% did so without crossing the 3.5% threshold." **The rule has a perfect record in NAVCO 1.1; in NAVCO 1.2 it is 16 of 18.** Reconciled in validation: 88.89% of 18 is exactly 2 non-successes, and the brief names exactly two exceptions, Brunei 1962 (violent, mistakenly excluded from NAVCO 1.1, coded not successful) and Bahrain 2011-14. That the two table failures *are* these two is my inference from the count, not a statement in the brief. The 88.89% is therefore the NAVCO 1.2 update of the NAVCO 1.1 "all succeeded".

**My caution (not in the brief).** Peak participation is measured "during the final year of the campaign" / at the peak event, which is close in time to the outcome. A campaign that is winning attracts more people, so size and success share a common time-ordered cause. The brief does not address this and the table cannot separate it. That is my inference from the construction described, not a finding in the text.

**Scale and consent/manipulation.** Scale: **crowd/mobilisation, national** (peak event size over national population), with a regime-level outcome. The mechanisms she names (disruption, public sympathy, elite defections via cascade, citing Kuran 1991 and Lohmann 1994) are stated, not tested in this brief. The movements are nonviolent civil resistance, so the lever (mobilise, sustain) works by **voluntary participation**; however the rule is explicitly descriptive and untested as a target.

**Out-of-sample.** None as a prediction made before the data. The rule was found in NAVCO 1.1 after the fact; Bahrain 2011-14 is the main new case since and it is a failure, which she says makes it "a tendency, rather than a law".

### 4.2 Momentum, p = m*v (Chenoweth & Belgioioso 2019)

**Citation.** Chenoweth, E. & Belgioioso, M. (2019). The physics of dissent and the effects of movement momentum. *Nature Human Behaviour* 3(10): 1088-1095. DOI 10.1038/s41562-019-0665-8 (Crossref confirmed). Chenoweth at Harvard Kennedy School, Belgioioso at Brunel University London. **[read, main text and methods from the author copy]**

**Equation [read].** momentum = mass x velocity, p = mv, where **mass** = participants per thousand population (from the SCAD "npart" variable, ranges 0 to 132.634 per thousand, i.e. up to 13.3%; mean 0.165) and **velocity** = number of nonviolent dissent events in the seven days preceding the current country-day (0 to 189). The "interaction term" multiplies them for the current day, and a version multiplies the logs. The outcome is **irregular leader exit** on a country-day. *Added in validation:* SCAD's npart is a **seven-point ordinal scale** (<10; 10-100; 101-1,000; 1,001-10,000; 10,001-100,000; 100,001-1,000,000; >1,000,000); the authors set the end categories to 9 and 1,000,001 and use interval midpoints otherwise, so "mass" is itself an order-of-magnitude quantity. "Nonviolent" events include riots in the main measure.

**Data [read].** SCAD plus ARCHIGOS, African country-days 1990-2014, over 295,000 observations; **45** irregular exits, strict measure **24** (peaceful context, dissidents had called for the leader to step down in the prior three months). Rare-event logit, 8 model specifications; momentum "generally positive and significant"; not significant when riots are excluded (Models 2 and 7). Predicted probability "more than triples from the minimum to the maximum values", but absolute probabilities "fairly modest". At or below the median velocity (28 events a week) no level of mass raised the probability. Maximum participation seen: 13.3% of population (so a 25% tipping point from earlier experiments "moot" in this sample). *Corrected in validation (the first pass inverted this):* the paper says that **below** the 75th percentile of mass (0.138% of population) and the median velocity, "the probability of irregular leader exit on any given day remains low". At the highest mass (about 13.26%) it "surpasses 60% at the highest levels of velocity" (Fig. 2, Model 6, logged mass), and at the highest participation rates the probability starts rising at about 40 events a week. Main-text results use the strict 24 exits; the SI reports the 45-exit measure as consistent.

**Empirical standing, bluntly.** Positive in-sample association with 24 strict events. The rare-event design, the co-timed definition of the outcome ("conservative assumption that a protest occurs on the same day as the leader departs") and the dependence on riots mean this is suggestive, not a validated predictor. No out-of-sample forecast was reported in the text I read. Region: Africa only. Scale: **crowd to regime outcome**, country-day. Group size: mass is normalised by population and total (logged) population is a control, because "states with larger populations tend to have higher likelihoods of political instability". Consent/manipulation: observational; no intervention.

### 4.3 Online recruitment thresholds (González-Bailón et al. 2011)

**Citation.** González-Bailón, S., Borge-Holthoefer, J., Rivero, A. & Moreno, Y. (2011). The dynamics of protest recruitment through an online network. *Scientific Reports* 1: 197. DOI 10.1038/srep00197 (Crossref confirmed). **[read, abstract, results, discussion and Methods data paragraph]** Methods: protest messages were identified with a list of 70 hashtags (list in SI); "active" = first sent such a message.

**Operationalisation [read].** Threshold of user = k_a / k_in, the proportion of followed accounts already active when the user first posts. "Activists with an intrinsic willingness to participate have a threshold ... 0"; those who need much pressure approach 1. Data: Spain, May 2011 (15-M), Twitter, 87,569 users, 581,750 messages, 30 days; **98.03%** had posted by the end. **Result:** the empirical threshold distribution is "roughly uniform for almost the full threshold interval", with local maxima at 0 (seeds) and 0.5. Early participants have lower thresholds. Moderate- (0.2-0.5) and high-threshold (>0.5) users are more likely to join after a "burst" of activations among neighbours; early participants (<0.2) are insensitive to bursts (Fig. 3A). Removing broadcasters (symmetric network) raises the count of zero-threshold early participants by an order of magnitude, i.e. the measured F depends on which network is taken as "the group". Early participants have no typical network position, but spreaders are more central.

**What it does and does not show.** It gives the first real empirical F for a protest, but **the threshold is defined from the activation order itself**, which is exactly the "tautological" index Granovetter warns about. It does not show that the exposure *caused* joining versus common exposure to news; the authors note that media coverage did not appear to raise low-threshold activation. The behaviour is posting a protest message, not marching. Scale: **online network, 87,569 users**, a nation-wide movement seen through one platform. Consent/manipulation: observational.

---

## 5. What exists versus what does not

**Exists.**
- Exact, readable statements of Granovetter's map r(t+1) = F[r(t)] and Kuran's fixed-point model; both are the same mathematical shape (monotone map on a joined share, fixed points, sensitivity to the distribution).
- Open (CC0) event data: CCC (US, 72,181 events in 2017-2020 alone, plus later phases), Mass Mobilization (15,239 events in 17,145 rows, 166 countries, 1990-2020), NAVCO (about 250 to 323 campaigns). All are documented, downloadable and free to reuse.
- One real empirical threshold distribution for a protest (González-Bailón), one aggregate regularity (3.5%, with a 16-of-18 record and two named exceptions), one momentum regression (24 strict events).
- A working record of what each dataset omits: size categories, selection by English-language papers, success bias.

**Does not exist (in what I read).**
- A dataset of individuals' conditional joining decisions at street level from which a full F could be estimated; so no direct estimate of F for a physical protest. (Not "nothing at the individual level": see the Cantoni et al. item below.)
- Any out-of-sample forecast of a protest outcome from these models (not tested by a search in validation; stated for the works read).
- *Corrected in validation; the first pass listed these as non-existent, and a search found both.* **[sa, abstracts only; not read; nothing here may feed an equation]**
  - **Measurement of preference falsification exists.** Jiang, J. & Yang, D. L. (2016). Lying or believing? Measuring preference falsification from a political purge in China. *Comparative Political Studies* 49: 600-634. DOI 10.1177/0010414015626450 (Crossref confirmed). Abstract (via Crossref): "the first quantitative study of this phenomenon in a non-democratic setting"; after the 2006 Shanghai purge, expressed support rose while a synthetic measure of actual support fell. So "private preferences unobservable by construction" is too strong: they are hard to observe, and indirect designs (purges, list experiments) estimate the public/private gap at the aggregate level. Frye, Gehlbach, Marquardt & Reuter, "Is Putin's popularity real?", *Post-Soviet Affairs* 33: 1-15 (online 2016), DOI 10.1080/1060586X.2016.1144334, is a list-experiment study of the same kind (existence and authors confirmed via Crossref; no abstract read).
  - **An intervention on beliefs about others' turnout exists.** Cantoni, D., Yang, D. Y., Yuchtman, N. & Zhang, Y. J. (2019). Protests as strategic games: experimental evidence from Hong Kong's antiauthoritarian movement. *Quarterly Journal of Economics* 134: 1021-1077. DOI 10.1093/qje/qjz002 (Crossref confirmed; working paper NBER w23110, 2017). Abstract (NBER page, via summariser): the first field experiment to shift students' beliefs about others' protest participation, a day before a protest; the evidence points to **strategic substitutes**, the opposite of the complementarity that Granovetter's and Kuran's maps assume. This is the most direct challenge to the monotone-F assumption found here and should be read before any equation rests on complementarity.
- A bridge between CCC and MM's event sizes and a defined group, so r(t) is not computable. This is the main finding of this file for the algebra: **the data are event-level; the equations are person-level.**

---

## Does it reduce to a drive basis?

**Partly, and the part that does is the smaller part.**

- **Reduces.** The individual threshold is, by Granovetter's own account, "the result of some (possibly complex) combination of costs and benefits". In Kuran's model it is derived from two named motives: reputational reward (belonging and status among co-supporters) and integrity (cost of acting against one's own view). Fear shows up as the cost of arrest (Granovetter) and as the cost of exposing oneself under repression (Kuran). So the *individual* parameter x is plausibly a **net balance of drives** (grievance or desire for change against fear or loss against belonging and self-consistency). In González-Bailón it is just the share of followed accounts already active.
- **Does not reduce.**
  1. **F, the distribution of thresholds, is a group-level object.** Granovetter's whole point is that two groups with near-identical mean preferences give totally different outcomes (equilibrium 1 vs 100) because of a *gap*. A drive per person does not determine the gap; it is a property of the composition. A drive basis for the group would have to carry the distribution (or at least its upper tail and gaps), not a mean.
  2. **The aggregation operator r(t+1) = F[r(t)]** (iterate, find fixed points) is not itself a drive. It is a composition law; it would sit in the algebra as an operator on distributions.
  3. **Instability and sampling effects** (0.37 and 0.14 probabilities; sigma_c about 12.2) depend on n and on who happens to be in the crowd, not on any drive intensity.
  4. **Social structure** (friend weights, sociomatrix) changes outcomes; Granovetter notes it "may overwhelm" individual preferences when the equilibrium is unstable.
  5. **Elite defections, the security forces and repression** (NAVCO's sec_defect, state_defect, repression) are role-bound and institutional; they are not individual drives of the crowd.
  6. **Momentum** (events per week times participants) is a property of *timing and concentration of the group*, with no individual-drive reading in the paper.
  7. Granovetter explicitly *excludes* where the preferences come from, so the model gives no drive content; the "drive" has to be supplied from outside.
- **Verdict on "drives as primitives" for this tradition:** supported only as the story of where one threshold parameter comes from. The *predictive* content of the tradition lies in the distribution and the aggregation map, so, for this tradition, **drives are an input to the parameter and not the primitive of the group-level law**. This is a working-hypothesis check, not a conclusion.

---

## What does it predict or control, and how well?

- **Granovetter.** Predicts equilibrium r_e from F; it is a *conditional* result (given F). Its main empirical content is negative: outcomes are not predictable from mean preference. The only out-of-sample number is Dozier's 5 held-out Korean villages: predictions beat ordinary regression only when the threshold regression explained more than 50% of threshold variance, with possible leakage; Dozier not read. Control: none stated beyond "remove or add the instigator or a gap-filler".
- **Kuran.** Predicts **that revolutions are unpredictable** (1991 abstract), and that the most committed regime supporters defect last. It does not forecast any particular event. No estimation of the model; case evidence only. Unusually for this literature the claim is a result *about the limits of prediction*, which fits file 07's warning about individual-level prediction.
- **3.5% rule.** Outcome: success of maximalist campaigns. In the updated NAVCO table, success is 88.9% (16/18) at or above 3.5% peak participation, falling to 4.2% below 0.0035%; "p<.003". Effect size is therefore large and monotone across bins. Failures: Brunei 1962 and Bahrain 2011-14. Out-of-sample: none planned; found post hoc; the author warns against using it as a target. Reverse-causation risk noted above. Selection bias acknowledged by the codebook (success-biased sample of campaigns of at least 1,000 people).
- **Momentum.** Outcome: irregular leader exit, Africa 1990-2014. Probability "more than triples" from minimum to maximum momentum but absolute probabilities stay low; 24 strict events; no out-of-sample test seen; effect disappears when riots are excluded. Not a control tool yet; the paper itself says it offers dissidents "a straightforward way ... to quantify their coercive potential", which is a claim of use, not evidence of it.
- **Online thresholds.** Description, not prediction: the distribution of k_a/k_in is roughly uniform with peaks at 0 and 0.5 in one episode of one movement (Spain 15-M); no forecast of another episode.
- **Consent or manipulation.** Nothing here tests an intervention. The mobilisation levers discussed (turnout, tempo, defection) are voluntary on the movement side. The state-side levers (repression, which NAVCO codes) act on the cost term and are coercive. Whether manipulating perceived participation (Granovetter's misperception cases, Kuran's falsified public support) would move outcomes is a theoretical possibility in the models and untested in the data.

---

## Unconfirmed

- **Kuran 1991** (World Politics): paywalled, not read. The version of the threshold function and any numerical illustration in it are not verified. The 1989 model above may not match it in detail.
- **Kuran 1989**: sections 4-5 and the opening of 6 now read (validation); the remainder of 6, section 7 (how falsification gets exposed) and section 8 (post-revolutionary repression) not read in full. There is no appendix.
- **Lohmann 1994** ("The dynamics of informational cascades: the Monday demonstrations in Leipzig, East Germany, 1989-91", *World Politics* 47(1): 42-101, DOI 10.2307/2950679, confirmed) and **Enikolopov, Makarin & Petrova 2020** ("Social media and protest participation: evidence from Russia", *Econometrica* 88(4): 1479-1514, DOI 10.3982/ECTA14281, confirmed): not read. Lohmann's Crossref abstract only: forty-two Monday demonstrations in five protest cycles, read as an informational cascade. Their empirical content is otherwise not described here.
- **Dozier 1977**: only Granovetter's summary of it was read.
- **Chenoweth's original 3.5% derivation** (TEDx 2013, Chenoweth & Stephan 2011) and the Technical Appendix of the 2020 brief: not read. The test behind "p<.003" is unknown to me. The table's base is now known (389 maximalist campaigns, both kinds, NAVCO 1.2, per fn. 13), but the 83% is over successful *nonviolent* campaigns only, so the two figures "16 of 18" and "83% of successful nonviolent campaigns lacked 3.5%" should not be combined without reading it.
- **NAVCO 2.0 data file, NAVCO 1.2/2.1/3.0 contents, CCC Phases 2 and 3, SCAD**: metadata only or not opened. I did not download the NAVCO tab file or compute any statistic from it.
- **Global Protest Tracker** methodology: the page's stated inclusion rule (what counts as "significant") is not in the static HTML; no download link was found there.
- **MM participants_category blank rate among events (35.1%; 42% of all rows) and CCC unknown rate (50%)** are my counts of the files named above; I did not check whether blanks mean "not reported" or "not coded". The MM manual says the category was added mid-coding.
- **González-Bailón** SI not read (the 70-hashtag list and robustness checks).
- **Jiang & Yang 2016, Frye et al., Cantoni et al. 2019** (added in validation): abstracts only (Frye: not even that); [sa]. They bear directly on whether x can be measured and on whether participation is a complement or a substitute, and need reading before use.
- **Whether any of the four datasets supports a person-level threshold estimate** is a negative claim from the codebooks and data dictionaries I read; I did not search for derived datasets (e.g. Twitter-linked protest panels) beyond González-Bailón.

## Validation log (2026-10-30)

- ✓ Granovetter 1978, AJS 83(6):1420-1443, 10.1086/226707. Full text re-read: r(t+1)=F[r(t)], 45-degree fixed point, sigma_c about 12.2 (n=100, mean 25), 63/120=.525, .37/.14/.51 and .9^10=.35, single-crossing net-benefit curve, Dozier summary (23 villages, 18/5 split, 50% variance) all confirmed. ✎ added the paper's own credits: Winship (difference equation), Phillips (normal case), Danforth (simulations).
- ✎ Kuran 1989, Public Choice 61(1):41-74, 10.1007/BF00116762. Eqs (1)-(8) confirmed against the text. Read further (secs 4-5, opening of 6, conclusion): added the three comparative-statics results, eq. (9) revolutionary potential S* with Table 1 values, and the repression-as-leftward-shift reading; replaced the unsupported "distribution tail" claim with what the paper says (g alone cannot precipitate).
- ✓ Kuran 1991, World Politics 44(1):7-48, 10.2307/2010422. Paywalled; Crossref abstract re-read and matches the quoted line. Body stays [sa].
- ✎ Chenoweth 2020, Carr Center DP 2020-005. Read from an HKS-hosted PDF. Quotes, Brunei/Bahrain figures and table values confirmed. Corrected "denominator not stated": fn. 13 gives 389 maximalist campaigns (violent and nonviolent, NAVCO 1.2, 1945-2013). Reconciled 16/18 with the two named exceptions (as an inference). Added that armed-campaign peaks count fighters, and Lichbach's 5% figure came from a footnote.
- ✎ Chenoweth & Belgioioso 2019, NHB 3(10):1088-1095, 10.1038/s41562-019-0665-8. Author copy read. **Corrected an inverted claim:** leader-exit probability stays low *below*, not above, the 75th-percentile mass and median velocity. Added that mass is built from SCAD's 7-point ordinal npart scale.
- ✎ González-Bailón et al. 2011, Sci Rep 1:197, 10.1038/srep00197. Threshold definition, 87,569 / 581,750 / 98.03%, uniform-with-peaks-at-0-and-0.5, burst finding and media caption all confirmed. Added the 70-hashtag definition of "active" and that broadcaster removal changes F.
- ✎ Mass Mobilization (Clark & Regan), doi:10.7910/DVN/HTTWYL, CC0. Manual definitions confirmed. **Corrected the counts:** 17,145 is rows, of which 15,239 are protest events. Category blanks among events are 5,352 (35.1%), not 7,258 (42%).
- ✓ CCC Phase 1-3 (Chenoweth, Pressman, Ulfelder; plus Hammam and Shay), DOIs, CC0, file sizes and versions confirmed. Dictionary rules (hundreds=200, several=3, size_cat bins, valence, macroevent scope, Count Love 3,400+ outlets) confirmed. Recount matches 72,181; size_cat bins differ by 1-2 rows depending on the parser. ✎ added credits.
- ✓ NAVCO 1.1/1.2/2.0/2.1/3.0 and Major Episodes: DOIs and CC0 confirmed. The NAVCO 2.0 codebook's 250 campaigns, 1,000-participant floor, "biased toward success" and the variable codes are confirmed. ✎ added authors (2.0 is Chenoweth & Lewis) and 1.2's 1945-2014 span.
- ✎ Global Protest Tracker (Carnegie). Full raw HTML searched. **Corrected "no size":** the table has 1,054 entries with peak size, duration, motivation and violence. Still no download link, no stated threshold, all rights reserved.
- ? Dozier 1977 (Stanford PhD dissertation), Lohmann 1994, Enikolopov et al. 2020: existence confirmed (Granovetter's reference list for Dozier; Crossref for the other two), content not read.
- ✎ "Does not exist" claims tested by search. Two were false, and the file now lists the counterexamples [sa, abstracts only]: measurement of preference falsification (Jiang & Yang 2016, CPS, 10.1177/0010414015626450; Frye et al., Post-Soviet Affairs, 10.1080/1060586X.2016.1144334) and a field intervention on beliefs about others' turnout (Cantoni, Yang, Yuchtman & Zhang 2019, QJE, 10.1093/qje/qjz002), which reports strategic *substitutes*.
- ✗ No fabricated works found; nothing deleted.

Sources opened by the validator: 12 (Granovetter PDF, Kuran 1989 PDF, Chenoweth 2020 PDF, Chenoweth & Belgioioso author PDF, González-Bailón PDF, MM manual, NAVCO 2.0 codebook, CCC Phase 1 dictionary, MM v16 data file, CCC Phase 1 data file, Global Protest Tracker HTML, NBER w23110 page). Also opened: Crossref records for all DOIs and Dataverse metadata for 10 datasets.

**Verdict.** The citations are real, correctly attributed and the DOIs resolve. The equations from Granovetter and Kuran 1989 are transcribed faithfully. Errors were in the empirical detail, all now fixed: an inverted reading of the momentum result, MM's row count reported as events, a Global Protest Tracker field list taken from a partial fetch, and two "nothing exists" claims that a search refuted. The headline holds (event data cannot identify F or g). Cantoni et al.'s substitutes finding is the item most likely to change the algebra and should be read at source before any drive equation assumes participation is a complement.

## Cross-checks (2026-10-30)

**Method.** Grep of every other file in `docs/prior-work/` for the works named here (Granovetter, Kuran, Chenoweth, Belgioioso, González-Bailón, Dozier, Spilerman, Cantoni, Jiang, Frye, Lohmann, Enikolopov, NAVCO, Mass Mobilization, CCC, Global Protest Tracker), for their DOIs, and for the numbers (sigma_c, .37/.14/.51, 63/120, Kuran eq. 8). Files that name Granovetter: 05, 066, 067, 068, 081, 091 and others that cite the threshold model in passing. Files that name Kuran: 066, 067, 068. No other file names the protest datasets, Chenoweth, González-Bailón, Dozier, Lohmann, Enikolopov, Cantoni or the Frye and Jiang studies. The "strategic substitute" hit in file 23 is an eigenvalue remark about a different model, not Cantoni et al., and is not a contradiction.

**Agreements.**
- Granovetter's map r(t+1) = F[r(t)] and equilibrium at the first crossing from above: this file §1 = 066 §1 = 05 §12.
- Sampling numbers .37, .14, .51 and (.90)^10 = .35: this file §1 = 066 §1.
- sigma_c approximately 12.2 for normal thresholds (n = 100, mean 25): this file §1 = 066 §1 (computed 12.222) = 081 §1.2.
- Thresholds 0,1,...,99 giving equilibrium 100, and the threshold-2 swap giving 1: this file §1 = 05 §12.
- Friend-weight example 63/120 = .525: this file §1 = 066 validation log.
- Granovetter's paper has no fit to data, and Spilerman is an illustration, not a test: this file §1 = 066 §1.
- Kuran eq. (8), S = g(x(S^e)), with one or three equilibria: this file §2 = 066 §3. Both attribute it to Kuran 1989 (*Public Choice*), not to the 1991 paper.
- Kuran 1991 is unread here and in 066: this file §2 = 066 §3.
- Private versus public preference, with falsification as the hidden state: this file §2 = 066 §3 and §6.
- Kuran's model unpredictable in principle: this file §5 = 066 §3.

**Gaps.** 066 §1 records Granovetter's falsification section (pp. 1437-1439: "all or most thresholds at 0% or 100%", and oscillation under a stable cost-benefit curve) and his pluralistic-ignorance remark (p. 1438). This file does not mention either. Both bear on the "what can be falsified" question in §"What it predicts", so they should be added at the next pass.

**Contradictions (not resolved).**
- **C1, Kuran's utility terms.** This file §2 (read at source, Kuran 1989): reputational utility and *integrity* utility. 066 §3 (secondary, via Rasmusen and Brummitt et al.): *intrinsic*, *expressive* and *reputational* utility. The validation log of this file does not settle it, and 066 never read the 1989 text. Unresolved. The primary text is this file's; the term needs checking against it before any utility form is written.
- **C2, the distribution-shift route.** 066 §3 (secondary, citing Kuran 1989 §4.1 and "Fig. 3") says a shift of the private-preference distribution toward the opposition is one of two routes to a saddle-node. This file §2, result 3 (read at source, §4.3, "Fig. 6"), says an upward shift of g can set the stage but cannot precipitate a revolution by itself. These may both be true (a saddle-node creates the alternative equilibrium without triggering the jump), but the figure numbers differ and the wording differs. Unresolved.

**Provenance note.** 05 §12 tags the stability criterion F'(r) < 1 as "[from abstract/standard account]"; 066 §1 tags the same criterion as [derived]. Not a contradiction of content, but the tag should be one or the other.

**Ledger.** Lines are returned with the structured result; they are not written into this file. Nothing committed.
