# Prior work, cluster 30: ecological stability and resilience theorems

Date: 2026-10-29. Strand: social-algebra. Aim (Aldred): an algebra of basic human and group drives, composed into equations, from which theorems follow, used to predict or control behaviour. This file asks one question of community ecology and resilience theory: **which theorems about systems of many interacting parts could a group-drive algebra inherit, and what would each cost?** Cluster 09 covers evolutionary game theory, Price, SIR; this file does not repeat them.

## Verification status

- Every DOI below was resolved at api.crossref.org on 2026-10-29 and the title, first author and year matched. Two initial guesses were wrong and are corrected (Quirk & Ruppert is 10.2307/2295838, not ...837; Wichers is 10.1159/000441458).
- Nature and Science pages are paywalled to the fetch tool. For the abstracts quoted I used Europe PMC's abstract text and tag **[read: abstract]**. Everything else is **[from abstract/standard account]**: textbook form from general knowledge, not re-derived from the paper's full text. No paper below was read in full.
- Items I could not resolve are under "Unconfirmed".

## Summary

1. Ecology has the one thing the aim needs and cluster 09 lacked: **theorems of the form "a system built from many coupled parts of such-and-such interaction structure is (un)stable with probability p, as a function of size, connectance and coupling strength"**. The object is the community matrix, a signed real matrix of pairwise effects. The theorems are about its eigenvalues.
2. The drive-coupling matrix of a group is a natural analogue, but the analogy is only as good as the linearisation: it needs an equilibrium, small perturbations, and entries that can be estimated. Nothing in the ecology literature supplies those entries for humans; psychology does estimate them for one person (VAR) and for dyads (Gottman, coupled oscillators; see 20 and 27), but not for groups. (Corrected in validation.)
3. Resilience theory (alternative stable states, hysteresis, early-warning signals) is the part with real human transfers, and the only part tested on human data: mood time series (van de Leemput 2014; Wichers 2016). The tests are about individuals' affect, not group drives.
4. The adaptive cycle and panarchy are narrative frameworks, not theorems. Do not count them as inheritable mathematics.
5. Niche construction is the one genuinely formal piece about agents modifying the environment that feeds back on them. Its equations are two-locus population genetics with an environment variable; the transferable idea is the extra feedback term, not the equations.

---

## A. Community matrix, local stability, and May's criterion

### A1. The community (interaction) matrix and the Jacobian of generalised Lotka-Volterra (Levins 1968; May 1972)

- Source: R. Levins, *Evolution in Changing Environments*, Princeton UP, 1968. DOI 10.1515/9780691209418. [from standard account]
- **Object.** Populations x_i obey dx_i/dt = x_i f_i(x). At an equilibrium x*, linearise: d(delta x)/dt = M delta x with M_ij = x*_i (partial f_i / partial x_j) at x*. For generalised Lotka-Volterra, f_i = r_i + sum_j A_ij x_j, so M_ij = x*_i A_ij: the community matrix is the interaction matrix scaled row-wise by equilibrium abundance. The sign of M_ij is the type of effect of j on i (+/-), and the pair (sign M_ij, sign M_ji) classifies the interaction: (-,+) predation, (-,-) competition, (+,+) mutualism.
- **Theorem (standard linear stability).** The equilibrium is locally asymptotically stable iff every eigenvalue of M has negative real part. Local only: says nothing about large perturbations, other equilibria, or non-equilibrium dynamics.
- **Assumptions.** An interior equilibrium exists and is feasible (all x*_i > 0); small perturbations; the functional form of the dynamics is known or at least its Jacobian is.
- **Empirical standing.** Estimating M from field data is hard and rarely done for large webs; measured M for real communities is mostly built from allometric or trophic assumptions. [from standard account]
- **Operand/operator translation.** Operands: drive levels of persons and groups (x). Operator: the coupling matrix M, whose (i,j) entry is how a unit of drive j changes the growth of drive i. "Stable" means a perturbed group returns to its equilibrium drive profile. The algebra gets a typed classification of drive-pair couplings by sign pair for free: (-,+) drive exploits drive, (-,-) drives that mutually inhibit, (+,+) drives that mutually reinforce.
- **Cost.** Needs a dynamical law for drive levels, so a differential equation per drive, which is the reopened Q4 (discrete vs real-valued drives).

### A2. May 1972, "Will a Large Complex System be Stable?"

- Citation: R. M. May, Nature 238, 413-414 (1972). DOI 10.1038/238413a0. Resolved at Crossref; abstract not available to me.
- **Statement.** [from standard account] Take S species, community matrix M = -I + B (diagonal -1: each species self-limits at unit rate after rescaling), where each off-diagonal entry is, independently, nonzero with probability C (the connectance) and then drawn from a distribution with mean 0 and variance sigma^2. In the limit of large S the eigenvalues of B fill a disc of radius sigma*sqrt(S*C) (a Wigner/Girko-type circular law). Hence the system is stable with probability tending to 1 if sigma*sqrt(S*C) < 1, and unstable with probability tending to 1 if sigma*sqrt(S*C) > 1. The transition is sharp.
- **Reading.** Complexity (S, C, interaction strength sigma) destabilises: for fixed strength, a stable system can hold only about 1/(sigma^2 C) species. This reversed the then-received wisdom (MacArthur, Elton) that diversity begets stability. Precursor: Gardner & Ashby 1970, "Connectance of Large Dynamic (Cybernetic) Systems: Critical Values for Stability", Nature 228, 784, DOI 10.1038/228784a0 (Crossref-resolved), found by simulation that stability collapses past a critical connectance.
- **Assumptions.** Interactions are random, independent, zero-mean; self-regulation is uniform; local stability; large S. All of these are false for real communities.
- **Empirical standing.** The result is a mathematical theorem under its assumptions. It is a null model: its role is to show what randomness gives, and real systems beat it because they are not random. McCann 2000, "The diversity-stability debate", Nature 405, 228, DOI 10.1038/35012234 (Crossref-resolved), reviews how structured real systems evade it. [from standard account]
- **Operand/operator translation.** Operands: drives. Operator: random coupling. Meaning for a group: if a group has S distinct active drive-carriers (persons x drives) each coupled to a fraction C of the others at strength sigma, **the group is stable only while sigma*sqrt(S*C) < 1**. Larger groups, or denser couplings, need weaker couplings or more self-limitation (drive saturation, norms). This is a precise, inheritable scaling law: size times density times strength.
- **Human transfer.** No study found applies May's criterion to a *measured* human drive or influence matrix. The argument has been applied theoretically to human economic systems (Haldane & May 2011 on banks; Moran & Bouchaud 2019 on large economies; see "What exists vs what does not").
- **Check of the statement.** Correct as stated. With M = -I + B and B's nonzero entries of variance sigma^2 at density C, each entry of B has variance C sigma^2, so by the circular law the spectrum of B fills a disc of radius sqrt(S C sigma^2) = sigma*sqrt(SC); the rightmost eigenvalue of M is then ≈ -1 + sigma*sqrt(SC). May's 1972 argument was heuristic (he leaned on Wigner); the rigorous circular law for general iid entries is Tao & Vu 2010.

