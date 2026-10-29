# Prior work 05: influence, opinion, diffusion, collective behaviour and their control

Date: 2026-10-29. Cluster survey for `social-algebra`.

## Summary

Almost every model in this cluster has the same skeleton: **operands** are a
vector (or a distribution over vectors) of scalar states, one per person,
and **operators** are a matrix, a pairwise update rule, or a transition
generator acting on that state, with the *influence graph* supplying the
structure. The oldest and cleanest case is French 1956 / DeGroot 1974:
the group is a state vector `x(t)` in R^n, the group structure is a
row-stochastic matrix `W`, and one social "step" is `x(t+1) = W x(t)`.
Everything else is a variation on which of three things is made richer:
the state (vector, discrete spin, threshold, culture vector), the operator
(linear, bounded-confidence nonlinear, stochastic pairwise copy,
threshold step), or the graph (static, state-dependent, networks with
control inputs). There is also a real control literature (driver nodes,
campaign optimisation, influence maximisation) that treats "steering a
group" as a formal problem. What is largely absent is anything that treats
the *interaction types* (who does what to whom: obey, defer, rebuke, ally,
exclude) as a typed, composable set of operators with an algebra of their
own; the models fix one operator and vary the graph. Citations below are
verified for bibliographic existence; the mathematical descriptions of model
structure are my own summaries of the standard forms, not quotations, and
the empirical-record judgements are flagged where I found a source.

Verification key: **[Crossref]** = DOI and details returned by the Crossref
API; **[search]** = confirmed by search results from publisher/repository/
citing sources; **[secondary]** = only seen in citations by other papers.

---

## 1. French (1956), "A formal theory of social power"

- French, J. R. P. Jr. (1956). A formal theory of social power. *Psychological Review* 63(3), 181-194.
- DOI: https://doi.org/10.1037/h0046123 [Crossref]

**Their vocabulary.** Social power, influence, pressure, unanimity, "resultant force", group, opinion on an issue, power of A over B.

**Operands.** Each of n people holds a scalar opinion `x_i` on one issue (French works with a bounded continuous scale). Group state = vector `x in R^n`.

**Operators.** Pairwise "power" weights: person j's influence over i. In the matrix form later standardised, a nonnegative matrix `C` with unit row sums; the opinion update is `x(t+1) = C x(t)` (French's original equations were written in terms of resultant social forces on i; the iterated-averaging form is the standard reading used by Harary and later by DeGroot). Structure: an iterated linear map on R^n; the group's social structure is the graph of nonzero `c_ij`.

**Predictive/control claim.** Predicts when a group reaches unanimity from the structure of the power graph alone, independent of initial opinions. Empirical record: French's own theory was a theoretical sketch; later work (Friedkin-Johnsen) is the empirically tested descendant.

**Limits.** One issue only; static weights; no distinction between kinds of power in the dynamics (the "bases of power" taxonomy, French & Raven 1959, is a separate, non-formal paper); consensus-only prediction.

**Relevance.** The origin of "social structure = matrix, social process = repeated application". Operand = opinion vector; operator = a single, undifferentiated influence matrix. Social-algebra would want that matrix to decompose into named operators.

## 2. Harary (1959), criterion for unanimity in French's theory

- Harary, F. (1959). A criterion for unanimity in French's theory of social power. In D. Cartwright (ed.), *Studies in Social Power*, pp. 168-182, Ann Arbor: Institute for Social Research, University of Michigan.
- Source: cited in Wagner's lecture notes (https://web.math.utk.edu/~cwagner/papers/class1.pdf) and in SIAM (https://epubs.siam.org/doi/10.1137/0121023) [secondary]; the volume exists in the ISR historic publications archive (https://cdn.isr.umich.edu/pubFiles/historicPublications/studiesinsocialpower_1413_.pdf). I did not read the chapter. No DOI.

**Their vocabulary.** Digraph, strongly connected, unanimity, matrix of influence.

**Operands.** Same as French: opinion vector.

**Operators.** Powers of the influence matrix `C^k`; Harary's criterion is a graph-theoretic condition on `C` (in modern terms: convergence of `C^k x` to a common value for all `x` iff the digraph has one closed strongly connected class that is aperiodic). Wagner's notes (search result summary) argue Harary misapplied a classical Markov chain result, whereas Proskurnikov and Tempo (2017, Part I, sec. 3) say French stated his consensus conditions without proof and that they were "later corrected and rigorously proved by Harary". The two secondary accounts disagree; the exact statement is unread here. [validation 2026-10-29]

**Predictive/control claim.** Gives a necessary and sufficient-style structural test for consensus. Mathematical; no empirical claim.

**Limits.** As French. Reported by Wagner to contain a misapplication of Markov chain theory; reported by Proskurnikov-Tempo as the rigorous correction of French's unproved claims. Unresolved.

**Relevance.** Shows the move from "a social theory" to "a theorem about a graph", which is exactly the target form.

## 3. DeGroot (1974), "Reaching a consensus"

- DeGroot, M. H. (1974). Reaching a consensus. *Journal of the American Statistical Association* 69(345), 118-121.
- DOI: https://doi.org/10.1080/01621459.1974.10480137 [Crossref]

**Their vocabulary.** Subjective probability distributions, weights assigned to other group members by perceived expertise, pooling, consensus, Markov chain.

**Operands.** Each of n individuals holds a probability distribution `F_i` (or, in the standard reduction, a scalar belief `p_i`). State = `p(t) in R^n`.

**Operators.** A row-stochastic matrix `W` (`w_ij >= 0`, `sum_j w_ij = 1`), `w_ij` = weight i gives j; update `p(t+1) = W p(t)`, hence `p(t) = W^t p(0)`. Consensus for every initial vector iff `W^t` converges to a rank-one matrix `1 pi^T`; equivalently, the influence digraph has exactly one closed (sink) strongly connected class and that class is aperiodic. For a strongly connected (irreducible) `W` this reduces to aperiodicity, which a single positive self-weight `w_ii > 0` already guarantees. Limit: `p(inf) = 1 pi^T p(0)` where `pi` is the stationary left eigenvector of W, so `pi_j` is j's final "social influence" (a power index).

**Predictive/control claim.** Predicts whether consensus occurs and exactly where it lands; `pi` quantifies each member's leverage. Golub and Jackson (2010), "Naive learning in social networks and the wisdom of crowds", *AEJ: Microeconomics* 2(1), 112-149, DOI 10.1257/mic.2.1.112 [Crossref, validation], is theory: when DeGroot updating aggregates information correctly in large networks. Experimental evidence for DeGroot-*type* updating does exist and should not be understated: Chandrasekhar, Larreguy and Xandri (2020), "Testing models of social learning on networks", *Econometrica* 88(1), 1-32, DOI 10.3982/ECTA14407, find DeGroot-style averaging fits lab-in-field network experiments better than Bayesian learning; Becker, Brackbill and Centola (2017), *PNAS* 114(26), DOI 10.1073/pnas.1615978114, run estimation tasks in which revisions are well described by weighted averaging [both Crossref, validation]. What experiments do not support is DeGroot's *consensus* prediction for real opinion disputes, which is why Friedkin-Johnsen adds stubbornness.

