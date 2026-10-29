# Prior work 045: Affect Control Theory, equations, dictionaries and predictive standing

Direction: D042

Date: 2026-10-29. Kind: data (with a cross-check of file 03's ACT section). Cross-references: 03 (ACT summary), 32 (Osgood semantic differential), 16, 19.

**Method and honesty note.** Opened and read at source this session: (a) the Interact guide (Heise, PDF mirrored at cs.uwaterloo.ca, about 3,270 lines of extracted text, read where it concerns deflection, cultures, equation families, history, terms of use); (b) Hoey, Schröder & Alhothali, arXiv 1306.5279 (the BayesACT paper, text extracted, equations 1, 3-8, 13, 17-18 and appendix B read); (c) Troyer 2004 AAAI symposium paper (full, 2 pages, which prints one impression-formation equation; Troyer, L. (2004). Affect Control Theory as a Foundation for Socially Intelligent Systems. AAAI Spring Symposium *Architectures for Modeling Emotion*, SS-04-02; https://cdn.aaai.org/Symposia/Spring/2004/SS-04-02/SS04-02-026.pdf. Hoey et al.'s reference list gives a slightly different title, "An affect control theory as a foundation for the design of socially intelligent systems"; the PDF title is the one above); (d) the affectcontroltheory.org dictionary index and two dictionary pages (Indiana 2003, West Germany 1989); (e) the first page of the authors' ASR appendix. Not read: Heise 2007 *Expressive Order* itself (Springer, paywalled; Part II holds the derivations), Heise 2010 *Surveying Cultures*, Smith-Lovin 1987, Heise 2013 SPQ, Schröder & Scholl 2009, Schröder et al. 2013, the ASR 2016 main text. Wikipedia and affectcontroltheory.org's theory page give no equations. Tags: [read] = seen in a source opened this session (including a secondary source that prints the equation, named); [from abstract/standard account] otherwise. DOIs below were each returned by Crossref bibliographic search this session.

**Summary.** ACT has three parts: (1) a measurement structure, EPA profiles (Evaluation, Potency, Activity) of concepts rated on a semantic differential, giving "fundamental sentiments" **f**; (2) event-reaction equations, a fixed polynomial regression map from a 29-term feature vector of the previous transient impressions and the new behaviour to the new 9-vector of transient impressions **tau** for actor, behaviour, object; (3) the control principle, that actors choose behaviour and labels to minimise **deflection**, the squared distance between **f** and **tau**. The behaviour that minimises deflection has a closed form (a linear solve) because the impression equations are linear in the behaviour's own EPA (see §3). Dictionaries exist for at least eight countries and about 18 datasets. Predictive evidence is mostly experiments and simulation by the theory's own community; I found no independent meta-analysis, and the quantitative predictive standing (how often the minimum-deflection behaviour is the one people choose) is not reported in anything I read.

---

## 1. Core definitions

**Their vocabulary.** Fundamental sentiment (culturally shared EPA meaning of a concept); transient impression (the momentary EPA meaning of an element after an event); deflection; affect control principle; reidentification (relabelling an actor to reduce deflection); attribution; emotion as the difference between transient and fundamental self-identity; actor-behaviour-object (ABO) event, extended with setting and modifier (ABOS); interactant; tension; repository/dictionary; actualisation.

**Drives/operands.** None in the drive sense. Operands are concepts (identities, behaviours, modifiers, settings) each a point in R^3 (EPA). The only "motive" is consistency: minimise deflection. Hoey et al. place ACT among psychological consistency theories [read, arXiv 1306.5279 §2.1].

**EPA scales.** The Interact-era convention is a range of -4.3 to +4.3 [read, Hoey et al. §2.1]; Troyer gives -4.5 to +4.5 [read, Troyer 2004]. The discrepancy is a convention difference between sources; the Interact guide gives example profiles such as Japanese *child* -0.24, -2.10, 2.75 (males) [read, guide]. Hoey et al. example: professor [1.7, 1.8, 0.5], student [1.8, 0.7, 1.2] [read].

## 2. Impression-formation equations

**Citation.** Smith-Lovin, L. (1987). Impressions from events. *Journal of Mathematical Sociology* 13(1-2), 35-70. doi:10.1080/0022250x.1987.9990026 (Crossref confirms title, year, journal). Same issue: Heise, D. R. (1987). Affect control theory: Concepts and model. *J. Math. Sociol.* 13, 1-33. doi:10.1080/0022250x.1987.9990025. Smith-Lovin (1987b), The affective control of events within settings, doi:10.1080/0022250x.1987.9990027. Averett, C. P. & Heise, D. R. (1987), Modified social identities: Amalgamations, attributions, and emotions, *J. Math. Sociol.* 13, 103-132, doi:10.1080/0022250x.1987.9990028. Heise & Smith-Lovin (1981), Impressions of goodness, powerfulness, and liveliness from discerned social events, *Social Psychology Quarterly* 44(2), 93-, doi:10.2307/3033705.

**General form.** tau' = M(x) G(f', tau, x) where G is a vector of monomials in the previous transients tau and the new behaviour fundamental f_b', M is a 9 x 29 matrix of regression coefficients (rows = E, P, A of actor, behaviour, object), and x says whose turn it is (actor/object rows are swapped on the other party's turn) [read, Hoey et al. §3.1.1].

