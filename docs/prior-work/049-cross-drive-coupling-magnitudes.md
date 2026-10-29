# Prior work 049: measured magnitudes and time scales of cross-drive couplings

Direction: D107
Date: 2026-10-29. Kind: data. Question: what is measured, in what units and over what time, for fear to affiliation, exclusion to aggression, frustration to anger, and status to fear? Cross-references: 20 (dyadic coupling), 42 (drives by drive), 27 (measuring drive dynamics), 22 (neuroscience).

**Method and honesty note.** Read at source this session: Hartgerink et al. 2015 (PLOS ONE, via a summarising fetch of the full text, first 100k of 107k characters); Verduyn & Lavrijsen 2014/2015 (PDF downloaded, text extracted, results and Table 1 read, Figure 1 values not extractable); Maier & Seligman 2016 (PMC, first 100k of 189k characters); Magee & Galinsky 2008 (PDF downloaded and extracted; definitions and the power-approach passage read, and the whole text grepped for effect sizes, none found). Abstract-level only (search or PubMed abstract): Gump & Kulik 1997, Berkowitz 1989, Gerber & Wheeler 2009, Quarmley et al. 2022, Sherman et al. 2012, Bettencourt & Miller 1996, Rofé & Lewin 1988. Schachter 1959 was NOT read and no secondary page supplying its numbers was found. DOIs below were resolved at Crossref. No full text was available for several papers (PMC served a bot check for Quarmley and the multimotive paper).

**Summary (blunt).** The four couplings are not equally quantified.
- **Exclusion to need threat / mood:** the best-measured coupling in the whole set. Large, immediate, heterogeneous, and it fades.
- **Exclusion to aggression:** a moderate effect (d about 0.4) from one recent meta-analysis, with doubts about the evidence base.
- **Fear to affiliation:** one famous effect, never stated as a rate or a gain, with a long-standing moderator story (similarity, utility) and sex differences.
- **Frustration to anger:** no magnitude found. Berkowitz 1989 is a reformulation, not a measurement.
- **Status to fear:** one observational field result on cortisol and anxiety; Magee & Galinsky is a qualitative review with no effect sizes.
- **Time scales:** almost nowhere. The only systematic time data found are emotion durations (Verduyn), ostracism recovery (Hartgerink, mostly reported second-hand), and rodent passivity (Maier & Seligman). None is a coupling time constant between two drives.

Nothing here gives a coefficient in a drive-to-drive equation of the form dB/dt = k * A. The magnitudes are standardised differences between experimental conditions at a single time point.

---

## 1. Hartgerink, van Beest, Wicherts & Williams (2015): ostracism, 120 Cyberball studies

**Citation.** Hartgerink, C. H. J., van Beest, I., Wicherts, J. M., & Williams, K. D. (2015). The ordinal effects of ostracism: a meta-analysis of 120 Cyberball studies. PLOS ONE 10(5): e0127002. doi:10.1371/journal.pone.0127002 (Crossref resolved). https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0127002

**Their vocabulary.** Ostracism, Cyberball (virtual ball-toss exclusion), fundamental needs (belonging, self-esteem, control, meaningful existence), "first measure" and "last measure" (immediate versus later dependent variable), reflexive and reflective responses.

**Drives/operands.** Participant; three types of dependent measure: interpersonal, intrapersonal, fundamental needs.

**Operators / equations.** None; an effect-size meta-analysis. Numbers `[read]` (full text via fetch, last 7.6k characters unread):
- 120 studies, 98 papers, N = 11,869; mean n = 98.9, median 74.
- First measure: d = -1.36, 95% CI [-1.54, -1.18], k = 120, I^2 = 92.99%, tau^2 = 0.90.
- Last measure: d about -0.76, 95% CI [-0.91, -0.61], k = 95. The text also gives -0.73 and CI [-0.86, -0.59] elsewhere, so the paper is internally inconsistent here.
- Time since ostracism (mean 4.85 minutes) did not moderate the last-measure effect: b = 0.0069, p = .187.
- Homogeneous subset of 19 studies (3 players, 30 tosses, under 5 minutes, immediate needs): d = -2.05, CI [-2.44, -1.65], I^2 = 83%.
- Only 2 of 120 studies lasted over 5 minutes; game length and number of tosses were not reliable predictors.
- Recovery: second-hand in the paper: full recovery within 5 to 10 minutes in some studies, delayed (45 minutes) in people high in social anxiety (Zadro et al., reported not read). The paper calls for more research on this time course.
- Power: detecting the last-measure interaction at power .8 would need about N = 2,186, by the paper's own calculation.

