# Prior work: social preferences, psychological games, emotions as strategic devices

Date: 2026-10-29. Survey for the `social-algebra` strand, drive-survey phase (see `notes/2026-10-29-drives-as-the-core.md`). Aim (Aldred): an algebra of basic human and group drives that compose into equations, give theorems, and predict or control behaviour. Earlier drive surveys (15-19) found drive dynamics for single agents. This file asks where economics already puts **other people's states into one's own motive**, with equations and theorems.

## Summary

- **Economics has a mature, theorem-bearing way to make one person's motive depend on others: a utility with other people's payoffs (Fehr-Schmidt, Bolton-Ockenfels, Charness-Rabin) or other people's beliefs and intentions (Rabin, psychological games).** The first family is static, memoryless and outcome-only. The second is where fear, guilt and anger live.
- **The one formalism that is directly a "drive with state" is the Battigalli-Dufwenberg line** (guilt 2007, dynamic psychological games 2009, frustration/anger with Smith 2019). Utility depends on beliefs, including second-order beliefs; there is an existence theorem for sequential equilibrium; the sums run over all co-players j != i (so more than two players); and anger is a history-dependent quantity (frustration `F_i(h)`) that is created by a gap between expectation and attainable payoff. I read the anger paper's text and the guilt paper's model section.
- **Time and n players are handled only as extensions of the equilibrium machinery, not as dynamics.** There is no law of motion for a drive (no differential equation, no decay, no contagion) in the game-theoretic models here; habit-formation and Kőszegi-Rabin reference points do have one (added in validation; see closing section). Frustration is reset by the game's stage structure. Anticipatory feeling (Caplin-Leahy) and information gaps (Golman-Loewenstein) are single-agent. See the closing section.
- **Verification note.** Bibliographic records were checked in Crossref (DOIs below). Content tagged [read] was read in this session from primary text: Battigalli-Dufwenberg-Smith (2015 working paper version, via `eller.arizona.edu`; the 2019 GEB version is the cited record) and Battigalli-Dufwenberg 2007 (AER, via a Bocconi-hosted PDF). Everything else is [from abstract/standard account], meaning a search abstract, secondary page, or my own recall of the standard form; those are flagged and any number from memory is marked as such. The exact forms for Rabin, Charness-Rabin, Bolton-Ockenfels, Bernheim, Bénabou-Tirole, Caplin-Leahy and Golman-Loewenstein were **not** verified against primary text. A first attempt at several DOIs from memory landed on unrelated papers (for example a guessed DOI for dynamic psychological games resolved to a mechanism-design paper); the DOIs below are the ones whose Crossref title matched.

Entry count: 22 numbered entries, 1-22 (see end of file).

---

## A. Static social preferences (other people's payoffs in my utility)

### 1. Fehr and Schmidt (1999), inequity aversion
- **Citation:** Ernst Fehr and Klaus M. Schmidt, "A Theory of Fairness, Competition, and Cooperation", *Quarterly Journal of Economics* 114(3), 1999. doi:10.1162/003355399556151 (Crossref title confirmed).
- **Utility** [from abstract/standard account; form cross-checked in three secondary sources, one of which states the restrictions]:
  `U_i(x) = x_i - (alpha_i/(n-1)) * SUM_{j!=i} max(x_j - x_i, 0) - (beta_i/(n-1)) * SUM_{j!=i} max(x_i - x_j, 0)`
  with `0 <= beta_i <= alpha_i` and `beta_i < 1`. [Validation: form and restrictions confirmed against Levin's Stanford lecture notes (Econ 286, "Fairness"), which write `0 <= beta_i <= 1`, `alpha_i >= beta_i`; the strict `beta_i < 1` is the paper's own as commonly quoted. Primary text not read.] `alpha` is aversion to being behind (envy), `beta` aversion to being ahead (guilt or fairness). The `beta < 1` bound keeps the own-payoff term from turning negative (a player ahead of everyone would otherwise burn money). The ordering `alpha >= beta` encodes "behind hurts more than ahead".
- **Equilibrium and results:** Nash equilibrium (and subgame perfect) of the game with these utilities. The paper's headline, as I recall it and as its title says: the same distribution of types explains both fair outcomes in ultimatum and public-goods-with-punishment games and selfish outcomes under competition, because in a market a few selfish proposers or competitors set the price. Specific propositions (ultimatum: responders reject if `alpha` is high enough relative to the offer; public goods: cooperation is sustained only when enough types exist to make punishment credible) are [standard account, not read]. The calibrated type distribution (a minority of purely selfish types, roughly a third, and a long tail of high-`alpha` types) is from memory; I did not verify the numbers. [Validation: the distribution usually attributed to the paper is `alpha` in {0, 0.5, 1, 4} with shares 30/30/30/10 % and `beta` in {0, 0.25, 0.6} with shares 30/30/40 %; that is also recall, not confirmed in this pass. A secondary source notes the distribution was chosen, not estimated, and that later estimates found much smaller mean `alpha`.]
- **Critique** [validation addition; abstracts and titles only]: Ken Binmore and Avner Shaked, "Experimental economics: Where next?", *JEBO* 73(1), 87-100, 2010, doi:10.1016/j.jebo.2008.10.019, attack the calibration (the parameter distribution is not fitted to the ultimatum data it claims to explain, and is not then tested out of sample on the other games). Reply: Fehr and Schmidt, "On inequity aversion: A reply to Binmore and Shaked", *JEBO* 73(1), 101-108, 2010, doi:10.1016/j.jebo.2009.12.001; rejoinder doi:10.1016/j.jebo.2009.11.008 (all Crossref title-confirmed). The reply says Binmore and Shaked withdrew some of their points. For the algebra: the most-cited drive parameters in this cluster were never estimated as a joint distribution.
- **Drive formalised:** fairness / envy (`alpha`) and guilt-like fairness (`beta`).
- **Evidence and failures:** fits ultimatum rejections and punishment in public goods. Fails where **intentions** matter: Falk, Fehr and Fischbacher, "Testing theories of fairness - Intentions matter", *Games and Economic Behavior* 62 (2008), doi:10.1016/j.geb.2007.06.001 (Crossref title confirmed; the finding is in the title, details not read). An outcome-only utility cannot distinguish the same outcome reached by a kind or an unkind choice.
- **Operand/operator:** operands are payoff vectors (one number per person); the "operator" is a fixed comparison `max(x_j - x_i, 0)`. Each person carries two parameters. No operator acts between people; the comparison is baked into the utility. For the algebra: this is the **cheapest transmission law** (my motive reads your holdings) and it is symmetric, static and two-parameter.

