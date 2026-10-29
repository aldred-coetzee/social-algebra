# Prior work 067: formal downward functions from group state to a member's drive

Direction: D249

Date: 2026-10-29. Kind: survey. Question: which published models give an explicit function from a group-level state to a member's drive-like variable (anger/grievance, efficacy, significance, fear)? Seeds: Friedkin 1999; Epstein 2002; Kozlowski et al. 2013. Follows file 24 (which said no downward function exists for a drive) and file 05 (Friedkin-Johnsen equations).

**Method and honesty note.** Tags: **[read]** read at source this session; **[abs]** abstract or search summary only; **[std]** standard account from background, unchecked; **[derived]** my own algebra from a [read] equation, not in any source.
- **Epstein: read, but the working paper, not the PNAS text.** The PNAS page returned 403 and the PMC copy sat behind a browser check (I did not try to bypass it). I read the Brookings Working Paper (Epstein, Steinbruner & Parker, "Modeling Civil Violence", CSED Working Paper 20, Jan 2001, `https://www.brookings.edu/wp-content/uploads/2016/06/cviolence.pdf`), the direct precursor, downloaded and text-extracted. Rules below are from it. The PNAS version may differ in detail (the working paper calls itself "work in progress"). Thron & Jackson (read) quote the PNAS form of P and agree with it.
- **Friedkin 1999: not read.** SAGE and JSTOR paywalled; only the abstract surfaced. The equations used are from file 05 (FJ 1990/2011) plus a read corollary in Biondi et al. 2023.
- **Kozlowski et al. 2013: not read.** SAGE 403; abstract only. Nothing equation-level is claimed from it.

## Summary

1. **Only one of the three seeds actually contains a downward function for a drive-like variable: Epstein.** Each agent's net risk N = R*P depends on the local cop-to-active ratio, so the group's current state (how many are already active near me) directly sets the cost-of-acting term in my decision. It is explicit, closed-form and monotone. It is a function onto a *risk/fear* term, not onto grievance (G = H(1-L) has no group input in the base model).
2. **Friedkin's is a downward function for an opinion, not a drive.** The group's positions move a member through the weighted-average term. Anything called "anger" or "efficacy" would have to be coded as an opinion-like scalar; no source does that.
3. **Kozlowski et al. 2013 is methodology, not a function** [abs]: it argues for simulation of bottom-up emergence. It tells you what a model must contain (a process, over time), not what the downward function is.
4. **Verdict on file 24's gap:** narrowed, not closed. Epstein supplies one worked case (fear/risk as a function of local active share). Nothing found supplies grievance, efficacy or significance as an explicit function of group state with an empirical fit.

---

## 1. Epstein (2002): net risk as a downward function of local group state

**Citation.** Epstein, J. M. (2002). Modeling civil violence: an agent-based computational approach. *PNAS* 99 (suppl. 3), 7243-7250. doi:10.1073/pnas.092080199 (Crossref-confirmed, issued 2002-05-14). Precursor read: Epstein, Steinbruner & Parker (2001), Brookings CSED WP 20 (URL above). Book reprint: *Generative Social Science* (Princeton), ch. 11, doi:10.1515/9781400842872.247 (Crossref-confirmed).

**Their vocabulary.** Hardship H, legitimacy L, grievance G, risk aversion R, estimated arrest probability P, net risk N, threshold T, vision v, active/quiescent (A/Q), cops C, jail term. "Preference falsification" (after Kuran) is named as the interpretation of T. Epstein explicitly separates private grievance from public action.

**Drives/operands.** Per agent: H ~ U(0,1) fixed, R ~ U(0,1) fixed, state in {Q, A}. Global: L (exogenous, equal across agents), cop density. The working paper is explicit that "we make no pretense to measuring model variables such as perceived hardship or legitimacy" [read].

