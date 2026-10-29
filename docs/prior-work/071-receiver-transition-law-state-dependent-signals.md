# Prior work 071: a receiver transition law x(t+1) = f(x, signal, environment) for threat, appeasement and alarm signals

Direction: D330 (deep-read). Date: 2026-10-29. Builds on file 31 (ethology, signals and drives), which flagged the gap and named the seeds.

**Honesty note, read this first.** The brief asked for a deep read of McNamara & Houston 1986, Mangel & Clark 1986, Houston & McNamara 1999 and Bradbury & Vehrencamp 2011. **None of the four could be read at source this session.** The University of Chicago page returned HTTP 403, figshare returned 403, search returned only bibliographic records, and the web-search budget ran out before a second route could be tried. Everything below that is attributed to those four works is therefore `[standard account]` (my background knowledge of the dynamic-programming method) or `[secondary]`, and **no equation here is `[read]` from a seed**. What was read at source: Kern, Laker & Radford 2017 (full text, downloaded and extracted), the one empirical test found. DOIs were checked via Crossref. This file is a map of what the transition-law literature has and what to read next, not a transcription.

## 1. Bibliographic checks (Crossref)

| Work | Check |
|---|---|
| McNamara & Houston (1986) "The common currency for behavioral decisions", *Am. Nat.* 127(3), 358-378, DOI 10.1086/284489 | Crossref OK. Publisher page paywalled (403). |
| Mangel & Clark (1986) *Ecology* 67(5), 1127-1138, DOI 10.2307/1938669 | Crossref OK (Crossref's record misspells the title "Unifield"), **but the title is "Towards a Unified Foraging Theory"**, a foraging paper. File 31 cited it as a state-dependent model, which is right in method, but it is not a signalling or alarm paper and the signal input would be an extension. The fuller treatment is the book Mangel & Clark (1988) *Dynamic Modeling in Behavioral Ecology*, Princeton (confirmed to exist by catalogue records, Open Library, not read), and Clark & Mangel (2000) *Dynamic State Variable Models in Ecology*, OUP (catalogue only, Open Library). |
| Houston & McNamara (1999) *Models of Adaptive Behaviour: An Approach Based on State*, Cambridge UP | Exists (Bristol research portal, publisher listings). Scope per catalogue and an *Auk* review: work backwards from a terminal point by dynamic programming; chapters on energy-predation trade-offs, dynamic games, state-dependent life histories. Not read. |
| Bradbury & Vehrencamp (2011) *Principles of Animal Communication*, 2nd ed., Sinauer | Book; existence confirmed by Open Library (Sinauer Associates 2011, ISBN 978-0-87893-045-6; 1st ed. 1998). Not read. Their earlier paper, Bradbury & Vehrencamp (2000) "Economic models of animal communication", *Anim. Behav.* 59, 259-268, DOI 10.1006/anbe.1999.1330, resolves in Crossref (title confirmed, not read). |
| Proctor, Broom & Ruxton (2001) "Modelling antipredator vigilance and flight response in group foragers when warning signals are ambiguous", *J. Theor. Biol.* 211, 409-417, DOI 10.1006/jtbi.2001.2353 | Crossref OK (found by title query; **not** the DOI I first guessed, which resolved to an unrelated paper, so do not cite DOIs from memory). Not read. Known only through Kern et al. 2017's description. |
| Kern, Laker & Radford (2017), *Anim. Behav.* 127, 43-51, DOI 10.1016/j.anbehav.2017.03.002 | Crossref OK. **Read in full.** |
| Pollard, Kimberly A. (2011), "Making the most of alarm signals: the adaptive value of individual discrimination in an alarm context", *Behav. Ecol.* 22(1), 93-100, DOI 10.1093/beheco/arq179 (online Nov 2010) | Crossref OK (single author). Abstract seen via the OUP article page (summarised by a fetch tool, one sentence quoted); body not read. |
| Clark, Colin W. (1994) "Antipredator behavior and the asset-protection principle", *Behav. Ecol.* 5(2), 159-170, DOI 10.1093/beheco/5.2.159 | Crossref OK (added in validation; see section 6). Not read. |

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

with p the receiver's current probability of danger and L the signal likelihoods (the signaller's reliability). The dynamic-programming state then becomes the pair (x, p), and the policy is a function of both. This is the cleanest known way a signal enters a state-dependent model. Pollard's (2011) dynamic model is the nearest published relative: it compares five receiver response strategies across environmental, life-history and social conditions, one of which responds to signallers according to their individual reliability, and "the individual discrimination strategy yielded the highest fitness under the widest range of conditions" (abstract). Whether Pollard's receivers update by Bayes' rule, as written above, is not known from the abstract; the body was not read.

