# Wiki-RfA and Bitcoin: the tie-conversion half of the v0.1 n = 3 test, on explicit-sign data

_Generated 2026-11-01 by `uv run python -m models.wikirfa_report report` (seed 20261101, 10,000 null draws). Code: `sim/models/wikirfa.py`, `sim/models/wikirfa_report.py`; checks: `sim/tests/test_wikirfa_conversion.py`. Ledger ids are the lines of `docs/ledger.jsonl` with source "117 §" (L4547-L4668, L4854, L4855). Results are computed statistics only: the SNAP files are local-use-only and are not redistributed (`sim/data/README.md`), and no vote text, comment or user name is read into a result._

**What was tested (v0.1 §7, n = 3; v0's hypothesis, not a source's).** In longitudinal signed triads the one-negative triangle must convert to a balanced triangle faster than the all-negative one, and "if conversion runs at the null rate, (4.2b)/(5.1) is refuted". The Newcomb run (`results/newcomb_n3.md`) left the conversion half undecided: 15 and 33 events, ranks recoded to signs, 17 men. Wikipedia's requests for adminship are the first explicit-sign file in which the same ordered pair is signed twice: a voter rates a candidate at a candidacy and again at a later candidacy of the same candidate, sometimes with the opposite sign [L4564]. Each third party in a triple is a user tied to both, and the triple is judged before and after the re-vote; the 16 directed triad types are those of Leskovec, Huttenlocher & Kleinberg (106 §1.2).

## Verdict

**In short.** Against the brief's own null (signs shuffled within voter, 10,000 draws) conversion moves triples toward weak balance 6.7 points more than chance, p <1e-4; but 4.3 to 6.4 of that is the 79% oppose-to-support direction mix. Holding the network and permuting who converts leaves 1.4 to 3.1 points (z +2.9 to +6.8); the part that only balance could produce is confined to triples where u and v rated the same third party, and the friend-of-a-friend chain shows none. The first-tie asymmetry is a property of the voter, not the triple. Bitcoin's closure figure reproduces and shrinks under reputation-preserving baselines. For v0.2 that is a weak, setting-specific agreement term, not a law.