**Operators / equations [read, working paper].**
- G = H(1 - L). "Grievance is the product of perceived hardship (H) and perceived illegitimacy (1-L)."
- P = 1 - exp[-k (C/A)_v], where (C/A)_v is the cop-to-active ratio within vision v, and the agent counts itself as active (so A >= 1). k "is set to ensure a plausible estimate (of P = .9) when C = 1 and A = 1". Appendix A: k = 2.3. [derived check: exp(-2.3) = 0.1003, so P(1,1) = 0.90, consistent; k = 2.3 is ln 10 rounded, so P is approximately 1 - 0.1^(C/A), which is how Thron & Jackson write the PNAS form (their eq. 4).]
- N = R P. Extension (appendix, not run): N = R P J^alpha, J = 1 + Jmax/Life, alpha in [0,1], alpha = 0 in all runs, so **jail has no deterrent effect in the published runs** and released agents "leave jail exactly as aggrieved as when they entered".
- Agent Rule A: if G - N > T be Active, otherwise Quiet. Appendix A: T = 0.1.
- Cop Rule C: inspect all sites within v* and arrest a random active agent. Movement Rule M: move to a random site within vision. Asynchronous activation, random order. 40x40 torus, initial population density 0.7, cop density 0.04 (0.074 in runs 3-5), v = v* = 1.7 or 7, Jmax 15/30/infinite, cloning prob 0.05 (Model II). Max age: Appendix A lists 200 for all models, but the Model II text says "max_age=100" and Appendix A is footnoted "Departures noted in text", so Model II ran with 100 [read; corrected in validation].
- Tension index (Fig. 7, "Tension and Actives"): G*B / R-bar, with B the fraction quiescent ("Blues") and R-bar mean risk aversion; Epstein says the true warning is a *dip* in this index just before an outburst, from one run.
- Appendix extensions (not run, so no results): endogenous legitimacy L_B(t) = L0 (1 - sum_{i=1..m} beta_i^i), beta_i the fraction of Blues killed by Greens i periods ago (a memory-m, discounted grievance update); retaliation-aware risk P = 1 - exp[-k((C + A_G)/A_B)_v]; group-specific hardship distributions as relative deprivation.

**Theorems or derived predictions.** None proved. Reported simulation phenomena [read, from one or few runs each]: (a) *individual deception*: a high-grievance agent is Quiet while cops are within vision and turns Active when they leave; (b) *catalysis*: a local cluster of actives lowers local C/A, lowering P and N for neighbours, so less aggrieved agents join ("to be the first rioter one must be very angry or very risk neutral... to be the 4000th... far lower"); (c) punctuated equilibrium in total actives, persisting over 20,000 iterations; (d) *salami result*: legitimacy falling 0.9 -> 0.2 in small steps produces no outburst, while a single drop 0.9 -> 0.7 at t = 77 produces one, so the *rate* of change matters; (e) cop reductions do tip society, unlike slow legitimacy decline. Model II (two ethnic groups, cloning, death) produces local ethnic-cleansing episodes at L = 0.8; high L gives peaceful coexistence.

**[derived] structure of the downward function.** Agent i is active iff H_i(1-L) - R_i(1 - e^{-k x}) > T with x = (C/A)_v. Solving: if G_i - T >= R_i the agent is active whatever the group does (the "extremist" set); if G_i - T <= 0 it is never active; otherwise active iff x < x_i* = -(1/k) ln(1 - (G_i - T)/R_i). So the group enters each member only through the single scalar x, via a threshold, and the individual parameters (H, R) only set where on x that member flips. **Credit: this reduction is not new.** Thron & Jackson (2013/2015, sec. 4.1) [read] already reduce Epstein's agents to a population "activism response function" f(y) of the local active-to-cop ratio y, and with H, R ~ U(0,1) give the extremist fraction (Gmax - T)^2/(2 Gmax) (active whatever the cops do) and the inert fraction T/Gmax (never active), Gmax = 1 - L; the per-agent cut-off x_i* is my restatement of the same algebra, and their two fractions follow from my two boundary cases by integrating over H and R (checked). It is a Granovetter threshold model (file 05) with the threshold on a *ratio* rather than on a count, plus a fixed point question (how many agents have x_i* above the local x). I have not carried out the mean-field fixed-point calculation; the spatial and mobile structure breaks the simple version. The 'P' term is a function from group state to a fear-like operand and it is **positive feedback**: more actives, lower N, more actives.

