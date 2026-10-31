# Composition theorems on the certificate, steering levers, and the validity column

_2026-10-31, revised the same day after next-pattern's audit (every theorem correct; 3.2's proof made self-contained; 3.3 and 3.4 made exact). Written by the session itself on Aldred's "go on all"; to be folded into v0.2 once batch 4 (where signs come from; drift and datedness) lands. Provenance: every theorem below is [derived, shown]; the objects it acts on are v0.1's (models/00-v0.md §5, ledger L3996 [read] for small-gain, L4467 [derived] for the (n−1)g row sums). Nothing here uses a line marked ⚠._

## 1. Why this exists

v0.1 declared absent any law for the drive *state* of a merged or split group (its §5, citing 083's inventory). It does own one object that composes: the no-escalation certificate, small-gain in the form ρ(Γ) < 1 on the gain matrix Γ = (γ_ij), γ_ij ≥ 0 the gain from j to i, γ_ii = 0. The two theorems below are the first composition laws in the project that are *about* merging and splitting groups. They are modest, they are about certificates rather than states, and they are proved.

**Standing facts used.** (F1) For non-negative matrices, 0 ≤ B ≤ A entrywise implies ρ(B) ≤ ρ(A) (Perron–Frobenius monotonicity). (F2) For any matrix, ρ(A) ≤ ‖A‖_∞ = max_i Σ_j |a_ij|. (F3) For non-negative A with ρ(A) < 1, I − A is a non-singular M-matrix, (I − A)^{-1} = Σ_k A^k ≥ 0.

## 2. Split inherits the certificate

**Theorem 2.1 (split).** Let a group G with gain matrix Γ satisfy ρ(Γ) < 1. Let G split into blocks B_1, …, B_k (any partition) and let each fragment keep only its internal gains, Γ_B = Γ restricted to B × B. Then ρ(Γ_B) < 1 for every block B.

*Proof.* Pad Γ_B with zeros to a matrix Γ'_B of the size of Γ. Then 0 ≤ Γ'_B ≤ Γ entrywise, so by (F1) ρ(Γ_B) = ρ(Γ'_B) ≤ ρ(Γ) < 1. ∎

*Reading.* A fragment of a certified group is certified: splitting can never create an escalation loop that the whole did not already have. The converse is false: two certified fragments can form an uncertified whole. Smallest case: two singletons (Γ_1 = Γ_2 = [0], certified) joined by c_12 = c_21 = 1 give Γ_m = [0 1; 1 0], ρ = 1. So in v0.1's dynamics splitting is *safe* for the certificate and merging is where the risk lies, which is the asymmetry 083 asked for a law about.

*Scope.* The certificate certifies no self-amplification (ISS of the interconnection, v0.1 §5); it says nothing about *which* partition forms or whether the fragments' states differ. It is a composition law for a guarantee, not for a state.

## 3. Merge needs a condition

Let G_1, G_2 be certified (ρ(Γ_1) < 1, ρ(Γ_2) < 1) and let the merged group have

  Γ_m = [ Γ_1  C_12 ; C_21  Γ_2 ],  C_12 ≥ 0 the gains members of G_1 receive from members of G_2, C_21 likewise.

**Theorem 3.1 (merge, row-sum form).** If for every member i of the merged group the total incoming gain, old plus cross, is below one — Σ_j (Γ_m)_ij < 1 for all i — then ρ(Γ_m) < 1.

*Proof.* (F2): ρ(Γ_m) ≤ ‖Γ_m‖_∞ = max_i Σ_j (Γ_m)_ij < 1. ∎

**Theorem 3.2 (merge, block form; sharper).** With ρ(Γ_1) < 1 and ρ(Γ_2) < 1, ρ(Γ_m) < 1 if and only if ρ( (I − Γ_1)^{-1} C_12 (I − Γ_2)^{-1} C_21 ) < 1.

*Proof (self-contained; uses only (F3) and the Collatz–Wielandt bound: for P ≥ 0 and x > 0 componentwise, ρ(P) ≤ max_i (Px)_i / x_i).* Write A = I − Γ_1 and P' = (I − Γ_2)^{-1} C_21 A^{-1} C_12, so ρ(P') = ρ(P) by ρ(XY) = ρ(YX).

(⇒) Suppose ρ(Γ_m) < 1. By (F3) x := (I − Γ_m)^{-1} 1 exists, x = 1 + Γ_m x ≥ 1 > 0, and (I − Γ_m)x = 1. With x = (x_1; x_2), row block 1 gives x_1 = A^{-1}(1 + C_12 x_2) ≥ A^{-1} C_12 x_2, and row block 2 gives x_2 = (I − Γ_2)^{-1}(1 + C_21 x_1) ≥ (I − Γ_2)^{-1} 1 + P' x_2. Since (I − Γ_2)^{-1} = Σ_k Γ_2^k ≥ I, the first term is ≥ 1 > 0, so P' x_2 < x_2 componentwise with x_2 > 0; Collatz–Wielandt gives ρ(P') < 1.

(⇐) Suppose ρ(P') < 1. Then (I − P')^{-1} = Σ_k P'^k ≥ 0, and S := (I − Γ_2) − C_21 A^{-1} C_12 = (I − Γ_2)(I − P') is invertible with S^{-1} = (I − P')^{-1}(I − Γ_2)^{-1} ≥ 0. The block-inverse formula for [A, −C_12; −C_21, I − Γ_2] (Schur complement S of A) gives (I − Γ_m)^{-1} with blocks A^{-1} + A^{-1} C_12 S^{-1} C_21 A^{-1}, A^{-1} C_12 S^{-1}, S^{-1} C_21 A^{-1}, S^{-1}; every factor is non-negative, so (I − Γ_m)^{-1} exists and is ≥ 0. Put y := (I − Γ_m)^{-1} 1; then y = 1 + Γ_m y > 0 and Γ_m y = y − 1 < y, so ρ(Γ_m) < 1 by Collatz–Wielandt. ∎

*(Proof supplied by next-pattern's audit, 2026-10-31, replacing a sketch that leaned on M-matrix theory; checked line by line here. Numerically: 3,000 random draws, block sizes 1–5, cross-gains up to 2, the two sides agreed in every draw.)*

*Reading.* The merged group escalates only through the **loop** G_1 → G_2 → G_1: cross-gains one way, amplified by the receiving group's own internal loop (I − Γ_2)^{-1}, back the other way, amplified by (I − Γ_1)^{-1}. Two certified groups with cross-ties in one direction only (C_21 = 0 or C_12 = 0) are always certified. Reciprocal cross-ties are what can break it.

**Corollary 3.3 (uniform cliques; the exact size law).** Let G_1 be a complete graph on n_1 members with uniform internal gain g_1, so ρ_1 := ρ(Γ_1) = (n_1 − 1)g_1 < 1 (L4467), likewise G_2 with (n_2, g_2), and let every cross tie carry gain c. Then the merge is certified **iff**

  c² < (1 − ρ_1)(1 − ρ_2) / (n_1 n_2),  i.e.  c < √( (1 − ρ_1)/n_2 · (1 − ρ_2)/n_1 ).

*Proof.* Γ_1 1 = ρ_1 1, so (I − Γ_1)^{-1} 1 = 1/(1 − ρ_1) · 1, likewise for Γ_2. With C_12 = c·J (n_1×n_2) and C_21 = c·J (n_2×n_1), P = (I − Γ_1)^{-1} C_12 (I − Γ_2)^{-1} C_21 = c² n_2 /((1 − ρ_1)(1 − ρ_2)) · 1 1ᵀ, rank one with ρ(P) = n_1 n_2 c² /((1 − ρ_1)(1 − ρ_2)); apply 3.2. ∎ Equivalently, by the equitable partition, ρ(Γ_m) is the spectral radius of the 2×2 quotient [ρ_1, n_2 c; n_1 c, ρ_2].

*Remark (the row-sum version).* Theorem 3.1 gives the sufficient condition c < min( (1 − ρ_1)/n_2 , (1 − ρ_2)/n_1 ); the exact threshold is the geometric mean of those two bounds, so 3.1 is conservative here: on 2,000 random uniform-clique merges the exact law certified 669 and the row-sum bound 453 (next-pattern's check). Example: n = (10, 2), ρ = (0.45, 0.10): the bound allows c < 0.090, the truth is c < 0.157.

*Reading.* The cross-gain a merger can tolerate falls like 1/√(n_1 n_2) — symmetric in the two groups — and with the square root of the **product** of the two slacks 1 − ρ_i. (A first version of this file stated the row-sum form's asymmetric scaling, 1/n of the other group; that was the bound's scaling, not the law's. Corrected 2026-10-31 after the audit.) This is a prediction about size v0.1 did not have: **larger merged groups need weaker cross-ties, or more slack in both parts, to stay certified**, and the two groups' sizes enter symmetrically. Whether real groups behave this way is testable on fission–fusion and community-lifetime data (Palla's leave probability rising with w_out/(w_in + w_out), L4468, is the natural first comparison, though it is about leaving, not escalation).

**Corollary 3.4 (one member joins; exact).** Let a certified group G (gain matrix Γ, ρ(Γ) < 1) admit one person p, with c_{·p} ≥ 0 the column of gains members receive from p and c_{p·} ≥ 0 the row of gains p receives from them. Then the enlarged group is certified **iff**

  c_{p·} (I − Γ)^{-1} c_{·p} < 1.

*Proof.* Take G_2 = {p}: Γ_2 = [0], (I − Γ_2)^{-1} = 1, and P = (I − Γ)^{-1} c_{·p} c_{p·} is rank one with ρ(P) = c_{p·}(I − Γ)^{-1} c_{·p}; apply 3.2. ∎

*Reading.* A newcomer is safe iff their influence on the group, propagated through the group's own loop (I − Γ)^{-1} = Σ_k Γ^k, and returned along what they receive, sums to less than one. The row-sum version (Σ_j c_pj < 1 and every member's total stays below one) is sufficient but not needed.

## 4. Steering levers, read off the certified laws

Every term in a certified law is a lever: something an outsider or a member can change, with a predicted effect on the certificate or on the partition. v0.1 had no intervention operators; these are the ones it already implies. Each names its term, its predicted effect, and the practitioner literature already catalogued that uses it (file numbers), so that cluster O (applied practice) and cluster Q (social control) can later check whether practice matches prediction. Ethics tag per the ledger: whether the lever works with the target's consent.

| Lever | Term it moves | Predicted effect (v0.1/this file) | Already catalogued as practice in | Ethics |
|---|---|---|---|---|
| Strengthen anchoring: raise a member's w_i (identity, commitment, private conviction) | D1 set-point weight; certificate w_i > 2E_i (v0.1 6.1) | moves the group toward the no-split regime; reduces the effect of all couplings on that member (6.2) | commitment and cohesion practice (24, 38); sacred values (37); Kuran's integrity term (089) | consent (when it is the member's own conviction); manipulation (when induced) |
| Weaken enemy ties: reduce |a_ik| for k ∈ enemies(i) (mediation, separation, reduced contact) | E_i in the certificate; cross-gains C_12, C_21 in 3.2 | directly loosens the certificate's binding constraint; in a merger, the only way to make reciprocal cross-ties safe | mediation and reconciliation (31, 13); contact hypothesis conditions (13) | consent |
| Flip a sign: turn a negative tie positive (reconciliation; a common enemy) | sgn(a_ij), an input in v0.1 §2.2 | changes the balance partition (4.2b) and the faction readout (5.1); a common enemy is the threat → in-group-positive generator D603 is reading | reconciliation (31); superordinate goals, Sherif (13); threat → cohesion (24, 39) | consent (reconciliation); manipulation (manufactured enemy) |
| Shift a gate threshold: raise θ_i or θ̄_i (cost of joining; fear appeals; efficacy messages) | crowd gate (4.4a–b); dyad gates K⁻, K⁺ | moves fixed points of F; can create or remove the second stable equilibrium Kuran's comparative statics need (L3968) | fear appeals and efficacy (35); repression as a threshold shift (089); deterrence (39) | manipulation (most), consent (information that is true) |
| Change what members can see: the sensing range r, who hears whom | Leonard's θ_c = 2·arccos r (4.3b); the wiring in 3.2 | smaller r raises θ_c: a team compromises over a wider range of goal angles before it chooses; wiring one-way removes the loop in 3.2 | communication structure, hierarchy (07, 38); platform design (D606) | consent (structure agreed) / manipulation (hidden) |
| Add an uninformed majority | N_3 in (4.3a); ω_i = 0 members | returns control to the numerical majority (Couzin, L3879) | — | n/a |
| Partition deliberately: split a group before escalation | Theorem 2.1 | a fragment of a certified group is certified; splitting cannot create a loop | organisational design (38, O) | consent |
| Control a merger's cross-ties | Theorem 3.2, Corollary 3.3 | merge is safe iff the two-way loop gain is below one; one-way ties are always safe | mergers, alliances (10, 39) | consent |

What the table does **not** claim: magnitudes. Every lever's effect size is era- and medium-bound (§5); the table is the list of operators the certified form supports, which is what an algebra of steering needs first.

## 5. The validity column (fluidity)

Aldred, 2026-10-31: consider accelerated change and the datedness of theories. Adopted here as a design rule for v0.2 and after:

- Every law in the equation set carries a **validity domain**: era of the data it was fitted on, medium (face-to-face, online, mixed, animal), population, size range. The ledger carries `era` and `medium` on every empirical line from batch 4 on, and D608 back-fills v0.1's.
- **Forms are era-invariant given their hypotheses; magnitudes are not.** Theorems 2.1, 3.1, 3.2, v0.1's 6.1, 6.3 and 6.4 hold for any gains and signs that satisfy their hypotheses, in 1956 or 2026. Whether a given group's gains satisfy them is an empirical question whose answer moves with the medium (064: contagion on feeds d ≈ 0.01 per person-week, against face-to-face couplings) and with time (D605). A magnitude older than the medium it is used for is a hypothesis, not a parameter.
- **The set is modular.** Each adopted law is a plug with its domain stated; a replaced magnitude or a swapped sign-generator does not touch the theorems; the testbed can hot-swap them.
- **Reflexivity is a term in the validity domain.** Publication and use can move the parameters (093; performative stability needs ε < γ/β, L4118). A law that has been used to steer a group has, by that use, a smaller validity domain than before.

## 6. What belongs in sim/ from this file

Regression tests, each citing this file: (a) 2.1 on random non-negative Γ with ρ < 1 and random partitions (every block's ρ < 1); (b) 3.1 on random block matrices (row sums < 1 ⇒ ρ < 1) and a counterexample where ρ(Γ_1), ρ(Γ_2) < 1 but ρ(Γ_m) ≥ 1; (c) 3.2's iff, numerically, on random blocks with ρ(Γ_i) < 1 (check both directions on many draws); (d) 3.3's exact law against ρ(Γ_m) computed directly, and against the 2×2 quotient; the row-sum bound's conservativeness has the closed form √(b_1 b_2)/min(b_1, b_2) with b_1 = (1 − ρ_1)/n_2, b_2 = (1 − ρ_2)/n_1 — check it; (e) 3.4's exact scalar against ρ(Γ_m) on random instances.
