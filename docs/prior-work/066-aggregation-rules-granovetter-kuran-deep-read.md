# Prior work 66: aggregation rules, with Granovetter and Kuran read in full

Direction: D245

Date: 2026-10-29. Survey for the social-algebra strand. Question (research map D245): catalogue the rules by which individual states become a group state, read Granovetter and Kuran in full (equilibrium condition, stability), and say which rules are equivalent and which theorems each carries. Merges the old 18 aggregation-rules survey and 24 Granovetter/Kuran deep-read.

Aim served (Aldred, 2026-10-29): an algebra of basic human and group drives that compose into equations, yield theorems, and are used to predict or control behaviour. Cross-references: 05 (Granovetter, opinion dynamics), 18 (collective emotion, ASCRIBE, Schweitzer-Garcia, McClelland), 24 (Steiner, Chan, Bell, Epstein), 47-48 (coupling proofs).

**Method and honesty note.** Tags used throughout:
- **[read]** read at source this session, text extracted and checked line by line.
- **[derived]** my own algebra from [read] equations; a check I did, not a claim of the authors.
- **[computed]** numerical check run this session.
- **[secondary]** a secondary source that describes the primary.
- **[standard account]** background knowledge, not checked this session.

Sources read in full this session: Granovetter 1978 (gwern.net scan, 22 pages), Watts 2002 (NYU copy of the PNAS text), Schweitzer and Garcia 2010 (arXiv 1006.5305, all 26 pages through the equations), Smaldino et al. 2012 (JASSS PDF, model sections), Bertozzi et al. 2015 (UCLA CAM report 14-36, sections 1-1.2). **Not obtainable: Kuran 1991 and 1995** (JSTOR/Harvard UP paywalled; the Duke link for the 1991 PDF is dead, 404). Kuran below is **[secondary]**: Brummitt, Barnett and D'Souza 2015 (arXiv 1410.4175), which cites his equation numbers, Rasmusen's book review, and abstracts. **Validation correction (2026-10-29):** the equation and figure numbers Brummitt et al. cite ("[62, Eq. 8]", "[62, Figures 3-7]", "[62, Section 4.1, pages 51-53]") are to Kuran's **1989** *Public Choice* paper "Sparks and prairie fires", not to the 1991 *World Politics* paper this note originally named. So the "read Kuran in full" half of D245 is **not done**; see Unconfirmed.

DOIs confirmed through Crossref this session: 10.1086/226707 (Granovetter), 10.1073/pnas.082090499 (Watts), 10.2307/2010422 (Kuran 1991), 10.1140/epjb/e2010-00292-1 (Schweitzer-Garcia), 10.18564/jasss.2030 (Smaldino), 10.1007/s10955-014-1019-6 (Bertozzi), 10.1007/s10458-012-9201-1 (Bosse 2013), 10.1007/978-3-642-17537-4_25 (Hoogendoorn 2010), 10.1007/s12559-014-9277-9 (Bosse 2015), 10.1016/j.ijhcs.2003.08.003 (McClelland 2004; **the Crossref title is "The collective control of perceptions: constructing order from conflict"**, differing from the "Collective control of perception" in notes 18 and elsewhere), 10.1177/0956797620970561 (Goldenberg et al. 2021, *Psychological Science* 32, 437-450, "The Crowd-Emotion-Amplification Effect"; this fills the volume and pages that note 18 lacked), 10.1037/0021-9010.83.2.234 (Chan 1998). Added at validation (all resolved on Crossref 2026-10-29): 10.1007/BF00116762 (Kuran 1989), 10.2307/j.ctvt1sgqt (Kuran, *Private Truths, Public Lies*, JSTOR/Harvard UP record), 10.1098/rsif.2015.0712 (Brummitt et al. 2015), 10.1016/S0167-2681(98)90013-0 (Rasmusen 1998 review), 10.1103/PhysRevE.75.056103 (Gleeson and Cahalane 2007), 10.1007/978-3-642-23974-8_42 (Tsai et al. 2011), 10.7148/2009-0212-0218 (Bosse et al. 2009), 10.1007/s11135-019-00883-9 (Lustick and Miodownik), 10.1098/rsos.160059 (Garcia et al. 2016), 10.1037/0021-9010.92.3.595 (Bell 2007), 10.1073/pnas.092080199 (Epstein 2002), 10.1016/S0065-2601(10)43002-6 (Leonardelli, Pickett and Brewer 2010).

---

## Summary

