# Prior work 077: fitted models of observational threat learning, and the in-group gain

Direction: D460

Date: 2026-10-29. Kind: deep-read. Cluster: social transmission of fear as an operator (follows file 22, section on observational fear).

**Question.** File 22 treats `observe(b, a's reaction to cue x)` as the one place where "transmission is not a metaphor", with a gain depending on whether a is in-group for b, and says "parameter values not yet extracted". Do Lindström, Haaker & Olsson 2018; Lindström et al. 2019; Olsson, Knapska & Lindström 2020; and Golkar, Castro & Olsson 2015 give a fitted model with a learning-rate gain, and is the in-group gain a fitted parameter?

**Blunt answer up front.** No. Of the four seeds, I could read only one at source with its equations (Lindström et al. 2019, main text). Two others were abstract-only (paywalled, no open copy: unpaywall `is_oa: false` for both NeuroImage 2018 and Nat Rev Neurosci 2020), and Golkar 2015's full text was blocked (PMC returned a reCAPTCHA page, Europe PMC full-text returned HTTP 500, the publisher returned 403). **The in-group effect is reported in the abstract as "more potent", with no gain parameter in anything I could see.** The supplementary appendix of the PNAS paper, where the model equations and fitted parameters live, was blocked (HTTP 403 from pnas.org; Europe PMC supplementary endpoint returned nothing). So no fitted learning rate, softmax temperature or in-group multiplier is transcribed here. Where I state a form, I say how I know it.

**Method note.** Web search budget was exhausted before I started, so every source was found by direct fetch (Crossref, Europe PMC REST, OSF API, PMC XML). Tags: [read] = read at source in this session; [abstract] = abstract read only; [standard] = standard account from background knowledge, not checked.

---

## 1. Lindström, Golkar, Jangard, Tobler & Olsson (2019), PNAS

**Citation.** Lindström B, Golkar A, Jangard S, Tobler PN, Olsson A (2019). Social threat learning transfers to decision making in humans. *PNAS* 116(10): 4732-4737. DOI 10.1073/pnas.1810180116 (confirmed via Europe PMC record, PMC6410767, open access CC BY-NC-ND). Data: OSF project xfe72, one file `social_threat_learning_transfers_2019.csv` (461 kB), found via the OSF API; not downloaded or analysed here.

**Design [read].** Three experiments, n = 40 each (120 analysed; 121 recruited, one excluded for technical failure). Block 1 is conditioning: Exp 1 direct Pavlovian shock conditioning; Exp 2 observational (video of a demonstrator receiving shocks after CS+); Exp 3 instructed (told CS+ predicts shock, never shown the cues). Block 2 is a 70-trial two-choice instrumental task with probabilistic shocks, 35-trial Transfer phase, then the outcome contingencies reverse (Reversal phase). Half the participants are "No Change" (CS+ remains the more shocked cue), half "Change" (CS+ becomes the less shocked cue). Control experiments: 25 with no conditioning block, 80 in controls 3B-C. Participants: 69 female, mean age 26 y; ethics approval at Karolinska Institutet.

**Model [read, in words; equations are in the SI, not read].** A "competing systems" model: a Pavlovian controller learns cue values V during conditioning, an instrumental controller learns action values Q during decision making, both "implemented as simple, independent reinforcement learning algorithms". At choice the two compete, with "a weight (omega, 0 <= omega <= 1)": positive omega means the Pavlovian value of a cue biases the probability of choosing it. Pavlovian values "are updated together", so the Pavlovian influence is roughly constant through decision making. The generic form in this literature (Dayan, Niv, Seymour & Daw 2006; Huys 2011, both cited in the paper) is a weighted mixture of V and Q inside a softmax [standard]. I did not see the paper's exact expression, so treat any specific equation as unconfirmed.

