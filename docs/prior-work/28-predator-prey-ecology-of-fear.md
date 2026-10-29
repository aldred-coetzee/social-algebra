# Prior work, cluster 28: predator-prey mathematics, the ecology of fear, and transfers to human systems

Date: 2026-10-29. Strand: social-algebra. Part of the drive survey (see `notes/2026-10-29-drives-as-the-core.md`). Cross-references `09-biology-ecology.md` (evolutionary games, Price equation, collective motion, SIR) and `07` (Richardson, applied control). Does not repeat them.

## Verification conventions

- Every DOI below was resolved at `api.crossref.org/works/<doi>` on 2026-10-29 unless marked otherwise; "confirmed" means author, year, title, journal and pages matched.
- Equation tags: **[read]** = read at source this session (the Goodwin derivation on hetwebsite.net, a secondary derivation, tagged as such; and, added in validation, the Abrams-Strogatz 2003 equation and fit from the authors' PDF); **[standard]** = standard textbook/abstract account, written from general knowledge and not re-derived from the paper. Most are [standard]. The paywalled Science/Nature/Ecology pages returned 403 or a login redirect, so quantitative claims taken from them come via search-result summaries and are flagged.

## Summary

1. **The mathematics of coupled populations is old, solid, and mostly about two things: what is conserved or stable, and what destabilises it.** Lotka-Volterra gives neutral cycles with a conserved quantity; any realistic saturation (Holling II) makes them unstable (Rosenzweig-MacArthur, paradox of enrichment); competition gives exclusion theorems. These are the "theorems" Aldred wants, and they are real theorems.
2. **The ecology of fear supplies the piece the drive algebra most needs: fear as a cost term that changes approach/forage acts without any consumption occurring.** Brown's giving-up density turns that cost into a measurement; Preisser et al. (2005) find the non-lethal effect on prey demographics at least as strong as consumption, and Zanette et al. (2011) show perceived risk alone cutting annual offspring by 40% (they did not compare it with a lethal treatment). This is the best-evidenced existing formalisation of "fear" as an operator on other behaviour.
3. **Group-living theory (vigilance, selfish herd, dilution, ideal free distribution, producer-scrounger) already contains group-level drive laws**: individual vigilance falls with group size; position in a group changes risk; consumers distribute to equalise payoff. These are the natural "group drive" operators.
4. **Transfers to humans are thin.** Goodwin (1967) is a literal Lotka-Volterra system with real fits to data; Harvie's (2000) negative verdict was largely overturned once a reporting error was corrected (Grasselli & Maheshwari 2017, 2018), though long-run US data show no long cycles (Mohun & Veneziani); Richardson's arms-race equations have a poor empirical record; language competition (Abrams-Strogatz) fits some declines but its structure is not predator-prey. Predator-prey crime, terrorism and fear-of-crime models are mostly theory; I found no fitted ecological landscape-of-fear model of human movement, only lab/VR analogues and correlational mobility studies (D5). The reverse direction, *animals'* landscape of fear of humans, is well tested (D5).
5. **Blunt answer:** the ecological laws transfer as *structural templates* (cost terms, frequency-dependent equalisation, stability conditions); none transfers as a *tested quantitative law* about human drives.

---

## A. Population-interaction mathematics

### A1. Lotka-Volterra predator-prey

- Citations: A. J. Lotka, *Elements of Physical Biology* (Williams & Wilkins, 1925) [book, no DOI; not fetched]. V. Volterra, "Fluctuations in the abundance of a species considered mathematically", Nature 118, 558-560 (1926), DOI 10.1038/118558a0 (confirmed).
- **Equations [standard]:** with prey x and predator y,
  dx/dt = αx − βxy,  dy/dt = δxy − γy.
  Interior equilibrium x* = γ/δ, y* = α/β.
- **Theorem:** the function V(x,y) = δx − γ ln x + βy − α ln y is constant along trajectories (checked by the validator: dV/dt = (δx − γ)(α − βy) + (βy − α)(δx − γ) = 0), so every interior orbit is a closed curve around (x*, y*): neutral cycles. Amplitude is set by initial conditions, not by the system. Time-averages of x and y over a cycle equal x* and y* (Volterra's averaging law); a uniform harvest of both species raises mean prey and lowers mean predator (Volterra's principle). [standard]
- **Empirical standing:** the cycles are *structurally unstable*: any small change to the model (density dependence, saturation) breaks the conserved quantity and yields either a stable point or a limit cycle. The classic Hudson Bay lynx-hare record is often cited but the data are fur-trade returns, and Gilpin (1973), "Do hares eat lynx?", Am Nat 107, 727-730, DOI 10.1086/282870 (confirmed) is the standard cautionary paper on fitting that series: per secondary accounts (not read at source), in parts of the record the lynx peak leads the hare peak, so a predator-prey fit runs the cycle backwards, as if hares ate lynx; trapping effort on the fur returns is the usual suspected cause. Krebs et al. (1995), "Impact of food and predation on the snowshoe hare cycle", Science 269, 1112-1115, DOI 10.1126/science.269.5227.1112 (confirmed), ran field manipulations and found both food and predation shape the cycle, i.e. it is not a two-variable system. Fussmann et al. (2000), "Crossing the Hopf bifurcation in a live predator-prey system", Science 290, 1358-1360, DOI 10.1126/science.290.5495.1358 (confirmed), is a lab chemostat (rotifer-algae) where the system moves between stable point and cycles as nutrient supply varies, matching Rosenzweig-MacArthur-type theory.
- **Operand/operator translation:** operands are two populations (levels); the operator is a bilinear coupling term xy with opposite signs: one's gain is the other's loss. A "predator" and a "prey" are *roles*, not types. For people: two coupled quantities where one's growth is fed by, and drains, the other.
- **Limits:** well-mixed, no saturation, no memory, no behaviour change in prey. The last is exactly what the ecology of fear adds (section B).

### A2. Lotka-Volterra competition and competitive exclusion

- Citations: Gause, *The Struggle for Existence* (1934) [book, not fetched]; G. Hardin, "The competitive exclusion principle", Science 131, 1292-1297 (1960), DOI 10.1126/science.131.3409.1292 (confirmed). Chesson, "Mechanisms of maintenance of species diversity", Annu Rev Ecol Syst 31, 343-366 (2000), DOI 10.1146/annurev.ecolsys.31.1.343 (confirmed). May & Leonard, "Nonlinear aspects of competition between three species", SIAM J Appl Math 29, 243-253 (1975), DOI 10.1137/0129022 (confirmed).
- **Equations [standard]:** dN1/dt = r1 N1 (1 − (N1 + α12 N2)/K1), dN2/dt = r2 N2 (1 − (N2 + α21 N1)/K2).
- **Theorem [standard]:** four outcomes by comparing K1 with α12 K2 and K2 with α21 K1 (each species' ability to invade the other's carrying-capacity state). Species 2 excludes 1 if K1 < α12 K2 and K2 > α21 K1; the reverse for 1 excluding 2. Stable coexistence iff K1 > α12 K2 and K2 > α21 K1 (each invades the other; this implies α12 α21 < 1, intraspecific limitation exceeding interspecific, but α12 α21 < 1 alone is not sufficient, since the K's must also be close enough). If both inequalities reverse (K1 < α12 K2 and K2 < α21 K1) the interior equilibrium is a saddle and the winner depends on initial conditions (priority effect). Chesson's framing: coexistence needs stabilising mechanisms (niche difference) that outweigh fitness differences. May-Leonard (1975): with three species, cyclic dominance gives heteroclinic cycles (rock-paper-scissors dynamics) that are not stable orbits in the symmetric strong-competition case. [standard]
- **Empirical standing:** Gause's Paramecium experiments are the textbook confirmation; field evidence of strict exclusion is weaker because niches differ; modern theory emphasises coexistence mechanisms.
- **Operand/operator translation:** operands are populations; the operator is a *symmetric-sign* coupling (−α ij Nj) set against self-limitation. The theorem is a comparison of two numbers per pair. This is the cleanest "two groups competing for the same resource" template: the matrix of α's is an editable per-group parameter in the sense Aldred's rules prefer.

### A3. Holling's functional responses I, II, III

- Citations: C. S. Holling, "The components of predation as revealed by a study of small-mammal predation of the European pine sawfly", Can Entomol 91, 293-320 (1959), DOI 10.4039/Ent91293-5 (confirmed); Holling, "Some characteristics of simple types of predation and parasitism", Can Entomol 91, 385-398 (1959), DOI 10.4039/Ent91385-7 (confirmed). Holling 1965 (Mem Entomol Soc Can) not checked.
- **Equations [standard]:** intake rate per predator f(N):
  Type I: f = aN up to a ceiling.
  Type II: f = aN/(1 + a h N) (a attack rate, h handling time).
  Type III: f = aN²/(1 + a h N²) (sigmoidal; learning, prey switching, refuges at low N).
- **Theorem/role:** Type II saturates; the proportion of prey killed falls with N (inversely density-dependent), which destabilises. Type III has a region where the killed proportion rises with N, giving a stabilising low-density refuge. [standard]
- **Empirical standing:** forms derived from field data on small mammals (1959a) and the disc experiment (1959b), in which a blindfolded *human* "predator" picked sandpaper discs by touch, so the type II equation was first fitted to a person; widely supported as a descriptive family. Arditi & Ginzburg (1989), "Coupling in predator-prey dynamics: ratio-dependence", J Theor Biol 139, 311-326, DOI 10.1016/S0022-5193(89)80211-5 (confirmed) argue f should depend on N/P; Abrams & Ginzburg (2000), TREE 15, 337-341, DOI 10.1016/S0169-5347(00)01908-X (confirmed) review the prey-, ratio- and predator-dependent debate and conclude the truth is intermediate (their title question answers "neither" in spirit; read from title only).
- **Translation:** the functional response is the *operator's saturation curve*: how much of a drive's object gets consumed as the object becomes plentiful. For human drives this is the first place a "diminishing return" (satiation, handling time) enters.

### A4. Rosenzweig-MacArthur and the paradox of enrichment

- Citations: M. L. Rosenzweig & R. H. MacArthur, "Graphical representation and stability conditions of predator-prey interactions", Am Nat 97, 209-223 (1963), DOI 10.1086/282272 (confirmed). Rosenzweig, "Paradox of enrichment: destabilization of exploitation ecosystems in ecological time", Science 171, 385-387 (1971), DOI 10.1126/science.171.3969.385 (confirmed).
- **Equations [standard]:** dN/dt = rN(1 − N/K) − aNP/(1 + a h N); dP/dt = e aNP/(1 + a h N) − mP.
- **Theorem [standard; algebra re-derived by the validator]:** prey nullcline P = (r/a)(1 − N/K)(1 + a h N) is a hump peaking at N = (K − 1/(a h))/2; predator nullcline is vertical at N* = m/(a(e − m h)) (requires e > m h). If N* lies to the right of the hump's peak the equilibrium is stable; raising K moves the hump right until N* sits left of the peak, where the equilibrium loses stability through a Hopf bifurcation and a limit cycle appears. More food for the prey makes the system oscillate, with troughs that risk extinction.
- **Empirical standing:** Fussmann et al. (2000) crossed the Hopf bifurcation in a live system (above). Paradox-of-enrichment predictions are supported in some lab systems and contested in field data. Standing: a real theorem with partial experimental confirmation.
- **Translation and relevance:** this is a *theorem about control*: increasing an input (resource, supply, stimulation) can destabilise a coupled system. It is the best template for a drive-algebra theorem of the form "raising the supply of X to a drive above a threshold produces oscillation".

---

## B. The ecology of fear

### B1. Lima & Dill 1990 and the foundation

- Citation: S. L. Lima & L. M. Dill, "Behavioral decisions made under the risk of predation: a review and prospectus", Can J Zool 68, 619-640 (1990), DOI 10.1139/z90-092 (confirmed).
- **Content [standard]:** prey trade off foraging gain against risk; the decision is a state-dependent optimisation. This is the root of everything below.

### B2. Brown 1988 and giving-up density

- Citation: J. S. Brown, "Patch use as an indicator of habitat preference, predation risk, and competition", Behav Ecol Sociobiol 22, 37-47 (1988), DOI 10.1007/BF00395696 (confirmed).
- **Equation [standard]:** a forager should quit a patch when its harvest rate H equals the sum of costs: H = C + P + MOC (metabolic cost, predation cost, missed-opportunity cost). The food left behind when it quits is the **giving-up density (GUD)**, measurable in a tray of seeds. Higher perceived predation cost P gives a higher GUD at the same food level.
- **Follow-ups:** Brown & Kotler, "Hazardous duty pay and the foraging cost of predation", Ecol Lett 7, 999-1014 (2004), DOI 10.1111/j.1461-0248.2004.00661.x (confirmed): quantifies the cost of predation in the currency of foregone food ("hazardous duty pay"); the key idea is that fear has a *price in units of the thing the animal wants*.
- **Standing:** widely used method; criticised for ignoring state dependence and for confounds between predation cost and competition, but real.
- **Translation:** GUD is the single best example in this cluster of a *drive-vs-drive exchange rate made measurable*: how much of drive A (hunger) an agent gives up to avoid drive B (fear). For the algebra this is a candidate for a "price" operator between drives.

### B3. Brown, Laundré & Gurung 1999 and the landscape of fear

- Citation: J. S. Brown, J. W. Laundré, M. Gurung, "The ecology of fear: optimal foraging, game theory, and trophic interactions", J Mammal 80, 385-399 (1999), DOI 10.2307/1383287 (confirmed). Laundré, Hernández & Altendorf, "Wolves, elk, and bison: reestablishing the 'landscape of fear' in Yellowstone National Park, U.S.A.", Can J Zool 79, 1401-1409 (2001), DOI 10.1139/z01-094 (confirmed).
- **Content [from abstract/standard]:** predator and prey play a game in which prey allocate foraging and vigilance across space; perceived risk varies over the habitat as a map (the "landscape of fear"), and prey behaviour (where they feed) shifts the dynamics of the trophic interaction beyond the numbers eaten. The 2001 paper proposes this for wolves, elk and bison.
- **Contest:** Kauffman et al. (2010), "Are wolves saving Yellowstone's aspen? A landscape-level test of a behaviorally mediated trophic cascade", Ecology 91, 2742-2755, DOI 10.1890/09-1949.1 (confirmed; title only) tested one headline cascade and (abstract via USGS listing and search summary) found elk browsing on aspen was not lower at sites of higher wolf predation risk and aspen stands were not recovering; and Creel & Christianson (2008), TREE 23, 194-201, DOI 10.1016/j.tree.2007.12.004 (confirmed) argue risk effects and direct predation must be analysed together because behavioural responses may carry little demographic cost. I did not read either.
- **Translation:** the landscape of fear is a *scalar field over places* that modulates every approach act; "fear" is not an act of its own but a field in which acts are priced. Directly usable as the algebra's field/operator form.

### B4. Non-consumptive effects

- **Werner & Peacor** 2003, "A review of trait-mediated indirect interactions in ecological communities", Ecology 84, 1083-1100, DOI 10.1890/0012-9658(2003)084[1083:AROTII]2.0.CO;2 (confirmed via crossref search, DOI lower-cased in the index). **Schmitz, Krivan & Ovadia** 2004, "Trophic cascades: the primacy of trait-mediated indirect interactions", Ecol Lett 7, 153-163, DOI 10.1111/j.1461-0248.2003.00560.x (confirmed).
- **Preisser, Bolnick & Benard 2005**, "Scared to death? The effects of intimidation and consumption in predator-prey interactions", Ecology 86, 501-509, DOI 10.1890/04-0719 (confirmed). **Abstract (seen via MIDAS reposting and search summaries, full text not read):** meta-analysis; "on average, the impact of intimidation on prey demographics was at least as strong as direct consumption". Search summaries of the abstract give intimidation 63% of the total predator effect on prey demographics against 51% for consumption (the shares are of separate experimental contrasts, so they need not sum to 100%), intimidation rising to 85% for cascading effects on prey resources, and stronger effects in aquatic than terrestrial systems. Treat the percentages as indicative.
- **Zanette, White, Allen & Clinchy 2011**, "Perceived predation risk reduces the number of offspring songbirds produce per year", Science 334, 1398-1401, DOI 10.1126/science.1210908 (confirmed). **Abstract (reposted text, checked):** "the perception of predation risk alone reduced the number of offspring produced per year by 40%", in free-living song sparrows with direct predation removed (electric fencing and netting) and predator vs non-predator playbacks. Mechanism per the abstract and press coverage: females laid fewer eggs, fewer eggs hatched and fewer nestlings fledged (parents fed nestlings less). The 53% nestling-survival and ~50% multi-generation population figures sometimes quoted come from the follow-up Allen, Clinchy & Zanette 2022, PNAS 119, e2112404119, DOI 10.1073/pnas.2112404119 (confirmed; not read), not from the 2011 paper.
- **Standing:** strongest empirical result in this cluster that "fear alone" changes outcomes; effect size depends on system and the lab-to-field gap is not closed.
- **Translation:** fear is a *state variable that reduces the yield of other drives (feeding, reproduction) without any loss event*. In an algebra: an operator F acting on the intensity of other drives, multiplicatively or by shifting their exchange rates.

---

## C. Group-living theory

### C1. Pulliam 1973 and vigilance versus group size

- Citation: H. R. Pulliam, "On the advantages of flocking", J Theor Biol 38, 419-422 (1973), DOI 10.1016/0022-5193(73)90184-7 (confirmed).
- **Model [standard]:** if each of n animals scans independently with some probability per unit time, the probability that no one detects an approaching predator falls geometrically with n; so each individual can reduce its own scanning as n grows while the group's detection stays high (the "many eyes" effect).
- **Reviews:** Elgar 1989, Biol Rev 64, 13-33, DOI 10.1111/j.1469-185X.1989.tb00636.x (confirmed); Roberts 1996, "Why individual vigilance declines as group size increases", Anim Behav 51, 1077-1086, DOI 10.1006/anbe.1996.0109 (confirmed; abstract not read; citing papers credit it with the group-vigilance (many-eyes) and individual-risk (dilution) explanations, and it is usually read as also raising food-competition explanations; content unverified); Beauchamp 2008, "What is the magnitude of the group-size effect on vigilance?", Behav Ecol 19, 1361-1368, DOI 10.1093/beheco/arn096 (confirmed).
- **Standing (via search summaries):** Beauchamp 2008 re-examines the claim because an increasing number of studies failed to show the decline, and asks for the effect size; a later mammal meta-analysis (Beauchamp, Li, Yu, Bednekoff & Blumstein et al. 2021, "A meta-analysis of the group-size effect on vigilance in mammals", Behav Ecol 32, 919-925, DOI 10.1093/beheco/arab048, confirmed; abstract via search summary) reported a moderate negative effect (r = −0.44; 296 effect sizes, 97 species) with 43% of effect sizes compatible with null and signs of publication bias. So: robust on average, weak and variable case by case.
- **Translation:** individual vigilance (a fear-driven act) is a *decreasing function of group size* because the group provides the detection. This is a candidate group-to-individual operator: "membership discounts a drive".

### C2. Hamilton 1971, selfish herd, and dilution/confusion

- Citation: W. D. Hamilton, "Geometry for the selfish herd", J Theor Biol 31, 295-311 (1971), DOI 10.1016/0022-5193(71)90189-5 (confirmed; see also 09's treatment of Hamilton 1964).
- **Model [standard]:** each prey has a "domain of danger", the region of space closer to it than to any other individual; a predator striking at a random point kills the nearest. Individuals reduce their domain by moving toward neighbours, so aggregation arises from selfish risk-minimisation with no cooperation.
- **Formalisations:** Viscido, Miller & Wethey 2001, J Theor Biol 208, 315-328, DOI 10.1006/jtbi.2000.2221 (confirmed): simulation of the response of a selfish herd to an outside attack. Reluga & Viscido 2005, "Simulated evolution of selfish herd behavior", J Theor Biol 234, 213-225, DOI 10.1016/j.jtbi.2004.11.035 (confirmed): evolved movement rules. **Corrected by the validator from the abstract:** the earlier claim here ("nearest-neighbour rules do better than move-to-centre") was wrong; the abstract notes that nearest-neighbour-only rules had failed to produce herd-like aggregation, and finds that predation-driven selection evolves rules weighting *more distant* neighbours relatively more, so selfish herding can evolve from local rules.
- **Dilution and confusion:** Foster & Treherne 1981, "Evidence for the dilution effect in the selfish herd from fish predation on a marine insect", Nature 293, 466-467, DOI 10.1038/293466a0 (confirmed): per-capita attack risk falls as group size rises. Turner & Pitcher 1986, "Attack abatement: a model for group protection by combined avoidance and dilution", Am Nat 128, 228-240, DOI 10.1086/284556 (confirmed): combines detection and dilution in one model. The confusion effect (predator success falls with many moving targets) is standard; I did not source a specific paper.
- **Standing:** dilution is well supported in the field; the geometric selfish herd has experimental support in some systems (e.g. fish, frogs, crabs, per standard accounts) and weak support for the "domain of danger" being what individuals actually minimise. Not verified here.
- **Translation:** group formation as a *response to fear*: a fear drive generates affiliation/approach acts, giving a mechanism "fear → seek proximity → group", and a position-dependent risk (edge vs centre) that makes members differ within the same group.

### C3. Optimal foraging: Charnov marginal value theorem

- Citation: E. L. Charnov, "Optimal foraging, the marginal value theorem", Theor Popul Biol 9, 129-136 (1976), DOI 10.1016/0040-5809(76)90040-X (confirmed).
- **Theorem [standard]:** with cumulative gain g(t) in a patch and mean travel time τ, the rate-maximising residence time t* satisfies g′(t*) = g(t*)/(t* + τ), i.e. leave a patch when the instantaneous rate equals the long-run average rate. Longer travel gives longer residence; poorer environment gives longer residence.
- **Human uses:** Pirolli & Card 1999, "Information foraging", Psychol Rev 106, 643-675, DOI 10.1037/0033-295X.106.4.643 (confirmed); Hills et al. 2012, "Optimal foraging in semantic memory", Psychol Rev 119, 431-440, DOI 10.1037/a0027373 (confirmed). Both apply the theorem to cognition (searching information and memory). Not read at source.
- **Translation:** the MVT is the *rule for when a drive's current act is abandoned*; it gives the exchange of "stay on this" vs "switch" in terms of rate of return, and Brown's GUD is the same logic with a fear cost added.

### C4. Fretwell & Lucas and the ideal free distribution

- Citation: S. D. Fretwell & H. L. Lucas, "On territorial behavior and other factors influencing habitat distribution in birds. I. Theoretical development", Acta Biotheor 19, 16-36 (indexed by Crossref as 1969; the issue is conventionally dated 1970), DOI 10.1007/BF01601953 (confirmed).
- **Theorem [standard]:** if consumers are free to move and know patch quality, and payoff in a patch falls with the number of consumers there, then at equilibrium payoffs are equal across occupied patches, giving "input matching": numbers proportional to resource input (for continuous input with no interference). Under interference the match is weaker than proportional.
- **Empirical standing:** Kennedy & Gray 1993, "Can ecological theory predict the distribution of foraging animals? A critical analysis of experiments on the ideal free distribution", Oikos 68, 158 (DOI 10.2307/3545322, confirmed; page 158 start; findings not read, but the title states a critical analysis; standard account is that animals under-match: fewer in rich patches than predicted). Human experiments: Kraft & Baum 2001, J Exp Anal Behav 76, 21-42, DOI 10.1901/jeab.2001.76-21 (confirmed): groups of people choosing between options with different payoff rates distributed in a ratio positively related to the ratio of payoffs, with slopes near but below 1 (undermatching). Madden, Peden & Yamaguchi 2002, "Human group choice: discrete-trial and free-operant tests of the ideal free distribution", JEAB 78, 1-15, DOI 10.1901/jeab.2002.78-1 (confirmed; abstract via search summary): undermatching throughout, s = 0.59 for initial and 0.86 for final choices (Exp. 1), 0.82 (Exp. 2), 0.71 (free-operant Exp. 3), read as a systematic deviation consistent with melioration. Sokolowski, Tonneau & Freixa i Baqué 1999, "The ideal free distribution in humans: an experimental test", Psychon Bull Rev 6, 157-161, DOI 10.3758/BF03210824 (confirmed; abstract via summary): people competing for money came close to IFD predictions, to about the degree seen in other species. Mobbs et al. 2013, "Foraging under competition: the neural basis of input-matching in humans", J Neurosci 33, 9866-9872, DOI 10.1523/JNEUROSCI.2238-12.2013 (confirmed; not read) adds an fMRI version.
- **Translation:** the first equilibrium law in this cluster that has been tested on human groups: *under frequency-dependent payoff, group allocation equalises payoff.* A Nash-like characterisation with a fixed-point statement the algebra can take over.

### C5. Producer-scrounger games

- Citations: Barnard & Sibly, "Producers and scroungers: a general model and its application to captive flocks of house sparrows", Anim Behav 29, 543-550 (1981), DOI 10.1016/S0003-3472(81)80117-0 (confirmed). Vickery, Giraldeau, Templeton, Kramer & Chapman, "Producers, scroungers, and group foraging", Am Nat 137, 847-863 (1991), DOI 10.1086/285197 (confirmed, full author list matches Crossref). Giraldeau & Caraco, *Social Foraging Theory* (Princeton, 2000) [book, not fetched].
- **Model [standard]:** a producer finds food; a scrounger exploits others' finds. Payoff to each is frequency dependent: scrounger payoff falls as scroungers become common. The stable mix is where payoffs equalise, i.e. the same equalisation logic as the IFD; Vickery et al. give an evolutionarily stable strategy for the group.
- **Human:** Rendell et al. 2010, "Why copy others? Insights from the social learning strategies tournament", Science 328, 208-213, DOI 10.1126/science.1184719 (confirmed): a computer tournament in which strategies that relied heavily on copying (scrounging on others' discoveries) did best; Kameda & Nakanishi 2002, Evol Hum Behav 23, 373-393, DOI 10.1016/S1090-5138(02)00101-0 (confirmed): models and tests cost-benefit of social learning. Neither is a direct test of producer-scrounger payoff equalisation in people; I did not read either at source.
- **Translation:** two *roles* (find / exploit) with a frequency-dependent payoff and a stable mixture; a dual to Hawk-Dove from 09.

---

## D. Transfers to human social systems

### D1. Goodwin 1967 class-struggle cycle

- Citation: R. M. Goodwin, "A growth cycle", in C. H. Feinstein (ed.), *Socialism, Capitalism and Economic Growth* (Cambridge UP, 1967). [Book chapter; no DOI found. Citation confirmed by search, which reproduces it in secondary sources. Crossref lists Goodwin 1955, "A model of cyclical growth", DOI 10.1007/978-1-349-08437-1_10, which is a different, earlier piece.]
- **Equations [read in a secondary derivation, hetwebsite.net/het/essays/multacc/goodw2.htm]:** u = wage share, m = employment rate, v = capital-output ratio, q = productivity growth, n = labour-supply growth, Phillips curve wage growth = −a + b m:
  dm/dt = [1/v − (q + n) − u/v] m,  du/dt = [−(a + q) + b m] u.
  Equilibrium u* = 1 − v(q + n), m* = (a + q)/b. Integrating gives the same type of conserved quantity as Lotka-Volterra: −(a+q) ln m + b m = [1/v − (q+n)] ln u − u/v + c, so orbits are closed and clockwise (with wage share on the horizontal axis). (Validator re-derived: this is the LV integral with x = m, y = u, α = 1/v − (q+n), β = 1/v, δ = b, γ = a + q; equilibria and integral correct.) The employment rate plays the role of prey (growth fed by capital), the wage share of predator.
- **Standing:** Harvie 2000, "Testing Goodwin: growth cycles in ten OECD countries", Camb J Econ 24, 349-376, DOI 10.1093/cje/24.3.349 (confirmed): per the summary I found, the qualitative evidence for Goodwin-type cycles is encouraging but the estimated parameters poorly predict the centres of the cycles. Grasselli & Maheshwari 2017, "A comment on 'Testing Goodwin'", Camb J Econ 41, 1761-1766, DOI 10.1093/cje/bex018 (confirmed), and Grasselli & Maheshwari 2018, Metroeconomica 69, 619-643, DOI 10.1111/meca.12204 (confirmed) re-test. **Abstracts read (arXiv 1803.01527, 1803.01536):** correcting a *reporting mistake* in some of Harvie's estimated parameters gives realistic Phillips-curve parameters and equilibrium employment rates with on average one tenth of Harvie's relative error; the 2018 paper (capital accumulation rate not fixed at one) reports "near perfect agreement" between estimated equilibrium employment and empirical averages and much better wage-share estimates. So Harvie's negative verdict on the cycle *centres* does not stand. Against that, Mohun & Veneziani, "Goodwin cycles and the U.S. economy, 1948-2004" (MPRA paper 30444; book chapter in Flaschel & Landesmann eds., *Mathematical Economics and the Dynamics of Capitalism*, Routledge 2008; abstract read on MPRA/IDEAS) find a sharp break around 1980 and **no long-run cycles** in US data, only short detrended Goodwin cycles roughly aligned with NBER troughs; Barbosa-Filho & Taylor 2006, Metroeconomica 57, 389-411, DOI 10.1111/j.1467-999X.2006.00250.x (confirmed; not read) report clockwise distributive cycles in US data with a structuralist variant. Net: real empirical engagement, centres now well estimated, cyclical dynamics only partly supported, and the same structural instability as Lotka-Volterra.
- **Translation:** this is the one worked case where *two human collective quantities are explicitly modelled as predator and prey.* The coupling is institutional (bargaining power rises with employment, which cuts profit), not a drive, but the algebraic form is the one the strand wants.

### D2. Richardson arms-race equations

- Source: L. F. Richardson, *Arms and Insecurity* (1960) [book; not fetched]. See 07 for the model; not repeated.
- **Standard form [standard]:** dx/dt = k y − α x + g, dy/dt = l x − β y + h (k, l reaction to the rival's arms; α, β fatigue/cost; g, h grievance). Stable if αβ > kl; otherwise runaway or mutual disarmament.
- **Standing:** Rattinger, "Empirical validation of Richardson models of arms races" (1984 chapter, DOI 10.1007/978-1-4613-2805-6_8, confirmed), and Majeski & Jones 1981, "Arms race modeling: causality analysis and model specification", J Conflict Resolut 25, 259-288, DOI 10.1177/002200278102500203 (confirmed; abstract via bibliographic record): causality analysis of twelve commonly proposed arms-race dyads found expenditures independent in a majority, and where interdependent the traditional Richardson specification was not supported. Brito & Intriligator 1999, "Increasing returns to scale and the arms race: the end of the Richardson paradigm?", Def Peace Econ 10, 39-54, DOI 10.1080/10430719908404915 (confirmed) argue for replacing it. Poor record.
- **Translation:** linear coupled response. **Corrected:** this is *not* Lotka-Volterra (LV couples bilinearly, x·y; Richardson is linear in x and y): it is a linear system with positive off-diagonals (mutual stimulation), stable iff αβ > kl (trace −α−β is always negative, so the determinant decides). Its stability condition is a matrix criterion on a drive-coupling matrix.

### D3. Abrams & Strogatz 2003 language competition

- Citation: D. M. Abrams & S. H. Strogatz, "Modelling the dynamics of language death", Nature 424, 900 (2003), DOI 10.1038/424900a (confirmed). Mira & Paredes, "Interlinguistic similarity and language death dynamics", Europhys Lett 69, 1031-1034 (2005), DOI 10.1209/epl/i2004-10438-4 (confirmed). Abrams, Yaple & Wiener, "Dynamics of social group competition: modeling the decline of religious affiliation", Phys Rev Lett 107, 088701 (2011), DOI 10.1103/PhysRevLett.107.088701 (confirmed).
- **Equation [read: author PDF, validator]:** x fraction speaking X, s relative status of X, 1−s of Y; dx/dt = y P_yx(x,s) − x P_xy(x,s) with P_yx = c x^a s, P_xy = c (1−x)^a (1−s):
  dx/dt = c[(1 − x) x^a s − x (1 − x)^a (1 − s)].
  (The rate constant c was missing in the previous version.) Fitted to 42 regions in Peru, Scotland, Wales, Bolivia, Ireland and Alsace-Lorraine: a = 1.31 ± 0.25 (mean ± s.d.), "roughly constant across cultures" (Abrams & Strogatz 2003). The exponent is called volatility in later literature.
- **Result [read]:** the paper states that under mild assumptions there are three fixed points of which only x = 0 and x = 1 are stable, so "two languages cannot coexist stably". **Corrected:** the previous version said that for s ≠ 1/2 "one language is driven to extinction and the other is the attractor"; in fact both endpoints are attractors and the interior point is an unstable threshold, so which language dies depends on s *and* the initial share x(0) (bistability). The validator checked the exponent dependence: near x = 0, dx/dt ≈ c[s x^a − (1−s) x], negative for a > 1 (x = 0 stable) but positive for a < 1, so for a < 1 the endpoints are unstable and a coexistence point is stable; a = 1 is the borderline. The paper also notes that feedback control of s can stabilise a bilingual point. Fitted curves shown for Scottish Gaelic (Sutherland), Quechua (Huanuco), Welsh (Monmouthshire, all Wales).
- **Critique:** not predator-prey; it is a two-state conversion process, closer to the voter-model/SIS family (cross-ref 05). Mira & Paredes add the bilingual state and show coexistence with enough similarity. Patriarca & Leppänen 2004, "Modeling language competition", Physica A 338, 296-299, DOI 10.1016/j.physa.2004.02.056 (confirmed; not read) add geography; Vazquez, Castelló & San Miguel 2010, J Stat Mech P04007, DOI 10.1088/1742-5468/2010/04/P04007 (confirmed; not read) relate the model to agent-based versions, where a = 1 is the voter model and the a < 1 / a > 1 split is the order-disorder transition. The religion model reuses the structure with "utility" in place of status.
- **Translation:** two groups competing for members through *a single scalar, status*; the operator is "convert"; which group wins is set by status and starting share together (an unstable threshold between two absorbing states), and the exponent a decides whether coexistence is possible at all. Useful because the one parameter is a drive-like quantity.

### D4. Predator-prey and competition models of crime, policing, gangs, terrorism

- Gangs: Brantingham, Tita, Short & Reid, "The ecology of gang territorial boundaries", Criminology 50, 851-885 (2012), DOI 10.1111/j.1745-9125.2012.00281.x (confirmed). Via abstract summaries (NCJRS/Georgia Tech copies; full text not read): spatial Lotka-Volterra competition models among 13 rival gangs in LAPD's Hollenbeck division produced estimated territorial boundaries, and 563 between-gang shootings clustered along them (highest concentration within about two blocks). The previous version's parenthesis that territories came "not from police or geographic data" was unsupported and is removed; the model is anchored at known gang locations, but the exact inputs were not checked. This is competition between gangs, not police-versus-criminal. A sibling paper (Crime Science 8, 2019, DOI 10.1186/s40163-019-0102-3, confirmed) extends the line.
- Crime hotspots: Short, D'Orsogna, Pasour, Tita, Brantingham, Bertozzi & Chayes, "A statistical model of criminal behavior", Math Models Methods Appl Sci 18, 1249-1267 (2008), DOI 10.1142/S0218202508003029 (confirmed; author list matches Crossref). Review: M. R. D'Orsogna & M. Perc, "Statistical physics of crime: a review", Phys Life Rev 12, 1-21 (2015), DOI 10.1016/j.plrev.2014.11.001 (confirmed). Reaction-diffusion with an "attractiveness" field; cited in the review as matching hotspot dynamics qualitatively.
- Police as predator, criminals as prey: various works exist (a gang-police model with disease, a Ghanaian thesis fitting a 2000-2010 series with a period of about 12 months, a 2024 kidnapping paper; all from search results and not verified). The Ghanaian fit is the closest to data, a thesis, with assumptions built into the estimated parameters. **No rigorous test found.**
- Terrorism: Udwadia, Leitmann & Lambertini, "A dynamical model of terrorism", Discrete Dyn Nat Soc 2006, article 85653, DOI 10.1155/DDNS/2006/85653 (confirmed): three groups (active terrorists, those open to both messages, pacifists) under two interventions (force against terrorists, persuasion toward pacifism); the authors state it can be tested against field data and it has not been (I found no test). Castillo-Chavez & Song, "Models for the transmission dynamics of fanatic behaviors", in *Bioterrorism: Mathematical Modeling Applications in Homeland Security* (SIAM, 2003), DOI 10.1137/1.9780898717518.ch7 (confirmed): epidemic form. Nuño, Herrero, Primicerio, "A triangle model of criminality", Physica A 387, 2926-2936 (2008), DOI 10.1016/j.physa.2008.01.076 (confirmed), and "A mathematical model of a criminal-prone society", Discrete Contin Dyn Syst S 4, 193-207 (2011), DOI 10.3934/dcdss.2011.4.193 (confirmed): coupled-population models of criminals, victims and police.
- **Translation:** in all of these the predator's drive is a policy parameter (enforcement rate) and the prey's response is a fixed coefficient. No model puts fear in the prey as a state that changes their behaviour, which is the ecology-of-fear addition.

### D5. Fear of crime as landscape of fear

- Search turned up human-geography "landscapes of fear" (Tuan 1979 and Davis 1998 are the usual references; not retrieved) treated as a social concept, a virtual-environment pedestrian study (60 participants; fear raised by narrow routes, hidden spaces, litter), a South African study finding that place use and avoidance do not always track crime hotspots, and urban-park work using prospect-refuge theory (concealment raises perceived danger). All via search snippets; none verified.
- **Added by the validator.** (i) *Humans as the predator in an animal landscape of fear* is a well-tested line: Darimont et al. 2015, "The unique ecology of human predators", Science 349, 858-860, DOI 10.1126/science.aac4249; Clinchy et al. 2016, "Fear of the human 'super predator' far exceeds the fear of large carnivores in a model mesocarnivore", Behav Ecol 27, 1826-1832, DOI 10.1093/beheco/arw117; Smith et al. 2017, "Fear of the human 'super predator' reduces feeding time in large carnivores", Proc R Soc B 284, 20170433, DOI 10.1098/rspb.2017.0433; Suraci et al. 2019, "Fear of humans as apex predators has landscape-scale impacts from mountain lions to mice", Ecol Lett 22, 1578-1586, DOI 10.1111/ele.13344; Zanette et al. 2023, "Fear of the human 'super predator' pervades the South African savanna", Curr Biol 33, 4689-4696, DOI 10.1016/j.cub.2023.08.089 (per coverage: ~95% of species ran or abandoned waterholes faster to human voices than to lions); Gaynor et al. 2018, Science 360, 1232-1235, DOI 10.1126/science.aar7121 (human disturbance shifts wildlife to nocturnality). All DOIs confirmed; findings from titles and press/abstract summaries, not read. (ii) *Human lab analogues of fear-priced foraging* exist: Silston, Wise, Qi, Sui, Dayan & Mobbs 2021, "Neural encoding of perceived patch value during competitive and hazardous virtual foraging", Nat Commun 12, 5478, DOI 10.1038/s41467-021-25816-9 (confirmed; abstract via summary): people trade reward, threat and competition into a "perceived patch value". (iii) *Correlational human mobility studies* exist: a Chilean study combining mobile-phone tracking with reported insecurity found perceived insecurity associated with lower mobility, more so for women; an SFU dissertation built a fear-of-crime pedestrian navigation model and validated it in VR with 60 subjects (both seen via search only, citations not resolved). (iv) Field reviews: Gaynor, Brown, Middleton, Power & Brashares 2019, "Landscapes of fear: spatial patterns of risk perception and response", TREE 34, 355-368, DOI 10.1016/j.tree.2019.01.004; Bleicher 2017, "The landscape of fear conceptual framework: definition and review of current applications and misuses", PeerJ 5, e3772, DOI 10.7717/peerj.3772 (both confirmed; not read).
- **Finding (narrowed by the validator):** I found no study that fits an *ecological* landscape-of-fear model (risk field priced against foraging gain) to real human movement or crime data. Weaker versions exist (VR validation, correlational mobility data, lab foraging under threat), so "no tested model" overstates the gap; "no field-fitted model" is accurate. The mismatch finding (avoidance not tracking actual crime) is itself informative: perceived risk and actual risk need separate variables, as in the ecology literature (Creel and Christianson).

### D6. Competing firms, parties, technologies (Lotka-Volterra in economics)

- Search surfaced two working papers on Lotka-Volterra competition applied to market share and bank competition (SSRN 4881238, 2024; SSRN 7352501, 2026; both existence confirmed by Crossref listing only; content not assessed). I did not find a peer-reviewed canonical source in this session; Marchetti/Modis-type substitution work is **unconfirmed**. Treat the firms/parties/ideas transfer as mostly illustrative.

---

## E. Which laws plausibly transfer, and on what assumptions

| Ecological law | Plausible human-drive reading | Assumptions needed | Status |
|---|---|---|---|
| Fear as a cost in the patch-leaving rule (Brown) | Fear shifts the exchange rate between acts: approach/forage acts are dropped when fear cost exceeds their rate of return | A common currency for the drives (rate of gain); a measurable cost | Template transfers; no literal human GUD, but human prices of risk exist in money (hedonic house prices, e.g. Linden & Rockoff 2008) and in lab virtual foraging (Silston et al. 2021) |
| Non-consumptive effects (Preisser, Zanette) | Threat reduces the yield of other drives with no loss event | Perceived threat is an input; the effect on reproduction-like outputs is measurable | Strongest evidence is animal; human parallel (stress, performance) not surveyed |
| Landscape of fear (field over space) | Perceived-risk field over places/people modulating approach | Risk map is learnable and stable | Concept used in human geography without model tests |
| Many-eyes vigilance | Individual vigilance falls with group size | Independent scanning, shared detection | Average effect real, weak and variable |
| Dilution / selfish herd | Fear produces affiliation and position-dependent risk | Predator attack random in space | Dilution well supported in animals; geometric version partly |
| Marginal value theorem | Leave an activity when marginal rate equals average rate | Patchy resources, known gain curve | Applied to cognitive search; thin elsewhere |
| IFD (payoff equalisation) | Members distribute so payoffs equalise | Free movement, payoff knowledge | Tested on people in lab; undermatching |
| Producer-scrounger stable mix | Roles in a group settle where payoffs equalise | Frequency-dependent payoff | Tournament evidence on social learning |
| Lotka-Volterra coupling | Two collective quantities, one feeding on the other | Well-mixed, no saturation | Goodwin only; mixed fit |
| Rosenzweig-MacArthur instability | Raising supply to a coupled system can destabilise it | Saturating response, delay | Theorem; one lab confirmation (non-human) |
| Competitive exclusion | One group wins unless self-limitation exceeds cross-limitation | Single shared resource | Language/religion models fit decline curves |

**Transfers that failed or are weak**
- Richardson's linear arms-race coupling: poor fit in the empirical record found here.
- Strict Lotka-Volterra (neutral cycles) as a literal description of anything: structurally unstable; applies as a pattern, not a prediction.
- Police-as-predator crime models: almost entirely theory.

**What the ecology literature does not give a drive algebra**
- Drives are not populations: ecology's quantities are counts; a drive level is an internal state. Using Lotka-Volterra on drive intensity needs an argument that intensity behaves like a conserved or reproducing quantity. Nothing here supplies it.
- Ecological fear acts on foraging and reproduction; there is no counterpart in this cluster for curiosity or desire (the other two on Aldred's list). That belongs to clusters 15-17.

## F. What exists versus what does not

**Exists:**
- Real theorems on coupled quantities: LV conserved quantity, competitive exclusion conditions, Hopf destabilisation via enrichment, MVT, IFD, ESS mixes of producer-scrounger.
- A measurable fear cost (giving-up density) and a meta-analysis showing non-lethal effects comparable to lethal ones.
- Group-size laws for vigilance and risk, with variable but real support.
- Human tests: IFD in lab groups (close to prediction, systematic undermatching); Goodwin centres in OECD data (good once Harvie's error is corrected; long cycles absent in US data); language decline (fits).

**Does not exist (found none):**
- A composable algebra in which fear, hunger-like and approach drives are operators with stated composition rules. The ecology of fear is verbal plus optimisation models, not an algebra.
- A human giving-up-density in the strict sense (food or effort left behind in a patch as a function of threat, in the field). **Narrowed by the validator:** the *price of fear* has been measured for people in other currencies: Linden & Rockoff 2008, "Estimates of the impact of crime risk on property values from Megan's laws", Am Econ Rev 98, 1103-1127, DOI 10.1257/aer.98.3.1103 (confirmed; finding from memory, not read: house prices very close to a newly arrived registered sex offender fall by roughly 4%) is a hazardous-duty-pay analogue, as is the compensating-differential/value-of-statistical-life literature (not surveyed); and Silston et al. 2021 measure reward-threat trade-offs in virtual foraging.
- A field-fitted landscape-of-fear model for people moving through cities (VR validations and correlational mobility studies exist; see D5).
- A fitted, tested police-criminal or counter-terrorism predator-prey model.
- Any ecological-law analogue for curiosity or desire.
- Evidence that these laws predict individual human behaviour (the warning in the 10-29 note applies: only aggregate claims have done better).

## Unconfirmed

- Books (no DOI, not retrieved): Lotka 1925; Gause 1934; Richardson 1960 (*Arms and Insecurity*); Giraldeau & Caraco 2000; Krause & Ruxton 2002; Tuan 1979 (*Landscapes of Fear*); Davis 1998 (*Ecology of Fear*); Goodwin 1967 chapter (citation confirmed via secondary sources only).
- Holling 1965 monograph; Tilman 1982 resource competition; Elton & Nicholson 1942 lynx data; Turchin 2003.
- (Beauchamp et al. 2021, Madden et al. 2002, Brito & Intriligator 1999, Majeski & Jones 1981, and the Short et al. and Vickery et al. author lists were resolved in validation and moved into the text.)
- Roberts 1996 content (abstract not read; reason: paywalled, no abstract in search).
- Laundré, Hernández & Ripple 2010 review; Ripple & Beschta wolf-cascade papers; exact Preisser percentages (abstract summary only, not the full text).
- Linden & Rockoff 2008 effect size (DOI confirmed; the ~4% figure is from memory).
- Kraft & Baum 2001 slope values ("near but below 1"; abstract not read).
- The Ghanaian police-criminal thesis, the gang-police disease paper, the 2024 kidnapping paper, the pedestrian virtual-environment study, and the South African place-avoidance study: seen in search results only.
- Statements marked "as I recall" in sections A1, B3, C1, C2 are from memory and not verified.

## Validation log (2026-10-29)

Method: every DOI in the file (59, plus 22 added) resolved at api.crossref.org; author, year, title, journal, volume and pages compared. Every equation re-derived by hand (LV integral, Volterra averaging and harvest principle, LV competition invasion conditions, Holling II/III per-capita kill rates, R-M nullclines and N*, MVT, Richardson stability, Goodwin integral, Abrams-Strogatz fixed-point stability). Abstracts read where reachable; publisher pages mostly 403.

Mathematics
- ✓ LV predator-prey, equilibrium, first integral V (dV/dt = 0 verified), averaging law, Volterra's principle.
- ✎ LV competition: invasion conditions correct; "equivalently intraspecific > interspecific" overstated (implies α12α21 < 1, not equivalent).
- ✓ Holling I/II/III forms and density-dependence of per-capita kill (II decreasing; III increasing below N = 1/√(ah)). ✎ added that the disc experiment used a blindfolded human.
- ✓ Rosenzweig-MacArthur: N* = m/(a(e − mh)) verified; hump peak (K − 1/(ah))/2 added; Hopf with rising K correct.
- ✓ Charnov MVT condition g′(t*) = g(t*)/(t* + τ) and its comparative statics.
- ✓ Brown 1988 H = C + P + MOC quitting rule (standard; not read).
- ✓ Goodwin equations, equilibria and integral (mapped to LV parameters).
- ✎ Richardson: stability αβ > kl correct; "Lotka-Volterra with positive off-diagonals" wrong (linear, not bilinear).
- ✎ Abrams-Strogatz: rate constant c restored; a = 1.31 ± 0.25 over 42 regions confirmed [read]; outcome is bistable (depends on s and x(0)), not "for s ≠ 1/2 one language is the attractor"; a < 1 gives stable coexistence.

Works
- ✓ Volterra 1926; Gilpin 1973 (✎ finding added from secondary accounts); Krebs et al. 1995; Fussmann et al. 2000; Hardin 1960; Chesson 2000; May & Leonard 1975; Holling 1959a, 1959b; Arditi & Ginzburg 1989; Abrams & Ginzburg 2000; Rosenzweig & MacArthur 1963; Rosenzweig 1971; Lima & Dill 1990; Brown 1988; Brown & Kotler 2004; Brown, Laundré & Gurung 1999; Laundré et al. 2001; Creel & Christianson 2008; Werner & Peacor 2003; Schmitz et al. 2004.
- ✎ Kauffman et al. 2010: "as I recall" replaced with abstract finding (browsing not reduced in high-risk sites).
- ✎ Preisser et al. 2005: 63%/51%/85% confirmed via abstract summaries; "other measure" mislabel fixed (51% is consumption).
- ✎ Zanette et al. 2011: 40% confirmed from abstract text; "sat on eggs less / chicks weighed less" replaced with abstract mechanism; 53%/50% figures attributed to Allen et al. 2022.
- ✓ Pulliam 1973; Elgar 1989; Beauchamp 2008. ? Roberts 1996 (content unverified). ✎ Beauchamp et al. 2021: DOI added, figures confirmed.
- ✓ Hamilton 1971; Viscido et al. 2001; Foster & Treherne 1981; Turner & Pitcher 1986. ✎ Reluga & Viscido 2005: claimed finding was wrong, replaced from abstract.
- ✓ Charnov 1976; Pirolli & Card 1999; Hills et al. 2012.
- ✓ Fretwell & Lucas 1969/70; Kennedy & Gray 1993; ? Kraft & Baum 2001 (record confirmed; slope claim not checked). ✎ Madden et al. 2002: DOI added, s values confirmed and extended. ✎ Sokolowski et al. 1999 added (close to IFD).
- ✓ Barnard & Sibly 1981; ✎ Vickery et al. 1991 (author list now confirmed); ✓ Rendell et al. 2010; ✓ Kameda & Nakanishi 2002.
- ? Goodwin 1967 (book chapter, no DOI; citation standard). ✓ Goodwin 1955 note.
- ✎ Harvie 2000 / Grasselli & Maheshwari 2017, 2018: consequence of the "error" made explicit from the abstracts (centres well estimated after correction); Mohun & Veneziani and Barbosa-Filho & Taylor 2006 added.
- ✓ Rattinger 1984. ✎ Majeski & Jones 1981: identified, DOI added, finding confirmed. ✎ Brito & Intriligator 1999: DOI added.
- ✓ Abrams & Strogatz 2003 (now [read]); Mira & Paredes 2005; Abrams, Yaple & Wiener 2011.
- ✎ Brantingham et al. 2012: unsupported "not from police or geographic data" removed; 13 gangs, 563 shootings added. ✓ Brantingham, Valasik & Tita 2019.
- ✓ Short et al. 2008 (author list now confirmed); D'Orsogna & Perc 2015; Udwadia et al. 2006 (abstract matches, including the testability statement); Castillo-Chavez & Song 2003; Nuño et al. 2008, 2011.
- ? SSRN working papers (D6), Ghanaian thesis, gang-police paper, kidnapping paper, VR pedestrian study, South African and Chilean studies: search-only.
- ✗ None removed as fabricated.

Closing claims
- ✎ "No human giving-up density": true only literally; human prices of risk exist (hedonic crime pricing, Linden & Rockoff 2008; virtual foraging under threat, Silston et al. 2021).
- ✎ "No tested landscape-of-fear model for people": narrowed to "no field-fitted model"; VR and correlational mobility work exists; and animal landscapes of fear *of humans* are well tested (Clinchy 2016, Smith 2017, Suraci 2019, Zanette 2023, Darimont 2015, Gaynor 2018).

Added as clearly missing: Gaynor et al. 2019 TREE and Bleicher 2017 (landscape-of-fear reviews); the human "super predator" series; Allen et al. 2022 PNAS; Silston et al. 2021; Mobbs et al. 2013; Sokolowski et al. 1999; Mohun & Veneziani; Barbosa-Filho & Taylor 2006; Majeski & Jones 1981; Patriarca & Leppänen 2004; Vazquez, Castelló & San Miguel 2010; Linden & Rockoff 2008. Still missing, not added: Volterra's 1926 Lincei memoir, Sutherland 1983 interference IFD, Abrams 2000 review of predator-prey adaptive behaviour.

**Verdict.** Bibliographically sound: all 59 DOIs resolve and match, nothing fabricated, and the mathematics of the core models is correct. The errors are in what the papers were said to find, mostly where the author wrote from memory or from search snippets: Reluga & Viscido reversed, Abrams-Strogatz's outcome described wrongly (bistable, not status-determined), Richardson mislabelled as Lotka-Volterra, and Goodwin's empirical standing understated because the consequence of the Harvie correction was not stated. The two closing "does not exist" claims were overstated and are narrowed.

## Licences of quoted and transcribed material (2026-10-30)

No tables or datasets are transcribed in this file; the material below is short quotation, restated equations, or citation only. Everything else is citation, fact or number, which is free.

| Source | Licence | Use |
|---|---|---|
| Abrams & Strogatz 2003, Nature 424, 900 | not determined; publisher copyright (Springer Nature) presumed | one 4-word quotation, now attributed inline; restated equation and fitted values (a = 1.31 ± 0.25, 42 regions); short quotation "two languages cannot coexist stably" |
| Preisser, Bolnick & Benard 2005, Ecology 86, 501 | not determined; publisher copyright (Ecological Society of America) presumed | one short abstract quotation (under 20 words) |
| Zanette et al. 2011, Science 334, 1398 | not determined; publisher copyright (AAAS) presumed | one short abstract quotation (under 25 words) |
| Goodwin derivation on hetwebsite.net (secondary) | not determined; presumed copyright of site author | restated equations only, no text copied |
| All other cited papers and books (Lotka, Volterra, Holling, Rosenzweig-MacArthur, Brown, Pulliam, Hamilton, Charnov, Fretwell-Lucas, Goodwin, Richardson and others) | not determined; publisher copyright presumed | citation, restated standard equations, and paraphrased findings; no quotation |