**Exact feature vector for the agent's turn, as printed by Hoey et al. eq. (3), which they give as their rewriting of Heise (2007) eq. (11.16)** [read; subscripts: a actor, b behaviour, c object/client; e, p, a = E, P, A; "tau_ae" = transient evaluation of the actor; "f_be" = fundamental evaluation of the behaviour]. G has 29 entries in this order: 1, tau_ae, tau_ap, tau_aa, f_be, f_bp, f_ba, tau_ce, tau_cp, tau_ca, then the two-way products tau_ae f_be, tau_ae f_bp, tau_ae tau_ce, tau_ae tau_cp, tau_ap f_be, tau_ap f_bp, tau_ap tau_cp, tau_ap tau_ca, tau_aa f_ba, tau_ce f_be, tau_cp f_be, tau_ce f_bp, tau_cp f_bp, tau_ca f_bp, tau_cp f_ba, and the three-way products tau_ae tau_ce f_be, tau_ae tau_cp f_bp, tau_ap tau_cp f_bp, tau_ap tau_ca f_bp. (My reading of the PDF text extraction; the extraction mangled the layout, so exact ordering of a few middle terms should be re-checked against the paper before coding. The count of 29 and the use of monomials up to degree 3 are stated explicitly [read].)

**Troyer's printed example, the equation for the transient evaluation of the actor** [read, Troyer 2004, attributed there to Smith-Lovin 1987]:

    A_e' = c1 A_e + c2 A_p + c3 A_a + c4 B_e + c5 B_p + c6 B_a + c7 O_e + c8 O_p + c9 O_a
         + c10 A_a B_e + c11 B_a O_e + c12 A_p B_p + c13 B_p O_p + c14 A_a B_a + c15 A_e B_p
         + c16 A_e B_a + c17 A_p B_e + c18 A_p O_a + c19 B_e O_p + c20 B_p O_e + c21 B_p O_a
         + c22 B_a O_e + c23 B_a O_p + c24 A_e B_e O_e + c25 A_p B_p O_p + c26 A_a B_a O_a
         + c27 A_e B_p O_p + c28 A_p B_p O_a + e

