# Prior work, cluster 09: biology, ecology, epidemiology

Date: 2026-10-29. Strand: social-algebra. Scope: natural-science treatments of group behaviour, translated into operand/operator terms. Other clusters cover sociology, social psychology, opinion dynamics, cybernetics and history.

## Summary

Verification status: existence, authors, venue, year and DOI/URL were confirmed by web search for every entry in the main list. The formal structures (payoff matrices, ODEs, rules) are the standard textbook forms, stated here from general knowledge and not re-derived from the papers' full text, except where a result below quotes a source. Anything not confirmed is in "Unconfirmed" at the end. A validation pass on 2026-10-29 corrected several attributions and statements; see the log at the end.

Biology has no single "social algebra", but it has three things the strand wants:

1. **A genuine operator/operand split for pairwise interaction**: evolutionary game theory. Operands are strategies (types); the operator is the payoff matrix applied to encounters; the dynamics (replicator equation) is the induced flow on type frequencies.
2. **A formal decomposition of change in a group into within-group and between-group parts**: the Price equation. It is an identity, not a model, and so is the closest thing to an algebraic law across all levels of grouping.
3. **A layered ontology of "what a social group is"**: Hinde's interactions, relationships, social structure. It is a framework, not a calculus, but it names the levels an algebra would need.

The rest is local-rule simulation (Vicsek, Couzin), network measurement (Croft/Krause/James, Whitehead) and contagion models (SIR, Centola-Macy), each with a clear operator structure but little claim to be a general algebra.

Works listed: 22 main entries. After validation, six formerly unconfirmed items are confirmed and folded into the main entries; the remaining unconfirmed items are listed at the end.

---

## A. Interaction types and evolutionary dynamics

### A1. Maynard Smith and Price 1973, "The Logic of Animal Conflict"

- Citation: J. Maynard Smith and G. R. Price, Nature 246, 15-18 (2 Nov 1973). DOI 10.1038/246015a0. PDF copy: https://www.energia.mta.hu/~szabo/EGT20/library/maynard_n73.pdf
- Longer treatment: Maynard Smith 1974, "The Theory of Games and the Evolution of Animal Conflicts", J Theor Biol 47(1), 209-221, DOI 10.1016/0022-5193(74)90110-6. Book: Maynard Smith, Evolution and the Theory of Games, Cambridge University Press, 1982. Role asymmetry and Bourgeois: Maynard Smith and Parker, "The logic of asymmetric contests", Animal Behaviour 24, 159-175 (1976).
- **Their vocabulary**: strategy, evolutionarily stable strategy (ESS), payoff as fitness, "limited war". The 1973 paper's simulated strategies are Mouse, Hawk, Bully, Retaliator and Prober-Retaliator. The two-strategy Hawk-Dove game with V and C is the later simplification (1974 paper, 1982 book), and Bourgeois comes from the asymmetric-contest work (1976, 1982), not from this paper. (Validation correction; the earlier text attributed Dove and Bourgeois to 1973.)
- **Operands (translated)**: behavioural types (strategies) in a population; contests are between two role-symmetric individuals.
- **Operators (translated)**: the payoff matrix E(i,j) = expected fitness change to a type-i player meeting a type-j player. Hawk-Dove (1974/1982 form) with value V and injury cost C: HH = (V-C)/2, HD = V, DH = 0, DD = V/2. The ESS condition is a stability test on the matrix: a strategy I is an ESS if, for every mutant J, E(I,I) > E(J,I) or (E(I,I) = E(J,I) and E(I,J) > E(J,J)). Mixed ESS for C > V is Hawk with probability V/C.
- **Predictive/control claim**: predicts that contests are usually limited (ritualised) rather than escalated, and gives equilibrium mixtures. Held up qualitatively across many species; quantitative fits are mixed, because real contests have assessment, role asymmetry and repeated play that the base matrix omits. It does not by itself give control; it says which interaction rules are stable against invasion, which is a design constraint.
- **Limits**: well-mixed population, pairwise encounters, fixed strategy sets, fitness as the only currency.
- **Relevance**: the cleanest existing algebra-shaped object: a finite set of types, a bilinear interaction operator, a stability criterion. For humans the matrix is not fitness but whatever the group values; the move is to treat payoffs as an editable per-group parameter. What it lacks is composition: the matrix handles one encounter type, with no way to chain or nest interactions. Note that role asymmetry (owner vs intruder in Bourgeois) is already in the 1976/1982 theory, so "operand = type in a role" has a biological precedent.

### A2. Taylor and Jonker 1978, replicator dynamics

- Citation: P. D. Taylor and L. B. Jonker, "Evolutionary stable strategies and game dynamics", Mathematical Biosciences 40(1-2), 145-156 (1978). DOI 10.1016/0025-5564(78)90077-9. PDF: https://www.energia.mta.hu/~szabo/EGT20/library/taylor_mbs78.pdf
- Note: one library record (Vidal) gives vol 16, pp 76-83, which search showed to be wrong for this paper.
- **Their vocabulary**: game dynamics, replicator equation, stable point vs ESS.
- **Operands**: the frequency vector x over strategies (a point on the simplex).
- **Operators**: ODE dx_i/dt = x_i [ (Ax)_i - x^T A x ], where A is the payoff matrix. The payoff matrix is the generator; the replicator equation is the flow it induces. (The name "replicator equation" was coined later, by Schuster and Sigmund 1983; Taylor and Jonker call it game dynamics.) Search confirmed the paper shows an ESS is stable under the continuous dynamic given a non-degeneracy condition, that the discrete version can fail by overshoot, and that dynamically stable points need not be ESS.
- **Predictive/control claim**: gives trajectories and fixed points of type frequencies. Strong as mathematics; as a description of real populations it assumes inheritance of strategy and random mixing.
- **Limits**: no structure (who meets whom), no memory, no individuals.
- **Relevance**: converts a static interaction table into dynamics. For social-algebra this is the template for "later model interactions": define operator tables first, then derive the flow.

### A3. Axelrod and Hamilton 1981, "The Evolution of Cooperation"

