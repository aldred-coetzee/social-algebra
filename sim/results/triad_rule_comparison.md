# Which directed triad rule best predicts the sign of a closing or converting tie?

_Generated 2026-11-01 by `uv run python -m models.triad_rule_comparison report` (seed 20261101). Code: `sim/models/triad_rule_comparison.py`; checks: `sim/tests/test_triad_rule_comparison.py`. Ledger ids are the `id` fields of `docs/ledger.jsonl` entries (not always line numbers), named in the module docstring. Results are computed statistics only; the data files are local-use-only, git-ignored and not redistributed (`sim/data/README.md`)._

**What was tested.** `models/00-v0.md` section 4.2 (v0.2.1) carries three statements about triads: (4.2b) strict balance as a structure theorem; (4.2d) a **directed law**, a two-factor product rule on the two ties into the third person, sgn(a_ik)·sgn(a_jk) = +, independent of the first tie i -> j, which is D&K's first-tie partition of the eight ordered-triple types {LLL, LDD, DLL, DDD} enriched and {LLD, LDL, DLD, DDL} depleted [hypothesis; one group of 17 men]; and (4.2e) weak balance as a depletion, not a prohibition. Its section 7 states the test: reproduce the partition against a row-wise sign-shuffle null in a longitudinal explicit-sign panel; *if DLL is depleted like LLD, (4.2d) is refuted and the symmetric rule returns*; and it asks for a side-by-side of directed triad rules. Here five rules compete to predict the sign of a tie that **closes** a triad (or, in wiki-RfA, **re-signs** a tie), on three formation-ordered, explicit-sign data sets, with models fitted on the past and scored on the future: strict balance (the product rule), weak (Davis) balance, the first-tie asymmetric rule (on a forward chain it is (4.2d): the closing tie takes the sign of the second tie), Leskovec et al.'s status rule, and a person-propensity baseline (sender and receiver sign tendencies from earlier ties). The static test of section 7 is run too, on the same data.

## Verdict

**Bottom line.** By the criterion that `models/00-v0.md` section 7 states for the directed law (4.2d) (*if DLL is depleted like LLD, (4.2d) is refuted and the symmetric rule returns*), (4.2d) is refuted on Bitcoin OTC and Alpha, where DLL is depleted and balance returns (on Alpha by the whole-period null; the test period alone gives z -1.8), and reproduced, weakly, on wiki-RfA (DLL z +2.5), where it is a reception pattern: it reverses when reception is held, it is indistinguishable from zero once the person terms are in, and the rule built from it predicts no better than balance at the pre-specified split (it beats strict balance by its interval in 2 of 49 variation configurations: Alpha ridge 100, wiki-RfA every earlier dated vote). Weak balance has the lowest held-out log-loss of the four canonical single triad rules on every site at the pre-specified split, level with strict balance (and on Alpha with the first-tie rule); the person terms predict more than any triad rule except on Bitcoin OTC.

**In short.**

- *Best of the four canonical single rules: weak balance; strict balance is level with it; the first-tie rule is never ahead of weak balance at the pre-specified split (level with strict balance on Alpha and wiki-RfA); status is last.* Held-out log-loss at the pre-specified split (OTC / Alpha / wiki-RfA; lower is better): weak 0.264 / 0.306 / 0.500, strict 0.265 / 0.307 / 0.507, first-tie 0.407 / 0.307 / 0.507, status 0.560 / 0.394 / 0.525, person propensity 0.355 / 0.244 / 0.471, training base rate 0.657 / 0.406 / 0.534, recent rate 0.528 / 0.375 / 0.562. Weak balance has the lowest log-loss of the four canonical single rules in 41 of 49 distinct variation configurations (OTC 14 of 16, Alpha 10 of 16, wiki-RfA 17 of 17; the pre-specified configuration, which several tables repeat, counted once), the first-tie rule in 7 (OTC 1, Alpha 6, wiki-RfA 0), strict balance in 1, status in 0; the first-tie rule beats strict balance by its paired interval in 2 (Alpha ridge 100, wiki-RfA every earlier dated vote) (section 5.5). Weak against strict: OTC -0.002 [-0.005, +0.001], Alpha -0.001 [-0.002, -0.000], wiki-RfA -0.007 [-0.009, -0.006]. Status is not distinguishable from the training base rate on Alpha (-0.012 [-0.054, +0.020]). LHK's learned conjunction pattern, a fifth rule we added, is ahead of weak balance on wiki-RfA (-0.004 [-0.006, -0.002]) and behind it on OTC (+0.035 [+0.021, +0.051]) and level on Alpha (+0.005 [-0.006, +0.017]).

Accuracy and held-out log-loss per rule per site (pre-specified 70/30 split; accuracy is the rule's own majority-vote prediction with silence to +, or the model's at 0.5; log-loss is the calibrated one with its 95% cluster-bootstrap interval; balanced accuracy, AUC and the rolling-origin results are in section 3):

| model | OTC accuracy | OTC log-loss | Alpha accuracy | Alpha log-loss | wiki-RfA accuracy | wiki-RfA log-loss |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| always positive (accuracy = test positive share) | 0.724 | - | 0.877 | - | 0.783 | - |
| training base rate | 0.724 | 0.657 [0.563, 0.757] | 0.877 | 0.406 [0.306, 0.541] | 0.783 | 0.534 [0.503, 0.568] |
| recent rate | 0.774 | 0.528 [0.463, 0.596] | 0.877 | 0.375 [0.309, 0.458] | 0.780 | 0.562 [0.535, 0.592] |
| strict balance | 0.915 | 0.265 [0.223, 0.312] | 0.902 | 0.307 [0.220, 0.431] | 0.746 | 0.507 [0.479, 0.540] |
| weak balance | 0.916 | 0.264 [0.220, 0.311] | 0.903 | 0.306 [0.219, 0.431] | 0.744 | 0.500 [0.471, 0.532] |
| first-tie asymmetric | 0.839 | 0.407 [0.336, 0.489] | 0.904 | 0.307 [0.214, 0.447] | 0.749 | 0.507 [0.478, 0.539] |
| status | 0.705 | 0.560 [0.479, 0.642] | 0.701 | 0.394 [0.291, 0.523] | 0.641 | 0.525 [0.495, 0.559] |
| person propensity | 0.851 | 0.355 [0.294, 0.421] | 0.907 | 0.244 [0.198, 0.290] | 0.790 | 0.471 [0.445, 0.500] |
| person + weak balance | 0.897 | 0.265 [0.218, 0.318] | 0.907 | 0.241 [0.193, 0.291] | 0.795 | 0.463 [0.437, 0.492] |
| person + 16 types | 0.894 | 0.274 [0.226, 0.328] | 0.906 | 0.243 [0.196, 0.295] | 0.796 | 0.463 [0.437, 0.491] |

Read accuracy against the first row. The best accuracy of any of the four rules' own predictions against always-positive: OTC 0.916 against 0.724; Alpha 0.904 against 0.877; wiki-RfA 0.749 against 0.783. On wiki-RfA none of the rules' own predictions reaches the trivial accuracy: strict, weak and first-tie vote negative on 15%-18% of the test votes and are right 38%-39% of the time when they do (the positive class is 78% of the test votes). Log-loss and AUC are the fairer scores there, and only the person-based models clear the trivial accuracy (0.790-0.796).

- *Person terms against triad terms.* On **Alpha** and **wiki-RfA** the person-propensity baseline beats every single triad rule (strict - person: Alpha +0.063 [+0.006, +0.150], wiki-RfA +0.036 [+0.027, +0.046]) and the triad terms add little to it (16 types - person: Alpha -0.001 [-0.011, +0.011] at the split and -0.016 [-0.023, -0.009] rolling; wiki-RfA -0.009 [-0.013, -0.004]). On **OTC** it does not: strict balance alone beats the person terms alone at the pre-specified split (-0.089 [-0.156, -0.034]; AUC 0.921 against 0.918), the triad terms add a great deal to them (-0.080 [-0.108, -0.057]), and the best model is person + strict balance (0.258). Under the rolling origin the OTC gap shrinks to -0.029 [-0.071, +0.013]. So 112 section 6.5 test 2 ('person terms dominate') is supported on two sites; on OTC it fails at the pre-specified split and the two are level under the rolling origin.

- *Does the first-tie asymmetry replicate outside the fraternity? As a static pattern, on one site of three, weakly; as a predictor, not ahead of balance at the pre-specified split, and ahead of strict balance by its interval in 2 of 49 variation configurations; given the person terms, nowhere.*
  - *Static, under the formation-ordered analogue of the Newcomb run's row-wise null (closing signs shuffled within sender, the context ties held; each closing tie counted once):* the eight directions of the fraternity are reproduced on **wiki-RfA** (8/8; DLL above its null (z +2.5), whole period; 8/8 in the test period alone), not on **Alpha** (6/8; DLL below its null (z -5.6)) and not on **OTC** (4/8; DLL below its null (z -19.1), and the eight directions are those of strict balance, 8/8). With reception held (closing signs shuffled within receiver) the two directions that carry the asymmetry, DLL above and DLD below, are reversed on all three: DLL is below its null (OTC z -23.4, Alpha -11.7, wiki-RfA -21.3). The agreement counts under the sender null, and the side of DLL under both nulls, do not depend on the weighting (each tie once or every triad), on the period (whole or test only) or on holding the sender and the year together (section 4.2); the sizes do (Alpha's DLL under the sender null, test period alone: z -1.8).
  - *Cell contrast* P(closing +) after (first -, second +) minus after (first +, second -), which strict balance puts at zero and the asymmetry makes positive: OTC +0.04 [-0.01, +0.09], **Alpha +0.44 [+0.32, +0.53]**, wiki-RfA -0.15 [-0.18, -0.12] (reversed). Alpha has the asymmetry between the two one-negative starts, in the raw cells.
  - *Predictive.* The first-tie rule minus strict balance in held-out log-loss: OTC +0.142 [+0.076, +0.223] (rolling +0.098 [+0.051, +0.151]), Alpha +0.000 [-0.013, +0.018], wiki-RfA -0.001 [-0.003, +0.001]; on the closing ties where the two rules can differ (a forward chain with a negative first tie) OTC +0.228 [+0.130, +0.330], Alpha +0.050 [-0.013, +0.120], wiki-RfA -0.004 [-0.012, +0.002]. Against weak balance on wiki-RfA it is worse (+0.007 [+0.005, +0.009]). Beside the person terms the first-tie rule adds less than balance on OTC (person + first-tie - person + strict +0.037 [+0.021, +0.055]) and the same on wiki-RfA (-0.000 [-0.001, +0.000]); on Alpha it is nominally the best addition (-0.003 [-0.008, +0.003]; rolling +0.003 [-0.001, +0.007]; disagreement subset -0.029 [-0.067, +0.003]), a hint that clears no interval. The 2 variation configurations in which the first-tie rule is ahead of strict balance by its interval (section 5.5): Alpha at ridge 100 (-0.018 [-0.029, -0.009]; first-tie 0.328 against weak balance 0.344), a penalty under which strict balance worsens from 0.307 (ridge 1) to 0.345 and the first-tie rule only from 0.307 to 0.328; wiki-RfA's vote-level horizon, where a voter sees the same election's earlier votes (-0.009 [-0.014, -0.004]); it is still behind weak balance there (0.466 against 0.459), and a rule that copies the earlier votes on the candidate is the herding setting, which is reception again.
  - *Given the person terms* the coefficient contrast FFmp - FFpm that the asymmetry makes positive is -0.19 [-0.84, +0.40] (OTC), -0.47 [-1.31, +0.50] (Alpha), +0.02 [-0.18, +0.22] (wiki-RfA; 400 cluster-bootstrap refits): zero within the interval, the Bitcoin point estimates on the wrong side for an asymmetry. The product structure of balance, (FFpp + FFmm) - (FFpm + FFmp) in the same model, is +4.63 [+3.65, +5.75] (OTC), +2.53 [+1.40, +3.85] (Alpha), +0.30 [+0.04, +0.59] (wiki-RfA).

- *What the fraternity's pattern was.* Re-read post hoc, D&K's eight-type pattern in the Newcomb ranks is, from the second wave on, exactly the partition 'the closing tie has the sign of the second tie' (8 of 8 cells in 14 of 14 waves under the row-wise null), so the first tie takes no part in it; under a column-wise null that holds each man's popularity it shrinks to about chance (agreement 4-6 of 8, |z| <= 3.4). What the Newcomb run called a first-tie asymmetry is a consensus about the third man, in the sense that it disappears when each man's popularity is held. Reception is what the sender null leaves free and the receiver null removes, which is why wiki-RfA reproduces the pattern under the first and loses it under the second.

- *Converting ties (wiki-RfA re-votes).* Persistence alone gives 0.392; adding the context of weak balance 0.371 (-0.021 [-0.030, -0.012]), strict 0.375, first-tie 0.380 (+0.005 [+0.000, +0.009] against strict), status 0.385 (-0.007 [-0.014, +0.001]); the person terms 0.372. Rules help a little, balance most, and the 16 types add nothing to the person terms (+0.002 [-0.009, +0.011]). Conversion is not decided by any rule.

**Status of `models/00-v0.md` section 4.2 as now written (v0.2.1): (4.2b) strict balance as a structure theorem, (4.2d) the directed law, (4.2e) weak balance as a depletion.**

