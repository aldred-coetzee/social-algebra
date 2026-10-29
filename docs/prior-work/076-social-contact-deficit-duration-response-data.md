# 076. Human duration-response data for the social-contact deficit

Direction: D457 (data). Date: 2026-10-29. Seeds: Tomova et al. 2020; Stijovic et al. 2023; Hall & Davis 2016/17; Lee, Chen & Tye 2021. From file 22.

**Method note.** WebSearch was exhausted by the shared budget, so this is built from Crossref, Europe PMC and PMC full text (WebFetch). Tags: [read] = the passage was read at source (PMC/Europe PMC full text, through a summarising fetch tool, so numbers are as that tool returned them; re-check against the PDF before citing in print); [abstract/metadata] = Crossref or Europe PMC record only. No search for further isolation studies could be run; see Unconfirmed.

**Summary.** The question is whether human data exist that trace the social-contact deficit over time (growth, saturation, ceiling). Blunt answer: **two lab datasets exist with repeated within-session ratings, both public, neither fitted with anything but a straight line, and neither goes beyond 10 hours.** No human data were found on the satiety/ceiling side. The only dose-like human data on excess contact is theoretical (Hall & Davis). Lee, Chen & Tye is an animal review and supplies no human data. The prior file 22 said "Dose-response in time is not mapped: one duration (10 hours), one condition". That is right about duration but **wrong that only the endpoints were measured**: Tomova collected ratings every 2 h. The time course is plotted in the paper (Tomova et al. 2020, Fig. 2b: boxplots of social craving over time during isolation) but was never modelled; only first-versus-last tests were run. Whether the intermediate points are in the public OSF deposit is unconfirmed. *(Validation 2026-10-29: the original note said the curve had "apparently not been published"; Fig. 2b's legend shows it was, as a plot.)*

---

## 1. Tomova et al. 2020 (dataset: ratings every 2 h over 10 h)

**Citation.** Tomova, L., Wang, K. L., Thompson, T., Matthews, G. A., Takahashi, A., Tye, K. M. & Saxe, R. (2020). Acute social isolation evokes midbrain craving responses similar to hunger. *Nature Neuroscience* 23(12), 1597-1605. DOI 10.1038/s41593-020-00742-z (confirmed Crossref). Author Correction: *Nature Neuroscience* 25(3), 399 (2022), DOI 10.1038/s41593-021-01004-2 (confirmed Crossref; content not read). Author manuscript PMC8580014.

**Data access [read].**
- De-identified neuroimaging: OpenNeuro, DOI 10.18112/openneuro.ds003242.v1.0.0.
- Summary fMRI and behavioural data, plus analysis and figure code: OSF, DOI 10.17605/OSF.IO/F9CRU.
- Task code and example stimuli: OSF, DOI 10.17605/OSF.IO/CF2RT. Preregistration: osf.io/cwg9e.
- Licence: not stated in the fetched text; Crossref lists only Springer Nature TDM terms for the article. Check each repository's licence field before reuse (not verified).

**Variables and sample [read].** N = 40 healthy "socially connected" adults (27 women, 18-40), 10 h alone (09:00-19:00), no phone, laptop or social media; one session each of isolation and food fasting (also a baseline session with an evening scan), the three scan sessions at least 24 h apart, order counterbalanced. Isolation condition: online 0-100 visual-analogue ratings of loneliness, social craving, discomfort, happiness and dislike of isolation **"every 2 h during the social isolation period"** (so about six time points per person, 0 to 10 h). Fasting condition: food craving, hunger, discomfort, happiness, dislike of fasting, same schedule. In-scanner craving 0-10 after each cue block (5 s to respond); pre-scan craving questionnaire (Craving_Q, 0-100). Shared household was an entry requirement, so participants expected contact after the session. UCLA loneliness and social network measures at screening.

**What was reported [read].** Only first-versus-last paired t-tests (isolation, df = 39): social craving t = 5.00, loneliness 5.17, discomfort 5.57, dislike of isolation 4.13, happiness -4.21. Fasting (df = 36): food craving 17.40, hunger 23.90, discomfort 13.56, dislike 6.28, happiness -3.05. Of 40, 36 reported feeling more lonely after isolation. Social craving after 10 h isolation was more variable across people than food craving after 10 h fasting (mean (s.d.) 66.38 (24.52) vs 80.25 (19.39); Levene F(76) = 15.86, P < .001). Fasting tests used n = 37 because three participants missed the first or last fasting questionnaire.

**What the drive equation could test.** With the 2-hourly series (not examined by me) one could fit, per person, `d(t)` for the contact deficit: linear `d = d0 + k t`, saturating `d = D(1 - e^{-t/τ})`, or logistic. Individual variance (Levene result) means a hierarchical fit with per-person `k` or `D` is the natural form, and `D` would be a candidate "trait" parameter. **Limits:** six points and one duration cannot separate linear from mildly saturating growth; no recovery (reunion) period was sampled, so relaxation rate is unidentified; no control for boredom (Stijovic et al. 2023 found boredom only partially mediates the isolation effect on energy and fatigue; they did not test it for loneliness or desire).

**Empirical standing.** Self-report effects are robust within the study and echoed by Stijovic. Preregistered anatomical SN/VTA test was null for social cues: in the anatomical ROI, responses to social cues were not significantly higher after isolation than after fasting (b = 0.006, t = 0.7, P = 0.50) [read]; the positive midbrain results came from the functionally localized ROI, which the authors label exploratory (see file 22, A2). No independent fMRI replication found (search not exhaustive).

## 2. Stijovic et al. 2023 (lab: hourly and 2-hourly ratings over 8 h; field: 7-day ESM)

**Citation.** Stijovic, A., Forbes, P. A. G., Tomova, L., Skoluda, N., Feneberg, A. C., Piperno, G., Pronizius, E., Nater, U. M., Lamm, C. & Silani, G. (2023). Homeostatic regulation of energetic arousal during acute social isolation: evidence from the lab and the field. *Psychological Science* 34(5), 537-551. DOI 10.1177/09567976231156413 (confirmed Crossref). PMC13029414, licence CC BY (Europe PMC record).

**Data access [read].** "The data, analysis code, and analysis outputs for both the lab and the field study have been made publicly accessible via OSF": https://osf.io/s8xk9/. Open Data keyword; CC BY article.

**Lab design [read].** 30 women, 18-33, three counterbalanced 8-h sessions: baseline (meals plus four 30-min prescheduled video/audio calls with friends and family, one every 2 h; internet and smartphones otherwise barred in all sessions), social isolation (SI; meals, no contact), food deprivation (FD; contact, no meals). Stress, anxiety, control, avoidance rated hourly (hours 0-8, VAS); mood, fatigue, desire for social contact and food at hours 0, 2, 4, 6, 8; manipulation-check items (desire for social contact, loneliness, desire for food, hunger) each on a 0-100 VAS; boredom at 0, 4, 8 (0-100 VAS); energetic arousal from the Multidimensional Mood State Questionnaire (Steyer et al. 2003; four bipolar adjectives on 5-point scales, score 4-20). Hourly saliva (cortisol, alpha-amylase), continuous heart rate.

**Lab results [read].** Fixed effects versus baseline: energetic arousal SI beta = -1.73 (SE 0.42, p < .001), FD -1.27 (p = .003), BF01 = 3.71 for SI-FD comparability; general fatigue SI 0.37 (p = .004), FD 0.43 (p < .001), BF01 = 9.13; loneliness SI beta = 13.01 (p < .001); desire for social contact SI beta = 14.19 (p < .001). Hunger (beta = 33.37) and food desire (34.78) rose under FD, about 2.5 times the SI effects on loneliness and social desire. Stress (p > .3) and anxiety (p > .27) unchanged; cortisol and alpha-amylase not modulated by either deprivation after Bonferroni correction; heart rate not modulated by SI (lower under FD).

**The nearest thing to a human growth rate [read].** Linear condition x time models. Desire for social contact: SI-by-time beta = 2.29 (SE 0.61), t(328) = 3.75, p < .001; loneliness 1.72 (SE 0.54), t(357) = 3.19, p = .002. Simple slopes within isolation: desire beta = 3.73 per hour (p < .001), loneliness 2.96 per hour (p < .001). **But the baseline session also rose**: desire 1.45 (p = .007), loneliness 1.24 (p = .001), with scheduled social calls. So the isolation-specific slope (the interaction term, which equals 3.73 - 1.45 and 2.96 - 1.24) is about 2.3 (desire) and 1.7 (loneliness) VAS points per hour, on a 0-100 VAS (confirmed in Methods). The baseline rise of 1.2-1.5 per hour happened despite the scheduled calls; the authors do not explain it (they suggest remote rather than in-person contact may have weakened the baseline), so reading it as time-of-day or boredom drift is this file's interpretation, not theirs. The model is linear only: no curvature or plateau test is reported. Figure 2 plots raw data (solid lines) and model estimates (dashed) over the day; image not viewed.

**Field study [read].** 87 adults (47 women), Austria/Italy/Germany, COVID lockdowns (April-May and November-December 2020), smartphone prompts in four windows a day (10-11, 11-14, 14-17, 17-20 h) for 7 consecutive days. Only days with all four prompts answered were analysed; a day counted as SI if no social interaction was reported at any of the four prompts, baseline if at least one was: mean 1.46 (SD 0.76) SI days and 3.02 (SD 1.46) baseline days per person. Field study preregistered at osf.io/6ynt3. Findings: loneliness higher on SI days (beta = 3.64, p = .007); **desire for social contact LOWER on SI days (beta = -3.22, p = .031)**, the opposite sign from the lab; no overall energetic-arousal difference; energy lower on SI days for high sociability (simple slope -4.69, p = .013) and for people living alone (-6.41, p = .006). Time of day did not interact with day type.

**Why the sign flip matters.** The lab shows the deficit raising desire; the field shows desire falling on isolated days. Authors' own caveats: field data are correlational, people may select solitude, and sociable people may avoid contact on low-energy days. For the algebra this is the central unresolved point: **a deficit variable `d` that rises with time since contact (lab) is not the same as the felt wish for contact (field)**. Chosen solitude is an input (a policy), not a clamp, and the lab design forces the clamp. A model needs `d` and `want` as separate sorts, with `want` also depending on cost, choice and boredom.

**Empirical standing.** Single-lab, all-women lab sample (30), authors share a person (Tomova) with the first study; not independent in the strong sense. Boredom only partly mediates the energy and fatigue effects (post hoc). Treat as a plausible, small, honest dataset, not a replicated law. D459 is the independent-replication question.

## 3. Hall & Davis: communicate-bond-belong theory (theory, not data)

**Citation.** Hall, J. A. & Davis, D. C. (2017; online 28 Oct 2016). Proposing the communicate bond belong theory: evolutionary intersections with episodic interpersonal communication. *Communication Theory* 27(1), 21-47. DOI 10.1111/comt.12106 (confirmed Crossref). File 22 dates it 2016 (online year); the print issue is February 2017.

**What I could read.** Crossref metadata, plus the abstract at the publisher page (academic.oup.com/ct/article/27/1/21/4093846, read via a summarising fetch tool) [abstract]. No full text. The abstract confirms the theory treats all interaction as energy-expending, describes a homeostatic system driven by the need to belong that balances investing and conserving social energy, and makes no quantitative prediction in the abstract. That is the only source in the seed set that implies a ceiling (interaction costs energy). I did not obtain any equation, any dataset, or any empirical dose-response from it. It cannot be counted as data on the satiety side.

**Action for D458.** Obtain the full text before using it for a two-sided set point.

## 4. Lee, Chen & Tye 2021 (animal review, no human data)

**Citation.** Lee, C. R., Chen, A. & Tye, K. M. (2021). The neural circuitry of social homeostasis: consequences of acute versus chronic social isolation. *Cell* 184(6), 1500-1516. DOI 10.1016/j.cell.2021.02.028 (confirmed Crossref; the DOI is the one found by Crossref bibliographic search, not recalled). The two-page item with the same title at 10.1016/j.cell.2021.04.044 (184(10), 2794-2795) is an erratum: Crossref's record for the main article lists it under relation "erratum". Europe PMC/PubMed (PMID 33691140, PMC8580010) class the main article as a Review. Abstract [abstract]: social homeostasis as detect / compare to set point / adjust effort; contact is negative-valence when in excess; chronic deficits shift the set point so the previous optimum is felt as surplus.

**Relevance.** Not read in full; that it contains no human data is from file 22's description and the abstract's circuit framing, not checked against the text. As described in file 22 it makes the set point two-sided and adaptive (acute versus chronic isolation yield different states). For D457 it matters only as the animal source of the form `d(t)` and of the chronic-versus-acute distinction, which no human dataset in this file addresses (all human durations are 8-10 h).

## 5. Catalogue summary (what could test which equation)

| Dataset | Access | Variables | Sample | Durations | Tests |
|---|---|---|---|---|---|
| Tomova 2020 behavioural + fMRI | OpenNeuro ds003242; OSF F9CRU | loneliness, social craving, discomfort, happiness every 2 h; cue-reactivity fMRI | 40 (27 F) | 10 h, 6 pts (plotted in Fig. 2b; OSF content unchecked) | linear vs saturating `d(t)`; per-person `D`, `k`; cue readout of `d` |
| Stijovic 2023 lab | OSF s8xk9 | desire for social contact, loneliness, mood, fatigue (0,2,4,6,8 h); stress hourly; cortisol, amylase, HR | 30 F | 8 h, 3 sessions | isolation-specific slope net of baseline drift; deprivation parity (social vs food) |
| Stijovic 2023 field | OSF s8xk9 | momentary loneliness, desire, energy, 4 prompts/day x 7 days | 87 | days | chosen vs forced solitude; trait moderators (sociability, living alone) |

## 6. Operand/operator translation

- Operand: `d_contact(t)` scalar deficit per person (sort: person state). Rate evidence: forced isolation raises desire about 2.3 and loneliness about 1.7 VAS pts per hour above baseline drift over 8 h (Stijovic, [read]); no ceiling identified within 8-10 h.
- Operator: `isolate(Δt)` raises `d` at a person-specific rate; `contact(Δt)` lowers it at an unmeasured rate (no reunion data). Free-time-of-day and boredom terms needed.
- Need a separate `want` sort. Field data contradict `want = d`.
- The ceiling (excess contact aversive) has animal-circuit support (file 22) and a theoretical human account (Hall & Davis); no human dose data.

## What exists vs what does not

- **Exists:** two open lab datasets with repeated within-session ratings of loneliness and social desire up to 10 h; effect sizes in VAS points; a field dataset that complicates the lab sign.
- **Not found (seed set only; no literature search could be run):** any human recovery curve after reunion; any human isolation duration beyond 10 h with these measures in the seed set; any saturation or curvature test; any human measurement of social excess (satiety) in a controlled dose; a published per-person fit of `D` and `τ`; an independent replication of either lab study.

## Unconfirmed

- Whether the 2-hourly Tomova ratings are in the OSF summary data or only the first and last (the Methods say they were collected; the OSF contents were not opened).
- The licence of the OpenNeuro and OSF deposits.
- Whether Hall & Davis state any quantitative prediction in the full text (the abstract states none).
- Whether longer-duration isolation human data exist (Antarctic overwintering, bed rest, solitary confinement, lockdown ESM studies, cave studies): not searched; search budget gone in both the original pass and the validation pass (2026-10-29). This is the obvious next pass. Until then the "Does not exist" list above means "not found in the seed set", not "absent from the literature".

## Validation log (2026-10-29)

Every DOI resolved at api.crossref.org; Tomova et al. 2020 read in the PMC author manuscript (PMC8580014) and Stijovic et al. 2023 in the Europe PMC full text (PMC13029414), each number below grepped against the text. WebSearch was exhausted for this pass too, so no "nothing exists" claim could be tested by search; those claims are now worded as seed-set limits.

- ✓ Tomova, Wang, Thompson, Matthews, Takahashi, Tye & Saxe 2020, *Nat. Neurosci.* 23(12) 1597-1605, 10.1038/s41593-020-00742-z: authors, N = 40 (27 women, 18-40), 09:00-19:00, 0-100 VAS every 2 h, all ten t values and dfs, Levene F(76) = 15.86, OpenNeuro/OSF DOIs, osf.io/cwg9e all match [read]. ✎ "time course not published as a curve" corrected: Fig. 2b plots it. ✎ Correction details added (25(3) 399, 2022). ✎ SN/VTA null made specific.
- ✎ Stijovic, Forbes, Tomova, Skoluda, Feneberg, Piperno, Pronizius, Nater, Lamm & Silani 2023, *Psychol. Sci.* 34(5) 537-551, 10.1177/09567976231156413: all betas, SEs, dfs, BFs and field numbers match [read]. Corrected: SI-day definition (no interaction at any of four prompts, not "in the first four"); boredom mediation applies to energy and fatigue only; "roughly twice" is about 2.5x; Fig. 2 shows raw data as well as model estimates; baseline-drift explanation flagged as this file's interpretation. VAS 0-100 now confirmed (removed from Unconfirmed).
- ✎ Hall & Davis 2017 (online 28 Oct 2016), *Commun. Theory* 27(1) 21-47, 10.1111/comt.12106: metadata confirmed; abstract now read via the publisher page and the "social energy / homeostatic / need to belong" description confirmed [abstract]; no quantitative prediction in the abstract.
- ✎ Lee, Chen & Tye 2021, *Cell* 184(6) 1500-1516, 10.1016/j.cell.2021.02.028: confirmed; 10.1016/j.cell.2021.04.044 resolved as its erratum (Crossref relation); Review type confirmed in PubMed/Europe PMC (removed from Unconfirmed). "No human data" left as file 22's claim, not checked.
- ? OSF/OpenNeuro deposit contents and licences: not opened.
- ? Longer-duration human isolation data, independent replications: unsearched (budget).

**Verdict.** The file is accurate on its numbers and attributions: every statistic checked against both full texts matched, and no fabricated work or DOI was found. The substantive correction is that Tomova's 2-hourly time course *is* published as a plot (Fig. 2b), merely never modelled. Several glosses were tightened (Stijovic's SI-day rule, the scope of boredom mediation, the baseline-drift reading). The absence claims remain untested by search and should be read as limits of the seed set.

