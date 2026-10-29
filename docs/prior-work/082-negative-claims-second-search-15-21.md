# Prior work 082: independent second check of the "does not exist" claims in 15-21

Direction: D546

Date: 2026-10-29. Kind: cross-check. Brief: negative claims were the unreliable ones in the first surveys, so check them independently.

**Method and honesty note (read this first).** The session's shared WebSearch budget ran out before the first query returned (all five attempted searches were refused: "limit: 200 WebSearch calls per turn, shared by every agent"). No fresh keyword search for absence was therefore possible, which is the core of this direction. What was done instead: DOI and metadata checks in Crossref, citation graphs from Semantic Scholar (the "who cites this" route, which finds work that keyword searches miss), and one full read of a primary source (Nizamani, Memon & Galam, extracted from the arXiv PDF). Paywalled items (Sack 2021, Smith/Seger/Mackie, Battigalli/Corrao/Dufwenberg) could not be opened. **So this file confirms or corrects specific seeds; it does NOT clear the negative claims in general. D546 should be re-run with search available.** Tags: [read] = primary text read this session; [meta] = Crossref/Semantic Scholar record; [file] = what files 15-21 already say, not re-verified.

## 1. Seed-by-seed results

### 1.1 Nizamani, Memon & Galam: the outrage ODE model (file 18, section on moral panic) [read]

- **Citation, verified [meta]:** Sarwat Nizamani, Nasrullah Memon, Serge Galam, "From public outrage to the burst of public violence: An epidemic-like model", *Physica A* 416, 620-630, 2014. DOI 10.1016/j.physa.2014.09.006 (Crossref resolves to this title). Preprint arXiv:1310.0731, 2 Oct 2013.
- **Their vocabulary [read]:** sociophysics, "contagious public outrage", "hatred contagion", "hate crimes", "hate violence". The words "moral panic" (and "panic" at all) do not appear anywhere in the arXiv v1 text [read, full-text grep at validation]; the paper calls itself, in its Related Work, "the first attempt to mathematically model such issues". File 18's reading ("none is a moral-panic model by name") is correct.
- **Operands [read]:** five population proportions summing to 1: S sensitive (unaware, susceptible), U upset (aware, spreading, not violent), I immune, V violent, R relaxed. The drive-like content is only the two states U (outrage) and V (revenge); no drive variable, no individual level, no data.
- **Operators / equations, transcribed [read].** Three-state SIR-like core (eqs 1-3):
  - dS/dt = -alpha S U
  - dU/dt = alpha S U - xi U
  - dR/dt = xi U
  Immunisation added (eqs 4-5, 6-7): S loses beta S U to I; failed immunisation returns kappa U I from I to U.
  Full five-agent set (eqs 8-11), as printed:
  - dS/dt = -alpha S U - beta S U - gamma S U - mu S V
  - dU/dt = alpha S U - xi U + kappa S I - sigma U U + mu S V
  - dR/dt = xi U + eta V
  - dV/dt = gamma S U - eta V + sigma U U
  Meaning: gamma, direct S to V on contact with U; sigma, U-U contact making V; mu, V turns S into U; xi, eta, relaxation rates (1/xi, 1/eta mean durations). Table 1 values: alpha 0.5-5, beta 0.5, gamma 0.2, mu 0.1, xi "1-30", eta "1-20", kappa 0.5, sigma 0.5. (The table prints the xi and eta ranges as 1-30 and 1-20 against descriptions "1/xi time units an individual remains spreader" and "1/eta time an individual remains violent"; reading these as durations, i.e. xi in 1/30-1, is an interpretation, consistent with the regressions using 1/xi and 1/eta.)
