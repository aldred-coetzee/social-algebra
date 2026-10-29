# Prior work 087: cohesion, measurement, the cohesion-performance lags, and a feedback-loop form

Direction: D261
Date: 2026-10-29. Kind: deep-read. Merged from 24 (cohesion survey, sections 11-12), 06, 29.

## Provenance, stated first

**Read in full or at length at source [read]:**
- Moody and White (2003), *American Sociological Review* 68(1), 103-127, doi 10.1177/000312240306800105 (Crossref confirmed). Full publisher text (ASA PDF, Wayback copy; eScholarship holds a CC BY copy). I read the definitions, the graph theory, both empirical sections including Tables 1 and 2, the implications and the conclusion. I did not read Appendix A (the blocking algorithm) line by line.

**Read at source, but a secondary account of the seeds [read as secondary]:**
- MacCoun and Hix (2010), "Unit cohesion and military performance", ch. 5 of *Sexual Orientation and U.S. Military Personnel Policy: An Update of RAND's 1993 Study* (RAND; open PDF at law.berkeley.edu/files/csls/Unit_Cohesion_and_Military_Performance_Ch5_MacCoun_Hix.pdf). I read the sections on definitions and on the cohesion-performance relationship. Every statement it makes about Mullen and Copper, Beal et al., Gully et al., Oliver et al. and Chiocchio and Essiembre is **[sa]** for this file: it is a reviewer's account of those meta-analyses, not the meta-analyses.
- Leo, González-Ponce, Sánchez-Oliva, Pulido and García-Calvo (2015), *Psicothema* 27(3), 261-268, doi 10.7334/psicothema2014.247 (Crossref confirmed): a validation of a short Spanish version of the GEQ. Used only for the GEQ definition and structure as quoted from Carron et al.; **[sa]** for Carron.

