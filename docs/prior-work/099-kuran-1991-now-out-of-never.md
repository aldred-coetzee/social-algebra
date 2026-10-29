# Prior work 99: Kuran 1991, "Now out of never", read at source (working-paper version)

Direction: D591
Date: 2026-10-30. Kind: deep-read. Survey for the social-algebra strand.
Question (research map D591): what is the threshold form in Kuran 1991 (reputational vs integrity utility), what is its revolutionary-bandwagon condition, and how does it differ from Kuran 1989? Settle ledger L3991 and say what to edit in file 066.

## Provenance, stated first

- **What was read.** Timur Kuran, "Now Out of Never: The Element of Surprise in the East European Revolution of 1989", **Papers in Political Economy No. 27, Political Economy Research Group, University of Western Ontario** (ISSN 1181-7151, ISBN 0-7714-1462-5). A scanned typescript, 48 PDF pages (cover, series page, title/abstract page, then printed pages 1-45; printed page n is PDF page n+3). Catalogue date 1992-01-01. URL: https://hdl.handle.net/20.500.14721/10358 (repository page https://ir.lib.uwo.ca/economicsperg_ppe/19; PDF https://uwo.scholaris.ca/bitstreams/90bbee63-eadf-4e87-9a9d-5bdc9763efc6/download). Licence not stated on the record; quotations below are short and attributed.
- **How.** The PDF is image-only (no text layer; no OCR available here), so I read **all 45 printed pages as page images**, one by one. Every [read] tag below is to those images. Because I could not text-search, **absence claims ("the paper never uses the word X") are weaker than presence claims**; they are marked.
- **This is a working paper, not the published article.** The published article is World Politics 44(1): 7-48, October 1991, DOI **10.2307/2010422**, confirmed on Crossref (title, volume 44, issue 1, pages 7-48, issued 1991-10, sole author Kuran). The working paper has the same title and the same abstract text as the Crossref abstract quoted in file 089, and its footnote 31 says an earlier summary appeared in the American Economic Review P&P May 1991, so it was written no earlier than spring 1991. It is plausibly the same text, but **I have not compared it with the journal pagination or wording, and the journal version is paywalled** (Unpaywall: oa_status closed, no repository copy; Semantic Scholar: openAccessPdf closed; JSTOR page returns a gate). So everything here is [read, WP]: true of the working paper, **presumed but not proven true of the journal text**.
- **Correction to the research map.** D591 and file 066 give "World Politics 43(1)". It is **44(1)** (Crossref, and file 089 already has 44).
- **Routes tried.** Duke old link (econ.duke.edu/uploads/assets/People/Kuran/Now out of Never.pdf, from Kuran's site) returns 404; sites.duke.edu/kuran/... 404; JSTOR gated; Cambridge Core page loads but is the paywalled record; the Western Ontario repository copy worked.

## 1. What the paper is

A verbal-and-numerical theory paper plus a historical application. **It contains no displayed equations at all.** The model is stated in words (pp. 11-13) and in worked ten-person threshold sequences (pp. 14-19); the formal version is delegated to footnotes: fn 31 and fn 80 point to Kuran 1989 ("Sparks and prairie fires", Public Choice 61(1): 41-74, DOI 10.1007/BF00116762, Crossref-confirmed) as where the theory is "developed more fully" and where the unequally weighted version lives; fn 30 points to Kuran, "Private and public preferences", Economics and Philosophy 6 (1990): 1-26 (DOI 10.1017/S026626710000064X, Crossref-confirmed) for "a detailed analysis of this tradeoff" between the external and internal payoffs. Sections: 1 amazement; 2 critique of structuralist, rational-choice and relative-deprivation theories; 3 preference falsification and revolutionary bandwagons (the model); 4 communism's stability; 5 the 1989 revolution; 6 the predictability of unpredictability.

## 2. The model as the working paper states it

**Operands [read, WP pp. 11-13].** A society of members indexed by i. Each faces a binary public choice: support the government or oppose it. **Private preference** x^i is "effectively fixed at any given instant"; **public preference** is "a variable under his control". Where they differ the individual is engaged in **preference falsification** (p. 11). S = size of public opposition as a percentage of the population, initially near 0; a revolution is "an enormous jump in S" (p. 12).

**The payoff trade-off [read, WP pp. 12-13].** Two payoffs, "one external and the other internal":
- **External payoff** to siding with the opposition: personal rewards and punishments; "apt to become increasingly favorable (or increasingly less unfavorable) with S" because the chance of persecution falls and "the fewer hostile supporters of the government he has to face". Government supporters persecute dissidents "as part of their personal efforts to establish convincing pro-government credentials" (p. 12).
- **Internal payoff**, "rooted in the psychological cost of preference falsification": suppressing one's wants "entails a loss of personal autonomy, a sacrifice of personal integrity"; discomfort greater "the more so the greater the lie". Postulated: "person i's internal payoff to supporting the opposition varies positively with his private preference, x^i" (p. 13).
- **Revolutionary threshold T^i**: the value of S at which "his external cost of joining the opposition falls below his internal cost of preference falsification"; a number between 0 and 100 (p. 13).

**Comparative statics of T^i, as stated [read, WP p. 13].** T^i falls if (a) x^i rises (more sympathetic to opposition); (b) the government becomes less efficient, or the opposition more efficient, at rewarding supporters and punishing rivals ("anything that affects the relationship between S and the individual's external payoff"); (c) "i develops a greater need to stand up and be counted", because the internal cost then dominates "at a lower S".

**Equilibrium and bandwagon, in the paper's own worked terms [read, WP pp. 14-19].** Threshold sequence = the list of the ten persons' T^i, each person weighing 10 percent. A value of S is an **equilibrium** if "self-sustaining"; if the next person's threshold is at or below S the move is "self-augmenting" and the process runs on to the next equilibrium. Worked cases, all re-computed by me and correct:

| Sequence | Start | Perturbation | Result |
|---|---|---|---|
| A = (0,20,20,30,40,50,60,70,80,100) | S=10 equilibrium | person 2's T drops 20 to 10 (A') | S: 10, 20, 30, ... 90; "revolutionary bandwagon"; person 10 (T=100) stays |
| B = (0,20,30,30,40,...,100) | S=10 | same drop (B') | S rises to 20 and stops: new S is self-sustaining |
| C = (0,20x7,60,100), mean 30 | S=10 | any one of the seven 20s drops by 10 | S goes 10 to 90 |
| A' mean 46 vs C mean 30 | | | A' explodes, C stays at 10 without the perturbation |
| D = (0,30x8,100) | S=10 | every threshold between 10 and 90 falls by 10 (D') | all eight now at 20, "willing to switch ... but only if someone else goes first. No one does" (p. 17); S stays 10 |

**Revolutionary-bandwagon condition, restated.** [derived by me, consistent with every worked case; **not stated by Kuran in this form in the text read**.] With N(S) = share of persons with T^i <= S, S is an equilibrium iff N(S) = S; a bandwagon from S0 runs while N(S) > S and stops at the first S with N(S) = S. This is exactly Granovetter's fixed-point map (file 066), so Kuran 1991 adds no new aggregation rule; what it adds is the account of where T^i comes from and of why N is unobservable.

## 3. Results and claims, with scale

All at **crowd/mobilisation scale, national (six East European states) or stylised n = 10**.

1. **Distribution, not level, drives the outcome [read, p. 16].** "One sufficiently disaffected person with a threshold of 10 may do more for a revolution than seven individuals with thresholds of 20." Mean threshold is the wrong summary: A' (mean 46) explodes, C (mean 30) does not. Kuran's use: this is why the relative-deprivation theory, which sums discontent, fails.
2. **Small differences, large effects [read, pp. 14-15, 17].** B vs A differ in one element; D vs A, B, C differ so that the same structural shock (everyone's threshold falls by 10) gives an explosion in three settings and nothing in the fourth. Structuralism and individualism are "essential components of a single story" (p. 17).
3. **Pluralistic ignorance [read, pp. 15, 26].** Thresholds are not common knowledge; "a society can come to the brink of a revolution without anyone knowing this". A regime that knows falsification is widespread "has no interest in publicizing" it, so it discourages independent polling (pp. 15-16).
4. **Thresholds depend on S itself [read, pp. 19-20].** Citing Tocqueville ("a grievance comes to appear intolerable once the possibility of removing it crosses men's minds"): the threshold sequence is "itself dependent on the size of the public opposition", so a bandwagon may be "the joint outcome of two mutually reinforcing trends: a fall in thresholds and a rise in public opposition". **This is the one structural addition beyond a fixed-F map**: T becomes T(S), i.e. a feedback from the aggregate to the member parameter. No functional form is given.
5. **Unequal weights [read, p. 37].** "A Politburo member distancing himself from the Party leader does more to expose the regime's vulnerability than a greengrocer who stops displaying the obligatory Marxist slogan"; a realistic S would be an unequally weighted sum "where the weights correlate with levels of relative influence". The central argument "would remain unaffected". Defections of officials and security forces are the strongest signals (p. 37). No weights are specified; the 1989 paper is cited for the formal version.
6. **Post-revolutionary falsification hides the cause [read, pp. 17-19].** The last jumpers on the bandwagon (A': person 9, T=80) have every reason to claim they always opposed the regime; so after the event it looks as though there was even less private support than there was. Historians face "great difficulty" telling A from C (p. 19).
7. **Contagion across states [read, p. 38].** Prague banner: "Poland--10 years, Hungary--10 months, East Germany--10 weeks, Czechoslovakia--10 days." "Each successful challenge ... lowered the perceived risk of dissent in the countries still under communist rule. In terms of our model, revolutionary thresholds in neighboring countries fell." Romania's late and bloody case is told as the same process (p. 39).
8. **Discourse feedback on private preference [read, pp. 28-29, 33, 38].** Falsifying people distort public discourse, which "affected the evolution of East European private preferences" (mental partitioning; Marxist forms of thought blunted articulation of alternatives). Glasnost then "probably pushed the private preferences of East Europeans against communism". So x is **endogenous to the falsification** it is meant to explain; the model's x^i is held fixed only "at any given instant".
9. **Speed as a determinant [read, pp. 38 and fn 81].** Faster mobilisation left officials and Soviet hard-liners no time to coordinate a response.
10. **Conclusion: prediction is limited in principle, by imperfect observability [read, pp. 40-45].** "Major revolutions are likely to come again and again as a surprise." Not unobservability: "a continuum"; Norway, Switzerland, France more predictable than Pakistan, Brazil, Ghana because less falsification about the political system (p. 44). "If we possessed a reliable technique for measuring people's revolutionary thresholds, we would see what it would take to get a revolution started" (p. 44). The theory "is fully falsifiable" by two routes (p. 45): a string of successful forecasts would render it suspect, and, "in principle, if not in practice", it "can also be falsified by showing that preference falsification was not a factor in unanticipated revolutions of the past".

**The drive vocabulary is Kuran's own, once [read, p. 25]:** the intrapersonal conflict "is rooted ... in the clash between the individual's drive to exercise autonomy and his need for social acceptance. Until 1989 most East Europeans tended to resolve this chronic clash in favor of social acceptance." Fear is explicit too: after the tipping "fear changed sides: where people had been afraid to oppose the regime, they came to fear being caught defending it" (p. 36).

## 4. Empirical content, with scale and exactness

All support is **case narrative plus three survey series**; none estimates T, x or F; none tests an equation.

- **Allensbach, East Germany, Feb-Mar 1990 [read, p. 4].** "A year ago did you expect such a peaceful revolution?" 5% yes; 18% "yes, but not that fast"; 76% totally surprised. Described only as "a broad sample of East Germans"; sample size not given in the text. Question 36, Institut fur Demoskopie Allensbach archive 4195 GEW. Kuran notes the hindsight bias (I-knew-it-would-happen fallacy; Fischhoff 1975) would only inflate foreknowledge, so true surprise was higher. **Scale: individual belief about a national event.** This measures surprise, not thresholds.
- **Leipzig Central Institute for Youth Development, trade-school students, East Germany [read, pp. 27, 33].** "I am a devoted citizen of the GDR": 1983 46% endorse / 45% with reservations / 9% reject; October 1989 15 / 60 / 25. "Socialism will triumph throughout the world": 1984 50 / 42 / 8; October 1989 3 / 27 / 70. Little variation 1970-85. Kuran: "may, of course, have been based on a flawed methodology" and reads the post-1985 fall as a rise in discontent that "must have lowered the revolutionary thresholds". Sample sizes not given; one non-random subpopulation; government-run surveys from a regime in which, on Kuran's own argument (pp. 15-16, 26), respondents falsify and results were kept secret. **Blunt reading:** he uses the flat 1970-85 series as evidence that private support was real, and the 1989 collapse as evidence that thresholds fell. The same instrument cannot be both falsified (his theory) and informative (his use). A drop in a falsified series is evidence of a change in falsification risk as much as in private preference, which is what the model says too, so the data cannot separate the two.
- **Surveys of East Europeans travelling abroad, by Western organisations in the 1970s-80s, as reported by Hart 1983 [read, p. 27, second-hand citation].** Henry O. Hart, "The tables turned: If East Europeans could vote", Public Opinion 6 (Oct/Nov 1983): 53-57 (fn 58; not opened; no DOI). In free elections the Communist Party "at most a tenth of the vote"; socialists would win.
- **Case chronology [read, pp. 33-39].** Early October 1989 East German officials refuse Honecker's order to fire; Leipzig 9 October; Gorbachev's "Sinatra doctrine" 25 October; Bulgaria early November; Czechoslovakia 24 and 27 November (general strike; party gave way "within a matter of hours"); Romania December. These are told as instances; no counterfactual and no comparison group (no failed cases beyond Romania's bloodier route, and the earlier crushed risings of 1953, 1956, 1968, which he calls exceptions that prove the rule, p. 21).
- **Earlier surprises [read, pp. 40-42]:** France 1789, Nazi takeover, Iran 1979, Russia Feb 1917, Hungary 1956, Prague 1968, listed as the same pattern; evidence is quotation of contemporaries' astonishment.

**Not supplied by this paper:** effect sizes, out-of-sample tests, replication, any estimate of how many people had low thresholds. The alternative explanations of 1989 (informational cascades, Lohmann 1994; strategic substitutes in the Hong Kong field experiment, Cantoni et al. 2019) are in file 089 [sa from 089] and are not addressed here; Cantoni et al. challenges the complementarity assumption (more participants make joining more attractive) that the whole threshold structure rests on.

## 5. How 1991 differs from 1989 (against file 089's reading of the 1989 text)

File 089 read Kuran 1989 sections 1-5 and the opening of 6 at source and reports equations (1)-(9). Compared with that:

| Point | 1989 (as read in 089) | 1991 working paper (read here) |
|---|---|---|
| Form | Formal: Y = sum w^i y^i; V = R + N; threshold function x(S^e); S = g(x(S^e)); S* revolutionary potential | Verbal; discrete ten-person sequences; **no displayed equation** |
| Motives | reputational utility R (f(s), F(S)) and integrity N(1-abs(x-y)) | **external payoff** (rises with S) and **internal payoff** (rises with x^i, "personal integrity"); terms "reputational" and "expressive" not seen (see caveat) |
| Weights | w^i sum to 1; revolution by "a small, but influential, share" | equal 10% weights in the examples; unequal weights discussed in prose, formalism deferred to 1989 (p. 37) |
| Extra determinant of T | exogenous shifts in R or g | adds "need to stand up and be counted" (p. 13) |
| Dynamics | comparative statics; equilibrium counts | adds T as a function of S (p. 19), x as discourse-dependent (pp. 28-29, 33), cross-country contagion (p. 38), post-hoc falsification (pp. 17-19) |
| Precipitation results | three results (S^e jump, threshold shift, g shift) | not restated; "structural shock" plus one chance egg-thrower (p. 14) is the same logic |
| Revolutionary potential S* | defined, Table 1 | absent |
| Evidence | cases | cases plus Allensbach and Leipzig survey series |

**Net:** the 1991 paper is the same model with its machinery removed and its application and its consequences for prediction added. A reader who wants the equations must use 1989; a reader who wants the 1989 case and the unpredictability claim should use 1991.

## 6. Ledger L3991 (Kuran's utility components): settled, with a caveat

L3991 pitted 089 (Kuran 1989 read at source: **reputational utility and integrity utility**) against 066 (**intrinsic, expressive, reputational**, via Rasmusen's review and Brummitt et al.).

- **089 is right about the 1989 paper.** Already confirmed by 089's own validation pass.
- **066's triple belongs to a different text.** File 066 itself says (and 089 §3 confirms) that the intrinsic/expressive/reputational vocabulary is Rasmusen's account of the **1995 book** *Private Truths, Public Lies*; Brummitt et al. describe the 1989 model with two components. So the two files were not describing the same text, and the contradiction is a **scope error in 066**, not a disagreement about the 1989 or 1991 paper.
- **The 1991 working paper is consistent with 089, not 066.** Two payoffs: external (reward and punishment, rising with S) and internal (integrity cost of falsification, rising with x^i). The word "integrity" appears as such ("need for integrity", "being true to himself", p. 13); the phrase "need to be true to himself" names the internal motive again on p. 20. The one addition, "a greater need to stand up and be counted" (p. 13), is a person-level weight on the internal payoff. It resembles what Rasmusen calls expressive utility, but **I do not claim they are the same**: Rasmusen's expressive utility is a separate term in the 1995 book; here it is a parameter of the internal payoff.
- **Caveat:** "reputational" and "expressive" were not seen on any page I read, but the pages were images and I did not search by string; Kuran names the external payoff as rewards, punishments and "convincing pro-government credentials", i.e. what 1989 calls reputational utility. The mapping external = reputational, internal = integrity is the natural reading and rests on the content of pp. 12-13, not on shared terms.

**Recommended edit to file 066 (not made; this task touches one file):** (i) change "World Politics 43(1)" to 44(1) wherever it occurs; (ii) in §3 state that the "intrinsic / expressive / reputational" triple is the **1995 book as summarised by Rasmusen**, and that the 1989 paper (read in 089) and the 1991 working paper (read in 099) both use **two** components, reputational/external and integrity/internal; (iii) mark Kuran 1991 as **read in a working-paper version** (099), no equations; (iv) point to 089 §2 and 099 §5 for the equation versus the narrative. Close L3991 as resolved: scope error, no substantive conflict, 089's two-component form stands for 1989 and 1991.

## 7. Group size (n) and composition

- **n.** The model has no n. Examples use n = 10 with each person 10 percent (p. 37); in general n enters only through weights; "each individual carries a weight of 10 percent" is a unit choice. The text does not say what happens as n grows, except implicitly that the unobservable distribution of thresholds, not headcount, matters. The case scale is nations of millions; there is no meso-level (group, firm, crowd of thousands) test.
- **Composition.** Everything depends on the **shape** of the threshold distribution: a person with T = 0 is needed to start (S=10 is "one person"), gaps in the sequence stop a cascade (B vs A), and a mean can mislead (A' vs C). Composition by role also matters: officials and security forces weigh more than ordinary citizens (p. 37). Intellectuals have low thresholds because they value self-expression (p. 13-14, Schumpeter). Definition of group: "a society", a regime; the opposing parties are exogenous.

## 8. Consent or manipulation

The theory is descriptive; it has no intervention operator. The levers named: **information control** by regimes (censorship, secret polls; pp. 15-16, 26, 44), which works by **manipulation** of what people can know about each other; **organised oppositions** that raise the external payoff and "through propaganda, shift people's private preferences in favor of change" (pp. 20-21), which can be either; **Soviet signals** (glasnost, the Sinatra doctrine) that lowered thresholds without intending to (consent-neutral; not an intervention aimed at the crowd). No experiment, so no estimate of whether manipulation works. The model does imply that an interventionist who could measure T could trigger a bandwagon with one well-chosen person; Kuran says no such measurement exists (p. 44).

## Does it reduce to a drive basis?

**Partly, at the individual parameter; not at the structure.**

Reduces:
- The threshold T^i is a **balance between two person-level motives** that Kuran himself calls drives: the "drive to exercise autonomy" (integrity cost of falsification, rising with private preference x^i) against "his need for social acceptance" and fear of punishment (the external payoff, p. 25). Fear is explicit (p. 36). "Need to stand up and be counted" (p. 13) is a third, person-level weight. So T^i is plausibly a function of a small drive vector plus a private preference. This is a mapping of a parameter, however; the paper supplies no functional form.

Does not reduce:
- **Pluralistic ignorance and observability.** What drives the unpredictability is that each person's x^i and T^i are hidden. That is an **epistemic state about others** (a belief, not a drive), and it is the paper's central result.
- **The distribution of T and its shape.** The cascade outcome depends on the gaps and shape of the whole sequence, a property of the group rather than a drive of any member. Group-level composition is not derivable from drives of individuals taken one at a time.
- **Influence weights** (Politburo vs greengrocer) are positional/status, not a drive.
- **Exogenous structural shocks** (Soviet policy, Sinatra doctrine) enter as parameter changes, not as drives.
- **Endogeneity of x and T.** Private preference is shaped by public discourse and by the size of the opposition (pp. 19-20, 28-29); the drive that is "fixed at any given instant" is therefore not primitive over time. Drives as primitives would need an endogenous-preference rule that the paper does not give.

## What does it predict or control, and how well?

- **Outcome.** The size of public opposition S for a society, and above all a statement about **when it cannot be forecast**. It predicts surprise: revolutions will keep surprising, more so where falsification is high. It does not forecast any event, timing or country.
- **Out-of-sample evidence.** None. The 1989 application is retrospective narrative of the autumn-1989 chain of events; the survey series are small, non-random, government-run and ambiguous (Section 4). Kuran names two falsification routes (p. 45): successful forecasting by a rival theory, which would count against his, and showing that preference falsification "was not a factor in unanticipated revolutions of the past". The first is unusual; the second is an ordinary historical test, though he concedes it is hard "in practice". [Corrected in validation: an earlier draft said forecasting was the only route.]
- **Effect sizes.** No estimate of any threshold, any distribution or any parameter.
- **Failures and caveats.** (1) Not tested against failed or crushed cases beyond the earlier risings, which are dismissed as exceptions. (2) Complementarity (more joiners lowers the cost of joining) is assumed; a field experiment (Cantoni et al., [sa from 089]) finds strategic substitutes. (3) The same survey instrument is used as both falsified and truthful. (4) The imperfect-observability claim makes the model hard to disconfirm with ordinary data (Kuran's second route, historical evidence on falsification, is the exception he offers), which is a strength for the theory's honesty and a weakness for control. (5) No control: no operator for steering S.
- **For the algebra.** What is usable is the **structure**: private state vs expressed state as separate operands; a threshold per person derived from two named motives; an aggregate map of Granovetter type; and an explicit limit on prediction. What is not usable as an equation: anything calibrated.

## Unconfirmed

- Whether the **journal text** (World Politics 44(1): 7-48) matches this working paper; the journal copy is paywalled on every route tried.
- The working paper's exact date (repository metadata says 1992-01-01; internal evidence says after May 1991).
- Footnote 31's AER P&P page numbers ("81 (May 1991), 123-27"): the piece is not on Crossref (JSTOR-era AER P&P); Duke's Scholars record confirms AER 81(2), May 1991 but gives no pages, and a search summary of Kuran's own site gives **121-125**, so the working paper's "123-27" is probably a pre-publication page forecast; not settled from a primary record. The companion piece "The East European Revolution of 1989: Is it surprising that we were surprised?" appears on the Duke repository but was not read.
- Absence claims about words ("reputational", "expressive") rest on reading page images without text search.
- Sample sizes and sampling frames of the Allensbach and Leipzig surveys are not in this paper; the Leipzig tables are an unpublished mimeo (Friedrich, Ladenburg conference February 1991), not obtained.
- I did not re-read Kuran 1989 here; the comparison in Section 5 relies on file 089's account of that text (read at source there).

## Validation log (2026-10-30)

Re-downloaded the Western Ontario PDF (48 pages, image-only, ScanSnap scan, confirmed) and read printed pp. 4, 12-20, 25, 27, 33, 37, 44-45 as page images myself; every [read] claim checked on those pages held, with the fixes below.

- ✓ Kuran 1991, World Politics 44(1): 7-48, DOI 10.2307/2010422: Crossref confirms title, sole author, 44(1), 7-48, 1991-10; Unpaywall oa_status closed (re-checked), so the journal text stays unread and the [read, WP] scoping stands.
- ✎ Kuran 1991 working paper (UWO PPE No. 27): model pp. 12-13, sequences A, A', B, B', C, D, D' (pp. 14-17), means 46 and 30, post-revolutionary falsification (p. 18, person 9 T=80), Tocqueville T(S) (p. 19), drive quote (p. 25), Leipzig figures (pp. 27, 33), Allensbach 5/18/76 (p. 4), weights (p. 37), imperfect observability (p. 44) all confirmed. Fixed: p. 37 quotation ("Politburo", not "Politbureau", and the greengrocer clause completed); p. 45 falsifiability claim, which omitted Kuran's second route (showing falsification played no part in past surprises), corrected in §3 item 10 and the prediction section; "integrity" also on p. 13, not only p. 20; Allensbach "broad sample" added.
- ✓ Kuran 1989, Public Choice 61(1): 41-74, DOI 10.1007/BF00116762: Crossref confirmed; added to §1.
- ✎ Kuran 1990, Economics and Philosophy 6: 1-26, DOI 10.1017/S026626710000064X: cited in the WP's fn 30 for the payoff trade-off; Crossref confirmed; added to §1.
- ? Kuran 1991 AER P&P 81(2): exists (Duke Scholars record); pages 121-125 per a search summary vs the WP's "123-27"; no Crossref record; left in Unconfirmed.
- ✎ Hart 1983, Public Opinion 6: 53-57: the surveys are Western organisations' surveys that Hart reports; reworded; not opened, no DOI.
- ✓ Fischhoff 1975, JEP:HPP 1(3): 288-299, DOI 10.1037/0096-1523.1.3.288: Crossref confirmed; cited in WP fn 17 as stated.
- ✓ Granovetter 1978, AJS 83(6): 1420-1443, DOI 10.1086/226707: Crossref confirmed; cited in WP fn 33.
- ✓ Lohmann 1994, World Politics 47(1): 42-101, DOI 10.2307/2950679: Crossref confirmed; content [sa from 089], not opened here.
- ✓ Cantoni, Yang, Yuchtman and Zhang 2019, QJE 134(2): 1021-1077, DOI 10.1093/qje/qjz002: Crossref confirmed; content [sa from 089], not opened here.
- ✓ Allensbach (fn 16) and Leipzig Zentralinstitut mimeo (fn 59, Walter Friedrich, Ladenburg, February 1991): citations as given in the WP; primary data not obtained.

Sources opened: 7 (WP PDF, 15 page images; Crossref records for 7 DOIs counted as 1; Unpaywall; Duke Scholars record; Kuran-site search; DukeSpace, bot-gated; one null search).

Verdict: the file is accurate and honestly scoped. Every load-bearing worked example and quotation checked against the page images held, and the derived bandwagon condition is correctly labelled as derived. One substantive error was corrected: Kuran does not make forecasting the only falsification route, so the "untestable by design" criticism was overstated. Nothing here is an equation from Kuran, so nothing [sa] feeds one; the paper's content is [read] only for the working paper, not the journal text.

## Cross-checks (2026-10-30)

Grep of `docs/prior-work/` for Kuran, the 1989 and 1991 papers, the DOIs, Granovetter, Cantoni, Hart, Allensbach and Leipzig. Files that mention Kuran: 066, 067, 068, 089, 093, 097. No file other than 099 reads the 1991 text. This section records agreements and contradictions only; no other file was edited.

**Agreements**

- The 1991 DOI 10.2307/2010422 and the 1989 DOI 10.1007/BF00116762 are the same in 066, 089 and 099. The 1991 volume is 44(1) in 066 (validation log, line 335) and 089 (line 71). 066 does not give 43(1); that figure is only in research map D591, which is not in this folder.
- The formal threshold equations (S = g(x(S^e)), the fixed-point structure) are in the 1989 paper, read at source in 089 section 2 and cited as Eq. 8 in 066 section 3. 099 section 5 and 089 agree that the 1991 working paper has no displayed equation.
- The 1991 working paper's bandwagon is the same fixed-point shape as Granovetter's map. 066 section 3 and 089 section 5 say the same of the 1989 model. 099 adds nothing new in aggregation.
- Complementarity (more joiners lower the cost of joining) is the assumption Cantoni et al. challenge. 097 section 4, 099 section 4 (failure 2) and 089 agree.
- Kuran's limit-of-prediction claim (revolutions unpredictable) is recorded the same way in 089 section 5 and 099 section 10.
- Cantoni et al. (QJE 134(2), DOI 10.1093/qje/qjz002) is recorded with the same DOI in 089 and 097, and 099 cites it as [sa from 089].

**Contradictions**

- Utility components. 089 section 2 (1989 read at source): reputational utility and integrity utility. 066 section 3 (secondary, via Rasmusen on the 1995 book and Brummitt et al.): intrinsic, expressive and reputational. 099 section 6 says the 066 triple belongs to the 1995 book and closes the question as a scope error. Verdict: **unresolved**. The validation log of 089 (item C1) records it as unresolved, and 099 has not read the 1989 text, so its scope-error explanation is an argument, not a settled result.
- Distribution-shift route. 066 section 3 (secondary, Brummitt et al. citing 1989 section 4.1) gives a shift of the private-preference distribution toward the opposition as one of two routes to a saddle-node. 089 section 2 result 3 (read at source, Fig. 6) says an upward shift of g can set the stage but cannot precipitate a revolution alone. Verdict: **unresolved** (089 item C2). 099 does not address it.
- Volume of the 1991 paper. 099 (Provenance, correction to the research map) says D591 and 066 give 43(1). 066 gives 44(1) and 089 gives 44. Verdict: **resolved** by the Crossref check in the 066 and 089 validation logs (44(1)). The 43(1) figure is in D591 only.

**Ledger lines** are in the structured output of this pass; the lines below are the same claims in prose for a reader of this file.

- Drives (read, p. 25): the clash between the drive to exercise autonomy and the need for social acceptance; fear of punishment (p. 36); "need to stand up and be counted" (p. 13) is a person-level weight on the internal payoff.
- Definitions (read, pp. 12-13): external payoff rises with S; internal payoff rises with private preference x^i; T^i is the S at which external cost of joining falls below internal cost of preference falsification; T(S) depends on S (p. 19).
- Derived, not stated by Kuran: bandwagon stops at the first S with N(S) = S, where N(S) is the share with T^i at or below S. This is Granovetter's fixed-point map. Provenance is [sa] because it is 099's derivation.
- Empirical (read, stylised n = 10, p. 16): one disaffected person with threshold 10 can do more than seven with threshold 20; the mean is the wrong summary (A' mean 46 explodes; C mean 30 does not).
- Empirical (read, national survey series, pp. 4, 27, 33): Allensbach East Germany 5/18/76 (sample size not given); Leipzig trade-school students 1983 vs October 1989, with no sample sizes and a government-run instrument. Neither estimates a threshold.
- Limit (read, pp. 44-45): prediction is limited by imperfect observability, and the theory is falsifiable by a rival forecast or by showing falsification played no part in past surprises.

**Not done.** The journal text of 1991 (World Politics 44(1)) was not read by anyone in this folder; every 1991 claim here is [read, WP] only. No file was committed.
