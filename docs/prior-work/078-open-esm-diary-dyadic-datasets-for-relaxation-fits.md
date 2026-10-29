# Prior work 078: open ESM, diary and dyadic datasets for fitting dx/dt = -k(x - x0) + input

Direction: D478

Date: 2026-10-29. Kind: data. Question: which public experience-sampling, diary or dyadic datasets hold at least two drive-like states per person, with what licence, density and size, and how would one fit dx/dt = -k(x - x0) + input to them.

**Method and honesty note.** The web-search budget ran out before any search could run (every WebSearch returned "budget used up"). So this file rests on direct fetches only: the OSF API (api.osf.io), the Crossref API, Zenodo records, and one Nature page. Tags: **[read]** = seen in a fetched record this session; **[crossref]** = bibliographic fields confirmed by Crossref; **[memory]** = my background knowledge, not checked, and must be confirmed before use. Files inside OSF projects were NOT opened, so no variable list, row count or file format below is confirmed unless tagged [read]. The OSF "licence" field was null or an opaque licence ID for most nodes; null means "no licence declared", which is not the same as "free to reuse".

**Summary.** There is a lot of public ESM material and almost none of it is built for this question. (1) Nearly all of it measures affect (valence, arousal, discrete emotions), not drives, so "two drive-like states per person" is met mostly by pairing positive and negative affect, or affect with a second construct (stress, craving, loneliness). (2) Truly open, licensed, row-level data are rare: the clearest cases are a CC BY single-patient series (Kossakowski et al. 2017), a 2-dataset OSF deposit with 15-study pooled data held back (Dejonckheere et al. 2019), and the EMOTE database (request-based). (3) Dyadic datasets with open rows are the scarcest; I confirmed one public project (parent-adolescent, 537 dyads) but not that its data are downloadable. (4) The fitting method is routine (OU/AR(1)/DSEM/ctsem) but the input term is the hard part: it needs time-stamped events, and few public sets carry them.

---

## 1. What the target model needs from a dataset