## Cross-checks (2026-10-29)

Compared against the validated files by grepping for Tomova, Stijovic, Hall & Davis, Lee/Chen/Tye, isolation, loneliness, the OSF/OpenNeuro identifiers and "076". Files 22, 42, 052, 054 and 081 overlap; 078 and the others do not. Primary-source rechecks were attempted for the Tomova points below; PMC returned a browser-verification page and Europe PMC returned 500/403, so those points are unresolved here.

### Agreements
- **22 A2 (Tomova design and numbers).** N = 40 (27 women), age 18-40, 10 h alone against 10 h fasting plus a baseline day, preregistration osf.io/cwg9e. The five isolation t values (5.00, 5.17, 5.57, 4.13, -4.21), food craving t(36) = 17.40, 36 of 40 lonelier, and the preregistered SN/VTA null (b = 0.006, P = 0.50) all match 076 section 1. DOI and the correction DOI 10.1038/s41593-021-01004-2 match.
- **22 A2 (Stijovic).** Same DOI, 8 h lab, N = 30 women, N = 87 field. Both say energy and fatigue effects are comparable to fasting, and that the field energy effect holds only for high sociability or living alone. Both say there is no independent fMRI replication of Tomova.
- **22 A1 and 42 (Lee, Chen & Tye 2021).** Same DOI (10.1016/j.cell.2021.02.028), *Cell* 184, 1500-1516, same PMC8580010. All agree it is a rodent-based review and that the set point is two-sided and adaptive (excess contact aversive, chronic deficit shifts the set point). 076 adds the erratum DOI, which 22 does not carry.
- **22 section "only social contact has homeostatic grounding" (Hall & Davis).** Same DOI (10.1111/comt.12106), same reading (interaction costs social energy, homeostatic, need to belong). 22 had title and search summary only; 076 read the abstract. 076 does not conflict.
- **22 summary and 42 line 56.** Both say there is no human decay rate, no human satiation curve and no cross-person scaling. 076 says the same.
- **052 section 1.2 and agreement list.** 052's saturating form P = P_max(1 - e^(-d/tau)) matches 076's candidate d = D(1 - e^(-t/tau)); both call it an untested illustration with tau unestimated and no human saturation data.
- **054 line 356.** Boredom only partly mediates the energy and fatigue effects (post hoc). Matches 076 section 2, including the scope limit to energy and fatigue.
- **081 lines 38 and 179.** Lists 076 as a data-side attempt. Consistent: 076 offers deficit-over-time data, not cascade-threshold data, and does not claim otherwise.
- **078 (ESM datasets).** Does not cite Tomova or Stijovic. Its "genuine drive items" gap (social need in ESM) is consistent with 076's catalogue, and the Stijovic field study (OSF s8xk9) is a candidate that 078 does not list.

