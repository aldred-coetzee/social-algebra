# Prior work 046: Atkinson & Birch's Dynamics of Action at source, against Revelle's CTA restatement

Direction: D068

Date: 2026-10-29. Kind: deep-read. Question: the instigating, consummatory and inhibitory forces, negaction and the switching rule in Atkinson & Birch (1970), compared with Revelle's CTA restatement. Cross-references: 16 (section 5 and 6, whose claims are checked and in two places corrected below), 15, 20, 27.

**Method and honesty note (read this first).** The 1970 book (Atkinson & Birch, *The Dynamics of Action*, Wiley) is not on the open web and was **not read**. What was read in full this session, downloaded and extracted with pdftotext: (a) Revelle, "Cues, Tendencies and Actions" working draft of 10/10/08 (cta.pdf, with the R code in its appendix); (b) Revelle & Condon (2015) author draft (rc.jrp14.pdf), whose section on social interaction contains a table of simulated talk shares; (c) Blankenship, Tumlinson & Sims (1995), a teaching simulation of the *full* DOA, which states the equations and the dominance rule procedurally; (d) the first two pages of Slade & Rush (1991), which quote the book with page numbers; (e) Revelle's achievement lecture handout. Everything about the 1970 book is therefore **second-hand but from people who implemented it** (Blankenship was a student of the theory and published empirical tests of it). Tags: `[read]` = read in one of the five sources above, source named; `[derived]` = derived here from the stated equations, not found in any source; `[simulated]` = reproduced by a short Python replication of Revelle's R code, run this session (scratch only, nothing committed); `[standard account]` = not checked.

---

## 0. Verified references

| Work | Verification |
|---|---|
| Atkinson, J. W. & Birch, D. (1970). *The Dynamics of Action*. New York: Wiley. | Book; no DOI. Cited by every source above. Not read. |
| Atkinson, J. W. (1957). Motivational determinants of risk-taking behavior. *Psychological Review* 64(6), 359-372. doi:10.1037/h0043445 | Crossref resolves (APA, issue "6, Pt.1"). Not read; the equations come from Revelle's handout and CTA paper. |
| Atkinson, J. W. & Birch, D. (1974). The dynamics of achievement-oriented activity. In Atkinson & Raynor (eds.), *Motivation and Achievement*, Washington, DC: Winston, 271-325. | Page range and publisher confirmed from Slade & Rush's (1991) reference list `[read]`; chapter pages 297-301 are cited by Slade & Rush for the "inhibition delays, cannot suppress" result. Not read. |
| Revelle, W. (2008 draft). Cues, Tendencies and Actions: the Dynamics of Action revisited. https://personality-project.org/revelle/publications/cta.pdf | Downloaded and read in full `[read]`. Working draft "10/10/08", unpublished. Its reference list prints Kuhl & Blankenship (1979) as *Psych. Rev.* **85**, 239-248; Crossref says the paper is vol. **86**(2), 141-151, doi:10.1037/0033-295x.86.2.141. The draft's volume and pages are wrong. |
| Revelle, W. & Condon, D. M. (2015). A model for personality at three levels. *J. Research in Personality* 56, 70-81. doi:10.1016/j.jrp.2014.12.006 | Crossref resolves. Author draft https://personality-project.org/revelle/publications/rc.jrp14.pdf read `[read]`; the published version not checked against it. The PDF itself is headed "This is a draft version as submitted to JRP. Please do not cite without …" `[read]`; numbers below are from the draft. |
| Blankenship, V., Tumlinson, J. & Sims, M. A. (1995). A STELLA-II teaching simulation of the dynamics of action model. *Behavior Research Methods, Instruments, & Computers* 27(2), 244-250. doi:10.3758/BF03204740 | Crossref resolves; PDF https://link.springer.com/content/pdf/10.3758/BF03204740.pdf read in full `[read]`. |
| Slade, L. A. & Rush, M. C. (1991). Achievement motivation and the dynamics of task difficulty choices. *J. Personality and Social Psychology* 60(1), 165-172. doi:10.1037/0022-3514.60.1.165 | Crossref resolves; PDF https://interruptions.net/literature/Slade-JP&SP91.pdf; introduction read `[read]`, method and results only skimmed. |
| Kuhl, J. & Blankenship, V. (1979). The dynamic theory of achievement motivation: from episodic to dynamic thinking. *Psychological Review* 86(2), 141-151. doi:10.1037/0033-295x.86.2.141 | Crossref resolves (title and pages confirmed). Not read. |
| Revelle, W. & Michaels, E. J. (1976). The theory of achievement motivation revisited: the implications of inertial tendencies. *Psychological Review* 83(5), 394-404. doi:10.1037/0033-295x.83.5.394 | Crossref resolves. Not read. |
| Revelle, W. (1986). Motivation and efficiency of cognitive performance. In Brown & Veroff (eds.), *Frontiers of Motivational Psychology*, Springer, 107-131. doi:10.1007/978-1-4684-6341-5_7 | Crossref resolves (chapter 7, pp. **107**-131; both Revelle papers print 105-131). Book chapter, not read. |
| psych::cta (R). https://www.rdocumentation.org/packages/psych/versions/2.5.6/topics/cta | Documentation page re-fetched in validation (summarising fetch): title "Simulate the C(ues) T(endency) A(ction) model of motivation", says "The learning part of the cta model is still under development"; its references are A&B 1970, Revelle 1986, Revelle 2008, Revelle & Condon 2015, and **not** Brown & Revelle 2021. The 2008 draft's appendix gives the earlier source verbatim `[read]`. |
| Blankenship, V. (1987). A computer-based measure of resultant achievement motivation. *J. Personality and Social Psychology* 53(2), 361-372. doi:10.1037/0022-3514.53.2.361 | Crossref resolves. Not read; content from Blankenship et al. 1995 and Revelle & Condon 2015. |
| Blankenship, V. (1992). Individual differences in resultant achievement motivation and latency to and persistence at an achievement task. *Motivation and Emotion* 16, 35-63. doi:10.1007/BF00996486 | Crossref resolves. Not read; content from Blankenship et al. 1995. |
| Sorrentino, R. M., Smithson, M., Hodson, G., Roney, C. J. R. & Walker, A. M. (2003). The theory of uncertainty orientation: a mathematical reformulation. *J. Mathematical Psychology* 47(2), 132-149. doi:10.1016/S0022-2496(02)00032-9 | Crossref resolves. Not read. Sorrentino (1993), "The warm look in control motivation and social cognition", in *Control Motivation and Social Cognition*, Springer, 291-322, per Revelle & Condon's reference list; not resolved. |
| Brown, A. D. & Revelle, W. (2021). Modeling the dynamics of action. In *Measuring and Modeling Persons and Situations*, Academic Press, 355-388. doi:10.1016/B978-0-12-819200-9.00012-0 | Crossref resolves (authors Brown, Revelle; title, pages). Not read. First initials of Brown not checked. |
| Antill, J. K. (1974). The validity and predictive power of introversion-extraversion for quantitative aspects of conversational patterns. *Dissertation Abstracts International* 35(1-B). | Cited in both Revelle papers. A dissertation abstract; **not found, not read**. |