- *(4.2d), the directed law (a two-factor product rule on the ties into the third person): refuted by section 7's own criterion on two of three sites, reproduced, weakly, on the third, and where it reproduces it is reception.* Against the row-wise (sender) null, in its formation-ordered form, DLL is depleted like LLD on OTC (z -19.1) and on Alpha (z -5.6), and the symmetric rule returns: all eight directions on OTC are those of strict balance (8/8), on Alpha 6/8 with the two misses in the (-,-) cells where weak balance is silent. On Alpha the refutation rests on the whole period: the test period alone gives z -1.8, and the raw cells do show the asymmetry (mp - pm +0.44 [+0.32, +0.53]), which holding each sender's own mix removes. On wiki-RfA DLL is enriched (z +2.5) and the partition reproduces. Cells of the four that follow the two-factor partition: wiki-RfA 4, Alpha 3, OTC 2 (OTC fails in both first-tie-negative cells, where it follows the three-factor product). What reproduces involves only the two ties into the third person, which is a statement about that person's reception and not a triadic law; it reverses when reception is held (DLL below its receiver null on all three, z -23.4 / -11.7 / -21.3), the contrast it predicts is indistinguishable from zero once the person terms are in, and the forward-chain rule built from it predicts no better than the three-factor product at the pre-specified split (above). The post hoc Newcomb re-read says the same of the fraternity. The reading of the third person as a contested Object, DLL as R-C's rivalry (section 4.2, 'ours and untested'), was read from the DLL-over pattern; that pattern shrinks to within 3.4 SD of its null once each man's popularity is held (section 4.1), so it is not evidence for rivalry.
- *(4.2e), weak balance as a depletion: the depletion of LLD and LDL is supported on all three sites; the Davis half, an all-negative closing that is not depleted, on Alpha and wiki-RfA but not on OTC; as a predictor weak balance is not worse than strict balance at the pre-specified split on any site.* Two of the three one-negative closings, LLD and LDL, are below the sender null on all three sites but present (OTC z -37.3 / -31.0, Alpha -24.0 / -25.1, wiki-RfA -9.6 / -9.1); the third, DLL, is the (4.2d) cell above. The all-negative closing DDD, the cell that separates Davis from Heider, is above the sender null on Alpha (z +2.5) and wiki-RfA (+4.1) and below it on OTC (-2.4; below its null in every variant of section 4.2), strict balance's direction. On Bitcoin the (-,-) start closes positive (FFmm 69% on OTC, 59% on Alpha, each tie once, against 13% and 17% for the mixed starts on OTC), and weak balance, silent there, loses nothing in log-loss (the start is rare: 147 and 77 closing ties); on wiki-RfA weak balance is ahead of strict (-0.007 [-0.009, -0.006]), and the (-,-) vote carries nothing once the person terms are in. The product structure of balance survives the person terms on Bitcoin and is faint on wiki-RfA (section 4.6). The learned FFmm coefficient of L4833 (-0.73 / -0.59 / -0.77, balance says +1) **does not transfer** to 2010-16 Bitcoin, where the person-adjusted coefficient is +1.36 [+0.76, +2.07] (OTC) and +1.15 [+0.34, +2.16] (Alpha), on 147 and 77 closing ties (modest support, intervals excluding zero), and is zero within its interval on wiki-RfA (112 section 6.5 test 1).
- *(4.2b), strict balance as a structure theorem:* a theorem, untouched by data. As an empirical rule it is level in size with weak balance on Bitcoin (weak - strict: OTC -0.002 [-0.005, +0.001], Alpha -0.001 [-0.002, -0.000]) and behind it on wiki-RfA. *Behind balance on these data (each carries signal on some site, so 'refuted' would overstate it):* status as a triad rule (last of the four canonical rules at the pre-specified split and in every variation configuration; its own hard predictions are below the always-positive accuracy on all three sites; as features, against the base rate: OTC -0.097 [-0.141, -0.056], Alpha -0.012 [-0.054, +0.020], wiki-RfA -0.009 [-0.012, -0.005]); and the kinetic law (4.2a), dA/dt = A^2, read as a sign predictor for a new tie (the net product vote of the forward chains alone), which is worse than direction-free balance on OTC (+0.046 [+0.025, +0.067]) and wiki-RfA (+0.026 [+0.020, +0.032]; there it is no better than the base rate, -0.000 [-0.005, +0.004]) and level on Alpha (+0.005 [-0.009, +0.021]); using direction does not help.
- *Supported otherwise:* the person-propensity terms as the larger part of the predictable sign on Alpha and wiki-RfA, with the triad terms adding a small, real amount (wiki-RfA) or a large one (OTC); and, post hoc, the reading of the Newcomb first-tie pattern as reception.
- *Not decided:* whether a rivalry mechanism of D&K's kind exists beyond reception in a small closed group, where reception can be held and the first tie is a rival's (the sender and receiver nulls each hold one person effect, the person-adjusted contrast holds both approximately and finds nothing distinguishable from zero, but none of the three media is a rivalry setting); whether the wiki-RfA static agreement (DLL above its null (z +2.5)) is anything but reception; whether the directed distinctions matter at all (the 16-type model against weak balance: OTC +0.028 [+0.014, +0.044], Alpha +0.006 [-0.013, +0.028], wiki-RfA -0.009 [-0.015, -0.004]); and the dynamical half of section 7 (conversion of a standing tie: no Bitcoin tie is re-signed, and the wiki-RfA re-votes are re-ratings of a re-run candidate; the dedicated conversion test is `results/wikirfa_conversion.md`).
- *For section 4.2 (a proposal, Aldred's call):* demote (4.2d) from a directed law to a **reception term**: in the Newcomb data and on wiki-RfA the sign of a tie into k agrees with the other ties into k beyond the sender's own mix; write the triad law as a **table of conditional sign probabilities over the 16 directed types, per site and period, estimated beside the person terms**, with weak balance as the structure it is closest to on Bitcoin and no first-tie term; withdraw the rivalry reading of DLL until a setting that can hold reception supplies it. A decisive test of the asymmetry as rivalry needs a signed panel of a small group with an independent measure of each member's popularity, which this ledger does not have.

## 1. Data, terms, target sets

- **Bitcoin OTC and Bitcoin Alpha** (SNAP `soc-sign-bitcoinotc.csv.gz`, 397,258 bytes; `soc-sign-bitcoinalpha.csv.gz`, 149,480 bytes). Pseudonymous traders rate one another from -10 to +10 after a trade; Kumar, Spezzano, Subrahmanian & Faloutsos (2016), Edge weight prediction in weighted signed networks, ICDM, doi:10.1109/ICDM.2016.0033, and Kumar, Hooi, Makhija, Kumar, Faloutsos & Subrahmanian (2018), REV2: fraudulent user prediction in rating platforms, WSDM, doi:10.1145/3159652.3159729 (the two papers the SNAP pages ask users to cite). **Terms:** none stated by SNAP [L4567]; fetched for local use into git-ignored `sim/data/bitcoin/`, never committed, sha256 recorded in `sim/data/README.md`. OTC: 35,592 ratings, 5,881 nodes, 90.0% positive [L4568], unique sub-second timestamps; Alpha: 24,186 ratings, 3,783 nodes, 93.6% positive [L4570], **timestamps are whole days (one stamp per day, at 04:00 or 05:00 UTC: 1,647 distinct values; 24,062 ratings share a timestamp with another)** (this module's counts, checked by its tests). No ordered pair is rated twice [L4571].
- **wiki-RfA** (SNAP `wiki-RfA.txt.gz`, 14,936,383 bytes). West, Paskov, Leskovec & Potts (2014), TACL 2, doi:10.1162/tacl_a_00184. Votes on Wikipedia adminship requests: voter, candidate, support/oppose/neutral, election result, date. **Terms:** none stated by SNAP (page read 2026-11-01, `sim/data/README.md`); the vote comments are Wikipedia text (CC BY-SA and GFDL [L4561]) and **are skipped line by line and never held in memory**; user names are replaced by integers on load and never written out. 198,275 votes: 144,451 support, 41,176 oppose, 12,648 neutral [L4562].
- **Newcomb fraternity ranks**, used only in the post hoc re-read of section 4.1 (UCINET `newfrat.dat`, 13,702 bytes, the Internet Archive's copy of Batagelj & Mrvar's Pajek datasets). **Terms:** none stated, so treated as not licensed for redistribution: local use only, git-ignored, sha256 in `sim/data/README.md`; only computed statistics appear here. Credit: Newcomb (1961), *The Acquaintance Process*; Nordlie (1958); UCINET (Borgatti, Everett & Freeman 1992), distributed via Batagelj & Mrvar (2006), Pajek datasets.
- **What is a tie, a closing tie, a converting tie.** A tie is a signed directed rating u -> v. A **closing** tie is the first tie between u and v in either direction (117's closing convention, [L4572-L4573]) that has at least one *common neighbour* w (a third party tied to both, in any direction) visible before it. A **converting** tie (wiki-RfA only) is a re-vote: u had already voted on v at an earlier candidacy; the target is the new sign. Bitcoin has no converting ties [L4571].
- **What 'before' means (no leakage).** A tie is visible as context only if its visibility time is *strictly* earlier than the target's cut. Bitcoin: the rating time (so, in Alpha, same-day ratings are never context for each other: the order inside a day is unknown). wiki-RfA, primary: the cut is the *start* of the target's election and a vote becomes visible at the *end* of its election, so a vote sees only the network its voter walked into, never the concurrent crowd. An election is a block of consecutive records of one candidate, result and year, split wherever the dated votes are more than 14 days apart; stray clusters of fewer than 10 votes and votes without a readable date in an ambiguous block are dropped (1,123 of the 198,275 votes), elections that the file carries twice with identical windows are merged (27), the election result (RES) is never used as a feature.

| site | target ties | with >= 1 common neighbour | closing ties used | positive share (used) | train | test | median embeddedness | embeddedness >= 25 |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Bitcoin OTC | 35,592 | 14,934 | 8,972 | 0.805 | 5,172 | 3,800 | 2 | 108 |
| Bitcoin Alpha | 24,186 | 9,497 | 7,875 | 0.918 | 4,659 | 3,216 | 2 | 70 |
| wiki-RfA | 182,419 | 89,410 | 78,254 | 0.821 | 52,050 | 26,204 | 4 | 5,611 |

## 2. Method

**Rules.** Each rule labels every context triad (a common neighbour w, with the two ties u~w and w~v) as predicting a positive closing tie, a negative one, or nothing. Balance (strict and weak) is applied the way Leskovec, Huttenlocher & Kleinberg (2010) define it [L4800, L4812, L4815]: on the direction-free pair sign, one vote per common neighbour. The others use the 16 directed types [F|B][F|B][p|m][p|m] [L4814], one vote per directed instance. 'First-tie asymmetric' is the Newcomb run's rule written as a predictor: balance, except that in a forward chain u -> w -> v (D&K's ordered triple (i->j)(j->k)(i->k), [L4481]) **a negative first tie u -> w reverses the balance prediction** [L4508, L4511]. Since reversing the product when s1 = - gives s2, this rule predicts *the sign of the second tie w -> v* in every forward chain; that identity is why a 'copy incoming' diagnostic and a time-first variant are run beside it.

| type (u->w, w->v, signs) | strict balance | status | first-tie | conjunction | copy incoming |
| :--- | ---: | ---: | ---: | ---: | ---: |
| FFpp | + | + | + | + | + |
| FFpm | - | . | - | - | - |
| FFmp | - | . | + | - | + |
| FFmm | + | - | - | - | - |
| FBpp | + | . | + | + | . |
| FBpm | - | + | - | - | . |
| FBmp | - | - | - | - | . |
| FBmm | + | . | + | - | . |
| BFpp | + | . | + | + | + |
| BFpm | - | - | - | - | - |
| BFmp | - | + | - | - | + |
| BFmm | + | . | + | - | - |
| BBpp | + | - | + | + | . |
| BBpm | - | . | - | - | . |
| BBmp | - | . | - | - | . |
| BBmm | + | + | + | - | . |

Weak balance is the strict-balance column with the (-,-) pair-level vote silent. The conjunction column is LHK's learned forward-chain pattern [L4811] extended to all forms by 'positive only if both ties are positive' (our extension). Further forms are run in section 5.4: balance per directed instance, the A^2 sign (the net product vote of forward chains only, v0.1 (4.2a)), the first-tie rule on forward chains only, on all forms, and by formation order (copy the later-formed tie).

**Models.** Every model is a logistic regression (ridge 1) fitted on the training period only. A rule enters as two features, log(1 + votes for +) and log(1 + votes for -), so a rule is judged by how well its *labelling* of the contexts sorts the closing signs; the same rule's **own** hard prediction (majority of its votes, ties and silence to +, the convention of 106's recount of LHK [L4817]) is reported beside it. *Person propensity* is LHK's four signed degrees [L4813]: u's earlier out-votes (+, -) and v's earlier in-votes (+, -), all counted from visible ties only (log(1 + count)). *Saturated 16 types* is a logistic model on the 16 triad-type counts alone, the triad half of LHK's 23-feature model [L4799]. The 'person + X' models add X to the person terms. *Base rate* is the training positive share; *recent rate* has no fitted parameter and is the smoothed positive share of the last 500 visible ties (an adaptive base rate, added because the Bitcoin test periods have a different share of negatives from their training periods).

**Protocol (fixed in the design before the first run of the primary split; the replication criterion was written down after an exploratory look at the sixteen-cell tables).** Chronological 70/30 split of all target ties by cut time (ties never straddle the cut); parameters from the training ties; each test tie's features from the ties visible before its own cut (the context grows through the test period, as it would in use; a 'frozen snapshot' variation removes that); closing ties with at least one common neighbour; accuracy, balanced accuracy, AUC and log-loss on the natural class mix. Intervals: cluster bootstrap (B = 2000 in section 3, 400 in section 5; in section 4.6, 1000 draws for the cell rates and 400 refits for the coefficients), clusters = raters or ratees for Bitcoin and voters or elections for wiki-RfA, the scheme with the larger standard error (section 4.6 uses ratees or elections). **Nulls.** (N0) a constant at the training positive share, and the adaptive recent rate; (N1) the person-propensity model: a triad rule must beat it to be more than a person effect; (N2) for the question 'do the triad terms add to the person terms', the rows of the added features are permuted among ties of equal embeddedness in the training and in the test set and the model is refitted (200 permutations; anti-conservative where the refit overfits, section 4.7); (N3) for the static eight-type pattern, the closing signs are shuffled within sender (the formation-ordered analogue of the Newcomb run's row-wise null [L4485], which redrew every tie of a row: here only the closing sign moves and the context ties stay as they were), within sender and calendar year, and, as a control that the Newcomb run did not have, within receiver; the pool is the closing ties that have a forward-chain context.

**Added after the first look at results (post hoc, reported anyway).** (1) The Bitcoin test periods have a different share of negative ratings from their training periods (OTC 27.6% against 13.5%), so the *recent rate* baseline and the rolling-origin evaluation (every block predicted by models fitted on everything earlier) were added; the single 70/30 split stays the headline, as pre-specified, and where the two designs rank models differently the text says so. (2) The receiver-shuffle null, the sender-by-year null and the person-adjusted coefficients, after seeing that the static comparison depends on which person effect is held. (3) The Newcomb reception re-read (section 4.1). (4) The merging of the elections the file carries twice, after the data README flagged them. (5) The shuffle pool of the static comparison was first every closing tie; it was corrected to the closing ties that have a forward-chain context (the first version made every positive-closing cell look depleted on wiki-RfA and gave a wrong '4/8' there, not reported), and the each-tie-once weighting was added beside the every-triad weighting. (6) The 'where the rules disagree' subset and the A^2 rule (v0.1 (4.2a)), as sharper tests of the same contrast.

## 3. Primary results

### 3.1 Bitcoin OTC: closing ties

**Bitcoin OTC, 70/30 chronological split** (train 5,172 events, test 3,800; positive share train 0.865, test 0.724)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.657 [0.563, 0.757] | - | 0.724 | 0.500 | - | - | - |
| recent rate | 0.528 [0.463, 0.596] | - | 0.774 | 0.618 | - | - | - |
| strict balance | 0.265 [0.223, 0.312] | 0.921 | 0.916 | 0.875 | 1.00 | 0.915 [0.896, 0.933] | 0.858 [0.819, 0.890] |
| weak balance | 0.264 [0.220, 0.311] | 0.922 | 0.914 | 0.875 | 0.99 | 0.916 [0.897, 0.933] | 0.861 [0.823, 0.892] |
| first-tie asymmetric | 0.407 [0.336, 0.489] | 0.855 | 0.857 | 0.792 | 1.00 | 0.839 [0.801, 0.872] | 0.718 [0.680, 0.753] |
| status | 0.560 [0.479, 0.642] | 0.796 | 0.751 | 0.774 | 0.92 | 0.705 [0.679, 0.728] | 0.663 [0.630, 0.691] |
| person propensity | 0.355 [0.294, 0.421] | 0.918 | 0.851 | 0.822 | - | - | - |
| conjunction | 0.299 [0.251, 0.349] | 0.913 | 0.905 | 0.858 | 1.00 | 0.910 [0.891, 0.927] | 0.860 [0.823, 0.891] |
| saturated 16 types | 0.292 [0.244, 0.344] | 0.920 | 0.903 | 0.871 | - | - | - |
| person + strict | 0.258 [0.212, 0.310] | 0.952 | 0.898 | 0.859 | - | - | - |
| person + weak | 0.265 [0.218, 0.318] | 0.950 | 0.897 | 0.860 | - | - | - |
| person + first-tie | 0.295 [0.246, 0.349] | 0.941 | 0.887 | 0.850 | - | - | - |
| person + status | 0.328 [0.271, 0.391] | 0.927 | 0.866 | 0.835 | - | - | - |
| person + 16 types | 0.274 [0.226, 0.328] | 0.947 | 0.894 | 0.850 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| strict balance - base rate | -0.391 [-0.490, -0.299] | <0.001 |
| weak balance - base rate | -0.393 [-0.494, -0.300] | <0.001 |
| first-tie asymmetric - base rate | -0.250 [-0.313, -0.190] | <0.001 |
| status - base rate | -0.097 [-0.141, -0.056] | <0.001 |
| person propensity - base rate | -0.302 [-0.404, -0.210] | <0.001 |
| person propensity - recent rate | -0.173 [-0.235, -0.105] | <0.001 |
| strict balance - person propensity | -0.089 [-0.156, -0.034] | <0.001 |
| weak balance - person propensity | -0.091 [-0.158, -0.036] | <0.001 |
| first-tie asymmetric - person propensity | +0.053 [-0.034, +0.139] | 0.227 |
| status - person propensity | +0.205 [+0.137, +0.279] | <0.001 |
| first-tie asymmetric - strict balance | +0.142 [+0.076, +0.223] | <0.001 |
| first-tie asymmetric - weak balance | +0.144 [+0.078, +0.225] | <0.001 |
| first-tie asymmetric - status | -0.153 [-0.214, -0.093] | <0.001 |
| weak balance - strict balance | -0.002 [-0.005, +0.001] | 0.250 |
| status - strict balance | +0.294 [+0.226, +0.365] | <0.001 |
| person + 16 types - person propensity | -0.080 [-0.108, -0.057] | <0.001 |
| person + strict - person propensity | -0.097 [-0.126, -0.071] | <0.001 |
| person + weak - person propensity | -0.089 [-0.116, -0.065] | <0.001 |
| person + first-tie - person propensity | -0.060 [-0.081, -0.040] | <0.001 |
| person + status - person propensity | -0.026 [-0.035, -0.017] | <0.001 |
| person + first-tie - person + strict | +0.037 [+0.021, +0.055] | <0.001 |
| person + first-tie - person + weak | +0.030 [+0.016, +0.044] | <0.001 |
| person + 16 types - person + strict | +0.016 [+0.005, +0.028] | 0.002 |
| person + strict - strict balance | -0.008 [-0.045, +0.037] | 0.679 |
| person + weak - weak balance | +0.002 [-0.036, +0.048] | 0.975 |
| saturated 16 types - weak balance | +0.028 [+0.014, +0.044] | <0.001 |
| conjunction - weak balance | +0.035 [+0.021, +0.051] | <0.001 |

