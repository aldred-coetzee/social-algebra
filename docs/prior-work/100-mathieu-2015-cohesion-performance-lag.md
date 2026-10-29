# Prior work 100: Mathieu et al. 2015, reciprocal cohesion-performance (settles L3911?)

Direction: D592

Date: 2026-10-29. Kind: deep-read. **Outcome: the full text could not be read. L3911 is NOT settled. Nothing in this file is a full-text [read], and nothing here may feed an equation.**

## What was tried (routes, so the next reader does not repeat them)

- Crossref (OK): doi 10.1037/a0038898, *J. Applied Psychology* 100(3), 713-734, Mathieu, Kukenberger, D'Innocenzo, Reilly; title "Modeling reciprocal team cohesion-performance relationships, as impacted by shared leadership and members' competence". 270 citing works. Crossref lists no references and no abstract.
- Unpaywall: `is_oa false`, `oa_status closed`, no locations. OpenAlex: closed, `any_repository_has_fulltext false`, two locations (publisher DOI, PubMed), neither with a PDF.
- doi.org to APA: HTTP 403 (Incapsula bot wall). Semantic Scholar page: HTTP 202 empty; its API: 429. Academia.edu: 403. CORE search: Cloudflare challenge. PubPeer: page exists, no comments, no text. A UNH CV PDF fetched OK but is a CV, not the paper. Two web searches (standard, extended) returned no PDF. Google Scholar "all versions" is not machine-reachable from here.
- Mullen and Copper 1994 (doi 10.1037/0033-2909.115.2.210): DTIC PDF ADA264020 returns 403 (as 087 also found). OpenAlex carries the abstract only.
- Validation 2026-10-30 retried: Drexel Esploro record (no file, DOI link only); DTIC ADA296297 (found by search as a Mullen and Copper report, possibly the ARI research-note version; 403 to both curl and WebFetch, so its identity is not confirmed); one further web search, no PDF of Mathieu 2015.
- So the text read is: the Europe PMC abstract of Mathieu et al. (REST API, PMID 25751749), the OpenAlex abstract of Mullen and Copper, and one secondary account (Mathieu, Gallagher, Domingo and Klock 2019, "Embracing Complexity: Reviewing the Past Decade of Team Effectiveness Research", *Annu. Rev. Organ. Psychol. Organ. Behav.* 6, 17-46, doi 10.1146/annurev-orgpsych-012218-015106; open PDF at psychiatry.ucsd.edu, provenance of that copy unconfirmed). Tag: **[abs]** = abstract read at the indexer; **[sa]** = secondary.

## 1. Mathieu et al. 2015

**Their vocabulary.** Team cohesion; team performance; cross-lagged panel (CLP) design; reciprocal relationship; shared leadership; members' academic competence.

**What the abstract says [abs, Europe PMC, verbatim in substance].**
- Part A, meta-analysis: "we synthesize findings from 17 CLP design studies, and analyze their results using SEM. Results support that team cohesion and performance are related reciprocally with each other over time." No direction, no coefficients in the abstract.
- Part B, new longitudinal study: 205 members of 57 student teams, a complex business simulation over 10 weeks. Questions: (a) reciprocal over multiple periods; (b) relative magnitude; (c) stability over time. Findings: "cohesion and performance were related positively, and reciprocally, over time. However, the cohesion -> performance relationship was significantly higher than the performance -> cohesion relationship. Moreover, the cohesion -> performance relationship grew stronger over time whereas the performance -> cohesion relationship remained fairly consistent over time."
- Shared leadership related positively to cohesion but not directly to performance; mean member academic competence related positively to performance and not to cohesion.
- A replication on a second student business-simulation sample "mostly replicated" the earlier relationships.