**Fitted values [read].**
- Pavlovian weight omega: Exp 1 M = 0.49; Exp 2 (observational) M = 0.5; difference reported as "t (76.13), P = 0.96" (degrees of freedom only, the t value is not printed); neither differs from 0.5 (smallest P = 0.49).
- Transfer effect, Change vs No Change, probability of the optimal choice (logistic GLMM): Exp 1 beta = -1.28 (SE 0.34, z = -3.81, P = 0.0001, 95% CI -1.94 to -0.62); Exp 2 beta = -1.73 (SE 0.32, z = -5.38, P < 0.0001, 95% CI -2.36 to -1.1); Exp 3 (instructed) beta = -1.56 (SE 0.32, z = -4.85, P < 0.0001, 95% CI -2.19 to -0.93). The paper calls these random-effects logistic regressions (GLMMs with by-subject random intercepts and slopes).
- Reversal: Exp 1 Group x Reversal chi2(1) = 6.86, P = 0.009; Exp 2 chi2(1) = 18.54, P < 0.0001; Exp 3 chi2(1) = 19.6, P < 0.0001.
- No reliable difference in transfer between Exp 1 and Exp 2: Group x Experiment chi2(1) = 1.39, P = 0.24.
- Exp 2: Change group received 20.4% more shocks than No Change (Wilcoxon W = 295.5, P = 0.009).
- Exp 1 manipulation check: SCR CS+ > CS-, t(38) = 2.33, P = 0.025. Exp 2: t(38) = 2.36, P = 0.02.
- Individual differences in empathy with the demonstrator and subjective unpleasantness of watching "slightly moderated" transfer strength (details in SI, not read).

**Model comparison [read].** Compared by AIC weights (wAIC); the dotted line is wAIC = 0.95. Observational learning (Exp 2) was best explained by the competing-systems model against alternatives (outcome bonus, confirmation bias, instructed-learning-D, prior model) from the advice-taking literature (Biele et al. 2009, 2011; Li et al. 2011; Doll et al. 2009). Instructed learning (Exp 3) was best explained by a prior model, in which instruction sets initial instrumental action values via a free parameter. The paper states Bayesian random-effects comparison converges (SI). The main text says the two social routes "rest on distinct computational mechanisms".

**What the paper does not contain.** There is no demonstrator-identity term, no in-group parameter, no observational learning rate separate from the direct one that I could see, no softmax temperature in the main text. The demonstrator is the same person-type for everyone. The model's social input, in the wording of Lindström et al. 2019 (PNAS 116(10), main text), is simply "the cue was followed by a shock for the demonstrator".

**Empirical standing, bluntly.** Three experiments of 40, one lab, one population (a Stockholm sample, mean age 26; the main text does not say students). The key "same controller" claim for observational vs Pavlovian rests on a null (omega not different from 0.5 and no Group x Experiment interaction), which with n = 40 per arm cannot establish equivalence (no equivalence test is reported in the main text). The instructed-learning result contradicted the authors' own prediction (they predicted it would not transfer; it did), and the model explaining it was found post hoc by comparing to published alternatives. No external replication found. Open data exist, so refit is possible.

## 2. Lindström, Haaker & Olsson (2018), NeuroImage

**Citation.** Lindström B, Haaker J, Olsson A (2018). A common neural network differentially mediates direct and social fear learning. *NeuroImage* 167: 121-129. DOI 10.1016/j.neuroimage.2017.11.039 (confirmed; Crossref and Europe PMC, PMID 29170069). Closed access.

**Content [abstract].** Direct (Pavlovian) and social fear learning produced indistinguishable behaviour and engaged the same self/other aversive learning network: amygdala, anterior insula (AI), anterior cingulate cortex (ACC). Information flow differed: dynamic causal modelling combined with reinforcement-learning modelling indicated amygdala input during direct learning and AI input during social learning; in both, AI gated surprise-based (associability) learning signals sent to the ACC. This is a Pearce-Hall style associability, [standard]: the usual hybrid is V(t+1) = V(t) + kappa * alpha(t) * (lambda - V(t)), alpha(t+1) = eta * |lambda - V(t)| + (1-eta) * alpha(t). The paper's actual equation, parameter values and sample size were not read.

**Empirical standing.** Neuroimaging with DCM. Fitted learning parameters, if any, are not in the abstract. Note that this file contradicts the premise in the direction text of "fitted models with the in-group gain": the paper contains no group manipulation per its abstract, so it cannot supply an in-group gain either.

## 3. Olsson, Knapska & Lindström (2020), Nature Reviews Neuroscience

**Citation.** Olsson A, Knapska E, Lindström B (2020). The neural and computational systems of social learning. *Nat Rev Neurosci* 21(4): 197-212. DOI 10.1038/s41583-020-0276-4 (confirmed via Crossref; author list and pages now confirmed, closing the "author list from memory" caveat in file 22).

**Content [abstract].** Review across species, aversive and appetitive domains. Claim: social learning "generally follows the same principles as self-experienced value-based learning, including computations of prediction errors", implemented in circuits active across tasks plus regions processing social information. Spans basic threat avoidance to social learning strategies and cultural phenomena. Full text closed; I did not see any equation, parameter table or statement on group-dependent gain. A review in any case does not produce fitted values.

