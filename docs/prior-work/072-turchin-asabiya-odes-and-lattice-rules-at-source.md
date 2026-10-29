# Prior work 072: Turchin's asabiya ODEs and lattice rules at source

Direction: D339

Date: 2026-10-29. Kind: deep-read. Question: frontier gain, scale loss and collapse threshold in Turchin's asabiya model, and whether they are testable. Merges the 08 asabiya direction and the 18 asabiya source check.

**Method and honesty note.** Read in full this session: Cheon and Poghosyan (arXiv 1512.07715v2, downloaded and text-extracted); Turchin and Gavrilets 2009 (full PDF); Turchin, Currie, Turner and Gavrilets 2013 (PMC full text; the Methods equations are images, which I downloaded and viewed one by one). Read as a page only: the CoMSES NetLogo replica (description page, no code). **Not accessed:** *Historical Dynamics* (2003) itself (book, paywalled; the Crossref record exists but no text), Turchin 2009 *J Global History*, Gavrilets, Anderson and Turchin 2010, and the PNAS SI Appendix. So the 2003 ODE is quoted from a *second paper that restates it* (Cheon and Poghosyan, eq. 2), tagged `[read, restated]`, not from the book. The 2003 **lattice update rules were not obtained anywhere**; this file says so rather than reconstructing them. The web search budget ran out mid-task, so the one planned search for the book's equations was not made; a follow-up could try it. Tags: `[read]` source text read; `[read, restated]` a read paper restating Turchin; `[derived]` my own algebra or numerics, checked this session; `[not obtained]`.

---

## 1. Headline findings

1. **The asabiya ODE and the lattice rules are two different models, and the 2013 PNAS model has no asabiya in it at all.** The PNAS model's state is a binary vector of "ultrasociality traits" per grid cell; asabiya appears nowhere in the Methods `[read]`. Files 05, 08 and 18 treat the 2013 paper as the "later, larger test" of the asabiya theory. It tests a *neighbouring* theory (cultural multilevel selection plus military-technology diffusion), not the ODE.
2. **The two-variable ODE is confirmed and has a clean closed-form interior fixed point** (below). File 18's form is right; one gloss in file 18 is in doubt (what `h` means, section 3).
3. **Collapse in the ODE is not a threshold rule.** It is the exit of an unstable spiral through A = 0 `[derived]`. A threshold-and-restart "collapse" exists only in the lattice simulation, whose rules I could not get.
4. **Testability is poor for the ODE and moderate for the 2013 model.** Asabiya S has no measurement protocol in any source read. The 2013 model was tested against 7,941 data points, but its own Table 1 shows the fit comes from the military-technology seeding, not from anything about cohesion.
5. **Glaeser 2005 does not belong in this cluster.** It is "The Political Economy of Hatred", *QJE* 120(1), 45-86, DOI https://doi.org/10.1162/qjec.2005.120.1.45 [Crossref confirmed] (file 18 §14), a supply-and-demand model of out-group hatred, with no asabiya, scale or frontier dynamics. The seed list for D339 carried it from file 18's scapegoating section; drop it from this direction.

---

## 2. Turchin 2003, the two-variable ODE (restated)

**Citation.** Turchin, P. (2003). *Historical Dynamics: Why States Rise and Fall*. Princeton University Press. DOI https://doi.org/10.1515/9781400889310 (Crossref: Turchin, 2004 record date). The metaethnic frontier theory is chapter 4 per the CoMSES page `[read]`.

**Their vocabulary.** Asabiya (from Ibn Khaldun): "the social cohesion that plays the key role in the growth and the decay of a polity", a "non-material resource" `[read, restated]`. Polity size A. Metaethnic frontier.

**Drives/operands.** One polity with two scalars: size A(t) (population, area or GDP; Cheon and Poghosyan say any of the three, p. 2) and asabiya S(t), with 0 ≤ S ≤ 1.

**Equations `[read, restated]`** (Cheon and Poghosyan eq. 2, which is their eq. 1 with R = 0; they attribute it to Turchin [1, 2] without page):

    dA/dt = c·S·A·(1 − A/h) − a
    dS/dt = r·(1 − A/(2b))·S·(1 − S)