- **Defects in the printed equations [read, my check]:** eq 9 has "kappa S I" where eq 6 had "kappa U I" (typo or error). The full set omits the I equation (it is only in eqs 5 and 7), so as printed the system is not closed. The sum of eqs 8-11 loses beta S U (to I) and has the stray kappa S I, so mass is not conserved unless I is added with its own terms. Do not copy these equations without re-deriving.
- **Theorems / results [read]:** only the SIR threshold, derived analytically for the three-state core: U grows iff S > xi/alpha; reproduction number R0 = alpha/xi; with immunisation they state R0 = (alpha + kappa)/(beta + xi) [as printed, not derived in the text read]. For the full model they give **regression fits to simulations**, not theorems: U peaks when S_t is about -0.0293 + 0.3268 (1/xi) + 0.1718 (correlation coefficient 0.9057, MAE 0.0168, RMSE 0.0238), and V peaks when U_t is about 0.0283 alpha - 0.4061 (1/xi) + 0.429 (1/eta) + 0.174 (correlation 0.901, MAE 0.0309, RMSE 0.0396). The abstract's "conditions coinciding with a twofold spreading" are these fits.
- **Empirical standing [read + meta]:** none. Anecdotes (Innocence of Muslims film 2012, Operation Blue Star 1984) motivate it; no parameter is fitted to any data. Semantic Scholar lists 34 citing works [meta], a mixed set: contagion-ODE and crowd-emotion papers, but also rumour and information-diffusion, computer-virus, drinking-behaviour and radicalisation models (see 2.1).
- **Translation:** a clean example of an epidemic-class operator on a vector (S,U,I,V,R) of states-of-a-population. It is a *state* machine of people, not a drive model. For the algebra it is a ready-made "outrage-to-violence" transition graph; rates alpha, gamma, sigma are the unmeasured drive couplings.

### 1.2 Sack 2021, "Geometries of Desire" (file 18; file 17 says "no tested mathematical model of mimetic desire") [meta only]

- **Verified [meta]:** Graham Alexander Sack, "Geometries of Desire: Simulating René Girard's Mimetic Theory", in *Proceedings of the 2020 Conference of The Computational Social Science Society of the Americas*, Springer Proceedings in Complexity, pp. 217-243, 2021 (online 4 Jan 2022). DOI 10.1007/978-3-030-83418-0_13 resolves. Semantic Scholar: 1 citation; abstract and references withheld by the publisher.
- **Not read.** Springer returns a login redirect. The "theorems in an appendix" and "Nash equilibrium of desire" content in file 18 therefore remains abstract-level and unverified by me.
- **New finding for the negative claim:** the single recorded citing work is Maxwell J. Black, "A Computational Test of Girard's Scapegoat Mechanism", *Contagion: Journal of Violence, Mimesis, and Culture* 33, 195-220, 2026, DOI 10.14321/contagion.33.0195 [meta; publisher page 403, content unread]. File 17's absence claim ("no tested mathematical model of mimetic desire"; "one unreviewed NetLogo scapegoating model exists") and file 18's list of Girard models are both **incomplete**: a 2026 peer-reviewed computational test exists and is not in either file. Whether it tests against data or only runs a simulation is unknown. Action: read it.
- **Verdict on the negative claim:** "tested against data: none" is **unconfirmed, probably still true for Sack, possibly false for Black 2026**.

### 1.3 Smith, Seger & Mackie 2007 (file 18, "most important omission") [meta]

- **Verified [meta]:** Eliot R. Smith, Charles R. Seger, Diane M. Mackie, "Can emotions be truly group level? Evidence regarding four conceptual criteria", *JPSP* 93(3), 431-446, 2007; DOI 10.1037/0022-3514.93.3.431. 699 Semantic Scholar citations. Abstract not available to me. Its 40 sampled citing titles are all empirical or applied (collective action, intergroup emotions, team affect); none is a model.
- **Relevance to the negative claim:** file 18 claims "no defined aggregation rule for most 'group X' claims" and "group-level drives... not an operand". This paper is empirical (it tests whether group-level emotion differs from individual emotion), so it does not contradict either claim, but it is the evidence the algebra needs to decide whether group-level drive is a legitimate operand. Content tags in file 18 for it are "from standard account"; I did not upgrade them.