**Theorems or derived predictions.** None. Abstract-level claim: the effect holds across structural, sampling and measure-type moderators.

**Empirical standing.** The first-measure effect is very large but very heterogeneous. The paper gives no separate d for mood, anger or aggression, so this file cannot give a Cyberball number for exclusion to anger.

**Translation.** Operand: participant with need levels. Operator: Exclude(x, y) lowers need satisfaction by about 1.4 SD at once, decaying to about 0.75 SD at the last measure, with an observed time scale of minutes (not hours). The relaxation form (exponential or not) and time constant are not estimated.

---

## 2. Gerber & Wheeler (2009): rejection meta-analysis, 88 studies

**Citation.** Gerber, J., & Wheeler, L. (2009). On being rejected: a meta-analysis of experimental research on rejection. Perspectives on Psychological Science 4(5): 468-488. doi:10.1111/j.1745-6924.2009.01158.x (Crossref resolved; page range not checked). Rebuttal by Baumeister, DeWall & Vohs in the same issue.

**Their vocabulary.** Needs account versus numbness account; belonging, control.

**Operators / equations.** None. Numbers `[from abstract, via search summary]`:
- Mood d = -0.50; self-esteem d = -0.70; no drop in arousal and no flattening of affect.
- Belonging d = 0.69; control d = 1.16 (frustrated by rejection).
- Antisocial responding when measures contrast belonging and control: d = -1.17; prosocial responding when control can be restored: d = 1.21.

**Theorems or derived predictions.** Aggression after rejection reflects attempts to regain control.

**Empirical standing.** The rebuttal says the sample is biased. A later paper (Quarmley et al., PMC9519812, as quoted by a search summary) notes that only 16 of 40 included studies measured actual aggressive or prosocial behaviour, so the aggression conclusion rests on thin behavioural evidence.

**Translation.** A competing mediator hypothesis: exclusion to control-threat to aggression, rather than exclusion to anger to aggression. For the algebra, a three-node chain with a restoring path, not a single edge.

---

## 3. Quarmley et al. (2022): rejection to aggression and prosocial behaviour

**Citation.** Quarmley, M., Feldman, J., Grossman, H., Clarkson, T., Moyer, A., & Jarcho, J. M. (2022). Testing effects of social rejection on aggressive and prosocial behavior: a meta-analysis. Aggressive Behavior 48(6): 529-545. doi:10.1002/ab.22026 (Crossref resolved).

**Numbers `[from abstract, via search summary]`.** Combined N = 3,864. Aggression: k = 19, d = 0.41, p < .0001. Prosocial: k = 7, d = 0.59. Studies measuring both: k = 15, d = 0.71. Authors conclude rejection is a robust elicitor of aggression and cast doubt on a rejection-to-prosocial account. (The k = 7 and k = 15 rows are as given by the search summary; the sign and meaning of d for those two rows are not checked.)

**Related, unverified.** A 2023 Chinese-language meta-analysis (Acta Psychologica Sinica 55(12)) reports 92 studies, r = 0.38, 95% CI [0.34, 0.41], no publication bias `[search summary only; title and authors not captured]`. A 2022 study reported that neither anger nor hostility mediated the ostracism-aggression link (mediator CIs including zero) `[search summary only]`.

**Translation.** The exclusion to aggression edge has a magnitude (d about 0.4, r about 0.4) but anger as the mediator is contested.

---

## 4. Berkowitz (1989): frustration to aggression, reformulated

**Citation.** Berkowitz, L. (1989). Frustration-aggression hypothesis: examination and reformulation. Psychological Bulletin 106(1): 59-73. doi:10.1037/0033-2909.106.1.59 (Crossref resolved). PubMed 2667009.

**Their vocabulary.** Frustration, interference with expected goal attainment, hostile (emotional) aggression, negative affect, attributions, cognitive-neoassociationistic model.

**Operators / equations.** None. The paper is verbal. `[from abstract]`: the 1939 proposition covers only interference with an expected goal on hostile aggression; frustrations create aggressive inclinations to the extent they arouse negative affect; "Frustrations can create aggressive inclinations even when they are not arbitrary or aimed at the subject personally"; attributions shape how unpleasant the thwarting is.

