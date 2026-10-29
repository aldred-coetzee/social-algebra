# Prior work 074: minimum driver nodes and control energy for DeGroot / Friedkin-Johnsen systems with self-loops

Direction: D402

Date: 2026-10-29. Kind: model. Question: for DeGroot and Friedkin-Johnsen (FJ) systems, which of structural controllability (Liu et al.), the self-loop correction (Cowan et al.), exact controllability (Yuan et al.) and control energy (Yan et al.) gives the right "number of nodes you must push" and "how hard", once the social structure (self-weights, symmetry, equal weights) is taken seriously. Cross-references file 05 (sections 14, 6, 12 and its validation log), 40 (behavioural approach to control), 63 (influence models), 67 (downward functions).

**Method and honesty note.** The primary sources are mostly paywalled or blocked to this session's fetch tool, and the web-search budget ran out mid-task, so some intended searches were not run. What was actually read:
- **Cowan et al. 2012**: the PLoS ONE full text was fetched, but through a summarising fetch, and the equations are images on the page, so the equations were not transcribed; the definitions and propositions are described in words. Tag [read, summarised, equations not transcribed].
- **Liu, Slotine, Barabasi 2011; Yuan et al. 2013; Yan et al. 2012; Muller & Schuppert 2011**: Crossref metadata confirmed [read]; abstract-level paraphrase only for Yan (Europe PMC search). The PMC and Nature full texts returned browser checks, 403s or paywall redirects. Their theorems are tagged [from abstract/standard account], and where I state a theorem's form it is the textbook form of the result, not a transcription. *(Validation 2026-10-29: Yuan et al.'s full text was read via the Europe PMC full-text XML service, so section 1.5 is now [read].)*
- **Kempe-Kleinberg-Tardos, Olfati-Saber & Murray, Hegselmann et al.**: Crossref confirmed for the first two (title, venue, pages, year). Hegselmann et al.'s Crossref lookup failed (my DOI guess was wrong; file 05 gives a JASSS URL instead); validation found it at DOI 10.18564/jasss.2847. None read for this file.
- **Everything in section 3 and the numerical checks in section 4 is derived here** (tag [derived]) from standard linear-systems facts (Kalman rank, PBH test, Gramians), and the small numerical checks were run this session with numpy. These are my own working, not published results, and need an independent check before anything is built on them.

