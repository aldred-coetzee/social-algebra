# Prior work 097: Cantoni, Yang, Yuchtman & Zhang 2019, "Protests as strategic games"

Direction: D589 (kind: deep-read). Date: 2026-10-29. Strand: social-algebra. From: 089.

**Question.** Are turnout decisions in a protest strategic complements or substitutes, with the design and estimates exactly; and does that decide whether a monotone (increasing) threshold map F is admissible at crowd scale?

## Method and provenance

- **[read]** = I fetched and read the primary text in full myself. The text is the published version (Quarterly Journal of Economics 134(2): 1021-1077), CC BY-NC 4.0, from LSE Research Online (`https://researchonline.lse.ac.uk/id/eprint/124819/1/qjz002.pdf`; fetched, `pdftotext`, read from abstract through conclusion). The OUP and Harvard URLs returned 403 to curl; the J-PAL copy returned an HTML page, not a PDF. The LSE copy worked.
- **Not read:** the Online Appendix (Tables A.1-A.12, Figures A.1-A.8, Appendix B on the benchmark models). Where the paper's main text cites an appendix result, I say "per the text" and tag it [read: main text only]. Figures I-VIII are images; I read their captions and the surrounding text, not the plotted values. Nothing from the appendix feeds any equation here.
- **Replications and follow-ups: searched 2026-10-30** (one web search plus Crossref). No direct replication with a new sample or protest turned up; that is a search result, not proof that none exists. One theoretical follow-up exists: Shadmehr, M. (2021), "Protest Puzzles: Tullock's Paradox, Hong Kong Experiment, and the Strength of Weak States", *Quarterly Journal of Political Science*, doi:10.1561/100.00019038 (title and author confirmed at Crossref; content not read, [sa]). It is the published form of the "Shadmehr (2018)" working paper the authors cite.
- DOI 10.1093/qje/qjz002 confirmed at Crossref (title, four authors, QJE 134(2), pp. 1021-1077, published online 21 Jan 2019, CC BY-NC 4.0 licence).

**Citation.** Cantoni, D., Yang, D. Y., Yuchtman, N., & Zhang, Y. J. (2019). Protests as strategic games: experimental evidence from Hong Kong's antiauthoritarian movement. *Quarterly Journal of Economics* 134(2): 1021-1077. doi:10.1093/qje/qjz002. AEA RCT registry AEARCTR-0001423.

## Headline

**[read]** In one framed field experiment on one protest, subjects who were pushed to expect *more* turnout by others became *less* likely to attend, and subjects pushed to expect *less* became *more* likely. The authors' own words: "we consistently find evidence of strategic substitutability" and "protests are not generically games of strategic complements". They do not claim substitutes everywhere: "we do not claim that protests are always games of strategic substitutes, but that models of protest turnout must allow for the possibility of strategic substitutability." So a monotone-increasing F (strategic complements, as in Granovetter 1978 and Kuran 1989) is **not admissible as a universal assumption** at crowd scale; it may hold in some settings (the paper names one-shot regime-toppling events) and the sign is a property of the setting, not of the person.

## 1. Setting, scale and sample [read]