**Empirical standing (blunt).**
- Epstein states no calibration; the model is a generator of qualitative patterns ("recognizable macroscopic revolutionary dynamics"). The "fits" are visual resemblance.
- **Thron & Jackson (read)**, "Practicality of agent-based modeling of civil violence: an assessment", arXiv:1501.05838 (arXiv-confirmed, submitted 22 Jan 2015; arXiv comment: "Originally presented at the International Organization for Social Sciences and Behavioral Research (IOSSBR) Conference (Fall 2012, Biloxi MS), JSSR 2013, Volume II"; no journal-ref or DOI on arXiv, journal record not verified): (i) the grievance form G = H(1-L) "is based solely on a plausibility argument by Epstein, and has never been verified by any empirical studies"; R and T "have never been subject to statistical study"; (ii) outbursts are produced "entirely by lapses in cop coverage" from random cop placement (Poisson-distributed coverage), so Epstein's liberalisation inference is "called into question"; (iii) the widely distributed NetLogo version, Wilensky's "Rebellion" model (Wilensky 2004, their ref. 2), replaces P with a floor-function form P = 1 - 0.1^floor((C/A)v) (their eq. 5; the extracted text lost the floor brackets); T&J say Wilensky chose it empirically because, "unlike (4) it produces outbursts", and on their own analysis the original form "has no critical crowd size (and hence exhibits no outbursts)". Note this sits awkwardly with Epstein's own working paper, which reports outbursts with the exponential form; T&J do not reconcile the two; (iii-b) their abstract states that "there are no 'tipping points'" and behaviour changes smoothly with parameters, which contests Epstein's cop-reduction tipping result (e) above; (iv) conclusion: similarity to riot phenomena "are the result of generic mathematical properties of the model, and are not due to the fact that the model gives an accurate causal explanation"; the dynamics are self-organised-critical and intrinsically hard to forecast. They also argue real riots recruit via peers, not only via absent police, i.e. this downward channel (police absence) omits the social one (others like me are acting).
- I found no empirical fit of the P function to arrest data in this session. Not searched exhaustively.

**Operand/operator translation.**
- Operand: a member carries (G, R) fixed; the group supplies a scalar state x = (C/A)_v, local not global.
- Operator: D_k : x -> P = 1 - e^{-kx}, then N = R*P, then a threshold test on G - N. Composition: grievance (G) minus fear (R * P(x)).
- Which drive is it? G is a drive-like term, N is the fear term. The downward function acts on fear only. A unified algebra could reuse this form: "other-actor state lowers the member's fear/cost term". Needs a separate downward term for grievance, which Epstein's appendix [read] only gestures at (endogenous L, memory m).

---

## 2. Friedkin (1999): choice shift as a structural property of influence

**Citation.** Friedkin, N. E. (1999). Choice shift and group polarization. *American Sociological Review* 64(6), 856-875. doi:10.1177/000312249906400606 (Crossref-confirmed; duplicate JSTOR DOI 10.2307/2657407). Later chapter of the same name in Friedkin & Johnsen (2011), *Social Influence Network Theory* (CUP).

**Their vocabulary [abs].** Choice shift = difference between the group's mean final and mean initial opinion; the paper argues that choice shifts "are a ubiquitous product of the inequalities of interpersonal influence that emerge during discussions of issues" rather than of a group norm or decision rule.

**Drives/operands.** An attitude/opinion on an issue per member. **Not a drive.** Susceptibility a_i in [0,1] and influence weights w_ij.

