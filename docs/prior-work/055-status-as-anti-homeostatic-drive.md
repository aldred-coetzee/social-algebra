# Prior work 055: status as a fundamental, possibly anti-homeostatic drive

Direction: D153

Date: 2026-10-29. Kind: deep-read. Question: is status a fundamental drive, is it positive feedback, and what bounds it? Seeds: Anderson, Hildreth & Howland 2015; Zink et al. 2008; Henrich & Gil-White 2001; Magee & Galinsky 2008. Cross-refs: 22 (anti-homeostatic direction), 42 section 1 (status dynamics), 20, 21, 23.

**Method and honesty note (read this first).** Only one of the four seeds was read at source: Zink et al. 2008 (author manuscript, PMC2430590, via a summarising fetch, so statistics are the fetch's transcription of the text and tables). Henrich & Gil-White 2001 and Magee & Galinsky 2008 are paywalled; the only full-text copies reachable were course-page or mirror PDFs. A download of one such copy of Anderson et al. was refused by the permission classifier as unauthorised copying, and I did not work around it; the two mirror PDFs that the fetch tool had already saved locally were not opened either. So Anderson 2015, Henrich & Gil-White 2001 and Magee & Galinsky 2008 are tagged `[from abstract/standard account]` or `[secondary]`. Two further sources were read: the Big Man Mechanism paper (open access, PMC4633849; its equations are images, so reconstructed from the prose) and the Boyce et al. 2010 abstract-level record. DOIs were checked at Crossref where stated. **No equation in this file is quoted from a primary source except where tagged [read], and none is [read] that is not a model parameter list.** The seeds contain almost no equations at all; that is itself the main finding.

**Summary.**
1. Status is well supported as a *motive* (Anderson et al.: wellbeing, health, behaviour, universality) and as a neural *reward* (Zink: rank outcomes drive ventral striatum at a magnitude comparable to money). Neither source gives a state variable with a dynamics law.
2. "Positive feedback" is asserted verbally by Magee & Galinsky (self-reinforcing power and status) and appears in a formal sense only for animals (Bonabeau, file 42). In humans no study measures the gain of the loop.
3. "Anti-homeostatic" is not shown by any of the four seeds. The strongest nearby evidence is that status is *relative and ordinal* (rank, not level), so a population-wide gain cannot be satiated. That is a different property from a runaway drive, and it is a bound-by-structure, not a set point.
4. What bounds it is the weakest-covered part of the literature: candidate bounds exist (fixed total of rank positions, legitimacy, conflict, prestige being freely conferred and so withdrawable, cost of dominance), but none is quantified for humans.

---

## 1. Anderson, Hildreth & Howland 2015: status as a fundamental motive

**Citation.** Anderson, C., Hildreth, J. A. D., & Howland, L. (2015). Is the desire for status a fundamental human motive? A review of the empirical literature. *Psychological Bulletin*, 141(3), 574-601. DOI 10.1037/a0038781 (Crossref confirmed; PMID 25774679 per PubMed record).

- **Their vocabulary.** Status = "the respect, admiration, and voluntary deference individuals are afforded by others" [abstract, via PubMed summary]. Distinguished from power (control over resources) and from wealth. "Status hypothesis": the desire for status is a fundamental motive.
- **Drives/operands.** One motive, status desire. State variable: status as granted by others (an others-held quantity, relative, not an internal deficit).
- **Operators/equations.** None [secondary: press summary and abstract]. A criteria checklist: (1) wellbeing and health depend on status, (2) people take goal-directed action to gain and keep it, (3) it is not reducible to other motives (they conclude it is not merely the need to belong), (4) universality across culture, gender, age, personality. Press summary (PsyPost) calls the first the strongest evidence; low status linked to depression, anxiety, cardiovascular disease.
- **Theorems or derived predictions.** Directional only: loss of respect harms wellbeing independently of material loss; people manage their status.
- **Empirical standing.** A review, as strong as its sources. Health links are largely correlational, and the press summary does not say otherwise. The review is the field's best statement of the *existence* of the drive, but a verdict on a *fundamental* drive depends on the criteria the authors chose. **Whether the drive is satiable, adapts to level, or has a set point is not addressed in the abstract and not stated in the secondary summary.** Not verified against the full text.
- **Translation.** Operand `status_i` (others-granted, ordinal). A separate felt-need scalar `s_i` is a modelling choice the review neither supplies nor excludes. It supports status as a first-class operand; it supplies no law.

## 2. Zink et al. 2008: neural processing of rank

**Citation.** Zink, C. F., Tong, Y., Chen, Q., Bassett, D. S., Stein, J. L., & Meyer-Lindenberg, A. (2008). Know your place: neural processing of social hierarchy in humans. *Neuron*, 58(2), 273-283. DOI 10.1016/j.neuron.2008.01.025 (Crossref confirmed; PMC2430590). Authors from my recollection of the paper; the Crossref title and volume were confirmed, the author list was not re-checked.

- **Their vocabulary.** Ranks shown as stars (three star superior, two star participant, one star inferior); "stable" and "unstable" hierarchy; "hierarchical value" of an outcome (whether it could change the participant's rank).
- **Design [read].** Exp 1 (stable): 24 participants (12 male), reaction-time task for money, 108 rounds, photo of a superior or inferior simulated player, ranks fixed, participants "never lost money", earned $1 for fast responses. Exp 2 (unstable): 24 new participants, visual discrimination, 168 rounds, ranks updated every four rounds from the preceding eight rounds' accuracy. Exp 3: 24 participants, non-social control with computers. Players simulated; nine more participants excluded for technical issues or doubt about the players.
- **Results [read].** Superior vs inferior player: occipital/parietal (right inferior parietal Z = 6.76), ventral striatum (Z = 3.99), parahippocampal, left DLPFC (Z = 4.48), P < 0.005 FDR. No region responded more to the inferior player. Unstable: pattern replicated (right DLPFC Z = 5.46) plus thalamus (5.34), right amygdala (4.34), posterior cingulate (4.25), medial PFC (3.78); thalamus, amygdala, posterior cingulate activity correlated with reported positive affect when top-ranked (r = 0.51, 0.48, 0.48). Losing to a lower-ranked player (negative hierarchical value): occipital/parietal, ventral striatum, midbrain/thalamus, anterior insula. Beating a higher-ranked player: pre-SMA (Z = 5.14), medial PFC, premotor; premotor correlated negatively with trait dominance (r = -0.45, P = 0.04). Outcomes without hierarchical value: no activations.
- **Reward comparison [read, quoted by the fetch].** "social hierarchical consequences of performance were neurally dissociable and of comparable salience to monetary reward"; in a GLM, hierarchical value contributed to ventral striatal activity "of comparable magnitude to that of the primary monetary reward itself". The authors speak of "a neural basis for the high motivational value of status" and speculate (interpretively) that acquiring a superior position may bias toward an active state.
- **Operators/equations.** None. No behavioural dynamics were estimated: rank was imposed, not evolved by the participant's own state.
- **Theorems or derived predictions.** Status outcomes are processed as rewards and losses on a scale comparable to money; the response to a superior is stronger when the hierarchy is unstable (extra amygdala, thalamus, mPFC), i.e. instability raises the arousal attached to rank.
- **Empirical standing, blunt.** Three samples of 24, simulated opponents, all Caucasian right-handed 19-43, rank from *incidental skill* and not power, wealth or occupation; the two social experiments used different tasks, scanners and TRs; some clusters at uncorrected P < 0.001; correlations on n = 24. A later review notes (secondary, search summary) that visual-cortex activations may track star count rather than hierarchy. No replication was located in this survey (not searched). It shows rank is reward-like in the lab, not that status is a runaway drive. Also: the response was to the *sight* of a superior, with no evidence on whether the reward saturates with repeated exposure to the same rank.
- **Translation.** Supports a utility term `u(rank change)` of order comparable to a monetary reward; a gain-loss asymmetry could not be read from the summary and is **not** claimed. Gives the sign of a rank-prediction-error operand, no gain. The instability finding suggests rank uncertainty (`var(rank)`) as a separate operand from rank.

## 3. Henrich & Gil-White 2001: prestige as freely conferred deference

**Citation.** Henrich, J., & Gil-White, F. J. (2001). The evolution of prestige: freely conferred deference as a mechanism for enhancing the benefits of cultural transmission. *Evolution and Human Behavior*, 22(3), 165-196. DOI 10.1016/S1090-5138(00)00071-4 (Crossref confirmed). Full text not read; 32-page PDF located at a mirror but not opened.

- **Their vocabulary [abstract].** "Information goods" theory; prestige = freely conferred deference, versus dominance = force or the threat of force; prestige processes as an emergent product of psychological adaptations that evolved to improve the quality of information gained through cultural transmission.
- **Drives/operands.** Two distinct status currencies. On this account the prestige-seeking side is a *learner's* drive (to get access to a skilled model), and the prestigious individual's reward is the deference, paid as goods, services and attention.
- **Operators/equations.** None found in the abstract or in secondary accounts [from abstract]. I do not know whether the paper contains a formal model; I believe it is verbal with cross-cultural evidence (standard account, unchecked).
- **Derived predictions [abstract].** Predictions are tested against data "from across the social sciences". The contrast with dominance predicts prestige is *conferred* and therefore **revocable** by the follower, which is the only bound on prestige that the theory states by construction: a prestige hierarchy is held up by continued choice of followers, a dominance hierarchy by cost imposed on them. This is my inference from the definition, not a quoted claim.
- **Empirical standing.** Followed by experiments on prestige-biased learning (Chudek, Heller, Birch & Henrich 2012: 3- and 4-year-olds more than twice as likely to learn from a model that bystanders had attended to for 10 seconds, stronger for artifact use than food preferences [secondary search summary]); a later critique reports mixed findings for direct tests of prestige bias [secondary]. Cheng et al. 2013 (DOI 10.1037/a0030398, Crossref confirmed) found in group tasks both dominant and prestigious individuals attained influence, the dominant ones less liked [from abstract; see file 42].
- **Translation.** Two operands `dom_i`, `prest_i`, with different update rules: `prest_i` is a function of other agents' *choices* (so an aggregate of followers' selections, naturally bounded by the followers' attention), `dom_i` a function of costs imposed. This is the cleanest structural statement of what bounds status in the seeds, but the bound is qualitative.

### 3a. Henrich, Chudek & Boyd 2015: a formal prestige model (added; read at PMC)

**Citation.** Henrich, J., Chudek, M., & Boyd, R. (2015). The Big Man Mechanism: how prestige fosters cooperation and creates prosocial leaders. *Phil. Trans. R. Soc. B*, 370(1683). DOI 10.1098/rstb.2015.0013 (Crossref confirmed). Read from PMC4633849 via a summarising fetch; **the equations (3.1-3.7) are images and were not seen**, so conditions below are the fetch's verbal restatement. The last 22k characters of the page text were not read, and the discussion was not seen.

- **Variables [read, prose].** x in {0,1} cooperation; q frequency; n group size; c leader cost; b total benefit split b/n; C = c - b/n net cost; p probability a follower copies the leader (the "prestige effect"); s probability learned traits stick across generations; R phenotypic assortment (leader-follower part plus a p^2 follower-follower part); alpha bleed-over of a cooperation gene.
- **Results [read, prose].** Cooperation spreads when R exceeds a threshold set by C relative to benefit; "will not evolve culturally unless p > 0"; for large n, R reduces to p^2 (p = 0.5 gives R of about 0.25; p a bit above 0.7 gives about 0.5); for p below about 0.20 cooperation is viable only in groups of about five or fewer; with s = 0 never in large groups; for large n, R = s p^2; "Natural selection does not favour reducing the prestige effect."
- **Bounds the model states.** Deference alone (no persistence) yields little cooperation; effects limited by n, s and alpha; p is an exogenous parameter not made a function of population size; the figure of about 80 people for a Big Man's sphere (citing Sahlins) is mentioned but not built in. **Competition among aspiring leaders, recruiting larger followings and punishment are listed as excluded future work.** So the one formal prestige model has no status dynamics and no competition: status is an assumed role, not an evolving quantity.
- **Translation.** `p` is a coupling coefficient (follower copies leader), a usable parameter for a prestige-transmission operator; its range is stated, its measured human value is not located here.

## 4. Magee & Galinsky 2008: the self-reinforcing hierarchy

**Citation.** Magee, J. C., & Galinsky, A. D. (2008). Social hierarchy: the self-reinforcing nature of power and status. *Academy of Management Annals*, 2(1), 351-398. DOI 10.5465/19416520802211628 (Crossref confirmed). A search summary gave the DOI as 10.1080/19416520802211628, which did **not** resolve at Crossref; use the 10.5465 form. SSRN preprint (different title: "The Self-Reinforcing Nature of Social Hierarchy: Origins and Consequences of Power and Status") abstract id 1298493. Full text not read (MIT-hosted course PDF located but not opened).

- **Their vocabulary [secondary: search summaries of the abstract].** Power = control over valued resources (and, in a later source's gloss, asymmetric control); status = respect and admiration in the eyes of others. Two bases of hierarchy. Hierarchy-enhancing belief systems. Conditions for hierarchy change.
- **Drives/operands.** No drives. Two hierarchy-position variables, power and status, each with psychological and behavioural correlates.
- **Core claim [secondary].** Power shapes how people think and act so as to keep or gain power; status creates expectations and opportunities that favour those who already have it. Later papers cite it for the point that hierarchies persist largely regardless of whether the original rise came from skill or luck [secondary].
- **Operators/equations.** None; verbal feedback model. This file was NOT able to confirm whether the paper has a figure of loops or states loop gain; the claim that it is "a positive feedback loop" is the standard reading, not a quote.
- **Bounds mentioned only second-hand [secondary, unverified against the paper].** Illegitimate hierarchies destabilise; low-power individuals under perceived illegitimacy become action- and risk-oriented; overconfidence yields higher status but groups with members overestimating their power have more conflict (these come from reference-laden excerpts in later work, not necessarily the paper's words).
- **Empirical standing, blunt.** The paper is a review, and its mechanisms (e.g. power priming approach orientation) rest on literature subject to the social-priming replication problems; I did not check which components replicated. Smith & Magee and others (e.g. "power without status drives interpersonal conflict") appear in search results; not read.
- **Translation.** The sign of status-on-status coupling is positive: `d status_i / dt` increases with `status_i` through others' deference and the holder's behaviour. The magnitude is unknown.

## 5. Other evidence on boundedness (limited)

- **Boyce, Brown & Moore 2010.** Money and happiness: rank of income, not income, affects life satisfaction. *Psychological Science*, 21(4), 471-475. DOI 10.1177/0956797610362671 (Crossref confirmed). Search-summary of abstract: income *rank* predicted life satisfaction, absolute income and reference-group income did not; upward comparisons weigh more than downward; British Household Panel Survey, seven years, 86,679 observations per a supplementary note [secondary]. Relevance: wellbeing tracks ordinal rank, so raising everyone leaves the average unmoved. This is the clearest quantity-conservation-like property available (rank is a permutation), and it is **a structural bound on the aggregate, not an individual set point**. Standing: one dataset, one country; not replicated here.
- **Anderson et al. 2012, The Local-Ladder Effect.** *Psychological Science*, DOI 10.1177/0956797611434537 (Crossref DOI hit via title search; contents **not read**). Cited from memory for the claim that subjective wellbeing tracks standing in the *local* group; check before use. A first guess at the DOI (…434539) resolved to a different paper and was discarded.

---

## Is status a positive-feedback drive, and what bounds it? (synthesis)

| Question | What the seeds support | Standing |
|---|---|---|
| Is there a status motive? | Yes: review of wellbeing, health, behaviour, universality (Anderson) | Moderate; review, mostly correlational |
| Is status reward-like in the brain? | Yes, magnitude comparable to $1-scale money (Zink) | Weak-moderate; n = 24 x 3, simulated opponents, incidental skill |
| Is it positive feedback? | Verbally yes (Magee & Galinsky); formal only for animals (Bonabeau, 42) | Qualitative only; no human gain estimated |
| Is it anti-homeostatic (no set point)? | Not tested in any seed. Rank-based wellbeing (Boyce) implies an unsatiable aggregate, not a runaway individual | Open |
| What bounds it? | (a) rank is ordinal and conserved in aggregate (Boyce, by implication); (b) prestige is conferred and revocable (Henrich & Gil-White, by definition); (c) legitimacy and conflict (secondary, Magee & Galinsky); (d) group size and transmission (Henrich et al. 2015: n, s, p) | Qualitative, unquantified for humans |

**Algebra reading (suggested, not established).** Treat the two possibilities as distinct sorts rather than one drive. (i) A *rank* operand: ordinal, relative, with a conservation law over the group (sum of ranks fixed), so status is zero-sum at the group level whatever each individual wants. (ii) A *need* scalar attached to it, whose dynamics are an open parameter: homeostatic (set point, adaptation after rank change) or monotone. The data in hand cannot choose between them. A decisive test would be the rate of hedonic adaptation after rank change in panel data; none was found among the seeds.

## What exists vs what does not

**Exists.** A well-argued case that status is a fundamental motive (Anderson); a neural measurement that rank is a reward on the same scale as small monetary gains (Zink); a clear conceptual split into prestige (conferred) and dominance (imposed) (Henrich & Gil-White, Cheng); a verbal self-reinforcement account (Magee & Galinsky); one formal prestige-transmission model with explicit parameters p, s, n (Big Man Mechanism); ordinal-rank wellbeing evidence (Boyce).

**Does not exist (in what was read).** Any human status dynamics law with a fitted gain or adaptation rate; any test of satiation or set point for status desire; any model where the status need and rank interact (need drives action, action changes rank, rank feeds the need); any formal bound on prestige competition (Big Man paper explicitly excludes it); measured status loss kinetics. Anderson's criteria do not include "is it homeostatic".

## Unconfirmed

- Anderson et al. 2015: the full text, in particular whether it discusses satiation, adaptation, or relativity; the criteria wording is from press and abstract summaries.
- Henrich & Gil-White 2001: everything beyond the abstract: section structure, any formal model, the ethnographic regularities.
- Magee & Galinsky 2008: the exact feedback diagrams, the section on hierarchy change, and which mechanisms survived replication; the "illegitimacy" and "overconfidence" claims came from reference-laden excerpts in later work.
- Zink 2008: author list and supplement; replication status; whether the DLPFC/amygdala finding generalises beyond incidental-skill hierarchies.
- Big Man Mechanism: the equations themselves (images), the discussion section.
- Local-Ladder Effect (10.1177/0956797611434537): contents unread.
- The 10.1080 form of the Magee & Galinsky DOI: reported by a search summary, not resolvable at Crossref.
- Not searched: status adaptation / hedonic treadmill for rank, testosterone-rank feedback (Mazur & Booth, see 22), Easterlin, relative deprivation (Runciman), and the rank-dynamics models of 06/42 beyond what those files report. These are the obvious next reads for the anti-homeostatic question.