## 4. Golkar, Castro & Olsson (2015), Biology Letters

**Citation.** Golkar A, Castro V, Olsson A (2015). Social learning of fear and safety is determined by the demonstrator's racial group. *Biol Lett* 11(1): 20140817. DOI 10.1098/rsbl.2014.0817 (confirmed via Crossref; PMID 25631229; PMC4321149).

**Result [abstract].** Two observational-learning experiments; "both fear and safety learning from a racial in-group demonstrator was more potent than learning from a racial out-group demonstrator." Sample sizes, effect sizes and p-values were not retrievable (full text not open: PMC record exists but is flagged not open access; NCBI efetch returns front matter only). Response measure: the abstract does not name it, but Golkar & Olsson 2017 [read] describe their SCR-based observational paradigm as the "established" one and cite Golkar 2015 for it, so SCR is likely; not confirmed from the 2015 text.

**What this gives the algebra.** A sign and a qualitative ordering: gain(in-group) > gain(out-group) for both fear acquisition and safety acquisition. Nothing more.

## 5. Neighbouring in-group and fitted-model works found while fetching

Crossref surfaced these. All titles, authors and DOIs confirmed against Crossref in validation; only the Sci Rep 2017 paper was read.
- Golkar A, Olsson A (2017). "The interplay of social group biases in social threat learning." *Sci Rep* 7: 7685, DOI 10.1038/s41598-017-07522-z (PMC5550414, open) [read]. n = 95 White Swedish observers, racial in/out-group demonstrator crossed with supporter-team in/out-group, outcome conditioned SCR at a direct test. Supporter group mattered only with a racial in-group demonstrator: Stimulus x Supporter group F(1,45) = 9.50, p = 0.004, eta_p^2 = 0.17; in-group vs rival-team difference t(45) = 3.08, p = 0.004, Cohen's d = 0.90. ANOVA on SCR only; no computational model, no learning rate. So a second, non-racial group label also orders the gain, but the two labels interact rather than combining additively.
- Golkar A, Björnstjerna M, Olsson A (2015). "Learned fear to social out-group members are determined by ethnicity and prior exposure." *Front Psychol* 6, DOI 10.3389/fpsyg.2015.00123; unread. Concerns direct conditioning to out-group faces, not observational gain, per title.
- Haaker J, Yi J, Petrovic P, Olsson A (2017). "Endogenous opioids regulate social threat learning in humans." *Nat Commun* 8: 15495, DOI 10.1038/ncomms15495. Authors confirmed via Crossref; unread. Relevant because opioid blockade scales observational learning: a candidate causal knob on the social gain.
- Haaker J, Molapour T, Olsson A (2016). "Conditioned social dominance threat: observation of others' social dominance biases threat learning." *SCAN* 11(10): 1627-1637, DOI 10.1093/scan/nsw074; unread. Another demonstrator-identity effect.
- Pärnamets P, Espinosa L, Olsson A (2018, bioRxiv). "Physiological synchrony predicts observational threat learning in humans", DOI 10.1101/454819. Preprint; candidate for a measured coupling between observer and demonstrator arousal.

## 6. The only fully read equations: observational update in an open model

Because the above lack equations, I read an open paper from the same lab that states how observational learning is specified: Lindström B, Selbing I, Olsson A (2016), "Co-evolution of social learning and evolutionary preparedness in dangerous environments", *PLoS ONE* 11(8): e0160245, DOI 10.1371/journal.pone.0160245 (PMC4972391, CC BY) [read: methods section 2.3 to 2.5].

- Eq 3 [read]: Q_i(t+1) = Q_i(t) + alpha * delta_i(t), with 0 < alpha < 1, **alpha = 0.3** in all simulations.
- Eq 4 [read]: delta(t) = R_i(t) - Q_i(t).
- Observational conditioning [read]: "identical to individual learning (Eqs 3 and 4): without error, the individual updated Q_i by the reward of the observed individual choosing option i, with the same learning rate, alpha". So the observation gain is exactly 1 relative to own experience. A fatal outcome observed sets R = -1000.
- Eq 5 [read]: softmax Pr_i = exp(Q_i + P_i) / sum_j exp(Q_j + P_j), j = 1..10; P_i is genetic preparedness added to the learned value, i.e. an "evolutionary prior". No temperature term appears, so it is effectively fixed at 1 (my inference from the equation; the paper does not say so).
- Parental transmission [read]: the parent's Q vector is copied to the offspring at reproduction.
- Observed demonstrator is "a randomly selected individual in the population"; no identity weighting.

