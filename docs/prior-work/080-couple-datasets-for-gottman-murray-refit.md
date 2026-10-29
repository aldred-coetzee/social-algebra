# Prior work 080: couple datasets for refitting and falsifying the Gottman-Murray equations

Direction: D504
Date: 2026-10-29. Kind: data. Question: which couple datasets could be used to refit or falsify the Gottman-Murray influence-function model. Cross-references: `059` (the model read at source; this file relies on its [read] numbers), `20` section 1, `060`, `061` (Boker-style coupled oscillators), `070`.

**Method and honesty note (read this first).** The web-search budget for the turn was exhausted before I began, and most data-portal pages returned 403, 404 or 500 to the fetch tool (GESIS, ICPSR, pairfam.de, Fragile Families, Wikipedia pages). So: **no dataset access page, licence, or variable list was read in this pass.** What I did verify is bibliographic: every DOI below was resolved against Crossref on 2026-10-29 (title, authors, year matched). Everything about sample size, cohorts, access terms and variables is tagged **[background, unverified]** (my memory, not checked) and must be confirmed from the portals before any application is written. Numbers about the Gottman-Murray model tagged [read-059] are taken from file 059, which read the primary papers. Tags: **[crossref]**, **[read-059]**, **[derived]** (my arithmetic), **[background, unverified]**.

## Summary