### 1.4 Bagarello & Oliveri 2010 (files 15, 16, 20 claim: no operators with algebraic laws; no composition of coupling operators) [read at validation, arXiv:1010.0210 section 2]

- **Verified [meta]:** Fabio Bagarello, Francesco Oliveri, "An operator-like description of love affairs", *SIAM J. Appl. Math.* 70(8), 3235-3251, 2010; DOI 10.1137/10079985x. Crossref abstract (summary): "occupation number representation" from quantum mechanics, also used for stock markets; two-person Alice-Bob model, periodic solutions (linear) or periodic or quasi-periodic (nonlinear); love triangle with analytic conditions in the linear case and numerical solutions in the nonlinear case.
- **Correction to the absence claims.** Files 15 (section "Does not exist": "any operators on drives with algebraic laws") and 20 ("operators are parameterised functions, not elements of a structure") are **too strong**. In Bagarello's line the state variables *are* operators obeying stated algebraic relations [read]: a1, a2 are independent **bosonic** operators with the canonical commutation rules [a_i, a_k†] = δ_ik 1, all other commutators zero (eq 2.1; not anticommutation); N_j = a_j† a_j is the number operator whose integer eigenvalue n_j is actor j's "level of attraction" (LoA). The Hamiltonian is H = λ(a1^M a2† + h.c.) (eq 2.4), so one application lowers Bob's LoA by M and raises Alice's by 1, and I = N1 + M N2 is conserved because [H, I] = 0. Dynamics are Heisenberg equations generated by H. File 20 already notes this line is "the one line... where people and interactions are operators"; it should not coexist with a blanket "no operators with laws" in files 15 and 16.
- **Two books found [meta, Crossref]:** Bagarello, *Quantum Dynamics for Classical Systems: With Applications of the Number Operator*, Wiley 2012, DOI 10.1002/9781118400586; Bagarello, *Quantum Concepts in the Social, Ecological and Biological Sciences*, Cambridge University Press 2019, DOI 10.1017/9781108684781. Neither was in files 15-21 (file 20 cites Bagarello, Gargano, Oliveri 2015 as the extension). The 2019 book's chapters include "Desertification" among ecological topics; whether it contains love, opinion, or group-level operator models beyond the 2010 paper was not checked.
- **Empirical standing:** none I could find; the models are not fitted to data. Quantitative standing remains zero; the correction concerns *algebraic structure*, not validation.
- **What still holds:** nothing in Bagarello states drive-specific operators (fear, curiosity, desire as distinct operators); each actor's "love" is one integer eigenvalue (the LoA) of one number operator, so there is one generator per actor-to-actor attraction, not per drive [read]. So "no operator algebra whose generators are separate drives" survives, as an unverified absence.

### 1.5 Liebovitch et al. 2008 (files 20, 15) [meta; content from file 20, [read] there]

- **Verified [meta]:** Larry S. Liebovitch, Vincent Naudot, Robin Vallacher, Andrzej Nowak, Lan Bui-Wrzosinska, Peter Coleman, "Dynamics of two-actor cooperation-competition conflict models", *Physica A* 387(25), 6360-6378, 2008; DOI 10.1016/j.physa.2008.07.020. Record matches file 20.
- File 20's content (tanh coupling, pitchfork, no-limit-cycle theorem, 3-10 actor numerics) was marked [read] there; not re-read here. Its absence claim "no fitted network version of Gottman, no general n-person theorem" was not independently re-searched (no search budget).

### 1.6 Battigalli, Corrao & Dufwenberg 2019 (file 21, "should be read before the drive slot design is fixed") [meta]

