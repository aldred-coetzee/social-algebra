# Prior work 12: narratology, game design and AI/agent simulation

Date: 2026-10-29. Survey for the `social-algebra` strand. Aim as stated by Aldred: identify the mechanics of a social group so that operators and operands can be named, and later used to model interactions.

## Summary

These three fields could not stay informal. A story generator, a game NPC or an agent platform has to be told what social acts exist, when each is allowed, and what each does to the state. So they hold the closest thing to a working catalogue of "social operators" that I found.

- **Narratology** (Propp, Greimas, Souriau, Polti, Lehnert, story grammars) gave the first operand/operator split. Operands are roles (spheres of action, actants, forces). Operators are functions or plot units. Almost all of it is descriptive and informal, and none of it is executable. Propp's ordering claim is the one real "grammar". Lehnert's plot units are the one narratological system with a precise graph notation.
- **Game social-simulation** (Versu/Praxis, Comme il Faut/Prom Week, Ensemble, Sims, Storytron) is where operators became executable. Comme il Faut and Praxis have authored, explicit inventories of social actions with preconditions and effects on a typed social state. They are the most borrowable material in this cluster. They are hand-authored per story world and have no algebraic laws.
- **Agent theory** (OCC, BDI, Singh's commitments, FIPA-ACL, Bayesian theory of mind, I-POMDP) gives operators with real semantics. FIPA acts and commitment operations are defined in logic. I-POMDP and inverse planning are formally precise about recursive modelling of others, but their operators are "update a belief", not "do a social act".
- **LLM social simulation** (Park et al.) has no operator inventory at all. The "operators" are free-text prompts. Its validity problems are the strongest argument for writing the operators down explicitly.

Nothing here is an algebra of social acts. Laws are rare and partial: Greimas and Rastier explicitly read the semiotic square as a Klein four-group (a real group structure, but over meanings, not people); Lehnert's plot units have a closed generating set and composition but no stated laws; Singh's later commitment work states reasoning postulates (for example detach: a conditional commitment whose antecedent holds becomes unconditional), which are laws over one relation type. None gives closure, identity or inverse laws over acts between people. (Validation note, 2026-10-29: the original sentence said "no laws anywhere, with one partial exception" and then named two; corrected.)

Method note: every entry below rests on a source I actually opened (full text via pdftotext, a publisher or arXiv abstract, or a search-result snippet, which I label as secondary). Where I only had a snippet, the entry says so. Anything I could not confirm is under "Unconfirmed" at the end.

---

## A. Narratology

### A1. Propp, Morphology of the Folktale

- **Citation:** Vladimir Propp, *Morphology of the Folktale* (Russian 1928; English translation by Laurence Scott 1958; 2nd ed. rev. Louis A. Wagner, intro. Alan Dundes, Austin: University of Texas Press, 1968).
- **Verified at:** https://en.wikipedia.org/wiki/Morphology_of_the_Folktale (31 functions listed; spheres of action named); https://www.degruyterbrill.com/document/doi/10.7560/783911/html (2nd ed. 1968, Scott/Wagner) . The Wikipedia page gives 1927 in its external links and 1928 in the text, so the Russian date is flagged: 1928 is the usual citation. I could not open the book itself (the one PDF I found returned 403).
- **Their vocabulary:** *function* ("an act of a character, defined from the point of view of its significance for the course of the action"), *sphere of action*, *dramatis personae*, *move*, *wonder tale*.
- **Operands (translated):** seven roles (dramatis personae), the villain, the hero and a handful of helper, giver and sought-for-person types (the full list is in the book, ch. 6, and on the Wikipedia article; wording follows the Wikipedia article 'Morphology of the Folktale', CC BY-SA 4.0). One character can fill several roles and one role can be spread over characters. Propp's operands are therefore roles, not people.
- **Operators (translated):** the 31 functions, numbered in Propp's order and running from an initial absentation or interdiction through villainy, donor tests, struggle and victory, to return, recognition, punishment and wedding (full list: Propp 1968, ch. 3; not transcribed here). Each function is an action by one role that changes the situation (a lack created, an object transferred, a status granted). Spheres group functions by who performs them. For example, secondary sources give the villain villainy, struggle and pursuit, and the donor the preparation and provision of the magical agent. The Roman-numeral mapping of functions to spheres came from a secondary summary that itself disagreed with my own draft, so I do not record a full table here. Check against the book.
- **Formal structure:** informal. Functions are named categories with a claimed **fixed order** (ascending 1 to 31, not all present, a few inversions). That order is the only compositional rule, and it is a sequence constraint, not an algebra. No state representation or update semantics is given.
- **Predictive/generative claim:** after the initial situation, a Russian wonder tale is a selection from the 31 functions in fixed order. It was drawn from about 100 tales. Secondary sources note it is a claim about one genre, and the extension to other genres is contested. It has been applied to other corpora (a Sesotho study found it usable), and used for story generators, but "fits" is looser than "predicts".
- **Limits:** one genre; function names are interpretive, so coding is not reproducible without judgement; no state, no continuous variables, no parallel action; roles are fixed set of seven.
- **Relevance to social-algebra:** the clearest ancestor of the operator/operand split and of "operators defined by their effect on roles, not on individuals". Also the first example of a *role–function* matrix (sphere ↔ function set), which is a typing of operators by operand role.

### A2. Greimas, actantial model and semiotic square

- **Citation:** A. J. Greimas, *Sémantique structurale* (Paris: Larousse, 1966; English: *Structural Semantics: An Attempt at a Method*). Square developed with F. Rastier, "The Interaction of Semiotic Constraints," *Yale French Studies* 41 (1968), 86–105.
- **Verified at:** https://en.wikipedia.org/wiki/Actantial_model (six actants, 1966, Propp and Souriau as inspiration); https://en.wikipedia.org/wiki/Semiotic_square (square, Rastier 1968, a nine-word characterisation of a term as an intersection of contrariety, contradiction and complementarity, which the Wikipedia 'Semiotic square' page, CC BY-SA 4.0, attributes to Greimas 1982, and which an arXiv paper at https://arxiv.org/pdf/2605.05273 also quotes). Secondary only. I did not see the book. The Larousse publisher detail came from a search summary, not a primary record.
- **Their vocabulary:** *actant*, *actor*, *subject/object*, *sender/receiver* (giver/gifted), *helper/opponent*, axes of desire, transmission and power; *semiotic square*, contrary, contradictory, complementary.
- **Operands (translated):** six abstract positions (actants): Subject, Object, Sender, Receiver, Helper, Opponent (names as on the Wikipedia article 'Actantial model', CC BY-SA 4.0). An actant is a role in a relation, and one actor can occupy several.
- **Operators (translated):** the model has no verbs. Its three axes are *relations between positions*: desire (subject–object), transmission (sender–receiver), power (helper–opponent). The semiotic square is a separate device: for a term S1 it generates S2 (contrary), not-S1 (contradictory) and not-S2, with implication links. That is a small closed set of negations and oppositions over meanings, not over people.
- **Formal structure:** the actantial model is a fixed graph of six positions. The square is a Klein-group-like diagram of opposition relations. Greimas and Rastier link it to the Klein group (secondary source). It is logical in appearance, but Pottier (cited in the same search) argues Greimas is inconsistent on whether it is a logical or non-logical model. No state, no update.
- **Predictive/generative claim:** none quantitative. A descriptive grid for any narrative, claimed universal.
- **Limits:** so abstract it fits anything; no timing; no mechanism for how roles change hands.
- **Relevance:** the three axes (desire, transmission, power) are a candidate **typology of relations** rather than of acts: who wants, who gives, who helps or blocks. Useful as a sanity check on which relation types a social algebra must have.

### A3. Souriau, Les deux cent mille situations dramatiques

- **Citation:** Étienne Souriau, *Les deux cent mille situations dramatiques* (Paris: Flammarion, 1950).
- **Verified at:** secondary only. https://en.wikipedia.org/wiki/Actant, https://dictionnaire.artcena.fr/print/pdf/node/7947 and a lecture-note PDF at https://www.people.iup.edu/sherwood/Archived-Courses/UTPB-Archive/engl3300S03/3300s03Notes/souriau.pdf. I did not see the book.
- **Their vocabulary:** six dramaturgic *functions* or *forces*, named after planets and signs. As given by the sources (wording follows the Wikipedia article 'Actant', CC BY-SA 4.0, and the lecture notes cited above; not checked against Souriau's French): Lion (thematic force, desire), Sun (the desired good), Earth (the one who gets it), Mars (the opponent), Balance (arbiter), Moon (helper, combines with any of the others). Sources differ on some of the glosses. Check the French.
- **Operands (translated):** the six forces. A character is a force within a system of forces.
- **Operators (translated):** situations are *configurations* of the six forces: which are filled by which characters, which are doubled, which are absent. The 200,000 is a combinatorial count of those configurations, not a list of acts.
- **Formal structure:** combinatorial, informal. A force "system" in which each force can be played by one or several characters.
- **Predictive/generative claim:** an enumeration claim only. Souriau's aim was to replace Polti's fixed list of 36 with a combinatorial system, showing the space is far larger. (Validation: the original said "reduce Polti's 36", which contradicts the rest of the sentence.)
- **Limits:** the 200,000 figure is a count of possible role assignments, not an observed distribution; the forces have no dynamics.
- **Relevance:** direct precedent for *counting configurations of role-fillers* as the object of study. Souriau's "character as a force within a system of forces" is close to treating individuals as operands carrying several roles.

### A4. Polti, The Thirty-Six Dramatic Situations

- **Citation:** Georges Polti, *Les trente-six situations dramatiques* (Paris, 1895); English: *The Thirty-Six Dramatic Situations*, trans. Lucile Ray (1916).
- **Verified at:** https://en.wikipedia.org/wiki/The_Thirty-Six_Dramatic_Situations; https://www.gutenberg.org/ebooks/72036 (French text). Polti credits Carlo Gozzi (1720–1806) with the claim that only 36 tragic situations exist (Polti's introduction, via secondary source). I did not read the list myself. The Wikipedia article 'The Thirty-Six Dramatic Situations' (CC BY-SA 4.0) gives the first as "Supplication" and the last as "Loss of loved ones"; the list and descriptions in this section follow that article.
- **Their vocabulary:** *situation*, with each one defined by the roles involved (for example a persecutor and a supplicant).
- **Operands (translated):** unlabelled character roles in each situation.
- **Operators (translated):** none explicit; each situation is a named typical relation or event pattern between roles, so the 36 are best read as *named multi-party relation patterns* (supplication, vengeance, rivalry, etc.).
- **Formal structure:** a flat list. No composition, no state.
- **Predictive/generative claim:** exhaustiveness of 36. This is a taxonomy claim and was never tested statistically. Goethe (to Eckermann) reports that Schiller tried to find more and could not find even as many as Gozzi's 36. (Validation: corrected from "could not find more than".)
- **Limits:** arbitrary granularity; drawn from classical drama; no rules for combining situations or moving between them.
- **Relevance:** weak but useful as a candidate checklist of *recurrent social configurations* that any algebra should be able to express.

### A5. Lehnert, Plot Units and Narrative Summarization

- **Citation:** Wendy G. Lehnert, "Plot Units and Narrative Summarization," *Cognitive Science* 5(4), 293–331 (1981). DOI 10.1207/s15516709cog0504_1 (the volume number differs across catalogues, so I rely on the DOI).
- **Verified at:** full text read from https://people.cs.pitt.edu/~wiebe/courses/CS3730/Spring2013/lehnert1981.pdf. Related: Lehnert, Black & Reiser, "Summarizing Narratives," IJCAI 1981, https://mlanthology.org/ijcai/1981/lehnert1981ijcai-summarizing (72 subjects, comparing plot units with story grammars).
- **Their vocabulary:** *affect state*, *plot unit*, *causal link*, *primitive plot unit*, *complex plot unit*, *cross-character links*.
- **Operands (translated):** three affect-state types per character: positive event (+), negative event (−), mental state (M). An operand is therefore an affect-valued state of an agent, not an agent.
- **Operators (translated):** four directed link types between affect states: motivation (m), actualization (a), termination (t), equivalence (e). m and a point forward in time, t and e backward. With three states and four links there are 36 possible pairs, of which **15 are legal and are named as the primitive plot units** (for example success, failure, motivation, change of mind, loss, resolution). Pairs compose into complex units: for example the string (− M +) yields intentional problem resolution, fortuitous problem resolution and success born of adversity, depending only on the links. Multi-character units use cross-character links, which Lehnert deliberately does **not** type ("we will not need to distinguish cross-character links"). What she names are nine cross-character *configurations*: three resulting-mental-state ones (request M/M, enablement +/M, motivation −/M), two speech acts (threat, promise), and shared and mixed events (+/+, −/−, +/−, −/+). Complex two-character units such as honored request, denied request, coerced agreement, honored promise and retaliation are built from them.
- **Formal structure:** a labelled directed graph over affect states with a closed set of 15 primitives and composition into larger graphs. This is the most algebra-like object in the narratology set: a small generating set and a combination rule. It is hand-coded on text by a trained analyst, and it is not executable on its own, although later work automated parts of it (Goyal, Riloff and Daumé 2010, seen as a search hit and not opened).
- **Predictive/generative claim:** units that overlap in a story are central to it, and a summary should preserve the highly connected ones. Lehnert, Black and Reiser compared it with story grammars on summary data from 72 subjects. I did not read the comparison's results, so I do not state which model won.
- **Limits:** needs a human to decide which events are + or −; one valence axis; no social structure beyond "request", "enablement" and so on; no relations that persist (friendship, authority, debt).
- **Relevance:** the nearest thing to "operators that compose". Its trick is to define the operand as *what the act did to someone's affect*, which makes acts across different domains comparable. The cross-character links are a minimal set of two-party operators.

### A6. Story grammars: Rumelhart, Mandler and Johnson

- **Citation:** David E. Rumelhart, "Notes on a schema for stories," in D. G. Bobrow & A. Collins (eds.), *Representation and Understanding: Studies in Cognitive Science* (Academic Press, 1975), pp. 211–236. Jean M. Mandler & Nancy S. Johnson, "Remembrance of things parsed: Story structure and recall," *Cognitive Psychology* 9, 111–151 (1977).
- **Verified at:** bibliographic details only, from https://narrativestudies.lib.unb.ca/bibcite/reference/18324 and https://scholarhub.vn/publication/:slug/3ba649c0-42f7-4387-b772-b8ed5f4ffeba, with a description of the Mandler–Johnson result from https://uh-ir.tdl.org/items/065853a7-a102-4835-8b86-08270195fb4f/full. I did not read the grammars' rewrite rules. Treat the rules themselves as unconfirmed here.
- **Their vocabulary:** *story schema*, *story grammar*, rewrite rules over setting, episode, event, goal, attempt, outcome.
- **Operands/operators (translated):** per the sources, a grammar of rewrite rules that parse a story into hierarchical constituents. In my reading that gives states and events as operands and rewrite rules as operators, but the sources I opened do not show the rules, so I will not claim more.
- **Formal structure:** context-free rewrite grammar (the sources say "grammar"; Rumelhart's is described as a network structure).
- **Predictive/generative claim:** Mandler and Johnson parsed simple stories and found recall omissions and errors could be predicted from grammar structure, a real, tested prediction about human memory. Lehnert, Black and Reiser then compared the grammar with plot units on summaries.
- **Limits:** about one protagonist's goal-directed episodes; a grammar of single-actor events does not directly express multi-party structure.
- **Relevance:** low, apart from the lesson that a formal structure was tested against human recall.

---

## B. Game social simulation

### B1. Versu / Praxis (Evans and Short)

- **Citation:** Richard Evans and Emily Short, "Versu—A Simulationist Storytelling System," *IEEE Transactions on Computational Intelligence and AI in Games* 6(2), 113–130 (June 2014). DOI 10.1109/TCIAIG.2013.2287297.
- **Verified at:** full text read from https://www.cs.uky.edu/~sgware/reading/papers/evans2014versu.pdf. Praxish, a later public reconstruction: https://ojs.aaai.org/index.php/AIIDE/article/view/27537. The original Versu is no longer available (Praxish authors, via search summary).
- **Their vocabulary:** *social practice* (successor to the Schankian script), *affordance*, *process*, *exclusion logic*, *role agnosticism*, *norm violation*, *drama manager (DM)*.
- **Operands (translated):** agents, and the **roles** they play in each practice instance (X, Y in `process.greet.X.Y`). Practices are first-class: a practice instance is itself a node in the state, with its own local data ("keep score").
- **Operators (translated):** **affordances**, i.e. social acts offered by a practice (greet, disapprove, forgive, and so on). A practice is "a hierarchical collection of affordances". An act exists only inside a practice that makes it available. This is the "constitutive" view, and the paper cites Rawls's chess example. Norms are handled by putting a "violation" postcondition on norm-breaking acts, which spawns a responsive sub-practice offering disapproval, forgiveness, anger or eviction.
- **Formal structure:** **explicit and executable.** World state is a set of sentences in **exclusion logic**, a modal logic using `.` and `!`; for example `brown.relationship.lucy.evaluation.attractive!40`. `!` asserts the value is the unique one, so changing it removes the old one automatically. State is a trie, so removing a prefix deletes a whole subtree, which ties lifetime of data to lifetime of the practice or agent that owns it. An action has preconditions and postconditions in PDDL-like form (quantified preconditions, negation as failure, expression evaluation, domain axioms, conditional effects). Update: performing an affordance adds and removes sentences; changed sentences activate or deactivate practices (`process.*` sentences); loop. Agents pick actions by **utility-based reactive selection**, forward-simulating each option's consequences against their desires, not full planning. The paper reports a type checker, an inspector, deterministic replay and a stress-test tool. [from abstract/standard account]
- **Predictive/generative claim:** generative, not predictive. It claims a system where the same story plays from any role and non-player agents stay coherent. Evidence is the shipped interactive fiction and designer experience, not empirical validation of social realism. The original product was cancelled in 2014.
- **Limits:** every practice and norm is hand-authored; a norm is only a flag; no algebraic laws; utilities are authored; no learning.
- **Relevance:** highest for **practice as a typed bundle of role-indexed operators with a lifetime**. Exclusion logic is a neat, borrowable state formalism (unique-value fields with automatic cleanup). The role-agnostic authoring is exactly "operators defined over roles, then bound to people".

### B2. Comme il Faut and Prom Week (McCoy et al.)

- **Citation:** Joshua McCoy, Mike Treanor, Ben Samuel, Aaron A. Reed, Michael Mateas and Noah Wardrip-Fruin, "Social Story Worlds With Comme il Faut," *IEEE TCIAIG* 6(2), 97–112 (2014). DOI 10.1109/TCIAIG.2014.2304692. Earlier: McCoy et al., "Comme il Faut: A System for Authoring Playable Social Models," AIIDE 2011, https://ojs.aaai.org/index.php/AIIDE/article/view/12454.
- **Verified at:** full text read from https://cs.uky.edu/~sgware/reading/papers/mccoy2014cif.pdf. Prom Week intro: https://ojs.aaai.org/index.php/AIIDE/article/view/12662. "Social physics" term in coverage at https://news.ucsc.edu/2012/02/prom-week/.
- **Their vocabulary:** *social exchange*, *intent*, *instantiation*, *volition formation*, *social state*, *trait*, *status*, *relationship*, *network*, *cultural knowledge base (CKB)*, *social facts database (SFDB)*, *influence rule*, *trigger rule*, *retargeting*.
- **Operands (translated):** characters, thin by design (McCoy et al. 2014 say that what makes characters rich is their relational situation). State per character or pair: **traits** (permanent binary), **statuses** (temporary binary, can be directional such as "angry at X"), **relationships** (binary, non-exclusive, e.g. housemates, rivals), and bidirectional **scalar social networks** (e.g. respect 30 toward a rival who reciprocates 85). Plus a CKB of shared cultural items with attitudes (loves, hates, has), and an SFDB log of past exchanges.
- **Operators (translated):** **social exchanges**: multi-character acts that exist to change the social state, each with a single intended outcome (the intent) such as "start friendship". Several exchanges can share an intent but differ in preconditions ("unlikely alliance" vs "comrades in arms"). An exchange has preconditions (hard limits), a responder accept/reject decision, and effects: adjust network values by fixed amounts, start or end relationships, add or remove statuses. Only characters in the exchange are directly affected. Third-party fallout comes through trigger rules.
- **Formal structure:** **explicit, executable, hand-authored rule base.** Rules are first-order-like and may quantify over third parties (the paper's example: X is cheating on Y if X and Y date and X also dates Z), and may query history. Pipeline: (1) volition formation re-ranks all intents and exchanges for each ordered pair using weighted **influence rules**, where each rule adds or subtracts weight; (2) the host picks an exchange; (3) response determination by the responder's own rules; (4) the most salient instantiation is selected and filled in with natural language; (5) effects applied; (6) trigger rules run; repeat. Hard vs soft: preconditions forbid, influence rules only change likelihood, so the author expresses how strict a norm is by which one they use.
- **Predictive/generative claim:** generative. The authors claim authors can write norms once and retarget them across contexts. They evaluate Prom Week (18 characters, one school week) by diversity of the stories players produced and critical reception, not by matching real human social behaviour. It is not claimed to predict real groups.
- **Limits:** all rules and weights are hand-tuned; traits are fixed (so no personality change); the world is small; no learning or fitting to data; no laws about how exchanges combine; rule inventories are per story world.
- **Relevance:** **highest in the cluster for operators.** It has a real inventory shape: operator = (precondition, intent, response rule, effects), operand = (traits, statuses, relationships, scalar networks, shared knowledge, history). It also separates *norms* (influence rules) from *acts* (exchanges), which is a design pattern worth copying. The Prom Week authored exchange library is a concrete list to mine; I did not obtain a count of its social games.

### B3. Ensemble engine

- **Citation:** Ben Samuel, Aaron A. Reed, Paul Maddaloni, Michael Mateas and Noah Wardrip-Fruin, "The Ensemble Engine: Next-Generation Social Physics," *Proceedings of the 10th International Conference on the Foundations of Digital Games (FDG 2015)*, pp. 22–25. No DOI found; FDG 2015 proceedings are not in the ACM DL. (Validation: title and pages confirmed from reference 31 of the ICIDS 2022 paper below and from a Crossref reference record that cites it with the same title; a search summary's alternative title "The Scored Rule Engine" is not supported by any record seen and should be ignored.) Johnson-Bey, Nelson and Mateas (ICIDS 2022) describe the engine as the successor to CiF, an attempt to take the lessons learned from working with CiF and repackage its rule-based architecture as a general-purpose tool for social simulation (paraphrased), released as a desktop application for defining characters, actions, relationship values and social rules.
- **Verified at:** https://www.kmjn.org/publications/SocialPhysics_ICIDS22.pdf (Johnson-Bey, Nelson and Mateas, "Exploring the Design Space of Social Physics Engines in Games," ICIDS 2022). Read; this is the source for the description above. The DOI 10.1145/2994258.2994285 belongs to a different paper, "Confluence: visualizing social physics for interactive narrative" (Dong et al., MiG 2016), which cites Ensemble; do not use it for Ensemble.
- **Their vocabulary / structure:** as CiF (rules, volition, social state). I have no first-hand detail on Ensemble's differences. The ICIDS 2022 paper is a good entry point for it.
- **Relevance:** it matters because it is CiF with the world content removed, i.e. an attempt at a *generic* social-rule engine. Read the ICIDS 2022 survey first (it also covers Versu, PsychSim, Crusader Kings II opinions, Talk of the Town and The Sims 4).

### B4. The Sims (needs and relationships)

- **Citation:** Will Wright / Maxis, *The Sims* (2000) and sequels. No primary design paper found.
- **Verified at:** secondary only. https://www.kmjn.org/publications/SocialPhysics_ICIDS22.pdf describes The Sims 4 as using utility AI over basic needs (comfort, social, hunger, hygiene, energy) and relationships as two scalar values (friendship, romance). The CiF paper (above) says The Sims 3 can only reference the two characters in an interaction and has no use of history in its rules. A transcript of a talk on the Sims AI (https://amara.org/subtitles/cVoJS4OdmVql/en/1/download/The%20Genius%20AI%20Behind%20The%20Sims.en.txt) says motives range from −100 to +100 and objects "advertise" actions that Sims score by current motive levels. Neither source covers daily vs lasting relationship scores, so I do not claim that detail.
- **Operands (translated):** a Sim with scalar needs; a pair with two scalar relationship values.
- **Operators (translated):** object-advertised interactions, scored by need satisfaction. Social interactions change the two relationship scalars.
- **Formal structure:** informal, utility-based; numbers hand-tuned.
- **Predictive/generative claim:** none. Believability only.
- **Limits:** relationship is two numbers; interactions only reference the two parties.
- **Relevance:** as the commercial baseline: the least structure that sells. Useful to know the minimum viable relationship state is a pair of scalars.

### B5. Crawford, Storytron, Deikto

- **Citation:** Chris Crawford, *Chris Crawford on Interactive Storytelling* (2nd ed., New Riders, 2013) and the Storytron platform (2006–2011).
- **Verified at:** secondary only. https://ifwiki.org/Storytron_1 and https://elmcip.net/node/15417 (via search). Storytron's authoring tool was Swat; Deikto is the language for character-to-character interaction, built around verbs, with verb scripting in a language called Sappho. Crawford's argument (via a search summary of his site) is that an interactive storyworld needs at least about 100 verbs. A Geneva wiki entry noted no scientific publications on Storytron. The only authoritative description is Crawford's own writing, which I did not read.
- **Operands/operators (translated):** characters with emotional-state variables and traits as operands; **verbs** as operators, scripted actor-independently, so any verb open to the protagonist is open to every character. The verb is the unit of authoring.
- **Formal structure:** executable in Swat/Sappho, but I could not verify the update rules or the character variables. Status: pre-alpha, now unavailable.
- **Limits and claim:** no empirical evaluation. The relevant idea is "verbs as the first-class social operators, with a fixed vocabulary and typed arguments".
- **Relevance:** useful as an existence proof of a design based on a **verb inventory**, but I cannot use it for detail.

### B6. Façade and drama management (adjacent)

- **Citation:** Michael Mateas and Andrew Stern, "Structuring Content in the Façade Interactive Drama Architecture," AIIDE 2005. Mark O. Riedl and Vadim Bulitko, "Interactive Narrative: An Intelligent Systems Approach," *AI Magazine* 34(1), 2013.
- **Verified at:** https://ojs.aaai.org/index.php/AIIDE/article/view/18722 and https://ojs.aaai.org/index.php/aimagazine/article/view/2449 (abstract level). Not read in full.
- **Summary:** Façade organises thousands of joint dialogue behaviours (written in ABL, a reactive planning language) into **beats** sequenced by a drama manager. Riedl and Bulitko survey about 20 years of interactive narrative and define a drama manager as an agent that steers the world so the player's experience conforms to a target aesthetic.
- **Relevance:** for a social algebra, drama management is a *control layer over operators*, not an operator set. It is out of scope for the notation, relevant later if modelling is to be steered toward outcomes.

---

## C. Agents and cognitive models

### C1. OCC model

- **Citation:** Andrew Ortony, Gerald L. Clore and Allan Collins, *The Cognitive Structure of Emotions* (Cambridge University Press, 1988).
- **Verified at:** https://www.cambridge.org/core/books/cognitive-structure-of-emotions/structure-of-the-theory/09C34EB15A6C01C6BCCC40CE09890EC0 (and sibling chapter pages). I confirmed the 22 emotion types and the three-way split (events, agents' actions, objects) only from the search summary of the book's chapters. I did not read the book. (Validation: the 22 types fall into groups by appraisal target: event-based, including prospect-based and the "fortunes-of-others" group (happy-for, gloating, resentment, pity), which is the explicitly social part; action-based; and object-based. Full list: OCC 1988, not transcribed; the type names were not checked against the book.)
- **Their vocabulary:** *appraisal*, *desirability*, *praiseworthiness*, *appealingness*; emotion types differentiated by the situation represented.
- **Operands (translated):** an appraising agent with goals, standards and attitudes, and the three appraisal targets: events, actions of agents, objects.
- **Operators (translated):** not operators on a group. It is a function from (event/action/object, appraiser's goals and standards) to emotion types. Its value for a social algebra is as a **valence function** for the effect of acts on each party (cf. Lehnert's +/−).
- **Formal structure:** a taxonomy with appraisal variables; implemented in many agent systems but loosely specified in the book as a decision tree.
- **Predictive claim:** emotion type follows from appraisal structure. The authors themselves say it is compatible with a psychological constructionist approach (Ortony 2015, from search). I did not check empirical support.
- **Relevance:** gives a ready set of "what an act does to a person" categories (pleased about a consequence for someone else, approving of someone's act, and so on).

### C2. BDI agents (Rao and Georgeff)

- **Citation:** Anand S. Rao and Michael P. Georgeff, "BDI Agents: From Theory to Practice," *Proceedings of the 1st International Conference on Multi-Agent Systems (ICMAS-95)*, San Francisco, 1995, pp. 312–319.
- **Verified at:** bibliographic record only, https://apice.unibo.it/xwiki/bin/view/Publication/BdiIcmas95 and a search summary. I did not read the formal logic. The abstract says it integrates theory, implementation and an air-traffic management application.
- **Operands/operators (translated):** an agent as (beliefs, desires, intentions). Operators are changes to those three sets and plan selection. The social part is minimal.
- **Formal structure:** modal logic of BDI (not verified by me from this source).
- **Relevance:** the standard vocabulary for an individual's mental state. Not a theory of groups.

### C3. Singh, social commitments

- **Citation:** Munindar P. Singh, "An ontology for commitments in multiagent systems: Toward a unification of normative concepts," *Artificial Intelligence and Law* 7, 97–113 (1999). Yolum & Singh, "Commitment Machines" (ATAL 2001) and "Flexible Protocol Specification and Execution: Applying Event Calculus Planning using Commitments" (AAMAS 2002).
- **Verified at:** abstract level via https://www.csc2.ncsu.edu/faculty/mpsingh/papers/mas/ai+law-final.pdf (listed in search; the direct fetch returned 403, so I read only the search summary) and Singh's course slides (https://www.csc2.ncsu.edu/faculty/mpsingh/local/SOC/f19/slides/commitments.pdf, search summary only).
- **Their vocabulary:** *commitment*, *spheres of commitment*, obligations, taboos, conventions and pledges as kinds of commitment; Hohfeldian directed obligations.
- **Operands (translated):** agents, and the commitments between them as objects. A commitment is a directed relation from a debtor to a creditor. In the 1999 paper it is written C(x, y, G, p): debtor x, creditor y, a context group G (the "sphere of commitment"), and condition p. The four-argument conditional form C(debtor, creditor, antecedent, consequent) is from later work (Yolum and Singh; Singh, "Semantical Considerations on Dialectical and Practical Commitments," AAAI 2008). (Validation: the original attributed the conditional form to the 1999 ontology; the context-group form is from the validator's knowledge of the paper, not re-read.) From the slides, commitments can be nested.
- **Operators (translated):** Singh 1999 names six operations: **create**, **discharge** (satisfy), **cancel** (by the debtor), **release** (by the creditor), **delegate** (change the debtor) and **assign** (change the creditor). (Validation: confirmed as attributed to Singh 1999 by Singh's own 2002 position paper and an AAAI 2007 paper, https://cdn.aaai.org/AAAI/2007/AAAI07-210.pdf; not from the 1999 text itself.) **Detach** (a conditional commitment becoming unconditional when its antecedent holds) belongs to the later conditional form; it appears in Singh's course slides.
- **Formal structure:** logic-based and executable. The context group G makes a group a party to every commitment (cancellation and release can be governed by G's norms). Yolum and Singh give commitment machines that compile to finite-state machines, and an event-calculus formalisation.
- **Claim and fit:** a design claim that protocol compliance can be checked from commitment state rather than from message order.
- **Limits:** one relation type (directed obligation) stands in for social structure; no affect, status or hierarchy beyond what can be written as commitments.
- **Relevance:** **the best-defined single relation type for social operators**. It turns "promise", "request accepted", "delegate", "release" into a small algebra of state changes on a debt-like relation. It gives a clean answer to "what persists after an act".

### C4. FIPA-ACL performatives

- **Citation:** Foundation for Intelligent Physical Agents, *FIPA Communicative Act Library Specification*, SC00037J (Standard, December 2002).
- **Verified at:** https://www.fipa.org/specs/fipa00037/index.html (version history), https://www.fipa.org/repository/fipa2000.html (per-act specs: Accept Proposal, Inform, Propose, Request, Cancel, CFP, Refuse), and lecture-note secondary sources (https://jmvidal.cse.sc.edu/talks/agentcommunication/inform.html). A direct fetch of the spec itself was blocked (403).
- **Their vocabulary:** *communicative act*, *performative*, *feasibility precondition (FP)*, *rational effect (RE)*, SL (semantic language).
- **Operands (translated):** agents with belief and intention operators (B_i, I_i) in SL.
- **Operators (translated):** a fixed library of speech acts (inform, request, propose, accept-proposal, reject-proposal, cfp, refuse, cancel, and more). **Explicit and standardised.** Per secondary sources, FP for `inform` is roughly "sender believes φ and does not believe the receiver already knows whether φ", with RE "receiver believes φ" (written B_iφ ∧ ¬B_i(Bif_jφ ∨ Uif_jφ) → B_jφ). `request`'s FP is FP(a)[i\j] ∧ B_i Agent(j, a) ∧ ¬B_i I_j Done(a): the act's own feasibility preconditions as far as they concern the sender, the sender believes the receiver is the agent of the act, and does not believe the receiver already intends it; RE is Done(a). (Validation: corrected from "the sender intends the act, believes the receiver can do it" — the sender's intention is not part of the FP; formula from the validator's knowledge of the spec, not re-read.) Most other acts are defined as macros or composites of inform and request (query-if is a request to inform-if, cfp a query-ref about proposals); confirm and disconfirm are also primitive. (Validation: softened from "all other acts are defined in terms of inform and request".) I did not see the formulas in the specification text, so treat the exact SL as unconfirmed.
- **Predictive/generative claim:** none. It is an interoperability standard, not a behavioural theory.
- **Limits:** a known critique (AAMAS 2005, found by search) is that mentalistic semantics cannot be verified from outside, and that the Gricean part of the `inform` precondition is really a social protocol. Speech-act coverage is thin on non-assertive social acts (praise, shaming, dominance moves).
- **Relevance:** the **closest existing thing to a standardised inventory of communicative operators with formal pre- and post-conditions**. It is small (22 acts in the 2002 library: accept-proposal, agree, cancel, cfp, confirm, disconfirm, failure, inform, inform-if, inform-ref, not-understood, propagate, propose, proxy, query-if, query-ref, refuse, reject-proposal, request, request-when, request-whenever, subscribe) and information-centred. Pair it with Singh's commitments and you get a rough formal skeleton for request, promise, accept, refuse.

### C5. Bayesian theory of mind (Baker, Saxe and Tenenbaum)

- **Citation:** Chris L. Baker, Rebecca Saxe and Joshua B. Tenenbaum, "Action understanding as inverse planning," *Cognition* 113(3), 329–349 (2009). DOI 10.1016/j.cognition.2009.07.005.
- **Verified at:** https://dspace.mit.edu/handle/1721.1/60852 (record and abstract). Earlier: NeurIPS 2005, "Bayesian models of human action understanding," https://papers.neurips.cc/paper_files/paper/2005/file/f5b1b89d98b7286673128a5fb112cb9a-Paper.pdf (found, not opened). I did not read the paper's equations.
- **Operands (translated):** an observed agent with a goal and beliefs; an observer with a prior over goals.
- **Operators (translated):** two: forward planning (goal and belief to action, assumed approximately rational) and its Bayesian inversion (action to goal). It is a model of **inference about others**, not of acts between them.
- **Formal structure:** probabilistic, with a rationality principle (agents plan approximately rationally). Executable.
- **Predictive claim:** human goal inferences in simple maze animations match the model quantitatively (three psychophysical experiments, per the abstract). The paper frames it as formalising Dennett's intentional stance. Tested only with simplified stimuli.
- **Limits:** one agent and a goal; small worlds; no social acts as such.
- **Relevance:** supplies the "what does X think Y wants" operator that a social algebra will eventually need.

### C6. I-POMDP (Gmytrasiewicz and Doshi)

- **Citation:** Piotr J. Gmytrasiewicz and Prashant Doshi, "A Framework for Sequential Planning in Multi-Agent Settings," *Journal of Artificial Intelligence Research* 24, 49–79 (2005).
- **Verified at:** https://jair.org/index.php/jair/article/view/10414 and https://arxiv.org/pdf/1109.2135 (abstract via search summary; the full paper not opened).
- **Operands (translated):** an agent's belief over the physical state *and over models of other agents*, which can nest (what I think you think I think).
- **Operators (translated):** Bayesian belief update and policy choice at each level of nesting.
- **Formal structure:** fully formal; extends POMDP with interactive states. Per the abstract, value iteration still converges and value functions remain piecewise linear and convex, but exact solutions are only asymptotically computable because beliefs nest arbitrarily; approximations are used.
- **Claim:** a decision-theoretic alternative to Nash equilibrium that also captures off-equilibrium behaviour.
- **Limits:** intractable at depth; models are of individuals; no group-level structure or norms.
- **Relevance:** the principled treatment of "recursive modelling of others", relevant to any operator whose effect depends on what others know.

### C7. Social deduction and hidden-role games (added)

- **Citation:** Luca Carminati, Brian Hu Zhang, Gabriele Farina, Nicola Gatti and Tuomas Sandholm, "Hidden-Role Games: Equilibrium Concepts and Computation," arXiv:2308.16017 (EC 2024).
- **Verified at:** https://arxiv.org/pdf/2308.16017 (abstract read in full text). Also found and not read: S. T. Wang, "Optimal Strategy in the Werewolf Game: A Theoretical Study," arXiv:2408.17177; Bard et al., "The Hanabi Challenge," arXiv:1902.00506.
- **What it does:** defines the first rigorous equilibrium concept for games where players are privately assigned to teams and must find allies (Mafia/Werewolf, The Resistance/Avalon). The equilibrium depends on the communication channels available. Optimal equilibria are computable efficiently in some cases, including the recreational games, but NP-hard or coNP-hard in general. They computed exact equilibria for full 5- and 6-player Avalon.
- **Operands/operators (translated):** operands are players with hidden team membership; operators are speech, voting and team proposals, treated through the communication model. It is a theory of *coalition inference under hidden roles*.
- **Relevance:** the only formal treatment here of **hidden role/allegiance** as part of the state, and an honest statement that the solution concept depends on the channel. Good for the "what operators need to be observable" question.

---

## D. LLM-based social simulation

### D1. Park et al., Generative Agents

- **Citation:** Joon Sung Park, Joseph C. O'Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang and Michael S. Bernstein, "Generative Agents: Interactive Simulacra of Human Behavior," UIST '23, October 2023. arXiv:2304.03442.
- **Verified at:** full text read from https://arxiv.org/pdf/2304.03442; abstract at https://arxiv.org/abs/2304.03442.
- **Their vocabulary:** *memory stream*, *retrieval* (recency, importance, relevance), *reflection*, *planning*, *observation*, *believability*.
- **Operands (translated):** 25 LLM agents in a Sims-like town, each seeded with a natural-language biography; state is a stream of natural-language memories.
- **Operators (translated):** **there is no operator inventory.** Each agent step is observe, retrieve, reflect, plan, act, all via prompts to a language model. Social acts (invite, ask out, gossip) are whatever the model writes. Information spread and relationships are emergent properties that the authors measure afterwards.
- **Formal structure:** none beyond the architecture. Not rule-based, not logical.
- **Claim and results:** believability, judged by humans, improves with each of observation, planning and reflection (ablation, TrueSkill ranking of conditions). Over two game days, knowledge of one agent's mayoral run rose from 1 agent (4%) to 8 (32%), and of a party from 1 to 13 (52%), with network density rising from 0.167 to 0.74. Among 453 responses about other agents, 6 (1.3%) were hallucinated. The party invitation reached 12 agents beyond its source.
- **Limits (the authors'):** agents embellished memories; location choices drifted; they misread physical norms (a single-occupancy dorm bathroom, shops closed after 5 pm); instruction tuning made agents overly polite and cooperative, so they accepted ideas that did not fit their character; a 25-agent two-day run cost thousands of dollars in tokens.
- **Relevance:** it is the opposing design: maximum fluency, zero explicit operators. It shows what the explicit-rule systems (B1, B2) give up and what they gain (inspectability, replay, control). The observed over-cooperation is a direct example of an implicit operator set being wrong without anyone noticing.

### D2. Park et al. 2024, simulating individuals

- **Citation:** Joon Sung Park, Carolyn Q. Zou, et al. (11 authors in v3), arXiv:2411.10109 (v1 November 2024; v3 June 2026). Originally "Generative Agent Simulations of 1,000 People", now retitled "LLM Agents Grounded in Self-Reports Enable General-Purpose Simulation of Individuals." (Validation: the widely quoted figure, "85% as accurately as participants replicate their own answers two weeks later" on the GSS, is v1's; the figures below are the current abstract's, confirmed 2026-10-29. Cite by version.)
- **Verified at:** https://arxiv.org/abs/2411.10109 (abstract fetched).
- **Result:** agents built from two-hour interviews with 1,052 Americans reproduce those people's held-out answers at 83% (interview-only), 82% (survey-only) and 86% (combined) of the participants' own two-week test-retest consistency, against 74% for demographic-only agents. The authors report smaller accuracy gaps across racial and ideological groups.
- **Relevance:** the best existing evidence that LLM agents can predict *individual attitudes* from rich input. It says nothing about group mechanics or interaction dynamics.

### D3. Validity of LLM social simulation

- **Citation:** Patrick Taillandier, Jean Daniel Zucker, Arnaud Grignard, Benoit Gaudou, Nghi Quang Huynh, Haojia Kong and Alexis Drogoul, "From the Fluency Fallacy to the Micro-to-Macro Validity Gap: Opportunities and Pitfalls of LLMs in Social Simulation," arXiv:2507.19364 (v4, 9 October 2026; v1, July 2025, carried a different title, reportedly "Integrating LLM in Agent-Based Social Simulation: Opportunities and Challenges" — cite by arXiv ID and version).
- **Verified at:** https://arxiv.org/pdf/2507.19364 (abstract read). Also found, not read in full: "Validation is the central challenge for generative social simulation: a critical review of LLMs in agent-based modeling," https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12627210/; "Don't Trust Generative Agents to Mimic Communication on ..." https://arxiv.org/html/2506.21974v3.
- **Their claim:** micro-level LLM limits (hallucination, stochastic inconsistency, representational bias, alignment effects) propagate into agent-level distortions (persona convergence) and macro-level risks (artificial consensus, behavioural homogenisation). Evaluators are exposed to a "fluency fallacy" and automation bias. They identify serious games, participatory settings and exploratory modelling as defensible uses. The review in PMC12627210 reaches a similar conclusion (validation relies on face validity or loosely tied outcome measures).
- **Relevance:** the strongest external argument for the project's premise: if the operators are not written down, you cannot say which of the many things an LLM does is the social mechanism, and you cannot validate it.

---

## What this cluster already covers

1. **A split between operands and operators**, in several forms: roles/functions (Propp, Souriau, Greimas), affect states/links (Lehnert), role-bound affordances (Versu), exchange/state (CiF), commitment/operations (Singh), agent/speech-act (FIPA).
2. **Executable operator inventories with preconditions and effects**: Praxis practices (Versu), CiF social exchanges and influence rules, FIPA communicative acts, Singh's commitment operations. These run.
3. **Typed social state**: CiF's traits, statuses, relationships, scalar networks, shared knowledge base and history; Versu's exclusion-logic tree.
4. **A small closed set of composable pieces**: Lehnert's 15 primitive plot units (the only one I found with true composition rules).
5. **Norms as a separate layer from acts**: CiF's hard preconditions vs soft influence rules; Versu's violation postconditions spawning responses.
6. **Role-agnostic authoring**: write the act over roles, bind later to individuals (Versu, CiF, Propp).
7. **Recursive modelling of others and hidden roles**: I-POMDP, inverse planning, hidden-role games.
8. **Evidence of the failure mode of the implicit approach**: Park et al. and Taillandier et al.

## What it does not cover

- **No algebra of social acts.** None of the systems states laws over acts between people: whether they compose, commute, have inverses or identities, or what is invariant. The nearest are Greimas's square read as a Klein group (laws, but over meanings), Lehnert's composition of primitives (no laws), and Singh's commitment postulates (laws over one relation). (Validation: softened from "none of the systems states laws", which the Greimas entry above contradicts.)
- **No operands above the pair.** Almost everything is dyadic (CiF's effects are limited to the two parties in the exchange; Sims 3 can only reference two). Third-party and group-level structure appears only through trigger rules or authored quantified conditions. A group as an operand, with membership, coalitions or hierarchy, is rarely first-class: the partial exceptions are Versu's practice instances (a multi-role situation as a node in the state), Singh's context group G, and the hidden teams in hidden-role games. (Validation: softened from "not first-class anywhere".)
- **Little validation against real groups.** CiF and Versu are judged by player experience. Baker et al. validate against human inference in toy mazes. Park et al. 2024 validate individual survey answers, not interaction. Nothing predicts the course of an observed group.
- **Authored, not derived.** Every inventory is hand-written per story world. There is no argument that the set is complete or minimal, apart from Propp's and Polti's counts, which are claims about corpora.
- **Weak on persistent structure**: status, authority, obligation and reputation are either scalars (Sims, CiF networks) or the one relation type of Singh. Kinship, hierarchy and institutions are barely touched.
- **Weak on time and dynamics.** Fixed order (Propp) or turn loops. No continuous-time or rate models.

## Which systems have an explicit, executable inventory of social operators that could be borrowed

Ranked by usefulness for social-algebra:

1. **Comme il Faut / Prom Week.** Operator = social exchange with intent, preconditions, response rule and effects on a typed social state. The most complete inventory of social acts with pre/post-conditions that I found. The Prom Week exchange library itself would be the thing to mine (I have not seen its contents).
2. **Versu / Praxis.** Operator = role-indexed affordance inside a practice, with norms and a state formalism (exclusion logic) that is small enough to adapt. The original Versu is gone, but Praxish (https://ojs.aaai.org/index.php/AIIDE/article/view/27537) is a public reconstruction.
3. **Singh's commitments plus FIPA-ACL.** Small, formally defined: promise, request, accept, refuse, release. No affect or status, but the semantics are clean. I could not retrieve the specification text, so check the formulas before relying on them.
4. **Ensemble.** A generic rewrite of CiF. Worth reading if a reusable engine is wanted. Primary paper: Samuel et al., FDG 2015 (see B3); its contents not yet read.
5. **Lehnert's plot units.** Not executable but precise: a closed set of 15 primitives over three affect states and four link types, with cross-character links for two-party structure.
6. **Storytron/Deikto.** An explicit verb vocabulary was the design, but the tool is unavailable and I could not verify details.

Not borrowable as operator inventories: Propp (31 functions are role-and-genre bound, though the matrix of role to function is a good template), Greimas, Souriau, Polti, OCC (appraisal not acts), BDI, Sims, Park et al. (no operators).

---

## Unconfirmed

Items I did not find a real source for, or found only via a search snippet and did not check:

- Propp's complete function-to-sphere table in Roman numerals (a secondary source and my own draft disagreed). The book itself was not opened.
- Greimas, Souriau and Polti primary texts: all secondary. The six Souriau glosses (Lion, Sun, Earth, Mars, Balance, Moon) differ between sources.
- Polti's complete list of 36 situations (only first and last given by one blog).
- The rewrite rules of Rumelhart's and Mandler–Johnson's story grammars.
- The 22 OCC emotion types against the book itself (listed in C1 from standard secondary usage).
- Rao–Georgeff's formal BDI logic.
- Singh 1999: the six operations are confirmed only via secondary attribution (Singh 2002, AAAI 2007), not the 1999 text; the C(x, y, G, p) form is from the validator's knowledge.
- The exact SL formulas for FIPA `inform` and `request` (lecture-note summaries and validator's knowledge; fipa.org blocked every fetch, 403/Cloudflare, on 2026-10-29).
- A Sesotho study applying Propp (secondary mention only; no citation).
- The Ensemble FDG 2015 paper's contents (citation now resolved; see B3).
- The Sims relationship model in detail (daily vs lasting scores): no source found.
- The count of social games in Prom Week.
- Storytron's character variables and verb semantics; Crawford's book content.
- Park et al. 2023 evaluation numbers beyond those quoted from the paper's own text (these are first-hand).
- Goyal, Riloff and Daumé (2010) on automating plot units: seen as a search result only.
- Whether anyone has published formal laws (algebraic or categorical) for social-practice or plot-unit composition: I did not search for this, and a negative result here should not be inferred from the survey.

## Missing work (found in validation, not yet surveyed)

Named from the validator's knowledge; citations to be checked before use.

- **Tzvetan Todorov, *Grammaire du Décaméron* (1969).** A narrative grammar with proper nouns as agents, adjectives as states and verbs as transforming actions, plus modal and negation operators on propositions. Arguably the most algebra-like narratology text and a direct precedent for operand/operator; its absence is the biggest gap in section A.
- **Claude Bremond, *Logique du récit* (1973).** Recasts Propp's functions as branching possibilities (virtuality, actualisation, outcome) and roles as agent/patient pairs (influencer, improver, degrader, protector, frustrator, retributor). Typed two-party operators.
- **PsychSim** (Pynadath and Marsella, 2005): multi-agent simulation with recursive models of others; covered by the ICIDS 2022 survey but not here.
- **Talk of the Town** (Ryan et al., 2015 onward): a simulated town with knowledge propagation, belief mutation and relationship structure; a natural group-level counterpart to Park et al.
- **Cristiano Castelfranchi, "Commitments: From Individual Intentions to Groups and Organizations" (ICMAS 1995).** Social commitment as a three-party relation (debtor, creditor, witness group); the precursor of Singh's context group.
- **Cohen and Perrault (1979) / Cohen and Levesque (1990).** The plan-based speech-act semantics that FIPA's FP/RE scheme descends from.
- **Concordia** (Vezhnevets et al., 2023, arXiv:2312.03664) and **Argyle et al., "Out of One, Many" (Political Analysis, 2023)**: the main LLM-simulation counterparts to Park et al., the first with an explicit game-master component that resolves agents' acts.
- **David Elson's Story Intention Graph** (2012): a validated descendant of Lehnert's plot units with an annotated corpus (DramaBank).

## Validation log (2026-10-29)

- A1 Propp — ✓ (1928 / Scott 1958 / 2nd ed. 1968; 31 functions and seven spheres match the standard list; ~100 tales correct). The Sesotho study moved to Unconfirmed (no citation).
- A2 Greimas / Rastier — ✎ Rastier venue added (*Yale French Studies* 41). Content ✓; arXiv 2605.05273 resolves to a paper on the Greimas square.
- A3 Souriau — ✎ self-contradictory aim sentence ("reduce" Polti's 36 / space "much larger") corrected. Six forces ✓.
- A4 Polti — ✎ Schiller anecdote inverted (he found fewer than 36, not "no more than"). Dates, translator and Gutenberg 72036 ✓.
- A5 Lehnert 1981 — ✎ DOI, volume 5(4), pages ✓ via Crossref; "36 possible pairs, 15 legal primitive units" ✓ from full text; the (− M +) example ✓. Corrected: cross-character links are untyped; request/enablement/motivation are three of nine cross-character configurations. Lehnert, Black & Reiser IJCAI 1981 ✓ (72-subject figure not rechecked).
- A6 Rumelhart 1975; Mandler & Johnson 1977 — ✓ bibliographically; rules remain unconfirmed.
- B1 Versu — ✓ (Crossref: TCIAIG 6(2) 113–130, DOI resolves). Praxish ✓ (Dameris, Hernandez Roman & Kreminski, AIIDE 2023).
- B2 Comme il Faut — ✓ (Crossref: TCIAIG 6(2) 97–112, six authors as listed); AIIDE 2011 ✓; AIIDE 12662 is the 2013 "Prom Week" paper ✓.
- B3 Ensemble — ✎ citation fixed: Samuel, Reed, Maddaloni, Mateas & Wardrip-Fruin, "The Ensemble Engine: Next-Generation Social Physics," FDG 2015, pp. 22–25; no DOI. The wrong DOI is confirmed as Dong et al., MiG 2016. Johnson-Bey et al. ICIDS 2022 ✓.
- B4 The Sims — ? relationship detail remains secondary only; the stated claims are suitably hedged.
- B5 Crawford / Storytron — ? secondary only; book citation ✓.
- B6 Mateas & Stern AIIDE 2005 ✓ (pp. 93–98); Riedl & Bulitko AI Magazine 34(1) 2013 ✓.
- C1 OCC 1988 — ✎ the 22 types added (standard list). Book itself not read.
- C2 Rao & Georgeff ICMAS-95 — ✓.
- C3 Singh 1999 — ✎ the four-argument conditional form C(debtor, creditor, antecedent, consequent) was wrongly placed in the 1999 paper; the paper uses C(x, y, G, p) with a context group, and the conditional form is later. The six operations (create, discharge, cancel, release, delegate, assign) confirmed via Singh-authored secondary sources and moved out of Unconfirmed. Yolum & Singh 2001/2002 ✓.
- C4 FIPA-ACL SC00037J — ✎ count fixed ("about 20" → 22). The request FP was wrong: the sender's intention is not part of the FP. "All acts defined from inform and request" softened. fipa.org blocked every fetch, so the formulas stay Unconfirmed.
- C5 Baker, Saxe & Tenenbaum 2009 — ✓ (Crossref: Cognition 113(3) 329–349); NeurIPS 2005 ✓.
- C6 Gmytrasiewicz & Doshi JAIR 2005 — ✓ (arXiv 1109.2135 resolves to it).
- C7 Carminati et al. arXiv:2308.16017 ✓; Werewolf 2408.17177 ✓; Hanabi 1902.00506 ✓.
- D1 Park et al. 2023 — ✓ (arXiv 2304.03442; figures first-hand in the survey, not re-read).
- D2 Park et al. 2024 — ✓ figures match the current (v3) abstract (83/82/86% vs 74%, 1,052 people). ✎ added that the much-quoted "85%" is the v1 figure, so cite by version.
- D3 Taillandier et al. — ✓ (title, v4 9 Oct 2026); ✎ full author list added, and a note that v1 carried a different title. arXiv 2506.21974 ✓; PMC12627210 not rechecked.
- Summary and "What it does not cover" — ✎ overclaims softened: "no laws anywhere" contradicted the survey's own Klein-group point for Greimas; "groups not first-class anywhere" ignored Versu practice instances, Singh's context group and hidden-role teams.
- No fabrications found; nothing removed.

**Verdict.** Bibliographically reliable: every work exists as cited, and the one broken citation (Ensemble) was flagged honestly by the author and is now fixed. Content errors cluster in the secondary-only entries (Singh's notation, FIPA's request FP, the Polti and Souriau asides) and in the closing generalisations, which were a notch stronger than the entries above them supported. Use the operator and operand readings of CiF, Versu, Lehnert and Singh with confidence. Recheck the FIPA formulas against the spec before building on them, and add Todorov and Bremond before concluding that narratology offers no algebra.

## Licences of quoted and transcribed material (2026-10-30)

Edits made in this pass: the Propp role and function lists reduced to descriptions; the OCC list of 22 types reduced to its grouping; Wikipedia-derived passages marked CC BY-SA 4.0; short quotations given named sources.

| Source | Licence as determined | How used |
|---|---|---|
| Wikipedia: Morphology of the Folktale, Actantial model, Semiotic square, Actant, The Thirty-Six Dramatic Situations | CC BY-SA 4.0 | Role names, actant names, Souriau forces, Polti first and last situation; wording follows the articles; marked inline in A1-A4 |
| Propp 1968 (UT Press) | not determined; publisher copyright presumed | Description of the 31 functions and 7 roles; one short quoted definition of "function"; citation |
| Greimas 1966, 1982; Greimas and Rastier 1968 | not determined; publisher copyright presumed | One nine-word characterisation, via secondary sources; citation |
| Souriau 1950 | not determined; publisher copyright presumed | Six force names via Wikipedia and lecture notes; description |
| Polti 1895 / Ray 1916 | public domain (text); not read | Two situation names via Wikipedia |
| Lehnert 1981 (Cognitive Science, Wiley) | not determined; publisher copyright presumed | Description only. CHECK: hosted PDF read was of unrecorded provenance (author or publisher posted); confirm before relying on it |
| Evans and Short 2014 (IEEE TCIAIG) | not determined; publisher copyright presumed | Description only. CHECK: hosted PDF provenance not recorded |
| McCoy et al. 2014 (IEEE TCIAIG) | not determined; publisher copyright presumed | One short attributed phrase; description. CHECK: hosted PDF provenance not recorded |
| Samuel et al. FDG 2015; Johnson-Bey, Nelson and Mateas ICIDS 2022 | not determined; publisher copyright presumed | Paraphrase of the Ensemble description, now attributed to the ICIDS 2022 paper (whether the wording originated in Samuel et al. is not established) |
| OCC 1988 (Cambridge UP) | not determined; publisher copyright presumed | Grouping described; list of 22 types no longer transcribed |
| FIPA SC00037J and per-act specs | not determined (FIPA licence not recorded; fipa.org blocked) | CHECK, left unchanged: two restated SL formulas (inform, request) and the list of 22 act names in C4; confirm the licence or reduce to a count and the three most relevant acts |
| Carminati et al., arXiv:2308.16017 | arXiv non-exclusive licence; per-paper licence not recorded | CHECK, left unchanged: C7 'What it does' is a close paraphrase of the abstract; restate in own words or confirm |
| Other cited papers (Singh, Rao and Georgeff, Gmytrasiewicz and Doshi, Baker et al., Park et al., Taillandier et al.) | not determined; publisher copyright presumed (arXiv items: arXiv licence) | Citation and description only; no quotation or transcription flagged |
