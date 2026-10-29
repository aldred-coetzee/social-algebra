# Iteration 1: batch report and batch-2 proposal

_2026-10-29. Files 043–082 (directions D025…D546), 120 agents, 12.5M tokens, 70 minutes. Part (B) replaced the same day on Aldred's instruction: targeted, not broad._

## (A) Batch report

1. **Aim:** an algebra of drives (persons and groups) composed into an equation set that predicts or steers outcomes at membership, group and crowd scale, including positively, sensitive to size and composition; drives-as-primitives is the hypothesis under test.
2. **Learned (equations):** Keramati–Gutkin's drive theorem re-derives as an identity, and the coupling D_self + w·D_partner extends it cleanly only if w is an operator, not a state; coupling aligns objectives (stabilising) yet lowers the simultaneous-best-response stability threshold, (N−2)·b²·v ≥ k², and additive coupling gives zero partner-deficit effect, so cross-drive inhibition needs the Minkowski exponent m > 1 (047, 062). With within-person coupling C the Friedkin–Johnsen margins multiply: stable iff ρ(ΛW)·ρ(C) < 1 (063); driver count is the max geometric multiplicity of A, and "one driver node" was a broadcast hub (074).
3. **Learned (crowd scale):** Granovetter's monotone map r(t+1)=F[r(t)] is the common aggregator: the fill-and-discharge cell reduces to it under fast equilibration (081), Epstein's rule reduces to a threshold on the local cop-to-active ratio (Thron & Jackson, 067) but its mean field has one fixed point and no tipping, so outbursts are spatial fluctuation (068). Tipping needs a second variable: with discharge efficacy, a hysteresis fold at r ≈ 0.22 (back) and 0.65–0.66 (forward) (081); normal-threshold fold at σ = 12.22 (066).
4. **Learned (composition):** syntax exists, VSL W-algebra and Baez–Pollard gluing (043), but no stability certificate composes through feedback; only ISS cascades (Capucci–Myers 2026, unreviewed) (044). Hierarchical parts can lean on proofs; mutual loops carry their theorem as an assumption. A prior operator algebra exists, Bagarello's bosonic CCR with a conserved N₁+M·N₂, with no data (082); ACT's 9×29 cubic event map and dictionaries are public, CC0 (045).
5. **Learned (calibration is thin):** the best-measured coupling is exclusion→need threat, d = −1.36 immediate, −0.76 last (056); feed contagion is d ≈ 0.01–0.02 per person-week (064); no coupling matrix for n ≥ 3 anywhere, and tolerable uniform pairwise reinforcement falls as 1/(n−1) (070); mortality→worldview defence is g 0.07–0.13 against an original d 1.34, out of the base layer (051); status adapts in no panel (055); seven-drive working basis Affiliation, Status, Threat, Seeking, Care, Mating, Anger-as-operator (050). Data: Tomova/Stijovic 8–10 h deficit curves never modelled (076), Kossakowski n=1 1,478 points with a known input (078); precision is set by span in relaxation times, SE ≈ √(2τ/T) (079); Gottman–Murray has been refit (Hamaker 2009) but never tested out of sample on divorce (059, 080).
6. **Corrections caught:** 40 files, one key correction each, no fabrication in any; 137 cross-file comparisons: 56 unresolved (need a source), 40 not a true conflict, 41 resolved for one file (ten fixes owed to 05, 16, 17, 20, 22, 25, 32, 42). Most consequential: Atkinson–Birch resistance is r·min(T,N), not r·N, and the 1970 book is unread (046); Gerber & Wheeler's d = 1.21 condition was reversed (049/056); Reverdy–Koditschek Theorem 2 limits and the honeybee pitchfork credit (048); the Epstein threshold reduction was Thron & Jackson's (067).
7. **Unresolved contradictions that matter, and what settles them:** A&B's book form of C and R (046 v 16) → A&B 1970 at source, no direction yet; Epstein spatial outbursts v "no tipping" (067/068) → seeded replication with Wilensky's code (D548/sim); N ≥ 3 drive conflict, Franci–Leonard unread (048/060/069) → D301; Gottman independent refit and Madhyastha sample (059/080/20) → D187; meaning of Turchin's A and h (072 v 18/08) → Historical Dynamics ch. 4 (D341); Fudenberg–Levine equilibrium (048 v 36) → D094; Myers chapter layout (043 v 40) → D026; 073's R1 against file 25 → independent check.
8. **Method gap:** none of the forty answers the two fixed questions (drive basis; outcome out of sample) in those words, because rule 5 landed after iteration 1; the digests inferred both. Batch 2 dives carry the two sections explicitly. Web search was exhausted in every validation pass, so every "does not exist" is "not found in what was read".
9. **Ledger:** `docs/ledger.jsonl` is empty, seeding in progress; the digests name about 15 equation lines and about 12 empirical-result lines ready to seed, each tagged read/sa.
10. **Cost of batch 1:** 120 agents, 12.5M tokens, 70 minutes, all on the subscription limit the phone sessions share; it already stopped seven validators mid-flight overnight.
11. **Why broad batches stop here:** forty directions bought many findings but low yield per direction toward an equation set, and 56 unresolved cross-checks of checking debt; what v0 needs is about a dozen sources read at source plus data at three group sizes, so batch 2 is targeted at writing and testing v0, not surveying.
12. Ask: run the targeted batch below?

## (B) Batch 2 proposal: targeted, 12 directions, n 083–094

**Purpose:** enough to write a first draft equation set (v0) and test it at three sizes, n = 3 (triad: coalition, balance, who sides with whom), n ≈ 8–12 (team: cohesion, split, efficiency) and n ≈ 100+ (crowd: adoption, mobilisation, fragmentation), against **one outcome common to all three: does the group hold together or split, and who leaves.** Equations fitted at one size are tested at the others. Deep-reads and data over surveys; the four Aldred named are in. Deep-reads validated on Opus; the two cross-checks on Haiku.