### 2. Bolton and Ockenfels (2000), ERC
- **Citation:** Gary E. Bolton and Axel Ockenfels, "ERC: A Theory of Equity, Reciprocity, and Competition", *American Economic Review* 90(1), 166-193, 2000. doi:10.1257/aer.90.1.166 (confirmed).
- **Utility** [from abstract/standard account, via a secondary description]: `v_i(y_i, sigma_i)` with `sigma_i = y_i / SUM_j y_j` (defined as `1/n` when the total is zero). Increasing in own payoff, strictly concave in the relative share, with the maximum at `sigma_i = 1/n` (own payoff equals the average).
- **Equilibrium and results:** Nash equilibrium of games with these motivation functions, in an incomplete-information setting stated in observable variables. The paper says it explains equity games (ultimatum, dictator), reciprocity games (prisoner's dilemma, gift exchange) and competitive settings (Bertrand). I could not retrieve the formal propositions; "near-equal split in the ultimatum game" is my recollection, unverified.
- **Drive formalised:** fairness as a preference for the average share, no separate envy or guilt.
- **Evidence and failures:** a comparison paper (found in search, not read in full) reports that the two theories mostly make similar predictions, and that in an experiment built to separate them, behaviour followed Fehr-Schmidt's prediction when it coincided with total-payoff maximisation but was dispersed when it coincided with ERC's. Same intentions weakness as 1.
- **Operand/operator:** operands are payoff vectors reduced to a share; one-dimensional.

### 3. Charness and Rabin (2002), "Understanding Social Preferences with Simple Tests"
- **Citation:** Gary Charness and Matthew Rabin, *Quarterly Journal of Economics* 117(3), 2002. doi:10.1162/003355302760193904 (confirmed).
- **Form** [from abstract/standard account, not read]: a weighted mix of own payoff, the worst-off person's payoff (Rawlsian maximin), and total surplus, plus a reciprocity term that reduces concern for a partner who has "misbehaved". I am not stating the equation because I did not read it.
- **Simple two-person form** [validation addition; standard account, two secondary sources agree on the `rho`, `sigma` part, the `theta q` term is recall]: `U_B(pi_A, pi_B) = (rho*r + sigma*s + theta*q) * pi_A + (1 - rho*r - sigma*s - theta*q) * pi_B`, with `r = 1` if `pi_B > pi_A` (B ahead), `s = 1` if `pi_B < pi_A` (B behind), else 0, and `q = -1` if A has misbehaved, else 0. Difference aversion is `sigma < 0 < rho < 1`; social-welfare preference is `0 < sigma <= rho <= 1`. Secondary sources disagree on the sign convention of `r` and `s`, so check before use. The general n-person model uses a maximin-plus-surplus term with weights `lambda`, `delta` (not retrieved). Note this is **one utility that composes a distributional drive and a reciprocity drive**; see the corrected closing section.
- **Why it matters here:** it is an **experimental discriminator** across the models above, and its design (simple tests that pull models apart) is the template for how an algebra's drive terms would be separated. Reported finding, in the standard account: pure inequity aversion is not enough; efficiency (surplus) and reciprocity both carry weight. Unverified in detail.
- **Drive formalised:** fairness plus efficiency plus reciprocity.

### 4. Rabin (1993), fairness and reciprocity
- **Citation:** Matthew Rabin, "Incorporating Fairness into Game Theory and Economics", *American Economic Review* 83(5), 1281-1302, 1993. Crossref returns only reprints (chapter in *Advances in Behavioral Economics*, doi:10.2307/j.ctvcm4j8j.15 and doi:10.1515/9781400829118-013, both title-confirmed); the original AER DOI was not confirmed (see Unconfirmed).
- **Form** [from abstract/standard account; secondary lecture notes agree on the pieces, but the exact interaction term was not confirmed in them]: each player has a **kindness function** `f_i(a_i, b_j) = (pi_j(b_j, a_i) - pi_j^e(b_j)) / (pi_j^h(b_j) - pi_j^min(b_j))`: how far my action pushes the other's payoff above the "equitable" payoff (midpoint of the other's best and worst Pareto-efficient payoffs), normalised by the gap between the other's best Pareto-efficient payoff and the other's minimum payoff. **Corrected in validation:** the range is `[-1, 1/2]`, not `[-1, 1]`: the numerator can be at most `(pi^h - pi^l)/2` while the denominator is at least `pi^h - pi^l`, so kindness tops out at 1/2 and unkindness reaches -1 (derived from the definition; the asymmetry means unkindness can bite twice as hard as kindness). Utility: `U_i(a_i, b_j, c_i) = pi_i(a_i, b_j) + f~_j(b_j, c_i) * [1 + f_i(a_i, b_j)]`, where `b_j` is i's belief about j's action and `c_i` i's belief about j's belief about i [confirmed against Levin's lecture notes, which carry the `1 +`; primary text, a scanned PDF, not machine-readable].
- **Equilibrium concept and theorems:** **fairness equilibrium** (a Nash equilibrium of the psychological game in which beliefs about beliefs are correct). Confirmed from a secondary page: if material payoffs are such that the outcome is a Nash equilibrium where players either mutually maximise or mutually minimise each other's payoff, it is a fairness equilibrium. That is Rabin's own statement that mutual kindness and mutual hostility are both self-sustaining. [Validation addition, same lecture notes:] a stakes result: when material payoffs are small, mutual-max and mutual-min profiles are fairness equilibria even if not Nash; when they are large, fairness equilibria approach the Nash equilibria. So **the drive's weight relative to material payoff is set by the stakes**, which is a scaling law worth keeping. Fairness equilibrium requires `c_i = b_i = a_i` (beliefs of both orders correct).
- **Drive formalised:** reciprocity, in both directions: **reward kindness and punish unkindness, driven by perceived intention**.
- **Evidence and failures:** normal-form games only, which is why extensions to extensive form exist (entry 10). The multiple-equilibria structure (cooperative and hostile) is the interesting part and is a testable prediction.
- **Operand/operator:** operands are strategies plus first- and second-order beliefs. **This is where "kind act" becomes an operator**: the kindness function is a signed, bounded scalar attached to an action relative to a reference payoff, and the product with the other's kindness is a **multiplicative interaction between two people's drives**. Closest thing in this cluster to a composition rule.

### 5. Levine (1998), altruism and spite
- **Citation:** David K. Levine, "Modeling Altruism and Spitefulness in Experiments", *Review of Economic Dynamics* 1(3), 1998. doi:10.1006/redy.1998.0023 (Crossref title confirmed).
- **Form** [from abstract/standard account, my recollection, not read]: `u_i = pi_i + SUM_{j!=i} ((a_i + lambda a_j)/(1 + lambda)) pi_j`, where `a_i` is player i's own altruism coefficient (negative for spite) and the weight on j blends i's coefficient with j's, so players are kinder to the kind and spiteful to the spiteful. Incomplete information about types; Bayes-Nash equilibrium.
- **Drive formalised:** altruism and spite as signed weights; reciprocity via the other's type.
- **Operand/operator:** operands are types `a_i` (a real number, signed); the `lambda` mixing is an explicit composition of two people's drive parameters. Note this one is **n-player and signed by construction**.

### 6. Envy: Kirchsteiger (1994) and Mui (1995)
- **Citations:** Georg Kirchsteiger, "The role of envy in ultimatum games", *Journal of Economic Behavior and Organization* 25 (1994), doi:10.1016/0167-2681(94)90106-6; Vai-Lam Mui, "The economics of envy", *JEBO* 26 (1995), doi:10.1016/0167-2681(94)00079-t (both Crossref title-confirmed; the abstracts were not read).
- **Content** [from title only plus standard account]: envy enters utility as a negative weight on others' payoffs, producing a willingness to destroy others' payoffs at a cost to oneself. Mui is, as I recall it, about envy's equilibrium and innovation consequences (envy as a brake on others' gains). I did not verify either.
- **Use for the algebra:** envy and spite are the **negative-sign case** of the same slot that altruism fills. Fehr-Schmidt's `alpha` is envy with a kink; Levine's negative `a` is spite without one.

