# Prior work 11: classical social theory, philosophy and statecraft

Date: 2026-10-29. Survey for `social-algebra`. Scope: classical sociology, social philosophy, analytic social ontology, and ancient/early-modern statecraft (Indian, Chinese, European). Network/role algebras, kinship, social psychology, opinion dynamics, cybernetics, cliodynamics, biology, economics and linguistics are covered by other agents.

## Summary

- **Twenty entries.** Almost none is formal. The value is the inventory of moves, not the calculus.
- **Closest precedents to the owner's aim, in order:** (1) Simmel's triad chapter, which is a small catalogue of operators on a three-party configuration; (2) Kautilya's *upayas* (sama, dana, bheda, danda), which are explicitly operators one party applies to another, plus the *mandala* as a relation-typing of states; (3) Homans/Emerson/Blau exchange theory, the only cluster with something close to operator-plus-state-update rules.
- **The only strictly formal results here are List & Pettit's impossibility theorems** (about aggregating operands, not about moves). They are a warning for any algebra with group-level operands.
- **Sourcing caveat.** Verified from fetched pages: SEP entries (Roth, Iser, Kim, Bourdeau, Aboulafia & Taylor, Nederman) and Wikipedia pages (with their own citations), plus search-result confirmation for List & Pettit, Kautilya's lists and Sun Tzu. Where a fetched page did not contain a claim, it is under "Unconfirmed" at the end and is not asserted in the entries. The "Operands/Operators (translated)" sections are my translation into the project's vocabulary, not the authors' words.
- **Validated 2026-10-29** (log at the end): Simmel checked against the full Wolff text, and most former "Unconfirmed" items resolved. The tertius gaudens, mandala and Sun Tzu/Kautilya entries were corrected.
- Formality scale used below: **informal** (prose categories), **taxonomic** (named, exhaustive-ish list), **semi-formal** (stated propositions or conditions), **formal** (theorems).

---

## 1. Georg Simmel, formal sociology: dyad, triad, forms of sociation

- **Citation.** Simmel, G., *Soziologie: Untersuchungen über die Formen der Vergesellschaftung* (Leipzig: Duncker & Humblot, 1908). English: *The Sociology of Georg Simmel*, trans., ed. Kurt H. Wolff (Glencoe, Ill.: Free Press, 1950). Triad chapter: Part Two ("Quantitative Aspects of the Group"), ch. IV, "The Triad", pp. 145-169 (sections: Sociological Significance of the Third Element, p.145; The Non-Partisan and the Mediator, p.145; The Tertius Gaudens, p.154; Divide et Impera, p.162). Dyad: ch. III, "The Isolated Individual and the Dyad", pp. 118-144 (§5 The Dyad p.122; §9 The Expansion of the Dyad, incl. "The Triad vs. the Dyad", p.135). Page numbers and section text checked against the full djvu text of Wolff 1950 in the validation pass.
- **Verified.** Wolff table of contents and bibliographic data: https://archive.org/stream/in.ernet.dli.2015.215265/2015.215265.The-Sociology_djvu.txt (only the contents page was readable by my tool; I did not read the chapter body). Summary of the triad forms: https://acawiki.org/The_triad . Overview of the five forms: https://en.wikipedia.org/wiki/Georg_Simmel . Secondary on later formalisation attempts: Nooteboom, B. (2006), "Simmel's treatise on the triad (1908)", *Journal of Institutional Economics* 2(3): 365-383, doi:10.1017/S1744137406000452 (DOI resolves; abstract only read; it is a commentary in the journal's classics series, not a formalisation).
- **Their vocabulary.** *Formen der Vergesellschaftung* (forms of sociation) vs *Inhalte* (contents/motives); the form is what stays constant across contents. Forms listed on Wikipedia: subordination, superordination, exchange, conflict, sociability (the "play-form"). Dyad: each member keeps individuality because no third can shift the balance; the dyad dies if either leaves. Triad: the third can become majority over a member, and a departure leaves a dyad. The third's roles: non-partisan (as mediator, who guides the two to agreement but "keeps out of any decision", or as arbitrator, to whom they hand the decision), tertius gaudens ("the third who rejoices": profits from an *existing or emerging* conflict between two, either passively because they hold each other in check or actively because they compete for his favour), divide et impera (the third "intentionally produces the conflict in order to gain a dominating position", turning two parties previously united against him on one another) (Wolff pp. 147-148, 154-155, 162).
- **Operands (translated).** Persons or groups as *positions* in a configuration of size 2 or 3 (and "larger groups"). Content (interests, feelings) is deliberately abstracted away; only the *form* of relation and the number of positions matter.
- **Operators (translated).** Informal but crisp, and the triad chapter is effectively an operator catalogue:
  - *Mediate/hold together*: third strengthens the bond between two or creates an indirect link (non-partisan).
  - *Arbitrate*: third stands above the two and decides.
  - *Exploit an existing conflict* (tertius gaudens): third gains because the two neutralise each other, or because they bid for its favour (*play off*). In Simmel the conflict is given, not made; the "broker who keeps two apart as gateway" reading is Burt's later network usage (*Structural Holes*, 1992), not Simmel's.
  - *Incite conflict* (divide et impera): third deliberately creates the conflict between two who were united or mutually dependent against it. The given-vs-made conflict is the operator-level difference between this and tertius gaudens.
  - *Subordinate / superordinate*, *exchange*, *conflict*, *sociability* as general forms of sociation (not specifically dyadic).
  - Structural operators: *add a third* (dyad -> triad: new coalition possibilities, majority over one), *remove a member* (triad -> dyad).
- **Predictive/control claim.** Structural: the form of the configuration constrains what can happen regardless of content (e.g. a third in a symmetric position has a "decisive" relation to both). No quantitative prediction. Guidance for control is implicit (a third can profit by separating).
- **Limits.** No formal notation; examples are anecdotal; operators are role-descriptions (what a third *is*) more than actions with defined effects; no composition rules; small-N emphasis.
- **Relevance.** Arguably the closest classical precedent for the "operators on operands in a configuration" idea. The form/content split is exactly the abstraction an algebra needs. The triad catalogue is a ready seed for a first operator set. Treat with care: Simmel names *roles* of the third, so some conversion to *moves* is needed (a role = the move it habitually makes).

## 2. Auguste Comte, "social physics"

