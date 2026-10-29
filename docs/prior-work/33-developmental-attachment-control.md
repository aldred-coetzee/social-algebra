# Prior work 33: developmental origins of social drives and their control-system models

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: attachment theory as a control system, Bischof's Zurich model, infant dyadic regulation, shared intentionality, mastery and curiosity development, social referencing, Harlow. Context: Aldred's aim, "an algebra which expresses basic human drives and group drives, which we can compose into equations, which we can then use to start making theorems and use to control or predict behavior... curiosity, fear, desire". Cross-references: 15 (taxonomies), 16 (formal models), 17 (curiosity, fear, desire), 20 (dyadic coupling), 22 (neuroscience; Panksepp), 31 (ethology).

**Method and honesty note.** Tags: `[read]` = read at source this session; `[from abstract/standard account]` = abstract, search snippet or background knowledge, not checked against the primary. All DOIs below were returned by the Crossref API this session (title, authors, year, journal matched) unless marked otherwise. **Only one work in this cluster was read at source in full: Gubler & Bischof (1991)**, an open-access copy of the book (Munich repository, text extracted with `pdftotext`). Everything else, including every number from a meta-analysis, is secondary or from memory, and is flagged. Attempts to read the Mesman et al. 2009 and Pinquart et al. 2013 full texts failed (HTTP 403); an attempt to fetch a university-hosted PDF of van IJzendoorn & Kroonenberg 1988 was blocked by the permission layer as a possibly unauthorised copy, and was not retried.

**Summary.**
1. **The one genuinely formal object here is Bischof's Zurich model, and it is exactly the kind of thing the algebra wants.** It is a closed set of scalar and vector equations: familiarity and relevance detectors, a proximity kernel, a joint-potency saturation rule, security and arousal as products, two setpoints (dependency D, enterprise E), appetence = setpoint minus level, a leaky-integrator "pool" refinement, an acclimatization rule that moves the setpoints, and the identity D = 1 - C, E = C. It reproduces the Strange Situation qualitatively (a 15-month-old retreats to mother when a stranger appears; a pubertal subject approaches the stranger), and the same chapter reports two parameter fits to data: Gubler's (1989) painted quail and Friedländer's (1987) toddlers (15 children, mean fit quality 0.7, with out-of-sample prediction). It is single-agent by construction (the paper "severs" social feedback loops on purpose). It is a worked example of how fear, curiosity and attachment fall out of two coupled homeostats, which is a direct answer to Aldred's "curiosity, fear, desire" request.
2. **Bowlby is control-systems in intent but not in equations.** The "equations" are verbal. Bischof (1975) is the mathematisation (the 1991 chapter itself says "Bischof (1975) pioneered this approach"), and it is much less cited.
3. **The empirical record is uneven, and the algebra should know which operators are solid.** Strong: still-face effect, social referencing direction, Harlow's contact comfort. Moderate: attachment classification stability (moderate, not high), sensitivity to security link (modest). Weak or contested: the specific numbers behind classic social-referencing demonstrations, and the transfer of Strange Situation categories across cultures.

---

## 1. Bowlby: attachment as a control system

**Citation.** Bowlby, J. (1969). *Attachment and Loss, Vol. 1: Attachment*. Hogarth / Basic Books (2nd ed. 1982). Vol. 2 *Separation: Anxiety and Anger* (1973); Vol. 3 *Loss* (1980). No DOI (books). Secondary: Bretherton, I. (1992). The origins of attachment theory: John Bowlby and Mary Ainsworth. *Developmental Psychology*, 28(5), 759-775. DOI 10.1037/0012-1649.28.5.759 (Crossref-confirmed). Bowlby, J. (1982). Attachment and loss: Retrospect and prospect. *Am. J. Orthopsychiatry*, 52(4), 664-678. DOI 10.1111/j.1939-0025.1982.tb01456.x (Crossref-confirmed).

**Read status.** Not read. Everything below is `[from abstract/standard account]`; the Zurich paper (section 3) was read and quotes Bowlby (1971 Penguin ed.) as the thing it formalises.