**Theorems or derived predictions.** Qualitative: aggression is driven by negative affect from any aversive event (frustration being one), so frustration to aggression runs through an affect variable.

**Empirical standing.** The abstract says results are mixed though many studies support the core. No effect size or time constant is stated in the abstract, and the full text was not read.

**Translation.** The coupling in the algebra should be Frustrate(x) to NegAffect to AggressiveInclination, with attribution as a gain on the first link. No magnitude exists in what was read. Bettencourt & Miller 1996 (doi:10.1037/0033-2909.119.3.422) is the obvious next source: per secondary summaries, provocation shrinks the male-female aggression difference from d = .33 to d = .17; no frustration-specific value was found.

---

## 5. Schachter (1959), Gump & Kulik (1997), Rofé: fear to affiliation

**Citations.**
- Schachter, S. (1959). The Psychology of Affiliation: Experimental Studies of the Sources of Gregariousness. Stanford University Press. (Book; no DOI. Library records only; not read.)
- Gump, B. B., & Kulik, J. A. (1997). Stress, affiliation, and emotional contagion. Journal of Personality and Social Psychology 72(2): 305-319. doi:10.1037/0022-3514.72.2.305 (Crossref resolved; page range not checked).
- Rofé, Y. (1984). Stress and affiliation: a utility theory. Psychological Review 91(2): 235-250. doi:10.1037/0033-295X.91.2.235 (Crossref resolved; page range not checked).
- Rofé, Y., & Lewin, I. (1988). Social comparison or utility: an experimental examination. Social Behavior and Personality 16(1): 5-?. doi:10.2224/sbp.1988.16.1.5 (Crossref resolved; end page not captured).

**Their vocabulary.** Emotional similarity hypothesis; affiliation; emotional contagion; mimicry; utility theory.

**Drives/operands.** Fear (manipulated threat of shock), affiliation (choice to wait with others, or time spent looking at a partner).

**Numbers.**
- Schachter 1959, `[from memory of the standard account, NOT confirmed by any source in this session]`: 20 of 32 high-fear participants chose to wait together versus 10 of 30 low-fear (about 63% versus 33%). The search tool itself declined to confirm these. Treat as unconfirmed.
- Gump & Kulik 1997, `[from abstract via search]`: female participants, high or low threat, partner believed to face the same or a different situation. Study 1 paired two real participants; study 2 a confederate acting calm or nervous. Affiliation measured as time spent looking at the affiliate. Threat increased affiliation, especially with partners facing the same situation; evidence of facial mimicry and of emotional contagion in self-reported anxiety. No effect sizes were seen.
- Rofé & Lewin 1988, `[from abstract via search]`: replication plus two conditions in which the utility of affiliation was reduced (immediate shock; physiological reactions shown publicly). Marked decrease in affiliation for males but not females in those two conditions.

**Operators / equations.** None exist in these papers. The coupling is a conditional proportion or a duration contrast, not a rate.

**Theorems or derived predictions.** Emotional similarity: Affiliate(x, y) rises with Fear(x) and with similarity of y's situation. Utility theory: Affiliate falls when affiliation risks embarrassment or unwanted contagion. The two predict different sign changes under the same fear, so the coupling is state-dependent, not a constant gain.

**Empirical standing.** Gump & Kulik is a conceptual-replication-style result with unknown N in what was read. Rofé & Lewin suggests the effect is moderated by sex and utility. A secondary item (Chicano and Anglo adolescents) reports a failed replication of Darley and Aronson 1966 on manipulated fear and notes variation by sex and ethnicity `[search snippet only, not read]`. No meta-analysis of fear to affiliation was found in this session.

**Time scale.** Not reported in anything found. Schachter's waiting period was a few minutes in the standard account (unconfirmed).

**Translation.** Operand: agent with fear level F and situation label S. Operator: Affiliate(x to y) with gain g(F, sim(S_x, S_y), utility). The gain's sign and size are not constants; the algebra should store it as a conditional, or hold the moderators as operands.

---

## 6. Magee & Galinsky (2008), Keltner et al. (2003), Sherman et al. (2012): status/power to fear