- Citation: R. Axelrod and W. D. Hamilton, Science 211(4489), 1390-1396 (27 Mar 1981). DOI 10.1126/science.7466396.
- **Vocabulary**: iterated Prisoner's Dilemma, tit-for-tat, tournament, ESS.
- **Operands**: strategies as finite-memory rules (functions from past history to move).
- **Operators**: the repeated game; a strategy is itself an operator on the opponent's history. Payoffs T > R > P > S with 2R > T + S.
- **Claim**: reciprocity-based cooperation can emerge and persist among egoists given enough future interaction (per the abstract as reproduced by search). Held up as a result about repeated games; the empirical claim that tit-for-tat is robustly best did not hold up against noise (later work found more forgiving strategies better; stated from general knowledge, not checked here).
- **Limits**: pairwise, symmetric, discrete moves.
- **Relevance**: strategies as operators acting on histories is the one place biology gives operators-as-first-class-objects rather than mere payoffs. Transfers readily to human dyads.

### A4. Trivers 1971, "The Evolution of Reciprocal Altruism"

- Citation: R. L. Trivers, Quarterly Review of Biology 46(1), 35-57 (1971). DOI 10.1086/406755. https://www.journals.uchicago.edu/doi/10.1086/406755 (paywalled; abstract confirmed).
- **Vocabulary**: altruism, cheater, delayed return, gratitude, trust, guilt, moralistic aggression.
- **Operands**: individuals with a ledger of past help given and received.
- **Operators**: help(i -> j) at cost c to i and benefit b to j with b > c; return-help; detect-and-punish a non-reciprocator.
- **Claim**: selection can favour reciprocal altruism when encounters repeat and cheating can be detected. The abstract (as found) applies it to cleaning symbioses, bird alarm calls and humans; the human case treats friendship, gratitude, sympathy, trust and guilt as adaptations regulating the exchange system.
- **Limits**: verbal model; cleaning-symbiosis and alarm-call examples have been disputed in the literature (general knowledge, not checked).
- **Relevance**: it names the human emotions that act as operator-regulators. Directly usable as a catalogue: each named emotion in the abstract is a state variable or a gate on an operator.

## B. Kin and multilevel selection

### B1. Hamilton 1964, kin selection and Hamilton's rule

- Citation: W. D. Hamilton, "The genetical evolution of social behaviour I and II", J Theor Biol 7(1), 1-16 and 17-52 (1964). DOIs 10.1016/0022-5193(64)90038-4 and 10.1016/0022-5193(64)90039-6. PDF of I: https://pdodds.w3.uvm.edu/files/papers/others/everything/hamilton1964b.pdf
- **Vocabulary**: inclusive fitness, coefficient of relationship, social behaviour classified by sign of effects on actor and recipient.
- **Operands**: individuals carrying genes, linked by a relatedness weight r in [0,1].
- **Operators**: a social act has an effect on actor fitness (-c) and recipient fitness (b); its evolutionary value is weighted by relatedness: act is favoured if r b > c. The taxonomy of acts by the signs of the two effects (mutual benefit/altruism/selfishness/spite) is a 2x2 classification of operators; it is usually credited to Hamilton 1964 with spite developed in Hamilton 1970 (Nature 228, 1218-1220), and the standard modern statement is West, Griffin and Gardner 2007, "Social semantics", J Evol Biol 20, 415-432. Hamilton's own 1964 form is k > 1/r (k the ratio of recipient gain to actor loss), equivalent to rb > c.
- **Claim**: altruism toward relatives is selected when rb > c. Widely supported empirically in eusocial insects and cooperative breeders; the rule's generality as a causal explanation has been contested: Nowak, Tarnita and Wilson (Nature 466, 1057, 2010) argued inclusive fitness is of little use, Abbot et al. (Nature 471, E1-E4, 2011) rebutted at length (both confirmed to exist by search; Nowak et al.'s reply is Nature 471, E9-E10, DOI 10.1038/nature09836). Gardner, West and Wild (J Evol Biol 24, 1020-1043, 2011, DOI 10.1111/j.1420-9101.2011.02236.x) argue the rule holds generally and misuse comes from mis-identifying b and c. Queller 1992, Evolution 46(2), 376-380, gives a general version.
- **Limits**: needs a measurable relatedness; for humans the analogue is closeness, which is not genetic.
- **Relevance**: the cleanest example of an operator weighted by a relation between operands. A social-algebra could replace r with any tie strength. The rb > c form is a template for "an act is stable if tie-weighted benefit exceeds cost".

### B2. Price 1970, "Selection and Covariance" (Price equation)