Parameter glosses as Cheon and Poghosyan give them: `h` is the growth limit of A set "by the natural resource of the land"; `a` is a constant term that "gives the threshold": when the first term is below `a`, A declines; `b` is such that S's growth rate "is higher for smaller size of the population and it becomes zero at the critical population A = 2b"; c and r are rate scales. File 18 reads `h` as "the spatial scale of power projection" and `a` as "geopolitical pressure from the hinterland". **These two glosses disagree on `h` and are different readings of `a`; I cannot adjudicate without the book.** File 18's gloss came from a secondary excerpt; Cheon and Poghosyan's gloss is a reader's paraphrase. Both are `[not obtained]` at the source of the equation.

**Frontier gain, scale loss, collapse: how each sits in the equation.**
- *Frontier gain.* There is no separate "gain" term. S grows logistically at rate r·(1 − A/2b), positive when A < 2b: a small polity is mostly frontier, so cohesion is rebuilt `[read, restated]`. The equation encodes "small implies mostly frontier" only through the factor (1 − A/2b); no frontier length or contact variable exists.
- *Scale loss.* For A > 2b the same factor is negative, so S decays toward 0 (the logistic factor S(1 − S) keeps S in [0, 1]). The scale at which gain flips to loss is exactly A = 2b.
- *Collapse.* A has a constant sink `a`, so with S low enough A falls and, in finite time, reaches 0. No "collapse threshold" parameter is stated in the restated ODE.

