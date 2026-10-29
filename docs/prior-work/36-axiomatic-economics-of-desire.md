# Prior work 36: axiomatic and formal economics of desire, temptation, craving, habit and needs

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: economics where there are already theorems about wanting. Cross-references: 16 (formal models of motivation), 17 (curiosity, fear, desire), 21 (social preferences, psychological games; Loewenstein's information-gap curiosity is covered there, only the link is noted here), 26 (philosophy of the passions), 15 (taxonomies).

**Method and honesty note.** Read at source this session: Gul & Pesendorfer 2001 (full text via PDF; axioms, Theorem 1, Theorem 2 and the commitment/self-control discussion extracted with pdftotext). Everything else is `[from abstract/standard account]`: search summaries of secondary pages, or background knowledge not re-checked against the primary. Where a formula is given from the standard account it is the field's usual statement and needs checking against the primary before anything is built on it. DOIs were checked against Crossref where marked "verified"; the Crossref API was flaky (many timeouts), so some are marked "not verified".

**Summary.** This is the one cluster in the survey where **proved theorems about wanting exist**. Gul-Pesendorfer is a genuine representation theorem: four axioms on preferences over menus are equivalent to a two-function form, U(A) = max[u+v] − max v. Becker-Murphy has stability and bifurcation results (unstable steady states, cold turkey). Kreps (1979) preceded the menu approach and Dekel-Lipman-Rustichini extend it. The weaknesses are as important as the strengths. (1) Almost every model is single-agent; the exceptions (Bagwell-Bernheim signalling, external habit, Battaglini-Bénabou-Tirole peer self-control) are noted in the closing section. (2) "Drive" appears only as a ranking or a utility function (v), never as a state that depletes and refills, except in habit and addiction models where a stock S does that job. (3) Empirical standing is mixed to poor for the cleanest-looking claims. (4) The useful structural import is not the content but the **form**: desire as a second ranking v whose maximum is subtracted as a cost, desire as a stock, desire as a gap to a reference, desire as a lexicographic ordering. Those are candidate operator shapes.

---

## 1. Gul & Pesendorfer (2001): temptation and self-control

**Citation.** Gul, F. & Pesendorfer, W. (2001). Temptation and Self-Control. *Econometrica* 69(6), 1403-1435. DOI 10.1111/1468-0262.00252 (verified, Crossref). Full text read: https://pages.nyu.edu/debraj/Courses/NewRes05/Papers/GulPesenSelfControl.pdf

**Their vocabulary.** Temptation, self-control, preference for commitment, menu (a set of lotteries chosen in period 1, from which an element is chosen in period 2), commitment ranking (u), temptation ranking (v), cost of self-control.

**Drives/operands.** Menus A, B (compact sets of lotteries over a space Z); elements x, y of a menu. Two real-valued linear functions: u, the commitment utility (what the agent would pick if choosing for a later self with no temptation), and v, the temptation utility (what pulls at the moment of choice). Drive is therefore represented as a second preference ordering over the same options, not as a magnitude of arousal.

**Axioms [read].**
1. Preference relation: complete and transitive on menus.
2. Strong Continuity: the sets {B : B ≽ A} and {B : A ≽ B} are closed.
3. Independence: A ≻ B and α in (0,1) implies αA + (1−α)C ≻ αB + (1−α)C (mixing menus). The paper argues this holds when the agent is indifferent to when uncertainty resolves.
4. Set Betweenness: A ≽ B implies A ≽ A ∪ B ≽ B.

Set Betweenness says adding an option to a menu never helps by more than the option's own worth, and can hurt (a tempting item), and that the union lies between its parts. A standard chooser has A ≽ B implies A ~ A ∪ B; the new freedom is that A ∪ B may be strictly worse than A (the value of commitment).

**Equation (Theorem 1) [read].** ≽ satisfies Axioms 1-4 iff there exist continuous linear U, u, v such that

    U(A) = max_{x∈A} [u(x) + v(x)] − max_{y∈A} v(y),  and U represents ≽.

Reading: the agent picks the best element by u+v, and pays a cost equal to how much better the most tempting element looks, in v-units, than the one she picked. The cost is zero if she picks the v-maximiser. u(x) = U({x}) (value of a singleton menu); v is defined from U on two-element sets {a, b} with U({a}) > U({a,b}) > U({b}) via mixtures, and Lemma 4 shows the v so defined is linear and independent of the choice of a and b. Uniqueness is Theorem 4 (common positive scale for u and v, separate additive constants); u+v is the utility of actual period-2 choice.

**Theorem 2 [read].** Take the representation above. These are equivalent: (i) the agent has self-control at A (defined as: A = B ∪ C with B ≻ A ≻ C); (ii) c_A(v) ∩ c_A(u+v) = ∅ (the most tempting elements are not the ones chosen); (iii) there is B ⊂ A with c_A(u+v) = c_B(u+v) and B ≻ A (some smaller menu is strictly preferred, so commitment has value and the agent resists temptation when forced). Commitment is behaviour in the planning period; self-control is behaviour in the consumption period.

**Further results [read, skimmed; corrected in validation].** Theorem 3: replacing Strong Continuity with Axioms 2a-c (upper semi-continuity, lower vNM continuity, lower singleton continuity) gives either the Theorem 1 form or the "overwhelming temptation" form U(A) = max u(x) subject to v(x) ≥ v(y) for all y ∈ A (the agent lexicographically maximises v first, then u). The paper motivates this as the k → ∞ limit of k·v, noting the limit can fail Strong Continuity. Theorem 4: for a regular self-control preference, (u, v) is unique up to a common positive scale and separate additive constants. Theorems 5-7 work with an extended preference over (menu, choice) pairs: Theorem 5 derives Set Betweenness from it, Theorem 7 shows period-2 choice is max (u+v) for self-control agents and lexicographic v-then-u otherwise. Theorem 8: ≽1 has greater preference for commitment than ≽2 iff u2, v2 are each convex combinations of u1, v1 (up to scale), i.e. the two rankings are closer together for agent 2. Theorem 9: ≽1 has more self-control than ≽2 iff u2+v2 and v2 are each convex combinations of u1+v1 and v1. Greater preference for commitment and more self-control are distinct; one agent can have more of both.

**Theorems or derived predictions.** The pair (u, v) is identified from menu preferences alone. A preference for smaller menus is explained and bounded. A "temptation magnitude" is defined (the gap in v). Self-control exercised costs utility even if the agent resists, which is the behavioural signature separating this model from standard preferences.

**Empirical standing.** Axiomatic result: correct as maths; no replication question. The behavioural content (people pay for commitment, take smaller menus, buy restricted-access devices) has support in field and lab studies of commitment contracts (Ashraf, Karlan & Yin 2006, savings commitment in the Philippines `[standard account]`, not re-checked here), though demand for commitment is smaller than the model predicts for naive agents. The representation is also compatible with several rival stories (planner-doer, Benabou-Pycia `[from abstract/standard account]`, via search) so a menu choice does not discriminate between them. Blunt: it is a representation, not a mechanism; it says nothing about how temptation arises or evolves.

**Operand/operator translation.**
- Operand: a menu (a set of available options) is a natural algebraic object; the algebra has A ∪ B as an operator on menus, with the Set Betweenness inequality as a stated law (A ≽ B implies A ≽ A∪B ≽ B). This is a ready-made partial-order law on a union operator.
- Two orderings (u, v) on the same objects: a drive in the algebra could be a second ranking, and "restraint" is the operator max[u+v] − max v.
- Cost of restraint as a defined quantity: self-control cost = max v − v(chosen).
- Limit k → infinity gives the lexicographic case (no restraint), an algebraic degenerate case.
- Social extension: another person adding or removing options from your menu is an operator on A (cf. 21 on choice sets and other-regarding preference). Not in the paper.

---

## 2. Related menu-preference work

**Kreps (1979).** Kreps, D. (1979). A Representation Theorem for "Preference for Flexibility". *Econometrica* 47(3), 565-577. DOI 10.2307/1910406 (verified, Crossref). `[from abstract/standard account; corrected in validation]`: axioms on preferences over menus (monotonicity, A ⊇ B implies A ≽ B; and Kreps's axiom, A ~ A ∪ B implies A ∪ C ~ A ∪ B ∪ C) give a representation U(A) = Σ_s max_{x∈A} u(x, s), a sum (more generally an increasing aggregate) over subjective states s of the best element in each, not a max over states. The "A ≽ B implies A ~ A ∪ B" axiom is not Kreps's: Gul-Pesendorfer [read] give it as the axiom of a *standard* decision-maker who cares only about the best element, and Set Betweenness weakens that standard axiom. The point: Kreps's agent values extra options (flexibility); Gul-Pesendorfer's can be hurt by them, which violates Kreps's monotonicity.

**Dekel, Lipman & Rustichini (2009).** Temptation-Driven Preferences. *Review of Economic Studies* 76(3), 937-971 (year, volume, pages confirmed against Crossref in validation). DOI 10.1111/j.1467-937X.2009.00560.x (verified, Crossref). Their 2001 paper, Representing Preferences with a Unique Subjective State Space, *Econometrica* 69(4), 891-934, DOI 10.1111/1468-0262.00224 (verified), is the flexibility-side extension of Kreps that Gul-Pesendorfer cite. Shows menu preferences can be represented by a state-dependent temptation (a distribution of v); extends the form to uncertain temptation. Not read.

**Operator note.** Both fix menus as the algebra's carrier and the union as the operator; this is the closest thing in economics to a "calculus of options" and is compatible with an algebra whose operands include opportunity sets.

---

## 3. Fudenberg & Levine (2006): dual-self model

**Citation.** Fudenberg, D. & Levine, D. K. (2006). A Dual-Self Model of Impulse Control. *American Economic Review* 96(5), 1449-1476. DOI 10.1257/aer.96.5.1449 (verified, Crossref). Not read; `[from abstract/standard account]`.

**Their vocabulary.** Long-run self, short-run self (a sequence of myopic selves), self-control cost, willpower.

**Drives/operands.** A long-run self (patient) and a series of short-run selves (myopic, maximising current utility). The long-run self can pay a cost to influence the short-run self's action. The cost of self-control is an increasing function of the divergence between what the short-run self would choose and what the long-run self wants.

**Equations `[standard account]`.** The long-run self can take a self-control action that changes the short-run self's utility, at a cost increasing in the forgone short-run utility; the long-run self's problem is a dynamic programme over wealth/consumption. Exact functional form not checked against the paper.

**Theorems / predictions `[from abstract, via search; corrected in validation]`.** The abstract claims a unified explanation of the apparent time inconsistency behind quasi-hyperbolic discounting and of Rabin's paradox (risk aversion in the small and in the large), the latter via mental accounts / a "pocket cash" limit set in the cool state; it also implies excess delay as in O'Donoghue-Rabin and fits cognitive-load evidence. The base model is consistent with the Gul-Pesendorfer axioms, but the authors argue those axioms must be relaxed to accommodate cognitive load. The Allais paradox is treated in a later paper, Fudenberg & Levine, Risk, Delay, and Convex Self-Control Costs (*AEJ: Microeconomics* 2011; SSRN DOI 10.2139/ssrn.1703603 verified), not in 2006.

**Empirical standing.** The model rationalises known anomalies (mental accounts, small-stakes risk aversion, hyperbolic-looking discounting) but is not a decisive test between itself and quasi-hyperbolic discounting; mostly a different decomposition of the same behaviour. Blunt: wide fit, weak discrimination.

**Translation.** Two agents inside one (planner, doer), with a priced channel from the planner to the doer. That is an **intra-person operator**: pay(c): doer's action. Mirrors the interpersonal operators of the algebra (influence with cost) and gives a way to treat internal conflict as a two-party interaction with the same notation.

---

## 4. Quasi-hyperbolic discounting (beta-delta) and naive/sophisticated agents

**Citations.**
- Strotz, R. H. (1955-56). Myopia and Inconsistency in Dynamic Utility Maximization. *Review of Economic Studies* 23(3), 165-180. DOI 10.2307/2295722 (verified, Crossref, in validation; the 1973 reprint DOI 10.1007/978-1-349-15492-0_10 found earlier is a reprint).
- Phelps, E. S. & Pollak, R. A. (1968). On Second-Best National Saving and Game-Equilibrium Growth. *Review of Economic Studies* 35(2), 185-199. DOI 10.2307/2296547 (verified, Crossref, in validation).
- Laibson, D. (1997). Golden Eggs and Hyperbolic Discounting. *Quarterly Journal of Economics* 112(2), 443-478. DOI 10.1162/003355397555253 (verified, Crossref).
- O'Donoghue, T. & Rabin, M. (1999). Doing It Now or Later. *American Economic Review* 89(1), 103-124. DOI 10.1257/aer.89.1.103 (verified, Crossref).
- O'Donoghue, T. & Rabin, M. (2001). Choice and Procrastination. *Quarterly Journal of Economics* 116(1), 121-160. DOI 10.1162/003355301556365 (verified, Crossref; added in validation as the source of partial naivete).
- Harris, C. & Laibson, D. (2001). Dynamic Choices of Hyperbolic Consumers. *Econometrica* 69(4), 935-957. DOI 10.1111/1468-0262.00225 (verified; added in validation).
- Thaler, R. H. & Shefrin, H. M. (1981). An Economic Theory of Self-Control. *Journal of Political Economy* 89(2), 392-406. DOI 10.1086/260971 (verified, Crossref, in validation); NBER working paper w0208 (1977) is the earlier version.
None read; all `[from abstract/standard account]`.

**Their vocabulary.** Present bias, time inconsistency, beta-delta preferences, naive, sophisticated, partially naive, procrastination, preproperation, commitment.

**Equation `[standard account]`.** Utility at time t: U_t = u_t + beta·sum_{k≥1} delta^k u_{t+k}, with 0 < beta ≤ 1 (present bias), delta in (0,1]. beta = 1 gives exponential discounting. Strotz showed that unless the discount function is exponential, plans made now will not be followed later, and proposed precommitment and "consistent planning" as responses. The two-parameter (beta, delta) form is due to Phelps & Pollak (1968), for successive *generations* saving for one another; Laibson (1997) reinterpreted it as one person's successive selves and named it quasi-hyperbolic. Naive agents believe their future selves will act on current preferences (they believe beta_future = 1); sophisticated agents predict the true future behaviour; partial naivete (believed beta-hat between beta and 1) is O'Donoghue & Rabin (2001), not the 1999 paper.

**Theorems / derived predictions `[standard account]`.**
- Sophisticated beta-delta agents have an equilibrium of the multi-self game (Laibson 1997: the "Golden Eggs" result, a hyperbolic consumer undersaves and values illiquid assets as commitment devices). Pathologies of the equilibrium consumption function (discontinuities, non-monotonicity) are analysed in Harris & Laibson (2001), not attributed here to the 1997 paper.
- O'Donoghue & Rabin (1999): for immediate costs, naive agents procrastinate more than sophisticated ones and can delay indefinitely; for immediate rewards, sophisticated agents may act too soon (preproperation); full results are stated as propositions about the timing of completing a task with a deadline.

**Empirical standing.** Present bias has solid lab support in money-now-versus-later choices, but the magnitude of beta is unstable across studies and across domains (money versus real effort versus food); a large literature (Frederick, Loewenstein & O'Donoghue 2002 review `[standard account, not read]`) found wide variation in estimated discount rates. Field evidence of naivete (gym membership, Della Vigna & Malmendier 2006 `[standard account, not verified]`) exists but is contested; Andreoni & Sprenger (2012) `[standard account]` found much of the money-time evidence is confounded by risk and convex utility. Blunt: present bias exists as a pattern, the specific beta-delta form is a convenient approximation.

**Translation.** Time-inconsistency can be represented as a pair (self_now, self_later) with a relation between them; sophisticated and naive are two different operators for forecasting the other self (identity versus true best response). This gives a **forecast operator** in the algebra: the same kind of object as one person's model of another's behaviour. Present bias beta is a scalar parameter that rescales drives that pay off immediately.

---

## 5. Rational addiction and cue-triggered addiction

### 5.1 Becker & Murphy (1988)

**Citation.** Becker, G. S. & Murphy, K. M. (1988). A Theory of Rational Addiction. *Journal of Political Economy* 96(4), 675-700. DOI 10.1086/261558 (verified, Crossref). Not read; `[from abstract/standard account]` via search summaries.

**Their vocabulary.** Consumption capital, adjacent complementarity, tolerance, reinforcement, withdrawal, cold turkey, binges, rational (consistent plan to maximise utility over time).

**Drives/operands.** A stock S (consumption capital) built by past consumption c of an addictive good and depreciating at rate delta; instantaneous utility U(c, S, y) where y is a non-addictive good. Addiction is **adjacent complementarity**: past consumption raises the marginal utility of current consumption, U_cS > 0 `[standard account]`.

**Equations `[standard account]`.** dS/dt = c − delta·S; the consumer maximises the integral of e^{-rt}·U(c, S, y) subject to the budget and the law of motion. Stability of steady states is determined by the sign of the second-order derivative conditions; strong complementarity produces more than one steady state, one unstable.

**Theorems or derived predictions.** The search summary confirms: strong complementarity makes some steady states unstable (a small deviation drives consumption sharply up or down), and the theory implies "cold turkey" quitting for strong addictions and binges. Permanent price changes have larger effects than temporary ones. Cross-price effects between periods are negative (consumption in different periods are complements). These are propositions about a dynamic optimisation, with proofs in the paper (I did not read them).

**Empirical standing.** Becker, Grossman & Murphy (1994) found cigarette consumption responds to announced future prices, taken as support; Gruber & Kőszegi (2001), QJE 116(4), 1261-1303, found the same using pre-announced tax increases, but argued the forward-looking behaviour is equally consistent with time-inconsistent (hyperbolic) preferences, which carry very different welfare and tax implications; DOI 10.1162/003355301753265570 (verified, Crossref, in validation: Is Addiction "Rational"? Theory and Evidence). Critics: the model is nearly unfalsifiable because any consumption path can be rationalised by suitable preferences; forward-looking behaviour in the data does not show the person is planning optimally, only that the future enters. Many addicts report regret and wanting-without-liking, which the model has no place for (see Berridge in file 22). Blunt: the prediction of forward-looking consumption holds; the claim that addicts are rational does not follow from it.

**Translation.** The pair (c, S) with dS/dt = c − delta·S is a clean **drive-as-stock** law: consumption builds the stock, the stock raises the marginal pull of consumption. This is the positive-feedback loop that also appears in file 16's models. Unstable fixed points give a **threshold/bifurcation theorem** the algebra can adopt: a region of state space where small changes tip into escalation or abstention. It is also single-agent, with no social feedback.

### 5.2 Bernheim & Rangel (2004)

**Citation.** Bernheim, B. D. & Rangel, A. (2004). Addiction and Cue-Triggered Decision Processes. *American Economic Review* 94(5), 1558-1590. DOI 10.1257/0002828043052222 (verified, Crossref). Not read; `[from abstract/standard account]`.

**Their vocabulary.** Hot mode, cold mode, cue, mistaken use, environmental cues, policy (taxes, bans, treatment, public education).

**Structure `[standard account]`.** The brain operates in one of two modes. In the cold mode the person maximises true utility. In the hot mode, triggered by a cue (stimulus associated with past use), the person uses the substance regardless of his preferences. The probability of entering hot mode is an increasing function of the cue's presence and of past use; the person in cold mode takes costly actions to avoid cues. Choice is **mistaken** when it is made in hot mode and is not what cold-mode preference would choose.

**Derived predictions `[from abstract/standard account]`.** Optimal policy differs from rational addiction: the normative case for restricting exposure to cues; the model explains relapse after long abstention (a cue triggers hot mode after the stock has decayed), which Becker-Murphy cannot; and why people avoid cues when sophisticated.

**Empirical standing.** Qualitatively consistent with cue-induced relapse and craving (Robinson & Berridge incentive-sensitisation work, file 22), but not tested as a structural model in the way Becker-Murphy has been. Blunt: more plausible than rational addiction, less quantified.

**Translation.** A **cue-gated mode switch** with a probability that depends on environment and history: an operator that takes (state, environment) to (mode). The environment includes other people, so social cues are natural inputs. This is a better template for the algebra's "trigger" than a continuous utility.

### 5.3 Laibson (2001): cue theory of consumption

**Citation.** Laibson, D. (2001). A Cue-Theory of Consumption. *Quarterly Journal of Economics* 116(1), 81-119. DOI 10.1162/003355301556356 (verified, Crossref). Not read; `[from abstract/standard account]`.

**Structure `[standard account]`.** Past consumption of a good is encoded as a set of cues; encountering a cue raises the **hedonic level** of the good (desire) and the agent, who knows the dynamic, can avoid cues or choose consumption knowing future desire will follow. Desire is a function of the cue, not of the stock directly, and the agent's intertemporal problem is a dynamic programme with endogenous preferences. Result: consumption is driven by the (visible) cues; the agent sometimes overconsumes now to condition himself.

**Empirical standing.** Qualitative; supports advertising, display and exposure effects; not estimated as a structural model.

**Translation.** Desire is a **function of a context variable** (cue) as well as the history. An algebra whose primitives include contexts and a trigger operator trigger(cue, history) gives a state-to-drive map.

---

## 6. Habit formation

**Citations.**
- Pollak, R. A. (1970). Habit Formation and Dynamic Demand Functions. *Journal of Political Economy* 78(4), 745-763. DOI 10.1086/259667 (verified, Crossref).
- Constantinides, G. M. (1990). Habit Formation: A Resolution of the Equity Premium Puzzle. *Journal of Political Economy* 98(3), 519-543. DOI 10.1086/261693 (verified, Crossref).
Neither read; `[from abstract/standard account]`.

**Equation `[standard account]`.** Utility depends on consumption relative to a habit stock: u(c_t − h·X_t) (subtractive, Constantinides) or u(c_t / X_t) (ratio; Abel 1990, Asset Prices under Habit Formation and Catching Up with the Joneses, *AER P&P* 80(2), 38-42, NBER w3279 DOI 10.3386/w3279 verified; Abel's habit can be the person's own past consumption or others' consumption, the "Joneses"), where X_t = a weighted average of past consumption, X_{t+1} = (1−delta)X_t + delta·c_t. Pollak: preferences at t depend on past consumption through a state; with habit the demand function is dynamic and long-run elasticities differ from short-run ones. Constantinides: the habit makes marginal utility of consumption in bad times very high, so risk aversion is effectively large with modest curvature; this resolves the equity premium puzzle.

**Theorems / predictions.** Habit models give slow adjustment of consumption, long-run versus short-run elasticity gaps, and, in asset pricing, a high effective relative risk aversion.

**Empirical standing.** Habit formation is a standard and quite successful ingredient in macro models (consumption smoothness, hump-shaped responses) and in asset pricing (Campbell-Cochrane 1999 builds on it `[standard account, not verified here]`), though identification against other sources of persistence is hard. Blunt: well used, not unique; often a convenience parameter.

**Translation.** The reference stock X moves toward consumption; the felt value is consumption **minus or divided by** that stock. This is the same state-gap form as drive reduction (file 16) and as expectation-based reference dependence (below), and a common form is: felt = f(current) − g(stock), with stock updated by a leaky integrator. A reusable operator.

---

## 7. Reference-dependent preferences and disappointment

**Citations.**
- Kőszegi, B. & Rabin, M. (2006). A Model of Reference-Dependent Preferences. *Quarterly Journal of Economics* 121(4), 1133-1165. DOI 10.1093/qje/121.4.1133 (verified, Crossref). Working paper: https://www.wiwi.uni-bonn.de/koszegi/refdep.pdf.
- Kőszegi, B. & Rabin, M. (2007). Reference-Dependent Risk Attitudes. *American Economic Review* 97(4), 1047-1073. DOI 10.1257/aer.97.4.1047 (verified, Crossref).
- Kahneman & Tversky (1979) prospect theory is cross-referenced in 16; not repeated.
Search summaries only; `[from abstract/standard account]`.

**Their vocabulary.** Reference point as rational expectations, consumption utility, gain-loss utility, loss aversion lambda, personal equilibrium (PE), preferred personal equilibrium (PPE), choice-acclimating personal equilibrium (CPE, in the 2007 paper), attachment effect.

**Equation.** Per the search result (a 2026 arXiv restatement and a Toronto conference summary, both secondary): U(c | r) = m(c) + n(c | r), where m is consumption utility and n gain-loss utility; gains weighted by eta, losses by eta·lambda with lambda > 1. Over lotteries, the 2006 form sums consumption utility weighted by probabilities plus a double sum over pairs of outcomes weighted by p and r with a gain-loss function mu applied to differences in consumption utility. Exact notation not checked against the primary.

**Theorems or derived predictions.** The reference point is the agent's recent beliefs about outcomes, so what an agent plans or expects sets how it feels about what arrives: an expected loss hurts less than a surprising one but still hurts; the "attachment effect" is that expecting to own something raises the pain of not getting it. The paper characterises personal equilibria (consistent plans given beliefs) and shows existence in the stated setting `[from abstract]`. Masatlioglu & Raymond (2016), A Behavioral Analysis of Stochastic Reference Dependence, *AER* 106(9), 2760-2782, DOI 10.1257/aer.20140973 (verified in validation): linear CPE lies in the intersection of quadratic utility and rank-dependent utility (as cited in the search result; not read).

**Empirical standing.** Evidence supports reference dependence (endowment effect; Heffetz & List 2014 and Plott & Zeiler 2005 argued the endowment effect partly depends on procedure `[standard account, not verified]`; loss aversion magnitude varies, and Gal & Rucker 2018 argued that loss aversion is overstated `[standard account, not verified]`). Expectations as the reference point has evidence from taxi labour supply and marathon finish-time bunching (Allen et al. 2017, `[standard account]`) but Camerer et al. 1997's cabdriver result has been challenged by later data. Blunt: reference dependence is real; the specific expectations-based form is plausible but not settled; loss aversion lambda about 2 is a headline figure with a very wide range.

**Translation.** Disappointment is a **signed difference between the received outcome and an expectation**, weighted asymmetrically. For the algebra: an expectation is an operand (a belief about one's own future state) and the emotion is gain-loss(received − expected). The same form drives fear (anticipated loss) and desire (anticipated gain) under one operator, with other people's promises or threats setting the reference point (cf. 21's psychological games, where beliefs enter payoffs).

---

## 8. Lexicographic preferences and hierarchy of needs

**Citations.**
- Georgescu-Roegen, N. (1954). Choice, Expectations and Measurability. *Quarterly Journal of Economics* 68(4), 503-534. DOI 10.2307/1881875 (verified, Crossref). Not read.
- Maslow, A. H. (1943). A Theory of Human Motivation. *Psychological Review* 50(4), 370-396. DOI 10.1037/h0054346 (verified, Crossref). Not read; the Crossref hit for a loose query was the 1958 chapter, the 1943 DOI was confirmed separately.
- Lancaster, K. J. (1966). A New Approach to Consumer Theory. *Journal of Political Economy* 74(2), 132-157. DOI 10.1086/259131 (verified, Crossref). Not read.
All `[from abstract/standard account]`.

**Vocabulary.** Lexicographic ordering (dictionary order), threshold, satiation, hierarchy of needs, characteristics.

**Content `[standard account]`.**
- Georgescu-Roegen 1954: argued that needs are not all commensurable and that a lexicographic ordering is realistic; a lower-ranked want counts only when higher wants are satisfied. Mathematical statement: bundle x ≻ y iff at the first coordinate where they differ (in priority order), x is greater.
- Debreu, G. (1954). Representation of a Preference Ordering by a Numerical Function. In R. M. Thrall, C. H. Coombs & R. L. Davis (eds), *Decision Processes*, Wiley, 159-165 (reprinted in Debreu, *Mathematical Economics*, CUP 1983, DOI 10.1017/CCOL052123736X.007, verified). This is where the lexicographic order on R^2 is given as the example of a complete, transitive preference with **no** real-valued representation, alongside Debreu's sufficient conditions (continuity) for one to exist. The result is credited to Debreu, not Georgescu-Roegen. Standard argument: each x gives a non-degenerate interval (U(x,0), U(x,1)), these are disjoint for distinct x, and there are uncountably many, contradicting one rational per interval `[standard account]`.
- Maslow 1943: five levels (physiological, safety, love/belonging, esteem, self-actualisation), with prepotency: a higher need emerges when the lower one is "reasonably satisfied". Maslow himself said satisfaction is relative, not all-or-none, and ordering is not rigid (the paper contains explicit caveats `[standard account]`). Reading Maslow as lexicographic utility is a later gloss, not Maslow's statement.
- Lancaster 1966: goods are not directly valued; they provide **characteristics** (vectors), and utility is defined on characteristics through a consumption technology (a matrix B mapping goods to characteristics, z = Bx).

**Theorems.** No real-valued utility represents strict lexicographic preferences on R^n (n ≥ 2) (Debreu 1954): a proved negative result and a reason a single scalar "total drive" cannot always exist. Lancaster derives that new goods can be valued by their characteristics and that efficient bundles lie on a frontier of the characteristics space.

**Empirical standing.** Maslow's strict ordering is not supported (Wahba & Bridwell 1976 review found little evidence for the hierarchy `[standard account, not verified]`; Tay & Diener 2011, Gallup World Poll across 123 countries, found that needs are broadly universal but fulfilment of different needs is largely independent of order `[standard account, not verified]`). Lexicographic choice appears in experiments on sacred or protected values (Tetlock) and in a minority of subjects, but strict lexicographic behaviour is rare for ordinary goods. Blunt: the hierarchy as a strict law is false; as soft priority (large weights that fall off with satisfaction) it is defensible, which matches the project instruction that rules be soft settings with slack.

**Translation.** Two forms for the algebra: (a) strict priority (lexicographic) as an exact limit; (b) priority as a weight that declines with satisfaction, which is the same shape as Gul-Pesendorfer's overwhelming-temptation limit (k → infinity of v). Lancaster gives a two-layer structure, drives (characteristics) over objects, with a **matrix operator** from options to drive-contributions: z = Bx. That is a linear map from acts to drive changes, a candidate core form.

---

## 9. Veblen and signalling models

**Citation.** Bagwell, L. S. & Bernheim, B. D. (1996). Veblen Effects in a Theory of Conspicuous Consumption. *American Economic Review* 86(3), 349-373 (bibliographic details re-confirmed in validation via IDEAS and Bernheim's Stanford page; the 1996 AER issue has no Crossref DOI, JSTOR only, so no DOI is given). Working paper: Bagwell & Bernheim (1992), Conspicuous Consumption, Pure Profits, and the Luxury Tax, NBER w4163, DOI 10.3386/w4163 (verified, Crossref). Veblen, T. (1899). *The Theory of the Leisure Class* (book; no DOI relied on). Abstract-level only.

**Content (confirmed from the search abstracts).** Veblen effects (in their definition, willingness to pay a higher price for a functionally equivalent good, not literally upward-sloping demand) cannot ordinarily arise when preferences satisfy a **single-crossing property** in a signalling game; they can emerge when it fails. In the model, "budget" brands sell at marginal cost and "luxury" brands, though not intrinsically superior, sell at higher prices to consumers advertising wealth, earning strictly positive profit. The working-paper version adds that a properly designed luxury tax is a non-distortionary tax on pure profits.

**Theorems.** The proof structure: in a separating equilibrium, price conveys wealth if the cost of a high price is lower for the wealthy; with a failure of single crossing, Veblen effects (a premium paid for a functionally equivalent luxury brand) can occur in equilibrium. Veblen effects are a theorem about a **signalling** equilibrium, not an assumed taste.

**Empirical standing.** Conspicuous consumption exists (Charles, Hurst & Roussanov 2009 found minority groups spend more on visible goods `[standard account, not verified]`); the specific model's predictions about luxury brands pricing are hard to test and the paper is a theory paper. Blunt: a good existence result for status goods, thin on quantitative validation.

**Translation.** Desire for status is desire about **what others infer**; the payoff depends on observers' beliefs (as in psychological games, 21). The operator is display(act) with an observer's inference as the reward, giving the algebra a social drive whose operand is another person's belief about me.

---

## 10. Scitovsky's *The Joyless Economy*

**Citation.** Scitovsky, T. (1976). *The Joyless Economy: An Inquiry into Human Satisfaction and Consumer Dissatisfaction*. Oxford University Press (revised 1992 as *The Joyless Economy: The Psychology of Human Satisfaction*). No DOI relied on. **Not read, not searched this session; `[standard account]` only.**

**Content `[standard account]`.** Draws on Berlyne and Hebb: organisms need an **optimal level of arousal**, and both too little (boredom) and too much (stress) are unpleasant. Distinguishes **comfort** (relief of discomfort, drive reduction) from **pleasure** (the rise in arousal, novelty, stimulation); satisfaction from pleasure is transient and requires change. Argues that affluent consumption over-supplies comfort and under-supplies stimulation, and that skills (acquired tastes) are needed to enjoy stimulation.

**Theorems.** None. It is a verbal argument that informed later work on novelty and boredom.

**Empirical standing.** The inverted-U between arousal/novelty and liking (Berlyne) has mixed support (Wundt curve; see file 16/17 on Berlyne); the comfort/pleasure split is similar to the wanting/liking split (file 22) but not identical. Blunt: a framing, not a model.

**Translation.** Two kinds of satisfaction: one removing a deficit (drive reduction), one raising arousal toward an optimum. In the algebra a drive could have **an optimum level rather than a zero** (a target set point with penalties on both sides), which differs from Hull's reduction to zero.

---

## 11. Loewenstein: visceral factors, hot-cold empathy gaps, curiosity

**Citations.**
- Loewenstein, G. (1996). Out of Control: Visceral Influences on Behavior. *Organizational Behavior and Human Decision Processes* 65(3), 272-292. DOI 10.1006/obhd.1996.0028 (verified, Crossref). Not read; `[from abstract/standard account]`.
- Loewenstein, G. (1994). The Psychology of Curiosity: A Review and Reinterpretation. *Psychological Bulletin* 116(1), 75-98. DOI 10.1037/0033-2909.116.1.75 (verified, Crossref). Information-gap theory is treated in file 21; only the link is noted.
- Loewenstein, G. & O'Donoghue, T. (2004). Animal Spirits: Affective and Deliberative Processes in Economic Behavior. SSRN 539843, DOI 10.2139/ssrn.539843 (verified, Crossref; a working paper).
- Caplin, A. & Leahy, J. (2001). Psychological Expected Utility Theory and Anticipatory Feelings. *QJE* 116(1), 55-79. DOI 10.1162/003355301556347 (verified, Crossref). `[from abstract/standard account]`.

**Content `[standard account]`.** Visceral factors (hunger, thirst, sexual arousal, pain, emotions, cravings) have these properties: they crowd out other goals as intensity rises, they narrow attention to the present and to the self, they are underestimated when in a cold state and when in the hot state future states are discounted (**hot-cold empathy gap**), and they are hard to describe. Choice in Loewenstein's account is a mix of deliberative and visceral systems, not a single utility maximisation. In Loewenstein & O'Donoghue's dual-system model the behaviour is a weighted mix of a deliberative and an affective system, with the weight shifting to the affective system when arousal is high and self-control effort is costly (a form close to Fudenberg-Levine). Caplin-Leahy add anticipatory feelings (utility from beliefs) to expected utility, a formal bridge to psychological games.

**Theorems / predictions.** Qualitative propositions. No representation theorem.

**Empirical standing.** The empathy-gap effect has direct experimental support: Read & Van Leeuwen (1998) found hungry people choose unhealthy snacks for later; Van Boven & Loewenstein (2003) found people underpredict the effect of states like thirst after exercise `[standard account, not verified here]`. Sexual-arousal studies (Ariely & Loewenstein 2006) are lab studies with the usual limits on generalisation. Blunt: the effect that being in state X changes one's forecast of state not-X is one of the more robust findings in this cluster, but the effect sizes vary and replication reports on related priming and ego-depletion work (Hagger et al. 2016 multi-lab failure to replicate ego depletion, `[standard account, not verified]`) warn against assuming a depleting willpower resource.

**Translation.** A state variable (arousal intensity) that **reweights** the objective (shifting weight toward immediate drives) and **biases forecasts** of other states. For a group: a person in a hot state mispredicts another's cold state, and vice versa, giving a prediction error operator between persons (empathy gap) that is the same form as the sophisticated/naive forecast operator in section 4.

---

## 12. Composing several drives into one value: multi-attribute and multi-objective views

**Citations.**
- Keeney, R. L. & Raiffa, H. (1976). *Decisions with Multiple Objectives: Preferences and Value Tradeoffs*. Wiley (reissued Cambridge University Press 1993). No DOI relied on. Not read this session; `[standard account]`.
- Pareto, V. (1896-97, 1906). Pareto efficiency, as multi-objective optimisation; `[standard account]`.

**Content `[standard account]`.** Keeney-Raiffa: conditions under which a multi-attribute utility decomposes. **Additive** form U(x) = sum k_i·u_i(x_i) holds iff attributes are mutually preferentially independent (for ordinal value) and additively independent (for lotteries); **multiplicative** form 1 + kU = prod(1 + k·k_i·u_i) holds under utility independence, with the scaling constant k fixed by the condition sum k_i = 1 when additive and otherwise solving 1 + k = prod(1 + k·k_i). The form depends on stated independence conditions that can be tested, so the choice between additive, multiplicative and non-decomposable is an empirical question. Pareto view: where drives conflict without a common scale, the object is the **set of non-dominated points** (the Pareto frontier); a scalarisation (weights) picks one point, and each weight vector corresponds to a supporting hyperplane on the convex part of the frontier.

**Theorems.** Keeney-Raiffa representation theorems (additive, multiplicative) under independence conditions; the Pareto frontier is characterised by weighted-sum optimisation only on convex regions (non-convex frontier points cannot be found by any weighting; a standard multi-objective result).

**Empirical standing.** Widely used in decision analysis; the independence assumptions are often violated for emotional attributes. For competing drives, weights are not stable across states (hot-cold gap, section 11).

**Translation.** This is the algebra's direct answer to "how do drives combine": additive, multiplicative (interaction through k), lexicographic (priority), or Pareto (no total order). The conditions tell you which law to adopt for which drives, and the lexicographic and Gul-Pesendorfer forms (sections 1, 8) appear as degenerate or asymmetric special cases. Weights that depend on state are the Loewenstein shift.

---

## Cross-cutting: how this cluster combines drives

| Form | Source | Law |
|---|---|---|
| Second ranking with cost of restraint | Gul-Pesendorfer | U(A) = max[u+v] − max v |
| Two selves, priced control | Fudenberg-Levine | long-run self pays to constrain short-run |
| Present-weighted sum | beta-delta | u_t + beta·sum delta^k u_{t+k} |
| Stock that feeds its own marginal utility | Becker-Murphy | dS/dt = c − delta·S, U_cS > 0 |
| Cue-gated mode switch | Bernheim-Rangel, Laibson | mode = f(cue, history) |
| Gap to a moving stock | habit models | u(c − hX) |
| Gap to an expectation, asymmetric | Kőszegi-Rabin | m(c) + n(c|r) |
| Strict priority | Georgescu-Roegen, Maslow (as read); non-representability Debreu 1954 | lexicographic; no scalar utility |
| Linear map from acts to characteristics | Lancaster | z = Bx |
| Additive/multiplicative composition | Keeney-Raiffa | conditions on independence |

---

## What exists versus what does not

**Exists.**
- Proved theorems about desire versus restraint (Gul-Pesendorfer Theorems 1-2, read): a menu-based algebra with a union operator and an order law.
- Proved dynamic results on addiction (stability, bifurcation) in single-agent control form.
- Standard decomposition tools for several drives (Keeney-Raiffa; lexicographic impossibility result).
- Reasonable evidence for present bias, reference dependence, cue-triggered relapse, empathy gaps, habit persistence.

**Does not exist (or I did not find).** *Corrected in validation: the claim that this cluster has no multi-person theorems is too strong.* Bagwell-Bernheim (section 9) is itself a multi-person equilibrium theorem about a desire (status); external-habit models (Abel 1990, "catching up with the Joneses"; Campbell-Cochrane 1999) put other people's consumption inside one's own utility with formal asset-pricing results; and Battaglini, Bénabou & Tirole (2005), Self-Control in Peer Groups, *Journal of Economic Theory* 123(2), 105-134, DOI 10.1016/j.jet.2005.04.001 (verified), prove equilibrium results for present-biased agents who learn about their own willpower from peers' behaviour (good and bad peer effects). What is true is narrower:
- No **axiomatic** (representation-theorem) multi-person version of temptation or addiction found. Peer effects in addiction otherwise exist mostly as applied work (Christakis & Fowler on smoking networks, `[standard account]`; contested on identification).
- A theorem linking menu preference (Gul-Pesendorfer) to a social operator (someone else editing your menu). Natural but not found.
- A state-dependent theory where drive magnitudes rise and fall (hunger-like cycles) inside the axiomatic framework: temptation is static (a ranking), addiction is a stock; neither has satiation and recovery dynamics of the Hull or Lorenz kind (file 16).
- A validated unit or scale for temptation strength: v is identified only up to affine transformation.
- Replicated willpower-as-resource support; the dual-self cost is a modelling device.
- A strict Maslow hierarchy as an empirical law.

## Unconfirmed

- Fudenberg-Levine 2006: equations, exact theorem statements, and the equivalence with Gul-Pesendorfer: from memory.
- Laibson 1997 and O'Donoghue-Rabin 1999: results are the standard account; not read.
- Becker-Murphy: stability conditions and the exact form of the utility; only search summaries seen.
- Bernheim-Rangel 2004 and Laibson 2001: structural details are from memory.
- Kőszegi-Rabin 2006: the lottery form and equilibrium existence claims; notation is from a secondary restatement.
- Georgescu-Roegen 1954 and Maslow 1943: content is the standard account; Maslow's own caveats about non-rigid ordering are from memory.
- Scitovsky: entirely from memory; no search done.
- Keeney-Raiffa theorem statements and the multiplicative equation: from memory.
- All empirical items marked "not verified": Ashraf-Karlan-Yin, DellaVigna-Malmendier, Andreoni-Sprenger, Tay-Diener, Wahba-Bridwell, Read-Van Leeuwen, Van Boven-Loewenstein, Ariely-Loewenstein, Hagger et al., Gal-Rucker, Heffetz-List, Charles-Hurst-Roussanov, Allen et al., Camerer et al. 1997, Campbell-Cochrane, Christakis-Fowler.
- Gul-Pesendorfer 2004 (Self-Control and the Theory of Consumption, *Econometrica* 72(1), 119-158, DOI 10.1111/j.1468-0262.2004.00480.x verified) and Noor-Takeoka (convex cost of self-control) were found but not covered beyond the search note that they relax Independence; they extend the continuous-time and cost-function structure and are worth a later read.

## Missing important work (added in validation)

- Battaglini, Bénabou & Tirole (2005), Self-Control in Peer Groups, *JET* 123(2), 105-134, DOI 10.1016/j.jet.2005.04.001: the closest thing to a multi-person theory of temptation with theorems; directly relevant to the social extension.
- Bénabou & Tirole (2004), Willpower and Personal Rules, *JPE* 112(4), 848-886, DOI 10.1086/421167: self-control as self-signalling, personal rules as equilibria of an intrapersonal game.
- Abel (1990) and Campbell & Cochrane (1999): external habit, desire indexed to others' consumption.
- Debreu (1954): the source of the lexicographic non-representability result (now cited in section 8).
- O'Donoghue & Rabin (2001) and Harris & Laibson (2001): now cited in section 4.
- Pollak (1968), Consistent Planning, *RES* 35(2), 201-208 (not DOI-checked here): the correction to Strotz's consistent-planning solution, worth adding when section 4 is read at source.
- Dekel, Lipman & Rustichini (2001) and Noor & Takeoka (convex self-control cost): menu-preference extensions (2001 now cited in section 2).

## Validation log (2026-10-29)

Method: every DOI resolved against the Crossref API; Gul-Pesendorfer 2001 re-read from the NYU PDF (axioms, Theorems 1-4, 8, 9 checked against the text); other works checked by Crossref metadata and abstracts via search. Formal claims for unread works remain tagged as standard account.

- Gul & Pesendorfer 2001 — ✎ corrected: Theorem 8 is comparative preference for commitment, not uniqueness (that is Theorem 4); Theorem 9 statement completed; Theorem 3's actual form given; Theorem 2's self-control definition added; axioms, Theorem 1 and Theorem 2 otherwise accurate [read].
- Kreps 1979 — ✎ corrected: the axiom "A ≽ B ⇒ A ~ A∪B" is GP's standard-agent axiom, not Kreps's; representation is a sum over states, not a max.
- Dekel, Lipman & Rustichini 2009 — ✓ (year/volume/pages now confirmed); DLR 2001 added.
- Fudenberg & Levine 2006 — ✎ corrected: Allais explanation belongs to their 2011 paper; "money illusion" and the windfall-MPC claim removed; abstract claims (quasi-hyperbolic time inconsistency, Rabin paradox via pocket cash, cognitive load relaxing GP axioms) substituted.
- Strotz 1955-56 — ✎ DOI resolved, 10.2307/2295722.
- Phelps & Pollak 1968 — ✎ DOI resolved, 10.2307/2296547; credited as originators of the beta-delta form (intergenerational), Laibson as the intrapersonal reinterpretation.
- Laibson 1997 — ✎ corrected: consumption-function discontinuities moved to Harris & Laibson 2001.
- O'Donoghue & Rabin 1999 — ✎ corrected: partial naivete is from their 2001 QJE paper (added).
- Thaler & Shefrin 1981 — ✎ journal DOI resolved, 10.1086/260971.
- Becker & Murphy 1988 — ✓ citation; dynamics remain standard account.
- Gruber & Kőszegi 2001 — ✎ DOI 10.1162/003355301753265570 verified; their conclusion restated (data equally consistent with time inconsistency, not "better explained").
- Bernheim & Rangel 2004 — ✓ citation; structure standard account.
- Laibson 2001 cue theory — ✓.
- Pollak 1970; Constantinides 1990 — ✓; ratio form now credited to Abel 1990 (added).
- Kőszegi & Rabin 2006, 2007 — ✓ citations; equation notation still secondary.
- Masatlioglu & Raymond 2016 — ✎ volume/pages/DOI added; "pessimistic" dropped as unconfirmed.
- Georgescu-Roegen 1954 — ✎ corrected: non-representability of lexicographic order credited to Debreu 1954 (added).
- Maslow 1943; Lancaster 1966 — ✓.
- Bagwell & Bernheim 1996 — ✎ confirmed (AER 86(3) 349-373, no Crossref DOI exists); "Veblen effect" redefined as the authors define it (premium for a functionally equivalent good), not upward-sloping demand.
- Veblen 1899; Scitovsky 1976 — ✓ (bibliographic; content standard account).
- Loewenstein 1996, 1994; Loewenstein & O'Donoghue 2004; Caplin & Leahy 2001 — ✓ citations; content standard account.
- Keeney & Raiffa 1976 — ✓ (book; additive/multiplicative forms match the standard statement).
- Empirical side citations (Ashraf-Karlan-Yin, DellaVigna-Malmendier, Andreoni-Sprenger, etc.) — ? not individually checked in validation; left in Unconfirmed.
- Closing claim "no social or multi-person theorems" — ✎ corrected: false as stated (Bagwell-Bernheim in this very file, external habit, Battaglini-Bénabou-Tirole 2005); narrowed to "no axiomatic multi-person theory of temptation".
- Fabrications found: none (✗ 0).

**Verdict.** Bibliographically sound: every cited paper exists with the stated authors, and all three "unverified" DOIs resolve to the right papers. The weak points were attribution and theorem numbering — Gul-Pesendorfer's Theorems 8/9 were misdescribed despite the [read] tag, Kreps's axiom was misstated, the lexicographic impossibility was left uncredited (Debreu), and partial naivete and the Allais result were credited to the wrong papers. The closing "no multi-person theorems" claim contradicted the file's own section 9 and should not be relied on.

## Licences of quoted and transcribed material (2026-10-30)

No passage in this file is a long quotation, a transcribed table or a dataset extract. The table in the cross-cutting section is the author's own synthesis. Audit verdicts were "check" only; no text was changed.

- **Gul & Pesendorfer (2001), Econometrica 69(6), 1403-1435.** Licence: not determined; publisher copyright (Econometric Society) presumed. Use: restated equations (Theorem 1 representation, Theorem 2 equivalences, axioms) and paraphrase of the theorems. Check before open-sourcing: the lead-in to Theorem 1 ("satisfies Axioms 1-4 iff there exist continuous linear U, u, v such that") tracks the standard wording closely; confirm it is our own phrasing. The surrounding explanation is paraphrase.
- **Gul & Pesendorfer full-text link (pages.nyu.edu course-page PDF).** Licence: not determined; publisher copyright presumed, and the authorisation of the hosted copy is unknown. Use: a link only; nothing reproduced. The Econometrica DOI (10.1111/1468-0262.00252) is the primary reference; the hosted copy should not be relied on as a licensed source.
- **All other works cited (Kreps 1979, Fudenberg & Levine 2006, Becker & Murphy 1988, Bernheim & Rangel 2004, Laibson, Scitovsky, Loewenstein, etc.).** Licence: not determined; publisher copyright presumed. Use: citations, facts and restated or described results only; no quotation or transcription.
