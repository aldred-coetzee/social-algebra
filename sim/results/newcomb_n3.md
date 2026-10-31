# Newcomb fraternity: the n = 3 refutation test of v0.1 section 7, run on the data

_Generated 2026-11-01 by `uv run python -m models.newcomb_report report` (seed 20261031, 10,000 null draws). Code: `sim/models/newcomb.py`, `sim/models/newcomb_report.py`; checks: `sim/tests/test_newcomb_triads.py`. Ledger ids are the lines with source "104 §" (L4471-L4546). Results are computed statistics only; the rank file is local-use-only and is not redistributed (`sim/data/README.md`)._

**What was tested (v0.1 §7, n = 3; v0's hypothesis, not a source's):** in longitudinal signed triads the one-negative triangle must be (a) under-represented against a sign-shuffled null and (b) convert to a balanced triangle faster than the all-negative one; if conversion runs at the null rate, (4.2b)/(5.1) is refuted. Half (a) is Doreian & Krackhardt's (2001) static count; half (b) is new: neither D&K nor the 1996 paper prints a type-to-type transition table [L4527].

## Verdict

**In short.**

- *The pre-specified undirected cell cannot be run.* Under the 'agree' symmetrisation (only mutual same-sign ties; the reading faithful to v0's symmetric a_ij) the data hold **1** one-negative triangle in 15 waves against an expected 0.25 per wave, and conversion has 1 and 7 triangles at risk. Two proxies carry enough events: D&K's directed triples, and undirected triangles in which either direction signs a pair ('sum').
- *(a) Static: supported in aggregate, refuted for one of the three directed forms.* The one-negative class is below the sign-shuffled null in every wave as a pool, and LLD and LDL in every wave; DLL, also one-negative, is above it from wave 6 on (D&K's pattern, reproduced). All-negative DDD is enriched, which strict balance forbids.
- *(b) Conversion: not decided.* A one-negative triple becoming a complete balanced one is rare (15 and 33 events) and runs at about 1.5 times the null rate (p = 0.099 directed, p = 0.020 'sum'); it is not shown to be faster than the all-negative class (p = 0.334, p = 0.082). So v0's criterion, "conversion at the null rate", is not established either way. If a lost tie also counts as balanced (v0 §4.2; post hoc), one-negative triples do resolve faster than all-negative ones (in 7 of 8 recode-by-cell combinations), but because all-negative triples are unusually stable, which weak balance predicts and a consensus-disliked cluster also produces.
- *Net.* As an empirical rule, (4.2b)/(5.1) is **refuted in two forms by this data (symmetric in the three ties; strict and total), its weak form is supported as a depletion, and its dynamical claim is undecided.**

**(a) Is the one-negative triangle under-represented against the sign-shuffled null?**

- *Directed (D&K's eight types, top-4/bottom-3):* yes for two forms, no for the third. All ten text-stated claims of D&K's Figure 1 reproduce on these files (section 2.1). LLD and LDL are below the null in 15/15 waves; DLL, also one-negative, is *above* it in every wave from 6 on (p(obs > random) 0.988 to 1.000, z up to +6.3); D&K's reading is rivalry for the third man, with the first tie negative [L4508, L4511]. The pool of the three is below the null in 15/15 waves (z -6.0 to -2.5) but is 36% of complete triples at wave 1 and 21% at wave 15 against 45% under the null: depleted by up to half, not forbidden.
- *Undirected, 'sum' rule:* under-represented in 8 of 15 waves (3, 4, 6, 11, 12, 13, 14, 15), not detectably in the rest.
- *Undirected, 'agree' rule:* untestable, see above.
- *Consequence for v0:* a rule symmetric in the three ties cannot tell LLD, LDL and DLL apart, and the data do: an unbalanced triple whose first tie is negative is over-represented, not depleted. D&K's first-tie asymmetry [L4508] is reproduced and 104 §9's conclusion stands: (4.2b)/(5.1) is refuted as stated for directed ties.

**(b) Does it convert to balance faster than the all-negative one?**

- *Literal reading (a complete balanced type at the next wave), top-4/bottom-3, 14 transitions pooled:* directed one-negative 15 of 1375 (1.09%) against a null rate of 0.75% (ratio 1.45, p = 0.099); DDD 2 of 652 (0.31%, null 0.10%). 'Sum' triangles: 33 of 601 (5.49%) against 3.70% (ratio 1.48, p = 0.020); all-negative 7 of 251, at its null rate. **Faster than all-negative: p = 0.334 (directed) and p = 0.082 ('sum')** (difference 0.78% vs 0.65% expected under the null; 2.70% vs 0.85%). A modest excess in the predicted direction, from 15 and 33 events, no more. It is not stable across the cuts (section 4: over four recodes and the two cells the ratio runs 1.0-1.7, the p of the one-negative rate 0.02-0.59, the p of the difference 0.03-0.59). Against v0's criterion: conversion cannot be told from the null rate at 5% in the better-powered directed analysis, and is nominally above it in one of the two.
- *Where tension goes (post hoc).* What leaves a one-negative class leaves almost entirely by a tie dropping to 0, not by a sign flip: triples that lose a tie outnumber those that become complete balanced 728 to 15 (directed) and 311 to 33 ('sum'), i.e. 53% and 52% of those at risk (null 52% and 46%). Against the cond null the first-tie-positive unbalanced forms lose ties more and persist less (LLD to incomplete z = +4.1, LDL +3.9, ++- +2.9), whereas DLL, whose first tie is negative, does the opposite (z = -2.6): the first-tie rule again, now in the dynamics.
- *Relief reading (a complete balanced type OR a lost tie; v0 §4.2 calls an absent tie vacuously balanced; post hoc):* one-negative 54.0% vs all-negative 39.1% (directed), 57.2% vs 38.6% ('sum'); the difference exceeds the null difference (p < 0.001 directed, p < 0.001 'sum'; significant at 5% in 7 of 8 recode-by-cell combinations, section 4). Taken at face value that is the prediction. But the one-negative class itself is at its null (52.6%, p = 0.141) in the directed data and above it (49.3% null, p < 0.001) in the 'sum' triangles, while the all-negative class resists relief (55.1% null, below it with p < 0.001). The asymmetry is carried by the stability of all-negative triples, which is a late pattern (section 3.5).

**Weak (Davis) vs strict (Heider) balance.** Weak fits better than strict on every count. DDD is enriched from wave 5 on (z up to +13.0), the all-negative triangle is enriched under both symmetrisations, all-negative triples neither convert (2 of 652) nor dissolve at the null rate (61% stay complete against 45%), and the one-negative form is depleted but still common. Strict balance as a total rule is refuted on this group, as on the online networks (084 §4); the weak form survives as a depletion, not a prohibition.

**What the recode does.** It sets how many ties are signed, hence how many triples are at risk (directed one-negative at risk: 4/3 1375, 3/3 771, 5/4 2969, 3/2 496) and so the power; and it is a choice the files do not constrain [L4479]. The static contrasts (LLD, LDL depleted; DLL, DDD enriched; pool depleted) hold under all four cuts (section 4); D&K's ten wave-by-wave claims hold for 10/10 at 4/3, 7/10 at 3/3, 7/10 at 5/4, 4/10 at 3/2, so [L4478]'s "qualitative results also hold" is true of the contrasts, not of the details. The conversion results move with the cut: the strict ratio for the one-negative class runs 1.0-1.7 and its p 0.02-0.59, and the 'agree' rule never reaches a usable count (at most 8 one-negative triangles seen over all waves and cuts). The recode assumption therefore decides how powerful the test is and whether a marginal result survives; it does not decide the static verdicts.

**Status of v0.1 §7, n = 3.**

- *Refuted:* the symmetric triangle rule as a description of directed ties (DLL); strict balance as a total empirical rule (DDD enriched and stable).
- *Supported:* a depletion of the one-negative class in aggregate (directed pool 15/15 waves, 'sum' 8/15), the weak form of balance, and the relief asymmetry between one-negative and all-negative triples, each with the caveats above (one group, ranks recoded to signs, popularity free in the null).
- *Not decided:* whether one-negative triples convert to balance faster than a no-pressure null does: p = 0.099 directed, p = 0.020 'sum', difference from all-negative not significant, and the pre-specified 'agree' reading has no data. A decisive run needs a longer signed panel with explicit negatives, which D&K ask for [L4479] and which the ledger still lacks (v0 §7).

## 1. Data, terms, recode

- **Source.** `newfrat.dat`, the UCINET dataset "Newcomb Fraternity Networks" (fifteen 17 x 17 rank matrices NEWC0-NEWC15 without NEWC9 [L4538]), fetched from the Internet Archive's public snapshot of `vlado.fmf.uni-lj.si/pub/networks/data/UciNet/newfrat.dat` (the original host timed out from the box on 2026-10-31). Two snapshots (2021-04-21, 2024-10-04) are byte-identical, 13,702 bytes, sha256 `884537cbb60cf6c9c8e3cea3fa2d9f4a54fef8981b28151e65d65c5d89d43b46`.
- **Independent cross-check.** The R package `networkdata` (`schochastics/networkdata`, `data/fraternity.rda`, list of 15 igraph objects, edge attribute `rank`) holds exactly the same 15 x 17 x 17 ranks (compared cell by cell once, with a throwaway reader; that file was not kept). Each row of each wave is a permutation of 1-16 (checked on every load).
- **Terms [L4539-L4544].** The Pajek/UCINET listing states none; absence of a stated licence is not a grant. The UCI mirror's R documentation says CC BY-NC-ND 2.5 "if the source does not specify otherwise". The `networkdata` MIT licence covers the package, not the data. Treated as not licensed for redistribution: fetched for local use into git-ignored `sim/data/newcomb/`, never committed, results only here. Credit: Newcomb (1961), *The Acquaintance Process*; Nordlie (1958), thesis; the UCINET distribution (Borgatti, Everett, Freeman), via Batagelj & Mrvar's Pajek datasets.
- **Waves.** 15 observation indices (D&K's "weeks" 1-15; wave 9 is NEWC8, wave 10 is NEWC10), so 14 transitions, of which 9->10 spans two calendar weeks, which the authors ignored [L4472, L4545]; windows below include a "without the gap" check.
- **The sign is a modelling choice, not data [L4476, L4479].** Ranks 1-4 -> +, 14-16 -> -, 5-13 -> 0 (D&K's top-4 / bottom-3), so every man sends exactly 4 + / 3 - / 9 0 ties in every wave (68 + and 51 - ties per wave, [L4480]; verified). D&K themselves call this "a major data problem" [L4479]: the files cannot say whether a man ranking 16 others dislikes the bottom three or merely likes them least. Null ties are a third state; absence is not coded negative. Section 4 reruns everything with top-3/bottom-3, top-5/bottom-4 and D&K's own top-3/bottom-2 [L4478].
- **Does the recode reproduce what the 1996 paper measured on the same ranks?** Reciprocated positive ties per wave: 34, 30, 36, 36, 36, 32, 32, 32, 30, 36, 30, 30, 30, 34, 34 (1996 text: 30-35 of 68, plot reaching 36 in weeks 3-5 and 10 [L4520]; here 36 in waves 3, 4, 5 and 10; null median about 17 [L4521], here 16, mean 17.0, closed form 17). Share of ordered pairs changing state at the first transition: 31.2% (1996: "slightly above 30%" [L4527]); at transitions 2-5: 22.1%, 23.5%, 18.8%, 24.3%. That is consistent with the file, the wave order and the recode being the ones the authors used.
- **Correction to the brief.** It asked for "the 16 D&K types". D&K have **eight** signed ordered-triple types (LLL ... DDD) [L4481]; sixteen is Leskovec et al.'s count of directed triad types with edge direction (084 §4). The eight are computed, plus the undirected triangle types.

## 2. Static counts against the row-wise sign-shuffle null

Null: D&K's [L4485], 10,000 draws; every man keeps his 4 L and 3 D out-ties, received ties are free. Its distribution is the same for every wave (every row of every wave is a permutation of 1-16), so one sample serves all waves. Null mean counts (closed form in brackets, from the row structure alone): LLL 51.1 [51.0], LLD 51.0 [51.0], LDL 38.3 [38.2], LDD 38.2 [38.2], DLL 51.1 [51.0], DLD 25.5 [25.5], DDL 38.2 [38.2], DDD 19.1 [19.1].

### 2.1 D&K's eight directed types: p(obs > random) by wave (top-4 / bottom-3)

Above 0.95 = significantly more than the null, below 0.05 = significantly fewer [L4486]. Types are named (i->j)(j->k)(i->k), L = +, D = -. Heider-balanced: LLL LDD DLD DDL [L4482]; one-negative: LLD LDL DLL; all-negative: DDD.

| wave | LLL | LLD | LDL | LDD | DLL | DLD | DDL | DDD |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 1.000 | 0.002 | 0.006 | 0.920 | 0.600 | 0.599 | 0.017 | 0.799 |
| 2 | 1.000 | 0.000 | 0.000 | 1.000 | 0.600 | 0.417 | 0.232 | 0.799 |
| 3 | 1.000 | 0.000 | 0.000 | 1.000 | 0.920 | 0.124 | 0.094 | 0.857 |
| 4 | 1.000 | 0.000 | 0.000 | 1.000 | 0.661 | 0.328 | 0.094 | 0.726 |
| 5 | 1.000 | 0.000 | 0.000 | 1.000 | 0.892 | 0.001 | 0.009 | 1.000 |
| 6 | 1.000 | 0.000 | 0.000 | 1.000 | 0.988 | 0.014 | 0.001 | 1.000 |
| 7 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 |
| 8 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 |
| 9 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 |
| 10 | 1.000 | 0.000 | 0.000 | 1.000 | 0.999 | 0.000 | 0.000 | 1.000 |
| 11 | 1.000 | 0.000 | 0.000 | 1.000 | 0.999 | 0.014 | 0.000 | 1.000 |
| 12 | 1.000 | 0.000 | 0.000 | 1.000 | 1.000 | 0.000 | 0.000 | 1.000 |
| 13 | 1.000 | 0.000 | 0.000 | 1.000 | 0.998 | 0.000 | 0.000 | 1.000 |
| 14 | 1.000 | 0.000 | 0.000 | 1.000 | 0.995 | 0.000 | 0.000 | 1.000 |
| 15 | 1.000 | 0.000 | 0.000 | 1.000 | 0.999 | 0.000 | 0.000 | 1.000 |

z-scores of the same counts against the null (observed - null mean) / null sd:

| wave | LLL | LLD | LDL | LDD | DLL | DLD | DDL | DDD |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | +3.8 | -2.7 | -2.4 | +1.5 | +0.3 | +0.4 | -2.0 | +0.9 |
| 2 | +3.8 | -4.1 | -3.9 | +4.5 | +0.3 | -0.1 | -0.6 | +0.9 |
| 3 | +4.6 | -3.6 | -4.1 | +5.9 | +1.5 | -1.0 | -1.2 | +1.2 |
| 4 | +3.8 | -4.1 | -3.7 | +5.9 | +0.5 | -0.3 | -1.2 | +0.7 |
| 5 | +5.6 | -6.0 | -5.2 | +9.5 | +1.3 | -2.9 | -2.2 | +5.1 |
| 6 | +5.6 | -5.8 | -5.4 | +12.3 | +2.5 | -2.0 | -2.8 | +6.3 |
| 7 | +5.4 | -6.7 | -5.8 | +11.4 | +6.3 | -3.6 | -4.4 | +10.6 |
| 8 | +5.6 | -6.9 | -5.1 | +14.7 | +4.8 | -4.1 | -4.6 | +13.0 |
| 9 | +5.9 | -5.8 | -4.7 | +12.6 | +4.8 | -4.6 | -3.2 | +11.1 |
| 10 | +6.3 | -6.5 | -6.0 | +12.5 | +3.5 | -3.4 | -3.6 | +7.5 |
| 11 | +4.3 | -7.2 | -6.0 | +14.0 | +3.6 | -2.0 | -3.2 | +8.2 |
| 12 | +5.2 | -7.0 | -5.6 | +13.7 | +5.3 | -4.3 | -4.6 | +8.9 |
| 13 | +4.6 | -6.9 | -4.9 | +14.4 | +3.1 | -3.4 | -4.0 | +9.7 |
| 14 | +7.1 | -7.7 | -6.8 | +15.8 | +2.8 | -4.6 | -4.6 | +8.9 |
| 15 | +5.7 | -7.7 | -6.6 | +15.6 | +3.6 | -4.8 | -4.8 | +12.6 |

Observed counts of ordered triples (null mean in the last row):

| wave | LLL | LLD | LDL | LDD | DLL | DLD | DDL | DDD |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 75 | 35 | 26 | 47 | 53 | 27 | 28 | 23 |
| 2 | 75 | 27 | 18 | 64 | 53 | 25 | 35 | 23 |
| 3 | 80 | 30 | 17 | 72 | 60 | 21 | 32 | 24 |
| 4 | 75 | 27 | 19 | 72 | 54 | 24 | 32 | 22 |
| 5 | 86 | 16 | 11 | 93 | 59 | 13 | 27 | 40 |
| 6 | 86 | 17 | 10 | 109 | 66 | 17 | 24 | 45 |
| 7 | 85 | 12 | 8 | 104 | 89 | 10 | 16 | 63 |
| 8 | 86 | 11 | 12 | 123 | 80 | 8 | 15 | 73 |
| 9 | 88 | 17 | 14 | 111 | 80 | 6 | 22 | 65 |
| 10 | 91 | 13 | 7 | 110 | 72 | 11 | 20 | 50 |
| 11 | 78 | 9 | 7 | 119 | 73 | 17 | 22 | 53 |
| 12 | 84 | 10 | 9 | 117 | 83 | 7 | 15 | 56 |
| 13 | 80 | 11 | 13 | 121 | 70 | 11 | 18 | 59 |
| 14 | 96 | 6 | 3 | 129 | 68 | 6 | 15 | 56 |
| 15 | 87 | 6 | 4 | 128 | 73 | 5 | 14 | 71 |
| null mean | 51.1 | 51.0 | 38.3 | 38.2 | 51.1 | 25.5 | 38.2 | 19.1 |

**D&K's reported pattern, checked claim by claim (text-stated claims only, L4490-L4498), for each recode:**

| claim | 4/3 | 3/3 | 5/4 | 3/2 |
| :--- | :--- | :--- | :--- | :--- |
| LLL above the null in all 15 waves [L4490] | yes | **no** | yes | **no** |
| LDD above the null from wave 2 [L4491] | yes | yes | yes | yes |
| LDL below the null in all 15 waves [L4492] | yes | **no** | yes | yes |
| LLD below the null in all 15 waves, significant at the outset [L4493] | yes | yes | yes | yes |
| DLL not significant at wave 1 [L4494] | yes | yes | **no** | yes |
| DLL above the null in every wave from 6 on [L4494] | yes | yes | **no** | **no** |
| DDD above the null from wave 5 on [L4495] | yes | yes | yes | **no** |
| DLD below the null from wave 5 on [L4496] | yes | yes | yes | **no** |
| DDL below the null at wave 1 and from wave 5 on [L4497] | yes | yes | yes | **no** |
| from wave 6 every type is on one side of its null [L4498] | yes | **no** | **no** | **no** |

### 2.2 Is the one-negative triangle under-represented? Yes/no per wave (top-4 / bottom-3)

"under" / "over" = observed count below / above the null mean with a one-sided exact Monte-Carlo p <= 0.05 that counts ties against the observation (so a zero against a null that is mostly zero is not "under"); "-" = no difference detected. Columns: the three directed one-negative forms and their pool; the undirected one-negative triangle (++-) under the two symmetrisation rules.

| wave | LLD | LDL | DLL | LLD+LDL+DLL | ++- (sum) | ++- (agree) |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | under | under | - | under | - | - |
| 2 | under | under | - | under | - | - |
| 3 | under | under | - | under | under | - |
| 4 | under | under | - | under | under | - |
| 5 | under | under | - | under | - | - |
| 6 | under | under | over | under | under | - |
| 7 | under | under | over | under | - | - |
| 8 | under | under | over | under | - | - |
| 9 | under | under | over | under | - | - |
| 10 | under | under | over | under | - | - |
| 11 | under | under | over | under | under | - |
| 12 | under | under | over | under | under | - |
| 13 | under | under | over | under | under | - |
| 14 | under | under | over | under | under | - |
| 15 | under | under | over | under | under | - |
| **waves under** | 15/15 | 15/15 | 0/15 | 15/15 | 8/15 | 0/15 |
| **waves over** | 0/15 | 0/15 | 10/15 | 0/15 | 0/15 | 0/15 |

The pool is depleted but the one-negative form is nowhere near forbidden: it is 36% of complete directed triples at wave 1 and 21% at wave 15, against 45% under the null. Pooled z-scores run from -6.0 to -2.5.

**Under the 'agree' rule the test cannot be run.** Only mutual ties of one sign survive, and the null expects 0.25 one-negative triangles per wave (P(count = 0) = 0.78). Observed one-negative triangles per wave: 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 (a single one in 15 waves). All-negative: 0, 0, 0, 0, 0, 0, 1, 1, 2, 0, 1, 1, 1, 0, 1 against a null mean of 0.012; all-positive 2, 1, 5, 3, 4, 3, 2, 3, 2, 5, 2, 2, 2, 5, 3 against 0.085.

All four 'agree' triangle counts per wave (null mean in the last row), for completeness:

| wave | +++ | ++- | +-- | --- |
| :--- | ---: | ---: | ---: | ---: |
| 1 | 2 | 0 | 0 | 0 |
| 2 | 1 | 0 | 1 | 0 |
| 3 | 5 | 1 | 2 | 0 |
| 4 | 3 | 0 | 0 | 0 |
| 5 | 4 | 0 | 2 | 0 |
| 6 | 3 | 0 | 1 | 0 |
| 7 | 2 | 0 | 1 | 1 |
| 8 | 3 | 0 | 0 | 1 |
| 9 | 2 | 0 | 0 | 2 |
| 10 | 5 | 0 | 1 | 0 |
| 11 | 2 | 0 | 0 | 1 |
| 12 | 2 | 0 | 0 | 1 |
| 13 | 2 | 0 | 0 | 1 |
| 14 | 5 | 0 | 1 | 0 |
| 15 | 3 | 0 | 0 | 1 |
| null mean | 0.085 | 0.252 | 0.129 | 0.012 |

Undirected triangle counts under the 'sum' rule (a pair is + / - if either direction is, a conflict is 0), types by number of negative edges; null mean in the last row:

| wave | +++ | ++- | +-- | --- | complete |
| :--- | ---: | ---: | ---: | ---: | ---: |
| 1 | 28 | 53 | 54 | 11 | 146 |
| 2 | 32 | 51 | 57 | 8 | 148 |
| 3 | 26 | 40 | 43 | 14 | 123 |
| 4 | 22 | 36 | 63 | 11 | 132 |
| 5 | 26 | 42 | 68 | 18 | 154 |
| 6 | 31 | 41 | 60 | 19 | 151 |
| 7 | 31 | 51 | 55 | 24 | 161 |
| 8 | 31 | 55 | 65 | 28 | 179 |
| 9 | 35 | 58 | 60 | 24 | 177 |
| 10 | 30 | 46 | 66 | 24 | 166 |
| 11 | 31 | 27 | 61 | 16 | 135 |
| 12 | 32 | 35 | 44 | 15 | 126 |
| 13 | 29 | 41 | 59 | 19 | 148 |
| 14 | 29 | 25 | 55 | 20 | 129 |
| 15 | 27 | 26 | 50 | 20 | 123 |
| null mean | 23.8 | 61.9 | 43.1 | 8.0 | 136.7 |

z-scores of the 'sum' triangle counts against the null:

| wave | +++ | ++- | +-- | --- |
| :--- | ---: | ---: | ---: | ---: |
| 1 | +0.7 | -0.7 | +1.0 | +1.0 |
| 2 | +1.4 | -0.8 | +1.3 | +0.0 |
| 3 | +0.4 | -1.7 | -0.0 | +2.0 |
| 4 | -0.3 | -2.0 | +1.9 | +1.0 |
| 5 | +0.4 | -1.6 | +2.4 | +3.3 |
| 6 | +1.2 | -1.6 | +1.6 | +3.6 |
| 7 | +1.2 | -0.8 | +1.1 | +5.2 |
| 8 | +1.2 | -0.5 | +2.1 | +6.5 |
| 9 | +1.9 | -0.3 | +1.6 | +5.2 |
| 10 | +1.1 | -1.2 | +2.2 | +5.2 |
| 11 | +1.2 | -2.7 | +1.7 | +2.6 |
| 12 | +1.4 | -2.1 | +0.1 | +2.3 |
| 13 | +0.9 | -1.6 | +1.5 | +3.6 |
| 14 | +0.9 | -2.9 | +1.1 | +3.9 |
| 15 | +0.6 | -2.8 | +0.7 | +3.9 |

### 2.3 Weak (Davis) vs strict (Heider) balance, static

Strict balance forbids the one-negative AND the all-negative triple; weak balance forbids only the one-negative [L4482, L4483]. Share of complete directed triples that are strictly imbalanced (LLD LDL DLL DDD) and weakly imbalanced (LLD LDL DLL), observed vs null mean:

| wave | complete | strict-imbal | (null) | weak-imbal | (null) | z of DDD |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 314 | 43.6% | 51.0% | 36.3% | 44.9% | +0.9 |
| 2 | 320 | 37.8% | 51.0% | 30.6% | 44.9% | +0.9 |
| 3 | 336 | 39.0% | 51.0% | 31.8% | 44.9% | +1.2 |
| 4 | 325 | 37.5% | 51.0% | 30.8% | 44.9% | +0.7 |
| 5 | 345 | 36.5% | 51.0% | 24.9% | 44.9% | +5.1 |
| 6 | 374 | 36.9% | 51.0% | 24.9% | 44.9% | +6.3 |
| 7 | 387 | 44.4% | 51.0% | 28.2% | 44.9% | +10.6 |
| 8 | 408 | 43.1% | 51.0% | 25.2% | 44.9% | +13.0 |
| 9 | 403 | 43.7% | 51.0% | 27.5% | 44.9% | +11.1 |
| 10 | 374 | 38.0% | 51.0% | 24.6% | 44.9% | +7.5 |
| 11 | 378 | 37.6% | 51.0% | 23.5% | 44.9% | +8.2 |
| 12 | 381 | 41.5% | 51.0% | 26.8% | 44.9% | +8.9 |
| 13 | 383 | 39.9% | 51.0% | 24.5% | 44.9% | +9.7 |
| 14 | 379 | 35.1% | 51.0% | 20.3% | 44.9% | +8.9 |
| 15 | 388 | 39.7% | 51.0% | 21.4% | 44.9% | +12.6 |

DDD, which strict balance forbids, is above its null in 11 of 15 waves by D&K's rule, and in every wave from 5 on; the all-negative triangle is over-represented in 12/15 waves ('sum') and 7/15 ('agree', on 1-2 triangles a wave against an expected 0.01). Strict balance fails as a total descriptive rule here, as in the large online networks (084 §4); the weak form is the one that survives, and only as a depletion, not a prohibition.

## 3. Conversion: the new computation

**Definitions.** A triple of the start class at wave w is followed to its type at wave w+1; counts are pooled over transitions (a triple at risk at several waves is counted at each, so they are not independent events). *Strict conversion* = it is a complete balanced type at w+1: LLL LDD DLD DDL (triples), +++ or +-- (triangles) [L4482]. *Incomplete* = a tie fell to 0, which v0 §4.2 calls vacuously balanced. *Relief* = strict conversion or incomplete, i.e. v0's own convention taken literally (added after the first transition matrices were seen; see section 5). *Stays weakly balanced* (all-negative class) = still a complete weak-balanced type, in practice still all-negative [L4483].

**The null that matters is 'cond'.** The start wave is kept and the next wave's ties are re-placed at random within strata of start sign, keeping every man's own start-to-end transition table (directed triples) or the whole dyad transition table (triangles). Persistence, turnover and the 4/3/9 counts are held; only *which* ties change is random (10,000 draws per transition, independent across transitions; p = (1 + #{null >= obs})/(B + 1), one-sided in the direction v0 predicts unless marked). An excess over it means changes are aimed at tension; it cannot separate balance from reciprocity, popularity or rivalry (D&K's other mechanisms, L4511, L4512). The literal "independently shuffled waves" null is in 3.7: it ignores persistence, so every observed rate falls far below it.

### 3.1 Strict conversion into a complete balanced type (all 14 transitions pooled, top-4 / bottom-3)

| cell | start class | at risk | -> strict bal. | rate | null rate | ratio | p (>= obs) |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| directed D&K triples | one-negative (LLD, LDL, DLL) | 1375 | 15 | 1.09% | 0.75% | 1.45 | 0.099 |
| directed D&K triples | all-negative (DDD) | 652 | 2 | 0.31% | 0.10% | 3.01 | 0.145 |
| triangles, 'sum' rule | one-negative (++-) | 601 | 33 | 5.49% | 3.70% | 1.48 | 0.020 |
| triangles, 'sum' rule | all-negative (---) | 251 | 7 | 2.79% | 2.85% | 0.98 | 0.565 |
| triangles, 'agree' rule | one-negative (++-) | 1 | 0 | 0.00% | 0.00% | n/a | n/a (<10 at risk) |
| triangles, 'agree' rule | all-negative (---) | 7 | 0 | 0.00% | 0.00% | n/a | n/a (<10 at risk) |

v0 §7 asks whether the one-negative class converts *faster than the all-negative* one. The statistic is the difference of the two rates, compared with the same difference under the null, which is not zero (the one-negative triple has more routes to a balanced one than DDD has, so the null already favours it):

| cell | r(1-neg) - r(all-neg) | null mean of it | p (>= obs), vs null | naive Fisher p |
| :--- | ---: | ---: | ---: | ---: |
| directed D&K triples | 0.78% | 0.65% | 0.334 | 0.053 |
| triangles, 'sum' rule | 2.70% | 0.85% | 0.082 | 0.059 |
| triangles, 'agree' rule | 0.00% | 0.00% | n/a | n/a |

("naive Fisher p": one-sided exact test on the raw counts, which ignores that triples share ties and that the null already favours the one-negative class; shown because it is the first thing a reader would compute.)

### 3.2 Relief: balanced by a sign change OR by losing a tie (post hoc, v0's own convention)

| cell | start class | at risk | relief (rate) | null | p (>= obs) | p (<= obs) | of it, tie lost | null |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| directed D&K triples | one-negative (LLD, LDL, DLL) | 1375 | 743 (54.0%) | 52.6% | 0.141 | 0.871 | 52.9% | 51.9% |
| directed D&K triples | all-negative (DDD) | 652 | 255 (39.1%) | 55.1% | 1.000 | <0.001 | 38.8% | 55.0% |
| triangles, 'sum' rule | one-negative (++-) | 601 | 344 (57.2%) | 49.3% | <0.001 | 1.000 | 51.7% | 45.6% |
| triangles, 'sum' rule | all-negative (---) | 251 | 97 (38.6%) | 50.1% | 1.000 | <0.001 | 35.9% | 47.3% |

| cell | relief(1-neg) - relief(all-neg) | null mean of it | p (>= obs), vs null | naive Fisher p |
| :--- | ---: | ---: | ---: | ---: |
| directed D&K triples | 14.9% | -2.4% | <0.001 | <0.001 |
| triangles, 'sum' rule | 18.6% | -0.8% | <0.001 | <0.001 |

### 3.3 Type-to-type transition counts (pooled over the 14 transitions)

Rows = type at wave w, columns = type at wave w+1; "inc" = incomplete (some tie 0). These are the tables neither paper prints [L4527]. The second table gives the z-score of each cell against the 'cond' null (cells whose null never varies are "-").

Read the diagonal (z of persistence against the null; a post hoc reading). Among directed types the first tie decides, as in D&K [L4508]: with a positive first tie balanced types persist more than chance (LLL +2.6, LDD +8.0) and unbalanced ones less (LLD -4.3, LDL -3.8); with a negative first tie the balanced DDL persists *less* (-2.5), DLD at chance (-0.7), and the unbalanced DLL and DDD *more* (+2.3, +6.8). Triangles: +++ +3.4, +-- +2.1 and --- +3.4 persist more, ++- -3.7 less.

**directed D&K triples: observed counts**

| from \ to | LLL | LLD | LDL | LDD | DLL | DLD | DDL | DDD | inc |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| LLL | 717 | 3 | 0 | 0 | 5 | 0 | 0 | 0 | 440 |
| LLD | 0 | 70 | 0 | 0 | 0 | 3 | 0 | 0 | 168 |
| LDL | 1 | 0 | 45 | 0 | 0 | 0 | 1 | 0 | 127 |
| LDD | 0 | 1 | 0 | 907 | 0 | 0 | 0 | 2 | 481 |
| DLL | 0 | 0 | 0 | 0 | 517 | 3 | 7 | 0 | 433 |
| DLD | 0 | 0 | 0 | 0 | 0 | 61 | 0 | 0 | 142 |
| DDL | 0 | 0 | 0 | 0 | 1 | 0 | 100 | 1 | 219 |
| DDD | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 397 | 253 |
| inc | 459 | 138 | 107 | 565 | 457 | 113 | 198 | 300 | 49676 |

**directed D&K triples: z against the cond null**

| from \ to | LLL | LLD | LDL | LDD | DLL | DLD | DDL | DDD | inc |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| LLL | +2.6 | +0.4 | -0.7 | -0.3 | +2.0 | - | -0.3 | - | -2.8 |
| LLD | -0.7 | -4.3 | - | -0.7 | - | +2.5 | - | -0.1 | +4.1 |
| LDL | +1.4 | -0.4 | -3.8 | -1.0 | -0.4 | - | +0.2 | - | +3.9 |
| LDD | - | +1.1 | -1.0 | +8.0 | - | -0.4 | - | +0.0 | -8.0 |
| DLL | -0.9 | - | - | - | +2.3 | +1.7 | +1.1 | -0.3 | -2.6 |
| DLD | - | -0.4 | - | - | -0.4 | -0.7 | - | -1.1 | +0.9 |
| DDL | -0.2 | - | -0.6 | - | +0.6 | -0.4 | -2.5 | +0.3 | +2.5 |
| DDD | - | - | - | -0.5 | - | +1.7 | +1.7 | +6.8 | -6.8 |
| inc | +5.5 | -8.0 | -6.4 | +12.5 | +2.9 | -3.5 | -3.1 | +8.1 | -5.5 |

**triangles, 'sum' rule: observed counts**

| from \ to | +++ | ++- | +-- | --- | inc |
| :--- | ---: | ---: | ---: | ---: | ---: |
| +++ | 243 | 13 | 1 | 0 | 156 |
| ++- | 11 | 257 | 22 | 0 | 311 |
| +-- | 0 | 14 | 428 | 6 | 362 |
| --- | 0 | 0 | 7 | 154 | 90 |
| inc | 158 | 290 | 348 | 100 | 6549 |

**triangles, 'sum' rule: z against the cond null**

| from \ to | +++ | ++- | +-- | --- | inc |
| :--- | ---: | ---: | ---: | ---: | ---: |
| +++ | +3.4 | -0.7 | +0.4 | -0.1 | -3.2 |
| ++- | +1.5 | -3.7 | +1.8 | -0.6 | +2.9 |
| +-- | -0.4 | -0.8 | +2.1 | -1.0 | -1.7 |
| --- | -0.0 | -0.3 | -0.1 | +3.4 | -3.4 |
| inc | +0.2 | -3.9 | +2.9 | +1.0 | +0.7 |

**triangles, 'agree' rule: observed counts** (the whole of the evidence under the rule the brief named)

| from \ to | +++ | ++- | +-- | --- | inc |
| :--- | ---: | ---: | ---: | ---: | ---: |
| +++ | 23 | 0 | 0 | 0 | 18 |
| ++- | 0 | 0 | 0 | 0 | 1 |
| +-- | 0 | 0 | 1 | 0 | 8 |
| --- | 0 | 0 | 0 | 3 | 4 |
| inc | 19 | 1 | 8 | 5 | 9429 |

### 3.4 Windows

D&K find the dynamics essentially over by waves 5-6 [L4498], so the informative window is the first transitions, when about 30% of ties change [L4527]. Strict conversion of the one-negative class vs its null, and the difference test:

| cell | window | 1-neg at risk | -> bal. | null | p | all-neg at risk | -> bal. | p of difference |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| directed D&K triples | all 14 transitions | 1375 | 15 (1.09%) | 0.75% | 0.099 | 652 | 2 (0.31%) | 0.334 |
| directed D&K triples | first 5 (waves 1-6) | 505 | 12 (2.38%) | 1.49% | 0.096 | 132 | 2 (1.52%) | 0.564 |
| directed D&K triples | last 9 (waves 6-15) | 870 | 3 (0.34%) | 0.32% | 0.562 | 520 | 0 (0.00%) | 0.562 |
| directed D&K triples | all but the two-week gap (9->10) | 1264 | 15 (1.19%) | 0.82% | 0.099 | 587 | 2 (0.34%) | 0.334 |
| triangles, 'sum' rule | all 14 transitions | 601 | 33 (5.49%) | 3.70% | 0.020 | 251 | 7 (2.79%) | 0.082 |
| triangles, 'sum' rule | first 5 (waves 1-6) | 222 | 21 (9.46%) | 6.11% | 0.028 | 62 | 3 (4.84%) | 0.204 |
| triangles, 'sum' rule | last 9 (waves 6-15) | 379 | 12 (3.17%) | 2.29% | 0.176 | 189 | 4 (2.12%) | 0.228 |
| triangles, 'sum' rule | all but the two-week gap (9->10) | 543 | 27 (4.97%) | 3.29% | 0.023 | 227 | 5 (2.20%) | 0.062 |

Relief, same windows:

| cell | window | 1-neg relief | null | p (>=) | all-neg relief | null | p (<=) | p of difference |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| directed D&K triples | all 14 transitions | 54.0% | 52.6% | 0.141 | 39.1% | 55.1% | <0.001 | <0.001 |
| directed D&K triples | first 5 (waves 1-6) | 67.1% | 64.4% | 0.106 | 59.1% | 71.3% | 0.003 | <0.001 |
| directed D&K triples | last 9 (waves 6-15) | 46.4% | 45.8% | 0.364 | 34.0% | 50.9% | <0.001 | <0.001 |
| directed D&K triples | all but the two-week gap (9->10) | 55.0% | 53.5% | 0.137 | 37.5% | 54.4% | <0.001 | <0.001 |
| triangles, 'sum' rule | all 14 transitions | 57.2% | 49.3% | <0.001 | 38.6% | 50.1% | <0.001 | <0.001 |
| triangles, 'sum' rule | first 5 (waves 1-6) | 68.9% | 59.2% | 0.002 | 51.6% | 62.8% | 0.040 | 0.001 |
| triangles, 'sum' rule | last 9 (waves 6-15) | 50.4% | 43.5% | 0.009 | 34.4% | 46.0% | 0.002 | <0.001 |
| triangles, 'sum' rule | all but the two-week gap (9->10) | 58.0% | 49.7% | <0.001 | 38.8% | 51.7% | <0.001 | <0.001 |

### 3.5 Per transition (directed triples; top-4 / bottom-3)

| transition | 1-neg at risk | -> bal. | tie lost | DDD at risk | -> bal. | DDD stays complete |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1->2 | 114 | 7 | 77% | 23 | 2 | 17% |
| 2->3 | 98 | 0 | 66% | 23 | 0 | 52% |
| 3->4 | 107 | 0 | 67% | 24 | 0 | 8% |
| 4->5 | 100 | 5 | 55% | 22 | 0 | 59% |
| 5->6 | 86 | 0 | 55% | 40 | 0 | 62% |
| 6->7 | 93 | 0 | 48% | 45 | 0 | 73% |
| 7->8 | 109 | 0 | 41% | 63 | 0 | 90% |
| 8->9 | 103 | 0 | 36% | 73 | 0 | 70% |
| 9->10 (gap) | 111 | 0 | 43% | 65 | 0 | 46% |
| 10->11 | 92 | 0 | 48% | 50 | 0 | 48% |
| 11->12 | 89 | 0 | 44% | 53 | 0 | 58% |
| 12->13 | 102 | 0 | 44% | 56 | 0 | 66% |
| 13->14 | 94 | 0 | 66% | 59 | 0 | 66% |
| 14->15 | 77 | 3 | 47% | 56 | 0 | 73% |

12 of the 15 directed strict conversions fall in the first five transitions, and DDD stays complete in 26% of cases over transitions 1-3 against 65% over transitions 4-14: the all-negative stability is a late, consolidating pattern (D&K's macro-structure story, L4516), not present from the start.

### 3.6 Weak vs strict, dynamic

Strict balance says the all-negative triple is as tense as the one-negative and should be repaired. It is not repaired: its strict conversion is 2 of 652 (directed) and 7 of 251 (sum), and it stays a complete weakly-balanced triple at 61.2% (directed) and 64.1% (sum) against null rates of 45.0% and 52.7% (both p < 0.001). It persists *more* than random tie change would, which is what weak balance (nothing to repair) predicts and strict balance does not. The cause may be macro-structure rather than a drive: the consensus-disliked men [L4516-L4518] keep their negative in-ties, and the null does not preserve received ties [L4485 note].

### 3.7 The literal 'independently shuffled waves' null (why it is not the test)

Both waves of a transition are re-drawn independently from the row-wise shuffle, so the null rate is the marginal share of balanced triples at the next wave whatever the start. Ties persist (70-90% per transition [L4528]), so observed conversion is far below it for every class and the comparison says nothing about balance:

| cell | class | strict conv. | indep null | p (<= obs) | tie lost | indep null |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: |
| directed D&K triples | one-negative (LLD, LDL, DLL) | 1.09% | 3.75% | <0.001 | 52.9% | 92.3% |
| directed D&K triples | all-negative (DDD) | 0.31% | 3.77% | <0.001 | 38.8% | 92.3% |
| triangles, 'sum' rule | one-negative (++-) | 5.49% | 9.88% | <0.001 | 51.7% | 79.8% |
| triangles, 'sum' rule | all-negative (---) | 2.79% | 9.86% | 0.004 | 35.9% | 79.9% |

## 4. What the recode assumption does

The cut changes which ties count as signed: top-3/bottom-3 and top-3/bottom-2 sign fewer ties (3+3 = 6 and 3+2 = 5 of 16), top-5/bottom-4 more (9 of 16); the null is rebuilt with the matching row composition each time. Static questions, each recode (counts of waves out of 15; D&K's rule for the directed types, exact Monte-Carlo for the triangles):

| recode | LLD under | LDL under | DLL over (w6-15) | DDD over (w5-15) | 1-neg pool under | ++- (sum) under | --- (agree) over | D&K claims held | ++- (agree) seen |
| :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4/3 | 15 | 15 | 10/10 | 11/11 | 15 | 8 | 7 | 10/10 | 1 |
| 3/3 | 15 | 14 | 10/10 | 11/11 | 13 | 8 | 7 | 7/10 | 0 |
| 5/4 | 15 | 15 | 9/10 | 11/11 | 15 | 6 | 7 | 7/10 | 8 |
| 3/2 | 15 | 15 | 9/10 | 10/11 | 12 | 9 | 2 | 4/10 | 0 |

The contrasts that matter (LLD and LDL depleted, DLL and DDD enriched, the one-negative pool depleted) survive every cut; D&K's claim that the qualitative results hold for top-3/bottom-3 and top-3/bottom-2 [L4478] is confirmed in that sense, but the wave-by-wave significance details (section 2.1) are not stable: fewer signed ties means smaller counts and a noisier early study. Dynamic questions, all 14 transitions pooled, strict conversion:

| recode | cell | 1-neg at risk | -> bal. (rate) | null | p | all-neg at risk | -> bal. (rate) | p of difference |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4/3 | directed D&K triples | 1375 | 15 (1.09%) | 0.75% | 0.099 | 652 | 2 (0.31%) | 0.334 |
| 4/3 | triangles, 'sum' rule | 601 | 33 (5.49%) | 3.70% | 0.020 | 251 | 7 (2.79%) | 0.082 |
| 4/3 | triangles, 'agree' rule | 1 | 0 (0.00%) | 0.00% | 1.000 | 7 | 0 (0.00%) | 1.000 |
| 3/3 | directed D&K triples | 771 | 10 (1.30%) | 0.78% | 0.050 | 652 | 2 (0.31%) | 0.157 |
| 3/3 | triangles, 'sum' rule | 394 | 20 (5.08%) | 3.53% | 0.057 | 290 | 7 (2.41%) | 0.081 |
| 3/3 | triangles, 'agree' rule | 0 | 0 (n/a) | n/a | n/a | 7 | 0 (0.00%) | n/a |
| 5/4 | directed D&K triples | 2969 | 53 (1.79%) | 1.50% | 0.120 | 1301 | 16 (1.23%) | 0.034 |
| 5/4 | triangles, 'sum' rule | 889 | 53 (5.96%) | 5.14% | 0.149 | 396 | 15 (3.79%) | 0.043 |
| 5/4 | triangles, 'agree' rule | 8 | 0 (0.00%) | 0.00% | 1.000 | 16 | 0 (0.00%) | 1.000 |
| 3/2 | directed D&K triples | 496 | 3 (0.60%) | 0.60% | 0.592 | 201 | 0 (0.00%) | 0.592 |
| 3/2 | triangles, 'sum' rule | 285 | 10 (3.51%) | 2.43% | 0.155 | 103 | 1 (0.97%) | 0.171 |
| 3/2 | triangles, 'agree' rule | 0 | 0 (n/a) | n/a | n/a | 2 | 0 (0.00%) | n/a |

And relief (balanced or tie lost), where the one-negative class is compared with its null and with the all-negative class:

| recode | cell | 1-neg relief | null | p (>=) | all-neg relief | null | p (<=) | p of difference |
| :--- | :--- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 4/3 | directed D&K triples | 54.0% | 52.6% | 0.141 | 39.1% | 55.1% | <0.001 | <0.001 |
| 4/3 | triangles, 'sum' rule | 57.2% | 49.3% | <0.001 | 38.6% | 50.1% | <0.001 | <0.001 |
| 3/3 | directed D&K triples | 60.1% | 60.9% | 0.701 | 39.1% | 55.1% | <0.001 | <0.001 |
| 3/3 | triangles, 'sum' rule | 56.9% | 53.1% | 0.081 | 39.7% | 50.9% | <0.001 | <0.001 |
| 5/4 | directed D&K triples | 52.4% | 50.8% | 0.056 | 36.2% | 48.0% | <0.001 | <0.001 |
| 5/4 | triangles, 'sum' rule | 58.7% | 47.4% | <0.001 | 40.4% | 50.9% | <0.001 | <0.001 |
| 3/2 | directed D&K triples | 61.3% | 64.5% | 0.963 | 53.7% | 61.2% | 0.012 | 0.136 |
| 3/2 | triangles, 'sum' rule | 61.8% | 58.6% | 0.149 | 52.4% | 60.9% | 0.046 | 0.019 |

## 5. What this test cannot say, and what was decided when

- **One group, 17 men, one semester, strangers meeting for the first time** [L4471]: an acquaintance process, not a mature group, and a triangle inside a group of 17 is not an isolated n = 3 triad (each of its edges is also an edge of 14 other triangles).
- **Signs are a cut of ranks with fixed counts** [L4476, L4479, L4480]: neither the share of negative ties nor the share of balanced triples can vary, and a "conversion" can be a rank crossing the cut-off. Nothing here measures a sign the men reported.
- **The nulls hold rows, not columns.** D&K's shuffle, and the conditional one built from it, leave popularity free. Consensus-disliked men (J, P, C, O: [L4517, L4518]) make negative triples persist, which looks like stability of the all-negative triangle without any drive [L4512]. Competition for a third party [L4511] and reciprocity [L4513] are the other rivals, and actor attributes are lost [L4473], so a pattern here cannot be assigned to balance rather than to those.
- **Triples and triangles at risk overlap** and recur across waves; the permutation nulls respect the overlap, a naive count test does not (the Fisher p-values shown are for comparison only). The per-wave yes/no columns are 15 correlated tests, not 15 replications, and p-values across four recodes, three cells and four windows are not corrected for multiplicity: read p of about 0.02-0.05 as suggestive.
- **What was fixed in advance.** Before any result was computed: the 4/3 recode, 10,000 draws, the cells (directed triples; undirected triangles under 'agree'), the strict-conversion statistic and its difference test, the three sensitivity recodes, and the 'sum' rule and the windows as secondaries. **Post hoc:** the 'relief' target and the reading of the z-matrices for where tension goes, both after the first transition matrices showed that almost every exit from a tense triple is a tie dropping to 0 rather than a sign change; relief is nonetheless v0's own convention (§4.2: an absent tie is vacuously balanced). Nothing was dropped for disagreeing.
- **Absolute strict-conversion rates are tiny.** A conversion into a complete balanced type needs a + / - flip, which on a rank scale is a jump across nine neutral ranks. With 15 (directed) and 33 (sum) events the power to see a modest excess is low.

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.newcomb_report fetch    # once; checks sha256, writes to git-ignored data/newcomb/
    ~/.local/bin/uv run python -m models.newcomb_report report   # rewrites this file
    ~/.local/bin/uv run pytest tests/test_newcomb_triads.py

