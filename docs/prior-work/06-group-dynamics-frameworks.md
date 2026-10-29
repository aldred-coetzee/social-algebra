# Prior work 06: group dynamics and interpersonal frameworks

Date: 2026-10-29. Cluster: psychology, psychotherapy, microsociology, ethology.

## Summary

Nearly every framework here names a fixed set of moves people make on one
another, and almost none is an algebra. Three exceptions carry real
structure:

1. **Interdependence theory** (Thibaut & Kelley; Kelley et al.). Outcome
   matrices with a *transformation* from the given matrix to the effective
   matrix. Closest thing here to operators acting on a state.
2. **Dominance-hierarchy models** (Landau, Chase). Dyadic win/loss relations
   as a tournament graph, with an explicit dynamic (winner/loser effects,
   triad formation sequences). Real mathematics, but one operand type and
   essentially one operator (a dyadic contest).
3. **Structural balance** (Heider; Cartwright & Harary). Signed graphs with
   a theorem, but it is a state constraint, not a set of moves.

Everything else is a typology (Belbin, French & Raven, Karpman's roles,
Berne's ego states, Bion, Tuckman), a descriptive grammar (Berne's
transactions, Sacks et al., Goffman, Harre/positioning), or a verbal
process theory (Lewin, Girard, Collins, Tajfel/Turner). (Validation note:
Berne is split because his *transactions* come with explicit continuation
rules, which is a grammar, not just a list; Karpman's triangle has
transitions but no rules for when they fire, so "typology" is fair there.) Those are useful as a *catalogue of candidate operators*,
and as evidence about which moves matter.

**Provenance note.** Citations and DOIs below were checked against the
Crossref API (bibliographic record only). Claims about content come from
web-search summaries of secondary sources, not from reading the primary
texts. I did not read any paper in full. Where a result was thin I say so,
and it sits in "Unconfirmed" at the end. Treat "empirical standing" lines as
orientation, not review.

---

## 1. Kurt Lewin: topological/field psychology and group dynamics

- Lewin, K. (1936). *Principles of Topological Psychology*. McGraw-Hill.
  DOI 10.1037/10019-000 (APA PsycNET record, Crossref-confirmed).
- Lewin, K. (1947). Frontiers in group dynamics: concept, method and
  reality in social science; social equilibria and social change. *Human
  Relations*, 1(1), 5-41. DOI 10.1177/001872674700100103.
- Lewin, K. (1951). *Field Theory in Social Science: Selected Theoretical
  Papers* (D. Cartwright, ed.). Harper & Row. (Record confirmed via
  reviews: 10.2307/2087618, 10.1086/638467 (DOI of review/reprint, not of the book); the book itself has no DOI
  found.)

**Their vocabulary.** Life space, regions, boundaries, paths/locomotion,
valence, forces, barriers, field; in groups, "quasi-stationary
equilibria" held by driving and restraining forces, unfreezing/change.
(Schein's essay and encyclopedia entries confirm the equilibrium and
driving/restraining-force language; the primary text was not retrieved.)

**Operands (translated).** Persons as points moving in a structured
region-space; groups as fields containing persons and forces.

**Operators (translated).** Forces (vectors) with direction and strength
acting on a person's position; barriers; locomotion between regions;
adding a driving force or removing a restraining force. Lewin's topology
was borrowed from mathematical topology (regions, connectedness,
boundaries) and he explicitly aimed at vectors; it is formal in *intent*
and notation but was never developed into a calculus other people could
compute with. Treat as a diagram language with a physics metaphor. [from abstract/standard account]

**Predictive/control claim.** Behaviour is determined by the field at that
moment; change a group by shifting force balance, more effectively by
removing restraints than adding pushes (per Schein's summary: adding a
driving force tends to provoke a counterforce). Standing: enormously
influential as method (action research, change management); the specific
topological/vector machinery is not used predictively today.

**Limits.** Forces and valences are not measurable independently of the
behaviour they explain. No composition rules. The three-step "unfreeze,
move, refreeze" popularisation is a later simplification (one commercial
source attributes "refreezing" to Festinger; unverified).

**Relevance.** The origin of "group as a state with stabilising and
destabilising influences." Gives the *equilibrium/perturbation* framing:
operators as perturbations, groups as having restoring forces. Useful as a
prior on what an operator *should be able to express* (a push that is
absorbed vs one that shifts the equilibrium).

---

## 2. Moreno: sociometry

- Moreno, J. L. (1934). *Who Shall Survive? A New Approach to the Problem
  of Human Interrelations*. Nervous and Mental Disease Publishing Co.
  DOI 10.1037/10648-000 (APA PsycNET record of the 1934 book).

**Their vocabulary.** Sociometric test (each member names whom they would
choose for an activity), sociogram (picture of choices), isolates, stars,
mutual pairs, rejection.

**Operands (translated).** Persons as nodes; choices as directed, signed
edges.

**Operators (translated).** Essentially none. Sociometry is a *measurement
and representation* scheme: it fixes what a state looks like (a directed
signed graph), not what changes it. The sociogram is among the earliest
network drawings. Formality: a data model, no dynamics. [from abstract/standard account]

**Predictive/control claim.** The sociometric work was done at the New York
Training School for Girls, Hudson (with Helen Jennings; presented publicly
1933). The runaway story is told in several forms (the survey's source said
two isolated girls; the version usually retold is a wave of runaways
explained by their network position); neither was confirmed against *Who
Shall Survive?*, so it is under Unconfirmed. Used for regrouping
(classrooms, therapy). Standing: the foundation of social network
analysis; predictive claims were never rigorously tested in his own work.

**Limits.** Static snapshots of stated preference; no theory of how choices
change.

**Relevance.** Establishes the *state* half of an algebra: a graph with
signed directed edges is the oldest operand structure. Social-algebra
needs this plus the moves.

---

## 3. Bion: basic-assumption groups

- Bion, W. R. (1948-1951). Experiences in Groups I-VII. *Human Relations*.
  E.g. I: 1(3), 314-320, DOI 10.1177/001872674800100303; II: 1(4),
  487-496, DOI 10.1177/001872674800100406; IV: 2(4), 295-303, DOI
  10.1177/001872674900200401.
- Bion, W. R. (1961). *Experiences in Groups and Other Papers*. Tavistock.
  (Book edition cited by secondary sources; no DOI found.)

**Their vocabulary.** Work group vs basic-assumption group; three basic
assumptions: dependency, fight-flight, pairing. Later additions: oneness
(Turquet), "Me" (Bain et al.), and others.

**Operands (translated).** The group as a whole in one of a small number of
collective modes; a leader figure the mode attaches to.