**Operators / equations.** The model behind it (FJ / SINT): y(t+1) = A W y(t) + (I - A) y(1), with W row-stochastic, A = diag(a_i); fixed point y* = (I - AW)^-1 (I - A) y(1) if rho(AW) < 1. Exact form is in file 05 sections 4 [read there]; **not re-read here from the 1999 paper**, so the 1999 statement of it is [std].

**Theorems or derived predictions.**
- [read, Biondi, Boldrini, Passarella & Conti, "Dynamics of opinion polarization", IEEE Trans. SMC: Systems 2023, doi:10.1109/tsmc.2023.3268758 (Crossref-confirmed), arXiv:2206.06134]: Definition 3: choice shift iff sum z_i != sum s_i (final vs initial mean). Corollary 7: restricted FJ (w_ii = 1, (D+I)z(k+1) = s + A z(k)) on an undirected graph is never polarising and sum z_i = sum s_i, "there is never a choice shift". Corollary 6: variational FJ on undirected graphs polarises iff the self-weights w_ii are not identical; with identical self-weights, again no choice shift. They credit the undirected, no-choice-shift result for rFJ to Gionis et al. (their ref 26; I did not check it). Note these are *model* results for particular FJ variants, not Friedkin's 1999 theorem.
- So the mechanism by which the mean moves is asymmetric influence (non-doubly-stochastic structure, heterogeneous self-weight), which is Friedkin's thesis [abs] and consistent with the corollaries. The sign and size of the shift follow from the influence structure.

**Empirical standing.** Friedkin & Johnsen's small-group experiments are the support (file 05); I have not read the 1999 evidence. Choice shift/polarisation as a phenomenon has a large empirical literature (Myers & Lamm 1976, file 24); whether *this* model beats persuasive-arguments or social-comparison accounts in head-to-head tests: not checked. Treat as untested here.

**Operand/operator translation.** Downward function: y_i(t+1) = a_i sum_j w_ij y_j(t) + (1-a_i) y_i(1). The group enters as a weighted average of others' states; the member's own anchor (1-a_i) is the resistance. This is the general template for a linear downward function onto any scalar operand. To apply it to a drive (anger, efficacy) one must **assume** the drive is influenceable like an opinion; no source tests that. Two operators in the algebra: W (who weights whom) and A (how open each member is), exactly the "typing of operands" noted in file 05.

---

## 3. Kozlowski, Chao, Grand, Braun & Kuljanin (2013): emergence as dynamic process

**Citation.** Kozlowski, S. W. J., Chao, G. T., Grand, J. A., Braun, M. T. & Kuljanin, G. (2013). Advancing multilevel research design: capturing the dynamics of emergence. *Organizational Research Methods* 16(4), 581-615. doi:10.1177/1094428113493119 (Crossref-confirmed). (An ORM best-paper award was claimed here; not verified, moved to Unconfirmed.) A related follow-up: Kozlowski, Chao, Grand, Braun & Kuljanin (2016), "Capturing the multilevel dynamics of emergence: computational modeling, simulation, and virtual experimentation", *Organizational Psychology Review* 6(1), doi:10.1177/2041386614547955 6(1), 3-33 (Crossref: title "Capturing the multilevel dynamics of emergence", Feb 2016, authors Kozlowski, Chao, Grand, Braun, Kuljanin).

**Content [abs only; abstract read via OpenAlex, matches the summary].** Quantitative multilevel research mostly studies top-down contextual effects; bottom-up emergence is neglected; the authors argue for more direct, dynamic, temporally sensitive designs, with computational modelling/agent-based simulation as the direct route and complementary to indirect (measurement-based) designs. I could not read the paper, so cannot say whether it contains any functional form.

**What it contributes anyway.** The vocabulary in file 24 (Chan 1998 composition models; Kozlowski & Klein 2000 composition vs compilation) is the standard way to *classify* an upward function. The 2013 argument is that emergence is a process in time, so a model needs a state-update rule per time step. That is what Epstein and Friedkin both give. No downward drive function is derived.