**Not obtainable (all of what L3911 needs).** The lagged coefficients, their standard errors, the lag length (the time between waves in the 10 weeks), the number of waves, the size of "significantly higher", the meta-analytic cross-lagged estimates, the cohesion measure (task vs social vs a composite), the performance measure, the team sizes, the competence and shared-leadership scales. The abstract gives none. The 2019 review (secondary, [sa]) adds only: time moderated the cohesion-performance relationship, which strengthens with time (p. 28), and shared leadership was a potent predictor of cohesion "and thereby, team performance trajectories". It reports no coefficients for this paper. Its general static figures (Cohesion rho = .21, sourced in its table to Beal, Cohen, Burke and McLendon 2003 and Hülsheger, Anderson and Salgado 2009; social .26 and task .30, sourced to Castaño, Watts and Tekleab 2013 and Chiocchio and Essiembre 2009; all vs performance) are the review's report of those meta-analyses, so [sa] for the underlying numbers, and are static, not lagged. (Validation re-read the review PDF: the p. 28 time-moderation sentence and the "potent predictor of team cohesion, and thereby, team performance trajectories" sentence are quoted correctly.)

**Equations.** None stated in the abstract. The design implies a cross-lagged autoregression with cross terms, which 087 already wrote as a proposed form (C_t, P_t, a_CP, a_PC). That is 087's construction, not a transcription from Mathieu. [no equation read]

**GROUP SIZE (n) and COMPOSITION.** n enters only as the sample: 57 teams, 205 members, so about 3.6 members per team on average (arithmetic from the abstract, not a stated team size). No size moderator is reported in the abstract. Composition: member academic competence (mean) predicted performance and not cohesion; shared leadership predicted cohesion. Both are within-sample student-team composition variables. Whether the meta-analysis tested type of team is not stated.

**SCALE.** Group scale: cohesion and performance of a team, over time (a group-level state and an efficiency/outcome measure). Student teams in a simulation; not membership (join/stay/leave) and not crowd.

**Consent / manipulation.** Observational. No intervention on cohesion was made, so there is no consent/manipulation question. The shared-leadership and competence results are correlational.

## 2. Mullen and Copper 1994 (comparison)

**Abstract [abs, OpenAlex, from the DTIC record], verbatim in substance:** "Overall, the cohesiveness-performance effect was highly significant and of small magnitude." The effect "was significantly stronger when cohesiveness was operationalized in terms of measurements of group members' perceptions of cohesiveness than when cohesiveness was operationalized in terms of experimental inductions of cohesiveness. The results of this analysis suggest that the more direct effect may be from performance to cohesiveness rather than from cohesiveness to performance."

Note what this does and does not say. The direction claim is an inference from the contrast between correlational and experimental effects, hedged ("may be"). That is a different evidential basis from a cross-lagged panel. 087's claim that Mullen and Copper "examined seven cross-lagged panel analyses" and that performance influenced cohesion more is MacCoun and Hix's account [sa] and is **not in the abstract**; I could not check it. No coefficient, study count or "smaller groups" moderator appears in the abstract. Experimental inductions of cohesiveness are interventions, but on contrived lab groups, and by manipulation of the group's cue, not with the members' stated consent to be made cohesive.

## 3. Does this settle L3911?

No. What can honestly be said:
- Both works, at abstract level, support only that the association is **reciprocal**. This agrees with 087's final line.
- The two directional claims differ in kind. Mullen and Copper's (abstract) rests on a correlational-versus-experimental contrast across a meta-analysis and is hedged. Mathieu's rests on cross-lagged paths in one student-team sample, plus a mostly-replicating second sample, and its meta-analysis does not claim a direction. They could both be true: different designs, different operationalisations, lab and student groups, and a time-growth finding (the cohesion path grows with time, so a short window would look performance-led).
- A fair status for L3911: **unresolved, probably a scope difference rather than a contradiction; resolution needs the Mathieu coefficient table and lag length, and the Mullen and Copper cross-lagged subset, both paywalled.** The ledger entry should not be closed as "settled".
- Access route that could still work and I could not use: a library or inter-library copy of the APA PDF; the authors' own request-a-copy; Mathieu's ResearchGate/Academia page behind a login. Aldred could fetch the PDF from a journal subscription and drop it in the scratch directory.

## Does it reduce to a drive basis?

