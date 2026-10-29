# Prior work 57: does the second-order-belief channel causally drive behaviour (guilt aversion versus promise-keeping)?

Direction: D171

Date: 2026-10-29. Kind: cross-check. Question (research-map D171): does the second-order-belief channel, in which i feels guilt in proportion to how far i's action falls short of what i believes j expects, causally drive behaviour, or is the observed belief-behaviour correlation a false-consensus artefact or a separate promise-keeping preference? Files checked: 21 (Battigalli-Dufwenberg guilt entry and the Charness-Dufwenberg / Ellingsen lines) and 41 (guilt as a self-conscious drive).

**Method and honesty note.** Read in full at source this session, tagged [read]: Vanberg 2008 (Econometrica, publisher PDF via Heidelberg); Charness & Dufwenberg 2006 (JSTOR scan of the Econometrica article); Ellingsen, Johannesson, Tjøtta & Torsvik, *Testing guilt aversion*, as the **December 2007 Bergen working paper** (WP 14/07), not the published 2010 version; Reuben, Sapienza & Zingales 2009 (Economics Letters, publisher PDF); Ederer & Stremitzer 2017 (Cowles DP 1931R, October 2017 revision, not the journal PDF); Di Bartolomeo, Dufwenberg, Papa & Passarelli 2019 (GEB, author-hosted PDF). Tagged [abstract] where only the abstract or a search/fetch summary was available: Khalmetski 2016, Khalmetski-Ockenfels-Werner 2015, Bellemare-Sebald-Suetens 2018 and 2019, Ismayilov-Potters, Di Bartolomeo-Dufwenberg-Papa 2023. Tagged [standard] where not opened: Dufwenberg-Kirchsteiger 2004, Cox-Friedman-Gjerstad 2007, Camerer 2003, Battigalli-Dufwenberg 2007 (file 21 already holds a primary-text read of the last). All DOIs below were checked against Crossref this session. The PDF text of Ederer-Stremitzer lost its Greek letters in extraction; the utility function below was reconstructed from the surviving structure and is flagged where so. **Validation pass (2026-10-29):** every number in sections 2.1-2.6 was re-checked against the same source texts; Khalmetski 2016, Bellemare et al. 2019 and Di Bartolomeo-Dufwenberg-Papa 2023 were then read as author or working-paper versions, and the Bellemare 2019 and Ismayilov-Potters DOIs were resolved. See the log at the end.

---

## Summary

1. **File 21's wording needs sharpening on one point, and the contest is wider than it says.** File 21 lists the Ellingsen et al. null result as "contested". It is more than contested: it is the disclosure test built to remove false consensus (Vanberg 2008, Reuben et al. 2009, Khalmetski 2016 and Ederer-Stremitzer 2017 also address it, by other designs), it is the only one of them that found zero (Pearson r between -0.075 and +0.085 across three experiments, 455 participants including three monitors), and the later causal studies split by design. The honest verdict is below.
2. **Verdict.** The second-order-belief channel is a **real but conditional, heterogeneous and modest-sized** causal driver, not a general law. Evidence for causation exists only where beliefs were shifted by the experimenter (Reuben et al. 2009, Ederer & Stremitzer 2017, Khalmetski 2016, Khalmetski-Ockenfels-Werner 2015). Where beliefs were merely elicited and correlated (Charness & Dufwenberg 2006) the correlation is explained equally well by false consensus, as Vanberg and Ellingsen et al. argue and as Charness & Dufwenberg themselves concede. Where beliefs were disclosed, Ellingsen et al. found no effect and Reuben et al. found a one-sided one. Effect sizes, when found, are small: Ederer & Stremitzer's reliable-versus-unreliable device moved mean contribution by $5.76 versus $5.28 [read].
3. **The condition matters more than the sign.** Ederer & Stremitzer find the effect **only when a promise exists** (belief shifts without a promise did not move behaviour even though second-order beliefs moved significantly) and write the utility with a promise gate. That single feature reconciles most of the apparent contradictions: Ellingsen et al. and Vanberg's switch condition have no promissory link from the dictator to the recipient, so the channel is switched off there. (It does not reconcile everything: Di Bartolomeo et al. 2019 find no belief effect in the promisor's own-promise cell, and Reuben et al., Khalmetski and Khalmetski-Ockenfels-Werner find effects with no promise at all.) For the algebra, guilt is a **gated operator**, not a free-standing one.
4. **Promise-keeping per se (Vanberg) is not settled either.** Vanberg's own promise-versus-others'-promise contrast (73 % versus 54 % roll rate; p = 0.03) is replicated in Di Bartolomeo et al. 2019 only in one of two cells (high switching probability, 58 % versus 28 %; not at low switching probability, 51 % versus 47 %). A 2023 follow-up by a subset of the same authors in Charness-Dufwenberg's game with one-way promises gets the opposite pattern: "Our results are the opposite of Vanberg's, supporting EBE, and not supporting CBE" [read, December 2021 working-paper version]. No study has cleanly measured both effects' magnitudes.
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