**Operand/operator translation.** Provides the taxonomy for the upward map (mean, min, max, configuration, dispersion); the algebra should carry the upward map and the downward map as two explicit operators with a time index.

---

## 4. Adjacent models (checked lightly, flagged)

- **Bosse, Duell, Memon, Treur & van der Wal (2015)**, "Agent-based modeling of emotion contagion in groups", *Cognitive Computation* 7(1), 111-136, doi:10.1007/s12559-014-9277-9 (Crossref-confirmed). [abs only: Springer page redirected to a login] An agent-based model of emotion contagion in groups with absorb/amplify cases, simulated and analysed mathematically; coupled to an ambient agent monitoring and forecasting group emotion level. This is the closest candidate for a downward function onto an *emotion* (the group's level feeds each member's), but I did not see the equations, so nothing is stated. Worth a deep-read direction.
- **Granovetter thresholds, Latane social impact, Karau-Williams collective effort, Klandermans funnel:** already in files 05 and 24; they remain the other closed-form downward forms (threshold on active share; strength x immediacy x number). Not re-verified here.

---

## What exists vs what does not

**Exists:**
- One explicit, monotone, closed-form downward function onto a fear/risk term (Epstein: P = 1 - exp[-k C/A], N = R P), with a threshold decision rule. Simulated, qualitatively suggestive, unvalidated.
- A linear weighted-average downward function onto opinions with individual susceptibility (FJ/Friedkin), with theory (fixed points, choice-shift corollaries for variants) and small-group experiments.
- A methodology argument that emergence must be modelled as a time process (Kozlowski et al.).

**Does not exist (in what I found):**
- A downward function for *grievance/anger*, *efficacy* or *significance* with an empirical fit. Epstein's G has no group input in the runs; his endogenous-legitimacy and relative-deprivation extensions were never run [read: they are in the appendix].
- A tested form for Epstein's P. Thron & Jackson say even the published formula yields no outbursts in their analysis (contradicting Epstein's reported runs) and that Wilensky's floor-function form is used in practice.
- Any empirical estimate of k, R or T from real riots or arrests.
- A reading-level confirmation that Friedkin 1999 or Kozlowski 2013 contains anything beyond what is above.
- A cross-model comparison showing which downward form (threshold-on-ratio, weighted average, contagion) best predicts real member change.

## Unconfirmed

- Whether the PNAS 2002 text matches the 2001 working paper in every rule, parameter and run (not opened).
- Whether Epstein's P cited in PNAS is exactly 1 - exp[-k(C/A)_v]; the working paper, and Thron & Jackson's eq. 4 (as 1 - 0.1^(C/A) in form), agree, and the NetLogo floor variant differs.
- The full text, equations and evidence of Friedkin 1999; the Gionis et al. undirected-graph result cited by Biondi et al.
- Anything in Kozlowski et al. 2013 beyond the abstract, including whether it gives equations.
- Bosse et al. 2015 equations.
- Thron & Jackson's journal record (JSSR 2013, vol. II, per arXiv comment only; no DOI found).
- Kozlowski et al. 2013 winning an ORM best-paper award (search budget exhausted before it could be checked).
- All "does not exist" items above: the validation pass could not re-test them with fresh searches (session web-search limit reached), so they stand as the original author's negative findings, not independently confirmed.
- The mean-field fixed point of Epstein's rule; [derived] threshold x_i* above is my algebra and assumes a well-defined local x.

## Validation log (2026-10-29)