1. **Four structurally different aggregators carry the field, not ten.** (a) A *weighted mean* toward neighbours (consensus: ASCRIBE with no amplification, McClelland's virtual controller). (b) A *threshold on a population fraction* (Granovetter, Watts, Epstein), whose group outcome is a fixed point of a cumulative distribution. (c) A *decaying field* fed by expressions (Schweitzer-Garcia). (d) A *nearest-to-target frequency choice* (Smaldino). The static composition rules (sum, min, max, mean, product, dispersion; Steiner, Chan, Bell) are a fifth, different kind: they define a group variable, not a dynamic.
2. **Granovetter's model is a monotone one-dimensional map, and everything he shows follows from that.** r(t+1) = F[r(t)] [read]. Because F is non-decreasing, iteration from the start converges monotonically to the *least* fixed point, never oscillates, and the least fixed point is what his "first crossing from above" means [derived]. His headline result, that two crowds with almost the same mean threshold have wildly different outcomes, is a statement that the fixed-point map is not continuous in the mean. I reproduced his normal-distribution result: critical sigma 12.22 against his "approximately 12.2" [computed].
3. **Watts reduces to Granovetter on a complete graph, and extends it with a static percolation criterion.** Watts's cascade condition, the sum over k of k(k-1) rho_k p_k = z [read], replaces "iterate F to the fixed point" with "does the vulnerable subgraph percolate". It gives two phase transitions (a window in z), a power-law cascade-size distribution at the lower edge and a bimodal one at the upper edge [read].
4. **Schweitzer-Garcia's agent is a Granovetter agent in a quasi-static limit, but its aggregate is a rate, not a stock, and the paper contains sign errors in its stationary solution.** The expression threshold on arousal converts to a threshold on the field: h_i* = tau_i gamma_a / (d0 + tau_i d1) under the paper's own linear case [derived from its eq. 22]. The field's fixed point then has the Granovetter form with a *rate function* in place of F [derived]. The paper's eq. (17) and the drift in (18) have an inconsistent sign for b3 against its own Figure 2 (b3 = -1) [read; derived]. The mathematics is right once b3 < 0 is handled correctly: bistability iff b1 h > gamma_v.
5. **ASCRIBE's amplifying variant is a convex combination of three drifts, and with bias beta = 1/2 the amplification cancels** [derived from the standard-account equation, which I could not read at source]. The consensus core is [read] in Bertozzi. In the data comparison cited by Bertozzi, the consensus-type ASCRIBE beat a threshold model (Durupinar) by 14% per agent per frame on a 15 s clip [read, as reported], which is the only head-to-head of threshold against consensus on behavioural data found so far, and it is thin (two video clips).
6. **Kuran's contribution relative to Granovetter is a rule that derives the threshold from utilities, and a distinction between expressed and private state.** The equilibrium condition has the same fixed-point structure: share S of public opposition, one or three equilibria, two stable and one unstable when three [secondary: Brummitt et al. 2015, citing Kuran **1989** (*Public Choice* 61) Eq. 8 and Figures 3-7; corrected at validation from "Kuran 1991"]. What it adds is the cause of the threshold, which Granovetter left as a black box. It is unverified at source here.
7. **No test of which aggregator is right for a motivational state exists.** The comparison of mean vs min vs max vs dispersion has been done for team traits (Bell 2007, 24) but not for drives. D247 owns that question.

---

## 1. Granovetter 1978: Threshold models of collective behavior [read in full]

**Citation.** Granovetter, M. (1978). Threshold models of collective behavior. *American Journal of Sociology* 83(6), 1420-1443. DOI 10.1086/226707 (Crossref confirmed). Text read from the gwern.net scan, pp. 1420-1443, all sections.

**Their vocabulary.** "Threshold": "the proportion of the group he would have to see join before he would do so" [read p. 1422]; "instigator" (threshold 0%); "radical" and "conservative" as low and high threshold; threshold 100% means will not join under any circumstances; "bandwagon" and "domino" effect; "equilibrium outcome"; "forward recursion"; "perceived proportion of rioters".

**Drives/operands.** The operand is a population of actors each carrying a single scalar threshold x in [0, 1] (or an absolute count; "the mathematical analysis is the same in either case" [read, fn. 3]). The threshold is "the result of some (possibly complex) combination of costs and benefits" [read], "simply that point where the perceived benefits to an individual of doing the thing in question exceed the perceived costs". There is no named drive. The paper explicitly says it treats the aggregation of individual preferences and does not consider how individuals come to have them [read]. Scope: binary decisions where the cost and benefit depend on how many others choose which (binary collective decisions of the kind Granovetter catalogues in the paper, from riots to adoption and diffusion examples [read]).

**Operators / equations, exactly [read].**
- Thresholds x, frequency distribution f(x), cumulative distribution F(x) "indicates the proportion of the population having threshold less than or equal to x" (p. 1425).
- r(t) = proportion who have joined by time t (discrete time).
- **Difference equation: r(t+1) = F[r(t)]** (p. 1425).
- **Equilibrium: setting r(t+1) = r(t); "the point where the c.d.f. first crosses the 45 degree line from above. Algebraically ... F(r) = r"** (p. 1427). Write r_e for the equilibrium.
- "In this simple version of the model, where no provision has been made for 'removal' of participants, oscillatory behavior of r(t) is not possible, and an equilibrium will always be reached" (p. 1426).
- Graphical method (Fig. 1, credited to Christopher Winship): plot F(x) against x and the 45 degree line; iterate vertically to the cdf, horizontally to the diagonal.
- **Social structure extension** (p. 1429): influence weighted by tie; example "the influence of friends is twice that of strangers": an individual with threshold 50% who knows 20 people of whom 15 have joined "sees" [(15 x 2) + (33 x 1)] joiners and [(5 x 2) + (47 x 1)] non-joiners, ratio 63/120 = .525 > .5, so he joins. Procedure: threshold distribution, a sociomatrix and a weight for each cell give equilibrium by forward recursion.
- **Sampling extension** (pp. 1431-1432): a crowd of 100 drawn at random from a population with the uniform distribution (1% at each integer threshold 0 to 99). Probability of no instigator = (1 - .01)^100 = .37; probability of exactly one instigator and no one at threshold 1 = 100(.01)(.99)^99 times (.99)^100 ≈ .14, so over half (.51) of crowds end with zero or one rioter. With 10 incidents of probability .10 each of a large riot, the chance of no large riot is (.90)^10 = .35. This is used to explain Spilerman's finding that the number of racial disorders scales with black population.

**Worked results [read].**
- **Uniform distribution of thresholds** (one individual at each of 0, 1, ..., 99 of 100): equilibrium 100 (a bandwagon). Replace the person at 1 by a second at 2: equilibrium 1. "The two crowds are essentially identical", the outcome is not (p. 1425).
- **Normal thresholds** (mean 25, N = 100, thresholds below 0 treated as 0, above 100 as never; analysis credited to Bob Phillips): equilibrium rises gradually with sigma "to about six", then at sigma_c "approximately 12.2" r_e "jumps to nearly 100, after which it declines"; limit as sigma grows without bound is 50 (Fig. 2, p. 1427). Mechanism: the normal cdf can cross the diagonal three, two or once; at sigma_c the first two crossings merge in a tangency. **[computed]** I iterated r -> 100 * Phi((r - 25)/sigma) from r = 0: sigma = 12.0 gives 4.0; 12.1 gives 4.55; 12.2 gives 5.48; 12.3 gives 100.0; bisection puts the jump at sigma_c = 12.222. This matches the paper to the digits given. His "about six" is the left-limit value just below sigma_c (5.5 at 12.2).

**Stability, in his own words and in the algebra.** Section "The stability of equilibrium outcomes" says the uniform distribution and the normal near sigma_c "have highly unstable equilibria" (p. 1429). He states the aim as "mathematical procedures for assessing the stability characteristics of any distribution's equilibrium under a variety of possible perturbations", and **does not supply one**. He tests three perturbations: removing or adding individuals (gaps in the distribution), social structure (sociomatrix weights; simulation by Douglas Danforth), and sampling (above). Results [read]: for the perturbed uniform (equilibrium 1), social structure rarely moves the outcome by more than 5-10 rioters, largest effects when acquaintance volume is about one quarter of the group; for the true uniform (equilibrium 100), "almost any kind of social structural influence" collapses it, the modal equilibrium becoming one rioter. "When threshold distributions have very stable equilibria it may make very little difference; when these equilibria are unstable, however, the effects of social structure may overwhelm those of individual preferences" (p. 1430).

**The standard stability criterion, which the paper does not state [derived].** For a smooth F: a fixed point r_e is locally stable if F'(r_e) < 1 and unstable if F'(r_e) > 1; tangency F'(r_e) = 1 is a saddle-node (fold) bifurcation, which is exactly the sigma_c event in Fig. 2. For the empirical (finite, step-function) F the derivative does not exist; the relevant robustness notion is the size of the gap: the number of individuals that must be added or removed to change the crossing. Under that reading the uniform distribution is a case of *marginal* stability (F(x) = x exactly: every point is a fixed point of the continuous version) broken only by integer effects. Here is the algebraic reason it is so fragile.

**Theorems or derived predictions.**
- *Monotone convergence* [derived]: if F is non-decreasing and r(0) = 0 then r(t) is non-decreasing and converges to the least solution of F(r) = r. (Standard monotone-sequence argument; Granovetter asserts "an equilibrium will always be reached".) Validation caveat [derived]: the limit is a fixed point when F is left-continuous at it, which holds for any finite population (the iteration stops in finitely many steps) and for continuous F; a cdf with an atom approached from below (e.g. F(x) = x/2 + 1/4 on [0, 1/2), F = 1 from 1/2) gives a limit 1/2 that is not a fixed point.
- *Non-identifiability of individual dispositions from aggregate outcome* [read]: "it is hazardous to infer individual dispositions from aggregate outcomes" (p. 1425). This is the substantive claim, supported by the example pair above.
- *Sensitivity to the distribution not the mean* [read]: two groups with almost identical mean threshold "radically different" in outcome; he states that sociology concentrates on averages and should not.
- *Sampling variability produces between-city divergence with identical distributions* [read], with the Bernoulli calculations above.
- No uniqueness, existence or complexity theorem is stated formally; the paper is calculation plus argument.

**Empirical standing, blunt.** Granovetter's paper contains **no fit to data**; the Spilerman discussion is an illustrative reinterpretation of a published regression, not a test. His section "The Falsification of Threshold Models" (pp. 1437-1439) [read at validation, 2026-10-29] does give falsification conditions: the model "may be said to have been, in effect, falsified" where "all or most thresholds are at 0% or 100%" (behaviour not contingent on others); and if aggregate participation "oscillated from one level ... to another" in a stable cost-benefit situation, some individuals' net-benefit curves cross zero more than once, which the simple model excludes (p. 1438-1439). He also treats misperception of the proportion, including Merton's "pluralistic ignorance", where thresholds are passed but actors do not know it (p. 1438). The field's evidence is indirect: Watts-type models fitted to diffusion and crowd data, Epstein's agent-based version (24), and the Tsai et al. comparison (section 5). A blunt reading (this note's, not Granovetter's): the model is **weakly falsifiable in practice** because the threshold distribution is a free function fitted post hoc, and the number of parameters (the whole cdf) exceeds the single outcome it predicts; Granovetter's own conditions test the model's *form*, not any particular F. Its value is as a *counterexample generator* showing why mean-based reasoning fails, not as a predictive model.

**Operand/operator translation for the algebra.**
- Operand: a population with a threshold distribution F (an element of the space of non-decreasing functions [0,1] to [0,1]). Group state: r in [0,1].
- Operator: **cascade** C_F : r -> F(r); group outcome = least fixed point lfp(C_F). Composition of two aggregation steps is composition of maps; because each is monotone, the composition is monotone and lfp exists (Knaster-Tarski) [derived].
- Group outcome is *not a function of any finite moment of F*. This is a theorem-grade constraint on the algebra: a group variable "mean threshold" cannot be a sufficient statistic.
- Drive mapping: threshold = the point where approach tendency exceeds avoidance tendency (Granovetter's footnote, quoting Wheeler (Wheeler, quoted in Granovetter 1978, fn. 2; Wheeler's wording, not Granovetter's): contagion "occurs at the point where observing another individual's behavior pushes the approach tendency above the avoidance tendency", fn. 2 [read]). That is exactly the Miller (1944) crossing d* of note 16. So **a threshold is the crossing of an approach drive and an avoidance drive, expressed in the variable "fraction already acting"**. This is the cleanest bridge between the two-drive core (16) and the group aggregate found in this survey.

---

## 2. Watts 2002: global cascades on random networks [read in full]

**Citation.** Watts, D. J. (2002). A simple model of global cascades on random networks. *PNAS* 99(9), 5766-5771. DOI 10.1073/pnas.082090499 (Crossref confirmed). Read from the NYU copy of the PNAS text.

**Their vocabulary.** "Binary decisions with externalities"; "threshold rule"; "vulnerable" vertex and "stable" vertex; "early adopters", "innovators"; "cascade condition"; "global cascade" (occupies a finite fraction of an infinite network); "extended vulnerable cluster"; "cascade window".

**Model, exactly [read].** "An individual agent observes the current states (either 0 or 1) of k other agents, which we call its neighbors, and adopts state 1 if at least a threshold fraction phi of its k neighbors are in state 1, else it adopts state 0." Thresholds drawn from f(phi) on [0,1]; degrees from p_k with mean z; initially all off with a fraction Phi_0 << 1 switched on; asynchronous random-order updating; once on, stays on.

**Equations [read].**
- Vulnerable: with a single seed neighbour, a vertex with degree k activates iff phi <= 1/k, i.e. k <= K = 1/phi. Probability a degree-k vertex is vulnerable: rho_k = P[phi <= 1/k] = F(1/k) for k > 0 (and 1 for k = 0) (Eq. 1b).
- Generating functions of vulnerable-vertex degree: G_0(x) = sum_k rho_k p_k x^k (1a); G_1(x) = sum_k k rho_k p_k x^(k-1) / sum_k k p_k = G_0'(x)/z (2); vulnerable cluster-size generating functions satisfy H_1(x) = [1 - G_1(1)] + x G_1(H_1(x)) (3a), H_0(x) = [1 - G_0(1)] + x G_0(H_1(x)) (3b).
- Mean vulnerable cluster size <n> = H_0'(1) = G_0(1) + [G_0'(1)]^2 / (z - G_0''(1)) (4).
- **Cascade condition (Eq. 5): the average vulnerable cluster size diverges when G_0''(1) = sum_k k(k-1) rho_k p_k = z.** G_0''(1) < z: vulnerable clusters finite, no global cascades. G_0''(1) > z: a percolating vulnerable cluster, global cascades with finite probability.
- Uniform random graph (Poisson p_k = e^(-z) z^k / k!) with homogeneous threshold phi*: Eq. 5 reduces to **z Q(K* - 1, z) = 1**, K* = 1/phi*, Q the incomplete gamma function. Size of the vulnerable cluster there: S_v = Q(K*+1, z) - e^(z(H_1 - 1)) Q(K*+1, z H_1) with H_1 solving H_1 = 1 - Q(K*, z) + e^(z(H_1 - 1)) Q(K*, z H_1) (given in the text).

**Theorems or derived predictions [read].**
- Because rho_k decreases with k while k(k-1) increases, Eq. 5 has either zero or two solutions in z: a **cascade window** in average connectivity, with a phase transition at each edge. Below the window the early adopters are isolated; above it each node has so many neighbours that no one is moved by a single one.
- At the lower edge cascade sizes are power-law distributed (cumulative slope 1/2, density exponent 3/2; n = 1,000, z = 1.05); at the upper edge the distribution is **bimodal** (exponential tail plus a peak at system size; z = 6.14). The upper transition is first-order (discontinuous). Larger cascades are "increasingly rare" toward the upper edge.
- **Heterogeneity is two different things and they do not act alike**: widening the threshold distribution widens the window (more vulnerable); widening the degree distribution (power-law with cut-off) narrows it (less vulnerable). So "network heterogeneity and threshold heterogeneity ... are not equivalent" [read].
- In the lower regime the most connected nodes trigger cascades disproportionately; in the upper regime they do not.
- Surprising result [read]: the average *size* of a global cascade tracks the whole connected component S, not the vulnerable cluster: a cascade started in a small vulnerable core eventually topples the stable majority too once enough neighbours are on, so a small vulnerable percolating cluster suffices to activate the entire connected component (random graphs only; stated as holding "at least within the class of random graphs").

**Empirical standing.** The analytic condition is checked against simulation of the *same model* (n = 10,000; 1,000 realisations), agreeing except near the upper boundary (finite size). **No empirical data are fitted in the paper.** Later empirical work on real cascades (e.g. the "Flickr" and viral-marketing literature) is out of scope and unread here; it is a known weak point that real cascades are mostly small and subcritical.

**Operand/operator translation.** Operand: a graph with a threshold per node. Operator: threshold update on neighbour fraction. The cascade condition is a **graph invariant** (a moment of the degree distribution weighted by vulnerability), the first *structural* theorem in the survey: it says what group property decides whether a drive-level cascade can happen, as a function of network and threshold distributions jointly.

---

## 3. Kuran 1991, 1995: preference falsification [secondary only]

**Citations.** Kuran, T. (1989). Sparks and prairie fires: a theory of unanticipated political revolution. *Public Choice* 61(1), 41-74. DOI 10.1007/BF00116762 (Crossref confirmed at validation; **this is the paper whose Eq. 8 and Figs 3-7 the equilibrium statements below come from**, per Brummitt et al.'s reference [62]). Kuran, T. (1991). Now out of never: the element of surprise in the East European revolution of 1989. *World Politics* 44(1), 7-48. DOI 10.2307/2010422 (Crossref confirmed). Kuran, T. (1995). *Private Truths, Public Lies: The Social Consequences of Preference Falsification*. Harvard University Press. (The original note said "no DOI found"; at validation Crossref returns the JSTOR book record 10.2307/j.ctvt1sgqt, dated 1998, the paperback/JSTOR edition. 10.2307/2076660 and 10.2307/2235544 are reviews by Boudon, *Contemporary Sociology* 1995, and Hamlin, *Economic Journal* 1996.)

**What was and was not read.** The primary texts could not be obtained. Everything below is from three sources I did read: (i) Rasmusen, E. (1998), review of *Private Truths, Public Lies*, *Journal of Economic Behavior & Organization* 33, 309-311, DOI 10.1016/S0167-2681(98)90013-0 (preprint at rasmusen.org/published/Rasmusen_98.JEBO.kuran.pdf, read in full; re-read at validation); (ii) Brummitt, C. D., Barnett, G. and D'Souza, R. M. (2015). Coupled catastrophes: sudden shifts cascade and hop among interdependent systems. *Journal of the Royal Society Interface* 12(112), 20150712, DOI 10.1098/rsif.2015.0712 (read as arXiv 1410.4175; the Kuran passage is in its section 3.1 and cites "[62, Eq. 8]", "[62, Figures 3-7]", where [62] is **Kuran 1989**, re-read at validation); (iii) abstracts and commentary found by search. All tagged [secondary]. Note that the three-utility vocabulary (intrinsic, expressive, reputational) is Rasmusen's account of the **1995 book**; Brummitt et al. describe the **1989** model with two components, "reputational utility" and "integrity utility".

**Their vocabulary.** Private preference (fixed); public preference (a chosen declaration); **preference falsification** (the gap); three utility components: **intrinsic utility** (maximal at the person's true preference), **expressive utility** (value of declaring one's own view; Kuran assumes it peaks at the same point as intrinsic [Rasmusen]), **reputational utility** (maximal at the declaration that elicits the most favourable response from society, independent of effect on the outcome); **political / revolutionary threshold** (the level of public opinion at which a person is indifferent between publicly supporting the extremes); **pluralistic ignorance**; "thinkable and unthinkable" [Rasmusen].

**Drives/operands.** Persons with a position on a spectrum [0, 1] (0 the current government, 1 the opposition) [secondary]; the group state is the (weighted) share of people who publicly declare for the opposition [secondary, arXiv 1410.4175]. The drives in play: wanting to be right (intrinsic), wanting to be authentic (expressive), wanting social approval or avoiding punishment (reputational).

**Operators / equations.**
- The individual utility is a sum of the three components, with the declaration chosen to maximise it [secondary, Rasmusen: "if he gives weight to all three considerations" the declaration lies between 30 and 70 in his example]. **I could not obtain the functional form or the weights; not transcribed.**
- The threshold is derived: it is the level of mean public opinion at which reputational utility tips the person's declaration from one extreme to the other (Rasmusen's example: intrinsic optimum 20, switches from 0 to 100 when others' mean support moves from 59 to 60).
- **Equilibrium**: the share S of public opposition solves a fixed-point equation (Eq. 8 of the **1989** *Public Choice* paper per Brummitt et al.; corrected at validation from "the 1991 paper") with "one or three equilibria; in the latter case, two equilibria are stable and the other unstable" (Figs 3-7). Slow changes in utilities or in the preference distribution can cause "a large, sudden change in collective sentiment (in a saddle-node bifurcation)". Brummitt et al. state the equilibrium manifold is equivalent in a catastrophe-theoretic sense to its own stylised model.
- Kuran gives two routes to a saddle-node bifurcation [secondary, Brummitt et al. citing Kuran 1989 §4.1, pp. 51-53; filled in at validation]: (1) a shift in the distribution of private preferences toward the opposition (Kuran's Fig. 3), e.g. from an economic downturn; (2) a change in the reputational utility terms (e.g. the opposition becomes better able to give reputational utility), shifting the threshold function. Brummitt et al. also quote Kuran (Kuran 1989 p. 53, quoted in Brummitt et al. 2015) that such a shift could be "made possible by funds provided by a foreign source".

**Theorems or derived predictions.**
- *Multiple self-fulfilling equilibria and discontinuous jumps from small shocks* [secondary, Rasmusen]: because my position is itself part of public opinion, which determines my reputational payoff.
- *Revolutions are unpredictable even to participants* because the private distribution is hidden: public opinion stays stable while private opinion shifts, and a small trigger moves it [secondary].
- Rasmusen notes the formal model "fades into the background" in the later chapters (communism, caste, affirmative action) and that the examples are narrated rather than computed.

**Relation to Granovetter [derived, from the secondary equilibrium description].** Same mathematical object: a population share S, a map from S to the induced share, a fixed-point condition, one or three roots, stable/unstable alternate by the sign of (slope - 1). The shared structure is what lets the arXiv authors treat it as a fold catastrophe. The differences:
1. *Threshold origin.* Granovetter takes x as primitive. Kuran *derives* x from intrinsic position, expressive and reputational weights; so changing the reputational weight (the cost of dissent, i.e. repression) shifts every threshold at once. This is a *control parameter*, which Granovetter has no analogue for and the algebra needs.
2. *Observed vs hidden state.* Kuran separates private preference (hidden) from public preference (what the aggregation sees). The aggregation operator acts on public state only. This is the one *model* in the survey where aggregate and member state diverge by design. (Validation note: Granovetter 1978, p. 1438, already names the phenomenon, Merton's "pluralistic ignorance", where thresholds are passed but actors do not make their action public; he does not formalise it. Kuran formalises it.)
3. *Continuous positions.* Kuran's position is on [0, 1]; the declaration is chosen, not binary, though the arXiv paper's description is of the share declaring for the opposition.

**Empirical standing, blunt.** The 1991 paper is an *ex post* interpretation of 1989; Kuran's own historical examples are narrative. The related claim, that opposition is hidden by falsification until a trigger, has experimental and survey support for pluralistic ignorance in general, but the specific 1989 prediction is unfalsifiable post hoc and he explicitly argues that such events are unpredictable in principle. Rasmusen's critique [read]: expressive utility is problematic (some people do not care to express anything, and others may differentiate from the crowd rather than match their private view); reputational utility is underspecified (why do others care about *my* declaration?); and the informational-cascade explanation (Bikhchandani, Hirshleifer, Welch) is mentioned but not integrated. A further published critique (a 1997 review found by search, unread) argues reputational and intrinsic utility double count in the East European case. A later simulation paper (Lustick, I. S. and Miodownik, D., "When do institutions suddenly collapse? Zones of knowledge and the likelihood of political cascades", *Quality & Quantity* 54(2), 413-437, online 2019, issue 2020, DOI 10.1007/s11135-019-00883-9, Crossref confirmed at validation; **content could not be fetched; unread**) says it overcomes limitations of Kuran's mathematical models with continuous private opinion and binary public opinion.

**Operand/operator translation.** Operand: person = (private position, weights on the three utility components); group state = public share. Operator: **declare** D_w : (private position, perceived public share) -> public position. The aggregate is the fixed point of the induced map on public share. Control parameter: reputational weight (repression, anonymity). Drive mapping: expressive and intrinsic utility are *internal* drives, reputational utility is a *coupling* to group state. The algebra needs this split (internal vs coupling), and it is the same split as note 56's sociometer.

---

## 4. Schweitzer and Garcia 2010: Brownian agents with a communication field [read]

**Citation.** Schweitzer, F. and Garcia, D. (2010). An agent-based model of collective emotions in online communities. *European Physical Journal B* 77(4), 533-545. DOI 10.1140/epjb/e2010-00292-1 (Crossref confirmed). Read from arXiv 1006.5305 (the preprint, "to appear 2010"; equation numbers below are the preprint's, and the published version may differ in the signs flagged below).

**Their vocabulary.** Brownian agent; valence v and arousal a; emotional state e = {v, a}; communication field h+(t), h-(t); "emotional expression"; "silent regime" and "excited regime"; "dropout" of agents; "saturated" vs "superlinear" feedback; "collective emotion".

**Equations, exactly [read].**
- (1) generic Brownian-agent form: state change = deterministic force + stochastic force.
- (2) dv_i/dt = -gamma_v,i v_i(t) + F_v + A_v,i xi_v(t);  (3) da_i/dt = -gamma_a,i a_i(t) + F_a + A_a,i xi_a(t); xi white noise.
- (4) expression: s_i(t + Dt) = sign(v_i(t)) Theta[a_i(t) - tau_i], Theta the Heaviside step. Number of expressions N_s(t) = sum_i Theta[a_i - tau_i] (5); average n_s = (1/t_end) integral of N_s dt (6). Delay Dt may be drawn from a power law P(Dt) ~ Dt^(-alpha).
- (7) field: dh_±/dt = -gamma_± h_±(t) + s N_±(t) + I_±(t), N_± the number of agents expressing a positive or negative statement, s the impact of one expression, I an external input.
- (8) valence force F_v ∝ (r_i/2){(1 + r_i) f[h+] - (1 - r_i) f[h-]}, r_i = sign(v_i): agents respond to field content of their own valence's sign. (9) alternative F_v ∝ g[h+ - h-]. (10) f[h±, v_i] = h±(t) sum_{k=0..n} b_k v^k(t).
- (11) arousal with reset: da/dt = (subthreshold form) Theta[tau - a] - a Theta[a - tau]: reset to zero on expression. (12) F_a ∝ [h+ + h-] sum_k d_k a^k; (13) alternative F_a ∝ [h+ + h-] a Theta[a].
- (14) dv/dt = -gamma_v v + h±(b0 + b1 v + b2 v² + b3 v³ + ...); stationary: **(15)** v³ + v²{b2/b3} + v{(b1 - gamma_v/h±)/b3} + {b0/b3} = 0. With b0 = b2 = 0: **(17) v² = (b1 - gamma_v/h±)/b3**, real only if b1 > gamma_v/h±; solutions symmetric about zero.
- (18) Fokker-Planck for p(v,t); (19) stationary p(v) = (1/N_v) exp{[v²(b1 h± - gamma_v) - v⁴ (b3 h±/2)] / A_v²}: unimodal at v = 0 if b1 < gamma_v/h±, bimodal otherwise; variance set by A_v².
- (20) subthreshold arousal da/dt = -gamma_a a + h(d0 + d1 a + d2 a² + ...), h = h+ + h-; (22) for d2 = 0: **a(h) = h d0 / (gamma_a - d1 h)**; (23)-(24) for d2 ≠ 0: two real stationary solutions iff [(d1 - gamma_a/h)/(2 d2)]² > d0/d2.
- (25) time to threshold: T = integral from 0 to tau of da / [h d2 a² + (h d1 - gamma_a) a + d0 h]; (26) arctanh form for d2 < 0; (27) arctan form for d2 > 0 and R(h) = 4 d2 d0 - (d1 - gamma_a/h)² > 0. Expression frequency f_s(h, tau) = 1/T.

**Theorems or derived predictions [read].**
- **Valence pitchfork**: for the symmetric cubic, v = 0 is stable and unique when b1 h < gamma_v; two symmetric stable valences appear when b1 h > gamma_v. So "collective emotion" requires the field to exceed the critical value **h* = gamma_v / b1**. This is a supercritical pitchfork in h [derived label for the paper's statement].
- **Arousal**: saturated feedback (d2 < 0) gives one stable positive and one unstable negative stationary arousal; an agent whose arousal fluctuates below the unstable level "drops out" permanently; superlinear feedback (d2 > 0) gives two negative stationary solutions, a stable one at the more negative value, so agents can re-enter. Hence "the non-saturated case defines the scenario where we most likely expect the emergence of collective emotions". Fluctuations are essential: "such a scenario can never be sustained in a purely deterministic dynamics" [read].
- **Critical field for sustained expression**: f_s(h, tau) is zero below a critical h = h⋆ and rises above it (Fig. 4, tau = 0.5).
- **Sign problem [read; derived]**: from (14) with b0 = b2 = 0 the nonzero stationary solutions satisfy -gamma_v + h(b1 + b3 v²) = 0, i.e. v² = (gamma_v/h - b1)/b3. The paper's (17) has the opposite numerator, (b1 - gamma_v/h)/b3. They agree only if b3 is read as a positive stabilising magnitude, but Figure 2 uses **b3 = -1** (the stabilising sign under (14)). With b3 = -1, (17) as printed gives a negative v² when b1 > gamma_v/h. Likewise the drift in (18) shows -b3 h v³ and the potential in (19) shows -v⁴ (b3 h/2), which for b3 = -1 is the *unconfining* sign. The bifurcation condition (b1 h > gamma_v) is unaffected; a reader building on the stationary amplitudes or on (19) must restore the sign. I checked this against the preprint only; the published EPJB text may have corrected it (**Unconfirmed**).
- Simulation: Fig. 2 compares (19) with histograms of N = 1,000 agents (A_v = 0.15, gamma_v = 0.8, b1 = 1, b3 = -1, h = 0.25 and h = 17.5).

**Empirical standing.** The 2010 paper fits no data; it states hypotheses "which can be tested". Garcia, Kappas, Küster and Schweitzer (2016, *Royal Society Open Science* 3(8):160059, from 18) tested the micro-dynamics on 207 participants (relaxation to baseline; arousal rises with emotional content, falls after posting). I did not re-read that paper this session. No test of the *aggregate* prediction (bimodal valence as a function of field) on human data was found.

**Operand/operator translation.** Operand: agent = (v, a, tau, gamma_v, gamma_a), plus a shared field (h+, h-). Operators: relax, perceive-field (F_v, F_a), express-and-reset, field-update. This is the only model in the survey where the aggregate is a *memory* (a leaky integral of expressions) rather than an instantaneous statistic.

---

## 5. ASCRIBE and related consensus-type models (Hoogendoorn, Bosse, Bertozzi, Tsai)

**Citations.** Bosse, T., Duell, R., Memon, Z. A., Treur, J. and van der Wal, C. N. (2009). A multi-agent model for mutual absorption of emotions. ECMS 2009, 212-218, DOI 10.7148/2009-0212-0218 (Crossref confirmed at validation). Tsai, J., Bowring, E., Marsella, S. and Tambe, M. (2011). Empirical evaluation of computational emotional contagion models. IVA 2011, LNCS, 384-397, DOI 10.1007/978-3-642-23974-8_42 (Crossref confirmed at validation; this is Bertozzi's ref. [40], the source of the 14%/12% figures; unread). Hoogendoorn, M., Treur, J., van der Wal, C. N. and van Wissen, A. (2010). Modelling the interplay of emotions, beliefs and intentions within collective decision making based on insights from social neuroscience. ICONIP 2010, LNCS, 196-206, DOI 10.1007/978-3-642-17537-4_25 (Crossref confirmed). Bosse et al. (2013), *AAMAS* 27(1), 52-84, DOI 10.1007/s10458-012-9201-1 (Crossref confirmed). Bosse et al. (2015), *Cognitive Computation* 7(1), 111-136, DOI 10.1007/s12559-014-9277-9 (Crossref confirmed). Bertozzi, A. L., Rosado, J., Short, M. B. and Wang, L. (2015). Contagion shocks in one dimension. *Journal of Statistical Physics* 158(3), 647-664, DOI 10.1007/s10955-014-1019-6 (Crossref confirmed). Read: Bertozzi's section 1.1 (UCLA CAM 14-36).

**What is [read].** Bertozzi Eq. (1): dq_i/dt = gamma (q_i* - q_i), q_i* = (sum over j in G_i of w_ij q_j) / (sum over j in G_i of w_ij). "The basic contagion model is a variant of a classical consensus model in control theory." The full ASCRIBE weights w depend on five quantities: sender's emotion level, receiver's emotion level, sender's expressiveness, receiver's openness, channel strength. Movement x_i' ∝ q_i. Durupinar's model is "a probabilistic threshold model based on epidemiological models" and ASCRIBE gave "a 14% improvement per agent per frame over the Durupinar model in a 15 s clip and a 12% improvement in only a four-second clip", from the Tsai et al. comparison on a video of an Amsterdam crowd and a Greek tear-gas protest [read, as reported by Bertozzi; the Tsai paper itself unread this session]. The 1-D continuum limit leads to shock dynamics related to pressureless gas with sticky particles; in 1-D, q plays the role of velocity as in Cucker-Smale.

**What is [standard account] (note 18, not verifiable here).** The amplification form: q_R(t + Dt) = q_R + gamma_R [eta_R (beta_R (1 - (1 - q*_R)(1 - q_R)) + (1 - beta_R) q*_R q_R) + (1 - eta_R) q*_R - q_R] Dt, eta the tendency to amplify, beta the bias upward. I could not obtain Bosse 2009 or 2015 to read it.

**Consequences of that equation [derived; hold only if the standard-account form is right].** Write bracket = eta (Phi - q) + (1 - eta)(q* - q), Phi = beta(1 - (1 - q*)(1 - q)) + (1 - beta) q* q. Then Phi - q = beta q*(1 - q) - (1 - beta) q (1 - q*). So

dq/dt = gamma [ eta ( beta q*(1 - q) - (1 - beta) q (1 - q*) ) + (1 - eta)(q* - q) ]

- eta = 0: pure consensus, a linear equation whose weighted-mean fixed point is unique on a connected graph.
- eta = 1, beta = 1: dq/dt = gamma q*(1 - q) >= 0: **upward amplification saturating at 1**, driven by any positive q*; fixed points are q = 1 or q* = 0.
- eta = 1, beta = 0: dq/dt = -gamma q (1 - q*): decay to 0 unless q* = 1.
- eta = 1, beta = 1/2: dq/dt = (gamma/2)(q* - q): **amplification cancels and the model is consensus at half rate**. Amplification only does something when beta ≠ 1/2.

**Equivalence with Granovetter: no.** The consensus core has no threshold and no multiple equilibria: with q* a convex combination of others' q, it contracts toward the weighted mean (DeGroot-type). It cannot produce a bandwagon from a small seed: a small initial q is *averaged away* unless amplified. The amplifying variant is a different object: a mean-field map with fixed points at the boundary {0, 1}, which can mimic tipping (positive feedback until saturation) but has no interior unstable fixed point in the homogeneous case, hence no critical mass. Tipping requires heterogeneous beta or eta across agents [derived; unverified].

**Operand/operator translation.** Operand: scalar intensity q in [0,1] per person per emotion. Operator: weighted-mean absorption plus a nonlinear amplifier. The weighting w_ij = sender expressiveness x channel x receiver openness is a *product* of three person/dyad parameters [standard account; Bertozzi [read] says only that the full ASCRIBE weights depend on five quantities, including both emotion levels, and does not give the product]; the algebra should carry it as a dyadic operator. The comparison with the threshold model is a bright spot: the only behavioural-data contest between aggregator types found in this survey, albeit two clips.

---

## 6. McClelland: the collective controller [abstract and secondary; unread]

**Citation.** McClelland, K. (2004). The collective control of perceptions: constructing order from conflict. *International Journal of Human-Computer Studies* 60, 65-99. DOI 10.1016/j.ijhcs.2003.08.003 (Crossref confirmed; the title on Crossref differs from the "Collective control of perception" used in notes 05, 07 and 18).

**What I could confirm.** The citation. An academia.edu abstract (identity unconfirmed: possibly this paper, possibly a sibling) says: collective control of perceptions "can stabilize variables in a shared environment even when interactants conflict" and applies PCT to elementary interactions by computer simulation. The paper itself was not retrievable. The aggregation rule is therefore **[standard account], carried over from note 18**: two controllers acting on one variable behave as a single virtual controller with summed gain and a reference at the gain-weighted mean, r_v = (G1 r1 + G2 r2)/(G1 + G2) (reported from McClelland 1993 via Martin Taylor's PCT page).

**Where it sits.** It is the same arithmetic as ASCRIBE consensus (a weighted mean) but arises from a different place: opposed *references* acting on a *shared environmental variable*, not influence between internal states. The weighted mean is therefore the group's *set point*, while the output effort of the parties escalates against one another [standard account]. That makes two things the other models lack: a distinction between the set point and the effort, and conflict as a property of the aggregate (effort goes up while the variable sits still). **Equivalent to ASCRIBE consensus only at the level of the formula.**

---

## 7. Smaldino et al. 2012: optimal-distinctiveness group choice [read, model sections]

**Citation.** Smaldino, P. E., Pickett, C., Sherman, J. and Schank, J. (2012). An agent-based model of social identity dynamics. *Journal of Artificial Societies and Social Simulation* 15(4), 7. DOI 10.18564/jasss.2030 (Crossref confirmed).

**Model [read].** Agents hold a social identity (SID) among a finite number; each has a preferred frequency d* of its SID in the (visible) population ("optimal distinctiveness"). Update: the agent computes d_g = n_g/N for each SID and switches to the SID whose d_g is closest to d* by |d_g - d*|, ties random (the example: d* = 0.33, own d = 0.15, others 0.35 and 0.5, switches to the 0.35 SID). Spatial version on an L x L lattice with neighbourhood radius r (square of side 2r + 1); the agent sees only local frequencies.

**Equations and results [read].**
- (1) Prediction from the theory: if everyone were optimally distinct, the number of active SIDs would be k* = round[1/d*].
- (2) **Observed in the well-mixed model: k*(d*) = floor[1/(2 d*)] + 1** (results "exactly follow" it; N = 3,000, k0 = 30). For d* = 0.2 this gives 3, versus the theory's 5. In the N = 50 example the run ends with three groups of about equal size, each of frequency about 0.33, "a level significantly higher than the optimal" [read].
- Mechanism: an SID with fewer members than d* N is always nearer the target than one far over it, so members leave the smaller SIDs; the number of groups collapses until each is too big.
- Spatial restriction (local, overlapping neighbourhoods) gives average distinctiveness "much closer to optimal" than the well-mixed case; runs used L = 50, k0 = 9.

**Theorem-like content.** Equation (2) is an exact empirical law of the simulation, **not a proof** in the paper; the mechanism is verbal. The lesson is general and sharp: an individual-level target (moderate-sized groups) does not aggregate to the group state it targets when everyone shares the same information, but does when information is local.

**Empirical standing.** None; a theory-testing simulation of Brewer's optimal distinctiveness theory. Brewer's ODT itself has experimental support (Leonardelli, Pickett and Brewer 2010 review), not rechecked here.

**Operand/operator translation.** Operand: agent with target frequency d*. Operator: **move toward nearest-to-target group** (a choice rule, not a mean or a threshold). Drive mapping: it is one concrete two-drive balance (belonging vs distinctiveness) giving a single target on a group-level frequency. Note the update is on a *frequency* like Granovetter's r, so the same state variable can be fed to both rules: one agent's rule is monotone in r (Granovetter), the other's is single-peaked in r (Smaldino). Validation note: Granovetter (1978, pp. 1438-1439, Fig. 3) [read] already considers individuals whose net benefit crosses zero twice (the restaurant that is too empty or too full; the rioter who leaves past 90%), says equilibria "cannot be guaranteed" then, and that "a somewhat different analytical apparatus would be needed". So the non-monotone case is flagged, not modelled, in Granovetter.

---

## 8. Static composition rules (from 24, not re-read)

For completeness, and with the 24 tags carried over:
- **Steiner (1972)** task-typed combination: additive (sum), disjunctive (max), conjunctive (min), compensatory (mean), discretionary; actual = potential - process loss [standard account].
- **Chan (1998)** composition models: additive, direct consensus, referent-shift, dispersion, process (DOI 10.1037/0021-9010.83.2.234, Crossref confirmed this session). **Kozlowski and Klein (2000)**: composition (isomorphic) vs compilation (non-isomorphic, e.g. min, max, configuration) [standard account].
- **Bell (2007)** meta-analysis: the operationalisation (mean, min, max, variance) moderated the link between team trait composition and performance [24, from abstract].
- **Goldenberg et al. (2021)** (*Psychological Science* 32, 437-450, DOI 10.1177/0956797620970561, Crossref confirmed): perceived crowd emotion exceeds the true mean, more so with more faces and for anger [from abstract, per 18]. This is a rule for the *perceived* aggregate, a biased-mean operator: **members respond to Amplify(mean), not mean**, which changes what any feedback aggregator actually computes.
- **Epstein (2002)** civil violence: an agent acts if grievance G = H(1 - L) minus net risk exceeds a threshold, with risk rising with the local cop-to-active ratio [standard account, 24]. This is Granovetter with a state-dependent threshold shift.

---

## Catalogue: aggregation rules and their types

| # | Rule | Group state computed | Type | Source | Read? |
|---|------|----------------------|------|--------|-------|
| 1 | Sum / count | N_s(t), total | static | Steiner additive; Schweitzer-Garcia (5) | read (S-G) |
| 2 | Max / min | best / weakest member | static (compilation) | Steiner disjunctive / conjunctive | standard |
| 3 | Mean | average state | static | Steiner compensatory; Chan additive | standard |
| 4 | Dispersion | variance | static | Chan dispersion | standard |
| 5 | Product | conjunction of factors | static | Karau-Williams, Vroom (24) | standard |
| 6 | Weighted mean of neighbours | q_i* | dynamic, linear | ASCRIBE consensus (Bertozzi Eq. 1) | read |
| 7 | Gain-weighted mean of references | r_v | static solution of a control equilibrium | McClelland | secondary |
| 8 | Mean-field threshold on population fraction | fixed point of F | dynamic, monotone nonlinear | Granovetter | read |
| 9 | Threshold on neighbour fraction on a graph | cascade size; percolation of vulnerable cluster | dynamic, structural | Watts | read |
| 10 | Threshold on a leaky field | h, rate of expression | dynamic, memory | Schweitzer-Garcia | read |
| 11 | Nearest-to-target frequency choice | group size distribution | dynamic, non-monotone | Smaldino | read |
| 12 | Amplify-mean (perceived) | perceived crowd state | bias operator | Goldenberg 2021 | abstract |
| 13 | Public from private (falsified) | public share | threshold, hidden state | Kuran | secondary |
| 14 | Mean plus nonlinear amplifier (absorb/amplify) | q after contagion | dynamic, nonlinear | ASCRIBE full | standard |

---

## Which are equivalent, and which are not

Stated as precisely as the evidence allows; every equivalence below is **[derived]** here unless said otherwise.

1. **Granovetter = Watts on the complete graph with homogeneous information.** On K_n each node sees all others; phi becomes the fraction threshold x; rho_k for the single degree n - 1 is F(1/(n-1)), but with seeds of size larger than one, the "vulnerable by one neighbour" analysis fails, and the correct mean-field reduction is Granovetter's r(t+1) = F[r(t)]. Watts's cascade condition therefore *replaces*, rather than restates, Granovetter's fixed-point test when the graph is sparse and the seed small. Conversely, sparse-graph mean-field versions of Watts that recover the Granovetter map as a limit exist in the literature (Gleeson, J. P. and Cahalane, D. J. (2007), "Seed size strongly affects cascades on random networks", *Physical Review E* 75(5), 056103, DOI 10.1103/PhysRevE.75.056103; existence and citation confirmed on Crossref at validation; **that it recovers the Granovetter map as a limit is not checked; Unconfirmed**). Watts's own paper states the model "differs from" others in that it uses a fraction of the neighbourhood, and its "extended vulnerable cluster" results show that the stable majority matters, which a pure Granovetter treatment cannot represent.
2. **Granovetter ≈ Schweitzer-Garcia, in the quasi-static limit, as a *rate* map.** Under the paper's linear arousal case (d2 = 0, eq. 22), agent i expresses iff a(h) = h d0/(gamma_a - d1 h) >= tau_i, i.e. iff h >= h_i* = tau_i gamma_a/(d0 + tau_i d1) (valid when d0 + tau_i d1 > 0, and h d1 < gamma_a). The field's stationary value, from (7) with I = 0 and averaged expression, is h = (s/gamma) times the sum over agents of expression frequency, so h = (s/gamma) sum_i f_s(h, tau_i). If an expresser stayed expressed, f_s would be a unit step at h_i*, and this is exactly h = (s N/gamma) F_h(h), with F_h the cdf of the h_i*: Granovetter's fixed-point equation up to scale, with the threshold on the field instead of on a fraction. Because of the reset (11), f_s is a continuous increasing rate (non-zero above h⋆), not a step. So the equivalence holds *only if expression is persistent*; otherwise S-G's aggregate is a rate whose fixed-point has the same structure (monotone map, least fixed point, folds) but different numerics. The valence pitchfork has no Granovetter analogue (it is a within-agent symmetry-breaking in sign), though the amplitude of h required, h* = gamma_v/b1, is a threshold on the field in the same sense.
3. **Kuran = Granovetter with a derived threshold and a hidden/observed split** (see section 3). Same fixed-point structure, same fold bifurcations. Not a different aggregator; a different *primitive* (utilities, not thresholds).
4. **ASCRIBE consensus ≠ Granovetter.** A linear contraction with a unique weighted-mean fixed point has no critical mass. The amplifying variant behaves as a saturating positive-feedback map but without an interior unstable equilibrium in the homogeneous case. Both outperform or fail relative to threshold models only on the 12-14% data comparison.
5. **ASCRIBE consensus ≈ McClelland gain-weighted mean.** The same arithmetic, different interpretation: (influence on state) vs (opposed references on a shared variable). A map from one to the other would need a theory of what the shared variable is.
6. **Smaldino ≠ any of the above.** Its response to the group frequency is single-peaked, not monotone, so the Knaster-Tarski least-fixed-point argument fails and its dynamics need not be monotone; it can and does collapse groups. It is the one model here in which the agent's *target* is a function of the group state, the strongest case for treating group state as an operand of an individual drive.
7. **Static rules (1-5) are not in competition with the dynamic ones.** They define the group *variable*; the dynamic rules define how it *evolves*. Granovetter's r is a count/mean of binary states (rule 3 applied to indicator variables). Watts's cascade size is rule 1 over a percolating cluster.
8. **Mean vs threshold is the key non-equivalence.** Granovetter's theorem-grade point: mean is not a sufficient statistic of F. The ASCRIBE linear model, in contrast, *is* determined by weighted means. So choosing the aggregator for a drive decides whether the group outcome depends on the mean or on the whole distribution. That is an empirical choice that, as far as found, **no one has tested for a motivational variable** (D247).

## Theorems each carries (summary)

| Model | What is proved or exact | Status |
|-------|------------------------|--------|
| Granovetter | r(t+1) = F[r(t)]; equilibrium F(r) = r at first crossing from above; no oscillation; monotone convergence; fold at sigma_c ≈ 12.2 for normal thresholds, mean 25 | stated in the paper; monotone convergence and the F' < 1 criterion are **[derived]**; sigma_c **[computed]** 12.222 |
| Watts | Cascade condition sum k(k-1) rho_k p_k = z; two phase transitions; power-law at lower edge, bimodal at upper; S_v closed form (Poisson, homogeneous) | analytic, checked by simulation of the same model |
| Schweitzer-Garcia | Valence pitchfork at h* = gamma_v/b1; stationary p(v) from Fokker-Planck; arousal fixed points and dropout vs re-entry; critical h⋆ for sustained expression | analytic; sign errors in preprint eq. (17)-(19) |
| Kuran | One or three equilibria; two stable one unstable; saddle-node on slow change | **secondary**; not read |
| ASCRIBE | Consensus convergence to weighted mean (standard); amplification form (standard account) | consensus **[read]** (Bertozzi), rest **[standard]** |
| Smaldino | k*(d*) = floor[1/(2d*)] + 1 | empirical regularity of the simulation, not proved |
| McClelland | Virtual controller reference r_v = gain-weighted mean | **[standard account]** |

---

## What exists vs what does not (blunt)

**Exists.**
- A rigorous, small theory of threshold aggregation: the monotone map, its fixed points, folds (Granovetter, Watts, Kuran's equilibrium as reported) with real theorems on graphs (Watts's percolation criterion).
- A linear-consensus family with analytic results (ASCRIBE core, McClelland) and a head-to-head against a threshold model on two crowd clips (12-14% improvement).
- A leaky-field model with an explicit bifurcation analysis (Schweitzer-Garcia).
- A vocabulary of static composition rules (Steiner, Chan) and a trait-level test of them (Bell).

**Does not exist (as far as found).**
- A test of **which aggregator describes a motivational state** (mean vs min vs max vs threshold vs dispersion) on human data. Each model assumes its own.
- **Measured threshold distributions.** Granovetter's F is never independently measured. Without it, the models are not falsifiable in the form published.
- A **common state space**: Granovetter's r is a fraction of binary actors; Schweitzer-Garcia's h is a field amplitude; ASCRIBE's q is a continuous intensity; Smaldino's d_g is a group frequency; Kuran's S is a share of *declarations*. There is no mapping among them in the literature, and I did not construct one beyond the Granovetter / Schweitzer-Garcia quasi-static correspondence above.
- **Stability theory for threshold distributions** under perturbation beyond the one-dimensional F' < 1 criterion and Granovetter's simulations (social-structure and sampling). Granovetter states this aim and does not deliver it.
- A model in which **the aggregator is chosen per drive** (fear by one rule, curiosity by another). Every model uses one rule.
- A reading of Kuran's utility-based threshold in terms of *drive strengths* (the expressive/reputational weights are the nearest thing to a drive-weight vector, but are not calibrated against anything).

## Implications for the algebra (suggested, not decided)

1. Make the **aggregator an explicit, named operator** with a declared signature: input = a population's states (and possibly a graph), output = a group-level quantity. Granovetter's point means a group variable computed by `mean` and one computed by `lfp(F)` are different *types*, even when both are reported as "proportion active".
2. Include **least fixed point of a monotone map** as a primitive: C_F with F in the space of cdfs, with a known composition law (composition of monotone maps is monotone) [derived].
3. A **threshold is the crossing point of an approach drive and an avoidance drive** on the variable "fraction acting" (Granovetter fn. 2; Miller in 16). This gives the algebra a derivation of a population threshold from two drive curves, rather than a free parameter.
4. Keep **private state and expressed state as separate operands**, with the aggregator acting on expressed state (Kuran). Repression and anonymity are then control parameters that change the map from private to expressed.
5. Keep **fold points (tangency, F' = 1)** as the theorem-bearing objects: the algebra's prediction/control claims should be statements of the form "this operator shifts the distribution across a fold", not point predictions of group behaviour.

## Unconfirmed

- **Kuran's own text.** Neither the 1989 or 1991 article nor the 1995 book was read. The utility functional forms, the weights, Eq. 8 (of the 1989 paper), and any explicit stability condition are unverified at source; the "two ways" are now known only through Brummitt et al.'s summary. The statements in section 3 about equilibrium count and stability come from that one paper's summary.
- **The ASCRIBE amplification equation** (eta, beta) is from note 18's standard account; I could not access Bosse 2009 or 2015 to read it. The three-term decomposition and the beta = 1/2 cancellation are my algebra on that unverified form.
- **McClelland 2004** was not read; the gain-weighted-mean rule is carried over from note 18.
- **Whether the published EPJB version of Schweitzer-Garcia corrected the b3 sign** in eqs. (17)-(19). I read only the arXiv preprint.
- **Gleeson and Cahalane 2007** as the mean-field bridge between Watts and Granovetter: the paper exists (DOI confirmed); its content was not read.
- **The Tsai et al. 2011 comparison** (14%, 12%) is quoted through Bertozzi (whose wording was re-checked at validation), not read at source. (A 2013 *AAMAS* follow-up by the same authors, DOI 10.1007/s10458-013-9220-6, exists; unread.)
- **The Lustick and Miodownik paper** on Kuran-type cascades (10.1007/s11135-019-00883-9; citation confirmed, content unread) and the 1997 double-counting review (not identified; no author, venue or DOI) were not fetched.
- **Granovetter's final section**: the falsification subsection (pp. 1437-1439) was read at validation and is now reported in section 1; the remaining closing pages on norms were not transcribed.
- **Garcia et al. 2016** (207 participants) is carried from note 18; citation confirmed, numbers not re-read.
- **Hoogendoorn et al. 2010** is cited with a confirmed DOI, but its content (the extension to beliefs and intentions) is from note 18 only.
- **Goldenberg et al. 2021 effect sizes** and Bell 2007 numbers are as in notes 18 and 24, unread.

## Author's working log (pre-validation)

- Granovetter PDF downloaded and extracted with pdftotext; equations, page numbers and the 100-person examples checked against the text. The normal-threshold result reproduced numerically (sigma_c = 12.222).
- Watts PDF downloaded (NYU copy) and extracted; Eqs. 1-5 transcribed from the text layer. The Poisson reduction z Q(K* - 1, z) = 1 and the S_v expression are quoted as printed; I did not re-derive them.
- Schweitzer-Garcia preprint extracted; eqs. (1)-(27) transcribed; the sign analysis is my derivation from (14), checked by hand.
- Bertozzi CAM report: section 1.1 read; the amplifying variant is not in it.
- Smaldino JASSS PDF extracted; eqs. (1)-(2) quoted, and the worked example read.
- DOIs checked by Crossref as listed in the header; two DOI guesses failed and were replaced by Crossref-located ones (McClelland 2004; Goldenberg 2021).

## Validation log (2026-10-29)

Every DOI below was resolved at api.crossref.org/works/<doi> on 2026-10-29; [read] marks where the source text was re-read for this pass.

- ✓ Granovetter 1978, AJS 83(6) 1420-1443, 10.1086/226707 [read: gwern scan re-extracted]. Difference equation, "first crosses the 45° line from above", no-oscillation sentence, Winship/Phillips/Danforth credits, friend-weight example (63/120 = .525), sampling numbers (.37, .14, .51, (.90)^10 = .35), "about six" / "approximately 12.2" all match. sigma_c = 12.222 recomputed independently.
- ✎ Granovetter 1978, falsification: the note said the model is "unfalsifiable as stated" and that the later pages only treat thresholds as hard to measure; the paper's falsification subsection (pp. 1437-1439) gives explicit falsifying conditions and discusses pluralistic ignorance and two-crossing (non-monotone) individuals. Rewritten; caveat added on monotone convergence for cdfs with atoms.
- ✓ Watts 2002, PNAS 99(9) 5766-5771, 10.1073/pnas.082090499 [read: JSTOR copy]. Poisson reduction z Q(K*-1, z) = 1, S_v and H_1 expressions, n = 10,000 with 1,000 realisations, z = 1.05 and 6.14 at n = 1,000, slope 3/2 (cumulative 1/2), bimodal/first-order upper edge, "not equivalent" heterogeneity and "at least within the class of random graphs" all match.
- ✎ Kuran 1989, Public Choice 61(1) 41-74, 10.1007/BF00116762: added. Brummitt et al.'s "[62, Eq. 8]" and "Figures 3-7" are to this paper, not to Kuran 1991 as the note said (summary 6, section 3 fixed). Its "two ways" to a saddle-node, which the note said it had not read, are filled in from Brummitt et al. [secondary].
- ✓ Kuran 1991, World Politics 44(1) 7-48, 10.2307/2010422 (citation only; unread).
- ✎ Kuran 1995 book: the note said there was no DOI; the JSTOR record 10.2307/j.ctvt1sgqt exists. The two DOIs the note gave are now identified as reviews by Boudon and Hamlin.
- ✎ Brummitt, Barnett and D'Souza 2015, J. R. Soc. Interface 12(112) 20150712, 10.1098/rsif.2015.0712 [read: arXiv 1410.4175]: the note gave it only as an "arXiv physics paper". Now credited by name. It describes the 1989 model with "reputational" and "integrity" utility, not the three-utility scheme of the 1995 book.
- ✎ Rasmusen 1998, JEBO 33, 309-311, 10.1016/S0167-2681(98)90013-0 [read]: citation completed. The example (30/70, intrinsic optimum 20, switch at 59 to 60), the "fades into the background" remark, the expressive/reputational critique and the Bikhchandani-Hirshleifer-Welch remark all match.
- ✓ Schweitzer and Garcia 2010, EPJB 77(4) 533-545, 10.1140/epjb/e2010-00292-1 [read: arXiv 1006.5305]. Eqs (14)-(28) and the Fig. 2 parameters match. The sign finding is confirmed: (15) and (16) are correct, (17) drops the minus sign (the correct result is v² = (gamma_v/h - b1)/b3), and the drift in (18) and the exponent in (19) carry -b3, which is unconfining for b3 = -1. h_i* derivation from (22) re-derived. Whether the published version corrects this is still unconfirmed.
- ✓ Smaldino, Pickett, Sherman and Schank 2012, JASSS 15(4) 7, 10.18564/jasss.2030 [read: jasss.org HTML]. Eqs (1)-(2), N = 3000, k0 = 30, the worked example, L = 50, k0 = 9, and the 2r + 1 neighbourhood all match.
- ✓ Bertozzi, Rosado, Short and Wang 2015, J. Stat. Phys. 158(3) 647-664, 10.1007/s10955-014-1019-6 [read]. Eq. (1), "variant of a classical consensus model", the five weight quantities, and the 14%/12% sentence citing Tsai et al. [40] all match. The three-factor product for w_ij is not in Bertozzi and is now tagged as standard account.
- ✎ Tsai, Bowring, Marsella and Tambe 2011, IVA/LNCS 384-397, 10.1007/978-3-642-23974-8_42: added as the actual source of the 14%/12% figures (unread).
- ✓ Bosse, Duell, Memon, Treur and van der Wal 2009, ECMS 212-218, 10.7148/2009-0212-0218: Crossref confirmed (the note said it was not).
- ✓ Hoogendoorn et al. 2010, 10.1007/978-3-642-17537-4_25; Bosse et al. 2013, AAMAS 27(1) 52-84, 10.1007/s10458-012-9201-1 (authors Bosse, Hoogendoorn, Klein, Treur, van der Wal and van Wissen); Bosse et al. 2015, Cogn. Comput. 7(1) 111-136, 10.1007/s12559-014-9277-9. Citations only.
- ✓ McClelland 2004, IJHCS 60(1) 65-99, 10.1016/j.ijhcs.2003.08.003. The title note is correct; content still unread.
- ✓ Goldenberg, Weisz, Sweeny, Cikara and Gross 2021, Psych. Sci. 32(3) 437-450, 10.1177/0956797620970561. Citation only.
- ✓ Chan 1998, JAP 83(2) 234-246, 10.1037/0021-9010.83.2.234; Bell 2007, JAP 92(3) 595-615, 10.1037/0021-9010.92.3.595; Epstein 2002, PNAS 99 suppl. 3 7243-7250, 10.1073/pnas.092080199. Citations only; the content remains standard account.
- ✎ Gleeson and Cahalane 2007, PRE 75(5) 056103, 10.1103/PhysRevE.75.056103: the note had it as "remembered, not checked". The paper exists as cited (title "Seed size strongly affects cascades on random networks"); the content claim stays unconfirmed.
- ✓ Garcia, Kappas, Küster and Schweitzer 2016, R. Soc. Open Sci. 3(8) 160059, 10.1098/rsos.160059. Citation only; N = 207 not re-read.
- ✎ Lustick and Miodownik (Q&Q 54(2) 413-437, 10.1007/s11135-019-00883-9): now credited by name (the note said only "Springer 2019"). Content unread.
- ✓ Leonardelli, Pickett and Brewer 2010, Adv. Exp. Soc. Psychol. 43, 63-113, 10.1016/S0065-2601(10)43002-6. Citation only.
- ? Steiner 1972, Kozlowski and Klein 2000, McClelland 1993 (via Taylor), Miller 1944, and the 1997 "double-counting" review of Kuran: not checked in this pass. The 1997 review is too vaguely identified to look up.
- ✓ Derived algebra re-checked by hand: the ASCRIBE three-drift decomposition and the beta = 1/2 cancellation (on the unverified standard-account form), the S-G field threshold h_i* = tau gamma_a/(d0 + tau d1), and the S-G sign error.

No fabricated works were found. The web-search budget ran out during this pass, so the "nothing exists" claims (no test of aggregator choice for motivational states; no measured threshold distributions) were **not** re-tested by search and remain the author's.

**Verdict.** The core transcriptions are accurate where re-read: Granovetter, Watts, Schweitzer-Garcia, Smaldino and Bertozzi all match the source text, and the sigma_c computation and the Schweitzer-Garcia sign finding hold up. The main error was in attribution: the Kuran equilibrium (Eq. 8, Figs 3-7, the saddle-node routes) belongs to Kuran's 1989 *Public Choice* paper, not the 1991 *World Politics* paper. The secondary source had been left unnamed and is now credited to Brummitt, Barnett and D'Souza. The note also understated Granovetter's own treatment of falsification, pluralistic ignorance and non-monotone responses. All three are fixed in place.

## Cross-checks (2026-10-29)

Direction D245 checked against the other files in this folder by grep on the works, authors, equations and numbers. Only this file was edited. Web search budget was exhausted, and one fetch of the Bertozzi CAM report failed, so the one contradiction found below is left unresolved at source.

### Agreements

- **Granovetter map and equilibrium (05 section 12; 081 section 1.2; 24 sections 14 and 15).** r(t+1) = F[r(t)], equilibrium F(r) = r at the first crossing from above, stable iff F' < 1, iteration from 0 stops at the first fixed point. All agree with section 1 here. 081 restates 066's monotone convergence and no-oscillation results and cites them to 066.
- **Granovetter's 0..99 example (05 section 12).** Replacing the threshold-1 person with a threshold-2 person leaves "only the instigator" rioting, which matches the equilibrium of 1 in section 1 here. 05 marks the stability criterion as "standard account"; 066 says the same, that Granovetter does not state it.
- **sigma_c (081 sections 1.2 and 2).** Fold at sigma about 12.2, computed 12.222, matches section 1. 081's page cites (1425, 1427) also match.
- **Watts (05 section on Watts, 081 sections 2 and 6).** PNAS 99(9) 5766-5771 and DOI agree. 081 uses Watts's percolation criterion as the sparse-graph replacement for the complete-graph map, as in "Which are equivalent" item 1. 05's "two regimes" is the lower and upper edges of the cascade window here.
- **Epstein as a Granovetter-type threshold (068 section 4; 067 line 143; 24).** 068 derives theta_i = -ln(1 - (g_i - T)/R_i)/k and calls it a Granovetter threshold, with inert and extremist cases. 067 says this is compatible with 066's section 8 line "Granovetter with a state-dependent threshold shift". The citation (PNAS 99 suppl. 3, 7243-7250) agrees.
- **Kuran (068, 067).** Both gloss Epstein's T as Kuran's preference falsification, the hidden-versus-expressed split that section 3 here attributes to Kuran. No file contradicts section 3. 068 also notes that Epstein separates private grievance from public action.
- **Smaldino et al. 2012 (18 section on Smaldino).** Both give d_g = n_g/N, switching to the |d_g - d*| minimiser, and k*(d*) = floor(1/(2d*)) + 1 versus the naive round(1/d*). 18 adds the 0.01 error rate and the d* > 0.5 collapse to one identity, which follow from the formula. 18 says Smaldino and Epstein 2015 repeats the conformity result; 066 does not cover it.
- **Schweitzer and Garcia 2010 (18).** Saturating versus superlinear arousal feedback, bimodal valence and the 207-participant Garcia et al. 2016 test agree. 18 only had the abstract; 066's equations extend it.
- **ASCRIBE and Tsai (18 section 18; 063; 067).** The update rule with eta and beta is identical in 18 and section 5 here. The 14% and 12% per-agent-per-frame figures, the Durupinar comparison and the Bertozzi attribution agree. DOIs for Bosse 2009, Hoogendoorn 2010, Bosse 2013 and Bosse 2015 agree across 18, 063 and 067, and all say the equations were not read at source. 18 gives the Tsai journal version as JAAMAS 2013, doi 10.1007/s10458-013-9220-6, which is the DOI 066 records as the "2013 AAMAS follow-up".
- **McClelland 2004 (18 section 16; 063).** Both use the Crossref title "constructing order from conflict" (063) and flag the older title (18). The virtual controller has summed gain and a reference between the two, with r_v = (G1 r1 + G2 r2)/(G1 + G2) as the standard analysis. All three files say the paper was not read and the source is Taylor's page on McClelland 1993.
- **Static rules (24 sections 8 and 15).** Steiner's additive, disjunctive, conjunctive, compensatory and discretionary types, Chan 1998 (JAP 83(2) 234-246) and Kozlowski and Klein 2000 agree with section 8. Bell 2007 (JAP 92(3) 595-615) agrees. 24's correction that mean, min and max have been tested for team traits is the same finding as summary item 7.
- **Goldenberg et al. 2021 (18).** The result (perceived crowd emotion exceeds the mean, more with more faces and for anger) agrees. 18 left the volume and pages unchecked, and this file supplies them (Psych. Sci. 32, 437-450). No clash.
- **Merged fixed-point theory (081).** 081 reduces drive cascades exactly to the Granovetter map and takes the "w < 0 reverses the inequality" caveat, which agrees with this file's monotonicity requirement and the non-monotone note in section 7.

### Contradictions and tensions

1. **Epstein as a threshold on a population fraction with a fixed-point cascade (here: Summary 1(b) and section 8; there: 068 sections 4 and 5, 067).**
   - Here: Summary 1(b) lists Epstein among "a threshold on a population fraction ... fixed point of a cumulative distribution", and section 8 calls it "Granovetter with a state-dependent threshold shift".
   - There: 068 [read] derives the threshold in the cop-to-active ratio C/A, not the fraction acting. It then scans the homogeneous mean field and finds exactly one fixed point in every case, with no hysteresis or saddle-node. It cites Thron and Jackson that the original response "has no critical crowd size", so no outbursts.
   - Verdict: 068 is right, and the Granovetter equivalence holds only in form. Epstein's original rule has the monotone-threshold structure but a unique mean-field fixed point and none of Granovetter's fold or bandwagon behaviour. The "Granovetter" label in 066 should not be read as implying tipping. Checked against 068's displayed equations and Thron and Jackson as quoted there. I did not re-fetch Thron and Jackson.

2. **Whether Bertozzi confirms the three-factor product for the ASCRIBE weights (here: section 5; there: 18 section 18).**
   - Here: Bertozzi [read] says only that the weights depend on five quantities. The product of sender expressiveness, channel strength and receiver openness is tagged "standard account".
   - There: 18 says, in paraphrase, that both Ntika et al. and Bertozzi et al. were read as confirming the product form of gamma and the consensus core.
   - Verdict: unresolved. A fetch of the UCLA CAM report failed and the search budget was spent. The files can both be right if the product is in Ntika et al. and not in Bertozzi. The weaker claim, that the product form is in at least one read source, is not established here either, because Ntika et al. was not read in this folder's 066 pass.

3. **Granovetter's stability criterion source (05 section 12 and validation line; here: section 1).** 05 gives "stable if F' < 1" under "from abstract/standard account", while 066 gives it as [derived] and not stated in the paper. This is a labelling difference, not a clash. Both say the paper's own stability section supplies no such criterion. 05's validation line "stability condition qualified" is consistent with 066's note that the monotone-convergence limit needs left-continuity.

4. **Watts "rare but large" (05) versus the cascade-size distributions here (section 2).** 05 says global cascades "are rare but large". 066 says the distribution is power-law at the lower edge, so many small ones, and bimodal at the upper edge. Both agree that large cascades are rare toward the upper edge. 05's phrase is a loose summary of the upper regime, and 066 is the more precise. No source check was needed.

## Licences of quoted and transcribed material (2026-10-30)

Licence as determined, and how each source is used. Equations are restated, not copied with surrounding text. Provenance of the reading copies (gwern.net scan of Granovetter, NYU and JSTOR copies of Watts) is not recorded and not confirmed as authorised; reading is not reproduction, but record provenance before going public.

- Granovetter 1978, AJS 83(6): not determined; publisher copyright presumed (University of Chicago Press). Short quotations of vocabulary and phrases (each under 60 words) and restated equations; the eight-item example catalogue is reduced to a description. Wheeler's contagion wording is quoted via Granovetter fn. 2.
- Watts 2002, PNAS 99(9): not determined; publisher copyright presumed (PNAS). Restated equations and short phrases only.
- Kuran 1989 (Public Choice 61(1)), 1991 (World Politics), 1995 (Harvard UP): not determined; publisher copyright presumed. Never read directly; one 9-word quotation taken second-hand via Brummitt et al. 2015; otherwise description.
- Brummitt, Barnett and D'Souza 2015 (arXiv 1410.4175 / J. R. Soc. Interface): not determined; arXiv licence not checked, publisher copyright presumed for the journal version. Short quotations and description.
- Rasmusen 1998 review (JEBO, author preprint at rasmusen.org): not determined; publisher copyright presumed. Description and a worked example, no quotation beyond a phrase.
- Schweitzer and Garcia 2010 (arXiv 1006.5305; EPJ B): not determined; arXiv licence not checked. Restated equations and description.
- Smaldino et al. 2012 (JASSS): not determined; JASSS is open access, licence not checked. Description and restated model.
- Bertozzi et al. 2015 (UCLA CAM report 14-36; J. Stat. Phys.): not determined; publisher copyright presumed. Description.
- McClelland 2004 (IJHCS): not determined; publisher copyright presumed. One 12-word phrase from an academia.edu abstract of unconfirmed identity; licence of that abstract unknown.
- Thron and Jackson (as quoted in sibling file 068): not determined; wording not re-fetched. Six-word quotation; check at source before going public.
- Epstein 2002, ASCRIBE sources (Hoogendoorn, Bosse, Tsai), Gleeson and Cahalane and other cited works: citation only (DOIs and facts); no text reproduced.
- Sibling notes 18, 05, 068: internal and unpublished; paraphrased, no licence issue.
- Datasets: none.
