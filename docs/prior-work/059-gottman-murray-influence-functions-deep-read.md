# Prior work 059: Gottman-Murray influence functions, read at source

Direction: D186
Date: 2026-10-29. Kind: deep-read. Question: thresholds, steady states, fitted parameters of the Gottman-Murray influence-function model, and how its terms map onto drive terms. Cross-references: `20-dyadic-coupling.md` section 1 (survey, mostly secondary), `03-interaction-as-operator.md` (pointer only), `47` and `49` (Keramati-Gutkin coupling), `16` (drive models).

**Method and honesty note.** Three primary papers were downloaded as PDFs from johngottman.net and read with `pdftotext`: Cook et al. 1995, Gottman, Swanson and Murray 1999, and Gottman, Levenson et al. 2003. Numbers and quotations tagged **[read]** come from those texts. Equations 3, 4 and 5 of Cook et al. are images and did not survive text extraction; they are reconstructed from the prose and from Murray's text as quoted in survey 20, and tagged **[reconstructed]**. Gottman, Swanson and Swanson 2002 (*PSPR*) and the 2002 book were NOT obtained (no free PDF found; abstract only). All four DOIs below were resolved against Crossref on 2026-10-29. Tags: **[read]**, **[reconstructed]**, **[derived]** (my own algebra from the stated equations, not in the papers), **[abs]**.

## Summary (what this pass settles)

1. **The threshold-sign dispute in survey 20 is resolved, and neither draft was wrong in the way it feared.** In the 1999 newlywed study, couples who later divorced had a *more negative* husband negativity threshold (mean -7.71 vs -5.36 for stable; F(1,123) = 8.25, p < .01). "More negative" means the husband had to become *more hostile* before the wife's response changed. The abstract's "lower negative threshold" means lower on the number line, i.e. larger in magnitude. So stable couples have the *smaller-magnitude* threshold, i.e. they respond to milder negativity (the "marital negativity detector"). Murray's "lower" and the popular "good couples react early" are the same finding in two vocabularies. **Only the husband's threshold was significant; the wife's was not (F = 0.03).** [read]
2. **The lag convention differs between papers.** Cook et al. 1995 state the model with alternating turns: `W(t+1) = f(W_t, H_t)`, `H(t+1) = g(W_{t+1}, H_t)` (the wife speaks first; the husband answers her new turn) [read]. The 1999 paper prints both influence terms at lag t: `W_{t+1} = a + r1 W_t + I_HW(H_t)`, `H_{t+1} = b + r2 H_t + I_WH(W_t)` [read, OCR; its Figure 1 caption still says `I_WH(W_{t+1})`, so the printed text is internally inconsistent]. The 2003 paper is simultaneous (lag t) with added repair and damping terms [read]. An algebra must pick one; they have different stability conditions (section 6).
3. **The headline prediction is a statistic on 17 divorces, with weights tuned on earlier divorce data.** The SPAFF code weights "were based on the differential ability of the specific codes to predict divorce in previous studies in our laboratory" [read, 1999 p. 11]. The affect scale is therefore not independent of the outcome. No out-of-sample test of the 1999 parameters was found.
4. **Cook et al. 1995 present no statistical tests for the typology.** "Note that we present no statistical tests here. Our purpose is the qualitative description of the data for generating theory." [read]. The five-way influence-function typology (volatile, validating, avoiding, hostile, hostile-detached) rests on couple-group averages, with subgroup sizes not stated in the text I could read.
5. **No drive is modelled.** The state is one weighted valence score per speaker per turn. Mapping it to a drive needs a stated interpretation (section 7).

---

## 1. Citations (all DOIs resolved on Crossref)