- Citation: G. R. Price, Nature 227, 520-521 (1970). DOI 10.1038/227520a0. https://www.doi.org/10.1038/227520A0. Multilevel extension: Price 1972, "Extension of covariance selection mathematics", Annals of Human Genetics 35, 485-490. Overview: S. A. Frank, "George Price's contributions to evolutionary genetics", J Theor Biol 175, 373-388 (1995), https://stevefrank.org/reprints-pdf/95JTB-Price.pdf (confirmed in validation).
- **Vocabulary**: selection, covariance, transmission, groups and subgroups.
- **Operands**: any population partitioned into groups, each with a trait value z and fitness w.
- **Operators**: the identity w_bar * delta(z_bar) = Cov(w_i, z_i) + E(w_i * delta z_i), over units i (z_i the unit's trait, w_i its fitness, delta z_i the parent-offspring change). Selection (covariance) plus transmission (expectation). Applied recursively (the 1972 extension; Hamilton 1975 used it for group structure) it splits change into between-group and within-group components at each level.
- **Claim**: exact, so no predictive claim of its own; it is a bookkeeping law. Its strength is that it makes group selection and individual selection commensurable.
- **Limits**: it is an accounting identity, so it explains nothing causally without a model of w and z; the covariance term hides the mechanism.
- **Relevance**: the nearest thing in this cluster to an algebraic law that is true at every level. A social algebra could aim for a Price-like conservation or decomposition law as a test of correctness.

### B3. Wilson and Wilson 2007, multilevel selection

- Citation: D. S. Wilson and E. O. Wilson, "Rethinking the theoretical foundation of sociobiology", Quarterly Review of Biology 82(4), 327-348 (2007). DOI 10.1086/522809. https://www.journals.uchicago.edu/doi/abs/10.1086/522809
- **Vocabulary**: multilevel selection, group-level adaptation, the major transitions.
- **Operands**: nested groups; traits that are costly within a group but beneficial between groups.
- **Operators**: selection at each level, with the Price decomposition as the formalism.
- **Claim**: group selection provides the unifying foundation for sociobiology (abstract as found). Contested; kin-selection advocates say the two are formally equivalent.
- **Limits**: much of the dispute is about causal interpretation, not mathematics.
- **Relevance**: human groups are explicitly nested (family, team, firm, nation); this is the only literature here that treats nesting as primary.

## C. Cooperation mechanisms

### C1. Nowak 2006, "Five rules for the evolution of cooperation"

- Citation: M. A. Nowak, Science 314, 1560-1563 (8 Dec 2006). DOI 10.1126/science.1133755. Free copy: https://moodle2.units.it/pluginfile.php/816523/mod_resource/content/1/nowak2006_fiverules.pdf
- **Vocabulary**: five mechanisms: kin selection, direct reciprocity, indirect reciprocity, network reciprocity, group selection.
- **Operands**: cooperators and defectors, plus a population structure.
- **Operators**: one inequality per mechanism, each a condition on b/c: kin r > c/b; direct reciprocity w > c/b (w = probability of another round); indirect reciprocity q > c/b (q = probability of knowing a reputation); network reciprocity b/c > k (k = number of neighbours per individual); group selection b/c > 1 + n/m (n maximum group size, m number of groups). Validation checked all five against the paper's Fig. 1 summary as known to the validator; they match. Each holds only under the paper's simplifying assumptions (e.g. the direct-reciprocity rule compares TFT with always-defect; network rule is for death-birth updating and weak selection; group rule for weak selection and rare group splitting).
- **Claim**: each mechanism gives a threshold under which cooperation can evolve. A compact classification, widely taught. Criticised for assuming weak selection and for treating mechanisms as separate.
- **Limits**: one behaviour (cooperation), two types, fitness currency.
- **Relevance**: five mechanisms, each with a stability inequality, is algebra-shaped. But they are conditions under which a cooperate/defect operator is stable, not operators that form groups; calling them "bonding operators" would be a reinterpretation by this strand, not something the paper offers. Candidate source of five structural parameters (r, w, q, k, n/m) rather than five primitives.

### C2. Nowak and Sigmund 1998, indirect reciprocity by image scoring

- Citation: Nature 393(6685), 573-577 (11 Jun 1998). DOI 10.1038/31225. https://pure.iiasa.ac.at/id/eprint/5334/
- **Vocabulary**: image score, discriminator, reputation.
- **Operands**: individuals each carrying a public score.
- **Operators**: help(i -> j) if score(j) >= k; update score(i) after acting. Confirmed key condition: probability of knowing the recipient's image must exceed the cost-to-benefit ratio.
- **Claim**: cooperation without repeated meeting, via reputation. Later work (not checked here) showed image scoring alone is unstable against second-order cheats, motivating standing and judging norms.
- **Relevance**: a reputation is a state attached to an operand and updated by operators. This is the clearest biology treatment of "gossip" as an operator.

### C3. Nowak and May 1992, spatial games

- Citation: Nature 359, 826-829 (1992). DOI 10.1038/359826a0. https://www.nature.com/articles/359826a0
- **Operands**: cells on a lattice, each a cooperator or defector.
- Title: "Evolutionary games and spatial chaos".
- **Operators**: each cell plays its neighbours (and, in the paper, itself), then adopts the strategy of the highest scorer among its neighbourhood including itself (synchronous update). The game is a simplified PD with a single parameter b (T = b, R = 1, P = S = 0).
- **Claim**: spatial structure allows cooperators to persist, with chaotic spatial patterns. Sensitive to update rule and payoff details.
- **Relevance**: shows that where interactions happen (topology) is as much a part of the algebra as what they are.

### C4. Ohtsuki, Hauert, Lieberman, Nowak 2006, evolution on graphs

- Citation: Nature 441(7092), 502-505 (25 May 2006). DOI 10.1038/nature04605. https://www.nature.com/articles/nature04605
- **Operators**: death-birth updating on a k-regular graph; cooperation favoured when b/c > k (confirmed in abstract), derived by pair approximation. Title: "A simple rule for the evolution of cooperation on graphs and social networks". Y.-T. Chen, "Sharp benefit-to-cost rules for the evolution of cooperation on regular graphs", Annals of Applied Probability 23(2), 637-664 (2013), arXiv 1107.1513, gives the rigorous version (confirmed). Generalisation to any population structure: Allen et al., "Evolutionary dynamics on any population structure", Nature 544, 227-230 (2017).
- **Limits**: weak selection, regular or near-regular graphs, no rewiring.
- **Relevance**: the update rule is an explicit operator (who replaces whom), so changing the rule changes the result. That is a warning that an algebra must specify update order.

## D. Collective animal behaviour

### D1. Vicsek et al. 1995

- Citation: T. Vicsek, A. Czirok, E. Ben-Jacob, I. Cohen, O. Shochet, "Novel type of phase transition in a system of self-driven particles", Phys Rev Lett 75(6), 1226-1229 (1995). DOI 10.1103/PhysRevLett.75.1226. arXiv: https://arxiv.org/abs/cond-mat/0611743
- **Vocabulary**: self-driven particles, noise, order parameter, kinetic phase transition.
- **Operands**: particles with position and heading, constant speed.
- **Operators**: each step, set heading to the average heading of neighbours within radius r, plus noise. Order parameter is the normalised mean velocity. The abstract (confirmed) states particles move at constant speed and adopt the average direction of neighbours with random noise.
- **Claim**: a transition from disordered to aligned motion as noise falls or density rises. Held up as a model class. The original paper reported a continuous (second-order) transition; Grégoire and Chaté, "Onset of collective and cohesive motion", PRL 92, 025702 (2004) argued it is discontinuous (first-order) at large system sizes, and that dispute is the substantive one. (The arXiv item cond-mat/0703532 cited earlier is a minor one-page comment by Chen and Zhang, 2007, on a different pitfall, not the order dispute.) The arXiv copy cond-mat/0611743 is the 1995 paper posted in 2006 (confirmed).
- **Limits**: no leaders, no heterogeneity, no goals.
- **Relevance**: one operator (align with neighbours) yields a macro-level phase change. Useful as a model for conformity; the order parameter is a candidate macro-observable.

### D2. Couzin, Krause, James, Ruxton and Franks 2002

- Citation: "Collective memory and spatial sorting in animal groups", J Theor Biol 218(1), 1-11. DOI 10.1006/jtbi.2002.3065. (Some indexes list a malformed variant.) Abstract: https://eprints.gla.ac.uk/10628 (via search).
- **Vocabulary**: zone of repulsion, orientation, attraction; swarm, torus, dynamic parallel, highly parallel group; collective memory (hysteresis).
- **Operands**: individuals in 3D with position and direction.
- **Operators**: three concentric zones; move away from anyone in the inner zone, align with those in the middle, move toward those in the outer zone. Repulsion has strict priority: if anyone is in the zone of repulsion, orientation and attraction are ignored that step; otherwise the two are combined. There is also a blind angle behind each individual, noise and a maximum turning rate. Changing zone widths switches the group between collective states.
- **Claim**: small changes in individual rules cause group-level state transitions, with hysteresis ("collective memory"). Qualitative agreement with fish schools; direct individual-level validation is limited.
- **Relevance**: a small parameter set (three ranges) spans a typology of group states. A good model of a "mode switch" operator.

### D3. Couzin, Krause, Franks and Levin 2005

- Citation: "Effective leadership and decision-making in animal groups on the move", Nature 433(7025), 513-516 (3 Feb 2005). DOI 10.1038/nature03236. https://www.cs.princeton.edu/courses/archive/fall24/cos597C/bib/nature03236.pdf
- **Vocabulary**: informed individuals, leadership, consensus, preferred direction.
- **Operands**: uninformed individuals plus a fraction with a preferred direction.
- **Operators**: the 2002 zone rule plus a weighted pull toward the preferred direction for informed members.
- **Claim** (confirmed): bigger groups need a smaller share of informed members to steer them; a small informed minority gives high accuracy; consensus is reached even when informed members do not know whether they are in the majority.
- **Limits**: simulation; later experiments on fish and pigeons partly support it.
- **Relevance**: a worked example of influence without command: leadership as a minority operator acting through a local alignment operator.

### D4. Sumpter 2006 and 2010

- Citations: D. J. T. Sumpter, "The principles of collective animal behaviour", Phil Trans R Soc B 361, 5-22 (2006), DOI 10.1098/rstb.2005.1733, https://pmc.ncbi.nlm.nih.gov/articles/PMC1626537. Book: Collective Animal Behavior, Princeton University Press, 2010, https://press.princeton.edu/books/paperback/9780691148434/collective-animal-behavior (also DOI 10.1515/9781400837106).
- **Vocabulary**: self-organisation, positive feedback, response thresholds, individual integrity.
- **Operands**: individuals with simple response rules.
- **Operators**: repeated local interaction; positive feedback loops amplify, thresholds gate response, negative feedback limits.
- **Claim**: group patterns follow from a small set of principles rather than from central control.
- **Relevance**: states in words the design principles for an algebra: operators are local, state is distributed, thresholds are explicit.

### D5. Seeley on honeybee swarms

- Citations: T. D. Seeley, Honeybee Democracy, Princeton University Press, 2010 (confirmed existence, 273 pp). Seeley, Visscher, Schlegel, Hogan, Franks, Marshall, "Stop signals provide cross inhibition in collective decision-making by honeybee swarms", Science 335(6064), 108-111 (2012), DOI 10.1126/science.1210361 (the reference list I found gave the journal wrongly as Nature; the DOI points to Science). News summary: https://news.cornell.edu/node/271186
- **Vocabulary**: scouts, waggle dance, quorum, stop signal, cross-inhibition.
- **Operands**: scout bees committed to a site.
- **Operators**: recruit (dance), abandon (decay), inhibit (stop-signal aimed at scouts advocating the other site), quorum threshold triggers commitment. Modelled as ODEs of committed-population fractions. Confirmed: scouts committed to one box directed stop signals mainly at scouts promoting the other.
- **Claim**: swarms pick the best site with high reliability; the quorum and cross-inhibition rules explain deadlock avoidance. Well supported experimentally.
- **Relevance**: the best-documented group decision procedure with named operators: advocate, inhibit, count, commit. A strong template for human committee dynamics. Quorum: Seeley and Visscher, "Quorum sensing during nest-site selection by honeybee swarms", Behav Ecol Sociobiol 56(6), 594-601 (2004) (confirmed in validation via library catalogue).

## E. Primate and human social structure

### E1. Hinde 1976, interactions, relationships, social structure

- Citation: R. A. Hinde, "Interactions, relationships and social structure", Man 11(1), 1-17 (1976). DOI 10.2307/2800384 (JSTOR 2800384; confirmed as citation, abstract not retrieved). Book follow-up: Towards Understanding Relationships, Academic Press, 1979 (confirmed: European monographs in social psychology, 367 pp).
- **Vocabulary**: interaction, relationship, group structure, "levels of social complexity", dialectic between levels.
- **Operands** (my reading, from the framework as described in a 2022 PMC review): at level one, individuals; level two, dyads; level three, the group as a whole.
- **Operators**: the same review states that interaction history constitutes a relationship; the relationship in turn conditions future interactions; structure is the pattern of relationships and constrains both. The three-level framework is not a formal calculus; the "operators" are the up-and-down maps between levels.
- **Validation additions** (from the validator's general knowledge of Hinde's writing; the 1976 text was not retrievable in validation either, so treat as secondary): (a) social structure is defined as the content, quality and patterning of relationships, and Hinde distinguishes the observed "surface structure" from more abstract regularities; (b) each level has properties not relevant to the level below, so a relationship is not reducible to a sum or average of its interactions; (c) a relationship includes each partner's perceptions and expectations of the other, not only the record of past interactions, so "relationship = interaction history" undersells it. Confirmed via a publisher description of Hinde's later book (Individuals, Relationships and Culture, Cambridge UP, 1987): the levels are individuals, interactions, relationships and groups, all in two-way interaction with a **socio-cultural structure** of institutions, beliefs and norms, and ethological principles are said to have "severe limitations" at the higher levels.
- **Claim**: a descriptive framework; no prediction.
- **Limits**: the characterisation of the 1976 paper is secondhand; read the JSTOR text before building on it.
- **Relevance**: the most direct statement of the problem the strand has. Levels: individuals, interactions (events), relationships (histories plus expectations between a pair), group structure (content, quality and patterning of relationships), and in the later framework a socio-cultural layer of norms and institutions acting on all of them. An algebra needs operators within each level and maps between them. Hinde was an ethologist (zoologist by training) who moved into human relationships research, and his own later view is that ethology transfers well only at the lower levels; the transfer to humans is therefore not "without change", and the socio-cultural layer is exactly where roles and institutions enter.

### E2. de Waal, Chimpanzee Politics

- Citation: F. de Waal, Chimpanzee Politics: Power and Sex among Apes, Jonathan Cape / Harper & Row (1982) (publisher of the first edition not confirmed; reissued Johns Hopkins University Press, 1998 and 2007 edition). https://www.bearpondbooks.com/book/9780801886560
- **Vocabulary**: alpha, coalition, alliance, reconciliation, kiss-and-make-up.
- **Operands**: named individuals with rank and relationships, in a closed group (Arnhem colony).
- **Operators**: form coalition against X, switch sides, support, reconcile, intervene. Documented as sequences of observed events; no formal rules.
- **Claim**: dominance is won by coalition-building, not strength alone. Descriptive; the coalition and reconciliation phenomena have been widely observed in other primate groups (reconciliation was formalised separately in de Waal and van Roosmalen 1979, Behav Ecol Sociobiol 5, 55-66).
- **Limits**: one colony; narrative, not measured.
- **Relevance**: the richest catalogue of political operators with observed outcomes. Candidate source of an empirical operator list (coalition, defection, reconciliation).

### E3. Dominance hierarchies (brief)

- Citations: de Vries 1995, "An improved test of linearity in dominance hierarchies containing unknown or tied relationships", Animal Behaviour 50(5), 1375-1389 (found via https://utrecht-main-test.atmire.com/items/34c9294a-39a0-4224-8f50-3994a7bb2ae7); Landau 1951 index and Appleby 1983 test are as described there. Landau, Bull Math Biophys 13, 1-19 (1951); Appleby, Animal Behaviour 31, 600-608 (1983). Hemelrijk's DomWorld: C. K. Hemelrijk, "An individual-orientated model of the emergence of despotic and egalitarian societies", Proc R Soc B 266, 361-369 (1999) (confirmed in validation); self-reinforcing win/lose updates, and aggression intensity alone shifts the society from egalitarian to despotic. The win/lose-update idea goes back to Hogeweg and Hesper 1983 (bumblebee MIRROR model). Network view: Shizuka and McDonald, "A social network perspective on measurements of dominance hierarchies", Animal Behaviour 83, 925-934 (2012), DOI 10.1016/j.anbehav.2012.01.011 (confirmed in validation): triangle transitivity, the proportion of transitive triads.
- **Operands**: ordered pairs of individuals with win/loss counts.
- **Operators**: dyadic win; in DomWorld, win/lose updates on a scalar.
- **Claim**: many, but not all, animal hierarchies are near-linear (Landau's h >= 0.9 is the conventional cut-off for "strongly linear"; many groups fall below it, which is why de Vries' test exists). DomWorld shows hierarchy can arise without prior differences in ability.
- **Relevance**: the dominance relation is an order on operands; the winner-loser update is a minimal feedback operator. Triangle transitivity is notable for this strand because it is a statement about how dyadic relations compose into triads (A>B and B>C implies A>C, mostly), i.e. a measured composition law. Missing from this entry: Chase's work showing hierarchy formation is driven by sequences of dyadic and triadic interactions rather than individual attributes (Chase, Tovey, Spangler-Martin and Manfredonia 2002, PNAS 99, 5744-5749; not checked in validation).

### E4. Dunbar's social brain and group-size layers

- Citations: R. I. M. Dunbar, "Neocortex size as a constraint on group size in primates", J Human Evolution 22(6), 469-493 (1992), DOI 10.1016/0047-2484(92)90081-J (confirmed in validation; abstract via https://www.neuroscience.ox.ac.uk/publications/945607). The human figure of ~150 is from Dunbar 1993, Behav Brain Sci 16, 681-735. Dunbar and Shultz, "Evolution in the social brain", Science 317, 1344-1347 (2007), DOI 10.1126/science.1145463. Zhou, Sornette, Hill and Dunbar, "Discrete hierarchical organization of social group sizes", Proc R Soc B 272(1561), 439-444 (2005), DOI 10.1098/rspb.2004.2970, https://pmc.ncbi.nlm.nih.gov/articles/PMC1634986/
- **Vocabulary**: social brain hypothesis, neocortex ratio, group size, layers.
- **Operands**: an individual's relationships, bounded by cognitive capacity.
- **Operators**: none; this is a constraint, not a dynamics. The layered result: preferred group sizes with a scaling ratio close to three, roughly 3-5, 9-15, 30-45 (as reported).
- **Claim**: group size is limited by neocortex size; humans have nested layers with ratio about 3. The regression across primates is supported; the specific figure of 150 for humans is contested: Lindenfors, Wartel and Lind, "'Dunbar's number' deconstructed", Biology Letters 17, 20210158 (2021), re-ran the analysis and found 95% intervals too wide to support any single number (validator's knowledge; not opened).
- **Relevance**: gives a capacity limit and a layered structure of ties (a hierarchy of relationship classes), a ready-made constraint for any model with finite attention.

### E5. Animal social networks

- Citations: D. P. Croft, R. James, J. Krause, Exploring Animal Social Networks, Princeton University Press, 2008 (ISBN 9780691127521). H. Whitehead, Analyzing Animal Societies: Quantitative Methods for Vertebrate Social Analysis, University of Chicago Press, 2008 (ISBN 9780226895246). (Validation removed two URLs: a vague Princeton node link and a third-party ebook-store link of unclear standing; cite by ISBN.)
- **Operands**: individuals (nodes); edges from association or interaction.
- **Operators**: not dynamics; measurement operators (degree, centrality, community, association indices, permutation tests against null models).
- **Claim**: social structure is measurable and varies in ways that matter for fitness, disease and information flow. Strong methodological base; the two books differ in emphasis: Croft et al. on network analysis, Whitehead on a wider framework including association data and null-model testing.
- **Limits**: measurement and description. Whitehead is explicit that sampling and definition of "association" shape the result.
- **Relevance**: tells you how to define an edge from observations and how to test it against chance. A needed companion to any notation.

## F. Contagion and kinetics

### F1. SIR and compartmental models

- Citation: H. W. Hethcote, "The Mathematics of Infectious Diseases", SIAM Review 42(4), 599-653 (2000). DOI 10.1137/S0036144500371907. https://epubs.siam.org/doi/10.1137/S0036144500371907
- **Operands**: compartment sizes S, I, R (susceptible, infected, recovered).
- **Operators** (mass action): dS/dt = -beta S I / N, dI/dt = beta S I / N - gamma I, dR/dt = gamma I. Threshold quantity R0 = beta/gamma (for this closed SIR model). The review (confirmed) covers threshold theorems for basic reproduction, contact and replacement numbers in SIR/SEIR-type models. Origin: Kermack and McKendrick, Proc R Soc A 115, 700-721 (1927).
- **Claim**: at the start of an outbreak, infections grow iff R0 * S(0)/N > 1 (approximately R0 > 1 in a fully susceptible population). Good record for pathogens as a qualitative and short-run tool, with known failures where mixing is heterogeneous. Transmission per contact is independent, so each contact acts additively; that independence (not literally "a single exposure") is the assumption Centola and Macy relax.
- **Relevance**: the template for "a state spreads through contact". Treating a behaviour or opinion as an infection assumes single-contact transmission, which Centola and Macy below test.

### F2. Centola and Macy 2007, complex contagions

- Citation: D. Centola and M. Macy, "Complex Contagions and the Weakness of Long Ties", American Journal of Sociology 113(3), 702-734 (Nov 2007). DOI 10.1086/521848 (validator's knowledge: this is the AJS DOI for the paper). Preprint: https://repository.upenn.edu/asc_papers/590 and https://pdodds.w3.uvm.edu/research/papers/others/2007/centola2007ua.pdf
- **Vocabulary**: simple vs complex contagion, bridge width, adoption threshold.
- **Operands**: nodes in a network with an adopted/not state.
- **Operators**: adopt if at least k neighbours have adopted (or a fraction, in the paper's relative-threshold variant). Their definition: a contagion is complex if activation requires contact with two or more distinct sources; k = 1 is simple contagion. The paper runs fixed thresholds (often k = 2 or 3) on rewired lattices. Confirmed result: long ties can hinder diffusion as thresholds rise; bridge width matters, not just length.
- **Claim**: weak ties speed simple contagion but can impede complex contagion. Later experiment: Centola, "The spread of behavior in an online social network experiment", Science 329, 1194-1197 (2010), found faster and wider adoption in clustered networks. Threshold models themselves go back to Granovetter 1978 (AJS 83, 1420-1443), covered by the sociology cluster.
- **Relevance**: tells us the transmission operator has a threshold, which changes which network shapes matter. Applies directly to human adoption of norms and behaviours.

### F3. Christakis and Fowler 2007 and critics

- Citation: N. A. Christakis and J. H. Fowler, "The Spread of Obesity in a Large Social Network over 32 Years", N Engl J Med 357, 370-379 (2007). DOI 10.1056/NEJMsa066082. https://www.stat.cmu.edu/~brian/780/bibliography/01%20homophily%20and%20contagion/c&f%20obesity%20nejmsa066082.pdf
- Critiques: R. Lyons, "The Spread of Evidence-Poor Medicine via Flawed Social-Network Analysis", Statistics, Politics and Policy 2(1) (2011), https://arxiv.org/pdf/1007.2876. C. R. Shalizi and A. C. Thomas, "Homophily and Contagion Are Generically Confounded in Observational Social Network Studies", Sociological Methods and Research 40(2), 211-239 (2011), arXiv 1004.4704. Response: T. J. VanderWeele, E. L. Ogburn and E. J. Tchetgen Tchetgen, "Why and when 'flawed' social network analyses still yield valid tests of no contagion", Statistics, Politics, and Policy 3(1) (2012), DOI 10.1515/2151-7509.1050 (confirmed in validation): estimates and confidence intervals may be invalid, but lagging the alter's state an extra period gives a valid test of the null of no contagion; Shalizi commented in the same issue that the power of such tests is unknown. Also relevant: Cohen-Cole and Fletcher, BMJ 337, a2533 (2008), found "contagion" of acne, headaches and height with the same method (validator's knowledge).
- **Claim** (confirmed): odds of obesity rose 57 percent if a friend became obese (95 percent CI 6 to 123), 40 percent for a sibling, 37 percent for a spouse; no effect among neighbours; same-sex ties had greater influence.
- **Held up?** Poorly as a causal claim, though not refuted. Shalizi and Thomas show that, without strong assumptions, observational network data cannot separate contagion from latent homophily (or shared environment): the effects are not identified, which is a statement about what the data can show, not a proof there is no contagion. Lyons argues the specific statistical methods and inferences are flawed (model inconsistency, dependence between observations, and that the claimed significance tests do not support the conclusions). VanderWeele et al. argue a weaker test of "no contagion" can still be valid. The descriptive clustering survives; the causal transmission interpretation is unsupported rather than disproved.
- **Relevance**: a caution. Any algebra that models influence between persons needs a way to separate influence from selection into ties. This is a limit on inference from data, not on the algebra, but it determines what could ever validate it.

### F4. Lotka-Volterra and mass action for social encounters

- Searched specifically; the search found the general framework (mass action gives Lotka-Volterra, per-capita growth linear in densities; F. Dercole, arXiv 1411.0075, "The ecology of asexual pairwise interactions: A generalized law of mass action", which generalises mass action beyond linear density dependence) and Lotka-Volterra-type opinion dynamics (M. Aleandri and I. G. Minelli, "Opinion dynamics with Lotka-Volterra type interactions", arXiv 1811.05937, 2018; both confirmed in validation). Note the replicator equation is formally equivalent to Lotka-Volterra (Hofbauer 1981; Hofbauer and Sigmund 1998, Evolutionary Games and Population Dynamics), which ties F4 back to A2. I did not find a mainstream Lotka-Volterra literature on social groups specifically; see Unconfirmed.
- **Operands**: group sizes or densities.
- **Operators**: pairwise encounter terms x_i x_j with signed coefficients; signs define predation, competition or mutualism.
- **Relevance**: a sign pattern of an interaction matrix is a natural coarse algebra of group-to-group relations. The cost is the well-mixed assumption.

---

## Unconfirmed (not verified, do not cite as established)

Resolved in validation and moved into the main entries: Dunbar 1992 DOI (E4), Seeley and Visscher 2004 (D5), Shizuka and McDonald 2012 (E3), Hemelrijk 1999 (E3), Frank 1995 (B2), Centola and Macy DOI (F2).

- Allen and Nowak, "Games on graphs", EMS Surveys in Mathematical Sciences 1(1), 113-151 (2014): validator believes this exists as cited but did not confirm it by search. The higher-value citation is Allen et al. 2017 (see C4).
- Hinde 1976 content details (surface structure, emergent properties, expectations): see E1; secondhand.
- Lindenfors et al. 2021, Cohen-Cole and Fletcher 2008, Chase et al. 2002, Grégoire and Chaté 2004, Maynard Smith and Parker 1976, West et al. 2007: added in validation from the validator's knowledge, not search-confirmed; check before citing.
- Social-group Lotka-Volterra literature (for example intergroup or cultural competition): not found by one search; a second, narrower search is needed before claiming it exists or does not.
- Not searched: kin recognition, social insect division of labour (response-threshold models), Hamilton's later work on structured populations, Hobbs/Turchin-style cliodynamics (history cluster), Hemelrijk's wider work, Sueur and others on primate networks, Ballerini et al. is verified (PNAS 105(4), 1232-1237, 2008, DOI 10.1073/pnas.0711437105, https://pmc.ncbi.nlm.nih.gov/articles/PMC2234121/: starlings respond to about 6-7 nearest neighbours, topological not metric) but was not given its own entry above; note it as a refinement of D1/D2: the interaction neighbourhood is defined by count, not distance.

---

## What this cluster already covers

- **A real operator/operand structure for pairwise interaction**: types, a payoff table, a stability criterion, and induced dynamics (A1, A2). This is the algebra in embryo. Nothing in the strand's notes should ignore it.
- **Strategies as operators on histories** (A3, A4, C2): reciprocity, reputation and punishment as rules mapping past to action.
- **Weighted-by-relation operators** (B1): an act's value scaled by a tie weight. Hamilton's rb > c is the prototype.
- **Level decomposition** (B2, B3, E1): the Price equation (within vs between groups) and Hinde's interaction/relationship/structure give two complementary descriptions of levels.
- **A small catalogue of mechanisms for the evolution of cooperation, with explicit inequalities** (C1): five rules, each a threshold on b/c (conditions for a cooperative operator to be stable, not group-formation operators).
- **Local-rule to group-state maps** (D1 to D5): align/attract/repel, informed minority, quorum with cross-inhibition. These are operator definitions with demonstrated macro behaviour.
- **Transmission by contact with a threshold** (F1, F2).
- **Measurement of structure** (E5) and capacity limits (E4).

## What it does not cover

- **Little explicit composition.** Most models here define one interaction rule on one level. None offers a general calculus for chaining operators (A then B) or saying when two operators commute. Partial exceptions, so the claim should not be stated as "nothing": the recursive Price equation and multilevel selection (B2, B3) treat a group as a unit at the next level up, which is nesting; Couzin's zone rule (D2) composes three sub-rules by strict priority; strategies in repeated games (A3) are compositions over time; and dominance transitivity (E3) is a measured law for how dyadic relations compose into triads. A general algebra of composition is still the gap this strand would fill.
- **No unified operand.** Operands differ per model (strategy, particle, compartment, node). There is no common type for "person in a role in a group".
- **Roles and institutions are thin, not absent.** Role asymmetry exists in asymmetric-contest theory (owner/intruder, A1 note), castes and response-threshold division of labour in social insects (not covered here), and Hinde's later framework explicitly adds a socio-cultural layer of norms and institutions (E1). What biology lacks is roles as constructed, reassignable offices and rules-about-rules. Human groups are mostly made of these.
- **Language and commitment.** Promises, agreements, threats, declarations, and anything that changes the rules of the game by being said have no biological counterpart. Biology does have a substantial theory of signalling (honest signals, handicaps, cheap talk among kin: Zahavi 1975; Grafen 1990; Maynard Smith and Harper, Animal Signals, 2003), not covered here; it explains when signals are credible, which matters for threats and promises, but not institutional speech acts.
- **Transfer to humans is mostly by analogy.** The formal results (rb > c, R0 > 1, the zone model) were derived for fitness, genes, infections or fixed-speed particles. Moving them to people means replacing fitness with an editable payoff; whether the thresholds survive is untested. Christakis and Fowler show even the simplest transfer (influence as infection) could not be validated causally from observational data.
- **Validation is weak outside the lab.** Strong for honeybees, pathogens and some fish; weak for primates and humans, where the data are observational and confounded (Shalizi and Thomas).
- **Cognition is missing from the models that are tractable.** Bridging the cognitive models (Dunbar's constraint, Trivers' emotions) with the formal ones (replicator, Price) has not been done in this cluster.

## Clearly missing important work (added in validation)

- Maynard Smith 1982, Evolution and the Theory of Games (the canonical source for Hawk-Dove, Bourgeois and ESS), and Hofbauer and Sigmund 1998, Evolutionary Games and Population Dynamics (replicator = Lotka-Volterra; the mathematical reference).
- Signalling theory: Zahavi 1975, Grafen 1990, Maynard Smith and Harper 2003. The biological account of when threats and promises are credible.
- Social-insect division of labour: response-threshold models (Bonabeau, Theraulaz and Deneubourg 1996, Proc R Soc B 263, 1565-1569). The nearest biological thing to roles as operands.
- Dominance-formation dynamics: Chase et al. 2002 (PNAS); winner-loser effects. Composition of dyads into triads.
- Altruistic punishment and strong reciprocity (Fehr and Gächter 2002, Nature 415, 137-140), human experimental evidence on a punish operator; may sit in the social-psychology cluster.
- Okasha 2006, Evolution and the Levels of Selection (Oxford UP), the careful treatment of the multilevel-selection dispute in B1/B3.
- Krause and Ruxton 2002, Living in Groups (Oxford UP): why groups form at all, costs and benefits.
- Reynolds 1987 "boids" (SIGGRAPH), the precursor rule set to Couzin's zones.
- Ballerini et al. 2008 should be a full entry (D-series), not a note in Unconfirmed: it changes the neighbourhood definition from metric to topological.

None of these was search-confirmed in validation; details are from the validator's knowledge.

## Validation log (2026-10-29)

- A1 Maynard Smith and Price 1973: ✎ corrected. Citation fine; vocabulary wrongly attributed Hawk-Dove-as-V/C, Dove and Bourgeois to the 1973 paper (its strategies are Mouse, Hawk, Bully, Retaliator, Prober-Retaliator); added 1974 volume/pages, 1982 book, 1976 asymmetric contests. ESS condition, Hawk-Dove payoffs and V/C mixture are correct.
- Maynard Smith 1974: ✓ (vol/pages added).
- A2 Taylor and Jonker 1978: ✓. Replicator equation correct; noted the name is Schuster and Sigmund's (1983).
- A3 Axelrod and Hamilton 1981: ✓. T > R > P > S, 2R > T + S correct.
- A4 Trivers 1971: ✓.
- B1 Hamilton 1964: ✎ corrected. rb > c correct; added Hamilton's own k > 1/r form; sign taxonomy re-attributed (Hamilton 1964/1970, West et al. 2007); Nowak et al. reply pages 9-10 → E9-E10 with DOI.
- Nowak, Tarnita and Wilson 2010; Abbot et al. 2011; Gardner, West and Wild 2011; Queller 1992: ✓.
- B2 Price 1970: ✎ corrected. Equation correct (subscripts made explicit); recursive multilevel use attributed to Price 1972; Frank 1995 confirmed (J Theor Biol 175, 373-388) and the wrong reprint link replaced.
- B3 Wilson and Wilson 2007: ✓.
- C1 Nowak 2006: ✎ corrected. All five rules (r > c/b, w > c/b, q > c/b, b/c > k, b/c > 1 + n/m) correct; n is maximum group size; added the assumptions each rule needs; "five bonding operators" relevance downgraded as overclaim.
- C2 Nowak and Sigmund 1998: ✓.
- C3 Nowak and May 1992: ✎ corrected (update rule includes self; game parameterisation; title added).
- C4 Ohtsuki et al. 2006: ✓; Chen arXiv 1107.1513 confirmed as Ann Appl Probab 23, 637-664 (2013); Allen et al. 2017 added.
- D1 Vicsek et al. 1995: ✎ corrected. Citation, arXiv copy and rule correct; the cited "dispute" cond-mat/0703532 is a minor comment (Chen and Zhang 2007), not the order-of-transition dispute, which is Grégoire and Chaté 2004.
- D2 Couzin et al. 2002: ✎ corrected (title added; repulsion priority, blind angle, turning rate added).
- D3 Couzin et al. 2005: ✓ (title added).
- D4 Sumpter 2006, 2010: ✓.
- D5 Seeley 2010; Seeley et al. 2012: ✓. Seeley and Visscher 2004: ✓ moved from Unconfirmed (BES 56, 594-601).
- E1 Hinde 1976, 1979: ✎ corrected. Citations fine; framework was under-described (missing individuals level, expectations in relationships, emergent properties, "content, quality and patterning", and the later socio-cultural layer); "transfers to humans without change" reversed, since Hinde himself limits ethology to the lower levels. 1976 text still not read: partly ?.
- E2 de Waal 1982: ✓ (claim wording tempered; de Waal and van Roosmalen 1979 added).
- E3 de Vries 1995, Landau 1951, Appleby 1983: ✓. Hemelrijk 1999: ✓ moved from Unconfirmed. Shizuka and McDonald 2012: ✓ moved from Unconfirmed. "Hierarchies are strongly linear" ✎ corrected to "many but not all".
- E4 Dunbar 1992: ✓ DOI confirmed, moved from Unconfirmed. Dunbar and Shultz 2007; Zhou et al. 2005: ✓. Critique named (Lindenfors et al. 2021, ?).
- E5 Croft, James and Krause 2008; Whitehead 2008: ✓ (dubious URLs removed).
- F1 Hethcote 2000: ✎ corrected (threshold is R0 S(0)/N > 1; "single exposure" restated as independent per-contact transmission; Kermack and McKendrick 1927 added).
- F2 Centola and Macy 2007: ✓ (volume/pages and DOI filled; complex-contagion definition stated as ≥ 2 distinct sources); Centola 2010 cited in full.
- F3 Christakis and Fowler 2007: ✓ figures. Lyons 2011; Shalizi and Thomas 2011: ✓, critique content ✎ sharpened (non-identification is not refutation). VanderWeele, Ogburn and Tchetgen Tchetgen 2012: ✓ confirmed and summarised.
- F4 Dercole arXiv 1411.0075; Aleandri and Minelli arXiv 1811.05937: ✓ (authors added).
- Ballerini et al. 2008: ✓ (recommended for promotion to a full entry).
- Allen and Nowak 2014: ? not search-confirmed.
- Closing "What it does not cover": ✎ corrected. "Nothing chains or nests operators" and "roles absent" were overclaims (Price recursion, multilevel selection, Couzin priority, triad transitivity, role asymmetry, Hinde's socio-cultural layer); signalling theory named as an uncovered counterpart to commitment.
- No item was found to be fabricated; nothing removed except two low-quality URLs.

**Verdict.** The bibliography is reliable: every main citation checked out, and the formal statements (ESS condition, Hawk-Dove, replicator equation, Hamilton's rule, Price equation, Nowak's five rules, SIR, complex contagion) are correct as mathematics. The errors are of attribution and emphasis, the most consequential being Hinde's framework, which was reduced to three levels and declared to transfer "without change", when Hinde's own later scheme adds a socio-cultural layer of norms and institutions and warns that ethology weakens at higher levels; together with the "no composition, no roles" verdict this overstated the gap the strand would fill. Treat entries marked as validator's knowledge as leads, not confirmed citations.