Equation under test: dx_i/dt = -k_i (x_i - x0_i) + u_i(t), with x_i a drive-like state, x0_i a set point, k_i a relaxation rate, u_i an input (event, other person's state, intervention).

Minimum data features, in order of importance:
1. **Repeated measures of the same person**, ideally 4-10 prompts a day over 7 days or more. Reason: the exact discretisation (section 6) gives lag-Delta autocorrelation phi = exp(-k Delta). With Delta = 2 h and k around 0.5 per hour, phi is about 0.37; with Delta = 6 h it is about 0.05, and k becomes unidentifiable from noise. So prompt interval sets the range of k one can recover.
2. **Time stamps**, not just prompt indices. Overnight gaps and irregular spacing break discrete AR(1) but are handled by the continuous-time form.
3. **At least two states per person**, so that a coupling term (k_ij) or a set point shifted by a second state can be tested.
4. **A recorded input** (event ratings, partner state, a randomised intervention) or the input term cannot be separated from the noise term.
5. **Open licence and row-level access.**

## 2. Catalogue: confirmed this session

### 2.1 Dejonckheere et al. 2019 pooled affect time series (15 studies)
- **Citation.** Dejonckheere, E., Mestdagh, M., Houben, M., Rutten, I., Sels, L., Kuppens, P. & Tuerlinckx, F. (2019). Complex affect dynamics add limited information to the prediction of psychological well-being. *Nature Human Behaviour* 3(5), 478-491. DOI 10.1038/s41562-019-0555-0 **[crossref]**.
- **Access.** OSF project http://osf.io/zm6uw **[read]**; public, created 2018-06-07, **licence field null** **[read]**. Folders: "Reproducible R & MATLAB Code", "2 Datasets", "Figures", "Supplementary Information", "Reply to Lapate & Heller" **[read]**.
- **Data availability statement [read]**: two datasets are in the Supplementary Data or on OSF; "the other datasets ... are available upon reasonable request from the original sources ... but restrictions apply ... used under licence ... not publicly available." So **2 of 15 studies are open; 13 are restricted.**
- **Size.** 15 studies, n = 1,777 in total **[read]**. Per-study size and prompt density are in Supplementary Table 1, not read.
- **Variables.** Positive and negative affect (momentary); well-being scales. Drive-like use: valence pair only.
- **What it could test.** The relaxation rate k_i (the inverse of "inertia"; Kuppens, Allen & Sheeber 2010, *Psychological Science* 21(7), 984-991, DOI 10.1177/0956797610372634 **[crossref]**) fitted per person from two open sets; the paper's own result is that inertia, variability and instability add little beyond mean level, which is a warning that k may be weakly informative about anything beyond the mean.
- **Not read.** The two datasets' internal structure; which two of the fifteen they are.

### 2.2 EMOTE database (Kalokerinos, Kuppens, Koval et al.)
- **Citation.** Kalokerinos, E. K., Russo-Batterham, D., Grewal, K., Moeck, E., Wilson, E. M., Smith, I., Greenaway, K. H., Garrett, P. M., Shrestha, K. M., Kuppens, P. & Koval, P. (2026). The EMOTE Database: An open, searchable database of experience sampling data mapping everyday emotion processes. PsyArXiv preprint, DOI 10.31234/osf.io/h7kxd_v1 **[crossref]**.
- **Access.** OSF node https://osf.io/eb7rt/ **[read]**, public, created 2021-12-07, modified 2026-03-25, licence null, no description **[read]**. The abstract says EMOTE (emotedatabase.com) lets researchers "request experience-sampling data for reanalysis, and ... deposit data for others to use" **[read]**. A Zenodo preregistration using the FEEL Study 1 data from EMOTE (DOI 10.5281/zenodo.23238611, CC BY 4.0) says the record is "publicly accessible, but files are restricted" and N = 179 **[read]**; the CC BY licence covers the preregistration text, not necessarily the data.
- **Size.** The authors' demonstration analyses use Ns = 2,369-2,834 participants and 167,811-190,972 surveys (preprint abstract, via api.osf.io/v2/preprints/h7kxd_v1) **[read]**. Density per person is therefore roughly 67-71 surveys (my division of those two ranges), consistent with 1-2 weeks of daily-life sampling. Not a confirmed figure.
- **Variables.** Emotion items and emotion-regulation processes; item sets differ by study. Which sets carry two or more drive-like items, and time stamps, not read.
- **Why it matters.** This is the nearest thing to a harmonised, multi-study, request-based archive. It would let k and x0 be estimated across thousands of people with the same pipeline. Licence for reuse beyond the request terms is unconfirmed.

### 2.3 Kossakowski et al. 2017: single-participant intensive series
- **Citation.** Kossakowski, J. J., Groot, P. C., Haslbeck, J. M. B., Borsboom, D. & Wichers, M. (2017). Data from 'Critical Slowing Down as a Personalized Early Warning Signal for Depression'. *Journal of Open Psychology Data* 5. DOI 10.5334/jopd.29 **[crossref]**. Licence **CC BY 4.0** **[crossref]**.
- **Companion paper.** Wichers, M., Groot, P. C., Psychosystems, ESM Group, EWS Group (2016). *Psychotherapy and Psychosomatics* 85(2), 114-116. DOI 10.1159/000441458 **[crossref]** (paper licence CC BY-NC-ND 4.0 **[crossref]**; data licence is the separate CC BY above).
- **Size and density [read, JOPD data paper]:** one person, 1,478 ESM measurements over 239 consecutive days (13 Aug 2012 to 11 Apr 2013); 50 momentary items asked 10 times a day at random times within ten 90-minute blocks, plus 6 morning and 6 evening items and 13 weekly SCL-90-R depression items. Five phases (4-week baseline, 0-6-week double-blind, 8-week taper, 8-week post-reduction, 12-week follow-up); venlafaxine reduced from 150 mg to 0 mg over eight weeks on a randomised, double-blind schedule. Data at http://osf.io/j4fg8 (public **[read]**).
- **What it could test.** Many states per time point (so any pair is available), a known perturbation (the taper) as an input, and a long enough series to fit k_i for one person and watch it drift. N = 1, so it validates the estimator, not the law.
- **Link to D482.** This is the standard test case for early-warning signals (rising AR(1), i.e. falling k); the same file serves both directions.

### 2.4 OSF projects found by title search (public; data status unconfirmed)
Each is a **[read]** record of an OSF node title/description only. Licence fields were not shown (opaque ID or null). None has had files opened.

| OSF node | Title (short) | What the description says | Use here |
|---|---|---|---|
| https://osf.io/wcfvt/ | Dyadic affect dynamics: parent-adolescent affect inertia and synchrony as risk factor for depression | Three-week dyadic ESM, **537 parent-adolescent pairs** (description says "will investigate", i.e. a registered/planned analysis); preprint; the node shows a licence ID and a 2026 copyright to "The Authors"; data sharing not stated | Best dyadic candidate: two people, same time, coupling term k_ij testable. Data access unconfirmed. |
| https://osf.io/z2u43/ | Improving the Comparability of Momentary Affect Assessments (item-specific effects in within-person affect dynamics) | Reanalyses **five large intensive longitudinal datasets**; proposes residualised DSEM with reference items; licence null; access requests enabled; created 2025-06-20 | Methods paper that bundles five datasets and handles item heterogeneity; relevant to choosing which "item" stands for a drive. |
| https://osf.io/paxut/ | Measurement of affect dynamics in daily life: an artifact of extreme response style? | Combines several real-world ESM studies | Warns that variability measures can be response-style artefacts. |
| https://osf.io/5b798/ | Adolescent sexting in romantic relationships and daily positive and negative affect dynamics: a dyadic intensive longitudinal study | No description | Dyadic; data access unconfirmed. |
| https://osf.io/djufr/ | Beyond main effects? Affect level as a moderator ... | "Hosts the pre-registration, data, and code" | States data are hosted; contents unopened. |
| https://osf.io/yh395/ | Emotion dynamics in borderline personality disorder: daily-life events, event reactivity, recovery | 10 smartphone prompts a day for 7 days rating PA, NA and positive/negative events; BPD (N=40), MDE (N=38), healthy controls (N=40); stronger reactivity in BPD | Has **events plus reactivity plus recovery**, i.e. the input u(t) and the relaxation k in one design. Access unconfirmed. |
| https://osf.io/7rbxj/ | Emotional inertia in daily life: DSEM analysis of emotion regulation strategy use | Replication of rumination/suppression/reappraisal mediating negative-affect inertia | Gives a DSEM pipeline for inertia. |
| https://osf.io/hf7uj/, https://osf.io/rxun6/, https://osf.io/82m5u/ | Further emotional-inertia projects (regulation; cognitive flexibility; state-dependent "tilt") | Titles only | The "tilt" paper bears on asymmetric relaxation (rate depends on sign of displacement), which a linear -k(x - x0) cannot express. |
| https://osf.io/x8zpq/ | Sex differences and menstrual-cycle temporal variation | Planned daily ESM, 60 days, 20 men and 20 women | A long daily series with a slow forcing (cycle); data stage unclear (planned). |
| https://osf.io/2nj3x/ | General psychopathology and within-person variability of everyday mentalising | Adolescent ESM; **dataset not public**, de-identified data on request | Example of the common pattern: code open, data on request. |
| https://osf.io/qpn5e/ | Temporal dynamics of mental defeat in chronic pain (Warwick WITHIN study) | Network analysis; code provided; **anonymised data on request** | Same pattern. |
| https://osf.io/29svx/ | Connected, yet alone? (social media multitasking, loneliness, need satisfaction; SDT) | Preregistered ESM with need-satisfaction mediators | Possible bridge to D479 (need satisfaction). |

**Pattern across the OSF hits [read]:** most ESM projects list code and preregistration publicly and put the data "on request" or restricted. The share with open row-level data is clearly a minority; I did not count it, and the OSF title searches were truncated at about 100k characters of each result, so there are more records than listed.

## 3. Seeds in the direction that did not resolve to a dataset

- **Kuppens, Oravecz & Tuerlinckx (2010).** Feelings change: accounting for individual differences in the temporal dynamics of affect. *J. Personality and Social Psychology* 99(6), 1042-1060. DOI 10.1037/a0020962 **[crossref]**. The DynAffect/OU paper (see prior-work 27). No data deposit found; the study predates routine data sharing. Treat as a method source, not a dataset.
- **Neel, Kenrick, White & Neuberg (2016).** Individual differences in fundamental social motives. *J. Personality and Social Psychology* 110(6), 887-907. DOI 10.1037/pspp0000068 **[crossref]**. The Fundamental Social Motives Inventory is catalogued in PsycTESTS (DOI 10.1037/t51742-000) **[crossref]**. This is a **trait scale** of named social motives (self-protection, disease avoidance, affiliation and others, per my memory), not a time series. Useful as a candidate for the *drive* items that ESM lacks (D480), not as dynamic data.
- **Sadler, Ethier, Gunn, Duong & Woody (2009).** Are we on the same wavelength? Interpersonal complementarity as shared cyclical patterns during interactions. *J. Personality and Social Psychology* 97(6), 1005-1020. DOI 10.1037/a0016232 **[crossref]**. A lab dyad study with continuous interpersonal-behaviour ratings (per my memory of the method; not read). Dyadic and high-density but no public data found.
- **Butler (TIES).** Crossref returned a 2011 PsycEXTRA conference record (Butler & Howerter, DOI 10.1037/e634112013-852) and the book chapter "Next steps toward understanding interpersonal emotion dynamics" (DOI 10.1017/9781316822944.012) **[crossref]**. The foundational paper is Butler, E. A. (2011). Temporal interpersonal emotion systems. *Personality and Social Psychology Review* 15(4), 367-393. DOI 10.1177/1088868311411164 **[crossref]** (resolved in validation; title as Crossref gives it). No open TIES dataset located.
- **Palumbo, R. V., Marraccini, M. E., Weyandt, L. L., Wilder-Smith, O., McGee, H. A., Liu, S. & Goodwin, M. S. (2017).** Interpersonal autonomic physiology: a systematic review of the literature. *Personality and Social Psychology Review* 21(2), 99-141 (online 2016). DOI 10.1177/1088868316628405 **[crossref]** (resolved in validation). A systematic review of dyadic physiological synchrony, not a dataset.

## 4. Gaps against the required features

| Need | Best confirmed source | Status |
|---|---|---|
| Open licence, row-level, many people | None confirmed. EMOTE is request-based; Dejonckheere has 2 open sets | Gap |
| Two or more drive-like states per person | Positive plus negative affect in every set; Kossakowski has about 50 items | Met only as affect pair |
| Genuine drive items (hunger, social need, curiosity, craving) in ESM | OSF craving and gaming projects (titles seen, e.g. withdrawal symptoms in gaming disorder, data posted, https://osf.io/k9vb2/ **[read]**); loneliness/need satisfaction project (osf.io/29svx) | Scattered, not harmonised |
| Dyadic, open | wcfvt (537 pairs), 5b798 | Access unconfirmed |
| Recorded input u(t) | BPD event-reactivity project (yh395); Kossakowski (taper) | Few |
| Time stamps | Not checked in any file | Unknown |

## 5. Practical access route (what a next session should do)
1. Open the file trees of osf.io/zm6uw, wcfvt, z2u43, yh395, djufr, k9vb2 through `api.osf.io/v2/nodes/<id>/files/osfstorage/` and record format, rows, columns, time-stamp field, licence.
2. Email or request through EMOTE for a harmonised extract: item names, time stamps, study of origin.
3. Pull Kossakowski from osf.io/j4fg8 (figures confirmed in validation).
4. Pick one pilot: Kossakowski (one person, rich) plus the two open Dejonckheere sets (many people, sparse), to check the estimator before touching dyads.

## 6. Fitting dx/dt = -k(x - x0) + u: specification (derived here, standard OU theory; not from a dataset)

**Model.** For person i and state j: dX = -k (X - mu) dt + b u(t) dt + sigma dW, with mu the set point (x0), k > 0, and measurement y_t = X(t) + e, e ~ N(0, s_e^2).

**Exact discretisation** between observations separated by Delta (with u constant over the interval):
X(t + Delta) = mu + exp(-k Delta) (X(t) - mu) + (b/k)(1 - exp(-k Delta)) u + eta, eta ~ N(0, sigma^2 (1 - exp(-2 k Delta)) / (2 k)).
Stationary variance sigma^2 / (2 k). This is the same discretisation the OU-for-affect papers rely on (cited in prior-work 27), written out here rather than read from them.

**Link to AR(1).** phi = exp(-k Delta), so k = -ln(phi)/Delta. With equal spacing the DSEM/AR(1) estimate converts directly. With measurement error, naive phi is biased toward zero, so k is overestimated; fit as a state-space model, not an observed AR(1).

**Estimators, cheapest adequate first:**
- Per-person Kalman filter with irregular Delta (exact likelihood); needs about 50+ points per person to give a usable k.
- Hierarchical Bayesian OU (the route in prior-work 27) pools sparse persons.
- ctsem (R) or Mplus DSEM for multi-state systems with a drift matrix A replacing -k, off-diagonals being coupling; D489 covers parameter recovery.
- Input u: indicator or intensity of rated events; for dyads, u_i = c (X_j - X_i) with the partner's state, which is the standard coupled-relaxation form (compare prior-work 20 and 59).

**What a fit can and cannot show.** A good fit of a linear OU does not distinguish "a drive relaxing to a set point" from "a mood decaying after a shock". Tests that do separate them: (a) k should differ by state in a pattern a drive theory predicts (hunger vs boredom); (b) mu should shift with a manipulated deprivation (D479 data); (c) asymmetric relaxation (the "tilt" project above) would falsify the symmetric linear form.

## 7. What exists vs what does not

**Exists.** Hundreds of public OSF projects on ESM affect dynamics; one clear CC BY single-case series (Kossakowski); two open sets from a 15-study pool; a request-based harmonised archive on the order of 2,500 people and 170,000 surveys (EMOTE); at least two public dyadic ESM projects by title (parent-adolescent, 537 pairs; romantic sexting). A well-established OU/AR(1)/DSEM fitting pipeline.

**Does not exist (as far as found).** An open, licensed, harmonised dataset with named drive items sampled at high density; an open dyadic ESM set with confirmed downloadable rows and time stamps; a public data set that records inputs u(t) and states together for more than a handful of people. Row-level data are mostly "on request", so the practical bottleneck is access and licensing, not method.

## 8. Unconfirmed

- Whether any of the OSF projects in 2.4 has downloadable raw data; formats; column names; time-stamp fields; real licences (null or opaque IDs seen).
- Which two of the 15 Dejonckheere studies are the open ones, and their n and prompts per person.
- EMOTE: licence for reuse, per-person density, which items overlap across studies, the request procedure.
- Open data for Butler's TIES studies and for Sadler et al. 2009.
- Other datasets I believe exist but did not check: Bolger-style daily-diary couple studies, Pittsburgh/Wright dyad data, the Wichers group's other ESM sets, and Fried/Borsboom network-literature open ESM sets. None cited above as fact.
- Not searched at all (budget exhausted): Dataverse, ICPSR, GESIS, DANS, Figshare, GitHub repositories of ESM data.

## Validation log (2026-10-29)

Every DOI below was resolved at api.crossref.org/works/<doi> (Zenodo and PsycTESTS via doi.org); OSF nodes via api.osf.io/v2/nodes/<id>/. Web search was unavailable (per-turn budget exhausted), so the "does not exist" claims in section 7 were NOT re-tested by search and remain "as far as found".

- ✓ Dejonckheere et al. 2019, NHB 3(5) 478-491, 10.1038/s41562-019-0555-0: authors, venue and "15 studies (n = 1,777)" confirmed against the Europe PMC abstract [read]; OSF zm6uw folders confirmed. Data availability statement not re-read (Nature page paywall-redirected); kept as the original pass reported it.
- ✎ EMOTE (Kalokerinos ... Kuppens & Koval 2026), 10.31234/osf.io/h7kxd_v1: authors confirmed; sizes replaced with the abstract's exact ranges (2,369-2,834 participants; 167,811-190,972 surveys) and the access sentence quoted [read].
- ✓ Zenodo 10.5281/zenodo.23238611 (Mildred-Short, Krug & Bianchi preregistration): FEEL Study 1, N = 179, CC BY 4.0, files restricted [read].
- ✎ Kossakowski et al. 2017, JOPD 5, 10.5334/jopd.29, CC BY 4.0: memory figures replaced by the data paper's (1,478 measurements, 239 days, 50 ESM items, 10/day, 8-week venlafaxine taper 150 to 0 mg); data at osf.io/j4fg8 [read].
- ✎ Wichers, Groot et al. 2016, 10.1159/000441458: added issue and pages 85(2), 114-116 (a short communication).
- ✎ Kuppens, Oravecz & Tuerlinckx 2010, JPSP 99(6) 1042-1060: ✓. The bare "Kuppens et al. 2010" credited for inertia is made explicit as Kuppens, Allen & Sheeber 2010, Psych Sci 21(7) 984-991, 10.1177/0956797610372634.
- ✓ Neel, Kenrick, White & Neuberg 2016, JPSP 110(6) 887-907. PsycTESTS 10.1037/t51742-000 resolves at doi.org (not in Crossref); the list of motive domains stays [memory].
- ✎ Sadler, Ethier, Gunn, Duong & Woody 2009: ✓, issue 6 added.
- ✓ Butler & Howerter 2011 (PsycEXTRA) and Butler chapter 10.1017/9781316822944.012 (pp. 179-188).
- ✎ Butler 2011 TIES paper: resolved from "unverified" to PSPR 15(4) 367-393, 10.1177/1088868311411164.
- ✎ Palumbo et al. 2017: resolved from "unconfirmed" to PSPR 21(2) 99-141, 10.1177/1088868316628405, a systematic review, not a dataset.
- ✓ OSF nodes zm6uw, eb7rt, wcfvt, z2u43, paxut, 5b798, djufr, yh395, 7rbxj, hf7uj, rxun6, 82m5u, x8zpq, 2nj3x, qpn5e, 29svx, k9vb2: all exist and are public with the titles given; wcfvt (537 dyads, three weeks) and yh395 (N = 40/38/40, 10 prompts/day, 7 days) checked against the full descriptions. wcfvt is worded as a planned analysis.
- ✓ Section 6 algebra: phi = exp(-k Delta) gives 0.37 (Delta 2 h, k 0.5/h) and 0.05 (6 h); exact OU transition, input term (b/k)(1 - e^{-k Delta})u, innovation variance and stationary variance sigma^2/(2k) are correct; attenuation of phi by measurement error is the standard result.

**Verdict.** The file is honest and largely accurate: every cited work exists with the stated authors, and no fabrication was found. The corrections replace memory-tagged figures (Kossakowski, EMOTE sizes) with sourced ones and resolve two previously unresolved citations (Butler 2011 TIES, Palumbo et al. 2017); the claims about what does not exist were not re-searched and should be treated as provisional.


## Cross-checks (2026-10-29)

Method: grepped the other prior-work files for the works, authors, numbers and equations in this file. No web re-check was needed: the one numeric discrepancy was already resolved against the JOPD abstract in file 053.

### Agreements
- **Dejonckheere et al. 2019** (NHB 3, 478-491, 10.1038/s41562-019-0555-0; 15 studies, n = 1,777): same citation and figures in 27 (refs; validation line "15 studies, 1,777"). Agree.
- **Kuppens, Oravecz & Tuerlinckx 2010** and **Kuppens, Allen & Sheeber 2010** (10.1037/a0020962; 10.1177/0956797610372634): identical citations in 27 refs. 27 section on DynAffect gives dX = -theta(X - mu)dt + sigma dW with theta the inverse of inertia, matching 078 section 1 and 6.
- **Wichers, Groot et al. 2016** (Psychother Psychosom 85(2) 114-116, 10.1159/000441458; venlafaxine 150 to 0 mg over 8 weeks, 239 days, up to 10 prompts/day): matches 053 section 4 and its validation entry.
- **Neel, Kenrick, White & Neuberg 2016** (JPSP 110(6) 887-907): 15 section 4, and 050 section 2.1 and its cross-reference note both treat it as a trait scale. 050 reads the seven motives (self-protection, disease avoidance, affiliation, status, mate acquisition, mate retention, kin care) from the Pick et al. 2022 abstract, which upgrades this file's section 3 list from [memory] to confirmed.
- **Sadler et al. 2009** (JPSP 97(6) 1005-1020): 20 section 12 gives the same citation; observer-coded dominance and warmth with joysticks (dyadic, high-density), consistent with 078's "continuous interpersonal-behaviour ratings". 20 also reports no equations or public data seen.
- **Butler 2011 TIES** (PSPR 15(4) 367-393, 10.1177/1088868311411164): 20 section 6 and its validation list agree; both treat it as theory/framework. **Palumbo et al. 2017** (PSPR 21(2) 99-141, 10.1177/1088868316628405): 20 section 10 agrees.
- **Coupled form u_i = c(X_j - X_i)** and the 20/59/61 skeleton (own set-point pull plus partner function): consistent with 20 section 1 and 61.
- **N = 1 caveat for Kossakowski**: consistent with 27 (Fisher et al.: a law fitted on the group may not hold for an individual).
- **080 section 2** (Boker & Laurenceau 2006; Ferrer & Nesselroade 2003 supply method, daily couple data held by authors) is compatible with 078 section 8's unchecked "Bolger-style daily-diary couple studies" and section 7's claim that no open dyadic set was found.

### Contradictions and tensions
1. **Kossakowski series length: 1,478 here versus 1,474 in 053 section 4.** Verdict: **both right, different denominators.** 053's own cross-check (lines ~197-200) checked the JOPD abstract, which says 1,478 measurements over 239 days; 1,474 is the Wichers & Groot letter's own figure. Use 1,478 for the data set (this file) and 1,474 when describing the letter's analysis. Not a true contradiction; this file's figure is correct for the OSF data.
2. **Genuine drive items "scattered, not harmonised" (section 4) and "no open set with named drive items" (section 7) versus 076.** 076 catalogues Tomova 2020 (OSF F9CRU, OpenNeuro ds003242; loneliness, social craving every 2 h over 10 h, N = 40) and Stijovic 2023 (OSF s8xk9; field study N = 87, 4 prompts/day for 7 days, desire for social contact, loneliness, energy). Neither is cited here. Verdict: this file's "does not exist" claim is **too strong**, since 076 shows open social-need series with drive-named items at moderate density; 078 is incomplete, not wrong about harmonisation. 076 itself flags the Stijovic field set as a 078 candidate. Not re-opened at source here (OSF files unread in 076 as well), so partly **unresolved** on licence and time stamps.
3. **Sadler 2009 "no public data found" versus 20's "estimation method ?"**: not a contradiction; both are unread on data. Marked unresolved.

No file contradicts a dataset size, citation or equation in this file beyond item 1.