Honest answer from what was read (abstracts only):
- **Reduces, in principle:** cohesion could be treated as a group state built from members' affiliative/belonging drive satisfaction (task cohesion as shared goal-drive alignment; social cohesion as mutual attraction). Performance feeding cohesion is the "success breeds liking" loop, which a drive model would call reward to the affiliation drive. That is my mapping; neither abstract proposes it.
- **Does NOT reduce, or is not shown to:** the cross-lagged paths are statistical associations between two aggregate scores; no drive of a person appears in either study. Shared leadership and member competence are structural properties of the team, not drives. Mullen and Copper's measurement-versus-induction contrast is a methods artefact, not a drive. So this tradition contributes a **group-level feedback loop with an estimated sign and relative size**, and no evidence about drives of persons.
- Verdict for the working hypothesis: neither supports nor refutes "drives as primitives"; it shows a group-level reciprocal state variable that a drive model would need to reproduce, not derive.

## What does it predict or control, and how well?

- **Predicts:** the abstract claims team performance across 10 weeks is predicted by earlier cohesion, with a path that grows over time, in 57 student teams. Out-of-sample: a second student sample "mostly replicated" it (no numbers). Real-world, non-student teams: not tested in the part I can see; the meta-analysis of 17 CLP studies shows reciprocity only.
- **Effect sizes:** not obtainable. "Significantly higher" gives no magnitude. Do not quote any figure. The only numbers read are static meta-analytic correlations in a secondary review (rho .21 to .30), which are not lagged.
- **Controls:** nothing. No intervention on cohesion; shared leadership is correlated with cohesion, not manipulated. Mullen and Copper's experimental inductions, per the abstract, give a weaker effect than perceived cohesion, which counts against cohesion being an easy lever.
- **Failures and caveats:** the key claim rests on one student simulation sample; student teams in a business simulation have an unusual, short and scored task; the direction claim is opposed by the earlier meta-analysis's inference; the methods needed to judge it (lags, waves, measurement invariance) are closed.

## Unconfirmed

- All Mathieu 2015 coefficients, lags, waves, team sizes, measures and the meta-analytic CLP estimates.
- Whether the 17-study meta-analysis reports unequal cross paths (the abstract says only "reciprocal").
- The seven cross-lagged panels in Mullen and Copper, and any statement about group size there.
- The "mostly replicated" second sample's detail.

## Ledger recommendation

L3911: keep open, re-mark as "scope difference, unresolved", note this file as 100 (abstracts only), and add the abstract-level contrast above. Provenance stays sa/abs.

## Validation log (2026-10-30)

- ✓ Mathieu, Kukenberger, D'Innocenzo, Reilly 2015, *J. Appl. Psychol.* 100(3), 713-734, doi 10.1037/a0038898: Crossref confirms title, authors, venue, pages; Europe PMC abstract re-read and every [abs] statement in section 1 matches it (17 CLP studies, 205 members / 57 teams / 10 weeks, C->P > P->C, C->P grows, shared leadership -> cohesion, competence -> performance, replication "mostly replicated"). 205/57 = 3.6 checked. Full text still closed (OpenAlex/Unpaywall closed; Drexel record has no file).
- ✓ Mullen and Copper 1994, *Psychol. Bull.* 115(2), 210-227, doi 10.1037/0033-2909.115.2.210: Crossref confirms; OpenAlex abstract re-read, quotes match. Full text not reached (DTIC 403). The "seven cross-lagged panels" and any group-size moderator remain unconfirmed; a search found no independent statement of either.
- ✎ Mathieu, Gallagher, Domingo, Klock 2019, *Annu. Rev. Organ. Psychol. Organ. Behav.* 6, 17-46, doi 10.1146/annurev-orgpsych-012218-015106: full citation and DOI added (file had only "Mathieu et al. 2019"); PDF read, p. 28 and shared-leadership quotations confirmed; the rho .21/.26/.30 figures now credited to the meta-analyses the review's table names (Beal et al. 2003; Hülsheger et al. 2009; Castaño et al. 2013; Chiocchio and Essiembre 2009), which were not themselves opened, so they stay [sa].
- No fabrications found; nothing removed. The "no text obtainable" claim was re-tested with a search and three access routes and holds.

Sources opened: 7 (Crossref x3 records, Europe PMC abstract, OpenAlex x2 records, the 2019 review full PDF; plus the Drexel record page). Verdict: the file is accurate and appropriately cautious; its only defects were an incomplete citation for the 2019 review and uncredited secondary figures, both fixed. No claim in it is [read] from the primary text of Mathieu 2015, nothing may feed an equation, and L3911 stays open.