- **Citation.** Comte, *Cours de philosophie positive* (1830-42); *Système de politique positive* (1851-54). Entry: Bourdeau, M., "Auguste Comte", *Stanford Encyclopedia of Philosophy*, first pub. 1 Oct 2008, substantive rev. 13 Jan 2026. https://plato.stanford.edu/entries/comte/
- **Vocabulary.** *Physique sociale* -> *sociologie*; social statics (spontaneous order, ch. 50 of the *Cours*) vs social dynamics (progress); law of three stages (theological/metaphysical/positive, also military -> industrial); the hierarchy of sciences with sociology last.
- **Operands.** Society as a whole, plus institutions (family, state, language, religion) as elements. Not individuals.
- **Operators.** Almost none at the interaction level. Closest: *specialise* (division of labour), which threatens cohesion, and *govern* (counter disintegrating tendencies). Informal.
- **Predictive/control claim.** Strong: laws of social development permit prevision, and prevision permits intervention. The law of three stages is a historical-trend claim.
- **Limits.** Macro-only; stage law is 19th-century philosophy of history (SEP says it "now seems alien"); no operators on persons.
- **Relevance.** Establishes the project's claim ("a science of the social with laws") but offers nothing at operator level. Useful only as the ancestor of the ambition and as a warning about the scale at which laws were sought.

## 3. Adolphe Quetelet, "social physics" and the average man

- **Citation.** Quetelet, *Sur l'homme et le développement de ses facultés, ou Essai de physique sociale* (Paris, 1835); English *A Treatise on Man* (1842). https://en.wikipedia.org/wiki/Adolphe_Quetelet (cites Beirne, P. (1987), "Adolphe Quetelet and the Origins of Positivist Criminology", *American Journal of Sociology* 92(5): 1140-1169, and Grue & Heiberg (2006), *Scandinavian Journal of Disability Research* 8(4): 232-246).
- **Vocabulary.** *Homme moyen* (average man), statistical laws of crime, marriage, suicide; normal distribution of traits; deviation from the mean.
- **Operands.** Populations; the "average man" as a summary operand; rates.
- **Operators.** Statistical: *average*, *measure deviation*; and causal-correlational links from social factors (age, sex, poverty, education, climate) to rates. Not actions of one party on another. Formality: quantitative but not algebraic.
- **Predictive/control claim.** Regularities in aggregate rates are stable and predictable even though individual acts are free; this was the scandal.
- **Limits.** Aggregate only; no interaction; the mean is treated as an ideal type, which is normatively loaded.
- **Relevance.** Marks the statistical branch, not the algebraic one. Relevant as the "model the distribution, not the individual" alternative to the project's approach.

## 4. Emile Durkheim, mechanical and organic solidarity

- **Citation.** Durkheim, *De la division du travail social* (1893); *The Division of Labour in Society*. Secondary: https://en.wikipedia.org/wiki/Mechanical_and_organic_solidarity (cites Lukes 1973, *Emile Durkheim: His Life and Work*, Allen Lane; Lukes & Scull 2013, *Durkheim and the Law*). The SEP Durkheim page returned "Not Yet Available", so no SEP citation.
- **Vocabulary.** Mechanical solidarity (cohesion by likeness; repressive law); organic solidarity (cohesion by interdependent difference; restitutive law); social facts.
- **Operands.** Individuals as similar (mechanical) or specialised (organic) members of a society; the society's "type".
- **Operators.** Two *types of bond* rather than actions: *resemble* and *depend*. Plus the sanction operators: *repress* (penal) and *restore/compensate* (restitutive). Informal; the sanction type is read as an indicator of the solidarity type.
- **Predictive/control claim.** Division of labour increases with density; law type tracks solidarity type.
- **Limits.** Typological; two ideal types on one axis; Wikipedia flags one statement as "dubious", so cross-check anything leaned on.
- **Relevance.** Gives the project a first pair of *relation kinds* (similarity-based vs complementarity-based tie), a useful primitive: a tie is either "same as" or "needs from".

## 5. Max Weber, types of action and authority

