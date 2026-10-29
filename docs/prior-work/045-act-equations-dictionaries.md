# Prior work 045: Affect Control Theory, equations, dictionaries and predictive standing

Direction: D042

Date: 2026-10-29. Kind: data (with a cross-check of file 03's ACT section). Cross-references: 03 (ACT summary), 32 (Osgood semantic differential), 16, 19.

**Method and honesty note.** Opened and read at source this session: (a) the Interact guide (Heise, PDF mirrored at cs.uwaterloo.ca, about 3,270 lines of extracted text, read where it concerns deflection, cultures, equation families, history, terms of use); (b) Hoey, Schröder & Alhothali, arXiv 1306.5279 (the BayesACT paper, text extracted, equations 1, 3-8, 13, 17-18 and appendix B read); (c) Troyer 2004 AAAI symposium paper (full, 2 pages, which prints one impression-formation equation); (d) the affectcontroltheory.org dictionary index and two dictionary pages (Indiana 2003, West Germany 1989); (e) the first page of the authors' ASR appendix. Not read: Heise 2007 *Expressive Order* itself (Springer, paywalled; Part II holds the derivations), Heise 2010 *Surveying Cultures*, Smith-Lovin 1987, Heise 2013 SPQ, Schröder & Scholl 2009, Schröder et al. 2013, the ASR 2016 main text. Wikipedia and affectcontroltheory.org's theory page give no equations. Tags: [read] = seen in a source opened this session (including a secondary source that prints the equation, named); [from abstract/standard account] otherwise. DOIs below were each returned by Crossref bibliographic search this session.

**Summary.** ACT has three parts: (1) a measurement structure, EPA profiles (Evaluation, Potency, Activity) of concepts rated on a semantic differential, giving "fundamental sentiments" **f**; (2) event-reaction equations, a fixed polynomial regression map from a 29-term feature vector of the previous transient impressions and the new behaviour to the new 9-vector of transient impressions **tau** for actor, behaviour, object; (3) the control principle, that actors choose behaviour and labels to minimise **deflection**, the squared distance between **f** and **tau**. The behaviour that minimises deflection has a closed form (a linear solve) because the impression equations are linear in the behaviour's own EPA (see §3). Dictionaries exist for at least eight countries and about 18 datasets. Predictive evidence is mostly experiments and simulation by the theory's own community; I found no independent meta-analysis, and the quantitative predictive standing (how often the minimum-deflection behaviour is the one people choose) is not reported in anything I read.

---

## 1. Core definitions

**Their vocabulary.** Fundamental sentiment (culturally shared EPA meaning of a concept); transient impression (the momentary EPA meaning of an element after an event); deflection; affect control principle; reidentification (relabelling an actor to reduce deflection); attribution; emotion as the difference between transient and fundamental self-identity; actor-behaviour-object (ABO) event, extended with setting and modifier (ABOS); interactant; tension; repository/dictionary; actualisation.

**Drives/operands.** None in the drive sense. Operands are concepts (identities, behaviours, modifiers, settings) each a point in R^3 (EPA). The only "motive" is consistency: minimise deflection. Hoey et al. place ACT among psychological consistency theories [read, arXiv 1306.5279 §2.1].

**EPA scales.** The Interact-era convention is a range of -4.3 to +4.3 [read, Hoey et al. §2.1]; Troyer gives -4.5 to +4.5 [read, Troyer 2004]. The discrepancy is a convention difference between sources; the Interact guide gives example profiles such as Japanese *child* -0.24, -2.10, 2.75 (males) [read, guide]. Hoey et al. example: professor [1.7, 1.8, 0.5], student [1.8, 0.7, 1.2] [read].

## 2. Impression-formation equations

**Citation.** Smith-Lovin, L. (1987). Impressions from events. *Journal of Mathematical Sociology* 13(1-2), 35-70. doi:10.1080/0022250x.1987.9990026 (Crossref confirms title, year, journal). Same issue: Heise, D. R. (1987). Affect control theory: Concepts and model. *J. Math. Sociol.* 13, 1-33. doi:10.1080/0022250x.1987.9990025. Smith-Lovin (1987b), The affective control of events within settings, doi:10.1080/0022250x.1987.9990027. Averett & Heise (1987) doi:10.1080/0022250x.1987.9990028 (modifiers/emotions). Heise & Smith-Lovin (1981), Impressions of goodness, powerfulness, and liveliness from discerned social events, *Social Psychology Quarterly*, doi:10.2307/3033705.

**General form.** tau' = M(x) G(f', tau, x) where G is a vector of monomials in the previous transients tau and the new behaviour fundamental f_b', M is a 9 x 29 matrix of regression coefficients (rows = E, P, A of actor, behaviour, object), and x says whose turn it is (actor/object rows are swapped on the other party's turn) [read, Hoey et al. §3.1.1].

