# Prior work 26: philosophical and classical theories of the passions and their composition

Date: 2026-10-29. Survey for the social-algebra strand. Cluster: the long tradition that tried to derive the passions from a few primaries and state their laws.

**Context.** Aim (Aldred): an algebra of basic human and group drives (curiosity, fear, desire) that compose into equations, then theorems, then prediction or control. This file asks who already tried to derive the many passions from a few, and in what form. Classical social and political theory is in `11-classical-theory-statecraft.md` and is not repeated; modern taxonomies and the core set are in `15-drive-taxonomies.md`; formal models in `16`; curiosity, fear, desire in `17`; group emotion in `18`.

**Method note.** Tags: **[read]** = text seen at a source page this session; **[from abstract/standard account]** = from the standard scholarly account as I know it, not checked against the primary text. Read this session, and only these: Spinoza's *Ethics* Part III in the Elwes translation (Project Gutenberg #3800; fragmentary: the fetch tool returned selected propositions and affect definitions, not the Postulates or Definitions 1-3); Hobbes, *Leviathan* ch. 6 (Gutenberg #3207; quoted passages); the SEP entry on Descartes's ethics (a secondary summary only). Everything else is from memory of the standard account. Note the Elwes translation says "pleasure/pain" where modern translators say "joy/sadness" (*laetitia/tristitia*).

