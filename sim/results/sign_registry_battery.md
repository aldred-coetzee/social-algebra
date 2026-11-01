# Sign-law registry battery: the five tests of 112 section 6.5 on wiki-RfA, Bitcoin OTC and Alpha, and BlueTempNet

_Generated 2026-11-01 by `cd sim && ~/.local/bin/uv run python -m models.sign_registry_battery report` from statistics cached by `compute SITE` (seeded, 20261101). Code: `sim/models/sign_registry_battery.py`; checks: `sim/tests/test_sign_registry_battery.py`. Ledger ids: L5421 (the R-E form), L4811 and L4833 (forward chains), L4826-L4830 and L4850-L4852 (LHK's accuracies, person terms, visibility), L4812 (symmetry), L4857-L4859 (unrefreshed magnitudes, validity record), L4561-L4564 (wiki-RfA), L4567-L4580 (Bitcoin), L4593-L4598 (BlueTempNet). Results are computed statistics only; the data are local-use-only and are not redistributed (`sim/data/README.md`)._

## Verdict

**In short.** *Do signs have a mechanism inside the registry beyond person propensities?* **No by the pre-registered rule (R2), and not in the form the registry writes; but not nothing.** The registry's headline, FFmm < 0, is a person effect, and the triad terms add less than the pre-registered 0.02 AUC to person terms at every site. What remains beyond static person propensities is a residue at wiki-RfA, Bitcoin OTC and BlueTempNet (0.5 to 1.0 points of AUC overall, 3.1 at the best site where triad evidence is dense) that is only partly what the registry names. Small in AUC is not small per triad: on these networks a planted forward-chain mechanism of 0.3 log-odds per triad adds only 0.4 to 1.0 points above the person-only world, and the residue exceeds that at Bitcoin OTC and BlueTempNet.

- **Person terms carry the prediction.** Held out in time (causal features, four forward-chained blocks), a user's own earlier signs and the signs others gave the target predict a sign better than the 16 triad types do: AUC +0.056 to +0.152 higher at the 4 sites, every interval above 0 (the registry's prediction, 112 section 6.5 item 2, holds). Adding the triad types to the person terms adds -0.006 to +0.010 AUC against the pre-registered 0.02 for a material mechanism: R2 is **NO** (material at none of 4; the same with sender-and-receiver intervals).
- **A residue beyond static person propensities is real: in AUC it is 0.5 to 1.0 points, which exceeds a planted 0.3 log-odds-per-triad mechanism at Bitcoin OTC and BlueTempNet, and it is of a different form from the registry's.** Against the null (signs redrawn from person propensities on the same network, G -0.005 to +0.001) the observed G is clearly above it at wiki-RfA, Bitcoin OTC and BlueTempNet (z +18.8, +13.3, +60.6 in units of the null's replicate spread, which holds the person effects fixed; the two-way bootstrap interval of the observed G, which is wider, also lies above the null mean at each); where triad evidence is dense (C >= 5) G is -0.008 to +0.031, material at Bitcoin OTC. With person terms in the fit the types that keep a sign and a z beyond 1.96 (against 0; the null was recorded for the forward chains only) at three or more sites are FFpm (-), FFmp (-), FBpp (+), FBmp (-), FBmm (+), BFpp (+), BFpm (-), BFmm (+): two of the registry's forward chains (the mixed-sign ones, at 0.35 to 0.63 of their size without person terms) and agreement through a shared third party, not FFmm and not FFpp.
- **FFmm < 0 is a person effect.** Fitted alone, as LHK did, it is supported at wiki-RfA, Bitcoin Alpha and BlueTempNet (undecided at Bitcoin OTC; contradicted nowhere), and the whole forward chain pp +, pm -, mp -, mm - is supported at wiki-RfA and BlueTempNet. But signs drawn from person propensities alone give FFmm -0.80 to -0.58 on the same networks, as negative as or more negative than observed (-0.50 to -0.18); and with person terms in the fit, which is how R-E is written, FFmm is -0.06 to +0.11: no better than 0 at wiki-RfA, Bitcoin OTC and Bitcoin Alpha and positive at BlueTempNet (z beyond 1.96 on both rules). Power: with person terms in the causal fit a planted FFmm of -0.3 comes back as -0.33 at wiki-RfA, -0.04 at Bitcoin OTC, -0.18 at Bitcoin Alpha, -0.14 at BlueTempNet (full size at wiki-RfA, attenuated elsewhere); the observed values are +0.03 [-0.03, +0.09] at wiki-RfA, +0.20 [-0.10, +0.49] at Bitcoin OTC, +0.64 [-0.01, +1.29] at Bitcoin Alpha, +0.21 [+0.01, +0.41] at BlueTempNet, so a mechanism of that size is excluded at wiki-RfA, Bitcoin Alpha and BlueTempNet and cannot be excluded at Bitcoin OTC.
- **Reciprocity is a pair-level effect of the same order as the triads.** The reverse tie's sign adds +0.001 to +0.019 AUC to person terms (interval above 0 at wiki-RfA, Bitcoin OTC, Bitcoin Alpha and BlueTempNet; more than the 16 triad types add at Bitcoin OTC and Bitcoin Alpha, less at wiki-RfA and BlueTempNet); R-E has no such term.

| test (rule) | wiki-RfA | Bitcoin OTC | Bitcoin Alpha | BlueTempNet |
| --- | ---: | ---: | ---: | ---: |
| T1  FFmm, 16 types alone, static: coef (z 1-way/2-way) R1 | -0.48 (-21.2/-16.2) S/S | -0.18 (-1.8/-1.7) u/u | -0.46 (-2.5/-2.8) S/S | -0.50 (-8.0/-7.3) S/S |
| T1  FFmm, 16 types alone, in a person-only world | -0.58 (0.01) | -0.76 (0.08) | -0.80 (0.11) | -0.73 (0.03) |
| T1  FFmm, with person terms (R-E as written), static | +0.01 (+0.8/+0.7) u/u | +0.02 (+0.3/+0.3) u/u | -0.06 (-0.3/-0.3) u/u | +0.11 (+3.4/+2.7) C/C |
| T1  forward chains supported with person terms, static (of 4; 1-way/2-way) | 3/3 | 2/2 | 2/2 | 2/2 |
| T2  D = AUC(person) - AUC(triad), 2-way interval | +0.109 [+0.101, +0.117] | +0.097 [+0.071, +0.126] | +0.152 [+0.109, +0.196] | +0.056 [+0.048, +0.066] |
| T2  G = AUC(both) - AUC(person), 2-way interval | +0.0046 [+0.0029, +0.0063] | +0.0100 [+0.0042, +0.0166] | -0.0059 [-0.0192, +0.0037] | +0.0088 [+0.0060, +0.0112] |
| T2  R2 tier (1-way / 2-way) | small / small | small / small | none / none | small / small |
| T2  G at C >= 5, 2-way interval | +0.0086 [+0.0046, +0.0120] | +0.0315 [+0.0106, +0.0527] | -0.0078 [-0.0344, +0.0194] | +0.0053 [+0.0032, +0.0078] |
| T2  G minus person-only-world mean (z) | +0.0042 (z +18.8) | +0.0109 (z +13.3) | -0.0009 (z -0.4) | +0.0080 (z +60.6) |
| T3  forward chains CONTRADICTED in >= 2 date bins (16 types alone) | none | none | none | none |
| T3  intercepts move (range, logit) | yes (1.03) | yes (2.67) | yes (2.63) | yes (0.92) |
| T4  opposite-sign share of reciprocated pairs | 14.6% (NOT rare) | 2.5% (rare) | 2.5% (rare) | 4.1% (rare) |
| T5  InSign - OutSign at C = 0 (static), R5 1-way / 2-way (the verdict needs both) | +0.177 SUPPORTED / SUPPORTED | -0.020 ABSENT / UNDECIDED | -0.001 UNDECIDED / UNDECIDED | -0.060 ABSENT / ABSENT |

**Registry claims, one by one.**