- **Verified [meta]:** Pierpaolo Battigalli, Roberto Corrao, Martin Dufwenberg, "Incorporating belief-dependent motivation in games", *J. Econ. Behav. Organ.* 167, 185-218, 2019; DOI 10.1016/j.jebo.2019.04.009. 59 Semantic Scholar citations. Summary of its abstract (paraphrase of the record, not quoted): a more practical framework for specific belief-dependent motivations, embedded in game forms, stressing timing and perception of intentions, and refining solution concepts with recent game-theory foundations.
- Companion survey, verified [meta]: Battigalli & Dufwenberg, "Belief-Dependent Motivations and Psychological Game Theory", *J. Econ. Literature* 60(3), 833-882, 2022, DOI 10.1257/jel.20201378 (matches file 21).
- **Relevance to a negative claim:** file 21 says "a drive that changes over time as a quantity" does not exist in this cluster. This paper's emphasis on *timing* is on the game form (when motives are evaluated), not on a decaying or accumulating state variable; this does not by itself overturn the claim, but I did not read it, so the claim is **not independently confirmed**.

## 2. New finds that bear on the negative claims

### 2.1 The outrage-contagion family is larger than file 18 says [meta]

Semantic Scholar's citing list for Nizamani et al. includes (titles and years as listed; none opened; re-pulled at validation, all seven titles present):
- "From Public Gatherings to the Burst of Collective Violence: An Agent-based Emotion Contagion Model" (2018)
- "Affinity and Hostility in Divided Communities: a Mathematical Model" (2015)
- "Modeling Radicalization Phenomena in Heterogeneous Populations" (2015)
- "Global stability in a mathematical model of de-radicalization" (2018)
- "Propagation of radical ideas in societies with memory: competition between radical strength and social cohesion" (2021)
- "Dynamics of competing public sentiment contagion in social networks incorporating higher-order interactions" (2024)
- "Intervening in Negative Emotion Contagion on Social Networks Using Reinforcement Learning" (2025); several crowd-emotion contagion papers for evacuations (2021-2025), including "Emotional Contagion-Aware Deep Reinforcement Learning for Antagonistic Crowd Simulation" (2021).

The full list of 34 is more heterogeneous than this selection suggests: about a third are rumour, news or information-dissemination models, and several are computer-virus or drinking-behaviour models that cite Nizamani only as an SIR-type precedent. These bear on file 18's claim that formal group-emotion models are thin and on file 17's "no formal model in which one person's act changes another's drive" (file 17 already flagged that as a search limit). The set contains control-flavoured papers ("intervening", "optimal policies"), which touches the "control with guarantees" absence in file 19. All unread; DOIs not checked; they are leads, not citations to rely on.

### 2.2 Statuses

| Absence claim (file) | Result of this check |
|---|---|
| Moral-panic formal model under that name (18) | Holds for Nizamani; not re-searched generally |
| No tested model of mimetic desire (17) | Weakened: Black 2026 found, unread |
| Sack's equilibrium results (18) | Citation verified, content unread |
| No operators with algebraic laws (15, 16, 20) | **Overstated**: Bagarello operator algebra exists |
| n > 2 theory (20) | Not re-checked |
| Drive varying in time in psych games (21) | Not re-checked |

## 3. What exists vs what does not (after this check)

Exists, now confirmed or newly located: an epidemic-class five-state outrage-to-violence ODE model with threshold results by analysis only for the three-state core and by regression for the full set, no data (Nizamani et al.); a 34-paper citing family of contagion-of-hostility models; operator-algebra models of interpersonal states (Bagarello, three sources); a 2026 computational test of Girard (Black); all six seed citations resolve to real works.

Does not exist (still unrefuted, but I could not search for it): a model that treats curiosity, fear and desire as separate operators with stated laws; any of these models fitted to data on a real group; a group-level drive as an irreducible operand.

## 4. Unconfirmed