**Not accessible, so [sa] or [abs] only (paywalled or blocked; I tried the DOI landing pages, Semantic Scholar's open-access field (status CLOSED for all three), a DTIC technical-report copy of Mullen and Copper (HTTP 403 / HTML error), ResearchGate (403), a Birmingham repository PDF (403) and PubMed (cookie wall)):**
- Mullen and Copper (1994), *Psychological Bulletin* 115(2), 210-227, doi 10.1037/0033-2909.115.2.210 (Crossref confirmed). Not read. No coefficient from it below is a [read].
- Beal, Cohen, Burke and McLendon (2003), *J. Applied Psychology* 88(6), 989-1004, doi 10.1037/0021-9010.88.6.989 (Crossref confirmed). Not read; abstract-level only.
- Mathieu, Kukenberger, D'Innocenzo and Reilly (2015), *J. Applied Psychology* 100(3), 713-734, doi 10.1037/a0038898 (Crossref confirmed). Abstract-level only (via a Drexel repository summary).
- Carron, Colman, Wheeler and Stevens (2002), *J. Sport & Exercise Psychology* 24, 168-188, doi 10.1123/jsep.24.2.168 (Crossref confirmed). Not read.
- Gully, Devine and Whitney (1995), *Small Group Research* 26(4), 497-520, doi 10.1177/1046496495264003 (Crossref confirmed, 2026-10-30 validation). Not read.
- Chiocchio and Essiembre (2009), "Cohesion and performance: a meta-analytic review of disparities between project teams, production teams, and service teams", *Small Group Research* 40(4), 382-420, doi 10.1177/1046496409335103 (Crossref confirmed, 2026-10-30 validation; an earlier guessed DOI had resolved to Rovio et al.). Not read.
- Casey-Campbell and Martens (2009), *Int. J. Management Reviews* 11(2), 223-246, doi 10.1111/j.1468-2370.2008.00239.x (Crossref confirmed). Not read; a narrative review, not a meta-analysis.
- Carron, Widmeyer and Brawley (1985) *J. Sport Psychology* 7, 244-266 (the Group Environment Questionnaire); Evans and Dion (1991) *Small Group Research* 22(2), 175-186, doi 10.1177/1046496491222002 (Crossref confirmed; abstract read via Crossref); Carron, Widmeyer and Brawley (1985) is doi 10.1123/jsp.7.3.244 (Crossref confirmed). Hogg (1992) *The Social Psychology of Group Cohesiveness: From Attraction to Social Identity*, Harvester Wheatsheaf (Open Library confirms) (archive.org lending copy exists, not read); Festinger, Schachter and Back (1950). Not read. Festinger et al. appears only as quoted in Moody and White.

**Count: one primary text read in full-ish (Moody and White). None of the five seed meta-analyses was readable. This is the main finding about the evidence base for D261: the cohesion-performance quantitative record cannot be checked from open sources, and nothing [sa] below may feed an equation.**

---

## 1. Moody and White (2003): structural cohesion, the only formally defined cohesion measure found [read]

**Their vocabulary [read].** Structural cohesion; embeddedness; nestedness; k-connected graph, k-component, cutset, node-independent paths; cohesive blocking; "relational" versus "ideational" components of solidarity.

**Drives/operands [read].** None. Operands are actors (nodes) and relations (undirected positive ties; footnote 2: "the dyadic relation is a positive connection"). No motive, drive or affect enters the definition. This is deliberate: the paper separates the "relational togetherness of a group" from "the sense of togetherness that people express" (their wording) and says that conflating them "limits our ability to ask questions about how the relational component of solidarity affects, or is affected by, ideational factors".

**Definitions [read], quoted.**
- Definition 1: "A collectivity is structurally cohesive to the extent that the social relations of its members hold it together."
- Definition 2: "A group is structurally cohesive to the extent that multiple independent relational paths among all pairs of members hold it together."
- Definition 3a: "A group's structural cohesion is equal to the minimum number of actors who, if removed from the group, would disconnect the group."
- Definition 3b: "A group's structural cohesion is equal to the minimum number of independent paths linking each pair of actors in the group."
- Formal basis: Menger's theorem (via Harary 1969). A graph with node connectivity k has at least k node-independent paths between every pair, and conversely. A k-component is a maximal subgraph with no cutset smaller than k. "This conception scales, ranging from 0 (not connected) to n - 1 (a complete clique), and applies to networks of any size." (Moody and White 2003)
- Nestedness: cohesive blocking recursively removes cutsets; a member's nestedness is the depth of the deepest k-component containing it. Group-level cohesion is a single number (k); individual embeddedness is the nesting level.

So, written out, κ(G) = min |S| such that G − S is disconnected (κ = n − 1 for the complete graph K_n); and embeddedness of node i = max k such that i lies in some k-component. These are the paper's definitions in symbols; the symbols are mine.

**The one dynamical-looking equation [read].** Footnote 28: for d-step paths with dyadic transmission probability p, two independent paths give 2(p)^d − (p)^{2d}. Their worked example: one six-step chain at p = .9 delivers .53; two independent paths .78. (Check: .9^6 = .5314; 2(.5314) − .2824 = .780. Correct.) The authors call it "a simplification". It assumes independence of the paths and a fixed p; there is no time variable and no state.

**Group size [read].** Definition 1 has "five important features", the fifth being "the definition makes no reference to group size". But cohesion is bounded by size: k ≤ n − 1 (a clique), and every member of a k-component must have degree at least k, so a k-cohesive group needs at least k + 1 members and at least k ties per member. In large groups a high k needs a high minimum degree, which is expensive and rare; the paper notes that a clique level "is rarely observed except in small primary groups". They propose, but do not test, a size-normalised variant: "the ratio of connectivity to group size". The one test of size they run is a school-level coefficient on mean attachment: −.058 (SE .062, not significant) in Model 7, with 12 schools of 200-500 students (mean 349). So no evidence either way on size from this paper, and 12 school-level observations could not detect much.

**Group composition [read].** Composition enters only through who is tied to whom. Same-sex ties are about 1.6 times more likely than cross-sex ties in Add Health (their footnote 16, citing Moody 2001). The measure is blind to tie content, valence strength and role.

**Empirical standing [read], with SCALE stated.**
1. **Membership scale (individual attitude from group position).** Add Health friendship networks, 12 schools, 3,606 students at level 1 (Table 1 note), outcome the mean of three Perceived Cohesion Scale items (Bollen and Hoyle 1990; alpha = .82). Hierarchical linear model. Nestedness coefficient .016 (SE .001) in Model 2, standardized .279, the largest standardized effect in that model; with all rival network measures in (Model 7) it falls to .011 (SE .003), standardized .181. Degree (friends count) is .029 (SE .014, not significant at the table's stars). Deviance falls from 9,842.31 to 9,577.57 when nestedness is added. Cross-sectional self-report; attachment and friendship nominations come from the same students in the same survey. **The outcome is an attitude (feeling part of the school), not leaving, staying or conforming.**
2. **Group scale (dyad behaviour similarity).** 57 large U.S. firms, 1,596 dyads, Mizruchi's 1980 political-contribution similarity. Cohesive blocking: 51 of 57 firms in the largest bicomponent, a hierarchy 19 layers deep, 28 firms in the single 14-connected component. Table 2: R² .195 (Mizruchi baseline) to .217 with nestedness (.004, standardized .201, p ≤ .05), against common stockholders .029 (standardized .182). In Models 4 and 5 it stays at .004 with p < .10 only in the last. QAP tests, one year, one network.
3. **Nothing about outcomes of the group as such.** There is no test of performance, decision, split or survival. The authors write: "although we expect that structurally cohesive groups will also be stable groups, this expectation must be tested empirically." The stability claim, which would make this a dynamical measure, is explicitly untested.

**Consent or manipulation.** Not applicable. Observational network measurement; no intervention. (The implications section does discuss targeted removal of a node as an attack, which is manipulation of structure, but only as a thought experiment.)

**Operand/operator translation.** Operands: persons and ties. Operator: `remove(i)` on a group, with κ(G) reporting how many removals disconnect it. This is the best-defined operator-type object in the cohesion literature: it is an algebra of subtraction on a graph, with a theorem (Menger) behind it. What it does not offer is a drive-level cause of why ties form, and no time evolution.

---

## 2. Psychological cohesion: definitions and measurement, as second-hand accounts

**Carron/GEQ [sa; quoted by Leo et al. 2015, which I read].** Cohesion is "a dynamic process that is reflected in the tendency for a group to stick together and remain united in the pursuit of its instrumental objectives and/or for the satisfaction of member affective needs" (Carron, Brawley and Widmeyer 1998, p. 213, as quoted). The GEQ (Carron, Widmeyer and Brawley 1985) measures four first-order factors: individual attraction to the group, task (ATG-T) and social (ATG-S); group integration, task (GI-T) and social (GI-S). Leo et al. report that the four-factor structure was often not reproduced in other samples (references in their introduction) and that in their own 604-athlete sample it fitted acceptably (CFI .95, RMSEA .07), with correlations of r = .45 to .72 that the authors report as discriminant validity (their wording: "the discriminant capacity of the items of each factor"; not a factor-correlation matrix). Two qualifications from the same paper: the version validated is a short Spanish adaptation, not the original 18-item GEQ, and the authors summarise prior critiques as supporting the task/social distinction "but not the group integration-individual attraction to the group distinctions". **Scale: membership perception, aggregated to team by mean (aggregation convention only).**

**MacCoun and Hix 2010 on the military vocabulary [read as secondary].** Task cohesion: shared commitment to achieving a goal needing collective effort. Social cohesion: liking, preferring to spend time together, emotional closeness. Horizontal (peer) versus vertical (leader-follower) cohesion; group pride/collective identity treated as a possible third factor; trust as distinct from both; collective efficacy/potency as distinct. They also note that "cohesion is similarly influenced by a variety of factors, including leadership, group size, and unit turnover" (citing RAND 1993) but give no size coefficients in the sections I read.

**Hogg [sa; search accounts only].** Hogg (1992) argues that the concept of cohesiveness was reduced to interpersonal attraction and proposes social-identity/self-categorisation instead, distinguishing personal attraction from "social attraction", a depersonalised liking based on prototypicality. I did not read the book. The claim is a proposal, not a measured law; Hogg, Hardie and Reynolds (1995, *Eur. J. Soc. Psych.* 25, 159-177) is reported to find that people prefer prototypical members over interpersonal partners [sa, search summary].

**Evans and Dion (1991) [abs; publisher abstract via Crossref].** Positive link: "the average cohesive group performing 18 percentile points above the average noncohesive group"; the abstract adds that because all included studies were previously published, "caution is suggested in generalizing these results to 'real' work groups". Group-size moderation: not retrieved.

**Structural versus attitudinal: they are different constructs.** Moody and White say so explicitly and the field is split on it: a group can be dense and not feel united, and the reverse. For the algebra this means "cohesion" is at least two operands, a relational one (κ of the tie graph, measurable from behaviour without asking) and an ideational one (perceived cohesion, task or social). No source I read relates the two quantitatively except Moody and White's school regression, where graph nestedness predicts self-reported attachment.

---

## 3. The cohesion-performance relation and its lags

### 3a. Static magnitudes (all [sa], from MacCoun and Hix 2010 unless noted)

- All five meta-analyses agree there is a reliable positive cohesion-performance association; magnitude varies with task and measurement. Study counts per MacCoun and Hix: Gully et al. 46, Oliver et al. 36 (military only), Beal et al. 64, Chiocchio and Essiembre 29. My earlier file 24 recorded other counts for Mullen and Copper (49 / 66) from conflicting secondaries; the number is still unconfirmed.
- Components, as MacCoun and Hix report them: task cohesion ("commitment to task") r = .43 versus social cohesion ("interpersonal attraction") .27 in Mullen and Copper; .25 versus .17 in Beal et al. [sa]. For correlational studies Mullen and Copper found social cohesion and group pride had no reliable effect once task cohesion was controlled, and the converse did not hold [sa]. Beal et al. say all three components relate independently to performance, but MacCoun and Hix argue (their footnote 7) that Beal's coding could not control for task cohesion, so the two sets of conclusions are not directly comparable [sa; a reviewer's critique I cannot adjudicate without Beal].
- Moderators [sa]: stronger when performance is measured at group not individual level (Gully; Oliver); stronger with high task coordination (Beal; Chiocchio and Essiembre); stronger for behaviour than outcome and efficiency than effectiveness (Beal, abstract); larger in smaller groups and real rather than artificial groups, stronger in correlational than experimental designs (Mullen and Copper, from a search-engine summary of an EBSCO/Google Scholar listing; unverified); weaker in military than sports studies (Mullen and Copper per MacCoun and Hix).
- **Group size as a moderator: the reported "larger in smaller groups" finding for Mullen and Copper is the only size statement found, and it is a search-snippet-level [sa]. No effect size for size was retrieved.** Composition (task versus social cohesion; heterogeneity) is the moderator that is better documented, and that too is [sa].

### 3b. Direction of causality: the lag question

What is on record, with the confidence level of each:

1. **Mullen and Copper (1994)** examined seven cross-lagged panel analyses (cohesion and performance each measured at two times). MacCoun and Hix: "the patterns they reported in at least some of these studies suggest that performance had a stronger influence on cohesiveness than the reverse" [sa]. MacCoun and Hix also say later meta-analyses "have not updated this analysis" and that Beal et al. and Chiocchio and Essiembre coded only the Time 2 values of both variables. Their example (their footnote 8) is Chiocchio and Essiembre's coding specifically: Bakeman and Helmreich (1975; *J. Exp. Soc. Psych.* 11, 478-489, doi 10.1016/0022-1031(75)90050-5, Crossref confirmed, paywalled) is coded as r = .73 for social cohesion with performance (both at Time 2), but the Time 1 cohesion to Time 2 performance correlation in that study was .13 [sa; a reviewer's reading of one primary]. If that is right, the strong static correlations in the later meta-analyses are largely contemporaneous and cannot show a cohesion-to-performance arrow. I could not read Bakeman and Helmreich.
2. **Mathieu, Kukenberger, D'Innocenzo and Reilly (2015)** [abs only; full abstract read via Europe PMC, 2026-10-30; full text closed]: a meta-analysis of 17 cross-lagged panel (CLP) studies combined by structural equation modelling plus a new longitudinal study (205 members, 57 student teams, a 10-week business simulation, with a second student sample "mostly replicated"). **The two parts say different things, and the abstract keeps them apart.** The 17-study meta-analysis supports only that "team cohesion and performance are related reciprocally with each other over time"; it is not reported as favouring either direction. The directional findings come from the single student-team study: "the cohesion → performance relationship was significantly higher than the performance → cohesion relationship", and it "grew stronger over time whereas the performance → cohesion relationship remained fairly consistent"; shared leadership related to cohesion but not directly to performance; mean member competence related to performance but not cohesion. A Drexel news item describes the same pattern in plain terms (reciprocal; the performance effect on cohesion steady, the cohesion effect on performance growing).
3. **These two accounts point in different directions** (performance-driven in Mullen and Copper's seven panels as reported by MacCoun and Hix, versus cohesion-stronger in Mathieu et al.'s own 57-team student study; the 17-study meta-analysis itself is reported only as reciprocal, so it does not contradict Mullen and Copper at abstract level). I cannot reconcile them from what I could read. Candidates, all untested here: different evidence (Mathieu's directional claim rests on one student sample and its replication; Mullen and Copper had seven panels from mixed groups), different cohesion components, student teams in a simulation versus mixed real groups, lag length, and the growth-over-time finding (an early-window study would see performance dominate, a later window cohesion). **The honest status: direction of effect is unresolved; reciprocity is the only claim both sides support.**
4. **Scale of these results:** group-level (team cohesion, team performance). Student teams in a simulation are the primary study for the best-designed lag evidence; sports and military groups feature in the older meta-analyses. Not membership-level.

### 3c. A feedback-loop form: what the evidence permits and what it does not

The following is **my construction, not from any source**. It is stated as a hypothesis class only, with no parameter values, because none of the sources I could read supplies a coefficient I am allowed to use.

Let C_t be team cohesion (a vector if the task/social split is kept), P_t performance, at discrete time t. The minimal reciprocal form that matches the qualitative claim in Mathieu et al. (and the cross-lagged-panel design used in both lines of evidence) is

C_{t+1} = a_CC·C_t + a_CP·P_t + (exogenous terms) + noise,
P_{t+1} = a_PP·P_t + a_PC·C_t + (exogenous terms) + noise.

This is simply a first-order vector autoregression with the cross terms a_CP (performance to cohesion) and a_PC (cohesion to performance). The reported findings translate to: both cross terms positive; a_PC larger and growing with t, a_CP roughly constant (Mathieu et al.'s 57 student teams, abstract-level; their 17-study meta-analysis supports only both cross terms positive); or a_CP > a_PC (Mullen and Copper per MacCoun and Hix). The loop gain is a_CP·a_PC; if it exceeds the leftover stability margin the loop is self-reinforcing (success breeds cohesion breeds success, or the reverse spiral), and the sources speak in exactly that language (the "momentum" literature in file 24 §13 does too). Two cautions:
- A cross-lagged coefficient is identified only if the measurement interval matches the true time scale. Neither the sources nor I know the time scale of the underlying process; simulations with 10 weekly waves are one sample point.
- The model needs an exogenous term for performance that is not caused by cohesion (task difficulty, luck, competence). Mathieu et al. include member competence; no source includes difficulty.

This is deliberately the same shape as the coupling models of files 20, 59 and 79, with C and P as the two coupled state variables; file 79 gives the identifiability arithmetic for such fits.

---

## 4. Cross-reference to files 24, 06, 29

- File 24 §12 stated that the average cohesion-performance correlation was "small but significant" with study counts unconfirmed; this pass confirms none of that. It adds: (i) the Mathieu et al. 2015 cross-lagged meta-analysis, which file 24 lacked; (ii) the Bakeman and Helmreich Time 1 / Time 2 contrast (.13 versus .73), as reported by MacCoun and Hix; (iii) Moody and White, which file 24 listed under neither section.
- File 24 says "success may cause cohesion" is [std]. It remains [sa]: MacCoun and Hix is the best secondary source, resting on Mullen and Copper's seven panels.
- Files 06 and 29 (animal collective behaviour): not reread this pass. Nothing in the sources read here concerns non-human groups.

---

## 5. What exists vs what does not

**Exists.**
- One precise group-level cohesion measure with a theorem behind it and two regressions showing it adds explanatory power (Moody and White): κ(G), nestedness. Read at source.
- A mature psychometric vocabulary (task, social, pride, horizontal, vertical, trust) and a questionnaire (GEQ) with a patchy factor-structure record. Second-hand.
- Five meta-analyses agreeing on a positive, moderated cohesion-performance association (second-hand), with one reviewer's account that the static effect is partly or mostly performance causing cohesion, and a 2015 meta-analysis reporting reciprocity, plus a longitudinal student-team study in the same paper finding the cohesion-to-performance path significantly stronger and growing. Abstract-level.

**Does not exist (as far as I could check).**
- A dynamical law for cohesion that is estimated on data: no source read gives a differential or difference equation for cohesion with fitted parameters. The cross-lagged panel is a statistical design, not a law. Tested by search (2026-10-30): the nearest hit is Dimas, Rebelo, Lourenço and Rocha (2019), "A nonlinear dynamical system perspective on team learning: the role of team culture and social cohesion", *ICCSA 2019*, LNCS, 38-49, doi 10.1007/978-3-030-24302-9_4 (Crossref confirmed), reported to fit a cusp-catastrophe difference model to 44 workgroups at two time points with social cohesion as the bifurcation (control) variable and team learning as the state [sa, search summary; not read]. That is cohesion as a parameter, not a law for cohesion itself, so the gap stands but should be stated as "none found", not "none exists".
- A link from the structural measure (κ) to the attitudinal measure (perceived cohesion, GEQ) beyond one school regression, and a link from either to group outcomes such as splitting, decision or survival. Moody and White say stability is untested.
- A size-aware cohesion-performance result: only the unverified "larger in smaller groups" statement.
- A resolved direction of causality.
- Any intervention evidence: no source read manipulates cohesion with or without consent and measures what follows. Mullen and Copper's experimental subset exists (per MacCoun and Hix, none of the cohesion types had a significant partial correlation in experimental studies), but I did not read it, and it appears weaker than the correlational subset.

## Unconfirmed

- Mullen and Copper: every coefficient, the study count, the moderator pattern including "smaller groups", the seven cross-lagged panels and their reading.
- Beal et al. 2003 coefficients and the components claim; Gully, Oliver, Chiocchio and Essiembre figures; Carron et al. 2002 (stated as moderate, mainly through task cohesion, from file 24 secondaries).
- Mathieu et al. 2015 effect sizes, lag lengths, and the meta-analytic cross-lagged estimates (closed access; the abstract says the student-study difference is "significantly higher" but gives no numbers).
- Bakeman and Helmreich (1975) .13 versus .73 (MacCoun and Hix's reading).
- Hogg's claims beyond the book's blurb; Hogg, Hardie and Reynolds (1995), *Eur. J. Soc. Psych.* 25(2), 159-177, doi 10.1002/ejsp.2420250204 (Crossref confirmed; content not read). The Evans and Dion 18-percentile figure is now confirmed at abstract level only.
- That Moody and White's measure behaves similarly in small teams (their tests are 200-500-person schools and 57 firms; no team-size network is tested).

---

## Does it reduce to a drive basis?

**Mostly no for the part I could read; partly yes for what the psychology literature says about its causes.**
- **Structural cohesion does not reduce to drives, and does not try to.** κ(G) is defined on ties, not motives. Moody and White deliberately separate the relational from the ideational. Whether ties form from affiliation, status-seeking or task need is not in the definition. A drive-based algebra could generate the tie graph (drives of persons produce `bond(i, j)`, `abandon(i, j)`), after which κ(G) is a derived readout. That is a modelling choice the algebra would add, not a result of this literature.
- **Psychological cohesion is defined partly by drives.** Carron's definition names two motivational sources: "instrumental objectives" (task need) and "member affective needs" (social need). Task cohesion = shared goal commitment; social cohesion = liking and closeness. These map to a goal-pursuit drive and an affiliation drive of members, aggregated by mean. That mapping is the proposed reduction; the sources give no aggregation law and no derivation of the group quantity from member drives.
- **What does not reduce to member drives.** Group pride and collective identity (Hogg's social attraction: liking for a person as a prototype of a group, not as an individual) are defined on the group-as-category, not on a member's own needs. Trust, collective efficacy and vertical (leader) cohesion are likewise treated as separate constructs. Whether any of these are drives of the group or a member's appraisal of group state, the sources do not decide; Hogg's account is that the group category itself shifts the member's liking, which is a downward map that a pure person-drive basis would need to represent as a group-level operator.
- **Verdict for the working hypothesis:** this tradition gives no support for, and no counterexample to, drives as primitives. It measures cohesion without reference to drives, and what drive language it uses is a post hoc split of the questionnaire into task and social. The cleanest use of the tradition is as readout operands (κ, task and social cohesion scores), not as a derivation.

## What does it predict or control, and how well?

- **Structural cohesion (read).** Predicts, cross-sectionally, students' self-reported attachment to school (standardized .28 alone, .18 beside degree, betweenness and density, 12 schools, 3,606 students) and, in one year, 57 firms' political-contribution similarity (adds about .02 of R² to .195, standardized .20, borderline significance in the fullest model). No prediction of any future event, split, exit or performance; no out-of-sample test; no intervention. Effect sizes moderate; the sources are one nationally sampled survey and one network.
- **Psychological cohesion and performance (second-hand).** Reported correlations of the order of .17 to .43 depending on component and meta-analysis (these are the MacCoun and Hix figures for Mullen and Copper and Beal; I did not read the meta-analyses). Out-of-sample prediction of a given team's performance from its cohesion is not shown anywhere in what I could access. The static correlation is substantially contemporaneous, and the one detailed example available (.13 versus .73) suggests the lagged predictive power of cohesion for later performance may be small in at least some studies. Mathieu et al. (2015) report a significantly stronger cohesion-to-performance path in their 57-team student study (their 17-study meta-analysis is reported only as reciprocal), but I could read only the abstract and cannot give a magnitude.
- **Control.** No intervention that raises cohesion and then measures performance was found in what I read. The military summary (MacCoun and Hix) makes policy claims (task cohesion, not social liking, matters; leadership and shared mental models build it) from correlational evidence.
- **Failures and caveats.** Direction of causation unresolved between meta-analyses; component conclusions (task versus all three) disputed between Mullen and Copper and Beal et al.; GEQ factor structure unstable across samples; social cohesion sometimes linked to worse team performance from the organisation's point of view (Janis 1982; Stogdill 1972; Peterson 2007 per MacCoun and Hix [sa]); weaker or null effects in simulated-combat military studies (Wong 1992; Peterson 2007, per MacCoun and Hix [sa]). Group size and composition moderation is essentially undocumented in the sources I could access.

## Validation log (2026-10-30)

DOIs resolved at api.crossref.org for every cited work that has one; content checked against the primary text where it is open.

- ✓ Moody and White (2003), doi 10.1177/000312240306800105. Reopened the published text (eScholarship CC BY copy, the JSTOR-stamped ASR pages) and checked against it: Definitions 1, 2, 3a and 3b verbatim; "ranging from 0 (not connected) to n − 1"; the five features, (5) "makes no reference to group size"; "rarely observed except in small primary groups"; "ratio of connectivity to group size"; "this expectation must be tested empirically"; footnote 2, "a positive connection"; the .53 / .78 example (footnotes 27-28) and the formula 2(p)^d − (p)^{2d} with "This is a simplification"; same-sex ties "about 1.6 times"; 12 schools, 200-500 students, mean 349; Table 1 (nestedness .016 (.001) [.279] in Model 2, .011 (.003) [.181] in Model 7; degree .029 (.014) [.118] unstarred; school size −.058 (.062); deviance 9,842.31 to 9,577.57; level 1 n = 3,606, level 2 n = 12); 57 firms, 1980, 1,596 dyads, 51 of 57 in the largest bicomponent, 19 layers, 28 firms in a 14-connected component; Table 2 (R² .195 to .217, nestedness .004* [.201], common stockholders .029* [.182]). All correct.
- ✓ MacCoun and Hix (2010), RAND ch. 5 (open PDF, reread). Study counts 46 / 36 / 64 / 29; the group-level and coordination moderators; military weaker than sport; Wong 1992 null and Peterson 2007 negative; .43 vs .27 and .25 vs .17; footnote 5 (no significant partial correlation in experimental studies); footnote 7 (the critique of Beal's coding); the seven cross-lagged panels; "subsequent meta-analyses have not updated this analysis"; footnote 8 (.73 vs .13). All as stated. ✎ Footnote 8 attributes the Bakeman and Helmreich coding to Chiocchio and Essiembre specifically, not to Beal et al. as well: fixed.
- ✎ Leo et al. (2015), doi 10.7334/psicothema2014.247. Reread. The Carron 1998 p. 213 quote, n = 604, CFI .95 and RMSEA .07 are correct. The r = .45-.72 values are reported as discriminant validity of the items, not as factor correlations: fixed. Added that the instrument is a short Spanish adaptation, and the authors' summary that prior critiques support the task/social split but not the GI/ATG split.
- ✎ Mathieu, Kukenberger, D'Innocenzo and Reilly (2015), doi 10.1037/a0038898 (closed; full abstract via Europe PMC). **Main correction:** the file credited the "cohesion→performance stronger and growing" finding to the 17-study cross-lagged meta-analysis. The abstract gives that finding for the authors' own 57-team student study ("significantly higher"). For the meta-analysis it reports only reciprocity. Fixed in §3b, §3c, §5, the predictions section and Unconfirmed. The claimed conflict with Mullen and Copper narrows to one student sample against seven mixed panels.
- ✎ Evans and Dion (1991), doi 10.1177/1046496491222002. The 18-percentile figure is confirmed from the publisher abstract via Crossref, so it moves from [sa] to [abs]. Added the abstract's caution about "real" work groups.
- ✎ Chiocchio and Essiembre (2009): DOI found and confirmed as 10.1177/1046496409335103. Content not read (closed).
- ✓ Gully, Devine and Whitney (1995), doi 10.1177/1046496495264003: the Crossref re-confirmation that was pending is now done. Content not read.
- ? Mullen and Copper (1994), doi 10.1037/0033-2909.115.2.210: confirmed to exist. Closed access, and the DTIC copy returns 403. The "smaller groups" moderator still cannot be found in any searchable source, so it stays in Unconfirmed.
- ? Beal, Cohen, Burke and McLendon (2003), doi 10.1037/0021-9010.88.6.989: confirmed to exist. Closed access, content [sa].
- ? Carron, Colman, Wheeler and Stevens (2002), doi 10.1123/jsep.24.2.168: confirmed to exist. Not read.
- ✓ Casey-Campbell and Martens (2009), doi 10.1111/j.1468-2370.2008.00239.x; Carron, Widmeyer and Brawley (1985), doi 10.1123/jsp.7.3.244; Bakeman and Helmreich (1975), doi 10.1016/0022-1031(75)90050-5 (paywalled); Hogg, Hardie and Reynolds (1995), doi 10.1002/ejsp.2420250204; Hogg (1992), the book (Open Library). Existence and authorship confirmed for each. Content not read.
- Search test of "no fitted dynamical law for cohesion": it turned up Dimas et al. (2019, doi 10.1007/978-3-030-24302-9_4). That paper is a fitted cusp difference model with social cohesion as the control variable, not the state. It is added as [sa], and the claim is reworded to "none found".

Sources opened for content: 5. Full texts: Moody and White, MacCoun and Hix, Leo et al. Abstracts: Mathieu et al. via Europe PMC, Evans and Dion via Crossref. Crossref was checked for all 16 DOIs.

**Verdict.** The [read] material is accurate. Every Moody and White figure and quotation checked matches the published text, and the MacCoun and Hix figures are reported faithfully. One substantive error was found and fixed. The file credited Mathieu et al.'s directional result (cohesion→performance stronger and growing) to their 17-study meta-analysis, but it comes from one student-team study, so the "conflict" with Mullen and Copper is weaker than the file stated. No fabrications were found, and no claim was upgraded to [read]. The file's central caution still holds: nothing quantitative on cohesion and performance here is [read], so nothing in §3 may feed an equation.

## Cross-checks (2026-10-30)

Checked against the other prior-work files by grep for the same authors, works, equations and terms (Moody, MacCoun, Mullen, Mathieu, Carron, Beal, Gully, Chiocchio, Bakeman, Hogg, Evans, Dimas, Leo, cross-lag, cohesion). Overlap is with 24 (cohesion survey, sections 11-13), 020, 072, 079, 085, 091 and 092. No other file cites Moody and White or Mathieu et al.

**Agreements.**
- Mullen and Copper's study count is unconfirmed. 24 §12 says so, and so does 087. 24 withdrew its recalled r of about .25. 087's .43 (task) and .27 (social) come from MacCoun and Hix and are a different figure. They do not confirm 24's withdrawn value, and 087 keeps them [sa].
- Gully et al. 1995: 46 studies, with 51 effect sizes in 24 §12 (abstract). 087 gets 46 studies from MacCoun and Hix. The counts agree.
- Carron et al. 2002 is "moderate, mainly through task cohesion" in both files.
- Beal et al. 2003 finds all three components independently related. Both files record that claim, and 087 adds MacCoun's coding critique.
- Performance-to-cohesion at least as strong as the reverse: 24 §12 (tagged [std]) and 087 (via MacCoun, [sa]) agree on the claim. 087 correctly downgrades the provenance to [sa].
- The cohesion-performance loop: 24 §13 (momentum as a positive-feedback loop on efficacy, needing a state with memory) and 24 §12 ("should not treat cohesion as a primitive input without a loop") agree with the VAR form in 087 §3c.
- Cohesion as a state with a fitted law: 072 (Turchin asabiya ODE) has a cohesion state with no fitted parameters and no measurement protocol. This agrees with 087's "none found" for a fitted dynamical law for cohesion.
- Lag dependence: 079 (Ryan, Kuiper and Hamaker, Phi(dt) = e^{A dt}, the lag problem) agrees with 087 §3c caution that a cross-lagged coefficient depends on the measurement interval.
- Cross-lagged form: 020 (Y1 = aX1 + pX2 + e1, with the lagged version as cross-lagged panel) matches 087 §3c.
- Structural measures without outcome validity: 084 says none of its six works links balance to a group outcome. This is the same gap 087 §1 records for κ(G) ("stability untested").

**Contradictions and conflicts (not resolved here; both sides recorded in the ledger lines below).**
- Direction of cohesion-performance causation: performance-led in MacCoun and Hix's account of seven panels, versus cohesion-led in Mathieu et al.'s student study. The 17-study meta-analysis is reciprocal only. Unresolved.
- Beal et al. (independent components) versus Mullen and Copper (social and pride add nothing once task is controlled). MacCoun's footnote 7 disputes Beal's coding. 24 §12 uses the framing "unlike Mullen and Copper". Unresolved.
- Cohesion and performance: 087 and 24 report a positive association. 092 reports Woolley et al. 2010 found cohesion did not predict collective intelligence c (read for the null). The outcome differs, so this is a scope tension and not a direct conflict. Unresolved.
- 091 §size census (line 89) reports a "marked negative effect of group size on group cohesion" (sa, Indik; Porter and Lawler; Silverman). 091 line 213 says there is no empirical group-size law for cohesion. These are inside 091 and are a caveat for that file, not a source conflict. 087 has no cohesion-size result beyond the unverified Mullen and Copper "smaller groups" statement.

**Terms that collide.** "Cohesiveness" in 085 (Dörfler-Bullo, phase cohesiveness on an arc) is not the social or structural cohesion of 087. Any equation set must keep them apart.

**Ledger lines for D261 (cluster H).** These are structured in the return. They are not yet in `docs/ledger.jsonl`, which was not edited. Provenance follows the file's tags. The author's own VAR construction in §3c is tagged `sa` with a note, because the ledger has no `derived` tag in this batch. It may not feed v0.

## Licences of quoted and transcribed material (2026-10-30)

- **Moody and White (2003), ASR 68(1)**: publisher copyright (ASA); an eScholarship copy is CC BY according to the validation log (not re-verified in this pass). Used as short quotations of the definitions (each under 60 words, attributed), restated equations (kappa, the footnote-28 path formula, written in our own symbols), and a description of Tables 1 and 2 with only the coefficients actually used. The standard graph-theory wording of the Menger/k-component sentence is not copied from Wikipedia as far as this file shows; Wikipedia is not cited and derivation is not confirmed (check item: if it was, mark CC BY-SA or reword). Access route: the provenance line mentions an ASA PDF Wayback copy and JSTOR-stamped pages; the lawful route is not stated here. The CC BY eScholarship copy is the route to cite; re-read from it if the other route was not legitimate.
- **Add Health (friendship networks, 12 schools, 3,606 students)**: not determined; distributed under a data use agreement, not an open licence, presumed. Dataset citation only, via published results in Moody and White Table 1; no microdata in the repo.
- **Mizruchi (1980) political-contribution similarity, 57 firms, 1,596 dyads**: not determined; publisher copyright presumed. Dataset citation of derived figures reported by Moody and White Table 2; no data in the repo.
- **MacCoun and Hix (2010), RAND ch. 5**: RAND report, open PDF; licence not determined, publisher copyright presumed. Short quotations and described figures only.
- **Leo et al. (2015), Psicothema**: not determined; publisher copyright presumed. Short quotations and described fit statistics (the Carron et al. 1998 definition is quoted as cited by Leo et al.).
- **Mathieu, Kukenberger, D'Innocenzo and Reilly (2015), J. Applied Psychology**: closed access; not determined, publisher copyright presumed. Short abstract quotations (via Europe PMC) and a description of the study design (205 members, 57 teams, 10-week simulation); no data reproduced, underlying data unavailable.
- **Evans and Dion (1991), Small Group Research**: not determined; publisher copyright presumed. Short abstract quotations via Crossref.
- **Mullen and Copper (1994); Beal et al. (2003); Carron et al. (1985, 2002); Gully et al. (1995); Chiocchio and Essiembre (2009); Casey-Campbell and Martens (2009); Bakeman and Helmreich (1975); Hogg (1992); Hogg, Hardie and Reynolds (1995); Dimas et al. (2019)**: not read, or read only as secondary accounts; not determined, publisher copyright presumed. Citations and second-hand figures only; no text quoted from the works themselves.
- **Access note (check item)**: the file records 403 responses and a cookie wall for DTIC, ResearchGate, a Birmingham repository and PubMed. None gave content and nothing was reproduced; no workaround is recorded in the file, and none is to be used.