**Summary.** Four published answers to "how many driver nodes?" disagree, and the disagreement is not noise: each uses a different assumption about **what the diagonal of the system matrix looks like and whether weights are generic**. For social systems all those assumptions are questionable.
1. Liu et al. (no self-dynamics, generic weights): the count is set by a maximum matching and the degree distribution.
2. Cowan et al. (each node has its own, generic, first-order dynamics): **one** independent input signal suffices for essentially any network. *(Corrected in validation: in Cowan et al.'s Proposition 1 that single input is broadcast to all nodes, their "control hub"; it is not one driver node in Liu et al.'s sense. The single-node version is derived in 4.1 and follows from Lin's theorem, see 1.2.)*
3. Yuan et al. (exact controllability, arbitrary fixed weights): the count is the **maximum geometric multiplicity** of the eigenvalues of the system matrix (algebraic multiplicity when the matrix is diagonalizable, e.g. undirected). Symmetric, equal-weight structure, which is exactly what social models have, makes this large.
4. Yan et al.: whatever the count, the **energy** needed can be astronomically large, so the number of drivers is not the practical quantity.

For the algebra the useful result is that "structural" controllability is the wrong object for FJ/DeGroot networks (it holds almost everywhere and almost never tells you anything), and the right objects are (a) repeated eigenvalues from symmetry in the social structure, which decide the **exact** driver count, and (b) the Gramian, which decides the **cost**.

---

## 1. The sources

### 1.1 Liu, Slotine, Barabasi (2011)
- Liu, Y.-Y., Slotine, J.-J., Barabasi, A.-L. (2011). Controllability of complex networks. *Nature* 473, 167-173. DOI 10.1038/nature10011 [Crossref confirmed].
- **Their vocabulary.** Controllability, driver nodes, structural controllability, maximum matching, degree distribution.
- **Operators/equations** [from abstract/standard account; file 05 section 14 carries the same]: dx/dt = A x + B u on a directed graph. Structural controllability is Lin's: Lin, C.-T. (1974). Structural controllability. *IEEE Trans. Automatic Control* 19(3), 201-208, DOI 10.1109/TAC.1974.1100557 [Crossref confirmed; not read] - controllable for generic weights iff every node is reachable from an input and there is no dilation. N_D = max(N - |M*|, 1), M* a maximum matching of the bipartite out-copy/in-copy representation; the unmatched nodes are the drivers.
- **Empirical standing.** Further Barabasi-group work (Posfai, M., Liu, Y.-Y., Slotine, J.-J., Barabasi, A.-L., "Effect of correlations on network controllability", *Sci. Rep.* 3, 1067, 2013, DOI 10.1038/srep01067 [Crossref confirmed; arXiv 1203.5161 abstract read]) finds that clustering and modularity have "no discernible impact" on N_D, while degree correlations can produce linear, quadratic or no dependence depending on the kind of correlation; the results "help narrow" the gap between predicted and observed driver counts. This is the same line of work, so not independent.
- Related: Liu, Slotine & Barabasi, "Control centrality and hierarchical structure in complex networks", *PLoS ONE* 7(9), e44459 (2012), DOI 10.1371/journal.pone.0044459 [Crossref confirmed; arXiv 1203.2655 abstract read]: a node's control centrality (how large a subnetwork it alone can control) in a loop-free directed network is determined by its position in the hierarchy.

### 1.2 Cowan et al. (2012)
- Cowan, N. J., Chastain, E. J., Vilhena, D. A., Freudenberg, J. S., Bergstrom, C. T. (2012). Nodal dynamics, not degree distributions, determine the structural controllability of complex networks. *PLoS ONE* 7(6), e38398. DOI 10.1371/journal.pone.0038398 [Crossref confirmed; title and venue match]. Full text fetched, summarised [read, summarised].
- **Setup [read, described not transcribed].** Each node has its own intrinsic dynamics plus coupling through the adjacency matrix plus inputs through a coupling matrix. Liu et al.'s model is the special case of every node being a pure integrator (infinite time constant).
- **Claim [read, quoting the fetch's rendering].** "upon inclusion of first-order self dynamics, essentially all real networks are structurally controllable" with a single input (N_D = 1), "irrespective of network topology". The sentence is in the body, comparing with Liu et al., not in the abstract.
- **Proposition 1 [read, described].** For a network with nonzero self-loops, one independent input suffices - but the input is the "control hub", "a single driver node attached to *all nodes*"; the proof says "connect a single input to all nodes". *(Corrected in validation: this file previously said "one driver node", which reads as B = e_i. Cowan et al.'s formulation "explicitly allows each independent input to be connected to multiple (and possibly all) nodes".)* Proof idea: set the self-loops to distinct nonzero values and all edges to zero; the result is diagonal with distinct eigenvalues, hence controllable by the broadcast input; since controllability is a generic property, it then holds on a dense set of weights. The single-**node** version (B = e_i) is a different, stronger claim; it follows from Lin's theorem [derived here, not Cowan's]: self-loops on every node rule out dilations, so a single node input is structurally controllable iff every node is reachable from it.
- **Proposition 2 [read, described].** The same holds (N_D = 1) for nodal dynamics given by arbitrary proper rational transfer functions with generic coefficients, the single input connected to a power-dominating set; the authors call their generalisation "at best incremental" over the work of Sundaram and Hadjicostis (their refs 24-25, 2010 and 2008; not opened here).
- **Their stated point on what is the right question.** Controllability is generic; the relevant questions are whether a system is "almost uncontrollable", "almost unobservable", or has "almost pole-zero cancellations". That is a statement about conditioning, which is Yan et al.'s territory.
- **Caveat that matters here.** The argument is about **generic** parameters. It is silent on structured, non-generic social weights (equal weights, symmetric ties) and on actuation limits. Also, "the number of inputs limits the number of setpoints that may be specified" [read] - the authors themselves flag this.

### 1.3 Muller & Schuppert (2011)
- Muller, F.-J., Schuppert, A. (2011). Few inputs can reprogram biological networks. *Nature* 478, E4. DOI 10.1038/nature10543 [Crossref confirmed: title, authors, volume, page, year]. This is a Matters Arising comment on Liu et al.; **the text was not read**. File 05 describes it as a related objection. I cannot state its argument from a source I read, so I do not.

### 1.4 Yan, Ren, Lai, Lai, Li (2012)
- Yan, G., Ren, J., Lai, Y.-C., Lai, C.-H., Li, B. (2012). Controlling complex networks: how much energy is needed? *Phys. Rev. Lett.* 108, 218703 (published 23 May 2012). DOI 10.1103/PhysRevLett.108.218703 [Crossref confirmed, authors from Crossref; file 05 omitted the author list].
- **Abstract level only [from abstract, paraphrased by Europe PMC fetch].** It derives and validates scaling laws for lower and upper bounds on the control energy, aiming to move from controllability to control. I did **not** read the scaling exponents; do not quote them from here.
- The underlying framework is the standard minimum-energy result (section 3.4), which I state as textbook, not as Yan et al.'s transcribed result.

### 1.5 Yuan, Zhao, Di, Wang, Lai (2013)
- Yuan, Z., Zhao, C., Di, Z., Wang, W.-X., Lai, Y.-C. (2013). Exact controllability of complex networks. *Nature Communications* 4, 2447. DOI 10.1038/ncomms3447 [Crossref confirmed: DOI, journal, year **and author list** (validation 2026-10-29)]. Europe PMC ID PMC3945876; full text read in validation via the Europe PMC full-text XML [read].
- **Abstract [read].** An exact controllability framework "based on maximum multiplicity" for the fewest driver nodes needed to fully control networks with arbitrary structure and link weights; it reproduces structural controllability for directed networks with structural matrices; "dense networks with identical weights are difficult to be controlled" (the earlier paraphrase "hard to control" was not a quotation).
- **Theorem [read; checked against the full text in validation].** Their equation (3): for **arbitrary** A, N_D = max_i mu(lambda_i), mu(lambda_i) = N - rank(lambda_i I_N - A) the geometric multiplicity, where N_D is the minimum number of independent drivers/controllers, min rank(B). If A is diagonalizable (e.g. undirected networks) this is the maximum algebraic multiplicity. They prove necessity and sufficiency via PBH, and give a column-elimination procedure that identifies the driver nodes. They note the lower-bound half "has been implied in linear control theory" and earlier literature, so section 3.2 below is a re-derivation of a known bound, not new. Simplified forms: equation (5), for large **sparse** networks with few self-loops, N_D = max{1, N - rank(A)} (corrected: this file had "N - rank(A)" for "the sparse/directed case"; it is the sparse case, directed or not, and carries the max with 1); equation (6), for dense networks with identical weights w, N_D = max{1, N - rank(wI_N + A)}. Their Table 1 gives the unweighted undirected star N_D = N - 2 and the complete graph N - 1, and states the star (and chain) agree with structural controllability.

### 1.6 Seed works not re-read
- Kempe, Kleinberg & Tardos (2003), *Proc. KDD '03*, 137-146, DOI 10.1145/956750.956769 [Crossref confirmed]. In file 05 section 12. Not a continuous-control result: influence maximisation on discrete cascades, monotone submodular spread, greedy within (1 - 1/e). Different object (seed selection, not input signals). Not used in the model below.
- Olfati-Saber & Murray (2004). Consensus problems in networks of agents with switching topology and time-delays. *IEEE TAC* 49, 1520-1533, DOI 10.1109/TAC.2004.834113 [Crossref confirmed]. Not read. Its role here is the consensus dynamics dx/dt = -L x [standard account], which is DeGroot in continuous time; the connection to controllability with leaders is not from this paper.
- Hegselmann, R., Konig, S., Kurz, S., Niemann, C., Rambau, J. (2015). Optimal opinion control: the campaign problem. *JASSS*, DOI 10.18564/jasss.2847 [Crossref confirmed by bibliographic search in validation; not read]: strategic broadcaster under bounded-confidence dynamics; nonlinear, optimal-control formulation. Not read here. It is the nonlinear counterpart to this linear analysis.
- Kalman (1960 and after): the rank condition and the Gramian. Standard account; no specific paper cited because none was opened.

---

## 2. The model (specified, not coded)

**Operands.** N agents; state x_i(t) in R (an opinion, or one coordinate of a drive vector - the vector case is the Kronecker product with the same graph structure; see file 63). Weights W = (w_ij) row-stochastic, w_ij >= 0, sum_j w_ij = 1. Susceptibility Lambda = diag(lambda_i), lambda_i in [0, 1). Prejudice vector x0 (fixed).

**FJ, discrete time** [standard account; file 05 sections for FJ]:

x(t+1) = Lambda W x(t) + (I - Lambda) x0.

The fixed point is x* = (I - Lambda W)^{-1} (I - Lambda) x0. Since rho(Lambda W) <= max lambda_i < 1, the system is stable, and y = x - x* obeys y(t+1) = A y(t) with A = Lambda W. **DeGroot** is lambda_i = 1 (A = W, marginally stable, eigenvalue 1 on the consensus direction).

**FJ, continuous time (one common choice; the choice matters, see 4.1).** dx/dt = (Lambda W - I) x + (I - Lambda) x0.

**DeGroot, continuous time.** dx/dt = -L x with L = I - W (or the graph Laplacian). [standard account]

**Control inputs.** An exogenous signal u(t) in R^m enters through B in R^{N x m}: x(t+1) = A x(t) + B u(t) (+ affine term). Each column of B is one **driver** channel. Two physically different actuations exist and must not be conflated:
- **Additive input** (a campaign message that shifts a node's opinion by u): B = e_i, the case analysed below.
- **Clamping / zealot** (a node whose state is held fixed): this deletes a node's dynamics instead of adding an input; it is **not** controllability in the Kalman sense, and the reachable set is the convex hull of the clamped values under row-stochastic W. Out of scope here; recorded as a different operator.

**Operators for the algebra.** inject_i(u) (adds u to node i), and the structural operators already in the strand (tie change = edit W; stubbornness change = edit lambda_i). Control is then a question about the pair (A, B), where A is the algebra's group-structure element and B is the set of nodes the controller can touch.

---

## 3. Results

### 3.1 Kalman and PBH [standard account]
(A, B) is controllable iff rank[B, AB, ..., A^{N-1}B] = N, equivalently (PBH, Popov-Belevitch-Hautus) rank[zI - A, B] = N for every eigenvalue z of A. For discrete time with singular A, "reachable" (from zero) and "null-controllable" differ; the rank test above is for reachability, which is the property we want (drive to any target).

### 3.2 Lower bound from multiplicity [derived; proof sketch]
**Claim.** If A has an eigenvalue z of geometric multiplicity mu, then m >= mu input channels are necessary for controllability.
*Proof.* rank(zI - A) = N - mu, and adding m columns raises the rank by at most m, so rank[zI - A, B] <= N - mu + m. PBH needs N, so m >= mu. QED.
For symmetric A the geometric equals the algebraic multiplicity, so repeated eigenvalues of a symmetric (undirected, reciprocal) social structure directly force N_D >= max multiplicity. This is the lower-bound half of the Yuan et al. result, which Yuan et al. themselves describe as already implied in linear control theory; sufficiency is proved in Yuan et al. 2013 [read], not here.

### 3.3 Automorphism obstruction [derived]
**Claim.** If a permutation matrix P != I with PA = AP satisfies P b = b for the single input column b, then (A, b) is uncontrollable.
*Proof.* P A^k b = A^k P b = A^k b, so every Krylov vector lies in the fixed subspace of P, which is a proper subspace. QED.
This is a re-derivation of a published result: Rahmani, A., Ji, M., Mesbahi, M., Egerstedt, M. (2009). Controllability of multi-agent systems from a graph-theoretic perspective. *SIAM J. Control Optim.* 48(1), 162-186, DOI 10.1137/060674909 [Crossref confirmed; abstract read: "we show how the symmetry structure of the network, characterized in terms of its automorphism group, directly relates to the controllability", extended to several leaders via equitable partitions]. Their setting is leader-follower consensus (Laplacian, i.e. continuous DeGroot); the exact form of their theorem was not read here. Meaning: **a single driver cannot control a network that has a graph symmetry fixing the driver.** Social structure is full of such symmetries (two identical followers of one leader, two members with the same ties and the same susceptibility). This is where the Cowan result stops applying: it needs generic distinct self-loops, and equivalent members have equal self-loops by definition.

### 3.4 Control energy [standard account; Yan et al.'s scaling not read]
For stable A and a single column b, the controllability Gramian is W_c = sum_{k>=0} A^k b b^T (A^T)^k, the solution of the discrete Lyapunov equation W_c - A W_c A^T = b b^T. The minimum input energy (sum of |u|^2) to steer y from 0 to y_f in the infinite-horizon limit is y_f^T W_c^{-1} y_f. For unit-norm targets this ranges from 1/lambda_max(W_c) to 1/lambda_min(W_c). The conditioning of W_c, not the rank, is the cost. Targets x_f must be expressed as y_f = x_f - x*, so the **prejudices x0 fix where the free point sits**; pushing against x0 is what costs.

### 3.5 Verdict table (what each theory predicts for the same structure)
For an undirected star (hub plus N - 1 leaves) with a row-stochastic weighted adjacency:

| Theory | Driver count | Source status |
|---|---|---|
| Liu matching, no self-dynamics, undirected | N - 2 [derived by hand: the bipartite maximum matching has size 2] | method [from abstract/standard account]; count [derived], and agrees with Yuan et al.'s Table 1 statement that the star's N - 2 matches structural controllability [read] |
| Cowan, generic distinct self-loops | 1 input (broadcast to all nodes in Cowan's Prop. 1) | [read, summarised]; the single-**node** version is this file's own result (Lin's theorem plus 4.1 numerics), not Cowan's |
| Yuan exact, dx/dt = -L x (Laplacian eigenvalue 1 has multiplicity N - 2) | N - 2 | theorem [read]; lower bound [derived], and verified numerically. (Yuan's own Table 1 uses the adjacency matrix, eigenvalue 0 of multiplicity N - 2, and gets the same N - 2.) |
| Discrete FJ, W with zero diagonal, equal lambda | N - 2 observed (numerics) | [derived numerically] |

The first row requires a note: I derived the matching by hand and did not run an implementation; Yuan et al.'s Table 1 independently gives N - 2 for the star and says it agrees with structural controllability, so the count is now corroborated.

---

## 4. Numerical checks run this session [derived; numpy, rank tolerance 1e-9]

All use additive input, B a set of unit columns, with controllability tested by the Kalman rank and the minimum number of driver nodes found by trying every subset.

### 4.1 Where the self-loop matters
- Star graph with N = 4, 5, 6, system matrix A = -L (continuous DeGroot): Laplacian spectrum {0, 1 (mult. N - 2), N}; minimum drivers found 2, 3, 4 = N - 2 [matches 3.2].
- Complete graph K5, -L: spectrum {0, 5 (mult. 4)}; minimum drivers 4 = N - 1. Matches the "dense, identical weights are hard" abstract claim, and 3.2.
- Path on 3 nodes, -L: driver at an end gives rank 3 (controllable); driver at the middle gives rank 2 (uncontrollable). Matches 3.3 (the swap of the two ends fixes the middle).
- Discrete FJ on the star, W with **zero diagonal**, equal lambda = 0.5: eigenvalues {0.5, -0.5, 0, ...}; minimum drivers N = 4: 2, N = 5: 3 (= N - 2). Giving each node a different lambda but keeping the zero diagonal does **not** give one-driver controllability: with N = 5, hub driver rank 2, leaf driver rank 3. The reason: in A = Lambda W the diagonal is zero; the susceptibility-weighted prejudice term (1 - lambda_i) x0_i lies in the affine part, **not in A**, so FJ's "stubbornness self-loop" is **not** a self-loop in the Cowan sense.
- Same star, but with W given **distinct positive self-weights** w_ii (a person's own prior opinion weighting differing between members): leaf or hub driver rank 5 of 5, i.e. a single driver suffices. This is Cowan's mechanism (distinct self-dynamics), operating through w_ii and not through the prejudice term; note it is tested here with a single-**node** input, which is stronger than Cowan's broadcast input.
- Same with **equal** self-weights and equal lambda: leaf driver rank 3 of 5. So the Cowan escape needs the self-weights to differ, which is a strong assumption for a social group (people in the same role are assumed alike).
- Continuous-time DeGroot with distinct node time constants (dx/dt = -diag(1/tau) L x), random tau: leaf driver rank 5 of 5.

**Consequence for the strand.** Two natural modelling choices (unit-diagonal continuous FJ, or zero-diagonal W) both give identical or zero self-loops and hence bring back the multiplicity penalty. Whether real people supply the "distinct self-dynamics" that rescues one-driver control is an empirical question about heterogeneity, and it is also the thing the energy numbers below make costly.

### 4.2 Energy in the one-driver case that Cowan makes possible
Same star, distinct susceptibilities and self-weights (the one-driver case), a leaf as driver, infinite-horizon Gramian from the discrete Lyapunov equation:

| N | spectral radius of A | lambda_max(W_c) | lambda_min(W_c) |
|---|---|---|---|
| 5 | 0.654 | 1.14 | 2.0e-8 (energy ratio about 5.6e7) |
| 10 | 0.645 | 1.02 | numerically zero (negative at machine precision) |
| 20 | 0.621 | 1.02 | numerically zero |
| 30 | 0.495 | 1.03 | numerically zero |

So a network that is **controllable by one driver in the rank sense** needs roughly seven orders of magnitude more energy to push the worst direction than the best at N = 5, and beyond N = 10 the Gramian is singular in double precision. Random seeds, one draw each; the pattern is what matters, not the digits. *(Validation re-run with a different seed: N = 5 lambda_min about 3e-10, lambda_max about 1.0; N = 10, 20, 30 lambda_min numerically zero or negative at 1e-17. The pattern reproduces; the digits in the table do not, as expected.)* This is the Yan et al. message demonstrated on the model that matters here, and it is also the "almost uncontrollable" warning of Cowan et al. I did not compare to Yan's scaling law, which I have not read.

---

## 5. Operand/operator translation for the algebra

- **Operand.** The pair (A, B): the group-structure element A = Lambda W (who listens to whom, how stubbornly) and the actuation set B (which members a controller can touch). A is the strand's group element; B is the controller's reach.
- **Operators.** inject_i; structural edits to W and Lambda; the Gramian as a derived element giving cost of reaching a target.
- **Theorem-shaped statements to prove or test (none proved here beyond 3.2, 3.3):**
  1. Lower bound: minimum drivers >= max geometric multiplicity of A (proved, 3.2).
  2. Symmetry obstruction: a driver fixed by a non-trivial automorphism of (A) cannot control (proved, 3.3). This gives a **role-equivalence criterion**: members with identical (row of W, lambda) are interchangeable, and a controller must treat them as a class or break the symmetry.
  3. Conjecture: for a group built from r role classes (members within a class identical), the exact driver count is governed by the class sizes: at least size - 1 drivers within each class of equal members that have no distinguishing outside link. Not proved; in line with 3.2 (an eigenvalue of multiplicity size - 1 on the antisymmetric subspace of a class), but I did not prove it for non-symmetric W.
  4. Cost is the real quantity: the worst-direction energy 1/lambda_min(W_c) should be tracked, not just the rank.
- **For the drive layer.** A drive vector replaces x_i; the same results hold with A = (Lambda W) tensor C where C is the drive-coupling matrix (files 49, 70 for measured coupling matrices). Then repeated eigenvalues can arise from C as well as from W. Not worked here.

---

## 6. Empirical standing (be blunt)

- None of these papers tests control on a human group. Liu et al.'s examples are biological, technological and some social-communication networks, not opinion data [file 05]. Cowan et al.'s result is analytical (no simulations on real networks reported on the page [read, summarised]); Yan et al. is theory plus simulation [abstract].
- The only empirical neighbourhood is the FJ experimental literature (file 05, file 63) and the failure of individual-level prediction (file 05, file 07). A controllability claim assumes A is known; for a real group A is estimated with large error, and **the energy results say the conditioning amplifies exactly that error**: if W_c is near singular, a small error in A changes which directions are cheap.
- Linear-time-invariant opinion models ignore bounded confidence, saturation (opinions live in [0,1]) and input limits, all of which make "any target is reachable" false in a social setting. The nonlinear problem is Hegselmann et al.'s campaign problem; it is open whether anything like 3.2 and 3.3 survives there.

## 7. What exists vs what does not

**Exists.**
- A rigorous map from graph structure to the minimum number of additive drivers for linear networks, with competing answers and a clear reason for the disagreement (what is on the diagonal; generic versus structured weights).
- The standard Gramian account of cost, with a scaling-law paper (Yan) that I did not read.
- A simple, proved lower bound by eigenvalue multiplicity and a symmetry obstruction, which do not rely on any of the genericity assumptions.

**Does not exist (found).**
- A study of controllability of FJ opinion dynamics specifically under non-generic **social** weights (role-equivalent members). I did not find one; given the search budget I cannot say none exists. *(Qualified in validation: for continuous DeGroot/consensus with equal weights it does exist - the leader-follower consensus literature, Rahmani et al. 2009 (see 3.3), ties controllability to the automorphism group and equitable partitions, which is exactly role-equivalence. The FJ-specific claim was not re-tested: the validation pass had no search budget left.)* File 05's dismissal of Liu et al. for social systems stands; this file adds that Cowan's escape is also fragile.
- Any treatment of control with **bounded** inputs and **saturating** opinions on group networks in the linear-controllability literature.
- Any measurement of the conditioning of a real group's A. No data.
- Any test, on human groups, that a driver-node count predicts a successful intervention.

## 8. Unconfirmed

- The argument of Muller & Schuppert 2011 (text not read).
- Yan et al.'s scaling exponents and their precise setup (text not read).
- Cowan et al.'s equations (images; not transcribed). Proposition 2's wording was re-checked in validation and matches the corrected paraphrase in 1.2.
- Conjecture 3 of section 5.
- Equivalence of the discrete and continuous FJ controllability claims in 4.1 beyond the cases tested (N = 4 to 6 stars, K5, path3; one random seed for the distinct-parameter cases).
- Rahmani et al. 2009 is now confirmed (abstract) to relate the automorphism group to controllability, so 3.3 is credited to them (see 3.3); the exact theorem statement was not read. Tanner (2004) and Parlangeli & Notarstefano were not checked and are not cited.
- Sundaram & Hadjicostis (2008, 2010), credited by Cowan et al.: not opened; no bibliographic details given here.

## Validation log (2026-10-29)

- ✓ Liu, Slotine, Barabasi 2011, *Nature* 473, 167-173, 10.1038/nature10011: Crossref confirms authors, venue, pages. Matching formula is the standard account.
- ✎ Lin 1974, *IEEE TAC* 19(3), 201-208, 10.1109/TAC.1974.1100557: the structural theorem was credited only as "Lin's"; full citation added (Crossref confirmed, not read).
- ✎ Posfai et al. 2013, *Sci. Rep.* 3, 1067, 10.1038/srep01067: Crossref confirmed. The arXiv abstract says degree correlations give linear, quadratic or no dependence and "help narrow" the gap; the old wording "degree correlations do ... to explain gaps" overstated it.
- ✎ Liu, Slotine, Barabasi 2012, control centrality: venue was unchecked; it is *PLoS ONE* 7(9), e44459, 10.1371/journal.pone.0044459 (Crossref confirmed, arXiv abstract read).
- ✎ Cowan et al. 2012, *PLoS ONE* 7(6), e38398, 10.1371/journal.pone.0038398: Crossref confirmed. **Main correction**: Proposition 1's single input is a "control hub" broadcast to all nodes, not one driver node. The single-node claim is this file's own derivation (Lin's theorem plus numerics). The quoted sentence is from the body, not the abstract, and the setpoints quote was reworded to match the paper.
- ? Muller & Schuppert 2011, *Nature* 478, E4, 10.1038/nature10543: Crossref confirmed. Argument still not read, and the file correctly makes no claim about it.
- ✓ Yan, Ren, Lai, Lai, Li 2012, *PRL* 108, 218703, 10.1103/PhysRevLett.108.218703: Crossref confirms authors and date. Scaling laws still not read.
- ✎ Yuan, Zhao, Di, Wang, Lai 2013, *Nat. Commun.* 4, 2447, 10.1038/ncomms3447: Crossref confirms the author list, so it is no longer unconfirmed. Full text read via Europe PMC. Corrected: the general theorem uses geometric multiplicity for arbitrary A. The sparse formula is max{1, N - rank(A)} for sparse networks, not "the directed case". The abstract quote was fixed. The paper says the lower bound was already implied in control theory.
- ✎ Rahmani, Ji, Mesbahi, Egerstedt 2009, *SIAM J. Control Optim.* 48(1), 162-186, 10.1137/060674909: Crossref confirmed and abstract read. It ties controllability to the automorphism group, so 3.3 is now credited to them as prior work. It also qualifies the "does not exist" claim for DeGroot and consensus.
- ✓ Kempe, Kleinberg, Tardos 2003, KDD, 137-146, 10.1145/956750.956769: Crossref confirmed.
- ✓ Olfati-Saber & Murray 2004, *IEEE TAC* 49(9), 1520-1533, 10.1109/TAC.2004.834113: Crossref confirmed.
- ✎ Hegselmann, Konig, Kurz, Niemann, Rambau 2015, *JASSS*, 10.18564/jasss.2847: full author list and DOI added (Crossref bibliographic match, not read).
- ✓ Derived results: 3.1-3.4 are correct as standard linear-systems facts. All of 4.1 was re-run independently: star N = 4, 5, 6 gives 2, 3, 4; K5 gives 4; path3 end/middle gives 3/2; FJ zero-diagonal star; distinct-lambda hub/leaf ranks 2/3; distinct self-weights 5/5; equal self-weights leaf 3. All reproduce. 4.2 reproduces in pattern but not in its digits, as the file already warned.
- ? The "nothing exists" claim for FJ under role-equivalent weights could not be tested by search: the validation pass's web-search budget was exhausted.

**Verdict.** The file is honest and its own mathematics and numerics check out, and every DOI resolves to the stated work with no fabrications. The substantive error was attributing a one-*node* driver result to Cowan et al., whose single input is broadcast to all nodes. Yuan et al.'s theorem was also stated loosely, and two "derived" results (the multiplicity lower bound and the automorphism obstruction) are known results, now credited to Yuan et al.'s account and to Rahmani et al. 2009.

## Cross-checks (2026-10-29)

Direction D402. Checked against the validated files in this directory by grep for the same works, authors and equations (Liu, Cowan, Yuan, Yan, Rahmani, Muller-Schuppert, Posfai, Kempe, Olfati-Saber, Hegselmann, Friedkin-Johnsen, Gramian, controllability). The works in this file appear in full only in file 05; file 63 supplies the FJ equations; files 40, 43, 04 touch controllability only in passing.

### Agreements
- **FJ equation and fixed point.** Section 2 here, `x(t+1) = Lambda W x(t) + (I - Lambda) x0`, `x* = (I - Lambda W)^{-1}(I - Lambda) x0`, matches file 63 section 2 (P&T 2017 eq. 20, [read]) and file 05 section 4 (`y(t+1) = A W y(t) + (I - A) y(1)`, same fixed point). Notation: file 05's A is this file's Lambda.
- **Stability.** 074 section 2 (rho(Lambda W) <= max lambda_i < 1 is stable) agrees with file 63 section 5 (stable for any W_d when Lambda_d < I) and file 63 Theorem 21 (P-dependent block Schur stable).
- **DeGroot.** `x(t+1) = W x(t)`, row-stochastic, equals file 05 section 3; the continuous form `dx/dt = -Lx` equals file 05 section 5 (Abelson, via P&T) and file 04 (Hansen-Ghrist diffusion).
- **Liu, Slotine, Barabasi 2011.** Citation (Nature 473, 167-173, 10.1038/nature10011), the Lin 1974 structural condition and `N_D = max(N - |M*|, 1)` agree with file 05 section 14. Both flag the claim as [from abstract/standard account] and the social interpretation as by analogy.
- **Muller & Schuppert 2011, Nature 478, E4, 10.1038/nature10543.** Same citation; both files describe it only as a related objection and neither claims to have read its argument.
- **Yan et al. 2012, PRL 108, 218703, 10.1103/PhysRevLett.108.218703.** Same citation; both say structural controllability does not bound control energy. Crossref re-checked in this cross-check: DOI resolves, published 23 May 2012, issue 21.
- **Cowan et al. 2012, PLoS ONE 7(6), e38398.** Same citation. Both say the Liu result rests on nodes having no self-dynamics and that self-loops form a maximum matching. Primary text re-fetched: "the set of all self-links ... is itself a maximum matching; all nodes in the network are then matched nodes".
- **Hegselmann, Konig, Kurz, Niemann, Rambau 2015, JASSS 18(3).** File 05 section 15 gives JASSS 18(3), 18 (URL .../18/3/18/18.pdf); this file's DOI 10.18564/jasss.2847 resolves in Crossref (JASSS issue 3). Same work, same authors. Both describe it as the nonlinear optimal-control (campaign) problem under bounded confidence.
- **Kempe-Kleinberg-Tardos 2003, KDD '03, 137-146, 10.1145/956750.956769.** Same citation. Both treat it as seed selection with a (1 - 1/e) greedy guarantee, not continuous control. 074 section 1.6 calls the file 05 location "section 12"; it is actually section 15 (see Contradictions item 2).
- **Olfati-Saber & Murray 2004** appears only here and in 074's own citation; no conflict. No other file mentions Yuan et al. 2013, Rahmani et al. 2009, Posfai et al. 2013 or Lin's paper by title, so those have no overlap to check.
- **Controllability as structure.** File 40 (behavioural approach: controllability as patching of trajectories, linear time-invariant) and file 43 (Fong thesis ch. 5, structural controllability, abstract-level) are consistent with 074 treating controllability as a linear-systems property; no numbers in common.

### Contradictions
1. **Cowan et al.: what the single input is.**
   - File 05 section 14: once self-loops exist "the self-loops form a perfect matching and **one** driver node suffices".
   - This file section 1.2 and 3.5: Proposition 1's single input is broadcast to all nodes (a "control hub"); the single-node claim is derived here from Lin's theorem and numerics (section 4.1).
   - Primary source (PLoS ONE full text, fetched): proof says "connect a single input to all nodes", the paper calls it "a single driver node attached to all nodes", and the matching is called "a maximum matching". Verdict: **074 is right; file 05's "one driver node" is loose** (the matching wording is also "maximum", not "perfect", though for the self-loop set they coincide). File 05 not edited, as instructed; it should be corrected there. The conclusion that Liu's degree-distribution result dissolves stands in both.
2. **Cross-reference to file 05 sections.** 074's header cites file 05 "sections 14, 6, 12" and section 1.6 puts Kempe in "section 12". In file 05, section 6 is Hegselmann-Krause (fine), section 12 is Granovetter, and Kempe and Hegselmann et al. are in **section 15**. Verdict: file 05's numbering is authoritative; 074's reference should read 14, 6, 15. Also section 2 says "file 05 sections for FJ": that is section 4.
3. **File 05 section 4, susceptibility tied to self-weight (`a_ii = 1 - w_ii`).** This file section 4.1 treats Lambda and the self-weight w_ii as independent and notes the prejudice term is not a Cowan self-loop. This is not a contradiction (file 05 itself says "the general form above treats them as independent") but it matters: under Friedkin's own specification, distinct lambda_i imply distinct w_ii, so the "zero diagonal with distinct lambda" case in 4.1 is outside Friedkin's specification and the "distinct self-weights" case is the realistic one. Verdict: consistent; 074 section 4.1 should be read with that caveat.

No numerical results in 074 (section 4) overlap with any other file. Unresolved: none.