```json
[
 {"id":"D584","n":"083","cluster":"T"},
 {"id":"D207","n":"084","cluster":"H"},
 {"id":"D215","n":"085","cluster":"G"},
 {"id":"D301","n":"086","cluster":"I"},
 {"id":"D261","n":"087","cluster":"H"},
 {"id":"D187","n":"088","cluster":"F"},
 {"id":"D507","n":"089","cluster":"M"},
 {"id":"D028","n":"090","cluster":"A"},
 {"id":"D559","n":"091","cluster":"P"},
 {"id":"D577","n":"092","cluster":"S"},
 {"id":"D583","n":"093","cluster":"T"},
 {"id":"D551","n":"094","cluster":"N"}
]
```

### Reasons, by what each gives v0

**The frame (required)**
- D584 (T, cross-check): the merge/split/nest inventory, Liebovitch's two camps (20), Altafini (23), fission–fusion (29), coalitions (10) included; it names the composition law v0 must state and the gap it must fill. 043/044 already give half the answer (syntax yes, feedback certificates no).
- D577 (S, survey): the outcome-measures table; "holds together or splits, who leaves" has to be an instrumented outcome at each size before anything is fitted, and Aldred picks the measure.
- D583 (T, survey): reflexivity, with Perdomo's performative prediction as the formal case; decides whether v0 carries a "known-model" term or a validity caveat.
- D559 (P, survey): group size; the empirical size laws that 070's 1/(n−1) stability bound and 069's N² tie-breaking cost are tested against, and the scaling of parameters from n = 3 to 100+.

**n = 3, triad**
- D207 (H, deep-read): Heider balance, the signed-graph product rule, Caplow's triad coalitions, Bowen triangles, and how well real signed networks obey balance; the triad split rule at source, still [sa] in every file.
- D215 (G, cross-check): verify the hypotheses of Altafini's bipartite consensus (060 omitted the connectivity condition), Kuramoto critical coupling and Olfati-Saber; Altafini's theorem is the candidate "splits into two camps iff structurally balanced" law that runs from triad to crowd.

**n ≈ 8–12, team**
- D301 (I, deep-read): the compromise-or-choose bifurcation and uninformed-majority effect (Franci–Leonard line); the honeybee cross-inhibition result for N ≥ 3 options that 048, 060 and 069 all stop at unread, and the team-scale decide-or-deadlock law.
- D261 (H, deep-read): cohesion measurement, the cohesion→performance lags and a feedback-loop form; cohesion is the team-scale state whose collapse is the split, and no file has its dynamics.
- D187 (F, deep-read): Gottman–Murray out-of-sample accuracies, the lower-threshold couples, Madhyastha 2011 and Hamaker 2009; settles 059 v 080 v 20 and fixes the coupling and trigger functions v0 lifts from the dyad into the team.

**n ≈ 100+, crowd**
- D507 (M, data): protest event data for threshold and preference-falsification models; the agent reads Kuran 1989/1991 at source as the model the data are for (066 has them only via Brummitt), giving crowd-scale mobilisation and fragmentation to fit Granovetter's map against.

**Across sizes**
- D028 (A, deep-read): passivity, small-gain and contraction under asymmetric, non-reciprocal influence; the certificate that would let a stability result fitted at one size be composed to the next, which 044 found missing for feedback.
- D551 (N, cross-check): circularity and identifiability, simulation-based calibration and parameter recovery; the discipline for testing v0 on a population built independently of it, which 079 (precision set by span) and 081 (one parameter set) both lack.

**Left out, and why:** Keramati–Gutkin coupling is already [read] at theorem level (047, 062); the remaining [sa] is the 2011 supplement, not load-bearing for v0. Clusters O, Q, R and the rest of S and the testbed wait for a v0 to steer. D026 (Myers) is syntax, not certificates. Two sources still have no direction and should be added to the map for batch 3: Atkinson & Birch 1970 at source (046) and Bischof's Zurich model at source.

Cluster split: T 2, H 2, G 1, I 1, F 1, M 1, A 1, P 1, S 1, N 1 = 12 (5 deep-reads, 1 data, 3 cross-checks, 3 surveys).
| Cluster | Directions | New claims | of which read | Contradictions | Empirical results | Duplicates of earlier files | New claims per direction |
|---|---|---|---|---|---|---|---|
| A | 2 | 68 | 57 | 2 | 1 | 28 | 34 |
| B | 1 | 40 | 34 | 12 | 10 | 8 | 40 |
| C | 4 | 121 | 72 | 13 | 22 | 96 | 30 |
| D | 5 | 193 | 121 | 21 | 61 | 71 | 39 |
| E | 4 | 119 | 46 | 16 | 49 | 81 | 30 |
| F | 4 | 147 | 91 | 14 | 38 | 52 | 37 |
| G | 2 | 73 | 62 | 2 | 21 | 45 | 36 |
| H | 4 | 103 | 83 | 6 | 37 | 93 | 26 |
| I | 3 | 79 | 33 | 8 | 18 | 30 | 26 |
| J | 2 | 86 | 54 | 12 | 15 | 9 | 43 |
| K | 2 | 67 | 19 | 7 | 18 | 23 | 34 |
| L | 2 | 45 | 27 | 6 | 14 | 21 | 22 |
| M | 3 | 74 | 31 | 3 | 21 | 44 | 25 |

## Ledger yield, iteration 1 (added after seeding)

| N | 2 | 28 | 5 | 4 | 6 | 50 | 14 |