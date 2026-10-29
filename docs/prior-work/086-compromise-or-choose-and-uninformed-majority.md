# Prior work 086: the compromise-or-choose bifurcation and the uninformed-majority effect

Direction: D301 (kind: deep-read). Date: 2026-10-29. Strand: social-algebra.

**Question.** Are the compromise-or-choose bifurcation (Leonard et al. 2012; Strandburg-Peshkin et al. 2015) and the uninformed-majority effect (Couzin et al. 2011) usable as constraints on how group goals compose, and what changes with group size and composition?

**Method and provenance.** Four texts were fetched and read in full as text-extracted PDFs, in scratch files only.

- Leonard et al. 2012: Princeton author PDF, main text plus the SI pages bundled with it. Equations are transcribed from the pdftotext output. Subscripts and fractions were partly garbled, so each equation below was checked for internal consistency (limiting cases and the paper's own worked numbers). The garbled ones are flagged.
- Couzin et al. 2011: Konstanz repository copy, main text only. The text is OCR-noisy. **The supporting online material (SOM: model equations, figs S1–S11) was not available and is not read.**
- Strandburg-Peshkin et al. 2015: Konstanz repository copy, main text only. OCR-noisy. **The SOM was not read** (GEE table S2, fig. S9 thresholds).
- Conradt & Roper 2005, *Trends Ecol. Evol.* 20, 449: read in full (review). **Conradt & Roper 2003, *Nature* 421, 155, is paywalled and its body was NOT read**; its abstract was read at Europe PMC on 2026-10-30. Everything beyond the abstract is [sa]. The 2005 review by the same authors is [read] and is used in its place, labelled as a different paper.

DOIs were confirmed at Crossref this session:

- 10.1073/pnas.1118318108
- 10.1126/science.1210280
- 10.1126/science.aaa5099
- 10.1038/nature01294
- 10.1016/j.tree.2005.05.008 (title there: "Consensus decision making in animals")
- 10.1038/nature03236 (Couzin, Krause, Franks & Levin 2005)

Tags: [read] = fetched and read at source. [derived] = my algebra from [read] equations. [sa] = secondary account, not read, and nothing [sa] feeds an equation.

**Bottom line up front.**

1. The only exact result is Leonard's Eq. 7, a threshold on the angle between two preferred directions. It depends on a sensing-range parameter r and on nothing else. In particular it does not depend on preference strength (K1) or on the number of uninformed individuals (N3). So the choose/compromise boundary is set by the geometry of the options and the sensing network, not by how strong anyone's drive is.
2. The "uninformed help" result is real in two senses (a bifurcation proof for exclusivity of the decision, and 18-replicate fish data) but narrow. It is a direction-of-travel model with a deterministic two-informed-group setup, and the fish experiment is a single design with N1=6, N2=5 and N3 of 0, 5 or 10. The mechanism Leonard offers for the N3 effect on the Eq. 7 threshold is an interpretation (density lets sensing range shrink), not a theorem.
3. Baboon data show qualitative agreement with the compromise/choose picture (an angle of about 90 degrees is printed in the text) and a majority-follows rule. They do not test Leonard's equations. No parameter of Eq. 7 (r) was measured.

---

## 1. Leonard, Shen, Nabet, Scardovi, Couzin & Levin 2012 [read, full text]

**Citation.** Leonard N.E., Shen T., Nabet B., Scardovi L., Couzin I.D., Levin S.A. (2012). "Decision versus compromise for animal groups in motion." *PNAS* 109(1), 227–232. DOI 10.1073/pnas.1118318108 (Crossref confirmed). Open copy: PMC3252942 (confirmed at Europe PMC to map to this DOI; the copy actually read was the Princeton author PDF https://naomi.princeton.edu/wp-content/uploads/sites/744/2021/03/PNAS-2012-Leonard-227-32SI.pdf). The author order above is the PDF's and matches Crossref.

**Their vocabulary.** Informed vs uninformed individuals. "Preference" for a direction. "Collective decision" (one informed subgroup plus all uninformed move together in that subgroup's preferred direction, the other informed subgroup moves off alone) vs "compromise" (subgroups settle on averaged directions). Sensing range, coupling weights, invariant manifolds, boundary-layer (fast) and slow dynamics. Note the paper's definition of "decision" differs from the earlier simulation paper (all individuals reach consensus); the authors say so explicitly.

**Operands.** N individuals, each a constant-speed particle with heading θ_j. Three subgroups: N1 prefer direction θ̂1, N2 prefer θ̂2, N3 have no preference. N1+N2+N3 = N. Coupling weights a_jl(t) in [0,1] between individuals.

**Equations [read], transcribed.**

Heading dynamics (Eqs. 1–3), for j in subgroup 1, 2 and 3 respectively:

- 1: dθ_j/dt = sin(θ̂1 − θ_j) + (K1/N) Σ_l a_jl sin(θ_l − θ_j)
- 2: dθ_j/dt = sin(θ̂2 − θ_j) + (K1/N) Σ_l a_jl sin(θ_l − θ_j)
- 3: dθ_j/dt = (K1/N) Σ_l a_jl sin(θ_l − θ_j)

"K1 > 0 weights the attention paid to other individuals versus the attention paid to the preferred direction." The coefficient on the preference term is fixed at 1, so K1 is the ratio of social coupling to preference strength.

Coupling dynamics (Eqs. 4–5): dη_jl/dt = K2(ρ_jl − r); a_jl = 1/(1+e^(−η_jl)); equivalently da_jl/dt = K2(1−a_jl)a_jl(ρ_jl − r). Here ρ_jl = |cos((θ_j − θ_l)/2)|, which is 1 when two individuals head the same way and 0 when opposed, and 0 ≤ r ≤ 1 is "a chosen fixed threshold representing an individual's sensing range". A pair is coupled only if their headings are within a window set by r. Coupling is therefore a function of heading similarity, not of space (a deliberate simplification; the paper justifies it for initially aggregated groups).

Slow dynamics on the eight coupling manifolds (Eq. 6), with Ψ_k the mean heading of subgroup k and A_12, A_13, A_23 in {0,1} the inter-subgroup coupling constants:

- dΨ1/dt = sin(θ̂1 − Ψ1) + (K1/N)(A12 N2 sin(Ψ2 − Ψ1) + A13 N3 sin(Ψ3 − Ψ1))
- dΨ2/dt = sin(θ̂2 − Ψ2) + (K1/N)(A12 N1 sin(Ψ1 − Ψ2) + A23 N3 sin(Ψ3 − Ψ2))
- dΨ3/dt = (K1/N)(A13 N1 sin(Ψ1 − Ψ3) + A23 N2 sin(Ψ2 − Ψ3))

Setup: θ̂1 = 0, 0 ≤ θ̂2 ≤ π, N1 = N2 for the analysis (N1 ≠ N2 is treated in the SI, with simulations).

**Main result (Eq. 7) [read].** The manifolds M010 and M001 (the uninformed subgroup coupled to exactly one of two uncoupled informed subgroups, that is, a "decision") are both stable if and only if cos θ̂2 < 2r² − 1, i.e. θ̂2 > θ_c, where

  θ_c = cos⁻¹(2r² − 1).

The fully coupled manifold M111 (compromise) is stable if θ̂2 < θ_c (stated as "stable if", and the text then adds the further conditions below). M101 and M110 are always unstable.

**[derived]** Since cos(2x) = 2cos²x − 1, θ_c = 2·arccos(r). The paper's own worked numbers check: r = 0.9 gives 51.7° (paper: 52°); r = 0.6 gives 106.3° (paper: 106°); r = 0.707 gives 90° (paper Fig. 4: π/2). The threshold falls as r rises, i.e. as sensing narrows.

**Other conditions on uninformed numbers [read; Eqs. 8–10, garbled in extraction, checked for consistency].**

- Eq. 8, existence of a pathological second compromise solution on M111 (uninformed heading opposite to the mean preference): it does not exist if (N3/(2N1))^(2/3) > 1 − (2N1K1/(N sin(θ̂2/2)))^(2/3). The paper states this is always satisfied for N3 > 2N1 or for K1 ≥ 2. Check: for N3 > 2N1 the left side exceeds 1 and the right side is below 1, so it holds, as stated.
- Eq. 9: for M100, the second solution is not attracting if r > sqrt(1 − d²), d = N sin(θ̂2/2)/(2 N1 K1).
- Eq. 10: M011 is unstable if r < 1/sqrt(1+ν²) or r > sqrt(1/2 + 1/(2 sqrt(1+ν²))), with ν = N sin(θ̂2/2)/(N3 K1 + N cos(θ̂2/2)). [derived: as N3 grows, ν falls toward 0, the first bound approaches 1 and the second approaches 1, so the range of r where M011 can survive shrinks.]
- Table 1: with N3 > 2N1, M111 is unstable precisely when M010 and M001 are stable.

**Theorems / derived predictions.**

- (T1) Sharp threshold: for r fixed, a decision is stable iff θ̂2 > θ_c(r); a compromise is stable iff θ̂2 < θ_c. The bifurcation is in the angle between options. Stated by the authors as a proof ("prove a necessary and sufficient condition"). My reading: the "iff" is for stability of M010/M001 as manifolds; whether the system reaches them from given initial conditions is separate (they list M000, M100 and M011 as possible competing stable solutions for some parameters).
- (T2) More uninformed individuals widen the parameter region in which the decision manifolds are the only stable ones (Fig. 5, N3 = 11, 50, 500, N1 = N2 = 5, K1 = 2). Authors: "the larger N3 provides the same effect as increasing the social interaction strength K1" and call the uninformed a kind of "glue".
- (T3) The authors also argue that adding uninformed individuals raises density, an individual can then shrink its sensing range and still see the same number of neighbours, r rises, θ_c falls. **This is an interpretive argument, not part of Eq. 7, which contains no N3.** I flag it because it is the only route by which N3 lowers the threshold itself.

**Empirical standing.** None in the paper: it is a model compared qualitatively with the authors' own earlier agent-based simulation (ref. 1 there = Couzin et al. 2005, DOI 10.1038/nature03236, not read here). The introduction also cites simulation evidence that more uninformed individuals lower the conflict threshold, in Nabet's 2009 Princeton PhD thesis (ref. 13 there, not read). So T3 has simulation backing in the cited work, but the threshold Eq. 7 itself has no N3 term. Simulations with a small random term "suggest" robustness (SI, not separately verified). Honest statement: a deterministic ODE derived to match a simulation, with no data. The authors call the N3 result "a testable result", and Couzin 2011 below is the test.

**GROUP SIZE and COMPOSITION.** N enters in three ways. (i) K1/N weights each social term; (ii) N3 > 2N1 makes the pathological compromise impossible and makes M111's stability necessary-and-sufficient (not just sufficient); (iii) more N3 expands the region of exclusive decision stability. Composition: only N1 = N2 analysed in the text; N1 ≠ N2 "yields the same necessary and sufficient conditions" with a "dominating region of attraction" for the majority informed subgroup (SI, simulation only, not read). Only two options and two informed blocs are modelled; nothing is said for three or more options.

**SCALE.** Group (direction-of-travel decision / split), model only. The "split" outcome here is the minority informed subgroup leaving the aggregation. **Consent vs manipulation:** nothing in the model is consented to; individuals merely respond to neighbour headings and no one is aware of anyone's information. The model has no intervention; adding N3 is a design choice by the analyst, not an act by an agent.

**Operand/operator translation.** Operands: Informed(preferred direction, strength fixed at 1) and Uninformed; plus a pairwise coupling variable that is itself dynamical (a "Hebbian"-like saturating gain). Operators: Align (K1 weighted), Couple/Decouple (K2, r). The group-level outcomes (decision, compromise, split) are attractors of the composed system, not an operator output.

---

## 2. Couzin, Ioannou, Demirel, Gross, Torney, Hartnett, Conradt, Levin & Leonard 2011 [read, main text; SOM not read]

**Citation.** Science 334(6062), 1578–1580. DOI 10.1126/science.1210280 (Crossref confirmed). Open copy: Konstanz KOPS (nbn urn:nbn:de:bsz:352-0-388247).

**Vocabulary.** Informed vs uninformed ("lack a preference or are uninformed about the features on which the collective decision is being made"); "strongly opinionated, or extremist, minority"; "intransigence" (resistance to social influence); "democratic consensus".

**Operands.** Subpopulations N1 (majority), N2 (minority), N3 (uninformed). Each individual has a preference vector ω with length |ω| = strength ("also represent greater intransigence to social influence"). Uninformed: ω ≈ 0. Options: two mutually exclusive targets.

**Equations.** The main text contains no equations, only verbal model description (individuals avoid collisions, are attracted to and align with near neighbours; a preference term weighted by ω). The adaptive-network model and the convention game (the "increasingly minimalist" analogues, citing Young 1998, Huepe et al.) and the saddle-node bifurcation analysis are in the SOM [not read]. Fig. 2B caption in the main text says: for low uninformed density the minority-controlled state is the only stable attractor; as uninformed proportion increases the system undergoes a saddle-node bifurcation giving a stable majority-controlled state and an unstable undecided state. That sentence is [read] as a caption; the equations behind it are not.

**Findings [read].**

- Spatial simulation (Fig. 1): ω1 = 0.3, N1 = 6 informed majority, N2 = 5 minority. Fig. 1A (all informed): as the minority raises ω2 (x-axis 0.3 to 0.5), it increasingly controls group motion. Fig. 1B (curves for ω2 = 0.36 to 0.42, N3 from 0 to 100 on the x-axis): with enough uninformed individuals the minority can no longer exploit the majority by raising ω2. The effect "reaches a maximum and then begins to slowly diminish. Eventually, noise dominates and uninformed individuals neither amplify a weak numerical majority nor lend substantial support to the minority." Outcomes counted only for consensus decisions (splitting "infrequent", 20,000 replicates).
- Mechanism (their words): uninformed individuals "lend support to, and tend to amplify, a numerical advantage (even a slight one)"; if numerous they "reduce the effect of intransigence".
- Network and convention-game analogues give "the same qualitative collective features".
- Experiment: golden shiners (Notemigonus crysoleucas); N1 = 6 trained to one target, N2 = 5 to the other, N3 = 0, 5 or 10 untrained; shiners had a spontaneous bias to the yellow target, so the yellow-trained group was effectively the stronger-preference minority. With N3 = 0 the minority N2 dictated the outcome; with untrained fish present control returned to the numerical majority (18 replicates per data point; GLM likelihood ratio test chi-sq(1,52) = 5.60, P = 0.018). Control experiment, strong preference also in the majority: majority won 72% of trials overall (12, 16, 11 of 18 for N3 = 0, 5, 10), and uninformed fish had no effect (LRT = 0.14, P = 0.71). (The extraction rendered the statistics with some symbols dropped; the numbers are as printed.)
- Authors' caution: "this process will tend to inhibit any strong minority preference, regardless of the intrinsic quality or value of that view."

**GROUP SIZE and COMPOSITION.** Size is the object: N3 from 0 to 100 in simulation, 0–10 in fish. Predictions "do not depend on the absolute number of N1" (stated; fig. S2 not read). Non-monotone: benefit rises then falls at very large N3 (noise). Composition: the result requires (i) a numerical majority, (ii) a stronger-minority preference, (iii) uninformed individuals who actually follow neighbours. If the stronger preference sits in the majority already, there is no effect (read).

**SCALE.** Group (which of two targets the shoal reaches; splitting counted separately and rare). Fish, n = 11 to 21 per trial. Human extension is explicitly only a "suggest" in the last sentence ("a principle that may extend to self-organized decisions among human agents"), with no human data.

**Consent vs manipulation.** The paper is about resistance to manipulation: a strongly opinionated minority manipulates the outcome; uninformed individuals dampen it without any act of defence. The "intervention" (adding naive individuals) is imposed by the experimenter on animals and works regardless of anyone's consent. For humans this is untested.

**Empirical standing.** One lab; one species; one design with a single positive test (P = 0.018, 18 replicates per point). The main-text claim "for a wide range of conditions" rests on simulations. No independent replication found (one search on 2026-10-30 found none; absence not established). The earlier-stated worry that "too many uninformed" erodes coherence is now [read] (see above: "eventually, noise dominates").

**Operand/operator translation.** Operands: Informed(pref, ω) and Uninformed (ω = 0, still coupled). Operator: Align(weights). New observation [derived]: Uninformed is an operand with no goal term but a positive coupling term; it is the identity of the preference part and a non-identity of the coupling part. Its effect on the fixed point is nonlinear (a bifurcation), so the group goal is not the sum of member goals.

---

## 3. Strandburg-Peshkin, Farine, Couzin & Crofoot 2015 [read, main text; SOM not read]

**Citation.** Science 348(6241), 1358–1361. DOI 10.1126/science.aaa5099 (Crossref confirmed). Open copy: Konstanz KOPS (urn:nbn:de:bsz:352-0-296905); author manuscript PMC4801504 (not fetched; its page returned a bot challenge).

**Vocabulary.** "Movement initiation": pull (initiator moves away, is followed) or anchor (not followed, initiator returns). "Event": concurrent pulls and anchors on one potential follower. "Directional agreement" = 1 − circular variance of the unit vectors from the potential follower to each initiator. "Choose" vs "compromise". "Shared decision-making".

**Data.** Wild olive baboons, Mpala Research Centre, Kenya; 25 animals (about 80% of a troop's adults and subadults) GPS-collared, one fix per second. Troops of up to 100.

**Equations.** The main text has no model equations. The analysis uses a binomial GEE for P(follow) as a function of (number of initiators) × (directional agreement) (table S2, not read) and sigmoidal fits for P(follow majority) vs numerical difference (Fig. 4). Theory cited is ref. 22 (Couzin et al. 2005 [sa]; the main text cites it only as "theory (22)").

**Findings [read].**

1. P(follow) depends on an interaction of number of initiators and agreement. Most likely when many initiators agree. "When agreement is low, having more concurrent initiators decreases the likelihood that a baboon will follow anyone", which the authors read as decisions being delayed when opinions are split.
2. No dominance effect: the dominant male did not have the highest probability of being followed, rank did not correlate with initiation success, no sex difference (binomial GLMM, male coefficient 0.222 ± 0.159 SE, z = 1.402, P = 0.161; the extraction drops minus signs elsewhere in this text, so the sign of the coefficient and z is not certain from the copy read; P is unaffected). Followers were more likely to follow initiators moving in a highly directed manner (fig. S2).
3. Two regimes: for two initiators, followers choose one direction when the angle between them exceeds roughly 90 degrees, and compromise below it. "The same pattern emerges in events with multiple initiators clustered into two subgroups."
4. When initiators conflict, followers go with the larger subgroup, increasingly so as the numerical difference grows, whatever the total number of initiators (3–4, 5–7, 8–10) and whether the troop was moving or stationary (fig. S6).
5. After such conflicts, "the troop's travel direction is positively correlated with the direction associated with successful (but not failed) subgroups of initiators (fig. S4). Thus, failed initiators ultimately move in the direction of the majority". (Corrected 2026-10-30: an earlier note said the text was cut off here; the full main text was re-read and the sentence is complete.)

**GROUP SIZE and COMPOSITION.** Number of initiators is the size variable and enters twice: more agreeing initiators raises P(follow); more disagreeing ones lowers it. Composition is defined by which animals initiate, and the data show rank and sex do not predict success. Troop size itself is not varied (one troop).

**SCALE.** Membership-level (does a given animal follow a given initiator) aggregated to group-level direction. Observational; one troop; 25 individuals. No intervention. Consent/manipulation is moot: the pull/anchor definition "is agnostic to individual intention and motivation" (quoted), and the authors say a particular sequence "may or may not reflect a causal relationship".

**Empirical standing.** Strong for the qualitative claim that rank does not predict following in this troop (one troop, so no replication shown; the tracking period is given in the SOM, not read). The 90-degree threshold is read off plots by a statistical assignment into modes (fig. S9, not read). Whether it matches Leonard's θ_c is unknowable from the data: Eq. 7 gives 90 degrees only if r = 0.707, a value no one measured, so the agreement is not a test. Also, the two papers use different notions of "compromise": Leonard's is the group's stable heading; this paper's is a follower's chosen direction in a single event.

**Operand/operator translation.** Operand: an individual with a position and a heading, no stored preference. Operators: Pull(i, j), Anchor(i, j). Group-level: Follow-majority as a sigmoid. The directions here are measured outcomes of moves, not a set of declared preferences.

---

## 4. Conradt & Roper 2003 (not read) and 2005 (read)

**2003, "Group decision-making in animals", Nature 421, 155–158, DOI 10.1038/nature01294 (Crossref confirmed). Full text paywalled (nature.com redirects to login); body not read.** The abstract was read at Europe PMC [read: abstract only]: a model of 'despotism' vs 'democracy' where "under most conditions, the costs to subordinate group members, and to the group as a whole, are considerably higher for despotic than for democratic decisions"; "Even when the despot is the most experienced group member, it only pays other members to accept its decision when group size is small and the difference in information is large"; democratic decisions are better "primarily because they tend to produce less extreme decisions". The model itself, its equations and parameter ranges are [sa]. Nothing from this paper feeds an equation.

**2005 review, "Consensus decision making in animals", *Trends Ecol. Evol.* 20, 449–456, DOI 10.1016/j.tree.2005.05.008 [read, full text].** What it supports, as a framework and not as equations (the review contains none):

- Definition [read]: "Consensus costs: if there is a conflict of interest involved in a consensus decision, individual members can incur consensus costs (in terms of reduced fitness) of forgoing their own optimal action to comply with the decision outcome."
- Claim [read, citing ref. 8 = the 2003 paper]: "if conflicts of interest are involved, consensus costs to groups are, in theory, considerably higher for unshared than for equally shared decisions". Equally shared decisions are better "primarily because they tend to produce less extreme decisions, rather than because each individual has an influence on the decision per se".
- Group size [read]: coercion by a dominant "is unlikely to work in practice because of the inability of a dominant animal to force a consensus decision, either because it is physically unable to do so, particularly in large groups, or because it would not gain sufficiently to outweigh the costs of coercion"; hence conflicting decisions "typically have to be made through voluntary compliance".
- Small groups can communicate globally, large groups only locally. The review states that "it is not immediately obvious whether simple rules could also lead to equally shared decisions in larger groups" and then summarises the Couzin et al. model result as (their summary) a compromise heading for small preference differences and the majority-preferred goal for large ones. This is the same compromise/choose pair as Leonard, stated verbally.
- Prediction [read, Box 3, navigation, a low-conflict case]: directional scatter between groups should be inversely correlated with group size. "Few empirical data are available to test these predictions"; of those cited, homing-pigeon studies conflict and migrating-skylark data support it. (Corrected 2026-10-30: an earlier version called the prediction untested.)
- Consensus costs accumulate daily ("related consensus costs can augment"), and for ungulates the costs are large enough to cause sexual segregation.

**SCALE.** Group (cost of decision rule). **Consent vs manipulation:** the review's own framing is exactly this axis: "voluntary compliance" vs coercion, with coercion limited by group size. It gives no numbers.

---

## 5. What follows for composing group goals

**Candidate constraints, graded by how well they are supported.**

- **C1 [read: Eq. 7]. The choose/compromise switch is at θ_c = 2·arccos r, independent of K1 and N3.** If the algebra has a "composition of two goals" operator, the first thing it must know is the angle between the goals and an r-like sensing/coupling threshold. Preference strength is not an input to this switch.
- **C2 [read: Couzin 2011 Fig. 1B, Fig. 2B caption, Fig. 3 text]. An uninformed fraction can flip minority control to majority control** by a saddle-node bifurcation, when the minority is stronger but fewer. No effect if the stronger preference is already the majority's (12/16/11 of 18).
- **C3 [read: Strandburg-Peshkin Fig. 4 text]. With conflicting initiators, follow the larger subgroup, with a sigmoidal dependence on the numerical difference.** This is the empirical form of "majority".
- **C4 [read: 2005 review].** Group size makes coercion by one member fail and pushes toward voluntary, more moderate outcomes. Qualitative.

**What does NOT follow.**

- The reductions are for "preference for a direction". They say nothing about group goals that are not points in a plane (e.g. a status goal, a belonging goal). Whether "angle between options" has a social analogue is a modelling choice, not a finding.
- No source here has human data. The Couzin paper's human extension is one sentence.
- Because the stability result is for a pair of equal informed blocs and one set of uninformed, nothing here covers three or more informed blocs.

---

## Does it reduce to a drive basis?

**What reduces, partly.** The parameters in these models sit near drive-like quantities of persons:

- The preference term with strength ω (Couzin 2011) or the fixed unit coefficient on sin(θ̂ − θ) (Leonard) is a goal-attraction of a person.
- K1 (Leonard) is the ratio of social attraction to goal attraction, which is a cohesion/affiliation drive relative to a goal drive. In Couzin 2011 the same ratio shows up as intransigence.
- "Uninformed" is a person with no goal drive but intact affiliation. That is a legitimate drive-basis statement: remove one drive and keep the other.
- The sign of the effect of increasing a goal drive (ω2) is monotone in Couzin 2011 (stronger minority controls more) until the uninformed fraction crosses a bifurcation.

**What does NOT reduce.**

- **The switch itself.** In Eq. 7 the boundary between choose and compromise depends on the angle between the options and on r, not on how strong either drive is or on K1. The drive magnitudes do not appear. So the central result of the tradition is a property of the option geometry and the coupling threshold. Under "drives as primitives" it would be a property of the situation (where the options lie relative to each other), which is not a drive of any person or group.
- **The coupling gain a_jl(t).** It is a state of the relation, updated by heading similarity (Eqs. 4–5). That is the relational variable the algebra would need in addition to drives, and it is dynamic.
- **The size effect.** The N3 effect arises through the structure of the coupling manifolds and the existence of attractors (M111 vs M010/M001, Eqs. 8–10). The drive of any one member does not carry it; it is a property of the composition of the group.
- **The baboon follow-the-majority rule** (sigmoid in numerical difference) is a rule of followers, not a drive; the paper says the pull/anchor definition is "agnostic to intention and motivation". Nothing in it identifies a drive.
- **Rank does not predict following** in one troop. Whatever a "dominance drive" might be, it was not what moved the troop's decisions here. This is a negative result for a power/status drive as the operator on group movement in this setting (one troop, one tracking period).

**Verdict for the working hypothesis.** The tradition supports "drives as primitives" only in the narrow sense that preference strength and cohesion are inputs. Its main theorem is about the arrangement of the options and the coupling threshold, not drive amplitudes. This is a mild counterexample to drives-only: a drive basis would need at least a relational state variable (a_jl or r) and a situation variable (θ̂2) as primitives alongside drives.

---

## What does it predict or control, and how well?

**What it predicts.**

- Leonard: the stability of a group-level direction outcome (decision vs compromise) as a function of θ̂2 and r. The prediction is exact within the model and is checked only against the authors' own earlier simulation (qualitatively). Out-of-sample: none.
- Couzin 2011: which of two targets a shoal reaches, given N1, N2, N3 and preference strengths. Out-of-sample: one experiment in golden shiners, effect P = 0.018, 18 replicates per data point, three values of N3 (0, 5, 10), with a null control (P = 0.71) in the case the theory predicts a null. No effect sizes are reported in the main text other than the proportions in the control (12, 16, 11 of 18) and a 72% majority-win rate overall in that control.
- Strandburg-Peshkin: whether a given baboon follows, as a function of the number and agreement of initiators; and whether followers choose or compromise by angle. Out-of-sample: the analysis is of one troop; the 90-degree transition and the majority rule are descriptive fits, not out-of-sample predictions from a prior model with fixed parameters.
- Conradt & Roper (2005 review): that costs are lower for equally shared than unshared decisions and that coercion fails in large groups. [Cited to the 2003 paper, which was not read.] Almost no empirical test is cited in the sections read (the review itself says few data are available for the navigation predictions).

**What it controls.** Nothing in these four sources is an intervention on a human group. The one controllable lever is the number of uninformed (weakly or non-opinionated) members, tested only in fish, and it controls the group's resistance to a strong minority, not the group's choice in any direction the experimenter picks (the majority wins, whatever its merit).

**Failures and limits actually visible in the texts.**

- Couzin 2011: effect fades at high N3 (noise dominates); no effect when the strong preference is already the majority; the process inhibits any strong minority "regardless of the intrinsic quality or value of that view", so it also suppresses a correct minority.
- Leonard 2012: the "decision" is only one informed subgroup plus the uninformed; the other informed subgroup splits off. M000, M100 or M011 can be co-stable for some parameters, so the decision is not guaranteed even above θ_c. A deterministic model; N3's effect on the threshold depends on an interpretation of r.
- Strandburg-Peshkin: one troop; association with intention is explicitly not claimed; the compromise/choose threshold has no measured r to compare with Eq. 7.
- Across all: the tested species are fish and baboons; humans are not tested.

---

## What exists vs what does not

**Exists.** A proven threshold for compromise-vs-choose in one tractable model (Leonard Eq. 7). A bifurcation account and a fish experiment for the uninformed-majority effect. A GPS field dataset consistent with the qualitative picture and against a dominance account. A qualitative review of consensus costs vs group size.

**Exists in the wider literature (found by search 2026-10-30; abstracts read, bodies not read, all [sa] beyond the abstract):**

- Dyer, Johansson, Helbing, Couzin & Krause (2009, online 2008), "Leadership, consensus decision making and collective behaviour in humans", *Phil. Trans. R. Soc. B* 364, 781–789, DOI 10.1098/rstb.2008.0233 (Crossref confirmed; PMC2689712). Abstract: in groups of eight people, "both group size and the presence of uninformed individuals can affect the speed with which small human groups ... decide between two opposing directional preferences and the likelihood of the group splitting". This is a human experiment on uninformed members under a two-direction conflict, with equal informed blocs; it is not a test of the strong-minority versus majority effect. A tool-summarised fetch of the PMC page (so [sa]) reported 22 groups, uninformed-present groups slower to the periphery, and 4-v-4 groups splitting most. Also Dyer et al. 2008, "Consensus decision making in human crowds", *Anim. Behav.* 75, 461–470, DOI 10.1016/j.anbehav.2007.05.010 (Crossref confirmed; not read).
- Pinkoviezky, Couzin & Gov (2018), "Collective conflict resolution in groups on the move", *Phys. Rev. E* 97, 032304, DOI 10.1103/PhysRevE.97.032304 (Crossref confirmed). Abstract: a spin model with an exact solution in the thermodynamic limit; the compromise/choose transition at a critical angle coincides with a change from Brownian to persistent collective motion, and "the number of uninformed individuals ... acts as an inverse of the temperature (noise) of the spin model"; unequal subgroups tend toward the larger subgroup's target.
- Sridhar, Li, Gorbonos, Nagy, Schell, Sorochkin, Gov & Couzin (2021), "The geometry of decision-making in individuals and collectives", *PNAS* 118(50), DOI 10.1073/pnas.2102157118 (Crossref confirmed). Abstract: for two or more options in space, repeated bifurcations from averaging to excluding an option until one remains, with experiments in fruit flies, desert locusts and larval zebrafish (individuals in virtual reality).

**Does not exist (in what was read).** Any human test of the strong-minority versus uninformed-majority effect (a human experiment on uninformed members with equal informed blocs does exist: Dyer et al. 2009, above). A measurement of r, K1 or the coupling threshold in any real group. A test of Leonard's quantitative threshold on real animal groups. Within the four texts, a model with three or more options or more than two informed blocs (Sridhar et al. 2021, above, treats three or more options). A treatment of non-spatial goals. A treatment of group-size change at fixed composition ratio for the bifurcation (the fish data vary N3 only). Independent replications.

## Unconfirmed

- Conradt & Roper 2003 content: abstract read at Europe PMC (the "small group ... difference in information is large" quote is now confirmed verbatim from the abstract); the model and its body are paywalled and [sa].
- Couzin 2011 SOM: model equations, S1–S11 figures, the network and convention-game bifurcation equations. Not read.
- Strandburg-Peshkin 2015 SOM: GEE coefficients (table S2), thresholds from the statistical assignment (fig. S9), post-conflict troop-direction correlation magnitude. Not read; the end of the main text was truncated by extraction.
- Leonard SI: the N1 ≠ N2 stability conditions, random-noise robustness figures, the Moon et al. 2007 and Nabet et al. 2009 prior analyses (ref. 12 there). Not read.
- Eqs. 8 and 10 of Leonard: re-checked 2026-10-30 against a fresh layout-preserving extraction of the same PDF, where the fraction and root structure is legible and matches the transcription; still not compared with a rendered typeset page.
- Later work: Pinkoviezky, Couzin & Gov 2018 and Sridhar et al. 2021 now exist-confirmed (Crossref) and abstract-read (see "Exists in the wider literature"); bodies not read.
- Independent replication of the Couzin 2011 fish result: one search 2026-10-30 found none; absence not established.

## Validation log (2026-10-30)

- ✓ Leonard, Shen, Nabet, Scardovi, Couzin & Levin 2012, PNAS 109(1) 227–232, 10.1073/pnas.1118318108: Crossref matches. Re-read the Princeton PDF. Eqs. 1–10, θ_c = cos⁻¹(2r²−1), the 52°/106°/π/2 examples, Fig. 5 (K1 = 2, N1 = N2 = 5, N3 = 11/50/500), the "glue" quote and Table 1 all confirmed. ✎ Added that the text cites simulations (Nabet 2009 thesis, not read) for N3 lowering the threshold. ✎ Confirmed PMC3252942.
- ✓✎ Couzin, Ioannou, Demirel, Gross, Torney, Hartnett, Conradt, Levin & Leonard 2011, Science 334(6062) 1578–1580, 10.1126/science.1210280: Crossref matches. Re-read the KOPS PDF. The LRT 5.60 P = 0.018, the control 12/16/11 of 18 with 72%, LRT 0.14 P = 0.71, the noise quote and the saddle-node caption all confirmed. ✎ The ω2 range is now attributed to the right panel (1A versus 1B). ✎ C2 now cites Fig. 2B for the saddle-node.
- ✓✎ Strandburg-Peshkin, Farine, Couzin & Crofoot 2015, Science 348(6241) 1358–1361, 10.1126/science.aaa5099: Crossref matches. Re-read the KOPS PDF. The ~90° regime, the GEE interaction, the majority sigmoid (fig. S6) and the agnosticism quote are confirmed. ✎ Finding 5 was not truncated, and the full sentence has been restored. ✎ The sign of the GLMM coefficient is flagged as uncertain because minus signs were dropped. ✎ "One season" was removed because it is not in the main text.
- ✓✎ Conradt & Roper 2005, TREE 20(8) 449–456, 10.1016/j.tree.2005.05.008: Crossref matches. Read in full (third-party copy of the published PDF). The glossary definitions, the Box 1 quotes and the coercion/voluntary-compliance passage are confirmed. Ref. 8 = 2003 Nature and ref. 15 = Couzin 2005 are confirmed. ✎ The group-size/directional-scatter prediction is in Box 3, and some data support it (skylarks), so it is not "untested".
- ✓✎ Conradt & Roper 2003, Nature 421(6919) 155–158, 10.1038/nature01294: Crossref matches, and the title "Group decision-making in animals" was added. Body paywalled. ✎ The abstract was read at Europe PMC, and the quoted sentence is verbatim there rather than from a search summary. The body stays [sa].
- ✓ Couzin, Krause, Franks & Levin 2005, Nature 433(7025) 513–516, 10.1038/nature03236: Crossref matches. Not read (cited only).
- ✓ Pinkoviezky, Couzin & Gov 2018, PRE 97, 032304, 10.1103/PhysRevE.97.032304: Crossref matches, abstract read, body not read. ✎ Moved from "not verified" to exist-confirmed.
- ✓ Sridhar et al. 2021, PNAS 118(50), 10.1073/pnas.2102157118: Crossref matches (eight authors), abstract read. ✎ Added. It qualifies "no model with three or more options".
- ✓ Dyer, Johansson, Helbing, Couzin & Krause 2009, Phil Trans B 364 781–789, 10.1098/rstb.2008.0233: Crossref matches, abstract read, experiment details [sa]. ✎ Added. It qualifies "no human test".
- ✓ Dyer et al. 2008, Anim Behav 75 461–470, 10.1016/j.anbehav.2007.05.010: Crossref matches. Not read.
- No fabrications found. Nothing was removed.

Sources opened this pass: 4 primary full texts (Leonard 2012, Couzin 2011, Strandburg-Peshkin 2015, Conradt & Roper 2005), 4 abstracts (Conradt & Roper 2003, Pinkoviezky 2018, Sridhar 2021, Dyer 2009), and 10 Crossref records.

**Verdict.** The file is accurate where it matters. Every equation and statistic that a drive equation could rest on (Leonard Eqs. 1–10 and θ_c; the Couzin fish statistics) matches the primary text, and the [read] tags are earned. The corrections are local. One misplaced figure panel, one false "truncated" note, one review prediction wrongly called untested, and a sign that is uncertain because of the extraction. The "does not exist" list was too strong: a human experiment on uninformed members (Dyer et al. 2009) and a model for three or more options (Sridhar et al. 2021) exist, and both are now listed with scope.


## Cross-checks (2026-10-30)

Checked against the other prior-work files by grep for each work, author and key term (Leonard, Couzin, Strandburg-Peshkin, Conradt & Roper, Dyer, Pinkoviezky, Sridhar, Nabet, the DOIs, "uninformed", "shiner", "baboon"). Only file 29 (animal collective behaviour) and, for one line, file 09 and file 069 state the same works. Nothing here was resolved by re-reading a source; contradictions are recorded as found.

**Agreements.**

- Leonard et al. 2012 author order and DOI 10.1073/pnas.1118318108 match `29-animal-collective-behaviour.md` (B3 reference list).
- Couzin et al. 2011 DOI 10.1126/science.1210280 matches. Author order matches file 29 after its own validation corrected it (Levin before Leonard). File 29 gives the title "Uninformed individuals promote democratic consensus in animal groups"; this file gives no title.
- Sridhar et al. 2021 DOI 10.1073/pnas.2102157118 matches. File 29 gives the volume as "PNAS 118, e2102157118"; this file gives "118(50)". Same paper.
- Strandburg-Peshkin et al. 2015 DOI 10.1126/science.aaa5099 matches. Both files say the baboons follow the majority of initiators rather than dominant individuals, and both put the choose/compromise split at a small angle versus a large one. File 29 gives this from the abstract only; this file reads the main text and adds the ~90 degree figure.
- Couzin et al. 2011 abstract wording ("a strongly opinionated minority can dictate group choice, but the presence of uninformed individuals spontaneously inhibits this process") matches this file's read findings. File 29 had flagged the "too many uninformed" erosion as a press-summary claim; this file now reads it in the main text (Fig. 1B, "noise dominates").
- Conradt & Roper 2003 is described as a shared-versus-unshared consensus-cost model in file 29 and as an unread paywalled body here. Both agree that its body was not read; the abstract quote here is the only text either file has.
- Couzin et al. 2005 (DOI 10.1038/nature03236) is "not read" in this file and in `069-honeybee-quorum-cross-inhibition-model.md`. Agreement on status.
- Dyer et al. 2009 is listed in file 29 as known from memory with its DOI not checked. This file confirms the DOI at Crossref and reads the abstract. This is an upgrade, not a conflict.

**Contradictions (unresolved; both sides recorded).**

- C-a. Status of the compromise-or-choose split as a test of Leonard's threshold. `29-animal-collective-behaviour.md`, B3 (line 88): the split "is the empirical counterpart of the bifurcation analysed by Leonard et al. 2012 and Sridhar et al. 2021". This file, section 3 "Empirical standing": the agreement "is not a test", because Eq. 7 gives 90 degrees only at r = 0.707, which no one measured. Not settled by either validation log. Unresolved.
- C-b. Attribution of uncommitted-pool damping of a strong minority. `29-animal-collective-behaviour.md`, Missing/translation table (line 194): credited to Couzin 2005, "not verified here". This file, section 2: credited to Couzin et al. 2011 (read in the main text); Couzin 2005 is cited by Leonard as the authors' earlier simulation and was not read here. Unresolved; the 2005 text would decide it.

**Duplicates.** The following claims already stand in another file, so the ledger lines below mark `dup_of_file`:

- Sridhar et al. 2021 abstract-level claim (repeated bifurcations; same geometry for individuals and groups): `29-animal-collective-behaviour.md`, reference list (line 238).
- Strandburg-Peshkin "dominance does not predict following" and "majority of initiators": `29-animal-collective-behaviour.md`, B3 (lines 87-88).
- Couzin 2011 "strongly opinionated minority ... uninformed inhibits" abstract wording: `29-animal-collective-behaviour.md`, B4 (line 96).

**Related, not the same work.** `091-group-size-scaling-thresholds-and-what-is-held-fixed.md` section 4 reads Kao & Couzin 2014 (group size and decision accuracy). It is a different paper by one of the same authors and bears on the group-size question here. Not a duplicate; no claim is shared.

**Ledger.** Returned to the orchestrating step as structured lines (provenance taken as tagged here: [read] as `read`; abstract-only and [sa] as `sa`; [derived] lines carry the provenance of the [read] equation they come from, with the derived step in the note). Nothing committed.