- **Design.** Three experiments, 455 participants total (171 + 196 + 88, the first including three monitors; experiment 1 at the Stockholm School of Economics, 2 and 3 at Bergen): (1) double-blind dictator game, 168 subjects, 84 pairs; (2) complete-information trust game, 196 subjects, 98 pairs (88 trustee observations after ten pairs with no investment); (3) hidden-action trust game (Charness-Dufwenberg's F1), 88 subjects, 44 pairs. Donors (dictators / trustees) are **told the recipient's actual elicited belief**, which is elicited with incentives to be honest. If guilt aversion held, donations should rise with the disclosed belief.
- **Results [read].** Dictator game: Pearson -0.075 (p = 0.497), Spearman -0.044 (p = 0.689); dropping six observations with beliefs above 50 %: -0.008; dropping the four who gave everything: 0.012 / 0.012; dropping the 29 who gave nothing: Pearson -0.026 (p = 0.852), Spearman 0.091 (p = 0.509); dropping both the four all-givers and the six high-belief cases: 0.099 / 0.051 (p = 0.400 / 0.668). Trust game back-transfers: Pearson 0.085 (p = 0.434); dropping the one subject who transferred everything, Pearson 0.044 (p = 0.683) and Spearman 0.096 (p = 0.378); dropping the two subjects with 100 % back-transfer beliefs gives Pearson 0.122 (p = 0.264). Hidden-action game: Pearson -0.071 (p = 0.646), Spearman -0.066 (p = 0.669); mean belief among Rollers **41.6 %** versus **45.7 %** among Don't-Rollers (p = 0.657), against Charness & Dufwenberg's 54.2 % versus 39.6 % in the closest treatment. Their conclusion: "If Scandinavian students are guilt averse, the effect is small."
- **Reading, blunt.** A strong null on the *disclosed-belief* causal test. Three caveats the field raises and that I confirmed: (a) the beliefs shown are elicited, so a donor may doubt they are sincere (Reuben et al. fn. 4-6 make this point and pay senders for accuracy to reduce it); (b) the hold-out is population specific (Scandinavian students); (c) subsequent work (Khalmetski-Ockenfels-Werner) finds the correlation can be positive or negative and wash out in aggregate [abstract].

### 2.4 The mirror test: Reuben, Sapienza & Zingales

Reuben, Sapienza & Zingales, "Is mistrust self-fulfilling?", *Economics Letters* 104(2), 89-91, 2009, doi:10.1016/j.econlet.2009.04.007 (Crossref-confirmed). [read]

- **Design.** Lost-wallet game (sender has $50; if sent, receiver gets $150 and returns any amount). 52 MBA students as receivers, twice: first without knowing the sender's expectation, then after being told it (24 told a **low** expectation, under $10; 28 told a **high** expectation, over $70). Within-subject. Senders were paid for expectation accuracy (up to $75 minus absolute error) to discourage strategic reporting.
- **Results [read].** Low expectation: return fell from **$53.75 to $40.63** (Wilcoxon signed rank p = 0.030; 54 % reduced, 33 % unchanged, 13 % increased). High expectation: return rose from $52.14 to $58.29, **not significant** (p = 0.125; 61 % unchanged). Tobit: facing a low-expectation sender, return $31.77 lower than facing a high-expectation one (a 43 % difference).
- **Reading.** Causal evidence for the channel, but **asymmetric**: low expectations lower giving, high expectations barely raise it. That matches a hinge `max(0, E - actual)`: raising the benchmark above the baseline return only adds guilt for those who were already under it. It is also compatible with a social-norm or "legitimate expectation" reading.

### 2.5 The exogenous belief shock under a promise: Ederer & Stremitzer

Ederer & Stremitzer, "Promises and expectations", *Games and Economic Behavior* 106, 161-178, 2017, doi:10.1016/j.geb.2017.09.012 (Crossref-confirmed). [read as Cowles DP 1931R]

- **Design.** Dictator sends a free-form message; recipient opts in or out; then Nature selects a **reliable (rho = 5/6)** or **unreliable (rho = 1/6)** random device that determines whether the dictator can choose a positive level of performance (Perform, 3/4, 1/2, 1/4, Don't Perform). If performance is impossible or Don't Perform, payoffs are (dictator 14, recipient 0); full Perform gives (10, 12). Strategy method, within-subject: dictators choose for both device states, which exogenously shifts second-order expectations without changing the dictator's incentives. 1,120 decisions.
- **Results [read].** Mean contribution $5.76 (reliable) versus $5.28 (unreliable), conditional on performance being feasible; Wilcoxon signed rank p < 0.01; "small in magnitude". The difference is driven by dictators who made a promise. Among promisors whose choice differed between the two devices (Figure 2; not all promisors), 40 % chose Don't Perform under the unreliable device versus under 5 % under the reliable one. Recipients' conditional first-order beliefs: 0.28 versus 0.24 (p = 0.15, not significant), with the promise-conditional difference 0.052 in a fixed-effects regression (10 % level). **Dictators' second-order beliefs: 0.64 versus 0.53** (p < 0.01); by message: no message 0.59 / 0.48, empty talk 0.59 / 0.43, promise 0.72 / 0.64, all significant. So beliefs moved in all three message conditions, **but behaviour moved only under a promise**. Opt-out after a promise 7.3 % versus 21.6 % after no message.
- **Model [read, with symbol loss; reconstructed].** The paper says its model uses Battigalli-Dufwenberg's *simple guilt*, with guilt switched on by a promise. Recoverable form, with `pi_D(a) = 14 - 4a`, recipient payoff `pi_R(a) = 12a`, `mu_D(rho)` the dictator's belief about the recipient's expected action given device reliability `rho`, `theta_D >= 0` the sensitivity (the paper's symbol is gamma_D, which survives in the Figure 4b axis label; theta is this file's renaming), `sigma in {0,1}` the promise indicator, `k >= 1` the convexity (extraction dropped the Greek, so the exact placement of the promise indicator in eq. (1) is inferred from the text, which states "this term only plays a role if the dictator sent a promise"):

      U_D(a) = pi_D(a) - sigma * (theta_D / k) * ( max{ E[pi_R | mu_D(rho)] - pi_R(a), 0 } )^k
             = 14 - 4a - sigma * (theta_D / k) * 12^k * ( max{ mu_D(rho) - a, 0 } )^k

  For `k = 1` it nests Charness-Dufwenberg as a special case with corner solutions; `k > 1` allows interior solutions. An altruism term `(delta_D / r) * (12 - pi_R(a))^r` is added when estimating, and `theta_D`, `delta_D` are identified per subject from first-order conditions at sigma = 0 and sigma = 1.
- **Estimated guilt sensitivity (r = k = 2) [read].** Identified for the 104 dictators observed both with and without a promise. Just under 50 % of dictators have `theta_D = 0`; about 25 % sit at a corner mass `theta_D >= 20` (guilt so large they fully eliminate the shortfall); about 25 % lie between. A bimodal, zero-inflated distribution, not a single `theta`.
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
- **Follow-up [read, Sapienza working paper No. 215, December 2021; not the journal text].** Di Bartolomeo, Dufwenberg & Papa, "Promises and partner-switch", *Journal of the Economic Science Association* 9(1), 77-89, 2023, doi:10.1007/s40881-023-00128-4 (Crossref-confirmed). The same partner-switch idea in Charness-Dufwenberg's trust game with a single unilateral B-to-A message (Rome, May 2019; 226 undergraduates, 8 sessions; 1,130 pairs; 527 promises; In 76 % after a promise versus 49 % without, Z = 2.52, p = 0.012). "We do not find support for CBE"; "Our results are the opposite of Vanberg's, supporting EBE, and not supporting CBE." The abstract argues Vanberg's back-and-forth chat tested informal agreements rather than unilateral promises, which is their reconciliation.

### 2.7 Other direct tests (abstract level)

- **Khalmetski 2016,** "Testing guilt aversion with an exogenous shift in beliefs", GEB 97, 110-119, doi:10.1016/j.geb.2016.04.003 (Crossref-confirmed). [read: abstract and conclusion of the Bath accepted manuscript; Cologne lab] A sender-receiver communication game where the receiver knows only the *distribution* of the sender's lying incentive; changing that distribution shifts receiver payoff expectations while the sender's incentive is fixed. Lying is significantly less frequent when receivers are expected to have higher payoff expectations, **but only when the lying incentive is at a moderate level.**
- **Khalmetski, Ockenfels & Werner 2015,** "Surprising gifts: Theory and laboratory evidence", *Journal of Economic Theory* 159, 163-208, doi:10.1016/j.jet.2015.05.008 (Crossref-confirmed). [abstract, quotes checked against the Bath accepted manuscript] Extends guilt aversion to positive surprise ("may also like to exceed" expectations). Dictator-game experiments find "a strong causal effect of recipients' expectations on dictators' transfers", and the correlation between transfers and expectations "can be both positive and negative, obscuring the effect in the aggregate." Di Bartolomeo et al. (fn. 1) read this as a possible reconciliation with Ellingsen et al.
- **Bellemare, Sebald & Suetens 2018,** "Heterogeneous guilt sensitivities and incentive effects", *Experimental Economics* 21(2), 316-336, doi:10.1007/s10683-017-9543-2 (Crossref-confirmed). [abstract] Measures guilt sensitivity per individual at several stakes in a dictator game and fits a structural model: roughly **60 % of decision makers have stake-dependent guilt sensitivity**; for those 60 %, average sensitivities are significantly above zero at all stakes but **decrease as stakes rise**.
- **Bellemare, Sebald & Suetens 2019,** "Guilt aversion in economics and psychology", *Journal of Economic Psychology* 73, 52-59, doi:10.1016/j.joep.2019.05.002 (Crossref-confirmed) [read: abstract and introduction of the Copenhagen preprint]. The economic guilt-sensitivity estimate, identified while controlling for false consensus, correlates with the psychology questionnaire TOSCA-3 in binary trust and dictator games: "Spearman rank correlations are well above 0.2 in absolute value, and statistically significant in both"; it does not correlate with TOSCA-3's other dispositions (shame, externalization, detachment). It is not the only bridge: they build on Bracht & Regner 2013, who regressed trustee choices on second-order beliefs and on TOSCA-3 and GASP scores.
- **Ismayilov & Potters 2016,** "Why do promises affect trustworthiness, or do they?", *Experimental Economics* 19(2), 382-393, doi:10.1007/s10683-015-9444-1 (Crossref-confirmed) [abstract]: promises appeared to raise trustworthiness through an internal consistency mechanism, but a control treatment banning promises showed no drop in cooperation; they conclude **self-selection**: cooperative trustees are the ones who promise.

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

Three patterns: (1) **the correlation is not good evidence** in either direction; (2) **where beliefs are shifted from outside the dictator's head, the sign is usually positive, but the size is small and cell-specific**; (3) **who the expectation belongs to and why it exists seems to matter** (promise, legitimacy) more than its magnitude. An unnamed search summary (not the paper; its wording is quoted here only to reject it) attributed to Khalmetski the gloss that people live up only to expectations "that appear to be legitimate"; the word does not occur in the accepted manuscript, whose own phrasing is that the effect appears when "high expectations can be rationalized from the sender's informational perspective". Use that wording, not the gloss.

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
- A theory with a stated utility and an existence theorem (Battigalli-Dufwenberg 2007; and "Dynamic psychological games", *Journal of Economic Theory* 144(1), 1-35, 2009, doi:10.1016/j.jet.2008.01.004, Crossref-confirmed; file 21).
- Several designs that shift beliefs from outside the player (Reuben 2009; Khalmetski 2016; KOW 2015; Ederer-Stremitzer 2017; Di Bartolomeo et al. 2019) and one null built on disclosure (Ellingsen et al.).
- A specified conditional-guilt model with per-subject estimated parameters and a zero-inflated distribution (Ederer-Stremitzer).
- A separate commitment account with its own design (Vanberg 2008).
- A questionnaire-to-parameter bridge (Bellemare et al. 2019 [read, preprint]).

**Does not exist.**
- **A replication that holds the game fixed and reproduces any single belief-shift result in a different lab.** Near misses exist and do not reproduce cleanly: Di Bartolomeo et al. 2019 re-ran Vanberg's partner-switch design in Rome with the switching probability varied, and Schwartz, Spires & Young, "Why do people keep their promises? A further investigation", *Experimental Economics* 22, 530-551, 2019, doi:10.1007/s10683-018-9567-2 (Crossref-confirmed, [abstract]), manipulated promise delivery and found "no support for the internal consistency rationale; only delivered promises are relevant". Neither is a same-game replication of a belief-shift result.
- **A clean separate magnitude for EBE and CBE.** Two pure-ish tests reached opposite conclusions in the same design family (Vanberg versus Di Bartolomeo et al. 2019 and 2023).
- **Dynamics.** Every study is one-shot or perfect-stranger; no decay, no accumulation, no learning of other people's beliefs. Charness & Dufwenberg's own text flags that "in psychological games, finding a best response may in addition require players to learn about the beliefs about beliefs of others" (p. 1592) and defers it.
- **A group-level or n > 2 test.** All designs are dyadic; the sum over j != i in Battigalli-Dufwenberg is unused empirically.
- **Non-student, non-WEIRD samples, in the causal tests above.** Those are all university students (Jena, Santa Barbara, Stockholm/Bergen, Northwestern MBAs, Cologne, Rome, UCLA). Corrected 2026-10-29: the wider literature is not all students. Nihonsugi, Tanaka & Haruno, "Gender differences in guilt aversion in Korea and the United Kingdom", *Scientific Reports* 12, 2022, doi:10.1038/s41598-022-12163-y [abstract via OpenAlex], ran an online trust game on Korean (n = 294) and UK (n = 347) participants, following a Japanese study; whether their design shifts beliefs exogenously is not checked.
- **A meta-analysis.** I found none for guilt-aversion belief effects (re-checked by validation with OpenAlex keyword searches only; the web-search budget was exhausted, so this is a weak negative); verdicts here are by hand from the cell-level results above.

## 6. Cross-check of files 21 and 41

- **File 21, line 81** says the Charness-Dufwenberg finding is "from memory". Now [read]: Roll 67 % versus 44 %, In 74 % versus 56 %, belief gap significant in all five treatments. Update to [read].
- **File 21, summary table** says Ellingsen et al.'s null is "contested". Accurate but incomplete: add that the null is on **disclosed** beliefs, that the strongest later causal tests (Ederer-Stremitzer, Khalmetski) find small positive effects, and that the effect in Ederer-Stremitzer exists **only under a promise**, which Ellingsen et al.'s dictator and trust games lack. The two are not necessarily in conflict.
- **File 21, line 207** ("Two drives with a belief-based mechanism and theorems: guilt and anger") overstates what is proved. The theorems (existence) are about equilibria of the formal game; none shows that human guilt follows that functional form. The empirical support is the table in section 3.
- **File 41, row "Guilt"** cites "Guilt-prosociality r = .13, k = 63" for dispositional guilt, and "static: guilt aversion in utility". The bridge exists in the opposite direction from what 41 implies: the economic guilt sensitivity correlates with the TOSCA-3 questionnaire (Bellemare et al. 2019 [read, preprint]), so the r = .13 prosociality figure and the economic parameter may be measuring related traits; the economic-to-TOSCA correlation is Spearman above 0.2 in absolute value (Bellemare et al. 2019 preprint, read in validation).
- **Neither file mentions Vanberg 2008.** File 21 should carry it, because it is the main alternative explanation to the guilt channel for the promise result.

## Unconfirmed

- Whether the published version of Ellingsen et al. (GEB 2010) has the same correlations as the 2007 working paper; I read the latter only. The abstract (via search) repeats "close to zero in all three experiments".
- The exact symbols in Ederer-Stremitzer's equation (1); recovered by reading the structure of the garbled text. Check against the journal PDF before using `theta` and `k` placements in any equation of the algebra.
- Di Bartolomeo, Dufwenberg & Papa 2023: numbers and the "opposite of Vanberg's" sentence now read in the December 2021 working paper; the journal version was not reachable (publisher bot wall), so the final numbers could differ.
- Bellemare-Sebald-Suetens 2019: read as the preprint only; exact correlation per game not taken.
- Khalmetski-Ockenfels-Werner 2015: abstract-level only (quotes match the accepted manuscript); how expectations were varied was not read.
- Nihonsugi, Tanaka & Haruno 2022 and Schwartz, Spires & Young 2019 (added in validation): abstract only.
- Works cited by Ederer-Stremitzer and Di Bartolomeo et al. that I did not open: Mischkowski, Stone & Stremitzer (conditional guilt, cited as "2016"); Charness & Dufwenberg 2010 "bare promises" (small effects of pre-coded messages); Krupka et al. 2017 (norm-based promise-keeping); Bacharach, Guerra & Zizzo 2007; Bracht & Regner 2013; Chang et al. 2011; Regner & Harth 2014.
- Seeds from the map not read here: Charness & Dufwenberg 2011 "Participation" (AER 101(4), 1211-1237, doi:10.1257/aer.101.4.1211, Crossref-confirmed, not opened); Dufwenberg & Kirchsteiger 2004 (GEB 47, 268-298, doi:10.1016/j.geb.2003.06.003, confirmed, [standard] only); Cox, Friedman & Gjerstad 2007 (GEB 59, 17-45, doi:10.1016/j.geb.2006.05.001, confirmed, [standard] only); Camerer 2003 *Behavioral Game Theory* (book; not opened). These are reciprocity and status models, not tests of the second-order-belief channel.

## Validation log (2026-10-29)

Every DOI below was resolved at api.crossref.org; titles, authors, volumes and pages match unless noted. Numbers in 2.1-2.6 were re-checked line by line against the source texts this file was written from.

- ✓ Battigalli & Dufwenberg 2007, AER 97(2) 170-176, 10.1257/aer.97.2.170.
- ✎ Battigalli & Dufwenberg 2009: was cited without details; added JET 144(1) 1-35, 10.1016/j.jet.2008.01.004.
- ✓ Charness & Dufwenberg 2006, Econometrica 74(6) 1579-1601: all Table II-IV numbers, the 67/44 %, 74/56 %, 50/20 % and the 1583/1592 quotes match [read].
- ✓ Vanberg 2008, Econometrica 76(6) 1467-1480, 10.3982/ECTA7673 (Crossref omits the author; the text names Christoph Vanberg). Table I-III numbers and the footnote 13-14 p-values match; the decimals the extraction lost (Z = 148, p = 014) were read correctly as 1.48 and 0.14 [read].
- ✎ Ellingsen, Johannesson, Tjøtta & Torsvik 2010, GEB 68(1) 95-107: the 455 total includes three monitors (171 + 196 + 88), now said; the exclusion analyses were misdescribed (0.099/0.051 drops the four all-givers and the six high-belief cases, not "gave everything and gave nothing") and are now quoted correctly [read, WP].
- ✓ Reuben, Sapienza & Zingales 2009, Econ. Letters 104(2) 89-91: every figure ($53.75 to $40.63, p = 0.030, $52.14 to $58.29, p = 0.125, $31.77, 43 %, Northwestern MBAs) matches [read].
- ✎ Ederer & Stremitzer 2017, GEB 106 161-178: the 40 %/5 % Don't-Perform figure is for promisors whose choice differed between devices, not all promisors (fixed); the guilt parameter is gamma_D in the paper, not theta (noted); the 104-dictator identification sample added. All other numbers match [read, Cowles DP].
- ✓ Di Bartolomeo, Dufwenberg, Papa & Passarelli 2019, GEB 113 137-146: all belief and Roll-rate numbers, fn. 1 and fn. 4, Table 5 and the "42 % reneged" line match [read].
- ✎ Di Bartolomeo, Dufwenberg & Papa 2023, JESA 9(1) 77-89: upgraded from a fetch summary to [read] in the 2021 working paper; 226 subjects, 1,130 pairs, 76 %/49 % and "opposite of Vanberg's" confirmed.
- ✎ Khalmetski 2016, GEB 97 110-119: claim confirmed in the accepted manuscript; the "legitimate expectations" gloss is not in the paper and was replaced with its own wording.
- ✓ Khalmetski, Ockenfels & Werner 2015, JET 159 163-208: quoted phrases are in the abstract [abstract].
- ✎ Bellemare, Sebald & Suetens 2018, Exp. Econ. 21(2) 316-336: "above zero at all stakes" applies to the 60 % stake-dependent group; narrowed [abstract].
- ✎ Bellemare, Sebald & Suetens 2019, JEP 73 52-59: DOI 10.1016/j.joep.2019.05.002 added; correlation size (Spearman > 0.2) added; the claim that it is "the only bridge" was wrong (Bracht & Regner 2013 came first) and is removed [read, preprint].
- ✎ Ismayilov & Potters: year and venue resolved, Exp. Econ. 19(2) 382-393, 2016, 10.1007/s10683-015-9444-1; the description matches the abstract.
- ✓ Charness & Dufwenberg 2011, AER 101(4); Dufwenberg & Kirchsteiger 2004, GEB 47(2); Cox, Friedman & Gjerstad 2007, GEB 59(1): DOIs resolve, not opened.
- ? Camerer 2003 and the unopened works in Unconfirmed: not checked.
- ✎ "Nothing exists" claims: "all samples are university students" was false for the wider literature (Nihonsugi et al. 2022, online Korea and UK samples) and is now scoped to the causal tests; "no replication" was kept but now names the near misses (Di Bartolomeo et al. 2019; Schwartz, Spires & Young 2019). The meta-analysis negative held up in an OpenAlex search but is weak, because the web-search budget was used up before this pass could search the web.

**Verdict.** The file is accurate and honestly tagged. Every cited work exists with the stated authors, and no fabrication was found. The corrections are mostly about scope: one statistic was given for the wrong subgroup (Ederer-Stremitzer's 40 %), one set of exclusion analyses was misdescribed (Ellingsen et al.), two "only" or "all" claims were too broad (the TOSCA bridge, student-only samples), and one gloss was attributed to Khalmetski that is not in his paper. The main conclusion holds as written: the guilt channel is real but conditional and modest. The promise gate is still an interpretation, and the 2019 own-promise null and the effects found without any promise both count against it.

## Cross-checks (2026-10-29)

Checked against the other files in this directory by grep for the same works, authors, equations and numbers. Files touching this file's material: 21 (Battigalli-Dufwenberg line, Charness-Dufwenberg, Ellingsen et al., Vanberg seed), 41 (guilt row, Tignor & Colvin), 082 (Battigalli-Corrao-Dufwenberg, JEL survey). Files 049, 065, 15, 34 and 38 mention guilt only in unrelated senses, with no overlap in works or numbers. Primary-source checking was not possible for the one open item: the web-search budget was exhausted.

### Agreements

- **File 21, entry 8**: Battigalli & Dufwenberg 2007 (AER 97(2), 170-176, doi:10.1257/aer.97.2.170) and the base let-down form `max(0, E_j[m_j] - m_j)`. This file's operator `Let-down` and the sensitivity `theta >= 0` match 21's `D_j` and `theta_ij`.
- **File 21, entry 9**: Battigalli & Dufwenberg 2009, JET 144(1), 1-35. Matches the citation here.
- **File 21, entry 8, Evidence**: Charness & Dufwenberg 2006 (Econometrica 74(6), doi:10.1111/j.1468-0262.2006.00719.x) and 2011 (AER 101(4), 1211-1237, doi:10.1257/aer.101.4.1211). Citation details agree. 21 marks the 2006 finding "from memory"; this file's [read] figures (Roll 67 % vs 44 %, In 74 % vs 56 %) are consistent with 21's qualitative claim that promises raise trust and trustworthiness.
- **File 21, entry 8, counter-evidence**: Ellingsen, Johannesson, Tjøtta & Torsvik 2010 (GEB 68(1), 95-107, doi:10.1016/j.geb.2009.04.021). Both say three experiments, correlation close to zero, beliefs passed to the dictator or trustee (disclosed). Agree, and this file adds the numbers (r between -0.075 and +0.085, 455 participants).
- **File 21, entry 8**: Khalmetski 2016 (doi:10.1016/j.geb.2016.04.003). The same DOI, and 21 describes it only as an exogenous belief shift with "findings not read". This file supplies the finding, which does not conflict with 21.
- **File 21, entry 10 and the summary table**: Dufwenberg & Kirchsteiger 2004 (GEB 47(2), doi:10.1016/j.geb.2003.06.003) and Cox, Friedman & Gjerstad 2007 (GEB 59(1), 17-45, doi:10.1016/j.geb.2006.05.001). DOIs and pages match; both files tag them as not read.
- **File 21, entry 12**: Camerer 2003, book not located. This file also lists it as [standard], not opened. Consistent.
- **File 41, row "Guilt" and section A** (also its validation log): Tignor & Colvin 2017, dispositional guilt and prosociality r = .13, k = 63. The citation of that figure in section 6 above is accurate. 41 also says guilt has no dynamics and only trait (TOSCA-type) measures, which agrees with section 5 here ("Dynamics" absent).
- **File 21, line 207 and the "Closing claims" section**: this file's critique that the existence theorems do not show human guilt follows the functional form is compatible with 21's own later weakening of its claims in validation.
- **File 082, section 1.6**: Battigalli-Corrao-Dufwenberg 2019 and the 2022 JEL survey. This file does not cite them, so there is no overlap to contradict. Both are relevant background for the "gate" proposal here.

### Contradictions and discrepancies

1. **Vanberg 2008 coverage.** Section 6 above says "Neither file mentions Vanberg 2008" and "File 21 should carry it". **File 21 does mention it**: its further-reading list (around lines 245-246) names Vanberg (2008) as "the main rival to guilt aversion", with "DOI not confirmed". Verdict: **this file is partly wrong**. 21 names the paper but gives no content and no confirmed DOI. This file's confirmed DOI (10.3982/ECTA7673) and content supply what 21 lacks. File 41 does not mention Vanberg, so that half of the statement holds. The wording should read "File 21 lists Vanberg only as unread further reading". This was not edited elsewhere, as instructed.
2. **Charness & Dufwenberg 2011 "Participation".** The Unconfirmed section above (seeds from the map) groups it with "reciprocity and status models, not tests of the second-order-belief channel". **File 21, entry 8** says it supports guilt aversion (guilt from blame), from a search summary and not read. Verdict: **unresolved**. Neither file read the paper, and the search that could settle it (the AER abstract) could not run because the web-search budget was exhausted. My recollection is that it is a guilt-based paper, which would favour 21, but I did not verify it. Do not use either characterisation until the abstract is read.
3. **Bellemare, Sebald & Suetens: two different papers.** File 21 cites a 2017 GEB paper (doi:10.1016/j.geb.2016.11.002) as an attempt to shift beliefs exogenously, "findings not read". This file cites Bellemare, Sebald & Suetens 2018 (Exp. Econ. 21(2)) and 2019 (JEP 73). The DOIs differ, so these are different papers by the same authors, not a conflict. This file does not cover the 2017 GEB paper, so its "exogenous belief shift" list in section 2.7 and the table in section 3 are incomplete on that point. Not a disagreement of fact; flagged for completeness.
4. **File 21 summary table, Ellingsen "contested"** versus this file's claim that the null is on disclosed beliefs and that the effect in Ederer-Stremitzer appears only under a promise. 21's gloss "beliefs are induced" and its entry-8 text ("elicited and passed to the dictator") are the same design this file calls disclosure. No factual conflict; this file's section 6 already proposes the refinement.

### Result

No numeric contradiction between this file and any validated file. One factual slip in this file (item 1), one open question that needs a primary source (item 2), and one coverage gap (item 3).

## Licences of quoted and transcribed material (2026-10-30)

Licences below are not determined from the publisher pages; where no open licence was checked, publisher copyright is presumed. Nothing here is transcribed beyond short quotations, restated equations and prose descriptions of table values.

| Source | Licence | How used |
|---|---|---|
| Charness & Dufwenberg 2006, Econometrica 74(6) | not determined; publisher copyright presumed | short quotations; values from Tables II-IV given as numbers in prose; restated model condition |
| Vanberg 2008, Econometrica 76(6) | not determined; publisher copyright presumed | short quotations; values from Tables I and III given as numbers in prose |
| Ellingsen et al. (WP 2007; GEB 2010) | not determined; publisher copyright presumed | reported correlations as numbers; no extended quotation |
| Reuben, Sapienza & Zingales 2009, Economics Letters | not determined; publisher copyright presumed | reported means and test results as numbers |
| Ederer & Stremitzer 2017, GEB (Cowles DP 1931R) | not determined; publisher copyright presumed | short quotations; restated, reconstructed equations |
| Di Bartolomeo et al. 2019, GEB; Di Bartolomeo, Dufwenberg & Papa 2023, JESA (WP 215) | not determined; publisher copyright presumed | short quotations; Table 5 summarised in prose |
| Khalmetski 2016, GEB; Khalmetski, Ockenfels & Werner 2015, JET (Bath accepted manuscripts) | not determined; publisher copyright presumed | short quotations (a 5-word phrase from an unnamed search summary, attributed as such and rejected; a phrase of about 10 words from the manuscript) |
| Battigalli & Dufwenberg 2007, 2009; Bellemare et al. 2018, 2019; Ismayilov & Potters 2016 | not determined; publisher copyright presumed | citation and description only |

The comparison table in section 3 is our own synthesis in prose-level values. No dataset is quoted, transcribed or reused.
