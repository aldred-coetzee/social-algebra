# Prior work 23: collective dynamics of motivated agents, with provable results

Date: 2026-10-29. Cluster survey for `social-algebra`, drive-survey phase.

Aim (Aldred, 2026-10-29): an algebra of drives that composes into equations,
yields theorems, and supports prediction or control. This file asks: where is
there mathematics of MANY agents, each with a drive or objective, from which
group-level behaviour and theorems follow? Opinion dynamics and sociophysics
are in `05-influence-opinion-control.md` and are not repeated.

Verification key: **[Crossref]** = DOI and bibliographic details returned by
the Crossref API this session; **[arXiv]** = abstract fetched from arXiv this
session (no DOI); **[read]** = I read the formulas or findings in the source
text; **[abstract]** = abstract or search summary only; **[standard]** = the
standard account from memory, not re-read, treat the exact form with care.

## Summary

Three families, and they differ sharply in how much is proved.

1. **Optimising agents with a mean-field limit** (mean-field games, the
   Kuramoto-as-game work). Each agent has an explicit objective (a cost to
   minimise), the group is a *distribution*, and there are real theorems:
   existence, sometimes uniqueness, an epsilon-Nash property for finite
   groups, and phase transitions in coupling strength. The price is
   anonymity: agents see only the distribution (relaxed by type
   distributions, major-minor and graphon MFGs; see section 14).
2. **Dynamical systems with a drive-like parameter** (Helbing panic,
   Kuramoto, consensus, Epstein fear-and-disease, Lux-Marchesi). The "drive"
   is a number in an ODE or an agent rule. Theorems exist for the abstract
   cores (Kuramoto thresholds, consensus convergence, Cucker-Smale
   flocking, awareness-epidemic thresholds) but the social-psychological
   models (panic, fear contagion, herding finance) are *simulated*, not
   proved.
3. **Learning agents with intrinsic motivation** (MARL social-influence and
   inequity-aversion rewards) and **evolutionary games with emotion
   strategies**. Here drives are explicit reward or payoff terms, and the
   results are experimental or simulation-based. The one mathematical bridge
   is **potential games**, where aligned drives give a convergence theorem.

The sharpest single fact for the algebra: a drive appears in the proved
literature as **a term in an objective or a parameter in a vector field**,
and theorems follow when the interaction has *exploitable structure*:
mean-field anonymity, a potential, monotonicity, or linear (or
linear-quadratic) coupling through a known weighted, signed or directed
network. *(Corrected in validation, 2026-10-29: the original said "only when
symmetric or mean-field". Altafini, Olfati-Saber, Dorfler-Bullo,
heterogeneous and graphon MFGs and linear-quadratic network games, section
14, all give theorems for heterogeneous, non-anonymous agents.)* What has
almost no theorem-grade treatment is drives that are typed, asymmetric *and*
nonlinear or non-monotone together (fear of *this* person, desire for *that*
role).

---

## 1. Mean-field games (Lasry-Lions; Huang-Malhame-Caines)

- Lasry, J.-M. & Lions, P.-L. (2006). Jeux a champ moyen. I, Le cas stationnaire. *C. R. Math.* 343. DOI 10.1016/j.crma.2006.09.019 [Crossref]
- Lasry, J.-M. & Lions, P.-L. (2006). Jeux a champ moyen. II, Horizon fini et controle optimal. *C. R. Math.* 343. DOI 10.1016/j.crma.2006.09.018 [Crossref]
- Lasry, J.-M. & Lions, P.-L. (2007). Mean field games. *Japan. J. Math.* 2, 229-260. DOI 10.1007/s11537-007-0657-8 [Crossref]
- Huang, M., Malhame, R. P. & Caines, P. E. (2006). Large population stochastic dynamic games: closed-loop McKean-Vlasov systems and the Nash certainty equivalence principle. *Commun. Inf. Syst.* 6(3), 221-252. DOI 10.4310/CIS.2006.v6.n3.a5 [Crossref, full title confirmed in validation]
- Huang, M., Caines, P. E. & Malhame, R. P. (2007). Large-population cost-coupled LQG problems with nonuniform agents: individual-mass behavior and decentralized epsilon-Nash equilibria. *IEEE Trans. Autom. Control* 52(9), 1560-1571. DOI 10.1109/TAC.2007.904450 [Crossref; added in validation; content standard]
- Cardaliaguet, P., Delarue, F., Lasry, J.-M. & Lions, P.-L. (2019). *The Master Equation and the Convergence Problem in Mean Field Games.* Annals of Mathematics Studies 201, Princeton UP. DOI 10.23943/princeton/9780691190716.001.0001 [Crossref; moved from Unconfirmed in validation]
- Carmona, R. & Delarue, F. (2018). *Probabilistic Theory of Mean Field Games with Applications I.* Springer. DOI 10.1007/978-3-319-58920-6 [Crossref]
- Gueant, O., Lasry, J.-M. & Lions, P.-L. (2011). Mean field games and applications. *Paris-Princeton Lectures on Mathematical Finance 2010*, LNM 2003, 205-266. DOI 10.1007/978-3-642-14660-2_3 [Crossref; the DOI I first tried, `_4`, resolved to a different paper and is discarded]

**Agent's drive.** A cost functional: each of N agents controls its own
state `X_i` (drift `a_i`) to minimise expected running cost plus terminal
cost, where the running cost depends on the *empirical distribution* of all
agents, `F(x, m)`. The "drive" is whatever `F` encodes: a desire to be near
a target, an aversion to crowds, a wish to conform.

**The coupled system** [standard]. A representative agent solves a
Hamilton-Jacobi-Bellman equation backward in time, the population density
follows a Fokker-Planck equation forward in time:

    -d_t u - nu * Lap(u) + H(x, Du) = F(x, m)        u(T, x) = G(x, m(T))
     d_t m - nu * Lap(m) - div( m * D_p H(x, Du) ) = 0   m(0) = m_0

The forward-backward structure is the defining feature: each agent
optimises *given the anticipated population path*, and the population path
is generated by those optimisers. A solution is a fixed point (a Nash
equilibrium in the N -> infinity limit).

**Theorems** [standard, Lasry-Lions]:
- Existence of solutions under mild regularity (fixed-point argument).
- **Uniqueness** under the *Lasry-Lions monotonicity condition*:
  `integral (F(x,m1) - F(x,m2)) d(m1 - m2) >= 0` for all m1, m2, **and the
  same for the terminal cost `G`**, with `H` convex in `p`; one of the two
  must be strict (e.g. `F` strictly monotone, or `H` strictly convex) to get
  uniqueness. *(Validation: the original omitted the `G` condition and the
  strictness.)* Monotone means roughly "agents dislike crowding". With
  **attractive** coupling (agents like company) the condition fails and
  multiple equilibria *can* occur; they are not guaranteed, and calling them
  "the mathematical form of herding" is an interpretation, not a theorem.
