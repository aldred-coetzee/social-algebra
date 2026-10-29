# Prior work 071: a receiver transition law x(t+1) = f(x, signal, environment) for threat, appeasement and alarm signals

Direction: D330 (deep-read). Date: 2026-10-29. Builds on file 31 (ethology, signals and drives), which flagged the gap and named the seeds.

**Honesty note, read this first.** The brief asked for a deep read of McNamara & Houston 1986, Mangel & Clark 1986, Houston & McNamara 1999 and Bradbury & Vehrencamp 2011. **None of the four could be read at source this session.** The University of Chicago page returned HTTP 403, figshare returned 403, search returned only bibliographic records, and the web-search budget ran out before a second route could be tried. Everything below that is attributed to those four works is therefore `[standard account]` (my background knowledge of the dynamic-programming method) or `[secondary]`, and **no equation here is `[read]` from a seed**. What was read at source: Kern, Laker & Radford 2017 (full text, downloaded and extracted), the one empirical test found. DOIs were checked via Crossref. This file is a map of what the transition-law literature has and what to read next, not a transcription.

## 1. Bibliographic checks (Crossref)

| Work | Check |
|---|---|
| McNamara & Houston (1986) "The common currency for behavioral decisions", *Am. Nat.* 127(3), 358-378, DOI 10.1086/284489 | Crossref OK. Publisher page paywalled (403). |
| Mangel & Clark (1986) *Ecology* 67(5), 1127-1138, DOI 10.2307/1938669 | Crossref OK, **but the title is "Towards a Unified Foraging Theory"**, a foraging paper. File 31 cited it as a state-dependent model, which is right in method, but it is not a signalling or alarm paper and the signal input would be an extension. The fuller treatment is the book Mangel & Clark (1988) *Dynamic Modeling in Behavioral Ecology*, Princeton (confirmed to exist by catalogue records, not read), and Clark & Mangel (2000) *Dynamic State Variable Models in Ecology*, OUP (catalogue only). |
| Houston & McNamara (1999) *Models of Adaptive Behaviour: An Approach Based on State*, Cambridge UP | Exists (Bristol research portal, publisher listings). Scope per catalogue and an *Auk* review: work backwards from a terminal point by dynamic programming; chapters on energy-predation trade-offs, dynamic games, state-dependent life histories. Not read. |
| Bradbury & Vehrencamp (2011) *Principles of Animal Communication*, 2nd ed., Sinauer | Book, not checked. Their earlier paper, Bradbury & Vehrencamp (2000) "Economic models of animal communication", *Anim. Behav.* 59, 259-268, DOI 10.1006/anbe.1999.1330, resolves in Crossref (title confirmed, not read). |
| Proctor, Broom & Ruxton (2001) "Modelling antipredator vigilance and flight response in group foragers when warning signals are ambiguous", *J. Theor. Biol.* 211, 409-417, DOI 10.1006/jtbi.2001.2353 | Crossref OK (found by title query; **not** the DOI I first guessed, which resolved to an unrelated paper, so do not cite DOIs from memory). Not read. Known only through Kern et al. 2017's description. |
| Kern, Laker & Radford (2017), *Anim. Behav.* 127, 43-51, DOI 10.1016/j.anbehav.2017.03.002 | Crossref OK. **Read in full.** |
| Pollard (2011), "Making the most of alarm signals: the adaptive value of individual discrimination in an alarm context", *Behav. Ecol.* 22(1), 93-100 | Bibliographic record and abstract summary only (RePEc). DOI not checked. |

## 2. What the state-dependent method is `[standard account]`

