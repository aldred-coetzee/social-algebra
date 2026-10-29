# Prior work 57: does the second-order-belief channel causally drive behaviour (guilt aversion versus promise-keeping)?

Direction: D171

Date: 2026-10-29. Kind: cross-check. Question (research-map D171): does the second-order-belief channel, in which i feels guilt in proportion to how far i's action falls short of what i believes j expects, causally drive behaviour, or is the observed belief-behaviour correlation a false-consensus artefact or a separate promise-keeping preference? Files checked: 21 (Battigalli-Dufwenberg guilt entry and the Charness-Dufwenberg / Ellingsen lines) and 41 (guilt as a self-conscious drive).

**Method and honesty note.** Read in full at source this session, tagged [read]: Vanberg 2008 (Econometrica, publisher PDF via Heidelberg); Charness & Dufwenberg 2006 (JSTOR scan of the Econometrica article); Ellingsen, Johannesson, Tjøtta & Torsvik, *Testing guilt aversion*, as the **December 2007 Bergen working paper** (WP 14/07), not the published 2010 version; Reuben, Sapienza & Zingales 2009 (Economics Letters, publisher PDF); Ederer & Stremitzer 2017 (Cowles DP 1931R, October 2017 revision, not the journal PDF); Di Bartolomeo, Dufwenberg, Papa & Passarelli 2019 (GEB, author-hosted PDF). Tagged [abstract] where only the abstract or a search/fetch summary was available: Khalmetski 2016, Khalmetski-Ockenfels-Werner 2015, Bellemare-Sebald-Suetens 2018 and 2019, Ismayilov-Potters, Di Bartolomeo-Dufwenberg-Papa 2023. Tagged [standard] where not opened: Dufwenberg-Kirchsteiger 2004, Cox-Friedman-Gjerstad 2007, Camerer 2003, Battigalli-Dufwenberg 2007 (file 21 already holds a primary-text read of the last). All DOIs below were checked against Crossref this session. The PDF text of Ederer-Stremitzer lost its Greek letters in extraction; the utility function below was reconstructed from the surviving structure and is flagged where so.

---

## Summary

1. **File 21's wording needs sharpening on one point, and the contest is wider than it says.** File 21 lists the Ellingsen et al. null result as "contested". It is more than contested: it is the only one of the direct tests that was designed to remove false consensus, it found zero (Pearson r between -0.075 and +0.085 across three experiments, N = 455 subjects), and the later causal studies split by design. The honest verdict is below.
2. **Verdict.** The second-order-belief channel is a **real but conditional, heterogeneous and modest-sized** causal driver, not a general law. Evidence for causation exists only where beliefs were shifted by the experimenter (Reuben et al. 2009, Ederer & Stremitzer 2017, Khalmetski 2016, Khalmetski-Ockenfels-Werner 2015). Where beliefs were merely elicited and correlated (Charness & Dufwenberg 2006) the correlation is explained equally well by false consensus, as Vanberg and Ellingsen et al. argue and as Charness & Dufwenberg themselves concede. Where beliefs were disclosed (Ellingsen et al.) the effect vanished. Effects sizes, when found, are small: Ederer & Stremitzer's reliable-versus-unreliable device moved mean contribution by $5.76 versus $5.28 [read].
3. **The condition matters more than the sign.** Ederer & Stremitzer find the effect **only when a promise exists** (belief shifts without a promise did not move behaviour even though second-order beliefs moved significantly) and write the utility with a promise gate. That single feature reconciles most of the apparent contradictions: Ellingsen et al. and Vanberg's switch condition have no promissory link from the dictator to the recipient, so the channel is switched off there. For the algebra, guilt is a **gated operator**, not a free-standing one.
4. **Promise-keeping per se (Vanberg) is not settled either.** Vanberg's own promise-versus-others'-promise contrast (73 % versus 54 % roll rate; p = 0.03) is replicated in Di Bartolomeo et al. 2019 only in one of two cells (high switching probability, 58 % versus 28 %; not at low switching probability, 51 % versus 47 %). A 2023 follow-up by a subset of the same authors in a different game reportedly gets the opposite pattern (supports the expectations account, not commitment) [abstract]. No study has cleanly measured both effects' magnitudes.
5. **For the algebra:** carry guilt as `Guilt(i->j) = theta_i * max(0, E_i[E_j[m_j]] - m_j(a_i))^k` multiplied by a **claim gate** (promise or equivalent entitlement), with `theta_i` drawn from a distribution that has roughly half its mass at zero, and add a separate, belief-independent **obligation** term. Do not assume the first-order link from beliefs to action holds outside a claim relation.