---

## 1. The Atkinson & Birch model as implemented by people who read the book

### 1.1 Vocabulary `[read: Revelle 2008, Table 1; Blankenship et al. 1995; Slade & Rush 1991]`

| Symbol | Name | Role |
|---|---|---|
| F | instigating force | rate at which the stimulus situation raises an action tendency |
| T | action tendency | inertial state, "a wish persists until satisfied and does not increase unless instigated" |
| c | consummatory value | how fast doing the activity satisfies it (doughnut > celery) |
| C | consummatory force | the outflow actually applied, only while the activity is going |
| I | inhibitory force | rate at which the situation raises the negaction tendency |
| N | negaction tendency | the "tendency not to"; "opposes, resists, and dampens the effect of an action tendency" (A&B 1970 p. 204, quoted by Slade & Rush) |
| r | resistance value | cost of resisting that activity |
| R | force of resistance | outflow of N: R = r·N in Revelle (Eq. 5); R = r·min(T, N) in Blankenship et al., citing A&B 1970 p. 239 (see 1.3) |
| T_r (BAR-T) | resultant action tendency | T minus N, the quantity that is compared between activities |

Two further concepts appear in Blankenship et al. and not in Revelle: **selective attention** (a number in (0,1) scaling the instigating and inhibitory forces of a non-focal stimulus, "the full (100%) instigating and inhibitory forces of the doughnut are not applied") and **displacement** and **substitution**, which are family relations among activities. Displacement: a stimulus instigating one activity also feeds the instigating force of an associated one (doughnut feeds drinking milk; their example adds 0.2 × the doughnut's force of 2.0 to the milk's 1.0, with selective attention 0.6 scaling whichever terms come from non-focal stimuli: milk dominant gives 1.0 + 0.6·0.2·2.0; doughnut dominant gives 0.6·1.0 + 0.2·2.0; article dominant gives 0.6·1.0 + 0.6·0.2·2.0. The displaced term is present in every state, not only when the doughnut is not dominant). Substitution: consummatory force is shared among related activities (eating the doughnut also satisfies the tendency to eat a sticky bun). Both are lifted by the full model into a coupling between activities, which Revelle's CTA writes as off-diagonal entries of matrices.

### 1.2 Equations `[read]`

Per activity i (Revelle 2008 Eqs. 1-6; Blankenship et al. 1995 for the resultant, discrete form and C):

- Action tendency: dT_i/dt = F_i − C_i, where C_i = c_i·T_i **if activity i is ongoing** and C_i = 0 otherwise. So dT_i/dt = F_i − c_i·T_i if ongoing; dT_i/dt = F_i if not (Revelle Eq. 3).
- Negaction: dN_i/dt = I_i − R_i = I_i − r_i·N_i, **always, whether or not the activity is ongoing** (Revelle Eq. 5: "it requires effort to resist even if not doing a task"). Blankenship et al. agree it acts "at all times, not just when the activity is dominant" but program R = r·**min**(T, N), citing A&B 1970 p. 239; Slade & Rush say N "is reduced whenever the action tendency is resisted" `[read]`.
- Resultant: T_r,i = T_i − N_i.
- Selection: "Atkinson & Birch (1970) assumed that action choice between competing action tendencies simply followed the maximum action tendency" (Revelle). In Blankenship's STELLA implementation: dominance = argmax over activities of BAR-T, ties broken by listed order (`if BART1 >= BART2 and BART1 >= BART3 then 1 else if ...`), and "in the simplest case, an activity is ongoing when it is dominant". That is the switching rule: **the activity with the largest resultant tendency is the one performed, and only that one has its consummatory force switched on.**
- Discrete time as implemented: ΔT = F − C and ΔN = I − R per time unit (Blankenship et al.); a FORTRAN version existed from 1973 (Seltzer; Seltzer & Sawusch 1974; Bongort 1975; D. Atkinson 1986 in BASIC).
- Lags `[read, Blankenship et al.]`: the full consummatory force is not applied until the activity has been dominant for an **initiation lag** (10 time units in their example; the PASE page, not read in full, says 2-5), and continues for a **cessation lag** after the activity stops being dominant. Their stated purpose is to separate the two tendencies "just coming on and just going off, and avoid quick reversals … behavioral chatter". Revelle says the same of the lags.