(28 coefficients c1..c28 plus error e, no constant; transcription re-checked against the PDF in validation. The source itself lists B_a O_e twice, as c11 and c22, so as printed it has 27 distinct terms: a typo in Troyer, not in this file. Troyer does not print coefficient values.) **Corrected in validation:** the coefficient values *are* published and machine-readable: Interact's "View equations" screen shows them (guide, "Handling Equations"), and Aidan Combs's R package *actdata* (github.com/ahcombs/actdata, CC0 package licence) ships them as `data-raw/eqns/<set>_<kind>_<sex>.dat`, in Interact's Z-pattern format (one row per term, a 0/1 string over Ae Ap Aa Be Bp Ba Oe Op Oa, then one coefficient column per predicted component). Sets present: nc1978, japan1984, canada1985, canada20012003, china2000, germany2007, us2010, egypt2014, morocco2015, each with impressionabo, impressionabos, selfdir, traitid, emotionid, male and female. Example, us2010 ABO male, constant row: `Z000000000 -0.16 -0.06 -0.05 -0.26 0.09 0.21 -0.18 0.00 -0.14` [read]. **Also corrected:** the earlier note that Troyer's A, B, O are "fundamental" ratings while Hoey uses transients is a false contrast. The Interact guide defines the regressors as *pre-event* impressions of A, B, O; for a first event these equal fundamentals, and Hoey's G uses previous transients for actor and object and the new fundamental for behaviour, which is the same thing. What does differ is the **term set**: Troyer's equation (from Smith-Lovin 1987) and Hoey's G (from Heise 2007) share the shape (constant/linear terms plus selected two- and three-way products, 28 non-constant terms each) but not the terms (e.g. Troyer has A_a B_e, A_e B_a, A_a B_a O_a; Hoey's G has A x O products tau_ae tau_ce, tau_ae tau_cp absent from Troyer). Different estimations, different selected terms.

**Structure of the map.** Linear terms plus products of up to three elements; mostly cross-element products (actor x behaviour, behaviour x object, three-way). Within the behaviour component the map is linear in f_b' once tau and x are fixed, so tau' = H(tau,x) f_b' - C(tau,x) with H a 9 x 3 and C a 9 x 1 matrix [read, Hoey et al. §3.1.1 eq. after (4)].

**Equation families.** Interact carries separate coefficient sets for: U.S.A. 1978, Japan 1984, Canada 1985, China 2000 (listed in the menu), Germany 2007; and notes US 1970s equations are used for Irish and Chinese analyses, Canadian 1990s equations for Canada, Japanese 1990s for Japan, German 2007 for Germany; male and female equation sets exist [read, guide, "Changing Cultures" and "Impression-formation Equations"]. The guide states the ABO equations "were obtained in two phases" and that ABOS equations came from stepwise regression, and that methodological differences may produce differences in results [read, guide footnote 5]. Nuance: the guide's menu list (1978, 1984, 1985, 2000, 2007) and the running-text list (1990s Canada and Japan) disagree on dates inside the same document. I have not resolved which is right. (Validation: the *actdata* equation files are labelled canada1985 and japan1984, matching the menu, and the guide's own Cultures page dates the Canadian data to "the mid-1980s", so the running text's "1990s" looks like the error; the Japanese ratings, though, run 1989-1996 per that page, so it is not settled. Hoey et al. say impression-formation equations exist for English, Japanese and German [read].)

**Modifier and emotion equations.** Emotions are a function of the transient impression of self and its difference from the fundamental identity sentiment; separate empirically derived equations. Hoey et al. (§3.2 in the arXiv v2 text) cite only Heise 2007 ch. 14 for these [read]. Averett & Heise 1987 (above) and Heise, D. R. & Thomas, L. (1989), Predicting impressions created by combinations of emotion and social identity, *Social Psychology Quarterly* 52, 141-, doi:10.2307/2786913 exist (Crossref) but were not opened; their attribution to emotion/amalgamation equations is from Wikipedia. Coefficients: the emotionid/traitid sets in *actdata* (see §2).

## 3. Deflection and the control principle

**Exact definition** [read, Hoey et al. eq. (1)]:

    D = sum_i w_i (f_i - tau_i)^2

summed over the nine fundamental/transient components (E, P, A of actor, behaviour, object), w_i typically 1.0. Troyer says the same ("sum of the squared differences between fundamental sentiments of the ABO elements and transient impressions"), and attributes to Heise & MacKinnon (1987) the claim that deflection corresponds to perceived *likelihood* of an event [read, secondary]. Heise & MacKinnon (1987) Affective bases of likelihood judgments, *J. Math. Sociol.* 13, 133-151, doi:10.1080/0022250x.1987.9990029 (Crossref; original article); reprinted in *Analyzing Social Interaction* (Routledge, 2016), doi:10.4324/9781315025773-5.