**(b) The signal changes the payoff structure (a game).** Houston & McNamara's dynamic games treat the other animal's behaviour as an element of the environment of the first, and solve for an equilibrium of state-dependent strategies. Dyadic threat or appeasement signals would sit here, with the signal a component of the opponent's strategy. Described in the 1999 book's scope; not read.

**(c) The signal is an ambiguous warning in a group.** Proctor, Broom & Ruxton (2001) model vigilance and flight in group foragers when warning signals are ambiguous. Kern et al. report from it that "when the amount of energy required for survival is large, the optimal strategy is not always to respond to alarm signals but to maximize available foraging time" `[read, as a paraphrase in Kern et al. 2017; the model itself not read]`.

None of (a) to (c) is a transition law written as "x(t+1) = f(x, signal, environment)" for a **drive vector** in the sense of the strand. In each, the state is energy (and sometimes belief), and the signal acts on the action choice or on the belief, not directly on a drive.

## 4. The one empirical test found: Kern, Laker & Radford 2017 `[read]`

Wild, habituated dwarf mongooses (*Helogale parvula*), playback experiments. Experiment 1: focal foragers either supplementary-fed or not; alarm call broadcast from 1.5 m (as if from a sentinel) or from ground level (as if from a forager). Experiment 1 analysed N = 72 trials, 18 individuals, seven groups, all with aerial alarm calls (Fig. 2 legend). Experiment 2: an olfactory predator cue (river sand soaked in cat urine) or control, then an aerial or terrestrial alarm call; the response-type and latency models use **35 trials, nine individuals, six groups** (the 35 of 36 visible trials in which the focal animal responded; vigilance-after-cue measures used 30 trials, 10 individuals) `[read]`. Quoted from the text:

- "Individuals were more likely to respond to alarm calls when they had received supplementary food, and hence could prioritize minimization of predation risk over starvation." (abstract; the Results say "significantly more likely to respond").
- Sentinel-position calls were more likely to be responded to than forager-position calls; given a response, flight (rather than vigilance) was more likely after a ground-level call (Table 1, response-type model: caller position chi-square = 4.63, df 1, P = 0.031; supplementary feeding had no significant effect on response type).
- Table 1, Response model `[read]`: alarm caller position chi-square = 9.42, df 1, P = 0.002; supplementary feeding chi-square = 9.42, df 1, P = 0.002; their interaction dropped (chi-square 0.00, P = 0.989). **The two effects entered additively on the model's scale** (binomial GLMM). The sentinel and unfed coefficients were reported as 9.63 ± 4.91 and 9.63 ± 4.90 (relative to forager and fed set to zero; intercept 18.62 ± 6.92), on the link scale, with a large random-effect variance for individual ID nested in group (312.40 ± 17.67), which suggests near-separation; **treat the magnitudes as unreliable.** The text extraction used here drops minus signs, and since fed animals responded more, the unfed coefficient must be negative in the original; take signs from the Results text, not from these numbers.
- Experiment 2: a predator cue did not change the probability of fleeing versus becoming vigilant (Table 3, cue type dropped, chi-square 0.89, P = 0.346), but changed latency to return to non-vigilance in an interaction with call type (Table 3, chi-square 8.08, P = 0.004, df printed as 3; aerial call after terrestrial cue produced longer latency; the authors suggest novelty of the social information). Foragers were also more vigilant in the minute after a predator cue than after a control cue.

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