**Exact feature vector for the agent's turn, as printed by Hoey et al. eq. (3)** [read; subscripts: a actor, b behaviour, c object/client; e, p, a = E, P, A; "tau_ae" = transient evaluation of the actor; "f_be" = fundamental evaluation of the behaviour]. G has 29 entries in this order: 1, tau_ae, tau_ap, tau_aa, f_be, f_bp, f_ba, tau_ce, tau_cp, tau_ca, then the two-way products tau_ae f_be, tau_ae f_bp, tau_ae tau_ce, tau_ae tau_cp, tau_ap f_be, tau_ap f_bp, tau_ap tau_cp, tau_ap tau_ca, tau_aa f_ba, tau_ce f_be, tau_cp f_be, tau_ce f_bp, tau_cp f_bp, tau_ca f_bp, tau_cp f_ba, and the three-way products tau_ae tau_ce f_be, tau_ae tau_cp f_bp, tau_ap tau_cp f_bp, tau_ap tau_ca f_bp. (My reading of the PDF text extraction; the extraction mangled the layout, so exact ordering of a few middle terms should be re-checked against the paper before coding. The count of 29 and the use of monomials up to degree 3 are stated explicitly [read].)

**Troyer's printed example, the equation for the transient evaluation of the actor** [read, Troyer 2004, attributed there to Smith-Lovin 1987]:

    A_e' = c1 A_e + c2 A_p + c3 A_a + c4 B_e + c5 B_p + c6 B_a + c7 O_e + c8 O_p + c9 O_a
         + c10 A_a B_e + c11 B_a O_e + c12 A_p B_p + c13 B_p O_p + c14 A_a B_a + c15 A_e B_p
         + c16 A_e B_a + c17 A_p B_e + c18 A_p O_a + c19 B_e O_p + c20 B_p O_e + c21 B_p O_a
         + c22 B_a O_e + c23 B_a O_p + c24 A_e B_e O_e + c25 A_p B_p O_p + c26 A_a B_a O_a
         + c27 A_e B_p O_p + c28 A_p B_p O_a + e