### A3. Allesina & Tang 2012, structure-specific stability criteria

- Citation: S. Allesina and S. Tang, "Stability criteria for complex ecosystems", Nature 483, 205-208 (2012). DOI 10.1038/nature10832.
- **[read: abstract]**: "we extend May's results to these relationships and find remarkable differences between predator-prey interactions, which are stabilizing, and mutualistic and competitive interactions, which are destabilizing. We provide analytic stability criteria for all cases ... the probability of stability for predator-prey networks decreases when a realistic food web structure is imposed or if there is a large preponderance of weak interactions. Similarly, stability is negatively affected by nestedness in bipartite mutualistic networks ... Stable predator-prey networks can be arbitrarily large and complex, provided that predator-prey pairs are tightly coupled. The stability criteria are widely applicable, because they hold for any system of differential equations."
- **Mathematical form** [read: arXiv preprint 1105.2071v1 of the same paper, full text; notation may differ slightly from the Nature version]. Diagonal -d; each pair (M_ij, M_ji) nonzero with probability C; magnitudes half-normal |N(0, sigma^2)|, so E|X| = sigma*sqrt(2/pi). Let tau = E[M_ij M_ji]/sigma^2 over interacting pairs. By the elliptic law (Sommers et al. 1988) the bulk eigenvalues of the off-diagonal part fill an ellipse with horizontal semi-axis sigma*sqrt(SC)*(1+tau) and vertical semi-axis sigma*sqrt(SC)*(1-tau), centred at -d. Stability needs the horizontal semi-axis < d. Criteria:
  - Random (May): tau = 0, sigma*sqrt(SC) < d.
  - Predator-prey (each linked pair has opposite signs, which partner is positive chosen at random): tau = -(E|X|)^2/sigma^2 = -2/pi, so **sigma*sqrt(SC)*(1 - 2/pi) < d**, i.e. K = sigma*sqrt(SC) < pi/(pi-2) ≈ 2.75 d. General form sigma*sqrt(SC)*(1 - E^2/sigma^2) < d with E the mean magnitude. Example given: sigma = 0.5, C = 0.1 fails at S = 40 for random but only at S = 304 for predator-prey.
  - Mixture of competition and mutualism (same-sign pairs, sign of each pair random so the mean is still 0): tau = +2/pi, so **sigma*sqrt(SC)*(1 + 2/pi) < d**, K < pi/(pi+2) ≈ 0.61 d.
  - Pure mutualism (mean coupling E > 0): one outlier real eigenvalue at the row sum, (S-1)*C*E - d, dominates; stability iff (S-1)*C*sigma*sqrt(2/pi) < d, which is diagonal dominance. The pairing does not matter here; the nonzero mean does.
  - Pure competition (mean -E): the outlier is at -(S-1)CE - d, i.e. **stabilising**; what destabilises is that the bulk is shifted right by C*E. Criterion found only for C = 1: sigma*(sqrt(S*pi/(2+pi)) + sqrt(2/pi)) < d.
  - Imposing realistic food-web structure (cascade, niche models) on predator-prey matrices *reduces* stability; nestedness reduces stability of bipartite mutualistic matrices; a preponderance of weak interactions reduces predator-prey stability but increases mutualistic/competitive stability (because it shrinks |tau|).
- **Correction to the earlier draft of this file.** It said tau "tends to -1" for predator-prey and "+1, doubling the radius" for competition/mutualism, with the outlier as the cause of competitive instability. None of that is the paper's result: tau = ∓2/pi for half-normal magnitudes; tau approaches -1 only when the two magnitudes in each pair are tightly correlated (this is what "tightly coupled pairs" in the abstract means); and for competition the outlier stabilises while the shifted bulk destabilises.
- **Assumptions.** Same as May plus the stated interaction structure; random placement of links given the type; independent magnitudes within a pair unless stated.
- **Operand/operator translation.** This is the clearest inheritable result for an algebra with typed couplings. Stated precisely: **what stabilises is a negative expected product E[M_ij M_ji] (opposite-sign pairs, "my gain is your loss"); a positive product (same-sign pairs, both reinforcing or both inhibiting) destabilises; and a nonzero mean coupling adds an outlier eigenvalue that destabilises for net-positive (mutualistic) coupling and stabilises for net-negative (competitive) coupling.** "Exploitative versus reciprocal" is a loose gloss: predator-prey links *are* reciprocal in the sense that both entries are nonzero; the operative quantity is the sign of the product, and its magnitude (the correlation of strengths within a pair) matters as much as the sign. Translated: a group whose drive couplings are mostly counter-balanced pairs (A gains as B loses, B pushes back) tolerates size; a group whose drives mostly echo each other in sign hits instability earlier, and net mutual reinforcement (emotional contagion) is the worst case. Net mutual inhibition is *not* uniformly destabilising: Coyte et al. 2015 (A4) find competition stabilises cooperative microbial networks. **This is a bound on a class of random-matrix models, not a statement about any real group.**
- **Cost.** The algebra must keep the coupling matrix as first-class, with the pair correlation tau and the mean coupling as computed parameters; the sign pair alone does not determine the result.

### A4. Related random-matrix and feasibility results

- Grilli, Adorisio, Suweis, Barabas, Banavar, Allesina, Maritan 2017, "Feasibility and coexistence of large ecological communities", Nat Commun 8, 14389, DOI 10.1038/ncomms14389 (Crossref title/year matched; I did not verify the author list beyond first author Grilli). Standard account: stability is not enough, the equilibrium must also be *feasible* (x* > 0); feasibility, not stability, is the binding constraint in large random communities. [from standard account]
- Stone 2018, "The feasibility and stability of large complex biological networks: a random matrix approach", Sci Rep 8, 8246, DOI 10.1038/s41598-018-26486-2 (Crossref-resolved). Same theme.
- Allesina & Tang 2015, "The stability-complexity relationship at age 40: a random matrix perspective", Population Ecology 57, 63-75, DOI 10.1007/s10144-014-0471-0 (Crossref-resolved; authors Allesina and Tang per my recall; the Crossref lookup returned Allesina first). Review of the line from A2.
- Mougi & Kondoh 2012, "Diversity of Interaction Types and Ecological Community Stability", Science 337, 349, DOI 10.1126/science.1220529. **[read: abstract]**: "A moderate mixture of antagonistic and mutualistic interactions can stabilize population dynamics. Furthermore, increasing complexity leads to increased stability in a 'hybrid' community." Translation: a group mixing exploitative and reciprocal drive couplings is more stable than one of a single type; the inheritable claim is a *composition rule* on coupling types.
- Coyte, Schluter & Foster 2015, "The ecology of the microbiome: Networks, competition, and stability", Science 350, 663-666, DOI 10.1126/science.aad2602 (Crossref: authors Coyte, Schluter, Foster). **[read: abstract]**: "Although cooperating networks of microbes can be efficient, we find that they are often unstable. Counterintuitively, this finding indicates that hosts can benefit from microbial competition when this competition dampens cooperative networks and increases stability. More generally, stability is promoted by limiting positive feedbacks and weakening ecological interactions." So cooperation destabilises and **competition stabilises** (corrected: the earlier draft said competition destabilises "in line with A3"). Consistent with A3's pure-competition case, where the mean-field outlier is stabilising. Translation: mutual inhibition between drives can be the brake on a runaway reinforcing loop.
- Tang, Pawar & Allesina 2014, "Correlation between interaction strengths drives stability in large ecological networks", Ecology Letters 17, 1094-1100, DOI 10.1111/ele.12312 (Crossref-resolved; added in validation, not read). Generalises A3: the within-pair correlation of strengths, not only signs, sets stability.
- Ives & Carpenter 2007, "Stability and Diversity of Ecosystems", Science 317, DOI 10.1126/science.1133258 (Crossref-resolved). Review noting that "stability" has many meanings, and results depend on which is used. [from standard account]