### Contradictions and discrepancies
1. **Time course of Tomova's ratings.**
   - 22 A2: "Dose-response in time is not mapped: one duration (10 hours), one condition"; and "self-report after isolation versus its start."
   - 076 (summary and section 1): ratings were taken every 2 h and plotted in Fig. 2b, but never modelled.
   - Verdict: **076 is right on the point that matters**, and it does not contradict 22's narrower claim. 22 is correct that only one duration and one condition were run, so it is no dose-response in the duration sense. 22's wording can be misread as "only endpoints measured", which 076's validation checked against the PMC full text. I could not re-open the primary source in this pass. Whether the intermediate points are in the OSF deposit is unresolved. 22 should be reworded; 22 was not edited.
2. **Tomova entry criteria and restrictions.**
   - 22 A2: "people living alone or scoring high on loneliness were excluded, per the preprint"; isolation had "no social media, email or fiction".
   - 076 section 1: "Shared household was an entry requirement"; isolation had "no phone, laptop or social media". It does not mention a loneliness exclusion.
   - Verdict: **unresolved.** The household point is compatible in both (a shared household implies not living alone). The loneliness exclusion and the exact banned items differ in wording, and 22 cites the preprint while 076 cites the published manuscript, so both may be right. Primary source not reachable in this pass. Check the Methods before citing either list in print.