- **Data and terms.** SNAP wiki-RfA (198,275 votes, 2003 to May 2013; West, Paskov, Leskovec & Potts 2014) and the Bitcoin OTC and Alpha rating files, fetched on 2026-11-01 from `snap.stanford.edu` into git-ignored `sim/data/`, sha256 recorded in `sim/data/README.md`. The pages state no terms and ask for citations; the wiki-RfA "License" link is the SNAP software BSD licence, and the comments are Wikipedia text (CC BY-SA), which the parser streams past and stores none of. Nothing stated forbids local research use of a public download, so the run went ahead; nothing is committed or redistributed.
- **Counts.** 198,275 records leave 184,182 non-neutral votes with a named voter, a placeable candidacy and another user as candidate (neutral 12,648, empty voter 1,661, self 103, unplaceable undated 467 dropped; the groups overlap), and 182,996 (voter, candidate, candidacy) votes after collapsing 1,186 repeats inside a candidacy: 4,047 candidacies of 3,497 candidates. **5,990 re-votes** (consecutive votes of one voter on one candidate at different candidacies, 1,563 voters); **1,201 conversions**: 951 oppose-to-support, 250 support-to-oppose, in 1,176 pairs, by 545 voters, on 272 candidates. 117's 677 reproduces exactly under its own rule (519 + 158: first vote per year, first against last) and is a lower bound. 1,192 conversions sit in at least one triple: 229,424 instances (re-vote, third party, orientation).
- **What a conversion is here.** 48.6% of re-votes after an oppose flip to support, 6.2% after a support flip to oppose; 665 of the 951 oppose-to-support conversions are a failed candidacy followed by a passed one. Most conversions are a candidate judged better the second time, not a tie settling after tension.
- **Against the brief's null, conversion moves triples toward weak balance far more than chance: 56.7% of the weak-balance changes are repairs against 50.0%, +6.7 points, p <1e-4 (10,000 draws, signs shuffled within voter).** But that null makes as many support-to-oppose as oppose-to-support conversions (891 against 890; observed 250 against 951), and in a mostly positive context the direction alone moves the share: holding the observed conversions and shuffling only context signs gives 55.4% (within voter), 54.3% (within voter and candidacy outcome), 56.4% (within candidacy: +0.3 points, p 0.102). **4.3 to 6.4 of the 6.7 points are the direction mix (the observed old and new signs).**
- **Holding the network and permuting who converts (Newcomb's conditional design, the dynamic test) leaves a small excess that halves under voter controls.** Repair share 56.7% against 53.6% for re-votes with the same new candidacy and old sign (+3.1 points, z +6.8, p <1e-4), 55.3% within the same voter and old sign (+1.4, z +2.9, p 0.002), 55.5% also within terciles of the voter's generosity (+1.2, z +3.2). Counting each conversion once: +4.1, +2.1, +2.1 points (z +12.4, +7.0, +7.8). A re-vote inside a one-negative triple flips at 31.4% against 27.9% / 30.0% / 29.6% (+3.5 / +1.5 / +1.8 points); inside a weakly balanced one it flips at its null (14.2%).
- **The excess is agreement on a third party, not a friend of a friend.** A double-difference contrast in which the voter's generosity and the candidate's reception cancel (a planted 20-point lift in the strictly unbalanced cells scores 0.4, an additive effect 0) is at its null in the chain u -> w -> v (FF: -0.003, z -0.4) and above it where u and v both rated the third party (FB: +0.052, z +4.9; within voter +0.067, z +5.5), less where the third party rated both (BF: +0.036, z +3.8; within voter z +1.7). The FF repair-share excess (+2.7 points) is the voter's own generosity: it vanishes within voter (+0.2).
- **v0's contrast, one-negative faster than all-negative, is not a robust finding.** The one-negative class flips above its null in every event-permutation null; the all-negative class does not (48.3% against 49.5%, z -1.2). The difference r1 - r3 exceeds its null by +4.7 points (z +5.0) with candidacy held, by +0.1 (z +0.1) within voter and +0.6 (z +0.8) with generosity held.
- **First-tie asymmetry (Q2): which tie is negative does predict the conversion, but as a property of the voter, not of the triple.** Where a positive tie turns negative (a join), the converting voter joins above null exactly when the lone negative tie touches him (DLL-FF, DLL-BF, LLD-FB: 11.4% against 7.6%, z +6.0) and not when it is the third party's tie to the candidate (LDL-FF, LDL-FB, LLD-BF: 7.0% against 6.9%, z +0.4); contrast +3.7 points over null (z +5.6) with the candidacy held, but -0.1 (z -0.1) with the voter held and +1.3 (z +2.7) within generosity terciles: a voter with a negative tie to someone is a voter who turns against candidates, whatever the triple. In D&K's terms the first-tie-negative form DLL joins at 11.8% against 7.7% and the second-tie-negative form LDL at its null (6.6% against 6.7%). Repairs (the converting tie is the lone negative one) are above null for all three forms, most for DLL, but the DLL - LDL gap is explained by voter generosity. The reactive first-tie form is the reverse of Newcomb's, where DLL was the stable one [L4508, L4511].
- **Bitcoin OTC and Alpha (formation only; no pair is rated twice).** 117's figure reproduces exactly: OTC 29,900 of 33,493 triangles balanced (89.3%) against 69.3% under the global sign shuffle; Alpha 17,567 of 20,016 strictly ordered (87.8%; 88.2% of all 22,153) against 79.1%. But the excess shrinks with a stricter baseline: within rater 72.7% (OTC) and 79.4% (Alpha); within ratee, i.e. holding each trader's reputation, 80.1% (OTC, still below the data) and 87.6% (Alpha, strictly ordered, where it reaches the data: p 0.376). Whether the all-negative triangle is enriched (117) or depleted also depends on the baseline (section 8).
- **For v0.2.** Tie conversion toward weak balance exceeds the null on wiki-RfA, but little: +1.4 to +3.1 points of repair share and +1.5 to +3.5 points of flip rate in one-negative triples once the network, the candidacy and the direction are held, against +6.7 under the brief's null, most of which is the 79% oppose-to-support mix. The part that only balance could produce (the interaction) is local to triples where u and v rated the same third party, so v0.2 can carry it as a weak, setting-specific agreement term with a fitted coefficient, not as a law, and the chain form of (4.2b) (friend of a friend) has no support from conversion. Caveats: **votes are not friendships** (a tie in a triple is a vote at some other candidacy); **a vote is a one-shot evaluation** of a candidacy, and most conversions are the candidate improving; **timing is by candidacy** (about a week), not by tie; **selection into re-voting** is severe (3.4% of pairs re-vote, almost all after a failed candidacy, 545 voters supply the conversions). Section 9.

## 1. Data, terms, cleaning

- **Source and terms [L4561, L4567].** `snap.stanford.edu/data/wiki-RfA.txt.gz` (14,936,383 bytes, sha256 `88d53196fb2564a2e20286dbba818832f718cc352bb181a2101d23d2556f0862`) and the two Bitcoin files (397,258 and 149,480 bytes); plain public downloads, no login or access control; `robots.txt` disallows only course-video directories. Neither page states terms; both ask for citations (West et al. 2014, TACL 2: 297-310; Kumar et al. 2016 and 2018). The wiki-RfA comments are Wikipedia text under CC BY-SA 4.0 / GFDL (117 §3.3), skipped unread at parse time and never stored; user names are replaced by integers on load and written nowhere. Absence of a stated licence is not a grant, so the files are used for local runs only (git-ignored, never committed) and only statistics are published.
- **The file reproduces 117's counts [L4562, L4563].** 198,275 records: 144,451 support, 41,176 oppose, 12,648 neutral; the per-year totals; 11,380 named users and 1,661 records with an empty voter. Found here: 9,367 records have no time, one has an impossible one (hour 31), three month names carry slips (`Mya`, `Julu`, `Janry`, read as May, July, January).
- **A finding in the file: 18 elections carry both outcome labels, 15 of them as a complete copy.** Grouping a candidate's votes by (candidate, result) as 117's 3,926 elections do would make the copy a second candidacy and its votes 618 re-votes with a zero-day gap. Candidacies here are a candidate's dated votes split at gaps of more than 14 days (the median span is 6.3 days); in 18 clusters both labels occur (15 exact ties, equal numbers of votes under each label and the outcome unknown; in the rest a few votes carry the other label), and 23 late or mis-dated stray signatures (37 votes) are folded into the nearest big candidacy. Undated votes join their candidacy by year; 467 cannot be placed and are dropped.
- **117's 677 [L4564, L4855].** Under its rule (ordered pairs with a named voter, the first vote of the pair in each file year, the first and last non-neutral of those): 3,761 pairs vote in more than one year, 7,793 pairs carry more than one vote (16,330 votes), and 519 oppose-to-support plus 158 support-to-oppose changes = **677**, exactly. Its two non-changing cells do not reproduce: 1,971 support-to-support and 632 oppose-to-oppose here, against 1,946 and 647 in 117 (not resolved; they do not enter this analysis). Counting every sign change between consecutive candidacies gives **1,201**.

## 2. The conversions: direction, timing, selection, and the 16 types

| re-votes | n | converted | rate | median days between the two votes, conversions |
| :--- | ---: | ---: | ---: | ---: |
| after an oppose (old sign -) | 1,957 | 951 | 48.6% | 144 |
| after a support (old sign +) | 4,033 | 250 | 6.2% | 215 |
| all re-votes | 5,990 | 1,201 | 20.1% | 155 |

Median gap for re-votes that did not convert: 142 days; 87% of conversions fall within a year of the earlier vote; the clock is minutes in the file but a candidacy lasts about a week, so "before" means before the candidacy began. Outcomes of the two candidacies, (earlier, later) = (failed, passed) / (failed, failed) / (passed, failed) / (passed, passed): all re-votes 3,270 / 2,414 / 110 / 166; oppose-to-support conversions 665 / 281 / 4 / 1; support-to-oppose 40 / 157 / 34 / 18 (30 re-votes involve one of the 15 candidacies of unknown outcome). Re-votes are 3% of the 177,006 voter-candidate pairs and come mostly from candidates who failed (a re-run after a pass is rare): **selection into re-voting is the selection of failed-then-re-run candidates and of the voters who turn up twice**. The conversions are concentrated but not dominated: 545 converting voters (at most 25 conversions each; the ten largest hold 15%), 272 candidates. Conversions / re-votes by year of the later vote: 2004: 10/62, 2005: 54/315, 2006: 186/1016, 2007: 212/1133, 2008: 252/1200, 2009: 242/1117, 2010: 145/711, 2011: 71/289, 2012: 15/71, 2013: 14/76. Candidacy of the converting vote, second / third / fourth / fifth of its candidate: 768 / 242 / 97 / 68 conversions out of 3,626 / 1,319 / 504 / 342 re-votes.

**The 16 directed triad types [106 §1.2] over all instances.** F = the u-w tie runs u to w (first letter) or the w-v tie runs w to v (second letter), B = the reverse; p / m = the sign of the u-w tie then the w-v tie. "Expected" is the mean of the 10,000 draws of the Newcomb-style null (conversions permuted within the same new candidacy and old sign). Balance predicts the converting tie's sign on all 16 types, status on 8 [106 §1.2].

| type | instances | from - | -> + (expected) | rate | from + | + -> - (expected) | rate | balance | status |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| FFpp | 37,710 | 7,757 | 4,520 (4,003) | 58% | 29,953 | 2,106 (2,214) | 7% | + | + |
| FFpm | 18,266 | 5,615 | 3,089 (2,822) | 55% | 12,651 | 833 (841) | 7% | - | none |
| FFmp | 6,530 | 3,026 | 1,262 (1,392) | 42% | 3,504 | 409 (266) | 12% | - | none |
| FFmm | 3,258 | 1,492 | 578 (688) | 39% | 1,766 | 204 (132) | 12% | + | - |
| FBpp | 64,632 | 15,449 | 9,720 (8,557) | 63% | 49,183 | 2,664 (2,948) | 5% | + | none |
| FBpm | 7,862 | 1,929 | 1,014 (938) | 53% | 5,933 | 385 (399) | 6% | - | + |
| FBmp | 9,201 | 4,643 | 1,922 (2,152) | 41% | 4,558 | 492 (335) | 11% | - | - |
| FBmm | 5,832 | 2,254 | 1,206 (1,194) | 54% | 3,578 | 273 (245) | 8% | + | none |
| BFpp | 36,607 | 8,310 | 4,567 (4,211) | 55% | 28,297 | 2,200 (2,126) | 8% | + | none |
| BFpm | 14,877 | 5,078 | 2,615 (2,441) | 51% | 9,799 | 768 (706) | 8% | - | - |
| BFmp | 3,834 | 952 | 451 (477) | 47% | 2,882 | 345 (226) | 12% | - | + |
| BFmm | 5,033 | 1,256 | 634 (594) | 50% | 3,777 | 344 (268) | 9% | + | none |
| BBpp | 12,238 | 3,300 | 1,852 (1,671) | 56% | 8,938 | 610 (569) | 7% | + | - |
| BBpm | 1,888 | 518 | 257 (244) | 50% | 1,370 | 73 (92) | 5% | - | none |
| BBmp | 1,356 | 344 | 163 (160) | 47% | 1,012 | 97 (69) | 10% | - | none |
| BBmm | 300 | 73 | 33 (36) | 45% | 227 | 28 (17) | 12% | + | + |

Reading. The rate of oppose-to-support conversion follows the sign of the u-w tie whatever the w-v tie is (FF: 58% and 55% when u -> w is positive, 42% and 39% when it is negative): the voter's own generosity, which is not balance. The product structure that balance needs shows only where u and v rated the same third party (FB): from an oppose, conversion is 63% when both ratings are positive, 54% when both are negative, 53% and 41% when they disagree.

## 3. Do conversions move triples toward weak balance more than the null? (H1)

**Statistic.** Over converting instances, FIX = a one-negative triple becomes balanced, BREAK = a weakly balanced one becomes one-negative; the share FIX / (FIX + BREAK) is 56.73% (24,061 against 18,353); strict balance 58.00%; the event-level mean (each of 1,189 conversions weighs one) 55.54%. Flipping any tie of a one-negative triple makes it balanced, so FIX is exactly "the triple was one-negative". Instances share ties, so the permutation nulls, not a binomial, carry the inference; p = (1 + #{null >= obs}) / (B + 1), one-sided.

**What the nulls hold.** (1) *The brief:* every voter's non-neutral signs shuffled over his votes, targets and times kept, conversions re-determined. (2) *Context shuffles (conversions held):* the observed old and new sign of every re-vote is kept and only the signs of the context ties are shuffled, within voter, within voter and candidacy outcome, or within candidacy. They compare the converters' triples with random triples, so they are blind to the static depletion of one-negative triples (the (a) half of the test; table below). (3) *Event permutations (network held, Newcomb's conditional design):* contexts and old signs stay as observed and the conversion indicator is permuted among the re-votes of a stratum, so every pre-state class size is fixed and only *who converts* is random: same new candidacy and old sign (candidate-level consensus and direction held); same old and new candidacy; same voter and old sign (voter propensity held); and the first with terciles of the number of triples or of the voter's share of positive votes added. Group (3) is the dynamic test (it holds the pre-state, as Newcomb's conditional null held the start wave); group (2) compares the converters' triples with random ones. **(3) was added after (2)'s rows disagreed with each other and the brief's; that is post hoc and is why both are shown.**

| null | what it holds | share null | excess (pp) | z | p | event-level null | excess (pp) | z | p |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| voter_uncond | the brief: signs shuffled within voter, conversions re-determined | 50.0% | +6.7 | +12.8 | <1e-4 | 50.0% | +5.5 | +11.3 | <1e-4 |
| ctx_voter | conversions held; context signs shuffled within voter | 55.4% | +1.3 | +4.9 | <1e-4 | 56.3% | -0.7 | -1.6 | 0.953 |
| ctx_voter_res | conversions held; context signs shuffled within voter and candidacy outcome | 54.3% | +2.4 | +10.1 | <1e-4 | 53.5% | +2.0 | +4.9 | <1e-4 |
| ctx_candidacy | conversions held; context signs shuffled within candidacy | 56.4% | +0.3 | +1.3 | 0.102 | 55.3% | +0.3 | +0.7 | 0.248 |
| ev_cur_old | contexts held; who converts permuted within the same new candidacy and old sign | 53.6% | +3.1 | +6.8 | <1e-4 | 51.5% | +4.1 | +12.4 | <1e-4 |
| ev_pair_old | contexts held; permuted within the same old and new candidacy and old sign | 53.7% | +3.1 | +7.4 | <1e-4 | 51.6% | +4.0 | +12.4 | <1e-4 |
| ev_voter_old | contexts held; permuted within the same voter and old sign | 55.3% | +1.4 | +2.9 | 0.002 | 53.4% | +2.1 | +7.0 | <1e-4 |
| ev_cur_old_deg | as ev_cur_old, and within terciles of the number of triples | 54.4% | +2.3 | +6.3 | <1e-4 | 52.8% | +2.7 | +9.7 | <1e-4 |
| ev_cur_old_pos | as ev_cur_old, and within terciles of the voter's share of positive votes | 55.5% | +1.2 | +3.2 | 6.0e-4 | 53.4% | +2.1 | +7.8 | <1e-4 |

Observed pooled share 56.7%, event-level 55.5%. Excess in percentage points; p one-sided upper tail. Number of conversions per draw in the brief's null: 1781 (890 oppose-to-support, 891 support-to-oppose); in every other null 1,201 (951 and 250).

**By direction** (share FIX / (FIX + BREAK) among oppose-to-support and among support-to-oppose conversions; the null mean, the excess in points and z):

| null | oppose -> support: obs vs null | excess | z | support -> oppose: obs vs null | excess | z |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| ctx_voter_res | 65.7% vs 59.9% | +5.8 | +18.3 | 31.0% vs 38.4% | -7.4 | -14.6 |
| ctx_candidacy | 65.7% vs 63.8% | +1.9 | +5.6 | 31.0% vs 35.2% | -4.3 | -8.1 |
| ev_cur_old | 65.7% vs 63.4% | +2.3 | +7.1 | 31.0% vs 27.2% | +3.8 | +5.2 |
| ev_voter_old | 65.7% vs 64.1% | +1.6 | +5.4 | 31.0% vs 29.9% | +1.1 | +1.3 |
| ev_cur_old_pos | 65.7% vs 64.9% | +0.9 | +3.7 | 31.0% vs 29.1% | +1.8 | +3.0 |

The two directions part under the context shuffles (support-to-oppose conversions sit in *less* tension-resolving contexts than random ones) and agree under the event permutations (both above null). That is the signature of the static depletion: the real network has fewer one-negative triples than a shuffled one, so a random context is more often a repair than a real one, and a converter's real context can be below the random baseline and above its non-converting neighbours at once.

**Static depletion, for reference (the (a) half; instances by pre-state class, observed against the context shuffles).**

| pre-state class | observed | ctx_voter | ctx_voter_res | ctx_candidacy |
| :--- | ---: | ---: | ---: | ---: |
| no negative | 116,371 | 106,416 (+9%) | 98,930 (+18%) | 105,848 (+10%) |
| one-negative | 76,525 | 86,898 (-12%) | 87,879 (-13%) | 87,164 (-12%) |
| two-negative | 31,453 | 31,599 (-0%) | 35,828 (-12%) | 31,709 (-1%) |
| all-negative | 5,075 | 4,510 (+13%) | 6,787 (-25%) | 4,703 (+8%) |

## 4. Hazard by pre-state class (H2): v0's "one-negative faster than all-negative"

The class is the number of negative ties among (u-w, w-v, old u-v): 0, 1, 2, 3. Class sizes (instances) 116,371 / 76,525 / 31,453 / 5,075; they are fixed under the event permutations, so the rate of conversion in a class is comparable with its null (under the brief's null the sizes move and the rates are not comparable; not shown). Cells show observed vs null (excess in points, z, upper-tail p). A re-vote flips more easily from an oppose than from a support, so class 3 (which needs an old oppose) converts more than class 0 in every null; the question is the excess over the null.

| null | one-negative (r1) | weakly balanced (0, 2, 3) | all-negative (r3) | r1 - balanced | r1 - r3 |
| :--- | ---: | ---: | ---: | ---: | ---: |
| ev_cur_old | 31.4% vs 27.9% (+3.5, z +8.5, p <1e-4) | 14.2% vs 14.2% (-0.0, z -0.0, p 0.499) | 48.3% vs 49.5% (-1.2, z -1.2, p 0.889) | 17.3% vs 13.8% (+3.5, z +9.7, p <1e-4) | -16.9% vs -21.5% (+4.7, z +5.0, p <1e-4) |
| ev_pair_old | 31.4% vs 28.2% (+3.3, z +8.3, p <1e-4) | 14.2% vs 14.3% (-0.1, z -0.4, p 0.662) | 48.3% vs 49.6% (-1.3, z -1.3, p 0.904) | 17.3% vs 13.9% (+3.4, z +10.0, p <1e-4) | -16.9% vs -21.4% (+4.5, z +4.9, p <1e-4) |
| ev_voter_old | 31.4% vs 30.0% (+1.5, z +3.1, p 0.001) | 14.2% vs 14.2% (-0.1, z -0.3, p 0.597) | 48.3% vs 46.9% (+1.4, z +1.3, p 0.095) | 17.3% vs 15.8% (+1.5, z +3.7, p <1e-4) | -16.9% vs -16.9% (+0.1, z +0.1, p 0.480) |
| ev_cur_old_deg | 31.4% vs 29.8% (+1.6, z +6.3, p <1e-4) | 14.2% vs 14.6% (-0.5, z -2.5, p 0.996) | 48.3% vs 51.5% (-3.2, z -4.4, p 1.000) | 17.3% vs 15.2% (+2.1, z +7.7, p <1e-4) | -16.9% vs -21.7% (+4.9, z +6.3, p <1e-4) |
| ev_cur_old_pos | 31.4% vs 29.6% (+1.8, z +5.2, p <1e-4) | 14.2% vs 13.9% (+0.2, z +0.9, p 0.180) | 48.3% vs 47.0% (+1.3, z +1.6, p 0.060) | 17.3% vs 15.7% (+1.6, z +5.4, p <1e-4) | -16.9% vs -17.4% (+0.6, z +0.8, p 0.219) |

One-negative triples flip above their null in every row; weakly balanced triples are at theirs (the largest departure is -0.5 points); the all-negative class never flips significantly faster than its null (excess between -3.2 and +1.4 points). v0's contrast holds against the null difference only where the voter is not held fixed. The prediction that conversion is *at the null rate* if balance does not operate is not what is seen: the one-negative rate is above it.

## 5. Where the excess sits: the balance-specific interaction

The repair share mixes balance with two additive effects that are not balance: the voter's generosity (u's tie to w is positive, so u is positive toward v too) and the candidate's reception (w supports v, so u is drawn to). Strict balance predicts a *product*: the effect of the w-v sign should reverse with the u-w sign. Within each orientation and old sign the conversion rate of the four context cells (pp, pm, mp, mm) gives D = sgn(old)(r_pp + r_mm - r_pm - r_mp), which cancels both additive effects and is positive when conversion is higher exactly where the product of the three signs is negative (a planted full balance rule gives D = 0.4, a planted additive effect 0, `test_interaction_contrast_...`). I is the precision-weighted mean of the eight blocks. The nulls centre above zero because strata with higher conversion rates hold a different mix of context cells; the comparison is the excess over the null.

| null | I (all) | FF: u->w->v | FB: u->w<-v | BF: u<-w->v | BB: cycle |
| :--- | ---: | ---: | ---: | ---: | ---: |
| voter_uncond | +0.050 vs +0.003 (z +8.0) | -0.001 vs +0.001 (z -0.2) | +0.107 vs +0.005 (z +9.2) | +0.039 vs +0.003 (z +3.9) | -0.021 vs +0.000 (z -1.1) |
| ctx_candidacy | +0.050 vs +0.010 (z +9.3) | -0.001 vs +0.002 (z -0.3) | +0.107 vs +0.022 (z +12.6) | +0.039 vs +0.003 (z +4.3) | -0.021 vs -0.005 (z -0.8) |
| ev_cur_old | +0.050 vs +0.023 (z +4.9) | -0.001 vs +0.002 (z -0.4) | +0.107 vs +0.056 (z +4.9) | +0.039 vs +0.003 (z +3.8) | -0.021 vs +0.013 (z -1.6) |
| ev_voter_old | +0.050 vs +0.023 (z +4.6) | -0.001 vs +0.006 (z -0.8) | +0.107 vs +0.041 (z +5.5) | +0.039 vs +0.024 (z +1.7) | -0.021 vs -0.020 (z -0.1) |
| ev_cur_old_pos | +0.050 vs +0.033 (z +3.8) | -0.001 vs +0.008 (z -1.4) | +0.107 vs +0.067 (z +4.8) | +0.039 vs +0.017 (z +2.6) | -0.021 vs +0.008 (z -1.5) |

FF is at its null in every row: no transitivity (friend of a friend) in the conversions. FB (u and v both rated w) carries it, BF (w rated both) a smaller part, BB (a directed cycle, few instances) nothing. On the contrast's scale an excess of 0.028 means conversion is about 1.4 points higher in the two strictly unbalanced context cells than in the two balanced ones, beyond the additive baseline (FB: 2.6; within voter, all orientations 1.4 and FB 3.3). That is also what homophily of judgement predicts (u and v voted alike on w), and the data cannot separate the two: the sign law's similarity-as-attraction generator and balance coincide on this triple.

## 6. The first-tie asymmetry (Q2)

D&K's types name the signs of an ordered triple i->j, j->k, i->k (L = +, D = -). With u -> v the converting tie, the orientation fixes where it sits: FF is (u->w, w->v, u->v), so the converting tie is **third**; FB is (u->v, v->w, u->w), **first**; BF is (w->u, u->v, w->v), **second**; BB is a cycle and has no D&K type. For a one-negative triple the lone negative tie is first (DLL), second (LDL) or third (LLD). Either the converting tie is that negative tie (a **repair**: oppose to support; the diagonal cells FF-LLD, FB-DLL, BF-LDL) or a positive tie turns negative (a **join**: the other six). Cells give the conversion rate (conversions / re-vote instances) against the null mean of the same-new-candidacy event permutation, with z.

| type | FF (converting tie third) | FB (first) | BF (second) |
| :--- | ---: | ---: | ---: |
| **LLD** (third tie negative) | 4,520/7,757 = 58.3% (repair); null 51.6%, z +6.8 | 492/4,558 = 10.8%; null 7.3%, z +3.6 | 768/9,799 = 7.8%; null 7.2%, z +1.2 |
| **LDL** (second tie negative) | 833/12,651 = 6.6%; null 6.6%, z -0.1 | 385/5,933 = 6.5%; null 6.7%, z -0.4 | 4,567/8,310 = 55.0% (repair); null 50.7%, z +3.2 |
| **DLL** (first tie negative) | 409/3,504 = 11.7%; null 7.6%, z +5.9 | 9,720/15,449 = 62.9% (repair); null 55.4%, z +7.7 | 345/2,882 = 12.0%; null 7.8%, z +3.7 |

Contrasts, by kind of conversion. The repair rate of a type is its diagonal cell; the join rate pools its two off-diagonal cells.

|  | observed | null: same new candidacy | null: same voter | null: + voter generosity |
| :--- | ---: | ---: | ---: | ---: |
| repair, DLL | 62.9% | 55.4% (+7.5, z +7.7, p <1e-4) | 58.9% (+4.1, z +2.8, p 0.002) | 59.5% (+3.4, z +4.2, p <1e-4) |
| repair, LDL | 55.0% | 50.7% (+4.3, z +3.2, p 8.0e-4) | 54.0% (+1.0, z +0.9, p 0.194) | 51.6% (+3.3, z +2.9, p 0.002) |
| repair, LLD | 58.3% | 51.6% (+6.7, z +6.8, p <1e-4) | 56.8% (+1.4, z +1.5, p 0.074) | 55.5% (+2.8, z +3.4, p 6.0e-4) |
| **repair: DLL - LDL** | 8.0% | 4.7% (+3.2, z +2.2, p 0.015) | 4.9% (+3.1, z +1.8, p 0.034) | 7.9% (+0.1, z +0.0, p 0.488) |
| repair: DLL - (LLD, LDL) | 6.4% | 4.3% (+2.1, z +1.9, p 0.026) | 3.5% (+2.9, z +1.8, p 0.033) | 6.0% (+0.3, z +0.4, p 0.361) |
| join, DLL (first tie negative) | 11.8% | 7.7% (+4.1, z +6.2, p <1e-4) | 10.3% (+1.5, z +2.8, p 0.004) | 9.8% (+2.0, z +3.3, p 1.0e-3) |
| join, LDL (second) | 6.6% | 6.7% (-0.1, z -0.3, p 0.612) | 6.1% (+0.4, z +1.2, p 0.109) | 6.3% (+0.3, z +0.7, p 0.231) |
| join, LLD (third) | 8.8% | 7.2% (+1.5, z +3.1, p 0.003) | 8.6% (+0.2, z +0.4, p 0.321) | 8.1% (+0.7, z +1.7, p 0.045) |
| **join: DLL - LDL** | 5.3% | 1.0% (+4.2, z +5.8, p <1e-4) | 4.2% (+1.1, z +1.9, p 0.029) | 3.5% (+1.8, z +2.8, p 0.003) |
| join: DLL - (LLD, LDL) | 4.3% | 0.8% (+3.5, z +5.4, p <1e-4) | 3.1% (+1.2, z +2.1, p 0.017) | 2.7% (+1.6, z +2.7, p 0.005) |
| join, negative tie touches the voter (DLL-FF, DLL-BF, LLD-FB) | 11.4% | 7.6% (+3.8, z +6.0, p <1e-4) | 10.9% (+0.5, z +0.7, p 0.222) | 9.7% (+1.7, z +3.3, p 7.0e-4) |
| join, negative tie is w-v (LDL-FF, LDL-FB, LLD-BF) | 7.0% | 6.9% (+0.1, z +0.4, p 0.343) | 6.4% (+0.5, z +1.7, p 0.045) | 6.7% (+0.3, z +1.1, p 0.136) |
| **join: touches the voter - not** | 4.4% | 0.7% (+3.7, z +5.6, p <1e-4) | 4.4% (-0.1, z -0.1, p 0.493) | 3.1% (+1.3, z +2.7, p 0.004) |
| share of unbalanced conversions that are DLL | 47.5% | 46.3% (+1.2, z +2.4, p 0.007) | 46.4% (+1.1, z +1.7, p 0.042) | 47.3% (+0.2, z +0.5, p 0.321) |
| ... LDL | 26.2% | 27.9% (-1.6, z -3.2, p 1.000) | 26.8% (-0.5, z -1.2, p 0.884) | 26.3% (-0.1, z -0.2, p 0.568) |
| ... LLD | 26.2% | 25.8% (+0.4, z +1.1, p 0.135) | 26.8% (-0.6, z -1.5, p 0.931) | 26.3% (-0.1, z -0.4, p 0.668) |

Reading. **Joins.** Each of the three join cells whose lone negative tie touches the converting voter (DLL-FF: u -> w negative; DLL-BF: w -> u negative; LLD-FB: u -> w negative) is above its null, and the three whose negative tie is the third party's tie to the candidate (LDL-FF, LDL-FB: w -> v and v -> w; LLD-BF: w -> v) are at it: pooled 11.4% against 7.6% and 7.0% against 6.9%. D&K's "first tie" (position one) is a proxy for that incidence in the join cells, because the first tie of the ordered triple is one of u's ties whenever the converting tie is not the first. With the voter held fixed the incidence contrast is -0.1 points (z -0.1) and within generosity terciles +1.3 (z +2.7): so the asymmetry is the voter's own negativity (a voter who has a negative tie to a third party is a voter who turns against candidates), not a feature of the triple and not shown to be rivalry for the third party [L4511]. DLL minus LDL on its own is above its null in all three nulls (z +5.8, +1.9, +2.8) but is largely the incidence contrast under another name. **Repairs.** Repair rates are above null for all three forms and highest for DLL, but the DLL - LDL gap disappears once the voter's generosity is held. **Against Newcomb.** D&K found balance supported when the first tie is positive and contradicted when it is negative [L4508], and DLL over-represented and persistent; here the first-tie-negative form is the *more* reactive, in the direction balance asks for (the voter turns against a candidate whom a person the voter dislikes supports). The analyses do not measure the same thing: Newcomb's triple changes through any of three ties, mostly by losing one, and here only the voter's tie to the candidate is re-observed, so this neither confirms nor contradicts D&K.

## 7. Sensitivities (secondary; none replaces the headline)

Pooled repair share, event-level share, flip-rate excess in one-negative triples over weakly balanced ones, and the interaction contrast, each as observed / null mean (excess, z), under two event-permutation nulls: **A** same new candidacy and old sign, **B** same voter and old sign.

| cut | instances | A share | A event | A r1-bal | A I | B share | B event | B r1-bal | B I |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| main analysis | 229,424 | 0.567 / 0.536 (+3.1, +6.8) | 0.555 / 0.515 (+4.1, +12.4) | 0.173 / 0.138 (+3.5, +9.7) | 0.050 / 0.023 (+0.028, +4.9) | 0.567 / 0.553 (+1.4, +2.9) | 0.555 / 0.534 (+2.1, +7.0) | 0.173 / 0.158 (+1.5, +3.7) | 0.050 / 0.023 (+0.027, +4.6) |
| context cut-off at the vote, not the candidacy start | 259,232 | 0.597 / 0.568 (+2.9, +6.5) | 0.597 / 0.555 (+4.3, +13.5) | 0.206 / 0.169 (+3.7, +10.3) | 0.056 / 0.026 (+0.030, +5.8) | 0.597 / 0.574 (+2.3, +5.1) | 0.597 / 0.565 (+3.2, +11.8) | 0.206 / 0.180 (+2.6, +6.6) | 0.056 / 0.023 (+0.033, +6.0) |
| no co-voters of the old candidacy (w -> v tie not from the old candidacy) | 126,552 | 0.633 / 0.594 (+3.9, +6.1) | 0.645 / 0.592 (+5.3, +12.4) | 0.237 / 0.190 (+4.7, +9.0) | 0.080 / 0.041 (+0.039, +4.4) | 0.633 / 0.609 (+2.4, +3.0) | 0.645 / 0.622 (+2.3, +6.0) | 0.237 / 0.217 (+2.0, +3.2) | 0.080 / 0.036 (+0.044, +4.5) |
| contexts at most two years old | 212,957 | 0.573 / 0.542 (+3.1, +6.6) | 0.556 / 0.515 (+4.1, +11.7) | 0.184 / 0.146 (+3.8, +10.0) | 0.049 / 0.023 (+0.026, +4.6) | 0.573 / 0.556 (+1.8, +3.5) | 0.556 / 0.534 (+2.2, +6.8) | 0.184 / 0.165 (+1.9, +4.5) | 0.049 / 0.020 (+0.028, +4.6) |
| orientation FF only | 65,764 | 0.472 / 0.444 (+2.7, +6.6) | 0.456 / 0.423 (+3.3, +8.3) | 0.068 / 0.042 (+2.6, +8.1) | -0.001 / 0.003 (-0.003, -0.5) | 0.472 / 0.469 (+0.2, +0.6) | 0.456 / 0.443 (+1.3, +3.2) | 0.068 / 0.064 (+0.4, +1.3) | -0.001 / 0.006 (-0.007, -0.8) |
| orientation FB only | 87,527 | 0.654 / 0.605 (+4.9, +6.2) | 0.655 / 0.599 (+5.6, +11.6) | 0.294 / 0.237 (+5.7, +9.2) | 0.107 / 0.055 (+0.052, +4.9) | 0.654 / 0.623 (+3.2, +3.4) | 0.655 / 0.631 (+2.4, +6.1) | 0.294 / 0.267 (+2.7, +3.5) | 0.107 / 0.046 (+0.061, +5.0) |
| orientation BF only | 60,351 | 0.519 / 0.506 (+1.3, +2.6) | 0.507 / 0.498 (+0.9, +2.2) | 0.112 / 0.098 (+1.4, +3.7) | 0.039 / 0.002 (+0.037, +4.2) | 0.519 / 0.514 (+0.5, +1.0) | 0.507 / 0.493 (+1.4, +2.6) | 0.112 / 0.105 (+0.7, +1.6) | 0.039 / 0.023 (+0.016, +1.8) |
| orientation BB only | 15,782 | 0.663 / 0.667 (-0.4, -0.4) | 0.676 / 0.672 (+0.4, +0.6) | 0.248 / 0.238 (+1.0, +1.3) | -0.021 / 0.013 (-0.034, -1.6) | 0.663 / 0.656 (+0.6, +0.5) | 0.676 / 0.668 (+0.8, +1.2) | 0.248 / 0.239 (+0.9, +0.9) | -0.021 / -0.012 (-0.009, -0.4) |
| new candidacy before 2007 | 52,133 | 0.585 / 0.561 (+2.3, +2.1) | 0.581 / 0.554 (+2.7, +3.9) | 0.208 / 0.179 (+3.0, +3.7) | 0.031 / 0.016 (+0.015, +1.3) | 0.585 / 0.565 (+2.0, +1.7) | 0.581 / 0.564 (+1.7, +3.1) | 0.208 / 0.200 (+0.8, +1.0) | 0.031 / 0.016 (+0.016, +1.2) |
| new candidacy in 2007 or later | 177,291 | 0.563 / 0.531 (+3.3, +6.4) | 0.549 / 0.504 (+4.5, +11.9) | 0.161 / 0.124 (+3.7, +9.0) | 0.050 / 0.019 (+0.031, +4.9) | 0.563 / 0.552 (+1.2, +2.2) | 0.549 / 0.528 (+2.1, +6.2) | 0.161 / 0.145 (+1.6, +3.4) | 0.050 / 0.028 (+0.022, +3.3) |
| undated votes dropped | 219,516 | 0.566 / 0.534 (+3.2, +6.8) | 0.549 / 0.510 (+4.0, +11.9) | 0.172 / 0.136 (+3.6, +9.6) | 0.048 / 0.021 (+0.027, +4.8) | 0.566 / 0.551 (+1.5, +2.9) | 0.549 / 0.528 (+2.1, +6.7) | 0.172 / 0.156 (+1.6, +3.7) | 0.048 / 0.022 (+0.026, +4.3) |

Cut-off at the vote's own time keeps the in-candidacy votes of others that came earlier (herding is possible there) and raises the observed share; excluding w -> v ties from the old candidacy (co-voters of the old vote) leaves the excess; contexts at most two years old leave it; FF shows an excess under A that vanishes under B and has no interaction; FB carries the interaction; BB is empty. The era split shows it in both halves, thinly before 2007. Dropping every undated vote changes nothing.

## 8. Bitcoin OTC and Alpha: formation, not conversion [L4567-L4580]

No ordered pair is rated twice in either file (0 and 0 repeats): a tie is signed once, so only the closing of a triangle by a new tie can be looked at [L4571, L4580]. Undirected projection, each pair signed and timed by its earliest rating (the rule that reproduces 117's counts): OTC 21,492 pairs (358 rated with opposite signs in the two directions) and 33,493 triangles; Alpha 14,124 pairs (248) and 22,153 triangles, of which 20,016 have strictly ordered edge times (2,137 have a tie in the times, broken by pair number) [L4572]. The third edge's sign equals the product of the first two exactly when the triangle has an even number of negative ties, so the "closing-edge balance" is the share of strictly balanced triangles.

Three sign-shuffled nulls, each re-signing the pairs from the shuffled ratings: **global** (all pair signs permuted: 117's null, here 10,000 draws instead of 20), **rater** (each rater's ratings shuffled among his own: a negative-prone rater stays negative-prone) and **ratee** (shuffled among those received by the same trader: a widely distrusted trader stays distrusted, which is reputation or status in the sense of Leskovec et al.).

|  | triangles | balanced (third edge = product of the first two) | global null [95%], p | rater null | ratee null |
| :--- | ---: | ---: | ---: | ---: | ---: |
| OTC | 33,493 | 29,900 (89.3%) | 69.3% [68.1%, 70.6%], p <1e-4 | 72.7% [71.6%, 73.8%], p <1e-4 | 80.1% [79.2%, 81.1%], p <1e-4 |
| Alpha, strictly ordered | 20,016 | 17,567 (87.8%) | 79.1% [77.4%, 80.7%], p <1e-4 | 79.4% [77.9%, 80.9%], p <1e-4 | 87.6% [86.4%, 88.7%], p 0.376 |
| Alpha, all triangles | 22,153 | 19,539 (88.2%) | 79.1% [77.5%, 80.6%], p <1e-4 | 79.1% [77.7%, 80.6%], p <1e-4 | 86.7% [85.6%, 87.8%], p 0.003 |

**117's OTC figure reproduces exactly**: 29,900 of 33,493 (89.3%) against 69.3% (117: 67.9-70.7 over 20 shuffles; here 68.1%-70.6% at 95%). Alpha, which 117 gives for the strictly ordered triangles only (17,567 of 20,016, 87.8%, null 78.8%), reproduces too, and with all 22,153 triangles is 88.2% against 79.1%. **The excess does not survive every baseline.** Keeping each rater's negativity trims OTC's null to 72.7%; keeping each ratee's reputation lifts it to 80.1% (the data stay above every draw), and in Alpha the ratee null reaches the strictly ordered data (87.6% against 87.8%, p 0.376; with the 2,137 tied-time triangles added the data are +1.5 points above it, p 0.003): in Alpha the balance of the triangles adds almost nothing to who is widely distrusted.

Triangles by number of negative ties, the weak-balance reading (a one-negative triangle is the forbidden one; an all-negative one is balanced only weakly): observed, then each null's mean and the tail p in the direction of the departure.

|  | class | observed | global null | rater null | ratee null |
| :--- | ---: | ---: | ---: | ---: | ---: |
| OTC | one-negative | 3,354 | 10,188 (below, p <1e-4) | 8,130 (below, p <1e-4) | 5,561 (below, p <1e-4) |
| OTC | all-negative | 239 | 84 (above, p <1e-4) | 1,014 (below, p <1e-4) | 1,088 (below, p <1e-4) |
| Alpha (all) | one-negative | 2,518 | 4,627 (below, p <1e-4) | 4,568 (below, p <1e-4) | 2,795 (below, p 0.008) |
| Alpha (all) | all-negative | 96 | 13 (above, p <1e-4) | 54 (above, p <1e-4) | 143 (below, p 0.001) |

The one-negative triangle is depleted against every baseline in OTC and against the global and rater baselines in Alpha; against the ratee baseline Alpha's depletion is mild with all triangles (p 0.008) and absent among the strictly ordered ones (p 0.295). **The all-negative triangle is commoner than the global null (OTC 239 against 84; Alpha 96 against 13) but rarer than the rater and ratee nulls in OTC (against about 1,000).** 117's reading, that strict balance fails because the all-negative triangle is commoner than null, holds only against the global shuffle; once raters' negativity or targets' reputation is kept, OTC is depleted in both the one- and the all-negative triangle, which is what strict balance predicts. The formation figures support the weak form under the global baseline and the strict form under the others, so they do not settle strict against weak.

Closing sign by the first two edges (the two earliest edges by time; the share of closings that are positive):

|  | first two | triangles | closes positive | global null | rater null | ratee null |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| OTC | (+,+) | 26,964 | 92.3% | 86.4% | 87.7% | 93.0% |
| OTC | (+,-) | 5,500 | 23.0% | 86.4% | 69.0% | 69.4% |
| OTC | (-,-) | 1,029 | 76.8% | 86.5% | 39.6% | 44.2% |
| Alpha (all) | (+,+) | 19,814 | 91.4% | 91.7% | 90.6% | 94.8% |
| Alpha (all) | (+,-) | 1,855 | 43.6% | 91.7% | 84.2% | 77.9% |
| Alpha (all) | (-,-) | 484 | 80.2% | 91.8% | 79.8% | 58.7% |
| Alpha (ordered) | (+,+) | 18,201 | 91.0% | 91.7% | 90.7% | 95.0% |
| Alpha (ordered) | (+,-) | 1,536 | 49.0% | 91.8% | 85.3% | 81.1% |
| Alpha (ordered) | (-,-) | 279 | 77.1% | 91.8% | 82.4% | 78.3% |

A mixed start (+,-) closes *negative* 77% of the time in OTC against 14% under the global null, 31% within rater and 31% within ratee: the friend-of-my-enemy half of balance, robust. A (-,-) start closes positive 76.8% against 86.5% globally (enemy of my enemy fails), 39.6% within rater and 44.2% within ratee (it works): the verdict on that half depends on the baseline, as the all-negative count does. A (+,+) start closes positive at the global null rate in Alpha and below the ratee null in both files. Formation follows balance more strongly than conversion does (a new tie has to take some sign; a re-vote already has one), and none of this is a conversion result.

## 9. What this cannot say, and what was decided when

- **Votes are not friendships.** The ties in a triple are public evaluations of candidacies by voters: u -> w is u's vote at w's adminship election, w -> v is w's vote at an earlier candidacy of v. Agreement on a third party is agreement of judgement about a wiki role; it is balance in form and similarity-as-attraction or faction in content, and the FB-carried interaction cannot tell them apart.
- **A vote is a one-shot evaluation of a candidacy.** Oppose-to-support conversions are 79% of the total and 70% of those are a failed candidacy followed by a passed one: the candidate changed, or the voter judged the same record differently the second time. The nulls hold the new candidacy fixed but cannot hold *why* a given voter changed.
- **Timing granularity.** The unit of "before" is the candidacy (about a week; times are minutes, but 9,367 votes have none and are placed at their candidacy's median). Contexts are votes dated before the new candidacy began. Votes inside a candidacy are visible to later voters (the cut-off-at-the-vote cut raises the observed repair share by +2.9 points, consistent with herding), so the primary cut excludes them.
- **Selection into re-voting.** 5,990 re-votes by 1,563 voters (of 11,380 users) among 177,006 voter-candidate pairs; almost all follow a failed candidacy; 545 voters and 272 candidates supply the conversions, and a voter can supply 25. A candidacy cannot be re-voted unless the candidate failed, so the ties that can convert are the ties of a particular kind of candidate; the voter-matched nulls use only voters who re-vote at least twice with the same old sign.
- **One tie only.** A one-negative triple can be resolved through any of its three ties; here only the voter's tie to the candidate is re-observed, so tension resolved by changing u's tie to w or w's to v is invisible. The conversion rates are lower bounds on resolution.
- **Overlap and multiplicity.** Triples share ties, the same third party recurs across re-votes, and a voter appears many times: the permutation nulls respect that structure within their strata, the pooled counts do not. 9 nulls, several statistics and 10 cuts are shown without correction; read p of about 0.001-0.05 as suggestive. **Fixed before any null was computed:** the candidacy rule, the context cut-off, weak balance as the primary reading, the pooled repair share under the brief's null as the headline test, 10,000 draws. **Post hoc:** the conditional context shuffles (added on seeing the 79% direction mix), the event-permutation family (added when the context shuffles disagreed), the interaction contrast and orientation split (added on seeing that the FF cell rates carry no product structure), and the voter-generosity and number-of-triples terciles. The first-tie contrasts were defined after the cell rates were seen and before any null was run on them. Nothing was dropped for disagreeing.
- **Not tested.** The v0 §7 criterion as written ("conversion at the null rate") has no unique null; the nulls here are three different ones, and the answer depends on which is taken, which is the finding. The directed first-tie asymmetry in *formation* (Bitcoin ratings are directed and timed) is untested; the counts above are undirected.

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.wikirfa_report fetch    # once; checks sha256, writes to git-ignored data/wiki-rfa/ and data/bitcoin/
    ~/.local/bin/uv run python -m models.wikirfa_report report   # about 5 minutes on 8 cores; rewrites this file
    ~/.local/bin/uv run pytest tests/test_wikirfa_conversion.py
