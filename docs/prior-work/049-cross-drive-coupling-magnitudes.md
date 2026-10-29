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

**Citation.** Gerber, J., & Wheeler, L. (2009). On being rejected: a meta-analysis of experimental research on rejection. Perspectives on Psychological Science 4(5): 468-488. doi:10.1111/j.1745-6924.2009.01158.x (Crossref resolved, pages confirmed). Rebuttal in the same issue: Baumeister, R. F., DeWall, C. N., & Vohs, K. D. (2009). Social rejection, control, numbness, and emotion: how not to be fooled by Gerber and Wheeler (2009). PPS 4(5): 489-493. doi:10.1111/j.1745-6924.2009.01159.x; rejoinder Gerber & Wheeler (2009) PPS 4(5): 494-495, doi:10.1111/j.1745-6924.2009.01160.x (both Crossref resolved, not read).

**Their vocabulary.** Needs account versus numbness account; belonging, control.

**Operators / equations.** None. Numbers `[abstract read, Crossref record]`:
- Mood d = -0.50; self-esteem d = -0.70; no drop in arousal and no flattening of affect.
- Belonging d = 0.69; control d = 1.16 (frustrated by rejection).
- Antisocial responding when measures contrast belonging and control: d = -1.17; prosocial responding when control can be restored: d = 1.21.

**Theorems or derived predictions.** Aggression after rejection reflects attempts to regain control.