**Affect control principle** [read, Hoey et al. Definition 1]: actors work to experience transient impressions consistent with their fundamental sentiments. Interact's rules of thumb for who acts next: the person whose optimal action yields the lowest deflection (the guide reports an example of 0.87, 1.19, 1.27) [read, guide].

**Deflection decomposition** [read, guide]: Interact reports total deflection and the parts from stressing the actor's identity and the object's identity; the remainder comes from behaviour and setting. Interact also bins deflection into four quarters on a graph (comfortable/normal, unusual, weird, and "invalidates the impression"); the guide's worked event has deflection 4.3 in the lowest sector; so the scale is unbounded sum of squares, not 0-1.

**Optimal behaviour (closed form).** Because tau' is linear in f_b' (above), minimising D over f_b' is a quadratic minimisation, a linear solve. Hoey et al. derive it in their appendix B and state the result matches **Heise (2007) eq. (12.21)** exactly: in Heise's notation (Hoey et al. eq. 49), f_b* = -(S_beta^T I_beta [I; -M] [I -M] I_beta S_beta)^{-1} S_beta^T I_beta [I; -M] [I -M] I_beta g_beta, a least-squares solve; in Hoey's own notation (eq. 46), with H_a, H_b, H_c (3 x 3 blocks of H) and C_a, C_b, C_c, f_b* = -z^{-1}[-H_a(f_a - C_a - ...) - H_c(f_c - C_c - ...) - z C_b (1 - H_b)^{-1}], z = H_a^T H_a + (I - H_b)^T(I - H_b) + H_c^T H_c [read; block layout reconstructed from a scrambled extraction, check against the PDF before coding]. Equations (13.11) and (13.18) of Heise 2007 give the corresponding closed forms for the optimal actor and object identities [read, via Hoey et al.]. Practical consequence: Interact finds the *dictionary* behaviour nearest to the continuous optimum, so predictions are restricted to the finite set of rated words. Hoey et al. warn of constraints in the action space ("you can't give a student a really hard problem to solve in a way that will seem accommodating/submissive") [read].