- **epsilon-Nash property** (Huang-Malhame-Caines): the mean-field optimal
  strategy used in an N-player game is an epsilon_N-Nash equilibrium,
  epsilon_N -> 0 (typically O(1/sqrt N)). The 2006 CIS paper is the
  nonlinear McKean-Vlasov setting; the LQG version, the 2007 TAC paper,
  already allows **nonuniform agents with a continuum of types** (parameter
  distribution), so MFG does not require identical agents [standard].
- Convergence of N-player Nash equilibria to the mean-field solution is the
  harder "convergence problem", solved under monotonicity via the *master
  equation* (Cardaliaguet, Delarue, Lasry, Lions 2019, above) [Crossref
  title; content standard].

**Empirical standing.** MFG is a framework, not a verified account of any
crowd. Calibration to data is thin; where it is used (economics, pedestrian
flow) it is as a structured hypothesis.

**Operand/operator.** Operand: a probability distribution `m` over agent
states (plus a value function `u` per type). Operator: the pair HJB
(best-response operator, backward) and Fokker-Planck (transport operator,
forward); the equilibrium is the fixed point of their composition. A drive is
a choice of `F`, `G` and `H`. Composing two drives is adding cost terms,
which is a well-defined operation on `F`. This is the cleanest existing
"drive composes into an equation" structure. Its limit is anonymity (see
Close).

## 2. MFG applied to crowds, pedestrians, herding, "Mexican wave"

- Lachapelle, A. & Wolfram, M.-T. (2011). On a mean field game approach modeling congestion and aversion in pedestrian crowds. *Transp. Res. B* 45(10), 1572-1589. DOI 10.1016/j.trb.2011.07.011 [Crossref]
- Gueant-Lasry-Lions lectures (above) for the crowd examples.
- Arxiv 2303.03303, "Social herding in mean field games" [arXiv-listed in a search result only; model and results unread, see Unconfirmed].

**Drive.** Aversion to crowding and a wish to reach an exit or target;
anticipation of others' paths.

**Model** [abstract, via search summary]. A macroscopic forward-backward
model derived from microscopic pedestrians who anticipate the future;
two problems, crowd *aversion* (agents avoid dense regions) and
*congestion* (movement cost rises with density). Numerical solvers;
reproduces anticipation and lane formation.

**Theorems.** Well-posedness theory comes from the general MFG results
above; the cited paper is mainly modelling and numerics [abstract].

**Mexican wave.** A Cardaliaguet lecture (Ravello 2012) lists crowd motion,
including the Mexican wave, among applications credited to Gueant, Lasry,
Lions and Lachapelle [search summary only]. I did not find the equations. The
empirical Mexican-wave model is separate: Farkas, Helbing, Vicsek (2002)
*Mexican waves in an excitable medium*, *Nature* 419, 131-132, DOI
10.1038/419131a [Crossref], an excitable-medium (threshold-and-refractory)
model fitted to stadium video data. That model has no optimising agent.

**Empirical standing.** MFG-for-crowds: demonstrations only. The
excitable-medium Mexican wave is fitted to field observations.

**Operand/operator.** As section 1, with spatial position as state; the
"fear" analogue would be a large weight on a crowd-avoidance term.

## 3. Helbing, Farkas & Vicsek (2000), escape panic

- Helbing, D., Farkas, I. & Vicsek, T. (2000). Simulating dynamical features of escape panic. *Nature* 407, 487-490. DOI 10.1038/35035023 [Crossref]
- Helbing, D. & Molnar, P. (1995). Social force model for pedestrian dynamics. *Phys. Rev. E* 51, 4282. DOI 10.1103/PhysRevE.51.4282 [Crossref]

**Drive.** Each pedestrian wants to move in a desired direction `e_i^0` at
desired speed `v_i^0`. In panic the desired speed rises. A parameter `p_i`,
which the paper says "reflects the degree of panics of individual i", mixes
own intention with imitation of neighbours. *(Validation: the original
called it "nervousness"; the paper does not.)*

**The system** [read in validation, arXiv cond-mat/0009448]. Newtonian
dynamics:

    m_i dv_i/dt = m_i (v_i^0(t) e_i^0(t) - v_i)/tau_i + sum_{j!=i} f_ij + sum_W f_iW
    e_i^0 = N[ (1 - p_i) e_i + p_i <e_j^0>_i ]          N(z) = z/|z|
    f_ij  = { A_i exp[(r_ij - d_ij)/B_i] + k g(r_ij - d_ij) } n_ij
            + kappa g(r_ij - d_ij) (Delta v_ji . t_ij) t_ij

with `g(x) = x` if touching, else 0 (body force `k`, sliding friction
`kappa`), `f_iW` wall forces, and `<e_j^0>_i` the average desired direction
of neighbours within radius `R_i`. Low `p`: individualistic; high `p`:
herding. The paper also gives an impatience law,
`v_i^0(t) = [1 - p_i(t)] v_i^0(0) + p_i(t) v_i^max` with
`p_i(t) = 1 - vbar_i(t)/v_i^0`: waiting raises the desired speed, which
feeds clogging, a positive-feedback loop.

**Results** (simulation, not theorems) [read]:
- **Faster-is-slower**: above about `v^0 = 1.5 m/s`, raising desired speed
  *lowers* the outflow and lengthens evacuation, through arching and
  clogging at the exit, **provided the friction `kappa` is large enough**.
- Neither pure individualism nor pure herding performs well; the best
  escape is **a mixture** (intermediate `p`). Pure herding sends the crowd
  to the same exit and wastes alternatives.
- Agents are injured when pressure exceeds 1600 N/m and become obstacles.

**Theorems.** None. This is a simulation result with a qualitative
phase-like transition.

**Empirical standing.** The authors compared qualitatively with reports of
disasters. Later controlled experiments (verified in validation):
- Soria, Josens & Parisi (2012). Experimental evidence of the "faster is slower" effect in the evacuation of ants. *Safety Science* 50, 1584-1588. DOI 10.1016/j.ssci.2012.03.010 [Crossref]
- Garcimartin, Zuriguel, Pastor, Martin-Gomez & Parisi (2014). Experimental evidence of the "faster is slower" effect. *Transp. Res. Procedia* 2, 760-767. DOI 10.1016/j.trpro.2014.09.085 [Crossref; abstract via search]: students leaving a room through a door; the effect is shown in the *distribution of time gaps* between successive exits (power-law tail), with competitiveness rather than speed manipulated.
- Zuriguel et al. (2014). Clogging transition of many-particle systems flowing through bottlenecks. *Sci. Rep.* 4, 7324. DOI 10.1038/srep07324 [Crossref; content standard]: one clogging description across grains, colloids, sheep and pedestrians.
- Garcimartin et al. (2015). Flow and clogging of a sheep herd passing through a bottleneck. *Phys. Rev. E* 91, 022808. DOI 10.1103/PhysRevE.91.022808 [Crossref]

