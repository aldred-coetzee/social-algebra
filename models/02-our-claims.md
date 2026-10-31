# Our own claims

_Started 2026-11-01 after Aldred: "this all seems completely derivative… integrate the current and become less derivative." Everything in this file is ours: a definition we made, a theorem we proved, or a conjecture we state, each with the test that would refute it, kept apart from the inherited equations in `models/00-v0.md` and the corollaries in `models/01`. Provenance tags: [derived, shown] proof on this page, by us, with the audit status stated; [computed] observed in exact-arithmetic draws, evidence not proof; [conjecture]. Nothing here rests on a ⚠ line._

## Claim 1. A group's drive state is a distribution, and the merge law is a sandwich

**1.1 Definition (group drive state).** For the crowd law (v0.1 §4.4; Granovetter's map, L1831 [read]) the state of a group of n members is not a number but the empirical distribution of its members' thresholds, F(r) = #{i : θ_i ≤ r}/n, or equivalently the **excess function** E_F(r) = F(r) − r. Its equilibrium is τ(F) = lfp(F), the share that eventually acts (v0.1 Theorem 6.3). **Merge** of (n_1, F_1) and (n_2, F_2) is the mixture F_m = λF_1 + (1 − λ)F_2, λ = n_1/(n_1 + n_2): thresholds are kept as fractions of the crowd, so a merge dilutes. **Split** by any rule on members gives the conditional distributions. Merge is linear in E_F; the equilibrium is E_F's first non-positive point.

*Why this and not a mean.* v0.1 §2.3 already showed (Granovetter's pair, L1225 [read]) that the equilibrium is not determined by mean and variance. Proposition 1.6 below sharpens this to: no summary of the parts' equilibria and sizes determines the merged equilibrium at all.

**Fact 0.** τ(F) = min P(F), where P(F) = {r ∈ [0,1] : F(r) ≤ r} is the pre-fixed set (1 ∈ P(F) always). *Proof.* The orbit from 0 converges to a fixed point r* (v0.1 6.3(i)); if r ∈ P(F) then by induction every orbit point is ≤ r, so r* ≤ r. ∎ [derived, shown]

**1.2 Theorem (merge sandwich).** For any two crowds and any λ ∈ (0,1),

  min(τ_1, τ_2) = τ(min(F_1, F_2)) ≤ τ(F_m) ≤ τ(max(F_1, F_2)) = min(P(F_1) ∩ P(F_2)),

and both ends are attained for some pairs.

*Proof.* If λE_1(r) + (1−λ)E_2(r) ≤ 0 then E_1(r) ≤ 0 or E_2(r) ≤ 0, so P(F_m) ⊆ P(F_1) ∪ P(F_2); if both are ≤ 0 so is the combination, so P(F_1) ∩ P(F_2) ⊆ P(F_m). Take minima with Fact 0. The identifications of the ends: P(min(F_1,F_2)) = P(F_1) ∪ P(F_2) and P(max(F_1,F_2)) = P(F_1) ∩ P(F_2). Attainment: λ → 1 gives the lower end when τ_1 ≤ τ_2; the example in 1.4 attains the upper end. ∎ [derived, shown; audit requested 2026-11-01]

*Reading.* **A merge is never damped below both parts**, and it can rise above both, but never beyond the smallest share at which *both* parts would stop on their own.

**1.3 Theorem (monotonicity and convexity).** (a) F ≤ G pointwise ⇒ τ(F) ≤ τ(G); hence F_1 ≤ F_2 ⇒ τ_1 ≤ τ(F_m) ≤ τ_2. (b) For every c, {F : τ(F) ≥ c} is convex, because τ(F) ≥ c iff F(r) > r for all r < c, a family of strict linear inequalities; so any mixture of any number of crowds has τ at least the least of the parts', two full cascades merge to a full cascade, and λ ↦ τ(F_λ) is unimodal. (c) τ(F) = 0 iff F(0) = 0: two dormant crowds merge dormant; a dormant crowd merged with any live one is live. *Proofs* as stated. [derived, shown]

**1.4 Theorem (ignition).** τ(F_m) > max(τ_1, τ_2) is possible. Smallest example: a crowd of one with threshold 1/6 (dormant, τ_1 = 0) merged with a crowd of two with thresholds {0, 2/3} (τ_2 = 1/2) gives F_m(0) = 1/3, F_m(1/3) = 2/3, F_m(2/3) = 1: τ(F_m) = 1. A **necessary** condition, with τ_low ≤ τ_high = M: F_low(M) > M ("latent pressure": the lower crowd, at the higher crowd's equilibrium share, would exceed it), since otherwise F_m(M) ≤ M and M ∈ P(F_m). The set of weights λ that ignite is an interval; with a margin, latent pressure is also sufficient. *Proof of necessity* as stated; the interval and sufficiency-with-margin are proved in `sim/results/mixture_equilibria.md` M7 and await audit. [derived, shown]

*Reading.* Ignition needs neither a dormant part nor a large one; two crowds that each recruit nobody beyond their instigators can ignite together (1,428 such pairs found [computed]). It is the formal content of "a group is more than its members" for this law.

**1.5 Proposition (what fails).** τ(F_m) ≤ max(τ_1, τ_2) is false (1.4); τ(F_m) ≥ λτ_1 + (1−λ)τ_2 and ≤ are both false (31.8% and 26.6% of 255,568 random pairs where they can differ, [computed]); the average bound from below holds when neither part recruits beyond its instigators (M10, [derived, shown]).

**1.6 Proposition (non-reducibility).** τ(F_m) is not a function of (τ_1, τ_2, n_1, n_2): two pairs with identical (τ_1, τ_2, n_1, n_2) have merged equilibria 1 and 1/3 (`sim/results/mixture_equilibria.md` §5). *Consequence:* a group-level drive state for this law must carry the excess function E_F (equivalently the threshold distribution), not any summary of it. This is the definitional claim of this file.

**1.7 Corollaries for split.** min(τ_A, τ_B) ≤ τ(whole); no split makes both parts strictly more active than the whole; cutting by threshold gives τ_B ≤ τ ≤ τ_A. [derived, shown] By contrast the escalation certificate is hereditary under split (models/01 2.1) and never improves under merge (ρ(Γ_m) ≥ max ρ_i): the two kinds of group state compose in opposite directions, which is why one law cannot serve both.

**1.8 Numerics [computed].** Exact rational arithmetic on a 10⁷ grid, 829,756 random merge pairs (n from 10 to 10,000; uniform, beta, bimodal, clipped-normal, Granovetter families) plus exhaustive small cases and an independent pure-Python re-implementation: zero violations of 1.2–1.7; ignition in 14.1% of random pairs where it is possible; in 27.8% of fair-coin splits of cascading wholes some part is strictly more active than the whole; fair-coin splits kill about half of cascades. Script `sim/explore/mixture_equilibria.py`; results `sim/results/mixture_equilibria.md`.

**1.9 Conjecture.** For two crowds drawn i.i.d. from one population whose first crossing of the diagonal is transversal, P(ignition) → 0 as sizes grow, at about n^{−1/2}. [conjecture; linearisation heuristic in the results file]

**1.10 Validity domain and test.** The law is v0.1's crowd law with its two-sided gate switched off (monotone F); era-free as a theorem; its empirical content is whatever F is. *Refutation test:* a merger of two mobilised groups whose combined action exceeds the upper end of the sandwich (the least share at which both would have stopped alone) refutes the model's merge law as a description of that merger. *Data candidates:* merged protest coalitions with per-group participation (089's event data cannot do it; a per-member panel can); online community mergers with per-member activity.

## Queued claims (stated, not yet worked)

- **Claim 2. The medium is an operator on the gain matrix** (D611): a feed's ranking rule rewrites Γ; the certificate is a design constraint on it; Bail 2018's sign flip as a case.
- **Claim 3. Non-human members** (D612): from models/01 Corollary 3.4 (exact), a broadcast-only agent cannot create an escalation loop; a reactive one can, with safe loop gain c_{p·}(I − Γ)^{-1}c_{·p} < 1.
- **Claim 4. Levers that survive being known** (D613): consent-based anchoring levers remain effective under reflexivity; gate-manipulating levers decay.
- **Claim 5. Our own sign law** (D614): after batch 4's reads; directional, with a first-tie asymmetry, since the Newcomb test refuted the symmetric rule (v0.1 §7); tested on the modern signed data of file 117.