**Citations.**
- Magee, J. C., & Galinsky, A. D. (2008). Social hierarchy: the self-reinforcing nature of power and status. Academy of Management Annals 2(1): 351-398. doi:10.5465/19416520802211628 (Crossref resolved; pages not checked).
- Keltner, D., Gruenfeld, D. H., & Anderson, C. (2003). Power, approach, and inhibition. Psychological Review 110(2): 265-284. doi:10.1037/0033-295X.110.2.265. Comment: Moskowitz (2004) doi:10.1037/0033-295X.111.3.808.
- Sherman, G. D., Lee, J. J., Cuddy, A. J. C., Renshon, J., Oveis, C., Gross, J. J., & Lerner, J. S. (2012). Leadership is associated with lower levels of stress. PNAS 109(44): 17903-17907. doi:10.1073/pnas.1207042109 (Crossref resolved; pages from memory, unchecked).

**Their vocabulary / definitions `[read]` (Magee & Galinsky PDF).** Social status: "the extent to which an individual or group is respected or admired by others." Social power: "asymmetric control over valued resources in social relations." Power-approach theory (Keltner et al. 2003) `[read as restated by Magee & Galinsky]`: elevated power increases the tendency to focus on and approach rewards; low-power individuals face more social and material threats and have a primary "inhibit" response. "Whereas the powerful see mostly opportunity dancing in front of them, the powerless are more likely to see potential hazards lurking about."

**Numbers.**
- Magee & Galinsky: whole text grepped. No effect sizes, no time constants. It is a qualitative review `[read]`.
- Sherman et al. 2012 `[from abstract via search]`: real leaders (military officers, government officials) had lower cortisol and reported less anxiety than nonleaders (study 1); within leaders, higher power meant lower cortisol and anxiety, partly mediated by sense of control (study 2). Sample sizes and effect sizes were not seen.

**Empirical standing.** The Sherman result is observational and cross-sectional; selection into leadership cannot be separated from effect of leadership. Power-approach theory has been contested (Moskowitz 2004 comment exists; its content was not read). Whether lab power priming effects replicate was not checked here; do not assume.

**Time scale.** None found.

**Translation.** Operand: agent with rank (status s, power p). Operator: Rank to FearLevel is sign-negative with control as a plausible mediator, which is the same variable that Gerber & Wheeler (control threat) and Maier & Seligman (control detection) use. That coincidence is the most useful structural finding: control sits under three of the four couplings.

---

## 7. Maier & Seligman (2016): uncontrollability, passivity and the time scale

**Citation.** Maier, S. F., & Seligman, M. E. P. (2016). Learned helplessness at fifty: insights from neuroscience. Psychological Review 123(4): 349-367. doi:10.1037/rev0000033 (Crossref resolved; PMC4920136).

**Their vocabulary.** Passivity as unlearned default; dorsal raphe nucleus (DRN) serotonin; prelimbic medial prefrontal cortex; control detection; immunization.

**Numbers `[read]`** (first half of PMC text; no formal effect sizes, no CIs, no p-values seen):
- Passivity and anxiety after uncontrollable stress "lasts for a few days"; 5-HT1A desensitisation recovers within 3 days.
- Immunization from prior control: "quite enduring, but perhaps not permanent"; control experienced 7 days earlier still protected, including against social defeat.
- Prelimbic-DRN plasticity "require several hours". Rodents learn to escape by trial 2 or 3. Original dog study: 64 shocks, tested 24 hours later; about two-thirds of the inescapable group failed to escape versus about 90% of controls.
- Claim: "it is the presence of control, not the absence of control, that is detected by prelimbic medial prefrontal circuits."

**Empirical standing.** Animal lesion, inactivation and tracing data; mechanism of detection admitted unknown. A 2021 commentary (found by search, not read) disputes the "unlearned" claim. Human evidence is thin and mostly analogical.

**Translation.** The only paper here with explicit time scales on a drive-like state: hours to establish, days to decay, a week or more of protection. Operand: agent with a control-belief state c. Operators: Uncontrollable(stressor) lowers c with decay on the order of days; Control(experience) raises resistance with a longer tail. Cross-species; do not transfer numbers to humans.

---

## 8. Verduyn & Lavrijsen (2015): how long emotions last

**Citation.** Verduyn, P., & Lavrijsen, S. (2015). Which emotions last longest and why: the role of event importance and rumination. Motivation and Emotion 39: 119-127. doi:10.1007/s11031-014-9445-y (Crossref gives online date 2014-10-31).