### 1.3 A discrepancy between two second-hand sources

Revelle's Eq. 2 is C = c·T (consummatory force proportional to the **action tendency**). Blankenship et al. write "the rate at which one is eating (BAR-T) determines the satisfaction of the hunger: **C = c·BAR-T**" (printed "C = c- BAR-T"; the hyphen is a mangled multiplication sign in the PDF). One of them differs from the 1970 book, or the book itself is loose. With C = c·T the ongoing asymptote is T∞ = F/c (Revelle Eq. 4) and the resultant at that point is F/c − N∞ = F/c − I/r. With C = c·(T − N) we get dT/dt = F − c(T − N), so T → F/c + N and the **resultant** T − N → F/c, independent of N; in that reading inhibition leaves the ongoing activity's resultant untouched at its asymptote, while in Revelle's reading N lowers it. `[derived]` The two readings predict different things about persistence of a fear-laden activity once begun. **Unresolved without the book** (see Unconfirmed). It matters for the algebra: it decides whether inhibition acts on the sign of the state or on its rate of discharge.

A second discrepancy, found in validation `[read]`: Revelle's Eq. 5 has R = r·N, while Blankenship et al. program the force of resistance as `0.1*Min(Action_Tendency_1, Negaction_Tendency_1)` and say so with a page reference: "multiplied by whichever is smaller, the action tendency or the negaction tendency (see J. W. Atkinson & Birch, 1970, p. 239)". Since that one carries a page citation to the book, it is the better-attested form; with it, N cannot discharge faster than r·T, so an inhibition with no action tendency to resist builds N almost linearly at rate I until T catches up. Revelle's R = r·N is the simplification.

---

## 2. What the model predicts, derived from the equations

All `[derived]` unless a source is named. These are the closed-form consequences; none of them is a quoted theorem from A&B.

Let activity i have F_i, c_i, I_i, r_i, state (T_i, N_i). Write the half-lives of the exponentials as 1/c_i and 1/r_i.