- Contents of Sack 2021 (theorems, Nash equilibrium of desire): paywalled, unread.
- Black 2026 (publisher 403): whether it tests against data.
- Smith, Seger & Mackie 2007 findings: abstract unavailable to me.
- Battigalli-Corrao-Dufwenberg 2019 body.
- All independent absence searches for files 15-21 beyond these seeds: **not done** (search budget exhausted). In particular the claims in 15 ("no calculus of conflict resolution"), 17 ("no common unit across drives"), 19 ("no controllability analysis of drive dynamics"), and 21 are unchecked and should be re-run.

## Validation log (2026-10-29)

Every DOI below was resolved at api.crossref.org/works/<doi>; titles, authors, volume and pages matched unless noted. Semantic Scholar counts re-pulled by DOI. WebSearch was refused again at validation (same shared 200-call budget), so no "nothing exists" claim could be tested by a fresh search; the absence verdicts above stand as unverified, exactly as the method note says.

- ✎ Nizamani, Memon & Galam 2014, *Physica A* 416:620-630, 10.1016/j.physa.2014.09.006: citation ✓; arXiv:1310.0731 re-read; eqs 1-11, the kappa S I typo in eq 9, the missing I equation in the full set, R0 = alpha/xi and (alpha+kappa)/(beta+xi), Table 1 and both regression fits all match the text. Corrected: correlation 0.9057 (not 0.906) with RMSE 0.0238, V-fit MAE 0.0309 / RMSE 0.0396 added; "moral panic" confirmed absent from the whole paper, not just the part read; Table 1 prints xi as "1-30", so the durations reading is now flagged as interpretation; "34 citing works, almost all contagion/crowd-emotion" corrected to a mixed set. 34 citations ✓.
- ✓ Sack 2021, Springer Proc. Complexity, pp. 217-243, 10.1007/978-3-030-83418-0_13: sole author, online 4 Jan 2022, 1 citation. Content still unread (abstract elided by publisher).
- ✎ Black 2026, *Contagion* 33, 10.14321/contagion.33.0195: exists, sole author Maxwell J. Black; pages 195-220 added. Closed access, no abstract in Crossref or Semantic Scholar; whether it tests against data remains unknown.
- ✓ Smith, Seger & Mackie 2007, *JPSP* 93(3):431-446, 10.1037/0022-3514.93.3.431: 699 citations ✓; abstract elided.
- ✎ Bagarello & Oliveri 2010, *SIAM J. Appl. Math.* 70(8):3235-3251, 10.1137/10079985x: citation and abstract summary ✓. Upgraded to [read] from arXiv:1010.0210: the relations are bosonic CCR (the "or anticommutation" hedge removed), Hamiltonian H = lambda(a1^M a2† + h.c.) and conserved I = N1 + M N2 added; "single scalar eigenvalue" corrected to one number-operator eigenvalue per actor. No data fitted, confirmed. The correction to files 15/16/20 ("no operators with algebraic laws" is overstated) holds.
- ✓ Bagarello 2012, *Quantum Dynamics for Classical Systems*, Wiley, 10.1002/9781118400586.
- ✓ Bagarello 2019, *Quantum Concepts in the Social, Ecological and Biological Sciences*, CUP, 10.1017/9781108684781. Chapter contents ("Desertification") not checked.
- ✓ Liebovitch, Naudot, Vallacher, Nowak, Bui-Wrzosinska & Coleman 2008, *Physica A* 387(25):6360-6378, 10.1016/j.physa.2008.07.020.
- ✓ Battigalli, Corrao & Dufwenberg 2019, *JEBO* 167:185-218, 10.1016/j.jebo.2019.04.009; 59 citations; the paraphrase matches the abstract ("We emphasize the role of time and of the perception of players' intentions").
- ✓ Battigalli & Dufwenberg 2022, *JEL* 60(3):833-882, 10.1257/jel.20201378.
- ✓ Section 2.1 citing titles (seven named): all present in the Semantic Scholar citing list for Nizamani et al.; DOIs exist in that list but were not resolved individually and the papers were not opened, so they remain leads.