**Reidentification and attribution.** When deflection is too high to be resolved by behaviour, actors relabel the other (e.g. "grouch", "delinquent" in Troyer's two simulations: deflections 2.0, 5.0, 7.0, then 12.0 or 14.0, with relabel and response "scold" or "avoid") [read, Troyer 2004 Table 2].

**Algebraic reading.** What exists: a state space R^9 (or R^3 per concept), a fixed nonlinear map per event type, a quadratic potential, and a closed-form arg-min. Not present: any composition law between acts (two events in a row are handled by iterating the map, with the previous transients as state, not by an algebraic composition), and no statement that the family of event maps is closed under anything. The map is a 3-degree polynomial in the transient state; it is not linear in state, so it does not give a matrix group.

## 4. BayesACT (Hoey, Schröder & Alhothali)

**Citations.** Hoey, J., Schröder, T., & Alhothali, A. (2013). Bayesian Affect Control Theory. *ACII 2013*, 166-172. doi:10.1109/acii.2013.34 (Crossref confirms; as in file 03). Hoey, J., Schröder, T., & Alhothali, A. (2016). Affect control processes: Intelligent affective interaction using a partially observable Markov decision process. *Artificial Intelligence* 230, 134-172. doi:10.1016/j.artint.2015.09.004 (Crossref confirms). Preprint arXiv:1306.5279 (this is the text read). Schröder, T., Hoey, J., & Rogers, K. B. (2016). Modeling dynamic identities and uncertainty in social interactions: Bayesian affect control theory. *American Sociological Review* 81(4), 828-855, doi:10.1177/0003122416650963 (Crossref). Note arXiv 1306.5279 (v2, April 2014) is the preprint of the 2016 *Artificial Intelligence* paper, same title; appendix at cs.uwaterloo.ca/~jhoey/papers/ASRAppendix.pdf (read: page 1 only plus parameter table).

**Their vocabulary.** Fundamental dynamics, transient dynamics, deflection potential, identity inertia, belief state over sentiments, client/agent, POMCP-C.

**Model as stated** [read, arXiv 1306.5279 §3]:
- Transient dynamics, deterministic: Pr(tau' | tau, f', x) = delta(tau' - H(tau,x) f_b' - C(tau,x)) (eq. 5).
- Deflection potential: phi(f', tau') proportional to exp(-(f'-tau')^T Sigma^{-1} (f'-tau')) (eq. 7); the paper says that if Sigma is diagonal with elements 1/w_i, then log phi = D + c where D is eq. (1) [read]. **Sign slip in the source:** from eq. (7) as printed, log phi = -D + c; the potential is highest at zero deflection.
- Fundamental dynamics: Pr(f' | f, tau, x, b_a, phi) proportional to exp(-psi(f',tau,x) - xi(f',f,b_a,x)) (eq. 8), psi = (f' - M G)^T Sigma^{-1} (f' - M G) (eq. 18), and xi an "inertia" term keeping f' near f for identities and equal to the agent's chosen behaviour b_a on the agent's turn.
- Expected deflection under belief b(s): E_b[D] = integral b(s) D(s) ds (eq. 13); states of "Joy" and other emotions would be functions of (f, tau).
- Planning: a POMDP with reward on top of the potential; sequential Monte Carlo for the belief; POMCP-C (continuous Monte-Carlo planner) in the UAI 2015 follow-up (title from a search result, not opened).
- Appendix simulation parameters for Simulation 1: alpha = 0.1 (std. dev. of a diagonal Sigma), identity inertia beta_a = beta_c = 0.001, initial identity std. dev. 2.0 (agent) and 0.01 (client) [read, ASR appendix].

**Theorems or derived predictions.** The paper re-derives Heise's closed-form optimal behaviour (eq. 12.21) as a limit of its Gaussian treatment (appendix B). No new theorem about long-run behaviour.

**Empirical standing** (blunt). Simulations show BayesACT agents recover identities with low identity-deflection over sample counts, tolerate noise, and track a shifting client (Appendix C tables) [read, text]. Human evidence is a pilot: a 37-participant survey to build a tutoring system's EPA mappings and a 20-participant (7 female) study of the "MathTutor", 10 per arm, about 20 minutes' use, with one-tailed t-tests (df = 18, p < .05 to < .01) comparing BayesAct to a control tutor that chose its affective action at random from the same set, on items like "dialogue was simple and natural"; mean deflection 2.9 +/- 2.1 (BayesAct) vs 4.5 +/- 2.2 (random) [read, §4.2.1 and Table 2]. The 37-participant survey was 22 female [read]. Hoey et al. themselves say to treat this small-sample result with caution [read]. The ASR paper's evidence is simulation. I did not find evidence that the BayesACT *behaviour* predictions have been tested against naturally occurring interaction data.

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
- **USA Indiana 2003** (Francis & Heise, "Mean Affective Ratings of 1,500 Concepts by Indiana University Undergraduates in 2002-3"): 1,027 respondents (US-resident at 16, roughly gender-balanced), 1,500 concepts = 500 identities, 500 behaviours, 300 modifiers, 200 settings; collected online with the Surveyor applet; licence not stated on the page. (Validation: the Interact guide's own Cultures page describes the same IU 2003 data as "970 raters ... 496 female, 474 male"; the hub's N = 1,027 and the guide's 970 disagree, perhaps before and after exclusions. Unresolved.)
- **West Germany 1989** (Schneider, "Mean Affective Ratings of 804 Concepts by West German Students in 1989"): N = 520 (mostly Mannheim; 12th-13th-grade pupils and university students), 442 identities, 295 behaviours, 67 modifiers; concepts chosen for back-translatability with the 1978 US dictionary. (Validation: the Interact guide's Cultures page gives "400 Mannheim students" for the same data; hub says N = 520. Unresolved.)

**Format and access.** Described as "[Computer file]"; downloadable through Interact or from Aidan Combs's *actdata* repository (the pages spell it "Comb's"; link given there: https://ahcombs.github.io/actdata/index.html; source github.com/ahcombs/actdata, an R package in beta, "dictionaries and equations ... spanning about 45 years", package licence CC0-1.0 [read in validation]). The CC0 package licence and Heise's noncommercial terms below sit uneasily together; for a public repo, ask rather than assume. No file format was stated on the pages opened. Per the guide's terms of use: site materials are copyrighted by Heise/Indiana, "for noncommercial, research use only"; governmental, political or commercial use needs written permission [read]. So a public repo of these data would need permission; for private modelling noncommercial use is permitted.

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

**Does not exist** (in what I found). ~~Published, tabulated coefficients~~ (struck in validation: they are public in *actdata* and Interact, see §2); independent replication or effect sizes for deflection-minimisation as a predictor of behaviour; any law of composition for acts; any treatment of groups beyond dyads plus a turn-taking heuristic; anything for asymmetric power/status beyond P in EPA; a drive vocabulary beyond consistency; validation that the EPA map's fixed coefficients survive across decades (the guide itself uses 1978-vs-2007 families).

## 10. Corrections to file 03

File 03 says the ACT equation form was "from the validator's knowledge" and not quoted. This file now supplies the printed forms: deflection D = sum w_i (f_i - tau_i)^2 [read] and the 29-term feature vector [read, with a layout caveat], plus Troyer's printed 28-coefficient equation for the actor's transient evaluation [read], and (validation) the location of the actual coefficient tables (*actdata*). 03's reading of ACT as "a fitted polynomial map on EPA vectors, deflection minimisation with a closed-form optimum" is confirmed.

## Unconfirmed

- ~~The coefficient values M~~ Resolved in validation: public in *actdata* (`data-raw/eqns/`) and Interact's View-equations screen. Which set Hoey et al. used is not stated in what was read.
- Exact term ordering in G for some middle terms (PDF extraction scrambled layout).
- The matrix expression for f_b* (eq. 12.21) transcribed only in outline.
- Scale range: -4.3..4.3 (Hoey) vs -4.5..4.5 (Troyer) not reconciled.
- Which year's equation set (1978/1984/1985/2000/2007 in the guide menu, versus 1990s in running text) belongs to Canada and Japan. Partly resolved: *actdata* labels them canada1985 and japan1984, matching the menu.
- Dataset sample sizes, concept counts, licence for the 16 dictionaries I did not open. (*actdata* located: github.com/ahcombs/actdata.) Rater counts disagree between hub and guide for the two opened (1,027 vs 970; 520 vs 400).
- Effect sizes or accuracy figures for the leadership, non-verbal and turn-taking studies (not opened).
- The "eleven repositories" versus 18 listed datasets: the guide's older count against the hub's newer list.
- ~~Whether Heise 2010 *Surveying Cultures* is the book cited~~ Resolved: Crossref doi:10.1002/9780470575789 is Heise, *Surveying Cultures*, Wiley, online 2009-12-23; Hoey et al. cite "Surveying Cultures: Discovering Shared Conceptions and Sentiments. Wiley, 2010", the same book (print year 2010).
- Schröder (2011) as a source of emotion equations (from Wikipedia; not identified on Crossref in this pass).
- "No independent meta-analysis / no independent test" (Summary, §6, §9): not re-tested in validation, because the shared web-search budget was exhausted before this check; treat as the original author's negative finding, unverified.

## Validation log (2026-10-29)

Sources opened in validation: arXiv 1306.5279v2 PDF (full text), Troyer 2004 PDF (AAAI CDN), Interact guide PDF and its HTML Cultures and Equations pages (cs.uwaterloo.ca ACT mirror), ASR appendix PDF, affectcontroltheory.org hub and the two dictionary pages, the *actdata* GitHub repo; every DOI resolved at api.crossref.org/works/<doi>.

- ✓ Smith-Lovin 1987, Impressions from events, JMS 13(1-2) 35-70, doi:10.1080/0022250x.1987.9990026.
- ✓ Heise 1987, Affect control theory: Concepts and model, JMS 13 1-33, doi:10.1080/0022250x.1987.9990025.
- ✓ Smith-Lovin 1987b, The affective control of events within settings, JMS 13 71-101, doi:...9990027.
- ✎ Averett & Heise 1987: added title and pages (Modified social identities: Amalgamations, attributions, and emotions, JMS 13 103-132); DOI ✓.
- ✎ Heise & Smith-Lovin 1981: added SPQ 44(2), first page 93; DOI ✓.
- ✎ Heise & MacKinnon 1987: added the original JMS DOI 10.1080/0022250x.1987.9990029 (pp. 133-151); the cited 10.4324 DOI is a 2016 Routledge reprint.
- ✎ Troyer 2004: exact title and stable URL added; equation transcription ✓ exact; source's duplicated B_a O_e term noted; "same regression structure as Hoey's G" and the "fundamental vs transient" contrast corrected (same shape, different term sets; regressors are pre-event impressions); -4.5..+4.5, 15 raters, Table 2 deflections 2.0/5.0/7.0/12.0 or 14.0 and grouch/scold, delinquent/avoid ✓.
- ✎ Hoey, Schröder & Alhothali arXiv 1306.5279 / AIJ 2016 230 134-172 (doi ✓): eq. 1, 3, 5, 7, 8, 13, 18, H/C refactoring, -4.3..+4.3, professor/student EPA, consistency-theory placement, "many experimental and observational studies" quote, 37/20-participant studies, df = 18, caution remark, eq. 12.21/13.11/13.18 claims ✓; added the source's sign slip (log phi = -D + c, not D + c), the random-control design and deflection means, and a transcription of eq. 46/49; G is Heise 2007 eq. 11.16.
- ✓ Hoey, Schröder & Alhothali 2013, ACII 166-172, doi:10.1109/acii.2013.34.
- ✎ Schröder, Hoey & Rogers 2016 ASR: added 81(4) 828-855; appendix Simulation 1 parameters (alpha 0.1, beta_a = beta_c = 0.001, initial s.d. 2.0 / 0.01) ✓.
- ✓ Schröder & Scholl 2009 SPQ 72(2) 180-197; ✓ Schröder, Netzel, Schermuly & Scholl 2013 Social Psychology 44(1) 47-58; ✓ Heise 2013 SPQ 76(1) 52-72 (all Crossref; citation-level only, as the file says).
- ✓ Heise, *Surveying Cultures* (Wiley, doi:10.1002/9780470575789): same book Hoey et al. cite as 2010; moved from Unconfirmed to resolved.
- ✎ Heise & Thomas 1989: added SPQ 52, 141-, doi:10.2307/2786913 (Crossref); Hoey et al. cite only Heise 2007 ch. 14 for emotion equations, so the other emotion attributions are from Wikipedia, now said so.
- ? Schröder 2011 (emotion equations): not identified; moved to Unconfirmed.
- ? Heise 2007 *Expressive Order* (Springer): existence attested by Hoey et al. and the guide; not opened, no DOI checked.
- ✓ Interact guide (Heise): six nations / quarter century, eleven repositories, six without settings, equation-culture menu years vs 1990s text, two-phase ABO and stepwise ABOS footnote, child EPA values, 0.87/1.19/1.27, deflection 4.3 in lowest sector, four-quarter graph labels, 1972 PL/1 to 1997 Java history, "Mac hits Bob", noncommercial terms: all found in the PDF.
- ✓ affectcontroltheory.org hub: 18 datasets as tabled; Indiana 2003 (N 1,027; 500/500/300/200) and West Germany 1989 (N 520; 442/295/67) pages ✓; ✎ noted the guide's conflicting rater counts (970; 400).
- ✎ *actdata*: owner is Aidan Combs (not "Comb"), located at github.com/ahcombs/actdata, CC0; it holds the equation coefficients, which the file had said were unavailable. Corrected in §2, §9, §10 and Unconfirmed.

**Verdict.** The file is substantially accurate: every DOI resolves to the stated work and authors, and the equations, numbers and quotations checked against the opened sources match, with no fabrications found. The main correction is that ACT's impression-formation coefficients are not locked in Heise 2007 but are published in machine-readable form (Interact, Combs's *actdata*), which changes what the algebra can use directly; smaller fixes are a sign slip inherited from Hoey et al., an overstated equivalence between Troyer's and Hoey's term sets, and missing original-journal DOIs. The "no independent test" negative was not re-searched (search budget exhausted) and stands as unverified.

## Cross-checks (2026-10-29)

Checked against the other files in this directory (grep for ACT, Heise, Hoey, Troyer, deflection, EPA, Osgood, Smith-Lovin). Files that touch ACT: 03, 06, 32 (and 15/16/19/20/082 mention it only in passing or not at all).

**Agreements**
- **03 section 2 (ACT):** same event grammar (actor-behaviour-object, with setting), two layers (fundamental sentiments, transient impressions), EPA profiles per element. 03's description of the map (one regression per post-event value, nine in all, on the nine pre-event EPA values plus selected two- and three-way products, estimated per culture) matches 045 section 2 (9 x 29 matrix M, monomials to degree 3). Deflection as weighted squared difference matches 045 section 3, eq. (1).
- **03 section 2 citations:** Averett & Heise 1987 (JMS 13(1-2) 103-132, doi:10.1080/0022250X.1987.9990028) and Hoey, Schroder & Alhothali 2013 (ACII 166-172, doi:10.1109/ACII.2013.34) match 045 sections 2 and 4. Interact guide mirror at cs.uwaterloo.ca/~jhoey matches 045 sources.
- **03 Limits and Relevance, and 03 summary lists ("No closed composition law beyond iterating the map", "no group structure beyond actor and object", dictionaries and fitted equations could supply parameters)** agree with 045 sections 3 (algebraic reading), 8 and 9.
- **03 "Unconfirmed" (ACT equation form was from the validator's knowledge, not quoted)** is resolved by 045: section 10 supplies the printed forms. 045 confirms 03's reading.
- **06 (Heise 1979, *Understanding Events*; ABO events with EPA vectors and empirically estimated impression-change equations):** agrees with 045. 06 flags ACT as "literally operators with equations", consistent with 045 section 8.
- **32 section 4 (Osgood, Suci & Tannenbaum 1957; Osgood, May & Miron 1975; EPA = Evaluation, Potency, Activity) and 32's translation that ACT is the only worked, estimable operator calculus on EPA:** agrees with 045 sections 1 and 8. 045's per-culture dictionaries are consistent with 32's cross-cultural EPA universals claim; no number overlaps conflict (32's 40 teenage male raters and 620 concepts are Osgood 1975, not the ACT dictionaries).
- **Closed-form optimal behaviour (03 summary line, "deflection minimisation with a closed-form optimum")** agrees with 045 section 3.

**Contradictions**
1. **32 section 4, "Operators / equations": "events change EPA by a linear transformation function."** 045 section 2 says the event map is a degree-3 polynomial in the transient state (29-term feature vector G), linear only in the new behaviour's own EPA once the state is fixed. 03 section 2 also says a polynomial map with product terms. **Verdict: 045 (and 03) right, 32 wrong.** Primary source re-checked this session: Hoey, Schroder & Alhothali, arXiv 1306.5279v2, text: "G is a non-linear operator that combines tau, f', and x", "M is then a 9 x 29 matrix", G a 29 x 1 vector; Troyer 2004 prints products up to three-way. 32 should read "a fitted non-linear (polynomial) map", with linearity holding only in the behaviour term.
2. **03 section 2 / Unconfirmed vs 045 section 10 on provenance of the equation form.** Not a factual conflict: 03 labels its form "validator knowledge" and 045 supplies the sourced form. One residual detail: 03 says "nine pre-event EPA values plus a selected set of two- and three-way product terms", and 045 shows the term set differs between sources (Troyer/Smith-Lovin 1987 versus Hoey/Heise 2007 eq. 11.16). **Verdict: compatible; 03 should not imply one canonical term set.**

**Minor items for the record (no conflict, 045 could be updated)**
- 045 Validation log says Heise 2007 *Expressive Order* was "not opened, no DOI checked". 03 section 2 records doi:10.1007/978-0-387-38179-4 as Crossref-confirmed. Take that DOI from 03.
- 06 gives Heise 1979 with "no DOI checked"; 03 marks it secondary (Wikipedia). 045 does not cite it. Nothing to reconcile.
- No other file (16, 19, 20, 42, 059, 082, 050) cites ACT, Hoey, Troyer, Smith-Lovin or the dictionaries, so 045's dictionary sizes, deflection definition and BayesACT study numbers have no second source in the directory.
