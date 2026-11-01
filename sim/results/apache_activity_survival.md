# Apache Incubator: team-scale activity and survival, against Claim 1's "state is a distribution", the size question and the early-warning signals

_Generated 2026-11-01 by `uv run python -m models.apache_activity_survival report` (seed 20261101; 500 permutations, 2000 bootstrap draws, 20 cross-validation repeats). Code: `sim/models/apache_activity_survival.py`; checks: `sim/tests/test_apache_activity_survival.py`. Ledger ids: the dataset L4623-L4633 (file 117 section 4.3) and L4666 (how 117's counts were made, its sections 0 and 8); Claim 1 and the cascade map L1225, L1831; size L5779, L5740; early warning L0512, L0527, L0547, L3057, L1404-L1406; individual dynamics L5742, L4367, L5764. Results are computed statistics only: no name, address or message text is kept anywhere in the repo, and the data files are local-use-only (`sim/data/README.md`)._

**What we are trying to achieve (one line).** An algebra of drives, of persons and of groups, composed into an equation set usable to predict or steer outcomes at the membership, group and crowd scales, sensitive to group size, composition and definition (`CLAUDE.md`, 2026-10-29).

**What was tested.** On the Apache Incubator sustainability dataset (CC BY 4.0), a proxy for the team-scale half of `models/00-v0.md` section 7. Per podling: per-member activity (distinct commits and human mailing-list messages) month by month, the number of regular members n, and the outcome (graduated or retired, from the ASF's own status file). Three questions. **(1)** Does the *distribution* of activity across members (concentration: Gini, top-k share, entropy; the shape, not the mean) predict graduation better than the *mean* activity, the spirit of Claim 1 (`models/02-our-claims.md` 1.1: a group's state is a distribution, because no summary of it fixes the outcome, L1225)? **(2)** What changes with n (Aldred's size question)? **(3)** Is there a measurable analogue of a threshold cascade or of escalation in the activity series: sustained growth against collapse, a critical mass, and the early-warning signals of 027 and 030 (rising lag-1 autocorrelation and variance before retirement, L0512, L0527)? It is a **proxy**: the dataset records no anchoring w_i, no enemy weight E_i and no tie signs, and its outcome is dissolution against a success exit, not a split (L4632; 117 section 5.3), so nothing here can refute the section 7 certificate.

## Verdict

**In short.**

- *(1) For the pre-specified measure (commits plus list messages) the shape of the activity distribution, added to team size and mean activity, does not predict graduation: not supported. For list conversation alone there is a lead.* At the first-year landmark (201 podlings with at least 3 regular members, 154 graduated and 47 retired) the held-out AUC for graduation is 0.76 for size alone and 0.58 for the mean activity per member; adding the four shape measures to size and mean changes it by +0.000 (bootstrap 95% interval -0.017 to +0.017; permutation p = 0.17, within size quintiles p = 0.18; likelihood-ratio p = 0.26). The Gini coefficient alone separates the outcome no better than the mean does (0.59 against 0.58; difference +0.01, 95% -0.08 to +0.11). Shape-only models reach 0.74, because top-3 share and Gini move with n. The mean per member is not told apart from chance (0.58, interval 0.48 to 0.68; 0.69 in the podlings started 2003-2012, 0.48 in the later ones); size is. **The lead:** counting only messages on the development lists (no commits), the Gini alone beats the mean by +0.11 AUC (95% +0.03 to +0.19) and the shape block adds +0.037 AUC to size and mean (permutation p = 0.007; within size quintiles p = 0.017), rising to +0.096 at 18 months (p = 0.003; p = 0.003): conversation carried by a few voices goes with graduation. It came out of a grid of 42 variants (33 distinct tests) and does not survive a correction over them (Holm p = 0.13 at 12 months); it is absent in podlings started 2003-2012 (gain -0.02, p = 0.31) and present in those started 2013-2021 (+0.08, p = 0.013), and it vanishes when automated senders are kept (-0.001). A lead to test on podlings after 2021 with the rule written first, not a finding (section 7.4).
- *(2) Size is the predictor, and the association of concentration with graduation changes with it: supported.* The graduation rate climbs with the number of regular members: 1-4 members 25% (1/4), 5-7 members 53% (9/17), 8-12 members 55% (17/31), 13-25 members 74% (51/69), 26+ members 93% (76/82). The pre-specified shape-by-size interaction is significant (likelihood-ratio p < 0.001 on 2 df), and the Gini x size term carries it (1 df, p < 0.001; the mean x size term p = 0.35); held out, size + Gini + Gini x size beats size alone by +0.013 AUC (paired 95% +0.002 to +0.024; the best of 12 forms, so biased upward). Where the association sits is post hoc: above the median size (n > 20) the Gini has a raw AUC of 0.73 for graduation (97 podlings, 9 retired), at or below it 0.51; the per-band AUCs rest on 6 to 18 retired projects per band.
- *(3) Growth against collapse is visible and predictive; a critical-mass step and early-warning signals are not found.* First-year activity up by half or more: 86% graduate (66/77); down by a third or more: 54% (21/39; Fisher p < 0.001). A smooth rise of graduation with early size beats a jump at a critical mass (held-out log-loss 0.464 against 0.499). Monthly early-warning statistics do not separate retirement from graduation (autocorrelation AUC 0.52, variance 0.58), **but they could not have**: in simulation they detect a true slowing down with AUC 0.55 and 0.43. Weekly series do have power (0.72 in simulation); there the data give 0.43 (0.33 to 0.53) for autocorrelation and 0.45 for variance; within retired projects the variance trend sits at 0.36 of the project's own history (nominal p = 0.035, one of 16 within-project tests, Holm 0.56): if anything decay, not slowing down. The level trend discriminates strongly (AUC 0.70 for graduation).
- *Individual dynamics carry the member-level signal; a mean-field coupling term adds nothing material.* Whether a member is active next month is predicted with AUC 0.90 by her own history alone (D1: persistence, rate, tenure, volume); adding the share of the other members active now (D2) gains +0.0007 AUC (+0.0002 to +0.0012), and a quadratic term for a threshold-like response gains +0.0010. v0 section 7's rule ("if D2 adds no predictive gain over D1 for who leaves, the coupling term goes") is met only for this proxy: D2 here is the others' activity share, not tie-based coupling (who replies to whom, 117 section 5.3), and the outcome is next month's activity, not departure. On that reading the dyad finding of 098 (partner term near zero beside inertia, L4367) reappears at team scale; the tie-based test has not been run.

**Status.**

- *Not supported (and bounded):* that concentration, entropy or top-k share of commits plus messages, added as a block, add held-out information about graduation beyond team size and mean activity (-0.017 to +0.017 AUC); that the mean activity per member predicts the outcome; that graduation turns on a critical early size (step against smooth); that the others' activity share adds to a member's own for staying active.
- *Supported:* that the number of regular members predicts graduation (AUC 0.76); that sustained growth against decline in the first year separates the outcomes; that the association of concentration with graduation changes with size (interaction p < 0.001, carried by the Gini x size term, p < 0.001); that a member's own recent activity predicts her next month (AUC 0.90).
- *Not found, with limits:* early-warning signals of the slowing-down kind before retirement: absent on monthly series (which have no power) and on weekly series (which would have caught a strong signal), so any such signal here is weaker than a rise of the lag-1 coefficient from 0.3 to 0.9. The retirement date is administrative, which blurs the reference point.
- *Lead, unconfirmed:* that the concentration of list conversation (messages without commits, automated senders removed) adds to size and mean, in the later half of the sample and at windows of 9 months or more; its point estimate is larger in the larger projects (development lists at 12 months: +0.100 above the median of 15 members, 11 retired, against +0.023 at or below it; post hoc). Found in the variation grid, not surviving a correction over it, to be tested on new podlings with a rule written first.
- *Undecided:* whether concentration matters in large projects specifically (a post hoc subgroup, see section 4); anything about thresholds, which this data cannot identify.

**What an activity-first outcome could be fitted to here, and what cannot.**

*Could be fitted:* (a) the team's size and the level and trend of its monthly activity, against exit (graduated or retired): size AUC 0.76, size plus growth 0.77, and the six-month retirement hazard from tenure, size and mean 0.79; (b) a member's own persistence, the set-point-and-inertia form D1, for staying active (AUC 0.90), which is the activity-first analogue of v0's D1; (c) a size-conditional concentration rule, as a Gini x size interaction term (held out +0.013 AUC over size alone), with concentration going with graduation in the larger projects; where it changes sign is post hoc and its mechanism is not in the data; (d) possibly, a conversation-concentration term (list messages without commits, robots removed), which is a lead for the later podlings and not a result.

*Cannot be fitted:* (a) any main effect of the *distribution* of commits plus messages beyond size and mean (its interaction with size is (c) above); (b) a mean-field coupling term (the others' activity share) beyond a member's own, while the tie-based D2 has not been tried; (c) a threshold or critical-mass cascade: thresholds are not observed (activity is an outcome of the thresholds, and an aggregate entry curve does not identify them: read as thresholds, the order in which members first appear gives a uniform distribution by construction), and the step-against-smooth test prefers smooth; (d) an early-warning rule of the slowing-down kind: the monthly series are too short for the indicators to work even when the signal is present, and the weekly ones, which would catch a strong signal, show none; (e) drives, tie signs, enemy weights E_i or anchoring w_i, none of which the data record; (f) a split: the outcome is dissolution against success, and the exit date is administrative (59 of 64 retired projects, and 203 of 205 graduated ones, show activity in the exit month itself, so a quiet spell before a retirement is not visible as a gap and the exit month's mail is at least partly about the exit; the messages were not read, by design); (g) causation: activity is both a cause and a symptom of the outcome.

## 1. Data and terms

- **Dataset.** Yin, Zhang, Xuan, Filkov, *Apache Software Foundation Incubator Project Sustainability Dataset*, version 1.1 (updated June 2021), Zenodo, doi:10.5281/zenodo.5637530, **CC BY 4.0** (open access; 117 section 4.3, L4623). Papers: Yin, Zhang, Xuan, Filkov 2021, MSR data showcase, doi:10.1109/msr52588.2021.00081; Yin, Chen, Xuan, Filkov 2021, ESEC/FSE, doi:10.1145/3468264.3468563. Credit as CC BY requires; the only change is aggregation (counts per pseudonym per month).
- **Files.** `commits_2021_update.zip` (156,231,855 bytes, md5 `952ec9c66f1c2a96ddf3deab2e78f9e9`, sha256 `143dab8e9ef184b62b505615906578022118665b0f6dc9d7de36cc5df021ce8c`) and `emails_2021_update.zip` (1,041,656,466 bytes, md5 `ac716c35e7f160178e83ea9ae40fd4be`, sha256 `3be525e64893256bfab8128bc889c5e9829de1e1cfe16ef7602b6457dfc7b5fb`); md5s match the Zenodo record. Streamed from the archives; nothing is extracted to disk; git-ignored under `sim/data/apache-incubator/`.
- **The build reproduces 117's counts.** 12,608,575 commit rows from 265 projects (117: 12,608,575; 265) and 2,161,558 messages from 274 projects (117: 2,161,558; 274), once 562 and 7 short CSV records are set aside (they have fewer fields than the header and cannot be assigned to a project). The commit file is one row per file touched; rows are grouped by revision into 356,810 distinct commits.
- **Labels.** The Zenodo record has no label file (L4628). Labels come from the ASF's own `podlings.xml` (`https://incubator.apache.org/podlings.xml`, fetched 2026-11-01, sha256 `98f0b33016c850b6ee9fdb6d623c20c4116fefd5f1619ab35dcf2c152ffcb541`, 253,042 bytes; licensed to the ASF under the Apache License 2.0 in its header): status (graduated, retired, current), start date and end date per podling. Only those attributes are read. 269 of the 275 project names in the files match a podling; the 6 that do not (ant, avalon, bookkeeper, commons, pubscribe, struts) have no podling of that name in the file (old top-level projects that were never podlings, and `pubscribe`) and are left out; two names were matched by an explicit alias table (`empire` is Empire-db, `openoffice` is OpenOffice.org). All 269 matched projects are resolved by the data end, so a later cut-off for the labels changes nothing: **205 graduated and 64 retired**: the MSR paper's 269 labelled projects (L4628), and against the APEX paper's 273 = 211 + 62 (L4630) six fewer graduated and two more retired (the labels of those papers are not on the Zenodo record, so the difference is not explained).
- **Time.** Month 0 is the podling's start month. The exit month (graduation or retirement) has quartiles 12, 17, 27 for graduated and 22, 30, 46 for retired podlings. The files cover the incubation only: 1.6% of events fall after the exit month. The last month with any activity is the exit month itself for 203/205 graduated and 59/64 retired projects: the exit process (votes, resolutions, retirement threads) plausibly accounts for some of that mail (the messages were not read), so the last month may be contaminated by the outcome; the early-warning windows stop before it (section 5.3).
- **Coverage.** The commit file starts on 2005-01-30 and the mail file on 2003-04-01 (L4624, L4625). Of the 207 podlings at risk at month 12, 9 (5 graduated, 4 retired) started before February 2005, so some or all of their first-year commits are missing (median regular committers 0, against 4 for the rest; 2 also started before the mail file). Without them: size AUC 0.753, shape gain -0.005 (p = 0.30), interaction p < 0.001; the development-list lead +0.035 (p = 0.010). Nothing turns on them.
- **Era.** Outcomes by start year of the podling (graduated / retired): 2003-2008: 55 / 23; 2009-2011: 50 / 11; 2012-2014: 43 / 12; 2015-2018: 52 / 18; 2019-2021: 5 / 0. The Incubator's practice changed over these years, and magnitudes here are era-bound (`models/00-v0.md` 0.6); section 7 splits at 2012 and adds the start year as a control.
- **Pseudonyms and robots.** 49,373 addresses become project-local integers (a one-way hash with a per-build random salt that is never stored, then relabelled by first appearance); 893 are flagged as automated (JIRA, GitHub and CI relays, commit-notification senders and the like, by address or display-name pattern, and 1 by a behavioural relay rule). They carry 4% of commit events but 43% of the messages on human lists: most "dev" traffic in this dataset is tracker mail. Human lists are every list except commits, issues, notifications, reviews and the like (`HUMAN_LIST_RULE`).
- **Privacy.** The raw files carry names and addresses (L4623). They were read once, as a stream. The derived arrays hold integers only (`derived/*.npz`, `meta.json`: project and list names, counts); no name, address or text is in the repo, this file or the tests' output (a test scans this file for the at-sign of an address).

## 2. Method

- **Unit and landmark.** A podling is at risk at month W if it is still in the Incubator then (exit month >= W). Features come from months 0 to W-1 only, so nothing from the exit leaks in. Primary W = 12: 207 podlings at risk (155 graduated, 52 retired); the 62 that exit earlier are in the survival form (section 6).
- **Activity.** An *event* is a distinct commit or a message on a human list sent by a non-automated pseudonym. A *regular member* is active (at least one event) in at least a quarter of the window's months (3 of 12). The shape block needs at least 3 regular members (6 podlings have fewer). Median n = 20 (quartiles 12 and 39); with the looser *any-event* rule the median is 56, a crowd rather than a team.
- **Shape and mean.** From the per-member totals a_i in the window: n; mean = T/n; the Gini coefficient rescaled by n/(n-1); the top-1 and top-3 shares; the entropy of the shares over ln n. Variations add the effective number, Theil, the coefficient of variation, the share of one-event members, and the profile of the five largest shares.
- **Models and scores.** Ridge logistic regression (penalty 1 on standardised inputs; intercept free), five-fold stratified cross-validation repeated 20 times, predictions averaged over repeats, AUC of the out-of-fold predictions for *graduation*. Intervals are percentile bootstraps of those fixed predictions (positives and negatives resampled separately); the standard error of Hanley and McNeil gives the scale for variants. The survival form and the member panel hold out whole podlings.
- **The nulls.** (1) *Shape adds nothing given size and mean*: the shape rows are permuted across podlings (500 times), which keeps the penalty for carrying useless columns; p is the share of permuted gains at least the observed one. A free permutation also breaks the shape-size correlation that the hypothesis keeps (top-k shares fall with n, the Gini rises with it), so its null is not quite the hypothesis's; the p from permuting within size quintiles, which keeps most of that correlation, is shown beside it (for the primary the two nulls' mean gains are -0.0092 and -0.0078), as is a nested likelihood-ratio test. (2) *Members are interchangeable*: the same events spread by chance over the same number of members give a Gini of 0.08 (median); the observed median is 0.63, so activity is far more concentrated than chance, as in every contribution system. (3) *Early warning*: the retired against graduated contrast, a within-project comparison against the same project's earlier windows, and a simulation of a true slowing down for power. (4) *Coupling*: the held-out gain of D2 over D1, with the cluster bootstrap over podlings. (5) *Critical mass*: step against smooth, on held-out log-loss.
- **Pre-specified, and what was looked at first.** Fixed before any outcome relation was computed: the unit and landmark, the activity measure, the human-list rule, the robot patterns, the shape block, the model and scoring, the decision rules (gain > 0 with permutation p < 0.05; Gini against mean by the paired bootstrap; shape-by-size interaction p < 0.05; early warning by the one-sided Mann-Whitney test on monthly series, 6-month windows, 12 windows, lag 1; growth by Fisher's test; D2 by a gain above 0.01 AUC; step against smooth). Descriptive looks that came first and did not involve the outcome relation: the list inventory, the label counts and exit-month distribution, the lag between the last activity and the exit, the robot-share and the top senders' behaviour. **Two changes after a first look.** (i) A first run at W = 12 used *any event* as the member rule; its median n was 56, a crowd, so the member rule became "regular" (3 of 12 months). The same printout showed raw AUCs, so this change was not outcome-blind; the any-event rule is reported in full in section 7 (gain -0.005, permutation p = 0.31), and gives the same answer. (ii) The first build flagged robots by address only; after seeing that its top senders were relays it gained display-name patterns and the relay rule (no outcome involved). The monthly early-warning grid (eight configurations) was explored before the (6, 12, lag 1) design was named primary, and the weekly series (four configurations) was added after the monthly power simulation showed that the monthly test had no power, so their p-values are descriptive, not confirmatory. The survival form, the step-against-smooth comparison and the D1/D2 panel were each run once in exploration (same code, fewer resamples) before this run; after seeing those runs the code gained the detrending option, the weekly series, the era split and the robustness checks of the size interaction, and nothing in the definitions was changed. The conversation lead of section 7.4 came out of the variation grid of section 7.2, which is a search, and was then re-examined (windows, eras, robots) on the same data. Added at review (2026-11-01), after every result here had been seen, and so checks rather than tests: the permutation within size quintiles, the one-term split of the size interaction, the paired comparison of model forms with size alone, the coverage check of section 1, the lead by size half, and the counting of each distinct test once in the corrections.

## 3. Does the distribution beat the mean? (question 1)

Primary specification: W = 12, events, robots dropped, regular members, n >= 3: 201 podlings (154 graduated, 47 retired); 6 with fewer than 3 regular members are left out (5 of them retired).

**Single features, held out** (the sign is learned in the training folds; "raw AUC" fixes the orientation, above 0.5 meaning a higher value goes with graduation):

| feature | held-out AUC for graduation [95%] | raw AUC |
|---|---|---|
| size ln n | 0.758 [0.681, 0.828] | 0.769 |
| mean ln(T/n) | 0.580 [0.476, 0.678] | 0.599 |
| total ln T | 0.725 [0.639, 0.800] | 0.731 |
| shape gini | 0.592 [0.489, 0.697] | 0.600 |
| shape top1 | 0.631 [0.536, 0.723] | 0.357 |
| shape top3 | 0.668 [0.573, 0.755] | 0.321 |
| shape entropy | 0.397 [0.298, 0.501] | 0.467 |

**Models, held out:**

| model | AUC [95%] | log-loss |
|---|---|---|
| size + mean | 0.754 [0.678, 0.825] | 0.469 |
| size + mean + shape | 0.754 [0.681, 0.823] | 0.476 |
| shape only | 0.740 [0.667, 0.812] | 0.488 |
| mean only | 0.580 [0.480, 0.680] | 0.547 |

- *Gain from adding the shape block to size and mean:* -0.0003 AUC (paired bootstrap -0.0174 to +0.0173); permutation p = 0.17 (the permuted gains average -0.0092, 95th percentile +0.0100); permuted within size quintiles p = 0.18; likelihood-ratio statistic 5.29 on 4 df, p = 0.26. **Decision rule: not met.**
- *Gini against mean, the pre-specified single comparison:* held-out AUC 0.592 against 0.580; paired difference +0.012 (-0.085 to +0.107). **Not met.** The best of the four shape features (`top3`) differs from the mean by +0.088 (-0.045 to +0.231); it was picked as the best of four on the same predictions, so that figure is biased upward.
- *Shape alone against mean alone, as models:* +0.160 (+0.056 to +0.264). Shape "beats" the mean in this narrow sense, but the shape measures carry n (top-k share and Gini move with it; section 4), and once size is in the model they add nothing.
- *Standardised coefficients of the full ridge model:* ln_n +1.37, ln_mean -0.12, gini -0.02, top1 -0.41, top3 +0.58, entropy -0.09. Size carries the signal.

**Reading for Claim 1.** Claim 1 is about the *threshold* distribution of a cascade law: no summary of it fixes the equilibrium (L1225, L1831). Activity is not thresholds. This test asks the weaker, measurable question whether the distribution of *engagement* carries outcome information the mean does not, once the group's size is known, and on these 201 podlings, for commits plus messages, it does not. For the conversation alone it may (section 7.4). That is not a refutation or a support of Claim 1 (thresholds are unobserved here): the engagement shape is not a free predictor of success, and where it is one, the measure matters.

## 4. What changes with n (question 2)

n is the number of regular members in the first year. Size ranges follow the scales of v0 (a team is 8 to 12). Graduation rate with a 95% Wilson interval, and the raw (in-sample) AUC of each quantity for graduation *within* the band, with a bootstrap interval, where the band has at least 5 of each outcome. 4 podlings with no regular member at all (3 of them retired) belong to no band:

| n | podlings | graduated / retired | graduation rate [95%] | median events per member | median Gini | AUC of Gini | AUC of mean | AUC of total |
|---|---|---|---|---|---|---|---|---|
| 1-4 | 4 | 1 / 3 | 25% [5%, 70%] | 27 | - | - | - | - |
| 5-7 | 17 | 9 / 8 | 53% [31%, 74%] | 28 | 0.50 | 0.22 [0.01, 0.47] | 0.33 [0.08, 0.62] | 0.36 [0.11, 0.65] |
| 8-12 | 31 | 17 / 14 | 55% [38%, 71%] | 37 | 0.55 | 0.50 [0.27, 0.72] | 0.56 [0.35, 0.77] | 0.60 [0.37, 0.79] |
| 13-25 | 69 | 51 / 18 | 74% [62%, 83%] | 51 | 0.63 | 0.66 [0.50, 0.81] | 0.57 [0.39, 0.74] | 0.56 [0.39, 0.74] |
| 26+ | 82 | 76 / 6 | 93% [85%, 97%] | 57 | 0.65 | 0.81 [0.64, 0.94] | 0.54 [0.33, 0.75] | 0.70 [0.51, 0.83] |

- *Size is linked to concentration and to the mean:* Spearman rho between n and the Gini = +0.30 (p < 0.001); between n and events per member = +0.27. Larger projects are more concentrated and busier per member, which is why a shape-only model looks good and a size-aware one does not need it.
- *The shape-by-size interaction (pre-specified):* adding Gini x ln n and mean x ln n to {ln n, ln mean, Gini} improves the likelihood by 15.9 on 2 df, p < 0.001 (parametric bootstrap under the main-effects model, 1,000 draws: p = 0.0020; with the Gini replaced by its rank p = 0.002; with ln T as the moderator p = 0.018). The 2-df test also holds mean x ln n; taken one at a time, each given the other, Gini x ln n gives 13.7 on 1 df (p < 0.001) and mean x ln n 0.9 (p = 0.35), so the concentration term carries it. Standardised coefficients: ln_n -3.16, ln_mean +0.78, gini -3.55, gini x ln_n +9.08, ln_mean x ln_n -2.60. Split at the median size (20; a post hoc split): at or below it the Gini coefficient is -0.05 (standardised, ridge) with raw AUC 0.51 (104 podlings); above it +0.79 with AUC 0.73 (97 podlings). In the larger projects a concentrated core goes with graduation; in the smaller ones concentration is uninformative. This is the form of L5779 (the sign of a group-size effect depends on a return) and L5740 (stability depends on turnover and size): a *sign flag that is a setting operand*, as `models/00-v0.md` 0.6 rule 5 already requires, here with n as the moderator. The mechanism is not in the data. Part of the weaker association at small n may be estimation noise (a Gini from five members is a noisy measure of concentration, which attenuates an effect rather than reversing it); attenuation alone would not give the reversal in the 5 to 7 band, but that band holds 17 podlings (9 / 8), its interval reaches 0.47, and it is one of 12 within-band AUCs, so chance is not excluded.
- *Shape gain within the small half (post hoc):* 104 podlings, 38 retired; AUC 0.602 for size + mean and 0.592 with shape: gain -0.010, permutation p = 0.34.
- *Shape gain within the large half (post hoc):* 97 podlings, 9 retired; AUC 0.717 for size + mean and 0.740 with shape: gain +0.023, permutation p = 0.20.
- *With the looser any-event rule* (members = anyone who posted or committed once, a crowd): the interaction p = 0.17, graduation rate by band 5-7: 0%, 8-12: 25%, 13-25: 52%, 26+: 82%.
- *The team band.* At 8 to 12 regular members the graduation rate is 55% (17/31), and at 5 to 7 it is 53% (9/17): retirement is about as likely as graduation. In the 8 to 12 band the Gini has AUC 0.50 (0.27 to 0.72), the mean 0.56, the total 0.60: none separates the outcomes there. The within-band Gini intervals exclude 0.5 in: 5-7 (AUC 0.22), 26+ (AUC 0.81). A reversal of sign from the smallest bands to the largest is what the interaction says; the bands with an AUC hold 6 to 18 retired podlings each, so it is a pattern to test, not a result.

## 5. Cascade and escalation analogues (question 3)

### 5.1 Sustained growth against decline, over the first year

The log ratio of events in months 6 to 11 to those in months 0 to 5 (each plus one). Growth is a ratio of at least 1.5, decline of at most 2/3 (`growth_cut`, fixed in advance).

| first-year trajectory | podlings | graduated / retired | graduation rate |
|---|---|---|---|
| growth | 77 | 66 / 11 | 86% |
| steady | 91 | 68 / 23 | 75% |
| decline | 39 | 21 / 18 | 54% |

Growth against decline: Fisher p < 0.001; the log ratio as a single predictor has AUC 0.66 for graduation. **Met.** It adds little once size is known (0.768 for size + growth against 0.758 for size), plausibly because growing projects are the ones that recruit.

### 5.2 The whole pre-exit series (retrospective, not a predictor)

Rolling six-month mean of events, last month dropped (the exit's own mail). *Ended at peak*: the final rolling mean is at least 80% of its maximum; *decayed*: at most 50%; *collapsed*: at most 20% of the maximum for the last six months; *in between*: otherwise.

| trajectory | podlings | graduated / retired |
|---|---|---|
| ended at peak | 99 | 96 / 3 |
| in between | 31 | 29 / 2 |
| decayed | 47 | 26 / 21 |
| collapsed | 30 | 4 / 26 |

81% of the graduated projects ended at or near their peak (or in between), and 90% of the retired ones decayed or collapsed; collapse alone is 26 of the 30 collapsed projects retiring. That is a description of the series in hindsight, and the exit is partly the reason for it.

### 5.3 Early-warning signals before retirement

Series: ln(1 + events) per month. Rolling window w, linear detrending inside the window (or only mean removal), lag-1 autocorrelation (AR1) and standard deviation (SD) per window; Kendall's tau of each against time over the L windows before the reference month. The series used ends at the month *before* the reference month, and the reference month is the exit month minus *lag*: lag 0 drops the exit month (the exit's own mail), lag 1 also the month before it, lag 3 the three before that. Retired podlings are the "transition" cases; graduated ones are the contrast (graduation is also an exit, and not a fold bifurcation). AUC is for *retired* (a higher tau means retired); the alarm share counts tau > 0.5; p is one-sided Mann-Whitney.

| w | L | lag | detrend | podlings (retired / graduated) | AR1: AUC [95%], p, alarm retired / graduated | SD: AUC [95%], p, alarm retired / graduated | level trend: AUC for retired |
|---|---|---|---|---|---|---|---|
| 6m | 12m | 1 | linear | 145 (50 / 95) | 0.52 [0.43, 0.62], 0.33, 8% / 9% | 0.58 [0.48, 0.67], 0.060, 21% / 14% | 0.30 |
| 6m | 12m | 0 | linear | 159 (51 / 108) | 0.51 [0.41, 0.61], 0.39, 8% / 8% | 0.59 [0.49, 0.69], 0.042, 14% / 11% | 0.28 |
| 6m | 12m | 3 | linear | 132 (49 / 83) | 0.55 [0.45, 0.65], 0.17, 12% / 6% | 0.50 [0.39, 0.61], 0.47, 16% / 17% | 0.31 |
| 6m | 18m | 1 | linear | 100 (43 / 57) | 0.53 [0.41, 0.65], 0.30, 7% / 4% | 0.50 [0.38, 0.62], 0.48, 12% / 9% | 0.29 |
| 9m | 18m | 1 | linear | 91 (38 / 53) | 0.51 [0.39, 0.63], 0.45, 11% / 8% | 0.56 [0.43, 0.69], 0.19, 18% / 13% | 0.28 |
| 12m | 24m | 1 | linear | 53 (27 / 26) | 0.46 [0.31, 0.63], 0.68, 0% / 4% | 0.60 [0.44, 0.76], 0.10, 30% / 15% | 0.27 |
| 6m | 12m | 1 | mean | 145 (50 / 95) | 0.51 [0.41, 0.61], 0.42, 17% / 9% | 0.57 [0.47, 0.66], 0.099, 12% / 13% | 0.30 |
| 9m | 18m | 1 | mean | 91 (38 / 53) | 0.47 [0.36, 0.59], 0.67, 5% / 11% | 0.53 [0.40, 0.65], 0.31, 16% / 6% | 0.28 |
| 26w | 52w | 0 | linear | 145 (50 / 95) | 0.43 [0.33, 0.53], 0.92, 6% / 8% | 0.45 [0.36, 0.55], 0.83, 6% / 13% | 0.29 |
| 26w | 52w | 4 | linear | 138 (50 / 88) | 0.45 [0.34, 0.55], 0.84, 8% / 8% | 0.47 [0.37, 0.58], 0.69, 6% / 11% | 0.29 |
| 26w | 52w | 8 | linear | 132 (49 / 83) | 0.44 [0.33, 0.55], 0.88, 10% / 8% | 0.46 [0.36, 0.56], 0.78, 6% / 11% | 0.30 |
| 13w | 26w | 4 | linear | 230 (56 / 174) | 0.51 [0.42, 0.60], 0.41, 11% / 10% | 0.53 [0.44, 0.61], 0.29, 13% / 10% | 0.34 |

- The rows with *m* are monthly series, the rows with *w* weekly series (a variation added after the power check below). The primary monthly design is the first row (w = 6, L = 12, lag 1). **Autocorrelation: not met; variance: not met** (one-sided Mann-Whitney p < 0.05). Over all 12 configurations, 0 reach p < 0.05 for autocorrelation and 1 for variance; 24 tests were run, so 1.2 such values are expected by chance, and the grid was explored before the primary was named.
- Alarms at tau > 0.5 are about as common among graduated projects as among retired ones: the poor specificity of Helmich et al. 2023 (L0547, L3057: rising autocorrelation before 89% of transitions and before 62.5% of non-transitions) appears here as low sensitivity together with no separation.
- The *level* trend, which is the growth-or-collapse signal, separates the groups strongly and in the expected direction (last column: AUC for retired far below 0.5, so graduated projects trend up). Slowing-down statistics are built to be independent of such a drift; here the drift is the information and the slowing-down statistics are not.

**Within-project time-matched comparison** (monthly, w = 6, L = 12; weekly, w = 26, L = 52). For each project, where does the pre-exit tau sit among the taus at every earlier reference month whose window does not overlap? u is the share of those earlier taus below the observed one (0.5 under no signal). Only podlings with at least 5 non-overlapping earlier references qualify (long series).

| design | group | indicator | podlings | mean u | Wilcoxon p (two-sided) | Holm p (over these rows) |
|---|---|---|---|---|---|---|
| w=6m, L=12m, lag 1 | retired | AR1 | 27 | 0.475 | 0.64 | 1.00 |
| w=6m, L=12m, lag 1 | retired | SD | 27 | 0.433 | 0.32 | 1.00 |
| w=6m, L=12m, lag 1 | graduated | AR1 | 29 | 0.602 | 0.12 | 1.00 |
| w=6m, L=12m, lag 1 | graduated | SD | 29 | 0.427 | 0.15 | 1.00 |
| w=6m, L=12m, lag 0 | retired | AR1 | 29 | 0.465 | 0.56 | 1.00 |
| w=6m, L=12m, lag 0 | retired | SD | 29 | 0.437 | 0.32 | 1.00 |
| w=6m, L=12m, lag 0 | graduated | AR1 | 31 | 0.581 | 0.17 | 1.00 |
| w=6m, L=12m, lag 0 | graduated | SD | 31 | 0.469 | 0.50 | 1.00 |
| w=26w, L=52w, lag 0 | retired | AR1 | 31 | 0.435 | 0.36 | 1.00 |
| w=26w, L=52w, lag 0 | retired | SD | 31 | 0.361 | 0.035 | 0.56 |
| w=26w, L=52w, lag 0 | graduated | AR1 | 40 | 0.507 | 0.78 | 1.00 |
| w=26w, L=52w, lag 0 | graduated | SD | 40 | 0.530 | 0.58 | 1.00 |
| w=26w, L=52w, lag 4 | retired | AR1 | 31 | 0.455 | 0.58 | 1.00 |
| w=26w, L=52w, lag 4 | retired | SD | 31 | 0.388 | 0.088 | 1.00 |
| w=26w, L=52w, lag 4 | graduated | AR1 | 36 | 0.483 | 0.78 | 1.00 |
| w=26w, L=52w, lag 4 | graduated | SD | 36 | 0.517 | 0.62 | 1.00 |

**Power: could these tests have seen a true slowing down?** Simulated AR(1) series whose coefficient rises from 0.3 to 0.9 over the last L + w points, against constant 0.3, passed through the same windows, detrending and Kendall statistic (noise sd fixed, so the variance rises too). AUC for telling them apart, and the share above tau 0.5 in each:

| series | w | L | detrend | AUC (AR1) | AUC (SD) | alarm AR1: slowing / flat | alarm SD: slowing / flat |
|---|---|---|---|---|---|---|---|
| months | 6 | 12 | linear | 0.55 | 0.43 | 6% / 7% | 8% / 12% |
| months | 6 | 12 | mean | 0.59 | 0.50 | 12% / 10% | 16% / 15% |
| months | 9 | 18 | linear | 0.61 | 0.48 | 14% / 8% | 8% / 16% |
| months | 9 | 18 | mean | 0.65 | 0.55 | 18% / 9% | 16% / 17% |
| months | 12 | 24 | linear | 0.58 | 0.51 | 16% / 10% | 11% / 14% |
| months | 12 | 24 | mean | 0.62 | 0.56 | 21% / 12% | 18% / 16% |
| weeks | 26 | 52 | linear | 0.72 | 0.60 | 34% / 12% | 20% / 13% |
| weeks | 26 | 52 | mean | 0.76 | 0.66 | 41% / 14% | 32% / 14% |
| weeks | 13 | 26 | linear | 0.59 | 0.46 | 15% / 12% | 10% / 16% |

At the monthly series lengths this dataset allows (a podling lives 17 to 30 months at the median) the statistics barely separate a true critical slowing down from none (AUC 0.55 for autocorrelation, 0.43 for variance at 6 and 12), with either detrending, so the monthly null says nothing. At weekly resolution (26-week windows, 52 windows) the same simulated signal is caught with AUC 0.72 (autocorrelation) and 0.60 (variance), and there the data give 0.43 (0.33 to 0.53) and 0.45 (0.36 to 0.55) for retired against graduated: the upper ends are far below the simulated strength. A slowing down as strong as that one (the lag-1 coefficient rising from 0.3 to 0.9 in the year before the exit) is therefore not there; a weaker one cannot be excluded, and the retirement date is administrative, so the reference point is blurred. Pull-request latency or issue turnaround, which have a recovery time built in, would be a better series than counts.
Within the retired projects' own histories (weekly, lag 0; 31 long series) the variance trend before the exit sits at 0.36 of the project's earlier windows (Wilcoxon p = 0.035, nominal: the weekly design came after the power check, and over the 16 within-project rows above Holm gives 0.56). If real, variance falls before retirement, as it does when activity decays towards zero: the opposite of critical slowing down.

### 5.4 A critical mass: step against smooth

The group-level analogue of an ignition point (Claim 1.4): does the graduation probability jump at a threshold in early size? The step model chooses its cut on the training folds from the 10th to 90th percentile of ln n; the smooth model is a logistic in ln n. Held-out log-loss: base rate 0.544, smooth 0.464, step 0.499; AUC 0.758 against 0.692. The best cut on all the data is 39 regular members (69% graduate below, 96% above; 148 and 53 podlings). On total activity ln T the two are tied (0.496 against 0.494). **Smooth preferred.** There is no ignition point to find in this sample: more regular members means more graduation, steadily.

### 5.5 Individual dynamics (D1) against coupling (D2), for who stays active

A member-month panel: 235,625 rows from 257 podlings; a member is eligible once active in two distinct months, the outcome is activity in the next month (base rate 26%), whole podlings are held out. **D1** is her own state: active now, last month and the month before, the share of her months since her first that were active (her set point), her tenure and her volume now. **D2** adds the share of the *other* eligible members active now and last month and their volume now.

| model | AUC | log-loss |
|---|---|---|
| D1 | 0.8954 | 0.3462 |
| D1 + D2 | 0.8961 | 0.3454 |
| D1 + D2 + s^2 | 0.8971 | 0.3444 |

D2 gain: +0.0007 AUC (+0.0002 to +0.0012; cluster bootstrap over podlings), log-loss +0.0009. Quadratic term: +0.0010 AUC. **D2 adds nothing material** (rule: a gain above 0.01). Standardised coefficients: a0 +0.09, a1 +0.23, a2 +0.36, rate +0.70, tenure +0.32, volume +0.91, s_others +0.15, s_others_lag +0.04, v_others -0.04. The interval excludes 0 because the gain, though tiny, recurs across podlings; it is a thousandth of the AUC. Own volume and own rate dominate.
- small teams (<=10 eligible): 3,396 rows; AUC 0.818 for D1, 0.816 with D2; log-loss change -0.0020.
- larger (>10): 232,229 rows; AUC 0.896 for D1, 0.897 with D2; log-loss change +0.0009.

The response curve (members active next month against the others' active share now, by decile) rises steadily, and the D1-only prediction rises with it almost exactly: the share of others active is mostly the average of the members' own states, which D1 already holds. No knee appears.

| mean share of others active | active next month (observed) | D1-predicted | rows |
|---|---|---|---|
| 0.03 | 0.077 | 0.097 | 23,273 |
| 0.09 | 0.095 | 0.117 | 23,644 |
| 0.15 | 0.149 | 0.161 | 23,629 |
| 0.21 | 0.192 | 0.197 | 22,859 |
| 0.26 | 0.231 | 0.227 | 24,371 |
| 0.31 | 0.269 | 0.262 | 23,537 |
| 0.37 | 0.310 | 0.302 | 22,865 |
| 0.44 | 0.341 | 0.332 | 24,289 |
| 0.53 | 0.421 | 0.404 | 23,427 |
| 0.72 | 0.517 | 0.506 | 23,731 |

Caveat that cuts the other way from the usual one: the others' share is a project-month quantity that all members share, so it is confounded with common shocks (a release, a holiday), which would *inflate* the apparent coupling. That the gain is still negligible makes the null stronger, not weaker. It does not make coupling absent: monthly counts are a coarse channel for what 098 measured per six seconds.

## 6. The survival form: retirement and graduation within the next six months

One row per podling and origin month (every third month from month 6 while still incubating), features from the trailing six months, outcome: retires (or graduates) within the next six months; 1,794 rows from 262 podlings, 119 retirement events in 62 podlings and 384 graduation events in 200. Whole podlings are held out; intervals are cluster bootstraps over podlings. Tenure (ln of the origin month) is in the base because graduates leave early (median 17 months) and retirees late (30).

| outcome within 6 months | tenure + size + mean | + shape | + growth | + shape + growth | shape gain [95%] | growth gain [95%] |
|---|---|---|---|---|---|---|
| retires | 0.792 | 0.800 | 0.794 | 0.802 | +0.008 [-0.008, +0.023] | +0.002 [-0.005, +0.007] |
| graduates | 0.773 | 0.769 | 0.774 | 0.770 | -0.003 [-0.009, +0.002] | +0.001 [-0.003, +0.005] |

The conclusion of section 3 holds in the survival form: the shape of the distribution adds a few thousandths of AUC to the six-month retirement ranking, with an interval that includes zero, and nothing to the graduation ranking. What does the work is tenure, size and the mean (0.79 for retirement, 0.77 for graduation).

## 7. Variations

### 7.1 The primary window under different model forms

Same 201 podlings (154 graduated, 47 retired), same folds; held-out AUC for graduation, its Hanley-McNeil standard error (the uncertainty of that one AUC), log-loss (base rate 0.544), and the AUC minus that of size alone with a paired bootstrap of the fixed predictions: two forms scored on the same podlings differ by far less than either s.e., so a difference is read against the paired interval.

| model form | AUC | s.e. | log-loss | minus size alone [paired 95%] |
|---|---|---|---|---|
| size + Gini + Gini x size | 0.771 | 0.035 | 0.457 | +0.013 [+0.002, +0.024] |
| size + growth | 0.768 | 0.035 | 0.462 | +0.010 [-0.012, +0.033] |
| size + mean + Gini + Gini x size + mean x size | 0.765 | 0.035 | 0.463 | +0.007 [-0.006, +0.021] |
| size + mean + shape + growth | 0.760 | 0.036 | 0.475 | +0.002 [-0.026, +0.029] |
| size + mean + growth | 0.760 | 0.036 | 0.468 | +0.002 [-0.022, +0.026] |
| size (ln n) | 0.758 | 0.036 | 0.464 | - |
| size + mean | 0.754 | 0.036 | 0.469 | -0.004 [-0.011, +0.002] |
| size + mean + shape (primary) | 0.754 | 0.036 | 0.476 | -0.004 [-0.022, +0.014] |
| shape only | 0.740 | 0.037 | 0.488 | -0.018 [-0.045, +0.007] |
| total activity (ln T) | 0.725 | 0.038 | 0.494 | -0.033 [-0.092, +0.021] |
| step on size (cut chosen in training folds) | 0.692 | 0.041 | 0.499 | -0.066 [-0.088, -0.045] |
| mean per member (ln T/n) | 0.580 | 0.046 | 0.547 | -0.178 [-0.283, -0.075] |

**Best fit by held-out AUC: size + Gini + Gini x size** (0.771, against 0.758 for plain size). The forms whose paired interval against size alone lies above zero: size + Gini + Gini x size. They were picked from 12 forms on the same predictions, the interaction forms were added because the size interaction was tested, and the paired intervals hold the predictions fixed (they leave out the variation from refitting), so any such edge is biased upward: it backs the interaction of section 4 and is not a separate finding. The forms without size are total activity (ln T) (0.72), mean per member (ln T/n) (0.58), shape only (0.74): the shape block recovers most of size's signal because its members move with n, and the mean per member has almost none. The step on size is the worst of the size-based forms and is below size alone. By held-out log-loss the three best are size + Gini + Gini x size, size + growth, size + mean + Gini + Gini x size + mean x size.

### 7.2 Window, activity measure, robots, member rule, shape measure, regularisation, dynamics (one factor at a time)

Held-out AUC (10 repeats) for graduation of size, mean, size + mean, size + mean + shape; the shape gain with its permutation p (200 draws) and Holm-adjusted p across the distinct shape-gain tests in this table (a row that repeats the primary's test says so and is counted once; a row whose shape column is constant is no test); the p of the shape-by-size interaction (Gini).

| factor | variant | podlings (retired) | size | mean | size + mean | + shape | gain | perm p | Holm p | interaction p |
|---|---|---|---|---|---|---|---|---|---|---|
| primary | W=12, events, bots dropped, member = active in >= 3 months | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | 1.00 | < 0.001 |
| window | W=3 (member: >= 2 active months) | 236 (50) | 0.679 | 0.613 | 0.677 | 0.652 | -0.026 | 0.79 | 1.00 | 0.22 |
| window | W=6 (member: >= 2 active months) | 253 (57) | 0.782 | 0.586 | 0.776 | 0.771 | -0.005 | 0.29 | 1.00 | 0.020 |
| window | W=9 (member: >= 3 active months) | 234 (52) | 0.762 | 0.563 | 0.758 | 0.764 | +0.007 | 0.100 | 1.00 | 0.004 |
| window | W=12 (member: >= 3 active months) | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | = primary | < 0.001 |
| window | W=18 (member: >= 5 active months) | 139 (45) | 0.724 | 0.553 | 0.714 | 0.742 | +0.028 | 0.026 | 0.78 | 0.007 |
| window | W=24 (member: >= 6 active months) | 96 (40) | 0.706 | 0.538 | 0.685 | 0.712 | +0.027 | 0.076 | 1.00 | 0.017 |
| activity measure | events | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | = primary | < 0.001 |
| activity measure | commits | 133 (22) | 0.630 | 0.477 | 0.626 | 0.611 | -0.015 | 0.31 | 1.00 | 0.13 |
| activity measure | messages | 199 (45) | 0.736 | 0.617 | 0.728 | 0.754 | +0.027 | 0.013 | 0.42 | < 0.001 |
| activity measure | dev_messages | 199 (45) | 0.729 | 0.605 | 0.723 | 0.760 | +0.037 | 0.004 | 0.13 | < 0.001 |
| activity measure | replies | 197 (43) | 0.722 | 0.628 | 0.714 | 0.755 | +0.041 | 0.004 | 0.14 | 0.001 |
| activity measure | files | 133 (22) | 0.630 | 0.475 | 0.627 | 0.602 | -0.025 | 0.44 | 1.00 | 0.11 |
| activity measure | events_all | 201 (47) | 0.761 | 0.580 | 0.754 | 0.754 | -0.000 | 0.19 | 1.00 | < 0.001 |
| bots | flagged robots dropped (primary) | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | = primary | < 0.001 |
| bots | robots kept | 201 (47) | 0.763 | 0.615 | 0.756 | 0.758 | +0.002 | 0.18 | 1.00 | 0.069 |
| bots | robots dropped and the project's single most active pseudonym dropped | 200 (46) | 0.758 | 0.622 | 0.746 | 0.757 | +0.012 | 0.065 | 1.00 | 0.002 |
| member rule | any event (participants) | 204 (50) | 0.783 | 0.575 | 0.778 | 0.778 | -0.000 | 0.21 | 1.00 | 0.17 |
| member rule | active in >= 2 months | 202 (48) | 0.777 | 0.571 | 0.772 | 0.764 | -0.009 | 0.28 | 1.00 | < 0.001 |
| member rule | active in >= 3 months (primary) | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | = primary | < 0.001 |
| member rule | active in >= 6 months (half the window) | 195 (45) | 0.737 | 0.628 | 0.736 | 0.744 | +0.009 | 0.11 | 1.00 | 0.14 |
| member rule | at least 5 events | 201 (47) | 0.759 | 0.569 | 0.750 | 0.741 | -0.009 | 0.41 | 1.00 | < 0.001 |
| shape measure | Gini only | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | +0.000 | 0.25 | 1.00 | < 0.001 |
| shape measure | top-1 share only | 201 (47) | 0.761 | 0.575 | 0.753 | 0.749 | -0.004 | 0.47 | 1.00 | < 0.001 |
| shape measure | top-3 share only | 201 (47) | 0.761 | 0.575 | 0.753 | 0.755 | +0.002 | 0.17 | 1.00 | < 0.001 |
| shape measure | entropy only | 201 (47) | 0.761 | 0.575 | 0.753 | 0.752 | -0.002 | 0.30 | 1.00 | < 0.001 |
| shape measure | effective number only | 201 (47) | 0.761 | 0.575 | 0.753 | 0.752 | -0.002 | 0.40 | 1.00 | < 0.001 |
| shape measure | Theil only | 201 (47) | 0.761 | 0.575 | 0.753 | 0.757 | +0.004 | 0.13 | 1.00 | < 0.001 |
| shape measure | coefficient of variation only | 201 (47) | 0.761 | 0.575 | 0.753 | 0.755 | +0.002 | 0.17 | 1.00 | < 0.001 |
| shape measure | share of one-event members only | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | +0.000 | 1.00 | constant | < 0.001 |
| shape measure | all four (primary) | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | = primary | < 0.001 |
| shape measure | profile of the five largest shares | 201 (47) | 0.761 | 0.575 | 0.753 | 0.754 | +0.001 | 0.11 | 1.00 | < 0.001 |
| shape measure | profile of the five largest shares + effective number | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.13 | 1.00 | < 0.001 |
| regularisation | ridge l2 = 0.01 | 201 (47) | 0.761 | 0.575 | 0.753 | 0.744 | -0.010 | 0.35 | 1.00 | < 0.001 |
| regularisation | ridge l2 = 0.1 | 201 (47) | 0.760 | 0.575 | 0.753 | 0.746 | -0.007 | 0.29 | 1.00 | < 0.001 |
| regularisation | ridge l2 = 1.0 | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | = primary | < 0.001 |
| regularisation | ridge l2 = 10.0 | 201 (47) | 0.761 | 0.575 | 0.755 | 0.751 | -0.004 | 0.25 | 1.00 | < 0.001 |
| era | podlings started 2003-2012 | 110 (26) | 0.755 | 0.688 | 0.754 | 0.748 | -0.005 | 0.23 | 1.00 | < 0.001 |
| era | podlings started 2013-2021 | 91 (21) | 0.754 | 0.479 | 0.755 | 0.757 | +0.002 | 0.19 | 1.00 | 0.003 |
| era | start year added to size and mean | 201 (47) | 0.761 | 0.575 | 0.746 | 0.747 | +0.001 | 0.14 | 1.00 | < 0.001 |
| dynamics | adds growth over the window (second half against first) | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | = primary | < 0.001 |
| dynamics | adds growth and monthly variability | 201 (47) | 0.761 | 0.575 | 0.753 | 0.753 | -0.000 | 0.17 | = primary | < 0.001 |

- *Shape gain across the grid:* 42 rows hold 33 distinct tests (the primary's own test recurs in 9 rows and is counted once; 1 row has a constant shape column: the one-event share is 0 for every regular member, who has at least 3 events). 4 have a raw permutation p below 0.05 (0 after Holm; p-values under 0.06 were re-run with 2,000 permutations). The largest gains are +0.041 (activity measure: replies); +0.037 (activity measure: dev_messages); +0.028 (window: W=18 (member: >= 5 active months)). The median gain is -0.000. With 33 correlated tests a few nominal p-values below 0.05 are expected by chance; the variants with a nominal gain are the three message-based measures and the 18-month window, which section 7.4 follows up; none of them survives the Holm correction over this grid.
- *Dynamics:* the two dynamics rows repeat the primary's shape test; their own result is the held-out AUC with the term added to size and mean: adds growth over the window (second half against first): 0.759 (with the shape block too, 0.762); adds growth and monthly variability: 0.766 (with the shape block too, 0.765), against 0.753 for size and mean alone.
- *The shape-by-size interaction:* p < 0.05 in 14 of the 20 distinct tables (23 of the 42 rows use the primary's table, and the shape measures, the penalty and the added terms do not enter this unpenalised test). It is absent (p >= 0.05) for: window: W=3 (member: >= 2 active months); activity measure: commits; activity measure: files; bots: robots kept; member rule: any event (participants); member rule: active in >= 6 months (half the window). These are the commit-only measures (few podlings have three regular committers), the shortest window, the two extreme member rules (anyone, and half the window's months) and the variant with robots kept.
- *Which variant fits best:* by size + mean, `member rule: any event (participants)` (0.778); by size + mean + shape, `member rule: any event (participants)` (0.778). In no row does size + mean or size + mean + shape beat size alone by more than 0.033 AUC: the number of people active early is the predictor, however it is counted. The best window for size is `W=6 (member: >= 2 active months)` (0.782); later windows keep only the longer-lived podlings and fall in AUC.
- *Era (drift):* size AUC 0.755 for podlings started 2003-2012 (110 podlings, 26 retired) and 0.754 for those started 2013-2021 (91, 21); shape gain -0.005 and +0.002; with the start year added to size and mean the AUC goes from 0.753 to 0.746 and the shape gain is +0.001. The size effect and the absence of a shape effect hold in both eras.

### 7.3 The any-event (crowd) reading of question 1

With every pseudonym who did anything counted as a member (204 podlings, 50 retired): size AUC 0.783, mean 0.574, Gini 0.634; shape gain -0.005 (permutation p = 0.31); likelihood ratio p = 0.50. The same answer.

### 7.4 A lead: the concentration of conversation

In the grid of 7.2 the three measures that count list messages only (all human lists, the development list, replies) show a larger shape gain than the combined measure, which adds commits. This is the one place where the distribution of activity beats its mean. It is a **lead, not a result**: it came out of a search over 42 variants, and the table below re-examines it on the same data, so its p-values are descriptive. Held-out AUC for graduation, 10 repeats; permutation p from 300 draws (so 0.003 is the floor), free and within size quintiles (the second keeps the shape-size correlation, section 2):

| measure | variant | podlings (retired) | size | size + mean | + shape | gain | perm p | perm p within size quintiles |
|---|---|---|---|---|---|---|---|---|
| messages | W=6 | 252 (57) | 0.777 | 0.774 | 0.781 | +0.007 | 0.043 | 0.037 |
| messages | W=9 | 231 (50) | 0.737 | 0.729 | 0.776 | +0.047 | 0.003 | 0.003 |
| messages | W=12 | 199 (45) | 0.736 | 0.728 | 0.754 | +0.027 | 0.020 | 0.013 |
| messages | W=18 | 137 (43) | 0.668 | 0.654 | 0.737 | +0.083 | 0.003 | 0.007 |
| messages | started 2003-2012 | 109 (25) | 0.742 | 0.748 | 0.724 | -0.023 | 0.38 | 0.53 |
| messages | started 2013-2021 | 90 (20) | 0.705 | 0.688 | 0.753 | +0.065 | 0.030 | 0.013 |
| messages | robots kept | 200 (46) | 0.738 | 0.742 | 0.733 | -0.008 | 0.32 | 0.30 |
| messages | robots and the most active pseudonym dropped | 198 (45) | 0.737 | 0.733 | 0.743 | +0.010 | 0.050 | 0.056 |
| dev_messages | W=6 | 251 (57) | 0.764 | 0.756 | 0.765 | +0.010 | 0.040 | 0.060 |
| dev_messages | W=9 | 231 (50) | 0.722 | 0.713 | 0.769 | +0.057 | 0.003 | 0.003 |
| dev_messages | W=12 | 199 (45) | 0.729 | 0.723 | 0.760 | +0.037 | 0.007 | 0.017 |
| dev_messages | W=18 | 137 (43) | 0.651 | 0.631 | 0.728 | +0.096 | 0.003 | 0.003 |
| dev_messages | started 2003-2012 | 109 (25) | 0.738 | 0.736 | 0.719 | -0.017 | 0.31 | 0.67 |
| dev_messages | started 2013-2021 | 90 (20) | 0.688 | 0.681 | 0.760 | +0.079 | 0.013 | 0.010 |
| dev_messages | robots kept | 200 (46) | 0.729 | 0.732 | 0.731 | -0.001 | 0.19 | 0.14 |
| dev_messages | robots and the most active pseudonym dropped | 198 (45) | 0.730 | 0.732 | 0.744 | +0.012 | 0.027 | 0.033 |
| replies | W=6 | 249 (56) | 0.779 | 0.775 | 0.778 | +0.003 | 0.18 | 0.100 |
| replies | W=9 | 226 (47) | 0.724 | 0.718 | 0.766 | +0.048 | 0.003 | 0.003 |
| replies | W=12 | 197 (43) | 0.722 | 0.714 | 0.755 | +0.041 | 0.007 | 0.003 |
| replies | W=18 | 134 (42) | 0.681 | 0.671 | 0.761 | +0.091 | 0.003 | 0.003 |
| replies | started 2003-2012 | 108 (24) | 0.740 | 0.737 | 0.736 | -0.001 | 0.17 | 0.12 |
| replies | started 2013-2021 | 89 (19) | 0.683 | 0.670 | 0.724 | +0.054 | 0.047 | 0.030 |
| replies | robots kept | 200 (46) | 0.743 | 0.739 | 0.732 | -0.006 | 0.28 | 0.33 |
| replies | robots and the most active pseudonym dropped | 195 (43) | 0.729 | 0.728 | 0.752 | +0.024 | 0.020 | 0.023 |

The Gini alone against the mean alone (held out; paired bootstrap of the difference):

| measure | window | podlings (retired) | Gini | mean | size | Gini minus mean [95%] | raw AUC of the Gini |
|---|---|---|---|---|---|---|---|
| messages | 12 | 199 (45) | 0.712 | 0.617 | 0.736 | +0.096 [+0.013, +0.178] | 0.717 |
| messages | 18 | 137 (43) | 0.708 | 0.554 | 0.668 | +0.154 [+0.055, +0.266] | 0.712 |
| dev_messages | 12 | 199 (45) | 0.718 | 0.605 | 0.729 | +0.112 [+0.032, +0.193] | 0.723 |
| dev_messages | 18 | 137 (43) | 0.706 | 0.546 | 0.651 | +0.160 [+0.055, +0.268] | 0.714 |
| replies | 12 | 197 (43) | 0.731 | 0.628 | 0.722 | +0.103 [+0.023, +0.177] | 0.738 |
| replies | 18 | 134 (42) | 0.718 | 0.591 | 0.681 | +0.127 [+0.022, +0.235] | 0.726 |

- *Across windows:* the gain is positive in 12 of 12 measure-by-window cells (+0.003 to +0.096); 11 have a raw permutation p below 0.05 and 8 after Holm over these 12 cells (within size quintiles: 10 and 7). The gain grows with the window (the long windows keep only the longer-lived podlings: 134 to 137 at 18 months).
- *Direction, at a given size and mean:* the standardised logistic coefficient of each concentration measure when added alone to {ln n, ln mean}, with a bootstrap 95% interval (positive: more of it goes with graduation). The raw AUCs of the top-k shares are below 0.5 only because they fall with n; given n they point the other way.

| measure | window | Gini | top-1 share | top-3 share | Theil | entropy |
|---|---|---|---|---|---|---|
| messages | 12 | +0.32 [-0.10, +0.86] | +0.66 [+0.14, +1.31] | +1.43 [+0.81, +2.47] | +1.02 [+0.36, +1.89] | -0.45 [-0.92, +0.03] |
| messages | 18 | +0.66 [+0.21, +1.29] | +0.59 [-0.01, +1.23] | +2.33 [+1.36, +3.73] | +1.15 [+0.57, +2.00] | -0.63 [-1.20, -0.21] |
| dev_messages | 12 | +0.40 [-0.02, +0.95] | +0.66 [+0.14, +1.40] | +1.51 [+0.86, +2.56] | +1.09 [+0.48, +1.96] | -0.53 [-1.04, -0.08] |
| dev_messages | 18 | +0.66 [+0.22, +1.30] | +0.58 [-0.01, +1.18] | +2.30 [+1.23, +3.82] | +1.11 [+0.55, +1.99] | -0.62 [-1.30, -0.14] |
| replies | 12 | +0.69 [+0.19, +1.45] | +0.82 [+0.27, +1.50] | +2.01 [+1.26, +3.02] | +1.48 [+0.81, +2.28] | -0.72 [-1.42, -0.24] |
| replies | 18 | +0.87 [+0.35, +1.53] | +0.66 [+0.11, +1.44] | +2.70 [+1.55, +4.64] | +1.38 [+0.80, +2.51] | -0.82 [-1.58, -0.34] |

30 of the 30 coefficients point to concentrated conversation going with graduation (a positive Gini, top-k share and Theil, a negative entropy), and 25 of the 30 intervals exclude zero. They are not independent confirmations: three overlapping measures, two nested windows and five correlated shape measures on the same podlings.

- *Size (post hoc):* split at its median (15 members), the development-list gain at 12 months is +0.023 at or below it (102 podlings, 34 retired; p = 0.060; raw Gini AUC 0.64) and +0.100 above it (97, 11 retired; p = 0.013; raw Gini AUC 0.77): larger in the larger projects, as the combined measure's interaction in section 4 is, on few retired podlings.

- *Era:* messages: gain -0.02 for podlings started 2003-2012 (p = 0.38) and +0.07 for 2013-2021 (p = 0.030); dev_messages: gain -0.02 for podlings started 2003-2012 (p = 0.31) and +0.08 for 2013-2021 (p = 0.013); replies: gain +0.00 for podlings started 2003-2012 (p = 0.17) and +0.05 for 2013-2021 (p = 0.047). Two cohorts of about a hundred podlings each and 20 to 26 retired: the contrast is itself within noise, and the gain sits in the later half. A possible reason, not tested: in 2013-2021 more of the discussion had moved to trackers and pull requests, so the list is a smaller and more selective channel. The lead may then measure workflow (how much of the conversation still sits on the list) rather than group structure.
- *Robots:* messages: -0.008 with robots kept, +0.010 with the most active pseudonym also dropped; dev_messages: -0.001 with robots kept, +0.012 with the most active pseudonym also dropped; replies: -0.006 with robots kept, +0.024 with the most active pseudonym also dropped. The effect needs the automated mail removed, which is what the human distribution is; but it also shrinks when the most active human voice goes, so it rests on the top of the distribution.
- *Why the combined measure shows less:* commits alone show no gain (-0.015), and the combined count sums two different distributions (many people with a few commits; a few voices on the list). The combined measure's gain is +0.000 at 12 months and +0.028 at 18 (p = 0.026). Whether a pooled measure should be the algebra's activity variable is the question this lead raises.
- *Multiplicity:* Holm over the 33 distinct tests of 7.2 gives p = 0.13 for the development-list cell at 12 months; Holm over the 12 cells above does the rest. Neither is the right correction for a search whose size is not known; the honest reading is that the lead is nominally strong, consistent in sign across windows and measures, era-dependent and not confirmed.
- *What would confirm it.* Podlings that started after July 2021 (their lists are public), a rule written first (development-list messages, automated senders removed, W = 12 and 18, Gini, top-3 share and entropy added to size and mean, gain above 0.02 AUC with a one-sided permutation p below 0.05), and the same code. The era dependence says to expect it only if the later podlings resemble 2013-2021.

## 8. What this test cannot say

- **A proxy for the team half of section 7, not the test.** The outcome is dissolution against a success exit (L4632); no tie signs, no anchoring, no enemy weights. Whatever happens here, the certificate (kappa(G) >= 2 and w_i > 2E_i) is not touched.
- **The Incubator is an institution.** Mentors, reviews and the Board decide exits; retirement is often an administrative closing of a project that went quiet long before, and the graduation date is a vote. Both leave their mail in the last month.
- **Activity is not effort.** Commits count revisions, not work; messages on human lists miss the discussion that happens in the tracker (the robots carry 43% of the messages on those lists, and the human comments on them arrive under the robot's address). Commits alone leave 133 podlings with three regular committers against 201 for events, and show no shape gain (-0.015).
- **Identity.** One pseudonym per address: a person with two addresses is two members, and a committer who posts from a private address is not joined to her commits. This inflates n and lowers concentration, probably more for long-lived projects.
- **"Team" is a window choice** (117). The rule used, active in a quarter of the window's months, is arbitrary; section 7 varies it: the size effect is stable across the rules, the interaction is not.
- **Small numbers.** 47 retired podlings in the primary analysis, fewer in later windows and in size bands; intervals are wide, and the 42 variants are exploratory. The per-band AUCs in section 4 and the within-half gains are post hoc.
- **Selection.** The files hold podlings that resolved by mid-2021 (the dataset is conditioned on the label), so the "at risk" group at month 12 is conditioned on having lasted that long and on being resolved; the 62 podlings that exited earlier are in section 6 only. Podlings still incubating in 2021 are absent, so the retired fraction (24%) is that of a closed cohort.
- **Reflexivity.** The sustainability papers and the Incubator's own reporting use activity measures like these; a podling that knows it is monitored may produce activity for the monitors. Not tested.
- **Early warning needs finer data and a collapse date.** Section 5.3: the monthly series are too short for the indicators; the weekly ones have power only against a strong signal; the exit date is not the collapse date; the level trend swamps the indicators.

## Reproduce

    cd sim
    ~/.local/bin/uv run python -m models.apache_activity_survival fetch    # once; checks md5, writes to git-ignored data/apache-incubator/
    ~/.local/bin/uv run python -m models.apache_activity_survival build    # once; about 3 minutes; derived/ holds integers only
    ~/.local/bin/uv run python -m models.apache_activity_survival report   # rewrites this file (about 12 minutes; a ## Review section is kept)
    ~/.local/bin/uv run pytest tests/test_apache_activity_survival.py

## Review (2026-11-01)

An independent review of the module, the tests and this file after the first version was written. Nothing was committed.

**What was re-run.** The test file passed 49 of 49 tests before any change and 53 of 53 after (four tests added). The full `report` run (12 minutes, same seed) reproduces every number of the first version to the printed digit. What changed is text, the Holm column of 7.2 and some added columns.

**Re-derived independently.** A separate script has its own loader (the derived arrays and podlings.xml), its own list and robot rules written from `HUMAN_LIST_RULE` and the relay rule, its own landmark table, and its own ridge-logistic cross-validation (scipy L-BFGS, other folds and seeds). It gives:
- labels: 269 of 275 names matched, 205 graduated and 64 retired;
- robots: 893, 1 of them by the relay rule;
- at risk at month 12: 207 (155 / 52); with at least 3 regular members: 201 (154 / 47); median n 20 (quartiles 12, 39);
- raw AUCs of size, mean and Gini: 0.769, 0.599, 0.600, as printed;
- held out: size 0.761 (here 0.758), mean 0.586 (0.580), shape gain +0.001 (-0.000);
- likelihood ratio 5.29 on 4 df, p = 0.26; interaction 15.85 on 2 df;
- the size bands, and the growth table with its Fisher p (0.0005);
- development lists: a gain of +0.040 at 12 months and +0.089 at 18 (here +0.037 and +0.096).

The module's landmark tables match the independent ones row by row. The md5s of both zips and the sha256 of podlings.xml match the recorded values.

**The null.** It is implemented as described, but it is not quite the null the hypothesis states. "Shape adds nothing given size and mean" keeps the shape-size correlation (rho = +0.30; the top-k shares fall with n), and a free permutation breaks it. Three nulls keep it: permutation within size quintiles; residual permutation after regressing the shape block on size and mean; and a parametric bootstrap of the outcome from the base model. With 300 draws each (p in the order free, quintiles, residual, bootstrap):
- primary: 0.22, 0.19, 0.24, 0.19;
- development lists, 12 months: 0.003, 0.010, 0.003, 0.010;
- development lists, 18 months: 0.003 under all four;
- messages: 0.027, 0.010, 0.017, 0.010;
- replies: 0.003, 0.003, 0.003, 0.007.

The free null always has the lowest mean gain (for the development lists -0.017, against -0.012 to -0.005), but p moves in both directions and no decision changes. The within-quintile p is now computed by `size_strata` and printed beside the pre-specified free p; the decision rule is unchanged.

The exchangeable-member reference gives each member one event, where a regular member has at least three. Its Gini of 0.08 is therefore if anything too high, and the comparison stands.

**Leakage.** None found. Features use months [0, W) and the at-risk rule is exit month >= W. Scaling is fitted in the training folds. The survival form and the member panel hold out whole podlings. The early-warning series end before the reference month, and the member panel uses months up to t only. Two checks were added:
- *Exit-process mail inside the window* (votes and resolutions precede the exit date). Dropping the podlings that exit within 0, 3 or 6 months of the landmark: size AUC 0.761, 0.748, 0.710; shape gain -0.000, +0.004, -0.007; the development-list lead +0.037, +0.035, +0.030 (p = 0.005, 0.005, 0.030), and +0.096, +0.103, +0.093 at 18 months.
- *Coverage* (new in section 1). The commit file starts on 2005-01-30, so 9 of the 207 podlings at risk have no commits for some or all of their first year (median regular committers 0 against 4; 4 of the 9 retired). Without them nothing changes: size 0.753, shape gain -0.005, interaction p < 0.001, lead +0.035. The first version did not say so.

**Multiple comparisons.**
- The Holm correction over the 7.2 grid counted 42 rows. Nine are one test (the primary's: same table, block and penalty), and one is no test at all: the one-event share is 0 for every regular member. Over the 33 distinct tests, the development-list cell's Holm p is 0.13 (0.17 before). The conclusion is the same.
- "The interaction is significant in 36 of 42 variants": 23 of those rows use the primary's table and are one unpenalised test. The true count is 14 of 20 distinct tables.
- The verdict cited p = 0.035 for falling variance within retired projects as a finding. It is one of 16 within-project tests, in a weekly design added after the power check (Holm 0.56).
- Section 7.1 read the differences between forms against the Hanley-McNeil s.e. of a single AUC, and concluded that no form is separated from size alone. Paired on the same podlings, size + Gini + Gini x size beats size alone by +0.013 (+0.002 to +0.024). It is the best of 12 forms, so the edge is biased upward. The table now has the paired column.

**Terms and personal data.** The data are used as `sim/data/README.md` records:
- CC BY 4.0 credit is in section 1;
- this file holds only counts, AUCs and p-values;
- the derived arrays hold integers and booleans;
- nothing under `sim/data/` is tracked except its README;
- no address or name appears in this file, the module or the tests (the tests' addresses are invented examples).

One mismatch was fixed. The loader also read podlings.xml's `sponsor` attribute (the sponsoring committee's name, never used), where the README says only status, dates and names are read. That read is removed.

**Ledger ids.** Every cited id exists and says what the text uses it for: L4623-L4633, L4666, L1225, L1831, L5779, L5740, L0512, L0527, L0547, L3057, L1404-L1406, L5742, L4367, L5764. The cited sections exist too: `models/00-v0.md` 0.6 rule 5, section 7 "Team" and section 8 item 5; `models/02-our-claims.md` 1.1 and 1.4; 117 sections 4.3, 5.2 and 5.3; 027 section I; 030 F3. Three corrections:
- the APEX count is L4629 (L4630 is the contradiction it feeds);
- a test docstring read L5779 as an effect that flips with size; it flips with the return;
- the header placed L4666 in 117 section 4.3; it comes from sections 0 and 8.

**Verdict text brought into line with the numbers.**
- (1) "The mean does not predict graduation" is now "not told apart from chance" (0.58, 0.48 to 0.68; 0.69 in the podlings started 2003-2012). The not-supported claim now covers the shape as an added block, since its interaction with size is supported.
- (2) The pre-specified 2-df interaction also included mean x ln n. Taken one term at a time, Gini x ln n carries it (13.7 on 1 df, p < 0.001; mean x ln n p = 0.35), so "concentration's association changes with size" stands. "Only in the larger projects" came from a post hoc split but was stated as supported, while Status called it undecided. It is now marked post hoc.
- (3) The within-project variance result is now marked nominal (see Multiple comparisons).
- D1 against D2: "coupling adds nothing; the term goes" is now "a mean-field coupling proxy adds nothing material". v0's rule names tie-based coupling and who leaves; this test used the others' activity share and next month's activity (117 section 5.3). The tie-based test has not been run.
- Status said the lead "is also stronger in the larger projects", with no computation behind it. It is now computed, post hoc: +0.100 above the median of 15 members (11 retired), against +0.023 at or below it.
- Section 4 said the reversal in the 5 to 7 band "is what noise does not explain". That band holds 17 podlings, its interval reaches 0.47, and it is one of 12 within-band AUCs.

**Bugs fixed.**
- A string in section 4 lacked its f prefix and printed code instead of "6 to 18".
- Section 6 hard-coded the retirees' median exit as 29 months; section 1 computes 30.
- The two dynamics rows of 7.2 printed the primary's shape test and never their own result. Their result is now printed.
- The writer now keeps this section when the file is regenerated.

New tests cover the size strata, the test family, a scan of this file for unformatted fields, and the coverage check. The data tests now also assert the one-term split of the interaction and the within-quintile p of the lead.

**Verdict after review.** No finding is reversed:
- For commits plus messages, the shape of the activity distribution adds nothing to size and mean for graduation (gain -0.000; p 0.17 to 0.24 under four nulls).
- Size predicts graduation (AUC 0.76).
- First-year growth separates the outcomes.
- A smooth rise with size beats a critical-mass step.
- Early-warning signals are not found, and the monthly test had no power to find them.
- The size interaction holds, and the Gini term carries it.
- The conversation lead survives the choice of null, the exit-process mail and the coverage gap. It is still a lead: Holm p = 0.13 over the grid's 33 distinct tests, and absent before 2013.

The first version claimed more than its numbers in six places (the six items under "Verdict text" above). Those are now in line.