1. **Trajectories.** Ongoing: T(t) = F/c + (T0 − F/c)·e^{−ct}. Not ongoing: T(t) = T0 + F·t, linear and unbounded. N(t) = I/r + (N0 − I/r)·e^{−rt} always. Revelle gives only the asymptotes, T∞ = F/c and N∞ = I/r.
2. **Inhibition delays but cannot prevent** `[read as a claim: Revelle 2008 (Fig. 5 heading "Inhibitory cues delay but do not stop activity", shown for CTA in simulation) and Slade & Rush 1991, whose own sentence, citing "cf." A&B 1970 pp. 232-233 and 1974 pp. 297-301, is "An inhibitory force, no matter how strong, cannot permanently suppress an activity with an instigating stimulus." It is Slade & Rush's paraphrase, not a quotation of A&B]`. Derived proof (under Revelle's R = r·N): N is bounded by max(N0, I/r) whereas an idle T grows without bound at rate F, so T − N exceeds any fixed baseline b after t ≤ (b − T0 + max(N0, I/r))/F. The onset-latency bound is linear in the negaction ceiling I/r and inversely proportional to F. This is the one theorem-shaped result of the model, and it is the answer to why fear of failure shows as delay (latency) rather than as abstention. Under Blankenship's R = r·min(T, N) the conclusion survives but the bound does not: while T < N, d(T − N)/dt = F − I + r·T, which turns positive once T > (I − F)/r, reached in finite time since idle T grows at rate F; after T > N, N relaxes to I/r as before. `[derived]`
3. **No activity is absorbing.** If at least two activities have F > 0, the ongoing one has T bounded by max(T0, F/c) while each idle one has T − N → ∞; so every idle activity eventually overtakes. The model therefore **cannot** rest in one activity: behaviour is a perpetual stream, which is what Atkinson & Birch meant by "stream of behaviour" (Blankenship et al.). Sequence is generated with a constant environment: "change of behavior even in a constant environment" (Revelle `[read]`).
4. **Chatter condition.** At a switch from i to j the resultants are equal, T_r,i = T_r,j. Immediately after, j's resultant has slope F_j − c_j·T_j − (I_j − r_j·N_j) and i's has slope F_i − (I_i − r_i·N_i). A reversal at once happens iff j's slope is smaller. Since c_j·T_j is positive and large at a switch (T_j has been growing from idle), j's slope is typically the smaller whenever c_j·T_j > F_j − F_i + (the N terms). So reversal is the generic case unless consummation is delayed: this is the algebraic content of "chatter" and of the reason lags were added. `[derived]`; matches the verbal account in Revelle and Blankenship et al.
5. **The static model is a limit.** Setting F = Ps(1−Ps)·N_ach and I = Ps(1−Ps)·N_af (Revelle Eqs. 7-8 `[read]`) makes the asymptotic resultant (N_ach/c − N_af/r)·Ps(1−Ps) when the ongoing/resistance values are equal for the two sides; Atkinson 1957's T_r = (N_ach − N_af)·Ps(1−Ps) is recovered only if c = r = 1 or the same scale is imposed. **The dynamic form removes the old requirement that approach and avoidance motives sit on one ratio scale** (Revelle citing Kuhl & Blankenship 1979, `[read]`). Nuance: the claim "decoupling" is about the forces; the comparison in T − N still subtracts the two, so the scale issue is moved to the tendencies, not removed. `[derived]`
6. **Carry-over (Revelle & Michaels 1976).** Success quenches T (consummation) but failure does not, so resultant tendency grows over successive failures, faster for harder tasks. This reconciles Atkinson's inverted-U with Locke's monotone goal-difficulty effect `[read, Revelle's handout and CTA draft; the 1976 paper itself not read]`.

---

## 3. Revelle's CTA restatement, what it changes and what it keeps

### 3.1 Equations `[read: Revelle 2008, Eqs. 10-13; Revelle & Condon 2015 draft, Eqs. 10-11 with capitalised S, C, E, I]`

dT/dt = s·C − c·A
dA/dt = e·T − i·A

with C (cues) a vector set by the environment, T (tendencies) and A (actions) dynamic vectors, and s (cue to tendency), e (tendency to action), c (action consummates tendency), i (action inhibits action) matrices. "Cues stimulate action tendencies which in turn excite actions. Actions may be mutually inhibitory and also reduce action tendencies." (Fig. 2 caption.) The **diagonal of i is the cost of doing the action**; off-diagonals are mutual incompatibility; "mutually compatible activities have inhibition strength of 0" (2015 draft, Fig. 2 caption). Learning of s and e by reinforcement is sketched in 2015 and in `psych::cta`, flagged "under development".

Revelle prints T∞ = s·C·i/c (Eq. 12) and A∞ = e·C/c (Eq. 13). **Both are wrong as printed** (confirmed by 16 and re-derived here): setting both derivatives to zero in the scalar case gives A∞ = s·C/c and T∞ = i·s·C/(e·c). `[derived]` and `[simulated]`: replicating the R update with step 0.05, s = e = 0.05, c = 0.03, i = 0.1 and C = 3 gives A → 100.0 = C/c exactly. The printed forms coincide with the correct ones only if s = e = 1 and for A∞ the s/e swap vanishes. Consequence: the asymptotic action level is **independent of e and i** (the inhibition parameter and the excitation matter only for the transient and for T∞).

The scalar linear system has characteristic polynomial λ² + i·λ + e·c = 0, so it is a damped oscillator when i² < 4ec. `[derived]` This explains the figures' damped waves (Figs. 1, 3) and the "saw-tooth" tendencies under competition.

### 3.2 What actually changed from A&B

| Feature | Atkinson & Birch 1970 `[read second-hand]` | Revelle CTA `[read]` |
|---|---|---|
| State | tendency T and negaction N per activity | tendency T and **action A** per activity; no N |
| Inertia | on T (and N) | on **both** T and A |
| Selection | external rule: argmax of T − N, only winner consummates | **emergent**: mutual inhibition through i; no max rule in the dynamics |
| Chatter | cured by explicit initiation and cessation lags | cured by A's own inertia (action must build) |
| Negative drive | explicit N with its own forces I, R | "inhibitory cue" gives a negative tendency (2008 Fig. 5) or an inhibitory entry in i |
| Coupling between activities | displacement, substitution (added by hand) | any off-diagonal entry of s, e, c, i |
| Single-agent / multi-agent | single person | vector may stack several people; used for four-person talking |

**Is CTA a restatement or a different theory?** It is a different, more tractable theory that reproduces the qualitative signature (parallel tendencies, serial actions, latency and persistence functions of cue strength). It is not an equivalent: (a) negaction as a separate state disappears, so "delay but not prevent" is no longer a theorem of the structure but a property of how an inhibitory *cue* is injected (Revelle's Fig. 5 shows it empirically in simulation only); (b) A is clipped at zero in the code and T is not (T goes negative, plotted down to about −100), so T is a signed quantity unlike A&B's non-negative T; (c) the winner is not an unambiguous 0/1: all A_i are simultaneously non-negative, and the "action" reported is `which.max(act)` in the code, which is **the max rule again, applied to the output** rather than the dynamics `[read, appendix code]`. The claim that CTA has "no decision mechanism" is true of the dynamics and false of the reported behaviour.

### 3.3 Implementation details found in the code `[read, appendix of the 2008 draft]`

- Euler with step 0.05; both tendency and action updates are scaled by `step`, and the action update uses the **already updated** T (sequential, not simultaneous). Time units are iterations, so the continuous rates are 0.05× the nominal ones.
- Default inhibition matrix: off-diagonal 1, diagonal 0.05, i.e. cross-inhibition twenty times the self-cost. Default consummation: diag(0.05). Default cues 2^(n − 1:n). Initial A = cues, initial T = 0.
- Reported statistics: counts of which action is argmax each step (time share), transitions and frequency matrices.

---

## 4. The multi-agent claim and Antill's data (answers part of D070; flag for D070)

**What 16 said.** That the four-person talking model "does not reproduce Antill's finding" and "the one test of it failed." That is the 2008 draft's sentence `[read]`: "Simple variations of group size keeping the range of cue strength constant do not reproduce this effect."

**What the 2015 paper says `[read, author draft]`.** The same model is used in the "TAI" (between-individual) section, and Table 3 reports simulated shares of talking time in four groups of four. The text now says: "when the groups differ in the range of introversion-extraversion within the group, the extraverts will tend to dominate the conversation. Data supporting this prediction were reported by Antill (1974)". So **by 2015 the author claims the model reproduces the qualitative result, with the explanatory variable changed from group size to group composition**, and Antill's group-size effect is cited as supporting. That is a retraction of the 2008 negative in the form of a changed claim; the paper does not discuss the earlier failure.

**Replication of Table 3 `[simulated]`.** I re-implemented the R code in Python and ran 10,000 steps on the table's cue strengths. Table 3 has **four** groups; the fourth, "Full range of Introversion-Extraversion" (cues 1, 2, 3, 4; published shares 0.17 0.21 0.28 0.34 `[read]`), was not replicated in this file. Time shares (fraction of steps with each person as argmax) match the published column to two decimals in the three groups run:

| Group | Cue strengths | Published time shares | Replicated |
|---|---|---|---|
| four introverts | 0.95, 1.00, 1.05, 1.10 | 0.24 0.25 0.24 0.27 | 0.24 0.25 0.24 0.27 |
| four extraverts | 3.95, 4.00, 4.05, 4.10 | 0.25 0.24 0.25 0.26 | 0.25 0.24 0.25 0.26 |
| two + two | 0.95, 1.00, 4.05, 4.10 | 0.11 0.13 0.37 0.38 | 0.11 0.13 0.37 0.38 |

The table is reproducible as printed. The replication is evidence about the *code*, not about people. Table 3 is not a test against data: the cues were chosen by the author and Antill's numbers are not given.

**What the result is made of `[derived]`.** The extraverts' advantage is a consequence of the max rule on A plus cross-inhibition twenty times self-cost: a 4:1 ratio of cue strengths produces roughly a 3:1 ratio of time. In all-introvert and all-extravert groups, the shares are equal because only the ratio of cues matters (A∞ = C/c per person, and scaling all cues by 4 changes intensity, 80 to 320 in the table, but not shares). So the model predicts **share depends on relative cue strength, intensity on absolute**. That is a clean, falsifiable prediction, and it is not the group-size prediction.

**Group size (exploratory, `[simulated]`, one run per size, no noise, not a result).** One extravert (cue 4.0) with N−1 introverts (1.0-1.25): extraverts' share 0.92, 0.83, 0.48, 0.41, 0.33 for N = 2, 3, 4, 6, 8, against 1/N = 0.5, 0.33, 0.25, 0.17, 0.125. As a multiple of fair share, the extravert is at 1.8, 2.5, 1.9, 2.5, 2.6 times; introverts' mean share as a multiple of fair share is 0.17, 0.25, 0.70, 0.70, 0.77. With balanced mixes of 2k people the extravert multiple is about 1.5-1.7 at every size and the introvert multiple about 0.3-0.5 with no clear trend. So **Antill's pattern (extraverts' relative time rises with size, introverts' falls) is not clearly reproduced or contradicted by the quick scan; the model has an extravert premium at every size**, and a size trend would need deterministic argmax chatter averaged out. Treat as a lead for D069/D070, not an answer.

**Empirical standing of the whole multi-agent use.** One qualitative citation of an unread dissertation abstract; no data fit; no test with interacting people published since, in anything found. "Has CTA been tested on interacting people since?" **Not found** (see Unconfirmed). Sorrentino's uncertainty-orientation line (Sorrentino 1993, Sorrentino et al. 2003, named in the 2015 draft as a modification of DOA "applied to a variety of social contexts") is the only social application of the dynamic form named in the sources; it was not read.

---

## 5. Empirical standing of the dynamics of action itself (blunt)

- **Revelle, 2015 `[read]`**: "few researchers were interested in testing the implications of computer simulations with studies of human behavior. An important exception was Blankenship (1987)". That is the author most invested in the model saying it has been barely tested.
- **Blankenship (1987)** `[read second-hand, Blankenship et al. 1995]`: high fear-of-failure subjects took longer to go to an achievement task after an anxiety manipulation (apparent computer breakdown) than low fear-of-failure subjects. Supports "inhibition delays" (latency). Single study.
- **Kuhl & Blankenship (1979a, b)** `[read second-hand: Slade & Rush; Blankenship et al.]`: both motive groups shifted toward harder tasks over trials, high-achievement subjects faster. Predicted by dynamic theory; the static model predicts no shift. Houtmans (1989) and Slade & Rush (1991) replicate the phenomenon, per Blankenship et al.; Slade & Rush's own results not read.
- **Blankenship (1992)**, *Motivation and Emotion* 16, 35-63 `[read second-hand]`: persistence at easy and hard tasks; "simulations could not model all of the experimental results" but differential persistence of low-resultant-motivation subjects was supported, contrary to Atkinson 1957.
- **Simulation-as-argument** `[read second-hand, Blankenship et al.]`: Birch 1972; Birch, Atkinson & Bongort 1974; Atkinson, Bongort & Price 1977 (simulated TAT measurement: low internal consistency is expected even with correct classification); Reuman, Atkinson & Gallop 1986 (90 simulated individuals, three motives, nine behaviours; consistency of behaviour and factor-analytic structure). These are use of the model to argue about measurement, not tests of it.
- **Sorrentino's modification** `[read, 2015 draft name-check only]`.
- **No meta-analysis, no replication programme, no direct test of the stream-of-behaviour or the switching rule** in anything found. The specific quantitative objects that would test it (latencies and persistence as functions of F, c, I, r) are almost never measured; the achievement-task difficulty choices are the main data and are far from the equations. Be blunt: the model is **mostly a simulation tool plus a handful of achievement-domain latency and persistence studies in the 1980s**.
- **Revelle & Condon 2015** `[read]` stresses within-person dynamics through diary and telemetry methods "now" possible; no fit is reported.

---

## 6. Operand / operator translation for the algebra

**Operands.** For each agent a, a vector over its activities i of (T_ai, N_ai), or in CTA form (T_ai, A_ai). Forces F, I and the values c, r are not operands but *parameters carried by the situation and the activity*. A group is a stack of agents whose coupling is the matrices i, c, s, e.

**Operators, as the model supplies them.**
- *instigate(a, i, F)*: dT_i/dt += F (any cue); idle T grows linearly.
- *inhibit(a, i, I)*: dN_i/dt += I; N relaxes to I/r.
- *consume(a, i)*: only for the dominant activity: dT_i/dt −= c_i·T_i (or c_i·(T_i − N_i)).
- *select(a)*: argmax over i of T_i − N_i.
- *couple(a, i → j)*: displacement (F_j += κ·F_i when i not dominant), substitution (consumption shared).
- In CTA: *excite* e (T to A), *self-inhibit* diag(i), *cross-inhibit* off-diagonal(i), *stimulate* s.

**Interaction between people.** There is none in A&B. CTA adds it by making the talking activity of person p inhibit the talking activity of person q through an off-diagonal of i. That is a *rival* coupling (one speaker at a time). Nothing in either theory expresses a coupling in which one person's action *raises* another's tendency (contagion, attraction, rapport). In matrix terms this is a positive off-diagonal in s, e or c, which the form allows but nobody has used.

**What the algebra can take from this.** (1) The separation of F and I as two independent force types with different decay (T decays only when acted, N decays always) is a ready-made two-field structure, and is the only place in the survey where "not doing X" has a state variable with its own dynamics; (2) the "delay-not-prevent" theorem and the "no absorbing activity" corollary are real, provable results; (3) the chatter theorem shows the need to separate state from output (CTA's A); (4) the time-share = relative cues result (Table 3, replicated) is a genuine prediction for an N-person rival-inhibition system.

---

## 7. What exists vs what does not

**Exists.** A two-state-per-activity dynamical model with inertia, a global argmax switch and explicit lags (A&B 1970); a matrix reparametrisation without a decision rule (CTA); a published, reproducible simulation of four-person talk with a composition result; a small set of achievement-domain latency and persistence studies (Blankenship, Kuhl, Slade) consistent with the delay and shift predictions; a handful of simulation studies using it to argue about measurement; closed-form scalar asymptotes (correct forms derived here).

**Does not exist (in anything found).**
- A published derivation of the full multi-activity trajectory (switching times) in closed form. The activity-pair crossing time is solvable but nobody printed it; D069 should.
- A test of the four-person CTA against interaction data, or any fit of F, c, I, r to latencies.
- A positive-coupling form (one person's action raises another's tendency).
- A resolution of the C = c·T versus C = c·(T − N) discrepancy without the book.
- Replication of the "extravert premium rises with group size" with real conversations beyond a dissertation abstract.
- A population-level (many agent) analysis of the switching rule; the model is single-agent or four-agent.

---

## 8. Unconfirmed

- The 1970 book's own equations and the page-level statement of the switching rule. Everything here is from implementers. Needed: a library copy, or the 1974 Atkinson & Birch chapter.
- Which of C = c·T or C = c·(T − N) is the book's form, and whether the book's R is r·N or r·min(T, N) (section 1.3; Blankenship cites p. 239 for the latter).
- The numeric lag values in the book (10 time units is Blankenship's example; the PASE page says 2-5).
- The exact content of Antill (1974): dissertation abstract only; whether its effect is group size, composition, or both. Revelle's 2008 and 2015 characterisations differ.
- Whether Revelle's published (not draft) 2015 text keeps Table 3 and the Antill sentence.
- Whether CTA has been tested on interacting people since 2015. Brown & Revelle (2021) exists (Crossref, see section 0) but was not read; note that the `psych::cta` 2.5.6 docs page fetched in validation does **not** list it, so 16's attribution of the citation to those docs is unverified.
- Sorrentino (1993) and Sorrentino et al. (2003): named only.
- Exploratory group-size runs in section 4 are single deterministic runs; a proper sweep (with noise and tie-breaking) is not done.

---

## Validation log (2026-10-29)

Every DOI resolved at api.crossref.org; source PDFs (cta.pdf, rc.jrp14.pdf, Blankenship et al. 1995, Slade & Rush 1991) re-downloaded and grepped against each quoted sentence, equation and number. Web search budget was exhausted during this pass, so the "nothing exists" claims in section 7 were not re-tested by search.

- Atkinson & Birch 1970 (book): ? not readable; existence and Wiley imprint confirmed by every source's reference list.
- Atkinson 1957, doi:10.1037/h0043445: ✓ authorship, venue, 64(6 Pt.1), 359-372.
- Atkinson & Birch 1974 chapter: ✎ page range 271-325 and publisher (Winston, Washington DC) now confirmed from Slade & Rush's references, tag changed from `[standard account]`.
- Revelle 2008 CTA draft: ✓ Eqs. 1-13 as quoted, including the wrong printed Eqs. 12-13; Antill sentence; "constant environment"; code defaults (step .05, inhibit 1/.05, consume .05, cues 2^(n-1:n), which.max); Kuhl & Blankenship misprint (85, 239-248) confirmed in its reference list.
- Revelle & Condon 2015, doi:10.1016/j.jrp.2014.12.006: ✓ Crossref; draft quotes, Eqs. 10-11, Fig. 2 caption, Table 3 rows checked. ✎ "do not cite" is in the PDF itself, not a search snippet; ✎ Table 3 has four groups, the fourth not replicated, now said.
- Blankenship, Tumlinson & Sims 1995, doi:10.3758/BF03204740: ✓ C = c·BAR-T, lags of 10, selective attention, STELLA dominance code, empirical summaries. ✎ displacement example was misdescribed (displaced force applies in every state, scaled by 0.6 attention when non-focal); ✎ the force of resistance is r·min(T, N) citing A&B p. 239, which the file had omitted, now in 1.1, 1.2, 1.3 and the proof in 2.2.
- Slade & Rush 1991, doi:10.1037/0022-3514.60.1.165: ✓ p. 204 quotation. ✎ "no matter how strong" sentence is Slade & Rush's paraphrase with "cf." to A&B, not a quotation of A&B.
- Kuhl & Blankenship 1979, doi:10.1037/0033-295x.86.2.141: ✓.
- Revelle & Michaels 1976, doi:10.1037/0033-295x.83.5.394: ✓; the carry-over summary matches the CTA draft's account.
- Revelle 1986: ✎ DOI 10.1007/978-1-4684-6341-5_7 added; Crossref pages 107-131, Revelle prints 105-131.
- psych::cta docs: ✓ page exists, "under development" confirmed; ✎ Brown & Revelle 2021 not among its references.
- Blankenship 1987, doi:10.1037/0022-3514.53.2.361: ✓ (added).
- Blankenship 1992, doi:10.1007/BF00996486: ✓ (added).
- Sorrentino et al. 2003, doi:10.1016/S0022-2496(02)00032-9: ✓ (added); Sorrentino 1993: ? reference-list only.
- Brown & Revelle 2021, doi:10.1016/B978-0-12-819200-9.00012-0: ✓ exists; content ? unread.
- Antill 1974: ? Crossref finds nothing (expected for a DAI abstract); reference string confirmed in both Revelle papers.
- Seltzer 1973, Seltzer & Sawusch 1974, Bongort 1975, D. Atkinson 1986, Houtmans 1989, Birch 1972, Birch/Atkinson/Bongort 1974, Atkinson/Bongort/Price 1977, Reuman/Atkinson/Gallop 1986: ? named-as-cited in Blankenship et al. 1995 (confirmed there), not resolved individually.
- Derivations (corrected CTA asymptotes A∞ = sC/c, T∞ = isC/(ec); characteristic polynomial λ² + iλ + ec): ✓ re-derived. Simulations: not re-run.

**Verdict.** The file is substantially accurate and honest about what it read: every DOI resolves to the stated authors and venue, the Revelle equations, misprints and code details are quoted correctly, and the derived corrections to Revelle's Eqs. 12-13 hold. Three real errors were fixed: the force of resistance in Blankenship's implementation (and, by his page citation, likely in A&B 1970) is r·min(T, N), not r·N, which changes the latency bound though not the delay-not-prevent result; the displacement example was misdescribed; and a Slade & Rush paraphrase had been presented as a quotation of Atkinson & Birch. No fabrications found.


---

## Cross-checks (2026-10-29)

Method: grepped every other file in this directory for Atkinson, Birch, Revelle, Antill, Blankenship, Kuhl, Sorrentino, Slade, negaction and "file 46". Only file 16 (sections 5 and 6, "Atkinson & Birch: The Dynamics of Action", and its Summary, Gaps and validation log) overlaps substantially; the rest mention the model in passing. Contradictions were checked against the primary sources re-downloaded today: Revelle's cta.pdf (2008 draft), the Revelle & Condon 2015 author draft (rc.jrp14.pdf), and the psych 2.5.6 `cta` documentation page (rdocumentation.org). No other file was edited.

### Agreements

- **16 section 6, equations.** dT/dt = F - cT (ongoing) or F (not ongoing); dN/dt = I - rN; T_r = T - N; asymptotes F/c and I/r; CTA dT/dt = sC - cA, dA/dt = eT - iA. Same as 046 sections 1.2 and 3.1.
- **16 section 6, corrected CTA asymptotes.** A_inf = sC/c and T_inf = isC/(ec), with Revelle's printed Eqs. 12-13 wrong unless s = e = 1. 046 section 3.1 agrees (and adds the characteristic polynomial).
- **16 section 6, chatter and lags.** Max-selection chatters and the original needed lags. Agrees with 046 sections 1.2 and 2.4.
- **16 section 6, F = Ps(1-Ps)N_ach, I = Ps(1-Ps)N_af recovers Atkinson 1957 as the static limit.** Agrees with 046 section 2.5 (which adds the c = r = 1 proviso).
- **16 section 5, Atkinson 1957 resultant (Ms - Maf)Ps(1-Ps), DOI 10.1037/h0043445.** Matches 046 section 0 and section 2.5.
- **16 section 6, Revelle & Condon 2015, DOI 10.1016/j.jrp.2014.12.006, J. Res. Personality 56, 70-81; 34 (reference list and validation log, "corrected vol./pages").** Same citation as 046 section 0.
- **16 section 6, Revelle & Michaels 1976 used inertia to reconcile Atkinson with Locke.** Agrees with 046 section 2.6.
- **16 section 6, "few psychologists could handle the differential equations in the 1970s" / thin empirical standing.** Agrees with 046 section 5 (Revelle 2015: "few researchers were interested in testing...").
- **16 section 6, translation (operands: tendency vectors, possibly stacked across agents; operators instigate, consummate, inhibit).** Agrees with 046 section 6.
- **16 Gaps: "the 1970 book itself not read; equations are as Revelle restates them".** Same stance as 046 Method note and section 8.
- **15 (taxonomies, Dynamics of Action entry and caveats): books with no DOI, Atkinson & Birch 1970 not read; "explicit differential equations deciding which activity is expressed".** Agrees with 046 sections 0 and 1.2.
- **40 (switching rules include Atkinson-Birch); 34 (Revelle CTA as quantitative descendant); 48 (A&B treated in 16, not repeated); 52 (Atkinson-Birch consummation as a signed-sequence dynamic, "file 46").** Consistent with 046 sections 1.2 and 6; nothing numerical to conflict.
- **No other file cites Blankenship, Kuhl, Slade & Rush, Sorrentino or Antill.** No overlap, so no conflict for those references.

### Contradictions

1. **Brown & Revelle (2021) and the psych::cta docs.**
   - 16 section 6 (Empirical standing): Brown & Revelle 2021, "Modeling the dynamics of action", is "cited in the `psych::cta` docs".
   - 046 sections 0 and 8: the 2.5.6 docs page does not list it.
   - Primary source checked (rdocumentation.org psych 2.5.6 `cta` references, fetched today): references are A&B 1970, Revelle 1986, Revelle 2008, Revelle & Condon 2015 only. **046 is right; 16 is wrong** on the attribution. The DOI itself is fine in both.

2. **Antill (1974) and the four-person model: did it fail?**
   - 16 section 6 and Gaps item 6 ("the one test of it failed", "did not match the data"); 16 Summary and gaps.
   - 046 section 4: true of the 2008 draft only; the 2015 draft claims the model reproduces the qualitative result with the explanatory variable changed to group composition.
   - Primary sources checked: cta.pdf (lines ~530-536): "Simple variations of group size keeping the range of cue strength constant do not reproduce this effect." rc.jrp14.pdf (Table 3 passage): "the extraverts will tend to dominate the conversation. Data supporting this prediction were reported by Antill (1974)". **Both are right about their own source; 046 is right that 16's "failed" is stale and incomplete.** 16 should say the 2008 negative was group size, the 2015 positive is composition. Neither is a test against data.

3. **Consummatory force and force of resistance.**
   - 16 section 6: C = c*T and R = r*N (Revelle's forms), stated as the model.
   - 046 sections 1.3 and 1.2: Blankenship et al. (1995) give C = c*BAR-T and R = r*min(T, N) citing A&B 1970 p. 239.
   - Primary source: the 1970 book is unavailable, so which form is the book's cannot be settled. Revelle's cta.pdf has C = cT and R = rN as 16 says; Blankenship's paper (read in full in 046's validation) has the min form with a page citation. **Unresolved for the book; 16 is accurate to Revelle but omits the discrepancy, 046 is the fuller account.**

4. **"Selection is no longer a max rule" (16 section 6) versus 046 section 3.2(c).**
   - 16: selection emerges from mutual inhibition. 046: true of the dynamics, but the reported action is `which.max(act)`.
   - Primary source: cta.pdf appendix code contains `old.act <- which.max(act)` and `which.act <- which.max(act)` (lines ~773, 787). **046 is right; 16 is right about the dynamics only.** Not a factual clash, a scope difference.

5. **Revelle's reference to Kuhl & Blankenship (1979).** 46 notes the draft prints Psych. Rev. 85, 239-248 against Crossref 86(2), 141-151. No other file cites it, so no conflict; recorded so 16 and 34 are not later seeded with the misprint.

No file contradicts 046 on any equation, number or DOI. All real clashes are in 16 section 6 (items 1, 2, 4) and are staleness or scope, already flagged inside 046; 16 itself was not edited, per the task.

## Licences of quoted and transcribed material (2026-10-30)

Audit result: every flagged item had verdict "check", so no text was changed. Each source is listed with the licence as determined and how this file uses it.

| Source | Licence as determined | Use in this file |
|---|---|---|
| Revelle (2008), "Cues, Tendencies and Actions", working draft 10/10/08 (cta.pdf, with R code) | Not determined; publisher copyright presumed (unpublished author draft, no licence recorded) | Short quotations (8 to 19 words each: Table 1 row T, Eq. 5 negaction text, selection sentence, Fig. 2 and Fig. 5 captions, the "What 16 said" passage, repeated in Cross-checks); restated equations; the section 1.1 vocabulary table is a description of Table 1's role column, not a copy. Keep only once a licence is recorded, or reduce to paraphrase. |
| Revelle & Condon (2015), author draft of "A model for personality at three levels", J. Research in Personality 56 | Not determined; publisher copyright presumed (draft header reads "Please do not cite without ..."; published version not checked) | Short quotations (8 to 29 words: Fig. 2 caption, Table 3 passage, section 5 first bullet, repeated in Cross-checks). Check the published version's wording or licence, or paraphrase, before open-sourcing. |
| Blankenship, Tumlinson & Sims (1995), Behav. Res. Methods, Instruments, & Computers 27(2) | Not determined; publisher copyright presumed (Springer) | Read in full; restated equations and values only. Access route to the Springer PDF not recorded: confirm it was legitimate. |
| Slade & Rush (1991), J. Personality and Social Psychology 60(1) | Not determined; publisher copyright presumed (APA); the copy read came from an unofficial third-party host | Introduction read; claims reported in our own words. Confirm the copy was legitimately obtained; keep the text out of the repo. |
| Blankenship (1992); Kuhl & Blankenship (1979); Revelle & Michaels (1976); Revelle (1986) | Not determined; publisher copyright presumed | Dataset-style citation only (title, venue, pages, DOI); not read or not reproduced. |
| Atkinson (1957); Antill (1974) abstract; Atkinson & Birch (1970, 1974) | Not determined; publisher copyright presumed | Citation and restated equations only. The 1970 book was not read; the A&B 1970 characterisation is second-hand via Revelle. |
| psych::cta documentation (R, rdocumentation.org) | Not determined; package documentation (psych is GPL-licensed software, documentation licence not checked) | Short title phrase and reference-list facts only. |

Open items before open-sourcing: record or confirm the Revelle draft licences, check the published 2015 version, and confirm legitimate access to the Springer and Slade & Rush copies (readable copy provenance; re-read needed if not).