**Operators (translated).** Mode switches (the group slides from one basic
assumption to another); the "valency" of individuals to be drawn into a
mode. Pure typology plus a clinical-theoretical narrative; no formal
structure. [from abstract/standard account]

**Predictive/control claim.** Groups predictably take on one of the three
emotional stances regardless of stated task, and these displace work.
Standing: clinically influential in Tavistock/group-relations tradition;
empirical support thin (secondary source notes dispute even whether modes
alternate or combine).

**Limits.** Interpretive, not falsifiable as stated; group-as-a-whole unit
is hard to translate to agents.

**Relevance.** A candidate *discrete state space for the group* (3-4 modes)
with transitions. Useful as a coarse model of group-level mode.

---

## 4. Tuckman: stages of group development

- Tuckman, B. W. (1965). Developmental sequence in small groups.
  *Psychological Bulletin*, 63(6), 384-399. DOI 10.1037/h0022100.
- Tuckman, B. W., & Jensen, M. A. C. (1977). Stages of small-group
  development revisited. *Group & Organization Studies*, 2(4), 419-427.
  DOI 10.1177/105960117700200404.

**Their vocabulary.** Forming, storming, norming, performing (1965);
adjourning added 1977. Each stage has an interpersonal ("group structure")
and a task-activity face.

**Operands (translated).** The group as a whole at a stage.

**Operators (translated).** A fixed linear sequence. No operators on
individuals; the only "move" is advancing a stage. [from abstract/standard account]

**Predictive/control claim.** Groups pass through the stages in order.
Standing: a literature review and synthesis (reportedly of roughly 50
studies, per secondary sources), narrow sample (therapy, T-groups,
laboratory groups); the model is widely taught; later evidence is that real
groups cycle, skip, or never settle. Do not treat as a law.

**Limits.** Descriptive stage model, not a mechanism.

**Relevance.** Low formal value; shows what a "group state machine" looks
like and why people reach for it. A model should be able to *generate*
stage-like behaviour, not assume it.

---

## 5. Belbin: team roles

- Belbin, R. M. (1981). *Management Teams: Why They Succeed or Fail*.
  Heinemann. (Reviews: 10.1111/j.1467-9310.1982.tb00500.x,
  10.2307/2581652; DOI of review/reprint, not of the book.)
- Evaluation: Aritzeta, A., Swailes, S., & Senior, B. (2007). Belbin's team
  role model: development, validity and applications for team building.
  *Journal of Management Studies*, 44(1), 96-118. DOI
  10.1111/j.1467-6486.2007.00666.x.

**Their vocabulary.** The 1981 book had **eight** roles: Chairman, Shaper,
Plant, Monitor-Evaluator, Company Worker, Resource Investigator, Team
Worker, Completer-Finisher. Later versions renamed Chairman to
Co-ordinator and Company Worker to Implementer, and added a ninth,
Specialist (date of addition not confirmed). The nine-role list is the
current commercial form, not the 1981 model.

**Operands.** Persons typed by preferred role profile.

**Operators.** None; roles are *dispositions*, not moves. The implied
operation is composition of a team from role types (balance rule). [from abstract/standard account]

**Predictive/control claim.** Balanced role mixes yield better teams.
Standing: the 2007 review (43 studies) finds adequate convergent validity
but weak discriminant validity for some scales; Fisher et al. (2001, cited
therein) found the model overparameterised and mappable onto the Big Five.
Commercially dominant, scientifically weak.

**Limits.** Self-report typology; roles are traits not interactions.