**Numbers `[read]`.** Retrospective questionnaire, 27 emotions, about 233 Dutch-speaking students (mean age 17.02; sample size from a press-coverage search result, the PDF text read here gives mean age only). Pooled median duration: 2 h if the end is "first return to baseline", 5 h if "permanent return". Women's median 5.04 h versus men's 2 h (pooled across definitions as printed). Event importance and rumination together explained 43% of between-emotion variability in duration (13% beyond emotion intensity). Event importance r = .59 and .57; rumination r = .36 and .56 (the two definitions). Table 1 (pairwise tests) shows anger (long group) lasting longer than irritation, fear and shame (short group). Per-emotion medians sit in Figure 1, which could not be extracted; press reports give sadness about 120 h, hatred about 60 h and joy about 35 h (secondary, unchecked as medians or means).

**Standing.** Retrospective recall of episodes; the authors tested a recent-episode subset and event importance still held (B = .12, p = .036). Self-report, adolescents.

**Translation.** Gives a decay scale for a single emotion, not for a coupling. Useful as the default time constant for the anger or fear state that a coupling would feed: fear and irritation decay in a couple of hours, anger and sadness take longer, and rumination is the multiplier.

---

## Table: coupling, magnitude, time scale, evidence grade

| Coupling | Best magnitude found | Time scale | Source type | Grade |
|---|---|---|---|---|
| Exclusion to need threat | d about -1.36 immediate; about -0.76 last measure | minutes; recovery 5-10 min or longer | meta-analysis, k = 120 [read] | strong, heterogeneous |
| Exclusion to mood / self-esteem | d = -0.50 / -0.70 | not given | meta-analysis, 88 [abstract] | moderate, contested |
| Exclusion to aggression | d = 0.41 (k = 19); r = 0.38 (k = 92, unverified) | not given | meta-analyses [abstract] | moderate, thin behavioural base |
| Fear to affiliation | proportions only (63% vs 33% unconfirmed) | minutes (unconfirmed) | experiments [abstract] | moderated by sex, utility |
| Frustration to anger/aggression | none found | none found | review, verbal | not quantified |
| Power/status to fear | cortisol and anxiety lower in leaders, no d seen | none | observational [abstract] | weak causal |
| Uncontrollability to passivity | none formal | hours onset, days decay, 7+ days protection | animal review [read] | mechanistic, rodent |

## What exists versus what does not

**Exists.** Large-sample effect sizes for exclusion on needs, mood and aggression. A structural hint that control is the common mediator. One animal time scale for uncontrollability. A decay prior for emotion states (hours).

**Does not exist (in what was found).** (1) A coupling coefficient or lag between two drives with a confidence interval. (2) Any quantified frustration to anger edge. (3) Any fear to affiliation meta-analysis or dose-response curve. (4) A status to fear magnitude with causal identification. (5) A longitudinal or experience-sampling dataset that tracks two drives over time within people, which is what a dynamical coupling needs. The sources are between-condition snapshots.

## Datasets worth chasing (access not verified)

- Hartgerink's meta-analysis data and code (PLOS ONE data statement not read; likely on OSF or Figshare). Variables: study-level d by measure type, duration, players. Could test exclusion to need decay across first and last measures.
- Experience-sampling work on within-person emotion dynamics, as the only route to real coupling lags (pointer only; none located this session).

## Unconfirmed

- Schachter 1959 numbers (20/32, 10/30) and waiting time.
- Page ranges for Gerber & Wheeler, Gump & Kulik, Rofé, Rofé & Lewin, Sherman, Magee & Galinsky (Crossref DOI resolution done; page ranges from memory in places).
- Quarmley k = 7 and k = 15 rows and sign conventions; the 92-study Chinese meta-analysis (title, authors).
- Verduyn per-emotion medians and exact N; whether the PDF's 2 h / 5 h medians are pooled across all 27 emotions.
- Hartgerink's second-hand recovery claims (5-10 min; 45 min for high social anxiety) and the -0.73 versus -0.76 inconsistency.
- Gump & Kulik effect sizes and N; Sherman effect sizes and N; Berkowitz full text; Bettencourt & Miller frustration-specific values; the Moskowitz 2004 critique content.
- Whether the Maier & Seligman second half contains additional timing or human data.
- Kulik & Mahler's hospital roommate work: search failed; not cited.