Their vocabulary: **state variable** (energy reserves, body condition, for a receiver also a belief about the world), **action** (the behavioural option chosen), **terminal reward** (fitness at the horizon T), **reproductive value / state-dependent value function** V(x,t), **common currency** (McNamara & Houston's term: all behavioural options are compared on the one scale of expected contribution to future fitness), **dynamic programming / backward induction**.

Generic form, as the method is normally stated `[standard account, not read in either seed]`. With state x, time t, action a, a stochastic next state X':

    F(x, t) = max over a of  E[ F(X'(x, a, t), t+1) ]          (backward recursion)
    F(x, T) = Phi(x)                                            (terminal fitness)

and the transition is a state equation of the form x' = x - cost(a) + gain, with gain occurring with probability lambda(a) and death with probability mu(a), where lambda and mu depend on the action and on the environment. Two points that matter for us:

1. **The state-transition law is part of the model's specification, not an output.** The modeller writes x' = f(x, a, environment). What is solved for is the policy a*(x,t). So the literature gives a ready form of "x(t+1) = f(x, action, environment)", but the optimisation lives one level up: it picks the action given the state. Our direction asks for the other thing, the **response of the state to a received signal**, and in this framework that appears only indirectly (below).
2. **Common currency gives a price for every state change.** Because F(x,t) values each state, the marginal value dF/dx converts any drive-like change (hunger, safety) into the same units. This is the formal content of "common currency" `[standard account]` and is the nearest thing in the literature to a **conserved, comparable scale across drives**. It is a single-agent, single-currency scale; it assumes fitness is the currency, and a human algebra would have to say what replaces fitness.

## 3. Where a signal enters `[standard account / secondary]`

Three routes appear in the literature as far as can be told without the seeds.

**(a) The signal changes the environment variable (belief update).** The receiver does not observe whether a predator is present (e in {0,1}). The signal s is evidence. The standard Bayesian receiver update, written here from first principles and attributed in spirit to Bradbury & Vehrencamp's decision-theoretic framing `[standard account, their text not read]`:

    p' = p * L(s | e=1) / ( p * L(s | e=1) + (1 - p) * L(s | e=0) )

with p the receiver's current probability of danger and L the signal likelihoods (the signaller's reliability). The dynamic-programming state then becomes the pair (x, p), and the policy is a function of both. This is the cleanest known way a signal enters a state-dependent model, and it matches Pollard's (2011) dynamic model, whose receiver strategies include discriminating between signallers by their individual reliability (the strategy that discriminates among individuals did best across the widest range of conditions; abstract only).

**(b) The signal changes the payoff structure (a game).** Houston & McNamara's dynamic games treat the other animal's behaviour as an element of the environment of the first, and solve for an equilibrium of state-dependent strategies. Dyadic threat or appeasement signals would sit here, with the signal a component of the opponent's strategy. Described in the 1999 book's scope; not read.

**(c) The signal is an ambiguous warning in a group.** Proctor, Broom & Ruxton (2001) model vigilance and flight in group foragers when warning signals are ambiguous. Kern et al. report from it that "when the amount of energy required for survival is large, the optimal strategy is not always to respond to alarm signals but to maximize available foraging time" `[read, as a paraphrase in Kern et al. 2017; the model itself not read]`.

None of (a) to (c) is a transition law written as "x(t+1) = f(x, signal, environment)" for a **drive vector** in the sense of the strand. In each, the state is energy (and sometimes belief), and the signal acts on the action choice or on the belief, not directly on a drive.

## 4. The one empirical test found: Kern, Laker & Radford 2017 `[read]`

Wild, habituated dwarf mongooses (*Helogale parvula*), playback experiments. Experiment 1: focal foragers either supplementary-fed or not; alarm call broadcast from 1.5 m (as if from a sentinel) or from ground level (as if from a forager). Experiment 2: an olfactory predator cue (river sand soaked in cat urine) or control, then an aerial or terrestrial alarm call; **35 trials, nine individuals** `[read]`. Quoted from the text:

- "Individuals were significantly more likely to respond to alarm calls when they had received supplementary food, and hence could prioritize minimization of predation risk over starvation."
- Sentinel-position calls were more likely to be responded to than forager-position calls; given a response, flight (rather than vigilance) was more likely after a ground-level call.
- Table 1, Response model `[read]`: alarm caller position chi-square = 9.42, df 1, P = 0.002; supplementary feeding chi-square = 9.42, df 1, P = 0.002; their interaction dropped (chi-square 0.00, P = 0.989). **The two effects entered additively on the model's scale** (binomial GLMM). The fed/unfed and sentinel/forager coefficients were reported as 9.63 ± 4.9, on the link scale, with a large random-effect variance for individual ID (312.40), which suggests near-separation; **treat the magnitudes as unreliable.**
- Experiment 2: a predator cue did not change the probability of fleeing versus becoming vigilant, but changed latency to return to non-vigilance in an interaction with call type (aerial call after terrestrial cue produced longer latency; the authors suggest novelty).

What this gives the strand: (i) a clean demonstration that the receiver's response to the same signal depends on **receiver state (satiation)** and on **signaller context (position as a proxy for reliability)**, in line with the state-dependent framework; (ii) **no interaction** between the two, weak evidence for additive combination of state and reliability on the response scale; (iii) the authors themselves cite McNamara & Houston 1986 and Lima & Dill 1990 for the starvation-predation trade-off and Proctor et al. 2001 for the theory.

**Limits, bluntly.** One species, one study, small samples, binomial responses (respond or not), no estimate of a transition function. Nothing here estimates x(t+1) given x(t) and the signal; it estimates the probability of an action given state and context, and the "state" is a two-level manipulation. It is a test of the direction of an effect, not of a functional form.

## 5. Candidate form for the algebra (synthesis, not from any source)

Marked as the strand's own construction. Combining routes (a) and the state-equation of section 2, with a drive vector d in place of energy x and a belief vector b in place of p:

    b' = U(b, s)                   (belief update by Bayes, route a)
    d' = d + G(d, b', e) - D(d)    (drive step: gain G from the situation, decay D)
    action = argmax over a of  V(d', b', a)    (policy, one level above)

where s is the received signal (threat, appeasement, alarm), e the environment. For the three signal types:

- **Alarm** raises danger belief (p up); the drive effect (fear) follows through G, and the action response is moderated by the hunger-like state exactly as in section 4.
- **Threat** from a known sender changes the payoff of the dyadic game (route b), not only the belief.
- **Appeasement** is a signal that lowers the receiver's expected cost of the encounter; in this scheme it is a likelihood change (the signal is evidence that the sender will not attack), which is why a **reliability** parameter (the L above) is unavoidable: an appeasement signal that carries no information about future behaviour is cheap talk.

What the form does and does not buy: it separates **belief update** (signal as evidence) from **drive update** (state as input to policy), which is the "gate versus shift" distinction file 31 asked for, now with an explicit place for each. It does not tell us what G is, and no source found estimates one.

## 6. Theorems or derived predictions

None stated as theorems in the material read. Qualitative predictions `[standard account]` that follow from the method: the optimal response to an unreliable alarm falls as the energy needed for survival rises (Proctor et al., via Kern et al.); the value of discriminating between signallers rises with the variance of their reliability (Pollard, abstract). Both are ordering predictions, not equations. The "asset protection principle" (Clark 1994: individuals with more to lose are more cautious) is the textbook corollary of this family; **I did not verify it** and could not name the citation with confidence.

## 7. Empirical standing

Mixed and thin. State-dependent models are the dominant theory in behavioural ecology, but fits to data are usually qualitative (direction of effect). Kern et al. is the single direct test found here; replication across species was not located. Whether human drive states update according to anything like this is untested; the models carry no human data.

## 8. Operand/operator translation

- Operands: an agent with a state vector (drives) and a belief vector.
- Operators: **signal receipt** s as a map on (d, b); **action** as a map from state to a change in the environment; **decay** D.
- Reliability L of a sender is a **relation** (sender to receiver), not an attribute of either; this is the only place the framework needs an edge, which is useful for the group layer.
- The terminal-reward / backward-induction machinery is a **control** layer; the algebra could use only the forward transition and treat policy as given, which avoids committing to fitness as the objective.

## 9. What exists versus what does not

**Exists:** a mature method for a state-transition-plus-policy model (dynamic programming over a state, with environment as a stochastic input); a Bayesian route for a signal to update a receiver's belief about the world; at least two dynamic models of receiver response to alarm signals (Proctor et al. 2001; Pollard 2011); one field experiment consistent with state-by-context effects (Kern et al. 2017).

**Does not exist (as far as found):** a transition law in which a **conspecific signal acts on a drive vector** with estimated coefficients; any model of **appeasement** receipt in this framework (all alarm-oriented); any estimate of G, the effect size of a signal on state, in any species; any treatment of **many senders** (Pollard's discrimination gets nearest); any human application.

## 10. Unconfirmed (read next)

1. All four seeds, at source: McNamara & Houston 1986 (the state equation and the common-currency argument), Mangel & Clark 1986 and 1988, Houston & McNamara 1999 (the dynamic-games chapters especially), Bradbury & Vehrencamp 2011 (the receiver chapter; confirm the Bayesian form I gave in section 3a is theirs).
2. Proctor, Broom & Ruxton 2001 and Pollard 2011 in full, for the exact state equations and parameters.
3. Whether McNamara & Houston's later "rules of thumb" work (state-dependent mechanisms that approximate the optimal policy) offers a **forward** form of the policy that avoids backward induction. I recall such a paper (around 2009) but could not confirm its details or DOI; one search for it was refused for budget.
4. The asset protection principle citation.
5. Whether appeasement is covered anywhere in the formal signalling literature (Maynard Smith & Harper 2003 is the first place to look, see D331).