## Cross-checks (2026-10-30)

Checked against the other prior-work files by grep for the same authors, works, equations and terms (Mathieu, Mullen, Copper, cross-lagged, cohesion, shared leadership, Beal, Carron, Chiocchio, Castaño, Hülsheger, the 2019 review). Main overlap: 087 and 24 §12. No other file cites Mathieu 2015 or the 2019 review. Nothing is resolved here. L3911 stays **unresolved**.

**Agreements**
- Mathieu 2015 is a reciprocal, cross-lagged cohesion-performance result, with the directional finding from the 57-team student study only. 087 §3b item 2 and 100 §1 agree on this.
- The 17-study meta-analysis is reciprocal only and states no direction. 087 §3b item 2 agrees.
- Mullen and Copper (abstract): small but significant cohesion-performance effect. 24 §12 and 100 §2 agree. 24 §12 uses "small but significant"; 100 quotes "highly significant and of small magnitude".
- Mullen and Copper's direction claim (performance-to-cohesion at least as strong, or more direct) appears in 24 §12 (tagged [std]) and 087 §3b item 1 (via MacCoun and Hix, [sa]). 100 §2 quotes the abstract's hedged "may be".
- Study counts: Gully et al. (46 studies, 51 effect sizes) in 24 §12 and 087 §3a agree with each other. Neither file contradicts 100.
- Beal et al. 2003 component values: 087 §3a gives task .25 and social .17 (via MacCoun and Hix, [sa]). The 2019 review (100 §1, [sa]) gives the Beal cohesion aggregate as rho .21. Arithmetically consistent with the mean of .25 and .17, so not a contradiction. The social and task figures in 100 (.26 and .30, Castaño et al. 2013 and Chiocchio and Essiembre 2009) come from different meta-analyses and are not comparable to 087's Beal split.
- Lag caution: 087 §3c (a cross-lagged coefficient depends on the measurement interval) matches 079 (the lag problem). 100 §1 "lag length not reported" is consistent with this.
- Cross-lagged form: 087 §3c's VAR form is 087's own construction. 100 states no equation. The two agree that no coefficient is available.
- Mathieu 2015 vs 087 correction: 087 once credited the "cohesion→performance stronger and growing" finding to the meta-analysis. It has since been corrected to the student study (087 validation log, 2026-10-30). 100 reads the abstract the same way. Agreement.
- Scope of the student sample (student simulation, 57 teams): 087 §3b item 3 lists it as a candidate reason the two directions differ. 100 §3 lists the same candidates.

**Contradictions (both sides recorded; not resolved)**
- **Direction of cohesion-performance causation.**
  - Mathieu et al. 2015 (student study): cohesion→performance significantly higher than performance→cohesion, and growing over time. Records: 100 §1 (and validation log, [abs]); 087 §3b item 2 [abs].
  - Mullen and Copper 1994 (seven cross-lagged panels, performance-led): 100 §2 (abstract, hedged "may be"); 087 §3b item 1 ([sa], MacCoun and Hix); 24 §12 (tagged [std], "at least as strong").
  - Verdict: **unresolved.** 100's own suggestion, "probably a scope difference", is not settled by any log entry and is not adopted here. Candidates (100 §3, 087 §3b item 3): one student sample against seven mixed panels, lag length, components, growth over time.
- **Cohesion components (Beal vs Mullen and Copper).** Beal et al. (all three components independently related) vs Mullen and Copper (social and pride add nothing once task is controlled, per 087 §3a [sa]). MacCoun's footnote 7 disputes Beal's coding. 24 §12 uses "unlike Mullen and Copper". 100 does not address this. **Unresolved.** Recorded in 087 §5 and 24 §12.
- **Mullen and Copper's "task is larger" component (24 §12, [std]) vs the abstract in 100.** The 100 abstract read says nothing about components. The 24 §12 claim that commitment-to-task "carries most of it" is therefore not checked by 100. **Unresolved, unverified.**

**Ledger lines** (provenance is "sa" throughout: the file has no [read] tag, and its abstract reads are tagged [abs]; no drive or equation is taken from a full text)