So faster-is-slower is now *experimentally* supported in ants, sheep and
competitive human egress, but in the human case what is manipulated is
pushing/competitiveness, not the model's `v^0`, and some later human studies
report the effect is condition-dependent [standard]. It remains no theorem.

**Operand/operator.** Operand: the state `(x_i, v_i, p_i, v_i^0)`.
**Fear is encoded as `v^0` (urgency) and `p` (susceptibility to
imitation)**, i.e. fear as a *parameter modulating other forces*, a useful
pattern: drives as multiplicative modulators of base interaction operators.
Operator: the force-summing vector field.

## 4. Emotional contagion in evacuation and crowd models

- Tsai, J. et al. (2013). Empirical evaluation of computational fear contagion models in crowd dispersions. *Auton. Agent Multi-Agent Syst.* DOI 10.1007/s10458-013-9220-6 [Crossref]
- Kim, O'Connell, Ott & Quaini. A kinetic theory approach for 2D crowd dynamics with emotional contagion. arXiv:2012.08108 [arXiv]
- Fu, Song, Lv & Lo (2014). Simulation of emotional contagion using modified SIR model: a cellular automaton approach. *Physica A* 405, 380-391. DOI 10.1016/j.physa.2014.03.043 [Crossref in validation]
- Tsai et al. full citation [Crossref]: Tsai, Bowring, Marsella & Tambe, *AAMAS J.* 27(2), 200-217.

**Drive/state.** A scalar fear level per agent that is increased by
proximity to fearful neighbours and sets walking speed (Kim et al.) or
behaviour (Tsai et al.).

**Findings.** Tsai et al. [abstract]: of two contagion models run in the ESCAPES
simulator, the thermodynamics-style (Bosse et al.) model reproduced a real
crowd-panic video better than the epidemiological-style model; graduated
fear and proximity-based contagion were the key ingredients. Kim et al.
[abstract]: fear level modulates a trade-off between seeking less
congested areas and herding; kinetic-theory (active-particle) PDEs, operator
splitting; qualitatively reproduces a distressed-ant experiment.

**Theorems.** None stated in either abstract. Kinetic-theory papers may
carry well-posedness results; I could not read the equations (page showed
abstract only).

**Empirical standing.** Tsai et al. is a direct comparison to a real
video, uncommon in this area; one video, so weak.

**Operand/operator.** Operand: (position, velocity, fear in [0,1]).
Operator: a contagion kernel `fear_i += kappa(d_ij)(fear_j - fear_i)` or a
SIR-like transition, plus a fear -> speed/choice map. Fear is a *diffusing*
(averaging) state, structurally like DeGroot but with a nonlinearity
coupling it to motion.

## 5. Kuramoto synchronisation applied to groups

- Acebron, J. A. et al. (2005). The Kuramoto model: a simple paradigm for synchronization phenomena. *Rev. Mod. Phys.* 77, 137. DOI 10.1103/RevModPhys.77.137 [Crossref]
- Strogatz, S. H. & Mirollo, R. E. (1991). Stability of incoherence in a population of coupled oscillators. *J. Stat. Phys.* 63. DOI 10.1007/BF01029202 [Crossref]
- Strogatz, S. H. (2000). From Kuramoto to Crawford. *Physica D* 143. DOI 10.1016/S0167-2789(00)00094-4 [Crossref]
- Dorfler, F. & Bullo, F. (2011). On the critical coupling for Kuramoto oscillators. *SIAM J. Appl. Dyn. Syst.* 10. DOI 10.1137/10081530X [Crossref; abstract read]
- Neda, Z. et al. (2000). The sound of many hands clapping. *Nature* 403, 849-850. DOI 10.1038/35002660 [Crossref]

**Drive.** Each oscillator has a natural frequency `omega_i` (its own
tempo/preference) and is pulled toward the others' phase (a drive to
conform, or to be in step).

**System** [standard]:

    d theta_i / dt = omega_i + (K/N) sum_j sin(theta_j - theta_i)

with order parameter `r e^{i psi} = (1/N) sum_j e^{i theta_j}`.

**Theorems** (these are real and well developed):
- In the N -> infinity limit with a symmetric unimodal frequency density
  `g`, Kuramoto's self-consistency argument gives the critical coupling
  `K_c = 2/(pi g(0))`: a partially synchronised branch (r > 0) bifurcates
  from incoherence there [standard; formula checked]. The precise stability
  statement is subtler than "stable below, unstable above"
  *(validation correction)*: Strogatz-Mirollo 1991 showed the incoherent
  state is **linearly unstable above `K_c` but only neutrally stable below
  it** (continuous spectrum on the imaginary axis); the order parameter
  nevertheless decays below `K_c` by a Landau-damping mechanism
  (Strogatz, Mirollo & Matthews 1992, *PRL* 68, 2730, DOI
  10.1103/PhysRevLett.68.2730 [Crossref]), proved rigorously only much later.
  For the Lorentzian `g`, `r = sqrt(1 - K_c/K)` exactly; for a uniform `g`
  the transition is first-order [standard].
- Strogatz-Mirollo 1991, *J. Stat. Phys.* 63, 613-635: the linear stability
  analysis above [Crossref; content standard].
- Dorfler-Bullo 2011 [abstract read]: define "phase cohesiveness"; survey
  critical-coupling estimates; give the **first explicit necessary and
  sufficient condition on critical coupling for synchronisation in the
  finite-dimensional model for an arbitrary frequency distribution**. Note
  this is a finite-N result with *heterogeneous* frequencies; the
  "necessary" half is worst-case over distributions with a given spread, not
  for each particular distribution [standard].

**Social application.** Neda et al. (2000) [title confirmed; content from the
standard account]: audience applause spontaneously alternates between
incoherent fast clapping and synchronised slow clapping, interpreted as a
Kuramoto-type transition driven by a conflict between the wish to be loud
and the wish to be in step. This is a *measured* social synchrony phenomenon,
which is rare in this survey. Pluchino-Latora-Rapisarda also use Kuramoto
dynamics for opinion change; that belongs to cluster 05.

**Operand/operator.** Operand: a phase on the circle (a cyclic scalar) plus
a frequency. Operator: sinusoidal pairwise coupling; the group transforms
through the order parameter. The scalar-per-agent, all-to-all, symmetric
structure is what makes the threshold theorem possible.

## 6. "Synchronization of coupled oscillators is a game" (Kuramoto as mean-field game)

- Yin, H., Mehta, P. G., Meyn, S. P. & Shanbhag, U. V. (2012). Synchronization of coupled oscillators is a game. *IEEE Trans. Autom. Control* 57(4), 920-935. DOI 10.1109/TAC.2011.2168082 [Crossref; abstract via search results]

**Drive.** Each oscillator *chooses* its frequency control to minimise a
cost that penalises effort (control cost `c`) and deviation from the
population's phase (a Kuramoto-like coupling cost): self-interested
synchronisation.