**Limits.** Always consensus in connected aperiodic groups; no stubbornness; weights fixed and exogenous; one issue.

**Relevance.** The canonical linear operator-on-state-vector. `W` is the single operator; its left eigenvector is a derived quantity (a "centrality"). The algebraic fact that the matrices form a semigroup under multiplication is what a social algebra would generalise to many named operators.

## 4. Friedkin and Johnsen, social influence network theory

- Friedkin, N. E. and Johnsen, E. C. (1990). Social influence and opinions. *Journal of Mathematical Sociology* 15(3-4), 193-206 (some listings give 193-205).
- DOI: https://doi.org/10.1080/0022250X.1990.9990069 [Crossref, validation: pages 193-206; scanned reprint at https://escholarship.org/uc/item/2r82w1vs]
- Friedkin, N. E. (1998). *A Structural Theory of Social Influence*. Cambridge University Press. https://resolve.cambridge.org/core/books/a-structural-theory-of-social-influence/5938F144BE35810A377FF3E795A3555C [search]
- Friedkin, N. E. and Johnsen, E. C. (2011). *Social Influence Network Theory: A Sociological Examination of Small Group Dynamics*. Cambridge University Press (Structural Analysis in the Social Sciences 33), ISBN 9781107002463. [search, library records]

**Their vocabulary.** Interpersonal influence, endogenous and exogenous (initial) opinion, susceptibility to interpersonal influence, interpersonal influence network, social influence process, attitude change, group polarisation.

**Operands.** Scalar (or vector for multiple issues) opinions `y_i(t)`, initial opinions `y(1)`, and per-person susceptibility `a_ii`.

**Operators.** `y(t+1) = A W y(t) + (I - A) y(1)`, with `W` row-stochastic (interpersonal influence) and `A = diag(a_1..a_n)` in [0,1] (susceptibility). If `rho(AW) < 1` the iteration converges to the unique fixed point `y* = (I - AW)^{-1}(I - A) y(1)`. In Friedkin's own specification susceptibility is tied to the self-weight, `a_ii = 1 - w_ii`; the general form above treats them as independent. A continuous-time precursor with stubborn/external influence is Taylor (1968), "Towards a mathematical theory of influence and attitude change", *Human Relations* 21(2), 121-139, DOI 10.1177/001872676802100202 [Crossref, validation]. Structure: affine iterated map; the residual attachment to the initial opinion is what permits disagreement at equilibrium. Extension to multiple issues with logical constraints: Friedkin, Proskurnikov, Tempo and Parsegov, "Network science on belief system dynamics under logic constraints", *Science* 354(6310), 321-326 (2016), DOI https://doi.org/10.1126/science.aag2624 [Crossref, validation], which in Kronecker form reads `x(t+1) = ((Lambda W) (x) C) x(t) + ((I - Lambda) (x) I_m) x(0)`, with an m x m matrix C coupling the m issues (the earlier text here had a garbled second term).

**Predictive/control claim.** Predicts the final opinion profile and, in the book, group-decision outcomes, from `W`, `A`, and `y(1)`. Empirical record: the most directly tested model *of opinion change under disagreement* in the cluster, though not the only model with experimental support (see DeGroot, Centola, Bass). Proskurnikov-Tempo (2017, Part I, sec. 6) say, verbatim, that "this model has been experimentally validated for small and medium-size groups", citing Friedkin and collaborators' own work; essentially all of that validation is by Friedkin's group. Not independently checked. The weights `W` are estimated from observed communication/ attention data in those experiments, which weakens "prediction" to "fit with fitted structure".

**Limits.** Linear; weights usually estimated from the data being predicted; single or few issues; no coalition or role differentiation beyond the weights; no negative influence in the basic form.

**Relevance.** The model closest to an *operator that distinguishes a person's type*: `a_ii` is a per-person parameter, i.e. a role-like attribute of an operand. Closest empirical anchor for any operator-table claim.

## 5. Abelson (1964), mathematical models of attitude distribution under controversy