**Validation pass (2026-10-29).** A second agent downloaded and read the primary texts in full: Spinoza *Ethics* (Elwes, Gutenberg #3800: Part III definitions, postulates, propositions 6-46 with proofs, the 48 Definitions of the Affects, E4p7); Hobbes *Leviathan* ch. 6 (Gutenberg #3207, the whole chapter); Descartes *Passions of the Soul* Parts 2 and 3 (Bennett, earlymoderntexts.com); Hume *Treatise* Book II (Gutenberg #4705, the section headings, T 2.1.1 and 2.2.5); Smith *TMS* (Gutenberg #67363, I.i.4 and I.ii.3-5); Aristotle *Rhetoric* II.1-11 (Rhys Roberts, classics.mit.edu); Diogenes Laertius 7.110-116 (Wikisource, via a summarising fetch); Bentham *IPML* chs. IV-V (econlib, via fetch); SEP "Johann Friedrich Herbart". Items so checked now carry **[read]**; corrections are marked "(corrected)" and listed in the validation log at the end. Sections 14-17 (Hutcheson, Bentham, Herbart, Wolff) were added by the validation pass.

**Headline.**

1. Spinoza's *Ethics* Part III is the closest precedent in the *axiomatic* form Aldred wants: definitions, postulates, numbered propositions with proofs, and a closing catalogue of 48 affects each defined from three primaries [read]. It is not the only precedent for a *formal* treatment of the passions (corrected): Hutcheson (1725) wrote algebraic formulas for moral quantities, Bentham (1789) gave dimensions for measuring a pleasure and tables of simple pleasures and pains, Herbart (1816, 1824-25) wrote actual equations for the rise and fall of ideas and derived feeling and desire from them, and Wolff (1732-34) treated the mind in a deductive, numbered method with a programme of "psychometria". See sections 14-17. It is axiomatic in presentation, but the proofs lean on informal association and on "the nature of the mind", so it is a quasi-formal system, not a checkable one. It also contains a social-transmission law (E3p27) and laws that compose affects (love = joy + idea of external cause).
2. Nearly every other tradition is classificatory: lists of primaries plus a rule or two for compounding. The notable rule-bound ones are the Abhidharma (co-occurrence tables of mental factors), rasa theory (a grammar of cause, sign and transient factor yielding a flavour) and Hobbes (compound definitions by conjunction: fear = aversion + opinion of hurt).
3. A convergent core recurs across all of them: a desire/aversion pair (approach/avoid), a pleasure/pain pair (joy/sadness), and a cognitive qualifier that turns the bare pair into a named passion (object present or future, belief in attaining it, an external cause, a social other). That is the structure the algebra could adopt: two or three primaries, plus operators that attach an object, a time and a person.
4. Nobody in this tradition states anything in the form of theorems about groups that can be tested. Spinoza states laws and derives corollaries, none quantified. Quantification was attempted, but outside the passions-catalogue tradition and not for groups: Bentham's felicific dimensions (summed over persons, the nearest thing to a group aggregate) and Herbart's equations of ideas (individual only). (corrected)

---

## 1. Spinoza, *Ethics* Part III (1677): the key precedent

**Citation.** Spinoza, B. *Ethica ordine geometrico demonstrata* (1677), Part III, "On the Origin and Nature of the Affects". Translation read: R. H. M. Elwes (1883), Gutenberg #3800. Standard modern translation: Curley (Princeton, 1985). Secondary: SEP "Spinoza's Psychological Theory" (not read). [read, validation pass: Part III Definitions 1-3, Postulates 1-2, propositions 6-46 with proofs and scholia, all 48 Definitions of the Affects]

**Primaries.** Three, stated as such in E3p11s: "beyond these three I recognize no other primary emotion; I will show as I proceed, that all other emotions arise from these three" [read].
- **Desire** (*cupiditas*): "the actual essence of man, in so far as it is conceived, as determined to a particular activity by some given modification of itself" (Def. of Affects 1; the survey's quotation dropped the last clause, which Spinoza's explanation says is the point of the definition) (corrected) [read]. Rooted in the *conatus*: each thing "endeavours to persist in its own being" (E3p6) and this endeavour "is nothing else but the actual essence of the thing" (E3p7). Desire is "appetite with consciousness thereof" (E3p9 scholium).
- **Joy** (*laetitia*): "the transition of a man from a less to a greater perfection" (Def. 2; Elwes: "pleasure").
- **Sadness** (*tristitia*): "the transition ... from a greater to a less perfection" (Def. 3; Elwes: "pain").

Two things to notice. The three are not on a par: desire is the standing quantity (power of acting), joy and sadness are signed changes in it. So the primaries are a state and its derivative, which is already an algebraic shape (a level and its sign of change). And "perfection" is the same thing as power of acting, which gives the system one scalar.

**Derivation structure.** The method is the geometrical one: definitions, axioms and postulates, then propositions each with a proof citing earlier items. In Part III the moves that matter are:

| Rule | Statement (paraphrase, with proposition) | Algebraic reading |
|---|---|---|
| Conatus | Each thing strives to persist (p6, p7) | The ground drive; invariant |
| Valence | Joy/sadness are changes in power of acting (p11) | Signed increment on a scalar |
| Direction | The mind strives to imagine what raises the body's power (p12) and to remember what excludes what lowers it (p13) | Selection: attention is biased by valence |
| Love/hate | Love = joy + idea of an external cause; hate = sadness + idea of an external cause (Defs. 6, 7; p13s) [read] | A composition: affect (x) cause-idea |
| Association | If the mind has once been affected by two affects at once, then whenever it is afterwards affected by one it is also affected by the other (p14) [read] (added) | Co-occurrence becomes a link |
| Accidental cause | Anything can be accidentally a cause of joy, sadness or desire (p15) [read] | Association: any object can be attached |
| Similarity | A thing similar to a cause of joy/sadness is loved/hated (p16) [read] | Transfer along a similarity relation |
| Ambivalence | An object tied to both joy and sadness is loved and hated at once, a "fluctuation of mind" (p17) [read] | Superposition of opposite signs, not cancellation |
| Imitation | Imagining a thing like us, towards which we had no affect, to be affected, we are affected alike; but if we hate it, we are affected by a *contrary* affect (p27 and its proof) [read] (corrected: the sign-flip clause was missing) | Transmission over a similarity relation, with the sign set by the prior relation (neutral: copy; hate: invert) |
| Striving to produce | We endeavour to bring about what we imagine conduces to joy, and to remove or destroy what we imagine conduces to sadness (p28) [read] | Desire follows valence |
| Reinforcement | If we imagine another loves, desires or hates what we love, desire or hate, our affect becomes "more steadfast"; if another shrinks from what we love, we vacillate (p31) [read] | Social amplification, or ambivalence on disagreement |
| Jealousy | Imagining a loved object joined to another "with closer bonds of friendship than he himself has attained" gives hatred of the object and envy of the rival (p35) [read] (corrected: not "equal or stronger") | Conflict from a shared scarce object |
| Retaliation | One who hates tries to harm, "unless he fears that a greater injury will thereby accrue to himself" (p39); one who believes himself hated without cause hates back (p40); hatred is increased by being reciprocated and can be destroyed by love (p43) [read] (corrected: p39's fear condition and p43 added) | Reciprocity law with a deterrence guard; a feedback loop that love can break |
| Extension to classes | Love/hate for a stranger of a class we associate with a class affect (p46) [read] | Transmission from individual to group |

After the propositions come the *Definitions of the Affects*, numbered I to XLVIII: 48 [read], ending with lust. Examples [read]: hope = "an inconstant pleasure, arising from the idea of something past or future, whereof we to a certain extent doubt the issue" (Def. 12); fear = the same with pain (Def. 13), and Spinoza draws the corollary that "there is no hope unmingled with fear, and no fear unmingled with hope"; pity = pain accompanied by the idea of evil befallen someone we conceive to be like ourselves (Def. 18; cf. p22s, p27s) (corrected: the definition is Def. 18, not p22); emulation = "the desire of something, engendered in us by our conceiving that others have the like desire" (Def. 33; p27s1). Each is a defined combination of: a primary, a time, a doubt, an object, a person.

**Social transmission.** E3p27, "imitation of the affects": if we imagine a thing like us, towards which we had no affect, to be affected by some affect, we are ourselves affected by a like affect [read: "we are ourselves affected with a like emotion"]. The scholium names imitation of pain compassion and imitation of desire emulation; Cor. 1 gives love or hate towards whoever pleases or pains a thing like us; Cor. 2 says we cannot hate what we pity [read]. Benevolence (Def. 35), ambition (Def. 44) and honour (Def. 30) are defined in the catalogue [read]; their derivation from p27 in p29-p32 is from the standard account. This is the most direct precedent for "drives of groups from drives of persons" in the whole tradition: similarity is the channel, valence is the payload. Combined with p31 and p46 it gives a small theory of how affect spreads and polarises.

**Formality.** The most formal item in this file, but be careful. [from abstract/standard account] Commentators (Bennett 1984, *A Study of Spinoza's Ethics*; Della Rocca; Curley) agree that the proofs invoke the psychophysical parallelism, definitions of "adequate cause" and unstated associationist principles; some propositions (the imitation law among them) are widely held to be weakly derived. So: axiomatic in form, informal in rigour, never quantified. It states laws and corollaries; it does not give measurable parameters.

**Operand/operator translation.** Operands: persons (modes), objects (ideas of external causes), a signed scalar (power of acting). Operators: *attach cause* (turn joy into love), *transfer by similarity* (p16), *imitate* (p27, person to person), *combine* (hope = joy x doubt), *oppose* (p17, p35). Joy and sadness are increments; desire is the level.

**Borrowable as axioms.** (a) A conative ground quantity per agent (conatus). (b) Joy and sadness as signed increments on it. (c) Love/hate as affect composed with a cause-idea. (d) Imitation as transmission across a similarity relation. (e) Fluctuation as superposition rather than sum. (f) Desire follows the sign of the expected change. All six are directly stateable in a typed algebra.

**Gap.** There is no explicit curiosity or fear primary; fear is derived (inconstant sadness). Wonder (*admiratio*) is defined as a conception in which "the mind comes to a stand" because the concept has no connection with others, and Spinoza says "I do not include wonder among the emotions" (Def. of Affects 4 and explanation) [read]. Fear would be a derived term, curiosity roughly desire attached to an unresolved cause-idea. That fits the algebra's wish to treat curiosity, fear and desire as compounds if needed.

## 2. Hobbes, *Leviathan* ch. 6 (1651) [read, ch. 6 passages]

**Primaries.** Endeavour toward or from an object. Toward it: **appetite or desire**; from it: **aversion**. "That which men Desire, they are also sayd to LOVE"; hate is aversion, the difference being that desire and aversion signify the object's absence, love and hate its presence. **Joy** and **grief** are pleasures and displeasures of the mind arising from expectation of consequences. Hobbes names the set explicitly: "These simple Passions called Appetite, Desire, Love, Aversion, Hate, Joy, and griefe" — seven names, of which appetite and desire are one passion, so effectively six. [read]

**Derivation.** Compound definitions by conjunction, stated exactly in the text [read]: hope = appetite with an opinion of attaining; despair = the same without it; fear = aversion with opinion of hurt from the object; courage = fear with hope of avoiding the hurt by resistance; anger = sudden courage. Curiosity: "Desire, to know why, and how, CURIOSITY; such as is in no living creature but Man." Admiration = "Joy, from apprehension of novelty ... because it excites the appetite of knowing the cause" (added). Deliberation is the alternation of appetites, aversions, hopes and fears about one thing; "In Deliberation, the last Appetite, or Aversion, immediately adhaering to the action, or to the omission thereof, is that wee call the WILL" (corrected: the survey's "last appetite in deliberating" is Hobbes's own gloss, and the definition includes the last aversion) [read].

**Social mechanism.** (corrected: the survey said "Not in ch. 6" and "no transmission law"; wrong.) Ch. 6 defines **panic terror** as "Feare, without the apprehension of why, or what", and explains it socially: "there is always in him that so feareth, first, some apprehension of the cause, though the rest run away by example; every one supposing his fellow to know why. And therefore this Passion happens to none but in a throng, or multitude of people" [read]. That is a transmission law for fear in a crowd, with the object dropped in transit: one agent has fear-of-x, the rest acquire fear-of-unknown by imitation plus an assumption about the first agent's knowledge. Fear also enters the state-of-nature argument (chs. 13 and following; see `11`) as the passion that drives men to covenant.

**Formality.** Classificatory with a definite grammar: a base (appetite or aversion), plus modifiers (opinion of attaining, opinion of hurt, hope of resisting). Short, clean, and directly translatable.

**Operand/operator.** Operand: an endeavour with object and sign. Modifiers as operators: `opine-attain`, `opine-hurt`, `add-hope`. Courage = hope(fear(x)) is a literal composition.

**Borrowable.** (a) Curiosity as desire-to-know: a desire with an epistemic object, and admiration (joy at novelty) as what excites it. (Corrected: the survey called this "the only classical definition of curiosity ... that reduces it to desire"; Descartes art. 88 says the same, "Curiosity ... is nothing but a desire for knowledge", and Hume has a section "Of curiosity, or the love of truth", T 2.3.10 [read].) (b) Fear as aversion with an opinion of hurt. (c) The idea that a named passion is a primary plus a belief. (d) Will as the terminal state of a deliberation sequence (the last element, not strictly a fixed point). (e) Panic as crowd transmission of fear with the object lost.

## 3. Descartes, *The Passions of the Soul* (1649)

**Citation read (validation pass).** Bennett's version, earlymoderntexts.com, Parts 2 and 3 (212 articles, numbering Descartes's).

**Primaries.** Six "simple and basic": wonder, love, hatred, desire, joy, sadness (art. 69) [read]. Wonder is "the first of all the passions" because it can happen "before we know whether the object is beneficial to us", and it "has no opposite" (art. 53) [read]; esteem and contempt are species of wonder (art. 54). Wonder alone involves no change in heart or blood, because it carries no value-judgement (art. 71) [read].

**Derivation.** Art. 69: "All the others are either composed from some of these six or they are species of them" [read] (corrected: the survey left this as unknown). Desire, the forward-looking passion (art. 57), divides by estimated likelihood: a good chance gives hope, a poor one anxiety (of which jealousy is a variety); extreme hope becomes confidence, extreme anxiety despair (art. 58) [read; the article numbers 57-58 are confirmed]. Art. 87: desire "has no opposite" — the Schools' "aversion" is the same movement as desire, seen from the evil avoided rather than the good pursued, accompanied by hatred, anxiety and sadness instead of love, hope and joy [read]. Art. 88: desire has as many kinds as it has objects; "Curiosity ... is nothing but a desire for knowledge" [read]. Part 3 (arts. 149-210) then treats the particular passions as species or compounds. The number of named passions (the SEP's "about forty") was not counted here. Physiological account: animal spirits and the pineal gland.

**Social mechanism.** (corrected) Part 3 treats many other-directed passions — pity (arts. 185-189), gratitude, indignation, envy, glory and shame — but as passions of one soul about another person; there is no rule by which one person's passion produces another's. The survey's "Art. 187ff treat the passions of one soul" mis-cited articles that are in fact about pity.

**Formality.** Classificatory with a mechanistic backing.

**Borrowable.** Wonder as an unvalenced primary that precedes appraisal: the response to the novel before it is classified as good or bad. Curiosity itself is a species of *desire* (art. 88), triggered by wonder. That is a useful architectural point: curiosity needs an unvalenced trigger plus a desire with an epistemic object. Second: art. 87's single desire with a sign (pursue good / avoid evil as one movement) is an argument for one signed approach operator rather than separate approach and avoidance primaries.

## 4. Hume, *Treatise of Human Nature* Book II (1739-40)

**Primaries and classification.** Passions are impressions of reflection. T 2.1.1 [read]: direct passions "arise immediately from good or evil, from pain or pleasure" — "desire, aversion, grief, joy, hope, fear, despair and security"; indirect ones "proceed from the same principles, but by the conjunction of other qualities" — "pride, humility, ambition, vanity, love, hatred, envy, pity, malice, generosity, with their dependants". Book II's structure (Part I pride and humility, Part II love and hatred, Part III the will and direct passions) makes pride, humility, love and hatred the four core indirect passions [read: section headings].

**Derivation rule.** The **double relation of impressions and ideas**: pride is produced when an object that causes pleasure (an impression similar to pride) is related by association of ideas to oneself (the object of pride). Two parallel associations, one of feeling by resemblance, one of idea by contiguity, causation or resemblance, jointly cause the indirect passion. This is the clearest example in the tradition of a rule that generates a passion from an object, an owner and a valence. It is a sort of tensor: (quality-valence) x (relation-to-owner). [the phrase "double relation of impressions and ideas" read at several places in Book II; the mechanism as summarised is the standard account]

**Social mechanism.** **Sympathy** (main treatment T 2.1.11, "Of the love of fame"; section title read): the idea of another's passion, inferred from signs, is enlivened into the passion itself by the vivid idea of self, as the other resembles us [standard account]. T 2.2.5 ("Of our esteem for the rich and powerful") [read, location confirmed]: "the minds of men are mirrors to one another, not only because they reflect each others emotions, but also because those rays of passions, sentiments and opinions may be often reverberated, and may decay away by insensible degrees." Hume's example is a loop: the rich man's pleasure produces esteem in the beholder, which the rich man sympathises with, which increases his pleasure, which is "once more reflected" to the beholder. (added) So Hume's sympathy is not only one-way transmission: it is an iterated two-way reflection with damping, i.e. a convergent feedback series. Resemblance, contiguity and causation raise its strength [standard account].

**Formality.** Aims at a "Newtonian" science of man with laws of association. Not axiomatic; no derivations in proof form.

**Borrowable.** (a) Double relation: indirect passion = valence x relation to self. (b) Sympathy strength as a function of resemblance and proximity: gives a real-valued transmission operator. (c) Reverberation: affect reflected back and forth between two agents with decay per pass, a geometric-series feedback whose sum is a stable amplified level.

## 5. Adam Smith, *The Theory of Moral Sentiments* (1759)

**Primaries.** Smith classifies passions as unsocial (hatred, resentment), social (generosity, humanity, kindness) and selfish, which "holds a sort of middle place": "Grief and joy, when conceived upon account of our own private good or bad fortune" (TMS I.ii.3-5) [read]. Not derived from a few primaries.

**Mechanism.** **Sympathy**: chiefly an imaginative exchange of situations rather than contagion: we feel what we imagine we would feel in the other's place [standard account]. The spectator's feeling "will still be very apt to fall short"; the sufferer, wanting "entire concord", "can only hope to obtain this by lowering his passion to that pitch, in which the spectators are capable of going along with him. He must flatten ... the sharpness of its natural tone"; and the spectators in turn assume his circumstances. The result is not identity: "Though they will never be unisons, they may be concords, and this is all that is wanted or required" (TMS I.i.4.7-8) [read]. The **impartial spectator** as the internalised judge [read: phrase; development in Part III from the standard account]. Propriety is the level at which spectator and agent can meet (corrected typo "Proprietary").

**Formality.** Descriptive; but sympathy is an explicit two-sided adjustment of sentiment toward a mutually acceptable level: agent lowers, spectator raises, and they settle at concord, not equality. This is a coordination structure with an equilibrium; "fixed point" is fair as a reading, with the caveat that Smith's endpoint is a band of compatibility, not a single value.

**Borrowable.** Sympathy as a bidirectional adjustment operator converging to propriety. (Corrected: the survey contrasted this with "Spinoza's and Hume's one-way transmission"; Hume's mirrors passage is a two-way reverberating loop, and Spinoza's p31, p40 and p43 are reciprocal loops. What is distinctive in Smith is that both parties *move toward each other* by choice to reach agreement, rather than amplifying.) Useful for modelling mutual calibration of affect in a group.

## 6. Aristotle, *Rhetoric* II.1-11 (4th c. BCE)

**Citation read (validation pass).** Rhys Roberts translation, Book II chs. 1-11, classics.mit.edu.

**Primaries.** None as such. Emotions are "all those feelings that so change men as to affect their judgements, and that are also attended by pain or pleasure" (II.1) [read]. About fifteen are analysed, mostly in opposed pairs: anger and calmness (II.2-3), friendship and enmity (II.4), fear and confidence (II.5), shame and shamelessness (II.6), kindness and unkindness (II.7), pity (II.8), indignation (II.9), envy (II.10), emulation, with contempt as its opposite (II.11) [read].

**Derivation.** Each emotion is analysed under three heads: "(1) what the state of mind of angry people is, (2) who the people are with whom they usually get angry, and (3) on what grounds" — and "unless we know all three, we shall be unable to arouse anger in any one" (II.1) [read]. Anger is "an impulse, accompanied by pain, to a conspicuous revenge for a conspicuous slight directed without justification towards what concerns oneself or towards what concerns one's friends", and so always towards a particular individual (II.2) [read]. Fear is "a pain or disturbance due to a mental picture of some destructive or painful evil in the future", and only if near enough to seem imminent (II.5) [read]. This is the first structure of emotion as (belief + valence + target + conative tendency).

**Social mechanism.** Emotions toward others (friend/enemy, superior/inferior) are the whole point of the exposition, aimed at persuading an audience. It is a manual for evoking emotions in groups.

**Formality.** Classificatory with a consistent template.

**Borrowable.** The template: an emotion type = (belief schema, valence, target role, tendency). Oppositional pairs as an involution (anger/calming).

## 7. The Stoics (Zeno, Chrysippus; 3rd c. BCE onward)

**Primaries.** Four genera of passion (*pathe*): **appetite/desire** (*epithumia*), **fear** (*phobos*), **pleasure** (*hedone*), **distress** (*lupe*). Distress and pleasure concern present things; appetite and fear future ones; appetite and pleasure concern an apparent good, fear and distress an apparent evil. A 2x2 grid: (good/evil) x (present/future). [The four genera read in Diogenes Laertius 7.110 via a summarising fetch of the Wikisource Yonge translation; the explicit 2x2 arrangement is the standard account (Stobaeus, Cicero *Tusc.* IV; Long & Sedley 65), not stated in DL.]

**Derivation.** Each genus has named subspecies defined by object and cause [read, DL 7.111-114]: under distress, pity (at undeserved suffering), envy, jealousy, rivalry, heaviness, annoyance, anguish, distraction; under fear, terror, shame (fear of disgrace), shrinking, consternation, panic, mental agony; under desire, want, **hatred**, contentiousness, **anger**, **love**, wrath, resentment; under pleasure, ravishment, malevolent joy, delight, transport. (Corrected: "grief" is the genus itself in some translations, not a subspecies; and note that love, hatred and anger are species of *desire*.) A passion is "an irrational and unnatural movement in the soul" (DL 7.110), an **excessive impulse** founded on a false judgement [standard account]. Good counterparts (*eupatheiai*, DL 7.116) [read]: joy (for pleasure), caution (for fear), wish (for desire); none for distress.

**Social mechanism.** Mostly absent; the passions are individual errors in judgement.

**Formality.** The cleanest classificatory grid in the tradition: two binary axes generating the four genera, with subspecies as refinements. Claims a *therapeutic* use (remove the false belief and the passion goes), the closest classical analogue of "control".

**Borrowable.** The 2x2: valence x time. Fear and desire are the future-evil and future-good cells; each an operator on a judgement. A passion is a function of one judgement, which suggests a minimal state: the set of active evaluative judgements.

## 8. Buddhist Abhidharma: cetasikas and the three poisons

**Primaries.** Three **unwholesome roots**: greed/attachment (*lobha*), hatred/aversion (*dosa*), delusion (*moha*), the "three poisons", with three wholesome opposites (non-greed, non-hatred, non-delusion). [from abstract/standard account]

**Derivation.** In the Theravada scheme (*Abhidhammattha-sangaha*, Anuruddha, 11th-12th c.) there are 52 mental factors (*cetasikas*): 7 universal to every consciousness (contact, feeling, perception, volition, one-pointedness, life faculty, attention), 6 occasional, 14 unwholesome, 25 beautiful. The system then lists **which factors can co-occur with which type of consciousness** (*citta*), as tables. The Sarvastivada has a different count (46 in six groups). [from abstract/standard account]

**Social mechanism.** Largely individual; dependent origination gives causal chains of craving to clinging to becoming. Group-level content appears in the Vinaya and monastic rules, not in the psychology.

**Formality.** Strongly rule-bound and enumerated: an explicit incidence relation between consciousness types and mental factors. Not mathematical but already a combinatorial table, which is closer to an algebra's operator table than most other items here. Unlike Western lists it ranks by wholesomeness, built in as a normative axis.

**Borrowable.** (a) Three roots as a minimal primary set: attraction (greed), repulsion (hatred), and a cognitive-clarity variable (delusion, i.e. misperception). Notice the third is epistemic and links to curiosity as its remedy. (b) The co-occurrence table: which drives may be simultaneously active, as a compatibility relation. (c) Universal factors: things always present in any state.

## 9. Indian rasa theory: Natyashastra (c. 200 BCE-200 CE), Abhinavagupta

**Primaries.** Eight **stayibhavas** (durable/dominant states): love/delight (*rati*), mirth (*hasa*), sorrow (*soka*), anger (*krodha*), energy/fortitude (*utsaha*), fear (*bhaya*), disgust (*jugupsa*), wonder (*vismaya*), each with an aesthetic flavour (*rasa*): erotic, comic, pathetic, furious, heroic, terrible, odious, marvellous. A ninth (peace, *shanta*) is added later: commonly credited first to Udbhata (8th c.) and defended at length by Abhinavagupta (10th-11th c.), who ties it to liberation (corrected: the survey credited Abhinavagupta alone). [standard account; secondary check via search, not a primary text]

**Derivation.** The famous sutra (Natyashastra ch. 6, v. 31; *vibhāvānubhāva-vyabhicāri-saṃyogād rasa-niṣpattiḥ*; quoted from the standard citation, the edition or translation consulted was not recorded this session): rasa results from the **combination** of determinants (*vibhava*, causes), consequents (*anubhava*, visible signs) and transitory states (*vyabhicaribhava*, 33 of them such as anxiety, jealousy, recollection). The sutra itself does not name the dominant state; its role as the "fixed" element is from Bharata's prose and the commentators. There are also 8 *sattvika bhavas* (involuntary bodily states such as trembling, tears), giving the classical total of 49 bhavas (8 + 33 + 8) (added). The image of transitory states passing through the dominant one like waves is a later commentarial gloss; the determinants and consequents are the cause and effect. Some rasas are said to arise from others (comic from erotic, pathetic from furious, and so on). [from abstract/standard account]

**Social mechanism.** The entire theory is about transmission from performer to audience: the spectator's emotion is generalised (*sadharanikarana*), de-personalised, so that it is enjoyed without private stakes. (Corrected: generalisation as a doctrine is Bhatta Nayaka's (c. 10th c.), known through Abhinavagupta's *Abhinavabharati*, which reworks it; it is not stated as such in the *Natyashastra*.) Not a model of contagion in groups but of mediated shared affect.

**Formality.** A **combination grammar**: rasa = f(dominant, determinant, consequent, transitory). The most explicit grammar for composition in the cluster other than Spinoza, and the only one with three roles (cause, sign, passing state) for each emotion. Entirely classificatory; no quantities.

**Borrowable.** (a) Separating the persistent drive (stayibhava) from the transient affects that flow through it. In the algebra: a slowly varying base state plus fast modulation. (b) The cause/sign/state triple as the type of an emotion event: what triggers (operator), what is expressed (output), what momentary mood rides on it. (c) Eight primaries that include wonder, fear and delight, which map onto curiosity, fear, desire.

## 10. Freud: the theory of drives (*Trieb*)

**Citations.** "Instincts and their Vicissitudes" (1915); *Beyond the Pleasure Principle* (1920); *Group Psychology and the Analysis of the Ego* (1921). [from abstract/standard account]

**Primaries.** A drive has four features: **source** (somatic excitation), **pressure** (*Drang*, force), **aim** (satisfaction through discharge), **object** (what or whom it is satisfied through, the most variable part). Early dualism: sexual drives and ego/self-preservation drives; later (1920): **Eros** (binding, life) and **Thanatos**/death drive (return to the inorganic, repetition). [from abstract/standard account]

**Derivation / composition.** **Vicissitudes**: reversal into the opposite (sadism to masochism), turning round upon the subject, repression, sublimation. These are operators on a drive, with defined effects on aim and object. The **economic** model: psychic energy (cathexis) is quantity that can be displaced, condensed, bound; the system seeks to minimise tension (constancy/pleasure principle). [from abstract/standard account]

**Social mechanism.** In *Group Psychology* a group is individuals who have put the same object (the leader) in place of their ego ideal and thereby **identify with one another**; libidinal ties explain cohesion. This is a structural account of how drive orientations align.

**Formality.** Quasi-quantitative metaphor (energy, flow) with named operators (displacement, condensation, sublimation, reversal). Not testable in the original form; the energy economy is widely considered a failed physical analogy. But the **drive = (source, pressure, aim, object)** tuple and the **vicissitudes as operators** are good algebraic shapes.

**Borrowable.** (a) The four-tuple as the type of a drive. (b) Vicissitudes as a named operator set (reverse, redirect-to-self, repress, sublimate). (c) The group as shared-object identification: a clean group-drive law. Treat the energy conservation as discarded.

## 11. Lacan: desire as desire of the Other, and the mathemes

**Citations.** Lacan, *Écrits* (1966); *Seminars* (e.g. XI, XX); the four discourses in *Seminar XVII* (1969-70). [from abstract/standard account]

**Primaries.** Need, demand, desire as distinct registers; desire arises from the gap between need and demand and is **"the desire of the Other"** (both desire for the Other's desire, and desire as structured by the Other's). Drives in his view have no natural object and circle around it. [from abstract/standard account]

**Notation.** Mathemes: S (signifier), $ (the barred, split subject), a (object cause of desire, *objet a*), A (the big Other), the formula of fantasy $ ◇ a, the graph of desire, and the **four discourses** (master, university, hysteric, analyst), each a four-slot structure (agent, other, product, truth) filled by S1, S2, $, a and rotated a quarter turn. [from abstract/standard account]

**How formal.** Honestly: symbolic notation, not an algebra. The symbols have no operation table, no stated axioms and no way to derive a conclusion by manipulation; the discourses are a combinatorial permutation device, which comes closest to a group structure (cyclic rotation) but is not used as one. The use of topology and number theory has been criticised as decorative (Sokal and Bricmont, *Impostures intellectuelles*, 1997; English *Fashionable Nonsense*, 1998 (corrected date); the standard objection; Lacanian defenders disagree). [from abstract/standard account]

**Social mechanism.** Desire as "desire of the Other": one's desire is structured by, and aimed at, another's desire (a theme Lacan takes from Kojève's reading of Hegel). Girard's **mimetic desire** — desire copied from a model, leading to rivalry and scapegoating — is the closest relative and is covered in `06-group-dynamics-frameworks.md` §8. Spinoza already has the core: emulation, "the desire of something, engendered in us by our conceiving that others have the like desire" (Def. 33), and rivalry over a shared object (p35). (Corrected: the original passage, "Girard (see `11` or a later file)", pointed at the wrong file and labelled Lacan's idea with Girard's term.)

**Borrowable.** One idea: desire has the *other's desire* as its object, a reflexive typing. In an algebra, desire(a, desire(b, x)) is a legitimate nested term. Nothing else is safely borrowable; the notation is unconstrained.

## 12. Nietzsche: will to power (brief)

**Primaries.** One, claimed: will to power, as the fundamental drive of which others are forms (*Beyond Good and Evil* 36, the hypothesis; the *Nachlass* material). The self is a society of competing drives (*Triebe*), with "the strongest" ruling the others (*Daybreak* 109, *BGE* 12, 19). [from abstract/standard account]

**Composition.** Drives are quanta of force in perpetual struggle; behaviour is the outcome of their competition, not a decision. No formal rules.

**Borrowable.** Only the structural idea that the individual is an arena of competing drives with a dominance relation, which is an order or weighted-voting structure; and the group-level analogue.

## 13. Contemporary analytic philosophy of emotion

**Authors.** Solomon, *The Passions* (1976); Nussbaum, *Upheavals of Thought* (2001); de Sousa, *The Rationality of Emotion* (1987). [from abstract/standard account]

**Structure.** The cognitivist or judgement theory: an emotion is, or contains, an **evaluative judgement** about an object (Solomon: emotions are judgements; Nussbaum: judgements of the importance for one's flourishing of things outside one's control, "eudaimonistic"). Each emotion has a **formal object** (fear: the dangerous; envy: the other's advantage) and a **target**. De Sousa adds "paradigm scenarios" learned in childhood that fix the emotion repertoire. The Stoic judgement theory in modern clothes. Ortony-Clore-Collins (see `15`) is the formalised relative.

**Formality.** Conceptual analysis, not formal. Gives a type signature: emotion : (agent, target, appraisal) to feeling + action tendency.

**Borrowable.** The type signature; and the warning that if emotion is judgement, then changing beliefs changes the drive (the Stoic therapy), so the algebra should have a belief-change operator and ask whether a drive survives it.

## 14. Hutcheson: moral algebra (1725) (added by validation pass)

**Citation.** Hutcheson, F. *An Inquiry into the Original of our Ideas of Beauty and Virtue* (1725), Treatise II, sec. III, the part headed as "an attempt to introduce a Mathematical Calculation in subjects of Morality". [secondary sources via search; primary not read]

**Content.** The moral importance of an action, M (the quantity of public good it produces), is in "compound ratio" of the agent's benevolence B and ability A: M = B x A, so B = M / A; with self-love S added, M = (B + S) x A or (B - S) x A depending on whether self-interest concurs or opposes. Also the first statement of "the greatest happiness for the greatest numbers". [standard account; the M = BA form is confirmed by secondary sources, the self-love variants are from memory]

**Why it matters here.** The earliest explicit *algebra* of a motive in this tradition: a drive (benevolence) inferred from an observed outcome divided by capacity. Hutcheson removed the formulas from later editions (from the 4th, 1738) [standard account, unverified]. Commentators note they sit uneasily with his moral-sense theory.

## 15. Bentham: the felicific calculus and the tables of pleasures and pains (1789, 1817) (added)

**Citation.** Bentham, J. *An Introduction to the Principles of Morals and Legislation* (printed 1780, published 1789), chs. IV-V [read, econlib, via fetch]; *A Table of the Springs of Action* (1817) [standard account].

**Measurement.** Ch. IV: the value of a pleasure or pain to one person depends on its **intensity, duration, certainty, propinquity**; as the tendency of an act, also **fecundity** (chance of being followed by the same kind) and **purity** (chance of not being followed by the opposite kind); across persons, **extent** (the number affected). The procedure sums the balance of pleasure over pain for each person, then over all persons affected [read].

**Catalogue.** Ch. V: 14 simple pleasures (sense, wealth, skill, amity, good name, power, piety, benevolence, malevolence, memory, imagination, expectation, association, relief) and 12 simple pains (privation, senses, awkwardness, enmity, ill name, piety, benevolence, malevolence, memory, imagination, expectation, association) [read]. Only benevolence and malevolence are "extra-regarding": they presuppose another person's pleasure or pain (ch. V para. XXXII) [read]. The *Table of the Springs of Action* maps each pleasure and pain to the motive and the interest it gives rise to [standard account].

**Why it matters here.** The first catalogue of affects paired with explicit dimensions of magnitude and an aggregation rule across persons: in form, a vector-valued quantity summed over a group. Benevolence and malevolence are coupling terms (my pleasure as a function of yours, with either sign), which is exactly the social-transmission slot. None of it was operationalised; Edgeworth's *Mathematical Psychics* (1881) and its imagined "hedonimeter" are the later attempt to make it so [standard account].

## 16. Herbart: equations of ideas, with feeling and desire derived (1816, 1824-25) (added)

**Citation.** Herbart, J. F. *Lehrbuch zur Psychologie* (1816); *Psychologie als Wissenschaft, neu gegründet auf Erfahrung, Metaphysik und Mathematik* (2 vols., 1824-25). Secondary: SEP "Johann Friedrich Herbart" [read, via fetch]; Boudewijnse, Murray and Bandomir, "Herbart's mathematical psychology", *History of Psychology* (1999) [cited by SEP; not read; volume number given inconsistently in search results].

**Content.** Representations (*Vorstellungen*) have strengths and oppose one another, inhibiting each other. **Statics**: the total inhibition (the *Hemmungssumme*) is shared out inversely to strength; for two fully opposed representations a > b the shares are b²/(a+b) and ab/(a+b). **Mechanics**: the inhibited amount approaches equilibrium as σ = S(1 - e^(-t)), never quite arriving. A **threshold of consciousness**: with three representations a > b > c, c is driven below threshold when c ≤ b·sqrt(a/(a+b)). [read, SEP]

**Feelings and desires.** Not separate faculties: they are *states of representations*. Feeling arises from the pressure of rising and inhibiting representations (a representation held between opposed forces is felt as unpleasant compression); desire is the awareness of a representation rising toward clarity against resistance; affects and passions are large representational masses driven far from equilibrium, transient because the system returns to equilibrium. [read, SEP]

**Why it matters here.** The one real precedent for **equations** in which the passions appear: a dynamical system with state variables, an equilibrium, a relaxation law and a threshold, from which feeling and desire are *derived* quantities. It is the counter-example to "nobody quantified". Its weaknesses are the ones to avoid: the inhibition rule was criticised as arbitrary, the parameters were never measured, and some configurations give zero or negative inhibited quantities (SEP notes). Herbart's line runs through Fechner into experimental psychology. Individual only; no group terms.

## 17. Wolff: deductive empirical and rational psychology (1732, 1734) (added, brief)

**Citation.** Wolff, C. *Psychologia empirica* (1732); *Psychologia rationalis* (1734). [secondary only, via search]

**Content.** A full treatment of the faculties, including pleasure, displeasure, appetites and affects, written in Wolff's "mathematical method" of numbered definitions and demonstrated paragraphs, with a proposed **psychometria** (a mathematical knowledge of the mind, by measuring effects indirectly). [standard account; the psychometria programme confirmed by secondary sources; the paragraph number usually cited (§522) not confirmed]

**Why it matters here.** Shows that Spinoza is not the only early-modern deductive treatment of the affects; Wolff's is the textbook-scale one that shaped German psychology up to Kant and Herbart. Less interesting as content: it does not reduce the affects to a small primary set with laws of composition as Spinoza does.

---

## Cross-walk of primaries

Rows are functional slots; cells give what each tradition calls it. A dash means no counterpart.

| Slot | Spinoza | Hobbes | Descartes | Hume | Stoics | Abhidharma | Rasa | Freud | Modern (see `15`) |
|---|---|---|---|---|---|---|---|---|---|
| Approach / wanting | desire (cupiditas) | appetite, desire | desire | desire | appetite (epithumia) | greed (lobha) | love/delight (rati) | libidinal aim (Eros) | reward, affiliation, mating, status motives |
| Avoidance | aversion = pain + accidental cause (Def. 9; derived) | aversion | desire itself, turned from an evil (art. 87: no separate aversion) | aversion | fear (phobos) | hatred (dosa) | fear (bhaya) | unpleasure, anxiety | self-protection, disease avoidance |
| Positive valence | joy | joy | joy | joy | pleasure (hedone) | pleasant feeling (vedana, universal) | - (no valence axis; rati, hasa nearest) | pleasure principle | valence axis (Russell) |
| Negative valence | sadness | grief | sadness | grief | distress (lupe) | painful feeling (vedana, universal) | - (soka nearest) | unpleasure | valence axis |
| Attach to cause | love, hate | love, hate | love, hatred | love, hatred (indirect) | love, hatred as species of desire | - | determinants | object | Plutchik mixtures |
| Novelty / curiosity | wonder (not an affect, Def. 4); no curiosity entry | curiosity = desire to know; admiration = joy at novelty | wonder (first passion, art. 53); curiosity = desire for knowledge (art. 88) | curiosity, or love of truth (T 2.3.10) | - | (delusion/clarity) | wonder (vismaya) | (sublimation to knowing) | curiosity as motive (see `17`) |
| Self-assertion / anger | anger = desire to injure from hatred (Def. 36) | anger = sudden courage | derived | pride, malice | anger as species of desire | hatred | anger (krodha) | aggression | status, power |
| Persistence | conatus | (endeavour is motion, not self-preservation) | - | - | - | life faculty | - | self-preservation | self-protection |
| Death / dissolution | - | - | - | - | - | - | - | Thanatos | - |
| Social transmission | imitation (p27), reciprocity (p31, p40, p43) | panic "by example" in a throng (ch. 6) | - | sympathy; reverberation (T 2.2.5) | - | - | sadharanikarana (Bhatta Nayaka) | identification | contagion (see `18`) |

**Patterns.**
- Almost every tradition has a desire/aversion pair and a joy/sadness pair. Hobbes and Hume list all four plus love and hate. Spinoza and Descartes do *not* make aversion primary (corrected): Spinoza derives it (Def. 9), and Descartes folds it into desire (art. 87), so for both the approach/avoid axis is one signed desire. The Stoics put love and hate under desire as species (DL 7.113).
- Fear is primary for the Stoics, rasa and the modern lists; derived (inconstant sadness, or aversion plus opinion) for Spinoza and Hobbes. Whether fear is primary is a modelling choice with a precedent either way.
- Curiosity is primary only in McDougall (`15`); in Hobbes, Descartes (art. 88) and Hume (T 2.3.10) it is a desire or love whose object is knowledge, and in Hobbes and Descartes it is triggered by an unvalenced or joyful response to novelty (admiration, wonder). Everywhere it is the only motive that is about *information*. (corrected)
- Group transmission has a precedent in at least six places: Spinoza's imitation and reciprocity laws, Hobbes's panic, Hume's sympathy and reverberation, Smith's mutual adjustment, Bentham's extra-regarding pleasures of benevolence and malevolence, Freud's identification (plus rasa's generalisation, for audiences). (corrected: the survey said four, and said "only Smith's has a fixed-point structure". That is too strong. Hume's mirrors are an iterated two-way reflection that decays, i.e. a convergent series with a stable sum; Spinoza's p43 makes reciprocal hatred a positive-feedback loop that love can break. Smith's is distinctive as the only one where the two parties *deliberately* move toward a shared level — a coordination equilibrium — rather than amplifying one another.)

## Maps to the algebra's wishes

- **Operands**: an agent's drive state: a conatus-level (Spinoza) with valence increments; an object slot; a time (present/future, Stoics); a belief or appraisal qualifier (Hobbes, Aristotle).
- **Operators**: attach-cause (love/hate), transfer-by-similarity, imitate, redirect or reverse (Freud's vicissitudes), add-hope or add-doubt (Hobbes, Spinoza), sympathise (mutual adjustment).
- **Candidate axioms from the sources**: (1) every agent has a ground level of striving; (2) valence is the signed change of that level; (3) a named passion is a primary with a typed qualifier; (4) valence follows association with objects; (5) affect transmits across similarity; (6) opposite associations superpose; (7) a deliberation ends in a last appetite (Hobbes).

## What exists vs what does not

**Exists.**
- A worked axiomatic derivation of a catalogue of passions from three primaries, with laws for association and social imitation: Spinoza E3 (and a deductive, larger-scale psychology in Wolff).
- Dimensions of magnitude for pleasures and pains and a rule for summing them over a group: Bentham. An algebraic formula for a motive: Hutcheson. A dynamical system with equations, equilibrium and threshold, from which feeling and desire are derived: Herbart. (added)
- Compound definitions by conjunction (Hobbes) and by the 2x2 valence-time grid (Stoics) that could be coded as a small typed grammar without much change.
- Enumerated co-occurrence rules (Abhidharma) and a cause-sign-state grammar (rasa).
- A tuple type for a drive and named operators on it (Freud).
- Multiple accounts of affect transmission between persons.

**Does not exist.**
- Any *operationalised* quantification. Bentham names dimensions and Herbart writes equations, but neither gives a unit or a measured parameter; Spinoza's "perfection" scalar is not operationalised either. (corrected: the survey said "any quantification", which Bentham and Herbart contradict)
- Any checkable proof system. Spinoza's proofs are not formally valid by modern standards; the Stoics' and Buddhists' are classificatory.
- Any group-level drive defined in its own right. Groups appear only as sums of imitating individuals (Spinoza), identifiers with a leader (Freud) or audiences (rasa).
- A treatment of drive *conflict* with a resolution rule, apart from Hobbes's deliberation (last wins), Nietzsche's dominance, Herbart's inhibition statics, and Spinoza's E4p7: "An emotion can only be controlled or destroyed by another emotion contrary thereto, and with more power for controlling emotion" [read].
- Theorems about control or prediction. The Stoics claim a therapy and Aristotle a technique of persuasion; neither states a result.
- Any test against data. For that see `16` and `07` (the first survey's warning on individual-level prediction still applies).

## Unconfirmed

Revised by the validation pass. Items resolved by reading are removed from this list: Spinoza's Definitions 1-3, Postulates and proofs (read); the count of 48 affect definitions (confirmed); Descartes arts. 57-58 (confirmed) and whether Descartes derives the others from the six (yes, art. 69); Hume's "mirrors" phrase (T 2.2.5, confirmed); E4p7 (confirmed); the Girard pointer (fixed: `06` §8).

- Commentators' verdicts on the rigour of Spinoza's proofs (Bennett 1984, Della Rocca, Curley): standard account, not checked.
- The derivation of ambition and honour from p27 in p29-p32: the definitions were read, the chain of propositions was not traced.
- The mechanism of Hume's double relation and of sympathy's enlivening (T 2.1.11): only the phrase and section titles were read.
- Smith's impartial spectator beyond the phrase, and "sympathy by situation, not contagion" (TMS I.i.1.10): standard account.
- The Stoic 2x2 grid (from Stobaeus and Cicero, not DL); the DL catalogue was read through a summarising fetch, not verbatim.
- All Abhidharma counts (52 Theravada: 7 universal, 6 occasional, 14 unwholesome, 25 beautiful; 46 Sarvastivada in six groups). These match the standard account (Bodhi's *Comprehensive Manual*) as the validator knows it, but no source was read this session.
- Natyashastra counts (8 sthayibhavas, 33 vyabhicaribhavas, 8 sattvikabhavas) and the rasas arising from others (NS 6.39-41): standard account. Shanta's history (Udbhata, Abhinavagupta): secondary search only.
- Freud's four features, vicissitudes, and *Group Psychology* definition of a group; Lacan's discourse structure; the Nietzsche passages (BGE 12, 19, 36; Daybreak 109): standard account, consistent with the validator's knowledge, not read.
- Descartes: the SEP's "about forty" passions in all, not counted.
- Hutcheson's self-love variants of the formula and their removal in the 4th edition; Bentham's *Table of the Springs of Action*; Edgeworth's hedonimeter; Wolff's §522: standard account or secondary search only.
- Herbart: equations as summarised by the SEP (which itself follows Weiss 1928 and Boudewijnse et al. 1999), not checked against *Psychologie als Wissenschaft*.

## Validation log (2026-10-29)

- Spinoza, *Ethics* III: ✎ corrected — Def. 1 quotation completed; p27's sign-flip for a hated other added; p35 "closer bonds", not "equal or stronger"; p39 deterrence guard and p43 added; pity is Def. 18, not p22; p14 association added; 48 definitions, three primaries (p11s), love/hate (p13s), conatus (p6-p9), wonder not an affect (Def. 4), E4p7 all confirmed [read].
- Hobbes, *Leviathan* 6: ✎ corrected — "no social mechanism in ch. 6" was false (panic terror spreads "by example" in a throng); will is the last appetite *or aversion*; simple passions listed verbatim; fear, hope, courage, anger, curiosity definitions confirmed [read].
- Descartes, *Passions*: ✎ corrected — art. 69 six and composition rule confirmed; arts. 57-58 confirmed; art. 87 (no separate aversion) and art. 88 (curiosity = desire for knowledge) added; arts. 185-189 are on pity, not "one soul" [read].
- Hume, *Treatise* II: ✎ corrected — direct/indirect lists confirmed (T 2.1.1); mirrors passage confirmed at T 2.2.5 and found to describe two-way reverberation with decay, so not "one-way"; curiosity section T 2.3.10 added [read].
- Smith, *TMS*: ✎ corrected — classification and lowering-the-pitch confirmed; endpoint is "concord", not unison; "Proprietary" typo [read].
- Aristotle, *Rhetoric* II: ✓ definitions of emotion, anger, fear and the three heads confirmed, quotations tightened [read].
- Stoics: ✎ corrected — four genera and eupatheiai confirmed (DL 7.110-116, via fetch); love, hatred, anger are species of desire; 2x2 grid is from other sources.
- Abhidharma: ✓ counts match the standard account; not read (moved to Unconfirmed).
- Natyashastra / rasa: ✎ corrected — sadharanikarana is Bhatta Nayaka's, not Bharata's; shanta first credited to Udbhata; sattvika bhavas added; counts unconfirmed.
- Freud: ✓ standard account, not read.
- Lacan: ✎ corrected — Sokal-Bricmont dated (1997 French, 1998 English); garbled Girard passage rewritten, pointer fixed to `06` §8, "mimetic desire" no longer attributed to Lacan.
- Nietzsche: ? standard account, passages not checked.
- Analytic philosophy of emotion: ✓ standard account, not read.
- Cross-walk table: ✎ corrected — Descartes avoidance (art. 87), Spinoza aversion derived, rasa valence cells (were "comic, heroic"), rasa "disgust?" in death row removed, Stoic anger and love under desire, Hobbes and Hume curiosity, Hobbes panic and Hume reverberation in transmission row.
- Closing claims: ✎ corrected — "Spinoza the one precedent" and "no quantification" contradicted by Hutcheson, Bentham, Herbart, Wolff; "only Smith's has a fixed-point structure" overstated (Hume's reverberation is a convergent loop).
- Added: Hutcheson (§14), Bentham (§15, chs. IV-V read), Herbart (§16, SEP read), Wolff (§17, secondary).
- Nothing removed as fabricated.

**Verdict.** The survey's spine is sound: every quotation it marked [read] checked out against the full texts, and no work or claim was invented. Its errors are of omission and overreach — the significant ones are the closing claims (Spinoza as the only formal precedent, "no quantification", Smith as the only feedback structure, "no transmission in Hobbes ch. 6"), all of which the primary texts or the missing Bentham/Herbart line contradict. Treat the [read] items as reliable and the [standard account] items on Indian and Buddhist sources as plausible but unchecked.

## Licences of quoted and transcribed material (2026-10-30)

Audit result: no passage needed removal or shortening; one attribution added (Natyashastra chapter and verse, section 9). Six items are flagged "check" and the text is unchanged.

| Source | Licence as determined | How used |
|---|---|---|
| Spinoza, *Ethics*, Elwes trans. (1883), Gutenberg #3800 | public domain | short quotations of definitions and propositions, with proposition numbers |
| Hobbes, *Leviathan* ch. 6, Gutenberg #3207 | public domain | short quotations, attributed to chapter |
| Hume, *Treatise* Book II, Gutenberg #4705 | public domain | short quotations (T 2.1.1, T 2.2.5) and section headings |
| Smith, *Theory of Moral Sentiments*, Gutenberg #67363 | public domain | short quotations (I.i.4, I.ii.3-5) |
| Bentham, *IPML* chs. IV-V (econlib) | public domain text (original 1789); econlib's hosting terms not checked | description of dimensions and of the catalogue of simple pleasures and pains (names listed, no table copied) |
| Diogenes Laertius 7.110-116, Yonge trans. (1853), via Wikisource | public domain | one nine-word quotation (7.110) and an enumeration of about 30 named subspecies; read through a summarising fetch, so wording and names need checking against the text before reliance (check) |
| Descartes, *Passions of the Soul*, Bennett's version (earlymoderntexts.com) | not determined; publisher copyright presumed (no licence stated on the cited page) | three short quotations (arts. 53, 69, 88) and paraphrase; to confirm the terms or paraphrase before open-sourcing (check) |
| Aristotle, *Rhetoric* II, Rhys Roberts trans. (classics.mit.edu) | not determined; publisher copyright presumed (1924 translation, status not verified) | five short quotations (II.1, II.2, II.5); to confirm public-domain status or paraphrase (check) |
| Natyashastra, rasa sutra | public domain (ancient text) | one Sanskrit quotation of about four words, now cited to ch. 6, v. 31 |
| Stanford Encyclopedia of Philosophy, "Johann Friedrich Herbart" | publisher copyright (not an open licence) | restated equations in our own notation and a paraphrased summary in section 16; to rewrite from the primary works or confirm no close wording before open-sourcing (check) |
| Abhidharma (section 8) and Natyashastra gloss (section 9) prose | not determined; unsourced recall, no Wikipedia text identified | description only; if any sentence proves to derive from Wikipedia it must be marked CC BY-SA and attributed (check) |
| Secondary works cited only by name (Bennett 1984, Curley, Della Rocca, Boudewijnse et al. 1999, Weiss 1928, Long & Sedley, Bodhi) | publisher copyright | citation only, nothing quoted |
