# Prior work 73: does any model run the chain threat -> (conformity, noise) -> convention?

Direction: D357 (kind: model). Date: 2026-10-29. Survey for the social-algebra strand. From: 25.

**Question (research map).** Does any single model run the chain: threat sets conformity and noise, which then selects a convention? If none does, specify it.

**Method and honesty note.** Read at source this session, full text via `pdftotext`: Roos, Gelfand, Nau & Lun 2015 (author PDF, cs.umd.edu/~nau/papers/roos2015societal.pdf); De, Nau & Gelfand 2017 (arXiv 1704.04720); De, Nau, Pan & Gelfand 2018 (arXiv 1804.07406). Every equation of theirs below is transcribed from those texts and tagged **[read]**; I re-derived De 2017 eq. (2), (4) and De 2018 eq. (6), (7), (8) by hand and they check. **Not read:** Pan, Gelfand & Nau 2021 (only Crossref metadata); Young 1993 and Kandori-Mailath-Rob 1993 (paywalled; the free-PDF guesses returned HTML stubs), so their statements are **[standard account]**; Boyd & Richerson 1985 (book; equation taken from file 25, which checked it against a secondary source). Web search was refused this turn (budget exhausted), so no new literature search for a competing chain model was possible beyond what files 25 and 40 already hold; the "no" below rests on the three papers read plus file 25's survey, and should be re-asked with search when budget returns. Everything tagged **[derived]** is this note's own algebra, not literature. The key identity was also checked numerically (see section 5).