- *T1, form transfer (R1).* **Supported** in the reading LHK fitted (16 types alone) at wiki-RfA, Bitcoin Alpha and BlueTempNet; **undecided** at Bitcoin OTC (FFmm z -1.8); **not supported** in the reading R-E writes (person terms in the fit): FFmm is not significantly negative at any site (R1's refutation, FFmm contradicted with adequate support, is met at BlueTempNet on both rules, though a person-only world gives +0.05 there too), and FFpp is not significantly positive at Bitcoin OTC and Bitcoin Alpha. FFpm and FFmp survive at wiki-RfA, Bitcoin OTC and Bitcoin Alpha.
- *T2, person terms against triad terms.* Person terms carry more: **supported** (D +0.056 to +0.152). The triad terms add more than person terms: **refuted**. R2 as pre-registered: **NO**. The result depends on what a person term is: with ridge-fitted effects frozen at the end of training (the other reading of a_i and b_j) person terms alone fall far below even the triad terms, because most test-period users are new (frozen minus online AUC -0.264 to -0.098).
- *T3, drift by date.* **Supported**: no forward-chain type is contradicted in two date bins at any site in the 16-type fit alone (R3), while intercepts move at wiki-RfA, Bitcoin OTC, Bitcoin Alpha and BlueTempNet (range 0.92 to 2.67 logit). The between-user variance of the sign (ICC, section 5) moves too, across date bins: wiki-RfA senders 0.15 to 0.22, receivers 0.28 to 0.41; Bitcoin OTC senders -0.01 to 0.39, receivers 0.46 to 0.63; Bitcoin Alpha senders -0.00 to 0.20, receivers 0.43 to 0.57; BlueTempNet senders 0.37 to 0.70, receivers 0.30 to 0.42. With person terms in the fit R3 is met by FFmm (positive in two or more bins) at BlueTempNet and, on the receiver-cluster rule only, at wiki-RfA. Magnitudes are not stable (I^2 is high for most coefficients); the 2010-11 bin (98% positive) has FFpp negative at Bitcoin OTC and Bitcoin Alpha, one bin.
- *T4, symmetry.* Opposite signs are **rare** (R4, at most 10%) at Bitcoin OTC, Bitcoin Alpha and BlueTempNet (0.025 to 0.041) and **not rare** at wiki-RfA (0.146), where a reciprocated pair is two votes in two elections years apart, not a reply. The two ties of a pair are concordant beyond person terms at every site (residual correlation 0.16 to 0.45): R-A's symmetric p_ij is defensible where replies are quick, but it is the reverse tie, not a symmetric factor, that carries the information. The opposite-sign share rises with the date at every site (first to last year with at least 100 pairs): wiki-RfA 5.2% in 2005 to 33.7% in 2012; Bitcoin OTC 1.1% in 2011 to 4.3% in 2015; Bitcoin Alpha 1.2% in 2011 to 6.1% in 2014; BlueTempNet 3.9% in 2023 to 4.8% in 2024.
- *T5, visibility.* **Supported** at wiki-RfA (gap at C = 0 +0.177, vanishing by C >= 25 as in LHK); **absent** at BlueTempNet; undecided at Bitcoin OTC and Bitcoin Alpha (absent on the receiver-cluster rule only at Bitcoin OTC, whose two-way interval is wide). Both rules must agree for either call. The gap moves with the date (at C = 0, static evidence): wiki-RfA +0.03 in 2003-04, +0.23 in 2010, +0.14 in 2013; Bitcoin OTC +0.16 in 2010-11, +0.07 in 2015-16; Bitcoin Alpha +0.16 in 2010-11, -0.06 in 2014-16; BlueTempNet +0.23 in 2023-05..2023-06, -0.07 in 2024-04..2024-05. It cannot be read as visibility: a received-majority advantage is also candidate quality and shared information, and a before/after test of earlier against later votes does not identify visibility (section 2).

**Refuted, supported, undecided.**

- *Refuted:* FFmm < 0 as something beyond person propensities (R-E as written: not significantly negative with person terms at any site, positive at BlueTempNet); that triad terms carry more than person terms (D > 0 at every site); a material triad gain beyond person terms (R2 NO: material at no site); opposite-sign reciprocation as rare at wiki-RfA; a received-majority advantage at BlueTempNet (R5 absent on both rules).
- *Supported:* that person terms carry more than triad terms; the forward-chain pattern in the 16-type fit alone at wiki-RfA and BlueTempNet (FFmm < 0 at wiki-RfA, Bitcoin Alpha and BlueTempNet), as R1 reads it, though a person-only world gives the same pattern; stability of the pattern across date bins with moving intercepts; rare opposite signs at Bitcoin OTC, Bitcoin Alpha and BlueTempNet; a received-majority advantage at low embeddedness at wiki-RfA; mixed-sign chains (FFpm, FFmp) as a small negative term beyond person terms at wiki-RfA, Bitcoin OTC and Bitcoin Alpha.
- *Undecided:* FFmm < 0 in the 16-type fit alone at Bitcoin OTC; FFpp > 0 at Bitcoin OTC and Bitcoin Alpha; visibility at Bitcoin OTC and Bitcoin Alpha; and whether the residue is a mechanism or a drifting person propensity (the null's person effects are static). The FFmm test has little power on the two small Bitcoin skeletons (a planted -0.3 does not come back there), so its null is firm at the larger sites only.

**Variations.** With person terms in the model strict and weak balance are practically indistinguishable (weak minus strict AUC -0.0003 to -0.0001; strict is ahead by that much, with the interval excluding 0, at Bitcoin OTC and BlueTempNet); alone, dropping the mm term helps where triads are many (weak minus strict AUC wiki-RfA +0.024 [+0.022, +0.026]; Bitcoin OTC +0.004 [+0.003, +0.006]; Bitcoin Alpha -0.001 [-0.004, +0.002]; BlueTempNet +0.021 [+0.018, +0.024]), which is LHK's weak-balance reading. Status adds -0.0015 to +0.0009 AUC to person terms and -0.0003 to +0.0004 to the 16 types (a small log-loss gain at some sites, no material AUC gain). By held-out log-loss the best of the registry's own forms is wiki-RfA: person+tri16+status; Bitcoin OTC: person+tri16+status; Bitcoin Alpha: person+bal_strict+status; BlueTempNet: person+tri16+status; the best variant overall is wiki-RfA: person_flex+tri16+interactions+recip; Bitcoin OTC: person_flex+tri16+interactions+recip; Bitcoin Alpha: person+bal_strict+status; BlueTempNet: person_flex+tri16+interactions+recip.

**What this does not settle.** It tests the registry's additive-logistic triad terms against online person histories on four sites; nonlinear learners, global structure, a measured drive, or exogenous variation in the triads could find more. Person-adjusted triad coefficients understate a mechanism that also shaped the person histories, and the null's person effects are static, so a user whose propensity drifts would also make recent triad counts informative (section 10). The AUC increment is insensitive on sparse skeletons: a planted forward-chain effect of 0.3 log-odds per triad adds only a few thousandths of AUC (section 9.2), so the coefficients and the C >= 5 strata carry the weight.

**For the first-outcome decision (Aldred's, not made here).** On this evidence the sign that a 'holds together or splits' model needs is a person-level propensity (a sender's habit, a receiver's standing) plus a local residue worth about one point of AUC overall (3 where triads are dense at the best site), not an output of the registry's triad terms as written; v0.2 section 2.2 already treats the sign as an input, and the residue (0.5 to 1.0 AUC points, more than a planted 0.3 log-odds-per-triad mechanism adds at Bitcoin OTC and BlueTempNet, but of a different form from the registry's) is too unlike the registry's triad terms to derive the sign from structure or composition instead. It does not say whether those propensities are drives (no site measures one) or whether the residue is a mechanism or drifting propensities, and it says nothing about conformity or effort outcomes.

## 1. Data and terms

| site | file bytes | sha256 | edges used | nodes | positive | period | distinct times | clusters |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| wiki-RfA | 14,936,383 | `88d53196fb25` | 170,334 | 11,017 | 77.9% | 2003-08-16 to 2013-06-05 | 162,986 | 4,040 |
| Bitcoin OTC | 397,258 | `6424ac981dad` | 35,592 | 5,881 | 90.0% | 2010-11-08 to 2016-01-25 | 35,592 | 5,858 |
| Bitcoin Alpha | 149,480 | `3a178611b9c2` | 24,186 | 3,783 | 93.6% | 2010-11-08 to 2016-01-22 | 1,647 | 3,754 |
| BlueTempNet | 221,305,868 | `360839bfc6f7` | 298,034 | 15,396 | 91.8% | 2023-05-11 to 2024-05-11 | 295,449 | 13,688 |

Clusters are the units resampled by the bootstrap and used by the robust standard errors: elections for wiki-RfA, receivers elsewhere.

- **wiki-RfA.** West, Paskov, Leskovec & Potts 2014, TACL 2: 297-310, doi:10.1162/tacl_a_00184. Fetched from `https://snap.stanford.edu/data/wiki-RfA.txt.gz`. Terms: SNAP states none; comments are Wikipedia text (CC BY-SA), never kept; local use only.
- **Bitcoin OTC.** Kumar, Spezzano, Subrahmanian & Faloutsos 2016, ICDM, doi:10.1109/ICDM.2016.0033; Kumar et al. 2018, WSDM, doi:10.1145/3159652.3159729. Fetched from `https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz`. Terms: SNAP states none; local use only.
- **Bitcoin Alpha.** Kumar, Spezzano, Subrahmanian & Faloutsos 2016, ICDM, doi:10.1109/ICDM.2016.0033; Kumar et al. 2018, WSDM, doi:10.1145/3159652.3159729. Fetched from `https://snap.stanford.edu/data/soc-sign-bitcoinalpha.csv.gz`. Terms: SNAP states none; local use only.
- **BlueTempNet.** Jeong, Jiang, Tan, Bernard & Liu 2024, IEEE Data Descriptions 1: 71-79, doi:10.1109/IEEEDATA.2024.3474640. Fetched from `https://media.githubusercontent.com/media/ujeong1/BlueTempNet-IEEE-DATA-2024/main/data/networks_to_share.zip`. Terms: DataCite lists CC BY 4.0 for the DataPort record (doi:10.21227/yrsy-ee91); the GitHub copy has no licence file; the authors ask for citation; local use only.

wiki-RfA filters: 198,275 records; 184,459 with a named voter, a non-neutral vote and not a self-vote; 177,181 of those dated; the first dated vote of each ordered pair is the edge (170,334 edges in 4,040 elections). Neutral votes, empty-voter records, self-votes and undated votes are dropped; repeat votes by a pair are the other agent's conversion test, not used here.

BlueTempNet: the feed-creator graph (`graph_dimension1`), 298,058 signed records, of which 24 self-loops are dropped. The feed-member graph (1.15 GB, 4.9 million follows) was not used. A follow is interest and a block is partly a safety tool (117 section 3.6); where a pair had both, the release keeps the block [L4595].

Embeddedness C(u,v) (common neighbours, direction ignored) of the edges, as the share of all edges, under the causal rule (earlier edges only) and the static rule (every other edge):

| site | C = 0 | C 1-4 | C 5-24 | C >= 25 |
| --- | ---: | ---: | ---: | ---: |
| wiki-RfA | 24% / 7% | 34% / 17% | 34% / 43% | 8% / 33% |
| Bitcoin OTC | 58% / 30% | 32% / 41% | 10% / 26% | 1% / 3% |
| Bitcoin Alpha | 61% / 30% | 29% / 40% | 10% / 27% | 1% / 3% |
| BlueTempNet | 22% / 6% | 37% / 20% | 33% / 43% | 8% / 31% |

## 2. Method

**Objects.** An edge is an ordered pair (u, v) with a sign, a time and a cluster. The 16 triad types are LHK's [F|B][F|B][p|m][p|m] [L4814]: for a common neighbour w of u and v, F if the u-w edge points u to w (B if w to u), F if the w-v edge points w to v (B if v to w), then the two signs. FFpp, FFpm, FFmp, FFmm are the forward chains. **Person terms** are the sender's earlier outgoing signs and the receiver's earlier incoming signs, as counts and shrunken log-odds (eight columns, deliberately generous; the empirical a_i and b_j of R-E). A second reading, a_i and b_j as ridge-fitted effects frozen at the end of each training window, is a variation.

**Two evidence rules.** *Static* (LHK's): every other edge of the snapshot is the evidence for an edge. *Causal*: only edges with a strictly earlier time are (edges at the same instant are invisible to one another). T2 uses only the causal rule; T1 and T3 report both.

**T2 protocol.** Edges are sorted by time; four forward-chained folds: train on the first 40% of edges and test on the next 15%, then train on 55% and test on the next 15%, and so on to 100% (60% of the edges are tested once). Logistic regression, ridge 1 on standardised columns, refit on every edge before each test block; the choice of raw or log counts is made once on an inner validation block (30% to 40%) and then held fixed. Metrics are pooled over the test blocks: AUC (primary), balanced accuracy at the training prevalence, log-loss. Intervals are 95% percentile intervals of a cluster bootstrap that resamples the same clusters for every model, so differences are paired; the clusters are elections (wiki-RfA) or receivers, as pre-registered, and a second, two-way interval resamples receivers and senders independently (the pigeonhole bootstrap), because the sign is strongly clustered by sender as well (ICC of the sign across senders up to 0.70, section 5). The z-values of the coefficients likewise come in a receiver-cluster and a two-way (Cameron-Gelbach-Miller) version.

**Pre-registered decision rules** (constants in the module, pinned by a test, fixed before any result): R1 a forward-chain coefficient is SUPPORTED if sigma z > 1.96, CONTRADICTED if sigma z < -1.96, with at least 100 edges carrying a triad of the type; the registry is refuted at a site if FFmm is CONTRADICTED. R2 triad terms add a mechanism beyond person terms at a site if G = AUC(person + triad) - AUC(person) is at least 0.02 with its interval above 0 ('small' if only the interval is above 0); YES overall if material at three or more of four sites, NO at one or none. R3 the pattern flips with date if a type is CONTRADICTED in at least 2 date bins; intercepts 'move' if Q has p < 0.001 and the range is at least 0.5 logit. R4 opposite signs are 'rare' at 10% or less of reciprocated pairs. R5 visibility is SUPPORTED if the lower bound of BA(InSign) - BA(OutSign) at C = 0 exceeds 0.02.

**What was and was not fixed in advance, stated plainly.** The numerical rules above were written before any result existed. R1 and R3 did not say whether the person terms are in the fit; a first look at T1 showed that the two readings diverge sharply, so both are reported side by side and every verdict says which it is for (nothing was dropped). The one-way clustering of the rules ignored the sender effect, so the two-way version was added beside it; where it changes a verdict that depends on a threshold the change is: wiki-RfA R3 snapshot:person True to False; Bitcoin OTC causal tri16 FFpp SUPPORTED to UNDECIDED; Bitcoin OTC R5 (static) ABSENT to UNDECIDED; Bitcoin Alpha causal person+tri16 FFmm CONTRADICTED to UNDECIDED; BlueTempNet causal person+tri16 FFpm SUPPORTED to UNDECIDED. The person-only generative null (section 9) was added after the first T2 pass showed G small, to interpret G; its first version (heavily shrunken person effects) produced a world with far less person signal than the real data and was replaced by one whose ridge is tuned so that the person-only model reaches the real data's held-out AUC. A before/after comparison of vote windows was run once on wiki-RfA during development (the k votes after a vote predicted it slightly better than the k before, by 0.2 to 1.9 balanced-accuracy points, k = 1 to 10) and a position gradient was never run; both were meant to separate visibility from candidate quality and were dropped because neither identifies it (in a stationary process the two directions of time are statistically indistinguishable, and a gradient has other causes, such as nominators voting first).

## 3. T1: form transfer, the 16-type model per site

Forward-chain coefficients of the logistic fit of the sign on the 16 raw triad counts (as LHK), by evidence rule and with or without the person terms in the fit. Cell: coefficient per triad, then z with clusters = receivers (elections for wiki-RfA), the pre-registered rule, and z with receiver-and-sender clusters (two-way), then the R1 letter under each (S supported, C contradicted, u undecided; at least 100 supporting edges). Predicted: FFpp +, FFpm -, FFmp -, FFmm -. 'Transfers' = FFmm supported and no forward chain contradicted; 'refuted' = FFmm contradicted. Senders are strongly clustered (section 5, ICC), so the two-way z is the more careful one; where the two disagree both are shown.

| site | evidence | fit | FFpp | FFpm | FFmp | FFmm | transfers (1-way / 2-way) | refuted (1-way / 2-way) |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| wiki-RfA | static | 16 types alone | +0.210 (+37.0/+24.4) S/S | -0.242 (-28.4/-15.5) S/S | -0.184 (-25.2/-16.1) S/S | -0.476 (-21.2/-16.2) S/S | yes / yes | no / no |
| wiki-RfA | static | 16 types + person terms | +0.060 (+16.7/+12.0) S/S | -0.086 (-13.1/-8.5) S/S | -0.095 (-13.8/-10.4) S/S | +0.013 (+0.8/+0.7) u/u | no / no | no / no |
| wiki-RfA | causal | 16 types alone | +0.348 (+26.8/+21.5) S/S | -0.405 (-20.4/-16.7) S/S | -0.273 (-20.6/-13.8) S/S | -0.722 (-19.8/-15.0) S/S | yes / yes | no / no |
| wiki-RfA | causal | 16 types + person terms | +0.090 (+11.7/+9.3) S/S | -0.121 (-8.7/-7.7) S/S | -0.121 (-9.4/-6.8) S/S | +0.030 (+1.2/+1.0) u/u | no / no | no / no |
| Bitcoin OTC | static | 16 types alone | +0.044 (+0.5/+0.5) u/u | -0.661 (-7.4/-5.9) S/S | -0.880 (-7.6/-6.4) S/S | -0.185 (-1.8/-1.7) u/u | no / no | no / no |
| Bitcoin OTC | static | 16 types + person terms | -0.012 (-0.2/-0.2) u/u | -0.416 (-8.4/-7.5) S/S | -0.443 (-5.6/-5.6) S/S | +0.023 (+0.3/+0.3) u/u | no / no | no / no |
| Bitcoin OTC | causal | 16 types alone | +0.225 (+2.0/+1.8) S/u | -1.283 (-6.6/-5.6) S/S | -1.548 (-9.2/-7.1) S/S | +0.027 (+0.2/+0.2) u/u | no / no | no / no |
| Bitcoin OTC | causal | 16 types + person terms | +0.128 (+1.5/+1.3) u/u | -0.498 (-4.2/-3.9) S/S | -0.781 (-6.5/-5.7) S/S | +0.196 (+1.4/+1.3) u/u | no / no | no / no |
| Bitcoin Alpha | static | 16 types alone | +0.044 (+0.5/+0.5) u/u | -0.589 (-6.2/-5.0) S/S | -0.551 (-4.0/-4.1) S/S | -0.458 (-2.5/-2.8) S/S | yes / yes | no / no |
| Bitcoin Alpha | static | 16 types + person terms | +0.014 (+0.2/+0.2) u/u | -0.304 (-4.4/-3.8) S/S | -0.315 (-3.4/-3.6) S/S | -0.059 (-0.3/-0.3) u/u | no / no | no / no |
| Bitcoin Alpha | causal | 16 types alone | +0.172 (+1.8/+1.7) u/u | -0.772 (-2.8/-2.7) S/S | -0.601 (-2.7/-2.6) S/S | +0.475 (+0.9/+0.9) u/u | no / no | no / no |
| Bitcoin Alpha | causal | 16 types + person terms | +0.056 (+0.6/+0.6) u/u | +0.024 (+0.1/+0.2) u/u | -0.369 (-2.0/-1.6) u/u | +0.644 (+2.0/+1.9) C/u | no / no | YES / no |
| BlueTempNet | static | 16 types alone | +0.266 (+12.9/+7.3) S/S | -0.112 (-5.1/-4.3) S/S | -0.151 (-3.7/-2.8) S/S | -0.504 (-8.0/-7.3) S/S | yes / yes | no / no |
| BlueTempNet | static | 16 types + person terms | +0.066 (+6.5/+3.3) S/S | -0.053 (-3.2/-2.7) S/S | +0.005 (+0.9/+0.6) u/u | +0.109 (+3.4/+2.7) C/C | no / no | YES / YES |
| BlueTempNet | causal | 16 types alone | +0.383 (+11.5/+7.8) S/S | -0.280 (-6.2/-4.7) S/S | -0.460 (-12.6/-9.4) S/S | -0.841 (-7.9/-5.1) S/S | yes / yes | no / no |
| BlueTempNet | causal | 16 types + person terms | +0.068 (+4.0/+2.6) S/S | -0.069 (-2.1/-1.6) S/u | -0.009 (-0.6/-0.4) u/u | +0.210 (+2.3/+2.1) C/C | no / no | YES / YES |

Support (edges carrying at least one triad of the type), static design:

| site | edges | FFpp | FFpm | FFmp | FFmm |
| --- | ---: | ---: | ---: | ---: | ---: |
| wiki-RfA | 170,334 | 134,993 | 62,081 | 72,335 | 26,817 |
| Bitcoin OTC | 35,592 | 20,864 | 3,880 | 4,389 | 1,031 |
| Bitcoin Alpha | 24,186 | 15,096 | 2,600 | 2,919 | 562 |
| BlueTempNet | 298,034 | 244,238 | 36,895 | 52,267 | 16,143 |

### 3.1 All 16 types, static design, with the sign each theory predicts

Learned coefficient (z) of the 16-type fit alone, then with person terms. Theory signs: B strict balance, W weak balance (0 = no prediction), S status [L4800, L4801, L4815]. In LHK's Table 2 (L4836) balance agreed with the learned signs on 13, 12 and 9 of 16 types at Epinions, Slashdot and Wikipedia and status on 5, 6 and 6 of its 8.

*16 types alone* (z with receiver clusters; the last column counts sites where the two-way z is beyond 1.96 with support >= 100)

| type | B / W / S | wiki-RfA | Bitcoin OTC | Bitcoin Alpha | BlueTempNet | sites sig. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| FFpp | +1 / +1 / +1 | +0.210 (+37.0) | +0.044 (+0.5) | +0.044 (+0.5) | +0.266 (+12.9) | 2+ 0- |
| FFpm | -1 / -1 / +0 | -0.242 (-28.4) | -0.661 (-7.4) | -0.589 (-6.2) | -0.112 (-5.1) | 0+ 4- |
| FFmp | -1 / -1 / +0 | -0.184 (-25.2) | -0.880 (-7.6) | -0.551 (-4.0) | -0.151 (-3.7) | 0+ 4- |
| FFmm | +1 / +0 / -1 | -0.476 (-21.2) | -0.185 (-1.8) | -0.458 (-2.5) | -0.504 (-8.0) | 0+ 3- |
| FBpp | +1 / +1 / +0 | +0.033 (+10.7) | +0.253 (+4.2) | +0.224 (+3.1) | +0.066 (+6.2) | 4+ 0- |
| FBpm | -1 / -1 / +1 | +0.003 (+0.3) | -0.064 (-0.5) | +0.004 (+0.0) | -0.006 (-0.4) | 0+ 0- |
| FBmp | -1 / -1 / -1 | -0.128 (-15.6) | -0.687 (-7.1) | -0.430 (-3.2) | -0.603 (-12.4) | 0+ 4- |
| FBmm | +1 / +0 / +0 | -0.006 (-0.5) | +0.133 (+1.0) | +0.158 (+1.1) | -0.159 (-4.9) | 0+ 1- |
| BFpp | +1 / +1 / +0 | +0.076 (+28.9) | +0.259 (+2.8) | +0.015 (+0.2) | +0.055 (+6.7) | 3+ 0- |
| BFpm | -1 / -1 / -1 | -0.187 (-30.6) | -0.595 (-7.4) | -0.578 (-5.5) | -0.537 (-8.2) | 0+ 4- |
| BFmp | -1 / -1 / +1 | +0.027 (+4.2) | -0.116 (-0.7) | +0.061 (+0.4) | -0.128 (-3.7) | 1+ 1- |
| BFmm | +1 / +0 / +0 | -0.034 (-4.7) | +0.014 (+0.3) | +0.053 (+0.7) | +0.041 (+1.9) | 0+ 1- |
| BBpp | +1 / +1 / -1 | -0.018 (-3.1) | -0.042 (-0.5) | +0.064 (+0.8) | -0.040 (-4.1) | 0+ 2- |
| BBpm | -1 / -1 / +0 | +0.006 (+0.2) | -0.311 (-2.7) | -0.129 (-0.8) | -0.013 (-0.3) | 0+ 1- |
| BBmp | -1 / -1 / +0 | +0.011 (+0.8) | +0.166 (+1.1) | -0.178 (-1.2) | +0.177 (+4.3) | 0+ 0- |
| BBmm | +1 / +0 / +1 | +0.062 (+1.2) | -0.046 (-0.3) | +0.062 (+0.3) | -0.013 (-0.3) | 0+ 0- |

Agreement of significant coefficients (|z| > 1.96, support >= 100) with each theory: wiki-RfA: balance 7/11, weak 7/9, status 6/6; Bitcoin OTC: balance 7/7, weak 7/7, status 2/2; Bitcoin Alpha: balance 5/6, weak 5/5, status 3/3; BlueTempNet: balance 8/12, weak 8/10, status 5/6.

*16 types + person terms* (z with receiver clusters; the last column counts sites where the two-way z is beyond 1.96 with support >= 100)

| type | B / W / S | wiki-RfA | Bitcoin OTC | Bitcoin Alpha | BlueTempNet | sites sig. |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| FFpp | +1 / +1 / +1 | +0.060 (+16.7) | -0.012 (-0.2) | +0.014 (+0.2) | +0.066 (+6.5) | 2+ 0- |
| FFpm | -1 / -1 / +0 | -0.086 (-13.1) | -0.416 (-8.4) | -0.304 (-4.4) | -0.053 (-3.2) | 0+ 4- |
| FFmp | -1 / -1 / +0 | -0.095 (-13.8) | -0.443 (-5.6) | -0.315 (-3.4) | +0.005 (+0.9) | 0+ 3- |
| FFmm | +1 / +0 / -1 | +0.013 (+0.8) | +0.023 (+0.3) | -0.059 (-0.3) | +0.109 (+3.4) | 1+ 0- |
| FBpp | +1 / +1 / +0 | +0.016 (+7.4) | +0.139 (+3.0) | +0.132 (+2.5) | +0.034 (+5.8) | 4+ 0- |
| FBpm | -1 / -1 / +1 | -0.025 (-3.2) | +0.011 (+0.1) | -0.081 (-0.7) | +0.012 (+1.2) | 0+ 1- |
| FBmp | -1 / -1 / -1 | -0.066 (-10.6) | -0.193 (-2.5) | -0.009 (-0.1) | -0.160 (-10.2) | 0+ 3- |
| FBmm | +1 / +0 / +0 | +0.052 (+5.9) | +0.328 (+2.8) | +0.372 (+3.9) | +0.048 (+4.1) | 4+ 0- |
| BFpp | +1 / +1 / +0 | +0.032 (+15.4) | +0.181 (+3.0) | +0.052 (+0.9) | +0.029 (+5.9) | 3+ 0- |
| BFpm | -1 / -1 / -1 | -0.070 (-15.7) | -0.166 (-2.7) | -0.247 (-4.0) | -0.135 (-5.4) | 0+ 4- |
| BFmp | -1 / -1 / +1 | -0.023 (-4.3) | -0.066 (-0.6) | -0.042 (-0.3) | -0.094 (-6.1) | 0+ 2- |
| BFmm | +1 / +0 / +0 | +0.079 (+11.6) | +0.450 (+5.2) | +0.350 (+3.7) | +0.157 (+8.8) | 4+ 0- |
| BBpp | +1 / +1 / -1 | -0.002 (-0.5) | -0.134 (-2.6) | -0.066 (-1.2) | -0.014 (-2.3) | 0+ 1- |
| BBpm | -1 / -1 / +0 | +0.006 (+0.3) | -0.259 (-2.9) | -0.021 (-0.2) | -0.012 (-0.6) | 0+ 1- |
| BBmp | -1 / -1 / +0 | +0.002 (+0.1) | -0.163 (-1.3) | -0.232 (-1.9) | +0.038 (+2.8) | 0+ 0- |
| BBmm | +1 / +0 / +1 | +0.040 (+1.0) | -0.068 (-0.6) | -0.011 (-0.1) | -0.068 (-1.9) | 0+ 0- |

Agreement of significant coefficients (|z| > 1.96, support >= 100) with each theory: wiki-RfA: balance 11/11, weak 9/9, status 3/5; Bitcoin OTC: balance 9/10, weak 7/8, status 3/3; Bitcoin Alpha: balance 6/6, weak 4/4, status 1/1; BlueTempNet: balance 10/12, weak 7/9, status 4/6.

### 3.2 How the forward chain depends on what is controlled (static design)

The same four coefficients as the person controls get stronger: none; two columns (shrunken sender and receiver log-odds); LHK's seven degree features [L4813]; the eight-column person block; the same with squares and products (14 columns).

| site | controls | FFpp | FFpm | FFmp | FFmm |
| --- | --- | ---: | ---: | ---: | ---: |
| wiki-RfA | none | +0.210 (+37.0/+24.4) S/S | -0.242 (-28.4/-15.5) S/S | -0.184 (-25.2/-16.1) S/S | -0.476 (-21.2/-16.2) S/S |
| wiki-RfA | 2 columns | +0.062 (+17.8/+13.1) S/S | -0.073 (-12.1/-7.4) S/S | -0.126 (-18.7/-13.5) S/S | +0.004 (+0.3/+0.2) u/u |
| wiki-RfA | LHK degree7 | +0.109 (+14.4/+8.3) S/S | -0.171 (-14.8/-9.6) S/S | -0.176 (-15.1/-11.9) S/S | -0.246 (-11.0/-8.1) S/S |
| wiki-RfA | person (8) | +0.060 (+16.7/+12.0) S/S | -0.086 (-13.1/-8.5) S/S | -0.095 (-13.8/-10.4) S/S | +0.013 (+0.8/+0.7) u/u |
| wiki-RfA | person (14) | +0.059 (+15.2/+11.9) S/S | -0.093 (-13.1/-9.2) S/S | -0.094 (-13.1/-10.0) S/S | -0.011 (-0.7/-0.6) u/u |
| Bitcoin OTC | none | +0.044 (+0.5/+0.5) u/u | -0.661 (-7.4/-5.9) S/S | -0.880 (-7.6/-6.4) S/S | -0.185 (-1.8/-1.7) u/u |
| Bitcoin OTC | 2 columns | -0.009 (-0.2/-0.1) u/u | -0.427 (-7.5/-7.1) S/S | -0.483 (-6.1/-6.0) S/S | -0.001 (-0.0/-0.0) u/u |
| Bitcoin OTC | LHK degree7 | +0.052 (+0.6/+0.5) u/u | -0.554 (-8.3/-6.0) S/S | -0.663 (-7.0/-5.6) S/S | +0.048 (+0.4/+0.4) u/u |
| Bitcoin OTC | person (8) | -0.012 (-0.2/-0.2) u/u | -0.416 (-8.4/-7.5) S/S | -0.443 (-5.6/-5.6) S/S | +0.023 (+0.3/+0.3) u/u |
| Bitcoin OTC | person (14) | -0.027 (-0.4/-0.4) u/u | -0.431 (-8.1/-7.4) S/S | -0.429 (-5.6/-5.4) S/S | +0.013 (+0.2/+0.2) u/u |
| Bitcoin Alpha | none | +0.044 (+0.5/+0.5) u/u | -0.589 (-6.2/-5.0) S/S | -0.551 (-4.0/-4.1) S/S | -0.458 (-2.5/-2.8) S/S |
| Bitcoin Alpha | 2 columns | +0.031 (+0.5/+0.5) u/u | -0.327 (-5.1/-4.7) S/S | -0.345 (-3.6/-3.8) S/S | -0.044 (-0.3/-0.3) u/u |
| Bitcoin Alpha | LHK degree7 | +0.101 (+1.3/+1.2) u/u | -0.468 (-5.5/-4.7) S/S | -0.353 (-3.1/-3.4) S/S | -0.275 (-1.3/-1.4) u/u |
| Bitcoin Alpha | person (8) | +0.014 (+0.2/+0.2) u/u | -0.304 (-4.4/-3.8) S/S | -0.315 (-3.4/-3.6) S/S | -0.059 (-0.3/-0.3) u/u |
| Bitcoin Alpha | person (14) | +0.017 (+0.3/+0.2) u/u | -0.304 (-4.0/-3.6) S/S | -0.218 (-2.4/-2.5) S/S | -0.174 (-0.9/-0.9) u/u |
| BlueTempNet | none | +0.266 (+12.9/+7.3) S/S | -0.112 (-5.1/-4.3) S/S | -0.151 (-3.7/-2.8) S/S | -0.504 (-8.0/-7.3) S/S |
| BlueTempNet | 2 columns | +0.064 (+6.1/+3.2) S/S | -0.089 (-6.2/-4.7) S/S | -0.018 (-1.6/-1.0) u/u | +0.063 (+2.9/+2.4) C/C |
| BlueTempNet | LHK degree7 | +0.173 (+9.6/+5.1) S/S | -0.059 (-2.7/-2.1) S/S | -0.067 (-2.0/-1.3) S/u | -0.172 (-3.4/-2.6) S/S |
| BlueTempNet | person (8) | +0.066 (+6.5/+3.3) S/S | -0.053 (-3.2/-2.7) S/S | +0.005 (+0.9/+0.6) u/u | +0.109 (+3.4/+2.7) C/C |
| BlueTempNet | person (14) | +0.072 (+6.9/+3.8) S/S | -0.035 (-2.2/-1.9) S/u | +0.012 (+3.8/+2.5) C/C | +0.073 (+2.4/+1.9) C/u |

### 3.3 Where triad evidence exists: edges with C >= 5 (static design)

| site | edges | fit | FFpp | FFpm | FFmp | FFmm |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| wiki-RfA | 129,787 | 16 types alone | +0.177 (+36.4/+25.5) S/S | -0.215 (-27.8/-15.2) S/S | -0.188 (-26.0/-17.3) S/S | -0.429 (-20.1/-15.4) S/S |
| wiki-RfA | 129,787 | 16 types + person terms | +0.056 (+15.0/+11.1) S/S | -0.077 (-11.4/-7.8) S/S | -0.099 (-13.6/-10.1) S/S | +0.012 (+0.7/+0.6) u/u |
| Bitcoin OTC | 10,246 | 16 types alone | +0.105 (+1.5/+1.4) u/u | -0.441 (-7.3/-5.1) S/S | -0.424 (-7.0/-7.0) S/S | -0.126 (-1.9/-1.6) u/u |
| Bitcoin OTC | 10,246 | 16 types + person terms | +0.027 (+0.4/+0.4) u/u | -0.395 (-7.4/-7.3) S/S | -0.273 (-4.3/-4.9) S/S | +0.014 (+0.2/+0.2) u/u |
| Bitcoin Alpha | 7,280 | 16 types alone | +0.052 (+0.7/+0.7) u/u | -0.469 (-6.0/-5.0) S/S | -0.293 (-2.4/-2.6) S/S | -0.330 (-1.9/-2.0) u/S |
| Bitcoin Alpha | 7,280 | 16 types + person terms | +0.000 (+0.0/+0.0) u/u | -0.345 (-5.0/-4.6) S/S | -0.158 (-1.7/-1.9) u/u | -0.051 (-0.3/-0.3) u/u |
| BlueTempNet | 219,295 | 16 types alone | +0.209 (+11.6/+6.9) S/S | -0.094 (-5.0/-4.2) S/S | -0.131 (-3.8/-3.0) S/S | -0.449 (-8.5/-7.8) S/S |
| BlueTempNet | 219,295 | 16 types + person terms | +0.056 (+6.3/+3.3) S/S | -0.031 (-2.3/-1.9) S/u | +0.000 (+0.1/+0.0) u/u | +0.109 (+3.5/+3.0) C/C |

### 3.4 Cross-site transfer of the fitted form

AUC at C >= 5 of the model fitted on every edge of the row site (static evidence) and scored on the column site's edges (LHK's Table 6 analogue, L4830: 0.925 to 0.935 on Epinions and Slashdot and 0.772 to 0.802 on Wikipedia at C >= 25, whichever site trained it). The diagonal is a fit scored in-sample.

*16 types alone*

| trained on | scored on wiki-RfA | scored on Bitcoin OTC | scored on Bitcoin Alpha | scored on BlueTempNet |
| --- | ---: | ---: | ---: | ---: |
| wiki-RfA | 0.866 | 0.932 | 0.882 | 0.952 |
| Bitcoin OTC | 0.832 | 0.952 | 0.907 | 0.950 |
| Bitcoin Alpha | 0.820 | 0.953 | 0.912 | 0.942 |
| BlueTempNet | 0.845 | 0.942 | 0.898 | 0.960 |

*16 types + person terms*

| trained on | scored on wiki-RfA | scored on Bitcoin OTC | scored on Bitcoin Alpha | scored on BlueTempNet |
| --- | ---: | ---: | ---: | ---: |
| wiki-RfA | 0.913 | 0.950 | 0.920 | 0.975 |
| Bitcoin OTC | 0.874 | 0.968 | 0.939 | 0.972 |
| Bitcoin Alpha | 0.877 | 0.967 | 0.943 | 0.973 |
| BlueTempNet | 0.907 | 0.959 | 0.935 | 0.978 |

## 4. T2: person terms against triad terms, held out in time

Forward-chained, causal features, pooled over the four test blocks (60% of the edges, the latest in time). 'person' = the eight person columns; 'triad' = the 16 triad counts alone; 'both' = person + triad. D = AUC(person) - AUC(triad) (the registry predicts D > 0); G = AUC(both) - AUC(person) (what the triad terms add beyond person terms; R2 calls it material at 0.02). 95% cluster-bootstrap intervals in brackets.

| site | model | AUC | balanced acc. | log-loss | params | counts |
| --- | --- | ---: | ---: | ---: | ---: | --- |
| wiki-RfA | person | 0.8776 [0.8700, 0.8832] | 0.7880 | 0.3544 | 9 | raw |
| wiki-RfA | triad | 0.7688 [0.7604, 0.7758] | 0.7028 | 0.4622 | 17 | log |
| wiki-RfA | both | 0.8822 [0.8748, 0.8877] | 0.7946 | 0.3493 | 25 | log |
| Bitcoin OTC | person | 0.9007 [0.8876, 0.9120] | 0.7499 | 0.2535 | 9 | raw |
| Bitcoin OTC | triad | 0.8033 [0.7866, 0.8205] | 0.7243 | 0.3209 | 17 | log |
| Bitcoin OTC | both | 0.9107 [0.8987, 0.9209] | 0.7630 | 0.2262 | 25 | log |
| Bitcoin Alpha | person | 0.8553 [0.8324, 0.8787] | 0.7269 | 0.2141 | 9 | raw |
| Bitcoin Alpha | triad | 0.7028 [0.6736, 0.7302] | 0.6472 | 0.2967 | 17 | log |
| Bitcoin Alpha | both | 0.8494 [0.8276, 0.8723] | 0.7323 | 0.2242 | 25 | log |
| BlueTempNet | person | 0.9520 [0.9486, 0.9551] | 0.8790 | 0.1421 | 9 | raw |
| BlueTempNet | triad | 0.8960 [0.8885, 0.9014] | 0.7922 | 0.2105 | 17 | log |
| BlueTempNet | both | 0.9608 [0.9579, 0.9633] | 0.8972 | 0.1256 | 25 | log |

Differences (paired). Intervals: first with clusters = receivers (elections for wiki-RfA), the pre-registered choice; second two-way (receivers and senders resampled independently, the pigeonhole bootstrap), which respects the strong sender effect.

| site | test edges | D person - triad | G both - person | R2 tier (1-way / 2-way) | edges C >= 5 | G, C >= 5 | tier, C >= 5 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| wiki-RfA | 102,200 | +0.1089 [+0.1041, +0.1136] / [+0.1013, +0.1169] | +0.0046 [+0.0034, +0.0058] / [+0.0029, +0.0063] | small / small | 46,443 | +0.0086 [+0.0062, +0.0113] / [+0.0046, +0.0120] | small / small |
| Bitcoin OTC | 21,355 | +0.0974 [+0.0799, +0.1135] / [+0.0706, +0.1262] | +0.0100 [+0.0061, +0.0143] / [+0.0042, +0.0166] | small / small | 2,937 | +0.0315 [+0.0164, +0.0460] / [+0.0106, +0.0527] | material / material |
| Bitcoin Alpha | 14,504 | +0.1524 [+0.1318, +0.1788] / [+0.1086, +0.1959] | -0.0059 [-0.0136, +0.0007] / [-0.0192, +0.0037] | none / none | 2,230 | -0.0078 [-0.0259, +0.0147] / [-0.0344, +0.0194] | none / none |
| BlueTempNet | 178,820 | +0.0560 [+0.0505, +0.0645] / [+0.0483, +0.0655] | +0.0088 [+0.0073, +0.0101] / [+0.0060, +0.0112] | small / small | 80,393 | +0.0053 [+0.0041, +0.0065] / [+0.0032, +0.0078] | small / small |

R2 across the sites run (4): material at 0, small at 3, none at 1 -> **NO** (YES needs three of four); with two-way intervals: material at 0, small at 3, none at 1 -> **NO**.

### 4.1 By embeddedness of the edge

Triad terms can only help where there is triad evidence; D and G inside strata of C (causal).

| site | stratum | edges | D | G |
| --- | ---: | ---: | ---: | ---: |
| wiki-RfA | C = 0 | 22,521 | +0.3653 | +0.0003 [-0.0001, +0.0008] |
| wiki-RfA | C 1-4 | 33,236 | +0.1008 | +0.0031 [+0.0021, +0.0044] |
| wiki-RfA | C 5-24 | 37,158 | +0.0447 | +0.0076 [+0.0057, +0.0098] |
| wiki-RfA | C >= 25 | 9,285 | +0.0242 | +0.0098 [+0.0045, +0.0157] |
| Bitcoin OTC | C = 0 | 10,958 | +0.2514 | -0.0016 [-0.0031, -0.0001] |
| Bitcoin OTC | C 1-4 | 7,460 | +0.0524 | +0.0159 [+0.0111, +0.0209] |
| Bitcoin OTC | C 5-24 | 2,712 | -0.0078 | +0.0289 [+0.0157, +0.0418] |
| Bitcoin OTC | C >= 25 | 225 | -0.1304 | +0.0758 [-0.0204, +0.1723] |
| Bitcoin Alpha | C = 0 | 7,351 | +0.1909 | +0.0004 [-0.0013, +0.0022] |
| Bitcoin Alpha | C 1-4 | 4,923 | +0.1795 | -0.0105 [-0.0209, +0.0000] |
| Bitcoin Alpha | C 5-24 | 2,088 | +0.0631 | -0.0092 [-0.0279, +0.0132] |
| Bitcoin Alpha | C >= 25 | 142 | -0.0399 | +0.0052 [-0.0781, +0.0686] |
| BlueTempNet | C = 0 | 37,944 | +0.3670 | +0.0087 [+0.0054, +0.0118] |
| BlueTempNet | C 1-4 | 60,483 | +0.0458 | +0.0093 [+0.0082, +0.0106] |
| BlueTempNet | C 5-24 | 60,485 | +0.0103 | +0.0054 [+0.0044, +0.0066] |
| BlueTempNet | C >= 25 | 19,908 | -0.0005 | +0.0075 [+0.0051, +0.0104] |

### 4.2 By test block

AUC in each forward-chained block (person / triad / both), the period of the block and its positive share.

| site | block | period | edges | positive | person | triad | both | G |
| --- | ---: | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| wiki-RfA | 1 | 2007-03-21 to 2007-12-05 | 25,550 | 80.3% | 0.891 | 0.765 | 0.897 | +0.005 |
| wiki-RfA | 2 | 2007-12-05 to 2008-10-12 | 25,550 | 75.7% | 0.874 | 0.769 | 0.879 | +0.005 |
| wiki-RfA | 3 | 2008-10-12 to 2010-04-16 | 25,550 | 73.8% | 0.859 | 0.756 | 0.865 | +0.006 |
| wiki-RfA | 4 | 2010-04-16 to 2013-06-05 | 25,550 | 77.2% | 0.884 | 0.776 | 0.887 | +0.003 |
| Bitcoin OTC | 1 | 2012-09-30 to 2013-03-15 | 5,339 | 89.6% | 0.879 | 0.732 | 0.885 | +0.006 |
| Bitcoin OTC | 2 | 2013-03-15 to 2013-07-19 | 5,338 | 91.8% | 0.917 | 0.725 | 0.911 | -0.006 |
| Bitcoin OTC | 3 | 2013-07-19 to 2013-12-29 | 5,339 | 77.2% | 0.920 | 0.845 | 0.932 | +0.013 |
| Bitcoin OTC | 4 | 2013-12-29 to 2016-01-25 | 5,339 | 85.9% | 0.864 | 0.773 | 0.889 | +0.025 |
| Bitcoin Alpha | 1 | 2012-04-30 to 2012-10-14 | 3,622 | 94.7% | 0.814 | 0.673 | 0.783 | -0.030 |
| Bitcoin Alpha | 2 | 2012-10-15 to 2013-04-04 | 3,636 | 91.1% | 0.856 | 0.658 | 0.843 | -0.013 |
| Bitcoin Alpha | 3 | 2013-04-05 to 2013-11-23 | 3,628 | 93.3% | 0.856 | 0.711 | 0.850 | -0.006 |
| Bitcoin Alpha | 4 | 2013-11-24 to 2016-01-22 | 3,618 | 84.6% | 0.829 | 0.680 | 0.843 | +0.015 |
| BlueTempNet | 1 | 2023-08-14 to 2023-09-15 | 44,705 | 90.3% | 0.967 | 0.935 | 0.975 | +0.009 |
| BlueTempNet | 2 | 2023-09-15 to 2023-11-23 | 44,705 | 90.5% | 0.955 | 0.895 | 0.962 | +0.007 |
| BlueTempNet | 3 | 2023-11-23 to 2024-02-11 | 44,705 | 90.7% | 0.942 | 0.862 | 0.952 | +0.010 |
| BlueTempNet | 4 | 2024-02-11 to 2024-05-11 | 44,705 | 87.2% | 0.944 | 0.883 | 0.955 | +0.011 |

### 4.3 Against LHK's own protocol (static evidence, random folds)

Five random folds, every other edge of the snapshot as evidence, as in LHK (10 folds there). 'degree7' is LHK's seven degree features; they found the triad types added 2 to 6 points of accuracy over them [L4829] and the degree features alone about 0.886 at C >= 25 on Epinions [L4828].

| site | edges | n | degree7 | person | triad | degree7 + triad | gain over degree7 | gain over person |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| wiki-RfA | all | 170,334 | 0.907 | 0.907 | 0.868 | 0.915 | +0.008 [+0.007, +0.009] | +0.009 |
| wiki-RfA | C >= 5 | 129,787 | 0.905 | 0.904 | 0.889 | 0.915 | +0.010 [+0.009, +0.011] | +0.011 |
| wiki-RfA | C >= 25 | 55,821 | 0.881 | 0.881 | 0.888 | 0.898 | +0.017 [+0.015, +0.019] | +0.018 |
| Bitcoin OTC | all | 35,592 | 0.926 | 0.928 | 0.880 | 0.945 | +0.018 [+0.014, +0.023] | +0.018 |
| Bitcoin OTC | C >= 5 | 10,246 | 0.941 | 0.939 | 0.961 | 0.970 | +0.029 [+0.022, +0.036] | +0.032 |
| Bitcoin OTC | C >= 25 | 1,149 | 0.817 | 0.806 | 0.940 | 0.926 | +0.109 [+0.073, +0.145] | +0.122 |
| Bitcoin Alpha | all | 24,186 | 0.915 | 0.912 | 0.832 | 0.927 | +0.012 [+0.007, +0.016] | +0.012 |
| Bitcoin Alpha | C >= 5 | 7,280 | 0.924 | 0.921 | 0.915 | 0.942 | +0.019 [+0.012, +0.028] | +0.021 |
| Bitcoin Alpha | C >= 25 | 752 | 0.884 | 0.876 | 0.912 | 0.911 | +0.027 [-0.011, +0.062] | +0.038 |
| BlueTempNet | all | 298,034 | 0.973 | 0.970 | 0.955 | 0.978 | +0.004 [+0.004, +0.005] | +0.009 |
| BlueTempNet | C >= 5 | 219,295 | 0.978 | 0.977 | 0.975 | 0.982 | +0.005 [+0.004, +0.005] | +0.006 |
| BlueTempNet | C >= 25 | 91,076 | 0.979 | 0.978 | 0.982 | 0.984 | +0.005 [+0.004, +0.006] | +0.006 |

LHK's 2 to 6 points over the degree features (points of balanced accuracy on balanced sets, read from a figure [L4829]; the gains here are AUC, so the comparison is loose) are reached here (point estimates; the interval includes 0 at Bitcoin Alpha at C >= 25) at Bitcoin OTC at C >= 5, Bitcoin OTC at C >= 25, Bitcoin Alpha at C >= 25; elsewhere the triad types add less. On all edges the static protocol gives the triad terms more than the time-split protocol does at wiki-RfA (+0.009 against +0.005), Bitcoin OTC (+0.018 against +0.010), Bitcoin Alpha (+0.012 against -0.006) (gain over person terms against G), as expected if static evidence includes edges that came after the one being predicted.

## 5. T3: drift by date

Each date bin is refitted separately: the bin's own edges form the snapshot (static evidence inside the bin), 16 types alone. Bins are calendar years (months for BlueTempNet) merged until each has enough edges (3,000 for wiki-RfA, 1,000 for Bitcoin, 9,000 for BlueTempNet). Cell: coefficient (z) and R1 letter. 'Q p' is Cochran's test that the per-bin estimates are equal; I^2 the share of their variance that is heterogeneity. ICC is the between-user share of the variance of the sign, for senders and for receivers.

**wiki-RfA**

| bin | edges | positive | intercept | FFpp | FFpm | FFmp | FFmm | ICC send | ICC recv |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2003-04 | 4,343 | 87.2% | +1.68 | +0.425 (+7.8/+8.2) S/S | -1.070 (-7.9/-8.7) S/S | -0.554 (-6.0/-6.7) S/S | -1.189 (-4.7/-3.9) S/S | 0.16 | 0.38 |
| 2005 | 15,866 | 85.8% | +1.32 | +0.405 (+13.0/+10.9) S/S | -0.572 (-10.5/-8.5) S/S | -0.504 (-9.0/-7.4) S/S | -1.057 (-8.7/-5.7) S/S | 0.22 | 0.35 |
| 2006 | 38,771 | 76.8% | +0.87 | +0.272 (+18.2/+13.4) S/S | -0.284 (-15.9/-6.2) S/S | -0.183 (-9.6/-6.9) S/S | -0.730 (-10.8/-9.1) S/S | 0.18 | 0.40 |
| 2007 | 37,227 | 79.5% | +0.95 | +0.287 (+19.1/+12.7) S/S | -0.435 (-15.4/-9.9) S/S | -0.222 (-11.0/-6.2) S/S | -0.792 (-13.5/-11.3) S/S | 0.17 | 0.37 |
| 2008 | 26,398 | 75.8% | +0.81 | +0.324 (+16.7/+12.9) S/S | -0.335 (-11.5/-8.7) S/S | -0.200 (-10.4/-9.2) S/S | -0.514 (-11.1/-6.6) S/S | 0.16 | 0.35 |
| 2009 | 18,650 | 74.1% | +0.75 | +0.316 (+14.6/+11.8) S/S | -0.245 (-8.6/-7.5) S/S | -0.140 (-5.6/-4.5) S/S | -0.568 (-11.1/-9.3) S/S | 0.16 | 0.32 |
| 2010 | 12,211 | 74.7% | +0.73 | +0.382 (+12.5/+11.2) S/S | -0.499 (-10.7/-8.4) S/S | -0.185 (-6.7/-7.0) S/S | -1.013 (-11.1/-9.6) S/S | 0.16 | 0.41 |
| 2011 | 7,678 | 79.2% | +0.95 | +0.402 (+10.3/+9.6) S/S | -0.570 (-6.7/-6.3) S/S | -0.302 (-3.6/-3.8) S/S | -0.653 (-5.1/-4.7) S/S | 0.15 | 0.37 |
| 2012 | 6,124 | 72.6% | +0.65 | +0.553 (+9.1/+8.2) S/S | -0.320 (-4.2/-4.3) S/S | -0.141 (-2.5/-2.5) S/S | -0.611 (-4.5/-4.4) S/S | 0.19 | 0.36 |
| 2013 | 3,066 | 80.5% | +1.13 | +0.511 (+7.9/+7.3) S/S | -0.922 (-4.8/-4.5) S/S | -0.104 (-1.3/-1.2) u/u | -1.293 (-5.7/-4.6) u/u | 0.16 | 0.28 |

Heterogeneity across bins (Q p / I^2): FFpp 2.8e-09 / 0.85; FFpm 3.8e-19 / 0.92; FFmp 6.7e-09 / 0.84; FFmm 6.9e-09 / 0.84; intercept 5.7e-15 / 0.90.

**Bitcoin OTC**

| bin | edges | positive | intercept | FFpp | FFpm | FFmp | FFmm | ICC send | ICC recv |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2010-11 | 7,900 | 98.0% | +4.11 | -0.907 (-3.9/-3.5) C/C | -2.247 (-4.0/-2.7) S/S | -2.843 (-4.9/-4.4) S/S | -2.566 (-3.0/-3.9) u/u | -0.01 | 0.46 |
| 2012 | 9,432 | 91.4% | +2.34 | +0.274 (+1.2/+1.2) u/u | -0.953 (-4.3/-3.7) S/S | -1.575 (-8.2/-6.3) S/S | -0.918 (-1.8/-1.8) u/u | 0.23 | 0.47 |
| 2013 | 12,982 | 85.8% | +2.09 | +0.173 (+1.4/+1.4) u/u | -1.016 (-7.6/-4.6) S/S | -1.432 (-6.5/-5.6) S/S | -0.138 (-1.0/-0.8) u/u | 0.39 | 0.50 |
| 2014 | 4,225 | 84.1% | +1.44 | +0.567 (+3.5/+4.5) S/S | -1.050 (-6.1/-7.1) S/S | -0.699 (-2.4/-3.0) S/S | -0.855 (-1.2/-1.3) u/u | 0.22 | 0.59 |
| 2015-16 | 1,053 | 92.0% | +1.99 | -0.135 (-0.4/-0.4) u/u | -2.590 (-1.7/-1.7) u/u | -9.026 (-5.1/-4.7) u/u | +0.000 (n/a/+0.0) u/u | 0.11 | 0.63 |

Heterogeneity across bins (Q p / I^2): FFpp 9.1e-06 / 0.86; FFpm 0.22 / 0.31; FFmp 3.5e-06 / 0.87; FFmm 0.016 / 0.71; intercept 2.3e-42 / 0.98.

**Bitcoin Alpha**

| bin | edges | positive | intercept | FFpp | FFpm | FFmp | FFmm | ICC send | ICC recv |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2010-11 | 7,701 | 98.1% | +4.13 | -0.891 (-4.0/-3.6) C/C | -2.460 (-4.2/-2.7) S/S | -2.816 (-4.9/-4.3) S/S | -2.662 (-3.3/-4.0) u/u | -0.00 | 0.46 |
| 2012 | 7,250 | 94.8% | +2.89 | +0.327 (+1.2/+1.2) u/u | -0.993 (-2.9/-2.6) S/S | -0.949 (-2.5/-2.0) S/S | -1.219 (-2.5/-2.1) u/u | 0.06 | 0.43 |
| 2013 | 6,121 | 91.0% | +2.36 | +0.560 (+3.0/+3.2) S/S | -0.778 (-6.0/-3.6) S/S | -0.941 (-5.5/-5.8) S/S | -0.724 (-2.2/-2.2) S/S | 0.17 | 0.53 |
| 2014-16 | 3,114 | 85.3% | +1.50 | +0.381 (+2.3/+1.8) S/u | -0.519 (-3.4/-2.6) S/S | -0.312 (-0.7/-1.0) u/u | -0.676 (-0.9/-1.0) u/u | 0.20 | 0.57 |

Heterogeneity across bins (Q p / I^2): FFpp 2.3e-06 / 0.90; FFpm 0.011 / 0.73; FFmp 0.005 / 0.77; FFmm 0.16 / 0.42; intercept 1.9e-38 / 0.98.

**BlueTempNet**

| bin | edges | positive | intercept | FFpp | FFpm | FFmp | FFmm | ICC send | ICC recv |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2023-05..2023-06 | 14,760 | 94.5% | +2.56 | +0.933 (+7.2/+6.4) S/S | -0.283 (-2.3/-1.8) S/u | -1.290 (-8.9/-8.4) S/S | -2.423 (-6.9/-6.7) S/S | 0.37 | 0.40 |
| 2023-07 | 70,170 | 95.4% | +2.31 | +0.652 (+6.2/+5.6) S/S | -0.662 (-4.1/-2.3) S/S | -0.473 (-1.4/-1.2) u/u | -1.892 (-9.8/-7.7) S/S | 0.39 | 0.42 |
| 2023-08 | 63,915 | 94.4% | +2.44 | +0.850 (+6.7/+4.7) S/S | -1.007 (-10.2/-7.4) S/S | -1.478 (-12.8/-11.9) S/S | -1.841 (-8.5/-6.3) S/S | 0.53 | 0.41 |
| 2023-09 | 30,426 | 87.8% | +2.07 | +1.678 (+9.4/+9.3) S/S | -0.631 (-6.0/-3.9) S/S | -1.668 (-13.8/-6.2) S/S | -3.623 (-16.8/-7.0) S/S | 0.70 | 0.37 |
| 2023-10 | 19,371 | 89.5% | +2.03 | +1.302 (+6.9/+5.5) S/S | -0.840 (-4.1/-3.7) S/S | -2.234 (-11.6/-9.0) S/S | -1.664 (-3.6/-2.8) S/S | 0.55 | 0.42 |
| 2023-11 | 12,426 | 88.6% | +2.02 | +1.343 (+5.6/+5.0) S/S | -1.117 (-4.0/-3.3) S/S | -1.678 (-5.3/-6.1) S/S | -1.632 (-2.8/-2.6) u/u | 0.53 | 0.37 |
| 2023-12 | 13,491 | 90.4% | +2.09 | +0.649 (+2.8/+2.7) S/S | -1.277 (-2.4/-2.4) u/u | -2.531 (-7.9/-6.0) S/S | -2.317 (-3.4/-3.4) u/u | 0.59 | 0.31 |
| 2024-01 | 11,462 | 87.8% | +1.87 | +1.674 (+4.4/+3.8) S/S | +0.273 (+0.3/+0.3) u/u | -2.675 (-9.2/-7.6) S/S | -1.561 (-3.8/-3.1) u/u | 0.64 | 0.35 |
| 2024-02 | 36,407 | 90.8% | +2.07 | +0.577 (+5.2/+3.2) S/S | -0.645 (-3.7/-3.0) S/S | -1.380 (-9.0/-7.4) S/S | -1.732 (-4.9/-4.3) S/S | 0.58 | 0.31 |
| 2024-03 | 13,303 | 86.4% | +1.65 | +0.936 (+5.9/+4.8) S/S | -0.176 (-0.7/-0.5) u/u | -0.980 (-3.1/-2.8) S/S | -1.610 (-4.1/-4.2) u/u | 0.57 | 0.30 |
| 2024-04..2024-05 | 12,303 | 86.0% | +1.64 | +1.317 (+5.5/+4.6) S/S | -0.366 (-1.5/-1.3) u/u | -1.988 (-8.6/-6.1) S/S | -1.705 (-3.9/-3.6) u/u | 0.66 | 0.35 |

Heterogeneity across bins (Q p / I^2): FFpp 3.3e-07 / 0.80; FFpm 0.00034 / 0.69; FFmp 4.6e-09 / 0.83; FFmm 4.8e-09 / 0.83; intercept 4.4e-19 / 0.91.

### 5.1 R3 verdicts

Bins in which a forward-chain type is CONTRADICTED (R1 rule, per bin), for the four readings: snapshot or cumulative history evidence, 16 types alone or with person terms. R3 calls the pattern flipped when a type is contradicted in at least 2 bins.

| site | reading | bins | contradicted bins, 1-way/2-way (pp pm mp mm) | supported bins, 1-way/2-way of adequate | R3, 1-way ; 2-way | intercepts move |
| --- | --- | ---: | --- | --- | --- | --- |
| wiki-RfA | snapshot:triad-only | 10 | pp 0/0, pm 0/0, mp 0/0, mm 0/0 | pp 10/10 of 10, pm 10/10 of 10, mp 9/9 of 10, mm 9/9 of 9 | stable ; stable | yes (range 1.03) |
| wiki-RfA | history:triad-only | 10 | pp 0/0, pm 0/0, mp 0/0, mm 0/0 | pp 10/10 of 10, pm 10/10 of 10, mp 10/10 of 10, mm 9/9 of 9 | stable ; stable | yes (range 0.98) |
| wiki-RfA | snapshot:+person | 10 | pp 0/0, pm 0/0, mp 0/0, mm 2/1 | pp 9/9 of 10, pm 9/9 of 10, mp 8/8 of 10, mm 0/0 of 9 | FLIPPED FFmm ; stable | no (range 2.66) |
| wiki-RfA | history:+person | 10 | pp 0/0, pm 0/0, mp 0/0, mm 1/1 | pp 6/6 of 10, pm 6/5 of 10, mp 8/8 of 10, mm 1/1 of 9 | stable ; stable | yes (range 3.81) |
| Bitcoin OTC | snapshot:triad-only | 5 | pp 1/1, pm 0/0, mp 0/0, mm 0/0 | pp 1/1 of 5, pm 4/4 of 4, mp 4/4 of 4, mm 0/0 of 2 | stable ; stable | yes (range 2.67) |
| Bitcoin OTC | history:triad-only | 5 | pp 0/0, pm 0/0, mp 0/0, mm 0/0 | pp 1/0 of 5, pm 3/3 of 3, mp 2/2 of 4, mm 0/0 of 0 | stable ; stable | yes (range 2.48) |
| Bitcoin OTC | snapshot:+person | 5 | pp 1/1, pm 0/0, mp 0/0, mm 1/0 | pp 1/1 of 5, pm 3/3 of 4, mp 3/3 of 4, mm 0/0 of 2 | stable ; stable | yes (range 13.31) |
| Bitcoin OTC | history:+person | 5 | pp 0/0, pm 0/0, mp 0/0, mm 0/0 | pp 0/0 of 5, pm 3/3 of 3, mp 3/3 of 4, mm 0/0 of 0 | stable ; stable | yes (range 7.33) |
| Bitcoin Alpha | snapshot:triad-only | 4 | pp 1/1, pm 0/0, mp 0/0, mm 0/0 | pp 2/1 of 4, pm 4/4 of 4, mp 3/3 of 4, mm 1/1 of 1 | stable ; stable | yes (range 2.63) |
| Bitcoin Alpha | history:triad-only | 4 | pp 0/0, pm 0/0, mp 0/0, mm 0/0 | pp 1/0 of 4, pm 1/1 of 2, mp 0/1 of 3, mm 0/0 of 0 | stable ; stable | yes (range 2.25) |
| Bitcoin Alpha | snapshot:+person | 4 | pp 1/1, pm 0/0, mp 0/0, mm 0/0 | pp 0/0 of 4, pm 1/1 of 4, mp 2/3 of 4, mm 0/0 of 1 | stable ; stable | yes (range 6.45) |
| Bitcoin Alpha | history:+person | 4 | pp 0/0, pm 0/0, mp 0/0, mm 0/0 | pp 0/0 of 4, pm 0/0 of 2, mp 0/0 of 3, mm 0/0 of 0 | stable ; stable | yes (range 4.98) |
| BlueTempNet | snapshot:triad-only | 11 | pp 0/0, pm 0/0, mp 0/0, mm 0/0 | pp 11/11 of 11, pm 7/6 of 8, mp 10/10 of 11, mm 6/6 of 6 | stable ; stable | yes (range 0.92) |
| BlueTempNet | history:triad-only | 11 | pp 0/0, pm 0/0, mp 0/0, mm 0/0 | pp 11/11 of 11, pm 7/6 of 11, mp 11/11 of 11, mm 8/8 of 10 | stable ; stable | yes (range 1.48) |
| BlueTempNet | snapshot:+person | 11 | pp 0/0, pm 0/0, mp 1/0, mm 5/5 | pp 4/3 of 11, pm 3/3 of 8, mp 1/1 of 11, mm 0/0 of 6 | FLIPPED FFmm ; FLIPPED FFmm | no (range 4.01) |
| BlueTempNet | history:+person | 11 | pp 0/0, pm 0/0, mp 1/1, mm 8/8 | pp 5/4 of 11, pm 3/4 of 11, mp 0/0 of 11, mm 0/0 of 10 | FLIPPED FFmm ; FLIPPED FFmm | yes (range 3.50) |

## 6. T4: symmetry

A reciprocated pair has a tie in each direction. Opposite-sign share with a Wilson interval; the null of independent signs at the observed marginals (2p(1-p), p the positive share inside reciprocated pairs); the person-propensity null (the expected opposite share if each tie were drawn from the sender-and-receiver model fitted on all ties); the correlation of the two ties' residuals from that model (positive = concordant beyond person terms). 'Reply' is the probability that the later tie of a pair is positive given the sign of the earlier one. R4 'rare' = at most 10%.

| site | reciprocated pairs | opposite signs | null: independent | null: person | residual corr. | reply + after + | reply + after - | R4 |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| wiki-RfA | 5,954 (7% of ties) | 14.6% [13.7, 15.5]% | 18.2% | 24.4% | +0.16 [+0.12, +0.19] | 92.7% (n 5,303) | 73.9% (n 651) | NOT rare |
| Bitcoin OTC | 14,100 (79% of ties) | 2.5% [2.3, 2.8]% | 6.6% | 9.4% | +0.45 [+0.42, +0.48] | 97.5% (n 13,779) | 5.3% (n 321) | rare |
| Bitcoin Alpha | 10,062 (83% of ties) | 2.5% [2.2, 2.8]% | 5.0% | 7.7% | +0.42 [+0.37, +0.46] | 97.8% (n 9,892) | 20.0% (n 170) | rare |
| BlueTempNet | 65,553 (44% of ties) | 4.1% [4.0, 4.3]% | 6.6% | 9.3% | +0.38 [+0.37, +0.40] | 95.8% (n 64,653) | 1.9% (n 900) | rare |

Opposite-sign share by the year of the pair's later tie:

| site | 2003 | 2004 | 2005 | 2006 | 2007 | 2008 | 2009 | 2010 | 2011 | 2012 | 2013 | 2014 | 2015 | 2016 | 2023 | 2024 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| wiki-RfA | 0.0% (n 1) | 7.7% (n 91) | 5.2% (n 630) | 14.6% (n 1775) | 11.3% (n 1225) | 16.1% (n 782) | 20.7% (n 527) | 16.4% (n 372) | 17.8% (n 281) | 33.7% (n 181) | 23.6% (n 89) |  |  |  |  |  |
| Bitcoin OTC |  |  |  |  |  |  |  | 0.0% (n 51) | 1.1% (n 3406) | 2.6% (n 3723) | 3.0% (n 4957) | 3.8% (n 1524) | 4.3% (n 418) | 4.8% (n 21) |  |  |
| Bitcoin Alpha |  |  |  |  |  |  |  | 0.0% (n 36) | 1.2% (n 3349) | 2.1% (n 3000) | 2.9% (n 2558) | 6.1% (n 1030) | 8.1% (n 86) | 0.0% (n 3) |  |  |
| BlueTempNet |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 3.9% (n 48237) | 4.8% (n 17316) |

## 7. T5: visibility

Balanced accuracy of InSign (predict + iff the target's other incoming ties are at least as often + as -) and OutSign (the same for the sender's other outgoing ties) [L4802], and their gap, by embeddedness; 95% cluster-bootstrap intervals. LHK's Wikipedia figures at C >= 0: InSign 0.706, OutSign 0.576; at C >= 25: 0.578 and 0.572 [L4851, L4852]. R5: SUPPORTED if the lower bound of the gap at C = 0 exceeds 0.02. The data cannot say whether a received-majority advantage is candidate quality, shared information or visibility of earlier votes [L4852].

| site | evidence | stratum | edges | InSign | OutSign | gap (interval 1-way / 2-way) | R5 at C = 0 (1-way / 2-way) |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- |
| wiki-RfA | static | all | 170,334 | 0.687 | 0.580 | +0.107 [+0.097, +0.119] / [+0.089, +0.127] |  |
| wiki-RfA | static | C = 0 | 11,628 | 0.739 | 0.562 | +0.177 [+0.162, +0.193] / [+0.154, +0.205] | SUPPORTED / SUPPORTED |
| wiki-RfA | static | C 1-4 | 28,919 | 0.758 | 0.580 | +0.178 [+0.165, +0.190] / [+0.156, +0.199] |  |
| wiki-RfA | static | C 5-24 | 73,966 | 0.681 | 0.583 | +0.098 [+0.085, +0.112] / [+0.077, +0.122] |  |
| wiki-RfA | static | C >= 25 | 55,821 | 0.577 | 0.570 | +0.007 [-0.008, +0.022] / [-0.017, +0.036] |  |
| wiki-RfA | causal | all | 170,334 | 0.674 | 0.573 | +0.101 [+0.092, +0.111] / [+0.088, +0.118] |  |
| wiki-RfA | causal | C = 0 | 40,305 | 0.715 | 0.564 | +0.151 [+0.142, +0.162] / [+0.136, +0.169] | SUPPORTED / SUPPORTED |
| wiki-RfA | causal | C 1-4 | 57,595 | 0.695 | 0.582 | +0.113 [+0.103, +0.124] / [+0.096, +0.134] |  |
| wiki-RfA | causal | C 5-24 | 58,725 | 0.614 | 0.572 | +0.043 [+0.031, +0.057] / [+0.023, +0.066] |  |
| wiki-RfA | causal | C >= 25 | 13,709 | 0.570 | 0.553 | +0.016 [-0.006, +0.035] / [-0.013, +0.049] |  |
| Bitcoin OTC | static | all | 35,592 | 0.688 | 0.654 | +0.034 [+0.008, +0.059] / [-0.029, +0.094] |  |
| Bitcoin OTC | static | C = 0 | 10,656 | 0.639 | 0.660 | -0.020 [-0.046, +0.005] / [-0.141, +0.106] | ABSENT / UNDECIDED |
| Bitcoin OTC | static | C 1-4 | 14,690 | 0.702 | 0.632 | +0.070 [+0.038, +0.101] / [-0.002, +0.142] |  |
| Bitcoin OTC | static | C 5-24 | 9,097 | 0.712 | 0.684 | +0.028 [-0.020, +0.074] / [-0.036, +0.089] |  |
| Bitcoin OTC | static | C >= 25 | 1,149 | 0.516 | 0.481 | +0.035 [-0.024, +0.119] / [-0.043, +0.147] |  |
| Bitcoin OTC | causal | all | 35,592 | 0.631 | 0.619 | +0.012 [-0.010, +0.038] / [-0.031, +0.051] |  |
| Bitcoin OTC | causal | C = 0 | 20,658 | 0.603 | 0.598 | +0.004 [-0.019, +0.028] / [-0.052, +0.062] | UNDECIDED / UNDECIDED |
| Bitcoin OTC | causal | C 1-4 | 11,307 | 0.658 | 0.640 | +0.018 [-0.010, +0.050] / [-0.033, +0.066] |  |
| Bitcoin OTC | causal | C 5-24 | 3,389 | 0.633 | 0.615 | +0.018 [-0.028, +0.060] / [-0.039, +0.072] |  |
| Bitcoin OTC | causal | C >= 25 | 238 | 0.512 | 0.495 | +0.017 [-0.010, +0.122] / [-0.044, +0.169] |  |
| Bitcoin Alpha | static | all | 24,186 | 0.641 | 0.573 | +0.068 [+0.030, +0.119] / [-0.026, +0.166] |  |
| Bitcoin Alpha | static | C = 0 | 7,169 | 0.637 | 0.638 | -0.001 [-0.042, +0.047] / [-0.109, +0.128] | UNDECIDED / UNDECIDED |
| Bitcoin Alpha | static | C 1-4 | 9,737 | 0.668 | 0.584 | +0.083 [+0.038, +0.130] / [-0.036, +0.197] |  |
| Bitcoin Alpha | static | C 5-24 | 6,528 | 0.624 | 0.535 | +0.089 [+0.014, +0.160] / [-0.015, +0.183] |  |
| Bitcoin Alpha | static | C >= 25 | 752 | 0.550 | 0.485 | +0.065 [+0.011, +0.193] / [+0.000, +0.228] |  |
| Bitcoin Alpha | causal | all | 24,186 | 0.567 | 0.523 | +0.044 [+0.013, +0.085] / [-0.002, +0.103] |  |
| Bitcoin Alpha | causal | C = 0 | 14,689 | 0.541 | 0.522 | +0.019 [+0.002, +0.042] / [-0.020, +0.053] | UNDECIDED / UNDECIDED |
| Bitcoin Alpha | causal | C 1-4 | 6,996 | 0.611 | 0.525 | +0.085 [+0.038, +0.137] / [+0.014, +0.165] |  |
| Bitcoin Alpha | causal | C 5-24 | 2,357 | 0.545 | 0.520 | +0.025 [-0.020, +0.090] / [-0.036, +0.113] |  |
| Bitcoin Alpha | causal | C >= 25 | 144 | 0.519 | 0.491 | +0.027 [+0.000, +0.253] / [+0.000, +0.308] |  |
| BlueTempNet | static | all | 298,034 | 0.661 | 0.728 | -0.066 [-0.108, -0.029] / [-0.145, +0.006] |  |
| BlueTempNet | static | C = 0 | 18,567 | 0.635 | 0.694 | -0.060 [-0.090, -0.030] / [-0.117, -0.015] | ABSENT / ABSENT |
| BlueTempNet | static | C 1-4 | 60,172 | 0.654 | 0.708 | -0.054 [-0.087, -0.020] / [-0.102, -0.007] |  |
| BlueTempNet | static | C 5-24 | 128,219 | 0.666 | 0.738 | -0.072 [-0.119, -0.028] / [-0.151, +0.012] |  |
| BlueTempNet | static | C >= 25 | 91,076 | 0.672 | 0.743 | -0.072 [-0.143, -0.008] / [-0.217, +0.088] |  |
| BlueTempNet | causal | all | 298,034 | 0.636 | 0.699 | -0.063 [-0.097, -0.027] / [-0.132, +0.005] |  |
| BlueTempNet | causal | C = 0 | 64,608 | 0.626 | 0.673 | -0.046 [-0.081, -0.010] / [-0.105, +0.009] | ABSENT / ABSENT |
| BlueTempNet | causal | C 1-4 | 111,749 | 0.637 | 0.708 | -0.071 [-0.108, -0.032] / [-0.141, -0.005] |  |
| BlueTempNet | causal | C 5-24 | 97,786 | 0.636 | 0.721 | -0.085 [-0.135, -0.038] / [-0.176, +0.008] |  |
| BlueTempNet | causal | C >= 25 | 23,891 | 0.661 | 0.647 | +0.014 [-0.044, +0.067] / [-0.115, +0.123] |  |

Does the gap move with the date? Gap at C = 0 by date bin (static evidence):

**wiki-RfA**

| bin | edges at C = 0 | gap |
| --- | ---: | ---: |
| 2003-04 | 533 | +0.033 [-0.034, +0.100] |
| 2005 | 1,198 | +0.110 [+0.052, +0.161] |
| 2006 | 2,405 | +0.157 [+0.120, +0.187] |
| 2007 | 2,814 | +0.178 [+0.147, +0.211] |
| 2008 | 1,727 | +0.194 [+0.156, +0.229] |
| 2009 | 1,124 | +0.227 [+0.185, +0.272] |
| 2010 | 678 | +0.231 [+0.185, +0.279] |
| 2011 | 481 | +0.156 [+0.072, +0.239] |
| 2012 | 422 | +0.201 [+0.130, +0.261] |
| 2013 | 246 | +0.142 [+0.044, +0.241] |

**Bitcoin OTC**

| bin | edges at C = 0 | gap |
| --- | ---: | ---: |
| 2010-11 | 3,383 | +0.155 [+0.047, +0.259] |
| 2012 | 2,533 | +0.014 [-0.054, +0.067] |
| 2013 | 3,568 | -0.034 [-0.071, +0.008] |
| 2014 | 955 | -0.075 [-0.127, -0.023] |
| 2015-16 | 217 | +0.066 [-0.003, +0.164] |

**Bitcoin Alpha**

| bin | edges at C = 0 | gap |
| --- | ---: | ---: |
| 2010-11 | 3,329 | +0.161 [+0.060, +0.266] |
| 2012 | 1,793 | +0.049 [-0.019, +0.110] |
| 2013 | 1,502 | -0.058 [-0.133, +0.028] |
| 2014-16 | 545 | -0.061 [-0.133, +0.014] |

**BlueTempNet**

| bin | edges at C = 0 | gap |
| --- | ---: | ---: |
| 2023-05..2023-06 | 258 | +0.227 [-0.003, +0.395] |
| 2023-07 | 1,421 | +0.111 [-0.019, +0.228] |
| 2023-08 | 1,724 | -0.028 [-0.098, +0.034] |
| 2023-09 | 1,106 | -0.044 [-0.153, +0.057] |
| 2023-10 | 1,055 | -0.003 [-0.108, +0.097] |
| 2023-11 | 851 | +0.027 [-0.067, +0.116] |
| 2023-12 | 1,738 | -0.130 [-0.192, -0.068] |
| 2024-01 | 1,190 | -0.115 [-0.188, -0.039] |
| 2024-02 | 6,434 | -0.084 [-0.131, -0.032] |
| 2024-03 | 1,557 | -0.092 [-0.142, -0.038] |
| 2024-04..2024-05 | 1,233 | -0.071 [-0.127, -0.020] |

## 8. Variations: model forms, and which fits best

Every variant is run through the same forward-chained protocol as T2 (person terms are the eight online columns unless the name says otherwise). **Balance features**: `bal_strict` is the one-column sum over triads of s(u,w) s(w,v) (Heider, all 16 types), `bal_weak` the same with the mm types set to 0 (Davis); `tri4` the four undirected types; `tri16` the 16 free types. **Status features**: `status` = the one-column sum of the oriented status rule over triads plus the node status difference sigma(v) - sigma(u) [L4801, L4802]. `recip` = the sign of the reverse tie when it is already in the evidence. `person_flex` adds squares and products of the person columns; `+interactions` adds the 16 log counts times the sender and receiver log-odds. `frozen_effects` is the other reading of a_i and b_j: one ridge-fitted effect per user, frozen at the end of each training window. Counts are raw or log, chosen once on the inner validation block. Sorted by pooled held-out log-loss; the best row of each site is in bold; the best of the registry's own forms (person plus balance, status or triad terms) is marked.

**wiki-RfA** (best by log-loss: person_flex+tri16+interactions+recip; by AUC: person_flex+tri16+interactions+recip)

| variant | params | counts | AUC | AUC minus person | log-loss | balanced acc. |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| **person_flex+tri16+interactions+recip** | 65 | log | 0.8840 | +0.0064 [+0.0051, +0.0076] | 0.3467 | 0.7967 |
| person_flex+tri16+interactions | 62 | log | 0.8832 | +0.0056 [+0.0044, +0.0068] | 0.3477 | 0.7951 |
| person+tri16+recip | 27 | log | 0.8827 | +0.0051 [+0.0039, +0.0063] | 0.3487 | 0.7958 |
| person+tri16+status (best registry form) | 26 | log | 0.8826 | +0.0050 [+0.0039, +0.0063] | 0.3488 | 0.7957 |
| person+bal_strict+status | 12 | log | 0.8824 | +0.0048 [+0.0037, +0.0058] | 0.3492 | 0.7951 |
| person+tri16 | 25 | log | 0.8822 | +0.0046 [+0.0034, +0.0058] | 0.3493 | 0.7946 |
| person+bal_weak+status | 12 | log | 0.8822 | +0.0046 [+0.0036, +0.0057] | 0.3496 | 0.7953 |
| person+tri4 | 13 | log | 0.8815 | +0.0039 [+0.0029, +0.0049] | 0.3503 | 0.7923 |
| person+bal_strict | 10 | log | 0.8810 | +0.0034 [+0.0023, +0.0044] | 0.3509 | 0.7929 |
| person+bal_weak | 10 | log | 0.8809 | +0.0033 [+0.0022, +0.0044] | 0.3512 | 0.7930 |
| person+status | 11 | log | 0.8784 | +0.0008 [+0.0005, +0.0010] | 0.3535 | 0.7896 |
| person_flex | 14 | raw | 0.8783 | +0.0007 [+0.0003, +0.0010] | 0.3537 | 0.7887 |
| person+recip | 11 | raw | 0.8783 | +0.0007 [+0.0003, +0.0011] | 0.3537 | 0.7891 |
| person | 9 | raw | 0.8776 | (reference) | 0.3544 | 0.7880 |
| tri16+status | 18 | log | 0.7979 | -0.0798 [-0.0836, -0.0754] | 0.4428 | 0.7301 |
| frozen_effects+tri16 | 22051 | ridge 8 | 0.7731 | -0.1046 [-0.1096, -0.0994] | 0.4574 | 0.7025 |
| tri16 | 17 | log | 0.7688 | -0.1089 [-0.1136, -0.1041] | 0.4622 | 0.7028 |
| tri4 | 5 | log | 0.7469 | -0.1307 [-0.1367, -0.1249] | 0.4711 | 0.6857 |
| bal_weak | 2 | log | 0.7174 | -0.1603 [-0.1675, -0.1533] | 0.4905 | 0.6732 |
| bal_strict | 2 | log | 0.6932 | -0.1845 [-0.1925, -0.1772] | 0.5025 | 0.6484 |
| status | 3 | log | 0.7072 | -0.1705 [-0.1773, -0.1629] | 0.5035 | 0.6592 |
| frozen_effects | 22035 | ridge 8 | 0.6139 | -0.2638 [-0.2756, -0.2511] | 0.5250 | 0.5810 |

**Bitcoin OTC** (best by log-loss: person_flex+tri16+interactions+recip; by AUC: person+tri16+recip)

| variant | params | counts | AUC | AUC minus person | log-loss | balanced acc. |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| **person_flex+tri16+interactions+recip** | 65 | log | 0.9230 | +0.0224 [+0.0152, +0.0306] | 0.2050 | 0.8060 |
| person+tri16+recip | 27 | log | 0.9258 | +0.0252 [+0.0196, +0.0314] | 0.2064 | 0.7849 |
| person+tri16+status (best registry form) | 26 | log | 0.9104 | +0.0097 [+0.0057, +0.0143] | 0.2244 | 0.7690 |
| person+bal_strict+status | 12 | log | 0.9098 | +0.0092 [+0.0058, +0.0129] | 0.2253 | 0.7699 |
| person+tri16 | 25 | log | 0.9107 | +0.0100 [+0.0061, +0.0143] | 0.2262 | 0.7630 |
| person_flex+tri16+interactions | 62 | log | 0.9081 | +0.0075 [+0.0018, +0.0131] | 0.2265 | 0.7788 |
| person+bal_weak+status | 12 | log | 0.9095 | +0.0089 [+0.0058, +0.0126] | 0.2268 | 0.7699 |
| person+recip | 11 | raw | 0.9192 | +0.0186 [+0.0151, +0.0224] | 0.2291 | 0.7748 |
| person+bal_strict | 10 | log | 0.9084 | +0.0077 [+0.0041, +0.0113] | 0.2313 | 0.7638 |
| person+bal_weak | 10 | log | 0.9081 | +0.0074 [+0.0040, +0.0108] | 0.2328 | 0.7630 |
| person+tri4 | 13 | raw | 0.9101 | +0.0094 [+0.0060, +0.0130] | 0.2366 | 0.7660 |
| person_flex | 14 | raw | 0.9006 | -0.0000 [-0.0016, +0.0019] | 0.2498 | 0.7474 |
| person+status | 11 | raw | 0.9016 | +0.0009 [-0.0014, +0.0030] | 0.2517 | 0.7531 |
| person | 9 | raw | 0.9007 | (reference) | 0.2535 | 0.7499 |
| tri16+status | 18 | log | 0.8439 | -0.0568 [-0.0753, -0.0389] | 0.2971 | 0.7700 |
| frozen_effects+tri16 | 11779 | ridge 8 | 0.8414 | -0.0592 [-0.0727, -0.0451] | 0.3036 | 0.7727 |
| tri16 | 17 | log | 0.8033 | -0.0974 [-0.1135, -0.0799] | 0.3209 | 0.7243 |
| tri4 | 5 | log | 0.8077 | -0.0930 [-0.1094, -0.0757] | 0.3227 | 0.7302 |
| bal_weak | 2 | log | 0.7609 | -0.1397 [-0.1665, -0.1159] | 0.3879 | 0.6302 |
| bal_strict | 2 | log | 0.7565 | -0.1442 [-0.1719, -0.1198] | 0.3916 | 0.6271 |
| frozen_effects | 11763 | ridge 8 | 0.6959 | -0.2048 [-0.2255, -0.1854] | 0.4139 | 0.6290 |
| status | 3 | raw | 0.7260 | -0.1747 [-0.2088, -0.1442] | 0.4147 | 0.6955 |

**Bitcoin Alpha** (best by log-loss: person+bal_strict+status; by AUC: person_flex+tri16+interactions+recip)

| variant | params | counts | AUC | AUC minus person | log-loss | balanced acc. |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| **person+bal_strict+status** | 12 | log | 0.8615 | +0.0062 [+0.0031, +0.0099] | 0.2042 | 0.7287 |
| person+bal_weak+status | 12 | log | 0.8614 | +0.0061 [+0.0031, +0.0098] | 0.2044 | 0.7290 |
| person+bal_strict | 10 | log | 0.8602 | +0.0049 [+0.0022, +0.0082] | 0.2094 | 0.7316 |
| person+bal_weak | 10 | log | 0.8601 | +0.0048 [+0.0021, +0.0080] | 0.2096 | 0.7314 |
| person_flex | 14 | raw | 0.8571 | +0.0018 [-0.0010, +0.0044] | 0.2097 | 0.7258 |
| person+recip | 11 | raw | 0.8639 | +0.0087 [+0.0045, +0.0137] | 0.2098 | 0.7406 |
| person+status | 11 | log | 0.8537 | -0.0015 [-0.0051, +0.0018] | 0.2101 | 0.7236 |
| person+tri4 | 13 | log | 0.8630 | +0.0077 [+0.0031, +0.0116] | 0.2102 | 0.7340 |
| person | 9 | raw | 0.8553 | (reference) | 0.2141 | 0.7269 |
| person_flex+tri16+interactions+recip | 65 | log | 0.8645 | +0.0092 [-0.0001, +0.0186] | 0.2182 | 0.7551 |
| person+tri16+recip | 27 | log | 0.8572 | +0.0019 [-0.0062, +0.0097] | 0.2188 | 0.7449 |
| person+tri16+status | 26 | log | 0.8495 | -0.0058 [-0.0140, +0.0008] | 0.2218 | 0.7319 |
| person+tri16 | 25 | log | 0.8494 | -0.0059 [-0.0136, +0.0007] | 0.2242 | 0.7323 |
| person_flex+tri16+interactions | 62 | log | 0.8490 | -0.0063 [-0.0158, +0.0027] | 0.2279 | 0.7317 |
| tri16+status | 18 | log | 0.7666 | -0.0886 [-0.1217, -0.0659] | 0.2767 | 0.6948 |
| tri4 | 5 | log | 0.7264 | -0.1289 [-0.1540, -0.1022] | 0.2853 | 0.6604 |
| frozen_effects+tri16 | 7583 | ridge 2 | 0.7488 | -0.1064 [-0.1257, -0.0882] | 0.2907 | 0.6851 |
| status | 3 | log | 0.7202 | -0.1350 [-0.1738, -0.1049] | 0.2915 | 0.6577 |
| tri16 | 17 | log | 0.7028 | -0.1524 [-0.1788, -0.1318] | 0.2967 | 0.6472 |
| frozen_effects | 7567 | ridge 2 | 0.7042 | -0.1511 [-0.1814, -0.1247] | 0.3149 | 0.6344 |
| bal_weak | 2 | log | 0.6156 | -0.2396 [-0.2881, -0.1914] | 0.3308 | 0.5384 |
| bal_strict | 2 | log | 0.6169 | -0.2384 [-0.2896, -0.1891] | 0.3309 | 0.5356 |

**BlueTempNet** (best by log-loss: person_flex+tri16+interactions+recip; by AUC: person_flex+tri16+interactions+recip)

| variant | params | counts | AUC | AUC minus person | log-loss | balanced acc. |
| --- | ---: | --- | ---: | ---: | ---: | ---: |
| **person_flex+tri16+interactions+recip** | 65 | log | 0.9662 | +0.0143 [+0.0126, +0.0158] | 0.1142 | 0.9037 |
| person+tri16+recip | 27 | log | 0.9653 | +0.0133 [+0.0117, +0.0148] | 0.1166 | 0.9038 |
| person_flex+tri16+interactions | 62 | log | 0.9613 | +0.0094 [+0.0080, +0.0106] | 0.1234 | 0.8967 |
| person+tri16+status (best registry form) | 26 | log | 0.9609 | +0.0089 [+0.0075, +0.0103] | 0.1253 | 0.8979 |
| person+tri16 | 25 | log | 0.9608 | +0.0088 [+0.0073, +0.0101] | 0.1256 | 0.8972 |
| person+bal_strict+status | 12 | log | 0.9597 | +0.0077 [+0.0065, +0.0088] | 0.1267 | 0.8937 |
| person+bal_weak+status | 12 | log | 0.9595 | +0.0075 [+0.0063, +0.0086] | 0.1277 | 0.8943 |
| person+tri4 | 13 | log | 0.9594 | +0.0075 [+0.0065, +0.0084] | 0.1281 | 0.8924 |
| person+bal_strict | 10 | log | 0.9586 | +0.0066 [+0.0057, +0.0075] | 0.1295 | 0.8905 |
| person+bal_weak | 10 | log | 0.9583 | +0.0063 [+0.0055, +0.0072] | 0.1307 | 0.8905 |
| person+recip | 11 | raw | 0.9569 | +0.0049 [+0.0042, +0.0058] | 0.1331 | 0.8846 |
| person_flex | 14 | raw | 0.9522 | +0.0002 [-0.0005, +0.0008] | 0.1394 | 0.8841 |
| person+status | 11 | log | 0.9528 | +0.0008 [+0.0004, +0.0011] | 0.1408 | 0.8809 |
| person | 9 | raw | 0.9520 | (reference) | 0.1421 | 0.8790 |
| tri16+status | 18 | log | 0.9217 | -0.0302 [-0.0329, -0.0274] | 0.1909 | 0.8328 |
| frozen_effects+tri16 | 30809 | ridge 0.5 | 0.9296 | -0.0224 [-0.0259, -0.0194] | 0.2031 | 0.8303 |
| tri16 | 17 | log | 0.8960 | -0.0560 [-0.0645, -0.0505] | 0.2105 | 0.7922 |
| tri4 | 5 | log | 0.8712 | -0.0808 [-0.0884, -0.0738] | 0.2378 | 0.7728 |
| frozen_effects | 30793 | ridge 0.5 | 0.8539 | -0.0981 [-0.1073, -0.0906] | 0.2616 | 0.7610 |
| bal_weak | 2 | log | 0.7934 | -0.1586 [-0.1782, -0.1390] | 0.2719 | 0.7284 |
| status | 3 | log | 0.8005 | -0.1515 [-0.1648, -0.1390] | 0.2824 | 0.7200 |
| bal_strict | 2 | log | 0.7723 | -0.1797 [-0.1990, -0.1602] | 0.2840 | 0.7096 |

### 8.1 Paired comparisons that answer the named questions

First minus second; AUC and log-loss differences with 95% intervals; and the AUC difference restricted to edges with C >= 5. A negative log-loss difference favours the first model.

**wiki-RfA**

| comparison | AUC | log-loss | AUC at C >= 5 |
| --- | ---: | ---: | ---: |
| weak minus strict balance (with person terms) | -0.0001 [-0.0003, +0.0001] | +0.0003 [-0.0001, +0.0006] | -0.0004 [-0.0008, -0.0000] |
| weak minus strict balance (alone) | +0.0242 [+0.0222, +0.0264] | -0.0120 [-0.0132, -0.0106] | +0.0229 [+0.0207, +0.0257] |
| status added to strict balance | +0.0014 [+0.0009, +0.0019] | -0.0016 [-0.0023, -0.0011] | +0.0027 [+0.0017, +0.0038] |
| status added to weak balance | +0.0013 [+0.0009, +0.0018] | -0.0016 [-0.0022, -0.0010] | +0.0027 [+0.0018, +0.0037] |
| status added to person terms | +0.0008 [+0.0005, +0.0010] | -0.0009 [-0.0012, -0.0006] | +0.0014 [+0.0006, +0.0020] |
| status added to the 16 types | +0.0004 [+0.0002, +0.0007] | -0.0006 [-0.0009, -0.0003] | +0.0005 [+0.0000, +0.0010] |
| status added to the 16 types (no person terms) | +0.0291 [+0.0256, +0.0328] | -0.0194 [-0.0221, -0.0164] | +0.0039 [+0.0008, +0.0066] |
| 16 types minus status (no person terms) | +0.0616 [+0.0517, +0.0706] | -0.0414 [-0.0474, -0.0349] | +0.1270 [+0.1146, +0.1407] |
| 16 free types minus weak balance | +0.0013 [+0.0007, +0.0020] | -0.0018 [-0.0026, -0.0010] | +0.0029 [+0.0015, +0.0041] |
| 16 directed types minus 4 undirected types | +0.0008 [+0.0002, +0.0012] | -0.0009 [-0.0015, -0.0002] | +0.0019 [+0.0007, +0.0031] |
| 4 undirected types minus weak balance | +0.0006 [+0.0001, +0.0011] | -0.0009 [-0.0016, -0.0002] | +0.0010 [-0.0002, +0.0020] |
| strict balance added to person terms | +0.0034 [+0.0023, +0.0044] | -0.0035 [-0.0048, -0.0023] | +0.0061 [+0.0040, +0.0083] |
| weak balance added to person terms | +0.0033 [+0.0022, +0.0044] | -0.0033 [-0.0046, -0.0020] | +0.0057 [+0.0038, +0.0079] |
| 16 types added to person terms (G) | +0.0046 [+0.0034, +0.0058] | -0.0051 [-0.0066, -0.0037] | +0.0086 [+0.0062, +0.0113] |
| reverse-tie sign added to person terms | +0.0007 [+0.0003, +0.0011] | -0.0007 [-0.0011, -0.0002] | +0.0011 [+0.0001, +0.0020] |
| reverse-tie sign added to the 16 types | +0.0005 [+0.0002, +0.0007] | -0.0006 [-0.0009, -0.0003] | +0.0009 [+0.0004, +0.0014] |
| flexible person terms minus person terms | +0.0007 [+0.0003, +0.0010] | -0.0008 [-0.0012, -0.0003] | +0.0008 [+0.0002, +0.0014] |
| 16 types + interactions added to flexible person terms | +0.0049 [+0.0036, +0.0062] | -0.0059 [-0.0075, -0.0044] | +0.0081 [+0.0052, +0.0109] |
| frozen user effects minus online person terms | -0.2638 [-0.2756, -0.2511] | +0.1705 [+0.1627, +0.1783] | -0.2211 [-0.2375, -0.2046] |

**Bitcoin OTC**

| comparison | AUC | log-loss | AUC at C >= 5 |
| --- | ---: | ---: | ---: |
| weak minus strict balance (with person terms) | -0.0003 [-0.0005, -0.0001] | +0.0015 [+0.0010, +0.0021] | -0.0013 [-0.0020, -0.0007] |
| weak minus strict balance (alone) | +0.0045 [+0.0028, +0.0061] | -0.0038 [-0.0051, -0.0024] | +0.0018 [-0.0009, +0.0042] |
| status added to strict balance | +0.0014 [-0.0007, +0.0034] | -0.0060 [-0.0104, -0.0018] | +0.0076 [+0.0002, +0.0143] |
| status added to weak balance | +0.0015 [-0.0005, +0.0034] | -0.0060 [-0.0104, -0.0018] | +0.0077 [+0.0005, +0.0144] |
| status added to person terms | +0.0009 [-0.0014, +0.0030] | -0.0018 [-0.0052, +0.0012] | -0.0028 [-0.0187, +0.0082] |
| status added to the 16 types | -0.0003 [-0.0011, +0.0007] | -0.0018 [-0.0046, +0.0007] | +0.0003 [-0.0012, +0.0019] |
| status added to the 16 types (no person terms) | +0.0406 [+0.0266, +0.0538] | -0.0238 [-0.0319, -0.0155] | +0.0056 [-0.0017, +0.0132] |
| 16 types minus status (no person terms) | +0.0773 [+0.0432, +0.1141] | -0.0938 [-0.1537, -0.0485] | +0.2647 [+0.2076, +0.3239] |
| 16 free types minus weak balance | +0.0026 [-0.0001, +0.0053] | -0.0066 [-0.0123, -0.0011] | +0.0082 [+0.0005, +0.0155] |
| 16 directed types minus 4 undirected types | +0.0006 [-0.0014, +0.0026] | -0.0104 [-0.0157, -0.0058] | +0.0049 [-0.0001, +0.0101] |
| 4 undirected types minus weak balance | +0.0020 [+0.0002, +0.0044] | +0.0038 [-0.0037, +0.0107] | +0.0033 [-0.0045, +0.0100] |
| strict balance added to person terms | +0.0077 [+0.0041, +0.0113] | -0.0222 [-0.0288, -0.0162] | +0.0246 [+0.0140, +0.0362] |
| weak balance added to person terms | +0.0074 [+0.0040, +0.0108] | -0.0207 [-0.0269, -0.0151] | +0.0233 [+0.0131, +0.0347] |
| 16 types added to person terms (G) | +0.0100 [+0.0061, +0.0143] | -0.0273 [-0.0359, -0.0198] | +0.0315 [+0.0164, +0.0460] |
| reverse-tie sign added to person terms | +0.0186 [+0.0151, +0.0224] | -0.0243 [-0.0292, -0.0198] | +0.0148 [+0.0055, +0.0255] |
| reverse-tie sign added to the 16 types | +0.0152 [+0.0120, +0.0187] | -0.0198 [-0.0235, -0.0165] | +0.0046 [+0.0010, +0.0090] |
| flexible person terms minus person terms | -0.0000 [-0.0016, +0.0019] | -0.0037 [-0.0078, -0.0007] | -0.0080 [-0.0134, -0.0029] |
| 16 types + interactions added to flexible person terms | +0.0075 [+0.0014, +0.0131] | -0.0233 [-0.0316, -0.0146] | +0.0262 [+0.0063, +0.0433] |
| frozen user effects minus online person terms | -0.2048 [-0.2255, -0.1854] | +0.1605 [+0.1317, +0.1918] | -0.2679 [-0.3080, -0.2171] |

**Bitcoin Alpha**

| comparison | AUC | log-loss | AUC at C >= 5 |
| --- | ---: | ---: | ---: |
| weak minus strict balance (with person terms) | -0.0001 [-0.0002, +0.0000] | +0.0002 [+0.0001, +0.0004] | -0.0004 [-0.0008, +0.0001] |
| weak minus strict balance (alone) | -0.0012 [-0.0041, +0.0019] | -0.0001 [-0.0006, +0.0003] | +0.0018 [-0.0067, +0.0081] |
| status added to strict balance | +0.0013 [-0.0016, +0.0042] | -0.0051 [-0.0096, -0.0018] | +0.0048 [-0.0023, +0.0119] |
| status added to weak balance | +0.0013 [-0.0016, +0.0043] | -0.0052 [-0.0097, -0.0018] | +0.0048 [-0.0022, +0.0119] |
| status added to person terms | -0.0015 [-0.0051, +0.0018] | -0.0041 [-0.0083, -0.0009] | -0.0009 [-0.0097, +0.0080] |
| status added to the 16 types | +0.0001 [-0.0020, +0.0022] | -0.0024 [-0.0051, -0.0003] | +0.0008 [-0.0023, +0.0036] |
| status added to the 16 types (no person terms) | +0.0638 [+0.0423, +0.0839] | -0.0200 [-0.0273, -0.0132] | +0.0216 [+0.0076, +0.0381] |
| 16 types minus status (no person terms) | -0.0174 [-0.0477, +0.0159] | +0.0053 [-0.0082, +0.0169] | +0.0904 [+0.0465, +0.1431] |
| 16 free types minus weak balance | -0.0107 [-0.0175, -0.0046] | +0.0146 [+0.0094, +0.0197] | -0.0175 [-0.0341, +0.0008] |
| 16 directed types minus 4 undirected types | -0.0136 [-0.0205, -0.0071] | +0.0140 [+0.0092, +0.0186] | -0.0270 [-0.0428, -0.0113] |
| 4 undirected types minus weak balance | +0.0029 [-0.0001, +0.0055] | +0.0006 [-0.0020, +0.0030] | +0.0094 [-0.0002, +0.0211] |
| strict balance added to person terms | +0.0049 [+0.0022, +0.0082] | -0.0048 [-0.0074, -0.0025] | +0.0101 [+0.0034, +0.0189] |
| weak balance added to person terms | +0.0048 [+0.0021, +0.0080] | -0.0045 [-0.0070, -0.0023] | +0.0097 [+0.0031, +0.0184] |
| 16 types added to person terms (G) | -0.0059 [-0.0136, +0.0007] | +0.0100 [+0.0037, +0.0155] | -0.0078 [-0.0259, +0.0147] |
| reverse-tie sign added to person terms | +0.0087 [+0.0045, +0.0137] | -0.0043 [-0.0080, -0.0008] | +0.0111 [+0.0034, +0.0206] |
| reverse-tie sign added to the 16 types | +0.0078 [+0.0026, +0.0135] | -0.0054 [-0.0095, -0.0013] | +0.0078 [-0.0045, +0.0197] |
| flexible person terms minus person terms | +0.0018 [-0.0010, +0.0044] | -0.0044 [-0.0085, -0.0013] | +0.0021 [-0.0031, +0.0084] |
| 16 types + interactions added to flexible person terms | -0.0081 [-0.0174, +0.0009] | +0.0182 [+0.0083, +0.0262] | -0.0309 [-0.0544, -0.0040] |
| frozen user effects minus online person terms | -0.1511 [-0.1814, -0.1247] | +0.1008 [+0.0719, +0.1342] | -0.1819 [-0.2331, -0.1288] |

**BlueTempNet**

| comparison | AUC | log-loss | AUC at C >= 5 |
| --- | ---: | ---: | ---: |
| weak minus strict balance (with person terms) | -0.0003 [-0.0003, -0.0002] | +0.0012 [+0.0009, +0.0016] | -0.0002 [-0.0003, -0.0001] |
| weak minus strict balance (alone) | +0.0211 [+0.0184, +0.0244] | -0.0122 [-0.0145, -0.0100] | +0.0139 [+0.0112, +0.0174] |
| status added to strict balance | +0.0011 [+0.0005, +0.0017] | -0.0028 [-0.0036, -0.0020] | +0.0009 [+0.0001, +0.0017] |
| status added to weak balance | +0.0012 [+0.0005, +0.0017] | -0.0030 [-0.0039, -0.0022] | +0.0009 [+0.0001, +0.0017] |
| status added to person terms | +0.0008 [+0.0004, +0.0011] | -0.0013 [-0.0018, -0.0006] | +0.0003 [-0.0002, +0.0008] |
| status added to the 16 types | +0.0002 [+0.0001, +0.0002] | -0.0003 [-0.0004, -0.0002] | +0.0000 [-0.0001, +0.0001] |
| status added to the 16 types (no person terms) | +0.0258 [+0.0202, +0.0335] | -0.0196 [-0.0227, -0.0161] | +0.0010 [-0.0001, +0.0020] |
| 16 types minus status (no person terms) | +0.0954 [+0.0763, +0.1120] | -0.0719 [-0.0793, -0.0627] | +0.1369 [+0.1192, +0.1594] |
| 16 free types minus weak balance | +0.0024 [+0.0018, +0.0032] | -0.0051 [-0.0066, -0.0039] | +0.0035 [+0.0027, +0.0044] |
| 16 directed types minus 4 undirected types | +0.0013 [+0.0007, +0.0019] | -0.0025 [-0.0035, -0.0015] | +0.0017 [+0.0010, +0.0024] |
| 4 undirected types minus weak balance | +0.0011 [+0.0006, +0.0016] | -0.0027 [-0.0037, -0.0018] | +0.0018 [+0.0012, +0.0025] |
| strict balance added to person terms | +0.0066 [+0.0057, +0.0075] | -0.0126 [-0.0140, -0.0109] | +0.0020 [+0.0012, +0.0027] |
| weak balance added to person terms | +0.0063 [+0.0055, +0.0072] | -0.0113 [-0.0127, -0.0098] | +0.0018 [+0.0010, +0.0026] |
| 16 types added to person terms (G) | +0.0088 [+0.0073, +0.0101] | -0.0164 [-0.0183, -0.0143] | +0.0053 [+0.0041, +0.0065] |
| reverse-tie sign added to person terms | +0.0049 [+0.0042, +0.0058] | -0.0090 [-0.0102, -0.0079] | +0.0032 [+0.0023, +0.0042] |
| reverse-tie sign added to the 16 types | +0.0046 [+0.0038, +0.0053] | -0.0090 [-0.0102, -0.0076] | +0.0034 [+0.0026, +0.0042] |
| flexible person terms minus person terms | +0.0002 [-0.0005, +0.0008] | -0.0027 [-0.0040, -0.0014] | -0.0012 [-0.0017, -0.0006] |
| 16 types + interactions added to flexible person terms | +0.0092 [+0.0081, +0.0103] | -0.0159 [-0.0176, -0.0139] | +0.0072 [+0.0058, +0.0086] |
| frozen user effects minus online person terms | -0.0981 [-0.1073, -0.0906] | +0.1195 [+0.1077, +0.1331] | -0.0663 [-0.0768, -0.0584] |

### 8.2 Restricting to edges with C >= 5

The same ranking on the edges that have triad evidence (best of all variants and best registry form by log-loss, and G):

| site | edges | best by log-loss | best registry form | AUC person | AUC both | G |
| --- | ---: | --- | --- | ---: | ---: | ---: |
| wiki-RfA | 46,443 | person_flex+tri16+interactions+recip | person+tri16+status | 0.864 | 0.873 | +0.0086 [+0.0062, +0.0113] |
| Bitcoin OTC | 2,937 | person+bal_strict+status | person+bal_strict+status | 0.910 | 0.942 | +0.0315 [+0.0164, +0.0460] |
| Bitcoin Alpha | 2,230 | person+bal_strict+status | person+bal_strict+status | 0.878 | 0.871 | -0.0078 [-0.0259, +0.0147] |
| BlueTempNet | 80,393 | person_flex+tri16+interactions+recip | person+tri16+status | 0.968 | 0.974 | +0.0053 [+0.0041, +0.0065] |

## 9. The null, and what the test could have found

**Why a null is needed.** Triad counts are built from the same ties as the person terms, so G is not zero when nothing but person propensities generated the signs: the counts carry extra (noisy) information about users' propensities, such as how a user is treated as a receiver when the question concerns their behaviour as a sender. The right comparison for G, and for the forward-chain coefficients, is therefore not zero but what a world with person propensities only would give.

**The person-only world.** The real network skeleton (who rates whom, and when) is kept; the signs are redrawn from a period intercept plus one ridge-fitted effect per sender and per receiver, with the ridge tuned so that the online person model reaches the same held-out AUC it reached on the real signs; each redrawn world goes through the whole pipeline. Two further worlds add a planted forward-chain mechanism of known size on top of the same person terms (FFpp +, FFpm -, FFmp -, FFmm - by 0.1 or 0.3 log-odds per triad; the signs are drawn in time order from the counts of the signs already drawn).

| site | ridge | person AUC: real / null world | G observed | G, person-only world (sd) | z | p | G, planted 0.1 | G, planted 0.3 | G at C >= 5 | null at C >= 5 | z |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| wiki-RfA | 0.076 | 0.8776 / 0.8772 | +0.0046 | +0.0004 (0.0002) | +18.8 | 0.048 | +0.0022 | +0.0085 | +0.0086 | +0.0003 | +17.4 |
| Bitcoin OTC | 0.0438 | 0.9007 / 0.9020 | +0.0100 | -0.0009 (0.0008) | +13.3 | 0.048 | +0.0001 | +0.0036 | +0.0315 | -0.0068 | +12.3 |
| Bitcoin Alpha | 0.14 | 0.8553 / 0.8572 | -0.0059 | -0.0050 (0.0022) | -0.4 | 0.714 | -0.0018 | +0.0046 | -0.0078 | -0.0166 | +1.0 |
| BlueTempNet | 0.12 | 0.9520 / 0.9535 | +0.0088 | +0.0008 (0.0001) | +60.6 | 0.048 | +0.0025 | +0.0051 | +0.0053 | +0.0003 | +23.9 |

Replicates: 20 person-only, 8 per planted size. z = (observed - null mean) / null sd; p = share of null replicates at or above the observation (with +1). The null sd is the spread of G over redrawn signs with the generator's person effects held fixed, 3 to 10 times narrower than the two-way bootstrap spread of the observed G (section 4), so z measures distance from this generator rather than the precision of G; the observed G's two-way interval lies above the null mean at wiki-RfA, Bitcoin OTC and BlueTempNet. The generator's effects are fitted on every edge with a light ridge (in-sample AUC on the real signs 0.94 at wiki-RfA, 0.99 at Bitcoin OTC, 0.99 at Bitcoin Alpha, 0.99 at BlueTempNet), so the person-only world inherits much of the real sign pattern; it is static, and has no reciprocity beyond person effects (added at review).

### 9.1 The forward-chain pattern in the person-only world

Mean forward-chain coefficients over the person-only replicates (sd in brackets), against the observed ones. If the pattern of the 16 types alone (static) appears here it needs no mechanism.

| site | fit | FFpp: observed vs null | FFpm: observed vs null | FFmp: observed vs null | FFmm: observed vs null |
| --- | --- | ---: | ---: | ---: | ---: |
| wiki-RfA | static, 16 types alone | +0.21 vs +0.18 (0.00), z +11.1 | -0.24 vs -0.18 (0.00), z -14.7 | -0.18 vs -0.13 (0.00), z -11.3 | -0.48 vs -0.58 (0.01), z +7.9 |
| wiki-RfA | static, + person terms | +0.06 vs +0.01 (0.00), z +24.9 | -0.09 vs -0.01 (0.00), z -18.2 | -0.10 vs -0.03 (0.00), z -14.2 | +0.01 vs -0.04 (0.01), z +5.3 |
| wiki-RfA | causal, 16 types alone | +0.35 vs +0.32 (0.00), z +6.0 | -0.40 vs -0.34 (0.01), z -6.9 | -0.27 vs -0.20 (0.01), z -8.7 | -0.72 vs -0.86 (0.03), z +4.7 |
| wiki-RfA | causal, + person terms | +0.09 vs +0.04 (0.00), z +16.2 | -0.12 vs -0.03 (0.01), z -12.1 | -0.12 vs -0.06 (0.01), z -8.0 | +0.03 vs -0.06 (0.02), z +4.2 |
| Bitcoin OTC | static, 16 types alone | +0.04 vs +0.05 (0.03), z -0.3 | -0.66 vs -0.39 (0.05), z -6.0 | -0.88 vs -0.38 (0.04), z -12.6 | -0.18 vs -0.76 (0.08), z +7.2 |
| Bitcoin OTC | static, + person terms | -0.01 vs -0.01 (0.02), z -0.2 | -0.42 vs -0.14 (0.03), z -10.2 | -0.44 vs -0.05 (0.04), z -10.8 | +0.02 vs +0.02 (0.03), z +0.2 |
| Bitcoin OTC | causal, 16 types alone | +0.23 vs +0.22 (0.04), z +0.1 | -1.28 vs -0.53 (0.09), z -8.0 | -1.55 vs -0.60 (0.11), z -8.4 | +0.03 vs -1.38 (0.20), z +7.1 |
| Bitcoin OTC | causal, + person terms | +0.13 vs +0.08 (0.03), z +1.4 | -0.50 vs +0.00 (0.06), z -8.3 | -0.78 vs -0.08 (0.05), z -12.8 | +0.20 vs +0.13 (0.07), z +0.9 |
| Bitcoin Alpha | static, 16 types alone | +0.04 vs +0.02 (0.05), z +0.5 | -0.59 vs -0.43 (0.07), z -2.4 | -0.55 vs -0.30 (0.05), z -4.7 | -0.46 vs -0.80 (0.11), z +3.1 |
| Bitcoin Alpha | static, + person terms | +0.01 vs -0.03 (0.03), z +1.5 | -0.30 vs -0.08 (0.05), z -5.0 | -0.31 vs -0.09 (0.05), z -4.8 | -0.06 vs +0.02 (0.08), z -1.0 |
| Bitcoin Alpha | causal, 16 types alone | +0.17 vs +0.17 (0.07), z +0.1 | -0.77 vs -0.38 (0.18), z -2.2 | -0.60 vs -0.30 (0.14), z -2.2 | +0.48 vs -1.02 (0.35), z +4.2 |
| Bitcoin Alpha | causal, + person terms | +0.06 vs +0.03 (0.06), z +0.5 | +0.02 vs +0.05 (0.13), z -0.2 | -0.37 vs -0.03 (0.13), z -2.7 | +0.64 vs +0.10 (0.13), z +4.0 |
| BlueTempNet | static, 16 types alone | +0.27 vs +0.16 (0.01), z +18.5 | -0.11 vs -0.07 (0.01), z -6.6 | -0.15 vs -0.13 (0.01), z -2.0 | -0.50 vs -0.73 (0.03), z +8.7 |
| BlueTempNet | static, + person terms | +0.07 vs +0.01 (0.00), z +23.5 | -0.05 vs -0.00 (0.00), z -10.1 | +0.00 vs -0.00 (0.00), z +2.3 | +0.11 vs +0.05 (0.01), z +6.5 |
| BlueTempNet | causal, 16 types alone | +0.38 vs +0.31 (0.01), z +4.6 | -0.28 vs -0.22 (0.02), z -3.1 | -0.46 vs -0.35 (0.01), z -9.7 | -0.84 vs -1.16 (0.06), z +5.8 |
| BlueTempNet | causal, + person terms | +0.07 vs +0.03 (0.01), z +5.4 | -0.07 vs -0.01 (0.01), z -4.2 | -0.01 vs +0.01 (0.01), z -3.7 | +0.21 vs +0.13 (0.02), z +5.1 |

### 9.2 Planted mechanisms: recovered?

Mean person-adjusted coefficients over the replicates with a planted mechanism (the planted values are +0.1/-0.1/-0.1/-0.1 and +0.3/-0.3/-0.3/-0.3), and the held-out gain G they produced. Two things follow. A mechanism of 0.3 per triad, the size of the triad-only coefficients, adds very little AUC on these skeletons, which is the sensitivity of the test. And the static design attenuates a mechanism that acts from earlier ties on later ones, because the later edges it counts are noise to an earlier tie: it returns a fraction of the planted size where the causal design returns all of it, so coefficient sizes are comparable with planted sizes only in the causal rows. FFmm is also poorly supported on the small Bitcoin skeletons, where even a planted -0.3 does not come back.

| site | world | fit | FFpp | FFpm | FFmp | FFmm | G (sd) | G at C >= 5 |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| wiki-RfA | planted 0.1 | causal, + person | +0.13 | -0.11 | -0.15 | -0.16 | +0.0022 (0.0002) | +0.0038 |
| wiki-RfA | planted 0.1 | static, + person | +0.04 | -0.03 | -0.05 | -0.06 | +0.0022 (0.0002) | +0.0038 |
| wiki-RfA | planted 0.3 | causal, + person | +0.30 | -0.28 | -0.31 | -0.33 | +0.0085 (0.0003) | +0.0152 |
| wiki-RfA | planted 0.3 | static, + person | +0.07 | -0.07 | -0.08 | -0.09 | +0.0085 (0.0003) | +0.0152 |
| Bitcoin OTC | planted 0.1 | causal, + person | +0.17 | -0.12 | -0.24 | +0.11 | +0.0001 (0.0011) | -0.0046 |
| Bitcoin OTC | planted 0.1 | static, + person | +0.03 | -0.16 | -0.12 | +0.00 | +0.0001 (0.0011) | -0.0046 |
| Bitcoin OTC | planted 0.3 | causal, + person | +0.34 | -0.29 | -0.45 | -0.04 | +0.0036 (0.0012) | +0.0047 |
| Bitcoin OTC | planted 0.3 | static, + person | +0.07 | -0.19 | -0.19 | -0.01 | +0.0036 (0.0012) | +0.0047 |
| Bitcoin Alpha | planted 0.1 | causal, + person | +0.11 | -0.07 | -0.19 | +0.10 | -0.0018 (0.0027) | -0.0069 |
| Bitcoin Alpha | planted 0.1 | static, + person | -0.00 | -0.11 | -0.09 | +0.07 | -0.0018 (0.0027) | -0.0069 |
| Bitcoin Alpha | planted 0.3 | causal, + person | +0.28 | -0.28 | -0.41 | -0.18 | +0.0046 (0.0027) | +0.0060 |
| Bitcoin Alpha | planted 0.3 | static, + person | +0.05 | -0.14 | -0.15 | +0.09 | +0.0046 (0.0027) | +0.0060 |
| BlueTempNet | planted 0.1 | causal, + person | +0.16 | -0.11 | -0.07 | +0.04 | +0.0025 (0.0001) | +0.0020 |
| BlueTempNet | planted 0.1 | static, + person | +0.05 | -0.02 | -0.01 | +0.05 | +0.0025 (0.0001) | +0.0020 |
| BlueTempNet | planted 0.3 | causal, + person | +0.38 | -0.26 | -0.22 | -0.14 | +0.0051 (0.0002) | +0.0041 |
| BlueTempNet | planted 0.3 | static, + person | +0.09 | -0.03 | -0.02 | +0.03 | +0.0051 (0.0002) | +0.0041 |

## 10. Caveats

- **Four sites, three media, two eras.** Bitcoin OTC and Alpha are two views of one market (2010-16); wiki-RfA is public voting on one wiki (2003-13); BlueTempNet is Bluesky follows and blocks (2023-24) in the creator graph only. The registry's R-E was checked on 1999-2009 sites; nothing here is a re-estimate on those. Magnitudes are per site and per period [L4857, L4859].
- **The signs mean different things.** A Bitcoin rating follows a trade; an RfA vote is public, consequential and strategic; a block is partly a safety tool and a follow is not affect [L4567, L4823; 117 section 3.6]. No site records a drive.
- **Person terms are measured, not known.** The online person columns are noisy estimates of a_i and b_j from earlier ties; the triad counts add some information about the same users. That is why the person-only world is needed, and it assumes static person effects: if users' propensities drift, a triad-only gain over a static world could be a recent-behaviour gain, not a mechanism.
- **Controlling for person terms is not innocent.** If a triad mechanism shaped the earlier ties, it also shaped the person histories, so person-adjusted triad coefficients are lower bounds on a mechanism that acts through both; the claim made is predictive (what triad counts add to held-out accuracy given person histories), not causal.
- **Static against causal coefficients.** A mechanism that acts from earlier ties on later ones is attenuated in a static fit, because the later edges it counts are noise to an earlier tie: a planted 0.3 per triad comes back as 0.07 to 0.09 in the static fit and 0.28 to 0.33 in the causal fit at wiki-RfA (section 9.2). LHK's design is static, so its coefficients (and the R1 rows labelled static) understate such a mechanism by a factor of three or four; the causal rows do not, and they agree with the static ones on every sign that matters here (FFmm is not negative once person terms are in).
- **Insensitivity of the AUC increment.** A forward-chain mechanism of 0.3 log-odds per triad, planted on the real skeletons, adds only a few thousandths of AUC, because most edges have little or no triad evidence (section 1). G < 0.02 does not exclude a per-triad effect of that size; the coefficients and the strata at C >= 5 are the better guides, and R2 as pre-registered is the less sensitive instrument.
- **Additive logistic forms only.** The registry's R-E is additive in the logit; nonlinear learners (trees, embeddings; Chiang et al. found low-rank global methods beat local triad methods [L4864]) were not tried, and global structure beyond common neighbours is outside the registry's form.
- **Time resolution.** Bitcoin Alpha's times are coarse (about 1,650 distinct values for 24,186 ratings), so the causal rule discards same-day evidence there; wiki-RfA times are to the minute but voters in one election are partly simultaneous.
- **wiki-RfA reciprocal pairs are not replies.** A voter and a candidate who each voted on the other did so in two different elections, years apart; the T4 share there is a different thing from a trader's reply.
- **Interval method.** Percentile intervals from 300 bootstrap replicates; null replicates number 20 (person-only) and 8 per planted size, so null means carry visible Monte Carlo error, shown as the sd, and the smallest possible p is 1/21.
- **Multiplicity and thresholds** (added at review). R1 to R5 are per-test rules (|z| beyond 1.96, 95% intervals) applied without a family-wise correction across four sites, four forward chains, two evidence rules, two fits, two clusterings and the per-bin calls of T3. Claims that rest on one marginal z would not survive a Bonferroni correction over the sixteen forward-chain cells of one fit (|z| above 2.96): FFmm in the 16-type fit alone at Bitcoin Alpha (z -2.5 / -2.8); FFmm positive with person terms at BlueTempNet on the two-way rule (z +2.7). R2's NO is the conservative direction, but its 0.02 threshold is a gain in balanced-accuracy points that LHK's figure shows by eye (about +-0.02) over a different baseline [L4829], used here as an AUC gain. With the same intervals R2 would read MIXED at a threshold of 0.0088 or below and YES at 0.0046 or below. The variant rankings of section 8 are chosen on the same test window they are scored on, so the order of close variants is optimistic.

## 11. Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.sign_registry_battery fetch            # missing sources, sha256-checked
    for s in wiki otc alpha bsky; do ~/.local/bin/uv run python -m models.sign_registry_battery compute $s --workers 3; done
    ~/.local/bin/uv run python -m models.sign_registry_battery report
    ~/.local/bin/uv run pytest tests/test_sign_registry_battery.py

`compute` is seeded and takes minutes to tens of minutes per site (BlueTempNet longest; most of it is the null replicates). Statistics are cached under `sim/data/sign_registry_battery_cache/` (git-ignored, with the data); `report` rewrites this file from them. The Bluesky sources are fetched from the authors' public GitHub LFS endpoint (`fetch bsky`, 221 MB, checksum-verified).


## Review (2026-11-01)

Independent review, same day, before commit. Nothing was re-tuned: no threshold, seed, protocol or cached statistic changed. The sections above were regenerated from the unchanged cache after the wording fixes listed below.

**Re-run.** `cd sim && ~/.local/bin/uv run pytest tests/test_sign_registry_battery.py`: 91 passed and 11 strict xfails as found; 93 passed and 11 strict xfails after (two tests added). With the code as found, `report` reproduced this file byte for byte from the cache.

**Headline numbers re-derived.**

- *Independently.* Only the loaders were shared; the triad counts came from my own sparse row products, the fit from my own logistic objective and the intervals from my own cluster sandwich. FFmm in the 16-type fit alone, static: -0.4759 (z -21.24), -0.1850 (-1.82), -0.4581 (-2.50), -0.5036 (-8.05) at wiki-RfA, Bitcoin OTC, Bitcoin Alpha and BlueTempNet. With person terms: +0.0131 (+0.82), +0.0228 (+0.34), -0.0590 (-0.31), +0.1087 (+3.43). FFmm support: 26,817, 1,031, 562, 16,143. T4 opposite-sign share: 0.1456, 0.0254, 0.0246, 0.0412 of 5,954, 14,100, 10,062 and 65,553 pairs. T5 static gap at C = 0: +0.1769, -0.0203, -0.0005, -0.0598. All equal the cache to the digits shown.
- *With the current code, against the cache.* T2 is identical at all four sites: fold bounds, transform choices, the pooled AUCs (recounted with an independent Mann-Whitney sum), and D, G and G at C >= 5 with their one-way and two-way B = 300 intervals. The person-only null is identical at Bitcoin OTC and Alpha: the calibration grid, the ridge (0.0438, 0.140), the generator AUC, and replicate 0 of the person-only and planted-0.3 worlds. The 20-replicate nulls at wiki-RfA and BlueTempNet, most of the original 12- and 26-minute computes, were not re-run.

**Checks.**

- *The null* is the right kind for the question and is implemented as described. It keeps the real skeleton, uses a period intercept plus ridge sender and receiver effects, and tunes the ridge to the real held-out person AUC (null worlds reach 0.877, 0.902, 0.857 and 0.954 against 0.878, 0.901, 0.855 and 0.952). Two properties are now stated in section 9. First, its replicate sd holds the generator fixed and is 3 to 10 times narrower than the bootstrap spread of the observed G, so a z of +13 to +61 measures distance from this generator, not precision; the two-way interval of G still clears the null mean at the same three sites. Second, its effects are in-sample fits (AUC 0.94 to 0.99 on the real signs), static, with no reciprocity beyond person effects.
- *Leakage:* none found. Causal features use strictly earlier edges only (the prefix identity is tested on constructed data and on Alpha); fold edges never split a timestamp; transforms are chosen on the 30-40% block; standardisation, BA thresholds and frozen effects come from training rows. Section 4.3 uses later edges by design, as LHK did, and says so.
- *Multiple comparisons:* no correction is applied, which is now stated in section 10 with what a Bonferroni correction over the sixteen forward-chain cells would lose: FFmm alone at Bitcoin Alpha, and FFmm positive at BlueTempNet on the two-way rule. No main verdict rests on either. R2's NO rests on its threshold: with the same intervals it reads MIXED at 0.0088 or below and YES at 0.0046 or below. The threshold carries LHK's balanced-accuracy gain, read by eye (L4829, `sa`), over to AUC.
- *Data and terms:* all four sources are git-ignored and sha256-checked, and only `data/README.md` is tracked. The results hold statistics only (no names, ids, text or `@`). wiki-RfA comments are skipped before decoding and names are integer-coded in memory. The README's wiki-RfA and Bitcoin "Used by" lists did not name this battery; it is now added to both.
- *Ledger ids:* all 54 cited ids exist and say what the code assumes, except one: "a follow is interest and a block is partly a safety tool" was cited to L4593, which does not say it. The source is 117 section 3.6, which is now cited.

**Changed in the code** (`verdict_text` and the report sections, with assertions on each new claim).

1. *T5.* "Absent" was read from the receiver-cluster rule alone, while "supported" needed both rules. Bitcoin OTC (two-way [-0.14, +0.11]) is therefore now undecided: absent on one rule only (`r5_both`, with tests).
2. *T1 wording.* With person terms, "FFmm is not negative at any site" was wrong for Alpha, whose estimate is -0.06; it now reads "not significantly negative", and FFpp likewise. The R1 refutation at BlueTempNet is now stated, with the person-only world's +0.05 beside it.
3. *Headline.* "No" is now "No by the pre-registered rule (R2)", and "small residue" is calibrated. A planted forward-chain mechanism of 0.3 log-odds per triad adds only 0.4 to 1.0 AUC points above the null on these networks, and the residue exceeds that at Bitcoin OTC and BlueTempNet. The first-outcome paragraph follows suit.
4. *Refuted list.* It cited R2 (G) as the evidence for a claim about D; the two are now separate items.
5. *Balance variants.* Strict and weak balance with person terms were called "indistinguishable", but strict leads by 0.0003 AUC with the interval excluding 0 at Bitcoin OTC and BlueTempNet; the text now says so.
6. *Smaller fixes.* The power sentence no longer calls wiki-RfA's -0.33 attenuated. The scoreboard says which intervals are two-way. Section 4.3 says LHK's gains are accuracy points and computes its interval note instead of hard-coding it. `write_report` now keeps this section when it rewrites the file.

**Noted, not changed.** Several things were left as they are:

- The test file's T2 and T5 intervals use B = 100, so the xfail reasons differ from the tables above in the third decimal.
- The before/after window run of section 2 has no code in the repo.
- T4's "rises with the date" compares the first and last years only.

**Verdict after review.** The numbers stand. The verdict keeps its direction and is no longer stronger than the numbers.

- R2 as pre-registered is NO on both clusterings: material at no site.
- FFmm < 0 is a person effect. A person-only world gives FFmm as negative or more so, and with person terms it is not significantly negative at any site.
- Beyond static person propensities there is a residue at wiki-RfA, Bitcoin OTC and BlueTempNet. It is small in AUC (0.5 to 1.0 points), but against the battery's own planted calibration it is as large as a substantial per-triad mechanism at two sites. It is only partly of the registry's form: FFpm and FFmp are negative beyond the null at three sites.
- Visibility is absent at BlueTempNet only; Bitcoin OTC is now undecided.