- Drive (author's mapping, not in any source): cohesion as a group state built from members' affiliative and belonging drive satisfaction; performance feedback as reward to the affiliation drive. 100 §"Does it reduce to a drive basis" labels it "my mapping; neither abstract proposes it". No file in prior-work states this claim.
- Equation: none stated in 100. The cross-lagged form the design implies is 087 §3c's construction (C_t, P_t, a_CP, a_PC), not Mathieu's. Dup of 087 §3c.
- Empirical result: Mathieu et al. 2015 student study (57 teams, 205 members, 10 weeks, business simulation). Predicted: performance over 10 weeks from earlier cohesion, with the cohesion path growing over time and the performance path steady. Controlled: none (observational). Effect size: not obtainable from abstract ("significantly higher", no numbers). Dup of 087 §3b item 2.
- Empirical result: Mathieu et al. 2015 meta-analysis of 17 CLP studies. Result: reciprocal association only, no direction, no coefficients. Dup of 087 §3b item 2.
- Empirical result: Mathieu et al. 2015 shared leadership and member competence. Shared leadership predicts cohesion but not performance directly; mean member competence predicts performance but not cohesion. Correlational. Dup of 087 §3b item 2 (abstract).
- Empirical result: Mathieu et al. 2015 second student sample "mostly replicated" the first. No numbers. Scope: replication within student simulations only.
- Empirical result: Mullen and Copper 1994 (abstract, OpenAlex): effect "highly significant and of small magnitude"; stronger for perceived cohesiveness than for experimental induction; direct effect "may be" performance→cohesiveness. Controlled: none (meta-analysis of experimental and correlational studies). Dup of 24 §12 (magnitude, [abs, secondary]); the direction and induction contrast is in 100 only.
- Empirical result: 2019 review (Mathieu, Gallagher, Domingo and Klock; [sa], p. 28 and shared-leadership sentence confirmed in validation): time moderates the cohesion-performance relationship; shared leadership is a potent predictor of cohesion and thereby of team performance trajectories. No coefficients. Dup: none in prior-work.
- Empirical result: static meta-analytic correlations via the 2019 review (Beal et al. 2003 aggregate rho .21; Castaño et al. 2013 social .26 and task .30; Chiocchio and Essiembre 2009 same). [sa], static, not lagged. Dup of 087 §3a (Beal split .25/.17, different values; not the same figure).
- Definition: team cohesion (task vs social components; group-level state). Dup of 087 §1 and 24 §12 (MacCoun and Hix definitions).
- Definition: team performance (group-level outcome; efficiency vs effectiveness in Beal). Dup of 24 §12 and 087 §3a moderators.
- Definition: cross-lagged panel (CLP) design; reciprocal relationship over time. Dup of 20 (cross-lagged form, [std]) and 079 (lag problem).
- Definition: shared leadership; members' academic competence (student team composition variables). No dup found.
- Contradiction: direction of causation, Mathieu (student study, cohesion-led) vs Mullen and Copper (seven panels, performance-led). Source: 100 §1, §2; 087 §3b items 1-3; 24 §12. Verdict: unresolved.
- Contradiction: cohesion components, Beal vs Mullen and Copper. Source: 087 §3a and §5; 24 §12. Verdict: unresolved.

**Size dependence**
- n appears only as the sample: 57 teams and 205 members, about 3.6 per team (arithmetic from the abstract, not a stated team size). No size moderator is reported in the Mathieu abstract. The "larger in smaller groups" claim for Mullen and Copper (087 §3a, [sa], search-snippet only) is **not** in the Mullen and Copper abstract that 100 read, so it stays unconfirmed. No size law for cohesion exists in the prior-work files (091 says so, line 213).

**Consent and manipulation**: Mathieu 2015 is observational, so none. Mullen and Copper's experimental inductions are interventions on contrived lab groups, per the abstract.

**Summary**: 100 duplicates 087 §3b on the Mathieu and Mullen and Copper claims and adds nothing new that changes a verdict. The only new facts are the 2019 review's time-moderation sentence and the abstract-level reading of Mullen and Copper's hedge. Nothing in this section is a full-text [read] and nothing may feed an equation. L3911 stays open.
