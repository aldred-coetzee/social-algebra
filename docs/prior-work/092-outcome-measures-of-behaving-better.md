# Prior work 092: outcome measures of "behaving better", by tradition, with instrument and scale

Direction: D577

Date: 2026-10-29. Kind: survey, run as a table build with deep reads of the accessible seeds. Question: across traditions, what does "better" mean as a measured outcome (trust, violence, wellbeing, output, decision quality, survival of the group, efficiency), with what instrument, at what scale, and does anything that steers it work by consent or by manipulation?

**Provenance rule applied.** [read] = I fetched the text of the work itself this session and read it. [read-extract] = the text was fetched by the WebFetch tool, which returns the output of a small summarising model, not the raw text; numbers are copied from that output and need a re-check against the PDF before they feed an equation (validation 2026-10-30 re-read every [read-extract] work raw, so none remain in this file). [sa] = secondary account (search summary, other file in this repo, or background knowledge). Nothing [sa] feeds an equation. No equation in this file is derived; the outcome variables below are candidate *dependent variables*, not laws.

## What I actually read

| Work | Status | Route and caveat |
|---|---|---|
| Woolley, Chabris, Pentland, Hashmi, Malone 2010, Science 330(6004):686-688, doi:10.1126/science.1193147 | [read], whole 3-page report plus Table 1 | PDF copy (a student-hosted annotated copy on students.cs.byu.edu; rights unverified) converted with pdftotext. The Supporting Online Material (task details, Tables S1-S4) was NOT read. Official page 403 to the fetch tool. |
| Cox, Arnold, Villamayor Tomás 2010, Ecology and Society 15(4):38, doi:10.5751/ES-03704-150438 | [read], full text | `ecologyandsociety.org/vol15/iss4/art38/main.html`, converted to text (re-read 2026-10-30). Tables 1-4 are images/blocks that did not survive conversion; prose read, not the cell counts of Table 3. DOI Crossref-confirmed 2026-10-30. |
| Edmondson 1999, ASQ 44(2):350-383, doi:10.2307/2666999 | [read]: sample, measures, method, prose of the results, and (validation 2026-10-30) Tables 4-8 | MIT-hosted JSTOR-derived PDF (rights unverified), pdftotext. DOI Crossref-confirmed 2026-10-30. |
| Clauset 2018, Sci. Adv. 4(2):eaao3580, doi:10.1126/sciadv.aao3580 | [read] (validation 2026-10-30): the Science Advances text via Europe PMC full-text XML (PMC5834001), and the arXiv chapter adaptation (arXiv:1901.05086) as raw PDF text | Both read by the validator; figures below checked against both. |
| Cirillo & Taleb 2016, Physica A 452:29-45, doi:10.1016/j.physa.2016.01.050 (Crossref-confirmed), arXiv:1505.04722 | [read] of the arXiv v2 preprint (raw PDF text, validation 2026-10-30) | Published Physica A version not read (paywalled); numbers are the preprint's. |
| Credé & Howardson 2017, J. Applied Psychology 102(10):1483-1492, doi:10.1037/apl0000176 | abstract read (Europe PMC); body [sa] | Paywalled; body not read. |
| Bates & Gupta 2017, Intelligence 60:46-56, doi:10.1016/j.intell.2016.11.004 | [read], author-formatted in-press PDF (gwern.net mirror; rights unverified) | Added by validation; previously only a secondary description. |
| Graf, Gimpel & Barlow 2019, "Clarifying the Structure of Collective Intelligence in Teams: A Meta-Analysis", Collective Intelligence 2019 (extended abstract, work in progress) | [read], fim-rc.de PDF | No DOI found in Crossref; conference abstract. Added by validation. |
| Hackman 2002 (Leading Teams, Harvard Business School Press; title confirmed by Woolley's ref. 3); Ostrom 1990; Pinker 2011; Sosis & Bressler 2003; OECD How's Life 2020; Project Aristotle; Eisner 2003 | [sa] | Books or paywalled/blocked pages. Hackman, Sosis and Ostrom's text are NOT read at source here. OECD page 403; re:Work URL 404; Eisner full text unreachable. |

I did not guess any DOI. Validation 2026-10-30 resolved every DOI in this file at api.crossref.org: Woolley, Edmondson, Clauset, Credé-Howardson, Cox et al. (10.5751/ES-03704-150438), Cirillo-Taleb, Bates-Gupta, and those added below all return the stated title and authors. The Woolley PDF was re-read from a second copy (chabris.com, co-author's site) because the students.cs.byu.edu URL no longer serves a PDF.

---

## 1. Per-work records

### 1.1 Woolley et al. 2010: collective intelligence c (group: decision/problem-solving quality)

**Their vocabulary.** "collective intelligence (c)", defined as "the general ability of the group to perform a wide variety of tasks"; "empirically, collective intelligence is the inference one draws when the ability of a group to perform one task is correlated with that group's ability to perform a wide range of other tasks" [read]. "a property of the group itself, not just the individuals in it" [read].

**Instrument and scale.** Random assignment of individuals to groups. Study 1: 40 three-person groups, up to five hours, tasks sampled from all quadrants of the McGrath Task Circumplex: visual puzzles (group matrix reasoning), brainstorming, collective moral judgments, negotiating over limited resources (shopping trip plan), typing, and a criterion task at the end (the text says checkers against a standardised computer opponent; Table 1 labels the criterion column "Video Game"; this discrepancy is in the source) [read]. Study 2: 152 groups of two to five members, a broader task sample, up to ten tasks for a subset, criterion an architectural design task [read]. Total 699 individuals [read]. c score = factor-loading-weighted sum of task scores. Scale: group, small (2-5), lab, newly formed, single session.

**Results as printed [read].**
- Study 1: average inter-task correlation r = .28; first factor eigenvalue "over 43%" of variance, second 18%; single-factor CFA chi2 = 1.66, P = .89, df = 5, CFI = .99, RMSEA = .01. After principal-axis extraction the first factor explains 31% (Study 1) and 35% (Study 2). c predicts the criterion task r = .52, P = .01. Average member intelligence vs c r = .19 ns; max member intelligence vs c r = .27 ns; average and max intelligence vs criterion r = .18 ns, r = .13 ns. Regression with both: c beta = .51, P = .001; average member intelligence beta = .08 ns; max beta = .01 ns.
- Study 2: first factor 44%, second 20%; CFA chi2 = 5.85, P = .32, df = 5, CFI = .98, NFI = .89, RMSEA = .03. Criterion (architectural design) done individually by 63 people: individual intelligence predicts, r = .33, P = .009. Done by groups: average member intelligence r = .18 ns; regression c beta = .36, P = .0001; average member intelligence beta = .05 ns; max beta = .12 ns (controlling for group size in Study 2).
- Pooled: average member intelligence vs c r = .15, P = .04; highest-scoring member vs c r = .19, P = .008.
- Predictors of c: average social sensitivity ("Reading the Mind in the Eyes") r = .26, P = .002; variance in number of speaking turns (sociometric badges, a subset of groups) r = -.41, P = .01; proportion female r = .23, P = .007, "largely mediated" by social sensitivity (Sobel z = 1.93, P = .03; women scored better, t(441) = 3.42). In a regression with all three (groups with all available) beta for social sensitivity = .33, P = .05, the other two not individually significant. "group cohesion, motivation, and satisfaction — did not" predict c [read, direct quote].
- Group size: only controlled for in Study 2; the report states no size effect on c itself [read: not stated].

**Theorems or derived predictions.** None; a measurement-model claim (one dominant factor).

**Empirical standing.** The 2010 report itself cites no replication. Contested:
- Credé & Howardson 2017 reexamine "6 previously published samples", conclude "the empirical support for the construct is generally weak", that "the general factor explains only little variance in the performance on many group tasks", and that "low effort responding and the nested nature of the data" may have inflated the covariation [abstract read; body not read].
- Bates & Gupta 2017 (three studies, 312 people) [read]: "individual IQ accounted for around 80% of group-IQ differences"; the women and turn-taking hypotheses "were not supported"; RME "exerted no influence on the group-IQ latent factor"; "In structural tests, this group-IQ factor was indistinguishable from average individual IQ". Note they DID find a group general factor ("a robust cognitive g-factor across diverse tasks", about 50% of variance): their dispute is that it is distinct from member IQ, not that it exists. (Corrected 2026-10-30: the earlier quote "completely indistinguishable" is not in the paper.) An after-study authority/empathy instruction manipulation had no effect, F(2,34) = 1.14, p = .33, both point estimates negative [read].
- Graf, Gimpel & Barlow 2019 [read]: MASEM over 745 teams in 13 studies from 6 papers; the single-factor CFA fit badly (chi2 = 40.79, df = 5, CFI = .73, TLI = .45, RMSEA = .10); principal-axis factoring gave three factors, first eigenvalue 1.05 (17% of variance), average inter-task-type correlation r = .001. Work in progress, extended abstract.
- Riedl, Kim, Gupta, Malone & Woolley 2021, PNAS 118(21):e2005737118, doi:10.1073/pnas.2005737118: 22 studies, 5,279 individuals, 1,356 groups; abstract says the results "support the conclusion that a robust CI factor" exists and predicts out-of-sample criterion tasks [abstract read only; by the original authors]. Added by validation as the counterweight.
- Woolley, Kim & Malone, "Measuring Collective Intelligence in Groups: A Reply to Credé and Howardson", SSRN 2018, doi:10.2139/ssrn.3187373 [exists, Crossref; not read].
Bluntly: the existence of a single c factor distinct from member IQ is unsettled, with the original group's own meta-analysis for it and an independent meta-analysis and replication against; the cohesion null is a notable contrast with group-cohesion folklore, and the 2010 sample is small (40 + 152 groups) and lab-only.

**Outcome definition.** "Better" = performing better across a battery of puzzle-like and negotiation tasks, scored by the experimenter. It is an efficiency/decision-quality measure, scored externally, in a single session. It says nothing about survival, wellbeing or ethics.

**Consent vs manipulation.** The paper proposes (does not test) raising c by "better electronic collaboration tools" [read]. The turn-taking finding would, if causal, be steerable by facilitation; not tested.

**Translation.** Operand: group of 2-5 with member traits (social sensitivity) and an interaction statistic (turn-taking variance). Outcome: a scalar c per group. Candidate operator: none stated; correlational only.

### 1.2 Cox, Arnold & Villamayor Tomas 2010: Ostrom's design principles (group/commons: survival and sustainable resource use)

**Their vocabulary.** "design principles", "robust institutions for managing common-pool resources", "community-based natural resource management", "successful" [read].

**Instrument and scale.** A review of 91 studies published after Ostrom (1990), coded for methodology (detailed, statistical, synthesis, abstract), sector (forest, fishery, irrigation, pasture, multiple, other) and an evaluation variable 1 (highly unsupportive) to 5 (highly supportive) by the balance of evidence [read]. In a case data set they coded for each principle an "evidence" variable (are conditions satisfying the principle present) and a "success" variable (does the case report successful community-based natural resource management) in 0/1 form, cross-tabulated, Fisher's exact test, phi as effect size [read]. The success variable is the review's coding of what each case study reports, not an independent instrument.

**The eight principles as the review lays them out [read]:** 1 well-defined boundaries (coded 1A user boundaries, 1B resource boundaries); 2 congruence between appropriation/provision rules and local conditions (2A, 2B); 3 collective-choice arrangements ("most individuals affected by the operational rules can participate in modifying the operational rules", quoting Ostrom 1990:90); 4 monitoring (4A presence of monitors, 4B monitors are members or accountable to them); 5 graduated sanctions; 6 low-cost conflict-resolution mechanisms; 7 minimum recognition of rights to organise by external government; 8 nested enterprises.

**Results as printed [read].** Overall mean evaluation 3.73 of 5 across 91 studies. Study types differ (Kruskal-Wallis P = .004); abstract (theoretical) studies had median 2.0, "moderately unsupportive", versus the three empirical types combined (Mann-Whitney P = .002); once abstract studies are removed the empirical types do not differ (P = .122). Sector differences not significant (P = .747); no relation with publication year; 60 overt vs 31 implicit evaluations, means 3.60 vs 3.97, P = .343. 91 studies and 77 cases were coded [read]. The case "success" variable is 1 if a case "reported successful long-term environmental management" and 0 if it "reported a clear failure in collective action and management", blank if ambiguous [read]. Per-principle prose: "strong evidence" for 1A, "moderate" for 1B; "very strong" for 2A/2B; principles 3, 4A, 5 and 6 "moderately well supported"; 4B "very strongly supported"; principles 7 and 8 "moderately supportive". The labels are defined by the ratio of supportive (diagonal) to unsupportive cases: > 10 very strong, 5-10 strong, 2 to < 5 moderately well; "every one had at least twice as many supportive cases as unsupportive" [read]. Fisher's exact test was significant at the 5% level "for every principle except Principle 8, which was significant at the 10% level" [read; corrected 2026-10-30, this line previously said significant for every principle]. The exact cell counts and phi values are in Table 3, not read. Conclusion: "well supported", "a probabilistic, rather than deterministic, interpretation ... is warranted"; incompleteness is "the most important empirical critique" (user group size, heterogeneity, government regime are named as missing); uncertainty "whether the principles may apply to systems at a variety of scales" [read]. Recommended reformulation splits 1, 2 and 4 (social monitoring vs environmental monitoring) [read].

**Empirical standing, bluntly.** Support is association between a coded presence of an institution and a coded report of success in published case studies: no controlled comparison, selection of cases on success is likely (the paper does not claim to have dealt with it), and the reverse-causation problem is explicit in one quoted study: a negative correlation between having a guard and forest condition across 95 Indian community forests, read by its authors as "villagers are more likely to hire guards and impose fines more frequently if their forests are not in a good condition" (Agrawal & Chhatre 2006, World Development 34(1):149-166, doi:10.1016/j.worlddev.2005.07.013, quoted at p.160 in the review [read in the review; Agrawal & Chhatre not read directly]). Group size: named by the authors as an important omitted factor, with no effect size given.

**Outcome definition.** "Better" = the commons is managed without collapse and the user community persists as a rule-making body; durable institution rather than wellbeing. Scale: village/community (tens to thousands of users).

**Consent vs manipulation.** Principle 3 and 6 are consent-based (participation, adjudication); principle 5 is graduated punishment (sanction) administered by the group on its members; principle 7 is about outsiders not overriding. The review argues the principles can be combined with a diagnostic approach rather than applied as a blueprint; "Design Principles Are not Blue Prints, but Are They Robust?" is the title of the earlier Lincoln Institute report (a meta-analysis of 112 studies) that the paper revises, per its acknowledgments [read].

**Translation.** Operand: a user group with a boundary, a rule set, monitors. Operators are rule-level (monitor, sanction, adjudicate, nest), not drive-level. These are institutional operators with unspecified drive content.

### 1.3 Edmondson 1999: psychological safety, learning behaviour, team performance (group: output)

**Their vocabulary.** "team psychological safety", "a shared belief held by members of a team that the team is safe for interpersonal risk taking"; "team learning behavior"; "team efficacy"; "context support"; "team leader coaching" [read].

**Instrument and scale.** 51 teams in one manufacturing company; surveys returned by 427 team members, 86% response, 90% of members in the 51 teams responded; two teams returned none. Psychological-safety items include "If you make a mistake on this team, it is often held against you" (reverse scored), "It is safe to take a risk on this team", "No one on this team would deliberately act in a way that would undermine my efforts"; learning behaviour items such as "We regularly take time to figure out ways to improve our team's work process". Performance: Hackman's team performance scale for self-report, and a parallel observer scale that Edmondson built herself ("I developed a similar scale for the observer survey"; items "This team meets or exceeds its customers' expectations", "This team does superb work"), rated by observers/customers [read]. Analysis at the team level (N = 51) to avoid non-independence; plus GLM at the individual level (N = 427) [read].

**Results in prose [read].** Learning behaviour (self-reported) predicts observer-rated team performance (H1 supported), and accounts for more variance than psychological safety, efficacy, context support or coaching alone. Psychological safety predicts learning behaviour significantly, and accounts for more variance in it than context support or coaching; efficacy predicts it but adds nothing once safety is controlled for self-reported learning (with observer-rated learning, efficacy stays significant, "some support" for H5). Psychological safety mediates between context support/coaching and learning (H7 supported), though coaching only approached significance as a predictor of safety (B = .33, t = 1.89, P = .06; context support B = .56, P < .001; Table 6); efficacy as mediator (H8) not supported. The paper's headline mediation (H3), omitted in the first draft of this file: learning behaviour mediates safety -> observer-rated performance; entered together, safety "becomes insignificant (B = .25, p = .42)" while learning "remains significant (B = .60, p < .05)" [read]. Member/observer agreement: r = .60 on team learning, r = .36 on team performance. Observer-rated learning and performance lacked discriminant validity, so the paper avoided testing them against each other.

**Coefficients (Tables 4-5, parsed by the validator 2026-10-30 from pdftotext; significance stars partly garbled in conversion) [read].** Observer-rated performance, N = 51, single predictors: learning behaviour .80 (adj R2 .26), psychological safety .67 (.21), team efficacy .60 (.17), context support .75 (.22), coaching .93 (.23), all p < .01. Self-reported learning on safety: .76, adj R2 .63; on efficacy .45, .23; with both, safety .70, efficacy .11, adj R2 .63. Observer-rated learning on safety .46, adj R2 .35. Unstandardised, one firm, cross-sectional: not a basis for an equation.

**Standing.** Cross-sectional, one firm, small N, author-built scales; the discriminant-validity caveat is the paper's own. Later meta-analytic standing is in file 38 (Frazier, Fainshmidt, Klinger, Pezeshkan & Vracheva 2017, Personnel Psychology 70(1):113-165, doi:10.1111/peps.12183, Crossref-confirmed; not read here).

**Outcome definition.** "Better" = customers/observers say the team meets expectations. Scale: team in an organisation. Safety is a *shared belief* operand with an interpersonal-risk drive flavour (fear of punishment/embarrassment suppressing speaking up); the paper says cohesion is not the same thing and can reduce willingness to disagree [read, paraphrase of the paper's framing].

### 1.4 Violence: Clauset 2018 and Cirillo & Taleb 2016 (crowd/state: lethal conflict)

**Clauset ([read], Science Advances text via Europe PMC and the arXiv chapter; validation 2026-10-30).** Data: Correlates of War interstate wars 1823-2003, 95 conflicts; severity = battle deaths from 1,000 (definitional minimum) to 16,634,907 (World War II); mean gap between onsets 1.91 years. Stationary model: severity power law Pr(x) proportional to x^-alpha for x >= x_min, alpha-hat = 1.53 +/- 0.07 for x >= 7,061 (51 wars), goodness-of-fit p = 0.78 +/- 0.03; arrivals constant-rate Poisson / geometric gaps. Trend test on "large" wars (upper quartile, x >= 26,625 deaths): 1914-1939, 10 large wars; 1940-2003, 5 large wars; under the stationary model (model 1, bootstrap of sizes on historical onset years) the probability of the "great violence" pattern (>= 10 large wars in <= 27 years) is 0.107(1) and of the "long peace" pattern (<= 5 large wars in >= 64 years) 0.622(2), the parenthesis being the standard error in the last digit; the Science Advances paper adds models 2 and 3 with 0.159/0.121 and 0.569/0.681. The 51 wars in the power-law fit are "the upper 54% of the distribution"; 95% of the bootstrap distribution of alpha-hat lies in [1.37, 1.76]. Conclusion: the post-1945 lull is "entirely typical" given heavy-tailed sizes; the postwar peace "would need to endure at least another 100 to 140 years to become a statistically significant trend" (Science Advances abstract; crossing points "around 100 to 140 years in the future for models 1 and 2", model 3 "much longer"); under the model the 100-year probability of at least one war at least as deadly as WWII is 0.43 +/- 0.01 (expected number 0.62 +/- 0.01). Caveats: only 95 wars; civil wars excluded; per-capita normalisation can create an artificial decline. Corrected 2026-10-30: the first draft doubted the "100-140 years" figure because a summariser missed it; it is in the published abstract and text.

**Cirillo & Taleb ([read], arXiv v2 preprint; published version not read).** 565 conflicts with more than 3,000 casualties over 1-2015 AD (504 for 1500-2015). Peaks-over-threshold: GPD shape xi about 1.5 in all fits (raw 1.4985 at 25k; rescaled 1.5868 at 145k; 1500-2015 restricted 1.4093 raw), "significantly greater than 1", which would imply an infinite mean for an unbounded distribution; because casualties are bounded by world population they fit a "dual" distribution and derive a "shadow mean": for L = 25,000 and H = 7.2 billion "the sample mean underestimates the shadow mean by a factor of at least 1.6 (up to a maximum of 7.5!)". Inter-arrival times for conflicts of >= 5M casualties: mean 93.03 years, MAD 113.57; no structural change can be asserted; for 1500-2015 the null of equiprobable multinomial cannot be rejected at 10%. Conclusion: "at least in the last 500 years humanity has shown to be as violent as usual."

**Reading them together [both read].** Both attack the same inference (decline from a short window of a fat-tailed process) with Poisson-arrival plus heavy-tailed-size models and reach a similar statement: the data cannot separate a real decline from a quiet stretch of a stationary process on the scale of wars. Clauset is more measured: his models "cannot rule out the existence of a change", but if it occurred "it cannot have been a dramatic shift". That is a statement about *war-size tail events* (state level). It does not test Pinker's claim about *homicide, torture, slavery and everyday violence*, on which the evidence is Eisner's and others' per-100,000 series, which I could not read at source: a secondary account (search summary of a CrimRxiv paper on English homicide 1250-1750, crimrxiv.com/pub/p38lquh1, 403 to fetch) reports that by 2014 Eisner's History of Homicide Database held 823 local estimates for 1200-1750 from 115 studies, and a "consistent, but not linear" downward movement [sa]. The first draft also quoted a drop of "over 90 percent from the 1300-1349 peak"; validation could not locate that figure in any search result and it is moved to Unconfirmed. Eisner 2003 is "Long-Term Historical Trends in Violent Crime", Crime and Justice 30:83-142, doi:10.1086/652229 (Crossref-confirmed; not read). Pinker 2011 itself: not read; no claim from it is used.

**Instrument and scale, violence.** Lethal violence is the best-measured "behaving better" variable (a body count, units battle deaths or deaths per 100,000), and the least informative about mechanisms. Scale: state (wars) and population (homicide).

**Consent vs manipulation.** Not an intervention literature here.

### 1.5 Other seeds: record of what I could and could not do

- **Hackman 2002** [sa]. Five conditions (real team, compelling direction, enabling structure, supportive context, expert coaching) are confirmed by search; the three effectiveness criteria (output acceptable to receivers; members' capability to work together in future; member satisfaction/growth) are from background knowledge and the search could NOT confirm them. File 24 §9 also tags Hackman [abs/std]. Note that Edmondson used "Hackman's team performance scale" [read], and Woolley cites Hackman 2002 in its reference 3 [read]; neither gives the criteria.
- **Sosis & Bressler 2003**, "Cooperation and Commune Longevity: A Test of the Costly Signaling Theory of Religion", Cross-Cultural Research 37(2):211-239, doi:10.1177/1069397103037002003 (Crossref-confirmed; abstract confirms "eighty-three 19th-century U.S. communes" and survival as the outcome) [sa beyond the abstract, from file 37]: survival analysis of 83 19th-century US communes; commune longevity (survival) is the outcome; reported religious versus secular difference, with the "6% vs 39% at 20 years" figure flagged unconfirmed in file 37.
- **OECD How's Life? 2020: Measuring Well-being**, OECD Publishing, doi:10.1787/9870c393-en (DOI resolves; 10.1787/9a7effb4-en redirects to it) [sa]. Search summaries of OECD-hosted pages (re-checked 2026-10-30) state it covers "37 OECD countries and 4 partner countries", over 80 indicators, 15 dimensions of the Better Life Initiative with a split into current well-being outcomes, inequalities and "resources for future well-being" (natural, human, economic, social capital) [sa]. The page was 403, so I cannot give the dimension list or per-indicator units from source. It is the only seed whose "better" is defined by plural, unweighted indicators with no aggregation; that is a design choice recorded as in the secondary summary.
- **Project Aristotle (Google)** [sa]. Outcome = four ratings (executive evaluation, team-leader evaluation, team-member evaluation, sales against quarterly quota) across 180 teams (reported as 115 engineering project teams and 65 sales pods), top reported factor psychological safety. Validation 2026-10-30: a search summary of the re:Work guide and of secondary write-ups agrees with these figures, but the guide itself was not read; it is an unpublished, non-peer-reviewed company study. Do not use for an equation.
- **Eisner 2003** [sa as above].

---

## 2. The table across traditions

Scale key: M = membership (join/stay/leave/conform), G = group (cohesion/decision/split/efficiency), C = crowd (adoption/mobilisation/opinion), S = state/population. "Status" says whether I read the instrument.

| "Better" | Tradition / work | Instrument (as read or as secondary) | Unit and scale | Status | Who scores it | Intervention and consent |
|---|---|---|---|---|---|---|
| Decision / problem-solving quality across tasks | Woolley 2010 c | factor-weighted composite of 5-10 lab task scores; criterion task | G, 2-5 people | [read] | experimenter, externally | none tested; suggested tools/facilitation |
| Output as judged by receivers | Edmondson 1999 (Hackman scale for self-report; observer scale her own) | survey scale ("meets or exceeds customers' expectations") by observers/customers | G, work team in one firm, N = 51 | [read] | customers/observers | none; leader coaching and context support as antecedents (design, consensual) |
| Learning behaviour (a process measure) | Edmondson 1999 | member survey items on improving process, seeking information | G | [read] | members; observers (r = .60 agreement) | as above |
| Psychological safety (a state, treated as antecedent not outcome) | Edmondson 1999 | 7-item author-built scale | G, shared belief | [read] (items sampled; full Appendix not read) | members | via leader and context |
| Team viability / satisfaction | Hackman 2002 | not read | G | [sa] | members | design of conditions |
| Persistence of a self-governing group and the resource | Ostrom 1990; Cox et al. 2010 | coded success (0/1) per case study; evidence of each principle (0/1) | G/S, village or irrigation system | [read] review, [sa] Ostrom | reviewers coding other people's case studies | rule design; sanction is graduated (coercion by the group), participation and adjudication are consent-based |
| Survival of the group | Sosis & Bressler (communes) | commune lifespan, survival analysis | G, n = 83 communes [sa] | [sa] | historians' records | none |
| Violence, lethal, war-scale | Clauset 2018; Cirillo-Taleb 2016 | battle deaths (COW); casualty counts, EVT tail fits | S | [read] (Cirillo-Taleb preprint) | historical record | none |
| Violence, homicide | Eisner database; Pinker 2011 | homicide per 100,000, 823 local estimates [sa] | S, local populations over centuries | [sa] | court and coroner records | none |
| Wellbeing | OECD How's Life 2020 | 80+ indicators, 15 dimensions, plural | S, country | [sa] | official statistics plus surveys | policy; no consent unit |
| Trust | not a seed-by-seed instrument in anything I read | (none read) | | | | |
| Cohesion | Woolley says it did NOT predict c | (the instrument for cohesion is in the SOM, not read) | G | [read] for the null only | | |

**Trust is empty.** None of the seeds read measures trust as an outcome. Woolley's task battery has no trust measure; Edmondson's safety is closest (belief the team will not punish a risk), and it enters as a cause. Trust-as-outcome (generalised trust surveys, trust games) is outside D577's seeds and not covered here; it needs its own direction. (Validation note: OECD How's Life 2020, a seed that was not read, does include social connections and trust in government among its tracked outcomes per the search summaries [sa], so "empty" means empty among the texts read, not among the seeds.)

---

## 3. What changes with group size and composition (only what the sources say)

- **Woolley** [read]: groups of two to five, composition varies in average social sensitivity, proportion female, and turn-taking evenness; the c factor appears in groups of different sizes (Study 2, size controlled), but the report gives no result by size. Composition matters via sensitivity and equality of speaking; maximum or mean member intelligence matters little to c (r = .15-.19).
- **Edmondson** [read]: team size is mentioned among group-level variables meaningful for aggregation ("team size is a ..." appears in the text) but I did not read a size result; no claim.
- **Cox et al.** [read]: user-group size, heterogeneity and regime are named as "clearly important in many cases" but omitted from the principles; "scale" is open: "we remain uncertain as to whether the principles may apply to systems at a variety of scales".
- **Clauset / Cirillo-Taleb** [read]: scale is the whole interstate system; the heavy tail means that the largest events dominate the mean (Cirillo-Taleb: sample mean underestimates the tail mean by 1.6x up to 7.5x), so sample size of events is the limiting factor, not group size.
- Group size as a driver of outcome: unresolved in everything I read.

---

## 4. Reflexivity and Goodhart in this table

Each outcome here is a *measure*, and several are measured by a party with an interest: group cohesion by members (could be inflated), performance by the same team in self-report (Edmondson used observer ratings precisely because self-report is weaker; self vs observer agreement on performance was only r = .36 [read]). Cox et al.'s success coding is by reviewers of other people's reports. A measure used as a target will move (Goodhart; Campbell). This file did not research that (D583 owns it) and no source read here tests it.

---

## 5. What exists vs what does not

Exists:
- A measurement model for group task performance with a single dominant factor in two small lab studies, contested [read for 2010; sa for the contest].
- A consistent pattern of positive association between institutional features and reported success in 91 coded commons studies, mostly case-based [read].
- A cross-sectional link from shared safety belief to learning behaviour to rated performance in one company [read].
- Clear statistical statements that war-scale violence cannot be shown to have declined from the available record [read].

Does not exist (in what I read):
- Any single "better" aggregate. The outcomes are incommensurable: performance (c), receiver-rated output (Edmondson), persistence (Ostrom, Sosis), deaths (Clauset), plural indicators (OECD). No source gives an exchange rate or a weighting. The closest to a deliberate refusal to aggregate is the OECD dashboard [sa].
- Any outcome measured prospectively and out of sample for group quality, other than c's criterion-task prediction (r = .52 in Study 1, beta = .36 in Study 2) within the same experiment.
- A trust outcome.
- A causal intervention study of any outcome at group level among the sources I read, with one small exception found in validation: Bates & Gupta 2017 ran an after-study authority/empathy instruction manipulation on group IQ and found no effect (F(2,34) = 1.14, p = .33) [read].
- Wellbeing measured for the group as an object (OECD is a country-level dashboard of person-level outcomes).

## Unconfirmed

- Hackman's three effectiveness criteria; Hackman's 2002 claim that conditions explain a quantified share of variance (no number was found).
- Ostrom 1990's own statements and the per-principle phi values and cell counts in Cox et al. Table 3.
- Cirillo-Taleb published (Physica A) version; numbers above are the arXiv v2 preprint's (paywalled).
- The Woolley SOM, including how cohesion, motivation and satisfaction were measured.
- Credé & Howardson 2017's numbers beyond the abstract (paywalled); Riedl et al. 2021 beyond the abstract; the Woolley-Kim-Malone SSRN reply (not read).
- Pinker 2011's own arguments and data; Eisner 2003's tables (paywalled).
- "Over 90 percent from the 1300-1349 peak" (homicide): not found in any search result during validation; source unknown. Do not use.
- OECD dimension list and units; Project Aristotle's details at source; Sosis & Bressler's figures beyond the abstract and file 37.
- Agrawal & Chhatre 2006 at source (quoted only via Cox et al.).

---

## Does it reduce to a drive basis?

Partly, and only at the level of the *antecedents*, not the outcomes.
- **Reduces (candidate mapping, not shown):** Edmondson's psychological safety is a shared belief about whether risk-taking will be punished, which maps to a fear/punishment-expectation drive on persons and a group-level aggregate of it; the finding that cohesion and motivation do not predict Woolley's c while social sensitivity does is consistent with a social-perception variable, not a motivational drive. Even-handed turn-taking could be read as a sharing of the "voice" drive. These are my mappings; none of the sources states a drive.
- **Does not reduce:** (1) the outcomes themselves, which are externally defined criteria (task score, customer expectation, commons survival, body counts), not drive satisfaction; a "drive basis" says what agents want, whereas these measures say what an observer counts as good. (2) Ostrom's principles 1, 2, 7 and 8 (boundaries, congruence with local conditions, external recognition, nesting) are structural properties of institutions and of the environment, not drives of persons or groups. (3) The heavy-tailed size distribution of wars and its Poisson arrival is an aggregate statistical law with no drive in it. (4) The c factor is a statistical dimension of performance; it says groups differ in a general capacity, and drives enter only via the weak predictors.

## What does it predict or control, and how well?

- **Woolley c**: predicts performance on a later task in the same session, r = .52 (Study 1, 40 groups) and beta = .36 (Study 2, 152 groups), beating mean and max member intelligence in the same models; out of sample beyond these studies it is contested (Credé & Howardson [abstract]; Bates & Gupta and Graf et al. 2019 [read] against; Riedl et al. 2021 [abstract] for). It controls nothing: no intervention was tested.
- **Edmondson**: associations with receiver-rated performance in 51 teams of one firm (learning behaviour alone, adj R2 .26; safety alone, .21); safety's link to performance runs through learning (H3 mediation); no intervention, no out-of-sample test in the paper.
- **Ostrom / Cox et al.**: predicts, in the weak sense of association, that commons with the principles present are reported as successful; mean support 3.73 of 5 across 91 studies; empirical (non-abstract) studies agree with each other; success coding is by the reviewers; reverse causation is explicit for monitoring. It does not predict an outcome in a held-out set; it is a diagnostic with a probabilistic reading.
- **Clauset; Cirillo-Taleb**: a stationary heavy-tailed model fits war sizes (p = .78 for the size fit) and is not rejected for the "long peace"; the prediction it makes is a base rate (at least one WWII-scale war within a century at 0.43) with huge uncertainty from n = 95 wars, and a horizon (100 to 140 more years of peace before a decline becomes significant). Failure is by design: the models say the declining-violence claim cannot be established from this record, and the same models cannot establish its absence either.
- **No steering by consent or manipulation is tested** in anything read here. The Woolley-style suggestion (tools, facilitation) and Edmondson's antecedents (leader coaching, context support) are consent-based design levers proposed from correlations, not demonstrated causal controls.

## Validation log (2026-10-30)

Provenance after validation: the [read-extract] tier is retired in this file. Every [read] above is a text the validator fetched raw (PDF via pdftotext, or HTML/JATS XML) and read; everything else is [sa] or "abstract read".

- ✓ Woolley, Chabris, Pentland, Hashmi & Malone 2010, Science 330(6004):686-688, doi:10.1126/science.1193147: Crossref matches; full report re-read (chabris.com copy); every number in §1.1 matches the text and Table 1.
- ✎ Cox, Arnold & Villamayor Tomás 2010, Ecology and Society 15(4):38, doi:10.5751/ES-03704-150438: Crossref matches; Fisher tests were NOT significant at 5% for every principle (principle 8 only at 10%); added 77 cases, the ratio-based support labels, and principles 3/4A/4B/5 wording; "not blueprints" attribution clarified.
- ✎ Edmondson 1999, ASQ 44(2):350-383, doi:10.2307/2666999: Crossref matches; observer performance scale is Edmondson's own, not Hackman's; headline H3 mediation added; coaching -> safety only p = .06; Table 4-5 coefficients added.
- ✎ Clauset 2018, Sci. Adv. 4(2):eaao3580, doi:10.1126/sciadv.aao3580: Crossref matches; published text read via Europe PMC (upgraded to [read]); the "100 to 140 years" figure the draft doubted IS in the abstract and text; model 2/3 probabilities added.
- ✎ Cirillo & Taleb 2016, Physica A 452:29-45: DOI added, 10.1016/j.physa.2016.01.050 (Crossref); arXiv v2 read raw, all figures confirmed; shadow-mean sentence tightened; published version paywalled.
- ✎ Credé & Howardson 2017, JAP 102(10):1483-1492, doi:10.1037/apl0000176: Crossref matches; abstract read, consistent with the draft; body paywalled.
- ✎ Bates & Gupta 2017, Intelligence 60:46-56, doi:10.1016/j.intell.2016.11.004: read; the quoted "completely indistinguishable" is not in the paper (actual: "indistinguishable from average individual IQ"); they DO find a group g-factor; null manipulation added.
- ✎ Graf, Gimpel & Barlow 2019 (Collective Intelligence 2019 extended abstract, no DOI): read; findings added (single-factor fit poor, three factors, n = 745 teams).
- ✓ Riedl, Kim, Gupta, Malone & Woolley 2021, PNAS 118(21):e2005737118, doi:10.1073/pnas.2005737118: added as counter-evidence; Crossref matches; abstract only.
- ✓ Woolley, Kim & Malone 2018 reply, SSRN, doi:10.2139/ssrn.3187373: exists (Crossref); not read; dated 2018, not 2017.
- ✎ Agrawal & Chhatre 2006, World Development 34(1):149-166, doi:10.1016/j.worlddev.2005.07.013: Crossref matches; paraphrase corrected to the quoted guards/fines finding (95 forests).
- ✓ Frazier, Fainshmidt, Klinger, Pezeshkan & Vracheva 2017, Personnel Psychology 70(1):113-165, doi:10.1111/peps.12183: exists; not read.
- ✓ Sosis & Bressler 2003, Cross-Cultural Research 37(2):211-239, doi:10.1177/1069397103037002003: Crossref matches; abstract confirms 83 communes and survival outcome; "6% vs 39%" still unconfirmed.
- ? Eisner 2003, Crime and Justice 30:83-142, doi:10.1086/652229: exists; not read. The "over 90 percent from 1300-1349 peak" figure could not be found in a search and is moved to Unconfirmed; 823 estimates / 115 studies only from a search summary.
- ? Hackman 2002, Leading Teams: exists; five conditions found by search; the three effectiveness criteria still not confirmed by any search result.
- ? OECD How's Life? 2020, doi:10.1787/9870c393-en: DOI resolves; 37+4 countries, 80+ indicators, 15 dimensions agree across OECD-page search summaries; page 403, so [sa].
- ? Project Aristotle (Google re:Work): 180 teams and four measures agree across secondary summaries; primary guide not read; not peer reviewed.
- ? Ostrom 1990; Pinker 2011: exist (standard books); not read; no claim rests on them beyond what Cox et al. quote.
- No fabrications found; nothing deleted.

Sources opened by the validator: 9 primary texts (Woolley 2010 PDF; Cox 2010 HTML; Edmondson 1999 PDF; Clauset 2018 Science Advances full text; Clauset arXiv chapter; Cirillo-Taleb arXiv preprint; Bates & Gupta PDF; Graf et al. 2019 PDF; plus the Credé-Howardson, Riedl, Sosis-Bressler and Clauset abstracts), and Crossref records for 16 DOIs.

Verdict: The file is substantially sound and honest about what it did not read; no citation was invented and every DOI resolves to the stated work. The errors that mattered were a summariser's: it missed Clauset's published "100 to 140 years" horizon and put a phrase ("completely indistinguishable") in Bates & Gupta's mouth, and Cox et al.'s principle 8 was overstated as significant at 5%. Nothing here supplies an equation: the outcome measures are correlational, mostly single-sample, and the c factor itself is contested by meta-analyses pointing in opposite directions.

## Cross-checks (2026-10-30)

Checked against the other 93 files in this directory: every seed work, author and headline number in this file was grepped across the directory. Ledger lines are returned to the orchestrator for `docs/ledger.jsonl`; no other file was edited, nothing committed.

**Agreements**
- Edmondson 1999 (51 teams, one manufacturing firm; the psychological-safety definition; team efficacy adding nothing once safety is controlled): `38-organisational-motivation.md` §11 gives the same sample, definition and efficacy result.
- Hackman 2002's five team conditions: `24-collective-action-team-motivation.md` §9 gives the same five, both as abstract/standard account. 24 also records a "shared mindset" extension that this file does not mention.
- Sosis & Bressler 2003 (83 communes, survival outcome, abstract read; "6% vs 39%" unconfirmed): `37-ritual-sacred-awe.md` gives the same n, outcome and unconfirmed status.
- Ostrom's design principles and the caveat that case selection is a likely problem: `25-culture-scale-drives-norms.md` §F3 says the same, as standard account.
- Campbell's law and Goodhart's law: §4 here defers to `093-reflexivity-performativity-goodhart-lucas.md`, which owns them. No conflict.

**Contradictions, unresolved (both claims recorded; validation has not settled any of them)**
- C1. Woolley 2010 single-factor CFA fits well (Study 1 CFI .99, RMSEA .01; Study 2 CFI .98) [read], §1.1, versus Graf, Gimpel & Barlow 2019 single-factor fit poor (CFI .73, RMSEA .10, 745 teams) [read], §1.1. Different samples and task sets.
- C2. Woolley 2010: c beats average member intelligence (beta .51, Study 1; beta .36 for c, Study 2) [read], §1.1, versus Bates & Gupta 2017: individual IQ accounts for around 80% of group-IQ differences, and the group factor is indistinguishable from average individual IQ [read], §1.1.
- C3. Woolley 2010: turn-taking variance correlates r = -.41 with c, in a subset of groups [read], §1.1, versus Bates & Gupta 2017: the turn-taking hypothesis was not supported [read], §1.1.
- C4. Woolley 2010: proportion female correlates r = .23 with c, largely mediated by social sensitivity [read], §1.1, versus Bates & Gupta 2017: the women hypothesis was not supported [read], §1.1.
- C5. Riedl et al. 2021 (22 studies, 5,279 people): a robust CI factor exists and predicts out-of-sample criterion tasks [abstract, sa], §1.1, versus Credé & Howardson 2017: empirical support for the construct is generally weak [abstract, sa], §1.1. Both sa, so neither may feed an equation.
- C6. Woolley 2010: cohesion did not predict c [read], §1.1 and §5, versus `087-cohesion-measurement-lags-feedback-loop.md` §3: positive cohesion-performance association across five meta-analyses [sa]. 087 says the outcomes differ (c versus performance). That is a scope difference recorded by 087, not a resolution, so it stays open.

**Not contradictions, but check before an equation uses them**
- Clauset's density exponent alpha = 1.53 (95 wars, x >= 7,061) and Cirillo-Taleb's GPD shape xi ~ 1.5 (565 conflicts, > 3,000 casualties) are different estimators on different samples. Both imply heavy tails. This file does not reconcile them, and they must not be combined without re-deriving.
- Name clashes with other files: "Ostrom" here is Ostrom 1990 and Cox et al. 2010; `04-logics-institutions-calculi.md` cites Crawford & Ostrom 1995 (ADICO), a different work. "Riedl" here is Riedl et al. 2021; 12 and 33 cite Riedl & Bulitko. "Agrawal" here is Agrawal & Chhatre 2006; `054-boredom-information-opportunity-cost.md` cites Agrawal et al. 2022. No duplicate marks are made across these.
- Eisner's homicide figures (823 estimates, 115 studies) appear only here, as search summary. No other file covers them. `058-honour-cultures-retaliation-thresholds.md` covers Cohen & Nisbett's honour-homicide work, a different source.
- No other file cites Clauset 2018, Cirillo & Taleb 2016, Credé & Howardson 2017 (beyond this file), Graf et al. 2019, or Project Aristotle. Riedl 2021 and Bates & Gupta 2017 are cited only here.

Ledger lines for D577 (cluster S) were returned to the orchestrator. The count of lines marked duplicate is in the return, not here.