None stated as theorems in the material read. Qualitative predictions `[standard account]` that follow from the method: the optimal response to an unreliable alarm falls as the energy needed for survival rises (Proctor et al., via Kern et al.); discriminating between signallers by reliability gives the highest fitness under the widest range of conditions, with a substantial advantage except when predation pressure is very low and signaller accuracy high (Pollard 2011, abstract; an earlier draft of this line said the value rises with the variance of signallers' reliability, which the abstract does not state). Both are ordering predictions, not equations. The "asset-protection principle" (individuals with more to lose are more cautious) is Clark, C. W. (1994) "Antipredator behavior and the asset-protection principle", *Behav. Ecol.* 5(2), 159-170, DOI 10.1093/beheco/5.2.159 (Crossref confirmed in validation; the gloss is the standard one, the paper not read).

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
3. Whether McNamara & Houston's later "rules of thumb" work (state-dependent mechanisms that approximate the optimal policy) offers a **forward** form of the policy that avoids backward induction. A likely candidate is McNamara & Houston (2009) "Integrating function and mechanism", *Trends Ecol. Evol.* 24(12), 670-675, DOI 10.1016/j.tree.2009.05.011 (Crossref confirmed in validation); its content, and whether it is the paper meant, are unconfirmed (publisher page 403).
4. Clark 1994 (now cited, section 6) at source, for the principle's exact statement.
5. Whether appeasement is covered anywhere in the formal signalling literature (Maynard Smith & Harper 2003 is the first place to look, see D331).

## Validation log (2026-10-29)

- ✓ McNamara & Houston 1986, *Am. Nat.* 127(3) 358-378, DOI 10.1086/284489: Crossref matches. Not read; Kern et al. 2017 does cite it for the starvation-predation trade-off [read].
- ✓ Mangel & Clark 1986, *Ecology* 67(5) 1127-1138, DOI 10.2307/1938669: Crossref matches (Crossref misspells "Unified"). Not read.
- ✓ Mangel & Clark 1988 (Princeton) and Clark & Mangel 2000 (OUP): exist per Open Library. Not read.
- ✓ Houston & McNamara 1999 (Cambridge UP): exists per Open Library. Not read.
- ✎ Bradbury & Vehrencamp 2011: was "not checked"; existence and ISBN now confirmed (Sinauer, 2nd ed.). Not read. Their 2000 *Anim. Behav.* 59(2) 259-268 paper, DOI 10.1006/anbe.1999.1330, ✓ Crossref.
- ✓ Proctor, Broom & Ruxton 2001, *J. Theor. Biol.* 211(4) 409-417, DOI 10.1006/jtbi.2001.2353: Crossref matches; the quoted paraphrase is verbatim in Kern et al. 2017's introduction [read].
- ✎ Kern, Laker & Radford 2017, *Anim. Behav.* 127, 43-51, DOI 10.1016/j.anbehav.2017.03.002: Crossref matches; checked against the previously extracted full text [read]. Fixed: the quoted sentence is from the abstract and has no "significantly"; added experiment 1 sample (72 trials, 18 individuals, seven groups) and clarified that 35 trials / nine individuals is experiment 2's responding subset; added intercept, SEs and response-type and latency statistics; flagged that minus signs are lost in extraction (the unfed coefficient must be negative). Table 1 chi-square values (both 9.42, interaction 0.00, P = 0.989) and 312.40 confirmed. Author-accepted version is on the Bristol research portal (CC BY-NC-ND).
- ✎ Pollard 2011, *Behav. Ecol.* 22(1) 93-100: DOI 10.1093/beheco/arq179 added (Crossref), sole author Kimberly A. Pollard (UCLA). Section 3a softened (no evidence from the abstract that the model is Bayesian); section 6 prediction corrected: the abstract says discrimination wins across the widest range of conditions except at very low predation pressure with high signaller accuracy, not that its value rises with reliability variance.
- ✎ Clark 1994, asset-protection principle: citation was missing; added and Crossref confirmed, DOI 10.1093/beheco/5.2.159. Not read.
- ? McNamara & Houston 2009 "Integrating function and mechanism", DOI 10.1016/j.tree.2009.05.011: exists (Crossref), but whether it is the "rules of thumb" paper recalled is unconfirmed; left in section 10.
- ✓ Maynard Smith & Harper 2003 *Animal Signals* (OUP): exists per Open Library.
- ? "Does not exist" claims (section 9: no drive-vector transition law with estimated coefficients, no appeasement-receipt model, no estimate of G, no human application) and "no replication across species" (section 7) could not be tested: the shared web-search budget was exhausted in this pass. They stand as the original author's negative findings, unretested.
- No fabrications found. The equations in sections 2, 3a and 5 are correctly labelled as standard account or the strand's own construction; none is attributed to a seed as read, and none was checked against a seed.

**Verdict.** The file is honest about what it did and did not read, and its one [read] source, Kern et al. 2017, checks out against the text in all its numbers and attributions, with a small misquote (an inserted "significantly") and incomplete sample sizes now fixed. The real error was the Pollard 2011 prediction in section 6, which said something the abstract does not; it is corrected, and two missing citations (Pollard's DOI, Clark 1994) are supplied. The seed-derived content remains unread background and should be treated as such until the section 10 reading is done.

## Cross-checks (2026-10-29)

Method: grepped every other file in this directory for the works, authors, DOIs, equations and numbers used here (McNamara, Houston, Mangel, Clark, Bradbury, Vehrencamp, Proctor, Ruxton, Kern, Pollard, Maynard Smith & Harper, asset protection, mongoose, alarm, vigilance, dynamic programming, Bayes). Only file 31 overlaps substantively; 052 and 043 refer to this file; 28 and 29 touch vigilance without sharing a work. The six DOIs in section 1 were re-resolved on Crossref in this pass.

**Agreements**

- **File 31, "Does not exist" (the bullet on the transition law) and "Implication for the strand"** agree with sections 2, 5 and 9 here: no formal drive-state transition law driven by a conspecific signal; state-dependent dynamic programming with x(t+1) = f(x, action, environment) is the natural substrate; neither file read the seeds.
- **File 31, same bullet, on McNamara & Houston (1986)** *Am. Nat.* 127, 358-378, DOI 10.1086/284489: agrees with section 1 here. Crossref re-checked: title, volume, issue, pages match.
- **File 31, same bullet, on Bradbury & Vehrencamp (2000)** *Anim. Behav.* 59, 259-268, DOI 10.1006/anbe.1999.1330: agrees with section 1. Crossref gives "Economic models of animal communication", 59(2). Both files label the Bayesian framing `[standard account, not read]`, so the claim has the same weak standing in each.
- **File 31, further reading, on Bradbury & Vehrencamp (2011)** ("receiver-side, decision-theoretic treatment... signals as updates to the receiver's estimates"): agrees with section 3a. The Bayesian form there is still unconfirmed against the book; this is unchanged.
- **File 31, further reading, on Maynard Smith & Harper (2003)** and on appeasement as the loser's conceding strategy: consistent with section 10 item 5 here. Both treat the book as existing but unread.
- **File 31 and 071 on Houston & McNamara (1999)**: same description (book, dynamic programming, not read).
- **File 052, section 4.3 cross-reference** ("Dynamic games with state... with 071 (Houston & McNamara dynamic games)"): agrees with section 3b here. Both say the other animal's behaviour is part of the environment and that nothing was read in full.
- **Files 28 and 29 (vigilance, Pulliam 1973, Ward et al. 2011)**: no shared work or number with this file. Qualitatively compatible with section 3c, in that vigilance trades against feeding, but they model group size, not signal reliability or satiation.
- **File 043, last item of its cross-check list**: states that this file's Pollard (2011, Kimberly A.) is a different person from its own Brendan S. Pollard. Confirmed here: Crossref gives a single author, Pollard, *Behav. Ecol.* 22(1), 93-100.

**Contradictions**

- None of substance. Checked in detail:
  - **Mangel & Clark (1986)**: file 31 (the same bullet and the further-reading line) lists it as a state-dependent behavioural-ecology model with an explicit transition. This file (section 1) says it is a foraging paper whose title is "Towards a Unified Foraging Theory", with signalling as an extension. These are compatible: 31 states the method, 071 narrows the subject. Crossref confirms the title (spelled "Unifield" in its record), 67(5), 1127-1138. Reading: 071 is the more precise statement; 31's use of it as a source for the *form* of the transition law is fair, but it is not evidence about signals. Verdict: no conflict, 071's narrowing stands.
  - **Seed status**: file 31 marks McNamara & Houston 1986 and Mangel & Clark 1986 "not read". This file also did not read them. Neither file asserts an equation as read from these seeds, so the generic recursion in section 2 is not a contradiction of 31's x(t+1) = f form; it is the same standard account.
  - **Dynamic games / belief update**: file 31 names Bayesian self-assessment (Fawcett & Johnstone 2010) and sequential assessment (Enquist & Leimar 1983) as belief-update substrates; this file does not mention them, so the two files do not conflict, but section 3a here is incomplete without them. Likewise file 31's mood models (Mendl 2010, Nettle & Bateson 2012, Trimmer 2013) are absent here.
- **Not checked against the primary source**: the section 9 and 7 negative claims ("no estimate of G in any species", "no replication across species") remain unretested, as the validation log says. No other file contradicts them; file 31 makes the narrower claim of no *drive-vector* transition law, which is consistent.

## Licences of quoted and transcribed material (2026-10-30)

- **Kern, Laker & Radford (2017), *Anim. Behav.* 127, 43-51.** Licence of the copy used for reading: not determined; publisher copyright presumed. The file records only that an author-accepted version is on the Bristol research portal under CC BY-NC-ND; where the full text actually read was obtained is not recorded (audit verdict: check, provenance to be noted in `docs/licensing.md`). Use: one short quotation from the abstract (about 28 words), a short quoted paraphrase of Proctor et al. as it appears in their introduction (about 28 words), and reported test statistics (chi-square, df, P, sample sizes, coefficients and SEs from Table 1 and Table 3), which are facts and numbers rather than a transcribed table.
- **Pollard (2011), *Behav. Ecol.* 22(1), 93-100.** Not determined; publisher copyright presumed. Use: one short quotation (about 13 words) from the abstract as shown on the publisher page; body not read.
- **Proctor, Broom & Ruxton (2001), *J. Theor. Biol.* 211, 409-417.** Not determined; publisher copyright presumed. Use: cited only through Kern et al.'s quoted description (above); no text of the paper reproduced.
- **McNamara & Houston (1986); Mangel & Clark (1986, 1988); Clark & Mangel (2000); Houston & McNamara (1999); Bradbury & Vehrencamp (2000, 2011); Clark (1994); McNamara & Houston (2009); Maynard Smith & Harper (2003).** Not determined; publisher copyright presumed. Use: bibliographic citation only (Crossref and Open Library metadata, which are facts); not read, nothing quoted. The equations in sections 2, 3a and 5 are written from the standard method or are the strand's own construction, not copied from these works.