---

## 1. The claim under test

**The theory.** Guilt aversion: a player feels guilt in proportion to how much he believes he lets another down relative to what that other expects. Because the other's expectation is a belief, utility depends on a **second-order belief** (i's belief about j's belief about i's action or j's payoff). First formal general statement: Battigalli & Dufwenberg 2007, "Guilt in Games", AER P&P 97(2), 170-176, doi:10.1257/aer.97.2.170 (Crossref-confirmed; model section read in file 21).

**The testable prediction (Charness & Dufwenberg 2006, p. 1583) [read].** In their hidden-action trust game, with `tau_B` the mean of B's belief about A's belief that B will Roll:

- If B chooses Don't Roll, A gets 0. B believes A expects `tau_B * [(5/6)*12 + (1/6)*0] = 10 * tau_B`. The shortfall is `10 * tau_B`, and B's guilt is `gamma_B * 10 * tau_B` with `gamma_B > 0` the sensitivity.
- B rolls iff `14 - gamma_B * 10 * tau_B < 10`. "The higher `tau_B` is the greater the likelihood that B will choose Roll." The paper assumes guilt sensitivity differs among B's and is independent of `tau_B`.

This independence assumption is exactly what the false-consensus rival violates: a B who is himself trustworthy believes others expect trustworthiness.

## 2. Direct evidence, in order of causal strength

### 2.1 Correlational tests: Charness & Dufwenberg 2006

Charness & Dufwenberg, "Promises and Partnership", *Econometrica* 74(6), 1579-1601, 2006, doi:10.1111/j.1468-0262.2006.00719.x (Crossref-confirmed). [read, JSTOR scan]

- **Design.** Five treatments, 15 sessions, UCSB, 24-36 participants per session. Hidden-action trust game F1: A chooses In or Out (outside option (5,5), or (7,7) in two treatments); B then chooses Roll (die; success with p = 5/6 gives A 12 and B 10) or Don't Roll (A 0, B 14). Beliefs elicited **after** choices: A guesses the proportion of B's who Roll; B guesses "the average guess made by A's who chose In"; $5 if within five percentage points. B messages free-form; one treatment lets A message B.
- **Communication.** (5,5), B messages: 28/42 (67 %) Roll versus 20/45 (44 %) without; In 74 % versus 56 %; (In, Roll) 50 % versus 20 % (Z = 2.94). (7,7): Roll 49 % versus 25 %. A messages did nothing (Roll 39 % versus 44 %).
- **Belief-behaviour (Table II).** B's average guess of A's guess, Roll versus Don't Roll: 54.2 vs 39.6 (no messages, (5,5)); 73.2 vs 45.1 (B messages, (5,5)); 69.6 vs 50.0 (A messages); 69.4 vs 41.7 ((7,7) no messages); 66.9 vs 36.9 ((7,7) B messages). Z between 1.99 and 3.52, all significant, one-tailed. "The support for guilt aversion is considerable in all of our treatments."
- **Promises (Table III, Table IV).** Pooled: Roll 79 % (38/48) after a promise, 33 % (14/43) without. Promises raise beliefs only modestly (A guesses 64.4 vs 50.5, p < 0.05 pooled; B guesses 63.1 vs 54.7); "the effects are modest".
- **Self-acknowledged limit.** Beliefs are elicited ex post and are average guesses over all A's, not about the paired A. They do not claim causation; the paper says the test uses within-person structure and "does not presume that players coordinate on some equilibrium".
- **Standing.** Correlational. Upgrades file 21's "finding … from memory" to [read].

