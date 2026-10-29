# Prior work 08: History and historical social science, as operators and operands

Date: 2026-10-29. Survey for `social-algebra`. Not committed.

## Summary

History and historical social science have produced many models of how groups change. Almost all are typologies, cycles or narrative mechanisms, with a few exceptions. The verbs are unusually rich: **circulate, routinise, degenerate, co-opt, bridge, capture, withdraw-and-return, shed, extract**. The operands are mostly *classes of actor* (elites, peasants, creative minority, dynasty, faction, state), and the *states* a group moves between (regime types, asabiya level, access order).

Three findings matter most:

1. **Oldest operator model is a state-transition rule.** Polybius's anacyclosis (c. 2nd c. BC) is a six-state cycle with named degeneration and alteration transitions. Khaldun's dynasty cycle is the same shape with a continuous state variable (solidarity).
2. **Only Turchin et al., Padgett et al. and the selectorate theorists come close to a calculus.** Turchin writes differential equations and spatial simulation rules. Padgett writes relation-to-actor production rules (autocatalysis) in agent-based models. Bueno de Mesquita et al. write a formal game. Everything else is typology or narrative. *(Validation: the original listed only the first two, contradicting its own item 25.)*
3. **The empirical record is weak where it is most formal.** A Seshat causal result (the 2019 *Nature* moralizing-gods paper) was retracted by its authors; the 2020 forecast was loose (a 50-year period from three spikes, "around 2020") and has been assessed only by its own authors; the selectorate results are contested under re-estimation, with the authors' reply claiming support survives. Formalising without an independent test is the recurring failure.

**Verification note.** Sources were gathered by web search on 2026-10-29. Most are publisher, library-catalogue or secondary pages; I did **not** open primary texts. Each entry says what was confirmed. Claims about content marked (background) are from general knowledge, not checked in this pass, and are listed again under Unconfirmed.

---

## 1. Ibn Khaldun, *Muqaddimah* (1377) — the 'asabiyya cycle

- **Citation:** Ibn Khaldun, *al-Muqaddima*; English: Franz Rosenthal (trans.), *The Muqaddimah: An Introduction to History*, 3 vols., Bollingen Series XLIII, New York: Pantheon, 1958 (now Princeton University Press; abridged one-volume edition 1969).
- **Source:** https://en.wikipedia.org/wiki/Asabiyyah (secondary); edition: https://press.princeton.edu/node/66459
- **Their vocabulary:** 'asabiyya (group feeling), dynasty (dawla), nomad/desert vs. sedentary/urban life (badawa/hadara), luxury, generations.
- **Operands:** Groups (tribes, dynasties) each carrying a scalar *solidarity*; two environments (periphery, centre); generations.
- **Operators:** *Conquer from periphery* (high-solidarity group displaces a low-solidarity ruling group); *settle/luxuriate* (solidarity decays with sedentary life); *replace*. Cycle length: Khaldun says a dynasty as a rule does not last beyond three generations, reckoning a generation at forty years, so about 120 years (Muqaddimah ch. 3; validator's knowledge of the text, consistent with the secondary sources; the original's "3 or 4 generations (~120 years)" conflated two figures). Formality: **narrative with an implicit one-variable state machine**. No equations in the original.
- **Predictive claim:** Dynasties last about three generations then fall to a more cohesive outsider. Retrodiction by later authors (Turchin) on Eurasian imperial cases; not tested in the original.
- **Limits:** One scalar for solidarity; no inter-group structure within the dynasty; generation count is a heuristic; sourced largely to Maghreb history.
- **Relevance:** Cleanest example of an operand with a *level* that an operator (settle, conquer) raises or lowers. Directly translatable: `S(g)` solidarity, `settle: S -> S - d`, `frontier-pressure: S -> S + f`.

## 2. Polybius, *Histories* Book 6 — anacyclosis