---

## B. Psychological games: beliefs inside payoffs

### 7. Geanakoplos, Pearce and Stacchetti (1989)
- **Citation:** John Geanakoplos, David Pearce, Ennio Stacchetti, "Psychological games and sequential rationality", *Games and Economic Behavior* 1(1), 1989. doi:10.1016/0899-8256(89)90005-5 (confirmed).
- **Form** [from abstract/standard account]: payoffs depend on the **hierarchy of beliefs** as well as on actions. Equilibrium is a fixed point in actions and beliefs, and existence follows under continuity, by the usual fixed-point argument. The paper's examples (guilt about letting someone down, surprise, fear of being rejected) are the original demonstration that **emotions can enter as belief-dependent payoffs**.
- **Limits as reported by later work:** the Battigalli-Dufwenberg 2007 paper notes in a footnote that this framework would not allow a player's utility to depend on other players' beliefs or on updated beliefs [read, as their characterisation; I did not read GPS]. The later line (entries 8-9) was built to fix that.
- **Drive formalised:** any emotion that is a function of expectation: surprise, guilt, anxiety.

### 8. Battigalli and Dufwenberg (2007), "Guilt in Games"
- **Citation:** Pierpaolo Battigalli and Martin Dufwenberg, *American Economic Review* 97(2), 170-176, 2007. doi:10.1257/aer.97.2.170 (confirmed).
- **Utility** [read]: with `m_i` material payoff, `D_j(z, s_j, alpha_j) = max{0, E[m_j | h0] - m_j(z)}` how much j is "let down" relative to what j initially expected, and `G_ij` the part of that due to i's behaviour (the shortfall minus the least it could be given i's other choices):
  **simple guilt:** `u_i^SG(z, s_-i, alpha_j) = m_i(z) - SUM_{j!=i} theta_ij * G_ij(z, s_-i, alpha_j)`, `theta_ij >= 0` is guilt sensitivity;
  **guilt from blame:** i cares about what j *infers* about i's intentions, an expectation over j's updated beliefs. Beliefs up to the fourth order are used.
  [Validation: re-read from the Bocconi-hosted AER PDF. `G_ij(z, s_-i, alpha_j) = D_j(z, s_j, alpha_j) - min_{s_i} D_j(z(s_i, s_-i), s_j, alpha_j)` is confirmed. The paper also names the simpler form often quoted, `u_i = m_i(z) - SUM_{j!=i} theta_ij * D_j(z, s_j, alpha_j)`, i.e. `m_i - theta_ij * max(0, E_j[m_j] - m_j)`, and explains why it uses `G_ij` instead: the plain `D_j` would make i guilty for let-down caused by others. The two coincide when i could have avoided all of j's let-down.]
- **Equilibrium and theorems** [read]: sequential equilibrium for the psychological game. They state that every psychological game with simple guilt or guilt from blame has a sequential equilibrium (via the existence proof of Battigalli-Dufwenberg 2009). Observation 1: in any two-player simultaneous-move game without chance moves, pure-strategy equilibria of the two guilt types coincide. Observation 2: in any simultaneous-move game without chance moves, every pure-strategy equilibrium of the material-payoff game is also an equilibrium with guilt. Example 1 (three players, a dummy Cleo) shows the two guilt types **diverge** with three players: abstaining is an equilibrium under simple guilt but not under guilt from blame when the deviator cannot be identified, so blame can be diffused.
- **Drive formalised:** guilt. **The shortfall is measured against the other person's expectation**, so the drive is created by a *belief about someone else's belief*.
- **Evidence:** Charness and Dufwenberg, "Promises and Partnership", *Econometrica* 74(6), 2006, doi:10.1111/j.1468-0262.2006.00719.x (Crossref title-confirmed; the finding that promises raise trust and trustworthiness is from memory). Charness and Dufwenberg, "Participation", *American Economic Review* 101(4), 1211-1237, 2011, doi:10.1257/aer.101.4.1211 (Crossref title-confirmed in validation; the claim that it supports guilt aversion is from a search summary, not read). **Counter-evidence, added in validation** [abstract]: Ellingsen, Johannesson, Tjøtta and Torsvik, "Testing guilt aversion", *GEB* 68(1), 95-107, 2010, doi:10.1016/j.geb.2009.04.021: the earlier positive correlation between second-order beliefs and generosity may be a false-consensus effect; when recipients' expectations are elicited and passed to the dictator or trustee, the correlation is **close to zero** in three experiments, so guilt aversion is smaller than thought. Later attempts to shift beliefs exogenously exist (Khalmetski 2016, doi:10.1016/j.geb.2016.04.003; Bellemare, Sebald and Suetens 2017, doi:10.1016/j.geb.2016.11.002; both title-confirmed, findings not read). Net: the guilt term's empirical weight is **contested**, not established. Also Battigalli, Charness and Dufwenberg, "Deception: The role of guilt", *JEBO* 93 (2013), doi:10.1016/j.jebo.2013.03.033 (title confirmed; content not read).
- **Operand/operator:** operands are strategies and beliefs of every order; the sum over `j != i` makes it **n-player**, and the three-player example shows n-player is not a trivial add-on (blame attribution). The guilt term is a **max-with-zero ("let-down") operator** composed with a "counterfactual least harm" subtraction.

### 9. Battigalli and Dufwenberg (2009), "Dynamic psychological games"
- **Citation:** *Journal of Economic Theory* 144(1), 2009. doi:10.1016/j.jet.2008.01.004 (Crossref confirmed; the SSRN preprint doi:10.2139/ssrn.707401 also exists).
- **Content** [read only as quoted in the BDS text]: extends psychological games to extensive form with **conditional probability systems over beliefs** and proves existence of a sequential equilibrium for continuous belief-dependent utilities. BDS write that they use these "abstract definitions of equilibrium for games with belief-dependent preferences (and the associated existence theorem)" which "apply to all multistage game forms". That is the dynamic-games existence theorem the whole line rests on. The theorem statement itself I did not read; the BDS text calls it a "trembling-hand technique" proof.
- **Role:** the formal base: beliefs get **updated as the game unfolds** and utility at a node may depend on them. Time is event time (stages), not clock time.

### 10. Dufwenberg and Kirchsteiger (2004), sequential reciprocity
- **Citation:** Martin Dufwenberg and Georg Kirchsteiger, "A theory of sequential reciprocity", *Games and Economic Behavior* 47(2), 2004. doi:10.1016/j.geb.2003.06.003 (Crossref title confirmed; the content below is from the title and standard account).
- **Content** [from abstract/standard account]: Rabin's kindness mechanics carried to extensive-form games, with kindness evaluated at each node on updated beliefs; the equilibrium is a **sequential reciprocity equilibrium**, with existence for finite games asserted in the standard account.
- **Also:** Falk and Fischbacher, "A theory of reciprocity", *Games and Economic Behavior* 54(2), 2006, doi:10.1016/j.geb.2005.03.001 (title confirmed): reciprocity as a function of kindness and **intention**. Not read. [Validation, from abstract and a secondary description:] kindness is the product of an **outcome term** (the payoff difference between the players, so an inequity measure) and an **intention factor** (smaller when the other had no fairer alternative); the reciprocation term multiplies that by how much i alters j's payoff. So this is a single utility that **composes inequity aversion and intention-based reciprocity**, with an equilibrium concept (reciprocity equilibrium; existence asserted in the standard account, not checked). It is cited as fitting ultimatum, gift-exchange, best-shot, dictator, PD and public-goods data.
- **Also** [validation addition]: Cox, Friedman and Gjerstad, "A tractable model of reciprocity and fairness", *GEB* 59(1), 17-45, 2007, doi:10.1016/j.geb.2006.05.001 (title-confirmed; not read): altruism weight that moves with the other's generosity and with status, i.e. an "emotional state" parameter driven by the other's act.
- **Drive formalised:** reciprocity (reward/punish) with time-structure.

### 11. Battigalli, Dufwenberg and Smith (2019), frustration, aggression and anger
- **Citation:** Pierpaolo Battigalli, Martin Dufwenberg, Alec Smith, "Frustration, aggression, and anger in leader-follower games", *Games and Economic Behavior* 117, 15-39, 2019. doi:10.1016/j.geb.2019.06.001 (confirmed). Earlier: "Frustration and Anger in Games", CESifo WP 5258, 2015 (doi:10.2139/ssrn.2591839); I read the 2015 working-paper text, and equation numbers below are its.
- **Utility** [read]: player i at history h picks action `a_i` to maximise
  `u_i(h, a_i, alpha_i) = E[pi_i | (h, a_i), alpha_i] - theta_i * SUM_{j != i} B_ij(h, alpha_i) * E[pi_j | (h, a_i), alpha_i]`   (their eq. 5)
  with `theta_i >= 0` a sensitivity, `B_ij >= 0` how much of i's **frustration** is blamed on j, and `B_ij` positive only when frustration `F_i` is positive (eq. 6). So an angry player trades own payoff against hurting the blamed player, in proportion to blame. Frustration is the shortfall of the payoff attainable now against what was expected; in the multistage "slow play" extension `F_i(h, alpha_i) = [E[pi_i | h, alpha_i] - max_a E[pi_i | (h, a), alpha_i]]^+`. Blame variants: **simple anger** `B_ij = F_i` (anger is not directed); **anger from blaming behaviour** (blame falls on the player(s) who moved in the first stage); and **anger from blaming intentions** (blame depends on what i thinks j expected or intended). In leader-follower games simple anger coincides with both behaviour-blame versions.
- **Equilibrium and theorems** [read]: sequential equilibrium of the psychological game. Theorem 1: if decision utility is continuous in beliefs, a sequential equilibrium exists; Corollary 1: every game with any of the three anger utilities has one. Proposition 1: in a two-stage perfect-information game with no chance moves and a unique equilibrium of the material-payoff game, that equilibrium is realization-equivalent to an equilibrium of the anger game (anger lives only off the path, as **threat**). Proposition 2: for leader-follower games, equilibria in which the leader mixes with full support correspond to purified equilibria. Multiple equilibria arise: in the Ultimatum Minigame, whether the responder is frustrated depends on what he expected, so **expectations select the equilibrium**. A hold-up example shows **fast play versus slow play** (whether beliefs update between stages) changes the equilibrium set.
- **Drive formalised:** anger as **frustration (expectation shortfall) times blame, acting as a taste for hurting**. This is the cleanest formalisation in this cluster of a drive that (a) is a state, (b) is triggered by another person's act, (c) gets expressed as an act against that person.
- **Evidence:** the paper discusses experimental and field evidence rather than running one; it refers in its discussion to a field result by Card and Dahl on family violence after unexpected football losses [read, as a mention]. A test: Aina, Battigalli and Gamba, "Frustration and anger in the Ultimatum Game: An experiment", *GEB* 122 (2020), doi:10.1016/j.geb.2020.04.006 (Crossref title confirmed; findings not read).
- **Operand/operator:** operands are belief systems and a payoff scale; **operators** are `F` (expectation minus best available), `B` (blame allocator, three versions), and the `theta * B * pi_j` hurting term. The multistage extension (Section 6 of the paper) is the only item in this survey that writes down a **drive carried across periods**, though only as lagged expectations, not as a decaying state.

### 12. Camerer (2003), behavioural game theory, for empirical standing
- **Citation:** Colin F. Camerer, *Behavioral Game Theory: Experiments in Strategic Interaction*, Princeton University Press, 2003. Crossref has book reviews (Baltz 2004, doi:10.1007/s11615-004-0067-y; Prosch 2018, doi:10.14712/24647055.2018.28) and a Camerer chapter in *Advances in Behavioral Economics* (doi:10.1515/9781400829118-016), which are **not** the book; the book DOI was not located (see Unconfirmed).
- **Use:** the standard compendium of ultimatum, trust, public-goods, centipede and beauty-contest data and the models fitted to them. Use it as the evidence base for which of entries 1-11 survive. I did not read it this session; I cannot report specific numbers.

---

## C. Status, image and conformity

### 13. Frank, *Choosing the Right Pond* (1985), and positional goods
- **Citation:** Robert H. Frank, *Choosing the Right Pond: Human Behavior and the Quest for Status*, Oxford University Press, 1985. Crossref: reviews only (Soligo, *Southern Economic Journal* 1986, doi:10.2307/1059455; Wagner, *Contemporary Sociology* 1986, doi:10.2307/2070056; a *Public Choice* 1988 note, doi:10.1007/bf00052075). Book DOI not located.
- **Content** [from the title and standard account; not read]: people care about rank within a reference group; positional goods (consumption whose value depends on what others have) generate an arms race; preference for a small pond in which one ranks high. Formally, utility depends on own consumption and own rank or relative level, so welfare effects of growth need not be positive.
- **Survey:** Ori Heffetz and Robert H. Frank, "Preferences for Status: Evidence and Economic Implications", in *Handbook of Social Economics*, 2011, doi:10.1016/b978-0-444-53187-2.00003-6 (confirmed; not read).
- **Drive formalised:** status-seeking, rank-envy.

### 14. Clark and Oswald (1996), comparison income
- **Citation:** Andrew E. Clark and Andrew J. Oswald, "Satisfaction and comparison income", *Journal of Public Economics* 61(3), 359-381, 1996. doi:10.1016/0047-2727(95)01564-7 (confirmed).
- **Form** [from abstract/standard account]: utility (job satisfaction) as a function of own income and a **comparison income** `y*`, estimated, not derived.
- **Evidence** [abstract]: about 5,000 British workers; reported satisfaction is inversely related to comparison wage rates; a secondary summary says the negative effect of comparison income outweighs the positive effect of absolute income in magnitude.
- **Operand/operator:** a one-parameter reference-income operand; no dynamics beyond choosing the reference group.

### 15. Bernheim (1994), conformity
- **Citation:** B. Douglas Bernheim, "A Theory of Conformity", *Journal of Political Economy* 102(5), 841-877, 1994. doi:10.1086/261957 (confirmed).
- **Form and results** [from abstract, found in search]: payoff is intrinsic utility from one's action plus **status** (esteem), which depends on what others believe about one's unobservable type, inferred from one's action. Result: when status matters enough relative to intrinsic utility, many people conform to one homogeneous standard despite heterogeneous underlying preferences; the penalty for nonconformity arises in equilibrium rather than being assumed; both persistent norms and transitory fads arise at different parameter values. Equilibrium concept: (signalling) perfect Bayesian; not verified.
- **Drive formalised:** need for approval / belonging.
- **Operand/operator:** this is a **two-level model**: the operand is a belief about a type, and action is the operator that moves the belief. It is the closest in this survey to a **norm-formation theorem** at group level.

### 16. Bénabou and Tirole (2006), prosocial behaviour and image
- **Citation:** Roland Bénabou and Jean Tirole, "Incentives and Prosocial Behavior", *American Economic Review* 96(5), 1652-1678, 2006. doi:10.1257/aer.96.5.1652 (confirmed).
- **Content** [from abstract, found in search]: prosocial behaviour reflects an endogenous, unobservable **mix of intrinsic, extrinsic and reputational motives**, which observers have to infer. Rewards or punishments make the motive ambiguous and can partly or fully crowd out the behaviour (the overjustification effect); whether acts are strategic complements or substitutes depends on whether stigma or honour dominates; a sponsor-competition result is noted as potentially lowering welfare.
- **Utility** [read in validation, IZA DP 1695 version, eqs. 1-2; check numbering against the AER text]: agent with type `(v_a, v_y)` chooses participation `a` at incentive rate `y` to maximise `(v_a + v_y*y)*a - C(a) + R(a, y)`, with reputational payoff `R(a, y) = x * [gamma_a * E(v_a | a, y) - gamma_y * E(v_y | a, y)]`, `gamma_a, gamma_y >= 0`, `x` the visibility of the act. The agent wants to be seen as prosocial (high `v_a`) and **not greedy** (low `v_y`); a reward raises the inference that the act was for money, which is the crowding-out channel. Three motives, one additive utility, with the interaction arising through the observer's inference.
- **Drive formalised:** reputation / self-image.
- **Operand/operator:** the operator "attach an incentive" feeds back into the operand "what others infer about my motive". Gives a theorem-grade **non-additivity of drives** (rewarding a drive can erase another).

---

## D. Emotions as commitment devices; evolutionary grounding

### 17. Frank (1987/1988), emotions as commitment
- **Citations:** Robert H. Frank, "If Homo Economicus Could Choose His Own Utility Function, He Would Want One with a Conscience", *American Economic Review* 77(4), 1987 (found in Crossref only as a 2017 reprint in *Evolutionary Ethics*, doi:10.4324/9781315255767-14, title-confirmed); *Passions within Reason: The Strategic Role of the Emotions*, W. W. Norton, 1988 (a German edition, *Die Strategie der Emotionen*, appears in Crossref as doi:10.1515/9783486827248, 1992, title-confirmed as a translation).
- **Argument** [from title and standard account; not read]: some emotions (anger, guilt, love, shame) work as **commitment devices** that make threats and promises credible because they are hard to fake. A person disposed to retaliate irrationally, if others can detect this, can do better than a pure maximiser; the cost of the disposition is repaid in avoided exploitation. The equilibrium is a population of detectably committed and non-committed types, with detection (honest signals) as the load-bearing assumption.
- **Drive formalised:** anger, guilt, love as strategic assets.
- **Why it matters:** this is the only item in the cluster that says what drives are **for**, which is exactly what an algebra meant to predict and control behaviour needs.

### 18. Hirshleifer, emotions as guarantors of threats and promises
- **Reference:** Jack Hirshleifer, "On the emotions as guarantors of threats and promises", in J. Dupré (ed.), *The Latest on the Best: Essays on Evolution and Optimality*, MIT Press, 1987 (recalled; **not found in Crossref**). A Crossref search on the title returned unrelated work. It is in Unconfirmed.
- **Content** [recall only]: the same commitment argument as Frank, from an evolutionary angle.

### 19. Bowles and Gintis, strong reciprocity
- **Citations:** Samuel Bowles and Herbert Gintis, "The evolution of strong reciprocity: cooperation in heterogeneous populations", *Theoretical Population Biology* 65(1), 2004. doi:10.1016/j.tpb.2003.07.001 (confirmed); *A Cooperative Species*, Princeton University Press, 2011, doi:10.1515/9781400838837 (confirmed). Experimental base: Ernst Fehr and Simon Gächter, "Altruistic punishment in humans", *Nature* 415, 2002, doi:10.1038/415137a (confirmed; abstract not read).
- **Content** [from title and standard account]: **strong reciprocity** is a predisposition to cooperate with cooperators and punish defectors at a personal cost, even in one-shot interactions. The 2004 paper is, as I recall it, an agent-based and analytic model showing such types can persist and spread in heterogeneous populations where group-level competition rewards them. The mechanics and the fixation conditions were not read.
- **Drive formalised:** cooperative and punitive dispositions as heritable traits.
- **Relevance:** population-level dynamics over drive types (replicator-like), unlike entries 1-11, which are one-game. It is the only item here with a law of motion, and the motion is over **who exists**, not over a drive's intensity within a person.

---

## E. Information, curiosity and fear (single-agent but economic)

### 20. Loewenstein (1994) and Golman-Loewenstein (2018), curiosity as an information gap
- **Citations:** George Loewenstein, "The psychology of curiosity: A review and reinterpretation", *Psychological Bulletin* 116(1), 1994. doi:10.1037/0033-2909.116.1.75 (confirmed). Russell Golman and George Loewenstein, "Information gaps: A theory of preferences regarding the presence and absence of information", *Decision* 5(3), 2018. doi:10.1037/dec0000068 (confirmed). The earlier working paper "Curiosity, Information Gaps, and the Utility of Knowledge" is doi:10.2139/ssrn.2149362.
- **Content** [from titles and standard account; the model's equation was not retrieved]: curiosity is a deprivation drive that arises when attention is drawn to a gap between what one knows and what one wants to know; its strength depends on how much attention is on the question and on how close one is to the answer. The 2018 model puts attention-weighted information gaps into utility and derives when people seek or avoid information.
- **Utility** [read in validation, CMU-hosted preprint of the *Decision* paper, eq. 1]: `u(pi, w) = SUM_{x in X} pi_X(x) v_X(x) + SUM_{i=1..m} w_i * ( SUM_{A_i} pi_i(A_i) v_i(A_i) - H(pi_i) )`: expected material value, plus for each activated question `i` its attention weight `w_i` times (expected **valence** of the answers minus the **entropy** `H` of current beliefs about it). Uncertainty is aversive in proportion to attention; curiosity is the drive to remove the `-w_i H` term, avoidance the drive to keep bad-valence answers unresolved or unattended. Attention depends on salience and importance. This is a genuine **two-term composition** (valence, the fear/hope side, and clarity, the curiosity side) in one utility, although single-agent.
- **Drive formalised:** curiosity.
- **Gap for us:** single-agent. No social transmission.

### 21. Golman, Hagmann and Loewenstein (2017), information avoidance
- **Citation:** *Journal of Economic Literature* 55(1), 96-135, 2017. doi:10.1257/jel.20151245 (confirmed).
- **Content** [from abstract/summary]: the standard economic view says people should never avoid free information; the paper catalogues when and how they do (not obtaining information, directing attention away, forgetting) and why. Three motives I recall as emotion management, decision costs and belief maintenance; not confirmed from the abstract I retrieved.
- **Drive formalised:** fear and ego-protection as drives that *reduce* information gathering, a direct interaction of fear and curiosity, but written as a survey, not as a theorem.

### 22. Caplin and Leahy (2001), anticipatory feelings
- **Citation:** Andrew Caplin and John Leahy, "Psychological Expected Utility Theory and Anticipatory Feelings", *Quarterly Journal of Economics* 116(1), 55-79, 2001. doi:10.1162/003355301556347 (confirmed; note that the DOI I first guessed resolved to a different paper).
- **Content** [from abstract]: extends expected utility to situations in which agents feel **anticipation before uncertainty resolves**; shows such feelings can create **time inconsistency**; gives a portfolio example for asset prices. A later paper (Barigozzi and Levaggi, *J. Risk and Uncertainty* 2010, doi:10.1007/s11166-010-9092-y, "Emotional decision-makers and anomalous attitudes towards information", *JRU* 40(3), Crossref-confirmed in validation) uses a simple version for information acquisition and finds anomalous attitudes to information. The preference representation (utility over beliefs) was not retrieved. [Validation, standard account, not read:] a two-period structure in which the first-period "psychological state" depends on beliefs about second-period physical outcomes and enters utility; the ex-ante self values the anticipatory term, the later self no longer does once it has passed, which is the source of the time inconsistency, handled by treating the agent as a sequence of selves in a subgame-perfect way (Caplin's own page describes "recursive methodology" for changing tastes). Unconfirmed in detail.
- **Drive formalised:** fear / anxiety / hope as functions of the belief held now about a future state.
- **Operand/operator:** the operand is a **belief distribution** and the value attached to holding it; this is the cleanest "fear as state" in economics and it is single-agent.

### Cross-reference
- **Akerlof and Kranton (2000), identity:** already covered in `docs/prior-work/10`, which holds full equations read from the paper PDF. It belongs in the table below as the "identity/social category" slot (utility depends on one's own action relative to prescriptions for one's category and on others' actions) and is not repeated.

---

## Table: drive -> formal object -> theorem -> evidence

| Drive | Formal object | Theorem / result | Evidence and failure |
|---|---|---|---|
| Fairness (static) | Fehr-Schmidt `alpha`, `beta`; ERC share `sigma_i` | Nash equilibrium; fairness and competition both explained (F-S, title claim) | Fits ultimatum and punishment; fails on intentions (Falk-Fehr-Fischbacher 2008) |
| Envy / spite | `alpha` kink; Levine signed `a_i` | Bayes-Nash with type-dependent weights (Levine, recalled) | Rejections of low offers; Kirchsteiger and Mui not read |
| Reciprocity | Rabin kindness product; Dufwenberg-Kirchsteiger; Falk-Fischbacher | Fairness equilibrium; mutual max and mutual min are equilibria (Rabin, secondary) | Intentions matter; multiple equilibria |
| Guilt | `theta_ij * G_ij` let-down measure (Battigalli-Dufwenberg 2007) | Sequential equilibrium exists; simple guilt and guilt-from-blame diverge at 3 players [read] | Promises experiment (Charness-Dufwenberg 2006); near-zero belief-generosity correlation when beliefs are induced (Ellingsen et al. 2010): contested |
| Anger | `theta_i * B_ij * pi_j` with frustration `F_i` [read] | Existence (Thm 1, Cor 1); anger is a threat off the path (Prop 1); expectations select equilibria [read] | Lab test (Aina-Battigalli-Gamba 2020, not read); field mention (Card-Dahl) |
| Status / rank | Rank or comparison income in utility; esteem (Bernheim) | Conformity equilibrium; persistent norms and fads (Bernheim, abstract) | Comparison-income effect on satisfaction (Clark-Oswald, abstract); Frank not read |
| Image / reputation | Bénabou-Tirole `(v_a + v_y y)a - C(a) + x[gamma_a E(v_a) - gamma_y E(v_y)]` [read, WP] | Crowding out under extrinsic incentives | Not tested in what I read |
| Strategic emotion | Frank / Hirshleifer commitment | Verbal-evolutionary; no theorem I verified | Not read |
| Cooperative / punitive trait | Bowles-Gintis strong reciprocity | Persistence in heterogeneous populations (title, recalled) | Fehr-Gächter punishment results (not read) |
| Curiosity | Information gap (Loewenstein; Golman-Loewenstein) | Information-seeking and avoidance conditions (standard account) | Behavioural review (JEL, 2017) |
| Fear / anxiety | Anticipatory utility, belief-dependent (Caplin-Leahy) | Time inconsistency (abstract) | Applications to information (Barigozzi-Levaggi, summary) |
| Identity | A-K 2000 (see file 10) | See file 10 | See file 10 |

## What exists versus what does not

**Exists**
- **Several clean motive slots in which another person enters one's own utility:** payoff comparison (F-S, ERC, Levine), kindness with intention (Rabin, D-K), expectation shortfall (guilt, anger), esteem (Bernheim), reference income (Clark-Oswald).
- **Two drives with a belief-based mechanism and theorems:** guilt and anger (Battigalli and coauthors). Existence of equilibrium under continuity [read]; threat/off-path anger result [read]; equilibrium selection by expectations [read]. These are the nearest thing to the target: a drive as an equation with a proved property.
- **Signed composition:** altruism and spite are the same slot with opposite signs; Levine mixes two people's coefficients.
- **n players in the formal statement:** the BDS and guilt utilities sum over all `j != i`; Levine and F-S also sum over co-players. The guilt paper shows n >= 3 is not trivial (blame diffusion with a dummy third party).
- **Time in event form:** BDS Section 6 (multistage, slow and fast play) and Battigalli-Dufwenberg 2009 (belief updating through the game).

**Does not exist (in what I found)**
- **A drive that changes over time as a quantity.** Frustration is recomputed from lagged expectations at each history; nothing decays, accumulates or is contagious. Anticipatory feelings (Caplin-Leahy) give time inconsistency but not a trajectory. The only dynamics are over *types in a population* (Bowles-Gintis) and over *beliefs within one game*. [Validation qualifier: true within this cluster's game-theoretic models, but not of economics at large. Relative-position utility **does** have explicit laws of motion in the habit-formation and "keeping up with the Joneses" literature: Abel (1990, *AER* P&P, NBER w3279, doi:10.3386/w3279) and Campbell and Cochrane ("By Force of Habit", *JPE* 1999; DOI not confirmed) let the reference level be a decaying weighted average of past own or aggregate consumption, i.e. a status/comparison reference that accumulates and decays on clock time. Kőszegi and Rabin (2006, *QJE* 121(4), doi:10.1162/qjec.121.4.1133; 2009, *AER* 99(3), "Reference-Dependent Consumption Plans", doi:10.1257/aer.99.3.909; both title-confirmed, not read) make the reference point **lagged rational expectations** that update over periods, the same "expectation minus outcome" structure as BDS frustration. None of these is social in the psychological-game sense, but they are the nearest existing laws of motion for a reference-dependent drive.]
- ~~More than one drive interacting in one person with a theorem.~~ **Corrected in validation: this claim was too strong, and contradicted entry 16 of this same file.** Composed utilities with results do exist: Charness-Rabin (distributional concern plus reciprocity, one utility); Falk-Fischbacher 2006 (inequity outcome term times intention factor, with an equilibrium concept); Bénabou-Tirole 2006 (intrinsic plus extrinsic plus reputational motive, with proved crowding-out results, i.e. a theorem about how two drives interact); Golman-Loewenstein 2018 (valence plus entropy-aversion, axiomatised). And the Battigalli-Dufwenberg existence theorem (2009; BDS Theorem 1) holds for **any** utility continuous in beliefs, so a sum of guilt and anger terms has an equilibrium for free; Battigalli, Corrao and Dufwenberg, "Incorporating belief-dependent motivation in games", *JEBO* 167, 185-218, 2019, doi:10.1016/j.jebo.2019.04.009, and the survey Battigalli and Dufwenberg, "Belief-Dependent Motivations and Psychological Game Theory", *JEL* 60(3), 833-882, 2022, doi:10.1257/jel.20201378 (both title-confirmed, not read) set out the general framework in which several belief-dependent motives sit side by side. What remains true: I found no paper that puts anger and guilt in one utility and derives a result **specific to their interaction** (as opposed to existence); and the compositions that exist are additive or multiplicative terms in a static utility, not a calculus of drives.
- **Transmission between people as an operator.** Entry 4's kindness product and Levine's mixing are the closest, and both are one-shot static functions. Nothing in this cluster says how my anger *causes* your fear, then your behaviour, then my next anger, as a repeated composition.
- **Group-level drives as objects.** Conformity and norms (Bernheim) and strong-reciprocity population models are group-level, but group drive is an emergent equilibrium property, not an operand. No cluster entry gives a "group fear" or "group anger" term.
- **Prediction record at the individual level.** Experimental work confirms qualitative patterns (rejections, punishment, promises) at aggregate level; the repeated finding is that outcome-only models miss intention. I found no evidence in this cluster that a drive equation predicts a specific individual's later behaviour; the first synthesis' warning stands.
- **Verified fit of continuous-intensity drives.** All the intensity parameters (`alpha`, `theta`) are fixed per person and estimated from choices.

**For the algebra** (my reading, not a source's claim): the most reusable piece is the BDS pattern, a drive defined as `(expectation or reference) minus (attainable)` clipped at zero and multiplied by an attribution weight over other people. That gives an explicit operator for the creation of a drive and a second operator for its expression, and the existence theorem shows such compositions can be well-posed. What would have to be added is a law of motion for the drive level between acts and a rule for composing two different drives in one person.

---

## Unconfirmed (not located in Crossref or only recalled)
- Rabin (1993) original AER record (*AER* 83(5), 1281-1302; the volume and pages were independently given by a search result in validation, but 1993 AER articles generally have no Crossref DOI, so "not confirmed" here means no DOI exists to check, not that the record is doubtful). Reprint chapters confirmed: doi:10.1515/9781400829118-013 (2004) and doi:10.2307/j.ctvcm4j8j.15 (2011 edition).
- Charness-Rabin `theta q` reciprocity term and the r/s sign convention: recall plus disagreeing secondary sources.
- Fehr-Schmidt calibrated distribution (30/30/30/10 for `alpha`, 30/30/40 for `beta`): recall.
- Falk-Fischbacher existence theorem: standard account.
- Campbell-Cochrane (1999) DOI: Crossref lookup failed in validation.
- Caplin-Leahy formal structure: standard account only.
- Frank (1987) AER original (only a 2017 reprint chapter confirmed); *Passions within Reason* (1988, Norton) and *Choosing the Right Pond* (1985, OUP): books, DOI not located.
- Hirshleifer (1987), "On the emotions as guarantors of threats and promises": not found in Crossref.
- Camerer (2003) book: not located; reviews only.
- Charness and Dufwenberg (2011), "Participation": record now confirmed (doi:10.1257/aer.101.4.1211); the guilt-from-blame finding is still from a search summary.
- Exact equations for ERC theorems, Bernheim, Levine, Caplin-Leahy: not retrieved. (Rabin confirmed against lecture notes, Bénabou-Tirole and Golman-Loewenstein read in validation, Charness-Rabin from secondary sources.)
- Fehr-Schmidt's specific propositions: from memory, not verified.
- Kirchsteiger (1994) and Mui (1995) abstracts: title only.
- GPS (1989) text itself: the limitation attributed to it is Battigalli and Dufwenberg's characterisation.

Entry count: 22 numbered entries (A 1-6, B 7-12, C 13-16, D 17-19, E 20-22) plus the Akerlof-Kranton cross-reference and an Unconfirmed list.

## Clearly missing work (added in validation)
- **Kőszegi-Rabin expectation-based reference dependence** (2006, 2009; DOIs above): the general, non-social version of "expectation minus outcome" that BDS frustration and BD guilt both specialise; with lagged expectations it is the nearest existing law of motion for such a drive.
- **Habit formation / keeping up with the Joneses** (Abel 1990; Campbell-Cochrane 1999): status and comparison utility with an explicit, decaying reference state. Directly relevant to entries 13-14 and to the "no law of motion" claim.
- **Battigalli-Dufwenberg JEL survey (2022)** and **Battigalli-Corrao-Dufwenberg (2019)**: the up-to-date map of belief-dependent motives (guilt, anger, surprise, image, reciprocity) in one framework; should be read before the algebra's "drive slot" design is fixed.
- **Vanberg (2008), "Why do people keep their promises?"** (*Econometrica*; DOI not confirmed): the main rival to guilt aversion as the explanation of Charness-Dufwenberg's promise effect (preference for promise keeping vs expectation-based guilt).
- **Cox-Friedman-Gjerstad (2007)**: reciprocity as an emotional state that shifts the altruism weight; added to entry 10.
- **Andreoni (1990) warm glow** and **Akerlof-Dickens (1982) cognitive dissonance** (utility over beliefs, the precursor to Caplin-Leahy and Golman-Loewenstein): standard slots not covered. Recalled, not checked.

## Validation log (2026-10-29)
Every DOI in the original file (42 checked) resolved in Crossref with matching title and authors; none was wrong.
- 1 Fehr-Schmidt: ✎ form confirmed (secondary); calibration numbers supplied but left as recall; Binmore-Shaked 2010 critique and F-S reply added.
- 1 Falk-Fehr-Fischbacher 2008: ✓
- 2 Bolton-Ockenfels ERC: ✓ (form consistent with standard account; theorems still unread)
- 3 Charness-Rabin: ✎ added the `rho r + sigma s + theta q` form, tagged as secondary/recall; noted it composes two drives.
- 4 Rabin 1993: ✎ kindness range corrected from [-1, 1] to [-1, 1/2]; `(1 + f_i)` form confirmed; small/large-stakes result added; original AER has no DOI (? record only).
- 5 Levine 1998: ✓ record; ? form (recall, unchanged).
- 6 Kirchsteiger 1994, Mui 1995: ✓ records; ? content.
- 7 GPS 1989: ✓ record; existence-under-continuity description consistent with standard account.
- 8 Battigalli-Dufwenberg 2007: ✓ `G_ij` re-read and confirmed; ✎ simpler `D_j` form and its relation noted; Charness-Dufwenberg 2006 ✓; Charness-Dufwenberg 2011 moved from Unconfirmed to confirmed; ✎ Ellingsen et al. 2010 counter-evidence added; Battigalli-Charness-Dufwenberg 2013 ✓.
- 9 Battigalli-Dufwenberg 2009: ✓ record (JET 144(1), 1-35).
- 10 Dufwenberg-Kirchsteiger 2004: ✓ record; Falk-Fischbacher 2006 ✎ content added (inequity x intention); Cox-Friedman-Gjerstad 2007 added.
- 11 Battigalli-Dufwenberg-Smith 2019: ✓ record; content not re-read (original [read] tags kept). Aina-Battigalli-Gamba 2020 ✓.
- 12 Camerer 2003: ? book DOI still not located (Crossref has reviews only).
- 13 Frank 1985: ? book; reviews ✓; Heffetz-Frank 2011 ✓.
- 14 Clark-Oswald 1996: ✓
- 15 Bernheim 1994: ✓ record; ? exact form.
- 16 Bénabou-Tirole 2006: ✎ utility and reputational term added [read, IZA WP].
- 17 Frank 1987/1988: ? originals; reprint and German edition ✓.
- 18 Hirshleifer 1987: ? not in Crossref (edited-volume chapter; plausible, unconfirmable here).
- 19 Bowles-Gintis 2004, 2011; Fehr-Gächter 2002: ✓
- 20 Loewenstein 1994, Golman-Loewenstein 2018 and SSRN: ✓; ✎ utility `u(pi, w)` with attention-weighted valence minus entropy added [read, preprint].
- 21 Golman-Hagmann-Loewenstein 2017: ✓
- 22 Caplin-Leahy 2001: ✓ record; ? formal structure (standard account added); Barigozzi-Levaggi 2010 ✓ (now Crossref-confirmed).
- Closing claims: ✎ "no model composes two drives with a proved result" withdrawn (Charness-Rabin, Falk-Fischbacher, Bénabou-Tirole, Golman-Loewenstein, and BD existence covering any continuous sum); ✎ "no law of motion" scoped to this cluster's game models (habit formation and Kőszegi-Rabin are counterexamples outside it).
- ✗ Nothing removed: no fabricated work found.

**Verdict.** Bibliographically the file is sound: every DOI resolves to the stated work, and the [read] passages on the Battigalli-Dufwenberg line check out. Its weak point was the synthesis, not the citations: the headline "no composed drives with a theorem" contradicted the file's own Bénabou-Tirole entry and ignored Charness-Rabin and Falk-Fischbacher, and the evidence for guilt was presented one-sidedly. Treat formula details tagged [standard account] as provisional; the corrected closing section is usable.