**Results** [abstract, via search summary, rechecked in validation]: a
variant of the Huang (2007) large-population LQG model, an N-dimensional
controlled SDE coupled only through the cost; the states are phases of
**non-homogeneous** oscillators (heterogeneous natural frequencies). A
deterministic PDE mean-field model is shown to approximate the stochastic
system as N -> infinity; the "incoherence" Nash equilibrium (all opt out,
control zero) exists, and a **bifurcation analysis of the linearised PDE**
about incoherence gives a **critical value of the control-cost parameter:
above it, incoherence; below it (cheap control), synchronisation**. So the
phase transition is a local (linear-stability/bifurcation) result about the
mean-field PDE, plus an epsilon-Nash approximation for finite N; not a
global theorem about the N-player game. The exact critical-value formula
was not read.

**Why it matters here.** It is the single closest piece found to what the
project wants: a drive (cost) per agent, an equation for the group, and a
threshold result about collective behaviour as a function of the drive's
strength. Note what the "drive" is: a quadratic penalty. Nothing says fear
or desire.

**Operand/operator.** As sections 1 and 5 combined.

## 7. Evolutionary games with emotion or emotion-signalling strategies

- Cimpeanu, T., Pereira, L. M. & Han, T. A. (2025). The evolutionary advantage of guilt: co-evolution of social and non-social guilt in structured populations. *J. R. Soc. Interface* 22(228), 20250164. DOI 10.1098/rsif.2025.0164 [Crossref; paper text read]
- Szolnoki, A., Perc, M. & Szabo, G. (2012). Defense mechanisms of empathetic players in the spatial ultimatum game. *Phys. Rev. Lett.* 109, 078701. DOI 10.1103/PhysRevLett.109.078701 [Crossref; content not read]
- O'Connell, C. (guilt and apology), model-based account in iterated prisoner's dilemma [search-result summary only; see Unconfirmed]

**Drive.** Guilt as a cost `gamma` paid on alleviating after defection,
with a social variant that costs `gamma_s` to observe or signal guilt.