- **Scale: crowd (mobilisation).** One outcome: did the subject attend the 1 July 2016 march in Hong Kong. Plus beliefs about others' turnout.
- **The group whose size matters is two groups.** (a) The reference group in the information treatment: other subjects in the study (HKUST students; 17% "planned to participate"). (b) The whole protest: actual turnout was "only 26,000 people overall" against subjects' average prior of 155,153 and posterior 142,684. Of the experimental sample, 3% attended.
- **Sample.** Email to all HKUST undergraduates on 24 June 2016; 1,741 completed (19.1% response rate); 1,576 Hong Kong "natives"; 1,303 completed Part 2 (30 June); **1,234 completed Part 3 (15 July)** and form the analysis sample. Treatment 833, control 401 (two-thirds / one-third). Mean payment about HK$205 (about US$25) for Part 1, HK$25 each for Parts 2 and 3.
- **Group-size and composition content in the paper.**
  - Size enters only as the believed turnout P_-i (the reference group, a percentage of study subjects, and total turnout of all Hong Kong citizens). The paper varies belief about size; it does not vary actual group size.
  - Beliefs of success and of crackdown both rise with hypothetical protest size, from 10,000 to 1,250,000 (Figure I, described in text; values not read). That is the paper's own evidence that complement-forces and substitute-forces coexist.
  - Composition: the sample is university students (chosen because "students' importance in Hong Kong's democratic movement"), 55% male in the control group, mostly nonreligious (78%). Composition effects are tested only through a prosociality index and "ideologically more extreme friends" (both [read: main text only]).
  - Past marches: 2003 about 500,000; 2012 up to 400,000; 2008 low 17,000; 2016 "under 100,000 participants" (paper's wording, section II.B) and "only 26,000 people overall" (section IV.A). Turnout is important for success per Hong Kong commentary (cited in a footnote), which is the paper's own motivation for treating size as relevant.

## 2. Design, exactly [read]

Three online parts, all with incentivised belief elicitation (HK$10 bonus for a guess within 2 percentage points; within 10% for total turnout).

| Part | Date | What |
|---|---|---|
| 1 | 24 Jun 2016 | Own plan (Box I: Yes / not sure more likely than not / not sure more unlikely / No). Prior belief about % of study subjects planning to attend ("planned", Box II). Prior belief about % who will actually attend ("actual", Box III). Prior belief about total turnout (Box IV). |
| 2 | 30 Jun 2016 | Random 2/3 treated: reminded of their own prior about others' planned participation and told "the true percentage of survey participants who plan to attend the July 1 march is 17%" (Box V). All reminded of Part 1 answers on actual participation (Box VI), then re-elicited (Box VII). |
| 3 | 15 Jul 2016 | "Did you attend the July 1, 2016 March?" (self-report). |

- "Planned" = answered Yes or "Not sure yet, but more likely than not". 16.9% of all Part 1 subjects, rounded to 17%. Mean prior about others' planned participation 15.8%, SD 15.8 points. Mean prior about others' actual 13.8%; correlation of the two priors 0.83.
- **Identification idea.** The information (17%) is above some subjects' priors and below others', so it moves beliefs in opposite directions by prior. The authors split at 17% (priors below: 873 subjects; above: 361), or pool with the treatment coded -1 for priors above 17% ("direction adj.") so the effect is monotonic.
- Priors are not randomised. The authors say so (footnote 28) and test it with predicted vs residual priors (Table V).
- Balance: of 49 variables in Appendix Table A.1, 8 differ at 10% [read: main text; footnote 29 says 8 of 49 at the 10% level, section IV.D says 6 of 47 "subject characteristics elicited in Part 1" at the 5% level. The thresholds differ, so 8 vs 6 is not a contradiction; why the base is 49 in one place and 47 in the other is not explained in the main text]. Controlling for each interaction "leaves our treatment effect estimates practically unaffected".

## 3. Estimates, exactly [read]

All coefficients are in percentage points. Standard errors in brackets (as printed). Stars as printed: * 10%, ** 5%, *** 1%.

**First stage (Table III, Panel A): effect on posterior belief about % of study subjects who will actually attend.**
- Pooled, direction-adjusted: **5.891*** [0.567]**.
- Priors below 17%: **+4.457*** [0.545]**; priors above 17%: **-9.459*** [1.413]**. Equality rejected, p < .001.
- Control-group DV mean 14.04 (SD 14.10). Observations 1,234 / 873 / 361.
- With controls (Panel B): 6.119, 4.638, -10.120. Trimmed 5%/5% (Panel C): 5.144, 4.279, -7.568.
- Total turnout belief (columns 4-6): pooled +11,423.9* [5,988.6]; below +13,198.0** [6,541.3]; above -7,013.5 [13,108.6], not significant. The paper calls this "suggestive evidence".

**Reduced form (Table IV, Panel A): effect on own attendance (percentage points, outcome 0/100).**
- Pooled, direction-adjusted: **-2.713*** [0.765]**.
- Priors below 17%: **-2.105* [1.182]**; priors above 17%: **+6.373*** [1.873]**. Equality rejected, p < .001.
- Control-group DV mean 2.743 overall; **3.472 for priors below; 0.885 for priors above**. Observations 1,234 / 873 / 361.
- With controls (Panel B): -2.151**, -2.066*, +7.106***. Trimmed (Panel C): -2.467***, -2.230*, +5.711***.
- Persuasion rate (DellaVigna-Gentzkow) among priors above: 6.43%. Check: 6.373 / (100 - 0.885) = 6.43. Consistent. For comparison the paper says the findings of Gerber & Green (2000, *APSR* 94: 653-663, doi:10.2307/2585837) "imply" 1% for impersonal GOTV mail and 15.6% for door-to-door (footnote 40); the persuasion-rate formula is DellaVigna & Gentzkow (2010, *Annual Review of Economics* 2: 643-669, doi:10.1146/annurev.economics.102308.124309). Both confirmed at Crossref, not read; the 1% and 15.6% are the authors' figures, [sa] as to Gerber & Green.

**Two-stage (Table VI, Panel A): own attendance on posterior belief, instrumented by treatment.**
- Pooled: **-0.553*** [0.177]**. Priors below: **-0.468** [0.236]**. Priors above: **-0.654** [0.264]**. Equality p = .585.
- With controls: -0.554***, -0.447*, -0.660***. Trimmed: -0.607***, -0.514**, -0.754**.
- Readable as: about half a percentage point lower own attendance per percentage point higher believed attendance of others. The authors warn: "one should not interpret the two-stage estimates too literally" because the treatment also moved beliefs about total turnout, so the exclusion restriction is not clean ("we cannot estimate the 'pure' causal effect").
- My arithmetic check: reduced-form / first-stage gives -0.47 (below) and -0.67 (above), matching the printed -0.468 and -0.654 to rounding. For the pooled column, -2.713 / 5.891 = -0.46, not the printed -0.553; the pooled 2SLS includes an extra control interaction (table note), so the ratio need not match. I did not reproduce this.

**Heterogeneity (Table V).** Treatment effect on attendance grows with distance of the prior from 17%: Treatment x prior beliefs +0.284*** [0.068] (reduced form); first stage -0.430*** [0.059]. Both still hold using only the residual (unexplained-by-observables) part of the prior (0.246*** and -0.441***).

**Other checks [read].** Randomisation inference (10,000 draws) gives p-values "very similar" to conventional ones. Control-group naturally varying beliefs also correlate negatively with own attendance (Appendix Figure A.6, text only; the authors caution it is confounded with belief accuracy). The treatment explains more variation in attendance than economic preferences, personality, cognitive ability, background or economic status (Appendix Table A.7, text only).

## 4. Equations stated exactly [read]

The benchmark model the authors reject (Section V.A):

    U_i = 1[P_i = 1] ( V_i(P_-i, S(P_-i)) - C_i(P_-i, S(P_-i)) )

with P_-i the participation of others, S protest success. Assumptions: dS/dP_-i > 0; dV/dS > 0; dV/dP_-i > 0; dC/dS < 0; dC/dP_-i < 0. "All of these generate a common prediction: if an individual believes that the turnout of others will be greater, she is unambiguously more likely to turn out to a protest herself."

The three substitute-sources they add (Section V.B), each flagged by them as suggestive and not identified:
1. Threshold public good: V_i = V_i(S(P_-i), phi(P_-i)), with phi increasing in P_-i below the point where the good is produced and decreasing around the point where one's own turnout is "no longer needed".
2. Crackdown cost: C_i = C_i(pi(P_-i) x c_i(P_-i), S(P_-i)), with dc_i/dP_-i < 0, dS/dP_-i > 0, **d pi/dP_-i > 0** (crackdown probability rises with size). dC/dP_-i "may be positive or negative".
3. Signalling value: V_i = V_i(S(P_-i), phi(P_-i), theta_i(P_-i)), dV/dS > 0, d phi/dP_-i < 0 (over some range), **d theta_i/dP_-i < 0** (when P_-i is small enough). Follows Bénabou & Tirole (2011), "Laws and Norms", NBER Working Paper 17579 (doi:10.3386/w17579; confirmed at Crossref, not read).

The paper gives no solved equilibrium, no threshold distribution, no dynamic law and no fitted structural model. The only estimated quantities are the reduced-form, first-stage and two-stage coefficients above.

## 5. Mechanism evidence [read: main text only]

- Public good: a prosociality index (altruism, reciprocity) correlates with attendance, "unconditionally, as well as conditional on treatment status, posterior beliefs... and on subjects' own antiauthoritarian ideology" (Appendix Table A.12; not read).
- Crackdown: subjects believe both success and crackdown probability rise with protest size (Figure I; values not read).
- Signalling: in a 2017 follow-up survey, 45% of participants gave "Being politically active is an important component of my identity"; identity was the second most frequent answer (27 of the 59 protest participants asked, footnote 50); the most frequent was "I believed the march would produce political change" (28 of 59). The 2017 sample included some 2016 subjects and additional respondents, so it is not the experimental sample. Treatment-group attenders with high priors had more antiauthoritarian friends than control attenders (Appendix Figure A.8; not read).
- Mechanisms the authors looked for and did **not** find: moderates dropping out on positive updating (Shadmehr & Bernhardt 2011; Myatt 2017). Pivotality (Shadmehr 2018, a working paper in the paper's references; published as Shadmehr 2021, see Method) was not measured. Cited works: Shadmehr & Bernhardt 2011, *APSR* 105: 829-851, doi:10.1017/S0003055411000359; Myatt 2017, "A Theory of Protest Voting", *Economic Journal* 127: 1527-1567, doi:10.1111/ecoj.12333 (both confirmed at Crossref, not read).
- The authors say plainly that the mechanisms are "suggestive" and "we cannot conclusively identify specific mechanisms".

## 6. Scope limits stated by the authors [read]

- "Even in the same context we study... at a different level of protest participation the causal effect of beliefs about others' turnout on one's own could differ—indeed, it may even flip signs."
- Substitutability "most likely during stages of a political movement when the public goods component of a protest looms large relative to a movement's ultimate success." It is **not** expected in one-shot events like the Arab Spring: "One-shot protests are more likely to exhibit strategic complementarity."
- The crackdown source is "unlikely to be present in settings where protests are patently illegal"; there a crackdown is "essentially guaranteed" and larger crowds lower individual cost, which "push[es] toward strategic complementarity".
- The signalling source "may be less relevant in one-shot events aimed at toppling a dictator".
- Hong Kong has "basic rights of association and expression" protected (their wording); small protests are tolerated.
- Dynamics: the protest is part of a series; "there are dynamic considerations among protesters, learning among protest participants and nonparticipants, and potentially important cross-protest spillovers".

## 7. Consent versus manipulation

**[read]** The intervention gave subjects *truthful* information (17% was the real Part 1 figure) that they could use or ignore; it was delivered to paid participants who had agreed to a three-part survey. It is a belief nudge, not a covert incentive. Two caveats from the text: the recruitment email "did not explicitly mention our interest in political attitudes" (footnote 23); and the treatment group was reminded of its own prior alongside the figure, which the authors say may act as an anchor (footnote 22). The paper reports IRB approvals (Munich, Stanford, Berkeley, HKUST). Whether subjects were debriefed is not stated in the main text: **Unconfirmed**. I would class this as consent-compatible informational influence of low strength, but the paper does not discuss ethics beyond the approvals.

## What this decides for the algebra

1. **Is a monotone threshold map F admissible at crowd scale?** Not as a universal axiom. In this data the sign of the effect of believed others' turnout on one's own is negative (-0.47 to -0.65 percentage points of own turnout per point of believed turnout), the opposite of Granovetter/Kuran's assumption. It is admissible only as a **setting-dependent** form with a sign parameter, or as the sum of several terms with opposite-signed derivatives (complement from success and crowd-cost; substitute from public-good saturation, crackdown, signalling).
2. **The sign is not a drive of the person.** The paper's own mechanisms are properties of the situation (is there a threshold good; is the regime tolerant; is the movement ongoing) plus a trait (prosociality, identity). That is a cue for the algebra to carry F as a *situation-indexed* map, not a person-indexed one.
3. **Measurement.** The number that can be taken from this paper as data is the pair of (first stage, reduced form) coefficients, per percentage point; the 2SLS ratio is not a clean structural elasticity (authors' own warning).
4. **n.** Size is represented only through belief; no result here says how the effect changes with actual n. The only within-paper size evidence is the elicited success/crackdown curves (Figure I, not read) and the contrast between a 26,000-person event and beliefs of about 143,000.

## Unconfirmed

- Any replication, failed or successful, of strategic substitutability in other protests. Searched 2026-10-30; none found (only Shadmehr 2021, a theory paper). Absence of a hit is not absence.
- Appendix values: Figure I numbers; Tables A.1-A.12; Appendix B model derivations. Not read.
- Whether the published version differs from NBER w23110. The working paper now exists at Crossref: Cantoni, Yang, Yuchtman & Zhang (2017), "Are Protests Games of Strategic Complements or Substitutes? Experimental Evidence from Hong Kong's Democracy Movement", NBER WP 23110, doi:10.3386/w23110. Its content was not compared.
- Debriefing of subjects. Not stated in main text.
- Why the balance base is 49 variables in footnote 29 and 47 in section IV.D. The 8-vs-6 difference is explained by the 10% vs 5% thresholds; the base is not.

## Does it reduce to a drive basis?

**Partly, and the part that does not reduce is the headline.**

Reduces to drives of persons (in the paper's own mechanisms): the signalling term theta_i is an identity or status-display motive (45% of 2017 attenders cited identity); the public-good term depends on prosociality (a trait index); crackdown cost is a threat/fear term. These are person-level quantities that could be read as drives (affiliation or status, care, fear) with magnitudes that vary by person.

Does **not** reduce:
- **The sign of F.** Whether others' turnout raises or lowers own turnout comes from the structure of the situation: is the good a threshold public good (saturates), does the regime punish size, is the series ongoing. A drive on the person does not carry that sign. The same person under a "patently illegal" regime is predicted by the authors to flip to complement. So the sign needs a *situation* operand (regime tolerance, movement stage, threshold), which is not a drive of a person or a group.
- **Beliefs about others' behaviour as the input.** Everything runs through P_-i as *believed*. The algebra would need a belief operand (or a mapping from group state to a belief), which is not a drive.
- **The dynamic spillover across protests** (the authors' stated future work).

Working-hypothesis verdict: drives of persons give the *magnitudes* of three of the terms; they do not give the *sign structure*. Evidence here is consistent with drives plus situation, not drives alone. One protest cannot test the hypothesis for other types of crowd.

## What does it predict or control, and how well?

- **Outcome predicted/steered: individual attendance at one march**, 0/1, self-reported two weeks later, by students in one university.
- **Steering effect.** Truthful information about others' plans moved attendance by about **-2.1 points** (priors below; only 10% significant), **+6.4 points** (priors above; 1%), pooled direction-adjusted **-2.7 points** (1%). Against a base attendance of 3.5% (priors below) and 0.9% (priors above), +6.4 points is a very large relative change, but the baseline is tiny and the absolute counts are small. Persuasion rate 6.43% in the above group.
- **Out-of-sample evidence: none in the paper.** There is one protest, one year, one sample. No holdout, no second protest, no forecast tested against later data. The authors' own aggregate belief prediction failed: subjects expected about 143,000, actual about 26,000 (which they attribute to an announcement on the morning that a leader would not march, footnote 30; not tested).
- **Effect sizes and fragility.** The below-17% reduced-form effect is only at 10% (SE 1.182 on -2.105); with controls -2.066 (10%), trimmed -2.230 (10%). The above-17% group is 361 subjects. 19.1% response rate. Attendance is self-reported. The two-stage estimate is not a clean elasticity (authors' own words). The mechanisms are suggestive only.
- **Failures and negatives.** No evidence found for Shadmehr-Bernhardt or Myatt-type mechanisms. Beliefs about total turnout moved significantly only in the below-prior group (the above-prior total-turnout effect is not significant). Authors say results may flip sign at other turnout levels.
- **What it controls.** Not the crowd outcome. It shows a lever (publishing a figure for others' plans) that moves individuals in a setting-dependent direction, and its persuasion rate (6.43%) sits between impersonal mail (1%) and door-to-door visits (15.6%) as the paper cites them, so it is a moderate lever on a tiny base. Nothing here says what the lever does to total turnout; with strategic substitutes, publicising a high figure may *reduce* turnout, which is a prediction of this paper and untested at crowd scale.

## Validation log (2026-10-30)

- ✓ Cantoni, Yang, Yuchtman & Zhang 2019, QJE 134(2): 1021-1077, doi:10.1093/qje/qjz002. Crossref: title, four authors, volume, issue, pages, CC BY-NC 4.0 all match. LSE PDF re-fetched and read by the validator; every number in sections 1-3 (sample counts, priors, Tables III, IV, V, VI incl. Panels B/C, DV means, persuasion rate 6.43%, equality p = .585), the Section V equations and assumptions, and every quoted phrase checked against the text and found as written. [read] tags stand.
- ✎ Balance count: "the text is inconsistent" was wrong; 8 of 49 is at 10% and 6 of 47 is at 5%. Only the 49 vs 47 base is unexplained. Fixed in section 2 and Unconfirmed.
- ✎ 2017 follow-up survey: "28 of 59 vs 27 of 59" was unlabelled; now says identity was 27 of 59 (second), political change 28 of 59 (first), per footnote 50, and that the 2017 sample is not the experimental sample.
- ✎ "Not searched" for replications: searched; no direct replication found; Shadmehr 2021 QJPS (doi:10.1561/100.00019038, Crossref ✓, not read) added as the published form of the cited Shadmehr 2018 working paper.
- ✓ NBER WP 23110 (2017), doi:10.3386/w23110: existence, title and authors confirmed at Crossref (previously [sa] from a search title). Content not compared.
- ✓ Granovetter 1978, AJS 83: 489-515, doi:10.1086/226707 (Crossref; not read; cited only as the complements assumption, which is how the paper's footnote 1 uses it).
- ✓ Kuran 1989, Public Choice 61: 41-74, doi:10.1007/BF00116762 (Crossref; not read; same use).
- ✓ Gerber & Green 2000, APSR, doi:10.2307/2585837 (Crossref; not read; 1% / 15.6% are the QJE authors' figures, [sa]).
- ✓ DellaVigna & Gentzkow 2010, Annu. Rev. Econ., doi:10.1146/annurev.economics.102308.124309 (Crossref; not read). The 6.43% arithmetic re-checked from the QJE table values.
- ✎ Bénabou & Tirole 2011: added title "Laws and Norms", NBER WP 17579, doi:10.3386/w17579 (Crossref ✓, not read).
- ✓ Shadmehr & Bernhardt 2011, APSR 105, doi:10.1017/S0003055411000359; Myatt 2017, EJ 127, doi:10.1111/ecoj.12333 (Crossref ✓, not read; DOIs added). The "not found in our setting" claim matches footnote 51.
- ? Online Appendix (Tables A.1-A.12, Figures A.1-A.8, Appendix B): not read; claims resting on it stay tagged as main-text-only.
- ✗ Fabrications: none found.

Sources opened: 1 primary text read (the QJE paper, LSE copy), plus 12 Crossref records and 1 web search.

Verdict: The note is accurate. Every load-bearing number and equation was checked against the published text and holds. The fixes are minor: a false "inconsistency" in the balance counts, an unlabelled pair of survey counts, and missing DOIs and follow-up literature. The only things that may feed an equation are the Table III/IV/VI coefficients and the Section V utility forms, and all of them are [read]. The note's own warning stands: the 2SLS ratio is not a clean structural elasticity.

## Cross-checks (2026-10-30)

Checked against the other files in `docs/prior-work/` by name, DOI, equation and number (grep, 2026-10-30). Not re-verified against the primary text beyond what the validation log above records.

**Agreements**
- The paper's citation (QJE 134(2): 1021-1077, doi:10.1093/qje/qjz002) matches 089's citation, which gives the same venue, volume and pages and the same DOI.
- The sign finding (others' turnout lowers own turnout in this experiment) matches 089's abstract summary and 099's "Not supplied" and "Failures and caveats" paragraphs, which both cite Cantoni et al. as finding strategic substitutes.
- The monotone-F form that the paper's benchmark assumes (complementarity, dS/dP > 0 and related signs) matches the monotone threshold map in 066 section 1 (F non-decreasing, least fixed point), and the Granovetter-Kuran shape described in 089.
- 099 and 089 both say Kuran's model rests on complementarity; 097 section 4 says the same for the benchmark, so the three files agree that the assumption is the one being challenged.

**Unresolved (not settled here; both claims recorded, the two files are not edited)**
- Scope of the substitutes finding. 089 (section "Cantoni et al." item, and the verdict paragraph) and 099 (section on "Not supplied by this paper", and "Failures and caveats" item 2) describe the result as the opposite of the complementarity assumption, and 089 calls it "the most direct challenge to the monotone-F assumption". 097 section "Scope limits stated by the authors" and section "What this decides for the algebra", item 1, record that the authors explicitly say "we do not claim that protests are always games of strategic substitutes", that one-shot events are predicted to show complementarity, and that the sign is setting-dependent. The two readings differ on whether the result is general or setting-bound. Unresolved: 097's validation log checked 097 against the paper, not 089 or 099 against 097.
- Provenance of the Cantoni claim in 099. 099 cites Cantoni et al. as "[sa from 089]". 097 now has the primary text read. 099 needs its tag updated if it is re-read; this is a stale tag, not a disagreement on content.

**Not a contradiction, recorded so it is not read as one**
- 097's signalling equation cites Benabou and Tirole 2011, "Laws and Norms" (NBER 17579). The Benabou-Tirole papers in 021, 036 and 038 are 2003, 2004, 2005 and 2006 papers, with different equations. No overlap in the equations.
- NBER w23110 (the 2017 working paper) is named in 089 as the source of the abstract. 097 records its content as not compared. Nothing in 089 contradicts 097 on this.

Ledger lines (provenance, dup_of_file, and the read/sa split) were returned to the orchestrating session in structured form, not written to any other file.