**Relevance.** Illustrates *operand typing* (a person's type as a label),
and the weakness of doing that without interaction rules. Low value as a
source of operators.

---

## 6. Berne: transactional analysis and "games"

- Berne, E. (1964). *Games People Play: The Psychology of Human
  Relationships*. Grove Press. (Contemporary review confirmed:
  10.1080/00207284.1965.11642867 (DOI of review/reprint, not of the book); I did not confirm publisher details
  from a primary record.)
- Berne, E. (1961). *Transactional Analysis in Psychotherapy*. Grove Press.
  (Not independently confirmed; ego-state theory is documented in
  10.4324/9780203753996-10 (DOI of review/reprint, not of the book: a later book chapter).)

**Their vocabulary.** Ego states Parent/Adult/Child; transaction (stimulus
and response between ego states); complementary, crossed and ulterior
transactions; games as series of ulterior transactions with a gimmick and a
predictable payoff; strokes; scripts.

**Operands (translated).** A person has three internal states; the operand
in an exchange is a (person, ego state) pair.

**Operators (translated).** The transaction is the closest thing in
psychotherapy to a typed operator: a directed move from one (person, ego
state) to another's. Classification rules: complementary (reply from the
addressed state back to the sender's addressing state) continues the
exchange; crossed breaks it; ulterior carries a hidden second message.
This is a *composition grammar* with a well-formedness rule ("lines of
transaction must be parallel to continue"), which is more than most of the
cluster. Berne states it as three rules of communication: (1) complementary
transactions can continue indefinitely; (2) a crossed transaction breaks
communication off, and one or both parties must shift ego state to restore
it; (3) the behavioural outcome of an ulterior transaction is decided at
the psychological, not the social, level. (Rule wording via secondary TA
teaching material; consistent with Berne 1964.) Games are named sequences of such moves (e.g. a stated number of
published named games). Formality: a diagrammatic notation (arrows between
three circles), not mathematics; no quantities. [from abstract/standard account]

**Predictive/control claim.** Crossed transactions end communication;
games repeat with predictable payoffs; intervene by changing the ego state
you respond from. Standing: used in therapy and training; weak experimental
validation, with ego states contested as constructs (a popular-press
retrospective notes its decline; not a research source).

**Limits.** Three-state personality model is a metaphor; games are
hand-recognised patterns from clinical anecdote.

**Relevance.** High as a model of *what a notation looks like*: states,
directed moves, a closure rule for what composes, and named recurring
chains. A good template for a "moves" vocabulary.

---

## 7. Karpman: the drama triangle

- Karpman, S. (1968). Fairy tales and script drama analysis.
  *Transactional Analysis Bulletin*, 7(26), 39-43. (Citation confirmed from
  the author's site and a 2019 follow-up; no independent database record
  found.)
- Karpman, S. (2019). Script drama analysis II. *International Journal of
  Transactional Analysis Research & Practice*, 10(1), 21-39. DOI
  10.29044/v10i1p21.

**Their vocabulary.** Persecutor, Rescuer, Victim; role switches; the
Drama Triangle, plus a Role Diagram and Location Diagram.

**Operands.** Persons occupying one of three roles in a triad.

**Operators.** The *switch* (a person moves to another corner, typically
after the others do) and the pairwise stances. Formality: a labelled
triangle with transitions; a three-state-per-person state machine in
effect, never axiomatised. [from abstract/standard account]

**Predictive/control claim.** Roles are unstable and switch predictably
(rescuer becomes persecutor); step out by adopting a non-corner role.
Standing: popular in therapy/coaching; won a TA award (1972); little formal
empirical testing found.

**Limits.** Applies to dysfunctional interaction only; no account of who
switches when.

**Relevance.** Small, memorable example of a role-triad with cyclic
transitions. Useful test case: can the algebra express a drama triangle as
a periodic orbit?

---

## 8. Girard: mimetic theory

- Girard, R. (1961; Eng. 1965/1976). *Deceit, Desire, and the Novel*.
  Johns Hopkins UP. DOI 10.56021/9780801802201 (Crossref, the 1976
  edition).
- Girard, R. (1972). *La Violence et le sacre*; Eng. (1977) *Violence and
  the Sacred*. (Not independently confirmed bibliographically.)
- Reconstruction: Livingston, P. (1992). *Models of Desire: Rene Girard
  and the Psychology of Mimesis*. Johns Hopkins UP. (Reviews confirmed:
  10.2307/1771634, 10.1017/S0012217300011252; DOI of review/reprint, not of the book.)

**Their vocabulary.** Mimetic desire (desire borrowed from a model),
triangular desire (subject, model, object), rivalry, contagion,
sacrificial crisis, scapegoat mechanism.

**Operands.** Subject, model, object (the triad); the community.

**Operators.** Imitation of desire; rivalry escalation (reciprocal
mimesis); scapegoating (collective redirection onto one victim).
Entirely verbal and literary-anthropological; secondary sources note he
never gave a systematic presentation, and that Livingston was the first
rigorous reconstruction. The structure (positive feedback in reciprocal
imitation, collapse into a single target) is easy to formalise as a
dynamical system but he did not. [from abstract/standard account]

**Predictive/control claim.** Mimetic rivalry spreads and resolves via
scapegoating; societies are held together by this mechanism. Standing:
influential in humanities; weak empirical test; some psychology work on
imitation of desire.

**Limits.** Universal sweeping claim from literature and myth; hard to
falsify.

**Relevance.** Offers one clean candidate operator, *imitate-desire*, with
positive feedback, and a collective-level operator, *scapegoat*, which
collapses a many-to-many conflict into many-to-one. Worth a sketch.

---

## 9. Thibaut & Kelley: interdependence theory

- Thibaut, J. W., & Kelley, H. H. (1959). *The Social Psychology of
  Groups*. Wiley. (Reprint DOI 10.4324/9781315135007; DOI of review/reprint, not of the book.)
- Kelley, H. H., & Thibaut, J. W. (1978). *Interpersonal Relations: A
  Theory of Interdependence*. Wiley. (Review records only: 10.2307/351281,
  10.1093/sw/25.3.245; DOI of review/reprint, not of the book.)
- Kelley, H. H., Holmes, J. G., Kerr, N. L., Reis, H. T., Rusbult, C. E.,
  & Van Lange, P. A. M. (2003). *An Atlas of Interpersonal Situations*.
  Cambridge UP. DOI 10.1017/CBO9780511499845 (print 2003, confirmed by the
  publisher's synopsis; Crossref's 2001 date is a placeholder for the
  online record). Catalogues 21 common situations.
- Van Lange, P. A. M. (1999). The pursuit of joint outcomes and equality in
  outcomes: an integrative model of social value orientation. *JPSP*,
  77(2), 337-349. DOI 10.1037/0022-3514.77.2.337. (Source for MinDiff.)
- Rusbult, C. E., & Van Lange, P. A. M. (2003). Interdependence,
  interaction, and relationships. *Annual Review of Psychology*, 54,
  351-375. DOI 10.1146/annurev.psych.54.101601.145059.

**Their vocabulary.** Outcome matrix (each person's payoff for each
combination of the two actors' behaviour options); given matrix vs
effective matrix; transformation of motivation (a motivated shift away from
immediate self-interested impulse).

**Matrix decomposition (validated).** Each person's outcomes in a 2x2
matrix decompose into three additive components: **actor control** (AC,
what my own choice does to my outcome), **partner control** (PC, what your
choice does to my outcome) and **joint control** (JC, the interaction term:
what our combination does to my outcome). These are the Atlas's names; in
Thibaut & Kelley (1959) and Kelley & Thibaut (1978) they were **reflexive
control**, **fate control** and **behaviour control** respectively. The
Atlas builds every 2x2 pattern from three base patterns: bilateral actor
control, mutual partner control, and corresponding or conflicting mutual
joint control. This is, in effect, a two-way ANOVA decomposition of the
payoff matrix (row effect, column effect, interaction), the same shape as
Kenny's SRM below. [from abstract/standard account]

**Six situation dimensions** (Rusbult & Van Lange 2003; the count is
confirmed by the abstract, the names from the verifier's knowledge of that
paper): level of dependence, mutuality of dependence, basis of dependence
(actor/partner/joint control), covariation of interests (correspondence,
from fully corresponding to fully conflicting), temporal structure, and
availability of information.

**Operands (translated).** Persons with behaviour options, and a *situation*
as a matrix of outcomes over joint behaviour.

**Operators (translated).** Two layers. (1) Behaviours select a cell of the
matrix. (2) **Transformations** map the given matrix to an effective matrix
(secondary sources: reweighting outcomes by concern for the partner's
welfare, long-term goals). This *is* a genuine operator structure: a
function from payoff matrices to payoff matrices parameterised by
disposition. It is a close cousin of game theory (a Van Lange/VU entry is
titled "bridging psychology and game theory yields interdependence
theory"), so formal machinery exists. **Named transformations
(validated):** MaxOwn (maximise own outcome; the given-matrix default),
MaxOther (maximise the partner's outcome; altruism), MaxJoint (maximise
the sum; cooperation), MinDiff (minimise the absolute difference;
equality) and MaxRel (maximise own minus partner's; competition). MaxOwn,
MaxOther, MaxJoint and MaxRel are used in Wieselquist et al. (1999, JPSP)
citing Kelley & Thibaut (1978); MinDiff is from the social-value-orientation
line (Van Lange 1999). The shorthand labels are the later literature's,
not necessarily Kelley & Thibaut's own. All but MinDiff are weighted linear
combinations of own and other outcomes (w_own, w_other), so they form a
one-parameter family (an angle in outcome space); MinDiff is not linear.
Kelley & Thibaut also describe *sequential* (temporal) transformations,
which act on sequences of choices rather than single cells. [from abstract/standard account]

**Predictive/control claim.** Behaviour in a situation is predicted from the
structure of the situation plus transformation dispositions; relationship
quality tracks the transformation. Standing: very strong in relationships
research (commitment, trust, accommodation); coherent and testable;
Atlas catalogues situation types.

**Limits.** Mostly dyadic; larger groups blow up combinatorially; payoffs
must be elicited; transformations are fitted per person.

**Relevance.** The single best-fitting precedent. Operands: persons plus
situations (matrices). Operators: choice (select a cell) and transformation
(rewrite the matrix). The social-algebra should either embed in this or
state exactly what it adds (group size, roles, positions, time).

---

## 10. Kenny: the Social Relations Model

- Kenny, D. A., & La Voie, L. (1984). The social relations model. In L.
  Berkowitz (Ed.), *Advances in Experimental Social Psychology*, vol. 18,
  pp. 141-182. DOI 10.1016/S0065-2601(08)60144-6.
- Kenny, D. A., & La Voie, L. (1985). Separating individual and group
  effects. *J. Personality and Social Psychology*, 48(2), 339-348. DOI
  10.1037/0022-3514.48.2.339.
- Warner, R. M., Kenny, D. A., & Stoto, M. (1979). A new round robin
  analysis of variance for social interaction data. *JPSP*, 37(10),
  1742-1757. DOI 10.1037/0022-3514.37.10.1742.

**Their vocabulary.** Actor effect, partner effect, relationship effect
(plus group effect), round-robin design, reciprocity.

**Operands.** Dyadic measurements between all pairs in a group.

**Operators.** None; a variance decomposition of an observed dyadic
variable into additive components: X_ij = m + a_i + b_j + g_ij (+ error),
with a_i the actor effect of i, b_j the partner effect of j, g_ij the
relationship effect unique to i toward j, and m the group mean (which
becomes a group effect when several groups are studied). Reciprocity is
read off two covariances: generalised (a_i with b_i) and dyadic (g_ij with
g_ji). Statistical model (ANOVA-family), fully formal, but a *measurement*
model. [from abstract/standard account]

**Predictive/control claim.** Tells you how much of A's behaviour toward B
is A's trait, B's evoking power, or the pair's unique fit, and how much is
reciprocated. Standing: solid, widely used.

**Limits.** Additive decomposition, no dynamics, no moves.

**Relevance.** Gives a clean parametrisation of *dyadic* quantities
(actor/partner/relationship terms); useful for calibrating operators from
data later, not for defining them.

---

## 11. French & Raven: bases of social power

- French, J. R. P., Jr., & Raven, B. (1959). The bases of social power. In
  D. Cartwright (Ed.), *Studies in Social Power* (pp. 150-167). Institute
  for Social Research, University of Michigan. (Chapter reprint record:
  10.2307/jj.12381759.38 (DOI of review/reprint, not of the book), a 1986 reprint in *Political Leadership*,
  pp. 300-318; the 1959 volume has no DOI found.)
- Measurement critique: Hinkin & Schriesheim (1989). 10.1037/0021-9010.74.4.561.

**Their vocabulary.** Five bases: reward, coercive, legitimate, referent,
expert; Raven added informational (1965). Power defined as potential
influence.

**Operands.** Agent, target, and the resource or relationship that gives
the agent leverage.

**Operators.** Influence attempts grounded in a base (offer reward, threaten
punishment, invoke authority, appeal to identification, cite expertise).
Typology of *sources of leverage*, not a formal system. [from abstract/standard account]

**Predictive/control claim.** Different bases produce different
durability/internalisation of compliance (referent and expert more
lasting). Standing: widely used; measurement has been a persistent
problem. Hinkin & Schriesheim (1989) built new scales because earlier
single-item measures were psychometrically weak; Raven and colleagues
later expanded the scheme to eleven bases (the Interpersonal Power
Inventory, 1998). (The original survey's claim that the 5-base and 11-base
scales "correlate weakly" had no source and has been removed.)

**Limits.** Categories overlap; says nothing on how power accumulates or is
lost.

**Relevance.** A ready operator-type list: influence moves keyed by what
backs them. Pair with interdependence theory (a base of power is a way to
alter another's matrix).

---

## 12. Goffman: frame analysis and face-work

- Goffman, E. (1955). On face-work: an analysis of ritual elements in
  social interaction. *Psychiatry*, 18(3), 213-231. DOI
  10.1080/00332747.1955.11023008.
- Goffman, E. (1974). *Frame Analysis: An Essay on the Organization of
  Experience*. Harper & Row. ix + 586 pp. (Bibliographic detail from a
  secondary citation; no DOI.)

**Their vocabulary.** Face, line, face-saving, avoidance and corrective
processes (1955). Primary frameworks, **keyings** (transformations that
re-pattern an already meaningful activity so participants see it as
something else, e.g. play-fighting), **fabrications** (deliberately
inducing a false belief about what is going on; benign or exploitative),
laminations of frames. Goffman names five basic keys: make-believe,
contests, ceremonials, technical redoings, regroundings. (The keying and
fabrication definitions match Goffman's own wording; the survey attributed
them to "Davis & Gamson 1975", which is two separate reviews of *Frame
Analysis* in *Contemporary Sociology* 4(6): Davis, pp. 599-603, DOI
10.2307/2064021; Gamson, pp. 603-607, DOI 10.2307/2064022; these are DOIs of reviews, not of the book.)

**Operands.** Activities / strips of interaction with a frame (a
meaning-assignment), and participants' face.

**Operators.** Keying and fabrication are named *transformations on
frames*, with stated structure (a keying can be re-keyed, so layers stack).
Face-work moves (avoidance, correction, repair) act on the status of faces.
Closest to Kelley & Thibaut's transformation in spirit: an operator that
changes the interpretation of the situation. Not formalised; the layering
looks algebraic (iterated keying) but is only described. [from abstract/standard account]

**Predictive/control claim.** Little prediction; analytic and descriptive.
Standing: a foundation for framing research in sociology and media studies.

**Limits.** Dense taxonomic prose; no procedure for deciding which frame
applies.

**Relevance.** Strongest source for *meta-level operators* (acting on the
frame, not the move): play, deceit, ritual, rehearsal. Needed if the
algebra is to express "this is a joke."

---

## 13. Conversation analysis: turn-taking and adjacency pairs

- Sacks, H., Schegloff, E. A., & Jefferson, G. (1974). A simplest
  systematics for the organization of turn-taking for conversation.
  *Language*, 50(4), 696-735. DOI 10.2307/412243.
- Schegloff, E. A., & Sacks, H. (1973). Opening up closings. *Semiotica*,
  8(4), 289-327. DOI 10.1515/semi.1973.8.4.289 (introduces the adjacency
  pair notion in its conversational-closing setting; per Schegloff's
  later letter).

**Their vocabulary.** Turn-constructional unit, transition-relevance place
(TRP), current-speaker-selects-next, self-selection, continuation,
adjacency pair (first pair part, second pair part: question-answer,
greeting-greeting).

**Operands.** Speakers and turns.

**Operators (translated).** Genuinely rule-based, and the most formal
interaction grammar in this cluster. At each TRP, an ordered rule set
applies: (a) current speaker selects next, otherwise (b) another party may
self-select (first starter gets the turn), otherwise (c) the current
speaker may, but need not, continue; and (rule 2) if (c) applies, the set
re-applies at the next TRP, recursively. First pair
parts create a conditional relevance for a matching second pair part.
This reads as a small production system, though stated in prose. [from abstract/standard account]

**Predictive/control claim.** Predicts the distribution of gaps/overlaps
and where turn transitions occur; deviations are accountable. Standing:
strongly supported cross-linguistically as an organisation (and
refined/contested in details); one of the most robust findings in
microsociology.

**Limits.** Scope is conversation; says nothing about content, motives or
power; turn-taking is a *local allocation* system.

**Relevance.** Evidence that fixed rule-sets for interaction *can* be
specified and tested. A candidate for the algebra's "who gets to act next"
scheduling layer, and the adjacency pair is a literal operator-with-
expected-response.

---

## 14. Positioning theory (Harre, van Langenhove, Davies)

- Davies, B., & Harre, R. (1990). Positioning: the discursive production of
  selves. *J. for the Theory of Social Behaviour*, 20(1), 43-63. DOI
  10.1111/j.1468-5914.1990.tb00174.x.
- Harre, R., & van Langenhove, L. (Eds.) (1999). *Positioning Theory: Moral
  Contexts of Intentional Action*. Blackwell. (Edition details from
  secondary sources; Wiley catalogue shows a typo.)
- Harre, R., & Moghaddam, F. (Eds.) (2003). *The Self and Others*. Praeger.
  DOI 10.5040/9798216187646.

**Their vocabulary.** Position (a cluster of short-term, disputable
rights, obligations and duties), speech act / social force, storyline;
the "positioning triangle."

**Operands.** Persons holding positions in a storyline.

**Operators.** Positioning acts: assigning or accepting/rejecting a
position (first-order), contesting it (second-order), and so on.
Descriptive; the triangle (position-act-storyline) is a conceptual
dependence structure, not a calculus. [from abstract/standard account]

**Predictive/control claim.** Little predictive; used as an analytic lens
(discourse analysis, public relations). Standing: qualitative and
interpretive.

**Limits.** Rights and duties are tacit and local; no enumeration of
position types.

**Relevance.** Directly relevant: "what you may do" as a function of
position gives operators *preconditions*. The idea of a position as a set
of permissions and obligations is exactly how a typed algebra would limit
operator application.

---

## 15. Collins: interaction ritual chains

- Collins, R. (2004). *Interaction Ritual Chains*. Princeton UP. DOI
  10.1515/9781400851744.

**Their vocabulary.** Interaction ritual, emotional energy, group
solidarity, symbols of membership, chains of encounters, market for
emotional energy. Ingredients (validated against several secondary
accounts; the model figure is Collins 2004, p. 48): group assembly (bodily
co-presence), barriers to outsiders, mutual focus of attention, shared
mood; the last two feed each other. Outcomes: group solidarity, emotional
energy in individuals, symbols of the relationship, standards of morality.

**Operands.** Situations (encounters) and the individuals' stock of
emotional energy and symbols.

**Operators.** An encounter is the unit operation; it produces or drains
emotional energy and charges symbols. Verbal theory; sociologists have
called it a "model" because outcomes are directional, but there is no
mathematics. [from abstract/standard account]

**Predictive/control claim.** Successful rituals raise energy and
solidarity; failed ones drain it; individuals gravitate to encounters that
maximise energy. Standing: influential, partially supported by studies of
ritual and emotion; contested in detail.

**Limits.** Energy is hard to measure.

**Relevance.** Offers a quantity that accumulates across encounters (a
resource with gain and loss per interaction), which an algebra could use as
a state variable; also links micro encounters to macro structure.

---

## 16. Ethology: dominance hierarchies (Landau, Chase)

- Landau, H. G. (1951). On dominance relations and the structure of animal
  societies: I. Effect of inherent characteristics. *Bulletin of
  Mathematical Biophysics*, 13, 1-19. DOI 10.1007/BF02478336 (Crossref,
  pp. 1-19). Part II: 13(4), 245-262, DOI 10.1007/BF02477920. Landau
  (1968) Models of social structure, 30, 215-224, DOI 10.1007/BF02476691.
- Chase, I. D. (1982). Dynamics of hierarchy formation: the sequential
  development of dominance relationships. *Behaviour*, 80, 218-239. DOI
  10.1163/156853982X00364. (The original jigsaw-puzzle model.)
- Chase, I. D. (1985). The sequential analysis of aggressive acts during
  hierarchy formation: an application of the 'jigsaw puzzle' approach.
  *Animal Behaviour*, 33, 86-100. DOI 10.1016/S0003-3472(85)80122-6.
- Chase, I. D., Bartolomeo, C., & Dugatkin, L. A. (1994). Aggressive
  interactions and inter-contest interval: how long do winners keep
  winning? *Animal Behaviour*, 48, 393-400. DOI 10.1006/anbe.1994.1253.
- Chase, I. D., Tovey, C., Spangler-Martin, D., & Manfredonia, M. (2002).
  Individual differences versus social dynamics in the formation of animal
  dominance hierarchies. *PNAS*, 99(8), 5744-5749. DOI
  10.1073/pnas.082104199.
- Chase, I. D., & Seitz, K. (2011). Self-structuring properties of
  dominance hierarchies. *Advances in Genetics*, 75, 51-81. DOI
  10.1016/B978-0-12-380858-5.00001-0.
(Entries for de Vries 1995, Chase 1974 and 1980, and Dugatkin 1997 were
dropped as unused by this entry.)

**Their vocabulary.** Dyadic dominance relation, tournament, transitive
(linear) hierarchy, Landau's h (linearity index; formula h = 12/(n^3 - n) *
sum (v_a - (n-1)/2)^2, v_a = number of animals a dominates; validated:
h ranges from 0 (every animal dominates equally many) to 1 (perfectly
linear), and h >= 0.9 is the conventional threshold for "strongly
linear"), winner and loser effects (a win raises, a loss lowers,
the chance of winning the next contest), triad dominance patterns.

**Operands.** Animals; ordered pairs with a dominance relation; the
tournament as a whole.

**Operators (translated).** A dyadic contest with a win/loss outcome that
sets the pair's relation (and, with winner/loser effects, updates each
animal's state). Chase's work classifies the *sequence of dyadic
interactions in triads* by whether they produce transitive or intransitive
outcomes. **Jigsaw-puzzle model (resolved).** Chase (1982, *Behaviour*;
the term is in the title of Chase 1985) treats a hierarchy as assembled
from triad pieces. Given a first contest A over B, the next contest
involving bystander C takes one of four forms: **double dominance** (A
attacks C), **double subordinance** (C attacks B), **pass-along** (B
attacks C) or **bystander attacks initiator** (C attacks A). The first two
guarantee a transitive triad; the last two can end either way. In 14
groups of four hens the two transitivity-guaranteeing sequences made up
77% of sequences (Chase 1985), and high proportions were later reported in
rhesus and Japanese macaques, cichlids and crayfish (per Chase et al.
2002). So linearity comes from the *order* in which contests happen, not
only from who would win. Genuinely formal: tournament graph theory plus
stochastic processes. Landau (1951, I) showed that inherent
characteristics alone produce linear hierarchies only when ability
differences are implausibly large, which is what opened the door to
social-dynamics explanations. [from abstract/standard account]

**Predictive/control claim.** Linear hierarchies form much faster than
random contests would allow, and the Chase 2002 PNAS finding (abstract
read via PMC122842): "although differences in attributes play a
significant part, we find that social interaction is necessary for high
proportions of groups with linear hierarchies." In its reassembly
experiment, only 27.3% of 22 cichlid groups reformed the identical
hierarchy after separation (above chance, far below what attributes alone
would predict).
Standing: strong empirically in fish, chickens, wasps; the winner-loser
literature is active (Lindquist & Chase 2009 data analysis; Kura, Broom,
Kandler 2016 game-theoretic model). Note Chase's own later position that
the standard individual-attribute approach has "significant deficiencies"
(Chase & Lindquist 2016, via search summary).

**Limits.** One relation type (dominance), one operator (a contest), no
content, and the human-group version is only gestured at.

**Relevance.** Best exemplar of *emergent structure from iterated simple
dyadic operators*, with a testable generative claim (structure is
self-organised, not just attribute-sorted). Directly usable: one operator
with state-updating (winner/loser effect) producing macro structure.

---

## 17. Tajfel & Turner: social identity and self-categorisation

- Tajfel, H., & Turner, J. C. (1979). An integrative theory of intergroup
  conflict. In W. G. Austin & S. Worchel (Eds.), *The Social Psychology of
  Intergroup Relations* (pp. 33-47). Brooks/Cole. (Later chapter versions
  in Crossref: 10.1093/oso/9780199269464.003.0005 and
  10.4324/9780203505984-16, titles slightly different; the 1979 chapter
  itself has no DOI found.)
- Turner, J. C., Hogg, M. A., Oakes, P. J., Reicher, S. D., & Wetherell,
  M. S. (1987). *Rediscovering the Social Group: A Self-Categorization
  Theory*. Blackwell. (Reviews confirmed: 10.2307/2073157,
  10.1086/229205; DOI of review/reprint, not of the book.)

**Their vocabulary.** Social categorisation, social identity, social
comparison, positive distinctiveness; minimal group paradigm; in SCT,
levels of self-categorisation (personal vs social identity), depersonal-
isation.

**Operands.** Persons as members of categories; the categories (in-group,
out-group).

**Operators.** Categorise, identify, compare; switch salience between
personal and group-level identity. Verbal theory plus experiment. SCT has
a "meta-contrast principle" that is quasi-formal (categories form to
maximise between-group relative to within-group difference), but I did not
confirm the exact statement. [from abstract/standard account]

**Predictive/control claim.** Mere categorisation produces in-group bias
even in minimal groups (Tajfel's Bristol studies, per secondary
summaries); change salience to change behaviour. Standing: among the most
replicated findings in social psychology.

**Limits.** Says what makes group boundaries bite, not how they are built
or move.

**Relevance.** Provides the operand *membership* and an operator that
changes salience of the category used. Needed for any model where
"us/them" matters.

---

## 18. Additions not in the brief

### Heider; Cartwright & Harary: structural balance

- Heider, F. (1946). Attitudes and cognitive organization. *Journal of
  Psychology*, 21, 107-112. DOI 10.1080/00223980.1946.9917275.
- Cartwright, D., & Harary, F. (1956). Structural balance: a
  generalization of Heider's theory. *Psychological Review*, 63(5),
  277-293. DOI 10.1037/h0046049.

Vocabulary: signed relations (like/dislike) among persons and objects; a
triad is balanced when the product of the signs is positive ("the friend
of my friend is my friend; the enemy of my enemy is my friend").
Cartwright & Harary generalised it to signed graphs. **Operands:** nodes
and signed edges. **Operators:** none as moves; it is an equilibrium
constraint, with the implied dynamic "change a sign to restore balance."
**Formality:** genuine graph theory with a theorem (a complete signed graph
is balanced if and only if its nodes split into two sets, all positive
edges inside a set and all negative edges between them, one set possibly
empty: Harary's structure theorem, stated in Cartwright & Harary 1956;
equivalently, every cycle has an even number of negative edges). **Standing:** classic, but real networks are
only partially balanced. **Relevance:** the best-known formal constraint on
a signed relation structure; any social algebra with like/dislike edges
should say how it relates.

### Bales: interaction process analysis

- Bales, R. F. (1950). *Interaction Process Analysis: A Method for the
  Study of Small Groups*. Addison-Wesley. (Reviews confirmed:
  10.2307/2086941, 10.2307/3707344; the book has no DOI found.)

- Bales, R. F. (1950). A set of categories for the analysis of small group
  interaction. *American Sociological Review*, 15(2), 257-263.

Vocabulary (validated): twelve categories of act in four blocks. Positive
socio-emotional: (1) shows solidarity, (2) shows tension release, (3)
agrees. Task, attempted answers: (4) gives suggestion, (5) gives opinion,
(6) gives orientation. Task, questions: (7) asks for orientation, (8) asks
for opinion, (9) asks for suggestion. Negative socio-emotional: (10)
disagrees, (11) shows tension, (12) shows antagonism. The scheme is
symmetric (1 opposes 12, 2 opposes 11, and so on), with pairs mapped to
six functional problems (communication, evaluation, control, decision,
tension reduction, reintegration). Exact label wording varies between
editions; later superseded by Bales's SYMLOG. **Operands:** members and their acts. **Operators:**
the coding categories are literally a fixed set of moves one person makes
in a group. Standing: a very influential observation instrument. This is
the nearest direct hit to "a fixed set of moves people make on one another"
in small-group research; it should be pulled and read in full before the
move catalogue is drafted.

### Hollander: idiosyncrasy credit

- Hollander, E. P. (1958). Conformity, status, and idiosyncrasy credit.
  *Psychological Review*, 65(2), 117-127. DOI 10.1037/h0042501.

A bookkeeping model: conforming earns credit that later licenses deviance.
Verbal, but gives a conserved-quantity-style state variable for leaders.
(Content from the title and general knowledge; abstract not retrieved.)

### Homans, Blau: exchange theory

- Blau, P. M. (1964). *Exchange and Power in Social Life*. Wiley.
  (Reprint DOI 10.4324/9780203792643; DOI of review/reprint, not of the book.)
- Homans, G. C. (1961). *Social Behavior: Its Elementary Forms*. (Record
  seen only as a review: 10.2307/2576649; DOI of review/reprint, not of the book.)

Out of scope for this cluster's search depth; flagged as important
neighbours of interdependence theory (exchange as the operator). Probably
belongs in the sociology/economics cluster.

---

## What this cluster already covers

- **A catalogue of candidate operators**, by type: transaction (Berne),
  switch of role (Karpman), transformation of the situation (Kelley &
  Thibaut), transformation of the frame (Goffman), position assignment
  (Positioning), influence by base (French & Raven), turn allocation and
  adjacency pair (Sacks et al.), dyadic contest (Chase), imitation of desire
  and scapegoating (Girard), categorise/identify (Tajfel & Turner), apply a
  force (Lewin), earn/spend emotional energy (Collins).
- **State representations for operands:** signed directed graphs (Moreno,
  Heider), dominance tournaments (Landau), outcome matrices (Kelley &
  Thibaut), role triangles, group-level modes (Bion), stages (Tuckman).
- **Genuine formal machinery in three places:** interdependence-theory
  matrix transformations, tournament and winner/loser models, signed-graph
  balance. Conversation analysis is formal in rules, not in maths.
- **Empirical track record** for several: turn-taking, minimal-group bias,
  dominance hierarchy self-organisation, interdependence in relationships.

## What it does not

- **No unified algebra.** There is no framework here with typed operands,
  a closed set of operators, composition rules, and identities that you
  could compute with across more than one domain. The nearest, Berne's
  transaction diagrams and interdependence theory's matrix transformation,
  each cover one slice (a dyad's exchange; a payoff structure).
- **Groups bigger than a dyad or triad are poorly handled.** Interdependence
  theory is dyadic, Berne and Karpman are dyadic/triadic, Chase's triads
  scale only by tournament counting, Bion and Tuckman treat the group as
  one lump and so never need an operator on individuals.
- **Operators are mostly typologies.** Belbin, French & Raven, Bion, Tuckman,
  Berne's ego states and Karpman's roles are labelled lists whose
  boundaries were set by clinicians or consultants, not derived, and whose
  empirical standing ranges from mixed (Belbin) to untested (Karpman).
  French & Raven is a typology of *sources* of leverage, which is fair;
  it is still the most usable of these as a list of influence-move types. [from abstract/standard account]
- **Few frameworks say what changes the state.** Moreno, Kenny, and Heider
  describe a state; Lewin, Collins and Girard describe change only in prose.
- **Composition is mostly absent.** Only Goffman's stacked keyings and
  Berne's closure rule hint at "do A, then B." Nothing gives equations like
  "scapegoat after rivalry returns the group to equilibrium."
- **Time and memory are thin** (apart from Chase's updating effects and
  Collins's energy accumulation).

The practical reading: the algebra is not a rediscovery of any one of these,
but nearly every operator it will need already has a name in one of them.
Start from the catalogue, borrow the matrix-transformation structure and the
tournament dynamics for the formal core, and treat the typologies as hypotheses
about which moves to include.

## Clearly missing important work (added in validation)

These are closer to "typed operators with rules" than most of the above
and should be read before the move catalogue is drafted. DOIs checked
against Crossref unless noted.

- **Heise, D. R. (1979). *Understanding Events: Affect and the
  Construction of Social Action*. Cambridge UP** (no DOI checked).
  Affect control theory: Actor-Behaviour-Object events, each element an
  Evaluation-Potency-Activity vector, with empirically estimated
  impression-change equations. Literally operators with equations; the
  single most relevant omission.
- **Fiske, A. P. (1992). The four elementary forms of sociality.
  *Psychological Review*, 99(4), 689-723. DOI
  10.1037/0033-295X.99.4.689.** Relational models theory: communal
  sharing, authority ranking, equality matching, market pricing, explicitly
  mapped to nominal, ordinal, interval and ratio scale structures. An
  algebraic typing of relationships.
- **Benjamin, L. S. (1974). Structural analysis of social behavior.
  *Psychological Review*, 81(5), 392-425. DOI 10.1037/h0037024.** SASB:
  interpersonal acts on three surfaces (focus on other, on self,
  introjected) with complementarity and antithesis rules.
- **Kiesler, D. J. (1983). The 1982 interpersonal circle: a taxonomy for
  complementarity in human transactions. *Psychological Review*, 90(3),
  185-214. DOI 10.1037/0033-295X.90.3.185.** (Leary 1957 lineage.)
  Complementarity: an act on the circumplex invites a predictable reply
  (similar on warmth, reciprocal on dominance). An operator with an
  expected response, like an adjacency pair but on content.
- **Emerson, R. M. (1962). Power-dependence relations. *American
  Sociological Review*, 27(1), 31-41. DOI 10.2307/2089716.** See 03 §8.
- **French, J. R. P., Jr. (1956). A formal theory of social power.
  *Psychological Review*, 63(3), 181-194. DOI 10.1037/h0046123.** See 05 §1
  (and Harary 1959, 05 §2). Formal companion to French & Raven (§11).
- **Berger, J., Fisek, M. H., Norman, R. Z., & Zelditch, M. (1977).
  *Status Characteristics and Social Interaction*. Elsevier** (no DOI
  checked). Expectation states theory, with a graph-theoretic model of how
  status characteristics combine into performance expectations and
  interaction hierarchies in task groups; the human counterpart to Chase.

## Unconfirmed (not verified from a source I could retrieve; do not cite)

Revised in validation: items resolved have been folded into the text above
and removed from this list.

- Moreno's runaway anecdote at the Hudson school, in any of its versions
  (two isolated girls, or a networked wave of runaways). Read *Who Shall
  Survive?* before using it.
- The date Belbin added the Specialist role.
- Berne's "game formula" wording (Con + Gimmick = Response, Switch,
  Cross-up, Payoff), which is from his 1972 *What Do You Say After You Say
  Hello?*, not 1964; not checked.
- The names of the six interdependence dimensions are from the verifier's
  knowledge of Rusbult & Van Lange (2003); only the count was confirmed
  from the abstract.
- Lewin's "refreezing" attributed to Festinger by a commercial source.
- Tuckman & Jensen 1977 study count (20 vs 22).
- Fisher et al. (2001) mapping Belbin onto the Big Five: cited via
  Aritzeta et al. 2007 only.

Resolved by the verifier from standard knowledge rather than retrieval
(reliable, but cite the primary text if it matters): Lewin's B = f(P, E)
(1936) and hodological space (1938); Moreno's tele and social atom; the
meta-contrast ratio (mean inter-category difference over mean
intra-category difference, Turner et al. 1987); Bion 1961 Tavistock,
Berne 1964 and 1961 Grove Press, Goffman 1974 Harper & Row; Tuckman's
review of about 50 articles.

## Sociological role theory: Linton, Merton, Biddle (§role theory)

- Linton, R. (1936). *The Study of Man*. New York: Appleton-Century. (Status/role definitions known only second-hand, via Merton 1957.)
- Merton, R. K. (1957). "The Role-Set: Problems in Sociological Theory." *British Journal of Sociology* 8(2): 106–120. DOI 10.2307/587363 [Crossref-checked]. Full text: https://home.uevora.pt/~eje/ROLESET.HTM
- Biddle, B. J. (1986). "Recent developments in role theory." *Annual Review of Sociology* 12: 67-92. DOI 10.1146/annurev.so.12.080186.000435 (confirmed by search).

**Their vocabulary**: status (position in a social system, with designated rights and obligations); role (behaviour oriented to the patterned expectations attached to a status); role-set; status-set; role conflict; consensus; conformity; role taking.

**Operands**: positions (statuses) and the persons who occupy them. A person holds several statuses (status-set); each status carries several roles toward different counter-positions (role-set).

**Operators** and structure:
- Occupancy: person -> status, one person to many statuses [from standard account].
- Status -> role-set: the complement of role relationships a person has because they occupy one status (Merton) [read, via Wikipedia and the Évora text]. A status is thus a bundle of relations to counter-positions (teacher to pupil, to parent, to colleague).
- Role conflict: incompatible expectations within a role-set or across a status-set [from standard account].
- Biddle sorts the field into five perspectives: functional, symbolic interactionist, structural, organizational, cognitive; and four derived concepts: consensus, conformity, role conflict, role taking [from abstract/search summary].

**Limits**: Descriptive and verbal. No composition of roles, no calculus of what one role-holder does to another; "expectation" is the only relation and is left informal. Linton and Merton were not read directly. Biddle's review was not read beyond its summary. Later network work (White, Lorrain, Boorman) formalises exactly what this tradition leaves informal.

**Relevance to social-algebra**: This is the vocabulary check. Status/role is the operand layer (positions and role-sets are what the algebra's operands should be able to express), and Merton's role-set gives a ready account of one operand carrying a bundle of typed relations to counter-operands. The tradition supplies no operators, so the algebra has to supply them; the role-conflict notion is a candidate for a consistency condition between operators.

Unconfirmed: Linton's definitions at source; the content of Biddle beyond the summary; whether Biddle discusses formal/network role models.

_Added 2026-10-29 after the second pass, on next-pattern's direction; this entry has not itself been second-passed. Provenance tags as marked._

## Validation log (2026-10-29)

Every DOI in the file was re-resolved against Crossref; all matched
authors, year, title and venue.

- Lewin 1936, 1947, 1951: ✓
- Moreno 1934: ✎ runaway anecdote demoted to Unconfirmed (version given was unsupported and differs from the usual telling)
- Bion 1948-49, 1961: ✓
- Tuckman 1965; Tuckman & Jensen 1977: ✓
- Belbin 1981: ✎ 1981 model had eight roles under older names; nine-role list is the later form
- Aritzeta et al. 2007: ✓
- Berne 1964, 1961: ✎ added his three rules of communication; summary no longer files transactions as a mere typology
- Karpman 1968, 2019: ✓ (typology label fair)
- Girard 1965/76, 1977; Livingston 1992: ✓
- Thibaut & Kelley 1959; Kelley & Thibaut 1978: ✎ added reflexive/fate/behaviour control as the original names
- Kelley et al. 2003 Atlas: ✎ print year 2003 confirmed; added AC/PC/JC decomposition, three base patterns, 21 situations
- Rusbult & Van Lange 2003: ✎ six dimensions added (names partly from knowledge, see Unconfirmed)
- Transformations: ✎ resolved: MaxOwn, MaxOther, MaxJoint, MinDiff, MaxRel, stated with sources (Wieselquist et al. 1999; Van Lange 1999 added)
- Kenny & La Voie 1984, 1985; Warner et al. 1979: ✎ added pages and the SRM equation with both reciprocity terms
- French & Raven 1959: ✎ reprint record identified (1986); unsourced "5- and 11-factor scales correlate weakly" claim removed
- Hinkin & Schriesheim 1989: ✓
- Goffman 1955, 1974: ✎ "Davis & Gamson 1975" was two separate reviews; both cited with DOIs; five basic keys added
- Sacks, Schegloff & Jefferson 1974: ✎ added rule 2 (recursion) and the may-but-need-not of 1(c)
- Schegloff & Sacks 1973: ✓
- Davies & Harré 1990; Harré & van Langenhove 1999; Harré & Moghaddam 2003: ✓
- Collins 2004: ✎ ingredients and outcomes resolved and added
- Landau 1951 I and II, 1968: ✎ Part I DOI found, pages 1-19 settled; h range 0-1 stated
- de Vries 1995: ✎ full record added
- Chase 1974, 1980: ✓
- Chase 1982, 1985: ✎ added; jigsaw-puzzle model resolved (four triad sequences, 77% transitive in hens)
- Chase et al. 2002 PNAS: ✎ abstract quoted; reassembly result (27.3% of 22 groups) added
- Chase & Seitz 2011; Dugatkin 1997: ✓
- Chase, Bartolomeo & Dugatkin 1994: ✎ added as the winner-effect source
- Lindquist & Chase 2009; Kura et al. 2016; Chase & Lindquist 2016: ? named only, no records checked
- Tajfel & Turner 1979; Turner et al. 1987: ✓
- Heider 1946; Cartwright & Harary 1956: ✎ structure theorem stated correctly
- Bales 1950: ✎ twelve categories confirmed and listed; ASR 1950 article added
- Hollander 1958: ✓
- Blau 1964; Homans 1961: ✓
- Missing work added: Heise 1979, Fiske 1992, Benjamin 1974, Kiesler 1983, Emerson 1962, French 1956, Berger et al. 1977

**Verdict.** The bibliography is sound: every DOI resolves to the claimed
work, and nothing was fabricated. The content was thinner than the
citations. Its sources were search summaries, so it left the most formal
material unresolved: the interdependence decomposition and
transformations, the jigsaw model and Bales's categories. Two claims were
unsupported (Moreno's anecdote and the French & Raven scale correlation).
The biggest weakness was the omission of affect control theory and
relational models theory, which come closer to an operator algebra than
anything the survey did include.