**Bitcoin OTC, rolling origin (5 expanding blocks over the last half)** (train 3,485 events, test 5,487; positive share train 0.842, test 0.759)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.588 [0.518, 0.659] | - | 0.759 | 0.471 | - | - | - |
| recent rate | 0.509 [0.452, 0.568] | - | 0.794 | 0.667 | - | - | - |
| strict balance | 0.264 [0.223, 0.303] | - | 0.914 | 0.868 | 0.99 | 0.914 [0.898, 0.930] | 0.838 [0.806, 0.869] |
| weak balance | 0.259 [0.220, 0.299] | - | 0.915 | 0.875 | 0.99 | 0.916 [0.900, 0.932] | 0.844 [0.812, 0.874] |
| first-tie asymmetric | 0.362 [0.307, 0.421] | - | 0.871 | 0.804 | 1.00 | 0.856 [0.828, 0.883] | 0.715 [0.684, 0.745] |
| status | 0.489 [0.429, 0.554] | - | 0.793 | 0.763 | 0.92 | 0.713 [0.693, 0.733] | 0.667 [0.638, 0.694] |
| person propensity | 0.293 [0.253, 0.335] | - | 0.879 | 0.849 | - | - | - |
| conjunction | 0.278 [0.237, 0.320] | - | 0.910 | 0.864 | 1.00 | 0.913 [0.896, 0.928] | 0.851 [0.819, 0.879] |
| saturated 16 types | 0.275 [0.234, 0.316] | - | 0.909 | 0.873 | - | - | - |
| person + strict | 0.218 [0.186, 0.252] | - | 0.919 | 0.884 | - | - | - |
| person + weak | 0.224 [0.191, 0.258] | - | 0.917 | 0.881 | - | - | - |
| person + first-tie | 0.245 [0.211, 0.278] | - | 0.907 | 0.874 | - | - | - |
| person + status | 0.273 [0.236, 0.312] | - | 0.893 | 0.860 | - | - | - |
| person + 16 types | 0.222 [0.191, 0.255] | - | 0.917 | 0.880 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| strict balance - person propensity | -0.029 [-0.071, +0.013] | 0.181 |
| first-tie asymmetric - strict balance | +0.098 [+0.051, +0.151] | <0.001 |
| person + 16 types - person propensity | -0.071 [-0.092, -0.050] | <0.001 |
| person + first-tie - person + strict | +0.027 [+0.015, +0.040] | <0.001 |

*Where the rules disagree.* The first-tie rule and strict balance say different things only when a closing tie has a forward chain whose first tie is negative (1,323 of 8,972 closing ties). On those ties alone (models refitted on the training ties of that kind):

**Bitcoin OTC, closing ties with a negative-first-tie forward chain** (train 486 events, test 837; positive share train 0.403, test 0.373)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.662 [0.630, 0.701] | - | 0.627 | 0.500 | - | - | - |
| strict balance | 0.236 [0.181, 0.295] | 0.965 | 0.914 | 0.916 | 1.00 | 0.908 [0.871, 0.943] | 0.916 [0.878, 0.948] |
| weak balance | 0.239 [0.183, 0.299] | 0.964 | 0.910 | 0.922 | 0.98 | 0.912 [0.876, 0.943] | 0.918 [0.881, 0.948] |
| first-tie asymmetric | 0.464 [0.376, 0.561] | 0.879 | 0.787 | 0.801 | 1.00 | 0.560 [0.470, 0.656] | 0.645 [0.600, 0.694] |
| status | 0.453 [0.374, 0.537] | 0.873 | 0.818 | 0.824 | 0.80 | 0.568 [0.500, 0.636] | 0.562 [0.501, 0.622] |
| person propensity | 0.389 [0.300, 0.482] | 0.915 | 0.829 | 0.805 | - | - | - |
| person + strict | 0.238 [0.177, 0.302] | 0.972 | 0.890 | 0.878 | - | - | - |
| person + first-tie | 0.333 [0.256, 0.413] | 0.935 | 0.860 | 0.845 | - | - | - |
| person + 16 types | 0.270 [0.205, 0.340] | 0.960 | 0.879 | 0.875 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| first-tie asymmetric - strict balance | +0.228 [+0.130, +0.330] | <0.001 |
| first-tie asymmetric - weak balance | +0.225 [+0.128, +0.327] | <0.001 |
| first-tie asymmetric - person propensity | +0.075 [-0.045, +0.194] | 0.238 |
| strict balance - person propensity | -0.153 [-0.231, -0.080] | <0.001 |
| person + first-tie - person + strict | +0.095 [+0.061, +0.130] | <0.001 |

### 3.2 Bitcoin Alpha: closing ties

**Bitcoin Alpha, 70/30 chronological split** (train 4,659 events, test 3,216; positive share train 0.946, test 0.877)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.406 [0.306, 0.541] | - | 0.877 | 0.500 | - | - | - |
| recent rate | 0.375 [0.309, 0.458] | - | 0.877 | 0.530 | - | - | - |
| strict balance | 0.307 [0.220, 0.431] | 0.777 | 0.896 | 0.722 | 1.00 | 0.902 [0.861, 0.933] | 0.643 [0.597, 0.689] |
| weak balance | 0.306 [0.219, 0.431] | 0.777 | 0.897 | 0.725 | 1.00 | 0.903 [0.862, 0.934] | 0.647 [0.601, 0.691] |
| first-tie asymmetric | 0.307 [0.214, 0.447] | 0.781 | 0.901 | 0.717 | 1.00 | 0.904 [0.860, 0.936] | 0.630 [0.583, 0.679] |
| status | 0.394 [0.291, 0.523] | 0.664 | 0.881 | 0.644 | 0.97 | 0.701 [0.676, 0.724] | 0.642 [0.600, 0.684] |
| person propensity | 0.244 [0.198, 0.290] | 0.895 | 0.907 | 0.807 | - | - | - |
| conjunction | 0.311 [0.219, 0.444] | 0.778 | 0.898 | 0.714 | 1.00 | 0.901 [0.860, 0.932] | 0.657 [0.614, 0.714] |
| saturated 16 types | 0.312 [0.219, 0.443] | 0.778 | 0.902 | 0.716 | - | - | - |
| person + strict | 0.238 [0.191, 0.288] | 0.905 | 0.907 | 0.822 | - | - | - |
| person + weak | 0.241 [0.193, 0.291] | 0.904 | 0.907 | 0.821 | - | - | - |
| person + first-tie | 0.236 [0.189, 0.284] | 0.905 | 0.906 | 0.824 | - | - | - |
| person + status | 0.241 [0.199, 0.291] | 0.889 | 0.910 | 0.813 | - | - | - |
| person + 16 types | 0.243 [0.196, 0.295] | 0.895 | 0.906 | 0.812 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| strict balance - base rate | -0.099 [-0.159, -0.055] | <0.001 |
| weak balance - base rate | -0.100 [-0.161, -0.056] | <0.001 |
| first-tie asymmetric - base rate | -0.099 [-0.159, -0.055] | <0.001 |
| status - base rate | -0.012 [-0.054, +0.020] | 0.507 |
| person propensity - base rate | -0.162 [-0.258, -0.095] | <0.001 |
| person propensity - recent rate | -0.131 [-0.191, -0.083] | <0.001 |
| strict balance - person propensity | +0.063 [+0.006, +0.150] | 0.015 |
| weak balance - person propensity | +0.062 [+0.005, +0.150] | 0.019 |
| first-tie asymmetric - person propensity | +0.063 [+0.001, +0.166] | 0.038 |
| status - person propensity | +0.150 [+0.084, +0.240] | <0.001 |
| first-tie asymmetric - strict balance | +0.000 [-0.013, +0.018] | 0.973 |
| first-tie asymmetric - weak balance | +0.001 [-0.011, +0.018] | 0.931 |
| first-tie asymmetric - status | -0.086 [-0.132, -0.046] | <0.001 |
| weak balance - strict balance | -0.001 [-0.002, -0.000] | 0.048 |
| status - strict balance | +0.087 [+0.050, +0.131] | <0.001 |
| person + 16 types - person propensity | -0.001 [-0.011, +0.011] | 0.973 |
| person + strict - person propensity | -0.006 [-0.016, +0.005] | 0.314 |
| person + weak - person propensity | -0.003 [-0.014, +0.008] | 0.592 |
| person + first-tie - person propensity | -0.008 [-0.015, -0.001] | 0.020 |
| person + status - person propensity | -0.003 [-0.010, +0.006] | 0.535 |
| person + first-tie - person + strict | -0.003 [-0.008, +0.003] | 0.322 |
| person + first-tie - person + weak | -0.005 [-0.011, +0.000] | 0.075 |
| person + 16 types - person + strict | +0.005 [-0.008, +0.020] | 0.417 |
| person + strict - strict balance | -0.069 [-0.149, -0.017] | 0.001 |
| person + weak - weak balance | -0.065 [-0.146, -0.013] | 0.002 |
| saturated 16 types - weak balance | +0.006 [-0.013, +0.028] | 0.588 |
| conjunction - weak balance | +0.005 [-0.006, +0.017] | 0.415 |

**Bitcoin Alpha, rolling origin (5 expanding blocks over the last half)** (train 2,822 events, test 5,053; positive share train 0.949, test 0.887)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.382 [0.309, 0.474] | - | 0.887 | 0.455 | - | - | - |
| recent rate | 0.353 [0.299, 0.420] | - | 0.887 | 0.530 | - | - | - |
| strict balance | 0.277 [0.217, 0.354] | - | 0.904 | 0.746 | 1.00 | 0.913 [0.887, 0.935] | 0.661 [0.616, 0.708] |
| weak balance | 0.277 [0.216, 0.354] | - | 0.905 | 0.748 | 0.99 | 0.914 [0.888, 0.936] | 0.667 [0.621, 0.714] |
| first-tie asymmetric | 0.285 [0.218, 0.370] | - | 0.905 | 0.731 | 1.00 | 0.910 [0.882, 0.934] | 0.635 [0.587, 0.687] |
| status | 0.356 [0.283, 0.430] | - | 0.889 | 0.654 | 0.96 | 0.710 [0.689, 0.729] | 0.660 [0.620, 0.696] |
| person propensity | 0.214 [0.177, 0.251] | - | 0.922 | 0.804 | - | - | - |
| conjunction | 0.285 [0.221, 0.367] | - | 0.903 | 0.732 | 1.00 | 0.912 [0.885, 0.933] | 0.673 [0.626, 0.723] |
| saturated 16 types | 0.276 [0.211, 0.355] | - | 0.913 | 0.748 | - | - | - |
| person + strict | 0.199 [0.163, 0.233] | - | 0.927 | 0.826 | - | - | - |
| person + weak | 0.200 [0.164, 0.235] | - | 0.928 | 0.826 | - | - | - |
| person + first-tie | 0.202 [0.165, 0.237] | - | 0.926 | 0.820 | - | - | - |
| person + status | 0.208 [0.172, 0.244] | - | 0.925 | 0.808 | - | - | - |
| person + 16 types | 0.198 [0.165, 0.232] | - | 0.930 | 0.826 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| strict balance - person propensity | +0.063 [+0.024, +0.120] | <0.001 |
| first-tie asymmetric - strict balance | +0.008 [-0.004, +0.020] | 0.196 |
| person + 16 types - person propensity | -0.016 [-0.023, -0.009] | <0.001 |
| person + first-tie - person + strict | +0.003 [-0.001, +0.007] | 0.103 |

*Where the rules disagree.* The first-tie rule and strict balance say different things only when a closing tie has a forward chain whose first tie is negative (626 of 7,875 closing ties). On those ties alone (models refitted on the training ties of that kind):

**Bitcoin Alpha, closing ties with a negative-first-tie forward chain** (train 219 events, test 407; positive share train 0.749, test 0.742)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.571 [0.460, 0.692] | - | 0.742 | 0.500 | - | - | - |
| strict balance | 0.426 [0.305, 0.547] | 0.821 | 0.801 | 0.751 | 1.00 | 0.786 [0.702, 0.871] | 0.651 [0.592, 0.733] |
| weak balance | 0.424 [0.302, 0.549] | 0.824 | 0.803 | 0.759 | 1.00 | 0.791 [0.708, 0.876] | 0.660 [0.599, 0.748] |
| first-tie asymmetric | 0.476 [0.317, 0.657] | 0.793 | 0.784 | 0.702 | 1.00 | 0.794 [0.687, 0.889] | 0.606 [0.544, 0.679] |
| status | 0.579 [0.389, 0.771] | 0.718 | 0.740 | 0.574 | 0.97 | 0.582 [0.518, 0.648] | 0.610 [0.540, 0.678] |
| person propensity | 0.370 [0.300, 0.438] | 0.886 | 0.840 | 0.775 | - | - | - |
| person + strict | 0.363 [0.295, 0.440] | 0.897 | 0.838 | 0.798 | - | - | - |
| person + first-tie | 0.334 [0.265, 0.399] | 0.906 | 0.860 | 0.803 | - | - | - |
| person + 16 types | 0.360 [0.286, 0.440] | 0.899 | 0.853 | 0.807 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| first-tie asymmetric - strict balance | +0.050 [-0.013, +0.120] | 0.134 |
| first-tie asymmetric - weak balance | +0.052 [-0.007, +0.119] | 0.085 |
| first-tie asymmetric - person propensity | +0.106 [-0.028, +0.275] | 0.186 |
| strict balance - person propensity | +0.056 [-0.043, +0.173] | 0.355 |
| person + first-tie - person + strict | -0.029 [-0.067, +0.003] | 0.071 |

### 3.3 wiki-RfA: closing ties