No fabrications found; nothing deleted. **Verdict:** every citation in this file is real and correctly attributed, and its one full read (Nizamani et al.) is transcribed accurately, with minor number and characterisation fixes made above; the Bagarello correction to files 15/16/20 is now backed by the text itself. The file's own caveat is the important part and remains true: it confirms or corrects specific seeds but does not test any general "does not exist" claim, because web search was unavailable both when it was written and at validation, so D546 still needs a re-run with search.

## Cross-checks (2026-10-29)

Method: grepped the other files in this directory for the same works, authors, equations and numbers (Nizamani, Bagarello, Sack, Girard, Black, Smith/Seger/Mackie, Liebovitch, Battigalli, Paes, NetLogo). Files with overlap: 17, 18, 20, 15, 16, 21, 057, 060, 065, 080. Primary source consulted: arXiv abs 1010.0210 (abstract only; the commutation relations and Hamiltonian were not re-verified here, they rest on this file's own full-text read).

### Agreements

- **Nizamani, Memon & Galam** (file 18 section 11 "moral panic" Formal models, and its validation list): file 18 gives arXiv 1310.0731, five agent types (upset, violent, sensitive, immune, relaxed) in ODEs, and "none is a moral-panic model by name". This file agrees on all three and upgrades the evidence from [from abstract] to [read]. No other file cites the paper, so no numbers or equations overlap.
- **Bagarello & Oliveri 2010** (file 20 section 4b, line "Bagarello and Oliveri (2010)"): same DOI 10.1137/10079985x, SIAM J. Appl. Math. 70(8):3235-3251, same occupation-number representation, same love triangle (Alice, Bob, Carla) with analytic conditions for periodic vs quasi-periodic solutions in the linear case. Consistent with the abstract fetched here. File 20 says the Hamiltonian form was "not opened"; this file supplies it, which adds detail and does not conflict.
- **Liebovitch et al. 2008** (files 20, 060 section 2, 080): same DOI 10.1016/j.physa.2008.07.020, Physica A 387(25):6360-6378, same six authors. File 080 notes an SSRN version without Naudot; the published list here includes him, which is consistent. File 060 says the 2008 3-10 actor numerics are the only other n > 2 result in that skeleton; this file did not re-check it.
- **Smith, Seger & Mackie 2007** (files 18 section 5 and Missing, 065): same DOI 10.1037/0022-3514.93.3.431, JPSP 93(3), 431-446. File 065 read the full text and found it tests four criteria empirically; this file's statement that it is empirical, not a model, agrees. File 065 itself already notes this file could not open the paper.
- **Sack 2021** (file 18 section 14): same title, proceedings and DOI 10.1007/978-3-030-83418-0_13. File 18 says its content is [from abstract], with theorems in an appendix; this file did not read it either, so both rest on the abstract.
- **Girard formal models are untested** (files 17 C3 and Missing, 18 sections 14 and Missing): files 17 and 18 say the models (Antunes 2014, Paes 2025 NetLogo, Sack) are untested against data. This file's "probably still true for Sack" agrees.
- **Battigalli-Corrao-Dufwenberg 2019 and the 2022 JEL survey** (file 21 line 245, 057 lines 204-217): file 21 names both and says to read them before fixing the drive slot. The JEL citation here (60(3):833-882, 10.1257/jel.20201378) is not contradicted by any file; file 057 says it does not cite them. No overlap in claims.

### Contradictions and discrepancies

1. **"No operators with algebraic laws" (files 15, 16, 20) vs this file section 1.4.**
   - File 15, "Does not exist": "Any operators on drives with algebraic laws... Nothing in this cluster states one."
   - File 20 line 182: "The operators are parameterised functions, not elements of a structure."
   - This file: Bagarello's number operators obey bosonic CCR, so the claims are overstated.
   - Verdict: **this file is right on substance, with scope caveats.** File 20 contradicts itself, since its own section 4b (line 77) calls Bagarello "the one line in this survey where the people and interactions are operators in an algebra". File 15's claim is scoped to taxonomies ("this cluster"), so Bagarello falls outside it and it is not wrong as written. File 16's "no algebra" lines (46, 362) are about the models in that file and about closure across rules, which Bagarello does not address. The claim about CCR and the Hamiltonian H = lambda(a1^M a2† + h.c.) rests on this file's full-text read of arXiv 1010.0210; the abstract fetched during this cross-check does not confirm those details, so that part is **unresolved by me**.
2. **File 17's absence claim vs file 18's.** File 17 (C3 and Missing) lists only Antunes and the NetLogo model and does not mention Sack; file 18 says Sack exists. Not a conflict in the strict sense, since 17 says "tested", but 17 is incomplete. This file's note that 17 and 18 omit Black 2026 stands: neither file mentions Black, Contagion 33. Verdict: this file is right that Black is missing from both; whether Black tests against data is **unresolved** (paywalled).
3. **Girard model list.** This file says file 18's list is incomplete. File 18 already includes Paes 2025 (the CoMSES NetLogo model that file 17 calls "unreviewed"). That is the only model this file's "NetLogo" remark could refer to, and it is not new. Not a contradiction; the incompleteness concerns Black 2026 only.
4. **File 060 "only other n > 2 result" vs file 20 and this file.** File 060 (line 13) says the 2008 3-10 actor numerics are the only other n > 2 result in the Gottman-Liebovitch skeleton. File 20 lists triangles in Bagarello-Oliveri, Dercole-Rinaldi, Sprott and Bielczyk. These are different skeletons, so it is consistent, but the wording in 060 is easy to misread. Verdict: no change to this file.

No numeric or equation conflicts were found: only this file reports Nizamani's equations, Table 1 values and regression coefficients, so there was nothing to compare them against. No primary-source search was needed beyond the arXiv abstract above.

## Licences of quoted and transcribed material (2026-10-30)

- **Nizamani, Memon & Galam 2014**, *Physica A* 416:620-630 (arXiv:1310.0731). Licence: not determined; publisher copyright (Elsevier) presumed, and the arXiv preprint licence was not recorded. Use: equations 1-11 restated as the model's rate terms (the "as printed" wording marks fidelity to the source, not a copy of surrounding text), the Table 1 parameter values restated as numbers (facts, 8 values), the two regression fits and R0 expressions restated, and a few words of vocabulary in quotation marks. No prose is reproduced. Audit verdict "check": text left unchanged. If the repo is opened, either confirm the arXiv licence or reduce the equations to a citation to eqs 1-11 and Table 1.
- **Bagarello & Oliveri 2010**, *SIAM J. Appl. Math.* 70(8) (arXiv:1010.0210). Licence: not determined; publisher copyright presumed. Use: restated commutation relation and Hamiltonian (eqs 2.1, 2.4), a paraphrase of the Crossref abstract, and one short quoted phrase ("occupation number representation").
- **Battigalli, Corrao & Dufwenberg 2019**, *JEBO* 167. Licence: not determined; publisher copyright presumed. Use: paraphrase of the abstract; one nine-word quotation in the validation log.
- **Sack 2021; Black 2026; Smith, Seger & Mackie 2007; Liebovitch et al. 2008; Bagarello 2012 and 2019; Battigalli & Dufwenberg 2022.** Licence: not determined; publisher copyright presumed. Use: citation and bibliographic metadata only. Paywalled text was not read or reproduced.
- **Crossref and Semantic Scholar records** (DOIs, titles, years, citation counts, the seven citing titles in 2.1). Use: dataset citation of bibliographic facts. Crossref metadata is released as CC0; Semantic Scholar's licence terms were not checked here (not determined).