### 2.2 The false-consensus challenge: Vanberg 2008

Vanberg, "Why Do People Keep Their Promises? An Experimental Test of Two Explanations", *Econometrica* 76(6), 1467-1480, 2008, doi:10.3982/ECTA7673 (Crossref-confirmed). [read]

- **Design.** Random-dictator mini game: Don't Roll gives dictator 14 and recipient 0; Roll gives dictator 10 and recipient 12 w.p. 5/6, 0 w.p. 1/6 (Charness-Dufwenberg's trustee choice). Pairs chat, then roles are drawn, then **half of recipients are re-matched** to a new dictator. Dictators know whether the switch happened and can read the new partner's chat; recipients do not know, so recipients' first-order and dictators' second-order beliefs depend on promises received, not on whether the switch occurred. 192 subjects, 6 sessions, 8 rounds each; 384 decisions per cell; tests on session averages (Wilcoxon). Second-order beliefs elicited on a 5-point scale (0, 1/4, 1/2, 3/4, 1) with a quadratic scoring rule, after the decision.
- **Results.** Table I: second-order belief 0.76 (no switch) versus 0.71 (switch), Z = 1.48, p = 0.14 (not different); **Roll 69 % versus 54 %**, Z = 2.20, p = 0.03. Table III: dictator who promised and was not switched: 227/309 = 73 %; promised and switched, partner holding another's promise: 129/238 = 54 %; the second-order beliefs of the latter rise significantly with the partner holding a promise (p = 0.03) while Roll does not move (p = 0.60). Appendix B logit: promise × switched negative and significant; **coefficient on second-order belief positive and significant in every specification (RILOG4 printed as "352" with the decimal point lost in extraction, presumably 0.352)**, which Vanberg attributes either to guilt or to false consensus.
- **Claim.** "The results demonstrate that the effects of promises cannot be accounted for by changes in payoff expectations. This suggests that people have a preference for promise keeping per se." He notes the commitment account "is entirely compatible with" a guilt motive; the dispute is over **what triggers guilt** (an expectation versus an obligation).
- **Standing, blunt.** A clean design for separating promise from belief for the *switched* dictator. It does not exogenously vary beliefs for the non-switched promisor, so it cannot test whether the expectation channel matters for one's own promise (Di Bartolomeo et al. 2019, fn. 4). The ES critique (2.5) says the result does not require a separate commitment preference at all.

### 2.3 The disclosure test: Ellingsen, Johannesson, Tjøtta & Torsvik

Ellingsen, Johannesson, Tjøtta & Torsvik, "Testing guilt aversion", *Games and Economic Behavior* 68(1), 95-107, 2010, doi:10.1016/j.geb.2009.04.021 (Crossref-confirmed). [read as the Dec 2007 working paper only; the published version may differ in details]