(28 coefficients c1..c28 plus error e; the Troyer paper does not print the coefficient values, and I did not find them in any source opened. They live in Heise 2007 Part II / Interact's "View equations" screen, per the guide.) Note the guide and Hoey differ in notation (Troyer's A, B, O are the *fundamental* ratings in the regression; Hoey's G uses previous transients tau for actor and object and f for behaviour). Both describe the same regression structure: Troyer is reproducing the general shape.

**Structure of the map.** Linear terms plus products of up to three elements; mostly cross-element products (actor x behaviour, behaviour x object, three-way). Within the behaviour component the map is linear in f_b' once tau and x are fixed, so tau' = H(tau,x) f_b' - C(tau,x) with H a 9 x 3 and C a 9 x 1 matrix [read, Hoey et al. §3.1.1 eq. after (4)].

**Equation families.** Interact carries separate coefficient sets for: U.S.A. 1978, Japan 1984, Canada 1985, China 2000 (listed in the menu), Germany 2007; and notes US 1970s equations are used for Irish and Chinese analyses, Canadian 1990s equations for Canada, Japanese 1990s for Japan, German 2007 for Germany; male and female equation sets exist [read, guide, "Changing Cultures" and "Impression-formation Equations"]. The guide states the ABO equations "were obtained in two phases" and that ABOS equations came from stepwise regression, and that methodological differences may produce differences in results [read, guide footnote 5]. Nuance: the guide's menu list (1978, 1984, 1985, 2000, 2007) and the running-text list (1990s Canada and Japan) disagree on dates inside the same document. I have not resolved which is right.

**Modifier and emotion equations.** Emotions are a function of the transient impression of self and its difference from the fundamental identity sentiment; separate empirically derived equations (Heise 2007 ch. 14, Averett & Heise 1987, Heise & Thomas 1989, Smith-Lovin; Schröder 2011) [read, via Hoey et al. §3.2 and Wikipedia]. Coefficients not seen.

## 3. Deflection and the control principle

**Exact definition** [read, Hoey et al. eq. (1)]:

    D = sum_i w_i (f_i - tau_i)^2

summed over the nine fundamental/transient components (E, P, A of actor, behaviour, object), w_i typically 1.0. Troyer says the same ("sum of the squared differences between fundamental sentiments of the ABO elements and transient impressions"), and attributes to Heise & MacKinnon (1987) the claim that deflection corresponds to perceived *likelihood* of an event [read, secondary]. Heise & MacKinnon (1987) Affective bases of likelihood judgments, *J. Math. Sociol.* 13, 133-151 (reprinted doi:10.4324/9781315025773-5; Crossref).

**Affect control principle** [read, Hoey et al. Definition 1]: actors work to experience transient impressions consistent with their fundamental sentiments. Interact's rules of thumb for who acts next: the person whose optimal action yields the lowest deflection (the guide reports an example of 0.87, 1.19, 1.27) [read, guide].

**Deflection decomposition** [read, guide]: Interact reports total deflection and the parts from stressing the actor's identity and the object's identity; the remainder comes from behaviour and setting. Interact also bins deflection into four quarters on a graph (comfortable/normal, unusual, weird, and "invalidates the impression"); the guide's worked event has deflection 4.3 in the lowest sector; so the scale is unbounded sum of squares, not 0-1.

**Optimal behaviour (closed form).** Because tau' is linear in f_b' (above), minimising D over f_b' is a quadratic minimisation, a linear solve. Hoey et al. derive it in their appendix B and state the result matches **Heise (2007) eq. (12.21)** exactly: f_b* = -(S_beta^T I_beta [I; -M] ... )^{-1} ... with H_a, H_b, H_c, C_a, C_b, C_c from the 9 x 3 and 9 x 1 refactoring (their eq. 48-49) [read, but the formula is a long matrix expression I do not transcribe because the PDF extraction scrambled the block structure]. Equations (13.11) and (13.18) of Heise 2007 give the corresponding closed forms for the optimal actor and object identities [read, via Hoey et al.]. Practical consequence: Interact finds the *dictionary* behaviour nearest to the continuous optimum, so predictions are restricted to the finite set of rated words. Hoey et al. warn of constraints in the action space ("you can't give a student a really hard problem to solve in a way that will seem accommodating/submissive") [read].

**Reidentification and attribution.** When deflection is too high to be resolved by behaviour, actors relabel the other (e.g. "grouch", "delinquent" in Troyer's two simulations: deflections 2.0, 5.0, 7.0, then 12.0 or 14.0, with relabel and response "scold" or "avoid") [read, Troyer 2004 Table 2].

**Algebraic reading.** What exists: a state space R^9 (or R^3 per concept), a fixed nonlinear map per event type, a quadratic potential, and a closed-form arg-min. Not present: any composition law between acts (two events in a row are handled by iterating the map, with the previous transients as state, not by an algebraic composition), and no statement that the family of event maps is closed under anything. The map is a 3-degree polynomial in the transient state; it is not linear in state, so it does not give a matrix group.

## 4. BayesACT (Hoey, Schröder & Alhothali)

**Citations.** Hoey, J., Schröder, T., & Alhothali, A. (2013). Bayesian Affect Control Theory. *ACII 2013*, 166-172. doi:10.1109/acii.2013.34 (Crossref confirms; as in file 03). Hoey, J., Schröder, T., & Alhothali, A. (2016). Affect control processes: Intelligent affective interaction using a partially observable Markov decision process. *Artificial Intelligence* 230, 134-172. doi:10.1016/j.artint.2015.09.004 (Crossref confirms). Preprint arXiv:1306.5279 (this is the text read). Schröder, T., Hoey, J., & Rogers, K. B. (2016). Modeling dynamic identities and uncertainty in social interactions: Bayesian affect control theory. *American Sociological Review*, doi:10.1177/0003122416650963; appendix at cs.uwaterloo.ca/~jhoey/papers/ASRAppendix.pdf (read: page 1 only plus parameter table).

**Their vocabulary.** Fundamental dynamics, transient dynamics, deflection potential, identity inertia, belief state over sentiments, client/agent, POMCP-C.

**Model as stated** [read, arXiv 1306.5279 §3]:
- Transient dynamics, deterministic: Pr(tau' | tau, f', x) = delta(tau' - H(tau,x) f_b' - C(tau,x)) (eq. 5).
- Deflection potential: phi(f', tau') proportional to exp(-(f'-tau')^T Sigma^{-1} (f'-tau')) (eq. 7); if Sigma is diagonal with elements 1/w_i, then log phi = D + const where D is eq. (1).
- Fundamental dynamics: Pr(f' | f, tau, x, b_a, phi) proportional to exp(-psi(f',tau,x) - xi(f',f,b_a,x)) (eq. 8), psi = (f' - M G)^T Sigma^{-1} (f' - M G) (eq. 18), and xi an "inertia" term keeping f' near f for identities and equal to the agent's chosen behaviour b_a on the agent's turn.
- Expected deflection under belief b(s): E_b[D] = integral b(s) D(s) ds (eq. 13); states of "Joy" and other emotions would be functions of (f, tau).
- Planning: a POMDP with reward on top of the potential; sequential Monte Carlo for the belief; POMCP-C (continuous Monte-Carlo planner) in the UAI 2015 follow-up (title from a search result, not opened).
- Appendix simulation parameters for Simulation 1: alpha = 0.1 (std. dev. of a diagonal Sigma), identity inertia beta_a = beta_c = 0.001, initial identity std. dev. 2.0 (agent) and 0.01 (client) [read, ASR appendix].

**Theorems or derived predictions.** The paper re-derives Heise's closed-form optimal behaviour (eq. 12.21) as a limit of its Gaussian treatment (appendix B). No new theorem about long-run behaviour.

**Empirical standing** (blunt). Simulations show BayesACT agents recover identities with low identity-deflection over sample counts, tolerate noise, and track a shifting client (Appendix C tables) [read, text]. Human evidence is a pilot: a 37-participant survey to build a tutoring system's EPA mappings and a 20-participant (7 female) study of the "MathTutor", with one-tailed t-tests (df = 18, p < .05 to < .01) comparing BayesAct to a baseline on items like "dialogue was simple and natural" [read, Table 2]. Hoey et al. themselves say to treat this small-sample result with caution [read]. The ASR paper's evidence is simulation. I did not find evidence that the BayesACT *behaviour* predictions have been tested against naturally occurring interaction data.

## 5. EPA dictionaries (what exists, sizes, access)

**Hub.** affectcontroltheory.org/resources-for-researchers/data-sets-for-simulation/ lists 18 datasets "intended for simulation in Interact" [read]. Interact itself has been described as spanning "six nations and a quarter of a century" and "eleven cultural repositories", of which six lack setting sentiments, and all but Ireland have at least emotion modifiers [read, guide]. The guide's history says Neil MacKinnon's work produced a set of Canadian dictionaries and a cross-national replication of the equations (no date given there) [read].

| Country | Dataset | Year |
|---|---|---|
| USA | North Carolina Student Dictionary | 1978 |
| USA | Texas Student Dictionary | 1998 |
| USA | Indiana Dictionary | 2003 |
| USA | Online, Georgia Student, Student Surveyor, Combined Surveyor dictionaries | 2015 |
| USA | OCCS Dictionary | 2020 |
| USA | Kelly Situational Dictionary | 2021 |
| Canada | Ontario Student Dictionary | 1980-1986; 2001-2003 |
| China | Mainland Students Dictionary | 1999 |
| Egypt | Cairo Dictionary | 2012-2014 |
| Germany | West Students Dictionary | 1989 |
| Japan | Japan Dictionary | 1989-2002 |
| Morocco | Morocco Dictionary | 2015 |
| Northern Ireland | Belfast Student Dictionary | 1977 |
| France/Germany | Gendered Social Identities | 2023 |

(Table from the hub page [read]; the 2020s items are as listed there; I did not open them. The guide mentions a separate 2007 German dictionary by Schröder, "Germany 2007", not on the hub list as such. Possibly the 2007 data is the source of the equations and the dictionary shown above is the 1989 one. Unresolved.)

**Details for the two pages opened** [read]:
- **USA Indiana 2003** (Francis & Heise, "Mean Affective Ratings of 1,500 Concepts by Indiana University Undergraduates in 2002-3"): 1,027 respondents (US-resident at 16, roughly gender-balanced), 1,500 concepts = 500 identities, 500 behaviours, 300 modifiers, 200 settings; collected online with the Surveyor applet; licence not stated on the page.
- **West Germany 1989** (Schneider, "Mean Affective Ratings of 804 Concepts by West German Students in 1989"): N = 520 (mostly Mannheim; 12th-13th-grade pupils and university students), 442 identities, 295 behaviours, 67 modifiers; concepts chosen for back-translatability with the 1978 US dictionary.

**Format and access.** Described as "[Computer file]"; downloadable through Interact or from Aidan Comb's *actdata* repository (named on the pages; I did not locate or open it, so GitHub path unconfirmed). No file format was stated on the pages opened. Per the guide's terms of use: site materials are copyrighted by Heise/Indiana, "for noncommercial, research use only"; governmental, political or commercial use needs written permission [read]. So a public repo of these data would need permission; for private modelling noncommercial use is permitted.

**Variables.** Per concept: mean E, P, A (and in Interact, separate male/female means and standard deviations; Troyer's table shows variances per rating). Gender splits exist in the Interact data [read, guide].

**Cross-cultural contrast example** [read, guide]: Japanese *child* has E -0.24 (m) / 0.00 (f), P -2.10 / -2.00, A 2.75 / 2.80, whereas American *child* is evaluated very positively, so a "same" word differs in affect across cultures; the guide offers this as the reason to use per-culture dictionaries.

**Reliability claim** (secondary, by Hoey et al. citing Heise 2010): within-culture agreement on EPA is high across subgroups and cultural means from as few as a few dozen respondents are "extremely stable over extended periods" [read as a claim; I did not see the underlying statistics].

## 6. Empirical standing of deflection minimisation

Evidence cited by Hoey et al. [read as citations only; papers not opened]:
- Schröder & Scholl (2009), Affective dynamics of leadership: an experimental test of ACT, *Social Psychology Quarterly* 72, 180-197, doi:10.1177/019027250907200207 (Crossref). Mock leaders in a computer-simulated business game; verbal behaviours consistent with deflection minimisation per Hoey et al.
- Schröder, Netzel, Schermuly & Scholl (2013), Culture-constrained affective consistency of interpersonal behavior, *Social Psychology* 44, 47-58, doi:10.1027/1864-9335/a000101 (Crossref). Non-verbal displays in dyads.
- Heise (2013), Modeling interactions in small groups, *Social Psychology Quarterly* 76, 52-72, doi:10.1177/0190272512467654 (Crossref). Conversational turn-taking in small groups per Hoey et al.
- Heise & MacKinnon (1987) on deflection as inverse likelihood.

**Blunt assessment.** Hoey et al.'s sentence is "many experimental and observational studies have shown that deflection is indeed inversely related to the likelihood of humans to engage in the corresponding social actions" [read]; the three named studies are all by ACT authors or their collaborators. Troyer's pilot study measured only EPA ratings of computer terms and ran Interact simulations; it tested nothing against behaviour [read]. I found no pre-registered or independent test, no effect sizes, and no out-of-sample prediction accuracy figure in what I opened. Another weakness stated by the theory's own guide: the equations differ by culture and decade, and the guide notes methodological differences in how they were estimated. Treat "ACT predicts behaviour" as plausible for scripted, dictionary-describable, short event sequences and untested at scale.

## 7. Interact software

- Written by Heise; first version 1972, PL/1; Java applet since 1997; current Interact.jar; features added over time: labelling 1975, settings and modifiers 1980, attributions and emotions 1984, cross-national data 1991, facial-expression display 1996, a learning capability 2005, self-sentiment/identity-actualisation 2007 [read, guide history].
- Heise's anecdote: the first run, "Bob insults Mac; what will Mac do?", output "Mac hits Bob" and the author "didn't have much hope" it would work [read]. Anecdote, not evidence.
- Links named in sources: indiana.edu/~socpsy/ACT (original; Hoey et al. 2013), cs.uwaterloo.ca/~jhoey/research/ACTBackup (mirror), affectcontroltheory.org, bayesact.ca (the last two from Wikipedia).
- The guide's terms: noncommercial research use.

## 8. Operand/operator translation for the algebra

- **Operand:** a concept vector in R^3; a situation state is the 9-vector tau (plus, for settings/modifiers, extra components) with the fundamental vector f as reference. A drive-like quantity: *deflection D = ||f - tau||^2_W* is a scalar potential on the state; its gradient defines a pull.
- **Operator:** an event type (actor-behaviour-object) acts as a map tau -> tau' = M G(f_b', tau); the whole family is the single parametrised map given by M. Behaviour choice is an arg-min over f_b' (closed form), a **control law**, not an operator composition. Relabelling is a second operator (nearest identity to the arg-min).
- **What it gives the algebra:** the only fully worked example in the literature of an **act-to-state map with a numerical consistency potential and a closed-form controller**. If drives are scalar potentials, then deflection is a social-affective potential and "behaviour minimises deflection" is a drive-reduction law (compare Hull in file 16).
- **What it does not give:** (i) no list of drives; one drive (consistency) only; (ii) maps are not constructed to compose or invert; (iii) no groups: events are dyadic ABO, group effects are handled by multiple interactants each applying their own minimisation and the "next speaker = lowest deflection" rule of thumb; (iv) EPA is a three-dimensional descriptive space, so curiosity/fear/desire could be represented only as EPA concepts (e.g. the emotion modifiers) rather than as driving forces.

## 9. What exists vs what does not

**Exists.** A concrete polynomial event-reaction map with 28-29 coefficients per component, per culture/gender family; a quadratic deflection potential with closed-form optimal behaviour; about 18 dictionaries across at least eight countries, free for noncommercial research; a simulator; a probabilistic POMDP generalisation with code and a few small human tests; several experiments by the ACT community.

**Does not exist** (in what I found). Published, tabulated coefficients that I could read (they need Heise 2007 or Interact); independent replication or effect sizes for deflection-minimisation as a predictor of behaviour; any law of composition for acts; any treatment of groups beyond dyads plus a turn-taking heuristic; anything for asymmetric power/status beyond P in EPA; a drive vocabulary beyond consistency; validation that the EPA map's fixed coefficients survive across decades (the guide itself uses 1978-vs-2007 families).

## 10. Corrections to file 03

File 03 says the ACT equation form was "from the validator's knowledge" and not quoted. This file now supplies the printed forms: deflection D = sum w_i (f_i - tau_i)^2 [read] and the 29-term feature vector [read, with a layout caveat], plus Troyer's printed 28-coefficient equation for the actor's transient evaluation [read]. 03's reading of ACT as "a fitted polynomial map on EPA vectors, deflection minimisation with a closed-form optimum" is confirmed.

## Unconfirmed

- The coefficient values M (needs Heise 2007 Part II or Interact's "View equations").
- Exact term ordering in G for some middle terms (PDF extraction scrambled layout).
- The matrix expression for f_b* (eq. 12.21) transcribed only in outline.
- Scale range: -4.3..4.3 (Hoey) vs -4.5..4.5 (Troyer) not reconciled.
- Which year's equation set (1978/1984/1985/2000/2007 in the guide menu, versus 1990s in running text) belongs to Canada and Japan.
- Dataset sample sizes, concept counts, licence for the 16 dictionaries I did not open; location of the *actdata* repository.
- Effect sizes or accuracy figures for the leadership, non-verbal and turn-taking studies (not opened).
- The "eleven repositories" versus 18 listed datasets: the guide's older count against the hub's newer list.
- Whether Heise 2010 *Surveying Cultures* (doi:10.1002/9780470575789 per Crossref, year printed as 2009-12) is the 2010 book cited by Hoey et al.; Crossref lists the online date.