- **Citation.** Weber, *Wirtschaft und Gesellschaft* (1922); *Economy and Society*, ed. Roth & Wittich (Berkeley: University of California Press, 1978), p. 4 for the social-action definition (as cited at https://en.wikipedia.org/wiki/Social_action). Authority types: Kim, S. H., "Max Weber", *SEP*, first pub. 24 Aug 2007, rev. 21 Sep 2022. https://plato.stanford.edu/entries/weber/
- **Vocabulary.** Social action = action whose subjective meaning takes account of the behaviour of others. Four types: *zweckrational* (instrumentally rational), *wertrational* (value-rational), affectual, traditional (*Economy and Society*, Part One, ch. I, §2, pp. 24-26 in Roth & Wittich; "social relationship" is defined in §3, pp. 26-28; the three pure types of legitimate domination are at ch. III, p. 215). Three legitimate authorities: charismatic, traditional, legal-rational.
- **Operands.** Actors with subjective meanings; a *social relationship* (a plurality of actors whose action is mutually oriented, existing as the probability that such action occurs); a ruler and a staff or the ruled.
- **Operators.** The four action types are *orientations* (what the actor is guided by), not moves. Authority types are *legitimation bases* for command/obedience. Closest to operators: *command-obey* conditioned on legitimacy type. Informal, typological.
- **Predictive/control claim.** Legitimacy type predicts stability and the form of administration (not fully read here).
- **Limits.** Ideal types, explicitly not laws; no composition; meaning-based so hard to observe.
- **Relevance.** Supplies the "attributes of the operator application": the same move (a command) works differently depending on the legitimation basis. Suggests operators should carry a parameter for why the target complies.

## 6. Talcott Parsons, pattern variables and AGIL

- **Citation.** Parsons, *The Social System* (1951); Parsons & Smelser, *Economy and Society* (1956). AGIL table: https://en.wikipedia.org/wiki/AGIL_paradigm (cites Parsons, "On the Concept of Value-Commitments", *Sociological Inquiry* 38(2), April 1968: 135-160, for the media). Biographical dates: https://en.wikipedia.org/wiki/Talcott_Parsons .
- **Vocabulary.** AGIL: Adaptation (economy, medium money), Goal attainment (polity, power), Integration (societal community, influence), Latency/pattern maintenance (value-commitment). Pattern variables: five dichotomous choices an actor faces in defining a situation, generalising Tönnies's Gemeinschaft-Gesellschaft axis: affectivity / affective neutrality; self-orientation / collectivity-orientation; universalism / particularism; ascription / achievement (quality / performance); diffuseness / specificity (Parsons, *The Social System*, 1951, ch. II; Parsons & Shils, eds., *Toward a General Theory of Action*, Harvard UP, 1951). Self/collectivity orientation was dropped in later work.
- **Operands.** Subsystems (and actors within roles); *generalized symbolic media* circulate between them.
- **Operators.** Exchanges of media between subsystems (money, power, influence, commitments); each subsystem "does" its function. Closest to a formal "input-output table" among the classics, though still informal. Notably media are *conserved/inflatable* in analogy to money.
- **Predictive/control claim.** Functional prerequisites: a viable system must solve all four problems; imbalance predicts strain.
- **Limits.** Functionalist; heavy on categories, light on dynamics; macro; criticised as static (not sourced here).
- **Relevance.** Offers the idea that interaction can be modelled as typed *media* passed along edges, and a four-slot decomposition of any group's function. Probably the best classical source for "what flows" if the algebra needs conserved quantities.

## 7. George Homans, *Social Behavior: Its Elementary Forms*

- **Citation.** Homans, G. C., "Social Behavior as Exchange", *American Journal of Sociology* 63(6): 597-606 (1958), doi:10.1086/222355; *Social Behavior: Its Elementary Forms* (New York: Harcourt, Brace & World, 1961; rev. ed. 1974); *The Human Group* (1950) for activities/interactions/sentiments. Verified secondary: https://en.wikipedia.org/wiki/Social_exchange_theory (reference list gives Homans 1958 and 1961; Emerson, R. M. (1976), "Social Exchange Theory", *Annual Review of Sociology* 2: 335-362).
- **Vocabulary.** Propositions (as listed in the 1974 revised edition): success (rewarded behaviour repeats), stimulus, value, deprivation-satiation (diminishing marginal reward), aggression-approval (unexpected non-reward -> anger; unexpected reward -> approval), and rationality (choose the act whose value times probability of success is greater). Six in all.
- **Operands.** Persons; activities, sentiments, interactions (the triple is from *The Human Group*, 1950); rewards and costs.
- **Operators.** *Reward*, *punish*, *reciprocate*, *withhold*. The propositions are state-update rules: given a history of reward, behaviour probability changes. Semi-formal (verbal propositions borrowed from behavioural psychology).
- **Predictive/control claim.** Yes: by manipulating rewards you change another's behaviour frequency. This is explicitly an influence calculus.
- **Limits.** Reduces to individual psychology; propositions not derived; difficulty with institutions; critics say tautological (not sourced here).
- **Relevance.** One of the few places where "operator on another party" and "resulting state change" are both stated. A good test-bed for what an interaction rule looks like.

## 8. Peter Blau (and Emerson), exchange and power

- **Citation.** Blau, P. M., *Exchange and Power in Social Life* (New York: John Wiley & Sons, 1964). Emerson, R. M. (1962), "Power-Dependence Relations", *American Sociological Review* 27(1): 31-41, doi:10.2307/2089716 (the primary source for power-dependence; added in validation). Emerson, R. M. (1976), *Annual Review of Sociology* 2: 335-362. https://en.wikipedia.org/wiki/Peter_Blau ; https://en.wikipedia.org/wiki/Social_exchange_theory
- **Vocabulary.** Social vs economic exchange (intrinsic vs extrinsic rewards, emotional component); emergent social structure from exchange patterns in small groups; Emerson's *power-dependence*: dependence of A on B gives B power over A; position in an exchange network determines dependence.
- **Operands.** Actors in exchange relations; network positions; rewards.
- **Operators.** *Give*, *reciprocate*, *incur obligation/debt*, *avoid dependence*, *withdraw*. Blau moves from exchange to power and structure; Emerson makes it network-structural. Semi-formal (Emerson's later work is experimental/formal; this survey only confirmed the stated claims).
- **Predictive/control claim.** Relative dependence in a network predicts power and the course of bargaining.
- **Power from unreciprocated exchange** (Blau 1964, ch. 5): a person needing a service who cannot reciprocate has four alternatives: supply something the other needs, obtain it elsewhere, coerce the provider, or do without; failing all four, they must subordinate themselves, and this unilateral dependence is the source of power. Status differentiation in groups follows from it. This is standard Blau and well attested in the secondary literature; the Wikipedia page the original pass read simply did not cover it. The four alternatives are themselves an operator set (reciprocate, substitute, coerce, forgo, else submit).
- **Limits.** Blau's macrostructural later work (1977) not reviewed.
- **Relevance.** Contributes an invariant: *power = asymmetry of dependence*, a derived quantity not a primitive. Good candidate for something the algebra should compute rather than assume.

## 9. Mead and Blumer, symbolic interactionism

- **Citation.** Mead, G. H., *Mind, Self and Society*, ed. C. W. Morris (Chicago, 1934; compiled from lectures after Mead's death in 1931). Blumer, H., *Symbolic Interactionism: Perspective and Method* (Englewood Cliffs, N.J.: Prentice-Hall, 1969). Entries: Aboulafia, M. & Taylor, S., "George Herbert Mead", *SEP*, first pub. 13 Apr 2008, rev. 24 Nov 2022, https://plato.stanford.edu/entries/mead/ ; https://en.wikipedia.org/wiki/Symbolic_interactionism
- **Vocabulary.** Gesture; significant symbol (a gesture that calls up in the sender the response it calls up in the receiver); taking the attitude of the other; "I" and "me"; generalized other. Blumer's premises: people act on the meanings things have for them; meanings arise from interaction; meanings are handled and modified through interpretation. "Definition of the situation".
- **Operands.** Selves; gestures/symbols; groups as generalized others.
- **Operators.** *Gesture -> response* (the conversation of gestures); *role-take* (adopt the other's attitude); *interpret/redefine meaning*. Informal.
- **Predictive/control claim.** Deliberately weak; Blumer argued against variable-style prediction. Meaning is emergent in interaction.
- **Limits.** Anti-formal by principle; micro; hard to aggregate.
- **Relevance.** Identifies a hidden operand: *the other's model of me*. If the algebra treats an act as acting on a bare state it will miss that outcomes depend on how the move is read. The `role-take` operator is a nested-model operation.

## 10. Niklas Luhmann, social systems as communication

- **Citation.** Luhmann, N., *Soziale Systeme* (Frankfurt: Suhrkamp, 1984); *Social Systems*, trans. J. Bednarz with D. Baecker (Stanford University Press, 1995). *Die Gesellschaft der Gesellschaft* (Suhrkamp, 1997); *Theory of Society* (Stanford UP, 2012-13). Verified via https://en.wikipedia.org/wiki/Niklas_Luhmann (publication table).
- **Vocabulary.** Social systems consist of communications, not people (people are environment); autopoiesis (recursive self-reproduction of communications); operational closure; meaning (*Sinn*) as selection; binary codes per function system (e.g. payment/non-payment); symbolically generalised communication media (truth, love, money, power, among others; "peace" in the original pass was wrong); interpenetration. Communication is a synthesis of three selections: information (*Information*), utterance (*Mitteilung*) and understanding (*Verstehen*) (*Social Systems*, ch. 4). Separately, it faces three improbabilities: of being understood, of reaching its addressee, and of being accepted.
- **Operands.** Communications (events), not persons; function systems.
- **Operators.** *Communicate* (an event that connects to a previous communication and enables the next); *code* (apply a system's binary distinction to an observation); *observe another system via own code*. Formality: highly abstract; Luhmann borrows the "draw a distinction" vocabulary of Spencer-Brown's *Laws of Form* (1969) but does not use its calculus.
- **Predictive/control claim.** Deliberately no steering claim; systems can only irritate each other.
- **Limits.** Radical: removes people as operands, which conflicts with the project's stated operands (people, roles, groups). Notoriously opaque.
- **Relevance.** Offers an alternative operand choice (events rather than agents) and a clean statement that an operator is anything that connects to a prior one. Worth keeping as the competing representation to the agent-centric one.

## 11. Jurgen Habermas, communicative vs strategic action

- **Citation.** Habermas, *Theorie des kommunikativen Handelns* (1981); *The Theory of Communicative Action*, trans. T. McCarthy, 2 vols (Boston: Beacon, 1984, 1987). Entry: Finlayson, J. G. & Rees, D. H., "Jürgen Habermas", *SEP*, first pub. 15 Sep 2023, https://plato.stanford.edu/entries/habermas/ (authors confirmed in validation; the page gives Habermas's dates as 1929-2026, which post-dates the validator's knowledge and is not evidence of an error).
- **Vocabulary.** Communicative action (oriented to reaching understanding) vs instrumental and strategic action (strategic = influencing others for one's ends). Every speech act raises validity claims: truth, rightness, truthfulness. Speech acts: constatives, regulatives, expressives.
- **Operands.** Speakers and hearers; validity claims; the lifeworld.
- **Operators.** *Assert*, *request/command* (regulative), *express*, *accept/reject a claim* (yes/no), and the meta-distinction *strategic move* (influence by threat or inducement) vs *communicative move* (appeal to reasons). Informal, though the speech-act typology gives a finite list.
- **Predictive/control claim.** Normative: rational agreement is possible when claims are redeemable. Claims communicative action is more basic than strategic action (the SEP says critics doubt this is established).
- **Limits.** Normative reconstruction rather than description; hard to model.
- **Relevance.** Gives a *typing of operators by mode*: the same surface move can be strategic or communicative. In the algebra that is a flag on every operator (does it work through the target's reasons, or around them?).

## 12. Hegel and Honneth, recognition

- **Citation.** Hegel, *Phänomenologie des Geistes* (1807), master-slave section. Honneth, A., *Kampf um Anerkennung* (1992); *The Struggle for Recognition: The Moral Grammar of Social Conflicts*, trans. J. Anderson (Cambridge: Polity Press, 1995). Entry: Iser, M., "Recognition", *SEP*, first pub. 23 Aug 2013, substantive rev. 27 Jul 2026, https://plato.stanford.edu/entries/recognition/ ; Honneth bibliography: https://en.wikipedia.org/wiki/Axel_Honneth
- **Vocabulary.** Struggle for recognition; the master-slave outcome (one submits; the master gets inadequate recognition because the slave does not count as a competent judge; adequate recognition requires an institutional order of rights). Honneth's spheres: love (self-confidence), rights (self-respect), esteem (self-esteem). Misrecognition damages practical identity and motivates resistance. The three forms of disrespect mirror the spheres (*Struggle for Recognition*, ch. 6): physical maltreatment (rape, torture) against love/self-confidence; denial of rights and exclusion against self-respect; denigration of one's way of life against self-esteem.
- **Operands.** Subjects with identities; recognition as a good one party confers.
- **Operators.** *Recognise* (confer status), *withhold/deny recognition*, *submit*, *struggle/resist*; by sphere: love, grant rights, esteem. Informal.
- **Predictive/control claim.** Social conflict is driven by misrecognition; a normative-developmental claim.
- **Limits.** Speculative philosophy; the master-slave dyad is a thought experiment.
- **Relevance.** A distinct *currency*: recognition is not money, power or obligation. Non-conserved, asymmetric (it can be given without loss). Suggests (interpretation, not Hegel's or Honneth's claim) that a mutual operator (reciprocal recognition) reaches a stable state that unilateral ones cannot, which is the moral of the master-slave outcome. Disrespect gives three typed negative operators, one per sphere.

## 13. Martin Buber, I-Thou and I-It

- **Citation.** Buber, M., *Ich und Du* (1923); *I and Thou*. Entry: Zank, M. & Braiterman, Z., "Martin Buber", *SEP*, https://plato.stanford.edu/entries/buber/ (first pub. 20 Apr 2004, substantive rev. 12 May 2026).
- **Vocabulary.** Primary words (*Urworte*) I-Thou and I-It; encounter (*Begegnung*), presence, the "between" (*das Zwischen*).
- **Operands.** A self in one of two stances to another.
- **Operators.** Two modes: *encounter* (I-Thou, open reciprocity) and *objectify* (I-It: use, measure, manipulate). One can switch between them. Informal and anti-formal by intent ("no doctrine").
- **Predictive/control claim.** None.
- **Limits.** Explicitly resists systematisation.
- **Relevance.** Marks the boundary of what an algebra can capture: I-Thou is not an operation on the other. The I-It stance is nearly the algebra's own stance (treat the other as an object with properties), so the algebra should be honest that it models only that mode.

## 14. Analytic social ontology: Gilbert, Tuomela, Bratman

- **Citation.** Roth, A. S., "Shared Agency", *SEP*, first pub. 13 Dec 2010, rev. 1 May 2017, https://plato.stanford.edu/entries/shared-agency/ . Also the SEP entry on collective intentionality, https://plato.stanford.edu/entries/social-ontology-collective-intentionality/ (fetch returned an error; not read). Primary works: Gilbert, M., *On Social Facts* (London: Routledge, 1989); Gilbert, M., "Walking Together: A Paradigmatic Social Phenomenon", *Midwest Studies in Philosophy* 15: 1-14 (1990), doi:10.1111/j.1475-4975.1990.tb00202.x; Tuomela, R., *The Importance of Us* (Stanford UP, 1995) and *Social Ontology: Collective Intentionality and Group Agents* (Oxford UP, 2013); Bratman, M. E., "Shared Intention", *Ethics* 104(1): 97-113 (1993), doi:10.1086/293577, and *Shared Agency: A Planning Theory of Acting Together* (Oxford UP, 2014). DOIs checked in validation.
- **Vocabulary.** Bratman (1993): we intend to J iff (1) (a) I intend that we J and (b) you intend that we J; (2) I intend that we J in accordance with and because of (1a), (1b) and meshing sub-plans of (1a) and (1b), and you likewise; (3) (1) and (2) are common knowledge between us. The intentions interlock (each refers to the other's) and require meshing sub-plans, not identical ones. Gilbert: *joint commitment* is primitive, arises from open expressions of readiness, cannot be rescinded unilaterally, and generates directed obligations between parties (Sue may rebuke Jack for walking too fast; the example is from "Walking Together"). Tuomela: *we-mode* (acting as a group member for a group reason, under collective commitment) vs *I-mode* (acting as a private person, possibly with others).
- **Operands.** Agents with intentions; a joint commitment as a relation-object between agents.
- **Operators.** *Express readiness* (create a joint commitment), *concur in release* (the only way out), *rebuke* (enforce a directed obligation), *mesh plans* (Bratman). Semi-formal: Bratman gives conditions; Gilbert gives creation and dissolution rules.
- **Predictive/control claim.** Constitutive: what makes an activity joint, and what obligations follow.
- **Limits.** Conceptual analysis, not formal; critics say Gilbert redescribes rather than explains obligation (SEP).
- **Relevance.** Gilbert's joint commitment is a ready-made *binary relation with create/dissolve rules and generated obligations*, essentially a primitive object in a social algebra, and the nearest philosophy gets to "operator that changes the normative state of two parties at once".

## 15. Christian List and Philip Pettit, *Group Agency*

- **Citation.** List, C. & Pettit, P., *Group Agency: The Possibility, Design, and Status of Corporate Agents* (Oxford University Press, 2011; ISBN 9780199591565; doi:10.1093/acprof:oso/9780199591565.001.0001). Earlier: "Aggregating sets of judgments: An impossibility result", *Economics and Philosophy* 18(1): 89-110 (2002); "Aggregating sets of judgments: Two impossibility results compared", *Synthese* 140(1-2): 207-235 (2004). DOIs checked: 10.1017/S0266267102001098; 10.1023/B:SYNT.0000029950.50517.59. Background: the "doctrinal paradox" of Kornhauser & Sager (1986, 1993), which the discursive dilemma generalises. Verified via search results: https://researchonline.lse.ac.uk/id/eprint/35735 ; https://philarchive.org/rec/LISASO ; https://ideas.repec.org/a/cup/ecnphi/v18y2002i01p89-110_00.html
- **Vocabulary.** Judgement aggregation; the discursive dilemma (propositionwise majority voting over connected propositions can produce inconsistent collective judgements); a general impossibility theorem (no aggregation function satisfies universal domain, anonymity and systematicity and always yields complete and consistent collective judgements); corporate agents exist over and above members.
- **Operands.** Individuals' sets of judgements; a collective judgement set.
- **Operators.** An *aggregation function* from profiles of individual judgement sets to a collective set. This is the one formal operator in this cluster.
- **Predictive/control claim.** Theorems: which aggregation rules fail which conditions; the design consequence is that a group must give up some desideratum (e.g. use premise-based or conclusion-based procedures, or relax independence/universal domain).
- **Limits.** Models agreement only, not influence or conflict; the 2004 paper shows the result is related to, but not a corollary of, Arrow's theorem.
- **Relevance.** Sets a hard constraint: if the algebra has "group" as an operand whose properties are functions of members' properties, then some natural closure properties cannot all hold. Plan for groups to be defined by an explicit constitution (aggregation rule), not by "the sum of members".

## 16. Kautilya, *Arthashastra*: upayas, mandala, shadgunya

- **Citation.** *Kautilya's Arthashastra*. Authorship and date uncertain; the text is composite, with layers argued c. 150 BCE-300 CE (Olivelle 2013). Translations: R. Shamasastry (Sanskrit text 1909; English translation in installments from 1905, as a book 1915); R. P. Kangle, *The Kautiliya Arthasastra*, 3 parts (University of Bombay: critical text 1960, translation 1963, study 1965; second editions 1969-72); L. N. Rangarajan (1992, Penguin); P. Olivelle, *King, Governance, and Law in Ancient India: Kautilya's Arthasastra* (Oxford University Press, 2013), described as superseding earlier English translations. https://en.wikipedia.org/wiki/Arthashastra . Lists below confirmed by secondary summaries from search (e.g. https://www.gktoday.in/kautilyas-concept-of-raja-mandala-and-shadguna-in-foreign-policy/); these are exam-prep and explainer sites, so check each term against Kangle or Olivelle before building on it. Wikipedia's Mandala page covers the later Southeast Asian *mandala* political model, which is a different (derived) usage; it was not used for the Kautilyan doctrine.
- **Their vocabulary.** *Upaya* (means): sama (conciliation), dana (gift; the text's usual term is *upapradana*), bheda (division, sowing dissension), danda (force). *Mandala* (circle of states, Book 6 ch. 2) centred on the *vijigishu* (would-be conqueror): in front, *ari* (enemy, the contiguous neighbour), *mitra* (ally, beyond the enemy), *ari-mitra*, *mitra-mitra*, *ari-mitra-mitra*; behind, *parshnigraha* (rear enemy), *akranda* (rear ally), and their allies *parshnigrahasara*, *akrandasara*; plus the *madhyama* (middle king, adjoining both conqueror and enemy, able to help or suppress either singly) and the *udasina* (neutral, outside the territories of the other three and more powerful than any of them, able to help or suppress them). That is 12 kings; with five material elements (*prakriti*) each, 72 elements. Principle: the neighbour is the natural enemy, the neighbour's neighbour the natural ally. (The original pass had the madhyama "stronger than both" and the udasina "beyond the circle"; in Kangle's reading it is the udasina that is stronger, and both are members of the circle.) *Shadgunya* (six measures): *sandhi* (peace/treaty), *vigraha* (hostility), *asana* (stay neutral/wait), *yana* (march), *samshraya* (seek shelter with a stronger power), *dvaidhibhava* (dual policy: peace with one, war with another). This order is the text's own (Book 7 ch. 1). Sources agree the choice is a calculus of relative power, not of right (decline -> peace; ascent -> war; etc.). The *saptanga* (seven constituents of a state: svamin ruler, amatya ministers, janapada territory and people, durga fort, kosha treasury, danda army, mitra ally) is Book 6 ch. 1, and is the operand-structure of a single state.
- **Operands (translated).** States/rulers (and by extension, any party) located in a position relative to the actor: enemy, ally, middle, neutral, and a ruler's own constituents.
- **Operators (translated).** The most explicit operator set in the corpus:
  - On a single target: *conciliate* (sama), *pay/induce* (dana), *divide* (bheda), *coerce* (danda). Ordered from lightest to heaviest, with the earlier generally preferred; the ordering is the standard reading and is stated in the text (Book 9), though the exact verse was not checked against Kangle in validation. The text also allows them to be combined.
  - On a relation between parties: *make peace*, *make war*, *stay neutral*, *advance*, *shelter under a stronger*, *split policy* (peace with one, war with another).
  - Relation typing: *natural enemy* (neighbour), *natural ally* (neighbour's neighbour); a function of position, not of choice.
  Formality: taxonomic and rule-like (try in order; choose by relative power), with a topology (concentric circle) that makes relation types derivable from position.
- **Predictive/control claim.** Prescriptive: given relative power and position, the right measure follows. Lighter upayas preferred to heavier ones.
- **Limits.** Prescriptive composite text, not a record of practice (the sources note this); no composition semantics beyond sequencing; state-level.
- **Relevance.** Strongest ancient precedent for an operator set with a cost ordering and a relation topology that determines default valence. The bheda operator maps directly onto Simmel's divide et impera, which suggests the two lists can be merged.

## 17. Sun Tzu, *The Art of War*

- **Citation.** Sun Tzu (attributed; the earliest parts probably date from a century or more after the traditional dates, per Wikipedia), *The Art of War*, 13 chapters. Translations: L. Giles (annotated English, London: Luzac, 1910); S. B. Griffith (Oxford: Clarendon, 1963, UNESCO Collection of Representative Works); R. T. Ames (New York: Ballantine, 1993, incorporating the Yinqueshan finds). https://en.wikipedia.org/wiki/The_Art_of_War ; Giles text of ch. III: https://en.wikisource.org/wiki/The_Art_of_War_(Sun)/Section_III ; spies (ch. XIII): https://www.marxists.org/reference/archive/sun-tzu/works/art-of-war/ch13.htm
- **Vocabulary.** Calculation (five factors, seven elements, ch. I); preference ordering of attacks (III.3): baulk the enemy's plans (best), prevent the junction of his forces (Giles; most modern translators render 伐交 as "attack his alliances"), attack the army, besiege walled cities (worst); subdue without fighting; *shi* (momentum, ch. V; not defined on the page I read); five kinds of spy (local, inward, converted, doomed, surviving, per Giles; others say local/internal/double/dead/live).
- **Operands.** Opposing states/armies; the enemy's plan, alliances, forces, cities; information.
- **Operators (translated).** *Thwart plan*, *isolate from allies* (cut alliance), *engage*, *besiege*; information operators: *infiltrate/turn* (converted spy), *feed false information* (doomed spy), *scout*. Ranking by cost and by indirectness. Taxonomic.
- **Predictive/control claim.** Prescriptive; victory is probable if the pre-battle calculation favours you.
- **Limits.** Aphoristic; ordering is advisory.
- **Relevance.** Adds *information operators* and the idea that the preferred move is the one that works on the target's *plans and relations* rather than on the target's body. The preference runs the same way as Kautilya's upayas: force last. (The original pass said "run backwards", which was wrong; both lists put the costliest, most direct means at the bottom.)

## 18. Niccolo Machiavelli

- **Citation.** *Il Principe* (written 1513, pub. 1532); *Discorsi*. Entry: Nederman, C., "Niccolo Machiavelli", *SEP*, first pub. 13 Sep 2005, rev. 6 Dec 2023. https://plato.stanford.edu/entries/machiavelli/
- **Vocabulary.** *Virtu* (practical skill, flexible disposition), *fortuna* (hostile chance, met with boldness), fear vs love (fear more reliable), arms as the basis of law ("no good laws without good arms"), the ruler must be prepared to do evil if necessary, citizen militia over mercenaries.
- **Operands.** Prince and subjects; prince and other princes; arms.
- **Operators.** *Instil fear*, *win love* (less reliable) (*Prince* ch. 17), *use force*, *deceive* (the fox and the lion; keep faith only when it serves, *Prince* ch. 18), *arm the citizens*, *rely on mercenaries* (condemned, ch. 12). Informal.
- **Predictive/control claim.** Conditional counsel: given a type of principality and circumstances, certain conduct preserves the state.
- **Limits.** Case-based and rhetorical; no systematic table in the SEP summary.
- **Relevance.** Contributes a *stability criterion* for operators: which moves are reliable (fear) vs reversible (love). A tag on each operator: durable under defection or not.

## 19. Carl von Clausewitz, *On War*

- **Citation.** *Vom Kriege* (1832); *On War*, ed./trans. M. Howard & P. Paret (Princeton University Press, 1976; rev. ed. 1984); older translations J. J. Graham (London: Trübner, 1873), O. J. M. Jolles (Random House, 1943). https://en.wikipedia.org/wiki/Carl_von_Clausewitz (the SEP entry URL guessed returned 404).
- **Vocabulary.** War as continuation of policy by other means (Howard & Paret p. 87); the "remarkable trinity" (violent emotion, chance, reason; often misread as people-army-government); friction; fog of war; centre of gravity; culminating point.
- **Operands.** Opposing wills and forces; policy as the aim.
- **Operators.** *Attack*, *defend*, *concentrate at the centre of gravity*; the notion of *friction* is a damping term on any operator. Informal, though dialectical (polar opposition of offence and defence).
- **Predictive/control claim.** Stated tendencies (the defence is the stronger form, Book 6 ch. 1; the attack has a culminating point, Book 7 chs 5 and 22) but not formal.
- **Limits.** Not all of the Wikipedia page was read; war-specific.
- **Relevance.** Two structural ideas: *operators are executed with loss* (friction, fog), so any model needs noise; and *there is a threshold past which an operator reverses* (culminating point). Both are worth building into the algebra as parameters, not exceptions.

## 20. Confucian five relationships (wulun)

- **Citation.** *Mencius* 3A.4 (Teng Wen Gong I.4): 父子有親，君臣有義，夫婦有別，長幼有序，朋友有信; D. C. Lau (Penguin, 1970): "love between father and son, duty between ruler and subject, distinction between husband and wife, precedence of the old over the young, and faith between friends". Text confirmed in validation from knowledge of the standard translation. The term *wulun* (五倫) is later than Mencius. Secondary: https://en.wikipedia.org/wiki/Three_Fundamental_Bonds_and_Five_Constant_Virtues ; Lapham's Quarterly entry (as reported by search) giving the pairs and virtues; Kenyon College note comparing D. C. Lau's translation of 3A.4 with the 1890 Japanese Imperial Rescript, https://www2.kenyon.edu/Depts/Religion/Fac/Adler/Reln275/5%20Relations.htm . (The Wikipedia page URL "Five_Relationships" returned 404.)
- **Vocabulary.** Five dyads, each with a paired virtue (per Lapham's, as reported): father-son (love/affection), ruler-subject (righteousness), husband-wife (difference/distinct roles), elder-younger brother (seniority/order), friend-friend (trust). Friendship is the only non-hierarchical, non-kin one. The Three Bonds (ruler-minister, father-son, husband-wife) are a later (Han) subset credited to Dong Zhongshu. The virtue assignments differ across sources and eras (the Kenyon page shows loyalty/filial piety/harmony reassigned in the 1890 Rescript), so the table is a historical variable, not a fixed lookup.
- **Operands.** Persons occupying roles in a dyad.
- **Operators (translated).** Not actions but the *obligation attached to a role-pair*: the ordered pair (A, B) fixes what each owes. Mencius gives one virtue per *relation*, not a duty per party; the "ten duties" (十義: father kind / son filial, elder brother good / younger respectful, husband righteous / wife obedient, elder kind / junior docile, ruler benevolent / minister loyal) come from the *Liji* (Liyun chapter), whose five pairs differ from Mencius's (no friends). Asymmetrical in rank throughout. Formality: a lookup table of role-pair -> duty. This is already a role-relation table, which is what the owner asked about.
- **Predictive/control claim.** Normative: social order follows when each role-pair performs its duties.
- **Limits.** Closed list of five; no composition (what if a person holds two roles in conflict?); duties not conditional on conduct in the simplest reading.
- **Relevance.** A direct template for the *role-pair table* part of the algebra: (role_a, role_b) -> {duty_a, duty_b}. The open problem it exposes is role conflict, i.e. what a product of two role-pairs on the same person means.

---

## What this cluster already covers

- **An inventory of moves,** and a good one, especially in the triad chapter of Simmel and in Kautilya, Sun Tzu and Machiavelli.
- **Typing of relations:** similarity vs complementarity (Durkheim), five role-pair obligations (wulun), natural enemy/ally by position (mandala), directed obligation (Gilbert), dependence (Emerson).
- **Preference/cost orderings of operators:** upayas, Sun Tzu's ranking of attacks, Machiavelli's reliability of fear vs love.
- **Operator parameters:** legitimation basis (Weber), mode strategic vs communicative (Habermas), meaning/reading by the target (Mead/Blumer).
- **Conserved or typed flows:** media (Parsons), rewards (Homans), recognition (Hegel/Honneth).
- **A few precise constraints:** aggregation impossibility (List & Pettit), Gilbert's create/dissolve rules for joint commitment.
- **Noise and thresholds:** friction and culminating point (Clausewitz).

## What it does not

- **No composition.** Nothing says what happens when you apply two operators in sequence, or what the identity, inverse or commutator is. Kautilya says "try in order" and nothing more. This is the central gap.
- **No closed algebra.** No set of operands closed under the operators; no axioms; no theorems except List & Pettit, who study aggregation not moves.
- **Mostly dyad/triad, or macro.** Simmel stops at three and a few larger groups; Parsons, Comte and Durkheim work at system scale. Almost nothing treats n-party operator application with variable group structure.
- **Few first-class states.** Operands rarely have a defined state vector (Homans and Emerson are exceptions); most work with roles/types.
- **No dynamics with verification.** Predictions are prescriptive or normative rather than tested against data; the exception is the exchange tradition (and Quetelet's statistics).
- **Operator effects are rarely specified.** "Divide" or "recognise" are named but their pre/post conditions are not given (again except Homans and Gilbert).
- **Individuals vs groups.** Luhmann removes persons; Quetelet and Comte aggregate; analytic ontology takes groups as agents without a calculus.
- **Role conflict and multi-membership** are unaddressed (wulun, Parsons).

---

## Consolidated list of distinct operators (a move one party makes on another)

Deduplicated; source in brackets; grouped for readability only.

**Relational / structural**
1. Mediate / hold together (Simmel non-partisan)
2. Arbitrate (Simmel)
3. Exploit an existing conflict between two (Simmel tertius gaudens; corrected in validation from "broker / gatekeep, profiting from separation", which is Burt's 1992 reading, not Simmel's)
4. Play off / let two compete for one's favour (Simmel; the active sub-form of tertius gaudens, so a special case of 3)
5. Incite conflict / divide: create a conflict between two previously united (Simmel divide et impera ~ Kautilya bheda; differs from 3 in that the conflict is made, not found)
6. Add a third; remove a member (Simmel dyad<->triad)
7. Isolate from allies / prevent junction of forces (Sun Tzu; overlaps 5 when done by sowing dissension)

**Influence and exchange**
8. Conciliate (Kautilya sama)
9. Give / induce (Kautilya dana; Blau give; Homans reward)
10. Coerce (Kautilya danda; Machiavelli force)
11. Punish (Homans)
12. Instil fear (Machiavelli; the threat form of 10)
13. Win love / goodwill (Machiavelli)
14. Reciprocate (Homans, Blau)
15. Incur / create obligation by unreciprocated giving (Blau; the original list also credited Gilbert, whose joint commitment is 41)
16. Withhold reward (Homans, Blau; denial of recognition is 37)
17. Avoid dependence: substitute another supplier, or forgo the need (Blau's alternatives, Emerson's balancing operations)
18. Command / obey under a legitimation basis (Weber)
19. Repress (penal sanction) / restore (restitutive sanction) (Durkheim; repress overlaps 11)
20. Subordinate / superordinate (Simmel forms of sociation; also Blau: subordinate oneself when no alternative to dependence exists; overlaps 38)

**Foreign-policy relations (between parties)**
21. Make peace / treaty (sandhi)
22. Make war / hostility (vigraha)
23. Stay neutral (asana)
24. Advance / march (yana)
25. Shelter under a stronger (samshraya)
26. Dual policy (dvaidhibhava; composite of 21 on one party and 22 on another)

**Information and meaning**
27. Thwart plan (Sun Tzu)
28. Infiltrate / turn an agent (Sun Tzu converted/inward spy)
29. Feed false information / deceive (Sun Tzu doomed spy; Machiavelli, *Prince* ch. 18)
30. Scout / gather intelligence (Sun Tzu local, surviving spy)
31. Gesture and response; adopt the other's attitude (role-take) (Mead)
32. Interpret / redefine meaning (Blumer)
33. Assert, request/command, express (Habermas speech-act types; request/command overlaps 18)
34. Accept or reject a validity claim (Habermas)
35. Communicate, i.e. connect an event to a prior event (Luhmann)
36. Apply one's own code to another system's operation (Luhmann)

**Recognition and joint action**
37. Recognise / deny recognition (Hegel, Honneth); denial typed by sphere: maltreat, deny rights, denigrate (Honneth)
38. Submit (Hegel)
39. Struggle / resist (Honneth)
40. Encounter (I-Thou) / objectify (I-It) (Buber; a stance rather than a move, by Buber's own account, so better treated as an operator parameter)
41. Express readiness to be jointly committed (Gilbert)
42. Concur in release from commitment (Gilbert)
43. Rebuke for breach (Gilbert)
44. Mesh plans / form shared intention (Bratman)

**Aggregation and collective**
45. Aggregate judgements into a group judgement (List & Pettit)
46. Specialise / differentiate roles (Comte, Durkheim)
47. Exchange media between subsystems (Parsons)

**Combat-specific (engage/defend)**
48. Attack, defend, concentrate force, besiege (Sun Tzu, Clausewitz)
49. Arm citizens vs hire mercenaries (Machiavelli; a move on one's own constituents, not on another party, so it fails the list's own definition and is kept only as an internal-organisation operator)

**Validation note on the list.** No operator was invented: each traces to its source. But the 49 are not all distinct: 4 is a case of 3; 12 of 10; 26 composes 21 and 22; 11/19, 18/33, 20/38 and 5/7 overlap. A cleaner count of independent moves is about 40. Lines 6, 33, 37 and 48 each bundle several operators.

**Parameters on operators (not operators themselves)**: legitimation basis (Weber), strategic vs communicative mode (Habermas), cost and reliability (Kautilya, Machiavelli), friction and culminating point (Clausewitz), how the target reads the move (Mead).

---

## Unconfirmed (not asserted above)

Revised in validation, 2026-10-29. Items the original pass listed here and that are now resolved (Parsons's pattern variables, Homans's six propositions, Blau on power from unreciprocated exchange, Honneth's forms of disrespect, Luhmann's information/utterance/understanding, Bratman/Gilbert/Tuomela primary works, *saptanga*, Mencius 3A.4, Weber's types and "social relationship", Simmel's triad text, the Habermas SEP authors) have been folded into the entries above with sources. What remains:

- **The exact verse in the *Arthashastra* stating that each earlier upaya is lighter** (Book 9 by standard reading): the ordering is not in doubt, the locus is unchecked against Kangle or Olivelle.
- **Sun Tzu's *shi*, deception as a chapter-level concept, and the Griffith/Ames wording:** not read; the Giles quotations are from Wikisource.
- **Weber page numbers** (pp. 4, 24-28, 215 of Roth & Wittich) are from the validator's knowledge of the edition, not from a scan.
- **Habermas's death date (2026)** as given on the SEP page post-dates the validator's knowledge; it is reported, not confirmed.
- **SEP revision dates for Recognition (27 Jul 2026) and Buber (12 May 2026)** read from the live pages; not independently checkable.

## Missing work worth adding

- **Emerson 1962** (added to entry 8): the primary power-dependence paper, with the four balancing operations (withdrawal, network extension, status-giving, coalition formation), which are explicit operators on a dependence relation.
- **Caplow, T., *Two Against One: Coalitions in Triads* (Prentice-Hall, 1968)** and "A Theory of Coalitions in the Triad", *American Sociological Review* 21 (1956): the direct formalisation of Simmel's triad by power distribution, predicting which coalitions form. The nearest thing to a calculus on Simmel's operands.
- **Burt, R. S., *Structural Holes* (Harvard UP, 1992):** the source of the "broker" reading of tertius gaudens; covered by the network survey, but the attribution belongs here.
- **Goffman, E., *The Presentation of Self in Everyday Life* (1956/1959) and *Interaction Ritual* (1967):** face-work, deference and demeanour as a finite move-set at the micro level; a striking gap given Mead and Blumer are included.
- **Hobbes, *Leviathan* (1651):** authorisation and covenant as the operator that makes a group agent; the classical ancestor of List & Pettit.
- **Searle, J., *The Construction of Social Reality* (Free Press, 1995):** "X counts as Y in C" and status functions; the most algebra-shaped formula in social ontology.
- **Schelling, T. C., *The Strategy of Conflict* (Harvard UP, 1960):** threats, promises, commitment, focal points; the modern formal heir of the statecraft cluster (may be covered by the economics survey).
- **Han Feizi** (the "two handles", reward and punishment, *Han Feizi* ch. 7): the Chinese statecraft counterpart to Kautilya's upayas and to Homans.

## Validation log (2026-10-29)

- Simmel / Wolff 1950: ✎ corrected. Pages 145/154/162 confirmed from the full djvu text; dyad chapter range fixed (118-144); **tertius gaudens was misdescribed as "keeps two apart / gatekeep / broker"** (Burt's reading). In Simmel the third profits from a conflict already there; divide et impera is the case where the third makes it. Mediator vs arbitrator distinction added from the text.
- Nooteboom 2006: ✓ (DOI resolves).
- Comte / Bourdeau SEP: ✓ (dates confirmed on the live page).
- Quetelet, Beirne 1987, Grue & Heiberg 2006: ✓.
- Durkheim 1893: ✓ (no SEP entry exists, as stated).
- Weber: ✎ four action types and "social relationship" sourced to *Economy and Society* §§2-3; authority p. 215. SEP Kim dates ✓.
- Parsons: ✎ five pattern variables confirmed and moved out of Unconfirmed; Parsons & Shils 1951 added. AGIL media ✓.
- Homans: ✎ six propositions (aggression-approval, rationality) confirmed from the 1974 edition; 1958 citation completed; activities/interactions/sentiments reattributed to *The Human Group*.
- Blau / Emerson: ✎ Blau's power-from-unreciprocated-exchange restored (standard, ch. 5); Emerson 1962 primary paper added.
- Mead, Blumer: ✓.
- Luhmann: ✎ "peace" as a medium was wrong (truth, love, money, power); information/utterance/understanding confirmed; Spencer-Brown wording fixed.
- Habermas: ✎ SEP authors (Finlayson & Rees, 2023) supplied; the "wrong life dates" suspicion withdrawn. Content ✓.
- Hegel / Honneth / Iser SEP: ✎ disrespect forms confirmed and added; revision date and translator added; "fixed point" relevance claim marked as interpretation.
- Buber / SEP: ✎ authors (Zank & Braiterman) added; otherwise ✓.
- Gilbert, Tuomela, Bratman / Roth SEP: ✎ primary works confirmed (DOIs for Bratman 1993 and Gilbert 1990); Bratman's conditions restated (interlocking intentions, meshing sub-plans, common knowledge; "bridge intention" removed); Tuomela's we-mode supplied.
- List & Pettit: ✓ (both DOIs resolve; theorem's conditions stated precisely; Synthese issue is 140(1-2)).
- Kautilya: ✎ Kangle dates fixed (translation 1963, not 1969); Shamasastry book 1915; upapradana noted; **madhyama/udasina descriptions swapped back** (udasina is the stronger one, and both are inside the 12-king circle); 12 kings named; shadgunya order confirmed as the text's; saptanga added. Upaya ordering ✓, verse locus ?.
- Sun Tzu: ✎ III.3 ranking ✓ with 伐交 translation note; publishers added; **"Kautilya's order run backwards" was wrong** (both put force last).
- Machiavelli / Nederman SEP: ✎ deception sourced to *Prince* ch. 18; otherwise ✓.
- Clausewitz: ✎ Howard & Paret 1976 first edition; book/chapter loci added. p. 87 ✓.
- Confucian five relationships: ✎ Mencius 3A.4 text and Lau translation confirmed; "ten duties, two per relation" reattributed to the *Liji*, whose list differs.
- Operator list: ✎ no fabrications; one misattribution fixed (3), one double-credit removed (15), recognition duplicate removed (16), overlaps and non-operators (40, 49) flagged; about 40 independent moves, not 49.
- Removed: ✗ none.

**Verdict.** Bibliographically sound: every cited work exists with correct authors and essentially correct dates, and no operator was invented. The errors were in content, and three would have shaped the algebra: tertius gaudens read as brokerage (which erased the found-vs-made conflict distinction that separates it from divide et impera), the madhyama/udasina power relation inverted, and Sun Tzu's ordering said to oppose Kautilya's when it agrees. Several "Unconfirmed" items were standard and are now resolved; use the corrected entries, and treat the closing verdict (no composition, no closed algebra) as accurate.