**Their vocabulary.** Behavioural system; set-goal (a "set-goal" is a desired state of the organism-environment relation, here a degree of proximity or accessibility to the attachment figure, not a fixed place); attachment behaviour; exploratory system; fear (wariness) system; sociable system; "secure base"; internal working model; felt security; environmental-stability argument (the "environment of evolutionary adaptedness", Bowlby's term).

**Drives/operands.** Attachment (proximity-seeking to a preferred figure), exploration, fear/wariness, affiliation. Bowlby deliberately rejected the psychoanalytic "drive" language (secondary drive from feeding) in favour of "behavioural systems" organised by control-theoretic goal correction, citing Craik, Wiener, Miller-Galanter-Pribram, and Ashby. In the algebra's terms: these are state-dependent controllers, not energy quantities.

**Operators / equations.** `[standard account]` None are given in the original as equations. The structure is: a comparator takes the perceived proximity/accessibility of the figure, compares it with a set-goal whose value is raised by internal states (illness, fatigue, hunger) and by external alarm (a strange or sudden event, separation); if the discrepancy exceeds a threshold, attachment behaviours (signalling, approaching, clinging) are activated until the discrepancy is cancelled. Exploration is activated when the attachment system is quiescent. Fear and attachment are tied: fear raises the proximity set-goal. The secure-base idea is that the figure's accessibility lets the exploration system run, i.e. the three systems form a priority-ordered, mutually inhibiting set.

**Theorems or derived predictions.** Verbal only: (a) a threatened infant seeks proximity; (b) the figure's presence reduces fear and enables exploration; (c) separation produces protest, despair and detachment (Vol. 2). No quantitative law and nothing derivable beyond ordering. The one formal consequence that has been tested is the exploration-vs-proximity trade-off in the Strange Situation (section 2).

**Empirical standing.** The core claims (proximity-seeking under threat, secure-base effect on exploration, protest on separation) are among the best replicated in developmental psychology. The control-systems *framing* has not been formally tested; the quantitative model that tests it is Bischof's.

**Operand/operator translation.** Operands: three activation levels (attachment A, exploration X, fear F) per person; one set-goal parameter per system. Operators: a *raise-set-goal* operator (alarm: sets proximity set-goal up), a *cancel* operator (figure present: discrepancy to zero), and a priority/inhibition relation between systems. Everything Bowlby says that is not in Bischof is a candidate law with no equation behind it. The honest gap: no stated rule for how much a stimulus raises the set-goal, nor for how exploration and attachment trade off numerically.

---

## 2. Ainsworth: Strange Situation and the classifications

**Citations.**
- Ainsworth, M. D. S., & Bell, S. M. (1970). Attachment, exploration, and separation: Illustrated by the behavior of one-year-olds in a strange situation. *Child Development*, 41(1), 49-67. DOI 10.2307/1127388 (Crossref-confirmed).
- Ainsworth, M. D. S., Blehar, M. C., Waters, E., & Wall, S. (1978). *Patterns of Attachment: A Psychological Study of the Strange Situation*. Erlbaum. No DOI.
- Main, M., & Solomon, J. (1990). Procedures for identifying infants as disorganized/disoriented during the Ainsworth Strange Situation. In Greenberg, Cicchetti & Cummings (Eds.), *Attachment in the Preschool Years*. Univ. Chicago Press. No DOI. (Not found in Crossref.)
- van IJzendoorn, M. H., Schuengel, C., & Bakermans-Kranenburg, M. J. (1999). Disorganized attachment in early childhood: Meta-analysis of precursors, concomitants, and sequelae. *Development and Psychopathology*, 11(2), 225-250. DOI 10.1017/s0954579499002035 (Crossref-confirmed).
- van IJzendoorn, M. H., & Kroonenberg, P. M. (1988). Cross-cultural patterns of attachment: A meta-analysis of the Strange Situation. *Child Development*, 59, 147-156. DOI 10.1111/j.1467-8624.1988.tb03202.x (Crossref-confirmed).

**Read status.** None read. `[from abstract/standard account]` throughout; the Cross-cultural paper's design (32 studies, nearly 2,000 classifications, 8 countries) is confirmed from a search summary.

**Their vocabulary.** Strange Situation (eight episodes, the first a brief introduction and the other seven nominally 3 minutes, separations curtailed if the infant is very distressed: mother and infant, stranger enters, separation, reunion, alone, stranger returns, mother returns); secure (B), insecure-avoidant (A), insecure-resistant/ambivalent (C), later disorganized/disoriented (D); maternal sensitivity; exploration, proximity-seeking, contact-maintaining, avoidance, resistance as coded scales.

**Drives/operands.** The operationalised variables are behavioural: exploration, proximity seeking, contact maintaining, avoidance, resistance. The classification is a *regulatory strategy*: B balances exploration and proximity as the discrepancy changes; A deactivates attachment display; C hyperactivates it; D is breakdown of any strategy (fear of the figure).

**Operators / equations.** `[standard account]` None. A classification is a discrete label from a coding tree, not a model.

**Theorems or derived predictions.** (a) Sensitive caregiving predicts B. (b) Classification predicts later social competence, with weaker prediction for internalising problems. (c) Disorganisation is predicted by frightening or frightened caregiver behaviour and maltreatment.

**Empirical standing.** Blunt version:
- Strange Situation is reliably codable and widely replicated. It is a *relationship-specific* measure (infant-mother and infant-father classifications differ).
- Sensitivity-to-security link is real but modest: De Wolff & van IJzendoorn (1997), *Child Development* 68, 571-591, DOI 10.2307/1132107 (Crossref-confirmed; `[from abstract, via search snippet]`: r = .24 is the combined effect for the core subset of 21 Strange Situation studies, N = 1,099, out of 66 studies, N = 4,176, in total; "moderately strong" by Cohen's criteria). Madigan et al. (2024, *Psychological Bulletin*) report a near-identical pooled r = .25 (k = 174, N = 22,914) `[search snippet only; not Crossref-checked]`. Bakermans-Kranenburg, van IJzendoorn & Juffer (2003), *Psychological Bulletin* 129, 195-215, DOI 10.1037/0033-2909.129.2.195 (Crossref-confirmed): interventions raise sensitivity more than they raise security (`[from abstract, via search snippet]`: randomised interventions d = 0.33 on insensitive parenting, d = 0.20 on attachment insecurity; 70 studies, 88 intervention effects). So the "sensitivity transmission gap" is a known unexplained residual.
- Temperament is not the explanation: Groh et al. (2017), *Child Development* 88, 770-795, DOI 10.1111/cdev.12677, **[read, Crossref abstract]**: 109 samples, N = 11,440; temperament weakly associated with insecurity (d = .14, CI .08-.19), modestly with resistant (d = .30), not significantly with avoidant (d = .10) or disorganized (d = .11).
- **Stability.** Fraley (2002), *Pers. Soc. Psychol. Rev.* 6, 123-151, DOI 10.1207/s15327957pspr0602_03, **[read, Crossref abstract]**: "attachment security is moderately stable across the first 19 years of life and ... patterns of stability are best accounted for by prototype dynamics" (i.e. early patterns keep some influence vs. a pure-revision model). Pinquart, Feußner & Ahnert (2013), *Attachment & Human Development* 15(2), 189-218, DOI 10.1080/14616734.2013.746257 (Crossref-confirmed), **[read, PubMed abstract]**: 127 papers, n = 21,072 attachments, 225 time intervals from half a month to 29 years; overall **r = .39**, "a medium-sized stability"; no significant stability over intervals longer than 15 years; higher for intervals under two years than over five, for representational rather than behavioural measures beyond infancy, and for middle-class rather than at-risk samples. (A 2021 *Frontiers* paper paraphrases it as "very high in childhood after the age of 6"; that phrase is not in the abstract.) Waters et al. (2000), *Child Development* 71(3), 684-689, DOI 10.1111/1467-8624.00176 (Crossref-confirmed), **[read, PubMed abstract]**: 50 of 60 infants re-assessed about 20 years later; 72% kept the same secure/insecure classification (kappa = .44); 44% (8/18) changed where mothers reported negative life events vs. 22% (7/32) where none were reported. **Unqualified conclusion: moderate, not high.** The algebra should model security as a slowly drifting parameter, not a fixed type.
- Cross-cultural: van IJzendoorn & Kroonenberg's reported conclusion (from memory, unconfirmed here) is that B is the modal class everywhere and that within-culture variance exceeds between-culture variance; secondary sources confirm more A in individualist and more C in collectivist samples. Treat as a caution that the categories carry cultural assumptions, not as a finding with numbers.
- Disorganisation (1999 meta-analysis), **[read, PubMed abstract]**: nearly 80 studies, more than 6,000 dyads; "about 15%" of infants in normal middle-class families, a rate that "may become twice or even three times higher" in clinical/at-risk groups; "modest" stability.

**Operand/operator translation.** An agent's *attachment strategy* is a three-valued (or continuous two-parameter: anxiety, avoidance) setting of the controller in section 3, not a state: the Zurich model's D and the proximity kernel are where A and C would sit (A: low D, C: high D with weak cancel). Treat classification as a coarse *parameter regime* of the control law; this is a modelling suggestion, not something any source states.

---

## 3. Bischof: the Zurich model of social motivation (the formal core of this file)

**Citations.**
- **Gubler, H., & Bischof, N. (1991).** A systems theory perspective. [Chapter 3.] In M. E. Lamb & H. Keller (Eds.), *Infant Development: Perspectives from German-Speaking Countries* (pp. 35-66; the contents page gives p. 35, "Harry Gubler and Norbert Bischof", and the scan's running heads run to p. 66, where the references begin). Hillsdale, NJ: Lawrence Erlbaum Associates. ISBN 0-8058-0666-0. Open-access scan: https://epub.ub.uni-muenchen.de/2863/1/oa_2863.pdf **[read in full, including all equations, the three simulations and the model-estimation section; re-read in the validation pass]**. The chapter's title, in both the contents and the running head, is simply "A Systems Theory Perspective" (ch. 3); the longer title above is descriptive, not the published one, so cite it as "A systems theory perspective".
- **Bischof, N. (1975).** A systems approach toward the functional connections of attachment and fear. *Child Development*, 46(4), 801-817. DOI 10.2307/1128384 (Crossref-confirmed). Not read; the 1991 chapter says its first two simulations correspond to this paper but with the pool model replacing the proportional model.
- Bischof, N. (1985). *Das Rätsel Ödipus: Die biologischen Wurzeln des Urkonfliktes von Intimität und Autonomie*. München: Piper. No DOI. Not read; cited in the chapter for the autonomy system's positive-feedback stability problems.
- Unpublished Zurich work reported in the chapter (not obtainable, not read): Gubler, H. (1989), doctoral dissertation on pair bonding and distance regulation in the Chinese painted quail (*Excalfactoria chinensis*), Univ. Zürich; Friedländer, R. (1987) and Diener, R. (1982), empirical tests of the (pool) security-regulation model in toddlers, Univ. Zürich, Biomathematical Section.
- **Quirin, M., Malekzad, F., Paudel, D., Knoll, A. C., & Mirolli, M. (2023).** Dynamics of personality: The Zurich model of motivation revived, extended, and applied to personality. *Journal of Personality*, 91(4), 928-946. DOI 10.1111/jopy.12805 (Crossref-confirmed in validation; PMID 36577709). `[from abstract]`: describes the model as cybernetic and nomothetic, linking needs for security, arousal and power to approach-avoidance. The abstract mentions no equations, simulation or implementation; the full text was not read, so whether it contains any is **unconfirmed**.
- Schönbrodt, F. D., Unkelbach, C., & Spinath, F. M. (2009). Broad motives in short scales: A questionnaire for the Zurich Model of Social Motivation. *European J. Psychological Assessment*, 25(3), 141-149. DOI 10.1027/1015-5759.25.3.141 (Crossref-confirmed in validation; an OSF preprint also exists, 10.31219/osf.io/wj78p). Measures five motives (security, arousal, power, prestige, achievement) with six items per scale, per search snippet; psychometrics not read.

**Their vocabulary.** Security system, arousal system, autonomy system (later split: power, prestige, achievement); familiarity detector F, relevancy detector R, locality detector; psychological proximity H(x); potency P; incentive vector I; appetence/aversion A; dependency D; enterprise E; autonomy claim C; "joint familiarity atmosphere"; joint potency; momentum M; pool (leaky integrator); coping (invention, aggression, supplication); acclimatization AC; Buridan's point; "surfeit behaviour".

**Drives/operands (all `[read]`).** Per subject: location y (2-vector); setpoints D (dependency), E (enterprise) in [0,1]; autonomy claim C in [0,1]; levels s (security) and a (arousal) in [0,1]; activations A_s, A_a (scalar, signed) bounded to [-1,1]; incentive vectors I_s, I_a; momenta M_s, M_a. Per social object i: location z_i, familiarity F_i in [0,1] (mother 0.9, stranger 0.4 in the chapter), relevancy R_i in [0,1] (1 = an uncontested alpha adult), treated as fixed attributes.

**Operators / equations `[read]`** (numbering as in the chapter; OCR of the PDF damaged a few symbols, repairs noted):
- (1) Psychological proximity H(x_i): a monotone decaying hyperbola, H = 1 at x = 0, H = 0 for x >= x_max, slope parameter r. (Exact algebraic form was garbled in extraction; only the stated properties are recorded here.)
- (2) Potency P_i = R_i * H(x_i) (the chapter describes it as "the product of proximity and relevancy").
- (3), (4a-c) Incentive magnitudes: |I_si| = P'_i * F_i; |I_ai| = P'_i * (1 - F_i), with P'_i = R_i * H'(x_i), H' a separate decay with its own slope r'. Direction: pointing from the subject toward object i.
- (5) Total incentive I_s(y) = sum_i I_si; same for I_a. A stranger and a mother can cancel; the zero is "Buridan's point" B.
- (6) Joint familiarity atmosphere F = (sum_i P_i * F_i) / (sum_i P_i): potency-weighted mean of familiarities, bounded in [0,1].
- (7) Joint potency P = 1 - prod_i (1 - P_i): quasi-additive for small P_i, saturating at P_max = 1 (two potent objects do not give double security).
- (8) Security s = P * F; arousal a = P * (1 - F). (The extracted text prints "x = P - F"; the prose two paragraphs later says "security as the product of joint familiarity and joint potency", and Fig. 3.1's legend draws these as multiplication nodes; read as products. Confirmed in validation.)
- (9) Activation A_s = D - s, A_a = E - a. Positive means appetence (seek the thing), negative aversion. D is the *setpoint for security*, E the *setpoint for arousal*: both systems are homeostats; the paper notes explicitly that exploration is homeostatic too, "runs counter to a widespread notion" that exploration is antihomeostatic. Fear is arousal above E ("Aversion against arousal (negative Aa), and hence, fear behavior, results from arousal exceeding the setpoint of enterprise"); below E, "an appetence for arousal (positive Aa) develops", which leads to exploration. The chapter itself uses the word "curiosity" for the positive sign: in the arousal momentum field, centrifugal arrows round the stranger denote "fear" and centripetal ones "curiosity". So "fear and curiosity are the two signs of one error term" is the authors' own reading, not an interpretation.
- (10) Momentum M_s = A_s * I_s, M_a = A_a * I_a.
- Motor integration: simple vector sum M_s + M_a, damped with friction, integrated twice to give position; location feeds back into the proximity detectors and closes the loop. The paper itself says competition and time-sharing (McFarland) are "very likely" the right integration but not implemented.
- (11) **Pool model**: A_s(T) = sum_{t=0}^{T} (D - s)_t and A_a(T) = sum_{t=0}^{T} (E - a)_t, i.e. security and arousal set the *rate* of change of the activation, not the activation. Clipped to [-1, 1]. This introduces a double integral (activation -> momentum -> position), which is inherently unstable and produces the undamped oscillations the authors identify with Mahler et al.'s "emotional refueling".
- (12) Coping as random motor unrest of standard deviation u = k * (|A_s| + |A_a| - |M_s + M_a|), only if positive. Unrest rises when the two drives pull against each other and cancel.
- (13) D = 1 - C and E = C, 0 <= C <= 1: **autonomy claim is a single parameter that trades dependency for enterprise.**
- (14)-(16) **Acclimatization**: stress coefficient q(T) = sum over the time since the last adaptation of the *difference* of A_s and A_a (the paper sums the difference "rather than each separately", so excess security can balance excess arousal). If |q| exceeds q_lim, C is moved toward 1 (sustained overarousal) or toward 0 (sustained overprotection) at a rate rho much less than 1 (dC = rho * (1 - C) or -rho * C), and q is reset to zero. The OCR garbled the sign conditions in 16a/16b; the semantics are stated in prose in the chapter.

**Theorems or derived predictions `[read]`.** All are simulation results, not proofs, and all are single-subject with other agents on fixed schedules (the authors say they "sever" the social feedback loops on purpose, and note Ainsworth's own design does the same).
1. **A stranger raises clinging in a dependent infant.** For D = 0.75 the locus A_s = 0 contracts toward the mother when a stranger is added; for D = 0.5 it does not (and the stranger raises s near himself). So "stranger anxiety" is a *conditional* effect that vanishes below a dependency threshold, a derived prediction of equations (6)-(9).
2. **Infancy simulation (C = E = 0.25, D = 0.75):** with mother alone, oscillatory refueling; with mother plus stranger, retreat to mother's lap and oscillation dies; with stranger alone, approach with residual unrest because security and arousal cannot both be satisfied.
3. **Puberty simulation (C = 0.5):** excursions from mother widen; a moderately familiar stranger is approached while the mother is present, with avoidance of the interval between them; when the mother leaves, only moderate effect, because the stranger is still slightly too unfamiliar. A small rise (C = 0.6) is enough to sit comfortably with the stranger.
4. **Acclimatization simulation (C starts at 0):** an irreversible rise in autonomy claim emerges although the mechanism is symmetric in security and arousal. The authors trace the asymmetry to the *choice of familiarity coefficients*: "the stranger is more familiar than the mother is alien" (stranger F = 0.4, mother's alienness 1 - F = 0.1), standing in for the real-life fact that mother stays familiar through separation while strangers become familiar with time (familiarisation itself is not modelled). The authors' conclusion: a mother who provides security and a way to cope with the strange also promotes autonomy "until she is no longer required for security homeostasis". This is the closest thing in the survey so far to a theorem about *how a dyadic arrangement changes a drive's setpoint*.
5. **Empirical contact (section "Model estimation", pp. 60-65).** Two fits, both reported only in this chapter from unpublished Zurich theses:
   - *Quail.* Gubler (1989) fitted a modified pool model to painted-quail pairs (siblings raised together vs. strangers). The fit required four changes: a *site-preference* system alongside attachment; a proportional-*differential* distance controller (partner's approach/withdrawal velocity matters); momentum depending only on the *sign* of A_s; and McFarland-style *time-sharing* between the two momenta. Parameters were estimated from the data and all sibling/stranger differences were accounted for by familiarity alone (stranger pairs synchronised their movement; siblings moved independently).
   - *Human toddlers.* Friedländer (1987) tested emotional refueling in a long corridor, raising arousal with an unlocalisable low-frequency sound (so the arousal incentive field I_a is homogeneous). A modified pool model was fitted per child (example: a 21-month-old); mean fit quality **0.7** across **15 children** (worst 0.4, best 0.9; 1.0 = exact, 0.0 = no better than a straight line). Parameters estimated up to the second sound signal predicted the following minutes with only two new parameters. Diener (1982) used a sudden strange object instead; no results are given.
   The earlier claim in this file that "validation on humans is not in this source" was wrong and has been corrected.

**Empirical standing.** Blunt version:
- The three Strange-Situation simulations are qualitative. But the chapter is **not** fit-free: it reports parameter estimation on quail (Gubler 1989) and on 15 human toddlers with out-of-sample prediction (Friedländer 1987). These are small, unpublished, single-lab, and visible only through this chapter; treat them as existence proofs that the pool model can be fitted, not as validation. The authors list the difficulty that adult and higher-animal relationships are not expressed in spatial distance, which is why the tests use quail and toddlers.
- No replication literature in the usual sense. Quirin et al. (2023) is a revival and extension, not a replication. The questionnaire (MPZM / MPZM-R) has been developed and used (a German-language handbook was in the search results), but a questionnaire for individual differences in motive strength is a different thing from a test of the dynamics.
- I found no independent re-implementation of the 1991 equations. This is **unconfirmed**; Quirin et al. 2023 includes computer scientists (Paudel, Knoll, Mirolli) and may contain one (its abstract does not say so). The nearest independent computational attachment work found in validation is Petters' agent architectures (Petters & Waters 2015; Petters & Beaudoin 2017; see "Missing"), which model Bowlby/Ainsworth scenarios rather than Bischof's equations.
- The chapter itself names the model's main deficiency in its conclusion: only the child regulates distance; the mother's caregiving would have to be added for real dyadic simulation.

**Operand/operator translation.** The most reusable part of the survey so far.
- **Two homeostats with settable setpoints, coupled through a shared stimulus and a shared actuator (distance).** Fear and curiosity are not separate primitives: they are the *signs* of one error term, A_a = E - a. Attachment and surfeit are the signs of A_s = D - s. Four named states from two scalars (the algebra would get fear, curiosity, desire-for-closeness and wish-for-distance as sign-regions).
- **Detector operators:** F(object) and R(object) are labels on operands, not state. In the algebra these are properties of the *other* person (familiarity to me, relevance to me), which is already an asymmetric, directed relation (cf. 20).
- **Joint operators:** the weighted mean (6) and the saturating sum (7) are explicit aggregation laws for several others present. These are the only stated aggregation laws in this file, and they are directly adoptable as "how multiple sources combine into one drive input".
- **Setpoint dynamics:** D = 1 - C, E = C is a conservation-like constraint (dependency plus enterprise = 1) and (14)-(16) is a slow adaptive rule. Candidate theorem class: when does acclimatization converge, and to what C, given a configuration of others (the authors do this by simulation only).
- **Group version:** the chapter says each individual "ought to be endowed with a motivational system of the kind described" and that group interaction could be simulated but is "highly complex"; no result. The group case (every member a Zurich agent with other members as objects, F_i and R_i as inter-member relations) is the obvious extension and **does not exist in this source**.
- **Autonomy as a third system:** the authors flag that its social feedback is *positive* and brings "stability problems" (assumptions 1-3 are rank, achievement and sexual motivation; only 4 and 5 are modelled). That is a gap, and a place where the algebra might add something the original deferred.

---

## 4. Tronick: still-face and mutual regulation

**Citations.**
- Tronick, E. Z., Als, H., Adamson, L., Wise, S., & Brazelton, T. B. (1978). The infant's response to entrapment between contradictory messages in face-to-face interaction. *Journal of the American Academy of Child Psychiatry*, 17(1), 1-13. DOI 10.1016/s0002-7138(09)62273-1 (Crossref-confirmed in validation). The *Pediatrics* 62(3), 403 record (DOI 10.1542/peds.62.3.403) is a one-page item with the same title, i.e. an abstract/notice, not the article; cite J. AACP.
- Tronick, E. Z. (1989). Emotions and emotional communication in infants. *American Psychologist*, 44(2), 112-119. DOI 10.1037/0003-066x.44.2.112 (Crossref-confirmed). Contains the Mutual Regulation Model (MRM). Not read; `[from abstract/standard account]`.
- Gianino, A., & Tronick, E. Z. (1988). The mutual regulation model: The infant's self and interactive regulation and coping and defensive capacities. In Field & Fox (Eds.), *Stress and Coping Across Development*. Erlbaum. No DOI found; the Crossref hit for "Infant coping with interpersonal stress" (Gianino, Plimpton & Tronick 1986, DOI 10.1016/s0163-6383(86)80140-0) is a related but different item.
- Tronick, E. Z., & Cohn, J. F. (1989). Infant-mother face-to-face interaction: Age and gender differences in coordination and the occurrence of miscoordination. *Child Development*, 60, 85-92. DOI 10.2307/1131074 (Crossref-confirmed). Reports that interaction is matched in only about a third of the time, with repair; I recall roughly 30% coordinated; **unconfirmed here**.
- Cohn, J. F., & Tronick, E. Z. (1988). Mother-infant face-to-face interaction: Influence is bidirectional and unrelated to periodic cycles in either partner's behavior. *Developmental Psychology*, 24, 386-392. DOI 10.1037/0012-1649.24.3.386 (Crossref-confirmed). Bidirectional influence found; I did not read it.
- **Mesman, J., van IJzendoorn, M. H., & Bakermans-Kranenburg, M. J. (2009).** The many faces of the Still-Face Paradigm: A review and meta-analysis. *Developmental Review*, 29(2), 120-162. DOI 10.1016/j.dr.2009.02.001 (Crossref-confirmed; full text not read; abstract not retrievable).

**Their vocabulary.** Face-to-face interaction; still-face (mother holds a neutral face); mutual regulation; coordinated and miscoordinated states; interactive repair; matching and mismatching; self-regulation versus other-regulation; coping and defensive behaviours; "dyadic states of consciousness" (later); positive and negative affect; gaze.

**Drives/operands.** An infant has an emotional state and a coping/regulatory capacity; the dyad has a coordination state (matched or mismatched). The infant's drive for coordinated interaction ("engagement") and the caregiver's responsiveness are the two coupled variables.

**Operators / equations.** `[standard account]` No equations. The model is a verbal two-feedback system: infant regulates own state (looking away, self-comforting) and regulates the interaction (signalling to the partner); partner responds. Mismatch is the norm and repair the key transition (mismatch -> repair -> positive affect); the pattern of repair over time is what the infant learns.

**Theorems or derived predictions.** (a) Removing contingent response (still-face) causes a drop in positive affect and gaze, with an increase in negative affect and self-comfort, within about two minutes. (b) Repeated successful repair builds a sense of efficacy. (c) Chronic unrepaired mismatch (e.g. maternal depression) leads to defensive withdrawal.

**Empirical standing.** The still-face *effect* is one of the most replicated infant findings: Mesman et al. (2009) pooled the paradigm's studies; a search summary says there were more than 80 empirical studies by then. The qualitative pattern (positive affect and gaze fall, negative affect rises; positive affect and gaze partly recover at reunion, negative affect does not fully recover, carry-over effect) is confirmed by secondary sources (Li et al. 2019 in *Infancy*, a Brazilian review, and Graham et al. 2018). **I could not retrieve a single effect size from the meta-analysis**; I will not quote any. Cross-cultural caveat: a Dutch/Chinese 4-month-old study (Li, Woudstra, Branger, Wang, Alink & Mesman 2019, *Infancy* 24(6), 893-910, DOI 10.1111/infa.12313, Crossref-confirmed in validation; 123 Dutch and 63 Chinese infants) reports the classic pattern for positive affect and gaze in both countries but a different negative-affect pattern with fathers in Chinese infants, and that only a minority of infants showed the expected pattern across all episodes. So: robust on average, variable across individuals. The "matched only about a third of the time" figure from Tronick & Cohn is cited widely but **not checked**.

**Operand/operator translation.** The still-face is a clean *contingency-removal operator*: it turns off the partner's response while keeping the partner present. In the algebra, it is the control experiment for any dyadic law: dyad state with partner response switched to zero. It supports a model in which the infant's engagement drive has a *setpoint on contingent responsiveness* rather than on proximity (compare Bischof, where the controlled variable is distance). The MRM's mismatch-repair cycle is a candidate for a *dyadic* limit cycle that nothing here formalises (see 20 for formal dyadic coupling work; Beebe, Lachmann & Jaffe (1997), "Mother-infant interaction structures and presymbolic self- and object representations", *Psychoanalytic Dialogues* 7(2), 133-182, DOI 10.1080/10481889709539172, and Beebe & Lachmann (1988), "The contribution of mother-infant mutual influence to the origins of self- and object representations", *Psychoanalytic Psychology* 5(4), 305-337, DOI 10.1037/0736-9735.5.4.305, both Crossref-confirmed, are the closest dyadic-systems statement, not read).

---

## 5. Trevarthen: primary and secondary intersubjectivity

**Citations.** Trevarthen, C. (1979). Communication and cooperation in early infancy: A description of primary intersubjectivity. In M. Bullowa (Ed.), *Before Speech*. Cambridge UP. No DOI found. Trevarthen, C., & Hubley, P. (1978). Secondary intersubjectivity: Confidence, confiding and acts of meaning in the first year. In A. Lock (Ed.), *Action, Gesture and Symbol*. Academic Press. No DOI found (Crossref returned only a 2012 Trevarthen article, DOI 10.1515/cogsem.2012.4.1.6 and a 2009 duplicate, titled "Embodied Human Intersubjectivity...", which I did not read). Reddy, V. (2008). *How Infants Know Minds*. Harvard UP, DOI 10.4159/9780674033887 (Crossref-confirmed), is a modern book-length treatment that I did not read.

**Read status.** None read. Entirely `[from abstract/standard account]`.

**Vocabulary.** Primary intersubjectivity (from about 2 months: dyadic, face-to-face, protoconversation, "innate" sensitivity to the partner's expressions and timing); secondary intersubjectivity (from about 9 months: person-person-object triads; joint attention, social referencing, pointing, gestural sharing). "Innate intersubjectivity", "companionship", "co-regulation".

**Drives/operands.** A motive to engage and share emotion with a partner, present from early on; later a motive to share attention to an object. This is the claim: sociability is a primary motive, not derived.

**Operators / equations.** None. The structural contribution is the *dyad -> triad* step: a new operator type (attend jointly) requires a third term (an object).

**Empirical standing.** The developmental sequence (face-to-face engagement at 2 months, joint attention at 9-12 months) is robust descriptive data. Whether primary intersubjectivity implies "innate" mind-reading is a contested theoretical point, with the field split (Reddy defends a second-person view; others, such as Tomasello below, put the shift to sharing later). No quantitative model.

**Operand/operator translation.** Gives the *type structure* for the algebra: binary relations (dyadic engagement) before ternary relations (person, person, object). Joint attention is the first ternary operator, which matters for the algebra because the group-level operators (shared goals, norms) are all ternary-or-higher.

---

## 6. Tomasello: shared intentionality and the drive to share

**Citations.**
- Tomasello, M., Carpenter, M., Call, J., Behne, T., & Moll, H. (2005). Understanding and sharing intentions: The origins of cultural cognition. *Behavioral and Brain Sciences*, 28(5), 675-691. DOI 10.1017/s0140525x05000129 (Crossref-confirmed). **[read, Crossref abstract]**
- Tomasello, M., & Carpenter, M. (2007). Shared intentionality. *Developmental Science*, 10(1), 121-125. DOI 10.1111/j.1467-7687.2007.00573.x (Crossref-confirmed; Crossref lists the year as 2006, the issue is 2007). **[read, Crossref abstract]**
- Warneken, F., & Tomasello, M. (2006). Altruistic helping in human infants and young chimpanzees. *Science*, 311, 1301-1303. DOI 10.1126/science.1121448 (Crossref-confirmed). `[from abstract/standard account]`.
- Tomasello, M., Carpenter, M., & Liszkowski, U. (2007). A new look at infant pointing. *Child Development*, 78, 705-722. DOI 10.1111/j.1467-8624.2007.01025.x (Crossref-confirmed). Not read.
- Moll, H., & Tomasello, M. (2007). Cooperation and human cognition: the Vygotskian intelligence hypothesis. *Phil. Trans. R. Soc. B*, 362, 639-648. DOI 10.1098/rstb.2006.2000 (Crossref-confirmed). Not read.

**Their vocabulary.** Shared intentionality; joint attention; joint goals; collaborative activity; motivation to share psychological states with others (a basic motive, not derived; the phrase follows the Tomasello et al. 2005 BBS 28(5) and Tomasello & Carpenter 2007 Dev. Sci. 10(1) abstracts as read via Crossref, exact wording and page not verified); dialogic cognitive representations; ape vs. human 1- to 2-year-old comparison; helping; cooperative communication.

**Drives/operands `[read]`.** The 2005 abstract: human children's skills of shared intentionality develop over the first 14 months as two ontogenetic pathways intertwine: (1) the ape-general understanding of others as goal-directed intentional agents; and (2) "a species-unique motivation to share emotions, experience, and activities with other persons." So there are two operands: an *intention-reading capacity* and a *sharing drive*. The sharing drive is the primitive that matters for the algebra.

**Operators / equations.** None; this is a comparative developmental programme. The 2007 abstract names the four transformations as operators in a loose sense: gaze following -> joint attention, social manipulation -> cooperative communication, group activity -> collaboration, social learning -> instructed learning. Each is "an individualist skill (apes) becomes a shared-intentional skill (human toddlers)".

**Theorems or derived predictions.** (a) Toddlers, unlike apes, point to share attention rather than only to request. (b) They help spontaneously (Warneken & Tomasello: 18-month-olds help an adult with an out-of-reach object without reward). (c) They engage in collaborative play with shared goals from about 14 to 18 months, and take roles.

**Empirical standing.** Blunt version: the descriptive human-ape comparison (pointing, collaboration) has held up in many labs. Warneken & Tomasello's helping finding has been replicated in the sense that the phenomenon recurs; **I have not checked** the later large-scale replication literature on infant prosociality or the "many labs" issues and I have not found and should not state conclusions on that here. The claim that apes lack the sharing motivation is more contested (ape cooperation studies). The claim that the sharing motive is *primary* rather than learned is a theoretical interpretation, not an experimental result.

**Operand/operator translation.** A **sharing drive** is a good candidate primitive that belongs to the dyad, not the individual: it is satisfied only by a partner's matching state (shared attention, shared emotion). That makes it a relational drive: the algebra needs a drive whose satisfaction function takes *two* agents' states. Zurich's detectors do not have this property. Joint attention is the ternary operator again.

---

## 7. White (1959): effectance and mastery motivation

**Citation.** White, R. W. (1959). Motivation reconsidered: The concept of competence. *Psychological Review*, 66(5), 297-333. DOI 10.1037/h0040934 (Crossref-confirmed). Not read. `[from abstract/standard account]`.

**Their vocabulary.** Competence; effectance motivation (the motive behind exploration, manipulation, play and other activity directed at producing effects on the environment; paraphrase of the standard account of White 1959, Psychological Review 66(5), 297-333, wording not verified against the paper); feeling of efficacy; reality-based drive; ego psychology; critique of drive-reduction.

**Drives/operands.** *Effectance*: an intrinsic drive to have an effect on the environment, satisfied by producing effects, not by reducing tension. Its reward is the feeling of efficacy.

**Operators / equations.** None. White's argument is that drive-reduction (Hull, Freud) cannot explain play and exploration, so a second kind of motive is needed whose satisfaction is *increase*, not reduction. See 16 for the formal drive models that White was arguing against.

**Empirical standing.** Conceptually influential, no direct test; later work in intrinsic motivation (Deci, Ryan, and the computational "competence progress" models in 19) is the descendant. Mastery motivation measurement in infants (Morgan, Harmon, MacTurk and others) is a field; **not covered here**.

**Operand/operator translation.** Effectance gives a drive whose controlled variable is *contingency between action and outcome*. Notably the Zurich model's autonomy claim C ("a need for feeling competent and being respected by others", `[read]`) is the same construct fused with rank: C is White's competence plus social standing in one scalar. This is a place where the Zurich model is under-differentiated and the algebra might separate the two.

---

## 8. Social referencing: fear transmission as an operator

**Citations.**
- Sorce, J. F., Emde, R. N., Campos, J. J., & Klinnert, M. D. (1985). Maternal emotional signaling: Its effect on the visual cliff behavior of 1-year-olds. *Developmental Psychology*, 21(1), 195-200. DOI 10.1037/0012-1649.21.1.195 (Crossref-confirmed). Not read (primary not obtainable in validation either); figures from Karasik, Tamis-LeMonda & Adolph (2016), "Decisions at the brink: Locomotor experience affects infants' use of social information on an adjustable drop-off", *Frontiers in Psychology* 7:797, DOI 10.3389/fpsyg.2016.00797 **[read in validation, the passages on Sorce et al.]**.
- Klinnert, M. D., Campos, J. J., Sorce, J. F., Emde, R. N., & Svejda, M. (1983). Emotions as behavior regulators: Social referencing in infancy. In Plutchik & Kellerman (Eds.), *Emotion: Theory, Research, and Experience, Vol. 2: Emotions in Early Development*. Academic Press. DOI 10.1016/b978-0-12-558702-0.50009-1 (Crossref-confirmed; this is the Crossref entry). Not read.
- Kretch, K. S., & Adolph, K. E. (2013). Cliff or step? Posture-specific learning at the edge of a drop-off. *Child Development*, 84(1), 226-240. DOI 10.1111/j.1467-8624.2012.01842.x (Crossref-confirmed in validation). Not read; it is the source Karasik et al. cite for 30 cm being "risky for most infants, not ambiguous". The critique of Sorce et al. is Karasik et al.'s, not Kretch & Adolph's.

**Their vocabulary.** Social referencing; emotional signalling; ambiguity; visual cliff; joy, fear and neutral facial expressions; "behavior regulators".

**Drives/operands.** Infant state: uncertainty about a novel/ambiguous stimulus (an arousal that, in Bischof's terms, is a), plus the mother's displayed emotion as a *signal* that sets the infant's approach/avoid decision.

**Operators / equations.** A single operator, informally: **transmit(emotion expression, from caregiver to infant) -> infant's approach/avoid bias, conditional on infant ambiguity.** No equation.

**Theorems or derived predictions / findings.** From Karasik et al. (2016), quoting Sorce et al.: 12-month-olds facing a single 30 cm apparent drop-off (safety glass) crossed in 74% of cases when the mother posed a happy face and none crossed when she posed fear; in the fear condition 11 of 17 infants (65%) moved onto the brink and retreated. Karasik et al. also note a 40% attrition rate. The paper's other conditions (interest, anger, sadness) circulate in teaching material with crossing rates (73%, 11%, 33%) that could not be traced to a citable source and are **not** stated here as findings.

**Empirical standing.** Blunt: the direction (infants modulate approach to ambiguous objects using caregivers' emotional expression) is replicated many times in the social-referencing literature, using objects rather than cliffs. The *visual-cliff* version is weaker: Karasik, Tamis-LeMonda & Adolph (2016) argue the single 30 cm drop was risky rather than ambiguous for most infants (citing Kretch & Adolph 2013), that a single trial and static posed expressions limit interpretation, and that safety glass hid which partial crossers would have fallen. Their own adjustable drop-off study finds use of social information depends on locomotor experience and drop-off height. No effect size has been verified here. Treat the percentages as unverified.

**Operand/operator translation.** The cleanest candidate for a **fear-transmission operator**: a signal from agent j to agent i that shifts i's arousal set or the sign of i's activation A_a. In the Zurich frame, the mother's fearful face would change the *effective F* (familiarity of the object, via a lower-trust reading) or raise R, or directly add to the infant's arousal term; the model has no signal channel to represent this, so the operator must be added. This is the nearest thing in this cluster to a transmission law between agents, and it is stated only qualitatively. Link to group-level contagion models in 18.

---

## 9. Panksepp: separation distress, PANIC/GRIEF (cross-reference only)

**Citations.** Panksepp, J., Nelson, E., & Bekkedal, M. (1997). Brain systems for the mediation of social separation-distress and social-reward. *Ann. N.Y. Acad. Sci.*, 807, 78-100. DOI 10.1111/j.1749-6632.1997.tb51914.x (Crossref-confirmed). Panksepp, J., Siviy, S., & Normansell, L. (1985). Brain opioids and social emotions. In Reite & Field (Eds.), *The Psychobiology of Attachment and Separation*. Academic Press. DOI 10.1016/b978-0-12-586780-1.50006-9 (Crossref-confirmed). Not read here.

**Position.** Panksepp's PANIC/GRIEF is covered in 15 and 22; here only the developmental point: separation distress calls (young mammals vocalising on separation, reduced by opioid agonists) are the evolutionary base on which Bowlby's protest phase sits. The claim that attachment has an opioid substrate is from this line; it is cited as `[from abstract/standard account]` and not examined here. Go to 22 for the neural detail and its replication standing.

**Operand/operator translation.** PANIC/GRIEF supplies the *distress signal* operator: an unmet security setpoint (A_s above threshold in the Zurich notation) emits a signal that others can detect, and it is reduced by contact. That fits Bischof's A_s = D - s with an output channel.

---

## 10. Kidd: the development of curiosity, the "Goldilocks effect"

**Citations.**
- **Kidd, C., Piantadosi, S. T., & Aslin, R. N. (2012).** The Goldilocks effect: Human infants allocate attention to visual sequences that are neither too simple nor too complex. *PLoS ONE*, 7(5), e36399. DOI 10.1371/journal.pone.0036399 (Crossref-confirmed). **[read, article page]**
- Kidd, C., Piantadosi, S. T., & Aslin, R. N. (2014). The Goldilocks effect in infant auditory attention. *Child Development*, 85(5), 1795-1804. DOI 10.1111/cdev.12263 (Crossref-confirmed, including volume and pages). `[from PubMed abstract]`: 7- to 8-month-olds selectively attend to non-social auditory sequences that are intermediately predictable/complex under sound-to-sound transitional statistics; the authors present it as evidence for a domain-general principle across modalities. No peak value in the abstract.
- Kidd, C., & Hayden, B. Y. (2015). The psychology and neuroscience of curiosity. *Neuron*, 88(3), 449-460. DOI 10.1016/j.neuron.2015.09.010 (Crossref-confirmed). Not read here; see 17.

**Their vocabulary.** Ideal learner; surprisal (negative log probability of the next event under the learner's current model, in bits); rate of information absorption; look-away; Markov Dirichlet-multinomial (MDM) model; complexity.

**Drives/operands `[read]`.** An *information-rate* preference. 7- to 8-month-old infants (experiment 1: 44 tested, 42 analysed, mean age 7.9 months, one box revealing or not revealing an object; experiment 2: 30 tested and analysed, mean 7.6 months, three boxes each hiding a different object) watched sequences of events on screen; complexity was calculated as surprisal under a Markov Dirichlet-multinomial ideal-learner model with a uniform prior (alpha = 1).

**Operators / equations `[read]`.** The complexity measure: surprisal = -log2 P(next event | model so far), summed or averaged over the sequence. Look-away probability is then a **U-shaped function of complexity** (tested with Cox regression with a significant squared-complexity effect in both experiments). The authors' stated claim: "infants implicitly seek to maintain intermediate rates of information absorption."

**Theorems or derived predictions `[read]`.** Infants look away from events that are either very predictable or very surprising. The paper states a "Goldilocks" value of complexity "around 1.25 bits" for **Experiment 1 only** (read off the fitted curve, Fig. 3); no value is given for Experiment 2, and the number is specific to that stimulus set and model, not a constant. In Experiment 2, when transitional (order-dependent) and non-transitional complexity were entered together, only the transitional term was significant; the authors caution that the null for the non-transitional term is hard to interpret.

**Empirical standing.** Two experiments, small samples (42 and 30), eye-tracking, 7-8-month-olds; the effect was "small" in experiment 1 and considerably larger in experiment 2 (as reported on the article page). The 2014 auditory follow-up is described by the same authors as extending the effect. I have not found or checked any independent replication; **unconfirmed**. Note: the original design and the interpretation as "curiosity" is the authors'; look-away can also reflect fatigue or satiation.

**Operand/operator translation.** The Goldilocks result is a *measured* version of what Berlyne's inverted-U and Bischof's arousal homeostat predict: an optimal arousal level E (enterprise) with fear/avoidance above it and boredom/approach below it. In the algebra, curiosity is a **U-shaped (or signed-error) response of attention to surprisal, with a setpoint** that varies by individual and age. Bischof's E and Kidd's 1.25 bits are arguably the same concept at different levels (distance in space vs. information in a sequence); the Zurich model never leaves the spatial case. A bridge: measure a(x) as surprisal rate and keep E - a as the signed drive. This mapping is an interpretation, not a result in any source, but it has a foothold in the chapter itself: Gubler & Bischof define the familiarity detector information-theoretically, its output rising with the object's redundancy, "inversely to the object's entropy (or 'collativity' in the sense of Berlyne, 1960)" `[read]`. So 1 - F, the arousal-driving novelty, is already an entropy-like quantity in the original.

---

## 11. Play development (limited coverage)

**Citation.** Pellegrini, A. D., & Smith, P. K. (1998). Physical activity play: The nature and function of a neglected aspect of play. *Child Development*, 69(3), 577-598. DOI 10.1111/j.1467-8624.1998.tb06226.x (Crossref-confirmed). Not read; the Crossref listing also shows a companion "Physical Activity Play: Consensus and Debate" (DOI 10.1111/j.1467-8624.1998.tb06231.x).

**Status.** I only identified this source and did not read it, nor do I have a primary source for the ontogeny of play in the sense of Piaget, Parten, or the self-handicapping and role-reversal accounts of Bekoff and Byers. `[from abstract/standard account]` only. The structural point that I can state without a source: rough-and-tumble play is a **dyadic operator with self-handicapping**: partners deliberately lower their strength, which keeps the interaction going; this is a regulation of arousal across two agents (cf. Zurich a and E), and the ethological account is in 31. A proper play-development treatment is a gap in this file.

---

## 12. Harlow: contact comfort

**Citations.** Harlow, H. F. (1958). The nature of love. *American Psychologist*, 13(12), 673-685. DOI 10.1037/h0047884 (Crossref-confirmed). Harlow, H. F., & Zimmermann, R. R. (1959). Affectional responses in the infant monkey. *Science*, 130(3373), 421-432. DOI 10.1126/science.130.3373.421 (Crossref-confirmed; the Crossref title reads "Affectional Response in the Infant Monkey"). Neither was read. `[from abstract/standard account]`.

**Their vocabulary.** Contact comfort; surrogate mothers (wire and cloth); the infant's "affectional" response; the cloth surrogate as a source of security and a base from which to explore a novel object. (Note: "secure base" as a term is Ainsworth's, later; it is not Harlow's coinage, though his open-field and fear tests are routinely described with it.)

**Drives/operands.** Contact comfort is an *independent* drive: infant monkeys raised with both a lactating wire surrogate and a non-lactating cloth surrogate spent most of their time on the cloth one, regardless of which gave milk. In Harlow's reading, this refuted the secondary-drive (cupboard-love) account. The cloth surrogate also served as a base: a frightened infant ran to cloth and then explored.

**Operators / equations.** None. Qualitatively: fear (a novel object) -> contact seeking -> reduction of fear -> exploration. This is exactly the compound system of section 3 acted out.

**Empirical standing.** Contact comfort over food is a robust observation in Harlow's lab (the wire-vs-cloth time data are in both the 1958 address and Harlow & Zimmermann 1959); "repeated in other primates" is a standard-account claim with no specific source checked here. The study is also a long-standing ethical case (maltreated animals, isolate rearing), and some of Harlow's design (small groups, no formal statistics) would not meet current standards. The empirical claim that *contact* trumps *feeding* for attachment is not seriously contested; the secondary-drive theory it refuted is dead. No quantitative law.

**Operand/operator translation.** Evidence that *security* (Bischof's s) has an input channel, contact (tactile), that is independent of the nutritive drive. In the algebra's terms: two different drives with different satisfiers, which must not be collapsed into one hunger-like quantity. It also supports using a **proximity-like variable** for security (contact is the limit of H(x) as x -> 0).

---

## What exists vs. what does not

**Exists.**
- A **complete, explicit, simulated control model of attachment, fear and exploration** (Gubler & Bischof 1991; Bischof 1975): two coupled homeostats with setpoints D and E, products of a familiarity and a potency term, a pool (integrating) refinement that yields the observed oscillation, and a slow acclimatization rule that changes setpoints. Read at source.
- A verbal control-systems theory (Bowlby) with robust empirical backing for its qualitative claims.
- A strong descriptive literature on dyadic regulation in infancy (Tronick) with a robust average still-face effect, and a careful comparative developmental programme on sharing (Tomasello).
- A U-shaped curiosity result with an ideal-learner information measure (Kidd), a clean quantitative bridge to Bayesian surprisal.
- Evidence that stability of attachment security is moderate (Fraley 2002; Pinquart et al. 2013, r = .39; both read at abstract level).
- Two small parameter fits of the Zurich pool model, quail (Gubler 1989) and 15 toddlers (Friedländer 1987), known only through the 1991 chapter.

**Does not exist (in what I found).**
- **A group version of the Zurich model**, or any multi-agent result for it. The authors defer it explicitly.
- Any **numerical** model of Bowlby's three-system balance outside Bischof.
- A **signal channel** (social referencing, fear transmission) in any of the formal models; the transmission operator is only verbal.
- **Equations for the Mutual Regulation Model.** The mismatch/repair cycle has no formal statement in what I found.
- A treatment of **sharing drive** as a formal quantity with a two-agent satisfaction function.
- *Published*, replicated human behavioural tests of the Zurich dynamics. (Corrected in validation: unpublished toddler fits exist, Friedländer 1987 and Diener 1982, reported in the 1991 chapter; nothing peer-reviewed or independent was found.)
- A reconciliation between the **individual-difference** view (attachment classification as a trait-like regime) and the **dynamic** view (setpoints that adapt): Bischof's acclimatization rule is exactly this reconciliation, but nobody appears to have tested it.

## Unconfirmed

- All effect sizes of the Mesman et al. (2009) meta-analysis: not retrieved (publisher 403; abstract elided in Semantic Scholar and Crossref; no open copy found in validation). Only the qualitative pattern is supported, by secondary sources.
- Pinquart et al. (2013): overall r = .39 now confirmed from the abstract; the claim "very high after age 6" is a secondary paraphrase not in the abstract, and age-band coefficients were not seen.
- van IJzendoorn & Kroonenberg (1988) A/B/C percentages and the within- vs. between-culture variance ratio: from memory; abstract not retrieved in validation.
- The 1985 Sorce et al. study's full design and statistics: the 74%/0% figures come from Karasik et al. (2016), not the primary; the interest, anger and sadness conditions were not seen in any citable source.
- Whether Quirin et al. (2023) contains equations or simulations (abstract mentions none).
- Gubler & Bischof (1991): the OCR mangled the hyperbola form (eq. 1) and the inequality signs in (16a)/(16b) (both print "q < q_lim"; the prose fixes the semantics); eq. (8) is settled as products.
- Friedländer (1987), Diener (1982), Gubler (1989): unpublished Zurich theses, seen only through the chapter.
- Independent replication of Kidd et al. (2012) and of Warneken & Tomasello (2006).
- Tronick & Cohn (1989) "coordinated about a third / 30% of the time": from memory, not checked.
- "Graham et al. 2018" (cited as a still-face secondary source): no full reference was given and it was not identified in validation.
- Trevarthen (1979), Trevarthen & Hubley (1978), Gianino & Tronick (1988), Main & Solomon (1990), Bowlby (1969) are real and standard but have no DOI found; they were not read.
- Pellegrini & Smith (1998) content; Harlow (1958, 1959) content: not read.

## Missing important work (identified in validation, none read)

- **Formal and computational attachment after Bowlby.** Petters, D., & Waters, E. (2015). Modelling emotional attachment: An integrative framework for architectures and scenarios. *IJCNN 2015*, 1-8, DOI 10.1109/ijcnn.2015.7280431; Petters, D., & Beaudoin, L. (2017). Attachment modelling: From observations to scenarios to designs. In *Springer Series in Bio-/Neuroinformatics*, 227-271, DOI 10.1007/978-3-319-49959-8_9 (both Crossref-confirmed). Agent-based simulations of secure-base and Strange-Situation behaviour; the nearest successor to Bischof's programme.
- **Bretherton, I. (1985).** Attachment theory: Retrospect and prospect. *Monographs of the SRCD*, 50(1-2), 3-35, DOI 10.2307/3333824 (Crossref-confirmed). The standard control-systems reading of Bowlby, cited by Gubler & Bischof; also Waters & Deane (1982), cited there (book chapter, no DOI).
- **Mahler, Pine & Bergman (1975)**, *The Psychological Birth of the Human Infant* (Basic Books). Origin of "emotional refueling", the behaviour the pool model was built to reproduce; credit the phenomenon to them, the mechanism to Gubler & Bischof.
- **Berlyne, D. E. (1960)**, *Conflict, Arousal and Curiosity* (McGraw-Hill). Source of "collativity", which Bischof uses to define familiarity; the curiosity side of the Zurich model descends from it (cross-ref 17).
- **Contingency detection.** Gergely, G., & Watson, J. S. (1999), "Early socio-emotional development: Contingency perception and the social-biofeedback model", in Rochat (Ed.), *Early Social Cognition* (Crossref lists the 2014 Psychology Press reissue, DOI 10.4324/9781410604194-12); Gergely (2004), *Social Development* 13, 468-478, DOI 10.1111/j.1467-9507.2004.00277.x. The nearest formal account of what the still-face removes.
- **Play.** Panksepp, J., & Burgdorf, J. (2000). 50-kHz chirping (laughter?) in response to conditioned and unconditioned tickle-induced reward in rats. *Behavioural Brain Research*, 115, 25-38, DOI 10.1016/s0166-4328(00)00238-2 (Crossref-confirmed). Pellis, S. M., & Pellis, V. C. (2009), *The Playful Brain* (Oneworld; book, no DOI checked); Pellis, Pellis, Ham & Stark (2023), Play fighting and the development of the social brain: The rat's tale, *Neurosci. Biobehav. Rev.* 145, 105037, DOI 10.1016/j.neubiorev.2023.105037 (Crossref-confirmed). Section 11 remains a stub without these.

## Validation log (2026-10-29)

DOIs were re-resolved against the Crossref API for every work that carries one; authors, year, journal, volume and pages matched unless noted.

- Bowlby 1969/1973/1980 (books) — ✓ standard; not read.
- Bretherton 1992, Dev. Psych. 28, 759-775 — ✓
- Bowlby 1982, Am. J. Orthopsychiatry — ✓
- Ainsworth & Bell 1970 — ✓
- Ainsworth, Blehar, Waters & Wall 1978 (book) — ✎ corrected: episode description (not eight 3-minute episodes).
- Main & Solomon 1990 (chapter) — ✓ standard; no DOI.
- van IJzendoorn, Schuengel & Bakermans-Kranenburg 1999 — ✎ 15% figure confirmed from abstract and the "from memory" tag removed; rate in risk groups restated as the abstract's "twice or even three times".
- van IJzendoorn & Kroonenberg 1988 — ✓ citation; ? content numbers (abstract not retrieved).
- De Wolff & van IJzendoorn 1997 — ✎ r = .24 confirmed and tied to its 21-study subset (66 studies total).
- Bakermans-Kranenburg, van IJzendoorn & Juffer 2003 — ✎ d = .33 / .20 confirmed (search snippet of abstract).
- Groh et al. 2017 — ✓
- Fraley 2002 — ✓
- Pinquart, Feußner & Ahnert 2013 — ✎ r = .39 confirmed from PubMed abstract, with n, intervals and moderators; "very high after 6" marked as not in the abstract.
- Waters et al. 2000 — ✎ 72%, kappa .44, life-events figures confirmed from abstract.
- Gubler & Bischof 1991 — ✎ re-read in full: equations (1)-(16) and variable names correct; eq. (8) confirmed as products; "fear and curiosity are two signs of A_a" confirmed as the authors' own wording; corrected the chapter title (published title is "A Systems Theory Perspective"), pages (35-66), the familiarity-asymmetry parenthetical (mother's alienness is 0.1, not 0.9), and, most consequentially, the claim that the chapter has no human validation: it reports Friedländer's (1987) fit to 15 toddlers (mean quality 0.7, out-of-sample prediction) and Gubler's (1989) quail fit with four model modifications.
- Bischof 1975 — ✓ (credited as the originator of the approach, per the chapter).
- Bischof 1985 (book) — ✓ as cited in chapter; full subtitle added.
- Quirin et al. 2023 — ✎ Crossref-confirmed; abstract checked, mentions no equations or simulation.
- Schönbrodt, Unkelbach & Spinath 2009 — ✎ Crossref does resolve 10.1027/1015-5759.25.3.141; the "only an OSF preprint" note was wrong.
- Tronick et al. 1978 — ✎ resolved: J. AACP 17(1), 1-13 is the article; the Pediatrics 62(3):403 record is a one-page abstract item.
- Tronick 1989 — ✓
- Gianino & Tronick 1988 (chapter) — ✓ standard; no DOI. Gianino, Plimpton & Tronick 1986 — ✓
- Tronick & Cohn 1989 — ✓ citation; ? "about 30% coordinated".
- Cohn & Tronick 1988 — ✓
- Mesman, van IJzendoorn & Bakermans-Kranenburg 2009 — ✓ citation; ? effect sizes (no access).
- Li et al. 2019 — ✎ full authors, volume and pages added.
- Graham et al. 2018 — ? not identifiable from the reference given.
- Beebe, Lachmann & Jaffe 1997; Beebe & Lachmann 1988 — ✎ authors, titles and venues added; malformed DOI (`10.1037//`) fixed.
- Trevarthen 1979; Trevarthen & Hubley 1978 (chapters) — ✓ standard; no DOI. Trevarthen 2012 — ✓. Reddy 2008 — ✓
- Tomasello et al. 2005 — ✓. Tomasello & Carpenter 2007 — ✓ (online 2006). Warneken & Tomasello 2006 — ✓. Tomasello, Carpenter & Liszkowski 2007 — ✓. Moll & Tomasello 2007 — ✓
- White 1959 — ✓ (not read; characterisation is the standard account).
- Sorce, Emde, Campos & Klinnert 1985 — ✎ citation ✓; the unnamed "Frontiers 2016 article" identified as Karasik, Tamis-LeMonda & Adolph 2016 and read; 74%/0% confirmed only as their report of the primary; added the 11/17 brink-and-retreat figure and the 40% attrition; the critique re-credited to Karasik et al. (Kretch & Adolph supply the 30 cm risk point).
- Kretch & Adolph 2013 — ✎ volume, pages and DOI added (Crossref-confirmed).
- Klinnert et al. 1983 — ✓
- Panksepp, Nelson & Bekkedal 1997; Panksepp, Siviy & Normansell 1985 — ✓
- Kidd, Piantadosi & Aslin 2012 — ✎ confirmed U-shape, Cox regression with quadratic term, sample sizes; "around 1.25 bits" confirmed but restricted to Experiment 1 only; Experiment 2 model comparison restated accurately (joint entry, only transitional term significant).
- Kidd, Piantadosi & Aslin 2014 — ✎ volume/pages confirmed (not from memory); abstract summarised.
- Kidd & Hayden 2015 — ✓
- Pellegrini & Smith 1998 (both items) — ✓
- Harlow 1958; Harlow & Zimmermann 1959 — ✓ citations; ✎ "secure base" removed from Harlow's vocabulary (Ainsworth's term); "repeated in other primates" flagged as unsourced.
- Nothing was found to be fabricated; no entries removed.

**Verdict.** The survey is reliable on bibliography: every DOI resolves to the work claimed, and no citation is invented. Its one source read at source, Gubler & Bischof 1991, is transcribed accurately at the level of equations and variable names, but the survey stopped reading before the model-estimation section and so understated the model's empirical contact, which was the most consequential error. Secondary numbers were mostly right where checkable (Pinquart .39, Waters 72%, De Wolff .24, 15% disorganisation, Kidd 1.25 bits) but were stated with less precision about scope than the sources warrant; still-face effect sizes and the full Sorce design remain unverified.

## Licences of quoted and transcribed material (2026-10-29/30 audit)

Facts, numbers and citations are free to reuse; the entries below record what is quoted, transcribed or taken from a dataset.

- **Gubler & Bischof (1991), "A systems theory perspective", in Lamb & Keller (Eds.), Lawrence Erlbaum.** Licence: publisher copyright (Erlbaum); the open-access scan at the Munich repository has no licence recorded here, so not determined; publisher copyright presumed. Use: restated equations (1)-(16) in the survey's own notation, a variable vocabulary list (about 21 terms, kept as a description of the model's variables, flagged "check" in the audit), and a few short attributed quotations ("runs counter to a widespread notion", "the stranger is more familiar than the mother is alien", "inversely to the object's entropy (or 'collativity' ...)" and similar, each under 60 words). Audit note: the line-87 sentence "fear and curiosity are the two signs of one error term" is the survey's wording, not the chapter's (the chapter says "two signs of A_a", line 339); left unchanged per the audit's "check" verdict, to be fixed by either quoting exactly or removing the marks.
- **Kidd, Piantadosi & Aslin (2012), PLoS ONE 7(5), e36399.** Licence: CC BY (PLoS open access). Use: short quotation ("infants implicitly seek to maintain intermediate rates of information absorption") and restated results (sample sizes, 1.25 bits).
- **Karasik, Tamis-LeMonda & Adolph (2016), Frontiers in Psychology 7:797.** Licence: CC BY (Frontiers open access). Use: reported figures from Sorce et al. (74%, 0%, 11 of 17, 40% attrition) restated as numbers with citation. The untraceable teaching-material crossing rates (73%, 11%, 33%) are mentioned but not stated as findings; no source, licence unknown (audit verdict "check").
- **Pinquart, Feussner & Ahnert (2013), Attachment & Human Development (Taylor & Francis); Waters et al. (2000), Child Development (Wiley); Fraley (2002), Pers. Soc. Psychol. Rev. (Sage); van IJzendoorn, Schuengel & Bakermans-Kranenburg (1999), Dev. Psychopathol. (Cambridge UP); De Wolff & van IJzendoorn (1997); Bakermans-Kranenburg et al. (2003); Groh et al. (2017); Madigan et al. (2024).** Licence: not determined; publisher copyright presumed (paywalled journals; PubMed/Crossref abstracts are public). Use: numbers and findings restated from abstracts with citation, plus short quoted phrases ("a medium-sized stability", "about 15%", "moderately stable ..." under 60 words). Audit note: the stability paragraph is dense abstract-derived content; a rewrite in fully independent wording is still to do ("check").
- **Tronick & Cohn (1989), Child Development.** Publisher copyright (Wiley), not determined. Use: an unverified "about a third / about 30%" figure from memory; the quotation marks around it are the survey's own paraphrase, not a quotation (audit "check"); treat it as an unverified report from that paper.
- **Tomasello et al. (2005), BBS; Tomasello & Carpenter (2007), Dev. Sci.** Publisher copyright (Cambridge UP; Wiley), not determined. Use: short quoted phrases from the abstracts (under 20 words each), attributed above.
- **White (1959), Psychological Review (APA).** Publisher copyright, not determined. Use: description only, in the survey's paraphrase of the standard account; no longer quoted.
- **Ainsworth et al. (1978); Strange Situation procedure and Bowlby standard account (sections 1-2).** Background knowledge written in the survey's own words; no source text reproduced. Audit asked to confirm it was not derived from Wikipedia: no Wikipedia source is cited, and none is recorded; if any phrasing came from Wikipedia it would be CC BY-SA 4.0 and must be attributed. Not determined.
- **Crossref API (DOI metadata).** Facts (titles, authors, years, DOIs); bibliographic metadata is not copyrightable and Crossref asserts it is freely reusable. Use: dataset citation.
- **All other citations (Bowlby, Trevarthen, Harlow, Panksepp, Beebe, Petters and others).** Bibliographic references and short descriptions only; no text reproduced.