- ✓ Epstein 2002, PNAS 99 suppl. 3, 7243-7250, doi:10.1073/pnas.092080199: Crossref confirms title, sole author, pages, 2002-05-14. PNAS text itself not opened here either.
- ✓ Epstein 2012, *Generative Social Science* ch. 11, doi:10.1515/9781400842872.247: Crossref confirms (pp. 247-270).
- ✎ Epstein, Steinbruner & Parker 2001, Brookings CSED WP 20: re-downloaded and read. G, P, k = 2.3, T = 0.1, N = RP J^alpha, Rule A, Cop Rule C, Rule M, lattice/density/vision/jail values, tension index G B / R-bar and its dip, salami runs (0.9 -> 0.2 in 1%/cycle steps vs 0.9 -> 0.7 at t = 77), "4000th" quote, "no pretense" quote, Appendix B extensions (L_B = L0(1 - sum beta_i^i), retaliation P, relative deprivation) all confirmed. Corrected: Model II max age is 100 per text (Appendix A's 200 is overridden); "Run on warning signals" replaced by the figure name.
- ✎ Thron & Jackson, arXiv:1501.05838: read. All quoted phrases confirmed (plausibility argument, never subject to statistical study, lapses in cop coverage / Poisson, liberalisation "called into question", generic mathematical properties, peers in London/LA riots). Corrected: the NetLogo floor form is credited to Wilensky (2004); added their "no tipping points" result; added that their response-function analysis (extremist and inert fractions) already contains the file's [derived] threshold reduction, so credit moved to them; noted the unreconciled conflict with Epstein's reported outbursts. Journal record still unverified.
- ✓ Friedkin 1999, ASR 64(6), 856-875, doi:10.1177/000312249906400606 (and JSTOR 10.2307/2657407): Crossref confirms; abstract read via Semantic Scholar and matches the quoted "ubiquitous product" sentence. Full text still not read; the eScholarship link returned HTML, not the PDF.
- ✓ Biondi, Boldrini, Passarella & Conti 2023, IEEE TSMC: Systems 53(9), 5381-5392, doi:10.1109/tsmc.2023.3268758, arXiv:2206.06134: read. Definition 3, Corollary 6 and Corollary 7, the rFJ update (D+I)z(k+1) = s + Az(k) with w_ii = 1, and the credit to Gionis et al. [26] all confirmed.
- ✎ Kozlowski, Chao, Grand, Braun & Kuljanin 2013, ORM 16(4), 581-615, doi:10.1177/1094428113493119: Crossref confirms; abstract read via OpenAlex, consistent with the summary. Best-paper award claim unverified, moved to Unconfirmed.
- ✎ Kozlowski et al. 2016, OPR 6(1), 3-33, doi:10.1177/2041386614547955: Crossref confirms the same five authors; pages added.
- ✓ Bosse, Duell, Memon, Treur & van der Wal, Cognitive Computation 7(1), 111-136, doi:10.1007/s12559-014-9277-9 (online 2014): Crossref confirms; VU repository abstract matches (absorb/amplify, simulation plus mathematical analysis, ambient agent). Equations not read.
- ? Wilensky 2004, NetLogo Rebellion model: named via Thron & Jackson's ref. 2 only; not opened.
- ? Gionis et al. (Biondi ref. 26): not checked, as the file already says.
- No fabrications found.

**Verdict.** The note is accurate in substance: every citation exists with the stated authors, and the Epstein equations, parameters and quoted results check against the working paper. The corrections are of credit and detail rather than substance: the threshold reduction the note presented as its own algebra was already published by Thron & Jackson; the NetLogo floor form is Wilensky's; Thron & Jackson's "no tipping points" result directly contests Epstein's cop-reduction result; and Model II used a maximum age of 100. The negative ("nothing exists") claims could not be re-tested with searches in this pass and remain the original author's.

## Cross-checks (2026-10-29)

Checked against the other files in this directory by grep on Epstein, Thron & Jackson, Wilensky, Friedkin, Kozlowski, Bosse and the Epstein parameters. Files 068, 066, 063, 24, 18, 05 carry the overlaps.

### Agreements

- **Epstein equations and parameters (068 section 1 "Operators / equations, exact" and run settings).** G = H(1 - L); P = 1 - exp[-k (C/A)_v] with k = 2.3 (about ln 10, P(1,1) about 0.90); N = R P with the J^alpha extension and alpha = 0; Rule A with T = 0.1; 40 x 40 torus, density 0.7; vision 1.7 or 7; Jmax 15/30/infinite. All match this file. 068 read the PNAS text via PMC128592, so this also closes part of this file's Unconfirmed item that the PNAS text matches the working paper: the equations and parameters do.
- **Granovetter reduction.** 068 section 4 gives theta_i = -ln(1 - (g_i - T)/R_i)/k, the same as this file's x_i*, and the same inert and extremist boundary cases. 068 re-derived the closed form and the two Thron & Jackson fractions by hand. 066 (line 228) calls Epstein "Granovetter with a state-dependent threshold shift", compatible with "threshold on a ratio".
- **Only fear is coupled downward (068 operator 6).** 068: no operator raises grievance in neighbours; the only coupling is fear. Same as this file's summary point 1 and "Which drive is it?". 24 (section 10 and Gaps) says no formal downward function for a drive exists in the motivational theories; this file's verdict "narrowed, not closed" is consistent with that file's validation correction.
- **Thron & Jackson (068 section 5; arXiv:1501.05838).** Plausibility-only G, no study of R and T, outbursts from cop-coverage lapses, original response function has no critical crowd size, NetLogo floor form (Wilensky 2004, via their ref. 2, not opened in either file), extremist fraction (Gmax - T)^2/(2 Gmax) and inert fraction T/Gmax. Journal record unverified in both. 068 also failed to reproduce outbursts with the printed exponential P, which supports this file's point that T&J contradict Epstein's reported runs.
- **Salami tactics, the 4000th rioter, and tipping under cop reduction.** 068 results 6 and 7 agree with this file's items (c), (d), (e). I confirmed at PMC128592 that Epstein writes that "there comes a point at which a marginal reduction in central authority does 'tip' society into rebellion".
- **Friedkin 1999.** 24 (section 10) gives the same citation (ASR 64(6) 856-875; DOI 10.2307/2657407, same work as this file's 10.1177/000312249906400606). Neither file read the full text. 063 and 05 give the FJ fixed point consistent with the form used in section 2 here.
- **Kozlowski et al. 2013.** 24 cites the same paper as [abs], computational modelling of bottom-up emergence. Agrees; none claims equation-level content.
- **Bosse et al. 2015.** 18, 063, 066 all give Cogn. Comput. 7(1) 111-136, doi:10.1007/s12559-014-9277-9 and agree equations were not read. 063 and 18 add that the model family (ASCRIBE) has a weighted-mean core plus amplification, which is the likely downward function onto an emotion; see 066 section 5 and 18 for what is known.

### Contradictions and tensions

1. **Tension index: dip or buildup.** Here (section 1, Tension index bullet): the true warning is a dip just before an outburst. 068 (Tension index bullet): Epstein says "a buildup of tension precedes each outburst". **Verdict: both right, they quote different sentences.** In the Brookings working paper (re-extracted this session with pdftotext, section "A Ripeness Index") both appear: "It is clear that a buildup of tension precedes each outburst", then "on close inspection, our tension curve dips just at the outset of major explosions. The true warning indicator is this pronounced dip." The PNAS text (PMC128592) shows the buildup sentence, and a fetch summary did not show the dip sentence, so whether the dip claim survives into PNAS is unresolved. In the PNAS paper it is Fig. 8; in the working paper, Fig. 7. 068 should not be read as saying the buildup is the warning signal.
2. **Which runs used cop density 0.074.** Here: runs 3-5. 068: the Table 2 columns are garbled and read as runs 3 and 4 only. The PNAS text discusses these only through Table 2 and the column layout is unclear. **Unresolved**; this file's "3-5" should be read as the working paper's count, not the PNAS table's.
3. **Epstein outbursts with the exponential P.** This file reports Epstein's outbursts and T&J's denial side by side, unreconciled. 068 replicated the printed rule and got no outbursts with wide vision (v = 7) but sustained or near-threshold activity at v = 1.7. **Verdict: leans to T&J on the printed formula, but one unseeded replication; unresolved.** T&J "no tipping points" (here) versus Epstein's cop-tipping (068 result 7): 068's fixed-point scan found a single fixed point, no hysteresis, in the mean-field version, which supports T&J for that version. The spatial model is untested. Unresolved.
4. **Mean-field fixed point.** This file's Unconfirmed list says it was not carried out. 068 section 4 did so (exactly one fixed point in every case scanned). Not a contradiction, an update: this file's gap is filled by 068.
5. **Wording hazard, not a contradiction.** 063 lists "Friedkin & Johnsen 1999", *Advances in Group Processes* 16, a different work from Friedkin 1999, ASR. Do not merge them.

No source contradicted a numerical claim here beyond items 1 and 2. 068's note that Epstein's text calls the legitimacy drop 0.30 while 0.9 to 0.7 is 0.20 is a source inconsistency not mentioned in this file.

## Licences of quoted and transcribed material (2026-10-30)

Audit verdicts for this file were all "check": no text was changed. No tables or datasets are transcribed; equations are restated, not copied with surrounding text.

- **Epstein, Steinbruner & Parker (2001), Brookings CSED Working Paper 20.** Licence not determined; publisher copyright presumed. Use: short quotations (each well under 60 words, e.g. "we make no pretense to measuring model variables...", the "4000th" remark, "dips just at the outset"), restated equations (G, P, N, Rule A), and a description of parameter values and run settings.
- **Epstein (2002), PNAS 99 (suppl. 3), 7243-7250.** Licence not determined; publisher copyright presumed (PMC copy licence not recorded). Use: one short quotation of 22 words in Cross-checks ("there comes a point at which a marginal reduction in central authority does 'tip' society into rebellion"), plus restated equations. Access note: line 8 says the PNAS page returned 403 and the PMC copy sat behind a browser check that was not bypassed, while the Cross-checks (lines 143, 146, 153) say the PMC text was read at PMC128592. This file does not record how that access was obtained. Unresolved: confirm the text was reached legitimately (for example a normal browser view), or the claims that depend on it (the 22-word quotation, the "buildup" sentence, the parameter agreement) should be downgraded to [abs]/[std] with "readable copy not obtained legitimately; re-read needed".
- **Thron & Jackson, arXiv:1501.05838.** Licence not determined (arXiv default licence unknown for this deposit); publisher/author copyright presumed. Use: short quoted phrases (each a few words to one sentence) and restated equations and fractions.
- **Friedkin (1999), ASR 64(6), 856-875.** Not determined; publisher copyright presumed (SAGE/ASA). Use: one short quoted phrase from the abstract ("ubiquitous product of the inequalities of interpersonal influence...") and citation only.
- **Biondi, Boldrini, Passarella & Conti, arXiv:2206.06134 / IEEE TSMC 2023.** Not determined; publisher copyright presumed. Use: description of Definition 3 and Corollaries 6 and 7 in our own words, with short quoted phrase ("there is never a choice shift"), and restated update rule.
- **Kozlowski et al. (2013), ORM 16(4), 581-615.** Not determined; publisher copyright presumed. Abstract read only; used as paraphrase and citation.
- **Kozlowski et al. (2016), OPR 6(1), 3-33.** Not determined; publisher copyright presumed. Citation only.
- **Bosse et al. (2015), Cognitive Computation 7(1), 111-136.** Not determined; publisher copyright presumed. Abstract-level paraphrase and citation only.
- **Wilensky (2004), NetLogo Rebellion; Gionis et al.; Epstein (2012) book reprint.** Cited only (via Thron & Jackson, Biondi et al., Crossref); not opened or quoted.