**Model (Cimpeanu et al.)** [read]. Donation game (benefit `b`, cost `c`),
iterated. Six strategies: always-C, always-D, and four guilt-prone ones
(non-social vs social; "keeps defecting" vs "switches to cooperation after
guilt"). Strategy update by Fermi pairwise imitation (`beta = 1`). Well-mixed
populations analysed by a fixation-probability Markov chain with small
mutation; structured ones (lattice N = 900, scale-free N = 1000) by
simulation.

**Findings** [read]. Well-mixed: only *social* guilt evolves, only when the
social cost is small, peaking near `gamma` ~ `c`; non-social guilt is
eliminated. Structured: clustering lets guilt-prone strategies and
cooperation persist over a much wider range of costs.

**Theorems.** Analytic part is the standard fixation-probability / stationary
distribution machinery (so exact results for the well-mixed chain, within the
low-mutation approximation); structured results are simulation.

**Empirical standing.** Pure theory; no human data.

**Operand/operator.** Operand: strategy type with an emotional state
machine. Operator: payoff map plus imitation dynamics. Emotion here is a
strategy *trigger*, not a continuous quantity.

## 8. Multi-agent reinforcement learning with intrinsic social motivation

- Jaques, N. et al. (2019). Social influence as intrinsic motivation for multi-agent deep reinforcement learning. ICML 2019. arXiv:1810.08647 [arXiv; abstract read]
- Hughes, E. et al. (2018). Inequity aversion improves cooperation in intertemporal social dilemmas. NeurIPS 2018. arXiv:1803.08884 [arXiv; formulas read]
- Leibo, J. Z. et al. (2017). Multi-agent reinforcement learning in sequential social dilemmas. AAMAS 2017. arXiv:1702.03037 [arXiv; abstract read]

**Drives (explicit reward terms).**
- Jaques: an intrinsic reward for **causal influence** on others' actions,
  measured counterfactually [read in validation, arXiv PDF Eq. 1]:

      r_t^k = alpha e_t^k + beta c_t^k
      c_t^k = sum_{j!=k} D_KL[ p(a_t^j | a_t^k, s_t^j) || sum_{a~} p(a_t^j | a~_t^k, s_t^j) p(a~_t^k | s_t^j) ]
            = sum_{j!=k} D_KL[ p(a_t^j | a_t^k, s_t^j) || p(a_t^j | s_t^j) ]

  i.e. how far j's policy conditioned on k's actual action is from j's
  marginal policy. **In expectation** it equals the mutual information
  `I(a^k; a^j | s)` (proof in their supplement); "equivalent" in the
  original overstated this. Environments: Cleanup and Harvest.
- Hughes: **inequity aversion** in the Fehr-Schmidt form [read]:

      u_i = r_i - (alpha_i/(N-1)) sum_{j!=i} max(e_j - e_i, 0)
                - (beta_i /(N-1)) sum_{j!=i} max(e_i - e_j, 0)
      e_j^t = gamma * lambda * e_j^{t-1} + r_j^t       (temporal smoothing)

  `alpha` = aversion to disadvantageous inequity (envy), `beta` = to
  advantageous (guilt-like). Best sweep: alpha = 5, beta = 0.05.
- Leibo: no extra drive; defines **sequential social dilemmas** as Markov
  games sharing the mixed-incentive structure of matrix-game dilemmas,
  with Gathering and Wolfpack as examples [read].

**Findings** [read]. Hughes: advantageous inequity aversion helps in
Cleanup (public goods), disadvantageous in Harvest (commons), the latter
working even if only one of five agents has it, but with costly fining;
delaying the intrinsic signal removes the benefit, interpreted as improved
temporal credit assignment. Jaques: influence reward improves coordination
and learning curves [abstract].

**Theorems.** None. These are empirical machine-learning results on small
gridworld games; no equilibrium or convergence guarantee is claimed.

**Empirical standing.** Benchmarks, not human behaviour. Their value for the
project is the explicit, composable form of drive-as-reward-term.

**Operand/operator.** Operand: the agent's reward vector and smoothed
reward trace. Operator: the transformation `r -> u` (a drive is a *reward
transformer*: it maps the base payoff vector to the subjective one). This is
the most algebraic framing in the cluster: drives are maps on reward vectors
and compose by function composition or addition.

## 9. Potential games

- Monderer, D. & Shapley, L. S. (1996). Potential games. *Games Econ. Behav.* 14. DOI 10.1006/game.1996.0044 [Crossref]

**Drive.** Every player has an arbitrary payoff, but there exists a single
function `Phi` on joint actions with
`u_i(a_i, a_-i) - u_i(a_i', a_-i) = Phi(a_i, a_-i) - Phi(a_i', a_-i)`
for every player and every unilateral change (exact potential).

**Theorems** [standard; checked against the known statements in validation]:
- Every finite potential game (exact, weighted or ordinal) has a
  pure-strategy Nash equilibrium (any maximiser of `Phi`).
- Finite improvement property: in every finite *ordinal* potential game
  (hence every exact one) every improvement path is finite, so sequential
  (one player at a time) better-reply and best-reply dynamics stop at a pure
  Nash equilibrium. Simultaneous updating can cycle. Fictitious play
  converges (in beliefs) in weighted potential games: Monderer & Shapley
  (1996), Fictitious play property for games with identical interests,
  *J. Econ. Theory* 68, 258-265, DOI 10.1006/jeth.1996.0014 [Crossref;
  added in validation, the original gave no source].
- A game is an exact potential game **iff each payoff is the sum of a
  common coordination (identical-interest) game and a dummy game** (payoff
  depending only on the others' actions). *(Validation: the original said
  "isomorphic to"; it is a decomposition.)* This is the formal sense in which
  aligned drives are a convergent system. Players need not be identical:
  the decomposition is per player.

**Empirical standing.** A structural property, not a behavioural claim;
useful because a convergence theorem comes free once the potential is
exhibited. Congestion games are a standard example.

**Operand/operator.** Operand: a joint action profile with the scalar
potential. A *drive* contributes a term to `Phi`; if all drives are of this
form then the **sum of drives is the potential, an actual algebra** (the
potential games form a vector space). Conflicting drives (envy, status
competition) typically fall outside the class.

## 10. Lyapunov and consensus results: Olfati-Saber, Altafini, Cucker-Smale

- Olfati-Saber, R. & Murray, R. M. (2004). Consensus problems in networks of agents with switching topology and time-delays. *IEEE Trans. Autom. Control* 49. DOI 10.1109/TAC.2004.834113 [Crossref]
- Altafini, C. (2013). Consensus problems on networks with antagonistic interactions. *IEEE Trans. Autom. Control* 58(4). DOI 10.1109/TAC.2012.2224251 [Crossref; abstract not available, content from the standard account]
- Cucker, F. & Smale, S. (2007). Emergent behavior in flocks. *IEEE Trans. Autom. Control* 52. DOI 10.1109/TAC.2007.895842 [Crossref]

**Drive.** Agree with, or (Altafini) *oppose*, neighbours. Cucker-Smale:
align velocity with neighbours, with a strength decaying in distance.

**Systems** [standard]. Consensus: `dx_i/dt = sum_j a_ij (x_j - x_i)`.
Altafini: signed weights `a_ij` (negative = antagonistic):
`dx_i/dt = sum_j |a_ij| (sgn(a_ij) x_j - x_i)`.
Cucker-Smale: `dv_i/dt = (1/N) sum_j psi(|x_i - x_j|)(v_j - v_i)` with
`psi(r) = 1/(1+r^2)^beta`.

**Theorems** [standard]:
- Olfati-Saber & Murray: Lyapunov-style convergence of average consensus for
  balanced digraphs, with time-delay bounds and switching topologies.
- **Altafini** [standard; abstract not read]: for a **connected** signed
  graph (strongly connected if directed), states converge to **bipartite
  consensus** (`|x_i|` to one common value, opposite signs across the two
  camps) **iff** the graph is *structurally balanced* (nodes split into two
  camps, friendly within, hostile between); if it is not balanced, the
  signed Laplacian is stable and all states go to zero. In the undirected
  balanced case the limit is `sigma_i (1/n) sum_j sigma_j x_j(0)` via the
  gauge transformation `x -> diag(sigma) x`. *(Validation: the connectivity
  assumption was missing; without it neither branch holds. Later work
  refines the directed, weakly connected case.)* This is the neat result for hostility:
  structural balance (Heider) is exactly the condition under which
  antagonism still gives order, a theorem linking a social-psychology
  concept to dynamics.
- Cucker-Smale: unconditional flocking (velocities converge, relative
  positions stay bounded) when `beta < 1/2`; conditional on initial data
  otherwise. (The original paper writes `psi = K/(sigma^2 + r^2)^beta`
  without the 1/N; the borderline `beta = 1/2` was added by Ha & Liu 2009
  [standard].)
- Olfati-Saber & Murray, precise form [standard]: average consensus for
  strongly connected **balanced** digraphs; under switching among such
  graphs via a common Lyapunov function; for fixed undirected graphs with a
  uniform delay `tau`, iff `tau < pi/(2 lambda_max(L))`.

**Empirical standing.** Consensus and flocking: engineering and animal
motion. Altafini: motivated by social networks but not fitted to data.

**Operand/operator.** Operand: a scalar or vector per agent. Operator: the
signed graph Laplacian. Hostility is the *sign of an edge*: a one-bit
typed operator. Cheap, and with a theorem attached, which makes it the most
algebra-ready "fear/hostility" result here.

## 11. Herding in finance: Lux-Marchesi

- Lux, T. & Marchesi, M. (1999). Scaling and criticality in a stochastic multi-agent model of a financial market. *Nature* 397, 498-500. DOI 10.1038/17290 [Crossref; content from the standard account]

**Drive.** Fundamentalists (trade on price versus value) and chartists
(optimistic or pessimistic, follow trends and each other); agents switch
group by probabilities depending on the observed profit differential and the
majority opinion among chartists. Fear and greed appear as the chartist
mood swing: pessimist to optimist.

**System** [standard]. Mean-field transition rates between groups with
exponential dependence on a "herding" parameter; a stochastic master
equation for group sizes, coupled to a price-adjustment equation.

**Results** [abstract and 1998 working-paper summary, via search, in
validation]. The news process has no power-law scaling and no volatility
dependence, yet the interacting agents generate fat-tailed returns (Pareto
exponent about 2.6 in the working paper) and volatility clustering; scaling
is explained by "a critical state which is repeatedly approached" as the
system evolves (the fundamental equilibrium intermittently losing stability
when the chartist share grows).
*(Validation: the original's "unimodal to bimodal bifurcation of the chartist
fraction" is the classic result of Lux (1995), Herd behaviour, bubbles and
crashes, *Econ. J.* 105, 881-896, DOI 10.2307/2235156 [Crossref], and of
Kirman-type recruitment models, not a confirmed result of the 1999 Nature
paper.)*

**Theorems.** Local stability analysis of the deterministic equilibrium;
the stylised-fact match is numerical.

**Empirical standing.** The best of the cluster: the claim is checked
against statistical properties of real return series (scaling exponents).
Still a fit to aggregate stylised facts, not a test of individual
fear/greed.

**Operand/operator.** Operand: group occupancy (n_optimists, n_pessimists,
n_fundamentalists). Operator: Markov switching rates driven by a social
term (majority) and an economic term (profit). A "drive" is the rate
parameter on each channel.

## 12. Epstein et al. (2008): coupled contagion of fear and disease

- Epstein, J. M., Parker, J., Cummings, D. & Hammond, R. A. (2008). Coupled contagion dynamics of fear and disease: mathematical and computational explorations. *PLoS ONE* 3(12), e3955. DOI 10.1371/journal.pone.0003955 [Crossref; text read, though the equations are images and were not extractable]

**Drive.** Fear: contagious, spreading from the sick, the scared and
the sick-and-scared; scared agents remove themselves from contact; those
removed by fear return to circulation (R_F -> S) at rate `H`, constant or
time-dependent, which is what produces the second wave.

**System** [read, from prose; equations unrecovered]. Seven mutually
exclusive states: S (susceptible to both), I_F (fear only), I_P (pathogen
only), I_PF (both), R_F (removed due to fear), R_PF (removed by fear and
infected), R (recovered, immune to fear). Disease transmits per contact at
rate `beta` from I_P and I_PF; fear at rate `alpha` from I_P, I_F and I_PF.
Removal rates `lambda_F`, `lambda_PF`, `lambda_P`. Fear does not alter
transmission directly; it acts through withdrawal. A generalised
Kermack-McKendrick SIR system. Part II: agent-based on a 120x120 lattice
with Fleers, Hiders and Ignorers.

**Findings** [read]. With `alpha = beta`, fear still precedes disease
because more states transmit fear. Settings give a **second wave**:
susceptibles self-isolate, return early as incidence drops, and reignite
the epidemic (t ~ 100). Agent model, 1800 agents, 30 runs per setting:
all ignorers 99.9% incidence; all hiders 27.8%; 90% hiders / 10% fleers 64%
incidence and corner-to-corner spread in 92% of runs; 90% hiders / 10%
ignorers 32%. Flight, not extra circulation, drives the spread.

**Theorems.** None stated. The R0 results (fear R0 versus pathogen R0) use
the next-generation operator following Diekmann, so there is a threshold
characterisation, but no theorem about the coupled behaviour.

**Empirical standing.** None. No calibration; historical cases (Memphis 1878,
Cairo 1831, cholera 1832, 1918 quarantines) cited qualitatively; calibration
is listed as future work.

**Operand/operator.** Operand: one of seven product states
(pathogen-status x fear-status). Operator: two contagion channels coupled
by shared contacts, with fear as a *second epidemic riding on the first*. A
direct, usable template for "fear as a contagious drive coupled to
another process".

## 13. Behaviour-disease coupling: awareness, vaccination, multiplex

- Funk, S., Gilad, E., Watkins, C. & Jansen, V. A. A. (2009). The spread of awareness and its impact on epidemic outbreaks. *PNAS* 106. DOI 10.1073/pnas.0810762106 [Crossref; abstract read]
- Funk, S., Salathe, M. & Jansen, V. A. A. (2010). Modelling the influence of human behaviour on the spread of infectious diseases: a review. *J. R. Soc. Interface* 7. DOI 10.1098/rsif.2010.0142 [Crossref]
- Granell, C., Gomez, S. & Arenas, A. (2013). Dynamical interplay between awareness and epidemic spreading in multiplex networks. *Phys. Rev. Lett.* 111, 128701. DOI 10.1103/PhysRevLett.111.128701 [Crossref]
- Bauch, C. T. & Earn, D. J. D. (2004). Vaccination and the theory of games. *PNAS* 101. DOI 10.1073/pnas.0403823101 [Crossref]
- Perra, N. et al. (2011). Towards a characterization of behavior-disease models. *PLoS ONE* 6. DOI 10.1371/journal.pone.0023084 [Crossref]

**Drive.** Self-protection: aware or fearful hosts reduce susceptibility.
Bauch & Earn: each individual chooses whether to vaccinate by weighing
perceived infection risk against vaccine risk, a game with a *non-optimal
Nash equilibrium* (voluntary uptake falls short of the group-optimal).

**Results.**
- **Funk et al. (abstract, read):** in a well-mixed population, the spread
  of awareness lowers outbreak size but **does not change the epidemic
  threshold**; if the response is *local* (arising in the proximity of an
  outbreak), it **can completely stop** a disease from spreading, but only if
  the infection rate is below a threshold. A pair of threshold statements
  about how a protective drive interacts with spreading.
- **Granell et al. [abstract read in validation, arXiv:1306.4136]:**
  microscopic Markov-chain analysis of awareness (virtual layer) versus SIS
  epidemic (physical layer) on a multiplex: the epidemic threshold has a
  **meta-critical point**, set by the awareness dynamics and the virtual
  network's topology, beyond which the onset rises and incidence falls.
- **Bauch & Earn** [standard]: vaccination game: Nash coverage below the
  social optimum, so the group-level outcome of individually rational fear
  is predictably suboptimal.

**Theorems.** Threshold and endemic-equilibrium statements; Funk's claims are
supported by analysis of the model, not just simulation [abstract].

**Empirical standing.** Mixed. The qualitative idea (behaviour change shapes
epidemics) is widely accepted, and Perra et al. is a characterisation
paper; direct measurement of fear-driven behaviour change is limited in
these sources.

**Operand/operator.** Operand: (infection state, awareness state) per node on
a multiplex. Operator: two coupled contagion processes, with the coupling
map `awareness -> reduced susceptibility`.

## 14. Heterogeneous and networked games with theorems (added in validation)

Added because the original Close claimed theorems need sameness. These are
the counterexamples.

- Ballester, C., Calvo-Armengol, A. & Zenou, Y. (2006). Who's who in networks. Wanted: the key player. *Econometrica* 74(5), 1403-1417. DOI 10.1111/j.1468-0262.2006.00709.x [Crossref; abstract via search; theorem statement standard]
- Bramoulle, Y., Kranton, R. & D'Amours, M. (2014). Strategic interaction and networks. *Am. Econ. Rev.* 104(3), 898-930. DOI 10.1257/aer.104.3.898 [Crossref; content standard]
- Caines, P. E. & Huang, M. (2021). Graphon mean field games and their equations. *SIAM J. Control Optim.* 59(6), 4373-4399. DOI 10.1137/20M136373X [Crossref; conference version CDC 2018, DOI 10.1109/CDC.2018.8619367]
- Carmona, R., Cooney, D., Graves, C. & Lauriere, M. (2022). Stochastic graphon games: I. The static case. *Math. Oper. Res.* 47, 750-778. DOI 10.1287/moor.2021.1148 [Crossref]
- Lacker, D. & Soret, A. (2022). A case study on stochastic games on large graphs in mean field and sparse regimes. *Math. Oper. Res.* 47, 1530-1565. DOI 10.1287/moor.2021.1179 [Crossref]
- Huang, M. (2010). Large-population LQG games involving a major player: the Nash certainty equivalence principle. *SIAM J. Control Optim.* 48, 3318-3353. DOI 10.1137/080735370 [Crossref]

**Ballester et al. (key player)** [standard]. Payoff
`u_i = alpha x_i - (1/2) beta x_i^2 - gamma sum_{j!=i} x_i x_j + lambda sum_j g_ij x_i x_j`
on an arbitrary network `G`: own concavity, global substitutability, local
complementarity weighted by *who is linked to whom*. Theorem: if the decay
`lambda/(beta+gamma)`-type parameter times the spectral radius of `G` is
below 1, there is a **unique interior Nash equilibrium, and each player's
action is proportional to her Bonacich centrality** in `G`. The key player
(whose removal most reduces aggregate activity) is the one with the highest
*intercentrality*, `b_i^2 / m_ii`. A closed-form equilibrium for
non-anonymous, heterogeneous positions.

**Bramoulle-Kranton-D'Amours** [standard]: for linear best replies on any
network, uniqueness and stability of equilibrium are governed by the
**lowest eigenvalue** of `G` (strategic substitutes), a spectral theorem.

**Graphon games and graphon MFG**: the MFG machinery with agents indexed by
a position in `[0,1]` and coupled through a graphon `W(u,v)`, so the
interaction is *who-with-whom*, not anonymous; existence, epsilon-Nash for
finite graphs sampled from `W`, and LQ solutions. **Major-minor MFG**
(Huang 2010) adds one non-anonymous dominant agent (a leader).

**Operand/operator.** Operand: an action per agent plus a weighted
(possibly directed) network. Operator: `x -> (I - delta G)^{-1} 1`, the
Bonacich resolvent. A drive here is a weight on an edge or on own-action
concavity, and **the theorem survives heterogeneity because the coupling is
linear-quadratic**: that, not sameness, is the enabling assumption.

---

## Close: what is a genuine theorem, and under what assumptions

| Result | Type | What it proves | Assumptions it needs |
|---|---|---|---|
| MFG existence/uniqueness | theorem | equilibrium of optimising agents exists; unique under monotone coupling | **anonymity (or graphon/major-minor structure), N -> infinity, rationality**; types may form a continuum |
| Huang-Malhame-Caines epsilon-Nash | theorem | mean-field strategy near-optimal in finite groups | 2006: nonlinear McKean-Vlasov; 2007: LQG with nonuniform agents |
| Kuramoto threshold, Dorfler-Bullo | theorem (Kuramoto `K_c`: self-consistency + linear stability, rigorous later) | critical coupling for synchrony | scalar phase, all-to-all or known graph; heterogeneous frequencies allowed |
| Yin et al. oscillator game | bifurcation analysis + epsilon-Nash | phase transition in the control-cost parameter | MFG assumptions, quadratic control cost, heterogeneous frequencies |
| Altafini | theorem | bipartite consensus iff structurally balanced | linear dynamics, fixed **connected** signed graph |
| Ballester et al.; Bramoulle et al.; graphon games | theorem | equilibrium = Bonacich centrality; spectral uniqueness; graphon-MFG existence | **linear-quadratic** payoffs, arbitrary known network; no anonymity |
| Olfati-Saber / Cucker-Smale | theorem | consensus / flocking convergence | linear or specific kernel, connectivity |
| Potential games | theorem | pure Nash, convergence of improvement dynamics | the existence of a potential, i.e. **aligned or symmetric drives** |
| Funk et al. awareness | analytic threshold | local awareness stops epidemic below threshold | SIR-type compartments |
| Lux-Marchesi | bifurcation + numerics | herding parameter creates fat tails | mean-field switching |
| Helbing panic | **simulation only** | faster-is-slower, herding failure | none provable |
| Epstein fear-disease | **simulation / R0 only** | fear precedes disease, second wave | uncalibrated |
| Tsai, Kim, Fu | **simulation only** | contagion models vs. video | one video |
| Guilt evolution | exact for the well-mixed Markov chain at low mutation, **simulation** otherwise | guilt can evolve | simple strategy set |
| MARL (Jaques, Hughes, Leibo) | **empirical only** | intrinsic rewards help cooperation | gridworld benchmarks |

**Pattern** *(rewritten in validation)*. Theorems appear where the model
has one of: (a) **linear or linear-quadratic coupling on a known network**
(consensus, Altafini, Ballester, Bramoulle), (b) **a mean-field or graphon
limit** (MFG, Kuramoto, Yin), (c) **a potential**, or (d) **monotonicity**.
These are assumptions of *structure*, not of sameness: heterogeneous
positions (Bonacich centrality), signed and directed edges (Altafini),
heterogeneous frequencies (Kuramoto, Dorfler-Bullo) and continua of types
(HMC 2007) all carry theorems. The original claim, that theorems need
symmetric scalar coupling, anonymity or potentials, was too strong. What is
missing is the conjunction: typed, asymmetric drives with **nonlinear,
non-monotone** coupling (fear and attraction between specific people), where
only simulation exists.

**Assumptions to watch.** Anonymity (agents see the distribution, not
individuals); symmetry of coupling; a single scalar per agent; rationality
(MFG) versus mechanical rules (Kuramoto, panic); a stationary environment;
and, for MFG uniqueness, a monotonicity condition that precisely excludes
herding.

### What exists versus what does not

**Exists.**
- Mathematics of many optimising agents with a mean-field limit, existence
  and sometimes uniqueness (MFG).
- Phase-transition theorems for collective behaviour as a function of
  coupling or cost strength (Kuramoto, Yin et al.).
- A theorem linking hostility to dynamics through structural balance
  (Altafini).
- A convergence theorem for aligned drives (potential games).
- Compartmental templates for fear as a contagious state coupled to another
  process (Epstein), and threshold results for protective behaviour
  (Funk).
- Drive as a map on rewards (Hughes inequity aversion) and as a modulator of
  other forces (Helbing's `p` and `v^0`).

**Does not exist (in what I found).**
- A single formalism in which *curiosity, fear and desire* are all
  primitives with composition laws. Each drive in the literature is a
  one-off term in one model.
- Theorems for panic, fear contagion, or emotional herding. The famous
  panic results are simulations.
- Empirical validation of any of the fear/emotion models at the level of
  individual drives; the validated ones (Lux-Marchesi, Neda, Farkas Mexican
  wave) are matched at the *aggregate* level, consistent with the earlier
  warning in `notes/2026-10-29-drives-as-the-core.md`.
- Mean-field or potential-game treatment of *typed* heterogeneous agents
  with asymmetric, **nonlinear** drives (X fears Y, Y desires Z). Linear
  versions do exist: a directed weighted network game or graphon game
  encodes "X is pulled by Y" with a theorem (section 14).
- A theory of *drive conflict* inside one agent within these frameworks;
  they sum terms or switch strategies, and none treat curiosity-versus-fear
  as a structured trade-off with proved properties.

**Implication for the algebra.** Three formal shapes carry theorems and are
candidates: a drive as a **term in a cost or potential** (adds, composes,
gives equilibrium and convergence results if aligned or monotone), as a
**signed or weighted edge** in a consensus-type operator, and as a
**rate parameter** in a compartmental or phase model. Anonymity should be
treated as a stated assumption of any theorem, not hidden.

---

## Unconfirmed

- Mexican wave in MFG: only a lecture-list mention (Cardaliaguet, Ravello 2012); equations not found.
- "Social herding in mean field games", arXiv:2303.03303: appears in search results, content unread.
- Szolnoki-Perc-Szabo (2012) content: only the title, journal and DOI were confirmed; I described no findings.
- Szolnoki & Perc on emotion-based strategies in general: not found as such.
- O'Connell, "The evolution of guilt: a model-based approach" (*Philosophy of Science*): the search result gave the abstract summary; no DOI checked.
- Bosse et al. (2009) emotion contagion model: named by Tsai et al.; the original not looked up.
- Du et al. (2018) personality-based emotion contagion: paywalled, not read; no citation details given, so not checkable.
- Neda et al. (2000) content; Altafini abstract; Lux-Marchesi equations; Olfati-Saber convergence statements; Ballester and Bramoulle theorem statements; Yin et al. critical-value formula: standard accounts only (stated forms checked against known results in validation, not re-read from source).
- Epstein et al. equations and Table 1: images, not recoverable from the page.
- Resolved in validation and removed from this list: Cardaliaguet et al. master-equation book (Crossref, now in section 1); Fu, Song, Lv & Lo (2014) (Crossref: DOI 10.1016/j.physa.2014.03.043, "Simulation of emotional contagion using modified SIR model: a cellular automaton approach", *Physica A* 405, 380-391); human faster-is-slower experiments (section 3); Granell "metacritical" (abstract read); Helbing 2000 equations (read).

## Validation log (2026-10-29)

All 31 originally cited DOIs resolved via the Crossref API; all five arXiv IDs resolved to the stated titles. No fabrications found.

- Lasry & Lions 2006 I, II; 2007 JJM ✓
- Lasry-Lions monotonicity ✎ corrected (terminal-cost `G` condition and strictness added; "multiple equilibria = herding" softened to interpretation)
- Huang, Malhame & Caines 2006 ✎ corrected (full title and pages confirmed; it is nonlinear McKean-Vlasov, not LQG; LQG nonuniform-agent paper HCM 2007 added)
- Carmona & Delarue 2018 ✓
- Gueant, Lasry & Lions 2011 (`_3` DOI) ✓
- Cardaliaguet et al. 2019 master equation ✎ moved from Unconfirmed to confirmed (Crossref)
- Lachapelle & Wolfram 2011 ✓
- arXiv:2303.03303 social herding MFG ? title confirmed, content unread
- Farkas, Helbing & Vicsek 2002 ✓
- Helbing, Farkas & Vicsek 2000 ✎ corrected (equations read and confirmed; `p_i` is the paper's "degree of panic", not "nervousness"; friction condition, 1.5 m/s threshold, optimal individualism/herding mixture, impatience law added)
- Helbing & Molnar 1995 ✓
- Faster-is-slower experiments ✎ now verified: Soria et al. 2012 (ants), Garcimartin et al. 2014 (humans), Zuriguel et al. 2014, Garcimartin et al. 2015 (sheep), with the caveat that human studies manipulate competitiveness
- Tsai et al. 2013 ✓ (authors and pages added)
- Kim et al. arXiv:2012.08108 ✓
- Fu et al. 2014 ✎ DOI found and confirmed, moved out of Unconfirmed
- Acebron et al. 2005 ✓
- Kuramoto `K_c = 2/(pi g(0))` ✓ formula; ✎ stability statement corrected (incoherence only neutrally stable below `K_c`; Landau damping, Strogatz-Mirollo-Matthews 1992 added)
- Strogatz & Mirollo 1991 ✓; Strogatz 2000 ✓
- Dorfler & Bullo 2011 ✓ (abstract read; finite-N, worst-case caveat added)
- Neda et al. 2000 ✓ bibliographic; content standard
- Yin, Mehta, Meyn & Shanbhag 2012 ✎ corrected (oscillators are heterogeneous; transition is a bifurcation analysis of the linearised PDE plus epsilon-Nash, not a global theorem)
- Cimpeanu, Pereira & Han 2025 ✓ (not re-read)
- Szolnoki, Perc & Szabo 2012 ✓ bibliographic only
- O'Connell guilt model ? unchanged, no DOI
- Jaques et al. 2019 ✎ corrected (influence reward formula added from the paper; MI equivalence is in expectation only)
- Hughes et al. 2018 ✓ (arXiv title; formula matches the known form)
- Leibo et al. 2017 ✓
- Monderer & Shapley 1996 ✓ pure NE; ✎ corrected (FIP is the ordinal-potential result and sequential only; "isomorphic" -> coordination-plus-dummy decomposition; fictitious-play source, Monderer & Shapley JET 1996, added)
- Olfati-Saber & Murray 2004 ✓ (precise conditions added, standard)
- Altafini 2013 ✎ corrected (connectivity assumption added; iff statement and limit value made precise; abstract still not read)
- Cucker & Smale 2007 ✓ (kernel normalisation and Ha-Liu borderline noted)
- Lux & Marchesi 1999 ✎ corrected (the "unimodal-to-bimodal bifurcation" belongs to Lux 1995 / Kirman-type models; replaced with the abstract's critical-state account; Lux 1995 added)
- Epstein et al. 2008 ✎ minor (rate `H` is R_F -> S return, driving the second wave; agent-based numbers re-confirmed)
- Funk et al. 2009 ✓ (abstract matches exactly)
- Funk, Salathe & Jansen 2010 ✓; Bauch & Earn 2004 ✓; Perra et al. 2011 ✓
- Granell et al. 2013 ✎ upgraded (abstract read; meta-critical point confirmed)
- Closing claim ✎ corrected (theorems need structure, not sameness: section 14 added with Ballester et al. 2006, Bramoulle et al. 2014, Caines & Huang 2021 graphon MFG, Carmona et al. 2022 graphon games, Lacker & Soret 2022, Huang 2010 major-minor MFG, all Crossref-confirmed)

Still missing and worth adding later: Kuramoto's own 1975/1984 work; Jadbabaie, Lin & Morse 2003 (switching consensus); DeGroot/Friedkin-Johnsen belong to file 05; Hegselmann-Krause bounded confidence; Galam / Granovetter threshold models of collective action; Kirman 1993 ants recruitment model.

**Verdict.** Bibliographically sound: every DOI and arXiv ID resolved to the stated work and nothing was fabricated. The mathematics was mostly right in outline but repeatedly imprecise at the level that matters for theorems (missing hypotheses in Lasry-Lions and Altafini, Kuramoto stability overstated, Yin's result promoted to a theorem, one Lux-Marchesi result misattributed). The most consequential error was the closing thesis that theorems require sameness; the corrected thesis, that they require structure such as linear-quadratic coupling on a known network, changes what the algebra should aim for.