**wiki-RfA, 70/30 chronological split** (train 52,050 events, test 26,204; positive share train 0.840, test 0.783)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.534 [0.503, 0.568] | - | 0.783 | 0.500 | - | - | - |
| recent rate | 0.562 [0.535, 0.592] | - | 0.780 | 0.487 | - | - | - |
| strict balance | 0.507 [0.479, 0.540] | 0.640 | 0.784 | 0.602 | 1.00 | 0.746 [0.728, 0.762] | 0.569 [0.559, 0.579] |
| weak balance | 0.500 [0.471, 0.532] | 0.659 | 0.785 | 0.617 | 0.98 | 0.744 [0.726, 0.760] | 0.592 [0.580, 0.604] |
| first-tie asymmetric | 0.507 [0.478, 0.539] | 0.640 | 0.784 | 0.603 | 1.00 | 0.749 [0.731, 0.765] | 0.572 [0.562, 0.583] |
| status | 0.525 [0.495, 0.559] | 0.587 | 0.783 | 0.581 | 0.65 | 0.641 [0.627, 0.656] | 0.582 [0.568, 0.596] |
| person propensity | 0.471 [0.445, 0.500] | 0.715 | 0.790 | 0.644 | - | - | - |
| conjunction | 0.496 [0.467, 0.528] | 0.668 | 0.786 | 0.621 | 1.00 | 0.728 [0.710, 0.744] | 0.612 [0.598, 0.627] |
| saturated 16 types | 0.491 [0.462, 0.522] | 0.685 | 0.789 | 0.635 | - | - | - |
| person + strict | 0.465 [0.439, 0.494] | 0.727 | 0.794 | 0.656 | - | - | - |
| person + weak | 0.463 [0.437, 0.492] | 0.729 | 0.795 | 0.658 | - | - | - |
| person + first-tie | 0.465 [0.438, 0.494] | 0.727 | 0.795 | 0.656 | - | - | - |
| person + status | 0.471 [0.445, 0.500] | 0.716 | 0.792 | 0.646 | - | - | - |
| person + 16 types | 0.463 [0.437, 0.491] | 0.731 | 0.796 | 0.660 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| strict balance - base rate | -0.027 [-0.033, -0.020] | <0.001 |
| weak balance - base rate | -0.034 [-0.042, -0.027] | <0.001 |
| first-tie asymmetric - base rate | -0.027 [-0.033, -0.021] | <0.001 |
| status - base rate | -0.009 [-0.012, -0.005] | <0.001 |
| person propensity - base rate | -0.063 [-0.075, -0.051] | <0.001 |
| person propensity - recent rate | -0.091 [-0.110, -0.073] | <0.001 |
| strict balance - person propensity | +0.036 [+0.027, +0.046] | <0.001 |
| weak balance - person propensity | +0.029 [+0.020, +0.039] | <0.001 |
| first-tie asymmetric - person propensity | +0.035 [+0.027, +0.045] | <0.001 |
| status - person propensity | +0.054 [+0.044, +0.064] | <0.001 |
| first-tie asymmetric - strict balance | -0.001 [-0.003, +0.001] | 0.531 |
| first-tie asymmetric - weak balance | +0.007 [+0.005, +0.009] | <0.001 |
| first-tie asymmetric - status | -0.018 [-0.025, -0.012] | <0.001 |
| weak balance - strict balance | -0.007 [-0.009, -0.006] | <0.001 |
| status - strict balance | +0.018 [+0.011, +0.024] | <0.001 |
| person + 16 types - person propensity | -0.009 [-0.013, -0.004] | 0.001 |
| person + strict - person propensity | -0.006 [-0.010, -0.002] | <0.001 |
| person + weak - person propensity | -0.008 [-0.012, -0.004] | <0.001 |
| person + first-tie - person propensity | -0.007 [-0.011, -0.003] | <0.001 |
| person + status - person propensity | -0.000 [-0.002, +0.001] | 0.531 |
| person + first-tie - person + strict | -0.000 [-0.001, +0.000] | 0.260 |
| person + first-tie - person + weak | +0.001 [+0.000, +0.002] | 0.034 |
| person + 16 types - person + strict | -0.002 [-0.004, -0.000] | 0.024 |
| person + strict - strict balance | -0.042 [-0.051, -0.034] | <0.001 |
| person + weak - weak balance | -0.037 [-0.044, -0.029] | <0.001 |
| saturated 16 types - weak balance | -0.009 [-0.015, -0.004] | 0.001 |
| conjunction - weak balance | -0.004 [-0.006, -0.002] | <0.001 |

**wiki-RfA, rolling origin (5 expanding blocks over the last half)** (train 36,140 events, test 42,114; positive share train 0.841, test 0.792)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.519 [0.494, 0.543] | - | 0.792 | 0.518 | - | - | - |
| recent rate | 0.543 [0.521, 0.564] | - | 0.785 | 0.491 | - | - | - |
| strict balance | 0.492 [0.468, 0.514] | - | 0.793 | 0.607 | 1.00 | 0.754 [0.740, 0.768] | 0.571 [0.563, 0.578] |
| weak balance | 0.485 [0.461, 0.508] | - | 0.794 | 0.624 | 0.98 | 0.751 [0.738, 0.765] | 0.593 [0.584, 0.602] |
| first-tie asymmetric | 0.492 [0.469, 0.516] | - | 0.792 | 0.607 | 1.00 | 0.755 [0.741, 0.769] | 0.571 [0.562, 0.579] |
| status | 0.511 [0.487, 0.535] | - | 0.792 | 0.581 | 0.65 | 0.636 [0.624, 0.647] | 0.579 [0.569, 0.590] |
| person propensity | 0.457 [0.436, 0.478] | - | 0.800 | 0.653 | - | - | - |
| conjunction | 0.482 [0.458, 0.504] | - | 0.794 | 0.626 | 1.00 | 0.734 [0.720, 0.747] | 0.614 [0.604, 0.624] |
| saturated 16 types | 0.476 [0.452, 0.498] | - | 0.797 | 0.640 | - | - | - |
| person + strict | 0.450 [0.429, 0.470] | - | 0.803 | 0.664 | - | - | - |
| person + weak | 0.449 [0.428, 0.469] | - | 0.804 | 0.666 | - | - | - |
| person + first-tie | 0.450 [0.429, 0.470] | - | 0.804 | 0.663 | - | - | - |
| person + status | 0.457 [0.436, 0.477] | - | 0.800 | 0.655 | - | - | - |
| person + 16 types | 0.448 [0.427, 0.469] | - | 0.805 | 0.666 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| strict balance - person propensity | +0.035 [+0.028, +0.042] | <0.001 |
| first-tie asymmetric - strict balance | +0.001 [-0.001, +0.002] | 0.382 |
| person + 16 types - person propensity | -0.009 [-0.012, -0.005] | <0.001 |
| person + first-tie - person + strict | -0.000 [-0.001, +0.001] | 0.770 |

*Where the rules disagree.* The first-tie rule and strict balance say different things only when a closing tie has a forward chain whose first tie is negative (6,182 of 78,254 closing ties). On those ties alone (models refitted on the training ties of that kind):

**wiki-RfA, closing ties with a negative-first-tie forward chain** (train 3,350 events, test 2,832; positive share train 0.637, test 0.659)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| base rate | 0.643 [0.620, 0.668] | - | 0.659 | 0.500 | - | - | - |
| strict balance | 0.619 [0.592, 0.649] | 0.632 | 0.666 | 0.601 | 1.00 | 0.634 [0.598, 0.667] | 0.554 [0.532, 0.577] |
| weak balance | 0.607 [0.579, 0.638] | 0.661 | 0.679 | 0.618 | 0.97 | 0.638 [0.603, 0.674] | 0.595 [0.567, 0.623] |
| first-tie asymmetric | 0.614 [0.587, 0.644] | 0.645 | 0.678 | 0.611 | 1.00 | 0.669 [0.629, 0.706] | 0.586 [0.560, 0.612] |
| status | 0.610 [0.581, 0.645] | 0.658 | 0.667 | 0.622 | 0.95 | 0.594 [0.566, 0.621] | 0.592 [0.564, 0.621] |
| person propensity | 0.585 [0.561, 0.613] | 0.703 | 0.701 | 0.654 | - | - | - |
| person + strict | 0.583 [0.558, 0.613] | 0.703 | 0.698 | 0.652 | - | - | - |
| person + first-tie | 0.582 [0.558, 0.610] | 0.707 | 0.707 | 0.651 | - | - | - |
| person + 16 types | 0.580 [0.554, 0.610] | 0.704 | 0.700 | 0.646 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| first-tie asymmetric - strict balance | -0.004 [-0.012, +0.002] | 0.233 |
| first-tie asymmetric - weak balance | +0.007 [+0.001, +0.014] | 0.030 |
| first-tie asymmetric - person propensity | +0.029 [+0.017, +0.041] | <0.001 |
| strict balance - person propensity | +0.033 [+0.021, +0.046] | <0.001 |
| person + first-tie - person + strict | -0.001 [-0.005, +0.004] | 0.773 |

### 3.4 wiki-RfA: converting ties (re-votes)

The target is the new sign of a voter's vote on a candidate the voter had voted on before. Every model includes the voter's previous sign, so the 'base rate' row is **persistence** (predict the old sign, calibrated). The question is what each rule's context adds to persistence. The 'own' columns are the rule's hard prediction alone and ignore the previous sign, so they are not comparable with persistence's accuracy; read the log-loss, which has the previous sign in every row.

**wiki-RfA re-votes, 70/30 chronological split** (train 3,453 events, test 2,328; positive share train 0.790, test 0.798)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| persistence (previous sign) | 0.392 [0.351, 0.441] | - | 0.784 | 0.784 | - | - | - |
| strict balance | 0.375 [0.335, 0.424] | 0.832 | 0.834 | 0.785 | 1.00 | 0.783 [0.749, 0.815] | 0.604 [0.581, 0.630] |
| weak balance | 0.371 [0.332, 0.420] | 0.838 | 0.837 | 0.785 | 1.00 | 0.775 [0.741, 0.809] | 0.652 [0.621, 0.685] |
| first-tie asymmetric | 0.380 [0.339, 0.430] | 0.821 | 0.834 | 0.784 | 1.00 | 0.787 [0.752, 0.820] | 0.597 [0.569, 0.631] |
| status | 0.385 [0.342, 0.439] | 0.807 | 0.821 | 0.784 | 0.97 | 0.670 [0.639, 0.699] | 0.612 [0.575, 0.654] |
| person propensity | 0.372 [0.338, 0.412] | 0.849 | 0.829 | 0.776 | - | - | - |
| conjunction | 0.371 [0.332, 0.421] | 0.836 | 0.842 | 0.782 | 1.00 | 0.744 [0.704, 0.785] | 0.686 [0.648, 0.725] |
| saturated 16 types | 0.374 [0.339, 0.418] | 0.839 | 0.834 | 0.780 | - | - | - |
| person + strict | 0.365 [0.331, 0.405] | 0.856 | 0.833 | 0.781 | - | - | - |
| person + weak | 0.365 [0.331, 0.405] | 0.856 | 0.834 | 0.779 | - | - | - |
| person + first-tie | 0.369 [0.335, 0.408] | 0.853 | 0.831 | 0.773 | - | - | - |
| person + status | 0.372 [0.338, 0.413] | 0.847 | 0.824 | 0.776 | - | - | - |
| person + 16 types | 0.374 [0.339, 0.414] | 0.847 | 0.836 | 0.776 | - | - | - |

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| strict balance - base rate | -0.017 [-0.025, -0.009] | <0.001 |
| weak balance - base rate | -0.021 [-0.030, -0.012] | <0.001 |
| first-tie asymmetric - base rate | -0.012 [-0.019, -0.005] | 0.001 |
| status - base rate | -0.007 [-0.014, +0.001] | 0.081 |
| person propensity - base rate | -0.020 [-0.035, -0.005] | 0.011 |
| person + 16 types - person propensity | +0.002 [-0.009, +0.011] | 0.811 |
| first-tie asymmetric - strict balance | +0.005 [+0.000, +0.009] | 0.042 |

**wiki-RfA re-votes, rolling origin** (train 1,957 events, test 3,824; positive share train 0.799, test 0.782)