**Summary.**
1. **No, no published model runs the whole chain.** Roos 2015 has threat but no conformity parameter and a fixed mutation rate. De 2017 and De 2018 have conformity or coordination-need parameters (`c`, `m`, `k`) but threat appears only in the motivation; the parameters are exogenous. Neither uses stochastic stability: De 2018 is a deterministic replicator, De 2017 is replicator plus simulations.
2. **The threat-to-parameter links are the weak joints, not the selection step.** Roos derives a threat effect from a concave fitness function with *no* `c` or `m` anywhere; "threat raises `c`" and "threat raises `m`" are verbal bridges in De et al., never derived.
3. **Specified model (section 4) gives three clean derived results**: (i) with conformity symmetric about one half, the stochastically stable convention is always the payoff-dominant one, whatever `m`, `c`, finite `k` (in De's matrix `M'` the payoff-dominant norm is also the risk-dominant one, so this is the usual KMR/Young risk-dominance selection, left unmoved by symmetric conformity); (ii) conformity only shrinks the *margin*: log-odds of the inferior convention are exactly `-beta N (1-m) (b-a)(2-c)/2` under logit revision; (iii) under uniform-error revision the same conformity can erase the margin entirely once `m >= m_c = Delta/(1+Delta)`. Result (iii) versus (ii) is a noise-model sensitivity the literature on tightness has not noticed. All three are derived here, unreplicated, and the three threat links feeding them are postulates.

---

## 1. Roos, Gelfand, Nau & Lun 2015

**Citation.** P. Roos, M. Gelfand, D. Nau, J. Lun, "Societal threat and cultural variation in the strength of social norms: An evolutionary basis", *Organizational Behavior and Human Decision Processes* 129, 14-23, July 2015. DOI 10.1016/j.obhdp.2015.01.003 (Crossref: volume 129; the PDF running head says 127). Read in full.

**Their vocabulary.** Societal threat `s`; strength of norms = share of norm adherers and of norm-enforcing punishers; cultural adaptation; "exploration (mutation) rate".

**Drives/operands.** No agent drive. Fear is an environmental subtraction from payoff. Agents carry a strategy (contribution type C/D/O, punishment type R/A/S/N in the public goods study; norm A/B and enforcement type in the coordination study).

**Operators / equations [read].**
- Payoff with threat: `p = base-pay - s + x` (x = accumulated game plus punishment payoff; base-pay = 30).
- Fitness: `f(p) = 1 - exp(-0.1 p)`, "diminishing marginal increases in fitness".
- Per step: birth of a random-strategy agent in an empty site; base payoff; four games; punishment; fitness; reproduction with probability `f` into an empty neighbouring site; mutation with probability `mu = 0.1` to a random strategy ("analogous to an exploration rate"); death with probability `d = 0.1`. Lattice 50x50, periodic, von Neumann neighbours.
- Public goods: contribution `c = 1`, multiplier `r = 3`, fine `q = 3/2`, punisher cost `k = 1/2`. Opportunist contributes iff (responsible punishers - anti-social punishers in group) `> c/q`, which with these parameters means "more responsible than anti-social punishers".
- Extreme threat: reference point shifted so far left that fitness is near 0 and "the death rate wipes out the population"; extreme low threat: flat part of the curve, "neutral drift". Results reported for `0 <= s <= 30`.

**Theorems / derived predictions.** None; simulation. The authors' mechanism is the concavity of `f`: raising `s` moves agents to the steep part where game payoffs matter more to reproduction.

**Empirical standing.** A model, so support is internal. It shows threat *can* select for norm enforcement given concave fitness; it does not show it did. The fitness shape is asserted; the authors say linear-logarithmic and sigmoid variants give the same direction (supplement, not read).

**Relevance to the chain.** The noise `mu` is fixed at 0.1. There is no conformity parameter. In the coordination study there are two symmetric norms A and B, so no convention is "selected" on merit. So Roos supplies exactly one link, threat acting on the *stakes* of the game through `f'`, and nothing else in the chain.

**Operand/operator translation.** `Threaten(s)` shifts a reference payoff; the carrier is the derivative `f'(w0 - s) = 0.1 exp(-0.1 (w0 - s))`, which multiplies every game payoff difference. That is my reading of what the concavity does; the paper gives it only in words.

---

## 2. De, Nau & Gelfand 2017; De, Nau, Pan & Gelfand 2018

**De 2017.** S. De, D. S. Nau, M. J. Gelfand, "Understanding Norm Change: An Evolutionary Game-Theoretic Approach", Proc. 16th AAMAS 2017, 1433-1441; arXiv 1704.04720 (the arXiv text is what I read; pages 1433-1441 confirmed by the validation pass from the IFAAMAS proceedings PDF, ifaamas.org/Proceedings/aamas2017/pdfs/p1433.pdf). Read in full except the appendix proofs (stated in text, not re-read in the appendix).

**Their vocabulary.** Need for coordination `c`; cultural inertia; exploration rate `mu`; structural shock; tight = high `c`.

**Equations [read].**
- Payoff matrix `M = c Mc + (1-c) Mf`; `Mc` has diagonal `(ac,ac)`, `(bc,bc)` and zeros off it; `Mf` has `(af,af)` for row A and `(bf,bf)` for row B regardless of the partner. Assuming `ac - bc = af - bf` and adding a constant (Lemma 1), `M'`: `A,A = (a,a)`; `A,B = ((1-c)a, (1-c)b)`; `B,A = ((1-c)b, (1-c)a)`; `B,B = (b,b)`.
- Replicator: `xA' = xA (E[uA] - E[u])`. Eq. (2): `xA' = xA (1-xA) ( c(a+b) xA - (b - (1-c)a) )`. Fixed points `xA = 0`, `1`, `phi = (b - (1-c)a) / (c(a+b))`.
- Lemma 2 / Theorem 1 (for `b > a`): `B` is an ESS; `A` is also an ESS iff `c >= (b-a)/b`; the interior point is unstable (Corollary 1). Symmetric statement for `a > b`.
- Eq. (4): for two societies with `c2 > c1`, both switching, `xB2' - xB1' = xB (1-xB)(c2 - c1)((a+b) xB - b)`: the tighter society is slower while `xB < b/(a+b)` and faster after (the tipping point).
- Replicator-mutator, eq. (5): `xA' = xA(1-xA)( c(a+b) xA - (b-(1-c)a) ) + mu ( xA xB (1-c)(b-a) + xB^2 b - xA^2 a )`.
- Simulation: 2500-node torus, Fermi imitation `p = (1 + exp(-s(ua - un)))^-1`, `s = 5`, exploration `mu`; "structural shock" = swap `a` and `b` (at 2500 iterations; for the exploration study every 75 iterations, 2000 iterations total); `mu` is chosen from `L = {0, 0.1, ..., 0.5}` as part of the copied strategy (the paper lists six values but says "5 possible exploration rates in L", a slip in the source).

**Results.** Higher `c` gives more inertia, and for `c >= (b-a)/b` permanent lock-in on the inferior norm (theorem, well-mixed). Evolved exploration rates are lower at high `c` (simulation, 100-run averages for the shock study; the exploration study shows plotted proportions, no tests). The paper itself notes that with no shocks `mu = 0` is always stable, so **the noise result depends on an exogenous shock schedule**.

**De 2018.** S. De, D. S. Nau, X. Pan, M. J. Gelfand, "Tipping Points for Norm Change in Human Cultures", SBP-BRiMS 2018, LNCS (Springer), pp. 61-69, DOI 10.1007/978-3-319-93372-6_7 (Crossref confirms authors, title, years and pages); arXiv 1804.07406. Read in full (7 pages).

**Equations [read].**
- Replicator (1): `xi' = xi ( fi(x) - phi(x) )`. Fitness (2): `fi = (1-m) ui + m theta_i(x,k)`, `theta_i = [1 + exp(-k (x - 0.5))]^-1`, with `uA + uB = 1`. (The text writes `x`; from context it is the share playing `i`.) Step-function limit `theta_inf` = 0, 0.5, 1 for share below, at, above one half.
- (5): `xB' = xB (1-xB) [ (1-m)(uB - uA) + m (thetaB - thetaA) ]`.
- (6): starting with `xA > xB` and `uB > uA`, change occurs iff `m < (uB - uA) / ((uB - uA) + (thetaA - thetaB))`; step limit gives `m < (uB-uA)/(uB-uA+1) < 0.5`.
- (7), (8): the more conformist society is slower for `xB <= 0.5`, and faster once `xB = 0.5 + eps` with `eps > ( ln(1 + uB - uA) - ln(1 - (uB - uA)) ) / k`. I re-derived (8) as `eps > (2/k) artanh(uB - uA)`; it agrees.

**Empirical standing of both.** Analytic or simulated models; no data are fitted. The modelling of tightness as `c` (or `m`) is a modelling choice, defended by citation to Gelfand 2011 and Roos 2015. The cultural-psychology correlates are in file 25.

**What they leave out, precisely.** Threat `s` is not a variable in either paper. `c`, `m`, `k` are inputs. No stochastic-stability analysis; no population-size scaling; no link from threat to the noise rate except De 2017's simulation (low `mu` evolves where `c` is high, *given* exogenous shocks).

**Operand/operator translation.** Operand: population share vector plus a parameter vector `(c, m, k, mu)`. Operators: `Shock` (swap `a,b`), `Tighten(c)` / `Loosen(c)`, the replicator flow. The `(1-m) u + m theta` form is a convex combination of a payoff and a conformity score, which is exactly the "drive composed with a social term" shape Aldred asked for.

---

## 3. The selection step and the sources not read

**Pan, Gelfand & Nau 2021.** X. Pan, M. J. Gelfand, D. Nau, "Integrating evolutionary game theory and cross-cultural psychology to understand cultural dynamics", *American Psychologist* 76(6), 1054-1066, DOI 10.1037/amp0000851. Crossref confirms title, authors, volume, pages; **content not read** (no open full text found). It is a review integrating the above models, so it is unlikely to contain a new chain model, but that is an inference from the title.

**Young 1993; Kandori, Mailath & Rob 1993 [standard account, not read].** H. P. Young, "The Evolution of Conventions", *Econometrica* 61(1), 57-84, DOI 10.2307/2951778; M. Kandori, G. Mailath, R. Rob, "Learning, Mutation, and Long Run Equilibria in Games", *Econometrica* 61(1), 29-56, DOI 10.2307/2951777 (both Crossref-confirmed). Standard content: a population repeatedly plays a coordination game, each agent best-responds (Young: to a sample of past play) except with probability `epsilon`, when it errs; the perturbed process is an irreducible Markov chain with a unique stationary distribution; as `epsilon -> 0` the mass concentrates on **stochastically stable** states, found by minimising the number of errors ("resistance") on trees of transitions (Freidlin-Wentzell). In a 2x2 coordination game that is the risk-dominant convention. Files 25 (F1) and 40 hold more.

**Further sources used for the specification (Crossref-confirmed, existence and venue only).**
- L. Blume, "The Statistical Mechanics of Strategic Interaction", *Games and Economic Behavior* 5, 387-424, 1993, DOI 10.1006/game.1993.1023. Standard account: **log-linear (logit) revision** of strategies; for potential games the long-run distribution is the Gibbs measure of the potential.
- J. Bergin, B. L. Lipman, "Evolution with State-Dependent Mutations", *Econometrica* 64, 943, 1996, DOI 10.2307/2171851. Standard account: if the error rate may depend on the state, the stochastically stable set can be changed, and the selection of risk-dominant conventions is not robust to the choice of mutation model. **This is the reason section 4 gives both a uniform-error and a logit version.**
- G. Ellison, "Learning, Local Interaction, and Coordination", *Econometrica* 61, 1047, 1993, DOI 10.2307/2951493. Standard account: with local interaction the waiting time to the selected convention is far shorter than with global interaction.
- D. Foster, H. P. Young, "Stochastic evolutionary game dynamics", *Theoretical Population Biology* 38, 219-232, 1990, DOI 10.1016/0040-5809(90)90011-j. Existence only.
- Boyd & Richerson 1985; Henrich & Boyd 1998 (DOI 10.1016/S1090-5138(98)00018-X) and 2001 (DOI 10.1006/jtbi.2000.2202), both Crossref-confirmed this session. Conformist transmission, from file 25 [confirmed there against a secondary source]: `p' = p + D p (1-p)(2p - 1)`, `D > 0` conformity. Note this term, like De's `theta`, is **odd about p = 1/2**; that property drives result 1 below.

**Empirical standing of the selection step (blunt).** Stochastic stability is a theorem about a limit (`epsilon -> 0`, `N` fixed) with waiting times that grow like `epsilon^-R`. For realistic `N` the "long run" is astronomically long, which is Ellison's point. It has not been tested against data on real conventions in any study I can name from this session's reading. Treat it as a selection *rule inside a model*, not a finding about societies.

---

## 4. Specified model: threat sets conformity and noise; the convention is selected

Everything in this section is **[derived]** unless it quotes a source. The model is built so each source's equation appears as a special case and every postulated link is flagged and replaceable.

### 4.1 Objects

- Environment: threat `s >= 0` (a payoff subtraction, as Roos). Operand of the slow layer.
- Population of `N` agents, each on norm `A` or `B`. `x` = share on `A` among the *other* agents the reviser samples (well-mixed; see 4.6 for local).
- Payoff scalars `a, b > 0`, coordination need `c in (0,1]`. Payoff gap in favour of `A` when the reviser faces share `x` on `A` (this is De 2017's `M'`, **[read]**, taken from eq. (2)):
  `L(x) = E[uA] - E[uB] = c(a+b) x - (b - (1-c) a)`.
- Conformity score (De 2018, **[read]**): `theta(x) = 1/(1 + exp(-k(x - 1/2)))`. Because `theta(1-x) = 1 - theta(x)`, the A-versus-B conformity gap is `theta(x) - theta(1-x) = tanh(k(x - 1/2)/2)` [derived, one line].
- Decision gap: `D(x) = (1-m) L(x) + m tanh(k(x - 1/2)/2)`. At `m = 0` this is De 2017; the `m` part is De 2018's `(1-m) u + m theta` applied to the *differences*.
- Revision (one agent at a time, then the others' shares update), two versions:
  - **U (uniform error, KMR/Young):** choose `A` if `D(x) > 0`, `B` if `D(x) < 0`, with probability `epsilon` choose uniformly at random.
  - **G (logit, Blume):** choose `A` with probability `1/(1 + exp(-beta D(x)))`.

### 4.2 The threat maps (the postulated joints)

| Link | Form | Status |
|---|---|---|
| T1 stakes: `beta(s) = beta0 f'(w0 - s) / f'(w0)` with Roos's `f(p) = 1 - exp(-kappa p)`, giving `beta(s) = beta0 exp(kappa s)`, `kappa = 0.1` | Roos's own concave `f`, but Roos uses `f` as a *reproduction probability*, not a choice intensity; carrying it to `beta` assumes agents learn through `f(payoff)`. **Bridging assumption.** | postulate built from a read equation |
| T2 coordination need: `c(s)` increasing, e.g. `c = s/(s + s_half)` capped at 1 | De 2017 motivates `c` by threat but states no map. Roos holds payoffs fixed. **Not in any source.** | postulate; shape is an editable setting |
| T3 conformity weight: `m(s)` increasing | De 2018: "tight = high m", no derivation from threat. **Not in any source.** | postulate; editable |
| T4 noise: in U, `epsilon(s)` decreasing | Only support: De 2017's *simulation* where low `mu` evolves at high `c` under periodic shocks. Roos fixes `mu`. In G, T1 already makes noise fall with `s` (`beta` up), so T4 is then not an extra postulate. | G: derived from T1; U: postulate |

Viability constraint (Roos): the population exists only for `s` below an extinction threshold (fitness near 0 and `d = 0.1`); the model is silent above it, and `Select` (below) is defined only inside that range.

### 4.3 Selection results (the derived theorems)

Let `g = c(a+b)`, `phi = (b - (1-c)a)/g` (the zero of `L`), `Delta = (b - a)(2 - c)/2`. Assume `b > a` for definiteness, so `B` is the payoff-dominant convention. For a pure convention to be an equilibrium of `L` we need `0 < phi < 1`, i.e. `c > (b-a)/b` for `A` (De's condition, **[read]**).

**R1 (winner invariance).** `D(1/2) = (1-m)(a-b)(2-c)/2`, because `tanh(0) = 0` and `L(1/2) = (a-b)(2-c)/2` (check: `c(a+b)/2 - b + (1-c)a = (a-b)(1 - c/2)`). `D` is strictly increasing (both parts are). So the best-response threshold `x*` (root of `D`) satisfies `x* > 1/2` iff `b > a`, for **every** `m < 1`, `k > 0`, `c in (0,1]`. Under U with `epsilon -> 0`, the cost to leave `A` is `N(1 - x*)` errors and to leave `B` is `N x*`, so `B` is stochastically stable iff `x* > 1/2` iff `b > a`. (The two-state birth-death argument is the standard KMR/Young one [standard account]; the algebra for `x*` is derived.) In De's `M'`, `B` is also risk-dominant (deviation losses `b-(1-c)a > a-(1-c)b` iff `(b-a)(2-c) > 0`), so R1 is the standard risk-dominance result surviving symmetric conformity, not a new selection criterion. Caveat (validation pass): at finite `N` resistances are integers, so when `x* - 1/2 < 1/(2N)` (large `k`, `m` near `m_c`) the two resistances can tie; R1 is a continuum statement. **Conformity that is symmetric between the norms cannot change the stochastically stable winner.** It cannot be the mechanism by which a tight society "stays on the inferior norm" in the long-run limit. De 2017's lock-in is an ESS (basin) statement, not a stochastic-stability one: `A` stays an ESS while `B` is the unique stochastically stable convention.

**R2 (margin, logit).** Under G with the sampling above (a `B`-agent samples `j` of `N-1` others on `A`, and so on), the stationary-distribution ratio of the two pure conventions is exactly `pi(all A)/pi(all B) = exp( beta * sum_{j=0}^{N-1} D(j/(N-1)) )`, because the combinatorial factors `(N-j)/(j+1)` telescope to 1. `D` minus its payoff part is odd about 1/2 so the conformity sum cancels, and `sum L(j/(N-1)) = N L(1/2)`. Hence
`log( pi(all A) / pi(all B) ) = - beta N (1-m) (b - a)(2 - c) / 2 = - beta N (1-m) Delta`.
It does not depend on `k`. Conformity (`m`) shrinks the exponent by `(1-m)`; it does not reverse it. If conformity is added as Boyd-Richerson's additive, odd term instead of the convex weight, the exponent is untouched by conformity.

**R3 (margin, uniform error).** Under U with `k -> infinity` (step conformity): `D(x) = (1-m) L(x) + m sgn(x - 1/2)`. If `m < m_c := Delta/(1 + Delta)` then `x* = phi - m/((1-m) g) > 1/2`, and the leading-order log-odds exponent is `R_B - R_A = N (2 x* - 1) = (2N/g)( Delta - m/(1-m) )`, i.e. `pi(A)/pi(B) ~ epsilon^{(2N/g)(Delta - m/(1-m))}`. If `m >= m_c` then `x* = 1/2` exactly: both conventions cost `N/2` errors to leave, **the payoff difference is invisible at leading order** and the system is a pure majority rule. `m_c = Delta/(1+Delta)` has the same form as De 2018's eq. (6) (`m < Delta u/(Delta u + 1)`), with `Delta u` replaced by the payoff gap at an even split, `Delta`. For finite `k` the threshold moves smoothly. So **R2 and R3 disagree about whether strong conformity erases payoff selection**: yes under uniform errors, no under logit. This is the Bergin-Lipman sensitivity, concretely, in the tightness setting.

**R4 (inertia).** For `m = 0`, global interaction, logit: the barrier (log of the expected escape time from `A`, large `N`, leading order) is `beta N * integral_{phi}^{1} L(x) dx = beta N g (1-phi)^2/2 = beta N (a - (1-c) b)^2 / (2 c (a+b))`, and from `B`: `beta N (b - (1-c) a)^2 / (2 c (a+b))`; their difference is `beta N Delta`, matching R2. The `A` barrier is increasing in `c` whenever `A` is an equilibrium and `b > a` (derivative sign `(a - b + c b)(b c + b - a)/c^2 > 0`). So at `m = 0` more coordination need and more `beta` both lengthen lock-in on the inferior norm. With conformity the barrier is `beta N * integral_{x*}^{1} D(x) dx` (the general form; I did not simplify it).

**R5 (what threat does to the margin).** With `beta(s) = beta0 e^{kappa s}`, `m(s)`, `c(s)`, the R2 exponent is `E(s) = beta(s) N (1 - m(s)) (b - a)(1 - c(s)/2)`. Then
`d ln E / ds = kappa - m'/(1-m) - (c'/2)/(1 - c/2)`.
**Threat makes the long run *more* decisive iff `kappa > m'/(1-m) + c'/(2-c)`; otherwise it flattens it.** So the model does not predict "threat gives a more rigid society" without qualification: the stakes channel pushes toward picking the better norm, the conformity and coordination channels push toward hold-whatever-you-have. Lock-in time (R4) rises with `beta` and with `c` (shown at `m = 0`). **Corrected by the validation pass:** this note first said it rises "along every channel"; the `m` channel depends on `k`. Numerically (a = 0.4, b = 0.6, c = 1, integral of `D` from `x*` to 1), the A-barrier for `m = 0, 0.2, 0.4, 0.6` is 0.080, 0.076, 0.072, 0.068 at `k = 1` (falls with `m`, because a weak conformity score cannot replace the payoff weight it displaces) and 0.080, 0.134, 0.191, 0.248 at `k = 10` (rises). So inertia rises with threat through `beta` and `c`, and through `m` only when `k` is large enough; the *selection quality* claim is the less robust of the two. This is a derived prediction, untested.

### 4.4 Numerical check
A scratch script (not kept in the repo) built the exact birth-death chain for `N = 200`, `beta = 0.05`, `a = 0.4`, `b = 0.6`, with `(c, m, k)` = `(0.5, 0, 10)`, `(0.5, 0.4, 10)`, `(0.5, 0.4, 200)`, `(1, 0, 10)`, `(1, 0.5, 10)`. In all five, `log pi(all A) - log pi(all B)` equalled `-beta N (1-m) Delta` to two decimals (`-1.50`, `-0.90`, `-0.90`, `-1.00`, `-0.50`), and did not change between `k = 10` and `k = 200`. This confirms R2 (and its `k`-independence) for that discretisation; it does not test R3, R4 or R5, which rest on the algebra above only.

### 4.5 Algebra translation
- **Operands:** the population share `x` or its distribution; the parameter vector `theta = (s, c, m, k, beta)`; the payoff pair `(a, b)`.
- **Operators:** `Threaten(ds)` and `Relax(ds)` (change `s`, slow clock); `Param`, the map `s -> (c, m, beta)` (T1-T3, the three editable joints); `Revise_theta`, the Markov kernel on `x` (U or G); `Shock` (swap `a` and `b`, De 2017); `Select`, the functional that returns the stationary distribution `pi_theta` (or its `epsilon -> 0` limit).
- **A law is a composition:** `Select . Revise . Param . Threaten`. The two clocks are explicit, which fits the "slow environment-to-parameter map, fast operator rule" two-layer reading already in file 25.
- Since `Select` is only defined as a limit, its output is best stored as a *log-odds exponent* (R2, R3) rather than a winner; that keeps it a smooth function of `theta`, so "soft settings" apply.

### 4.6 Limits and open items
- **Local interaction.** All results above are global-interaction. De 2017's simulations are on a torus. Ellison 1993 says local interaction changes waiting times drastically; whether R1 survives on a lattice with conformity was not derived here.
- **Magnitudes.** `N` multiplies every exponent, so with `N` in the thousands the margins are enormous and the model's long run is not a real time scale. Only signs and ratios are meaningful.
- **Endogenous noise.** The only evolving-noise result is De 2017's simulation, and it needs exogenous shocks. A derived `mu*(c, shock rate)` was not obtained. Plausible form, unverified: expected cost of a shock when locked on the inferior norm (R4's barrier time) against the payoff cost of exploring.
- **Asymmetric conformity** (for example, a bias toward the incumbent norm, or toward the elite's norm via prestige transmission) breaks the oddness behind R1 and can change the winner; not analysed.
- **No threat-dependent `a, b`.** Threat could itself change which norm pays (a structural shock); that is the `Shock` operator and is exogenous here.

---

## 5. Blunt "what exists vs what does not"

**Exists.**
- Threat -> norm strength via concave fitness (Roos 2015, simulation).
- Coordination need -> inertia, ESS multiplicity, lower evolved exploration (De 2017, theorem plus simulation).
- Conformity weight -> resistance to change and a tipping point (De 2018, analytic).
- Noise -> selection of conventions by resistance trees (Young, KMR; Blume for logit).
- Sensitivity of that selection to the noise model (Bergin-Lipman).

**Does not exist (in what was read).**
- A model with threat as a variable *and* conformity as a variable *and* noise, run through a stochastic-stability or Gibbs-measure selection step.
- Any derivation of `c(s)` or `m(s)` from threat. Both are postulated in the literature and here.
- Any empirical estimate of `m`, `c`, `k` for a real society. De et al.'s parameters are never fitted. (File 25 carries Boyd-Richerson-type conformity estimates; D361 owns those.)
- A test of R1-R5. They are consequences of assumptions, nothing more.

## 6. Unconfirmed

- Pan, Gelfand & Nau 2021 content (could contain a combined chain; unread).
- Young 1993 and KMR 1993 statements (standard account only; sampling and population-size conditions not checked at source).
- Whether a chain model exists in the 2022-2026 literature; search was unavailable this turn.
- Roos 2015's supplement (alternative fitness shapes; Study 2 detail on norm A versus B) not read.
- De 2017 appendix proofs not re-read; I only re-derived the replicator equations (2) and (4).
- Blume, Bergin-Lipman, Ellison, Foster-Young: Crossref existence and venue only; their theorem statements here are standard accounts.
- R3 and R4 closed forms were derived by hand and are not numerically checked against a chain. (The validation pass re-derived R3's `x*`, `m_c` and exponent and R4's two barriers, their difference `Delta` and the `c`-derivative by hand; all agree.)
- Whether a threat -> (conformity, noise) -> convention model exists outside the sources read: still untested, because web search was again unavailable to the validation pass (budget exhausted). The "no" in the summary stands as "none found in what was read".

## Validation log (2026-10-29)

Sources re-fetched this pass: De 2017 and De 2018 from arXiv, Roos 2015 author PDF, AAMAS 2017 p1433 PDF; every DOI resolved at api.crossref.org. Web search was unavailable (turn budget exhausted), so the "nothing exists" claim could not be re-tested by search.

- ✓ Roos, Gelfand, Nau & Lun 2015, OBHDP 129:14-23, DOI 10.1016/j.obhdp.2015.01.003 [read]: authors, volume (Crossref 129; PDF running head 127), `f(p) = 1 - e^{-0.1p}`, `p = base-pay - s + x`, base-pay 30, 50x50 periodic von Neumann lattice, 4 games, `mu = d = 0.1`, `r = 3, c = 1, q = 3/2, k = 1/2`, `0 <= s <= 30`, `c/q < N(R) - N(A)` rule, symmetric norms A/B, linear-log and sigmoid footnote all match.
- ✎ De, Nau & Gelfand 2017, AAMAS 1433-1441, arXiv 1704.04720 [read]: `M'`, eq. (2), fixed points, Lemma 2/Theorem 1 threshold `c >= (b-a)/b`, eq. (4), eq. (5), Fermi `s = 5`, 2500-node torus, shock at 2500 / every 75 over 2000, set `L`, "mu = 0 always stable" all match; pages now confirmed from the proceedings PDF; added the source's own 5-versus-6 slip on `L`.
- ✓ De, Nau, Pan & Gelfand 2018, SBP-BRiMS, LNCS pp. 61-69, DOI 10.1007/978-3-319-93372-6_7, arXiv 1804.07406 [read]: eqs. (1)-(8), step limit, `m < d/(d+1) < 0.5`, and (8) = `(2/k) artanh(uB - uA)` all match.
- ? Pan, Gelfand & Nau 2021, Am. Psychol. 76(6):1054-1066, DOI 10.1037/amp0000851: metadata confirmed; content unread.
- ✓ Young 1993, Econometrica 61(1):57-84, DOI 10.2307/2951778: metadata confirmed; content is a standard account, not read.
- ✓ Kandori, Mailath & Rob 1993, Econometrica 61(1):29-56, DOI 10.2307/2951777: metadata confirmed; standard account.
- ✓ Blume 1993, GEB 5(3):387-424, DOI 10.1006/game.1993.1023: metadata confirmed; standard account.
- ✓ Bergin & Lipman 1996, Econometrica 64(4):943, DOI 10.2307/2171851: metadata confirmed; standard account.
- ✓ Ellison 1993, Econometrica 61(5):1047, DOI 10.2307/2951493: metadata confirmed; standard account.
- ✓ Foster & Young 1990, TPB 38(2):219-232, DOI 10.1016/0040-5809(90)90011-j: metadata confirmed; existence only.
- ✓ Henrich & Boyd 1998, Evol. Hum. Behav. 19(4):215-241, DOI 10.1016/S1090-5138(98)00018-X, and Henrich & Boyd 2001, J. Theor. Biol. 208(1):79-89, DOI 10.1006/jtbi.2000.2202: metadata confirmed.
- ? Boyd & Richerson 1985 (book, *Culture and the Evolutionary Process*): no DOI to resolve; conformist-transmission equation is the standard form, carried from file 25.
- ✓ Derived R1, R2: re-derived; the R2 table in 4.4 reproduced exactly (-1.50, -0.90, -0.90, -1.00, -0.50) with an independent birth-death chain. ✎ R1: added that payoff-dominant and risk-dominant coincide in `M'`, and a finite-`N` tie caveat.
- ✓ R3, R4 closed forms: re-derived by hand, correct.
- ✎ R5: "lock-in rises along every channel" was wrong for the `m` channel at small `k`; corrected with numbers.

**Verdict.** Every cited work exists with the stated authors and venues, and each equation and parameter transcribed from the three papers read matches its source; nothing was fabricated. The note's own algebra holds (R2 exact, reproduced numerically; R3 and R4 check by hand), with one overreach corrected: conformity does not lengthen lock-in for every `k`. The headline "no model runs the chain" remains a claim about what was read, not a searched negative, because search was unavailable on both passes.

## Cross-checks (2026-10-29)

Method: grepped every other file in this directory for Roos, De/Nau/Gelfand, Pan, Young, KMR, Blume, Bergin, Ellison, Boyd, Henrich, stochastic stability, risk dominance, conformist transmission, tight/loose. Substantive overlap is with file 25 only (A2, C1, F1, Candidate laws 1, 3, 9, 10, "Does not exist"). Files 17 (section on Gelfand 2011), 51 (line 99 note on the tight/loose law) and 55 (Henrich and Gil-White, Henrich-Chudek-Boyd) touch the same authors but not the same claims. Files 66, 53, 63, 72 and 82 share no works or equations with this one. One primary-source check, below. No other file edited.

### Agreements (this file, section: file 25, section)

- Roos 2015 citation and volume (Crossref 129, PDF running head 127): 073 s.1: 25 A2. Same DOI 10.1016/j.obhdp.2015.01.003.
- Roos model details: payoff `p = base-pay - s + x`, base 30, `f(p) = 1 - exp(-0.1p)`, 50x50 periodic von Neumann lattice, four games, `mu = d = 0.1`, `c = 1`, `r = 3`, fine 3/2, punisher cost 1/2 (called `k` here, `lambda` in 25), opportunist rule `c/q` on responsible minus anti-social punishers, linear-log and sigmoid variants "same direction": 073 s.1: 25 A2.
- Roos mechanism is the concavity of `f`, no theorem, simulation only: 073 s.1: 25 A2 ("mechanism is diminishing returns, not fear").
- De, Nau & Gelfand 2017: `M = c Mc + (1-c) Mf`; Theorem 1 with `A` also an ESS iff `c >= (b-a)/b`; higher `c` evolves lower exploration and more inertia; threat only motivates `c`: 073 s.2: 25 A2 and Candidate law 3.
- De, Nau, Pan & Gelfand 2018: `f_i = (1-m) u_i + m theta_i`, logistic `theta`, tight = high `m`, tipping point in `m`, `k` and the payoff gap; DOI 10.1007/978-3-319-93372-6_7: 073 s.2: 25 A2.
- Pan, Gelfand & Nau 2021, Am. Psychol. 76(6) 1054-1066, DOI 10.1037/amp0000851, content unread in both: 073 s.3: 25 "Does not exist" and Unconfirmed. Both treat the "PNAS" version as absent or conflated.
- Conformist transmission `p' = p + D p(1-p)(2p-1)`, `D > 0` conformity, fixed points 0, 1/2, 1 with 1/2 unstable; secondary-source check (PMC8403876): 073 s.3: 25 C1. Henrich & Boyd 1998 and 2001 DOIs identical in both.
- Young 1993 (DOI 10.2307/2951778) and KMR 1993 (10.2307/2951777): same metadata; stochastic stability by resistance trees (Freidlin-Wentzell); risk-dominant in 2x2; both tag the theorem content as standard account, not read; both note the long-waiting-time caveat and local interaction: 073 s.3 and s.4.6: 25 F1.
- Headline "no single model runs threat -> (conformity, noise) -> stochastically stable convention; the pairwise pieces exist": 073 summary and s.5: 25 Candidate law 3 and "Does not exist". Both rest on a search that could not be re-run in validation; 073 says so, 25 says "as far as this survey found".
- Two-layer reading (slow environment-to-parameter map, fast operator rule): 073 s.4.5: 25 closing observation after Candidate laws.

### Contradictions

1. **De 2017 title.** 073 s.2 says "Understanding Norm Change: An Evolutionary Game-Theoretic **Approach**". File 25 A2 says "...Game-Theoretic **Study**". Primary source checked (arxiv.org/abs/1704.04720): "Understanding Norm Change: An Evolutionary Game-Theoretic Approach (Extended Version)", authors De, Nau, Gelfand. **Verdict: 073 is right; 25 A2 has the wrong last word** (to be fixed in 25 by its owner; not edited here).

### Tensions that are not strict contradictions

2. **Does tight = low noise decide which norm wins?** File 25 F1 Translation says that with tightness as lower `epsilon`, "Young's machinery says which norm a tight society locks in". 073 R1 shows the stochastically stable winner in the `epsilon -> 0` limit does not depend on symmetric conformity, `m`, `c` or `k`; lock-in on the inferior norm is an ESS (basin) result, not a stochastic-stability one. These agree only if 25 is read as being about basins and finite `epsilon`. 073 is the more precise statement, but it is the note's own derivation (not replicated), so the verdict is **unresolved** pending an independent check of R1; the numerical check in 073 s.4.4 supports R2 only.
3. **Status of the De 2017 noise result.** 25 A2 states "high `c` evolves a low exploration rate" without qualification; 073 s.2 adds that it needs an exogenous shock schedule (the paper itself says `mu = 0` is always stable with no shocks). Not a disagreement about the paper; 073 is the fuller account and 25 should carry the caveat.
4. **Payoff in Roos Study 2.** 25 A2 infers matching pays about 2 from a figure caption; 073 s.1 only says the two norms are symmetric. Compatible.

### Not cross-checked

- 073's own results R1-R5 and the Blume, Bergin-Lipman, Ellison and Foster-Young statements appear in no other file, so there is nothing to compare them with.
- 25 C1's "weighted-copying" prestige form is labelled there as a stylisation; 073 does not use it.