**Derived fixed points and stability `[derived]`.** Setting both derivatives to zero (S = 0, S = 1 or A = 2b from the second equation):
- S = 1: A = (h/2)·(1 ± √(1 − 4a/(ch))). Hyperbolic. (Cheon and Poghosyan's eq. 3 prints 8a in place of 4a for the S = 1, R = 0 points because their c/(1+f) prefactor has f = 1 substituted; with f = 0 it reduces to this form. Wording corrected in validation.)
- Interior: A* = 2b, S* = a·h / (2cb(h − 2b)). Requires S* < 1 and 2b < h. (Matches their eq. 6 with f = 0.)
- Jacobian at (A*, S*): ∂Ȧ/∂A = c·S*·(1 − 4b/h) =: α; ∂Ȧ/∂S = a/S* =: β; ∂Ṡ/∂A = −r·S*(1 − S*)/(2b) =: −γ; ∂Ṡ/∂S = 0 (because A* = 2b zeroes the bracket). Trace α, determinant βγ = a·r·(1 − S*)/(2b) = ω₀².
- So the interior point is an **unstable spiral iff α > 0 (that is, 2b < h/2) and α² < 4βγ**, which is the condition for a single "rise and fall"; it is a stable point if 2b > h/2. This reproduces Cheon and Poghosyan's own statement that the point is an attractor for 2b > h/2 and a repeller for 2b < h/2 (their eq. 5-6, p. 5), and their period estimate T ≈ 2π/ω₀ = √(8π²b / (a·r·(1 − S*))) (their eq. 20; mine is the same expression from ω₀² above).
- Their printed eq. 16 gives γ = (a·r/2b)·S*(1 − S*). I get γ without the factor a, and their own eq. 18 (ω₀² = βγ = (ar/2b)(1 − S*)) is consistent only with my γ. Probably a typesetting slip in the preprint, or in the text extraction; it does not affect the later results `[derived]`.

**Numerical check `[derived]`** (Euler, dt = 0.01, c = 1, h = 1, a = 0.03, r = 0.25, b = 0.2, which are Cheon and Poghosyan's Fig. 1 values at R = 0): S* = 0.125, α = 0.025, β = 0.24, γ = 0.0684, α² − 4βγ = −0.065 < 0, predicted period 2π/ω₀ = 49.1 (49.3 if the damping-corrected frequency ω = √(ω₀² − α²/4) of their eq. 19 is used; the draft gave 49.3 under the 2π/ω₀ label, corrected in validation). Trajectories from (A, S) = (0.245, 0.25), (0.3, 0.3) and (0.38, 0.25) all rise, then A reaches 0 at t = 48.9, 46.0 and 102.1. So the single-rise-and-fall shape and the order of magnitude of the period are real consequences of the equations. Note that A hits 0 with S still positive (0.23, 0.21, 0.04): the ODE ends there; **it has no re-founding rule**.

**Theorems or derived predictions.** The one result in the literature is local stability analysis of the fixed point (above). Cheon and Poghosyan credit the unstable-spiral finding to Turchin's book ("It is shown that this set of equations ... can possess unstable spiral fixed point ... [1]", p. 3) `[read, restated]`; their own contribution is the explicit linearisation and period estimate. No global theorem about the two-variable system was found in what I read.

**Empirical standing.** Nothing in the sources read fits the ODE to a historical series. Cheon and Poghosyan state that, "with proper tuning of parameters", the *networked* multi-polity version "could even be made to resemble the real historical data" (citing their ref. [4], which is Turchin and Hall (2003), "Spatial synchrony among and within world-systems: insights from theoretical ecology", *J World-Systems Research* 9, 37-64, DOI https://doi.org/10.5195/jwsr.2003.248 [Crossref confirmed], not Turchin alone as the draft said; not read). That is an author-side fit, not a test. Be blunt: **no independent test of the ODE was found.**

**Operand/operator translation.** A polity-level state (A, S). S is a bounded group drive, with a size-dependent source and sink; this is the one group-drive ODE in the survey, and its algebraic content is small: one scalar with logistic dynamics gated by a sign flip at A = 2b.

---

## 3. Turchin 2003 chapter 4, the lattice (spatial) model

**What is known `[read]` from the CoMSES page.** Paul Smaldino, "Replica of Turchin's (2003) Metaethnic Frontier model", CoMSES Computational Model Library, v1.0.0, 15 Feb 2026, NetLogo 6.4, AFL-3.0 licence, unreviewed, no DOI, 18 downloads: https://www.comses.net/codebases/15a2fc42-90bd-42c4-b21b-dfba428cdb16/releases/1.0.0/ . The page describes the mechanisms in words only:
1. regions bordering other groups gain asabiya from us-versus-them competition;
2. high asabiya improves growth, cooperation and war on neighbours;
3. the larger the frontier, the higher the empire's asabiya;
4. as an empire expands: access to resources drives growth; internal conflict lowers asabiya far from the frontier; a larger frontier reduces the ability to fight on all frontiers;
5. when asabiya falls too much the empire collapses, and a group with "more compelling asabiya" later establishes a new one.

The page lists **no equations, no update rules, no parameter names, and offers no downloadable files**. So the lattice update rules, the collapse threshold and the "frontier gain" function in the lattice model are `[not obtained]`. Statements in earlier files (08 "Exact functional forms … not checked") remain true.

**Tension between the page and the ODE worth noting.** The page says "the larger the frontier, the higher the asabiya", while the ODE gives S growth only when A is *small* (A < 2b). The two can be reconciled if "frontier" means border length per unit of area, which falls as an empire grows. That reconciliation is my reading, not stated in either source `[derived, unverified]`.

**Testability of the lattice model.** The model is open (NetLogo, now with a replica). Its parameters and rules cannot be audited without the book. A reimplementation from the book's text is possible *if the book is obtained*, and would be a clean D-direction (model).

---

## 4. Cheon and Poghosyan: the three-variable extension

**Citation.** Cheon, T., Poghosyan, S. S. (2017). Spiral orbits and oscillations in historical evolution of empires. *Physica A* 469, 353-362. DOI https://doi.org/10.1016/j.physa.2016.11.035 [Crossref confirmed]. Preprint arXiv:1512.07715v2 (Aug 2016), read in full. (File 18's note that arXiv 1512.07715 is *not* Turchin's source is confirmed here.)

**Their vocabulary.** Asabiya S; **metaasabiya** R, "cultural" assets (religion, science, art, entertainment) that ease internal tensions and provide technology; Spengler (Kultur to Zivilisation) and Toynbee (universal state, universal religion) as the motivation.

**Equations `[read]`** (their eq. 1; 0 ≤ S, R ≤ 1; f is the relative contribution of R to growth):

    dA/dt = (c/(1+f))·(S + f·R)·A·(1 − A/h) − a
    dS/dt = r·(1 − A/(2b))·S·(1 − S)
    dR/dt = q·(1 − A/(2d))·S·R·(1 − R)

R's growth needs S > 0 ("the presence of larger value of asabiya is the prerequisite"), and its sign flips at A = 2d with 2d typically above 2b. Their interesting regime is 2b < h/2 < 2d.

**Results `[read]`.** Fixed points on the unit cube (their eqs. 3-7): four hyperbolic points with S = 1 and R = 0 or 1 (eq. 3; the draft called these "curves"); a curve S = 0, R = a(1+f)/(c·f·A(1 − A/h)) of attractors for A > 2b and repellers for A < 2b; the point (A, S, R) = (2b, S*, 0) with S* = a(1+f)h/(2cb(h − 2b)), attracting if 2b > h/2 and repelling if 2b < h/2. For b = d the trajectory obeys the invariant dS/dR = (r/q)(1 − S)/(R(1 − R)) (their eq. 8-9). For 2b < h/2 < 2d the system has a "repeller axis" (their eq. 13-14) around which orbits spiral while drifting from R = 0 toward S = 0; the linearised oscillation about the R = 0 end gives their eqs. 15-20, whose R = 0, f = 0 limit I rederived above. Their Fig. 1 shows four qualitative outcomes (one rise and fall; two cycles then permanence; two cycles then fall; small oscillation then stability) at c = f = h = 1, a = 3/100, r = q = 1/4, b = 1/5, d = 2/5, varying only A(0) from 0.245 to 0.405.

**Empirical standing.** None. The paper is a dynamical-systems study; "agree very well with our knowledge on the evolution of historical polities" is qualitative, with no data fitted `[read]`. Author-side only; I found no citation of it as tested.

**Operand/operator translation.** The one place where a *second* group-level scalar is added to the first with an explicit dependency (R needs S). It shows the pattern for composing group drives: each additional drive is a logistic with its own size-gate, and the growth of one is a precondition for another.

---

## 5. Turchin and Gavrilets 2009

**Citation.** Turchin, P., Gavrilets, S. (2009). Evolution of complex hierarchical societies. *Social Evolution & History* 8(2), 167-198. PDF read in full: https://volweb2.utk.edu/~gavrila/papers/turchin-gavr.pdf (Crossref has no usable record for this journal; page range from the PDF header).

**What it contains `[read]`.** A review plus a verbal description of an agent-based model: hexagonal grid of "villages" with Gaussian base-line resources; polities are trees (chief community, superiors, subordinates); each subordinate pays a fixed proportion of its resources as tribute; polity power is the chief community's total resource; every "year" (time is continuous; a year is the expected interval between a community's decisions) the chief decides whether to attack the **weakest neighbour**, subordinates decide whether to secede (if they calculate the old master's attack will be repelled); attack success uses a **Lanchester-Osipov** form (linear and quadratic variants tried); a span-of-control limit (tunable, 4 to 10) forces demotion when slots run out; secession takes all of a seceder's subordinates with it and disconnected parts secede too. Qualitative result: low warfare intensity gives "chiefly cycling" between one-community polities and 2-3-level polities; high intensity gives up to six or more levels and periodic fissioning (Fig. 4). The full description was "reported elsewhere (Gavrilets, Anderson and Turchin 2010)", not read here.

**What it does not contain.** No asabiya variable, no ODE, and no equations at all for the agent-based model (functional forms are named, not given). So **file 18's "Turchin and Gavrilets co-authored later work (2009 …)" in the asabiya context is misleading**: the 2009 paper is about hierarchical complexity under warfare, and asabiya does not enter its model. Empirical section (verbal, one-line proxies), reporting results of Turchin (2009b), i.e. Turchin 2009 *J Global History*, not new analysis in TG2009: metaethnic-frontier location as proxy for warfare intensity; 65 "megaempires" (peak territory > 1 million km²) with over 90% in or beside the Afroeurasian arid belt; China unified 14 times, all but one (Ming) from the north; South Asia 9 unifications, 5 from the northwest. These are counts and associations, not tests of any equation.

---

## 6. Turchin, Currie, Turner and Gavrilets 2013

**Citation.** Turchin, P., Currie, T. E., Turner, E. A. L., Gavrilets, S. (2013). War, space, and the evolution of Old World complex societies. *PNAS* 110(41), 16384-16389 (published 23 Sep 2013), DOI https://doi.org/10.1073/pnas.1308825110 [Crossref confirmed]. PMC3799307. Read in full; Methods equations transcribed from the article's own equation images.

**Their vocabulary.** Cultural multilevel selection (CMLS); **ultrasocial** norms and institutions; military technology (MilTech); macrostates; ethnocide; steppe frontier.

**Drives/operands.** A grid cell (100 × 100 km squares of Afroeurasia, 2,647 agricultural cells) holds a community with two binary vectors, U (ultrasociality traits) and M (MilTech traits). Cells aggregate into polities. "Asabiya" does not appear in the Methods; the nearest analogue is the average U per polity, Ū.

**Operators and equations `[read]`** (discrete time; border cells are sampled each year; the attack probability between two polities is proportional to the length of their shared boundary):

    Ū_att = (Σ_j Σ_i u_ij) / S_att
    P_att = 1 + β·Ū_att·S_att
    P_def = 1 + β·Ū_def·S_def + γ·E_def
    P_success = (P_att − P_def) / (P_att + P_def)          (attack fails if negative)
    ū (mutation equilibrium) = μ01 / (μ01 + μ10),   with μ01 << μ10
    P_ethnocide = ε_min + (ε_max − ε_min)·M̄_att − γ1·E_def (nothing if negative)
    P_disint = δ0 + δ_s·S − δ_a·Ū        (clipped to [0, 1]; each polity dissolves into its communities)

where S is the polity size in cells, E_def the elevation of the defending cell in km, M̄_att the attacker's mean MilTech fraction in [0, 1], β, γ, γ1, ε_min, ε_max, δ0, δ_s, δ_a, μ01, μ10 coefficients. (The equation images give these forms; the text's variable list and the two-sentence glosses match.) MilTech traits start at 1 in cells bordering the steppe and diffuse by a random-neighbour copy at rate σ, never lost. Ultrasocial traits are gained at μ01, lost at μ10, and copied wholesale (0s and 1s) from attacker to defender on ethnocide. Success is for the attacker if power is higher; annexation can bring ethnocide.

**This is where "scale loss" and "collapse threshold" live in the 2013 model.** `P_disint` rises linearly with size S and falls with average ultrasociality Ū: bigger polities are more likely to dissolve, more cohesive ones less so. That is the *same qualitative shape* as the asabiya ODE (scale erodes cohesion, cohesion resists collapse), but with a different state variable and a *probabilistic* collapse. The ODE's flip at A = 2b has no counterpart here: δ_s·S is linear in size with no threshold.

**Theorems.** None; it is a simulation.

**Empirical standing `[read]`.** Tested on 7,941 points (2,647 agricultural cells × 3 eras of 500 years each, 1500 BCE to 1500 CE), imperial density maps built from historical atlases for polities over about 100,000 km². Model output averaged over 20 realisations. Table 1 (R²): full model 0.56 / 0.65 / 0.47 by era and **0.65 overall**; no elevation effect 0.48 overall; no effect of MilTech on ethnocide **0.16**; MilTech seeded randomly instead of on the steppe interface **0.17**. Separate spatial-autoregression analysis: distance from steppe is the strongest predictor, then long-term agriculture then elevation, together explaining 42%. The paper says 12 parameters, four with substantial effect, and R² about 0.5 or better over a broad range of parameters.

**Blunt reading.** (a) The test is of *where large polities were*, not of how any group's cohesion changed over time. (b) The authors' own ablation says the fit is carried by the steppe-seeded MilTech diffusion, a geographic prior; turning off the "ultrasociality" mechanism was **not** among the ablations in Table 1, so the paper does not show that the *cultural-selection* mechanism is needed for the fit. A model with MilTech diffusion alone, and no trait dynamics, may do as well; that control is missing. (c) Authors tested their own model against a dataset they assembled; no replication by an independent group was found in this session. (d) It is the CMLS model, not the asabiya model.

**Operand/operator translation.** Operands: a community with two bit-vectors. Operators: attack (probabilistic, power-ratio), annex, ethnocide-copy, mutate, diffuse, disintegrate. Here operators genuinely act on communities with a neighbour relation, which is closer to the algebra's "operators between actors" than the ODE. A group drive appears only as an average of binary traits.

---

## 7. Is any of it testable? A direct answer per claim

| Claim | State variable measured? | Test in the literature | Verdict |
|---|---|---|---|
| S grows when A < 2b, decays when A > 2b | No protocol for S | none found | Not testable until S has a proxy |
| Interior fixed point (2b, S*) is an unstable spiral iff 2b < h/2 | no | none | Math is checked `[derived]`; empirical meaning of b, h, a unknown |
| Single rise-and-fall with period T = √(8π²b/(a·r·(1−S*))) | A only (area, population) | author-side tuning only (via Cheon and Poghosyan's citation of Turchin) | Testable in principle with polity-area time series; not done independently |
| Polities rise on metaethnic frontiers | frontier location | Turchin 2003 Table 5.1 (not read); Turchin 2009b counts as summarised in TG2009, 65 megaempires | Associational; steppe proxy is the best-supported piece |
| Large polities arise where MilTech diffuses first, via ultrasociality selection | cell-level large-polity occupancy | PNAS 2013, R² 0.65 | Fit real for the geographic pattern; the ultrasociality mechanism is untested separately |

**What would make S testable.** None of the sources define a measurable S. Candidate proxies would be a political-instability or elite-conflict index, or Seshat variables, but doing so is a research task, not something found. Related: file 08 notes the Seshat moralizing-gods retraction as the warning about coding; D342 covers it.

---

## 8. What exists vs what does not

**Exists.**
- A two-variable ODE for size and cohesion with an analytically tractable interior fixed point and an unstable-spiral regime, now independently re-derived `[derived]` and matching a second group's analysis `[read]`.
- A three-variable extension with a second group-level "resource" whose growth is conditional on the first, with a stated qualitative phase portrait.
- A spatial agent-based model with explicit equations for attack, annexation, ethnocide and disintegration (2013), tested for geographic fit with a decomposed R².
- A third-party NetLogo replica of the 2003 lattice model, with no published rules.

**Does not exist (as far as this read goes).**
- Any measured value of S, or independent fit of the ODE to time series.
- Any published rule set for the 2003 lattice model that I could read; the replica and the book are the only routes.
- Any link between the ODE and the 2013 model: no paper read derives one from the other.
- A group-drive vocabulary beyond a single scalar: no drive for fear, curiosity or desire, and no individual-level operand. In 2013 the "drive" is a bit-vector mean.
- Any theorem about the lattice model.
- Any algebra: no composition law for operators; the 2013 operators (attack, annex, ethnocide, mutate, diffuse, disintegrate) are listed as simulation steps with no closure or commutativity claims.

**For the algebra.** The reusable pieces are small: (1) a bounded group scalar with a size-gated sign (A < 2b gain, A > 2b loss); (2) a second scalar gated on the first (R needs S); (3) a size-up, cohesion-down disintegration probability (P_disint); (4) a power-ratio attack kernel (P_success = (P_att − P_def)/(P_att + P_def)) and a trait-copy operator (ethnocide). Of these, (4) is an operator on two groups and is the closest thing to what the algebra needs.

---

## Unconfirmed

- The book's own statement of the ODE, its parameter definitions (`h`, `a`, `b`) and whether Turchin writes it as here (all `[read, restated]` via Cheon and Poghosyan). File 18's glosses of `h` and `a` conflict with theirs.
- The lattice-model update rules, the form of "frontier gain" and the collapse trigger in *Historical Dynamics* ch. 4; the NetLogo code of the CoMSES replica (not downloadable from the page).
- The PNAS SI Appendix (parameter values, the 12 parameters, the exact atlases) and whether any independent reimplementation exists.
- Gavrilets, Anderson and Turchin 2010, *Cliodynamics* 1: DOI 10.21237/c7clio11193 resolves (Crossref, landing page https://escholarship.org/uc/item/5536t55r), but I did not read the paper.
- Turchin 2009, "A theory for formation of large empires", *J Global History* 4(2), 191-217, DOI 10.1017/S174002280900312X resolves (Crossref gives 191-217; TG2009's reference list says 191-207, so take Crossref); not read. File 08's "Turchin (2009b)" in TG2009 is probably this.
- Whether the 2019 Currie, Turchin and Gavrilets preprint ("History of agriculture and intensity of warfare shaped the evolution of large-scale human societies", OSF, DOI 10.31235/osf.io/9kmrw, found in Crossref only) extends or independently tests the 2013 model.
- The claim, in Cheon and Poghosyan's introduction, that the networked multi-polity version was tuned to resemble historical data (their ref. [4], identified in validation as Turchin and Hall 2003, *JWSR*, DOI 10.5195/jwsr.2003.248); the paper itself not read.
- Whether the extra factor a in Cheon and Poghosyan's eq. 16 is a typo or an extraction error; only the downstream equations were checked.
- (Validation) The PNAS 2013 body text (Table 1 except the 0.65 and 0.16 figures, Methods equations, 7,941 points, 20 realisations, 12 parameters, 42% spatial regression) could not be re-read in the validation pass: PMC sat behind a browser check, Europe PMC returned errors, pnas.org returned 403, and the web-search budget was used up. These rest on the drafter's reading alone. The abstract (Europe PMC) confirms 65% overall and 16% for the model without diffusing military technology.

## Validation log (2026-10-29)

- Turchin 2003, *Historical Dynamics* (DOI 10.1515/9781400889310): ✓ exists, sole author Turchin, Crossref record dated 2004; book text still not obtained, so the ODE remains `[read, restated]`.
- Cheon and Poghosyan 2017, *Physica A* 469, 353-362 (DOI 10.1016/j.physa.2016.11.035) and arXiv 1512.07715v2: ✎ re-read the preprint. Eqs. 1, 2, 4-6, 8, 13-20, Fig. 1 parameters and outcomes, the h/a/b glosses and the quotes all match. Corrected: eq. 3 gives four points, not "curves"; eq. 3 prints 8a (f = 1 substituted); their ref. [4] is Turchin and Hall 2003, not Turchin alone. The claimed eq. 16 slip (extra factor a in γ) is confirmed: their eq. 18 holds only without it.
- Derived algebra and numerics: ✎ S*, α, β, γ and the three Euler trajectories (A = 0 at t = 48.9, 46.0, 102.1; final S 0.232, 0.21, 0.041) reproduced exactly. One fix: 2π/ω₀ = 49.1, and 49.3 is the damping-corrected period.
- Turchin and Gavrilets 2009, *Social Evolution & History* 8(2), 167-198: ✎ PDF re-read. Model description, span of control 4-10, Lanchester-Osipov, chiefly cycling, six or more levels, 65 megaempires, >90%, China 14 unifications (Ming the exception), South Asia 9/5 NW all confirmed; "asabiya" appears 0 times. Two fixes: time is continuous ("year" = mean decision interval), and the empirical counts are TG2009 reporting Turchin 2009b. No Crossref DOI (confirmed by a bibliographic query).
- Turchin, Currie, Turner and Gavrilets 2013, *PNAS* 110(41), 16384-16389 (DOI 10.1073/pnas.1308825110, PMC3799307): ✎ authors, title, issue and date confirmed; title added. Only the abstract could be re-read (65%, 16% confirmed); the rest is `?` for this pass (see the note above).
- Smaldino, CoMSES replica of Turchin's Metaethnic Frontier model: ✓ author, v1.0.0, 15 Feb 2026, NetLogo 6.4, AFL-3.0, unreviewed, no DOI, 18 downloads, no files listed, ch. 4, and all five mechanisms confirmed on the page.
- Gavrilets, Anderson and Turchin 2010, *Cliodynamics* 1(1) (DOI 10.21237/c7clio11193): ✓ resolves, title "Cycling in the complexity of early societies"; not read.
- Turchin 2009, *J Global History* 4(2) (DOI 10.1017/S174002280900312X): ✎ resolves; pages are 191-217 per Crossref (TG2009 cites 191-207).
- Currie, Turchin and Gavrilets 2019 OSF preprint (DOI 10.31235/osf.io/9kmrw): ✓ resolves with these authors and title; content unread.
- Turchin and Hall 2003, *JWSR* (DOI 10.5195/jwsr.2003.248): ✓ added in validation as Cheon and Poghosyan's ref. [4]; not read.
- Glaeser 2005, "The Political Economy of Hatred", *QJE* 120(1), 45-86 (DOI 10.1162/qjec.2005.120.1.45): ✓ added the DOI. The exclusion from this cluster stands.
- "Nothing exists" claims (no lattice rules published, no independent ODE fit, no measured S): ? Not re-searched, because the session's web-search budget was used up. Cheon and Poghosyan's own discussion (p. 13) calls relating asabiya to measurable quantities "an urgent task", which supports the "no measured S" claim as of 2016.

**Verdict.** The file is accurate on everything I could re-read: the equations, the glosses, the fixed-point and spiral analysis, the numerics and the TG2009 content all hold, and its two sharpest claims stand (the 2013 PNAS model has no asabiya, and Cheon and Poghosyan's eq. 16 has a stray factor a). The corrections are small attribution and wording fixes: ref. [4] is Turchin and Hall, the period figure was mislabelled, eq. 3 gives points rather than curves, and TG2009's counts belong to Turchin 2009b. I found no fabrications. The PNAS body numbers and the "nothing exists" claims remain checked by the drafter only.

## Cross-checks (2026-10-29)

Direction D339 checked against the other files in this directory (grep for Turchin, asabiya, Cheon, Poghosyan, Gavrilets, Glaeser, Lanchester, Seshat, 7,941). Files citing Turchin: 05 s18, 07 s13 and the forecast item, 08 s3/s4/s6/s7, 09 (Unconfirmed), 18 s15, 28 (Unconfirmed). Web search budget was exhausted, so no primary source could be fetched for the one real conflict; it is marked unresolved.

### Agreements
- 18 s15 and this file: same two-variable ODE (dS/dt = r(1 - A/2b)S(1 - S); dA/dt = cSA(1 - A/h) - a), same sign flip at A = 2b. Symbols differ only in c0/r0 vs c/r.
- 18 s15 (and its validation log): arXiv 1512.07715 is Cheon and Poghosyan, *Physica A* 469 (2017) 353-362, adding metaasabiya R, not Turchin's source. Confirmed here (s4).
- 08 s3: two formalisms exist (ODE system plus lattice simulation, ch. 4, NetLogo replica on CoMSES). Agrees with s2-s3. 08's lattice mechanisms (frontier regions gain asabiya, internal conflict lowers it far from the frontier, war capacity spread thin, collapse below a threshold, a higher-asabiya group re-founds) match the five CoMSES points in s3. 08 "Unconfirmed" says the lattice update rules were not read; this file likewise did not obtain them.
- 08 s3 on Turchin, Currie, Turner and Gavrilets 2013 (PNAS 110(41):16384-16389, doi 10.1073/pnas.1308825110, 1500 BCE-1500 CE, about 65% of variance in where large polities arose): agrees with s6 (R2 0.65).
- 08 s3 and 05 s18 ("Turchin's predictive claims are self-reported"): agree with s2 and s7, where no independent test of the ODE was found. 08 "Limits: asabiya is one scalar, not observed directly" agrees with the no-measured-S finding in s7.
- 08 s7 (Seshat moralizing-gods retraction as a coding warning): consistent with the pointer in s7.
- 07 s13a (Lanchester/Osipov): consistent with the Lanchester-Osipov attack form in Turchin and Gavrilets 2009 (s5). 07 states the equations; this file only names the form.
- 05 s18 and 08 s6 cite Turchin 2008 *Nature* 454:34-35 and 2010 *Nature* 463:608; this file does not touch them, so there is no overlap to conflict.
- 09 (Unconfirmed list: Hobbs/Turchin-style cliodynamics not searched): no claim to conflict.

### Contradictions and tensions
1. **Meaning of A.** 18 s15: A is territory "(not population)". This file s2: A is population, area or GDP per Cheon and Poghosyan p. 2. 08 s3 says "polity area". Verdict: **unresolved** for the book; compatible if Turchin's A is territory and C&P generalise it. Not checked against the book (paywalled; search budget exhausted).
2. **Gloss of h.** 18 s15: "spatial scale of power projection". This file: growth limit set by the natural resource of the land (C&P). Verdict: **unresolved** (already flagged in s2 and Unconfirmed). If A is territory, 18's reading is the more natural one; if A is population, C&P's. The two choices of A and h are tied together.
3. **Gloss of a.** 18 s15: "geopolitical pressure from the hinterland, not a death rate". This file: a constant sink that sets a threshold for A's growth (C&P). The readings are compatible in effect (a constant loss term) but differ in interpretation. Verdict: **unresolved**.
4. **2013 PNAS as test of asabiya.** 08 s3 calls it "the later, larger agent-based test" of the frontier mechanism and the "real agent-based test of the frontier/warfare mechanism" (Missing important work). This file s1/s6: the Methods contain no asabiya; it is a cultural-multilevel-selection plus military-technology model, and its fit is carried by steppe-seeded MilTech. Verdict: **this file is right on the Methods content as read from the paper in the draft session**, but the PNAS body could not be re-read in validation (only the abstract). 08 is defensible as "frontier/warfare" (steppe frontier is in the model) and wrong as "test of the asabiya ODE". Treat as a wording correction to 08 and 18, not a factual dispute.
5. **Turchin-Gavrilets 2009 in the asabiya context.** 18 s15: "Turchin and Gavrilets co-authored later work (2009 ...; 2010)", marked ✓ "standard account". This file s5: asabiya appears 0 times in the 2009 paper (PDF read). Verdict: **this file is right**; 18's sentence is true as co-authorship but misleading as support for asabiya.
6. **Lattice: frontier size and asabiya.** 08 s3 and the CoMSES page: larger frontier means higher asabiya. The ODE: S grows only when A < 2b. Already noted in s3 as a tension; no other file resolves it. Verdict: **unresolved** (the border-length-per-area reconciliation is this file's own reading).
7. **Glaeser 2005.** 18 s14 places it among scapegoating models; this file says it does not belong in the asabiya cluster. No conflict: both agree it is a hatred supply-and-demand model with no asabiya. Bibliographic details agree (QJE 120(1), 45-86).
8. **Possible name collision, 28 (Unconfirmed): "Turchin 2003".** In 28 this most likely refers to Turchin's ecology book *Complex Population Dynamics* (Princeton, 2003), a different book from *Historical Dynamics* (2003). Not a contradiction with this file; do not merge the two citations. Verdict: unresolved which 28 means, since 28 gives no title.
9. **Numerical and dating details** (7,941 points, 20 realisations, 12 parameters, 42%): no other file repeats them, so nothing to cross-check; they remain on the drafter's reading alone (see Unconfirmed).