- Cook, J., Tyson, R., White, J., Rushe, R., Gottman, J., and Murray, J. (1995). Mathematics of marital conflict: qualitative dynamic mathematical modeling of marital interaction. *Journal of Family Psychology* 9(2):110-130. doi 10.1037/0893-3200.9.2.110. [read in full]
- Gottman, J., Swanson, C., and Murray, J. (1999). The mathematics of marital conflict: dynamic mathematical nonlinear modeling of newlywed marital interaction. *Journal of Family Psychology* 13(1):3-19. doi 10.1037/0893-3200.13.1.3. PDF: johngottman.net/wp-content/uploads/2011/05/The-Mathematics-of-Marital-Conflict-Dynamic-Mathematical-Nonlinear-Modeling-of-Newlywed-Marital-Interaction.pdf. [read in full]
- Gottman, J. M., Levenson, R. W., Swanson, C., Swanson, K., Tyson, R., and Yoshimoto, D. (2003). Observing gay, lesbian and heterosexual couples' relationships: mathematical modeling of conflict interaction. *Journal of Homosexuality* 45(1):65-91. doi 10.1300/J082v45n01_04. [read in full; the equation section and results quoted below]
- Gottman, J., Swanson, C., and Swanson, K. (2002). A general systems theory of marriage: nonlinear difference equation modeling of marital interaction. *Personality and Social Psychology Review* 6(4):326-340. doi 10.1207/s15327957pspr0604_07. [abs only; not read]
- Gottman, J. M., Murray, J. D., Swanson, C. C., Tyson, R., and Swanson, K. R. (2002). *The Mathematics of Marriage: Dynamic Nonlinear Models.* MIT Press. [not read; the 2003 paper cites it as "in press" for the estimation algorithms for each parameter and influence function]
- Input to the model: Gottman, J. M., and Levenson, R. W. (1992), "Marital processes predictive of later dissolution", *J. Personality and Social Psychology* 63:221-233 (cited by Cook et al. as the source of the regulated/nonregulated predictor; not opened).

## 2. Their vocabulary [read]

- **Score / affect:** the weighted positive-minus-negative code total per speaking turn (RCISS, 1995) or per 6-second block (SPAFF, 1999 and 2003).
- **Uninfluenced set point / steady state:** the level a speaker would hold if the partner's score were zero. 1995 "set point", 1999 "steady state" [read]. Computed as `a/(1 - r1)` for the wife and `b/(1 - r2)` for the husband.
- **Emotional inertia:** `r`, the lag-one autoregression of the speaker's own series.
- **Influence function:** `I_AB(x)`, "the influence of person A's state at turn t on person B's state". Attributed to the influencer "although we recognize that the influenced spouse also plays a part in determining the influence" [read, Cook p. 120].
- **Influenced steady state:** an intersection of the two null clines. Also called an attractor if stable [read].
- **Null cline:** for each person, the locus where that person's score is unchanged over one iteration, as a function of the partner's score.
- **Negativity / positivity threshold:** the points on an S-shaped influence function where the partner's score starts to have an effect.
- **Basin of attraction; separatrix; first-order vs second-order change** (steady states move vs influence functions change) [read, Cook p. 119].
- **Regulated / nonregulated couples:** Gottman-Levenson variable; regulated if both spouses' cumulative positive-minus-negative speaker-code plot has a significantly positive slope [read].
- **Repair and damping (2003):** repair is a jump in the series when the partner's negativity crosses a threshold; damping is its mirror for positivity. "We viewed repair as a communication strength and damping as a communication deficit." [read]
- **Marital negativity detector:** the 1999 label for a low-magnitude negative threshold.

## 3. Operands