**Empirical standing.** The rebuttal says the sample is biased (as reported in this file's first pass; the rebuttal was not read in validation). A later paper (Quarmley et al., PMC9519812, as quoted by a search summary) notes that only 16 of 40 included studies measured actual aggressive or prosocial behaviour, so the aggression conclusion rests on thin behavioural evidence.

**Translation.** A competing mediator hypothesis: exclusion to control-threat to aggression, rather than exclusion to anger to aggression. For the algebra, a three-node chain with a restoring path, not a single edge.

---

## 3. Quarmley et al. (2022): rejection to aggression and prosocial behaviour

**Citation.** Quarmley, M., Feldman, J., Grossman, H., Clarkson, T., Moyer, A., & Jarcho, J. M. (2022). Testing effects of social rejection on aggressive and prosocial behavior: a meta-analysis. Aggressive Behavior 48(6): 529-545. doi:10.1002/ab.22026 (Crossref resolved).

**Numbers `[abstract read, Crossref record]`.** Three random-effects meta-analyses, combined N = 3,864. Rejection potentiated aggressive behaviour: k = 19, d = 0.41, p < .0001. Rejection attenuated prosocial behaviour: k = 7, d = 0.59, p < .0001 (so d is reported as a positive magnitude of a reduction). Where participants could choose to behave prosocially or aggressively, the aggression effect held: k = 15, d = 0.71, p < .0001. The authors call these "medium effects", conclude rejection is a robust elicitor of aggression, and cast doubt on a rejection-to-prosocial account.

**Related, unverified.** A 2023 Chinese-language meta-analysis (Acta Psychologica Sinica 55(12)) reports 92 studies, r = 0.38, 95% CI [0.34, 0.41], no publication bias `[search summary only; title and authors not captured]`. A 2022 study reported that neither anger nor hostility mediated the ostracism-aggression link (mediator CIs including zero) `[search summary only]`.

**Translation.** The exclusion to aggression edge has a magnitude (d about 0.4, r about 0.4) but anger as the mediator is contested.

---

## 4. Berkowitz (1989): frustration to aggression, reformulated

**Citation.** Berkowitz, L. (1989). Frustration-aggression hypothesis: examination and reformulation. Psychological Bulletin 106(1): 59-73. doi:10.1037/0033-2909.106.1.59 (Crossref resolved). PubMed 2667009.

**Their vocabulary.** Frustration, interference with expected goal attainment, hostile (emotional) aggression, negative affect, attributions, cognitive-neoassociationistic model.

**Operators / equations.** None. The paper is verbal. `[from PubMed abstract; the quoted sentence checked verbatim]`: the 1939 proposition covers only interference with an expected goal on hostile aggression; frustrations create aggressive inclinations to the extent they arouse negative affect; "Frustrations can create aggressive inclinations even when they are not arbitrary or aimed at the subject personally"; attributions shape how unpleasant the thwarting is.

**Theorems or derived predictions.** Qualitative: aggression is driven by negative affect from any aversive event (frustration being one), so frustration to aggression runs through an affect variable.

**Empirical standing.** The abstract says results are mixed though many studies support the core. No effect size or time constant is stated in the abstract, and the full text was not read.

**Translation.** The coupling in the algebra should be Frustrate(x) to NegAffect to AggressiveInclination, with attribution as a gain on the first link. No magnitude exists in what was read. Bettencourt, B. A., & Miller, N. (1996). Gender differences in aggression as a function of provocation: a meta-analysis. Psychological Bulletin 119(3): 422-447. doi:10.1037/0033-2909.119.3.422 (Crossref resolved) is the obvious next source. A first-pass secondary summary said provocation shrinks the male-female aggression difference from d = .33 to d = .17; this was not confirmed at source (see Unconfirmed), and no frustration-specific value was found.

---

## 5. Schachter (1959), Gump & Kulik (1997), Rofé: fear to affiliation

**Citations.**
- Schachter, S. (1959). The Psychology of Affiliation: Experimental Studies of the Sources of Gregariousness. Stanford University Press. (Book; no DOI. Library records only; not read.)
- Gump, B. B., & Kulik, J. A. (1997). Stress, affiliation, and emotional contagion. Journal of Personality and Social Psychology 72(2): 305-319. doi:10.1037/0022-3514.72.2.305 (Crossref resolved, pages confirmed).
- Rofé, Y. (1984). Stress and affiliation: a utility theory. Psychological Review 91(2): 235-250. doi:10.1037/0033-295X.91.2.235 (Crossref resolved, pages confirmed).
- Rofé, Y., & Lewin, I. (1988). Social comparison or utility: an experimental examination. Social Behavior and Personality 16(1): 5-10. doi:10.2224/sbp.1988.16.1.5 (Crossref resolved, pages confirmed).
- Pointer, not read: Kulik, J. A., Mahler, H. I. M., & Moore, P. J. (1996). Social comparison and affiliation under threat: effects on recovery from major surgery. JPSP 71(5): 967-979. doi:10.1037/0022-3514.71.5.967 (Crossref resolved). This is the hospital-roommate line of work the first pass could not locate.

**Their vocabulary.** Emotional similarity hypothesis; affiliation; emotional contagion; mimicry; utility theory.

**Drives/operands.** Fear (manipulated threat of shock), affiliation (choice to wait with others, or time spent looking at a partner).

**Numbers.**
- Schachter 1959, `[from memory of the standard account, NOT confirmed by any source in this session]`: 20 of 32 high-fear participants chose to wait together versus 10 of 30 low-fear (about 63% versus 33%). The search tool itself declined to confirm these. Treat as unconfirmed.
- Gump & Kulik 1997, `[from abstract via search]`: female participants, high or low threat, partner believed to face the same or a different situation. Study 1 paired two real participants; study 2 a confederate acting calm or nervous. Affiliation measured as time spent looking at the affiliate. Threat increased affiliation, especially with partners facing the same situation; evidence of facial mimicry and of emotional contagion in self-reported anxiety. No effect sizes were seen.
- Rofé & Lewin 1988, `[abstract read, Crossref record]`: three conditions: a replication of the main features of Schachter's study, then two in which the utility of affiliation was reduced while social comparison was kept or increased (shocks said to be immediate rather than deferred; in the third, also physiological reactions projected on a screen for public comparison). Those two conditions produced a marked decrease in affiliation for males but not females.

**Operators / equations.** None exist in these papers. The coupling is a conditional proportion or a duration contrast, not a rate.

**Theorems or derived predictions.** Emotional similarity: Affiliate(x, y) rises with Fear(x) and with similarity of y's situation. Utility theory: Affiliate falls when affiliation risks embarrassment or unwanted contagion. The two predict different sign changes under the same fear, so the coupling is state-dependent, not a constant gain.

**Empirical standing.** Gump & Kulik is a conceptual-replication-style result with unknown N in what was read. Rofé & Lewin suggests the effect is moderated by sex and utility. A secondary item (Chicano and Anglo adolescents) reports a failed replication of Darley and Aronson 1966 on manipulated fear and notes variation by sex and ethnicity `[search snippet only, not read]`. No meta-analysis of fear to affiliation was found in this session.

**Time scale.** Not reported in anything found. Schachter's waiting period was a few minutes in the standard account (unconfirmed).

**Translation.** Operand: agent with fear level F and situation label S. Operator: Affiliate(x to y) with gain g(F, sim(S_x, S_y), utility). The gain's sign and size are not constants; the algebra should store it as a conditional, or hold the moderators as operands.

---

## 6. Magee & Galinsky (2008), Keltner et al. (2003), Sherman et al. (2012): status/power to fear

**Citations.**
- Magee, J. C., & Galinsky, A. D. (2008). Social hierarchy: the self-reinforcing nature of power and status. Academy of Management Annals 2(1): 351-398. doi:10.5465/19416520802211628 (Crossref resolved; pages not checked).
- Keltner, D., Gruenfeld, D. H., & Anderson, C. (2003). Power, approach, and inhibition. Psychological Review 110(2): 265-284. doi:10.1037/0033-295X.110.2.265 (Crossref resolved). Comment: Moskowitz, D. S. (2004). Does elevated power lead to approach and reduced power to inhibition? Comment on Keltner, Gruenfeld, and Anderson (2003). Psychological Review 111(3): 808-811. doi:10.1037/0033-295X.111.3.808 (Crossref resolved, not read).
- Sherman, G. D., Lee, J. J., Cuddy, A. J. C., Renshon, J., Oveis, C., Gross, J. J., & Lerner, J. S. (2012). Leadership is associated with lower levels of stress. PNAS 109(44): 17903-17907. doi:10.1073/pnas.1207042109 (Crossref resolved, pages confirmed).

**Their vocabulary / definitions `[read]` (Magee & Galinsky PDF).** Social status: "the extent to which an individual or group is respected or admired by others." Social power: "asymmetric control over valued resources in social relations." Power-approach theory (Keltner et al. 2003) `[read as restated by Magee & Galinsky]`: elevated power increases the tendency to focus on and approach rewards; low-power individuals face more social and material threats and have a primary "inhibit" response. "Whereas the powerful see mostly opportunity dancing in front of them, the powerless are more likely to see potential hazards lurking about."

**Numbers.**
- Magee & Galinsky: whole text grepped. No effect sizes, no time constants. It is a qualitative review `[read]`.
- Sherman et al. 2012 `[abstract read, Crossref record]`: real leaders (military officers, government officials) had lower cortisol and reported less anxiety than nonleaders (study 1); within leaders, higher power meant lower cortisol and anxiety, partly mediated by sense of control (study 2). Sample sizes and effect sizes were not seen.

**Empirical standing.** The Sherman result is observational and cross-sectional; selection into leadership cannot be separated from effect of leadership. Power-approach theory has been contested (Moskowitz 2004 comment exists; its content was not read). Whether lab power priming effects replicate was not checked here; do not assume.

**Time scale.** None found.

**Translation.** Operand: agent with rank (status s, power p). Operator: Rank to FearLevel is sign-negative with control as a plausible mediator, which is the same variable that Gerber & Wheeler (control threat) and Maier & Seligman (control detection) use. That coincidence is the most useful structural finding: control sits under three of the four couplings.

---

## 7. Maier & Seligman (2016): uncontrollability, passivity and the time scale

**Citation.** Maier, S. F., & Seligman, M. E. P. (2016). Learned helplessness at fifty: insights from neuroscience. Psychological Review 123(4): 349-367. doi:10.1037/rev0000033 (Crossref resolved; PMC4920136).

**Their vocabulary.** Passivity as unlearned default; dorsal raphe nucleus (DRN) serotonin; prelimbic medial prefrontal cortex; control detection; immunization.

**Numbers `[read]`** (first half of PMC text; no formal effect sizes, no CIs, no p-values seen):
- Passivity after inescapable shock is "transient, lasting for only a few days", and the paper speaks of "the passivity and increased anxiety that follows uncontrollable stressors for several days"; 5-HT1A desensitisation "recovers to normal within 3 days".
- Immunization from prior control: "quite enduring, but perhaps not permanent"; control experienced 7 days earlier still protected, including against social defeat.
- Prelimbic-DRN plasticity "require several hours". Rodents without prior inescapable shock escape at near-asymptotic latencies "by the second or third trial". Original dog work: 64 shocks, tested in a shuttlebox 24 hours later; "two-thirds of the animals from the INESC group failed to learn to escape", while "90% of the animals in both the ESC and 0 groups easily learned to escape" (escapable and no-shock groups).
- Claim: "it is the presence of control, not the absence of control, that is detected by prelimbic medial prefrontal circuits."

**Empirical standing.** Animal lesion, inactivation and tracing data; mechanism of detection admitted unknown. A 2021 commentary (found by search, not read) disputes the "unlearned" claim. Human evidence is thin and mostly analogical.

**Translation.** The only paper here with explicit time scales on a drive-like state: hours to establish, days to decay, a week or more of protection. Operand: agent with a control-belief state c. Operators: Uncontrollable(stressor) lowers c with decay on the order of days; Control(experience) raises resistance with a longer tail. Cross-species; do not transfer numbers to humans.

---

## 8. Verduyn & Lavrijsen (2015): how long emotions last

**Citation.** Verduyn, P., & Lavrijsen, S. (2015). Which emotions last longest and why: the role of event importance and rumination. Motivation and Emotion 39: 119-127. doi:10.1007/s11031-014-9445-y (Crossref gives online date 2014-10-31).

**Numbers `[read]`.** Retrospective questionnaire, 27 emotions, 233 high-school students (112 women, 118 men, 3 unreported; mean age 17.02, SD .79; N confirmed in the PDF's Participants section), 8.42 episodes per participant on average. Median duration across all emotions: 2 h if the end is "first return to baseline", 5 h if "permanent return" (main effect of definition, F(1, 1621) = 4.66, p = .03). Women's median 5.04 h versus men's 2 h (pooled across definitions as printed). Event importance and rumination together explained 43% of between-emotion variability in duration (13% beyond emotion intensity). Event importance r = .59 and .57; rumination r = .36 and .56 (the two definitions). Table 1 (pairwise tests, p < .01): sadness lasted significantly longer than all 26 others; anger lasted significantly longer than fear, surprise and shame only, and was NOT significantly different from irritation (corrected in validation: the first pass listed irritation); fear lasted significantly shorter than anxiety (t(1647) = 4.12). Only 117 of 351 contrasts were significant. Per-emotion medians sit in Figure 1; the extracted text shows bar labels up to 120 h and values of 60 and 35 h in the permanent-return median panel, consistent with press reports of sadness about 120 h, hatred about 60 h and joy about 35 h, but the label-to-emotion mapping could not be recovered from the text.

**Standing.** Retrospective recall of episodes; the authors tested a recent-episode subset and event importance still held (B = .12, p = .036). Self-report, adolescents.

**Translation.** Gives a decay scale for a single emotion, not for a coupling. Useful as the default time constant for the anger or fear state that a coupling would feed: fear and irritation are among the shortest, sadness is clearly the longest, anger sits in the undifferentiated middle (longer than fear, not distinguishable from irritation), and rumination and event importance are the multipliers.

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

- Schachter 1959 numbers (20/32, 10/30) and waiting time: book not available; still from memory.
- The 92-study Acta Psychologica Sinica 2023 meta-analysis (title, authors, r = 0.38) and the 2022 no-mediation-by-anger study: search-summary only, no title or DOI, so not citable as they stand.
- Quarmley et al.'s statement that only 16 of 40 Gerber & Wheeler studies measured behaviour: PMC bot check blocked the full text in validation too.
- Verduyn per-emotion medians (label-to-emotion mapping in Figure 1).
- Hartgerink's second-hand recovery claims (5-10 min, unnamed studies; 45 min for high social anxiety, Zadro et al.): the paper does say both, but the primary studies were not read.
- Gump & Kulik content (female participants, two studies, looking time, mimicry, contagion): no abstract was obtainable at Crossref or APA in validation, so these details rest on the first pass's search summary. Effect sizes and N also unseen.
- Sherman effect sizes and N (PNAS full text 403 in validation); Berkowitz full text; Bettencourt & Miller d = .33 to .17 and frustration-specific values; the Moskowitz 2004 critique content; the Baumeister, DeWall & Vohs rebuttal content.
- Whether the Maier & Seligman second half contains additional timing or human data.
- Kulik & Mahler's hospital roommate work: now located (Kulik, Mahler & Moore 1996, section 5) by DOI, but not read.

## Validation log (2026-10-29)

All DOIs resolved at api.crossref.org; titles, authors, volume, issue and pages checked against the records. Web search budget was exhausted during this pass, so "nothing exists" claims (no fear-to-affiliation meta-analysis; no frustration-to-anger magnitude; no ESM coupling dataset) were NOT re-tested by search and stand as the first pass's negative findings only.

- ✓ Hartgerink, van Beest, Wicherts & Williams 2015, PLOS ONE: re-fetched; N, k, d = -1.36 [-1.54, -1.18], I^2, tau^2, last-measure -0.76 / -0.73 and CI [-0.86, -0.59] inconsistency, 4.85 min, b = 0.0069, k = 19 subset, 2 of 120, N = 2,186 and the recovery sentences all confirmed [read].
- ✎ Gerber & Wheeler 2009: all d values confirmed from the Crossref abstract; pages confirmed; rebuttal now cited in full (Baumeister, DeWall & Vohs 2009) with rejoinder.
- ✎ Quarmley et al. 2022: abstract read; prosocial d = 0.59 is an attenuation and k = 15 is the free-choice set where aggression held; meaning now stated. 16-of-40 claim still unconfirmed.
- ✓ Berkowitz 1989: bibliographic record and the quoted "arbitrary" sentence confirmed verbatim on PubMed.
- ✎ Bettencourt & Miller 1996: full citation added (pages 422-447); d = .33 to .17 moved to Unconfirmed.
- ? Schachter 1959: book exists; numbers unconfirmed (unchanged).
- ✎ Gump & Kulik 1997: citation and pages confirmed; content details downgraded to unconfirmed (no abstract obtainable).
- ✓ Rofé 1984: citation and pages confirmed.
- ✎ Rofé & Lewin 1988: end page 10 added; condition description corrected to match the abstract (three conditions).
- ✎ Kulik, Mahler & Moore 1996: added as a located pointer (DOI resolved, not read).
- ✓ Magee & Galinsky 2008: citation and pages confirmed; both definitions and the "dancing in front of them" sentence re-checked verbatim in the extracted PDF; no d or r found [read].
- ✓ Keltner, Gruenfeld & Anderson 2003: citation confirmed.
- ✎ Moskowitz 2004: title, pages and author initials added from Crossref; content not read.
- ✎ Sherman et al. 2012: pages confirmed (no longer "from memory"); abstract content confirmed from Crossref; N and effect sizes still unseen.
- ✎ Maier & Seligman 2016: all quoted time scales confirmed [read]; the "about 90% of controls" line reworded to the paper's statement (90% of escapable and no-shock dogs learned to escape).
- ✎ Verduyn & Lavrijsen 2015: N = 233 is in the PDF (first pass wrongly said it was not); anger is NOT significantly longer than irritation in Table 1 (first pass wrong), corrected along with the translation; 43%/13%, r values, 5.04 h vs 2 h and B = .12, p = .036 confirmed [read].
- ? Acta Psychologica Sinica 2023 meta-analysis and the 2022 mediation study: no title, authors or DOI; left in section 3 labelled unverified and listed in Unconfirmed.
- No fabrications found; nothing deleted.

**Verdict.** The file is substantially accurate: every DOI resolves to the stated authors, venue and pages, and the headline numbers (Hartgerink, Gerber & Wheeler, Quarmley, Maier & Seligman, Verduyn) check out at source or in the published abstract. The one substantive error was in Verduyn's Table 1, where anger was said to outlast irritation; it does not, which weakens the "anger is a long emotion" prior used in the translation. Remaining soft spots are the Schachter proportions, the Gump & Kulik details, and two uncited search-summary items, all now flagged.

## Cross-checks (2026-10-29)

Direction D107 checked against the other files in this folder. Only this file was edited. Overlaps exist with 056, 053, 042, 017, 051, 055 and 041. Quarmley, Bettencourt & Miller, Rofé and Sherman et al. 2012 appear in no other file (066 and 018 mention a different Sherman, Smaldino et al. 2012).

### Agreements

- **Hartgerink et al. 2015** (here section 1; 056 section 2). Same citation and DOI. Agree on k = 120, 98 papers, N = 11,869, first-measure d = -1.36 [-1.54, -1.18], I^2 = 92.99%, tau^2 = 0.90, last-measure d = -0.76 [-0.91, -0.61] (k = 95), mean 4.85 min with b = 0.0069, p = .187, homogeneous subset k = 19 d = -2.05 [-2.44, -1.65], N = 2,186 for power, and the recovery of 5-10 min and 45 min (socially anxious) as second-hand. 056 section "Translation / operator exclude(a, b)" carries the same d -1.36 decaying to -0.76 with no identified rate, matching the translation in section 1 here.
- **Gerber & Wheeler 2009** (here section 2; 056 section 3). Same DOI and pages. Agree on 88 studies, mood d = -0.50, self-esteem d = -0.70, belonging 0.69, control 1.16, antisocial -1.17, no arousal drop. Both read the abstract only. 056 additionally records the Blackhart et al. 2009 meta-analysis (192 studies; self-esteem no different from neutral controls), which disputes the self-esteem figure. This supports this file's "contested" label for the mood/self-esteem row and is worth citing there.
- **Control as the common mediator** (here sections 2, 6, 7; 056 control-action paragraph). 056 fits the control-first reading to the same two Gerber & Wheeler numbers (1.16 against 0.69). 053 section 1 also puts control detection at the centre of Maier & Seligman. This matches the "control sits under three of the four couplings" finding here.
- **Maier & Seligman 2016** (here section 7; 053 section 1). Agree on the DOI, passivity lasting a few days, 5-HT1A recovery within 3 days, escape by the second or third trial, 64 shocks, two-thirds of the inescapable group failing against about 90% of the escapable and no-shock groups, and immunization "quite enduring, but perhaps not permanent" with protection at 7 days. 042 (Maier row) agrees on the substance: passivity is the unlearned default and control is detected in medial PFC.
- **Berkowitz 1989** (here section 4; 042 frustration-aggression entry; 017 reference list). Same DOI. All agree that frustration produces aggressive inclination via negative affect, with no magnitude. 017 and 042 give the same qualitative sign (blocked wanting to aggression through negative affect).
- **Schachter 1959 and fear to affiliation** (here section 5; 017, 042, 051). All agree the effect is qualitative, with no functional form and no numbers in hand. 042 and 051 both say Schachter was not read. 049's unconfirmed 20/32 versus 10/30 figures appear nowhere else, so nothing corroborates or contradicts them. 051 states that fear to affiliation does not depend on terror management, which fits this file's treatment.
- **Magee & Galinsky 2008** (here section 6; 055 section 4; 042). Same DOI 10.5465/19416520802211628. All three treat it as a qualitative review that gives the sign and no equation or effect size. 055 and 042 did not read it, so this file's full-text grep for effect sizes (none found) is the stronger check.
- **Verduyn & Lavrijsen 2015** (here section 8; 041). Same DOI and journal details. 041 is tagged secondary and says shame was among the shortest and guilt outlasted shame. This file does not cover shame or guilt, so there is no conflict. Its "fear among the shortest" is consistent with 041's picture of short-lived emotions.
- **Gump & Kulik 1997** (here section 5; 051, 042). All give the same bibliographic record (JPSP 72(2), 305-319). 051 notes the DOI is now resolved.

### Contradictions

1. **Gerber & Wheeler 2009, d = 1.21 (here section 2, "Numbers").**
   - 049 originally said: "prosocial responding when control **can be restored**: d = 1.21".
   - 056 section 3 says: measures that "do **not** allow for control to be restored cause prosocial responding (d = 1.21)".
   - Primary source: the Crossref abstract of doi:10.1111/j.1745-6924.2009.01158.x reads "measures that do not allow for control to be restored cause prosocial responding (d = 1.21)".
   - **Verdict: 056 is right and 049 is wrong.** The condition is reversed in 049. Where control cannot be restored, behaviour is prosocial. Where belonging and control are contrasted (control restorable), it is antisocial. The "restoring path" in the section 2 translation should be read this way, and the aggression-as-control-regain gloss still holds.
2. **Hartgerink last-measure -0.76 versus -0.73 (here section 1 and Validation log).**
   - 049 says the paper "is internally inconsistent here".
   - 056 section 2 says these are two models: the mixed-effects model with elapsed time as a predictor gives the intercept -0.76 [-0.91, -0.61], and the summary without it gives about -0.73 [-0.86, -0.59]. It records this as "not an internal inconsistency (corrected at validation)".
   - Primary source (Europe PMC PMC4449005 full text): the intercept d = -0.76 is stated for the model "including ... estimated time in seconds since completing the Cyberball game as predictor". The "-0.73" sentence is in the summary after the model "including both the time and SE as predictor". It is a different model.
   - **Verdict: 056 is right.** The two figures are not an inconsistency. 049's wording should be read as "-0.76 with the time predictor, about -0.73 in the summary model".
3. **Gump & Kulik 1997 characterisation (here section 5; 042 line on affiliation under threat).**
   - 042 describes it as a later review qualifying Schachter ("social support under stress") and tags it "[recalled]".
   - 049 describes it as two experiments (threat, same or different partner situation, looking time, mimicry and contagion).
   - Source check: the paper's title is "Stress, affiliation, and emotional contagion", and 049's description comes from a search abstract. 051 independently says it was not read. Neither 042 nor 049 holds a verified abstract.
   - **Verdict: unresolved.** 049's description is more specific and probably nearer the abstract, but it was not confirmed at source either.

### Not checked

No file other than 049 contains Quarmley et al. 2022, Rofé 1984 and Rofé & Lewin 1988, Bettencourt & Miller 1996, Sherman et al. 2012 (PNAS), Keltner et al. 2003 (beyond brief mentions in 017) or the Kulik, Mahler & Moore 1996 pointer. Those claims have no second source in this folder.

## Licences of quoted and transcribed material (2026-10-30)

No passage in this file was removed, shortened or re-attributed by the audit; all three audit items were "check" and are recorded here. Quotations are all under 60 words. No table is transcribed from a source: the coupling table (line 174) is our own summary of values taken from the sources, and Verduyn & Lavrijsen's Table 1 is described, not copied.

| Source | Licence as determined | How used |
|---|---|---|
| Hartgerink, van Beest, Wicherts & Williams (2015), PLOS ONE 10(5): e0127002 | CC BY 4.0 (PLOS default; the article's own licence line was not read) | Short restated results (d values, k); no long quotation |
| Hartgerink et al. 2015 supplementary data and code | Not determined; the PLOS ONE data statement was not read. Not accessed, not used. Read the OSF or Figshare licence before any use or redistribution | Dataset citation only (Datasets worth chasing) |
| Gerber & Wheeler (2009), Perspectives on Psychological Science | Not determined; publisher copyright presumed (abstract and Crossref record only) | Short quotation of the abstract sentence in Cross-checks; reported d values |
| Quarmley et al. (2022), Aggressive Behavior | Not determined; publisher copyright presumed (abstract and Crossref record only) | Restated numbers from the abstract |
| Berkowitz (1989), Psychological Bulletin | Not determined; publisher copyright presumed (PubMed abstract only) | One short quotation (line 83), restated claims |
| Schachter (1959), Gump & Kulik (1997), Rofé (1984), Rofé & Lewin (1988), Kulik et al. (1996), Bettencourt & Miller (1996) | Not determined; publisher copyright presumed (not read, or abstract only) | Citations and restated findings only |
| Magee & Galinsky (2008), Academy of Management Annals | Not determined; publisher copyright presumed. The file does not record how the PDF was obtained: confirm the copy was legitimate (institutional, author-deposited or open) and that a re-read is not needed | Two short definition quotations and one short passage (line 130) |
| Keltner et al. (2003), Sherman et al. (2012) | Not determined; publisher copyright presumed (abstract only) | Restated findings |
| Maier & Seligman (2016), Psychological Review (PMC full text) | Not determined; publisher copyright presumed, PMC open-access terms not checked | Short quotations (lines 151-154), restated numbers |
| Verduyn & Lavrijsen (2015), Motivation and Emotion (Springer) | Not determined; publisher copyright presumed. The file does not record how the PDF was obtained: confirm it was legitimate | Restated statistics and Table 1 findings described in prose; no table transcribed |
| Crossref records (DOIs, titles, pages, abstracts) | Facts are not copyrightable; Crossref metadata is CC0 | Citation checking |