This is a simulation with assumed parameters, not fits to human data. The authors state it is a "best case scenario" for social learning (error-free, costless). It is useful here only as the explicit statement that in this lab's modelling tradition, the default is gain = 1 on observed outcomes.

## 7. Operand/operator translation

Operands: agent state (cue-value vector Q_a over cues/actions, an associability alpha_a, a Pavlovian weight omega_a); observed other (with a group label g(a')).

Operator: `observe(b, a, x, outcome)` updates Q_b(x) by gain * alpha * (R - Q_b(x)). In the open model the gain is 1; in the human data the only established constraint is an ordering, gain(in-group of b) > gain(out-group of b). The cleaner way to put the Golkar finding into an algebra is as a multiplicative modifier w(g_b, g_a) in [0, 1] on the learning rate: alpha_social = w * alpha. This is a modelling choice by me; no source fitted w.

Composition: Lindström 2019 gives a mixing law for the two controllers (weight omega, about 0.5 in both direct and observational arms), and a separate path for instruction (prior on Q). So three transmission operators have different algebraic type: direct and observational both are updates of V (Pavlovian) coupled to Q by omega; instruction is an assignment to Q(t=0), not an update. Different types, therefore not the same operator with different gains.

## 8. What exists vs what does not

**Exists.** (a) A sign for the in-group effect on both fear and safety acquisition (Golkar 2015, abstract). (b) A fitted-in-the-sense-of-estimated Pavlovian weight omega ~ 0.5 for direct and observational conditioning combined with instrumental choice (Lindström 2019, [read]), with n = 40 per experiment. (c) A model-comparison result that observational and instructed routes are different mechanisms (Lindström 2019). (d) A neural route result for the input source of direct vs social learning (Lindström 2018, abstract). (e) A reproducible default of gain = 1 in the lab's own simulations (2016). (f) Open data (OSF xfe72) from which learning rates could be refitted.

**Does not exist (as far as I could verify).** (1) A fitted in-group gain parameter, with confidence interval, in any seed work. (2) A fitted observational learning rate separate from the direct one. (3) Any replication of the 2019 competing-systems result by another lab. (4) Any demonstration that the in-group effect acts on learning rate rather than on attention to the demonstrator, expression, or arousal at test: the abstract-level result cannot tell these apart, and they are different operator types. (5) Parameters for dyads, groups of three, or non-racial groups in a fitted model (Golkar 2015's group is racial only; Golkar & Olsson 2017 add supporter-team membership but fit no model, only SCR ANOVAs).

## 9. Unconfirmed

- Exact equations of the competing-systems model, softmax temperature and learning rate values in Lindström 2019: in the SI (pnas.org returned 403). Next step: obtain the SI by another route, or refit from the OSF CSV.
- Whether Lindström, Haaker & Olsson 2018 reports learning-rate or associability parameter values, the sample size, and whether it contains any group manipulation (I believe not, from the abstract).
- All numbers in Golkar 2015: n, measure, effect sizes, p-values.
- Whether Olsson, Knapska & Lindström 2020 states any group-dependent gain in the review text.
- The Front Psychol 2015 paper (Golkar, Björnstjerna & Olsson): design and numbers (unread).
- Whether the in-group effect survives replication (no replication seen).
- The Haaker 2017 opioid paper's effect size (authors now confirmed; text unread).
- "Does not exist" items (1)-(4) in section 8 were not tested by a literature search in validation: the web-search budget was exhausted, so they remain "not found by this file's author", not "shown absent".

## Validation log (2026-10-29)

All ten DOIs resolved at api.crossref.org; titles, authors, venues matched. Web search unavailable (budget exhausted), so no "nothing exists" claim could be tested.

- ✎ Lindström, Golkar, Jangard, Tobler & Olsson 2019, PNAS 116(10):4732-4737 — main text re-read via Europe PMC XML [read]; every number in section 1 matches (omega 0.49/0.5, betas, chi2s, W = 295.5, SCR ts, 121/1 excluded, 25 + 80 controls, OSF xfe72). Fixed: "Karolinska students" (text says only ethics at KI, mean age 26), "unsignalled" reversal (not in text), noted t(76.13) is df only; added CIs.
- ✓ Lindström, Haaker & Olsson 2018, NeuroImage 167:121-129 — abstract checked; summary accurate; closed access.
- ✎ Olsson, Knapska & Lindström 2020, Nat Rev Neurosci 21(4):197-212 — abstract checked; added issue number.
- ✎ Golkar, Castro & Olsson 2015, Biol Lett 11(1):20140817 — abstract quote exact; full text still not open; SCR measure now supported indirectly via Golkar & Olsson 2017.
- ✎ Golkar & Olsson 2017, Sci Rep 7:7685 — authors added; read; design and statistics added; no model.
- ✎ Golkar, Björnstjerna & Olsson 2015, Front Psychol 6 — authors added; unread.
- ✎ Haaker, Yi, Petrovic & Olsson 2017, Nat Commun 8:15495 — authors confirmed (were "partly from memory").
- ✎ Haaker, Molapour & Olsson 2016, SCAN 11(10):1627-1637 — authors and pages added.
- ✎ Pärnamets, Espinosa & Olsson 2018, bioRxiv 10.1101/454819 — authors added.
- ✓ Lindström, Selbing & Olsson 2016, PLoS ONE 11(8):e0160245 — methods re-read [read]; Eqs 3-5, alpha = 0.3, R = -1000, "identical to individual learning... same learning rate", random demonstrator, "best case scenario", parental Q transfer all confirmed. The "temperature fixed at 1" reading is an inference from Eq 5 having no temperature term, not a sentence in the paper.
- Dayan, Niv, Seymour & Daw 2006 and Huys 2011 — confirmed as refs 20 and 36 of the PNAS paper; not themselves checked.

**Verdict.** The file is accurate and appropriately cautious: no number, quotation or attribution was wrong, and no fabrications were found. The corrections were small (an unsupported "students" and "unsignalled", missing authors and issue numbers), and the main addition is that the Sci Rep 2017 paper, open and now read, extends the in-group ordering to a non-racial label but, like Golkar 2015, fits no learning-rate model, so the central answer (no fitted in-group gain in the seeds) stands.

## Cross-checks (2026-10-29)

Method: grepped every other file in this directory for Lindström, Golkar, Olsson, Haaker, Pärnamets, Pavlovian, associability, Pearce-Hall, Dayan and opioid. Overlaps are with files 22, 064, 17 and 34 only; no other file touches these works. No numeric overlap exists: 077 is the only file with the omega, beta and chi-square values from Lindström 2019, so none of them could be cross-checked. No primary source was re-fetched, because no claim in another file conflicts with a claim here on the facts.

### Agreements
- **File 22 (neuroscience-social-drives), D1 reference list and "Quantitative structure" bullet.** Citations of Lindström, Haaker & Olsson 2018 (NeuroImage 167:121-129), Lindström et al. 2019 (PNAS 116:4732-4737) and Golkar, Castro & Olsson 2015 (Biol Lett 11:20140817) match, DOIs included.
- **File 22, "Quantitative structure" bullet, on Lindström 2018.** Direct and social fear learning are behaviourally indistinguishable, share the amygdala/AI/ACC network, differ in input (amygdala for direct, AI for social), and AI gates surprise (associability) learning. 077 section 2 says the same. Both are abstract-level only.
- **File 22, same bullet, on Lindström 2019.** n = 120, three experiments, observational and instructed learning both transfer to instrumental choice, and the modelling shows different mechanisms. 077 section 1 agrees (n = 40 x 3; 121 recruited, 1 excluded; observational by competing systems, instructed by a prior model).
- **File 22, "Parameter values were not retrieved" and "values not yet extracted".** 077 confirms the gap: no fitted learning rate, temperature or in-group gain is available from the seed papers.
- **File 22, Olsson, Knapska & Lindström 2020 entry.** 077 section 3 closes the "author list from memory" caveat (Crossref confirmed, 21(4):197-212).
- **File 22, "in-group, per Golkar et al. 2015".** The sign of the effect agrees with 077 section 4 (in-group more potent for fear and safety learning). 077 adds that Golkar & Olsson 2017 find a second label (supporter team) that interacts with the racial label.
- **File 22, "Replication standing".** Both say replication is thin; 077 section 8 item 3 says none was found for the 2019 competing-systems result.
- **File 064 section 8 (Olsson & Phelps 2004).** Similar SCR fear learning across Pavlovian, observational and instructed routes. This is consistent with 077's Lindström 2019 result of no Group x Experiment difference in transfer between direct and observational (chi2(1) = 1.39, P = 0.24), and with omega about 0.5 in both arms. They are different papers (2004 Psych Sci; 2019 PNAS) and neither file conflates them.
- **File 17 line 143.** The same three-pathway framing as 077 section 7, where instruction is an assignment to initial Q and not an update.
- **File 34 (Huys et al. 2012, Pavlovian bias in a parameter vector).** Consistent with 077's use of a Pavlovian weight omega as a per-agent parameter. These are different Huys papers (2012 PLoS Comput Biol; 077 cites Huys 2011), so the overlap is thematic, not a shared source.

### Contradictions
- **File 22, "Exists" item (b), line 247, versus 077 title, sections 8 and 9.**
  - File 22 says there are "fitted learning models" for fear transmission "and an in-group gain on it (Golkar et al. 2015)", which reads as if a fitted in-group gain exists.
  - 077 says no in-group gain parameter appears in any seed paper (Golkar 2015 is an abstract-level ordering only; the fitted omega in Lindström 2019 carries no group term).
  - Verdict: 077 is right. File 22's own line 180 says parameter values were not retrieved, and Golkar 2015 as read is a two-experiment ordering. File 22's line 247 and line 183 overstate. This is a difference of strength, not an incompatible fact, and it is the correction 077 was written to make. Not edited here, per instruction.
- No other contradictions found. Nothing is "unresolved".

### Not checkable against other files
Lindström 2019 omega 0.49/0.5, the GLMM betas, the reversal chi-squares and W = 295.5; Lindström, Selbing & Olsson 2016 Eqs 3-5 (alpha = 0.3, R = -1000); Golkar & Olsson 2017 statistics; the neighbouring works in section 5 (Haaker 2016 and 2017, Pärnamets 2018, Golkar, Björnstjerna & Olsson 2015). None occur in any other file. The Haaker 2017 in file 22 is the Nature Protocols paper (Haaker, Golkar, Selbing, Olsson), not the Nat Commun opioid paper in 077; they are two distinct works.

## Licences of quoted and transcribed material (2026-10-30)

Each source quoted, restated or taken from a dataset in this file. All quotations are under 60 words and attributed; no table or list is transcribed.

- **Lindström, Golkar, Jangard, Tobler & Olsson 2019, PNAS 116(10):4732-4737** (PMC6410767): CC BY-NC-ND (open access, as recorded in section 1). Used as short quotations from the main text (model description, "competing systems", omega weight, the demonstrator-input sentence), and reported statistics (omega, betas, chi-squares) as numbers with a prose description. No table copied.
- **Lindström, Selbing & Olsson 2016, PLoS ONE 11(8):e0160245** (PMC4972391): CC BY. Used as restated equations (Eqs 3-5, alpha = 0.3) and short quotations from the methods.
- **Golkar & Olsson 2017, Sci Rep 7:7685** (PMC5550414): open access; licence not individually checked here (Scientific Reports articles are normally CC BY 4.0). Used as reported statistics and description only.
- **Golkar, Castro & Olsson 2015, Biol Lett 11(1):20140817**: not determined; publisher copyright presumed (PMC record flagged not open access). Used as a short quotation from the abstract (20 words, also a 2-word fragment in the blunt answer), under the 60-word limit.
- **Olsson, Knapska & Lindström 2020, Nat Rev Neurosci 21(4):197-212**: not determined; publisher copyright presumed (full text closed). Used as a short quotation from the abstract (14 words) and a paraphrase.
- **Lindström, Haaker & Olsson 2018, NeuroImage 167:121-129**: not determined; publisher copyright presumed (closed access). Used as a paraphrase of the abstract; the Pearce-Hall form is restated from background knowledge.
- **Dayan et al. 2006; Huys 2011; Biele et al. 2009, 2011; Li et al. 2011; Doll et al. 2009**: cited only (citations are free); not read here.
- **Dataset: OSF project xfe72, `social_threat_learning_transfers_2019.csv`** (Lindström et al. 2019 data): licence not determined; not downloaded and nothing copied. Record the OSF file's licence before any refit is committed.
- **Haaker et al. 2016/2017, Pärnamets et al. 2018, Golkar, Björnstjerna & Olsson 2015**: cited only; unread; licences not determined; no text used.

Access note (verdict check, text unchanged): sections 0 and 9 record that the Golkar 2015 full text and the PNAS supplement were blocked (reCAPTCHA, HTTP 403/500) and that other routes (Europe PMC REST, PMC XML, Unpaywall) were used. Aldred should confirm those were public open-access routes and not workarounds for closed copies; if any was a workaround, downgrade the dependent [read] tags to [from abstract/standard account] with "readable copy not obtained legitimately; re-read needed".