- Abelson, R. P. (1964). Mathematical models of the distribution of attitudes under controversy. In N. Frederiksen and H. Gulliksen (eds.), *Contributions to Mathematical Psychology*, pp. 142-160. New York: Holt, Rinehart and Winston. (Same citation and page range in Proskurnikov-Tempo 2017, ref. [34].)
- Source: BibSonomy record (https://bibsonomy.org/bibtex/91fa5c2add216efab059f6fec9cbd0b1) and a literature review (https://revintsociologia.revistas.csic.es/index.php/revintsociologia/article/view/1023) [search]. Chapter text not read; no DOI. A related earlier simulation, Abelson and Bernstein (1963), is described at CoMSES (https://www.comses.net/codebases/a1a0c5b7-f427-4f32-bd70-60c307b61697/releases/1.0.0/).

**Their vocabulary.** Attitude distribution, controversy, influence, polarisation.

**Operands / operators.** Confirmed from Proskurnikov-Tempo (2017, Part I, sec. 4), not from the chapter itself: the linear Abelson model is `dx_i/dt = sum_j a_ij (x_j - x_i)`, i.e. `dx/dt = -L[A] x` with `L` the weighted Laplacian, the continuous-time counterpart of French-DeGroot; Abelson also proposed nonlinear extensions (coupling that weakens with opinion distance). Abelson proved that the kernel of `L` is spanned by `1` iff the graph is "compact" (in modern terms *quasi-strongly connected*, i.e. has a directed spanning tree), and concluded that this is necessary and sufficient for consensus; his proof covered only diagonalisable Laplacians. Note the condition is quasi-strong connectivity, not mere connectivity. Unlike discrete DeGroot, the continuous model always converges (no periodicity issue).

**Relevance.** Abelson posed the problem; the names are later: "community cleavage problem" (Friedkin 2015, *IEEE Control Systems Magazine* 35(3), 40-51) and "Abelson's diversity puzzle" (Kurahashi-Nakamura, Mas and Lorenz 2016, *JASSS* 19(4), 7), both per Proskurnikov-Tempo. Why do linear influence models predict consensus when real groups do not? That puzzle motivates stubbornness (Friedkin-Johnsen) and bounded confidence.

## 6. Hegselmann and Krause (2002), bounded confidence

- Hegselmann, R. and Krause, U. (2002). Opinion dynamics and bounded confidence: models, analysis and simulation. *Journal of Artificial Societies and Social Simulation* 5(3), 2. https://www.jasss.org/5/3/2.html [search]

**Their vocabulary.** Opinion dynamics, bounded confidence, consensus, polarisation, fragmentation, confidence level epsilon.

**Operands.** Scalar opinions `x_i in [0,1]`.

**Operators.** Synchronous: `x_i(t+1) = (1/|I(i,x(t))|) sum_{j in I(i,x(t))} x_j(t)`, `I(i,x) = { j : |x_i - x_j| <= eps }`. Equivalent to `x(t+1) = A(x(t)) x(t)`: a DeGroot update whose matrix depends on the state (a state-dependent graph). The paper also treats the classical (DeGroot) model, a Friedkin-Johnsen-type variant, and a time-dependent variant (abstract).

**Predictive/control claim.** Predicts, as a function of eps, whether the group ends in consensus, polarisation (two clusters) or fragmentation (many). Pure simulation/analysis; no empirical test in the paper. Later experiments find mixed support: Moussaid, Kammer, Analytis and Neth (2013), "Social influence and the collective dynamics of opinion formation", *PLoS ONE* 8(11), e78433, DOI 10.1371/journal.pone.0078433 [Crossref, validation], observe that people mostly keep their opinion or compromise and that confidence, not just distance, governs the shift.

**Limits.** Homophily is hard-wired as a distance threshold; no network; no roles; outcome depends on initial distribution and eps.

**Relevance.** Shows an operator that is *conditional on the relation between operands* (apply influence only if opinions are close). A social algebra needs conditional / guarded operators of this kind.

## 7. Deffuant, Neau, Amblard and Weisbuch (2000), "Mixing beliefs among interacting agents"

- *Advances in Complex Systems* 3(01n04), 87-98.
- DOI: https://doi.org/10.1142/S0219525900000078 [Crossref]

**Their vocabulary.** Interacting agents, mixing beliefs, threshold, random binary encounters, clusters.

**Operands.** Scalar opinion `x_i`. (Per-agent uncertainty `u_i` belongs to the later "relative agreement" model, Deffuant, Amblard, Weisbuch and Faure 2002, *JASSS* 5(4), not to the 2000 paper; the 2000 paper also has a binary-vector-opinion variant.)

**Operators.** Random pair (i, j) chosen; if `|x_i - x_j| < d` then `x_i <- x_i + mu (x_j - x_i)`, `x_j <- x_j + mu (x_i - x_j)`, `0 < mu <= 1/2`; otherwise nothing. A stochastic pairwise operator, asynchronous, state-guarded.

**Predictive/control claim.** Large threshold d gives convergence to a single average opinion; small d gives several clusters (abstract), roughly `1/(2d)` of them on [0,1]. The 2000 paper is simulation-based; the rate/master-equation analysis is later (Ben-Naim, Krapivsky and Redner 2003, *Physica D*). Not empirically tested in the source.

**Limits / relevance.** As HK but pairwise and stochastic. The unit of dynamics is the *encounter*, a typed pairwise operator, which is the closest bridge to "operators are things people do to one another".

## 8. Voter model: Clifford and Sudbury (1973); Holley and Liggett (1975)

- Clifford, P. and Sudbury, A. (1973). A model for spatial conflict. *Biometrika* 60(3), 581-588. DOI: https://doi.org/10.1093/biomet/60.3.581 [Crossref, validation]
- Holley, R. A. and Liggett, T. M. (1975). Ergodic theorems for weakly interacting infinite systems and the voter model. *Annals of Probability* 3(4), 643-663. DOI: https://doi.org/10.1214/aop/1176996306 [Crossref, validation; title corrected to include "infinite"]. Context: https://en.wikipedia.org/wiki/Voter_model ; Castellano et al. review (below).

**Operands.** Discrete spins `s_i in {0,1}` on the vertices of a graph or lattice Z^d.

**Operators.** Continuous-time Markov process: each site, at rate 1, copies the state of a uniformly chosen neighbour. Generator `L f(s) = sum_i (fraction of neighbours disagreeing with s_i) [f(s^i) - f(s)]` where `s^i` flips site i.

**Predictive/control claim.** Dimension-dependent: in d <= 2 the system coarsens to consensus (probability of seeing two opinions in a finite box tends to 0); in d > 2 there is a one-parameter family of stationary measures indexed by the density of 1s (Holley-Liggett, as quoted in the search result). On finite graphs fixation is certain and the probability of ending at 1 equals the degree-weighted initial fraction of 1s, so *whom you convert first* matters in proportion to degree.

**Limits.** No confidence, no memory, no heterogeneity; purely imitative; the authors framed it as spatial conflict between species (Clifford-Sudbury), not as a social theory. Empirical: Fernandez-Gracia et al. (2014), "Is the voter model a model for voters?", *PRL* 112, 158701, DOI 10.1103/PhysRevLett.112.158701 [Crossref, validation], fit a noisy voter model with recurrent mobility to US county vote-share statistics with some success.

**Relevance.** The minimal stochastic copy operator. Gives a clean example of an operator algebra (duality with coalescing random walks) that social-algebra might want to emulate.

## 9. Weidlich, Sociodynamics

- Weidlich, W. (2000/2002/2006). *Sociodynamics: A Systematic Approach to Mathematical Modelling in the Social Sciences*. Harwood Academic (Amsterdam, 2000); Taylor & Francis (2002); Dover (2006), ISBN 9780486450278. [search: JASSS review https://www.jasss.org/7/4/reviews/lesins.html; Dover https://www.powells.com/book/sociodynamics-9780486450278] Earlier papers (Weidlich, *Physics Reports* 204, 1991) not verified here.

**Their vocabulary.** Sociodynamics, configuration, transition rates, master equation, trend parameters, collective variables, synergetics, "micro-macro".

**Operands.** A *configuration* `n = (n_1..n_K)` of numbers of individuals in K attitudes or states; a probability distribution `P(n,t)` over configurations.

**Operators.** Master equation `dP(n,t)/dt = sum_{n'} [ p(n,n';t) P(n',t) - p(n',n;t) P(n,t) ]` with transition rates `p` typically of the form `nu exp(theta-dependent utility)`, e.g. `p_{ij}(n) = n_i nu_{ij} exp(...)`. Mean-field limit gives nonlinear ODEs for expectation values. Dover's description (search): three parts: modelling concepts, applications (population dynamics, urbanisation, etc.), mathematical methods.

**Predictive/control claim.** Predicts macro-trends, bifurcations and phase transitions in collective attitudes from micro-level transition rates, and has been applied to migration, urban agglomeration, opinion formation. I found no source that assesses empirical fit; fits were largely to aggregate time series (unverified).

**Limits.** Operands are *counts in states*, not individuals with identities; rates are modelled functions, not derived; exchangeability between individuals.

**Relevance.** The right *formalism* for turning a rule set into aggregate predictions, and the best-developed example of "the group as a Markov generator". It forgets who did what to whom.

## 10. Galam, sociophysics

- Galam, S. (2008). Sociophysics: a review of Galam models. *International Journal of Modern Physics C* 19(3), 409-440.
- DOI: https://doi.org/10.1142/S0129183108012297 ; arXiv:0803.1800 [Crossref, validation]

**Their vocabulary.** Sociophysics, majority rule, local rule, hierarchical voting, contrarians, floaters, inflexibles, minority spreading.

**Operands.** Binary opinions `+/-` in a population; fraction `p_t` holding `+`.

**Operators.** Repeated random grouping into groups of size r, then the whole group adopts the local majority (or a tie-breaking bias). Mean-field map: `p_{t+1} = sum_{k > r/2} C(r,k) p_t^k (1-p_t)^{r-k}` (+ tie term). A one-dimensional iterated map with unstable fixed point at the threshold; adding a fraction of inflexible or contrarian agents shifts the threshold.

**Predictive/control claim.** The abstract claims models "successfully predicted" the far right's first-round success in the French presidential election (the abstract says "2000"; the election was in **2002**, an error in the source), fifty-fifty votes in Germany, Italy and Mexico, and the 2005 French "no" to the European constitution. A 2016 Improbable Research post records that the review cites 71 papers, all written or co-written by Galam (https://improbable.com/2016/11/26/galams-work-on-galam-models-reviewed-by-galam/ [fetched, validation]). No independent assessment of the predictions was found. Treat as self-reported.

**Limits.** Binary opinions; mean-field; self-citation; tuning of parameters after the fact.

**Relevance.** Useful *derived* result: tipping thresholds. Majority-rule is a clean example of a group-level operator acting on a set of individuals.

## 11. Castellano, Fortunato and Loreto (2009), statistical physics of social dynamics

- *Reviews of Modern Physics* 81(2), 591-646 (page range corrected from 591-657). DOI: https://doi.org/10.1103/RevModPhys.81.591 ; arXiv:0710.3256 [Crossref, validation]

**Their vocabulary.** Social dynamics, order-disorder transition, universality, opinion dynamics, cultural dynamics, language dynamics, crowd behaviour, hierarchy formation, human dynamics, social spreading.

**Operands / operators.** A taxonomy rather than a model: voter, majority-rule, Sznajd, Ising-type spin models for discrete opinions; bounded confidence (Deffuant, HK) for continuous opinions; Axelrod's model for vector-valued culture; naming game for language. Each is an update rule on a state vector or spin field; analysed with Fokker-Planck and master equations, mean field, and finite-size scaling.

**Predictive/control claim.** The paper's stated aim is to identify universality classes (which microscopic rules give the same macroscopic behaviour). It explicitly calls for comparison with data and notes that this is largely missing (abstract: "comparisons between model results and empirical social data"). The review itself is a valuable index to the 2009 literature.

**Limits.** Physics-style: mean field, identical agents, long-time limits; the empirical programme is called for rather than delivered.

**Relevance.** The best single map of the cluster. Its taxonomy of operators (copy, majority, confidence-bounded averaging, feature-matching adoption, naming) is effectively a first list of candidate social-algebra primitives.

## 12. Granovetter (1978), threshold models of collective behaviour

- *American Journal of Sociology* 83(6), 1420-1443. DOI: https://doi.org/10.1086/226707 [Crossref, validation; JSTOR stable 2778111, Stanford page https://sociology.stanford.edu/publications/threshold-models-collective-behavior]

**Their vocabulary.** Threshold, riot, collective behaviour, equilibrium, instigator, distribution of thresholds.

**Operands.** Each actor i has a threshold `theta_i`: the fraction (or number) of others who must already act for i to act. Group state = the cumulative distribution `F(x)` of thresholds.

**Operators.** Iterated map on the fraction `r` active: `r_{t+1} = F(r_t)`. Equilibria are fixed points `r = F(r)`; for the monotone map, a fixed point is stable if `F'(r) < 1` (F crosses the diagonal from above), and from `r_0 = 0` the process stops at the first fixed point.

**Predictive/control claim.** Two groups with almost identical average thresholds can end in completely different outcomes (Granovetter's example: 100 people with thresholds 0,1,2,...,99 all riot; replace the person with threshold 1 by one with threshold 2 and only the instigator riots); hence aggregate outcomes do not reveal individual dispositions (abstract). Macy and Evtushenko (2020), *Sociological Science* 7, 628-648 ("Threshold Models of Collective Behavior II: The Predictability Paradox and Spontaneous Instigation") revisit and argue outcomes can be fragile and hard to predict [search]. Watts (below) gives the network generalisation.

**Limits.** Well-mixed population; thresholds exogenous and unobservable; no dependence on *who* the others are.

**Relevance.** An operand attribute (threshold) and a guard on an operator ("act iff enough others have acted"). Clear model of why control requires placing the right individual.

## 13. Schelling (1971), dynamic models of segregation

- *Journal of Mathematical Sociology* 1(2), 143-186. DOI: https://doi.org/10.1080/0022250x.1971.9989794 [Crossref]
- Book: Schelling, T. C. (1978). *Micromotives and Macrobehavior*. W. W. Norton. (Not separately verified in this run.)

**Their vocabulary.** Discriminatory choices, neighbourhood, tipping, interactive dynamics, micromotives and macrobehaviour.

**Operands.** Agents of two types on a grid or line, plus empty sites.

**Operators.** An agent with fraction of same-type neighbours below tolerance `tau` moves to a vacant site satisfying its preference. Deterministic or random scheduling; a relocation operator guarded by a local-composition predicate.

**Predictive/control claim.** Strong segregation emerges even when no agent wants it (a mild preference for a modest same-type fraction suffices); described in a JASSS history by Hegselmann (via search) as a family of different models of which one became canonical. Empirical record: the *mechanism* is widely accepted as a demonstration of how micro to macro can mislead; direct empirical calibration to real cities is contested (not investigated here).

**Limits.** Toy; no costs of moving; assumes a particular utility shape.

**Relevance.** The archetype of "macro-pattern is not the sum of micro-intent". For the algebra: a move/avoid operator on operands in a spatial/relational frame.

## 14. Liu, Slotine and Barabasi (2011), controllability of complex networks

- *Nature* 473(7346), 167-173. DOI: https://doi.org/10.1038/nature10011 [Crossref, validation]

**Their vocabulary.** Controllability, driver nodes, structural controllability, maximum matching, degree distribution.

**Operands.** Node states `x in R^N`.

**Operators.** Linear time-invariant system on a directed graph, `dx/dt = A x + B u`; input matrix `B` connects M external signals to "driver" nodes. Structural controllability (Lin 1974): the system is controllable for generic weights iff every node is reached by an input-rooted path and there are no dilations; the minimum number of driver nodes is `N_D = max(N - |M*|, 1)` where `M*` is a maximum matching of the directed graph (one driver when the matching is perfect); drivers are the unmatched nodes.

**Predictive/control claim.** Number of driver nodes depends mainly on degree distribution; sparse heterogeneous networks need many; drivers tend to avoid the hubs (abstract/press release). Applies to **linear** dynamics; the paper's own examples are not social opinion data. Critiques (retrieved in validation, Crossref-confirmed): Cowan, Chastain, Vilhena, Freudenberg and Bergstrom (2012), "Nodal dynamics, not degree distributions, determine the structural controllability of complex networks", *PLoS ONE* 7(6), e38398, DOI 10.1371/journal.pone.0038398, show the result rests on nodes having no self-dynamics; once each node has its own time constant (a self-loop), the self-loops form a perfect matching and **one** driver node suffices, so the degree-distribution conclusion largely dissolves. Muller and Schuppert (2011), "Few inputs can reprogram biological networks", *Nature* 478, E4, DOI 10.1038/nature10543, make a related objection. Yan et al. (2012), "Controlling complex networks: how much energy is needed?", *PRL* 108, 218703, DOI 10.1103/PhysRevLett.108.218703, show structural controllability says nothing about the (often prohibitive) control energy. Social opinion models (DeGroot, FJ) have self-weights, so the Cowan point applies directly to them.

**Limits.** Linear dynamics, known graph, generic weights, ignores energy cost of control; the social interpretation is by analogy.

**Relevance.** Gives a precise sense of "steer the group by acting on a minimal set of members". Combined with DeGroot/Friedkin-Johnsen it gives the control problem in the same notation.

## 15. Control of opinion dynamics and influence maximisation

- Hegselmann, R., Konig, S., Kurz, S., Niemann, C. and Rambau, J. (2015). Optimal opinion control: the campaign problem. *JASSS* 18(3), 18. https://jasss.soc.surrey.ac.uk/18/3/18/18.pdf [search; the author list I was first given omitted Rambau; validation: author list and venue consistent with JASSS]
- Kempe, D., Kleinberg, J. and Tardos, E. (2003). Maximizing the spread of influence through a social network. *Proc. KDD '03*, 137-146. DOI: https://doi.org/10.1145/956750.956769 [Crossref, validation]; journal version *Theory of Computing* 11 (2015), article 4, 105-147.
- Proskurnikov, A. V. and Tempo, R. (2017). A tutorial on modeling and analysis of dynamic social networks. Part I. *Annual Reviews in Control* 43, 65-79. DOI: https://doi.org/10.1016/j.arcontrol.2017.03.002 ; Part II (2018), vol. 45, 166-190, DOI: https://doi.org/10.1016/j.arcontrol.2018.03.005 ; arXiv:1701.06307, 1801.06719 [Crossref, validation]

**Their vocabulary.** Optimal control, campaign, strategic agent, broadcast opinion, model predictive control; seed set, independent cascade, linear threshold, influence function; multi-agent systems, consensus.

**Operands.** Opinion vector under bounded confidence (campaign problem); active/inactive node set (influence maximisation).

**Operators.** Campaign: HK dynamics plus one strategic agent whose broadcast opinion `u(t)` is a control input chosen to maximise the number of agents in a target interval at horizon T. Influence maximisation: choose seed set S, |S| = k, to maximise expected spread `sigma(S)` under independent cascade (each edge fires once with probability `p_uv`) or linear threshold (node u activates when sum of in-weights from active neighbours >= a random threshold `theta_u`). `sigma` is monotone and submodular in both models, so greedy gives a `(1 - 1/e)` (about 63%) approximation by the Nemhauser-Wolsey-Fisher theorem (Kempe et al.); in practice `sigma` must itself be estimated by simulation, giving `(1 - 1/e - eps)`, and exact computation of `sigma` was later shown #P-hard (Chen, Wang and Wang 2010, not checked here).

**Predictive/control claim.** Campaign problem: even a ten-period problem with eleven agents is very hard; mixed-integer linear programming finds global optima and model predictive control can be well away from the optimum (search summary of the Bayreuth working paper). Influence maximisation: provable approximation guarantees; selecting the best seeds is NP-hard. Empirical: influence maximisation works algorithmically on recorded cascades; claims of real-world persuasion effect sizes are a separate, weaker literature (not checked).

**Limits.** All assume the model is the true dynamics. The authors of the campaign paper explicitly note moral and political concerns about optimal opinion control.

**Relevance.** The only place in the cluster where "controlling a group" is a stated formal problem. The Proskurnikov-Tempo tutorials are the best single survey bridging sociology and control theory.

## 16. Helbing, social force model of crowds

- Helbing, D. and Molnar, P. (1995). Social force model for pedestrian dynamics. *Physical Review E* 51(5), 4282-4286. DOI: https://doi.org/10.1103/physreve.51.4282 [Crossref]
- Helbing, D., Farkas, I. and Vicsek, T. (2000). Simulating dynamical features of escape panic. *Nature* 407, 487-490. DOI: https://doi.org/10.1038/35035023 ; arXiv:cond-mat/0009448 [Crossref, validation]

**Their vocabulary.** Social force, desired velocity, repulsive interaction, panic, "faster is slower", lane formation.

**Operands.** Position and velocity of each pedestrian, `(r_i, v_i) in R^4`.

**Operators.** Newtonian: `m_i dv_i/dt = m_i (v_i^0 e_i - v_i)/tau_i + sum_j f_ij + sum_W f_iW`, where `f_ij` is a (partly psychological) repulsion with exponential decay in distance plus contact forces. Coupled ODEs; no graph but a metric.

**Predictive/control claim.** Reproduces lane formation, bottleneck oscillations, and clogging under panic; design implications for exits (e.g. a column before an exit). Empirical record: qualitative phenomena are reproduced; quantitative calibration to field data is variable, and the model was revisited by Helbing himself (collective-dynamics.eu A168, "What have we learnt since then?") [search]. Not a model of social relations.

**Limits.** Physical space only; a "social force" is not a social relation.

**Relevance.** Shows that the *same* formal approach works when the "social" is geometry; marks the boundary of the cluster.

## 17. Pentland (2014), Social Physics

- Pentland, A. (2014). *Social Physics: How Good Ideas Spread, the Lessons from a New Science*. New York: Penguin Press, ISBN 978-1-59420-565-1. [search: Publishers Weekly]

**Their vocabulary.** Idea flow, social learning, engagement, exploration, "honest signals", reality mining.

**Operands.** People as nodes in an interaction network reconstructed from sensor, phone and transaction logs; ideas as flows.

**Operators.** Mostly statistical: measured *exploration* (contact with new sources) and *engagement* (density of contact within a group) are used as predictors of group performance and idea spread. Not a closed set of dynamical equations in the book.

**Predictive/control claim.** Claims that patterns of communication (e.g. turn-taking, energy) predict team performance independently of content, and that incentives to peers (social network incentives) change behaviour more than individual incentives; supporting studies are authored by Pentland's group. I did not check the underlying papers; treat the strength of claims as unassessed.

**Limits.** A popular book; the formal content is in the cited papers; privacy and consent are a significant caveat.

**Relevance.** The only item here that works from measured data on real groups at scale; useful for what to measure, not for the algebra.

## 18. Turchin, cliodynamics

- Turchin, P. (2003). *Historical Dynamics: Why States Rise and Fall*. Princeton University Press. https://press.princeton.edu/books/hardcover/9780691116693/historical-dynamics [search]
- Turchin, P. and Nefedov, S. A. (2009). *Secular Cycles*. Princeton University Press, ISBN 978-0-691-13696-7. https://press.princeton.edu/node/52401 [search]
- Turchin, P. (2008). Arise "cliodynamics". *Nature* 454(7200), 34-35. DOI: https://doi.org/10.1038/454034a [Crossref; confirmed year is 2008, not 2010 as the brief assumed; the 2010 *Nature* item is the separate prediction letter below]

**Their vocabulary.** Cliodynamics, asabiya, demographic-structural theory, elite overproduction, secular cycles, sociopolitical instability.

**Operands.** Aggregate variables: population, per-capita resources, elite number, state strength, instability index.

**Operators.** Coupled ODEs / difference equations (population-resource dynamics, predator-prey style; the "metaethnic frontier" asabiya model of collective solidarity with diffusion and a threshold). Aggregate mechanisms, not individuals.

**Predictive/control claim.** Predicts the timing of recurring waves of breakdown in agrarian states and tests with historical series (England, France, Russia, Rome); the publisher descriptions say so. Turchin also made a public prediction of rising US instability around 2020: Turchin (2010), "Political instability may be a contributor in the coming decade", *Nature* 463, 608, DOI 10.1038/463608a [Crossref, validation]; whether events vindicated it is contested and not assessed here. Independent assessments of the quantitative record were not retrieved.

**Limits.** Few cycles per case, many parameters, retrospective fit; aggregate level only.

**Relevance.** Shows what the "group" level looks like when the operands are classes (elite, commoner, state) rather than people. A candidate scale for typed operands.

## 19. Rashevsky, mathematical biology of social behaviour

- Rashevsky, N. (1947). *Mathematical Theory of Human Relations: An Approach to a Mathematical Biology of Social Phenomena*. Bloomington, Indiana: Principia Press, xiv+202 pp. Wellcome Collection record: https://content.www.wellcomecollection.org/works/ypbvwu6m [search]
- Rashevsky, N. (1951). *Mathematical Biology of Social Behavior*. University of Chicago Press, xii+256 pp. Nature listing: https://www.nature.com/articles/170003a0 [search]; AMS review of the 1947/1949 work: https://www.ams.org/bull/1949-55-07/S0002-9904-1949-09260-1 [search]

**Their vocabulary.** Mathematical biology, human relations, social behaviour, "neural" threshold units, cooperation/competition.

**Operands / operators.** Existence of the research programme confirmed (validation): a *Psychometrika* series from 1939 onward, "Studies in the mathematical theory of human relations" and "Further studies on the mathematical theory of interaction of individuals in a social group", which includes models of one group controlling another. The specific characterisation (excitation/inhibition variables of neural type driving imitative choice between two behaviours, aggregated to population equations) is from background knowledge and remains **unconfirmed**. Neither book was read.

**Predictive/control claim.** None retrieved. The programme is generally regarded as influential in kind (mathematical sociology, mathematical biophysics) but not for specific predictive success.

**Relevance.** Historical priority for "write the group as a coupled dynamical system with typed interaction terms".

## 20. Simon (1952), formal theory of interaction in social groups

- Simon, H. A. (1952). A formal theory of interaction in social groups. *American Sociological Review* 17(2), 202-211.
- DOI: https://doi.org/10.2307/2087661 [Crossref returned volume 17, start page 202, April 1952; DOI string in the brief (2088835) was wrong]. Context: a dissertation abstract (https://archives.albany.edu/description/catalog/ua435aspace_48b5c66d577e79547709784dca9799d8) says Simon formulated a model of Homans' postulates and focused on stability. [search]

**Their vocabulary.** Interaction, activity, friendliness, sentiment, external system, internal system (Homans's terms), equilibrium.

**Operands / operators.** Four group-level variables: interaction I, friendliness F, activity A, and externally imposed activity E (Homans, *The Human Group*, 1950). Corrected in validation: not every variable has its own rate equation. In the linear model, as usually reproduced (e.g. Simon's *Models of Man*, 1957), interaction adjusts instantaneously, `I = a1 F + a2 A`, while `dF/dt = b (I - beta F)` and `dA/dt = c1 (F - gamma A) + c2 (E - A)`; the analysis is about equilibrium, stability and comparative statics. That exact form is from background knowledge (**unconfirmed**). Confirmed from a secondary source (Montgomery's lecture notes, users.ssc.wisc.edu/~jmontgom/twodimmodels.pdf): Simon focused mostly on a linear model **but also discussed a nonlinear version**, which the notes write as `dF/dt = A - beta F^2`, `dA/dt = F + xi - gamma A^2` with `xi` the external activity.

**Predictive/control claim.** Deduces which qualitative changes follow from perturbing one variable (e.g. increasing external demands). No empirical test in Simon's paper.

**Limits.** Four group-level aggregates; no individuals; mainly linear (the nonlinear case is treated qualitatively).

**Relevance.** Direct precedent: a verbal sociological theory translated into an equation system *so its consequences can be derived*. It also shows the cost of aggregation.

## 21. Coleman, mathematical sociology and the linear system of action

- Coleman, J. S. (1964). *Introduction to Mathematical Sociology*. New York: Free Press of Glencoe (and Collier-Macmillan), xiv+554 pp. [search: library records, CASBS]
- Coleman, J. S. (1990). *Foundations of Social Theory*. Cambridge, MA: Belknap Press of Harvard University Press, 993 pp., ISBN 0-674-31225-2. [search: library record]

**Their vocabulary.** Actors, events, resources, control, interest, rights, exchange, "linear system of action", norm, authority, trust.

**Operands.** Actors `i` and events or resources `j`, with a matrix of *control* `c_ij` (share of control of j held by i) and *interest* `x_ij`.

**Operators.** The equations previously given here were garbled and have been replaced (validation). The standard form, from background knowledge and **unconfirmed** against the book: with `C` the actors-by-events control matrix (columns sum to 1) and `X` the events-by-actors interest matrix (each actor's interests sum to 1), the value of event j is `v_j = sum_i x_ji r_i` and the power (resources) of actor i is `r_i = sum_j c_ij v_j`; hence `r = C X r`, so power is the stationary eigenvector of the stochastic matrix `CX`, structurally the same object as DeGroot's `pi`. The model predates 1990 (Coleman's 1966 *AJS* paper on collective decisions and *The Mathematical Study of Collective Action*, 1973; not checked).

**Predictive/control claim.** Equilibrium prices and actor power from `C` and `X`. Not widely used for empirical prediction; its influence is as the foundation of rational-choice sociology.

**Limits.** Rational-actor, exchange-only, equilibrium, strong aggregation.

**Relevance.** Coleman's actors/resources/control/interest matrices are an explicit operand-operator grammar for *transfer of control*, the closest thing in the cluster to "operators are things done to one another" (transfer, delegate, trust).

## 22. Bass (1969), new product growth

- *Management Science* 15(5), 215-227. DOI: https://doi.org/10.1287/mnsc.15.5.215 (reprint with commentary 2004, DOI 10.1287/mnsc.1040.0264, *Management Science* 50(12 suppl.), 1825-1832) [Crossref, validation; the 1969 title as registered reads "A New Product Growth for Model Consumer Durables", a long-standing typo for "Model for"]

**Their vocabulary.** Innovators, imitators, coefficient of innovation p, coefficient of imitation q, adoption.

**Operands.** Cumulative fraction of adopters `F(t)` in a population with market potential m.

**Operators.** `dF/dt = (p + q F)(1 - F)`; closed form (with `F(0) = 0`) `F(t) = (1 - e^{-(p+q)t}) / (1 + (q/p) e^{-(p+q)t})`. One ODE, two parameters (three with m). [Equation and closed form checked in validation.]

**Predictive/control claim.** Fitted to eleven consumer durables, and used for forecasting colour-TV sales (abstract). It fits adoption curves well retrospectively and has one of the largest empirical records of any model in this cluster (decades of marketing applications); early-data forecasting is unstable in p, q (well known; not sourced here).

**Limits.** Homogeneous mixing; no network; a market, not a group.

**Relevance.** The aggregate limit of a threshold/contagion model; shows a minimal two-operator split: external (innovation) vs internal (imitation).

## 23. Additions

- Axelrod, R. (1997). The dissemination of culture: a model with local convergence and global polarization. *Journal of Conflict Resolution* 41(2), 203-226. DOI: https://doi.org/10.1177/0022002797041002001 [Crossref, validation]. **Operands:** culture vector of F features, each with q traits. **Operator:** pick neighbours i, j; with probability equal to the fraction of features on which they already agree, copy one differing feature. Predicts stable cultural regions; a globalisation-polarisation (order-disorder) transition in q found later by Castellano, Marsili and Vespignani (2000), *PRL* 85, 3536, DOI 10.1103/PhysRevLett.85.3536 [Crossref, validation]. Relevance: the only model here where the operand is a *vector of attributes* and the interaction is conditioned on similarity of the whole vector.
- Watts, D. J. (2002). A simple model of global cascades on random networks. *PNAS* 99(9), 5766-5771. DOI: https://doi.org/10.1073/pnas.082090499 [Crossref, validation]. Granovetter thresholds on a sparse random graph; global cascades occur in two regimes and are rare but large. Relevance: threshold rule plus network gives *which* seeds matter.
- Centola, D. and Macy, M. (2007). Complex contagions and the weakness of long ties. *American Journal of Sociology* 113(3), 702-734. DOI: https://doi.org/10.1086/521848 [Crossref]. Adoption needs confirmation from several sources; long ties can impede diffusion; bridges must be wide. Relevance: contagion operators come in at least two kinds (simple: one source suffices; complex: k sources needed), which is typed-operator thinking.
- Centola, D. (2010). The spread of behavior in an online social network experiment. *Science* 329(5996), 1194-1197. DOI: https://doi.org/10.1126/science.1185231 [Crossref, validation; added]. A controlled experiment: health-behaviour adoption spread further and faster on clustered-lattice networks than on random ones, as complex contagion predicts. One of the few *experimental* tests of a diffusion mechanism in this cluster.

---

## Unconfirmed

- **Abelson (1964):** chapter not read; the Laplacian model and the "compact" (quasi-strongly connected) consensus condition are now confirmed from Proskurnikov-Tempo 2017 (validation), so this is secondary-confirmed rather than unconfirmed. The nonlinear variants are not detailed here.
- **Rashevsky:** books and the *Psychometrika* series exist; the excitation/imitation characterisation is from memory and unconfirmed.
- **Simon (1952):** variables and the linear-plus-nonlinear structure confirmed from a secondary source; the exact linear equations (with I algebraic, not a rate equation) are from background knowledge.
- **Coleman:** the original equations here were garbled and were replaced in validation by the standard `r = CXr` form, which is from background knowledge and not checked against the book.
- **Harary (1959):** exact theorem statement not read; two secondary sources disagree on whether it corrects or misapplies the Markov-chain result.
- **Sznajd (2000) majority-rule model, Latane social impact theory, Holme-Newman coevolution, Hegselmann-Krause 2005/2006 follow-ups, Acemoglu-Ozdaglar-ParandehGheibi 2010 "Spread of (mis)information":** known to belong in this cluster, not searched this run. Not cited. (Golub-Jackson 2010 now cited under DeGroot.)
- **Missing work flagged in validation (important, not yet surveyed):** Altafini (2013) signed networks / antagonistic interactions (*IEEE TAC* 58(4)) — directly relevant because it adds *negative* influence, a second operator type; structural balance (Heider 1946; Cartwright and Harary 1956), which is the formal theory of signed relations and arguably belongs here or in a relations cluster; Friedkin-Bullo (2017, *PNAS*) on opinion dynamics along issue sequences (reflected appraisal, endogenous `W`); Jia, MirTabatabaei, Friedkin and Bullo (2015, *SIAM Review*) on the DeGroot-Friedkin model of evolving social power; Acemoglu and Ozdaglar (2011) survey of opinion dynamics and learning; Latane (1981) social impact. None checked here.
- **Schelling (1978) book, Pentland's underlying papers, Friedkin-Johnsen's experimental validation data, Galam's alleged predictions:** not independently checked.
- **Helbing and Molnar 1995 quantitative validation** and the **empirical status of bounded confidence** in experiments: not retrieved.

---

## What this cluster already covers

1. **A mature, exact formal language for "state vector plus influence graph".** DeGroot, French, Friedkin-Johnsen and Hegselmann-Krause are the same object: a map on R^n with a structure matrix. Consensus, polarisation and fragmentation are theorems, not guesses.
2. **Operators that are guarded by a relation between operands** (bounded confidence, thresholds, Axelrod similarity, Schelling tolerance), and **operators that are stochastic pairwise events** (Deffuant, voter).
3. **Operators with individual parameters** (Friedkin-Johnsen susceptibility, Granovetter thresholds): a minimal typing of operands.
4. **Aggregation machinery:** master equations (Weidlich), mean-field maps (Galam, Granovetter, Bass), universality classes (Castellano et al.).
5. **A formal control theory of groups:** driver nodes (Liu et al.), campaign optimisation and influence maximisation (Hegselmann et al., Kempe et al.), control-theoretic survey (Proskurnikov-Tempo).
6. **Good precedent for turning verbal sociology into equations** (Simon on Homans, Coleman, Rashevsky).
7. **Some empirical anchors:** Friedkin-Johnsen small-group experiments (per reviews; mostly by Friedkin's group), DeGroot-style updating in network experiments (Chandrasekhar et al. 2020; Becker et al. 2017), Centola's 2010 complex-contagion experiment, the Bass model's long forecasting record, and partial voter-model fits to election data. (Corrected in validation: earlier text named Friedkin-Johnsen as the single anchor.)

## What it does not cover

1. **Typed, named interaction operators.** Nearly every model has *one* operator (average, copy, majority, threshold-step) and varies the graph or the parameters. Nothing here distinguishes "defer", "command", "ally against", "exclude", "mediate", "reward", "shame" as separate operators and asks how they compose. Coleman's control/interest/transfer is the closest, and it is a single exchange scheme.
2. **Composition and algebraic structure of the operators themselves.** The linear models give a semigroup of stochastic matrices as a by-product, and the voter model has a duality, but nobody here asks what the *set of social acts* closes under, which commute, which have inverses.
3. **Roles, offices, and group types as first-class operands.** Operands are people with a scalar, or aggregate counts. A role (parent, chair, foreman) as a position that different people fill, with operators attached to the position, is absent.
4. **Relations as operands.** Edges are fixed weights or parameters, not states that are themselves changed by operators (a few coevolution models, not surveyed here, do part of this).
5. **Multi-issue, multi-valued, and logical structure** apart from Friedkin et al. 2016 and Axelrod.
6. **Empirical grounding.** Most models, especially the physics-style ones (HK, Deffuant, Galam, Axelrod, Schelling as a social claim), are validated mainly by their own simulations, and Castellano et al. say as much. The exceptions are listed under "covers" item 7; Friedkin-Johnsen is the best-tested model of *persistent disagreement*, but it is not alone in having experimental support. Galam's and Turchin's predictive claims are self-reported and should be treated as such until independently checked.
7. **Individual intent and strategy.** Agents are mechanical updaters; the campaign problem adds one strategic agent, but a group of mutually strategic agents with operators chosen by the actors belongs to game theory and is another cluster's job.

## Validation log (2026-10-29)

Bibliographic details were re-checked against Crossref where a DOI exists; formal claims against standard results and, where flagged, Proskurnikov-Tempo 2017 Part I and Montgomery's lecture notes.

- French 1956: ✓
- Harary 1959: ✎ corrected (added the conflicting Proskurnikov-Tempo account; theorem statement still unread, ? for exact wording)
- DeGroot 1974: ✎ corrected (consensus condition restated precisely: one closed class, aperiodic; Golub-Jackson verified and described as theory; experimental support for DeGroot-type updating added)
- Friedkin-Johnsen 1990 / Friedkin 1998 / 2011: ✎ corrected (Science 2016 DOI confirmed; garbled Kronecker equation fixed; a_ii = 1 - w_ii convention noted; "best-tested" narrowed to persistent-disagreement models and noted as self-validated; Taylor 1968 added)
- Abelson 1964: ✎ corrected (equation confirmed via secondary source; condition is quasi-strong connectivity, not connectivity; puzzle names attributed to later authors)
- Hegselmann-Krause 2002: ✓ (empirical note given a source: Moussaid et al. 2013)
- Deffuant et al. 2000: ✎ corrected (uncertainty u_i belongs to the 2002 relative-agreement model; master-equation analysis is later work)
- Clifford-Sudbury 1973 / Holley-Liggett 1975: ✎ corrected (H-L title missing "infinite"; DOI added; empirical voter fit added)
- Weidlich: ✓ (books; content standard)
- Galam 2008: ✎ corrected (the "2000" French election is a 2002 event misdated in Galam's own abstract; full claim list; 71-self-citation figure confirmed)
- Castellano et al. 2009: ✎ corrected (pages 591-646, not 591-657)
- Granovetter 1978: ✎ corrected (riot example misdescribed; stability condition qualified)
- Schelling 1971: ✓
- Liu-Slotine-Barabasi 2011: ✎ corrected (N_D = max(N - |M*|, 1); critiques added: Cowan et al. 2012 self-loop argument, Muller-Schuppert 2011, Yan et al. 2012 control energy)
- Hegselmann et al. 2015 campaign problem: ✓
- Kempe-Kleinberg-Tardos 2003: ✓ (1 - 1/e grounded in Nemhauser-Wolsey-Fisher; simulation caveat added)
- Proskurnikov-Tempo 2017/2018: ✓
- Helbing-Molnar 1995 / Helbing-Farkas-Vicsek 2000: ✓
- Pentland 2014: ✓ (citation; claims remain unassessed)
- Turchin 2003 / 2009 / 2008: ✓ (2010 prediction letter added)
- Rashevsky 1947 / 1951: ? unconfirmed (model content from memory; programme existence confirmed)
- Simon 1952: ✎ corrected (interaction is algebraic, not a rate equation; a nonlinear version exists, so "linear" in Limits was wrong); exact linear coefficients ? unconfirmed
- Coleman 1964 / 1990: ✎ corrected (garbled price equations replaced with r = CXr form); ? unconfirmed against the book
- Bass 1969: ✓ (equation and closed form correct; 2004 reprint pages added; empirical record upgraded)
- Axelrod 1997: ✓ (transition attributed to Castellano-Marsili-Vespignani 2000)
- Watts 2002: ✓
- Centola-Macy 2007: ✓; Centola 2010 experiment added
- No fabrications found; nothing removed.

**Verdict.** Bibliographically the survey is reliable: every DOI checked resolves to the stated work, and the errors were small (one page range, one title word, one misdated election inherited from the source). The mathematics of the core linear and stochastic models was sound; the errors were in the from-memory items (Coleman's equations were garbled, Simon's structure was misdescribed) and in two details (Deffuant's uncertainty, Granovetter's example). The most consequential problem was the empirical framing: the claim that Friedkin-Johnsen alone has real experimental support was overstated and is now corrected, and the Liu et al. control result is far weaker for social systems than the survey implied once the self-loop critique is taken into account.