- **Design.** Three experiments, 455 subjects total (Stockholm and Bergen): (1) double-blind dictator game, 168 subjects, 84 pairs; (2) complete-information trust game, 196 subjects, 98 pairs; (3) hidden-action trust game (Charness-Dufwenberg's F1), 88 subjects. Donors (dictators / trustees) are **told the recipient's actual elicited belief**, which is elicited with incentives to be honest. If guilt aversion held, donations should rise with the disclosed belief.
- **Results [read].** Dictator game: Pearson -0.075 (p = 0.497), Spearman -0.044 (p = 0.689); dropping six observations with beliefs above 50 %: -0.008; dropping those who gave everything and those who gave nothing, correlations stay near zero or slightly positive and non-significant (0.099 / 0.051 when both extremes are dropped). Trust game back-transfers: Pearson 0.085 (p = 0.434); with a sensitivity exclusion Pearson 0.044 (p = 0.683) and Spearman 0.096 (p = 0.378); dropping the two subjects with 100 % back-transfer beliefs gives Pearson 0.122 (p = 0.264). Hidden-action game: Pearson -0.071 (p = 0.646), Spearman -0.066 (p = 0.669); mean belief among Rollers **41.6 %** versus **45.7 %** among Don't-Rollers (p = 0.657), against Charness & Dufwenberg's 54.2 % versus 39.6 % in the closest treatment. Their conclusion: "If Scandinavian students are guilt averse, the effect is small."
- **Reading, blunt.** A strong null on the *disclosed-belief* causal test. Three caveats the field raises and that I confirmed: (a) the beliefs shown are elicited, so a donor may doubt they are sincere (Reuben et al. fn. 4-6 make this point and pay senders for accuracy to reduce it); (b) the hold-out is population specific (Scandinavian students); (c) subsequent work (Khalmetski-Ockenfels-Werner) finds the correlation can be positive or negative and wash out in aggregate [abstract].

### 2.4 The mirror test: Reuben, Sapienza & Zingales

Reuben, Sapienza & Zingales, "Is mistrust self-fulfilling?", *Economics Letters* 104(2), 89-91, 2009, doi:10.1016/j.econlet.2009.04.007 (Crossref-confirmed). [read]

- **Design.** Lost-wallet game (sender has $50; if sent, receiver gets $150 and returns any amount). 52 MBA students as receivers, twice: first without knowing the sender's expectation, then after being told it (24 told a **low** expectation, under $10; 28 told a **high** expectation, over $70). Within-subject. Senders were paid for expectation accuracy (up to $75 minus absolute error) to discourage strategic reporting.
- **Results [read].** Low expectation: return fell from **$53.75 to $40.63** (Wilcoxon signed rank p = 0.030; 54 % reduced, 33 % unchanged, 13 % increased). High expectation: return rose from $52.14 to $58.29, **not significant** (p = 0.125; 61 % unchanged). Tobit: facing a low-expectation sender, return $31.77 lower than facing a high-expectation one (a 43 % difference).
- **Reading.** Causal evidence for the channel, but **asymmetric**: low expectations lower giving, high expectations barely raise it. That matches a hinge `max(0, E - actual)`: raising the benchmark above the baseline return only adds guilt for those who were already under it. It is also compatible with a social-norm or "legitimate expectation" reading.

### 2.5 The exogenous belief shock under a promise: Ederer & Stremitzer

Ederer & Stremitzer, "Promises and expectations", *Games and Economic Behavior* 106, 161-178, 2017, doi:10.1016/j.geb.2017.09.012 (Crossref-confirmed). [read as Cowles DP 1931R]

- **Design.** Dictator sends a free-form message; recipient opts in or out; then Nature selects a **reliable (rho = 5/6)** or **unreliable (rho = 1/6)** random device that determines whether the dictator can choose a positive level of performance (Perform, 3/4, 1/2, 1/4, Don't Perform). If performance is impossible or Don't Perform, payoffs are (dictator 14, recipient 0); full Perform gives (10, 12). Strategy method, within-subject: dictators choose for both device states, which exogenously shifts second-order expectations without changing the dictator's incentives. 1,120 decisions.
- **Results [read].** Mean contribution $5.76 (reliable) versus $5.28 (unreliable), conditional on performance being feasible; Wilcoxon signed rank p < 0.01; "small in magnitude". The difference is driven by dictators who made a promise. Among promisors, 40 % chose Don't Perform under the unreliable device versus under 5 % under the reliable one. Recipients' conditional first-order beliefs: 0.28 versus 0.24 (p = 0.15, not significant), with the promise-conditional difference 0.052 in a fixed-effects regression (10 % level). **Dictators' second-order beliefs: 0.64 versus 0.53** (p < 0.01); by message: no message 0.59 / 0.48, empty talk 0.59 / 0.43, promise 0.72 / 0.64, all significant. So beliefs moved in all three message conditions, **but behaviour moved only under a promise**. Opt-out after a promise 7.3 % versus 21.6 % after no message.
- **Model [read, with symbol loss; reconstructed].** The paper says its model uses Battigalli-Dufwenberg's *simple guilt*, with guilt switched on by a promise. Recoverable form, with `pi_D(a) = 14 - 4a`, recipient payoff `pi_R(a) = 12a`, `mu_D(rho)` the dictator's belief about the recipient's expected action given device reliability `rho`, `theta_D >= 0` the sensitivity, `sigma in {0,1}` the promise indicator, `k >= 1` the convexity (extraction dropped the Greek, so the exact placement of the promise indicator in eq. (1) is inferred from the text, which states "this term only plays a role if the dictator sent a promise"):

      U_D(a) = pi_D(a) - sigma * (theta_D / k) * ( max{ E[pi_R | mu_D(rho)] - pi_R(a), 0 } )^k
             = 14 - 4a - sigma * (theta_D / k) * 12^k * ( max{ mu_D(rho) - a, 0 } )^k

  For `k = 1` it nests Charness-Dufwenberg as a special case with corner solutions; `k > 1` allows interior solutions. An altruism term `(delta_D / r) * (12 - pi_R(a))^r` is added when estimating, and `theta_D`, `delta_D` are identified per subject from first-order conditions at sigma = 0 and sigma = 1.
- **Estimated guilt sensitivity (r = k = 2) [read].** Just under 50 % of dictators have `theta_D = 0`; about 25 % sit at a corner mass `theta_D >= 20` (guilt so large they fully eliminate the shortfall); about 25 % lie between. A bimodal, zero-inflated distribution, not a single `theta`.
- **What it does to Vanberg.** Their discussion argues that if guilt is switched on only by a promise, a promisor will outperform a non-promisor "without any independent preference for promise-keeping" and that to show a separate commitment preference "we would have to design an experiment that varies the dictator's promissory commitment while keeping the recipient's expectations at zero." They also state their design "was not suited to directly test our theory of conditional guilt aversion" and that no-promise null results could reflect self-selection into promising.
- **Standing.** Best single piece of evidence for a causal belief channel; effect small; the gate is estimated, not independently tested.

### 2.6 Both exogenous at once: Di Bartolomeo, Dufwenberg, Papa & Passarelli

Di Bartolomeo, Dufwenberg, Papa & Passarelli, "Promises, expectations & causation", *Games and Economic Behavior* 113, 137-146, 2019, doi:10.1016/j.geb.2018.07.009 (Crossref-confirmed). [read, author PDF]

- **Design.** Vanberg's partner-switch random-dictator game with the **switching probability set at 25 % or 75% by treatment**, which shifts recipients' first-order and dictators' second-order beliefs exogenously for non-switched promisors. 192 subjects, 6 sessions (Rome, December 2015), 8 rounds, 768 dictator decisions, 575 coded as promises. Beliefs elicited before the dictator knows about the switch.
- **Manipulation check [read].** Promisors' second-order beliefs 0.80 (switch prob. 25 %) versus 0.66 (75 %), Z = 2.20, p = 0.027 (1st-order 0.74 vs 0.55). Without a promise the switching probability does nothing (0.38 vs 0.40). So the shifter works only under a promise.
- **EBE test (H1: non-switched promisors, high versus low belief).** Roll **51 % (high beliefs) versus 58 % (low beliefs)**, Z = 0.93, p = 0.345. **No support** for the expectations account in the promisor's own-promise cell.
- **CBE test (H2: non-switched versus switched, both holding a promise).** At 75 % switching: 58 % versus 28 %, Z = 2.20, p = 0.027, **supports** Vanberg. At 25 % switching: 51 % versus 47 %, Z = 0.52, p = 0.600, **no support**.
- **Guilt-aversion tests among switched dictators (H3).** (a) Switched promisors facing a recipient who holds a promise: 47 % (high beliefs) versus 28 % (low), Z = 1.99, p = 0.046, **supports** guilt aversion; switched non-promisors: 29 % versus 27 %, no effect. (b) At 25 % switching, a promise-holding recipient 47 % versus 24 % without, p = 0.046, supports; at 75 %, 28 % versus 27 %, no.
- **Their summary (Table 5):** EBE no; CBE yes in one cell of two; GA yes in two cells of four. Overall roll rates are low: "the cell with the most frequent promise-keeping gets 58 %, so 42 % reneged."
- **Notable.** The authors' own conclusion notes the two explanations "are not mutually exclusive".
- **Follow-up [abstract / summary only].** Di Bartolomeo, Dufwenberg & Papa, "Promises and partner-switch", *Journal of the Economic Science Association* 9(1), 77-89, 2023, doi:10.1007/s40881-023-00128-4 (Crossref-confirmed). A fetch summary of the article page reports the same partner-switch idea in Charness-Dufwenberg's asymmetric trust game with a single unilateral message (226 students, 1,130 pairs; In rate 76 % after a promise versus 49 % without), and reports results "opposite to Vanberg": support for the expectations account, none for commitment. I have not read the text; treat as [abstract].

### 2.7 Other direct tests (abstract level)

- **Khalmetski 2016,** "Testing guilt aversion with an exogenous shift in beliefs", GEB 97, 110-119, doi:10.1016/j.geb.2016.04.003 (Crossref-confirmed). [abstract] A sender-receiver communication game where the receiver knows only the *distribution* of the sender's lying incentive; changing that distribution shifts receiver payoff expectations while the sender's incentive is fixed. Lying is significantly less frequent when receivers are expected to have higher payoff expectations, **but only when the lying incentive is at a moderate level.**
- **Khalmetski, Ockenfels & Werner 2015,** "Surprising gifts: Theory and laboratory evidence", *Journal of Economic Theory* 159, 163-208, doi:10.1016/j.jet.2015.05.008 (Crossref-confirmed). [abstract] Extends guilt aversion to positive surprise ("may also like to exceed" expectations). Dictator-game experiments find "a strong causal effect of recipients' expectations on dictators' transfers", and the correlation between transfers and expectations "can be both positive and negative, obscuring the effect in the aggregate." Di Bartolomeo et al. (fn. 1) read this as a possible reconciliation with Ellingsen et al.
- **Bellemare, Sebald & Suetens 2018,** "Heterogeneous guilt sensitivities and incentive effects", *Experimental Economics* 21(2), 316-336, doi:10.1007/s10683-017-9543-2 (Crossref-confirmed). [abstract] Measures guilt sensitivity per individual at several stakes in a dictator game and fits a structural model: roughly **60 % of decision makers have stake-dependent guilt sensitivity**; sensitivities are reliably above zero at all stakes but **decrease as stakes rise**.
- **Bellemare, Sebald & Suetens 2019,** "Guilt aversion in economics and psychology", *Journal of Economic Psychology* 73, 52-59 [abstract; DOI not independently checked]. The economic guilt-sensitivity estimate correlates well and significantly with the psychology questionnaire TOSCA-3 in trust and dictator games. This is the only bridge I found between the guilt of file 41's psychological literature and the guilt of the economic models.
- **Ismayilov & Potters** (*Experimental Economics* 2016 per their citations; Cambridge page shows a 2025 online date; year not confirmed) [abstract]: promises appeared to raise trustworthiness through an internal consistency mechanism, but a control treatment banning promises showed no drop in cooperation; they conclude **self-selection**: cooperative trustees are the ones who promise.

## 3. How the pieces fit (my reading)

| Source | Beliefs exogenous? | Promise in play? | Effect of higher second-order belief on giving |
|---|---|---|---|
| Charness & Dufwenberg 2006 | No (elicited) | Yes (endogenous) | Positive correlation |
| Vanberg 2008 | Partly (switched cells only) | Yes | Beliefs moved; behaviour did not (switched) |
| Ellingsen et al. 2010 (WP) | Disclosed | No | None (r near 0) |
| Reuben et al. 2009 | Disclosed | No | Low expectation lowers giving ($53.75 to $40.63); high does not raise (n.s.) |
| Khalmetski-Ockenfels-Werner 2015 | Yes [abstract] | No | Strong, sign-varying |
| Khalmetski 2016 | Yes [abstract] | No | Present only at moderate incentives |
| Ederer & Stremitzer 2017 | Yes | Yes | Small positive; only under a promise |
| Di Bartolomeo et al. 2019 | Yes | Yes | None for own-promise cell (51 vs 58 %); positive in two switched cells |

Three patterns: (1) **the correlation is not good evidence** in either direction; (2) **where beliefs are shifted from outside the dictator's head, the sign is usually positive, but the size is small and cell-specific**; (3) **who the expectation belongs to and why it exists seems to matter** (promise, legitimacy) more than its magnitude. The Khalmetski summary that people may not want to live up to any expectations "but only to those that appear to be legitimate" is a secondary-source paraphrase [search summary, not the paper].

## 4. Operand/operator translation for the algebra

**Their vocabulary.** Guilt aversion; second-order belief; simple guilt versus guilt from blame; expectations-based explanation (EBE); commitment-based explanation (CBE); false consensus; conditional guilt aversion; guilt sensitivity `theta`.

**Drives/operands.** Guilt (as a drive with an object, the person who might be let down); belief states at orders 1 and 2; a claim relation (promise, entitlement).

**Operators.**
- `Let-down(i -> j) = max(0, E_i[E_j[m_j]] - m_j(a_i))^k` [read in ES; the base form read in Battigalli-Dufwenberg via file 21].
- `Guilt(i -> j) = theta_i * g(claim_ij) * Let-down(i -> j) / k`, where `g(claim)` is 1 under a promise and a small or zero value otherwise [conditional structure estimated in ES; gate shape not tested].
- `Obligation(i -> j)`: a belief-independent term attached to a made promise (CBE), additive with Guilt. Nobody has estimated its size separately from Guilt; the single clean test (Vanberg) is cell-dependent in the one replication.
- Belief propagation (how a promise moves `E_j[m_j]` and so `E_i E_j[m_j]`): observed to be modest (Charness-Dufwenberg: A guesses 27.5 % higher after a promise; ES: second-order 0.72 vs 0.59 under reliable device).

**Parameters worth putting in as editable settings (not hardcoded).**
- `theta_i` distribution: a zero-inflated mixture, **about half at 0, about a quarter at a corner, about a quarter in between** (ES, r = k = 2, student sample); stake dependence with `theta` falling as stakes rise (Bellemare et al. [abstract]).
- Convexity `k`: ES allow k > 1; the data fit used r = k = 2; no independent test of k.
- Gate `g`: ES estimate effectively `g(no promise) = 0`; Ellingsen et al. support a near-zero value outside promises; Khalmetski-Ockenfels-Werner and Reuben et al. suggest non-zero effects without promises. Keep `g` free.
- Asymmetry: Reuben et al. imply the hinge matters in practice (decrease under low expectation, almost nothing under high).

**Theorems or derived predictions.** The only formal results are in Battigalli-Dufwenberg (existence of sequential equilibrium; file 21). The empirical regularities above are not theorems. One consequence of the hinge that follows from the definitions: for a guilt-averse player, giving is non-decreasing in `E_i[E_j[m_j]]` and **flat above** the level at which the shortfall is zero, so correlation tests that pool across the whole range dilute the effect (consistent with the sign-varying result of Khalmetski-Ockenfels-Werner [abstract]).

## 5. What exists versus what does not

**Exists.**
- A theory with a stated utility and an existence theorem (Battigalli-Dufwenberg 2007, 2009; file 21).
- Several designs that shift beliefs from outside the player (Reuben 2009; Khalmetski 2016; KOW 2015; Ederer-Stremitzer 2017; Di Bartolomeo et al. 2019) and one null built on disclosure (Ellingsen et al.).
- A specified conditional-guilt model with per-subject estimated parameters and a zero-inflated distribution (Ederer-Stremitzer).
- A separate commitment account with its own design (Vanberg 2008).
- A questionnaire-to-parameter bridge (Bellemare et al. 2019 [abstract]).

**Does not exist.**
- **A replication that holds the game fixed and reproduces any single belief-shift result in a different lab.** Every causal study uses a different game and population.
- **A clean separate magnitude for EBE and CBE.** Two pure-ish tests reached opposite conclusions in the same design family (Vanberg versus Di Bartolomeo et al. 2019 and 2023).
- **Dynamics.** Every study is one-shot or perfect-stranger; no decay, no accumulation, no learning of other people's beliefs. Charness & Dufwenberg's own text flags that "in psychological games, finding a best response may in addition require players to learn about the beliefs about beliefs of others" (p. 1592) and defers it.
- **A group-level or n > 2 test.** All designs are dyadic; the sum over j != i in Battigalli-Dufwenberg is unused empirically.
- **Non-student, non-WEIRD samples.** All samples are university students (Jena, Santa Barbara, Stockholm/Bergen, Northwestern MBAs, Rome, UCLA).
- **A meta-analysis.** I found none for guilt-aversion belief effects; verdicts here are by hand from the cell-level results above.

## 6. Cross-check of files 21 and 41

- **File 21, line 81** says the Charness-Dufwenberg finding is "from memory". Now [read]: Roll 67 % versus 44 %, In 74 % versus 56 %, belief gap significant in all five treatments. Update to [read].
- **File 21, summary table** says Ellingsen et al.'s null is "contested". Accurate but incomplete: add that the null is on **disclosed** beliefs, that the strongest later causal tests (Ederer-Stremitzer, Khalmetski) find small positive effects, and that the effect in Ederer-Stremitzer exists **only under a promise**, which Ellingsen et al.'s dictator and trust games lack. The two are not necessarily in conflict.
- **File 21, line 207** ("Two drives with a belief-based mechanism and theorems: guilt and anger") overstates what is proved. The theorems (existence) are about equilibria of the formal game; none shows that human guilt follows that functional form. The empirical support is the table in section 3.
- **File 41, row "Guilt"** cites "Guilt-prosociality r = .13, k = 63" for dispositional guilt, and "static: guilt aversion in utility". The bridge exists in the opposite direction from what 41 implies: the economic guilt sensitivity correlates with the TOSCA-3 questionnaire (Bellemare et al. 2019 [abstract]), so the r = .13 prosociality figure and the economic parameter may be measuring related traits, but I could not check the size of that correlation.
- **Neither file mentions Vanberg 2008.** File 21 should carry it, because it is the main alternative explanation to the guilt channel for the promise result.

## Unconfirmed

- Whether the published version of Ellingsen et al. (GEB 2010) has the same correlations as the 2007 working paper; I read the latter only. The abstract (via search) repeats "close to zero in all three experiments".
- The exact symbols in Ederer-Stremitzer's equation (1); recovered by reading the structure of the garbled text. Check against the journal PDF before using `theta` and `k` placements in any equation of the algebra.
- Di Bartolomeo, Dufwenberg & Papa 2023: results taken from a summarised fetch of the article page; confirm numbers and the "opposite to Vanberg" claim from the text.
- Bellemare-Sebald-Suetens 2019: the DOI and the strength of the TOSCA-3 correlation were not checked.
- Khalmetski 2016 and Khalmetski-Ockenfels-Werner 2015: abstract-level only; the "legitimate expectations" gloss is a secondary-source phrase.
- Works cited by Ederer-Stremitzer and Di Bartolomeo et al. that I did not open: Mischkowski, Stone & Stremitzer (conditional guilt, cited as "2016"); Charness & Dufwenberg 2010 "bare promises" (small effects of pre-coded messages); Krupka et al. 2017 (norm-based promise-keeping); Bacharach, Guerra & Zizzo 2007; Bracht & Regner 2013; Chang et al. 2011; Regner & Harth 2014.
- Seeds from the map not read here: Charness & Dufwenberg 2011 "Participation" (AER 101(4), 1211-1237, doi:10.1257/aer.101.4.1211, Crossref-confirmed, not opened); Dufwenberg & Kirchsteiger 2004 (GEB 47, 268-298, doi:10.1016/j.geb.2003.06.003, confirmed, [standard] only); Cox, Friedman & Gjerstad 2007 (GEB 59, 17-45, doi:10.1016/j.geb.2006.05.001, confirmed, [standard] only); Camerer 2003 *Behavioral Game Theory* (book; not opened). These are reciprocity and status models, not tests of the second-order-belief channel.