Each partner is a scalar time series `x_t` on a fixed axis. Scale: SPAFF weights give a "potential range of -24 to +24" per 6-second block [read, 1999]. Weights [read, 1999 p. 11]: anger -1, sadness -1, fear 0, defensiveness -2, contempt -4, belligerence -2, domineering -1, stonewalling -2, disgust -3, whining -1, neutral +0.1, interest +2, affection +4, humor +4, listener backchannel or validation +4, joy +4. (The 2003 paper's list has the same values and adds "Validation = +4".) RCISS (1995) used speaker-code point counts per turn, Cohen's kappa .72 across subcodes; SPAFF kappa averaged .80 and generalisability coefficients averaged .907 in the 1999 sample [read]. 2003: same weights, observer correlation .90 for married, .52 for gay and lesbian couples [read].

Parameters live on each person (set point, inertia) and on each ordered pair (influence function).

## 4. Equations stated exactly

**4.1 Uninfluenced component** [read, Cook eq. 2]: `P_{t+1} = r_i P_t + a_i`, set point `P* = a_i/(1 - r_i)`, stable iff `|r_i| < 1`. "The natural state needs to be stable, so we were only interested in the case in which the absolute value of r_i was less than one." [read]

**4.2 Full model, 1995 (alternating turns)** [reconstructed from Cook eqs. 1, 3, 4 and prose; confirms the form quoted from Murray in survey 20]:

    W_{t+1} = a + r1 W_t + I_HW(H_t)
    H_{t+1} = b + r2 H_t + I_WH(W_{t+1})

Cook's own definition has a labelling slip: the text says "W_t and H_t as the husband's and wife's scores" in the same paragraph where "we assumed... the wife speaks first" and `W` is used for the wife throughout the rest. Treat W as the wife.

**4.3 Full model, 1999 (as printed)** [read, OCR]:

    W_{t+1} = a + r1 W_t + I_HW(H_t)          (1)
    H_{t+1} = b + r2 H_t + I_WH(W_t)          (2)

with "the uninfluenced steady states actually a/(1 - r1) and b/(1 - r2)". The caption of Figure 1 writes the husband-to-wife influence as `I_HW(H_t)` and the wife-to-husband as `I_WH(W_{t+1})`, so the paper itself is not consistent about the lag in (2).

**4.4 Full model, 2003 (with repair and damping)** [read]:

    N_{t+1} = r1 N_t + a + I_{P->N}(P_t) + E_PR R(K_P) + E_PD D(K_P)
    P_{t+1} = r2 P_t + b + I_{N->P}(N_t) + E_NR R(K_N) + E_ND D(K_N)

N is the "initiator" (the spouse who raised the issue), P the "partner". `R(.)` "is a standard trigger function that makes the time series jump to a higher value with amplitude E (the effectiveness of repair) at the trigger threshold of negativity, K". `D(K)` is "a mirror of repair, reducing the positive effects of positive affect after K, a threshold trigger of positivity is crossed with effectiveness E". "It is the magnitude and not the sign of this measure that is important (it is expected to be a negative number precisely in order to have a damping effect)." The exact functional form of `R` and `D` is not given in this paper; it defers to the book. "Adding these terms to the model improved the fit of the model by an order of magnitude" (no fit statistic reported there). [read]

**4.5 Estimation** [read, 1999 p. 12]:
- Restrict to pairs where the partner's intervening score is zero. "We assume that the influence functions are zero at zero values; at the subset of values for which H = 0, using least squares fitting, we fit the reduced linear equation `W_{t+1} = r1 W_t + a`, and at the subset of values for which W = 0, ... `H_{t+1} = r2 H_t + b`." Minimum: couples with fewer than 10 zeros in the seventy-five 6-second blocks were dropped as missing (1999). The 1995 paper says about 15 percent of turns qualify.
- Residuals `I_HW = W_{t+1} - r1 W_t - a` and `I_WH = H_{t+1} - r2 H_t - b` are then fitted by "the ogive", with husband parameters `A_H, B_H, C_H, D_H, E_H, F_H` and wife parameters `A_W ... F_W`: six parameters per influence function. **The ogive's formula is not printed in the 1999 paper.** The thresholds are read off the fitted ogive. Software "can be supplied on request" (Swanson). [read]
- Cook's own footnote on the zero-influence assumption: "the assumption that zero scores have zero influence is arbitrary. We could have assumed nonzero influences, made these additional parameters, and estimated these parameters as well. In fact, an asymmetry in these parameters would be theoretically interesting." [read, fn. 7]

**4.6 Influence-function forms** [read]
- Two-slope (bilinear): two straight lines through the origin, one slope for positive scores and one for negative. 1995: "summarize these results using the two-slope form". 2003: "The functional form of the influence function we have found to fit our data the best is the bilinear form... Differences in slopes are our operational definition of power in the relationship, which is defined separately for positive and negative affect."
- Sigmoid / O-jive: zero influence inside a band around zero; a bounded positive constant beyond a positivity threshold; a bounded negative constant beyond a negativity threshold. Chosen in 1999 "because it permitted us to create four important new parameters in the model: the thresholds for negativity and the thresholds for positivity for each spouse". A third variant (threshold plus slopes) is mentioned and not fitted.
- Piecewise reading of the ogive [derived, from the prose]: `I(x) = -M_-` for `x < K_-`, `0` for `K_- <= x <= K_+`, `+M_+` for `x > K_+` (a smooth monotone version is what is fitted).

**4.7 Null clines and steady states** [reconstructed from Cook eq. 5 and the prose "simple algebra gives the form"; "the null clines have the same shape as the influence functions, ... moved over (translated) by a constant, and ... scaled by another constant"]:

    W-cline (alternating form, W against H_t):   W = [a + I_HW(H_t)] / (1 - r1)
    H-cline (against W_{t+1}):                   H = [b + I_WH(W_{t+1})] / (1 - r2)

Steady states are the intersections. With the sigmoid, "we can have one, three, or five steady states", with stable and unstable alternating (three stable, two unstable at five) [read, Figure 4 caption and text]. Stability is "only possible once we assume a functional form for the influence functions" [read]. The planned stability metric (1999): "the eigenvalue obtained from linearizing the model using Taylor series" near an attractor, to measure "strength of the attractors", noted as future work "we will have to see if this measure has validity" [read]. I found no paper in this set that reports it.

## 5. Fitted parameters and results (the tables)

### 5.1 Cook et al. 1995 [read, Table 1]

Sample: 79 couples assessed 1983; 73 followed up in 1987 (70 husbands, 72 wives); 42 regulated and 31 nonregulated couples (Gottman-Levenson 1992 sample, RCISS point graphs). Parameters by group (inertia, uninfluenced set point, influenced set point):

| Group | H inertia | H uninfl. | H infl. | W inertia | W uninfl. | W infl. |
|---|---|---|---|---|---|---|
| Volatile | .33 | .68 | .75 | .20 | .68 | .61 |
| Validating | .37 | .38 | .56 | .14 | .52 | .59 |
| Avoiding | .18 | .26 | .53 | .25 | .46 | .60 |
| Regulated mean | .29 | .44 | .61 | .20 | .55 | .60 |
| Hostile | .32 | .10 | .03 | .51 | -.64 | -.45 |
| Hostile-detached | .40 | -.42 | -.50 | .46 | -.24 | -.62 |
| Nonregulated mean | .36 | -.16 | -.24 | .49 | -.44 | -.54 |

Correlations with outcomes [read, Table 2]: divorce correlates with wife's set point r = -.42 (p < .001) and husband's set point r = -.32 (p < .05); inertia does not (husband .05, wife .22, n.s.). Wife inertia correlates with marital type r = -.54 (p < .001). Set points correlate with RCISS negative codes (e.g. husband contempt vs husband set point r = -.74). The paper's own summary: "both the husbands' and the wives' uninfluenced set points are related to the dissolution cascade variables... significantly predictive of divorce."

Qualitative results [read]:
- Validating couples: a roughly constant positive slope across the whole range (negative scores push the partner negative, positive scores push positive). Avoiding: influence only in the positive range (flat on the negative side). Volatile: influence "primarily with negativity" (flat on the positive side). Hostile: validator husband paired with avoider wife. Hostile-detached: validator husband paired with volatile wife. **Mismatch hypothesis:** unstable marriages are "failed attempts at creating a pure type". Cook concedes it cannot be tested on this data because the typing came from the same interactions: "the marital interaction is a means for classifying couples."
- A volatile-avoiding pairing was not found: "perhaps they are just too different for the relationship to survive, even temporarily." [read]
- Group means of the per-group Figure 6 slopes (values like .10, .20, .31 etc.) could not be reliably transcribed from the extracted layout; not used.
- Support for the mismatch hypothesis on separate data: husband-minus-wife differences in positive speaker codes F(1,70) = 4.12 (p < .05), negative codes F(1,70) = 10.42 (p < .01), difference F(1,70) = 8.57 (p < .01), larger in the unstable groups [read].
- Influenced set points are more positive than uninfluenced ones in regulated couples, and more negative in nonregulated couples: "the effect of influence in nonregulated marriages is to make the set point more negative, whereas, in general, the reverse is true in regulated marriages" [read]. The exception is the volatile type.

### 5.2 Gottman, Swanson and Murray 1999 [read, Tables 1 and 2]

Sample: 179 couples screened; 130 newlyweds in the lab (first marriages, within 6 months, childless; Puget Sound, 1989-92); followed 3-6 years; 17 divorces (6, 6, 5 by cohort; the paper says about 22 would be expected). 125 couples had estimable models (excluding those with fewer than 10 zeros per half); df 1,123. Divorce comparison: 108 stable vs 17 divorced. A 3-group comparison used 20 happiest stable, 20 unhappiest stable (Time 2 MAT means 128.30 vs 90.70) and the divorced. 15-minute conflict discussion, 150 data points per spouse, 75 interacts on average.

**Table 1, divorce prediction** (mean stable / mean divorced; F with df 1,123; influenced steady state df 1,106) [read]:

| Variable | Wife stable / divorced | F | Husband stable / divorced | F |
|---|---|---|---|---|
| Inertia | 0.39 / 0.42 | 0.20 | 0.40 / 0.30 | 3.07 (p < .10) |
| Uninfluenced steady state | 0.51 / -2.26 | 14.86*** | 0.72 / -1.89 | 18.40*** |
| Positive threshold | 8.25 / 7.24 | 0.71 | 8.45 / 6.65 | 2.49 |
| Negative threshold | -6.23 / -6.06 | 0.03 | -5.36 / -7.71 | 8.25** |
| Influenced steady state | -0.65 / -1.95 | 1.29 | 0.71 / -1.49 | 4.36* |

(The text prints the husband's influenced steady states as 0.72 vs -1.89 and the table as 0.71 vs -1.49; the 0.72 and -1.89 are the uninfluenced values, so the text confuses the rows. Use the table.)

**Table 2, three criterion groups** (happy stable / unhappy stable / divorced; df 2,48) [read]:
- Wife uninfluenced steady state 1.07 / -0.03 / -2.26, F = 12.61***. Husband 1.06 / -0.41 / -1.89, F = 9.10***. Husband influenced steady state significant between groups per the text but listed F = 1.15 (df 2,41) in the table (the text says it discriminated; the table does not show significance, another inconsistency).
- Husband negative threshold -5.94 / -5.29 / -7.71, F = 2.22, n.s. in the three-group test. The divorced mean is the most negative, but the unhappy-stable mean (-5.29) is the *least* negative, so the ordering is not monotone with marital quality.
- Wife negative threshold -5.76 / -6.76 / -6.06, F = 0.28. Positive thresholds n.s. for both.

Reading of the threshold in the paper's own example: "a wife in a marriage that later turned out to be stable had initially reacted to her husband's defensiveness, whereas in a marriage that dissolved, the wife did not react until he became contemptuous, a more negatively weighted behavior." [read] In weights: defensiveness -2, contempt -4. (Note: that example concerns the wife's response to the husband's score, so it is a threshold in `I_HW`, whereas the table row labelled "Husband negative threshold" is the husband's own function. The paper uses "husband's threshold" to mean the husband's influence function's threshold, i.e. how negative he must be before the wife responds. I read it that way; the paper is not fully explicit.)

Other results [read]: uninfluenced steady states contain both an enduring-individual component and a prior-relationship (spillover) component (split-half regressions; wife F(7,108) = 8.62, husband F(7,107) = 17.72); the husband's enduring component relates to bad outcomes (interaction partial correlation -.25, p < .05). Exploratory correlates of the negative threshold (footnote 2): more negative when the couple's life was "chaotic", when negativity was spontaneously expressed in the interview, when the husband whined, and with lower "we-ness"; more months of counselling correlates with a more negative threshold, r = .35. Husband-rated severity of problems goes with a *lower* threshold (the footnote's wording; the sign convention "lower" is the ambiguous one here).

### 5.3 Gottman et al. 2003 (heterosexual, gay, lesbian couples) [read]

Four groups; two of them heterosexual (woman raises the issue or man does). Bilinear influence function fits best. Reported means:
- Uninfluenced steady state of the initiator: homosexual 0.61, heterosexual -0.98 (F(1,75) = 8.18, p = .005). Partner: 0.37 vs -1.09 (F(1,75) = 6.45).
- Repair effectiveness (partner): gay men 2.78, man initiating to woman 3.98, woman to man 3.99, lesbian 3.65.
- Repair threshold (partner): man initiating -4.64, woman initiating -6.04 (F(1,69) = 5.14, p = .027): "when a man initiates the issue, he detects negativity in his partner and attempts to repair sooner".
- Damping effectiveness: initiator -4.85 homosexual vs -3.11 heterosexual (p = .029); partner -5.03 vs -3.37 (p = .052).
- Slope of influence function: "In every study we have conducted with heterosexual couples using the mathematical modeling, the slope of the influence functions in the negative affect range is steeper than the slope in the positive affect range" (positive-slope minus negative-slope: man initiates to woman -.086, woman to man -.283, gay male -.331, lesbian -.122; the reversal for homosexual couples is marginal, p = .085). This is the model's version of "negative outweighs positive."
- Number of stable positive-positive attractors: homosexual 0.86 vs heterosexual 0.32 (p = .025); lesbian 1.14.
- The inter-rater correlation for the gay and lesbian sample is only .52 against .90 for married couples, which limits comparison.

## 6. Theorems and derived results

**In the papers (all qualitative, none proved):**
1. Steady states = null-cline intersections; with a sigmoid influence, one, three or five, alternating stable and unstable [read].
2. Initial conditions select the basin of attraction; the long-run direction of a conversation can depend "critically on the opening scores" [read]. Cook interprets this as why one couple can have a good and a bad conversation with identical parameters.
3. Bilinear influence "proposes that every marriage has a negative and a positive stable steady state... a 'dark side attractor,' and a 'bright side attractor'" [read, 1999 p. 17]. This is asserted from the shape, not derived or tested for existence in the fitted functions (the 1999 paper itself says most couples had one influenced steady state).
4. Damping can create a positive-positive stable attractor "where none existed before" [read, 2003]. Stated as a finding; no derivation is given in the paper.
5. The model "is, in some ways, rather grim": for most couples the initial conditions fix the trajectory [read].

**Derived here [derived], for the linear (bilinear within one half-plane) case.** Not in any of the papers; check before use.
- Simultaneous form (1999/2003): state `(W,H)`, linear influence slopes `c1` (H to W), `c2` (W to H). Map matrix `[[r1, c1],[c2, r2]]`. Fixed point `W* = [(1-r2) a + c1 b] / [(1-r1)(1-r2) - c1 c2]`, `H* = [(1-r1) b + c2 a] / [(1-r1)(1-r2) - c1 c2]`. Stable iff both eigenvalues have modulus below 1 (Jury conditions: `|det| < 1`, `|tr| < 1 + det`). The pole at `(1-r1)(1-r2) = c1 c2` marks the loss of the unique fixed point: this is the same cross-gain-versus-self-damping comparison as the pitchfork condition of Liebovitch et al. 2008 (survey 20).
- Alternating form (1995): substitute `W_{t+1}` into the husband's equation: map `[[r1, c1],[c2 r1, r2 + c1 c2]]`, determinant `r1 r2`, trace `r1 + r2 + c1 c2`. Fixed point is the same as above; stability conditions differ, because the effective husband inertia becomes `r2 + c1 c2`. So the lag convention is not cosmetic.
- With the two-slope form the map is piecewise-linear with four regions (signs of the two partner scores). With the piecewise-constant ogive each influence function takes three values, so the fixed-point equation reduces to a finite check over 3 x 3 = 9 combinations: a clean place for a theorem (existence and count of fixed points in terms of `a, b, r, M_+, M_-, K_+, K_-`). **The papers do not state it; it follows from their description.**

**What no paper here derives:** bounds on thresholds from outcomes, conditions under which repair terms produce a second attractor, any control or optimality result.

## 7. Empirical standing (blunt)

- **Sample and power.** 17 divorces in 125 couples (1999); 73 couples and 4-year follow-up (1995). With four to ten parameters per spouse and only a few significant, the multiple-comparisons exposure is substantial. Table 1 reports ten parameter tests; four reach p < .05 (two uninfluenced steady states, husband's influenced steady state, husband's negative threshold). No correction is mentioned.
- **No cross-validation.** The divorce finding is an in-sample group-mean comparison (F tests), not a predictive classification. The prediction-accuracy figures that circulate for Gottman's work come from other papers (see survey 20 on Heyman and Slep 2001, Kim, Capaldi and Crosby 2007; direction D187 covers them).
- **Outcome-tuned measurement.** The SPAFF weights were set by how well codes predicted divorce in earlier lab studies [read]. Combined with a single sample, the uninfluenced steady state (the strongest result, wife F = 14.86, husband F = 18.40) is a mean of that weighted score during a conflict conversation; its predictive power is largely the weighted score's predictive power.
- **The negative threshold is the weak link.** It is estimated from a fitted six-parameter ogive on roughly 75 interacts per couple, where the influence function is averaged over few observations at the extremes (Cook: "Only data close to the natural set point for each group could be trusted to avoid infrequent numbers of instances of RCISS values"). It is significant for husbands only, not in the three-group test, and the unhappy-stable group has the *least* negative mean. I found no independent replication of the threshold result and no estimate of its reliability.
- **Mismatch hypothesis.** Self-described as untestable on the same data. The partial support (husband-wife code differences larger in unstable groups) is from the same sample.
- **Parameters are per couple**, with no reported population distribution of influence-function shapes; the only population-level numbers are the group means above.
- **Replication of structure in other labs**: the 2003 paper replicates the same model form on four more groups from the same lab; Liebovitch et al. 2011 and Peluso et al. 2012 fit it to therapy sessions (survey 20, title and abstract only). I did not find an independent-lab fit of the *threshold* parameter to an outcome.
- **The 2002 book and PSPR paper** may report larger or later samples; not read, so nothing here should be taken as the final word on the model.

## 8. Operand/operator translation for the algebra

The model is a drive-like system with a different state variable, so the mapping needs to be explicit and none of it is in the sources.

| Gottman-Murray term | Role in the model | Candidate drive-algebra role | Strength of mapping |
|---|---|---|---|
| `x_t` (weighted affect) | Observed scalar per speaker | Net valence of the agent's momentary state, or the signed output of the drive system (reward minus drive level) | Weak; it is a measured behaviour code, not a latent drive |
| `a/(1-r)` (uninfluenced steady state) | Level held with no partner input | Homeostatic **set point** `H*` of the agent (compare `47`, Keramati-Gutkin `D = |H* - H|`), but with a nonzero mean rather than zero | Medium; the papers themselves say it mixes temperament and relationship history |
| `r` (inertia) | Persistence of own state | Relaxation rate `1 - r` toward the set point: speed of drive recovery | Medium; direct analogy, the Cook paper links it to arousal (hypothesis) |
| `I_AB(.)` | Partner's push as function of the partner's state | The inter-agent coupling term `w`, in a model of the form `D = D_self + w D_partner` (compare `49`) | Strong structurally; it is the one thing that is a genuine between-person operator |
| Negative threshold `K_-` | Level of partner negativity before the response engages | Dead-zone or trigger level of the response, comparable to a fear-detection threshold | Medium; a threshold on an input, not on the agent's own drive |
| Slope asymmetry (negative steeper than positive) | "Triumph of negative over positive" | Negativity-bias gain asymmetry (loss aversion analogue) | Medium; well supported as a descriptive regularity in the lab's own samples |
| Repair `E_R R(K)` | Upward jump after a negativity trigger | A regulatory controller engaging past a threshold (Powers-style loop) | Medium; but an additive jump, not a feedback law |
| Damping `E_D D(K)` | Reduction of the positive effect | A brake on over-positivity (contextual appropriateness) | Weak; authors say they "do not yet fully understand" it |
| Mismatch of `I` functions | Predicts instability | Incompatibility of the two agents' coupling operators | Hypothesis only |

**Operator algebra.** `I_AB` is a unary map from sender state to receiver push; the receiver combines push + own inertia + set point additively. Composition `I_BC o I_AB` is defined as a function but has no result in these papers; chains of three persons are not modelled. The additive combination of self and partner terms is an assumption (Cook: "the past two scores contribute separately and the effects can be added together"), not tested against interaction terms. The model has no drive other than the single valence axis; to use it for curiosity, fear or desire, the scalar would have to be replaced by a vector, and the influence function by a matrix of such functions. That step has no precedent in these papers.

## 9. What exists vs what does not

**Exists:**
- A fully specified discrete-time two-person coupled-difference model with a clear estimation procedure for inertia, set point, and influence function from a time series, and named parameters (set point, inertia, thresholds, repair, damping).
- Real fitted values on a scale of -24 to +24 for positive thresholds (about 6.6 to 9.1), negative thresholds (about -5.3 to -7.7), uninfluenced steady states (about -2.3 to +1.1), inertia (about 0.3 to 0.4 in the newlywed sample), for 125 couples, and group means for other samples.
- A defensible reading of the threshold direction: divorcing husbands needed more hostility from themselves to move their wives.
- Qualitative phase-plane results (alternating stable and unstable steady states, basins).

**Does not exist (in what I could read):**
- Any proof, closed-form or theorem about the model; the one-three-five steady-state count and the dark/bright attractor claim are asserted.
- The ogive formula, the trigger functions `R` and `D`, or the code (all deferred to the book or the author).
- A published stability or eigenvalue measure for fitted couples.
- A test of the model's *parameters* out of sample, or by an independent lab, as predictors of divorce.
- Anything beyond two persons or beyond one scalar state.
- Any link to a motivational drive; the authors never use the word.

## Unconfirmed

- The exact ogive formula (six parameters, `A` to `F`): the 1999 paper names them, does not print the formula.
- The exact repair and damping trigger functions: 2003 paper defers to the book.
- Murray's text as quoted in survey 20 (alternating-lag equations; "lower negative threshold" statement): not re-read this pass; consistent with Cook's eq. 1 and the 1999 abstract.
- Gottman, Swanson and Swanson 2002 (*PSPR*) contents, and any later sample or reliability data for the threshold parameter.
- The group sizes behind the Cook et al. Figure 6 influence-function typology, and the numeric slopes in the figure (OCR layout unreadable).
- Whether the printed `I_WH(W_t)` in 1999 eq. 2 is a typographical choice or the model actually used in that fit.
- Whether "husband's negative threshold" in the 1999 table means the threshold of the husband's influence function on the wife (my reading) or a threshold of the husband's own responsiveness; the paper's prose allows both.
- Heyman and Slep, Kim and Capaldi, and the 94 percent accuracy claim: not re-examined here (direction D187).