3. **052's statement that 076 notes the isolation / general-contact confound.**
   - 052 line 279: "both note the isolation / general social-contact confound."
   - 076: does not state that confound for the human data. It notes forced versus chosen solitude (section 2), the baseline session rising despite scheduled calls, and boredom. Section 4 draws the acute versus chronic distinction from Lee et al. only. The confound 052 describes (isolation also removes general contact, grooming rising with a different time constant) is Siviy's rat finding, which 076 does not discuss.
   - Verdict: **052 overstates 076's content here.** This is a cross-reference slip in 052, not a factual conflict over a source. No primary-source check needed.
4. **Hall & Davis year.** 22 gives 2016, 076 gives 2017 (online 28 Oct 2016, print 27(1) February 2017). Verdict: **no real conflict**; same work, 076's dating is the more exact (Crossref).

No conflict was found on any equation, effect size, or sample size between 076 and the other files.

## Licences of quoted and transcribed material (2026-10-30)

No text was changed by the licensing audit of this file: all five flagged items had verdict "check", and none is a reproduction. Statistics, effect sizes, sample sizes and citations are facts and are free to reuse; the entries below record what is quoted or referenced and under what licence.

| Source | Licence as determined | How used |
|---|---|---|
| Tomova et al. 2020, *Nature Neuroscience* 23(12) (article and PMC8580014 author manuscript) | Not determined; publisher copyright (Springer Nature) presumed | Restated numbers (t values, N, schedule); one short quoted phrase ("every 2 h during the social isolation period"); description of Fig. 2b, no figure content copied |
| OpenNeuro ds003242 (Tomova 2020 neuroimaging) | Not determined; check the OpenNeuro licence field before any reuse | Dataset citation only (DOI); no data copied |
| OSF F9CRU and OSF CF2RT (Tomova 2020 summary data, code, task code) | Not determined; check each deposit's licence field | Dataset citation only; contents not opened |
| OSF registrations osf.io/cwg9e and osf.io/6ynt3 | Not determined | Cited by identifier only; no text reproduced |
| Stijovic et al. 2023, *Psychological Science* 34(5) (PMC13029414) | CC BY (per Europe PMC record) | Restated numbers (betas, SEs, dfs, sample sizes); one short quotation of the data statement; description of Fig. 2, no figure content copied |
| OSF s8xk9 (Stijovic 2023 lab and field data and code) | Not determined for the deposit (the article's CC BY does not automatically cover it); publisher copyright not applicable, check the OSF licence field | Dataset citation only; no data copied |
| Hall & Davis 2017, *Communication Theory* 27(1) (abstract only) | Not determined; publisher copyright (Oxford University Press) presumed | Paraphrase of the abstract; no quotation |
| Lee, Chen & Tye 2021, *Cell* 184(6) (abstract only) | Not determined; publisher copyright (Elsevier) presumed | One-line paraphrase of the abstract in section 4, not in quotation marks; flagged for a near-verbatim check against the abstract, to be rephrased if it is too close |
| Crossref and Europe PMC records | Bibliographic metadata (facts); not reproduced beyond citation fields | DOIs, titles, authors, pages, erratum relation |