---

## B. Qualitative analysis and sign-stability

### B1. Quirk & Ruppert 1965; Levins 1974; Dambacher et al. 2003

- Quirk and Ruppert, "Qualitative Economics and the Stability of Equilibrium", Review of Economic Studies 32(4), 311-326 (1965). DOI 10.2307/2295838. Resolved at Crossref. (Note: the economics origin; ecology borrowed it.)
- Levins, "The qualitative analysis of partially specified systems", Annals of the New York Academy of Sciences 231, 123-138 (1974). DOI 10.1111/j.1749-6632.1974.tb20562.x. Resolved.
- Dambacher, Luh, Li & Rossignol 2003, "Qualitative Stability and Ambiguity in Model Ecosystems", American Naturalist 161, 876-888, DOI 10.1086/367590. Resolved (corrected: Crossref lists four authors; the draft omitted Luh).
- Jeffries 1974, "Qualitative Stability and Digraphs in Model Ecosystems", Ecology 55, 1415-1419, DOI 10.2307/1935470; Jeffries, Klee & van den Driessche 1977, "When is a Matrix Sign Stable?", Canadian Journal of Mathematics 29, 315-326, DOI 10.4153/CJM-1977-035-3. Both Crossref-resolved, added in validation, not read. These complete the characterisation.
- **Object.** Specify only the *signs* of the entries of M (+, -, 0) as a signed digraph. A sign pattern is **sign-stable** if every real matrix with that pattern is stable, whatever the magnitudes. [from standard account]
- **Theorem (standard form, from standard account; not read in the originals).** The Quirk-Ruppert conditions (as popularised by May 1973) are: (i) a_ii <= 0 for all i; (ii) a_ii < 0 for at least one i; (iii) a_ij*a_ji <= 0 for all i != j (only predation-type or one-way links, no competition or mutualism pairs); (iv) no cycles of length >= 3 in the digraph (a_ij a_jk ... a_qi = 0 for every sequence of three or more distinct indices); (v) det M != 0. These are necessary, and sufficient when every a_ii < 0. When some a_ii = 0 they are not sufficient: Jeffries 1974 and Jeffries-Klee-van den Driessche 1977 add a **colour test** on the predation graph (roughly: the undamped nodes must not admit a colouring that lets an undamped predator-prey sub-structure oscillate), giving the complete necessary-and-sufficient characterisation. Conditions (iii) and (iv) are the load-bearing exclusions for this file's purposes.
- **Levins' loop analysis (use).** Given the signed digraph, the sign of the response of x_i to a sustained press perturbation of x_j is read from loops in the graph (via the adjoint of -M). Dambacher et al. show many such predictions are *ambiguous* (opposite-sign paths), and give an approach to measuring it.
- **Empirical standing.** Sign-stable systems are rare; real food webs contain length-three cycles (omnivory) and positive links. Loop analysis has been used to predict responses to perturbation in several managed systems, with mixed success. I did not review the tests. [from standard account]
- **Operand/operator translation.** This is the **best fit for an algebra that is qualitative by design** (Aldred leaned discrete: none/low/high). Operands: drives with signed couplings. Operator: the signed digraph. Theorems available without any numbers: which structures are stable for all strengths (almost none: only acyclic exploitative chains with self-limits), and which press perturbations have determinate sign. The cost is that the stable class is so small and so un-group-like (no mutual reinforcement, no cycles) that its main use is as a negative result: **no group with mutual reinforcement or cyclic drive coupling is stable by structure alone**; stability must come from magnitudes, so from the quantitative layer.

---

## C. Keystones, engineers, cascades

### C1. Keystone species (Paine 1966, 1969)

- Paine 1966, "Food Web Complexity and Species Diversity", American Naturalist 100, 65-75. DOI 10.1086/282400. Resolved. Paine 1969, "A Note on Trophic Complexity and Community Stability", American Naturalist 103, 91-93. DOI 10.1086/282586. Resolved (the "keystone" term is from the 1969 note).
- **Claim.** [from standard account] Experimental removal of the starfish *Pisaster ochraceus* from rocky shore plots was followed by loss of species (I recall 15 down to 8) and takeover by mussels, so a predator of low abundance had a community effect disproportionate to its biomass. Empirical, not a theorem. Power, Tilman, Estes, Menge, Bond et al. 1996, "Challenges in the Quest for Keystones", BioScience 46, 609-620, DOI 10.2307/1312990 (Crossref-resolved in validation), is the usual formalisation of "disproportionate effect relative to abundance" (community importance per unit biomass). [from standard account; not read]
- **Network formalisation.** Loosely, keystone-ness is high centrality in the interaction network, or a large entry in the row/column of M^-1 (the press-response matrix). I found centrality-based keystone indices in the literature but did not confirm a specific paper, so I do not cite one.
- **Operand/operator translation.** A keystone drive (or drive-carrier) is one whose removal changes the group's equilibrium disproportionately to its level. In the algebra this is a **sensitivity theorem**: the response of the equilibrium to removing a node is a column of -M^-1; the keystone is the node with largest effect per unit abundance. That is a derivable, not inherited, property, and it needs M.
- **Human transfer.** Modlmeier, Keiser, Watters, Sih & Pruitt 2014, "The keystone individual concept: an ecological and evolutionary overview", Animal Behaviour 89, 53-62, DOI 10.1016/j.anbehav.2013.12.020 (Crossref-resolved; co-authors from recall). Keystone individuals in *animal* social groups (spiders, others), where the removal of one individual changes group behaviour disproportionately. Human application is by analogy only; I did not find a tested human instance with this formal definition. [from standard account of the concept]

### C2. Ecosystem engineers (Jones, Lawton & Shachak 1994)