| model | held-out log-loss [95% CI] | AUC | acc @0.5 | bal. acc @prior | own: coverage | own: accuracy [CI] | own: bal. accuracy [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| persistence (previous sign) | 0.406 [0.375, 0.443] | - | 0.780 | 0.785 | - | - | - |
| strict balance | 0.390 [0.359, 0.427] | - | 0.825 | 0.787 | 1.00 | 0.778 [0.752, 0.802] | 0.612 [0.592, 0.633] |
| weak balance | 0.386 [0.355, 0.423] | - | 0.828 | 0.785 | 1.00 | 0.770 [0.745, 0.795] | 0.648 [0.623, 0.672] |
| first-tie asymmetric | 0.396 [0.364, 0.434] | - | 0.815 | 0.785 | 1.00 | 0.775 [0.748, 0.800] | 0.589 [0.566, 0.614] |
| status | 0.402 [0.368, 0.442] | - | 0.811 | 0.785 | 0.97 | 0.660 [0.635, 0.683] | 0.601 [0.575, 0.628] |
| person propensity | 0.380 [0.353, 0.411] | - | 0.830 | 0.782 | - | - | - |
| conjunction | 0.387 [0.356, 0.424] | - | 0.831 | 0.784 | 1.00 | 0.743 [0.715, 0.771] | 0.670 [0.643, 0.696] |
| saturated 16 types | 0.383 [0.353, 0.418] | - | 0.828 | 0.784 | - | - | - |
| person + strict | 0.375 [0.347, 0.406] | - | 0.832 | 0.783 | - | - | - |
| person + weak | 0.374 [0.348, 0.406] | - | 0.833 | 0.782 | - | - | - |
| person + first-tie | 0.377 [0.350, 0.409] | - | 0.830 | 0.780 | - | - | - |
| person + status | 0.380 [0.353, 0.411] | - | 0.828 | 0.780 | - | - | - |
| person + 16 types | 0.378 [0.350, 0.410] | - | 0.834 | 0.781 | - | - | - |

## 4. Does the first-tie asymmetry replicate outside the fraternity?

### 4.1 What the Newcomb pattern is (post hoc re-read of the Newcomb run)

D&K's eight-type pattern in the Newcomb ranks, from the second wave on, is exactly the partition **'the closing tie has the sign of the second tie'**: LLL, LDD, DLL, DDD above the row-wise null, LLD, LDL, DLD, DDL below it. Counting the eight directions that match that partition under the row-wise null: w1 7/8, w2 8/8, w3 8/8, w4 8/8, w5 8/8, w6 8/8, w7 8/8, w8 8/8, w9 8/8, w10 8/8, w11 8/8, w12 8/8, w13 8/8, w14 8/8, w15 8/8. Under a **column-wise null** (each man's received signs held and permuted across senders, so popularity is held and the senders' quotas are free) the same pattern shrinks to |z| <= 3.4 in every cell of every wave (median over waves of the largest |z|: 2.4); agreement with the partition 4-6/8, about what chance gives (4/8). (2,000 draws per null; D&K's own 10,000-draw numbers are in `newcomb_n3.md`.) The first tie plays no part in this partition: DLL over and DLD under are 'copy the second tie' as much as LLL over and LLD under. So the pattern the Newcomb run called a first-tie asymmetry is also what a consensus about the third man (differential popularity, D&K's 'recognition of attributes', [L4512]) produces; the Newcomb data cannot separate the two, and a replication has to.

### 4.2 Summary of the eight-type comparison on the three sites

Direction of each of D&K's eight types against a shuffled-sign null, on formation-ordered closing ties, compared with three readings: the Newcomb pattern, 'the closing tie has the sign of the second tie' (which the Newcomb pattern equals from the second wave on), and strict balance. 'over' means more than the null. **Weighting.** 'event' counts each closing tie once, split over its forward-chain cells (the unit is the tie, and embeddedness cannot pose as a link between cell and sign); 'instance' counts every triad, as D&K count ordered triples, so a tie with many common neighbours counts many times and the test also asks whether embeddedness goes with sign. **Four coupled pairs.** A cell's two closings sum to the cell total, so each z score has a mirror image and 'x/8' counts every cell twice: 4/8 means two of the four cells agree. The two cells that separate the Newcomb pattern from balance are the two whose first tie is negative (mp: DLL against DLD; mm: DDL against DDD).

| site | null | period, weighting | closing ties | matches Newcomb | matches 'closing = second tie' | matches strict balance | DLL (Newcomb: over) | DLD (Newcomb: under) | DDD (Newcomb: over) |
| :--- | :--- | :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- |
| Bitcoin OTC | sender | whole, event | 7,639 | 4/8 | 4/8 | 8/8 | under (z -19.1) | over (z +19.1) | under (z -2.4) |
| Bitcoin OTC | sender | test, event | 3,350 | 4/8 | 4/8 | 8/8 | under (z -11.1) | over (z +11.1) | under (z -4.7) |
| Bitcoin OTC | sender | whole, instance | 7,639 | 4/8 | 4/8 | 8/8 | under (z -8.4) | over (z +8.4) | under (z -2.9) |
| Bitcoin OTC | sender x year | whole, event | 7,639 | 4/8 | 4/8 | 8/8 | under (z -16.2) | over (z +16.2) | under (z -3.6) |
| Bitcoin OTC | receiver | whole, event | 7,639 | 4/8 | 4/8 | 8/8 | under (z -23.4) | over (z +23.4) | under (z -3.7) |
| Bitcoin OTC | receiver | test, event | 3,350 | 4/8 | 4/8 | 8/8 | under (z -18.7) | over (z +18.7) | under (z -5.2) |
| Bitcoin OTC | receiver | whole, instance | 7,639 | 4/8 | 4/8 | 8/8 | under (z -15.9) | over (z +15.9) | under (z -2.0) |
| Bitcoin Alpha | sender | whole, event | 6,757 | 6/8 | 6/8 | 6/8 | under (z -5.6) | over (z +5.6) | over (z +2.5) |
| Bitcoin Alpha | sender | test, event | 2,839 | 6/8 | 6/8 | 6/8 | under (z -1.8) | over (z +1.8) | over (z +2.3) |
| Bitcoin Alpha | sender | whole, instance | 6,757 | 6/8 | 6/8 | 6/8 | under (z -3.0) | over (z +3.0) | over (z +2.4) |
| Bitcoin Alpha | sender x year | whole, event | 6,757 | 6/8 | 6/8 | 6/8 | under (z -3.4) | over (z +3.4) | over (z +2.3) |
| Bitcoin Alpha | receiver | whole, event | 6,757 | 6/8 | 6/8 | 6/8 | under (z -11.7) | over (z +11.7) | over (z +0.7) |
| Bitcoin Alpha | receiver | test, event | 2,839 | 4/8 | 4/8 | 8/8 | under (z -6.4) | over (z +6.4) | under (z -0.2) |
| Bitcoin Alpha | receiver | whole, instance | 6,757 | 4/8 | 4/8 | 4/8 | under (z -13.8) | over (z +13.8) | over (z +2.1) |
| wiki-RfA | sender | whole, event | 15,956 | 8/8 | 8/8 | 4/8 | over (z +2.5) | under (z -2.5) | over (z +4.1) |
| wiki-RfA | sender | test, event | 6,193 | 8/8 | 8/8 | 4/8 | over (z +2.5) | under (z -2.5) | over (z +3.6) |
| wiki-RfA | sender | whole, instance | 15,956 | 8/8 | 8/8 | 4/8 | over (z +2.8) | under (z -2.8) | over (z +0.7) |
| wiki-RfA | sender x year | whole, event | 15,956 | 8/8 | 8/8 | 4/8 | over (z +3.3) | under (z -3.3) | over (z +3.5) |
| wiki-RfA | receiver | whole, event | 15,956 | 4/8 | 4/8 | 4/8 | under (z -21.3) | over (z +21.3) | over (z +18.2) |
| wiki-RfA | receiver | test, event | 6,193 | 4/8 | 4/8 | 4/8 | under (z -12.8) | over (z +12.8) | over (z +13.2) |
| wiki-RfA | receiver | whole, instance | 15,956 | 4/8 | 4/8 | 4/8 | under (z -16.7) | over (z +16.7) | over (z +13.6) |

### 4.3 Bitcoin OTC: the eight D&K types on formation-ordered closing ties

*Bitcoin OTC, sender null (closing signs shuffled within sender: the formation-ordered analogue of the Newcomb run's row-wise null); whole period, each closing tie counted once (split over its forward-chain cells), 7,639 closing ties with a forward-chain context.* Agreement of the eight directions with: Newcomb 4/8, 'closing = second tie' 4/8, strict balance 8/8.

| type | observed | null mean | z | p(obs > null) | here | Newcomb | strict balance |
| :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- |
| LLL | 5,948.8 | 5,609.9 | 37.3 | 1.000 | over | over | over |
| LLD | 349.3 | 688.2 | -37.3 | 0.000 | under | under | under |
| LDL | 60.5 | 284.1 | -31.0 | 0.000 | under | under | under |
| LDD | 423.1 | 199.4 | 31.0 | 1.000 | over | over | over |
| DLL | 133.2 | 254.6 | -19.1 | 0.000 | under | over | under |
| DLD | 665.2 | 543.8 | 19.1 | 1.000 | over | under | over |
| DDL | 40.5 | 34.4 | 2.4 | 0.990 | over | under | over |
| DDD | 18.4 | 24.6 | -2.4 | 0.010 | under | over | under |

*Bitcoin OTC, receiver null (closing signs shuffled within receiver: reception held); whole period, each closing tie counted once (split over its forward-chain cells), 7,639 closing ties with a forward-chain context.* Agreement of the eight directions with: Newcomb 4/8, 'closing = second tie' 4/8, strict balance 8/8.

| type | observed | null mean | z | p(obs > null) | here | Newcomb | strict balance |
| :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- |
| LLL | 5,948.8 | 5,739.4 | 29.5 | 1.000 | over | over | over |
| LLD | 349.3 | 558.7 | -29.5 | 0.000 | under | under | under |
| LDL | 60.5 | 148.3 | -16.8 | 0.000 | under | under | under |
| LDD | 423.1 | 335.3 | 16.8 | 1.000 | over | over | over |
| DLL | 133.2 | 264.2 | -23.4 | 0.000 | under | over | under |
| DLD | 665.2 | 534.2 | 23.4 | 1.000 | over | under | over |
| DDL | 40.5 | 31.1 | 3.7 | 1.000 | over | under | over |
| DDD | 18.4 | 27.8 | -3.7 | 0.000 | under | over | under |

### 4.4 Bitcoin Alpha: the eight D&K types on formation-ordered closing ties

*Bitcoin Alpha, sender null (closing signs shuffled within sender: the formation-ordered analogue of the Newcomb run's row-wise null); whole period, each closing tie counted once (split over its forward-chain cells), 6,757 closing ties with a forward-chain context.* Agreement of the eight directions with: Newcomb 6/8, 'closing = second tie' 6/8, strict balance 6/8.

| type | observed | null mean | z | p(obs > null) | here | Newcomb | strict balance |
| :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- |
| LLL | 6,045.3 | 5,913.0 | 24.0 | 1.000 | over | over | over |
| LLD | 288.8 | 421.1 | -24.0 | 0.000 | under | under | under |
| LDL | 39.7 | 148.8 | -25.1 | 0.000 | under | under | under |
| LDD | 153.3 | 44.2 | 25.1 | 1.000 | over | over | over |
| DLL | 136.8 | 157.0 | -5.6 | 0.000 | under | over | under |
| DLD | 75.8 | 55.5 | 5.6 | 1.000 | over | under | over |
| DDL | 10.2 | 13.1 | -2.5 | 0.009 | under | under | over |
| DDD | 7.2 | 4.2 | 2.5 | 0.991 | over | over | under |

*Bitcoin Alpha, receiver null (closing signs shuffled within receiver: reception held); whole period, each closing tie counted once (split over its forward-chain cells), 6,757 closing ties with a forward-chain context.* Agreement of the eight directions with: Newcomb 6/8, 'closing = second tie' 6/8, strict balance 6/8.

| type | observed | null mean | z | p(obs > null) | here | Newcomb | strict balance |
| :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- |
| LLL | 6,045.3 | 5,992.6 | 13.4 | 1.000 | over | over | over |
| LLD | 288.8 | 341.5 | -13.4 | 0.000 | under | under | under |
| LDL | 39.7 | 62.5 | -7.7 | 0.000 | under | under | under |
| LDD | 153.3 | 130.4 | 7.7 | 1.000 | over | over | over |
| DLL | 136.8 | 166.0 | -11.7 | 0.000 | under | over | under |
| DLD | 75.8 | 46.5 | 11.7 | 1.000 | over | under | over |
| DDL | 10.2 | 10.8 | -0.7 | 0.217 | under | under | over |
| DDD | 7.2 | 6.6 | 0.7 | 0.783 | over | over | under |

### 4.5 wiki-RfA: the eight D&K types on formation-ordered closing ties

*wiki-RfA, sender null (closing signs shuffled within sender: the formation-ordered analogue of the Newcomb run's row-wise null); whole period, each closing tie counted once (split over its forward-chain cells), 15,956 closing ties with a forward-chain context.* Agreement of the eight directions with: Newcomb 8/8, 'closing = second tie' 8/8, strict balance 4/8.

| type | observed | null mean | z | p(obs > null) | here | Newcomb | strict balance |
| :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- |
| LLL | 6,158.4 | 6,002.6 | 9.6 | 1.000 | over | over | over |
| LLD | 1,444.8 | 1,600.5 | -9.6 | 0.000 | under | under | under |
| LDL | 4,147.3 | 4,289.5 | -9.1 | 0.000 | under | under | under |
| LDD | 1,404.4 | 1,262.2 | 9.1 | 1.000 | over | over | over |
| DLL | 976.5 | 951.4 | 2.5 | 0.993 | over | over | under |
| DLD | 661.4 | 686.4 | -2.5 | 0.007 | under | under | over |
| DDL | 623.8 | 662.4 | -4.1 | 0.001 | under | under | over |
| DDD | 539.5 | 500.8 | 4.1 | 1.000 | over | over | under |

*wiki-RfA, receiver null (closing signs shuffled within receiver: reception held); whole period, each closing tie counted once (split over its forward-chain cells), 15,956 closing ties with a forward-chain context.* Agreement of the eight directions with: Newcomb 4/8, 'closing = second tie' 4/8, strict balance 4/8.

| type | observed | null mean | z | p(obs > null) | here | Newcomb | strict balance |
| :--- | ---: | ---: | ---: | ---: | :--- | :--- | :--- |
| LLL | 6,158.4 | 5,877.8 | 17.9 | 1.000 | over | over | over |
| LLD | 1,444.8 | 1,725.4 | -17.9 | 0.000 | under | under | under |
| LDL | 4,147.3 | 4,027.2 | 8.2 | 1.000 | over | under | under |
| LDD | 1,404.4 | 1,524.5 | -8.2 | 0.000 | under | over | over |
| DLL | 976.5 | 1,208.1 | -21.3 | 0.000 | under | over | under |
| DLD | 661.4 | 429.8 | 21.3 | 1.000 | over | under | over |
| DDL | 623.8 | 792.9 | -18.2 | 0.000 | under | under | over |
| DDD | 539.5 | 370.3 | 18.2 | 1.000 | over | over | under |

### 4.6 The four forward-chain cells, and what the first tie adds once the person terms are in

Share of closing ties that are positive, by the signs (first tie u -> w, second tie w -> v), counting every triad ('instance') or every closing tie once ('event': split over its cells), cluster-bootstrap 95% interval (1,000 draws; clusters are ratees on Bitcoin and elections on wiki-RfA). Strict balance says: pp high, pm low, mp low, mm high. The first-tie rule (= copy the second tie): pp high, pm low, **mp high**, mm low.

*Bitcoin OTC*

| cell or contrast | weighting | triads (instance) or closing-tie weight (event) | closing ties | P(closing +) or difference [95% CI] |
| :--- | :--- | ---: | ---: | ---: |
| FFpp | instance | 19,639 | 6,518 | 0.938 [0.919, 0.953] |
| FFpm | instance | 1,294 | 754 | 0.181 [0.121, 0.260] |
| FFmp | instance | 2,586 | 1,224 | 0.246 [0.174, 0.338] |
| FFmm | instance | 326 | 147 | 0.733 [0.535, 0.869] |
| mp - pm | instance |  |  | +0.065 [-0.038, +0.171] |
| pp - mm | instance |  |  | +0.205 [+0.076, +0.396] |
| mm - mp | instance |  |  | +0.487 [+0.286, +0.639] |
| FFpp | event | 6,298.1 | 6,518 | 0.945 [0.934, 0.954] |
| FFpm | event | 483.5 | 754 | 0.125 [0.092, 0.169] |
| FFmp | event | 798.4 | 1,224 | 0.167 [0.134, 0.207] |
| FFmm | event | 59.0 | 147 | 0.687 [0.556, 0.822] |
| mp - pm | event |  |  | +0.042 [-0.012, +0.093] |
| pp - mm | event |  |  | +0.257 [+0.122, +0.385] |
| mm - mp | event |  |  | +0.520 [+0.381, +0.657] |

Coefficients of the four forward-chain counts in the model *person + 16 types* fitted on all 8,972 closing ties, training and test together, as a description, not a forecast (log-odds per unit of log(1 + count); cluster-bootstrap 95% interval, 400 refits on resampled ratees):

| term | coefficient [95% CI] |
| :--- | ---: |
| FFpp | +0.64 [+0.27, +0.93] |
| FFpm | -1.22 [-1.72, -0.71] |
| FFmp | -1.41 [-1.89, -1.03] |
| FFmm | +1.36 [+0.76, +2.07] |
| FFmp - FFpm (first-tie asymmetry given the person terms) | -0.19 [-0.84, +0.40] |
| (FFpp + FFmm) - (FFpm + FFmp) (the product structure of balance given the person terms) | +4.63 [+3.65, +5.75] |

*Bitcoin Alpha*

| cell or contrast | weighting | triads (instance) or closing-tie weight (event) | closing ties | P(closing +) or difference [95% CI] |
| :--- | :--- | ---: | ---: | ---: |
| FFpp | instance | 19,301 | 6,514 | 0.948 [0.933, 0.960] |
| FFpm | instance | 587 | 343 | 0.257 [0.155, 0.409] |
| FFmp | instance | 798 | 577 | 0.723 [0.654, 0.781] |
| FFmm | instance | 107 | 77 | 0.673 [0.412, 0.871] |
| mp - pm | instance |  |  | +0.466 [+0.313, +0.573] |
| pp - mm | instance |  |  | +0.275 [+0.081, +0.525] |
| mm - mp | instance |  |  | -0.050 [-0.298, +0.128] |
| FFpp | event | 6,334.2 | 6,514 | 0.954 [0.945, 0.962] |
| FFpm | event | 193.0 | 343 | 0.206 [0.126, 0.322] |
| FFmp | event | 212.5 | 577 | 0.644 [0.569, 0.714] |
| FFmm | event | 17.3 | 77 | 0.587 [0.379, 0.798] |
| mp - pm | event |  |  | +0.438 [+0.323, +0.530] |
| pp - mm | event |  |  | +0.367 [+0.155, +0.573] |
| mm - mp | event |  |  | -0.056 [-0.262, +0.148] |

Coefficients of the four forward-chain counts in the model *person + 16 types* fitted on all 7,875 closing ties, training and test together, as a description, not a forecast (log-odds per unit of log(1 + count); cluster-bootstrap 95% interval, 400 refits on resampled ratees):

| term | coefficient [95% CI] |
| :--- | ---: |
| FFpp | +0.34 [-0.09, +0.80] |
| FFpm | -0.29 [-0.90, +0.26] |
| FFmp | -0.76 [-1.41, -0.20] |
| FFmm | +1.15 [+0.34, +2.16] |
| FFmp - FFpm (first-tie asymmetry given the person terms) | -0.47 [-1.31, +0.50] |
| (FFpp + FFmm) - (FFpm + FFmp) (the product structure of balance given the person terms) | +2.53 [+1.40, +3.85] |

*wiki-RfA*

| cell or contrast | weighting | triads (instance) or closing-tie weight (event) | closing ties | P(closing +) or difference [95% CI] |
| :--- | :--- | ---: | ---: | ---: |
| FFpp | instance | 36,800 | 11,264 | 0.811 [0.779, 0.839] |
| FFpm | instance | 22,932 | 9,813 | 0.769 [0.742, 0.793] |
| FFmp | instance | 6,839 | 4,309 | 0.624 [0.586, 0.663] |
| FFmm | instance | 4,157 | 3,134 | 0.599 [0.563, 0.632] |
| mp - pm | instance |  |  | -0.145 [-0.173, -0.117] |
| pp - mm | instance |  |  | +0.212 [+0.181, +0.249] |
| mm - mp | instance |  |  | -0.026 [-0.062, +0.005] |
| FFpp | event | 7,603.1 | 11,264 | 0.810 [0.787, 0.832] |
| FFpm | event | 5,551.7 | 9,813 | 0.747 [0.722, 0.771] |
| FFmp | event | 1,637.9 | 4,309 | 0.596 [0.561, 0.630] |
| FFmm | event | 1,163.2 | 3,134 | 0.536 [0.498, 0.572] |
| mp - pm | event |  |  | -0.151 [-0.184, -0.121] |
| pp - mm | event |  |  | +0.274 [+0.239, +0.313] |
| mm - mp | event |  |  | -0.060 [-0.103, -0.022] |

Coefficients of the four forward-chain counts in the model *person + 16 types* fitted on all 78,254 closing ties, training and test together, as a description, not a forecast (log-odds per unit of log(1 + count); cluster-bootstrap 95% interval, 400 refits on resampled elections):

| term | coefficient [95% CI] |
| :--- | ---: |
| FFpp | +0.24 [+0.14, +0.36] |
| FFpm | -0.08 [-0.19, +0.03] |
| FFmp | -0.06 [-0.19, +0.08] |
| FFmm | -0.08 [-0.23, +0.07] |
| FFmp - FFpm (first-tie asymmetry given the person terms) | +0.02 [-0.18, +0.22] |
| (FFpp + FFmm) - (FFpm + FFmp) (the product structure of balance given the person terms) | +0.30 [+0.04, +0.59] |

### 4.7 Do the triad terms add anything to the person terms? (permutation null)

| site | added to the person terms | log-loss person only | log-loss with the addition | gain | gain under the permutation null | p |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| Bitcoin OTC | person + 16 types | 0.3546 | 0.2743 | +0.0803 | -0.0040 (sd 0.0050, max +0.0093) | <= 0.005 |
| Bitcoin OTC | person + strict balance | 0.3546 | 0.2580 | +0.0966 | -0.0003 (sd 0.0030, max +0.0071) | <= 0.005 |
| Bitcoin OTC | person + weak balance | 0.3546 | 0.2653 | +0.0893 | -0.0004 (sd 0.0030, max +0.0073) | <= 0.005 |
| Bitcoin OTC | person + first-tie asymmetric | 0.3546 | 0.2949 | +0.0597 | -0.0006 (sd 0.0028, max +0.0054) | <= 0.005 |
| Bitcoin OTC | person + status | 0.3546 | 0.3283 | +0.0263 | -0.0001 (sd 0.0010, max +0.0022) | <= 0.005 |
| Bitcoin Alpha | person + 16 types | 0.2439 | 0.2434 | +0.0006 | -0.0076 (sd 0.0041, max +0.0015) | 0.010 |
| Bitcoin Alpha | person + strict balance | 0.2439 | 0.2384 | +0.0056 | -0.0051 (sd 0.0028, max -0.0005) | <= 0.005 |
| Bitcoin Alpha | person + weak balance | 0.2439 | 0.2409 | +0.0030 | -0.0050 (sd 0.0028, max -0.0005) | <= 0.005 |
| Bitcoin Alpha | person + first-tie asymmetric | 0.2439 | 0.2355 | +0.0084 | -0.0047 (sd 0.0031, max +0.0008) | <= 0.005 |
| Bitcoin Alpha | person + status | 0.2439 | 0.2412 | +0.0027 | -0.0038 (sd 0.0020, max +0.0015) | <= 0.005 |
| wiki-RfA | person + 16 types | 0.4714 | 0.4629 | +0.0085 | -0.0000 (sd 0.0003, max +0.0005) | <= 0.005 |
| wiki-RfA | person + strict balance | 0.4714 | 0.4651 | +0.0063 | +0.0001 (sd 0.0002, max +0.0004) | <= 0.005 |
| wiki-RfA | person + weak balance | 0.4714 | 0.4634 | +0.0079 | +0.0001 (sd 0.0002, max +0.0005) | <= 0.005 |
| wiki-RfA | person + first-tie asymmetric | 0.4714 | 0.4646 | +0.0068 | +0.0001 (sd 0.0002, max +0.0004) | <= 0.005 |
| wiki-RfA | person + status | 0.4714 | 0.4710 | +0.0004 | +0.0003 (sd 0.0002, max +0.0007) | 0.333 |

The permutation null's mean gain is negative when the added features are noise (the refitted model overfits them); the p value says the observed gain is beyond what shuffled features give, not that it is large. The size of the gain is the column before.

The null is anti-conservative where the refit overfits: a feature that duplicates the person terms overfits less than a shuffled one, so an addition with no held-out gain can still beat a null whose mean gain is negative. Where N2 and the paired bootstrap of section 3 disagree (N2 p <= 0.05 while the paired interval of the held-out log-loss difference includes zero), the interval is the reading: Bitcoin Alpha: person + 16 types - person -0.001 [-0.011, +0.011] against N2 p 0.010; person + strict - person -0.006 [-0.016, +0.005] against N2 p <= 0.005; person + weak - person -0.003 [-0.014, +0.008] against N2 p <= 0.005; person + status - person -0.003 [-0.010, +0.006] against N2 p <= 0.005.

## 5. Variations

Every table is the pre-specified protocol with one thing changed; entries are held-out log-loss (lower is better; the best of the four canonical single rules is in bold). 'first-tie - strict' and 'person+16 - person' are paired log-loss differences with cluster-bootstrap intervals (B = 400); negative means the first named model is better. Intervals on the individual entries are in section 3 and are of the same order as in the primary tables.

### 5.1 Bitcoin OTC

**Embeddedness threshold (closing ties with at least k common neighbours; the model is refitted on the training ties that pass the same threshold)**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| k >= 1 | 3,800 | 0.72 | 0.657 | 0.528 | 0.265 | **0.264** | 0.407 | 0.560 | 0.355 | 0.292 | 0.274 | +0.142 [+0.079, +0.219] | -0.080 [-0.106, -0.056] |
| k >= 2 | 2,669 | 0.71 | 0.658 | 0.518 | 0.237 | **0.235** | 0.382 | 0.513 | 0.327 | 0.252 | 0.238 | +0.145 [+0.074, +0.231] | -0.089 [-0.118, -0.059] |
| k >= 3 | 2,001 | 0.72 | 0.655 | 0.508 | 0.225 | **0.221** | 0.367 | 0.488 | 0.322 | 0.234 | 0.235 | +0.141 [+0.059, +0.231] | -0.087 [-0.119, -0.058] |
| k >= 5 | 1,240 | 0.73 | 0.639 | 0.477 | 0.209 | **0.207** | 0.385 | 0.453 | 0.337 | 0.219 | 0.248 | +0.176 [+0.077, +0.308] | -0.090 [-0.133, -0.053] |
| k >= 10 | 512 | 0.81 | 0.502 | 0.390 | 0.210 | **0.208** | 0.373 | 0.418 | 0.361 | 0.266 | 0.356 | +0.163 [+0.013, +0.345] | -0.005 [-0.040, +0.040] |
| k >= 25 | 78 | - | too few |  |  |  |  |  |  |  |  |  |  |

**Sign recode (ratings in between are dropped from the graph, as targets and as context)**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| all | 3,800 | 0.72 | 0.657 | 0.528 | 0.265 | **0.264** | 0.407 | 0.560 | 0.355 | 0.292 | 0.274 | +0.142 [+0.079, +0.219] | -0.080 [-0.106, -0.056] |
| drop+1 | 1,498 | 0.58 | 0.712 | 0.620 | 0.381 | **0.377** | 0.491 | 0.638 | 0.428 | 0.389 | 0.323 | +0.110 [+0.045, +0.178] | -0.105 [-0.155, -0.061] |
| drop-1..-4 | 3,652 | 0.76 | 0.622 | 0.466 | 0.200 | **0.197** | 0.351 | 0.522 | 0.298 | 0.219 | 0.224 | +0.152 [+0.079, +0.237] | -0.074 [-0.105, -0.043] |
| drop+1,-1..-4 | 1,375 | 0.63 | 0.699 | 0.560 | 0.307 | **0.296** | 0.452 | 0.609 | 0.387 | 0.308 | 0.273 | +0.145 [+0.053, +0.247] | -0.114 [-0.159, -0.069] |

**Time design**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| split 50/50 | 5,487 | 0.76 | 0.605 | 0.509 | 0.270 | **0.267** | 0.369 | 0.511 | 0.349 | 0.284 | 0.277 | +0.099 [+0.050, +0.152] | -0.072 [-0.095, -0.054] |
| split 60/40 | 4,633 | 0.75 | 0.602 | 0.502 | 0.260 | **0.257** | 0.369 | 0.521 | 0.324 | 0.290 | 0.270 | +0.109 [+0.057, +0.172] | -0.054 [-0.075, -0.031] |
| split 70/30 | 3,800 | 0.72 | 0.657 | 0.528 | 0.265 | **0.264** | 0.407 | 0.560 | 0.355 | 0.292 | 0.274 | +0.142 [+0.079, +0.219] | -0.080 [-0.106, -0.056] |
| split 80/20 | 2,491 | 0.81 | 0.488 | 0.481 | **0.308** | 0.309 | 0.316 | 0.437 | 0.394 | 0.335 | 0.295 | +0.008 [-0.008, +0.024] | -0.099 [-0.132, -0.058] |
| snapshot frozen at the 70% cut | 1,203 | 0.84 | 0.451 | 0.461 | 0.389 | 0.385 | **0.374** | 0.509 | 0.373 | 0.401 | 0.384 | -0.014 [-0.036, +0.012] | +0.011 [-0.013, +0.031] |
| rolling origin, 5 blocks from 50% | 5,487 | 0.76 | 0.588 | 0.509 | 0.264 | **0.259** | 0.362 | 0.489 | 0.293 | 0.275 | 0.222 | +0.098 [+0.052, +0.150] | -0.071 [-0.093, -0.054] |
| rolling origin, 10 blocks from 30% | 7,297 | 0.77 | 0.587 | 0.498 | 0.262 | **0.259** | 0.362 | 0.490 | 0.283 | 0.289 | 0.223 | +0.100 [+0.061, +0.145] | -0.060 [-0.078, -0.044] |

**Ridge penalty**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ridge 0.01 | 3,800 | 0.72 | 0.657 | 0.528 | 0.266 | **0.264** | 0.408 | 0.560 | 0.356 | 0.294 | 0.279 | +0.142 [+0.078, +0.220] | -0.076 [-0.103, -0.051] |
| ridge 1 | 3,800 | 0.72 | 0.657 | 0.528 | 0.265 | **0.264** | 0.407 | 0.560 | 0.355 | 0.292 | 0.274 | +0.142 [+0.079, +0.219] | -0.080 [-0.106, -0.056] |
| ridge 100 | 3,800 | 0.72 | 0.657 | 0.528 | 0.311 | **0.308** | 0.412 | 0.569 | 0.319 | 0.343 | 0.254 | +0.101 [+0.054, +0.160] | -0.065 [-0.081, -0.050] |

**Target set** (the rules see triads only; 'person+recip' adds the sign of a visible v -> u tie)

| target set | n test | test + | base | recent | strict | first-tie | person | person+recip | person+16 | person+recip+16 | (person+recip+16) - (person+recip) [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| first tie of the pair (primary) | 3,800 | 0.72 | 0.657 | 0.528 | 0.265 | 0.407 | 0.355 | 0.355 | 0.274 | 0.274 | -0.080 [-0.106, -0.056] |
| every new directed tie | 6,077 | 0.79 | 0.573 | 0.463 | 0.258 | 0.343 | 0.352 | 0.319 | 0.275 | 0.253 | -0.066 [-0.099, -0.036] |
| reciprocating ties only | 2,277 | 0.89 | 0.371 | 0.355 | 0.228 | 0.210 | 0.357 | 0.285 | 0.291 | 0.233 | -0.052 [-0.095, -0.012] |

### 5.2 Bitcoin Alpha

**Embeddedness threshold (closing ties with at least k common neighbours; the model is refitted on the training ties that pass the same threshold)**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| k >= 1 | 3,216 | 0.88 | 0.406 | 0.375 | 0.307 | **0.306** | 0.307 | 0.394 | 0.244 | 0.312 | 0.243 | +0.000 [-0.012, +0.017] | -0.001 [-0.011, +0.010] |
| k >= 2 | 2,208 | 0.87 | 0.412 | 0.392 | 0.291 | 0.289 | **0.289** | 0.393 | 0.234 | 0.288 | 0.226 | -0.002 [-0.020, +0.021] | -0.008 [-0.018, +0.003] |
| k >= 3 | 1,682 | 0.87 | 0.398 | 0.389 | 0.267 | **0.266** | 0.268 | 0.371 | 0.229 | 0.265 | 0.221 | +0.001 [-0.017, +0.021] | -0.008 [-0.025, +0.009] |
| k >= 5 | 1,085 | 0.88 | 0.380 | 0.374 | 0.248 | **0.244** | 0.248 | 0.342 | 0.234 | 0.257 | 0.236 | -0.000 [-0.017, +0.018] | +0.002 [-0.016, +0.021] |
| k >= 10 | 438 | 0.89 | 0.343 | 0.352 | 0.243 | 0.241 | **0.240** | 0.315 | 0.239 | 0.240 | 0.222 | -0.003 [-0.020, +0.010] | -0.017 [-0.045, +0.014] |
| k >= 25 | 55 | - | too few |  |  |  |  |  |  |  |  |  |  |

**Sign recode (ratings in between are dropped from the graph, as targets and as context)**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| all | 3,216 | 0.88 | 0.406 | 0.375 | 0.307 | **0.306** | 0.307 | 0.394 | 0.244 | 0.312 | 0.243 | +0.000 [-0.012, +0.017] | -0.001 [-0.011, +0.010] |
| drop+1 | 1,234 | 0.76 | 0.583 | 0.548 | 0.451 | 0.447 | **0.432** | 0.557 | 0.360 | 0.411 | 0.327 | -0.019 [-0.048, +0.004] | -0.034 [-0.053, -0.014] |
| drop-1..-4 | 3,088 | 0.93 | 0.280 | 0.269 | 0.174 | 0.173 | **0.172** | 0.255 | 0.148 | 0.175 | 0.144 | -0.002 [-0.012, +0.006] | -0.004 [-0.012, +0.006] |
| drop+1,-1..-4 | 1,111 | 0.86 | 0.421 | 0.414 | 0.274 | 0.271 | **0.258** | 0.407 | 0.244 | 0.250 | 0.210 | -0.017 [-0.040, +0.006] | -0.034 [-0.057, -0.017] |

**Time design**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| split 50/50 | 5,053 | 0.89 | 0.435 | 0.353 | 0.300 | **0.299** | 0.315 | 0.414 | 0.234 | 0.320 | 0.228 | +0.015 [+0.002, +0.030] | -0.006 [-0.014, +0.002] |
| split 60/40 | 4,201 | 0.88 | 0.415 | 0.362 | 0.296 | **0.296** | 0.301 | 0.385 | 0.227 | 0.296 | 0.214 | +0.005 [-0.006, +0.020] | -0.012 [-0.019, -0.005] |
| split 70/30 | 3,216 | 0.88 | 0.406 | 0.375 | 0.307 | **0.306** | 0.307 | 0.394 | 0.244 | 0.312 | 0.243 | +0.000 [-0.012, +0.017] | -0.001 [-0.011, +0.010] |
| split 80/20 | 2,348 | 0.87 | 0.410 | 0.376 | 0.336 | **0.335** | 0.342 | 0.399 | 0.272 | 0.335 | 0.246 | +0.007 [-0.011, +0.031] | -0.026 [-0.041, -0.012] |
| snapshot frozen at the 70% cut | 1,004 | 0.80 | 0.628 | 0.502 | 0.523 | **0.522** | 0.525 | 0.621 | 0.564 | 0.567 | 0.562 | +0.002 [-0.019, +0.019] | -0.002 [-0.018, +0.014] |
| rolling origin, 5 blocks from 50% | 5,053 | 0.89 | 0.382 | 0.353 | 0.277 | **0.277** | 0.285 | 0.356 | 0.214 | 0.276 | 0.198 | +0.008 [-0.003, +0.021] | -0.016 [-0.022, -0.008] |
| rolling origin, 10 blocks from 30% | 6,647 | 0.91 | 0.322 | 0.301 | 0.240 | **0.240** | 0.247 | 0.303 | 0.189 | 0.239 | 0.177 | +0.006 [-0.004, +0.015] | -0.012 [-0.018, -0.006] |

**Ridge penalty**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ridge 0.01 | 3,216 | 0.88 | 0.406 | 0.375 | 0.309 | **0.308** | 0.308 | 0.395 | 0.245 | 0.321 | 0.254 | -0.001 [-0.014, +0.016] | +0.009 [-0.004, +0.026] |
| ridge 1 | 3,216 | 0.88 | 0.406 | 0.375 | 0.307 | **0.306** | 0.307 | 0.394 | 0.244 | 0.312 | 0.243 | +0.000 [-0.012, +0.017] | -0.001 [-0.011, +0.010] |
| ridge 100 | 3,216 | 0.88 | 0.406 | 0.375 | 0.345 | 0.344 | **0.328** | 0.395 | 0.249 | 0.346 | 0.234 | -0.018 [-0.029, -0.009] | -0.015 [-0.020, -0.011] |

**Target set** (the rules see triads only; 'person+recip' adds the sign of a visible v -> u tie)

| target set | n test | test + | base | recent | strict | first-tie | person | person+recip | person+16 | person+recip+16 | (person+recip+16) - (person+recip) [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| first tie of the pair (primary) | 3,216 | 0.88 | 0.406 | 0.375 | 0.307 | 0.307 | 0.244 | 0.244 | 0.243 | 0.243 | -0.001 [-0.011, +0.010] |
| every new directed tie | 3,976 | 0.87 | 0.426 | 0.402 | 0.335 | 0.323 | 0.267 | 0.262 | 0.267 | 0.260 | -0.002 [-0.014, +0.013] |
| reciprocating ties only | 760 | 0.82 | 0.497 | 0.519 | 0.428 | 0.379 | 0.345 | 0.315 | 0.339 | 0.306 | -0.009 [-0.040, +0.016] |

### 5.3 wiki-RfA

**Embeddedness threshold (closing ties with at least k common neighbours; the model is refitted on the training ties that pass the same threshold)**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| k >= 1 | 26,204 | 0.78 | 0.534 | 0.562 | 0.507 | **0.500** | 0.507 | 0.525 | 0.471 | 0.491 | 0.463 | -0.001 [-0.003, +0.002] | -0.009 [-0.013, -0.004] |
| k >= 2 | 19,974 | 0.78 | 0.536 | 0.563 | 0.501 | **0.493** | 0.501 | 0.526 | 0.472 | 0.483 | 0.460 | +0.000 [-0.002, +0.002] | -0.012 [-0.016, -0.007] |
| k >= 3 | 16,496 | 0.78 | 0.533 | 0.561 | 0.495 | **0.487** | 0.496 | 0.523 | 0.471 | 0.476 | 0.457 | +0.001 [-0.001, +0.003] | -0.014 [-0.019, -0.009] |
| k >= 5 | 12,222 | 0.79 | 0.520 | 0.555 | 0.480 | **0.472** | 0.481 | 0.508 | 0.463 | 0.465 | 0.451 | +0.001 [-0.001, +0.004] | -0.012 [-0.018, -0.007] |
| k >= 10 | 7,162 | 0.81 | 0.490 | 0.535 | 0.456 | **0.451** | 0.457 | 0.476 | 0.443 | 0.441 | 0.433 | +0.002 [-0.001, +0.005] | -0.010 [-0.016, -0.005] |
| k >= 25 | 2,356 | 0.83 | 0.459 | 0.522 | 0.434 | **0.431** | 0.436 | 0.440 | 0.418 | 0.424 | 0.418 | +0.002 [-0.002, +0.006] | +0.000 [-0.009, +0.009] |

**Sign recode (neutral votes)**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| neutral: drop | 26,204 | 0.78 | 0.534 | 0.562 | 0.507 | **0.500** | 0.507 | 0.525 | 0.471 | 0.491 | 0.463 | -0.001 [-0.003, +0.002] | -0.009 [-0.013, -0.004] |
| neutral: oppose | 28,216 | 0.73 | 0.591 | 0.623 | 0.572 | **0.563** | 0.571 | 0.583 | 0.534 | 0.555 | 0.528 | -0.001 [-0.002, +0.001] | -0.006 [-0.010, -0.002] |
| neutral: support | 28,216 | 0.79 | 0.517 | 0.540 | 0.494 | **0.488** | 0.494 | 0.511 | 0.460 | 0.480 | 0.453 | +0.000 [-0.001, +0.002] | -0.007 [-0.010, -0.004] |

**Time design**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| split 50/50 | 42,114 | 0.79 | 0.525 | 0.543 | 0.495 | **0.488** | 0.496 | 0.516 | 0.459 | 0.480 | 0.451 | +0.001 [-0.001, +0.002] | -0.008 [-0.012, -0.005] |
| split 60/40 | 34,605 | 0.78 | 0.544 | 0.562 | 0.514 | **0.507** | 0.514 | 0.535 | 0.476 | 0.498 | 0.468 | +0.000 [-0.002, +0.002] | -0.009 [-0.012, -0.004] |
| split 70/30 | 26,204 | 0.78 | 0.534 | 0.562 | 0.507 | **0.500** | 0.507 | 0.525 | 0.471 | 0.491 | 0.463 | -0.001 [-0.003, +0.002] | -0.009 [-0.013, -0.004] |
| split 80/20 | 17,723 | 0.78 | 0.534 | 0.572 | 0.514 | **0.507** | 0.512 | 0.525 | 0.471 | 0.495 | 0.465 | -0.001 [-0.004, +0.001] | -0.006 [-0.011, -0.000] |
| snapshot frozen at the 70% cut | 4,819 | 0.77 | 0.560 | 0.543 | 0.546 | **0.539** | 0.546 | 0.558 | 0.518 | 0.523 | 0.509 | -0.001 [-0.006, +0.006] | -0.009 [-0.019, -0.001] |
| rolling origin, 5 blocks from 50% | 42,114 | 0.79 | 0.519 | 0.543 | 0.492 | **0.485** | 0.492 | 0.511 | 0.457 | 0.476 | 0.448 | +0.001 [-0.001, +0.002] | -0.009 [-0.012, -0.006] |
| rolling origin, 10 blocks from 30% | 57,512 | 0.80 | 0.498 | 0.525 | 0.471 | **0.466** | 0.472 | 0.490 | 0.441 | 0.457 | 0.432 | +0.000 [-0.001, +0.002] | -0.009 [-0.012, -0.007] |

**Ridge penalty**

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| ridge 0.01 | 26,204 | 0.78 | 0.534 | 0.562 | 0.507 | **0.500** | 0.507 | 0.525 | 0.471 | 0.491 | 0.463 | -0.001 [-0.003, +0.002] | -0.009 [-0.013, -0.004] |
| ridge 1 | 26,204 | 0.78 | 0.534 | 0.562 | 0.507 | **0.500** | 0.507 | 0.525 | 0.471 | 0.491 | 0.463 | -0.001 [-0.003, +0.002] | -0.009 [-0.013, -0.004] |
| ridge 100 | 26,204 | 0.78 | 0.534 | 0.562 | 0.507 | **0.500** | 0.507 | 0.525 | 0.472 | 0.490 | 0.463 | -0.000 [-0.002, +0.002] | -0.009 [-0.013, -0.005] |

**Target set** (the rules see triads only; 'person+recip' adds the sign of a visible v -> u tie)

| target set | n test | test + | base | recent | strict | first-tie | person | person+recip | person+16 | person+recip+16 | (person+recip+16) - (person+recip) [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| first tie of the pair (primary) | 26,204 | 0.78 | 0.534 | 0.562 | 0.507 | 0.507 | 0.471 | 0.471 | 0.463 | 0.463 | -0.009 [-0.013, -0.004] |
| every new directed tie | 27,677 | 0.79 | 0.529 | 0.559 | 0.502 | 0.502 | 0.468 | 0.467 | 0.459 | 0.459 | -0.008 [-0.013, -0.004] |
| reciprocating ties only | 1,473 | 0.86 | 0.412 | 0.499 | 0.397 | 0.394 | 0.394 | 0.389 | 0.394 | 0.386 | -0.003 [-0.011, +0.007] |

**Context horizon** (wiki-RfA): election start (the network the voter walked into) against every earlier dated vote, including the same election's earlier votes (the herding setting; undated votes are not targets)

| variant | n test | test + | base | recent | strict | weak | first-tie | status | person | 16 types | person+16 | first-tie - strict [CI] | person+16 - person [CI] |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| election start (primary) | 26,204 | 0.78 | 0.534 | 0.562 | 0.507 | **0.500** | 0.507 | 0.525 | 0.471 | 0.491 | 0.463 | -0.001 [-0.003, +0.002] | -0.009 [-0.013, -0.004] |
| every earlier dated vote | 38,865 | 0.77 | 0.544 | 0.533 | 0.475 | **0.459** | 0.466 | 0.482 | 0.368 | 0.437 | 0.361 | -0.009 [-0.014, -0.004] | -0.007 [-0.009, -0.004] |

### 5.4 Which form of each rule fits best

Alternative forms of the same rules on the primary split (balance counted per pair or per directed instance; the first-tie rule on forward chains only, on forward chains with balance elsewhere [primary], on all forms, or by formation order; the person terms as counts or as two smoothed rates), sorted by held-out log-loss.

*Bitcoin OTC*

| model form (sorted by 70/30 log-loss) | 70/30 held-out log-loss [CI] | AUC | rolling-origin log-loss | own accuracy |
| :--- | ---: | ---: | ---: | ---: |
| weak balance | 0.264 [0.223, 0.304] | 0.922 | 0.259 | 0.916 |
| strict balance | 0.265 [0.225, 0.305] | 0.921 | 0.264 | 0.915 |
| strict (per instance) | 0.271 [0.231, 0.313] | 0.922 | 0.261 | 0.916 |
| weak (per instance) | 0.272 [0.231, 0.314] | 0.922 | 0.260 | 0.915 |
| saturated 16 types | 0.292 [0.246, 0.337] | 0.920 | 0.275 | - |
| conjunction | 0.299 [0.251, 0.346] | 0.913 | 0.278 | 0.910 |
| A^2 sign (FF only) | 0.311 [0.265, 0.359] | 0.913 | 0.295 | 0.892 |
| first-tie, time-first | 0.330 [0.278, 0.378] | 0.894 | 0.311 | 0.893 |
| person (rate form) | 0.336 [0.290, 0.379] | 0.904 | 0.304 | - |
| person propensity | 0.355 [0.295, 0.421] | 0.918 | 0.293 | - |
| first-tie asymmetric | 0.407 [0.336, 0.484] | 0.855 | 0.362 | 0.839 |
| copy incoming | 0.522 [0.426, 0.620] | 0.781 | 0.456 | 0.803 |
| first-tie, all forms | 0.531 [0.440, 0.627] | 0.765 | 0.462 | 0.789 |
| status | 0.560 [0.479, 0.640] | 0.796 | 0.489 | 0.705 |
| first-tie, FF only | 0.571 [0.475, 0.672] | 0.715 | 0.503 | 0.781 |
| base rate | 0.657 [0.565, 0.746] | - | 0.588 | - |

**Best-fitting rule form: weak balance** (0.264); the runner-up, strict balance (0.265), is behind by +0.002 [-0.001, +0.005]. Under the rolling origin the best rule form is weak balance (0.259). Best of all forms listed, the person terms included: **weak balance** (0.264). The first-tie rule's own forms, best to worst: first-tie, time-first 0.330, first-tie asymmetric 0.407, first-tie, all forms 0.531, first-tie, FF only 0.571.

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| first-tie asymmetric - strict (per instance) | +0.136 [+0.070, +0.210] | <= 0.0025 |
| strict (per instance) - strict balance | +0.006 [-0.003, +0.014] | 0.185 |
| weak (per instance) - weak balance | +0.008 [-0.000, +0.016] | 0.055 |
| first-tie, FF only - first-tie asymmetric | +0.164 [+0.119, +0.214] | <= 0.0025 |
| first-tie, all forms - first-tie asymmetric | +0.123 [+0.083, +0.169] | <= 0.0025 |
| first-tie, time-first - first-tie asymmetric | -0.078 [-0.153, -0.018] | 0.020 |
| copy incoming - first-tie asymmetric | +0.115 [+0.078, +0.152] | <= 0.0025 |
| conjunction - weak balance | +0.035 [+0.021, +0.048] | <= 0.0025 |
| person (rate form) - person propensity | -0.019 [-0.072, +0.030] | 0.465 |
| A^2 sign (FF only) - strict (per instance) | +0.040 [+0.019, +0.060] | <= 0.0025 |
| A^2 sign (FF only) - strict balance | +0.046 [+0.025, +0.067] | <= 0.0025 |

*Bitcoin Alpha*

| model form (sorted by 70/30 log-loss) | 70/30 held-out log-loss [CI] | AUC | rolling-origin log-loss | own accuracy |
| :--- | ---: | ---: | ---: | ---: |
| person propensity | 0.244 [0.203, 0.296] | 0.895 | 0.214 | - |
| weak (per instance) | 0.303 [0.212, 0.426] | 0.786 | 0.279 | 0.903 |
| strict (per instance) | 0.303 [0.213, 0.426] | 0.786 | 0.279 | 0.903 |
| weak balance | 0.306 [0.219, 0.422] | 0.777 | 0.277 | 0.903 |
| strict balance | 0.307 [0.220, 0.423] | 0.777 | 0.277 | 0.902 |
| first-tie asymmetric | 0.307 [0.213, 0.439] | 0.781 | 0.285 | 0.904 |
| person (rate form) | 0.311 [0.228, 0.410] | 0.828 | 0.281 | - |
| conjunction | 0.311 [0.218, 0.435] | 0.778 | 0.285 | 0.901 |
| A^2 sign (FF only) | 0.312 [0.223, 0.427] | 0.786 | 0.283 | 0.901 |
| saturated 16 types | 0.312 [0.219, 0.433] | 0.778 | 0.276 | - |
| copy incoming | 0.328 [0.222, 0.479] | 0.725 | 0.296 | 0.907 |
| first-tie, FF only | 0.340 [0.236, 0.479] | 0.717 | 0.310 | 0.901 |
| first-tie, time-first | 0.342 [0.248, 0.459] | 0.737 | 0.308 | 0.892 |
| first-tie, all forms | 0.343 [0.236, 0.493] | 0.711 | 0.314 | 0.898 |
| status | 0.394 [0.288, 0.516] | 0.664 | 0.356 | 0.701 |
| base rate | 0.406 [0.302, 0.529] | - | 0.382 | - |

**Best-fitting rule form: weak (per instance)** (0.303); the runner-up, strict (per instance) (0.303), is behind by +0.001 [-0.000, +0.001]. Under the rolling origin the best rule form is weak balance (0.277). Best of all forms listed, the person terms included: **person propensity** (0.244). The first-tie rule's own forms, best to worst: first-tie asymmetric 0.307, first-tie, FF only 0.340, first-tie, time-first 0.342, first-tie, all forms 0.343.

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| first-tie asymmetric - strict (per instance) | +0.004 [-0.004, +0.014] | 0.420 |
| strict (per instance) - strict balance | -0.004 [-0.013, +0.006] | 0.430 |
| weak (per instance) - weak balance | -0.003 [-0.012, +0.006] | 0.460 |
| first-tie, FF only - first-tie asymmetric | +0.033 [+0.012, +0.054] | 0.010 |
| first-tie, all forms - first-tie asymmetric | +0.036 [+0.014, +0.061] | <= 0.0025 |
| first-tie, time-first - first-tie asymmetric | +0.035 [+0.012, +0.055] | <= 0.0025 |
| copy incoming - first-tie asymmetric | +0.021 [-0.003, +0.048] | 0.090 |
| conjunction - weak balance | +0.005 [-0.007, +0.016] | 0.410 |
| person (rate form) - person propensity | +0.067 [+0.022, +0.129] | <= 0.0025 |
| A^2 sign (FF only) - strict (per instance) | +0.008 [-0.005, +0.023] | 0.265 |
| A^2 sign (FF only) - strict balance | +0.005 [-0.009, +0.021] | 0.610 |

*wiki-RfA*

| model form (sorted by 70/30 log-loss) | 70/30 held-out log-loss [CI] | AUC | rolling-origin log-loss | own accuracy |
| :--- | ---: | ---: | ---: | ---: |
| person propensity | 0.471 [0.444, 0.500] | 0.715 | 0.457 | - |
| person (rate form) | 0.474 [0.447, 0.502] | 0.712 | 0.463 | - |
| saturated 16 types | 0.491 [0.462, 0.523] | 0.685 | 0.476 | - |
| conjunction | 0.496 [0.466, 0.529] | 0.668 | 0.482 | 0.728 |
| weak (per instance) | 0.500 [0.470, 0.534] | 0.659 | 0.485 | 0.743 |
| weak balance | 0.500 [0.470, 0.534] | 0.659 | 0.485 | 0.744 |
| first-tie asymmetric | 0.507 [0.476, 0.541] | 0.640 | 0.492 | 0.749 |
| strict (per instance) | 0.507 [0.477, 0.541] | 0.640 | 0.492 | 0.745 |
| strict balance | 0.507 [0.477, 0.541] | 0.640 | 0.492 | 0.746 |
| first-tie, time-first | 0.511 [0.481, 0.544] | 0.629 | 0.496 | 0.761 |
| first-tie, all forms | 0.524 [0.492, 0.557] | 0.581 | 0.508 | 0.745 |
| status | 0.525 [0.492, 0.560] | 0.587 | 0.511 | 0.641 |
| copy incoming | 0.533 [0.501, 0.566] | 0.524 | 0.516 | 0.752 |
| first-tie, FF only | 0.534 [0.502, 0.567] | 0.532 | 0.517 | 0.753 |
| A^2 sign (FF only) | 0.534 [0.501, 0.567] | 0.519 | 0.516 | 0.749 |
| base rate | 0.534 [0.502, 0.567] | - | 0.519 | - |

**Best-fitting rule form: conjunction** (0.496); the runner-up, weak (per instance) (0.500), is behind by +0.004 [+0.002, +0.006]. Under the rolling origin the best rule form is conjunction (0.482). Best of all forms listed, the person terms included: **person propensity** (0.471). The first-tie rule's own forms, best to worst: first-tie asymmetric 0.507, first-tie, time-first 0.511, first-tie, all forms 0.524, first-tie, FF only 0.534.

| paired contrast (log-loss; negative = first is better) | difference [95% CI] | bootstrap p |
| :--- | ---: | ---: |
| first-tie asymmetric - strict (per instance) | -0.000 [-0.002, +0.001] | 0.640 |
| strict (per instance) - strict balance | -0.000 [-0.001, +0.000] | 0.590 |
| weak (per instance) - weak balance | -0.000 [-0.001, +0.001] | 0.595 |
| first-tie, FF only - first-tie asymmetric | +0.027 [+0.020, +0.032] | <= 0.0025 |
| first-tie, all forms - first-tie asymmetric | +0.017 [+0.011, +0.022] | <= 0.0025 |
| first-tie, time-first - first-tie asymmetric | +0.004 [-0.001, +0.009] | 0.080 |
| copy incoming - first-tie asymmetric | +0.026 [+0.020, +0.032] | <= 0.0025 |
| conjunction - weak balance | -0.004 [-0.007, -0.002] | <= 0.0025 |
| person (rate form) - person propensity | +0.003 [-0.005, +0.011] | 0.400 |
| A^2 sign (FF only) - strict (per instance) | +0.026 [+0.020, +0.031] | <= 0.0025 |
| A^2 sign (FF only) - strict balance | +0.026 [+0.020, +0.032] | <= 0.0025 |

### 5.5 Which variant wins, in counts

Over the distinct configurations of the variation tables of section 5.1-5.3 (embeddedness, sign recode, time design, ridge, wiki-RfA horizon; the target-set rows have a different model list and are left out), how often each canonical single rule has the lowest held-out log-loss, which model is best overall, and how often the paired 95% interval puts one model below the other ('better' = the first named model has the lower log-loss with the interval wholly below zero). The pre-specified configuration is the reference row of the recode, split, ridge and (wiki-RfA) horizon tables as well as 'k >= 1'; it is counted once, so a site has 16 (Bitcoin OTC), 16 (Bitcoin Alpha), 17 (wiki-RfA) distinct configurations.

| site | distinct configurations | best single rule (count) | best model overall (count) | first-tie vs strict: better / tied / worse | strict vs person: better / tied / worse | person+16 vs person: better / tied / worse |
| :--- | ---: | :--- | :--- | ---: | ---: | ---: |
| Bitcoin OTC | 16 | weak 14, strict 1, first-tie 1 | person + strict 11, weak balance 4, person + first-tie 1 | 0 / 2 / 14 | 10 / 6 / 0 | 14 / 2 / 0 |
| Bitcoin Alpha | 16 | weak 10, first-tie 6 | person + 16 types 8, person + first-tie 4, person + strict 3, weak balance 1 | 1 / 14 / 1 | 0 / 9 / 7 | 7 / 9 / 0 |
| wiki-RfA | 17 | weak 17 | person + 16 types 15, person + strict 1, person + first-tie 1 | 1 / 16 / 0 | 0 / 2 / 15 | 16 / 1 / 0 |

## 6. Reproduction of file 117's undirected closure counts

The formation-order counts of 117 section 3.4 [L4572-L4577] are reproduced from the same files by an independent code path (first rating per unordered pair, triangles of mutually rated pairs, edges ordered by time). OTC: 21,492 pairs, 33,493 triangles, starts (+,+) 26,964 / (+,-) 5,500 / (-,-) 1,029, closing positive 24,875 / 1,265 / 790, product rule 29,900 (89.3%); all identical to 117. Alpha: 14,124 pairs, 22,153 triangles, 20,016 with three distinct times of which 17,567 follow the product rule (87.8%), identical to 117; the three start classes (19,815, 1,856, 482) differ from 117's (19,814, 1,855, 484) by one or two triangles because ties between equal timestamps are broken arbitrarily (by file order here), as 117 says of its own run.

## 7. Caveats

- Three data sets, two kinds of medium (trading-forum ratings and public votes), 2003-2016: this is a test of whether a rule found on one fraternity's 1956 rankings transfers to online rating and voting sites, not a test of the rules in a group of about 17 people.
- The signs are ratings (Bitcoin, after a trade) and public votes (wiki-RfA, strategic and consequential), not liking. A negative Bitcoin rating is often a fraud report. Nothing here bridges these to Newcomb's rank recode (v0.2 section 0.6, rule 7).
- Alpha's timestamps are whole days, so 'earlier' means an earlier day; within-day order, and every same-day context, is lost. OTC's are unique and sub-second.
- Only embedded closing ties are scored: 25% of OTC's ratings, 33% of Alpha's and 43% of wiki-RfA's non-neutral votes. The results are about ties that close a triad.
- Person propensity is estimated from the same site's earlier ties; for a wiki-RfA candidate on a first candidacy there is no earlier in-vote, so the receiver half of the baseline is empty there (election-start horizon). The vote-level horizon variation shows what the same election's earlier votes add.
- No correction is made for the many comparisons: section 3 alone has 27 paired contrasts per site, and sections 4 and 5 add more; all but the pre-specified ones are descriptive. Of the 39 pre-specified contrasts (13 per site: each rule and the person terms against the base rate, each rule against the person terms, the first-tie rule against strict, weak and status, the 16 types added to the person terms), those with p between the Bonferroni threshold 0.0013 and 0.05 are: Bitcoin Alpha strict balance - person propensity +0.063 [+0.006, +0.150], p 0.015 (rolling origin +0.063 [+0.024, +0.120], p <0.001); Bitcoin Alpha weak balance - person propensity +0.062 [+0.005, +0.150], p 0.019 (rolling origin +0.063 [+0.023, +0.120], p <0.001); Bitcoin Alpha first-tie asymmetric - person propensity +0.063 [+0.001, +0.166], p 0.038 (rolling origin +0.071 [+0.028, +0.137], p <0.001). The static criterion is one pre-specified cell (DLL) on three sites: wiki-RfA's z +2.5 (two-sided p 0.014) passes a correction for three sites (0.017) and does not pass one over the four coupled cells of three sites (0.004).
- wiki-RfA elections are reconstructed from the file's block order and its dates (3,875 elections against 117's 3,926 (candidate, year, result) groups); 1,123 votes are dropped for ambiguous or stray dates.
- The rolling-origin pooled AUC is not shown: it would mix predictions calibrated on different training periods.
- Rankings of variants (sections 5.4 and 5.5) are read off the same held-out period that scores them, so the best of many variants is optimistic by selection; differences smaller than the paired intervals are ties, not rankings, and no variant was chosen to produce a number elsewhere in this file.
- The person baseline is LHK's four signed degrees as log counts, a linear model; a stronger person model (latent sender and receiver effects, REV2-style) could absorb more of what the triad terms add. Its counts also grow through the test period (the context is online), which the frozen-snapshot variation removes.
- A null that fixes the sender's and the receiver's sign mix at once (a two-margin swap shuffle on the sender-by-receiver grid) was not implemented; the sender and receiver nulls each hold one margin and the person-adjusted coefficient approximates both.
- The static D&K comparison is shown with each closing tie counted once and with every triad counted; triads that share a closing tie are not independent, and the shuffles permute whole closing ties, so the z scores are relative to that structure and are large because there are thousands of ties, not because the effects are large.

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.triad_rule_comparison report      # a few minutes on a quiet machine, seeded
    ~/.local/bin/uv run pytest tests/test_triad_rule_comparison.py

`report --save-pickle PATH` keeps the computed numbers and `report --from-pickle PATH` re-renders the prose from them without recomputing (the numbers are seeded and identical on a rerun). A `## Review` section appended below is kept when the file is re-rendered.

## Review (2026-11-01)

*Independent review of this file, `sim/models/triad_rule_comparison.py` and `sim/tests/test_triad_rule_comparison.py`, against the data files, `docs/ledger.jsonl`, `models/00-v0.md` section 7 and `sim/data/README.md`. Everything above this section was regenerated by `report` after the fixes below.*

**Re-run and re-derivation.** Before any change, `report` reproduced the previous file byte for byte and `uv run pytest tests/test_triad_rule_comparison.py` passed (55 tests; 57 after the review, two added). The headline numbers were re-derived by an independent code path: my own sweep, features and ridge-logistic fit (scipy), with exact within-group permutation moments in place of Monte Carlo. Bitcoin was read raw; wiki-RfA went through the module's election builder only. Closing ties, train and test: 8,972, 5,172 and 3,800 (OTC); 7,875, 4,659 and 3,216 (Alpha); 78,254, 52,050 and 26,204 (wiki-RfA). Held-out log-loss of base rate, strict, weak and person: 0.657, 0.265, 0.264 and 0.355; 0.406, 0.307, 0.306 and 0.244; 0.534, 0.507, 0.500 and 0.471. All of these equal the tables. DLL's exact z against the sender null is -18.4, -5.5 and +2.5, and against the receiver null -23.2, -11.6 and -21.2; the Monte Carlo values are -19.1, -5.6, +2.5 and -23.4, -11.7, -21.3. OTC's -19.1 sits at the edge of five seeds' -18.1 to -19.1, so the static z scores are good to a few per cent, which changes no reading.

**Sound as built.** *Leakage:* none found.
- The sweep uses strict visibility (t_vis < cut), which the tests check by deletion and by flipping signs that are not yet visible.
- The wiki-RfA horizon cuts at election start and makes a vote visible at election end.
- Fits use training rows only. The split is by cut time over all targets, and each rolling-origin block is fitted on the past. RES is never a feature.

*Nulls:* implemented as described (the within-sender null mean equals the exact one). *Data:* used as their `sim/data/README.md` entries say.
- Only that README is tracked under `sim/data/`.
- No wiki-RfA user name occurs in the module, the test or this file. The three collisions are the prose words 'Status', 'Where' and 'here'.
- Comments are never read, and only aggregates are published.

*Ledger:* every cited id exists.

**Fixed (code, tests and this file; no rule, model, split, null or seed changed).**
1. *Counting.* Section 5.5 and the verdict counted the pre-specified configuration four times per Bitcoin site and five times on wiki-RfA. Besides being 'k >= 1', it is the reference row of the recode, split, ridge and horizon tables. "Weak best in 51 of 59 variation rows" is really 41 of 49 distinct configurations, and the 5.5 tallies changed with it.
2. *"The one variation row where the first-tie rule is ahead of strict balance by its interval"* (and "never ahead of balance, one herding variation aside"). There are two:
   - Alpha at ridge 100: -0.018 [-0.029, -0.009], and ahead of weak balance there too (0.328 against 0.344).
   - wiki-RfA's vote-level horizon.

   The list is now computed (`ft_ahead_rows`), and "never ahead" is scoped to the pre-specified split.
3. *"Also refuted on these data: status ...; the kinetic law (4.2a)".* Both carry signal, so "behind balance, with numbers" is what the numbers support.
   - Status beats the base rate on OTC (-0.097 [-0.141, -0.056]) and wiki-RfA, and adds to the person terms on OTC (-0.026 [-0.035, -0.017]).
   - The A^2 sign beats the base rate on OTC (-0.346) and Alpha (-0.094).
4. *(4.2e) "supported"* passed over the all-negative cell. On OTC, DDD is below its sender null in every variant (z -2.4 to -4.7), which is strict balance's direction. The text now says: LLD and LDL are depleted on all three sites, and the Davis half holds on Alpha and wiki-RfA only.
5. *(4.2d).* On Alpha the refutation rests on the whole-period null: the test period alone gives z -1.8, and the raw cells do show the asymmetry (mp - pm +0.44). wiki-RfA's reproduction is now called weak (z +2.5, two-sided p 0.014). "Zero once the person terms are in" became "indistinguishable from zero".
6. *Coefficient bootstrap.* Section 4.6's person-adjusted coefficients used 100 bootstrap refits, while the Method stated B = 2000. The ends of a 100-draw percentile interval are noisy: OTC's FFmm was [+0.73, +2.36] at 50 refits and [+0.90, +2.14] at 100.
   - The fix is 400 refits, with every B stated.
   - New intervals: OTC FFmm +1.36 [+0.76, +2.07]; Alpha FFmm +1.15 [+0.34, +2.16]; wiki-RfA FFmm -0.08 [-0.23, +0.07].
   - FFmp - FFpm: -0.19 [-0.84, +0.40], -0.47 [-1.31, +0.50] and +0.02 [-0.18, +0.22].
   - The balance term on wiki-RfA is +0.30 [+0.04, +0.59].

   No reading changes. These fits are in-sample descriptions, and now say so.
7. *The N2 permutation null is anti-conservative where the refit overfits.* Its mean gain is negative, so an addition with no held-out gain still beats it. On Alpha it gives p <= 0.01 to four additions whose paired intervals include zero. This is now flagged in 4.7 and the Method; the verdict never rested on it.
8. *Multiple comparisons.* The caveat now names the pre-specified contrasts that a Bonferroni correction for 39 would not pass: Alpha's three rule - person contrasts at the split (p 0.015 to 0.038), which the rolling origin repeats at p < 0.001. It also says that wiki-RfA's DLL passes a three-site correction but not one over the four cells of three sites.
9. *Wording and provenance.*
   - The sender null is the formation-ordered analogue of the Newcomb row-wise null, not "the Newcomb run's own null": D&K redraw every tie of a row (L4485), while here only the closing sign moves.
   - Alpha's stamps are whole days at 04:00 or 05:00 UTC, not "on the hour"; OTC's are sub-second, not "to the second".
   - Credit is added for Kumar et al. (2018), the second paper the SNAP pages ask users to cite, and for the Newcomb ranks. `sim/data/README.md` now lists this module among the Newcomb file's users.
   - Ledger ids are `id` fields, not line numbers (L0898 is line 1279).
   - 'Ties go to +' (L4817) is 106's recount convention, not LHK's.
   - L4799 is LHK's 23-feature model, of which 'saturated 16 types' is the triad half.
   - L4561 documents the comment licence, not the absence of terms.
   - L4562's "11,380 named voters" are all distinct names: 10,416 of them vote. The data README is corrected; the ledger line is left to its owner.
   - A p at the floor of a 400-draw bootstrap now prints as "<= 0.0025", not "0.002".
   - `report` now keeps this section when it re-renders the file (`keep_reviews`).

**Verdict after review.** The headline stands, narrower in three places.
- By section 7's own criterion, (4.2d) is refuted on OTC and (on the whole-period null) on Alpha. It reproduces weakly on wiki-RfA, where it behaves as reception: reversed under the receiver null, and indistinguishable from zero given the person terms.
- Weak balance is the best single rule at the pre-specified split, level with strict balance and, on Alpha, with the first-tie rule. The first-tie rule beats strict balance by its interval in 2 of 49 configurations, and neither is evidence for rivalry.
- The person terms dominate on Alpha and wiki-RfA, not on OTC.

The three narrowings:
- (4.2e)'s Davis half holds on Alpha and wiki-RfA, not on OTC.
- Status and the A^2 sign are behind balance, not refuted.
- Alpha's refutation of (4.2d) is a whole-period result.