1. **What a refit of the Gottman-Murray equations needs is rare.** The model (059) is fitted on a scalar weighted-valence score per spouse per 6-second block (1999: 150 blocks per spouse, 75 per half, from a 15-minute conflict discussion; the older 1995 data were per speaking turn, and the "75 interacts" figure belongs to that RCISS data, not the 1999 sample), using only the subset of time points where the partner's score is zero for the uninfluenced part, with at least 10 such points per half [read-059]. Any dataset that lacks turn-level or sub-minute coded interaction **cannot refit the influence function**. It can test only downstream claims (that couples' negativity predicts later dissolution).
2. **Of the four seeds, none (as far as I can tell) contains observed, turn-coded conflict interaction that is publicly downloadable.** pairfam is large self-report panel data; Family Life Project is a child-development cohort; Early Years of Marriage is interview and questionnaire data. The one dataset that does have what the model needs is the Gottman lab's own; **I found no evidence that its raw coded data are public** [unverified: I could not search]. This is the central finding: the model has been fitted almost entirely on the Gottman lab's data, and independent refitting is limited by data availability, not by method. *Validation correction:* re-estimation does exist. Hamaker, Zhang & van der Maas (2009) showed the Gottman-Murray model is a special case of the threshold autoregressive (TAR) model, proposed a new estimator, and fitted it to three dyads; Madhyastha, Hamaker & Gottman (2011) then fitted TAR-estimated influence functions to the lab's moment-to-moment 6-second affect data (couples N = 124, newlyweds N = 130) and compared influence-function forms by BIC [abstracts read]. The latter has Gottman as co-author and uses lab data, so it is not an independent-sample replication, but it shows the lab has shared coded series with outside methodologists.
3. **There are two honest routes.** (a) Request the original coded series from the Gottman lab (precedent: Madhyastha, Hamaker & Gottman 2011 used them) and refit, using the TAR estimator of Hamaker et al. (2009), with cross-validation. (b) Collect new data (sample sizes in section 4). Meanwhile public panels can test a **coarser corollary**, not the influence function, namely that a time-averaged negativity-minus-positivity index predicts dissolution. That corollary is already well supported (Gottman et al. 1998; Carrere et al. 2000), and is mostly the same finding as the uninfluenced steady state (059: "its predictive power is largely the weighted score's predictive power").
4. **Power is the binding constraint, and it is sharper than the original sample suggests.** The one significant husband-threshold result had F(1,123) = 8.25 [read-059], i.e. r about 0.25 [derived: r = sqrt(F/(F+df))]. Detecting r = 0.25 at 80% power, alpha .05 needs N about 123; a replication should assume a shrunk effect (r = 0.125, plausible given winner's curse on ten uncorrected tests) which needs N about 500 [derived, Fisher z]. With a divorce rate of 17 in 125 [read-059], 500 couples gives about 68 events over 3-6 years.
5. **A falsifiable test list is given in section 5**, each with the data it needs, so that a dataset can be matched to a test rather than the reverse.

---

## 1. What the model's own data look like (the benchmark)

[read-059] Cook et al. 1995: 79 couples assessed 1983, 73 followed up 1987, RCISS speaker codes per turn. Gottman, Swanson and Murray 1999: 179 screened, 130 newlyweds in the lab (Puget Sound, 1989-92), followed 3-6 years, 17 divorces, 125 couples with estimable models; 15-minute conflict discussion; SPAFF weighted score per 6-second block, range -24 to +24; inter-rater kappa .80 average. Gottman et al. 2003: heterosexual, gay and lesbian couples, observer correlation .90 married and .52 gay/lesbian.

Citations resolved [crossref]:
- Gottman, Swanson & Murray (1999), *J Family Psychology* 13(1):3-19, doi 10.1037/0893-3200.13.1.3.
- Gottman, Swanson & Swanson (2002), "A general systems theory of marriage: Nonlinear difference equation modeling of marital interaction", *Personality and Social Psychology Review* 6(4):326-340, doi 10.1207/s15327957pspr0604_07 (not read).
- Gottman, Murray, Swanson, Tyson & Swanson (2002), *The Mathematics of Marriage*, MIT Press, doi 10.7551/mitpress/4499.001.0001 (not read; the book is where any fuller data description should be).
- Ryan, Gottman, Murray, Carrère & Swanson (2000), "Theoretical and mathematical modeling of marriage", chapter in *Emotion, Development, and Self-Organization* (Cambridge UP), pp. 349-372, doi 10.1017/cbo9780511527883.015 (not read).
- Gottman, Coan, Carrere & Swanson (1998), *J Marriage and the Family* 60(1):5-22, "Predicting marital happiness and stability from newlywed interactions", doi 10.2307/353438 (not read; Crossref gives first page 5 only, end page from memory).
- Carrere, Buehlman, Gottman, Coan & Ruckstuhl (2000), *J Family Psychology* 14(1):42-58, "Predicting marital stability and divorce in newlywed couples", doi 10.1037/0893-3200.14.1.42 (not read).
- Gottman (2023), "Replication and Extension", chapter in *What Predicts Divorce?* (Routledge), pp. 268-289, doi 10.4324/9781003429807-13 [crossref record only; not read]. *Validation correction:* this is a reissue, not new work. *What Predicts Divorce?* is Gottman's 1994 Erlbaum book (reviewed in *Family Relations* 44(1), January 1995, doi 10.2307/584749; also reissued by Psychology Press 2014, doi 10.4324/9781315806808). The chapter therefore predates the 1995 and 1999 influence-function papers and almost certainly concerns the divorce-prediction cascade, not a refit of the influence functions.
- Hamaker, Zhang & van der Maas (2009), "Using threshold autoregressive models to study dyadic interactions", *Psychometrika* 74(4):727-745, doi 10.1007/s11336-009-9113-4 [crossref abstract read]. Gottman-Murray model shown to be a special case of TAR; new estimation procedure compared by simulation with Gottman-Murray's; empirical example on three dyads (source of the three dyads not read).
- Madhyastha, Hamaker & Gottman (2011), "Investigating spousal influence using moment-to-moment affect data from marital conflict", *J Family Psychology* 25(2):292-300, doi 10.1037/a0023028 [PubMed abstract read]. Couples N = 124 and newlyweds N = 130, 6-second affect, TAR estimation, influence-function forms compared by BIC.

**Blunt note on the benchmark:** the in-sample parameters are what 059 reports; **no independent-sample replication of the threshold parameters was found**. Re-estimation on the lab's data with a different estimator exists (Madhyastha, Hamaker & Gottman 2011), and so does an outside-lab method paper with a three-dyad example (Hamaker et al. 2009); neither is an out-of-sample test of the 1999 divorce-prediction parameters. Searches were limited (see Validation log), so this is weak evidence, not proof.

## 2. Candidate datasets (catalogue)

Format: access; variables; sample; which drive/equation it could test. All access and sample statements are [background, unverified] unless marked.

### 2.1 pairfam (Panel Analysis of Intimate Relationships and Family Dynamics)
- **Citation.** Huinink, Brüderl, Nauck, Walper, Castiglioni & Feldhaus (2011), "Panel Analysis of Intimate Relationships and Family Dynamics (pairfam): Conceptual framework and design", *Journal of Family Research* (Zeitschrift für Familienforschung) 23(1):77-101, doi 10.20377/jfr-235 [crossref]. Further: Keller & Nauck (2013), "The German Family Panel (pairfam): Research potential and first results of a multi-disciplinary longitudinal study on partnership and family dynamics in Germany", *Analyse & Kritik* 35(2):321-340, doi 10.1515/auk-2013-0204 [crossref].
- **Access.** Distributed via GESIS as study ZA5678, DOI pattern 10.4232/pairfam.5678.x.y.z [the doi.org redirect to search.gesis.org/research_data/ZA5678 was confirmed, but the page returned 403 and was not read]. Scientific-use file under registration; terms [unverified]. 
- **Design [background, unverified].** Annual waves from 2008/09; three birth cohorts (about 1971-73, 1981-83, 1991-93); roughly 12,000 anchors, with partner, parent and child modules attached for a subset.
- **Variables relevant here [background, unverified].** Self-reported relationship quality, conflict style, conflict frequency, communication, commitment, break-up and separation events, with dates. **No observed interaction, no turn-level data.**
- **Can test.** Not the influence function. Can test: (a) whether reported negativity-style items (the self-report analogue of the uninfluenced steady state) predict separation, with a large number of events; (b) the "four horsemen"-like conflict-style predictors; (c) asymmetry claims (husband-only effect) with partner data, in a sample large enough to have power. Under the drive framing: reported fear/anger in the relationship as a slow state, not as a coupled fast dynamic.

### 2.2 Family Life Project
- **Citation (validated).** Vernon-Feagans, Cox & the Family Life Project Key Investigators (2013), "The Family Life Project: An epidemiological and developmental study of young children living in poor rural communities", *Monographs of the Society for Research in Child Development* 78(5). Chapter I, Vernon-Feagans & Cox, "Poverty, rurality, parenting, and risk: An introduction", pp. 1-23, doi 10.1111/mono.12047; chapter II, Willoughby, Burchinal, Garrett-Peters, Mills-Koonce, Vernon-Feagans & Cox, "Recruitment of the Family Life Project sample", pp. 24-35, doi 10.1111/mono.12048 [crossref].
- **Design.** A representative sample of every baby born over one year to mothers in six poor rural counties, oversampling for poverty and African American families; 1,292 children followed from birth (abstract covers to 36 months); North Carolina and Pennsylvania (from PubMed MeSH terms) [PubMed abstract read]. Birth years 2003-04 and later waves [background, unverified]. Data are largely child-development outcomes and observed parenting.
- **Can test.** Little for this question: couple-level coded interaction is, to my recollection, not a core component; partner/co-parenting measures are reported by the mother. It could supply **co-parenting conflict series** under chronic stress (poverty) and so a different regime (the dark-side attractor, in 059's terms) but not the influence function. Low priority.

### 2.3 Early Years of Marriage Project (Huston and colleagues)
- **Citation.** Huston, Caughlin, Houts, Smith & George (2001), "The connubial crucible: Newlywed years as predictors of marital delight, distress, and divorce", *JPSP* 80(2):237-252, doi 10.1037/0022-3514.80.2.237 [crossref]. Also Huston, Niehuis & Smith (2001), "The early marital roots of conjugal distress and divorce", *Current Directions in Psychological Science* 10(4):116-119, doi 10.1111/1467-8721.00129 [crossref].
- **Design [background, unverified].** Couples married in 1981 in central Pennsylvania, followed for over 13 years with repeated interviews and questionnaires (about 168 couples at start). Variables include affection, "negativity", courtship history and marital outcomes. **Not turn-coded interaction.**
- **Why it matters.** It is the strongest prior challenge to the Gottman account: Huston reports that newlywed (not conflict-discussion) affection and negativity trajectories predicted divorce, with the "disillusionment" pathway of declining love, which is a **slow-state** account, not a fast influence-function account [from the title and abstract-level memory; not read]. That makes it a falsification test of whether the fast dynamics add anything over the slow trend.
- **Access.** Unknown; I could not verify that these data are archived. Likely by request to the investigators [unverified].

### 2.4 Items the seed list implies but I could not source
- **Gottman lab raw coded data.** Not located. Would be the only direct refit. Request route: the authors and publisher of the 2002 book and the 2023 reissue. The Love Lab's archives are held privately [unverified].
- **Fragile Families / Future of Families.** Princeton; couple relationship quality at births and ages 1, 3, 5, 9, 15 for unmarried parents; the fetch returned 403. Self-report only; useful for the slow-state corollary in a high-separation population. [background, unverified]
- **Intensive-longitudinal dyadic data (diaries, EMA).** Boker & Laurenceau (2006), "Dynamical Systems Modeling: An Application to the Regulation of Intimacy and Disclosure in Marriage", in *Models for Intensive Longitudinal Data* (Oxford UP), pp. 195-218, doi 10.1093/acprof:oso/9780195173444.003.0009 [crossref], is the model for fitting coupled difference/differential equations to daily couple data (see 061). Ferrer & Nesselroade (2003), "Modeling affective processes in dyadic relations via dynamic factor analysis", *Emotion* 3(4):344-360, doi 10.1037/1528-3542.3.4.344 [crossref; page range corrected from 344-359], fit dynamic factor models to dyadic affect. These supply the **method**; the datasets are held by the authors [unverified]. Day-level data test coupling and inertia, not the nonlinear threshold, because the unit is a day, not a conversational turn.
- **Liebovitch, Naudot, Vallacher, Nowak, Bui-Wrzosinska & Coleman (2008)**, "Dynamics of two-actor cooperation-competition conflict models", *Physica A* 387(25):6360-6378, doi 10.1016/j.physa.2008.07.020 [crossref; an earlier 2007 SSRN version, 10.2139/ssrn.1066815, lists Liebovitch, Coleman, Vallacher, Nowak & Bui-Wrzosinska, without Naudot]. A cousin model with the same two-actor structure. Whether it has data: not checked.

## 3. What the matched datasets can and cannot do

| Test target | Needs | pairfam | Family Life Project | Early Years of Marriage | Gottman raw data |
|---|---|---|---|---|---|
| Influence function (threshold, slopes) | Turn-level coded affect, both spouses | no | no | no | yes (if obtainable) |
| Inertia and set point, slow scale | Repeated measures per couple | partly (annual) | partly | yes | yes |
| Negativity predicts dissolution | Outcomes with dates | yes (large N) | weak | yes (long follow-up) | yes (17 events) |
| Husband-only threshold effect | Both spouses, sex-specific | yes if partner data | no | yes | yes |
| Out-of-sample parameter validation | Hold-out couples | n/a | n/a | n/a | only with a new split |

## 4. Design implications and power

- **Original effect** [derived from read-059]: F(1,123) = 8.25 gives eta-squared .063, r about .25. Required N for 80% power at alpha .05 with Fisher z: about 123 [derived].
- **Shrunk effect.** Ten parameter tests, four significant, no multiplicity correction [read-059], one sample, outcome-tuned weights [read-059]. Planning for r = .125 needs N about 500 [derived].
- **Events.** At 17/125 (13.6%) over 3-6 years [read-059], N = 500 yields about 68 divorces. If the follow-up is 10 years, the rate is higher and events come sooner, but censoring from attrition dominates.
- **Pre-register** (a) the functional form (bilinear vs ogive), (b) the sign convention for the lag (059 section 6 shows the papers differ), (c) the affect weights, ideally fixed from independent data instead of the divorce-tuned SPAFF weights, (d) a single primary outcome and a multiplicity rule.

## 5. Falsification tests the equations license

Each states a result that would count against the model, and the dataset that could deliver it.

1. **Threshold replication.** Prediction: the husband negative threshold is more negative in couples who later separate. Fail if the effect, in an independent sample with N >= 500, is within +-0.05 of zero in r. Data: new coded interaction or the Gottman raw data held out.
2. **Fast adds nothing over slow.** Prediction (the model's selling point): influence-function parameters predict divorce beyond the time-averaged weighted score. Fail if adding them leaves cross-validated AUC unchanged. Data: Gottman raw data; coded samples. pairfam/EYM can test only the slow side and set the baseline.
3. **Lag form.** The 1995 alternating-turn and 1999/2003 simultaneous versions have different stability conditions (059). Fail the one whose one-step prediction error is larger, in out-of-sample turns.
4. **Bilinear versus linear.** Prediction: separate slopes for positive and negative affect. Fail if a single slope fits as well by cross-validation. The negativity-steeper regularity is claimed in the lab's own samples only [read-059].
5. **Dark-side attractor.** Prediction: some couples have a stable negative steady state. 059 notes most couples had one influenced steady state, so existence is asserted from shape, not tested. Test: count the fitted couples with two stable fixed points.
6. **Mismatch hypothesis.** Unestimable on the same data (Cook et al.). Needs an independent sample typed on one interaction and tested on a second.

## 6. Operand/operator translation

Operands: a dyad, each member a scalar affect state per turn. Datasets differ in the **time-scale at which the operand is observed** (turn, day, year). An algebra that wants to be tested must declare the scale: the same operator "influence of partner on partner" is a one-step map at turn scale, a coupling coefficient at day scale, and a drift (love-decline) at year scale. A dataset can falsify an operator only at its own scale. This is the useful structural fact from this pass: **the three public-style datasets here are all year-scale, and the model is turn-scale, so they do not test the same object.**

## 7. What exists vs what does not

**Exists:** the original coded series (privately held, but shared at least once with outside methodologists: Madhyastha, Hamaker & Gottman 2011); a TAR re-estimation framework for the model (Hamaker et al. 2009); large public panels with self-reported relationship quality and dated separations (pairfam, Fragile Families); a long-running newlywed cohort with interviews (Early Years of Marriage); methods papers for fitting coupled dynamics to daily data (Boker & Laurenceau; Ferrer & Nesselroade).

**Does not (found):** a public, turn-coded, two-spouse conflict-interaction dataset; any independent-sample refit of the influence-function threshold (re-estimation on lab data exists, above); any out-of-sample test of the 1999 parameters; any dataset in the seed list that matches the model's time-scale.

## Unconfirmed

- All access terms, licences, variable lists, cohort definitions and sample sizes for pairfam, Family Life Project and Early Years of Marriage (portals returned 403/404/500 or search budget was exhausted).
- Whether the Gottman lab data are open (the 2023 chapter is a 1994 reissue and is not expected to contain refits; not read).
- Whether any independent group has refit the influence functions on an independent sample. Validation found Hamaker et al. 2009 and Madhyastha et al. 2011 through Crossref, but web search was again unavailable; a forward-citation search on those two papers is the next step. Also unread: the source of Hamaker et al.'s three dyads, and Madhyastha et al.'s results (which form won by BIC).
- Contents of Gottman, Swanson & Swanson 2002, the 2002 MIT Press book, Carrere et al. 2000 and Gottman et al. 1998 (DOIs resolved, texts not read).
- Everything tagged [background, unverified].

## Validation log (2026-10-29)

Every DOI resolved at api.crossref.org/works on 2026-10-29. Web search was unavailable (turn budget exhausted); two abstracts were read via Crossref and PubMed. Arithmetic checked: r = sqrt(8.25/131.25) = .251, eta-squared .063; Fisher-z N = 123.3 (r = .25) and 499.8 (r = .125) at 80%/.05 two-sided; 17/125 = 13.6%, x500 = 68. All ✓.

- ✎ Summary 1: "about 75 interacts per couple" was the 1995 RCISS figure; the 1999 data are 150 six-second blocks per spouse (75 per half), per 059's own correction.
- ✓ Gottman, Swanson & Murray 1999, JFP 13(1):3-19 (numbers via 059 [read]).
- ✎ Gottman, Swanson & Swanson 2002, PSPR: added title and 6(4):326-340.
- ✓ Gottman, Murray, Swanson, Tyson & Swanson 2002, MIT Press.
- ✎ Ryan et al. 2000: added chapter title and pp. 349-372.
- ✎ Gottman, Coan, Carrere & Swanson 1998, JMF: added 60(1).
- ✓ Carrère, Buehlman, Gottman, Coan & Ruckstuhl 2000, JFP 14(1):42-58.
- ✎ Gottman 2023 "Replication and Extension": a reissue of the 1994 Erlbaum book, so it predates the influence-function model; removed the implied "2023 reissue's authors" data route.
- ✎ Huinink et al. 2011: pagination 23(1):77-101 added. ✎ Keller & Nauck 2013: title and 35(2):321-340 added.
- ✎ Family Life Project: citation and DOIs found (Vernon-Feagans, Cox et al. 2013, Monographs SRCD 78(5); mono.12047, mono.12048); "about 1,200" corrected to 1,292 children, six counties [abstract read].
- ✓ Huston, Caughlin, Houts, Smith & George 2001, JPSP 80(2):237-252. ✎ Huston, Niehuis & Smith 2001: title and 10(4):116-119 added.
- ✎ Boker & Laurenceau 2006: book and pages added. ✎ Ferrer & Nesselroade 2003: pages 344-360, not 344-359.
- ✎ Liebovitch et al. 2008: full author list and 387(25):6360-6378; the SSRN version's author list differs (no Naudot).
- ✎ Added Hamaker, Zhang & van der Maas 2009 (Psychometrika 74(4):727-745) and Madhyastha, Hamaker & Gottman 2011 (JFP 25(2):292-300). Both contradict the "no refit" wording, so findings 2, section 1 and section 7 were narrowed to "no independent-sample refit".
- ? pairfam design and access, Early Years of Marriage sample size and archive, Fragile Families: still [background, unverified] (pairfam.de returned 500).

**Verdict.** The bibliography is real: no fabrications, and every DOI resolves to the stated authors and title. The errors were a carried-over "75 interacts" slip, a 2023 chapter misread as new work, missing or wrong pagination, and a gap: the TAR re-estimation literature (Hamaker et al. 2009; Madhyastha et al. 2011) went unmentioned, and it softens the claim that no refit exists. The central conclusion still holds: no public turn-coded couple dataset was found, and the seed datasets are all year-scale, so they cannot test the influence function.

## Cross-checks (2026-10-29)

Method: grepped the other validated files in this directory for the same works, authors, equations and numbers. Overlaps exist with `059`, `20`, `060`, `061`, `078`, `079` and `082`. `059` already carries its own cross-check of this file (its "Cross-checks" section, items 2 and 3). Pairfam, Family Life Project, Early Years of Marriage, Fragile Families, Hamaker et al. 2009 and Madhyastha et al. 2011 appear in no other file, so nothing can be cross-checked for them. No web fetch was needed: the one tension is settled by the abstracts that `20` already read.

### Agreements

- Section 1 benchmark numbers match `059` sections 3, 4.5 and 5: 79 couples assessed 1983 and 73 followed up 1987 (1995); 179 screened, 130 newlyweds, 125 estimable couples, 17 divorces (1999); 15-minute discussion, 150 six-second blocks per spouse (75 per half); at least 10 zero-partner points per half; kappa .80; 2003 observer correlation .90 married vs .52 gay/lesbian (`059` prints .907).
- Summary 1 and Validation log: "75 interacts" belongs to the 1995 RCISS data, not the 1999 sample. Same correction as `059` section 5.2 / Summary.
- Section 4 power arithmetic starts from F(1,123) = 8.25 for the husband negative threshold. `059` Table 1 gives exactly that (-5.36 stable vs -7.71 divorced, p < .01). The 10 parameter tests and no multiplicity correction agree with `059` section 7.
- Section 4 pre-registration items (functional form, lag sign convention, divorce-tuned SPAFF weights) agree with `059` section 6 (lag convention differs between papers) and section 3 (weights tuned on earlier divorce data).
- Section 5 test 6 (mismatch hypothesis unestimable on the same data) agrees with `059` section 5.1 (Cook's concession). Test 5 (existence of a dark-side attractor asserted from shape) agrees with `059` section 6.
- Sections 1 and 7, "no out-of-sample test of the parameters": agrees with `20` section 1 ("not tested out of sample in anything I found"), `059` Summary 3 and sections 7 and 9, and `082`.
- Citations with identical authors, journal, volume, pages and DOI in both files: Gottman, Swanson & Murray 1999 (`059` s1, `20`); Gottman, Swanson & Swanson 2002 PSPR 6(4):326-340; Gottman et al. 2002 MIT Press; Gottman, Coan, Carrere & Swanson 1998, JMF 60(1):5-22 (`20` validation); Boker & Laurenceau 2006, pp. 195-218, same DOI (`20` section 5); Liebovitch, Naudot, Vallacher, Nowak, Bui-Wrzosinska & Coleman 2008, Physica A 387(25):6360-6378 (`20` s4b, `059` s1, `060` s2, `082` s1.5).
- Section 2.4 / 6: Boker & Laurenceau and Ferrer & Nesselroade supply the method for daily couple data and test coupling and inertia at day scale. Consistent with `061` (Boker-Laurenceau coupled oscillator, with `061` noting the original chapter was not read, as here), `20` section 5, and `078` section 8 (explicitly judges 080 section 2 compatible).
- Section 6 time-scale point (turn vs day vs year; a dataset can falsify an operator only at its own scale) agrees with `079` (sampling-interval and aliasing, sections 5.3 and 5.4).
- Section 7 "no public turn-coded two-spouse conflict dataset": consistent with `078` section 7 (no open dyadic set suited to relaxation fits found) and with `20` (no public data seen for Sadler et al. 2009).

### Contradictions and tensions

1. **"Already well supported" corollary vs `20` section 1 (Heyman & Slep 2001; Kim, Capaldi & Crosby 2007).**
   - Here (Summary 3): the coarse corollary that time-averaged negativity predicts dissolution "is already well supported (Gottman et al. 1998; Carrere et al. 2000)". Section 3 table also lists pairfam, Early Years of Marriage and the Gottman raw data as simple tests of it.
   - There (`20` section 1, "Empirical fitting and standing"): Heyman & Slep (2001, JMF 63(2):473-479) show that divorce prediction without cross-validation inflates accuracy (positive predictive value 65% fitting half, 29% hold-out; those figures from a secondary write-up and unchecked), naming Gottman et al. 1998 as the example. Kim, Capaldi & Crosby (2007, JMF 69(1):55-72), 85 at-risk community couples, found the 1998 affective-process variables (rejection of influence, lack of de-escalation, negative start-up) did not predict relationship status [abstract read]. A reply (Coan & Gottman 2007) argues the sample was too specialised. `059` section 7 likewise says the divorce finding is in-sample with no cross-validation.
   - Verdict: **`20` is right; this file overstated.** The wording should be "supported in the Gottman lab's own samples, contested on cross-validation and in one independent at-risk sample". Primary papers were not re-opened here, but both sides rest on abstracts and `20` read the relevant ones. Consequence for this file: the coarse-corollary test is a genuine test, not a settled baseline, and Kim et al. is itself an observed-interaction dataset on couples (Oregon Youth Study) that this file's catalogue omits.
2. **Unnamed in this file: independent-sample evidence exists (Kim et al. 2007), which bears on Summary 2 and section 7 ("Does not (found)").** `20` records it as an independent test of the 1998 affective variables, not of the difference-equation parameters. Section 7's narrow claim (no independent refit of the influence-function threshold) survives, and `20` itself says "I found no independent out-of-sample test of the difference-equation model's own parameters". Verdict: **consistent on the narrow claim; this file should cite Kim et al. as the nearest independent test.**
3. **Hamaker et al. 2009 and Madhyastha et al. 2011 vs "no refit exists" in `059` / `20`.** Already raised from the other side in `059` Cross-checks item 2: this file is the more complete source. Verdict: **this file is right**, and the `059` and `20` wording ("no independent-lab test", "not tested out of sample") should be read as narrower than "no re-estimation". Unresolved only in that neither file has read Madhyastha's results.
4. **Sample size: Madhyastha "couples N = 124 and newlyweds N = 130" (section 1) vs `059`'s 130 newlyweds with 125 estimable.** Not a conflict on the 1999 paper (`059` is correct there: 130 in lab, 125 estimable). The 124 is probably a separate sample in Madhyastha et al. and was taken from an abstract. Verdict: **unresolved** until the Madhyastha text is opened.
5. **Threshold sign.** This file does not state the sign direction; it uses `059` ("more negative husband threshold in divorcing couples"). `20` still lists the sign as contested, but `059` Cross-checks item 1 resolves it from the 1999 paper's own wording. Verdict: **`059` right; no conflict with this file.**
6. **`078` open dyadic sets (OSF wcfvt, 537 parent-adolescent pairs; 5b798) vs section 7 "does not exist: a public turn-coded two-spouse dataset".** No conflict: `078` marks both as access unconfirmed, day-scale, and not romantic-couple conflict coding (wcfvt is parent-adolescent, planned analysis). Worth adding to section 3 as day-scale options for the coupling and inertia test. Verdict: **consistent**.