- **Citation:** Polybius, *Histories*, Book 6 (2nd c. BC); book survives in part.
- **Source:** secondary: https://jls.shirazu.ac.ir/article_7567.html?lang=en ; https://scriptaclassica.org/index.php/sci/article/download/4163/3659/7707
- **Their vocabulary:** kingship, tyranny, aristocracy, oligarchy, democracy, ochlocracy; anacyclosis; mixed constitution.
- **Operands:** Constitutions, three healthy and three corrupt; implicitly the ruling class and the populace.
- **Operators:** *Degeneration* (kingship -> tyranny, aristocracy -> oligarchy, caused by rulers' behaviour when unchecked, children growing soft) and *alteration* (tyranny -> aristocracy, by overthrow). One analysis distinguishes these two kinds of change. Sequence in secondary sources: primitive monarchy -> kingship -> tyranny -> aristocracy -> oligarchy -> democracy -> ochlocracy -> monarchy again. Sources differ slightly on the final step. **Mixed constitution** is the cycle-breaking operator (Rome, Sparta). Formality: **typology plus a deterministic transition table**; the closest ancient thing to a state-transition rule.
- **Predictive claim:** Every simple constitution decays in a fixed order; only mixing stops it. Not testable as stated; Polybius used it to explain Rome's success. The idea of cycles predates him (Plato, Aristotle).
- **Limits:** Single deterministic path; no exogenous shock; classification by number of rulers only.
- **Relevance:** Template for an operator table over a finite regime set, plus a "composition" operator (mix) that kills a transition. Direct fit.

## 3. Turchin, *Historical Dynamics* (2003)

- **Citation:** Peter Turchin, *Historical Dynamics: Why States Rise and Fall*, Princeton University Press, 2003.
- **Source:** https://press.princeton.edu/books/hardcover/9780691116693/historical-dynamics ; NetLogo replication: https://forum.comses.net/t/replica-of-turchins-2003-metaethnic-frontier-model/10733
- **Their vocabulary:** asabiya, metaethnic frontier, imperial cycle.
- **Operands:** Spatial cells/regions each carrying asabiya; polities as sets of cells; frontier cells.
- **Operators:** Per the publisher and replication notes: regions bordering other groups *gain* asabiya (us-versus-them competition); larger frontiers raise an empire's asabiya; as an empire grows, internal conflict *reduces* asabiya for regions far from the frontier; war capacity is spread thin; below a threshold the empire collapses and a higher-asabiya group re-establishes one. Formality: **both**: the book condenses the theory into small systems of differential equations (polity area coupled to collective solidarity, with an appendix on the simulations), and chapter 4 adds a **spatially explicit agent-based (lattice) simulation** of the metaethnic frontier, replicated in NetLogo on CoMSES. Exact functional forms not checked here. The later, larger agent-based test is Turchin, Currie, Turner and Gavrilets, "War, space, and the evolution of Old World complex societies", *PNAS* 110(41): 16384-16389 (2013), doi:10.1073/pnas.1308825110: a cultural-evolution model on an Afro-Eurasian grid, 1500 BCE-1500 CE, explaining about 65% of variance in where large polities arose.
- **Predictive claim:** Imperial territorial expansion concentrates where frontiers coincide with religious or ethnic divides. Tested against the historical record in the book. Reviewed by J. A. Tainter, *Nature* 427: 488-489 (2004) (text not retrieved). See Seshat (item 7) for what happened to later tests.
- **Limits:** Asabiya is one scalar, not observed directly; calibration rests on a small number of historical cases.
- **Relevance:** The most direct existing formalisation of Khaldun. Reusable pieces: asabiya as a state variable, frontier as an external-pressure operator, collapse as a threshold event.

## 4. Turchin and Nefedov, *Secular Cycles* (2009), structural-demographic theory

- **Citation:** Peter Turchin and Sergey A. Nefedov, *Secular Cycles*, Princeton University Press, 2009.
- **Source:** https://press.princeton.edu/node/52401 ; https://stafforini.com/works/turchin-2009-secular-cycles/
- **Their vocabulary:** secular cycles; population, elite, and state sectors; popular immiseration; elite overproduction; state fiscal crisis; sociopolitical instability.
- **Operands:** Three aggregate classes (population, elites, state), each with numbers, incomes and finances.
- **Operators:** Coupled feedbacks: population growth depresses real wages, raises elite numbers relative to positions, strains state finances, which generates instability; instability reduces population and elites and restarts the cycle. Built on Goldstone's demographic-structural theory (publisher text). Formality: **dynamical-systems framing with quantitative predictions** tested on England, France, Russia and Rome (publisher text). Whether the book states the system as differential equations I could not confirm here.
- **Predictive claim:** Century-scale oscillations with specific lead-lag signatures. Tested on four cases by the authors. A 2009 review indexed at ProQuest notes critics raising Eurocentrism concerns; the authors cite Chinese dynastic cycles and Khaldun in reply. I found no independent test of the quantitative predictions.
- **Limits:** Aggregate classes, not individuals; case selection by the theory's authors; each cycle is one data point.
- **Relevance:** Shows how to turn class-level sectors into coupled state variables. Weak for an algebra of individual-level interaction.

## 5. Goldstone, *Revolution and Rebellion in the Early Modern World* (1991)

- **Citation:** Jack A. Goldstone, *Revolution and Rebellion in the Early Modern World: Population Change and State Breakdown in England, France, Turkey, and China, 1600-1850*, 1991; 25th anniversary edition Routledge 2016. Original: Berkeley, University of California Press, 1991 (validator's knowledge; not web-checked).
- **Source:** https://www.routledge.com/products/9781138222113 ; retrospective: Goldstone, "Demographic Structural Theory: 25 Years On", *Cliodynamics* 8 (2017) 85-112, https://escholarship.org/uc/item/9sb894t0
- **Their vocabulary:** demographic structural theory; state fiscal crisis; elite conflict; popular mobilisation; transformative ideology.
- **Operands:** State, elites, populace.
- **Operators:** Population growth triggers a cycle of state financial crisis, intra-elite and elite-state conflict, popular opposition, and transformative ideology. Formality: **causal-mechanism narrative with a fixed sequence of conditions**; comparative, not formal.
- **Predictive claim:** Conjunction of fiscal crisis, elite division and popular mobilisation predicts state breakdown. Applied to four early modern cases; the 2017 retrospective reviews reception and extensions.
- **Limits:** Four cases; conditions are necessary-conjunction claims, not rates.
- **Relevance:** Source of the "three sector conjunction" idea; shows a minimal structure (three actors, three coupled stresses) that an algebra could encode.

## 6. Turchin's forecasts (2008/2010 *Nature*; *Ages of Discord*, 2016)

- **Citation:** Turchin, "Arise 'cliodynamics'", *Nature* 454: 34-35 (2008); "Political instability may be a contributor in the coming decade", *Nature* 463: 608 (2010), one of the "2020 visions" correspondence pieces (title from validator's knowledge; the quoted sentence below confirmed via secondary sources); "Dynamics of political instability in the United States, 1780-2010", *Journal of Peace Research* 49(4) (2012); *Ages of Discord*, Beresta Books (2016). Self-assessment: Turchin and Korotayev, "The 2010 structural-demographic forecast for the 2010-2020 decade: A retrospective assessment", *PLOS ONE* 15(8): e0237458 (2020), doi:10.1371/journal.pone.0237458.
- **Source:** secondary: https://today.uconn.edu/?p=180536 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC7430736 ; critique: https://newstatesman.com/the-weekend-essay/2023/06/peter-turchins-empty-prophecies
- **Operands/Operators:** As item 4 applied to the US: political-stress indicator composed of wages, elite overproduction and state fiscal health.
- **Predictive claim:** 2010: "50-year instability spikes occurred around 1870, 1920 and 1970, so another could be due around 2020." The 2010 text says "around 2020"; later work projects the Political Stress Indicator into the 2020s, which is where the "mid-to-late 2020s" accounts come from. Turchin and Korotayev (2020) tested it against the Cross-National Time-Series Data Archive and report that protests and riots rose sharply in 2010-2020 in the US, UK and several Western European countries. That is a test, but by the forecast's authors and with no pre-stated threshold. Critics (New Statesman) call the later book banal.
- **Limits:** A 50-year period from three observed spikes; no pre-registered threshold; assessed only by its authors.
- **Relevance:** A cautionary case for the algebra: a forecast loose in timing and magnitude is hard to fail, so the test has to be stated before the outcome.

## 7. Seshat Global History Databank and its critics

- **Citation:** Peter Turchin, Thomas E. Currie, Harvey Whitehouse, Pieter François, Kevin Feeney, Daniel Mullins, Daniel Hoyer and colleagues, "Quantitative historical analysis uncovers a single dimension of complexity that structures global variation in human social organization", *PNAS* 115(2): E144-E151 (2018). DOI 10.1073/pnas.1708800115.
- **Source:** https://discovery-pp.ucl.ac.uk/10041342/1/PNAS-2018-Turchin-E144-51.pdf
- **Their vocabulary:** social complexity, polities, coded variables, principal component.
- **Operands:** 414 polities from 30 world regions over about 10,000 years, coded on 51 variables in nine characteristics (abstract).
- **Operators:** None. This is a **database and statistical description**, not a transformation model. The paper's finding is a single principal component explaining about three-quarters of variation, taken to show that aspects of complexity co-evolve.
- **Predictive claim and how it held up:** The related Seshat paper, Whitehouse et al., "Complex societies precede moralizing gods throughout world history", *Nature* 568: 226-229 (2019), was **retracted by its authors on 7 July 2021** (retraction note *Nature* 595: 320, doi:10.1038/s41586-021-03656-3) after Beheim et al., "Treatment of missing data determined conclusions regarding moralizing gods", *Nature* 595: E29-E34 (2021), doi:10.1038/s41586-021-03655-4, showed 61% of moralizing-gods data points were missing and had been recoded as absences; analysis with extant data or standard imputation reversed the result. Whitehouse et al., "Testing the Big Gods hypothesis with global historical data: a review and 'retake'", *Religion, Brain & Behavior* 13(2): 124-166 (online 2022, issue 2023), published a "retake": correction does not significantly change the main findings, and complexity precedes Big Gods. Separately Slingerland et al. criticised data quality, periodisation, and "data pasting/filling"; Turchin's side says they run a rival project (Database of Religious History). Sources: https://hraf.yale.edu/ehc/documents/1225 ; https://peterturchin.com/publications/testing-the-big-gods-hypothesis-with-global-historical-data-a-review-and-retake/ ; https://peterturchin.com/they-call-it-coding-errors/. Beheim et al.'s abstract-level claims (61%, reversal under imputation) confirmed by validation; Retraction Watch reports the authors' own reanalysis "diluted" their conclusions: https://retractionwatch.com/2021/07/07/critique-topples-nature-paper-on-belief-in-gods/
- **Limits:** Coding by research assistants; missing data treated as absence; correlation not mechanism.
- **Relevance:** A source of *operands with attributes* (a typed feature schema for societies), and a lesson in coding discipline. Not a source of operators.

## 8. Toynbee, *A Study of History* (1934-61)

- **Citation:** Arnold J. Toynbee, *A Study of History*, 12 vols., Oxford University Press, 1934-61.
- **Source:** https://en.wikipedia.org/wiki/A_Study_of_History (secondary)
- **Their vocabulary:** challenge and response; creative minority; mimesis; withdrawal and return; dominant minority; universal state; breakdown.
- **Operands:** Civilisations; within them a creative minority, a mass, and later a dominant minority.
- **Operators:** *Respond to challenge*; *imitate* (mass imitates minority); *withdraw-and-return* (leader retreats, then reintegrates with new capacity). Breakdown occurs when the minority stops responding and the majority no longer follows or follows only under compulsion; the minority becomes a dominant minority forming a universal state. Formality: **narrative typology**; verbs are good but nothing is quantified.
- **Predictive claim:** Civilisations decline from internal failure, not external attack. Widely criticised as non-falsifiable and selective in case choice, most famously by Pieter Geyl (background, not web-checked).
- **Relevance:** Names two operators the others lack: imitation (leader-to-mass) and withdraw-return (agent temporarily leaves the group, returns altered).

## 9. Braudel and the Annales: the longue durée

- **Citation:** Fernand Braudel, "Histoire et sciences sociales: la longue durée", *Annales E.S.C.* 13(4): 725-753, Oct-Dec 1958 (pages from validator's knowledge).
- **Source:** https://www.redalyc.org/pdf/263/26311686007.pdf (secondary) ; https://aeaveiro.pt/biblioteca/download/763/Histoire%20et%20Sciences%20Sociales%20_%20-%20Fernand%20Braudel.pdf (excerpt)
- **Their vocabulary:** événement, conjoncture, structure; longue durée.
- **Operands:** Not actors but *timescales*: surface events, medium-term cycles of groups, near-motionless structures of the milieu.
- **Operators:** None. A **layered-time framework**, a classification.
- **Predictive claim:** None; the claim is that explanation lives in the long structures.
- **Relevance:** Argues for typing every term of an algebra by *rate of change*. Operators that act on fast variables (events) should not be allowed to rewrite slow ones (structures) without an explicit step.

## 10. Namier and prosopography (Namier 1929; Stone 1971)

- **Citation:** Lewis Namier, *The Structure of Politics at the Accession of George III*, Macmillan, 1929 (2nd ed. Macmillan, 1957; 1961 is the Papermac paperback reprint). Lawrence Stone, "Prosopography", *Daedalus* 100(1): 46-79 (Winter 1971).
- **Source:** https://en.wikipedia.org/wiki/The_Structure_of_Politics_at_the_Accession_of_George_III ; https://cbdb.hsites.harvard.edu/prosopography
- **Their vocabulary:** prosopography (Stone: "the investigation of the common background characteristics of a group of actors in history"); faction, office-holders, independents.
- **Operands:** Individual members of a group with biographical attributes (family, office, patronage).
- **Operators:** None formal. Namier's conclusion was that no party system existed; Parliament was factions of office-holders and independents. The method is **attribute tabulation for a named set of actors**.
- **Predictive claim:** Descriptive; overturned the Whig two-party account.
- **Relevance:** Defines the *operand record*: a person with attributes drawn from a collective biography. The algebra needs this layer and prosopography supplies the practice.

## 11. Padgett and Ansell, "Robust Action and the Rise of the Medici" (1993)

- **Citation:** John F. Padgett and Christopher K. Ansell, "Robust Action and the Rise of the Medici, 1400-1434", *American Journal of Sociology* 98(6): 1259-1319 (1993).
- **Source:** https://www.jstor.org/stable/2781822 ; doi:10.1086/230190 (resolves to University of Chicago Press journals, AJS's publisher; landing page not fetched).
- **Their vocabulary:** robust action, multivocality, ambiguity, blockmodel. ("Structural holes" is Burt's 1992 term; the paper is widely read through it, but it is not the paper's own key term.)
- **Operands:** Florentine families as nodes; multiple relation types (marriage, economic ties, patronage, friendship).
- **Operators:** Cosimo's party gained control by spanning structural holes between otherwise separate groups (search summary). The paper's operative claims are that the Medici were the *bridge* across blocks, and that actions were deliberately *multivocal* (readable several ways by different audiences), keeping options open. Formality: **empirical network analysis (block-models on historical relation data)** plus a verbal theory of the operator; the network measures are formal, the theory of action is not.
- **Predictive claim:** Not simply "centrality caused the rise" (the textbook reduction). The claim is structural: the Medici party was a sparse, star-shaped network, marrying into patrician families while doing business with new men, so its members were tied to the Medici and not to each other; the oligarchs were densely interlinked and so could not act decisively. That position plus multivocal, uncommitted action ("robust action") gave Cosimo control (validator's knowledge of the paper; secondary sources confirm the bridging and robust-action points). The small 16-family "Florentine families" teaching dataset (Breiger and Pattison 1986) is derived from Padgett's data.
- **Limits:** One city, one period; the network is a snapshot constructed from records.
- **Relevance:** Key. Shows operator = "span a gap between groups", operand = relation multiplex. Complements the sociology-cluster network algebras by giving a historical case.

## 12. Padgett and Powell, *The Emergence of Organizations and Markets* (2012)

- **Citation:** John F. Padgett and Walter W. Powell (eds.), *The Emergence of Organizations and Markets*, Princeton University Press, 2012.
- **Source:** https://en.wikipedia.org/wiki/The_Emergence_of_Organizations_and_Markets ; https://muse.jhu.edu/book/36479
- **Their vocabulary:** autocatalysis, spillovers, intertwined networks, relations produce actors.
- **Operands:** Actors and relations in multiple networks (production, communication).
- **Operators:** Borrowed from chemistry: autocatalysis. Short-run, actors form relations; long-run, relations produce new actors and forms. Novelty arises from spillovers across intertwined networks. The agent-based models in the first section reportedly generate overlapping production networks (blog summary only). Formality: **agent-based models plus fourteen historical case studies** (medieval Florence to Silicon Valley). Whether the book states a production-rule algebra I could not confirm. *Transposition* is in the book: ch. 6, Padgett, "Transposition and Refunctionality: The Birth of Partnership Systems in Renaissance Florence", pp. 168-207 (JSTOR table of contents), where a relational practice moves from one network domain to another and is refunctioned there; that is a candidate operator the original survey missed.
- **Predictive claim:** Explanatory; not forecasting.
- **Limits:** Edited volume, uneven formality across chapters.
- **Relevance:** The strongest existing statement that the algebra's *operands should be generated by its operators* (relations make actors), which is the right shape for a closed algebra.

## 13. Elias, *The Civilizing Process* and figurational sociology

- **Citation:** Norbert Elias, *Über den Prozess der Zivilisation* (1939), English *The Civilizing Process*; *Die höfische Gesellschaft* (1969; English *The Court Society*, 1983); *Was ist Soziologie?* (1970; *What is Sociology?*, 1978). Dates from validator's knowledge.
- **Source:** https://link.springer.com/chapter/10.1057/9781137312112_18 ; https://library.oapen.org/handle/20.500.12657/58717?show=full (Dunning and Hughes, open access)
- **Their vocabulary:** figuration (configuration), interdependence, civilising process, internalised constraint.
- **Operands:** Individuals in a *figuration*, a network of interdependence; the figuration, not the individual or "society", is the unit.
- **Operators:** Increasing interdependence leads to increasing regulation of behaviour by internalised norms and impulse control (secondary). Elias's game models (from a two-person game to multi-tier multi-person games, as models of shifting power balances) are in *What is Sociology?*, ch. 3 (validator's knowledge, not web-checked).
- **Predictive claim:** Directional long-term trend in European manners; descriptive.
- **Limits:** One region; directionality criticised as teleological (background).
- **Relevance:** Supplies the *unit* of analysis (a figuration) and the insight that structure should be a product of the interdependence of the operands.

## 14. Tilly, *Coercion, Capital, and European States* (1990)

- **Citation:** Charles Tilly, *Coercion, Capital, and European States, AD 990-1990*, Basil Blackwell, 1990.
- **Source:** secondary review pages from search, e.g. https://revistas.usal.es/uno/index.php/0213-2087/article/download/5817/5843/20029
- **Their vocabulary:** coercion-intensive, capital-intensive, capitalised coercion; state formation.
- **Operands:** States, characterised by their stocks of coercion and capital.
- **Operators:** War requires financing; financing shapes the state; states and warmaking shape one another. Three paths: coercion-intensive (Russia, Brandenburg), capital-intensive (Venice, Genoa, the Dutch Republic), and capitalised coercion (France, England). Formality: **typology with a causal mechanism (war -> extraction -> state structure)**.
- **Predictive claim:** The route to the modern national state depends on the mix of capital and coercion. Qualified acceptance in the field; I did not find critiques in this pass. The dictum "War made the state, and the state made war" is from Tilly's introduction to *The Formation of National States in Western Europe* (Princeton, 1975), not from this book, which develops it.
- **Relevance:** Two-resource state-space with a single operator class (extract-to-fight).

## 15. Tilly, repertoires of contention

- **Citation:** Charles Tilly, "Contentious Repertoires in Great Britain, 1758-1834", *Social Science History* 17(2) (1993); *Popular Contention in Great Britain, 1758-1834*, Harvard University Press, 1995. Data: *Contentious Gatherings in Britain, 1758-1834*, ICPSR 8872, doi:10.3886/ICPSR08872.
- **Source:** https://doi.org/10.3886/ICPSR08872 ; https://cambridge.org/core/journals/social-science-history/article/abs/contentious-repertoires-in-great-britain-17581834/57A3688FC69A75A71B22DAFB0B285FDE
- **Their vocabulary:** repertoire of contention; contentious gathering; claims.
- **Operands:** Claimants and targets; a *gathering* is the data unit (at least ten people in a public place making claims that would affect others, ICPSR definition).
- **Operators:** The repertoire is a **finite set of known claim-making forms** a population has, which change slowly: eighteenth-century local, often violent forms gave way from the 1790s to organised national movements addressed to Parliament (reviewer summary). Formality: **event-coded dataset plus concept**; no algebra.
- **Predictive claim:** Collective action choose from available forms, rather than inventing them. Supported by the dataset; I did not find criticism.
- **Relevance:** Excellent: a group's operator set is itself a slowly-changing state variable ("the repertoire"). Suggests the algebra's operators should be indexed by what a given group has available.

## 16. Skocpol, *States and Social Revolutions* (1979)

- **Citation:** Theda Skocpol, *States and Social Revolutions: A Comparative Analysis of France, Russia, and China*, Cambridge University Press, 1979.
- **Source:** https://en.wikipedia.org/wiki/States_and_Social_Revolutions ; https://www.nli.org.il/he/books/NNL_ALEPH997007876747105171/NLI
- **Their vocabulary:** state autonomy, state breakdown, peasant revolution, comparative historical method.
- **Operands:** States as administrative-coercive organisations; classes; peasantry.
- **Operators:** Social revolution arises from the simultaneous occurrence of state breakdown and peasant revolt (summary). Formality: **comparative-case argument**, three cases.
- **Predictive claim:** Conjunction. She explicitly frames the comparison with Mill's methods of agreement and difference (ch. 1; validator's knowledge, not web-checked).
- **Limits:** Three cases, outcome-selected.
- **Relevance:** Gives "state breakdown" as a separate operand state, needed alongside class dynamics.

## 17. Barrington Moore, *Social Origins of Dictatorship and Democracy* (1966)

- **Citation:** Barrington Moore Jr., *Social Origins of Dictatorship and Democracy: Lord and Peasant in the Making of the Modern World*, Boston: Beacon Press, 1966 (validator's knowledge).
- **Source:** https://en.wikipedia.org/wiki/Social_Origins_of_Dictatorship_and_Democracy
- **Operands:** Landed aristocracy, bourgeoisie, peasantry, state.
- **Operators:** Three routes (liberal democratic, fascist, communist) determined by timing of industrialisation and the pre-existing agrarian structure. Conditions for democracy include weakening the landed aristocracy and a revolutionary break; an aristocratic-bourgeois coalition against peasants and workers leads towards fascism. Six main cases (England, France, the United States, China, Japan, India), with Germany and Russia treated comparatively, which is why counts of six and eight both appear.
- **Formality:** Typology of **coalition configurations -> regime outcomes**.
- **Relevance:** Coalition between class-operands as the operator; outputs a regime type. A compact "coalition table" is exactly an operator table.

## 18. Mann, *The Sources of Social Power*, vol. 1 (1986)

- **Citation:** Michael Mann, *The Sources of Social Power*, vol. 1: *A History of Power from the Beginning to A.D. 1760*, Cambridge University Press, 1986 (publisher/year as given by search listing; Sage entry confirms 1986 and 1993 for two volumes).
- **Source:** https://sk.sagepub.com/ency/edvol/embed/power/chpt/mann-michael-1942 ; https://www.cambridge.org/core/product/165BD4D9FF0E918F355468AAE451BF1C
- **Their vocabulary:** IEMP: ideological, economic, military, political power; overlapping networks; extensive vs intensive power (background).
- **Operands:** Not individuals but **networks of interaction** of four kinds, each with its own spatial reach.
- **Operators:** Sources of power are autonomous and sometimes intertwine; no one has analytic precedence. Interplay is the explanation. Formality: **conceptual typology applied narratively**.
- **Relevance:** A ready four-way typing for relation kinds in the algebra; supports "multiplex relations with no privileged layer".

## 19. Tainter, *The Collapse of Complex Societies* (1988)

- **Citation:** Joseph A. Tainter, *The Collapse of Complex Societies*, Cambridge University Press, 1988.
- **Source:** https://en.wikipedia.org/wiki/Joseph_Tainter ; https://www.resilience.org/stories/2012-03-29/collapse-complex-societies-review/
- **Operands:** Societies as problem-solving organisations with a stock of complexity and a resource budget.
- **Operators:** *Invest in complexity* (new institutions, roles). Returns diminish; when marginal return reaches zero or negative, society *involuntarily sheds complexity* (his definition of collapse). Formality: **verbal economic argument** (diminishing marginal returns); not fitted.
- **Predictive claim:** Collapse follows falling marginal returns on complexity. One reviewer says "different rates of declining marginal returns" explains little.
- **Relevance:** Gives a cost-benefit operator for adding structure (offices, rules) and a shedding operator.

## 20. Elite theory: Pareto, Mosca, Michels

- **Citation:** Vilfredo Pareto, *Trattato di sociologia generale* (1916; *The Mind and Society*); Gaetano Mosca, *Elementi di scienza politica* (1896/1923); Robert Michels, *Zur Soziologie des Parteiwesens* (1911; *Political Parties*).
- **Source:** secondary only: https://www.encyclopedia.com/social-sciences-and-law/sociology-and-social-reform/sociology-general-terms-and-concepts/elite ; https://upscsociology.in/what-according-to-robert-michels-is-the-iron-law-of-oligarchy-do-lions-and-foxes-in-vilfredo-paretos-theory-essentially-differ-from-each-other-substantiate/ (exam-prep; weakest source, one description of lions and foxes conflicts with Pareto)
- **Operands:** An organised minority (the political class/elite) and an unorganised majority; elite types (lions: force; foxes: cunning).
- **Operators:** *Circulation of elites* (Pareto): rule alternates between the two types; *political formula* (Mosca) legitimises the ruling minority; *oligarchisation* (Michels): large organisations drift to rule by specialised leaders who put staying in power first, helped by rank-and-file apathy. Formality: **typology plus "law"** (the iron law is stated as a regularity).
- **Predictive claim:** Michels: every large organisation becomes oligarchic. Grounded on the German SPD. Overgeneralised from one party (background).
- **Relevance:** Core. "Circulate", "oligarchise" and "legitimise" are operators on the pair (ruling, ruled); the iron law is an attractor claim.

## 21. Weber, routinisation of charisma

- **Citation:** Max Weber, *Wirtschaft und Gesellschaft* (1922; *Economy and Society*, ed. Guenther Roth and Claus Wittich, 1968), ch. on charismatic authority.
- **Source:** secondary only: https://oyc.yale.edu/node/1793 ; https://hirr.hartfordinternational.edu/?p=4565 ; https://www.cambridge.org/core/books/tiberius-and-the-charisma-of-augustus/augustan-charisma-and-its-transfer/70D3BE226FC04BF5EB2726F74DF04843
- **Operands:** Authority types (charismatic, traditional, rational-legal); leader and followers; office.
- **Operators:** *Routinise*: charismatic authority, resting on a personal bond, cannot survive the leader's loss, so it is transformed into traditional (inheritance, sanctity) or rational-legal (rules) forms. Succession by search, revelation, designation or heredity. Office charisma transfers sanctity to the occupant. Weber never fully defined the process (Cambridge chapter), so application is uneven. Formality: **typology with a transformation named**.
- **Predictive claim:** Charismatic movements either institutionalise or die; broadly accepted, not quantitative.
- **Relevance:** A clean unary operator on a authority-type operand, with a succession sub-operator. Direct use.

## 22. Fogel and cliometrics

- **Citation:** Robert W. Fogel, *Railroads and American Economic Growth*, Johns Hopkins Press (1964; validator's knowledge); Fogel and Engerman, *Time on the Cross* (1974); Gutman, *Slavery and the Numbers Game* (1975).
- **Source:** https://www.nber.org/papers/w19213.pdf ; https://www.nybooks.com/articles/1975/10/02/the-true-tragical-history-of-time-on-the-cross/ ; https://www.press.uillinois.edu/books/?id=p071515. Publisher for the 1964 book not confirmed.
- **Operands:** Economic aggregates (freight cost, national product).
- **Operators:** The counterfactual "social saving": cost of the same freight by rivers and canals absent railroads. Moderately more expensive on most routes; saving below 3% of national product in 1890 (one summary), about 0.6% of GDP for interregional agricultural freight (lecture slides). Formality: **explicit counterfactual estimate**. Critique: it assumes the transport pattern would have stayed the same without railways.
- ***Time on the Cross*:** attracted heavy criticism of data and inference (Fogel and Engerman's 0.7 whippings per hand per year, from Bennet Barrow's diary, was recomputed by critics at about 1.1, mainly by questioning the labour-force denominator; Gutman also argued the per-year average is the wrong framing — "a whipping every 4.56 days". Which critic produced 1.1 is not confirmed.)
- **Relevance:** Method, not model: *counterfactual intervention* as an operator ("remove X, recompute") is what an algebra of interactions would support natively.

## 23. Carneiro, circumscription theory (added)

- **Citation:** Robert L. Carneiro, "A Theory of the Origin of the State", *Science* 169(3947): 733-738 (1970). DOI 10.1126/science.169.3947.733.
- **Source:** https://en.wikipedia.org/wiki/Circumscription_theory ; critiques: Zinkina, Korotayev and Andreev, *Cliodynamics* (2016) cross-cultural re-analysis (plausible in some situations, not enough to support wholesale); Stocker and Xiao, "Early State Formation: A Complete Rejection of the Circumscription Theory", *Social Evolution & History* 18(2) (2019), doi:10.30884/seh/2019.02.09, reject it.
- **Operands:** Villages/groups on land with barriers; population pressure.
- **Operators:** Where groups cannot disperse, *conflict and submission* produce chiefdoms and states. Formality: **verbal causal chain**, tested statistically by others, with mixed results.
- **Relevance:** A one-operator model (conquer when exit is blocked) and an example of an environment variable (exit cost) governing which operators fire.

## 24. North, Wallis and Weingast, *Violence and Social Orders* (2009; added)

- **Citation:** Douglass C. North, John Joseph Wallis, Barry R. Weingast, *Violence and Social Orders: A Conceptual Framework for Interpreting Recorded Human History*, Cambridge University Press, 2009.
- **Source:** https://www.cambridge.org/core/books/violence-and-social-orders/transition-from-limited-to-open-access-orders-the-doorstep-conditions/2994147E12F110E07F11C6EC9F3E401D
- **Operands:** Elite coalitions; orders: limited access (natural state) and open access.
- **Operators:** Violence is contained by creating rents for elites. Doorstep conditions for transition: rule of law for elites, perpetually lived organisations, consolidated control of the military. Transition is two-step: elite relationships become impersonal first, then extend to the wider population. Formality: **typology with named transition conditions**; the transition rule is a precondition list, effectively a guard on a state transition.
- **Relevance:** Strong. Operands: elite coalition; state-set of two orders; guarded transition.

## 25. Bueno de Mesquita et al., *The Logic of Political Survival* (2003; added)

- **Citation:** Bruce Bueno de Mesquita, Alastair Smith, Randolph Siverson, James Morrow, *The Logic of Political Survival*, MIT Press, 2003.
- **Source:** https://en.wikipedia.org/wiki/Selectorate_theory ; critique: Kevin A. Clarke and Randall W. Stone, "Democracy and the Logic of Political Survival", *APSR* 102(3): 387-392 (2008), https://www.sas.rochester.edu/psc/stone/articles/clarkestone2008.pdf ; reply: Morrow, Bueno de Mesquita, Siverson and Smith, "Retesting Selectorate Theory", *APSR* 102(3): 393-400 (2008)
- **Operands:** Leader, selectorate (those with a say in choosing), winning coalition (the subset whose support is needed).
- **Operators:** The leader allocates private goods vs public goods to keep the coalition; large coalitions favour public goods. Formality: **game-theoretic model with formal results**; one of the few here.
- **Predictive claim and test:** Large coalitions yield welfare and growth. Clarke and Stone argue that the original tests, which entered democracy only as residuals from regressing it on W and S, are equivalent to omitting democracy, inducing omitted-variable bias; with democracy controlled, most of the important findings do not survive. Morrow et al. accept the residualisation point but report, with new tests controlling for other elements of democracy, that the theory is robustly supported. So: contested, not refuted.
- **Relevance:** A formally stated model with two set-valued operands (selectorate, winning coalition) and one operator (allocate); the nearest to an executable algebra in this cluster.

## 26. Olson, *The Rise and Decline of Nations* (1982; added)

- **Citation:** Mancur Olson, *The Rise and Decline of Nations*, Yale University Press, 1982.
- **Source:** https://blog.christopherwink.com/2025/06/22/the-rise-and-decline-of-nations/ ; https://marginalrevolution.com/marginalrevolution/2021/12/the-rise-and-decline-and-rise-again-of-mancur-olson.html (secondary)
- **Operands:** Organised interest groups ("distributional coalitions") and the society.
- **Operators:** Stable societies *accumulate* distributional coalitions over time; they slow technology adoption and growth. Formality: **logic-of-collective-action deduction, verbal**.
- **Relevance:** Another slow accumulation operator that explains decline without invoking an external shock.

---

## What this cluster already covers

- **A vocabulary of operators.** Circulate, degenerate, alter, mix, routinise, bridge, co-opt, impose, extract, shed, imitate, withdraw-and-return, accumulate-coalitions, allocate. Many are well named and each is attributable.
- **A small set of state spaces.** Regime types (Polybius), authority types (Weber), access orders (North et al.), asabiya level (Khaldun/Turchin), elite type (Pareto), coalition configuration (Moore).
- **Cycles as the dominant dynamic.** Polybius, Khaldun, Pareto, Turchin and Olson all describe a loop in a state space with an exit condition.
- **Feedback between aggregate sectors** (Turchin/Goldstone) and **between actors and relations** (Padgett).
- **The unit of record.** Prosopography for individuals; Tilly's gathering for events; Seshat's coded polity.
- **Formal pieces that exist.** Turchin's asabiya model (spatial rules), Bueno de Mesquita (game theory), Padgett's agent-based models.

## What it does not cover

- **No operator algebra.** Nobody states closure, composition, identity, inverses or commutativity for these operators. As far as this survey (which read no primary texts) can tell, none of the 26 works asks whether `routinise` then `circulate` equals the reverse. Polybius's table and Weber's succession options are the nearest, and both are single-step.
- **Almost all are aggregate.** Classes, regimes and polities are the operands. Individual-level operands (a person with a role in a group) appear only in prosopography and Padgett, and there with no operators on persons.
- **Interaction between two named parties barely appears.** The models describe a group moving through a state space. They do not say what happens when A *does something to* B inside the group.
- **Poor testing.** A Seshat causal paper retracted; the 2020 forecast loose and self-assessed; selectorate empirics contested; Time on the Cross disputed. Where there are equations there is little validation; where there is validation (cliometrics, Tilly's dataset) there is no model.
- **Cycles are assumed single-path.** Polybius and Khaldun have one trajectory; Moore and Tilly have a few branches. None treats the operator sequence as a choice made by agents.
- **Control is mostly absent.** The only controller-shaped ideas are Polybius's mixed constitution and North et al.'s doorstep conditions. "Predicting and controlling" in the owner's sense is not here.

## Unconfirmed

Revised by validation, 2026-10-29. Items resolved by web search were removed from this list; items resolved only from the validator's own knowledge are marked so in the body and repeated here.

- Exact functional forms of Turchin's asabiya equations and lattice update rules (the existence of both an ODE system and a spatial simulation is confirmed; the equations were not read).
- Whether *Secular Cycles* itself states its model as differential equations (the models are in *Historical Dynamics*; *Secular Cycles* reads as mainly empirical, background only).
- From validator's knowledge, not web-checked: Goldstone 1991 UC Press; Moore 1966 Beacon; Fogel 1964 Johns Hopkins; Braudel pages 725-753; Skocpol's explicit use of Mill's methods; Elias's dates and the location of his game models; the title of Turchin's 2010 *Nature* piece; Khaldun's "three generations / 120 years" wording; Tilly's examples for the three paths; the sparse-vs-dense reading of Padgett and Ansell.
- Which critic produced the 1.1 whippings figure.
- Criticisms of Toynbee (Geyl), Michels and Elias given as background.
- An independent (non-author) statistical test of Turchin's 50-year cycle; only the authors' 2020 self-assessment and journalistic critique were found.

## Missing important work (added by validation)

- Turchin, Currie, Turner and Gavrilets, *PNAS* 2013 (cited in item 3): the real agent-based test of the frontier/warfare mechanism.
- Turchin and Korotayev, *PLOS ONE* 2020 (cited in item 6): the forecast's assessment.
- Daron Acemoglu and James A. Robinson, *Economic Origins of Dictatorship and Democracy*, Cambridge University Press, 2006: a formal game of elites vs citizens with regime transitions (democratise, repress, coup) as equilibrium moves; the closest formal descendant of Moore and a direct candidate for an operator table.
- Peter S. Bearman, *Relations into Rhetorics: Local Elite Social Structure in Norfolk, England, 1540-1640*, Rutgers University Press, 1993: blockmodels of kinship and patronage tracking elite structure across a century; the historical-network companion to Padgett and Ansell.
- Roger V. Gould, *Insurgent Identities: Class, Community, and Protest in Paris from 1848 to the Commune*, University of Chicago Press, 1995: mobilisation as a function of network identity; operands defined by relations, not class labels.
- Charles Tilly (ed.), *The Formation of National States in Western Europe*, Princeton, 1975: source of the war/state dictum.
- Peter Turchin, *End Times*, 2023: the popular statement of elite overproduction, if the forecast thread is followed.

## Validation log (2026-10-29)

1. Ibn Khaldun / Rosenthal — ✎ edition confirmed (1958, Bollingen XLIII, 3 vols); generation arithmetic corrected (3 x 40 = 120, not "3 or 4").
2. Polybius Bk 6 — ✓ six regimes and order (primitive monarchy, kingship, tyranny, aristocracy, oligarchy, democracy, ochlocracy) correct.
3. Turchin, *Historical Dynamics* — ✎ formality: ODE system **and** spatial lattice ABM (ch. 4), not ABM only; Tainter review and 2013 *PNAS* ABM added.
4. Turchin and Nefedov, *Secular Cycles* — ✓ citation; ? whether equations are stated.
5. Goldstone 1991 — ✓ (UC Press from knowledge; Routledge 2016 and *Cliodynamics* 2017 confirmed by original).
6. Turchin forecasts — ✎ *Nature* 463: 608 (2010) cited; "unfalsifiable" softened: the authors did test it (*PLOS ONE* 2020), but self-assessed and without a pre-stated threshold.
7. Seshat *PNAS* 2018 / moralizing gods — ✎ retraction details completed: Whitehouse et al. *Nature* 568 (2019), retracted by authors 7 July 2021; Beheim et al. *Nature* 595: E29-E34 confirmed (61%, reversal); retake RBB 13(2): 124-166.
8. Toynbee — ✓ citation; ? critiques (background).
9. Braudel 1958 — ✓ (pages added from knowledge).
10. Namier / Stone — ✎ Namier 2nd ed. is 1957, not 1961; Stone pages are 46-79, not 46-71.
11. Padgett and Ansell 1993 — ✎ DOI added; "structural holes" flagged as Burt's term; predictive claim corrected from "centrality caused the rise" to the sparse-party vs dense-oligarchs argument plus robust action.
12. Padgett and Powell 2012 — ✎ "transposition" is in the book (ch. 6, pp. 168-207); flagged as a missed operator.
13. Elias — ✎ *Court Society* 1969 (Eng. 1983); game models placed in *What is Sociology?* ch. 3 (knowledge).
14. Tilly 1990 — ✎ "war made the state" is from Tilly 1975, not this book; path examples completed.
15. Tilly repertoires / ICPSR 8872 — ✓ (DOI resolves to ICPSR study 8872).
16. Skocpol 1979 — ✎ Mill's methods resolved yes (knowledge).
17. Moore 1966 — ✎ publisher Beacon; six-vs-eight case count explained.
18. Mann 1986 — ✓.
19. Tainter 1988 — ✓.
20. Pareto / Mosca / Michels — ✓ citations and lions/foxes; ? Michels overgeneralisation critique (background).
21. Weber — ✓ (Roth and Wittich 1968 added).
22. Fogel / Fogel and Engerman / Gutman — ✎ whipping figures attributed correctly (0.7 is F&E; 1.1 is critics' recomputation, critic unnamed); Fogel publisher added.
23. Carneiro 1970 — ✓; Stocker and Xiao 2019 confirmed with title and DOI.
24. North, Wallis and Weingast 2009 — ✓.
25. Bueno de Mesquita et al. 2003 / Clarke and Stone 2008 — ✎ critique restated precisely (residualised democracy = omitted variable); "Chapter 4-5" claim removed as unverified; Morrow et al. 2008 reply added; summary changed from "fail" to "contested".
26. Olson 1982 — ✓.
- Summary finding 2 — ✎ selectorate theory added (the original contradicted its own item 25).
- ✗ removed: nothing fabricated was found.

**Verdict.** The survey is reliable on existence: every one of the 26 works is real and correctly attributed, with no fabrications. Its errors are in the detail and lean one way — toward overstating the field's failures (the "unfalsifiable" forecast, selectorate results that "fail") and understating its formal content (Turchin's ODEs, Padgett's transposition, the sparse-network mechanism behind the Medici). The structural conclusions (rich verbs, aggregate operands, no stated composition laws) survive validation, but rest on secondary sources, since neither the author nor the validator opened the primary texts.