- Citation: C. G. Jones, J. H. Lawton, M. Shachak, "Organisms as Ecosystem Engineers", Oikos 69, 373-386 (1994). DOI 10.2307/3545850. Resolved.
- **Object.** Organisms that modulate the availability of resources for others by causing physical state changes in biotic or abiotic materials (beavers, earthworms). Classification: autogenic vs allogenic engineers. Concept paper, no equations. [from standard account]
- **Translation.** Operator type: "alters the conditions under which other drives operate" as against "acts on another drive". This is a **second-order operator** (an operator that changes another operator's coefficients), exactly the point where niche construction (E) has equations. No theorem to inherit; the taxonomy is a useful design constraint: an algebra needs operators on couplings, not only on drives.

### C3. Trophic cascades (Pace et al. 1999; Estes et al. 2011)

- Pace, Cole, Carpenter & Kitchell 1999, "Trophic cascades revealed in diverse ecosystems", TREE 14, 483-488. DOI 10.1016/S0169-5347(99)01723-1. Resolved (Crossref authors match).
- Estes, Terborgh, Brashares, Power, Berger, Bond, Carpenter, Essington et al. 2011, "Trophic Downgrading of Planet Earth", Science 333, 301-306, DOI 10.1126/science.1205106 (Crossref-resolved in validation). **[read: abstract]**: loss of apex consumers has "extensive cascading effects ... in marine, terrestrial, and freshwater ecosystems worldwide", with effects on disease, wildfire, carbon sequestration, invasions and biogeochemical cycles.
- **Claim.** A change in the abundance of a top consumer propagates down through alternating signs: top predator up, herbivore down, plants up. In M terms, the response to a press at the top is the sign pattern of a path in the digraph, i.e. loop analysis of B. **[read: abstract of Pace et al.]**: cascades are now documented "in theoretically unlikely systems such as tropical forests and the open ocean"; transmission depends on productivity, refuges and compensation, and human extirpation of large animals removes cascades. (Corrected: the earlier draft attributed to this review the conclusion that cascades are "strongest in aquatic systems with simple webs"; that is the older Strong 1992 / Shurin et al. 2002 view, and Pace et al.'s point is the opposite, that cascades are more general than expected.)
- **Translation.** A path-propagation law with alternating sign. For a drive algebra: a perturbation entering the drive hierarchy at one level (e.g. status threat) produces alternating-sign effects through exploitation links. It is a derived consequence of the signed digraph.

---

## D. Mutualistic networks, nestedness, structural stability

### D1. Nestedness (Bascompte et al. 2003; Bastolla et al. 2009; Thebault & Fontaine 2010; James et al. 2012)

- Bascompte, Jordano, Melian & Olesen 2003, "The nested assembly of plant-animal mutualistic networks", PNAS 100, 9383-9387. DOI 10.1073/pnas.1633576100. Resolved (first author Bascompte; co-authors from recall). Empirical: plant-pollinator and plant-disperser networks are significantly nested (specialists interact with subsets of generalists' partners). [from standard account]
- Bastolla et al. 2009, Nature 458, 1018-1020. DOI 10.1038/nature07950. **[read: abstract]**: "nestedness reduces effective interspecific competition and enhances the number of coexisting species. Furthermore, we show that a nested network will naturally emerge if new species are more likely to enter the community where they have minimal competitive load. Nested networks seem to occur in many biological and social contexts."
- Thebault & Fontaine 2010, "Stability of Ecological Communities and the Architecture of Mutualistic and Trophic Networks", Science 329, 853. DOI 10.1126/science.1188321. Resolved. Standard account: mutualistic networks are most stable when nested; trophic networks when compartmented. [from standard account]
- James, Pitchford & Plank 2012, "Disentangling nestedness from models of ecological complexity", Nature 487, DOI 10.1038/nature11214. Resolved. **[read: abstract]**: across 59 plant-pollinator networks, the claim that nestedness increases species richness "is incorrect. A simpler metric—the number of mutualistic partners a species has—is a much better predictor ... Nestedness is, at best, a secondary covariate rather than a causative factor". (Corrected wording: the earlier draft attributed this to abundance and degree distribution; the paper names degree.)
- **Conflict worth recording.** Allesina & Tang (A3) say nestedness *destabilises* bipartite mutualistic networks (local stability); Thebault & Fontaine say nested, connected architecture *promotes* stability in mutualistic networks (persistence and resilience in their dynamic model); Bastolla says nestedness *increases coexistence*; James et al. say nestedness is secondary to degree. They measure different things, and Rohr et al. (D2) frame the disparity as a consequence of overlooking feasibility conditions and parameterisation. The disagreement is in the literature.
- **Translation.** Nested = the drives/persons with the fewest ties are tied only to the well-connected. For human groups: a core-periphery structure with the highest-degree members a subset of everyone's partners. The inheritable claim is conditional: nestedness reduces effective competition *if the coupling is mutualistic*, and the result is network-architecture-dependent.

### D2. Rohr, Saavedra & Bascompte 2014, structural stability

- Citation: Science 345, 1253497 (2014). DOI 10.1126/science.1253497. Resolved.
- **[read: abstract]**: "we introduce a mathematical framework based on the concept of structural stability to explain such a disparity of results. We investigated the range of conditions necessary for the stable coexistence of all species in mutualistic systems ... We show that observed network architectures maximize the range of conditions for species coexistence. We discuss the applicability of structural stability to study other types of interspecific interactions."
- **Mathematical form** [from standard account; checked for internal consistency, not against the full text]: for dx_i/dt = x_i(r_i + sum_j A_ij x_j) the feasibility domain is the set of intrinsic growth-rate vectors r for which x* = -A^-1 r > 0, a convex polyhedral cone in r-space spanned by the columns of -A. Rohr et al. restrict to interaction matrices for which any feasible equilibrium is also globally stable (a Lyapunov/diagonal-stability condition on A), so feasibility is the whole question. **Structural stability is measured by the normalised solid angle of that cone** (and, secondarily, by how far the actual r lies from the cone's centroid). It measures the size of the set of environmental conditions under which all components coexist, rather than the stability of one point.
- **Why it matters here.** It replaces the question "is this matrix stable?" with "how large is the region of conditions in which this structure persists?" That is a **robustness measure on the coupling structure**, directly usable by an algebra: a structure with a bigger feasibility cone tolerates more variation in the group's baseline drives (the r_i) before a drive dies out or goes negative.
- **Cost.** Requires the Lotka-Volterra form (linear, pairwise couplings). Computing the volume is expensive for large S. [from standard account]

---

## E. Assembly and niche construction

### E1. Assembly rules

- Law & Morton 1993, "Alternative Permanent States of Ecological Communities", Ecology 74, 1347-1361. DOI 10.2307/1940065. Resolved (the 1994 Ecology item with the same title is a reply). Standard account: in Lotka-Volterra communities built by sequential invasion, the final composition depends on the order of arrival; "permanent" communities are those resistant to all further invasion; multiple permanent communities can exist. [from standard account]
- Diamond 1975, "Assembly of species communities", in M. L. Cody & J. M. Diamond (eds.), *Ecology and Evolution of Communities*, Belknap Press of Harvard UP, pp. 342-444 (page range per standard citation; the chapter and book confirmed in library catalogues in validation; no DOI for the chapter). Standard account: from New Guinea and Bismarck bird distributions, Diamond proposed "assembly rules" (forbidden species combinations, "checkerboard" distributions). Contested by Connor & Simberloff 1979 as indistinguishable from null models, which started the null-model debate. [from standard account; not read]
- **Translation.** Order-dependence is a statement that the algebra is **non-commutative in the arrival of drives or members**: adding A then B gives a different final state than B then A. That is a structural property the algebra must either represent or exclude, and ecology gives a worked precedent and a well-defined notion of an invasion-resistant (permanent) state, essentially an ESS for communities (cluster 09 A1).

### E2. Niche construction (Odling-Smee, Laland & Feldman)

- Odling-Smee, Laland & Feldman 2003, *Niche Construction: The Neglected Process in Evolution*, Princeton UP (Monographs in Population Biology 37). DOI 10.1515/9781400847266. Resolved.
- Laland, Odling-Smee & Feldman 1996, "The evolutionary consequences of niche construction: a theoretical investigation using two-locus theory", J. Evol. Biol. 9, 293-316. DOI 10.1046/j.1420-9101.1996.9030293.x. Resolved.
- Laland, Odling-Smee & Feldman 1999, "Evolutionary consequences of niche construction and their implications for ecology", PNAS 96, 10242-10247. DOI 10.1073/pnas.96.18.10242. Resolved.
- **Object.** [from standard account] Two-locus population genetics in which one locus (E) determines a *niche-constructing* trait that modifies an environmental variable, and a second locus (A) determines a response to that environment's selective pressure. The recursion on gamete frequencies includes the term by which the genotype-dependent modification of the environment alters later selection. Result: niche construction can generate time lags, momentum, disequilibrium, and the fixation of otherwise-deleterious alleles, i.e. outcomes not obtained when the environment is a fixed parameter.
- **Assumptions.** Two loci, haploid or diploid with specified recursion; environment as a state variable with its own dynamics; population-genetic units.
- **Empirical standing.** Highly debated in evolutionary biology as to whether it is a distinct process or a re-description of the extended phenotype; modelling results are mathematical consequences, the biological significance is contested. [from standard account]
- **Translation.** Operands: agent drive-states and a shared environment variable (norms, institutions, physical setting). Operators: (a) agent acts on the environment; (b) environment modifies selection or drive dynamics on agents. The inheritable idea is the **closed loop**: the environment is a dynamic state variable, not a parameter. For a group-drive algebra, norms and institutions are the engineered niche and the loop explains persistent states (lock-in), momentum, and lag. The equations themselves (gamete recursion) do not transfer. The cultural version (Feldman & Laland on gene-culture) is a further step I did not survey.

---

## F. Regime shifts, resilience, early-warning signals

### F1. Holling 1973, resilience

- Citation: C. S. Holling, "Resilience and Stability of Ecological Systems", Annu. Rev. Ecol. Syst. 4, 1-23 (1973). DOI 10.1146/annurev.es.04.110173.000245. Resolved.
- **Definition.** [from standard account] Stability: ability of a system to return to equilibrium after a small perturbation (the A1 sense). Resilience: the capacity of a system to absorb disturbance and persist, measured as **the size of the disturbance that can be absorbed before the system flips to a different domain of attraction**. It is a geometric notion in state space, not an eigenvalue. A system can be highly resilient and fluctuate wildly, or be stable and brittle.
- **Formality.** A concept paper with a verbal and graphical model; the mathematical content is that of dynamical systems (basins of attraction). It is **not a theorem**.
- **Engineering vs ecological resilience.** Holling later named the two: *engineering resilience* is the speed of return to equilibrium, i.e. the return rate -Re(lambda_max) of the Jacobian (Pimm 1984, "The complexity and stability of ecosystems", Nature 307, 321-326, DOI 10.1038/307321a0, defines resilience this way); *ecological resilience* is the magnitude of disturbance absorbed before the basin changes. Holling 1996, "Engineering resilience versus ecological resilience", in Schulze (ed.), *Engineering Within Ecological Constraints*, National Academy Press, pp. 31-44 (reprinted in *Foundations of Ecological Resilience*, Crossref DOI 10.2307/jj.41003648.7). Added in validation; both Crossref-resolved, neither read. The two can move in opposite directions: a system can return fast near its equilibrium while sitting in a shallow, narrow basin. Neubert & Caswell 1997, "Alternatives to resilience for measuring the responses of ecological systems to perturbations", Ecology 78, 653, DOI 10.2307/2266047 (Crossref-resolved, not read), add *reactivity*: a stable but non-normal M can amplify perturbations transiently before they decay, which eigenvalue criteria (A1-A3) cannot see.
- **Brand & Jax 2007**, "Focusing the Meaning(s) of Resilience", Ecology and Society 12(1):23. DOI 10.5751/es-02029-120123. Resolved. Standard account: resilience is used in so many senses (descriptive, normative, engineering vs ecological) that without a stated definition the word is nearly useless as a scientific term. [from standard account]
- **Translation.** Two separate properties the algebra must not blur: *local stability* (eigenvalues, A1) versus *resilience* (basin size). Both can be defined on a group drive-dynamics, and they can disagree.

### F2. Alternative stable states, hysteresis, catastrophic shifts

- Scheffer, Carpenter, Foley, Folke & Walker 2001, "Catastrophic shifts in ecosystems", Nature 413, 591-596. DOI 10.1038/35098000. Resolved. **[read: abstract]**: "smooth change can be interrupted by sudden drastic switches to a contrasting state ... a loss of resilience usually paves the way for a switch to an alternative state ... strategies for sustainable management ... should focus on maintaining resilience."
- Scheffer & Carpenter 2003, "Catastrophic regime shifts in ecosystems: linking theory to observation", TREE 18, 648-656. DOI 10.1016/j.tree.2003.09.002. Resolved. Addresses how to test for alternative stable states from data. [from standard account]
- Scheffer 2009, *Critical Transitions in Nature and Society*, Princeton UP. DOI 10.1515/9781400833276. Resolved. Book spanning ecosystems, climate and some human systems. [from standard account]
- **Mathematics.** [from standard account] The canonical model is a one-dimensional gradient system dx/dt = a - b x + r x^2/(x^2 + 1) (lake-eutrophication form) or its normal form of a **fold (saddle-node) bifurcation**: as a control parameter a passes a threshold, a stable equilibrium collides with an unstable one and vanishes, and the state jumps to the other branch. **Hysteresis**: the threshold for the forward shift differs from the threshold for the backward shift, so recovery needs the control parameter pushed back well beyond where it tipped. These are theorems of bifurcation theory (fold normal form) applied to ecosystem models, not theorems specific to ecology.
- **Empirical standing.** Strong for lakes (shallow-lake turbid/clear states), coral reefs, some arid systems; evidence for alternative states in field data is often contested, and critics note that many apparent shifts are driven by a moving external driver rather than true bistability (Scheffer & Carpenter 2003 address this). [from standard account]
- **Translation.** If a group's drive dynamics has a fold, a smooth change in a slow variable (resources, threat, trust) produces an abrupt change in the group's drive profile and a hysteresis loop. The algebra needs: drives with nonlinear self-reinforcing terms (positive feedback), and slow control variables. Cheap to state; the hard part is showing it for any real group.

### F3. Early-warning signals (critical slowing down)

- Scheffer et al. 2009, "Early-warning signals for critical transitions", Nature 461, 53-59. DOI 10.1038/nature08227. **[read: abstract]**: "Complex dynamical systems, ranging from ecosystems to financial markets and the climate, can have tipping points at which a sudden shift to a contrasting dynamical regime may occur. Although predicting such critical points before they are reached is extremely difficult, work in different scientific fields is now suggesting the existence of generic early-warning signals that may indicate for a wide class of systems if a critical threshold is approaching."
- Scheffer et al. 2012, "Anticipating Critical Transitions", Science 338, 344. DOI 10.1126/science.1225244. Resolved (first author Scheffer).
- Dakos et al. 2008, "Slowing down as an early warning signal for abrupt climate change", PNAS 105, 14308. DOI 10.1073/pnas.0802430105. Resolved. Dakos et al. 2012, "Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data", PLoS ONE 7, e41010. DOI 10.1371/journal.pone.0041010. Resolved.
- **Theorem (standard).** Near a fold bifurcation the dominant eigenvalue lambda of the Jacobian tends to 0 from below, so the system recovers ever more slowly from small perturbations (Wissel 1984, "A universal law of the characteristic return time near thresholds", Oecologia 65, 101-107, DOI 10.1007/BF00384470, Crossref-resolved, added in validation, not read: return time scales as the inverse square root of the distance to the threshold). For a system with additive noise (Ornstein-Uhlenbeck approximation dy = lambda y dt + s dW), sampled at interval Δt: **lag-1 autocorrelation = e^{lambda Δt} → 1 and variance = s^2/(2|lambda|) → ∞** as lambda → 0^-. Checked: these follow directly from the OU stationary solution. Observable without knowing the model. [from standard account; derivation checked]
- **Limits.** It applies to *fold-type* transitions with slow approach and time-scale separation. Hastings & Wysham 2010, "Regime shifts in ecological systems can occur with no warning", Ecology Letters 13, 464. DOI 10.1111/j.1461-0248.2010.01439.x (Resolved) show shifts triggered by noise or other mechanisms that give no signal. False positives and missed alarms are real. [from standard account]
- **Link to A1.** Slowing down is *the same eigenvalue* as in the stability criterion: the rightmost eigenvalue of M. This is the one place where the community-matrix theory (A) and the regime-shift theory (F) are the same object seen from two sides; an algebra that has M gets both.
- **Human tests.** van de Leemput et al. 2014, "Critical slowing down as early warning for the onset and termination of depression", PNAS 111, 87-92. DOI 10.1073/pnas.1312114110 (Crossref gives year 2013 online). **[read: abstract]**: "the probability of an upcoming shift between a depressed and a normal state is related to elevated temporal autocorrelation, variance, and correlation between emotions in fluctuations of autorecorded emotions ... Our results support the hypothesis that mood may have alternative stable states separated by tipping points." Note the design: the abstract's "large group of healthy individuals and patients" means the association is shown across people, not as a forecast for one person. Wichers, Groot, Psychosystems, ESM Group & EWS Group 2016, "Critical Slowing Down as a Personalized Early Warning Signal for Depression", Psychotherapy and Psychosomatics 85, 114-116. DOI 10.1159/000441458. Resolved. A letter; **single patient confirmed** in validation via the companion data paper, Kossakowski, Groot, Haslbeck, Borsboom & Wichers 2017, Journal of Open Psychology Data 5, DOI 10.5334/jopd.29 (Crossref-resolved): one participant with major depression, 1,478 measurements over 239 days, during a double-blind antidepressant taper. Later work on larger samples (Clinical Psychological Science 2023) finds critical slowing down in only part of the sample and questions its value as a personalised predictor (seen in a search result only; not cited further).
- **Cross-reference.** `27-measuring-drive-dynamics.md` covers the measurement side: experience-sampling estimates of autocorrelation and variance, their reliability, and the caveats on the one positive human-affect early-warning study. Read it before treating item 8 of section H as measurable.
- **Translation.** **The inheritable, testable, human-validated result.** For the algebra: if drive dynamics sit near a fold, then a group's drive time series shows rising autocorrelation and variance (and rising cross-correlation among drives) before a shift in the group's state. This is also the only transfer from this cluster whose human evidence I found, though for individual mood, not group drives.
- **Social-scale transfer, weaker.** Barnosky et al. 2012, "Approaching a state shift in Earth's biosphere", Nature 486, 52-58, DOI 10.1038/nature11018 (Crossref-resolved), applies the tipping-point idea to the global biosphere, with a human-driver framing. It is about ecology, not a social group's regime shift. I did not find a peer-reviewed early-warning test on group mood or organisational collapse that I can cite.

---

## G. Adaptive cycle, panarchy, social-ecological systems

### G1. Gunderson & Holling 2002; Holling 2001

- Gunderson and Holling (eds.), *Panarchy: Understanding Transformations in Human and Natural Systems*, Island Press, 2002. The Crossref record found (DOI 10.2307/jj.41003538, "Panarchy", 2013) is the later reissue/book-chapter wrapper; the 2002 edition itself I did not find a DOI for. Holling & Gunderson chapter "Resilience and Adaptive Cycles" is 10.2307/jj.41003716.8 (Crossref, listed year 2012 for the reprint). Holling 2001, "Understanding the Complexity of Economic, Ecological, and Social Systems", Ecosystems 4, 390-405, DOI 10.1007/s10021-001-0101-5. Resolved.
- **Object.** [from standard account] Systems pass through four phases: r (rapid exploitation and growth), K (conservation: accumulation of capital, increasing connectedness and rigidity), Omega (release: collapse, "creative destruction"), alpha (reorganisation). Three axes: potential (accumulated capital), connectedness, resilience. **Panarchy** nests adaptive cycles across scales; "revolt" (a small fast cycle triggering a larger one) and "remember" (a larger slow cycle seeding a smaller one) are cross-scale links.
- **Formality.** A heuristic diagram (figure-eight loop) and verbal rules. I found no formal derivation: the adaptive cycle is not a dynamical system with stated equations or a theorem. Allen, Angeler, Garmestani, Gunderson & Holling 2014, "Panarchy: Theory and Application", Ecosystems 17, 578-589, DOI 10.1007/s10021-013-9744-2 (Crossref-resolved; authors per standard account), is the authors' own assessment that the framework needs more empirical and formal grounding. [from standard account]
- **Translation.** A phase-labelled narrative of group state (growth, rigidification, collapse, reorganisation). It could be a **state-machine overlay** on a drive algebra, with phases defined by thresholds on connectedness (C in A2's formula) and potential. But the labels are not derived from anything: the algebra would have to supply the dynamics.

### G2. Resilience in social-ecological systems (Walker et al. 2004; Folke 2006)

- Walker, Holling, Carpenter & Kinzig 2004, "Resilience, Adaptability and Transformability in Social-ecological Systems", Ecology and Society 9(2):5. DOI 10.5751/es-00650-090205. Resolved (co-authors from recall).
- Folke 2006, "Resilience: The emergence of a perspective for social-ecological systems analyses", Global Environmental Change 16, 253-267. DOI 10.1016/j.gloenvcha.2006.04.002. Resolved.
- **Content.** [from standard account] Resilience of a social-ecological system has three attributes: resistance to shocks (latitude), adaptability (capacity of actors to manage resilience), transformability (capacity to create a new system when the existing one is untenable). Conceptual frameworks with case studies; **no mathematics**.
- **Translation.** Vocabulary for what a group-algebra theorem should be about, not a calculus. Useful: "adaptability" corresponds to actors changing parameters of the dynamics, i.e. second-order operators (C2).

---

## H. Candidate theorems for a group-drive algebra

| # | Result | What it says for a group-drive algebra | What it requires | Source |
|---|---|---|---|---|
| 1 | May's bound | A group of S drive-carriers coupled to a fraction C at strength sigma is stable only while sigma*sqrt(S*C) < 1 | Linearisable drive dynamics; self-limiting diagonal; couplings that behave as random zero-mean | A2 |
| 2 | Allesina-Tang coupling-type law | Opposite-sign coupling pairs (negative E[M_ij M_ji]) raise the stability bound by 1/(1-2/pi) ≈ 2.75; same-sign pairs lower it to ≈ 0.61; net positive mean coupling (mutual reinforcement) adds a destabilising outlier, net negative (mutual inhibition) a stabilising one | Matrix with pair correlation tau and mean coupling as computed quantities | A3 |
| 3 | Mixed-type stabilisation | A moderate mix of coupling types beats a pure type | Typed couplings; random-structure assumption | A4 |
| 4 | Sign-stability (negative result) | No group with mutual reinforcement or cyclic coupling is stable by sign structure alone | Signed digraph only; no numbers | B1 |
| 5 | Press-response / keystone sensitivity | The effect of removing or boosting one drive-carrier on the equilibrium is a column of -M^-1; the keystone has the largest effect per unit | An actual M at an equilibrium | B1, C1 |
| 6 | Structural stability (feasibility cone) | A coupling structure's robustness is the volume of baseline-drive conditions for which all drives coexist | Lotka-Volterra form; baseline growth rates r | D2 |
| 7 | Fold bifurcation and hysteresis | Gradual change in a slow variable can flip the group profile abruptly; recovery needs overshoot | Self-reinforcing drive terms; a slow control variable | F2 |
| 8 | Critical slowing down | Autocorrelation and variance of drive time series rise before a tipping point; cross-correlation among drives rises too | Fold-type transition, slow approach, a measurable time series | F3 |
| 9 | Order-dependent assembly | Final group composition depends on order of entry, with invasion-resistant "permanent" states | Invasion dynamics on the coupling matrix | E1 |
| 10 | Niche-construction loop | Treat norms and institutions as a dynamic state variable that feeds back on drive selection | A second state equation and a coupling from agents to it | E2 |

Ranking by plausibility of inheritance (clearest and cheapest first): 4, 2, 1, 8, 7, then 5/6, then 9/10. Items 1-3 and 5-6 share one prerequisite: **an estimable coupling matrix M**, which is the load-bearing unknown for the whole cluster.

## What exists vs what does not

**Exists.**
- Theorems about random and structured coupling matrices (May 1972; Allesina & Tang 2012; Mougi & Kondoh 2012), correct under stated assumptions, and a literature of extensions (feasibility, structural stability).
- Sign-pattern theory (Quirk-Ruppert) that needs no numbers and gives hard negative results.
- Bifurcation-theory results (fold, hysteresis, critical slowing down) with generic early-warning statistics, tested on ecosystem and climate data and on individual human mood series (van de Leemput 2014; Wichers 2016).
- A formal two-locus treatment of niche construction.

**Exists, but was missed in the earlier draft (corrected in validation).**
- **Estimated coupling matrices for small human systems.** Within one person, VAR(1) coefficient matrices Phi among affect states are routinely estimated from experience sampling (27, section on networks); Phi is exactly a discrete-time community matrix (stable iff all |eigenvalues| < 1). Between two people, Gottman-Murray influence functions, actor-partner and cross-lagged dyadic VARs, and coupled-oscillator fits (Ferrer & Helm 2013; Helm, Sbarra & Ferrer 2012) estimate a 2x2 (or 2k x 2k) coupling matrix per couple (20). So "no estimable coupling matrix exists for any human group" was false. What is true: these are estimated for one person or a dyad, for affect or physiology rather than named drives; the edge-level replication record is poor (27); and nothing at group scale (S well above 2) has been estimated at the resolution a May-type test needs.
- **May-type stability arguments applied to human economic systems.** Haldane & May 2011, "Systemic risk in banking ecosystems", Nature 469, 351-355, DOI 10.1038/nature09659; May, Levin & Sugihara 2008, "Ecology for bankers", Nature 451, 893-894, DOI 10.1038/451893a; Moran & Bouchaud 2019, "May's instability in large economies", Phys. Rev. E 100, 032307, DOI 10.1103/PhysRevE.100.032307 (all Crossref-resolved in validation, none read). These are models of firms and banks using the random-matrix argument, not tests against a measured human matrix, and not social groups.

**Does not exist (as far as I found).**
- A measured drive-coupling matrix for any human group larger than a dyad, from which these theorems could be evaluated. No source found estimates "how much does one person's fear change another's curiosity" across a group at the resolution M needs.
- An empirical test of May's criterion against a measured interaction matrix of a human social or organisational network. (Theoretical applications to economies and banking exist; see above. A web search in validation found nothing more.)
- A tested early-warning signal for a *group* tipping point (collapse of a team, a norm flip) from drive-like time series. The tested human cases are individual mood.
- A formal, derivable adaptive cycle or panarchy. They are diagrams and prose.
- A formal definition of a keystone *human* that has been tested; only the animal-group concept paper (Modlmeier 2014).
- Any evidence that human-group drive dynamics are Lotka-Volterra, or that linearisation at an equilibrium is a reasonable model for them. All of A-D rest on that.

**Blunt caution.** The strength of this cluster is that its theorems are conditional and the conditions can be read off the algebra. The weakness is the same: the transfer to humans is an analogy until a coupling matrix is estimated from data. The cheapest honest first step would be to make the algebra produce a signed digraph (B1) and the sign-pair classification (A3) and check what falls out, before committing to numbers.

## Unconfirmed

- Gunderson & Holling 2002 *Panarchy* as a 2002 book with its own DOI: not found; only the later JSTOR wrapper records (10.2307/jj.41003538 resolves with no author or year metadata beyond 2013). The book itself certainly exists (Island Press 2002); only the DOI is unconfirmed.
- Diamond 1975 page range (342-444): standard citation, not seen in a catalogue.
- Exact wording of the Quirk-Ruppert conditions and the colour test: from the standard account; Quirk & Ruppert 1965 and Jeffries 1974/1977 were resolved but not read.
- Nature-version notation of Allesina-Tang: the criteria above are from the arXiv preprint; the published version states them with E (mean magnitude) in place of the half-normal constants.
- Any peer-reviewed early-warning test on group-level human data: none found; absence here is "I did not find", not "does not exist".
- (Resolved in validation and moved out of this list: Power et al. 1996, Estes et al. 2011, Diamond 1975 existence, Wichers 2016 single-patient design, all co-author lists, which Crossref now confirms.)

## Clearly missing important work (added in validation, not surveyed)

- Sommers, Crisanti, Sompolinsky & Stein 1988 (elliptic law, Phys. Rev. Lett. 60, 1895) and Tao & Vu 2010 (circular law): the random-matrix theorems May and Allesina-Tang rest on; May 1972 itself argued heuristically.
- May 1973, *Stability and Complexity in Model Ecosystems* (Princeton): the book-length treatment of A2 and B1.
- Pimm 1984, Neubert & Caswell 1997, Holling 1996 (now cited briefly in F1): the stability-notion taxonomy.
- Wissel 1984 (now cited in F3): origin of critical slowing down in ecology.
- Tang, Pawar & Allesina 2014 (now cited in A4): pair correlation as the driver.
- Barabás, Michalska-Smith & Allesina 2017, "Self-regulation and the stability of large ecological networks" (Nat. Ecol. Evol.): the diagonal, which May fixed at -1, is the free variable an algebra of self-limiting drives would set. Not resolved here.
- Kéfi et al. and Dakos et al. on spatial early-warning signals; Boettiger & Hastings 2012 on the statistics of false alarms. Not resolved here.

## Validation log (2026-10-29)

Every DOI re-resolved at api.crossref.org; abstracts checked at Europe PMC where available; Allesina & Tang checked against the full arXiv preprint (1105.2071v1). Mathematics re-derived where noted.

- Levins 1968 *Evolution in Changing Environments* (10.1515/9780691209418): ✓
- May 1972 (10.1038/238413a0): ✓ criterion sigma*sqrt(SC) < 1 checked; note added that May's argument was heuristic
- Gardner & Ashby 1970 (10.1038/228784a0): ✓
- McCann 2000 (10.1038/35012234): ✓
- Allesina & Tang 2012 (10.1038/nature10832): ✎ corrected: tau = ∓2/pi not ∓1; criteria now stated (predator-prey sigma*sqrt(SC)(1-2/pi) < d; mixture (1+2/pi); mutualism outlier (S-1)CE < d; competition outlier stabilising, bulk shift destabilising); "exploitative vs reciprocal" restated as sign of E[M_ij M_ji] plus mean coupling
- Grilli et al. 2017 (10.1038/ncomms14389): ✓ author list now confirmed
- Stone 2018 (10.1038/s41598-018-26486-2): ✓
- Allesina & Tang 2015 (10.1007/s10144-014-0471-0): ✓
- Mougi & Kondoh 2012 (10.1126/science.1220529): ✓ abstract quote verified
- Coyte, Schluter & Foster 2015 (10.1126/science.aad2602): ✎ corrected: competition *stabilises* in their model; the draft said it destabilises
- Ives & Carpenter 2007 (10.1126/science.1133258): ✓ (pages 58-62)
- Quirk & Ruppert 1965 (10.2307/2295838): ✎ conditions restated; sufficiency only with all a_ii < 0, colour test needed otherwise
- Levins 1974 (10.1111/j.1749-6632.1974.tb20562.x): ✓
- Dambacher et al. 2003 (10.1086/367590): ✎ corrected author list (Luh omitted)
- Paine 1966 (10.1086/282400), Paine 1969 (10.1086/282586): ✓
- Power et al. 1996: ✎ was unconfirmed; resolved 10.2307/1312990
- Modlmeier et al. 2014 (10.1016/j.anbehav.2013.12.020): ✓
- Jones, Lawton & Shachak 1994 (10.2307/3545850): ✓
- Pace et al. 1999 (10.1016/S0169-5347(99)01723-1): ✎ corrected: conclusion misattributed; review says cascades are more general than expected
- Estes et al. 2011: ✎ was unconfirmed; resolved 10.1126/science.1205106 and cited from abstract
- Bascompte et al. 2003 (10.1073/pnas.1633576100): ✓
- Bastolla et al. 2009 (10.1038/nature07950): ✓
- Thebault & Fontaine 2010 (10.1126/science.1188321): ✓ added to the nestedness conflict
- James, Pitchford & Plank 2012 (10.1038/nature11214): ✎ corrected summary (degree, not abundance)
- Rohr, Saavedra & Bascompte 2014 (10.1126/science.1253497): ✓ formulation tightened (cone spanned by columns of -A, solid angle, global-stability restriction)
- Law & Morton 1993 (10.2307/1940065): ✓
- Diamond 1975: ✎ was unconfirmed; book chapter confirmed (no DOI); page range still ?
- Odling-Smee, Laland & Feldman 2003 (10.1515/9781400847266): ✓ (Crossref lists the 2013 digital reissue)
- Laland et al. 1996 (10.1046/j.1420-9101.1996.9030293.x), 1999 (10.1073/pnas.96.18.10242): ✓
- Holling 1973 (10.1146/annurev.es.04.110173.000245): ✓ engineering-vs-ecological distinction added
- Brand & Jax 2007 (10.5751/es-02029-120123): ✓
- Scheffer et al. 2001 (10.1038/35098000), Scheffer & Carpenter 2003 (10.1016/j.tree.2003.09.002), Scheffer 2009 (10.1515/9781400833276): ✓
- Scheffer et al. 2009 (10.1038/nature08227), 2012 (10.1126/science.1225244): ✓
- Dakos et al. 2008 (10.1073/pnas.0802430105), 2012 (10.1371/journal.pone.0041010): ✓
- Hastings & Wysham 2010 (10.1111/j.1461-0248.2010.01439.x): ✓
- Critical-slowing-down theorem: ✓ OU formulae checked (AC = e^{lambda Δt}, Var = s^2/2|lambda|)
- van de Leemput et al. 2014 (10.1073/pnas.1312114110): ✓ note added that the evidence is between-person
- Wichers & Groot 2016 (10.1159/000441458): ✓ single patient confirmed via Kossakowski et al. 2017 (10.5334/jopd.29)
- Barnosky et al. 2012 (10.1038/nature11018): ✓
- Gunderson & Holling *Panarchy* 2002: ? DOI only (book exists)
- Holling & Gunderson chapter (10.2307/jj.41003716.8): ✓
- Holling 2001 (10.1007/s10021-001-0101-5): ✓
- Allen et al. 2014 (10.1007/s10021-013-9744-2): ✓ authors confirmed
- Walker et al. 2004 (10.5751/es-00650-090205), Folke 2006 (10.1016/j.gloenvcha.2006.04.002): ✓
- Closing claim "no estimable coupling matrix for any human group": ✎ corrected; VAR (within person) and dyadic coupling matrices are estimated (20, 27); the gap is group scale
- Closing claim "no test of May's criterion on human networks": ✎ narrowed; theoretical applications to banks and economies exist (Haldane & May 2011; Moran & Bouchaud 2019); no empirical test on a measured social matrix found
- Added in validation: Jeffries 1974, Jeffries-Klee-van den Driessche 1977, Tang-Pawar-Allesina 2014, Pimm 1984, Holling 1996, Neubert & Caswell 1997, Wissel 1984, Kossakowski 2017, May-Levin-Sugihara 2008, Haldane & May 2011, Moran & Bouchaud 2019 (all Crossref-resolved, none read)
- Fabrications found: none.

**Verdict.** The bibliography is sound: every DOI resolves to the claimed work and no citation was invented. The weak point was the mathematics and the summaries written from memory: the Allesina-Tang constants and mechanism were wrong in a way that changed the inheritable lesson (mutual inhibition is not uniformly destabilising, and pair-strength correlation matters as much as sign), and two "standard account" summaries (Pace 1999, Coyte 2015) said the opposite of the abstracts. Treat any remaining [from standard account] line as a lead, not a result.
